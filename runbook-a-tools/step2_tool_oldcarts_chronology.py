#!/usr/bin/env python3
"""
Runbook A — Step 2 Reusable OLDCARTS Deal Chronology Template Builder.
Builds: step2_tool_oldcarts_chronology_template.xlsx
"""

import argparse
import sys
from pathlib import Path

try:
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter
    from openpyxl.worksheet.datavalidation import DataValidation
except ImportError:
    print("ERROR: openpyxl is required. Install with: pip install openpyxl", file=sys.stderr)
    sys.exit(1)


def build_oldcarts_template(output_path: str = "step2_tool_oldcarts_chronology_template.xlsx") -> None:
    wb = Workbook()

    thin = Side(border_style="thin", color="CBD5E1")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    navy_fill = PatternFill("solid", fgColor="0F172A")
    hdr_fill = PatternFill("solid", fgColor="E2E8F0")
    sub_fill = PatternFill("solid", fgColor="F1F5F9")
    input_fill = PatternFill("solid", fgColor="FFFBEB")

    # =========================================================================
    # TAB 1: OLDCARTS_Matrix
    # =========================================================================
    ws = wb.active
    ws.title = "OLDCARTS_Matrix"

    ws.merge_cells("A1:G1")
    ws["A1"] = "RUNBOOK A — STEP 2: OLDCARTS DEAL CHRONOLOGY WORKSHEET (BLANK TEMPLATE)"
    ws["A1"].font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    ws["A1"].fill = navy_fill
    ws["A1"].alignment = Alignment(horizontal="left", vertical="center")
    ws.row_dimensions[1].height = 28

    ws.merge_cells("A2:G2")
    ws["A2"] = "Clinical Rule: Enter ONLY Step 1 primary-source facts in Column D. Flag every unproven item explicitly in Column F and Column G."
    ws["A2"].font = Font(italic=True, size=10, color="1E293B")
    ws["A2"].fill = sub_fill

    meta_pairs = [
        (4, 1, "Account Name:", True), (4, 2, "[Enter Account]", False),
        (4, 4, "Diagnostic Date (YYYY-MM-DD):", True), (4, 5, "", False),
        (4, 6, "Stall Onset Date (YYYY-MM-DD):", True), (4, 7, "", False),
        (5, 1, "CRM Opp ID:", True), (5, 2, "[Enter Opp ID]", False),
        (5, 4, "Calculated Stall Duration (Days):", True),
        (5, 5, '=IF(AND(ISNUMBER(E4),ISNUMBER(G4)),E4-G4,"Enter Dates")', False),
        (5, 6, "Headline Deal Value ($):", True), (5, 7, "", False),
    ]
    for r, c, val, is_bold in meta_pairs:
        cell = ws.cell(r, c, val)
        cell.font = Font(bold=is_bold)
        if (r, c) in {(4, 2), (4, 5), (4, 7), (5, 2), (5, 7)}:
            cell.fill = input_fill
        if (r, c) in {(4, 5), (4, 7)}:
            cell.number_format = "yyyy-mm-dd"
        if (r, c) == (5, 5):
            cell.font = Font(bold=True, color="991B1B")
            cell.number_format = "#,##0"
        if (r, c) == (5, 7):
            cell.number_format = "$#,##0"

    headers = [
        "Code", "OLDCARTS Dimension", "Clinical Question Applied to Deal",
        "Verified Fact (Step 1 Primary Sources Only)", "Step 1 Artifact Citation",
        "Verification Status", "Explicit UNVERIFIED Gap / Unknown"
    ]
    for idx, h in enumerate(headers, start=1):
        c = ws.cell(7, idx, h)
        c.font = Font(bold=True, color="0F172A")
        c.fill = hdr_fill
        c.border = border
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[7].height = 26

    dimensions = [
        ("O", "Onset", "When exactly did the stall begin, and what verified precursor event immediately preceded it?"),
        ("L", "Location", "Where precisely is the deal blocked (internal queue/ticket, CRM stage, or external buyer gate)?"),
        ("D", "Duration", "Exactly how many calendar days have elapsed since stall onset, last internal action, and last buyer contact?"),
        ("C", "Character", "What is the verified nature of the stall (commercial gap, missing sign-off, legal risk, or silent handoff)?"),
        ("A", "Aggravating / Alleviating", "What verified actions worsened the block, and what verified levers could relieve it?"),
        ("R", "Radiation", "Where else is this stall spreading (rev-rec/ASC 606, margin, forecast commit, cash DSO, Q4 slip)?"),
        ("T", "Temporal Pattern", "What is the cadence over time (close-date pushes, approval hop delays, silence windows, hard deadlines)?"),
        ("S", "Severity", "What is the verified financial, margin, contractual, and quarter-close severity?"),
    ]
    for offset, (code, dim, prompt) in enumerate(dimensions, start=8):
        ws.cell(offset, 1, code).alignment = Alignment(horizontal="center", vertical="top")
        ws.cell(offset, 1).font = Font(bold=True, size=11)
        ws.cell(offset, 2, dim).font = Font(bold=True)
        ws.cell(offset, 3, prompt)
        ws.cell(offset, 4, "").fill = input_fill
        ws.cell(offset, 5, "").fill = input_fill
        ws.cell(offset, 6, "UNVERIFIED").fill = input_fill
        ws.cell(offset, 7, "").fill = input_fill
        ws.row_dimensions[offset].height = 46
        for c_i in range(1, 8):
            cell = ws.cell(offset, c_i)
            cell.border = border
            cell.alignment = Alignment(
                horizontal="center" if c_i in {1, 6} else "left",
                vertical="top",
                wrap_text=True
            )

    dv = DataValidation(type="list", formula1='"VERIFIED,PARTIAL - CONTAINS UNVERIFIED,UNVERIFIED"', allow_blank=False)
    ws.add_data_validation(dv)
    dv.add("F8:F15")

    ws["A17"] = "OLDCARTS EVIDENCE INTEGRITY SUMMARY (LIVE FORMULAS)"
    ws["A17"].font = Font(bold=True, size=11)
    summary_rows = [
        (18, "Fully Verified Dimensions (Target = 8 or Explicit Partial)", '=COUNTIF(F8:F15,"VERIFIED")'),
        (19, "Dimensions Containing Explicit Unverified Gaps", '=COUNTIF(F8:F15,"*UNVERIFIED*")'),
        (20, "Populated OLDCARTS Dimensions", '=COUNTA(D8:D15)'),
        (21, "Step 2 Chronology Readiness", '=IF(C20=8,"READY FOR STEP 3 SURGICAL SIEVE","INCOMPLETE — FILL ALL 8 OLDCARTS DIMENSIONS")'),
    ]
    for r, label, formula in summary_rows:
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=2)
        ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=7)
        ws.cell(r, 1, label).font = Font(bold=True)
        ws.cell(r, 3, formula).font = Font(bold=True)
        for c_i in range(1, 8):
            ws.cell(r, c_i).border = border

    for idx, w in enumerate([8, 24, 38, 46, 22, 26, 38], start=1):
        ws.column_dimensions[get_column_letter(idx)].width = w

    # =========================================================================
    # TAB 2: Verified_Timeline_Log
    # =========================================================================
    ws2 = wb.create_sheet("Verified_Timeline_Log")
    ws2.merge_cells("A1:H1")
    ws2["A1"] = "CHRONOLOGICAL DEAL TIMELINE LOG (LIVE ELAPSED-DAY CALCULATOR)"
    ws2["A1"].font = Font(size=13, bold=True, color="FFFFFF")
    ws2["A1"].fill = navy_fill
    ws2.row_dimensions[1].height = 26

    t_headers = [
        "Event #", "Event Date", "Time (ET)", "Days Since Prior Event",
        "Days vs Stall Onset", "Actor / Channel", "Verified Event Description",
        "Step 1 Citation & Verification"
    ]
    for idx, h in enumerate(t_headers, start=1):
        c = ws2.cell(3, idx, h)
        c.font = Font(bold=True)
        c.fill = hdr_fill
        c.border = border
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    for r in range(4, 24):
        ws2.cell(r, 1, f"E-{r-3:02d}").alignment = Alignment(horizontal="center")
        ws2.cell(r, 2, "").number_format = "yyyy-mm-dd"
        ws2.cell(r, 2).fill = input_fill
        ws2.cell(r, 3, "").fill = input_fill
        if r == 4:
            ws2.cell(r, 4, '=IF(ISNUMBER(B4),0,"")')
        else:
            ws2.cell(r, 4, f'=IF(AND(ISNUMBER(B{r}),ISNUMBER(B{r-1})),B{r}-B{r-1},"")')
        ws2.cell(r, 5, f'=IF(AND(ISNUMBER(B{r}),ISNUMBER(OLDCARTS_Matrix!$G$4)),B{r}-OLDCARTS_Matrix!$G$4,"")')
        ws2.cell(r, 4).number_format = "#,##0"
        ws2.cell(r, 5).number_format = "+#,##0;-#,##0;0"
        for c_i in (6, 7, 8):
            ws2.cell(r, c_i, "").fill = input_fill
        for c_i in range(1, 9):
            ws2.cell(r, c_i).border = border
            ws2.cell(r, c_i).alignment = Alignment(
                horizontal="center" if c_i in {1, 2, 3, 4, 5} else "left",
                vertical="top",
                wrap_text=True
            )

    ws2["A25"] = "Total Deal Span (Days)"
    ws2["A25"].font = Font(bold=True)
    ws2["D25"] = '=IF(COUNT(B4:B23)>=2,MAX(B4:B23)-MIN(B4:B23),"")'
    ws2["D25"].font = Font(bold=True)
    ws2["A26"] = "Elapsed Days Since Stall Onset"
    ws2["A26"].font = Font(bold=True)
    ws2["D26"] = '=IF(AND(COUNT(B4:B23)>=1,ISNUMBER(OLDCARTS_Matrix!$G$4)),MAX(B4:B23)-OLDCARTS_Matrix!$G$4,"")'
    ws2["D26"].font = Font(bold=True)

    for idx, w in enumerate([10, 14, 12, 16, 16, 26, 48, 28], start=1):
        ws2.column_dimensions[get_column_letter(idx)].width = w

    out = Path(output_path).resolve()
    wb.save(out)
    print(f"SUCCESS: Built {out}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build blank Step 2 OLDCARTS Chronology Excel template.")
    parser.add_argument("--out", default="step2_tool_oldcarts_chronology_template.xlsx", help="Output .xlsx path")
    args = parser.parse_args()
    build_oldcarts_template(args.out)
