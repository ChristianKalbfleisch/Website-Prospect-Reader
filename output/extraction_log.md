# Extraction Log

One entry per run. Filenames in backticks are
treated as already processed and are skipped on re-run.

## Run 2026-08-04

**Source:** Two example screenshots pasted into the chat session (NOT files in ./screenshots/ — those directories are empty). Filenames below are provenance labels assigned at transcription time.

**Files processed:**
- `chat-example-listing-01.png`
- `chat-example-detail-newmont-01.png`

- Rows added: 3
- Rows updated: 1
- Rows unchanged: 0
- Conflicts: 1
  - Newmont Corporation: CONFLICT: province=British Columbia|BC (chat-example-detail-newmont-01.png)
- ILLEGIBLE flags: 3
  - Newmont Corporation: ILLEGIBLE: revenue_raw — SALES REVENUE column obscured by D&B live-chat widget overlay
  - Teck Resources Limited: ILLEGIBLE: revenue_raw — SALES REVENUE column obscured by D&B live-chat widget overlay
  - First Quantum Minerals Ltd: ILLEGIBLE: revenue_raw — value partially covered by the floating phone-number button
- Quality flags: 0

**Running total:** 3 unique companies — {'complete': 1, 'listing_only': 2}

**Notes:** Live site https://www.dnb.com/... is unreachable from this environment (network policy denies www.dnb.com:443 — verified via curl, WebFetch and headless Chromium). No pages were browsed. On the listing screenshot the SALES REVENUE column is covered by the D&B live-chat widget, so no revenue value was legible for any of the three visible rows.

## Run 2026-08-05

**Source:** Five listing-page screenshots pasted into the chat session (NOT files in ./screenshots/ — filenames below are provenance labels assigned at transcription time, in the order the screenshots were pasted).

**Files processed:**
- `chat-listing-2026-08-05-01.png`
- `chat-listing-2026-08-05-02.png`
- `chat-listing-2026-08-05-03.png`
- `chat-listing-2026-08-05-04.png`
- `chat-listing-2026-08-05-05.png`

- Rows added: 63
- Rows updated: 3
- Rows unchanged: 0
- Conflicts: 0
- ILLEGIBLE flags: 3
  - Newmont Corporation: ILLEGIBLE: revenue_raw — SALES REVENUE column obscured by D&B live-chat widget overlay
  - Teck Resources Limited: ILLEGIBLE: revenue_raw — SALES REVENUE column obscured by D&B live-chat widget overlay
  - First Quantum Minerals Ltd: ILLEGIBLE: revenue_raw — value partially covered by the floating phone-number button
- Quality flags: 0

**Running total:** 66 unique companies — {'complete': 1, 'listing_only': 65}

**Notes:** Screenshot 5 is cut off mid-list (page shows a total count badge partially obscured, '(83x' overlapping the corner); rows visible above the fold were transcribed, nothing below the visible cutoff was inferred.
