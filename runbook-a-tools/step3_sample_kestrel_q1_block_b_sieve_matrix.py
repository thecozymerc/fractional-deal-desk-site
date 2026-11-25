#!/usr/bin/env python3
"""
Builds Step 3 Sample 2: step3_sample_kestrel_q1_block_b_sieve_matrix.xlsx
Kestrel Industrial Holdings — Completed Q1 Block B 5-Bucket QTC Sieve & Prioritized Differential
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


def build_kestrel_step3_matrix(output_file: str = "step3_sample_kestrel_q1_block_b_sieve_matrix.xlsx") -> None:
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
    # TAB 1: QTC_5Bucket_Sieve
    # =========================================================================
    ws = wb.active
    ws.title = "QTC_5Bucket_Sieve"

    ws.merge_cells("A1:I1")
    ws["A1"] = "RUNBOOK A — STEP 3 SAMPLE: KESTREL INDUSTRIAL HOLDINGS — 5-BUCKET QTC SURGICAL SIEVE"
    ws["A1"].font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    ws["A1"].fill = navy_fill
    ws["A1"].alignment = Alignment(horizontal="left", vertical="center")
    ws.row_dimensions[1].height = 28

    ws.merge_cells("A2:I2")
    ws["A2"] = "Anchored strictly to Step 1 Raw Artifacts (a–e) and Step 2 Verified Problem Representation. Zero buckets skipped."
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
        "Code", "Q1 Block B — QTC Bucket", "Scanned?",
        "Severity (1-5)", "Evidence (1-5)", "Weighted Score",
        "Automated Risk Tier", "Verified Kestrel Findings (Step 1 Artifacts & Step 2 PR)",
        "Citations & Explicit UNVERIFIED Gaps"
    ]
    for idx, h in enumerate(headers, start=1):
        c = ws.cell(6, idx, h)
        c.font = Font(bold=True, color="0F172A")
        c.fill = hdr_fill
        c.border = border
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[6].height = 26

    bucket_rows = [
        (
            "B1", "Commercial / Pricing", "YES", 5, 5,
            "28.0% discretionary subscription discount (-$84,000 off $300K list) triggers Tier-4 (>25%). AE manually overwrote Impl list cell E13 ($30K->$24K, -$6K concealed discount; -$2K / -8.3% impl GM). Total true concession = $90,000 (27.3% off $330K list). Consolidated 3-yr GM = 70.8% ($170K/$240K), $10,000 below 75.0% policy floor; Y1 GM = 52.6%.",
            "b:Quote_Ramp_Calculator!E13,G12,M14,D18:M21; b:True_List_Leak_Bridge!B5:B12; e:PB-1.3,3.0,4.1. UNVERIFIED: Finance exception floor (U-2); actual SAP/ERP delivery cost vs $26K COGS (U-4)."
        ),
        (
            "B2", "Governance / Authority", "YES", 5, 5,
            "Zero written Finance Margin Sign-Off from Controller Elena Rostova (zero exception packet submitted). VP Sales Marcus Vance gave casual verbal Slack nods (Nov 4 & Nov 18) without viewing 28% disc / 70.8% GM / opt-out — invalid under PB-4.3. Deal Desk HARD HOLD (Nov 9, DD-8842) sat unworked by AE for 16 days. Externally, sole Economic Buyer/signatory >$50K is CFO Gregory Cho (zero meetings, zero budget approval), contradicting CRM.",
            "a:CRM-21-24,28-29; c:L098-104; d:T027-104; e:PB-3.0,4.2,4.3. UNVERIFIED: CFO Cho ROI priorities (U-1); VP Marcus sponsorship after viewing true P&L (U-3)."
        ),
        (
            "B3", "Config / Tools", "YES", 4, 5,
            "CRM operates in Manual/Unsynced offline Excel mode; CRM quote attachment is outdated v2 ($264K/20%). Stale CRM Discount=20.0% triggered a false-green workflow ('Not Required — Auto-Cleared <=20%'), blinding Finance to a Tier-4 breach. CRM leaves GM% blank, Net-30 stale, Opt-Out FALSE, ARR miscalculated ($80K flat), and permits Forecast=Commit while Deal Desk is On Hold & Legal Blocked. Excel E13 lacked cell protection.",
            "a:CRM-08,12,15-26; b:E13; e:PB-6.1. UNVERIFIED: Whether identical CRM-to-Quote-to-Legal gaps leak across 20-30% of broader enterprise pipeline (addressed in Step 6 Bridge)."
        ),
        (
            "B4", "Paper / Redline", "YES", 5, 5,
            "Kestrel GC Nadia Benali turned redlines in 3 days (Nov 6), disproving 'slow legal.' Redline OF-2026-4819-v3 inserts 7 policy breaches: (1) Sec 2.3 Month-12 unilateral penalty-free opt-out w/ zero clawback; (2) Sec 4.1 & 3.2 Net-60 post-Go-Live Acceptance; (3) Sec 1.3 20% Y2-3 seat true-down; (4) Sec 9.1 3x ($720K) liability cap + uncapped security/IP; (5) Sec 7.2 25% annual SLA credit + refund exit; (6) Sec 5.4 0% renewal cap / no auto-renew; (7) Sec 11.3 retroactive MFN.",
            "c:L015-095; d:T039-061; e:PB-2.3,5.1-5.4. UNVERIFIED: Which redlines are true CFO non-negotiables vs procurement opening asks (U-1)."
        ),
        (
            "B5", "Downstream Billability / Rev-Rec", "YES", 5, 5,
            "ASC 606 blow-up if signed as written: Month-12 penalty-free opt-out cuts enforceable TCV by 67.5% ($240,000 -> $78,000; $162,000 unbookable/at risk). Subjective acceptance billing (Sec 3.2/4.1) defers rev-rec start and stretches Y1 cash collection to ~105+ days. Upfront $24K commission (10% of $240K) vs $41K Y1 GP leaves just $17K (21.8%) net contribution + PB-6.2 clawback risk. True-down, SLA refund, and MFN trigger variable-consideration reversals.",
            "b:Year1_OptOut_Sensitivity!B3:B12; c:L019-094; d:T071-072; e:PB-5.1-6.2. UNVERIFIED: Actual SAP/ERP cutover duration beyond 45 days extending cash delay further (U-4)."
        ),
    ]

    for offset, (code, name, scanned, sev, evid, finding, cite) in enumerate(bucket_rows, start=7):
        ws.cell(offset, 1, code).font = Font(bold=True)
        ws.cell(offset, 2, name).font = Font(bold=True)
        ws.cell(offset, 3, scanned).font = Font(bold=True)
        ws.cell(offset, 4, sev)
        ws.cell(offset, 5, evid)
        ws.cell(offset, 6, f'=IF(C{offset}="YES",D{offset}*E{offset},0)').font = Font(bold=True)
        tier_c = ws.cell(
            offset, 7,
            f'=IF(C{offset}<>"YES","UNSCANNED — VIOLATION",IF(F{offset}>=21,"CRITICAL",IF(F{offset}>=15,"HIGH",IF(F{offset}>=8,"MODERATE","LOW"))))'
        )
        tier_c.font = Font(bold=True, color="991B1B" if sev * evid >= 21 else "92400E")
        tier_c.fill = red_fill if sev * evid >= 21 else amber_fill
        ws.cell(offset, 8, finding)
        ws.cell(offset, 9, cite)
        ws.row_dimensions[offset].height = 88
        for c_i in range(1, 10):
            cell = ws.cell(offset, c_i)
            cell.border = border
            cell.alignment = Alignment(
                horizontal="center" if c_i in {1, 3, 4, 5, 6, 7} else "left",
                vertical="top",
                wrap_text=True
            )

    ws["A13"] = "SURGICAL SIEVE COMPLETENESS & ANTI-ANCHORING GATE (LIVE FORMULAS)"
    ws["A13"].font = Font(bold=True, size=11)
    summary = [
        (14, "QTC Buckets Scanned (Mandatory = 5 of 5)", '=COUNTIF(C7:C11,"YES")'),
        (15, "CRITICAL Buckets (>=21 Score)", '=COUNTIF(G7:G11,"CRITICAL")'),
        (16, "Composite Deal Risk Index (Max = 125)", "=SUM(F7:F11)"),
        (17, "Average Bucket Severity (1-5)", '=IF(D14>0,AVERAGE(D7:D11),0)'),
        (18, "Anti-Anchoring Sieve Gate", '=IF(D14=5,"PASS — ALL 5 QTC BUCKETS SCANNED; DIFFERENTIAL UNLOCKED","STOP — SCAN ALL 5 BUCKETS")'),
    ]
    for r, label, formula in summary:
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3)
        ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=9)
        ws.cell(r, 1, label).font = Font(bold=True)
        val_c = ws.cell(r, 4, formula)
        val_c.font = Font(bold=True)
        if r == 17:
            val_c.number_format = "0.0"
        if r == 18:
            val_c.fill = green_fill
            val_c.font = Font(bold=True, color="166534")
        for c_i in range(1, 10):
            ws.cell(r, c_i).border = border

    for idx, w in enumerate([8, 28, 12, 13, 13, 14, 18, 56, 38], start=1):
        ws.column_dimensions[get_column_letter(idx)].width = w

    # =========================================================================
    # TAB 2: Prioritized_Differential
    # =========================================================================
    ws2 = wb.create_sheet("Prioritized_Differential")
    ws2.merge_cells("A1:I1")
    ws2["A1"] = "RUNBOOK A — STEP 3 SAMPLE: KESTREL PRIORITIZED DIFFERENTIAL DIAGNOSIS"
    ws2["A1"].font = Font(size=13, bold=True, color="FFFFFF")
    ws2["A1"].fill = navy_fill
    ws2.row_dimensions[1].height = 26

    d_headers = [
        "Slot", "Clinical Category", "Hypothesis / Threat Title",
        "QTC Buckets", "Likelihood (1-5)", "Impact (1-5)",
        "Priority Score", "Verified Evidence & Explicit UNVERIFIED Gaps",
        "Exact Step 4 Forensic Verification Test"
    ]
    for idx, h in enumerate(d_headers, start=1):
        c = ws2.cell(3, idx, h)
        c.font = Font(bold=True)
        c.fill = hdr_fill
        c.border = border
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    diff_rows = [
        (
            "D-1", "Leading Hypothesis",
            "Dual Internal Governance Deadlock & Unengaged Economic Buyer Gate",
            "B2, B1, B4, B3", 5, 5,
            "19-day stall is NOT slow customer legal (GC turned redlines in 3 days; buyer chased Nov 16). Legal (HOLD Nov 6) and Deal Desk (HARD HOLD Nov 9, DD-8842) blocked work over 5 control breaches (CRM mismatch, 28% Tier-4 disc, $6K impl override, 70.8% GM below 75% floor, Month-12 opt-out & Net-60 acceptance). AE left DD-8842 unworked 16 days with zero Finance Margin Exception and invalid verbal VP Slack nods only, while buyer CFO Gregory Cho (sole signatory >$50K, zero meetings) withholds Q4 budget approval.",
            "Run Approval-Hop Timestamp Audit (Nov 3-25), Three-Way Diff (CRM vs Quote v4 vs Redline), and Disconfirming-Evidence Hunt refuting AE's 'slow buyer legal' and 'VP approved' claims."
        ),
        (
            "D-2", "Can't-Miss / ROWS Threat",
            "Signing an Unenforceable Rev-Rec, Margin & Uncapped-Liability Landmine Under Q4 Panic",
            "B5, B4, B1", 3, 5,
            "Worst-case blow-up: rushing an executive override ahead of Dec 1 to save Q4 Commit and signing OF-2026-4819-v3 as written. ASC 606 collapses enforceable TCV 67.5% ($240K -> $78K; $162K unbookable); Y1 GM is 52.6% with only $17K net contribution after $24K upfront commission and -$2K impl loss; Net-60 post-acceptance pushes Y1 cash ~105+ days; 3x ($720K) cap + uncapped security/IP, 25% SLA refund exit, 20% true-down, and retroactive MFN threaten entire <=100-seat industrial base.",
            "Run 3-Window Deal Engine (Leak Waterfall, Behavioral Verdict, 51-Contract-Flag Audit) on Quote v4 and Redline v3 to quantify exact dollar leak, ASC 606 restatement, and contract-flag count."
        ),
        (
            "D-3", "Alternative Explanation #1",
            "Unqualified / Non-Viable Buyer Budget ('Phantom Q4 Deal') Masking as Legal Friction",
            "B2 (External)", 4, 4,
            "Even if Seller cleared DD-8842 tomorrow, deal may fail Q4 because CFO Gregory Cho never approved capital budget (d:T047-048), never met Seller (d:T104), and Ohio plant consolidation (c:L022-023) signals real Y2-3 headcount risk. Buyer's opt-out, 20% true-down, and acceptance-gated Net-60 may mask an unfunded VP Ops wish list. UNVERIFIED: CFO Cho's capital availability and competitive alternatives (U-1, U-5).",
            "Run Disconfirming-Evidence Hunt on buyer emails (d:T005-009,T045-050,T085-088) and GC redline comments (R-02, R-03, R-10) to isolate buyer budget non-qualification from Seller internal silence."
        ),
        (
            "D-4", "Alternative Explanation #2",
            "Systemic QTC Tooling & Upstream Control Architecture Failure Across Enterprise Pipeline",
            "B3, B1", 4, 4,
            "Stall may stem from systemic QTC tooling gaps rather than isolated AE error: zero CPQ-CRM sync (a:CRM-25), unprotected Excel list cell E13 (b:E13), false-green Finance workflow from unvalidated 20% CRM entry (a:CRM-15,22), optional blank GM% field (a:CRM-20), and zero CRM hard-lock blocking Commit forecast during Deal Desk/Legal holds (a:CRM-08,23,24). UNVERIFIED in 1-deal work-up: whether 20-30% of deal flow leaks identically (tested in 5-Deal Diagnostic).",
            "Run line-by-line Three-Way Diff (CRM vs Quote v4 vs Redline vs Policy) to isolate every systemic tooling/handoff gap where controls failed to enforce POL-COMM-2026-v3."
        ),
    ]

    for offset, (slot, cat, title, bkts, like, imp, rat, test) in enumerate(diff_rows, start=4):
        ws2.cell(offset, 1, slot).font = Font(bold=True)
        ws2.cell(offset, 2, cat).font = Font(bold=True)
        ws2.cell(offset, 3, title).font = Font(bold=True)
        ws2.cell(offset, 4, bkts)
        ws2.cell(offset, 5, like)
        ws2.cell(offset, 6, imp)
        sc = ws2.cell(offset, 7, f"=E{offset}*F{offset}")
        sc.font = Font(bold=True, color="991B1B" if like * imp >= 20 else "92400E")
        sc.fill = red_fill if slot in {"D-1", "D-2"} else amber_fill
        ws2.cell(offset, 8, rat)
        ws2.cell(offset, 9, test)
        ws2.row_dimensions[offset].height = 96
        for c_i in range(1, 10):
            cell = ws2.cell(offset, c_i)
            cell.border = border
            cell.alignment = Alignment(
                horizontal="center" if c_i in {1, 4, 5, 6, 7} else "left",
                vertical="top",
                wrap_text=True
            )

    ws2["A9"] = "STEP 3 DIFFERENTIAL READINESS GATE (CROSS-TAB LIVE FORMULAS)"
    ws2["A9"].font = Font(bold=True, size=11)
    checks = [
        (10, "Leading Hypothesis Populated (D-1)", '=IF(COUNTA(C4,H4,I4)=3,"YES","NO")'),
        (11, "Can't-Miss / ROWS Threat Populated (D-2)", '=IF(COUNTA(C5,H5,I5)=3,"YES","NO")'),
        (12, "2 Alternative Explanations Populated (D-3 & D-4)", '=IF(AND(COUNTA(C6,H6,I6)=3,COUNTA(C7,H7,I7)=3),"YES","NO")'),
        (13, "Step 3 Overall Gate Verdict", '=IF(AND(QTC_5Bucket_Sieve!D14=5,C10="YES",C11="YES",C12="YES"),"GREEN — READY FOR STEP 4 FORENSIC VERIFICATION","RED — INCOMPLETE")'),
    ]
    for r, label, formula in checks:
        ws2.merge_cells(start_row=r, start_column=1, end_row=r, end_column=2)
        ws2.merge_cells(start_row=r, start_column=3, end_row=r, end_column=9)
        ws2.cell(r, 1, label).font = Font(bold=True)
        val_c = ws2.cell(r, 3, formula)
        val_c.font = Font(bold=True)
        if r == 13:
            val_c.fill = green_fill
            val_c.font = Font(bold=True, color="166534")
        for c_i in range(1, 10):
            ws2.cell(r, c_i).border = border

    for idx, w in enumerate([8, 24, 36, 16, 13, 12, 14, 56, 44], start=1):
        ws2.column_dimensions[get_column_letter(idx)].width = w

    out = Path(output_file).resolve()
    wb.save(out)
    print(f"SUCCESS: Built {out}")


if __name__ == "__main__":
    build_kestrel_step3_matrix()
