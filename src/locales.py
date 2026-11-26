"""Localized reading UI. Cantonese uses written Cantonese in Traditional script.

HTML/Schema use yue-Hant-HK. Search alternates use zh-HK because Google's
hreflang language format is ISO 639-1; the URL remains /yue/.
Translation chapters are reviewed separately, never inherit English approval.
"""
LOCALES = {
    "en": {
        "label": "English", "lang": "en", "hreflang": "en",
        "title": "The Memory Repairman", "subtitle": "Five parts, one shop: stories about the things we choose to forget.",
        "genre": "Science Fiction",
        "description": "A near-future science fiction short story about a man who repairs other people's memories — and the one memory he is forbidden to touch.",
        "about": "About", "behind": "Behind the story", "chapters": "Chapters", "chapter": "Chapter {n}",
        "short_story": "A short story", "by": "By {author}", "stats": "{n} chapters", "readtime": "{n} min read",
        "previous": "← Previous", "next": "Next →", "languages": "Reading language",
        "draft_tag": "preview draft", "draft_title": "Editor's note — preview draft.",
        "draft_notice": "This AI-assisted text is awaiting human review. Preview only; it is not an approved publication.",
        "pending": "Translations are awaiting separate human review. Read the published English original while the translated chapters are being prepared.",
        "no_chapters": "No chapters are published in this language yet. Chapters appear after human editorial review.",
        "read_english": "Read in English", "about_hint": "Explore the world, the author, and how this story was made.",
        "disclosure_title": "How this story was made.",
        "disclosure": "The published English chapters were drafted with AI assistance and reviewed by a human editor. Translations are AI-assisted and require their own review before publication. Unapproved translations are available only in the local draft preview. No fabricated author biography or portrait is used.",
        "full_disclosure": "Full disclosure", "fiction": "A work of fiction. Any resemblance to persons or events is coincidental.",
        "idea": "The idea", "world": "In the Ward, memories can be stored as engrams and repaired with a machine called the Loom. Synthetic fill bridges damaged memories, but cannot bring back lost feeling. Elias Vane repairs other people's memories until an old engram forces him to confront his own past.",
        "glossary": "A small glossary", "terms_hint": "Terms the story uses, without spoilers.",
        "terms": [("Engram", "A portable recording of a memory; its missing parts may never be recovered."), ("The Loom", "A machine that renders an engram as a structure a repairman can work inside."), ("Fill", "Synthetic connections inserted into damaged memories: plausible, stable, emotionally inert."), ("The Grey", "Facts remain, but feeling is lost after heavy repair."), ("Memory architect", "An engineer who designed the first commercial looms.")],
        "authorship": "Authorship & AI disclosure", "byline_notice": "Published under the byline {author}. Translation drafts do not imply approval by the editor.",
        "unpublished": "Not published", "unpublished_description": "This chapter is not part of the published work in this language.",
        "toc": "Table of contents", "contact": "Contact",
        "subscribe": "Get new chapters by email", "subscribe_button": "Subscribe",
        "subscribe_hint": "No account needed. Reply to any chapter email to unsubscribe.",
        "subscribe_ok": "You are on the list. A new chapter will land in your inbox.",
        "subscribe_err": "That email did not go through. Check it and try again.",
    },
    "tr": {
        "label": "Türkçe", "lang": "tr", "hreflang": "tr",
        "title": "Hafıza Tamircisi", "subtitle": "Unutmayı seçtiğimiz şeyler üzerine üç hikâye.",
        "genre": "Bilimkurgu",
        "description": "Başkalarının anılarını onaran bir adamı ve dokunması yasak olan tek anıyı anlatan, yakın gelecekte geçen bir bilimkurgu öyküsü.",
        "about": "Hakkında", "behind": "Hikâyenin arka planı", "chapters": "Bölümler", "chapter": "Bölüm {n}",
        "short_story": "Bir kısa öykü", "by": "Yazar: {author}", "stats": "{n} bölüm", "readtime": "{n} dakika okuma",
        "previous": "← Önceki", "next": "Sonraki →", "languages": "Okuma dili",
        "draft_tag": "ön izleme taslağı", "draft_title": "Editör notu — ön izleme taslağı.",
        "draft_notice": "Yapay zekâ desteğiyle hazırlanan bu metin insan incelemesini bekliyor. Yalnızca ön izleme içindir; yayımlanması onaylanmış bir metin değildir.",
        "pending": "Çeviriler ayrı bir insan incelemesini bekliyor. Çeviri bölümleri hazırlanırken yayımlanmış İngilizce aslını okuyabilirsiniz.",
        "no_chapters": "Bu dilde henüz yayımlanmış bölüm yok. Bölümler insan editör incelemesinden sonra burada yer alır.",
        "read_english": "İngilizce oku", "about_hint": "Öykünün dünyasını, yazarını ve nasıl hazırlandığını keşfedin.",
        "disclosure_title": "Bu hikâye nasıl hazırlandı?",
        "disclosure": "Yayımlanmış İngilizce bölümler yapay zekâ desteğiyle taslak hâline getirildi ve insan editör tarafından incelendi. Çeviriler de yapay zekâ desteklidir ve yayımlanmadan önce ayrıca incelenmelidir. Onaylanmamış çeviriler yalnızca yerel taslak ön izlemesinde okunabilir. Uydurma yazar biyografisi veya portresi kullanılmaz.",
        "full_disclosure": "Ayrıntılı açıklama", "fiction": "Bu eser kurgudur. Gerçek kişi veya olaylarla benzerlikler tesadüfidir.",
        "idea": "Çıkış noktası", "world": "Ward'da anılar engram adı verilen çekirdeklere kaydedilip Tezgâh adlı bir makineyle onarılabilir. Sentetik dolgu hasarlı anıları birbirine bağlar, ama kaybolan duyguları geri getiremez. Elias Vane, eski bir engram onu kendi geçmişiyle yüzleşmeye zorlayana kadar başkalarının anılarını onarır.",
        "glossary": "Küçük bir sözlük", "terms_hint": "Hikâyede kullanılan terimler; sürprizleri bozmadan.",
        "terms": [("Engram", "Bir anının taşınabilir kaydı; kayıp parçaları bir daha bulunamayabilir."), ("Tezgâh", "Bir engramı, tamircinin içinde çalışabileceği bir yapıya dönüştüren makine."), ("Dolgu", "Hasarlı anılara eklenen sentetik bağlar: inandırıcı, kararlı ve duygusuz."), ("Grilik", "Yoğun onarımdan sonra olguların kaldığı, duyguların kaybolduğu durum."), ("Hafıza mimarı", "İlk ticari tezgâhları tasarlayan mühendis.")],
        "authorship": "Yazarlık ve yapay zekâ açıklaması", "byline_notice": "Eser {author} adıyla yayımlanır. Çeviri taslakları editörün onay verdiği anlamına gelmez.",
        "unpublished": "Yayımlanmadı", "unpublished_description": "Bu bölüm, eserin bu dilde yayımlanmış hâline dâhil değildir.",
        "toc": "İçindekiler", "contact": "İletişim",
        "subscribe": "Yeni bölümleri e-postayla al", "subscribe_button": "Abone ol",
        "subscribe_hint": "Hesap gerekmez. Herhangi bir e-postayı yanıtlayarak ayrılabilirsin.",
        "subscribe_ok": "Listedesin. Yeni bölüm e-postana gelecek.",
        "subscribe_err": "E-posta kaydedilemedi. Kontrol edip tekrar dene.",
    },
    "yue": {
        "label": "粵語（節錄）", "lang": "yue-Hant-HK", "hreflang": "zh-HK",
        "summary_title": "呢個係節錄版：",
        "summary_notice": "每章只譯咗開頭嘅段落，未係全文，亦唔會出現在搜尋結果。想睇完整故事，請讀英文原文。",
        "title": "記憶修補師", "subtitle": "三個關於我哋選擇忘記啲乜嘢嘅故事。",
        "genre": "科幻",
        "description": "一個近未來科幻短篇：一個替人修補記憶嘅男人，同埋嗰段佢唔可以掂嘅記憶。",
        "about": "關於", "behind": "故事背後", "chapters": "章節", "chapter": "第 {n} 章",
        "short_story": "科幻短篇", "by": "署名：{author}", "stats": "{n} 章", "readtime": "約 {n} 分鐘閱讀",
        "previous": "← 上一章", "next": "下一章 →", "languages": "閱讀語言",
        "draft_tag": "預覽草稿", "draft_title": "編輯提示——預覽草稿。",
        "draft_notice": "呢份由 AI 協助寫成嘅文字仲等緊人工審校。只供預覽，唔係已獲批准出版嘅定稿。",
        "pending": "譯文要另外經人工審校。粵語章節準備期間，你可以先睇已出版嘅英文原文。",
        "no_chapters": "呢種語言暫時未有正式出版嘅章節。通過人工審校之後，章節先會喺呢度出現。",
        "read_english": "睇英文原文", "about_hint": "了解故事世界、署名，同埋呢個故事係點樣寫成。",
        "disclosure_title": "呢個故事係點樣寫成嘅？",
        "disclosure": "已出版嘅英文篇章由 AI 協助起草，再經人工編輯審校。譯文亦由 AI 協助翻譯，出版前要獨立審校。未獲批准嘅譯文只會喺本機草稿預覽顯示。我哋唔會虛構作者履歷或者頭像。",
        "full_disclosure": "完整說明", "fiction": "呢個係虛構故事。同真實人物或事件有任何相似，純屬巧合。",
        "idea": "故事構想", "world": "喺 Ward，記憶可以存入叫做「記憶核」嘅裝置，再用「織機」修補。合成填料可以接返受損嘅記憶，卻帶唔返已經流失嘅感情。Elias Vane 一直替人修補記憶，直到一枚舊記憶核逼佢面對自己嘅過去。",
        "glossary": "小詞彙表", "terms_hint": "故事入面用到嘅詞語，唔會劇透。",
        "terms": [("記憶核（Engram）", "可以隨身帶住嘅記憶紀錄；失去咗嘅部分未必搵得返。"), ("織機（The Loom）", "將記憶核呈現成一個修補師可以喺入面工作嘅結構嘅機器。"), ("填料（Fill）", "接入受損記憶嘅合成組織：合理、穩定，卻冇感情。"), ("灰化（The Grey）", "大量修補之後，事實仲喺度，感情卻冇晒嘅狀態。"), ("記憶架構師", "設計第一批商用織機嘅工程師。")],
        "authorship": "署名同 AI 披露", "byline_notice": "作品以 {author} 署名出版。譯文草稿唔代表編輯已經批准。",
        "unpublished": "未出版", "unpublished_description": "呢一章唔屬於呢種語言已正式出版嘅內容。",
        "toc": "章節目錄", "contact": "聯絡",
        "subscribe": "有新章節用電郵通知你", "subscribe_button": "訂閱",
        "subscribe_hint": "唔需要帳號，回覆任何一封電郵就可以退訂。",
        "subscribe_ok": "已經加入名單，有新章會寄去你信箱。",
        "subscribe_err": "電郵登記唔成功，檢查一下再試。",
    },
    "ko": {
        "label": "한국어", "lang": "ko", "hreflang": "ko",
        "title": "기억 수리공", "subtitle": "우리가 잊기로 선택한 것들에 관한 세 이야기.",
        "genre": "공상과학",
        "description": "다른 사람의 기억을 고치는 남자와 그가 건드려서는 안 되는 단 하나의 기억을 다룬 근미래 공상과학 단편.",
        "about": "소개", "behind": "이야기 뒤편", "chapters": "목차", "chapter": "제 {n}장",
        "short_story": "단편 소설", "by": "글: {author}", "stats": "{n}개 장", "readtime": "읽는 데 약 {n}분",
        "previous": "← 이전 장", "next": "다음 장 →", "languages": "읽기 언어",
        "draft_tag": "미리보기 초안", "draft_title": "편집자 안내 — 미리보기 초안입니다.",
        "draft_notice": "AI의 도움으로 작성된 이 글은 사람의 검토를 기다리고 있습니다. 미리보기 전용이며, 출판이 승인된 최종 원고가 아닙니다.",
        "pending": "번역문은 별도의 사람 검토를 기다리고 있습니다. 번역된 장이 준비되는 동안 출판된 영어 원문을 읽을 수 있습니다.",
        "no_chapters": "이 언어로 출판된 장은 아직 없습니다. 사람의 편집 검토를 마친 뒤 여기에 표시됩니다.",
        "read_english": "영어 원문 읽기", "about_hint": "이야기의 세계와 저자, 작품이 만들어진 과정을 알아보세요.",
        "disclosure_title": "이 이야기는 어떻게 만들어졌나요?",
        "disclosure": "출판된 영어 원고는 AI의 도움으로 초안을 작성한 뒤 사람이 검토했습니다. 번역문도 AI의 도움으로 작성되며 출판 전에 별도로 검토해야 합니다. 승인되지 않은 번역문은 로컬 초안 미리보기에서만 읽을 수 있습니다. 허구의 저자 약력이나 초상은 사용하지 않습니다.",
        "full_disclosure": "자세한 안내", "fiction": "이 작품은 허구입니다. 실제 인물이나 사건과의 유사성은 우연입니다.",
        "idea": "이야기의 출발점", "world": "워드에서는 기억을 ‘엔그램’이라는 장치에 저장하고 ‘직조기’라는 기계로 수리할 수 있습니다. 합성 충전재는 손상된 기억을 이어 주지만 잃어버린 감정은 되돌리지 못합니다. 엘리아스 베인은 남들의 기억을 고치며 살아가다가 오래된 엔그램 때문에 자신의 과거와 마주하게 됩니다.",
        "glossary": "작은 용어 사전", "terms_hint": "줄거리의 비밀을 밝히지 않고 설명하는 작품 속 용어들입니다.",
        "terms": [("엔그램", "휴대할 수 있는 기억 기록. 사라진 부분은 영영 복구할 수 없을 수도 있습니다."), ("직조기", "엔그램을 수리공이 그 안에서 작업할 수 있는 구조로 펼치는 기계."), ("충전재", "손상된 기억에 넣는 합성 연결 조직. 그럴듯하고 안정적이지만 감정은 없습니다."), ("회색화", "대대적인 수리 뒤에 사실은 남고 감정은 사라지는 상태."), ("기억 설계자", "최초의 상업용 직조기를 설계한 기술자.")],
        "authorship": "저자 및 AI 사용 안내", "byline_notice": "작품은 {author}라는 이름으로 출판됩니다. 번역 초안이 편집자의 승인을 뜻하지는 않습니다.",
        "unpublished": "미출판", "unpublished_description": "이 장은 이 언어로 정식 출판된 작품에 포함되지 않습니다.",
        "toc": "목차로 돌아가기", "contact": "연락처",
        "subscribe": "새 장을 이메일로 받아보기", "subscribe_button": "구독",
        "subscribe_hint": "계정 필요 없습니다. 받은 메일에 답장하면 해지됩니다.",
        "subscribe_ok": "목록에 추가되었습니다. 새 장이 메일로 발송됩니다.",
        "subscribe_err": "이메일을 등록하지 못했습니다. 다시 확인해 주세요.",
    },
}


