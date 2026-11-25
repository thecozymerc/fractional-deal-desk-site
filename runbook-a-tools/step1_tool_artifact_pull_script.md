# Runbook A — Step 1: Primary-Source Pull Script & Pre-Session Request Kit (10 Min)

## Purpose
Enforce the core clinical rule of Runbook A: pull all five raw primary-source artifacts **before** accepting the Account Executive's verbal story.

---

## 1. Pre-Session Request Email (Send 24 Hours Before Session)

**Subject:** Action Required Before Tomorrow's 2-Hour Deal Diagnostic — 5 Raw Files for [ACCOUNT NAME]

Hi [CLIENT LEAD],

To make sure we spend our 2 hours diagnosing [ACCOUNT NAME] from hard evidence rather than opinion, please drop the following **5 raw files** into our shared folder before we start:

1. **(a) CRM Opportunity Record** — Native CSV/PDF export of the opportunity page (including stage history, close date pushes, discount %, payment terms, and next-step notes).
2. **(b) Quote / Pricing Spreadsheet** — The actual working Excel/Google Sheet or CPQ quote sent to the buyer (with formulas intact — not a summary slide).
3. **(c) Latest Redlined Contract / Order Form** — The exact Word/PDF file returned by the buyer's legal or procurement team, with tracked changes and comments visible.
4. **(d) Approval / Slack / Email Thread** — Unedited export or thread transcript covering internal pricing approvals, Deal Desk/Legal holds, and the latest buyer correspondence.
5. **(e) Standard Price Book / Discount Policy** — Your official list prices, discount approval tiers, payment-term rules, and margin floor policy.

**One ground rule:** Please do **not** prepare a summary deck or ask the AE to pre-brief us verbally. Just like a physician reviews the raw lab panel before accepting a patient's self-diagnosis, we inspect the raw documents first.

If any file is missing, leave it blank — a missing control artifact is itself diagnostic evidence.

Best,  
[CLINICIAN NAME]

---

## 2. Pre-Session Slack / Teams Message (Day-Of Reminder)

> Quick reminder before our 2-hour diagnostic on **[ACCOUNT NAME]** at **[TIME]**: please confirm all 5 raw artifacts are in the folder (`a` CRM export, `b` live quote spreadsheet, `c` redlined contract, `d` approval/email thread, `e` price book & discount policy). No summary slides needed — raw files only so we clear Step 1 in 10 minutes flat.

---

## 3. Live 10-Minute Session Facilitation Script

### Minute 0:00–2:00 — Set the Clinical Boundary
> "Welcome to Runbook A. Over the next 2 hours, we are going to run a clinical diagnostic work-up on **[ACCOUNT NAME]** as Slot #1 in Validation Mode. The diagnosis belongs to you. Our first rule comes straight from clinical medicine: we pull primary-source labs before taking the story at face value. For the next 10 minutes, we are only verifying that we have the 5 raw artifacts — not debating why the deal is stuck yet."

### Minute 2:00–7:00 — Verify All 5 Raw Artifacts (In Order)
Read each line aloud while opening the actual file on screen:
1. **Artifact (a) CRM Record:** "Show me the native CRM record. What is the exact Opportunity ID, last modified date, discount entered, payment terms, and close date?"
2. **Artifact (b) Quote / Pricing Spreadsheet:** "Open the actual file sent to the prospect. Are formulas intact, and what is the exact file version and date?"
3. **Artifact (c) Redlined Contract / Order Form:** "Open the latest document returned by the buyer. What date did it arrive, who marked it up, and are comments intact?"
4. **Artifact (d) Approval / Slack / Email Thread:** "Show me the raw thread from internal pricing ask through the latest buyer message. Do we have exact timestamps?"
5. **Artifact (e) Standard Price Book / Discount Policy:** "Open the governing policy document. What version is active, and where are the approval tiers and margin floor written?"

### Minute 7:00–9:00 — Quarantine Verbal AE Claims
> "I have heard two or three verbal beliefs about why this deal stalled. I am writing them into the **Quarantined Claims** box right now. We are not calling anyone wrong — we are simply tagging every verbal claim as unverified until we test it against a document line or timestamp in Step 4."

### Minute 9:00–10:00 — Call the Gate Status
- **GREEN (5/5 native artifacts verified):** "Gate passed. All 5 primary sources are locked. Starting Step 2 — Focused History."
- **YELLOW (4/5 present, 1 missing/partial):** "Conditional pass. We will proceed, and the missing artifact (`[X]`) is logged as an evidence gap."
- **RED (<4 artifacts or only verbal summaries):** "Hard stop. Diagnosing without raw files guesses at the cause. Let's take 15 minutes to pull the real exports or reschedule when primary sources are in hand."

---

## 4. AE Storytelling Deflection Playbook (6 Common Pushbacks)

| What the AE / Sponsor Says | Verbatim Clinician Response |
|---|---|
| *"Let me give you the 10-minute backstory first so you have context."* | "I definitely want your history in Step 2 — right after we pull the 5 raw files. Opening the files first keeps us from anchoring on the wrong hypothesis." |
| *"I don't have the Excel handy, it's roughly a 25% discount."* | "In a forensic check, 'roughly' is where margin leaks hide. Let's pull the exact file from your sent folder or CPQ right now." |
| *"Our VP already verbally approved the pricing."* | "Great — I am logging 'verbal VP support' in the Quarantine Log. In Step 1 we still need the raw approval thread and the written policy to see what counts as sign-off." |
| *"The redlines are just standard legal boilerplate."* | "Let's open the raw Word/PDF redline anyway. Boilerplate redlines often hide opt-out or acceptance clauses that break rev-rec." |
| *"CRM is out of date — ignore what Salesforce says."* | "Do not fix CRM right now. A stale CRM record is primary evidence of a handoff failure, so we want the exact record as it sits today." |
| *"Can you just tell us how to reply to their GC right now?"* | "We diagnose first and never rescue mid-intake. Give us 2 hours to prove the exact failure point so you don't patch the wrong symptom." |

---

## 5. Primary-Source Acceptance Standard

| Artifact | ACCEPT (Primary Source) | REJECT (Hearsay / Secondary) |
|---|---|---|
| (a) CRM Record | Native CSV/JSON export or full printed CRM record with audit fields | Verbal recap or Forecast slide bullet |
| (b) Pricing Sheet | Native `.xlsx` / `.csv` / CPQ export with live formulas intact | Rounded dollar number typed into Slack |
| (c) Redlined Contract | Latest buyer-returned `.docx` / `.pdf` / `.md` with track changes & comments | AE summary of "only 2 minor redlines" |
| (d) Approval Thread | Raw timestamped Slack/email thread export including Deal Desk & Legal | Paraphrased "everyone is aligned" |
| (e) Price Book & Policy | Official Finance/Deal Desk policy file with version and effective date | "Our usual rule of thumb is around 20%" |

---

## 6. Standard Deal-Folder File Naming Convention

Save pulled artifacts in one read-only folder using these exact prefixes so automated scripts can verify them:
- `<deal>_a_crm_opportunity.<csv|pdf>`
- `<deal>_b_pricing_spreadsheet.<xlsx|csv>`
- `<deal>_c_redlined_contract.<docx|pdf|md>`
- `<deal>_d_approval_thread.<md|pdf|txt>`
- `<deal>_e_price_book_policy.<md|pdf|docx>`
