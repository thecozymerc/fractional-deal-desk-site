#!/usr/bin/env python3
"""
Builds Step 4 Sample 1: step4_sample_kestrel_three_way_diff.xlsx
Kestrel Industrial Holdings — Line-by-Line Forensic Three-Way Diff (CRM vs Quote v4 vs Redlined Contract vs Policy)
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


def build_kestrel_three_way_diff(output_file: str = "step4_sample_kestrel_three_way_diff.xlsx") -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Three_Way_Diff"

    thin = Side(border_style="thin", color="CBD5E1")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    navy_fill = PatternFill("solid", fgColor="0F172A")
    hdr_fill = PatternFill("solid", fgColor="E2E8F0")
    sub_fill = PatternFill("solid", fgColor="F1F5F9")
    green_fill = PatternFill("solid", fgColor="DCFCE7")
    amber_fill = PatternFill("solid", fgColor="FEF3C7")
    red_fill = PatternFill("solid", fgColor="FEE2E2")

    ws.merge_cells("A1:J1")
    ws["A1"] = "RUNBOOK A — STEP 4 SAMPLE: KESTREL INDUSTRIAL HOLDINGS — LINE-BY-LINE THREE-WAY DIFF"
    ws["A1"].font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    ws["A1"].fill = navy_fill
    ws["A1"].alignment = Alignment(horizontal="left", vertical="center")
    ws.row_dimensions[1].height = 28

    ws.merge_cells("A2:J2")
    ws["A2"] = "Forensic Line-by-Line Comparison: CRM (OPP-2026-4819) vs Quote Excel (QT-2026-4819-v4) vs Redlined Contract (OF-2026-4819-v3) vs Policy (POL-COMM-2026-v3)"
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
        "Diff #", "Commercial / Legal Line Item", "Artifact (a): CRM Record",
        "Artifact (b): Quote Calculator v4", "Artifact (c): Redlined Contract v3",
        "Artifact (e): Standard Policy", "3-Way Formula Check",
        "Severity", "Quantified Exposure ($)", "Exact Step 1 Citations"
    ]
    for idx, h in enumerate(headers, start=1):
        c = ws.cell(6, idx, h)
        c.font = Font(bold=True, color="0F172A")
        c.fill = hdr_fill
        c.border = border
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[6].height = 26

    diff_rows = [
        ("TW-01", "Headline 3-Year Face Value (TCV)", "$240,000", "$240,000", "$240,000", "$330,000 Standard List", "NONE", 0, "a:CRM-11; b:I14; c:L005; e:PB-1.1,1.3"),
        ("TW-02", "Seat Ramp Schedule & True-Down", "50/70/80 Firm Commitment", "50/70/80 Firm Commitment", "50/70/80 w/ 20% Y2-3 True-Down", "Firm Commitment; True-Down Prohibited", "CRITICAL", 32400, "a:CRM-13; b:D9:D11; c:L009-023; e:PB-2.2,2.3"),
        ("TW-03", "Subscription Discretionary Discount %", "20.0% (Stale v2 Entry)", "28.0% (-$84,000)", "$1,080/seat Net (28.0% Masked)", ">25% = Tier 4 (VP + CFO/Controller)", "CRITICAL", 24000, "a:CRM-15; b:G12,H12; c:L008; e:PB-3.0"),
        ("TW-04", "Year-1 ARR vs Reported ARR", "$80,000 (Flat $240K/3)", "$54,000 Y1 / $75.6K Y2 / $86.4K Y3", "$54,000 Y1 / $75.6K Y2 / $86.4K Y3", "Actual Y1 Recurring = $54,000", "HIGH", 26000, "a:CRM-12; b:I9:I11; c:L009-011"),
        ("TW-05", "Implementation Fee & List Price", "$24,000 (No List Check)", "$24,000 (Cell E13 Overridden from $30K)", "$24,000 Fixed Cap (50% Acceptance Holdback)", "$30,000 List; 0% Disc; 100% Upfront", "CRITICAL", 6000, "a:CRM-16; b:E13; c:L014-016,044-047; e:PB-1.3,5.2"),
        ("TW-06", "Consolidated 3-Year Gross Margin %", "(Blank — Optional Field)", "70.8% ($170K GP / $240K TCV)", "Not Stated (Zero Overage Cap Risk)", "Minimum 75.0% GM Floor ($180K GP)", "CRITICAL", 10000, "a:CRM-20; b:M14,F19; c:L015-016; e:PB-4.1"),
        ("TW-07", "Contract Term & Custom Opt-Out", "36 Months Non-Cancellable (Opt-Out FALSE)", "36 Months Committed (Opt-Out = NO)", "Month-12 Unilateral Opt-Out ($0 Fee / No Clawback)", "Prohibited >10% Disc w/o CFO+GC+Clawback", "CRITICAL", 162000, "a:CRM-14,18; b:H5,Year1_OptOut!B5; c:L028-038; e:PB-5.3"),
        ("TW-08", "Payment Terms & Invoicing Trigger", "Net-30 (Default; Acceptance FALSE)", "Net-60 (Invoice Trigger Unmodeled)", "Net-60 Post-Go-Live Acceptance (~105+ Days)", "Net-30 Upfront on Effective Date", "CRITICAL", 66000, "a:CRM-17,19; b:H4; c:L044-060; e:PB-5.1"),
        ("TW-09", "Attached / Governing Quote Document", "Kestrel_Quote_v2_20pct.pdf ($264K)", "QT-2026-4819-v4.xlsx ($240K)", "OF-2026-4819-v3-KESTREL-REDLINE ($240K)", "Exact 3-Way Match Mandatory (PB-6.1)", "HIGH", 24000, "a:CRM-25,26; b:A2; c:L001; e:PB-6.1"),
        ("TW-10", "Finance Margin Sign-Off Status", "Not Required (False-Green <=20%)", "NONE - Verbal VP Only (FAIL)", "Unsigned / ZERO Packet in Finance Queue", "Mandatory Written Controller/CFO Sign-Off", "CRITICAL", 10000, "a:CRM-22; b:K5,G21; d:T102; e:PB-4.2,4.3"),
        ("TW-11", "VP Sales Approval Status", "Verbal - Marcus Vance (Nov 4 & 18)", "NONE - Verbal VP Only", "Unsigned (VP Never Viewed v4 P&L)", "Written Approval on Final P&L; Verbal INVALID", "CRITICAL", 0, "a:CRM-21; b:K5; d:T032-038,095-098; e:PB-4.3"),
        ("TW-12", "Economic Buyer / Authorized Signatory", "Derek Halvorsen (VP Ops; Met=TRUE)", "Not Listed", "Gregory Cho (CFO — Sole Authority >$50K)", "Verified Signatory Required Before Commit", "CRITICAL", 240000, "a:CRM-28,29; c:L098-104; d:T047-049,104"),
        ("TW-13", "Renewal Uplift & Auto-Renewal", "Standard Implied (7% Auto-Renew)", "Not Modeled", "No Auto-Renew; 0% Cap for 2 Renewal Terms", "Auto-Renew w/ 7% Annual Uplift Cap", "HIGH", 18567, "c:L065-070; e:PB-5.4"),
        ("TW-14", "Limitation of Liability & Carve-Outs", "Standard Implied (12-Mo Fees)", "Not Modeled", "3x TCV ($720K) + UNCAPPED Sec/Conf/IP", "1x 12-Mo Fees Paid; No Uncapped Carve-Outs", "CRITICAL", 666000, "c:L083-089; e:PB-5.4"),
        ("TW-15", "SLA Credits & Refund Termination", "Standard Implied (10% Monthly)", "Not Modeled", "25% Annual Credit + Full Refund Exit (2 Misses)", "10% Monthly Pro-Rata; No Refund Exit", "CRITICAL", 78000, "c:L074-080; e:PB-5.4"),
        ("TW-16", "Most Favored Nation (MFN) Pricing", "None", "None", "Retroactive MFN (<=100-Seat Industrial)", "Strictly Prohibited Without GC + CFO", "CRITICAL", 0, "c:L092-095; e:PB-5.4"),
    ]

    for offset, (code, item, v_crm, v_qt, v_ct, v_pol, sev, exp, cite) in enumerate(diff_rows, start=7):
        ws.cell(offset, 1, code).font = Font(bold=True)
        ws.cell(offset, 2, item).font = Font(bold=True)
        ws.cell(offset, 3, v_crm)
        ws.cell(offset, 4, v_qt)
        ws.cell(offset, 5, v_ct)
        ws.cell(offset, 6, v_pol)
        c_chk = ws.cell(offset, 7, f'=IF(AND(C{offset}=D{offset},D{offset}=E{offset}),"MATCH","MISMATCH")')
        c_chk.font = Font(bold=True)
        is_match = (v_crm == v_qt == v_ct)
        c_chk.fill = green_fill if is_match else red_fill
        c_chk.font = Font(bold=True, color="166534" if is_match else "991B1B")

        c_sev = ws.cell(offset, 8, sev)
        c_sev.font = Font(bold=True)
        if sev == "CRITICAL":
            c_sev.fill = red_fill
            c_sev.font = Font(bold=True, color="991B1B")
        elif sev == "HIGH":
            c_sev.fill = amber_fill
            c_sev.font = Font(bold=True, color="92400E")
        else:
            c_sev.fill = green_fill

        c_exp = ws.cell(offset, 9, exp)
        c_exp.number_format = "$#,##0"
        c_exp.font = Font(bold=(exp > 0))
        ws.cell(offset, 10, cite)

        ws.row_dimensions[offset].height = 42
        for col_i in range(1, 11):
            cell = ws.cell(offset, col_i)
            cell.border = border
            cell.alignment = Alignment(
                horizontal="center" if col_i in {1, 7, 8} else ("right" if col_i == 9 else "left"),
                vertical="top",
                wrap_text=True
            )

    ws["A24"] = "KESTREL THREE-WAY DIFF FORENSIC SUMMARY (LIVE EXCEL FORMULAS)"
    ws["A24"].font = Font(bold=True, size=11)
    summary = [
        (25, "Total Commercial & Legal Lines Audited", "=COUNTA(A7:A22)", "#,##0"),
        (26, "Exact 3-Way Matches", '=COUNTIF(G7:G22,"MATCH")', "#,##0"),
        (27, "3-Way Mismatches Detected", '=COUNTIF(G7:G22,"MISMATCH")', "#,##0"),
        (28, "3-Way Mismatch Rate (%)", '=D27/D25', "0.0%"),
        (29, "CRITICAL Mismatch Lines", '=COUNTIFS(G7:G22,"MISMATCH",H7:H22,"CRITICAL")', "#,##0"),
        (30, "Gross Sum of Quantified Line Exposures (Note: Non-Additive Risk Indicators; See Leak Waterfall for Net Cash)", "=SUM(I7:I22)", "$#,##0"),
        (31, "Policy PB-6.1 Three-Way Match Gate Verdict", '=IF(D27=0,"PASS","HARD HOLD — 15 OF 16 LINES MISMATCHED (93.8%); VIOLATES PB-6.1")', "@"),
    ]
    for r, label, formula, nfmt in summary:
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3)
        ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=10)
        ws.cell(r, 1, label).font = Font(bold=True)
        vc = ws.cell(r, 4, formula)
        vc.font = Font(bold=True, color="991B1B" if r in {27, 28, 29, 31} else "0F172A")
        vc.number_format = nfmt
        if r == 31:
            vc.fill = red_fill
        for c_i in range(1, 11):
            ws.cell(r, c_i).border = border

    widths = [9, 32, 28, 30, 32, 28, 14, 12, 18, 30]
    for idx, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(idx)].width = w

    out = Path(output_file).resolve()
    wb.save(out)
    print(f"SUCCESS: Built {out}")


if __name__ == "__main__":
    build_kestrel_three_way_diff()
