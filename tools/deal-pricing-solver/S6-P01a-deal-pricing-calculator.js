/* ==========================================================================
   S6-P01a-deal-pricing-calculator.js — the Deal Pricing Calculator
   (S6-P01.a tool page, /tools/deal-pricing-solver/).
   Built Nov 8, 2026 to Lucky's own spec, from his model documents:
   "Deal Pricing & Scenario Evaluation Model.xlsx" + "Enterprise Deal
   Pricing Engine.pdf". Features: New Deal view (baselines, dual-layout
   solver, TCV form, product lines with dropdowns + editable names +
   add/delete lines, coupons, usage lines, usage-threshold concession,
   ARPU expansion utility) and Old vs New view (both sides fully lined,
   per-line and total variance, SKU-mix checks). Core identity:
   Net PUPM = List x (1-Discount) x (1-Partner Margin) = ARPU / Months.
   The CALC block is pure math, verified in node against the model's own
   worked examples (28 checks at v1; regression re-run at every version).
   Formulas never display; the page shows inputs and computed values only.
   Rule: any change is recorded in ../../CHANGELOG.md with the CODE-MAP
   updated in the same change (Code Labeling System, Rule 3).
   ========================================================================== */

/* ============================ MATH (pure; verified in node vs the model) ============================ */
var CALC = {
  pupmFromArpu: function (arpu, months) { return months ? arpu / months : NaN; },
  pupmLayer: function (list, disc, pm) { return list * (1 - disc) * (1 - pm); },
  solveList: function (pupm, disc, pm) { var d = (1 - disc) * (1 - pm); return d ? pupm / d : NaN; },
  solveDisc: function (pupm, list, pm) { var d = list * (1 - pm); return d ? 1 - pupm / d : NaN; },
  solvePM: function (pupm, list, disc) { var d = list * (1 - disc); return d ? 1 - pupm / d : NaN; },
  line: function (list, seats, disc, pm, months) {
    var pupm = CALC.pupmLayer(list, disc, pm);
    var pupy = pupm * 12;
    var acv = pupy * seats;
    var tcv = acv * (months / 12);
    return { pupm: pupm, pupy: pupy, acv: acv, tcv: tcv, seats: seats, arpa: acv / 12 };
  },
  pctChange: function (oldV, newV) { return oldV ? (newV - oldV) / Math.abs(oldV) : NaN; },
  expand: function (price, pct) { return price * (1 + pct); },
  contract: function (price, pct) { return price * (1 - pct); },
  usage: function (units, pricePerUnit, disc, minUnits) {
    var billed = Math.max(units, minUnits || 0);
    var gross = billed * pricePerUnit;
    var net = gross * (1 - disc);
    return { billed: billed, gross: gross, net: net, year: net * 12,
             effPerUnit: billed ? net / billed : NaN };
  },
  applyCoupon: function (line, coupon, years) {
    var out = { pupm: line.pupm, pupy: line.pupy, acv: line.acv, tcv: line.tcv,
                seats: line.seats, arpa: line.arpa };
    out.facv = line.acv - (years ? coupon / years : coupon);
    out.ftcv = line.tcv - coupon;
    return out;
  },
  threshold: function (items, meterType, thresholdUnits, extraPct) {
    var units = 0, net = 0;
    items.forEach(function (it) {
      if (it.type === meterType) { units += it.billed; net += it.net; }
    });
    var triggered = thresholdUnits > 0 && units >= thresholdUnits;
    var off = triggered ? net * extraPct : 0;
    return { units: units, meteredNet: net, triggered: triggered, off: off, after: net - off };
  }
};

