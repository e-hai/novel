# -*- coding: utf-8 -*-
"""
generate.py — 精品小说静态站生成器（零第三方依赖）
从 content/ 读取 Markdown（front matter + 正文），生成：
  site/index.html              作品首页
  site/about/index.html        作品说明 + AI 披露 + 作者/审校声明
  site/chapters/<n>-<slug>/    每章正文页
  site/sitemap.xml, robots.txt

合规护栏：
  - 未人工终审（status != approved）的章节默认不发布；PREVIEW_DRAFTS=1 才显示且带草稿横幅
  - 每页可见 AI 披露（不伪造纯人类作者、不伪造头像履历）
  - schema 与可见内容一致；草稿页不宣称正式出版
"""
from __future__ import annotations

import hashlib
import html
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
import config as C
from locales import LOCALES, route, work

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
CHAPTERS_DIR = CONTENT / "chapters"
EDITORIAL_DIR = CONTENT / "editorial"


def revision_root() -> Path | None:
    if not C.REVISION_SET:
        return None
    if not C.PREVIEW_DRAFTS:
        raise ValueError("A revision is a preview-only draft; set PREVIEW_DRAFTS=1")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", C.REVISION_SET):
        raise ValueError("Invalid revision identifier")
    root = CONTENT / "revisions" / C.REVISION_SET
    if not (root / "chapters").is_dir() or not (root / "narrative-notes.json").is_file():
        raise ValueError("Revision chapters or narrative notes are missing")
    return root


def revision_notes() -> dict:
    root = revision_root()
    return json.loads((root / "narrative-notes.json").read_text(encoding="utf-8")) if root else {}


# ---------------------------------------------------------------------------
# 极简 front matter + Markdown 解析（够用即可，避免第三方依赖）
# ---------------------------------------------------------------------------
def parse_front_matter(text: str) -> tuple[dict, str]:
    meta: dict[str, str] = {}
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            header = text[3:end].strip("\n")
            for line in header.splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    value = v.strip()
                    if value.startswith('"') and value.endswith('"'):
                        try:
                            value = json.loads(value)
                        except json.JSONDecodeError:
                            value = value[1:-1]
                    elif value.startswith("'") and value.endswith("'"):
                        value = value[1:-1]
                    meta[k.strip()] = str(value)
            text = text[end + 4:].lstrip("\n")
    return meta, text


def md_inline(s: str) -> str:
    """行内 Markdown：加粗、斜体、行内代码。先转义，再替换。"""
    s = html.escape(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)
    return s


def md_to_html(md: str) -> str:
    """块级 Markdown：H1/H2/H3、段落、水平线。"""
    out: list[str] = []
    para: list[str] = []

    def flush():
        if para:
            out.append("<p>" + md_inline(" ".join(x.strip() for x in para)) + "</p>")
            para.clear()

    for line in md.splitlines():
        raw = line.rstrip()
        if not raw.strip():
            flush()
            continue
        if raw.startswith("# "):
            flush(); out.append(f"<h1>{md_inline(raw[2:].strip())}</h1>")
        elif raw.startswith("## "):
            flush(); out.append(f"<h2>{md_inline(raw[3:].strip())}</h2>")
        elif raw.startswith("### "):
            flush(); out.append(f"<h3>{md_inline(raw[4:].strip())}</h3>")
        elif raw.strip() in ("---", "***"):
            flush(); out.append("<hr/>")
        else:
            para.append(raw)
    flush()
    return "\n".join(out)


def read_doc(path: Path) -> tuple[dict, str, str]:
    text = path.read_text(encoding="utf-8")
    meta, body = parse_front_matter(text)
    return meta, body, md_to_html(body)


def strip_leading_h1(body_html: str) -> str:
    """章节正文开头的 # 标题已由页面单独渲染，去掉它避免重复 H1，
    并让首字下沉作用到真正的第一段。"""
    return re.sub(r"^\s*<h1>.*?</h1>\s*", "", body_html, count=1)


