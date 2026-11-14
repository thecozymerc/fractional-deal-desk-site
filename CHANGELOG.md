# CHANGE LOG — every change to the site code, in plain words

## 2026-11-13 — Tool 13 (S6-P03.4) ARGON FULL REBUILD live

- The Contract Analyzer page is rebuilt by Argon
  (TOOL 13.1) in the Tool 12 frame: the working surface
  first (upload TXT / DOCX / PDF or paste; Load the sample
  contract; Clear), results with a found / not-found
  filter bar and per-group counters, a copyable Analysis
  Brief, and the AI read panel with its three graceful
  failure states. Argon's Deal Check ruling (its call
  inside the no-selling rule, declared in its manifest):
  the old closing "Next — From a scan to a worked deal"
  section is dropped; the Deal Check rides as a plain
  descriptive link among the related links.
- THE ENGINE IS UNCHANGED: the analyzer JavaScript
  (Layer 1 six scans ported exactly from the operator's
  contract-analyzer repo, quirks included; Layer 2 the 33
  coverage checks) is inlined in the page byte-for-byte
  from S6-P03d-analyzer.js, LABEL header intact — verified
  by source diff (identical) and by output equivalence on
  three fixtures run against the original engine (sample
  8 of 33 with the exact found ids; prose 0 of 33;
  synthetic full-coverage 33 of 33). The standalone
  engine file retires from the folder to the
  tool-13-iterations branch archive.
