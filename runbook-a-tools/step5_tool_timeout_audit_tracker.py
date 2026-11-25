#!/usr/bin/env python3
"""
Runbook A — Step 5 Reusable Diagnostic Time-Out & Claim-to-Evidence Gate Excel Template Builder.
Builds: step5_tool_timeout_audit_tracker_template.xlsx
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


def build_step5_template(output_path: str = "step5_tool_timeout_audit_tracker_template.xlsx") -> None:
    wb = Workbook()

    thin = Side(border_style="thin", color="CBD5E1")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    navy_fill = PatternFill("solid", fgColor="0F172A")
    hdr_fill = PatternFill("solid", fgColor="E2E8F0")
    sub_fill = PatternFill("solid", fgColor="F1F5F9")
    input_fill = PatternFill("solid", fgColor="FFFBEB")

    # =========================================================================
    # TAB 1: Ely_Graber_TWED_Gate
    # =========================================================================
    ws = wb.active
    ws.title = "Ely_Graber_TWED_Gate"

    ws.merge_cells("A1:H1")
    ws["A1"] = "RUNBOOK A — STEP 5: MANDATORY DIAGNOSTIC TIME-OUT (ELY / GRABER / TWED BLANK TEMPLATE)"
    ws["A1"].font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    ws["A1"].fill = navy_fill
    ws["A1"].alignment = Alignment(horizontal="left", vertical="center")
    ws.row_dimensions[1].height = 28

    ws.merge_cells("A2:H2")
    ws["A2"] = "Hard Gate Rule: Zero FAIL - BLOCKING controls and zero BLOCKED Step 6 claims permitted before releasing Step 6 SNAPPS Readout."
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
        "Code", "Framework", "Clinical Safety Check / Debiasing Prompt",
        "Gate Status", "Test Result Against Step 3 & Step 4 Findings",
        "Step 1–4 Citation", "Catch Flagged?", "Mandatory Step 6 Correction / Guardrail"
    ]
    for idx, h in enumerate(headers, start=1):
        c = ws.cell(6, idx, h)
        c.font = Font(bold=True)
        c.fill = hdr_fill
        c.border = border
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[6].height = 26

    controls = [
        ("ELY-1", "Ely Time-Out", "Reviewed all 5 raw primary-source artifacts before accepting AE framing?"),
        ("ELY-2", "Ely Time-Out", "Does Leading Hypothesis explain ALL verified data points cleanly?"),
        ("ELY-3", "Ely Time-Out", "Can't-Miss / ROWS worst-case post-signature threat quantified?"),
        ("ELY-4", "Ely Time-Out", "Disconfirming evidence actively hunted against both buyer and seller stories?"),
        ("ELY-5", "Ely Time-Out", "All unverified unknowns explicitly quarantined from verified facts?"),
        ("GRB-C1", "Graber — Cognitive", "Anchoring Bias checked (rejected AE's opening story)?"),
        ("GRB-C2", "Graber — Cognitive", "Premature Closure checked (all 5 QTC buckets + 51 flags audited)?"),
        ("GRB-C3", "Graber — Cognitive", "Confirmation Bias checked (active falsification performed)?"),
        ("GRB-C4", "Graber — Cognitive", "Framing Effect checked (headline value / Q4 urgency stripped)?"),
        ("GRB-C5", "Graber — Cognitive", "Attribution Bias checked (systemic controls separated from individual error)?"),
        ("GRB-C6", "Graber — Cognitive", "Search Satisficing checked (every approval hop timestamp audited)?"),
        ("GRB-S1", "Graber — System", "Missing/unreviewed artifacts (base MSA, SOW) flagged as explicit scope limits?"),
        ("GRB-S2", "Graber — System", "Every stalled handoff tied to a named owner and exact elapsed hours?"),
        ("GRB-S3", "Graber — System", "False-green automated CRM/CPQ approvals detected and documented?"),
        ("GRB-S4", "Graber — System", "Client diagnostic ownership preserved cleanly?"),
        ("TWED-T", "TWED Check", "T (Threat): What blows up post-signature if this deal closes as written?"),
        ("TWED-W", "TWED Check", "W (What else?): Did I accept the AE's framing? What else explains the stall?"),
        ("TWED-E", "TWED Check", "E (Evidence): Does every finding tie to a specific document line or timestamp?"),
        ("TWED-D", "TWED Check", "D (Dispositional): Am I getting sucked into rescuing instead of diagnosing?"),
    ]
    for offset, (code, fw, prompt) in enumerate(controls, start=7):
        ws.cell(offset, 1, code).font = Font(bold=True)
        ws.cell(offset, 2, fw).font = Font(bold=("TWED" in fw))
        ws.cell(offset, 3, prompt)
        ws.cell(offset, 4, "FAIL - BLOCKING").fill = input_fill
        for col_i in (5, 6, 8):
            ws.cell(offset, col_i, "").fill = input_fill
        ws.cell(offset, 7, f'=IF(LEFT(D{offset},4)="FAIL","YES","NO")').font = Font(bold=True)
        ws.row_dimensions[offset].height = 38
        for col_i in range(1, 9):
            cell = ws.cell(offset, col_i)
            cell.border = border
            cell.alignment = Alignment(
                horizontal="center" if col_i in {1, 4, 7} else "left",
                vertical="top",
                wrap_text=True
            )

    dv_st = DataValidation(type="list", formula1='"PASS,FAIL - REMEDIATED,FAIL - BLOCKING"', allow_blank=False)
    ws.add_data_validation(dv_st)
    dv_st.add("D7:D25")

    ws["A27"] = "STEP 5 DIAGNOSTIC TIME-OUT RELEASE GATE (LIVE CROSS-TAB FORMULAS)"
    ws["A27"].font = Font(bold=True, size=11)
    summary = [
        (28, "Total Ely / Graber / TWED Controls Evaluated", "=COUNTA(A7:A25)"),
        (29, "Clean PASS Controls", '=COUNTIF(D7:D25,"PASS")'),
        (30, "Time-Out Failures Caught & Remediated", '=COUNTIF(D7:D25,"FAIL - REMEDIATED")'),
        (31, "Unresolved FAIL - BLOCKING Controls (Must = 0)", '=COUNTIF(D7:D25,"FAIL - BLOCKING")'),
        (32, "Candidate Step 6 Claims Caught by Raw Audit (Tab 2)", '=COUNTIF(Readout_Claim_Audit!F5:F16,"FAIL*")'),
        (33, "Unresolved BLOCKED Claims on Tab 2 (Must = 0)", '=COUNTIF(Readout_Claim_Audit!G5:G16,"BLOCKED*")'),
        (34, "Step 5 Readout Release Gate Verdict", '=IF(AND(D31=0,D33=0),"GREEN — TIME-OUT CLEARED; AUTHORIZED FOR STEP 6 SNAPPS READOUT","RED — HARD STOP: REMEDIATE BLOCKING FAILURES BEFORE STEP 6")'),
    ]
    for r, label, formula in summary:
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3)
        ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=8)
        ws.cell(r, 1, label).font = Font(bold=True)
        ws.cell(r, 4, formula).font = Font(bold=True)
        for c_i in range(1, 9):
            ws.cell(r, c_i).border = border

    for idx, w in enumerate([10, 20, 40, 20, 42, 22, 14, 40], start=1):
        ws.column_dimensions[get_column_letter(idx)].width = w

    # =========================================================================
    # TAB 2: Readout_Claim_Audit
    # =========================================================================
    ws2 = wb.create_sheet("Readout_Claim_Audit")
    ws2.merge_cells("A1:H1")
    ws2["A1"] = "STEP 5 PRE-READOUT CLAIM-TO-EVIDENCE AUDIT (TWED 'E' & 'D' GUARDRAIL)"
    ws2["A1"].font = Font(size=13, bold=True, color="FFFFFF")
    ws2["A1"].fill = navy_fill
    ws2.row_dimensions[1].height = 26

    ws2.merge_cells("A2:H2")
    ws2["A2"] = "Every statement proposed for Step 6 must pass Line/Timestamp Citation, Non-Additive Math/Scope Check, and No-Rescue Boundary."
    ws2["A2"].font = Font(italic=True, size=10, color="1E293B")
    ws2["A2"].fill = sub_fill

    c_hdr = [
        "ID", "Candidate Step 6 Readout Statement", "Line/Timestamp Cited?",
        "Math & Scope Valid?", "No-Rescue / Non-Blame?", "Raw Audit Result",
        "Final Disposition", "Approved Step 6 Wording / Strip Reason"
    ]
    for idx, h in enumerate(c_hdr, start=1):
        c = ws2.cell(4, idx, h)
        c.font = Font(bold=True)
        c.fill = hdr_fill
        c.border = border
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    for offset in range(5, 17):
        ws2.cell(offset, 1, f"R-{offset-4:02d}").font = Font(bold=True)
        ws2.cell(offset, 2, "").fill = input_fill
        for col_i in (3, 4, 5):
            ws2.cell(offset, col_i, "NO").fill = input_fill
        ws2.cell(offset, 6, f'=IF(B{offset}="","",IF(AND(C{offset}="YES",D{offset}="YES",E{offset}="YES"),"PASS","FAIL — CAUGHT BY TIME-OUT"))').font = Font(bold=True)
        ws2.cell(offset, 7, "BLOCKED").fill = input_fill
        ws2.cell(offset, 8, "").fill = input_fill
        ws2.row_dimensions[offset].height = 36
        for col_i in range(1, 9):
            cell = ws2.cell(offset, col_i)
            cell.border = border
            cell.alignment = Alignment(
                horizontal="center" if col_i in {1, 3, 4, 5, 6, 7} else "left",
                vertical="top",
                wrap_text=True
            )

    dv_yn = DataValidation(type="list", formula1='"YES,NO"', allow_blank=False)
    dv_dp = DataValidation(type="list", formula1='"CLEARED FOR STEP 6,REMEDIATED — REWRITTEN/STRIPPED,BLOCKED — UNRESOLVED"', allow_blank=False)
    ws2.add_data_validation(dv_yn)
    ws2.add_data_validation(dv_dp)
    dv_yn.add("C5:E16")
    dv_dp.add("G5:G16")

    for idx, w in enumerate([8, 42, 16, 16, 18, 24, 28, 44], start=1):
        ws2.column_dimensions[get_column_letter(idx)].width = w

    out = Path(output_path).resolve()
    wb.save(out)
    print(f"SUCCESS: Built {out}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build blank Step 5 Diagnostic Time-Out Excel template.")
    parser.add_argument("--out", default="step5_tool_timeout_audit_tracker_template.xlsx", help="Output .xlsx path")
    args = parser.parse_args()
    build_step5_template(args.out)
