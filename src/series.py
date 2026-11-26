# -*- coding: utf-8 -*-
"""series.py — 把六部独立短篇编成一套系列：《The Register》登记册。

共享设定：一个常设机构，专门登记「没有见证人的事件」。六部小说各是它的一宗
案卷：一本会提前写下沉船的簿、一份把舱室签给不在册者的舱单、十二块无名的
铁牌、一张没人签收的包裹回执、一份给将死语言开的死亡证明、一段为水下小镇
补登的观测站条目。对象各异，笔迹是同一个。

本模块只提供系列文案、卷次与互相指认的一句话；不改动章节正文，因此不影响
译本与英文源之间的 source_sha256 绑定。
"""
from __future__ import annotations

SERIES = {
    "slug": "the-register",
    "order": [
        "the-salt-ledger",
        "nine-minutes-of-static",
        "the-bone-orchard",
        "sunday-repeated",
        "the-last-translator",
        "weather-for-a-town-that-isnt-there",
        "the-twenty-fourth-child",
    ],
}

COPY = {
    "en": {
        "title": "The Register",
        "kicker": "Seven stories, one institution",
        "lede": ("A standing office exists to register events that had no witness. "
                 "Seven novels are seven of its files."),
        "paras": [
            ("The office has no building you can visit. It has a rule instead: if something "
             "happened and nobody saw it, somebody still has to write it down, in ink, in order, "
             "with a date at the top. Every story in this series is one of those entries, "
             "and every entry outlives the person who made it."),
            ("The objects differ — a harbour ledger, a compartment manifest, twelve blank iron "
             "tags, a delivery receipt, a language's death certificate, a station register "
             "paragraph, a school attendance book with one mark too many — but the hand is the "
             "same. That is the only thing the seven volumes "
             "share, and it is enough: a record kept honestly is a claim that the thing "
             "happened, whether or not the world still has room for it."),
        ],
        "order_title": "Reading order",
        "order_note": ("Each volume stands alone. Read them in any order; read them in this "
                       "one and the handwriting starts to show."),
        "volume": "Volume {n} of {total}",
        "volume_short": "Volume {n}",
        "connect_title": "In the Register",
        "back_series": "The Register",
        "all_novels": "All novels",
    },
    "tr": {
        "title": "Kütük",
        "kicker": "Yedi hikâye, tek kurum",
        "lede": ("Tanığı olmayan olayları kayda geçirmek için kurulmuş bir daire var. "
                 "Yedi roman, onun yedi dosyası."),
        "paras": [
            ("Dairenin gezilecek bir binası yok. Bir kuralı var: bir şey olduysa ve kimse "
             "görmediyse, biri yine de onu yazmak zorunda — mürekkeple, sırayla, en üstte "
             "tarihle. Bu dizideki her hikâye o kayıtlardan biri ve her kayıt, onu tutan "
             "kişiden daha uzun yaşıyor."),
            ("Nesneler değişiyor — bir liman defteri, bir bölme manifestosu, on iki boş demir "
             "plaka, bir teslim makbuzu, bir dilin ölüm belgesi, bir istasyon kütüğü paragrafı, "
             "bir fazla çentikli bir okul yoklama defteri — ama el aynı. Yedi cildin paylaştığı "
             "tek şey bu ve yetiyor: dürüstçe tutulmuş "
             "bir kayıt, dünyada artık yer kalmamış olsa da o şeyin olduğunu iddia eder."),
        ],
        "order_title": "Okuma sırası",
        "order_note": ("Her cilt tek başına durur. İstediğiniz sırayla okuyun; bu sırayla "
                       "okursanız el yazısı görünmeye başlar."),
        "volume": "{total} cildin {n}.",
        "volume_short": "{n}. cilt",
        "connect_title": "Kütük'te",
        "back_series": "Kütük",
        "all_novels": "Tüm romanlar",
    },
    "ko": {
        "title": "등록부",
        "kicker": "일곱 편의 이야기, 하나의 기관",
        "lede": ("목격자가 없던 사건을 등록하기 위해 존재하는 상설 부서가 있다. "
                 "일곱 편의 소설은 그 부서의 서류 일곱 건이다."),
        "paras": [
            ("그 부서에는 견학할 건물이 없다. 대신 규칙이 하나 있다. 어떤 일이 일어났는데 "
             "아무도 보지 못했다면, 누군가는 여전히 그것을 적어야 한다. 잉크로, 순서대로, "
             "맨 위에 날짜를 붙여서. 이 시리즈의 모든 이야기는 그 기록 중 하나이고, 모든 "
             "기록은 그것을 적은 사람보다 오래 산다."),
            ("대상은 달라진다. 항구 장부, 격실 명세서, 이름 없는 철제 명찰 열둘, 배송 "
             "영수증, 한 언어의 사망 증명서, 관측소 대장의 한 문단, 한 칸이 더 찍힌 학교 "
             "출석부. 그러나 필체는 같다. 일곱 권이 공유하는 것은 그것뿐이고, 그것으로 충분하다. 정직하게 남긴 기록은 "
             "세상에 그 자리가 더 이상 없더라도 그 일이 있었다고 주장한다."),
        ],
        "order_title": "읽는 순서",
        "order_note": ("각 권은 따로 완결된다. 아무 순서로 읽어도 되지만, 이 순서로 읽으면 "
                       "필체가 보이기 시작한다."),
        "volume": "{total}권 중 {n}권",
        "volume_short": "{n}권",
        "connect_title": "등록부 안에서",
        "back_series": "등록부",
        "all_novels": "모든 소설",
    },
    "yue": {
        "title": "登記冊",
        "kicker": "七個故事，一個機構",
        "lede": ("有個常設部門，專門登記「冇人見到」嘅事。六部小說，就係佢六宗檔案。"),
        "paras": [
            ("呢個部門冇一棟你參觀得到嘅樓。佢只有一條規矩：一件事發生過、而冇人見到，"
             "都仲要有人用墨寫低，按次序寫，頂頭寫日期。呢個系列每個故事都係其中一條紀錄，"
             "而每條紀錄都比寫佢嗰個人活得久。"),
            ("對象個個唔同——一本港口簿、一份艙格艙單、十二塊冇名嘅鐵牌、一張冇人簽收嘅"
             "送貨回執、一份開畀一種將死語言嘅死亡證明、一段幫水底小鎮補登嘅觀測站條目、"
             "一本多咗一格嘅點名簿——但隻字係同一隻手。七卷共用嘅就係呢樣，而已經夠："
             "老實寫低嘅紀錄，就算個世界"
             "已經冇位擺佢，都仍然係話「件事真係發生過」。"),
        ],
        "order_title": "閱讀次序",
        "order_note": ("每卷自己企得住。點讀都得；但照呢個次序讀，隻手就會慢慢現形。"),
        "volume": "{total}卷中第 {n} 卷",
        "volume_short": "第 {n} 卷",
        "connect_title": "喺登記冊入面",
        "back_series": "登記冊",
        "all_novels": "全部小說",
    },
}

