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
from datetime import datetime, timezone
from email.utils import format_datetime
import html
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
import config as C
import evergreen as EV
from locales import LOCALES, EXTRA, route, work
import glossary as GX
import extras as XT
import acts as AX
import bookcopy as BC

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
    ".evergreen-nav{flex-wrap:wrap;justify-content:flex-start;gap:.5rem 1rem}"
    ".evergreen-nav a{max-width:none}"
    ".evergreen-nav a[aria-current=page]{font-weight:700;color:var(--fg)}"
    # Explore menu
    ".explore{position:relative}"
    ".explore-btn{background:none;border:0;color:var(--muted);font-family:system-ui,sans-serif;"
    "font-size:.82rem;letter-spacing:.04em;cursor:pointer;padding:0}"
    ".explore-list{display:none;position:absolute;right:0;top:1.6rem;z-index:10;"
    "background:var(--paper);border:1px solid var(--line);border-radius:6px;"
    "box-shadow:0 6px 22px rgba(0,0,0,.08);padding:.5rem 0;min-width:150px}"
    ".explore-list a{display:block;padding:.4rem 1rem;white-space:nowrap}"
    ".explore:hover .explore-list,.explore:focus-within .explore-list,.explore.open .explore-list{display:block}"
    # Home: parts, CTA, progress, explore box
    ".part-title{font-family:system-ui,sans-serif;font-size:.78rem;letter-spacing:.14em;"
    "text-transform:uppercase;color:var(--accent);margin:2.4rem 0 .4rem;padding-bottom:.5rem;"
    "border-bottom:1px solid var(--line)}"
    ".cta{margin:1.6rem 0 .4rem}"
    ".btn{display:inline-block;background:var(--accent);color:#fff;text-decoration:none;"
    "font-family:system-ui,sans-serif;font-size:.9rem;padding:.6rem 1.1rem;border-radius:5px}"
    ".resume{margin:.8rem 0 0;font-family:system-ui,sans-serif;font-size:.86rem}"
    ".resume a{font-weight:700}"
    ".progress-card{background:#f4f1eb;border:1px solid var(--line);border-radius:6px;"
    "padding:12px 16px;margin:1.4rem 0;font-family:system-ui,sans-serif;font-size:.86rem}"
    ".progress-card small{display:block;color:var(--muted);margin-top:.5rem;font-size:.74rem}"
    ".link-btn{background:none;border:0;color:var(--accent);cursor:pointer;font-size:.8rem;"
    "text-decoration:underline;padding:0 0 0 .4rem}"
    ".explore-box{margin-top:3rem;padding-top:1.5rem;border-top:1px solid var(--line)}"
    ".part-title a{color:inherit;text-decoration:none}.part-title a:hover{color:var(--accent)}"
    ".glossary-list{list-style:none;padding:0;margin:2rem 0}"
    ".glossary-list li{margin:0 0 1rem}"
    ".glossary-list a{display:block;text-decoration:none;color:var(--fg);border-bottom:1px solid var(--line);padding-bottom:.8rem}"
    ".glossary-list strong{display:block;font-size:1.1rem;margin-bottom:.25rem}"
    ".glossary-list span{color:var(--muted);font-size:.92rem}"
    ".glossary-list a:hover strong{color:var(--accent)}"
    ".acts-chapters{list-style:none;padding:0;margin:2.5rem 0}"
    ".acts-chapters li{margin-bottom:1.2rem}"
    ".acts-chapters a{display:block;text-decoration:none;color:var(--fg)}"
    ".acts-chapters .num{font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}"
    ".acts-chapters h3{margin:.2rem 0 .3rem;font-size:1.05rem}"
    ".acts-chapters p{margin:0;color:var(--muted);font-size:.92rem}"
    ".subscribe{display:flex;flex-wrap:wrap;gap:.5rem;align-items:center;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--line);font-size:.9rem}"
    ".subscribe label{color:var(--muted);width:100%}"
    ".subscribe input{flex:1 1 14rem;padding:.5rem .6rem;border:1px solid var(--line);background:#fff;font:inherit}"
    ".subscribe button{padding:.5rem .9rem;border:1px solid var(--accent);background:var(--accent);color:#fff;font:inherit;cursor:pointer}"
    ".subscribe small{color:var(--muted-2,#8b8680);width:100%}"
    ".explore-box h2{font-size:1.15rem}"
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
    # Reading options: font scale, night mode, contents drawer, toast
    "html[data-fs=xs] body{font-size:15px}"
    "html[data-fs=sm] body{font-size:16px}"
    "html[data-fs=md] body{font-size:17px}"
    "html[data-fs=lg] body{font-size:19px}"
    "html[data-fs=xl] body{font-size:21px}"
    "html[data-theme=dark]{--fg:#e8e4dc;--muted:#a3a09a;--line:#32353b;"
    "--accent:#e0907d;--paper:#12141a;--ink-soft:#c6c1b7;--warn-bg:#3a3018;--warn-bd:#b58a45}"
    "html[data-theme=dark] body{background:var(--paper);color:var(--fg)}"
    "html[data-theme=dark] h1,html[data-theme=dark] h2,html[data-theme=dark] h3,"
    "html[data-theme=dark] .glossary dt{color:#f2ede4}"
    "html[data-theme=dark] .progress-card,html[data-theme=dark] .disclosure{background:#191c22}"
    "html[data-theme=dark] .subscribe input{background:#0d1014;color:var(--fg);border-color:var(--line)}"
    "html[data-theme=dark] .explore-list{background:#191c22}"
    ".reader-bar{display:flex;flex-wrap:wrap;align-items:center;gap:.35rem;"
    "padding:.55rem 0;border-bottom:1px solid var(--line);font-family:system-ui,sans-serif;"
    "font-size:.78rem}"
    ".reader-bar .rb-label{color:var(--muted);letter-spacing:.04em;margin-right:.4rem}"
    ".reader-bar button{background:none;border:1px solid var(--line);color:var(--muted);"
    "border-radius:4px;padding:.25rem .55rem;font:inherit;cursor:pointer}"
    ".reader-bar button:hover{color:var(--fg);border-color:var(--muted)}"
    ".reader-bar button[aria-expanded=true]{color:var(--fg);border-color:var(--accent)}"
    ".toast{position:fixed;left:50%;bottom:1.4rem;transform:translate(-50%,1rem);"
    "background:#1c1b19;color:#fff;font-family:system-ui,sans-serif;font-size:.82rem;"
    "padding:.55rem .9rem;border-radius:5px;opacity:0;pointer-events:none;"
    "transition:opacity .2s,transform .2s;z-index:20;max-width:80vw}"
    ".toast.on{opacity:1;transform:translate(-50%,0)}"
    ".toc-panel{position:fixed;inset:0 0 0 auto;width:min(88vw,360px);background:var(--paper);"
    "border-left:1px solid var(--line);box-shadow:-8px 0 26px rgba(0,0,0,.12);z-index:30;"
    "padding:1.2rem 1.3rem 2rem;overflow:auto;font-family:system-ui,sans-serif}"
    ".toc-panel h2{font-size:1rem;margin:0 0 .8rem;letter-spacing:.06em;text-transform:uppercase;"
    "color:var(--muted)}"
    ".toc-panel ol{list-style:none;margin:0;padding:0}"
    ".toc-panel li{border-bottom:1px solid var(--line);padding:.55rem 0;font-size:.86rem}"
    ".toc-panel a{text-decoration:none;color:var(--fg);display:block}"
    ".toc-panel a .n{display:block;color:var(--accent);font-size:.7rem;letter-spacing:.1em;"
    "text-transform:uppercase}"
    ".toc-panel a[aria-current=page]{color:var(--accent);font-weight:700}"
    ".toc-panel .close{background:none;border:0;color:var(--muted);cursor:pointer;"
    "font:inherit;float:right}"
    ".kbd-hint{display:none;color:var(--muted);font-family:system-ui,sans-serif;"
    "font-size:.76rem;margin-top:.6rem}"
    "@media(hover:hover) and (min-width:700px){.kbd-hint{display:block}}"

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
         switches: dict | None = None, page_kind: str = "",
         chapter_num: str = "", noindex: bool = False,
         toc_html: str = "") -> str:
    t = LOCALES[language]
    w = work(C.WORK, language)
    base = C.SITE["base_url"]
    canonical = base + canonical_path
    feed_path = route(language, "/feed.xml")
    rss_ok = language not in C.SUMMARY_LANGS
    noindex = is_draft or noindex or C.PREVIEW_DRAFTS or bool(C.REVISION_SET)
    ld = ""
    if jsonld is not None and not noindex:
        obj = jsonld if isinstance(jsonld, list) else [jsonld]
        ld = '<script type="application/ld+json">' + json.dumps(
            obj, ensure_ascii=False).replace("<", "\\u003c") + "</script>"
    # Only indexable, independently approved translations enter SEO clusters.
    alternate_tags = []
    if not noindex and alternates:
        for lang, path in alternates.items():
            if lang in C.SUMMARY_LANGS:
                continue  # 概要节录页不进 hreflang 集群
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
    summary_banner = (f'<div class="banner" data-summary-edition="true">'
                      f'<strong>{html.escape(t["summary_title"])}</strong> '
                      f'{html.escape(t["summary_notice"])}</div>') if language in C.SUMMARY_LANGS else ""
    revision_banner = ('<div class="banner"><strong>Classical-fiction fusion — revised draft.</strong> '
                       'Independent local preview. Not approved and not published. '
                       '<a href="/revision-notes/">创作来源、实质变化与审核要点</a></div>') if C.REVISION_SET else ""
    disclosure = (f'<div class="disclosure" data-ai-disclosure="true"><strong>'
                  f'{html.escape(t["disclosure_title"])}</strong> {html.escape(disclosure_text)} '
                  f'<a href="{route(language, "/about/")}">{html.escape(t["full_disclosure"])}</a>.</div>')
    # Explore menu: entry points to the evergreen companion pages.
    ex = EXTRA[language]
    explore_links = " ".join(
        f'<a href="{html.escape(route(language, f"/{slug}/"))}">'
        f'{html.escape(EV.PAGES[slug][language])}</a>' for slug in EV.PAGES)
    if language == "en" and not (C.PREVIEW_DRAFTS or C.REVISION_SET):
        explore_links += "".join(
            f'<a href="{html.escape(a["slug"].join(["/", "/"]))}">{html.escape(a["title"])}</a>'
            for a in AX.ACTS)
        explore_links += '<a href="/glossary/">Glossary</a>'
        explore_links += "".join(
            f'<a href="/{slug}/">{html.escape(XT.PAGES[slug]["title"])}</a>' for slug in XT.ORDER)
    show_explore = not (C.PREVIEW_DRAFTS or C.REVISION_SET)
    novels_link = (f'<a href="{route(language, "/novels/")}">'
                   f'{html.escape(BC.COPY[language]["novels"])}</a>'
                   if not (C.PREVIEW_DRAFTS or C.REVISION_SET) else "")
    explore_menu = (
        f'<div class="explore"><button type="button" class="explore-btn" '
        f'aria-expanded="false" aria-controls="explore-list">{html.escape(ex["explore"])} ▾</button>'
        f'<div class="explore-list" id="explore-list">{explore_links}</div></div>') if show_explore else ""
    rss_link = (f'<link rel="alternate" type="application/rss+xml" '
                f'title="{html.escape(w["title"])} — chapters" '
                f'href="{html.escape(base + feed_path)}"/>') if rss_ok else ""
    sub_form = ""
    rss_text = f'<a href="{html.escape(base + feed_path)}">RSS</a>' if rss_ok else ""
    sub_js = ""
    internal = bool(C.SUBSCRIBE_ENDPOINT) and C.SUBSCRIBE_ENDPOINT.startswith("/")
    if C.SUBSCRIBE_ENDPOINT and rss_ok and not C.PREVIEW_DRAFTS:
        form_attrs = ('data-internal'
                      if internal else
                      f'method="post" action="{html.escape(C.SUBSCRIBE_ENDPOINT)}" target="_blank"')
        sub_form = (f'<form class="subscribe" {form_attrs}>' if not internal else
                    f'<form class="subscribe" {form_attrs} novalidate>')
        sub_form += (f'<label for="sub-email">{html.escape(t["subscribe"])}</label>'
                     f'<input id="sub-email" type="email" name="email" '
                     f'placeholder="you@yourmail.com" required/>'
                     f'<button type="submit">{html.escape(t["subscribe_button"])}</button>'
                     f'<small data-msg aria-live="polite">{html.escape(t["subscribe_hint"])}</small></form>')
    if internal and rss_ok:
        sub_js = """
var sf=document.querySelector('form.subscribe[data-internal]');
if(sf){sf.addEventListener('submit',function(e){e.preventDefault();
  if(sf.dataset.busy==='1')return;
  var box=sf.querySelector('[data-msg]'); var btn=sf.querySelector('button');
  var em=sf.querySelector('input[type=email]').value||'';
  sf.dataset.busy='1'; btn.disabled=true;
  fetch('%s',{method:'POST',headers:{'content-type':'application/json'},
    body:JSON.stringify({email:em,source:location.pathname})})
  .then(function(r){return r.json();})
  .then(function(d){
    if(d&&d.ok){box.textContent=%s;sf.querySelector('input[type=email]').value='';}
    else{box.textContent=%s;}
  })
  .catch(function(){box.textContent=%s;})
  .then(function(){sf.dataset.busy='0';btn.disabled=false;});
});}
""" % ("/api/subscribe", repr(t["subscribe_ok"]), repr(t["subscribe_err"]), repr(t["subscribe_err"]))
    progress_js = """
var PK=document.body.getAttribute('data-page-kind');
var CN=document.body.getAttribute('data-chapter-num')||'';
var LS={'key':'cinder-progress-'+document.documentElement.lang};
function readLS(){try{return JSON.parse(localStorage.getItem(LS.key)||'{}')}catch(e){return {}}}
function writeLS(o){try{localStorage.setItem(LS.key,JSON.stringify(o))}catch(e){}}
if(PK==='chapter'&&CN){var s=readLS();s.num=CN;s.href=location.pathname;s.title=document.querySelector('h1')?document.querySelector('h1').textContent:'';writeLS(s)}
if(PK==='home'){
  var s=readLS();
  var rc=document.querySelector('[data-resume]');var pc=document.querySelector('[data-progress]');
  if(s&&s.num&&rc){
    var link=rc.querySelector('a');if(link&&s.href){link.href=s.href;link.textContent=(__HINT__).replace('{n}',s.num)+' →';rc.hidden=false}
  }
  if(s&&s.num&&pc){pc.hidden=false;var pt=pc.querySelector('[data-progress-text]');if(pt)pt.textContent=(s.title||('Ch.'+s.num))}
  var clr=document.querySelector('[data-clear]');if(clr){clr.addEventListener('click',function(){try{localStorage.removeItem(LS.key)}catch(e){}location.reload()})}
}
""".replace('__HINT__', json.dumps(ex["resume_hint"], ensure_ascii=False))
    tools_html = (
        f'<div class="reader-bar" role="group" aria-label="{html.escape(t["reader_tools"])}">'
        f'<span class="rb-label">{html.escape(t["reader_tools"])}</span>'
        f'<button type="button" data-fs="-" aria-label="{html.escape(t["font_smaller"])}" title="{html.escape(t["font_smaller"])}">A−</button>'
        f'<button type="button" data-fs="+" aria-label="{html.escape(t["font_larger"])}" title="{html.escape(t["font_larger"])}">A+</button>'
        f'<button type="button" data-theme-toggle aria-pressed="false">{html.escape(t["night_mode"])}</button>'
        f'<button type="button" data-copy>{html.escape(t["copy_link"])}</button>'
        + (f'<button type="button" data-toc-btn aria-expanded="false" '
           f'aria-controls="toc-panel">{html.escape(t["toc_open"])}</button>' if toc_html else "")
        + '</div>')
    extra_js = """
(function(){
  var root=document.documentElement;
  var L=__LABELS__;
  function rd(k,d){try{return localStorage.getItem(k)||d}catch(e){return d}}
  function wr(k,v){try{localStorage.setItem(k,v)}catch(e){}}
  var steps=['xs','sm','md','lg','xl'];
  var fs=rd('cinder-fs','md');
  if(steps.indexOf(fs)<0){fs='md'}
  root.setAttribute('data-fs',fs);
  function applyFs(n){fs=n;root.setAttribute('data-fs',n);wr('cinder-fs',n)}
  var bar=document.querySelector('.reader-bar');
  if(bar){bar.addEventListener('click',function(e){
    var b=e.target.closest('button'); if(!b)return;
    if(b.hasAttribute('data-fs')){
      var i=steps.indexOf(fs);
      i=b.getAttribute('data-fs')==='+'?Math.min(steps.length-1,i+1):Math.max(0,i-1);
      applyFs(steps[i]);
    }
  });}
  var th=rd('cinder-theme','');
  if(!th&&window.matchMedia&&window.matchMedia('(prefers-color-scheme: dark)').matches){th='dark'}
  function applyTheme(v){
    if(v==='dark'){root.setAttribute('data-theme','dark')}else{root.removeAttribute('data-theme')}
    var tb=document.querySelector('[data-theme-toggle]');
    if(tb){
      tb.textContent=v==='dark'?L.day_mode:L.night_mode;
      tb.setAttribute('aria-pressed',v==='dark'?'true':'false');
    }
  }
  applyTheme(th);
  var tb=document.querySelector('[data-theme-toggle]');
  if(tb){tb.addEventListener('click',function(){
    th=(root.getAttribute('data-theme')==='dark')?'light':'dark';wr('cinder-theme',th);applyTheme(th);
  });}
  var cb=document.querySelector('[data-copy]');
  var toast=document.getElementById('toast');
  function say(msg){ if(!toast)return; toast.textContent=msg; toast.classList.add('on');
    clearTimeout(say.t); say.t=setTimeout(function(){toast.classList.remove('on')},2200); }
  if(cb&&toast){cb.addEventListener('click',function(){
    var url=location.href;
    if(navigator.clipboard&&navigator.clipboard.writeText){
      navigator.clipboard.writeText(url).then(function(){say(L.copied)},function(){say(url)});
    } else {
      var t=document.createElement('textarea'); t.value=url; document.body.appendChild(t);
      t.select(); try{document.execCommand('copy'); say(L.copied);}catch(e){say(url);}
      document.body.removeChild(t);
    }
  });}
  var tocBtn=document.querySelector('[data-toc-btn]');
  var panel=document.getElementById('toc-panel');
  if(tocBtn&&panel){
    var closeBtn=panel.querySelector('[data-toc-close]');
    function setOpen(v){
      panel.hidden=!v; tocBtn.setAttribute('aria-expanded',v?'true':'false');
      if(v){panel.setAttribute('tabindex','-1');panel.focus();}
    }
    tocBtn.addEventListener('click',function(){setOpen(panel.hidden)});
    if(closeBtn){closeBtn.addEventListener('click',function(){setOpen(false);tocBtn.focus()})}
    document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!panel.hidden){setOpen(false);tocBtn.focus()}});
    panel.addEventListener('click',function(e){if(e.target.closest('a')){setOpen(false)}});
  }
  var nav=document.querySelector('.chapter-nav');
  if(nav){
    document.addEventListener('keydown',function(e){
      if(e.metaKey||e.ctrlKey||e.altKey)return;
      var tag=(e.target.tagName||'').toLowerCase();
      if(tag==='input'||tag==='textarea'||tag==='select')return;
      var prev=nav.querySelector('.prev'),next=nav.querySelector('.next');
      if(e.key==='ArrowLeft'&&prev){location.assign(prev.href)}
      if(e.key==='ArrowRight'&&next){location.assign(next.href)}
    });
  }
})();
""".replace('__LABELS__', json.dumps({k: t[k] for k in ("night_mode", "day_mode", "copied")}, ensure_ascii=False))
    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}"/>
