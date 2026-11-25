const EMAIL = /^[^@\s]+@[^@\s]+\.[a-z]{2,}$/i;
const json = (o, s = 200) => new Response(JSON.stringify(o), {
  status: s, headers: { "content-type": "application/json", "cache-control": "no-store" }
});
async function digest(v) {
  const b = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(v));
  return [...new Uint8Array(b)].map((x) => x.toString(16).padStart(2, "0")).join("");
}
export async function onRequestPost({ request, env }) {
  if (!env.SUBS) return json({ ok: false, error: "storage_unbound" }, 500);
  let email = "", source = "";
  const ct = request.headers.get("content-type") || "";
  if (ct.includes("application/json")) {
    const b = await request.json().catch(() => null);
    if (b) { email = b.email || ""; source = b.source || ""; }
  } else {
    const f = await request.formData().catch(() => null);
    if (f) { email = f.get("email") || ""; source = f.get("source") || ""; }
  }
  email = String(email).trim().toLowerCase();
  if (!EMAIL.test(email) || email.length > 254) return json({ ok: false, error: "invalid_email" }, 400);
  const key = "sub:" + await digest(email);
  await env.SUBS.put(key, JSON.stringify({
    email,
    added: new Date().toISOString(),
    source: String(source).slice(0, 80),
    country: request.headers.get("cf-ipcountry") || "",
  }), { expirationTtl: 31536000 * 5 });
  return json({ ok: true });
}
export async function onRequestGet() {
  return json({ ok: false, error: "POST only" }, 405);
}
