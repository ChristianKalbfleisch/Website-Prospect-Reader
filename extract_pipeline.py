#!/usr/bin/env python3
"""Merge transcribed D&B screenshot data into output/mining_master.xlsx.

Split of responsibilities:

  * Transcription is a *vision* step. A human or a vision-capable model reads
    each file in screenshots/{listing,detail}/ and writes what is legibly
    printed into a staging JSON file. Nothing is inferred there.
  * This script is the *deterministic* step. It merges staging JSON into the
    master workbook, runs the quality checks, and appends the run log.

Keeping them apart means the merge rules are testable and a re-run can never
double-count: processed screenshot filenames are recorded in the log.

The workbook has two sheets. "Companies" is one row per company and is the
deliverable. "People" is an append-only edge list, one row per
(person, company, role) assertion, and is the source of truth for the
relationship graph; the co_located_with / related_companies / management_group
columns on Companies are derived from it plus verified addresses, and are
recomputed on every run. Never hand-edit a derived column.

Staging JSON rows carry a `_page_type` of "listing", "detail" or "people".
A single payload may mix them.

Usage:
    python3 extract_pipeline.py staging/run_2026-08-04.json
    python3 extract_pipeline.py --check          # QC + status report only
    python3 extract_pipeline.py --derive         # recompute derived columns
"""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parent
WORKBOOK = ROOT / "output" / "mining_master.xlsx"
LOG = ROOT / "output" / "extraction_log.md"
SHEET = "Companies"
PEOPLE_SHEET = "People"

COLUMNS = [
    "company_name",
    "revenue_raw",
    "revenue_usd_millions",
    "street_address",
    "city",
    "province",
    "postal_code",
    "country",
    "key_principal",
    "key_principal_title",
    "contact_email",
    "contact_phone",
    "website",
    "industry_tags",
    "company_description",
    "recent_news",
    "news_source_urls",
    "former_names",
    "co_located_with",
    "related_companies",
    "management_group",
    "source_file",
    "date_captured",
    "status",
    "notes",
]

# Fields that carry real extracted data, merged blank-fill-once with a conflict
# logged on disagreement. Deliberately excluded:
#   * source_file / date_captured / status / notes — accumulated, not merged.
#   * recent_news / news_source_urls / former_names — expected to grow over
#     time, so they append rather than conflict-check.
#   * DERIVED_FIELDS — recomputed from the People sheet and address clustering
#     on every run. Never merged, never hand-edited.
# Listed explicitly rather than sliced positionally so inserting a column
# cannot silently change merge behaviour.
DATA_FIELDS = [
    "company_name",
    "revenue_raw",
    "revenue_usd_millions",
    "street_address",
    "city",
    "province",
    "postal_code",
    "country",
    "key_principal",
    "key_principal_title",
    "contact_email",
    "contact_phone",
    "website",
    "industry_tags",
    "company_description",
]

# Recomputed by derive_relationships() on every run.
DERIVED_FIELDS = ("co_located_with", "related_companies", "management_group")

# Append-style list fields: (items_field, paired_urls_field_or_None)
ACCUMULATING_FIELDS = (
    ("recent_news", "news_source_urls"),
    ("former_names", None),
)

# Fields where "; " separates items. A value written into one of these on the
# add path must be stored in the same split-and-rejoin form the merge path
# compares against, or a re-run will fail to recognise its own earlier output
# and append a duplicate every time. This bit once: a source_file value with a
# semicolon inside its prose grew the cell on each re-run.
LIST_FIELDS = (
    "notes", "source_file", "recent_news", "news_source_urls", "former_names",
)

# One row per (person, company, role) assertion. The edge list is the source of
# truth for the relationship graph; the Companies sheet only renders it.
PEOPLE_COLUMNS = [
    "person_name",
    "company_name",
    "role",
    "role_type",          # officer | director | both
    "role_start",
    "role_end",
    "as_of_date",
    "confidence",         # tier1_filing | tier2_website | registry
    "source_type",
    "source_url",
    "notes",
]

# Officer-type roles carry far more weight than a non-executive board seat:
# interlocking directorates are near-universal among Vancouver juniors and
# rarely say anything about who controls office space. A shared officer does.
OFFICER_TYPES = {"officer", "both"}

# Suites that are registered/records offices or registered-agent addresses
# rather than operating offices. Companies sharing one of these share a law
# firm, not a business relationship, so the cluster is suppressed.
#
# Keyed by SUITE, not building: excluding a whole tower is too blunt. Cathedral
# Place holds both a law firm acting as registered office AND First Majestic's
# genuine head office, so a building-level exclusion would wrongly drop a real
# co-location. Add entries only with a note on how each was identified.
EXCLUDED_CLUSTER_SUITES = {
    # Gold Royalty Corp lists "1000 Cathedral Place, 925 West Georgia Street"
    # as a Registered and Records Office distinct from its operating office.
    "1000|925 west georgia street",
}