<meta name="robots" content="{'noindex,follow' if noindex else 'index,follow'}"/>
<link rel="canonical" href="{html.escape(canonical)}"/>
{rss_link}
{chr(10).join(alternate_tags)}
{ld}
<style>{STYLE}</style>
</head>
<body data-page-kind="{html.escape(page_kind)}" data-chapter-num="{html.escape(chapter_num)}">
<div class="progress" id="progress"></div>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<header class="site"><div class="wrap">
  <a class="brand" href="{route(language)}">{html.escape(C.SITE['name'])}</a>
  <nav>{novels_link}<a href="{route(language, '/about/')}">{html.escape(t['about'])}</a>{explore_menu}</nav>
</div></header>
<div class="wrap">
<nav class="language-switch" aria-label="{html.escape(t['languages'])}">{' '.join(switch_links)}</nav>
{tools_html}
{toc_html}
{revision_banner}
{disclosure_banner(is_draft, language)}
{summary_banner}
{body}
{disclosure}
{sub_form}
<footer>&copy; {html.escape(w['author'])} · {html.escape(w['title'])}. {html.escape(t['fiction'])} · {rss_text}</footer>
</div>
<script>
window.addEventListener('scroll',function(){{
  var h=document.documentElement;
  var max=(h.scrollHeight-h.clientHeight);
  var p=max>0?(h.scrollTop/max)*100:0;
  document.getElementById('progress').style.width=p+'%';
}});
var exBtn=document.querySelector('.explore-btn');
if(exBtn){{exBtn.addEventListener('click',function(){{
  var box=this.parentElement;var open=box.classList.toggle('open');
  this.setAttribute('aria-expanded',open?'true':'false');
}});}}
{progress_js}
{sub_js}
{extra_js}
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
            "language": language, "review_date": meta.get("review_date", ""),
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