# ---------------------------------------------------------------------------
# 通用页面骨架
# ---------------------------------------------------------------------------
STYLE = (
    ":root{--fg:#1c1b19;--muted:#6b6762;--line:#e7e3dc;--accent:#8a3b2e;"
    "--paper:#fdfcf9;--ink-soft:#3a3733;--warn-bg:#fff6da;--warn-bd:#d9a441;"
    "--serif:Georgia,'Iowan Old Style','Times New Roman',serif}"
    "*{box-sizing:border-box}"
    "html{scroll-behavior:smooth}"
    "body{font-family:var(--serif);font-size:18px;line-height:1.8;color:var(--fg);"
    "background:var(--paper);margin:0}"
    ".wrap{max-width:680px;margin:0 auto;padding:0 24px}"
    "header.site{border-bottom:1px solid var(--line);margin-bottom:2.6rem}"
    "header.site .wrap{display:flex;justify-content:space-between;align-items:center;"
    "padding-top:1.1rem;padding-bottom:1.1rem}"
    "header.site a{color:var(--muted);text-decoration:none;font-family:system-ui,sans-serif;"
    "font-size:.82rem;letter-spacing:.04em}"
    "header.site a.brand{color:var(--fg);font-weight:700;font-size:.95rem;letter-spacing:.08em;"
    "text-transform:uppercase}"
    "h1,h2,h3{font-weight:600;line-height:1.25;color:#241f1a}"
    "h1{font-size:2.5rem;letter-spacing:-.01em;margin:.2rem 0 .6rem}"
    "h2{font-size:1.35rem;margin-top:2.6rem;margin-bottom:.8rem}"
    "h3{font-size:1.1rem;margin-top:1.8rem}"
    "p{margin:1.15rem 0}"
    "a{color:var(--accent)}"
    ".meta{color:var(--muted);font-family:system-ui,sans-serif;font-size:.8rem;"
    "letter-spacing:.03em}"
    ".eyebrow{font-family:system-ui,sans-serif;font-size:.72rem;letter-spacing:.16em;"
    "text-transform:uppercase;color:var(--accent);font-weight:700}"
    ".hero{padding:3rem 0 2.2rem;border-bottom:1px solid var(--line);margin-bottom:2.4rem}"
    ".hero h1{font-size:3rem;margin:.4rem 0}"
    ".hero .sub{font-size:1.25rem;font-style:italic;color:var(--ink-soft)}"
    ".hero .byline{margin-top:1.2rem}"
    ".chapters{list-style:none;padding:0;margin:1.4rem 0}"
    ".chapters li{border-bottom:1px solid var(--line);padding:1.3rem 0}"
    ".chapters li a{text-decoration:none;color:var(--fg)}"
    ".chapters li a:hover h3{color:var(--accent)}"
    ".chapters .num{font-family:system-ui,sans-serif;font-size:.75rem;letter-spacing:.12em;"
    "color:var(--accent);text-transform:uppercase}"
    ".chapters h3{font-size:1.4rem;margin:.3rem 0 .4rem}"
    ".chapters .summary{color:var(--ink-soft);font-style:italic;margin:.4rem 0 0}"
    ".chapters .readtime{font-family:system-ui,sans-serif;font-size:.72rem;color:var(--muted)}"
    ".chapter-nav{display:flex;justify-content:space-between;gap:1rem;margin:3.5rem 0 1rem;"
    "padding-top:1.5rem;border-top:1px solid var(--line);font-family:system-ui,sans-serif;"
    "font-size:.85rem}"
    ".chapter-nav a{text-decoration:none;color:var(--accent);max-width:45%}"
    ".chapter-nav .next{text-align:right}"
    ".chapter-nav .lbl{display:block;color:var(--muted);font-size:.7rem;"
    "letter-spacing:.1em;text-transform:uppercase}"
    ".chapter-body>p:first-of-type::first-letter{float:left;font-size:3.6em;line-height:.82;"
    "padding:.08em .12em 0 0;color:var(--accent)}"
    ".chapter-lead{font-style:italic;color:var(--ink-soft);font-size:1.12rem;"
    "border-left:3px solid var(--line);padding-left:1.1rem;margin:1.6rem 0 2.2rem}"
    ".glossary dt{font-weight:700;margin-top:1rem;color:#241f1a}"
    ".glossary dd{margin:.2rem 0 0;color:var(--ink-soft)}"
    ".banner{background:var(--warn-bg);border-left:4px solid var(--warn-bd);padding:12px 16px;"
    "border-radius:4px;margin:1.4rem 0;font-size:.88rem;font-family:system-ui,sans-serif}"
    ".disclosure{background:#f4f1eb;border:1px solid var(--line);padding:14px 18px;"
    "border-radius:6px;margin:2.6rem 0;font-size:.84rem;color:var(--ink-soft);"
    "font-family:system-ui,sans-serif;line-height:1.6}"
    "footer{margin-top:3.5rem;padding:1.6rem 0 3rem;border-top:1px solid var(--line);"
    "color:var(--muted);font-size:.8rem;font-family:system-ui,sans-serif}"
    "hr{border:0;border-top:1px solid var(--line);margin:2.4rem 0;"
    "max-width:120px;margin-left:auto;margin-right:auto}"
    ".progress{position:fixed;top:0;left:0;height:3px;background:var(--accent);width:0;z-index:9}"
    ".language-switch{display:flex;flex-wrap:wrap;gap:.5rem 1rem;padding:1rem 0;"
    "font-family:system-ui,sans-serif;font-size:.82rem;border-bottom:1px solid var(--line)}"
    ".language-switch a[aria-current=page]{color:var(--fg);font-weight:700}"
    "html:lang(ko) .chapter-body>p:first-of-type::first-letter,"
    "html:lang(yue) .chapter-body>p:first-of-type::first-letter{float:none;font-size:inherit;padding:0}"
    "html:lang(ko) body,html:lang(yue) body{word-break:normal;overflow-wrap:break-word}"
    "@media(max-width:600px){h1{font-size:2rem}.hero h1{font-size:2.2rem}"
    "body{font-size:17px}}"
)

