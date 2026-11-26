# -*- coding: utf-8 -*-
"""
config.py — 精品小说站配置
《The Memory Repairman》——AI 起草、人工终审的精工科幻短篇。
设计原则：半自动、人工关口不可省、每页有 AI 披露、不伪造作者。
"""
from __future__ import annotations

import os

# 站点域名：默认 Cloudflare Pages 免费域名，可用环境变量覆盖。
DEFAULT_BASE_URL = "https://novel-9wi.pages.dev"
BASE_URL = os.environ.get("SITE_BASE_URL", DEFAULT_BASE_URL).rstrip("/")

# 作品与作者。发布署名 apprank studio，可由 SITE_AUTHOR 环境变量覆盖，不伪造头像/履历。
WORK = {
    "title": "The Memory Repairman",
    "subtitle": "Thirteen parts, one shop: stories about the things we choose to forget.",
    "author": (os.environ.get("SITE_AUTHOR", "").strip() or "apprank studio"),  # 发布署名，可被 SITE_AUTHOR 变量覆盖
    "genre": "Science Fiction",
    "language": "en",
    "description": (
        "A near-future science fiction short story about a man who repairs other people's "
        "memories — and the one memory he is forbidden to touch."
    ),
    "isbn": "",  # 有则填，用于 Book schema
    "date_published": "2026-11-20",
}

SITE = {
    "name": "Cinder Lane",
    "base_url": BASE_URL,
    "lang": "en",
    "contact": os.environ.get("SITE_CONTACT", "").strip(),  # 可选：联系邮箱
}

# 发布门槛：
#   draft_only=True  -> 只发布 status=approved 的章节（默认，合规安全）
#   若想本地预览草稿，设环境变量 PREVIEW_DRAFTS=1（会在每章显示醒目草稿横幅）
PREVIEW_DRAFTS = os.environ.get("PREVIEW_DRAFTS", "").strip() in ("1", "true", "True")

# 概要节录语言：章节只翻出开头段落，正文远短于英文原文（约 1/9 长度）。
# 这类页面保留给人读（有语言切换和阅读路径），但不参与索引与 sitemap，避免薄页稀释站点质量。
# 2026-11-26：粤语不再是节录版，第 21-100 章已是全文翻译，故此集合清空。
SUMMARY_LANGS = set()

# 邮件订阅：填 Buttondown 的 embed 地址即可自动在页脚出现订阅表单，例如
#   SITE_SUBSCRIBE_ENDPOINT=https://buttondown.email/api/emails/embed-subscribe/<username>
# 未设置时页面只显示 RSS，不渲染任何空表单。
SUBSCRIBE_ENDPOINT = os.environ.get("SITE_SUBSCRIBE_ENDPOINT", "/api/subscribe").strip()


# 古典融合等修订只能独立预览，不替换已审核原稿和对应译文。
REVISION_SET = os.environ.get("NOVEL_REVISION_SET", "").strip()
# 草稿预览独立输出，不能意外覆盖生产构建。
DEFAULT_OUTPUT_DIR = ("revision-preview-site" if REVISION_SET else
                      "preview-site" if PREVIEW_DRAFTS else "site")
OUTPUT_DIR = os.environ.get("SITE_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
