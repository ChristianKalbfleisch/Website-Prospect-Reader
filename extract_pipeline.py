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

Usage:
    python3 extract_pipeline.py staging/run_2026-08-04.json
    python3 extract_pipeline.py --check          # QC + status report only
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
    "source_file",
    "date_captured",
    "status",
    "notes",
]

# Fields that carry real extracted data. source_file / date_captured / status /
# notes are accumulated rather than merged cell-by-cell. recent_news and
# news_source_urls are excluded too: unlike the other detail fields they're
# expected to change over time (new corporate-action news on a later run),
# so they need append-style handling like notes, not blank-fill-once-and-
# conflict semantics. No stage-3 runner exists yet to drive that logic —
# add it there when it's actually built, not speculatively here.
DATA_FIELDS = COLUMNS[:15]

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


def save_rows(rows: list[dict]) -> None:
    WORKBOOK.parent.mkdir(parents=True, exist_ok=True)
    wb = Workbook()
    ws = wb.active
    ws.title = SHEET
    ws.append(COLUMNS)

    head_fill = PatternFill("solid", fgColor="1F3B4D")
    for cell in ws[1]:
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = head_fill
        cell.alignment = Alignment(vertical="center")

    for row in rows:
        ws.append([row.get(c) for c in COLUMNS])

    widths = {
        "company_name": 34, "revenue_raw": 13, "revenue_usd_millions": 20,
        "street_address": 28, "city": 14, "province": 18, "postal_code": 12,
        "country": 10, "key_principal": 22, "key_principal_title": 20,
        "contact_email": 28, "contact_phone": 18,
        "website": 24, "industry_tags": 46, "company_description": 62,
        "recent_news": 60, "news_source_urls": 40,
        "source_file": 34, "date_captured": 14, "status": 14, "notes": 60,
    }
    for i, col in enumerate(COLUMNS, start=1):
        ws.column_dimensions[get_column_letter(i)].width = widths.get(col, 18)

    ws.freeze_panes = "A2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(COLUMNS))}{ws.max_row}"
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


def append_note(row: dict, note: str) -> None:
    if not note:
        return
    existing = str(row.get("notes") or "").strip()
    parts = [p.strip() for p in existing.split(";") if p.strip()]
    if note not in parts:
        parts.append(note)
    row["notes"] = "; ".join(parts)


def merge(existing: list[dict], incoming: list[dict]) -> tuple[list[dict], dict]:
    index = {normalize(r.get("company_name", "")): r for r in existing}
    stats = {"added": 0, "updated": 0, "conflicts": [], "unchanged": 0}

    for new in incoming:
        key = normalize(new.get("company_name", ""))
        source = new.get("source_file", "")
        page_type = new.pop("_page_type", "")

        if key not in index:
            row = {c: new.get(c) for c in COLUMNS}
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
                conflict = f"CONFLICT: {field}={current}|{incoming_val} ({source})"
                append_note(row, conflict)         # keep original, record clash
                stats["conflicts"].append(f"{row['company_name']}: {conflict}")
                changed = True

        for note in [n.strip() for n in str(new.get("notes") or "").split(";") if n.strip()]:
            if not note.startswith("CONFLICT:"):
                append_note(row, note)
                changed = True

        sources = [s.strip() for s in str(row.get("source_file") or "").split(";") if s.strip()]
        if source and source not in sources:
            sources.append(source)
            row["source_file"] = "; ".join(sources)
            changed = True

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

    if "--check" in args:
        flags = quality_checks(rows)
        print(f"rows={len(rows)} status={status_counts(rows)}")
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

    rows, stats = merge(rows, incoming)
    flags = quality_checks(rows)

    for row in rows:
        row.pop("_seen", None)
    save_rows(rows)

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
