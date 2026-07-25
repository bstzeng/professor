// 韓文拼音聽力練習題庫：100 句實用旅遊韓文句子。
// 每題格式：{ ko: 韓文原句, ro: 羅馬拼音, zh: 中文意思, cat: 分類標籤 }
// 給 topics/korean/practice.html 的練習頁使用（js/korean-quiz.js 負責出題邏輯）。
// 這些句子的發音檔存放在 audio/ko/ 底下，檔名規則與課程內文完全相同
// （見 js/korean-audio.js 的說明），由 tools/gen-korean-audio.py 產生。

window.KOREAN_QUIZ_SENTENCES = [
  // 打招呼與基本禮貌
  { ko: "안녕하세요", ro: "annyeonghaseyo", zh: "你好", cat: "打招呼" },
  { ko: "안녕히 가세요", ro: "annyeonghi gaseyo", zh: "慢走（自己留下，對方離開時說）", cat: "打招呼" },
  { ko: "안녕히 계세요", ro: "annyeonghi gyeseyo", zh: "慢走（自己離開，對方留下時說）", cat: "打招呼" },
  { ko: "감사합니다", ro: "gamsahamnida", zh: "謝謝", cat: "打招呼" },
  { ko: "죄송합니다", ro: "joesonghamnida", zh: "對不起", cat: "打招呼" },
  { ko: "괜찮아요", ro: "gwaenchanayo", zh: "沒關係／還可以", cat: "打招呼" },
  { ko: "만나서 반가워요", ro: "mannaseo bangawoyo", zh: "很高興認識你", cat: "打招呼" },
  { ko: "잘 먹겠습니다", ro: "jal meokgesseumnida", zh: "我要開動了", cat: "打招呼" },
  { ko: "잘 먹었습니다", ro: "jal meogeosseumnida", zh: "我吃飽了（謝謝招待）", cat: "打招呼" },
  { ko: "수고하세요", ro: "sugohaseyo", zh: "辛苦了（對還在工作的人說的道別語）", cat: "打招呼" },

  // 自我介紹與基本問答
  { ko: "저는 대만 사람이에요", ro: "jeoneun daeman saramieyo", zh: "我是台灣人", cat: "自我介紹" },
  { ko: "이름이 뭐예요", ro: "ireumi mwoyeyo", zh: "你叫什麼名字？", cat: "自我介紹" },
  { ko: "제 이름은 지영이에요", ro: "je ireumeun jiyeongieyo", zh: "我的名字是志英", cat: "自我介紹" },
  { ko: "한국에 처음 왔어요", ro: "hanguge cheoeum wasseoyo", zh: "我第一次來韓國", cat: "自我介紹" },
  { ko: "여행하러 왔어요", ro: "yeohaenghareo wasseoyo", zh: "我是來旅遊的", cat: "自我介紹" },
  { ko: "영어 하세요", ro: "yeongeo haseyo", zh: "你會說英文嗎？", cat: "自我介紹" },
  { ko: "한국어를 몰라요", ro: "hangugeoreul mollayo", zh: "我不懂韓語", cat: "自我介紹" },
  { ko: "천천히 말해 주세요", ro: "cheoncheonhi malhae juseyo", zh: "請說慢一點", cat: "自我介紹" },

  // 問路與方向
  { ko: "화장실이 어디예요", ro: "hwajangsiri eodiyeyo", zh: "廁所在哪裡？", cat: "問路" },
  { ko: "여기가 어디예요", ro: "yeogiga eodiyeyo", zh: "這裡是哪裡？", cat: "問路" },
  { ko: "길을 잃었어요", ro: "gireul ireosseoyo", zh: "我迷路了", cat: "問路" },
  { ko: "지하철역이 어디예요", ro: "jihacheollyeogi eodiyeyo", zh: "地鐵站在哪裡？", cat: "問路" },
  { ko: "이 근처에 있어요", ro: "i geuncheoe isseoyo", zh: "就在這附近", cat: "問路" },
  { ko: "얼마나 걸려요", ro: "eolmana geollyeoyo", zh: "要花多久時間？", cat: "問路" },
  { ko: "여기서 멀어요", ro: "yeogiseo meoreoyo", zh: "離這裡很遠嗎？", cat: "問路" },
  { ko: "걸어서 갈 수 있어요", ro: "georeoseo gal su isseoyo", zh: "可以走路過去嗎？", cat: "問路" },
  { ko: "오른쪽으로 가세요", ro: "oreunjjogeuro gaseyo", zh: "請往右走", cat: "問路" },
  { ko: "왼쪽으로 가세요", ro: "oenjjogeuro gaseyo", zh: "請往左走", cat: "問路" },

  // 交通：地鐵、公車、計程車
  { ko: "여기로 가 주세요", ro: "yeogiro ga juseyo", zh: "請載我去這裡", cat: "交通" },
  { ko: "공항으로 가 주세요", ro: "gonghangeuro ga juseyo", zh: "請載我去機場", cat: "交通" },
  { ko: "버스 정류장이 어디예요", ro: "beoseu jeongnyujangi eodiyeyo", zh: "公車站在哪裡？", cat: "交通" },
  { ko: "이 버스 홍대에 가요", ro: "i beoseu hongdaee gayo", zh: "這班公車有到弘大嗎？", cat: "交通" },
  { ko: "다음 역에서 내려요", ro: "daeum yeogeseo naeryeoyo", zh: "我在下一站下車", cat: "交通" },
  { ko: "여기서 환승해요", ro: "yeogiseo hwanseunghaeyo", zh: "在這裡轉乘", cat: "交通" },
  { ko: "표 한 장 주세요", ro: "pyo han jang juseyo", zh: "請給我一張票", cat: "交通" },
  { ko: "얼마나 남았어요", ro: "eolmana namasseoyo", zh: "還剩多久？", cat: "交通" },
  { ko: "여기 세워 주세요", ro: "yeogi sewo juseyo", zh: "請在這裡停車", cat: "交通" },
  { ko: "카드로 계산할게요", ro: "kadeuro gyesanhalgeyo", zh: "我要刷卡付款", cat: "交通" },

  // 飯店住宿
  { ko: "예약했어요", ro: "yeyakhaesseoyo", zh: "我有預約", cat: "住宿" },
  { ko: "체크인하고 싶어요", ro: "chekeuinhago sipeoyo", zh: "我想辦理入住", cat: "住宿" },
  { ko: "체크아웃 몇 시예요", ro: "chekeuaut myeot siyeyo", zh: "幾點退房？", cat: "住宿" },
  { ko: "방을 바꿀 수 있어요", ro: "bangeul bakkul su isseoyo", zh: "可以換房間嗎？", cat: "住宿" },
  { ko: "와이파이 비밀번호가 뭐예요", ro: "waipai bimilbeonhoga mwoyeyo", zh: "Wi-Fi 密碼是什麼？", cat: "住宿" },
  { ko: "에어컨이 안 돼요", ro: "eeokeoni an dwaeyo", zh: "冷氣不能用", cat: "住宿" },
  { ko: "수건 좀 더 주세요", ro: "sugeon jom deo juseyo", zh: "請再給我一些毛巾", cat: "住宿" },
  { ko: "짐을 맡길 수 있어요", ro: "jimeul matgil su isseoyo", zh: "可以寄放行李嗎？", cat: "住宿" },

  // 餐廳點餐
  { ko: "메뉴 좀 보여주세요", ro: "menyu jom boyeojuseyo", zh: "請給我看菜單", cat: "餐廳" },
  { ko: "이거 주세요", ro: "igeo juseyo", zh: "請給我這個", cat: "餐廳" },
  { ko: "이거 하나 주세요", ro: "igeo hana juseyo", zh: "請給我一份這個", cat: "餐廳" },
  { ko: "하나 더 주세요", ro: "hana deo juseyo", zh: "再一份", cat: "餐廳" },
  { ko: "맵지 않게 해주세요", ro: "maepji anke haejuseyo", zh: "請幫我不要辣", cat: "餐廳" },
  { ko: "물 좀 주세요", ro: "mul jom juseyo", zh: "請給我水", cat: "餐廳" },
  { ko: "여기서 먹을 거예요", ro: "yeogiseo meogeul geoyeyo", zh: "內用", cat: "餐廳" },
  { ko: "포장이에요", ro: "pojangieyo", zh: "外帶", cat: "餐廳" },
  { ko: "배달 되나요", ro: "baedal doenayo", zh: "可以外送嗎？", cat: "餐廳" },
  { ko: "이거 맛있어요", ro: "igeo masisseoyo", zh: "這個很好吃", cat: "餐廳" },
  { ko: "계산해 주세요", ro: "gyesanhae juseyo", zh: "請幫我結帳", cat: "餐廳" },
  { ko: "젓가락 좀 주세요", ro: "jeotgarak jom juseyo", zh: "請給我筷子", cat: "餐廳" },

  // 咖啡廳與小吃攤
  { ko: "아이스 아메리카노 주세요", ro: "aiseu amerikano juseyo", zh: "請給我一杯冰美式", cat: "咖啡小吃" },
  { ko: "따뜻한 거로 주세요", ro: "ttatteutan georo juseyo", zh: "請給我熱的", cat: "咖啡小吃" },
  { ko: "사이즈 업 할 수 있어요", ro: "saijeu-eop hal su isseoyo", zh: "可以升級大杯嗎？", cat: "咖啡小吃" },
  { ko: "여기서 드세요", ro: "yeogiseo deuseyo", zh: "內用嗎？", cat: "咖啡小吃" },
  { ko: "떡볶이 하나 주세요", ro: "tteokbokki hana juseyo", zh: "請給我一份辣炒年糕", cat: "咖啡小吃" },
  { ko: "이거 얼마예요", ro: "igeo eolmayeyo", zh: "這個多少錢？", cat: "咖啡小吃" },
  { ko: "데워 드릴까요", ro: "dewo deurilkkayo", zh: "需要幫您加熱嗎？", cat: "咖啡小吃" },
  { ko: "이거 두 개 주세요", ro: "igeo du gae juseyo", zh: "請給我兩個這個", cat: "咖啡小吃" },

  // 購物與退稅
  { ko: "이거 있어요", ro: "igeo isseoyo", zh: "有這個嗎？", cat: "購物" },
  { ko: "다른 색 있어요", ro: "dareun saek isseoyo", zh: "有其他顏色嗎？", cat: "購物" },
  { ko: "이거 입어봐도 돼요", ro: "igeo ibeobwado dwaeyo", zh: "可以試穿這個嗎？", cat: "購物" },
  { ko: "카드 되나요", ro: "kadeu doenayo", zh: "可以刷卡嗎？", cat: "購物" },
  { ko: "현금만 돼요", ro: "hyeongeumman dwaeyo", zh: "只能付現", cat: "購物" },
  { ko: "좀 깎아 주세요", ro: "jom kkakka juseyo", zh: "請算便宜一點", cat: "購物" },
  { ko: "여권 보여주세요", ro: "yeogwon boyeojuseyo", zh: "請出示護照", cat: "購物" },
  { ko: "이거 세일 중이에요", ro: "igeo seil jungieyo", zh: "這個在特價中嗎？", cat: "購物" },
  { ko: "봉투 필요하세요", ro: "bongtu piryohaseyo", zh: "需要袋子嗎？", cat: "購物" },
  { ko: "다른 사이즈 있어요", ro: "dareun saijeu isseoyo", zh: "有其他尺寸嗎？", cat: "購物" },

  // 緊急狀況與求助
  { ko: "도와주세요", ro: "dowajuseyo", zh: "請幫幫我", cat: "緊急求助" },
  { ko: "아파요", ro: "apayo", zh: "我不舒服／我痛", cat: "緊急求助" },
  { ko: "병원이 어디예요", ro: "byeongwoni eodiyeyo", zh: "醫院在哪裡？", cat: "緊急求助" },
  { ko: "약국이 어디예요", ro: "yakgugi eodiyeyo", zh: "藥局在哪裡？", cat: "緊急求助" },
  { ko: "경찰을 불러 주세요", ro: "gyeongchareul bulleo juseyo", zh: "請幫我叫警察", cat: "緊急求助" },
  { ko: "여권을 잃어버렸어요", ro: "yeogwoneul ireobeoryeosseoyo", zh: "我的護照弄丟了", cat: "緊急求助" },
  { ko: "지갑을 잃어버렸어요", ro: "jigabeul ireobeoryeosseoyo", zh: "我的錢包弄丟了", cat: "緊急求助" },
  { ko: "알레르기가 있어요", ro: "allereugiga isseoyo", zh: "我有過敏", cat: "緊急求助" },

  // 日常閒聊與旅遊常用
  { ko: "이거 뭐예요", ro: "igeo mwoyeyo", zh: "這是什麼？", cat: "日常閒聊" },
  { ko: "사진 찍어도 돼요", ro: "sajin jjigeodo dwaeyo", zh: "可以拍照嗎？", cat: "日常閒聊" },
  { ko: "사진 좀 찍어 주세요", ro: "sajin jom jjigeo juseyo", zh: "可以幫我拍張照嗎？", cat: "日常閒聊" },
  { ko: "정말 예뻐요", ro: "jeongmal yeppeoyo", zh: "真的很漂亮", cat: "日常閒聊" },
  { ko: "정말 맛있어요", ro: "jeongmal masisseoyo", zh: "真的很好吃", cat: "日常閒聊" },
  { ko: "너무 좋아요", ro: "neomu joayo", zh: "太好了／我很喜歡", cat: "日常閒聊" },
  { ko: "잠깐만요", ro: "jamkkanmanyo", zh: "請稍等", cat: "日常閒聊" },
  { ko: "알겠어요", ro: "algesseoyo", zh: "我知道了", cat: "日常閒聊" },
  { ko: "다시 한 번 말해 주세요", ro: "dasi han beon malhae juseyo", zh: "請再說一次", cat: "日常閒聊" },
  { ko: "이거 어떻게 써요", ro: "igeo eotteoke sseoyo", zh: "這個怎麼用？", cat: "日常閒聊" },
  { ko: "오늘 날씨가 좋아요", ro: "oneul nalssiga joayo", zh: "今天天氣很好", cat: "日常閒聊" },
  { ko: "시간 있어요", ro: "sigan isseoyo", zh: "你有時間嗎？", cat: "日常閒聊" },
  { ko: "조금만 기다려 주세요", ro: "jogeumman gidaryeo juseyo", zh: "請稍微等一下", cat: "日常閒聊" },
  { ko: "화이팅", ro: "hwaiting", zh: "加油", cat: "日常閒聊" },
  { ko: "다음에 또 올게요", ro: "daeume tto olgeyo", zh: "我下次會再來", cat: "日常閒聊" },
  { ko: "안녕히 주무세요", ro: "annyeonghi jumuseyo", zh: "晚安", cat: "日常閒聊" }
];
