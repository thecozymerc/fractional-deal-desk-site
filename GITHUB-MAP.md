# GITHUB MAP — where everything is in this repository

This repository mirrors the sitemap. **One folder per page** — a page's files live in its own folder and nowhere else, so a change touches exactly one folder. The same structure exists in the Drive mirror ("Site — Code & Pages (GitHub mirror)"), where each page folder also holds the page's text in a Page Text Sheet.

## How to read this repo
- **This file** = the map of the repository.
- **CODE-MAP.md** = the master map of the whole site project (copied here at each deploy).
- **CHANGELOG.md** = every change ever made to the site, in plain words (copied here at each deploy).
- **LABEL.md in every folder** = what that page is, its sitemap ID and address, and its status.
- This repo holds the **publish copies** (each page as `index.html` in its folder). The **source of truth** for a page is its ID-named file (for example `P02-services-and-pricing.html`), kept in the matching Drive mirror folder.

## The tree (sitemap order)

| Repo folder | Page ID | Address | Holds | Status |
|---|---|---|---|---|
| `/` (root) | P01 | `/` | Homepage publish copy + this map + README | Live |
| `assets/` | — | — | Shared styles + the spreadsheet engine | Live |
| `services/` | P02 | `/services/` | Services & Pricing | Live |
| `about/` | P03 | `/about/` | About — label only until built | Skeleton |
| `tools/` | P04 | `/tools/` | Tools hub — label only until built | Skeleton |
| `tools/pricing-engines/` | S6-P01 | `/tools/pricing-engines/` | Partition page — label only | Skeleton |
| `tools/deal-pricing-solver/` | S6-P01.a | `/tools/deal-pricing-solver/` | **Deal Pricing Calculator** | Live |
| `tools/perpetual-to-saas-conversion/` | S6-P01.b | `/tools/perpetual-to-saas-conversion/` | Conversion Calculator | Live |
| `tools/perm-calculator/` | S6-P01.c | `/tools/perm-calculator/` | Perm Calculator — label only | Skeleton |
| `tools/spend-variance/` | S6-P02 | `/tools/spend-variance/` | Spend Variance — label only | Skeleton |
| `tools/stories-and-sandboxes/` | S6-P05 | `/tools/stories-and-sandboxes/` | Stories partition — label only | Skeleton |
| `tools/intake-gate/` | S6-P05.1 | `/tools/intake-gate/` | Label only | Skeleton |
| `tools/redlining-playbook/` | S6-P05.2 | `/tools/redlining-playbook/` | Label only | Skeleton |
| `tools/qtc-diagnostic/` | S6-P05.3 | `/tools/qtc-diagnostic/` | Label only | Skeleton |
| `tools/bundling-sandbox/` | S6-P05.4 | `/tools/bundling-sandbox/` | Label only | Skeleton |
| `tools/contract-operations/` | S6-P03 | `/tools/contract-operations/` | Partition page — label only | Skeleton |
| `tools/deal-check/` | S6-P03.1 | `/tools/deal-check/` | Label only | Skeleton |
| `tools/contract-migration-triage/` | S6-P03.2 | `/tools/contract-migration-triage/` | Label only | Skeleton |
| `tools/case-operations-capacity/` | S6-P03.3 | `/tools/case-operations-capacity/` | Label only | Skeleton |
| `tools/contracts-library/` | S6-P06 | `/tools/contracts-library/` | Library partition — label only | Skeleton |
| `tools/contracts-library/tier-1/` | S6-P06.1 | `/tools/contracts-library/tier-1/` | Label only | Skeleton |
| `tools/contracts-library/tier-2/` | S6-P06.2 | `/tools/contracts-library/tier-2/` | Label only | Skeleton |
| `tools/contracts-library/tier-3/` | S6-P06.3 | `/tools/contracts-library/tier-3/` | Label only | Skeleton |
| `tools/executive-intelligence/` | S6-P04 | `/tools/executive-intelligence/` | Partition page — label only | Skeleton |
| `tools/weighted-decision-scoring/` | S6-P04 (tool) | `/tools/weighted-decision-scoring/` | Label only | Skeleton |
| `tools/executive-dashboard/` | S6-P04 (tool) | `/tools/executive-dashboard/` | Label only | Skeleton |

## Making a change
1. Find the page's folder in the table above (or in the Drive mirror).
2. The change is made on the ID-named source file, verified, then the publish copy here is refreshed — and the folder's LABEL, the CODE-MAP, and the CHANGELOG are updated in the same pass (the standing Build Checklist).
3. Every deploy refreshes this map if the tree changed.
