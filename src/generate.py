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

import html
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
import config as C

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
CHAPTERS_DIR = CONTENT / "chapters"
EDITORIAL_DIR = CONTENT / "editorial"


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
                    meta[k.strip()] = v.strip().strip('"').strip("'")
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
    "@media(max-width:600px){h1{font-size:2rem}.hero h1{font-size:2.2rem}"
    "body{font-size:17px}}"
)

DISCLOSURE = (
    "<div class=\"disclosure\"><strong>How this story was made.</strong> "
    "Drafted with the assistance of an AI language model, then reviewed and edited by a human "
    "editor before publication. No fabricated author biography or portrait is used. "
    "<a href=\"/about/\">Full disclosure</a>.</div>"
)


def disclosure_banner(is_draft: bool) -> str:
    if not is_draft:
        return ""
    return (
        "<div class=\"banner\"><strong>Editor's note — preview draft.</strong> "
        "This chapter is an AI-assisted draft awaiting human editorial review. "
        "It is shown for preview only and is not a finished, approved text.</div>"
    )


def page(title: str, description: str, canonical_path: str, body: str,
         jsonld: dict | list[dict] | None = None, is_draft: bool = False) -> str:
    base = C.SITE["base_url"]
    canonical = base + canonical_path
    ld = ""
    if jsonld is not None:
        obj = jsonld if isinstance(jsonld, list) else [jsonld]
        ld = '<script type="application/ld+json">' + json.dumps(
            obj, ensure_ascii=False) + "</script>"
    site_name = html.escape(C.SITE["name"])
    return f"""<!doctype html>
<html lang="{html.escape(C.SITE['lang'])}">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}"/>
<meta name="robots" content="{"noindex,follow" if is_draft else "index,follow"}"/>
<link rel="canonical" href="{html.escape(canonical)}"/>
<link rel="alternate" hreflang="x-default" href="{html.escape(canonical)}"/>
{ld}
<style>{STYLE}</style>
</head>
<body>
<div class="progress" id="progress"></div>
<header class="site"><div class="wrap">
  <a class="brand" href="/">{site_name}</a>
  <nav><a href="/about/">About</a></nav>
</div></header>
<div class="wrap">
{disclosure_banner(is_draft)}
{body}
{DISCLOSURE}
<footer>
&copy; {html.escape(C.WORK['author'])} · {html.escape(C.WORK['title'])}.
A work of fiction. Any resemblance to persons or events is coincidental.
</footer>
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
def load_chapters() -> list[dict]:
    chapters = []
    for p in sorted(CHAPTERS_DIR.glob("*.md")):
        meta, raw, body_html = read_doc(p)
        body_html = strip_leading_h1(body_html)
        slug = meta.get("slug") or re.sub(r"^\d+-", "", p.stem)
        num = meta.get("chapter", "?")
        status = meta.get("status", "draft")
        approved = status == "approved"
        words_raw = meta.get("words", "")
        try:
            wcount = int(words_raw)
            readtime = max(1, round(wcount / 220))
        except (ValueError, TypeError):
            wcount = 0
            readtime = 0
        chapters.append({
            "num": num,
            "slug": slug,
            "title": meta.get("title", p.stem),
            "summary": meta.get("summary", ""),
            "status": status,
            "approved": approved,
            "words": wcount,
            "readtime": readtime,
            "html": body_html,
            "path": p,
        })
    chapters.sort(key=lambda c: int(c["num"]) if str(c["num"]).isdigit() else 999)
    return chapters


# ---------------------------------------------------------------------------
# 各页面
# ---------------------------------------------------------------------------
def book_schema() -> dict:
    w = C.WORK
    schema: dict = {
        "@context": "https://schema.org",
        "@type": "Book",
        "name": w["title"],
        "description": w["description"],
        "inLanguage": w["language"],
        "genre": w["genre"],
        "author": {"@type": "Person", "name": w["author"]},
    }
    if w.get("isbn"):
        schema["isbn"] = w["isbn"]
    if w.get("date_published"):
        schema["datePublished"] = w["date_published"]
    return schema


def render_home(chapters: list[dict], out: Path):
    w = C.WORK
    visible = [c for c in chapters if c["approved"] or C.PREVIEW_DRAFTS]
    lis = []
    for c in visible:
        draft_tag = ' <span class="meta">· preview draft</span>' if not c["approved"] else ""
        rt = f'{c["readtime"]} min read' if c["readtime"] else ''
        summary = (f'<p class="summary">{html.escape(c["summary"])}</p>'
                   if c["summary"] else "")
        lis.append(
            f'<li><a href="/chapters/{html.escape(c["slug"])}/">'
            f'<span class="num">Chapter {html.escape(str(c["num"]))}</span>'
            f'<h3>{html.escape(c["title"])}{draft_tag}</h3>'
            f'{summary}<span class="readtime">{rt}</span>'
            f'</a></li>')
    toc = "\n".join(lis) or (
        '<li class="meta">No chapters are published yet. Chapters appear here after '
        'human editorial review.</li>')
    total_words = sum(c["words"] for c in visible)
    stat = (f'{len(visible)} chapters · ~{total_words:,} words' if visible
            else 'A story in three parts')
    body = f"""<section class="hero">
  <span class="eyebrow">A short story · {html.escape(w['genre'])}</span>
  <h1>{html.escape(w['title'])}</h1>
  <p class="sub">{html.escape(w['subtitle'])}</p>
  <p class="byline meta">By {html.escape(w['author'])} · {stat}</p>
