# S6-P02 — Tool 4 — Spend Variance & Renewal Tracker

- **Page ID:** S6-P02 · **Piece:** Tool 4
- **Address:** /tools/spend-variance/
- **Files:** `S6-P02-spend-variance.html` · `index.html`
- **Current build:** Argon full rebuild (Nov 12, 2026) — a control board,
  not a spreadsheet embed: sticky 5-card KPI strip, "Needs a Decision"
  exception list, three editable tables (Contract Register with
  editable notice window · Actual vs Forecast with editable REVIEW
  threshold · Invoice Audit Log), and a copyable Portfolio Brief.
  Sample data and anchors identical to the retired workbook build
  ($4,542,500 · 6 · $28,960 / 1.3% · REVIEW 4 / 3, as-of 2026-11-11).
  Argon wrote code and page words under the prompt + completeness /
  freedom-within-bounds addendum in ~/workspace/tool4-build/.
  Verified: anchors + interaction battery (24 checks), zero page
  errors.
- **Status:** LIVE on Cloudflare + GitHub Pages (Nov 12, 2026),
  pending Lucky's Review 1.
- **Retired iteration:** the workbook-embed build (page + data.js)
  is archived — GitHub branch `tool-4-iterations`, folder
  `tool-4-workbook/`; Drive folder "Tool 4 — Workbook Embed
  (retired)"; local snapshot ~/workspace/tool4-build/original-live-copy-2026-11-12/.

- **Grouping revision (Nov 12, 2026, later):** Section 02 rebuilt as
  per-contract groups with subtotals (the register generates the
  groups; empty contracts collapse to one line); Section 03 contract
  column is printed text with a single add-time picker. All per-row
  contract dropdowns removed at Lucky's ruling — the contract is
  context, set once. Group subtotals: Apex +$3,530 (+0.7%) ·
  Northwind +$1,136 (+0.4%) · Cascade +$28,069 (+2.4%) · Harborview
  −$3,775 (−1.9%). Sample data byte-identical; anchors unchanged.

- **Cascade fix (Nov 13, 2026):** battery found one defect — deleting
  a register contract removed its group and invoices from view but
  its forecast lines kept counting in the totals. Argon fix: totals
  count only contracts present in the register, deletion removes the
  contract's lines and invoices entirely, and contract-ID edits
  cascade to lines and invoices. Verified 255/255 checks, including
  the post-delete figures (YTD forecast $2,001,996 · actual
  $2,034,731 · REVIEW 3 / 2 after deleting Harborview).
