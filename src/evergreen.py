# -*- coding: utf-8 -*-
"""evergreen.py — 常青配套内容（世界观 / 人物 / 主题 / FAQ），四语。

这些页面是编辑性内容，派生自 world-bible.md 与 outline，不属章节，
因此不走章节的 human-review 闸门；AI 辅助披露由页面骨架统一呈现。
每页结构：{"title":..., "desc":..., "blocks":[(heading, [paragraphs]), ...]}
paragraph 中以 **粗体** 标记，由 generate.md_inline 渲染。
"""
from __future__ import annotations

# 页面 slug 与导航标题（各语）
PAGES = {
    "world": {"en": "The World", "tr": "Dünya", "yue": "故事世界", "ko": "세계"},
    "characters": {"en": "Characters", "tr": "Karakterler", "yue": "人物", "ko": "등장인물"},
    "themes": {"en": "Themes & Motifs", "tr": "Temalar ve Simgeler", "yue": "主題與意象", "ko": "주제와 모티프"},
    "faq": {"en": "FAQ", "tr": "SSS", "yue": "常見問題", "ko": "자주 묻는 질문"},
}

TITLES = {
    "world": {
        "en": "The World of The Memory Repairman",
        "tr": "Hafıza Tamircisi'nin Dünyası",
        "yue": "《記憶修補師》嘅世界",
        "ko": "『기억 수리공』의 세계",
    },
    "characters": {
        "en": "Characters",
        "tr": "Karakterler",
        "yue": "人物",
        "ko": "등장인물",
    },
    "themes": {
        "en": "Themes & Motifs",
        "tr": "Temalar ve Simgeler",
        "yue": "主題同意象",
        "ko": "주제와 모티프",
    },
    "faq": {
        "en": "Frequently Asked Questions",
        "tr": "Sıkça Sorulan Sorular",
        "yue": "常見問題",
        "ko": "자주 묻는 질문",
    },
}

DESCRIPTIONS = {
    "world": {
        "en": "How engrams, the Loom, synthetic fill and the grey work in The Memory Repairman.",
        "tr": "Hafıza Tamircisi'nde engram, Tezgâh, sentetik dolgu ve grinin nasıl işlediği.",
        "yue": "《記憶修補師》入面記憶核、織機、合成填料同灰化係點運作。",
        "ko": "『기억 수리공』에서 엔그램, 직조기, 합성 충전재, 회색화가 어떻게 작동하는지.",
    },
    "characters": {
        "en": "Elias Vane, Mara, Halloway and the people who come to have their memories repaired.",
        "tr": "Elias Vane, Mara, Halloway ve anılarını onartmaya gelenler.",
        "yue": "Elias Vane、Mara、Halloway，同埋嚟修補記憶嘅人。",
        "ko": "엘리아스 베인, 마라, 할로웨이와 기억을 고치러 오는 사람들.",
    },
    "themes": {
        "en": "Facts versus feeling, the ethics of erasing, and the recurring blue door and rain.",
        "tr": "Olgulara karşı duygu, silmenin etiği ve tekrar eden mavi kapı ile yağmur.",
        "yue": "事實對感覺、抹走記憶嘅倫理，同埋不斷出現嘅藍門同雨。",
        "ko": "사실 대 감정, 망각의 윤리, 그리고 반복되는 파란 문과 비.",
    },
    "faq": {
        "en": "About the story, its languages, its AI-assisted authorship and how it was published.",
        "tr": "Öykü, dilleri, yapay zekâ destekli yazarlığı ve yayınlanma biçimi hakkında.",
        "yue": "關於故事、語言、AI 輔助創作同出版方式。",
        "ko": "이야기, 언어, AI 지원 집필과 출판 방식에 관하여.",
    },
}

