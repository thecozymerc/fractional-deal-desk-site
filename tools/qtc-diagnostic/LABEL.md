# LABEL — tools/qtc-diagnostic

**Address:** /tools/qtc-diagnostic/
**What this folder holds:** S6-P05.3 QTC Diagnostic + Story 3 — quote-to-cash maturity x risk diagnostic. BUILT AND LIVE Nov 11, 2026 (Tool 7): page S6-P05c-qtc-diagnostic.html + data S6-P05c-qtc-diagnostic-data.js (converted from the restart's verified v2 diagnostic SAMPLE workbook, ALLINPUT mode, the workbook's one formatted column (error rate %, at 0%) mapped to whole-percent display; the workbook's two optional context columns — cycle days, error rate — are read by no formula, as its own note states). Verifying this tool caught the shared engine skipping cached error values inside aggregate ranges; SUM/AVERAGE/MIN/MAX now propagate range errors as Excel does, and every earlier tool re-verified clean after the change.

Rule (Code Labeling System): this label is updated in the same change as anything in this folder. Every change is recorded in the site CHANGELOG.md, and the CODE-MAP.md entry is updated in the same move.
