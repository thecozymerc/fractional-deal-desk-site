#!/usr/bin/env python3
"""
Builds Step 6 Sample 2: step6_sample_kestrel_meso_options_calculator.xlsx
Kestrel Industrial Holdings — Live-Formula MESO Structural Options Model & 5-Deal Diagnostic Slot Tracker
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


def build_kestrel_step6_workbook(output_file: str = "step6_sample_kestrel_meso_options_calculator.xlsx") -> None:
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
    # TAB 1: MESO_Options_Model
    # =========================================================================
    ws = wb.active
    ws.title = "MESO_Options_Model"

    ws.merge_cells("A1:G1")
    ws["A1"] = "RUNBOOK A — STEP 6 SAMPLE: KESTREL INDUSTRIAL HOLDINGS MESO STRUCTURAL OPTIONS MODEL"
    ws["A1"].font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    ws["A1"].fill = navy_fill
    ws["A1"].alignment = Alignment(horizontal="left", vertical="center")
    ws.row_dimensions[1].height = 28

    ws.merge_cells("A2:G2")
    ws["A2"] = "Clean-Boundary Client Options (Step 5 Time-Out Cleared). Compares Redline v3 (DO NOT SIGN) vs 3 MESO Packages + Controlled Q4 De-Commit."
    ws["A2"].font = Font(italic=True, size=10, color="1E293B")
    ws["A2"].fill = sub_fill

    ws["A4"] = "Policy GM Floor %:"
    ws["A4"].font = Font(bold=True)
    ws["B4"] = 0.75
    ws["B4"].number_format = "0.0%"
    ws["C4"] = "Upfront Commission %:"
    ws["C4"].font = Font(bold=True)
    ws["D4"] = 0.10
    ws["D4"].number_format = "0.0%"
    ws["E4"] = "Account / Opp:"
    ws["E4"].font = Font(bold=True)
    ws["F4"] = "Kestrel (OPP-2026-4819)"

    headers = [
        "Commercial / Financial Metric",
        "Current Redline v3\n(DO NOT SIGN)",
        "MESO Option A\n(Keep $240K -> Firm 3-Yr)",
        "MESO Option B\n(Policy Floor + PB-5.3 Exit)",
        "MESO Option C\n(Clean 12-Mo Paid Pilot)",
        "Option D\n(Controlled Q4 De-Commit)",
        "Step 5 Verified Governance & Audit Note"
    ]
    for idx, h in enumerate(headers, start=1):
        c = ws.cell(6, idx, h)
        c.font = Font(bold=True)
        c.fill = hdr_fill
        c.border = border
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[6].height = 32

    rows_data = [
        (7, "Subscription List Price ($)", [300000, 300000, 300000, 75000, 0], "$#,##0", "200 seat-yrs (50/70/80) @ $1,500; Pilot = 50 seats Y1"),
        (8, "Subscription Discretionary Discount (%)", [0.28, 0.28, 0.16, 0.00, 0.00], "0.0%", "Opt A=Tier 4 (28%); Opt B=Tier 2 (16%); Opt C=0% list"),
        (9, "Net Subscription Revenue ($)", ["=B7*(1-B8)", "=C7*(1-C8)", "=D7*(1-D8)", "=E7*(1-E8)", "=F7*(1-F8)"], "$#,##0", "Live formula: List * (1 - Discount %)"),
        (10, "Implementation / ERP Migration Fee ($)", [24000, 24000, 30000, 30000, 0], "$#,##0", "Opt B & C restore PB-1.3 standard $30K list + signed SOW"),
        (11, "Headline Contract Value — TCV ($)", ["=B9+B10", "=C9+C10", "=D9+D10", "=E9+E10", "=F9+F10"], "$#,##0", "Total face value of agreement"),
        (12, "Direct Subscription COGS ($)", [44000, 44000, 44000, 11000, 0], "$#,##0", "$220/seat/yr direct hosting & support COGS (PB-1.1)"),
        (13, "Direct Implementation COGS ($)", [26000, 26000, 26000, 26000, 0], "$#,##0", "$22K base + $4K ERP connector (SOW verification U-4 req'd)"),
        (14, "Total Direct COGS ($)", ["=B12+B13", "=C12+C13", "=D12+D13", "=E12+E13", "=F12+F13"], "$#,##0", "Live total direct delivery cost"),
        (15, "Consolidated Gross Profit ($)", ["=B11-B14", "=C11-C14", "=D11-D14", "=E11-E14", "=F11-F14"], "$#,##0", "Headline TCV minus Direct COGS"),
        (16, "Consolidated Gross Margin (%)", ['=IF(B11>0,B15/B11,0)', '=IF(C11>0,C15/C11,0)', '=IF(D11>0,D15/D11,0)', '=IF(E11>0,E15/E11,0)', '=IF(F11>0,F15/F11,0)'], "0.0%", "Option B = 75.2% (PASSES 75.0% GM Floor!)"),
        (17, "Variance vs 75.0% GM Floor ($)", ['=IF(B11>0,B15-(B11*$B$4),0)', '=IF(C11>0,C15-(C11*$B$4),0)', '=IF(D11>0,D15-(D11*$B$4),0)', '=IF(E11>0,E15-(E11*$B$4),0)', '=IF(F11>0,F15-(F11*$B$4),0)'], "$#,##0;($#,##0);$0", "Opt B = +$500 above floor; Opt C Y1 sub standalone GM = 85.3%"),
        (18, "ASC 606 Enforceable TCV ($)", [78000, 240000, 93000, 105000, 0], "$#,##0", "Redline collapses to $78K; Opt A & C = 100% enforceable; Opt B Y1 = $93K (+$12K clawback)"),
        (19, "Unenforceable / Optional TCV ($)", ["=B11-B18", "=C11-C18", "=D11-D18", "=E11-E18", "=F11-F18"], "$#,##0", "Opt B discloses optional Y2-3 transparently (no false Commit)"),
        (20, "Year-1 Enforceable Revenue ($)", [78000, 78000, 93000, 105000, 0], "$#,##0", "Opt B adds +$12K PB-5.3 list clawback ($105K total) if exit exercised"),
        (21, "Year-1 Direct COGS ($)", [37000, 37000, 37000, 37000, 0], "$#,##0", "$11K (50 Y1 seats) + $26K ERP implementation"),
        (22, "Commissionable Bookings Base ($)", [240000, 240000, 93000, 105000, 0], "$#,##0", "Opt B & C align commission strictly to ASC 606 enforceable base"),
        (23, "Upfront Sales Commission (10%) ($)", ["=B22*$D$4", "=C22*$D$4", "=D22*$D$4", "=E22*$D$4", "=F22*$D$4"], "$#,##0", "Eliminates upfront clawback shock under Opt B & Opt C"),
        (24, "Year-1 Net Contribution After Comm ($)", ["=B20-B21-B23", "=C20-C21-C23", "=D20-D21-D23", "=E20-E21-E23", "=F20-F21-F23"], "$#,##0;($#,##0);$0", "Opt C yields $57,500 Y1 net (3.4x Redline v3's $17,000!)"),
        (25, "Committed Net Contribution After Comm ($)", ['=IF(B18=B11,B15-B23,B24)', '=IF(C18=C11,C15-C23,C24)', '=IF(D18=D11,D15-D23,D24)', '=IF(E18=E11,E15-E23,E24)', '=IF(F18=F11,F15-F23,F24)'], "$#,##0;($#,##0);$0", "Opt A = $146K firm 3-yr net; Opt C = $57.5K clean 1-yr net"),
        (26, "Payment Terms & Est. Y1 Cash DSO", ["Net-60 Post-Accept (~105+d)", "Net-30 Upfront (30d)", "Net-60 Invoice Date (60d)", "Net-45/60 Invoice (45-60d)", "N/A — Re-Qualify"], "@", "All MESO options eliminate subjective acceptance billing gate"),
        (27, "Legal & Risk Clause Profile", ["41/47 Flags (20 CRIT); $720K+Uncapped; MFN", "Standard MSA (1x Cap, No MFN, Signed SOW)", "1x Cap (Opt 2x Sec), PB-5.3 Clawback, No MFN", "Standard MSA (1x Cap, Signed SOW, Y2-3 Opt)", "Audit Base MSA (F35-38) + SOW"], "@", "Base MSA flags F35-38 must still be reviewed pre-signature"),
        (28, "Required Written Approvals", ["BLOCKED — 6 Policy Breaches", "Tier-4 Finance Controller/CFO (U-2) + VP Written", "VP Sales (Tier-2) + Controller (Net-60) + GC/Rev-Rec", "0% Disc Clean + Controller (Net-45/60) + SOW", "CRO / VP RevOps Q4 De-Commit"], "@", "Verbal VP nods prohibited under PB-4.3 across all options"),
        (29, "Automated Policy & Governance Gate", ['=IF(AND(B16<$B$4,B19>0),"REJECT — BREACHES FLOOR & ASC 606","REVIEW")', '=IF(AND(C19=0,C16<$B$4),"VIABLE WITH WRITTEN TIER-4 FINANCE EXCEPTION","CHECK")', '=IF(D16>=$B$4,"VIABLE — PASSES 75% FLOOR (PB-5.3 / NET-60 SIGN-OFF)","CHECK")', '=IF(AND(E8=0,E19=0),"VIABLE — CLEAN 12-MO PILOT (0% DISC; 100% 606)","CHECK")', '"VIABLE — RESTORES Q4 FORECAST INTEGRITY"'], "@", "Client leadership selects; clinician maintains No-Rescue Boundary"),
    ]

    for r, label, vals, nfmt, note in rows_data:
        ws.cell(r, 1, label).font = Font(bold=(r in {11, 15, 16, 17, 18, 24, 25, 29}))
        ws.cell(r, 1).border = border
        for idx, v in enumerate(vals, start=2):
            c = ws.cell(r, idx, v)
            c.number_format = nfmt
            c.border = border
            is_formula = isinstance(v, str) and v.startswith("=")
            c.font = Font(bold=(is_formula or r in {11, 18, 29}))
            c.alignment = Alignment(horizontal="right" if nfmt != "@" else "left", vertical="center", wrap_text=True)
            if r == 29:
                if idx == 2:
                    c.fill = red_fill
                    c.font = Font(bold=True, color="991B1B")
                elif idx in {4, 5, 6}:
                    c.fill = green_fill
                    c.font = Font(bold=True, color="166534")
                else:
                    c.fill = amber_fill
                    c.font = Font(bold=True, color="92400E")
            elif r == 16 and idx == 4:
                c.fill = green_fill
            elif r in {16, 18, 24} and idx == 2:
                c.fill = red_fill
            elif r == 24 and idx == 5:
                c.fill = green_fill
        nc = ws.cell(r, 7, note)
        nc.border = border
        nc.alignment = Alignment(wrap_text=True, vertical="center")
        ws.row_dimensions[r].height = 38 if r in {26, 27, 28, 29} else 22

    for idx, w in enumerate([36, 23, 24, 25, 24, 23, 40], start=1):
        ws.column_dimensions[get_column_letter(idx)].width = w

    # =========================================================================
    # TAB 2: Slot1_to_5Deal_Bridge_Tracker
    # =========================================================================
    ws2 = wb.create_sheet("Slot1_to_5Deal_Bridge_Tracker")
    ws2.merge_cells("A1:H1")
    ws2["A1"] = "BEAT 4 COMMERCIAL BRIDGE — 5-DEAL FORENSIC DIAGNOSTIC TRACKER (SLOT #1 = KESTREL)"
    ws2["A1"].font = Font(size=13, bold=True, color="FFFFFF")
    ws2["A1"].fill = navy_fill
    ws2.row_dimensions[1].height = 26

    ws2.merge_cells("A2:H2")
    ws2["A2"] = "Proves in 5 business days whether Kestrel is an isolated outlier or how 20–30% of enterprise deal flow quietly leaks across handoffs."
    ws2["A2"].font = Font(italic=True, size=10, color="1E293B")
    ws2["A2"].fill = sub_fill

    b_hdr = ["Slot #", "Account / Sampling Criterion", "Status", "Headline TCV ($)", "True Price Leak ($)", "ASC 606 At-Risk ($)", "Primary Control / Handoff Finding", "Delivery Day"]
    for idx, h in enumerate(b_hdr, start=1):
        c = ws2.cell(4, idx, h)
        c.font = Font(bold=True)
        c.fill = hdr_fill
        c.border = border
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    slot_rows = [
        ("Slot #1", "Kestrel Industrial Holdings (OPP-2026-4819)", "COMPLETED", 240000, 90000, 162000, "15/16 CRM mismatch, false-green Finance flag, 85.4% unworked hold, 70.8% GM, Month-12 opt-out, unengaged CFO", "Day 0 (Done)"),
        ("Slot #2", "[Pull] Current Q4 Commit Deal (>$150K)", "PENDING", 0, 0, 0, "Test for false-green CRM approvals & unengaged Economic Buyers in Q4 Commit", "Day 1"),
        ("Slot #3", "[Pull] Current Redline-Stalled Deal (>14d)", "PENDING", 0, 0, 0, "Test whether redline delays sit with buyer legal or silent internal Desk/Finance holds", "Day 2"),
        ("Slot #4", "[Pull] Recently Closed-Won Multi-Year Ramp", "PENDING", 0, 0, 0, "Test whether signed deals leaked sub-75% GM, overwritten impl cells, or opt-outs", "Day 3"),
        ("Slot #5", "[Pull] Recent Closed-Lost Enterprise Deal", "PENDING", 0, 0, 0, "Test whether internal approval lag or misqualified champions drove avoidable loss", "Day 4"),
    ]
    for offset, (sl, acct, st, tcv, leak, risk, note, day) in enumerate(slot_rows, start=5):
        ws2.cell(offset, 1, sl).font = Font(bold=True)
        ws2.cell(offset, 2, acct).font = Font(bold=(sl == "Slot #1"))
        c_st = ws2.cell(offset, 3, st)
        c_st.font = Font(bold=True, color="166534" if st == "COMPLETED" else "92400E")
        c_st.fill = green_fill if st == "COMPLETED" else amber_fill
        for col_i, num in [(4, tcv), (5, leak), (6, risk)]:
            cc = ws2.cell(offset, col_i, num)
            cc.number_format = "$#,##0"
            cc.font = Font(bold=(sl == "Slot #1"))
        ws2.cell(offset, 7, note)
        ws2.cell(offset, 8, day).alignment = Alignment(horizontal="center")
        ws2.row_dimensions[offset].height = 36
        for c_i in range(1, 9):
            ws2.cell(offset, c_i).border = border
            if c_i in {1, 3, 8}:
                ws2.cell(offset, c_i).alignment = Alignment(horizontal="center", vertical="center")
            elif c_i in {4, 5, 6}:
                ws2.cell(offset, c_i).alignment = Alignment(horizontal="right", vertical="center")
            else:
                ws2.cell(offset, c_i).alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

    ws2.cell(10, 1, "TOTAL").font = Font(bold=True)
    ws2.cell(10, 2, "5-Deal Diagnostic Portfolio Roll-Up").font = Font(bold=True)
    ws2.cell(10, 3, '=COUNTIF(C5:C9,"COMPLETED")&" / 5 Done"').font = Font(bold=True)
    for col_let, col_i in [("D", 4), ("E", 5), ("F", 6)]:
        tot = ws2.cell(10, col_i, f"=SUM({col_let}5:{col_let}9)")
        tot.number_format = "$#,##0"
        tot.font = Font(bold=True)
    ws2.cell(10, 7, "Day 5 Deliverable: Executive Systemic Leak Quantification & Control Fix Plan")
    ws2.cell(10, 8, "Day 5 Readout").font = Font(bold=True)
    for c_i in range(1, 9):
        ws2.cell(10, c_i).fill = sub_fill
        ws2.cell(10, c_i).border = border

    ws2.merge_cells("A12:H12")
    ws2["A12"] = "Pricing Clarification (Unruled Suggestion): Neon's $100 validation fee credited toward the 5-deal Forensic Diagnostic is UNRULED / OPTIONAL and NOT part of the ruled price."
    ws2["A12"].font = Font(italic=True, bold=True, color="92400E")

    for idx, w in enumerate([10, 36, 14, 16, 18, 18, 48, 14], start=1):
        ws2.column_dimensions[get_column_letter(idx)].width = w

    out = Path(output_file).resolve()
    wb.save(out)
    print(f"SUCCESS: Built {out}")


if __name__ == "__main__":
    build_kestrel_step6_workbook()