</section>
<p>{html.escape(w['description'])}</p>
<hr/>
<h2>Chapters</h2>
<ul class="chapters">{toc}</ul>
<p class="meta">Read the <a href="/about/">about page</a> for the world, the author, and how this story was made.</p>"""
    (out / "index.html").write_text(
        page(f"{w['title']} — {C.SITE['name']}", w["description"], "/", body, book_schema()),
        encoding="utf-8")


GLOSSARY = [
    ("Engram", "A portable, editable recording of a single memory. Lossy by design — what it keeps is not always what mattered."),
    ("The Loom", "The table-sized apparatus that renders an engram as a structure a repairman can work inside."),
    ("Fill", "Synthetic connective tissue keyed into a damaged engram. Plausible, stable, and emotionally inert."),
    ("The Grey", "The calm, documentary flatness left by heavy repair. Facts intact; feeling gone."),
    ("Memory architect", "One of the engineers who designed the first commercial looms — and understood exactly what the fill would do."),
]


def render_about(out: Path):
    disclosure = strip_leading_h1(read_doc(EDITORIAL_DIR / "ai-disclosure.md")[2])
    bible_html = strip_leading_h1(read_doc(CONTENT / "world-bible.md")[2])
    # 从世界观文档里取 premise，作为开头精选段（避免整篇 bible 全文铺陈）
    terms = "\n".join(
        f"<dt>{html.escape(t)}</dt><dd>{html.escape(d)}</dd>" for t, d in GLOSSARY)
    contact = (f'<p class="meta">Contact: <a href="mailto:{html.escape(C.SITE["contact"])}">'
               f'{html.escape(C.SITE["contact"])}</a></p>' if C.SITE["contact"] else "")
    body = f"""<section class="hero">
  <span class="eyebrow">About</span>
  <h1>Behind the story</h1>
  <p class="sub">{html.escape(C.WORK['title'])} · {html.escape(C.WORK['genre'])}</p>
