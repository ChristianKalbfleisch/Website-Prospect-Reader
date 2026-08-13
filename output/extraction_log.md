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

## Run 2026-08-07

**Source:** Stage-3 corporate-action + hiring/expansion-signal news check, batch 4.

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

**Notes:** Batch 4 of the full-workbook stage-3 rollout. 5 of 10 companies got real, sourced news; 5 were deliberately skipped as already-flagged REVIEW/subsidiary entries.

## Run 2026-08-10

**Source:** Five more listing-page screenshots pasted into the chat session, continuing downward from the previous batch's bottom row (Gold Royalty Corp, $10.1M). Note: there is a gap between $10.1M and $4.26M not covered by these screenshots.

**Files processed:**
- `chat-listing-2026-08-10-01.png`
- `chat-listing-2026-08-10-02.png`
- `chat-listing-2026-08-10-03.png`
- `chat-listing-2026-08-10-04.png`
- `chat-listing-2026-08-10-05.png`

- Rows added: 64
- Rows updated: 0
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

**Running total:** 204 unique companies — {'complete': 90, 'detail_only': 50, 'listing_only': 64}

**Notes:** There is a revenue gap between the previous batch's bottom row (Gold Royalty Corp, $10.1M) and this batch's top row (Design Maintenance Systems Inc, $4.26M) — screenshots covering that range were not provided. Flagging so a future run knows to fill it if completeness matters.

## Run 2026-08-10

**Source:** First contact-lookup pass on the $2.33M-$4.26M revenue tier. Mix of direct fetches and search-engine snippets. This tier is showing a much higher rate of acquired/dormant/unverifiable shell entities than earlier, higher-revenue batches.

**Files processed:**
- `https://www.natbridgeresources.com/contact-us/`
- `https://www.mn25.ca/contact`

