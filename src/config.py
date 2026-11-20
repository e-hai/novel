# -*- coding: utf-8 -*-
"""
config.py — 精品小说站配置
《The Memory Repairman》——AI 起草、人工终审的精工科幻短篇。
设计原则：半自动、人工关口不可省、每页有 AI 披露、不伪造作者。
"""
from __future__ import annotations

import os

# 站点域名：默认 Cloudflare Pages 免费域名，可用环境变量覆盖。
DEFAULT_BASE_URL = "https://novel.pages.dev"
BASE_URL = os.environ.get("SITE_BASE_URL", DEFAULT_BASE_URL).rstrip("/")

# 作品与作者。作者用真实署名，由人类编辑在 SITE_PUBLISHER 填入，不伪造头像/履历。
WORK = {
    "title": "The Memory Repairman",
    "subtitle": "Three stories about the things we choose to forget.",
    "author": os.environ.get("SITE_AUTHOR", "C. Vale").strip(),  # ← 人类编辑改成自己的署名
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
