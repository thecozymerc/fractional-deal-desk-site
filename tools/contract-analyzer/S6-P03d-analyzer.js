/* ==========================================================================
   LABEL — S6-P03.d · Tool 13 — Contract Analyzer — analysis engine.
   What this file is: the analyzer's brain, in two layers.
   LAYER 1 — the original scans: an exact JavaScript port of the heuristic
   parser from Lucky's contract-analyzer repo (analyzer/parsers/clauses.py,
   Streamlit MVP, Oct 2025) — the same six patterns with the same semantics,
   quirks included, verified output-for-output against the Python original
   on the repo's sample contract (see the build record).
   LAYER 2 — the coverage checks: the full "what needs checking in a
   contract" checklist (basics, money, risk, data & IP, operations, legal),
   each check a set of phrase patterns; a check reports FOUND with the
   matched excerpt, or NOT FOUND so a human checks by hand. Heuristic
   pattern matching only — it locates language, it does not judge it, and
   it is not legal advice.
   Rule: any change to this file is recorded in CHANGELOG.md, and the
   CODE-MAP entry is updated in the same change (Code Labeling, Rule 3).
   ========================================================================== */
(function () {
  "use strict";

  /* ---------------- Layer 1 — the original six scans (faithful port) ---- */
  var DATE_RE = /\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)[\s,]+\d{1,2},\s*\d{4}\b|\b\d{4}-\d{2}-\d{2}\b/gi;
  var MONEY_RE = /\b(?:USD\s*)?\$\s?\d[\d,]*(?:\.\d{2})?\b/gi;
  var PARTY_RE = /\bbetween\s+([A-Z][\w\s,&.\-]+?)\s+and\s+([A-Z][\w\s,&.\-]+)/gi;
  var LAW_RE = /\b(governing law|jurisdiction)\b[:\s-]+([A-Za-z\s]+)/gi;
  var TERM_LENGTH_RE = /\b(initial\s+)?term\b.*?(?:is|for|of)?\s*(?:\w+\s*\(\s*\d+\s*\)\s*|\d+)\s*(?:month|year|day|week)s?/gi;
  var RENEWAL_PERIOD_RE = /\b(renews?|auto[-\s]?renew(al)?)\b.*?(?:for\s*)?(?:\w+\s*\(\s*\d+\s*\)\s*|\d+)\s*(?:month|year|day|week)s?/gi;

  function allMatches(text, re) {
    var out = [], m;
    re.lastIndex = 0;
    while ((m = re.exec(text)) !== null) {
      if (m.length > 1) {
        var groups = [];
        for (var i = 1; i < m.length; i++) groups.push(m[i] === undefined ? "" : m[i]);
        out.push(groups.length === 1 ? groups[0] : groups);
      } else {
        out.push(m[0]);
      }
      if (m[0] === "") re.lastIndex++;
    }
    return out;
  }

  function parseKeyClauses(text) {
    return {
      dates: allMatches(text, DATE_RE),
      money: allMatches(text, MONEY_RE),
      parties: allMatches(text, PARTY_RE),
      law: allMatches(text, LAW_RE),
      term_length: allMatches(text, TERM_LENGTH_RE),
      renewal_period: allMatches(text, RENEWAL_PERIOD_RE)
    };
  }

  /* ---------------- Layer 2 — the coverage checks ----------------------- */
  function P(s) { return new RegExp(s, "i"); }
  var CHECKS = [
    /* Basics */
    { id: "parties", group: "Basics", name: "Parties named",
      why: "Who is bound — the legal names of both sides.",
      patterns: [P("\\bbetween\\s+[A-Z][\\w\\s,&.\\-]+?\\s+and\\s+[A-Z]"), P("\\b(this agreement|this contract)\\s+is\\s+(made|entered into)\\b")] },
    { id: "effective-date", group: "Basics", name: "Effective / start date",
      why: "When the obligations start running.",
      patterns: [P("\\beffective date\\b"), P("\\bcommencement date\\b"), P("\\bmade on\\s+\\d{4}-\\d{2}-\\d{2}\\b")] },
    { id: "term", group: "Basics", name: "Term length",
      why: "How long the contract runs before it ends or renews.",
      patterns: [P("\\b(initial\\s+)?term\\b[^.\\n]{0,60}?(\\d+|twelve|twenty-four|thirty-six)(\\s*\\(\\s*\\d+\\s*\\))?\\s*(month|year|day|week)"), P("\\bterm of\\s+(this agreement|\\d)")] },
    { id: "renewal", group: "Basics", name: "Renewal / auto-renewal",
      why: "Whether it rolls over on its own, and for how long each time.",
      patterns: [P("\\bauto[-\\s]?renew"), P("\\bshall renew\\b"), P("\\brenew(s|al)?\\s+for\\b"), P("\\bsuccessive (terms|periods|renewal)\\b")] },
    { id: "renewal-notice", group: "Basics", name: "Non-renewal notice deadline",
      why: "The last day to stop a renewal — the date that gets missed.",
      patterns: [P("notice of non[-\\s]?renewal"), P("\\bnot\\s+(renew|extend)\\b[^.\\n]{0,40}notice"), P("(prior to|before)\\s+(the\\s+)?(renewal|expiration)[^.\\n]{0,60}notice"), P("notice[^.\\n]{0,50}(prior to|before)[^.\\n]{0,30}renew")] },
    { id: "termination-convenience", group: "Basics", name: "Termination for convenience + notice",
      why: "Whether either side can walk away without cause, and how much notice.",
      patterns: [P("terminate[^.\\n]{0,60}for convenience"), P("terminate[^.\\n]{0,40}without cause"), P("may terminate[^.\\n]{0,80}\\b\\d+\\s*days?['\\u2019]?\\s*(prior\\s+)?(written\\s+)?notice")] },
    { id: "termination-cause", group: "Basics", name: "Termination for cause",
      why: "The exit when the other side breaches — and any cure period.",
      patterns: [P("terminate[^.\\n]{0,60}for cause"), P("material breach"), P("cure (period|such breach|within)")] },
    /* Money */
    { id: "fees", group: "Money", name: "Fees / contract value",
      why: "What is actually being paid — amounts, per what, how often.",
      patterns: [P("(USD\\s*)?\\$\\s?\\d[\\d,]*(\\.\\d{2})?"), P("\\bfees? of\\s"), P("\\bper (month|year|annum|user|seat)\\b")] },
    { id: "payment-terms", group: "Money", name: "Payment terms (when invoices are due)",
      why: "Net days and the trigger (invoice date, receipt, acceptance).",
      patterns: [P("\\bnet\\s*\\d+\\b"), P("payable within\\s*\\d+\\s*days"), P("due within\\s*\\d+\\s*days"), P("within\\s*\\d+\\s*days of (invoice|receipt)")] },
    { id: "late-fees", group: "Money", name: "Late fees / interest on late payment",
      why: "What a late payment costs, and whether it is capped.",
      patterns: [P("late (fee|charge|payment)[^.\\n]{0,50}(%|interest|per)"), P("interest[^.\\n]{0,40}(late|overdue|per (month|annum))"), P("overdue[^.\\n]{0,40}interest")] },
    { id: "price-increase", group: "Money", name: "Price increases / escalators",
      why: "Whether prices can rise at renewal, by how much, tied to what index.",
      patterns: [P("price increase"), P("increase[^.\\n]{0,40}(fees|prices|charges)[^.\\n]{0,40}(%|CPI|index)"), P("\\bCPI\\b"), P("escalat(or|ion)"), P("uplift")] },
    { id: "taxes", group: "Money", name: "Taxes",
      why: "Which taxes sit on top of the fees and who carries them.",
      patterns: [P("\\b(exclusive of|plus|excluding)\\s+(all\\s+)?taxes\\b"), P("\\b(sales tax|VAT|GST|withholding tax)\\b"), P("responsible for[^.\\n]{0,30}taxes")] },
    /* Risk */
    { id: "liability-cap", group: "Risk", name: "Liability cap",
      why: "The ceiling on what either side can be made to pay — the number that matters most in a dispute.",
      patterns: [P("liability[^.\\n]{0,60}(shall not exceed|cap(ped)?|limited to)"), P("aggregate liability"), P("(cap|limitation) on liability"), P("in no event[^.\\n]{0,60}liable[^.\\n]{0,40}exceed")] },
    { id: "consequential", group: "Risk", name: "Consequential / indirect damages exclusion",
      why: "Whether lost profits and similar damages are excluded — for both sides or one.",
      patterns: [P("consequential damages"), P("indirect[^.\\n]{0,20}damages"), P("lost profits")] },
    { id: "indemnity", group: "Risk", name: "Indemnification",
      why: "Who pays when a third party comes after either side, and for what.",
      patterns: [P("\\bindemnif\\w+"), P("hold harmless"), P("defend[^.\\n]{0,40}against[^.\\n]{0,30}(claim|action)")] },
    { id: "warranties", group: "Risk", name: "Warranties",
      why: "What is promised about the service — and what is disclaimed.",
      patterns: [P("\\bwarrant(s|ies|y)\\b"), P("as[-\\s]is"), P("disclaim\\w*[^.\\n]{0,30}warrant")] },
    { id: "insurance", group: "Risk", name: "Insurance requirements",
      why: "Coverage the other side must carry, and at what limits.",
      patterns: [P("\\binsurance\\b[^.\\n]{0,50}(maintain|carry|coverage|policy)"), P("certificate of insurance"), P("(commercial general liability|cyber liability|professional liability) insurance")] },
    /* Data & IP */
    { id: "ip-ownership", group: "Data & IP", name: "IP ownership / work product",
      why: "Who owns what gets made under the contract.",
      patterns: [P("intellectual property"), P("work product"), P("(own|ownership)[^.\\n]{0,40}(deliverables|materials developed)"), P("all rights, title")] },
    { id: "license", group: "Data & IP", name: "License grant",
      why: "What each side is allowed to use, and where the grant stops.",
      patterns: [P("grant(s|ed)?[^.\\n]{0,40}licen[cs]e"), P("licen[cs]e to use"), P("non-exclusive[^.\\n]{0,30}licen[cs]e")] },
    { id: "confidentiality", group: "Data & IP", name: "Confidentiality",
      why: "What counts as confidential, how long the duty lasts, who can see it.",
      patterns: [P("confidential information"), P("\\bnon-disclosure\\b"), P("shall keep[^.\\n]{0,30}confidential")] },
    { id: "data-protection", group: "Data & IP", name: "Data protection / privacy (DPA)",
      why: "How personal data is handled, and whether a data processing addendum applies.",
      patterns: [P("data protection"), P("personal data"), P("\\bDPA\\b|data processing (addendum|agreement)"), P("(GDPR|CCPA|CPRA)"), P("data breach|security incident")] },
    { id: "security", group: "Data & IP", name: "Security requirements",
      why: "Named security standards, audits, and breach notice duties.",
      patterns: [P("(SOC\\s?2|ISO\\s?27001)"), P("security (measures|program|standards)"), P("notify[^.\\n]{0,50}(breach|incident)[^.\\n]{0,30}(hour|day)")] },
    /* Operations */
    { id: "sla", group: "Operations", name: "Service levels / SLA + credits",
      why: "Uptime and support commitments — and what happens when they are missed.",
      patterns: [P("service levels?"), P("\\bSLA\\b"), P("uptime"), P("service credits?"), P("availability of\\s*\\d")] },
    { id: "audit-rights", group: "Operations", name: "Audit rights",
      why: "Who can inspect books, usage, or compliance — and how often.",
      patterns: [P("audit rights?"), P("right to audit"), P("(inspect|examine)[^.\\n]{0,40}(books|records)"), P("upon[^.\\n]{0,30}notice[^.\\n]{0,30}audit")] },
    { id: "assignment", group: "Operations", name: "Assignment / change of control",
      why: "Whether the contract can be handed to another company without consent.",
      patterns: [P("\\bassign(ment|s|ed)?\\b[^.\\n]{0,50}(consent|successor)"), P("change of control"), P("may not assign")] },
    { id: "subcontracting", group: "Operations", name: "Subcontractors / subprocessors",
      why: "Who else touches the work or the data, and whether consent is needed.",
      patterns: [P("subcontract"), P("sub-?processor"), P("third-party (providers|services)[^.\\n]{0,30}(list|notif)")] },
    { id: "exclusivity-nonsolicit", group: "Operations", name: "Exclusivity / non-solicitation",
      why: "Lock-ins: exclusive dealing, non-competes, and staff poaching bans.",
      patterns: [P("\\bexclusiv(e|ity)\\b"), P("non-?solicit"), P("shall not solicit"), P("non-?compete")] },
    /* Legal */
    { id: "governing-law", group: "Legal", name: "Governing law",
      why: "Which state's or country's law interprets the contract.",
      patterns: [P("governing law"), P("governed by[^.\\n]{0,30}laws of")] },
    { id: "venue-disputes", group: "Legal", name: "Venue / dispute resolution / arbitration",
      why: "Where a fight happens and how — courts, arbitration, mediation first.",
      patterns: [P("\\bjurisdiction\\b"), P("\\bvenue\\b"), P("arbitrat\\w+"), P("mediation"), P("dispute resolution")] },
    { id: "force-majeure", group: "Legal", name: "Force majeure",
      why: "What happens when events outside both sides' control stop performance.",
      patterns: [P("force majeure"), P("act of God"), P("events beyond[^.\\n]{0,30}(reasonable )?control")] },
    { id: "notices", group: "Legal", name: "Notices (how formal notice is given)",
      why: "Where termination and other notices must be sent to count.",
      patterns: [P("notices? (shall|must) be (given|sent|in writing)"), P("notice to[^.\\n]{0,10}:"), P("all notices")] },
    { id: "entire-agreement", group: "Legal", name: "Entire agreement / amendments / precedence",
      why: "Whether side promises count, how changes are made, and which document wins a conflict.",
      patterns: [P("entire agreement"), P("order of precedence"), P("amend(ed|ment)[^.\\n]{0,40}in writing"), P("in the event of a conflict")] },
    { id: "signatures", group: "Legal", name: "Signatures / execution",
      why: "Whether the copy is actually signed — and by whom.",
      patterns: [P("IN WITNESS WHEREOF"), P("\\bsignature\\b"), P("/s/"), P("\\bexecuted\\b[^.\\n]{0,30}(by|as of)")] }
  ];

  function excerptAround(text, idx, len) {
    var start = Math.max(0, idx - 70);
    var end = Math.min(text.length, idx + len + 90);
    var s = text.slice(start, end).replace(/\s+/g, " ").trim();
    if (start > 0) s = "…" + s;
    if (end < text.length) s = s + "…";
    return s;
  }

  function runChecks(text) {
    return CHECKS.map(function (c) {
      var hit = null;
      for (var i = 0; i < c.patterns.length && !hit; i++) {
        var m = c.patterns[i].exec(text);
        if (m) hit = { match: m[0], excerpt: excerptAround(text, m.index, m[0].length) };
      }
      return { id: c.id, group: c.group, name: c.name, why: c.why, found: !!hit, excerpt: hit ? hit.excerpt : null };
    });
  }

  window.ContractAnalyzer = {
    parseKeyClauses: parseKeyClauses,
    runChecks: runChecks,
    CHECKS: CHECKS
  };
})();