def _chapter_li(c: dict, t: dict) -> str:
    draft_tag = f' <span class="meta">· {html.escape(t["draft_tag"])}</span>' if not c["approved"] else ""
    summary = f'<p class="summary">{html.escape(c["summary"])}</p>' if c["summary"] else ""
    return (f'<li><a href="{chapter_path(c)}" data-chapter="{html.escape(str(c["num"]))}">'
            f'<span class="num">{html.escape(t["chapter"].format(n=c["num"]))}</span>'
            f'<h3>{html.escape(c["title"])}{draft_tag}</h3>{summary}'
            f'<span class="readtime">{html.escape(t["readtime"].format(n=c["readtime"]))}</span></a></li>')


def render_home(chapters: list[dict], out: Path, language: str = "en", collection: dict | None = None):
    t = LOCALES[language]
    ex = EXTRA[language]
    w = work(C.WORK, language)
    collection = collection or {language: chapters}
    visible = [c for c in chapters if c["approved"] or C.PREVIEW_DRAFTS]
    approved = any(c["approved"] for c in chapters)

    # Group chapters by act. English links to the five /part-*/ pages; translated
    # editions carry localized part labels only (no act pages), so they use the same
    # five ranges with their own labels.
    if language == "en":
        groups = [(act["range"], act["title"], act["slug"]) for act in AX.ACTS]
    else:
        bands = [(1, 3), (4, 9), (10, 12), (13, 16), (17, 20)]
        groups = [(band, ex["parts"][i], None) for i, band in enumerate(bands)]
    toc_parts = []
    for (lo, hi), label, slug in groups:
        group = [c for c in visible if str(c["num"]).isdigit() and lo <= int(c["num"]) <= hi]
        if not group:
            continue
        items = "\n".join(_chapter_li(c, t) for c in group)
        title = html.escape(label)
        if slug and not C.PREVIEW_DRAFTS:
            title = f'<a href="/{html.escape(slug)}/">{title}</a>'
        toc_parts.append(f'<section class="part"><h3 class="part-title">{title}</h3>'
                         f'<ul class="chapters">{items}</ul></section>')
    toc = "\n".join(toc_parts) or f'<p class="meta">{html.escape(t["no_chapters"])}</p>'

    # Start / continue reading CTA (progress injected client-side).
    first = visible[0] if visible else None
    start = (f'<p class="cta"><a class="btn" href="{chapter_path(first)}">'
             f'{html.escape(ex["start_reading"])}</a></p>') if first else ""
    resume = (f'<p class="resume" data-resume hidden><a href="#"></a></p>')
    progress = (f'<aside class="progress-card" data-progress hidden>'
                f'<strong>{html.escape(ex["progress_label"])}</strong> '
                f'<span data-progress-text></span> '
                f'<button type="button" class="link-btn" data-clear>'
                f'{html.escape(ex["clear_progress"])}</button>'
                f'<small>{html.escape(ex["progress_hint"])}</small></aside>')

    # Explore entry points to the companion pages.
    explore_links = " · ".join(
        f'<a href="{html.escape(route(language, f"/{slug}/"))}">'
        f'{html.escape(EV.PAGES[slug][language])}</a>' for slug in EV.PAGES)
    explore_box = (f'<section class="explore-box"><h2>{html.escape(ex["further"])}</h2>'
                   f'<p>{explore_links}</p></section>') if not (C.PREVIEW_DRAFTS or C.REVISION_SET) else ""

    pending = (f'<p class="banner">{html.escape(t["pending"])} '
               f'<a href="/">{html.escape(t["read_english"])}</a></p>') if language != "en" and not approved else ""
    body = f"""<section class="hero">
<span class="eyebrow">{html.escape(t['short_story'])} · {html.escape(w['genre'])}</span>
<h1>{html.escape(w['title'])}</h1><p class="sub">{html.escape(w['subtitle'])}</p>
<p class="byline meta">{html.escape(t['by'].format(author=w['author']))} · {html.escape(t['stats'].format(n=len(visible)))}</p>
{start}{resume}</section><p>{html.escape(w['description'])}</p>{pending}{progress}<hr/>
<h2>{html.escape(t['chapters'])}</h2>{toc}
{explore_box}
<p class="meta"><a href="{route(language, '/about/')}">{html.escape(t['about_hint'])}</a></p>"""
    write_page(out, route(language), page(f"{w['title']} — {C.SITE['name']}", w["description"],
               route(language), body, book_schema(language), is_draft=not approved,
               language=language, alternates=page_alternates(collection), page_kind="home"))


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
    by_term = {p["term"]: slug for slug, p in GX.PAGES.items()}
    if language == "en" and not C.PREVIEW_DRAFTS:
        terms = "\n".join(
            f'<dt><a href="/glossary/{by_term.get(term, "")}/">{html.escape(term)}</a></dt>'
            f"<dd>{html.escape(desc)}</dd>" if term in by_term
            else f"<dt>{html.escape(term)}</dt><dd>{html.escape(desc)}</dd>"
            for term, desc in glossary)
    else:
        terms = "\n".join(f"<dt>{html.escape(term)}</dt><dd>{html.escape(desc)}</dd>"
                           for term, desc in glossary)
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


