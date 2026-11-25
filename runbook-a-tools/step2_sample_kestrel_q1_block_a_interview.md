# Runbook A — Step 2 Sample: Kestrel Industrial Holdings — Q1 Block A Structured Interview

## Session Header
- **Account Name:** Kestrel Industrial Holdings, Inc.
- **CRM Opportunity ID:** `OPP-2026-4819`
- **Diagnostic Date:** `2026-11-25` (Slot #1 — Validation Mode)
- **Interviewees Present:** Jordan Reyes (Enterprise AE), Client VP Revenue Operations (Diagnostic Lead)
- **Clinician:** Runbook A Lead Clinician
- **Evidence Standard:** Every interview answer is tested against Step 1 raw artifacts (`a` CRM, `b` Quote v4 Excel, `c` Redlined Contract, `d` Approval Thread, `e` Price Book Policy). Anything absent from primary sources is explicitly marked **`UNVERIFIED`**.

---

## BLOCK A1 — WHO (Real Decision-Maker / Economic Buyer vs Champion vs Internal Holders)

### Clinician Structured Q&A Log (Summary of Interview vs Primary-Source Proof)
1. **Q (Economic Buyer):** *"Who holds unilateral signature and budget authority for this $240,000 deal?"*
   - **AE Claim:** *"Derek Halvorsen, VP of Operations — we met with him in September, he's tagged as Economic Buyer in Salesforce, and he's ready to sign."*
   - **Primary-Source Check:** **CONTRADICTED.** Contract Section 12 (`c:L098-L104`) lists **Gregory Cho, Chief Financial Officer** on the signatory line, and GC Nadia Benali wrote in `[COMMENT R-10]` (`c:L103-L104`): *"Only CFO Gregory Cho has signature authority for contracts exceeding $50,000. Derek Halvorsen (VP Ops) cannot execute this Order Form."* Nadia's Nov 6 email (`d:T047-T048`) confirms Gregory Cho has **NOT** reviewed or approved budget, and audit pull (`d:T104`) confirms **ZERO** meetings or emails with Gregory Cho.
2. **Q (Internal Approvals):** *"Who inside Seller Corp owns the next required approval?"*
   - **AE Claim:** *"VP Sales Marcus Vance already approved $240K verbally on Slack; Legal and Deal Desk are just dragging their feet."*
   - **Primary-Source Check:** **CONTRADICTED.** Policy `PB-3.0`, `PB-4.1`, and `PB-4.3` (`e:PB-3.0, PB-4.1, PB-4.3`) require **written Finance Controller (Elena Rostova) or CFO Margin Sign-Off** plus written VP Sales approval on actual final P&L. Marcus Vance explicitly wrote on Nov 18 (`d:T095`): *"if Finance clears it, just get Desk what they need."* Zero exception packet has ever been submitted to Elena Rostova (`d:T102`).

### Block A1 Verified Stakeholder Table
| Role | Interviewee / CRM Claim | Verified Primary-Source Fact | Step 1 Citation | Status |
|---|---|---|---|---|
| **Real Economic Buyer / Signatory** | Derek Halvorsen (VP Ops); marked "Met = TRUE" in CRM (`a:CRM-28,29`) | **Gregory Cho, CFO** — sole authority >$50K; chairs Dec 2 Q4 budget committee; ZERO meetings, ZERO emails, ZERO budget approval | `c:L100-104`; `d:T008,T047-049,T104` | **CONTRADICTED** (EB Unengaged) |
| **Buyer Champion** | Derek Halvorsen (VP Ops) | Active operational champion on emails (Oct 28 & Nov 16), but lacks legal signature authority >$50K | `a:CRM-27`; `c:L103-104`; `d:T002,T082` | **VERIFIED** |
| **Buyer Legal Counsel** | "Slow legal team" (`a:CRM-32,33`) | **Nadia Benali, GC** — returned full redlines 3 days after Quote v4 (Nov 6) and stated she is waiting on Seller's written confirmation | `a:CRM-30`; `c:L001-104`; `d:T039-050` | **CONTRADICTED** |
| **Seller Executive Sponsor** | "VP Marcus verbally approved $240K" (`a:CRM-21`) | **Marcus Vance, VP Sales** — gave two casual Slack DMs (Nov 4 & Nov 18) without viewing 28% disc / 70.8% GM / opt-out; deferred to Finance clearance; invalid under `PB-4.3` | `d:T027-038,T089-098`; `e:PB-4.3` | **CONTRADICTED** (Invalid Approval) |
| **Seller Finance / Margin Approver** | "Not Required — Auto-Cleared <=20%" (`a:CRM-22`) | **Elena Rostova, Finance Controller** — mandatory approver for Tier-4 (>25%), <75% GM, and Net-60; has received **ZERO** exception submissions | `d:T074-075,T102`; `e:PB-3.0,PB-4.2,PB-5.1` | **CONTRADICTED** (Never Routed) |
| **Seller Deal Desk & Legal Holders** | "Being bureaucratic / slow" (`d:T091`) | **Tessa Morales (Legal)** triaged in 1.6h (`HOLD` Nov 6); **Priyesh Patel (Deal Desk)** audited in 1 bus. day (`HARD HOLD` Nov 9, bumped Nov 12); waiting 16 days on AE | `a:CRM-23,24`; `d:T056-080,T101` | **CONTRADICTED** |

---

## BLOCK A2 — WHEN (Stall Onset, Last Verified Events & Hard Deadlines)

### Block A2 Verified Timeline Table (Anchored to Diagnostic Date `2026-11-25`)
| Timeline Anchor | Interviewee / CRM Claim | Verified Date / Timestamp | Elapsed Days to Nov 25 | Step 1 Citation | Status |
|---|---|---|---|---|---|
| **Opportunity Created** | Q3 inbound enterprise deal | `2026-08-14 09:20 ET` | `103` days | `a:CRM-01` | **VERIFIED** |
| **Precursor Event (Unapproved Quote v4)** | Not mentioned in CRM | `2026-11-03 16:40 ET` | `22` days | `b:E4`; `d:T018-026` | **VERIFIED** |
| **Stall Onset (Redline Returned)** | "Waiting on Kestrel legal" | `2026-11-06 10:14 ET` | **`19` days** | `a:CRM-07`; `d:T039-050` | **VERIFIED** |
| **Legal Hold Placed** | Not surfaced on forecast calls | `2026-11-06 16:18 ET` | `19` days | `a:CRM-24`; `d:T056-061` | **VERIFIED** |
| **Deal Desk HARD HOLD Placed** | Not worked by AE | `2026-11-09 09:05 ET` | **`16` days** | `a:CRM-23`; `d:T062-076` | **VERIFIED** |
| **Last Verified External Event (Buyer)** | "Buyer legal is quiet" | `2026-11-16 11:30 ET` — Derek Halvorsen emailed AE chasing seller's reply | **`9` days** | `a:CRM-31`; `d:T081-088` | **VERIFIED** |
| **Last Verified Internal Event** | "VP re-confirmed Nov 18" | `2026-11-18 08:52 ET` — Marcus Vance told AE *"if Finance clears it, just get Desk what they need"* | `7` days | `a:CRM-21`; `d:T089-098` | **VERIFIED** |
| **Hard Buyer External Deadline** | CRM Target Close = Nov 30 (pushed 2x) | **Dec 2, 2026** — CFO Gregory Cho's Q4 budget committee (alignment needed before Dec 1 or slips to Q2 2027) | `-6` days remaining to Dec 1 | `a:CRM-09,10`; `d:T086-088` | **VERIFIED** |
| **Any Post-Nov 16 Phone Contact** | AE asserts "kept Derek warm by phone" | No logged call, email, or CRM note exists after Nov 16 | N/A | `a:CRM-31`; `d:T081-103` | **`UNVERIFIED`** |

---

## BLOCK A3 — WHAT DEAL SHAPE (Price, Term, Structure, Risk Clauses & Approvals)

### Block A3 Cross-Artifact Deal Shape Table
| Deal Shape Dimension | CRM Record (`Artifact a`) | Quote v4 Excel (`Artifact b`) | Redlined Contract (`Artifact c`) | Governing Policy (`Artifact e`) | Forensic Verification Status |
|---|---|---|---|---|---|
| **Headline TCV & Ramp** | `$240,000` TCV; ARR wrongly entered as `$80,000`; 50/70/80 ramp (`CRM-11,12,13`) | **`$240,000` TCV**: Y1 `$54K` (50) + Y2 `$75.6K` (70) + Y3 `$86.4K` (80) = `$216K` sub + `$24K` impl (`I9:I14`) | `$240,000` face value (`L005-014`); adds **20% Y2–3 seat true-down** (`L019-021`) | `PB-2.2/2.3`: Ramp allowed only if firm commitment; true-downs prohibited | **VERIFIED — MISMATCH & BREACH** |
| **Subscription Discount %** | **`20.0%`** (stale v2 entry; `CRM-15,26`) | **`28.0%`** discretionary discount (`-$84,000` off `$300,000` list; `G12,H12`) | `$1,080/seat/yr` net (28% off `$1,500`, discount % omitted; `L008`) | `PB-3.0`: `>25%` = **Tier 4** (VP Sales + Finance Controller / CFO written sign-off) | **VERIFIED — MISMATCH & TIER-4 BREACH** |
| **Implementation Fee & List Override** | `$24,000` (`CRM-16`) | `$24,000` net, `$26,000` COGS (`-8.3%` GM); **Cell `E13` manually overwritten from `$30K` list to `$24K`** (`-$6K` hidden) | `$24,000` fixed cap incl. custom SAP/ERP; 50% (`$12K`) held until acceptance (`L014-016,L044-047`) | `PB-1.3`: `$30,000` list, `0%` max AE discount; cell overwrite strictly prohibited; `PB-5.2`: 100% upfront | **VERIFIED — HIDDEN OVERRIDE & BREACH** |
| **Total True Concession** | Not calculated | `$90,000` total concession off `$330,000` true Price Book list (**27.3% true blended**; `True_List_Leak_Bridge!B8:B10`) | Matches `$240K` net (`$90K` off standard list) | `PB-1.0 / PB-3.0` | **VERIFIED** |
| **Consolidated Gross Margin %** | `(Blank)` (`CRM-20`) | **`70.8%` GM** (`$170,000` GP / `$240,000`; `$70,000` COGS) — **`$10,000` below 75.0% floor** (`M14,F19`) | Not stated in contract | `PB-4.1/4.2`: Minimum `75.0%` GM floor; mandatory written Finance Margin Sign-Off | **VERIFIED — MARGIN FLOOR BREACH** |
| **Term & Custom Opt-Out** | `36` months; `Custom_Opt_Out__c = FALSE` (`CRM-14,18`) | Modeled as 36-month committed (`Opt-Out = NO`); Sensitivity tab shows **$78K Y1 enforceable / $162K at risk / 52.6% Y1 GM / $17K Y1 net after $24K commission** | **Sec 2.3**: Unilateral Month-12 opt-out, 30 days' notice, **zero fee, zero discount clawback** (`L028-035`) | `PB-5.3`: Strictly prohibited on multi-year discount >10% w/o CFO+GC+Rev-Rec exception + clawback or >=50% ETF | **VERIFIED — CRITICAL ASC 606 BREACH** |
| **Payment Terms & Billing Trigger** | **`Net-30`** (`CRM-17`); Acceptance flag `FALSE` (`CRM-19`) | **`Net-60`** (invoice trigger unmodeled; `H4`) | **Sec 4.1**: **`Net-60` starting AFTER written Production Go-Live Acceptance Certificate** (~105-day effective DSO; `L055-058`) | `PB-5.1`: Net-30 upfront standard; Net-60 requires Finance Controller; acceptance billing requires Rev-Rec + CFO | **VERIFIED — THREE-WAY MISMATCH & BREACH** |
| **Additional Legal Risk Clauses** | None logged | Not modeled | 0% renewal cap / no auto-renew (`L067-069`); 25% annual SLA credit + refund exit (`L076-079`); **3x ($720K) liability cap + uncapped security/IP** (`L085-087`); MFN (`L092-094`) | `PB-5.4`: Standard 7% uplift, 1x 12-mo cap, no SLA refund exit, no MFN without GC + CFO | **VERIFIED — 4 LEGAL BREACHES** |
| **VP Sales Approval** | `"Verbal - Marcus Vance"` (`CRM-21`) | `"NONE - Verbal VP Only"` (`K5`) | Unsigned (`L098-102`) | `PB-4.3`: **Verbal / casual Slack approvals without final P&L are INVALID** | **VERIFIED — INVALID** |
| **Finance Margin Sign-Off** | `"Not Required (Auto-Cleared <=20%)"` (`CRM-22`) | `"NONE - Verbal VP Only"` (`K5`, `D21:M21 = FAIL`) | None (`d:T102` confirms ZERO packets submitted) | `PB-3.0 / PB-4.2`: Mandatory written Finance Controller / CFO sign-off | **VERIFIED — ABSENT** |

---

## EXPLICITLY FLAGGED `UNVERIFIED` GAPS (CARRY FORWARD TO STEP 3 & STEP 4)

| Gap # | Explicitly Flagged `UNVERIFIED` Unknown | Why It Cannot Be Treated as Verified Fact | Primary Source Needed to Verify |
|---|---|---|---|
| **U-1** | **`UNVERIFIED` — CFO Gregory Cho's real decision criteria, budget availability, and trade-off tolerance** | Zero direct meetings or written correspondence exist with Gregory Cho (`d:T104`). Champion Derek Halvorsen's email (`d:T008`) is secondhand. | Direct executive discovery call or written confirmation from CFO Gregory Cho. |
| **U-2** | **`UNVERIFIED` — Seller Finance Controller Elena Rostova's / CFO's exception floor** | AE never submitted the Tier-4 Margin Exception packet (`d:T102`); Finance has not ruled on 70.8% GM, Net-60 (invoice-dated), or any conditional opt-out structure. | Formal Margin Exception submission and written ruling from Elena Rostova / CFO. |
| **U-3** | **`UNVERIFIED` — VP Sales Marcus Vance's willingness to sponsor true v4 terms** | Marcus Vance was never shown the 28% discount, hidden $6K impl override, 70.8% GM, or Month-12 opt-out (`d:T032-033,T096`). | Written VP Sales review after viewing full Quote v4 P&L and redline summary. |
| **U-4** | **`UNVERIFIED` — SAP/ERP 45-day implementation feasibility and true delivery cost** | Section 3.1 (`c:L041`) mandates a 45-day cutover with zero overage (`c:L015-016`), and Quote v4 estimates `$26,000` COGS (`b:J13`), but no signed SOW or Services scoping review exists in Step 1 artifacts. | Written scoping sign-off and SOW from VP Professional Services. |
| **U-5** | **`UNVERIFIED` — Whether any competing vendor or internal build threatens Kestrel** | No competitor mention or competitive comparison exists in any of the 5 raw artifacts (`a–e`). | Direct discovery confirmation from Derek Halvorsen or Gregory Cho. |
| **U-6** | **`UNVERIFIED` — Whether AE made any unlogged verbal calls/promises to Derek Halvorsen between Nov 16 and Nov 25** | Last verified external email is Derek's Nov 16 chase (`a:CRM-31; d:T081-088`); zero call recordings or email replies exist afterward. | Phone/call log export or direct buyer check-in. |
| **U-7** | **`UNVERIFIED` — Exact submission cutoff hour and required packet for Kestrel's Dec 2 Q4 budget committee** | Derek wrote `"before Dec 1"` (`d:T087`), but Kestrel Finance's formal docket requirements are not in the raw artifacts. | Written procurement/finance docket instructions from Kestrel GC or CFO office. |
