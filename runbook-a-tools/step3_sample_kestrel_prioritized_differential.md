# Runbook A — Step 3 Sample: Kestrel Industrial Holdings — Surgical Sieve & Prioritized Differential

- **Account / Opportunity:** Kestrel Industrial Holdings, Inc. (`OPP-2026-4819`)
- **Diagnostic Date:** `2026-11-25` (Slot #1 — Validation Mode)
- **Step 2 Problem Representation Anchor:** `$240,000` enterprise 3-year ramp (50/70/80 seats + `$24K` ERP impl) stalled `19` calendar days post-redline (`2026-11-06` to `2026-11-25`); parked internally on Deal Desk Ticket `DD-8842` (`HARD HOLD` Nov 9, `16` days unworked) and externally before unengaged Economic Buyer CFO Gregory Cho's Dec 2 Q4 budget committee; carrying `28.0%` discretionary discount, hidden `$6K` impl cell override, `70.8%` GM (`$10K` below `75.0%` floor), verbal VP support only, zero Finance margin sign-off, Month-12 penalty-free opt-out, and Net-60 post-acceptance terms.

---

## 1. Complete 5-Bucket QTC Surgical Sieve (Q1 Block B — Zero Buckets Skipped)

| Bucket | Q1 Block B Domain | Scanned | Sev × Evid | Risk Tier | Verified Findings (Step 1 Artifacts & Step 2 PR) | Citations & Explicit `UNVERIFIED` Gaps |
|---|---|---:|---:|---|---|---|
| **B1** | **Commercial / Pricing** | YES | `5 × 5 = 25` | **CRITICAL** | `28.0%` discretionary subscription discount (`-$84,000` off `$300,000` list) breaches Tier-4 (`>25%`). AE manually overwrote impl list cell `E13` from `$30,000` to `$24,000` (`-$6,000` hidden concession; `-$2,000` / `-8.3%` standalone impl GM on `$26K` COGS). True total concession = **`$90,000` (`27.3%` off `$330K` list)**. Consolidated 3-year GM = **`70.8%`**, **`$10,000` below the `75.0%` policy floor**; Year-1 GM = **`52.6%`**. | `b:E13,G12,M14,D18:M21`; `b:True_List_Leak_Bridge!B5:B12`; `e:PB-1.3,3.0,4.1`. **`UNVERIFIED`:** Finance exception floor (`U-2`); actual SAP/ERP delivery cost vs `$26K` COGS (`U-4`). |
| **B2** | **Governance / Authority** | YES | `5 × 5 = 25` | **CRITICAL** | Zero written Finance Margin Sign-Off from Controller Elena Rostova (`ZERO` exception packets submitted). VP Sales Marcus Vance provided only casual verbal Slack nods (Nov 4 & Nov 18) without viewing true `28%` discount, `70.8%` GM, or opt-out — **explicitly INVALID under `PB-4.3`**. Deal Desk `HARD HOLD` (Nov 9, `DD-8842`) sat unworked by AE for `16` days. Externally, CRM mislabels VP Ops Derek Halvorsen as Economic Buyer; sole signatory `>$50K` is **CFO Gregory Cho** (`ZERO` meetings, `ZERO` budget approval). | `a:CRM-21-24,28-29`; `c:L098-104`; `d:T027-104`; `e:PB-3.0,4.2,4.3`. **`UNVERIFIED`:** CFO Cho decision criteria (`U-1`); VP Marcus sponsorship if shown real P&L (`U-3`). |
| **B3** | **Config / Tools** | YES | `4 × 5 = 20` | **HIGH** | Salesforce runs in `Manual / Offline Excel (Unsynced)` mode; CRM quote attachment is stale v2 (`$264K`, `20%`). Stale CRM `Discount = 20.0%` triggered a **false-green workflow** (`"Not Required — Auto-Cleared <=20%"`), hiding a Tier-4 breach from Finance. CRM leaves `GM%` blank, `Net-30` stale, `Opt-Out = FALSE`, `ARR = $80K` miscalculated, and permits `Forecast = Commit` during Deal Desk/Legal holds. Excel cell `E13` lacked formula/sheet protection. | `a:CRM-08,12,15-26`; `b:E13`; `e:PB-6.1`. **`UNVERIFIED`:** Whether identical CRM/Excel gaps affect 20–30% of broader enterprise pipeline (addressed in Step 6 Bridge). |
| **B4** | **Paper / Redline** | YES | `5 × 5 = 25` | **CRITICAL** | Kestrel GC Nadia Benali turned redlines promptly in **3 days** (Nov 3 -> Nov 6), falsifying AE's "slow legal" claim. `OF-2026-4819-v3` inserts **7 policy-breaching risk shifts**: (1) Sec `2.3` Month-12 unilateral penalty-free opt-out w/ zero discount clawback; (2) Sec `4.1` & `3.2` Net-60 post-Go-Live Acceptance; (3) Sec `1.3` `20%` Y2–3 seat true-down; (4) Sec `9.1` `3x` (`$720K`) liability cap + **UNCAPPED security/confidentiality/IP**; (5) Sec `7.2` `25%` annual SLA credit + refund exit; (6) Sec `5.4` `0%` renewal cap / no auto-renew; (7) Sec `11.3` retroactive MFN. | `c:L015-095`; `d:T039-061`; `e:PB-2.3,5.1-5.4`. **`UNVERIFIED`:** Which clauses are true CFO red lines vs procurement opening asks (`U-1`). |
| **B5** | **Downstream Billability / Rev-Rec** | YES | `5 × 5 = 25` | **CRITICAL** | **ASC 606 collapse:** Month-12 penalty-free opt-out cuts enforceable TCV **67.5%** from `$240,000` to **`$78,000`** (`$162,000` unbookable/at risk). Subjective acceptance billing (Sec `3.2`/`4.1`) defers revenue recognition start and pushes Year-1 cash collection to **`~105+` days**. Upfront `10%` commission on `$240K` (`$24K`) vs `$41K` Year-1 GP leaves just **`$17,000` (`21.8%`)** net contribution plus `PB-6.2` clawback risk. Seat true-down, SLA refund, and MFN trigger ASC 606 variable-consideration reversals. | `b:Year1_OptOut_Sensitivity!B3:B12`; `c:L019-094`; `d:T071-072`; `e:PB-5.1-6.2`. **`UNVERIFIED`:** Whether 45-day SAP/ERP cutover slips, pushing cash past 120 days (`U-4`). |

- **Composite Risk Index:** **`120 / 125`** (`4` CRITICAL buckets, `1` HIGH enabling bucket, `5 / 5` scanned — zero premature closure).

---

## 2. Prioritized Differential Diagnosis (4 Mandatory Clinical Slots)

### D-1 — LEADING HYPOTHESIS (Primary Root Cause of the 19-Day Stall)
- **Title:** **Dual Internal Governance Deadlock & Unengaged Economic Buyer Gate**
- **Priority Score:** **`25 / 25`** (`Likelihood = 5`, `Impact = 5`) | **Buckets:** `B2, B1, B4, B3`
- **Clinical Mechanism:**
  1. The 19-day post-redline stall is **NOT** caused by slow Kestrel legal. Kestrel GC Nadia Benali turned redlines in 3 days (`d:T018,T039`) and champion Derek Halvorsen chased Seller on Nov 16 (`d:T081-088`).
  2. Seller Legal (`HOLD` Nov 6, `1.6h` triage) and Deal Desk (`HARD HOLD` Nov 9, `DD-8842`) halted work properly after discovering 5 simultaneous violations across CRM (`20%` / `Net-30` / no opt-out), offline Quote v4 (`28%` Tier-4 / `$6K` impl override / `70.8%` GM / `Net-60`), and Redline v3 (Month-12 opt-out / Net-60 acceptance) (`d:T056-076`).
  3. AE Jordan Reyes left `DD-8842` unworked for **16 calendar days** — ignoring Deal Desk's Nov 9 hold and Nov 12 bump, submitting **ZERO** Finance Margin Exception to Elena Rostova (`d:T102`), relying on invalid casual VP Slack DMs (`e:PB-4.3`), and logging false `"Waiting on Kestrel legal"` CRM Commit notes (`a:CRM-08,32`).
  4. Simultaneously, real Economic Buyer **CFO Gregory Cho** (sole signatory `>$50K`, zero meetings) has not approved capital budget and blocks Dec 2 Q4 budget docket entry pending Seller's written confirmation of opt-out and Net-60 (`c:L036-038,L103-104; d:T047-050,T104`).
- **Step 4 Forensic Verification Test:** Execute **Approval-Hop Timestamp Audit** (Nov 3–25), **Three-Way Diff** (CRM vs Quote v4 vs Redline), and **Disconfirming-Evidence Hunt** testing AE's `"slow buyer legal"` and `"VP approved"` framing.

---

### D-2 — CAN'T-MISS / ROWS THREAT (*Rule Out Worst-Case Scenario*)
- **Title:** **Signing an Unenforceable Rev-Rec, Margin & Uncapped-Liability Landmine Under Q4 Panic**
- **Priority Score:** **`15 / 25`** (`Likelihood = 3`, `Impact = 5`) | **Buckets:** `B5, B4, B1`
- **Why It Is Can't-Miss (ROWS):** With 6 days left before Kestrel's Dec 1 docket cutoff and `$240K` sitting in Q4 Commit (`a:CRM-08; d:T087`), the catastrophic failure mode is **rushing an executive override to "save Q4" and signing `OF-2026-4819-v3` as redlined**. Post-signature consequences if closed as written:
  1. **ASC 606 Revenue Collapse:** Month-12 penalty-free opt-out (`c:L028-035`) slashes bookable/enforceable value **67.5% from `$240,000` to `$78,000`** (`$162,000` unbookable; `b:Year1_OptOut_Sensitivity!B3:B5; e:PB-5.3`).
  2. **Year-1 Cash & Margin Hemorrhage:** Year-1 GM is `52.6%`, `$24,000` upfront commission leaves just **`$17,000` (`21.8%`)** net contribution, implementation loses at least `-$2,000` (`-8.3%` GM) with zero overage cap on an unscoped 45-day SAP/ERP migration (`c:L015-016,L041`), and Net-60 post-acceptance pushes cash **`~105+` days**.
  3. **Balance-Sheet & Pricing Contagion:** `3x` TCV (`$720,000`) liability cap + **UNCAPPED security/confidentiality/IP indemnity** (`c:L085-087`), `25%` annual SLA refund exit (`c:L076-079`), `20%` Y2–3 seat true-down (`c:L019-021`), `0%` multi-year renewal cap (`c:L067-069`), and retroactive **MFN price contagion** across all `<=100`-seat industrial customers (`c:L092-094`).
- **Step 4 Forensic Verification Test:** Run **3-Window Deal Engine** (Leak Waterfall, Behavioral Verdict, and full **51-Contract-Flag Audit**) across Quote v4 and Redline v3 to quantify every post-signature dollar and contract exposure before any leadership decision.

---

### D-3 — ALTERNATIVE EXPLANATION #1 (Competing Hypothesis)
- **Title:** **Unqualified / Non-Viable Buyer Budget ("Phantom Q4 Deal") Masking as Legal Friction**
- **Priority Score:** **`16 / 25`** (`Likelihood = 4`, `Impact = 4`) | **Buckets:** `B2 (External Buyer Authority / Budget)`
- **Clinical Rationale:** Even if Seller resolved Ticket `DD-8842` and approved exceptions tomorrow morning, Kestrel could still fail to sign in Q4 because **CFO Gregory Cho has never reviewed or approved Q4 capital budget** (`d:T047-048`), has never engaged Seller (`d:T104`), and Kestrel's Ohio plant consolidation (`c:L022-023`) creates real Year 2–3 headcount uncertainty. Buyer's aggressive demands (Month-12 penalty-free opt-out, 20% true-down, acceptance-gated Net-60) may indicate an unfunded operational wish list championed by VP Ops Derek Halvorsen rather than a genuinely funded Q4 purchase.
- **Explicit `UNVERIFIED` Gaps:** CFO Gregory Cho's real ROI threshold, capital availability, and whether a competitor is active (`U-1`, `U-5`).
- **Step 4 Forensic Verification Test:** Execute **Disconfirming-Evidence Hunt** specifically auditing Derek's Oct 28/Nov 16 emails (`d:T005-009,T085-088`) and Nadia's Nov 6 comments (`R-02, R-03, R-10`) to isolate buyer budget non-qualification from Seller internal silence.

---

### D-4 — ALTERNATIVE EXPLANATION #2 (Competing Hypothesis)
- **Title:** **Systemic QTC Tooling & Upstream Control Architecture Failure Across Enterprise Deal Flow**
- **Priority Score:** **`16 / 25`** (`Likelihood = 4`, `Impact = 4`) | **Buckets:** `B3 (Config/Tools), B1 (Commercial/Pricing)`
- **Clinical Rationale:** Rather than an isolated AE misconduct event, Kestrel's late-stage crash may be the predictable output of Seller's disconnected QTC architecture: no CPQ-to-CRM lock (`a:CRM-25`), unprotected Excel list cells (`b:E13`), false-green CRM Finance clearance triggered by unvalidated rep-typed `20%` discount (`a:CRM-15,22`), optional blank `GM%` field (`a:CRM-20`), and zero CRM rule blocking `Commit` forecast status during Deal Desk/Legal holds (`a:CRM-08,23,24`). Under this hypothesis, Kestrel is merely the visible symptom of a systemic architecture defect leaking margin and cycle time across `20–30%` of Seller's enterprise pipeline.
- **Explicit `UNVERIFIED` Gap:** A single-deal work-up cannot prove whether this tooling failure is isolated to one AE or systemic across Seller's enterprise deal flow (explicitly addressed in Step 6's bridge to the 5-Deal Forensic Diagnostic).
- **Step 4 Forensic Verification Test:** Execute line-by-line **Three-Way Diff** (`Artifact a` vs `Artifact b` vs `Artifact c` vs `Artifact e`) to catalog every upstream system control that failed to prevent an unapproved Tier-4 quote from reaching a prospect.