def disclosure_banner(is_draft: bool, language: str = "en") -> str:
    if not is_draft:
        return ""
    t = LOCALES[language]
    return (f'<div class="banner"><strong>{html.escape(t["draft_title"])}</strong> '
            f'{html.escape(t["draft_notice"])}</div>')


def page(title: str, description: str, canonical_path: str, body: str,
         jsonld: dict | list[dict] | None = None, is_draft: bool = False,
         language: str = "en", alternates: dict | None = None,
         switches: dict | None = None) -> str:
    t = LOCALES[language]
    w = work(C.WORK, language)
    base = C.SITE["base_url"]
    canonical = base + canonical_path
    noindex = is_draft or C.PREVIEW_DRAFTS or bool(C.REVISION_SET)
    ld = ""
    if jsonld is not None and not noindex:
        obj = jsonld if isinstance(jsonld, list) else [jsonld]
        ld = '<script type="application/ld+json">' + json.dumps(
            obj, ensure_ascii=False).replace("<", "\\u003c") + "</script>"
    # Only indexable, independently approved translations enter SEO clusters.
    alternate_tags = []
    if not noindex and alternates:
        for lang, path in alternates.items():
            alternate_tags.append(f'<link rel="alternate" hreflang="{LOCALES[lang]["hreflang"]}" '
                                  f'href="{html.escape(base + path)}"/>')
        if "en" in alternates:
            alternate_tags.append(f'<link rel="alternate" hreflang="x-default" '
                                  f'href="{html.escape(base + alternates["en"])}"/>')
    switch_links = []
    available_languages = ("en",) if C.REVISION_SET else LOCALES
    for lang, path in (switches or {lang: route(lang) for lang in available_languages}).items():
        current = ' aria-current="page"' if lang == language else ''
        switch_links.append(f'<a href="{html.escape(path)}" lang="{LOCALES[lang]["lang"]}"'
                            f'{current}>{html.escape(LOCALES[lang]["label"])}</a>')
    disclosure_text = ("This is an AI-assisted revised draft inspired by narrative mechanisms in "
                       "classical Chinese fiction. It has not been human-reviewed. Earlier approvals "
                       "cover the earlier text only; existing translations do not represent this revision."
                       if C.REVISION_SET else t["disclosure"])
    revision_banner = ('<div class="banner"><strong>Classical-fiction fusion — revised draft.</strong> '
                       'Independent local preview. Not approved and not published. '
                       '<a href="/revision-notes/">创作来源、实质变化与审核要点</a></div>') if C.REVISION_SET else ""
    disclosure = (f'<div class="disclosure" data-ai-disclosure="true"><strong>'
                  f'{html.escape(t["disclosure_title"])}</strong> {html.escape(disclosure_text)} '
                  f'<a href="{route(language, "/about/")}">{html.escape(t["full_disclosure"])}</a>.</div>')
    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}"/>