LISTING_FIELDS = {"revenue_raw", "revenue_usd_millions", "city", "province", "country"}
DETAIL_FIELDS = {
    "street_address",
    "city",
    "province",
    "postal_code",
    "country",
    "key_principal",
    "key_principal_title",
    "contact_email",
    "contact_phone",
    "website",
    "industry_tags",
    "company_description",
}

SUFFIXES = ("ltd", "limited", "inc", "corp", "corporation", "ulc", "co")
POSTAL_RE = re.compile(r"^[A-Z]\d[A-Z] \d[A-Z]\d$")

# Tokens that suggest a key_principal cell holds an entity, not a person.
COMPANY_TOKENS = {
    "ltd", "limited", "inc", "corp", "corporation", "ulc", "llc", "llp", "plc",
    "company", "holdings", "group", "partners", "resources", "minerals",
    "mining", "capital", "trust", "associates", "ventures",
}


# --------------------------------------------------------------------------
# normalisation / matching
# --------------------------------------------------------------------------

def normalize(name: str) -> str:
    """Lowercase, strip punctuation, strip one trailing corporate suffix."""
    if not name:
        return ""
    s = re.sub(r"[^\w\s]", " ", name.lower())
    s = re.sub(r"\s+", " ", s).strip()
    parts = s.split()
    while parts and parts[-1] in SUFFIXES:
        parts.pop()
    return " ".join(parts)


def blank(value) -> bool:
    return value is None or (isinstance(value, str) and not value.strip())


def split_list(value) -> list[str]:
    """Semicolon-separated cell -> list of non-empty trimmed items."""
    return [p.strip() for p in str(value or "").split(";") if p.strip()]


def sanitize_item(value) -> str:
    """Make a value safe to store as a single item in a semicolon-joined cell.

    The semicolon is reserved as the item delimiter, so any that appear inside
    a value the pipeline *constructs* must go. Without this, a constructed note
    that embeds a source description containing "; " is split into fragments,
    never matches itself on the next run, and is appended again every time —
    the cell grows without bound.
    """
    return re.sub(r"\s*;\s*", ", ", str(value or "")).strip()


# Honorifics and post-nominals that filings append inconsistently. Stripped for
# matching only — the display name keeps whatever the source printed.
PERSON_NOISE = {
    "mr", "mrs", "ms", "miss", "dr", "prof", "sir",
    "jr", "sr", "ii", "iii", "iv",
    "p geo", "pgeo", "peng", "p eng", "cpa", "ca", "cfa", "icd d", "icdd",
    "mba", "phd", "llb", "qc", "kc", "msc", "bsc", "fcpa", "cma", "cga",
}


def normalize_person(name: str) -> str:
    """Normalise a person name for matching.

    Deliberately conservative: it strips punctuation, honorifics and
    post-nominals but does NOT collapse initials onto full names, because
    "J. Smith" and "John Smith" may be different people. Callers must
    corroborate with a second attribute before treating two records as the
    same person — see the entity-resolution rules in CLAUDE.md.
    """
    if not name:
        return ""
    s = re.sub(r"[^\w\s]", " ", name.lower())
    s = re.sub(r"\s+", " ", s).strip()
    parts = [p for p in s.split() if p not in PERSON_NOISE]
    # Drop multi-token post-nominals ("p geo", "icd d") left as separate words.
    joined = " ".join(parts)
    for noise in sorted(PERSON_NOISE, key=len, reverse=True):
        if " " in noise:
            joined = joined.replace(f" {noise}", "")
    return re.sub(r"\s+", " ", joined).strip()


def _clean_address(value) -> str:
    a = str(value or "").strip().lower()
    if not a:
        return ""
    a = re.sub(r"[.,#]", " ", a)
    # Floor designators are removed together with their number, in both word
    # orders, BEFORE the generic keyword strip below. Doing it after would
    # leave a bare "12th" that never matches "15th", silently splitting one
    # building into several keys — which is exactly how the 1040 West Georgia
    # (Hunter Dickinson) cluster went missing during development.
    a = re.sub(r"\b\d+(?:st|nd|rd|th)?\s*(?:floor|fl)\b", " ", a)
    a = re.sub(r"\b(?:floor|fl)\s*\d+(?:st|nd|rd|th)?\b", " ", a)
    a = re.sub(r"\b(suite|unit|ste|floor|fl|po box|rpo|stn)\b", " ", a)
    a = re.sub(r"\bhastings st w\b", "west hastings street", a)
    a = re.sub(r"\bpender st w\b", "west pender street", a)
    a = re.sub(r"\bgeorgia st w\b", "west georgia street", a)
    a = re.sub(r"\bst\b", "street", a)
    a = re.sub(r"\s+", " ", a).strip()
    # Removing a leading "14th Floor - " leaves a stray separator. No real
    # address begins with one, so stripping is safe — and leaving it in forks
    # one building into two keys.
    return re.sub(r"^[\s\-–,]+", "", a).strip()