# 站点丰富化文案：探索导航、三部曲分组、延伸阅读、阅读进度。
# 独立于 LOCALES 主表，便于增量维护；键名统一，四语齐全。
EXTRA = {
    "en": {
        "explore": "Explore",
        "parts": ["Part I · The Shop", "Part II · The Trade", "Part III · The Witness", "Part IV · The Review", "Part V · The Joint"],
        "start_reading": "Start reading →",
        "continue_reading": "Continue reading",
        "resume_hint": "You were on chapter {n}.",
        "further": "Continue exploring",
        "progress_label": "Reading progress",
        "progress_hint": "Saved on this device only — no account, no tracking.",
        "clear_progress": "Clear",
    },
    "tr": {
        "explore": "Keşfet",
        "parts": ["Bölüm I · Dükkân", "Bölüm II · Meslek", "Bölüm III · Şahit", "Bölüm IV · Denetim", "Bölüm V · Eklem"],
        "start_reading": "Okumaya başla →",
        "continue_reading": "Kaldığın yerden oku",
        "resume_hint": "Bölüm {n} üzerindeydin.",
        "further": "Keşfetmeye devam et",
        "progress_label": "Okuma ilerlemesi",
        "progress_hint": "Yalnızca bu cihazda saklanır — hesap yok, takip yok.",
        "clear_progress": "Temizle",
    },
    "yue": {
        "explore": "探索",
        "parts": ["第一部 · 間鋪", "第二部 · 呢行", "第三部 · 證人", "第四部 · 審查", "第五部 · 接駁"],
        "start_reading": "開始閱讀 →",
        "continue_reading": "繼續閱讀",
        "resume_hint": "你上次讀到第 {n} 章。",
        "further": "繼續探索",
        "progress_label": "閱讀進度",
        "progress_hint": "只保存在呢部裝置 —— 冇帳號、冇追蹤。",
        "clear_progress": "清除",
    },
    "ko": {
        "explore": "둘러보기",
        "parts": ["1부 · 가게", "2부 · 업계", "3부 · 증인", "4부 · 심사", "5부 · 이음"],
        "start_reading": "읽기 시작 →",
        "continue_reading": "이어서 읽기",
        "resume_hint": "제 {n}장까지 읽었습니다.",
        "further": "계속 둘러보기",
        "progress_label": "읽기 진행 상황",
        "progress_hint": "이 기기에만 저장됩니다 — 계정도, 추적도 없습니다.",
        "clear_progress": "지우기",
    },
}


