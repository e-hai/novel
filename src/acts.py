# -*- coding: utf-8 -*-
"""三幕结构页：把 12 章拆成 3 个可独立索引、可独立分享的入口。

小说站的问题是"只有一个入口"（首页），搜索引擎和读者都要翻到很后面才知道
这本书讲什么。三幕页各自承担一个叙事阶段的关键词与摘要，并向下链接本幕章节。
"""

ACTS = [
    {
        "slug": "part-i",
        "roman": "I",
        "title": "Part I · The Shop",
        "range": (1, 3),
        "lede": "Elias Vane repairs memories for a living, in a shop on Cinder Lane, for customers who "
                "mostly want the fact back and not the feeling.",
        "body": [
            "The first act is the trade as a job. Three customers, three cores, three kinds of damage — a "
            "chipped rim, a scene that will not close, a memory someone has already had repaired somewhere "
            "else. Each visit teaches the reader one rule of the Ward: that an engram holds a viewpoint and "
            "not an event, that fill holds a memory together without returning its feeling, and that a "
            "repairman is paid to stop the falling, not to decide what the customer should keep.",
            "It is also where the story puts its question on the counter. Elias is good at the work and "
            "increasingly unsure whether the work is kind. By the end of the act, a customer brings him "
            "something he cannot diagnose with technique: a memory that is intact, accurate, and wrong.",
        ],
    },
    {
        "slug": "part-ii",
        "roman": "II",
        "title": "Part II · The Trade",
        "range": (4, 9),
        "lede": "The middle act widens from one shop to the system behind it: the Grey, the suppliers, "
                "the people who specified what fill is allowed to do.",
        "body": [
            "Six chapters, and the story stops treating repair as a private transaction. A woman keeps receipts "
            "for memories she no longer has feelings about. A door appears in someone else's recollection and "
            "Elias has to decide whether he is looking at damage or at a message. The Grey stops being a "
            "complication in a customer and becomes something like weather — a condition the whole Ward lives "
            "inside and has agreed not to name.",
            "This is the act where the trade's paperwork starts to matter: the specification, the supplier, "
            "the rule written down by people who never meet the customers. Elias is still repairing, but he is "
            "now repairing inside a system that has already decided how much a person may forget before anyone "
            "notices.",
        ],
    },
    {
        "slug": "part-iii",
        "roman": "III",
        "title": "Part III · The Witness",
        "range": (10, 12),
        "lede": "The last act turns the machine around: the memory Elias has been avoiding is his own, "
                "and there is no technique for it.",
        "body": [
            "Three chapters, and the shop becomes a witness stand. The rule that governs repair is finally read "
            "aloud, two people end up at the Loom for reasons that are not professional, and a question that "
            "has been polite for nine chapters — what did she actually do — stops being polite.",
            "The ending does not resolve the trade. It resolves a person: a repairman who has spent the book "
            "keeping other people's memories stable while his own stayed exactly where he left it. Whether that "
            "counts as a repair is the thing the last chapter asks, and it does not answer it for the reader.",
        ],
    },
]