/* ============================ PAGE WIRING ============================ */
if (typeof document !== "undefined" && document.getElementById("calc-root")) (function () {
  var PRODUCTS = [
    { name: "Plus Ultra", list: 30, fam: "enterprise" },
    { name: "Core Standard", list: 23, fam: "enterprise" },
    { name: "Biz Plus", list: 22, fam: "business" },
    { name: "Frontline Lite", list: 4, fam: "frontline" },
    { name: "None", list: 0, fam: "none" }
  ];
  function $(id) { return document.getElementById(id); }
  function num(id) { var v = parseFloat($(id).value); return isNaN(v) ? 0 : v; }
  function money(v, dec) {
    if (v === null || v === undefined || isNaN(v)) return "—";
    return v.toLocaleString("en-US", { minimumFractionDigits: dec === undefined ? 2 : dec, maximumFractionDigits: dec === undefined ? 2 : dec });
  }
  function pctFmt(v) {
    if (v === null || v === undefined || isNaN(v)) return "—";
    return (v * 100).toFixed(2) + "%";
  }
  function deltaHtml(v) {
    if (isNaN(v)) return '<span class="num">—</span>';
    var cls = v > 0 ? "pos" : (v < 0 ? "neg" : "");
    return '<span class="num ' + cls + '">' + (v > 0 ? "+" : "") + pctFmt(v) + "</span>";
  }

  /* tabs (the model's "flip": a different tab per view) */
  var tabs = document.querySelectorAll(".tab");
  tabs.forEach(function (t) {
    t.addEventListener("click", function () {
      tabs.forEach(function (x) { x.classList.remove("active"); });
      t.classList.add("active");
      ["v1", "v2"].forEach(function (v) { $(v).style.display = v === t.dataset.view ? "" : "none"; });
    });
  });

  /* ---------- product line tables ---------- */
  var counts = { nd: 0, old: 0, new: 0, ndu: 0, oldu: 0, newu: 0 };
  function buildLineRow(table, prefix, i, d) {
    var tr = document.createElement("tr");
    var sel = '<select class="in" id="' + prefix + i + '-sku">' + PRODUCTS.map(function (p) {
      return '<option value="' + p.name + '"' + (p.name === d.sku ? " selected" : "") + ">" + p.name + "</option>";
    }).join("") + "</select>";
    tr.innerHTML =
      "<td>" + sel + "</td>" +
      '<td><input class="in" id="' + prefix + i + '-name" type="text" value="' + (d.name || (d.sku === "None" ? "" : d.sku)) + '" placeholder="Name this line"></td>' +
      '<td><input class="in" id="' + prefix + i + '-list" type="number" step="any" value="' + d.list + '"></td>' +
      '<td><input class="in" id="' + prefix + i + '-seats" type="number" step="any" value="' + d.seats + '"></td>' +
      '<td><input class="in" id="' + prefix + i + '-disc" type="number" step="any" value="' + d.disc + '"></td>' +
      '<td><input class="in" id="' + prefix + i + '-pm" type="number" step="any" value="' + d.pm + '"></td>' +
      '<td><input class="in" id="' + prefix + i + '-months" type="number" step="any" value="' + d.months + '"></td>' +
      '<td class="num" id="' + prefix + i + '-pupm">—</td>' +
      '<td class="num" id="' + prefix + i + '-pupy">—</td>' +
      '<td class="num" id="' + prefix + i + '-acv">—</td>' +
      '<td class="num" id="' + prefix + i + '-tcv">—</td>' +
      '<td><input class="in" id="' + prefix + i + '-coupon" type="number" step="any" value="' + (d.coupon || 0) + '"></td>' +
      '<td class="num" id="' + prefix + i + '-facv">—</td>' +
      '<td class="num" id="' + prefix + i + '-ftcv">—</td>' +
      '<td><button type="button" class="del" title="Delete this line">✕</button></td>';
    table.appendChild(tr);
    $(prefix + i + "-sku").addEventListener("change", function () {
      var p = PRODUCTS.filter(function (x) { return x.name === this.value; })[0];
      var row = this.closest("tr");
      row.querySelector('[id$="-list"]').value = p.list;
      row.querySelector('[id$="-name"]').value = p.name === "None" ? "" : p.name;
      recompute();
    });
    tr.querySelector(".del").addEventListener("click", function () {
      var row = this.closest("tr");
      var table = row.closest("table");
      row.remove();
      counts[prefix]--;
      renumber(table, prefix);
      recompute();
    });
  }
  function buildLines(tableId, prefix, defaults) {
    var table = $(tableId);
    defaults.forEach(function (d, i) { buildLineRow(table, prefix, i, d); });
    counts[prefix] = defaults.length;
  }
  function addSeatLine(tableId, prefix) {
    var i = counts[prefix]++;
    buildLineRow($(tableId), prefix, i, { sku: "None", name: "", list: 0, seats: 0, disc: 0, pm: 0, months: 36, coupon: 0 });
    recompute();
  }
  function readLine(prefix, i) {
    var months = num(prefix + i + "-months");
    var base = CALC.line(num(prefix + i + "-list"), num(prefix + i + "-seats"),
      num(prefix + i + "-disc") / 100, num(prefix + i + "-pm") / 100, months);
    return CALC.applyCoupon(base, num(prefix + i + "-coupon"), months / 12);
  }
  function paintLine(prefix, i, r) {
    $(prefix + i + "-pupm").textContent = money(r.pupm);
    $(prefix + i + "-pupy").textContent = money(r.pupy);
    $(prefix + i + "-acv").textContent = money(r.acv);
    $(prefix + i + "-tcv").textContent = money(r.tcv);
    $(prefix + i + "-facv").textContent = money(r.facv);
    $(prefix + i + "-ftcv").textContent = money(r.ftcv);
  }

  /* ---------- usage line tables (per use / per token, inside the deals) ---------- */
  var UNIT_TYPES = [
    { id: "token1m", name: "Tokens — per 1M tokens", per: 1000000 },
    { id: "token1k", name: "Tokens — per 1K tokens", per: 1000 },
    { id: "use", name: "Per use / per call", per: null },
    { id: "api", name: "Per API request", per: null }
  ];
  function buildUsageRow(table, prefix, i, d) {
    var tr = document.createElement("tr");
    var sel = '<select class="in" id="' + prefix + i + '-type">' + UNIT_TYPES.map(function (u) {
      return '<option value="' + u.id + '"' + (u.id === d.type ? " selected" : "") + ">" + u.name + "</option>";
    }).join("") + "</select>";
    tr.innerHTML =
      '<td><input class="in" id="' + prefix + i + '-name" type="text" value="' + (d.name || "") + '" placeholder="Name this line"></td>' +
      "<td>" + sel + "</td>" +
      '<td><input class="in" id="' + prefix + i + '-usage" type="number" step="any" value="' + d.usage + '"></td>' +
      '<td><input class="in" id="' + prefix + i + '-price" type="number" step="any" value="' + d.price + '"></td>' +
      '<td><input class="in" id="' + prefix + i + '-disc" type="number" step="any" value="' + d.disc + '"></td>' +
      '<td><input class="in" id="' + prefix + i + '-min" type="number" step="any" value="' + d.min + '"></td>' +
      '<td class="num" id="' + prefix + i + '-net">—</td>' +
      '<td class="num" id="' + prefix + i + '-eff">—</td>' +
      '<td class="num" id="' + prefix + i + '-pertoken">—</td>' +
      '<td><button type="button" class="del" title="Delete this line">✕</button></td>';
    table.appendChild(tr);
    tr.querySelector(".del").addEventListener("click", function () {
      var row = this.closest("tr");
      var table = row.closest("table");
      row.remove();
      counts[prefix]--;
      renumber(table, prefix);
      recompute();
    });
  }
  function buildUsage(tableId, prefix, defaults) {
    var table = $(tableId);
    defaults.forEach(function (d, i) { buildUsageRow(table, prefix, i, d); });
    counts[prefix] = defaults.length;
  }
  function addUsageLine(tableId, prefix) {
    var i = counts[prefix]++;
    buildUsageRow($(tableId), prefix, i, { type: "token1m", name: "", usage: 0, price: 0, disc: 0, min: 0 });
    recompute();
  }
  function renumber(table, prefix) {
    var rows = table.rows;
    for (var j = 0; j < rows.length - 1; j++) {
      var els = rows[j + 1].querySelectorAll("[id]");
      els.forEach(function (el) {
        el.id = el.id.replace(new RegExp("^" + prefix + "[0-9]+"), prefix + j);
      });
    }
  }
  function readUsage(prefix, i) {
    var type = $(prefix + i + "-type").value;
    var u = CALC.usage(num(prefix + i + "-usage"), num(prefix + i + "-price"),
      num(prefix + i + "-disc") / 100, num(prefix + i + "-min"));
    u.type = type;
    return u;
  }
  function paintUsage(prefix, i, u) {
    var meta = UNIT_TYPES.filter(function (x) { return x.id === u.type; })[0];
    $(prefix + i + "-net").textContent = money(u.net);
    $(prefix + i + "-eff").textContent = money(u.effPerUnit, 4);
    $(prefix + i + "-pertoken").textContent = meta.per ? "$" + (u.effPerUnit / meta.per).toFixed(8) : "—";
  }

  var ND = [
    { sku: "Core Standard", list: 23, seats: 86, disc: 45, pm: 12, months: 36, coupon: 1500 },
    { sku: "Biz Plus", list: 22, seats: 230, disc: 45, pm: 12, months: 36 },
    { sku: "Frontline Lite", list: 4, seats: 255, disc: 45, pm: 12, months: 36 },
    { sku: "None", list: 0, seats: 0, disc: 0, pm: 0, months: 0 }
  ];
  var OLD = [
    { sku: "Plus Ultra", list: 30, seats: 50, disc: 45, pm: 20, months: 36 },
    { sku: "None", list: 0, seats: 0, disc: 0, pm: 0, months: 0 },
    { sku: "None", list: 0, seats: 0, disc: 0, pm: 0, months: 0 }
  ];
  var NEW = [
    { sku: "Core Standard", list: 23, seats: 86, disc: 45, pm: 12, months: 36, coupon: 1500 },
    { sku: "Biz Plus", list: 22, seats: 230, disc: 45, pm: 12, months: 36 },
    { sku: "Frontline Lite", list: 4, seats: 255, disc: 45, pm: 12, months: 36 }
  ];
  buildLines("nd-table", "nd", ND);
  buildLines("old-table", "old", OLD);
  buildLines("new-table", "new", NEW);
  var NDU = [
    { type: "token1m", name: "Token usage", usage: 60, price: 3.00, disc: 10, min: 25 },
    { type: "use", name: "", usage: 0, price: 0, disc: 0, min: 0 }
  ];
  var OLDU = [
    { type: "token1m", name: "Token usage", usage: 30, price: 3.60, disc: 0, min: 0 },
    { type: "use", name: "", usage: 0, price: 0, disc: 0, min: 0 }
  ];
  var NEWU = [
    { type: "token1m", name: "Token usage", usage: 55, price: 3.00, disc: 10, min: 25 },
    { type: "use", name: "", usage: 0, price: 0, disc: 0, min: 0 }
  ];
  buildUsage("ndu-table", "ndu", NDU);
  buildUsage("oldu-table", "oldu", OLDU);
  buildUsage("newu-table", "newu", NEWU);

  /* add-line buttons */
  $("add-nd").addEventListener("click", function () { addSeatLine("nd-table", "nd"); });
  $("add-old").addEventListener("click", function () { addSeatLine("old-table", "old"); });
  $("add-new").addEventListener("click", function () { addSeatLine("new-table", "new"); });
  $("add-ndu").addEventListener("click", function () { addUsageLine("ndu-table", "ndu"); });
  $("add-oldu").addEventListener("click", function () { addUsageLine("oldu-table", "oldu"); });
  $("add-newu").addEventListener("click", function () { addUsageLine("newu-table", "newu"); });

  /* comparison rows, rebuilt when the line counts change */
  var cmpRowsBuilt = -1;
  function ensureCmpRows(n) {
    if (n === cmpRowsBuilt) return;
    var table = $("cmp-table");
    while (table.rows.length > 1) table.deleteRow(1);
    for (var i = 0; i < n; i++) {
      var tr = document.createElement("tr");
      tr.innerHTML = '<td id="cmp' + i + '-name">Line ' + (i + 1) + "</td>" +
        '<td id="cmp' + i + '-seats">—</td><td id="cmp' + i + '-arpu">—</td>' +
        '<td id="cmp' + i + '-arpa">—</td><td id="cmp' + i + '-acv">—</td><td id="cmp' + i + '-tcv">—</td>';
      table.appendChild(tr);
    }
    var tt = document.createElement("tr");
    tt.innerHTML = '<td><b>Totals</b></td><td id="cmpT-seats">—</td><td id="cmpT-arpu">—</td>' +
      '<td id="cmpT-arpa">—</td><td id="cmpT-acv">—</td><td id="cmpT-tcv">—</td>';
    table.appendChild(tt);
    cmpRowsBuilt = n;
  }

  /* smart form field labels by target */
  var SMART = {
    list: { f1: "Enter Partner Margin (PM) %", f2: "Enter Discount %", v1: 20, v2: 45 },
    disc: { f1: "Enter Partner Margin (PM) %", f2: "Enter List Price ($)", v1: 20, v2: 30 },
    pm: { f1: "Enter Discount %", f2: "Enter List Price ($)", v1: 45, v2: 30 }
  };
  $("s-target").addEventListener("change", function () {
    var s = SMART[this.value];
    $("s-f1-label").textContent = s.f1; $("s-f2-label").textContent = s.f2;
    $("s-f1").value = s.v1; $("s-f2").value = s.v2;
    recompute();
  });

  function recompute() {
    /* baselines + solver */
    var pupm = CALC.pupmFromArpu(num("b-arpu"), num("b-months"));
    $("b-pupm").textContent = money(pupm);
    $("m1-out").textContent = "$" + money(CALC.solveList(pupm, num("m1-disc") / 100, num("m1-pm") / 100));
    $("m2-out").textContent = pctFmt(CALC.solveDisc(pupm, num("m2-list"), num("m2-pm") / 100));
    $("m3-out").textContent = pctFmt(CALC.solvePM(pupm, num("m3-list"), num("m3-disc") / 100));
    var target = $("s-target").value, f1 = num("s-f1"), f2 = num("s-f2"), sres;
    if (target === "list") sres = "$" + money(CALC.solveList(pupm, f2 / 100, f1 / 100));
    else if (target === "disc") sres = pctFmt(CALC.solveDisc(pupm, f2, f1 / 100));
    else sres = pctFmt(CALC.solvePM(pupm, f2, f1 / 100));
    $("s-out").textContent = sres;

    /* TCV form */
    var tcv = num("t-tcv"), yrs = num("t-years"), seats = num("t-seats");
    var acv = yrs ? tcv / yrs : NaN, arpu = seats ? acv / seats : NaN;
    $("t-acv").textContent = money(acv);
    $("t-months").textContent = yrs ? String(yrs * 12) : "—";
    $("t-arpu").textContent = money(arpu);
    $("t-pupm").textContent = money(CALC.pupmFromArpu(arpu, 12));

    /* new-deal lines (View 1) */
    var totSeats = 0, totAcv = 0, totTcv = 0, totAcvRaw = 0;
    for (var ni = 0; ni < counts.nd; ni++) {
      var r = readLine("nd", ni); paintLine("nd", ni, r);
      totSeats += r.seats; totAcv += r.facv; totTcv += r.ftcv; totAcvRaw += r.acv;
    }
    $("nd-seats").textContent = String(totSeats);
    $("nd-acv").textContent = money(totAcv);
    $("nd-tcv").textContent = money(totTcv);
    $("nd-pupm").textContent = totSeats ? money(totAcvRaw / 12 / totSeats) : "—";

    /* expansion utility */
    $("e-up-out").textContent = money(CALC.expand(num("e-price"), num("e-up") / 100));
    $("e-down-out").textContent = money(CALC.contract(num("e-price"), num("e-down") / 100));

    /* old vs new (View 2) */
    var olds = [], news = [];
    for (var oi = 0; oi < counts.old; oi++) { var ro = readLine("old", oi); paintLine("old", oi, ro); olds.push(ro); }
    for (var wi = 0; wi < counts.new; wi++) { var rw = readLine("new", wi); paintLine("new", wi, rw); news.push(rw); }
    var sum = function (arr, k) { return arr.reduce(function (a, r) { return a + r[k]; }, 0); };
    var oPupy = sum(olds, "pupy"), nPupy = sum(news, "pupy");
    var oArpa = sum(olds, "arpa"), nArpa = sum(news, "arpa");
    var ZERO = { seats: 0, pupy: 0, arpa: 0, facv: 0, ftcv: 0 };
    var lineName = function (prefix, i) {
      var nm = $(prefix + i + "-name").value.trim();
      if (nm) return nm;
      var sku = $(prefix + i + "-sku").value;
      return sku === "None" ? "—" : sku;
    };
    var nCmp = Math.max(counts.old, counts.new);
    ensureCmpRows(nCmp);
    for (var i = 0; i < nCmp; i++) {
      var oL = olds[i] || ZERO, nL = news[i] || ZERO;
      $("cmp" + i + "-name").textContent =
        (i < counts.old ? lineName("old", i) : "—") + " → " + (i < counts.new ? lineName("new", i) : "—");
      $("cmp" + i + "-seats").innerHTML = deltaHtml(CALC.pctChange(oL.seats, nL.seats));
      $("cmp" + i + "-arpu").innerHTML = deltaHtml(CALC.pctChange(oL.pupy, nL.pupy));
      $("cmp" + i + "-arpa").innerHTML = deltaHtml(CALC.pctChange(oL.arpa, nL.arpa));
      $("cmp" + i + "-acv").innerHTML = deltaHtml(CALC.pctChange(oL.facv, nL.facv));
      $("cmp" + i + "-tcv").innerHTML = deltaHtml(CALC.pctChange(oL.ftcv, nL.ftcv));
    }
    $("cmpT-seats").innerHTML = deltaHtml(CALC.pctChange(sum(olds, "seats"), sum(news, "seats")));
    $("cmpT-arpu").innerHTML = deltaHtml(CALC.pctChange(oPupy, nPupy));
    $("cmpT-arpa").innerHTML = deltaHtml(CALC.pctChange(oArpa, nArpa));
    $("cmpT-acv").innerHTML = deltaHtml(CALC.pctChange(sum(olds, "facv"), sum(news, "facv")));
    $("cmpT-tcv").innerHTML = deltaHtml(CALC.pctChange(sum(olds, "ftcv"), sum(news, "ftcv")));
    $("cmp-old").textContent = money(sum(olds, "facv")) + " / " + money(sum(olds, "ftcv"));
    $("cmp-new").textContent = money(sum(news, "facv")) + " / " + money(sum(news, "ftcv"));
    $("cmp-acv").textContent = pctFmt(CALC.pctChange(sum(olds, "facv"), sum(news, "facv")));
    $("cmp-tcv").textContent = pctFmt(CALC.pctChange(sum(olds, "ftcv"), sum(news, "ftcv")));

    /* PDL / SKU-mix checks on the proposed deal (model §6 sample rules) */
    var totalNewSeats = sum(news, "seats");
    var entSeats = 0, bizSeats = 0;
    for (var pi = 0; pi < counts.new; pi++) {
      var prod = PRODUCTS.filter(function (x) { return x.name === $("new" + pi + "-sku").value; })[0];
      if (prod && prod.fam === "enterprise") entSeats += news[pi].seats;
      if (prod && prod.fam === "business") bizSeats += news[pi].seats;
    }
    var floor = Math.max(0.15 * totalNewSeats, 100);
    var f1ok = entSeats >= floor;
    $("pdl-1-flag").className = "flag " + (f1ok ? "pass" : "fail");
    $("pdl-1-flag").textContent = f1ok ? "PASS" : "FAIL";
    $("pdl-1-text").textContent = "Each top-tier product family needs at least 15% of total seats or 100 seats, whichever is larger. Proposed: " +
      entSeats + " top-tier seats of " + totalNewSeats + " total — floor is " + Math.ceil(floor) + ".";
    var f2ok = bizSeats <= 300;
    $("pdl-2-flag").className = "flag " + (f2ok ? "pass" : "fail");
    $("pdl-2-flag").textContent = f2ok ? "PASS" : "FAIL";
    $("pdl-2-text").textContent = "Mid-tier products together may not exceed 300 seats when mixed with top-tier products. Proposed: " + bizSeats + " mid-tier seats.";

    /* usage lines + threshold concessions, both views */
    var ndu = [], oldu = [], newu = [];
    for (var ui1 = 0; ui1 < counts.ndu; ui1++) { var u1 = readUsage("ndu", ui1); paintUsage("ndu", ui1, u1); ndu.push(u1); }
    for (var ui2 = 0; ui2 < counts.oldu; ui2++) { var u2 = readUsage("oldu", ui2); paintUsage("oldu", ui2, u2); oldu.push(u2); }
    for (var ui3 = 0; ui3 < counts.newu; ui3++) { var u3 = readUsage("newu", ui3); paintUsage("newu", ui3, u3); newu.push(u3); }
    function paintLever(g, res) {
      $(g + "-units").textContent = String(res.units);
      var st = $(g + "-status");
      st.className = "flag " + (res.triggered ? "pass" : "warn");
      st.textContent = res.triggered ? "CONCESSION ACTIVE" : "NOT REACHED";
      $(g + "-after").textContent = money(res.after);
      return res;
    }
    var g1 = paintLever("g1", CALC.threshold(ndu, $("g1-meter").value, num("g1-threshold"), num("g1-extra") / 100));
    var g2 = paintLever("g2", CALC.threshold(newu, $("g2-meter").value, num("g2-threshold"), num("g2-extra") / 100));
    var sumNet = function (arr) { return arr.reduce(function (a, u) { return a + u.net; }, 0); };
    var ndUsageMo = sumNet(ndu) - g1.off;
    var dealYears = counts.nd ? num("nd0-months") / 12 : 0;
    $("nd-usageyr").textContent = money(ndUsageMo * 12);
    $("nd-fulltcv").textContent = money(totTcv + ndUsageMo * 12 * dealYears);
    var oldUsageMo = sumNet(oldu);
    var newUsageMo = sumNet(newu) - g2.off;
    $("cmp-uold").textContent = money(oldUsageMo);
    $("cmp-unew").textContent = money(newUsageMo);
    $("cmp-udelta").textContent = pctFmt(CALC.pctChange(oldUsageMo, newUsageMo));
  }

  document.addEventListener("input", recompute);
  document.addEventListener("change", recompute);
  recompute();
})();