def address_building_key(value) -> str:
    """Street-number + street name, with any suite/unit number removed.

    Two companies sharing this are in the same tower — weak evidence on its
    own, since downtown Vancouver towers hold dozens of unrelated tenants.
    """
    a = _clean_address(value)
    if not a:
        return ""
    a = re.sub(r"^\s*[\d\-]+\s*[-–]\s*", " ", a)      # "1830 - 1188 West Georgia"
    tokens = a.split()
    # A trailing bare suite number or bare ordinal ("1188 West Georgia 1830",
    # "550 Burrard Street 11th") is a unit designator, not part of the address.
    # Only stripped when trailing, so a street named "1st Avenue" is untouched.
    if len(tokens) > 2 and re.fullmatch(r"\d+(?:st|nd|rd|th)?", tokens[-1]):
        tokens = tokens[:-1]
    if len(tokens) > 2 and tokens[0].isdigit() and tokens[1].isdigit():
        tokens = tokens[1:]
    return re.sub(r"\s+", " ", " ".join(tokens)).strip()


FLOOR_RE = re.compile(
    r"(?:\b(\d+)(?:st|nd|rd|th)?\s*(?:floor|fl)\b|\b(?:floor|fl)\s*(\d+)(?:st|nd|rd|th)?\b)",
    re.I,
)


def address_suite_key(value) -> str:
    """Full address including its unit designator, unit sorted to the front.

    Two companies sharing this occupy the same suite or the same floor, which is
    strong evidence of a shared management company or corporate-services
    provider. Handles the orderings the same unit appears in across sources
    ("1830 - 1188 West Georgia" and "1188 West Georgia Street 1830").

    A floor counts as the unit when no suite number is given. Discarding floors
    was a real miss: Hunter Dickinson's cluster puts Amarc Resources, Northern
    Dynasty and HDI Acquisition all on the 14th floor of 1040 West Georgia
    while Trekor Metals sits on the 12th, and a floor-blind key cannot tell
    those apart.
    """
    raw = str(value or "")
    a = _clean_address(raw)
    if not a:
        return ""
    building = address_building_key(raw)
    if not building:
        return ""
    suite = re.sub(r"\s+", "", re.sub(r"[-–]", " ", a.replace(building, " ").strip()))
    if not suite:
        match = FLOOR_RE.search(raw)
        if match:
            suite = "f" + (match.group(1) or match.group(2))
    return f"{suite}|{building}" if suite else ""


def build_alias_index(rows: list[dict]) -> dict[str, dict]:
    """Map normalized current *and* former names onto their row.

    Renames are rampant in this sector (Muzhu -> North Atlantic Titanium,
    Benchmark -> Thesis Gold -> Thesis Gold & Silver, and many more), so a
    staging entry that names an entity by an older name must still land on the
    existing row instead of creating a duplicate. Current names always win a
    collision; a former name never overwrites a current one.
    """
    index: dict[str, dict] = {}
    for row in rows:
        for former in split_list(row.get("former_names")):
            key = normalize(former)
            if key and key not in index:
                index[key] = row
    for row in rows:                      # second pass: current names win
        key = normalize(row.get("company_name", ""))
        if key:
            index[key] = row
    return index


# --------------------------------------------------------------------------
# workbook I/O
# --------------------------------------------------------------------------

def load_rows() -> list[dict]:
    if not WORKBOOK.exists():
        return []
    ws = load_workbook(WORKBOOK)[SHEET]
    header = [c.value for c in ws[1]]
    rows = []
    for excel_row in ws.iter_rows(min_row=2, values_only=True):
        if all(blank(v) for v in excel_row):
            continue
        rows.append({h: v for h, v in zip(header, excel_row)})
    return rows


def load_people() -> list[dict]:
    if not WORKBOOK.exists():
        return []
    wb = load_workbook(WORKBOOK)
    if PEOPLE_SHEET not in wb.sheetnames:
        return []
    ws = wb[PEOPLE_SHEET]
    header = [c.value for c in ws[1]]
    people = []
    for excel_row in ws.iter_rows(min_row=2, values_only=True):
        if all(blank(v) for v in excel_row):
            continue
        people.append({h: v for h, v in zip(header, excel_row)})
    return people