# 六部各一句：在系列里它是哪一宗案卷、留下哪件物件。
CONNECT = {
"the-salt-ledger": {
"en": ("Case one: a harbour ledger that runs nine days ahead of the sea. The series starts here "
       "because it is the oldest surviving entry — a record written before the event, by a man "
       "whose honesty the village depended on."),
"tr": ("Birinci dosya: denizden dokuz gün ileriden giden bir liman defteri. Dizi burada başlıyor "
       "çünkü bu, en eski kayıt — olaydan önce yazılmış, dürüstlüğüne köyün güvendiği bir adamın elinden."),
"ko": ("첫 번째 서류: 바다보다 아흐레 앞서가는 항구 장부. 시리즈가 여기서 시작하는 이유는 이것이 "
       "가장 오래 남은 기록이기 때문이다. 사건보다 먼저 쓰였고, 마을이 그 정직함을 믿었던 사람의 손에서."),
"yue": ("第一宗檔案：一本比海行快九日嘅港口簿。系列由呢度開始，因為佢係最舊嘅一條紀錄——"
        "喺件事發生之前就寫低，寫佢嘅人，全村都信佢老實。"),
},
"nine-minutes-of-static": {
"en": ("Case two: a compartment signed for by someone who is not on the manifest. The station's "
       "log is the second surviving entry, and the first one written in a hand that expected "
       "nobody to read it."),
"tr": ("İkinci dosya: manifestoda olmayan biri tarafından imzalanmış bir bölme. İstasyonun "
       "defteri, hayatta kalan ikinci kayıt ve kimsenin okumayacağını varsayan bir elle yazılmış ilk kayıt."),
"ko": ("두 번째 서류: 명세서에 없는 사람이 서명한 격실. 정거장의 일지는 두 번째로 남은 기록이고, "
       "아무도 읽지 않을 것이라 여긴 손으로 쓰인 첫 기록이다."),
"yue": ("第二宗檔案：一個由唔喺艙單上嘅人簽名嘅艙格。太空站嘅日誌係第二條留存紀錄，"
        "亦係第一條用「冇人會讀」嘅心態寫落去嘅紀錄。"),
},
"the-bone-orchard": {
"en": ("Case three: twelve iron tags with no names on them. Owning them is what makes the orchard "
       "a record rather than a weather event — which is exactly what the office exists to prevent."),
"tr": ("Üçüncü dosya: üzerinde isim olmayan on iki demir plaka. Onlara sahip olmak, bahçeyi bir "
       "hava olayı değil bir kayıt yapan şey — dairenin tam olarak engellemek için var olduğu şey."),
"ko": ("세 번째 서류: 이름이 없는 철제 명찰 열둘. 그것을 갖고 있다는 것이 과수원을 날씨 현상이 아니라 "
       "기록으로 만든다. 그 부서가 바로 그것을 막기 위해 존재한다."),
"yue": ("第三宗檔案：十二塊冇名嘅鐵牌。有呢啲牌，果園先至算係一份紀錄，唔係一場天氣現象——"
        "而個部門就係為咗防止呢種事而存在。"),
},
"sunday-repeated": {
"en": ("Case four: a receipt for a parcel nobody signed for, delivered to an address that is real "
       "for nineteen minutes a week. The office files it as a delivery, because refusing it would "
       "mean the address never existed."),
"tr": ("Dördüncü dosya: haftada on dokuz dakika gerçek olan bir adrese teslim edilmiş, kimsenin "
       "imzalamadığı bir paketin makbuzu. Daire bunu teslim olarak kaydediyor; reddetmek adresin "
       "hiç var olmadığını kabul etmek olurdu."),
"ko": ("네 번째 서류: 한 주에 십구 분만 실제인 주소로 배달된, 아무도 서명하지 않은 소포의 영수증. "
       "부서는 이것을 배달로 기록한다. 거절한다는 것은 그 주소가 존재한 적 없다고 인정하는 일이니까."),
"yue": ("第四宗檔案：一張冇人簽收嘅包裹回執，送去一個每星期只真實存在十九分鐘嘅地址。"
        "部門照樣入檔做「已送達」，因為唔收，就等於話嗰個地址從來冇存在過。"),
},
"the-last-translator": {
"en": ("Case five: a death certificate for a language that is still being spoken. The office keeps "
       "both versions — the one that was signed and the one that was refused — in the same file."),
"tr": ("Beşinci dosya: hâlâ konuşulan bir dil için düzenlenmiş ölüm belgesi. Daire iki versiyonu "
       "da aynı dosyada tutuyor: imzalananı ve reddedileni."),
"ko": ("다섯 번째 서류: 아직 말해지고 있는 언어의 사망 증명서. 부서는 서명된 것과 거절된 것, 두 판본을 "
       "같은 파일에 보관한다."),
"yue": ("第五宗檔案：一份仲有人講嘅語言嘅死亡證明。部門兩個版本都留住——簽咗嗰份，同埋拒簽嗰份——"
        "擺喺同一宗檔案。"),
},
"weather-for-a-town-that-isnt-there": {
"en": ("Case six: a station register entry for a town under fifteen metres of water. It is the "
       "newest file, and the only one where the office had to reopen a closed entry and give it "
       "a number that the model could find."),
"tr": ("Altıncı dosya: on beş metre suyun altındaki bir kasaba için istasyon kütüğü kaydı. En yeni "
       "dosya ve dairenin kapatılmış bir kaydı yeniden açıp modele bulunabilir bir numara vermek "
       "zorunda kaldığı tek dosya."),
"ko": ("여섯 번째 서류: 십오 미터 물 아래 있는 마을의 관측소 대장 항목. 가장 최근 파일이며, "
       "부서가 닫힌 기록을 다시 열어 모델이 찾을 수 있는 번호를 부여해야 했던 유일한 사례다."),
"yue": ("第六宗檔案：一段幫一個沉喺十五米水下嘅鎮補登嘅觀測站條目。係最新一宗檔案，"
        "亦係部門唯一一次要打開一條已經封咗嘅紀錄，畀返個模型搵得到嘅編號。"),
},
"the-twenty-fourth-child": {
"en": ("Case seven: a school attendance book with one mark too many, kept for a hundred and eleven "
       "years on behalf of a child who was buried in 1911. It is the only file in the series where "
       "somebody eventually wrote the name in the margin, and the hand that wrote it was in the room."),
"tr": ("Yedinci dosya: 1911'de defnedilen bir çocuk adına yüz on bir yıl boyunca tutulmuş, bir "
       "çentiği fazla bir okul yoklama defteri. Dizide birinin sonunda adı kenara yazdığı tek dosya "
       "ve o adı yazan el odadaydı."),
"ko": ("일곱 번째 서류: 1911년에 묻힌 아이를 대신해 백십일 년 동안 유지된, 한 칸이 더 찍힌 학교 "
       "출석부. 시리즈에서 누군가 결국 여백에 이름을 적은 유일한 파일이며, 그 이름을 적은 손은 "
       "그 방 안에 있었다."),
"yue": ("第七宗檔案：一本多咗一格嘅點名簿，替一個 1911 年落葬嘅細路，喺帳上留咗一百一十一年。"
        "係系列入面唯一一宗，最後有人喺邊位寫返個名——而寫嗰隻手，當時就喺課室入面。"),
},
}


def total() -> int:
    """本系列当前卷数。"""
    return len(SERIES["order"])


def label(language: str, slug: str) -> str:
    """「Volume N of M」这类卷次标注。"""
    return COPY[language]["volume"].format(n=volume(slug), total=total())


def short(language: str, slug: str) -> str:
    """只含卷次的短标注。"""
    return COPY[language]["volume_short"].format(n=volume(slug), total=total())


def volume(slug: str) -> int:
    """1-based 卷次；未登记的书返回 0。"""
    try:
        return SERIES["order"].index(slug) + 1
    except ValueError:
        return 0
