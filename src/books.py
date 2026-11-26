# -*- coding: utf-8 -*-
"""books.py — 多部独立小说的书目登记表。

每部小说一个目录：content/books/<slug>/chapters（英文）与
content/books/<slug>/translations/<lang>（译本，文件名必须与英文源同名）。
这里是书目元数据；章节标题与摘要来自各语言自己的 front matter。
"""

BOOKS = [
    {
        "slug": "the-salt-ledger",
        "title": "The Salt Ledger",
        "tagline": {
            "en": "A lighthouse keeper's book that writes the wreck nine days before the wreck.",
            "tr": "Bir fener bekçisinin defteri, kazayı kazadan dokuz gün önce yazıyor.",
            "ko": "등대지기의 장부가 배가 침몰하기 아흐레 전에 그 침몰을 적는다.",
            "yue": "燈塔看守人嘅簿，喺沉船前九日就寫低單沉船。",
        },
        "genre": {
            "en": "Maritime gothic mystery",
            "tr": "Deniz gotiği gizem",
            "ko": "해양 고딕 미스터리",
            "yue": "海事哥德懸疑",
        },
    },
    {
        "slug": "nine-minutes-of-static",
        "title": "Nine Minutes of Static",
        "tagline": {
            "en": "A comms officer on an ageing station hears a colleague inside nine minutes of radio hiss.",
            "tr": "Yaşlı bir istasyonda telsizci, dokuz dakikalık parazitin içinde bir iş arkadaşını duyuyor.",
            "ko": "낡은 정거장의 통신 장교가 9분짜리 잡음 속에서 동료의 목소리를 듣는다.",
            "yue": "老化太空站嘅通訊官，喺九分鐘雜音入面聽到一個同事把聲。",
        },
        "genre": {
            "en": "Space station science fiction",
            "tr": "Uzay istasyonu bilim kurgu",
            "ko": "우주 정거장 SF",
            "yue": "太空站科幻",
        },
    },
    {
        "slug": "the-bone-orchard",
        "title": "The Bone Orchard",
        "tagline": {
            "en": "In Orra the dead are not buried; they are planted, and the fruit is bone.",
            "tr": "Orra'da ölüler gömülmez; dikilir, ve meyve kemiktir.",
            "ko": "오라에서는 죽은 자를 묻지 않는다. 심고, 열매는 뼈다.",
            "yue": "Orra 唔埋葬死人，只種人；樹果結出嚟嘅係骨。",
        },
        "genre": {
            "en": "Folk horror",
            "tr": "Halk korku",
            "ko": "민속 공포",
            "yue": "民俗恐怖",
        },
    },
    {
        "slug": "sunday-repeated",
        "title": "Sunday, Repeated",
        "tagline": {
            "en": "A courier keeps delivering one parcel to an address that only exists for nineteen minutes a week.",
            "tr": "Bir kurye, haftada on dokuz dakika var olan bir adrese aynı paketi teslim etmeye devam ediyor.",
            "ko": "배달원이 일주일에 19분만 존재하는 주소로 같은 소포를 계속 배달한다.",
            "yue": "一個送貨仔，每星期都要送同一個包去一個只存在十九分鐘嘅地址。",
        },
        "genre": {
            "en": "Urban time-loop mystery",
            "tr": "Şehirde zaman döngüsü gizemi",
            "ko": "도시 시간 루프 미스터리",
            "yue": "都市時間循環懸疑",
        },
    },
    {
        "slug": "the-last-translator",
        "title": "The Last Translator",
        "tagline": {
            "en": "The last licensed translator of a dying language is paid to certify its death, and refuses.",
            "tr": "Ölmekte olan bir dilin son ruhsatlı çevirmenine ölümünü onaylaması için para verilir, ve kabul etmez.",
            "ko": "사라지는 언어의 마지막 공인 번역가에게 그 죽음을 인증하라고 돈을 주지만, 그는 거절한다.",
            "yue": "一種將死嘅語言，最後一個持牌翻譯員畀人出錢要佢簽話呢種語言已死，佢唔肯。",
        },
        "genre": {
            "en": "Dystopian linguistic fiction",
            "tr": "Distopik dil kurgusu",
            "ko": "디스토피아 언어 픽션",
            "yue": "反烏托邦語言小說",
        },
    },
    {
        "slug": "weather-for-a-town-that-isnt-there",
        "title": "Weather for a Town That Isn't There",
        "tagline": {
            "en": "A night-shift forecaster keeps finding a drowned parish in the model, three o'clock sharp.",
            "tr": "Gece vardiyasındaki bir hava tahmincisi, modelin içinde su altında kalmış bir köyü her gece üçte buluyor.",
            "ko": "야간 근무 예보관이 매일 새벽 세 시, 모델 속에서 물에 잠긴 마을을 발견한다.",
            "yue": "夜班預報員每個凌晨三點，都會喺模型入面見到一條沉咗落水嘅村。",
        },
        "genre": {
            "en": "Quiet speculative fiction",
            "tr": "Sakin spekülatif kurgu",
            "ko": "조용한 사변 소설",
            "yue": "靜默科幻小品",
        },
    },
    {
        "slug": "the-twenty-fourth-child",
        "title": "The Twenty-Fourth Child",
        "tagline": {
            "en": "A one-room school keeps twenty-three names on its roll and twenty-four children in the room.",
            "tr": "Tek odalı bir okulun listesinde yirmi üç isim, odasında yirmi dört çocuk var.",
            "ko": "한 교실 학교의 명단에는 스물세 개의 이름이, 교실에는 스물네 명의 아이가 있다.",
            "yue": "一間單室學校，名單上廿三個名，課室入面廿四個細路。",
        },
        "genre": {
            "en": "Quiet rural uncanny",
            "tr": "Sakin taşra tekinsizliği",
            "ko": "조용한 농촌 기이 소설",
            "yue": "靜默鄉村異談",
        },
    },
]