def render_evergreen_pages(out: Path, collection: dict, paths: list[str]):
    """Render evergreen companion pages (world / characters / themes / faq).

    These are editorial content derived from the world bible and outlines. They are
    not chapters, so they do not pass through the chapter human-review gate; the
    AI-assisted disclosure is shown by the shared page() skeleton.
    """
    for language in collection:
        w = work(C.WORK, language)
        for slug in EV.PAGES:
            title = EV.TITLES[slug][language]
            desc = EV.DESCRIPTIONS[slug][language]
            path = route(language, f"/{slug}/")
            # Shared navigation across the four evergreen pages of this language.
            links = []
            for other in EV.PAGES:
                current = ' aria-current="page"' if other == slug else ''
                links.append(f'<a href="{html.escape(route(language, f"/{other}/"))}"{current}>'
                             f'{html.escape(EV.PAGES[other][language])}</a>')
            nav_html = '<nav class="chapter-nav evergreen-nav">' + " · ".join(links) + "</nav>"
            blocks = []
            for heading, paragraphs in EV.CONTENT[language][slug]:
                blocks.append(f"<h2>{html.escape(heading)}</h2>")
                for para in paragraphs:
                    blocks.append(f"<p>{md_inline(para)}</p>")
            body = (f'<section class="hero"><span class="eyebrow">{html.escape(w["title"])}</span>'
                    f'<h1>{html.escape(title)}</h1><p class="sub">{html.escape(desc)}</p></section>'
                    + "".join(blocks) + nav_html)
            schemas = [book_schema(language)]
            if slug == "faq":
                # FAQPage schema, only native FAQ content (no fabricated Q&A).
                qa = [{"@type": "Question", "name": heading,
                       "acceptedAnswer": {"@type": "Answer",
                                          "text": " ".join(re.sub(r"\*\*", "", p) for p in paragraphs)}}
                      for heading, paragraphs in EV.CONTENT[language]["faq"]]
                schemas.append({"@context": "https://schema.org", "@type": "FAQPage",
                                "mainEntity": qa})
            write_page(out, path, page(title, desc, path, body, schemas,
                       language=language,
                       alternates={lang: route(lang, f"/{slug}/") for lang in collection},
                       switches={lang: route(lang, f"/{slug}/") for lang in collection},
                       noindex=language in C.SUMMARY_LANGS))
            if (not C.PREVIEW_DRAFTS and not C.REVISION_SET
                    and language not in C.SUMMARY_LANGS):
                paths.append(path)


