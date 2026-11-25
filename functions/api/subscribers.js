const json = (o, s = 200) => new Response(JSON.stringify(o), {
  status: s, headers: { "content-type": "application/json", "cache-control": "no-store" }
});
export async function onRequestGet({ request, env }) {
  const k = new URL(request.url).searchParams.get("key") || "";
  if (!env.SUBS_KEY || k !== env.SUBS_KEY) return json({ ok: false, error: "unauthorized" }, 401);
  const out = [];
  let cursor = null;
  for (let i = 0; i < 20; i++) {
    const page = await env.SUBS.list({ prefix: "sub:", cursor });
    for (const key of page.keys) {
      const v = await env.SUBS.get(key.name, "json");
      if (v && v.email) out.push(v);
    }
    if (page.list_complete) break;
    cursor = page.cursor;
  }
  out.sort((a, b) => String(a.added).localeCompare(String(b.added)));
  return json({ ok: true, count: out.length, subscribers: out });
}
