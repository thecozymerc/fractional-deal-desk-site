#!/usr/bin/env python3
"""
Runbook A — Step 3 Reusable Surgical Sieve & Prioritized Differential Excel Template Builder.
Builds: step3_tool_q1_block_b_sieve_matrix_template.xlsx
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


def build_step3_template(output_path: str = "step3_tool_q1_block_b_sieve_matrix_template.xlsx") -> None:
    wb = Workbook()

    thin = Side(border_style="thin", color="CBD5E1")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    navy_fill = PatternFill("solid", fgColor="0F172A")
    hdr_fill = PatternFill("solid", fgColor="E2E8F0")
    sub_fill = PatternFill("solid", fgColor="F1F5F9")
    input_fill = PatternFill("solid", fgColor="FFFBEB")

    # =========================================================================
    # TAB 1: QTC_5Bucket_Sieve
    # =========================================================================
    ws = wb.active
    ws.title = "QTC_5Bucket_Sieve"

    ws.merge_cells("A1:I1")
    ws["A1"] = "RUNBOOK A — STEP 3: SURGICAL SIEVE — Q1 BLOCK B (5 QTC BUCKETS BLANK TEMPLATE)"
    ws["A1"].font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    ws["A1"].fill = navy_fill
    ws["A1"].alignment = Alignment(horizontal="left", vertical="center")
    ws.row_dimensions[1].height = 28

    ws.merge_cells("A2:I2")
    ws["A2"] = "Anti-Anchoring Rule: Scan ALL 5 QTC buckets completely before locking Leading Hypothesis, Can't-Miss/ROWS Threat, and 2 Alternatives."
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
        "Code", "Q1 Block B — QTC Bucket", "Scanned? (YES/NO)",
        "Severity (1-5)", "Evidence Strength (1-5)", "Weighted Score",
        "Automated Risk Tier", "Verified Findings (Step 1 Artifacts & Step 2 PR)",
        "Citations & Explicit UNVERIFIED Gaps"
    ]
    for idx, h in enumerate(headers, start=1):
        c = ws.cell(6, idx, h)
        c.font = Font(bold=True, color="0F172A")
        c.fill = hdr_fill
        c.border = border
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[6].height = 26

    buckets = [
        ("B1", "Commercial / Pricing"),
        ("B2", "Governance / Authority"),
        ("B3", "Config / Tools"),
        ("B4", "Paper / Redline"),
        ("B5", "Downstream Billability / Rev-Rec"),
    ]
    for offset, (code, name) in enumerate(buckets, start=7):
        ws.cell(offset, 1, code).font = Font(bold=True)
        ws.cell(offset, 2, name).font = Font(bold=True)
        ws.cell(offset, 3, "NO").fill = input_fill
        ws.cell(offset, 4, 1).fill = input_fill
        ws.cell(offset, 5, 1).fill = input_fill
        ws.cell(offset, 6, f'=IF(C{offset}="YES",D{offset}*E{offset},0)')
        ws.cell(
            offset, 7,
            f'=IF(C{offset}<>"YES","UNSCANNED — VIOLATION",IF(F{offset}>=21,"CRITICAL",IF(F{offset}>=15,"HIGH",IF(F{offset}>=8,"MODERATE","LOW"))))'
        )
        ws.cell(offset, 8, "").fill = input_fill
        ws.cell(offset, 9, "").fill = input_fill
        ws.row_dimensions[offset].height = 54
        for c_i in range(1, 10):
            cell = ws.cell(offset, c_i)
            cell.border = border
            cell.alignment = Alignment(
                horizontal="center" if c_i in {1, 3, 4, 5, 6, 7} else "left",
                vertical="top",
                wrap_text=True
            )

    dv_yn = DataValidation(type="list", formula1='"YES,NO"', allow_blank=False)
    dv_15 = DataValidation(type="list", formula1='"1,2,3,4,5"', allow_blank=False)
    ws.add_data_validation(dv_yn)
    ws.add_data_validation(dv_15)
    dv_yn.add("C7:C11")
    dv_15.add("D7:E11")

    ws["A13"] = "SURGICAL SIEVE COMPLETENESS & ANTI-ANCHORING GATE (LIVE FORMULAS)"
    ws["A13"].font = Font(bold=True, size=11)
    summary = [
        (14, "QTC Buckets Scanned (Target = 5 of 5)", '=COUNTIF(C7:C11,"YES")'),
        (15, "CRITICAL Buckets (>=21 Score)", '=COUNTIF(G7:G11,"CRITICAL")'),
        (16, "Composite Deal Risk Index (Max = 125)", "=SUM(F7:F11)"),
        (17, "Average Bucket Severity (1-5)", '=IF(D14>0,AVERAGE(D7:D11),0)'),
        (18, "Anti-Anchoring Sieve Gate", '=IF(D14=5,"PASS — ALL 5 QTC BUCKETS SCANNED; DIFFERENTIAL UNLOCKED","STOP — SCAN ALL 5 BUCKETS BEFORE HYPOTHESIZING")'),
    ]
    for r, label, formula in summary:
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3)
        ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=9)
        ws.cell(r, 1, label).font = Font(bold=True)
        val_c = ws.cell(r, 4, formula)
        val_c.font = Font(bold=True)
        if r == 17:
            val_c.number_format = "0.0"
        for c_i in range(1, 10):
            ws.cell(r, c_i).border = border

    for idx, w in enumerate([8, 30, 14, 13, 15, 14, 22, 48, 34], start=1):
        ws.column_dimensions[get_column_letter(idx)].width = w

    # =========================================================================
    # TAB 2: Prioritized_Differential
    # =========================================================================
    ws2 = wb.create_sheet("Prioritized_Differential")
    ws2.merge_cells("A1:I1")
    ws2["A1"] = "RUNBOOK A — STEP 3: PRIORITIZED DIFFERENTIAL DIAGNOSIS (BLANK TEMPLATE)"
    ws2["A1"].font = Font(size=13, bold=True, color="FFFFFF")
    ws2["A1"].fill = navy_fill
    ws2.row_dimensions[1].height = 26

    d_headers = [
        "Slot", "Clinical Category", "Hypothesis / Threat Title",
        "QTC Buckets", "Likelihood (1-5)", "Impact (1-5)",
        "Priority Score", "Verified Evidence & Unverified Gaps",
        "Exact Step 4 Forensic Test to Confirm / Falsify"
    ]
    for idx, h in enumerate(d_headers, start=1):
        c = ws2.cell(3, idx, h)
        c.font = Font(bold=True)
        c.fill = hdr_fill
        c.border = border
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    slots = [
        ("D-1", "Leading Hypothesis"),
        ("D-2", "Can't-Miss / ROWS Threat"),
        ("D-3", "Alternative Explanation #1"),
        ("D-4", "Alternative Explanation #2"),
    ]
    for offset, (slot, cat) in enumerate(slots, start=4):
        ws2.cell(offset, 1, slot).font = Font(bold=True)
        ws2.cell(offset, 2, cat).font = Font(bold=True)
        for c_i in (3, 4, 8, 9):
            ws2.cell(offset, c_i, "").fill = input_fill
        ws2.cell(offset, 5, 3).fill = input_fill
        ws2.cell(offset, 6, 3).fill = input_fill
        ws2.cell(offset, 7, f"=E{offset}*F{offset}").font = Font(bold=True)
        ws2.row_dimensions[offset].height = 68
        for c_i in range(1, 10):
            cell = ws2.cell(offset, c_i)
            cell.border = border
            cell.alignment = Alignment(
                horizontal="center" if c_i in {1, 4, 5, 6, 7} else "left",
                vertical="top",
                wrap_text=True
            )

    dv_d15 = DataValidation(type="list", formula1='"1,2,3,4,5"', allow_blank=False)
    ws2.add_data_validation(dv_d15)
    dv_d15.add("E4:F7")

    ws2["A9"] = "STEP 3 DIFFERENTIAL READINESS GATE (CROSS-TAB LIVE FORMULAS)"
    ws2["A9"].font = Font(bold=True, size=11)
    checks = [
        (10, "Leading Hypothesis Populated (D-1)", '=IF(COUNTA(C4,H4,I4)=3,"YES","NO")'),
        (11, "Can't-Miss / ROWS Threat Populated (D-2)", '=IF(COUNTA(C5,H5,I5)=3,"YES","NO")'),
        (12, "2 Alternative Explanations Populated (D-3 & D-4)", '=IF(AND(COUNTA(C6,H6,I6)=3,COUNTA(C7,H7,I7)=3),"YES","NO")'),
        (13, "Step 3 Overall Gate Verdict", '=IF(AND(QTC_5Bucket_Sieve!D14=5,C10="YES",C11="YES",C12="YES"),"GREEN — READY FOR STEP 4 FORENSIC VERIFICATION","RED — COMPLETE ALL 5 BUCKETS AND ALL 4 DIFFERENTIAL SLOTS")'),
    ]
    for r, label, formula in checks:
        ws2.merge_cells(start_row=r, start_column=1, end_row=r, end_column=2)
        ws2.merge_cells(start_row=r, start_column=3, end_row=r, end_column=9)
        ws2.cell(r, 1, label).font = Font(bold=True)
        ws2.cell(r, 3, formula).font = Font(bold=True)
        for c_i in range(1, 10):
            ws2.cell(r, c_i).border = border

    for idx, w in enumerate([8, 24, 34, 14, 14, 12, 14, 48, 42], start=1):
        ws2.column_dimensions[get_column_letter(idx)].width = w

    out = Path(output_path).resolve()
    wb.save(out)
    print(f"SUCCESS: Built {out}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build blank Step 3 Surgical Sieve Excel template.")
    parser.add_argument("--out", default="step3_tool_q1_block_b_sieve_matrix_template.xlsx", help="Output .xlsx path")
    args = parser.parse_args()
    build_step3_template(args.out)