def chapter_further_slugs(num) -> tuple[str, ...]:
    """Map a chapter to two companion pages for 'continue exploring'."""
    try:
        n = int(num)
    except (TypeError, ValueError):
        return ("world", "faq")
    if n <= 3:
        return ("world", "characters")
    if n <= 6:
        return ("themes", "world")
    if n <= 9:
        return ("characters", "themes")
    return ("themes", "faq")


def breadcrumb_schema(language: str, c: dict) -> dict:
    base = C.SITE["base_url"]
    t = LOCALES[language]
    return {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": C.SITE["name"], "item": base + route(language)},
            {"@type": "ListItem", "position": 2, "name": t["chapters"], "item": base + route(language)},
            {"@type": "ListItem", "position": 3, "name": c["title"], "item": base + chapter_path(c)},
        ],
    }


def _toc(language: str, chapters: list[dict], current_slug: str, links: list[tuple[str, str]] |
         None = None, labels: tuple[str, str] | None = None) -> str:
    """目录抽屉：章节标题列表，当前章高亮。链接由调用方给出，保持各自路径规则。"""
    t = LOCALES[language]
    rows = []
    src = links or [(c["slug"], chapter_path(c)) for c in chapters]
    for slug, href in src:
        c = next((x for x in chapters if x["slug"] == slug), None)
        if not c:
            continue
        cur = ' aria-current="page"' if slug == current_slug else ""
        rows.append(f'<li><a href="{html.escape(href)}"{cur}>'
                    f'<span class="n">{html.escape(t["chapter"].format(n=c["num"]))}</span>'
                    f'{html.escape(c["title"])}</a></li>')
    if not rows:
        return ""
    return (f'<aside class="toc-panel" id="toc-panel" hidden aria-label="{html.escape(t["toc_open"])}">'
            f'<button type="button" class="close" data-toc-close '
            f'aria-label="{html.escape(t["toc_close"])}">✕</button>'
            f'<h2>{html.escape(t["toc_open"])}</h2><ol>{"".join(rows)}</ol></aside>')


