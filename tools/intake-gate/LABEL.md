# LABEL — S6-P05.1 — Intake Gate & Submission Scorecard (Tool 5)

- **Page ID:** S6-P05.1
- **Tool:** Tool 5 (TOOL 5.1 — the Argon rebuild, adopted Nov 13, 2026)
- **URL:** /tools/intake-gate/
- **Files in this folder:** `S6-P05a-intake-gate.html` (canonical),
  `index.html` (byte copy), this LABEL. The workbook-embed
  `S6-P05a-intake-gate-data.js` is RETIRED — removed from the site
  Nov 13, 2026; the embed build is preserved as an iteration (local
  snapshot, GitHub branch `tool-5-iterations`, Drive archive folder
  "Tool 5 — Workbook Embed (retired)").
- **What it does:** scores each submitted deal against five baseline
  checks (account verified, prior contract linked, eligibility
  confirmed, SKU mix valid, docs complete). Readiness = Y-count / 5.
  A deal Approved below 100% readiness or above a 20% discount fires
  "AUDIT ALERT: Approved Without Baseline" and routes STOP – REVOKE
  & AUDIT; incomplete deals HOLD – RETURN TO SALES; clean deals at
  ≤15% discount FAST-TRACK; other clean deals ROUTE TO DEAL DESK –
  FINANCE. Answers first: KPI strip, Needs a Decision exception
  list, the editable gate log, and a copyable Gate Report (plus a
  mailto "email the report to myself" button).
- **Anchors (sample untouched):** Total 5 · Clean First-Pass 2 ·
  First-Pass Yield 40% · Held at Gate 2 · Unauthorized Caught 1.
  Per deal: 101 → 100% FAST-TRACK · 102 → 60% HOLD · 103 → 40%
  AUDIT ALERT → STOP · 104 → 100% FAST-TRACK · 105 → 80% HOLD.
- **Built:** Argon (page code + all reader-facing words) from the
  workbook `Deal_Desk_Intake_Gate_&_Submission_Scorecard_SAMPLE.xlsx`
  under the standing prompt template (goal → look → build → SEO →
  integrity → QA standard). Muse prompt, verification, publishing.
- **Verification (Nov 13, 2026):** sample data exact; all anchors in
  the rendered page; interaction battery — flipping DEAL-102's
  checks to all-Y moves it to ROUTE TO DEAL DESK – FINANCE and the
  yield to 60%; approving DEAL-105 at 80% readiness fires the audit
  alert (Unauthorized 2); delete-all leaves Total 0 / Yield 0% with
  no NaN; add-deal works; reset restores the anchors; zero page
  errors. Internal links converted to the site's relative scheme at
  promotion, including Argon's Deal Check link corrected to
  ../deal-check/.
