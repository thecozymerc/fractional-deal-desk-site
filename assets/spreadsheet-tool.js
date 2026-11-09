/* ==========================================================================
   LABEL — Spreadsheet Tool Engine (shared; serves every tool page)
   What this file does: renders one of Lucky's workbooks on a web page as
   the actual spreadsheet — same sheets (as tabs), same rows, same words,
   same values. Yellow INPUT cells are live: a visitor can type in them,
   and the sheet recalculates with its OWN formulas, run by the formula
   engine (assets/formula-engine.js). Formula cells show computed values
   only — a formula is never written to the page (Lucky's rule, Nov 8,
   2026: embed the actual sheet, usable, without showing the formulas).
   Each tool supplies ONE data file, converted from the workbook by
   convert-workbook.py: cell text, input values, number formats, and the
   formulas as machinery. Nothing about a sheet's math is re-implemented
   by hand — if the workbook changes, re-run the converter and the page
   is the new workbook.
   Map: site/CODE-MAP.md ("assets/"). No libraries, no tracking.
   Rule: any change here is recorded in site/CHANGELOG.md with the CODE-MAP
   updated in the same change (Code Labeling System, Rule 3).
   ========================================================================== */
window.renderWorkbook = function (container, data) {
  if (!container || !data || !window.FormulaEngine) return;

  function fmtValue(v, fmt) {
    if (v === "" || v === null || v === undefined) return "";
    if (typeof v === "string") return v;
    if (typeof v === "boolean") return v ? "TRUE" : "FALSE";
    if (fmt === "money") return v.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    if (fmt === "pct") return (v * 100).toFixed(2) + "%";
    if (fmt === "int") return String(Math.round(v));
    return String(Math.round(v * 100) / 100);
  }
  function colIndex(addr) {
    var letters = addr.match(/^[A-Z]+/)[0], n = 0;
    for (var i = 0; i < letters.length; i++) n = n * 26 + (letters.charCodeAt(i) - 64);
    return n;
  }

  var tabBar = document.createElement("div");
  tabBar.className = "wb-tabs";
  var panels = [];

  data.sheets.forEach(function (sheet, si) {
    /* Build the calculation sheet from the workbook's own cells. */
    var cellsMap = {};
    sheet.rows.forEach(function (row) {
      row.cells.forEach(function (c) {
        if (c.t === "formula") cellsMap[c.a] = { kind: "formula", value: c.f };
        else cellsMap[c.a] = { kind: "value", value: c.v };
      });
    });
    var calc = window.FormulaEngine.createSheet(cellsMap);
    var outSpans = {};       /* formula cell address -> span element */
    var cellFmt = {};        /* formula cell address -> number format */

    var tab = document.createElement("button");
    tab.type = "button";
    tab.className = "wb-tab" + (si === 0 ? " active" : "");
    tab.textContent = sheet.name;
    tab.addEventListener("click", function () {
      panels.forEach(function (p, pi) {
        p.style.display = pi === si ? "" : "none";
        tabBar.children[pi].classList.toggle("active", pi === si);
      });
    });
    tabBar.appendChild(tab);

    var panel = document.createElement("div");
    panel.className = "wb-panel";
    if (si !== 0) panel.style.display = "none";
    var scroll = document.createElement("div");
    scroll.className = "wb-scroll";
    var table = document.createElement("table");
    table.className = "wb-table";

    sheet.rows.forEach(function (row, ri) {
      var tr = document.createElement("tr");
      if (row.span) {
        var td = document.createElement("td");
        td.colSpan = sheet.cols;
        var text = row.cells[0].v;
        td.textContent = text;
        td.className = "wb-span" + (ri === 0 ? " wb-title" :
          (text.length < 70 && !/[.]$/.test(text) ? " wb-head" : ""));
        tr.appendChild(td);
      } else {
        var byCol = {};
        row.cells.forEach(function (c) { byCol[colIndex(c.a)] = c; });
        for (var col = 1; col <= sheet.cols; col++) {
          var td2 = document.createElement("td");
          var c2 = byCol[col];
          if (c2) {
            if (c2.t === "text") {
              td2.textContent = c2.v;
            } else if (c2.t === "value") {
              td2.textContent = fmtValue(c2.v, c2.fmt);
              td2.className = "num";
            } else if (c2.t === "input") {
              var input = document.createElement("input");
              input.className = "wb-input";
              input.setAttribute("aria-label", c2.a);
              if (typeof c2.v === "string") {
                input.type = "text";
                input.value = c2.v;
                input.addEventListener("input", function () {
                  calc.set(c2.a, input.value);
                  recompute();
                });
              } else {
                input.type = "number";
                input.step = "any";
                input.inputMode = "decimal";
                input.value = c2.fmt === "pct" ? +(c2.v * 100).toFixed(4) : c2.v;
                input.addEventListener("input", function () {
                  var raw = parseFloat(input.value);
                  calc.set(c2.a, isNaN(raw) ? 0 : (c2.fmt === "pct" ? raw / 100 : raw));
                  recompute();
                });
              }
              td2.appendChild(input);
              if (c2.fmt === "pct") td2.appendChild(document.createTextNode(" %"));
              td2.className = "num";
            } else if (c2.t === "formula") {
              var span = document.createElement("span");
              span.className = "wb-out";
              td2.appendChild(span);
              outSpans[c2.a] = span;
              cellFmt[c2.a] = c2.fmt;
              td2.className = "num";
            }
          }
          tr.appendChild(td2);
        }
      }
      table.appendChild(tr);
    });

    /* Charts defined in the workbook itself: drawn from the same computed
       cells, and redrawn whenever an input changes. X labels come from the
       header row directly above the first series (the sheet's own labels). */
    var chartBoxes = [];
    function rangeAddrs(from, to) {
      function split(a) {
        var m = /^([A-Z]+)([0-9]+)$/.exec(a);
        var n = 0;
        for (var i = 0; i < m[1].length; i++) n = n * 26 + (m[1].charCodeAt(i) - 64);
        return { c: n, r: parseInt(m[2], 10) };
      }
      function name(n) {
        var s = "";
        while (n > 0) { var r = (n - 1) % 26; s = String.fromCharCode(65 + r) + s; n = Math.floor((n - 1) / 26); }
        return s;
      }
      var a = split(from), b = split(to), out = [];
      for (var r = a.r; r <= b.r; r++) for (var c = a.c; c <= b.c; c++) out.push(name(c) + r);
      return out;
    }
    (sheet.charts || []).forEach(function (chart) {
      var box = document.createElement("div");
      box.className = "wb-chart";
      var h = document.createElement("p");
      h.className = "wb-chart-title";
      h.textContent = chart.title || "Chart";
      box.appendChild(h);
      var holder = document.createElement("div");
      box.appendChild(holder);
      var legend = document.createElement("p");
      legend.className = "wb-chart-legend";
      legend.textContent = chart.series.map(function (s) { return s.name; }).join("  ·  ");
      box.appendChild(legend);
      panel.appendChild(box);
      chartBoxes.push({ chart: chart, holder: holder });
    });
    var CHART_COLORS = ["#1B2A41", "#0E6B5C", "#A97B12", "#6B4E8E"];
    function drawCharts() {
      chartBoxes.forEach(function (cb) {
        var seriesData = cb.chart.series.map(function (s, i) {
          return {
            name: s.name, color: CHART_COLORS[i % CHART_COLORS.length],
            values: rangeAddrs(s.from, s.to).map(function (a) { return calc.get(a); })
          };
        });
        var n = seriesData.length ? seriesData[0].values.length : 0;
        var nums = [];
        seriesData.forEach(function (s) { s.values.forEach(function (v) { if (typeof v === "number") nums.push(v); }); });
        if (!n || !nums.length) { cb.holder.innerHTML = ""; return; }
        var min = Math.min.apply(null, nums.concat([0])), max = Math.max.apply(null, nums);
        var W = 640, H = 250, L = 64, R = 12, T = 10, B = 26;
        function X(i) { return L + (W - L - R) * (n === 1 ? 0.5 : i / (n - 1)); }
        function Y(v) { return T + (H - T - B) * (1 - (v - min) / ((max - min) || 1)); }
        var svg = '<svg viewBox="0 0 ' + W + " " + H + '" role="img" style="width:100%;height:auto;display:block">';
        [0, 0.5, 1].forEach(function (f) {
          var v = min + (max - min) * f, y = Y(v);
          svg += '<line x1="' + L + '" y1="' + y + '" x2="' + (W - R) + '" y2="' + y + '" stroke="#D8D8D2" stroke-width="1"/>';
          svg += '<text x="' + (L - 6) + '" y="' + (y + 4) + '" text-anchor="end" font-size="11" fill="#5A6572">' +
            Math.round(v).toLocaleString("en-US") + "</text>";
        });
        for (var i = 0; i < n; i++) {
          svg += '<text x="' + X(i) + '" y="' + (H - 8) + '" text-anchor="middle" font-size="11" fill="#5A6572">Year ' + (i + 1) + "</text>";
        }
        seriesData.forEach(function (s) {
          var pts = s.values.map(function (v, i) {
            return (typeof v === "number") ? X(i).toFixed(1) + "," + Y(v).toFixed(1) : null;
          }).filter(Boolean).join(" ");
          if (pts) svg += '<polyline fill="none" stroke="' + s.color + '" stroke-width="2.5" points="' + pts + '"/>';
        });
        svg += "</svg>";
        cb.holder.innerHTML = svg;
      });
    }

    function recompute() {
      Object.keys(outSpans).forEach(function (addr) {
        outSpans[addr].textContent = fmtValue(calc.get(addr), cellFmt[addr]);
      });
      drawCharts();
    }
    recompute();

    scroll.appendChild(table);
    panel.appendChild(scroll);
    panels.push(panel);
    container.appendChild(panel);
  });

  container.insertBefore(tabBar, container.firstChild);
};