def render_chapter(c: dict, chapters: list[dict], out: Path, collection: dict | None = None):
    language = c["language"]
    t = LOCALES[language]
    w = work(C.WORK, language)
    collection = collection or {language: chapters}
    schema = {"@context": "https://schema.org", "@type": "Chapter", "name": c["title"],
              "isPartOf": {"@type": "Book", "name": w["title"],
                           "author": {"@type": "Organization", "name": w["author"]}},
              "inLanguage": w["language"]}
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(c.get("review_date", ""))):
        schema["datePublished"] = c["review_date"]
        schema["dateModified"] = c["review_date"]
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
    ex = EXTRA[language]
    further_links = " · ".join(
        f'<a href="{html.escape(route(language, f"/{slug}/"))}">'
        f'{html.escape(EV.PAGES[slug][language])}</a>' for slug in chapter_further_slugs(c["num"]))
    further = (f'<section class="explore-box"><h2>{html.escape(ex["further"])}</h2>'
               f'<p>{further_links}</p></section>') if not (C.PREVIEW_DRAFTS or C.REVISION_SET) else ""
    body = (f'<span class="eyebrow">{html.escape(t["chapter"].format(n=c["num"]))}</span>'
            f'<h1>{html.escape(c["title"])}</h1><p class="byline meta">{html.escape(w["title"])} · '
            f'{html.escape(t["by"].format(author=w["author"]))} · '
            f'{html.escape(t["readtime"].format(n=c["readtime"]))}</p>{lead}'
            f'<div class="chapter-body">{c["html"]}</div>{nav_html}'
            f'<p class="kbd-hint">{html.escape(t["keyboard_hint"])}</p>{further}')
    schemas = [schema, breadcrumb_schema(language, c)] if c["approved"] else [schema]
    write_page(out, chapter_path(c), page(f'{c["title"]} — {w["title"]}', c["summary"] or w["description"],
               chapter_path(c), body, schemas, is_draft=not c["approved"], language=language,
               alternates=page_alternates(collection, f'/chapters/{c["slug"]}/'),
               switches=chapter_switches(collection, c["slug"]),
               page_kind="chapter", chapter_num=str(c["num"]),
               noindex=language in C.SUMMARY_LANGS,
               toc_html=_toc(language, visible, c["slug"])))