<meta name="robots" content="{'noindex,follow' if noindex else 'index,follow'}"/>
<link rel="canonical" href="{html.escape(canonical)}"/>
{chr(10).join(alternate_tags)}
{ld}
<style>{STYLE}</style>
</head>
<body>
<div class="progress" id="progress"></div>
<header class="site"><div class="wrap">
  <a class="brand" href="{route(language)}">{html.escape(C.SITE['name'])}</a>
  <nav><a href="{route(language, '/about/')}">{html.escape(t['about'])}</a></nav>
</div></header>
<div class="wrap">
<nav class="language-switch" aria-label="{html.escape(t['languages'])}">{' '.join(switch_links)}</nav>
{revision_banner}
{disclosure_banner(is_draft, language)}
{body}
{disclosure}
<footer>&copy; {html.escape(w['author'])} · {html.escape(w['title'])}. {html.escape(t['fiction'])}</footer>
</div>
<script>
window.addEventListener('scroll',function(){{
  var h=document.documentElement;
  var max=(h.scrollHeight-h.clientHeight);
  var p=max>0?(h.scrollTop/max)*100:0;
  document.getElementById('progress').style.width=p+'%';
}});
</script>
</body>
</html>"""


# ---------------------------------------------------------------------------
# 加载章节，执行人工关口
# ---------------------------------------------------------------------------
def source_digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def translation_approved(meta: dict, source_meta: dict, source_hash: str) -> bool:
    # Original approval is NOT translation approval. Bind review to this source version.
    return bool(meta.get("status") == "approved"
                and source_meta.get("status") == "approved"
                and meta.get("source_sha256") == source_hash
                and meta.get("reviewer", "").strip()
                and re.fullmatch(r"\d{4}-\d{2}-\d{2}", meta.get("review_date", ""))
                and len(meta.get("review_notes", "").strip()) >= 12)


def load_chapters(language: str = "en") -> list[dict]:
    revision = revision_root()
    if revision and language != "en":
        return []  # Never reuse previously approved translations for changed prose.
    directory = (revision / "chapters" if revision else CHAPTERS_DIR) if language == "en" else CONTENT / "translations" / language
    chapters = []
    seen = set()
    for p in sorted(directory.glob("*.md")):
        meta, raw, body_html = read_doc(p)
        body_html = strip_leading_h1(body_html)
        slug = meta.get("slug") or re.sub(r"^\d+-", "", p.stem)
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug) or slug in seen:
            raise ValueError(f"Invalid or duplicate chapter slug: {p}")
        seen.add(slug)
        num = meta.get("chapter", "?")
        status = meta.get("status", "draft")
        approved = status == "approved" and not revision
        if language != "en":
            if meta.get("language") != language:
                raise ValueError(f"Translation language does not match directory: {p}")
            source = CHAPTERS_DIR / p.name
            if not source.exists():
                raise ValueError(f"Translation has no English source: {p}")
            source_meta, _, _ = read_doc(source)
            source_slug = source_meta.get("slug") or re.sub(r"^\d+-", "", source.stem)
            if source_slug != slug or source_meta.get("chapter") != num:
                raise ValueError(f"Translation does not match its source chapter: {p}")
            approved = translation_approved(meta, source_meta, source_digest(source))
        text = re.sub(r"^#.*$", "", raw, flags=re.M)
        units = len(re.findall(r"[\u3400-\u9fff]", text)) if language == "yue" else len(text.split())
        readtime = max(1, round(units / (350 if language == "yue" else 220)))
        chapters.append({
            "num": num, "slug": slug, "title": meta.get("title", p.stem),
            "summary": meta.get("summary", ""), "status": status, "approved": approved,
            "words": units, "readtime": readtime, "html": body_html, "path": p,
            "language": language,
        })
    chapters.sort(key=lambda c: int(c["num"]) if str(c["num"]).isdigit() else 999)
    return chapters


# ---------------------------------------------------------------------------
# 各页面
# ---------------------------------------------------------------------------
def book_schema(language: str = "en") -> dict:
    w = work(C.WORK, language)
    schema: dict = {
        "@context": "https://schema.org",
        "@type": "Book",
        "name": w["title"],
        "description": w["description"],
        "inLanguage": w["language"],
        "genre": w["genre"],
        "author": {"@type": "Organization", "name": w["author"]},
    }
    if w.get("isbn"):
        schema["isbn"] = w["isbn"]
    if language == "en" and w.get("date_published"):
        schema["datePublished"] = w["date_published"]
    return schema


def write_page(out: Path, path: str, document: str):
    dest = out / path.strip("/") / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(document, encoding="utf-8")


def chapter_path(c: dict) -> str:
    return route(c["language"], f'/chapters/{c["slug"]}/')


def page_alternates(collection: dict, suffix: str = "/") -> dict:
    result = {}
    for language, chapters in collection.items():
        if suffix in ("/", "/about/"):
            available = any(c["approved"] for c in chapters)
        else:
            available = any(c["approved"] and f'/chapters/{c["slug"]}/' == suffix for c in chapters)
        if available:
            result[language] = route(language, suffix)
    return result


def chapter_switches(collection: dict, slug: str) -> dict:
    return {language: (route(language, f"/chapters/{slug}/")
                       if any(c["slug"] == slug and (c["approved"] or C.PREVIEW_DRAFTS)
                              for c in chapters) else route(language))
            for language, chapters in collection.items()}


def render_home(chapters: list[dict], out: Path, language: str = "en", collection: dict | None = None):
    t = LOCALES[language]
    w = work(C.WORK, language)
    collection = collection or {language: chapters}
    visible = [c for c in chapters if c["approved"] or C.PREVIEW_DRAFTS]
    approved = any(c["approved"] for c in chapters)
    lis = []
    for c in visible:
        draft_tag = f' <span class="meta">· {html.escape(t["draft_tag"])}</span>' if not c["approved"] else ""
        summary = f'<p class="summary">{html.escape(c["summary"])}</p>' if c["summary"] else ""
        lis.append(f'<li><a href="{chapter_path(c)}">'
                   f'<span class="num">{html.escape(t["chapter"].format(n=c["num"]))}</span>'
                   f'<h3>{html.escape(c["title"])}{draft_tag}</h3>{summary}'
                   f'<span class="readtime">{html.escape(t["readtime"].format(n=c["readtime"]))}</span></a></li>')
    toc = "\n".join(lis) or f'<li class="meta">{html.escape(t["no_chapters"])}</li>'
    pending = (f'<p class="banner">{html.escape(t["pending"])} '
               f'<a href="/">{html.escape(t["read_english"])}</a></p>') if language != "en" and not approved else ""
    body = f"""<section class="hero">
