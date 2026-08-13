# Website Prospect Reader — working notes for Claude

This repo builds a prospecting workbook of companies (currently: Vancouver-area
mining/materials companies from a D&B directory) with contact info suitable for
outreach. See `README.md` for the screenshot-transcription pipeline mechanics
(`extract_pipeline.py`, staging JSON format, merge rules). This file covers the
*web contact-enrichment* workflow layered on top of that, and the ground rules
for doing this kind of prospecting work in general.

## Why this exists

The end user is an industrial CRE broker (CBRE). The point of this whole
pipeline isn't "build a company database" for its own sake — it's to hand
their brokerage team a warm-outreach list: which companies, which contact,
and *why now* (a signal suggesting they might need industrial space —
expanding, raising capital, hiring for a new site, being acquired, etc.).
When a stage-3 signal and a CRE opportunity read differently, favor framing
that answers "why would this company need to lease/buy/sell industrial real
estate right now" over generic corporate-news framing.

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
  `expansion/new project`, `management change`, `insolvency/receivership`,
  `hiring/expansion signal`. Prefix each item in `recent_news` with its
  category, e.g. `"acquisition/merger: acquired by X Corp (2026-03-14)"`.
  Multiple items for one company go in the same cell, semicolon-separated,
  each with its own category prefix and date.
- **`hiring/expansion signal` is the CRE-specific category** — added for
  the CBRE-outreach use case above. This means postings for roles like
  site/plant/facility manager, warehouse operations lead, or a hiring
  surge at a specific location — a real leading indicator that a company
  is scaling up a physical footprint before any press release exists.
  Source these from public job-board search (Indeed, company career
  pages, publicly-indexed postings) via WebSearch, not from LinkedIn.
  **Do not connect to or scrape LinkedIn for this or anything else** —
  its ToS explicitly prohibits automated data extraction and it actively
  enforces that (rate limiting, detection, account bans, and it has sued
  scrapers, e.g. hiQ Labs). That's the same "active bot-defense, hard
  stop" category as the Cloudflare/Reblaze blocks noted above, not
  something a personal login changes. LinkedIn's own API is partner-gated
  for ads/recruiting, not general company-signal lookup.
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

## Stage 4: the relationship graph (shared officers, directors, offices)

Vancouver junior mining runs on shared boards, shared management companies
and shared office suites. Hunter Dickinson Inc is the textbook case — a
private group providing management and technical services to a portfolio of
listed companies, holding the lease itself while the listed entities are
effectively tenants of its service model. Mapping those links turns one
conversation into several prospects and, more importantly, identifies who
actually signs a lease.

**Why it earns its place for CBRE:** one meeting can reach every company in
a management group; the real decision-maker is the management company, not
the listed shell; a shared officer is a warm-intro path; and it dedupes the
workbook by revealing which "companies" are really one office.

### Schema

`People` is a second worksheet, deliberately not more columns on
`Companies`: person-to-company is many-to-many and will not flatten into one
cell without losing the role, the dates and the provenance that make an edge
trustworthy. (This is the opposite call from `recent_news`, which *is* 1:1
with a company and so stayed on the main sheet.)

One row per `(person, company, role)` assertion, append-only. Nothing is
overwritten; a contradicting source becomes its own edge and is surfaced by
`people_checks()`. Derived onto `Companies`: `co_located_with`,
`related_companies`, `management_group` — recomputed by `--derive` on every
run, never hand-edited.

### Source hierarchy — Tier 1 is the spine, Tier 2 is a freshness overlay

Never the reverse.

- **tier1_filing** — management information circulars (Form 51-102F5), which
  disclose each director nominee's *other public-company directorships*
  along with age and city of residence; insider filings, which are
  person-keyed and carry a persistent identifier plus dated
  appointment/departure events; AIFs (51-102F2); CSE Form 2A listing
  statements.
- **registry** — BC Corporate Registry. The only option for the many
  non-reporting private companies here. Note OrgBook BC does *not* carry
  director data any more than it carries addresses.
- **tier2_website** — company Board/Management pages. Fresher than an annual
  circular but unstructured, and companies routinely fail to remove
  departed people.
- **Never** — data brokers, LinkedIn, or org-chart aggregators. theorg.com
  and theofficialboard.com both surface in searches for this and are both
  derivative.

