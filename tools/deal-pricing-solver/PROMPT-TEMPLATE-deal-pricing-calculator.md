# PROMPT TEMPLATE — The Deal Pricing Calculator pattern (S6-P01.a)

**What this is:** the reusable prompt that rebuilds the Deal Pricing Calculator — and, with the blanks refilled, the NEXT calculator the same way. Lucky asked for this on Nov 8, 2026: "create a prompt template for this first calculator so that we can make the exact thing next time easily."
**Filed for:** page S6-P01.a (Pricing Engines). Copies live in: this page folder · the site code folder `site/tools/deal-pricing-solver/` · the Drive mirror folder "S6-P01.a — Deal Pricing Solver (Calculator)" · the GitHub repo folder `tools/deal-pricing-solver/`.
**How to use it:** copy PART 1, fill every [BRACKET] from the new tool's own source documents, keep PART 2's rules as-is, and judge the build against PART 3. PART 4 shows how the brackets were filled for S6-P01.a itself — the worked instance.

---

## PART 1 — THE PROMPT (copy, fill the brackets, send)

Build a working web calculator for [PAGE ID — e.g. S6-P01.c] — [TOOL NAME] — for the Fractional Deal Desk & Contract Management site.

**Sources first.** Read these source documents IN FULL before building anything: [SOURCE DOC 1 — the model/workbook], [SOURCE DOC 2 — the design PDF/doc]. Every feature, default, and sample below comes from those documents or from my rulings — invent nothing. If a feature in the sources is internal-only (real company names, internal links, codenames), scrub it: generic playful sample names only, never the real vendor's.

**The math identity.** [THE CORE FORMULA(S) — e.g. Net PUPM = List × (1 − Discount) × (1 − Partner Margin); Net PUPM = Net ARPU ÷ Months]. Percent fields are real percents (typing 45 means 45%). Blank inputs show blank results, never errors.

**Views.** [NUMBER] views, switched by tabs:
1. [VIEW 1 NAME — the main build view]: [WHAT IT DOES].
2. [VIEW 2 NAME — the comparison view]: [WHAT IT COMPARES — old vs new, both sides fully lined].

**Line types (every view that takes lines):**
- **Product lines:** a dropdown of preset products (name + list price) that fills the row; the NAME IS EDITABLE (typing replaces the preset name); unit/list price; seat count; discount %; partner margin % where the model uses it. Computed per line: [PER-LINE OUTPUTS — e.g. net per-unit price, ARPU, ACV, TCV].
- **Usage lines, built INTO the same views (never a separate page):** meter dropdown — per use / per 1,000 tokens / per 1,000,000 tokens; units per month; price per unit; included/committed minimum units; discount %. Computed: gross, net monthly, annual, effective per-unit price, per-seat equivalent.
- **Add AND delete lines** on every table: an "+ Add a line" button and a ✕ on every row; deleting renumbers the rest; new rows are live immediately.
- **Coupons:** a $ coupon field on every product line — a flat amount off that line's contract value, spread evenly across its years. Deal totals and comparisons run on AFTER-coupon values.
- **Usage-threshold concession:** pick a meter, a monthly threshold, and an extra % — when that meter's units reach the threshold, the extra % comes off that meter's net. Show plainly whether the concession is ACTIVE or not reached.
- **Rules/checks the source carries:** [E.G. SKU-MIX RULES — keyed to a hidden product-family tag on each line so renamed lines can't break the checks; show PASS/FAIL per rule].

**Totals and variance.** Deal totals combine product lines AND usage lines over the deal term. The comparison view shows, per line and in total: [VARIANCE FAMILY — e.g. Seat ±, ARPU ±, ARPA ±, ACV ±, TCV ±] as % change old → new ("—" when the old value is 0).

**Sample data.** Defaults must reproduce the source documents' own worked examples EXACTLY (they are the test suite — Part 3). Preset product names: playful, made-up, NOT the real vendor's and not a pun on it: [PRESET NAMES + PRICES].

**Design.** The site's D01 system: warm off-white paper, navy ink, one deep-teal accent, serif display + sans body, hairline rules, the tool inside a framed document panel, inputs yellow, computed values green-tinted, dense INSIDE the tool frame and sparse around it. Phone-first: no sideways scrolling, tap targets ≥ 48px. NEVER display a formula anywhere.

**Files.** In the page's own folder: the page HTML (site shell: same header/footer/booking button as the other pages; the page's write-up verbatim from the copy of record, with only the mechanics paragraph describing THIS tool) + `[PAGE ID]-calculator.js` (pure math first, then wiring) + `[PAGE ID]-calculator.css` (every rule scoped under `.calc`).

**Companion workbook.** Build the same calculator as a live-formula spreadsheet ([TOOL NAME] — SAMPLE.xlsx): START HERE tab + one tab per view; yellow inputs, green formulas; percent cells stored as real percents. Any place the sheet must differ from the page (e.g. checks matched by name instead of hidden tags), say so on its START HERE tab.

