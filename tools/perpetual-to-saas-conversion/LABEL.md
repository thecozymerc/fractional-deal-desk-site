# LABEL — tools/perpetual-to-saas-conversion

**Address:** /tools/perpetual-to-saas-conversion/
**What this folder holds:** Perpetual-to-SaaS Conversion Calculator — stay-put vs 3 SaaS options, break-even + crossover.

**Files (built Nov 8, 2026):** `S6-P01b-perpetual-to-saas-conversion.html` — the tool page (write-up from Draft 1.11 Part II §6 verbatim + the embedded workbook + booking CTA); `S6-P01b-perpetual-to-saas-conversion-data.js` — the workbook's cells converted from "Perpetual-to-SaaS Conversion Calculator — SAMPLE v2.xlsx" by convert-workbook.py (1 sheet, 240 cells, 7 inputs, 103 formulas as machinery, plus the sheet's LineChart spec). The sheet calculates with its OWN formulas via the shared formula engine (assets/formula-engine.js, extended with INDEX/MATCH for this workbook); the chart is drawn by the shared renderer from the same computed cells. Verified against LibreOffice: 309 comparisons, zero differences.

Rule (Code Labeling System): this label is updated in the same change as anything in this folder. Every change is recorded in the site CHANGELOG.md, and the CODE-MAP.md entry is updated in the same move.