def feed_path(language: str) -> str:
    return route(language, "/feed.xml")


def write_feed(language: str, chapters: list[dict], out: Path):
    """RSS 2.0：只收录已批准章节，按 review_date 倒序。摘要语言页不产出 feed。"""
    if language in C.SUMMARY_LANGS:
        return
    w = work(C.WORK, language)
    t = LOCALES[language]
    base = C.SITE["base_url"]
    approved = [c for c in chapters if c["approved"]]
    approved.sort(key=lambda c: (c.get("review_date", ""), int(c["num"])), reverse=True)
    items = []
    for c in approved:
        d = str(c.get("review_date", ""))
        try:
            dt = datetime.strptime(d, "%Y-%m-%d").replace(hour=9, tzinfo=timezone.utc)
            pub = format_datetime(dt)
        except ValueError:
            pub = ""
        link = base + chapter_path(c)
        items.append(
            "<item>"
            f"<title>{html.escape(c['title'])}</title>"
            f"<link>{html.escape(link)}</link>"
            f'<guid isPermaLink="true">{html.escape(link)}</guid>'
            + (f"<pubDate>{pub}</pubDate>" if pub else "")
            + f"<description>{html.escape(c.get('summary', ''))}</description>"
            "</item>")
    last = approved[0].get("review_date", "") if approved else ""
    try:
        last_build = format_datetime(
            datetime.strptime(last, "%Y-%m-%d").replace(hour=9, tzinfo=timezone.utc))
    except ValueError:
        last_build = ""
    rss = ('<?xml version="1.0" encoding="UTF-8"?>'
           '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel>'
           f"<title>{html.escape(w['title'])} — chapters</title>"
           f"<link>{html.escape(base + route(language))}</link>"
           f"<description>{html.escape(w['description'])}</description>"
           f"<language>{html.escape(t['lang'])}</language>"
           + (f"<lastBuildDate>{last_build}</lastBuildDate>" if last_build else "")
           + f'<atom:link href="{html.escape(base + feed_path(language))}" rel="self" type="application/rss+xml"/>'
           + "".join(items) + "</channel></rss>")
    dest = out / feed_path(language).lstrip("/")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(rss, encoding="utf-8")


def render_glossary(out: Path):
    """设定词条：/glossary/ 索引 + 5 个详情页（英文）。"""
    base = C.SITE["base_url"]
    w = work(C.WORK, "en")
    cards = "".join(
        f'<li><a href="{base}/glossary/{slug}/"><strong>{html.escape(GX.PAGES[slug]["term"])}</strong>'
        f'<span>{html.escape(GX.PAGES[slug]["short"])}</span></a></li>'
        for slug in GX.ORDER)
    body = (f'<section class="hero"><span class="eyebrow">Glossary</span>'
            f'<h1>Terms in {html.escape(w["title"])}</h1>'
            f'<p class="sub">The five words the story keeps using, explained without spoilers.</p></section>'
            f'<ul class="glossary-list">{cards}</ul>')
    schema = {"@context": "https://schema.org", "@type": "DefinedTermSet",
              "name": f"Glossary — {w['title']}",
              "url": base + "/glossary/",
              "hasDefinedTerm": [
                  {"@type": "DefinedTerm", "name": GX.PAGES[s]["term"],
                   "description": GX.PAGES[s]["short"],
                   "url": base + f"/glossary/{s}/"} for s in GX.ORDER]}
    write_page(out, "/glossary/", page(
        f"Glossary — {w['title']}", "Definitions of engram, the Loom, fill, the Grey and memory architect.",
        "/glossary/", body, schema, language="en", page_kind="glossary"))

    for slug in GX.ORDER:
        p = GX.PAGES[slug]
        blocks = [f'<section class="hero"><span class="eyebrow">Glossary</span>'
                  f'<h1>{html.escape(p["term"])}</h1>'
                  f'<p class="sub">{html.escape(p["lede"])}</p></section>']
        for heading, paras in p["sections"]:
            blocks.append(f"<h2>{html.escape(heading)}</h2>")
            blocks += [f"<p>{html.escape(x)}</p>" for x in paras]
        read_more = " · ".join(
            f'<a href="{base}/chapters/{c}/">{html.escape(c.replace("-", " ").title())}</a>'
            for c in p["chapters"])
        related = " · ".join(
            f'<a href="{base}/glossary/{r}/">{html.escape(GX.PAGES[r]["term"])}</a>'
            for r in p["see"] if r in GX.PAGES)
        blocks.append(f'<section class="explore-box"><h2>Where it appears</h2><p>{read_more}</p>'
                      f'<h2>Related terms</h2><p>{related} · <a href="{base}/glossary/">All terms</a></p></section>')
        schema = {"@context": "https://schema.org", "@type": "DefinedTerm",
                  "name": p["term"], "description": p["short"],
                  "url": f"{base}/glossary/{slug}/",
                  "inDefinedTermSet": {"@type": "DefinedTermSet", "name": "Glossary", "url": f"{base}/glossary/"}}
        write_page(out, f"/glossary/{slug}/", page(
            f"{p['term']} — glossary", p["short"], f"/glossary/{slug}/",
            "".join(blocks), schema, language="en", page_kind="glossary"))


