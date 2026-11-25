#!/usr/bin/env python3
"""
Runbook A — Step 6 Reusable MESO Structural Options Calculator & 5-Deal Diagnostic Bridge Tracker Builder.
Builds: step6_tool_meso_options_calculator_template.xlsx
"""

import argparse
import sys
from pathlib import Path

try:
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter
except ImportError:
    print("ERROR: openpyxl is required. Install with: pip install openpyxl", file=sys.stderr)
    sys.exit(1)


def build_step6_template(output_path: str = "step6_tool_meso_options_calculator_template.xlsx") -> None:
    wb = Workbook()

    thin = Side(border_style="thin", color="CBD5E1")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    navy_fill = PatternFill("solid", fgColor="0F172A")
    hdr_fill = PatternFill("solid", fgColor="E2E8F0")
    sub_fill = PatternFill("solid", fgColor="F1F5F9")
    input_fill = PatternFill("solid", fgColor="FFFBEB")

    # =========================================================================
    # TAB 1: MESO_Options_Model
    # =========================================================================
    ws = wb.active
    ws.title = "MESO_Options_Model"

    ws.merge_cells("A1:G1")
    ws["A1"] = "RUNBOOK A — STEP 6: CLEAN-BOUNDARY MESO STRUCTURAL OPTIONS CALCULATOR (BLANK TEMPLATE)"
    ws["A1"].font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    ws["A1"].fill = navy_fill
    ws["A1"].alignment = Alignment(horizontal="left", vertical="center")
    ws.row_dimensions[1].height = 28

    ws.merge_cells("A2:G2")
    ws["A2"] = "Beat 3 No-Rescue Tool: Model 3 client-owned MESO structural packages + Controlled Deferral side-by-side against Current Redline."
    ws["A2"].font = Font(italic=True, size=10, color="1E293B")
    ws["A2"].fill = sub_fill

    ws["A4"] = "Policy GM Floor %:"
    ws["A4"].font = Font(bold=True)
    ws["B4"] = 0.75
    ws["B4"].number_format = "0.0%"
    ws["B4"].fill = input_fill
    ws["C4"] = "Upfront Commission %:"
    ws["C4"].font = Font(bold=True)
    ws["D4"] = 0.10
    ws["D4"].number_format = "0.0%"
    ws["D4"].fill = input_fill
    ws["E4"] = "Account Name:"
    ws["E4"].font = Font(bold=True)
    ws["F4"] = "[Enter Account]"
    ws["F4"].fill = input_fill

    headers = [
        "Commercial / Financial Metric",
        "Current Redline (Baseline)",
        "MESO Option A (Committed)",
        "MESO Option B (Protected Exit)",
        "MESO Option C (12-Mo Pilot)",
        "Option D (De-Commit / Defer)",
        "Governance / Audit Note"
    ]
    for idx, h in enumerate(headers, start=1):
        c = ws.cell(6, idx, h)
        c.font = Font(bold=True)
        c.fill = hdr_fill
        c.border = border
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[6].height = 28

    rows_spec = [
        (7, "Subscription List Price ($)", "input", "$#,##0", "Standard price book subscription baseline"),
        (8, "Subscription Discount (%)", "input", "0.0%", "Discretionary discount tier"),
        (9, "Net Subscription Revenue ($)", "formula", "$#,##0", "={col}7*(1-{col}8)"),
        (10, "Implementation / Services Fee ($)", "input", "$#,##0", "Must match PB-1.3 unless Finance exception"),
        (11, "Headline Contract Value — TCV ($)", "formula", "$#,##0", "={col}9+{col}10"),
        (12, "Direct Subscription COGS ($)", "input", "$#,##0", "Hosting + support direct cost"),
        (13, "Direct Implementation COGS ($)", "input", "$#,##0", "Delivery direct cost (incl. custom ERP)"),
        (14, "Total Direct COGS ($)", "formula", "$#,##0", "={col}12+{col}13"),
        (15, "Consolidated Gross Profit ($)", "formula", "$#,##0", "={col}11-{col}14"),
        (16, "Consolidated Gross Margin (%)", "formula", "0.0%", '=IF({col}11>0,{col}15/{col}11,0)'),
        (17, "Variance vs Policy GM Floor ($)", "formula", "$#,##0;($#,##0);$0", '=IF({col}11>0,{col}15-({col}11*$B$4),0)'),
        (18, "ASC 606 Enforceable TCV ($)", "input", "$#,##0", "Non-cancellable committed revenue under ASC 606"),
        (19, "Unenforceable / At-Risk TCV ($)", "formula", "$#,##0", "={col}11-{col}18"),
        (20, "Year-1 Enforceable Revenue ($)", "input", "$#,##0", "Year-1 subscription + Year-1 services"),
        (21, "Year-1 Direct COGS ($)", "input", "$#,##0", "Year-1 seats COGS + Year-1 services COGS"),
        (22, "Commissionable Bookings Base ($)", "input", "$#,##0", "TCV or enforceable revenue per commission plan"),
        (23, "Upfront Sales Commission ($)", "formula", "$#,##0", "={col}22*$D$4"),
        (24, "Year-1 Net Contribution After Commission ($)", "formula", "$#,##0;($#,##0);$0", "={col}20-{col}21-{col}23"),
        (25, "Committed Net Contribution After Comm ($)", "formula", "$#,##0;($#,##0);$0", '=IF({col}18={col}11,{col}15-{col}23,{col}24)'),
        (26, "Payment Terms & Est. Y1 DSO", "text", "@", "Invoice-dated vs acceptance-gated cash delay"),
        (27, "Legal & Risk Clause Profile", "text", "@", "Liability cap, SLA credits, MFN, SOW"),
        (28, "Written Approvals Required", "text", "@", "Policy authority matrix (Artifact e)"),
        (29, "Automated Margin & Enforceability Gate", "formula", "@", '=IF({col}11=0,"CONTROLLED DEFER",IF(AND({col}16>=$B$4,{col}19=0),"PASS — FLOOR & 606 CLEAN",IF({col}19>0,"CHECK 606 / EXIT PROTECTION","REQUIRES WRITTEN MARGIN EXCEPTION")))'),
    ]

    cols = ["B", "C", "D", "E", "F"]
    for r, label, kind, nfmt, spec in rows_spec:
        ws.cell(r, 1, label).font = Font(bold=(kind == "formula" or r in {11, 18, 29}))
        ws.cell(r, 1).border = border
        for idx, col_let in enumerate(cols, start=2):
            cell = ws.cell(r, idx)
            if kind == "formula":
                cell.value = spec.format(col=col_let)
                cell.font = Font(bold=True)
                cell.fill = sub_fill
            elif kind == "input":
                cell.value = 0
                cell.fill = input_fill
            else:
                cell.value = ""
                cell.fill = input_fill
            cell.number_format = nfmt
            cell.border = border
            cell.alignment = Alignment(horizontal="right" if nfmt != "@" else "left", vertical="center", wrap_text=True)
        note_c = ws.cell(r, 7, spec if kind != "formula" else "Calculated automatically")
        note_c.border = border
        note_c.alignment = Alignment(wrap_text=True, vertical="center")
        ws.row_dimensions[r].height = 28 if kind == "text" or r == 29 else 22

    for idx, w in enumerate([38, 22, 22, 22, 22, 22, 34], start=1):
        ws.column_dimensions[get_column_letter(idx)].width = w

    # =========================================================================
    # TAB 2: Slot1_to_5Deal_Bridge_Tracker
    # =========================================================================
    ws2 = wb.create_sheet("Slot1_to_5Deal_Bridge_Tracker")
    ws2.merge_cells("A1:H1")
    ws2["A1"] = "BEAT 4 COMMERCIAL BRIDGE — 5-DEAL FORENSIC DIAGNOSTIC TRACKER (5 BUSINESS DAYS)"
    ws2["A1"].font = Font(size=13, bold=True, color="FFFFFF")
    ws2["A1"].fill = navy_fill
    ws2.row_dimensions[1].height = 26

    ws2.merge_cells("A2:H2")
    ws2["A2"] = "Bridge: Slot #1 proves why one deal broke. Slots #2–#5 prove in 5 business days whether 20–30% of deal flow leaks across identical handoffs."
    ws2["A2"].font = Font(italic=True, size=10, color="1E293B")
    ws2["A2"].fill = sub_fill

    b_hdr = ["Slot #", "Account Name", "Status", "Headline TCV ($)", "True Price Leak ($)", "At-Risk / Unenforceable ($)", "Primary Control / Handoff Failure", "Target Day (1-5)"]
    for idx, h in enumerate(b_hdr, start=1):
        c = ws2.cell(4, idx, h)
        c.font = Font(bold=True)
        c.fill = hdr_fill
        c.border = border
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    for offset in range(5, 10):
        slot_num = offset - 4
        ws2.cell(offset, 1, f"Slot #{slot_num}").font = Font(bold=True)
        ws2.cell(offset, 2, "[Validation Deal]" if slot_num == 1 else "[Select Pipeline Deal]").fill = input_fill
        ws2.cell(offset, 3, "PENDING").fill = input_fill
        for c_i in (4, 5, 6):
            cc = ws2.cell(offset, c_i, 0)
            cc.fill = input_fill
            cc.number_format = "$#,##0"
        ws2.cell(offset, 7, "").fill = input_fill
        ws2.cell(offset, 8, f"Day {slot_num}").alignment = Alignment(horizontal="center")
        for c_i in range(1, 9):
            ws2.cell(offset, c_i).border = border

    ws2.cell(10, 1, "TOTAL").font = Font(bold=True)
    ws2.cell(10, 2, "5-Deal Diagnostic Portfolio Roll-Up").font = Font(bold=True)
    ws2.cell(10, 3, '=COUNTIF(C5:C9,"COMPLETED")&" / 5 Done"').font = Font(bold=True)
    for col_let, c_i in [("D", 4), ("E", 5), ("F", 6)]:
        tot = ws2.cell(10, c_i, f"=SUM({col_let}5:{col_let}9)")
        tot.number_format = "$#,##0"
        tot.font = Font(bold=True)
    ws2.cell(10, 7, "Systemic Leak Rate = (Total Leak + At-Risk) / Total TCV")
    ws2.cell(10, 8, "5 Bus. Days").font = Font(bold=True)
    for c_i in range(1, 9):
        ws2.cell(10, c_i).fill = sub_fill
        ws2.cell(10, c_i).border = border

    ws2.merge_cells("A12:H12")
    ws2["A12"] = "Pricing Governance Note: Neon's suggestion of a $100 validation fee credited toward the 5-deal Forensic Diagnostic is UNRULED / OPTIONAL and NOT part of the ruled price."
    ws2["A12"].font = Font(italic=True, bold=True, color="92400E")

    for idx, w in enumerate([10, 28, 15, 16, 18, 22, 40, 14], start=1):
        ws2.column_dimensions[get_column_letter(idx)].width = w

    out = Path(output_path).resolve()
    wb.save(out)
    print(f"SUCCESS: Built {out}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build blank Step 6 MESO Calculator & 5-Deal Bridge Tracker template.")
    parser.add_argument("--out", default="step6_tool_meso_options_calculator_template.xlsx", help="Output .xlsx path")
    args = parser.parse_args()
    build_step6_template(args.out)