Before any bulk retrieval from SEDAR+, check its terms: there is no open
public API, and automated bulk access may not be permitted. Targeted manual
lookups are fine. Treat this the same as the other hard rules — verify, do
not assume.

### Invert the crawl

Do not iterate companies. Insider reporting is **person-keyed**: one lookup
returns every issuer a person is an insider of, including companies not yet
in the workbook. Seed from officers of companies already clustered, then
expand one or two hops. Fewer queries, better recall, and every edge comes
from a filing rather than a marketing page.

### Entity resolution — where this quietly breaks

**Company name is not a key.** This workbook has already hit eight
near-collisions (Prodigy Gold Inc vs Prodigy Gold NL, Viscount Mining
Resources vs Viscount Mining Corp, Contango Mining Canada vs Contango ORE,
Irwin vs Irving Resources, XCite Resources vs Xcite Energy, Uec Resources vs
Uranium Energy, Adroit Resources mining vs Adroit Resources IT-staffing,
Lumina Metals vs Lumina Gold) and a dozen renames (Muzhu → North Atlantic
Titanium, Benchmark → Thesis Gold → Thesis Gold & Silver, Taseko → Trekor
Metals, Major Precious Metals → Intrusion, EMC Metals → Scandium
International, and more). Record every former name in `former_names`;
`build_alias_index()` resolves staging entries that use an older name onto
the existing row instead of creating a duplicate. Anchor identity to a hard
identifier where available — BC incorporation number, or CUSIP/ISIN.

**Person disambiguation: never merge on name alone.** Require two
corroborating attributes. `normalize_person()` strips honorifics and
post-nominals but deliberately does *not* collapse initials onto full names,
because "J. Smith" and "John Smith" may be different people. Available
discriminators: middle initials, professional suffixes (P.Geo, CPA, ICD.D),
age and city of residence from circulars, and the persistent insider ID,
which is definitive when present.

### Date every edge

A graph without dates is wrong. Every edge carries `role_start`, `role_end`,
`as_of_date` and its source's filing date; "current board" is a query, not a
stored fact. Acting on a stale interlock is the Sid Keswani error at graph
scale — that trap has already been hit twice in this project.

### Weighting — shared officers, not shared directors

Interlocking directorates here are so common they are nearly meaningless
raw. A non-executive board seat never drives a lease; a shared officer does.

| Signal | Weight |
| --- | --- |
| Shared officer (CEO/CFO/COO/GC/VP) | High |
| Shared executive chairman | High (recorded `role_type: both`) |
| Shared non-executive director | Low — `related_companies` only |
| Same suite | Medium, corroborating |
| Same building only | Weak, labelled as such |
| Registered/records office suite | Zero — in `EXCLUDED_CLUSTER_SUITES` |

`management_group` requires **≥2 shared officers, or ≥1 shared officer plus
co-location.** A shared board seat alone never forms a group.

Two address subtleties learned the hard way:

- Exclusions are keyed by **suite, not building**. Cathedral Place holds both
  a law firm acting as registered office *and* First Majestic's genuine head
  office; excluding the tower wrongly dropped a real co-location.
- Group corroboration uses **building level, not suite level**. A management
  company spreads its entities across floors — Hunter Dickinson occupies the
  12th, 14th and 15th of 1040 West Georgia — so a suite test misses exactly
  the pattern this is meant to catch. The shared-officer requirement carries
  the weight; the address only guards against a lone coincidence.

`people_checks()` flags any officer asserted at more than six companies at
once: that is usually two people collapsed by normalisation, not a finding.

### Validate before scaling

Run the method against a company whose answer is already knowable and score
it. The HDI pilot (`staging/run_2026-08-13_people_hdi_pilot.json`) is the
reference: it correctly grouped HDI with Northern Dynasty on three shared
officers, correctly *declined* to group Trekor Metals where only directors
are shared, resolved the Taseko→Trekor rename through the alias index, and
discovered two companies the D&B candidate list never contained. Then audit
a random 10% against primary filings and write the error rate down, so the
dataset can be handed over with a stated precision rather than a shrug.

Report confidence tiers separately. Do not blend tier1 filing edges,
website edges and registry edges into a single number.

### Cost

One research pass per company, same profile as contact enrichment — so the
same rule applies: **ask which subset before starting.** Never assume the
whole workbook.

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
