/* ==========================================================================
   LABEL — Formula Engine (shared; serves every tool page)
   What this file does: evaluates the workbook's OWN formulas, in the
   visitor's browser, so an embedded sheet calculates exactly like the
   spreadsheet it came from — every formula in the file, nothing
   re-implemented by hand per tool. The renderer shows computed values
   only; a formula itself is never written to the page (Lucky's rule,
   Nov 8, 2026: embed the actual sheet, usable, without showing the
   formulas).
   Understands: + - * / ^ %, parentheses, unary minus, & (join text),
   comparisons (= <> < <= > >=), cell refs (A1, $A$1), ranges (A1:B9),
   and the functions IF, IFERROR, SUM, SUMIF, COUNT, COUNTA, COUNTIF,
   AVERAGE, MIN, MAX, ROUND, ABS, AND, OR, NOT, INDEX, MATCH (exact
   match). Semantics follow Excel:
   SUM ignores text in ranges, "" results stay "", text comparisons are
   case-insensitive, a blank cell is 0 in arithmetic.
   API: window.FormulaEngine.createSheet(cells) where cells maps a cell
   address to {kind: "value"|"formula", value} — returns {get(addr),
   set(addr, rawValue), invalidate()}.
   Map: site/CODE-MAP.md ("assets/"). No libraries, no tracking.
   Rule: any change here is recorded in site/CHANGELOG.md with the
   CODE-MAP updated in the same change (Code Labeling System, Rule 3).
   ========================================================================== */
