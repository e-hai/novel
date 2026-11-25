# -*- coding: utf-8 -*-
"""设定词条（英文）——把世界观里反复出现的名词做成可检索的独立页面。

每页 300 词以上、只讲设定本身（不剧透结局），并在页尾指向相关章节与相关词条。
这些页面是小说站的主要长尾入口：读者搜的是"engram 是什么""memory repair 怎么做"，
而不是"best sci-fi story"。
"""

PAGES = {
    "engram": {
        "term": "Engram",
        "short": "A portable, editable recording of a single memory — lossy by design.",
        "lede": "An engram is the Ward's unit of memory: a palm-sized core that holds one "
                "person's recollection as a structure that can be opened, examined and edited. "
                "It is not a backup. It is a copy that has already lost something.",
        "sections": [
            ("What an engram actually stores",
             ["An engram records the shape of an experience rather than its content. What survives "
              "the transfer is sequence, weight and the feeling of a room — the order in which things "
              "happened, which details pressed hardest, where the light came from. What does not survive "
              "is everything the rememberer did not notice at the time.",
              "This is why two engrams of the same afternoon can disagree without either being false. "
              "The core preserves a viewpoint, not an event. Repairmen learn early that the question "
              "\"is this accurate?\" cannot be answered from inside a single engram; it can only be "
              "answered by comparing it with someone else's."]),
            ("Damage, and what damage looks like",
             ["An engram fails in recognizable ways. A chipped rim produces a memory that stops mid-scene, "
              "like a room with one wall missing. A cracked core repeats a single moment on a loop, and the "
              "person carrying it experiences the repetition as dread without knowing why. A core that has "
              "been repaired badly does not fail at all: it holds together, and that is the problem.",
              "In the shop on Cinder Lane, the first thing a repairman does is not open the core. It is to ask "
              "what the customer remembers without it. The gap between the two answers is the actual work."]),
            ("Why the Ward treats engrams as property",
             ["Engrams are stored, insured and inherited. A family can own a dead relative's engram the way "
              "another family owns a house, and the law treats a damaged core as damaged property rather than "
              "a damaged person. That legal fiction is the quiet engine of the story: it lets everyone behave "
              "as though a memory is an object, right up until someone has to live inside one."]),
        ],
        "see": ["the-loom", "fill"],
        "chapters": ["01-the-shop-on-cinder-lane", "05-a-blue-door-in-someone-elses-memory"],
    },
    "the-loom": {
        "term": "The Loom",
        "short": "The table-sized apparatus that renders an engram as a space a repairman can walk into.",
        "lede": "The Loom is the machine at the centre of the trade. It does not repair anything by itself. "
                "It converts an engram into a place — a room, a street, a version of an afternoon — that a "
                "repairman can enter and work inside.",
        "sections": [
            ("How the Loom renders a memory",
             ["The core is mounted, the frame is threaded, and the engram is projected as architecture. "
              "Walls appear where the rememberer felt resistance. Doors appear where the rememberer expected "
              "a choice. Weather is not decoration: it is the emotional pressure of the original moment, "
              "rendered as temperature and light.",
              "A repairman reads the room the way a builder reads a wall — for seams. Anything that looks too "
              "smooth is usually where someone has already been."]),
            ("The craft, and its limits",
             ["Working inside a rendered memory is slow and physical. You cannot edit a feeling directly. You "
              "can move furniture, change the direction a conversation takes, remove a person from a room. "
              "The memory then re-settles around the change, and the rememberer experiences the new version as "
              "what happened.",
              "The Loom can hold a scene steady for hours. It cannot tell you whether the scene is worth "
              "keeping. That judgement stays with the person paying for the repair, which is exactly why the "
              "trade has a reputation it does not entirely deserve."]),
            ("Why a machine, and not a therapy",
             ["The Ward chose hardware over counselling for Reasons of cost, insurance and speed. A session at "
              "the Loom is billed by the hour, not by the year. The result is a society that can fix the shape "
              "of a memory in an afternoon and has no idea what to do with the person afterwards — a gap the "
              "story keeps returning to."]),
        ],
        "see": ["engram", "fill", "the-grey"],
        "chapters": ["01-the-shop-on-cinder-lane", "11-two-at-the-loom"],
    },
    "fill": {
        "term": "Fill",
        "short": "Synthetic connective tissue keyed into a damaged engram: plausible, stable, emotionally inert.",
        "lede": "Fill is what a repairman inserts where a memory has torn. It is not a replacement and it is "
                "not a lie exactly — it is a plausible bridge, designed so the rememberer stops falling through "
                "the gap.",
        "sections": [
            ("What fill is made of",
             ["Fill is manufactured in sheets and keyed in by hand. It carries no content of its own; it "
              "carries structure — the expectation that a hallway leads somewhere, that a conversation has a "
              "second half, that a person who was standing there is still standing there.",
              "Good fill is invisible. Bad fill announces itself as politeness: a scene that is too calm, a "
              "sentence that arrives too neatly. Customers rarely notice. Repairmen always do."]),
            ("The emotional ceiling",
             ["Fill can hold a memory together. It cannot supply feeling. A repaired engram reads as true and "
              "feels like a report. This is the trade's open secret and its main selling point: the customer "
              "gets the fact back, and the fact is what they asked for.",
              "The Grey is what happens when enough fill is used that the whole engram starts to read that way. "
              "The customer is intact, competent, and slightly elsewhere."]),
            ("The ethics nobody writes down",
             ["There is no rule against fill. There is only a rule against telling the customer how much of "
              "their memory is now bridge. Every repairman develops a personal threshold — a number of sheets "
              "past which they will say something — and most of them set that threshold higher than they would "
              "admit."]),
        ],
        "see": ["the-grey", "engram"],
        "chapters": ["02-a-client-without-a-face", "06-what-the-grey-remember"],
    },
    "the-grey": {
        "term": "The Grey",
        "short": "The flatness left by heavy repair: facts intact, feeling gone.",
        "lede": "The Grey is not a place and not exactly a condition. It is the texture a person's memory "
                "acquires after enough repair — accurate, orderly, and quiet in a way that frightens the people "
                "who love them.",
        "sections": [
            ("How it presents",
             ["Someone in the Grey can tell you what happened. They can give you the date, the room, the order "
              "of events, sometimes the exact words. What they cannot give you is the temperature of it: whether "
              "it was funny, whether it hurt, whether they would do it again.",
              "Families describe the same experience repeatedly: the person is fine, and the person is not there. "
              "The Grey does not look like damage from the outside. It looks like composure."]),
            ("Why repairmen fear it",
             ["Every repair moves a customer a little closer to it, and no repairman can say how close a given "
              "customer already is. The trade has no unit for it. There is no test. There is only the moment a "
              "customer describes a memory they should be angry about in a level voice, and the repairman "
              "decides whether to mention it.",
              "In the Ward, the Grey is treated as an occupational hazard of being helped — which is a polite "
              "way of saying the cost is paid by the person who needed the repair, not by the person who "
              "performed it."]),
            ("The name",
             ["The name is not clinical. It came from customers, who kept reaching for the same word: grey. "
              "Not dark. Not blank. Grey, like a photograph of a photograph."]),
        ],
        "see": ["fill", "the-loom"],
        "chapters": ["06-what-the-grey-remember", "04-the-woman-who-kept-receipts"],
    },
    "memory-architect": {
        "term": "Memory architect",
        "short": "The engineers who designed the first commercial looms — and knew what the fill would do.",
        "lede": "Memory architects are the small, unglamorous profession standing behind the trade: the people "
                "who designed the first commercial looms, wrote the fill specifications, and set the tolerances "
                "that decide how much a memory can be changed before it stops counting as the same memory.",
        "sections": [
            ("What they designed",
             ["A memory architect does not repair memories. They design the machine that does, and the sheets "
              "that make the repair hold. Their decisions are abstract — a tolerance here, a rendering "
              "resolution there — and they land in the world as a policy about how much a person is allowed to "
              "forget without noticing.",
              "The first commercial looms were built to a specification that prioritized stability over fidelity, "
              "because unstable repairs generate complaints and faithful ones generate lawsuits. That single "
              "trade-off is the reason the Grey exists as a mass phenomenon rather than a rare complication."]),
            ("Why they are absent from the shop",
             ["Architects work for manufacturers, not for repairmen. The shop on Cinder Lane buys its fill from "
              "a supplier and has never met the person who specified it. This distance is deliberate: the trade "
              "can be blamed for individual repairs, and the specification that makes those repairs necessary "
              "stays out of reach.",
              "When a customer asks why the fill cannot carry feeling, the honest answer is that no one ever "
              "specified that it should."]),
            ("The professional silence",
             ["Architects do not publish. The Ward's trade press covers repair technique, not specification "
              "design, and the people who could explain the system have signed the kind of contracts that "
              "make explaining it expensive. The result is a profession that everyone depends on and no one "
              "can name — which is, in the story's terms, the most dangerous position in the Ward."]),
        ],
        "see": ["fill", "the-loom"],
        "chapters": ["08-the-engram-that-would-not-close", "10-the-rule-written-down"],
    },
}

ORDER = ["engram", "the-loom", "fill", "the-grey", "memory-architect"]
