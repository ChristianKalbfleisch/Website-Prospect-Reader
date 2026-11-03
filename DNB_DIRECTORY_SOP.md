# SOP — building a D&B directory target list for a city/sector

How to turn a D&B Business Directory search into a prospect list, given that
dnb.com cannot be scraped. Written after the Richmond BC run of 2026-10-01.

## Read this first: the site cannot be automated

Tested 2026-10-01 against all four Richmond directory URLs: **12 requests, 12
Cloudflare managed-challenge responses** (`Just a moment...`, HTTP 403). This
is a standing block on `/business-directory/`, not a rate limit that clears.

Two further reasons not to push at it:

- **D&B's terms of use prohibit automated collection** from the directory.
- Their `robots.txt` disallows `/business-directory/` for AI crawlers
  (`GPTBot`) specifically — a deliberate position on this exact path.

This project's standing rule (`CLAUDE.md`) is that an **active bot defence is a
hard stop, always** — no header spoofing, no headless-browser workaround, no
retry loops. That rule exists because the alternative risks the firm's IP
range and breaches a vendor's terms. It applies here.

**What does work is a human in the loop.** A person browsing normally is not
blocked. So the split is: a person captures, the pipeline processes. That is
exactly what this repo is built for, and how the 361-row mining workbook was
produced.

## The two-stage workflow

### Stage 1 — capture (a person, in a normal browser)

1. **Get the URL right.** The pattern is
   `https://www.dnb.com/business-directory/ca/<province>/<city>/<sector>/companies`
   — for example
   `https://www.dnb.com/business-directory/ca/british_columbia/richmond/manufacturing/companies`.
   **Omitting `/british_columbia/richmond/` silently gives you the Canada-wide
   list.** That single mistake is what put Magna International and BCE on a
   Richmond manufacturing tab. Load the page and confirm the heading says the
   city before capturing anything.
2. **Dismiss the overlays before screenshotting.** The D&B live-chat bubble and
   the floating phone button sit on top of the rightmost column and will hide
   SALES REVENUE.
3. **Capture the listing pages** — pages 1–3 of each sector. Save to
   `screenshots/listing/` as `<sector>_p1.png`, `_p2.png`, `_p3.png`.
4. **Capture the detail pages you actually want.** The company name in blue is a
   link to the company profile, which carries street address, phone, website and
   the key principal. The **"see more contacts"** link on that profile confirms
   the principal's job title. Save to `screenshots/detail/` as
   `<company-slug>.png` (and `<company-slug>_contacts.png` for the title page).
5. **Be selective at stage 4.** 599 companies is 599 page loads and roughly
   1,200 screenshots. Shortlist first — by sector, revenue band or employee
   count off the listing pages — then capture detail only for the shortlist.
   This is the step that makes or breaks the run's cost.

### Stage 2 — transcribe and merge (automated, in this repo)

6. Read each unprocessed file in `screenshots/` and write what is **legibly
   printed** into a staging JSON (`staging/run_<date>_<batch>.json`). Nothing is
   inferred. A field that is obscured, cut off or paywalled stays `null` with the
   reason in `notes` as `ILLEGIBLE: <field> — <reason>`. Partial numbers are
   never transcribed. Format is in `README.md`.
7. `python3 extract_pipeline.py staging/<file>.json` merges it into
   `output/mining_master.xlsx`, runs the quality checks and appends to the log.
   Re-running the same payload adds nothing — processed filenames are skipped.

## Field-by-field notes

| Field | Where it comes from | Caveat |
| --- | --- | --- |
| Company name | listing table | Reconstructing it from the URL slug loses ampersands and commas. Take it off the page. |
| Sales revenue | **listing table only** | On the profile page it sits behind a lock icon. Capture it from the results table or not at all. |
| Street address, phone, website | company profile page | One page load each. |
| Key principal name | company profile page | |
| Principal job title | **"see more contacts" page** | The profile alone often shows the name without a confirmed title. |
| Email, direct phone | **not published** | Free directory does not carry them — they sit behind a D&B Hoovers subscription. Leave blank. Never derive one from a firm's email pattern. |
| Province spelling | varies by page type | Listing prints `British Columbia`, profile prints `BC`. This trips the conflict rule by design; first value captured wins and the clash is logged. |

## Before you use D&B at all, consider the better source

For a **Richmond** list specifically, **City of Richmond business licence open
data** is the stronger starting point: every licensed business in the city, with
street address, phone and full/part-time employee counts, filterable by NAICS to
manufacturing, transportation and warehousing, wholesale trade and construction.
It is free, authoritative, has no terms problem and needs no screenshots.

D&B's advantage is revenue banding and a named principal. So the efficient play
is: **licence data for the universe and the addresses, D&B detail captures only
for the shortlist you actually intend to call.**

## Quality rules that apply to any run

- **Never fabricate** an address, email, phone or name. A blank with a reason
  beats a plausible guess — these lists get emailed and dialled.
- **Verify geography against the company's own site**, not the directory. Two
  companies in the mining run were listed in Vancouver but published a Calgary
  and a Dallas head office respectively.
- **Flag, never delete.** A company that is acquired, dissolved, a subsidiary of
  another row, or misclassified gets a `REVIEW` note; rows are only annotated.
- **Watch for near-collisions.** Company name is not a key — the mining workbook
  hit eight (Prodigy Gold Inc vs Prodigy Gold NL, Lumina Metals vs Lumina Gold,
  and so on). Record former names and resolve through the alias index.
