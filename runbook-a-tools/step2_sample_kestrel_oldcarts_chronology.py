#!/usr/bin/env python3
"""
Builds Step 2 Sample 2: step2_sample_kestrel_oldcarts_chronology.xlsx
Kestrel Industrial Holdings — Completed OLDCARTS Chronology & Verified Timeline Log
"""

import sys
from datetime import date
from pathlib import Path

try:
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter
except ImportError:
    print("ERROR: openpyxl is required. Install with: pip install openpyxl", file=sys.stderr)
    sys.exit(1)


def build_kestrel_oldcarts(output_file: str = "step2_sample_kestrel_oldcarts_chronology.xlsx") -> None:
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
    # TAB 1: OLDCARTS_Matrix
    # =========================================================================
    ws = wb.active
    ws.title = "OLDCARTS_Matrix"

    ws.merge_cells("A1:G1")
    ws["A1"] = "RUNBOOK A — STEP 2 SAMPLE: KESTREL INDUSTRIAL HOLDINGS OLDCARTS CHRONOLOGY"
    ws["A1"].font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    ws["A1"].fill = navy_fill
    ws["A1"].alignment = Alignment(horizontal="left", vertical="center")
    ws.row_dimensions[1].height = 28

    ws.merge_cells("A2:G2")
    ws["A2"] = "Evidence Standard: Verified strictly from Step 1 Raw Artifacts (a–e). All non-artifact unknowns explicitly flagged UNVERIFIED."
    ws["A2"].font = Font(italic=True, size=10, color="1E293B")
    ws["A2"].fill = sub_fill

    meta = [
        (4, 1, "Account Name:", True), (4, 2, "Kestrel Industrial Holdings, Inc.", False),
        (4, 4, "Diagnostic Date:", True), (4, 5, date(2026, 11, 25), False),
        (4, 6, "Stall Onset Date (Redline):", True), (4, 7, date(2026, 11, 6), False),
        (5, 1, "CRM Opp ID:", True), (5, 2, "OPP-2026-4819", False),
        (5, 4, "Post-Redline Stall (Days):", True), (5, 5, "=E4-G4", False),
        (5, 6, "Headline Deal Value:", True), (5, 7, 240000, False),
    ]
    for r, c, val, is_bold in meta:
        cell = ws.cell(r, c, val)
        cell.font = Font(bold=is_bold)
        if (r, c) in {(4, 5), (4, 7)}:
            cell.number_format = "yyyy-mm-dd"
        if (r, c) == (5, 5):
            cell.font = Font(bold=True, color="991B1B")
            cell.fill = red_fill
            cell.number_format = "#,##0"
        if (r, c) == (5, 7):
            cell.number_format = "$#,##0"

    headers = [
        "Code", "OLDCARTS Dimension", "Clinical Question Applied to Deal",
        "Verified Kestrel Finding (Step 1 Raw Artifacts Only)", "Step 1 Artifact Citation",
        "Verification Status", "Explicit UNVERIFIED Gap / Unknown"
    ]
    for idx, h in enumerate(headers, start=1):
        c = ws.cell(7, idx, h)
        c.font = Font(bold=True, color="0F172A")
        c.fill = hdr_fill
        c.border = border
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[7].height = 26

    rows = [
        (
            "O", "Onset",
            "When did the stall begin and what precursor triggered it?",
            "Exact stall onset: 2026-11-06 10:14 ET when Kestrel GC Nadia Benali returned redlines (OF-2026-4819-v3) inserting Month-12 opt-out and Net-60 post-acceptance while stating CFO Gregory Cho has not approved budget. Precursor: 2026-11-03 16:40 ET when AE sent unapproved offline Quote v4 (28% sub discount, $24K impl override, Net-60) without Deal Desk or CRM update.",
            "c:L028-060; d:T018-050",
            "VERIFIED",
            "None for onset timestamp. (Note: exact verbal discussions between AE and Derek Halvorsen prior to Oct 28 are UNVERIFIED.)"
        ),
        (
            "L", "Location",
            "Where precisely is the deal blocked internally and externally?",
            "Two-sided block: (1) Internal — parked in Slack #deal-desk-approvals on Ticket DD-8842 under Deal Desk HARD HOLD (Priyesh Patel) and Legal HOLD (Tessa Morales); ZERO packet in Finance Controller Elena Rostova's queue; CRM still reads Stage 5 Commit. (2) External — blocked prior to Kestrel CFO Gregory Cho's Dec 2 Q4 budget committee docket.",
            "a:CRM-05,08,23,24; d:T047-076,T101-104",
            "VERIFIED",
            "None — exact internal ticket and external budget gate are verified in writing."
        ),
        (
            "D", "Duration",
            "How many days elapsed since onset, internal hold, and last buyer contact?",
            "19 calendar days post-redline (Nov 6 to Nov 25, live cell E5); 16 calendar days unaddressed on Deal Desk HARD HOLD (Nov 9 to Nov 25); 9 calendar days since buyer champion Derek Halvorsen's Nov 16 chase email; 26 calendar days in Stage 5 (Oct 30 to Nov 25); 103 total deal days since Aug 14 creation.",
            "a:CRM-01,06,07,31; d:T039,T062,T081,T099-103",
            "VERIFIED",
            "UNVERIFIED whether any unlogged phone calls occurred between AE and Derek Halvorsen during the 9 days from Nov 16 to Nov 25."
        ),
        (
            "C", "Character",
            "What is the verified nature of the stall?",
            "Silent internal governance deadlock combined with an unengaged economic buyer — NOT slow customer legal. Kestrel legal turned redlines promptly (3 days after Quote v4) and buyer chased seller on Nov 16. Internal Legal and Deal Desk halted because CRM (20%/Net-30/no opt-out) conflicts with Quote v4 (28%/70.8% GM/Net-60) and Redline (Month-12 opt-out/Net-60 acceptance), with verbal VP support only and zero Finance margin sign-off.",
            "a:CRM-15-26,32; b:Quote_Ramp_Calculator!G12,M14; d:T039-098",
            "VERIFIED",
            "None — character directly falsifies AE's 'slow buyer legal' narrative."
        ),
        (
            "A", "Aggravating / Alleviating",
            "What worsened the stall and what verified levers could relieve it?",
            "Verified aggravating factors: (1) AE manually overwrote impl cell E13 ($30K->$24K) and left CRM at 20%, bypassing automated Tier-4 alerts; (2) AE ignored Deal Desk's Nov 9 hold and Nov 12 bump for 16 days; (3) AE sought a 2nd casual Slack DM from VP Marcus Vance on Nov 18 without showing P&L/margin; (4) Dec 2 CFO budget committee deadline is now 6 days away. Verified policy relief paths exist under PB-5.3 (list-price clawback or >=50% ETF) and PB-4.2 (formal Finance exception).",
            "b:E13; d:T062-098; e:PB-4.2,PB-5.3",
            "PARTIAL - CONTAINS UNVERIFIED",
            "UNVERIFIED: (1) Seller Finance Controller Elena Rostova's willingness to grant any margin/Net-60 exception; (2) Buyer CFO Gregory Cho's willingness to trade opt-out or acceptance billing for a structured alternative; (3) VP Marcus Vance's support once shown true 70.8% GM."
        ),
        (
            "R", "Radiation",
            "Where else is this stuck deal spreading risk?",
            "Verified spread across 5 downstream areas: (1) Revenue Recognition (ASC 606 cuts enforceable TCV from $240K to $78K; $162K at risk); (2) Cash / Working Capital (Net-60 post-acceptance pushes Y1 collection ~105 days); (3) Gross Margin & Commission (70.8% 3-yr GM; 52.6% Y1 GM; $24K upfront commission leaves only $17K Y1 net contribution plus PB-6.2 clawback exposure); (4) Q4 Forecast Integrity ($240K sits falsely in Commit); (5) Contract Risk (3x/$720K liability cap, uncapped security, 20% true-down, MFN).",
            "a:CRM-08; b:Year1_OptOut_Sensitivity!B3:B12; c:L019-095; e:PB-5.1-6.2",
            "PARTIAL - CONTAINS UNVERIFIED",
            "UNVERIFIED: (1) Whether 45-day SAP/ERP cutover scope (c:L041) creates professional-services delivery cost overruns beyond $26,000 COGS (no SOW on file); (2) Whether a competing vendor threatens Kestrel if Dec 2 docket is missed."
        ),
        (
            "T", "Temporal Pattern",
            "What cadence, delays, and deadlines define the timeline?",
            "Repeated optimism + silent stalls: Close Date pushed twice (Oct 31 -> Nov 15 -> Nov 30) while held in Commit. Fast initial VP DM (+16m) and Legal triage (+1.6h) and Deal Desk audit (+1 business day) followed by 16 consecutive days of zero AE compliance on Ticket DD-8842 and 19 days of zero written turnaround to Kestrel. Hard buyer gate verified in writing: CFO Gregory Cho's Q4 budget committee meets Dec 2 (alignment needed before Dec 1 or project slips to Q2 2027).",
            "a:CRM-08-10; d:T027-104",
            "PARTIAL - CONTAINS UNVERIFIED",
            "UNVERIFIED: Exact hour and required documentation packet for Kestrel's Dec 2 budget committee docket; whether AE verbally communicated any unlogged promises to Derek after Nov 16."
        ),
        (
            "S", "Severity",
            "What is the verified financial, governance, and timing severity?",
            "CRITICAL (High-Impact Commercial & Governance Failure): $90,000 true concession off $330,000 standard list (27.3% blended); 70.8% GM ($10,000 below 75.0% policy floor); 4 simultaneous Tier-4/Executive policy breaches (PB-1.3, PB-3.0, PB-4.1/4.3, PB-5.1-5.4); $162,000 unenforceable TCV under Month-12 opt-out; 100% of $240K Q4 Commit at immediate risk of slipping to Q2 2027 within 6 days.",
            "b:Quote_Ramp_Calculator!D18:M21,True_List_Leak_Bridge!B5:B12; d:T064-076,T087; e:PB-1.3-5.4",
            "VERIFIED",
            "None on verified downside exposure; upside recovery probability remains UNVERIFIED until CFO and Finance respond."
        ),
    ]

    for offset, row_data in enumerate(rows, start=8):
        for c_i, val in enumerate(row_data, start=1):
            cell = ws.cell(offset, c_i, val)
            cell.border = border
            cell.alignment = Alignment(
                horizontal="center" if c_i in {1, 6} else "left",
                vertical="top",
                wrap_text=True
            )
            if c_i == 1:
                cell.font = Font(bold=True, size=11)
            elif c_i == 2:
                cell.font = Font(bold=True)
            elif c_i == 6:
                cell.font = Font(bold=True)
                cell.fill = green_fill if val == "VERIFIED" else amber_fill
        ws.row_dimensions[offset].height = 84

    ws["A17"] = "OLDCARTS EVIDENCE INTEGRITY SUMMARY (LIVE FORMULAS)"
    ws["A17"].font = Font(bold=True, size=11)
    summary = [
        (18, "Fully Verified Dimensions", '=COUNTIF(F8:F15,"VERIFIED")'),
        (19, "Dimensions With Explicit UNVERIFIED Gaps Logged", '=COUNTIF(F8:F15,"*UNVERIFIED*")'),
        (20, "Total Populated OLDCARTS Dimensions", '=COUNTA(D8:D15)'),
        (21, "Step 2 Chronology Gate", '=IF(C20=8,"COMPLETE — READY FOR STEP 3 SURGICAL SIEVE","INCOMPLETE")'),
    ]
    for r, label, formula in summary:
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=2)
        ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=7)
        ws.cell(r, 1, label).font = Font(bold=True)
        val_c = ws.cell(r, 3, formula)
        val_c.font = Font(bold=True)
        if r == 21:
            val_c.fill = green_fill
            val_c.font = Font(bold=True, color="166534")
        for c_i in range(1, 8):
            ws.cell(r, c_i).border = border

    for idx, w in enumerate([8, 22, 34, 54, 24, 28, 44], start=1):
        ws.column_dimensions[get_column_letter(idx)].width = w

    # =========================================================================
    # TAB 2: Verified_Timeline_Log
    # =========================================================================
    ws2 = wb.create_sheet("Verified_Timeline_Log")
    ws2.merge_cells("A1:H1")
    ws2["A1"] = "KESTREL INDUSTRIAL HOLDINGS — VERIFIED CHRONOLOGICAL TIMELINE (14 PRIMARY-SOURCE EVENTS)"
    ws2["A1"].font = Font(size=13, bold=True, color="FFFFFF")
    ws2["A1"].fill = navy_fill
    ws2.row_dimensions[1].height = 26

    t_headers = [
        "Event #", "Event Date", "Time (ET)", "Days Since Prior",
        "Days vs Redline Onset", "Actor / Channel", "Verified Event Description (Step 1 Facts Only)",
        "Step 1 Citation & Tag"
    ]
    for idx, h in enumerate(t_headers, start=1):
        c = ws2.cell(3, idx, h)
        c.font = Font(bold=True)
        c.fill = hdr_fill
        c.border = border
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    events = [
        ("E-01", date(2026, 8, 14), "09:20 ET", "Jordan Reyes / CRM", "Opportunity OPP-2026-4819 created for Kestrel Industrial Holdings from inbound enterprise demo.", "a:CRM-01,02 [VERIFIED]"),
        ("E-02", date(2026, 10, 28), "14:12 ET", "Derek Halvorsen (VP Ops) / Email", "Requests 3-yr ramp (50/70/80) <=$240K all-in incl. SAP/ERP, Net-60, and warns CFO Gregory Cho will require a 1-yr exit.", "d:T001-009 [VERIFIED]"),
        ("E-03", date(2026, 10, 30), "11:05 ET", "Jordan Reyes / Email & CRM", "Sends Quote v2 ($264K, 20% disc); advances CRM to Stage 5; logs 20% discount & Net-30 (auto-clears CRM Finance gate).", "a:CRM-05,15,22,26; d:T010-017 [VERIFIED]"),
        ("E-04", date(2026, 11, 3), "16:40 ET", "Jordan Reyes / Offline Excel & Email", "Sends unapproved Quote v4 ($240K TCV, 28% sub disc, manual $24K impl cell override, Net-60, 70.8% GM) without Deal Desk or CRM sync.", "b:Quote_Ramp_Calculator!E4,E13,M14; d:T018-026 [VERIFIED]"),
        ("E-05", date(2026, 11, 4), "09:38 ET", "Marcus Vance (VP Sales) / Slack DM", "Gives 16-min casual verbal Slack nod for '$240K on a 3-yr ramp' without seeing 28% disc, 70.8% GM, Net-60, or opt-out. AE types $240K in CRM.", "a:CRM-11; d:T027-038 [VERIFIED]"),
        ("E-06", date(2026, 11, 6), "10:14 ET", "Nadia Benali (Kestrel GC) / Email", "STALL ONSET (DAY 0): Returns redlines (OF-2026-4819-v3) adding Month-12 penalty-free opt-out, Net-60 post-acceptance, 20% true-down, 3x cap; discloses CFO Gregory Cho has NOT approved budget.", "c:L019-104; d:T039-050 [VERIFIED]"),
        ("E-07", date(2026, 11, 6), "16:18 ET", "Jordan Reyes -> Tessa Morales / Slack", "AE posts DD-8842 at 14:42 claiming VP blessed deal. Senior Counsel Tessa Morales places Legal on HOLD (+1.6h) citing opt-out, Net-60 acceptance, 3x cap, and 28% discount.", "a:CRM-24; d:T051-061 [VERIFIED]"),
        ("E-08", date(2026, 11, 9), "09:05 ET", "Priyesh Patel (Deal Desk) / Slack", "Places DD-8842 on HARD HOLD citing 5 control violations (CRM mismatch, Tier-4 28% disc, $6K impl override, 70.8% GM breach, ASC 606 opt-out). Orders AE to fix CRM & submit Finance Margin Exception.", "a:CRM-23; d:T062-076 [VERIFIED]"),
        ("E-09", date(2026, 11, 12), "17:10 ET", "Priyesh Patel (Deal Desk) / Slack", "Bumps AE on DD-8842: zero CRM update and zero Finance Margin Exception submitted to Elena Rostova. HARD HOLD continues.", "d:T077-080 [VERIFIED]"),
        ("E-10", date(2026, 11, 14), "13:02 ET", "Jordan Reyes / CRM", "Pushes Target Close Date a 2nd time (Oct 31 -> Nov 15 -> Nov 30) while leaving deal in Stage 5 Commit.", "a:CRM-08,09,10 [VERIFIED]"),
        ("E-11", date(2026, 11, 16), "11:30 ET", "Derek Halvorsen (VP Ops) / Email", "LAST VERIFIED EXTERNAL EVENT: Chases AE after 10 days of seller silence; warns CFO Gregory Cho's Q4 budget committee meets Dec 2 (must align before Dec 1 or slip to Q2 2027).", "a:CRM-31; d:T081-088 [VERIFIED]"),
        ("E-12", date(2026, 11, 18), "08:52 ET", "Jordan Reyes <-> Marcus Vance / Slack DM", "LAST VERIFIED INTERNAL EVENT: AE bypasses Desk to re-ping VP; Marcus repeats 'if Finance clears it, just get Desk what they need.' AE logs verbal approval in CRM Commit.", "a:CRM-08,21; d:T089-098 [VERIFIED]"),
        ("E-13", date(2026, 11, 20), "12:45 ET", "Jordan Reyes / CRM", "Updates CRM Next Step claiming 'Waiting on Kestrel legal to finish minor redlines' — contradicting Nov 6 GC email and Nov 9 HARD HOLD.", "a:CRM-32,33 [VERIFIED]"),
        ("E-14", date(2026, 11, 25), "09:00 ET", "Diagnostic Audit Pull (Day 19)", "DD-8842 remains on HARD HOLD (16d unaddressed), ZERO Finance Margin Exception submitted, ZERO redline turn sent to Kestrel (19d), ZERO meetings with CFO Gregory Cho.", "d:T099-104 [VERIFIED]"),
    ]

    for idx, (ev_id, ev_dt, ev_tm, actor, desc, cite) in enumerate(events, start=4):
        ws2.cell(idx, 1, ev_id).alignment = Alignment(horizontal="center", vertical="top")
        c_dt = ws2.cell(idx, 2, ev_dt)
        c_dt.number_format = "yyyy-mm-dd"
        c_dt.alignment = Alignment(horizontal="center", vertical="top")
        ws2.cell(idx, 3, ev_tm).alignment = Alignment(horizontal="center", vertical="top")
        c_prev = ws2.cell(idx, 4, 0 if idx == 4 else f"=B{idx}-B{idx-1}")
        c_prev.number_format = "#,##0"
        c_prev.alignment = Alignment(horizontal="center", vertical="top")
        c_onset = ws2.cell(idx, 5, f"=B{idx}-OLDCARTS_Matrix!$G$4")
        c_onset.number_format = "+#,##0;-#,##0;0"
        c_onset.alignment = Alignment(horizontal="center", vertical="top")
        ws2.cell(idx, 6, actor)
        ws2.cell(idx, 7, desc)
        ws2.cell(idx, 8, cite)

        if ev_id in {"E-06", "E-08", "E-14"}:
            for col_i in range(1, 9):
                ws2.cell(idx, col_i).fill = red_fill
        elif ev_id in {"E-11", "E-12"}:
            for col_i in range(1, 9):
                ws2.cell(idx, col_i).fill = amber_fill

        for col_i in range(1, 9):
            ws2.cell(idx, col_i).border = border
            if col_i >= 6:
                ws2.cell(idx, col_i).alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
        ws2.row_dimensions[idx].height = 46

    # Live Timeline KPIs (Rows 19-23)
    ws2["A19"] = "LIVE TIMELINE DURATION METRICS (EXCEL FORMULAS)"
    ws2["A19"].font = Font(bold=True, size=11)
    kpis = [
        (20, "Total Deal Age (Aug 14 to Nov 25)", "=B17-B4", "Days"),
        (21, "Post-Redline Stall Duration (Nov 6 to Nov 25)", "=B17-B9", "Days"),
        (22, "Days Ticket DD-8842 Sat Unaddressed on HARD HOLD (Nov 9 to Nov 25)", "=B17-B11", "Days"),
        (23, "Days Since Last Verified Customer Contact (Nov 16 to Nov 25)", "=B17-B14", "Days"),
    ]
    for r, label, formula, unit in kpis:
        ws2.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3)
        ws2.cell(r, 1, label).font = Font(bold=True)
        val_c = ws2.cell(r, 4, formula)
        val_c.font = Font(bold=True, color="991B1B")
        val_c.number_format = "#,##0"
        val_c.alignment = Alignment(horizontal="center")
        ws2.cell(r, 5, unit)
        for c_i in range(1, 6):
            ws2.cell(r, c_i).border = border

    for idx, w in enumerate([10, 14, 12, 16, 18, 28, 56, 28], start=1):
        ws2.column_dimensions[get_column_letter(idx)].width = w

    out = Path(output_file).resolve()
    wb.save(out)
    print(f"SUCCESS: Built {out}")


if __name__ == "__main__":
    build_kestrel_oldcarts()
