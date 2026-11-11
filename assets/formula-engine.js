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

  /* A cell that does not exist is EMPTY — distinct from a formula that
     produced "" and from a stored blank. Excel coerces it by context:
     0 as a formula result or in arithmetic, "" in text, blank in
     comparisons and ISBLANK. (Perm Calculator, Nov 11, 2026.) */
  var EMPTY = { __formulaEngineEmpty: true };
  function isEmpty(v) { return v === EMPTY; }
  /* A formula whose result is a bare reference to an empty cell holds a
     PHANTOM (verified against LibreOffice, Nov 11, 2026): it reads as 0
     as a value, in arithmetic and in concatenation, yet still compares
     equal to "" — while a direct reference to the empty cell itself
     concatenates as "" and is blank for ISBLANK. */
  var PHANTOM = { __formulaEnginePhantom: true };
  function isError(v) { return typeof v === "string" && /^#(DIV\/0!|N\/A|REF!|VALUE!|NUM!|NAME\?)/.test(v); }
  function isPhantom(v) { return v === PHANTOM; }
  function truthy(v) { return isEmpty(v) || isPhantom(v) ? false : !!v; }

  function tokenize(src) {
    var tokens = [], i = 0, n = src.length;
    while (i < n) {
      var ch = src[i];
      if (ch === " " || ch === "\t" || ch === "\n" || ch === "\r") { i++; continue; }
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
      if (ch === "'") {
        var q = "", j2 = i + 1;
        while (j2 < n) {
          if (src[j2] === "'") {
            if (src[j2 + 1] === "'") { q += "'"; j2 += 2; continue; }
            break;
          }
          q += src[j2]; j2++;
        }
        tokens.push({ t: "sheet", v: q }); i = j2 + 1; continue;
      }
      if (/[A-Za-z_$]/.test(ch)) {
        var m2 = /^[A-Za-z_$][A-Za-z0-9_.$]*/.exec(src.slice(i));
        tokens.push({ t: "id", v: m2[0] }); i += m2[0].length; continue;
      }
      var two = src.substr(i, 2);
      if (two === "<=" || two === ">=" || two === "<>") { tokens.push({ t: "op", v: two }); i += 2; continue; }
      if ("+-*/^%&=<>(),:!".indexOf(ch) >= 0) { tokens.push({ t: "op", v: ch }); i++; continue; }
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
    function parseArg() {
      /* Type check matters: a string literal "," is a value, not a separator. */
      if (peek().t === "op" && (peek().v === "," || peek().v === ")")) return { k: "str", v: "" };
      return parseExpr();
    }
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
      if (t.t === "sheet" || (t.t === "id" && peek().v === "!")) {
        var sheetName = t.v;
        next(); /* consume ! */
        var rt = next();
        var rref = rt.v.replace(/\$/g, "").toUpperCase();
        if (peek().v === ":") {
          next();
          var rt2 = next();
          var rref2 = rt2.v.replace(/\$/g, "").toUpperCase();
          return { k: "range", sheet: sheetName, from: rref, to: rref2 };
        }
        return { k: "ref", sheet: sheetName, addr: rref };
      }
      if (t.t === "id") {
        var name = t.v;
        if (peek().v === "(") {
          next();
          var args = [];
          if (peek().v !== ")") {
            args.push(parseArg());
            while (peek().t === "op" && peek().v === ",") { next(); args.push(parseArg()); }
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

  function createSheet(cells, opts) {
    var cache = {}, busy = {};
    var asts = {};
    var resolver = (opts && opts.resolve) || null;
    function getCell(sheet, addr) {
      if (!sheet) return rawGet(addr);
      if (resolver) return resolver(sheet, addr);
      return "#REF!";
    }

    function rawGet(addr) {
      var c = cells[addr];
      if (!c) return EMPTY;                      /* blank cell */
      if (c.kind === "value") return c.value;
      if (Object.prototype.hasOwnProperty.call(cache, addr)) return cache[addr];
      if (busy[addr]) throw new Error("formula-engine: circular reference at " + addr);
      busy[addr] = true;
      try {
        if (!asts[addr]) asts[addr] = parse(c.value.charAt(0) === "=" ? c.value.slice(1) : c.value);
        var v = evaluate(asts[addr]);
        if (isEmpty(v)) v = PHANTOM;   /* bare reference to an empty cell */
        cache[addr] = v;
        return v;
      } finally { delete busy[addr]; }
    }

    function toNum(v) {
      if (v === null || v === undefined || isEmpty(v) || isPhantom(v)) return 0;
      if (typeof v === "number") return v;
      if (typeof v === "boolean") return v ? 1 : 0;
      if (v === "") return 0;
      var n = parseFloat(v);
      if (isNaN(n)) throw new Error("#VALUE!");
      return n;
    }
    function toText(v) {
      if (v === null || v === undefined || isEmpty(v)) return "";
      if (isPhantom(v)) return "0";
      if (typeof v === "boolean") return v ? "TRUE" : "FALSE";
      if (typeof v === "number") {
        /* Excel converts a number to text with at most 15 significant
           digits (LibreOffice agrees); JS String() prints up to 17 and
           made concatenated ratios carry phantom digits (Perm E2). */
        if (!isFinite(v)) return String(v);
        var s = v.toPrecision(15);
        if (s.indexOf("e") >= 0 || s.indexOf("E") >= 0) {
          var ep = s.split(/[eE]/), mant = ep[0], ex = parseInt(ep[1], 10);
          var neg = mant.charAt(0) === "-"; if (neg) mant = mant.slice(1);
          var digits = mant.replace(".", ""), dot = mant.indexOf(".") < 0 ? mant.length : mant.indexOf(".");
          var point = dot + ex;
          if (point <= 0) s = "0." + "0".repeat(-point) + digits;
          else if (point >= digits.length) s = digits + "0".repeat(point - digits.length);
          else s = digits.slice(0, point) + "." + digits.slice(point);
          if (neg) s = "-" + s;
        }
        if (s.indexOf(".") >= 0) s = s.replace(/0+$/, "").replace(/\.$/, "");
        return s;
      }
      return String(v);
    }
    function compare(op, l, r) {
      var ln = typeof l === "number" || (l !== null && l !== "" && !isNaN(parseFloat(l)) && typeof l !== "string"),
          rn = typeof r === "number" || (r !== null && r !== "" && !isNaN(parseFloat(r)) && typeof r !== "string");
      var a, b;
      if (typeof l === "number" && typeof r === "number") { a = l; b = r; }
      else if (typeof l === "string" && typeof r === "string") { a = l.toLowerCase(); b = r.toLowerCase(); }
      else if (l === null || r === null || isEmpty(l) || isEmpty(r) || isPhantom(l) || isPhantom(r)) {
        /* Excel: a blank cell compares as "" against text and as 0 against
           numbers. (Treating blank as 0 against "" made blank <> "" true,
           which shifted the Perm Calculator's list-extraction idiom by one.) */
        a = (l === null || isEmpty(l) || isPhantom(l)) ? (typeof r === "string" ? "" : 0) : l;
        b = (r === null || isEmpty(r) || isPhantom(r)) ? (typeof l === "string" ? "" : 0) : r;
        if (typeof a === "string") a = a.toLowerCase(); if (typeof b === "string") b = b.toLowerCase();
      }
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
    function isArr(v) { return Array.isArray(v); }
    function broadcast(l, r, fn) {
      if (isArr(l) && isArr(r)) {
        var out = [], n = Math.max(l.length, r.length);
        for (var i = 0; i < n; i++) out.push(fn(l[i], r[i]));
        return out;
      }
      if (isArr(l)) return l.map(function (x) { return fn(x, r); });
      if (isArr(r)) return r.map(function (x) { return fn(l, x); });
      return fn(l, r);
    }
    function rangeAddrs(node) {
      var a = splitAddr(node.from), b = splitAddr(node.to), out = [];
      for (var r = Math.min(a.row, b.row); r <= Math.max(a.row, b.row); r++)
        for (var c = Math.min(a.col, b.col); c <= Math.max(a.col, b.col); c++)
          out.push(colName(c) + r);
      return out;
    }
    function criteriaMatch(value, criteria) {
      if (isEmpty(value)) value = null;
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
        if (isError(cond)) return cond;
        if (isEmpty(cond) || isPhantom(cond)) cond = false;
        if (isArr(cond)) {
          var tv = ev(args[1]), fv = args.length > 2 ? ev(args[2]) : false;
          return cond.map(function (c, i) {
            var t = isArr(tv) ? tv[i] : tv, f = isArr(fv) ? fv[i] : fv;
            return c ? t : f;
          });
        }
        return cond ? ev(args[1]) : (args.length > 2 ? ev(args[2]) : false);
      },
      IFERROR: function (args, ev) {
        try { var v = ev(args[0]); return isError(v) ? ev(args[1]) : v; }
        catch (e) { return ev(args[1]); }
      },
      SUM: function (args, ev) {
        var total = 0;
        args.forEach(function (a) {
          if (a.k === "range") rangeAddrs(a).forEach(function (addr) {
            var v = getCell(a.sheet, addr); if (typeof v === "number") total += v;
          });
          else { var v2 = ev(a); if (isArr(v2)) v2.forEach(function (x) { if (typeof x === "number") total += x; }); else if (typeof v2 === "number") total += v2; }
        });
        return total;
      },
      COUNT: function (args, ev) {
        var n = 0;
        args.forEach(function (a) {
          if (a.k === "range") rangeAddrs(a).forEach(function (addr) { if (typeof getCell(a.sheet, addr) === "number") n++; });
          else if (typeof ev(a) === "number") n++;
        });
        return n;
      },
      COUNTA: function (args, ev) {
        var n = 0;
        args.forEach(function (a) {
          if (a.k === "range") rangeAddrs(a).forEach(function (addr) {
            var v = getCell(a.sheet, addr); if (v !== null && v !== "" && !isEmpty(v)) n++;
          });
          else { var v2 = ev(a); if (v2 !== null && v2 !== "" && !isEmpty(v2)) n++; }
        });
        return n;
      },
      COUNTIF: function (args, ev) {
        var addrs = rangeAddrs(args[0]), crit = ev(args[1]), n = 0;
        addrs.forEach(function (addr) { if (criteriaMatch(getCell(args[0].sheet, addr), crit)) n++; });
        return n;
      },
      SUMIF: function (args, ev) {
        var addrs = rangeAddrs(args[0]), crit = ev(args[1]), n = 0;
        var sumAddrs = args.length > 2 ? rangeAddrs(args[2]) : addrs;
        addrs.forEach(function (addr, i) {
          if (criteriaMatch(getCell(args[0].sheet, addr), crit)) {
            var v = getCell((args.length > 2 ? args[2] : args[0]).sheet, sumAddrs[i]); if (typeof v === "number") n += v;
          }
        });
        return n;
      },
      AVERAGE: function (args, ev) {
        var total = 0, n = 0;
        args.forEach(function (a) {
          if (a.k === "range") rangeAddrs(a).forEach(function (addr) {
            var v = getCell(a.sheet, addr); if (typeof v === "number") { total += v; n++; }
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
            return getCell(args[0].sheet, colName(a.col + c - 1) + (a.row + r - 1));
          }
          var n = toNum(ev(args[1]));
          return getCell(args[0].sheet, addrs[n - 1]);
        }
        return ev(args[0]);
      },
      MATCH: function (args, ev) {
        var lookup = ev(args[0]), addrs = rangeAddrs(args[1]);
        for (var i = 0; i < addrs.length; i++) {
          var v = getCell(args[1].sheet, addrs[i]);
          var hit = (typeof v === "number" && typeof lookup === "number") ? v === lookup
            : (typeof v === "string" && typeof lookup === "string")
              ? v.toLowerCase() === lookup.toLowerCase() : v === lookup;
          if (hit) return i + 1;
        }
        return "#N/A";
      },
      ROW: function (args, ev) {
        if (!args.length) throw new Error("formula-engine: ROW needs an argument");
        var a = args[0];
        if (a.k === "range") {
          var fa = splitAddr(a.from), ta = splitAddr(a.to), rows = [];
          if (fa.col === ta.col) { for (var r = fa.row; r <= ta.row; r++) rows.push(r); }
          else { for (var r2 = Math.min(fa.row, ta.row); r2 <= Math.max(fa.row, ta.row); r2++) rows.push(r2); }
          return rows;
        }
        if (a.k === "ref") return splitAddr(a.addr).row;
        throw new Error("formula-engine: ROW of a non-reference");
      },
      SMALL: function (args, ev) {
        var vals = [];
        function collect(v) {
          if (isArr(v)) { v.forEach(collect); return; }
          if (typeof v === "number") vals.push(v);
        }
        if (args[0].k === "range") rangeAddrs(args[0]).forEach(function (addr) { collect(getCell(args[0].sheet, addr)); });
        else collect(ev(args[0]));
        vals.sort(function (x, y) { return x - y; });
        var k = toNum(ev(args[1]));
        if (k < 1 || k > vals.length) throw new Error("#NUM!");
        return vals[k - 1];
      },
      CONCATENATE: function (args, ev) {
        var out = "";
        args.forEach(function (a) {
          if (a.k === "range") rangeAddrs(a).forEach(function (addr) { out += toText(getCell(a.sheet, addr)); });
          else out += toText(ev(a));
        });
        return out;
      },
      TEXTJOIN: function (args, ev) {
        var delim = toText(ev(args[0])), skip = args.length > 1 ? !!ev(args[1]) : false, parts = [];
        function push(v) { if (skip && (v === null || v === "" || isEmpty(v))) return; parts.push(toText(v)); }
        args.slice(2).forEach(function (a) {
          if (a.k === "range") rangeAddrs(a).forEach(function (addr) { push(getCell(a.sheet, addr)); });
          else push(ev(a));
        });
        return parts.join(delim);
      },
      ISBLANK: function (args, ev) {
        var a = args[0];
        if (a.k === "ref" && !a.sheet) {
          var c = cells[a.addr];
          if (!c) return true;
          if (c.kind === "formula") return false;
          return c.value === null || c.value === undefined || c.value === "";
        }
        var v;
        try { v = ev(a); } catch (e) { return false; }
        return v === null || v === undefined || v === "" || isEmpty(v);
      },
      ROUNDUP: function (args, ev) {
        var x = toNum(ev(args[0])), d = args.length > 1 ? toNum(ev(args[1])) : 0, f = Math.pow(10, d);
        return Math.sign(x) * Math.ceil(Math.abs(x) * f - 1e-10) / f;
      },
      TEXT: function (args, ev) {
        var v = ev(args[0]), fmt = toText(ev(args[1]));
        if (isError(v)) return v;
        if (fmt === "") return "";
        if (typeof v === "string") return v;
        if (v === null || v === undefined) return "";
        var num = toNum(v);
        if (/^dd\/mm\/yyyy$/i.test(fmt)) {
          var dt = new Date(Math.round((num - 25569) * 86400 * 1000));
          function p2(x) { return (x < 10 ? "0" : "") + x; }
          return p2(dt.getUTCDate()) + "/" + p2(dt.getUTCMonth() + 1) + "/" + dt.getUTCFullYear();
        }
        var pct = fmt.indexOf("%") >= 0;
        var dollar = fmt.indexOf("$") >= 0;
        var group = fmt.indexOf(",") >= 0;
        var dotAt = fmt.indexOf(".");
        var dp = 0;
        if (dotAt >= 0) { var m = /^0+/.exec(fmt.slice(dotAt + 1)); dp = m ? m[0].length : 0; }
        var scaled = pct ? num * 100 : num;
        var fixed = scaled.toFixed(dp);
        var neg = fixed.charAt(0) === "-";
        if (neg) fixed = fixed.slice(1);
        var parts = fixed.split("."), int = parts[0], frac = parts.length > 1 ? parts[1] : "";
        if (group) int = int.replace(/\B(?=(\d{3})+(?!\d))/g, ",");
        return (neg ? "-" : "") + (dollar ? "$" : "") + int + (dp > 0 ? "." + frac : "") + (pct ? "%" : "");
      },
      AND: function (args, ev) { return args.every(function (a) { return truthy(ev(a)); }); },
      OR: function (args, ev) { return args.some(function (a) { return truthy(ev(a)); }); },
      NOT: function (args, ev) { return !truthy(ev(args[0])); }
    };

    function evaluate(node) {
      switch (node.k) {
        case "num": return node.v;
        case "str": return node.v;
        case "bool": return node.v;
        case "ref": return getCell(node.sheet, node.addr);
        case "neg": {
          var nv = evaluate(node.x);
          return isArr(nv) ? nv.map(function (x) { return -toNum(x); }) : -toNum(nv);
        }
        case "pct": {
          var pv = evaluate(node.x);
          return isArr(pv) ? pv.map(function (x) { return toNum(x) / 100; }) : toNum(pv) / 100;
        }
        case "cat": return broadcast(evaluate(node.l), evaluate(node.r), function (a, b) {
          if (isError(a)) return a;
          if (isError(b)) return b;
          return toText(a) + toText(b);
        });
        case "bin": {
          var binFn = function (a, b) {
            var l = toNum(a), r = toNum(b);
            switch (node.op) {
              case "+": return l + r;
              case "-": return l - r;
              case "*": return l * r;
              case "/": return r === 0 ? "#DIV/0!" : l / r;
              case "^": return Math.pow(l, r);
            }
          };
          return broadcast(evaluate(node.l), evaluate(node.r), binFn);
        }
        case "cmp": return broadcast(evaluate(node.l), evaluate(node.r), function (a, b) { return compare(node.op, a, b); });
        case "call": {
          var fn = FUNCS[node.name];
          if (!fn) throw new Error("formula-engine: unsupported function " + node.name);
          return fn(node.args, evaluate);
        }
        case "range":
          return rangeAddrs(node).map(function (addr) { return getCell(node.sheet, addr); });
      }
      throw new Error("formula-engine: bad node");
    }

    return {
      get: function (addr) { var v = rawGet(addr); return isPhantom(v) ? 0 : v; },
      set: function (addr, rawValue) {
        cells[addr] = { kind: "value", value: rawValue };
        cache = {};
      },
      invalidate: function () { cache = {}; }
    };
  }

  return { createSheet: createSheet, _parse: parse };
})();
