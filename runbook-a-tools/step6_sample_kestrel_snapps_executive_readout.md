# Runbook A — Step 6 Sample: Kestrel Industrial Holdings — SNAPPS Executive Readout & Commercial Bridge

- **Account / Opportunity:** Kestrel Industrial Holdings, Inc. (`OPP-2026-4819`)
- **Diagnostic Date:** `2026-11-25` | **Session Mode:** Slot #1 in Validation Mode
- **Step 5 Time-Out Survival Status:** **CLEARED** — Built strictly from verified findings that survived Ely, Graber, and TWED review (non-additive `$1.33M` diff sum stripped; 4 base-MSA flags and 7 unknowns explicitly flagged `UNVERIFIED`; strict No-Rescue boundary enforced).

---

## BEAT 1 — PROBLEM REPRESENTATION (ALIGN ON VERIFIED FACTS)

Kestrel Industrial Holdings is a **$240,000 enterprise 3-year ramp** opportunity — 50, 70, and 80 seats plus `$24,000` implementation — stalled in Stage 5 for **19 calendar days** since Kestrel General Counsel Nadia Benali returned redlines on November 6, 2026 (`c:L001-104; d:T039-050`). The stall sits internally on Deal Desk Ticket `DD-8842`, placed on **HARD HOLD** by Priyesh Patel on November 9, and externally with Kestrel's unengaged economic buyer, **CFO Gregory Cho**, who has not reviewed or approved capital budget ahead of a December 2 Q4 budget committee deadline (`d:T047-049,T062-076,T086-088,T104`). What changed on November 3 and November 6 is that AE Jordan Reyes quoted an unapproved offline **28.0% discretionary subscription discount** with a manual **$6,000 implementation list override** and **Net-60** terms while leaving CRM at `20.0%` and `Net-30` (`a:CRM-15-26; b:E13,G12`), and Kestrel redlined a **penalty-free Month-12 opt-out**, **Net-60 post-acceptance invoicing**, a **20% Year 2–3 seat true-down**, and a **3x (`$720K`) liability cap with uncapped security/confidentiality/IP** (`c:L019-095`). Severity is critical: consolidated gross margin is **70.8%** (`$10,000` below the `75.0%` policy floor) with **verbal VP Sales support only** and **zero Finance margin sign-off** (`b:M14,F19; d:T036,T095,T102; e:PB-4.1,4.3`), while the Month-12 opt-out collapses ASC 606 enforceable value from `$240,000` to `$78,000` (`b:Year1_OptOut_Sensitivity!B4:B5; e:PB-5.3`). Six days remain before December 1, and neither CFO Gregory Cho's trade-off tolerance nor Seller Finance's exception appetite is verified.

---

## BEAT 2 — EXACT STUCK POINT & FAILED CONTROLS (CAUSE X vs CAUSE Y)

### Verified Non-Overlapping Financial Leak & Exposure (Leak Waterfall Only)
| Verified Metric | Exact Kestrel Figure | Primary-Source Proof |
|---|---:|---|
| **Standard Price Book Total List** | `$330,000` | `$300K` sub (`PB-1.1`) + `$30K` impl (`PB-1.3`) |
| **True Commercial Price Concession** | **`-$90,000` (`27.3%`)** | `-$84K` visible `28.0%` sub discount (`b:H12`) + `-$6K` hidden cell `E13` impl override (`b:E13`) |
| **Consolidated 3-Year Gross Margin** | **`70.8%` (`-$10,000` vs Floor)** | `$170K` GP / `$240K` TCV (`$70K` COGS); breaches `75.0%` policy floor (`b:M14,F19; e:PB-4.1`) |
| **Standalone Implementation Margin** | **`-8.3%` (`-$2,000` Loss)** | `$24K` fixed cap vs `$26K` direct ERP COGS (`b:L13:M13; c:L015-016`) |
| **ASC 606 Enforceable TCV (If Signed As Written)** | **`$78,000` (`-$162,000` / `-67.5%`)** | Month-12 penalty-free opt-out w/ zero clawback (`c:L028-035; b:Year1_OptOut!B4:B5; e:PB-5.3`) |
| **Year-1 Net Contribution After Upfront Comm** | **`$17,000` (`21.8%`)** | `$78K` Y1 rev − `$37K` Y1 COGS (`52.6%` Y1 GM) − `$24K` upfront `10%` comm (`b:Year1_OptOut!B6:B11`) |
| **Year-1 Cash Delay (Net-60 Post-Acceptance)** | **`~105+` Days (`$66,000` Deferred)** | `45`-day cutover + subjective acceptance certificate + `Net-60` (`c:L041-060; e:PB-5.1,5.2`) |
| **Separate Contingent Legal Risk (Non-Additive)** | **`$720K` Cap + Uncapped Sec/IP** | `3x` TCV cap (`13.3x` Y1 sub), uncapped sec/conf/IP, `25%` SLA refund exit, `20%` true-down (`-$32.4K`), `0%` 2-term renewal cap (`-$18.6K`), retroactive MFN (`c:L019-095`) |