def route(language: str, suffix: str = "/") -> str:
    return suffix if language == "en" else f"/{language}" + suffix


def work(base: dict, language: str) -> dict:
    data = LOCALES[language]
    return {**base, **{key: data[key] for key in ("title", "subtitle", "genre", "description")},
            "language": data["lang"]}


# 阅读交互文案（字号 / 夜间模式 / 目录 / 复制链接），四语齐备。
_READER_COPY = {'en': {'reader_tools': 'Reading options', 'font_smaller': 'Smaller text', 'font_larger': 'Larger text', 'night_mode': 'Night mode', 'day_mode': 'Day mode', 'copy_link': 'Copy link', 'copied': 'Link copied', 'toc_open': 'Contents', 'toc_close': 'Close contents', 'keyboard_hint': 'Use the arrow keys to move between chapters'}, 'tr': {'reader_tools': 'Okuma seçenekleri', 'font_smaller': 'Daha küçük yazı', 'font_larger': 'Daha büyük yazı', 'night_mode': 'Gece modu', 'day_mode': 'Gündüz modu', 'copy_link': 'Bağlantıyı kopyala', 'copied': 'Bağlantı kopyalandı', 'toc_open': 'İçindekiler', 'toc_close': 'İçindekileri kapat', 'keyboard_hint': 'Bölümler arasında geçmek için ok tuşlarını kullan'}, 'ko': {'reader_tools': '읽기 설정', 'font_smaller': '글자 작게', 'font_larger': '글자 크게', 'night_mode': '야간 모드', 'day_mode': '주간 모드', 'copy_link': '링크 복사', 'copied': '링크가 복사되었습니다', 'toc_open': '차례', 'toc_close': '차례 닫기', 'keyboard_hint': '화살표 키로 이전·다음 장으로 이동합니다'}, 'yue': {'reader_tools': '閱讀設定', 'font_smaller': '字細啲', 'font_larger': '字大啲', 'night_mode': '夜間模式', 'day_mode': '日間模式', 'copy_link': '複製連結', 'copied': '連結已複製', 'toc_open': '目錄', 'toc_close': '閂目錄', 'keyboard_hint': '用方向鍵可以跳去上一章或下一章'}}
for _lang, _extra in _READER_COPY.items():
    LOCALES[_lang].update(_extra)
