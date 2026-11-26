# -*- coding: utf-8 -*-
"""multibook.py — 多部独立小说的目录页、书页、章节页与单书 RSS。

目录：content/books/<slug>/chapters/*.md（英文源）
      content/books/<slug>/translations/<lang>/*.md（译本，文件名与英文源一致）
路由：/{lang}/novels/            小说总目录
      /{lang}/novels/<slug>/     单书首页（简介 + 目录）
      /{lang}/novels/<slug>/chapters/<ch>/  章节页
      /{lang}/novels/<slug>/feed.xml        单书 RSS（节录语言不产出）
沿用 generate.py 的 page()/STYLE 与翻译门禁（status + source_sha256 + 审校人 + 日期 + 备注）。
"""
from __future__ import annotations

import html
import json
import re
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path

import books as BK
import bookcopy as BC
import booknotes as BN
import config as C
import generate as G
from locales import LOCALES, route


# ---------------------------------------------------------------------------
# 读取与门禁
# ---------------------------------------------------------------------------
def book_dir(slug: str) -> Path:
    return G.CONTENT / "books" / slug


def chapter_dir(slug: str, language: str) -> Path:
    if language == "en":
        return book_dir(slug) / "chapters"
    return book_dir(slug) / "translations" / language


def book_path(slug: str, language: str) -> str:
    return route(language, f"/novels/{slug}/")


def chapter_url(slug: str, c: dict, language: str) -> str:
    return route(language, f"/novels/{slug}/chapters/{c['slug']}/")


def notes_path(slug: str, language: str) -> str:
    return route(language, f"/novels/{slug}/notes/")


def feed_url(slug: str, language: str) -> str:
    return route(language, f"/novels/{slug}/feed.xml")


def load_chapters(slug: str, language: str = "en") -> list[dict]:
    directory = chapter_dir(slug, language)
    chapters, seen = [], set()
    if not directory.exists():
        return []
    for p in sorted(directory.glob("*.md")):
        meta, raw, body_html = G.read_doc(p)
        body_html = G.strip_leading_h1(body_html)
        chapter_slug = meta.get("slug") or re.sub(r"^\d+-", "", p.stem)
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", chapter_slug) or chapter_slug in seen:
            raise ValueError(f"Invalid or duplicate chapter slug: {p}")
        seen.add(chapter_slug)
        num = meta.get("chapter", "?")
        status = meta.get("status", "draft")
        approved = status == "approved"
        if language != "en":
            if meta.get("language") != language:
                raise ValueError(f"Translation language does not match directory: {p}")
            source = book_dir(slug) / "chapters" / p.name
            if not source.exists():
                raise ValueError(f"Translation has no English source: {p}")
            source_meta, _, _ = G.read_doc(source)
            source_slug = source_meta.get("slug") or re.sub(r"^\d+-", "", source.stem)
            if source_slug != chapter_slug or str(source_meta.get("chapter")) != str(num):
                raise ValueError(f"Translation does not match its source chapter: {p}")
            approved = G.translation_approved(meta, source_meta, G.source_digest(source))
        text = re.sub(r"^#.*$", "", raw, flags=re.M)
        units = (len(re.findall(r"[\u3400-\u9fff]", text)) if language == "yue"
                 else len(text.split()))
        readtime = max(1, round(units / (350 if language == "yue" else 220)))
        chapters.append({
            "num": num, "slug": chapter_slug, "title": meta.get("title", p.stem),
            "summary": meta.get("summary", ""), "status": status, "approved": approved,
            "words": units, "readtime": readtime, "html": body_html, "path": p,
            "language": language, "review_date": meta.get("review_date", ""),
        })
    chapters.sort(key=lambda c: int(c["num"]) if str(c["num"]).isdigit() else 999)
    return chapters


# ---------------------------------------------------------------------------
# schema
# ---------------------------------------------------------------------------
def book_schema(book: dict, language: str) -> dict:
    t = LOCALES[language]
    return {
        "@context": "https://schema.org",
        "@type": "Book",
        "name": book["title"],
        "alternateName": book["tagline"][language],
        "inLanguage": t["lang"],
        "genre": book["genre"][language],
        "author": {"@type": "Organization", "name": G.C.WORK["author"]},
        "url": C.SITE["base_url"] + book_path(book["slug"], language),
        "numberOfPages": len(load_chapters(book["slug"], language)),
        "isPartOf": {"@type": "CollectionPage", "name": BC.COPY[language]["hub_title"],
                     "url": C.SITE["base_url"] + route(language, "/novels/")},
    }


