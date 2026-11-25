# Runbook A — Step 3: Surgical Sieve & Prioritized Differential Facilitation Guide (30 Min)

## Clinical Purpose
Prevent **premature closure** and **anchoring bias** (accepting the AE's first explanation) by forcing a disciplined scan across **all five Quote-to-Cash (QTC) buckets from Q1 Block B** before ranking the **Leading Hypothesis**, the **Can't-Miss / ROWS Threat**, and **2 Alternative Explanations**.

---

## 30-Minute Facilitation Choreography
- **Minutes 0–2:** Re-read the verified 60–90 second **Step 2 Problem Representation** verbatim so every hypothesis stays anchored to primary-source facts.
- **Minutes 2–17 (3 min per bucket):** Scan **all 5 QTC buckets** in strict order using the Q1 Block B probe table below. Score Severity (`1–5`) and Evidence Strength (`1–5`) for each bucket. Do **not** skip any bucket even if Bucket 1 or Bucket 2 looks obvious.
- **Minutes 17–25:** Draft the 4-slot **Prioritized Differential**:
  1. **Leading Hypothesis** (most probable primary mechanism explaining the stall).
  2. **Can't-Miss / ROWS Threat** (*Rule Out Worst-Case Scenario* — what blows up post-signature or breaks revenue/cash/risk if this deal closes as written).
  3. **Alternative Explanation #1** (genuine competing cause — not a throwaway strawman).
  4. **Alternative Explanation #2** (second distinct competing cause — often structural/systemic vs deal-specific).
- **Minutes 25–30:** Assign one specific **Step 4 Forensic Verification Test** to each of the 4 differential slots so Step 4 actively tests rather than merely confirms your diagnosis.

---

## Q1 Block B — Mandatory 5-Bucket QTC Diagnostic Probes

### Bucket 1: Commercial / Pricing
1. Does the true subscription discount exceed AE or VP approval tiers in `Artifact e`?
2. Were any list unit prices, services fees, or add-ons manually overwritten in `Artifact b`?
3. Does consolidated Gross Margin (and Year-1 standalone GM) fall below the written policy floor?
4. Do unit economics survive if the buyer triggers any ramp true-down or exit option?

### Bucket 2: Governance / Authority
1. Are all required written approvals (`Artifact e`) actually logged on the final P&L — or only verbal/Slack nods?
2. Has the Margin Exception or Deal Desk packet reached the named Finance/CFO approver's inbox?
3. Who inside Seller placed a hold (`Artifact d`), and how many days has that hold sat unworked?
4. On the buyer side, is the named CRM Economic Buyer the actual legal signatory (`Artifact c`) and budget holder (`Artifact d`)?

### Bucket 3: Config / Tools
1. Is the CRM record (`Artifact a`) synced to the live Quote (`Artifact b`) and Redline (`Artifact c`), or manually re-keyed offline?
2. Did stale CRM fields trigger a false-green automated approval rule (hiding a Tier-3/4 exception)?
3. Are spreadsheet list prices and margin floor checks locked, or editable without audit trails?
4. Does CRM allow `Forecast = Commit` even while Deal Desk or Legal status is `On Hold` / `Blocked`?

### Bucket 4: Paper / Redline
1. Did buyer counsel insert termination-for-convenience (opt-out) or seat true-down rights on a multi-year discount?
2. Did redlines move payment triggers from invoice/signature to subjective customer "acceptance"?
3. Did redlines alter liability caps (`>1x`), carve out uncapped security/IP, add SLA refund exits, cap renewal uplifts at `0%`, or insert MFN clauses?
4. Did buyer legal actually stall — or turn redlines promptly and wait on Seller?

### Bucket 5: Downstream Billability / Rev-Rec
1. Under **ASC 606**, does an opt-out or refund clause reduce enforceable contract term and unbook multi-year TCV?
2. Does acceptance-gated invoicing defer revenue recognition start and push DSO beyond 90–120 days?
3. Do true-downs, SLA refunds, or MFN credits create variable-consideration reversals?
4. Does upfront commission paid on multi-year TCV create immediate cash loss or clawback exposure if Year 1 ends in exit?

---

## Clinical Rules for the 4 Differential Slots

| Slot | Strict Diagnostic Standard | Common Error to Reject |
|---|---|---|
| **Leading Hypothesis** | Must explain the exact onset date, exact stall duration, exact internal/external block location, and cite Step 1 primary sources. | Repeating the AE's unverified story (*"buyer legal is slow"*). |
| **Can't-Miss / ROWS Threat** | Must quantify the worst-case post-signature blow-up (ASC 606 restatement, cash/margin loss, uncapped liability) even if likelihood is moderate. | Treating "losing the deal" as the worst-case scenario; signing a toxic contract is often far worse than losing it. |
| **Alternative Explanation #1** | Must be a plausible competing root cause (e.g., buyer-side non-budget / phantom deal) that would persist even if the Leading Hypothesis were fixed. | Writing a fake strawman alternative just to fill the box. |
| **Alternative Explanation #2** | Must test an independent mechanism (e.g., systemic CPQ/CRM control architecture failure vs individual AE error). | Restating the Leading Hypothesis in slightly different words. |

---

## Scoring Rubric (Used in Interactive Tool & Excel Matrix)
- **Bucket Weighted Risk Score** = `Severity (1–5) × Evidence Strength (1–5)` (Max = `25` per bucket; Composite Max = `125`).
  - `21–25` = **CRITICAL** | `15–20` = **HIGH** | `8–14` = **MODERATE** | `1–7` = **LOW**.
- **Differential Priority Score** = `Likelihood (1–5) × Impact (1–5)` (Max = `25` per hypothesis).
- **Gate to Step 4:** Locked until **5 / 5** QTC buckets are scanned AND **4 / 4** differential slots carry explicit Step 4 forensic verification tests.