HEAD_FILL = PatternFill("solid", fgColor="1F3B4D")

COMPANY_WIDTHS = {
    "company_name": 34, "revenue_raw": 13, "revenue_usd_millions": 20,
    "street_address": 28, "city": 14, "province": 18, "postal_code": 12,
    "country": 10, "key_principal": 22, "key_principal_title": 20,
    "contact_email": 28, "contact_phone": 18,
    "website": 24, "industry_tags": 46, "company_description": 62,
    "recent_news": 60, "news_source_urls": 40,
    "former_names": 30, "co_located_with": 40, "related_companies": 52,
    "management_group": 24,
    "source_file": 34, "date_captured": 14, "status": 14, "notes": 60,
}

PEOPLE_WIDTHS = {
    "person_name": 26, "company_name": 34, "role": 30, "role_type": 12,
    "role_start": 12, "role_end": 12, "as_of_date": 12, "confidence": 16,
    "source_type": 26, "source_url": 52, "notes": 50,
}


def _write_sheet(ws, columns: list[str], rows: list[dict], widths: dict) -> None:
    ws.append(columns)
    for cell in ws[1]:
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = HEAD_FILL
        cell.alignment = Alignment(vertical="center")
    for row in rows:
        ws.append([row.get(c) for c in columns])
    for i, col in enumerate(columns, start=1):
        ws.column_dimensions[get_column_letter(i)].width = widths.get(col, 18)
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(columns))}{ws.max_row}"


def save_rows(rows: list[dict], people: list[dict] | None = None) -> None:
    WORKBOOK.parent.mkdir(parents=True, exist_ok=True)
    wb = Workbook()
    ws = wb.active
    ws.title = SHEET
    _write_sheet(ws, COLUMNS, rows, COMPANY_WIDTHS)

    # The People sheet is written whenever edges exist. It is deliberately a
    # second sheet rather than more columns on Companies: person-to-company is
    # many-to-many and does not flatten into one cell without losing the role,
    # the dates and the provenance that make an edge trustworthy.
    if people:
        _write_sheet(wb.create_sheet(PEOPLE_SHEET), PEOPLE_COLUMNS, people, PEOPLE_WIDTHS)

    wb.save(WORKBOOK)


# --------------------------------------------------------------------------
# merge
# --------------------------------------------------------------------------

def derive_status(row: dict) -> str:
    """A row is complete once it carries data sourced from both page types."""
    has_listing = any(not blank(row.get(f)) for f in ("revenue_raw", "revenue_usd_millions"))
    has_detail = any(not blank(row.get(f)) for f in DETAIL_FIELDS - {"city", "province", "country"})
    seen = {s.strip() for s in str(row.get("_seen") or "").split(",") if s.strip()}
    if "listing" in seen and "detail" in seen:
        return "complete"
    if has_listing and has_detail:
        return "complete"
    if "detail" in seen or has_detail:
        return "detail_only"
    return "listing_only"


def append_note(row: dict, note: str) -> bool:
    """Append a note if it is not already present. Returns True if added.

    The return value matters: without it a re-run of an already-merged staging
    file reports every row as "updated" even though nothing changed, which
    makes the run log lie about what a run actually did.
    """
    if not note:
        return False
    parts = split_list(row.get("notes"))
    if note in parts:
        return False
    parts.append(note)
    row["notes"] = "; ".join(parts)
    return True


def merge_people(existing: list[dict], incoming: list[dict]) -> tuple[list[dict], dict]:
    """Append-only merge of the relationship edge list.

    Edge identity is (person, company, role). A re-run that re-asserts the same
    edge is a no-op; an edge with a different role, or the same role with new
    dates, is a new assertion. Nothing is ever overwritten — a contradicting
    source is recorded as its own edge and surfaced by the quality checks, the
    same principle the Companies merge uses for conflicting fields.
    """
    def edge_key(e: dict) -> tuple[str, str, str]:
        return (
            normalize_person(e.get("person_name", "")),
            normalize(e.get("company_name", "")),
            str(e.get("role") or "").strip().lower(),
        )

    seen = {edge_key(e) for e in existing}
    stats = {"added": 0, "duplicate": 0}
    for new in incoming:
        edge = {c: new.get(c) for c in PEOPLE_COLUMNS}
        key = edge_key(edge)
        if not key[0] or not key[1]:
            continue
        if key in seen:
            stats["duplicate"] += 1
            continue
        edge["as_of_date"] = edge.get("as_of_date") or str(date.today())
        existing.append(edge)
        seen.add(key)
        stats["added"] += 1
    return existing, stats