**Records (the standing Build Checklist, same pass):** the page folder's LABEL · CODE-MAP (bump version) · CHANGELOG · the page's PAGE.md · the folder charts regenerated · SITEMAP-TABLE status · the Drive mirror (Page Text Sheet + code files) · the GitHub repo folder · a Plans tab -19 log entry. One folder per page in every repository.

## PART 2 — RULES THAT NEVER CHANGE

1. The source documents are read in full first; their worked examples are the acceptance tests.
2. Nothing invented: no facts, no figures, no testimonials, no features the sources don't carry or Lucky didn't rule in.
3. Scrub anything internal: no real vendor names, codenames, or internal links in the public build — playful generic sample names instead.
4. Formulas are machinery, never display.
5. Build everything asked in ONE pass, then bring it back for Lucky's good/bad ruling — review versions are expected (this calculator took four).
6. Verify before reporting: the math against the sources' worked examples AND the companion workbook recalculated in a real spreadsheet engine — page and sheet must agree.
7. **THE FACTORS STANDARD (Lucky, Nov 8, 2026 — applies to Tool 1, Tool 2, and every pricing tool after):** every pricing tool keeps the full factor set in mind, adapted to its job — product lines with dropdown presets + editable names + add/delete; a coupon field per line; usage lines built INTO the deal views, never a separate tab (unit types: per use / per API request / per 1,000 tokens / per 1,000,000 tokens; a usage discount; a committed monthly minimum); and a usage-threshold concession where it fits the tool's job. The umbrella word is **usage** — tokens are one unit type inside it, never the headline word. Applied so far: S6-P01.a (the full set, as shipped) and S6-P01.b v3 (coupon adapted as a one-time Year-1 credit per option + a usage line per option; the concession's role there is played by the committed monthly minimum).

## PART 3 — THE ACCEPTANCE TESTS (S6-P01.a's actual numbers)

A rebuild of the Deal Pricing Calculator is only done when ALL of these reproduce:
- Baselines: List $30.00, Discount 45%, Partner Margin 20% → Net PUPM **$13.20** → Net ARPU **$158.40**. Solver in all three directions (solve List / solve Discount / solve Margin) returns 30.00 / 45% / 20%.
- TCV form: TCV $114,048 over 4 years, 180 seats → ACV **$28,512**, ARPU **$158.40**, PUPM **$13.20**.
- Expansion utility: $20.10 → +10% = **$22.11**, −10% = **$18.09**.
- Old deal line: List $30, 45%, 20%, 50 seats, 36 months → CPL/mo **$660.00**, ACV **$7,920.00**, TCV **$23,760.00**.
- New deal totals (PDF sample lines): ACV **$46,800.86**, TCV **$140,402.59**, 571 seats; line 1 ARPU **$133.58**, ARPU ± **−15.67%**, ACV ± **+45.05%**.
- With the $1,500 coupon on line 1: after-coupon totals ACV **$46,300.86** / TCV **$138,902.59**; old-vs-new line 1 after-coupon variance **+38.74%**, seat ± **+72%**.
- Usage concession (60 units ≥ threshold 50, extra 5%): metered net **$153.90/mo** and the banner reads CONCESSION ACTIVE; usage change old → new **+30.63%**.
- Full deal TCV (products + usage over the first line's term): **$144,442.99**.
- SKU-mix checks on the sample mix: top-tier line FAILS its floor (86 seats vs floor 100), mid-tier cumulative PASSES (230 ≤ 300).

## PART 4 — HOW THE BRACKETS WERE FILLED FOR S6-P01.a

- [TOOL NAME] Deal Pricing Calculator · [PAGE ID] S6-P01.a, address /tools/deal-pricing-solver/
- [SOURCES] "Deal Pricing & Scenario Evaluation Model.xlsx" (original model) + "Enterprise Deal Pricing Engine.pdf"
- [VIEWS] (1) New Deal — baselines, dual-layout solver (flat matrix + dropdown Smart Form), TCV form, product lines, usage lines, concession, expansion utility. (2) Old vs New — old footprint + proposed lines, dropdowns and usage on BOTH sides, variance per line and total, SKU-mix checks.
- [PRESETS] Plus Ultra $30 (top tier) · Core Standard $23 · Biz Plus $22 (mid tier) · Frontline Lite $4 · None $0.
- [RULES] SKU-mix: each top-tier SKU ≥ max(15% of seats, 100 seats); mid-tier SKUs cumulative ≤ 300 seats; frontline no rules — keyed to a hidden family tag per line.
- [FILES] S6-P01a-deal-pricing-solver.html + S6-P01a-deal-pricing-calculator.js + S6-P01a-deal-pricing-calculator.css · companion "Deal Pricing Calculator — SAMPLE.xlsx".

*Template created Nov 8, 2026 (Log 17.12), from the calculator built the same day (Logs 17.5–17.9).*