### Why Kestrel Broke: Proven **Cause X** — and NOT Just **Cause Y**
- **Refuting Cause Y #1 ("Kestrel Legal Is Slow"):** Kestrel GC Nadia Benali returned full redlines in **2.7 calendar days** (`Nov 3 16:40` -> `Nov 6 10:14`, `d:T018,T039`) and champion Derek Halvorsen chased Seller on Nov 16 (`d:T081-088`). Approval-Hop Timestamp Audit proves Buyer Legal held the ball for **`0.0%` (`0.0` hours)** of the 19-day (`454.8`-hour) post-redline stall.
- **Refuting Cause Y #2 ("Internal Bureaucracy" OR "Just One Bad Rep"):** Seller Legal triaged in **1.6 hours** (`d:T056`) and Deal Desk audited 5 valid SOX/margin/ASC 606 violations in **1 business day** (`d:T062-076`). Blaming AE Jordan Reyes alone (`85.4%` / `388.3` hours unworked hold) fails the Step 5 Time-Out because Seller's own QTC tools enabled the breach AND the buyer lacks CFO budget approval.
- **Proving Cause X (Dual Internal Governance/Tooling Breakdown + Unengaged Buyer CFO Gate):**
  1. **Internal Governance Deadlock:** Ticket `DD-8842` sat unworked on `HARD HOLD` for **16 calendar days** (`Nov 9–25`), **ZERO** Margin Exception packet ever reached Finance Controller Elena Rostova (`0.0%` Finance time, `d:T102`), and VP Sales Marcus Vance's casual Slack nods (`Nov 4` & `Nov 18`, never seeing `28%` / `70.8%` GM / opt-out) are **invalid under `PB-4.3`** (`d:T032-038,T095-098`).
  2. **4 Failed Upstream System Controls:** Three-Way Diff proved **15 of 16 lines mismatched (`93.8%`, violates `PB-6.1`)** because Salesforce runs unsynced offline Excel (`a:CRM-25`), stale `20.0%` discount triggered a **false-green** CRM Finance clearance (`"Not Required — Auto-Cleared <=20%"`, `a:CRM-15,22`), Excel cell `E13` lacked protection against a manual `$30K -> $24K` overwrite (`b:E13`), and CRM allowed `Forecast = Commit` during Legal/Deal Desk hard holds (`a:CRM-08,23,24`).
  3. **Unengaged External Economic Buyer Gate:** CRM misidentifies VP Ops Derek Halvorsen as Economic Buyer (`a:CRM-28,29`). Sole signatory `>$50K` is **CFO Gregory Cho** (`c:L100-104`), who has had **ZERO meetings** and **ZERO budget approval** (`d:T047-049,T104`), while Ohio plant consolidation risk (`c:L022-023`) drives Kestrel's exit and true-down demands.

### Explicit Step 5 Scope Limits & `UNVERIFIED` Unknowns
- **Contract Flag Scope:** `41` triggered flags (`20` CRITICAL, `16` HIGH, `5` MODERATE; `6` PASS) across **`47` evaluated Order Form/Amendment clauses**. Because Kestrel's base MSA and ERP SOW were not in Step 1 artifacts, **4 base-MSA flags (`F35` consequential damages, `F36` ERP IP ownership, `F37` cyber insurance, `F38` audit rights)** remain **`UNVERIFIED — FULL MSA REVIEW REQUIRED`**.
- **Explicitly Quarantined Unknowns (`UNVERIFIED`):** `U-1` CFO Gregory Cho's capital availability & trade-off appetite; `U-2` Seller Finance Controller Elena Rostova's margin exception floor; `U-3` VP Sales Marcus Vance's sponsorship after viewing actual `70.8%` GM; `U-4` 45-day SAP/ERP cutover feasibility & true cost vs `$26K` COGS (no SOW); `U-5` competitor presence; `U-6` unlogged AE phone calls Nov 16–25; `U-7` exact Dec 2 budget committee packet requirements.

---

## BEAT 3 — CLEAN BOUNDARY (NO RESCUE): CLIENT-OWNED MESO STRUCTURAL OPTIONS

**Clean Boundary Statement:** *Our diagnostic work ends with verified facts and modeled structural options. We will NOT redline `OF-2026-4819-v3`, contact Kestrel GC Nadia Benali, join a call with CFO Gregory Cho, or lobby Finance Controller Elena Rostova. Your Revenue, Finance, and Legal leaders own the decision and any counter-offer.*

