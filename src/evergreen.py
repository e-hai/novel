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
        "en": "Elias Vane, Mara, Wren Adey, Inspector Ader, Halloway and the people named on the register.",
        "tr": "Elias Vane, Mara, Wren Adey, Müfettiş Ader, Halloway ve sicile geçen insanlar.",
        "yue": "Elias Vane、Mara、Wren Adey、督察 Ader、Halloway，同埋名冊上嘅人。",
        "ko": "Elias Vane, Mara, Wren Adey, 조사관 Ader, Halloway와 명부 위의 사람들.",
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

CONTENT = {'en': {'world': [['Engrams',
                   ['An **engram** is a portable recording of a single recollection. It is lossy: damaged '
                    'parts cannot be recovered, only bridged. People carry them in cases and sleeves the way '
                    'they once carried photographs.',
                    'A repair does not restore. It fills the gaps with **synthetic connective tissue** — '
                    'plausible, stable, emotionally inert. The facts survive; the feeling does not.']],
                  ['The Loom',
                   ['The **Loom** is a table-sized machine that renders an engram as a structure a repairman '
                    'can work inside, the way a conservator works on a fresco. Every repair leaves a seam.',
                    'Elias works on an old, unlicensed loom assembled from parts that were legal in another '
                    'decade. Two people at the loom — one to hold, one to witness — is the whole of the '
                    "trade's ethics, written down late."]],
                  ['Fill and the warehouse',
                   ['Every repair spends **fill**, the synthetic tissue that bridges a gap. It is sold by '
                    'weight at a warehouse on the edge of the Ward, and the warehouse sells it by the brick: '
                    'four hours of work to a brick, no smaller unit.',
                    'The lots are numbered. In one summer the same lot was sold twice under two numbers, and '
                    'the paperwork that proved it surfaced only after a complaint. Fill is cheap; the record '
                    'of where it came from is not.']],
                  ['The Grey',
                   ['Repair at scale has made **the grey** a district-wide condition rather than a private '
                    "misfortune: two hundred and eleven addresses on the Ward's own register, and a name for "
                    'none of them.',
                    'The industry slogan promises, *"We give you back what happened."* Repairmen know the '
                    'truth: *"We give you back the shape of what happened."*']],
                  ['The Ward',
                   ["The Ward is the licensing authority and the weather. It issues licences like Mara's "
                    '4-119, keeps the register on which every legal repair carries two names, and sends '
                    'inspectors who write findings in triplicate.',
                    'Its offices are worn, bureaucratic and unremarkable: rain, metal awnings, clinics '
                    'painted a reassuring blue, and a depot where a clerk has kept the same notebook for six '
                    'years.']]],
        'characters': [['Elias Vane',
                        ['Late fifties, once a memory architect — one of the engineers who designed the '
                         'first commercial looms. He left after an incident he never discusses and now runs '
                         'an unlicensed shop on Cinder Lane.',
                         'His rule was that he does not repair his own engrams. From the first line of the '
                         'log he keeps himself, the rule is written where a second person can read it — '
                         'which is the only reason it ever changes.']],
                       ['Mara',
                        ["Elias's former mentor, and the other half of the truth about the day his memory "
                         'was erased. Her licence, 4-119, comes back on conditions: a dual signature, the '
                         'joint named before the work, two names on the books — and, from the seventy-ninth '
                         'chapter, a fourth: she may not repair her own account at the place where she is '
                         'the second signature.',
                         'She is not a ghost in this version of the story. She is the second pair of hands, '
                         'and the one who insists the seam be recorded.']],
                       ['Wren Adey',
                        ['Nineteen when she is hired, an apprentice who reads the ledger before she reads '
                         'the loom. She spends sixty-four chapters learning what a signature costs, and '
                         'gives her first one as an equal at the ninety-fifth.']],
                       ['Inspector Ader',
                        ["The auditor who checks his own doubt instead of the shop's paperwork, and writes "
                         'finding 12/2026 about it. His own splice sits at page eighty-four and runs nine '
                         'minutes; he has never asked anyone to remove it.']],
                       ['Halloway',
                        ["Elias's former partner, now running the licensed clinic on the corner. He made "
                         'repair affordable by making it ordinary, and offers Elias a room of his own in '
                         'exchange for silence — an offer that stays open, and stays unanswered.']],
                       ['The people on the register',
                        ['The woman with the receipts; the boy with the blue door; the family whose grey '
                         'father is factually intact; the old man who keeps asking for his wife; the '
                         'warehouse clerks who sold one summer twice; the two hundred and eleven addresses '
                         'that arrived as a list.']]],
        'themes': [['Facts versus feeling',
                    ['The central question: what makes a memory *yours* — the facts, or the feeling? The '
                     'story keeps returning to the line, *"You can save the facts, you can\'t save the '
                     'feeling."*']],
                   ['The second signature',
                    ["The story's answer to a closed trade is not a better machine but a second name on the "
                     'page. A repair holds because someone else can read what was done, and because the '
                     'person who did it can be found.']],
                   ['The ethics of helping',
                    ['Is a comfortable lie kinder than a painful truth? The repair trade sells relief by '
                     'erasing, and every client chooses that bargain willingly — including Elias. The fourth '
                     'condition on 4-119 is the trade admitting, in writing, where that bargain fails.']],
                   ['Recurring motifs',
                    ['The smell of rain on hot metal; a **blue door** that appears in more than one memory; '
                     'the phrase about facts and feeling; and a last line — *"The ledger is complete."* — '
                     'arriving as an ending rather than a flourish.']]],
        'faq': [['What is this?',
                 ['A near-future science-fiction serial in one hundred chapters and thirteen parts, '
                  'published under the byline apprank studio. It is a work of fiction.']],
                ['Which languages?',
                 ['All one hundred chapters exist in English, Turkish, Cantonese and Korean — four full '
                  'editions, not excerpts. Each chapter is reviewed before it appears; the full disclosure '
                  'is on the About page.']],
                ['Where do I start?',
                 ['At chapter one, or at the series page for The Register, which collects the parts. The '
                  'second half is written as dated ledger entries; the first half is not, and the log itself '
                  'explains why.']],
                ['Was it written by a human?',
                 ['The English chapters were drafted with AI assistance and reviewed. Translations are '
                  'AI-assisted and reviewed separately. No fabricated author biography or portrait is used — '
                  'see the About page for the full disclosure.']],
                ['Is it free?',
                 ['Yes. No account, no paywall, no tracking. The source and method are open.']]]},
 'tr': {'world': [['Engramlar',
                   ['**Engram**, tek bir anının taşınabilir kaydıdır. Kayıplıdır: hasarlı parçalar geri '
                    'getirilemez, yalnızca köprülenir. İnsanlar onları eskiden fotoğraf taşıdıkları gibi '
                    'kutu ve kılıflarda taşır.',
                    'Onarım, geri getirme değildir. Boşluklar **sentetik bağ dokusuyla** doldurulur: '
                    'inandırıcı, kararlı, duygusuz. Olgular hayatta kalır; duygu kalmaz.']],
                  ['Tezgâh',
                   ['**Tezgâh**, bir engramı tamircinin içinde çalışabileceği bir yapıya dönüştüren masa '
                    'büyüklüğünde bir makinedir; bir konservatörün fresk üzerinde çalışması gibi. Her onarım '
                    'bir dikiş bırakır.',
                    'Elias, bir başka on yılda yasal olan parçalardan yapılmış eski, lisanssız bir tezgâh '
                    'kullanır. Tezgâhta iki kişi — biri tutan, biri tanık olan — bu işin bütün etiğidir; geç '
                    'yazıya geçmiştir.']],
                  ['Dolgu ve depo',
                   ["Her onarım **dolgu** tüketir: boşluğu köprüleyen sentetik doku. Koruma Dairesi'nin "
                    'kıyısındaki bir depoda ağırlıkla satılır ve depo onu tuğlayla satar: bir tuğla dört '
                    'saatlik iş, daha küçük birim yok.',
                    'Partiler numaralıdır. Bir yaz aynı parti iki numarayla iki kez satıldı; bunu kanıtlayan '
                    'kâğıt ancak bir şikâyetten sonra ortaya çıktı. Dolgu ucuz; nereden geldiğinin kaydı '
                    'değil.']],
                  ['Gri',
                   ['Ölçekli onarım, **griyi** özel bir talihsizlik olmaktan çıkarıp bölge çapında bir '
                    "duruma dönüştürdü: Koruma Dairesi'nin kendi sicilinde iki yüz on bir adres var ve "
                    'hiçbirinin adı yok.',
                    'Sektörün sloganı, *"Size olanı geri veriyoruz"* der. Tamircilerin bildiği gerçek ise: '
                    '*"Size olanın şeklini geri veriyoruz."*']],
                  ['Koruma Dairesi',
                   ["Koruma Dairesi hem ruhsat makamı hem bu yerin havasıdır. Mara'nınki gibi ruhsatlar "
                    '(4-119) verir, her yasal onarımın iki ad taşıdığı sicili tutar ve bulgularını üç nüsha '
                    'yazan müfettişler gönderir.',
                    'Büroları yıpranmış, bürokratik ve sıradandır: yağmur, metal tenteler, güven veren '
                    'maviye boyanmış klinikler ve bir kâtibin altı yıldır aynı defteri tuttuğu bir depo.']]],
        'characters': [['Elias Vane',
                        ['Elli yaşlarının sonunda, bir zamanlar hafıza mimarı — ilk ticari tezgâhları '
                         'tasarlayan mühendislerden biri. Asla konuşmadığı bir olaydan sonra ayrıldı ve '
                         "şimdi Cinder Lane'de lisanssız bir dükkân işletiyor.",
                         'Kuralı kendi engramını onarmamaktı. Kendi tuttuğu kütüğün ilk satırından beri '
                         'kural, ikinci bir kişinin okuyabileceği yere yazılıyor — değişmesinin tek nedeni '
                         'de bu.']],
                       ['Mara',
                        ["Elias'ın eski mentoru ve anısının silindiği günün gerçeğinin diğer yarısı. 4-119 "
                         'numaralı ruhsatı koşullarla geri gelir: çift imza, işten önce ortak adın '
                         'yazılması, defterde iki ad — ve yetmiş dokuzuncu bölümden itibaren dördüncü koşul: '
                         'ikinci imza olduğu yerde kendi hesabını onaramaz.',
                         'Bu anlatıda hayalet değil. İkinci çift el ve dikişin kaydedilmesinde ısrar eden '
                         'kişi.']],
                       ['Wren Adey',
                        ['İşe alındığında on dokuz yaşında; tezgâhtan önce kütüğü okuyan bir çırak. Altmış '
                         'dört bölüm boyunca bir imzanın neye mal olduğunu öğrenir ve ilk imzasını doksan '
                         'beşinci bölümde eşit olarak verir.']],
                       ['Müfettiş Ader',
                        ['Dükkânın evrakı yerine kendi kuşkusunu denetleyen ve bunun üzerine 12/2026 '
                         'numaralı bulguyu yazan denetçi. Kendi eki seksen dördüncü sayfada duruyor ve dokuz '
                         'dakika sürüyor; kimseden onu çıkarmasını istemedi.']],
                       ['Halloway',
                        ["Elias'ın eski ortağı, şimdi köşedeki lisanslı kliniği yönetiyor. Onarımı "
                         "sıradanlaştırarak herkesin alabileceği hale getirdi ve Elias'a sessizlik "
                         'karşılığında kendi odasını teklif etti — teklif açık kalıyor ve cevapsız '
                         'kalıyor.']],
                       ['Sicildeki insanlar',
                        ['Makbuzlu kadın; mavi kapılı çocuk; olguları sağlam gri babası olan aile; karısını '
                         'ısrarla isteyen yaşlı adam; bir yazı iki kez satan depo kâtipleri; liste olarak '
                         'gelen iki yüz on bir adres.']]],
        'themes': [['Olgulara karşı duygu',
                    ['Merkezî soru: bir anıyı *senin* yapan nedir — olgular mı, duygu mu? Hikâye sürekli şu '
                     'cümleye döner: *"Olguları kurtarabilirsin, duyguyu kurtaramazsın."*']],
                   ['İkinci imza',
                    ['Hikâyenin kapalı bir mesleğe verdiği cevap daha iyi bir makine değil, sayfadaki ikinci '
                     'addır. Bir onarım tutar, çünkü başkası ne yapıldığını okuyabilir ve yapan kişi '
                     'bulunabilir.']],
                   ['Yardımın etiği',
                    ['Rahat bir yalan, acı gerçekten daha mı nazik? Onarım sektörü silerek rahatlama satar '
                     "ve her müşteri bu pazarlığı gönüllü yapar — Elias da dahil. 4-119'un dördüncü koşulu, "
                     'bu pazarlığın nerede iflas ettiğini yazıyla kabul etmesidir.']],
                   ['Yinelenen simgeler',
                    ['Yağmurun sıcak metaldeki kokusu; birden fazla anıda görünen **mavi kapı**; olgular ve '
                     'duygu üzerine söz; ve bir son cümle — *"Kütük tamamlandı."* — süs olarak değil, bir '
                     'bitiş olarak gelir.']]],
        'faq': [['Bu nedir?',
                 ['Yüz bölüm, on üç kısımdan oluşan, apprank studio imzasıyla yayımlanan bir yakın gelecek '
                  'bilimkurgu tefrikası. Bir kurgu eseridir.']],
                ['Hangi dillerde?',
                 ['Yüz bölümün tamamı İngilizce, Türkçe, Kantonca ve Korece olarak var — dört tam baskı, '
                  'bölüm özeti değil. Her bölüm yayımlanmadan önce incelenir; tam açıklama Hakkında '
                  'sayfasındadır.']],
                ['Nereden başlamalı?',
                 ['Birinci bölümden, ya da kısımları toplayan The Register dizin sayfasından. İkinci yarı '
                  'tarihli kütük kayıtları olarak yazılmıştır; ilk yarı değildir ve kütük bunun nedenini '
                  'anlatır.']],
                ['İnsan tarafından yazıldı mı?',
                 ['İngilizce bölümler yapay zekâ desteğiyle taslaklandı ve incelendi. Çeviriler yapay zekâ '
                  'desteklidir ve ayrıca incelenir. Uydurma yazar biyografisi veya portresi kullanılmaz — '
                  'ayrıntılı açıklama Hakkında sayfasındadır.']],
                ['Ücretsiz mi?',
                 ['Evet. Hesap yok, ödeme duvarı yok, takip yok. Kaynak ve yöntem açıktır.']]]},
 'yue': {'world': [['記憶核',
                    ['**記憶核**係一段回憶嘅可攜式紀錄。佢係有損嘅：受損部分救唔返，只可以搭橋。人哋用盒同套帶住佢，好似以前帶相咁。',
                     '修補唔係還原。佢用**合成填料**補返啲空洞 —— 合理、穩定、冇感情。事實留得低，感覺留唔低。']],
                   ['織機',
                    ['**織機**係一部枱咁大嘅機器，將記憶核呈現成修補師可以喺入面工作嘅結構，好似文物修復師對住壁畫咁。每次修補都會留低一道接縫。',
                     'Elias 用緊一部舊、冇牌嘅織機，由另一個年代仲合法嘅零件砌成。織機前面兩個人 —— 一個揸住，一個做證 —— 就係呢行嘅全部倫理，遲咗先寫落紙。']],
                   ['填料同貨倉',
                    ['每次修補都會耗**填料**：用嚟搭橋嘅合成組織。管理局邊上一間貨倉按重量賣，而且只按磚賣：一磚四粒鐘工，冇更細嘅單位。',
                     '每批都有號碼。有一個夏天，同一批貨用兩個號碼賣咗兩次；證明呢件事嘅紙，要等一封投訴信之後先浮上嚟。填料平；佢嚟自邊度嘅紀錄唔平。']],
                   ['灰化',
                    ['大規模修補令**灰化**變成分區現象，唔再係一個人嘅不幸：管理局自己本名冊上面有二百一十一個地址，而佢哋一個名都冇。',
                     '行業口號話：*「我哋將發生過嘢還返畀你。」* 修補師知嘅真相係：*「我哋將發生過嘢嘅形還返畀你。」*']],
                   ['管理局',
                    ['管理局係發牌嘅機構，亦係呢度嘅天氣。佢發 4-119 咁樣嘅牌照，保管一本名冊 —— 每次合法修補都要有兩個名 —— 又派督察，督察寫嘅結論一式三份。',
                     '辦事處殘舊、官僚、平平無奇：雨、金屬簷篷、漆成安心藍嘅診所，仲有一個貨倉 —— 嗰度有個文員，同一本簿記咗六年。']]],
         'characters': [['Elias Vane',
                         ['五十幾歲，曾經係記憶架構師 —— 設計第一批商用織機嘅工程師之一。佢喺一件從來唔講嘅事故之後離開，而家喺 Cinder Lane 開一間冇牌嘅鋪。',
                          '佢條規矩係唔修補自己嘅記憶核。由佢自己寫嘅簿第一行開始，規矩就寫喺第二個人讀得到嘅地方 —— 亦係佢後來會改嘅唯一原因。']],
                        ['Mara',
                         ['Elias 昔日嘅導師，亦係佢記憶被抹走嗰日真相嘅另一半。佢個牌 4-119 帶住條件返嚟：雙簽、動工前先寫低合夥人名、簿上兩個名 —— '
                          '由第七十九章起仲有第四條：佢做第二簽名嘅地方，唔可以修自己個戶口。',
                          '呢個版本入面佢唔係鬼。佢係第二雙手，亦係堅持要記低條接縫嗰個人。']],
                        ['Wren Adey', ['請佢嗰陣十九歲，係個讀簿先過讀織機嘅學徒。佢用六十四章學一個簽名值幾多，到第九十五章第一次以對等身份簽。']],
                        ['督察 Ader', ['唔查鋪頭嘅紙，查自己嘅疑惑，然後為此寫低 12/2026 號結論嘅審計員。佢自己嗰條接縫喺第八十四頁，行九分鐘；佢從來冇叫人拆。']],
                        ['Halloway',
                         ['Elias 昔日嘅合伙人，而家打理街角嗰間持牌診所。佢令修補變成平常事，人人負擔得起，並提出用沉默換一間屬於自己嘅房 —— 個 offer '
                          '一直開住，一直冇人答。']],
                        ['名冊上嘅人',
                         ['收據女人；有藍門嘅後生仔；灰化但事實完整嘅阿爸嘅家人；一直問要太太嘅老伯；一個夏天賣咗兩次貨嘅倉務員；以一份名單形式到嚟嘅二百一十一個地址。']]],
         'themes': [['事實對感覺', ['核心問題：係咩令一段記憶成為*你嘅* —— 事實，定係感覺？故事不斷回到呢句：*「你可以救返啲事實，你救唔返嗰種感覺。」*']],
                    ['第二個簽名', ['故事對一門閉門手藝嘅答案唔係更好嘅機器，而係紙上第二個名。修補掯得住，係因為第二個人讀得到做過咩，亦因為做嗰個人搵得返。']],
                    ['幫人嘅倫理',
                     ['舒服嘅謊話係咪比痛苦嘅真相更善良？修補行業靠抹走嘢賣解脫，每個客都自願做呢筆交易 —— Elias 都係。4-119 '
                      '嘅第四條，就係呢行用白紙黑字承認呢筆交易喺邊度破產。']],
                    ['重複意象', ['雨打熱金屬嘅味；喺多過一段記憶出現嘅**藍門**；關於事實同感覺嘅說話；仲有一句收尾 —— *「簿已經寫完。」* —— 佢係結局，唔係點綴。']]],
         'faq': [['呢個係咩？', ['一部一百章、十三部嘅近未來科幻連載，以 apprank studio 署名出版。係虛構作品。']],
                 ['有咩語言？', ['一百章全部有英文、土耳其文、粵文同韓文 —— 四個完整版本，唔係節錄。每章上架前都會審校；完整說明喺「關於」頁。']],
                 ['由邊度開始睇？', ['由第一章開始，或者去 The Register 系列頁（嗰度按部收埋）。後半部係有日期嘅簿記條目，前半部唔係，簿入面有講原因。']],
                 ['係咪人寫嘅？', ['英文章節由 AI 協助起草同審校。譯文由 AI 協助並獨立審校。我哋唔會虛構作者履歷或者頭像 —— 完整說明喺「關於」頁。']],
                 ['係咪免費？', ['係。冇帳號、冇付費牆、冇追蹤。源碼同方法都係公開。']]]},
 'ko': {'world': [['엔그램',
                   ['**엔그램**은 하나의 회상을 담은 휴대용 기록입니다. 손실이 있어 손상된 부분은 되찾을 수 없고 다리만 놓을 수 있습니다. 사람들은 예전에 사진을 들듯 '
                    '케이스와 슬리브에 넣어 들고 다닙니다.',
                    '수리는 복원이 아닙니다. 빈 곳을 **합성 채움**으로 메웁니다. 그럴듯하고 안정적이지만 감정이 없습니다. 사실은 남고 감정은 사라집니다.']],
                  ['직조기',
                   ['**직조기**는 엔그램을 수리공이 그 안에서 작업할 수 있는 구조로 펼치는 탁자 크기의 기계입니다. 보존사가 프레스코를 다루듯합니다. 모든 수리는 봉합을 '
                    '남깁니다.',
                    'Elias는 다른 십 년 전에는 합법이었던 부품으로 만든 낡고 무면허인 직조기를 씁니다. 직조기 앞의 두 사람 — 한 사람이 붙잡고 한 사람이 증언하는 것 '
                    '— 이 이 업의 윤리 전부이며, 뒤늦게 종이에 적혔습니다.']],
                  ['채움과 창고',
                   ['수리 한 번마다 **채움**이 듭니다. 빈 곳을 잇는 합성 조직입니다. 관리청 외곽의 창고에서 무게로 팔고, 벽돌 단위로만 팝니다. 벽돌 하나에 네 시간, '
                    '더 작은 단위는 없습니다.',
                    '로트에는 번호가 붙습니다. 어느 여름, 같은 로트가 두 번호로 두 번 팔렸고, 그것을 증명하는 종이는 한 통의 항의 뒤에야 나왔습니다. 채움은 싸고, 어디서 '
                    '왔는지의 기록은 싸지 않습니다.']],
                  ['회색화',
                   ['대규모 수리는 **회색화**를 이제 개인의 불운이 아니라 구역 전체의 현상으로 만들었습니다. 관리청 자기 명부에 이백열한 개 주소, 그리고 그중 어느 것에도 '
                    '이름이 없습니다.',
                    '업계 구호는 *"일어난 일을 되돌려 드립니다"* 라고 합니다. 수리공이 아는 진실은 이렇습니다. *"일어난 일의 형태를 되돌려 드립니다."*']],
                  ['관리청',
                   ['관리청은 면허 기관이고 이곳의 날씨입니다. 4-119 같은 면허를 내주고, 합법 수리마다 두 이름이 오르는 명부를 보관하며, 결론을 세 부로 쓰는 조사관을 '
                    '보냅니다.',
                    '사무실은 낡고 관료적이고 평범합니다. 비, 금속 차양, 안심되는 파란색으로 칠한 진료소, 그리고 한 서기가 육 년 동안 같은 공책을 쓰는 창고.']]],
        'characters': [['Elias Vane',
                        ['오십 대 후반. 한때 기억 설계자, 최초의 상업용 직조기를 설계한 기술자 중 한 명. 결코 말하지 않는 사건 뒤에 떠나 지금은 Cinder '
                         'Lane에서 무면허 가게를 엽니다.',
                         '규칙은 자기 엔그램을 수리하지 않는다는 것이었습니다. 자기가 직접 쓰기 시작한 장부의 첫 줄부터, 규칙은 두 번째 사람이 읽을 수 있는 곳에 적혀 '
                         '있습니다. 규칙이 바뀌는 이유도 그것뿐입니다.']],
                       ['Mara',
                        ['Elias의 옛 멘토이고, 기억이 지워진 날의 진실 절반입니다. 면허 4-119는 조건을 달고 돌아옵니다. 이중 서명, 작업 전 공동 이름 기재, '
                         '장부에 두 이름, 그리고 칠십구 장부터 네 번째 조건 — 두 번째 서명을 하는 자리에서 자기 계정은 고칠 수 없습니다.',
                         '이 버전에서 그녀는 유령이 아닙니다. 두 번째 손이고, 봉합을 기록하자고 고집하는 사람입니다.']],
                       ['Wren Adey',
                        ['고용될 때 열아홉 살, 직조기보다 장부를 먼저 읽는 견습공. 예순네 장 동안 서명값을 배우고, 구십오 장에서 처음으로 대등하게 서명합니다.']],
                       ['조사관 Ader',
                        ['가게 서류 대신 자기 의심을 심사하고 그에 대해 12/2026 결론을 쓴 조사관. 자기 봉합은 여든네 페이지에 있고 구 분 동안 이어집니다. '
                         '누구에게도 빼 달라고 한 적이 없습니다.']],
                       ['Halloway',
                        ['Elias의 옛 동료이자 지금은 모퉁이의 면허 진료소를 운영합니다. 수리를 흔한 일로 만들어 누구나 감당하게 했고, 침묵과 맞바꾸어 자기 방을 '
                         '제안합니다. 그 제안은 계속 열려 있고, 계속 답이 없습니다.']],
                       ['명부 위의 사람들',
                        ['영수증 든 여자, 파란 문이 있는 소년, 회색화됐지만 사실은 온전한 아버지의 가족, 아내를 계속 찾는 노인, 한여름을 두 번 판 창고 서기들, '
                         '목록으로 도착한 이백열한 개 주소.']]],
        'themes': [['사실 대 감정',
                    ['중심 질문: 어떤 회상을 *당신의 것*으로 만드는 것은 사실인가, 감정인가? 이야기는 계속 이 문장으로 돌아갑니다. *"사실은 살릴 수 있어도 감정은 살릴 '
                     '수 없다."*']],
                   ['두 번째 서명',
                    ['이야기가 닫힌 업종에 내놓는 답은 더 나은 기계가 아니라 종이 위의 두 번째 이름입니다. 수리가 버티는 것은 남이 무엇을 했는지 읽을 수 있고, 그 사람을 '
                     '찾을 수 있기 때문입니다.']],
                   ['돕기의 윤리',
                    ['편안한 거짓말이 고통스러운 진실보다 친절한가? 수리업은 지움으로써 안도를 팔고, 모든 고객이 자발적으로 그 거래를 한다 — Elias도 포함해. '
                     '4-119의 네 번째 조건은 그 거래가 어디서 무너지는지를 업계가 글로 인정한 것입니다.']],
                   ['되풀이되는 모티프',
                    ['뜨거운 금속에 내리는 비 냄새, 한 번 이상의 기억에 나타나는 **파란 문**, 사실과 감정에 관한 말, 그리고 마지막 문장 — *"장부는 완결되었다."* '
                     '— 장식이 아니라 결말로 도착합니다.']]],
        'faq': [['이건 무엇인가요?', ['백 장, 열세 부로 이어지는 근미래 공상과학 연재입니다. apprank studio 이름으로 출판되었고 허구의 작품입니다.']],
                ['어떤 언어로 있나요?',
                 ['백 장 전부가 영어, 터키어, 광둥어, 한국어로 있습니다. 발췌가 아닌 네 개의 완전판입니다. 각 장은 검토를 거쳐 게재되며 전체 공개 안내는 소개 페이지에 '
                  '있습니다.']],
                ['어디서 시작하나요?',
                 ['첫 장에서, 또는 부를 모아 둔 The Register 시리즈 페이지에서. 후반부는 날짜가 붙은 장부 항목이고 전반부는 아니며, 그 이유는 장부 안에 적혀 '
                  '있습니다.']],
                ['사람이 썼나요?',
                 ['영어 원고는 AI 도움으로 초안을 쓰고 검토했습니다. 번역도 AI 도움을 받아 별도로 검토됩니다. 허구의 작가 약력이나 초상은 쓰지 않습니다 — 자세한 내용은 '
                  '소개 페이지에 있습니다.']],
                ['무료인가요?', ['네. 계정도, 유료벽도, 추적도 없습니다. 출처와 방법은 공개되어 있습니다.']]]}}
