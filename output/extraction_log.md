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

## Run 2026-08-05

**Source:** Live fetch of each company's own official investor-relations/contact page (curl, respectful pace, cached). Verified against the primary source only — third-party data-broker sites (RocketReach, LeadIQ, GetProspect, etc.) surfaced in search results were NOT used, since they are unverified scraped aggregations, not the company's own published data.

**Files processed:**
- `https://www.teck.com/investors/contact-us/`
- `https://www.first-quantum.com/contact/`
- `https://www.lundinmining.com/about/contact/`

- Rows added: 0
- Rows updated: 3
- Rows unchanged: 0
- Conflicts: 2
  - First Quantum Minerals Ltd: CONFLICT: province=British Columbia|BC (https://www.first-quantum.com/contact/)
  - Lundin Mining Corporation: CONFLICT: province=British Columbia|BC (https://www.lundinmining.com/about/contact/)
- ILLEGIBLE flags: 5
  - Newmont Corporation: ILLEGIBLE: revenue_raw — SALES REVENUE column obscured by D&B live-chat widget overlay
  - Teck Resources Limited: ILLEGIBLE: revenue_raw — SALES REVENUE column obscured by D&B live-chat widget overlay
  - Teck Resources Limited: ILLEGIBLE: street_address — Vancouver HQ address not present in static HTML (site footer renders address via JavaScript, not fetched).
  - First Quantum Minerals Ltd: ILLEGIBLE: revenue_raw — value partially covered by the floating phone-number button
  - First Quantum Minerals Ltd: ILLEGIBLE: contact_email for Bonita To — no personal email published on official contact page
- Quality flags: 0

**Running total:** 66 unique companies — {'complete': 4, 'listing_only': 62}

**Notes:** Newmont Corporation and B2Gold Corp contact pages returned an active Cloudflare bot-challenge (cf-mitigated: challenge) rather than page content — treated the same as the earlier SEDAR+ active bot-block: not attempted to bypass. Left both companies' contact_email/contact_phone blank for this run rather than use unverified data-broker figures found in search results.

## Run 2026-08-05

**Source:** Live fetch of each company's own official contact page (curl, respectful pace, cached). Data-broker sites not used.

**Files processed:**
- `https://panamericansilver.com/about/contact/`
- `https://capstonecopper.com/contact-us/`
- `https://www.equinoxgold.com/contact/`

- Rows added: 0
- Rows updated: 5
- Rows unchanged: 0
- Conflicts: 3
  - Pan American Silver Corp: CONFLICT: province=British Columbia|BC (https://panamericansilver.com/about/contact/)
  - Capstone Copper Corp: CONFLICT: province=British Columbia|BC (https://capstonecopper.com/contact-us/)
  - Equinox Gold Corp: CONFLICT: province=British Columbia|BC (https://www.equinoxgold.com/contact/)
- ILLEGIBLE flags: 8
  - Newmont Corporation: ILLEGIBLE: revenue_raw — SALES REVENUE column obscured by D&B live-chat widget overlay
  - Teck Resources Limited: ILLEGIBLE: revenue_raw — SALES REVENUE column obscured by D&B live-chat widget overlay
  - Teck Resources Limited: ILLEGIBLE: street_address — Vancouver HQ address not present in static HTML (site footer renders address via JavaScript, not fetched).
  - First Quantum Minerals Ltd: ILLEGIBLE: revenue_raw — value partially covered by the floating phone-number button
  - First Quantum Minerals Ltd: ILLEGIBLE: contact_email for Bonita To — no personal email published on official contact page
  - Pan American Silver Corp: ILLEGIBLE: contact_email — page uses email obfuscation (renders as '*protected email*' in fetched HTML rather than an address)
  - Capstone Copper Corp: ILLEGIBLE: contact_email — page uses email obfuscation ('[email protected]' placeholder in fetched HTML)
  - Wheaton Precious Metals Corp: ILLEGIBLE: contact_email, contact_phone — wheatonpm.com contact page returned an active Cloudflare bot-challenge (cf-mitigated: challenge)
- Quality flags: 0

**Running total:** 66 unique companies — {'complete': 7, 'listing_only': 57, 'detail_only': 2}

**Notes:** 2 of 5 in this batch (Yamana, Wheaton) yielded no contact data — one due to an expired TLS cert on the company's own domain (declined to connect insecurely), one due to active Cloudflare bot-challenge (declined to bypass).

## Run 2026-08-05

**Source:** Mix of direct official-page fetches and, where the live page returned a 403, the company's own official-domain content as surfaced in search-engine result snippets (never third-party data-broker sites). Provenance noted per-row.

**Files processed:**
- `https://www.ero.com/contact-us/`
- `https://www.glencore.ca/en/evr`
- `https://www.chinagoldintl.com/contact/`
- `https://lundingold.com/contact/`
- `https://oceanagold.com/contact-us`

- Rows added: 0
- Rows updated: 8
- Rows unchanged: 0
- Conflicts: 6
  - Eldorado Gold Corporation: CONFLICT: province=British Columbia|BC (eldoradogold.com/contact-us (live fetch 403'd; sourced from search-engine snippet of the company's own official page, not a data broker))
  - OceanaGold Corporation: CONFLICT: province=British Columbia|BC (https://oceanagold.com/contact-us)
  - Lundin Gold Inc: CONFLICT: province=British Columbia|BC (https://lundingold.com/contact/)
  - Fortuna Mining Corp: CONFLICT: province=British Columbia|BC (fortunamining.com/contact/ (live fetch 403'd; sourced from search-engine snippet of the company's own official page))
  - Ero Copper Corp: CONFLICT: province=British Columbia|BC (https://www.ero.com/contact-us/)
  - China Gold International Resources Corp Ltd: CONFLICT: province=British Columbia|BC (https://www.chinagoldintl.com/contact/)
- ILLEGIBLE flags: 10
  - Newmont Corporation: ILLEGIBLE: revenue_raw — SALES REVENUE column obscured by D&B live-chat widget overlay
  - Teck Resources Limited: ILLEGIBLE: revenue_raw — SALES REVENUE column obscured by D&B live-chat widget overlay
  - Teck Resources Limited: ILLEGIBLE: street_address — Vancouver HQ address not present in static HTML (site footer renders address via JavaScript, not fetched).
  - First Quantum Minerals Ltd: ILLEGIBLE: revenue_raw — value partially covered by the floating phone-number button
  - First Quantum Minerals Ltd: ILLEGIBLE: contact_email for Bonita To — no personal email published on official contact page
  - Pan American Silver Corp: ILLEGIBLE: contact_email — page uses email obfuscation (renders as '*protected email*' in fetched HTML rather than an address)
  - Capstone Copper Corp: ILLEGIBLE: contact_email — page uses email obfuscation ('[email protected]' placeholder in fetched HTML)
  - Wheaton Precious Metals Corp: ILLEGIBLE: contact_email, contact_phone — wheatonpm.com contact page returned an active Cloudflare bot-challenge (cf-mitigated: challenge)
  - EVR Operations Limited: ILLEGIBLE: street_address.
  - China Gold International Resources Corp Ltd: ILLEGIBLE: contact_email — page uses email obfuscation ('[email protected]' placeholder)
- Quality flags: 0

**Running total:** 66 unique companies — {'complete': 14, 'listing_only': 49, 'detail_only': 3}

**Notes:** Two rows (Eldorado, Fortuna) sourced from search-engine snippets of the company's own official page because the live page itself 403'd on fetch — flagged per-row rather than treated as equally verified as a direct fetch. Atlatsa Resources flagged for manual review; its Vancouver presence looks stale post-2019 restructuring.