def _current_edges(people: list[dict]) -> list[dict]:
    """Edges with no recorded end date, i.e. presumed still in force."""
    return [e for e in people if blank(e.get("role_end"))]


def derive_relationships(rows: list[dict], people: list[dict]) -> dict:
    """Recompute co_located_with / related_companies / management_group.

    Fully derived from the edge list plus verified addresses, so it is safe to
    re-run at any time and never needs hand-editing.
    """
    for row in rows:
        for field in DERIVED_FIELDS:
            row[field] = None

    by_key = {normalize(r.get("company_name", "")): r for r in rows}
    stats = {"clusters": 0, "co_located": 0, "same_suite": 0, "linked": 0, "groups": 0}

    # ---- address co-location -------------------------------------------
    # Clustered at building level but *labelled* by precision, because the two
    # are worth very different amounts. Same suite implies a shared management
    # company or corporate-services provider; same building in downtown
    # Vancouver implies nothing at all. Only same-suite matches are allowed to
    # corroborate a management group further down.
    buckets: dict[str, list[dict]] = {}
    for row in rows:
        building = address_building_key(row.get("street_address"))
        if not building or len(building) < 9:
            continue
        if address_suite_key(row.get("street_address")) in EXCLUDED_CLUSTER_SUITES:
            continue
        buckets.setdefault(building, []).append(row)

    address_partners: dict[str, set[str]] = {}
    for building, members in buckets.items():
        if len(members) < 2:
            continue
        stats["clusters"] += 1
        for row in members:
            key = normalize(row.get("company_name", ""))
            suite = address_suite_key(row.get("street_address"))
            others = []
            for other in members:
                if other is row:
                    continue
                other_key = normalize(other.get("company_name", ""))
                other_suite = address_suite_key(other.get("street_address"))
                # Same corporate family (one name is a prefix of the other,
                # e.g. Aris Mining Corporation / Aris Mining Holdings Corp) is
                # not a discovery — label it so it cannot be mistaken for one.
                same_family = key.startswith(other_key) or other_key.startswith(key)
                same_suite = bool(suite) and suite == other_suite
                if same_family:
                    tag = "same family"
                elif same_suite:
                    tag = "same suite"
                    stats["same_suite"] += 1
                else:
                    tag = "same building only"
                others.append(f"{other.get('company_name')} [{tag}]")
                # Corroboration for management_group uses BUILDING level, not
                # suite. A management company routinely spreads its managed
                # entities across several floors of one tower — Hunter Dickinson
                # sits on the 12th, 14th and 15th floors of 1040 West Georgia,
                # so a suite-level test would miss the very pattern this is
                # meant to catch. The shared-officer requirement carries the
                # weight; the address only guards against a lone coincidence.
                if not same_family:
                    address_partners.setdefault(key, set()).add(other_key)
            row["co_located_with"] = "; ".join(sorted(others))
            stats["co_located"] += 1

    # ---- shared people -------------------------------------------------
    person_edges: dict[str, list[dict]] = {}
    for edge in _current_edges(people):
        pkey = normalize_person(edge.get("person_name", ""))
        if pkey:
            person_edges.setdefault(pkey, []).append(edge)

    links: dict[str, list[str]] = {}
    officer_partners: dict[str, set[str]] = {}
    for pkey, edges in person_edges.items():
        companies = {normalize(e.get("company_name", "")): e for e in edges}
        if len(companies) < 2:
            continue
        for ckey, edge in companies.items():
            for other_key, other_edge in companies.items():
                if other_key == ckey:
                    continue
                other_row = by_key.get(other_key)
                display = (
                    other_row.get("company_name") if other_row
                    else other_edge.get("company_name")
                )
                role_type = str(other_edge.get("role_type") or "").lower()
                marker = "officer" if role_type in OFFICER_TYPES else "director"
                conf = str(other_edge.get("confidence") or "unverified")
                links.setdefault(ckey, []).append(
                    f"{display} (via {edge.get('person_name')}, {marker}, {conf})"
                )
                if role_type in OFFICER_TYPES and \
                        str(edge.get("role_type") or "").lower() in OFFICER_TYPES:
                    officer_partners.setdefault(ckey, set()).add(other_key)

    for ckey, items in links.items():
        row = by_key.get(ckey)
        if row is None:
            continue
        row["related_companies"] = "; ".join(sorted(set(items)))
        stats["linked"] += 1

    # ---- management groups ---------------------------------------------
    # A management group needs either two shared officers with another member,
    # or one shared officer plus a shared operating office. A shared board seat
    # alone is never enough — that pattern is too common in this sector to mean
    # anything about who controls space.
    officers_of: dict[str, set[str]] = {}
    for edge in _current_edges(people):
        if str(edge.get("role_type") or "").lower() in OFFICER_TYPES:
            ckey = normalize(edge.get("company_name", ""))
            pkey = normalize_person(edge.get("person_name", ""))
            if ckey and pkey:
                officers_of.setdefault(ckey, set()).add(pkey)

    adjacency: dict[str, set[str]] = {}
    for ckey, partners in officer_partners.items():
        for other in partners:
            shared = len(officers_of.get(ckey, set()) & officers_of.get(other, set()))
            co_located = other in address_partners.get(ckey, set())
            if shared >= 2 or (shared >= 1 and co_located):
                adjacency.setdefault(ckey, set()).add(other)
                adjacency.setdefault(other, set()).add(ckey)

    visited: set[str] = set()
    for ckey in sorted(adjacency):
        if ckey in visited:
            continue
        stack, component = [ckey], []
        while stack:
            cur = stack.pop()
            if cur in visited:
                continue
            visited.add(cur)
            component.append(cur)
            stack.extend(adjacency.get(cur, set()) - visited)
        if len(component) < 2:
            continue
        stats["groups"] += 1
        label_row = max(
            (by_key[c] for c in component if c in by_key),
            key=lambda r: float(r.get("revenue_usd_millions") or 0),
            default=None,
        )
        label = f"group: {label_row.get('company_name')}" if label_row else f"group {stats['groups']}"
        for c in component:
            if c in by_key:
                by_key[c]["management_group"] = label

    return stats