def render_acts(out: Path, chapters: list[dict]):
    """三幕入口页：每幕一个可索引、可分享的摘要页，向下链接本幕章节。"""
    w = work(C.WORK, "en")
    base = C.SITE["base_url"]
    for act in AX.ACTS:
        lo, hi = act["range"]
        group = [c for c in chapters
                 if str(c["num"]).isdigit() and lo <= int(c["num"]) <= hi and c["approved"]]
        items = "".join(
            f'<li><a href="{base}/chapters/{c["slug"]}/">'
            f'<span class="num">Chapter {c["num"]}</span>'
            f'<h3>{html.escape(c["title"])}</h3>'
            f'<p>{html.escape(c.get("summary", ""))}</p></a></li>' for c in group)
        body = (f'<section class="hero"><span class="eyebrow">{html.escape(act["title"])}</span>'
                f'<h1>{html.escape(act["title"])}</h1>'
                f'<p class="sub">{html.escape(act["lede"])}</p></section>'
                + "".join(f"<p>{html.escape(x)}</p>" for x in act["body"])
                + (f'<ul class="acts-chapters">{items}</ul>' if items else "")
                + f'<p><a href="{base}/">Full contents</a> · <a href="{base}/glossary/">Glossary</a></p>')
        schema = {"@context": "https://schema.org", "@type": "CreativeWork",
                  "name": act["title"], "description": act["lede"],
                  "url": f"{base}/{act['slug']}/",
                  "isPartOf": {"@type": "Book", "name": w["title"],
                               "author": {"@type": "Organization", "name": w["author"]}}}
        write_page(out, f"/{act['slug']}/", page(
            f"{act['title']} — {w['title']}", act["lede"], f"/{act['slug']}/",
            body, schema, language="en", page_kind="act"))


def render_extras(out: Path):
    """补充页：/timeline/、/who-is-who/、/reading-guide/、/season-two/（英文）。"""
    base = C.SITE["base_url"]
    w = work(C.WORK, "en")
    for slug in XT.ORDER:
        p = XT.PAGES[slug]
        blocks = [f'<section class="hero"><span class="eyebrow">Companion</span>'
                  f'<h1>{html.escape(p["title"])}</h1>'
                  f'<p class="sub">{html.escape(p["lede"])}</p></section>']
        for heading, paras in p["sections"]:
            blocks.append(f"<h2>{html.escape(heading)}</h2>")
            blocks += [f"<p>{html.escape(x)}</p>" for x in paras]
        others = " · ".join(
            f'<a href="{base}/{o}/">{html.escape(XT.PAGES[o]["title"])}</a>'
            for o in XT.ORDER if o != slug)
        blocks.append(f'<section class="explore-box"><h2>More companion pages</h2><p>{others}</p>'
                      f'<p><a href="{base}/">Full contents</a> · <a href="{base}/glossary/">Glossary</a></p></section>')
        schema = {"@context": "https://schema.org", "@type": "Article",
                  "headline": p["title"], "description": p["description"],
                  "url": f"{base}/{slug}/",
                  "isPartOf": {"@type": "Book", "name": w["title"],
                               "author": {"@type": "Organization", "name": w["author"]}}}
        write_page(out, f"/{slug}/", page(
            f"{p['title']} — {w['title']}", p["description"], f"/{slug}/",
            "".join(blocks), schema, language="en", page_kind="extra"))


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


def write_not_found(out: Path):
    """真 404 页，避免未知路径回落成首页副本（软 404）。"""
    t = LOCALES["en"]
    w = work(C.WORK, "en")
    base = C.SITE["base_url"]
    body = ('<span class="eyebrow">404</span><h1>This page is not in the book</h1>'
            '<p>The address you opened does not match any chapter or companion page. '
            'You can start from the beginning, or jump to the contents.</p>'
            f'<p><a href="{base}/">Read from Chapter 1</a> · '
            f'<a href="{base}/about/">About this novel</a></p>')
    doc = f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Page not found — {html.escape(w['title'])}</title>
<meta name="robots" content="noindex,follow"/>
<style>{STYLE}</style>
</head>
<body data-page-kind="notfound">
<header class="site"><div class="wrap">
  <a class="brand" href="{base}/">{html.escape(C.SITE['name'])}</a>
  <nav><a href="{base}/about/">{html.escape(t['about'])}</a></nav>
</div></header>
<div class="wrap">
{body}
<footer>&copy; {html.escape(w['author'])} · {html.escape(w['title'])}. {html.escape(t['fiction'])}</footer>
</div>
</body>
</html>
"""
    (out / "404.html").write_text(doc, encoding="utf-8")


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
            if language not in C.SUMMARY_LANGS:  # 节录版章节不进 sitemap
                paths.extend(chapter_path(c) for c in approved)
    if revision:
        render_revision_notes(out)
    if not revision and not C.PREVIEW_DRAFTS:
        render_evergreen_pages(out, collection, paths)
        render_glossary(out)
        render_acts(out, collection["en"])
        render_extras(out)
        paths.extend(["/glossary/"] + [f"/glossary/{slug}/" for slug in GX.ORDER])
        paths.extend([f"/{act['slug']}/" for act in AX.ACTS])
        paths.extend([f"/{slug}/" for slug in XT.ORDER])
    if not revision:
        for language, chapters in collection.items():
            write_feed(language, chapters, out)
    if not revision and not C.PREVIEW_DRAFTS:
        import multibook as MB
        flagships = {}
        for language, chapters in collection.items():
            approved = [c for c in chapters if c["approved"]]
            if not approved:
                continue
            t = LOCALES[language]
            flagships[language] = [{
                "href": route(language),
                "title": t["title"],
                "tagline": t["subtitle"],
                "meta": t["stats"].format(n=len(approved)) + " · " + " · ".join(
                    p for p in [t["genre"]] if p),
            }]
        MB.render(out, paths, flagships)
    write_sitemap(paths, out)
    write_robots(out)
    write_not_found(out)
    print(f"[done] {len(paths)} indexable URLs -> {out}/")


if __name__ == "__main__":
    main()