| Client Option | Structural & Commercial Design | Verified Economics & ASC 606 | Required Written Approvals | Strategic Trade-Off Tested |
|---|---|---|---|---|
| **MESO Option A** *(Keep `$240K` Price -> Firm 3-Yr Commit)* | 50/70/80 ramp @ `28%` sub (`$216K`) + `$24K` impl = **`$240K`**. **STRIKE** Month-12 opt-out, 20% true-down, Net-60 acceptance, MFN, 3x/uncapped cap, SLA refund. Restore **Net-30 upfront** & signed ERP SOW. | TCV: **`$240,000`** \| ASC 606: **`$240,000` (100%)** \| 3-Yr GM: **`70.8%`** (`-$10K` floor) \| 3-Yr Net After Comm: **`$146,000`** | Written Tier-4 Finance Controller/CFO Margin Exception (`U-2`) + Written VP Sales + ERP SOW (`U-4`). | Forces CFO Cho to prove whether Kestrel wants a `$240K` 3-yr commitment or only a free 1-yr option. |
| **MESO Option B** *(Keep Exit & Net-60 Invoice -> Policy Floor + `PB-5.3`)* | 50/70/80 ramp @ **`16.0%` disc (`$1,260/seat`)** = `$252K` + **`$30K` std impl** = **`$282K`**. Allow Month-12 exit ONLY w/ 60-day notice + **`PB-5.3` list clawback (`+$12K`)**. **Net-60 from invoice** (no acceptance gate). Standard 1x cap (opt. GC 2x sec sub-cap), no MFN. | TCV: **`$282,000`** \| 3-Yr GM: **`75.2%` (`+$500` PASSES FLOOR)** \| ASC 606 Y1 Base: **`$93,000`** (`+$12K` exit clawback) \| Y1 Net After `$9.3K` Enforc. Comm: **`$46,700`** | Written VP Sales (Tier-2 `16%`) + Finance Controller (Net-60) + GC/CFO/Rev-Rec (`PB-5.3` exit) + ERP SOW. | Accommodates buyer exit & Net-60 AP rules while passing Seller's `75%` GM floor & ASC 606 discipline. |
| **MESO Option C** *(Clean 12-Month Paid Enterprise Pilot)* | **12-month non-cancellable**: 50 seats @ **`$1,500` list (`0%` disc)** = `$75K` + **`$30K` std impl** w/ signed SOW = **`$105K`**. Optional Y2–3 ramp schedule (`70/80` seats) unlocks upon signed 24-mo expansion order. **Net-45/60 invoice-dated**, standard MSA. | 1-Yr TCV: **`$105,000`** \| ASC 606: **`$105,000` (100%)** \| Y1 GM: **`64.8%`** (vs `52.6%` redline) \| Y1 Net After `$10.5K` Comm: **`$57,500` (`3.4x` Redline!)** | Zero discount tier exception (`0%`) + Finance Controller (Net-45/60) + VP Services SOW. | Fits smaller Q4 CFO budget, eliminates ASC 606/clawback distortion, and triples Year-1 net contribution. |
| **Option D** *(Controlled Q4 De-Commit & Re-Qualification)* | Remove `$240K` from Q4 Commit immediately (`a:CRM-08`); fix CRM mismatches (`PB-6.1`); require direct CFO Gregory Cho discovery call, ERP SOW, and full base MSA audit (`F35–F38`) before re-quoting for Q1/Q2 2027. | Toxic Risk Signed: **`$0`** \| Restores Q4 forecast integrity and prevents panic override ahead of Dec 1. | CRO / VP RevOps forecast adjustment + Deal Desk CRM reset. | Avoids signing an unenforceable, negative-unit-economics contract under artificial Q4 pressure. |

---

## BEAT 4 — THE COMMERCIAL BRIDGE (SLOT #1 -> 5-DEAL FORENSIC DIAGNOSTIC)

> **"We proved exactly why this deal broke. What neither of us knows yet is whether this is a one-off outlier or how 20-30% of your deal flow quietly leaks across handoffs. That's what the 5-deal Forensic Diagnostic proves in 5 business days — with this deal as Slot #1."**

### Proposed 5-Business-Day Sampling Plan (Slot #1 Already Complete)
1. **Slot #1 — Kestrel Industrial Holdings (`$240K`, COMPLETED):** Baseline proof of unsynced CRM/Excel (`15/16` mismatches), false-green Finance auto-clearance, `85.4%` unworked hold, `70.8%` GM, and `$162K` ASC 606 opt-out exposure.
2. **Slot #2 (Day 1):** One current Q4 Commit enterprise opportunity (`>$150K`) — tests whether false-green approvals and unengaged Economic Buyers sit inside Q4 Commit.
3. **Slot #3 (Day 2):** One currently stalled post-redline opportunity (`>14` days) — tests whether stalls belong to buyer legal or silent internal handoff holds.
4. **Slot #4 (Day 3):** One recently closed-won multi-year ramp — tests whether signed deals quietly shipped sub-75% GM, overwritten services prices, or hidden ASC 606 clauses.
5. **Slot #5 (Day 4):** One recent closed-lost enterprise deal — tests whether preventable approval lag or misqualified champions caused avoidable losses.
6. **Day 5 Deliverable:** Executive portfolio quantification of true handoff leakage (`$`), systemic control failure map, and prioritized QTC remediation plan.

*Commercial Pricing Note: Neon's suggestion of a `$100` validation fee credited toward the 5-deal Forensic Diagnostic is strictly **unruled and optional — not part of the ruled price**.*
