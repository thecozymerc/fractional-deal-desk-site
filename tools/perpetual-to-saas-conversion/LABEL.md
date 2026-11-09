# LABEL — tools/perpetual-to-saas-conversion

**Page ID:** S6-P01.b
**Tool / piece ID:** Tool 2 — Perpetual-to-SaaS Conversion Calculator
**Address:** /tools/perpetual-to-saas-conversion/
**What this folder holds:** Perpetual-to-SaaS Conversion Calculator — stay-put vs 3 SaaS options, break-even + crossover. Since v3 (Nov 8, 2026) each SaaS option also carries the Tool 1 factors: a one-time coupon credit (Year 1 only) and a usage line (per use / per API request / per 1K tokens / per 1M tokens, with usage discount and committed monthly minimum).

**Files:** `S6-P01b-perpetual-to-saas-conversion.html` — the tool page (write-up from Draft 1.11 Part II §6 verbatim + one mechanics sentence updated for v3 + the embedded workbook + booking CTA); `S6-P01b-perpetual-to-saas-conversion-data.js` — the workbook's cells converted from "Perpetual-to-SaaS Conversion Calculator — SAMPLE v3.xlsx" by convert-workbook.py (1 sheet, 332 cells, 25 inputs, 107 formulas as machinery, plus the sheet's LineChart spec). The sheet calculates with its OWN formulas via the shared formula engine (assets/formula-engine.js, extended with INDEX/MATCH for this workbook); the chart is drawn by the shared renderer from the same computed cells. Verified Nov 8, 2026: workbook recalculated in LibreOffice (19 headline checks, all pass — Option A Year 1 $23,700, 5-year $148,500; Option C 5-year $136,100; usage A $1,200/yr, C $1,800/yr; coupons $4,000) and the site's formula engine compared against LibreOffice on all 107 formula cells across 5 scenarios (defaults; Option A at $45,000; horizon 3; metered-usage-binds; per-use type) — 535 comparisons, zero differences.

Rule (Code Labeling System): this label is updated in the same change as anything in this folder. Every change is recorded in the site CHANGELOG.md, and the CODE-MAP.md entry is updated in the same move.
