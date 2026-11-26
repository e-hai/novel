# -*- coding: utf-8 -*-
"""补充页（英文）：时间线、人物表、阅读指南、第二季说明。

这四页承担"读者刚进来还不知道这是什么书"的检索需求，也把分散在二十章里的
设定与人物收成可引用的长尾入口。
"""

PAGES = {
    "timeline": {
        "title": "Story timeline",
        "description": "A dated timeline of The Memory Repairman, from the shop's opening to the "
                       "hearing that renamed the seam a joint.",
        "lede": "Twenty chapters, one lane, eleven years of trade. This timeline puts the dates in "
                "order without giving away what any of them cost.",
        "sections": [
            ("Before the first chapter",
             ["Elias Vane takes licence 4-119 at twenty-six and opens a repair bench on Cinder Lane. "
              "Mara takes 6-204 in the same intake year and leaves the trade after refusing to close a "
              "repair. The rule that keeps repairmen working alone is written in this period and is "
              "quoted, in pieces, across chapters 2, 9 and 10."]),
            ("Chapters 1-3, the shop",
             ["An old man brings a chipped core and a scorched square of cloth. Three customers teach "
              "three rules: an engram holds a viewpoint, fill holds a memory together without returning "
              "its feeling, and a repairman is paid to stop the falling rather than to decide what a "
              "customer should keep. A fatal signature from years earlier surfaces at the end of the act."]),
            ("Chapters 4-9, the trade",
             ["The story widens from the bench to the system: a woman who kept receipts for memories "
              "she had paid to have removed, a blue door that turns out not to be a place, a family "
              "asking for a man who is factually intact and emotionally gone, a same-day clinic with a "
              "different vocabulary, an engram with two lives braided into one moment. Mara returns as "
              "a client in chapter 9 and the rule sheet gets its second hand."]),
            ("Chapters 10-12, the witness",
             ["The sealed core is opened with two people at the loom, and for the first time the fill "
              "comes from a witness rather than a machine. Chapter 12 is the old man's last repair: "
              "the seam is left open, the sound is not recovered, and the client's account is written "
              "into the core instead of being filled over."]),
            ("Chapters 13-16, the review",
             ["Ten days after the open repair, a wet-stamped letter arrives. The archive's sealed core "
              "turns out to contain a room Elias has never stood in and a signature in his hand dated "
              "before the letter. Ilse Renn, depositions, admits she signed the file twice. The shop "
              "keeps working through all of it: a staircase, a widow's laugh, a courier with a parcel "
              "of fill stamped by a supplier nobody recognises."]),
            ("Chapters 17-20, the joint",
             ["Inspector Ader repairs his own doubt before he writes his finding. The fill warehouse "
              "shows donor forms with four hundred hours of a stranger's childhood and an empty second "
              "signature box. The hearing keeps licence 4-119, conditioned: dual-account repairs, joint "
              "named before the loom, second licence holder present. The sign goes back up on a Sunday "
              "and the rule sheet gets its fifth line."]),
        ],
    },
    "who-is-who": {
        "title": "Who is who",
        "description": "The people of The Memory Repairman: a repairman, a witness, an archive clerk, "
                       "an inspector, and the customers who keep the shop open.",
        "lede": "Six entries, no spoilers past chapter 4. Names in the Ward are mostly licence numbers, "
                "so the numbers are given where the story gives them.",
        "sections": [
            ("Elias Vane — licence 4-119",
             ["A repairman on Cinder Lane, eleven years at the bench. He is good at the work and "
              "increasingly unsure whether the work is kind. His method is physical and unhurried: he "
              "seats the core, runs the scene to the last intact frame, and decides what to leave "
              "uncorrected before he touches the console."]),
            ("Mara — licence 6-204",
             ["A repairman who left the trade after refusing to close a repair, and who returns first as "
              "a client and then as the second signature on Elias's rule sheet. She sets the lamp at the "
              "end of the bench rather than beside it, which is the detail that tells you she learned "
              "the work somewhere else first."]),
            ("Ilse Renn — depositions, ninth floor",
             ["The archive clerk who signed one contested file twice: once as depositor, once as "
              "reviewer. Her argument is procedural and, in the story's terms, unanswerable — a record "
              "with one signature closes in nine days and is never read again."]),
            ("Inspector Ader",
             ["The auditor assigned to licence 4-119. He arrives with his own loom in two cases, repairs "
              "his own doubt about whether the review is fair, and shows the reviewed party the log, "
              "because the manual says he may and nobody reads that section."]),
            ("The old man",
             ["The client of chapters 1 and 12. He comes in with an engram, a folded square of cloth and "
              "coins in a row, and he is the first person in the book to ask for a story rather than a "
              "repair. His wife's kitchen is the memory the whole trade gets measured against."]),
            ("The customers",
             ["A boy with a staircase he is afraid to climb, a widow who wants her husband's laugh "
              "removed, a woman who kept receipts, a family asking for a man who is factually intact. "
              "None of them are cases. Each of them is a rule the trade has not written down yet."]),
        ],
    },
    "reading-guide": {
        "title": "Reading guide",
        "description": "Where to start, how long each chapter takes, and which chapters carry the "
                       "argument — a spoiler-light guide to The Memory Repairman.",
        "lede": "The book is one hundred chapters in thirteen parts: twenty narrative chapters, then eighty "
                "dated ledger entries written from a bench. The early chapters run six to eight minutes; the "
                "ledger entries run two to three. "
                "This page is for readers deciding where to begin and for anyone returning after a gap.",
        "sections": [
            ("If you have ten minutes",
             ["Read chapter 1, The Shop on Cinder Lane. It is self-contained, it introduces the trade, "
              "and it contains the image — a scorched square of cloth against a repaired memory — that "
              "the rest of the book keeps returning to."]),
            ("If you want the argument",
             ["Chapters 10 to 12 and 19 to 20 carry the trade's central dispute: whether a repair should "
              "close, and what it costs when it does. A reader who only wants the ideas can start at "
              "chapter 10, The Rule, Written Down, and finish at chapter 20, The Joint, in Writing."]),
            ("If you are returning after a gap",
             ["Part IV opens a new thread (an audit of the repair in chapter 12) and does not require the "
              "middle chapters. The timeline page lists every dated beat in order, and the glossary "
              "explains the trade's terms of art: engram, the Loom, fill, the Grey, the Ward."]),
            ("What the chapters are not",
             ["There are no puzzles and no hidden chronology. The story is linear, told from one bench, "
              "and the only thing the reader has to hold is the difference between what a machine "
              "records and what a person can still say."]),
        ],
    },
    "season-two": {
        "title": "Season two, in numbers",
        "description": "What the 2026 expansion added to The Memory Repairman: eight chapters, two acts, "
                       "four glossary terms, and the audit thread that carries the argument forward.",
        "lede": "The book was twelve chapters when it launched. Eight chapters were added in November "
                "2026, taking it to twenty and opening the trade's paperwork as a second subject.",
        "sections": [
            ("What was added",
             ["Chapters 13 to 20, in two new parts: Part IV · The Review (13-16) and Part V · The Joint "
              "(17-20). The existing three parts were left as they were, so the book now reads as five "
              "movements rather than three.",
              "Four glossary entries — the Ward, the Audit, the Joint, Donor Form — and this set of "
              "companion pages: timeline, who is who, reading guide, and this note."]),
            ("Why the expansion goes where it goes",
             ["The first twelve chapters end with an open seam and a question the shop cannot answer on "
              "its own: what a record is for. Season two takes that question to the people who keep "
              "records — an archive clerk, an inspector, a warehouse, a hearing room — and brings it back "
              "to the bench with a rule that can be written before a repair instead of after it."]),
            ("Length and pace",
             ["Each new chapter runs between 760 and 920 words, in the same register as the first twelve: "
              "one bench, physical detail, dialogue that does not explain itself. The season is written "
              "to be read in three or four sittings, and every chapter is legible on its own."]),
        ],
    },
    "season-three": {
        "title": "Season three: one hundred chapters",
        "description": "The Memory Repairman, expanded from twenty chapters to one hundred in thirteen "
                       "parts, with the back half written as dated ledger entries rather than scenes.",
        "lede": "On 2026-11-26 the book became one hundred chapters. The first twenty are scenes. The "
                "last eighty are entries: dated pages in the shop's own ledger, two to three minutes "
                "each, in the voice of the man writing them down at the end of a day.",
        "sections": [
            ("What the change is",
             ["Chapters 21 to 100 continue the story without changing its mode of address. Nothing is "
              "restaged and nothing is re-explained: the ledger picks up the week after the joint is "
              "written down and carries the trade from one bench to a district, an office, a warehouse, "
              "and back.",
              "Eight new parts were added — Part VI · The Dual Signature through Part XIII · The Last "
              "Entry — so the book now runs in thirteen movements of about eight to ten chapters."]),
            ("How to read the ledger half",
             ["Every entry opens with a number and a date, and most of them are short. Read them as a "
              "sequence of afternoons rather than as chapters with a cliffhanger: the shape is cumulative, "
              "and the recurring object is the record itself — what a shop writes down, what it leaves "
              "out, and who is allowed to read it later."]),
            ("What has not changed",
             ["One bench, one district, the same five terms of art, and the same refusal to explain the "
              "trade to the reader. The four-language editions carry the same one hundred chapters, "
              "translated from the English source and recorded with the same approval fields."]),
            ("Where it stops",
             ["Entry 100 is the last page and it is a page about the page. The shop is still open at the "
              "end, which is the only ending the trade allows: a decision, a date, two signatures, and "
              "whatever was left standing."]),
        ],
    },
}

ORDER = ["timeline", "who-is-who", "reading-guide", "season-two", "season-three"]
