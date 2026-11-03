# Website Prospect Reader — D&B Mining (NAICS 21), Vancouver BC

Maintains a single master workbook of Mining, Quarrying, and Oil and Gas
Extraction companies in Vancouver, British Columbia, transcribed from
screenshots of the Dun & Bradstreet Business Directory.

## Layout

```
screenshots/listing/   # directory results table (COMPANY / LOCATION / SALES REVENUE)
screenshots/detail/    # individual company Overview pages
staging/               # per-run JSON transcriptions (the vision step's output)
output/mining_master.xlsx
output/extraction_log.md
extract_pipeline.py    # merge + quality checks + logging (the deterministic step)
```

## Why two steps

Reading a screenshot is a vision task; merging is a rules task. Splitting them
keeps the rules testable and makes a re-run safe:

1. **Transcribe.** Read each unprocessed file in `screenshots/` and write what
   is *legibly printed* into a staging JSON. Nothing is inferred. A field that
   is obscured, cut off, or paywalled is left `null` with the reason recorded
   in `notes` (`ILLEGIBLE: <field> — <reason>`). Partial numbers are never
   transcribed.
2. **Merge.** `python3 extract_pipeline.py staging/<file>.json` merges into the
   workbook, runs the quality checks, and appends a run entry to the log.

Filenames listed in the log are treated as processed and skipped on re-run, so
running the same payload twice adds nothing.

## Staging JSON format

```json
{
  "run_date": "2026-08-04",
  "run_source": "free-text provenance",
  "files_processed": ["listing_p1.png"],
  "rows": [
    {
      "_page_type": "listing",          // "listing" | "detail" | "people"
      "company_name": "Teck Resources Limited",
      "revenue_raw": "$1,802M",
      "revenue_usd_millions": 1802,
      "city": "Vancouver",
      "province": "British Columbia",
      "country": "Canada",
      "source_file": "listing_p1.png",
      "date_captured": "2026-08-04",
      "notes": ""
    }
  ]
}
```

Only `company_name` and `source_file` are required; omit or `null` anything not
legibly printed.

A `"people"` row is an edge in the relationship graph rather than a company:
`person_name`, `company_name`, `role`, `role_type` (`officer|director|both`),
`role_start`, `role_end`, `as_of_date`, `confidence`
(`tier1_filing|tier2_website|registry`), `source_type`, `source_url`, `notes`.
One payload may mix all three `_page_type` values.

## Workbook sheets

- **Companies** — one row per company. The deliverable.
- **People** — append-only edge list, one row per `(person, company, role)`
  assertion. Source of truth for the relationship graph.

`co_located_with`, `related_companies` and `management_group` on Companies are
*derived* from the People sheet plus verified addresses and are recomputed on
every merge. Never hand-edit them; `--derive` recomputes on demand.

See `CLAUDE.md` for the source hierarchy, entity-resolution rules and the
officer-over-director weighting that govern how edges are collected.

## Merge rules

Rows are matched on a normalized name: lowercased, punctuation stripped, and
trailing `ltd|limited|inc|corp|corporation|ulc|co` removed.

- New name → append a row.
- Existing name, blank cell → fill it.
- Existing name, populated cell with a different value → **keep the original**,
  append `CONFLICT: field=old|new (source_file)` to `notes`, and surface it in
  the run summary.

Rows are never deleted or overwritten.

## Quality checks

Run on every merge and reportable on demand with `--check`:

- `revenue_usd_millions` negative or above 100,000
- `postal_code` not matching the Canadian `A1A 1A1` pattern
- `key_principal` containing corporate tokens (looks like an entity, not a person)
- duplicate normalized names that were not merged

On the People sheet: edges missing a `source_url`, an unrecognised `confidence`
tier or `role_type`, a `company_name` that is neither a row nor a registered
former name, a person name that looks corporate, and any person asserted as an
officer of more than six companies at once (usually two people collapsed by
normalisation rather than a real finding).

Flags are reported, never silently corrected.

## Reserved delimiter

`"; "` separates items in `notes`, `source_file`, `recent_news`,
`news_source_urls` and `former_names`. A single value written into one of those
must not contain a semicolon — it would be read back as two items, so a value
the pipeline constructs (such as a `CONFLICT:` note embedding a source string)
is passed through `sanitize_item()` first. Skipping that step made re-runs
append a fresh copy of the same note every time and grow the cell without
bound.

## Known field caveats

- **Revenue is listing-only.** On a company's Overview page revenue sits behind
  a lock icon. Capture it from the results table or not at all.
- **The live-chat widget covers the SALES REVENUE column.** Dismiss the D&B
  chat bubble and the floating phone-number button before capturing a listing
  screenshot, or the rightmost column is unreadable.
- **Province spelling differs by page type.** The listing prints
  `British Columbia`; the detail page prints `BC`. This trips the conflict rule,
  which is working as intended — the first value captured wins and the clash is
  logged.

## Network access

The live site is not reachable from the automated environment: the network
policy denies `www.dnb.com:443` (verified via `curl`, `WebFetch`, and headless
Chromium). This pipeline reads screenshots only.
