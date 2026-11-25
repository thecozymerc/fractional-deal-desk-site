#!/usr/bin/env python3
"""
Builds Raw Artifact (b): step1_sample_kestrel_b_pricing_spreadsheet.xlsx
Kestrel Industrial Holdings — Quote QT-2026-4819-v4 (3-Year Ramp & Margin Calculator)
"""

import sys
from pathlib import Path

try:
    from openpyxl import Workbook
    from openpyxl.comments import Comment
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter
except ImportError:
    print("ERROR: openpyxl is required. Install with: pip install openpyxl", file=sys.stderr)
    sys.exit(1)


def build_kestrel_pricing_workbook(output_file: str = "step1_sample_kestrel_b_pricing_spreadsheet.xlsx") -> None:
    wb = Workbook()

    thin = Side(border_style="thin", color="CBD5E1")
    med_top = Side(border_style="medium", color="0F172A")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    total_border = Border(left=thin, right=thin, top=med_top, bottom=med_top)

    navy_fill = PatternFill("solid", fgColor="0F172A")
    subhdr_fill = PatternFill("solid", fgColor="E2E8F0")
    subtotal_fill = PatternFill("solid", fgColor="F1F5F9")
    total_fill = PatternFill("solid", fgColor="DBEAFE")
    warn_fill = PatternFill("solid", fgColor="FEF3C7")
    fail_fill = PatternFill("solid", fgColor="FEE2E2")
    pass_fill = PatternFill("solid", fgColor="DCFCE7")

    # =========================================================================
    # TAB 1: Quote_Ramp_Calculator
    # =========================================================================
    ws = wb.active
    ws.title = "Quote_Ramp_Calculator"

    ws.merge_cells("A1:M1")
    ws["A1"] = "KESTREL INDUSTRIAL HOLDINGS — ENTERPRISE 3-YEAR RAMP QUOTE & MARGIN CALCULATOR"
    ws["A1"].font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    ws["A1"].fill = navy_fill
    ws["A1"].alignment = Alignment(horizontal="left", vertical="center")
    ws.row_dimensions[1].height = 28

    ws.merge_cells("A2:M2")
    ws["A2"] = "Quote ID: QT-2026-4819-v4 | CRM Opp: OPP-2026-4819 | Version Status: UNAPPROVED OFFLINE AE DRAFT (NOT SYNCED TO CRM)"
    ws["A2"].font = Font(name="Calibri", size=10, italic=True, color="991B1B")
    ws["A2"].fill = fail_fill

    # Metadata block (Rows 4-5)
    meta_cells = [
        (4, 1, "Account:", True), (4, 2, "Kestrel Industrial Holdings, Inc.", False),
        (4, 4, "Quote Date:", True), (4, 5, "2026-11-03", False),
        (4, 7, "Payment Terms:", True), (4, 8, "Net-60", False),
        (4, 10, "Policy GM Floor:", True), (4, 11, 0.75, False),
        (5, 1, "AE Owner:", True), (5, 2, "Jordan Reyes", False),
        (5, 4, "Contract Term:", True), (5, 5, "36 Months Ramp", False),
        (5, 7, "Opt-Out Modeled:", True), (5, 8, "NO (Not Modeled)", False),
        (5, 10, "Margin Sign-Off:", True), (5, 11, "NONE - Verbal VP Only", False),
    ]
    for r, c, val, is_bold in meta_cells:
        cell = ws.cell(r, c, val)
        cell.font = Font(bold=is_bold)
        if (r, c) == (4, 11):
            cell.number_format = "0.0%"
        if (r, c) in {(4, 8), (5, 8), (5, 11)}:
            cell.fill = warn_fill
            cell.font = Font(bold=True, color="92400E")

    ws["A7"] = "1. LINE-ITEM PRICING, DISCOUNT & GROSS MARGIN SCHEDULE"
    ws["A7"].font = Font(bold=True, size=11, color="0F172A")

    headers = [
        "Line", "SKU", "Description", "Qty", "List Unit Price",
        "Extended List", "Discretionary Disc %", "Discount $",
        "Net Revenue", "Direct Unit COGS", "Extended COGS",
        "Gross Profit", "Gross Margin %"
    ]
    for c_idx, h in enumerate(headers, start=1):
        cell = ws.cell(8, c_idx, h)
        cell.font = Font(bold=True, color="0F172A")
        cell.fill = subhdr_fill
        cell.border = border
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[8].height = 26

    # Rows 9-11: Subscription 3-Year Ramp (50 / 70 / 80 seats @ $1,500 list, 28% disc, $220 unit COGS)
    ramp_lines = [
        (9, 1, "ENT-PLAT-USR", "Year 1 Enterprise Platform Seats (Months 1-12)", 50, 1500, 0.28, 220),
        (10, 2, "ENT-PLAT-USR", "Year 2 Enterprise Platform Seats (Months 13-24)", 70, 1500, 0.28, 220),
        (11, 3, "ENT-PLAT-USR", "Year 3 Enterprise Platform Seats (Months 25-36)", 80, 1500, 0.28, 220),
    ]
    for r, line_no, sku, desc, qty, list_px, disc, cogs in ramp_lines:
        row_vals = [
            line_no, sku, desc, qty, list_px,
            f"=D{r}*E{r}", disc, f"=F{r}*G{r}", f"=F{r}-H{r}",
            cogs, f"=D{r}*J{r}", f"=I{r}-K{r}", f"=L{r}/I{r}"
        ]
        for c_idx, val in enumerate(row_vals, start=1):
            cell = ws.cell(r, c_idx, val)
            cell.border = border

    # Row 12: Subscription Subtotal
    sub_vals = [
        "", "SUB-TOTAL", "3-Year Enterprise Subscription Subtotal",
        "=SUM(D9:D11)", "", "=SUM(F9:F11)", "=H12/F12", "=SUM(H9:H11)",
        "=SUM(I9:I11)", "", "=SUM(K9:K11)", "=SUM(L9:L11)", "=L12/I12"
    ]
    for c_idx, val in enumerate(sub_vals, start=1):
        cell = ws.cell(12, c_idx, val)
        cell.font = Font(bold=True)
        cell.fill = subtotal_fill
        cell.border = border

    # Row 13: Implementation (AE MANUALLY OVERRODE E13 from $30,000 Standard List to $24,000!)
    impl_vals = [
        4, "ENT-IMPL-STD", "Enterprise Implementation & ERP Data Migration (Year 1)",
        1, 24000, "=D13*E13", 0.0, "=F13*G13", "=F13-H13",
        26000, "=D13*J13", "=I13-K13", "=L13/I13"
    ]
    for c_idx, val in enumerate(impl_vals, start=1):
        cell = ws.cell(13, c_idx, val)
        cell.border = border
    ws["E13"].fill = warn_fill
    ws["E13"].comment = Comment(
        "AE EDIT (Jordan Reyes, 2026-11-03): Overwrote standard $30,000 Price Book list to $24,000 so total equals $240K flat while keeping Discount % at 0.0%. Violates Policy PB-1.3.",
        "Forensic Audit Note"
    )
    ws["L13"].fill = fail_fill
    ws["M13"].fill = fail_fill

    # Row 14: TOTAL 3-YEAR DEAL
    tot_vals = [
        "", "TOTAL", "TOTAL 3-YEAR RAMP CONTRACT (TCV)",
        "", "", "=F12+F13", "=H14/F14", "=H12+H13",
        "=I12+I13", "", "=K12+K13", "=L12+L13", "=L14/I14"
    ]
    for c_idx, val in enumerate(tot_vals, start=1):
        cell = ws.cell(14, c_idx, val)
        cell.font = Font(bold=True, size=11)
        cell.fill = total_fill
        cell.border = total_border
    ws["M14"].fill = fail_fill
    ws["M14"].font = Font(bold=True, size=11, color="991B1B")

    # Apply number formats for Rows 9-14
    for r in range(9, 15):
        ws.cell(r, 4).number_format = "#,##0"
        for c in (5, 6, 8, 9, 10, 11, 12):
            ws.cell(r, c).number_format = "$#,##0"
        for c in (7, 13):
            ws.cell(r, c).number_format = "0.0%"

    # Section 2: Policy Threshold & Governance Checks (Rows 16-21)
    ws["A16"] = "2. AUTOMATED POLICY FLOOR & APPROVAL GATE CHECKS (LIVE FORMULAS)"
    ws["A16"].font = Font(bold=True, size=11, color="0F172A")

    gate_headers = ["Policy Control", "Policy Ref", "Quote Value", "Policy Threshold", "Variance / Deficit", "Automated Gate Status"]
    col_map = [1, 3, 4, 5, 6, 7]
    ws.merge_cells("A17:B17")
    ws.merge_cells("G17:M17")
    for idx, h in enumerate(gate_headers):
        cell = ws.cell(17, col_map[idx], h)
        cell.font = Font(bold=True)
        cell.fill = subhdr_fill
        cell.border = border
    for c in range(1, 14):
        ws.cell(17, c).border = border
        ws.cell(17, c).fill = subhdr_fill

    gate_rows = [
        (
            18, "Subscription Discretionary Discount", "PB-3.0", "=G12", 0.25, "=D18-E18",
            '=IF(D18>0.25,"FAIL — TIER 4 (>25%): VP SALES + FINANCE CONTROLLER/CFO WRITTEN SIGN-OFF REQUIRED",IF(D18>0.20,"TIER 3: FINANCE DIRECTOR REQUIRED","PASS"))',
            "0.0%", "0.0%", "+0.0%;-0.0%;0.0%"
        ),
        (
            19, "Deal Gross Margin Floor (3-Year TCV)", "PB-4.1", "=M14", "=K4", "=L14-(I14*K4)",
            '=IF(D19<E19,"FAIL — 70.8% GM IS BELOW 75.0% FLOOR BY $10,000 (MANDATORY FINANCE MARGIN SIGN-OFF)","PASS")',
            "0.0%", "0.0%", "$#,##0;($#,##0);$0"
        ),
        (
            20, "Payment Terms Standard", "PB-5.1", "=H4", "Net-30", "30+ Extra Days",
            '=IF(D20<>"Net-30","FAIL — NET-60 EXCEEDS STANDARD NET-30 (FINANCE CONTROLLER SIGN-OFF REQUIRED)","PASS")',
            "@", "@", "@"
        ),
        (
            21, "Written Margin Sign-Off on File", "PB-4.3", "=K5", "Written Finance Sign-Off", "Missing",
            '=IF(LEFT(D21,4)="NONE","FAIL — VERBAL VP APPROVAL INVALID WITHOUT WRITTEN FINANCE MARGIN SIGN-OFF","PASS")',
            "@", "@", "@"
        ),
    ]
    for r, ctrl, ref, qv, thresh, var_f, status_f, f1, f2, f3 in gate_rows:
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=2)
        ws.merge_cells(start_row=r, start_column=7, end_row=r, end_column=13)
        ws.cell(r, 1, ctrl).font = Font(bold=True)
        ws.cell(r, 3, ref).alignment = Alignment(horizontal="center")
        c_qv = ws.cell(r, 4, qv)
        c_th = ws.cell(r, 5, thresh)
        c_vr = ws.cell(r, 6, var_f)
        c_st = ws.cell(r, 7, status_f)
        c_qv.number_format = f1
        c_th.number_format = f2
        c_vr.number_format = f3
        c_st.fill = fail_fill
        c_st.font = Font(bold=True, color="991B1B")
        for c in range(1, 14):
            ws.cell(r, c).border = border

    widths_t1 = [7, 15, 44, 9, 15, 15, 16, 14, 15, 15, 15, 15, 15]
    for idx, w in enumerate(widths_t1, start=1):
        ws.column_dimensions[get_column_letter(idx)].width = w

    # =========================================================================
    # TAB 2: Year1_OptOut_Sensitivity
    # =========================================================================
    ws2 = wb.create_sheet("Year1_OptOut_Sensitivity")
    ws2.merge_cells("A1:D1")
    ws2["A1"] = "YEAR-1 MONTH-12 OPT-OUT EXPOSURE MODEL (ASC 606 & CASH IMPACT)"
    ws2["A1"].font = Font(size=13, bold=True, color="FFFFFF")
    ws2["A1"].fill = navy_fill
    ws2.row_dimensions[1].height = 26

    ws2.append(["Metric", "Formula / Amount", "Policy / Forensic Note", "Risk Severity"])
    for c in range(1, 5):
        ws2.cell(2, c).font = Font(bold=True)
        ws2.cell(2, c).fill = subhdr_fill
        ws2.cell(2, c).border = border

    optout_rows = [
        ("Headline 3-Year Committed TCV", "=Quote_Ramp_Calculator!I14", "$#,##0", "Quoted 3-year ramp total across 200 seat-years + impl", "BASELINE"),
        ("Year-1 Enforceable Revenue (if Month-12 Opt-Out Signed)", "=Quote_Ramp_Calculator!I9+Quote_Ramp_Calculator!I13", "$#,##0", "ASC 606 enforceable term collapses from 36 mo to 12 mo", "CRITICAL"),
        ("At-Risk Unenforceable Years 2-3 Revenue", "=B3-B4", "$#,##0", "67.5% of booked TCV walks away penalty-free at Month 12", "CRITICAL"),
        ("Year-1 Direct COGS (50 Seats + ERP Impl)", "=Quote_Ramp_Calculator!K9+Quote_Ramp_Calculator!K13", "$#,##0", "$11,000 Year-1 seat COGS + $26,000 implementation COGS", "HIGH"),
        ("Year-1 Gross Profit", "=B4-B6", "$#,##0", "Year-1 revenue minus Year-1 direct delivery cost", "HIGH"),
        ("Year-1 Gross Margin %", "=B7/B4", "0.0%", "22.4 percentage points below 75.0% policy GM floor", "CRITICAL"),
        ("Upfront AE Commission Paid on 3-Yr TCV (10%)", "=B3*0.10", "$#,##0", "Commission paid on $240K TCV before Month-12 opt-out", "HIGH"),
        ("Year-1 Net Contribution After Upfront Commission", "=B7-B9", "$#,##0", "Leaves only $17,000 before CS, support, and Net-60+ working capital", "CRITICAL"),
        ("Year-1 Net Contribution %", "=B10/B4", "0.0%", "Severely distressed Year-1 unit economics", "CRITICAL"),
        ("Foregone Years 2-3 Gross Profit if Opt-Out Exercised", "=Quote_Ramp_Calculator!L10+Quote_Ramp_Calculator!L11", "$#,##0", "Lost multi-year profit while giving 28% discount with zero clawback", "CRITICAL"),
    ]
    for offset, (label, formula, num_fmt, note, sev) in enumerate(optout_rows, start=3):
        ws2.cell(offset, 1, label).font = Font(bold=(offset in {4, 5, 8, 10}))
        val_c = ws2.cell(offset, 2, formula)
        val_c.number_format = num_fmt
        val_c.font = Font(bold=True)
        ws2.cell(offset, 3, note)
        sev_c = ws2.cell(offset, 4, sev)
        sev_c.alignment = Alignment(horizontal="center")
        if sev == "CRITICAL":
            sev_c.fill = fail_fill
            sev_c.font = Font(bold=True, color="991B1B")
        elif sev == "HIGH":
            sev_c.fill = warn_fill
            sev_c.font = Font(bold=True, color="92400E")
        else:
            sev_c.fill = pass_fill
        for c in range(1, 5):
            ws2.cell(offset, c).border = border

    for idx, w in enumerate([48, 18, 56, 15], start=1):
        ws2.column_dimensions[get_column_letter(idx)].width = w

    # =========================================================================
    # TAB 3: True_List_Leak_Bridge
    # =========================================================================
    ws3 = wb.create_sheet("True_List_Leak_Bridge")
    ws3.merge_cells("A1:C1")
    ws3["A1"] = "STANDARD PRICE BOOK vs QUOTE v4 LEAK BRIDGE"
    ws3["A1"].font = Font(size=13, bold=True, color="FFFFFF")
    ws3["A1"].fill = navy_fill
    ws3.row_dimensions[1].height = 26

    ws3.append(["Bridge Step", "Amount / %", "Audit Source"])
    for c in range(1, 4):
        ws3.cell(2, c).font = Font(bold=True)
        ws3.cell(2, c).fill = subhdr_fill
        ws3.cell(2, c).border = border

    bridge_rows = [
        ("Standard Price Book Subscription List (200 seat-yrs @ $1,500)", 300000, "$#,##0", "Policy PB-1.1 (ENT-PLAT-USR)"),
        ("Standard Price Book Implementation List", 30000, "$#,##0", "Policy PB-1.3 (ENT-IMPL-STD)"),
        ("True Standard Price Book Total List Value", "=B3+B4", "$#,##0", "True Baseline Before Any Concessions"),
        ("Visible Discretionary Subscription Discount (28.0%)", "=-Quote_Ramp_Calculator!H12", "$#,##0", "Quote_Ramp_Calculator!H12"),
        ("Hidden Implementation Cell Override ($30K -> $24K)", "=Quote_Ramp_Calculator!E13-B4", "$#,##0", "AE Manual Overwrite in Cell E13"),
        ("Total True Price Concession vs Standard Price Book", "=B6+B7", "$#,##0", "Combined Commercial Discount Leak"),
        ("Final Quoted 3-Year TCV", "=B5+B8", "$#,##0", "Reconciles to Quote_Ramp_Calculator!I14 ($240,000)"),
        ("True Blended Discount vs Standard Price Book", "=-B8/B5", "0.0%", "27.3% True Blended Discount"),
        ("Displayed Blended Discount on Quote Sheet", "=Quote_Ramp_Calculator!G14", "0.0%", "25.9% Displayed (Masks $6K Impl Override)"),
        ("Hidden Discount Masking Gap", "=B10-B11", "0.0%", "1.3 percentage points concealed by cell overwrite"),
    ]
    for offset, (label, formula, num_fmt, src) in enumerate(bridge_rows, start=3):
        ws3.cell(offset, 1, label).font = Font(bold=(offset in {5, 8, 9, 10}))
        c_val = ws3.cell(offset, 2, formula)
        c_val.number_format = num_fmt
        c_val.font = Font(bold=(offset in {5, 8, 9, 10}))
        ws3.cell(offset, 3, src)
        if offset in {7, 8, 12}:
            c_val.fill = fail_fill
        for c in range(1, 4):
            ws3.cell(offset, c).border = border

    for idx, w in enumerate([54, 18, 46], start=1):
        ws3.column_dimensions[get_column_letter(idx)].width = w

    out = Path(output_file).resolve()
    wb.save(out)
    print(f"SUCCESS: Built {out}")


if __name__ == "__main__":
    build_kestrel_pricing_workbook()
