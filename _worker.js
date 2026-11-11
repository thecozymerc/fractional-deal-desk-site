// ==========================================================================
// LABEL — _worker.js — Cloudflare Pages advanced-mode worker for the site.
// What this file does: serves the static site through env.ASSETS, and runs
// ONE dynamic route — POST /api/analyze, the Contract Analyzer's AI read
// (Tool 13, S6-P03.4). The AI provider key is read from the Pages project's
// secret env vars (GEMINI_API_KEY, or OPENAI_API_KEY, or ANTHROPIC_API_KEY)
// — never from code, never shipped to the browser. If no key is configured
// the route answers 501 {error:"not_configured"} and the tool page says so
// plainly; the analyzer's own scan never touches this route and never
// leaves the visitor's device.
// Guards: POST only, JSON body, text capped at 60,000 characters, output
// capped, strict-JSON answer contract {summary, key_terms, watch_out,
// missing}. Errors answer 502 with a plain message. Rule: changes are
// recorded in site/CHANGELOG.md + CODE-MAP like any other change.
// ==========================================================================
const SYSTEM = [
  "You read contracts for a deal-desk operator. From the contract text ONLY,",
  "write a plain-English read. Never invent clauses, numbers, dates or names",
  "that are not in the text. If something standard is absent, list it under",
  "missing. Answer with STRICT JSON only, no markdown, no code fences:",
  '{"summary": "3-5 sentences: who, what, how much, how long",',
  ' "key_terms": ["term — value, from the text", "..."],',
  ' "watch_out": ["one-sided, unusual, or risky language, quoting the idea in plain words", "..."],',
  ' "missing": ["standard item not found in the text", "..."]}'
].join(" ");

async function callAI(env, text) {
  const prompt = SYSTEM + "\n\nCONTRACT TEXT:\n" + text;
  if (env.GEMINI_API_KEY) {
    // New-user keys: gemini-2.5-flash is refused ("no longer available to
    // new users"); Google directs to gemini-3.8-flash. The free tier can
    // answer 503/overloaded under load, so a lighter model backs it up.
    const models = ["gemini-3.8-flash", "gemini-3.1-flash-lite"];
    let lastErr = null;
    for (const model of models) {
      try {
        const r = await fetch("https://generativelanguage.googleapis.com/v1beta/models/" + model + ":generateContent?key=" + env.GEMINI_API_KEY, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            contents: [{ parts: [{ text: prompt }] }],
            generationConfig: { responseMimeType: "application/json", maxOutputTokens: 1200, temperature: 0.2 }
          })
        });
        if (!r.ok) { lastErr = new Error("gemini " + r.status); continue; }
        const j = await r.json();
        return j.candidates[0].content.parts.map(p => p.text || "").join("");
      } catch (e) { lastErr = e; }
    }
    throw lastErr || new Error("gemini unavailable");
  }
  if (env.OPENAI_API_KEY) {
    const r = await fetch("https://api.openai.com/v1/chat/completions", {
      method: "POST",
      headers: { "Content-Type": "application/json", "Authorization": "Bearer " + env.OPENAI_API_KEY },
      body: JSON.stringify({
        model: "gpt-4o-mini", temperature: 0.2, max_tokens: 1200,
        response_format: { type: "json_object" },
        messages: [{ role: "user", content: prompt }]
      })
    });
    if (!r.ok) throw new Error("openai " + r.status);
    const j = await r.json();
    return j.choices[0].message.content;
  }
  if (env.ANTHROPIC_API_KEY) {
    const r = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: { "Content-Type": "application/json", "x-api-key": env.ANTHROPIC_API_KEY, "anthropic-version": "2023-06-01" },
      body: JSON.stringify({
        model: "claude-haiku-4-5", max_tokens: 1200, temperature: 0.2,
        messages: [{ role: "user", content: prompt }]
      })
    });
    if (!r.ok) throw new Error("anthropic " + r.status);
    const j = await r.json();
    return j.content.map(p => p.text || "").join("");
  }
  return null;
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname !== "/api/analyze") return env.ASSETS.fetch(request);
    const json = (status, obj) => new Response(JSON.stringify(obj), { status, headers: { "Content-Type": "application/json" } });
    if (request.method !== "POST") return json(405, { error: "POST only" });
    let body;
    try { body = await request.json(); } catch { return json(400, { error: "JSON body required" }); }
    const text = typeof body.text === "string" ? body.text.slice(0, 60000) : "";
    if (text.trim().length < 40) return json(400, { error: "text too short" });
    let raw;
    try { raw = await callAI(env, text); } catch (e) { return json(502, { error: "AI provider error: " + e.message }); }
    if (raw === null) return json(501, { error: "not_configured" });
    try {
      const cleaned = raw.replace(/```json|```/g, "").trim();
      const parsed = JSON.parse(cleaned);
      return json(200, {
        summary: String(parsed.summary || ""),
        key_terms: Array.isArray(parsed.key_terms) ? parsed.key_terms.map(String).slice(0, 12) : [],
        watch_out: Array.isArray(parsed.watch_out) ? parsed.watch_out.map(String).slice(0, 10) : [],
        missing: Array.isArray(parsed.missing) ? parsed.missing.map(String).slice(0, 10) : []
      });
    } catch { return json(502, { error: "AI answer was not readable JSON" }); }
  }
};
