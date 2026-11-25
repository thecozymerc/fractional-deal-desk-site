#!/usr/bin/env python3
"""
Builds Step 4 Sample 3: step4_sample_kestrel_approval_hop_audit.xlsx
Kestrel Industrial Holdings — Forensic 12-Hop Timestamp Audit & Post-Redline Ball-Holder Attribution
"""

import sys
from datetime import datetime
from pathlib import Path

try:
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter
except ImportError:
    print("ERROR: openpyxl is required. Install with: pip install openpyxl", file=sys.stderr)
    sys.exit(1)


def build_kestrel_hop_audit(output_file: str = "step4_sample_kestrel_approval_hop_audit.xlsx") -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Approval_Hop_Audit"

    thin = Side(border_style="thin", color="CBD5E1")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    navy_fill = PatternFill("solid", fgColor="0F172A")
    hdr_fill = PatternFill("solid", fgColor="E2E8F0")
    sub_fill = PatternFill("solid", fgColor="F1F5F9")
    green_fill = PatternFill("solid", fgColor="DCFCE7")
    amber_fill = PatternFill("solid", fgColor="FEF3C7")
    red_fill = PatternFill("solid", fgColor="FEE2E2")

    ws.merge_cells("A1:J1")
    ws["A1"] = "RUNBOOK A — STEP 4 SAMPLE: KESTREL INDUSTRIAL HOLDINGS — APPROVAL-HOP TIMESTAMP AUDIT"
    ws["A1"].font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    ws["A1"].fill = navy_fill
    ws["A1"].alignment = Alignment(horizontal="left", vertical="center")
    ws.row_dimensions[1].height = 28

    ws.merge_cells("A2:J2")
    ws["A2"] = "Exact timestamps pulled from Artifact (d) (2026-10-28 14:12 ET to 2026-11-25 09:00 ET). Live Excel formulas reconcile 100% of the 19-day post-redline stall."
    ws["A2"].font = Font(italic=True, size=10, color="1E293B")
    ws["A2"].fill = sub_fill

    meta = [
        (4, 1, "Account Name:", True), (4, 2, "Kestrel Industrial Holdings, Inc.", False),
        (4, 4, "CRM Opp ID:", True), (4, 5, "OPP-2026-4819", False),
        (4, 7, "Diagnostic Pull (ET):", True), (4, 8, datetime(2026, 11, 25, 9, 0), False),
    ]
    for r, c, val, is_bold in meta:
        cell = ws.cell(r, c, val)
        cell.font = Font(bold=is_bold)
        if (r, c) == (4, 8):
            cell.number_format = "yyyy-mm-dd hh:mm"

    headers = [
        "Hop #", "Phase", "Start Timestamp (ET)", "End Timestamp (ET)",
        "Elapsed Clock Hours", "Elapsed Days", "% of Post-Redline Stall",
        "Ball Holder (Owner)", "Verified Hop Event Description", "Artifact (d) Line"
    ]
    for idx, h in enumerate(headers, start=1):
        c = ws.cell(6, idx, h)
        c.font = Font(bold=True)
        c.fill = hdr_fill
        c.border = border
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[6].height = 26

    # 12 Exact Hops (Rows 7-18): 4 Pre-Redline + 8 Post-Redline (Reconciling Exact 454.8 hrs / 18.95 days -> 19-day stall)
    hops = [
        ("H-01", "PRE-REDLINE", datetime(2026, 10, 28, 14, 12), datetime(2026, 10, 30, 11, 5), "AE (Jordan Reyes)", "Derek requests <=$240K ramp, Net-60 & CFO exit -> AE sends Quote v2 ($264K / 20%) & logs 20% in CRM.", "d:T001-017"),
        ("H-02", "PRE-REDLINE", datetime(2026, 10, 30, 11, 5), datetime(2026, 11, 3, 16, 40), "AE (Jordan Reyes)", "AE creates unapproved offline Quote v4 ($240K, 28% sub, $24K impl override, Net-60) & emails externally without Desk/CRM sync.", "d:T010-026"),
        ("H-03", "PRE-REDLINE", datetime(2026, 11, 4, 9, 22), datetime(2026, 11, 4, 9, 38), "VP Sales (Marcus Vance)", "Casual 16-min verbal Slack DM nod on '$240K 3-yr ramp' without viewing 28% disc, 70.8% GM, or opt-out (invalid under PB-4.3).", "d:T027-038"),
        ("H-04", "PRE-REDLINE", datetime(2026, 11, 3, 16, 40), datetime(2026, 11, 6, 10, 14), "Buyer Legal (Nadia Benali)", "Kestrel GC turns full redlines (OF-2026-4819-v3) in 2.7 calendar days — disproving 'slow buyer legal.' Discloses CFO Cho has not approved budget.", "d:T018,T039-050"),
        ("H-05", "POST-REDLINE", datetime(2026, 11, 6, 10, 14), datetime(2026, 11, 6, 14, 42), "AE (Jordan Reyes)", "STALL ONSET: AE holds returned redline 4.5 hours before posting Ticket DD-8842 to Slack #deal-desk-approvals.", "d:T039-055"),
        ("H-06", "POST-REDLINE", datetime(2026, 11, 6, 14, 42), datetime(2026, 11, 6, 16, 18), "Seller Legal (Tessa Morales)", "Senior Counsel triages redline in 1.6 hours; places Legal HOLD citing opt-out, Net-60 acceptance, 3x cap & 28% disc; routes to Deal Desk.", "d:T051-061"),
        ("H-07", "POST-REDLINE", datetime(2026, 11, 6, 16, 18), datetime(2026, 11, 9, 9, 5), "Deal Desk (Priyesh Patel)", "Deal Desk audits over weekend (1 business day / 64.8 clock hrs); places HARD HOLD for 5 breaches; directs AE to fix CRM & submit Finance Margin Exception.", "d:T056-076"),
        ("H-08", "POST-REDLINE", datetime(2026, 11, 9, 9, 5), datetime(2026, 11, 12, 17, 10), "AE (Jordan Reyes)", "UNWORKED HOLD WINDOW #1: 80.1 hours (3.3 days) of ZERO AE action until Deal Desk sends Nov 12 bump.", "d:T062-080"),
        ("H-09", "POST-REDLINE", datetime(2026, 11, 12, 17, 10), datetime(2026, 11, 16, 11, 30), "AE (Jordan Reyes)", "UNWORKED HOLD WINDOW #2: 90.3 hours (3.8 days) of ZERO AE action until buyer champion Derek Halvorsen chases status for Dec 2 CFO docket.", "d:T077-088"),
        ("H-10", "POST-REDLINE", datetime(2026, 11, 16, 11, 30), datetime(2026, 11, 18, 8, 45), "AE (Jordan Reyes)", "UNWORKED HOLD WINDOW #3: 45.3 hours (1.9 days) of ZERO Finance submission; AE attempts 2nd VP Slack DM bypass calling Desk 'bureaucratic.'", "d:T081-092"),
        ("H-11", "POST-REDLINE", datetime(2026, 11, 18, 8, 45), datetime(2026, 11, 18, 8, 52), "VP Sales (Marcus Vance)", "7-minute Slack DM reply: 'still support Kestrel at $240K if Finance clears it, just get Desk what they need.' Still zero margin view.", "d:T089-098"),
        ("H-12", "POST-REDLINE", datetime(2026, 11, 18, 8, 52), datetime(2026, 11, 25, 9, 0), "AE (Jordan Reyes)", "UNWORKED HOLD WINDOW #4: 168.1 hours (7.0 days) of ZERO Finance packet, ZERO CRM fix, ZERO buyer response through Nov 25 Audit Pull.", "d:T093-104"),
    ]

    for offset, (hid, phase, ts_st, ts_en, owner, desc, cite) in enumerate(hops, start=7):
        ws.cell(offset, 1, hid).font = Font(bold=True)
        ws.cell(offset, 2, phase).font = Font(bold=(phase == "POST-REDLINE"))
        c_st = ws.cell(offset, 3, ts_st)
        c_en = ws.cell(offset, 4, ts_en)
        c_st.number_format = "yyyy-mm-dd hh:mm"
        c_en.number_format = "yyyy-mm-dd hh:mm"
        c_hr = ws.cell(offset, 5, f"=(D{offset}-C{offset})*24")
        c_hr.number_format = "0.0"
        c_dy = ws.cell(offset, 6, f"=D{offset}-C{offset}")
        c_dy.number_format = "0.00"
        c_sh = ws.cell(offset, 7, f'=IF(B{offset}="POST-REDLINE",E{offset}/$E$19,0)')
        c_sh.number_format = "0.0%"
        ws.cell(offset, 8, owner).font = Font(bold=("AE" in owner and phase == "POST-REDLINE"))
        ws.cell(offset, 9, desc)
        ws.cell(offset, 10, cite)

        if phase == "POST-REDLINE" and "AE" in owner and hid in {"H-08", "H-09", "H-10", "H-12"}:
            for col_i in range(1, 11):
                ws.cell(offset, col_i).fill = red_fill
        elif phase == "PRE-REDLINE" and "Buyer Legal" in owner:
            for col_i in range(1, 11):
                ws.cell(offset, col_i).fill = green_fill

        ws.row_dimensions[offset].height = 44
        for col_i in range(1, 11):
            cell = ws.cell(offset, col_i)
            cell.border = border
            cell.alignment = Alignment(
                horizontal="center" if col_i <= 7 else "left",
                vertical="top",
                wrap_text=True
            )

    # Row 19: Total Post-Redline Stall Window
    ws.merge_cells("A19:D19")
    ws["A19"] = "TOTAL POST-REDLINE STALL WINDOW (NOV 6 10:14 ET TO NOV 25 09:00 ET)"
    ws["E19"] = '=SUMIF(B7:B18,"POST-REDLINE",E7:E18)'
    ws["E19"].number_format = "0.0"
    ws["F19"] = '=SUMIF(B7:B18,"POST-REDLINE",F7:F18)'
    ws["F19"].number_format = "0.00"
    ws["G19"] = '=SUMIF(B7:B18,"POST-REDLINE",G7:G18)'
    ws["G19"].number_format = "0.0%"
    ws.merge_cells("H19:J19")
    ws["H19"] = "454.8 exact clock hours = 18.95 exact days (19 calendar days post-redline)"
    for c_i in range(1, 11):
        ws.cell(19, c_i).font = Font(bold=True, color="991B1B" if c_i in {5, 6, 7} else "0F172A")
        ws.cell(19, c_i).fill = hdr_fill
        ws.cell(19, c_i).border = border

    # Rows 21-29: Ball-Holder Attribution Table (Live SUMIFS)
    ws["A21"] = "POST-REDLINE STALL ATTRIBUTION BY BALL HOLDER (LIVE SUMIFS — PROVES WHO CAUSED THE 19-DAY STALL)"
    ws["A21"].font = Font(bold=True, size=11)
    attr_hdr = ["Ball Holder Category", "Post-Redline Hours", "Post-Redline Days", "% of 19-Day Stall", "Forensic Audit Conclusion"]
    ws.merge_cells("E22:J22")
    for idx, h in enumerate(attr_hdr, start=1):
        c = ws.cell(22, idx, h)
        c.font = Font(bold=True)
        c.fill = hdr_fill
        c.border = border
    for c_i in range(5, 11):
        ws.cell(22, c_i).fill = hdr_fill
        ws.cell(22, c_i).border = border

    holders = [
        ("AE (Jordan Reyes)", "PRIMARY STALL OWNER (85.4%): 4.5h initial routing + 383.8h (16.0 days) ignoring Deal Desk HARD HOLD DD-8842.", red_fill),
        ("Deal Desk (Priyesh Patel)", "WITHIN SLA (14.2%): 64.8 clock hrs over Fri–Mon weekend = ~1 business day to complete 5-point audit & issue HARD HOLD.", amber_fill),
        ("Seller Legal (Tessa Morales)", "FAST TRIAGE (0.4%): 1.6 hours to spot opt-out, Net-60 acceptance, 3x cap & 28% discount and route to Desk.", green_fill),
        ("VP Sales (Marcus Vance)", "MINIMAL (0.03%): 7-minute DM reply on Nov 18; never shown P&L or asked for written exception.", green_fill),
        ("Finance (Elena Rostova)", "NEVER ROUTED (0.0%): 0.0 hours held because AE never submitted a Tier-4 Margin Exception packet (d:T102).", amber_fill),
        ("Buyer Legal (Nadia Benali)", "FALSIFIES AE STORY (0.0%): 0.0 hours held post-redline! Turned redlines in 2.7 days pre-stall; buyer chased Seller Nov 16.", green_fill),
    ]
    for idx, (h_name, concl, fill) in enumerate(holders, start=23):
        ws.merge_cells(start_row=idx, start_column=5, end_row=idx, end_column=10)
        ws.cell(idx, 1, h_name).font = Font(bold=True)
        c_h = ws.cell(idx, 2, f'=SUMIFS($E$7:$E$18,$B$7:$B$18,"POST-REDLINE",$H$7:$H$18,A{idx})')
        c_h.number_format = "0.0"
        c_d = ws.cell(idx, 3, f"=B{idx}/24")
        c_d.number_format = "0.00"
        c_p = ws.cell(idx, 4, f"=B{idx}/$E$19")
        c_p.number_format = "0.0%"
        c_p.font = Font(bold=True)
        c_p.fill = fill
        ws.cell(idx, 5, concl)
        ws.row_dimensions[idx].height = 30
        for col_i in range(1, 11):
            ws.cell(idx, col_i).border = border
            if col_i in {2, 3, 4}:
                ws.cell(idx, col_i).alignment = Alignment(horizontal="center", vertical="center")
            else:
                ws.cell(idx, col_i).alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

    ws.merge_cells("E29:J29")
    ws.cell(29, 1, "TOTAL ATTRIBUTED").font = Font(bold=True)
    ws.cell(29, 2, "=SUM(B23:B28)").number_format = "0.0"
    ws.cell(29, 3, "=SUM(C23:C28)").number_format = "0.00"
    ws.cell(29, 4, "=SUM(D23:D28)").number_format = "0.0%"
    ws.cell(29, 5, '=IF(ABS(B29-E19)<0.2,"RECONCILED 100.0% — EXACT AUDIT TRAIL PROVEN","CHECK LABELS")')
    for col_i in range(1, 11):
        ws.cell(29, col_i).font = Font(bold=True)
        ws.cell(29, col_i).fill = sub_fill
        ws.cell(29, col_i).border = border

    widths = [9, 15, 19, 19, 16, 13, 16, 26, 48, 16]
    for idx, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(idx)].width = w

    out = Path(output_file).resolve()
    wb.save(out)
    print(f"SUCCESS: Built {out}")


if __name__ == "__main__":
    build_kestrel_hop_audit()
