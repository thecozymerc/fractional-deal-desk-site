# LABEL — tools/deal-check

**Address:** /tools/deal-check/
**What this folder holds:** S6-P03.1 The Deal Check — the 6-step deal-health checklist (email gate REMOVED Nov 18, 2026 on Lucky’s order — plain download button).

**STAGE 3 — BRIDGE + METER (Nov 19, 2026, CODE-MAP v79):** outbound bridge block (paste field + 'Paste Full Contract → Run 51-Point Autopsy' button, text passed via localStorage), inbound carry-back summary (Deal Health Score, verdict, Window 1 total leak, 3 MESO alternatives with flags — the Analyzer ledger's own figures), shared usage meter + 3-door modal (same `qtc_contract_autopsy_runs_v1` key). Checklist + ungated PDF unchanged; no front-door gate.

**STAGE 3 CORRECTIVE 3 — BRIDGE SENDS THE FULL INPUT SET (Nov 19, 2026, CODE-MAP v80):** `sendContractAcrossBridge()` now builds the payload via `buildInboundBridgePayload()` carrying {acv, discountPct, netDays, billingFreq, upliftCapPct, termYears}; the Atlas sample sends `ATLAS_SAMPLE_INPUTS` (240000/22/60/quarterly/2/2). No visible copy changed on this page. Invited path verified end to end: Analyzer auto-run renders leak $66,002 / Health 38 (Problems List #21 fixed).

Rule (Code Labeling System): this label is updated in the same change as anything in this folder. Every change is recorded in the site CHANGELOG.md, and the CODE-MAP.md entry is updated in the same move.

**Status:** LIVE — `S6-P03a-deal-check.html` + `deal-check-checklist.pdf`. Nov 18, 2026: the email gate was REMOVED on Lucky's order (archived in the build log, deal-check-email-gate-archive-2026-11-18; the Google Form 'The Deal Check — Checklist Download', form 1o_YCJ2zkQyOPUL4Fp-AMh6bWALytI0BDHXnLTX6Bd6c, still exists but the page no longer posts to it) — the checklist is now a plain download button. The site-wide feedback form ('Site Feedback — Something Broken?', footer link 'Something broken? Tell me' on every page) also landed Nov 18, 2026. CODE-MAP v76.