CONTENT = {
    "en": {
        "world": [
            ("Engrams", [
                "An **engram** is a portable recording of a single recollection. It is lossy: damaged parts cannot be recovered, only bridged. People carry them in cases and sleeves the way they once carried photographs.",
                "A repair does not restore. It fills the gaps with **synthetic connective tissue** — plausible, stable, emotionally inert. The facts survive; the feeling does not.",
            ]),
            ("The Loom", [
                "The **Loom** is a table-sized machine that renders an engram as a structure a repairman can work inside, the way a conservator works on a fresco. Every repair leaves a seam.",
                "Elias works on an old, unlicensed loom assembled from parts that were legal in another decade. A serial number beneath its casing ties it to the first commercial machines.",
            ]),
            ("The Grey", [
                "Heavy repair produces **the grey**: a person whose facts are intact and whose feelings are gone. There is no clinical name for it, because the companies that sell repair have no interest in naming it.",
                "The industry slogan promises, *\"We give you back what happened.\"* Repairmen know the truth: *\"We give you back the shape of what happened.\"*",
            ]),
            ("The Ward", [
                "The story is set in the Ward, in a worn, bureaucratic near future — no neon spectacle, just rain, metal awnings and clinics painted a reassuring blue.",
            ]),
        ],
        "characters": [
            ("Elias Vane", [
                "Late fifties, once a memory architect — one of the engineers who designed the first commercial looms. He left after an incident he never discusses and now runs an unlicensed shop on Cinder Lane.",
                "His rule: he does not repair his own engrams. The story is about what that rule cost him, and how he finally rewrites it.",
            ]),
            ("Mara", [
                "Elias's former mentor. In the room when his memory was erased, she carries the other half of the truth. She returns not as a ghost but as a client, and finally as a witness.",
            ]),
            ("Halloway", [
                "Elias's former partner, now running the licensed clinic. He made repair affordable and asks Elias to trade silence for a room of his own.",
            ]),
            ("The clients", [
                "The woman with the receipts who wants feeling put back; the boy with the blue door; the family whose grey father is factually intact; the old man who keeps asking for his wife to be fixed.",
            ]),
        ],
        "themes": [
            ("Facts versus feeling", [
                "The central question: what makes a memory *yours* — the facts, or the feeling? The story keeps returning to the line, *\"You can save the facts, you can't save the feeling.\"*",
            ]),
            ("The ethics of helping", [
                "Is a comfortable lie kinder than a painful truth? The repair trade sells relief by erasing, and every client chooses that bargain willingly — including Elias.",
            ]),
            ("Recurring motifs", [
                "The smell of rain on hot metal; a **blue door** that appears in more than one memory; the phrase about facts and feeling. Each returns at a turning point rather than as decoration.",
            ]),
            ("Witness over isolation", [
                "The answer the story arrives at is not a better machine but a second person: a repair done in the presence of someone named on the page, with a seam that holds because it is shared.",
            ]),
        ],
        "faq": [
            ("What is this?", [
                "A near-future science-fiction short story in twelve chapters, published under the byline apprank studio. It is a work of fiction.",
            ]),
            ("Which languages?", [
                "The complete story is available in English, Turkish, Cantonese and Korean. Chapters appear after their own review; the full disclosure is on the About page.",
            ]),
            ("Was it written by a human?", [
                "The English chapters were drafted with AI assistance and reviewed. Translations are AI-assisted and reviewed separately. No fabricated author biography or portrait is used — see the About page for the full disclosure.",
            ]),
            ("Is it free?", [
                "Yes. No account, no paywall, no tracking. The source and method are open.",
            ]),
        ],
    },
    "tr": {
        "world": [
            ("Engramlar", [
                "**Engram**, tek bir anının taşınabilir kaydıdır. Kayıplıdır: hasarlı parçalar geri getirilemez, yalnızca köprülenir. İnsanlar onları eskiden fotoğraf taşıdıkları gibi kutu ve kılıflarda taşır.",
                "Onarım, geri getirme değildir. Boşluklar **sentetik bağ dokusuyla** doldurulur: inandırıcı, kararlı, duygusuz. Olgular hayatta kalır; duygu kalmaz.",
            ]),
            ("Tezgâh", [
                "**Tezgâh**, bir engram'ı tamircinin içinde çalışabileceği bir yapıya dönüştüren masa büyüklüğünde bir makinedir; bir konservatörün fresk üzerinde çalışması gibi. Her onarım bir dikiş bırakır.",
                "Elias, bir başka on yılda yasal parçalardan yapılmış eski, lisanssız bir tezgâh kullanır. Kasa altındaki seri numarası onu ilk ticari makinelere bağlar.",
            ]),
            ("Grinin", [
                "Yoğun onarım **griyi** doğurur: olguları sağlam, duyguları gitmiş bir insan. Bunun klinik bir adı yoktur, çünkü onarım satan şirketlerin ona ad vermeye ilgisi yoktur.",
                "Sektörün sloganı, *\"Size olanı geri veriyoruz\"* der. Tamircilerin bildiği gerçek ise: *\"Size olanın şeklini geri veriyoruz.\"*",
            ]),
            ("Ward", [
                "Hikâye, Ward'da, yıpranmış ve bürokratik bir yakın gelecekte geçer — neon gösterişi yok, sadece yağmur, metal tenteler ve güven veren maviye boyanmış klinikler.",
            ]),
        ],
        "characters": [
            ("Elias Vane", [
                "Elli li yıllarının sonunda, bir zamanlar hafıza mimarı — ilk ticari tezgâhları tasarlayan mühendislerden biri. Asla konuşmadığı bir olaydan sonra ayrıldı ve şimdi Cinder Lane'de lisanssız bir dükkân işletiyor.",
                "Kuralı: kendi engram'ını onarmaz. Hikâye, bu kuralın ona neye mal olduğunu ve onu sonunda nasıl yeniden yazdığını anlatır.",
            ]),
            ("Mara", [
                "Elias'ın eski mentoru. Anısı silindiğinde odadaydı ve gerçeğin diğer yarısını taşır. Bir hayalet olarak değil, bir müşteri olarak, sonunda da bir şahit olarak döner.",
            ]),
            ("Halloway", [
                "Elias'ın eski ortağı, şimdi lisanslı kliniği yönetiyor. Onarımı erişilebilir kıldı ve Elias'tan sessizlik karşılığında kendi odasını teklif etti.",
            ]),
            ("Müşteriler", [
                "Duyguyu geri koymak isteyen makbuzlu kadın; mavi kapılı çocuk; olgular bakımından sağlam olan gri babanın ailesi; karısını bir kez daha onartmak isteyen yaşlı adam.",
            ]),
        ],
        "themes": [
            ("Olgulara karşı duygu", [
                "Merkezî soru: bir anıyı *senin* yapan nedir — olgular mı, duygu mu? Hikâye sürekli şu cümleye döner: *\"Olguları kurtarabilirsin, duyguyu kurtaramazsın.\"*",
            ]),
            ("Yardımın etiği", [
                "Rahat bir yalan, acı gerçekten daha mı nazik? Onarım sektörü silerek rahatlama satar ve her müşteri bu pazarlığı gönüllü yapar — Elias da dahil.",
            ]),
            ("Yinelenen simgeler", [
                "Yağmurun sıcak metaldeki kokusu; birden fazla anıda görünen **mavi kapı**; olgular ve duygu üzerine söz. Her biri süs değil, bir dönüm noktasında geri döner.",
            ]),
            ("Yalnızlığa karşı şahit", [
                "Hikâyenin vardığı cevap daha iyi bir makine değil, ikinci bir insandır: kâğıtta adı yazılı birinin huzurunda yapılan ve paylaşıldığı için tutan bir dikişle onarım.",
            ]),
        ],
        "faq": [
            ("Bu nedir?", [
                "apprank studio adıyla yayımlanmış, on iki bölümlük bir yakın gelecek bilimkurgu öyküsü. Bir kurgu eseridir.",
            ]),
            ("Hangi dillerde?", [
                "Öykü tamamen İngilizce, Türkçe, Kantonca ve Korece olarak mevcuttur. Bölümler kendi incelemelerinden sonra yayınlanır; tam açıklama Hakkında sayfasındadır.",
            ]),
            ("İnsan tarafından yazıldı mı?", [
                "İngilizce bölümler yapay zekâ desteğiyle taslaklandı ve incelendi. Çeviriler yapay zekâ desteklidir ve ayrıca incelenir. Uydurma yazar biyografisi veya portresi kullanılmaz — ayrıntılı açıklama Hakkında sayfasındadır.",
            ]),
            ("Ücretsiz mi?", [
                "Evet. Hesap yok, ödüvar yok, takip yok. Kaynak ve yöntem açıktır.",
            ]),
        ],
    },
    "yue": {
        "world": [
            ("記憶核", [
                "**記憶核**係一段回憶嘅可攜式紀錄。佢係有損嘅：受損部分救唔返，只可以搭橋。人哋用盒同套帶住佢，好似以前帶相咁。",
                "修補唔係還原。佢用**合成填料**補返啲空洞 —— 合理、穩定、冇感情。事實留得低，感覺留唔低。",
            ]),
            ("織機", [
                "**織機**係一部枱咁大嘅機器，將記憶核呈現成修補師可以喺入面工作嘅結構，好似文物修復師對住壁畫咁。每次修補都會留低一道接縫。",
                "Elias 用緊一部舊、冇牌嘅織機，由另一個年代仲合法嘅零件砌成。機殼下面個序列號將佢連到第一批商用機器。",
            ]),
            ("灰化", [
                "大量修補會造成**灰化**：一個人事實完整、感覺消失。呢個病冇臨床名稱，因為賣修補嘅公司冇興趣幫佢命名。",
                "行業口號話：*「我哋將發生過嘢還返畀你。」* 修補師知嘅真相係：*「我哋將發生過嘢嘅形還返畀你。」*",
            ]),
            ("Ward", [
                "故事喺 Ward 發生，一個殘舊、官僚嘅近未來 —— 冇霓虹特效，只有雨、金屬簷篷同埋漆成令人安心藍色嘅診所。",
            ]),
        ],
        "characters": [
            ("Elias Vane", [
                "五十幾歲，曾經係記憶架構師 —— 設計第一批商用織機嘅工程師之一。佢喺一件從來唔講嘅事故之後離開，而家喺 Cinder Lane 開一間冇牌嘅鋪。",
                "佢條規矩：唔修補自己嘅記憶核。故事講嘅係呢條規矩令佢付出咗咩代價，同埋佢點樣最終改寫佢。",
            ]),
            ("Mara", [
                "Elias 昔日嘅導師。佢記憶被抹走時佢喺房入面，揹住真相嘅另一半。佢唔係以幽靈身份返嚟，而係以客人身份，最後以證人身份。",
            ]),
            ("Halloway", [
                "Elias 昔日嘅合伙人，而家打理持牌診所。佢令修補變得人人負擔得起，並提出用沉默換一間屬於自己嘅房。",
            ]),
            ("客人哋", [
                "想放回感覺嘅收據女人；有藍門嘅後生仔；灰化但事實完整嘅阿爸嘅家人；想再修一次太太嘅老伯。",
            ]),
        ],
        "themes": [
            ("事實對感覺", [
                "核心問題：係咩令一段記憶成為*你嘅* —— 事實，定係感覺？故事不斷回到呢句：*「你可以救返啲事實，你救唔返嗰種感覺。」*",
            ]),
            ("幫人嘅倫理", [
                "舒服嘅謊話係咪比痛苦嘅真相更善良？修補行業靠抹走嘢賣解脫，每個客都自願做呢筆交易 —— Elias 都係。",
            ]),
            ("重複意象", [
                "雨打熱金屬嘅味；喺多過一段記憶出現嘅**藍門**；關於事實同感覺嘅說話。每一樣都唔係裝飾，而係喺轉折點返嚟。",
            ]),
            ("證人勝過孤獨", [
                "故事最後嘅答案唔係一部更好嘅機器，而係第二個人：喺一個名寫喺紙上嘅人面前做、因為分享而掯得住嘅接縫嘅修補。",
            ]),
        ],
        "faq": [
            ("呢個係咩？", [
                "一部十二章嘅近未來科幻短篇，以 apprank studio 署名出版。係虛構作品。",
            ]),
            ("有咩語言？", [
                "完整故事有英文、土耳其文、粵文同韓文。章節要各自審校先會上架；完整說明喺「關於」頁。",
            ]),
            ("係咪人寫嘅？", [
                "英文章節由 AI 協助起草同審校。譯文由 AI 協助並獨立審校。我哋唔會虛構作者履歷或者頭像 ——  完整說明喺「關於」頁。",
            ]),
            ("係咪免費？", [
                "係。冇帳號、冇付費牆、冇追蹤。源碼同方法都係公開。",
            ]),
        ],
    },
    "ko": {
        "world": [
            ("엔그램", [
                "**엔그램**은 하나의 회상을 담은 휴대용 기록입니다. 손실이 있어 손상된 부분은 되찾을 수 없고 다리만 놓을 수 있습니다. 사람들은 예전에 사진을 들듯 케이스와 슬리브에 넣어 들고 다닙니다.",
                "수리는 복원이 아닙니다. 빈 곳을 **합성 충전재**로 메웁니다. 그럴듯하고 안정적이지만 감정이 없습니다. 사실은 남고 감정은 사라집니다.",
            ]),
            ("직조기", [
                "**직조기**는 엔그램을 수리공이 그 안에서 작업할 수 있는 구조로 펼치는 탁자 크기의 기계입니다. 보존사가 프레스코를 다루듯합니다. 모든 수리는 봉합을 남깁니다.",
                "엘리아스는 다른 십 년 전에는 합법이었던 부품으로 만든 낡고 무면허인 직조기를 씁니다. 케이스 아래의 일련번호가 그것을 최초의 상업용 기계와 연결합니다.",
            ]),
            ("회색화", [
                "대대적인 수리는 **회색화**를 낳습니다. 사실은 온전하지만 감정은 사라진 사람입니다. 임상적 이름이 없는데, 수리를 파는 회사들이 이름 붙일 이유가 없기 때문입니다.",
                "업계 구호는 *\"일어난 일을 되돌려 드립니다\"* 라고 합니다. 수리공이 아는 진실은 이렇습니다. *\"일어난 일의 형태를 되돌려 드립니다.\"*",
            ]),
            ("워드", [
                "이야기는 닳고 관료적인 근미래의 워드를 배경으로 합니다. 네온 과시가 아니라, 비와 금속 차양, 안심되는 파란색으로 칠해진 진료소가 있을 뿐입니다.",
            ]),
        ],
        "characters": [
            ("엘리아스 베인", [
                "오십 대 후반. 한때 기억 설계자, 최초의 상업용 직조기를 설계한 기술자 중 한 명. 결코 말하지 않는 사건 뒤에 떠나 지금은 신더 레인에서 무면허 가게를 엽니다.",
                "그의 규칙: 자기 엔그램은 수리하지 않는다. 이야기는 그 규칙이 그에게 무엇을 빼앗았는지, 그리고 어떻게 마침내 다시 쓰는지를 다룹니다.",
            ]),
            ("마라", [
                "엘리아스의 옛 멘토. 그의 기억이 지워질 때 방 안에 있었고 진실의 다른 절반을 지고 있습니다. 유령이 아니라 고객으로, 마지막에는 증인으로 돌아옵니다.",
            ]),
            ("할로웨이", [
                "엘리아스의 옛 동료이자 지금은 면허 진료소를 운영합니다. 수리를 누구나 감당할 수 있게 만들었고, 침묵과 맞바꾸어 자기 방을 제안합니다.",
            ]),
            ("고객들", [
                "감정을 되돌려 달라는 영수증 든 여자, 파란 문이 있는 소년, 사실은 온전한 회색화된 아버지의 가족, 아내를 한 번 더 고쳐 달라는 늙은 남자.",
            ]),
        ],
        "themes": [
            ("사실 대 감정", [
                "중심 질문: 어떤 회상을 *당신의 것*으로 만드는 것은 사실인가, 감정인가? 이야기는 계속 이 문장으로 돌아갑니다. *\"사실은 살릴 수 있어도 감정은 살릴 수 없다.\"*",
            ]),
            ("돕기의 윤리", [
                "편안한 거짓말이 고통스러운 진실보다 친절한가? 수리업은 지움으로써 안도를 팔고, 모든 고객이 자발적으로 그 거래를 한다 — 엘리아스도 포함해.",
            ]),
            ("되풀이되는 모티프", [
                "뜨거운 금속에 내리는 비 냄새, 한 번 이상의 기억에 나타나는 **파란 문**, 사실과 감정에 관한 말. 각각 장식이 아니라 전환점에서 돌아옵니다.",
            ]),
            ("고립보다 증인", [
                "이야기가 도달한 답은 더 나은 기계가 아니라 두 번째 사람입니다. 종이에 이름이 적힌 사람 곁에서 이루어지고, 나누었기에 버티는 봉합의 수리.",
            ]),
        ],
        "faq": [
            ("이건 무엇인가요?", [
                "apprank studio 이름으로 출판된 열두 장의 근미래 공상과학 단편입니다. 허구의 작품입니다.",
            ]),
            ("어떤 언어로 있나요?", [
                "전체 이야기가 영어, 터키어, 광둥어, 한국어로 있습니다. 각 장은 자체 검토를 거쳐 게시되며, 전체 공개 안내는 소개 페이지에 있습니다.",
            ]),
            ("사람이 썼나요?", [
                "영어 원고는 AI 도움으로 초안을 쓰고 검토했습니다. 번역도 AI 도움을 받아 별도로 검토됩니다. 허구의 작가 약력이나 초상은 쓰지 않습니다 — 자세한 내용은 소개 페이지에 있습니다.",
            ]),
            ("무료인가요?", [
                "네. 계정도, 유료벽도, 추적도 없습니다. 출처와 방법은 공개되어 있습니다.",
            ]),
        ],
    },
}
