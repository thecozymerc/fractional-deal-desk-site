#!/usr/bin/env python3
"""
Runbook A — Step 4 Reusable Line-by-Line Three-Way Diff Template Builder.
Builds: step4_tool_three_way_diff_template.xlsx
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


def build_three_way_diff_template(output_path: str = "step4_tool_three_way_diff_template.xlsx") -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Three_Way_Diff"

    thin = Side(border_style="thin", color="CBD5E1")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    navy_fill = PatternFill("solid", fgColor="0F172A")
    hdr_fill = PatternFill("solid", fgColor="E2E8F0")
    sub_fill = PatternFill("solid", fgColor="F1F5F9")
    input_fill = PatternFill("solid", fgColor="FFFBEB")

    ws.merge_cells("A1:J1")
    ws["A1"] = "RUNBOOK A — STEP 4: FORENSIC THREE-WAY DIFF (CRM vs QUOTE CALCULATOR vs REDLINED CONTRACT)"
    ws["A1"].font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    ws["A1"].fill = navy_fill
    ws["A1"].alignment = Alignment(horizontal="left", vertical="center")
    ws.row_dimensions[1].height = 28

    ws.merge_cells("A2:J2")
    ws["A2"] = "Rule: Enter exact primary-source values across Columns C, D, and E. Column G automatically computes MATCH vs MISMATCH."
    ws["A2"].font = Font(italic=True, size=10, color="1E293B")
    ws["A2"].fill = sub_fill

    meta = [
        (4, 1, "Account Name:", True), (4, 2, "[Enter Account]", False),
        (4, 4, "CRM Opp ID:", True), (4, 5, "[Enter Opp ID]", False),
        (4, 7, "Diagnostic Date:", True), (4, 8, "[YYYY-MM-DD]", False),
    ]
    for r, c, val, is_bold in meta:
        cell = ws.cell(r, c, val)
        cell.font = Font(bold=is_bold)
        if not is_bold:
            cell.fill = input_fill

    headers = [
        "Diff #", "Commercial / Legal Line Item", "Artifact (a): CRM Record",
        "Artifact (b): Quote Calculator", "Artifact (c): Redlined Contract",
        "Artifact (e): Standard Policy", "3-Way Formula Check",
        "Severity", "Quantified Exposure ($)", "Exact Artifact Citations"
    ]
    for idx, h in enumerate(headers, start=1):
        c = ws.cell(6, idx, h)
        c.font = Font(bold=True, color="0F172A")
        c.fill = hdr_fill
        c.border = border
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[6].height = 26

    default_lines = [
        ("TW-01", "Headline Total Contract Value (TCV)"),
        ("TW-02", "Seat / Unit Ramp Quantities & True-Down Rights"),
        ("TW-03", "Subscription Discretionary Discount %"),
        ("TW-04", "Year-1 ARR vs Headline Average ARR"),
        ("TW-05", "Implementation / Services Fee & List Override"),
        ("TW-06", "Consolidated 3-Year Gross Margin %"),
        ("TW-07", "Contract Term & Custom Opt-Out / T4C Clause"),
        ("TW-08", "Payment Terms & Invoicing Trigger"),
        ("TW-09", "Attached / Governing Quote Version"),
        ("TW-10", "Finance Margin Sign-Off Status"),
        ("TW-11", "VP Sales Approval Status"),
        ("TW-12", "Named Economic Buyer / Authorized Signatory"),
        ("TW-13", "Renewal Uplift Cap & Auto-Renewal"),
        ("TW-14", "Limitation of Liability & Uncapped Carve-Outs"),
        ("TW-15", "SLA Service Credits & Refund Termination Right"),
        ("TW-16", "Most Favored Nation (MFN) Pricing Clause"),
    ]

    for offset, (code, label) in enumerate(default_lines, start=7):
        ws.cell(offset, 1, code).font = Font(bold=True)
        ws.cell(offset, 2, label).font = Font(bold=True)
        for col_i in (3, 4, 5, 6, 10):
            ws.cell(offset, col_i, "").fill = input_fill
        ws.cell(
            offset, 7,
            f'=IF(COUNTA(C{offset}:E{offset})<3,"INCOMPLETE",IF(AND(C{offset}=D{offset},D{offset}=E{offset}),"MATCH","MISMATCH"))'
        ).font = Font(bold=True)
        ws.cell(offset, 8, "HIGH").fill = input_fill
        c_exp = ws.cell(offset, 9, 0)
        c_exp.fill = input_fill
        c_exp.number_format = "$#,##0"
        ws.row_dimensions[offset].height = 36
        for col_i in range(1, 11):
            cell = ws.cell(offset, col_i)
            cell.border = border
            cell.alignment = Alignment(
                horizontal="center" if col_i in {1, 7, 8} else ("right" if col_i == 9 else "left"),
                vertical="top",
                wrap_text=True
            )

    dv_sev = DataValidation(type="list", formula1='"CRITICAL,HIGH,MODERATE,LOW,NONE"', allow_blank=False)
    ws.add_data_validation(dv_sev)
    dv_sev.add("H7:H22")

    ws["A24"] = "THREE-WAY DIFF SUMMARY METRICS (LIVE EXCEL FORMULAS)"
    ws["A24"].font = Font(bold=True, size=11)
    summary = [
        (25, "Total Lines Audited", "=COUNTA(A7:A22)", "#,##0"),
        (26, "Exact 3-Way Matches", '=COUNTIF(G7:G22,"MATCH")', "#,##0"),
        (27, "3-Way Mismatches Detected", '=COUNTIF(G7:G22,"MISMATCH")', "#,##0"),
        (28, "Mismatch Rate (%)", '=IF(D25>0,D27/D25,0)', "0.0%"),
        (29, "Critical Mismatch Lines", '=COUNTIFS(G7:G22,"MISMATCH",H7:H22,"CRITICAL")', "#,##0"),
        (30, "Gross Sum of Line-Item Dollar Exposures (Non-Additive Risk Indicators)", "=SUM(I7:I22)", "$#,##0"),
        (31, "Policy PB-6.1 Three-Way Match Gate", '=IF(D27=0,"PASS — CLEAN 3-WAY MATCH","HARD HOLD — 3-WAY MISMATCH VIOLATES PB-6.1")', "@"),
    ]
    for r, label, formula, nfmt in summary:
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3)
        ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=10)
        ws.cell(r, 1, label).font = Font(bold=True)
        vc = ws.cell(r, 4, formula)
        vc.font = Font(bold=True)
        vc.number_format = nfmt
        for c_i in range(1, 11):
            ws.cell(r, c_i).border = border

    widths = [9, 32, 26, 26, 28, 26, 15, 13, 18, 28]
    for idx, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(idx)].width = w

    out = Path(output_path).resolve()
    wb.save(out)
    print(f"SUCCESS: Built {out}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build blank Step 4 Three-Way Diff Excel template.")
    parser.add_argument("--out", default="step4_tool_three_way_diff_template.xlsx", help="Output .xlsx path")
    args = parser.parse_args()
    build_three_way_diff_template(args.out)
