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
      "_page_type": "listing",          // or "detail" — drives the status column
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

Flags are reported, never silently corrected.

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