window.FormulaEngine = (function () {

  function tokenize(src) {
    var tokens = [], i = 0, n = src.length;
    while (i < n) {
      var ch = src[i];
      if (ch === " " || ch === "\t") { i++; continue; }
      if (ch === '"') {
        var s = "", j = i + 1;
        while (j < n) {
          if (src[j] === '"') {
            if (src[j + 1] === '"') { s += '"'; j += 2; continue; }
            break;
          }
          s += src[j]; j++;
        }
        tokens.push({ t: "str", v: s }); i = j + 1; continue;
      }
      if (/[0-9.]/.test(ch)) {
        var m = /^[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?/.exec(src.slice(i));
        tokens.push({ t: "num", v: parseFloat(m[0]) }); i += m[0].length; continue;
      }
      if (/[A-Za-z_$]/.test(ch)) {
        var m2 = /^[A-Za-z_$][A-Za-z0-9_.$]*/.exec(src.slice(i));
        tokens.push({ t: "id", v: m2[0] }); i += m2[0].length; continue;
      }
      var two = src.substr(i, 2);
      if (two === "<=" || two === ">=" || two === "<>") { tokens.push({ t: "op", v: two }); i += 2; continue; }
      if ("+-*/^%&=<>(),:".indexOf(ch) >= 0) { tokens.push({ t: "op", v: ch }); i++; continue; }
      throw new Error("formula-engine: unexpected character " + ch);
    }
    tokens.push({ t: "end", v: "" });
    return tokens;
  }

  function parse(src) {
    var tokens = tokenize(src), pos = 0;
    function peek() { return tokens[pos]; }
    function next() { return tokens[pos++]; }
    function expect(v) { var t = next(); if (t.v !== v) throw new Error("formula-engine: expected " + v); }

    function parseExpr() { return parseCompare(); }
    function parseCompare() {
      var left = parseConcat();
      while (peek().t === "op" && ["=", "<>", "<", "<=", ">", ">="].indexOf(peek().v) >= 0) {
        var op = next().v;
        left = { k: "cmp", op: op, l: left, r: parseConcat() };
      }
      return left;
    }
    function parseConcat() {
      var left = parseAdd();
      while (peek().v === "&") { next(); left = { k: "cat", l: left, r: parseAdd() }; }
      return left;
    }
    function parseAdd() {
      var left = parseMul();
      while (peek().v === "+" || peek().v === "-") {
        var op = next().v;
        left = { k: "bin", op: op, l: left, r: parseMul() };
      }
      return left;
    }
    function parseMul() {
      var left = parsePow();
      while (peek().v === "*" || peek().v === "/") {
        var op = next().v;
        left = { k: "bin", op: op, l: left, r: parsePow() };
      }
      return left;
    }
    function parsePow() {
      var left = parseUnary();
      while (peek().v === "^") { next(); left = { k: "bin", op: "^", l: left, r: parseUnary() }; }
      return left;
    }
    function parseUnary() {
      if (peek().v === "-") { next(); return { k: "neg", x: parseUnary() }; }
      if (peek().v === "+") { next(); return parseUnary(); }
      return parsePostfix();
    }
    function parsePostfix() {
      var node = parsePrimary();
      while (peek().v === "%") { next(); node = { k: "pct", x: node }; }
      return node;
    }
    function parsePrimary() {
      var t = next();
      if (t.t === "num") return { k: "num", v: t.v };
      if (t.t === "str") return { k: "str", v: t.v };
      if (t.v === "(") { var e = parseExpr(); expect(")"); return e; }
      if (t.t === "id") {
        var name = t.v;
        if (peek().v === "(") {
          next();
          var args = [];
          if (peek().v !== ")") {
            args.push(parseExpr());
            while (peek().v === ",") { next(); args.push(parseExpr()); }
          }
          expect(")");
          return { k: "call", name: name.toUpperCase(), args: args };
        }
        if (/^(TRUE|FALSE)$/i.test(name)) return { k: "bool", v: name.toUpperCase() === "TRUE" };
        /* cell reference, optionally the start of a range */
        var ref = name.replace(/\$/g, "").toUpperCase();
        if (peek().v === ":") {
          next();
          var t2 = next();
          var ref2 = t2.v.replace(/\$/g, "").toUpperCase();
          return { k: "range", from: ref, to: ref2 };
        }
        return { k: "ref", addr: ref };
      }
      throw new Error("formula-engine: unexpected token " + t.v);
    }
    var ast = parseExpr();
    if (peek().t !== "end") throw new Error("formula-engine: trailing tokens");
    return ast;
  }

  function colNum(letters) {
    var n = 0;
    for (var i = 0; i < letters.length; i++) n = n * 26 + (letters.charCodeAt(i) - 64);
    return n;
  }
  function colName(n) {
    var s = "";
    while (n > 0) { var r = (n - 1) % 26; s = String.fromCharCode(65 + r) + s; n = Math.floor((n - 1) / 26); }
    return s;
  }
  function splitAddr(addr) {
    var m = /^([A-Z]+)([0-9]+)$/.exec(addr);
    return { col: colNum(m[1]), row: parseInt(m[2], 10) };
  }

  function createSheet(cells) {
    var cache = {}, busy = {};
    var asts = {};

    function rawGet(addr) {
      var c = cells[addr];
      if (!c) return null;                       /* blank cell */
      if (c.kind === "value") return c.value;
      if (Object.prototype.hasOwnProperty.call(cache, addr)) return cache[addr];
      if (busy[addr]) throw new Error("formula-engine: circular reference at " + addr);
      busy[addr] = true;
      try {
        if (!asts[addr]) asts[addr] = parse(c.value.charAt(0) === "=" ? c.value.slice(1) : c.value);
        var v = evaluate(asts[addr]);
        cache[addr] = v;
        return v;
      } finally { delete busy[addr]; }
    }

    function toNum(v) {
      if (v === null || v === undefined) return 0;
      if (typeof v === "number") return v;
      if (typeof v === "boolean") return v ? 1 : 0;
      if (v === "") return 0;
      var n = parseFloat(v);
      if (isNaN(n)) throw new Error("#VALUE!");
      return n;
    }
    function toText(v) {
      if (v === null || v === undefined) return "";
      if (typeof v === "boolean") return v ? "TRUE" : "FALSE";
      return String(v);
    }
    function compare(op, l, r) {
      var ln = typeof l === "number" || (l !== null && l !== "" && !isNaN(parseFloat(l)) && typeof l !== "string"),
          rn = typeof r === "number" || (r !== null && r !== "" && !isNaN(parseFloat(r)) && typeof r !== "string");
      var a, b;
      if (typeof l === "number" && typeof r === "number") { a = l; b = r; }
      else if (typeof l === "string" && typeof r === "string") { a = l.toLowerCase(); b = r.toLowerCase(); }
      else if (l === null || r === null) { a = l === null ? 0 : l; b = r === null ? 0 : r; if (typeof a === "string") a = a.toLowerCase(); if (typeof b === "string") b = b.toLowerCase(); }
      else { a = l; b = r; }
      switch (op) {
        case "=": return a === b;
        case "<>": return a !== b;
        case "<": return a < b;
        case "<=": return a <= b;
        case ">": return a > b;
        case ">=": return a >= b;
      }
    }
    function rangeAddrs(node) {
      var a = splitAddr(node.from), b = splitAddr(node.to), out = [];
      for (var r = Math.min(a.row, b.row); r <= Math.max(a.row, b.row); r++)
        for (var c = Math.min(a.col, b.col); c <= Math.max(a.col, b.col); c++)
          out.push(colName(c) + r);
      return out;
    }
    function criteriaMatch(value, criteria) {
      if (typeof criteria === "number") return typeof value === "number" && value === criteria;
      var s = String(criteria), m = /^(>=|<=|<>|>|<|=)(.*)$/.exec(s);
      if (m) {
        var target = isNaN(parseFloat(m[2])) ? m[2] : parseFloat(m[2]);
        return compare(m[1], value, target);
      }
      if (typeof value === "string") return value.toLowerCase() === s.toLowerCase();
      return value === criteria;
    }

    var FUNCS = {
      IF: function (args, ev) {
        var cond = ev(args[0]);
        return cond ? ev(args[1]) : (args.length > 2 ? ev(args[2]) : false);
      },
      IFERROR: function (args, ev) {
        try { return ev(args[0]); } catch (e) { return ev(args[1]); }
      },
      SUM: function (args, ev) {
        var total = 0;
        args.forEach(function (a) {
          if (a.k === "range") rangeAddrs(a).forEach(function (addr) {
            var v = rawGet(addr); if (typeof v === "number") total += v;
          });
          else { var v2 = ev(a); if (typeof v2 === "number") total += v2; }
        });
        return total;
      },
      COUNT: function (args, ev) {
        var n = 0;
        args.forEach(function (a) {
          if (a.k === "range") rangeAddrs(a).forEach(function (addr) { if (typeof rawGet(addr) === "number") n++; });
          else if (typeof ev(a) === "number") n++;
        });
        return n;
      },
      COUNTA: function (args, ev) {
        var n = 0;
        args.forEach(function (a) {
          if (a.k === "range") rangeAddrs(a).forEach(function (addr) {
            var v = rawGet(addr); if (v !== null && v !== "") n++;
          });
          else { var v2 = ev(a); if (v2 !== null && v2 !== "") n++; }
        });
        return n;
      },
      COUNTIF: function (args, ev) {
        var addrs = rangeAddrs(args[0]), crit = ev(args[1]), n = 0;
        addrs.forEach(function (addr) { if (criteriaMatch(rawGet(addr), crit)) n++; });
        return n;
      },
      SUMIF: function (args, ev) {
        var addrs = rangeAddrs(args[0]), crit = ev(args[1]), n = 0;
        var sumAddrs = args.length > 2 ? rangeAddrs(args[2]) : addrs;
        addrs.forEach(function (addr, i) {
          if (criteriaMatch(rawGet(addr), crit)) {
            var v = rawGet(sumAddrs[i]); if (typeof v === "number") n += v;
          }
        });
        return n;
      },
      AVERAGE: function (args, ev) {
        var total = 0, n = 0;
        args.forEach(function (a) {
          if (a.k === "range") rangeAddrs(a).forEach(function (addr) {
            var v = rawGet(addr); if (typeof v === "number") { total += v; n++; }
          });
          else { var v2 = ev(a); if (typeof v2 === "number") { total += v2; n++; } }
        });
        return n === 0 ? 0 : total / n;
      },
      MIN: function (args, ev) { return Math.min.apply(null, args.map(function (a) { return toNum(ev(a)); })); },
      MAX: function (args, ev) { return Math.max.apply(null, args.map(function (a) { return toNum(ev(a)); })); },
      ROUND: function (args, ev) {
        var x = toNum(ev(args[0])), d = args.length > 1 ? toNum(ev(args[1])) : 0, f = Math.pow(10, d);
        return Math.round(x * f) / f;
      },
      ABS: function (args, ev) { return Math.abs(toNum(ev(args[0]))); },
      INDEX: function (args, ev) {
        if (args[0].k === "range") {
          var addrs = rangeAddrs(args[0]);
          if (args.length > 2) {
            var a = splitAddr(args[0].from), r = toNum(ev(args[1])), c = toNum(ev(args[2]));
            return rawGet(colName(a.col + c - 1) + (a.row + r - 1));
          }
          var n = toNum(ev(args[1]));
          return rawGet(addrs[n - 1]);
        }
        return ev(args[0]);
      },
      MATCH: function (args, ev) {
        var lookup = ev(args[0]), addrs = rangeAddrs(args[1]);
        for (var i = 0; i < addrs.length; i++) {
          var v = rawGet(addrs[i]);
          var hit = (typeof v === "number" && typeof lookup === "number") ? v === lookup
            : (typeof v === "string" && typeof lookup === "string")
              ? v.toLowerCase() === lookup.toLowerCase() : v === lookup;
          if (hit) return i + 1;
        }
        return "#N/A";
      },
      AND: function (args, ev) { return args.every(function (a) { return !!ev(a); }); },
      OR: function (args, ev) { return args.some(function (a) { return !!ev(a); }); },
      NOT: function (args, ev) { return !ev(args[0]); }
    };

    function evaluate(node) {
      switch (node.k) {
        case "num": return node.v;
        case "str": return node.v;
        case "bool": return node.v;
        case "ref": return rawGet(node.addr);
        case "neg": return -toNum(evaluate(node.x));
        case "pct": return toNum(evaluate(node.x)) / 100;
        case "cat": return toText(evaluate(node.l)) + toText(evaluate(node.r));
        case "bin": {
          var l = toNum(evaluate(node.l)), r = toNum(evaluate(node.r));
          switch (node.op) {
            case "+": return l + r;
            case "-": return l - r;
            case "*": return l * r;
            case "/": return r === 0 ? "#DIV/0!" : l / r;
            case "^": return Math.pow(l, r);
          }
          break;
        }
        case "cmp": return compare(node.op, evaluate(node.l), evaluate(node.r));
        case "call": {
          var fn = FUNCS[node.name];
          if (!fn) throw new Error("formula-engine: unsupported function " + node.name);
          return fn(node.args, evaluate);
        }
        case "range": throw new Error("formula-engine: range outside a function");
      }
      throw new Error("formula-engine: bad node");
    }

    return {
      get: function (addr) { return rawGet(addr); },
      set: function (addr, rawValue) {
        cells[addr] = { kind: "value", value: rawValue };
        cache = {};
      },
      invalidate: function () { cache = {}; }
    };
  }

  return { createSheet: createSheet, _parse: parse };
})();
