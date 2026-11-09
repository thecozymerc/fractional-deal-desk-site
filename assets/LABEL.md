# LABEL — assets

**Address:** (shared)
**What this folder holds:** Shared styling and scripts for the whole site — the D01 design tokens (colours, type, spacing) live here, once, for every page.
**Files:** `styles.css` — the shared D01 design system (every page). `spreadsheet-tool.js` — the shared workbook renderer: renders a converted workbook as the actual spreadsheet on a page (sheet tabs, live yellow INPUT cells, computed results, formulas never shown). `formula-engine.js` — the shared formula engine: evaluates each workbook's OWN formulas in the browser, so no tool's math is ever re-implemented by hand. (Retired: `mini-solver.js`, an invented shortcut, Nov 7; `homepage-solver.js`, a hand-built replica, Nov 8 — Lucky's rule: embed the actual sheet, usable, without showing the formulas.)

Rule (Code Labeling System): this label is updated in the same change as anything in this folder. Every change is recorded in the site CHANGELOG.md, and the CODE-MAP.md entry is updated in the same move.
