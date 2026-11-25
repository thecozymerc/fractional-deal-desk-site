#!/usr/bin/env python3
"""
Runbook A — Step 4 Reusable Approval-Hop Timestamp Audit Template Builder.
Builds: step4_tool_approval_hop_audit_template.xlsx
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


def build_hop_audit_template(output_path: str = "step4_tool_approval_hop_audit_template.xlsx") -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Approval_Hop_Audit"

    thin = Side(border_style="thin", color="CBD5E1")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    navy_fill = PatternFill("solid", fgColor="0F172A")
    hdr_fill = PatternFill("solid", fgColor="E2E8F0")
    sub_fill = PatternFill("solid", fgColor="F1F5F9")
    input_fill = PatternFill("solid", fgColor="FFFBEB")

    ws.merge_cells("A1:J1")
    ws["A1"] = "RUNBOOK A — STEP 4: APPROVAL-HOP TIMESTAMP AUDIT (BLANK TEMPLATE)"
    ws["A1"].font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    ws["A1"].fill = navy_fill
    ws["A1"].alignment = Alignment(horizontal="left", vertical="center")
    ws.row_dimensions[1].height = 28

    ws.merge_cells("A2:J2")
    ws["A2"] = "Enter exact timestamps (YYYY-MM-DD HH:MM) from Artifact (d). Formulas automatically compute elapsed hours, days, and % of post-redline stall."
    ws["A2"].font = Font(italic=True, size=10, color="1E293B")
    ws["A2"].fill = sub_fill

    meta = [
        (4, 1, "Account Name:", True), (4, 2, "[Enter Account]", False),
        (4, 4, "CRM Opp ID:", True), (4, 5, "[Enter Opp ID]", False),
        (4, 7, "Diagnostic Pull Timestamp:", True), (4, 8, "[YYYY-MM-DD HH:MM]", False),
    ]
    for r, c, val, is_bold in meta:
        cell = ws.cell(r, c, val)
        cell.font = Font(bold=is_bold)
        if not is_bold:
            cell.fill = input_fill

    headers = [
        "Hop #", "Phase", "Start Timestamp (ET)", "End Timestamp (ET)",
        "Elapsed Clock Hours", "Elapsed Days", "% of Post-Redline Stall",
        "Ball Holder (Owner)", "Hop Event Description", "Artifact (d) Citation"
    ]
    for idx, h in enumerate(headers, start=1):
        c = ws.cell(6, idx, h)
        c.font = Font(bold=True)
        c.fill = hdr_fill
        c.border = border
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[6].height = 26

    # Rows 7-18: 12 Hop Rows
    for offset in range(7, 19):
        ws.cell(offset, 1, f"H-{offset-6:02d}").font = Font(bold=True)
        ws.cell(offset, 2, "POST-REDLINE").fill = input_fill
        c_st = ws.cell(offset, 3, "")
        c_en = ws.cell(offset, 4, "")
        c_st.fill = input_fill
        c_en.fill = input_fill
        c_st.number_format = "yyyy-mm-dd hh:mm"
        c_en.number_format = "yyyy-mm-dd hh:mm"
        c_hr = ws.cell(offset, 5, f'=IF(AND(ISNUMBER(C{offset}),ISNUMBER(D{offset})),(D{offset}-C{offset})*24,0)')
        c_hr.number_format = "0.0"
        c_dy = ws.cell(offset, 6, f'=IF(AND(ISNUMBER(C{offset}),ISNUMBER(D{offset})),D{offset}-C{offset},0)')
        c_dy.number_format = "0.00"
        c_sh = ws.cell(offset, 7, f'=IF(AND(B{offset}="POST-REDLINE",$E$19>0),E{offset}/$E$19,0)')
        c_sh.number_format = "0.0%"
        for col_i in (8, 9, 10):
            ws.cell(offset, col_i, "").fill = input_fill
        for col_i in range(1, 11):
            cell = ws.cell(offset, col_i)
            cell.border = border
            cell.alignment = Alignment(
                horizontal="center" if col_i <= 7 else "left",
                vertical="top",
                wrap_text=True
            )

    dv_ph = DataValidation(type="list", formula1='"PRE-REDLINE,POST-REDLINE"', allow_blank=False)
    ws.add_data_validation(dv_ph)
    dv_ph.add("B7:B18")

    # Row 19: Post-Redline Totals
    ws.merge_cells("A19:D19")
    ws["A19"] = "TOTAL POST-REDLINE STALL WINDOW (LIVE SUMIF)"
    ws["A19"].font = Font(bold=True)
    ws["E19"] = '=SUMIF(B7:B18,"POST-REDLINE",E7:E18)'
    ws["E19"].number_format = "0.0"
    ws["F19"] = '=SUMIF(B7:B18,"POST-REDLINE",F7:F18)'
    ws["F19"].number_format = "0.00"
    ws["G19"] = '=IF(E19>0,SUMIF(B7:B18,"POST-REDLINE",G7:G18),0)'
    ws["G19"].number_format = "0.0%"
    ws.merge_cells("H19:J19")
    ws["H19"] = "Reconciles exact post-redline stall duration across all hops"
    for c_i in range(1, 11):
        ws.cell(19, c_i).font = Font(bold=True)
        ws.cell(19, c_i).fill = hdr_fill
        ws.cell(19, c_i).border = border

    # Rows 21-28: Ball-Holder Attribution Summary
    ws["A21"] = "POST-REDLINE STALL ATTRIBUTION BY BALL HOLDER (LIVE SUMIFS)"
    ws["A21"].font = Font(bold=True, size=11)
    attr_hdr = ["Ball Holder Category", "Post-Redline Hours", "Post-Redline Days", "% of Post-Redline Stall", "SLA / Control Interpretation"]
    for idx, h in enumerate(attr_hdr, start=1):
        c = ws.cell(22, idx, h)
        c.font = Font(bold=True)
        c.fill = hdr_fill
        c.border = border

    holders = [
        ("AE", "Rep routing & unworked hold dead-time"),
        ("Deal Desk", "Commercial / policy audit turnaround"),
        ("Seller Legal", "Contract redline triage turnaround"),
        ("VP Sales", "Executive sales sponsor response"),
        ("Finance", "Margin exception review time"),
        ("Buyer Legal", "Customer counsel turnaround post-redline"),
    ]
    for idx, (h_name, desc) in enumerate(holders, start=23):
        ws.cell(idx, 1, h_name).font = Font(bold=True)
        c_h = ws.cell(idx, 2, f'=SUMIFS($E$7:$E$18,$B$7:$B$18,"POST-REDLINE",$H$7:$H$18,"*"&A{idx}&"*")')
        c_h.number_format = "0.0"
        c_d = ws.cell(idx, 3, f'=B{idx}/24')
        c_d.number_format = "0.00"
        c_p = ws.cell(idx, 4, f'=IF($E$19>0,B{idx}/$E$19,0)')
        c_p.number_format = "0.0%"
        ws.cell(idx, 5, desc)
        for col_i in range(1, 6):
            ws.cell(idx, col_i).border = border

    ws.cell(29, 1, "TOTAL ATTRIBUTED").font = Font(bold=True)
    ws.cell(29, 2, "=SUM(B23:B28)").number_format = "0.0"
    ws.cell(29, 3, "=SUM(C23:C28)").number_format = "0.00"
    ws.cell(29, 4, "=SUM(D23:D28)").number_format = "0.0%"
    ws.cell(29, 5, '=IF(ABS(B29-E19)<0.2,"RECONCILED 100%","CHECK BALL-HOLDER LABELS")')
    for col_i in range(1, 6):
        ws.cell(29, col_i).font = Font(bold=True)
        ws.cell(29, col_i).fill = sub_fill
        ws.cell(29, col_i).border = border

    widths = [9, 15, 19, 19, 16, 13, 16, 24, 42, 18]
    for idx, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(idx)].width = w

    out = Path(output_path).resolve()
    wb.save(out)
    print(f"SUCCESS: Built {out}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build blank Step 4 Approval-Hop Timestamp Audit Excel template.")
    parser.add_argument("--out", default="step4_tool_approval_hop_audit_template.xlsx", help="Output .xlsx path")
    args = parser.parse_args()
    build_hop_audit_template(args.out)
