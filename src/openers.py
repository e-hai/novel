"""幕前场景：账簿体从第六部开始，每一部之前补一场不在账簿里的场景。

账簿是 Elias 自己写的，只记他愿意记下的东西；场景写的是他当天没写下的那部分。
每个场景挂在对应幕页上是正文，不占章节编号，也不改账簿的 Entry 序号。

结构：{幕序号: {"en": {...}, "tr": {...}, "ko": {...}, "yue": {...}}}
每语一个 {"title": 场景标题, "when": 日期行, "blocks": (段落, ...)}
段落支持 md_inline 的 **粗体** 与 *斜体*。
"""

OPENERS = {1: {'en': {'blocks': ['The bracket had been loose since the summer. On the first wet morning of October, '
                       'Elias carried a chair out to the front of the shop, stood on it, and tightened the '
                       'bolt with the spanner he had bought the week he opened.',
                       'The spanner had cost more than a spanner should, because it was the only tool in the '
                       'lane that fitted that bolt and the man who sold it knew it.',
                       'Two turns. He gave it a third because the second had not felt like enough. The metal '
                       'answered the way metal answers when it has been waiting all summer: it settled, and '
                       'then it was quiet.',
                       'The awning had been green in the year he opened. What it was now was the colour of a '
                       'thing that has been rained on for eleven years in a lane where nothing is replaced '
                       'until it falls.',
                       'Below him the lane did its morning. The bread seller at the end was wrapping the '
                       'unsold loaves, loosening each paper sleeve before tightening it again, a habit that '
                       'made the bread look handled and therefore wanted. A woman carried two chairs up the '
                       'hill and stopped twice to breathe. A dog with a bad back leg watched all of it from '
                       'under a cart and did not move.',
                       'People in the Ward saved everything that might still do one more job. Elias had once '
                       'thought of that as an economy. He had stopped thinking of it when he noticed that he '
                       'did it too.',
                       'Inside, the lamp was on over the bench and the loom was under a sheet, because nothing '
                       'was booked before eleven and a loom under a sheet makes a shop look like a shop that '
                       'is resting rather than a shop that is waiting.',
                       'He opened the drawer to check the rule sheet. He did not read it; he checked that it '
                       'was there, the way other men check that the stove is off.',
                       'Two lines in his own hand. *Do not repair your own engrams.* Under it, added a year '
                       'later: *Do not make a whole where two people were.*',
                       'The sheet had no date and no signature and no second reader. He had decided, some '
                       'years ago, that this was not the same as having no rule.',
                       'Eleven years in the trade. He counted it in what people brought him rather than in '
                       'years: cores in paper sleeves, cores in cloth, once a photograph used as a lid over '
                       'the thing itself. Most came to have something taken out. The ones who came to have '
                       'something put back were fewer, and they had almost always been polite about it the '
                       'first time.',
                       'At nine a young man came in with a Thursday he wanted removed. He said it the way men '
                       'say a thing they have rehearsed: a Thursday, a room, a name he would not give.',
                       'Elias quoted him a price. The young man said it was a lot for one day.',
                       "“It isn't the day,” Elias said. “It's the day it takes me. Fill has to be laid along "
                       "the edge of what's missing, by hand. Four hours, if the edge is clean.”",
                       "“And then it's gone?”",
                       "“Then there's a shape where the Thursday was. You'll know something happened on a "
                       "Thursday. You won't know what.”",
                       'The young man looked at the price sheet on the wall as if it had been unfair to him '
                       'personally. He said he would think about it. People who say they will think about it '
                       "are usually asking whether they can afford to keep the thing, and in Elias's "
                       'experience the answer was usually yes. The ones who could not afford it came back '
                       'inside the week.',
                       'He wrote the quote in the intake book and closed it. *Quoted, not taken.* It was the '
                       'fourth of those that month, and the only one he remembered afterwards.',
                       "The rain stopped being rain and became the lane's light, which is what rain does on "
                       'Cinder Lane at ten in the morning: it goes grey, and then it becomes the colour of '
                       'everything that is wet.',
                       'He stood at the counter with the spanner still in his hand and thought about the '
                       'sentence he said to customers, the one the Ward had taught him and the one he still '
                       'believed: *a repairman is paid to stop the falling, not to decide what the customer '
                       'should keep.* It was true. It was also the sentence that let him do the work at all.',
                       'Once a customer had asked whether a repair changed the person. He had given her the '
                       'sentence. She paid, and went out into the rain, and he had stood where he was standing '
                       'now with the feeling that he had answered a different question than the one she asked. '
                       'He thought about it about once a week. That is often enough to call it a habit.',
                       'At eleven the bell above the door went, and it was an old man with a coat that had '
                       'three different buttons and a folded square of cloth in his hand; and Elias '
                       'understood, before a word was said, that the cloth was the job, and that the core was '
                       'only the way in.'],
            'title': 'The Awning',
            'when': 'early October'},
     'ko': {'blocks': ['브래킷은 여름 내내 느슨해져 있었다. 10월의 첫 비 오는 아침, Elias는 의자를 가게 앞으로 내놓고 그 위에 올라서서, 가게를 연 그 주에 산 '
                       '스패너로 볼트를 조였다.',
                       '스패너는 스패너 한 자루값보다 비쌌다. 그 볼트에 맞는 공구가 이 거리에는 그것뿐이었고, 그것을 팔던 남자도 그 사실을 알고 있었기 때문이었다.',
                       '두 바퀴를 돌렸다. 둘째 바퀴가 충분하지 않게 느껴져 셋째를 더 돌렸다. 금속은 여름 내내 기다려 온 금속이 대답하는 방식으로 대답했다: 자리를 잡고, '
                       '그리고 그 뒤 조용해졌다.',
                       '차양은 가게를 연 해에는 녹색이었다. 지금 그것의 색은, 떨어져 나가기 전까지는 아무것도 바꾸지 않는 이 거리에서 열한 해를 비에 맞은 물건의 색이었다.',
                       '그 아래에서는 거리가 제 아침을 보내고 있었다. 거리 끝의 빵장수는 팔리지 않은 빵들을 싸고 있었고, 종이 소매를 하나하나 풀었다가 다시 조이는 습관을 '
                       '반복해, 빵이 만져진 것처럼, 따라서 찾는 사람이 있는 것처럼 보이게 했다. 여자는 의자 두 개를 언덕 위로 나르며 두 번이나 멈춰 숨을 고랐다. 뒷다리가 '
                       '좋지 않은 개는 수레 아래에서 그 모든 것을 지켜보며 움직이지 않았다.',
                       '관리청 사람들은 아직 한 번 더 쓸 수 있는 것은 무엇이든 모아 두었다. Elias는 한때 그것을 절약이라고 생각했다. 자기 역시 그렇게 하고 있다는 것을 '
                       '눈치챘을 때, 그는 그 생각을 멈췄다.',
                       '안에서는 작업대 위의 등이 켜져 있었고 직조기는 천으로 덮여 있었다. 열한 시 전에는 예약이 잡히지 않았고, 천으로 덮인 직조기는 가게를 기다리는 '
                       '가게라기보다 쉬고 있는 가게처럼 보이게 했다.',
                       '서랍을 열어 규칙 종이를 확인했다. 읽은 것이 아니라, 다른 사람들이 난로가 꺼졌는지 확인하듯이, 그것이 거기에 있는지만 확인했다.',
                       '자기 필체로 두 줄이 적혀 있었다. *자기 엔그램을 수리하지 마.* 그 아래, 일 년 뒤에 더한 줄: *두 사람이 있던 자리에 완전함을 만들지 마.*',
                       '종이에는 날짜도, 서명도, 두 번째 독자도 없었다. 몇 해 전에 그는 이것이 규칙이 없는 것과는 같지 않다고 판단했다.',
                       '업계에 열한 해를 보냈다. 해수로 세기보다 사람들이 자기에게 가져오는 것으로 그 시간을 헤아렸다: 종이 소매에 든 코어, 천에 싼 코어, 한번은 그 물건 '
                       '그것 위에 뚜껑처럼 얹힌 사진도 있었다. 대부분은 무언가를 빼내러 왔다. 무언가를 다시 넣으러 오는 사람은 더 적었고, 그들은 거의 언제나 첫 번째에는 '
                       '정중했다.',
                       '아홉 시에 젊은 남자가 지우고 싶은 목요일을 안고 들어왔다. 연습을 마친 말을 하는 사람이 말하는 방식으로 말했다: 목요일, 방, 끝내 주지 않은 이름.',
                       'Elias는 그에게 값을 불렀다. 젊은 남자는 하루 치고는 많은 액수라고 말했다.',
                       '“하루가 문제가 아니다.” Elias가 말했다. “내가 잡아먹히는 하루가 문제다. 채움은 손으로, 빠진 것의 가장자리를 따라 놓아야 한다. 가장자리가 '
                       '깨끗하면 네 시간이다.”',
                       '“그러면 그게 사라지나?”',
                       '“그러면 목요일 자리에 형태만 남는다. 목요일에 무슨 일이 있었는지는 알게 된다. 무엇이었는지는 모른다.”',
                       '젊은 남자는 벽에 붙은 가격표가 자기 개인에게 불공평하기라도 한 듯 쳐다보았다. 생각해 보겠다고 말했다. 생각해 보겠다고 하는 사람은 대개 그 물건을 둘 '
                       '형편이 되는지 묻는 것이었고, Elias의 경험상 그 대답은 대개 그렇다는 것이었다. 둘 형편이 안 되는 사람은 그 주 안에 다시 돌아왔다.',
                       '견적을 접수 장부에 적고 장부를 닫았다. *견적만 내고 안 맡김.* 그달 네 번째 건이었고, 뒤에 기억에 남은 유일한 건이었다.',
                       '비는 비라는 것을 멈추고 거리의 빛이 되었다. 열 시의 Cinder Lane에서 비가 늘 그렇듯이: 회색으로 바뀌었다가 젖은 모든 것의 색이 되었다.',
                       '스패너를 든 채 카운터에 서서, 손님에게 하는 그 문장을 생각했다. 관리청이 가르쳐 주었고 지금도 믿는 그 문장: *수리공은 떨어지는 것을 멈추게 하는 '
                       '대가를 받지, 손님이 무엇을 남겨야 할지 정하는 대가를 받지 않는다.* 그 말은 사실이었다. 그 문장 덕분에 일을 할 수 있기도 했다.',
                       '한때 어떤 손님이 수리가 그 사람을 바꾸는지 물은 적이 있었다. 그는 그 문장을 그녀에게 주었다. 여자는 값을 치르고 비 속으로 나갔고, 그는 지금 서 '
                       '있는 바로 그 자리에 서서, 자기가 물음과는 다른 질문에 대답한 기분을 느꼈다. 일주일에 한 번쯤 그것을 생각했다. 그 정도면 습관이라 부를 만했다.',
                       '열한 시에 문 위의 종이가 울렸다. 단추가 셋 다 다른 코트를 입고, 접은 네모난 천 조각을 손에 든 노인이었다. 말이 한마디 나오기 전에 Elias는 '
                       '알았다: 그 천이 작업이고, 코어는 그냥 들어가는 방식일 뿐이라는 것을.'],
            'title': '차양',
            'when': '10월 초'},
     'tr': {'blocks': ["Braket yazdan beri gevşek duruyordu. Ekim'in ilk yağışlı sabahında Elias dükkânın "
                       'önüne bir sandalye çıkardı, üzerine çıktı ve cıvatayı, dükkânı açtığı hafta aldığı '
                       'İngiliz anahtarıyla sıktı.',
                       'Anahtarın fiyatı bir anahtara yakışandan fazlaydı; çünkü sokakta o cıvataya uyan tek '
                       'alet oydu ve satan adam da bunu biliyordu.',
                       'İki tur. İkincisi yeterli gelmediği için bir tur daha çevirdi. Metal, bütün yaz '
                       'beklemiş bir metalin cevabını verdi: oturdu, sonra sustu.',
                       'Tente, dükkânı açtığı yıl yeşildi. Şimdiki rengi, on bir yıldır yağmur altında kalmış '
                       'bir şeyin rengiydi; bu sokakta hiçbir şey düşmeden değiştirilmez.',
                       'Altında sokak sabahını yaşıyordu. Sonundaki ekmek satıcısı satılmayan somunları '
                       'sarıyordu; her kâğıt kılıfı önce gevşetip yeniden sıkıyordu, bu alışkanlık ekmeğe el '
                       'değmiş, dolayısıyla istenmiş bir görünüm veriyordu. Bir kadın tepeye iki sandalye '
                       'taşıyordu, nefes almak için iki kez durdu. Arka bacağı bozuk bir köpek bunu bir '
                       'arabanın altından izliyor, kıpırdamıyordu.',
                       "Koruma Dairesi'nde insanlar bir işe daha yarayabilecek her şeyi saklardı. Elias bir "
                       'zamanlar bunu bir tasarruf sanmıştı. Kendisinin de aynı şeyi yaptığını fark edince bu '
                       'düşünceden vazgeçti.',
                       'İçeride lamba çalışma tezgâhının üzerinde yanıyordu; dokuma tezgâhı örtünün '
                       'altındaydı. On bire kadar randevu yoktu, örtü altındaki bir tezgâh da dükkânı bekleyen '
                       'değil dinlenen bir dükkân gibi gösterir.',
                       'Çekmeceyi açıp kural kâğıdını kontrol etti. Okumadı; yalnızca orada olduğunu '
                       'doğruladı, diğer adamların sobanın kapalı olup olmadığını kontrol edişi gibi.',
                       "Kendi el yazısıyla iki satır. *Kendi engram'larını onarma.* Altında, bir yıl sonra "
                       'eklenmiş: *İki insanın bulunduğu yerde bütün yaratma.*',
                       'Kâğıtta tarih yoktu, imza yoktu, ikinci okur yoktu. Yıllar önce bunun kuralın '
                       'olmamasıyla aynı şey olmadığına karar vermişti.',
                       'Meslekte on bir yıl. Bunu yıl yıl değil, insanların getirdikleriyle sayardı: kâğıt '
                       'kılıf içindeki çekirdekler, bez içindekiler, bir keresinde çekirdeğin üstüne kapak '
                       'diye konmuş bir fotoğraf. Çoğu bir şeyin çıkarılması için gelirdi. Geri konulması için '
                       'gelenler daha azdı ve neredeyse her seferinde ilk seferinde nazik davranırlardı.',
                       'Dokuzda genç bir adam girdi, çıkartılmasını istediği bir Perşembeyle. Bunu prova etmiş '
                       'birinin söylenişiyle söyledi: bir Perşembe, bir oda, vermek istemediği bir ad.',
                       'Elias fiyat söyledi. Genç adam bir gün için bunun fazla olduğunu söyledi.',
                       '“Söz konusu gün değil,” dedi Elias. “Benim ayıracağım gün. Dolgu, eksik olanın '
                       'kenarına elle döşenmeli. Kenar temizse dört saat.”',
                       '“Sonra o gün gider mi?”',
                       "“Perşembenin olduğu yerde bir şekil kalır. Bir Perşembe'de bir şey olduğunu bilirsin. "
                       'Ne olduğunu bilmezsin.”',
                       'Genç adam duvardaki fiyat listesine baktı, sanki liste kendisine karşı haksızlık etmiş '
                       'gibi. Düşüneceğini söyledi. Düşüneceğini söyleyenler genellikle o şeyi tutup '
                       "tutamayacaklarını soruyorlardı ve Elias'ın deneyimine göre cevap genellikle evet "
                       'oluyordu. Tutamayanlar o hafta içinde geri dönerdi.',
                       'Sözleştiği fiyatı kayıt defterine yazıp kapattı. *Fiyat verildi, iş alınmadı.* O ay '
                       'bunun dördüncüsüydü ve sonradan hatırladığı tek oydu.',
                       "Yağmur yağmur olmaktan çıktı, sokak ışığına dönüştü; sabah onda Cinder Lane'de "
                       'yağmurun yaptığı budur: önce grileşir, sonra ıslak olan her şeyin rengine bürünür.',
                       'Elinde anahtarla tezgâhın önünde durdu ve müşterilere söylediği cümleyi düşündü; '
                       "Koruma Dairesi'nin öğrettiği ve hâlâ inandığı cümleyi: *onarımcıya düşmeyi durdurması "
                       'için ödenir, müşterinin neyi tutması gerektiğine karar vermesi için değil.* Doğruydu. '
                       'Ama işi yapmasını sağlayan cümle de oydu.',
                       'Bir keresinde bir müşteri onarımın kişiyi değiştirip değiştirmediğini sormuştu. Ona o '
                       'cümleyi vermişti. Kadın ödedi, yağmurun dışına çıktı; Elias şimdi durduğu yerde '
                       'durmuş, kendisine sorulan sorudan başka bir soruya cevap vermiş gibi hissetmişti. Bunu '
                       'haftada bir kez kadar düşünüyordu. Bir alışkanlık demek için bu sıklık yeterdi.',
                       'On birde kapının üstündeki zil çaldı; içeri üç farklı düğmesi olan bir ceket giymiş, '
                       'elinde katlanmış kare bir kumaş olan yaşlı bir adam girdi. Daha tek kelime '
                       'konuşulmadan Elias anladı: iş kumaştı, çekirdek yalnızca içeri girme yoluydu.'],
            'title': 'Tente',
            'when': 'ekim başı'},
     'yue': {'blocks': ['支架由夏天開始就鬆。十月落雨嘅第一朝，Elias 搬張櫈出到鋪頭門前，企上去，用開張鋪嗰個禮拜買嘅扳手擰實粒螺絲。',
                        '支扳手貴過一支扳手應該嘅價錢，因為成條巷得呢一件工具啱呢粒螺絲，賣嘢嘅人亦都知。',
                        '擰兩轉。第二轉覺得唔夠，佢再擰第三轉。金屬回應嘅方式，係等咗成個夏天嘅金屬先會有嘅方式：定咗落嚟，然後就靜晒。',
                        '開張嗰年簷篷係綠色。而家嘅顏色，係一樣嘢喺一條唔爛唔換嘅巷入面淋咗十一年雨之後嘅顏色。',
                        '佢下面，條巷做緊朝早嘅事。巷尾賣包嘅人包緊賣剩嘅麵包，逐個紙套鬆開再收緊，呢個習慣令麵包好似畀人摸過，所以似係有人要嘅。一個女人攞住兩張櫈上山，停低兩次唞氣。一隻後腿有問題嘅狗喺車底望住呢一切，郁都冇郁。',
                        '管理局入面嘅人，乜都留，只要仲可以多用一次。Elias 曾經當呢樣係慳家。後來佢發現自己都係咁，就唔再咁諗。',
                        '入面，工作檯上面盞燈開住，織機蓋住塊布，因為十一點之前唔接單；蓋住布嘅織機，令間鋪睇落似係抖緊，而唔係等緊。',
                        '佢打開抽屜查對規條紙。佢冇讀；佢係確認張紙喺度，好似其他人查對爐有冇熄咁。',
                        '兩行自己嘅字。*唔好修補自己嘅 engram。* 下面，遲一年加上去：*唔好喺兩個人曾經喺度嘅地方造出一個完整。*',
                        '張紙冇日期、冇簽名、冇第二個讀者。幾年前佢已經決定，呢樣同冇規條唔係同一件事。',
                        '呢行做咗十一年。佢唔係用年數計，係用人家帶畀佢嘅嘢計：紙套入面嘅核、布包住嘅核，有一次仲係一張相，蓋喺樣嘢本身上面。多數人嚟係要択走啲嘢。嚟要放返啲嘢入去嘅少啲，而且第一次上門，幾乎都係客氣嘅。',
                        '九點，一個後生仔入嚟，帶住一個想択走嘅星期四。佢講嘅方式，似一個排練過嘅人講嘢：一個星期四、一間房、一個唔肯講嘅名。',
                        'Elias 畀咗個價。後生仔話，一日嘅事收咁多。',
                        '「唔係日頭嘅事，」Elias 話。「係呢件事使我嘅時間。填料要沿住缺失嘅邊緣人手鋪落去。邊緣乾淨嘅話，四個鐘。」',
                        '「咁之後就冇咗？」',
                        '「咁嗰個星期四嘅位置就剩低一個形。你會知有嘢喺星期四發生過；你唔會知係乜。」',
                        '後生仔望住牆上嘅價目表，好似張表對佢個人唔公平。佢話要諗諗先。講要諗諗先嘅人，通常係問自己負唔負擔得起留住件嘢；照 Elias '
                        '嘅經驗，答案多數係負擔得起。負擔唔起嘅，一個禮拜之內會再返嚟。',
                        '佢將報價寫入簿，合埋。*報咗價，冇做。* 呢個係月內第四單咁嘅嘢，亦係事後唯一一個佢記得嘅。',
                        '雨唔再係雨，變成條巷嘅光；朝早十點，Cinder Lane 嘅雨就係咁：先變灰，然後變成所有濕嘅嘢嘅顏色。',
                        '佢企喺櫃面，手仲拎住支扳手，諗起佢同客人講嘅嗰句說話——管理局教佢、而佢到而家仲信嘅嗰句：*修補師收錢係為咗擋住跌落嚟，唔係替客人決定佢應該留低啲乜。* '
                        '係真嘅。亦係呢句說話令佢可以做到呢份工。',
                        '有一次一個客人問，修補會唔會改變一個人。佢畀咗佢嗰句說話。佢畀錢，走入雨入面；佢企喺而家企嘅位置，覺得自己答咗另一條問題，唔係佢問嘅嗰條。佢大概一個禮拜諗起一次。呢個次數，已經夠稱得上係習慣。',
                        '十一點，門上個鈴響。係個老伯，件褸有三粒唔同嘅鈕，手入面拎住一塊摺埋嘅方布；一句說話都未講，Elias 已經明：塊布先係件工，粒核只係入場嘅路。'],
             'title': '簷篷',
             'when': '十月初'}},
 2: {'en': {'blocks': ['In the last week of October the rain stopped coming in showers and settled in, and the '
                       'shop stopped smelling of iron in the morning and started smelling of wet paper.',
                       'Three jobs before ten. A woman with a core that had gone soft at one end; a man who '
                       "wanted his sister's voice taken out of a recording of a birthday; a boy who brought a "
                       'core with no label and could not say whose it was. The boy was sent away with a note '
                       'and no charge, because a core without a name is either a mistake or a thing that '
                       'should not be in a shop.',
                       'The man in work boots came at half past ten. He wanted a night at the plant taken out: '
                       'a press, a hand, and the two seconds before he hit the stop.',
                       'Elias asked the questions he had to ask. Whose memory: his. Who else is in it: a man '
                       'called Petrie, who had worked that press for nine years. Does Petrie know you are '
                       'here: no.',
                       '“Then I need his name on the job, or I need him not to be in it,” Elias said.',
                       'The man said Petrie was dead. April, at another plant, a different machine. He said it '
                       'flatly, the way men say a fact they have already had to say to a form.',
                       'Elias was quiet for a moment, because this was the part of the trade that no price '
                       'sheet mentions. The rule protects the living. A dead man is not living, so the rule '
                       'does not cover him, and the shop is allowed to lay fill across his face and call the '
                       'result a repair.',
                       "“I'll do it,” he said. “I'm not going to pretend that's clean.”",
                       'The work took four hours and three quarters of a brick. He finished lot 7734, and '
                       'wrote the lot number into the material book, because the Ward can ask what went into a '
                       'repair and the answer has to be a number and not a shrug.',
                       'He laid the fill the way that has no name in the manuals: not smoothing the edge, '
                       'following it, the way you follow a torn page with a finger before you mend it.',
                       'The press went out of the memory the way sound goes out of a room when a door closes '
                       'on it. What was left was the man standing at a panel with his hand on the stop, and '
                       'beside the press a shape where something had been that he could not name.',
                       'When he came out of it the man sat for a while and then said he felt lighter. Then he '
                       "asked whether Petrie's face was still there.",
                       '“The face stays,” Elias said. “I took the sound.”',
                       '“The sound was the worst of it.”',
                       'He paid in coins and left them in a row on the counter, the way people leave things '
                       'they do not want to pick up again. At the door he said, “If I come back in a month and '
                       "it isn't right?”",
                       '“Then we look at it again, and it costs less the second time, because the edge will '
                       'still be clean.”',
                       'The man nodded and did not come back in a month, or in a year.',
                       'Elias wrote the job up: date, name, price, material. Then he sat with the book open '
                       'and thought about the forms.',
                       'Every form in the trade has one direction. There is a line for what is to be removed '
                       'and a line for the reason, and there is no line for what is to be returned. Clinics '
                       'that promise the other direction print their own forms and call them restorative, and '
                       "the Ward's inspectors write those up as misdescription. He had once written *restore: "
                       'no form* in the margin of his own book, and then crossed it out, because a margin is '
                       'not a form either.',
                       'The rain did not stop. At two the lane went the colour of a held breath, and the shop, '
                       'which had done three jobs and one difficult one, sat there being a shop.'],
            'title': 'The Default Direction',
            'when': 'late October'},
     'ko': {'blocks': ['10월 마지막 주에 비는 소나기처럼 오다가 그칠 사이 없이 자리를 잡고 내렸다. 가게는 아침에 철 냄새가 나다가 젖은 종이 냄새가 났다.',
                       '열 시 전에 세 건이 있었다. 한쪽 끝이 물러진 코어를 든 여자; 생일 녹음에서 누이의 목소리를 빼내고 싶어 하는 남자; 표식 없는 코어를 가져와 그것이 '
                       '누구 것인지 말하지 못하는 소년이었다. 그 소년은 메모만 받고 값을 받지 않은 채 돌려보냈다. 이름 없는 코어는 실수이거나 가게에 있어서는 안 되는 것이기 '
                       '때문이었다.',
                       '작업화를 신은 남자가 열 시 반에 들어왔다. 그는 공장에서의 하룻밤을 빼내고 싶어 했다: 프레스, 손, 그리고 정지를 누르기 직전의 이 초.',
                       'Elias는 물어야 하는 질문을 물었다. 누구 기억인가: 자기 것이다. 다른 누가 그 안에 들어 있는가: 아홉 해를 그 프레스에서 일한 Petrie라는 '
                       '남자. Petrie는 당신이 여기 온 줄 아는가: 모른다.',
                       '“그러면 작업에 그 이름을 적거나, 그가 안에 있지 않아야 한다.” Elias가 말했다.',
                       '남자는 Petrie는 죽었다고 말했다. 4월, 다른 공장의 다른 기계였다. 그는 이미 양식에 적어야 했던 그 사실을 말하듯 담담하게 말했다.',
                       'Elias는 잠시 침묵했다. 가격표 어디에도 적히지 않은 업계의 부분이었기 때문이다. 규칙은 살아 있는 이를 지킨다. 죽은 사람은 살아 있지 않으므로 '
                       '규칙이 그를 덮지 않고, 가게는 그의 얼굴에 채움을 놓고 그 결과를 수리라 불러도 된다.',
                       '“해 주겠다.” 그가 말했다. “깨끗한 일이라고는 속이지 않겠다.”',
                       '일은 네 시간과 벽돌 사 분의 삼이 들었다. 로트 7734를 끝내고 그 로트 번호를 재료 장부에 적었다. 관리청이 수리에 무엇이 들어갔는지 물을 수 있고, '
                       '그 대답은 어깨짐이 아니라 숫자여야 하기 때문이었다.',
                       '채움은 설명서에 이름이 없는 방식으로 놓았다. 가장자리를 다듬지 않고 그것을 따라가는 방식이었다. 고치기 전에 찢긴 페이지를 손가락으로 더듬어 가듯이 '
                       '그렇게 했다.',
                       '프레스는 문이 그 방을 닫으며 소리가 방에서 빠져나가듯 기억에서 빠져나갔다. 남은 것은 패널 앞에 서서 손을 정지 버튼에 댄 남자와, 프레스 옆에 무엇이 '
                       '있었는지 자기 이름으로는 대지 못할 형태뿐이었다.',
                       '그것에서 나왔을 때 남자는 한동안 앉아 있다가 자신이 가벼워진다고 말했다. 그리고 Petrie의 얼굴이 그대로 거기에 남아 있는지 물었다.',
                       '“얼굴은 남는다.” Elias가 말했다. “소리를 빼냈다.”',
                       '“그 소리가 그중 가장 심했다.”',
                       '동전으로 값을 치르고 그것들을 카운터에 줄지어 놓았다. 다시 줍고 싶지 않은 것을 내려놓는 사람들의 방식이었다. 문가에 이르러 그는 말했다, “한 달 뒤에 '
                       '돌아왔는데 그것이 잘못돼 있으면?”',
                       '“그러면 다시 보기로 한다. 두 번째는 값이 적게 든다. 가장자리가 여전히 깨끗할 것이니까.”',
                       '남자는 고개를 끄덕였고, 한 달 뒤에도, 일 년 뒤에도 돌아오지 않았다.',
                       'Elias는 그 작업을 적었다: 날짜, 이름, 값, 재료. 그리고 장부를 펼친 채 앉아 양식들을 생각했다.',
                       '업계의 모든 양식은 방향이 하나다. 빼낼 것을 적는 칸과 그 이유를 적는 칸은 있어도, 되돌릴 것을 적는 칸은 없다. 그 반대 방향을 약속하는 클리닉은 '
                       '자기 양식을 인쇄해 복원이라 부르고, 관리청 심사관들은 그런 것을 허위 기재로 적는다. 그는 한때 자기 장부 여백에 *복원: 양식 없음* 이라고 적었다가 '
                       '지웠다. 여백 역시 양식은 아니기 때문이었다.',
                       '비는 그치지 않았다. 두 시에 거리는 숨을 참은 듯한 색이 되었고, 세 건과 어려운 한 건을 마친 가게는 가게인 채 그 자리에 앉아 있었다.'],
            'title': '기본 방향',
            'when': '10월 말'},
     'tr': {'blocks': ["Ekim'in son haftasında yağmur sağanak sağanak gelmeyi bıraktı, çöreklendi; dükkân "
                       'sabahları demir kokusunu yitirip ıslak kâğıt kokusu almaya başladı.',
                       'On olmadan önce üç iş. Bir ucundan yumuşamış bir çekirdeği olan kadın; doğum günü '
                       'kaydından kızkardeşinin sesini çıkartmak isteyen adam; etiketi olmayan ve kimin '
                       'olduğunu söyleyemeyen bir çekirdek getiren oğlan. Oğlan bir notla, ücret alınmadan '
                       'gönderildi; adsız bir çekirdek ya bir yanlıştır ya da dükkânda bulunmaması gereken bir '
                       'şey.',
                       'On buçukta iş botlu adam geldi. Fabrikada geçen bir geceyi çıkartmak istiyordu: bir '
                       'pres, bir el ve durdurma koluna basmadan önceki iki saniye.',
                       'Elias sorması gereken soruları sordu. Kimin belleği: kendisinin. İçinde başka kim var: '
                       'Petrie adında, o preste dokuz yıl çalışmış bir adam. Petrie buraya geldiğini biliyor: '
                       'hayır.',
                       '“O halde işte onun adını görmem gerekiyor, ya da o kayıtta bulunmaması gerekiyor,” '
                       'dedi Elias.',
                       "Adam Petrie'nin öldüğünü söyledi. Nisan'da, başka bir fabrikada, başka bir makinede. "
                       'Bunu bir forma yazmak zorunda kalmış birinin söylediği gibi, düz bir sesle söyledi.',
                       'Elias bir an sustu; çünkü bu, fiyat listelerinin anlatmadığı mesleğin parçasıydı. '
                       'Kural yaşayanları korur. Ölü bir adam yaşayan değildir, bu yüzden kural onu kapsamaz; '
                       'dükkân yüzüne dolgu döşeyip sonuca onarım diyebilir.',
                       '“Yapacağım,” dedi. “Bunun temiz olduğunu iddia etmeyeceğim.”',
                       'İş dört saat ve üç çeyrek tuğla dolgu aldı. 7734 parçasını bitirdi ve parti numarasını '
                       'malzeme defterine yazdı; Koruma Dairesi bir onarıma ne girdiğini sorabilir ve cevap '
                       'bir sayı olmalıdır, omuz silkme değil.',
                       'Dolgu, kılavuzlarda adı olmayan biçimde döşedi: kenarı düzleştirmeyip izleyerek, '
                       'yırtık bir sayfayı onarmadan önce parmakla izleyiş gibi.',
                       'Pres, bir kapının kapanmasıyla sesin odadan çıkışı gibi bellekten çıktı. Geriye '
                       'panelin başında duran, eli durdurma kolunda bir adam kaldı; presin yanında ise adı '
                       'koyamadığı bir şeyin bulunmuş olduğu yerdeki bir şekil.',
                       'İşten çıktığında adam bir süre oturdu, sonra kendini daha hafif hissettiğini söyledi. '
                       "Ardından Petrie'nin yüzünün hâlâ orada olup olmadığını sordu.",
                       '“Yüz kalıyor,” dedi Elias. “Sesi aldım.”',
                       '“En kötüsü o sesmiş.”',
                       'Bozuk paralarla ödedi ve onları tezgâhta sıra sıra bıraktı, insanların yeniden almak '
                       'istemedikleri şeyleri bırakışı gibi. Kapıda, “Bir ay sonra gelip de düzgün olmazsa?” '
                       'dedi.',
                       '“O halde bir daha bakarız; ikinci sefer ücreti daha az olur, çünkü kenar hâlâ '
                       'temizdir.”',
                       'Adam başını salladı; ne bir ay sonra ne de bir yıl sonra geri döndü.',
                       'Elias işi kaydetti: tarih, ad, fiyat, malzeme. Sonra defter açık oturup formları '
                       'düşündü.',
                       'Meslekteki her formun tek yönü vardır. Çıkartılacak şey için bir satır, gerekçe için '
                       'bir satır vardır; geri verilecek şey için satır yoktur. Karşı yönü vaat eden klinikler '
                       "kendi formlarını basar ve bunlara iade formu der; Koruma Dairesi'nin denetçileri "
                       'bunları yanlış tanım diye yazıya geçirir. Bir keresinde kendi defterinin kenar '
                       'boşluğuna *iade: form yok* yazmış, sonra üstünü çizmişti; çünkü kenar boşluğu da bir '
                       'form değildir.',
                       'Yağmur durmadı. İkide sokak tutulan bir nefesin rengine büründü; üç iş ve bir zor iş '
                       'yapmış olan dükkân, orada bir dükkân gibi oturuyordu.'],
            'title': 'Varsayılan Yön',
            'when': 'ekim sonu'},
     'yue': {'blocks': ['十月最後一個禮拜，雨唔再係一陣一陣咁落，係留低咗；朝早鋪頭唔再係鐵鏽味，變成濕紙味。',
                        '十點之前三單。一個女人，粒核一端變軟咗；一個男人，想將妹妹把聲由一段生日錄音入面択走；一個細路，帶嚟一粒冇標籤嘅核，講唔出係邊個嘅。細路攞住張紙走，唔使畀錢；冇名嘅核，唔係出錯，就係一樣唔應該出現喺鋪頭嘅嘢。',
                        '十點半，一個着工靴嘅男人入嚟。佢想択走工廠入面一晚嘅事：一部壓機、一隻手，同埋佢撳落停止掣之前嗰兩秒。',
                        'Elias 問咗一定要問嘅問題。係邊個嘅記憶：佢自己。入面仲有邊個：一個叫 Petrie 嘅男人，喺部壓機做咗九年。Petrie 知唔知你喺度：唔知。',
                        '「咁我要喺單上寫佢個名，唔係就要佢唔可以喺入面，」Elias 話。',
                        '男人話 Petrie 已經死咗。四月，另一間工廠，另一部機。佢講得平直，好似一個人將已經要填表講過嘅事再講一次。',
                        'Elias 靜咗一陣，因為呢部分係價目表唔會寫嘅行內事。規條保護生還嘅人。死人唔係生還嘅人，規條覆蓋唔到佢；鋪頭可以將填料鋪過佢塊面，然後當個結果係一次修補。',
                        '「我做，」佢話。「我唔會扮呢樣係乾淨嘅。」',
                        '件工做咗四個鐘，用咗四分之三塊磚。佢用完批次 7734，將批號寫入材料簿；管理局可以查一次修補用咗咩，答案要係一個編號，唔係一個攤手。',
                        '佢鋪填料嘅方式，手冊上面冇名：唔係抹平邊緣，係跟住邊緣行，好似補好一張撕爛嘅紙之前，先用手指跟住撕口行。',
                        '壓機由記憶入面消失，好似聲音由一間房隔住門之後消失咁。剩低嘅，係企喺面板前面、手按停止掣嘅男人；壓機旁邊，有一個形，原本有嘢喺度，佢叫唔出名。',
                        '完成之後，男人坐咗一陣，然後話覺得輕咗。跟住佢問，Petrie 塊面仲喺唔喺度。',
                        '「塊面留低，」Elias 話。「我択走咗把聲。」',
                        '「把聲先係最難頂嘅部分。」',
                        '佢用硬幣畀錢，排成一行放喺櫃面，好似人哋放低一啲唔想再執返嘅嘢咁。到門口佢話：「如果一個月後我返嚟，事態唔對呢？」',
                        '「咁我哋再睇一次；第二次平啲，因為邊緣仲會係乾淨嘅。」',
                        '男人點頭。一個月後冇返嚟，一年後都冇。',
                        'Elias 將件工記低：日期、個名、價錢、材料。然後攤開本簿坐住，諗起一張張表格。',
                        '呢行每張表格都得一個方向。有一格寫要択走咩，一格寫原因；冇一格寫要放返咩。承諾另一個方向嘅診所，自己印表格，叫佢哋做復原；管理局嘅審查員將呢啲寫成失實描述。佢曾經喺自己本簿嘅頁邊寫過 '
                        '*復原：冇表格*，然後劃走，因為頁邊亦唔係一張表格。',
                        '雨冇停。兩點，條巷變成一口憋住嘅氣嘅顏色；間鋪做咗三單、一單難嘅，坐喺度做返一間鋪。'],
             'title': '默認方向',
             'when': '十月尾'}},
 3: {'en': {'blocks': ['He wrote it at night with the shutter down, because a man writing to the archive does '
                       'not want to be seen doing it.',
                       'The form was two pages. The first asked what record, what classification, and on whose '
                       "claim. The second asked for the claimant's relationship to the record and left four "
                       'lines for the reason.',
                       'He filled the first page: the record number from the letter that had come in '
                       'September, the classification as it stood, and under *claimant*, his own name in '
                       'capitals, the way it appeared on the licence.',
                       'Then he stopped, because a claim is a thing that moves. His had moved once before, at '
                       'twenty-six, when he signed for a licence and believed that a licence was a kind of '
                       'permission. He had learned since that a licence is a kind of debt: it is held, it is '
                       'answered for, and once a year somebody reads what you did with it.',
                       'The second page. *Relationship to record: the subject.* Four lines for the reason, and '
                       'he used three and a half of them.',
                       'The reason was not the letter. The reason was a clerk at the archive counter in '
                       'September, who had looked at the file and said, without unkindness, that a file with '
                       'one signature can be closed without anybody reading it. She had said it the way people '
                       'say a thing they have said many times, and then she had looked up to see whether it '
                       'had landed. It had.',
                       'He went to the drawer for the rule sheet and read it standing up this time.',
                       'He had been to the archive four times in eleven years, and each time he had come away '
                       'with the feeling of a building that had been built to hold paper and had later been '
                       'asked to hold people. The reading room was on the ninth floor, and the lift had a sign '
                       'about quiet that was older than the lift.',
                       "The letter in September had not been a summons. It was a notice, in the archive's flat "
                       'language, that the file had been placed at rest, which meant that it existed, that it '
                       'had been read once, and that it would not be read again unless somebody claimed it.',
                       'Reclassification meant the file would move. A file that moves is read at three desks, '
                       'and each desk writes initials in a different corner, and at the end of it the file has '
                       'a history of being looked at. That was all he wanted, he told himself: not a finding, '
                       'not a verdict, only the initials of people who had read it.',
                       'He wrote in the blue ink the archive asked for, with the pen he used for the rule '
                       'sheet, which meant that the two documents in his life were in the same hand.',
                       '*Do not repair your own engrams. Do not make a whole where two people were.*',
                       'Nine years of reading it, and he had never noticed what it did not say. It did not say '
                       'who had agreed to it. It did not say when it had been decided. It was a rule written '
                       'by one person, kept in a drawer, witnessed by nobody; and he had been its only reader '
                       'and its only judge, which is a polite way of saying he had been its only subject.',
                       'He thought about writing a third line. *Do not be the only reader of your own rule.* '
                       'He did not write it, because a line written alone is exactly the thing he was '
                       'complaining about, and because a man who writes his own oversight clause has not '
                       'understood the problem.',
                       'What Mara had described that week was a protocol: a second person beside the loom, '
                       'whose job was not to watch him but to be an account of the fill, so that the fill '
                       'could not quietly become the memory. He had built it for customers in an afternoon. He '
                       'had built nothing for himself in eleven years.',
                       'He signed the second page at the bottom, small and level, and left the date for the '
                       'counter clerk to fill in, because he did not want the date in his own hand.',
                       'Then he carried the packet out and stood it against the lamp on the till, where the '
                       'morning would have to move it in order to open the drawer.',
                       'The rain started before he had the second lamp off. It came flat along the lane and '
                       'hit the metal awning with a sound like handfuls of grit, and the smell of wet iron '
                       'came in under the door and stayed.',
                       'He left the packet standing. A thing left standing is a thing that has to be dealt '
                       'with; he had learned that from eleven years of customers who left things on his '
                       'counter and came back for them in their own time.'],
            'title': 'The Packet',
            'when': 'a night in November'},
     'ko': {'blocks': ['그는 셔터를 내린 밤에 그것을 썼다. 기록보관소에 글을 쓰는 사람은 자기가 그렇게 하는 모습을 보이고 싶지 않기 때문이었다.',
                       '양식은 두 장짜리였다. 첫 장에는 어떤 기록인지, 어떤 분류인지, 누구의 청구인지를 물었다. 둘째 장에는 청구인과 그 기록의 관계를 묻고, 이유를 적을 네 '
                       '줄을 남겼다.',
                       '첫 장을 채웠다. 9월에 온 편지에 적힌 기록 번호, 현재 그대로의 분류, 그리고 *청구인* 칸 아래에는 면허에 나온 대로 자기 이름을 대문자로 적었다.',
                       '그러다 그는 멈췄다. 청구는 움직이는 성질의 것이기 때문이었다. 자기 것은 스물여섯에 한 번 움직인 적이 있었다. 면허에 서명하고 면허가 일종의 허가라고 '
                       '믿었을 때였다. 그 뒤로 배운 바로는 면허는 일종의 빚이라는 것이었다. 보유하고, 그것에 대해 책임지고, 해마다 누군가 그것을 어떻게 썼는지 읽어 본다.',
                       '둘째 장이었다. *기록과의 관계: 대상자.* 이유를 적을 네 줄 중 삼 줄 반을 썼다.',
                       '이유는 편지가 아니었다. 9월에 기록보관소 카운터에 있던 직원이었다. 서류철을 넘겨보고 불친절하지 않은 투로, 서명 하나뿐인 서류철은 아무도 읽지 않아도 '
                       '닫을 수 있다고 말한 사람이었다. 그녀는 여러 번 해 본 말을 하는 방식으로 말한 뒤, 그 말이 제자리에 닿았는지 보려고 고개를 들었다. 말은 닿아 '
                       '있었다.',
                       '그는 서랍으로 가 규칙 종이를 꺼내, 이번에는 서서 그 규칙 종이를 읽었다.',
                       '열한 해 동안 그는 기록보관소에 네 번 갔다. 갈 때마다 종이를 담으라고 지어진 건물이 나중에 사람까지 담게 해 달라는 요청을 받은 듯한 느낌을 안고 '
                       '돌아왔다. 열람실은 건물 아홉 층에 있었고, 엘리베이터 안에는 그 엘리베이터보다 오래된 정숙 표지판이 붙어 있었다.',
                       '9월에 온 편지는 소환장이 아니었다. 기록보관소의 납작한 말투로, 그 서류철이 쉬게 놓였다는 통지였다. 그것이 존재한다는 것, 한 번 읽혔다는 것, 누군가 '
                       '청구하지 않으면 다시는 읽히지 않는다는 뜻이었다.',
                       '재분류는 그 서류철이 움직인다는 뜻이었다. 움직이는 서류철은 세 개의 책상에서 차례로 읽히고, 각 책상은 다른 모퉁이에 자기 이니셜을 적으며, 끝에는 '
                       '서류철이 본 이력이 남는다. 자기가 바란 것은 그것뿐이라고 그는 자신에게 말했다. 결론도, 평결도 아니라, 그것을 읽은 사람들의 이니셜만 있으면 된다.',
                       '기록보관소가 요구하는 파란색 잉크로, 규칙 종이에 쓰던 그 펜으로 썼다. 그것은 자기 삶의 두 문서가 같은 손글씨라는 뜻이었다.',
                       '*자기 엔그램을 수리하지 마. 두 사람이 있던 자리에 완전함을 만들지 마.*',
                       '아홉 해를 읽어 왔지만 거기에 적히지 않은 말을 한 번도 눈치채지 못했다. 누가 그것에 동의했는지 적혀 있지 않았다. 언제 그것이 정해졌는지도 적혀 있지 '
                       '않았다. 한 사람이 쓰고 서랍에 넣어 둔, 아무도 증인하지 않은 규칙이었다. 그는 그것의 유일한 독자이자 유일한 재판관이었고, 정중히 말하면 그것의 유일한 '
                       '대상자였다.',
                       '그는 셋째 줄을 쓰려고 생각했다. *자기 규칙의 유일한 독자가 되지 마.* 쓰지 않았다. 홀로 쓰인 줄은 자기가 불평하는 그것 그 자체이고, 자기 감독 '
                       '조항을 쓰는 사람은 그 문제를 이해하지 못한 사람이기 때문이었다.',
                       '그주 Mara가 설명한 것은 하나의 절차였다: 직조기 옆에 서는 두 번째 사람. 그의 일은 그를 지켜보는 것이 아니라 채움에 대한 기록자가 되어, 채움이 '
                       '조용히 기억으로 바뀌지 못하게 하는 것이었다. 그는 손님들에게는 한나절에 그 절차를 만들어 주었다. 열한 해 동안 자기에게는 아무것도 만들어 주지 못했다.',
                       '그는 둘째 장 아래쪽에 작고 가지런히 서명하고, 날짜는 카운터 직원이 채워 넣도록 남겨 두었다. 날짜를 자기 필체로 남기고 싶지 않았다.',
                       '그러고 봉투를 들고 나와 금전 등록기 위의 등에 기대 세웠다. 아침에 그가 서랍을 열려면 반드시 먼저 그것을 옮겨야만 하는 자리였다.',
                       '둘째 등을 끄기 전에 비가 시작되었다. 비는 거리를 납작하게 덮치고 금속 차양에 모래를 한 움큼씩 던지는 소리를 냈다. 젖은 철 냄새가 문 아래로 스며들어 '
                       '와 가게 안에 머물렀다.',
                       '그는 봉투를 세워 둔 채로 두었다. 세워 둔 것은 처리해야 할 물건이다. 카운터에 물건을 두고 제각각 자기 시간에 찾으러 돌아가는 열한 해의 손님들에게 '
                       '그것을 배웠다.'],
            'title': '봉투',
            'when': '11월 어느 밤'},
     'tr': {'blocks': ['Bunu gece, kepenk inik yazdı; çünkü arşive başvuran bir adam, bunu yaparken görülmek '
                       'istemez.',
                       'Form iki sayfaydı. Birinci sayfa hangi kayıt, hangi sınıflandırma ve kimin talebi '
                       'üzerine olduğunu soruyordu. İkinci sayfa başvuranın kayıtla ilişkisini soruyor, '
                       'gerekçe için dört satır bırakıyordu.',
                       "Birinci sayfayı doldurdu: Eylül'de kendisine gelen mektuptaki kayıt numarası, kaydın "
                       'şu anki sınıflandırması ve *başvuran* başlığının altına, tıpkı lisansında yazdığı '
                       'biçimde, kendi adı büyük harflerle.',
                       'Sonra durdu; çünkü talep yer değiştirebilen bir şeydir. Onunki daha önce bir kez yer '
                       'değiştirmişti: yirmi altı yaşında, lisans için imza attığı ve bir lisansın bir çeşit '
                       'izin olduğuna inandığı sırada. O zamandan beri öğrendiği şuydu: lisans bir çeşit '
                       'borçtur; elde tutulur, hesabı verilir ve yılda bir kez biri onunla ne yaptığını okur.',
                       'İkinci sayfa çevrildi. *Kayıtla ilişki: özne.* Gerekçe için dört satır bırakılmıştı; '
                       'satırların üç buçukunu kullandı.',
                       "Gerekçe mektup değildi. Gerekçe, Eylül'de arşiv gişesindeki bir memur kadındı; dosyaya "
                       'bakıp, hiçbir kötülük düşünmeden, tek imzalı bir dosyanın kimse tarafından okunmadan '
                       'kapatılabileceğini söylemişti. Bunu birçok kez söylemiş birinin doğal söylenişiyle '
                       'söyledi, ardından sözünün karşıda oturup oturmadığını görmek için başını kaldırdı. '
                       'Oturmuştu.',
                       'Kural kâğıdını almak için çekmeceye gitti ve bu kez kâğıdı ayakta okudu.',
                       'On bir yıl içinde arşive dört kez gitmişti; her defasında oradan, kâğıtları saklamak '
                       'amacıyla yapılmış, sonradan insanları da saklaması istenmiş bir bina izlenimiyle '
                       'ayrılıyordu. Okuma salonu dokuzuncu katta yer alıyordu; asansörün üzerindeki sessizlik '
                       'uyarısı asansörün kendisinden daha eskiydi.',
                       "Eylül'de gelen mektup bir çağrı niteliği taşımıyordu. Arşivin yalın diliyle yazılmış "
                       'bir bildirimdi: dosya dinlenmeye konmuştu; bu da dosyanın var olduğu, bir kez okunduğu '
                       've birinin talep etmesi dışında bir daha okunmayacağı anlamına geliyordu.',
                       'Yeniden sınıflandırma, dosyanın başka yere taşınması demekti. Yeri değişen bir dosya '
                       'üç ayrı masada okunur, her masa farklı bir köşeye kendi baş harflerini yazar ve bu '
                       'işlemin sonunda dosyanın bakılmış bir geçmişi olur. İstediği tek şey buydu, dedi kendi '
                       'kendine: bir bulgu ya da bir hüküm değil, yalnızca onu okumuş insanların baş harfleri.',
                       'Arşivin istediği mavi mürekkeple, kural kâğıdını yazarken kullandığı aynı kalemle '
                       'yazdı; bu da hayatındaki iki belgenin aynı el yazısına sahip olması demekti.',
                       "*Kendi engram'larını onarma. İki insanın bulunduğu yerde bütün yaratma.*",
                       'Dokuz yıldır kâğıdı okuyordu ama neyi söylemediğini bir kez olsun fark etmemişti. '
                       'Kurala kimin razı olduğunu söylemiyordu. Ne zaman verildiğine dair bir karar '
                       'içermiyordu. Tek bir insan tarafından yazılmış, bir çekmecede tutulan ve kimsenin '
                       'şahit olmadığı bir kuraldı; kuralın tek okuru ve tek yargıcı oydu; bu da onun tek '
                       'öznesi olduğunu söylemenin nezaketli biçimiydi.',
                       'Üçüncü bir satır eklemeyi düşündü. *Kuralının tek okuru olma.* Satırı yazmadı; çünkü '
                       'tek başına kaleme alınmış bir satır, şikâyet ettiği şeyin ta kendisidir ve kendi '
                       'gözetim hükmünü yazan adam, sorunu doğru anlamamış demektir.',
                       "Mara'nın o hafta anlattığı şey bir protokoldü: dokuma tezgâhının yanında duran ikinci "
                       'bir kişi; bu kişinin görevi onu izlemek değil, dolgunun hesabını tutmaktı, böylece '
                       'dolgu sessizce belleğe dönüşemezdi. Bunu müşteriler için bir öğleden sonra içinde '
                       'kurmuştu. On bir yıldır kendisi için ne böyle bir şey ne de başka bir düzenleme '
                       'kurmamıştı.',
                       'İkinci sayfanın alt kısmına küçük ve düzgün bir imza attı; tarihi gişe memurunun '
                       'kendisi doldursun diye bıraktı, çünkü tarihin kendi el yazısıyla yazılmış olmasını '
                       'istemiyordu.',
                       'Sonra paketi eline alıp dışarı çıktı ve kasanın üzerindeki lambaya dikey olarak '
                       'dayadı; sabah biri çekmeceyi açmak için önce paketi kaldırmak zorunda kalacaktı.',
                       'İkinci lambayı daha söndürmeden yağmur başladı. Yağmur sokak boyunca düzce iniyor, '
                       'metal saçağa avuç dolusu çakılın boşaltılma sesiyle vuruyordu; ıslak demir kokusu '
                       'kapının altından süzülüp içeri girdi ve orada kaldı.',
                       'Paketi dikey durur halde bıraktı. Dik bırakılmış bir nesne, üzerinde durulması gereken '
                       'bir nesnedir; bunu on bir yıl boyunca tezgâhına çeşitli şeyler bırakan ve kendi '
                       'zamanlarında geri gelen müşterilerden öğrenmişti.'],
            'title': 'Paket',
            'when': 'kasımda bir gece'},
     'yue': {'blocks': ['佢夜晚落咗閘先寫；一個寫信去檔案嘅人，唔想畀人見到佢寫。',
                        '表格有兩頁。第一頁問係咩紀錄、咩分類、根據邊個嘅申請。第二頁問申請人同紀錄嘅關係，留四行寫原因。',
                        '佢填第一頁：九月寄嚟嗰封信入面嘅紀錄編號、現行嘅分類；喺 *申請人* 下面，用大寫寫自己個名，同牌照上嘅一樣。',
                        '然後佢停低，因為申請係會郁動嘅嘢。佢嗰份以前郁過一次，二十六歲嗰陣，佢簽牌，相信牌照係一種准許。後來佢先明白，牌照係一種債：你揸住佢、要為佢負責，每年有人讀一次你用佢做過咩。',
                        '第二頁。*同紀錄嘅關係：當事人。* 留四行寫原因，佢用咗三行半。',
                        '原因唔係嗰封信。原因係九月檔案櫃台一個職員：佢望住個檔案，唔帶惡意咁講，得一個簽名嘅檔案，可以冇人讀過就封埋。佢講嘅方式，似一個講過好多遍嘅人；然後抬頭睇下句說話落唔落地。落咗。',
                        '佢去抽屜攞規條紙，今次係企住讀。',
                        '十一年嚟佢去過檔案四次；每次離開都有一種感覺：呢座建築起嚟係裝紙嘅，後來先至被要求裝人。閱讀室喺九樓，升降機有塊靜音告示，比部升降機仲老。',
                        '九月嗰封信唔係傳召。係一份通知，用檔案平直嘅語言寫，話個檔案已經安放；即係佢存在過、被讀過一次，除非有人申請，否則唔會再被讀。',
                        '重新分類即係個檔案會郁。郁動嘅檔案會喺三張枱被讀過，每張枱喺唔同角落寫上簽名縮寫；到最後，個檔案有一段被人睇過嘅歷史。佢同自己講，佢要嘅只係咁：唔係一項發現，唔係裁決，只係讀過佢嘅人嘅簽名縮寫。',
                        '佢用檔案要求嘅藍墨水、寫規條紙嗰支筆填；即係佢人生入面兩份文件，出自同一隻手。',
                        '*唔好修補自己嘅 engram。唔好喺兩個人曾經喺度嘅地方造出一個完整。*',
                        '讀咗九年，佢從來冇留意規條冇講嘅嘢。冇講邊個同意過。冇講幾時決定。一條一個人寫嘅規條，收喺抽屜，冇人見證；佢係唯一嘅讀者、唯一嘅判決者——講得客氣啲，即係佢係規條唯一嘅對象。',
                        '佢諗過寫第三行。*唔好做自己規條唯一嘅讀者。* 佢冇寫；因為獨自寫低嘅一行，正正係佢投訴緊嘅嘢；亦因為一個自己寫自己監察條款嘅人，未明個問題。',
                        '嗰個禮拜 Mara '
                        '講嘅係一套程序：織機旁邊要有第二個人，職責唔係盯住佢，係做填料嘅紀錄，等填料唔可以靜靜地變成記憶。佢一個下晝就為客人整好咗；十一年嚟，佢為自己乜都冇整。',
                        '佢喺第二頁底簽名，細而平；日期留畀櫃台職員填，因為佢唔想日期係自己嘅字跡。',
                        '然後佢拎住包裹出嚟，靠住收銀台上面盞燈擺好；朝早要打開抽屜，一定要先挪開佢。',
                        '第二盞燈未熄，雨已經開始落。雨沿住巷平平咁嚟，一把一把沙咁撲上金屬簷篷；濕鐵味由門底鑽入嚟，留低唔走。',
                        '佢將包裹留喺原地。留喺原地嘅嘢，係一定要處理嘅嘢；呢樣係十一年客人教佢嘅：人哋將嘢放喺佢櫃面，然後喺自己方便嘅時候返嚟攞。'],
             'title': '包裹',
             'when': '十一月某一晚'}},
 4: {'en': {'blocks': ['Monday was dry for the first time in nine days, and Elias took the awning brackets '
                       'down.',
                       'There were two, and the left one was bent where the wind had worked at it. He had '
                       'promised himself he would put the sign back up before the rain came again. That had '
                       'been a week of promises.',
                       'He had taken the sign down to repaint the lettering and had found, underneath it, a '
                       'second sign, older, in a hand he recognised as his own from the year he opened: '
                       '*repair, and refusal, on the record.* He had put the older one back in the storeroom, '
                       'undecided, and the brackets had been on the counter ever since.',
                       'A sentence on a sign is a promise made to strangers. He had written it in a week when '
                       'he thought the shop would last a year, and it had lasted eleven, and the sentence had '
                       'turned out to be more accurate than he was.',
                       'Mara was at the back, sorting sleeves. She had started coming in three mornings a week '
                       'and had not asked for a key, which he noticed every time she left.',
                       "“The drawer's sticking,” she said, without turning round.",
                       "“The drawer's fine.”",
                       "“I wasn't asking.”",
                       'He put the brackets on the counter and looked at them. A bent bracket is a thing you '
                       'can fix in an hour or leave for a year, and the difference is never in the bracket.',
                       'The archive packet was still on the till, standing against the lamp. Mara read the '
                       'address on her way past and did not ask. That was worse than a question. A question '
                       'can be answered with a sentence; not asking leaves the sentence for him to say to '
                       'himself.',
                       'She had begun reading the intake book backwards, from the most recent page, which he '
                       "had not known until he saw her at it. She said the shop's record read like a list of "
                       'people who had decided too late.',
                       '“They decide at the counter,” he said.',
                       '“They decide before they come. The counter is where they find out the price.”',
                       'At noon a man came in with a receipt and no core. He had paid, eleven months ago, for '
                       'a repair he had never collected, and he wanted either the core or the money and was '
                       'not sure which would feel better. Elias found the core in the second drawer, still in '
                       'its sleeve, and the man held it without opening it and asked whether it was still '
                       'good.',
                       "“It's good. It doesn't spoil.”",
                       "“Then I'll take it.” He did not take it. He put it in his coat pocket and stood there. "
                       '“My wife says I should have come in the spring.”',
                       "“She's probably right.”",
                       '“She usually is.” He went out, and the bell rang twice because he caught it with his '
                       'shoulder on the way.',
                       "At four there was a woman who wanted her mother's last week sharpened. Not restored; "
                       'sharpened, she said, so the days would hold their shape when she thought about them, '
                       'because at the moment they went soft at the edges and she could not tell one from '
                       'another.',
                       'It was a small job and he did it in an hour and a half. Mara watched from the back and '
                       'afterwards asked why he had laid the fill from the Thursday end rather than the Sunday '
                       'end.',
                       '“Because the Thursday was intact. You lay from the sound part toward the broken part, '
                       'or the fill starts deciding where the memory goes.”',
                       "“That isn't in the book.”",
                       '“The book is for prices.”',
                       'She said nothing, and he heard how it sounded: a book for prices, a rule for nobody, a '
                       'drawer that sticks.',
                       '“You could write the reason,” she said. “Not the price. The reason.”',
                       '“The reason is a sentence I only know afterwards.”',
                       '“Then write it afterwards.”',
                       'He thought about that for the rest of the afternoon, wrote nothing, and noticed '
                       'himself not writing it.',
                       'In the evening he wrote the job up while she put her coat on. From the door she asked '
                       'what he would do if the Ward asked for the log.',
                       '“Give it to them.”',
                       "“They'll read it as a defence.”",
                       '“It is one.”',
                       'She thought about that. “A defence written by one hand,” she said, and went out.',
                       'He put the brackets on the counter where he would see them in the morning. Tuesday '
                       "came with the bread cart's bell twice at the corner, and then the flap of the letter "
                       'slot, and then the flat slap of something too stiff to be a bill.'],
            'title': 'The Brackets',
            'when': 'the Monday before the letter'},
     'ko': {'blocks': ['아흐레 만에 처음으로 월요일은 마른 날이었다. Elias는 차양 브래킷들을 벽에서 내렸다.',
                       '두 개였고 왼쪽 것은 바람이 파고든 자리가 휘어 있었다. 그는 비가 다시 내리기 전에 간판을 다시 올리겠다고 자신과 약속했다. 그 한 주는 약속들로 채워진 '
                       '주였다.',
                       '글씨를 다시 칠하려 간판을 내렸다가 그 아래, 더 오래된 두 번째 간판을 발견했다. 가게를 연 해의 자기 필체라고 알아보았다: *수리, 그리고 거절, '
                       '기록으로.* 더 오래된 쪽은 결정하지 못하고 창고에 다시 넣었고, 브래킷은 그때부터 카운터에 놓여 있었다.',
                       '간판에 적힌 문장은 낯선 이들에게 하는 약속이다. 가게가 일 년은 갈 것이라고 생각한 그 주에 그는 그것을 썼고, 가게는 열한 해를 견뎠으며, 그 문장은 '
                       '자기보다 더 정확했다.',
                       'Mara는 뒤쪽에서 소매들을 정리하고 있었다. 주에 세 아침씩 오기 시작했고 열쇠를 요구하지 않았으며, 그녀가 떠날 때마다 그는 그것을 눈치챘다.',
                       '“서랍이 붙어요.” 그녀는 돌아보지 않고 말했다.',
                       '“서랍은 괜찮다.”',
                       '“묻는 말이 아니었어요.”',
                       '그는 브래킷들을 카운터에 놓고 그것들을 보았다. 휜 브래킷은 한 시간에 고칠 수도, 일 년을 그대로 둘 수도 있는 것이고, 차이는 브래킷에 있지 않다.',
                       '기록보관소 봉투는 여전히 등록기 위에 등에 기대 세워져 있었다. Mara는 지나가다 그 주소를 읽고 묻지 않았다. 그것은 질문보다 나빴다. 질문은 문장 '
                       '하나로 대답할 수 있지만, 묻지 않으면 그 문장이 자기 자신에게 돌아간다.',
                       '그녀는 최근 페이지부터 거꾸로 접수 장부를 읽기 시작했고, 그 모습을 보기 전까지 그는 그 사실을 알지 못했다. 가게의 기록은 결정이 늦게 내린 사람들의 '
                       '명단처럼 읽힌다고 그녀는 말했다.',
                       '“카운터에서 결정한다.” 그가 말했다.',
                       '“오기 전에 결정해요. 카운터는 값을 알아내는 곳일 뿐이지.”',
                       '정오에 영수증은 있으나 코어는 없는 남자가 들어왔다. 열한 달 전에 찾아가지 못한 수리 값을 치렀고, 코어든 돈이든 어느 쪽이 더 나을지 확신 없이 '
                       '원했다. Elias는 그 두 번째 서랍에서 아직 소매에 든 코어를 찾아냈다. 남자는 열어 보지도 않은 채 그것을 들고 아직 괜찮은지 물었다.',
                       '“괜찮다. 상하지 않는다.”',
                       '“그럼 가져갈게.” 그는 가져가지 않았다. 코트 주머니에 그것을 넣고 거기에 서 있었다. “아내가 봄에 왔어야 한다고 하네.”',
                       '“아마 맞을 거다.”',
                       '“대개 맞죠.” 그는 밖으로 나갔고, 나가는 길에 어깨가 종을 쳐서 두 번 울렸다.',
                       '네 시에는 어머니의 마지막 주를 선명하게 해 달라는 여자가 왔다. 복원이 아니라 선명하게, 그녀가 생각할 때 날들이 모양을 유지하도록. 지금은 가장자리가 '
                       '물러져 어느 날인지 서로 구분할 수 없다고 했다.',
                       '작은 일이었고 그는 한 시간 반 만에 끝냈다. Mara는 뒤쪽에서 지켜보았다가, 일이 끝난 뒤에 왜 채움을 일요일 끝이 아니라 목요일 끝부터 놓았는지 '
                       '물었다.',
                       '“목요일은 온전했으니까. 온전한 부분에서 깨진 부분으로 채움을 놓는다. 그렇지 않으면 채움이 기억이 어디로 갈지 결정하기 시작한다.”',
                       '“그건 장부에 없어요.”',
                       '“장부는 값을 적는 책이다.”',
                       '그녀는 아무 말도 하지 않았고, 그는 그 대답이 어떻게 들리는지 들었다. 값을 위한 책, 아무도 위한 규칙, 붙는 서랍.',
                       '“이유를 적어 둘 수도 있죠.” 그녀가 말했다. “값이 아니라 이유.”',
                       '“이유는 일이 끝난 뒤에야 아는 문장이다.”',
                       '“그럼 끝난 뒤에 쓰면 되죠.”',
                       '오후 남은 시간을 그것을 생각하며 보내고 아무것도 쓰지 않았으며, 쓰지 않는 자기 자신을 눈치챘다.',
                       '저녁에 그녀가 코트를 입는 동안 그는 작업을 장부에 적었다. 문가에서 관리청이 장부를 내놓으라고 요구하면 어떻게 하겠냐고 그녀가 물었다.',
                       '“장부를 주겠다.”',
                       '“그걸 방어 문서로 읽을 거예요.”',
                       '“그렇다. 방어 문서다.”',
                       '그녀는 그것을 생각했다. “한 필체가 쓴 방어 문서.” 그녀는 말하고 나갔다.',
                       '브래킷을 아침에 눈에 띄게 카운터에 놓았다. 화요일은 모퉁이에서 빵 수레 종이가 두 번 울리고, 편지 넣는 구멍 덮개가 들리고, 지폐라기엔 뻣뻣한 무언가가 '
                       '납작하게 부딪치는 소리와 함께 왔다.'],
            'title': '브래킷',
            'when': '편지 오기 전 월요일'},
     'tr': {'blocks': ['Pazartesi dokuz gündür ilk kez kuru bir gündü ve Elias saçağın braketlerini söküp '
                       'indirdi.',
                       'Braketler iki taneydi; soldaki, rüzgârın uğraşıp büktüğü yerden kıvrılmıştı. Yağmur '
                       'yeniden başlamadan tabelayı yerine asacağına kendine söz vermişti. O da sözlerle geçen '
                       'bir hafta olmuştu.',
                       'Harfleri yeniden boyamak için tabelayı indirmiş, altında ikinci, çok daha eski bir '
                       'tabela bulmuştu; dükkânı açtığı yıla ait, kendi el yazısı olduğunu tanıdığı bir '
                       'kalemle yazılmıştı: *onarım ve red, kayıt üzerinde.* Eski tabelayı ne yapacağına karar '
                       'veremeden depoya geri koymuştu; braketler ise o günden beri tezgâhın üzerindeydi.',
                       'Tabeladaki bir cümle, yabancılara verilmiş bir sözdür. O cümleyi, dükkânın bir yıl '
                       'süreceğini sandığı bir hafta içinde yazmıştı; dükkân on bir yıl dayanmıştı ve cümle, '
                       'kendisinden daha isabetli çıkmıştı.',
                       'Mara dükkânın arka tarafında kılıfları ayırıyordu. Haftada üç sabah gelmeye başlamış, '
                       'ona bir anahtar vermesini istememişti; Elias bunu her çıkışında yeniden fark ediyordu.',
                       '“Çekmece tutuyor,” dedi, dönmeden.',
                       '“Çekmece iyi.”',
                       '“Sormuyordum.”',
                       'Braketleri tezgâhın üzerine koyup onlara baktı. Bükülmüş bir braket, bir saatte '
                       'onarılabilir ya da bir yıl olduğu gibi bekletilebilir; ayrım asla braketin kendisinde '
                       'yatmaz.',
                       'Arşive gidecek paket hâlâ kasanın üzerindeydi, lambaya dayalı duruyordu. Mara yanından '
                       'geçerken adresi okudu ama hiçbir şey sormadı. Bu, bir sorudan daha kötüydü. Bir soruya '
                       'bir cümleyle karşılık verilebilir; sormamak, o cümleyi kendi kendine söylemesi için '
                       'ona bırakmaktır.',
                       'Kayıt defterini en son yazılan sayfadan başlayarak geriye doğru okumaya başlamıştı; '
                       'Elias bunu, kadın defterin başında otururken görene kadar bilmiyordu. Dükkânın '
                       'kaydının, kararını çok geç vermiş insanların bir listesi gibi okunduğunu söyledi.',
                       '“Kararlarını tezgâhta verirler,” dedi.',
                       '“Gelmeden karar verirler. Tezgâh fiyatı öğrendikleri yerdir.”',
                       'Öğleyin elinde fiş, çekirdeği olmayan bir adam girdi. On bir ay önce, hiçbir zaman '
                       'gelip almadığı bir onarım için para ödemişti; şimdi ya çekirdeğini ya parasını '
                       'istiyordu ve hangisinin kendisini daha iyi hissettireceğinden emin değildi. Elias '
                       'çekirdeği ikinci çekmecede buldu; hâlâ kılıfının içindeydi. Adam çekirdeği açmadan '
                       'elinde tuttu ve hâlâ kullanılabilir durumda olup olmadığını sordu.',
                       '“İyi. Bozulmaz.”',
                       '“O halde alıyorum.” Almadı. Ceketinin cebine koyup orada durdu. “Karım ilkbaharda '
                       'gelmem gerektiğini söylüyor.”',
                       '“Muhtemelen haklı.”',
                       '“Genelde haklıdır.” Dışarı çıktı; zil iki kez çaldı, çıkarken omzuyla çarpmıştı.',
                       'Saat dörtte, annesinin son haftasını keskinleştirmek isteyen bir kadın geldi. Geri '
                       'getirme değil, keskinleştirme istedi; öyle ki o günleri düşündüğünde günler '
                       'şekillerini korusun, çünkü şu an günler kenarlarından yumuşuyor ve kadın bir günü '
                       'diğerinden ayıramıyordu.',
                       'Küçük bir işti, bir buçuk saat içinde tamamladı. Mara arkadan onu izledi, iş bitince '
                       'dolguyu neden Pazar ucundan değil de Perşembe ucundan başlayarak döşediğini sordu.',
                       '“Perşembe sağlamdı. Dolguyu sağlam kısımdan bozuk kısma doğru döşersin, yoksa dolgu '
                       'belleğin nereye gideceğine karar vermeye başlar.”',
                       '“Defterde yazmıyor bu.”',
                       '“Defter fiyatlar içindir.”',
                       'Kadın hiçbir şey söylemedi; Elias sözlerin kulağa nasıl geldiğini kendi içinde duydu: '
                       'fiyatlar için tutulan bir defter, kimse için geçerli bir kural, tutup açılmayan bir '
                       'çekmece.',
                       '“Gerekçeyi yazabilirsin,” dedi. “Fiyatı değil. Gerekçeyi.”',
                       '“Gerekçe, sonradan bildiğim bir cümle.”',
                       '“Sonra yaz o halde.”',
                       'Öğleden sonranın kalan kısmında bunu düşündü, tek satır yazmadı ve hiçbir şey '
                       'yazmadığının farkına vardı.',
                       'Akşamüstü kadın ceketini giyerken o işi deftere geçirdi. Kadın kapıdan çıkarken, '
                       'Koruma Dairesi defteri istediği takdirde ne yapacağını sordu.',
                       '“Veririm onlara.”',
                       '“Savunma olarak okuyacaklar.”',
                       '“Öyle biridir.”',
                       'Bunu düşündü. “Tek elle yazılmış bir savunma,” dedi ve çıktı.',
                       'Braketleri sabah kalkar kalkmaz göreceği yere, tezgâhın üzerine koydu. Salı günü '
                       'köşeden ekmek arabasının zili iki kez çaldı; sonra mektup yuvasının kapağı oynadı, '
                       'sonra bir fatura olamayacak kadar sert bir şeyin düz patırtısı duyuldu.'],
            'title': 'Braketler',
            'when': 'mektuptan önceki pazartesi'},
     'yue': {'blocks': ['九日嚟第一個乾身嘅禮拜一，Elias 拆低簷篷支架。',
                        '一共兩個，左邊嗰個畀風吹彎咗。佢應承過自己，落雨之前會將招牌掛返上去。呢個禮拜好多應承。',
                        '佢拆低招牌重描字，喺下面搵到第二塊招牌，舊啲，字跡佢認得，係開張嗰年自己寫嘅：*修補同拒絕，都入紀錄。* 舊嗰塊佢擺回貯物室，未決定；支架由嗰陣起一直放喺櫃面。',
                        '招牌上嘅一句說話，係答應陌生人嘅承諾。佢寫嗰句嘅時候，以為間鋪頂得住一年；結果頂咗十一年，而句說話後來證明，比佢本人準確。',
                        'Mara 喺後面整理紙套。佢開始一個禮拜來三朝，從來冇問佢要鎖匙；佢每次走都會留意到呢樣。',
                        '「抽屜卡住，」佢話，冇回頭。',
                        '「抽屜冇事。」',
                        '「我唔係問你。」',
                        '佢將支架放喺櫃面望住。彎咗嘅支架，可以一個鐘整好，亦可以擺一年；分別永遠唔喺支架度。',
                        '檔案包裹仲喺收銀台，靠住盞燈。Mara 行過讀到地址，冇問。呢樣比起問仲差。問題可以用一句說話答；唔問，句說話就要留畀佢自己對自己講。',
                        '佢開始由最後一頁倒住讀本簿；佢見到先至知。佢話，鋪頭嘅紀錄讀落似一份名單，入面嘅人都係決定得太遲。',
                        '「佢哋喺櫃面先至決定，」佢話。',
                        '「佢哋未上門已經決定咗。櫃面只係畀佢哋知道價錢嘅地方。」',
                        '中午，一個男人拎住張收據入嚟，冇帶核。十一個月前佢畀錢做過一次修補，從來冇嚟攞；佢想攞返粒核，或者攞返筆錢，唔知邊樣會舒服啲。Elias '
                        '喺第二個抽屜搵到粒核，仲喺套入面；男人拎住唔打開，問仲好唔好。',
                        '「好嘅。核唔會壞。」',
                        '「咁我攞佢。」佢冇攞。佢放入件褸袋，企喺度。「我老婆話我應該春天就嚟。」',
                        '「佢大概係啱嘅。」',
                        '「佢多數都啱。」佢走出去，肩膀碰到門鈴，鈴響咗兩次。',
                        '四點，有個女人想將阿媽最後一個星期磨清晰。唔係復原；係磨清晰，佢話，等佢諗起嗰啲日子嘅時候，日子仲撐得住形；而家邊緣變軟，佢分唔開一日同另一日。',
                        '細工，佢一個半鐘做妥。Mara 喺後面睇住；之後問佢，填料點解由星期四嗰端開始鋪，唔由星期日嗰端。',
                        '「因為星期四嗰邊完整。要由完好嘅部分朝爛嘅部分鋪，唔係填料就會開始決定記憶擺喺邊。」',
                        '「呢樣冇寫入簿。」',
                        '「簿係寫價錢嘅。」',
                        '佢冇出聲；佢聽出呢句話聽落係咩：一本寫價錢嘅簿、一條冇對象嘅規條、一個卡住嘅抽屜。',
                        '「你可以寫低原因，」佢話。「唔係價錢，係原因。」',
                        '「原因係一句事後先至識得講嘅話。」',
                        '「咁事後先寫。」',
                        '下晝餘下嘅時間佢都諗住呢樣；乜都冇寫，而且留意到自己唔寫。',
                        '傍晚佢寫低件工，佢着褸。佢喺門口問，如果管理局要睇本簿，佢會點做。',
                        '「畀佢哋。」',
                        '「佢哋會當係辯解嚟讀。」',
                        '「本身就係。」',
                        '佢諗咗一下。「一隻手寫嘅辯解，」佢話，然後走咗出去。',
                        '佢將支架放喺櫃面，朝早一開門就見到。禮拜二跟住麵包車嘅鈴，喺街角響兩次；然後係信箱口嗒一聲；再然後，係一樣嘢拍落嚟嘅平實聲，硬淨到唔係一張賬單。'],
             'title': '支架',
             'when': '收信前嘅禮拜一'}},
 5: {'en': {'blocks': ['On the seventh day of the ten, Elias cleared the bench.',
                       'The drawer caught, as it always did. He lifted the front edge, cleared it, and took '
                       "out the mother's core, which was the one unsealed repair in the shop that the Ward "
                       'already knew about.',
                       '“Show him the seam,” he said.',
                       '“Show him the refusal,” Mara said.',
                       '“He wants to see a repair.”',
                       "“He wants to see what you do when it's difficult. A repair shows him your hands. A "
                       'refusal shows him your reasons.”',
                       '“A refusal shows him an opinion. He writes findings about facts.”',
                       'They had been having this conversation for a week, which is to say they each said the '
                       'same three sentences in a different order each time and then stopped.',
                       'Before that he had cleaned the plate, which did not need cleaning, and had put the '
                       'spare brick of fill where the inspector could see it, and then moved it back to where '
                       'he would have kept it anyway.',
                       "“You're arranging the shop,” Mara said.",
                       "“I'm tidying.”",
                       "“You've tidied the same shelf twice.”",
                       "The mother's core had sat in the drawer for five weeks, in the sleeve it came in, and "
                       'the label had gone soft at one corner from being turned over. She had not come back '
                       'for it, and the note in the margin said *not collected*, which was a fact and not an '
                       'explanation.',
                       'A finding is a small document. It says what happened, in the order it happened, and it '
                       'ends with a line that the Ward calls a conclusion and that everyone in the trade calls '
                       "a sentence. He had read other people's findings. They were never wrong, and they were "
                       'never the whole of it.',
                       'He laid the log open at the seam entry. Date, job, price, material, lot number. Four '
                       'columns and a margin.',
                       'The margin was where he wrote the things four columns could not hold, and there was '
                       'nothing in the margin against the seam, because at the time he had not thought it '
                       'needed explaining.',
                       "“There's no column for refusals,” Mara said.",
                       "“There's a margin.”",
                       '“A margin is not a column.”',
                       'He practised the sentence in the empty shop, out loud, twice: *This is fill, not '
                       'restoration. The seam held because the fill was laid along the edge and not across '
                       'it.* The second time he heard himself say it the way a man says a thing he has decided '
                       'to be true of himself.',
                       'Mara read the log aloud to him in her level voice, from the first of the ten days, and '
                       "he listened as a stranger would: a man who had kept a customer's core, who had "
                       'repaired without a witness, who had written a rule that nobody signed. None of it was '
                       'a crime. All of it was a finding.',
                       'They closed at seven. Mara went out, came back for her scarf, and said from the door '
                       'that the log was not the problem; the problem was that he would answer every question '
                       'honestly and then explain himself afterwards, and an explanation after an honest '
                       'answer sounds like a second answer.',
                       "“Then I'll stop explaining.”",
                       "“You won't.”",
                       'She was right, and he had known it before she said it, which is the only reason he did '
                       'not argue.',
                       'That night he did not sleep, and made a list instead, in his head, of what the '
                       'inspector could write. The list had four things on it and he could not get it down to '
                       'three.',
                       'At some point in the night he got up and read the log again by the kitchen light. '
                       'Against the fourth entry there was a mark he did not remember making: a small cross in '
                       'pencil, beside a job done on a Tuesday for a woman whose name he could not recall '
                       'without the book. He did not know whether the cross meant the work had gone well or '
                       'that he had wanted to look at it again, and the fact that both were possible was why '
                       'he sat down.',
                       'In the morning he shaved, which he did not do on Mondays, and boiled the kettle and '
                       'did not drink the tea. The lane was dry and cold and the awning dripped from the '
                       "night's rain at a rhythm that was almost a clock.",
                       'At ten a man came down the lane carrying two cases, one for a frame and one for a '
                       'plate, and he refused the courier at the corner and carried them himself.'],
            'title': 'The Seventh Day',
            'when': 'the seventh day of the ten'},
     'ko': {'blocks': ['그날 열흘 중 이레째 날, Elias는 작업대를 치웠다.',
                       '서랍은 늘 그렇듯 붙었다. 서랍 앞쪽을 들어 올려 빼내고 어머니의 코어를 꺼냈다. 관리청이 이미 알고 있는, 가게 안 유일한 봉인 안 된 수리였다.',
                       '“봉합을 보여 주어라.” 그가 말했다.',
                       '“거절을 보여 주세요.” Mara가 말했다.',
                       '“그는 수리를 보러 온 거다.”',
                       '“어려울 때 당신이 어떻게 하는지 보러 온 거예요. 수리는 그에게 당신의 손을 보여 주고, 거절은 당신의 이유를 보여 주죠.”',
                       '“거절은 의견을 보여 줄 뿐이다. 그는 사실에 관한 결론을 쓴다.”',
                       '그들은 이 대화를 일 주일째 계속하고 있었다. 매번 같은 세 문장을 순서만 바꿔 말하고 나서 멈추는 대화였다.',
                       '그전에 닦을 필요도 없는 판을 닦고, 여분 채움 벽돌을 심사관이 볼 수 있는 곳에 뒀다가, 다시 원래 자기가 뒀을 자리로 옮겼다.',
                       '“가게를 배치하고 있네요.” Mara가 말했다.',
                       '“정리하는 거다.”',
                       '“같은 선반을 두 번 정리했어요.”',
                       '어머니의 코어는 다섯 주 동안 서랍에, 들어왔던 소매 그대로 놓여 있었고, 뒤집히느라 한쪽 모퉁이의 라벨이 물러져 있었다. 그녀는 찾으러 돌아오지 않았고, '
                       '여백의 메모는 *찾아가지 않음* 이었다. 그것은 사실이지 설명은 아니었다.',
                       '결론은 작은 문서다. 무슨 일이 일어났는지, 일어난 그 순서대로 말하고, 관리청이 결론이라 부르고 업계의 모든 사람이 문장이라 부르는 한 줄로 끝난다. '
                       '그는 다른 사람의 결론을 읽어 본 적이 있었다. 그것들은 틀리지는 않았지만 결코 전부는 아니었다.',
                       '장부를 봉합 기록이 있는 페이지에 펼쳤다. 날짜, 작업, 값, 재료, 로트 번호. 네 칸과 여백.',
                       '여백은 네 칸에 담지 못하는 것을 적는 자리였고, 그 봉합 옆 여백에는 아무것도 없었다. 당시에는 설명이 필요하다고 생각하지 않았기 때문이었다.',
                       '“거절을 적는 칸은 없네요.” Mara가 말했다.',
                       '“여백이 있다.”',
                       '“여백은 칸이 아니에요.”',
                       '빈 가게에서 그 문장을 소리 내어 두 번 연습했다: *이것은 채움이지 복원이 아니다. 봉합이 버틴 것은 채움이 가장자리를 따라 놓였지 그것을 가로지르지 '
                       '않았기 때문이다.* 두 번째에는 자기 자신에게 참되다고 결심한 말을 하는 사람처럼 자기 말소리를 들었다.',
                       'Mara는 낮고 고른 목소리로 열흘째 첫날부터 장부를 소리 내어 읽어 주었고, 그는 낯선 사람이 듣듯 들었다. 손님의 코어를 맡아 둔 사람, 증인 없이 '
                       '수리한 사람, 아무도 서명하지 않은 규칙을 쓴 사람. 그중 어느 것도 범죄는 아니었지만, 그 모든 것이 하나의 결론이었다.',
                       '일곱 시에 가게를 닫았다. Mara는 나갔다가 스카프를 찾아 돌아왔고, 문가에 서서 장부가 문제가 아니라고 말했다. 문제는 그가 모든 질문에 정직하게 '
                       '대답한 뒤에 스스로 설명한다는 것이었고, 정직한 대답 뒤의 설명은 두 번째 대답처럼 들린다.',
                       '“그럼 설명을 그만두겠다.”',
                       '“못 그만둘 거예요.”',
                       '그녀가 맞았고, 그녀가 말하기 전에 그는 알고 있었다. 다툼을 벌이지 않은 유일한 이유였다.',
                       '그날 밤 잠들지 못하고 심사관이 쓸 수 있는 것을 머릿속으로 목록을 만들었다. 목록에는 네 가지가 적혀 있었고 그는 그것을 세 가지로는 줄이지 못했다.',
                       '밤중 어느 때 그는 일어나 부엌 불로 장부를 다시 읽었다. 네 번째 기록 옆에 자기가 남긴 기억 없는 표시가 있었다. 화요일에 한 여자를 위해 한 작업 '
                       '옆의 작은 연필 십자. 장부 없이는 이름도 떠올리지 못할 여자였다. 그 십자가 일이 잘 풀렸다는 뜻인지 다시 보고 싶었다는 뜻인지 몰랐다. 둘 다 '
                       '가능하다는 사실이 그를 앉게 한 이유였다.',
                       '아침에 그는 월요일에는 하지 않는 면도를 하고, 주전자를 끓였으나 차는 마시지 않았다. 거리는 마르고 추웠고, 차양은 밤에 내린 비에 거의 시계 같은 '
                       '리듬으로 물방울을 떨어뜨렸다.',
                       '열 시에 남자가 케이스 두 개를 들고 거리를 내려왔다. 하나는 프레임용, 하나는 판용이었다. 모퉁이에서 택배를 사양하고 그는 그것들을 직접 들었다.'],
            'title': '이레째 날',
            'when': '열흘 중 이레째'},
     'tr': {'blocks': ['On günün yedinci gününde Elias çalışma tezgâhının üzerini boşalttı.',
                       'Çekmece her zamanki gibi tutukluk yaptı. Ön kenarını yukarı kaldırıp çekmeceyi açtı ve '
                       "annenin çekirdeğini çıkardı; bu, dükkânda Koruma Dairesi'nin zaten bildiği, "
                       'mühürlenmemiş tek onarımdı.',
                       '“Ona dikişi göster,” dedi.',
                       '“Ona redi göster,” dedi Mara.',
                       '“Onarım görmek istiyor.”',
                       '“Zorlandığında ne yaptığını görmek istiyor. Onarım ona ellerini gösterir. Red '
                       'gerekçelerini gösterir.”',
                       '“Red ona bir görüş gösterir. Olgular hakkında bulgu yazar.”',
                       'Bu konuşmayı bir haftadır sürdürüyorlardı; yani ikisi de her seferinde aynı üç cümleyi '
                       'farklı bir sırayla söylüyor, ardından sustular.',
                       'Bunlardan önce, temizlenmeye hiç ihtiyacı olmayan plakayı silmiş, yedek dolgu '
                       'tuğlasını denetçinin görebileceği bir yere koymuş, sonra onu yine her zamanki yerine '
                       'geri taşımıştı.',
                       '“Dükkânı düzenliyorsun,” dedi Mara.',
                       '“Toparlıyorum.”',
                       '“Aynı rafı iki kez topladın.”',
                       'Annenin çekirdeği beş haftadır çekmecede, geldiği kılıfın içinde duruyordu; etiket, '
                       'çevrildikçe bir köşesinden yumuşamıştı. Kadın çekirdeği almak için geri gelmemişti; '
                       'kenar boşluğuna düşülmüş notta *alınmadı* yazıyordu; bu bir olguydu, bir açıklama '
                       'değil.',
                       'Bulgu küçük bir belgedir. Ne olduğunu, olayın gerçekleştiği sıra ile anlatır ve Koruma '
                       "Dairesi'nin sonuç, meslekteki herkesin ise cümle adını verdiği bir satırla sona erer. "
                       'Başkalarının hazırladığı bulguları okumuştu. Onlar asla yanlış değildi ama hiçbir '
                       'zaman olayın tamamını da kapsamıyordu.',
                       'Defteri dikiş geçen işin kaydının bulunduğu sayfaya kadar açtı. Tarih, iş, fiyat, '
                       'malzeme, parti numarası. Dört sütun ve bir kenar boşluğu vardı.',
                       'Kenar boşluğu, dört sütuna sığmayan şeyleri yazdığı yerdi; dikişle ilgili kaydın kenar '
                       'boşluğunda tek bir şey yazılı değildi, çünkü o zamanlar bu işin açıklanmaya '
                       'gereksinimi olduğunu düşünmemişti.',
                       '“Redler için sütun yok,” dedi Mara.',
                       '“Kenar boşluğu var.”',
                       '“Kenar boşluğu sütun değildir.”',
                       'Boş dükkânda cümleyi iki kez, yüksek sesle prova etti: *Bu dolgu, geri getirme değil. '
                       'Dikiş tuttu, çünkü dolgu kenar boyunca döşendi, üzerine doğru geçirilmedi.* İkinci '
                       'seferinde kendini, bir şeyi kendi hakkında doğru kabul etmeye karar vermiş birinin '
                       'söylenişiyle duydu.',
                       'Mara defteri düzgün, sakin sesiyle on günün ilk gününden başlayarak ona okudu; o da '
                       'yabancı birinin dinleyeceği gibi dinledi: bir müşterinin çekirdeğini elde tutmuş, '
                       'yanında şahit olmadan onarım yapmış, kimsenin imza atmadığı bir kural yazmış bir adam. '
                       'Bunların hiçbiri bir suç değildi. Hepsi birer bulguydu.',
                       'Saat yedide dükkânı kapadılar. Mara dışarı çıktı, atkısını almak için geri döndü ve '
                       'kapıdan, sorun olan şeyin defter olmadığını söyledi; sorun şuydu: her soruya dürüstçe '
                       'cevap verecek, ardından kendisini açıklayacaktı, dürüst bir cevaptan sonra gelen '
                       'açıklama ise ikinci bir cevap gibi duyulur.',
                       '“O halde açıklamayı keserim.”',
                       '“Kesmezsin.”',
                       'Kadın haklıydı, o daha söylemeden önce de bunu biliyordu; tartışmamasının tek nedeni '
                       'buydu.',
                       'O gece uyuyamadı; bunun yerine denetçinin neler yazabileceğini kafasında bir liste '
                       'halinde sıraladı. Listede dört madde vardı ve onu bir tür üçe indirememişti.',
                       'Gecenin bir saatinde kalktı ve mutfak ışığında defteri bir kez daha okudu. Dördüncü '
                       'kaydın karşısında, yapmayı hatırlamadığı bir işaret bulundu: kurşun kalemle atılmış '
                       'küçük bir çarpı; Salı günü, adı deftere bakmadan anımsayamadığı bir kadın için '
                       'yapılmış işin yanındaydı. Çarpının işin iyi gittiğini mi yoksa o işe yeniden bakmak '
                       'istediğini mi ifade ettiğini bilmiyordu; ikisinin de mümkün olması, oturup kalmasının '
                       'nedeniydi.',
                       'Sabah tıraş oldu; Pazartesileri tıraş olmazdı. Çaydanlığı kaynattı ama demlediği çayı '
                       'içmedi. Sokak kuru ve soğuktu; tente, gece yağan yağmurdan, neredeyse bir saati '
                       'andıran bir ritimle damlıyordu.',
                       'Saat onda bir adam sokaktan aşağı geldi, iki çanta taşıyordu; biri çerçeve, diğeri '
                       'plaka içindi. Köşede kuryeyi geri çevirmiş ve çantaları kendisi taşımıştı.'],
            'title': 'Yedinci Gün',
            'when': 'on günün yedincisi'},
     'yue': {'blocks': ['十日入面嘅第七日，Elias 清好工作檯。',
                        '抽屜卡住，同平常一樣。佢提起前面鬆開嘅邊，清順，拎出阿媽粒核；呢粒係鋪頭唯一一件未封閉、而管理局已經知嘅修補。',
                        '「畀佢睇接縫，」佢話。',
                        '「畀佢睇拒絕，」Mara 話。',
                        '「佢想睇一次修補。」',
                        '「佢想睇你遇到難搞嘅嘢會點做。修補畀佢睇你雙手；拒絕畀佢睇你嘅理由。」',
                        '「拒絕畀佢睇嘅係意見。佢寫發現，係寫事實。」',
                        '呢段對話已經講咗一個禮拜；即係每次佢哋各講同三句說話，次序唔同，然後停。',
                        '喺嗰之前，佢抹過塊板——根本唔使抹；將備用嗰磚填料放到督察見得到嘅位置，然後又搬返佢本來會放嘅地方。',
                        '「你佈緊間鋪，」Mara 話。',
                        '「我執緊雜。」',
                        '「同一層架你執咗兩次。」',
                        '阿媽粒核喺抽屜擺咗五個禮拜，用原來個套；標籤畀人翻嚟翻去，一角變軟。佢冇返嚟攞；頁邊嘅註記寫住 *冇嚟攞*，係一個事實，唔係解釋。',
                        '發現係一份細文件。按發生次序寫低發生過咩，最後一行，管理局叫佢做結論，呢行行內人都叫佢做判決。佢讀過人哋嘅發現。從來冇錯，亦從來唔係全部。',
                        '佢攤開本簿，翻到接縫嗰一條。日期、件工、價錢、材料、批號。四欄，加一個頁邊。',
                        '四欄裝唔落嘅嘢，佢寫喺頁邊；接縫嗰條嘅頁邊乜都冇，因為嗰陣佢覺得唔使解釋。',
                        '「冇一欄係寫拒絕嘅，」Mara 話。',
                        '「有頁邊。」',
                        '「頁邊唔係一欄。」',
                        '鋪頭空曠，佢大聲練習嗰句，兩次：*呢個係填料，唔係復原。接縫撐得住，係因為填料沿住邊緣鋪，唔係橫跨過去。* 第二次佢聽到自己講嘅方式，似一個人講一樣已經當作自己事實嘅嘢。',
                        'Mara '
                        '用平直把聲，由十日嘅第一日起，將本簿讀出聲畀佢聽；佢似陌生人咁聽：一個扣住客人粒核嘅人、一個冇見證就做修補嘅人、一個寫過一條冇人簽名規條嘅人。呢啲都唔係罪；呢啲全部係一項發現。',
                        '七點閂鋪。Mara 走出去，返嚟攞頸巾；佢喺門口講，本簿唔係問題；問題係佢會老老實實答每條問題，然後事後補解釋；誠實答完再解釋，聽落似第二個答案。',
                        '「咁我唔再解釋。」',
                        '「你做唔到。」',
                        '佢係啱嘅；佢未講佢已經知，亦係咁佢先冇駁嘴。',
                        '嗰晚佢冇瞓，喺腦入面列一份清單，寫督察可以落筆嘅嘢。清單有四樣，佢減唔到三樣。',
                        '夜晚某個鐘數，佢起身，借廚房燈光再讀一次本簿。第四條紀錄旁邊有個記號，佢唔記得自己畫過：一個鉛筆畫嘅細十字，喺禮拜二做嘅一件工隔籬；嗰個女人個名，唔靠簿佢記唔起。佢唔知個十字係指件工做得好，定係佢想再睇一次；兩樣都有可能，就係佢坐低嘅原因。',
                        '朝早佢剃鬚——禮拜一佢平時唔剃；煲滾水，茶冇飲。條巷乾而冷，簷篷滴住夜晚嘅雨水，節奏差唔多似個鐘。',
                        '十點，一個男人落巷，拎住兩個箱，一個裝框，一個裝盤；佢喺街角唔交快遞，自己拎。'],
             'title': '第七日',
             'when': '十日入面嘅第七日'}},
 6: {'en': {'blocks': ['The shop had been shut for eleven days and the dust had got into everything, including '
                       "the felt on the loom's two clamps, which Elias cleaned with a toothbrush because the "
                       'brush that belonged there had walked off in the summer.',
                       'He worked with the door open. Cinder Lane on a Sunday is a sound rather than a street: '
                       'a lift somewhere behind the buildings, water going down a drain that has been going '
                       'down that drain since before he was born, and a dog that barked at the same hour every '
                       'week at nothing.',
                       'The ledger was on the bench where he had left it, closed, with the pen laid across it '
                       'at an angle he did not like. He straightened the pen. Then he straightened it again, '
                       'and understood that he was stalling.',
                       'The rule was on a sheet of paper on the counter, written in his own hand, and it was '
                       'the third draft. The first had been one sentence. The second had grown a clause and '
                       'lost its nerve. This one he had written standing up, which is how he wrote things he '
                       'intended to keep.',
                       '*Two hands on every core. The joint named before the loom. Both names in the ledger, '
                       'whether the repair is done or refused.*',
                       'He read it the way a customer reads a price. Then he turned it over and wrote on the '
                       'back, in smaller letters, the thing the front did not say: *The second name is not a '
                       'witness. The second name is an account.*',
                       'Mara came at four with a bag of groceries she had bought for a shop that was not hers, '
                       'and stood in the doorway taking in the swept floor and the toothbrush and the paper, '
                       'and did not say anything for long enough that Elias began to wipe the counter, which '
                       'was already clean.',
                       '“You wrote it down,” she said.',
                       '“I wrote it down.”',
                       '“You want me to sign the back of it.”',
                       '“I want you to read it first. The back is the part that costs something.”',
                       'She put the bag down and read both sides twice, and Elias watched her read it the way '
                       'he watched a core settle — looking for the moment the surface stopped moving. It came '
                       'at the back, at the word *account*, and when it came she did not look up, which he had '
                       'expected, and she did not argue, which he had not.',
                       '“Four-one-one-nine is still suspended,” she said. “You know that. It comes back on '
                       'conditions, and one of the conditions is a second signer with a licence that is not '
                       "suspended, which is not me, and the other is that the second signer's name is on the "
                       'job before the job starts, which is your sentence, and the third is that both names '
                       "are in a book somebody can audit. That's your sentence too. You have written the "
                       "Ward's conditions in your own hand and hung them in your own shop.”",
                       '“I have written down what I should have been doing for two years.”',
                       "“Those are not the same thing.” She picked up the paper. “But they're close enough "
                       "that the difference is a matter of where you stand. Sit down. You're doing the thing "
                       'with the counter.”',
                       'He sat. She sat opposite him, and the ledger lay between them, and the street did its '
                       "Sunday noises. She said, “Say the fourth one out loud. The one you didn't write, "
                       'because it makes you look like a man who needs watching.”',
                       'He said it out loud. “The person who signs second does not repair their own account at '
                       'the place where they sign second.”',
                       "“That's not about me,” she said.",
                       "“It's about both of us. It's about the fact that a second signature is worthless if "
                       'the person giving it has something in the case.”',
                       'Mara was quiet. Then she took the pen off the ledger, uncapped it, and signed the back '
                       'of the paper underneath his sentence, small and level, the way she signed everything. '
                       "“I'll read every job before you start it,” she said. “And I'll be difficult about the "
                       "ones where the customer hasn't been told what the bridge will do. Not *sometimes* "
                       'difficult. Difficult as a matter of policy.”',
                       '“Good,” Elias said, and it came out with more relief in it than he wanted in the room.',
                       'She stayed until the light went. They put the groceries away in a shop that was still '
                       'not hers, and she took the second set of keys without being asked, and at the door she '
                       'said the thing that he would think about all the way through the first week: “You '
                       "closed for eleven days and the Ward didn't notice. Tomorrow it reopens and the Ward "
                       "still won't notice. That's not a reason to be careless. That's the reason the rule has "
                       'to be written down.”',
                       'On Monday, at nine, he would open the ledger to the first clean page and write the '
                       'date at the top of it. That night he did not sleep well, and the reason was not the '
                       'rule.'],
            'title': 'The Sunday Before',
            'when': '13 November'},
     'ko': {'blocks': ['가게는 열하루 동안 문을 닫고 있었고 먼지는 모든 것에 들어가 있었다. 직조기 두 집게의 펠트에도 먼지가 끼어 있었다. Elias는 칫솔로 그것을 닦았다. '
                       '그 자리에 있던 솔은 여름에 어디론가 사라졌기 때문이었다.',
                       '그는 문을 연 채 일했다. 일요일의 Cinder Lane은 거리라기보다 소리다. 건물 뒤편 어딘가의 엘리베이터, 그가 태어나기 전부터 같은 배수구로 '
                       '내려가는 물, 매주 같은 시각 아무것도 향해 짖는 개.',
                       '장부는 작업대 위, 그가 둔 그대로 닫혀 있었고 펜이 그 위에 좋아하지 않는 각도로 얹혀 있었다. Elias는 펜을 바로 세웠다. 그리고 다시 한 번 바로 '
                       '세우고, 자기가 시간을 끌고 있다는 걸 깨달았다.',
                       '규칙은 카운터 위 종이 한 장에 자기 필체로 적혀 있었고 세 번째 초안이었다. 첫 번째는 한 문장이었다. 두 번째는 조항이 늘어나더니 기운을 잃었다. 이번 '
                       '것은 서서 썼다. 남기려는 것을 그는 서서 썼다.',
                       '*모든 코어에 두 손. 직조기 앞에서 이중 서명을 명시한다. 수리를 마치든 거절하든 두 이름을 장부에 적는다.*',
                       '그는 고객이 가격을 읽듯 읽었다. 종이를 뒤집어 뒷면에, 앞면이 말하지 않은 것을 더 작은 글씨로 적었다: *두 번째 이름은 증인이 아니다. 두 번째 '
                       '이름은 계정이다.*',
                       'Mara는 네 시에, 자기 가게도 아닌 곳을 위해 산 식료품 봉지를 들고 와 현관에 서서 쓸린 바닥과 칫솔과 종이를 훑어보았다. 한참 아무 말도 하지 않자 '
                       'Elias는 이미 깨끗한 카운터를 닦기 시작했다.',
                       '“적었구나.” 그녀가 말했다.',
                       '“적었어.”',
                       '“뒷면에 서명하라는 거지.”',
                       '“먼저 읽어 줬으면 해. 뒷면이 대가가 따르는 부분이야.”',
                       '그녀는 봉지를 내려놓고 양면을 두 번씩 읽었다. Elias는 코어가 가라앉는 것을 지켜보듯 그녀를 지켜보았다. 표면이 움직임을 멈추는 순간을 찾듯이. 그 '
                       '순간은 뒷면, *계정* 이라는 단어에서 왔다. 순간이 왔을 때 그녀는 고개를 들지 않았다. 예상한 일이었다. 따지지도 않았고, 그건 예상하지 못한 '
                       '일이었다.',
                       '“사일일구는 여전히 정지 상태야.” 그녀가 말했다. “너도 알 거야. 조건부로 돌아오는데, 조건 하나는 정지되지 않은 면허를 가진 두 번째 서명자, 그건 '
                       '나 아니지. 다른 하나는 작업 시작 전에 두 번째 서명자의 이름이 작업에 올라 있어야 한다는 거, 그건 네 문장이야. 세 번째는 두 이름이 누군가 감사할 '
                       '수 있는 장부에 있어야 한다는 거, 그것도 네 문장이고. 너는 관리청 조건을 네 손으로 적어 네 가게에 걸어 놓은 거야.”',
                       '“내가 이 년 동안 해야 했던 일을 적은 거야.”',
                       '“같은 게 아니야.” 그녀가 종이를 집어 들었다. “하지만 차이가 네가 어디 서 있느냐에 달릴 만큼은 가깝지. 앉아. 카운터 닦는 짓 하고 있어.”',
                       '그는 앉았다. 그녀도 맞은편에 앉았고 장부는 둘 사이에 놓였다. 거리는 일요일 소리를 냈다. 그녀가 말했다. “네 번째 것을 소리 내어 말해 봐. 네가 '
                       '쓰지 않은 것. 지켜봐야 할 남자로 보이게 하니까.”',
                       '그는 소리 내어 말했다. “두 번째로 서명하는 사람은, 자기가 두 번째 서명하는 그곳에서 자기 계정을 수리하지 않는다.”',
                       '“내 얘기가 아니야.” 그녀가 말했다.',
                       '“우리 둘 얘기야. 두 번째 서명을 주는 사람이 사건에 걸린 게 있다면 그 서명은 가치가 없다는 사실의 얘기지.”',
                       'Mara는 조용했다. 장부에서 펜을 들어 뚜껑을 열고 종이 뒷면, 그의 문장 아래에 서명했다. 작고 가지런히, 그녀가 모든 것에 서명하는 방식으로. “작업 '
                       '시작 전에 매 작업을 읽을게.” 그녀가 말했다. “다리가 무엇을 할지 고객에게 말하지 않은 작업에는 까다롭게 굴 거야. *가끔* 까다로운 게 아니라 '
                       '방침으로서 까다로운 거지.”',
                       '“좋아.” Elias가 말했고, 목소리에는 방에 두고 싶지 않은 안도가 섞여 나왔다.',
                       '그녀는 빛이 꺼질 때까지 머물렀다. 여전히 그녀의 가게 아닌 곳에 식료품을 정리해 넣었고, 그녀는 묻지 않은 두 번째 열쇠 세트를 챙겼다. 문가에서 그녀가 '
                       '한 말을 그는 첫 주 내내 곱씹게 된다. “열하루 닫아 둬도 관리청은 눈치채지 못했어. 내일 다시 열어도 관리청은 여전히 눈치채지 못할 거야. 함부로 해도 '
                       '된다는 이유가 아니야. 규칙을 글로 적어 둬야 한다는 이유지.”',
                       '월요일 아홉 시에 그는 장부의 깨끗한 첫 페이지를 펴고 그 위에 날짜를 적을 것이었다. 그날 밤 잠은 잘 오지 않았고, 이유는 규칙 때문이 아니었다.'],
            'title': '그 전의 일요일',
            'when': '11월 13일'},
     'tr': {'blocks': ['Dükkân on bir gündür kapalı duruyordu; toz her şeyin en küçük yerine kadar girmişti, '
                       'buna tezgâhın iki mengenesi üzerindeki keçe de dâhildi. Elias keçeleri bir diş '
                       'fırçasıyla temizledi; oraya ait olan fırça yazın ortadan kaybolmuştu, bu yüzden elinde '
                       'diş fırçası vardı.',
                       'Kapıyı açık bırakarak çalıştı. Pazar günü Cinder Lane, bir sokaktan çok bir sestir: '
                       'binaların arkasında bir yerden yükselen bir asansör, kendisi daha doğmadan çok önce '
                       'aynı giderlere akmaya başlamış ve hâlâ akan su, ve her hafta aynı saatte hiçliğe '
                       'havlayan bir köpek.',
                       'Defter, bıraktığı yerdeki tezgâhın üzerinde duruyordu, kapağı kapalıydı. Kalem '
                       "defterin üzerine çapraz konmuştu, Elias'ın sevmediği bir açıyla. Elias kalemi eline "
                       'aldı ve düzeltti; sonra durdu, kalemi yeniden aldı ve bir kez daha düzeltti. İşte o '
                       'zaman kendisini oyaladığını anladı.',
                       'Kural, tezgâhın üzerindeki bir kâğıt yaprağının üzerindeydi; kendi el yazısıyla '
                       'yazılmıştı ve bu onun üçüncü taslağıydı. Birinci taslak tek bir cümleden ibaretti. '
                       'İkinci taslak üzerine bir fıkra almış, sonrasında cesaretini yitirmişti. Bunu ayakta '
                       'yazmıştı; Elias, saklamayı düşünmediği şeyleri oturarak, saklamayı düşündüğü şeyleri '
                       'ise ayakta yazardı.',
                       '*Her çekirdekte iki el. İkili tezgâhtan önce adıyla belirtilir. Onarılsa da reddedilse '
                       'de iki ad defterde yer alır.*',
                       'Onu bir müşterinin fiyatı okuduğu gibi okudu; yani olduğu gibi alıp geri bırakacak bir '
                       'bakışla. Sonra kâğıdı çevirdi ve arkasına, daha küçük harflerle, ön yüzde söylenmeyen '
                       'şeyi yazdı: *İkinci ad tanık değildir. İkinci ad bir kayıttır.*',
                       'Mara saat dörde geldi; kendisine ait olmayan bir dükkân için alışveriş yapmıştı ve '
                       'elinde bir torba bakkal alışverişi vardı. Eşikte durdu; süpürülmüş zemini, elindeki '
                       'diş fırçasını, tezgâhın üzerindeki kâğıdı tek tek süzdü. Uzun süre hiçbir şey '
                       'söylemedi; o kadar uzun süre sustu ki Elias, zaten temiz olan tezgâhı silmeye başladı.',
                       '“Bunu yazmışsın,” dedi.',
                       '“Ben yazdım.”',
                       '“Bu kâğıdın arka yüzüne imza atmamı istiyorsun.”',
                       '“Önce onu okumanı istiyorum. Kâğıdın arkası, bir şeye mal olan kısım.”',
                       'Torbaları yere indirdi ve kâğıdın ön ile arka yüzünü ikişer kez okudu. Elias onu, bir '
                       'çekirdeğin yerine oturmasını izler gibi izliyordu; bakışının altında yüzeyin hareket '
                       'etmeyi bıraktığı o anı bekliyordu. O an kâğıdın arka yüzünde, *kayıt* kelimesinin '
                       'üstünde geldi. Geldiğinde kadın başını kaldırmadı; Elias bunu bekliyordu. Kadın buna '
                       'itiraz da etmedi; Elias bunu beklemiyordu.',
                       '“Dört-bir-bir-dokuz hâlâ askıda,” dedi. “Biliyorsun bunu. Koşullar karşılığında geri '
                       'açılacak. Koşullardan biri, lisansı askıda olmayan ikinci bir imza sahibi bulunması; o '
                       'kişi ben değilim. İkincisi, ikinci imza sahibinin adının, iş başlamadan önce o iş '
                       'üzerinde yazılı olması; o senin kendi cümlen. Üçüncüsü, iki adın da herhangi birinin '
                       "denetleyebileceği bir defterde yer alması. O da senin cümlen. Koruma Dairesi'nin "
                       'koşullarını kendi el yazınla yazıp kendi dükkânının duvarına astın.”',
                       '“İki yıldır yapmam gereken şeyi, sonunda yazdım,” dedi.',
                       '“İkisi aynı şey değil,” dedi. Kâğıdı eline aldı. “Ama birbirlerine o kadar yakınlar '
                       'ki, aradaki fark nerede durduğuna bağlı. Otur. Tezgâhla uğraşıp duruyorsun, o şeyi '
                       'yapıyorsun.”',
                       'Elias oturdu. Kadın karşısına oturdu; defter ikisinin arasında duruyordu. Sokak, pazar '
                       'günü seslerini çıkarmaya devam etti. “Dördüncüyü yüksek sesle söyle,” dedi. “Senin '
                       'yazmadığın şu kuralı. Çünkü o seni, gözetilmesi gereken bir adam gibi gösteriyor.”',
                       'Elias kuralı yüksek sesle söyledi. “İkinci imzayı atan kişi, ikinci imzayı attığı '
                       'yerde kendi kaydını onarmaz.”',
                       '“Bu benle ilgili değil,” dedi.',
                       '“İkimizle ilgili. Şu gerçekle ilgili: imzayı atan kişinin, o davada bir çıkarı varsa, '
                       'ikinci imza hiçbir değer taşımaz.”',
                       'Mara bir süre sustu. Sonra kalemi defterin üzerinden aldı, kapağını çıkardı, kâğıdın '
                       'arkasına, onun cümlesinin altına imza attı; her şeyi imzaladığı gibi, küçük ve düzgün, '
                       'satırla aynı hizada. “Her işi, sen başlamadan önce okuyacağım,” dedi. “Köprünün ne '
                       'yapacağının müşteriye anlatılmadığı işlerde de zorlu olacağım. *Ara sıra* zorlu değil. '
                       'İlke olarak zorlu.”',
                       '“İyi,” dedi Elias. Sesi, oda içinde taşımasını istediğinden daha fazla bir ferahlık '
                       'taşıyordu.',
                       'Işık sönene kadar kaldı. Alışverişi dükkâna birlikte yerleştirdiler; dükkân hâlâ onun '
                       "değildi. İkinci anahtar takımını, kendisine sorulmadan aldı. Kapıda dururken, Elias'ın "
                       'ilk hafta boyunca aklından çıkaramayacağı şeyi söyledi: “On bir gün dükkânı kapalı '
                       'tuttun, Koruma Dairesi fark etmedi. Yarın dükkân açılacak, Koruma Dairesi yine fark '
                       'etmeyecek. Bu, dikkatsiz olmak için bir sebep değil. Kuralın yazılı olması gerektiği '
                       'sebep işte bu.”',
                       'Pazartesi sabahı dokuzda defteri ilk temiz sayfaya açacak, tarihi o sayfanın en üstüne '
                       'yazacaktı. O gece iyi uyumadı. Uykusunun sebebi kural değildi.'],
            'title': 'Bir Önceki Pazar',
            'when': '13 Kasım'},
     'yue': {'blocks': ['間鋪閂咗十一日，塵走入晒所有罅，連織機兩個夾子上嘅毛氈都有塵。Elias 用牙刷清，因為本來屬於嗰個位嘅刷，夏天已經唔見咗。',
                        '佢開住門做嘢。禮拜日嘅 Cinder Lane 唔似一條街，似一種聲：樓後面某處嘅升降機、一條由佢未出世就已經流緊嘅去水渠，仲有一隻狗，每個禮拜同一個鐘數，對住冇嘢吠。',
                        '簿就擺喺佢放低嘅位置，合埋，筆打斜橫喺簿上面，個角度佢唔鍾意。佢擺正支筆。再擺正一次，然後明白自己係喺度拖。',
                        '規條寫喺櫃面一張紙上，係佢自己嘅字，已經係第三稿。第一稿一句。第二稿長出一個子句，又冇咗膽。呢一稿佢係企住寫嘅 —— 佢想留住嘅嘢，通常都係企住寫。',
                        '*每個記憶核兩隻手。動織機之前，先寫低合夥人。做完都好，拒絕都好，兩個名都要入簿。*',
                        '佢讀呢段嘢，好似客人讀價錢咁。然後翻轉張紙，喺背面用細啲嘅字寫低正面冇講嘅嗰句：*第二個名唔係證人。第二個名係一個戶口。*',
                        'Mara 四點鐘到，帶住一袋餸 —— 佢買嗰陣當呢間鋪係自己嘅。佢企喺門口，望住掃乾淨嘅地、支牙刷、張紙，靜到 Elias 開始抹櫃面，而個櫃面本身已經乾淨。',
                        '「你寫咗落去。」',
                        '「我寫咗落去。」',
                        '「你想我喺背面簽名。」',
                        '「我想你先讀。背面先係要付代價嗰 part。」',
                        '佢放低袋，兩面都讀咗兩次。Elias 望住佢讀，好似望住一個記憶核定形 —— '
                        '等表面唔再動嗰一刻。嗰一刻嚟到背面，嚟到「戶口」兩個字；嚟到嘅時候佢冇抬頭，呢樣佢預咗；佢亦冇駁嘴，呢樣佢冇預。',
                        '「四一一九仲停緊牌，」佢話。「你知。復牌有條件：其中一條係第二個簽名人要有牌，而個牌冇停 —— 唔係我；第二條係第二個簽名嘅人要喺動工前入簿 —— '
                        '呢句係你寫嘅；第三條係兩個名都要落喺一本審得到嘅簿 —— 呢句都係你寫嘅。你親手寫低管理局嘅條件，掛喺自己鋪頭。」',
                        '「我寫低咗我兩年嚟本該做嘅事。」',
                        '「呢兩樣唔係同一件事。」佢執起張紙。「但近到只差你企喺邊。坐低。你又喺度搞個櫃面。」',
                        '佢坐低。佢坐對面，簿攤喺兩個人中間，條街做佢禮拜日嘅聲。佢話：「第四條，讀出聲。你冇寫落去嗰條 —— 因為寫咗，你就似一個要人盯住嘅人。」',
                        '佢讀出聲：「簽第二個名嘅人，喺佢簽第二個名嘅地方，唔可以修自己個戶口。」',
                        '「呢條唔係講我。」',
                        '「係講我哋兩個。係講：如果簽第二個名嘅人袋入面有嘢，呢個第二簽名一文不值。」',
                        'Mara '
                        '冇出聲。然後佢喺簿上拎起支筆，除筆蓋，喺佢嗰句下面簽咗自己個名，細而平，同佢簽所有嘢一樣。「每一單，你開工之前我都會讀，」佢話。「同埋客人未知道條橋會對佢間房做咩嘅嗰啲，我會麻煩。唔係有時麻煩 '
                        '—— 係政策上麻煩。」',
                        '「好。」Elias 話，講出口嘅時候，鬆一口氣嘅程度超過佢想喺呢間房入面露出嚟嘅。',
                        '佢留到光都收。佢哋將餸放入一間仲未算係佢嘅鋪，佢冇問就拎走第二串鎖匙。臨出門佢講咗一句，Elias '
                        '之後整個禮拜都會諗：「你閂咗十一日，管理局冇留意。聽日重開，管理局都唔會留意。呢個唔係大意嘅理由 —— 呢個就係規條要寫落紙嘅理由。」',
                        '禮拜一，九點，佢會打開簿，翻到第一張乾淨嘅頁，喺頂寫日期。嗰晚佢瞓得唔好，而原因唔係規條。'],
             'title': '前一晚，禮拜日',
             'when': '11 月 13 日'}},
 7: {'en': {'blocks': ['The girl came at seven in the morning, which was not the hour on the card, and Elias '
                       'knew before she said anything that she had come early because she had been afraid of '
                       'being late.',
                       'She was nineteen. She stood in the doorway with her hands where a person puts their '
                       'hands when they have decided not to put them in their pockets, and she said her name '
                       'twice, the second time with the first name only, as if the surname had been '
                       'over-egged.',
                       '“Wren Adey,” she said. “Wren.”',
                       "“You're early.”",
                       "“I know. The bus was early. I could wait outside but there's nowhere to wait outside "
                       "that isn't a doorway.”",
                       'He let her in because the alternative was a nineteen-year-old standing on Cinder Lane '
                       'for an hour in February, and because he had already made one decision that morning '
                       'that he was not proud of.',
                       'The trial was one day, unpaid, and the terms were on an index card: no touching a core '
                       'on the first day, no opinions about customers, and read the ledger before touching '
                       'anything at all. He handed her the card. She read it twice. Then she read the ledger, '
                       'all of it, sitting on the stool with her coat still on, for fifty minutes, and at the '
                       'end she closed it and said the thing that got her hired.',
                       '“This is a book about refusals,” she said. “There are more refusals than repairs in '
                       "the back half, and in the front half there aren't, and the difference isn't the "
                       "customers. It's the second signature.”",
                       "Elias had thought of it as a book about the shop. He did not say so. He said, “What's "
                       'the fourth condition for?” — because it was the hardest thing in the ledger and he '
                       'wanted to see what she would do with it.',
                       'She turned back four pages without hesitating, which meant she had memorised where it '
                       'was, which meant she had read it as a document and not as a story. “It stops the '
                       'second signature being a courtesy,” she said. “If the person signing second can repair '
                       'their own account at the same bench, then the second name is just a person standing '
                       'nearby. The fourth condition makes the second name cost something.”',
                       '“And what does it cost?”',
                       '“The right to be comfortable,” Wren said, and then looked at her own hands as though '
                       'she had heard herself.',
                       'The first core of the day was a wedge, forty years old, the kind of damage where the '
                       'customer cannot say when it happened, only that there used to be more of it. Elias '
                       'worked with her watching, narrating as he went, because narration is how you find out '
                       'whether somebody is following the loom or following you. She was following the loom. '
                       "At the third clamp she said, “You're going to stop there.”",
                       '“Why?”',
                       "“Because the next two centimetres are the part where the customer's sister is "
                       "standing, and if you bridge through her you'll give him a sister who is the same in "
                       "every particular except that she doesn't move.”",
                       'She was right. It was not a difficult deduction; it was the deduction the whole trade '
                       'was built on avoiding, because the customer pays for a whole room and a whole room has '
                       'people in it. Elias put the clamp down and looked at the clock and understood, with '
                       'the specific discomfort of a man whose shop has been quiet for eleven days, that he '
                       'was going to have to explain the word *no* to somebody who was going to be very good '
                       'at the work.',
                       'Mara came at ten to read the second account on the jobs, which was the rule, and found '
                       'a girl she had not been told about. The two of them went out to the doorway and talked '
                       'for six minutes while Elias pretended to work on the wedge. When they came back Mara '
                       "said, “She's not licensed, so she can't sign. She can hold.”",
                       '“I know what holding is,” Wren said, a little too quickly.',
                       "“You know what it's called,” Mara said. “You don't know what it costs yet, and that's "
                       "fine, that's what the sixty-four chapters are for.” She said it without irony, the way "
                       'she said most things, and Wren had the sense to write it down instead of answering.',
                       "The card said unpaid. At four o'clock Elias paid her for the day out of the till and "
                       "told her to come back on Monday, and she said, “I'll be early,” and he said, “I know.”",
                       'That evening he wrote the hire into the ledger in two lines, and then sat with the pen '
                       'for a while, because the next thing he wanted to write was not something a ledger is '
                       'for. He wrote it anyway, on the inside of the back cover, where the audits do not '
                       'reach: *She read the book before she read the loom. Somebody taught her that, and it '
                       "wasn't me.*"],
            'title': 'The Trial Morning',
            'when': '28 February'},
     'ko': {'blocks': ['소녀는 아침 일곱 시에 왔다. 그 시간은 카드에 적힌 시간이 아니었다. Elias는 그녀가 무엇을 말하기 전에 이미, 그녀가 늦을까 봐 두려워서 일찍 온 '
                       '것이라는 걸 알았다.',
                       '그녀는 열아홉 살이었다. 현관에 서서, 손을 주머니에 넣지 않기로 결심한 사람이 두 손을 두는 자리에 손을 두고 있었다. 그리고 이름을 두 번 말했다. 두 '
                       '번째에는 이름만 말했고, 성이 지나치게 부풀려진 것처럼 보였다.',
                       '“Wren Adey.” 그녀가 말했다. “Wren이에요.”',
                       '“일찍 왔네.”',
                       '“알아요. 버스가 일찍 왔어요. 밖에서 기다릴 수도 있지만 밖에는 현관문 아닌 기다릴 곳이 없어요.”',
                       '그는 들여보냈다. 다른 선택지는 이월에 열아홉 살짜리가 Cinder Lane에 한 시간 서 있는 거였고, 그날 아침 그는 자랑스럽지 못한 결정을 하나 이미 '
                       '내렸기 때문이었다.',
                       '시험은 하루, 무급이었고 조건은 인덱스 카드에 적혀 있었다. 첫날 코어를 만지지 말 것, 고객에 대한 의견을 내지 말 것, 무엇이든 만지기 전에 장부를 '
                       '읽을 것. 그는 카드를 건넸다. 그녀는 두 번 읽고 코트를 입은 채 의자에 앉아 장부를 처음부터 끝까지 오십 분 동안 읽었으며, 마지막에 덮고 그녀를 '
                       '채용하게 만든 한마디를 말했다.',
                       '“이건 거절에 관한 책이에요.” 그녀가 말했다. “뒤쪽 절반에는 수리보다 거절이 더 많고, 앞쪽 절반에는 그렇지 않아요. 그 차이는 고객 때문이 아니에요. '
                       '두 번째 서명 때문이에요.”',
                       'Elias는 그것을 가게에 관한 책이라고 생각해 왔다. 그는 그렇게 말하지 않았다. “네 번째 조건은 무엇을 위한 거지?” 라고 물었다. 장부에서 가장 '
                       '어려운 부분이었고, 그녀가 그것을 어떻게 다룰지 보고 싶었다.',
                       '그녀는 머뭇거리지 않고 네 페이지를 뒤로 넘겼다. 위치를 외웠다는 뜻이고, 이야기가 아니라 문서로 읽었다는 뜻이었다. “두 번째 서명이 예의로 끝나지 않게 '
                       '해요.” 그녀가 말했다. “두 번째로 서명하는 사람이 같은 작업대에서 자기 계정을 수리할 수 있다면 두 번째 이름은 곁에 서 있는 사람일 뿐이에요. 네 '
                       '번째 조건은 두 번째 이름에 대가를 만들어요.”',
                       '“그럼 무엇을 대가로 치르지?”',
                       '“편안할 권리요.” Wren가 말하고 나서, 자기 자신의 말을 들은 듯 자기 손을 내려다보았다.',
                       '그날 첫 코어는 사십 년 된 쐐기형 손상이었다. 고객은 언제 그것이 생겼는지 말하지 못하고, 예전에는 더 많았다는 것만 아는 종류였다. Elias는 그녀가 '
                       '지켜보는 가운데 일하면서 해 나가는 대로 설명했다. 설명해 보면 누가 직조기를 따르는지 자기를 따르는지 알 수 있기 때문이었다. 그녀는 직조기를 따르고 '
                       '있었다. 세 번째 집게에서 그녀가 말했다. “거기서 멈추시겠어요.”',
                       '“왜?”',
                       '“다음 이 센티미터는 고객의 누이가 서 있는 자리예요. 그녀를 지나 다리를 놓으면, 움직이지 않는다는 점을 빼고는 모든 면에서 똑같은 누이를 그가 갖게 '
                       '돼요.”',
                       '그녀는 옳았다. 어려운 추리는 아니었다. 하지만 그 추리는 업계 전체가 피하도록 세워진 종류였다. 고객은 방 전체에 대한 값을 치르고 방 전체에는 사람들이 '
                       '있기 때문이었다. Elias는 집게를 내려놓고 시계를 쳐다보았다. 열하루 동안 가게가 조용했던 남자가 느끼는 특유한 불편함과 함께, 앞으로 일솜씨가 아주 '
                       '좋아질 누군가에게 *아니오* 라는 말을 설명해야 하게 될 거라는 걸 깨달았다.',
                       'Mara는 열 시에 작업들의 두 번째 계정을 읽으러 왔다. 규칙대로였다. 그리고 자기에게 말하지 않은 소녀를 발견했다. 둘은 현관으로 나가 육 분 동안 '
                       '이야기했고, Elias는 쐐기 손상을 만지는 체했다. 돌아와 Mara가 말했다. “면허가 없으니 서명은 못 해. 잡아 줄 수는 있어.”',
                       '“잡는 일이 뭔지 알아요.” Wren가 조금 빠르게 대꾸했다.',
                       '“이름만 아는 거지.” Mara가 말했다. “그게 무엇을 대가로 치르는지는 아직 모르고, 그래도 돼. 그걸 알려는 데 예순네 개 장이 있는 거야.” 그녀는 '
                       '자신의 말 대부분을 그러듯 비꼬지 않고 말했고, Wren는 대답 대신 적어 둘 분별력이 있었다.',
                       '카드에는 무급이라고 적혀 있었다. 네 시에 Elias는 금전 등록기에서 그날 치를 주고 월요일에 다시 오라고 했다. 그녀가 “일찍 올게요.” 하자 그는 '
                       '“알아.” 라고 대답했다.',
                       '그날 저녁 그는 채용 내용을 장부에 두 줄로 적고, 한동안 펜을 들고 앉아 있었다. 다음으로 쓰고 싶은 것은 장부가 담을 일이 아니었기 때문이었다. 그래도 '
                       '그는 감사가 닿지 않는 뒷표지 안쪽에 적었다: *그녀는 직조기를 읽기 전에 책을 읽었다. 누군가 그걸 가르쳤고, 그 사람은 내가 아니었다.*'],
            'title': '시험의 아침',
            'when': '2월 28일'},
     'tr': {'blocks': ['Kız sabahın yedisinde dükkâna gelmişti; kartın üzerinde yazılı olan saat bu değildi. '
                       'Daha bir şey söylemeden önce Elias anlamıştı: kız erken gelmişti, çünkü geç kalmaktan '
                       'korkmuştu.',
                       'Kız on dokuz yaşındaydı. Eşikte duruyordu; ellerini, cebe koymamaya karar vermiş '
                       'birinin koyduğu yere koymuştu. Adını iki kez söyledi; ikinci kez yalnızca kendi adını '
                       'kullandı, sanki soyadı fazla koyulaştırılmış, sonradan geride bırakılmak istenmişti.',
                       '“Wren Adey,” dedi. “Wren.”',
                       '“Erken gelmişsin.”',
                       '“Biliyorum. Otobüs erkendi. Dışarıda bekleyebilirdim ama dışarıda bekleyebileceğim, '
                       'kapı eşiği olmayan bir yer yok.”',
                       "Elias içeri girmesine izin verdi; alternatif, Şubat ayında Cinder Lane'in üzerinde bir "
                       'saat boyunca dikilecek on dokuz yaşında bir kızdı, ve Elias o sabah gurur duymadığı '
                       'bir kararı zaten vermişti.',
                       'Deneme süresi tek bir gündü, ücret ödenmiyordu; koşullar bir indeks kartının üzerinde '
                       'yazılıydı: ilk gün hiçbir çekirdeğe dokunmayacaktı, müşteriler hakkında hiçbir görüş '
                       'beyân etmeyecekti, daha hiçbir şeye dokunmadan önce defteri okuyacaktı. Elias kartı '
                       'ona uzattı. Kız kartı iki kez okudu. Sonra defteri okudu; tamamını, ceketi hâlâ '
                       'üzerinde, taburede oturarak, elli dakika boyunca. En sonunda defteri kapattı ve onu '
                       'işe alan şeyi söyledi.',
                       '“Bu kitap, retler hakkında bir defter,” dedi. “Defterin arka yarısında onarımlardan '
                       'daha fazla ret bulunuyor; ön yarıda ise durum böyle değil. Aradaki fark müşterilerden '
                       'gelmiyor. Fark, ikinci imzada.”',
                       'Elias, o defteri dükkân hakkında bir kitap olarak düşünmüştü. Bunu ona söylemedi. '
                       '“Dördüncü koşul ne için?” diye sordu; çünkü bu koşul defterdeki en zor şeydi ve Elias, '
                       'kızın bu şeyle ne yapacağını görmek istiyordu.',
                       'Tereddüt etmeden dört sayfa geri çevirdi; bu, o koşulun yerini bellemiş olduğu '
                       'anlamına geliyordu, ki defteri bir hikâye gibi değil, bir belge gibi okuduğu anlamına '
                       'geliyordu. “İkinci imzanın bir nezaket gösterisi olmasını engeller,” dedi. “İkinci '
                       'imzayı atan kişi aynı tezgâhta kendi kaydını onarabiliyorsa, ikinci ad yalnızca '
                       'yakında duran bir insandan ibarettir. Dördüncü koşul, ikinci adın bir şeye mal '
                       'olmasını sağlar.”',
                       '“Neye mal olur peki?”',
                       '“Rahat olma hakkına,” dedi Wren. Sonra, sanki kendi sesini yeni duymuş gibi, kendi '
                       'ellerine baktı.',
                       'Günün ilk çekirdeği bir kamaydı; kırk yaşındaydı ve öyle bir hasar türüydü ki müşteri '
                       'ne zaman olduğunu söyleyemiyor, yalnızca eskiden hasarın daha fazla olduğunu '
                       'söyleyebiliyordu. Elias çalışırken kız onu izliyordu; Elias ilerledikçe başından '
                       'geçenleri anlatıyordu, çünkü kişi seni mi yoksa tezgâhı mı izlediğini anlatılarak '
                       'anlarsın. Kız tezgâhı izliyordu. Üçüncü mengenede konuştu: “Orada duracaksın.”',
                       '“Neden?”',
                       '“Çünkü sonraki iki santimetre, müşterinin ablasının durduğu kısımdır. Eğer onun '
                       'üzerinden bir köprü kurarsan, müşteriye her ayrıntısıyla aynı olan, ama hareket '
                       'etmeyen bir abla vermiş olursun.”',
                       'Kız haklıydı. Bu zor bir çıkarım değildi; bütün mesleğin kaçınmak üzere kurulduğu '
                       'çıkarımdı bu, çünkü müşteri bütün bir oda için öder ve bütün bir odanın içinde '
                       'insanlar bulunur. Elias mengeneyi yere bıraktı, saatine baktı ve dükkânı on bir gündür '
                       'sessiz kalmış bir adamın o özel rahatsızlığıyla, bu işte çok iyi olacak birine *hayır* '
                       'kelimesini açıklamak zorunda kalacağını anladı.',
                       'Mara saat onda geldi; kural gereği o günki işlerin ikinci kaydını okumaya gelmişti ve '
                       'kendisine söz edilmemiş bir kız buldu. İkisi birlikte dışarı, kapı eşiğine çıktı ve '
                       'altı dakika boyunca konuştular; Elias kamayla çalışıyormuş gibi yaptı. Geri '
                       'döndüklerinde Mara konuştu: “Lisansı yok, bu yüzden imza atamaz. Çerçeve tutabilir.”',
                       '“Çerçeve tutmanın ne olduğunu biliyorum,” dedi Wren, biraz fazla çabuk.',
                       '“Adının ne olduğunu biliyorsun,” dedi Mara. “Henüz neye mal olduğunu bilmiyorsun, ve '
                       'bu da önemli değil; altmış dört bölümün amacı zaten budur.” Mara bunu çoğu şeyi '
                       'söylediği gibi, alay karıştırmadan söyledi; Wren de cevap vermek yerine, bunu yazıya '
                       'geçirme inceliğini gösterdi.',
                       'Kartın üzerinde ücretsiz yazıyordu. Saat dörtte Elias günün parasını kasadan ödedi ve '
                       'ona pazartesi günü geri gelmesini söyledi. Kız, “Erken geleceğim,” dedi; Elias da, '
                       '“Biliyorum,” dedi.',
                       'O akşam bu işe almayı deftere iki satır hâlinde yazdı; sonra kalemi elinde bir süre '
                       'oturdu, çünkü yazmak istediği sonraki şey bir defterin amacı değildi. Yine de yazdı; '
                       'arka kapağın iç tarafına, denetimlerin ulaşamadığı yere: *Önce defteri okudu, sonra '
                       'tezgâhı. Bunu ona biri öğretti, ben değildim.*'],
            'title': 'Deneme Sabahı',
            'when': '28 Şubat'},
     'yue': {'blocks': ['個女仔七點鐘到，唔係卡上寫嘅鐘數。Elias 未聽佢講就知：佢早到，因為佢驚遲到。',
                        '佢十九歲。企喺門口，雙手擺喺一個人決定唔插袋嘅時候會擺嘅位；佢講咗自己個名兩次，第二次只講名，好似姓氏講多咗。',
                        '「Wren Adey，」佢話。「Wren。」',
                        '「你早到。」',
                        '「我知。巴士早到。我可以喺外面等，但出面冇一個唔係門口嘅地方可以等。」',
                        '佢放佢入去，因為另一個選擇係一個十九歲嘅人喺二月嘅 Cinder Lane 企一個鐘；亦因為佢嗰朝早已經做咗一個佢唔自豪嘅決定。',
                        '試工一日，冇錢。條款寫喺一張索引卡：第一日唔准掂記憶核、唔准有意見講客人、掂任何嘢之前先讀簿。佢遞張卡過去。佢讀咗兩次。然後佢讀簿，成本，坐喺凳上，外套仲未除，讀咗五十分鐘；讀完合上，講咗一句令佢被請嘅話。',
                        '「呢本係一本講拒絕嘅書，」佢話。「後半部拒絕多過修補；前半部冇咁多。差別唔係客人，係第二個簽名。」',
                        'Elias 一直當呢本係一本講間鋪嘅書。佢冇講出口。佢問：「第四條用嚟做咩？」—— 因為嗰條係簿入面最難嘅一條，佢想睇佢點接。',
                        '佢冇猶豫就翻返四頁，即係佢記住咗位置，即係佢當佢係一份文件，唔係一個故事。「佢令第二個簽名唔可以係人情，」佢話。「如果簽第二個名嘅人可以喺同一張檯修自己個戶口，個第二個名就只係一個人企喺隔籬。第四條令個第二個名要付代價。」',
                        '「付咩代價？」',
                        '「舒服嘅權利，」Wren 話，然後低頭望自己雙手，好似啱啱聽到自己講咗咩。',
                        '當日第一個記憶核係一個楔形，四十年，嗰種客人講唔出幾時發生、只講得出以前多啲嘅損傷。Elias '
                        '做，佢喺側邊睇；佢一路做一路講，因為講解係測試一個人跟住織機定跟住你嘅方法。佢跟住織機。去到第三個夾，佢話：「你會喺呢度停。」',
                        '「點解？」',
                        '「因為再過兩厘米就係客人個妹企嘅位。你穿過佢搭橋，就會畀佢一個妹 —— 每一樣都一樣，除咗佢唔會動。」',
                        '佢講得對。呢個唔係難嘅推論；係整個行業建嚟避開嘅推論，因為客人付錢買一間完整嘅房，而一間完整嘅房入面有人。Elias '
                        '放低夾子，望鐘，帶住一個鋪頭靜咗十一日嘅人嘅特別唔舒服，明白自己將要同一個會做得非常好嘅人解釋「唔」呢個字。',
                        'Mara 十點到，讀當日嘅第二個戶口 —— 呢個係規條；佢發現一個冇人同佢講過嘅女仔。兩個人出咗去門口講咗六分鐘，Elias 假裝做個楔形。返入嚟 Mara '
                        '話：「佢冇牌，唔可以簽。佢可以揸住。」',
                        '「我知乜嘢係揸住，」Wren 講得太快。',
                        '「你知個名，」Mara 話。「你仲未知要付咩，唔緊要 —— 六十四章就係用嚟學呢樣。」佢講嘅時候冇諷刺，同佢講大部分嘢一樣；Wren 有分寸，寫低佢，冇駁。',
                        '卡上寫冇錢。四點鐘 Elias 喺收銀機度畀咗當日錢，叫佢禮拜一再嚟；佢話「我會早到」，佢話「我知」。',
                        '嗰晚佢喺簿上寫咗兩行請人；然後揸住支筆坐咗一陣，因為佢想寫嘅下一句，唔係簿嘅用途。佢照寫，寫喺後封面內側，審計去唔到嘅地方：*佢讀完本書先讀織機。有人教佢咁做，唔係我。*'],
             'title': '試工嗰朝',
             'when': '2 月 28 日'}},
 8: {'en': {'blocks': ["The list came on a Wednesday, four pages, stapled, with the Ward's crest at the top of "
                       'the first page and no letter with it. Mara had asked for it in writing nine weeks '
                       'earlier and had been told it did not exist in that form; now it existed in that form, '
                       'which is how the Ward apologises.',
                       'Two hundred and eleven addresses. Nine of them were on streets Elias had never walked, '
                       'which meant they were on streets that had been built after he stopped paying attention '
                       'to the edge of the district.',
                       "“It's not a list of patients,” Mara said, reading over his shoulder. “There's no "
                       "diagnosis column. It's a list of addresses where somebody answered a question in a "
                       'certain way on a form.”',
                       '“Which question?”',
                       '“The one about whether anything has changed in the last twelve months that you would '
                       'not describe to a neighbour.”',
                       'They took the first page and walked it, because a list of two hundred and eleven is a '
                       'document and a list of eleven is a morning. The first four addresses were nothing: a '
                       'woman who had moved, a shop with the shutters down, a building with the entryphone '
                       'broken, a man who opened the door four inches and said his mother was fine, thank you, '
                       'and shut it.',
                       'The fifth was a kitchen. The door was opened by a woman of about forty in a coat with '
                       'the bus still on it, and behind her a man was watering three tomato plants on the '
                       'windowsill, one plant at a time, in a way that had the shape of a habit and none of '
                       'the hurry of one.',
                       '“He does that every day,” the woman said, quietly, in the doorway, not quietly enough. '
                       "“Twice a day. He doesn't know why. He says the plants need it. They don't need it "
                       'twice.”',
                       'Elias watched the man put the can down, lift the second pot, turn it a quarter turn, '
                       'and water it from the side away from the window. “How long?”',
                       '“Two years. It was the clinic on the corner. He had it done properly. They gave us the '
                       'receipt and everything.”',
                       '“Is he in pain?”',
                       "“He's not in anything.” She said it like a diagnosis she had been carrying in her "
                       "pocket. “He's not sad. He's not happy either, but he doesn't mind that. He's —” she "
                       'looked for the word and found an ordinary one — “ tidy.”',
                       'Inside the flat there was a shelf of photographs and a calendar with the days crossed '
                       'off up to today, and a newspaper folded to the crossword with the crossword complete. '
                       'Everything in the room had been done. That was the thing Elias could not stop looking '
                       'at: not neglect, not damage, but a room in which every task had been finished by '
                       'somebody who was not there.',
                       'He asked the questions he was required to ask — when it began, who had done the '
                       'repair, whether there was a second name on the paperwork — and the woman went to a '
                       "drawer and brought out a folder with the clinic's papers in it, and the paperwork had "
                       'one name on it.',
                       "“There's supposed to be two,” Elias said.",
                       "“There's one,” the woman said. “Does it matter now?”",
                       'It mattered, and he could not say why in a kitchen, to a woman holding a folder with '
                       'the bus still on her coat. What he said was, “Can I come back on Friday? With someone. '
                       "I'd like to look at what he's holding, not what he's missing.”",
                       "“You can come back,” she said. “He won't mind. He doesn't mind anything. That's the "
                       'whole problem.”',
                       "On the stairs Mara said, “You're going to take the job.”",
                       "“I don't know yet.”",
                       "“You are. You're going to take a job where the repair is already finished and the only "
                       'thing left to fix is the record.” She held the list up. “There are two hundred and ten '
                       'more of these. If you take them one at a time, this shop becomes a very slow apology.”',
                       "“What's the alternative?”",
                       "“You take them one at a time and you write it all down,” Mara said. “That's not the "
                       "alternative. That's the only version of this that isn't a lie.”",
                       'They walked the rest of the first page because the light was still good, and by the '
                       'seventh door Elias had stopped counting the ones who were fine. It was not the number '
                       'that stayed with him. It was the third plant, turned a quarter turn, watered from the '
                       'side away from the window — a man doing something perfectly, twice a day, for nobody.',
                       'That evening he put the four pages in the ledger, folded once, and wrote above them: '
                       '*Received 2 May. Not a customer list. A condition of the district. Eleven doors '
                       'walked, one true.*'],
            'title': 'Two Hundred and Eleven Doors',
            'when': '2 May'},
     'ko': {'blocks': ['목록은 수요일에 왔다. 네 장을 스테이플로 묶었고 첫 페이지 머리에는 관리청 휘장이 있었으며, 편지는 함께 오지 않았다. Mara는 아홉 주 전에 글로 '
                       '이것을 요청했고, 그런 형태로는 존재하지 않는다는 대답을 들은 바 있었다. 지금 그것이 그런 형태로 존재하고 있었다. 관리청이 사과하는 방식이었다.',
                       '주소가 이백열한 개 있었다. 그중 아홉 곳은 Elias가 한 번도 걸어 본 적 없는 거리에 있었고, 그가 구역 가장자리에 신경 쓰기를 그만둔 뒤에 생긴 '
                       '거리들이었다는 뜻이었다.',
                       '“환자 명단은 아니야.” Mara가 그의 어깨 너머로 읽으며 말했다. “진단을 적는 칸도 없어. 양식에서 어떤 질문에 특정한 방식으로 답한 사람들의 주소 '
                       '목록이지.”',
                       '“어떤 질문?”',
                       '“지난 십이 개월 동안, 이웃에게 설명하고 싶지 않은 어떤 변화가 있었는지를 묻는 질문.”',
                       '그들은 첫 페이지를 들고 걸어 나갔다. 이백열한 개짜리 목록은 문서이고 열한 개짜리 목록은 하루 아침이라는 차이 때문이었다. 처음 네 주소는 아무것도 '
                       '아니었다. 이사 간 여자, 셔터를 내린 가게, 초인종이 고장 난 건물, 문을 네 인치만 열어 어머니는 괜찮다고 고맙다고 하고 문을 닫은 남자.',
                       '다섯 번째는 부엌으로 이어지는 집이었다. 현관문을 연 것은 버스 표시가 아직 코트에 붙어 있는 사십 살쯤의 여자였고, 그녀 뒤 남자가 창틀의 토마토 세 '
                       '그루에 물을 주고 있었다. 한 그루씩, 습관의 모양은 가지고 있으나 습관의 서두름은 없는 방식으로.',
                       '“매일 저래요.” 여자가 현관에서 조용히, 그러나 충분히 조용하지 않게 말했다. “하루 두 번요. 왜 하는지는 몰라요. 식물이 필요로 한다고 해요. 두 '
                       '번씩은 필요 없는데.”',
                       'Elias는 남자가 물 주전자를 내려놓고 두 번째 화분을 들어 사분의 일 회전시키고 창문 반대편에서 물 주는 것을 보았다. “얼마나 됐죠?”',
                       '“이 년 정도 됐어요. 모퉁이에 있는 클리닉에서 했어요. 제대로 해 줬어요. 영수증이랑 모든 걸 다 주더라고요.”',
                       '“고통을 느끼고 있나요?”',
                       '“아무것도 느끼지 않아요.” 그녀는 주머니에 넣고 다니던 진단처럼 그렇게 말했다. “슬프지도 않고 행복하지도 않은데, 그건 개의치 않아요. 그는 —” '
                       '단어를 찾다가 평범한 것을 골랐다 — “정돈돼 있어요.”',
                       '집 안에는 사진이 꽂힌 선반과 오늘까지 날짜를 친 달력이 있고, 십자말풀이가 다 풀린 채 접힌 신문이 놓여 있었다. 방 안의 모든 일은 끝나 있었다. '
                       'Elias가 계속해서 눈을 떼지 못한 것은 그것이었다. 방치도 손상도 아니라, 자기 없는 사람이 모든 일을 마쳐 둔 방이었다.',
                       '그는 물어야 할 질문을 순서대로 물었다. 언제 시작됐는지, 누가 수리했는지, 서류에 두 번째 이름이 있는지. 그러자 여자는 서랍으로 가 클리닉 서류가 든 '
                       '폴더를 꺼냈고, 서류에는 이름이 하나만 적혀 있었다.',
                       '“둘 이어야 하는데.” Elias가 말했다.',
                       '“하나예요.” 여자가 말했다. “지금 와서 중요해요?”',
                       '중요했지만 부엌에서, 코트에 버스 표시가 붙은 폴더를 든 여자에게 이유를 말할 수 없었다. 그가 말한 것은 이것이었다. “금요일에 다시 와도 될까요? 함께 '
                       '사람을 데리고요. 그가 놓친 게 아니라 지닌 것을 보고 싶어서요.”',
                       '“다시 와도 돼요.” 여자가 말했다. “신경 안 쓸 거예요. 아무것도 신경 안 써요. 그게 문제 전부죠.”',
                       '계단에서 Mara가 말했다. “그 일을 맡을 거지.”',
                       '“아직은 모르겠어.”',
                       '“맡을 거야. 수리는 이미 끝나 있고, 고쳐야 할 기록만 남은 일을.” 그녀가 목록을 들어 올렸다. “이런 게 이백열 개 더 있어. 하나씩 맡아 가면 이 '
                       '가게는 아주 느린 사과가 돼.”',
                       '“다른 선택지는?”',
                       '“하나씩 맡아 전부 적어 내리는 거지.” Mara가 말했다. “그건 대안이 아니야. 이 일에서 거짓이 아닌 유일한 버전이지.”',
                       '빛이 아직 좋아서 첫 페이지 나머지를 걸었다. 일곱 번째 문쯤 Elias는 괜찮다는 대답을 하는 사람들을 세는 걸 그만뒀다. 마음에 남은 것은 숫자가 '
                       '아니었다. 사분의 일 회전되고 창문 반대편에서 물 준 세 번째 식물이었다. 하루 두 번, 아무도 위한 것 없이 일을 완벽하게 해내는 남자.',
                       '그날 저녁 네 장을 한 번 접어 장부에 넣고 그 위에 적었다: *5월 2일 접수. 고객 명단 아님. 구역의 한 조건. 열한 문을 걸어 하나가 참됨.*'],
            'title': '이백열한 개의 문',
            'when': '5월 2일'},
     'tr': {'blocks': ['Liste bir Çarşamba günü geldi; dört sayfaydı, zımbalıydı, ilk sayfanın en üstünde '
                       "Koruma Dairesi'nin arması vardı, yanında tek bir mektup bile yoktu. Mara bunu dokuz "
                       'hafta önce yazılı olarak istemiş, o biçimde olmadığı kendisine söylenmişti; şimdi o '
                       'biçimde vardı. Koruma Dairesi böyle özür diler.',
                       "İki yüz on bir adres vardı. Bunlardan dokuzu, Elias'ın hiç yürümediği sokaklardaydı; "
                       'bu, çevrenin ucuna dikkat etmeyi bıraktıktan sonra yapılmış sokaklar demekti.',
                       '“Hasta listesi değil,” dedi Mara, omzunun üzerinden okuyarak. “Teşhis sütunu yok bu '
                       'listede. Bir formda, bir soruya belirli bir biçimde cevap vermiş kişilerin adres '
                       'listesi.”',
                       '“Hangi soru?”',
                       '“Son on iki ay içinde, komşuna anlatmayacağın bir şeyin değişip değişmediğiyle ilgili '
                       'soru.”',
                       'İlk sayfayı alıp adresleri tek tek gezdiler; çünkü iki yüz on birlik liste bir '
                       'belgedir, on birlik liste ise bir sabah eder. İlk dört adres boş çıktı: taşınmış bir '
                       'kadın, kepengi indirilmiş bir dükkân, kapı telefonu bozuk bir bina, kapıyı dört parmak '
                       'aralayıp annesinin iyi olduğunu, sağ ol, söyleyen ve kapıyı kapatan bir adam.',
                       'Beşinci adres bir mutfaktı. Kapıyı, otobüs bileti hâlâ ceketinin üzerinde duran kırk '
                       'yaşlarında bir kadın açtı. Kadının arkasında bir adam, pencere pervazındaki üç domates '
                       'fidesini suluyordu; birer birer, bir alışkanlığın biçimi olan, ama alışkanlıktaki '
                       'hiçbir aceleyi taşımayan bir biçimde.',
                       '“Her gün yapıyor,” dedi kadın, eşikte, yeterince sessiz olmayan bir sesle. “Günde iki '
                       'kez. Neden yaptığını bilmiyor. Bitkilerin buna ihtiyacı olduğunu söylüyor. Oysa iki '
                       'kez buna ihtiyaçları yok.”',
                       'Elias adamı izledi: sulama kabını yere indirişini, ikinci saksıyı kaldırışını, saksıyı '
                       'çeyrek tur çevirişini, pencereden uzak taraftan sulayışını. “Ne zamandır böyle '
                       'yapıyor?”',
                       '“İki yıldır. Köşedeki klinikte yaptırdı. Düzgün bir onarım oldu. Makbuzu falan her '
                       'şeyi verdiler.”',
                       '“Acı çekiyor mu?”',
                       '“Hiçbir şeyin içinde değil.” Bunu, cebinde uzun süredir taşıdığı bir teşhis gibi '
                       'söyledi. “Üzgün değil. Mutlu da değil, ama buna aldırmıyor. O —” kelimeyi aradı, '
                       'sıradan bir kelime buldu — “düzenli.”',
                       'Dairenin içinde fotoğrafların olduğu bir raf, günleri bugüne kadar çizilerek silinmiş '
                       'bir takvim, ve bulmacası tamamlanmış gazete bulmacasına kadar katlanmış bir gazete '
                       "vardı. Odadaki her şey yapılmıştı. Elias'ın bakmaktan kendini alamadığı şey buydu: "
                       'ihmalkârlık değildi, hasar değildi; her işin, orada olmayan biri tarafından '
                       'bitirildiği bir odaydı.',
                       'Sorması gereken soruları sordu: ne zaman başlamıştı, onarımı kim yapmıştı, evrak '
                       'üzerinde ikinci bir ad var mıydı. Kadın bir çekmeceye gitti, kliniğin kâğıtlarının '
                       'bulunduğu bir dosyayı getirdi; evrakın üzerinde tek bir ad yazılıydı.',
                       '“İki ad olması gerekiyordu,” dedi Elias.',
                       '“Bir tane var,” dedi kadın. “Şimdi önemi var mı?”',
                       'Önemliydi, ama bir mutfakta, ceketinin üzerinde hâlâ otobüs bileti duran bir kadına '
                       'nedenini anlatamazdı. Söylediği şuydu: “Cuma günü geri dönebilir miyim? Biriyle '
                       'birlikte gelirim. Onun neyi tuttuğuna bakmak isterim, neyi eksik bıraktığına değil.”',
                       '“Gelebilirsin,” dedi kadın. “Aldırmaz. Hiçbir şeye aldırmıyor. Bütün sorun bu zaten.”',
                       'Merdivenlerde inerken Mara, “Bu işi alacaksın,” dedi.',
                       '“Henüz bilmiyorum,” dedi Elias.',
                       '“Alacaksın. Onarımı zaten bitmiş, düzeltilecek tek şeyin kayıt olduğu bir iş '
                       'alacaksın.” Listeyi yukarı kaldırdı. “Bunlardan iki yüz on tane daha var. Tek tek '
                       'alırsan, bu dükkân çok yavaş bir özür dileme hâline gelir.”',
                       '“Bunun alternatifi ne?”',
                       '“Tek tek alırsın ve hepsini yazarsın,” dedi Mara. “Alternatif o değil. Bu durumun '
                       'yalan olmayan tek biçimi o.”',
                       'Işık hâlâ iyi olduğu için ilk sayfanın kalan adreslerini de gezdiler; yedinci kapıya '
                       'geldiğinde Elias, iyi durumda olanları saymayı bırakmıştı. Aklında kalan sayı değildi. '
                       'Üçüncü fideydi: çeyrek tur çevrilmiş, pencereden uzak taraftan sulanmış; günde iki '
                       'kez, kimse için olmadan, bir şeyi kusursuzca yapan bir adam.',
                       'O akşam dört sayfayı deftere koydu, bir kez katladı, üstüne şunu yazdı: *2 Mayıs '
                       'alındı. Müşteri listesi değil. Çevrenin bir koşulu. Gezilen on bir kapı, biri doğru.*'],
            'title': 'İki Yüz On Bir Kapı',
            'when': '2 Mayıs'},
     'yue': {'blocks': ['張名單禮拜三到，四頁，釘埋，第一頁頂有管理局嘅徽，冇附信。Mara 九個禮拜前書面申請過，當時答佢「冇呢個格式」；而家有呢個格式 —— 管理局道歉就係咁樣。',
                        '二百一十一個地址。九個喺 Elias 從來冇行過嘅街，即係話，係啲佢唔再理區邊界之後起嘅街。',
                        '「呢張唔係病人名單，」Mara 喺佢背後讀。「冇診斷一欄。呢張係一張表上某條問題答得唔同嘅地址名單。」',
                        '「邊條問題？」',
                        '「問過去十二個月有冇啲咩變咗，係你唔會同鄰居講嘅。」',
                        '佢哋攞第一頁行 —— '
                        '二百一十一係文件，十一係一個朝早。頭四個地址乜都冇：一個搬走咗嘅女人、一間落咗閘嘅鋪、一幢壞咗對講機嘅樓、一個開門四寸話「我阿媽幾好，多謝」就閂門嘅男人。',
                        '第五個係一個廚房。開門嘅女人四十歲左右，著住件外套，上面仲有巴士嘅痕；佢身後有個男人喺窗台淋三盆番茄，一盆一盆淋，個樣係習慣，但冇習慣嘅急。',
                        '「佢日日都咁做，」女人喺門口細聲講，細聲得唔夠。「一日兩次。佢唔知點解。佢話啲植物要。植物唔需要兩次。」',
                        'Elias 望住個男人放低水壺，捧起第二盆，轉四分之一圈，喺遠離窗嘅一邊淋。「幾耐？」',
                        '「兩年。係街角嗰間診所。佢做得好正。連收據都畀埋我哋。」',
                        '「佢痛唔痛？」',
                        '「佢冇喺任何嘢入面。」佢講得好似講一個一直袋喺袋入面嘅診斷。「佢唔傷心。都唔開心，但佢唔介意。佢 ——」佢搵字，搵到一個普通嘅 ——「整齊。」',
                        '屋入面有一個相架、一個將日子劃到今日嘅月曆、一份摺到填字遊戲嘅報紙，填字遊戲填晒。間房每一樣嘢都做完。Elias '
                        '就係停唔到望呢樣：唔係荒廢，唔係損壞，而係一間每一件事都做完、但做嗰個人唔在場嘅房。',
                        '佢問咗佢必須問嘅問題 —— 幾時開始、邊個做嘅修補、文件上有冇第二個名 —— 女人去開抽屜，攞出一個文件夾，入面係診所嘅紙；文件上得一個名。',
                        '「應該有兩個，」Elias 話。',
                        '「得一個，」女人話。「而家仲有分別咩？」',
                        '有分別；而佢喺一個廚房、對住一個著住外套（上面仲有巴士痕）、揸住文件夾嘅女人，講唔出點解有分別。佢講嘅係：「我禮拜五可唔可以再嚟？帶個人。我想睇佢揸住啲咩，唔係睇佢冇咗啲咩。」',
                        '「你可以嚟，」佢話。「佢唔會介意。佢乜都唔介意。問題就係呢樣。」',
                        '喺樓梯 Mara 話：「你會接呢單。」',
                        '「我未知。」',
                        '「你會。你會接一單修補已經做完、剩返要修嘅只係紀錄嘅工。」佢舉起張名單。「仲有二百一十個。你一個一個接，呢間鋪就變成一個好慢嘅道歉。」',
                        '「另一個選擇係咩？」',
                        '「你一個一個接，然後全部寫低，」Mara 話。「呢個唔係另一個選擇。呢個係呢件事唯一唔係講大話嘅版本。」',
                        '佢哋行埋第一頁剩低嘅，因為光仲好；行到第七度門，Elias 已經唔再數嗰啲冇事嘅。留喺佢心入面嘅唔係個數字。係第三盆番茄，轉四分之一圈，喺遠離窗嘅一邊淋 —— '
                        '一個人完美地做一件事，一日兩次，為冇人。',
                        '嗰晚佢將四頁紙放入簿，摺一摺，喺上面寫：*5 月 2 日收到。唔係客人名單。係呢區嘅狀況。行咗十一度門，一個真。*'],
             'title': '二百一十一度門',
             'when': '5 月 2 日'}},
 9: {'en': {'blocks': ['The warehouse was on the edge of the Ward where the streets stop pretending to be '
                       'streets and become loading bays, and the man behind the counter had the flat forearms '
                       'of somebody who had spent thirty years lifting things and putting them down.',
                       '“How much do you want?” he said.',
                       '“Four hours,” Elias said.',
                       'The man looked at him for a moment, then wrote something on a pad without asking '
                       'anything else, and went through the back. Elias had been buying fill for eleven years '
                       'and had never once been asked what it was for, and had never once been given the '
                       'option of buying less than a brick.',
                       'The brick came out on a pallet truck, wrapped, stamped on the side with a lot number '
                       'and a date and a line of very small print. A brick of fill is the size of a shoebox '
                       'and weighs what a shoebox would weigh if it were full of sand, and Elias carried it to '
                       'the counter himself because the man had already turned away.',
                       'The stuff inside the wrap had the consistency of cold butter and no smell of its own, '
                       'which is the part of the trade nobody puts on a sign: fill does not smell like '
                       'anything until it is worked, and then it smells like a hospital corridor that has been '
                       'cleaned twice.',
                       '“You want a smaller one, you cut it,” the man said, without looking up. “Everybody '
                       'cuts it. We sell bricks because the paperwork is per brick, not because the shop '
                       'downstairs needs four hours at once.”',
                       '“Sign,” the man said, and pushed the pad across. Elias signed, and then, because '
                       "Mara's rule had got into his hands, he did not push the pad back.",
                       '“I need the second name on this.”',
                       'The man looked at the pad, and then at Elias, and then at the pad again. “On a fill '
                       'ticket.”',
                       "“On a fill ticket. Two names, or I don't take the brick.”",
                       'There was a pause of the kind that only exists in warehouses, where the pause is also '
                       'a decision about whether to fetch somebody. The man went through the back. He was gone '
                       'four minutes. He came back with a woman in a cardigan who looked at the ticket, looked '
                       'at Elias, and said, “Since when?”',
                       "“Since November. It's not a new rule, it's an old one somebody started applying.”",
                       "“We're not a repair shop.”",
                       "“You're the first half of one,” Elias said. “I can't put two names on my side of the "
                       'ledger and one on yours. The book has to agree with itself or the audit is theatre.”',
                       'The woman signed. She signed with her full name, in a hand that had been taught to '
                       'sign things in 1989, and underneath she wrote the date, and underneath that, '
                       'unprompted, she wrote *counter, 12 July, second name on a fill ticket, first time*. '
                       "Then she said, “You'll want the receipts for the last two lots as well, then.”",
                       '“Why?”',
                       "“Because if we're doing names, we're doing names,” she said, and went to a shelf "
                       "behind her and pulled down a ledger of the warehouse's own, and Elias saw, before she "
                       'opened it, that it had a spine reinforced with tape in three places, which is what a '
                       'book looks like when it is the only book. She opened it at the front, where the paper '
                       'was yellow, and the first page was dated six years earlier and every line on it began '
                       'with a single letter — F, D, N, F, F, D.',
                       "He did not see the two lots that day. He saw the shape of the shelf, and the woman's "
                       'hand on the spine, and the way she put the book back without opening it, and he went '
                       'home with one brick and a receipt with two names on it and the specific feeling of a '
                       'man who has been told that there is more paperwork than he thought and that the '
                       'paperwork is not on his side.',
                       'The brick lasted eleven days. On the twelfth, a customer brought in a core that had '
                       'been repaired twice already and Elias used the last of it on a seam that had been made '
                       'by somebody who had also been in a hurry, and he wrote in the ledger that evening: '
                       '*Fill: one brick, 12 July, two names, counter. Nine days left of the month and a job '
                       'on Thursday that will need a second.*',
                       'What he did not write, because a ledger is not for this, was that the warehouse ledger '
                       'had been reinforced with tape in three places, and that a book like that is either '
                       'very old or very busy, and that either way somebody has been keeping it for longer '
                       'than the shop has been open.'],
            'title': 'One Brick',
            'when': '12 July'},
     'ko': {'blocks': ['창고는 관리청 가장자리에 있었다. 거리가 거리인 체하는 것을 그만두고 하역장이 되는 곳이었다. 카운터 뒤의 남자는 삼십 년을 물건을 들어 올리고 내려놓는 '
                       '데 보낸 사람의 납작한 팔뚝을 가지고 있었다.',
                       '“얼마나 가져갈 건가?” 그가 물었다.',
                       '“네 시간 분량이요.” Elias가 말했다.',
                       '남자는 잠시 그를 쳐다보더니 더 묻지 않고 패드에 무언가 적고 뒤로 들어갔다. Elias는 열한 년 동안 채움을 사 왔지만 무엇에 쓰는지 물어본 적도 한 '
                       '번 없었고, 벽돌 하나보다 적게 살 선택지를 받은 적도 한 번 없었다.',
                       '벽돌은 팔레트 트럭에 실려 나왔다. 포장돼 있었고 측면에 로트 번호와 날짜, 아주 작은 글씨 한 줄이 찍혀 있었다. 채움 벽돌은 신발 상자만 하고, 모래가 '
                       '가득 찬 신발 상자의 무게였다. 남자가 이미 등을 돌린 뒤라 Elias가 직접 카운터까지 날랐다.',
                       '포장 안 물건은 차가운 버터 같은 농도였고 자기 냄새는 없었다. 간판에 누구도 적지 않는 업계의 부분이었다. 채움은 다루기 전까지는 아무 냄새도 나지 '
                       '않고, 다루기 시작하면 두 번 닦은 병원 복도 같은 냄새가 난다.',
                       '“작은 걸 원하면 잘라 쓰지.” 남자가 고개도 들지 않고 말했다. “다들 잘라 쓰지. 서류가 벽돌 단위라 벽돌로 파는 거지, 아래 가게가 네 시간 분을 한 '
                       '번에 필요해서가 아니야.”',
                       '“서명.” 남자가 말하며 패드를 밀어 왔다. Elias가 서명하고, 그리고 나서 Mara의 규칙이 손에 배어, 패드를 다시 밀지 않았다.',
                       '“이것에 두 번째 이름이 필요해요.”',
                       '남자는 패드를 보고, 다음으로 Elias를 쳐다보고, 다시 패드를 보았다. “채움 전표에?”',
                       '“채움 전표에. 두 이름 아니면 벽돌을 안 가져가요.”',
                       '창고에만 있는 종류의 침묵이 있었다. 그 침묵은 누군가를 불러올지 여부를 결정하는 침묵이기도 했다. 남자는 뒤로 들어가 사 분 동안 돌아오지 않았다. '
                       '가디건을 입은 여자를 데리고 돌아와 여자는 전표를 보고 Elias를 보더니 “언제부터?” 라고 물었다.',
                       '“11월부터요. 새 규칙이 아니라, 누군가 적용하기 시작한 옛 규칙이에요.”',
                       '“우리는 수리 가게가 아니야.”',
                       '“그 앞반은 당신들이에요.” Elias가 말했다. “장부 내 쪽엔 두 이름을, 당신들 쪽엔 한 이름을 둘 수 없어요. 책이 스스로와 일치해야 하지, 아니면 '
                       '감사는 연극이에요.”',
                       '여자가 서명했다. 자기 성명을 다 적어 서명했고, 1989년에 사물에 서명하는 법을 배운 손이었다. 그리고 그 아래 날짜를 쓰고, 그 아래에는 누가 시키지 '
                       '않아도 *카운터, 7월 12일, 채움 전표의 두 번째 이름, 처음* 이라고 적었다. 그러고는 “그럼 지난 두 로트 영수증도 필요하시겠네요.” 라고 말했다.',
                       '“왜죠?”',
                       '“이름을 적기로 한 거라면 제대로 적어야 하니까.” 그녀가 등 뒤 선반에서 창고 자체의 장부를 꺼냈다. Elias는 그녀가 펴기 전에 보았다. 세 군데 '
                       '테이프로 등을 보강한 장부였다. 유일한 책일 때 책이 그런 모양이다. 누런 종이가 있는 앞쪽을 펼쳤다. 첫 페이지는 육 년 전의 날짜였고 그 위 모든 줄이 '
                       '한 글자로 시작했다 — F, D, N, F, F, D.',
                       '그날 그는 두 로트를 보지 못했다. 그는 선반의 모양, 책 등 위에 얹힌 여자의 손, 펴지도 않고 책을 제자리에 두는 그 방식을 보았다. 그는 벽돌 하나와 '
                       '이름이 둘 적힌 영수증을 들고 집에 갔다. 자기가 생각한 것보다 서류가 많고, 그 서류가 자기 편이 아니라는 말을 들은 남자의 특유한 느낌과 함께.',
                       '벽돌은 열하루 갔다. 열두째 날에는, 이미 두 번 수리된 코어를 고객이 가져왔고 Elias는 서두른 적이 있는 사람이 만든 봉합에 남은 채움을 모두 썼다. '
                       '그날 저녁 장부에 이렇게 적었다: *채움: 벽돌 하나, 7월 12일, 두 이름, 카운터. 이 달 구 일 남았고 목요일 작업엔 두 번째가 필요할 거야.*',
                       '장부가 이런 일을 담기 위한 것이 아니어서 적지 않은 것은, 창고 장부가 세 군데 테이프로 보강돼 있었다는 것, 그런 책은 아주 오래됐거나 아주 바쁜 '
                       '책이라는 것, 그리고 어느 쪽이든 누군가 가게가 열린 시간보다 더 오래 그 책을 지켜 왔다는 사실이었다.'],
            'title': '벽돌 하나',
            'when': '7월 12일'},
     'tr': {'blocks': ["Depo, Koruma Dairesi'nin en ucundaydı; sokakların sokak gibi davranmaktan çıkıp "
                       'yükleme rıhtımına dönüştüğü yerdeydi. Tezgâhın arkasındaki adam, otuz yıl boyunca ağır '
                       'şeyleri kaldırıp tekrar yerine koymuş birinin düz, kaslı ön kollarına sahipti.',
                       '“Ne kadar istiyorsun?” dedi adam.',
                       '“Dört saatlik,” dedi Elias.',
                       'Adam bir an ona baktı, sonra başka hiçbir şey sormadan kalem defterine bir şeyler '
                       'yazdı ve arkaya geçti. Elias on bir yıldır dolgu alıyordu; dolgunun ne için '
                       'kullanılacağı ona bir kez bile sorulmamıştı ve bir tuğladan az alma seçeneği de ona '
                       'bir kez bile sunulmamıştı.',
                       'Tuğla palet arabasıyla içeri çıktı; sarılıydı, yan tarafında parti numarası, bir tarih '
                       've bir satır çok küçük baskıyla damgalanmıştı. Bir dolgu tuğlası ayakkabı kutusu '
                       'büyüklüğündedir; kumla dolu bir ayakkabı kutusu ne ağırlıktaysa o ağırlıktadır. Adam '
                       'çoktan sırtını döndüğü için Elias tuğlayı tezgâha kendi başına taşıdı.',
                       'Sargının içindeki madde soğuk tereyağı kıvamındaydı ve kendine özgü kokusu yoktu; '
                       'mesleğin kimsenin tabelaya yazmadığı kısmı buydu: dolgu işlenene kadar hiçbir şeye '
                       'benzemez, işlenince iki kez temizlenmiş bir hastane koridoru gibi kokar.',
                       '“Daha küçük istiyorsan, kendin kesersin,” dedi adam, başını kaldırmadan. “Herkes '
                       'keser. Tuğla satıyoruz çünkü evrak tuğla başına düzenleniyor; aşağıdaki dükkânın '
                       'birden dört saate ihtiyacı olduğu için değil.”',
                       '“İmza,” dedi adam, defteri tezgâhın öbür tarafına itti. Elias imzaladı. Sonra, '
                       "Mara'nın kuralı ellerine işlediği için, defteri geri itmedi.",
                       '“Bunun üzerinde ikinci adı görmem gerekiyor.”',
                       "Adam deftere baktı, sonra Elias'a, sonra yeniden deftere. “Dolgu fişinin üzerinde, "
                       'öyle mi?”',
                       '“Dolgu fişinin üzerinde. İki ad yazılı olacak, yoksa tuğlayı almam.”',
                       'Sadece depolarda görülen türden bir duraksama oldu; burada duraksama aynı zamanda '
                       'birini çağırıp çağırmama kararıdır. Adam arkaya geçti. Dört dakika boyunca ortada '
                       "yoktu. Hırkalı bir kadınla geri döndü; kadın önce fişe baktı, sonra Elias'a baktı ve "
                       '“Ne zamandan beri?” dedi.',
                       '“Kasımdan beri. Yeni bir kural değil, birinin uygulamaya başladığı eski bir kural.”',
                       '“Onarım dükkânı değiliz biz.”',
                       '“Bir onarım dükkânının ilk yarısısınız,” dedi Elias. “Defterin kendi tarafıma iki ad '
                       'yazıp sizin tarafınıza bir ad yazamam. Defter kendiyle aynı fikirde olmalı; yoksa '
                       'denetim bir gösteriden ibaret kalır.”',
                       "Kadın imzaladı. Tam adıyla, 1989'da bir şeyler imzalaması öğretilmiş bir el yazısıyla "
                       'imzaladı. Altına tarihi yazdı; onun altına da, hiç kimse söylemeden, *tezgâh, 12 '
                       'Temmuz, dolgu fişinde ikinci ad, ilk kez* yazdı. Sonra konuşmaya başladı: “Son iki '
                       'partinin makbuzlarını da isteyeceksin o hâlde.”',
                       '“Neden?”',
                       '“Çünkü isim yazacaksak, isim yazarız,” dedi. Arkasındaki rafa doğru gitti ve deponun '
                       'kendi defterini aşağı indirdi. Elias daha kadın defteri açmadan gördü: defterin sırtı '
                       'üç yerden bantla güçlendirilmişti; bir kitap tek kitapsa işte öyle görünür. Defteri ön '
                       'tarafa, kâğıdın sararmış olduğu yere açtı; ilk sayfa altı yıl öncesine tarihleniyordu '
                       've üzerindeki her satır tek bir harfle başlıyordu — F, D, N, F, F, D.',
                       'İki partiyi o gün görmedi. Rafın biçimini gördü, kadının elinin defterin sırtındaki '
                       'duruşunu, kitabı açmadan yerine koyuşunu gördü. Bir tuğlayla ve üzerinde iki ad yazılı '
                       'olan bir makbuzla eve gitti; evrakın sandığından fazla olduğunu, ve evrakın kendi '
                       'tarafında olmadığını öğrenmiş bir adamın o özel duygusuyla eve vardı.',
                       'Tuğla on bir gün dayandı. On ikinci gün, daha önce iki kez onarılmış bir çekirdek '
                       'getirdi bir müşteri; Elias dolgunun son parçasını, acele etmiş biri tarafından '
                       'yapılmış bir dikişte kullandı ve o akşam deftere şunu yazdı: *Dolgu: bir tuğla, 12 '
                       "Temmuz, iki ad, tezgâh. Ayın dokuz günü kaldı ve Perşembe'de ikinci bir isim isteyecek "
                       'bir iş var.*',
                       'Defterin bunun için olmadığı için yazmadığı şey şuydu: deponun defteri üç yerden '
                       'bantla güçlendirilmişti; böyle bir kitap ya çok eskiydi, ya çok yoğundu. Her iki '
                       'durumda da, biri o defteri, dükkânın açık kaldığı süreden daha uzun bir süredir '
                       'tutuyordu.'],
            'title': 'Bir Tuğla',
            'when': '12 Temmuz'},
     'yue': {'blocks': ['貨倉喺管理局邊緣，街開始唔再扮街、變成上貨位嘅地方；櫃檯後面嗰個男人，前臂好平，係做咗三十年搬上搬落嘅人先有嘅前臂。',
                        '「你要幾多？」佢話。',
                        '「四個鐘，」Elias 話。',
                        '男人望佢一陣，喺本簿上寫咗啲嘢，冇再問，行入後面。Elias 買咗十一年填料，從來冇人問過佢用嚟做咩，亦從來冇得買少過一磚。',
                        '磚用唧車推出來，包住，側邊印住批號、日期，同一行好細嘅字。一磚填料大細似鞋盒，重就似一個裝滿沙嘅鞋盒；Elias 自己捧去櫃檯，因為男人已經轉咗身。',
                        '包裝入面嘅嘢好似凍牛油，本身冇味 —— 呢樣係呢行唔會寫上招牌嘅部分：填料未動之前唔似有味，一動就似一條抹過兩次嘅醫院走廊。',
                        '「想要細啲，自己切，」男人冇抬頭講。「個個都切。我哋按磚賣，係因為張紙係按磚計，唔係因為樓下間鋪要一次用四個鐘。」',
                        '「簽名，」男人話，將簿推過來。Elias 簽咗，然後，因為 Mara 條規條已經入咗佢對手，佢冇將簿推返去。',
                        '「我要第二個名喺上面。」',
                        '男人望住本簿，再望 Elias，再望本簿。「喺一張填料單上面。」',
                        '「喺一張填料單上面。兩個名，否則我唔攞磚。」',
                        '停頓係得貨倉先有嗰種 —— 呢種停頓同時係一個決定：要唔要去後面搵人。男人行入後面。去咗四分鐘。返嚟帶住一個著開胸毛衣嘅女人；佢望單、望 Elias，話：「幾時開始？」',
                        '「十一月開始。唔係新規矩，係一條舊規矩有人開始執行。」',
                        '「我哋唔係修補鋪。」',
                        '「你哋係修補鋪嘅前半，」Elias 話。「我唔可以自己嗰邊簿寫兩個名，你哋呢邊寫一個。本書要同自己對得上，否則審計就係做戲。」',
                        '女人簽咗。佢簽全名，手勢係 1989 年學識簽嘢嗰種；下面寫日期，再下面，冇人叫佢，佢寫：*櫃檯，7 月 12 '
                        '日，填料單上第二個名，第一次*。然後佢話：「咁你都會想要最近兩批嘅收據。」',
                        '「點解？」',
                        '「因為如果我哋開始講名，就講到底，」佢話，行去後面一個架，拎低一本貨倉自己嘅簿；Elias 喺佢未打開之前就見到，簿脊用膠紙補咗三個位 —— '
                        '一本書得一本嘅時候就係咁樣。佢打開前面，紙已經黃；第一頁日期係六年前，每一行開頭都係一個字母：F、D、N、F、F、D。',
                        '嗰日佢冇見到嗰兩批。佢見到個架嘅形狀、女人隻手喺簿脊上面、佢冇打開就放返本書嘅方式；佢帶住一磚填料、一張有兩個名嘅收據返屋企，仲有嗰種特別嘅感覺：有人同佢講，紙比佢想像多，而啲紙唔喺佢呢邊。',
                        '磚用咗十一日。第十二日，一個客人帶嚟一個已經修過兩次嘅記憶核，Elias 用埋最後嗰啲，補喺一條同樣由一個趕時間嘅人整嘅接縫；嗰晚佢喺簿寫：*填料：一磚，7 月 12 '
                        '日，兩個名，櫃檯。月尾仲有九日，禮拜四有一單要第二個。*',
                        '佢冇寫嘅（因為簿唔係用嚟寫呢啲）：貨倉本簿嘅簿脊補咗三個位；一本咁嘅書，一係好舊，一係好忙；兩樣都好，有人記住佢嘅時間，比呢間鋪開嘅時間更長。'],
             'title': '一磚',
             'when': '7 月 12 日'}},
 10: {'en': {'blocks': ['Halloway brought the second loom himself, in a van he had borrowed, and refused help '
                        'carrying it because he had carried it into the clinic fourteen years earlier and '
                        'considered the removal to be the same job in reverse.',
                        'It was a commercial model, the kind that had been in every clinic on the Ward until '
                        'the clinics started buying the small ones, and it filled the back of the shop the way '
                        'a piano fills a room. Elias had spent nine years working on a machine assembled from '
                        'parts and had forgotten what it was like to stand in front of one that had been '
                        'designed by people who expected it to be used by strangers.',
                        "“The clinic's gone to the new units,” Halloway said, straightening up. “This one's "
                        "been in the back since March. It's not a gift. If I sell it I have to explain where "
                        "it came from, and the explanation is a paragraph I don't want in a file.”",
                        "“So you're giving it to the shop that keeps a book.”",
                        "“I'm giving it to the shop that keeps a book.” Halloway looked around the bench, at "
                        'the old loom on its marks and the ledger open at today, and said, “You know what the '
                        'difference is between my clinic and this shop? Mine has four machines and one of them '
                        'works. Yours has one machine that works and a book that says why.”',
                        'They set the second loom on the far side of the bench, where the light was worse, and '
                        'it took the whole afternoon. The old loom had to be moved eighteen inches, and Elias '
                        'marked the new position with tape before they moved it, which Halloway noticed and '
                        'did not comment on.',
                        'The two machines did not sound the same. The old one ran with a note that came up '
                        'through the floor and stopped at the knee; the commercial one ran almost silently and '
                        'put its noise into the air instead, a flat hum with nothing underneath it. Wren stood '
                        "between them with her hands behind her back and said, “The new one doesn't tell you "
                        'anything.”',
                        "“It tells you it's running,” Halloway said.",
                        "“The old one tells you *what* it's running,” she said, and then, because she was "
                        'nineteen and had been in the shop for six months, added, “Sorry.”',
                        "“Don't apologise for a diagnosis,” Mara said from the doorway. She had come to read "
                        "the second account on the afternoon's job and had stopped to watch the installation "
                        'the way she watched everything, from slightly further back than was polite.',
                        "The afternoon's job was the reason the second loom mattered. A core that had been "
                        'repaired twice, once by a good hand and once by a hand in a hurry, and the second '
                        'repair had bridged across the first seam instead of beside it. It could not be done '
                        'on one machine: the old loom could open the seam and hold it, and only the commercial '
                        'unit had the resolution to work inside a bridge that had already set.',
                        'So they ran both. Elias on the old one, holding, and Wren on the new one, reading out '
                        'what she saw, and Mara at the ledger with the pen not yet on the page, because the '
                        'rule says the joint is named before the loom and the joint had been named at two '
                        "o'clock, in front of the customer, in words the customer repeated back.",
                        'It took four hours. At the end there were two seams where there had been one, and the '
                        'room in the core had a floor again, and the customer, when they brought him in, sat '
                        "down in the chair and did not say anything for a while and then said, “It's the same "
                        "room. It's just that I'm in it now.”",
                        'Halloway stayed for the last hour and watched from the doorway with his coat on, and '
                        "when it was done he said, “You've got a bench that can do the work my clinic can't.”",
                        "“I've got a bench that can do the work and a book that says who did which half.”",
                        "“That's the same sentence,” Halloway said. “You just don't like the way it sounds "
                        'when I say it.”',
                        "He left without taking the van's parking money and without saying what he wanted, "
                        'which Elias noted in the ledger that evening under the job, in the space where he '
                        'usually wrote the fill used: *Second loom in, 17 Sep, ex-clinic, no paper. Job done '
                        'on both machines. Two seams. One room. Halloway stayed for the end and left without '
                        'an invoice, which is how he asks.*'],
             'title': 'Two Machines, One Bench',
             'when': '17 September'},
      'ko': {'blocks': ['Halloway가 직조기 둘째를 직접 빌려온 밴에 실어 가져왔다. 옮기는 일은 도움을 사양했다. 열네 해 전에 그가 직접 클리닉 안으로 들여놓았고, '
                        '빼내는 일은 같은 일을 거꾸로 하는 것이라고 생각했기 때문이다.',
                        '상업용 직조기 모델이었다. 관리청의 클리닉들이 작은 모델을 사기 시작하기 전까지는 모든 클리닉에 한 대씩 놓여 있던 종류였다. 그 기계는 가게 뒤편을 '
                        '피아노가 방 안을 채우는 방식으로 가득 채웠다. Elias는 부품을 하나씩 모아 직접 조립한 기계를 아홉 해 동안 다뤄 왔고, 낯선 사람이 쓰리라고 '
                        '예상한 설계자들이 설계한 기계 앞에 서는 것이 어떤 느낌인지 오래전에 잊고 있었다.',
                        '“클리닉은 새 유닛으로 바뀌었지,” Halloway가 허리를 펴며 말했다. “이 기계는 3월부터 클리닉 뒤편에 놓여 있었다. 이건 선물이 아니다. 내가 '
                        '팔면 출처를 설명해야 하고, 그 설명은 서류철에 넣고 싶지 않은 한 단락이 된다.”',
                        '“그러니 장부를 지키고 있는 이 가게에 주겠다는 거군.”',
                        '“장부를 지키는 가게에 주는 거다.” Halloway는 작업대 주위를 둘러보았다. 자리 표시가 놓인 옛 직조기, 오늘 장이 열린 장부를 보고 말했다. '
                        '“내 클리닉과 이 가게의 차이를 아나? 내 쪽은 기계 네 대에 돌아가는 건 하나다. 너희는 돌아가는 기계 하나와 그 이유를 적은 책이 있다.”',
                        '둘째 직조기는 작업대 건너편, 빛이 더 약한 쪽에 놓았고, 그 일에 오후 전체가 걸렸다. 옛 직조기는 열여덟 인치 옮겨야 했고, Elias는 옮기기 전에 '
                        '새 자리를 테이프로 표시해 두었다. Halloway는 그 표시를 눈치챘지만 아무 말도 하지 않았다.',
                        '두 기계 소리는 같지 않았다. 옛것은 바닥을 타고 올라와 무릎에 닿는 음조로 돌아갔다. 상업용은 거의 소리를 내지 않고 소음을 공기 중에 실었을 뿐, '
                        '밑동 없는 납작한 윙윙거림이었다. Wren는 등 뒤로 손을 모으고 두 기계 사이에 서서 말했다. “새것은 아무것도 알려 주지 않아요.”',
                        '“돌아가고 있다는 건 알려 주지,” Halloway가 말했다.',
                        '“옛것은 *무엇을* 돌리는지 알려 주죠.” 그녀가 말했다. 그리고 열아홉 살이고 가게에 온 지 여섯 달이라, 사과하는 말을 덧붙였다. “죄송해요.”',
                        '“진단 때문에 사과할 필요는 없다.” Mara가 출입구 쪽에서 말했다. 그녀는 그날 오후 작업의 두 번째 계정을 읽으러 온 길이었고, 늘 모든 것을 보는 '
                        '방식대로 예의보다 살짝 뒤쪽에서 설치를 지켜보려 멈춰 섰다.',
                        '오후 작업이 둘째 직조기가 필요한 이유였다. 코어는 두 번 수리되어 있었고, 한 번은 솜씨 좋은 손이, 한 번은 급한 손이 했다. 두 번째 수리는 첫 '
                        '봉합선 옆이 아니라 가로질러 다리를 놓았다. 한 기계로는 불가능했다. 옛 직조기는 봉합선을 열어 잡을 수 있었지만, 이미 굳은 다리 안쪽을 작업할 '
                        '해상도는 상업용 유닛에만 있었다.',
                        '그래서 두 기계를 함께 돌렸다. Elias는 옛것에 서서 틀을 잡았고, Wren는 새것에 앉아 자기가 보이는 것을 낱낱이 읊었으며, Mara는 장부 앞에 '
                        '펜을 아직 종이에 대지 않고 있었다. 규칙은 직조기 앞에서 이음을 밝히라고 하며, 이음은 두 시에 고객 앞에서, 고객이 다시 따라 말한 단어로 이미 '
                        '밝혀져 있었다.',
                        '네 시간이 걸렸다. 끝에는 봉합선이 하나에서 둘로 늘어 있었고, 코어 속 방에는 바닥이 다시 생겼다. 고객을 안으로 들였을 때 그는 의자에 앉아 한동안 '
                        '아무 말도 하지 않다가 말했다. “같은 방이네. 다만 지금은 내가 그 안에 있을 뿐이야.”',
                        'Halloway는 마지막 한 시간을 남아 코트를 입은 채 출입구에서 지켜보았다. 모든 일이 끝나자 그는 말했다. “내 클리닉이 못 하는 일을 해낼 수 '
                        '있는 작업대를 네가 가졌군.”',
                        '“일을 해낼 수 있는 작업대 하나와, 어느 절반을 누가 했는지 적은 책 하나를 가지고 있지.”',
                        '“그건 같은 문장이야.” Halloway가 말했다. “내가 말할 때 그 소리가 마음에 들지 않을 뿐이지.”',
                        '그는 밴 주차 돈도 받지 않고 자기가 원하는 것도 말하지 않고 돌아갔다. Elias는 그날 저녁 장부의 그 작업 아래, 평소 채움 사용량을 적는 칸에 '
                        '그것을 적었다. *둘째 직조기 들임, 9월 17일, 클리닉 출신, 서류 없음. 두 기계로 작업 완료. 봉합선 둘. 방 하나. Halloway는 끝까지 '
                        '남았고 청구서 없이 돌아감. 그가 부탁하는 방식이다.*'],
             'title': '직조기 둘, 작업대 하나',
             'when': '9월 17일'},
      'tr': {'blocks': ['Halloway ikinci tezgâhı kendisi getirdi, ödünç aldığı bir minibüsün içinde; taşırken '
                        'yardım almayı reddetti, çünkü on dört yıl önce onu kliniğe kendisi taşımıştı ve şimdi '
                        'yapılan kaldırma işini aynı görevin ters yöndeki hali sayıyordu.',
                        'Ticari bir modeldi; klinikler küçük makineleri almaya başlamadan önce Koruma '
                        "Dairesi'ndeki her klinikte bulunan türden bir makineydi. Dükkânın arkasını bir "
                        'piyanonun odayı doldurduğu gibi dolduruyordu. Elias dokuz yılını, parçalardan bir '
                        'araya getirilmiş bir makine üzerinde çalışarak geçirmişti; yabancı kullanıcıların '
                        'elinde kullanılmak üzere başkaları tarafından tasarlanmış bir makinenin önünde '
                        'durmanın nasıl olduğunu unutmuştu.',
                        "“Klinik yeni ünitelere geçti,” dedi Halloway, doğrularak. “Bu Mart'tan beri orada, "
                        'arka bölümde duruyor. Hediye değil. Eğer satmaya kalksam nereden geldiğini açıklamak '
                        'zorunda kalırdım ve o açıklama, bir dosyanın içinde görmek istemeyeceğim bir paragraf '
                        'olurdu.”',
                        '“Demek defter tutan dükkâna veriyorsun.”',
                        '“Defter tutan dükkâna veriyorum.” Halloway tezgâhın çevresine baktı; işaretleri '
                        'üzerindeki eski tezgâha, bugünün sayfasına açık deftere baktı. “Benim kliniğimle bu '
                        'dükkân arasındaki farkın ne olduğunu biliyor musun?” dedi. “Bende dört makine var, '
                        'yalnızca biri çalışıyor. Sende çalışan tek bir makine ve neden çalıştığını söyleyen '
                        'bir kitap var.”',
                        'İkinci tezgâhı tezgâhın karşı tarafına, ışığın daha kötü olduğu yere kurdular; bu iş '
                        'bütün öğleden sonrayı aldı. Eski tezgâhı on sekiz inç kaydırmaları gerekiyordu; Elias '
                        'onları taşımadan önce yeni duracağı yeri bantla işaretledi, Halloway bunu fark etti, '
                        'ama üzerinde durup konuşmadı.',
                        'İki makinenin sesi aynı değildi. Eskisi zeminden yukarı yükselip diz hizasında duran '
                        'bir nota ile çalışıyordu; ticari olan neredeyse hiç ses çıkarmıyordu, gürültüsünü '
                        'havaya veriyordu, altında hiçbir derinliği olmayan düz bir uğultuydu. Wren ellerini '
                        'sırtının arkasında tutarak ikisinin arasında durdu ve “Yeni olan sana hiçbir şey '
                        'anlatmıyor,” dedi.',
                        '“Çalıştığını söylüyor,” dedi Halloway.',
                        '“Eskisi sana *neyi* çalıştırdığını söylüyor,” dedi; sonra, on dokuz yaşında ve '
                        'dükkânda altı ay olduğu için, “Pardon,” diye ekledi.',
                        '“Bir teşhis sözcüğü için özür dileme,” dedi Mara, kapı eşiğinden. Öğleden sonraki '
                        'işin ikinci kaydını okumaya gelmişti; kurulumu, her şeyi izlediği gibi, nezaketin '
                        'gerektirdiğinden biraz daha geriden izlemek için orada durmuştu.',
                        'Öğleden sonraki iş, ikinci tezgâhın neden önemli olduğuydu. Çekirdek iki kez '
                        'onarılmıştı: bir kez iyi bir el, bir kez acele eden bir el; ikinci onarım ilk dikişin '
                        'yanından değil, üstünden köprü geçirmişti. Tek bir makinede yapılamazdı: eski tezgâh '
                        'dikişi açıp yerinde tutabilirdi, ama kurumuş bir köprünün içinde çalışabilecek '
                        'çözünürlük yalnızca ticari ünitede vardı.',
                        'Bu yüzden ikisini birden çalıştırdılar. Elias eskisinde, çerçeveyi tutarak yer '
                        'alıyordu; Wren yenisinde gördüklerini yüksek sesle okuyordu; Mara defterin '
                        'başındaydı, kalemi henüz sayfaya değmemişti. Çünkü kural, ikilinin tezgâh '
                        'çalıştırılmadan önce adlandırılmasını emreder ve ikili saat ikide, müşterinin gözü '
                        'önünde, müşterinin geri tekrar ettiği sözlerle adlandırılmıştı.',
                        'Dört saat sürdü. Sonunda, önceden bir olan yerde iki dikiş vardı ve çekirdeğin '
                        'içindeki odanın yeniden bir zemini oldu. Müşteriyi içeri getirdiklerinde sandalyeye '
                        'oturdu, bir süre hiçbir şey söylemedi, sonra şöyle konuştu: “Aynı oda. Yalnızca şimdi '
                        'içinde ben varım.”',
                        'Halloway son bir saat dükkânda kaldı, paltosu üzerinde kapı eşiğinden izledi. İş '
                        'bittiğinde, “Senin kliniğinin yapamadığı işi yapabilecek bir tezgâhın var,” dedi.',
                        '“İşi yapabilecek bir tezgâhım ve hangi yarımı kimin yaptığını yazan bir kitabım var.”',
                        '“İki cümle de aynı şeyi söylüyor,” dedi Halloway. “Sen yalnızca benim söylerkenki '
                        'sesini beğenmiyorsun.”',
                        'Minibüsün park parasını almadan ve istediğini açıkça söylemeden ayrıldı. Elias akşam '
                        'bunu defterde, ilgili işin altına, genellikle dolgu miktarını yazdığı boşluğa '
                        'kaydetti: *İkinci tezgâh girdi, 17 Eylül, klinikten gelme, evrak yok. İş iki makinede '
                        'birden yapıldı. İki dikiş. Bir oda. Halloway sonuna kadar kaldı ve faturasız çıktı; '
                        'bir şey istediğini her zaman böyle belli eder.*'],
             'title': 'İki Makine, Bir Tezgâh',
             'when': '17 Eylül'},
      'yue': {'blocks': ['Halloway 自己搬第二部織機嚟，用一架借返嚟嘅客貨車；佢唔肯畀人幫手搬，因為十四年前佢親手搬入診所，佢當今次係同一件事倒轉做。',
                         '係商用型號，管理局每間診所都有過嗰種，直到診所開始買細嘅；佢塞滿鋪頭後面，好似一部鋼琴塞滿一間房。Elias '
                         '九年都係用一部由零件砌成嘅機器，已經唔記得企喺一部由「預咗畀陌生人用」嘅人設計嘅機器前面，係咩感覺。',
                         '「診所換咗新機，」Halloway 直起身。「呢部三月開始擺喺後面。唔係送。如果我賣，我要解釋佢邊度嚟，而個解釋係一段我唔想入檔案嘅文字。」',
                         '「所以你就送畀一間會寫簿嘅鋪。」',
                         '「我送畀一間會寫簿嘅鋪。」Halloway 望一圈工作檯 —— 舊織機喺佢嘅位置記號上，簿打開喺今日 '
                         '——「你知我診所同呢間鋪嘅分別喺邊？我四部機，一部行得；你一部機行得，加一本簿講點解。」',
                         '佢哋將第二部織機擺喺工作檯對面，光差啲嗰邊，搞咗成個下晝。舊織機要移十八寸；Elias 喺移之前用膠紙黐低新位置，Halloway 見到，冇講嘢。',
                         '兩部機唔同聲。舊嗰部有個音由地板走上嚟，喺膝頭停；商用嗰部幾乎冇聲，將聲放晒入空氣，一個平嘅嗡嗡聲，下面乜都冇。Wren '
                         '企喺兩部中間，雙手擺背後，話：「新嗰部乜都唔話你知。」',
                         '「佢話你知佢行緊，」Halloway 話。',
                         '「舊嗰部話你知佢行緊*咩*，」佢話，然後因為佢十九歲、喺鋪六個月，補咗句「對唔住。」',
                         '「唔好為一個診斷道歉，」Mara 喺門口話。佢嚟讀下晝嗰單嘅第二個戶口，停低睇裝機 —— 好似佢睇所有嘢咁，企得比禮貌應有嘅遠少少。',
                         '下晝嗰單就係第二部織機嘅理由。一個記憶核修過兩次：一次好手，一次趕時間；第二次喺第一條接縫上面搭橋，唔係喺隔籬。呢單一部機做唔到：舊織機可以開條縫同揸住，但只有商用嗰部嘅解析度，可以喺一條已經定咗型嘅橋入面做嘢。',
                         '所以兩部一齊行。Elias 喺舊機揸住，Wren 喺新機讀出佢見到嘅，Mara 喺簿前面，支筆未落紙 —— '
                         '因為規條話：動織機之前先寫低合夥人；而合夥人兩點鐘已經喺客人面前寫低，客人仲複述咗一次。',
                         '做咗四個鐘。做完之後，本來一條接縫變兩條；記憶核入面間房又有返地板；客人帶入嚟，坐低喺椅，靜咗一陣，然後話：「同一間房。只係我而家喺入面。」',
                         'Halloway 留埋最後一個鐘，著住外套喺門口睇；做完佢話：「你有一張做得到我診所做唔到嘅工作檯。」',
                         '「我有一張做得到嘅工作檯，加一本簿講邊個做邊一半。」',
                         '「同一句，」Halloway 話。「你只係唔鍾意我講嘅時候個聲。」',
                         '佢走咗，冇收客貨車泊車錢，亦冇講佢想要咩。嗰晚 Elias 喺簿上、喺佢平時寫用咗幾多填料嘅位置，記低：*第二部織機入鋪，9 月 17 '
                         '日，出自診所，冇紙。兩部機做一單。兩條接縫。一間房。Halloway 留到最後，冇開單就走 —— 佢想要嘢就係咁樣問。*'],
              'title': '兩部機，一張檯',
              'when': '9 月 17 日'}},
 11: {'en': {'blocks': ["Ader's office had a window that looked onto the loading bay of the building next "
                        'door, and a desk with nothing on it but the file, because he had cleared the desk in '
                        'September and had not needed anything on it since.',
                        "The file was the shop's, and it was also his. Two years of paperwork, bought with "
                        'three requests and one formal complaint, and in the middle of it a page he had put '
                        'there himself and had not read since the day he put it there.',
                        'Page eighty-four. Nine minutes.',
                        'He did not read it. He had read it four times in two years and each time had come '
                        'away with the same two facts: that the splice was well made, and that he could not '
                        'remember the afternoon it recorded. The second fact was the one that had started the '
                        'file.',
                        'The finding number was still blank on the form. It had been blank since March. A '
                        'finding number is assigned when an inspector decides that what he has found is a '
                        'finding, and the form had been sitting on the desk with its blank space for eight '
                        'months, which is how long it takes to decide whether an irregularity is a mistake, a '
                        'practice, or a person.',
                        "He put on the headphones at four o'clock, which was the hour the building went quiet, "
                        'and listened to the nine minutes.',
                        "It was a kitchen. He knew that from the recording and not from his life. A woman's "
                        "voice, and a man's voice, and his own voice doing the thing he did in those years, "
                        'which was to explain the procedure in the calm flat register of a man who has '
                        'explained it four hundred times and has decided that the four hundred and first '
                        'person deserves the same care as the first.',
                        'At minute six the woman said, “Will he know it was me?” And his own voice said, '
                        "“He'll know the shape of it. He won't know the feeling. That's the trade.”",
                        'Ader stopped the recording at minute seven, because he had heard what he needed and '
                        'because there is no professional reason to listen to the rest of your own voice '
                        'selling something.',
                        'The finding was not that the shop had broken a rule. The finding was that the Ward '
                        'had written a rule in 1998, printed it in a handbook nobody read, and then built a '
                        'system in which the only way to apply it was for a second person to be present, and '
                        'in which nobody had ever defined *present*.',
                        'The handbook was in the corridor cupboard, third shelf, in a binder with the year on '
                        'the spine: 1998. Seventeen pages on the duties of a second person, written by '
                        'somebody who had clearly never stood at a bench, and not one of those pages contained '
                        'the word he needed. He read all seventeen again standing up, because sitting down '
                        'with it would have made the reading official.',
                        "He wrote it out longhand, because the form's boxes were too small for the sentence, "
                        'and he attached page eighty-four as an exhibit, and then he sat with the last box on '
                        'the form for eleven minutes before writing 12/2026 in it.',
                        'The number meant it was the twelfth finding of the year and the twenty-sixth of his '
                        'career, and he wrote it in the box the way a man writes a number he has been '
                        'avoiding, which is slowly, and then he closed the file and did not put it away.',
                        "“You'll be asked why you kept it,” his supervisor said the next morning, looking at "
                        'the file on the desk. “An inspector who files a finding on his own splice is filing a '
                        'finding on himself.”',
                        "“I know what I'm filing.”",
                        '“Do you want it reassigned?”',
                        "“No,” Ader said. “If it's reassigned, the next inspector reads page eighty-four and "
                        "thinks the problem is the shop. The problem is the word *present*. I'm the only "
                        'inspector who has been in the room and can say what the room was like.”',
                        'The finding went out on the twenty-eighth. He did not send a copy to Cinder Lane, and '
                        'he did not send a letter either, because a letter would have been an explanation and '
                        'the finding was the explanation. He put the file in the drawer, and the drawer had '
                        "the shop's name on it in his own handwriting, and he left it there for the winter."],
             'title': 'The File on His Own Desk',
             'when': '26 November'},
      'ko': {'blocks': ['Ader의 사무실에는 옆 건물 적재대를 내려다보는 창이 하나 있었고, 책상 위에는 서류철 외에 아무것도 놓여 있지 않았다. 9월에 책상을 비운 뒤로 그 '
                        '위에 둘 것이 필요 없었기 때문이다.',
                        '서류철은 가게의 것이면서 그의 것이기도 했다. 세 번의 요청과 한 건의 정식 불만으로 얻어낸 이 년 치 서류 한가운데, 그가 직접 넣고 넣은 날 이후 '
                        '읽지 않은 페이지가 있었다.',
                        '팔십사 페이지. 구 분.',
                        '그는 그것을 읽지 않았다. 이 년 동안 네 번 읽었고 매번 같은 두 가지 사실만을 안고 돌아왔다. 잇기가 잘 만들어졌다는 것, 그리고 그것이 기록한 그 '
                        '오후를 자기가 기억하지 못한다는 것. 서류철을 처음 시작하게 한 건 둘째 사실이었다.',
                        '결론 번호는 양식에 여전히 비어 있었고 3월부터 그 칸이 비어 있었다. 결론 번호는 심사관이 자기가 발견한 것을 결론이라고 판단한 뒤에야 부여된다. '
                        '양식은 빈 칸을 그대로 둔 채 여덟 달째 책상 위에 놓여 있었다. 그 팔 개월은 비정상이 실수인지, 관행인지, 사람인지 판단하는 데 걸리는 시간이었다.',
                        '네 시에 그는 헤드폰을 썼다. 건물 안이 조용해지는 시간이었다. 그리고 구 분짜리 녹음을 들었다.',
                        '거기는 부엌이었다. 자기 삶이 아니라 녹음을 통해서 안 장소였다. 여자의 목소리, 남자의 목소리, 그리고 그 시절 자기가 하던 대로 절차를 설명하는 자기 '
                        '목소리가 있었다. 사백 번 설명한 사람의 차분하고 납작한 어조였고, 사백한 번째 사람에게도 첫 번째 사람과 같은 정성을 주기로 결정한 톤이었다.',
                        '육 분째에 여자가 말했다. “내가 한 거라는 걸 알까?” 그리고 자기 목소리가 대답했다. “형태는 알아챌 거야. 느낌은 모를 거다. 그게 업계다.”',
                        'Ader는 칠 분째에 녹음을 멈췄다. 필요한 것은 이미 들었다. 자기 목소리가 무언가를 파는 나머지를 들을 전문적 이유는 없었다.',
                        '결론은 가게가 규칙을 어겼다는 것이 아니었다. 결론은 관리청 쪽에 있었다. 관리청은 1998년에 규칙을 쓰고, 아무도 읽지 않는 안내서에 인쇄한 뒤, '
                        '적용하는 유일한 방법이 두 번째 사람의 배석인 체계를 만들었고, *배석*이 무엇인지 아무도 정의한 적이 없었다.',
                        '안내서는 복도 찬장 세 번째 선반, 등면에 연도가 찍힌 바인더에 들어 있었다. 1998년. 작업대에 서 본 적 없는 사람이 분명 쓴, 두 번째 사람 '
                        '의무에 관한 열일곱 페이지였고, 그 어디에도 그가 필요한 단어는 들어 있지 않았다. 그는 열일곱 페이지를 다시 모두 서서 읽었다. 앉아서 읽으면 그 '
                        '읽기가 공식적인 것이 되기 때문이다.',
                        '양식 칸이 그 문장을 적기에 너무 작아 손으로 풀어 쓰고 팔십사 페이지를 증거물로 첨부했다. 그리고 양식 마지막 칸을 열한 분 붙들고 앉아 있다가 거기에 '
                        '12/2026을 적었다.',
                        '그 번호는 올해 열두 번째 결론이자, 그의 경력으로는 스물여섯 번째 결론이었다. 피해 온 번호를 적는 사람처럼 천천히, 즉 한참씩 멈추며 그 칸에 '
                        '적었다. 그리고 서류철을 닫았지만 제자리에 넣지는 않았다.',
                        '“왜 남겨 뒀는지 물음을 받을 겁니다.” 다음 날 아침 책상 위 서류철을 보며 상급자가 말했다. “자기 봉합에 결론을 올리는 심사관은 자기 자신에게 '
                        '결론을 올리는 겁니다.”',
                        '“내가 무엇을 올리는지 안다.”',
                        '“다른 심사관에게 재배당받고 싶나?”',
                        '“아니요.” Ader가 말했다. “재배당되면 다음 심사관이 팔십사 페이지를 읽고 문제를 가게 쪽이라 여길 겁니다. 문제는 *배석*이라는 단어입니다. 방에 '
                        '들어가 본 심사관은 저뿐이고, 방이 어땠는지 말할 수 있는 사람도 저뿐입니다.”',
                        '결론은 스물여덟째 날 발송되었다. Cinder Lane에는 사본 한 부도 보내지 않았고 편지도 보내지 않았다. 편지를 보내면 그것이 설명이 되었을 '
                        '것이고, 결론 그 자체가 설명이었기 때문이다. 서류철을 서랍에 넣었다. 서랍 겉면에는 자기 손글씨로 가게 이름이 적혀 있었고, 그는 겨울이 지날 때까지 '
                        '그 자리에 두었다.'],
             'title': '자기 책상 위의 서류철',
             'when': '11월 26일'},
      'tr': {'blocks': ["Ader'in ofisinde yan binanın yükleme rıhtımına bakan bir pencere ve üzerinde dosyadan "
                        'başka hiçbir şey olmayan bir masa vardı; masayı Eylül ayında boşaltmıştı ve o günden '
                        'beri üzerinde herhangi bir şeye ihtiyaç duymamıştı.',
                        'Dosya dükkânın dosyasıydı, ama aynı zamanda onun da dosyasıydı. İki yıllık evrak '
                        'birikimiydi; üç talep ve bir resmi şikâyet sonucu elde edilmişti. Ortasına kendi '
                        'eliyle koyduğu, koyduğu günden beri bir daha okumadığı bir sayfa sıkıştırılmıştı.',
                        'Seksen dördüncü sayfa. Dokuz dakika.',
                        'Sayfayı okumadı. İki yılın içinde onu dört kez baştan sona okumuş, her okuyuşundan '
                        'aynı iki sonuçla ayrılmıştı: birleştirme iyi yapılmıştı; kayda aldığı o öğleden '
                        'sonrayı kendisi bir türlü hatırlayamıyordu. Dosyayı tutma kararını asıl başlatan, '
                        'işte bu ikinci sonuçtu.',
                        'Bulgunun numarası form üzerinde hâlâ boş duruyordu. Mart ayından beri boştu. Bulgu '
                        'numarası, denetçi bulduğu şeyin bir bulgu olduğuna karar verdiği anda verilir. Form, '
                        'boş bırakılmış alanıyla birlikte sekiz aydır masanın üzerinde bekliyordu; bir '
                        'aykırılığın basit bir hata mı, yerleşmiş bir alışkanlık mı, yoksa bir kişi mi '
                        'olduğuna karar vermek bu kadar sürebilir.',
                        'Saat dördü vurduğunda, binanın sustığı o vakitte kulaklığı kulağına taktı ve kaydın '
                        'dokuz dakikasını dinlemeye koyuldu.',
                        'Kayıt bir mutfaktaydı. Bunu kendi hayatından değil, yalnızca kaydın kendisinden '
                        'biliyordu. Bir kadın sesi, bir erkek sesi ve o yıllarda sürekli yaptığı şeyi yapan '
                        'kendi sesi duyuluyordu: prosedürü, daha önce dört yüz kez anlatmış bulunan ve dört '
                        'yüz birinci kişinin de ilk kişiyle aynı özeni hak ettiğine hükmetmiş bir adamın '
                        'sakin, düz tonuyla anlatmak.',
                        'Altıncı dakikada kadın, “Beni o mu tanıyacak?” diye sordu. Kendi sesi ise şöyle cevap '
                        'verdi: “Olanın genel şeklini bilecek. İçindeki duygusunu bilmeyecek. Mesleğin esası '
                        'budur.”',
                        'Ader kaydı yedinci dakikada durdurdu; ihtiyaç duyduğu kısmı duymuştu ve kendi sesinin '
                        'bir şeye satıcılık yaptığı gerisini dinlemenin mesleki hiçbir gereğesi yoktu.',
                        'Bulgunun özü, dükkânın bir kuralı çiğnemesi değildi. Bulgu şuydu: Koruma Dairesi 1998 '
                        'yılında bir kural kaleme almış, bu kuralı kimsenin okumadığı bir el kitabında '
                        'bastırmış, ardından kuralı uygulamanın tek yolunun ikinci bir kişinin hazır bulunması '
                        'olduğu bir sistem kurmuştu; ve hazır bulunma durumunu hiç kimse *bulunma* diye '
                        'tanımlamamıştı.',
                        'El kitabı koridor dolabının üçüncü rafındaydı, sırtında yılın yazılı olduğu bir '
                        'cildin içindeydi: 1998. İkinci kişinin görevleri üzerine yazılmış on yedi sayfa; '
                        'bunları tezgâhın başında durmamış olduğu açıkça belli olan biri kaleme almıştı ve '
                        'sayfalardan tek birinde bile aradığı kelime geçmiyordu. On yedi sayfanın hepsini '
                        'yeniden ayakta okudu; çünkü oturarak yapacağı bir okuma, o okumayı resmi bir işlem '
                        'haline getirirdi.',
                        'Cümle, formun üzerinde ayrılmış kutulara sığmayacak kadar uzun olduğu için onu kendi '
                        'el yazısıyla kâğıda döktü; seksen dördüncü sayfayı da dosyaya bir delil niyetiyle '
                        'ekledi. Ardından formun en son boş kutusuyla on bir dakika boyunca oturdu; ancak bu '
                        "sürenin sonunda kutunun içine 12/2026'yı yazdı.",
                        'Bu numara, yılın on ikinci bulgusu ve kendi denetçilik kariyerinin yirmi altıncı '
                        'bulgusu anlamına geliyordu. Kutuya, insanın kaçınagelmiş bir sayıyı yazışı gibi, ağır '
                        'ağır yazdı; ardından dosyayı kapattı, ama bulunduğu çekmeceye kaldırmadı.',
                        '“Neden sakladığın sorulacak,” dedi ertesi sabah amiri, masanın üstündeki dosyaya '
                        'bakarak. “Kendi birleştirmesi üzerine bulgu açan bir denetçi, sonuçta kendi kişisi '
                        'üzerine bir bulgu açmış olur.”',
                        '“Neyi açtığımı biliyorum.”',
                        '“Bu dosyanın başka bir denetçiye verilmesini ister misin?”',
                        '“Hayır,” dedi Ader. “Dosya başka birine devredilirse, sonraki denetçi seksen dördüncü '
                        'sayfayı okur ve sorunun dükkânda olduğunu sanır. Oysa sorun *bulunma* kelimesidir. '
                        'Odada bulunmuş ve odanın nasıl bir yer olduğunu anlatabilmiş tek denetçi benim.”',
                        "Bulgu yirmi sekizinde çıktı. Cinder Lane'e bir kopya göndermedi, yanına bir mektup da "
                        'koymadı; çünkü bir mektup ilave bir açıklama niteliği taşırdı ve bulgunun kendisi '
                        'zaten açıklamaydı. Dosyayı çekmeceye yerleştirdi; çekmecenin yüzünde kendi el '
                        'yazısıyla dükkânın adı yazılıydı ve dosyayı kış gelene kadar orada bıraktı.'],
             'title': 'Kendi Masasındaki Dosya',
             'when': '26 Kasım'},
      'yue': {'blocks': ['Ader 間辦公室有個窗，望住隔籬幢樓嘅上貨位；檯面除咗個檔案乜都冇，因為佢九月清空咗張檯，之後冇需要用上面任何嘢。',
                         '個檔案係間鋪嘅，亦係佢自己嘅。兩年紙，用三次申請同一次正式投訴換返嚟；中間夾住一頁係佢自己放落去，放低嗰日之後冇再讀過。',
                         '第八十四頁。九分鐘。',
                         '佢冇讀。兩年嚟讀過四次，每次都帶走同樣兩件事實：接縫做得靚；佢唔記得錄音入面嗰個下晝。第二件事實就係呢個檔案嘅起點。',
                         '表格上嘅結論編號仲係空白。由三月空到今日。督察決定佢發現嘅嘢算係一個「結論」，先至會有編號；張表喺檯面連個空格擺咗八個月 —— '
                         '決定一個唔妥係錯、係慣例、定係一個人，就係要咁耐。',
                         '四點鐘佢戴耳機 —— 成幢樓靜落嚟嗰個鐘數 —— 聽嗰九分鐘。',
                         '係一個廚房。佢知，因為錄音，唔係因為佢人生。女人聲、男人聲，同佢自己把聲做嗰幾年做嘅嘢：用一個講過四百次、並且決定第四百零一個人都值得同第一個人一樣嘅心機嘅男人嗰種平穩聲線，解釋程序。',
                         '第六分鐘，女人話：「佢會知係我咩？」佢自己把聲話：「佢會知個形。佢唔會知個感覺。呢行就係咁。」',
                         '第七分鐘 Ader 停咗錄音，因為佢要聽嘅已經聽到；亦因為冇任何專業理由，要聽住自己把聲賣嘢賣到落尾。',
                         '結論唔係間鋪違規。結論係：管理局 1998 年寫咗一條規矩，印喺一本冇人讀嘅手冊，然後建咗一個制度 —— 唯一執行方法係要第二個人在場，而從來冇人定義過「在場」。',
                         '手冊喺走廊櫃，第三格，書脊印住年份：1998。十七頁講第二個人嘅職責，寫嗰個人明顯從來冇企喺工作檯前面；十七頁入面，冇一頁有佢要嗰個字。佢企住再讀一次十七頁 —— '
                         '坐住讀，就會令呢次閱讀變成官方行為。',
                         '佢用正楷寫低，因為表格啲格太細載唔到呢句；再將第八十四頁做附件；然後對住表格最後一格坐咗十一分鐘，先寫落 12/2026。',
                         '呢個號碼代表今年第十二個結論、佢事業第二十六個。佢寫入格嘅方式，係一個寫緊一個一直避開嘅號碼嘅人嘅方式 —— 慢；然後佢合上檔案，冇收埋。',
                         '「你會畀人問點解你留住佢，」第二朝上司望住檯面個檔案話。「一個督察為自己條接縫開結論，就係為自己開結論。」',
                         '「我知我開緊咩。」',
                         '「要唔要轉交第二個？」',
                         '「唔，」Ader 話。「轉交咗，下一個督察讀第八十四頁，會以為問題係間鋪。問題係「在場」呢個字。我係唯一入過嗰間房、講得出間房係咩樣嘅督察。」',
                         '結論二十八號出。佢冇寄副本去 Cinder Lane，亦冇寄信 —— '
                         '信會係一個解釋，而結論本身就係解釋。佢將檔案放入抽屜；抽屜上面有間鋪個名，係佢自己嘅字；佢就咁放住，放到冬天。'],
              'title': '自己檯上嘅檔案',
              'when': '11 月 26 日'}},
 12: {'en': {'blocks': ['The statement was taken in the shop because the shop was where the repair had '
                        'happened and the Ward had decided, late and in writing, that a statement should be '
                        'taken where the thing happened rather than where the form was filed.',
                        'The chair by the window had been put there in November for exactly this, and had been '
                        'used twice. The laptop had a battery that lasted three hours and a sticker on the lid '
                        'from a training course in a building that had since been sold.',
                        'The inspector was a young man with a laptop who had been told to record the words and '
                        'not to improve them, and he said this twice before he started, which Elias took to '
                        'mean that he had been told it by somebody who had once had a statement improved.',
                        "The repair was eleven days old. A woman of sixty had brought her father's core in and "
                        'asked for a seam to be reopened so that a name could be put back into a sentence, and '
                        'the seam had been made in 2019 by a hand Elias did not know, and the name had been '
                        'taken out by a repairman who had decided, reasonably, that a name which caused '
                        'distress was a name the customer could live without.',
                        '“Say what you did,” the inspector said.',
                        '“I reopened a bridge that had been made by somebody else, and I put the name back, '
                        'and I closed it beside the old seam rather than across it, so that the next person '
                        'can find both.”',
                        '“Say who was present.”',
                        'Elias said the joint first, in the order the rule requires, because the rule is not '
                        'about courtesy: “Elias Vane, first hand, and Wren Adey, holding. Mara Voss read the '
                        'second account before the loom was started and signed it at nine forty.”',
                        'The inspector typed. Then he said, “The second name on the paperwork is M. Voss. The '
                        'statement says Wren Adey was holding. Is holding a signature?”',
                        'Mara, from the chair by the window, said, “No. Holding is a body at the bench. It is '
                        "not a name on the account. That's why the paperwork has mine.”",
                        "“And the apprentice's name appears where?”",
                        '“In the ledger, under the job, in the second line,” Elias said. “Where it will appear '
                        "every time until she's licensed, and after that it appears on the account and "
                        'somebody else holds.”',
                        'The inspector looked at the ledger, at the page, at the two lines of handwriting — '
                        "his own and Wren's, the second one careful in the way a nineteen-year-old's writing "
                        "is careful when it is being watched — and said, “That's not a signature and it's not "
                        'nothing. What is it?”',
                        'It was the question the whole part of the story turns on, and Elias had been dodging '
                        'it for months because the honest answer made the shop look better than it was and the '
                        'cynical answer made it look worse.',
                        "“It's a record that she was there,” he said. “It doesn't carry liability and it "
                        "doesn't carry a licence. It carries the fact that a second person stood at the bench "
                        "and can say what she saw. In four years, if she's still here, that line will be worth "
                        "something in an audit. Right now it's worth exactly what a witness is worth before "
                        'anybody needs one.”',
                        'The woman of sixty gave her statement after that, which took nine minutes and was '
                        "shorter than the inspector's questions, and at the end she said, “I want to say one "
                        "thing that isn't for the form. I don't care about the seam. I care that somebody "
                        'wrote down that it was there.”',
                        "The inspector closed the laptop. “That's the sentence I'll be quoting,” he said, “if "
                        'it ever gets quoted.”',
                        'When he had gone, Wren took the ledger and read the page again, and then asked the '
                        'question she had not asked in front of the inspector: “Does my line count as a second '
                        'name if something goes wrong?”',
                        "“No,” Elias said. “It counts as a person. That's less than a signature and more than "
                        "nothing, and it's the only thing this shop has that a clinic doesn't.”",
                        '“Then I want it to be a signature,” she said, and went back to the bench, and Elias '
                        'wrote the sentence into the ledger that evening because it was the first time in '
                        'eleven months that anybody in the shop had said what the next part was going to be '
                        'about.'],
             'title': 'The Wording',
             'when': '9 February'},
      'ko': {'blocks': ['진술은 가게 안에서 받았다. 수리가 일어난 곳이 바로 이 가게였기 때문이다. 관리청은 늦게나마 글로 방침을 정했다. 진술은 양식이 제출되는 곳이 아니라, '
                        '일이 벌어진 장소에서 받아야 한다는 방침이었다.',
                        '창가 의자는 바로 이 진술을 받기 위해 11월에 놓은 것이었고 그때까지 두 번 쓰였다. 노트북 배터리는 세 시간을 갔고, 뚜껑에는 그 뒤로 팔린 건물에서 '
                        '열린 교육 과정 스티커가 붙어 있었다.',
                        '심사관은 노트북을 든 젊은 남자였다. 말을 그대로 기록하고 다듬지 말라는 지시를 받았고, 시작하기 전에 두 번이나 그 말을 했다. Elias는 그 말을, '
                        '한때 진술이 다듬어진 적 있는 사람이 그에게 지시했다는 뜻으로 받아들였다.',
                        '수리는 열한 날 된 일이었다. 예순 살 여자가 자기 아버지의 코어를 가져와, 한 문장에 이름을 다시 넣을 수 있도록 봉합선을 다시 열어 달라고 요청했다. '
                        '그 봉합선은 2019년에 Elias가 알지 못하는 손이 만든 것이었다. 괴로움을 주는 이름은 고객이 없이도 살 수 있는 이름이라고 판단한 다른 수리공이 '
                        '그 이름을 빼 냈다.',
                        '“무엇을 했는지 말해 보세요.” 심사관이 말했다.',
                        '“다른 사람이 놓은 다리를 다시 열고 그 이름을 돌려 넣었습니다. 옛 봉합선을 가로지르지 않고 그 옆에 닫아, 다음 사람이 둘 다 찾을 수 있게 '
                        '했습니다.”',
                        '“배석한 사람을 말해 주세요.”',
                        'Elias는 규칙이 요구하는 순서대로, 예의가 아닌 규칙이므로 이음부터 먼저 말했다. “Elias Vane, 첫 손, 그리고 Wren Adey, 잡는 '
                        '사람. Mara Voss는 직조기를 돌리기 전에 두 번째 계정을 읽고 아홉 시 사십 분에 서명했습니다.”',
                        '심사관이 타자를 치다가 물었다. “서류 두 번째 이름은 M. Voss입니다. 진술에는 Wren Adey가 잡았다고 되어 있습니다. 잡는 것이 '
                        '서명입니까?”',
                        '창가 의자의 Mara가 말했다. “아니요. 잡는 것은 작업대의 몸입니다. 계정 위 이름이 아니에요. 그래서 서류에 제 이름이 있는 겁니다.”',
                        '“견습생 이름은 어디에 나옵니까?”',
                        '“장부, 그 작업 아래 두 번째 줄입니다.” Elias가 말했다. “면허를 받을 때까지 매번 거기에 나오고, 그 뒤에는 계정에 이름이 나오고 다른 사람이 '
                        '잡습니다.”',
                        '심사관은 장부를 보고 페이지와 두 줄의 손글씨를 보았다. 자기 것과 Wren의 것이었고, 두 번째 줄은 열아홉 살의 글씨가 지켜볼 때那样 조심스러웠다. '
                        '그리고 물었다. “서명도 아니고 아무것도 아닌 것도 아닙니다. 이게 뭡니까?”',
                        '이 이야기 한 부분 전체가 걸린 질문이었다. Elias는 몇 달 동안 피해 왔다. 정직한 대답은 가게를 실제보다 좋아 보이게 하고 냉소적인 대답은 더 '
                        '나빠 보이게 했기 때문이다.',
                        '“그녀가 거기에 있었다는 기록입니다.” 그가 말했다. “책임도 면허도 싣지 않고, 두 번째 사람이 작업대에 서서 본 것을 말할 수 있다는 사실만 '
                        '싣습니다. 사 년 뒤 그녀가 여기 남아 있다면 그 줄은 감사에서 무언가 값어치가 있을 겁니다. 지금은 누군가 증인을 필요로 하기 전의 증인만큼의 '
                        '값어치밖에 없습니다.”',
                        '그 뒤 예순 살 여자가 자기 진술을 했다. 구 분이 걸렸고 심사관의 질문보다 짧았다. 진술이 끝나자 그녀가 말했다. “양식에는 넣지 않을 말을 하나 하고 '
                        '싶어요. 봉합선은 상관없어요. 누군가 그것이 거기에 있었다고 적어 둔 게 중요해요.”',
                        '심사관이 노트북을 닫았다. “제가 인용하게 될 문장입니다.” 그가 말했다. “인용될 일이 있다면.”',
                        '그가 가게를 나간 뒤 Wren는 장부를 받아 페이지를 다시 읽었다. 그리고 심사관 앞에서는 묻지 않았던 질문을 했다. “무언가 잘못되었을 때 제 줄이 두 '
                        '번째 이름으로 쳐지나요?”',
                        '“아니.” Elias가 말했다. “사람으로 칠 뿐이다. 서명보다는 적고 아무것도 아니기보다는 많으며, 이 가게에 있고 클리닉에는 없는 유일한 것이다.”',
                        '“그럼 그것이 서명이 되고 싶어요.” 그녀가 말하고 작업대로 돌아갔다. Elias는 그날 저녁 그 문장을 장부에 적었다. 열한 달 동안 가게 안에서 '
                        '누구도 다음 부분이 무엇에 관한 것인지 말하지 않았고, 그녀가 처음으로 그것을 말했다.'],
             'title': '문구',
             'when': '2월 9일'},
      'tr': {'blocks': ['İfade dükkânın kendi içinde alındı; çünkü onarımın gerçekleştiği yer tam olarak '
                        'burasıydı ve Koruma Dairesi, geç kalmış olsa da yazılı olarak, ifadenin formun '
                        'dosyaya konduğu yerde değil, olayın olduğu yerde alınması gerektiğine hükmetmişti.',
                        'Pencere kenarındaki sandalye tam olarak bu iş için Kasım ayında oraya konmuştu ve '
                        'şimdiye kadar iki kez kullanılmıştı. Dizüstü bilgisayarın üç saat giden bir pili '
                        'vardı; kapağının üzerinde, o zamandan beri satılmış olan bir binada düzenlenmiş '
                        'eğitim kursundan kalma bir çıkartma duruyordu.',
                        'Denetçi, yanında dizüstü bilgisayar taşıyan genç bir adamdı; kendisine sözleri '
                        'kaydetmesi, üzerinde hiçbir düzeltme yapmaması söylenmişti. İşe başlamadan önce bu '
                        'talimatı iki kez tekrarladı. Elias bundan, bir zamanlar kendi ifadesi düzeltilmiş '
                        'olan birinin bunu ona söylemiş olduğunu çıkardı.',
                        'Onarımın üzerinden on bir gün geçmişti. Altmış yaşlarında bir kadın, babasına ait '
                        'olan çekirdeği dükkâna getirmiş ve bir cümlenin içine adı geri konulabilsin diye eski '
                        "bir dikişin yeniden açılmasını talep etmişti. O dikiş 2019 yılında Elias'ın "
                        'tanımadığı bir el tarafından atılmıştı; çıkartılan adı ise, ıstıraba yol açan bir '
                        'ismin onsuz da yaşanabileceğine makul bir biçimde karar vermiş bulunan bir onarımcı '
                        'almıştı.',
                        '“Yaptığınız işi anlatın,” dedi denetçi.',
                        '“Başkasının kurduğu köprüyü yeniden açtım, adı geri koydum, eski dikişin üstünden '
                        'değil yanından kapattım, öyle ki sonraki kişi ikisini de bulabilsin.”',
                        '“Kimlerin bulunduğunu söyle.”',
                        'Elias kuralın gerektirdiği sırayla önce ikiliyi söyledi; çünkü kural nezaket '
                        'gösterisiyle ilgili değildi: “Elias Vane, birinci el; Wren Adey, çerçeve tutuyor. '
                        'Mara Voss tezgâh çalıştırılmadan önce ikinci kaydı okumuş ve saat dokuz kırkta '
                        'imzalamıştır.”',
                        'Denetçi klavyede yazdı. Sonra sözlerini sürdürdü: “Evrak üzerindeki ikinci ad M. '
                        "Voss. İfadede Wren Adey'in çerçeve tuttuğu belirtiliyor. Tutmak diye sözü edilen şey "
                        'bir imza mıdır?”',
                        'Mara pencere kenarındaki sandalyeden cevap verdi: “Hayır. Tutmak, tezgâhın başında '
                        'bulunmuş bir bedendir. Kayıt üzerinde yer alan bir ad değildir. Evrakta benim adımın '
                        'bulunmasının nedeni budur.”',
                        '“Çırağın adı nerede geçiyor?”',
                        '“Defterde, işin hemen altında, ikinci satırın üzerinde,” dedi Elias. “Lisans sahibi '
                        'olana kadar her kayıtta orada geçecektir; ondan sonra adı kayda yazılır ve başka biri '
                        'çerçeveyi tutar.”',
                        'Denetçi önce deftere, sonra açık sayfaya, ardından iki el yazısı satırına baktı; biri '
                        "kendininkine, diğeri Wren'e aitti. İkincisi, göz önünde yazılırken on dokuz yaşındaki "
                        'birinin yazısının taşıyacağı özeni gösteriyordu. “Bu bir imza sayılmaz, ama boş bir '
                        'şey de değildir,” dedi. “O halde nedir?”',
                        'Hikâyenin bütün bu bölümünün dayandığı soruydu bu ve Elias aylardır bu sorunun '
                        'çevresinden dolanıyordu; çünkü dürüst cevap dükkânı olduğundan daha iyi bir yer gibi '
                        'gösteriyor, alaycı cevap ise daha kötü bir yer gibi gösteriyordu.',
                        '“Onun o sırada orada hazır bulunduğunu gösteren bir kayıttır,” dedi. “Sorumluluk '
                        'yüklenmez, lisans taşımaz. İkinci bir kişinin tezgâhın başında durduğunu ve '
                        'gördüklerini anlatabileceği gerçeğini taşır. Dört yıl sonra hâlâ burada olursa, o '
                        'satır bir denetim sırasında bir değer ifade edecektir. Şu anki değeri ise, henüz '
                        'kimseye ihtiyaç duyulmamış bir tanığın taşıdığı değerle tam olarak aynıdır.”',
                        'Altmış yaşlarındaki kadın ondan sonra kendi ifadesini verdi; anlatması dokuz dakika '
                        'sürdü ve denetçinin sorularından daha kısaydı. Sözlerinin bitiminde şöyle konuştu: '
                        '“Forma geçirilmeyecek bir şey söylemek istiyorum. Dikiş benim umurumda değil. Orada '
                        'bulunduğunu birinin yazıya dökmüş olması benim için önemli.”',
                        'Denetçi dizüstü bilgisayarı kapattı. “İleride bu sözler bir yerde alıntı yapılacak '
                        'olursa, alıntılayacağım cümle budur,” dedi.',
                        'Adam dükkândan gittikten sonra Wren defteri eline aldı, açık sayfayı bir kez daha '
                        'okudu; ardından denetçinin önünde soramadığı o soruyu sordu: “Bir iş ters giderse, '
                        'benim satırım ikinci bir ad olarak sayılır mı?”',
                        '“Hayır,” dedi Elias. “Bir kişi olarak sayılır yalnızca. Bu, bir imzadan azdır ama '
                        'hiçbir şeyden fazladır; ve bu dükkânda bir klinikte bulunmayan tek şeydir.”',
                        '“O zaman bunun bir imza olmasını istiyorum,” dedi ve tezgâha doğru geri döndü. Elias '
                        'akşam o cümleyi deftere işledi; on bir ay boyunca dükkânda bulunan ilk kişi, bir '
                        'sonraki bölümün ne üzerine olacağını açıkça söylemişti.'],
             'title': 'Kelime Seçimi',
             'when': '9 Şubat'},
      'yue': {'blocks': ['聲明喺鋪頭錄，因為修補喺鋪頭發生，而管理局遲咗、但用書面決定：聲明要喺件事發生嘅地方錄，唔係喺表格歸檔嘅地方。',
                         '窗邊嗰張椅十一月擺咗喺度就係為咗呢件事，用過兩次。部筆記本電腦嘅電得三個鐘，蓋上有張貼紙，係一個已經賣咗嘅樓入面嘅訓練課程。',
                         '督察係個後生仔，帶住電腦；佢收到嘅指示係照字錄，唔准改好。佢開工前講咗兩次，Elias 覺得，即係有人同佢講過呢句，而嗰個人以前試過畀人改好一份聲明。',
                         '呢個修補已經十一天。一個六十歲嘅女人帶住佢阿爸個記憶核嚟，要求開返一條接縫，將一個名放返入一句句子；條縫係 2019 年由一隻 Elias '
                         '唔識嘅手做，個名係由一個修補師拎走 —— 佢當時嘅判斷好合理：一個令人痛苦嘅名，係客人可以冇咗嘅名。',
                         '「講你做咗咩，」督察話。',
                         '「我開返一條由人哋做嘅橋，放返個名，然後喺舊縫隔籬收口，唔係打橫閂過佢，等下一個人兩條都搵得到。」',
                         '「講邊個在場。」',
                         'Elias 先講合夥人，按規條要求嘅次序 —— 因為規條唔係講禮貌：「Elias Vane，第一隻手；Wren Adey，揸住。Mara Voss '
                         '喺開機之前讀咗第二個戶口，九點四十分簽咗。」',
                         '督察打字。然後話：「文件上第二個名係 M. Voss。聲明話揸住嘅係 Wren Adey。揸住算唔算簽名？」',
                         'Mara 喺窗邊張椅話：「唔算。揸住係工作檯前面有個人。唔係戶口上嘅名。所以文件上係我個名。」',
                         '「咁學徒個名出現喺邊？」',
                         '「喺簿，喺單下面，第二行，」Elias 話。「佢未攞牌之前，每次都喺呢個位；攞牌之後，個名上戶口，換另一個人揸住。」',
                         '督察望簿、望頁、望兩行字 —— 一行佢自己，一行 Wren，第二行小心到係一個十九歲嘅人知道有人望住嘅時候嘅小心 —— 然後話：「呢個唔係簽名，亦唔係冇嘢。咁係咩？」',
                         '呢條問題就係呢一部轉嘅軸；Elias 避咗幾個月，因為誠實答案令間鋪睇落好過實際，而犬儒答案令佢睇落差過實際。',
                         '「係一個紀錄：佢在場，」佢話。「唔孭責任，亦唔孭牌照。孭嘅係：有第二個人企喺工作檯前，講得出佢見到咩。四年後，如果佢仲喺度，呢一行喺審計度值啲嘢。而家，佢值嘅就係一個證人喺未有人需要之前嘅價值。」',
                         '六十歲嘅女人之後講佢嘅聲明，講咗九分鐘，比督察問嘅短；講完佢話：「我想講一句唔係畀表格嘅。我唔介意條縫。我介意有人寫低佢喺度。」',
                         '督察合上電腦。「呢句我會引，」佢話，「如果有一日要引。」',
                         '佢走咗之後，Wren 攞返簿，再讀一次嗰頁，然後問佢喺督察面前冇問嘅問題：「如果出事，我嗰行算唔算第二個名？」',
                         '「唔算，」Elias 話。「佢算一個人。少過一個簽名，多過乜都冇；而呢樣係呢間鋪有、診所冇嘅唯一嘢。」',
                         '「咁我要佢變成一個簽名，」佢話，返去工作檯；嗰晚 Elias 將呢句寫入簿，因為呢係十一個月嚟第一次，鋪入面有人講出下一部要講咩。'],
              'title': '字眼',
              'when': '2 月 9 日'}},
 13: {'en': {'blocks': ['In April the shop had a smell it did not have in winter, which was the smell of the '
                        'lane drying out, and Elias opened the ledger on a Monday morning and counted the '
                        'pages left in it, which is a thing he had done in November and had avoided doing '
                        'since.',
                        'Sixty. Maybe sixty-one if the last gathering had been bound tight.',
                        'He did the arithmetic on the back of a fill ticket because the ledger is for the '
                        'record and not for the arithmetic. Eleven weeks to the end of June at five entries a '
                        'week was fifty-five, and there were the two weeks in March when the shop had closed '
                        'for the boiler, and there was the fact that a ledger does not end because the pages '
                        'end: it ends because the year ends, or because the shop ends, or because the person '
                        'writing it decides that the next page is the last one.',
                        "“You're counting,” Wren said, from the bench. She was on the new loom three days a "
                        'week now and had stopped saying sorry, and she had begun to say *we* about the shop '
                        'in a way that Elias noticed and did not correct.',
                        "“I'm counting.”",
                        '“How many?”',
                        '“Sixty.”',
                        "“That's a hundred and eighty jobs if you do three pages a job.”",
                        "“It's a hundred and eighty jobs if nothing goes wrong, and it's a book about things "
                        'going wrong.”',
                        'She thought about it, which was one of the two things she did better than anybody he '
                        "had worked with; the other was hold. “Then don't end it at the year,” she said. “End "
                        'it when the book ends. A year is a thing the Ward invented. The book is a thing you '
                        'invented.”',
                        'He looked at her for a moment. Then he turned the ledger round and showed her the '
                        'inside of the back cover, where he had written the hire, and the sentence about her '
                        'reading the book before the loom.',
                        "“I know,” she said. “I read it. I read everything in this shop that isn't a "
                        "customer's.”",
                        "“Then you know why I can't write *the year ended* on the last page.”",
                        "“I know why you can't write it,” she said. “I don't know what you'll write instead, "
                        "and neither do you, and that's the first honest thing either of us has said this "
                        'morning.”',
                        "The morning's work was a seam on a core that had been in a drawer for six years, and "
                        'the customer was a man who had brought it in on the advice of his sister and who did '
                        'not want it repaired, only opened, looked at, and closed again, which is a job the '
                        'trade does not advertise and charges for anyway. Wren held. Mara read the second '
                        'account and asked the customer what he expected to see, and the customer said, '
                        "“Nothing. I want to know that it's still exactly as bad as I remember,” and Mara "
                        'wrote that down in the ledger because it was the best description of the trade either '
                        'of them had heard from a customer in a year.',
                        'In the afternoon Elias did what he had been putting off: he wrote the plan for the '
                        'last part of the book on the inside cover, in outline, in the small handwriting he '
                        'used for things that were going to be looked at. Thirteen lines, one for each part, '
                        'and under the last one, three words he did not finish and did not cross out: *the '
                        'last entry*.',
                        'The line on the sign had been written in the first week, in the tone of a man who '
                        'thought the shop would last a year: *Repairs, and refusals, in writing.* Eleven '
                        'months of ledger had made the second half of that sentence the accurate half, and the '
                        'first half the flattering one, which is a thing that happens to signwriters.',
                        "The sign was still up. It had been up for sixteen months and it had the shop's name "
                        'on it and, underneath, the line about repairs and refusals. In June it would come '
                        'down for a Monday and go back up on the Friday with one line changed, and he knew '
                        'that already in April, which is why he wrote the plan in April and left the ending to '
                        'the pages that were left.'],
             'title': 'Sixty Pages',
             'when': '19 April'},
      'ko': {'blocks': ['4월이 되자 가게에는 겨울 내내 없던 냄새가 났다. 겨울 내내 눅눅했던 골목이 마르는 냄새였다. Elias는 월요일 아침 장부를 펼치고 남은 페이지를 '
                        '헤아렸다. 그 일은 11월에 한 번 해 본 뒤로 줄곧 피해 온 일이었다.',
                        '육십. 마지막 속매가 단단히 묶였다면 육십일일 수도 있었다.',
                        '그는 채움 전표 뒷편에 계산을 적었다. 장부는 기록을 남기는 것이지 계산을 하는 자리가 아니기 때문이다. 6월 말까지 열한 주, 주에 다섯 건씩이면 '
                        '오십오 건이었고, 3월 보일러 공사 때문에 가게를 닫았던 두 주가 따로 있었다. 장부는 페이지가 다 떨어진다고 해서 끝나지 않는다. 해가 끝나면 끝나고, '
                        '가게가 끝나면 끝나며, 장부를 쓰는 사람이 다음 페이지를 마지막이라고 결정할 때 끝난다.',
                        '“세고 있네요.” Wren가 작업대 쪽에서 말했다. 그녀는 이제 주에 사흘씩 새 직조기를 돌렸고 사과하는 말을 그만두었다. 그리고 가게를 *우리*라고 '
                        '말하기 시작했고, Elias는 그 말버릇을 눈치챘지만 고치지 않았다.',
                        '“세고 있다.”',
                        '“몇이에요?”',
                        '“육십.”',
                        '“작업 하나에 세 페이지로 잡으면 백팔십 건이 나오네요.”',
                        '“잘못되는 일이 없으면 백팔십 건이고, 이 책은 잘못되는 일에 관한 책이다.”',
                        '그녀는 그것을 곰곰이 생각했다. 그가 함께 일한 누구보다 그녀가 잘하는 두 가지 중 하나였고, 다른 하나는 잡는 일이었다. “그럼 해 기준으로 끝내지 '
                        '마세요. 책이 끝날 때 끝내세요. 해는 관리청이 만든 것이고 책은 당신이 만든 거예요.”',
                        '그는 잠시 그녀를 보았다. 그리고 장부를 그녀 쪽으로 돌려 뒷표지 안쪽을 보여 주었다. 그 안쪽에는 고용에 관한 내용과, 그녀가 직조기보다 먼저 책을 '
                        '읽었다는 문장이 적혀 있었다.',
                        '“알아요.” 그녀가 말했다. “읽었어요. 이 가게에서 손님 것이 아닌 것은 다 읽어요.”',
                        '“그럼 마지막 페이지에 *해 끝남*이라고 쓸 수 없는 이유는 알 테지.”',
                        '“왜 못 쓰는지 저도 알아요.” 그녀가 말했다. “대신 무엇을 쓸지는 저도 모르고 당신도 모르죠. 그게 오늘 아침 우리 둘이 한 첫 번째 정직한 '
                        '말이에요.”',
                        '아침에 맡은 작업은 서랍 안에 육 년 동안 있던 코어의 봉합선이었다. 고객은 누이의 권유로 가져온 남자였고, 코어를 고쳐 달라고 하지 않고 열어서 보기만 '
                        '하고 다시 닫아 달라고 했다. 업계가 광고에 내걸지 않지만 그래도 값을 받는 일이다. Wren가 틀을 잡고 서 있었다. Mara는 두 번째 계정을 읽은 '
                        '뒤 고객에게 무엇을 보리라 기대하는지 물었다. 고객은 “아무것도요. 내가 기억하는 만큼 그대로 나쁜지 확인하고 싶어요”라고 했고, Mara는 그 말을 '
                        '장부에 적었다. 일 년 동안 그들 둘이 손님에게서 들은 업계 설명 가운데 가장 좋은 설명이었기 때문이다.',
                        '오후에 Elias는 오래 미뤄 온 일을 했다. 책 마지막 부분에 대한 계획을 안쪽 표지에 개요로 적었다. 뒤에서 누군가 보게 될 것들에 쓰는 작은 '
                        '글씨였다. 열세 줄이었다. 각 부분에 한 줄씩, 마지막 줄 아래에는 끝내지도 않고 지우지도 않은 세 단어가 남아 있었다. *마지막 기록*.',
                        '간판의 글줄은 첫 주에 쓰였다. 가게가 일 년은 갈 것이라고 생각한 사람의 톤이었다. 그 문장은 두 부분으로 나뉘어 있었다. *수리, 그리고 거절, '
                        '기록으로.* 열한 달 치 장부는 그 문장의 뒷절을 정확한 절로, 앞절을 미화하는 절로 만들었다. 간판에 글을 쓰는 사람에게 흔히 생기는 일이다.',
                        '간판은 아직도 그 자리에 걸려 있었다. 열여섯 달 동안 내리 걸려 있었다. 간판 윗부분에 가게 이름이, 그 아래에 수리와 거절에 관한 글줄이 적혀 '
                        '있었다. 6월이 되면 월요일에 내리고 금요일에 한 줄을 바꿔 다시 올릴 것이다. 그는 벌써 4월에 그 계획을 알고 있었고, 그래서 계획을 4월에 쓰고 '
                        '결말은 남은 페이지들에 맡겼다.'],
             'title': '육십 페이지',
             'when': '4월 19일'},
      'tr': {'blocks': ['Nisan ayına gelindiğinde dükkânın kış mevsiminde taşımadığı bir koku belirdi: sokağın '
                        'kuruma kokusu. Elias bir Pazartesi sabahı defteri önünde açtı ve içinde kalmış '
                        'sayfaların sayısını çıkardı; bu işi Kasım ayında yapmış, o günden sonra bir daha '
                        'yapmaktan kaçınmıştı.',
                        'Altmış. Son demet sıkı ciltlenmişse altmış bir olabilir.',
                        'Hesabı bir dolgu fişinin arkasına yaptı; çünkü defter kayıt tutmak içindir, hesap '
                        'çıkarmak için değildir. Haftada beşer kayıtla Haziran ayının sonuna dek on bir hafta '
                        'elli beş sayfa ediyordu; bir de kazan yüzünden dükkânın bir süre kapalı kaldığı Mart '
                        'ayının iki haftası vardı. Bir de şu gerçek duruyordu: bir defter yalnızca kâğıt '
                        'sayfaları bittiği için sona ermez; yıl bittiği, dükkân kapandığı ya da defteri yazan '
                        'kişi bir sonraki sayfanın son sayfa olduğuna kendi karar verdiği için sona erer.',
                        '“Sayıyorsun,” dedi Wren, bulunduğu tezgâhtan. Şimdi haftada üç gün yeni tezgâhtaydı, '
                        'özür dilemeyi bırakmıştı; dükkân söz konusu olduğunda *biz* demeye başlamıştı, Elias '
                        'bunu fark etti, ama onu sözünden düzeltmedi.',
                        '“Sayıyorum.”',
                        '“Kaç?”',
                        '“Altmış.”',
                        '“Her işe üç sayfa verirsen bu yüz seksen iş eder.”',
                        '“Hiçbir şey yolunda gitmezse yüz seksen iş eder; oysa bu kitap, yolunda gitmeyen '
                        'şeyler hakkında yazılmıştır.”',
                        'Bunu bir süre kafasında düşündü; birlikte çalıştığı insanlar arasında herkesten iyi '
                        'yaptığı iki şeyden biriydi bu, diğeri ise çerçeveyi tutmaktı. “O zaman kitabı yılın '
                        'sonunda bitirme,” dedi. “Kitap kendisi bittiğinde, o zaman bitir. Yıl Koruma '
                        "Dairesi'nin uydurduğu bir şeydir. Kitap ise senin uydurduğun bir şey.”",
                        'Elias bir süre yüzüne baktı. Sonra elindeki defteri çevirdi ve arka kapağın iç yüzünü '
                        'ona doğru gösterdi: işe almayı yazdığı yeri, tezgâhtan önce kitabı okuduğuna dair o '
                        'cümleyi.',
                        '“Biliyorum,” dedi. “Okudum. Bu dükkânda müşteriye ait olmayan her şeyi okurum.”',
                        '“O zaman son sayfaya *yıl bitti* diye yazamayışımın nedenini biliyorsun.”',
                        '“Neden o sözcüğü yazamadığını biliyorum,” dedi. “Yerine başka ne yazacağını ben '
                        'bilmiyorum, sen de bilmiyorsun; ve bu, bu sabah ikimizin de ağzından çıkan ilk dürüst '
                        'cümledir.”',
                        'Sabah yürütülen iş, altı yıldır bir çekmecenin içinde bekleyen bir çekirdekteki '
                        'dikişti. Müşteri, kendi kızkardeşinin öğüdüyle bu çekirdeği dükkâna getirmiş bir '
                        'erkekti; onarılmasını istemiyordu, yalnızca açılmasını, bakılmasını ve sonra yeniden '
                        'kapatılmasını istiyordu; bu, mesleğin ilanlarda anlatmadığı, yine de karşılığında '
                        'ücret aldığı bir iş türüydü. Wren çerçeveyi tuttu. Mara ikinci kaydı okudu ve '
                        'müşteriye orada ne görmeyi beklediğini sordu. Müşteri ise “Hiçbir şey,” dedi. “Hâlâ '
                        'tam olarak hatırladığım kadar kötü olduğunu bilmek istiyorum yalnızca.” Mara bu '
                        'sözleri deftere geçirdi; bir yıldan beri herhangi bir müşteri ağzından duydukları, '
                        'mesleğin en iyi tanımıydı bu.',
                        'Öğleden sonra Elias ertelediği işi yaptı: kitabın son bölümü için planı iç kapağa, '
                        'ana hatlarıyla, daha sonra gözden geçirilecek şeyler için kullandığı küçük el '
                        'yazısıyla yazdı. On üç satır vardı, her bölüm için bir tane; en sonuncu satırın '
                        'altında ise, tamamlamadığı ve üzerini çizmediği üç kelime duruyordu: *son kayıt*.',
                        'Tabeladaki satır, dükkânın bir yıl süreceğini sanan bir adamın tonuyla ilk hafta '
                        'yazılmıştı: *Onarımlar ve retler, yazıyla.* On bir aylık defter, o cümlenin ikinci '
                        'yarısını doğru olan, ilk yarısını ise hoşa giden bölüm haline getirmişti; tabela '
                        'yazarlarının başına gelen sıradan bir durum bu.',
                        'Tabela hâlâ dükkânın ön duvarında asılı duruyordu. On altı aydır oradaydı; üzerinde '
                        "dükkânın adı, altında onarımlar ve retler satırı bulunuyordu. Haziran'da bir "
                        'Pazartesi günü aşağı inecek, Cuma günü tek satırı değiştirilmiş olarak yerine geri '
                        "çıkacaktı. Bunu daha Nisan ayında biliyordu; planı Nisan'da yazıp kitabın sonunu "
                        'geride kalan sayfalara bırakmasının nedeni buydu.'],
             'title': 'Altmış Sayfa',
             'when': '19 Nisan'},
      'yue': {'blocks': ['四月，間鋪有種冬天冇嘅味 —— 條巷乾返嘅味；Elias 禮拜一朝早打開簿，數剩幾多頁。呢件事佢十一月做過一次，之後一直避開。',
                         '六十。如果最後一疊裝訂黐得實，可能六十一。',
                         '佢喺張填料單背面計數，因為簿係用嚟記，唔係用嚟計。到六月底仲有十一週，一週五條，五十五；三月有兩個禮拜因為鍋爐閂過鋪；仲有一件事：簿唔會因為頁用完而完 —— '
                         '佢完，係因為年完、因為鋪完，或者因為寫嗰個人決定下一頁係最後一頁。',
                         '「你喺度數，」Wren 喺工作檯話。佢而家一週三日喺新織機，已經唔再講對唔住；佢開始用「我哋」講間鋪，Elias 留意到，冇糾正。',
                         '「我喺度數。」',
                         '「幾多？」',
                         '「六十。」',
                         '「一單三頁，即係一百八十單。」',
                         '「如果乜都唔出事，就係一百八十單；而呢本係一本講出事嘅書。」',
                         '佢諗咗一陣 —— 呢樣係佢兩樣做得比 Elias '
                         '合過嘅任何人好嘅事之一，另一樣係揸住。「咁就唔好喺年尾收，」佢話。「喺本書完嗰陣收。年係管理局發明嘅。本書係你發明嘅。」',
                         '佢望住佢一陣。然後轉個簿，畀佢睇後封面內側 —— 嗰度寫住請人，同埋嗰句關於佢讀完本書先讀織機。',
                         '「我知，」佢話。「我讀過。呢間鋪入面唔係客人嘅嘢，我全部讀過。」',
                         '「咁你知我點解唔可以喺最後一頁寫『年完咗』。」',
                         '「我知你點解唔可以寫，」佢話。「我唔知你會寫咩；你都唔知。呢句係今朝我哋兩個講嘅第一句誠實話。」',
                         '今朝嘅工係一條縫：一個喺抽屜擺咗六年嘅記憶核；客人係個男人，佢家姐叫佢嚟，佢唔想修補，只想打開、睇吓、再合返 —— 呢種工呢行唔賣廣告，但照收錢。Wren '
                         '揸住。Mara 讀第二個戶口，問客人想見到咩；客人話：「乜都唔想。我想知佢仲係唔係同我記得一樣差。」Mara '
                         '將呢句寫入簿，因為呢係一年嚟佢哋喺客人身上聽到、對呢行最好嘅描述。',
                         '下晝 Elias '
                         '做咗佢一直拖住嘅事：喺內封面寫低本書最後一部嘅計劃，大綱式，用佢寫「會畀人睇」嘅嘢嗰種細字。十三行，一部一行；最後一行下面，三個字，佢冇寫完，亦冇劃走：*最後一賬*。',
                         '招牌上嗰句係第一個禮拜寫嘅，語氣係一個以為間鋪頂到一年嘅人：*修補，同拒絕，都寫低。* 十一個月嘅簿，令句子後半變成準確嗰半，前半變成好聽嗰半 —— '
                         '寫招牌嘅人總會遇到呢種事。',
                         '招牌仲掛住。掛咗十六個月，上面有鋪頭個名，下面係嗰句修補同拒絕。六月佢會落一個禮拜一，禮拜五再掛返，改一行字；四月佢已經知，所以四月寫計劃，將結尾留畀剩低嗰啲頁。'],
              'title': '六十頁',
              'when': '4 月 19 日'}}}
