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


# ---------------------------------------------------------------------------
# 通用页面骨架
# ---------------------------------------------------------------------------
STYLE = (
    ":root{--fg:#1a1a1a;--muted:#5f6368;--line:#e6e6e6;--accent:#334155;--warn-bg:#fff8e1;--warn-bd:#f0c000}"
    "*{box-sizing:border-box}"
    "body{font:17px/1.75 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Georgia,serif;"
    "color:var(--fg);max-width:720px;margin:0 auto;padding:32px 24px;background:#fff}"
    "header.site{border-bottom:1px solid var(--line);margin-bottom:2rem;padding-bottom:1rem;"
    "font-size:.85rem;color:var(--muted)} header.site a{color:inherit;text-decoration:none}"
    "h1{font-size:2.1rem;line-height:1.2}h2{font-size:1.35rem;margin-top:2.2rem;"
    "border-bottom:1px solid var(--line);padding-bottom:.3rem}h3{font-size:1.1rem}"
    "p{margin:1rem 0}a{color:var(--accent)}"
    ".meta{color:var(--muted);font-size:.88rem}"
    ".toc{list-style:none;padding:0}.toc li{padding:.6rem 0;border-bottom:1px solid var(--line)}"
    ".toc a{text-decoration:none;font-size:1.05rem}.toc .n{color:var(--muted);margin-right:.6rem}"
    ".banner{background:var(--warn-bg);border-left:4px solid var(--warn-bd);padding:12px 16px;"
    "border-radius:4px;margin:1.2rem 0;font-size:.9rem}"
    ".disclosure{background:#f6f7f9;border:1px solid var(--line);padding:14px 18px;"
    "border-radius:6px;margin:2rem 0;font-size:.86rem;color:#444}"
    "footer{margin-top:3rem;padding-top:1rem;border-top:1px solid var(--line);"
    "color:var(--muted);font-size:.82rem}"
    "hr{border:0;border-top:1px solid var(--line);margin:2rem 0}"
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
<header class="site"><a href="/">{site_name}</a></header>
{disclosure_banner(is_draft)}
{body}
{DISCLOSURE}
<footer>
&copy; {html.escape(C.WORK['author'])} · {html.escape(C.WORK['title'])}.
A work of fiction. Any resemblance to persons or events is coincidental.
</footer>
</body>
</html>"""


# ---------------------------------------------------------------------------
# 加载章节，执行人工关口
# ---------------------------------------------------------------------------
def load_chapters() -> list[dict]:
    chapters = []
    for p in sorted(CHAPTERS_DIR.glob("*.md")):
        meta, raw, body_html = read_doc(p)
        slug = meta.get("slug") or re.sub(r"^\d+-", "", p.stem)
        num = meta.get("chapter", "?")
        status = meta.get("status", "draft")
        approved = status == "approved"
        chapters.append({
            "num": num,
            "slug": slug,
            "title": meta.get("title", p.stem),
            "status": status,
            "approved": approved,
            "words": meta.get("words", ""),
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
    lis = []
    for c in chapters:
        if not c["approved"] and not C.PREVIEW_DRAFTS:
            continue
        draft_tag = " <span class=\"meta\">(preview draft)</span>" if not c["approved"] else ""
        lis.append(
            f'<li><span class="n">{html.escape(str(c["num"]))}.</span>'
            f'<a href="/chapters/{html.escape(c["slug"])}/">{html.escape(c["title"])}</a>'
            f'{draft_tag}</li>')
    toc = "\n".join(lis) or "<li class=\"meta\">No chapters published yet.</li>"
    body = f"""<h1>{html.escape(w['title'])}</h1>
<p class="meta">A short story in three parts · {html.escape(w['genre'])} · by {html.escape(w['author'])}</p>
<p>{html.escape(w['subtitle'])}</p>
<h2>Chapters</h2>
<ul class="toc">{toc}</ul>
<p><a href="/about/">About the story &amp; how it was made →</a></p>"""
    (out / "index.html").write_text(
        page(f"{w['title']} — {C.SITE['name']}", w["description"], "/", body, book_schema()),
        encoding="utf-8")


def render_about(out: Path):
    disclosure = read_doc(EDITORIAL_DIR / "ai-disclosure.md")[2]
    bible_meta, _, bible_html = read_doc(CONTENT / "world-bible.md")
    contact = (f'<p>Contact: <a href="mailto:{html.escape(C.SITE["contact"])}">'
               f'{html.escape(C.SITE["contact"])}</a></p>' if C.SITE["contact"] else "")
    body = f"""<h1>About the story</h1>
<p class="meta">{html.escape(C.WORK['title'])} · {html.escape(C.WORK['genre'])}</p>
<p>{html.escape(C.WORK['description'])}</p>
<h2>Background</h2>
{bible_html}
<h2>Authorship &amp; AI disclosure</h2>
{disclosure}
<p>This work is published under the byline <strong>{html.escape(C.WORK['author'])}</strong>,
the human editor responsible for the final text. There is no fabricated author portrait or biography.</p>
{contact}"""
    (out / "about" / "index.html").parent.mkdir(parents=True, exist_ok=True)
    (out / "about" / "index.html").write_text(
        page(f"About — {C.WORK['title']}", C.WORK["description"], "/about/", body, book_schema()),
        encoding="utf-8")


def render_chapter(c: dict, out: Path):
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
    body = (f'<h1>{html.escape(c["title"])}</h1>'
            f'<p class="meta">Chapter {html.escape(str(c["num"]))} · '
            f'{html.escape(C.WORK["title"])} · by {html.escape(C.WORK["author"])}</p>'
            f'{c["html"]}')
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
        render_chapter(c, out)

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