- One mechanical fix at promotion (disclosed): Argon's
  two Tool 10 links pointed at ../case-operations/ (the
  partition's address); corrected to
  ../case-operations-capacity/. Argon's manifest had
  itself flagged the hrefs for verification against
  CODE-MAP.
- Verification (Muse): DOM battery 25/25 (engine
  equivalence deep-compare, sample-load flow, full-fixture
  paste flow at 33 found, empty-run handling, AI wiring
  and fallbacks, zero page errors); standing-law scan
  clean; JSON-LD parses; width ladder zero overflow at
  280-1280; screenshots both modes; live on Cloudflare at
  the exact promoted bytes, with the AI read endpoint
  re-verified after deploy. Run note: AI Studio did not
  surface the .js engine file from the inputs zip; the
  engine was supplied as a byte-identical .txt copy
  (md5-verified) in the same window, and Argon inlined
  from that file.

## 2026-11-13 — Tool 12 (S6-P04.b) ARGON FULL REBUILD live

- The Executive Dashboard page is rebuilt by Argon
  (TOOL 12.1): seven headline KPIs computed live from the
  register (total case volume, Open + In Progress backlog,
  escalated, closed, escalation rate, average resolution /
  age, SLA breaches), a Regional Performance table rolling
  the same register up by region with a reconciled-sum
  footer, the full 36-case register as the editable working
  layer, a copyable Dashboard Brief, and one-tap scenario
  presets. The superseded page's closing booking section
  does not carry over (no-selling rule).
- Math is the workbook's, UNALTERED (Argon manifest) —
  including its two backlog definitions, kept and named
  rather than reconciled: the headline line counts Open +
  In Progress only; the regional Backlog column counts
  every not-Closed case. Escalation rate = ROUND
  (Escalated / Total x 100, 1); open cases age against the
  visitor's date, as the workbook's TODAY() formulas do.
  Load anchors: Total 36 · Backlog 21 · Escalated 3 ·
  Closed 12 · Escalation rate 8.3% · SLA breaches 28 and
  Avg age 35.1 at the 2026-11-11 reference date.
- Verification (Muse): independent DOM battery 74/74 with
  the clock frozen at the reference date — register
  cell-for-cell, KPIs, all 30 regional figures,
  reconciliation sums, the three preset boundary cases
  (close a case, escalate a case, widen a target), a
  manual region-edit probe, reset — zero page errors;
  standing-law scan clean; width ladder zero overflow at
  280-1280; screenshots both modes; live on Cloudflare at
  the exact promoted bytes. URL context was ON for the
  Argon run (standing instruction, Nov 13).

## 2026-11-13 — Tool 11 (S6-P04.a) ARGON FULL REBUILD live

- The Weighted Decision Scoring page is rebuilt by Argon
  (TOOL 11.1): two scoring grids on ONE shared weight set —
  the main grid (the framework's eight criteria, editable
  weights and scores for Option A / B / C — SAMPLE) and a
  worked vendor-evaluation example whose Weight column is a
  live display of the same weights, exactly as the workbook
  links every example Weight cell to its main sheet.
  Composites, ranks, winner lines, the weight total, and the
  workbook's OK / WARNING check line compute live; a
  copyable Decision Brief and one-tap scenario presets ride
  along. The superseded page's closing booking section does
  not carry over (no-selling rule).
- Math is the workbook's, UNALTERED (Argon manifest):
  Composite = SUMPRODUCT of the weights and that option's
  scores; Rank = Excel RANK descending (ties share the
  better rank); Winner = the first maximum (INDEX / MATCH
  first-match); weight check — ABS(total - 1) < 0.0001 reads
  "OK — weights add up to 100%", else the WARNING string.
  Load anchors: main composites 75.45 / 85.20 / 65.45
  (Option B — SAMPLE wins); example composites 82.55 /
  79.175 / 77.775 (Sample Vendor A wins).
- Verification (Muse): independent DOM battery 72/72 —
  all 64 sample inputs and 8 linked-weight displays
  cell-for-cell vs the workbook, verdict strip, both grids'
  composites / ranks / winners / check lines, all five
  preset boundary cases (weight-break, winner-flip,
  shared-weights, tie, zero weights), a manual weight-edit
  probe proving the example grid follows the shared
  weights, brief, sticky strip, reset — zero page errors;
  standing-law scan clean; width ladder zero overflow at
  280-1280; screenshots both modes; live on Cloudflare at
  the exact promoted bytes. URL context was ON for the
  Argon run (standing instruction, Nov 13).

## 2026-11-13 — Tool 10 (S6-P03.3) ARGON FULL REBUILD live

- The Case Operations & Capacity page is rebuilt by Argon
  (TOOL 10.1): a 30-case register carrying the workbook's
  eleven columns (Region / Queue / Case Type / Priority /
  Status as selects; Age / Resolution and SLA Flag computed,
  never typed), a Backlog & SLA Dashboard that recounts the
  register live (status counts, backlog, breaches, average
  age, and the by-region table), a Capacity Simulator whose
  current backlog is linked live from the dashboard (effective
  capacity, net cleared, days to clear, 30-day projection),
  and a copyable Queue Brief. The superseded page's closing
  booking section does not carry over (no-selling rule).
- Math is the workbook's, UNALTERED (Argon manifest): Age —
  Closed reads Closed minus Opened, otherwise TODAY() minus
  Opened (the visitor's local date, as the workbook behaves);
  Flag — BREACH when Age > SLA Target; Backlog — every case
  not Closed (the workbook's own corrected KPI; the note is
  carried on the page); Effective — Analysts x Cases/day
  divided by ((1 - Share) + Share x Multiplier); Days —
  ROUNDUP(Backlog / Net), or the workbook's exact words
  "Backlog grows at these settings — no clear date" when
  Net <= 0. Reference-date (2026-11-11) anchors: Total 30,
  Backlog 18, Breaches 27, Avg age 31.6, Effective 9.6,
  Net +3.6, Days 5.
- Corrective, disclosed: the rebuild prompt's sample data
  carried one wrong cell — CASE-1027 Region "AMER West"; the
  workbook says EMEA (Case Register B28). Argon's manifest
  flagged the discrepancy on the first pass; a corrective
  Argon run changed the one cell, workbook governing. Effect:
  reference-date breaches by region AMER West 5 / EMEA 4;
  total breaches 27 and backlog unchanged (the case is
  Closed).
- Verification (Muse): independent DOM battery at the frozen
  reference date, 75/75 — all 270 sample fields cell-for-cell
  vs the workbook, dashboard and region anchors, simulator
  anchors, all five preset boundary cases, zero-analyst
  sweep, brief, reset — zero page errors; standing-law scan
  clean; width ladder zero overflow at 280-1280; screenshots
  both modes; live on Cloudflare at the exact promoted
  bytes. URL context was ON for both Argon runs (standing
  instruction, Nov 13).

## 2026-11-13 — Tool 9 (S6-P03.2) ARGON FULL REBUILD live

- The Contract Migration & Triage Tracker page is rebuilt by
  Argon (TOOL 9.1): an editable tracker carrying the workbook's
  fourteen columns (Status, Tier, and Auto-Renewal as selects;
  every other field a live input; Risk Flag computed, never
  typed), a KPI strip with the workbook's own count-by-tier and
  Flags-at-REVIEW tallies, a copyable Migration Brief naming
  every REVIEW row, add/delete row with Reset to sample, and
  the three static governance references (Approval Routing,
  RACI Matrix, Exception Log). The superseded page's closing
  booking section does not carry over (no-selling rule).
- Math is the workbook's, UNALTERED (Argon manifest, section
  1): Risk Flag — At Risk → REVIEW, Complete → Done, anything
  else → Monitor; tier counts are the workbook's COUNTIFs over
  the rows present. Load anchors: Tier 1 3 · Tier 2 2 ·
  Tier 3 1 · REVIEW 1 · Done 1 · Monitor 4. The RACI section
  now correctly says six activities (the old page said seven;
  the workbook has six).
- Verification (Muse): sample data cell-for-cell against the
  workbook; DOM battery 116 checks incl. all five boundary
  cases, add/delete floor (the tracker always keeps one row),
  and reset — zero page errors; Argon's own 12 in-page asserts
  pass; standing-law scan clean; width ladder zero overflow
  at 280–1280; screenshots both modes; live on Cloudflare at
  the exact promoted bytes. One executor mechanical fix at
  promotion: two Deal Check hrefs corrected for link depth
  (../../deal-check/ → ../deal-check/).
- The first-generation workbook-embed build (page + data.js)
  is archived in tool9-build/original-live-copy-2026-11-13/
  and on the GitHub branch tool-9-iterations.

## 2026-11-13 — S6-P05 partition rename COMPLETE (Deal Desk Controls)

- The partition page at /tools/stories-and-sandboxes/ is
  rebuilt by Argon to the Tool 7/8 bank frame and renamed
  DEAL DESK CONTROLS in its title, breadcrumb, eyebrow,
  cards, and structured data. The address and all four tool
  targets (Tools 5–8) are unchanged. The old story framing
  and the Book-a-Call block are retired with the old page.
- The tools hub (S6-proof-of-work) is updated naming-only:
  the lede and the third partition card now say Deal Desk
  Controls; every other byte is the supplied file's.
- Verification (Muse): hub diff = the manifest plus the
  three naming lines only; partition law scans clean (no
  story framing, no pitch, no employer names; senior anchors
  present); JSON-LD parses; width ladder zero overflow at
  280–1280 on both pages; screenshots in both modes; live
  on Cloudflare at the exact promoted bytes.

## 2026-11-13 — Tool 8 (S6-P05.4) ARGON FULL REBUILD live

- The Bundling Sandbox page is rebuilt by Argon (TOOL 8.1):
  a working sandbox — two bundle options built line by line
  against a buyer budget ceiling and a margin floor, each
  gated live. Gate strip up top carries both verdicts;
  Deal Settings; the two option tables; a copyable Bundle
  Brief; Reset. Story 4 retired with the old embed build.
- Math is the workbook's, with three alterations Argon
  declared in its in-file manifest: (1) the zero-revenue
  margin guard extended to every line and total (never NaN);
  (2) gate messages now follow the CURRENT floor and read
  the same for both options (at the sample 75% floor they
  read exactly as the workbook's strings); (3) revenue/COGS
  labels follow the current term. Argon also caught an
  error in the prompt's own boundary note: at Term 1,
  Option B COGS is $22,600 and margin 73.4% per the workbook
  formulas (the prompt's prose said $23,800 / 72.0%) —
  Argon's figures verified independently and shipped.
- Verification (Muse): independent battery vs the workbook
  oracle — sample anchors exact, all four boundary cases,
  all-zero state, reset — 40/40 on displayed values; width
  ladder clean 280–1280; screenshots in both modes; law
  scans clean. Own additions by Argon: budget/margin
  headroom notes on the gate cards and a Quick Test
  Scenarios bar.
- The superseded workbook-embed build is archived:
  tool8-build/original-live-copy-2026-11-13/, GitHub branch
  tool-8-iterations, Drive mirror folder (data.js record).

## 2026-11-13 — THE QA PASS, CONSOLIDATED — what the pass before Tool 8 accomplished

- Tools 3 and 4 got their missing meta descriptions and
  canonical links — every page now describes itself to Google.
- robots.txt added: crawlers welcomed, pointed at the sitemap.
- sitemap.xml added: all 27 pages listed for Google in one file.
- Favicon live: the brass-and-navy D in every browser tab;
  link tags installed on all 52 page files.
- Custom 404 page live: a bad address returns a real HTTP 404
  on a real page, not a void.
- Security headers shipped in _headers (HSTS, nosniff,
  referrer policy, frame + permissions locks). Cloudflare
  applies 2 of 5 on the free pages.dev host; HSTS waits on a
  custom domain. No CSP — it would break the calculators'
  inline code; Argon's report-only CSP step awaits a ruling.
- Contrast fixed sitewide: the light grey failing at 2.46:1
  replaced with the passing slate at 5.10:1 (Argon's call).
- Photos set per the peer-reviewed research: the casual,
  smiling photo leads Homepage and About; the suit photo is
  a small secondary image on About only.
- Nothing shipped unverified: byte-diffs, the 240-check
  battery (Tool 3), anchor probes (Tool 4), the 10-width
  ladder on every page, live fetches on both hosts.
- Cloudflare, GitHub, and the Drive mirror carry the same
  bytes. Scoreboard: 8 findings — 7 closed, 1 partial
  (F7, platform limit). Detail in the wave entries below
  and Plans log 64–68.

## 2026-11-13 — QA job CLOSED: photo treatment live (Deliverables 8–9)

- Homepage (P01) + About (P03): the research-backed photo
  treatment is live on both hosts. The casual, smiling photo
  (assets/about-photo.jpg) now leads the Homepage Operator
  section (320) and the About page (240); the suit photo is
  off the Homepage entirely and sits on About only, smaller
  (180) and lower, alt "Joseph Conte in formal business
  attire". Argon's returns verified byte-identical outside
  the photo blocks (executor restored the in-file LABEL
  comments Argon had replaced with its manifest — both
  records now ride in the files); ladders clean; modes
  inherited undisturbed.
- With this, the Website QA Checklist fix program is COMPLETE:
  F1–F6 and F8 closed; F7 partially closed (platform limit,
  see wave 2 entry). Argon's closing inventory also delivered
  its CSP recommendation: (1) add a report-only CSP baseline
  permitting inline execution while locking external origins,
  object-src, base-uri, frame-ancestors, form-action;
  (2) a full enforced CSP only as a separate refactor that
  externalizes the tools' inline scripts/styles. Step 1 is
  awaiting Lucky's ruling; nothing was added to _headers.

## 2026-11-13 — QA fixes wave 2 (Argon master QA prompt, Deliverables 2–7)

- S6-P02 / Tool 4 (Spend Variance): meta description + canonical
  added (findings F1/F2 closed for this page); favicon link tags
  added. Contrast check: Tool 4's :root never carried #98A1AD —
  its light token was already the compliant value, so no token
  change. Everything else byte-identical (verified by full diff;
  live KPI anchors re-probed: $4,542,500 / $2,196,996 /
  $2,225,956 / $28,960, zero page errors).
- NEW root files, all live on Cloudflare: robots.txt (allow all
  + sitemap declaration — F3 closed); sitemap.xml (exactly the
  27 canonical URLs — F4 closed); 404.html in the site frame
  with absolute paths (live test: a bogus URL returns HTTP 404
  with this page — F6 closed); favicon.svg (Argon's design:
  navy field, brass rule, white D with brass counter; legible
  at 16px — F5 closed) + favicon link tags installed on every
  page of the site.
- _headers: the full safe set shipped (HSTS, nosniff,
  Referrer-Policy, X-Frame-Options SAMEORIGIN,
  Permissions-Policy). Live test: Cloudflare applies nosniff +
  Referrer-Policy on pages.dev but does NOT apply HSTS,
  X-Frame-Options, or Permissions-Policy from _headers on this
  host (HSTS is a zone-level setting — it needs a custom
  domain). F7 therefore stands PARTIALLY closed; the file
  itself is correct and complete for any future host.
- Still outstanding from the same Argon run: Deliverable 8
  (Homepage photo treatment) arrived truncated and Deliverable
  9 (About photo treatment) was never produced; a continuation
  is queued. The CSP recommendation Argon owed in its closing
  inventory is also outstanding with them.

## 2026-11-13 — Tool 3 QA fixes (Argon, master QA prompt, Deliverable 1)

- S6-P01.c / Tool 3 (Perm Calculator): meta description and
  self-referential canonical added (QA findings F1/F2 closed for
  this page); favicon link tags added (the icon file itself is a
  later deliverable in the same Argon run); the --text-light token
  darkened #98A1AD -> #5F6B7A per Argon's C4 contrast decision
  (5.10:1 on paper, was 2.46:1) with --grey-light declared at the
  same value. Everything else byte-identical to the prior build —
  verified by full diff, the 240-check battery (240/240), and a
  clean 10-width ladder sweep. Argon delivered the file in 3 parts
  (its own split); the parts were joined byte-clean by the
  executor and the join verified against the original.

## 2026-11-13 — Full-site proofread (spelling / capitalization / spacing)

- At Lucky's direction, a spelling + capitalization + spacing pass over
  every page's visible text. Result: ONE correction — "most-favoured-nation"
  -> "most-favored-nation" on S6-P03b / Tool 9 (US spelling; the workbook
  itself says "MFN clauses"). No capitalization errors and no rendered
  spacing errors found; every other candidate was a legitimate word, a
  proper name (David Tollen), a correct form (SaaS, SoW, LoL), or an
  abbreviation (U.S., vs.). Words and context untouched, per his scope.

## 2026-11-13 — Tool 7 REBUILT by Argon (QTC Diagnostic)

- Page/tool: S6-P05.3 / Tool 7 — Argon's full rebuild promoted,
  replacing the first-generation workbook-embed build (retired to
  the GitHub branch tool-7-iterations + local snapshot). Answers
  first: KPI strip (Readiness % · Earned of Max · P1 count),
  Needs a Decision (P1 stages worst-first, each with the
  workbook's finding & fix), the five-stage Scorecard (one-tap
  Maturity 0-3 and Risk Weight 1-3 segmented controls — no
  dropdowns), copyable QTC Readout + Reset. Measured context
  (cycle days, error rate) shown as static text, never scored —
  the workbook's own rule. Math UNALTERED from the workbook
  (declared in Argon's in-file manifest). ONE mechanical
  correction by the executor, authorized by Lucky as a defect
  fix: the "Clear All P1 Stages" preset label said 86% while
  the tool's own math produces 88% (37 of 42) — the label now
  reads 88%; Argon's manifest comment is untouched as the
  record of its claim. The first export Lucky received was a
  15 KB tail fragment (Argon crash); the complete 71 KB return
  followed and is what shipped. Verified before promotion:
  exhaustive battery — every Maturity x Risk Weight combination
  on every stage (60 probes) vs an independent oracle, KPIs and
  flags exact; boundaries (all Maturity 3 -> 100% / 42 / P1 0;
  Intake 0->3 -> 60% / 25 / P1 2; all-zero -> 0%); zero page
  errors; standing-law body scan clean; JSON-LD parses;
  width-ladder sweep zero overflow at all 10 widths on the new
  page and 27 of 27 pages sitewide after install; phone +
  desktop screenshots reviewed. Story 3 retired with the embed
  build (preserved in the archive). Argon improvements
  (declared in manifest): Raise-to-3 buttons on P1 decision
  cards, four-state preset test bar, per-stage headroom,
  pipeline jump bar, scoring rubric strip.

## 2026-11-13 — Tool 6 REBUILT by Argon (Redlining Playbook)

- Page/tool: S6-P05.2 / Tool 6 — Argon's full rebuild promoted,
  replacing the first-generation workbook-embed build (retired to
  the GitHub branch tool-6-iterations + local snapshot). Answers
  first: KPI strip, Needs a Decision (worst first), the full 8-clause
  Playbook Matrix verbatim, the Redline Scorer (one-tap segmented
  tier controls — no dropdowns), copyable Redline Brief + Reset.
  Hybrid style: bank frame, research voice. Math UNALTERED from the
  workbook (declared in Argon's in-file manifest). Verified before
  promotion: complete file DOCTYPE-</html>; sample data identical
  to the workbook; DOM battery — anchors 9 · 2 · ESCALATION
  REQUIRED - Finance/Legal · points 1,1,0,0,1,3,0,3 · escalation 2;
  32 combination probes vs an independent oracle, 0 mismatches;
  boundary states (all Tier 0 -> FAST-TRACK; CL-06 Tier 3 ->
  BLOCKED) pass; standing-law body scan clean (no prices, no sales
  copy, no "since 2006", no employer names, no Story 2 in the body);
  JSON-LD parses; width-ladder sweep zero overflow at all 10
  widths; phone + desktop screenshots reviewed. No story block —
  Story 2 retired with the embed build (preserved in the archive).
  Argon improvements (declared in manifest): matrix-scorer
  highlight sync, one-tap boundary preset bar, Give-Get surfaced
  in scorer rows, sticky live verdict bar.

## 2026-11-13 — Width-ladder defect fixes (Tier 1 library page, Tool 7)

- Pages/tools: S6-P06 tier-1 (/tools/contracts-library/tier-1/)
  and S6-P05.3 / Tool 7 (/tools/qtc-diagnostic/) — the first
  width-ladder sweep (all 27 pages x 280-1280 CSS px, real
  Chromium) found horizontal overflow on two first-generation
  pages. Tier 1: +7px at 320 (unbreakable preview strings inside
  the form cards). Tool 7: +27px at 280 (sheet tab wider than its
  strip; an unbreakable string in the Story 3 block). Fixed with
  page-local CSS only (overflow-wrap on card/prose text; tab cap
  + internal tab-strip scroll) — no copy, no design, no math
  changes; authorized by Lucky as mechanical defect repair.
  Re-sweep after the fix: 27 of 27 pages, zero overflow at every
  width, zero regressions. The sweep is now a standing item in
  the Argon Prompt Checklist (AFTER THE RETURN).

## 2026-11-13 — Tool 5 rename COMPLETED by Argon (Deal Desk Controls)

- Page/tool: S6-P05.1 / Tool 5 — Argon's completion build is
  promoted, superseding the executor's mechanical port (preserved
  in GitHub history and locally). Argon placed the Deal Desk
  Controls rename in its own design (badge, eyebrow, breadcrumbs,
  structured data; "Deal Desk Controls" x15 on the page) and
  removed a lingering start-date item from the base it was handed.
  Verified before promotion: complete file; zero prices / sales
  copy / "since 2006" / employer names in the body; sample data and
  logic identical to the workbook ground truth; DOM battery —
  anchors 5 · 2 · 40% · 2 · 1, DEAL-102 fix probe (3 · 60% · 1),
  DEAL-105 approval probe (unauthorized 2), reset restores, zero
  page errors; JSON-LD parses. Executor's promotion step was the
  standard mechanical conversion of Argon's 8 root-relative link
  targets to the site's relative scheme (targets unchanged).
  Partition links still resolve to /tools/stories-and-sandboxes/;
  the partition page, hub label, and URL rename in the pending
  story-removal pass.

## 2026-11-13 — S6-P05 partition renamed on Tool 5 (Argon naming)

- Page/tool: S6-P05.1 / Tool 5 — the S6-P05 partition is renamed
  from "Stories & Sandboxes" to DEAL DESK CONTROLS (Argon's first
  recommendation; alternates: Commercial Controls, Deal Governance
  — Lucky may veto, the swap is mechanical). Argon's return could
  NOT be promoted as delivered: the export was truncated mid-script
  (no closing </html>) and was built on the pre-correction page
  (280 diff lines vs the live file). The rename was therefore
  ported mechanically onto the verified live page: badge now
  "Tool 5 · Deal Desk Controls", a Deal Desk Controls level added
  to the visible breadcrumb and the JSON-LD BreadcrumbList, and
  applicationSubCategory set. Breadcrumb links still point at the
  partition's current address (/tools/stories-and-sandboxes/) —
  the partition page, the hub label, and the URL itself rename in
  a later pass once Lucky rules on the story-removal scope
  questions. Anchors re-verified after the port (5 · 2 · 40% · 2
  · 1); JSON-LD parses. Argon's full return incl. its manifest is
  preserved at tool5-build/argon-tool-5-rename-return.html.

## 2026-11-13 — correction (Lucky's ruling)

- SITE-WIDE: "corporate (roles) since 2006" RETIRED. Lucky's ruling
  (Nov 13): nobody prices a start date; the seniority is carried by
  years-in-the-line + scale. The clause was cut from the Tool 3,
  Tool 4, and Tool 5 provenance lines (and Tool 5's footer anchor
  strip) and from the Homepage + About roster lines, which now lead
  with the roster itself: "Eton, Reco, Apple, Raytheon, Meta,
  Google — with 15+ years in commercial contracts, deal desk, and
  revenue operations." The three-part field phrase was checked
  against the counted record (15y7m line: Reco contracts, Apple,
  Mailchimp, Raytheon procurement, Meta, Google Deal Strategy /
  Rev Ops) and stands as the accurate form — "revenue operations"
  alone would claim the procurement years, "operations" alone
  would undersell. Argon template Part B anchors updated so future
  builds do not reintroduce the date clause.

## 2026-11-13 — correction (Lucky's ruling)

- Page/tool: S6-P05.1 / Tool 5, S6-P02 / Tool 4, S6-P01.c / Tool 3,
  S6-P01.a / Tool 1 — NO-SELLING CORRECTION. Lucky's ruling (Nov 13):
  tool pages demonstrate; they never pitch — "does Apple ever say
  buy the iPhone on their page, or just demonstrate it and there's
  an option to buy?" All Deal Check sales copy stripped from the
  four tool pages that carried it: Tool 5's closing sales section
  ("When a Tool Is Not Enough", price tag, Book button), its
  price-tagged nav/footer links (now plain "The Deal Check" links),
  and the "Next Step" sales line inside the Gate Report output;
  Tool 4's "Commission The Deal Check ($6,500)" sentence; Tool 3's
  "The paid next step is…" paragraph; Tool 1's "Book the
  diagnostic" button + price note. Origin of the defect: the
  "tool pages end with the paid next step" idea was item 7 of the
  parked SPCL audit — a proposal Lucky never ruled on — which Muse
  hardened into the Argon template's Part A goal ("sell The Deal
  Check") and into Tools 3/4/5. Template Part A now carries the
  standing rule: demonstrate, never sell; the only commerce on a
  tool page is a plain descriptive link; pitch copy lives only on
  the Deal Check page and Services. Pages verified after the cut:
  anchors intact (Tool 5: 5 · 2 · 40% · 2 · 1, zero page errors),
  zero price/pitch strings on all four live routes.

## 2026-11-13 (later still)

- Page/tool: S6-P05.1 / Tool 5 — ARGON REBUILD (TOOL 5.1) replaces
  the workbook embed. First build under the standing Argon prompt
  template: goal (sell The Deal Check; the DEAL-103 audit-alert
  moment is the proof), bank/senior look rules, answers-first
  structure (KPI strip, Needs a Decision, editable gate log,
  copyable Gate Report + mailto report button), SEO per Google's
  published principles, the SEO-integrity never-list (no hidden
  text, no stuffing), and the Website QA Checklist as the build
  standard. Verified: anchors (5 · 2 · 40% · 2 · 1), per-deal
  routing, interaction battery (check flips move yield/routing;
  approving an 80%-ready deal fires the audit alert; delete-all
  safe; reset restores), zero page errors. Argon's Deal Check link
  (/the-deal-check/, a non-existent address) and its absolute
  internal links were corrected to the site's relative scheme at
  promotion (../deal-check/ etc.). Embed build deprecated as an
  iteration (see the Tool 4 entry pattern): local snapshot, GitHub
  branch tool-5-iterations, Drive archive folder. CODE-MAP v55.

## 2026-11-13 (later)

- SITE-WIDE CLOUDFLARE FIX: Lucky found Tool 5 (Intake Gate) 404ing
  on the Cloudflare host while the GitHub mirror served it fine.
  Cause: page folders carried only their ID-named HTML file;
  Cloudflare Pages needs an index.html in each folder to serve the
  directory URL. Only Tools 3 and 4 folders had one (both promoted
  by hand most recently). The publish tree's other index copies had
  been stripped by rsync --delete promotion passes mirroring site/
  (which lacked them), taking down every other route on Cloudflare,
  homepage included; the mirror masked it because GitHub batches had
  uploaded index copies all along. Fix: index.html copies generated
  from each folder's page file INSIDE site/ (25 created) so they are
  source files the sync can no longer remove; redeployed; all 27
  routes verified 200 with correct titles on Cloudflare.

## 2026-11-13

- Page/tool: S6-P02 / Tool 4 — CASCADE FIX (Argon). A 190-check
  combination battery found one defect: deleting a contract from the
  register removed its forecast group and invoices from view, but
  its forecast lines kept counting in the KPI strip, footer totals,
  REVIEW count, and Brief. Fix: totals count only contracts present
  in the register; deleting a contract removes its forecast lines
  and invoices entirely; editing a contract ID cascades to its lines
  and invoices. Verified 255/255 (battery extended with the delete
  and ID-edit cases plus the exact post-delete figures: YTD forecast
  $2,001,996, actual $2,034,731, REVIEW 3 / invoices 2). CODE-MAP
  stays v54.

## 2026-11-12 (later still)

- Page/tool: S6-P02 / Tool 4 — GROUPING REVISION (Argon, same day).
  Actual vs Forecast rebuilt as per-contract groups with subtotals
  (register generates the groups; empty contracts collapse to one
  compact line); Invoice Audit contract column is now printed text
  with a single add-time picker. Every per-row contract dropdown
  removed at Lucky's ruling (client usability: the contract is
  context, set once — a dropdown per row is a data-entry grid).
  Group subtotals verified: Apex +$3,530 (+0.7%), Northwind +$1,136
  (+0.4%), Cascade +$28,069 (+2.4%), Harborview −$3,775 (−1.9%);
  page anchors unchanged; sample data byte-identical. CODE-MAP
  stays v54.

## 2026-11-12 (later)

- Page/tool: S6-P02 / Tool 4 — Spend Variance & Renewal Tracker
  REBUILT (Argon). Control-board page replaces the workbook embed:
  sticky KPI strip, Needs a Decision exception list, editable
  register (notice window editable) / forecast (threshold editable) /
  invoice audit tables, copyable Portfolio Brief. Verified anchors
  unchanged: $4,542,500 · notices 6 · YTD variance $28,960 (1.3%) ·
  REVIEW 4 / 3. The workbook-embed build is deprecated as an
  iteration (GitHub branch tool-4-iterations; Drive archive folder;
  local snapshot in tool4-build/). CODE-MAP v54.

## 2026-11-12 — RESPONSIVE REVISION PROMOTED: Perm Calculator gains phone + desktop layouts; roster trimmed — Lucky's ruling
- Argon wrote the responsive pass (CSS only) and the trimmed intro paragraph; Muse executed and verified. One file, two shapes: phone <=760px single column with a compact totals strip; desktop >=1024px two-column workspace with strip card titles in full (the truncation is fixed).
- Roster rule applied (Lucky, Nov 12): the intro provenance paragraph names no employers — 15+ years in commercial contracts, deal desk, and revenue operations; corporate since 2006; contracts up to $300M; 3,000+ SKUs priced. The employer roster stays on the Homepage and About pages only. A full text diff confirms this paragraph is the ONLY words that changed on the page.
- Delivery, recorded honestly: Argon's return first truncated mid-script (94,534 bytes), then arrived in 3 parts with overlapping seams. Every part aligned verbatim against the proven script with zero gaps, and the assembled file is byte-identical to the independently built candidate (Argon's CSS + paragraph, proven script grafted), which had already passed the 240-check battery (240/240) and a live desktop browser pass (structure clean, totals $226,800 / $294,907.50 exact, Generate Note working, no page overflow).
- Design caveat, flagged to Lucky: at desktop width the Section 01 tables scroll sideways inside their card, so the PUPY / ACV / TCV columns start clipped. Built to the spec given; his call whether Argon gets a follow-up to fit the columns.
- Archival: the superseded wrapped build (3.3) joins the GitHub branch tool-3-iterations as the next iteration (branch README still pending Argon's writing); the candidate address /tools/perm-calculator-3-4/ is retired. Records: CODE-MAP v53; this entry; LABEL.md; Drive mirror + Page Text Sheet; Tool Review Checklist (3.3 row marked archived iteration, responsive build row added as adopted; verdict columns untouched).
- Page/tool: S6-P01.c / Tool 3 — Perm Calculator.


## 2026-11-12 — WRAP PROMOTED: Tool 3.3 (Argon frame + words, 3.2 tool core) becomes the Perm Calculator — Lucky's ruling
- Division of labor per Lucky's ruling: Argon writes (code and words), Muse executes and keeps the records. Argon's wrap adds the site masthead/footer, an intro led by the retained line 'One deal, structured several ways at once.', a how-it-works section with the plain-English factor gloss, the fictional-samples honesty line, and the Deal Check next step ($6,500, booking link). Every fact in the new words was checked against the approved record before publishing (15+ years, corporate since 2006 with the six named employers, $300M contracts, 3,000+ SKUs — nothing invented).
- Safety construction: the published file was built FROM the verified 3.2 core on disk — Argon's frame and words inserted around it, the three font alignments applied (body 16px/1.6, tool title weight 600, strip/picker labels sentence case) — so the tool's script is byte-identical to the tested build. Re-verified after wrapping: 240-check battery 240/240, JS syntax clean, live browser pass (frame order, totals exact, Generate Note, nav round-trip) clean.
- Font note (Lucky's catch): the families already matched the site (Georgia + the same system stack); what differed was treatment — 14px base vs the site's 18/1.6 pattern, title weight 400 vs 600, spaced-capital labels. Aligned in this build.
- Archival: the 3.1 / 3.2 / 3.3 candidate addresses are off the live site. The retired builds (workbook Tool 3, 3.1, 3.2) are preserved on the GitHub branch `tool-3-iterations` with a README lineage, in the Drive mirror, and in the local build records. The canonical page's provenance is stated on the page itself.
- Records: CODE-MAP v52; this entry; LABEL.md (perm-calculator); Plans tab -19 Log 49; Tool Review Checklist rows for 3.1/3.2 marked archived, new row for Tool 3.3 marked adopted (verdict columns untouched); Drive mirror S6-P01.c folder updated in the same pass.
- Page/tool: S6-P01.c / Tool 3 — Perm Calculator.


## 2026-11-12 — SWAP: Tool 3.2 (Argon build) replaces the workbook-converted Tool 3 at /tools/perm-calculator/ — Lucky's ruling
- Lucky reviewed all three live versions (Tool 3 workbook conversion, Tool 3.1 Argon build 1, Tool 3.2 Argon build 2) and ruled: 3.2 takes Tool 3's address 'if it works and you find no problems.' Verification before the swap: 240-check interaction battery across all 4 samples (every input tortured incl. $0/$1B prices, 0/1/1.5 factors, 1–120 month terms, −5%/250% growth, zero-unit usage) with ZERO page errors; usage math and the seat-growth model hand-verified to the cent; a live real-browser pass (load, Generate Note, price edit re-pricing to $341,870, sample switch to the $61,200 token commit) with no visible errors.
- What changed at this address: S6-P01c-perm-calculator.html + index.html are now the Tool 3.2 build (byte-identical to /tools/perm-calculator-3-2/). The retired workbook page + its data file are preserved (snapshot in the build records; data.js stays in the folder, unreferenced). Tools 3.1 and 3.2 keep their own addresses as the comparison record. Muse's only edit to Argon's code remains the version label (3.1 → 3.2, two spots).
- Records: CODE-MAP v51; Plans tab -19 Log 48; Tool Review Checklist rows for Tool 3 / Tool 3.2 updated (verdict columns untouched); Drive mirror S6-P01.c folder updated in the same pass.


## 2026-11-11 — About tenure line: 'Working since age 14.' opener cut (P03) — Lucky's order
- P03 About: the tenure line now opens with the corporate line — 'Corporate since 2006 — Eton, Reco, Apple, Raytheon, Meta, Google — with 15+ years in commercial contracts, deal desk, and revenue operations.' — matching the homepage hero (bank pass). No other About text changed.
- The fact itself is untouched (working since 14; 26 years total) — it simply no longer opens the page. A sourced research check on the opener's effect on senior presentation was commissioned the same evening at Lucky's request.

## 2026-11-11 — BANK PASS: the site looks like a bank; suit portrait leads (sitewide CSS; P01; P03; S6-P01.a CSS tokens) — Lucky's order
- Lucky's words: use the SUIT photo, and "make this look like a bank — the brand is power and change and law." He pasted an outside critique and ordered it done, with two of its suggestions REFUSED under his standing rulings: the hero solver stays a static preview (the live embed stays retired — his Nov 11 ruling) and no Conte-derived domain was touched (Conteworks scratched outright, same day).
- assets/styles.css (every page inherits): the D01 "Operating Manual" warm look is SUPERSEDED — warm cream paper and the deep-teal accent are out; deep institutional navy (#0F1E38) + restrained brass (#8A6D1F) on neutral off-white, squared geometry (radius 12/6px → 2px), flat frames (soft shadow removed), serif h3 joining the serif h1/h2, a navy masthead bar on the header, serif wordmark, navy primary buttons (brass is the accent, not the button), and a navy footer with a brass rule. New layout rules: `.op-grid` (operator portrait) and `.bucket-grid` / `.bucket` (homepage tools buckets). The D01 spacing and type scales did not move; workbook yellow-input / green-output colours are functional and unchanged. S6-P01.a's calculator CSS tokens (paper/ink/line/muted) moved to the same palette; its green stays — it marks positive results.
- P01 Homepage — hero tenure line: 'Working since age 14.' cut. The line now reads exactly: "Corporate since 2006 — Eton, Reco, Apple, Raytheon, Meta, Google — with 15+ years in commercial contracts, deal desk, and revenue operations. MBA." No '20 years' claim was made (the de-overlapped corporate record is 19 yrs 2 mos; 'since 2006' carries the span truthfully).
- P01 — hero solver caption reworded so it no longer implies the static card is typeable: it now says the card is a sample of what the solver returns, and the typing happens on the solver's own page.
- P01 — Section 06: the Tech Contracts Academy §C.3 disclaimer block came OFF the homepage. It remains publicly attributable on its proper page — S6-P06 Contracts Library already carries the §C.3 attribution/disclaimer under its lede, and every tier page carries the full label on every card. In its place on the homepage: a grid of ALL FOURTEEN tools under three buckets — Pricing & Margin (Deal Pricing Solver, Perpetual-to-SaaS Conversion, Perm Calculator, Cloud Commit & Usage Playbook, Bundling Sandbox) · Contract Risk & Redlining (Redlining Playbook, Contract Analyzer, Contract Migration & Triage Tracker) · QTC & Deal Governance (Spend Variance & Renewal Tracker, Intake Gate, QTC Diagnostic, Case Operations Triage Tool, Weighted Decision Scoring Tool, Executive Dashboard) — each linking its existing tool page; the one-line tool notes are drawn from the sitemap of record and the tools' own pages. (The brief for this pass said thirteen tools; Tool 14 landed earlier today and Lucky's pasted critique said fourteen — the grid carries all fourteen.) The three featured cards and the Contracts Library pointer stay as they were.
- P01 — Operator section: the suit portrait (assets/business-photo.jpg) at 320px in a two-column grid beside the credential text; the casual photo is off the homepage. P03 About: the same suit portrait leads at 240px; the casual photo is off the page; the small 'And when the room calls for it.' suit note (v47 furniture) is retired — the lead IS the suit now. This supersedes the v47 photo hierarchy (casual primary). assets/about-photo.jpg stays in the assets folder; no page presents it.
- NOT changed: Tool 3's design (parked review), the analyzer's AI key, any Review verdict, any other page copy. FLAGGED for Lucky's ruling, not changed: the About page still carries its own variant of the tenure line with the 'Working since age 14.' opener (the brief scoped the cut to the P01 hero).
- Records: CODE-MAP v49; this entry; LABEL.md (assets + about); Plans tab -19 Log 44; Tool Review Checklist P01/P03 status notes (verdict columns untouched); Drive mirror updated in the same pass (styles.css, P01, P03 code files; P01/P03 Page Text Sheets checked — they track headline boxes only, none in scope for the changed lines, same as Log 43 found). Cloudflare deploy via deploy_worker.py; GitHub mirror staged with a manifest (pending the browser-upload handoff, as before).

## 2026-11-11 — Seniority pass: tenure up front, 'nerdy' out (P01, P03) — Lucky's order
- P01 Homepage: tenure line added under the hero price note (working since age 14; corporate since 2006 — Eton, Reco, Apple, Raytheon, Meta, Google; 15+ years in commercial contracts, deal desk, and revenue operations; MBA); proof strip gained the $300M / 3,000+ SKUs / 300-page pricing wiki facts; identity photo 120px → 160px; Operator paragraph: 'sometimes nerdy' removed.
- P03 About: the same tenure line added after the background paragraph; 'sometimes nerdy' removed.
- Numbers counted from Lucky's LinkedIn profile (sent Nov 11, 2026): the commercial contracts / RevOps line Reco Jan 2008–May 2015 → Google Nov 2022–Jul 2024 = 15 yrs 7 mos; corporate since Eton (Mar 2006) = 19 yrs 2 mos with one gap (Jun 2015–Oct 2016); total working = 26 years since age 14. The old '9+' figure is retired.
- Copy discipline: this pass changes copy at Lucky's explicit order (his seniority ruling) — the standing words-untouched rule is overridden for these lines only.

## 2026-11-11 — Research applied: photo hierarchy (v47)
- Per Lucky's ruling on the peer-reviewed photo/attire research: homepage = casual photo only; About leads with the casual photo; the formal headshot moves to a small secondary note ('And when the room calls for it.'); both v46 captions removed. Name + LinkedIn/Book a Call furniture unchanged.

## 2026-11-11 — Identity pass: name + photo (Joseph Conte)
- About: identity block at the top of the story section (photo + name + role + LinkedIn + Book a Call). Homepage: the same block in the Operator section above 'More about the operator'. Photos: BOTH of Lucky's Nov 11 shots, side by side per his follow-up order ('the casual vs business guy') — casual denim photo as assets/about-photo.jpg ('In person') and the formal studio headshot as assets/business-photo.jpg ('In the boardroom'); square crops, 600×600, on both trees. styles.css gained .id-block rules. No locked copy edited.

## 2026-11-11 — Tool 14: Cloud Commit & Usage Playbook (S6-P01.d)
- New tool page at /tools/cloud-commit-playbook/ with the original sample workbook embedded (Discount Matrix / Renewal Check / Commit & Usage; ALLINPUT conversion; formulas hidden). Phone strip reads the asked discount's approver, the ratchet verdict, the deepest growing discount, the commit's effective discount, and the unused commitment.
- Provenance: built from the playbook STRUCTURE (governance first, gate second, levers third — mapped Nov 11 from Lucky's scrubbed deal-desk notes) and public CUD mechanics; no internal system, codename, KB text, real threshold, figure or SKU carried over. Every value is a labeled sample.
- Counts: 13 → 14 tools; 36 → 37 pieces (25 shown). Homepage strip, hub lede + P01 card, P01 partition page, SITEMAP-TABLE, MASTER-SITE-CHART, SECTION-6-CHART (count table reconciled to include Tool 13 as well), WEBSITE-CHART.html, CHART-ARROWS (regenerated, 43,876 B), folder charts regenerated.

## 2026-11-11 — Spacing pass + Contract Analyzer AI live (sitewide CSS; S6-P03.4 worker)
- Section padding cut from 64px (phone) / 96px (desktop) per side to 32 / 48 — the seam between stacked sections drops from 128/192px to 64/96px — per the Nov 11 spacing research (document design systems run 40–64px seams; NN/g flags wide gaps plus full-width hairlines as a false-floor risk). Hero keeps extra air (72px top on desktop); the homepage's closing section is marked final-cta (48 phone / 64 desktop). No words changed anywhere.
- The analyzer's AI read is switched ON: GEMINI_API_KEY set as a secret env var on the Pages project; the worker's Gemini model is gemini-3.8-flash with a gemini-3.1-flash-lite fallback (gemini-2.0/2.5-flash are refused to new users). Verified live end to end on the sample contract — summary, key terms, watch-outs and a missing list came back.

Lucky's rule (Nov 7, 2026): any change on any page is recorded here — date, page or file, what changed. A change is not finished until its label, the CODE-MAP, and this log are all updated in the same move.

## 2026-11-11 — Post-Tool-13 improvement loop (P04 + all pages)

- P04 / Tools hub — lede corrected: it still read "Twelve working tools, each one the actual workbook live on its page" after Tool 13 landed. Now: "Thirteen working tools, each one live on its page — the workbooks with inputs open and formulas hidden, every number the workbook's own math." The Tool 13 count update missed the hub lede, and the Contract Analyzer is not a workbook. His second sentence is untouched; this is the only page-text change in the pass.
- ALL PAGES (P01, P02, P03, P04 + every S6 page) — head pass: every page gained a canonical URL (Cloudflare primary host) and Open Graph tags (title / description / type / url) built from the page's own title and lede; the 22 pages that had no meta description gained one excerpted from the page's own lede. No claims added, no headings or body copy changed.
- Verified before deploy: dead-internal-link scan zero; meta scan complete on all 26 addresses; headless render audit of all 26 pages at 390px and 1440px — zero horizontal overflow, zero page errors, zero console errors; full visible-text proofread scan clean (no misspellings, no jammed words — "Tollen" is David Tollen of Tech Contracts Academy, a name, not a typo); the Perm Calculator's 65 #DIV/0! cells at defaults match a LibreOffice recalculation of the source workbook cell-for-cell in count (65) — the workbook's own values in its scenario space, not a site defect, and Tool 3's review stays parked.
- Cloudflare: deploy cb7f1aa7 via deploy_worker.py — stage success, worker preserved; live read-backs confirm the corrected lede, the new head tags, and /api/analyze answering (400 on too-short text, 501 not_configured on full text — the AI provider key remains Lucky's hand only).
- GitHub mirror: NOT updated in this pass — no authenticated route exists in this environment (prior uploads went through the signed-in browser flow). Pending on the mirror, precisely: the whole tools/contract-analyzer/ folder (index.html, S6-P03d-contract-analyzer.html, S6-P03d-analyzer.js — the shared analyzer assets jszip/pdf.js ARE already there), the updated tools/contract-operations/ page (its Analyzer card), and this pass's 74 changed HTML files (hub lede + head pass) across the repo tree. The changed files are staged with a manifest in the run log.
- Records: CODE-MAP v43; this entry; Plans tab -19 log + Tool Review Checklist updated in the same pass where the routes allow (see the run log for any step that had to be flagged instead).

## 2026-11-11 — Tool 13 — Contract Analyzer (S6-P03.4) + /api/analyze endpoint
- S6-P03.4 (new page, /tools/contract-analyzer/): Lucky's Oct 2025 Streamlit contract-analyzer MVP rebuilt as a native site tool (Lucky's order: Tool 13, full build, working AI, sitemap + folder + records). Layer 1: the original six scans ported exactly (engine S6-P03d-analyzer.js) — verified output-for-output vs the Python original on the repo sample, quirks included. Layer 2: 33 coverage checks (Basics / Money / Risk / Data & IP / Operations / Legal), FOUND with excerpt or NOT FOUND — verified 33/33 on a full contract, zero false positives on plain prose. Layer 3: the AI read — publish/_worker.js adds POST /api/analyze (Gemini/OpenAI/Anthropic key from the project's secret env vars; 501 not_configured until a key is set, page says so plainly).
- Extraction runs in the browser: DOCX via self-hosted JSZip 3.10.1 (byte-identical output to the Python extractor on the sample), PDF via self-hosted PDF.js 3.11.174. Scanned-image PDFs do not read — same limit as the original; stated on the page.
- Wiring: SITEMAP-TABLE row S6-P03.4 added; counts updated (13 tools; 36 pieces, 24 shown; 18 Section 6 folders) in SITEMAP-TABLE, MASTER-SITE-CHART, SECTION-6-CHART, WEBSITE-CHART; hub card text + a Contract Operations partition card link the tool; homepage proof strip 12 → 13. New project folder s6-p03-4-contract-analyzer with PAGE.md; folder charts re-run; LABEL.md written.
- Records: CODE-MAP v42; Plans Log 36; Tool Review Checklist + Site Build Checklist gain the Tool 13 rows.

## 2026-11-11 — P01 homepage hero rebuild + header/footer unification (P01, P02, S6-P01.a)
- P01 (homepage): the hero's live Deal Pricing Solver embed is replaced by a static preview card — the workbook's own labels and default sample outputs (ARPU 158.4, 12 months → PUPM $13.20; solved List Price $10,000.00; Discount 25.00%; Partner Margin 15.00% / $1,200.00) — with a "Run the solver" button to /tools/deal-pricing-solver/. The workbook, its data file and the tool page are untouched. The homepage no longer loads the workbook data/engine/renderer scripts.
- Why: Lucky's report ("the tool immediately on the side is wrong") + deep research (hero research report, Nov 11) + measured recheck: hero section 3,668px tall on desktop; on a 390px phone the homepage rendered 694px wide, clipping the headline and buttons. After: phone renders exactly 390px; desktop hero 819px.
- P01, P02 (Services), S6-P01.a (Tool 1): headers unified to the site-standard header (Home / Services & Pricing / Proof of Work / Book a Call) and footers to the standard one-liner — the three pages were the only variants left. The publish homepage was re-synced from the site source, retiring three stale "Opening with the full site" placeholders (S6-P02 and S6-P05.3 cards, operator link).
- Copy: no page text changed. Verified: full-site phone-overflow audit — all 25 pages clean; dead-link scan zero; screenshots at phone + desktop read.
- Records: CODE-MAP v41; P01 label comment updated; Plans Log 35.

## Entries

- **2026-11-11 (ALL TOOLS — TEST PASS FIXES: text-input clipping, Tool 2 chart legend, header button contrast)** — Lucky ordered every tool tested for function and looks. All twelve passed functionally (typing drives the outputs on each; zero page errors at phone and desktop widths; Tool 2's full engine comparison re-run: zero differences). Three display defects were found in the visual review and fixed: (1) text inputs in the sheet grids were fixed at 112px and clipped long labels ("Baseline submission gate…" showed as "Ba") — the renderer now sizes text inputs to their content and styles.css left-aligns them; the workbook values and math are untouched. (2) Tool 2's chart legend printed its series-name formulas verbatim (="SaaS "&$B$23&…) — the converter now resolves series titles to their values (cached value first, concatenation evaluated when no cache exists) and Tool 2's data file was regenerated; the only change in it is the three legend names, now "SaaS Option A/B/C — cumulative cost ($)". (3) The "Book the diagnostic" header button showed dark text on teal because the nav-link color rule outranked the button rule — styles.css pins the button's white text inside the nav. All fixes verified in fresh screenshots and re-deployed to both hosts. CODE-MAP v40.

- **2026-11-11 (S6-P06 + S6-P06.1/.2/.3 — ADAPTED CONTRACTS LIBRARY BUILT AND LIVE)** — Build-the-rest pass, part 3. The library home at /tools/contracts-library/ and its three tier pages are real pages: 15 annotated cards in total (5 per tier), each carrying the analyst note verbatim from Draft 1.11 Part II, a preview made of the form's own title lines and opening text (extracted from its ADAPTED_SAMPLE docx; the source header and adaptation header are not shown), and the full §C.3 adaptation label with the attorney line. Cards and previews only — no form is downloadable, per the library's PAGE.md rules. The Consulting Services card keeps the form's own warning that the paper is not friendly to the customer, as its tier PAGE.md requires. Verified in a real browser at phone and desktop widths: 5 cards, 5 labels, 5 previews per tier page; the home page links all three tiers. Same pass: the hub page's Adapted Contracts Library card now links to the library, and the homepage's adapted-forms sentence now points at the library instead of the Deal Pricing Calculator. CODE-MAP v39.

- **2026-11-11 (S6-P03.1 — THE DEAL CHECK BUILT AND LIVE, WITH ITS EMAIL-GATED DOWNLOAD)** — Build-the-rest pass, part 2. The page at /tools/deal-check/ shows all six steps on the page (Draft 1.11 Part II verbatim) plus the inputs/logic/limits note, per the page's own PAGE.md. The download is email-gated exactly as that PAGE.md's hard pre-publish rule requires — the call to action never points at nothing: the on-page form posts the visitor's email to Lucky's Google Form "The Deal Check — Checklist Download" and only then reveals the checklist PDF (the source checklist docx, converted). The gate was verified end to end before publish (a test submission is recorded in the form's responses; the reveal was exercised in a real browser at phone width). Same pass: the Contract Operations partition page's Deal Check card now links to the page. D01 OPEN 1 stays Lucky's to rule on — if he rules against the gate, removing it is a one-line edit; the build followed the page's PAGE.md. CODE-MAP v39.

- **2026-11-11 (P03 — ABOUT BUILT AND LIVE)** — Build-the-rest pass, part 1. The About page at /about/ is built to its sitemap line (Section 1 long version: photo, first-person story, external links): Draft 1.11 Part II copy verbatim — the Section 1 block, The Mess I Fix, How I Work, The Work Behind It (Google / Meta / Raytheon), The deal with no way forward, and What I Want Handed to Me — with Lucky's own photo (assets/about-photo.jpg) and LinkedIn + booking links. No new copy was written. Same pass: the homepage publish copy and Tool 1's publish copy carry their About links again (nav, story link, footer) — the Option B trim from when /about/ was unbuilt no longer applies; the site sources were never trimmed. Verified in a real browser at phone and desktop widths (photo loads, zero page errors). CODE-MAP v39.

- **2026-11-11 (HUB + PARTITION PASS — SECTION 6 HOME AND THE FOUR PARTITION PAGES BUILT AND LIVE)** — After the twelve tools landed, the site's routes were finished: the Proof of Work hub at /tools/ and the Pricing Engines, Stories & Sandboxes, Contract Operations, and Executive Intelligence partition pages are now real pages in the shared design system — a card per piece, linking every live tool. Unbuilt pieces (the Adapted Contracts Library, the Deal Check, the back drawer) appear as unlinked cards marked "Not yet published," per the Option B rule that only what exists gets linked. Card copy comes from the sitemap of record and the tools' own pages. The pass also fixed two leftovers it caught: the Perm Calculator's SITEMAP row still read "Draft" (now Built — live), and Tool 1's publish copy carried two links to the unbuilt /about/ page — trimmed in the publish copy only, the standing Option B practice, leaving the site source untouched. A scripted scan of the whole publish tree now finds ZERO dead internal links. Every page the site's navigation promises now exists: home, services, the hub, four partitions, and all twelve tools.

- **2026-11-11 (S6-P04.b / Tool 12 — EXECUTIVE DASHBOARD BUILT AND LIVE; THE TWELVE-TOOL SET IS COMPLETE)** — Completing Lucky's push-the-rest order. The page embeds the actual Executive Dashboard (SAMPLE) workbook — 4 tabs (README, Case Data, Executive Dashboard, Regional Performance), 447 cells, 109 of the workbook's own formulas — under a write-up built from the dashboard's own inputs/logic/limits note and the workbook README. PROVENANCE, stated on the page: this workbook is an EQUIVALENT SAMPLE built in October 2026 to pair with the Executive Dashboard portfolio PDF — the original dashboard was built inside a CRM system and no workbook version existed; the workbook's own README says so. The CRM's raw case export behind the original is not in this workbook and is never displayed; the Case Data tab is the sample's own illustrative register of 36 cases, labeled sample data in the file itself. Definitions are kept in each workbook's own words: this dashboard's backlog counts Open + In Progress and says so in its label — narrower than the Case Operations tool's not-Closed count (S6-P03.3), and the page names the difference instead of blending them. The shared engine gained AVERAGEIF for the regional rollups (criteria-matched averaging; an error in a matching row propagates; no matches is #DIV/0!), and Tool 2 was re-verified clean after the addition (5,954 comparisons, zero differences). Open cases age against TODAY() exactly as the workbook's formulas do, so ages, breaches and averages move with the calendar — stated on the page. A phone summary strip above the tool — the same pattern as Tools 2 and 4–11 — repeats the dashboard's seven headline KPIs from the same typed values. VERIFIED: engine vs a LibreOffice recalculation — defaults plus five scenarios (a status flip, a region move, an SLA target raise, a fractional target, hostile values) — ZERO differences in 109 compared formulas per scenario, 654 comparisons. Real-browser tests at phone and desktop widths: strip defaults exact (Total 36, Backlog 21, Escalated 3, Escalation rate 8.3%); reopening a closed case moves the backlog to 22 and the breach count with it; zero page errors. With this entry, all twelve Section 6 tools from the Nov 5 plan are built and live: Tools 1–3 (Pricing Engines), Tool 4 (Spend Variance), Tools 5–8 (Stories & Sandboxes), Tools 9–10 (Contract Operations), Tools 11–12 (Executive Intelligence).

- **2026-11-11 (S6-P04.a / Tool 11 — WEIGHTED DECISION SCORING BUILT AND LIVE)** — Continuing Lucky's push-the-rest order. The page embeds the actual Weighted Decision Scoring Tool (SAMPLE v2) workbook — 2 tabs (Decision Scoring Tool; Worked Example — Vendor Eval), 173 cells, 28 of the workbook's own formulas — under a write-up built from the workbook's own seven how-to steps and its inputs/logic/limits notes. PROVENANCE AND FRAMING, stated on the page in the workbook's own terms: the workbook implements the documented framework from the Weighted Decision Framework document — 8 criteria weighted 30/20/15/12.5/10/5/2.5/5 = 100%, scores normalized 0 to 100 with higher meaning better on every criterion — and it is NOT a "50-30-20" tool. The vendor evaluation sheet is a worked example of the method on generic sample vendors, not a record of any real procurement; its Weight cells are live formulas linked to the main sheet, so the example cannot drift from the framework. The shared engine gained SUMPRODUCT (text and blanks inside its ranges count as 0, errors propagate, per Excel) and classic RANK (ties share the top rank) for this workbook. One verification finding, recorded rather than smoothed over: a constructed scenario that made two composites exactly equal in decimal arithmetic (93.975) ranked them differently in the engine and in LibreOffice, because the two sum the same products to opposite sides of the tie at the 1e-14 level — probed directly: literal tied values rank identically (1, 2, 2) in both, and the formula-level disagreement is the same one Excel and LibreOffice have with each other on exact ties. The weight-shift scenario was set to 45% so the verification measures semantics, not float noise. VERIFIED: engine vs a LibreOffice recalculation — defaults plus five scenarios (a weight shift that breaks the 100% check, a score sweep, a main-sheet weight change followed through the vendor sheet's linked weights, fractional weights and scores, hostile values) — ZERO differences in 28 compared formulas per scenario, 168 comparisons. Tool 2 re-verified clean after the engine additions (5,954 comparisons, zero differences). A phone summary strip above the tool — the same pattern as Tools 2 and 4–10 — repeats both sheets' composites and result lines from the same typed values. Real-browser tests at phone and desktop widths: strip defaults exact (A 75.5, B 85.2, C 65.5; vendor example Sample Vendor A 82.6); typing a weight of 45% fires the workbook's own WARNING line in the sheet body and re-ranks both sheets live; zero page errors.

- **2026-11-11 (S6-P03.3 / Tool 10 — CASE OPERATIONS & CAPACITY BUILT AND LIVE)** — Continuing Lucky's push-the-rest order. The page embeds the actual Case Operations Triage Tool SAMPLE workbook — 4 tabs (README, Case Register, Backlog & SLA Dashboard, Capacity Simulator), 460 cells, 118 of the workbook's own formulas — under a write-up built from the page plan and the workbook's own notes. PROVENANCE, stated on the page: this workbook is an EQUIVALENT SAMPLE built in October 2026 to pair with the portfolio PDF "Case Operations Snapshot — Backlog & SLA Risk" — the original workbook was not in Drive, and the workbook's own README says so; the Capacity Simulator tab states on its face that it is a planning model built for this website and that nothing in it is measured data. One correction is carried in this website-build copy and the dashboard names it in its own note: the Backlog KPI counts every case not Closed — 18 of the 30 sample cases — matching the by-region table; the narrower count that disagreed with that table in an earlier version is fixed. The register's Age column and SLA Flag (BREACH when age exceeds the target) are formulas; open cases age against TODAY() exactly as the workbook's formulas do, so ages, breach counts and the average age move with the calendar — the page says so plainly rather than freezing a screenshot's numbers. The shared engine gained COUNTIFS for this workbook (its by-region counts use range/criteria pairs), and every earlier tool was re-verified after the addition (Tool 2: 5,954 comparisons, zero differences; Tool 3: six scenarios of 6,099, zero differences with the one known residual). A phone summary strip above the tool — the same pattern as Tools 2 and 4–9 — repeats the dashboard's totals and the simulator's capacity and net-clearance figures from the same typed values. The workbook's own date formats (yyyy-mm-dd) and its 0% format were mapped for display only. VERIFIED: engine vs a LibreOffice recalculation — defaults plus six scenarios (a status flip to Closed with a close date, an SLA target raise, capacity strain, a capacity boost, fractional throughput, hostile values including a Closed case with no close date) — ZERO differences in 118 compared formulas per scenario, 826 comparisons. Real-browser tests at phone and desktop widths: strip defaults exact where date-independent (Total 30, Backlog 18, Effective capacity 9.6/day, Net +3.6/day) and equal to the dashboard where date-dependent; a status flip drains the backlog 18 → 17; intake pushed past capacity flips Net to −2.4; zero page errors.

- **2026-11-11 (S6-P03.2 / Tool 9 — CONTRACT MIGRATION & TRIAGE TRACKER BUILT AND LIVE)** — Continuing Lucky's push-the-rest order. The page embeds the actual Migration Tracker SAMPLE workbook — 5 tabs (README, Migration Tracker, Approval Routing, RACI Matrix, Exception Log), 220 cells, 9 of the workbook's own formulas — under a write-up built from the build spec's corrected directions (SPEC — Migration Tracker.md). PROVENANCE, stated on the page: this workbook is an EQUIVALENT SAMPLE built in October 2026 to pair with the Contract Migration & Deal Desk Transformation Framework portfolio PDF — the framework itself is a document and no workbook version existed; the workbook's own README says so. The site build's enhancement (adopted Nov 5, 2026) is presented exactly as the workbook carries it: typed metadata columns (Governing Law, Effective Date, Auto-Renewal, Liability Cap) and a Tier column the USER assigns, with count-by-tier formulas below the rows. The page states plainly that metadata is recorded by hand — nothing extracts terms from contract documents — and that Tier is the operator's judgment, never auto-claimed by the tool. The only live logic is the Risk Flag (At Risk → REVIEW, Complete → Done, anything else → Monitor) and the tier counts; the Approval Routing and RACI tabs are static reference tables and the Exception Log is a record. There is no dashboard or velocity roll-up in the workbook and the page promises none. A phone summary strip above the tool — the same pattern as Tools 2 and 4–8 — repeats the workbook's own tier counts and tallies the sheet's own Risk Flag values from the same typed values, because the tracker is fourteen columns wide. The workbook carries no number formats and none were needed; its dates are text in the file and stay text. VERIFIED: engine vs a LibreOffice recalculation — defaults plus four scenarios (status flips across all three flag outcomes, a tier reassignment, mixed-case statuses — Excel's text equality is case-insensitive and the engine matches, hostile values including a numeric status and a bogus tier) — ZERO differences in 9 compared formulas per scenario. Hand anchors at defaults: flags Monitor / Monitor / REVIEW / Monitor / Monitor / Done; tier counts 3 / 2 / 1. Real-browser tests at phone and desktop widths: strip defaults exact; Status → At Risk flips the flag in the sheet body to REVIEW and the strip tally to 2; a Tier reassignment recounts live (4 / 2 / 0); zero page errors.

- **2026-11-11 (S6-P05.4 / Tool 8 — COMMERCIAL RESTRUCTURING & MARGIN BUNDLING SANDBOX BUILT AND LIVE)** — Continuing Lucky's push-the-rest order; this completes the S6-P05 Stories & Sandboxes set (Tools 5–8 all live). The page embeds the actual Bundling Sandbox SAMPLE workbook — 1 tab, 84 cells, 28 of the workbook's own formulas — under a write-up built from the build spec's corrected directions and Story 4's own words (Business Problem, Solution, Operational Impact). PROVENANCE, stated on the page: this workbook is a sample built for the site in the Argon batch, not one of Lucky's original work files; it was verified in the Section 6 restart and the directions are the spec's corrected directions, pasted in. The visitor sets the buyer's budget ceiling, the margin floor, and the contract term, then works the per-line levers (quantity/seats, annual list, unit COGS, discount %); each option is gated live — PASS only when its total revenue fits the ceiling AND its margin clears the floor. The source's deliberate quirk is preserved and stated on the page: each option's implementation line is a one-time item whose revenue and cost carry no term multiplier (Option B's implementation line honestly shows a −60% margin at sample values — that is the model's own math, left as the file has it). The workbook carries no number formats, so the conversion assigns display formats only (dollars, percents) — a format-only patch verified to change zero values and zero formulas. A phone summary strip above the tool — the same pattern as Tools 2 and 4–7 — carries both options' totals, margins, and gate verdicts computed from the same typed values, because the verdict columns sit at the far right of a ten-column sheet. VERIFIED: engine vs a LibreOffice recalculation — defaults plus six scenarios (term 3→5 years, ceiling raised, floor dropped to 60%, Option A discount fixed to 20%, fractional inputs, hostile values with nine matching error cells — a text quantity poisons Option A's totals to #VALUE! exactly as LibreOffice does, under the aggregate-propagation rule landed with Tool 7) — ZERO differences in 28 compared formulas per scenario. Hand anchors at defaults: Option A $234,000 revenue, 66% margin, FAIL – BELOW 75% MARGIN FLOOR; Option B $250,000 — exactly at the ceiling — 76% margin, PASS – HITS BUYER BUDGET & CLEARS 75% FLOOR. Real-browser tests at phone and desktop widths: strip defaults exact; Option A discount 48%→10% with the ceiling raised to $500,000 re-prices the sheet body (net $270, revenue $405,000, margin 80.37%) and flips its gate to PASS; zero page errors.

- **2026-11-11 (S6-P05.3 / Tool 7 — QTC DIAGNOSTIC & BOTTLENECK SCORECARD BUILT AND LIVE)** — Continuing Lucky's push-the-rest order. The page embeds the actual diagnostic SAMPLE workbook — the Section 6 restart's verified v2 build: 2 tabs (QTC_Audit_Scorecard, Diagnostic_Summary_Dashboard), 90 cells, 24 of the workbook's own formulas — under a write-up built from the build spec's corrected directions and Story 3's own words (The Problem, What This Piece Shows, How a Buyer Uses It, The Point It Proves). Five stages, one control point each in the sample: maturity (0–3) × risk weight (1–3) gives the weighted score, health % and the P1–P3/PASS priority flag follow the workbook's rules, and the Dashboard rolls earned points vs max into the Overall QTC Readiness % with the P1 bottleneck count. The workbook's two optional context columns (actual cycle days, error rate %) are read by NO formula — the page's Inputs section says so, as does the workbook's own note under its table. Display formats: the workbook's one formatted column (error rate %, at 0%) maps to whole-percent display; the Health % column carries no format in the file and displays as the raw decimal, exactly as the sheet does. A phone summary strip above the tool — the same pattern as Tools 2, 4, 5, 6 — carries the Dashboard verdict (earned points of max, readiness %, P1 count) computed from the same typed values. ENGINE CORRECTION (assets/formula-engine.js): the hostile scenario caught SUM returning a partial total (0.083 readiness) where LibreOffice returns #VALUE! — an Excel error cached as a cell VALUE inside a summed range was skipped as a non-number, while an error arriving by throw propagated, so results depended on evaluation order. SUM, AVERAGE, MIN and MAX now throw a cached error value the moment an aggregate touches it, matching Excel/LibreOffice; COUNT (ignores range errors) and COUNTA (counts them) were probed against LibreOffice and already match, so they stand. One behavior consequence, stated plainly: on Tool 4, letters typed into a forecast cell now also turn the Dashboard cells that SUM that column to #VALUE! — which is what Excel itself shows — instead of the Dashboard keeping a partial total. VERIFIED: engine vs a LibreOffice recalculation — defaults plus five scenarios (all stages mature, all maturity zero, all risk weights low, fractional scores, hostile values with five matching error cells) — ZERO differences in 24 compared formulas per scenario. Full regression after the engine change: Tool 2 5,954 comparisons ZERO fails; Tool 3 six scenarios × 6,099 ZERO fails except the one documented text-digit residual, unchanged; Tool 4 1,344 ZERO fails; Tool 5 200 ZERO fails; Tool 6 245 ZERO fails. Hand anchors at defaults: earned 16 of max 42, readiness 38%, P1 bottlenecks 3 (Intake, Pricing, Redlining). Real-browser tests at phone and desktop widths: strip defaults exact; Intake maturity 0→3 moves its row's weighted score 0→9 and flag P1 → PASS, strip to 25 of 42, 60%, 2 P1s; Dashboard tab repaints to agree; zero page errors.

- **2026-11-11 (S6-P05.2 / Tool 6 — REDLINING PLAYBOOK & CLAUSE FALLBACK MATRIX BUILT AND LIVE)** — Lucky's order ("push the rest of the tools… test it mobile and desktop view, make it understandable but do not shrink it"). The page embeds the actual Redlining Playbook SAMPLE workbook — 2 tabs (Playbook_Matrix, Deal_Redline_Scorer), 115 cells, 35 of the workbook's own formulas — under a write-up built from the build spec's corrected directions and Story 2's own words (The Problem, What This Piece Shows, How a Buyer Uses It, The Point It Proves). PROVENANCE, stated on the page: this workbook is a sample built for the site in the Argon batch, not one of Lucky's original work files; it was verified in the Section 6 restart and the directions are the spec's corrected directions, pasted in. The page also states the sample standards are illustrative governance architecture, not legal advice and not any client's actual positions. The workbook carries no number formats and none were needed — tiers and risk points display as the plain numbers they are. A phone summary strip above the tool — the same pattern as Tools 2, 4, and 5 — carries the scorer's verdict (Total Redline Risk Score, Highest Tier Requested, Overall Routing Decision) computed from the same typed values, because the verdict rows sit at the bottom of the second tab. ENGINE ADDITIONS (assets/formula-engine.js): the scorer's formulas use CHOOSE and a range MAX, which the engine did not have. CHOOSE added with Excel semantics (index truncated to an integer; below 1 or past the last value is #VALUE!). MIN/MAX corrected: they used to coerce each argument, so MAX over a range read only its first cell — a latent bug no earlier tool's formulas had exercised; they now collect every number in a range the way SUM and AVERAGE do. VERIFIED: engine vs a LibreOffice recalculation — defaults plus six scenarios (all tiers standard, all walk-away, one walk-away at CL-06, all escalation, fractional tiers, hostile values 5 / −1 / text / blank with four matching #VALUE! error cells) — ZERO differences in 35 compared formulas per scenario. Full regression after the engine changes: Tool 2 5,954 comparisons ZERO fails; Tool 3 six scenarios × 6,099 ZERO fails except the one documented text-digit residual, unchanged; Tool 4 1,344 ZERO fails; Tool 5 200 ZERO fails. Hand anchors at defaults: risk points 1+1+0+0+1+3+0+3 = Total 9, Highest Tier 2, ESCALATION REQUIRED – Finance/Legal. Real-browser tests at phone and desktop widths: strip defaults exact; CL-06 tier 2→3 flips its approver to STOP: Walk-Away Boundary and its points to 10, strip Total 16, Highest 3, BLOCKED – Walk-Away Redline; all tiers to 0 → Total 0, FAST-TRACK; desktop matrix renders all eight clauses; zero page errors.

- **2026-11-11 (S6-P01.c / Tool 3 — PHONE FIX: TAB GUIDE + COMPILED-TOTALS STRIP; workbook untouched)** — Lucky's report: the Perm Calculator "looks really clunky," "seems broken," "not doing that on my end," with his bettering notes (ES-to-E+ tab names too vague/Google-specific; lots of blanks; combinations never visible side-by-side while working). DIAGNOSIS at phone width, three findings: (1) The live page itself recalculates correctly — verified in a real browser (OPT 2 list price 30→45 re-prices the row 24→36, zero page errors) — but the phone PREVIEW file circulated earlier still inlines the pre-fix renderer, and typing in it throws ("Cannot read properties of undefined") and nothing moves; the preview has been regenerated with the current assets and re-verified (typing re-prices, strip live, zero errors). (2) The option grids are 38–51 columns wide, so at phone width the answers sit far off-screen — typing visibly does nothing, which reads as broken. (3) The rendered grids are 89% empty cells — not empty rows but the model's own sparse layout: a handful of live lines spread across many columns; that emptiness is the workbook's real working space and was left exactly as the file has it. FIXES (page only): a plain-English TAB GUIDE ("How the 22 tabs fit together") above the workbook — what each tab group is, and ES → E+ spelled out as the file's shorthand for the standard edition → the plus edition — and a PHONE SUMMARY STRIP carrying the Compiled Results headline totals (OPT 1 TCV; OPT 2/3/4 current → proposed; OPT 4's proposed is the 60-month figure), computed live from the same workbook data through the shared engine and re-synced as the visitor types in any tab (200 ms debounce — this is the 6,100-formula workbook). The guide's last line names the empty space as the model's working space. VERIFIED: strip defaults equal the workbook's Compiled totals ($176,800; $1,453,140 → $1,716,336; $1,182,672 → $1,855,188; $1,182,672 → $5,563,980); real-browser phone test — OPT 2 row 24 → 36 on typing; an edit in the "OPT 2 (35% discount)" tab (B37 list price 30→45) moves the strip's OPT 2 proposed TCV $1,716,336 → $2,489,940; zero page errors. Review 1 remains PARKED for Lucky's rested review (reminder stands).

- **2026-11-11 (S6-P05.1 / Tool 5 — INTAKE GATE & SUBMISSION SCORECARD BUILT AND LIVE)** — Lucky's order ("build 5 now — same things for tools 1-4: mobile vs desktop and so on"). The page embeds the actual Intake Gate SAMPLE workbook — 2 tabs (Intake_Gate_Log, Triage_Dashboard), 103 cells, 25 of the workbook's own formulas — under a write-up built from the build spec's corrected directions and Story 1's own words (the Problem, What This Piece Shows, How a Buyer Uses It, The Point It Proves). PROVENANCE, stated on the page: this workbook is a sample built for the site in the Argon batch, not one of Lucky's original work files; it was verified in the Section 6 restart and the directions are the spec's corrected directions, pasted in. The workbook carries no number formats, so the conversion assigns display formats only (ACV as dollars, discount and readiness as percentages); no value or formula was changed. A phone summary strip above the tool — the same pattern as Tools 2 and 4 — carries the Triage Dashboard KPIs (total deals, clean first-pass + yield %, held at gate, unauthorized approvals) computed from the same typed values, because the Dashboard is the last tab. VERIFIED: engine vs a LibreOffice recalculation — defaults plus seven scenarios (an approval without baseline, a discount over 20%, a clean fast-track, a finance routing, hostile values including a lowercase "approved" and a non-Y/N check letter, blanked inputs, text flow): ZERO differences in 25 compared formulas per scenario. Hand anchors at defaults: DEAL-101 100% OK FAST-TRACK; DEAL-103 40% AUDIT ALERT STOP – REVOKE & AUDIT; Dashboard 5 deals, 2 clean, 40% yield, 2 held, 1 unauthorized. Real-browser typing test at phone width: F4 Y→N moves readiness 100%→80%, routing to HOLD, strip clean 2→1, yield 40%→20%, held 2→3; K4→Approved fires the AUDIT ALERT, unauthorized 1→2; Dashboard repaints to agree exactly; zero page errors.

- **2026-11-11 (S6-P02 / Tool 4 + shared engine — ERROR-AS-VALUE FIX; found by the Tool 4 typing fuzz)** — Lucky's order: when a visitor types letters where a number belongs, the tool should SHOW the error the way a spreadsheet does. The fuzz found the crack: letters in a forecast cell threw an uncaught "Error: #VALUE!" behind the scenes — the numbers still landed right, but a throw is a throw. Root cause: the engine raises spreadsheet errors as thrown exceptions (its number-coercion helper throws #VALUE!), and the public `get()` let the throw escape. The page's sheet inputs parse typed values themselves (letters become 0 there), but the phone summary strip stores the raw text into its own engine copy, so its Dashboard formulas hit the throw and the strip's recalculation died mid-pass. FIX (assets/formula-engine.js, one place): `get()` now catches thrown Excel errors (#VALUE!, #DIV/0!, #NUM!, #REF!, #N/A, #NAME?) and returns them as values, so the cell DISPLAYS "#VALUE!" while the rest of the sheet keeps calculating — exactly Excel's behaviour; genuine engine bugs still throw. The Tool 2 phone strip's money formatters were also guarded (a non-number now shows "—", never "$NaN"); Tool 4's strip already had that guard. VERIFIED: Tool 2 full comparison re-run (458 × 13 scenarios = 5,954, ZERO fails); Tool 3 (6,099 × 6 scenarios, ZERO fails except the one documented text-digit residual in the scratch sheet's E2, pre-existing and unchanged by this patch); Tool 4 (defaults + 6 scenarios + 12 randomized fuzz workbooks = 3,648 comparisons, ZERO fails). Engine-level proof of the fix: with text forced into the Actual vs Forecast forecast cell, the variance $ and % cells now return "#VALUE!" as values while the Dashboard still totals correctly ($73,960, 3.4%, 4 REVIEW lines). Real-browser DOM checks: Tool 4 letters case — zero page errors, numbers recover when a number is typed back; Tool 2 B15="abc" → $90,000, zero errors; Tool 3 OPT 2 A13 30→45 → 24→36 exact, zero errors.

- **2026-11-11 (S6-P02 / Tool 4 — SPEND VARIANCE & RENEWAL TRACKER BUILT AND LIVE)** — Lucky's order ("push tool 4 — same explain, mobile vs desktop, test for crashes"). The page embeds the actual Contract Spend Variance & Renewal Tracker workbook — 5 tabs (README, Contract Register, Actual vs Forecast, Invoice Audit Log, Dashboard), 668 cells, 465 live inputs (every non-formula cell is typeable, as in the real sheet), 192 formulas — under the Draft 1.11 write-up (intro, directions, inputs/logic/limits verbatim). SHARED ASSETS GREW, small and additive: the formula engine learned TODAY() (the Dashboard's renewal count is COUNTIF(notice dates, "<="&TODAY()+90)), and the renderer learned the workbook's own display formats ("$"#,##0 as money0, yyyy-mm-dd as dateiso, 0.0% as pct1). A phone summary strip above the tool — the same pattern as Tool 2's — carries the Dashboard KPIs live from the same typed values, because the Dashboard is the last tab and its totals would otherwise sit far from the typing. VERIFIED: engine vs a LibreOffice recalculation — defaults plus six scenarios (spend changes, invoice changes, a register change, hostile zeros and negatives, fractions, blanked inputs): ZERO differences in 192 compared formulas per scenario. CRASH TESTS: the hostile and blanked scenarios above, plus a real-browser typing test at phone width (Actual vs Forecast E2 set to 99,999: variance $54,999, 122.2%, flag flips OK to REVIEW; the summary strip and the Dashboard tab agree to the dollar; zero page errors), and a browser regression pass on Tools 2 and 3 after the shared-asset changes (their verified anchors reproduce exactly; zero page errors).

- **2026-11-11 (assets / spreadsheet-tool.js — RENDERER RECALC FIX; found while building the Tool 3 demo video)** — The demo capture typed into the Perm sheet in a real browser and the answers did not move. Cause: each input's typing listener read the variables `c2` (the cell) and `input` (the box) at event time — but both are row-scoped vars that keep being reassigned while the rest of the row is built, so by the time a visitor typed, the listener aimed at the row's last column: it threw ("Cannot read properties of undefined") when that column was empty, and would have written into the wrong cell when it was not. The sheet body of every embed tool (S6-P01.b Tool 2, S6-P01.c Tool 3, and the P01 homepage hero) therefore never recalculated from typing; Tool 2's phone summary strip computes separately from the typed values, which is why numbers moved there and masked this. Tool 1's separate designed calculator does not use this renderer and is not affected. FIX: each listener now captures its own cell address, format, and element at build time. VERIFIED in headless Chrome against the publish tree: Tool 3 OPT 2 list price 30→45 — after-margin 24→36, paying ratio 0.55→0.37, actual discount 0.45→0.63 (all exact); Tool 2 term 60→24 months — stay-put total $190,000→$136,000 exactly, options moved with it; zero page errors on both pages. Redeployed to both hosts and the Drive mirror in the same pass.
- **2026-11-11 (S6-P01.c / Tool 3 — PERM CALCULATOR BUILT AND LIVE; the Pricing Engines trio is complete)** — Lucky asked for the Tool 3 run-through, ruled on its presentation ("we do both. Fuck the insiders that want to control anyway"), and said "show me when you are done." The page embeds the actual scrubbed workbook — 22 tabs, 10,748 cells, 4,368 live inputs (every non-formula cell is typeable, exactly as in the real sheet), 6,100 formulas — under a write-up taken from the sheet's own START HERE. THE ENGINE AND RENDERER GREW for this build (shared files; Tool 2 re-verified clean after every step, and its data file is byte-identical under the changed converter): cross-sheet references with a workbook resolver; TEXT(), CONCATENATE, ISBLANK, ROUNDUP, TEXTJOIN, ROW, SMALL; 1-D array evaluation for the sheet's 114 array formulas (the Summary Pattern list extraction that feeds every option tab's summary block); Excel's empty-cell semantics probed against LibreOffice and matched exactly (a bare reference to an empty cell reads 0 as a value but still equals "" — and a whitespace-only cell is real content: a single space in the summary list is an entry, and dropping it shifted the extraction by one until the converter stopped discarding it); error values now propagate through text the way a spreadsheet's do; Google Sheets' empty function arguments (TEXT(x, )) parse; numbers convert to text at Excel's 15 significant digits. THE CONVERTER gained ALLINPUT mode, date/time serials, and array-formula handling. VERIFIED: engine vs a LibreOffice recalculation of the workbook — defaults plus five scenarios (price/margin changes, a months change, summary-form text flow, hostile values, blanked inputs): ZERO differences in 6,099 compared formulas per scenario. Two residuals, documented: LibreOffice cannot evaluate TEXTJOIN (the engine follows Sheets semantics — an all-empty range joins to ""); and at defaults one scratch-sheet text cell differs from the source export's stale cached string, where a fresh recalculation agrees with the engine. THE GLOSS: the workbook's factors stay exactly as the file has them (0.65 means 35% off — the real model's dialect), and the page translates every factor live beside its input, in plain words — 301 factor inputs mapped from the sheet's own labels: discount columns read "— that's 35% off", partner-margin columns "— the partner keeps 20%".
- **2026-11-10 (S6-P01.b / Tool 2 — WORKBOOK v12: DECIMALS FLOW)** — Lucky's ruling on the v11 build: "Why is it rounding — let it use decimals and let it work like a spreadsheet?" Fair: the term inputs were still being rounded to whole months and days before the math saw them, and a spreadsheet never does that to an input. v12 removes the ROUND from both term inputs everywhere they feed the totals, per-seat, and readouts (58 occurrences each), and widens the days field to 7,300 days so a term can be stated in days alone ("400 days" now computes directly). The 20-year cap on the total term stands, and the pro-rata machinery underneath — whole years plus the leftover fraction of the next year — already spoke fractions, so nothing else in the math changed. The phone strip stopped rounding the typed term as well and prints it as entered. Verified: engine vs LibreOffice, 458 formulas × 13 scenarios (the full v11 regression set plus 30.5 months, 47.5 days, 13.25 months, 7.7 months + 13.3 days, 400 days alone, past-cap decimals, and a 0.1-month + 0.25-day sliver) = 5,954 comparisons, zero differences; the 34-scenario hostile fuzz re-run, zero divergences; hand anchors exact (30.5-month stay-put total $145,750; 47.5-day stay-put total $15,356.16). The only rounding left in the workbook is the seat counts — seats are whole people, and that rounding is part of the model itself (since v4), not an input being corrected.
- **2026-11-10 (S6-P01.b / Tool 2 — WORKBOOK v11: THE TERM IS SET IN MONTHS AND DAYS)** — Lucky's correction, from his Google deal-desk practice: contracts are calculated by months and days, not whole years — a "2.5-year horizon" is how nobody writes a term; a 30-month term with 47 extra days is. The years-only horizon input is now **Term — months** (0–240; the default is 60, the same 5-year sample, so every published and quoted number is unchanged) plus a **Term — extra days** input (0–364) placed on the one free row above the year table (no rows were inserted — the build rule). The four totals now compute: whole years read off the twenty year columns, plus the leftover part-year charged **pro-rata at the next year's cost** (months as twelfths, days as days/365 of that year). Cost-per-seat rows read the seats of the year the term ends in; the stay-put per-seat-per-month readout divides by the true term. Guards: a term past 20 years reads as 20; a zero term reads 0 in every result. Two rounding corners were found and fixed during verification: LibreOffice rounds −0.5 away from zero where JavaScript rounds toward zero, which made the whole-year count differ at exactly term 0; and a guard keyed on the year count alone let a sub-year term evaluate INDEX(…,0) in a real spreadsheet — both guards (year count AND term) are now in all four totals. Every "horizon" word in the sheet became "term" (steps text, Limits note, side notes, result and summary labels — only the provenance note's history keeps the old word), and the phone summary strip now reads "At your term — 30 months + 47 days" from the same result cells. Verified: engine vs LibreOffice on 458 formulas × 12 term scenarios (60m; 30m; 90 days only; 18m; 24m+47d; 71m+364d max stub; 240m+146d past-cap guard; zero term; 7m; 240m; 1m; 13m) = 5,496 comparisons, zero differences; the 34-scenario hostile fuzz re-run, zero divergences; LibreOffice identity vs v10 at the default — the only differing cell is the term input itself (5 → 60); hand anchors exact: 30-month stay-put total $145,000, 90-day $29,095.89, 24 months + 47 days $138,317.81.
- **2026-11-10 (S6-P01.b / Tool 2 — WORKBOOK v10: TEXT SWEEP)** — The GitHub upload verifier's read-back of the live v8 page caught what the widening pass missed: two instruction texts inside the sheet still spoke from the five-column era — the Limits note ("the table shows Years 1 to 5, so set the horizon between 1 and 5") and the horizon input's side note ("How many years to compare. Use 1 to 5."). Both now state the true range ("Years 1 to 20… between 1 and 20"; "Use 1 to 20 (a fraction rounds to the nearest whole year)"). A full-sheet sweep for stale range language found nothing else live: the only other matches are the v7 sentence inside the provenance note (history, accurate as history) and the fixed 5-year summary rows / Year-5 readouts, whose labels describe Year 5 and remain true. No math changed — the defaults engine-vs-LibreOffice comparison re-ran at 458/458. Lesson filed next to the INDEX one: when a range changes, sweep the sheet's WORDS for the old range, not just its formulas.
- **2026-11-10 (S6-P01.b / Tool 2 — WORKBOOK v9 + SIMULATION SWEEP ON BOTH TOOLS, Lucky's order)** — After approving Tool 2 ("approved for now" — Review 1: Temporarily approved), Lucky ordered full self-run simulations on both tools before Tool 3. TOOL 1: 20,000 randomized cases through CALC + the formatters — no throws, every internal invariant holds, and no output ever renders as NaN or ∞. CLEAN. TOOL 2: an every-horizon sweep (1–20; totals and per-seat values internally exact at each) plus a 34-scenario hostile fuzz against LibreOffice — negative growth to −2, discounts to 150%, list prices at 0 and negative, seat counts 0 / 1 / 1,000,000 / negative, coupons dwarfing the deal and negative, garbage and empty usage-type text, empty and symbol-laden option names, migration discount at 0% / 100% / 150% / negative, license at 0 / negative / $1B, and a combined chaos case. ONE break: a **fractional horizon (2.5)** reached the year INDEX as a fraction — LibreOffice truncates it to Year 2, but the page printed **#DIV/0!** in the cost-per-seat rows and blank totals. Fix (v9): the clamp now rounds first — MIN(MAX(ROUND($B$17,0),1),20) in the same nine places — so the sheet, the page, and the phone strip (which already rounds) read a fraction identically; the Inputs note states the rule ("a fraction rounds to the nearest whole year"). Verified: LibreOffice identity vs v8 at the defaults (zero differences); the 10-scenario engine-vs-LibreOffice comparison re-run (4,580 comparisons, zero differences); the full 34-scenario fuzz re-run — ZERO divergences.
- **2026-11-10 (S6-P01.b / Tool 2 — WORKBOOK v8: THE HORIZON TRULY RUNS 1–20 YEARS)** — Lucky overruled the v7 clamp ("I want everything to at least be 1–20 years — fuck the clamp"), so the sheet itself was widened: the year table grows from five year columns to TWENTY (columns B–U; the old column G was empty, so nothing had to move). Every year-driven row — year costs, cumulative rows, difference rows, the break-even and run-rate-crossover helpers, and the seats-by-year table — was extended by its own formula pattern; every year range in the result cells was widened to column U; the chart's series and categories now plot all twenty years; sheet merges and column widths follow. The horizon input reads "Horizon (years, 1–20)" and the v7 clamp survives only as a guard at those stated ends (above 20 reads as 20, below 1 as 1), so no horizon a visitor can type produces a silent zero again. The fixed Year-5 readouts and the 5-year summary rows still read Year 5, exactly as their labels say. The phone summary strip runs the same 1–20 range. Verified: LibreOffice recalculation of v8 vs v7 at the defaults — zero value differences across the whole original footprint; hand anchors at horizon 20 exact (stay-put total $460,000 = the $100,000 license + 20 × $18,000 maintenance; Option A seats at Year 20 = 764 = ROUND(125 × 1.1^19)); the horizon-20 totals equal the Year-20 cumulative column to the dollar; the site formula engine vs LibreOffice on all 458 formulas × 10 scenarios (defaults; all renamed; mixed growth 0%/20%/5%; horizons 3, 7, 12, 20, 25, 1, 0) = 4,580 comparisons, ZERO differences. Data reconverted (749 cells, 38 inputs, 458 formulas).
- **2026-11-10 (S6-P01.a / Tool 1 — ACCURACY AUDIT, Lucky's order: "accuracy is everything for these")** — Tool 1 got the same hostile treatment Tool 2 just failed. The math core (CALC) was hammered in node: the model's worked examples reproduce exactly (Net PUPM $13.20, PUPY $158.40, ACV $15,840 at 100 seats, after-coupon $15,340), every zero-divisor in the solvers and percent-change functions returns NaN (which the page renders as —), and no function throws on extreme inputs (zeros, negatives, >100% discounts, zero months). ONE real bug found, in the display layer: a per-token usage line with zero billed units (units and committed minimum both 0 — e.g. a visitor clearing both fields) showed **"$NaN"** as its per-token price. Fixed: the per-token cell now shows — when there is no billed unit to price. Hardening in the same pass: the money and percent formatters treated Infinity as a printable number ("∞"); they now render — for any non-finite value. CALC itself is byte-identical after the pass, so every prior numeric verification stands unchanged.
- **2026-11-10 (S6-P01.b / Tool 2 — WORKBOOK v7: THE HORIZON CAN NO LONGER ZERO THE TOOL)** — Lucky set the horizon to 20 years and every total on the page went to 0. Cause, found in the workbook's own formulas: the totals and cost-per-seat rows pick their year column with INDEX(range, horizon) — the sheet carries five year columns, so a horizon of 20 (or 0) indexes outside the table, and the browser formula engine reads an out-of-range INDEX as 0 (in Excel the same cell shows #REF!). Fix, in the workbook itself so Excel, LibreOffice and the page all agree: the eight horizon-indexed formulas now read MIN(MAX($B$17,1),5); the input is labeled "Horizon (years, 1–5)" and the Inputs note states the range and the read-as rule. Verified: LibreOffice recalculation of v7 vs v6 at the defaults — zero value differences anywhere; the site formula engine vs LibreOffice on all 218 formulas × 7 scenarios (defaults; all renamed; mixed growth 0%/20%/5%; horizon 3; horizon 20; horizon 1; horizon 0) = 1,526 comparisons, ZERO differences — at horizon 20 the tool now returns the 5-year numbers its label promises. The phone summary strip (mobile pass) clamps its horizon identically. Data reconverted (479 cells, 38 inputs, 218 formulas). Standing lesson recorded for every future embed tool: any input a workbook uses as an INDEX must be clamped inside the workbook, because the engine reads out-of-range as a silent 0.
- **2026-11-10 (S6-P01.a / Tool 1 + S6-P01.b / Tool 2 + shared assets — MOBILE PRESENTATIONS, per Lucky's ruling)** — Lucky asked whether his phone was the real reason Tool 2 felt unclear, had the question researched (sourced answer: the gap is scrolling + how little is visible at once, not the device; responsive re-presentation is the recommended pattern), and ruled: "if we're doing it for 1 tool we have to do it for all" — a mobile version and a desktop version for each tool. Built as ONE codebase per tool with the SAME numbers: every mobile rule lives inside a max-width media query, so desktop rendering is byte-for-byte the old rendering. (1) TOOL 2 (S6-P01.b page + shared `assets/styles.css`): on phones the workbook stays a real table (comparisons side-by-side) with the LABEL COLUMN STICKY while the year columns scroll, a scroll-hint shadow on the frame edge, inputs at 44px tall / 16px type (full tap targets, no focus zoom), the chart frame scroll-safe — and a SUMMARY STRIP above the sheet, phone-only, results first: each path's total at the visitor's horizon, its cost per seat, and its final-year seats. The strip is computed by a small page script from the SAME workbook data through the SAME formula engine and re-syncs on every input change — node-verified: defaults render exactly the sheet's numbers ($190,000 / $181,620 / $212,544 / $136,100; $1,520.00 / $992.46 / $1,161.44 / $1,088.80 per seat; 125 / 183 / 183 / 125 seats), a growth change to 30% moves the strip to the sheet's new values, a rename flows through. The P01 homepage hero embed inherits the shared mobile block automatically. (2) TOOL 1 (S6-P01.a page + its scoped calculator CSS): tables keep their real columns inside their scroll frames with the SKU NAME COLUMN STICKY, 44px tap targets (inputs, selects, delete buttons), scroll-hint shadow, and a STICKY TOTALS BAR pinned to the bottom of the phone screen showing the active view's totals (New Deal: seat TCV after coupons + full deal TCV; Old vs New: the new deal's ACV/TCV + the TCV change) — fed by a page script that only READS the calculator's rendered outputs; the calculator's math (CALC) is untouched, so its verification stands. (3) Both phone previews rebuilt. CODE-MAP v18 in this same change.
- **2026-11-10 (S6-P01.b / Tool 2 — v6: SEAT GROWTH MADE VISIBLE, per Lucky's Review 1 feedback, + the "Next" separator fix)** — Lucky, ruling on Tool 2: the tool was not clear about seat growth, about options whose seats stay the same, or about moving back and forth between deals; and the page's closing label still read "Next Put." (1) WORKBOOK v6 built from v5 by coordinate rebuild (+12 rows at row 77): a SEATS-BY-YEAR table under the cost table — stay-put's flat licensed seats and one row per option, using the same ROUND(start × (1+growth)^(year−1), 0) seat math the cost rows already price, so what a visitor sees is exactly what is priced — plus COST-PER-SEAT-AT-HORIZON rows (each total divided by the seats served in the final year). (2) SAMPLE CHANGE: the third option's seat growth is now 0% (flat, seats stay the same) next to two options growing at 10%, so the sample itself shows both shapes; its year costs go flat at $28,800 and its 5-year total lands on $136,100 — exactly the v3 flat-subscription total, to the dollar. Options A and B are untouched, so the numbers quoted in the How to Sell SaaS doc (Option B $212,544, 183 seats, ~$1,161/seat) stand. (3) PAGE: one mechanics sentence added (the seats-by-year table + the flat sample), and the closing section label now reads "Next — Put this to work on a real decision." with an em-dash separator; Tool 1's page, calculator JS and CSS were searched — no "Next" instance exists there, nothing to fix. VERIFIED: LibreOffice, shift-aware v6-vs-v5 — 143 mapped cells identical, the only changes being the intended Option C values and the three note appends; seat table hand-checked (125/138/151/166/183 growing, 125 flat; cost per seat at horizon: Stay put $1,520.00, A $992.46, B $1,161.44, C $1,088.80); site engine vs LibreOffice on all 218 formula cells × 4 scenarios (defaults; all three options renamed; mixed growth 0%/20%/5%; horizon 3) = 872 comparisons, zero differences. Data reconverted (479 cells, 38 inputs, 218 formulas). CODE-MAP v17 in this same change.
- **2026-11-09 (S6-P01.a / Tool 1 + S6-P01.b / Tool 2 — SKU NAMES EDITABLE, per Lucky's direction)** — Lucky, reviewing the live tools: the SKU names must be editable in both tools. TOOL 1 (calculator JS + page): the SKU name box now LEADS each product line (table headers, all 3 product tables: "SKU name (editable)" / "Preset") and picking a preset no longer wipes a name the visitor typed — a preset fills the name only while it is empty or still shows the previous preset's name (the pick still fills the list price). Usage-line names were already editable and are unchanged. CALC math untouched; re-verified against the model's worked examples (net PUPM $13.20, PUPY $158.40, ACV and coupon and usage checks pass). TOOL 2 (workbook v5, built from v4 by coordinate rebuild, +3 rows): three option-name INPUT cells top the seat block ("Option A / B / C" as the sample values), and ALL 68 labels that name an option — subscription lines, seat/usage inputs, year table, results, summary, crossovers, readouts — are now formulas carrying the typed name, so renaming an option renames it everywhere on the sheet; names are labels only. VERIFIED: LibreOffice — all 27 key numbers identical to v4, all 68 labels render exactly v4's strings at default names; site engine vs LibreOffice on all 188 formula cells × 4 scenarios (defaults; all three options renamed; growth 0%; horizon 3) = 752 comparisons, zero differences; live rename check: "Core Platform" flows into the readouts, Option A 5-year total unchanged at $181,620. Page + LABELs + publish copies + previews refreshed; CODE-MAP v16 in this same change.
- **2026-11-08 (S6-P01.b / Tool 2 — typo fix, Lucky's catch)** — "NextPut": the conversion page's "Next" section label was jammed against its heading ("Put this to work on a real decision") with no space. Space restored in source + publish + both hosts + Drive mirror. A scan of all four built pages for jammed words found no other instances (only real words like SaaS / PowerPoint flagged). Lucky's standing rule recorded in the build checklist + memory: after all 12 tools are built to the T, the whole site gets a full spelling/grammar pass — a page is not finished on math alone.
- **2026-11-08 (S6-P01.b / Tool 2 — v4: seats & PUPM, the upsell rebuild, per Lucky's direction)** — Lucky's ruling: Tool 2 must carry a good reason for companies to UP the TCV and spend more (the Google way — upsell), and seats/units are core factors because so much relies on PUPM and seat costs. (1) WORKBOOK v4 built from v3 (v3 stays on file) by coordinate rebuild (+14 rows): each SaaS option is now seat-driven — list price per seat per month, discount % → net PUPM, starting seats, seat growth %/yr (seats rounded to whole numbers each year); the three flat subscription inputs became DERIVED outputs (starting seats × net PUPM × 12) and reproduce v3's $30,000 / $36,000 / $27,000 exactly; stay-put keeps license + maintenance and gains a licensed-seats input. (2) NEW READOUTS BLOCK: net PUPM per option ($20.00 / $24.00 / $18.00), seats at Year 5 (183 each at 10% growth), Year-5 run rates ($45,120 / $52,704 / $41,328), stay-put effective cost per seat per month ($25.33) — headed by the framing note Lucky asked for: TCV up because the rollout grows, cost per seat down; Option B's 5-year total ($212,544) now passes stay-put ($190,000) precisely because it serves 183 seats instead of 125, at a lower per-seat price. (3) v3's factors all kept: coupon credits, usage lines, break-even, crossover, chart; notes copy (how-to, logic, limits, provenance, summary) updated. (4) PAGE: data reconverted (427 cells, 35 inputs, 120 formulas), label + LABEL.md updated, mechanics paragraph now tells the seats/PUPM story. VERIFIED: LibreOffice 36/36 hand checks; engine vs LibreOffice 120 formulas × 5 scenarios (defaults; growth 0%; Option A seats doubled to 250; horizon 3; Option C growth 25%) = 600 comparisons, zero differences; growth at 0% reproduces v3's totals to the dollar — v4 is a strict extension of v3. CODE-MAP v15 in this same change.
- **2026-11-08 (S6-P01.b / Tool 2 — v3: the Tool 1 factors, per Lucky's directive)** — "I want both tool 1 and 2 and possible everything related to it to keep all these factors in mind." (1) TOOL 1 AUDIT (S6-P01.a / Tool 1): the Deal Pricing Calculator already carries the full factor set — coupons per line, usage lines in both views (per use / per API request / per 1K / per 1M tokens), usage-threshold concession — no code change needed; the naming is locked in the prompt template: "usage" is the umbrella word, tokens are one unit type inside it. (2) TOOL 2 WORKBOOK v3: "Perpetual-to-SaaS Conversion Calculator — SAMPLE v3.xlsx" built from v2 (v2 untouched) by coordinate rebuild — each SaaS option gains a one-time coupon credit (Year 1 only; samples A $1,500 / B $0 / C $2,500) and a usage line (type, units per month, price per unit, usage discount, committed monthly minimum; A per-1M-tokens with the $100/mo minimum binding, C per-1K-tokens with $150/mo binding); cost formulas extended, four new results lines (annual usage per option + combined coupon credits), notes copy updated (how-to, logic, limits, provenance, summary). (3) PAGE: data reconverted (332 cells, 25 inputs, 107 formulas, chart series on the shifted cumulative rows), label comment + folder LABEL updated to v3, one mechanics sentence added to the page's second paragraph. VERIFIED: LibreOffice recalc 19/19 headline checks (stay-put $190,000; A Year 1 $23,700 → 5-year $148,500; B $172,800 unchanged; C Year 1 $20,900 → $136,100; difference at horizon $41,500; break-evens + crossovers all Year 1) and the site formula engine vs LibreOffice on all 107 formula cells × 5 scenarios (defaults; Option A $45,000; horizon 3; metered-binds; per-use) = 535 comparisons, zero differences. (4) THE FACTORS STANDARD written into PROMPT-TEMPLATE-deal-pricing-calculator.md Part 2 as rule 7 (both filed copies). CODE-MAP v14 in this same change.
- **2026-11-08 (S6-P01.a / Tool 1 + S6-P01.b / Tool 2 — Tool ID labels + the Tool Review Checklist)** — Lucky's review system, built on his instruction: (1) TOOL REVIEW CHECKLIST sheet created — "Tool Review Checklist — Site Tools (Nov 8, 2026)" (Google Sheet 1Lxw56_jX0DS47qaVH55SiTTAjnlJzjLuYeUfZp4Wz4U, in the Website build folder): 26 rows — every page, partition, tool and piece with Page ID, Tool/Piece ID, what it is, Cloudflare URL, status, and horizontally expanding Review columns; Review 1 for S6-P01.a / Tool 1 reads "Temporarily approved" (Lucky's words) dated 2026-11-08. Review order ruled by Lucky: tools first, in Tool ID order; homepage/services noted as built, checked later. (2) TOOL ID LABEL LINES added to both built tool pages ("Tool / piece ID: Tool 1 — Deal Pricing Calculator" in S6-P01a's label comment; "Tool 2 — Perpetual-to-SaaS Conversion Calculator" in S6-P01b's), publish copies refreshed, redeployed to BOTH hosts and verified in the GitHub repo. (3) The Standing Build Checklist gained steps 7–8: update the Review Checklist sheet on every build pass, and every CHANGELOG entry names the page ID + tool/piece ID it touches.
- **2026-11-08 (launch night, close)** — CLOUDFLARE LIVE: https://fractional-deal-desk-site.pages.dev — BOTH HOSTS UP, as ruled. How it finally went through: Cloudflare's bot check rejects Muse's cloud browser on every sign-in route (Google SSO bounced twice even after Google accepted the re-saved password — "Unable to sign in. Try again or use your email and password."), so the browser door was abandoned and the deploy went through Cloudflare's API with a token Lucky created on his own laptop ("Muse Pages Deploy", Account · Cloudflare Pages · Edit, no expiration, no IP filter), handed over through the secure connector (custom.cloudflare). Project created + all 42 publish files deployed via the direct-upload protocol; verified live by reading the pages: homepage (full copy + prices), /services/ (locked prices intact), /tools/deal-pricing-solver/ (calculator page), /tools/perpetual-to-saas-conversion/. New deploy path recorded in the Cloudflare connector doc — future deploys run the same helper, no browser. CODE-MAP updated to v13 in this same change.
- **2026-11-08 (later, launch night)** — GitHub Pages verified end to end after the relative-links upload (35 commits): homepage renders styled (warm off-white / navy / teal), nav clicks land correctly under the subpath (Services & Pricing, Deal Pricing Calculator — no 404s), calculator computes the verified defaults (PUPM 13.20, TCV $114,048 / ACV $28,512, full deal TCV $144,442.99, expansion 22.11 / 18.09). Two flagged items checked and CLOSED by direct source/live inspection, no fix needed: (1) the wordmark links are already relative in the shipped files (services ../, solver ../../) — the browser run's residual claim traces to the pre-rebuild cache it hit at 18:26 PT; (2) the Services numbers it quoted ($9,500 / $11,700) are menu lines (CPQ Readiness $9,500 etc.) — the locked phase/retainer prices are intact and verified on the live page ($6,500 / $5,000 / $4,500–$25,000 / $4,000–$7,500–$12,500, hero $7,500). Lesson kept: verify a subagent's residual flags against the source before acting on them.
- **2026-11-08 (launch night)** — SITE LIVE on GitHub Pages: https://thecozymerc.github.io/fractional-deal-desk-site/ (repo github.com/thecozymerc/fractional-deal-desk-site, 42 files incl. the sitemap skeleton + GITHUB-MAP). Same pass: every internal link and asset path in the 4 built pages switched from root-absolute (/services/, /tools/...) to relative paths, in BOTH the site sources and the publish copies — the site now works identically at a root domain (Cloudflare) and under the GitHub Pages subpath. Cloudflare Pages itself is still pending: the thecozymerc.sf@gmail.com Google password saved in the vault was rejected by Google ("Wrong password"), the same rejection recorded Oct 28-29; Cloudflare cannot be signed into until Lucky corrects it, resets it, or signs in himself. CODE-MAP updated to v12 in this same change.
- **2026-11-08 (PROMPT TEMPLATE for the calculator — Lucky's instruction)** — "Create a prompt template for this first calculator so that we can make the exact thing next time easily… and log it in the right folder for the right page." Built `PROMPT-TEMPLATE-deal-pricing-calculator.md`: Part 1 the reusable prompt (fill-in brackets: sources, math identity, views, line types — products with editable names + add/delete, usage built into both views, coupons, usage-threshold concession, rule checks — sample-data rules, D01 design, file pattern, companion workbook, records); Part 2 the rules that never change (sources first, nothing invented, scrub internal names, formulas never displayed, one-pass build, verify page-vs-sheet); Part 3 the acceptance tests — S6-P01.a's actual verified numbers (13.20; 30/45/20; 28,512; 46,800.86/140,402.59; after-coupon 46,300.86/138,902.59; concession $153.90 ACTIVE; full TCV 144,442.99; mix FAIL/PASS); Part 4 the brackets as filled for S6-P01.a. FILED in the right folder for the right page, all four repositories: the S6-P01 page folder (website-project), this code folder, the Drive mirror's S6-P01.a folder, and the GitHub repo's tools/deal-pricing-solver/ folder. PAGE.md gained it as a build source. CODE-MAP v11 in this same change. Log 17.12.
- **2026-11-08 (GITHUB LIVE + sitemap skeleton + GitHub map — Lucky's instruction)** — "Mirror the site map in GitHub, so we know where the folders and files are in GitHub for editing future code… don't forget to log." (1) GOOGLE SIGN-IN ENABLED for @thecozymerc (Lucky's ruling, closing the question open since Oct 29) — completed through josephconte.sf@gmail.com (thecozymerc.sf@gmail.com was not offered in the Google chooser; the account itself stays @thecozymerc / thecozymerc.sf@gmail.com). (2) REPOSITORY CREATED: github.com/thecozymerc/fractional-deal-desk-site (public) with the sitemap description; the staged Option B tree uploaded in 4 commits and the root tree verified against the staging (assets/, tools/, README.md, index.html; both tool folders complete). (3) SITEMAP SKELETON IN GITHUB: every sitemap folder now exists in the repo, each carrying its LABEL.md (what the page is, its ID, address, status) — one folder per page, siloed, in GitHub exactly as in the Drive mirror. GITHUB-MAP.md added at the repo root (the repo's own map: every folder ↔ page ID ↔ address ↔ contents ↔ status, plus how a change is made), and CODE-MAP.md + CHANGELOG.md now travel with the repo, refreshed at each deploy. P02's publish copy (services/index.html) uploaded in the same pass; the three earlier publish copies were refreshed (Services links restored — /services/ now exists). Publish tree re-verified: 41 files, zero dead internal links. (4) LOGGING: this entry + Log 17.10/17.11 in Plans tab -19 + the checklist doc annotated with tonight's runs. Still in flight at this entry: the Cloudflare Pages deployment (Google sign-in route) — its URL joins Doc 01's blanks when it lands.
- **2026-11-08 (P02 — Services & Pricing built)** — Tonight's push (Lucky: "We will push tonight to get as much done"). New page file `services/P02-services-and-pricing.html`: Draft 1.10 Section 5 ("What You Can Hire Me For") in full — intro, Phase 1/2/3 with their locked price lines, the hero offer (Embedded Commercial Redliner & Deal Desk, $7,500/mo, all five deal points), the 10-line service menu, and billing terms. VERIFIED: all 36 source paragraphs present verbatim (script compare), every locked price present, #pricing anchor on the Phase 1 heading. Records in the same change (Build Checklist): services LABEL, this entry, CODE-MAP v10, SITEMAP-TABLE status, Drive mirror folder "P02 — Services & Pricing" + Page Text Sheet (money lines) + the page code. Publish copy joins the staged tree at the next re-stage/redeploy.
- **2026-11-08 (records catch-up + Option B launch prep — Lucky's instruction)** — "Following the site map, replace what needs to be replaced by this calculator build; update the map, the charts, all of it, log etc.; add these into the checklist so we run them on the daily when we build." Done in this pass: (1) S6-P01 PAGE.md — piece 1 is now the Deal Pricing Calculator with its real build sources (original model + Pricing Engine PDF + companion workbook); status updated. (2) Folder charts regenerated (generator's P01 node rewritten for the calculator: New Deal view, Old vs New view, TCV form, companion workbook) — all 27 folders re-charted. (3) SECTION-6-CHART, WEBSITE-CHART.html, SITEMAP-TABLE updated — S6-P01.a renamed to Deal Pricing Calculator with its full description; S6-P01.a, S6-P01.b and P01 statuses now "Built — launching (Option B)". (4) STANDING BUILD CHECKLIST written (Lucky, Nov 8): sitemap-first · replace-in-the-same-pass · code+text together · two repositories (GitHub + Drive mirror) in the same pass · verify before reporting · log it — full text in the pre-publish checklist file + a summary in AGENTS.md. (5) DRIVE MIRROR BUILT: "Site — Code & Pages (GitHub mirror)" inside Website build 10.22.2026 — one folder per built page (P01 · S6-P01.a · S6-P01.b) + assets (shared); each page folder holds its Page Text Sheet (row 1 = text IDs matching the chart boxes, row 2 = the line's place, row 3 = the text) and its code files; a README explains the mirror. (6) Option B staging: publish copies (index.html per folder) built with navigation trimmed to the pages that exist — the ID-named files stay the source of truth, untouched. CODE-MAP updated to v9 in this same change.
- **2026-11-08 (S6-P01.a — the calculator replaces the embed; companion workbook built)** — Lucky's ruling in chat: save the Deal Pricing Calculator (review build v4, approved across Nov 8: "Jesus this is perfect") into the code on its page, and build a sheet like it too. The S6-P01.a page was rebuilt: same shell (header/footer/booking) and the same Draft 1.10 write-up paragraphs, with only the mechanics paragraph updated to describe the calculator instead of the retired embed; the calculator is carried by two new labeled files in the folder — `S6-P01a-deal-pricing-calculator.js` (math + wiring) and `S6-P01a-deal-pricing-calculator.css` (styles scoped under .calc). What the calculator is: built to Lucky's spec from his own model documents (the original Deal Pricing sheet + the Enterprise Deal Pricing Engine PDF) — New Deal view (baselines, dual-layout solver, TCV form, product lines, coupons, usage lines, usage-threshold concession, expansion utility) and Old vs New view (both sides lined, variance, SKU-mix checks); lines have dropdowns, editable names, add and delete. The embed's data files stay in the folder unused; the formula engine still powers S6-P01.b. The homepage (P01) still carries the embed — flagged to Lucky, his call pending. Companion workbook: "Deal Pricing Calculator — SAMPLE.xlsx" (tool-builds folder) — the same calculator as a live-formula spreadsheet (START HERE / New Deal / Old vs New / Expansion Utility; yellow inputs, green formulas; SKU-mix checks there match products by name, noted on its START HERE tab). VERIFIED: page math regression in node (the model's worked examples) + workbook recalculated in LibreOffice — the sheet reproduces the same headline values (PUPM 13.20; solver 30.00 / 45% / 20%; TCV form ACV 28,512; new totals ACV 46,800.86 / TCV-after-coupon 138,902.59; concession ACTIVE at $153.90/mo; old-vs-new line 1 after-coupon +38.74%; usage change +30.63%). CODE-MAP updated to v8 in this same change.
- **2026-11-08 (S6-P01.b built)** — Second tool page: Perpetual-to-SaaS Conversion Calculator (the old-deal-vs-new-deal comparison), at Lucky's request after a start-building verification. Verification found two gaps, both closed in this change: (1) the formula engine gained INDEX + MATCH (exact match) — the workbook's break-even lookups need them; (2) the renderer gained chart support, and convert-workbook.py now carries each sheet's own chart specs — this workbook's LineChart ("Cumulative Cost by Year — Status Quo vs SaaS Options", 4 series) is drawn on the page from the same computed cells and redraws when inputs change. The workbook converted as-is (v2, original wording; NO revised-descriptions copy was made — that variant exists only where Lucky asks for it). Page write-up verbatim from Draft 1.11 Part II (§6). VERIFIED vs LibreOffice recalculation: all 103 formula cells × 3 scenarios (defaults; Option A subscription $45,000 — the "No break-even within horizon" edge; horizon 3) = 309 comparisons, zero differences. CODE-MAP updated to v7 in this same change.
- **2026-11-08 (embed: the sheet's own formulas)** — Lucky's instruction: stop re-implementing the math — "embed the damn sheet without showing the formulas." The hand-written compute module is RETIRED (trash, recoverable). New: `assets/formula-engine.js`, a formula engine that evaluates each workbook's OWN formulas in the browser (IF, SUM, COUNTIF-family, comparisons, ranges); `convert-workbook.py` now carries the formulas in the data payload as machinery (the renderer never displays one); `assets/spreadsheet-tool.js` rewired to the engine. VERIFIED against the real spreadsheet: the workbook was recalculated in LibreOffice and the engine's outputs compared on every formula cell — 58 comparisons across the default case and two changed-input cases (Block 1 discount 35%; term 1 year + Quarterly terms) — zero differences. CODE-MAP updated to v6 in this same change.
- **2026-11-08 (revised descriptions — completed)** — The rewording now covers the WHOLE workbook, both sheets: 117 text cells reworded (the first pass's 37 narrative cells plus every remaining label, block title, column header, and note). Completeness was machine-checked: of 159 text cells, 117 reworded, 31 are the INPUT/OUTPUT machine markers, 11 are declared keeps ("Value" headers, Year labels, and "Annual Upfront" — a functional input value the sheet's own note says to type exactly). Nothing else remains in the original wording. A diff proves every value, input, and formula is identical to the original workbook. (First pass, same day: the revised copy "Deal Pricing Solver — SAMPLE (Revised Descriptions).xlsx" was created in the tool-builds folder with the original untouched beside it, converted to `S6-P01a-deal-pricing-solver-data-revised.js`, and both pages switched to it, saying so on the page.)
- **2026-11-08** — THE ACTUAL WORKBOOK, ON THE PAGE (Lucky's rule, restated twice): the hero no longer holds a replica — it holds the Deal Pricing Solver workbook itself. Built: `website-project/convert-workbook.py` (converts a SAMPLE workbook to a data file: every cell's text, input values, number formats — formula strings never emitted); `assets/spreadsheet-tool.js` (shared engine: renders the workbook as the actual spreadsheet — sheet tabs for both sheets, the sheet's own rows and words, yellow INPUT cells live, formula cells showing computed values only); `tools/deal-pricing-solver/` gained the tool page `S6-P01a-deal-pricing-solver.html` plus its data + compute files, which also power the homepage embed. `assets/homepage-solver.js` retired to trash. Verified: converted data matches the workbook cell-for-cell (205 cells, 18 inputs, 29 formula cells); compute outputs match the sheet on both tabs, including a term=1 case (out-of-term years show — and drop out of the totals). CODE-MAP updated to v4 in this same change.
- **2026-11-07 (correction)** — Hero solver panel REBUILT to match the workbook. Lucky flagged that the first panel ("mini solver": list + discount + margin → net/share/retain) was nothing like the actual sheet — he was right; it was an invented shortcut. The panel is now a faithful replica of "Deal Pricing Solver — SAMPLE.xlsx," sheet 1: PUPM block (ARPU 158.4, Months 12 → $13.20), Block 1 Solve List Price (20%, $8,000 → $10,000), Block 2 Solve Discount ($10,000, $7,500 → 25.0%), Block 3 Solve Partner Margin ($10,000, 20%, $6,800 → Net $8,000, Margin 15.0%, $1,200) — the sheet's own sample values, labels, formulas, guards, how-to, and Inputs/Logic/Limits wording; yellow INPUT cells and green result cells like the sheet. `assets/mini-solver.js` replaced by `assets/homepage-solver.js`; solver styles added to `assets/styles.css`; CODE-MAP updated to v3 in this same change. Outputs verified by executing the script (node) against the sheet's expected results. The Multi-Year Deal Block stays on the full tool page, as the panel now states.
- **2026-11-07 (later)** — P01 Homepage built (awaiting Lucky's approval): `P01-homepage.html` in the site root — Sections 1–6 from Draft 1.10 verbatim (tight homepage cut), D01 design, proof strip, 3 featured tool cards, booking route. New shared files: `assets/styles.css` (the D01 token system) and `assets/mini-solver.js` (hero mini calculator — a slice of the Deal Pricing Solver). Naming convention adopted on Lucky's instruction: page ID + descriptive sitemap title in each filename, `<title>`, and label comment. CODE-MAP updated to v2 and the root + assets LABEL.md files updated in this same change.
- **2026-11-07** — Code home created: folder skeleton for all 25 page addresses + the /about and /services pages, a LABEL.md in every folder, CODE-MAP.md v1, and this change log. No page code yet. Teach-back gate cleared today (Lucky, in his own words: master file with everything, labels in every folder, versions of the maps, and this change log).
