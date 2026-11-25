#!/usr/bin/env python3
"""
Runbook A — Step 1 Primary-Source Artifact Intake Verifier & Excel Register Builder.

Usage:
    python step1_tool_artifact_intake_checker.py <folder_path> --deal "Kestrel Industrial Holdings" --opp "OPP-2026-4819"
"""

import argparse
import hashlib
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter
except ImportError:
    print("ERROR: openpyxl is required. Install with: pip install openpyxl", file=sys.stderr)
    sys.exit(1)

ARTIFACT_SPECS = [
    {
        "code": "a",
        "name": "(a) CRM Opportunity Record",
        "patterns": ["_a_crm", "crm_opportunity", "opportunity_record"],
        "preferred_ext": {".csv", ".json", ".xlsx", ".pdf"},
    },
    {
        "code": "b",
        "name": "(b) Quote / Pricing Spreadsheet",
        "patterns": ["_b_pricing", "pricing_spreadsheet", "quote", "calculator"],
        "preferred_ext": {".xlsx", ".xls", ".csv", ".xlsm"},
    },
    {
        "code": "c",
        "name": "(c) Latest Redlined Contract / Order Form",
        "patterns": ["_c_redlined", "redlined_contract", "order_form", "redline"],
        "preferred_ext": {".docx", ".pdf", ".md", ".txt"},
    },
    {
        "code": "d",
        "name": "(d) Approval / Slack / Email Thread",
        "patterns": ["_d_approval", "approval_thread", "slack", "email_thread"],
        "preferred_ext": {".md", ".txt", ".pdf", ".eml", ".json", ".csv"},
    },
    {
        "code": "e",
        "name": "(e) Standard Price Book / Discount Policy",
        "patterns": ["_e_price_book", "price_book", "discount_policy", "policy"],
        "preferred_ext": {".md", ".pdf", ".docx", ".xlsx", ".txt"},
    },
]

REJECTED_SCREENSHOT_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp"}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def find_artifact_file(folder: Path, patterns: list[str], preferred_ext: set[str]) -> Path | None:
    candidates = []
    for item in sorted(folder.iterdir()):
        if not item.is_file():
            continue
        low = item.name.lower()
        if any(p in low for p in patterns):
            # Avoid matching builder scripts when the built spreadsheet exists
            if item.suffix.lower() == ".py":
                candidates.append((2, item))
            elif item.suffix.lower() in preferred_ext:
                candidates.append((0, item))
            else:
                candidates.append((1, item))
    if not candidates:
        return None
    candidates.sort(key=lambda pair: (pair[0], pair[1].name))
    return candidates[0][1]


def audit_folder(folder: Path) -> list[dict]:
    results = []
    for spec in ARTIFACT_SPECS:
        matched = find_artifact_file(folder, spec["patterns"], spec["preferred_ext"])
        if matched is None:
            results.append({
                "code": spec["code"],
                "name": spec["name"],
                "status": "MISSING",
                "file_name": "",
                "ext": "",
                "size_bytes": 0,
                "modified_utc": "",
                "sha256_short": "",
                "native_check": "NO",
                "audit_note": "Required raw artifact not found in deal folder.",
            })
            continue

        stat = matched.stat()
        ext = matched.suffix.lower()
        mod_utc = datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        digest = sha256_file(matched)

        notes = []
        native_ok = "YES"
        status = "RECEIVED"

        if stat.st_size == 0:
            native_ok = "NO"
            status = "PARTIAL"
            notes.append("File is 0 bytes (empty).")
        if ext in REJECTED_SCREENSHOT_EXT:
            native_ok = "NO"
            status = "PARTIAL"
            notes.append("Image/screenshot rejected as primary source; pull native file.")
        elif ext == ".py":
            native_ok = "NO"
            status = "PARTIAL"
            notes.append("Found Python generator script; run it first to produce the native .xlsx file.")
        elif ext not in spec["preferred_ext"]:
            notes.append(f"Non-standard extension ({ext}); confirm native export.")

        if not notes:
            notes.append("Native primary-source file verified and hashed.")

        results.append({
            "code": spec["code"],
            "name": spec["name"],
            "status": status,
            "file_name": matched.name,
            "ext": ext,
            "size_bytes": stat.st_size,
            "modified_utc": mod_utc,
            "sha256_short": digest[:16],
            "native_check": native_ok,
            "audit_note": " ".join(notes),
        })
    return results


