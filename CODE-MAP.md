# CODE MAP — every file and folder in the site code, in plain English

This is the master file (Code Labeling System, Rule 1). One entry per file or folder: what it does, in plain words.
If it is not on this map, it does not belong. Updated in the same change as the code — never later (Rule 3).
Every change is also recorded in CHANGELOG.md.

**Map version:** 14 — November 8, 2026 (Tool 2 v3 + review system: S6-P01.b's workbook rebuilt as v3 with the Tool 1 factors — one-time coupon credits + per-option usage lines — data reconverted (332 cells, 25 inputs, 107 formulas), verified against LibreOffice across 5 scenarios, 535 comparisons, zero differences. Both tool pages now carry Tool ID label lines (Tool 1 / Tool 2), and the Tool Review Checklist sheet exists as the standing review record — every build session updates it (Build Checklist steps 7–8). v13 note stands: BOTH hosts live — GitHub Pages at thecozymerc.github.io/fractional-deal-desk-site/ and Cloudflare Pages at fractional-deal-desk-site.pages.dev, the same publish tree on both; Cloudflare deploys run through the API token connector (custom.cloudflare), never the browser. All internal links stay relative so one tree serves both hosts.)

**File naming convention (Lucky's instruction, Nov 7):** every page's code file is named with its page ID + the descriptive title from the sitemap table — e.g. `P01-homepage.html`. The ID in the filename, the page's `<title>`, and the label comment at the top of the file always agree. At publish, a copy of each page file is placed as `index.html` in its own folder so the sitemap address resolves (e.g. `/tools/deal-check/`); the ID-named file stays the source of truth, and the publish step is recorded in the CHANGELOG like any other change.

## The control files
- `CODE-MAP.md` (this file) — the master list of everything, in plain English.
- `CHANGELOG.md` — one entry per change: date, page or file, what changed, in plain words. Any change on any page is recorded (Lucky's rule, Nov 7).
- `LABEL.md` (one in every folder) — what that folder holds; updated in the same change as the folder's contents.

## The pages
- `site/` — **/** — Homepage — the story page (Sections 1–6, proof strip, FAQ, booking route). Sells the diagnostic.
- `site/services/` — **/services/** — Services & Pricing — Section 5 in full; pricing anchored at /services/#pricing.
- `site/about/` — **/about/** — About — Section 1 long version: photo, first-person story, external links. Optional at launch.
- `site/tools/` — **/tools/** — Tools hub — Section 6 home: job labels, featured tools, counts, routes to every partition.
- `site/tools/pricing-engines/` — **/tools/pricing-engines/** — S6-P01 Pricing Engines — partition page for the 3 pricing tools.
- `site/tools/deal-pricing-solver/` — **/tools/deal-pricing-solver/** — the Deal Pricing Calculator — Lead Tool #1 (Lucky's designed calculator, Nov 8, 2026: new-deal pricing, old-vs-new comparison, per-use/per-token, coupons, usage concessions). Address stays /tools/deal-pricing-solver/.
- `site/tools/perpetual-to-saas-conversion/` — **/tools/perpetual-to-saas-conversion/** — S6-P01.b · Tool 2 — Perpetual-to-SaaS Conversion Calculator — stay-put vs 3 SaaS options, break-even + crossover; since v3 each option also carries a one-time coupon credit (Year 1 only) and a usage line (per use / per token, discount, committed minimum). **Built Nov 8, 2026; v3 same night:** `S6-P01b-perpetual-to-saas-conversion.html` (write-up verbatim from Draft 1.11 Part II §6 + one mechanics sentence for v3 + embedded workbook + CTA) and `S6-P01b-perpetual-to-saas-conversion-data.js` (converted from "Perpetual-to-SaaS Conversion Calculator — SAMPLE v3.xlsx": 1 sheet, 332 cells, 25 inputs, 107 formula cells + the sheet's LineChart spec, drawn by the renderer from the same computed cells). Verified: engine == LibreOffice on all 107 formula cells × 5 scenarios = 535 comparisons, zero differences; workbook headline checks 19/19 in LibreOffice (Option A 5-year $148,500; Option C $136,100; usage A $1,200/yr, C $1,800/yr; coupons $4,000).
- `site/tools/perm-calculator/` — **/tools/perm-calculator/** — Perm Calculator — the scrubbed 22-tab sample, playable, formulas hidden.
- `site/tools/spend-variance/` — **/tools/spend-variance/** — S6-P02 Spend Variance — Lead Tool #2 runs on this partition page (variance + renewal tracker).
- `site/tools/stories-and-sandboxes/` — **/tools/stories-and-sandboxes/** — S6-P05 Stories & Sandboxes — partition page for the 4 story + tool pairs.
- `site/tools/intake-gate/` — **/tools/intake-gate/** — S6-P05.1 Intake Gate + Story 1 — pre-sales qualification sandbox.
- `site/tools/redlining-playbook/` — **/tools/redlining-playbook/** — S6-P05.2 Redlining Playbook + Story 2 — clause-by-clause fallback positions from the playbook workbook.
- `site/tools/qtc-diagnostic/` — **/tools/qtc-diagnostic/** — S6-P05.3 QTC Diagnostic + Story 3 — quote-to-cash maturity x risk diagnostic.
- `site/tools/bundling-sandbox/` — **/tools/bundling-sandbox/** — S6-P05.4 Bundling Sandbox + Story 4 — rate-card bundling / good-better-best.
- `site/tools/contract-operations/` — **/tools/contract-operations/** — S6-P03 Contract Operations — partition page for the 3 operations tools.
- `site/tools/deal-check/` — **/tools/deal-check/** — S6-P03.1 The Deal Check — the 6-step deal-health checklist (email gate: OPEN, pending Lucky).
- `site/tools/contract-migration-triage/` — **/tools/contract-migration-triage/** — S6-P03.2 Contract Migration & Triage Tracker — enhanced tracker with metadata + tiering.
- `site/tools/case-operations-capacity/` — **/tools/case-operations-capacity/** — S6-P03.3 Case Operations Triage Tool — 30-case register, KPI counts, capacity simulator.
- `site/tools/contracts-library/` — **/tools/contracts-library/** — S6-P06 Contracts Library — the 15 adapted forms as annotated cards, full label, no raw downloads.
- `site/tools/contracts-library/tier-1/` — **/tools/contracts-library/tier-1/** — S6-P06.1 Tier 1 — Lead Commercial Paper: 5 forms shown up front.
- `site/tools/contracts-library/tier-2/` — **/tools/contracts-library/tier-2/** — S6-P06.2 Tier 2 — Core Enterprise Paper: 5 forms shown up front.
- `site/tools/contracts-library/tier-3/` — **/tools/contracts-library/tier-3/** — S6-P06.3 Tier 3 — Specialized: 5 forms buried (back drawer).
- `site/tools/executive-intelligence/` — **/tools/executive-intelligence/** — S6-P04 Executive Intelligence — partition page: scoring tool, dashboard, back drawer of 7 previews.
- `site/tools/weighted-decision-scoring/` — **/tools/weighted-decision-scoring/** — Weighted Decision Scoring Tool — the framework scoring tool + worked vendor example.
- `site/tools/executive-dashboard/` — **/tools/executive-dashboard/** — Executive Dashboard — the live 36-case sample under a generic name.
- `site/assets/` — **(shared)** — Shared styling and scripts for the whole site — the D01 design tokens (colours, type, spacing) live here, once, for every page.

## Code files
- `services/P02-services-and-pricing.html` — **P02 · /services/** — Services & Pricing: Draft 1.10 Section 5 in full (phases, hero offer, service menu, billing); every price locked-verbatim; /services/#pricing anchors at Phase 1.
- `P01-homepage.html` (in `site/`) — **P01 · /** — the homepage: Sections 1–6 in Draft 1.11 order, proof strip, booking route. Copy: Draft 1.10 verbatim (tight homepage cut). Design: D01.
- `assets/styles.css` — the shared D01 design system (colours, type scale, spacing scale, radius) for every page. A change here changes every page.
- `assets/spreadsheet-tool.js` — the shared workbook renderer: renders a converted workbook on any page as the actual spreadsheet (sheet tabs, the sheet's own rows and words, yellow INPUT cells live, formula cells showing computed values only — formulas never written to the page).
- `assets/formula-engine.js` — the shared formula engine: evaluates the workbook's OWN formulas in the visitor's browser (IF, SUM, COUNTIF-family, INDEX, MATCH, comparisons, ranges), so an embedded sheet calculates exactly like the spreadsheet — nothing re-implemented by hand per tool. Verified against LibreOffice recalculations of the actual workbooks.
- `tools/deal-pricing-solver/S6-P01a-deal-pricing-solver.html` — **S6-P01.a · /tools/deal-pricing-solver/** — the Deal Pricing Solver tool page: Draft 1.10 write-up (mechanics paragraph updated Nov 8) + the DEAL PRICING CALCULATOR, live. Since Nov 8, 2026 (Lucky's ruling) the page holds the designed calculator, not the workbook embed; the embed's data files stay in the folder unused, and the formula engine still powers S6-P01.b.
- `tools/deal-pricing-solver/S6-P01a-deal-pricing-calculator.js` — the calculator itself (Nov 8, 2026): pure CALC math (verified in node against the Pricing Engine model's worked examples) + page wiring for the New Deal and Old vs New views. Never displays a formula.
- `tools/deal-pricing-solver/S6-P01a-deal-pricing-calculator.css` — the calculator's styles, every rule scoped under .calc; token values match D01.
- `tools/deal-pricing-solver/S6-P01a-deal-pricing-solver-data.js` — the workbook's cells, converted from "Deal Pricing Solver — SAMPLE.xlsx" by `website-project/convert-workbook.py` (text + input values + number formats + the sheet's formulas as machinery for the formula engine; formulas are never displayed). Currently unused — kept as the original-wording provenance copy. Re-run the converter instead of hand-editing.
- `tools/deal-pricing-solver/S6-P01a-deal-pricing-solver-data-revised.js` — the REVISED DESCRIPTIONS data: converted from "Deal Pricing Solver — SAMPLE (Revised Descriptions).xlsx" (in the tool-builds folder, next to the untouched original). Every description, label, and note is reworded to read better on screen; every number and input is identical (verified by diff — only text cells differ). **Loaded by the P01 homepage hero embed only** (the S6-P01.a tool page carries the calculator since Nov 8, 2026).
- Retired Nov 8 (later): `tools/deal-pricing-solver/S6-P01a-deal-pricing-solver-compute.js` — the hand-written calculation module. Lucky's call: embed the sheet and let its own formulas do the work. Replaced by the formula engine; the file is in the trash, recoverable.
- Retired: `assets/mini-solver.js` (Nov 7, invented shortcut — trashed) and `assets/homepage-solver.js` (Nov 8, hand-built replica — trashed). Lucky's rule, restated Nov 8: site tools are the actual spreadsheet, usable, minus the formulas — never a hand-made miniature or replica.