def merge(existing: list[dict], incoming: list[dict]) -> tuple[list[dict], dict]:
    index = build_alias_index(existing)
    stats = {"added": 0, "updated": 0, "conflicts": [], "unchanged": 0}

    for new in incoming:
        key = normalize(new.get("company_name", ""))
        source = new.get("source_file", "")
        page_type = new.pop("_page_type", "")

        if key not in index:
            row = {c: new.get(c) for c in COLUMNS}
            for field in LIST_FIELDS:                  # canonical round-trip form
                if not blank(row.get(field)):
                    row[field] = "; ".join(split_list(row[field]))
            row["_seen"] = page_type
            row["date_captured"] = new.get("date_captured") or str(date.today())
            row["status"] = derive_status(row)
            existing.append(row)
            index[key] = row
            stats["added"] += 1
            continue

        row = index[key]
        changed = False

        for field in DATA_FIELDS:
            incoming_val = new.get(field)
            if blank(incoming_val):
                continue
            current = row.get(field)
            if blank(current):
                row[field] = incoming_val          # fill only blanks
                changed = True
            elif str(current).strip() != str(incoming_val).strip():
                conflict = sanitize_item(
                    f"CONFLICT: {field}={current}|{incoming_val} ({source})"
                )
                if append_note(row, conflict):     # keep original, record clash
                    changed = True
                # Reported every run, even when the note is already present:
                # the disagreement is still live and a reader of the log should
                # see it. Only `changed` is gated, so a re-run does not claim
                # to have modified rows it left untouched.
                stats["conflicts"].append(f"{row['company_name']}: {conflict}")

        for note in split_list(new.get("notes")):
            if not note.startswith("CONFLICT:") and append_note(row, note):
                changed = True

        # Append-style fields (news items, former names). These are expected to
        # grow across runs, so a second value is an addition rather than a
        # conflict. Where a paired field exists (news -> source URLs) the two
        # lists are kept aligned by position.
        for field, paired in ACCUMULATING_FIELDS:
            incoming_items = split_list(new.get(field))
            if not incoming_items:
                continue
            current_items = split_list(row.get(field))
            current_paired = split_list(row.get(paired)) if paired else []
            incoming_paired = split_list(new.get(paired)) if paired else []
            for i, item in enumerate(incoming_items):
                if item in current_items:
                    continue
                current_items.append(item)
                if paired:
                    current_paired.append(
                        incoming_paired[i] if i < len(incoming_paired) else ""
                    )
                changed = True
            row[field] = "; ".join(current_items)
            if paired:
                row[paired] = "; ".join(current_paired)

        sources = split_list(row.get("source_file"))
        for part in split_list(source):
            if part not in sources:
                sources.append(part)
                changed = True
        if sources:
            row["source_file"] = "; ".join(sources)

        seen = {s for s in str(row.get("_seen") or "").split(",") if s}
        if page_type:
            seen.add(page_type)
        row["_seen"] = ",".join(sorted(seen))
        row["status"] = derive_status(row)

        stats["updated" if changed else "unchanged"] += 1

    return existing, stats


# --------------------------------------------------------------------------
# quality checks
# --------------------------------------------------------------------------

