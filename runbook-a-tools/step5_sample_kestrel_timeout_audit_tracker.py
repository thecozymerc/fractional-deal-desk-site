#!/usr/bin/env python3
"""
Builds Step 5 Sample 2: step5_sample_kestrel_timeout_audit_tracker.xlsx
Kestrel Industrial Holdings — Completed Ely / Graber / TWED Time-Out & Step 6 Claim-to-Evidence Gate
"""

import sys
from pathlib import Path

try:
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter
except ImportError:
    print("ERROR: openpyxl is required. Install with: pip install openpyxl", file=sys.stderr)
    sys.exit(1)


def build_kestrel_step5_workbook(output_file: str = "step5_sample_kestrel_timeout_audit_tracker.xlsx") -> None:
    wb = Workbook()

    thin = Side(border_style="thin", color="CBD5E1")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    navy_fill = PatternFill("solid", fgColor="0F172A")
    hdr_fill = PatternFill("solid", fgColor="E2E8F0")
    sub_fill = PatternFill("solid", fgColor="F1F5F9")
    green_fill = PatternFill("solid", fgColor="DCFCE7")
    amber_fill = PatternFill("solid", fgColor="FEF3C7")
    red_fill = PatternFill("solid", fgColor="FEE2E2")

    # =========================================================================
    # TAB 1: Ely_Graber_TWED_Gate
    # =========================================================================
    ws = wb.active
    ws.title = "Ely_Graber_TWED_Gate"

    ws.merge_cells("A1:H1")
    ws["A1"] = "RUNBOOK A — STEP 5 SAMPLE: KESTREL INDUSTRIAL HOLDINGS DIAGNOSTIC TIME-OUT (ELY / GRABER / TWED)"
    ws["A1"].font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    ws["A1"].fill = navy_fill
    ws["A1"].alignment = Alignment(horizontal="left", vertical="center")
    ws.row_dimensions[1].height = 28

    ws.merge_cells("A2:H2")
    ws["A2"] = "Tests Step 3 Leading Hypothesis & Step 4 Forensic Findings. Flags 6 real time-out catches and 4 candidate Step 6 statement failures."
    ws["A2"].font = Font(italic=True, size=10, color="1E293B")
    ws["A2"].fill = sub_fill

    meta = [
        (4, 1, "Account Name:", True), (4, 2, "Kestrel Industrial Holdings, Inc.", False),
        (4, 4, "CRM Opp ID:", True), (4, 5, "OPP-2026-4819", False),
        (4, 7, "Diagnostic Date:", True), (4, 8, "2026-11-25", False),
    ]
    for r, c, val, is_bold in meta:
        ws.cell(r, c, val).font = Font(bold=is_bold)

    headers = [
        "Code", "Framework", "Clinical Safety Check", "Gate Status",
        "Kestrel Stress-Test Result (Steps 3 & 4)", "Step 1–4 Citation",
        "Catch Flagged?", "Mandatory Step 6 Correction / Guardrail"
    ]
    for idx, h in enumerate(headers, start=1):
        c = ws.cell(6, idx, h)
        c.font = Font(bold=True)
        c.fill = hdr_fill
        c.border = border
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[6].height = 26

    controls = [
        ("ELY-1", "Ely Time-Out", "Reviewed all 5 raw artifacts before accepting AE framing?", "PASS", "All 5 native files (a–e) verified in Step 1 before Step 2 interview; 4 AE claims quarantined.", "Step 1 Gate (a–e)", "None — clean."),
        ("ELY-2", "Ely Time-Out", "Does Leading Hypothesis explain ALL verified data cleanly?", "FAIL - REMEDIATED", "CAUGHT: Over-focusing on AE inaction (85.4% hop share) omits Seller's broken CRM/Excel controls AND Buyer CFO's unfunded budget.", "a:CRM-22,25; b:E13; d:T047-049", "Step 6 frames dual root cause: Internal Governance/Tooling Deadlock + External CFO Budget Gate."),
        ("ELY-3", "Ely Time-Out", "Can't-Miss / ROWS worst-case threat quantified?", "PASS", "3-Window Engine quantified $162K ASC 606 collapse, 52.6% Y1 GM / $17K net, ~105d DSO, $720K/uncapped cap, MFN.", "Step 4 Window 1 & 3", "Lead Step 6 Beat 2 with verified ROWS exposure."),
        ("ELY-4", "Ely Time-Out", "Disconfirming evidence actively hunted against both stories?", "PASS", "5 buyer claims (P-1..P-5) and 5 AE claims (A-1..A-5) disconfirmed with exact lines/timestamps.", "Step 4 Sample 4", "None — clean."),
        ("ELY-5", "Ely Time-Out", "All unverified unknowns explicitly quarantined?", "PASS", "7 unknowns (U-1..U-7) and 4 base-MSA flags (F35..F38) explicitly tagged UNVERIFIED.", "Step 2 & Step 4", "Preserve UNVERIFIED tags in Step 6."),
        ("GRB-C1", "Graber — Cognitive", "Anchoring Bias: Rejected AE's 'slow buyer legal' story?", "PASS", "Hop audit proves 0.0% post-redline stall belonged to Kestrel GC (2.7-day pre-stall turn; buyer chased Nov 16).", "d:T039,081; Hop Audit", "None — clean."),
        ("GRB-C2", "Graber — Cognitive", "Premature Closure: Scanned all 5 QTC buckets + 51 flags?", "PASS", "All 5 Q1 Block B buckets scored (120/125) and all 51 flags (F01–F51) evaluated.", "Step 3 & Step 4", "None — clean."),
        ("GRB-C3", "Graber — Cognitive", "Confirmation Bias: Tested claims against buyer & seller?", "PASS", "Completed both Part A (Prospect) and Part B (Internal) falsification tables.", "Step 4 Sample 4", "None — clean."),
        ("GRB-C4", "Graber — Cognitive", "Framing Effect: Stripped '$240K Q4 Commit' bias?", "PASS", "Reframed headline $240K to $78K ASC 606 enforceable TCV and $17K Y1 net contribution.", "b:Year1_OptOut!B4:B11", "None — clean."),
        ("GRB-C5", "Graber — Cognitive", "Attribution Bias: Separated system defects from rep error?", "FAIL - REMEDIATED", "CAUGHT: 85.4% AE stall share tempts scapegoating Jordan Reyes while missing false-green CRM clearance, unsynced Excel, unlocked E13, and unblocked Commit.", "a:CRM-08,15-26; b:E13", "Step 6 highlights failed system controls & handoffs alongside AE non-compliance; sets up Step 6 Bridge."),
        ("GRB-C6", "Graber — Cognitive", "Search Satisficing: Audited every hop & timestamp?", "PASS", "All 12 hops (H-01..H-12) reconciled 100.0% of 454.8-hr post-redline stall.", "Step 4 Hop Audit", "None — clean."),
        ("GRB-S1", "Graber — System", "Missing Artifacts: Base MSA & ERP SOW scope limit flagged?", "FAIL - REMEDIATED", "CAUGHT: Base MSA and signed ERP SOW were NOT pulled in Step 1; flags F35–F38 & 45-day ERP cutover cost (U-4) remain UNVERIFIED.", "c:L001-104; U-4; F35-38", "Explicitly scope Step 6 legal count to 47 Order Form clauses + 4 UNVERIFIED base-MSA checks; flag SOW absence."),
        ("GRB-S2", "Graber — System", "Handoff Ownership: Every stall hour tied to owner & time?", "PASS", "AE 388.3h (85.4%), Desk 64.8h (14.2%), Legal 1.6h (0.4%), VP 0.1h, Finance 0.0h, Buyer Legal 0.0h.", "Step 4 Hop Audit", "None — clean."),
        ("GRB-S3", "Graber — System", "False-Green Controls: Automated CRM false-green caught?", "PASS", "CRM Finance_Margin_SignOff__c auto-cleared <=20% due to stale 20.0% entry.", "a:CRM-15,22", "Highlight false-green control failure in Step 6 Beat 2."),
        ("GRB-S4", "Graber — System", "Client Ownership: Diagnosis preserved for client decision?", "PASS", "Readout frames findings and options strictly for client ownership.", "Runbook A Purpose", "None — clean."),
        ("TWED-T", "TWED Check", "T (Threat): What blows up post-signature if closed as written?", "PASS", "ASC 606 collapses TCV $240K->$78K (-$162K); Y1 GM 52.6% / $17K net after $24K comm; -$2K impl loss; ~105d DSO; $720K + uncapped sec/IP; 25% SLA refund exit; 20% true-down; MFN.", "b:Year1_OptOut; c:L015-095", "State exact non-overlapping Threat numbers in Step 6 Beat 2."),
        ("TWED-W", "TWED Check", "W (What else?): Rejected AE framing? Other stall causes?", "FAIL - REMEDIATED", "CAUGHT: Beyond AE's 16-day unworked HARD HOLD, two co-drivers explain Kestrel: (1) Unengaged CFO Gregory Cho w/ zero budget approval & Ohio consolidation risk; (2) Seller's broken QTC tooling.", "d:T047-049,104; c:L022-023; a:CRM-22,25", "Step 6 explains Cause X (dual internal governance/tooling deadlock + unengaged CFO gate) vs Cause Y ('slow legal' or 'lone rep')."),
        ("TWED-E", "TWED Check", "E (Evidence): Every finding tied to line/timestamp & clean math?", "FAIL - REMEDIATED", "CAUGHT: (1) Three-Way Diff $1,334,967 raw sum is NON-ADDITIVE (overlaps risks); (2) F35–F38 & U-1..U-7 lack primary docs.", "Step 4 Sample 1 & 2; U-1..U-7", "Ban $1.33M raw sum from Step 6; cite only Waterfall figures ($90K/$10K/$162K/$17K) + separate legal cap + explicit UNVERIFIED scope."),
        ("TWED-D", "TWED Check", "D (Dispositional): Getting sucked into rescuing the deal?", "FAIL - REMEDIATED", "CAUGHT: Dec 2 CFO budget docket (6 days away) + $240K Commit creates heavy pressure to draft redlines, email GC Nadia Benali, or call CFO Cho / Finance.", "d:T086-088; a:CRM-08", "HARD NO-RESCUE LOCK: Clinician delivers diagnosis + client-owned MESO options ONLY in Step 6 Beat 3."),
    ]

    for offset, (code, fw, prompt, st, res, cite, fix) in enumerate(controls, start=7):
        ws.cell(offset, 1, code).font = Font(bold=True)
        ws.cell(offset, 2, fw).font = Font(bold=("TWED" in fw))
        ws.cell(offset, 3, prompt)
        c_st = ws.cell(offset, 4, st)
        c_st.font = Font(bold=True, color="166534" if st == "PASS" else "92400E")
        c_st.fill = green_fill if st == "PASS" else amber_fill
        ws.cell(offset, 5, res)
        ws.cell(offset, 6, cite)
        c_fl = ws.cell(offset, 7, f'=IF(LEFT(D{offset},4)="FAIL","YES","NO")')
        c_fl.font = Font(bold=True)
        if st != "PASS":
            c_fl.fill = amber_fill
        ws.cell(offset, 8, fix)
        ws.row_dimensions[offset].height = 56 if st != "PASS" else 38
        for col_i in range(1, 9):
            cell = ws.cell(offset, col_i)
            cell.border = border
            cell.alignment = Alignment(
                horizontal="center" if col_i in {1, 4, 7} else "left",
                vertical="top",
                wrap_text=True
            )

    ws["A27"] = "KESTREL STEP 5 DIAGNOSTIC TIME-OUT RELEASE GATE (LIVE CROSS-TAB FORMULAS)"
    ws["A27"].font = Font(bold=True, size=11)
    summary = [
        (28, "Total Ely / Graber / TWED Controls Evaluated", "=COUNTA(A7:A25)"),
        (29, "Clean PASS Controls", '=COUNTIF(D7:D25,"PASS")'),
        (30, "Time-Out Failures Caught & Remediated", '=COUNTIF(D7:D25,"FAIL - REMEDIATED")'),
        (31, "Unresolved FAIL - BLOCKING Controls (Must = 0)", '=COUNTIF(D7:D25,"FAIL - BLOCKING")'),
        (32, "Candidate Step 6 Statements Caught by Raw Audit (Tab 2)", '=COUNTIF(Readout_Claim_Audit!F5:F16,"FAIL*")'),
        (33, "Unresolved BLOCKED Claims on Tab 2 (Must = 0)", '=COUNTIF(Readout_Claim_Audit!G5:G16,"BLOCKED*")'),
        (34, "Step 5 Readout Release Gate Verdict", '=IF(AND(D31=0,D33=0),"GREEN — TIME-OUT CLEARED (6 CATCHES + 4 CLAIMS REMEDIATED); AUTHORIZED FOR STEP 6","RED — HARD STOP")'),
    ]
    for r, label, formula in summary:
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3)
        ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=8)
        ws.cell(r, 1, label).font = Font(bold=True)
        vc = ws.cell(r, 4, formula)
        vc.font = Font(bold=True)
        if r == 34:
            vc.fill = green_fill
            vc.font = Font(bold=True, color="166534")
        elif r in {30, 32}:
            vc.fill = amber_fill
            vc.font = Font(bold=True, color="92400E")
        for c_i in range(1, 9):
            ws.cell(r, c_i).border = border

    for idx, w in enumerate([10, 20, 36, 20, 48, 22, 14, 44], start=1):
        ws.column_dimensions[get_column_letter(idx)].width = w

    # =========================================================================
    # TAB 2: Readout_Claim_Audit
    # =========================================================================
    ws2 = wb.create_sheet("Readout_Claim_Audit")
    ws2.merge_cells("A1:H1")
    ws2["A1"] = "KESTREL STEP 5 PRE-READOUT CLAIM-TO-EVIDENCE AUDIT (12 CANDIDATE STEP 6 STATEMENTS)"
    ws2["A1"].font = Font(size=13, bold=True, color="FFFFFF")
    ws2["A1"].fill = navy_fill
    ws2.row_dimensions[1].height = 26

    ws2.merge_cells("A2:H2")
    ws2["A2"] = "Tests 12 proposed Step 6 statements against TWED 'E' (Evidence) and 'D' (No-Rescue). 8 pass clean; 4 fail raw audit and are stripped/rewritten."
    ws2["A2"].font = Font(italic=True, size=10, color="1E293B")
    ws2["A2"].fill = sub_fill

    c_hdr = [
        "ID", "Candidate Step 6 Readout Statement", "Line/Time Cited?",
        "Math & Scope Valid?", "No-Rescue / Non-Blame?", "Raw Audit Result",
        "Final Disposition", "Approved Step 6 Wording / Remediation"
    ]
    for idx, h in enumerate(c_hdr, start=1):
        c = ws2.cell(4, idx, h)
        c.font = Font(bold=True)
        c.fill = hdr_fill
        c.border = border
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    claims = [
        ("R-01", "19-day post-redline stall: 0.0% Buyer Legal, 85.4% (388.3h) unworked AE hold on DD-8842, 0.0% Finance.", "YES", "YES", "YES", "CLEARED FOR STEP 6", "Approved verbatim (d:T039-103; Hop Audit H-05..H-12)."),
        ("R-02", "True pricing = 28.0% sub discount (-$84K) + hidden $6K impl override ($30K->$24K) = $90K (27.3%) off $330K list.", "YES", "YES", "YES", "CLEARED FOR STEP 6", "Approved verbatim (b:G12,E13,True_List_Leak_Bridge!B5:B10; e:PB-1.3)."),
        ("R-03", "3-year GM = 70.8% ($170K/$240K), $10K below 75.0% floor; verbal VP nods invalid under PB-4.3.", "YES", "YES", "YES", "CLEARED FOR STEP 6", "Approved verbatim (b:M14,F19; d:T036,095,102; e:PB-4.1,4.3)."),
        ("R-04", "Month-12 penalty-free opt-out cuts ASC 606 enforceable TCV 67.5% ($240K->$78K; $162K at risk); Y1 net = $17K.", "YES", "YES", "YES", "CLEARED FOR STEP 6", "Approved verbatim (c:L028-035; b:Year1_OptOut_Sensitivity!B3:B11)."),
        ("R-05", "Net-60 post-Go-Live Acceptance defers $66K Y1 billing ~105+ days under subjective customer discretion.", "YES", "YES", "YES", "CLEARED FOR STEP 6", "Approved verbatim (c:L041-060; e:PB-5.1,5.2)."),
        ("R-06", "Real Economic Buyer & sole signatory >$50K is CFO Gregory Cho (0 meetings, 0 budget approval), contradicting CRM.", "YES", "YES", "YES", "CLEARED FOR STEP 6", "Approved verbatim (a:CRM-28,29; c:L100-104; d:T047-049,104)."),
        ("R-07", "Three-Way Diff shows 15/16 lines mismatched (93.8%); CRM auto-cleared Finance based on stale 20.0% entry.", "YES", "YES", "YES", "CLEARED FOR STEP 6", "Approved verbatim (a:CRM-15,22,25; Three-Way Diff TW-01..TW-16)."),
        ("R-08", "41 of 51 contract flags triggered (20 CRITICAL) incl. $720K cap, uncapped sec/IP, 25% SLA exit, MFN (4 MSA flags UNVERIFIED).", "YES", "YES", "YES", "CLEARED FOR STEP 6", "Approved with explicit 47 Order Form / 4 UNVERIFIED base-MSA scope note."),
        ("R-09", "CANDIDATE: 'Kestrel carries $1.33M in direct commercial dollar exposure across the Three-Way Diff.'", "YES", "NO", "YES", "REMEDIATED — REWRITTEN/STRIPPED", "STRIPPED (TWED-E): $1,334,967 is non-additive. Use Waterfall ($90K/$10K/$162K/$17K) + separate $720K/uncapped legal cap."),
        ("R-10", "CANDIDATE: 'The 19-day stall is purely an AE discipline failure by Jordan Reyes.'", "YES", "NO", "NO", "REMEDIATED — REWRITTEN/STRIPPED", "REWRITTEN (ELY-2/GRB-C5/TWED-W): Dual internal governance/tooling breakdown + unengaged Buyer CFO budget gate."),
        ("R-11", "CANDIDATE: 'We audited all 51 MSA & Order Form clauses and confirmed Kestrel CFO has no Q4 budget.'", "NO", "NO", "YES", "REMEDIATED — REWRITTEN/STRIPPED", "REWRITTEN (GRB-S1/TWED-E): Scope to 47 Order Form clauses + 4 UNVERIFIED MSA checks; CFO budget availability is UNVERIFIED (U-1)."),
        ("R-12", "CANDIDATE: 'To beat Dec 1, our team will redline OF-2026-4819-v3 and join tomorrow's call with CFO Gregory Cho.'", "YES", "YES", "NO", "REMEDIATED — REWRITTEN/STRIPPED", "STRIPPED (TWED-D): Violates Clean Boundary (No Rescue). Provide client-owned MESO options only."),
    ]

    for offset, (cid, txt, c1, c2, c3, disp, fix) in enumerate(claims, start=5):
        ws2.cell(offset, 1, cid).font = Font(bold=True)
        ws2.cell(offset, 2, txt)
        ws2.cell(offset, 3, c1)
        ws2.cell(offset, 4, c2)
        ws2.cell(offset, 5, c3)
        c_raw = ws2.cell(offset, 6, f'=IF(AND(C{offset}="YES",D{offset}="YES",E{offset}="YES"),"PASS","FAIL — CAUGHT BY TIME-OUT")')
        raw_pass = (c1 == "YES" and c2 == "YES" and c3 == "YES")
        c_raw.font = Font(bold=True, color="166534" if raw_pass else "991B1B")
        c_raw.fill = green_fill if raw_pass else red_fill
        c_dp = ws2.cell(offset, 7, disp)
        c_dp.font = Font(bold=True, color="166534" if raw_pass else "92400E")
        c_dp.fill = green_fill if raw_pass else amber_fill
        ws2.cell(offset, 8, fix)
        ws2.row_dimensions[offset].height = 46 if not raw_pass else 36
        for col_i in range(1, 9):
            cell = ws2.cell(offset, col_i)
            cell.border = border
            cell.alignment = Alignment(
                horizontal="center" if col_i in {1, 3, 4, 5, 6, 7} else "left",
                vertical="top",
                wrap_text=True
            )

    ws2["A18"] = "TAB 2 CLAIM AUDIT SUMMARY"
    ws2["A18"].font = Font(bold=True)
    ws2["A19"] = "Total Statements Audited"
    ws2["B19"] = "=COUNTA(A5:A16)"
    ws2["A20"] = "Passed Raw Audit Clean"
    ws2["B20"] = '=COUNTIF(F5:F16,"PASS")'
    ws2["A21"] = "Failed Raw Audit (Caught & Fixed)"
    ws2["B21"] = '=COUNTIF(F5:F16,"FAIL*")'
    ws2["A22"] = "Remaining Unresolved Blockers"
    ws2["B22"] = '=COUNTIF(G5:G16,"BLOCKED*")'
    for r in range(19, 23):
        ws2.cell(r, 1).font = Font(bold=True)
        ws2.cell(r, 2).font = Font(bold=True)
        ws2.cell(r, 1).border = border
        ws2.cell(r, 2).border = border

    for idx, w in enumerate([8, 46, 15, 16, 18, 25, 28, 48], start=1):
        ws2.column_dimensions[get_column_letter(idx)].width = w

    out = Path(output_file).resolve()
    wb.save(out)
    print(f"SUCCESS: Built {out}")


if __name__ == "__main__":
    build_kestrel_step5_workbook()