def chapter_schema(book: dict, c: dict, language: str) -> dict:
    t = LOCALES[language]
    return {
        "@context": "https://schema.org",
        "@type": "Chapter",
        "name": c["title"],
        "description": c["summary"],
        "position": c["num"],
        "inLanguage": t["lang"],
        "url": C.SITE["base_url"] + chapter_url(book["slug"], c, language),
        "isPartOf": {"@type": "Book", "name": book["title"],
                     "url": C.SITE["base_url"] + book_path(book["slug"], language)},
        "author": {"@type": "Organization", "name": G.C.WORK["author"]},
    }


# ---------------------------------------------------------------------------
# 页面
# ---------------------------------------------------------------------------
def _approved(chapters: list[dict], preview: bool = False) -> list[dict]:
    return [c for c in chapters if c["approved"] or (preview and C.PREVIEW_DRAFTS)]


def _lang_has(slug: str, language: str) -> bool:
    return any(c["approved"] for c in load_chapters(slug, language))


def render_hub(out: Path, flagships: dict | None = None):
    """小说总目录：旗舰长篇（根路径）+ 五部独立短篇。"""
    flagships = flagships or {}
    langs_with_novels = {lg for lg in LOCALES for b in BK.BOOKS if _lang_has(b["slug"], lg)}
    for language in LOCALES:
        cc = BC.COPY[language]
        t = LOCALES[language]
        cards = []
        for f in flagships.get(language, []):
            cards.append(
                f'<li><a href="{html.escape(f["href"])}"><h3>{html.escape(f["title"])}</h3>'
                f'<p class="summary">{html.escape(f["tagline"])}</p>'
                f'<span class="readtime">{html.escape(f["meta"])}</span></a></li>')
        for b in BK.BOOKS:
            chapters = _approved(load_chapters(b["slug"], language))
            if not chapters:
                continue
            meta = cc["hub_meta"].format(n=len(chapters), genre=b["genre"][language])
            cards.append(
                f'<li><a href="{html.escape(book_path(b["slug"], language))}">'
                f'<span class="num">{html.escape(b["genre"][language])}</span>'
                f'<h3>{html.escape(b["title"])}</h3>'
                f'<p class="summary">{html.escape(b["tagline"][language])}</p>'
                f'<span class="readtime">{html.escape(meta)}</span></a></li>')
        body = (f'<h1>{html.escape(cc["hub_title"])}</h1>'
                f'<p class="lede">{html.escape(cc["hub_intro"])}</p>'
                f'<ul class="chapters hub-list">{"".join(cards)}</ul>'
                f'<p class="meta">{html.escape(cc["book_note"])}</p>')
        alternates = {lg: route(lg, "/novels/") for lg in langs_with_novels}
        G.write_page(out, route(language, "/novels/"), G.page(
            f'{cc["hub_title"]} — {C.SITE["name"]}', cc["hub_intro"],
            route(language, "/novels/"), body, None, False, language,
            alternates=alternates, switches={lg: route(lg, "/novels/") for lg in LOCALES},
            page_kind="hub", noindex=language in C.SUMMARY_LANGS and False))


def _also(book: dict, language: str) -> str:
    """书页底部的跨书导览：同一语言下其他四部的书名 + 一句钩子。"""
    cc = BC.COPY[language]
    others = [b for b in BK.BOOKS if b["slug"] != book["slug"]]
    items = "".join(
        f'<li><a href="{html.escape(book_path(b["slug"], language))}">'
        f'<h3>{html.escape(b["title"])}</h3>'
        f'<p class="summary">{html.escape(b["tagline"][language])}</p></a></li>'
        for b in others)
    return (f'<section class="part"><h2 class="part-title">{html.escape(cc["also"])}</h2>'
            f'<ul class="chapters">{items}</ul></section>')