<span class="eyebrow">{html.escape(t['short_story'])} · {html.escape(w['genre'])}</span>
<h1>{html.escape(w['title'])}</h1><p class="sub">{html.escape(w['subtitle'])}</p>
<p class="byline meta">{html.escape(t['by'].format(author=w['author']))} · {html.escape(t['stats'].format(n=len(visible)))}</p>
</section><p>{html.escape(w['description'])}</p>{pending}<hr/>
<h2>{html.escape(t['chapters'])}</h2><ul class="chapters">{toc}</ul>
<p class="meta"><a href="{route(language, '/about/')}">{html.escape(t['about_hint'])}</a></p>"""
    write_page(out, route(language), page(f"{w['title']} — {C.SITE['name']}", w["description"],
               route(language), body, book_schema(language), is_draft=not approved,
               language=language, alternates=page_alternates(collection)))


GLOSSARY = [
    ("Engram", "A portable, editable recording of a single memory. Lossy by design — what it keeps is not always what mattered."),
    ("The Loom", "The table-sized apparatus that renders an engram as a structure a repairman can work inside."),
    ("Fill", "Synthetic connective tissue keyed into a damaged engram. Plausible, stable, and emotionally inert."),
    ("The Grey", "The calm, documentary flatness left by heavy repair. Facts intact; feeling gone."),
    ("Memory architect", "One of the engineers who designed the first commercial looms — and understood exactly what the fill would do."),
]


def render_about(out: Path, language: str = "en", collection: dict | None = None):
    t = LOCALES[language]
    w = work(C.WORK, language)
    collection = collection or {language: load_chapters(language)}
    approved = any(c["approved"] for c in collection[language])
    disclosure = (strip_leading_h1(read_doc(EDITORIAL_DIR / "ai-disclosure.md")[2])
                  if language == "en" else f'<p>{html.escape(t["disclosure"])}</p>')
    bible_html = (strip_leading_h1(read_doc(CONTENT / "world-bible.md")[2])
                  if language == "en" else f'<p>{html.escape(t["world"])}</p>')
    if C.REVISION_SET:
        notes = revision_notes()
        bible_html = f'<p>{html.escape(notes["world_en"])}</p>'
        disclosure = ('<p>This revised text was drafted with AI assistance and is awaiting new human '
                      'editorial review. Earlier approvals do not cover this version.</p>')
    glossary = GLOSSARY if language == "en" else t["terms"]
    terms = "\n".join(f"<dt>{html.escape(term)}</dt><dd>{html.escape(desc)}</dd>" for term, desc in glossary)
    contact = (f'<p class="meta">{html.escape(t["contact"])}: '
               f'<a href="mailto:{html.escape(C.SITE["contact"])}">{html.escape(C.SITE["contact"])}</a></p>'
               if C.SITE["contact"] else "")
    body = f"""<section class="hero"><span class="eyebrow">{html.escape(t['about'])}</span>