def quality_checks(rows: list[dict]) -> list[str]:
    flags: list[str] = []

    for row in rows:
        name = row.get("company_name", "<unnamed>")

        rev = row.get("revenue_usd_millions")
        if not blank(rev):
            try:
                val = float(rev)
                if val < 0 or val > 100_000:
                    flags.append(f"REVENUE_RANGE: {name} revenue_usd_millions={val}")
            except (TypeError, ValueError):
                flags.append(f"REVENUE_NONNUMERIC: {name} revenue_usd_millions={rev!r}")

        pc = row.get("postal_code")
        if not blank(pc) and not POSTAL_RE.match(str(pc).strip()):
            flags.append(f"POSTAL_FORMAT: {name} postal_code={pc!r} does not match A1A 1A1")

        kp = row.get("key_principal")
        if not blank(kp):
            tokens = {t.strip(".,").lower() for t in str(kp).split()}
            if tokens & COMPANY_TOKENS:
                flags.append(f"PRINCIPAL_LOOKS_CORPORATE: {name} key_principal={kp!r}")

    seen: dict[str, list[str]] = {}
    for row in rows:
        seen.setdefault(normalize(row.get("company_name", "")), []).append(
            row.get("company_name", "")
        )
    for key, names in seen.items():
        if len(names) > 1:
            flags.append(f"UNMERGED_DUPLICATE: normalized={key!r} rows={names}")

    return flags


def people_checks(people: list[dict], rows: list[dict]) -> list[str]:
    """Provenance and plausibility checks on the relationship edge list."""
    flags: list[str] = []
    known = {normalize(r.get("company_name", "")) for r in rows}
    known |= {
        normalize(f) for r in rows for f in split_list(r.get("former_names"))
    }

    for edge in people:
        who = edge.get("person_name") or "<unnamed>"
        what = edge.get("company_name") or "<no company>"
        label = f"{who} @ {what}"

        if blank(edge.get("source_url")):
            flags.append(f"EDGE_NO_SOURCE: {label} has no source_url")
        if str(edge.get("confidence") or "").strip() not in {
            "tier1_filing", "tier2_website", "registry"
        }:
            flags.append(
                f"EDGE_CONFIDENCE: {label} confidence="
                f"{edge.get('confidence')!r} is not a recognised tier"
            )
        if str(edge.get("role_type") or "").strip().lower() not in {
            "officer", "director", "both"
        }:
            flags.append(
                f"EDGE_ROLE_TYPE: {label} role_type={edge.get('role_type')!r}"
            )
        if normalize(what) not in known:
            flags.append(
                f"EDGE_UNKNOWN_COMPANY: {label} — company is not a row in "
                f"{SHEET} and is not listed as a former name"
            )
        tokens = {t.strip(".,").lower() for t in str(who).split()}
        if tokens & COMPANY_TOKENS:
            flags.append(f"EDGE_PERSON_LOOKS_CORPORATE: {label}")

    # A person asserted as an officer of many companies at once is usually a
    # normalisation failure (two different people collapsed) rather than a real
    # finding. Surface it for a human rather than trusting it.
    by_person: dict[str, set[str]] = {}
    for edge in people:
        if blank(edge.get("role_end")) and \
                str(edge.get("role_type") or "").lower() in OFFICER_TYPES:
            by_person.setdefault(
                normalize_person(edge.get("person_name", "")), set()
            ).add(normalize(edge.get("company_name", "")))
    for pkey, companies in by_person.items():
        if len(companies) > 6:
            flags.append(
                f"EDGE_HIGH_DEGREE: {pkey!r} is an officer of {len(companies)} "
                f"companies — verify this is one person, not a name collision"
            )

    # normalize_person() refuses to merge "Robert Dickinson" with
    # "Robert A. Dickinson" because initials genuinely distinguish some people.
    # That is the right default, but it means one person can enter the graph
    # twice under two spellings. Where both variants appear on the SAME company
    # they are almost certainly one person, so surface it for a human instead of
    # merging silently. Resolve with a circular or insider ID, not a guess.
    per_company: dict[str, set[str]] = {}
    for edge in people:
        ckey = normalize(edge.get("company_name", ""))
        pkey = normalize_person(edge.get("person_name", ""))
        if ckey and pkey:
            per_company.setdefault(ckey, set()).add(pkey)
    for ckey, names in per_company.items():
        ordered = sorted(names)
        for i, a in enumerate(ordered):
            at = a.split()
            for b in ordered[i + 1:]:
                bt = b.split()
                if len(at) < 2 or len(bt) < 2 or a == b:
                    continue
                if at[0] == bt[0] and at[-1] == bt[-1] and len(at) != len(bt):
                    flags.append(
                        f"EDGE_NAME_VARIANT: {ckey!r} carries both {a!r} and "
                        f"{b!r} — likely one person recorded twice"
                    )

    return flags