def render_book(out: Path, book: dict, language: str):
    cc = BC.COPY[language]
    t = LOCALES[language]
    chapters = _approved(load_chapters(book["slug"], language))
    if not chapters and language in C.SUMMARY_LANGS:
        # 节录语言沿用站点既有口径：照样出页，但整页 noindex、不进 sitemap。
        chapters = load_chapters(book["slug"], language)
    if not chapters:
        return
    alternates = {lg: book_path(book["slug"], lg) for lg in LOCALES
                  if lg not in C.SUMMARY_LANGS and _lang_has(book["slug"], lg)}
    switches = {lg: (book_path(book["slug"], lg) if _lang_has(book["slug"], lg)
                     else route(lg, "/novels/")) for lg in LOCALES}
    first = chapters[0]
    items = "\n".join(
        f'<li><a href="{html.escape(chapter_url(book["slug"], c, language))}" '
        f'data-chapter="{html.escape(str(c["num"]))}">'
        f'<span class="num">{html.escape(t["chapter"].format(n=c["num"]))}</span>'
        f'<h3>{html.escape(c["title"])}</h3>'
        f'<p class="summary">{html.escape(c["summary"])}</p>'
        f'<span class="readtime">{html.escape(t["readtime"].format(n=c["readtime"]))}</span></a></li>'
        for c in chapters)
    rss = (f'<p class="meta"><a href="{html.escape(feed_url(book["slug"], language))}">'
           f'{html.escape(cc["book_feed"])} (RSS)</a></p>'
           if language not in C.SUMMARY_LANGS else "")
    body = (f'<p class="meta"><a href="{html.escape(route(language, "/novels/"))}">'
            f'← {html.escape(cc["back_hub"])}</a></p>'
            f'<h1>{html.escape(book["title"])}</h1>'
            f'<p class="lede">{html.escape(book["tagline"][language])}</p>'
            f'<p class="meta">{html.escape(book["genre"][language])} · '
            f'{html.escape(t["stats"].format(n=len(chapters)))}</p>'
            f'<p class="cta"><a class="btn" href="'
            f'{html.escape(chapter_url(book["slug"], first, language))}">'
            f'{html.escape(cc["start_first"])}</a></p>'
            f'<section class="part"><h2 class="part-title">{html.escape(cc["book_toc"])}</h2>'
            f'<ul class="chapters">{items}</ul></section>'
            f'<p class="meta"><a href="{html.escape(notes_path(book["slug"], language))}">'
            f'{html.escape(cc["notes"])}</a></p>'
            f'<p class="meta">{html.escape(cc["book_note"])}</p>{rss}'
            f'{_also(book, language)}')
    G.write_page(out, book_path(book["slug"], language), G.page(
        f'{book["title"]} — {C.SITE["name"]}',
        f'{book["tagline"][language]} {book["genre"][language]}, six chapters.',
        book_path(book["slug"], language), body, book_schema(book, language), False,
        language, alternates=alternates, switches=switches, page_kind="book"))
    for i, c in enumerate(chapters):
        prev_c = chapters[i - 1] if i > 0 else None
        next_c = chapters[i + 1] if i + 1 < len(chapters) else None
        nav = []
        if prev_c:
            nav.append(f'<a class="prev" href="{html.escape(chapter_url(book["slug"], prev_c, language))}">'
                       f'{html.escape(t["previous"])}: {html.escape(prev_c["title"])}</a>')
        if next_c:
            nav.append(f'<a class="next" href="{html.escape(chapter_url(book["slug"], next_c, language))}">'
                       f'{html.escape(t["next"])}: {html.escape(next_c["title"])}</a>')
        body = (f'<p class="meta"><a href="{html.escape(book_path(book["slug"], language))}">'
                f'← {html.escape(book["title"])}</a></p>'
                f'<h1>{html.escape(c["title"])}</h1>'
                f'<p class="meta">{html.escape(book["title"])} · '
                f'{html.escape(t["chapter"].format(n=c["num"]))} · '
                f'{html.escape(t["readtime"].format(n=c["readtime"]))}</p>'
                f'<div class="chapter-body">{c["html"]}</div>'
                f'<nav class="chapter-nav">{"".join(nav)}</nav>'
                f'<p class="kbd-hint">{html.escape(t["keyboard_hint"])}</p>'
                f'<p class="meta"><a href="{html.escape(book_path(book["slug"], language))}">'
                f'{html.escape(cc["book_toc"])}</a> · '
                f'<a href="{html.escape(route(language, "/novels/"))}">'
                f'{html.escape(cc["back_hub"])}</a></p>'
                f'{_also(book, language)}')
        G.write_page(out, chapter_url(book["slug"], c, language), G.page(
            f'{c["title"]} — {book["title"]}', c["summary"], chapter_url(book["slug"], c, language),
            body, chapter_schema(book, c, language), not c["approved"], language,
            alternates={lg: chapter_url(book["slug"], c, lg) for lg in LOCALES
                        if lg not in C.SUMMARY_LANGS and chapter_url(book["slug"], c, lg)
                        and any(x["approved"] and x["slug"] == c["slug"]
                                for x in load_chapters(book["slug"], lg))},
            switches={lg: (chapter_url(book["slug"], c, lg) if _lang_has(book["slug"], lg)
                           else route(lg, "/novels/")) for lg in LOCALES},
            page_kind="chapter", chapter_num=str(c["num"]),
            noindex=language in C.SUMMARY_LANGS,
            toc_html=G._toc(language, chapters, c["slug"],
                             [(x["slug"], chapter_url(book["slug"], x, language))
                              for x in chapters])))