<h1>{html.escape(t['behind'])}</h1><p class="sub">{html.escape(w['title'])} · {html.escape(w['genre'])}</p></section>
<p>{html.escape(w['description'])}</p><h2>{html.escape(t['idea'])}</h2>{bible_html}
<h2>{html.escape(t['glossary'])}</h2><p>{html.escape(t['terms_hint'])}</p><dl class="glossary">{terms}</dl>
<h2>{html.escape(t['authorship'])}</h2>{disclosure}
<p>{html.escape(t['byline_notice'].format(author=w['author']))}</p>{contact}"""
    write_page(out, route(language, "/about/"), page(f"{t['about']} — {w['title']}", w["description"],
               route(language, "/about/"), body, book_schema(language), is_draft=not approved,
               language=language, alternates=page_alternates(collection, "/about/"),
               switches={lang: route(lang, "/about/") for lang in collection}))


def render_chapter(c: dict, chapters: list[dict], out: Path, collection: dict | None = None):
    language = c["language"]
    t = LOCALES[language]
    w = work(C.WORK, language)
    collection = collection or {language: chapters}
    schema = {"@context": "https://schema.org", "@type": "Chapter", "name": c["title"],
              "isPartOf": {"@type": "Book", "name": w["title"],
                           "author": {"@type": "Organization", "name": w["author"]}},
              "inLanguage": w["language"]}
    visible = [x for x in chapters if x["approved"] or C.PREVIEW_DRAFTS]
    idx = next(i for i, x in enumerate(visible) if x["slug"] == c["slug"])
    nav = []
    for i, css, label in ((idx - 1, "prev", "previous"), (idx + 1, "next", "next")):
        if 0 <= i < len(visible):
            neighbor = visible[i]
            nav.append(f'<a class="{css}" href="{chapter_path(neighbor)}">'
                       f'<span class="lbl">{html.escape(t[label])}</span>{html.escape(neighbor["title"])}</a>')
    nav_html = '<nav class="chapter-nav">' + "".join(nav) + "</nav>" if nav else ""
    lead = f'<p class="chapter-lead">{html.escape(c["summary"])}</p>' if c["summary"] else ""
    body = (f'<span class="eyebrow">{html.escape(t["chapter"].format(n=c["num"]))}</span>'
            f'<h1>{html.escape(c["title"])}</h1><p class="byline meta">{html.escape(w["title"])} · '
            f'{html.escape(t["by"].format(author=w["author"]))} · '
            f'{html.escape(t["readtime"].format(n=c["readtime"]))}</p>{lead}'
            f'<div class="chapter-body">{c["html"]}</div>{nav_html}')
    write_page(out, chapter_path(c), page(f'{c["title"]} — {w["title"]}', c["summary"] or w["description"],
               chapter_path(c), body, schema, is_draft=not c["approved"], language=language,
               alternates=page_alternates(collection, f'/chapters/{c["slug"]}/'),
               switches=chapter_switches(collection, c["slug"])))


def write_sitemap(paths: list[str], out: Path):
    base = C.SITE["base_url"]
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in paths:
        lines.append(f"  <url><loc>{html.escape(base + p)}</loc></url>")
    lines.append("</urlset>")
    (out / "sitemap.xml").write_text("\n".join(lines), encoding="utf-8")


def write_robots(out: Path):
    (out / "robots.txt").write_text(
        "User-agent: *\nAllow: /\nSitemap: " + C.SITE["base_url"] + "/sitemap.xml\n",
        encoding="utf-8")


def render_revision_notes(out: Path):
    notes = revision_notes()
    blocks = [f'<section class="hero"><span class="eyebrow">修订工作台 · 未审核草稿</span>'
              f'<h1>{html.escape(notes["title"])}</h1></section>']
    for label, key in (("审核状态", "human_review"), ("创作目标", "purpose"),
                       ("合规边界", "policy_note"), ("引用边界", "copyright_boundary")):
        blocks.append(f'<h2>{label}</h2><p>{html.escape(notes[key])}</p>')
    blocks.append('<h2>古典叙事提炼与融合</h2>')
    for source in notes["sources"]:
        blocks.append(f'<h3>{html.escape(source["work"])}</h3>'
                      f'<p>{html.escape(source["mechanism"])}</p><p>{html.escape(source["transformation"])}</p>'
                      f'<p class="meta">{html.escape(source["source_type"])} '
                      f'<a href="{html.escape(source["reference_url"])}" target="_blank" rel="noopener noreferrer">参考来源</a></p>')
    blocks.append('<h2>逐章实质变化</h2>')
    for chapter in notes["chapter_changes"]:
        blocks.append(f'<h3>第{chapter["chapter"]}章</h3><p>{html.escape(chapter["changes"])}</p>')
    blocks.append('<h2>连续性与人工终审要点</h2><ul>')
    blocks.extend(f'<li>{html.escape(item)}</li>' for item in notes["continuity_and_review"])
    blocks.append('</ul><p><a href="/">阅读融合版英文草稿</a></p>')
    document = page(notes["title"], notes["purpose"], "/revision-notes/", "".join(blocks), is_draft=True)
    document = document.replace('<html lang="en">', '<html lang="zh-Hans">', 1)
    write_page(out, "/revision-notes/", document)


def main():
    revision = revision_root()  # Validate before creating or writing any build files.
    out = ROOT / C.OUTPUT_DIR
    if C.PREVIEW_DRAFTS and out.resolve() == (ROOT / "site").resolve():
        raise ValueError("Draft preview must not overwrite the production site directory")
    if revision and out.resolve() == (ROOT / "preview-site").resolve():
        raise ValueError("Revision preview must use its own output directory")
    out.mkdir(parents=True, exist_ok=True)
    languages = ("en",) if revision else LOCALES
    collection = {language: load_chapters(language) for language in languages}
    paths = []
    for language, chapters in collection.items():
        visible = [c for c in chapters if c["approved"] or C.PREVIEW_DRAFTS]
        approved = [c for c in chapters if c["approved"]]
        print(f"[i] {language}: {len(chapters)} chapters, {len(approved)} approved")
        render_home(chapters, out, language, collection)
        render_about(out, language, collection)
        for c in visible:
            render_chapter(c, chapters, out, collection)
        for c in chapters:
            if c in visible:
                continue
            t = LOCALES[language]
            body = (f'<h1>{html.escape(t["unpublished"])}</h1>'
                    f'<p>{html.escape(t["unpublished_description"])} '
                    f'<a href="{route(language)}">{html.escape(t["toc"])}</a></p>')
            write_page(out, chapter_path(c), page(t["unpublished"], t["unpublished_description"],
                       chapter_path(c), body, is_draft=True, language=language,
                       switches=chapter_switches(collection, c["slug"])))
        if approved and not C.PREVIEW_DRAFTS:
            paths.extend([route(language), route(language, "/about/")])
            paths.extend(chapter_path(c) for c in approved)
    if revision:
        render_revision_notes(out)
    write_sitemap(paths, out)
    write_robots(out)
    print(f"[done] {len(paths)} indexable URLs -> {out}/")


if __name__ == "__main__":
    main()
