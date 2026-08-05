# Website Prospect Reader — working notes for Claude

This repo builds a prospecting workbook of companies (currently: Vancouver-area
mining/materials companies from a D&B directory) with contact info suitable for
outreach. See `README.md` for the screenshot-transcription pipeline mechanics
(`extract_pipeline.py`, staging JSON format, merge rules). This file covers the
*web contact-enrichment* workflow layered on top of that, and the ground rules
for doing this kind of prospecting work in general.

## The two-stage pipeline

1. **Candidate list.** Get a raw list of company names for the target
   universe — currently sourced from pasted D&B directory screenshots
   (`_page_type: "listing"` in staging JSON), filtered to a sector +
   geography. Revenue and location come from this step.
2. **Contact enrichment.** For each company, find its own official
   website and pull: registered/operating address, a named contact if one
   is published, and email/phone. This is the `_page_type: "detail"` step,
   and it's manual/agentic research (WebSearch + fetch), not part of
   `extract_pipeline.py`'s automation — I do this by hand, batch by batch,
   then write a staging JSON and run it through the pipeline like any other
   detail-page batch.

## Contact-enrichment hard rules

- **Official sources only.** Fetch the company's own website. Never use
  third-party data-broker aggregators (RocketReach, LeadIQ, ZoomInfo,
  GetProspect, ContactOut, etc.) even when they surface in search results —
  their data is unverified and scraped. If a broker result is the only
  thing available, don't use it; note the gap instead.
- **robots.txt disallows are not a hard stop by user instruction** — I may
  fetch a disallowed path if the user has told me to (they explicitly
  removed that constraint on 2026-08-05 for this project). Absent explicit
  instruction otherwise, prefer not to.
- **Active bot-defenses are a hard stop, always.** Cloudflare
  "managed challenge" responses (`cf-mitigated: challenge` header),
  Reblaze/other bot-management blocks that explicitly cite a ToS violation,
  and similar active security controls are never bypassed — no headless
  browser tricks, no header spoofing, no retries. Leave the field blank and
  say why. This is different in kind from a passive `robots.txt` entry.
- **Never decode/bypass email obfuscation** (spambot-protection scripts,
  "\[email protected\]" placeholders, `*protected email*` renders). Leave
  `contact_email` blank with a note.
- **Never use expired-TLS-cert domains** — don't connect insecurely to
  verify a stale site.
- **Watch for domain squatting/takeover.** If a company's expected domain
  now serves unrelated content (gambling affiliate sites have shown up
  twice so far), don't treat it as the company's site. Flag it explicitly
  so a future run doesn't get fooled the same way.
- **Never fabricate an address, email, phone, or name.** Blank + a reason
  in `notes` beats a plausible guess, every time. This includes not
  reusing another company's address as if it were independently verified —
  when I fill a subsidiary's address from its parent's already-verified
  row, the note says so explicitly ("same registered office as X, not
  independently verified for this entity").
- **Named individual + personal email is the exception, not the norm.**
  Most companies publish a role (VP Investor Relations, Director
  Corporate Development) with a role-based or obfuscated email. Record
  what's actually published; don't infer a person exists just because a
  title does.

## The REVIEW flag

Set `status`/`notes` to flag a row for manual review (via a `detail`-page
entry with mostly-null fields and a clear REVIEW note) whenever a company
in the candidate list is not actually a live, independent prospect:

- **Acquired/merged** — route the note to the acquirer if that acquirer is
  already a row in the workbook (e.g. Calibre Mining → Equinox Gold).
- **Bankrupt/dissolved/inactive** for years — the listing entry is stale.
- **Subsidiary/project vehicle** of a company already in the workbook —
  not a separate office.
- **Not actually where the source list claims** — verify against the
  company's *own* site. Two real examples this project hit: a company
  listed as Vancouver whose own site showed a Calgary office, and another
  whose own site showed a Dallas, TX head office with only a transfer
  agent (not the company) at the Vancouver address given. Always trust the
  company's own published office location over the candidate-list source.
- **Likely misclassified** — e.g. a tobacco-alternatives company or a
  freight-forwarding company showing up under a mining NAICS code. Don't
  silently drop these; flag them so a human decides.

Never silently delete a flagged row — the merge pipeline's rule is rows are
never removed, only annotated.

## OrgBook BC, for the record

OrgBook's free API (`orgbook.gov.bc.ca/api/v4/...`) gives entity status
(active/historical/dissolved) and registration dates for BC-incorporated
companies, but does **not** carry registered-address data in practice —
the `address.registries.ca` schema exists but isn't populated for the
entities checked so far. Don't expect an address from it. A defunct
company's historical address would need BC Registry's paid search product.

## Schema

`extract_pipeline.py`'s `COLUMNS` includes `contact_email` and
`contact_phone` (added 2026-08-05) alongside the original D&B-derived
fields. Extend `COLUMNS`/`DATA_FIELDS`/`DETAIL_FIELDS`/`widths` together if
a future task needs another field — don't bolt it on elsewhere.

## Stage 3: recent news / corporate actions

An optional third stage on top of contact enrichment: for each company,
search for material corporate-action news and record it in two columns —
`recent_news` and `news_source_urls` — not a separate sheet.

- **Lookback window: 12 months** from the date the check is run. Don't
  report older news as if current; if the only thing findable is stale,
  leave it blank rather than padding the cell with old news.
- **Fixed category list** (use these labels verbatim so the column stays
  scannable): `acquisition/merger`, `capital raise`, `IPO/listing change`,
  `expansion/new project`, `management change`, `insolvency/receivership`.
  Prefix each item in `recent_news` with its category, e.g.
  `"acquisition/merger: acquired by X Corp (2026-03-14)"`. Multiple items
  for one company go in the same cell, semicolon-separated, each with its
  own category prefix and date.
- **Every item needs a source URL** in `news_source_urls` (semicolon-
  separated, same order as the items in `recent_news`), same as every
  other populated field in this workbook — no asserting a corporate
  action without a link to back it up.
- **This overlaps with REVIEW-flagging.** An `insolvency/receivership` or
  `acquisition/merger` hit found during this stage is exactly the kind of
  thing that should also produce/update a REVIEW note if it means the
  company isn't a live independent prospect — don't record it as a news
  item only and leave the row looking like a normal active lead.
- **Cost scales with company count, same as contact enrichment** — one
  search+read per company. Always ask (or wait to be told) how many
  companies/which subset to run this against before starting; don't
  assume "the whole workbook" by default.

## Generalizing beyond Vancouver mining

The contact-enrichment half of this pipeline (stage 2 above) is already
industry-agnostic — it's just "find the company's own site, pull address +
contact, apply the hard rules above." What's specific to this repo so far
is the *candidate-list source* (D&B screenshots) and the *filter*
(Vancouver, mining/materials sector).

To point this at a different industry/geography (e.g. "top N shipping
companies in a given city"), the candidate-list step needs a different
source — a public directory, an industry association list, a stock
exchange sector filter, etc. — screenshots aren't required; a plain list of
company names is enough input to start stage 2. Ask what source the user
already has in mind before assuming D&B/TMX-style research is needed
again; skip straight to enrichment if they just hand over names.
