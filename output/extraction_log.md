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

## Run 2026-08-05

**Source:** Direct fetches of each company's own official contact page.

**Files processed:**
- `https://www.international-petroleum.com/contact-us`
- `https://www.artemisgoldinc.com/contact/contact-details/`
- `https://mereninc.com/contact-us/`
- `https://www.firstmajestic.com/contact/contact-details/`
- `https://aris-mining.com/contact-us/`
- `https://imperialmetals.com/contact/`
- `https://www.calibremining.com/`

- Rows added: 0
- Rows updated: 8
- Rows unchanged: 0
- Conflicts: 6
  - International Petroleum Corporation: CONFLICT: province=British Columbia|BC (https://www.international-petroleum.com/contact-us)
  - Artemis Gold Inc: CONFLICT: province=British Columbia|BC (https://www.artemisgoldinc.com/contact/contact-details/)
  - Meren Energy Inc: CONFLICT: province=British Columbia|BC (https://mereninc.com/contact-us/)
  - First Majestic Silver Corp: CONFLICT: province=British Columbia|BC (https://www.firstmajestic.com/contact/contact-details/)
  - Aris Mining Corporation: CONFLICT: province=British Columbia|BC (https://aris-mining.com/contact-us/)
  - Imperial Metals Corporation: CONFLICT: province=British Columbia|BC (https://imperialmetals.com/contact/)
- ILLEGIBLE flags: 11
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
  - Artemis Gold Inc: ILLEGIBLE: contact_email — page uses email obfuscation ('[email protected]' placeholder)
- Quality flags: 0

**Running total:** 66 unique companies — {'complete': 20, 'listing_only': 41, 'detail_only': 5}

**Notes:** Two companies flagged REVIEW rather than treated as independent prospects: Goldcorp Canada Ltd (folded into Newmont after the 2019 acquisition) and Calibre Mining Corp (merged into Equinox Gold, confirmed via a live 301 redirect from calibremining.com to equinoxgold.com). Both entities' listing-page revenue figures may reflect historical/parent-company data rather than a currently independent Vancouver operation.

## Run 2026-08-05

**Source:** Mix of direct official-page fetches and, where blocked, search-engine snippets of the same official pages. Several companies in this batch are historical/merged entities identified via secondary sources and flagged rather than treated as live prospects.

**Files processed:**
- `https://asantegold.com/contact`
- `https://www.trekormetals.com/contact/`
- `https://k92mining.com/contact/`

- Rows added: 0
- Rows updated: 10
- Rows unchanged: 0
- Conflicts: 7
  - Endeavour Silver Corp: CONFLICT: province=British Columbia|BC (edrsilver.com/contact-us/contact-us/ (live fetch 403'd; sourced from search-engine snippet of the company's own official page))
  - Asante Gold Corporation: CONFLICT: province=British Columbia|BC (https://asantegold.com/contact)
  - Trekor Metals Limited: CONFLICT: province=British Columbia|BC (https://www.trekormetals.com/contact/)
  - K92 Mining Inc: CONFLICT: province=British Columbia|BC (https://k92mining.com/contact/)
  - Orla Mining Ltd: CONFLICT: province=British Columbia|BC (orlamining.com contact page (live fetch 404'd on the paths tried; sourced from search-engine snippet of the company's own official page))
  - Teck Highland Valley Copper Partnership: CONFLICT: city=Vancouver|Logan Lake (secondary sources (teck.com project pages, not fetched directly))
  - Teck Highland Valley Copper Partnership: CONFLICT: province=British Columbia|BC (secondary sources (teck.com project pages, not fetched directly))
- ILLEGIBLE flags: 11
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
  - Artemis Gold Inc: ILLEGIBLE: contact_email — page uses email obfuscation ('[email protected]' placeholder)
- Quality flags: 0

**Running total:** 66 unique companies — {'complete': 26, 'listing_only': 31, 'detail_only': 9}

**Notes:** 5 of 10 companies in this batch are historical, merged, or non-Vancouver entities (Northgate Minerals, Petaquilla Minerals, Leagold Mining, Silvermex Resources, Teck Highland Valley Copper Partnership) — flagged REVIEW rather than populated with fabricated current data.

## Run 2026-08-05

**Source:** Mix of direct official-page fetches and search-engine snippets where noted. Several entities flagged REVIEW as historical/inactive/subsidiary.

**Files processed:**
- `https://silvercorpmetals.com/contact-details/`
- `https://orezone.com/contact/`
- `https://santacruzsilver.com/contact/contact-information/`

- Rows added: 0
- Rows updated: 10
- Rows unchanged: 0
- Conflicts: 4
  - Silvercorp Metals Inc: CONFLICT: province=British Columbia|BC (https://silvercorpmetals.com/contact-details/)
  - Orezone Gold Corporation: CONFLICT: province=British Columbia|BC (https://orezone.com/contact/)
  - SantaCruz Silver Mining Ltd: CONFLICT: province=British Columbia|BC (https://santacruzsilver.com/contact/contact-information/)
  - Steppe Gold Ltd: CONFLICT: province=British Columbia|BC (steppegold.com/contact/ (live fetch returned a page without the contact block; data sourced from a search-engine snippet of the same official domain))
- ILLEGIBLE flags: 11
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
  - Artemis Gold Inc: ILLEGIBLE: contact_email — page uses email obfuscation ('[email protected]' placeholder)
- Quality flags: 0

**Running total:** 66 unique companies — {'complete': 30, 'listing_only': 21, 'detail_only': 15}

**Notes:** 6 of 10 companies in this batch flagged REVIEW as historical, inactive, or subsidiary entities rather than independent Vancouver prospects: Nevsun Resources, Target Exploration and Mining Corp, Aris Mining Holdings Corp, Teck-Bullmoose Coal, Huckleberry Mines, Continental Minerals.

## Run 2026-08-05

**Source:** Mix of direct official-page fetches and search-engine snippets where noted. Several entities flagged REVIEW as historical/inactive/dormant/domain-hijacked.

**Files processed:**
- `https://www.amerigoresources.com/company/contact/`
- `https://osinoresources.com/contact-3/`
- `https://thorexpl.com/contact-us/`

- Rows added: 0
- Rows updated: 10
- Rows unchanged: 0
- Conflicts: 5
  - Galiano Gold Inc: CONFLICT: province=British Columbia|BC (galianogold.com/contact/contact-us/default.aspx (live fetch 403'd; sourced from search-engine snippet of the company's own official page))
  - Amerigo Resources Ltd: CONFLICT: province=British Columbia|BC (https://www.amerigoresources.com/company/contact/)
  - Osino Resources Corp: CONFLICT: province=British Columbia|BC (https://osinoresources.com/contact-3/)
  - Thor Explorations Ltd: CONFLICT: province=British Columbia|BC (https://thorexpl.com/contact-us/)
  - SRK Consulting (Canada) Inc: CONFLICT: province=British Columbia|BC (srk.com/en/contact-us/vancouver (live fetch returned a page whose address block renders via JavaScript; sourced from a search-engine snippet of the same official page))
- ILLEGIBLE flags: 12
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
  - Artemis Gold Inc: ILLEGIBLE: contact_email — page uses email obfuscation ('[email protected]' placeholder)
  - Amerigo Resources Ltd: ILLEGIBLE: contact_email — both the general and CEO email addresses render as obfuscated placeholders in the fetched HTML
- Quality flags: 0

**Running total:** 66 unique companies — {'complete': 35, 'listing_only': 11, 'detail_only': 20}

**Notes:** Cache Exploration's former domain has been taken over by an unrelated online-gambling affiliate site — flagged explicitly so it is never mistaken for the company's real site in a future run. 4 of 10 companies in this batch flagged REVIEW as historical/inactive/dormant: Azure Resources (no site found), Trevali Mining (receivership), Aurcana Silver (apparently dormant since 2022), Sunward Resources (subsidiary since 2015).

## Run 2026-08-05

**Source:** Mix of direct official-page fetches and secondary sources for historical/relocated entities. This is the final batch covering all remaining listing_only companies.

**Files processed:**
- `https://bearcreekmining.com/investors/contact/contact-us/`
- `https://lucaradiamond.com/contact/contact-info/`
- `https://queensrdcapital.com/contact/offices/`

- Rows added: 0
- Rows updated: 10
- Rows unchanged: 0
- Conflicts: 4
  - Bear Creek Mining Corporation: CONFLICT: province=British Columbia|BC (https://bearcreekmining.com/investors/contact/contact-us/)
  - Lucara Diamond Corp: CONFLICT: province=British Columbia|BC (https://lucaradiamond.com/contact/contact-info/)
  - Queen's Road Capital Investment Ltd: CONFLICT: city=Vancouver|Hong Kong (https://queensrdcapital.com/contact/offices/)
  - Queen's Road Capital Investment Ltd: CONFLICT: country=Canada|Hong Kong (https://queensrdcapital.com/contact/offices/)
- ILLEGIBLE flags: 12
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
  - Artemis Gold Inc: ILLEGIBLE: contact_email — page uses email obfuscation ('[email protected]' placeholder)
  - Amerigo Resources Ltd: ILLEGIBLE: contact_email — both the general and CEO email addresses render as obfuscated placeholders in the fetched HTML
- Quality flags: 0

**Running total:** 66 unique companies — {'complete': 38, 'listing_only': 1, 'detail_only': 27}

**Notes:** This is the final batch of the 66-company set. 8 of 10 rows flagged REVIEW: two unverifiable/likely-shell entities (17411979 Canada Inc, Ridgetop Forwarding), and six historical/relocated/subsidiary entities whose D&B Vancouver listing does not reflect current independent operations (Puna Operations, Pretium Exploration, New Guinea Gold, Queen's Road Capital [confirmed Hong Kong, not Vancouver], Rockgate Capital, Newmont Canada Corporation). Only Bear Creek Mining and Lucara Diamond Corp were fully verified as independent, active Vancouver companies in this batch.

## Run 2026-08-06

**Source:** Five more listing-page screenshots pasted into the chat session (two of the five, screenshots 4 and 5, were the same view and overlapped with screenshot 1's top rows — deduplicated). Filenames are provenance labels assigned at transcription time.

**Files processed:**
- `chat-listing-2026-08-06-01.png`
- `chat-listing-2026-08-06-02.png`
- `chat-listing-2026-08-06-03.png`
- `chat-listing-2026-08-06-04.png`

- Rows added: 38
- Rows updated: 0
- Rows unchanged: 0
- Conflicts: 0
- ILLEGIBLE flags: 12
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
  - Artemis Gold Inc: ILLEGIBLE: contact_email — page uses email obfuscation ('[email protected]' placeholder)
  - Amerigo Resources Ltd: ILLEGIBLE: contact_email — both the general and CEO email addresses render as obfuscated placeholders in the fetched HTML
- Quality flags: 0

**Running total:** 104 unique companies — {'complete': 38, 'listing_only': 39, 'detail_only': 27}

**Notes:** Screenshots 4 and 5 pasted by the user were identical views (one a wider crop) covering $116.99M-$83.56M, overlapping the top of screenshot 1 (Central Sun Mining, Energold Drilling, 0908113 B.C. Ltd appeared in both) — deduplicated to a single row per company. Batch stops at Lion One Metals Limited ($42.21M), which is above the user's requested $40M cutoff; the next screenshot batch should pick up below this row to reach $40M.

## Run 2026-08-06

**Source:** Mix of direct official-page fetches and search-engine snippets where noted. Several entities flagged REVIEW as historical/merged/subsidiary/domain-parked.

**Files processed:**
- `https://www.tridentresourcescorp.com/corporate/overview/`
- `https://shamaranpetroleum.com/contact/contact-info/`
- `https://lucamining.com/contact/`
- `https://www.hivedigitaltechnologies.com/contact`

- Rows added: 0
- Rows updated: 10
- Rows unchanged: 0
- Conflicts: 6
  - Trident Resources Corp.: CONFLICT: province=British Columbia|BC (https://www.tridentresourcescorp.com/corporate/overview/)
  - HIVE Digital Technologies Ltd: CONFLICT: province=British Columbia|BC (https://www.hivedigitaltechnologies.com/contact (email/phone fetched directly; street address sourced from a search-engine snippet of the same official site, not present on the contact page itself))
  - Shamaran Petroleum Corp: CONFLICT: company_name=Shamaran Petroleum Corp|ShaMaran Petroleum Corp (https://shamaranpetroleum.com/contact/contact-info/)
  - Shamaran Petroleum Corp: CONFLICT: province=British Columbia|BC (https://shamaranpetroleum.com/contact/contact-info/)
  - Copper Mountain Mining Inc: CONFLICT: province=British Columbia|BC (cumtn.com/investors/contact/ (live fetch 403'd; sourced from search-engine snippet of the company's own official page))
  - Luca Mining Corp: CONFLICT: province=British Columbia|BC (https://lucamining.com/contact/)
- ILLEGIBLE flags: 12
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
  - Artemis Gold Inc: ILLEGIBLE: contact_email — page uses email obfuscation ('[email protected]' placeholder)
  - Amerigo Resources Ltd: ILLEGIBLE: contact_email — both the general and CEO email addresses render as obfuscated placeholders in the fetched HTML
- Quality flags: 0

**Running total:** 104 unique companies — {'complete': 43, 'listing_only': 29, 'detail_only': 32}

**Notes:** 5 of 10 companies in this batch flagged REVIEW as historical/merged/defunct/domain-parked: Magellan Minerals (parked domain), Mcilvenna Bay Operating (Foran Mining/Eldorado Gold subsidiary), Queenstake Resources (defunct since 2007/2014), Veris Gold (bankrupt since 2014), Klondex Mines (acquired by Hecla 2018).

## Run 2026-08-06

**Source:** Mix of direct official-page fetches and search-engine snippets where noted. Several entities flagged REVIEW as historical/merged/subsidiary.

**Files processed:**
- `https://monumentmining.com/contact/`
- `https://www.titanminingcorp.com/contact/contact-details/`
- `https://energold.com/contact/`
- `https://www.gsilver.com/contact`
- `https://www.hemisphereenergy.ca/contact`

- Rows added: 0
- Rows updated: 10
- Rows unchanged: 0
- Conflicts: 6
  - Monument Mining Limited: CONFLICT: province=British Columbia|BC (https://monumentmining.com/contact/)
  - Mako Mining Corp: CONFLICT: province=British Columbia|BC (makomining.com/contact/ (live fetch 403'd; address sourced from a search-engine snippet of the company's own official site))
  - Energold Drilling Corp: CONFLICT: province=British Columbia|BC (https://energold.com/contact/)
  - Guanajuato Silver Company Ltd: CONFLICT: province=British Columbia|BC (https://www.gsilver.com/contact)
  - Titan Mining Corporation: CONFLICT: province=British Columbia|BC (https://www.titanminingcorp.com/contact/contact-details/)
  - Hemisphere Energy Corporation: CONFLICT: province=British Columbia|BC (https://www.hemisphereenergy.ca/contact)
- ILLEGIBLE flags: 14
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
  - Artemis Gold Inc: ILLEGIBLE: contact_email — page uses email obfuscation ('[email protected]' placeholder)
  - Amerigo Resources Ltd: ILLEGIBLE: contact_email — both the general and CEO email addresses render as obfuscated placeholders in the fetched HTML
  - Guanajuato Silver Company Ltd: ILLEGIBLE: contact_email — page uses JavaScript-based spambot protection instead of a plain-text address
  - Titan Mining Corporation: ILLEGIBLE: street_address — the fetched contact page only lists the company's US mine-site address (Gouverneur, NY) alongside a Canadian phone/email
- Quality flags: 0

**Running total:** 104 unique companies — {'complete': 49, 'listing_only': 19, 'detail_only': 36}

**Notes:** 5 of 10 companies in this batch flagged REVIEW as historical/merged/subsidiary/inactive: Pretium Resources (same Newcrest/Newmont chain as Pretium Exploration, flagged previously), Central Sun Mining (inactive/amalgamated since 2009, Toronto-registered), 0908113 B.C. Ltd (Capstone Copper subsidiary), Atlantic Gold Corporation (acquired by St Barbara Limited 2019).

## Run 2026-08-06

**Source:** Mix of direct official-page fetches and search-engine snippets where noted. Several entities flagged REVIEW as historical/defunct/subsidiary/misclassified.

**Files processed:**
- `https://aticomining.com/contact-us/contact-information/`
- `https://www.uraniumenergy.com/contact`
- `https://avino.com/contact`

- Rows added: 0
- Rows updated: 8
- Rows unchanged: 0
- Conflicts: 4
  - Atico Mining Corporation: CONFLICT: province=British Columbia|BC (https://aticomining.com/contact-us/contact-information/)
  - Uranium Energy Corp: CONFLICT: province=British Columbia|BC (https://www.uraniumenergy.com/contact)
  - Avino Silver & Gold Mines Ltd: CONFLICT: province=British Columbia|BC (https://avino.com/contact)
  - MineSense Technologies Ltd: CONFLICT: province=British Columbia|BC (minesense.com/contact-us/ (live fetch 403'd; sourced from search-engine snippet of the company's own official site))
- ILLEGIBLE flags: 15
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
  - Artemis Gold Inc: ILLEGIBLE: contact_email — page uses email obfuscation ('[email protected]' placeholder)
  - Amerigo Resources Ltd: ILLEGIBLE: contact_email — both the general and CEO email addresses render as obfuscated placeholders in the fetched HTML
  - Guanajuato Silver Company Ltd: ILLEGIBLE: contact_email — page uses JavaScript-based spambot protection instead of a plain-text address
  - Titan Mining Corporation: ILLEGIBLE: street_address — the fetched contact page only lists the company's US mine-site address (Gouverneur, NY) alongside a Canadian phone/email
  - Atico Mining Corporation: ILLEGIBLE: contact_email — no email published alongside the named Corporate Development contact on the official page.
- Quality flags: 0

**Running total:** 104 unique companies — {'complete': 53, 'listing_only': 11, 'detail_only': 40}

**Notes:** 3 of 8 companies fully verified against official sources (Atico, Avino, Uranium Energy's Canadian office); TAAT flagged as a likely NAICS misclassification (not a mining company); Elevation Gold, Oromin Explorations, and Eskay Creek Mining flagged REVIEW as default-status, historically-acquired, or subsidiary entities respectively.

## Run 2026-08-06

**Source:** Mix of direct official-page fetches and secondary sources for historical/relocated/misidentified entities. This is the final batch of the second listing-screenshot set.

**Files processed:**
- `https://www.eastplats.com/contacts/`
- `https://somagoldcorp.com/contact/`
- `https://liononemetals.com/contact/contact-info/`
- `https://www.ngenergyintl.com/contact/contact-details/`
- `https://encoreuranium.com/corporate/corporate-directory/`

- Rows added: 0
- Rows updated: 10
- Rows unchanged: 0
- Conflicts: 8
  - Eastern Platinum Limited: CONFLICT: province=British Columbia|BC (https://www.eastplats.com/contacts/)
  - Soma Gold Corp: CONFLICT: province=British Columbia|BC (https://somagoldcorp.com/contact/)
  - NG Energy International Corp: CONFLICT: city=Vancouver|Calgary (https://www.ngenergyintl.com/contact/contact-details/)
  - NG Energy International Corp: CONFLICT: province=British Columbia|AB (https://www.ngenergyintl.com/contact/contact-details/)
  - enCore Energy Corp: CONFLICT: city=Vancouver|Dallas (https://encoreuranium.com/corporate/corporate-directory/)
  - enCore Energy Corp: CONFLICT: province=British Columbia|TX (https://encoreuranium.com/corporate/corporate-directory/)
  - enCore Energy Corp: CONFLICT: country=Canada|United States (https://encoreuranium.com/corporate/corporate-directory/)
  - Lion One Metals Limited: CONFLICT: province=British Columbia|BC (https://liononemetals.com/contact/contact-info/)
- ILLEGIBLE flags: 15
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
  - Artemis Gold Inc: ILLEGIBLE: contact_email — page uses email obfuscation ('[email protected]' placeholder)
  - Amerigo Resources Ltd: ILLEGIBLE: contact_email — both the general and CEO email addresses render as obfuscated placeholders in the fetched HTML
  - Guanajuato Silver Company Ltd: ILLEGIBLE: contact_email — page uses JavaScript-based spambot protection instead of a plain-text address
  - Titan Mining Corporation: ILLEGIBLE: street_address — the fetched contact page only lists the company's US mine-site address (Gouverneur, NY) alongside a Canadian phone/email
  - Atico Mining Corporation: ILLEGIBLE: contact_email — no email published alongside the named Corporate Development contact on the official page.
- Quality flags: 0

**Running total:** 104 unique companies — {'complete': 58, 'listing_only': 1, 'detail_only': 45}

**Notes:** This is the final batch of the second listing-screenshot set (down to Lion One Metals at $42.21M). 5 of 10 flagged REVIEW as historical/defunct/merged (Golden Queen, North American Tungsten, Newcastle Gold, Alio Gold) or newly-uncertain (Hemlo Mining). Two more — NG Energy International and enCore Energy — are NOT actually Vancouver companies: their own official sites list Calgary and Dallas head offices respectively, directly contradicting the D&B listing's Vancouver location.

## Run 2026-08-06

**Source:** No new fetches — filling subsidiary rows with the parent company's address already verified elsewhere in this workbook, per documented corporate relationships established in earlier REVIEW notes.

**Files processed:**
- none

- Rows added: 0
- Rows updated: 8
- Rows unchanged: 0
- Conflicts: 9
  - Mcilvenna Bay Operating Ltd: CONFLICT: province=British Columbia|BC (derived from Eldorado Gold Corporation's verified address (already a row in this workbook))
  - 0908113 B.C. Ltd: CONFLICT: province=British Columbia|BC (derived from Capstone Copper Corp's verified address (already a row in this workbook))
  - Newcastle Gold Ltd: CONFLICT: province=British Columbia|BC (derived from Equinox Gold Corp's verified address (already a row in this workbook))
  - Aris Mining Holdings Corp: CONFLICT: province=British Columbia|BC (derived from Aris Mining Corporation's verified address (already a row in this workbook))
  - Huckleberry Mines Ltd: CONFLICT: province=British Columbia|BC (derived from Imperial Metals Corporation's verified address (already a row in this workbook))
  - Silvermex Resources Inc: CONFLICT: province=British Columbia|BC (derived from First Majestic Silver Corp's verified address (already a row in this workbook))
  - Goldcorp Canada Ltd: CONFLICT: province=British Columbia|BC (derived from Newmont Corporation's verified address (already a row in this workbook))
  - Newmont Canada Corporation: CONFLICT: city=North Vancouver|Vancouver (derived from Newmont Corporation's verified address (already a row in this workbook))
  - Newmont Canada Corporation: CONFLICT: province=British Columbia|BC (derived from Newmont Corporation's verified address (already a row in this workbook))
- ILLEGIBLE flags: 15
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
  - Artemis Gold Inc: ILLEGIBLE: contact_email — page uses email obfuscation ('[email protected]' placeholder)
  - Amerigo Resources Ltd: ILLEGIBLE: contact_email — both the general and CEO email addresses render as obfuscated placeholders in the fetched HTML
  - Guanajuato Silver Company Ltd: ILLEGIBLE: contact_email — page uses JavaScript-based spambot protection instead of a plain-text address
  - Titan Mining Corporation: ILLEGIBLE: street_address — the fetched contact page only lists the company's US mine-site address (Gouverneur, NY) alongside a Canadian phone/email
  - Atico Mining Corporation: ILLEGIBLE: contact_email — no email published alongside the named Corporate Development contact on the official page.
- Quality flags: 0

**Running total:** 104 unique companies — {'complete': 66, 'listing_only': 1, 'detail_only': 37}

**Notes:** These 8 rows are true subsidiaries/successor-holders of companies already verified elsewhere in this workbook. Their addresses are recorded as 'same as parent' rather than independently confirmed filings for the subsidiary name itself — flagged accordingly in each row's notes.

## Run 2026-08-06

**Source:** Stage-3 corporate-action news check (12-month lookback) for the bottom 10 companies by revenue in the current workbook. Example/pilot run of the stage-3 workflow documented in CLAUDE.md.

**Files processed:**
- none

- Rows added: 0
- Rows updated: 10
- Rows unchanged: 0
- Conflicts: 0
- ILLEGIBLE flags: 15
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
  - Artemis Gold Inc: ILLEGIBLE: contact_email — page uses email obfuscation ('[email protected]' placeholder)
  - Amerigo Resources Ltd: ILLEGIBLE: contact_email — both the general and CEO email addresses render as obfuscated placeholders in the fetched HTML
  - Guanajuato Silver Company Ltd: ILLEGIBLE: contact_email — page uses JavaScript-based spambot protection instead of a plain-text address
  - Titan Mining Corporation: ILLEGIBLE: street_address — the fetched contact page only lists the company's US mine-site address (Gouverneur, NY) alongside a Canadian phone/email
  - Atico Mining Corporation: ILLEGIBLE: contact_email — no email published alongside the named Corporate Development contact on the official page.
- Quality flags: 0

**Running total:** 104 unique companies — {'complete': 66, 'listing_only': 1, 'detail_only': 37}

**Notes:** Pilot run of the stage-3 news workflow. 2 of 10 companies (Alio Gold, Newcastle Gold) had no citable 12-month news, consistent with being long-defunct. 1 of 10 (Soma Gold) had claims in search results with no primary source found, so nothing was recorded. Golden Queen's ownership REVIEW note was corrected (Andean Precious Metals, not Falco Resources) and Hemlo Mining's uncertain status was resolved to confirmed-active based on this pass — stage-3 news checks doubling as a REVIEW-status correction mechanism, as anticipated in CLAUDE.md.

## Run 2026-08-07

**Source:** Three more listing-page screenshots pasted into the chat session, continuing the revenue sequence downward from the previous batch's bottom (Lion One Metals at $42.21M). Screenshots were pasted out of strict order; reordered by revenue value before transcription.

**Files processed:**
- `chat-listing-2026-08-07-01.png`
- `chat-listing-2026-08-07-02.png`
- `chat-listing-2026-08-07-03.png`

- Rows added: 36
- Rows updated: 0
- Rows unchanged: 0
- Conflicts: 0
- ILLEGIBLE flags: 15
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
  - Artemis Gold Inc: ILLEGIBLE: contact_email — page uses email obfuscation ('[email protected]' placeholder)
  - Amerigo Resources Ltd: ILLEGIBLE: contact_email — both the general and CEO email addresses render as obfuscated placeholders in the fetched HTML
  - Guanajuato Silver Company Ltd: ILLEGIBLE: contact_email — page uses JavaScript-based spambot protection instead of a plain-text address
  - Titan Mining Corporation: ILLEGIBLE: street_address — the fetched contact page only lists the company's US mine-site address (Gouverneur, NY) alongside a Canadian phone/email
  - Atico Mining Corporation: ILLEGIBLE: contact_email — no email published alongside the named Corporate Development contact on the official page.
- Quality flags: 0

**Running total:** 140 unique companies — {'complete': 66, 'listing_only': 37, 'detail_only': 37}

**Notes:** Continues the revenue sequence from the previous batch's bottom row (Lion One Metals, $42.21M) down to $10.1M. Screenshots were pasted out of order (lowest range first, then two higher ranges); reordered by revenue before transcription — no gap or overlap detected against the existing 104-row workbook.

## Run 2026-08-07

**Source:** Mix of direct official-page fetches and search-engine snippets where noted, for the 36 companies added in the third listing-screenshot batch. Several entities flagged REVIEW as historical/merged/subsidiary/misclassified/not-actually-Vancouver.

**Files processed:**
- `https://www.heliostarmetals.com/contact/contact-us/`
- `https://integraresources.com/contact/contact/`
- `https://starcore.com/en/contact/contact-us/`
- `https://impactsilver.com/contact/contact-info/`
- `https://www.silverxmining.com/contact/`
- `https://www.goldgroupmining.com/contact`
- `https://www.canafinvestments.com/contact`
- `https://cathedra.com/contact/`
- `https://www.metallaroyalty.com/contact/`
- `https://www.uraniumroyalty.com/contact/`
- `https://www.goldroyalty.com/contact/contact-details/`
- `https://gunnisoncopper.com/contact/contact-us`

- Rows added: 0
- Rows updated: 36
- Rows unchanged: 0
- Conflicts: 24
  - Heliostar Metals Ltd: CONFLICT: province=British Columbia|BC (https://www.heliostarmetals.com/contact/contact-us/)
  - Integra Resources Corp: CONFLICT: province=British Columbia|BC (https://integraresources.com/contact/contact/)
  - EMX Royalty Corporation: CONFLICT: province=British Columbia|BC (secondary sources (merger press releases; general contact info corroborated across multiple search results))
  - Red Lake Madsen Mine Ltd: CONFLICT: province=British Columbia|BC (search-engine snippet of westredlakegold.com (the actual operating company; not fetched directly))
  - Starcore International Mines Ltd: CONFLICT: province=British Columbia|BC (https://starcore.com/en/contact/contact-us/)
  - Battery Mineral Resources Corp: CONFLICT: province=British Columbia|BC (bmrcorp.com/contact/contact-info/ (live fetch succeeded but the address block wasn't in the static content; sourced from search-engine snippet of the same official page))
  - IMPACT Silver Corp: CONFLICT: province=British Columbia|BC (https://impactsilver.com/contact/contact-info/)
  - Silver X Mining Corp: CONFLICT: province=British Columbia|BC (https://www.silverxmining.com/contact/)
  - Goldgroup Mining Inc: CONFLICT: province=British Columbia|BC (https://www.goldgroupmining.com/contact)
  - Canaf Investments Inc: CONFLICT: province=British Columbia|BC (https://www.canafinvestments.com/contact)
  - Hunter Dickinson Inc: CONFLICT: province=British Columbia|BC (search-engine snippet of hdimining.com (not fetched directly))
  - Cathedra Bitcoin Inc: CONFLICT: province=British Columbia|BC (https://cathedra.com/contact/)
  - Elemental Royalty Corporation: CONFLICT: province=British Columbia|BC (elementalroyalty.com/contact/ (live fetch 404'd on the path tried; sourced from search-engine snippet of the same official domain))
  - K+S Canada Holdings Ltd: CONFLICT: province=British Columbia|BC (search-engine snippet of ks-potashcanada.com (not fetched directly))
  - Metalla Royalty & Streaming Ltd: CONFLICT: province=British Columbia|BC (https://www.metallaroyalty.com/contact/details/)
  - Ledcor CMI Ltd: CONFLICT: province=British Columbia|BC (search-engine snippet of ledcor.com and 411directoryassistance.ca (not fetched directly))
  - Lida Resources Inc: CONFLICT: province=British Columbia|BC (secondary sources (CSE listing, newswire press releases; no official company website located))
  - AndeanGold Ltd: CONFLICT: province=British Columbia|BC (search-engine snippet (site itself could not be reached — connection error, not a policy block); the search results explicitly flagged this data as dating to 2015 or earlier)
  - Virginia Energy Resources Inc: CONFLICT: province=British Columbia|BC (search-engine snippet (direct fetch returned 403; underlying site appears to use old .asp pages dated 2019-2021))
  - Uranium Royalty Corp: CONFLICT: province=British Columbia|BC (https://www.uraniumroyalty.com/contact/)
  - Gunnison Copper Corp: CONFLICT: city=Vancouver|Phoenix (https://gunnisoncopper.com/contact/contact-us)
  - Gunnison Copper Corp: CONFLICT: province=British Columbia|AZ (https://gunnisoncopper.com/contact/contact-us)
  - Gunnison Copper Corp: CONFLICT: country=Canada|United States (https://gunnisoncopper.com/contact/contact-us)
  - Gold Royalty Corp: CONFLICT: province=British Columbia|BC (https://www.goldroyalty.com/contact/contact-details/)
- ILLEGIBLE flags: 20
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
  - Artemis Gold Inc: ILLEGIBLE: contact_email — page uses email obfuscation ('[email protected]' placeholder)
  - Amerigo Resources Ltd: ILLEGIBLE: contact_email — both the general and CEO email addresses render as obfuscated placeholders in the fetched HTML
  - Guanajuato Silver Company Ltd: ILLEGIBLE: contact_email — page uses JavaScript-based spambot protection instead of a plain-text address
  - Titan Mining Corporation: ILLEGIBLE: street_address — the fetched contact page only lists the company's US mine-site address (Gouverneur, NY) alongside a Canadian phone/email
  - Atico Mining Corporation: ILLEGIBLE: contact_email — no email published alongside the named Corporate Development contact on the official page.
  - Heliostar Metals Ltd: ILLEGIBLE: Rob Grey's personal email — obfuscated on the official page
  - Lida Resources Inc: ILLEGIBLE: street_address, contact_email, contact_phone, website — no official company site could be located distinct from third-party listings (CSE, BNamericas, TradingView). Company has a Vancouver corporate HQ and Lima, Peru administrative HQ per secondary sources
  - Uranium Royalty Corp: Shares the same 1188 West Georgia Street, Suite 1830 address as Gold Royalty Corp and Uranium Energy Corp's Vancouver office (both already rows in this workbook) — a known registered-agent-suite cluster, not an error. ILLEGIBLE: contact_email — obfuscated on the official page. The company's own news feed shows a 'Sweetwater Transaction' completed and a shareholder-approved 'Arrangement' both in July 2026 — a material recent corporate action worth a stage-3 news check if this company is of interest.
  - Gunnison Copper Corp: REVIEW: the company's own official contact page lists its head office in Phoenix, Arizona — not Vancouver — directly conflicting with the D&B listing. Recorded the verified Phoenix address rather than inferring a Vancouver one. ILLEGIBLE: contact_email — obfuscated on the official page.
  - Gold Royalty Corp: ILLEGIBLE: contact_email — obfuscated on the official page. Same building/suite as Uranium Royalty Corp and Uranium Energy Corp's Vancouver office (registered-agent-suite cluster). A separate 'Registered and Records Office' is listed at 1000 Cathedral Place, 925 West Georgia Street — a law-firm-style address, likely legal counsel rather than an operating office.
- Quality flags: 0

**Running total:** 140 unique companies — {'complete': 90, 'listing_only': 1, 'detail_only': 49}

**Notes:** 16 of 36 companies flagged REVIEW: misclassified non-mining entries (BioHarvest Sciences, Leef Brands, Sixth Wave Innovations), historically acquired/merged/subsidiary entities (Pacific Rim Mining, Core Gold, EMX Royalty->Elemental Royalty, Polaris Materials, Renaissance Oil, Hillsborough Resources, Golden Lake Exploration, Quintette Coal, Peace River Coal not in this file but flagged separately), project-name vs. entity-name confusion (Red Lake Madsen Mine -> West Red Lake Gold), mine-site operating vehicles (Afton Operating Corporation), an unlocatable entity (NEOS Canada Services), and one confirmed NOT-actually-Vancouver company (Gunnison Copper, real HQ Phoenix AZ). One company (Cambria Gold Mines) is blocked by an active bot-challenge, not bypassed. A registered-agent-suite cluster was identified at 1188 West Georgia St, Suite 1830 (Uranium Royalty Corp, Gold Royalty Corp, Uranium Energy Corp).

## Run 2026-08-07

**Source:** Stage-3 corporate-action + hiring/expansion-signal news check (12-month lookback) for the top 10 companies by revenue. First batch of the full-workbook stage-3 rollout.

**Files processed:**
- none

- Rows added: 0
- Rows updated: 11
- Rows unchanged: 0
- Conflicts: 0
- ILLEGIBLE flags: 20
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
  - Artemis Gold Inc: ILLEGIBLE: contact_email — page uses email obfuscation ('[email protected]' placeholder)
  - Amerigo Resources Ltd: ILLEGIBLE: contact_email — both the general and CEO email addresses render as obfuscated placeholders in the fetched HTML
  - Guanajuato Silver Company Ltd: ILLEGIBLE: contact_email — page uses JavaScript-based spambot protection instead of a plain-text address
  - Titan Mining Corporation: ILLEGIBLE: street_address — the fetched contact page only lists the company's US mine-site address (Gouverneur, NY) alongside a Canadian phone/email
  - Atico Mining Corporation: ILLEGIBLE: contact_email — no email published alongside the named Corporate Development contact on the official page.
  - Heliostar Metals Ltd: ILLEGIBLE: Rob Grey's personal email — obfuscated on the official page
  - Lida Resources Inc: ILLEGIBLE: street_address, contact_email, contact_phone, website — no official company site could be located distinct from third-party listings (CSE, BNamericas, TradingView). Company has a Vancouver corporate HQ and Lima, Peru administrative HQ per secondary sources
  - Uranium Royalty Corp: Shares the same 1188 West Georgia Street, Suite 1830 address as Gold Royalty Corp and Uranium Energy Corp's Vancouver office (both already rows in this workbook) — a known registered-agent-suite cluster, not an error. ILLEGIBLE: contact_email — obfuscated on the official page. The company's own news feed shows a 'Sweetwater Transaction' completed and a shareholder-approved 'Arrangement' both in July 2026 — a material recent corporate action worth a stage-3 news check if this company is of interest.
  - Gunnison Copper Corp: REVIEW: the company's own official contact page lists its head office in Phoenix, Arizona — not Vancouver — directly conflicting with the D&B listing. Recorded the verified Phoenix address rather than inferring a Vancouver one. ILLEGIBLE: contact_email — obfuscated on the official page.
  - Gold Royalty Corp: ILLEGIBLE: contact_email — obfuscated on the official page. Same building/suite as Uranium Royalty Corp and Uranium Energy Corp's Vancouver office (registered-agent-suite cluster). A separate 'Registered and Records Office' is listed at 1000 Cathedral Place, 925 West Georgia Street — a law-firm-style address, likely legal counsel rather than an operating office.
- Quality flags: 0

**Running total:** 140 unique companies — {'complete': 90, 'detail_only': 50}

**Notes:** First batch (top 10 by revenue plus one cross-reference correction) of the full stage-3 rollout across the 140-company workbook. All 10 primary companies are large, active, well-covered producers with abundant real news — no 'REVIEW' needed for any of them. One important catch: Orla Mining Ltd (a separately verified row) has merged into Equinox Gold Corp and is now flagged REVIEW as a result of this pass.

## Run 2026-08-07

**Source:** Stage-3 corporate-action + hiring/expansion-signal news check, batch 2 (companies ranked 12-21 by revenue).

**Files processed:**
- none

- Rows added: 0
- Rows updated: 10
- Rows unchanged: 0
- Conflicts: 0
- ILLEGIBLE flags: 20
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
  - Artemis Gold Inc: ILLEGIBLE: contact_email — page uses email obfuscation ('[email protected]' placeholder)
  - Amerigo Resources Ltd: ILLEGIBLE: contact_email — both the general and CEO email addresses render as obfuscated placeholders in the fetched HTML
  - Guanajuato Silver Company Ltd: ILLEGIBLE: contact_email — page uses JavaScript-based spambot protection instead of a plain-text address
  - Titan Mining Corporation: ILLEGIBLE: street_address — the fetched contact page only lists the company's US mine-site address (Gouverneur, NY) alongside a Canadian phone/email
  - Atico Mining Corporation: ILLEGIBLE: contact_email — no email published alongside the named Corporate Development contact on the official page.
  - Heliostar Metals Ltd: ILLEGIBLE: Rob Grey's personal email — obfuscated on the official page
  - Lida Resources Inc: ILLEGIBLE: street_address, contact_email, contact_phone, website — no official company site could be located distinct from third-party listings (CSE, BNamericas, TradingView). Company has a Vancouver corporate HQ and Lima, Peru administrative HQ per secondary sources
  - Uranium Royalty Corp: Shares the same 1188 West Georgia Street, Suite 1830 address as Gold Royalty Corp and Uranium Energy Corp's Vancouver office (both already rows in this workbook) — a known registered-agent-suite cluster, not an error. ILLEGIBLE: contact_email — obfuscated on the official page. The company's own news feed shows a 'Sweetwater Transaction' completed and a shareholder-approved 'Arrangement' both in July 2026 — a material recent corporate action worth a stage-3 news check if this company is of interest.
  - Gunnison Copper Corp: REVIEW: the company's own official contact page lists its head office in Phoenix, Arizona — not Vancouver — directly conflicting with the D&B listing. Recorded the verified Phoenix address rather than inferring a Vancouver one. ILLEGIBLE: contact_email — obfuscated on the official page.
  - Gold Royalty Corp: ILLEGIBLE: contact_email — obfuscated on the official page. Same building/suite as Uranium Royalty Corp and Uranium Energy Corp's Vancouver office (registered-agent-suite cluster). A separate 'Registered and Records Office' is listed at 1000 Cathedral Place, 925 West Georgia Street — a law-firm-style address, likely legal counsel rather than an operating office.
- Quality flags: 0

**Running total:** 140 unique companies — {'complete': 90, 'detail_only': 50}

**Notes:** Batch 2 of the full-workbook stage-3 rollout. 8 of 10 companies got real, sourced news; 2 (Atlatsa, Goldcorp Canada) were deliberately skipped since they're already flagged REVIEW as non-independent/relocated entities and a dedicated search would be low-value.

## Run 2026-08-07

**Source:** Stage-3 corporate-action + hiring/expansion-signal news check, batch 3.

**Files processed:**
- none

- Rows added: 0
- Rows updated: 10
- Rows unchanged: 0
- Conflicts: 0
- ILLEGIBLE flags: 20
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
  - Artemis Gold Inc: ILLEGIBLE: contact_email — page uses email obfuscation ('[email protected]' placeholder)
  - Amerigo Resources Ltd: ILLEGIBLE: contact_email — both the general and CEO email addresses render as obfuscated placeholders in the fetched HTML
  - Guanajuato Silver Company Ltd: ILLEGIBLE: contact_email — page uses JavaScript-based spambot protection instead of a plain-text address
  - Titan Mining Corporation: ILLEGIBLE: street_address — the fetched contact page only lists the company's US mine-site address (Gouverneur, NY) alongside a Canadian phone/email
  - Atico Mining Corporation: ILLEGIBLE: contact_email — no email published alongside the named Corporate Development contact on the official page.
  - Heliostar Metals Ltd: ILLEGIBLE: Rob Grey's personal email — obfuscated on the official page
  - Lida Resources Inc: ILLEGIBLE: street_address, contact_email, contact_phone, website — no official company site could be located distinct from third-party listings (CSE, BNamericas, TradingView). Company has a Vancouver corporate HQ and Lima, Peru administrative HQ per secondary sources
  - Uranium Royalty Corp: Shares the same 1188 West Georgia Street, Suite 1830 address as Gold Royalty Corp and Uranium Energy Corp's Vancouver office (both already rows in this workbook) — a known registered-agent-suite cluster, not an error. ILLEGIBLE: contact_email — obfuscated on the official page. The company's own news feed shows a 'Sweetwater Transaction' completed and a shareholder-approved 'Arrangement' both in July 2026 — a material recent corporate action worth a stage-3 news check if this company is of interest.
  - Gunnison Copper Corp: REVIEW: the company's own official contact page lists its head office in Phoenix, Arizona — not Vancouver — directly conflicting with the D&B listing. Recorded the verified Phoenix address rather than inferring a Vancouver one. ILLEGIBLE: contact_email — obfuscated on the official page.
  - Gold Royalty Corp: ILLEGIBLE: contact_email — obfuscated on the official page. Same building/suite as Uranium Royalty Corp and Uranium Energy Corp's Vancouver office (registered-agent-suite cluster). A separate 'Registered and Records Office' is listed at 1000 Cathedral Place, 925 West Georgia Street — a law-firm-style address, likely legal counsel rather than an operating office.
- Quality flags: 0

**Running total:** 140 unique companies — {'complete': 90, 'detail_only': 50}

**Notes:** Batch 3 of the full-workbook stage-3 rollout. 8 of 10 companies got real, sourced news; Northgate Minerals and Petaquilla Minerals were deliberately skipped as already-flagged REVIEW/defunct entities.