# --------------------------------------------------------------------------
# log
# --------------------------------------------------------------------------

def processed_files() -> set[str]:
    if not LOG.exists():
        return set()
    return set(re.findall(r"^\s*[-*]\s+`([^`]+)`", LOG.read_text(), flags=re.M))


def write_log(entry: str) -> None:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    if not LOG.exists():
        LOG.write_text("# Extraction Log\n\nOne entry per run. Filenames in backticks are\n"
                       "treated as already processed and are skipped on re-run.\n")
    with LOG.open("a") as fh:
        fh.write(entry)


def status_counts(rows: list[dict]) -> dict:
    counts: dict[str, int] = {}
    for row in rows:
        counts[row.get("status") or "unknown"] = counts.get(row.get("status") or "unknown", 0) + 1
    return counts


# --------------------------------------------------------------------------

def main() -> int:
    args = [a for a in sys.argv[1:]]
    rows = load_rows()
    people = load_people()

    if "--check" in args:
        flags = quality_checks(rows) + people_checks(people, rows)
        print(f"rows={len(rows)} people_edges={len(people)} status={status_counts(rows)}")
        print("flags:", *flags, sep="\n  " if flags else " none")
        return 0

    if "--derive" in args:
        # Recompute the relationship columns from the edge list plus verified
        # addresses. Safe to run any time; touches no source data.
        dstats = derive_relationships(rows, people)
        for row in rows:
            row.pop("_seen", None)
        save_rows(rows, people)
        print(f"derived: {dstats}")
        flags = people_checks(people, rows)
        print("flags:", *flags, sep="\n  " if flags else " none")
        return 0

    if not args:
        print(__doc__)
        return 1

    payload = json.loads(Path(args[0]).read_text())
    incoming = payload["rows"]
    already = processed_files()
    files = payload.get("files_processed", [])
    skipped = [f for f in files if f in already]
    if skipped:
        print(f"skipping already-processed: {skipped}")
        incoming = [r for r in incoming if r.get("source_file") not in skipped]

    if not incoming:
        # Every file in this payload was already merged. Do not append a no-op
        # entry to the log — that would make re-runs look like real runs.
        counts = status_counts(rows)
        print(f"nothing new to merge; total={len(rows)} status={counts}")
        return 0

    # A staging payload may carry company rows, relationship edges, or both.
    company_rows = [r for r in incoming if r.get("_page_type") != "people"]
    people_rows = [r for r in incoming if r.get("_page_type") == "people"]

    rows, stats = merge(rows, company_rows)
    people, pstats = merge_people(people, people_rows)
    dstats = derive_relationships(rows, people)
    flags = quality_checks(rows) + people_checks(people, rows)

    for row in rows:
        row.pop("_seen", None)
    save_rows(rows, people)

    counts = status_counts(rows)
    lines = [
        f"\n## Run {payload.get('run_date', date.today())}\n",
        f"\n**Source:** {payload.get('run_source', 'screenshots')}\n",
        "\n**Files processed:**\n",
    ]
    lines += [f"- `{f}`\n" for f in files if f not in skipped] or ["- none\n"]
    lines += [
        f"\n- Rows added: {stats['added']}\n",
        f"- Rows updated: {stats['updated']}\n",
        f"- Rows unchanged: {stats['unchanged']}\n",
        f"- Conflicts: {len(stats['conflicts'])}\n",
    ]
    lines += [f"  - {c}\n" for c in stats["conflicts"]]
    illegible = [
        f"{r['company_name']}: {clause.strip()}"
        for r in rows
        for clause in str(r.get("notes") or "").split(";")
        if "ILLEGIBLE" in clause
    ]
    lines.append(f"- ILLEGIBLE flags: {len(illegible)}\n")
    lines += [f"  - {i}\n" for i in illegible]
    lines.append(f"- Quality flags: {len(flags)}\n")
    lines += [f"  - {f}\n" for f in flags]
    if people_rows or people:
        lines += [
            f"- People edges added: {pstats['added']} "
            f"(duplicates skipped: {pstats['duplicate']}, total: {len(people)})\n",
            f"- Derived relationships: {dstats}\n",
        ]
    lines.append(f"\n**Running total:** {len(rows)} unique companies — {counts}\n")

    if payload.get("run_notes"):
        lines.append(f"\n**Notes:** {payload['run_notes']}\n")

    write_log("".join(lines))

    print(f"added={stats['added']} updated={stats['updated']} "
          f"conflicts={len(stats['conflicts'])} total={len(rows)} status={counts}")
    print("flags:", *flags, sep="\n  " if flags else " none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