- Rows added: 0
- Rows updated: 13
- Rows unchanged: 0
- Conflicts: 10
  - Anglo American Exploration (Canada) Ltd: CONFLICT: province=British Columbia|BC (search-engine snippets of yellowpages.ca/allbiz.ca listings (not the company's own site directly; two different Vancouver addresses appeared in results, this one matched the more complete contact record))
  - Gatos Silver Canada Corp: CONFLICT: province=British Columbia|BC (secondary sources (First Majestic Silver acquisition press release, not fetched directly))
  - South32 Canada Inc: CONFLICT: province=British Columbia|BC (south32.net/contact-us (live fetch 403'd; address sourced from search-engine snippet of the company's own official site))
  - NatBridge Resources Ltd: CONFLICT: city=Vancouver|Burnaby (https://www.natbridgeresources.com/contact-us/)
  - NatBridge Resources Ltd: CONFLICT: province=British Columbia|BC (https://www.natbridgeresources.com/contact-us/)
  - Kaizen Discovery Inc: CONFLICT: province=British Columbia|BC (secondary sources (Ivanhoe Electric acquisition press release, not fetched directly))
  - Ivanhoe Electric Inc: CONFLICT: city=Vancouver|Tempe (secondary sources (Kaizen Discovery acquisition press release, not fetched directly))
  - Ivanhoe Electric Inc: CONFLICT: province=British Columbia|AZ (secondary sources (Kaizen Discovery acquisition press release, not fetched directly))
  - Ivanhoe Electric Inc: CONFLICT: country=Canada|United States (secondary sources (Kaizen Discovery acquisition press release, not fetched directly))
  - Euro Manganese Inc: CONFLICT: province=British Columbia|BC (https://www.mn25.ca/contact)
- ILLEGIBLE flags: 21
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
  - Golden Shield Resources Inc: ILLEGIBLE: street_address, contact_email, contact_phone. Recommend a direct SEDAR+/CSE search if this entity matters.
- Quality flags: 0

**Running total:** 204 unique companies — {'complete': 97, 'detail_only': 56, 'listing_only': 51}

**Notes:** First pass of the $2.33M-$4.26M tier: 6 of 13 flagged REVIEW (2 acquired, 1 receivership-parent, 1 subsidiary of an already-verified row, 1 not-actually-Vancouver, 2 unlocatable shells). This tier is showing meaningfully more dormant/unverifiable entities than the higher-revenue tiers already processed — worth a scope decision on whether exhaustive research on the remaining ~50 companies in this batch is worth the time given the hit rate so far.

## Run 2026-08-10

**Source:** Three new listing-page screenshots pasted into the chat session, filling the previously-flagged gap between $10.1M (Gold Royalty Corp) and $4.26M (Design Maintenance Systems Inc). Two other screenshots pasted alongside these were exact duplicates of an earlier batch and were skipped.

**Files processed:**
- `chat-listing-2026-08-10-06.png`
- `chat-listing-2026-08-10-07.png`
- `chat-listing-2026-08-10-08.png`

- Rows added: 39
- Rows updated: 0
- Rows unchanged: 0
- Conflicts: 0
- ILLEGIBLE flags: 21
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
  - Golden Shield Resources Inc: ILLEGIBLE: street_address, contact_email, contact_phone. Recommend a direct SEDAR+/CSE search if this entity matters.
- Quality flags: 0

**Running total:** 243 unique companies — {'complete': 97, 'detail_only': 56, 'listing_only': 90}

**Notes:** This closes the revenue gap flagged in the previous batch — the sequence is now continuous from Gold Royalty Corp ($10.1M) down through this batch to Design Maintenance Systems Inc ($4.26M, already merged).

## Run 2026-08-10

**Source:** Contact lookup, batch 15 — first 10 of the 90 remaining listing_only companies (highest revenue tier of this set, $9.6M-$7.35M). Mix of direct fetches and search-engine snippets.

**Files processed:**
- `https://www.1911gold.com/contact/`
- `https://highgoldmining.com/contact/`

- Rows added: 0
- Rows updated: 10
- Rows unchanged: 0
- Conflicts: 6
  - Barrick Gold Inc: CONFLICT: province=British Columbia|BC (search-engine snippets (yellowpages.ca listing for a separate Barrick Technology Centre at 323 Alexander St; barrick.com contact page for general IR email; not fetched directly))
  - HighGold Mining Inc.: CONFLICT: province=British Columbia|BC (https://highgoldmining.com/contact/)
  - Pamicon Developments Ltd: CONFLICT: province=British Columbia|BC (search-engine snippets (yellowpages.ca/Kompass directory listings, not an official company site))
  - 1911 Gold Corporation: CONFLICT: province=British Columbia|BC (https://www.1911gold.com/contact/)
  - NEMI Northern Energy & Mining Inc: CONFLICT: province=British Columbia|BC (search-engine snippet (resourceconnector.ca directory listing, not the company's own site))
  - Sunoil Ltd.: CONFLICT: province=British Columbia|BC (search-engine snippets (yellowpages.ca directory listing, not the company's own site))
- ILLEGIBLE flags: 24
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
  - Golden Shield Resources Inc: ILLEGIBLE: street_address, contact_email, contact_phone. Recommend a direct SEDAR+/CSE search if this entity matters.
  - Western Magnesium Corporation: Confirmed active, Vancouver-headquartered (magnesium production technology). ILLEGIBLE: street_address, contact_email, contact_phone — not present in static HTML. Recommend re-verifying directly if precision matters.
  - HighGold Mining Inc.: ILLEGIBLE: contact_email — official page displays it in reversed character order (a JS-deobfuscation trick), not decoded. Nicole Hoeller, VP Communications, is the named Investor/Corporate Development contact, same phone.
  - Patagonia Gold Corp.: Confirmed active (TSXV: PGDC), Vancouver-headquartered, Argentina-focused gold/silver explorer. ILLEGIBLE: street_address, contact_email, contact_phone — site fetch failed on this attempt. Recommend re-verifying directly if precision matters.
- Quality flags: 0

**Running total:** 243 unique companies — {'complete': 105, 'detail_only': 58, 'listing_only': 80}

**Notes:** First batch of 10 from the 90-company backlog. 1 flagged REVIEW as dormant/stalled (Avanti Kitsault Mine); 1 flagged REVIEW as a regional office of a Toronto-headquartered parent (Barrick Gold Inc). Several small/thinly-documented companies (Rochester Resources, Pamicon Developments, Sunoil) had no official site locatable — recorded what directory listings offered rather than leaving entirely blank.

## Run 2026-08-10

**Source:** Contact lookup, batch 16 — next 10 of the 90-company backlog ($7M-$6.07M revenue tier). Mix of direct fetches and search-engine snippets.

**Files processed:**
- `https://trillionenergy.com/contact/`

- Rows added: 0
- Rows updated: 10
- Rows unchanged: 0
- Conflicts: 4
  - Orca Sand & Gravel Limited Partnership: CONFLICT: city=Vancouver|Port McNeill (secondary sources (Vulcan Materials, Natural Resources Canada, not fetched directly))
  - Orca Sand & Gravel Limited Partnership: CONFLICT: province=British Columbia|BC (secondary sources (Vulcan Materials, Natural Resources Canada, not fetched directly))
  - Trillion Energy International Inc: CONFLICT: province=British Columbia|BC (https://trillionenergy.com/contact/)
  - Sierra Madre Gold and Silver Ltd: CONFLICT: province=British Columbia|BC (search-engine snippet of the company's own official site (not fetched directly))
- ILLEGIBLE flags: 26
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
  - Golden Shield Resources Inc: ILLEGIBLE: street_address, contact_email, contact_phone. Recommend a direct SEDAR+/CSE search if this entity matters.
  - Western Magnesium Corporation: Confirmed active, Vancouver-headquartered (magnesium production technology). ILLEGIBLE: street_address, contact_email, contact_phone — not present in static HTML. Recommend re-verifying directly if precision matters.
  - HighGold Mining Inc.: ILLEGIBLE: contact_email — official page displays it in reversed character order (a JS-deobfuscation trick), not decoded. Nicole Hoeller, VP Communications, is the named Investor/Corporate Development contact, same phone.
  - Patagonia Gold Corp.: Confirmed active (TSXV: PGDC), Vancouver-headquartered, Argentina-focused gold/silver explorer. ILLEGIBLE: street_address, contact_email, contact_phone — site fetch failed on this attempt. Recommend re-verifying directly if precision matters.
  - Rio Tinto Exploration Canada Inc: Rio Tinto's Canadian operations are primarily centered on Iron Ore Company of Canada (Quebec/Labrador) and Rio Tinto Fer et Titane (Quebec) rather than a distinct Vancouver office. ILLEGIBLE: street_address, contact_email, contact_phone. Recommend direct verification if this entity matters.
  - Iberdrola Energy Projects Canada Corporation: This is a Canadian project-development subsidiary of Iberdrola S.A. (Spanish multinational utility). ILLEGIBLE: street_address, contact_email, contact_phone. Not a mining company — energy/utility sector. Recommend direct verification if this entity matters.
- Quality flags: 0

**Running total:** 243 unique companies — {'complete': 112, 'detail_only': 61, 'listing_only': 70}

**Notes:** 3 of 10 flagged REVIEW as acquired/subsidiary (Orca Sand & Gravel, Foran Mining, Alderon Iron Ore/dormant), 1 flagged REVIEW as misclassified non-mining (WellteQ Digital Health), and 1 flagged REVIEW as an inferred-not-confirmed entity match (Craigmont Mines / Nicola Mining). Two entities (Valhalla Resources, and full details for Rio Tinto Exploration Canada / Iberdrola Energy Projects Canada) could not be pinned down beyond parent-company confirmation.

## Run 2026-08-10

**Source:** Two new listing-page screenshots (of five pasted; three were exact duplicates of earlier batches and were skipped), continuing below the previous batch's bottom row (Continuum Resources Ltd, $2.33M).

**Files processed:**
- `chat-listing-2026-08-10-09.png`
- `chat-listing-2026-08-10-10.png`

- Rows added: 19
- Rows updated: 0
- Rows unchanged: 0
- Conflicts: 0
- ILLEGIBLE flags: 26
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
  - Golden Shield Resources Inc: ILLEGIBLE: street_address, contact_email, contact_phone. Recommend a direct SEDAR+/CSE search if this entity matters.
  - Western Magnesium Corporation: Confirmed active, Vancouver-headquartered (magnesium production technology). ILLEGIBLE: street_address, contact_email, contact_phone — not present in static HTML. Recommend re-verifying directly if precision matters.
  - HighGold Mining Inc.: ILLEGIBLE: contact_email — official page displays it in reversed character order (a JS-deobfuscation trick), not decoded. Nicole Hoeller, VP Communications, is the named Investor/Corporate Development contact, same phone.
  - Patagonia Gold Corp.: Confirmed active (TSXV: PGDC), Vancouver-headquartered, Argentina-focused gold/silver explorer. ILLEGIBLE: street_address, contact_email, contact_phone — site fetch failed on this attempt. Recommend re-verifying directly if precision matters.
  - Rio Tinto Exploration Canada Inc: Rio Tinto's Canadian operations are primarily centered on Iron Ore Company of Canada (Quebec/Labrador) and Rio Tinto Fer et Titane (Quebec) rather than a distinct Vancouver office. ILLEGIBLE: street_address, contact_email, contact_phone. Recommend direct verification if this entity matters.
  - Iberdrola Energy Projects Canada Corporation: This is a Canadian project-development subsidiary of Iberdrola S.A. (Spanish multinational utility). ILLEGIBLE: street_address, contact_email, contact_phone. Not a mining company — energy/utility sector. Recommend direct verification if this entity matters.
- Quality flags: 0

**Running total:** 262 unique companies — {'complete': 112, 'detail_only': 61, 'listing_only': 89}

**Notes:** Redhawk Resources, Maxy Gold, and Balmoral Resources are additional companies tied at the $2.33M revenue level, alongside the 10 already in the workbook at that same figure — same D&B tie-breaking pattern seen throughout this project.

## Run 2026-08-10

**Source:** Contact lookup, batch 17 — companies from the newest listing batch ($2.09M-$2.33M tier). Mix of direct fetches and search snippets.

**Files processed:**
- `https://www.westernlng.com/contact`

- Rows added: 0
- Rows updated: 5
- Rows unchanged: 0
- Conflicts: 1
  - Marathon Gold NI Corp.: CONFLICT: province=British Columbia|BC (search-engine snippet (tmgcorporation.com, not the company's own site))
- ILLEGIBLE flags: 27
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
  - Golden Shield Resources Inc: ILLEGIBLE: street_address, contact_email, contact_phone. Recommend a direct SEDAR+/CSE search if this entity matters.
  - Western Magnesium Corporation: Confirmed active, Vancouver-headquartered (magnesium production technology). ILLEGIBLE: street_address, contact_email, contact_phone — not present in static HTML. Recommend re-verifying directly if precision matters.
  - HighGold Mining Inc.: ILLEGIBLE: contact_email — official page displays it in reversed character order (a JS-deobfuscation trick), not decoded. Nicole Hoeller, VP Communications, is the named Investor/Corporate Development contact, same phone.
  - Patagonia Gold Corp.: Confirmed active (TSXV: PGDC), Vancouver-headquartered, Argentina-focused gold/silver explorer. ILLEGIBLE: street_address, contact_email, contact_phone — site fetch failed on this attempt. Recommend re-verifying directly if precision matters.
  - Rio Tinto Exploration Canada Inc: Rio Tinto's Canadian operations are primarily centered on Iron Ore Company of Canada (Quebec/Labrador) and Rio Tinto Fer et Titane (Quebec) rather than a distinct Vancouver office. ILLEGIBLE: street_address, contact_email, contact_phone. Recommend direct verification if this entity matters.
  - Iberdrola Energy Projects Canada Corporation: This is a Canadian project-development subsidiary of Iberdrola S.A. (Spanish multinational utility). ILLEGIBLE: street_address, contact_email, contact_phone. Not a mining company — energy/utility sector. Recommend direct verification if this entity matters.
  - Basin Uranium Corp: Confirmed active as of Dec 2024 (CSE-listed, Vancouver-based). ILLEGIBLE: street_address, contact_email, contact_phone, website — no official site located distinct from financial-news aggregators. Recommend a direct CSE/SEDAR+ search if this entity matters.
- Quality flags: 0

**Running total:** 262 unique companies — {'complete': 115, 'detail_only': 63, 'listing_only': 84}

**Notes:** Small batch given time constraints — 3 of 5 flagged REVIEW (Western LNG's real HQ is Houston, Marathon Gold NI Corp is a satellite office of a Toronto company, Dynasty Metals & Mining shows signs of dormancy since 2016). Remaining companies from this new batch and the older 70-company backlog still need research.

## Run 2026-08-10

**Source:** Contact lookup, batch 18 — remaining companies from the newest listing batch. Several had no locatable public record after repeated search attempts.

**Files processed:**
- none

- Rows added: 0
- Rows updated: 13
- Rows unchanged: 0
- Conflicts: 0
- ILLEGIBLE flags: 28
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
  - Golden Shield Resources Inc: ILLEGIBLE: street_address, contact_email, contact_phone. Recommend a direct SEDAR+/CSE search if this entity matters.
  - Western Magnesium Corporation: Confirmed active, Vancouver-headquartered (magnesium production technology). ILLEGIBLE: street_address, contact_email, contact_phone — not present in static HTML. Recommend re-verifying directly if precision matters.
  - HighGold Mining Inc.: ILLEGIBLE: contact_email — official page displays it in reversed character order (a JS-deobfuscation trick), not decoded. Nicole Hoeller, VP Communications, is the named Investor/Corporate Development contact, same phone.
  - Patagonia Gold Corp.: Confirmed active (TSXV: PGDC), Vancouver-headquartered, Argentina-focused gold/silver explorer. ILLEGIBLE: street_address, contact_email, contact_phone — site fetch failed on this attempt. Recommend re-verifying directly if precision matters.
  - Rio Tinto Exploration Canada Inc: Rio Tinto's Canadian operations are primarily centered on Iron Ore Company of Canada (Quebec/Labrador) and Rio Tinto Fer et Titane (Quebec) rather than a distinct Vancouver office. ILLEGIBLE: street_address, contact_email, contact_phone. Recommend direct verification if this entity matters.
  - Iberdrola Energy Projects Canada Corporation: This is a Canadian project-development subsidiary of Iberdrola S.A. (Spanish multinational utility). ILLEGIBLE: street_address, contact_email, contact_phone. Not a mining company — energy/utility sector. Recommend direct verification if this entity matters.
  - Basin Uranium Corp: Confirmed active as of Dec 2024 (CSE-listed, Vancouver-based). ILLEGIBLE: street_address, contact_email, contact_phone, website — no official site located distinct from financial-news aggregators. Recommend a direct CSE/SEDAR+ search if this entity matters.
  - Altima Energy Inc: renamed from Altima Resources Ltd in December 2024. ILLEGIBLE: street_address, contact_email, contact_phone, website. Recommend a direct search if this entity matters.
- Quality flags: 0

**Running total:** 262 unique companies — {'complete': 116, 'detail_only': 75, 'listing_only': 71}

**Notes:** This batch closes out the newest (19-company) listing batch. 8 of 13 had no locatable public record at all — a markedly higher rate of unverifiable entities than any prior batch, consistent with how small (sub-$2.3M revenue) these companies are. Recommend discussing strategy for the remaining ~70-company backlog given this pattern.

## Run 2026-08-10

**Source:** Four more listing-page screenshots, in the $2.09M-$2.04M revenue tier. One duplicate (Avanti Kitsault Mine Ltd, already a row) was skipped.

**Files processed:**
- `chat-listing-2026-08-10-11.png`
- `chat-listing-2026-08-10-12.png`
- `chat-listing-2026-08-10-13.png`
- `chat-listing-2026-08-10-14.png`

- Rows added: 49
- Rows updated: 0
- Rows unchanged: 0
- Conflicts: 0
- ILLEGIBLE flags: 28
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
  - Golden Shield Resources Inc: ILLEGIBLE: street_address, contact_email, contact_phone. Recommend a direct SEDAR+/CSE search if this entity matters.
  - Western Magnesium Corporation: Confirmed active, Vancouver-headquartered (magnesium production technology). ILLEGIBLE: street_address, contact_email, contact_phone — not present in static HTML. Recommend re-verifying directly if precision matters.
  - HighGold Mining Inc.: ILLEGIBLE: contact_email — official page displays it in reversed character order (a JS-deobfuscation trick), not decoded. Nicole Hoeller, VP Communications, is the named Investor/Corporate Development contact, same phone.
  - Patagonia Gold Corp.: Confirmed active (TSXV: PGDC), Vancouver-headquartered, Argentina-focused gold/silver explorer. ILLEGIBLE: street_address, contact_email, contact_phone — site fetch failed on this attempt. Recommend re-verifying directly if precision matters.
  - Rio Tinto Exploration Canada Inc: Rio Tinto's Canadian operations are primarily centered on Iron Ore Company of Canada (Quebec/Labrador) and Rio Tinto Fer et Titane (Quebec) rather than a distinct Vancouver office. ILLEGIBLE: street_address, contact_email, contact_phone. Recommend direct verification if this entity matters.
  - Iberdrola Energy Projects Canada Corporation: This is a Canadian project-development subsidiary of Iberdrola S.A. (Spanish multinational utility). ILLEGIBLE: street_address, contact_email, contact_phone. Not a mining company — energy/utility sector. Recommend direct verification if this entity matters.
  - Basin Uranium Corp: Confirmed active as of Dec 2024 (CSE-listed, Vancouver-based). ILLEGIBLE: street_address, contact_email, contact_phone, website — no official site located distinct from financial-news aggregators. Recommend a direct CSE/SEDAR+ search if this entity matters.
  - Altima Energy Inc: renamed from Altima Resources Ltd in December 2024. ILLEGIBLE: street_address, contact_email, contact_phone, website. Recommend a direct search if this entity matters.
- Quality flags: 0

**Running total:** 311 unique companies — {'complete': 116, 'detail_only': 75, 'listing_only': 120}

**Notes:** One duplicate skipped (Avanti Kitsault Mine Ltd, already flagged REVIEW in an earlier batch). 49 new companies at the $2.09M-$2.04M tier, mostly tied at exactly $2.04M — same D&B tie-breaking pattern as prior batches.

## Run 2026-08-10

**Source:** Contact lookup, batch 19 — from the newest ($2.04M-$2.09M) listing batch. Mix of search snippets; several dormant/acquired entities flagged and left without deep research per instruction.

**Files processed:**
- `https://pstlaw.ca/contact/`

- Rows added: 0
- Rows updated: 15
- Rows unchanged: 0
- Conflicts: 13
  - B2Gold Corp: CONFLICT: province=British Columbia|BC (b2gold.com/contact/contact-us/ (live fetch still returns an active Cloudflare bot-challenge, unchanged from earlier batches; address sourced from a search-engine snippet of the company's own official page instead))
  - Newcrest Red Chris Mining Limited: CONFLICT: province=British Columbia|BC (search-engine snippet (D&B directory listing, not the company's own site))
  - Hecla Canada Ltd: CONFLICT: province=British Columbia|BC (search-engine snippet (D&B directory listing, not the company's own site))
  - Niocorp Developments Ltd: CONFLICT: company_name=Niocorp Developments Ltd|NioCorp Developments Ltd (https://www.niocorp.com/contact-us/ (verified via search snippet of the official page))
  - Niocorp Developments Ltd: CONFLICT: city=Vancouver|Centennial (https://www.niocorp.com/contact-us/ (verified via search snippet of the official page))
  - Niocorp Developments Ltd: CONFLICT: province=British Columbia|CO (https://www.niocorp.com/contact-us/ (verified via search snippet of the official page))
  - Niocorp Developments Ltd: CONFLICT: country=Canada|United States (https://www.niocorp.com/contact-us/ (verified via search snippet of the official page))
  - Rare Element Resources Ltd: CONFLICT: city=Vancouver|Littleton (search-engine snippets (SEC filings, company FAQ page, not fetched directly))
  - Rare Element Resources Ltd: CONFLICT: province=British Columbia|CO (search-engine snippets (SEC filings, company FAQ page, not fetched directly))
  - Rare Element Resources Ltd: CONFLICT: country=Canada|United States (search-engine snippets (SEC filings, company FAQ page, not fetched directly))
  - Deakin Equipment Ltd.: CONFLICT: province=British Columbia|BC (search-engine snippets (Yelp listing, not the company's own site))
  - Pape Salter Teillet LLP: CONFLICT: province=British Columbia|BC (https://pstlaw.ca/contact/)
  - Kazax Minerals Inc: CONFLICT: company_name=Kazax Minerals Inc|KazaX Minerals Inc (search-engine snippets (LinkedIn/Bloomberg, described as 'recently re-capitalised' but no date given))
- ILLEGIBLE flags: 28
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
  - Golden Shield Resources Inc: ILLEGIBLE: street_address, contact_email, contact_phone. Recommend a direct SEDAR+/CSE search if this entity matters.
  - Western Magnesium Corporation: Confirmed active, Vancouver-headquartered (magnesium production technology). ILLEGIBLE: street_address, contact_email, contact_phone — not present in static HTML. Recommend re-verifying directly if precision matters.
  - HighGold Mining Inc.: ILLEGIBLE: contact_email — official page displays it in reversed character order (a JS-deobfuscation trick), not decoded. Nicole Hoeller, VP Communications, is the named Investor/Corporate Development contact, same phone.
  - Patagonia Gold Corp.: Confirmed active (TSXV: PGDC), Vancouver-headquartered, Argentina-focused gold/silver explorer. ILLEGIBLE: street_address, contact_email, contact_phone — site fetch failed on this attempt. Recommend re-verifying directly if precision matters.
  - Rio Tinto Exploration Canada Inc: Rio Tinto's Canadian operations are primarily centered on Iron Ore Company of Canada (Quebec/Labrador) and Rio Tinto Fer et Titane (Quebec) rather than a distinct Vancouver office. ILLEGIBLE: street_address, contact_email, contact_phone. Recommend direct verification if this entity matters.
  - Iberdrola Energy Projects Canada Corporation: This is a Canadian project-development subsidiary of Iberdrola S.A. (Spanish multinational utility). ILLEGIBLE: street_address, contact_email, contact_phone. Not a mining company — energy/utility sector. Recommend direct verification if this entity matters.
  - Basin Uranium Corp: Confirmed active as of Dec 2024 (CSE-listed, Vancouver-based). ILLEGIBLE: street_address, contact_email, contact_phone, website — no official site located distinct from financial-news aggregators. Recommend a direct CSE/SEDAR+ search if this entity matters.
  - Altima Energy Inc: renamed from Altima Resources Ltd in December 2024. ILLEGIBLE: street_address, contact_email, contact_phone, website. Recommend a direct search if this entity matters.
- Quality flags: 1
  - POSTAL_FORMAT: Niocorp Developments Ltd postal_code='80112' does not match A1A 1A1

**Running total:** 311 unique companies — {'complete': 123, 'detail_only': 82, 'listing_only': 106}

**Notes:** 14 companies processed from the newest listing batch. 8 flagged REVIEW as acquired/subsidiary/dormant/not-actually-Vancouver (Red Chris x2, Goldcorp Inc, B2Gold Logistics, NioCorp, Rare Element Resources, Great Bear Royalties, Salmon River Resources, Kobex Resources). Hecla Canada and Deakin Equipment confirmed active with real Vancouver addresses; Pape Salter Teillet confirmed active but is a law firm, not mining.

## Run 2026-08-10

**Source:** Contact lookup, batch 20 — remaining companies from the newest listing batch. Given how consistently unlocatable this tier has been, entities with no search hits after a reasonable attempt are flagged and left rather than exhaustively re-searched, per instruction.

**Files processed:**
- none

- Rows added: 0
- Rows updated: 18
- Rows unchanged: 0
- Conflicts: 0
- ILLEGIBLE flags: 28
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
  - Golden Shield Resources Inc: ILLEGIBLE: street_address, contact_email, contact_phone. Recommend a direct SEDAR+/CSE search if this entity matters.
  - Western Magnesium Corporation: Confirmed active, Vancouver-headquartered (magnesium production technology). ILLEGIBLE: street_address, contact_email, contact_phone — not present in static HTML. Recommend re-verifying directly if precision matters.
  - HighGold Mining Inc.: ILLEGIBLE: contact_email — official page displays it in reversed character order (a JS-deobfuscation trick), not decoded. Nicole Hoeller, VP Communications, is the named Investor/Corporate Development contact, same phone.
  - Patagonia Gold Corp.: Confirmed active (TSXV: PGDC), Vancouver-headquartered, Argentina-focused gold/silver explorer. ILLEGIBLE: street_address, contact_email, contact_phone — site fetch failed on this attempt. Recommend re-verifying directly if precision matters.
  - Rio Tinto Exploration Canada Inc: Rio Tinto's Canadian operations are primarily centered on Iron Ore Company of Canada (Quebec/Labrador) and Rio Tinto Fer et Titane (Quebec) rather than a distinct Vancouver office. ILLEGIBLE: street_address, contact_email, contact_phone. Recommend direct verification if this entity matters.
  - Iberdrola Energy Projects Canada Corporation: This is a Canadian project-development subsidiary of Iberdrola S.A. (Spanish multinational utility). ILLEGIBLE: street_address, contact_email, contact_phone. Not a mining company — energy/utility sector. Recommend direct verification if this entity matters.
  - Basin Uranium Corp: Confirmed active as of Dec 2024 (CSE-listed, Vancouver-based). ILLEGIBLE: street_address, contact_email, contact_phone, website — no official site located distinct from financial-news aggregators. Recommend a direct CSE/SEDAR+ search if this entity matters.
  - Altima Energy Inc: renamed from Altima Resources Ltd in December 2024. ILLEGIBLE: street_address, contact_email, contact_phone, website. Recommend a direct search if this entity matters.
- Quality flags: 1
  - POSTAL_FORMAT: Niocorp Developments Ltd postal_code='80112' does not match A1A 1A1

**Running total:** 311 unique companies — {'complete': 124, 'detail_only': 99, 'listing_only': 88}

**Notes:** 18 companies triaged from the newest listing batch. Given the very low hit rate at this revenue tier (most searches return either nothing or confirm dormancy/acquisition), remaining unresearched entries were flagged rather than exhaustively searched one-by-one. Still to do: Riva Gold Corporation, Viscount Mining Resources Ltd (partial), StrategX Elements Corp, Pegmatite One Lithium and Gold Corp, Coronation Mines Ltd, Lumina Metals Corp, Canadian De Hua International Trading Ltd, Magnus International Resources Inc, B C & Yukon Chamber of Mines, CanXGold Mining Corp, Norra Metals Corp, Xemplar Energy Corp, XCite Resources Inc, Africo Resources Ltd, Valory Resources Inc., Contango Mining Canada Inc, Adonis Minerals Corp — plus the entire older 71-company backlog.

## Run 2026-08-10

**Source:** Contact lookup, batch 21 — closes out the newest listing batch. Mix of direct fetches and search snippets.

**Files processed:**
- `https://www.strategxcorp.com/contact`
- `https://amebc.ca/contact/`

- Rows added: 0
- Rows updated: 17
- Rows unchanged: 0
- Conflicts: 3
  - StrategX Elements Corp: CONFLICT: province=British Columbia|BC (https://www.strategxcorp.com/contact)
  - B C & Yukon Chamber of Mines: CONFLICT: province=British Columbia|BC (https://amebc.ca/contact/)
  - Valory Resources Inc.: CONFLICT: province=British Columbia|BC (search-engine snippet (D&B directory listing, not the company's own site))
- ILLEGIBLE flags: 30
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
  - Golden Shield Resources Inc: ILLEGIBLE: street_address, contact_email, contact_phone. Recommend a direct SEDAR+/CSE search if this entity matters.
  - Western Magnesium Corporation: Confirmed active, Vancouver-headquartered (magnesium production technology). ILLEGIBLE: street_address, contact_email, contact_phone — not present in static HTML. Recommend re-verifying directly if precision matters.
  - HighGold Mining Inc.: ILLEGIBLE: contact_email — official page displays it in reversed character order (a JS-deobfuscation trick), not decoded. Nicole Hoeller, VP Communications, is the named Investor/Corporate Development contact, same phone.
  - Patagonia Gold Corp.: Confirmed active (TSXV: PGDC), Vancouver-headquartered, Argentina-focused gold/silver explorer. ILLEGIBLE: street_address, contact_email, contact_phone — site fetch failed on this attempt. Recommend re-verifying directly if precision matters.
  - Rio Tinto Exploration Canada Inc: Rio Tinto's Canadian operations are primarily centered on Iron Ore Company of Canada (Quebec/Labrador) and Rio Tinto Fer et Titane (Quebec) rather than a distinct Vancouver office. ILLEGIBLE: street_address, contact_email, contact_phone. Recommend direct verification if this entity matters.
  - Iberdrola Energy Projects Canada Corporation: This is a Canadian project-development subsidiary of Iberdrola S.A. (Spanish multinational utility). ILLEGIBLE: street_address, contact_email, contact_phone. Not a mining company — energy/utility sector. Recommend direct verification if this entity matters.
  - Basin Uranium Corp: Confirmed active as of Dec 2024 (CSE-listed, Vancouver-based). ILLEGIBLE: street_address, contact_email, contact_phone, website — no official site located distinct from financial-news aggregators. Recommend a direct CSE/SEDAR+ search if this entity matters.
  - Altima Energy Inc: renamed from Altima Resources Ltd in December 2024. ILLEGIBLE: street_address, contact_email, contact_phone, website. Recommend a direct search if this entity matters.
  - Lumina Metals Corp: contact Scott Hicks, shicks@luminagold.com, +1 604 646 1890, per search results — recorded for reference but not verified directly). ILLEGIBLE: street_address, contact_email, contact_phone for Lumina Metals specifically. Recommend re-verifying directly if precision matters.
  - B C & Yukon Chamber of Mines: This organization renamed itself the Association for Mineral Exploration British Columbia (AME BC) in 2005 — this is the current name and site, still Vancouver-based. Verified this is distinct from the similarly-named 'Yukon Chamber of Mines' (Whitehorse, YT), which some search results conflated it with. Not a mining company itself but the region's lead mineral-exploration industry association — a real, active, contactable organization. ILLEGIBLE: contact_email — obfuscated on the official page.
- Quality flags: 1
  - POSTAL_FORMAT: Niocorp Developments Ltd postal_code='80112' does not match A1A 1A1

**Running total:** 311 unique companies — {'complete': 128, 'detail_only': 110, 'listing_only': 73}

**Notes:** This closes out the newest (49-company) listing batch. StrategX Elements and B C & Yukon Chamber of Mines (now AME BC) verified with real Vancouver addresses. CanXGold Mining and Africo Resources flagged REVIEW as insolvent/acquired. Lumina Metals confirmed very active (major 2025 IPO) but direct contact not obtained. The remaining ~11 companies had no locatable public record — the highest unverifiable rate of any batch in this project, consistent with this being the lowest revenue tier processed so far ($2.04M-$2.09M).

## Run 2026-08-10

**Source:** Contact lookup, batch 22 — the $4.44M-$6.07M revenue tier of the older backlog. Mix of search snippets.

**Files processed:**
- none

- Rows added: 0
- Rows updated: 18
- Rows unchanged: 0
- Conflicts: 3
  - International Enexco Limited: CONFLICT: province=British Columbia|BC (secondary sources (Denison Mines information circular, not fetched directly))
  - Vicuña Corp: CONFLICT: province=British Columbia|BC (search-engine snippets (lundinmining.com press release, vicuna.com/en/contacto/ referenced but not fetched directly))
  - Constantine Metal Resources Ltd: CONFLICT: province=British Columbia|BC (search-engine snippets (yellowpages.ca, not the company's own site))
- ILLEGIBLE flags: 31
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
  - Golden Shield Resources Inc: ILLEGIBLE: street_address, contact_email, contact_phone. Recommend a direct SEDAR+/CSE search if this entity matters.
  - Western Magnesium Corporation: Confirmed active, Vancouver-headquartered (magnesium production technology). ILLEGIBLE: street_address, contact_email, contact_phone — not present in static HTML. Recommend re-verifying directly if precision matters.
  - HighGold Mining Inc.: ILLEGIBLE: contact_email — official page displays it in reversed character order (a JS-deobfuscation trick), not decoded. Nicole Hoeller, VP Communications, is the named Investor/Corporate Development contact, same phone.
  - Patagonia Gold Corp.: Confirmed active (TSXV: PGDC), Vancouver-headquartered, Argentina-focused gold/silver explorer. ILLEGIBLE: street_address, contact_email, contact_phone — site fetch failed on this attempt. Recommend re-verifying directly if precision matters.
  - Rio Tinto Exploration Canada Inc: Rio Tinto's Canadian operations are primarily centered on Iron Ore Company of Canada (Quebec/Labrador) and Rio Tinto Fer et Titane (Quebec) rather than a distinct Vancouver office. ILLEGIBLE: street_address, contact_email, contact_phone. Recommend direct verification if this entity matters.
  - Iberdrola Energy Projects Canada Corporation: This is a Canadian project-development subsidiary of Iberdrola S.A. (Spanish multinational utility). ILLEGIBLE: street_address, contact_email, contact_phone. Not a mining company — energy/utility sector. Recommend direct verification if this entity matters.
  - MGX Minerals Inc: Confirmed active — led by CEO/Founder Jared Lazerson, advancing the Fran Gold Project near Fort St. James, BC (~$18-20 million invested, 104+ drill holes). Official website is currently non-functional ('Site Under Construction'). ILLEGIBLE: street_address, contact_email, contact_phone. Recommend re-verifying if the site comes back online.
  - Basin Uranium Corp: Confirmed active as of Dec 2024 (CSE-listed, Vancouver-based). ILLEGIBLE: street_address, contact_email, contact_phone, website — no official site located distinct from financial-news aggregators. Recommend a direct CSE/SEDAR+ search if this entity matters.
  - Altima Energy Inc: renamed from Altima Resources Ltd in December 2024. ILLEGIBLE: street_address, contact_email, contact_phone, website. Recommend a direct search if this entity matters.
  - Lumina Metals Corp: contact Scott Hicks, shicks@luminagold.com, +1 604 646 1890, per search results — recorded for reference but not verified directly). ILLEGIBLE: street_address, contact_email, contact_phone for Lumina Metals specifically. Recommend re-verifying directly if precision matters.
  - B C & Yukon Chamber of Mines: This organization renamed itself the Association for Mineral Exploration British Columbia (AME BC) in 2005 — this is the current name and site, still Vancouver-based. Verified this is distinct from the similarly-named 'Yukon Chamber of Mines' (Whitehorse, YT), which some search results conflated it with. Not a mining company itself but the region's lead mineral-exploration industry association — a real, active, contactable organization. ILLEGIBLE: contact_email — obfuscated on the official page.
- Quality flags: 1
  - POSTAL_FORMAT: Niocorp Developments Ltd postal_code='80112' does not match A1A 1A1

**Running total:** 311 unique companies — {'complete': 132, 'detail_only': 124, 'listing_only': 55}

**Notes:** 18 companies from the $4.44M-$6.07M tier processed. Vicuña Corp is a genuinely significant, active find (Lundin Mining/BHP joint venture). 6 flagged REVIEW as acquired (International Enexco, Arizona Mining, Kaminak Gold, Constantine Metal Resources, Bellhaven Copper & Gold, Nevada Copper) plus 3 unlocatable (First Coal, Woulfe Mining, GB Minerals, Waroona Energy). Several remain unresearched due to time — will continue.

## Run 2026-08-10

**Source:** Contact lookup, batch 23 — closes out the $4.44M-$4.8M tier.

**Files processed:**
- `https://bmcminerals.com/contact-us/`

- Rows added: 0
- Rows updated: 5
- Rows unchanged: 0
- Conflicts: 1
  - BMC Minerals Ltd: CONFLICT: province=British Columbia|BC (https://bmcminerals.com/contact-us/)
- ILLEGIBLE flags: 31
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
  - Golden Shield Resources Inc: ILLEGIBLE: street_address, contact_email, contact_phone. Recommend a direct SEDAR+/CSE search if this entity matters.
  - Western Magnesium Corporation: Confirmed active, Vancouver-headquartered (magnesium production technology). ILLEGIBLE: street_address, contact_email, contact_phone — not present in static HTML. Recommend re-verifying directly if precision matters.
  - HighGold Mining Inc.: ILLEGIBLE: contact_email — official page displays it in reversed character order (a JS-deobfuscation trick), not decoded. Nicole Hoeller, VP Communications, is the named Investor/Corporate Development contact, same phone.
  - Patagonia Gold Corp.: Confirmed active (TSXV: PGDC), Vancouver-headquartered, Argentina-focused gold/silver explorer. ILLEGIBLE: street_address, contact_email, contact_phone — site fetch failed on this attempt. Recommend re-verifying directly if precision matters.
  - Rio Tinto Exploration Canada Inc: Rio Tinto's Canadian operations are primarily centered on Iron Ore Company of Canada (Quebec/Labrador) and Rio Tinto Fer et Titane (Quebec) rather than a distinct Vancouver office. ILLEGIBLE: street_address, contact_email, contact_phone. Recommend direct verification if this entity matters.
  - Iberdrola Energy Projects Canada Corporation: This is a Canadian project-development subsidiary of Iberdrola S.A. (Spanish multinational utility). ILLEGIBLE: street_address, contact_email, contact_phone. Not a mining company — energy/utility sector. Recommend direct verification if this entity matters.
  - MGX Minerals Inc: Confirmed active — led by CEO/Founder Jared Lazerson, advancing the Fran Gold Project near Fort St. James, BC (~$18-20 million invested, 104+ drill holes). Official website is currently non-functional ('Site Under Construction'). ILLEGIBLE: street_address, contact_email, contact_phone. Recommend re-verifying if the site comes back online.
  - Basin Uranium Corp: Confirmed active as of Dec 2024 (CSE-listed, Vancouver-based). ILLEGIBLE: street_address, contact_email, contact_phone, website — no official site located distinct from financial-news aggregators. Recommend a direct CSE/SEDAR+ search if this entity matters.
  - Altima Energy Inc: renamed from Altima Resources Ltd in December 2024. ILLEGIBLE: street_address, contact_email, contact_phone, website. Recommend a direct search if this entity matters.
  - Lumina Metals Corp: contact Scott Hicks, shicks@luminagold.com, +1 604 646 1890, per search results — recorded for reference but not verified directly). ILLEGIBLE: street_address, contact_email, contact_phone for Lumina Metals specifically. Recommend re-verifying directly if precision matters.
  - B C & Yukon Chamber of Mines: This organization renamed itself the Association for Mineral Exploration British Columbia (AME BC) in 2005 — this is the current name and site, still Vancouver-based. Verified this is distinct from the similarly-named 'Yukon Chamber of Mines' (Whitehorse, YT), which some search results conflated it with. Not a mining company itself but the region's lead mineral-exploration industry association — a real, active, contactable organization. ILLEGIBLE: contact_email — obfuscated on the official page.
- Quality flags: 1
  - POSTAL_FORMAT: Niocorp Developments Ltd postal_code='80112' does not match A1A 1A1

**Running total:** 311 unique companies — {'complete': 133, 'detail_only': 123, 'listing_only': 55}

**Notes:** Closes out this revenue tier. BMC Minerals confirmed strongly active (recent ASX IPO). Xrapplied Technologies flagged as a NAICS misclassification. Arlac Transamerican and Bucking Horse Energy had no locatable record.

## Run 2026-08-10

**Source:** Contact lookup, batch 24 — continuing the older backlog's $2.04M-$4.26M tier.

**Files processed:**
- none

- Rows added: 0
- Rows updated: 5
- Rows unchanged: 0
- Conflicts: 4
  - CapitalEnergy Corporation: CONFLICT: province=British Columbia|BC (search-engine snippets (scrapmonster.com, not the company's own site))
  - eCobalt Solutions Inc: CONFLICT: province=British Columbia|BC (search-engine snippet (D&B directory listing for the address; ecobalt.com itself was checked directly and found squatted))
  - Mason Resources Corp: CONFLICT: province=British Columbia|BC (secondary sources (name-change filings, not fetched directly))
  - Woodfibre LNG Limited Partnership: CONFLICT: province=British Columbia|BC (search-engine snippet (mailing address only; the live contact page renders via JavaScript, no static content found))
- ILLEGIBLE flags: 32
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
  - Golden Shield Resources Inc: ILLEGIBLE: street_address, contact_email, contact_phone. Recommend a direct SEDAR+/CSE search if this entity matters.
  - Woodfibre LNG Limited Partnership: ILLEGIBLE: contact_email, contact_phone. Recommend re-verifying directly if a street address/phone matters.
  - Western Magnesium Corporation: Confirmed active, Vancouver-headquartered (magnesium production technology). ILLEGIBLE: street_address, contact_email, contact_phone — not present in static HTML. Recommend re-verifying directly if precision matters.
  - HighGold Mining Inc.: ILLEGIBLE: contact_email — official page displays it in reversed character order (a JS-deobfuscation trick), not decoded. Nicole Hoeller, VP Communications, is the named Investor/Corporate Development contact, same phone.
  - Patagonia Gold Corp.: Confirmed active (TSXV: PGDC), Vancouver-headquartered, Argentina-focused gold/silver explorer. ILLEGIBLE: street_address, contact_email, contact_phone — site fetch failed on this attempt. Recommend re-verifying directly if precision matters.
  - Rio Tinto Exploration Canada Inc: Rio Tinto's Canadian operations are primarily centered on Iron Ore Company of Canada (Quebec/Labrador) and Rio Tinto Fer et Titane (Quebec) rather than a distinct Vancouver office. ILLEGIBLE: street_address, contact_email, contact_phone. Recommend direct verification if this entity matters.
  - Iberdrola Energy Projects Canada Corporation: This is a Canadian project-development subsidiary of Iberdrola S.A. (Spanish multinational utility). ILLEGIBLE: street_address, contact_email, contact_phone. Not a mining company — energy/utility sector. Recommend direct verification if this entity matters.
  - MGX Minerals Inc: Confirmed active — led by CEO/Founder Jared Lazerson, advancing the Fran Gold Project near Fort St. James, BC (~$18-20 million invested, 104+ drill holes). Official website is currently non-functional ('Site Under Construction'). ILLEGIBLE: street_address, contact_email, contact_phone. Recommend re-verifying if the site comes back online.
  - Basin Uranium Corp: Confirmed active as of Dec 2024 (CSE-listed, Vancouver-based). ILLEGIBLE: street_address, contact_email, contact_phone, website — no official site located distinct from financial-news aggregators. Recommend a direct CSE/SEDAR+ search if this entity matters.
  - Altima Energy Inc: renamed from Altima Resources Ltd in December 2024. ILLEGIBLE: street_address, contact_email, contact_phone, website. Recommend a direct search if this entity matters.
  - Lumina Metals Corp: contact Scott Hicks, shicks@luminagold.com, +1 604 646 1890, per search results — recorded for reference but not verified directly). ILLEGIBLE: street_address, contact_email, contact_phone for Lumina Metals specifically. Recommend re-verifying directly if precision matters.
  - B C & Yukon Chamber of Mines: This organization renamed itself the Association for Mineral Exploration British Columbia (AME BC) in 2005 — this is the current name and site, still Vancouver-based. Verified this is distinct from the similarly-named 'Yukon Chamber of Mines' (Whitehorse, YT), which some search results conflated it with. Not a mining company itself but the region's lead mineral-exploration industry association — a real, active, contactable organization. ILLEGIBLE: contact_email — obfuscated on the official page.
- Quality flags: 1
  - POSTAL_FORMAT: Niocorp Developments Ltd postal_code='80112' does not match A1A 1A1

**Running total:** 311 unique companies — {'complete': 137, 'detail_only': 124, 'listing_only': 50}

**Notes:** 5 companies processed. Important finding: eCobalt Solutions' former domain (ecobalt.com) has been taken over by an unrelated gambling/sweepstakes affiliate site — same domain-squatting pattern as Cache Exploration flagged earlier in this project. Not used for anything.

## Run 2026-08-10

**Source:** Contact lookup, batch 25 — full sweep of the remaining 50 untouched listing_only backlog companies (5 parallel research passes, A-E). Web-egress in the research sandboxes was blocked for direct site fetches; most results are sourced from search-engine-indexed snippets of official pages rather than freshly fetched pages, flagged per company.

**Files processed:**
- none

- Rows added: 0
- Rows updated: 50
- Rows unchanged: 0
- Conflicts: 35
  - Design Maintenance Systems Inc: CONFLICT: province=British Columbia|BC (search-indexed content (desmaint.com contact page; yellowpages.ca) — direct fetch of desmaint.com blocked in this session)
  - Latin Explore Inc: CONFLICT: province=British Columbia|BC (juniorminingnetwork.com, newsfilecorp.com press releases; latin-explore.com)
  - Select Sands Corp: CONFLICT: province=British Columbia|BC (selectsands.com/contact, thenewswire.com, rockproducts.com)
  - Hunter Dickinson Acquisition Inc: CONFLICT: province=British Columbia|BC (hdimining.com (search-indexed), dnb.com business directory)
  - Gold Line Resources Ltd: CONFLICT: province=British Columbia|BC (investing.com company profile, dnb.com, juniorminingnetwork.com)
  - XXL Energy Corp: CONFLICT: province=British Columbia|BC (opencorpdata.com (registered address, cross-referenced against SEDAR+); xxlenergy.com not directly fetched (network egress blocked))
  - Fox Exploration Limited: CONFLICT: province=British Columbia|BC (cylex-canada.ca, foxexploration.ca (search-indexed, direct fetch blocked))
  - Fuse Advisors Inc: CONFLICT: province=British Columbia|BC (slrconsulting.com press release, ised-isde.canada.ca (Investment Canada Act notice))
  - Atrum Coal Groundhog Inc: CONFLICT: province=British Columbia|BC (listcorp.com, tipranks.com)
  - Thesis Gold (Holdings) Inc: CONFLICT: province=British Columbia|BC (newswire.ca press release, thesisgold.com/contact (search-indexed, direct fetch blocked))
  - North Atlantic Titanium Corp: CONFLICT: province=British Columbia|BC (natitanium.com/contact (search-indexed, direct fetch blocked), proactiveinvestors.com)
  - Quebec Innovative Materials Corp: CONFLICT: province=British Columbia|BC (qimaterials.com, issuers.thecse.com (search-indexed, direct fetch blocked))
  - Canamex Gold Corp: CONFLICT: province=British Columbia|BC (canamexgold.com/contacts (search-indexed, direct fetch blocked), thecse.com listing)
  - Ashmont Resources Corp: CONFLICT: province=British Columbia|BC (search-indexed content from ashmont.ca (direct fetch blocked))
  - BM&H Oilfield Solutions Ltd: CONFLICT: province=British Columbia|BC (search-indexed content from bmhoilfield.com (direct fetch blocked))
  - Northern Prince Lng Inc.: CONFLICT: province=British Columbia|BC (northernprincelng.com/contact-1 (search-indexed, direct fetch blocked); Canada Energy Regulator REGDOCS filing C29880; canadacompanyregistry.com (address, lower confidence))
  - Miata Metals Corp.: CONFLICT: province=British Columbia|BC (miatametals.com/contact and /corporate (search-indexed, direct fetch blocked))
  - Gemdale Gold Inc.: CONFLICT: province=British Columbia|BC (gemdalegold.com/corporate/corporate-directory (search-indexed, direct fetch blocked))
  - Pulse Oil Corp: CONFLICT: province=British Columbia|BC (globenewswire.com (Oct 2024 AGM release), pulseoilcorp.com/contact (search-indexed, direct fetch blocked), theglobeandmail.com)
  - Offsetters Clean Technology Inc: CONFLICT: province=British Columbia|BC (en.wikipedia.org/wiki/Offsetters)
  - Esrey Resources Ltd: CONFLICT: province=British Columbia|BC (esreyresources.com/corporate-2 (search-indexed, direct fetch blocked), globenewswire.com (Feb 2020 management-change release), advfn.com)
  - Geoscience BC Society: CONFLICT: province=British Columbia|BC (geosciencebc.com/contactus and /about-us (search-indexed, direct fetch blocked))
  - Adroit Resources Inc: CONFLICT: province=British Columbia|BC (marketwired.com press release, miningfeeds.com (secondary directory, address corroboration))
  - Aurea Mining Inc: CONFLICT: province=British Columbia|BC (stale historical press releases (circa 2007, EQS News/ProQuest archive))
  - Anglo Coal Canada Inc: CONFLICT: province=British Columbia|BC (fasken.com, angloamerican.com press release (2025-11-02))
  - Golden Predator Exploration Ltd: CONFLICT: province=British Columbia|BC (whitehorsechamber.ca, cambridgehouse.com, yellowpages.ca, globenewswire.com (2016 CFO appointment release))
  - JKR Gold Resources Inc: CONFLICT: province=British Columbia|BC (sec.gov EDGAR filings, pitchbook.com)
  - Coral Gold Resources Ltd: CONFLICT: province=British Columbia|BC (sec.gov EDGAR Form 20-F (pre-acquisition), newswire.ca press release)
  - Bearing Lithium Corp: CONFLICT: province=British Columbia|BC (globenewswire.com press releases (Dec 2022))
  - Goldsource Mines Inc: CONFLICT: province=British Columbia|BC (newsfilecorp.com press release, goldsourcemines.com/corporate/corporate-info (search-cached, direct fetch blocked))
  - Continuum Resources Ltd: CONFLICT: province=British Columbia|BC (biv.com, rttnews.com)
  - Chubu Electric Power Cordova Gas LTD: CONFLICT: province=British Columbia|BC (search summary (Mitsubishi Corporation / Penn West Cordova Embayment JV reporting, 2010-2011))
  - Newstrike Capital Inc: CONFLICT: province=British Columbia|BC (biv.com, globenewswire.com (May 2015 release))
  - Global Cobalt Corporation: CONFLICT: province=British Columbia|BC (juniorminingnetwork.com press release, globalcobaltcorp.com (search-cached, direct fetch blocked))
  - Intrusion Precious Metals Corp: CONFLICT: province=British Columbia|BC (thenewswire.com, bcsc.bc.ca reporting-issuers list, globenewswire.com (name-change release, April 2024))
- ILLEGIBLE flags: 32
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
  - Golden Shield Resources Inc: ILLEGIBLE: street_address, contact_email, contact_phone. Recommend a direct SEDAR+/CSE search if this entity matters.
  - Woodfibre LNG Limited Partnership: ILLEGIBLE: contact_email, contact_phone. Recommend re-verifying directly if a street address/phone matters.
  - Western Magnesium Corporation: Confirmed active, Vancouver-headquartered (magnesium production technology). ILLEGIBLE: street_address, contact_email, contact_phone — not present in static HTML. Recommend re-verifying directly if precision matters.
  - HighGold Mining Inc.: ILLEGIBLE: contact_email — official page displays it in reversed character order (a JS-deobfuscation trick), not decoded. Nicole Hoeller, VP Communications, is the named Investor/Corporate Development contact, same phone.
  - Patagonia Gold Corp.: Confirmed active (TSXV: PGDC), Vancouver-headquartered, Argentina-focused gold/silver explorer. ILLEGIBLE: street_address, contact_email, contact_phone — site fetch failed on this attempt. Recommend re-verifying directly if precision matters.
  - Rio Tinto Exploration Canada Inc: Rio Tinto's Canadian operations are primarily centered on Iron Ore Company of Canada (Quebec/Labrador) and Rio Tinto Fer et Titane (Quebec) rather than a distinct Vancouver office. ILLEGIBLE: street_address, contact_email, contact_phone. Recommend direct verification if this entity matters.
  - Iberdrola Energy Projects Canada Corporation: This is a Canadian project-development subsidiary of Iberdrola S.A. (Spanish multinational utility). ILLEGIBLE: street_address, contact_email, contact_phone. Not a mining company — energy/utility sector. Recommend direct verification if this entity matters.
  - MGX Minerals Inc: Confirmed active — led by CEO/Founder Jared Lazerson, advancing the Fran Gold Project near Fort St. James, BC (~$18-20 million invested, 104+ drill holes). Official website is currently non-functional ('Site Under Construction'). ILLEGIBLE: street_address, contact_email, contact_phone. Recommend re-verifying if the site comes back online.
  - Basin Uranium Corp: Confirmed active as of Dec 2024 (CSE-listed, Vancouver-based). ILLEGIBLE: street_address, contact_email, contact_phone, website — no official site located distinct from financial-news aggregators. Recommend a direct CSE/SEDAR+ search if this entity matters.
  - Altima Energy Inc: renamed from Altima Resources Ltd in December 2024. ILLEGIBLE: street_address, contact_email, contact_phone, website. Recommend a direct search if this entity matters.
  - Lumina Metals Corp: contact Scott Hicks, shicks@luminagold.com, +1 604 646 1890, per search results — recorded for reference but not verified directly). ILLEGIBLE: street_address, contact_email, contact_phone for Lumina Metals specifically. Recommend re-verifying directly if precision matters.
  - B C & Yukon Chamber of Mines: This organization renamed itself the Association for Mineral Exploration British Columbia (AME BC) in 2005 — this is the current name and site, still Vancouver-based. Verified this is distinct from the similarly-named 'Yukon Chamber of Mines' (Whitehorse, YT), which some search results conflated it with. Not a mining company itself but the region's lead mineral-exploration industry association — a real, active, contactable organization. ILLEGIBLE: contact_email — obfuscated on the official page.
- Quality flags: 1
  - POSTAL_FORMAT: Niocorp Developments Ltd postal_code='80112' does not match A1A 1A1

**Running total:** 311 unique companies — {'complete': 165, 'detail_only': 146}

**Notes:** 50 companies from the long-standing untouched backlog processed via 5 parallel research passes (A-E). Roughly two-thirds turned out to be REVIEW cases (acquired/merged/renamed/subsidiary/dormant/misclassified) — consistent with this being the lowest-revenue, lowest-hit-rate tier of the original D&B list. Live active independent companies found with real contact info: Latin Explore Inc, Select Sands Corp (though REVIEW/foreclosure), Gold Line Resources Ltd, North Atlantic Titanium Corp, Quebec Innovative Materials Corp, Canamex Gold Corp, Northern Prince Lng Inc (REVIEW/misclassified), Miata Metals Corp, Gemdale Gold Inc, Pulse Oil Corp (REVIEW/misclassified), Geoscience BC Society (not a mining company), Intrusion Precious Metals Corp. This closes out the full 50-company backlog identified as untouched at the start of this run.

## Run 2026-08-10

**Source:** Chat-pasted D&B listing screenshots, next batch down by revenue ($2.04M-$1.46M tier). Candidate-list only; per user instruction, no advanced/contact-search research at this very low revenue tier.

**Files processed:**
- `chat-listing-2026-08-10-15.png`
- `chat-listing-2026-08-10-16.png`
- `chat-listing-2026-08-10-17.png`
- `chat-listing-2026-08-10-18.png`

- Rows added: 48
- Rows updated: 1
- Rows unchanged: 0
- Conflicts: 2
  - First Coal Corporation: CONFLICT: revenue_raw=$5.14M|$1.84M (chat-listing-2026-08-10-16.png)
  - First Coal Corporation: CONFLICT: revenue_usd_millions=5.14|1.84 (chat-listing-2026-08-10-16.png)
- ILLEGIBLE flags: 32
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
  - Golden Shield Resources Inc: ILLEGIBLE: street_address, contact_email, contact_phone. Recommend a direct SEDAR+/CSE search if this entity matters.
  - Woodfibre LNG Limited Partnership: ILLEGIBLE: contact_email, contact_phone. Recommend re-verifying directly if a street address/phone matters.
  - Western Magnesium Corporation: Confirmed active, Vancouver-headquartered (magnesium production technology). ILLEGIBLE: street_address, contact_email, contact_phone — not present in static HTML. Recommend re-verifying directly if precision matters.
  - HighGold Mining Inc.: ILLEGIBLE: contact_email — official page displays it in reversed character order (a JS-deobfuscation trick), not decoded. Nicole Hoeller, VP Communications, is the named Investor/Corporate Development contact, same phone.
  - Patagonia Gold Corp.: Confirmed active (TSXV: PGDC), Vancouver-headquartered, Argentina-focused gold/silver explorer. ILLEGIBLE: street_address, contact_email, contact_phone — site fetch failed on this attempt. Recommend re-verifying directly if precision matters.
  - Rio Tinto Exploration Canada Inc: Rio Tinto's Canadian operations are primarily centered on Iron Ore Company of Canada (Quebec/Labrador) and Rio Tinto Fer et Titane (Quebec) rather than a distinct Vancouver office. ILLEGIBLE: street_address, contact_email, contact_phone. Recommend direct verification if this entity matters.
  - Iberdrola Energy Projects Canada Corporation: This is a Canadian project-development subsidiary of Iberdrola S.A. (Spanish multinational utility). ILLEGIBLE: street_address, contact_email, contact_phone. Not a mining company — energy/utility sector. Recommend direct verification if this entity matters.
  - MGX Minerals Inc: Confirmed active — led by CEO/Founder Jared Lazerson, advancing the Fran Gold Project near Fort St. James, BC (~$18-20 million invested, 104+ drill holes). Official website is currently non-functional ('Site Under Construction'). ILLEGIBLE: street_address, contact_email, contact_phone. Recommend re-verifying if the site comes back online.
  - Basin Uranium Corp: Confirmed active as of Dec 2024 (CSE-listed, Vancouver-based). ILLEGIBLE: street_address, contact_email, contact_phone, website — no official site located distinct from financial-news aggregators. Recommend a direct CSE/SEDAR+ search if this entity matters.
  - Altima Energy Inc: renamed from Altima Resources Ltd in December 2024. ILLEGIBLE: street_address, contact_email, contact_phone, website. Recommend a direct search if this entity matters.
  - Lumina Metals Corp: contact Scott Hicks, shicks@luminagold.com, +1 604 646 1890, per search results — recorded for reference but not verified directly). ILLEGIBLE: street_address, contact_email, contact_phone for Lumina Metals specifically. Recommend re-verifying directly if precision matters.
  - B C & Yukon Chamber of Mines: This organization renamed itself the Association for Mineral Exploration British Columbia (AME BC) in 2005 — this is the current name and site, still Vancouver-based. Verified this is distinct from the similarly-named 'Yukon Chamber of Mines' (Whitehorse, YT), which some search results conflated it with. Not a mining company itself but the region's lead mineral-exploration industry association — a real, active, contactable organization. ILLEGIBLE: contact_email — obfuscated on the official page.
- Quality flags: 1
  - POSTAL_FORMAT: Niocorp Developments Ltd postal_code='80112' does not match A1A 1A1

**Running total:** 359 unique companies — {'complete': 165, 'detail_only': 145, 'listing_only': 49}

**Notes:** 49 unique companies added from the $2.04M-$1.46M revenue tier (one duplicate, Computational Geosciences Inc, appeared across two overlapping screenshots and was merged into a single row). Per user instruction, no advanced/contact-search research performed at this tier — listing data only. First Coal Corporation was already a row in the workbook (previously flagged REVIEW/no public record located in batch 22); this listing entry will just backfill its revenue figure. Quest Mortgage Corp flagged as a likely NAICS misclassification (name suggests a lending company, not mining).

## Run 2026-08-13

**Source:** Stage 3 (recent news / corporate actions) — single-company request: Thesis Gold. 12-month lookback from 2026-08-13 (back to ~2025-08-13).

**Files processed:**
- none

- Rows added: 0
- Rows updated: 1
- Rows unchanged: 0
- Conflicts: 0
- ILLEGIBLE flags: 32
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
  - Golden Shield Resources Inc: ILLEGIBLE: street_address, contact_email, contact_phone. Recommend a direct SEDAR+/CSE search if this entity matters.
  - Woodfibre LNG Limited Partnership: ILLEGIBLE: contact_email, contact_phone. Recommend re-verifying directly if a street address/phone matters.
  - Western Magnesium Corporation: Confirmed active, Vancouver-headquartered (magnesium production technology). ILLEGIBLE: street_address, contact_email, contact_phone — not present in static HTML. Recommend re-verifying directly if precision matters.
  - HighGold Mining Inc.: ILLEGIBLE: contact_email — official page displays it in reversed character order (a JS-deobfuscation trick), not decoded. Nicole Hoeller, VP Communications, is the named Investor/Corporate Development contact, same phone.
  - Patagonia Gold Corp.: Confirmed active (TSXV: PGDC), Vancouver-headquartered, Argentina-focused gold/silver explorer. ILLEGIBLE: street_address, contact_email, contact_phone — site fetch failed on this attempt. Recommend re-verifying directly if precision matters.
  - Rio Tinto Exploration Canada Inc: Rio Tinto's Canadian operations are primarily centered on Iron Ore Company of Canada (Quebec/Labrador) and Rio Tinto Fer et Titane (Quebec) rather than a distinct Vancouver office. ILLEGIBLE: street_address, contact_email, contact_phone. Recommend direct verification if this entity matters.
  - Iberdrola Energy Projects Canada Corporation: This is a Canadian project-development subsidiary of Iberdrola S.A. (Spanish multinational utility). ILLEGIBLE: street_address, contact_email, contact_phone. Not a mining company — energy/utility sector. Recommend direct verification if this entity matters.
  - MGX Minerals Inc: Confirmed active — led by CEO/Founder Jared Lazerson, advancing the Fran Gold Project near Fort St. James, BC (~$18-20 million invested, 104+ drill holes). Official website is currently non-functional ('Site Under Construction'). ILLEGIBLE: street_address, contact_email, contact_phone. Recommend re-verifying if the site comes back online.
  - Basin Uranium Corp: Confirmed active as of Dec 2024 (CSE-listed, Vancouver-based). ILLEGIBLE: street_address, contact_email, contact_phone, website — no official site located distinct from financial-news aggregators. Recommend a direct CSE/SEDAR+ search if this entity matters.
  - Altima Energy Inc: renamed from Altima Resources Ltd in December 2024. ILLEGIBLE: street_address, contact_email, contact_phone, website. Recommend a direct search if this entity matters.
  - Lumina Metals Corp: contact Scott Hicks, shicks@luminagold.com, +1 604 646 1890, per search results — recorded for reference but not verified directly). ILLEGIBLE: street_address, contact_email, contact_phone for Lumina Metals specifically. Recommend re-verifying directly if precision matters.
  - B C & Yukon Chamber of Mines: This organization renamed itself the Association for Mineral Exploration British Columbia (AME BC) in 2005 — this is the current name and site, still Vancouver-based. Verified this is distinct from the similarly-named 'Yukon Chamber of Mines' (Whitehorse, YT), which some search results conflated it with. Not a mining company itself but the region's lead mineral-exploration industry association — a real, active, contactable organization. ILLEGIBLE: contact_email — obfuscated on the official page.
- Quality flags: 1
  - POSTAL_FORMAT: Niocorp Developments Ltd postal_code='80112' does not match A1A 1A1

**Running total:** 359 unique companies — {'complete': 165, 'detail_only': 145, 'listing_only': 49}

**Notes:** Stage 3 on one company (Thesis Gold) at user request. Five in-window items found across four categories: expansion/new project (x2), management change, IPO/listing change, capital raise. No insolvency or acquisition-of-this-company signals — the company is the acquirer/consolidator side of its history, and is well capitalised. Also corrects a factual error in the batch-25 REVIEW note for this row (Centerra was miscast as a merger party, and the 2023 Benchmark combination was omitted).
