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
    {
        "slug": "part-iv",
        "roman": "IV",
        "title": "Part IV · The Review",
        "range": (13, 16),
        "lede": "A wet-stamped letter arrives, and the shop keeps working while the Ward decides what a seam is.",
        "body": [
            "The fourth act is the audit. Elias is not suspended and not forgiven; he is reviewed, which turns out "
            "to be a slower and more thorough kind of pressure. A letter with a crooked seal, a sealed core that "
            "contains a room he has never stood in, and an archive clerk who signed the record twice because a file "
            "with one signature can be closed without anyone reading it — the act moves the story from the bench "
            "to the paperwork behind it.",
            "It is also where the trade keeps going. Three customers come through in a single day: a boy who wants a "
            "staircase removed, a widow who wants her husband's laugh taken out, a courier with a parcel of fill "
            "stamped by a supplier nobody recognises. None of them can wait for the review. By the end of the act "
            "the rule sheet has a fourth line, and the shop is still open, and that is the point: a review does not "
            "stop the work, it only changes what the work has to say about itself.",
        ],
    },
    {
        "slug": "part-v",
        "roman": "V",
        "title": "Part V · The Joint",
        "range": (17, 20),
        "lede": "An inspector repairs his own doubt, a warehouse sells childhood by the hour, and a hearing decides whether honesty is a defect.",
        "body": [
            "The last act is the argument. Inspector Ader brings his own loom into the shop and uses it on himself "
            "before he writes a finding — an auditor is allowed to repair his own doubt, provided the log is shown "
            "to the reviewed party. Then the supply chain opens: fill bought by the brick, donor forms with four "
            "hundred hours of a stranger's back garden and a second signature box left empty. The material turns out "
            "to be the same argument as the seam, moved upstream.",
            "The hearing is where the two threads meet. Three board members read the file aloud and cannot decide "
            "whether a seam is a defect or a category, until Mara puts her suspended licence on the table as the "
            "second signature the rule now requires. Licence 4-119 survives, conditioned: dual-account repairs, "
            "joint named before the loom. The shop puts its sign back up, and the last line of the rule sheet is "
            "written before the repair rather than after it.",
        ],
    },
    {
        "slug": "part-vi",
        "roman": "VI",
        "title": "Part VI · The Dual Signature",
        "range": (21, 30),
        "lede": "The rule is now two hands on every core, and the shop has to learn what a second signature is for.",
        "body": [
            "From chapter twenty-one the book changes its hand: after the hearing, Elias starts keeping the "
            "shop's log himself, and the log is what you read. Entries are dated, shorter than the chapters before "
            "them, and written at the end of the day by someone who has decided that the record is part of the "
            "repair rather than an admission about it.",
            "The first ten entries are the new rule in practice. Mara signs beside him, which is not the same as "
            "agreeing with him; two customers are refused because the second name will not go on the line; and the "
            "shop discovers that a joint signature done properly costs a day it cannot bill for.",
        ],
    },
    {
        "slug": "part-vii",
        "roman": "VII",
        "title": "Part VII · The Apprentice",
        "range": (31, 40),
        "lede": "Wren Adey comes to learn the trade, and the ledger acquires a second handwriting whether Elias likes it or not.",
        "body": [
            "A shop with two names on every repair needs someone to hold the second pen. Wren is nineteen, "
            "fast, and better with the Loom than Elias was at that age, which is its own kind of review.",
            "The apprentice chapters are the trade taught out loud: what a seam looks like before it is one, why "
            "fill has no taste, how to refuse a customer without making the refusal a repair. Halfway through the "
            "part, Wren makes an error that the joint rule catches, and the shop's first shared mistake is filed "
            "under both names.",
        ],
    },
    {
        "slug": "part-viii",
        "roman": "VIII",
        "title": "Part VIII · The Grey Spreads",
        "range": (41, 50),
        "lede": "The Grey stops being a condition of individual customers and becomes weather over a district.",
        "body": [
            "Ten entries, and the grey patches move out of the shop: a school corridor, a bus shelter, the "
            "waiting room of a clinic, a street that has been repaved twice and still photographs wrong.",
            "The Ward issues guidance instead of a diagnosis, which is what an institution does when it cannot "
            "afford to name a thing. Elias keeps repairing, and starts writing down the addresses, because a "
            "pattern is the only kind of evidence the trade is allowed to produce.",
        ],
    },
    {
        "slug": "part-ix",
        "roman": "IX",
        "title": "Part IX · The Warehouse",
        "range": (51, 60),
        "lede": "Fill is bought by the brick, and the shop finally meets the people who sell other people's afternoons.",
        "body": [
            "The supply chain opens in the middle of the book, the way a floor gives way in the middle of a room. "
            "A warehouse outside the ring road sells fill in weighed lots: four hundred hours of a stranger's back "
            "garden, a wedding nobody in the buyer's family attended, a summer that was donated twice.",
            "Elias goes there to buy nothing and comes back with a donor form that has two signature boxes, one "
            "of them empty, and the empty box is the whole argument of the following ten years compressed into a "
            "rectangle of paper.",
        ],
    },
    {
        "slug": "part-x",
        "roman": "X",
        "title": "Part X · The Loom, Twice",
        "range": (61, 70),
        "lede": "Dual-account repair becomes a technique rather than a rule, and the shop runs the Loom for two people at once.",
        "body": [
            "The Loom was built to hold one account. Running it twice is not twice the work; it is a different "
            "trade, with its own failures — beating, drift, and the specific silence of two memories that will "
            "not agree about a room they both remember.",
            "Mara and Elias run the first legal dual-account repair in the Ward, and it works, and neither of them "
            "can say afterwards which of the two memories was repaired. That question is not resolved in this "
            "part, or in the next one.",
        ],
    },
    {
        "slug": "part-xi",
        "roman": "XI",
        "title": "Part XI · The Audit of the Audit",
        "range": (71, 80),
        "lede": "Inspector Ader's own file is opened, and the shop is asked to review the man who reviewed it.",
        "body": [
            "An inspector who repairs his own doubt in order to write a finding has produced a document that "
            "cannot be audited by anyone who trusts documents. The board sends the file back to the shop, which is "
            "either an appeal or a joke depending on which paragraph you read first.",
            "Elias reads Ader's seams the way Ader read his, and the ledger records the uncomfortable symmetry: "
            "two men, one technique, and a Ward that has no procedure for a reviewer who is also a customer.",
        ],
    },
    {
        "slug": "part-xii",
        "roman": "XII",
        "title": "Part XII · The Testimony",
        "range": (81, 90),
        "lede": "Nine customers come back to say what the repair did, and the shop has to sit still and listen.",
        "body": [
            "The book turns the bench around: instead of customers bringing damage, the ledger records people "
            "returning to describe the years after a repair. A man who cannot remember his mother's voice and "
            "does not want to. A woman whose seam held and made her life smaller. A boy who asked for a staircase "
            "to be removed and now climbs it every day without knowing why.",
            "None of it is a complaint. That is the difficulty. The shop has kept its records honestly and the "
            "records say the trade works, and the testimony says something the records were never built to hold.",
        ],
    },
    {
        "slug": "part-xiii",
        "roman": "XIII",
        "title": "Part XIII · The Last Entry",
        "range": (91, 100),
        "lede": "Elias's own core goes on the bench, Wren holds the second pen, and the ledger gets a last page.",
        "body": [
            "The last ten entries close the book the way the trade closes a core: not with a repair but with a "
            "decision about what to leave standing. Elias's own memory — the one he has kept exactly where he left "
            "it for the whole book — is opened, read, and signed for by two people.",
            "What happens to the shop is not a twist. It is an entry with a date at the top, a second signature "
            "beside the first, and a line at the bottom that says the ledger is complete. The last page is the "
            "shortest in the book and the only one written in two hands.",
        ],
    },
]