</section>
<p>{html.escape(C.WORK['description'])}</p>
<h2>The idea</h2>
{bible_html}
<h2>A small glossary</h2>
<p>Terms the story uses, without spoilers.</p>
<dl class="glossary">{terms}</dl>
<h2>Authorship &amp; AI disclosure</h2>
{disclosure}
<p>This work is published under the byline <strong>{html.escape(C.WORK['author'])}</strong>,
the human editor responsible for the final text. There is no fabricated author portrait or biography.</p>
{contact}"""
    (out / "about" / "index.html").parent.mkdir(parents=True, exist_ok=True)
    (out / "about" / "index.html").write_text(
        page(f"About — {C.WORK['title']}", C.WORK["description"], "/about/", body, book_schema()),
        encoding="utf-8")


def render_chapter(c: dict, chapters: list[dict], out: Path):
    is_draft = not c["approved"]
    schema: dict = {
        "@context": "https://schema.org",
        "@type": "Chapter",
        "name": c["title"],
        "isPartOf": {"@type": "Book", "name": C.WORK["title"],
                     "author": {"@type": "Person", "name": C.WORK["author"]}},
        "inLanguage": C.WORK["language"],
    }
    path = f"/chapters/{c['slug']}/"
    # 只在已发布集合中计算相邻章节
    visible = [x for x in chapters if x["approved"] or C.PREVIEW_DRAFTS]
    idx = next((i for i, x in enumerate(visible) if x["slug"] == c["slug"]), -1)
    nav = []
    if idx > 0:
        prev = visible[idx - 1]
        nav.append(
            f'<a class="prev" href="/chapters/{html.escape(prev["slug"])}/">'
            f'<span class="lbl">← Previous</span>{html.escape(prev["title"])}</a>')
    if idx >= 0 and idx < len(visible) - 1:
        nxt = visible[idx + 1]
        nav.append(
            f'<a class="next" href="/chapters/{html.escape(nxt["slug"])}/">'
            f'<span class="lbl">Next →</span>{html.escape(nxt["title"])}</a>')
    nav_html = ('<nav class="chapter-nav">' + "".join(nav) + "</nav>") if nav else ""
    lead = (f'<p class="chapter-lead">{html.escape(c["summary"])}</p>'
            if c["summary"] else "")
    rt = f'{c["readtime"]} min read' if c["readtime"] else ""
    body = (f'<span class="eyebrow">Chapter {html.escape(str(c["num"]))}</span>'
            f'<h1>{html.escape(c["title"])}</h1>'
            f'<p class="byline meta">{html.escape(C.WORK["title"])} · '
            f'by {html.escape(C.WORK["author"])}'
            + (f' · {rt}' if rt else '') + '</p>'
            + lead
            + f'<div class="chapter-body">{c["html"]}</div>'
            + nav_html)
    dest = out / "chapters" / c["slug"] / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(
        page(f'{c["title"]} — {C.WORK["title"]}', C.WORK["description"],
             path, body, schema, is_draft=is_draft),
        encoding="utf-8")


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


def main():
    out = ROOT / "site"
    out.mkdir(parents=True, exist_ok=True)
    chapters = load_chapters()
    published = [c for c in chapters if c["approved"] or C.PREVIEW_DRAFTS]
    print(f"[i] chapters found: {len(chapters)}, published: {len(published)} "
          f"(PREVIEW_DRAFTS={C.PREVIEW_DRAFTS})")

    render_home(chapters, out)
    render_about(out)
    for c in published:
        render_chapter(c, chapters, out)

    # 草稿墓碑：为未发布的草稿输出 noindex 占位页，覆盖旧部署可能残留的
    # 已发布版本（Cloudflare Pages 增量部署不删除历史文件）。
    # 这样任何曾误发布的草稿，其公开路径都会变成 noindex，不会被收录。
    published_slugs = {c["slug"] for c in published}
    for c in chapters:
        if c["slug"] in published_slugs:
            continue
        tombstone_body = (
            '<h1>Not published</h1>'
            '<p>This chapter is not part of the published work. '
            'Please return to the <a href="/">table of contents</a>.</p>'
        )
        dest = out / "chapters" / c["slug"] / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(
            page("Not published", "This chapter is not published.",
                 f"/chapters/{c['slug']}/", tombstone_body, None, is_draft=True),
            encoding="utf-8")

    # sitemap 只包含正式发布的页面，不含草稿墓碑
    paths = ["/", "/about/"] + [f"/chapters/{c['slug']}/" for c in published]
    write_sitemap(paths, out)
    write_robots(out)
    print(f"[done] {len(paths)} URLs -> {out}/")

    if not published and not C.PREVIEW_DRAFTS:
        print("[!] No approved chapters. Set PREVIEW_DRAFTS=1 to preview drafts, "
              "or mark chapters status: approved in front matter after human review.",
              file=sys.stderr)


if __name__ == "__main__":
    main()