def build_excel_register(output_path: Path, deal_name: str, opp_id: str, ae_name: str, results: list[dict]) -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Primary_Source_Gate"

    thin = Side(border_style="thin", color="CBD5E1")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    navy_fill = PatternFill("solid", fgColor="0F172A")
    hdr_fill = PatternFill("solid", fgColor="E2E8F0")
    green_fill = PatternFill("solid", fgColor="DCFCE7")
    amber_fill = PatternFill("solid", fgColor="FEF3C7")
    red_fill = PatternFill("solid", fgColor="FEE2E2")

    ws.merge_cells("A1:J1")
    ws["A1"] = "RUNBOOK A — STEP 1 PRIMARY-SOURCE ARTIFACT INTAKE REGISTER"
    ws["A1"].font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    ws["A1"].fill = navy_fill
    ws["A1"].alignment = Alignment(horizontal="left", vertical="center")
    ws.row_dimensions[1].height = 28

    meta = [
        ("Account / Deal:", deal_name, "CRM Opp ID:", opp_id),
        ("AE Owner:", ae_name, "Audit Timestamp (UTC):", datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")),
    ]
    for r_idx, row in enumerate(meta, start=3):
        ws.cell(r_idx, 1, row[0]).font = Font(bold=True)
        ws.cell(r_idx, 2, row[1])
        ws.cell(r_idx, 5, row[2]).font = Font(bold=True)
        ws.cell(r_idx, 6, row[3])

    headers = [
        "Code", "Required Artifact", "Receipt Status", "File Name",
        "Ext", "Size (Bytes)", "Last Modified (UTC)", "SHA-256 (16-char)",
        "Native Primary?", "Automated Audit Note"
    ]
    header_row = 6
    for c_idx, h in enumerate(headers, start=1):
        cell = ws.cell(header_row, c_idx, h)
        cell.font = Font(bold=True, color="0F172A")
        cell.fill = hdr_fill
        cell.border = border
        cell.alignment = Alignment(horizontal="center", vertical="center")

    start_row = 7
    for idx, rec in enumerate(results):
        r = start_row + idx
        vals = [
            rec["code"], rec["name"], rec["status"], rec["file_name"],
            rec["ext"], rec["size_bytes"], rec["modified_utc"],
            rec["sha256_short"], rec["native_check"], rec["audit_note"]
        ]
        for c_idx, val in enumerate(vals, start=1):
            cell = ws.cell(r, c_idx, val)
            cell.border = border
            if c_idx == 6:
                cell.number_format = "#,##0"
            if c_idx == 3:
                cell.font = Font(bold=True)
                if val == "RECEIVED":
                    cell.fill = green_fill
                elif val == "PARTIAL":
                    cell.fill = amber_fill
                else:
                    cell.fill = red_fill

    # Live Excel Gate Formulas (Rows 14-17)
    ws["A13"] = "AUTOMATED STEP 1 GATE SUMMARY (LIVE EXCEL FORMULAS)"
    ws["A13"].font = Font(bold=True, size=11)

    summary_rows = [
        ("Artifacts Received (Target = 5)", '=COUNTIF(C7:C11,"RECEIVED")'),
        ("Native Primary-Source Verified (Target = 5)", '=COUNTIF(I7:I11,"YES")'),
        ("Missing / Partial Artifacts", '=5-B14'),
        (
            "Step 1 Gate Verdict",
            '=IF(AND(B14=5,B15=5),"GREEN — PROCEED TO STEP 2",IF(B14>=4,"YELLOW — CONDITIONAL HOLD (RESOLVE GAP)","RED — HARD STOP (DO NOT DIAGNOSE ON HEARSAY)"))'
        ),
    ]
    for offset, (label, formula) in enumerate(summary_rows):
        r = 14 + offset
        ws.cell(r, 1, label).font = Font(bold=True)
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3)
        val_cell = ws.cell(r, 4, formula)
        ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=10)
        val_cell.font = Font(bold=True)
        for c in range(1, 11):
            ws.cell(r, c).border = border

    # Tab 2: Clinician Checklist
    ws2 = wb.create_sheet("Audit_Checklist")
    ws2["A1"] = "STEP 1 CLINICIAN HYGIENE CHECKLIST"
    ws2["A1"].font = Font(bold=True, size=12)
    ws2.append(["Item #", "Control Rule", "Done (YES/NO)", "Clinician Note"])
    for c in range(1, 5):
        ws2.cell(2, c).font = Font(bold=True)
        ws2.cell(2, c).fill = hdr_fill
        ws2.cell(2, c).border = border

    checks = [
        ("1", "Pulled all 5 raw artifacts BEFORE accepting AE verbal framing", "NO", ""),
        ("2", "Verified quote spreadsheet contains live formulas (no uninspected PDF summary)", "NO", ""),
        ("3", "Confirmed latest redlined contract includes tracked changes and counsel comments", "NO", ""),
        ("4", "Exported raw approval/Slack/email thread with intact timestamps", "NO", ""),
        ("5", "Loaded active Price Book & Discount Policy with explicit approval tiers", "NO", ""),
        ("6", "Logged all verbal AE claims into Quarantine Log for Step 4 testing", "NO", ""),
    ]
    for idx, row in enumerate(checks, start=3):
        for c_idx, val in enumerate(row, start=1):
            cell = ws2.cell(idx, c_idx, val)
            cell.border = border

    ws2["A10"] = "Checklist Completion %"
    ws2["A10"].font = Font(bold=True)
    ws2["C10"] = '=COUNTIF(C3:C8,"YES")/COUNTA(C3:C8)'
    ws2["C10"].number_format = "0%"
    ws2["C10"].font = Font(bold=True)

    widths = [7, 36, 15, 42, 8, 14, 22, 18, 15, 46]
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w
    for i, w in enumerate([10, 62, 16, 40], start=1):
        ws2.column_dimensions[get_column_letter(i)].width = w

    wb.save(output_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Verify Runbook A Step 1 raw artifacts and build Excel intake register.")
    parser.add_argument("folder", help="Path to directory containing the 5 raw deal artifacts")
    parser.add_argument("--deal", default="Unnamed Deal", help="Account / deal name")
    parser.add_argument("--opp", default="TBD", help="CRM Opportunity ID")
    parser.add_argument("--ae", default="TBD", help="Account Executive name")
    parser.add_argument("--out", default="", help="Optional output .xlsx path")
    args = parser.parse_args()

    folder = Path(args.folder).resolve()
    if not folder.is_dir():
        print(f"ERROR: Folder does not exist: {folder}", file=sys.stderr)
        sys.exit(1)

    results = audit_folder(folder)
    received = sum(1 for r in results if r["status"] == "RECEIVED")
    native = sum(1 for r in results if r["native_check"] == "YES")

    slug = re.sub(r"[^a-z0-9]+", "_", args.deal.lower()).strip("_") or "deal"
    out_path = Path(args.out) if args.out else folder / f"{slug}_step1_intake_register.xlsx"
    build_excel_register(out_path, args.deal, args.opp, args.ae, results)

    print(f"=== STEP 1 PRIMARY-SOURCE AUDIT: {args.deal} ({args.opp}) ===")
    for r in results:
        print(f"[{r['status']:8s}] {r['name']} -> {r['file_name'] or 'NOT FOUND'} | Native={r['native_check']} | SHA256={r['sha256_short'] or '-'}")
        if r["audit_note"]:
            print(f"           Note: {r['audit_note']}")
    verdict = "GREEN" if (received == 5 and native == 5) else ("YELLOW" if received >= 4 else "RED")
    print(f"VERDICT: {verdict} (Received {received}/5, Native {native}/5)")
    print(f"REGISTER SAVED: {out_path}")


if __name__ == "__main__":
    main()