def render_notes(out: Path, book: dict, language: str):
    """每部书的「背景与手记」页：题材来源、写法、阅读引导。"""
    note = BN.NOTES.get(book["slug"], {}).get(language)
    if not note:
        return
    cc = BC.COPY[language]
    body = (f'<p class="meta"><a href="{html.escape(book_path(book["slug"], language))}">'
            f'← {html.escape(cc["back_book"])}</a></p>'
            f'<h1>{html.escape(note["title"])}</h1>'
            f'<p class="lede">{html.escape(cc["notes_lede"])}</p>'
            f'<p class="meta"><a href="{html.escape(book_path(book["slug"], language))}">'
            f'{html.escape(book["title"])}</a> · {html.escape(book["genre"][language])}</p>'
            + "".join(f'<p>{html.escape(p)}</p>' for p in note["paras"]) +
            f'<p class="meta"><a href="{html.escape(book_path(book["slug"], language))}">'
            f'{html.escape(cc["book_toc"])}</a> · '
            f'<a href="{html.escape(route(language, "/novels/"))}">'
            f'{html.escape(cc["back_hub"])}</a></p>')
    schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": note["title"],
        "about": book["title"],
        "inLanguage": LOCALES[language]["lang"],
        "url": C.SITE["base_url"] + notes_path(book["slug"], language),
        "author": {"@type": "Organization", "name": G.C.WORK["author"]},
        "isPartOf": {"@type": "Book", "name": book["title"],
                     "url": C.SITE["base_url"] + book_path(book["slug"], language)},
    }
    usable = {lg for lg in LOCALES
              if lg not in C.SUMMARY_LANGS and BN.NOTES.get(book["slug"], {}).get(lg)
              and _lang_has(book["slug"], lg)}
    alternates = {lg: notes_path(book["slug"], lg) for lg in usable}
    G.write_page(out, notes_path(book["slug"], language), G.page(
        f'{note["title"]} — {book["title"]}', cc["notes_lede"],
        notes_path(book["slug"], language), body, schema, False, language,
        alternates=alternates,
        switches={lg: (notes_path(book["slug"], lg) if lg in usable
                       else route(lg, "/novels/")) for lg in LOCALES},
        page_kind="notes", noindex=language in C.SUMMARY_LANGS))


def write_feed(book: dict, chapters: list[dict], language: str, out: Path):
    if language in C.SUMMARY_LANGS:
        return
    t = LOCALES[language]
    base = C.SITE["base_url"]
    now = datetime.now(timezone.utc)
    items = []
    for c in chapters:
        if not c["approved"]:
            continue
        try:
            stamp = datetime.strptime(c["review_date"], "%Y-%m-%d").replace(tzinfo=timezone.utc)
        except (TypeError, ValueError):
            stamp = now
        items.append(
            f"<item><title>{html.escape(c['title'])}</title>"
            f"<link>{html.escape(base + chapter_url(book['slug'], c, language))}</link>"
            f"<guid isPermaLink=\"true\">{html.escape(base + chapter_url(book['slug'], c, language))}</guid>"
            f"<description>{html.escape(c['summary'])}</description>"
            f"<pubDate>{format_datetime(stamp)}</pubDate></item>")
    document = (
        '<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel>'
        f"<title>{html.escape(book['title'])} — {html.escape(t['chapters'])}</title>"
        f"<link>{html.escape(base + book_path(book['slug'], language))}</link>"
        f"<description>{html.escape(book['tagline'][language])}</description>"
        f"<language>{html.escape(t['lang'])}</language>"
        f"<lastBuildDate>{format_datetime(now)}</lastBuildDate>"
        f"{''.join(items)}</channel></rss>")
    dest = out / feed_url(book["slug"], language).strip("/")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(document, encoding="utf-8")


# ---------------------------------------------------------------------------
# 入口
# ---------------------------------------------------------------------------
def sitemap_paths() -> list[str]:
    """与 render() 一致的可索引路径列表（供 sitemap 与测试共用）。"""
    result = [route(language, "/novels/") for language in LOCALES]
    for book in BK.BOOKS:
        for language in LOCALES:
            chapters = _approved(load_chapters(book["slug"], language))
            if not chapters:
                continue
            result.append(book_path(book["slug"], language))
            if language not in C.SUMMARY_LANGS:
                result.extend(chapter_url(book["slug"], c, language) for c in chapters)
                if BN.NOTES.get(book["slug"], {}).get(language):
                    result.append(notes_path(book["slug"], language))
    return result


def render(out: Path, paths: list[str], flagships: dict | None = None):
    """生成全部多书页面，并把可索引路径追加到 sitemap 列表。"""
    render_hub(out, flagships)
    for language in LOCALES:
        paths.append(route(language, "/novels/"))
    for book in BK.BOOKS:
        for language in LOCALES:
            chapters = _approved(load_chapters(book["slug"], language))
            if not chapters:
                continue
            render_book(out, book, language)
            render_notes(out, book, language)
            write_feed(book, chapters, language, out)
            paths.append(book_path(book["slug"], language))
            if language not in C.SUMMARY_LANGS:
                paths.extend(chapter_url(book["slug"], c, language) for c in chapters)
                if BN.NOTES.get(book["slug"], {}).get(language):
                    paths.append(notes_path(book["slug"], language))
