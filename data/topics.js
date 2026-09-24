// 網站的主題與課程資料。
// 之後要新增主題時，只要在 topics 陣列裡新增一個物件即可，首頁會自動顯示。
//
// 主題物件格式：
// {
//   id: "example-topic",          // 唯一代號
//   title: "主題標題",
//   description: "簡短說明",
//   icon: "📘",
//   url: "topics/example-topic/index.html", // 主題頁面路徑
//   resources: [                  // 選填：獨立參考頁（不算在課程編號裡，例如速查表）
//     { title: "常見和弦總覽", description: "簡短說明", icon: "🎼", url: "topics/example-topic/reference.html" }
//   ],
//   modules: [                    // 課程依模組分組
//     {
//       title: "模組名稱",
//       courses: [
//         // url 留空代表尚未發布內容，只會在主題頁顯示「敬請期待」
//         { title: "第一課：介紹", url: "topics/example-topic/lesson-01.html" },
//         { title: "第二課：進階" }
//       ]
//     }
//   ]
// }

window.SITE_DATA = {
  // 主題分類，決定首頁折疊區塊的顯示順序與標題。
  categories: [
    { id: "music", label: "音樂", icon: "🎵" },
    { id: "tech", label: "科技與工程", icon: "💻" },
    { id: "math", label: "數學", icon: "📐" },
    { id: "science", label: "物理與宇宙學", icon: "🔭" },
    { id: "nobel", label: "諾貝爾獎", icon: "🏅" },
    { id: "life", label: "生活與實用知識", icon: "🧭" },
    { id: "wuxia", label: "小說", icon: "🗡️" },
    { id: "fantasy", label: "奇幻文學與電影宇宙", icon: "📖" },
    { id: "anime", label: "動漫", icon: "🍥" },
    { id: "games", label: "電玩遊戲世界觀", icon: "🎮" },
    { id: "mythology", label: "神話與傳說", icon: "🏺" },
    { id: "history", label: "歷史", icon: "📜" }
  ],
  topics: [
    {
      id: "guitar",
      category: "music",
      title: "民謠吉他彈唱",
      description:
        "從基本功穩固開始，聚焦換和弦流暢度與節奏穩定度，逐步進階到大和弦、指彈與抓歌能力，目標是能自彈自唱任何一首歌。",
      icon: "🎸",
      url: "topics/guitar/index.html",
      resources: [
        {
          title: "歌曲",
          description: "歌曲和弦進行清單，點和弦可看指法圖（另開新頁）",
          icon: "🎵",
          url: "https://sheet.bstzeng.cc/guitar.html"
        },
        {
          title: "常見和弦總覽",
          description: "所有教過的和弦指法圖，一頁快速複習",
          icon: "🎼",
          url: "topics/guitar/chords.html"
        }
      ],
      modules: [
        {
          title: "模組 A｜基礎穩固",
          courses: [
            { title: "姿勢、握琴與左右手基本動作總複習", url: "topics/guitar/lesson-01.html" },
            { title: "調音與節奏感訓練（節拍器怎麼用）", url: "topics/guitar/lesson-02.html" },
            { title: "開放和弦總複習：C、G、D、Em、Am、Dm、A、E", url: "topics/guitar/lesson-03.html" },
            { title: "換和弦的「最短路徑」原則", url: "topics/guitar/lesson-04.html" },
            { title: "基礎八分音符刷弦型態（down-up down-up）", url: "topics/guitar/lesson-05.html" }
          ]
        },
        {
          title: "模組 B｜換和弦與節奏流暢度",
          courses: [
            { title: "為什麼換和弦會卡：常見錯誤診斷", url: "topics/guitar/lesson-06.html" },
            { title: "兩和弦循環練習法：節拍器漸進加速訓練", url: "topics/guitar/lesson-07.html" },
            { title: "常見和弦進行套路：C–G–Am–F 及其變化", url: "topics/guitar/lesson-08.html" },
            { title: "切分節奏與悶音（palm mute）", url: "topics/guitar/lesson-09.html" },
            { title: "四四拍常見刷弦型態大全（12 種型態圖解）", url: "topics/guitar/lesson-10.html" },
            { title: "搭配實際歌曲練習換和弦與節奏穩定度", url: "topics/guitar/lesson-11.html" }
          ]
        },
        {
          title: "模組 C｜移調夾與和弦進行邏輯",
          courses: [
            { title: "認識移調夾（capo）：原理與使用時機", url: "topics/guitar/lesson-12.html" },
            { title: "用 capo 簡化困難調性的歌曲", url: "topics/guitar/lesson-13.html" },
            { title: "常見調性與其和弦家族（C / G / D 大調）", url: "topics/guitar/lesson-14.html" },
            { title: "級數與羅馬數字記譜：I–IV–V–vi 進行", url: "topics/guitar/lesson-15.html" },
            { title: "用級數概念快速抓一首新歌的和弦", url: "topics/guitar/lesson-16.html" }
          ]
        },
        {
          title: "模組 D｜大和弦 Barre Chords",
          courses: [
            { title: "大和弦的手指力量與角度訓練", url: "topics/guitar/lesson-17.html" },
            { title: "F 大和弦與 Bm 大和弦", url: "topics/guitar/lesson-18.html" },
            { title: "移動大和弦：一個把位彈遍所有調性", url: "topics/guitar/lesson-19.html" },
            { title: "大和弦與開放和弦的混合彈奏策略", url: "topics/guitar/lesson-20.html" }
          ]
        },
        {
          title: "模組 E｜進階刷弦與指彈基礎",
          courses: [
            { title: "切音與強弱動態控制", url: "topics/guitar/lesson-21.html" },
            { title: "悶音刷弦（percussive strumming）", url: "topics/guitar/lesson-22.html" },
            { title: "指彈基礎：拇指與食中無名指分工（PIMA）", url: "topics/guitar/lesson-23.html" },
            { title: "簡單琶音型態", url: "topics/guitar/lesson-24.html" },
            { title: "民謠彈唱常見前奏／間奏套路", url: "topics/guitar/lesson-25.html" },
            { title: "加花：過門與轉折的簡單技巧", url: "topics/guitar/lesson-26.html" }
          ]
        },
        {
          title: "模組 F｜樂理與抓歌能力",
          courses: [
            { title: "大調音階與指板音名", url: "topics/guitar/lesson-27.html" },
            { title: "抓歌基本功：聽音高、聽和弦色彩", url: "topics/guitar/lesson-28.html" },
            { title: "用「順階和弦」推測沒聽過的歌怎麼配", url: "topics/guitar/lesson-29.html" },
            { title: "不用 capo 的移調：任意調性的和弦轉換", url: "topics/guitar/lesson-30.html" },
            { title: "常見歌曲曲式（主歌／副歌／過門）與編排概念", url: "topics/guitar/lesson-31.html" }
          ]
        },
        {
          title: "模組 G｜實戰彈唱",
          courses: [
            { title: "完整拆解一首簡單歌曲的和弦與節奏", url: "topics/guitar/lesson-32.html" },
            { title: "完整拆解一首中等難度歌曲（含大和弦或 capo）", url: "topics/guitar/lesson-33.html" },
            { title: "把學過的技巧套用到任何新歌的方法", url: "topics/guitar/lesson-34.html" },
            { title: "總結：診斷自己的弱點，規劃下一步", url: "topics/guitar/lesson-35.html" }
          ]
        }
      ]
    },
    {
      id: "ukulele",
      category: "music",
      title: "烏克麗麗",
      description: "還沒有課程，先收錄一頁完整的常見和弦查詢表（12 個調的大和弦、小和弦、屬七和弦）。",
      icon: "🎶",
      url: "topics/ukulele/index.html",
      resources: [
        {
          title: "歌曲",
          description: "歌曲和弦進行清單，點和弦可看指法圖（另開新頁）",
          icon: "🎵",
          url: "https://sheet.bstzeng.cc/ukulele.html"
        },
        {
          title: "常見和弦總覽",
          description: "12 個調的大和弦、小和弦、屬七和弦，共 36 個和弦指法圖",
          icon: "🎼",
          url: "topics/ukulele/chords.html"
        }
      ]
    },
    {
      id: "music-theory",
      category: "music",
      title: "創作樂理：從音程到寫出一首歌",
      description:
        "為想創作音樂的人設計的樂理課：和弦怎麼疊、進行怎麼走、旋律怎麼配和弦、一首歌怎麼從零寫出來。全站第一門「聽得到」的課——每個音程、和弦、音階、進行都可以直接點擊試聽，用耳朵驗證每一個概念。與民謠吉他主題互相銜接。",
      icon: "🎹",
      url: "topics/music-theory/index.html",
      modules: [
        {
          title: "模組 A｜音的原料：音名、音程與音階",
          courses: [
            { title: "十二平均律：為什麼一個八度切成 12 個半音", url: "topics/music-theory/lesson-01.html" },
            { title: "音程（上）：度數與半音的算法", url: "topics/music-theory/lesson-02.html" },
            { title: "音程（下）：大小完全增減與每種音程的聲音表情", url: "topics/music-theory/lesson-03.html" },
            { title: "大調音階的構造：全全半全全全半", url: "topics/music-theory/lesson-04.html" },
            { title: "小調音階三兄弟：自然、和聲、旋律小調", url: "topics/music-theory/lesson-05.html" }
          ]
        },
        {
          title: "模組 B｜調性的地圖：五度圈",
          courses: [
            { title: "調號與五度圈：12 個大調的完整地圖", url: "topics/music-theory/lesson-06.html" },
            { title: "關係大小調與平行大小調：一張調號、兩種心情", url: "topics/music-theory/lesson-07.html" },
            { title: "五度圈的實用功能：和弦親疏、轉調距離一眼看出", url: "topics/music-theory/lesson-08.html" },
            { title: "模組總結：聽出一首歌在什麼調——主音引力", url: "topics/music-theory/lesson-09.html" }
          ]
        },
        {
          title: "模組 C｜和弦的構造",
          courses: [
            { title: "三和弦：大、小、增、減的堆疊邏輯", url: "topics/music-theory/lesson-10.html" },
            { title: "大調順階和弦：I ii iii IV V vi vii° 的完整推導", url: "topics/music-theory/lesson-11.html" },
            { title: "小調順階和弦：為什麼小調的 V 常常「借」大三度", url: "topics/music-theory/lesson-12.html" },
            { title: "七和弦：maj7、7、m7、m7♭5 的構造與色彩", url: "topics/music-theory/lesson-13.html" },
            { title: "轉位與斜線和弦：同一個和弦的不同重心", url: "topics/music-theory/lesson-14.html" }
          ]
        },
        {
          title: "模組 D｜和聲進行的邏輯",
          courses: [
            { title: "和弦功能：主—下屬—屬，緊張與解決的引擎", url: "topics/music-theory/lesson-15.html" },
            { title: "終止式：樂句怎麼收尾——正格、變格、假終止、半終止", url: "topics/music-theory/lesson-16.html" },
            { title: "經典套路解剖（一）：I–V–vi–IV 與卡農進行", url: "topics/music-theory/lesson-17.html" },
            { title: "經典套路解剖（二）：低音下行、12 小節藍調、小調套路", url: "topics/music-theory/lesson-18.html" },
            { title: "和聲節奏：一小節換幾個和弦，決定歌的步伐", url: "topics/music-theory/lesson-19.html" },
            { title: "模組總結：完整拆解三首經典歌的和聲骨架", url: "topics/music-theory/lesson-20.html" }
          ]
        },
        {
          title: "模組 E｜替旋律配和弦",
          courses: [
            { title: "旋律與和弦的關係：和弦內音與非和弦音", url: "topics/music-theory/lesson-21.html" },
            { title: "配和弦的完整流程：定調、找重拍音、選功能、試聽修正", url: "topics/music-theory/lesson-22.html" },
            { title: "同一段旋律的多種配法：重配和聲入門", url: "topics/music-theory/lesson-23.html" },
            { title: "經過音、掛留音、倚音：讓旋律離開和弦也好聽", url: "topics/music-theory/lesson-24.html" },
            { title: "旋律寫作：動機、重複與變化的平衡", url: "topics/music-theory/lesson-25.html" },
            { title: "實作課：從零開始替一段旋律完整配好和弦", url: "topics/music-theory/lesson-26.html" }
          ]
        },
        {
          title: "模組 F｜色彩與進階和聲",
          courses: [
            { title: "副屬和弦（V/x）：向別的調借屬和弦", url: "topics/music-theory/lesson-27.html" },
            { title: "借用和弦：從小調借來的 ♭VII、♭VI、iv", url: "topics/music-theory/lesson-28.html" },
            { title: "sus2、sus4、add9：懸浮與加味", url: "topics/music-theory/lesson-29.html" },
            { title: "延伸和弦：9、11、13 的爵士色盤", url: "topics/music-theory/lesson-30.html" },
            { title: "轉調技巧：共同和弦轉調、直接轉調、副歌升 key", url: "topics/music-theory/lesson-31.html" },
            { title: "調式（modes）：Dorian、Mixolydian 的色彩與流行應用", url: "topics/music-theory/lesson-32.html" },
            { title: "模組總結：進階和聲的品味地圖", url: "topics/music-theory/lesson-33.html" }
          ]
        },
        {
          title: "模組 G｜節奏、曲式與編曲",
          courses: [
            { title: "歌曲曲式：主歌、副歌、橋段的功能與能量曲線", url: "topics/music-theory/lesson-34.html" },
            { title: "律動（groove）：同一組和弦，節奏一改歌就變了", url: "topics/music-theory/lesson-35.html" },
            { title: "編曲分層思維：節奏組、和聲組、旋律組、填充", url: "topics/music-theory/lesson-36.html" },
            { title: "前奏、間奏、尾奏的寫法", url: "topics/music-theory/lesson-37.html" },
            { title: "動態與留白：編曲最常被忽略的維度", url: "topics/music-theory/lesson-38.html" }
          ]
        },
        {
          title: "模組 H｜創作實戰",
          courses: [
            { title: "從和弦進行開始寫歌：完整流程示範", url: "topics/music-theory/lesson-39.html" },
            { title: "從旋律開始寫歌：完整流程示範", url: "topics/music-theory/lesson-40.html" },
            { title: "歌詞與旋律的咬合：斷句、重音與中文聲調", url: "topics/music-theory/lesson-41.html" },
            { title: "課程總結：建立你自己的創作工作流程與檢查清單", url: "topics/music-theory/lesson-42.html" }
          ]
        }
      ]
    },
    {
      id: "electromagnetism",
      category: "science",
      title: "電磁學：從琥珀到馬克士威方程組",
      description:
        "相對論的前傳。從古希臘的琥珀與磁石、富蘭克林的風箏，到庫侖的扭秤、法拉第的力線與馬克士威的統一，完整走過電與磁從奇聞軼事變成古典物理最完美理論大廈的歷程。附完整數學推導（含向量微積分工具箱）與圖解，終點停在以太之謎，銜接相對論主題第 1 課。",
      icon: "⚡",
      url: "topics/electromagnetism/index.html",
      modules: [
        {
          title: "模組 A｜靜電的兩千年：從琥珀到富蘭克林",
          courses: [
            { title: "琥珀與磁石：古希臘的觀察到吉爾伯特的《論磁石》", url: "topics/electromagnetism/lesson-01.html" },
            { title: "電的兩種型態：杜費的雙流體說與富蘭克林的電荷守恆", url: "topics/electromagnetism/lesson-02.html" },
            { title: "萊頓瓶：電第一次被「儲存」起來", url: "topics/electromagnetism/lesson-03.html" },
            { title: "富蘭克林的風箏：天上的雷電與地上的靜電是同一件事", url: "topics/electromagnetism/lesson-04.html" }
          ]
        },
        {
          title: "模組 B｜定量化與數學工具箱",
          courses: [
            { title: "庫侖的扭秤實驗：完整驗證平方反比定律", url: "topics/electromagnetism/lesson-05.html" },
            { title: "純量場與向量場：梯度的完整推導", url: "topics/electromagnetism/lesson-06.html" },
            { title: "通量與散度：完整推導散度定理", url: "topics/electromagnetism/lesson-07.html" },
            { title: "環流與旋度：完整推導斯托克斯定理", url: "topics/electromagnetism/lesson-08.html" },
            { title: "平方反比的深意：與牛頓重力的完整對照", url: "topics/electromagnetism/lesson-09.html" },
            { title: "模組總結：為什麼電磁學需要一套新的數學語言", url: "topics/electromagnetism/lesson-10.html" }
          ]
        },
        {
          title: "模組 C｜靜電場論",
          courses: [
            { title: "「場」的誕生：法拉第的力線與超距作用之爭", url: "topics/electromagnetism/lesson-11.html" },
            { title: "完整推導高斯定律，以及它與庫侖定律的等價性", url: "topics/electromagnetism/lesson-12.html" },
            { title: "電位：完整推導能量與電位的關係", url: "topics/electromagnetism/lesson-13.html" },
            { title: "導體與電容：完整計算幾種經典幾何", url: "topics/electromagnetism/lesson-14.html" },
            { title: "模組總結：靜電學的完成與它還不能回答的問題", url: "topics/electromagnetism/lesson-15.html" }
          ]
        },
        {
          title: "模組 D｜電流：從青蛙腿到電路定律",
          courses: [
            { title: "伽伐尼與伏打：「動物電」之爭與電池的發明", url: "topics/electromagnetism/lesson-16.html" },
            { title: "歐姆定律：完整推導與歐姆生前被冷落的歷史", url: "topics/electromagnetism/lesson-17.html" },
            { title: "克希荷夫電路定律：光譜學那位克希荷夫的另一項成就", url: "topics/electromagnetism/lesson-18.html" },
            { title: "焦耳熱：完整推導電能與熱的轉換", url: "topics/electromagnetism/lesson-19.html" }
          ]
        },
        {
          title: "模組 E｜靜磁學：電與磁的第一次牽手",
          courses: [
            { title: "厄斯特 1820：一堂課上的意外——電流讓磁針偏轉", url: "topics/electromagnetism/lesson-20.html" },
            { title: "必歐—沙伐定律：完整推導經典電流組態的磁場", url: "topics/electromagnetism/lesson-21.html" },
            { title: "完整推導安培定律", url: "topics/electromagnetism/lesson-22.html" },
            { title: "磁場沒有源頭：磁單極之謎", url: "topics/electromagnetism/lesson-23.html" },
            { title: "勞侖茲力：完整推導帶電粒子在電磁場中的運動", url: "topics/electromagnetism/lesson-24.html" }
          ]
        },
        {
          title: "模組 F｜電磁感應：法拉第的革命",
          courses: [
            { title: "法拉第 1831：磁生電的十年執念", url: "topics/electromagnetism/lesson-25.html" },
            { title: "完整推導法拉第定律與冷次定律", url: "topics/electromagnetism/lesson-26.html" },
            { title: "發電機與馬達：改變世界的應用", url: "topics/electromagnetism/lesson-27.html" },
            { title: "自感與互感：完整推導", url: "topics/electromagnetism/lesson-28.html" },
            { title: "模組總結：對稱性的暗示——電生磁、磁生電，還缺什麼？", url: "topics/electromagnetism/lesson-29.html" }
          ]
        },
        {
          title: "模組 G｜馬克士威的統一",
          courses: [
            { title: "安培定律的矛盾：完整推導電荷守恆如何逼出位移電流", url: "topics/electromagnetism/lesson-30.html" },
            { title: "馬克士威方程組：四條方程式的完整整理", url: "topics/electromagnetism/lesson-31.html" },
            { title: "完整推導電磁波動方程式：光速從純電磁常數中浮現", url: "topics/electromagnetism/lesson-32.html" },
            { title: "光就是電磁波：史上最偉大的統一之一", url: "topics/electromagnetism/lesson-33.html" },
            { title: "赫茲 1887：完整驗證電磁波的存在", url: "topics/electromagnetism/lesson-34.html" },
            { title: "完整推導坡印廷向量與輻射壓", url: "topics/electromagnetism/lesson-35.html" },
            { title: "模組總結：古典物理最完美的理論大廈", url: "topics/electromagnetism/lesson-36.html" }
          ]
        },
        {
          title: "模組 H｜裂縫與門檻：以太問題",
          courses: [
            { title: "波需要介質？以太假說的必然與尷尬", url: "topics/electromagnetism/lesson-37.html" },
            { title: "完整推導邁克生—莫立實驗的預期結果", url: "topics/electromagnetism/lesson-38.html" },
            { title: "零結果：物理史上最著名的「失敗」實驗", url: "topics/electromagnetism/lesson-39.html" },
            { title: "課程總結：1905 年的門檻——故事在相對論主題第 1 課繼續", url: "topics/electromagnetism/lesson-40.html" }
          ]
        }
      ]
    },
    {
      id: "relativity",
      category: "science",
      title: "廣義相對論：從等效原理到愛因斯坦場方程式",
      description:
        "自學課程。從狹義相對論出發，建立張量與微分幾何工具，推導愛因斯坦場方程式，並學習如何求解與應用於黑洞、宇宙學、重力波等問題。",
      icon: "🌌",
      url: "topics/relativity/index.html",
      modules: [
        {
          title: "模組 A｜狹義相對論暖身",
          courses: [
            { title: "為什麼需要新理論：牛頓重力與光速不變性的衝突", url: "topics/relativity/lesson-01.html" },
            { title: "狹義相對論公設與勞侖茲變換", url: "topics/relativity/lesson-02.html" },
            { title: "時空圖、同時性的相對性、時間膨脹與長度收縮", url: "topics/relativity/lesson-03.html" },
            { title: "四維向量與閔可夫斯基度規、不變區間", url: "topics/relativity/lesson-04.html" },
            { title: "相對論性能量動量、四維速度與四維加速度", url: "topics/relativity/lesson-05.html" }
          ]
        },
        {
          title: "模組 B｜數學基礎：張量分析與微分幾何",
          courses: [
            { title: "向量與對偶向量、指標記號與愛因斯坦求和約定", url: "topics/relativity/lesson-06.html" },
            { title: "座標變換與張量的嚴格定義", url: "topics/relativity/lesson-07.html" },
            { title: "度規張量、指標的升降", url: "topics/relativity/lesson-08.html" },
            { title: "流形是什麼：微分幾何的基本語言", url: "topics/relativity/lesson-09.html" },
            { title: "切空間、基底向量與座標卡", url: "topics/relativity/lesson-10.html" },
            { title: "協變導數與克里斯托費爾符號", url: "topics/relativity/lesson-11.html" },
            { title: "平行移動與測地線", url: "topics/relativity/lesson-12.html" },
            { title: "黎曼曲率張量：定義與幾何意義", url: "topics/relativity/lesson-13.html" },
            { title: "里奇張量、里奇純量、比安基恆等式", url: "topics/relativity/lesson-14.html" },
            { title: "愛因斯坦張量與它為何「散度為零」", url: "topics/relativity/lesson-15.html" }
          ]
        },
        {
          title: "模組 C｜廣義相對論的物理",
          courses: [
            { title: "等效原理（弱等效原理與強等效原理）", url: "topics/relativity/lesson-16.html" },
            { title: "測地線方程：重力如何變成「自由落體沿測地線走」", url: "topics/relativity/lesson-17.html" },
            { title: "牛頓極限：如何從 GR 還原出牛頓重力", url: "topics/relativity/lesson-18.html" },
            { title: "應力-能量張量：如何描述物質與能量的分布", url: "topics/relativity/lesson-19.html" },
            { title: "GR 中的守恆律", url: "topics/relativity/lesson-20.html" },
            { title: "愛因斯坦場方程式的推導與物理動機", url: "topics/relativity/lesson-21.html" },
            { title: "宇宙常數與真空場方程式", url: "topics/relativity/lesson-22.html" },
            { title: "線性化場方程式與量綱檢查", url: "topics/relativity/lesson-23.html" }
          ]
        },
        {
          title: "模組 D｜精確解與求解技巧",
          courses: [
            { title: "利用對稱性簡化 EFE：基靈向量", url: "topics/relativity/lesson-24.html" },
            { title: "Schwarzschild 解的推導", url: "topics/relativity/lesson-25.html" },
            { title: "Schwarzschild 幾何：視界與奇異點", url: "topics/relativity/lesson-26.html" },
            { title: "Schwarzschild 時空中的測地線：軌道與水星近日點進動", url: "topics/relativity/lesson-27.html" },
            { title: "光線偏折、重力透鏡、Shapiro 延遲", url: "topics/relativity/lesson-28.html" },
            { title: "Reissner–Nordström 與 Kerr 解概覽", url: "topics/relativity/lesson-29.html" },
            { title: "黑洞熱力學初探", url: "topics/relativity/lesson-30.html" },
            { title: "FRW 度規：宇宙學的時空設定", url: "topics/relativity/lesson-31.html" },
            { title: "Friedmann 方程式", url: "topics/relativity/lesson-32.html" },
            { title: "宇宙學模型：物質／輻射／暗能量主導的宇宙", url: "topics/relativity/lesson-33.html" }
          ]
        },
        {
          title: "模組 E｜現代應用與延伸",
          courses: [
            { title: "線性化重力與重力波的推導", url: "topics/relativity/lesson-34.html" },
            { title: "重力波偵測（LIGO）：物理量如何對應觀測訊號", url: "topics/relativity/lesson-35.html" },
            { title: "GPS 的相對論修正：GR 在日常科技中的實際應用", url: "topics/relativity/lesson-36.html" },
            { title: "數值相對論概覽：EFE 如何在電腦上被解", url: "topics/relativity/lesson-37.html" },
            { title: "微擾方法與後牛頓近似", url: "topics/relativity/lesson-38.html" },
            { title: "ADM 形式（初值問題）簡介", url: "topics/relativity/lesson-39.html" },
            { title: "總結課：完整重走一遍 EFE 推導 + 開放問題", url: "topics/relativity/lesson-40.html" }
          ]
        }
      ]
    },
    {
      id: "atomism",
      category: "science",
      title: "原子論：從德謨克利特到量子革命前夕",
      description:
        "標準模型的前傳。從古希臘的原子臆測、道爾頓的化學原子論、氣體動力論與布朗運動的決定性證據，到週期表、光譜學與黑體輻射危機，完整走過原子從哲學概念變成科學事實的兩千四百年。附完整數學推導與圖解，終點銜接標準模型主題第 1 課。",
      icon: "⚗️",
      url: "topics/atomism/index.html",
      modules: [
        {
          title: "模組 A｜古代原子論的哲學根源",
          courses: [
            { title: "德謨克利特與留基伯：虛空與不可分割的原子", url: "topics/atomism/lesson-01.html" },
            { title: "伊比鳩魯與盧克萊修：《物性論》與原子論的古羅馬傳承", url: "topics/atomism/lesson-02.html" },
            { title: "亞里斯多德的連續體理論：原子論為何沉寂近兩千年", url: "topics/atomism/lesson-03.html" },
            { title: "十七世紀的復興：伽森狄與波以耳的機械哲學", url: "topics/atomism/lesson-04.html" },
            { title: "完整推導波以耳定律：第一個關於「看不見的粒子」的定量證據", url: "topics/atomism/lesson-05.html" }
          ]
        },
        {
          title: "模組 B｜化學原子論的誕生",
          courses: [
            { title: "拉瓦節與質量守恆定律：化學定量革命的起點", url: "topics/atomism/lesson-06.html" },
            { title: "定比定律：普魯斯特與貝托雷之爭", url: "topics/atomism/lesson-07.html" },
            { title: "完整推導倍比定律：道爾頓從化學數據中看見的規律", url: "topics/atomism/lesson-08.html" },
            { title: "道爾頓原子論：1803 年的五條公設", url: "topics/atomism/lesson-09.html" },
            { title: "給呂薩克氣體化合體積定律與道爾頓理論的矛盾", url: "topics/atomism/lesson-10.html" },
            { title: "亞佛加厥假說：分子概念如何解開氣體體積之謎", url: "topics/atomism/lesson-11.html" }
          ]
        },
        {
          title: "模組 C｜原子論的物理證據：氣體動力論與布朗運動",
          courses: [
            { title: "完整推導理想氣體狀態方程式：從微觀碰撞模型出發", url: "topics/atomism/lesson-12.html" },
            { title: "馬克士威—波茲曼分布：氣體分子的速度統計", url: "topics/atomism/lesson-13.html" },
            { title: "完整推導平均自由徑：分子大小與亞佛加厥常數的第一次估計", url: "topics/atomism/lesson-14.html" },
            { title: "布朗運動之謎：花粉為什麼會不停地抖動", url: "topics/atomism/lesson-15.html" },
            { title: "愛因斯坦的布朗運動理論：完整推導擴散係數與愛因斯坦關係式", url: "topics/atomism/lesson-16.html" },
            { title: "佩蘭的決定性實驗：原子論從假說變成事實", url: "topics/atomism/lesson-17.html" },
            { title: "模組總結：懷疑論者最終的讓步", url: "topics/atomism/lesson-18.html" }
          ]
        },
        {
          title: "模組 D｜元素的系統化：週期表",
          courses: [
            { title: "從煉金術到化學：元素概念的演化", url: "topics/atomism/lesson-19.html" },
            { title: "德貝萊納的三元素組與紐蘭茲的八音律", url: "topics/atomism/lesson-20.html" },
            { title: "門得列夫的週期表：鎵、鍺、鈧的預言與發現", url: "topics/atomism/lesson-21.html" },
            { title: "週期表為什麼「有效」：一個當時無人能回答的問題", url: "topics/atomism/lesson-22.html" }
          ]
        },
        {
          title: "模組 E｜光譜學：原子內部結構的第一道線索",
          courses: [
            { title: "夫朗和斐譜線與克希荷夫—本生的光譜分析", url: "topics/atomism/lesson-23.html" },
            { title: "用光譜發現新元素：氦如何先在太陽上被找到", url: "topics/atomism/lesson-24.html" },
            { title: "巴耳末公式的發現：氫原子光譜的神祕規律", url: "topics/atomism/lesson-25.html" },
            { title: "芮得柏公式的推廣：純粹經驗卻精確得驚人的公式", url: "topics/atomism/lesson-26.html" },
            { title: "模組總結：沒有人知道為什麼這個公式會成立", url: "topics/atomism/lesson-27.html" }
          ]
        },
        {
          title: "模組 F｜古典物理的極限：黑體輻射危機",
          courses: [
            { title: "熱輻射的古典理論：史特凡—波茲曼與維恩位移定律回顧", url: "topics/atomism/lesson-28.html" },
            { title: "完整推導空腔內電磁波模式的計數", url: "topics/atomism/lesson-29.html" },
            { title: "完整推導雷立—金斯公式與紫外災變", url: "topics/atomism/lesson-30.html" },
            { title: "蒲朗克的孤注一擲：量子化假設如何解決紫外災變", url: "topics/atomism/lesson-31.html" },
            { title: "完整推導蒲朗克公式的兩個極限：還原維恩與雷立—金斯", url: "topics/atomism/lesson-32.html" },
            { title: "模組總結：一個沒人理解物理意義的數學技巧", url: "topics/atomism/lesson-33.html" }
          ]
        },
        {
          title: "模組 G｜放射性的發現：通往新世界的最後一步",
          courses: [
            { title: "侖琴發現 X 射線：意外的開端", url: "topics/atomism/lesson-34.html" },
            { title: "貝克勒的意外發現：鈾鹽的神祕輻射", url: "topics/atomism/lesson-35.html" },
            { title: "居禮夫婦：釙與鐳的分離與能量之謎", url: "topics/atomism/lesson-36.html" },
            { title: "課程總結：1896 年的門檻——故事在標準模型第 1 課繼續", url: "topics/atomism/lesson-37.html" }
          ]
        }
      ]
    },
    {
      id: "standard-model",
      category: "science",
      title: "標準模型：從量子場論到希格斯機制",
      description:
        "從量子力學與相對論出發，建立量子場論、群論與規範對稱的工具箱，完整推導電弱統一、希格斯機制與量子色動力學，並系統整理所有基本粒子的性質、歷史發現過程與尚未解決的問題。附完整數學推導，不省略證明過程。",
      icon: "⚛️",
      url: "topics/standard-model/index.html",
      modules: [
        {
          title: "模組 A｜歷史與物理圖像",
          courses: [
            { title: "從原子到基本粒子：電子、質子、中子的發現", url: "topics/standard-model/lesson-01.html" },
            { title: "宇宙射線與奇異粒子：緲子、介子、K 介子的意外發現", url: "topics/standard-model/lesson-02.html" },
            { title: "加速器年代與粒子動物園：共振態大爆發", url: "topics/standard-model/lesson-03.html" },
            { title: "夸克模型的誕生：Gell-Mann、Zweig 與八重道", url: "topics/standard-model/lesson-04.html" },
            { title: "標準模型拼圖完成：中性流、W/Z 玻色子到希格斯玻色子", url: "topics/standard-model/lesson-05.html" }
          ]
        },
        {
          title: "模組 B｜怎麼探測與確認一個粒子",
          courses: [
            { title: "對撞機物理基礎：截面、亮度與事件率", url: "topics/standard-model/lesson-06.html" },
            { title: "粒子偵測器：徑跡室、量能器、緲子室的原理", url: "topics/standard-model/lesson-07.html" },
            { title: "從撞擊數據到發現：統計顯著性與五個標準差", url: "topics/standard-model/lesson-08.html" },
            { title: "案例研究：J/ψ 粒子與「十一月革命」", url: "topics/standard-model/lesson-09.html" }
          ]
        },
        {
          title: "模組 C｜量子力學基礎回顧與擴充",
          courses: [
            { title: "波函數、算符與測量公設的系統整理", url: "topics/standard-model/lesson-10.html" },
            { title: "角動量與自旋：完整推導升降算符與本徵值", url: "topics/standard-model/lesson-11.html" },
            { title: "全同粒子：波色子、費米子與包立不相容原理的量子起源", url: "topics/standard-model/lesson-12.html" },
            { title: "微擾理論與費米黃金定則：躍遷機率怎麼算", url: "topics/standard-model/lesson-13.html" }
          ]
        },
        {
          title: "模組 D｜狹義相對論與相對論性量子力學",
          courses: [
            { title: "四維時空與勞倫茲協變記號回顧", url: "topics/standard-model/lesson-14.html" },
            { title: "Klein–Gordon 方程式：把薛丁格方程式相對論化", url: "topics/standard-model/lesson-15.html" },
            { title: "負機率問題與 Dirac 的洞見", url: "topics/standard-model/lesson-16.html" },
            { title: "完整推導 Dirac 方程式", url: "topics/standard-model/lesson-17.html" },
            { title: "Dirac 方程式的解：自旋、反粒子與正電子的預言", url: "topics/standard-model/lesson-18.html" },
            { title: "從 Dirac 海到量子場論的過渡", url: "topics/standard-model/lesson-19.html" }
          ]
        },
        {
          title: "模組 E｜量子場論入門",
          courses: [
            { title: "為什麼粒子數必須能改變：從量子力學到量子場論", url: "topics/standard-model/lesson-20.html" },
            { title: "正則量子化：純量場的完整推導", url: "topics/standard-model/lesson-21.html" },
            { title: "費曼傳播子與微擾展開", url: "topics/standard-model/lesson-22.html" },
            { title: "費曼圖規則：公式怎麼畫成圖", url: "topics/standard-model/lesson-23.html" },
            { title: "S 矩陣與散射截面：連結理論與可觀測量", url: "topics/standard-model/lesson-24.html" }
          ]
        },
        {
          title: "模組 F｜群論與規範場論工具箱",
          courses: [
            { title: "群、表示與生成元：從轉動群 SO(3) 建立直覺", url: "topics/standard-model/lesson-25.html" },
            { title: "SU(2) 的表示論：從自旋到弱同位旋", url: "topics/standard-model/lesson-26.html" },
            { title: "SU(3) 的表示論：八重道的數學結構", url: "topics/standard-model/lesson-27.html" },
            { title: "Yang-Mills 規範場論總論：非阿貝爾規範場強張量的完整推導", url: "topics/standard-model/lesson-28.html" }
          ]
        },
        {
          title: "模組 G｜規範對稱與量子電動力學（QED）",
          courses: [
            { title: "諾特定理完整推導：對稱與守恆律", url: "topics/standard-model/lesson-29.html" },
            { title: "局域規範不變性：U(1) 對稱如何「生出」光子", url: "topics/standard-model/lesson-30.html" },
            { title: "QED 的拉格朗日量與費曼規則", url: "topics/standard-model/lesson-31.html" },
            { title: "電子異常磁矩：QED 最精確的預言", url: "topics/standard-model/lesson-32.html" },
            { title: "重整化初步：無窮大是怎麼被馴服的", url: "topics/standard-model/lesson-33.html" },
            { title: "重整化群方程式：耦合常數為什麼會「跑」", url: "topics/standard-model/lesson-34.html" }
          ]
        },
        {
          title: "模組 H｜弱交互作用與電弱統一",
          courses: [
            { title: "貝他衰變與費米的接觸作用理論", url: "topics/standard-model/lesson-35.html" },
            { title: "宇稱不守恆：吳健雄實驗與 V−A 理論", url: "topics/standard-model/lesson-36.html" },
            { title: "電荷共軛、時間反轉與 CPT 定理", url: "topics/standard-model/lesson-37.html" },
            { title: "中性流的預言與發現", url: "topics/standard-model/lesson-38.html" },
            { title: "SU(2)×U(1) 規範群：電弱統一的數學結構", url: "topics/standard-model/lesson-39.html" },
            { title: "W、Z 玻色子的質量問題：為什麼不能直接寫進拉格朗日量", url: "topics/standard-model/lesson-40.html" }
          ]
        },
        {
          title: "模組 I｜希格斯機制",
          courses: [
            { title: "WW 散射的么正性問題：為什麼希格斯是必要的", url: "topics/standard-model/lesson-41.html" },
            { title: "自發對稱破缺：墨西哥帽位能完整推導", url: "topics/standard-model/lesson-42.html" },
            { title: "Goldstone 定理與希格斯機制完整推導", url: "topics/standard-model/lesson-43.html" },
            { title: "規範玻色子如何「吃掉」Goldstone 玻色子獲得質量", url: "topics/standard-model/lesson-44.html" },
            { title: "費米子質量：湯川耦合", url: "topics/standard-model/lesson-45.html" },
            { title: "希格斯玻色子的發現：LHC 與 2012 年 7 月 4 日", url: "topics/standard-model/lesson-46.html" }
          ]
        },
        {
          title: "模組 J｜強交互作用與 QCD",
          courses: [
            { title: "夸克模型與八重道：SU(3) 味對稱", url: "topics/standard-model/lesson-47.html" },
            { title: "顏色電荷的發現：為什麼需要三種「顏色」", url: "topics/standard-model/lesson-48.html" },
            { title: "QCD 的規範結構：SU(3) 色對稱", url: "topics/standard-model/lesson-49.html" },
            { title: "漸近自由與夸克禁閉", url: "topics/standard-model/lesson-50.html" },
            { title: "強子動物園：介子、重子與夸克組成", url: "topics/standard-model/lesson-51.html" },
            { title: "夸克模型的定量驗證：重子磁矩與 Gell-Mann–Okubo 質量公式", url: "topics/standard-model/lesson-52.html" }
          ]
        },
        {
          title: "模組 K｜粒子分類總覽與味物理",
          courses: [
            { title: "標準模型粒子總表：三代費米子與規範玻色子", url: "topics/standard-model/lesson-53.html" },
            { title: "味的混合：CKM 矩陣與 CP 破壞", url: "topics/standard-model/lesson-54.html" },
            { title: "微中子振盪：標準模型之外第一個確定的證據", url: "topics/standard-model/lesson-55.html" },
            { title: "微中子質量之謎：Dirac 或 Majorana？翹翹板機制", url: "topics/standard-model/lesson-56.html" },
            { title: "標準模型拉格朗日總集成：把所有拼圖擺在一起", url: "topics/standard-model/lesson-57.html" }
          ]
        },
        {
          title: "模組 L｜超越標準模型",
          courses: [
            { title: "標準模型的未解之謎：階層問題、物質－反物質不對稱、暗物質", url: "topics/standard-model/lesson-58.html" },
            { title: "大一統理論展望：耦合常數的匯聚與超對稱簡介", url: "topics/standard-model/lesson-59.html" }
          ]
        }
      ]
    },
    {
      id: "astronomy",
      category: "science",
      title: "太空探索：恆星觀測到宇宙學",
      description:
        "從望遠鏡觀測原理、恆星物理量（距離、大小、質量、溫度）怎麼測，到星系、深空天體，最後是主流的宇宙形成假說。附完整數學推導，不省略證明過程。",
      icon: "🔭",
      url: "topics/astronomy/index.html",
      modules: [
        {
          title: "模組 A｜觀測基礎：我們怎麼「看」宇宙",
          courses: [
            { title: "電磁波譜與人類觀測宇宙的極限", url: "topics/astronomy/lesson-01.html" },
            { title: "望遠鏡技術：從光學到全波段天文學", url: "topics/astronomy/lesson-02.html" },
            { title: "星等系統：視星等與絕對星等", url: "topics/astronomy/lesson-03.html" },
            { title: "光譜學基礎：吸收線、發射線在說什麼", url: "topics/astronomy/lesson-04.html" },
            { title: "測光與濾鏡：顏色指數與觀測資料怎麼來的", url: "topics/astronomy/lesson-05.html" }
          ]
        },
        {
          title: "模組 B｜恆星的物理量怎麼測",
          courses: [
            { title: "視差法：最直接的幾何距離測量", url: "topics/astronomy/lesson-06.html" },
            { title: "光度、溫度與史特凡－波茲曼定律", url: "topics/astronomy/lesson-07.html" },
            { title: "維恩定律與黑體輻射：從顏色推溫度", url: "topics/astronomy/lesson-08.html" },
            { title: "恆星光譜分類（OBAFGKM）與 HR 圖", url: "topics/astronomy/lesson-09.html" },
            { title: "分光視差法：用光譜類型推距離", url: "topics/astronomy/lesson-10.html" },
            { title: "造父變星：標準燭光與週光關係", url: "topics/astronomy/lesson-11.html" },
            { title: "雙星系統：用克卜勒定律測恆星質量", url: "topics/astronomy/lesson-12.html" },
            { title: "距離階梯：從視差到哈伯定律的完整測距鏈", url: "topics/astronomy/lesson-13.html" }
          ]
        },
        {
          title: "模組 C｜恆星的一生",
          courses: [
            { title: "恆星誕生：分子雲與重力塌縮", url: "topics/astronomy/lesson-14.html" },
            { title: "主序星：氫融合與質光關係", url: "topics/astronomy/lesson-15.html" },
            { title: "紅巨星階段與氦閃", url: "topics/astronomy/lesson-16.html" },
            { title: "恆星之死：白矮星與錢卓塞卡極限", url: "topics/astronomy/lesson-17.html" },
            { title: "超新星爆炸、中子星與黑洞的形成", url: "topics/astronomy/lesson-18.html" },
            { title: "核合成：宇宙中的元素從哪裡來", url: "topics/astronomy/lesson-19.html" }
          ]
        },
        {
          title: "模組 D｜星系與大尺度結構",
          courses: [
            { title: "銀河系的結構與我們的位置", url: "topics/astronomy/lesson-20.html" },
            { title: "星系分類：哈伯音叉圖", url: "topics/astronomy/lesson-21.html" },
            { title: "星系自轉曲線：暗物質最早的證據", url: "topics/astronomy/lesson-22.html" },
            { title: "星系團、超星系團與宇宙網", url: "topics/astronomy/lesson-23.html" },
            { title: "活躍星系核與超大質量黑洞", url: "topics/astronomy/lesson-24.html" },
            { title: "重力透鏡：用廣義相對論繪製暗物質地圖", url: "topics/astronomy/lesson-25.html" }
          ]
        },
        {
          title: "模組 E｜深空與極端天體",
          courses: [
            { title: "深空長曝光：哈伯深空與時間回溯", url: "topics/astronomy/lesson-26.html" },
            { title: "中子星、脈衝星與磁星", url: "topics/astronomy/lesson-27.html" },
            { title: "黑洞的觀測證據：吸積盤到事件視界望遠鏡", url: "topics/astronomy/lesson-28.html" },
            { title: "重力波天文學：聽見宇宙的碰撞", url: "topics/astronomy/lesson-29.html" },
            { title: "系外行星：凌日法與徑向速度法", url: "topics/astronomy/lesson-30.html" },
            { title: "多信使天文學：整合光、重力波與微中子", url: "topics/astronomy/lesson-31.html" }
          ]
        },
        {
          title: "模組 F｜宇宙學：主流的宇宙形成假說",
          courses: [
            { title: "奧伯斯悖論：為什麼夜空是黑的", url: "topics/astronomy/lesson-32.html" },
            { title: "哈伯定律與宇宙膨脹的發現", url: "topics/astronomy/lesson-33.html" },
            { title: "大霹靂理論：時間線與三大關鍵證據", url: "topics/astronomy/lesson-34.html" },
            { title: "宇宙微波背景輻射：宇宙的嬰兒照", url: "topics/astronomy/lesson-35.html" },
            { title: "大霹靂核合成：輕元素從哪裡來", url: "topics/astronomy/lesson-36.html" },
            { title: "宇宙暴脹：解決視界問題與平坦性問題", url: "topics/astronomy/lesson-37.html" },
            { title: "暗能量與 ΛCDM 標準模型", url: "topics/astronomy/lesson-38.html" },
            { title: "宇宙的命運：熱寂、大擠壓還是大撕裂", url: "topics/astronomy/lesson-39.html" }
          ]
        },
        {
          title: "模組 G｜實戰應用",
          courses: [
            { title: "星圖與觀星：認識自己頭頂上的星空", url: "topics/astronomy/lesson-40.html" },
            { title: "公民科學與天文新聞：怎麼參與真實研究、讀懂報導", url: "topics/astronomy/lesson-41.html" },
            { title: "總結：還沒解決的大問題，以及怎麼持續追蹤宇宙研究", url: "topics/astronomy/lesson-42.html" }
          ]
        }
      ]
    },
    {
      id: "korean",
      category: "life",
      title: "韓文字母入門：看懂招牌、點餐、自由行",
      description:
        "為韓國自由行設計的實用課程。從世宗大王發明訓民正音的設計邏輯出發，完整拆解母音、子音、收尾音的拼讀規則，再進到打招呼、交通、住宿、點餐、購物等旅遊實戰場景。韓文內容可點擊聽真人發音（預錄音檔，任何裝置都能播放）。",
      icon: "🇰🇷",
      url: "topics/korean/index.html",
      resources: [
        {
          title: "拼音聽力練習題庫",
          description: "100 句實用旅遊韓文隨機出題，看文字猜拼音，按鈕核對答案並試聽真人發音",
          icon: "🎧",
          url: "topics/korean/practice.html"
        }
      ],
      modules: [
        {
          title: "模組 A｜認識韓文字：訓民正音的智慧",
          courses: [
            { title: "韓文為什麼好學：世宗大王與訓民正音的故事", url: "topics/korean/lesson-01.html" },
            { title: "母音的設計邏輯：天地人三個符號生出所有母音", url: "topics/korean/lesson-02.html" },
            { title: "子音的設計邏輯：模仿發音器官形狀的天才設計", url: "topics/korean/lesson-03.html" },
            { title: "音節方塊：韓文為什麼看起來像方塊字", url: "topics/korean/lesson-04.html" },
            { title: "模組總結：為什麼語言學家稱韓文是最科學的文字系統", url: "topics/korean/lesson-05.html" }
          ]
        },
        {
          title: "模組 B｜拼讀練習：從字母到會讀",
          courses: [
            { title: "基本母音全表與發音", url: "topics/korean/lesson-06.html" },
            { title: "基本子音全表與發音", url: "topics/korean/lesson-07.html" },
            { title: "複合母音：兩個母音黏起來的音", url: "topics/korean/lesson-08.html" },
            { title: "收尾音（받침）：音節最後藏起來的子音", url: "topics/korean/lesson-09.html" },
            { title: "硬音與送氣音：ㄲㄸㅃㅆㅉ 的緊張感", url: "topics/korean/lesson-10.html" },
            { title: "模組總結：完整拼讀練習，讀出你的第一個韓文句子", url: "topics/korean/lesson-11.html" }
          ]
        },
        {
          title: "模組 C｜生存韓語：基本溝通",
          courses: [
            { title: "敬語入門：韓國人講話為什麼要看關係", url: "topics/korean/lesson-12.html" },
            { title: "打招呼與自我介紹", url: "topics/korean/lesson-13.html" },
            { title: "數字系統：漢字數字與純韓文數字，用在哪裡不一樣", url: "topics/korean/lesson-14.html" },
            { title: "生存短句：謝謝、抱歉、多少錢、廁所在哪", url: "topics/korean/lesson-15.html" },
            { title: "模組總結：迷路、生病、緊急狀況怎麼開口求助", url: "topics/korean/lesson-16.html" }
          ]
        },
        {
          title: "模組 D｜實戰場景：交通與住宿",
          courses: [
            { title: "機場入境：看懂機場指標與入境資訊", url: "topics/korean/lesson-17.html" },
            { title: "大眾運輸：地鐵站名與公車站牌實戰判讀", url: "topics/korean/lesson-18.html" },
            { title: "計程車與問路：怎麼表達你要去哪裡", url: "topics/korean/lesson-19.html" },
            { title: "飯店住宿常見用語與設施標示", url: "topics/korean/lesson-20.html" },
            { title: "模組總結：交通 APP 與地圖韓文介面導覽", url: "topics/korean/lesson-21.html" }
          ]
        },
        {
          title: "模組 E｜實戰場景：吃喝購物",
          courses: [
            { title: "看懂菜單：常見料理漢字詞與固有詞", url: "topics/korean/lesson-22.html" },
            { title: "點餐與外送常用句型", url: "topics/korean/lesson-23.html" },
            { title: "購物與退稅：市場、百貨、便利商店", url: "topics/korean/lesson-24.html" },
            { title: "咖啡廳與小吃攤常用語", url: "topics/korean/lesson-25.html" },
            { title: "模組總結：一張表看懂常見連鎖店與招牌", url: "topics/korean/lesson-26.html" }
          ]
        }
      ]
    },
    {
      id: "wave-theory",
      category: "life",
      title: "波浪理論：艾略特波浪完整解析與實戰應用",
      description:
        "從道氏理論出發，完整拆解艾略特波浪理論的推動浪、調整浪、費波納契比率與波浪級別系統，建立系統化的市場結構判讀能力。每個浪型都搭配線圖圖解，並誠實檢視這套理論的爭議與限制——這是一門理論解說＋圖表判讀＋批判思考並重的課程，不是操作建議。",
      icon: "🌊",
      url: "topics/wave-theory/index.html",
      modules: [
        {
          title: "模組 A｜起源與理論基礎",
          courses: [
            { title: "道氏理論回顧：艾略特波浪理論的出發點", url: "topics/wave-theory/lesson-01.html" },
            { title: "艾略特其人：從會計師到市場理論家", url: "topics/wave-theory/lesson-02.html" },
            { title: "群眾心理與波浪：為什麼價格會呈現波浪狀態", url: "topics/wave-theory/lesson-03.html" },
            { title: "波浪理論的基本主張：5波驅動＋3波修正", url: "topics/wave-theory/lesson-04.html" },
            { title: "模組總結：波浪理論在技術分析體系中的位置", url: "topics/wave-theory/lesson-05.html" }
          ]
        },
        {
          title: "模組 B｜推動浪的完整規則",
          courses: [
            { title: "推動浪五波結構總覽：1-2-3-4-5 的角色分工", url: "topics/wave-theory/lesson-06.html" },
            { title: "第1波與第2波：起漲的猶豫與回測", url: "topics/wave-theory/lesson-07.html" },
            { title: "第3波：為什麼它通常是最強、最不能是最短的一波", url: "topics/wave-theory/lesson-08.html" },
            { title: "第4波與第5波：末端的分歧與衰竭", url: "topics/wave-theory/lesson-09.html" },
            { title: "三條鐵律：波浪理論唯一不可違反的規則，完整說明", url: "topics/wave-theory/lesson-10.html" },
            { title: "延伸浪（Extension）：當某一推動浪特別強勁", url: "topics/wave-theory/lesson-11.html" }
          ]
        },
        {
          title: "模組 C｜調整浪的完整規則",
          courses: [
            { title: "調整浪總覽：為什麼修正比驅動更難判讀", url: "topics/wave-theory/lesson-12.html" },
            { title: "鋸齒形（Zigzag）：5-3-5 的急跌急漲結構", url: "topics/wave-theory/lesson-13.html" },
            { title: "平台形（Flat）：規則形、擴張形、失敗形三種變化", url: "topics/wave-theory/lesson-14.html" },
            { title: "三角形調整：收斂、擴張、上升、下降、水平五種型態", url: "topics/wave-theory/lesson-15.html" },
            { title: "複合修正（Combination）：雙重三與三重三", url: "topics/wave-theory/lesson-16.html" },
            { title: "模組總結：調整浪型態速查與辨識技巧", url: "topics/wave-theory/lesson-17.html" }
          ]
        },
        {
          title: "模組 D｜特殊型態與例外規則",
          courses: [
            { title: "楔形（Diagonal）：唯一允許重疊的推動浪", url: "topics/wave-theory/lesson-18.html" },
            { title: "起始楔形與終結楔形的差異與辨識", url: "topics/wave-theory/lesson-19.html" },
            { title: "波浪截斷（Truncation）：第五波失敗的訊號", url: "topics/wave-theory/lesson-20.html" },
            { title: "模組總結：例外規則整理與常見誤判", url: "topics/wave-theory/lesson-21.html" }
          ]
        },
        {
          title: "模組 E｜費波納契比率與波浪測量",
          courses: [
            { title: "費波納契數列：完整推導黃金比例 1.618 的由來", url: "topics/wave-theory/lesson-22.html" },
            { title: "回撤比率：38.2%、50%、61.8% 在波浪理論中的意義", url: "topics/wave-theory/lesson-23.html" },
            { title: "延伸與目標比率：161.8%、261.8% 怎麼算出下一個目標價", url: "topics/wave-theory/lesson-24.html" },
            { title: "波浪等長與比例關係：第五波常見的測量法則", url: "topics/wave-theory/lesson-25.html" },
            { title: "時間週期的費波納契應用", url: "topics/wave-theory/lesson-26.html" },
            { title: "模組總結：完整費波納契測量流程演練", url: "topics/wave-theory/lesson-27.html" }
          ]
        },
        {
          title: "模組 F｜波浪級別與標記系統",
          courses: [
            { title: "波浪級別總表：從超級循環到次微浪的九個層級", url: "topics/wave-theory/lesson-28.html" },
            { title: "標記慣例：數字、羅馬數字、字母怎麼混用不出錯", url: "topics/wave-theory/lesson-29.html" },
            { title: "碎形結構：為什麼每一段浪裡面都藏著更小的浪", url: "topics/wave-theory/lesson-30.html" }
          ]
        },
        {
          title: "模組 G｜實戰數浪：從理論到圖表",
          courses: [
            { title: "數浪的第一步：先定調再找起點", url: "topics/wave-theory/lesson-31.html" },
            { title: "一步步數浪實戰：用真實線圖走一遍完整流程", url: "topics/wave-theory/lesson-32.html" },
            { title: "常見數浪錯誤與修正方法", url: "topics/wave-theory/lesson-33.html" },
            { title: "交替原則（Alternation）：排除錯誤波數的實用工具", url: "topics/wave-theory/lesson-34.html" },
            { title: "搭配其他指標驗證：成交量、RSI 與波浪的交叉確認", url: "topics/wave-theory/lesson-35.html" },
            { title: "多重可能路徑：波浪理論本質上是機率遊戲，不是唯一解", url: "topics/wave-theory/lesson-36.html" },
            { title: "模組總結：建立自己的數浪檢查清單", url: "topics/wave-theory/lesson-37.html" }
          ]
        },
        {
          title: "模組 H｜案例研究與理論的爭議",
          courses: [
            { title: "歷史案例一：完整走一遍經典大浪走勢", url: "topics/wave-theory/lesson-38.html" },
            { title: "歷史案例二：一次失敗的數浪與事後修正", url: "topics/wave-theory/lesson-39.html" },
            { title: "對波浪理論的批評：主觀性與不可證偽性爭議", url: "topics/wave-theory/lesson-40.html" },
            { title: "專業交易者怎麼用：作為輔助工具而非唯一系統", url: "topics/wave-theory/lesson-41.html" },
            { title: "課程總結：波浪理論的價值、限制，以及後續可以怎麼延伸學習", url: "topics/wave-theory/lesson-42.html" }
          ]
        }
      ]
    },
    {
      id: "web-scraping",
      category: "tech",
      title: "HTML／JavaScript 網頁解剖學：給爬蟲工程師的實戰入門",
      description:
        "為已有 Python 背景、想寫爬蟲的人設計。目標不是變成前端工程師，而是看懂一個網頁「資料從哪裡來、怎麼被瀏覽器組出來」——DOM 結構、CSS 選擇器與 XPath、JavaScript 與非同步請求、分頁與動態載入、追蹤 JS 算出來的神秘參數，一路橋接到 requests／Selenium／Playwright 的實戰選擇。",
      icon: "🕷️",
      url: "topics/web-scraping/index.html",
      modules: [
        {
          title: "模組 A｜HTML 深化：從爬蟲視角重新認識網頁結構",
          courses: [
            { title: "View Source vs. DOM：原始碼跟瀏覽器實際解析結果的關鍵差異", url: "topics/web-scraping/lesson-01.html" },
            { title: "DOM 樹狀結構：HTML 文字怎麼變成程式看得懂的物件樹", url: "topics/web-scraping/lesson-02.html" },
            { title: "屬性大複習：id、class、data-* 屬性在爬蟲裡的角色", url: "topics/web-scraping/lesson-03.html" },
            { title: "CSS 選擇器完整教學：標籤、class、id、組合選擇器", url: "topics/web-scraping/lesson-04.html" },
            { title: "XPath 入門：另一套定位元素的語言，跟CSS選擇器互補", url: "topics/web-scraping/lesson-05.html" },
            { title: "開發者工具實戰：用 DevTools 快速找到資料的選擇器路徑", url: "topics/web-scraping/lesson-06.html" }
          ]
        },
        {
          title: "模組 B｜JavaScript 語法基礎：給 Python 工程師的對照式入門",
          courses: [
            { title: "為什麼要學JS：現代網頁的資料不是都寫死在HTML裡", url: "topics/web-scraping/lesson-07.html" },
            { title: "變數與資料型態：對照 Python，注意 let/const 與動態型別的坑", url: "topics/web-scraping/lesson-08.html" },
            { title: "函式與箭頭函式：對照 def 與 lambda", url: "topics/web-scraping/lesson-09.html" },
            { title: "作用域與閉包（Closure）：看懂加密／簽章程式碼的關鍵基礎", url: "topics/web-scraping/lesson-10.html" },
            { title: "陣列與物件：對照 list 與 dict，重點在存取語法差異", url: "topics/web-scraping/lesson-11.html" },
            { title: "條件、迴圈與常用內建方法：對照 Python 慣用寫法", url: "topics/web-scraping/lesson-12.html" },
            { title: "模組總結：JS基礎語法速查表", url: "topics/web-scraping/lesson-13.html" }
          ]
        },
        {
          title: "模組 C｜JavaScript 與網頁互動：DOM 操作與事件",
          courses: [
            { title: "用JS選取並操作DOM元素：querySelector 系列方法", url: "topics/web-scraping/lesson-14.html" },
            { title: "事件是什麼：點擊、滾動、輸入怎麼觸發JS", url: "topics/web-scraping/lesson-15.html" },
            { title: "網頁「動態渲染」的原理：為什麼有些資料要等JS跑完才出現", url: "topics/web-scraping/lesson-16.html" },
            { title: "辨認靜態頁面 vs 動態渲染頁面的實戰技巧", url: "topics/web-scraping/lesson-17.html" },
            { title: "模組總結：從畫面回推「這段資料從哪裡來」的偵探流程", url: "topics/web-scraping/lesson-18.html" }
          ]
        },
        {
          title: "模組 D｜非同步與網路請求：現代網頁資料流動的核心",
          courses: [
            { title: "同步與非同步：為什麼JS常寫「等一下再做」", url: "topics/web-scraping/lesson-19.html" },
            { title: "Promise 與 async/await：JS處理非同步的核心工具", url: "topics/web-scraping/lesson-20.html" },
            { title: "Fetch API：JS怎麼發送網路請求", url: "topics/web-scraping/lesson-21.html" },
            { title: "用 DevTools 的 Network 分頁找到隱藏的API", url: "topics/web-scraping/lesson-22.html" },
            { title: "追蹤神秘參數：用 Initiator／中斷點回推是哪段JS算出這個值的", url: "topics/web-scraping/lesson-23.html" },
            { title: "這對爬蟲的意義：直接打API通常比爬渲染後的HTML更簡單", url: "topics/web-scraping/lesson-24.html" },
            { title: "模組總結：一步步示範怎麼在真實網站上找到隱藏的API", url: "topics/web-scraping/lesson-25.html" }
          ]
        },
        {
          title: "模組 E｜爬蟲實戰橋接：從瀏覽器知識到 Python 工具",
          courses: [
            { title: "靜態頁面策略：requests + BeautifulSoup 什麼時候就夠用", url: "topics/web-scraping/lesson-26.html" },
            { title: "動態頁面策略：Selenium / Playwright 概念與選擇時機", url: "topics/web-scraping/lesson-27.html" },
            { title: "分頁與動態載入完整攻略：頁碼連結、Load More、無限捲動、API分頁參數", url: "topics/web-scraping/lesson-28.html" },
            { title: "複製JS運算結果到Python：直接執行JS片段（Node.js／PyExecJS）vs. 重寫成Python邏輯", url: "topics/web-scraping/lesson-29.html" },
            { title: "模仿瀏覽器發送請求：headers、cookies、session 的角色", url: "topics/web-scraping/lesson-30.html" },
            { title: "常見反爬蟲機制與應對思路：User-Agent、速率限制、驗證碼", url: "topics/web-scraping/lesson-31.html" },
            { title: "爬蟲的合法與道德邊界：robots.txt、服務條款、資料使用的分寸", url: "topics/web-scraping/lesson-32.html" },
            { title: "課程總結：面對一個全新網站的完整診斷流程", url: "topics/web-scraping/lesson-33.html" }
          ]
        }
      ]
    },
    {
      id: "final-cut-pro",
      category: "tech",
      title: "Final Cut Pro 剪輯進階：磁性時間軸、複合片段、關鍵影格與效率工具",
      description:
        "為已經會剪Vlog、簡單轉場、字幕、基本關鍵影格的人設計的進階課程。從磁性時間軸的底層邏輯開始，把「已經會用」變成「懂得為什麼這樣用」，再深入複合片段、關鍵影格（含怎麼快速找到片段上已有的關鍵影格）、快捷鍵，最後補上一批投報率很高的效率工具。概念類搭配示意圖，實際操作類搭配依真實介面樣式繪製的高擬真示意圖。",
      icon: "🎬",
      url: "topics/final-cut-pro/index.html",
      modules: [
        {
          title: "模組 A｜FCP 的剪輯邏輯：重新理解你已經在用的東西",
          courses: [
            { title: "磁性時間軸：FCP 最大特色，跟傳統多軌剪輯的差異", url: "topics/final-cut-pro/lesson-01.html" },
            { title: "主要故事線 vs. 連接片段：B-roll、音樂為什麼不用手動對齊時間", url: "topics/final-cut-pro/lesson-02.html" },
            { title: "連接、覆蓋、插入：幾種基本剪輯動作在磁性時間軸裡的行為差異", url: "topics/final-cut-pro/lesson-03.html" },
            { title: "Roles（角色）系統：用類型管理音軌與素材，取代死板的軌道編號", url: "topics/final-cut-pro/lesson-04.html" },
            { title: "模組總結：理解這套邏輯之後，剪輯效率會差在哪裡", url: "topics/final-cut-pro/lesson-05.html" }
          ]
        },
        {
          title: "模組 B｜複合片段（Compound Clip）完整操作",
          courses: [
            { title: "複合片段是什麼：把多個片段包成一個可管理的單位", url: "topics/final-cut-pro/lesson-06.html" },
            { title: "建立複合片段：操作示範", url: "topics/final-cut-pro/lesson-07.html" },
            { title: "進入與離開複合片段：巢狀編輯與路徑列（breadcrumb）", url: "topics/final-cut-pro/lesson-08.html" },
            { title: "修改複合片段內部後，外部時間軸會發生什麼事", url: "topics/final-cut-pro/lesson-09.html" },
            { title: "複合片段 vs. 多機位剪輯：什麼時候該用哪一種", url: "topics/final-cut-pro/lesson-10.html" },
            { title: "實戰應用：用複合片段整理Vlog裡常重複的片段（片頭、Logo動畫等）", url: "topics/final-cut-pro/lesson-11.html" },
            { title: "模組總結：複合片段的整理心法", url: "topics/final-cut-pro/lesson-12.html" }
          ]
        },
        {
          title: "模組 C｜關鍵影格（Keyframe）完整攻略",
          courses: [
            { title: "關鍵影格是什麼：讓參數隨時間變化的機制複習", url: "topics/final-cut-pro/lesson-13.html" },
            { title: "怎麼幫一個參數加上關鍵影格：位置、縮放、透明度", url: "topics/final-cut-pro/lesson-14.html" },
            { title: "【核心】怎麼快速找到片段上已經有的關鍵影格：動畫編輯器完整教學", url: "topics/final-cut-pro/lesson-15.html" },
            { title: "在時間軸上跳轉到上一個／下一個關鍵影格", url: "topics/final-cut-pro/lesson-16.html" },
            { title: "修改、刪除、複製貼上關鍵影格", url: "topics/final-cut-pro/lesson-17.html" },
            { title: "常見應用：運鏡模擬（Ken Burns 效果）、音量淡入淡出、文字動畫", url: "topics/final-cut-pro/lesson-18.html" },
            { title: "疑難排解：動畫跑掉了，怎麼快速抓出是哪個影格出錯", url: "topics/final-cut-pro/lesson-19.html" }
          ]
        },
        {
          title: "模組 D｜快捷鍵完整攻略：加速你的剪輯流程",
          courses: [
            { title: "播放與瀏覽快捷鍵：JKL、空白鍵、逐格移動", url: "topics/final-cut-pro/lesson-20.html" },
            { title: "標記與選取快捷鍵：入點/出點、Marker、精準選取片段", url: "topics/final-cut-pro/lesson-21.html" },
            { title: "剪輯動作快捷鍵：連接（Q）、覆蓋（D）、插入（W）、附加（E）", url: "topics/final-cut-pro/lesson-22.html" },
            { title: "修剪快捷鍵：刀片工具、漣漪修剪、卷動剪輯、位置微調", url: "topics/final-cut-pro/lesson-23.html" },
            { title: "複合片段與關鍵影格相關快捷鍵總複習", url: "topics/final-cut-pro/lesson-24.html" },
            { title: "自訂快捷鍵：Command Editor，設定符合自己習慣的按鍵組合", url: "topics/final-cut-pro/lesson-25.html" },
            { title: "模組總結：一張完整的快捷鍵速查表", url: "topics/final-cut-pro/lesson-26.html" }
          ]
        },
        {
          title: "模組 E｜更多好用功能：讓剪輯更快更輕鬆",
          courses: [
            { title: "略讀（Skimming）：不用播放就能快速瀏覽素材", url: "topics/final-cut-pro/lesson-27.html" },
            { title: "關鍵字收藏與智慧收藏：管理大量Vlog素材的整理方法", url: "topics/final-cut-pro/lesson-28.html" },
            { title: "Markers 標記：邊剪邊記筆記，之後系統性處理", url: "topics/final-cut-pro/lesson-29.html" },
            { title: "穩定化（Stabilization）：一鍵修正手持拍攝的手震", url: "topics/final-cut-pro/lesson-30.html" },
            { title: "Match Color：不同鏡頭、不同光線的畫面一鍵配色統一", url: "topics/final-cut-pro/lesson-31.html" },
            { title: "Enhance Audio：一鍵降噪、齊平音量，解決Vlog收音品質問題", url: "topics/final-cut-pro/lesson-32.html" },
            { title: "精確剪輯器（Precision Editor）：微調剪接點的隱藏神器", url: "topics/final-cut-pro/lesson-33.html" },
            { title: "速度變更與速度坡度（Retiming）：慢動作、加速效果，銜接關鍵影格", url: "topics/final-cut-pro/lesson-34.html" },
            { title: "代理媒體與背景轉譯：4K素材剪輯更順暢的效能技巧", url: "topics/final-cut-pro/lesson-35.html" },
            { title: "課程總結：把這些功能整合進你的剪輯工作流程", url: "topics/final-cut-pro/lesson-36.html" }
          ]
        }
      ]
    },
    {
      id: "chinese-medicine",
      category: "life",
      title: "中醫完整知識課程：從陰陽五行到把脈、辨證、開方",
      description:
        "系統性的中醫理論入門課。從陰陽五行、臟腑經絡的世界觀開始，深入四診合參（把脈完整攻略）、辨證論治的推理邏輯，再到中藥學、方劑學怎麼決定用藥與劑量，最後以案例演練與現代反思收尾。這是理論與歷史脈絡的完整介紹，不是自我診斷或用藥指南——實際身體狀況請諮詢合格中醫師。",
      icon: "☯",
      url: "topics/chinese-medicine/index.html",
      modules: [
        {
          title: "模組 A｜中醫的世界觀：陰陽五行與氣血津液",
          courses: [
            { title: "中醫是什麼：跟西醫思維方式的根本差異", url: "topics/chinese-medicine/lesson-01.html" },
            { title: "陰陽：中醫理解一切變化的基本框架", url: "topics/chinese-medicine/lesson-02.html" },
            { title: "五行：木火土金水，一套關聯性思維系統", url: "topics/chinese-medicine/lesson-03.html" },
            { title: "氣、血、津液：中醫理解的身體「物質基礎」", url: "topics/chinese-medicine/lesson-04.html" },
            { title: "模組總結：這套世界觀怎麼指導後面所有的診斷跟治療", url: "topics/chinese-medicine/lesson-05.html" }
          ]
        },
        {
          title: "模組 B｜臟腑經絡：中醫如何理解人體結構",
          courses: [
            { title: "臟腑學說：中醫的「五臟六腑」跟解剖學臟器的差異", url: "topics/chinese-medicine/lesson-06.html" },
            { title: "心、肝：功能與相關症狀", url: "topics/chinese-medicine/lesson-07.html" },
            { title: "脾、肺：功能與相關症狀", url: "topics/chinese-medicine/lesson-08.html" },
            { title: "腎：先天之本，中醫特別重視的臟腑", url: "topics/chinese-medicine/lesson-09.html" },
            { title: "經絡系統：氣血運行的路徑，跟針灸的關係", url: "topics/chinese-medicine/lesson-10.html" },
            { title: "模組總結：臟腑經絡怎麼串成一張完整的人體地圖", url: "topics/chinese-medicine/lesson-11.html" }
          ]
        },
        {
          title: "模組 C｜四診合參：望聞問切完整攻略",
          courses: [
            { title: "四診總覽：望聞問切分別在收集什麼資訊", url: "topics/chinese-medicine/lesson-12.html" },
            { title: "望診：觀察氣色、舌診（舌頭是中醫的重要「儀表板」）", url: "topics/chinese-medicine/lesson-13.html" },
            { title: "聞診與問診：聲音氣味，以及問診要問哪些關鍵問題", url: "topics/chinese-medicine/lesson-14.html" },
            { title: "切診入門：把脈的基本原理，為什麼手腕的脈能反映全身", url: "topics/chinese-medicine/lesson-15.html" },
            { title: "把脈實務：寸關尺三部，怎麼定位、怎麼下指", url: "topics/chinese-medicine/lesson-16.html" },
            { title: "脈象大全：常見脈象的分類與意義（浮沉遲數等）", url: "topics/chinese-medicine/lesson-17.html" },
            { title: "把脈的難處：為什麼這是最難學的一診，常見誤區", url: "topics/chinese-medicine/lesson-18.html" },
            { title: "模組總結：四診合參——單一診法都不夠，怎麼綜合判斷", url: "topics/chinese-medicine/lesson-19.html" }
          ]
        },
        {
          title: "模組 D｜辨證論治：從症狀到證型的推理邏輯",
          courses: [
            { title: "辨證論治是什麼：中醫診斷的核心方法論", url: "topics/chinese-medicine/lesson-20.html" },
            { title: "八綱辨證：陰陽表裡寒熱虛實，最基礎的分類框架", url: "topics/chinese-medicine/lesson-21.html" },
            { title: "臟腑辨證：症狀怎麼對應到特定臟腑的問題", url: "topics/chinese-medicine/lesson-22.html" },
            { title: "六經辨證與衛氣營血辨證：外感疾病的階段性判斷", url: "topics/chinese-medicine/lesson-23.html" },
            { title: "同病異治、異病同治：中醫獨特的診斷邏輯", url: "topics/chinese-medicine/lesson-24.html" },
            { title: "模組總結：從一堆症狀，怎麼一步步推理出證型", url: "topics/chinese-medicine/lesson-25.html" }
          ]
        },
        {
          title: "模組 E｜中藥學基礎：性味歸經與怎麼認識一味藥",
          courses: [
            { title: "中藥的四氣五味：怎麼描述一味藥的基本性質", url: "topics/chinese-medicine/lesson-26.html" },
            { title: "歸經：一味藥主要作用在哪個臟腑經絡", url: "topics/chinese-medicine/lesson-27.html" },
            { title: "升降浮沉：藥性的作用方向", url: "topics/chinese-medicine/lesson-28.html" },
            { title: "中藥分類：解表藥、補益藥、清熱藥等主要類別", url: "topics/chinese-medicine/lesson-29.html" },
            { title: "常用中藥實例解析：從性味歸經看懂藥效邏輯", url: "topics/chinese-medicine/lesson-30.html" },
            { title: "模組總結：怎麼「讀懂」一味藥的完整檔案", url: "topics/chinese-medicine/lesson-31.html" }
          ]
        },
        {
          title: "模組 F｜方劑學：君臣佐使，怎麼把藥組成一帖方子",
          courses: [
            { title: "方劑學是什麼：為什麼中藥很少單味使用", url: "topics/chinese-medicine/lesson-32.html" },
            { title: "君臣佐使：一帖方子裡每味藥的角色分工", url: "topics/chinese-medicine/lesson-33.html" },
            { title: "經典方劑解析：從結構看懂一帖名方怎麼設計的", url: "topics/chinese-medicine/lesson-34.html" },
            { title: "藥物配伍：七情——藥物之間的加強、抵銷、拮抗關係", url: "topics/chinese-medicine/lesson-35.html" },
            { title: "加減變化：同一個基礎方，怎麼依證型調整", url: "topics/chinese-medicine/lesson-36.html" },
            { title: "模組總結：怎麼「決定藥品」——從證型走到一帖方子的完整邏輯", url: "topics/chinese-medicine/lesson-37.html" }
          ]
        },
        {
          title: "模組 G｜劑量的決定：影響用量的所有因素",
          courses: [
            { title: "劑量怎麼決定：藥性強弱、產地、炮製方式的影響", url: "topics/chinese-medicine/lesson-38.html" },
            { title: "個體差異：體質、年齡、體重怎麼影響劑量", url: "topics/chinese-medicine/lesson-39.html" },
            { title: "病情差異：病程輕重緩急、季節怎麼影響劑量", url: "topics/chinese-medicine/lesson-40.html" },
            { title: "煎煮法與服藥法：劑量之外，煎煮方式也會影響藥效", url: "topics/chinese-medicine/lesson-41.html" },
            { title: "模組總結：劑量決定是一套多因素綜合判斷，不是查表照抄", url: "topics/chinese-medicine/lesson-42.html" }
          ]
        },
        {
          title: "模組 H｜整合實戰與現代反思",
          courses: [
            { title: "案例演練一：一個常見證型的完整診斷到開方過程", url: "topics/chinese-medicine/lesson-43.html" },
            { title: "案例演練二：另一個證型的對照分析", url: "topics/chinese-medicine/lesson-44.html" },
            { title: "中西醫比較：中醫理論框架跟現代醫學實證方法的差異", url: "topics/chinese-medicine/lesson-45.html" },
            { title: "誠實看待中醫：哪些部分有現代研究支持、哪些仍有爭議", url: "topics/chinese-medicine/lesson-46.html" },
            { title: "課程總結：把整套中醫知識體系串起來回顧", url: "topics/chinese-medicine/lesson-47.html" }
          ]
        }
      ]
    },
    {
      id: "electronics",
      category: "tech",
      title: "電子電路完整課程：從電壓電流到麵包板實作",
      description:
        "從基礎數學出發的電子電路自學課程。從電壓電流的物理直覺開始，建立直流電路分析、微分方程（RC/RL）、複數與相量這些必要的數學工具箱，再深入濾波器、半導體元件、運算放大器與數位邏輯，最後用一系列麵包板實作專案把理論變成動手做的能力。",
      icon: "⚡",
      url: "topics/electronics/index.html",
      modules: [
        {
          title: "模組 A｜電路的基本語言：電壓、電流、電阻的物理直覺",
          courses: [
            { title: "電荷是什麼：從原子裡的電子講起", url: "topics/electronics/lesson-01.html" },
            { title: "電流：電荷的流動，跟水流的類比與差異", url: "topics/electronics/lesson-02.html" },
            { title: "電壓：為什麼電荷會流動，位能差的概念", url: "topics/electronics/lesson-03.html" },
            { title: "電阻與歐姆定律：V=IR 背後的物理意義", url: "topics/electronics/lesson-04.html" },
            { title: "電功率：電路裡能量轉換的速度", url: "topics/electronics/lesson-05.html" },
            { title: "模組總結：用電池、電阻、燈泡搭出你的第一個心智模型", url: "topics/electronics/lesson-06.html" }
          ]
        },
        {
          title: "模組 B｜直流電路分析：基爾荷夫定律與化簡技巧",
          courses: [
            { title: "串聯與並聯：電阻怎麼合併化簡", url: "topics/electronics/lesson-07.html" },
            { title: "基爾荷夫電流定律（KCL）：節點上的電荷守恆", url: "topics/electronics/lesson-08.html" },
            { title: "基爾荷夫電壓定律（KVL）：迴路上的能量守恆", url: "topics/electronics/lesson-09.html" },
            { title: "節點分析法：系統化解複雜電路的第一套方法", url: "topics/electronics/lesson-10.html" },
            { title: "迴路分析法：另一套系統化解法，跟節點分析法的取捨", url: "topics/electronics/lesson-11.html" },
            { title: "疊加定理：多電源電路的分而治之", url: "topics/electronics/lesson-12.html" },
            { title: "戴維寧與諾頓等效電路：把複雜電路簡化成一顆電池", url: "topics/electronics/lesson-13.html" },
            { title: "模組總結：面對一張複雜電路圖，你的解題流程", url: "topics/electronics/lesson-14.html" }
          ]
        },
        {
          title: "模組 C｜電容與電感：儲能元件與微分方程入門",
          courses: [
            { title: "電容是什麼：儲存電荷的元件，跟電池的差異", url: "topics/electronics/lesson-15.html" },
            { title: "電感是什麼：儲存磁場能量的元件", url: "topics/electronics/lesson-16.html" },
            { title: "【數學工具箱】為什麼需要微分方程：電容電感的電流電壓關係", url: "topics/electronics/lesson-17.html" },
            { title: "RC電路：充放電的指數曲線，時間常數的意義", url: "topics/electronics/lesson-18.html" },
            { title: "RL電路：跟RC對照著學，加深理解", url: "topics/electronics/lesson-19.html" },
            { title: "一階電路的完整解法：從物理情境列方程到解出答案", url: "topics/electronics/lesson-20.html" },
            { title: "模組總結：儲能元件怎麼讓電路有了「記憶」", url: "topics/electronics/lesson-21.html" }
          ]
        },
        {
          title: "模組 D｜交流電路：相量法與複數工具箱",
          courses: [
            { title: "為什麼要研究交流：從家用電談起", url: "topics/electronics/lesson-22.html" },
            { title: "【數學工具箱】複數與相量：把正弦波變成好算的東西", url: "topics/electronics/lesson-23.html" },
            { title: "阻抗：電阻概念在交流世界的推廣", url: "topics/electronics/lesson-24.html" },
            { title: "RLC 串聯電路的相量分析", url: "topics/electronics/lesson-25.html" },
            { title: "RLC 並聯電路的相量分析", url: "topics/electronics/lesson-26.html" },
            { title: "諧振：電路對特定頻率的特殊反應", url: "topics/electronics/lesson-27.html" },
            { title: "交流功率：實功、虛功、功率因數", url: "topics/electronics/lesson-28.html" },
            { title: "模組總結：直流思維怎麼無縫轉換成交流思維", url: "topics/electronics/lesson-29.html" }
          ]
        },
        {
          title: "模組 E｜濾波器與頻率響應",
          courses: [
            { title: "頻率響應是什麼：電路對不同頻率訊號的不同反應", url: "topics/electronics/lesson-30.html" },
            { title: "低通濾波器：為什麼能濾掉高頻雜訊", url: "topics/electronics/lesson-31.html" },
            { title: "高通與帶通濾波器", url: "topics/electronics/lesson-32.html" },
            { title: "波德圖（Bode Plot）：用圖形讀懂一個電路的個性", url: "topics/electronics/lesson-33.html" },
            { title: "模組總結：濾波器在真實產品裡的應用", url: "topics/electronics/lesson-34.html" }
          ]
        },
        {
          title: "模組 F｜半導體元件：二極體與電晶體",
          courses: [
            { title: "半導體是什麼：導體與絕緣體之間的材料", url: "topics/electronics/lesson-35.html" },
            { title: "PN接面與二極體：電流只能單向通過的原理", url: "topics/electronics/lesson-36.html" },
            { title: "二極體電路應用：整流、限幅、保護電路", url: "topics/electronics/lesson-37.html" },
            { title: "電晶體是什麼：從二極體到三端元件", url: "topics/electronics/lesson-38.html" },
            { title: "BJT：電流控制電流的放大器", url: "topics/electronics/lesson-39.html" },
            { title: "MOSFET：電壓控制電流，現代晶片的基礎", url: "topics/electronics/lesson-40.html" },
            { title: "電晶體當開關用：數位電路的元件基礎", url: "topics/electronics/lesson-41.html" },
            { title: "模組總結：從一顆電晶體到一整片晶片的距離", url: "topics/electronics/lesson-42.html" }
          ]
        },
        {
          title: "模組 G｜運算放大器",
          courses: [
            { title: "理想運算放大器模型：先別管內部，把它當黑盒子", url: "topics/electronics/lesson-43.html" },
            { title: "負回授：運放電路穩定運作的關鍵原理", url: "topics/electronics/lesson-44.html" },
            { title: "反相與非反相放大電路", url: "topics/electronics/lesson-45.html" },
            { title: "加法器、差動放大器：組合出更複雜的功能", url: "topics/electronics/lesson-46.html" },
            { title: "比較器：運放的另一種用法，類比通往數位的橋樑", url: "topics/electronics/lesson-47.html" },
            { title: "模組總結：運放是類比電路的萬用積木", url: "topics/electronics/lesson-48.html" }
          ]
        },
        {
          title: "模組 H｜數位邏輯基礎",
          courses: [
            { title: "二進位與邏輯準位：0與1怎麼對應到電壓", url: "topics/electronics/lesson-49.html" },
            { title: "基本邏輯閘：AND、OR、NOT、XOR", url: "topics/electronics/lesson-50.html" },
            { title: "真值表與布林代數：邏輯電路的數學語言", url: "topics/electronics/lesson-51.html" },
            { title: "組合邏輯電路：用邏輯閘搭出實際功能", url: "topics/electronics/lesson-52.html" },
            { title: "正反器與時脈：電路怎麼有了「記憶」與「節奏」", url: "topics/electronics/lesson-53.html" },
            { title: "模組總結：從邏輯閘到微處理器的一線之隔", url: "topics/electronics/lesson-54.html" }
          ]
        },
        {
          title: "模組 I｜實作應用：從電路圖到麵包板",
          courses: [
            { title: "怎麼讀懂一張真實的電路圖（電路符號總複習）", url: "topics/electronics/lesson-55.html" },
            { title: "麵包板實作入門：怎麼搭建、怎麼除錯", url: "topics/electronics/lesson-56.html" },
            { title: "實戰一：LED驅動電路", url: "topics/electronics/lesson-57.html" },
            { title: "實戰二：交替閃爍LED電路——兩顆電晶體搭出的無穩態震盪器", url: "topics/electronics/lesson-58.html" },
            { title: "實戰三：用555計時器IC重做交替閃爍——從分立元件到積體電路", url: "topics/electronics/lesson-59.html" },
            { title: "實戰四：光敏／溫度感測電路", url: "topics/electronics/lesson-60.html" },
            { title: "實戰五：直流穩壓電源供應器", url: "topics/electronics/lesson-61.html" },
            { title: "實戰六：簡單音訊放大電路", url: "topics/electronics/lesson-62.html" },
            { title: "實戰七：直流馬達控制電路", url: "topics/electronics/lesson-63.html" },
            { title: "實戰八：簡易警報／感應電路", url: "topics/electronics/lesson-64.html" },
            { title: "銜接微控制器：什麼時候該從純硬體電路，轉向Arduino這類可程式化控制", url: "topics/electronics/lesson-65.html" },
            { title: "課程總結：把整套電路知識整合成實作能力", url: "topics/electronics/lesson-66.html" }
          ]
        }
      ]
    },
    {
      id: "computer-science",
      category: "tech",
      title: "計算機概論：從資訊表示到現代電腦架構",
      description:
        "從二進位與資訊表示法出發，完整建立CPU運作、記憶體階層、作業系統、資料結構與演算法、網路、資料庫、資訊安全的知識地圖，最後深入管線化、分支預測、多核心、GPU、Spectre/Meltdown等現代電腦架構理論——不只是傳統計概，更補上「為什麼現代CPU這麼快」的完整解釋。",
      icon: "💻",
      url: "topics/computer-science/index.html",
      modules: [
        {
          title: "模組 A｜電腦系統與資訊表示法基礎",
          courses: [
            { title: "電腦是什麼：硬體、軟體與von Neumann架構", url: "topics/computer-science/lesson-01.html" },
            { title: "二進位、八進位、十六進位：數字系統與轉換", url: "topics/computer-science/lesson-02.html" },
            { title: "負數的表示法：二補數", url: "topics/computer-science/lesson-03.html" },
            { title: "浮點數：IEEE 754怎麼表示小數", url: "topics/computer-science/lesson-04.html" },
            { title: "字元編碼：從ASCII到Unicode／UTF-8", url: "topics/computer-science/lesson-05.html" },
            { title: "模組總結：資訊在電腦裡的「共同語言」", url: "topics/computer-science/lesson-06.html" }
          ]
        },
        {
          title: "模組 B｜從程式碼到執行：CPU如何運作",
          courses: [
            { title: "高階語言、組合語言、機器碼：三個層次", url: "topics/computer-science/lesson-07.html" },
            { title: "編譯與直譯：程式碼怎麼變成能執行的東西", url: "topics/computer-science/lesson-08.html" },
            { title: "CPU的基本結構：暫存器、ALU、控制單元", url: "topics/computer-science/lesson-09.html" },
            { title: "指令集架構（ISA）：CPU看得懂的「詞彙表」", url: "topics/computer-science/lesson-10.html" },
            { title: "提取－解碼－執行：一行程式碼的完整旅程", url: "topics/computer-science/lesson-11.html" },
            { title: "模組總結：從for迴圈到電路訊號的完整對照", url: "topics/computer-science/lesson-12.html" }
          ]
        },
        {
          title: "模組 C｜記憶體階層與儲存系統",
          courses: [
            { title: "記憶體階層：為什麼不能全部都用最快的記憶體", url: "topics/computer-science/lesson-13.html" },
            { title: "局部性原理：快取為什麼有效的理論基礎", url: "topics/computer-science/lesson-14.html" },
            { title: "快取記憶體基礎：直接對映、集合關聯、置換策略", url: "topics/computer-science/lesson-15.html" },
            { title: "RAM的種類與基本運作：SRAM vs. DRAM", url: "topics/computer-science/lesson-16.html" },
            { title: "VRAM：繪圖記憶體的特殊設計", url: "topics/computer-science/lesson-17.html" },
            { title: "虛擬記憶體：程式以為自己獨佔記憶體的幻覺", url: "topics/computer-science/lesson-18.html" },
            { title: "分頁機制：頁表與TLB怎麼加速位址轉換", url: "topics/computer-science/lesson-19.html" },
            { title: "儲存裝置（一）：硬碟的機械原理", url: "topics/computer-science/lesson-20.html" },
            { title: "儲存裝置（二）：SSD與快閃記憶體原理", url: "topics/computer-science/lesson-21.html" },
            { title: "記憶體可靠性：ECC與RAID基礎", url: "topics/computer-science/lesson-22.html" },
            { title: "模組總結：資料在系統裡的完整旅程", url: "topics/computer-science/lesson-23.html" }
          ]
        },
        {
          title: "模組 D｜作業系統概論",
          courses: [
            { title: "作業系統是什麼：管理硬體資源的軟體", url: "topics/computer-science/lesson-24.html" },
            { title: "程序與執行緒：程式執行的基本單位", url: "topics/computer-science/lesson-25.html" },
            { title: "CPU排程：誰先誰後，多工是怎麼做到的", url: "topics/computer-science/lesson-26.html" },
            { title: "記憶體管理：分頁與分段", url: "topics/computer-science/lesson-27.html" },
            { title: "檔案系統：資料怎麼被組織與存取", url: "topics/computer-science/lesson-28.html" },
            { title: "並行問題：死結與互斥鎖", url: "topics/computer-science/lesson-29.html" },
            { title: "模組總結：作業系統的全貌", url: "topics/computer-science/lesson-30.html" }
          ]
        },
        {
          title: "模組 E｜資料結構與演算法基礎",
          courses: [
            { title: "陣列與鏈結串列：兩種基本資料組織方式", url: "topics/computer-science/lesson-31.html" },
            { title: "堆疊與佇列：後進先出與先進先出", url: "topics/computer-science/lesson-32.html" },
            { title: "樹狀結構：階層式資料的表示法", url: "topics/computer-science/lesson-33.html" },
            { title: "圖形結構與走訪演算法：BFS與DFS", url: "topics/computer-science/lesson-34.html" },
            { title: "排序演算法：從氣泡排序到快速排序", url: "topics/computer-science/lesson-35.html" },
            { title: "演算法複雜度：大O記號", url: "topics/computer-science/lesson-36.html" },
            { title: "模組總結：資料結構與演算法的實務意義", url: "topics/computer-science/lesson-37.html" }
          ]
        },
        {
          title: "模組 F｜程式語言與軟體工程概論",
          courses: [
            { title: "程式語言典範：指令式、物件導向、函數式", url: "topics/computer-science/lesson-38.html" },
            { title: "版本控制：Git的基本概念", url: "topics/computer-science/lesson-39.html" },
            { title: "軟體開發生命週期：從需求到維護", url: "topics/computer-science/lesson-40.html" },
            { title: "測試的基本概念：單元測試、整合測試", url: "topics/computer-science/lesson-41.html" },
            { title: "模組總結：寫程式之外，軟體工程還在乎什麼", url: "topics/computer-science/lesson-42.html" }
          ]
        },
        {
          title: "模組 G｜電腦網路基礎",
          courses: [
            { title: "網路的分層模型：OSI與TCP/IP", url: "topics/computer-science/lesson-43.html" },
            { title: "實體層與資料鏈結層：訊號、MAC位址與乙太網路", url: "topics/computer-science/lesson-44.html" },
            { title: "網路設備：集線器、交換器、路由器的差異", url: "topics/computer-science/lesson-45.html" },
            { title: "IP位址與子網路：CIDR怎麼劃分網路", url: "topics/computer-science/lesson-46.html" },
            { title: "路由與NAT：封包怎麼找到路、私有位址怎麼連上網路", url: "topics/computer-science/lesson-47.html" },
            { title: "傳輸層：TCP的可靠傳輸機制 vs. UDP的簡單快速", url: "topics/computer-science/lesson-48.html" },
            { title: "DNS：網域名稱怎麼變成IP位址", url: "topics/computer-science/lesson-49.html" },
            { title: "HTTP：網頁背後的協定", url: "topics/computer-science/lesson-50.html" },
            { title: "HTTPS與TLS：幫網路連線加密", url: "topics/computer-science/lesson-51.html" },
            { title: "Wi-Fi與無線網路基礎", url: "topics/computer-science/lesson-52.html" },
            { title: "模組總結：打開瀏覽器輸入網址之後發生的事", url: "topics/computer-science/lesson-53.html" }
          ]
        },
        {
          title: "模組 H｜資料庫基礎",
          courses: [
            { title: "關聯式資料庫：資料表、主鍵與外鍵", url: "topics/computer-science/lesson-54.html" },
            { title: "SQL基礎：用查詢語言操作資料", url: "topics/computer-science/lesson-55.html" },
            { title: "正規化：如何設計不會互相矛盾的資料表", url: "topics/computer-science/lesson-56.html" },
            { title: "模組總結：資料庫在真實系統中的角色", url: "topics/computer-science/lesson-57.html" }
          ]
        },
        {
          title: "模組 I｜資訊安全基礎",
          courses: [
            { title: "資訊安全的核心目標：CIA三角", url: "topics/computer-science/lesson-58.html" },
            { title: "加密基礎：對稱式加密與非對稱式加密", url: "topics/computer-science/lesson-59.html" },
            { title: "常見攻擊手法概覽：釣魚、SQL注入、DDoS", url: "topics/computer-science/lesson-60.html" },
            { title: "模組總結：資安思維的日常應用", url: "topics/computer-science/lesson-61.html" }
          ]
        },
        {
          title: "模組 J｜現代電腦架構（一）指令層級平行化",
          courses: [
            { title: "管線化：把一條指令拆成好幾個階段同時做", url: "topics/computer-science/lesson-62.html" },
            { title: "管線危障：資料危障、控制危障與結構危障", url: "topics/computer-science/lesson-63.html" },
            { title: "超純量與亂序執行：一次做不只一件事", url: "topics/computer-science/lesson-64.html" },
            { title: "分支預測：CPU怎麼「猜」程式接下來要走哪條路", url: "topics/computer-science/lesson-65.html" },
            { title: "投機執行：先做了再說，錯了就丟掉重來", url: "topics/computer-science/lesson-66.html" },
            { title: "模組總結：現代CPU的「看不見的忙碌」", url: "topics/computer-science/lesson-67.html" }
          ]
        },
        {
          title: "模組 K｜現代電腦架構（二）平行運算與系統極限",
          courses: [
            { title: "快取階層與快取一致性：多核心時代的新問題", url: "topics/computer-science/lesson-68.html" },
            { title: "多核心與多執行緒：從單核到多核的轉變", url: "topics/computer-science/lesson-69.html" },
            { title: "SIMD與向量運算：一個指令處理多筆資料", url: "topics/computer-science/lesson-70.html" },
            { title: "GPU架構：為什麼繪圖卡特別適合平行運算", url: "topics/computer-science/lesson-71.html" },
            { title: "Spectre與Meltdown：投機執行留下的安全漏洞", url: "topics/computer-science/lesson-72.html" },
            { title: "模組總結：從指令平行到資料平行的完整圖像", url: "topics/computer-science/lesson-73.html" }
          ]
        },
        {
          title: "模組 L｜電腦發展史與課程總結",
          courses: [
            { title: "電腦發展簡史：從真空管到積體電路", url: "topics/computer-science/lesson-74.html" },
            { title: "RISC vs. CISC：兩種指令集設計哲學", url: "topics/computer-science/lesson-75.html" },
            { title: "課程總結：從二進位到GPU平行運算的完整旅程", url: "topics/computer-science/lesson-76.html" }
          ]
        }
      ]
    },
    {
      id: "zodiac",
      category: "life",
      title: "星座學：起源、十二星座個性與相性",
      description:
        "從巴比倫星空觀測與希臘化占星學的起源出發，依火土風水四元素完整解析十二星座的個性特質，深入星座相性與三方四正的配對邏輯，進一步認識本命盤、十大行星與十二宮位的完整占星系統，最後誠實檢視科學怎麼看占星（巴納姆效應、雙盲實驗）。這是文化與歷史脈絡的完整介紹，不是命運預測或人生決策指南。",
      icon: "♈",
      url: "topics/zodiac/index.html",
      modules: [
        {
          title: "模組 A｜星座的起源與基礎架構",
          courses: [
            { title: "星座的起源：從巴比倫的星空觀測開始", url: "topics/zodiac/lesson-01.html" },
            { title: "黃道十二宮：太陽在天空中的年度軌跡", url: "topics/zodiac/lesson-02.html" },
            { title: "希臘化時期的占星學：托勒密與《占星四書》", url: "topics/zodiac/lesson-03.html" },
            { title: "「星座」不是「星座」：歲差現象與現代天文對照的落差", url: "topics/zodiac/lesson-04.html" },
            { title: "四元素與三模式：認識星座的分類架構", url: "topics/zodiac/lesson-05.html" },
            { title: "太陽星座 vs. 本命盤：為什麼「你是什麼星座」只是冰山一角", url: "topics/zodiac/lesson-06.html" }
          ]
        },
        {
          title: "模組 B｜火象星座：熱情與行動力",
          courses: [
            { title: "牡羊座：開創者的衝勁與坦率", url: "topics/zodiac/lesson-07.html" },
            { title: "獅子座：舞台中央的自信與慷慨", url: "topics/zodiac/lesson-08.html" },
            { title: "射手座：追求自由的探險家靈魂", url: "topics/zodiac/lesson-09.html" }
          ]
        },
        {
          title: "模組 C｜土象星座：務實與穩定",
          courses: [
            { title: "金牛座：追求安穩的感官享受者", url: "topics/zodiac/lesson-10.html" },
            { title: "處女座：追求完美的分析者", url: "topics/zodiac/lesson-11.html" },
            { title: "摩羯座：目標導向的現實主義者", url: "topics/zodiac/lesson-12.html" }
          ]
        },
        {
          title: "模組 D｜風象星座：思考與溝通",
          courses: [
            { title: "雙子座：好奇多變的溝通者", url: "topics/zodiac/lesson-13.html" },
            { title: "天秤座：追求和諧的協調者", url: "topics/zodiac/lesson-14.html" },
            { title: "水瓶座：獨立不群的理想主義者", url: "topics/zodiac/lesson-15.html" }
          ]
        },
        {
          title: "模組 E｜水象星座與十二星座回顧",
          courses: [
            { title: "巨蟹座：重視家庭的情感守護者", url: "topics/zodiac/lesson-16.html" },
            { title: "天蠍座：深刻強烈的洞察者", url: "topics/zodiac/lesson-17.html" },
            { title: "雙魚座：浪漫富同理心的夢想家", url: "topics/zodiac/lesson-18.html" },
            { title: "模組總結：十二星座全貌總覽", url: "topics/zodiac/lesson-19.html" }
          ]
        },
        {
          title: "模組 F｜星座之間的關係學",
          courses: [
            { title: "相性基礎：四元素之間怎麼「合得來」", url: "topics/zodiac/lesson-20.html" },
            { title: "三方四正：星座關係圖上的幾何學（三合、六合、四正、對分）", url: "topics/zodiac/lesson-21.html" },
            { title: "常見配對怎麼解讀：以牡羊座為例走一遍完整邏輯", url: "topics/zodiac/lesson-22.html" },
            { title: "相性不只看太陽星座：金星、火星在感情關係中的角色", url: "topics/zodiac/lesson-23.html" },
            { title: "模組總結：星座配對，該怎麼理性看待", url: "topics/zodiac/lesson-24.html" }
          ]
        },
        {
          title: "模組 G｜星座之外：本命盤的完整樣貌",
          courses: [
            { title: "本命盤是什麼：出生那一刻的天空快照", url: "topics/zodiac/lesson-25.html" },
            { title: "十大行星在占星中的意義：太陽、月亮、水金火...", url: "topics/zodiac/lesson-26.html" },
            { title: "十二宮位：本命盤裡的十二個生活領域", url: "topics/zodiac/lesson-27.html" },
            { title: "上升星座：為什麼「第一印象」跟「太陽星座」常常對不上", url: "topics/zodiac/lesson-28.html" },
            { title: "模組總結：一張本命盤怎麼被「讀」出來", url: "topics/zodiac/lesson-29.html" }
          ]
        },
        {
          title: "模組 H｜現代反思：科學怎麼看占星",
          courses: [
            { title: "占星與天文的分家：一門學科怎麼一分為二", url: "topics/zodiac/lesson-30.html" },
            { title: "巴納姆效應：為什麼星座描述「感覺都很準」", url: "topics/zodiac/lesson-31.html" },
            { title: "科學驗證：卡爾森1985年雙盲實驗與其他研究", url: "topics/zodiac/lesson-32.html" },
            { title: "課程總結：怎麼誠實地享受星座這套文化知識", url: "topics/zodiac/lesson-33.html" }
          ]
        }
      ]
    },
    {
      id: "tx-futures",
      category: "life",
      title: "台指期操作全紀錄：做多與做空策略完整解析",
      description:
        "從期貨與現貨的本質差異、台指期契約規格與槓桿保證金開始，建立 K 線、均線、支撐壓力與 RSI/MACD 等技術分析工具，再拆解做多與做空各自的進場邏輯與停損停利設計，最後收在資金風險管理與交易心理紀律。這是觀念與框架的教學，不是投資建議——期貨為高槓桿商品，虧損可能超過原始保證金。",
      icon: "📈",
      url: "topics/tx-futures/index.html",
      modules: [
        {
          title: "模組 A｜基礎入門",
          courses: [
            { title: "什麼是期貨：跟股票的本質差異", url: "topics/tx-futures/lesson-01.html" },
            { title: "台指期是什麼：追蹤標的與契約規格（大台／小台）", url: "topics/tx-futures/lesson-02.html" },
            { title: "保證金與槓桿：期貨風險為什麼遠高於現股", url: "topics/tx-futures/lesson-03.html" },
            { title: "結算制度：到期日、結算價、月合約與週合約", url: "topics/tx-futures/lesson-04.html" },
            { title: "正價差與逆價差：期貨與現貨價差的意義", url: "topics/tx-futures/lesson-05.html" },
            { title: "日盤與夜盤：為什麼夜盤特別重要", url: "topics/tx-futures/lesson-06.html" },
            { title: "開戶與下單：期貨商、保證金帳戶怎麼運作", url: "topics/tx-futures/lesson-07.html" },
            { title: "模組總結：操作前必須建立的基本認知", url: "topics/tx-futures/lesson-08.html" }
          ]
        },
        {
          title: "模組 B｜技術分析基礎工具",
          courses: [
            { title: "K線基礎：紅K黑K在說什麼故事", url: "topics/tx-futures/lesson-09.html" },
            { title: "常見K線型態：吞噬、十字星、槌子線", url: "topics/tx-futures/lesson-10.html" },
            { title: "均線系統：排列與交叉的意義", url: "topics/tx-futures/lesson-11.html" },
            { title: "支撐與壓力：怎麼判斷關鍵價位", url: "topics/tx-futures/lesson-12.html" },
            { title: "成交量：價量關係的基本邏輯", url: "topics/tx-futures/lesson-13.html" },
            { title: "趨勢線與型態學：上升、下降、盤整", url: "topics/tx-futures/lesson-14.html" },
            { title: "RSI與MACD：動能指標的判讀", url: "topics/tx-futures/lesson-15.html" },
            { title: "布林通道：波動率與價格通道", url: "topics/tx-futures/lesson-16.html" },
            { title: "模組總結：技術分析是機率工具，不是水晶球", url: "topics/tx-futures/lesson-17.html" }
          ]
        },
        {
          title: "模組 C｜做多策略",
          courses: [
            { title: "做多的基本邏輯：什麼情況該站在多方", url: "topics/tx-futures/lesson-18.html" },
            { title: "順勢交易：均線多頭排列與突破操作", url: "topics/tx-futures/lesson-19.html" },
            { title: "回檔找買點：順勢交易的進場時機", url: "topics/tx-futures/lesson-20.html" },
            { title: "台積電權值效應：半導體循環對多方的意義", url: "topics/tx-futures/lesson-21.html" },
            { title: "外資期貨籌碼：三大法人部位怎麼看", url: "topics/tx-futures/lesson-22.html" },
            { title: "做多的停損與移動停利設計", url: "topics/tx-futures/lesson-23.html" },
            { title: "模組總結：做多策略檢查清單", url: "topics/tx-futures/lesson-24.html" }
          ]
        },
        {
          title: "模組 D｜做空策略",
          courses: [
            { title: "做空的基本原理：先賣後買，跟融券的差異", url: "topics/tx-futures/lesson-25.html" },
            { title: "做空的時機：頭部型態與跌破支撐", url: "topics/tx-futures/lesson-26.html" },
            { title: "做空的無限風險概念與軋空行情", url: "topics/tx-futures/lesson-27.html" },
            { title: "避險型放空：用期貨對沖現貨部位", url: "topics/tx-futures/lesson-28.html" },
            { title: "放空的停損紀律為什麼要更嚴格", url: "topics/tx-futures/lesson-29.html" },
            { title: "外部風險事件對空方的衝擊", url: "topics/tx-futures/lesson-30.html" },
            { title: "模組總結：做空策略檢查清單", url: "topics/tx-futures/lesson-31.html" }
          ]
        },
        {
          title: "模組 E｜實戰案例演練",
          courses: [
            { title: "案例①：多頭排列的順勢做多——從進場到停利全紀錄", url: "topics/tx-futures/lesson-32.html" },
            { title: "案例②：假突破陷阱——為什麼這筆多單該停損出場", url: "topics/tx-futures/lesson-33.html" },
            { title: "案例③：頭部型態確立的做空——從訊號到出場", url: "topics/tx-futures/lesson-34.html" },
            { title: "案例④：軋空情境模擬——一筆空單如何失控，以及正確的應對", url: "topics/tx-futures/lesson-35.html" },
            { title: "案例⑤：盤整格局的假訊號——為什麼這段時間不該進場", url: "topics/tx-futures/lesson-36.html" },
            { title: "案例⑥：財報／法說會前後的波動——事件驅動的多空判斷", url: "topics/tx-futures/lesson-37.html" },
            { title: "案例⑦：美股夜盤大跌的隔日應對——外部衝擊下的部位調整", url: "topics/tx-futures/lesson-38.html" },
            { title: "案例⑧：當沖情境——一天之內的多空轉換", url: "topics/tx-futures/lesson-39.html" },
            { title: "案例⑨：波段留倉——抱單過夜過週的心理與部位管理", url: "topics/tx-futures/lesson-40.html" },
            { title: "案例⑩：多空同時看錯的情境——如何認錯出場、避免凹單", url: "topics/tx-futures/lesson-41.html" },
            { title: "綜合案例：完整一週交易日誌拆解（多空交替）", url: "topics/tx-futures/lesson-42.html" },
            { title: "模組總結：從十個案例中萃取出的共同決策框架", url: "topics/tx-futures/lesson-43.html" }
          ]
        },
        {
          title: "模組 F｜資金與風險管理",
          courses: [
            { title: "保證金水位管理：為什麼不能滿倉操作", url: "topics/tx-futures/lesson-44.html" },
            { title: "部位大小計算：一口到多口的資金配置", url: "topics/tx-futures/lesson-45.html" },
            { title: "停損與停利紀律：為什麼多數人做不到", url: "topics/tx-futures/lesson-46.html" },
            { title: "追繳保證金與強制平倉：實際發生時怎麼處理", url: "topics/tx-futures/lesson-47.html" },
            { title: "資金曲線管理：連續虧損後該怎麼調整", url: "topics/tx-futures/lesson-48.html" },
            { title: "模組總結：活得夠久，才有機會等到好行情", url: "topics/tx-futures/lesson-49.html" }
          ]
        },
        {
          title: "模組 G｜交易心理與紀律",
          courses: [
            { title: "為什麼知道方法卻做不到：交易心理的核心矛盾", url: "topics/tx-futures/lesson-50.html" },
            { title: "損失規避與過度交易的心理陷阱", url: "topics/tx-futures/lesson-51.html" },
            { title: "交易日誌：紀錄與檢討的實際做法", url: "topics/tx-futures/lesson-52.html" },
            { title: "建立自己的交易系統：規則化決策", url: "topics/tx-futures/lesson-53.html" },
            { title: "模組總結：紀律比策略本身更重要", url: "topics/tx-futures/lesson-54.html" }
          ]
        },
        {
          title: "模組 H｜總體因素與總結",
          courses: [
            { title: "台指期與總體經濟：利率、匯率、半導體循環", url: "topics/tx-futures/lesson-55.html" },
            { title: "常見新手錯誤總整理", url: "topics/tx-futures/lesson-56.html" },
            { title: "課程總結：多空策略的核心原則回顧", url: "topics/tx-futures/lesson-57.html" }
          ]
        }
      ]
    },
    {
      id: "music-production",
      category: "music",
      title: "電子音樂製作：從合成器到完整編曲",
      description:
        "承接《創作樂理》的和聲與曲式基礎，專注在電子音樂製作本身的技術：減法合成器怎麼從零打造聲音、取樣與節奏編程、流行／EDM 編曲的段落語言、貝斯與側鏈壓縮、混音與母帶基礎，最後完成一趟從聲音設計到完整編曲的製作旅程。軟體無關，概念為主。",
      icon: "🎛️",
      url: "topics/music-production/index.html",
      resources: [
        {
          title: "AI音樂生成風格組合頁",
          description: "點按鈕組合曲風、情緒、樂器、人聲、年代、結構等描述詞，即時產生可複製的AI音樂生成prompt",
          icon: "🧩",
          url: "topics/music-production/prompt-builder.html"
        }
      ],
      modules: [
        {
          title: "模組 A｜電子音樂製作的基礎概念",
          courses: [
            { title: "電子音樂 vs. 傳統錄音：製作邏輯的根本差異", url: "topics/music-production/lesson-01.html" },
            { title: "聲音的物理基礎：頻率、振幅、音色", url: "topics/music-production/lesson-02.html" },
            { title: "DAW是什麼：音軌、MIDI vs. 音訊、鋼琴捲軸的共通邏輯", url: "topics/music-production/lesson-03.html" },
            { title: "取樣率與位元深度：數位音訊的基本規格", url: "topics/music-production/lesson-04.html" },
            { title: "模組總結：從樂理到製作，你需要換一套思維", url: "topics/music-production/lesson-05.html" }
          ]
        },
        {
          title: "模組 B｜合成器：從零打造聲音",
          courses: [
            { title: "減法合成：電子音樂最核心的造音邏輯", url: "topics/music-production/lesson-06.html" },
            { title: "振盪器：波形決定的音色個性", url: "topics/music-production/lesson-07.html" },
            { title: "濾波器：從泛音裡雕出聲音的形狀", url: "topics/music-production/lesson-08.html" },
            { title: "包絡（ADSR）：聲音怎麼隨時間變化", url: "topics/music-production/lesson-09.html" },
            { title: "LFO：讓聲音「動起來」的週期性調變", url: "topics/music-production/lesson-10.html" },
            { title: "其他合成方式概覽：FM合成與疊加合成（Wavetable）", url: "topics/music-production/lesson-11.html" },
            { title: "模組總結：一個完整合成音色的誕生", url: "topics/music-production/lesson-12.html" }
          ]
        },
        {
          title: "模組 C｜取樣與節奏編程",
          courses: [
            { title: "取樣是什麼：從真實聲音到可編輯的素材", url: "topics/music-production/lesson-13.html" },
            { title: "鼓組取樣：電子音樂節奏的骨架", url: "topics/music-production/lesson-14.html" },
            { title: "切片與變調：取樣素材的常見處理手法", url: "topics/music-production/lesson-15.html" },
            { title: "節奏編程：MIDI節奏型態與四大基本律動", url: "topics/music-production/lesson-16.html" },
            { title: "Quantize與Swing：機械精準跟人性搖擺的取捨", url: "topics/music-production/lesson-17.html" },
            { title: "模組總結：合成 vs. 取樣，什麼時候該用哪個", url: "topics/music-production/lesson-18.html" }
          ]
        },
        {
          title: "模組 D｜流行/EDM編曲：從段落到能量曲線",
          courses: [
            { title: "電子舞曲的段落語言：Intro、Verse、Pre-chorus、Chorus/Hook", url: "topics/music-production/lesson-19.html" },
            { title: "Build-up與Drop：電子舞曲特有的張力結構", url: "topics/music-production/lesson-20.html" },
            { title: "Breakdown：把能量拉下來，才有下一次拉高的空間", url: "topics/music-production/lesson-21.html" },
            { title: "編曲即能量管理：一首歌的密度曲線怎麼設計", url: "topics/music-production/lesson-22.html" },
            { title: "和聲進行在編曲裡的角色：銜接《創作樂理》的和弦知識", url: "topics/music-production/lesson-23.html" },
            { title: "模組總結：完整拆解一首Future Bass的段落結構", url: "topics/music-production/lesson-24.html" }
          ]
        },
        {
          title: "模組 E｜貝斯與低頻設計",
          courses: [
            { title: "Sub-bass vs. Bass：兩種低頻角色的分工", url: "topics/music-production/lesson-25.html" },
            { title: "Kick與Bass的頻率打架問題：為什麼要「讓位」", url: "topics/music-production/lesson-26.html" },
            { title: "側鏈壓縮（Sidechain）：電子舞曲招牌的「呼吸感」", url: "topics/music-production/lesson-27.html" },
            { title: "模組總結：打造扎實不糊的低頻基礎", url: "topics/music-production/lesson-28.html" }
          ]
        },
        {
          title: "模組 F｜混音基礎：讓聲音各就各位",
          courses: [
            { title: "EQ：頻率空間的分配邏輯", url: "topics/music-production/lesson-29.html" },
            { title: "壓縮器：動態控制的基本原理", url: "topics/music-production/lesson-30.html" },
            { title: "空間效果：Reverb與Delay怎麼營造距離感", url: "topics/music-production/lesson-31.html" },
            { title: "立體聲寬度與聲像：讓混音有「寬度」", url: "topics/music-production/lesson-32.html" },
            { title: "模組總結：一條混音鏈的基本框架", url: "topics/music-production/lesson-33.html" }
          ]
        },
        {
          title: "模組 G｜自動化與聲音設計",
          courses: [
            { title: "自動化是什麼：讓參數隨時間變化", url: "topics/music-production/lesson-34.html" },
            { title: "Riser與Impact：電子舞曲轉場的標準配備", url: "topics/music-production/lesson-35.html" },
            { title: "White Noise掃頻：從安靜到爆發的張力製造機", url: "topics/music-production/lesson-36.html" },
            { title: "模組總結：把Build-up的張力具體做出來", url: "topics/music-production/lesson-37.html" }
          ]
        },
        {
          title: "模組 H｜人聲處理與流行製作技巧",
          courses: [
            { title: "人聲在電子/流行製作裡的角色", url: "topics/music-production/lesson-38.html" },
            { title: "音準修正的基本概念", url: "topics/music-production/lesson-39.html" },
            { title: "Vocal Chop：把人聲變成樂器的招牌技巧", url: "topics/music-production/lesson-40.html" },
            { title: "模組總結：人聲怎麼融進電子編曲", url: "topics/music-production/lesson-41.html" }
          ]
        },
        {
          title: "模組 I｜完成一首歌：母帶與整合實戰",
          courses: [
            { title: "母帶處理（Mastering）是什麼：混音與母帶的分工", url: "topics/music-production/lesson-42.html" },
            { title: "響度戰爭：LUFS是什麼，為什麼串流時代要在乎它", url: "topics/music-production/lesson-43.html" },
            { title: "主流EDM子類型巡禮：House、Future Bass、Progressive House、Trap的製作差異", url: "topics/music-production/lesson-44.html" },
            { title: "課程總結：從零到一首完整電子流行歌的製作旅程", url: "topics/music-production/lesson-45.html" }
          ]
        },
        {
          title: "模組 J｜番外：AI音樂生成的Prompt工程",
          courses: [
            { title: "AI音樂生成Prompt工程：怎麼組合出你想要的風格", url: "topics/music-production/lesson-46.html" }
          ]
        }
      ]
    },
    {
      id: "architecture",
      category: "tech",
      title: "建築工程：房子怎麼蓋出來的",
      description:
        "從台灣住宅最常見的RC/SRC構造出發，完整解析一棟房子怎麼從地基蓋到交屋：結構載重與地震設計的基本邏輯、模板鋼筋灌漿的施工流程、水電消防管線怎麼埋進房子裡、室內裝修收尾，最後到建築設計與法規的基本概念。概念為主，輔以少量基礎力學計算，並與《電子電路》課的電學知識互相銜接。",
      icon: "🏗️",
      url: "topics/architecture/index.html",
      modules: [
        {
          title: "模組 A｜建築基礎概念與怎麼看懂一棟房子",
          courses: [
            { title: "一棟房子是怎麼「生」出來的：從買地到入住的完整流程地圖", url: "topics/architecture/lesson-01.html" },
            { title: "建築師、結構技師、營造廠：誰負責蓋房子的哪個部分", url: "topics/architecture/lesson-02.html" },
            { title: "讀懂建築圖：平面圖、立面圖、剖面圖是什麼", url: "topics/architecture/lesson-03.html" },
            { title: "建築的骨架與皮膚：結構、外殼、管線、裝修的四層邏輯", url: "topics/architecture/lesson-04.html" },
            { title: "模組總結：建立看懂一棟房子的完整框架", url: "topics/architecture/lesson-05.html" }
          ]
        },
        {
          title: "模組 B｜結構系統：RC、SRC與台灣常見構造",
          courses: [
            { title: "RC鋼筋混凝土：台灣住宅最主流的構造方式", url: "topics/architecture/lesson-06.html" },
            { title: "鋼筋與混凝土的分工：為什麼要兩種材料一起用", url: "topics/architecture/lesson-07.html" },
            { title: "SRC與鋼構造：比RC更強的另一種選擇", url: "topics/architecture/lesson-08.html" },
            { title: "磚造與其他構造方式：為什麼現在較少見", url: "topics/architecture/lesson-09.html" },
            { title: "模組總結：不同構造方式的優缺點比較", url: "topics/architecture/lesson-10.html" }
          ]
        },
        {
          title: "模組 C｜載重與結構力學基礎",
          courses: [
            { title: "房子要扛住什麼：重力荷重、活載重、風力、地震力", url: "topics/architecture/lesson-11.html" },
            { title: "力怎麼流動：從屋頂到地基的載重傳遞路徑", url: "topics/architecture/lesson-12.html" },
            { title: "柱、梁、板：結構三兄弟各自的角色", url: "topics/architecture/lesson-13.html" },
            { title: "【基礎數學】簡單樑的受力：為什麼梁中間比較容易彎", url: "topics/architecture/lesson-14.html" },
            { title: "台灣的地震課題：耐震設計的基本邏輯", url: "topics/architecture/lesson-15.html" },
            { title: "模組總結：一棟房子怎麼「站得住」", url: "topics/architecture/lesson-16.html" }
          ]
        },
        {
          title: "模組 D｜地基與基礎工程",
          courses: [
            { title: "地質調查：蓋房子前為什麼要先鑽探土壤", url: "topics/architecture/lesson-17.html" },
            { title: "基礎的種類：獨立基腳、筏式基礎、樁基礎", url: "topics/architecture/lesson-18.html" },
            { title: "開挖與擋土：地下室怎麼挖得出來又不會塌", url: "topics/architecture/lesson-19.html" },
            { title: "模組總結：看不見的地下工程，卻是最關鍵的一步", url: "topics/architecture/lesson-20.html" }
          ]
        },
        {
          title: "模組 E｜結構體施工：從綁鋼筋到灌漿",
          courses: [
            { title: "模板工程：混凝土還沒硬之前，靠什麼撐住形狀", url: "topics/architecture/lesson-21.html" },
            { title: "綁鋼筋：結構的「骨頭」怎麼被組裝起來", url: "topics/architecture/lesson-22.html" },
            { title: "灌漿與養護：混凝土怎麼從液體變成堅固的石頭", url: "topics/architecture/lesson-23.html" },
            { title: "一層一層往上蓋：樓層施工的標準循環", url: "topics/architecture/lesson-24.html" },
            { title: "模組總結：結構體完工，房子的骨架站起來了", url: "topics/architecture/lesson-25.html" }
          ]
        },
        {
          title: "模組 F｜外殼工程：牆體、防水、門窗",
          courses: [
            { title: "隔間牆：RC構造裡「不是結構」的牆怎麼砌", url: "topics/architecture/lesson-26.html" },
            { title: "防水工程：為什麼漏水是房子最常見的毛病", url: "topics/architecture/lesson-27.html" },
            { title: "外牆與立面：磁磚、塗料、帷幕牆的選擇", url: "topics/architecture/lesson-28.html" },
            { title: "門窗工程：氣密、水密、隔音怎麼一次顧到", url: "topics/architecture/lesson-29.html" },
            { title: "模組總結：讓房子真正擋風遮雨的最後一層", url: "topics/architecture/lesson-30.html" }
          ]
        },
        {
          title: "模組 G｜管線工程：水電消防怎麼埋進房子裡",
          courses: [
            { title: "管線配置的大原則：為什麼要在結構體裡預埋", url: "topics/architecture/lesson-31.html" },
            { title: "給水系統：自來水怎麼送到每一層每一戶", url: "topics/architecture/lesson-32.html" },
            { title: "排水與污水系統：用過的水怎麼安全排走", url: "topics/architecture/lesson-33.html" },
            { title: "電力系統：從總開關到每個插座的配電邏輯", url: "topics/architecture/lesson-34.html" },
            { title: "消防與弱電系統：火警、對講機、網路線", url: "topics/architecture/lesson-35.html" },
            { title: "模組總結：一套完整管線系統的全貌", url: "topics/architecture/lesson-36.html" }
          ]
        },
        {
          title: "模組 H｜室內裝修與收尾",
          courses: [
            { title: "地板、天花板、牆面：室內三大表面工程", url: "topics/architecture/lesson-37.html" },
            { title: "廚房與衛浴：管線密度最高的兩個空間", url: "topics/architecture/lesson-38.html" },
            { title: "油漆、木作與最後驗收", url: "topics/architecture/lesson-39.html" },
            { title: "模組總結：從毛胚屋到能住人的家", url: "topics/architecture/lesson-40.html" }
          ]
        },
        {
          title: "模組 I｜建築設計：從法規到平面配置",
          courses: [
            { title: "建蔽率與容積率：法規怎麼決定一塊地能蓋多大", url: "topics/architecture/lesson-41.html" },
            { title: "日照、通風、動線：好的平面配置在解決什麼問題", url: "topics/architecture/lesson-42.html" },
            { title: "結構限制怎麼影響設計：為什麼有些牆不能打掉", url: "topics/architecture/lesson-43.html" },
            { title: "綠建築與節能設計基本概念", url: "topics/architecture/lesson-44.html" },
            { title: "模組總結：設計是在多少限制條件下找答案", url: "topics/architecture/lesson-45.html" }
          ]
        },
        {
          title: "模組 J｜整合實戰：一棟房子從買地到入住的完整旅程",
          courses: [
            { title: "完整案例：一棟透天厝從畫圖到交屋的時間軸", url: "topics/architecture/lesson-46.html" },
            { title: "常見驗屋問題與怎麼看懂缺失", url: "topics/architecture/lesson-47.html" },
            { title: "課程總結：從一堆磚頭鋼筋，到一個家", url: "topics/architecture/lesson-48.html" }
          ]
        }
      ]
    },
    {
      id: "jin-yong",
      category: "wuxia",
      title: "金庸武俠：十五部作品完整導讀",
      description:
        "從查良鏞的生平與武俠世界觀出發，依發表順序逐一深度導讀金庸十五部作品——射鵰三部曲、天龍八部、笑傲江湖、鹿鼎記等重量級長篇逐一拆解故事線、人物與武學設定，短篇精簡收錄，最後以人物群像比較、主題思想演變、版本流變與金學文化影響收尾。完整涵蓋十五部作品的內容，是全套精讀而非入門書單推薦。",
      icon: "🗡️",
      url: "topics/jin-yong/index.html",
      modules: [
        {
          title: "模組 A｜認識金庸：生平與創作背景",
          courses: [
            { title: "金庸是誰：從查良鏞到武俠小說第一人", url: "topics/jin-yong/lesson-01.html" },
            { title: "報業與武俠：金庸小說誕生的時代背景", url: "topics/jin-yong/lesson-02.html" },
            { title: "十五部作品全覽：一張地圖看懂所有故事的年代與關聯", url: "topics/jin-yong/lesson-03.html" },
            { title: "「飛雪連天射白鹿，笑書神俠倚碧鴛」：十五部作品的暗語與創作年表", url: "topics/jin-yong/lesson-04.html" },
            { title: "模組總結：在開始讀之前，你需要知道的事", url: "topics/jin-yong/lesson-05.html" }
          ]
        },
        {
          title: "模組 B｜武俠世界觀：門派、武功與內力體系",
          courses: [
            { title: "江湖是什麼：金庸筆下的武俠世界基本規則", url: "topics/jin-yong/lesson-06.html" },
            { title: "內功與輕功：金庸武學系統的底層邏輯", url: "topics/jin-yong/lesson-07.html" },
            { title: "名門正派：少林、武當、丐幫、峨嵋等門派巡禮", url: "topics/jin-yong/lesson-08.html" },
            { title: "邪魔外道：明教、日月神教等「反派」門派的複雜性", url: "topics/jin-yong/lesson-09.html" },
            { title: "兵器與武功秘笈：從屠龍刀倚天劍到九陰真經", url: "topics/jin-yong/lesson-10.html" },
            { title: "模組總結：讀懂武功招式，才能讀懂江湖", url: "topics/jin-yong/lesson-11.html" }
          ]
        },
        {
          title: "模組 C｜《書劍恩仇錄》：金庸的第一部武俠小說",
          courses: [
            { title: "故事背景：乾隆身世之謎與紅花會", url: "topics/jin-yong/lesson-12.html" },
            { title: "陳家洛與乾隆：兄弟還是宿敵", url: "topics/jin-yong/lesson-13.html" },
            { title: "香香公主與早期金庸的悲劇美學", url: "topics/jin-yong/lesson-14.html" },
            { title: "模組總結：初試啼聲，卻已見雛形", url: "topics/jin-yong/lesson-15.html" }
          ]
        },
        {
          title: "模組 D｜《碧血劍》：袁崇煥之子的復仇與抉擇",
          courses: [
            { title: "故事背景：明末亂世與闖王李自成", url: "topics/jin-yong/lesson-16.html" },
            { title: "袁承志的江湖與朝堂兩難", url: "topics/jin-yong/lesson-17.html" },
            { title: "模組總結：一部常被低估的過渡之作", url: "topics/jin-yong/lesson-18.html" }
          ]
        },
        {
          title: "模組 E｜《雪山飛狐》與《飛狐外傳》：胡斐的故事",
          courses: [
            { title: "《雪山飛狐》：一個羅生門式的敘事實驗", url: "topics/jin-yong/lesson-19.html" },
            { title: "苗人鳳與胡一刀：恩怨糾葛的上一代", url: "topics/jin-yong/lesson-20.html" },
            { title: "《飛狐外傳》：胡斐的成長與程靈素的犧牲", url: "topics/jin-yong/lesson-21.html" },
            { title: "模組總結：金庸最特別的敘事手法", url: "topics/jin-yong/lesson-22.html" }
          ]
        },
        {
          title: "模組 F｜《射鵰英雄傳》：射鵰三部曲首部曲",
          courses: [
            { title: "故事背景：南宋偏安與蒙古崛起", url: "topics/jin-yong/lesson-23.html" },
            { title: "郭靖：資質平庸卻成為大俠的成長典範", url: "topics/jin-yong/lesson-24.html" },
            { title: "黃蓉：金庸筆下最聰慧靈動的女主角", url: "topics/jin-yong/lesson-25.html" },
            { title: "東邪西毒南帝北丐：五絕的武學與人格", url: "topics/jin-yong/lesson-26.html" },
            { title: "江南七怪與丘處機：師恩與承諾", url: "topics/jin-yong/lesson-27.html" },
            { title: "降龍十八掌與九陰真經：武學脈絡的建立", url: "topics/jin-yong/lesson-28.html" },
            { title: "華箏與黃蓉：兩種愛情的抉擇", url: "topics/jin-yong/lesson-29.html" },
            { title: "模組總結：俠之大者，為國為民", url: "topics/jin-yong/lesson-30.html" }
          ]
        },
        {
          title: "模組 G｜《神鵰俠侶》：射鵰三部曲二部曲",
          courses: [
            { title: "故事背景：郭靖楊過的兩代恩怨", url: "topics/jin-yong/lesson-31.html" },
            { title: "楊過：叛逆的成長與被拋棄的傷痕", url: "topics/jin-yong/lesson-32.html" },
            { title: "小龍女：金庸筆下最特殊的女主角原型", url: "topics/jin-yong/lesson-33.html" },
            { title: "師徒戀的爭議與時代意義", url: "topics/jin-yong/lesson-34.html" },
            { title: "郭襄：一見楊過誤終身", url: "topics/jin-yong/lesson-35.html" },
            { title: "絕情谷與情花：情與毒的隱喻", url: "topics/jin-yong/lesson-36.html" },
            { title: "獨孤求敗與武學的哲學化", url: "topics/jin-yong/lesson-37.html" },
            { title: "模組總結：問世間，情是何物", url: "topics/jin-yong/lesson-38.html" }
          ]
        },
        {
          title: "模組 H｜《倚天屠龍記》：射鵰三部曲三部曲",
          courses: [
            { title: "故事背景：元末群雄並起", url: "topics/jin-yong/lesson-39.html" },
            { title: "張無忌：金庸筆下最「軟弱」的男主角", url: "topics/jin-yong/lesson-40.html" },
            { title: "趙敏、周芷若、小昭、殷離：四女奪愛的敘事結構", url: "topics/jin-yong/lesson-41.html" },
            { title: "明教與武林正道的對立與反轉", url: "topics/jin-yong/lesson-42.html" },
            { title: "九陽神功與乾坤大挪移：張無忌的武學奇遇", url: "topics/jin-yong/lesson-43.html" },
            { title: "張三丰與武當派：金庸筆下最理想的師父", url: "topics/jin-yong/lesson-44.html" },
            { title: "模組總結：三部曲的完成與武俠史觀的建立", url: "topics/jin-yong/lesson-45.html" }
          ]
        },
        {
          title: "模組 I｜《連城訣》：金庸最黑暗的一部作品",
          courses: [
            { title: "故事背景：一部沒有廟堂只有人性的小說", url: "topics/jin-yong/lesson-46.html" },
            { title: "狄雲的悲劇與江湖的險惡", url: "topics/jin-yong/lesson-47.html" },
            { title: "模組總結：金庸筆下最不留情面的人性描寫", url: "topics/jin-yong/lesson-48.html" }
          ]
        },
        {
          title: "模組 J｜《天龍八部》：金庸武俠的巔峰之作",
          courses: [
            { title: "故事背景：北宋、大理、遼國的三國演義", url: "topics/jin-yong/lesson-49.html" },
            { title: "喬峰：金庸筆下最悲壯的英雄", url: "topics/jin-yong/lesson-50.html" },
            { title: "段譽：癡情與武學奇遇的喜劇色彩", url: "topics/jin-yong/lesson-51.html" },
            { title: "虛竹：小人物的意外際遇", url: "topics/jin-yong/lesson-52.html" },
            { title: "三兄弟結義：一部關於身分認同的史詩", url: "topics/jin-yong/lesson-53.html" },
            { title: "王語嫣與慕容復：執念的兩種面貌", url: "topics/jin-yong/lesson-54.html" },
            { title: "降龍十八掌、六脈神劍、北冥神功：三大絕學的對照", url: "topics/jin-yong/lesson-55.html" },
            { title: "「天龍八部」佛教意象與眾生皆苦的主題", url: "topics/jin-yong/lesson-56.html" },
            { title: "模組總結：無人不冤，有情皆孽", url: "topics/jin-yong/lesson-57.html" }
          ]
        },
        {
          title: "模組 K｜《俠客行》：一部關於身分與頓悟的寓言",
          courses: [
            { title: "故事背景：石破天的雙重身分之謎", url: "topics/jin-yong/lesson-58.html" },
            { title: "俠客島與武學頓悟的哲學隱喻", url: "topics/jin-yong/lesson-59.html" },
            { title: "模組總結：不識字的主角，讀懂了最難的武功秘笈", url: "topics/jin-yong/lesson-60.html" }
          ]
        },
        {
          title: "模組 L｜《笑傲江湖》：政治寓言與武俠的極致",
          courses: [
            { title: "故事背景：一部刻意抹去朝代背景的小說", url: "topics/jin-yong/lesson-61.html" },
            { title: "令狐沖：金庸筆下最灑脫的浪子俠客", url: "topics/jin-yong/lesson-62.html" },
            { title: "任盈盈與東方不敗：日月神教的權力鬥爭", url: "topics/jin-yong/lesson-63.html" },
            { title: "岳不群與「君子劍」：偽善的極致刻畫", url: "topics/jin-yong/lesson-64.html" },
            { title: "獨孤九劍與辟邪劍法：兩種武學哲學的對決", url: "topics/jin-yong/lesson-65.html" },
            { title: "「笑傲江湖」曲：一部小說裡的音樂敘事", url: "topics/jin-yong/lesson-66.html" },
            { title: "模組總結：政治權力鬥爭的武俠寓言", url: "topics/jin-yong/lesson-67.html" }
          ]
        },
        {
          title: "模組 M｜《鹿鼎記》：金庸封筆之作與武俠的解構",
          courses: [
            { title: "故事背景：康熙年間的政治與江湖", url: "topics/jin-yong/lesson-68.html" },
            { title: "韋小寶：金庸筆下最「反英雄」的主角", url: "topics/jin-yong/lesson-69.html" },
            { title: "七位夫人：一部顛覆武俠愛情敘事的作品", url: "topics/jin-yong/lesson-70.html" },
            { title: "天地會與康熙：忠誠的分裂與抉擇", url: "topics/jin-yong/lesson-71.html" },
            { title: "神龍教與通吃島：韋小寶的江湖歷險", url: "topics/jin-yong/lesson-72.html" },
            { title: "不會武功的主角：金庸對武俠類型的自我解構", url: "topics/jin-yong/lesson-73.html" },
            { title: "鰲拜、陳近南、康熙：韋小寶身邊的三種權威", url: "topics/jin-yong/lesson-74.html" },
            { title: "模組總結：從俠之大者到反英雄，金庸的創作終點", url: "topics/jin-yong/lesson-75.html" }
          ]
        },
        {
          title: "模組 N｜《白馬嘯西風》、《鴛鴦刀》、《越女劍》：三則短篇的餘韻",
          courses: [
            { title: "《白馬嘯西風》：一部關於文化隔閡的悲劇", url: "topics/jin-yong/lesson-76.html" },
            { title: "《鴛鴦刀》：金庸最輕鬆詼諧的短篇", url: "topics/jin-yong/lesson-77.html" },
            { title: "《越女劍》：金庸最後的作品與最早的江湖", url: "topics/jin-yong/lesson-78.html" },
            { title: "模組總結：三則短篇裡的金庸餘韻", url: "topics/jin-yong/lesson-79.html" }
          ]
        },
        {
          title: "模組 O｜人物群像與角色比較",
          courses: [
            { title: "金庸男主角的成長光譜：從郭靖到韋小寶", url: "topics/jin-yong/lesson-80.html" },
            { title: "金庸女主角的類型學：俠女、才女、癡女、毒女", url: "topics/jin-yong/lesson-81.html" },
            { title: "亦正亦邪的複雜角色：喬峰、楊過、令狐沖的共同性", url: "topics/jin-yong/lesson-82.html" },
            { title: "金庸筆下的反派：從單純的惡到人性的灰階", url: "topics/jin-yong/lesson-83.html" },
            { title: "模組總結：金庸角色塑造的演化軌跡", url: "topics/jin-yong/lesson-84.html" }
          ]
        },
        {
          title: "模組 P｜主題思想的演變",
          courses: [
            { title: "早期作品的民族主義色彩：從《書劍恩仇錄》到《射鵰英雄傳》", url: "topics/jin-yong/lesson-85.html" },
            { title: "中期作品的人性複雜化：從單純正邪到灰色地帶", url: "topics/jin-yong/lesson-86.html" },
            { title: "晚期作品的解構與反思：《笑傲江湖》與《鹿鼎記》的政治寓言", url: "topics/jin-yong/lesson-87.html" },
            { title: "模組總結：金庸思想的三十年旅程", url: "topics/jin-yong/lesson-88.html" }
          ]
        },
        {
          title: "模組 Q｜版本流變：三個版本的金庸",
          courses: [
            { title: "舊版、修訂版、新修版：金庸為什麼要一改再改", url: "topics/jin-yong/lesson-89.html" },
            { title: "著名修改案例：康敏之死、王語嫣的結局等版本差異", url: "topics/jin-yong/lesson-90.html" },
            { title: "模組總結：沒有「唯一正確」的金庸文本", url: "topics/jin-yong/lesson-91.html" }
          ]
        },
        {
          title: "模組 R｜金庸的文化影響與金學",
          courses: [
            { title: "從報紙連載到全球現象：金庸小說的傳播史", url: "topics/jin-yong/lesson-92.html" },
            { title: "影視改編的百花齊放：從邵氏電影到現代劇集", url: "topics/jin-yong/lesson-93.html" },
            { title: "「金學」研究：金庸小說的學術地位爭議", url: "topics/jin-yong/lesson-94.html" },
            { title: "模組總結：一個華人文化共同記憶的形成", url: "topics/jin-yong/lesson-95.html" }
          ]
        },
        {
          title: "模組 S｜課程總結",
          courses: [
            { title: "課程總結：讀完金庸，你讀懂了什麼", url: "topics/jin-yong/lesson-96.html" }
          ]
        }
      ]
    },
    {
      id: "gu-long",
      category: "wuxia",
      title: "古龍武俠：經典代表作完整導讀",
      description:
        "古龍一生寫了六七十部武俠小說，其中不少代筆、續完、真偽存疑，這門課不做窮盡式收錄，而是深度導讀十部左右公認的代表作與系列——絕代雙驕、小李飛刀、楚留香、陸小鳳、蕭十一郎、流星蝴蝶劍、七種武器、天涯明月刀等，並專闢模組談古龍求新求變的敘事革命，以及他跟金庸美學的根本差異。",
      icon: "🔪",
      url: "topics/gu-long/index.html",
      modules: [
        {
          title: "模組 A｜認識古龍：生平與創作背景",
          courses: [
            { title: "古龍是誰：從熊耀華到武俠奇才", url: "topics/gu-long/lesson-01.html" },
            { title: "台灣武俠與香港武俠：兩種武俠傳統的分道揚鑣", url: "topics/gu-long/lesson-02.html" },
            { title: "混亂的創作生涯：代筆、續完與作品真偽之謎", url: "topics/gu-long/lesson-03.html" },
            { title: "古龍作品全覽：一張地圖看懂主要系列與代表作", url: "topics/gu-long/lesson-04.html" },
            { title: "模組總結：在開始讀之前，你需要知道的事", url: "topics/gu-long/lesson-05.html" }
          ]
        },
        {
          title: "模組 B｜古龍的武俠革命：敘事風格與哲學",
          courses: [
            { title: "「求新求變求突破」：古龍為什麼要打破金庸建立的傳統", url: "topics/gu-long/lesson-06.html" },
            { title: "短句、留白與電影感：古龍獨特的文字風格", url: "topics/gu-long/lesson-07.html" },
            { title: "推理與懸疑：把偵探小說的敘事邏輯帶進江湖", url: "topics/gu-long/lesson-08.html" },
            { title: "存在主義的孤獨英雄：古龍筆下主角的共同底色", url: "topics/gu-long/lesson-09.html" },
            { title: "古龍 vs. 金庸：兩種武俠美學的根本差異", url: "topics/gu-long/lesson-10.html" },
            { title: "模組總結：不寫歷史的武俠，寫的是人性", url: "topics/gu-long/lesson-11.html" }
          ]
        },
        {
          title: "模組 C｜《絕代雙驕》：古龍成名的轉捩點",
          courses: [
            { title: "故事背景：一對雙生兄弟的宿命對決", url: "topics/gu-long/lesson-12.html" },
            { title: "小魚兒：古龍筆下第一個「非典型主角」", url: "topics/gu-long/lesson-13.html" },
            { title: "花無缺：完美養成的悲劇", url: "topics/gu-long/lesson-14.html" },
            { title: "十大惡人：古龍筆下最有趣的反派群像", url: "topics/gu-long/lesson-15.html" },
            { title: "移花宮與江別鶴：兩種扭曲的教養", url: "topics/gu-long/lesson-16.html" },
            { title: "燕南天：尋子復仇的悲劇英雄", url: "topics/gu-long/lesson-17.html" },
            { title: "鐵心蘭與蘇櫻：小魚兒的兩位紅顏", url: "topics/gu-long/lesson-18.html" },
            { title: "本性與教養的對決：雙生兄弟最終的和解", url: "topics/gu-long/lesson-19.html" },
            { title: "模組總結：從傳統武俠邁向古龍風格的過渡之作", url: "topics/gu-long/lesson-20.html" }
          ]
        },
        {
          title: "模組 D｜《多情劍客無情劍》：小李飛刀系列",
          courses: [
            { title: "故事背景：一個關於放棄與救贖的故事", url: "topics/gu-long/lesson-21.html" },
            { title: "李尋歡：古龍筆下最悲情的主角原型", url: "topics/gu-long/lesson-22.html" },
            { title: "小李飛刀：「例不虛發」背後的哲學", url: "topics/gu-long/lesson-23.html" },
            { title: "林詩音與龍嘯雲：一段成全與犧牲的三角關係", url: "topics/gu-long/lesson-24.html" },
            { title: "阿飛與荊無命：兩種極端的孤獨", url: "topics/gu-long/lesson-25.html" },
            { title: "模組總結：無情的是刀，多情的是人", url: "topics/gu-long/lesson-26.html" }
          ]
        },
        {
          title: "模組 E｜楚留香系列：盜帥的傳奇",
          courses: [
            { title: "楚留香是誰：盜亦有道的風流浪子", url: "topics/gu-long/lesson-27.html" },
            { title: "《血海飄香》、《大沙漠》、《畫眉鳥》：系列開端三部曲", url: "topics/gu-long/lesson-28.html" },
            { title: "胡鐵花與姬冰雁：楚留香身邊的江湖", url: "topics/gu-long/lesson-29.html" },
            { title: "水母陰姬與中原一點紅：系列裡的經典反派", url: "topics/gu-long/lesson-30.html" },
            { title: "《蝙蝠傳奇》：石觀音與系列中期的轉折", url: "topics/gu-long/lesson-31.html" },
            { title: "《桃花傳奇》與《新月傳奇》：系列後期的江湖冒險", url: "topics/gu-long/lesson-32.html" },
            { title: "《午夜蘭花》：系列最沉重蒼涼的告別", url: "topics/gu-long/lesson-33.html" },
            { title: "楚留香的推理辦案模式：武俠與偵探小說的融合", url: "topics/gu-long/lesson-34.html" },
            { title: "模組總結：一個「盜賊」如何成為古龍最受歡迎的主角", url: "topics/gu-long/lesson-35.html" }
          ]
        },
        {
          title: "模組 F｜陸小鳳傳奇系列：另一種瀟灑",
          courses: [
            { title: "陸小鳳是誰：四條眉毛的傳奇", url: "topics/gu-long/lesson-36.html" },
            { title: "花滿樓：一個盲眼卻看得比誰都清楚的角色", url: "topics/gu-long/lesson-37.html" },
            { title: "西門吹雪：劍神的孤高與寂寞", url: "topics/gu-long/lesson-38.html" },
            { title: "《繡花大盜》與系列的推理色彩", url: "topics/gu-long/lesson-39.html" },
            { title: "模組總結：楚留香與陸小鳳，兩種浪子的異同", url: "topics/gu-long/lesson-40.html" }
          ]
        },
        {
          title: "模組 G｜《蕭十一郎》：為電影而生的武俠小說",
          courses: [
            { title: "故事背景：一部先有劇本後有小說的特殊創作", url: "topics/gu-long/lesson-41.html" },
            { title: "蕭十一郎與沈璧君：被誤解的浪子與被困住的女人", url: "topics/gu-long/lesson-42.html" },
            { title: "《火併蕭十一郎》：續集裡的江湖險惡", url: "topics/gu-long/lesson-43.html" },
            { title: "模組總結：武俠小說與電影敘事的跨界實驗", url: "topics/gu-long/lesson-44.html" }
          ]
        },
        {
          title: "模組 H｜《流星‧蝴蝶‧劍》：教父式的江湖政治",
          courses: [
            { title: "故事背景：從《教父》得到的靈感", url: "topics/gu-long/lesson-45.html" },
            { title: "孟星魂：一個殺手的自我覺醒", url: "topics/gu-long/lesson-46.html" },
            { title: "模組總結：權力鬥爭底下的江湖黑幫史詩", url: "topics/gu-long/lesson-47.html" }
          ]
        },
        {
          title: "模組 I｜七種武器系列：兵器與人性的寓言",
          courses: [
            { title: "系列設計：每一種武器，都是一種人性的隱喻", url: "topics/gu-long/lesson-48.html" },
            { title: "《長生劍》與《孔雀翎》：自信與武器的關係", url: "topics/gu-long/lesson-49.html" },
            { title: "《碧玉刀》與《多情環》：溫柔與背叛的兩面", url: "topics/gu-long/lesson-50.html" },
            { title: "《霸王槍》與《離別鉤》：系列的遺憾收尾", url: "topics/gu-long/lesson-51.html" },
            { title: "模組總結：兵器之外，古龍真正想寫的是什麼", url: "topics/gu-long/lesson-52.html" }
          ]
        },
        {
          title: "模組 J｜《天涯‧明月‧刀》與《三少爺的劍》：孤獨的極致",
          courses: [
            { title: "傅紅雪：古龍筆下最沉重壓抑的主角", url: "topics/gu-long/lesson-53.html" },
            { title: "《天涯明月刀》的實驗性文體", url: "topics/gu-long/lesson-54.html" },
            { title: "謝曉峰：從天下第一到隱姓埋名", url: "topics/gu-long/lesson-55.html" },
            { title: "模組總結：放下武功，才是真正的強大", url: "topics/gu-long/lesson-56.html" }
          ]
        },
        {
          title: "模組 K｜其他重要作品巡禮",
          courses: [
            { title: "《邊城浪子》與《歡樂英雄》：浪子與友情的兩種寫法", url: "topics/gu-long/lesson-57.html" },
            { title: "《英雄無淚》：晚期作品的虛無與蒼涼", url: "topics/gu-long/lesson-58.html" },
            { title: "《大人物》與古龍的黑色幽默", url: "topics/gu-long/lesson-59.html" },
            { title: "模組總結：古龍創作光譜的其他面向", url: "topics/gu-long/lesson-60.html" }
          ]
        },
        {
          title: "模組 L｜人物群像與主題比較",
          courses: [
            { title: "古龍主角的共同原型：浪子、殺手、酒鬼、棄兒", url: "topics/gu-long/lesson-61.html" },
            { title: "古龍女性角色的類型與侷限", url: "topics/gu-long/lesson-62.html" },
            { title: "友情：古龍筆下比愛情更重要的主題", url: "topics/gu-long/lesson-63.html" },
            { title: "古龍 vs. 金庸：人物塑造的根本差異總整理", url: "topics/gu-long/lesson-64.html" },
            { title: "模組總結：古龍的江湖，是一群孤獨者的江湖", url: "topics/gu-long/lesson-65.html" }
          ]
        },
        {
          title: "模組 M｜古龍的文化影響",
          courses: [
            { title: "影視改編熱潮：從邵氏電影到楚留香陸小鳳劇集", url: "topics/gu-long/lesson-66.html" },
            { title: "古龍文字風格對後世創作者的影響", url: "topics/gu-long/lesson-67.html" },
            { title: "模組總結：一個影響華語通俗文化的奇才", url: "topics/gu-long/lesson-68.html" }
          ]
        },
        {
          title: "模組 N｜課程總結",
          courses: [
            { title: "課程總結：讀懂古龍，讀懂江湖裡的孤獨", url: "topics/gu-long/lesson-69.html" }
          ]
        }
      ]
    },
    {
      id: "harry-potter",
      category: "fantasy",
      title: "哈利波特深度解析：七部曲完整導讀",
      description:
        "從J.K.羅琳的創作背景與魔法世界觀出發，逐部深度解析七部曲的劇情、伏筆與主題演變，再跳出單一故事線，橫向剖析角色心理、死亡與愛等核心主題、羅琳精密的伏筆佈局，最後誠實面對文本本身與作者本人的公眾爭議，並總覽這個系列的文化影響。",
      icon: "🪄",
      url: "topics/harry-potter/index.html",
      modules: [
        {
          title: "模組 A｜認識哈利波特：作者與創作背景",
          courses: [
            { title: "J.K.羅琳是誰：從單親媽媽到最暢銷小說家", url: "topics/harry-potter/lesson-01.html" },
            { title: "創作起源：一列從曼徹斯特開往倫敦的火車", url: "topics/harry-potter/lesson-02.html" },
            { title: "出版史：從十二次退稿到全球現象", url: "topics/harry-potter/lesson-03.html" },
            { title: "七部曲全覽：一張地圖看懂七年的霍格華茲歲月", url: "topics/harry-potter/lesson-04.html" },
            { title: "模組總結：在開始深讀之前，你需要知道的事", url: "topics/harry-potter/lesson-05.html" }
          ]
        },
        {
          title: "模組 B｜魔法世界觀：霍格華茲與巫師社會",
          courses: [
            { title: "霍格華茲：四大學院的分類邏輯與象徵意義", url: "topics/harry-potter/lesson-06.html" },
            { title: "魔法系統：咒語、魔杖與魔藥的運作邏輯", url: "topics/harry-potter/lesson-07.html" },
            { title: "巫師社會結構：魔法部、對角巷與巫師媒體", url: "topics/harry-potter/lesson-08.html" },
            { title: "血統制度：純血、麻瓜出身與混血的社會階級", url: "topics/harry-potter/lesson-09.html" },
            { title: "魔法生物與奇獸：從家庭小精靈到龍", url: "topics/harry-potter/lesson-10.html" },
            { title: "死神的聖物傳說：貫穿全系列的古老寓言", url: "topics/harry-potter/lesson-11.html" },
            { title: "模組總結：建立一套完整的魔法世界字典", url: "topics/harry-potter/lesson-12.html" }
          ]
        },
        {
          title: "模組 C｜《神秘的魔法石》：一切的開端",
          courses: [
            { title: "德思禮一家與被忽視的童年", url: "topics/harry-potter/lesson-13.html" },
            { title: "麻瓜世界到魔法世界：一個孤兒的身分覺醒", url: "topics/harry-potter/lesson-14.html" },
            { title: "對角巷與奧利凡德的魔杖店：命運的第一個伏筆", url: "topics/harry-potter/lesson-15.html" },
            { title: "三巨頭的相遇：哈利、榮恩、妙麗的友誼起點", url: "topics/harry-potter/lesson-16.html" },
            { title: "分類帽的抉擇與史萊哲林的伏筆", url: "topics/harry-potter/lesson-17.html" },
            { title: "海格、跩哥與意若思鏡：引路人、宿敵與慾望的隱喻", url: "topics/harry-potter/lesson-18.html" },
            { title: "三顆頭犬與層層試煉：魔法石與奇洛教授，第一次面對伏地魔的殘影", url: "topics/harry-potter/lesson-19.html" }
          ]
        },
        {
          title: "模組 D｜《消失的密室》：血統與偏見的初登場",
          courses: [
            { title: "多比的警告與衛斯理家的溫暖", url: "topics/harry-potter/lesson-20.html" },
            { title: "湯姆瑞斗的日記：伏地魔身分的第一條線索", url: "topics/harry-potter/lesson-21.html" },
            { title: "蜘蛛、蛇與爆竹一家：純血與麻種的偏見主題正式浮現", url: "topics/harry-potter/lesson-22.html" },
            { title: "洛哈教授的虛榮與騙局：名聲與吹噓的諷刺", url: "topics/harry-potter/lesson-23.html" },
            { title: "密室的真相：蛇妖、預言與哈利的分類帽疑雲", url: "topics/harry-potter/lesson-24.html" },
            { title: "多比重獲自由：家庭小精靈議題的初次觸及", url: "topics/harry-potter/lesson-25.html" }
          ]
        },
        {
          title: "模組 E｜《阿茲卡班的逃犯》：時間、記憶與親情",
          courses: [
            { title: "天狼星布萊克：一個被誤解的「逃犯」", url: "topics/harry-potter/lesson-26.html" },
            { title: "路平教授與催狂魔：恐懼與絕望的具象化", url: "topics/harry-potter/lesson-27.html" },
            { title: "巴克比克與海格的第一堂課：偏見與正義的隱喻", url: "topics/harry-potter/lesson-28.html" },
            { title: "護法咒與快樂記憶：這本書的情感核心", url: "topics/harry-potter/lesson-29.html" },
            { title: "蟲尾與背叛的真相：上一代友誼的裂痕", url: "topics/harry-potter/lesson-30.html" },
            { title: "時光器與時間迴圈：敘事結構上的巧思", url: "topics/harry-potter/lesson-31.html" }
          ]
        },
        {
          title: "模組 F｜《火盃的考驗》：競賽、成長與伏地魔的回歸",
          courses: [
            { title: "魁地奇世界盃與黑魔標記的重現", url: "topics/harry-potter/lesson-32.html" },
            { title: "三巫鬥法大賽：競賽結構與角色成長的舞台", url: "topics/harry-potter/lesson-33.html" },
            { title: "波巴洞與德姆蘭：國際巫師教育體系的擴展", url: "topics/harry-potter/lesson-34.html" },
            { title: "麗塔史譏、SPEW與妙麗的社會意識覺醒", url: "topics/harry-potter/lesson-35.html" },
            { title: "神秘的舞會：青春期社交焦慮的第一次描寫", url: "topics/harry-potter/lesson-36.html" },
            { title: "瘋眼穆敵：偽裝與信任危機", url: "topics/harry-potter/lesson-37.html" },
            { title: "墓園的重生：伏地魔正式回歸，系列轉向黑暗史詩", url: "topics/harry-potter/lesson-38.html" }
          ]
        },
        {
          title: "模組 G｜《鳳凰會的密令》：反抗、創傷與青春期的憤怒",
          courses: [
            { title: "夏天的沉默與哈利的孤立感", url: "topics/harry-potter/lesson-39.html" },
            { title: "恩不里居與魔法部的政治操作", url: "topics/harry-potter/lesson-40.html" },
            { title: "鳳凰會：上一代的反抗組織重新集結", url: "topics/harry-potter/lesson-41.html" },
            { title: "鄧不利多的軍隊：DA的成立與哈利的教學相長", url: "topics/harry-potter/lesson-42.html" },
            { title: "天狼星之死與哈利的憤怒", url: "topics/harry-potter/lesson-43.html" },
            { title: "石內卜的記憶：儲思盆事件與詹姆的另一面", url: "topics/harry-potter/lesson-44.html" },
            { title: "預言的內容：選擇者與被選擇者的辯證", url: "topics/harry-potter/lesson-45.html" },
            { title: "為什麼這本書是系列裡青少年心理最真實的一部", url: "topics/harry-potter/lesson-46.html" }
          ]
        },
        {
          title: "模組 H｜《混血王子的背叛》：石內卜的秘密與鄧不利多的計畫",
          courses: [
            { title: "新任首相與魔法部的戰時狀態", url: "topics/harry-potter/lesson-47.html" },
            { title: "鄧不利多的私人課程：伏地魔的成長史", url: "topics/harry-potter/lesson-48.html" },
            { title: "孤兒院的湯姆瑞斗：惡的起源追溯", url: "topics/harry-potter/lesson-49.html" },
            { title: "分靈體：靈魂分裂的黑魔法與代價", url: "topics/harry-potter/lesson-50.html" },
            { title: "混血王子的真實身分：一本魔藥課本的秘密", url: "topics/harry-potter/lesson-51.html" },
            { title: "跩哥馬份的任務：反派視角的人性化", url: "topics/harry-potter/lesson-52.html" },
            { title: "鄧不利多之死：系列最震撼的轉折", url: "topics/harry-potter/lesson-53.html" },
            { title: "石內卜殺死鄧不利多：忠誠與背叛的表象", url: "topics/harry-potter/lesson-54.html" }
          ]
        },
        {
          title: "模組 I｜《死神的聖物》：終局、犧牲與選擇",
          courses: [
            { title: "出發前的告別：七個哈利與魔法部陷落", url: "topics/harry-potter/lesson-55.html" },
            { title: "三兄弟的傳說：死神聖物的象徵意義", url: "topics/harry-potter/lesson-56.html" },
            { title: "分靈體大搜索：一場公路電影式的逃亡", url: "topics/harry-potter/lesson-57.html" },
            { title: "妙麗的魔法小提包：魔法的日常智慧", url: "topics/harry-potter/lesson-58.html" },
            { title: "家庭小精靈多比之死：犧牲主題的延續", url: "topics/harry-potter/lesson-59.html" },
            { title: "葛林戴華德與鄧不利多的過去：老年鄧不利多的秘密", url: "topics/harry-potter/lesson-60.html" },
            { title: "石內卜的記憶：忠誠的真相與莉莉的秘密", url: "topics/harry-potter/lesson-61.html" },
            { title: "禁忌森林：哈利選擇赴死的那一刻", url: "topics/harry-potter/lesson-62.html" },
            { title: "國王十字車站與最終戰役：生死之間的對話", url: "topics/harry-potter/lesson-63.html" }
          ]
        },
        {
          title: "模組 J｜角色深度剖析",
          courses: [
            { title: "哈利波特：一個「英雄」的養成與代價", url: "topics/harry-potter/lesson-64.html" },
            { title: "妙麗與榮恩：智慧與忠誠的兩種友誼典範", url: "topics/harry-potter/lesson-65.html" },
            { title: "石內卜：文學史上最複雜的角色之一", url: "topics/harry-potter/lesson-66.html" },
            { title: "鄧不利多：智慧長者形象的陰影面", url: "topics/harry-potter/lesson-67.html" },
            { title: "伏地魔：純粹之惡的心理成因", url: "topics/harry-potter/lesson-68.html" },
            { title: "天狼星、路平與上一代的鳳凰會", url: "topics/harry-potter/lesson-69.html" },
            { title: "模組總結：羅琳筆下角色塑造的共同手法", url: "topics/harry-potter/lesson-70.html" }
          ]
        },
        {
          title: "模組 K｜主題與文學技藝",
          courses: [
            { title: "死亡：貫穿七部曲的核心命題", url: "topics/harry-potter/lesson-71.html" },
            { title: "愛：最重要也最被低估的魔法", url: "topics/harry-potter/lesson-72.html" },
            { title: "選擇 vs. 宿命：分類帽與預言的辯證", url: "topics/harry-potter/lesson-73.html" },
            { title: "偏見與純血主義：種族隱喻的文學手法", url: "topics/harry-potter/lesson-74.html" },
            { title: "羅琳的伏筆藝術：從魔法石到死神聖物的細節佈局", url: "topics/harry-potter/lesson-75.html" },
            { title: "姓名學：角色命名背後的典故與隱喻", url: "topics/harry-potter/lesson-76.html" },
            { title: "模組總結：一部兒童文學如何承載這麼多重的主題", url: "topics/harry-potter/lesson-77.html" }
          ]
        },
        {
          title: "模組 L｜爭議與反思",
          courses: [
            { title: "文本本身的爭議：家庭小精靈、妖精與種族刻板印象的批評", url: "topics/harry-potter/lesson-78.html" },
            { title: "J.K.羅琳的公眾爭議：跨性別議題與粉絲社群的分裂", url: "topics/harry-potter/lesson-79.html" },
            { title: "讀者如何在作品與作者之間劃界：藝術與創作者的分離難題", url: "topics/harry-potter/lesson-80.html" },
            { title: "模組總結：複雜的評價，不妨礙誠實地面對", url: "topics/harry-potter/lesson-81.html" }
          ]
        },
        {
          title: "模組 M｜文化影響",
          courses: [
            { title: "電影改編：從新人演員到影史級系列", url: "topics/harry-potter/lesson-82.html" },
            { title: "主題樂園、周邊產業與魔法世界的商業帝國", url: "topics/harry-potter/lesson-83.html" },
            { title: "對後續奇幻/YA文學的影響", url: "topics/harry-potter/lesson-84.html" },
            { title: "模組總結：一個定義了一整個世代童年的故事", url: "topics/harry-potter/lesson-85.html" }
          ]
        },
        {
          title: "模組 N｜課程總結",
          courses: [
            { title: "課程總結：從麻瓜世界到國王十字車站的完整旅程", url: "topics/harry-potter/lesson-86.html" }
          ]
        }
      ]
    },
    {
      id: "big-bang",
      category: "science",
      title: "大霹靂起源論：宇宙如何開始的完整解析",
      description:
        "完整獨立、自成一套的宇宙學課程：從歷史發展與觀測現象出發，自建廣義相對論工具箱，完整推導弗里德曼方程式，深入大霹靂核合成、宇宙微波背景輻射、早期宇宙時間線、暴脹理論與暗物質暗能量，最後誠實面對「大爆炸之前發生什麼」這個開放問題。全程完整推導，不省略證明過程。",
      icon: "💥",
      url: "topics/big-bang/index.html",
      modules: [
        {
          title: "模組 A｜歷史發展與現象學基礎",
          courses: [
            { title: "奧伯斯悖論：為什麼夜晚的天空是黑的", url: "topics/big-bang/lesson-01.html" },
            { title: "哈伯的發現：星系正在遠離我們", url: "topics/big-bang/lesson-02.html" },
            { title: "勒梅特與伽莫夫：大霹靂理論的誕生", url: "topics/big-bang/lesson-03.html" },
            { title: "穩態宇宙論之爭：霍伊爾與對手陣營", url: "topics/big-bang/lesson-04.html" },
            { title: "1965年的意外發現：噪音、鴿子糞便與宇宙微波背景輻射", url: "topics/big-bang/lesson-05.html" }
          ]
        },
        {
          title: "模組 B｜廣義相對論工具箱：從等效原理到愛因斯坦場方程式",
          courses: [
            { title: "為什麼描述宇宙需要廣義相對論：牛頓重力的極限", url: "topics/big-bang/lesson-06.html" },
            { title: "等效原理：重力與加速度的等價性", url: "topics/big-bang/lesson-07.html" },
            { title: "彎曲時空的直覺：從二維曲面到四維時空", url: "topics/big-bang/lesson-08.html" },
            { title: "度規張量：怎麼測量彎曲時空裡的距離", url: "topics/big-bang/lesson-09.html" },
            { title: "【數學工具箱】張量與指標記號的基本語言", url: "topics/big-bang/lesson-10.html" },
            { title: "曲率、測地線與重力的幾何本質", url: "topics/big-bang/lesson-11.html" },
            { title: "應力-能量張量：物質怎麼告訴時空要怎麼彎曲", url: "topics/big-bang/lesson-12.html" },
            { title: "愛因斯坦場方程式：完整的物理意義與各項解讀", url: "topics/big-bang/lesson-13.html" }
          ]
        },
        {
          title: "模組 C｜FRW度規與弗里德曼方程式完整推導",
          courses: [
            { title: "宇宙學原理：均勻與均向性的假設", url: "topics/big-bang/lesson-14.html" },
            { title: "FRW度規：描述膨脹宇宙的時空幾何", url: "topics/big-bang/lesson-15.html" },
            { title: "完整推導弗里德曼方程式（一）：把FRW度規代入場方程式", url: "topics/big-bang/lesson-16.html" },
            { title: "完整推導弗里德曼方程式（二）：加速度方程式與流體方程式", url: "topics/big-bang/lesson-17.html" },
            { title: "紅移與尺度因子：怎麼從光的波長推算宇宙膨脹了多少", url: "topics/big-bang/lesson-18.html" },
            { title: "模組總結：從愛因斯坦方程式到宇宙膨脹的完整數學鏈", url: "topics/big-bang/lesson-19.html" }
          ]
        },
        {
          title: "模組 D｜宇宙的成分與弗里德曼方程式的解",
          courses: [
            { title: "物態方程式：輻射、物質、暗能量的不同行為", url: "topics/big-bang/lesson-20.html" },
            { title: "完整推導輻射主導期的尺度因子解", url: "topics/big-bang/lesson-21.html" },
            { title: "完整推導物質主導期的尺度因子解", url: "topics/big-bang/lesson-22.html" },
            { title: "密度參數與宇宙的幾何：開放、封閉還是平坦", url: "topics/big-bang/lesson-23.html" },
            { title: "模組總結：一張圖看懂宇宙膨脹史", url: "topics/big-bang/lesson-24.html" }
          ]
        },
        {
          title: "模組 E｜大霹靂核合成：早期宇宙的核子物理",
          courses: [
            { title: "早期宇宙的熱力學：溫度與時間的關係", url: "topics/big-bang/lesson-25.html" },
            { title: "中子質子比與弱交互作用凍結", url: "topics/big-bang/lesson-26.html" },
            { title: "完整推導氘瓶頸：為什麼核合成要等到特定溫度才開始", url: "topics/big-bang/lesson-27.html" },
            { title: "氦、鋰的豐度預測與觀測驗證", url: "topics/big-bang/lesson-28.html" },
            { title: "模組總結：核合成如何成為大霹靂理論最有力的證據之一", url: "topics/big-bang/lesson-29.html" }
          ]
        },
        {
          title: "模組 F｜宇宙微波背景輻射：宇宙的第一道光",
          courses: [
            { title: "復合時期：宇宙從電漿變透明的關鍵時刻", url: "topics/big-bang/lesson-30.html" },
            { title: "完整推導黑體輻射譜：為什麼CMB是完美的黑體", url: "topics/big-bang/lesson-31.html" },
            { title: "溫度各向異性：CMB圖上的微小起伏", url: "topics/big-bang/lesson-32.html" },
            { title: "聲學震盪：早期宇宙的「聲波」如何烙印在CMB上", url: "topics/big-bang/lesson-33.html" },
            { title: "功率頻譜：從COBE到普朗克衛星的精密測量", url: "topics/big-bang/lesson-34.html" },
            { title: "模組總結：讀懂宇宙的嬰兒照", url: "topics/big-bang/lesson-35.html" }
          ]
        },
        {
          title: "模組 G｜標準模型時間線：從普朗克時間到重子生成",
          courses: [
            { title: "普朗克時期：物理定律失效的邊界", url: "topics/big-bang/lesson-36.html" },
            { title: "大一統時期：強力與電弱力分道揚鑣", url: "topics/big-bang/lesson-37.html" },
            { title: "電弱對稱破缺：希格斯機制賦予質量的瞬間", url: "topics/big-bang/lesson-38.html" },
            { title: "夸克時期：奈秒尺度的夸克膠子電漿", url: "topics/big-bang/lesson-39.html" },
            { title: "夸克-強子相變：從自由夸克到質子中子的禁閉", url: "topics/big-bang/lesson-40.html" },
            { title: "輕子時期與微中子退耦", url: "topics/big-bang/lesson-41.html" },
            { title: "重子生成之謎：沙卡洛夫條件與正反物質不對稱", url: "topics/big-bang/lesson-42.html" },
            { title: "模組總結：完整時間線，從10⁻⁴³秒到38萬年", url: "topics/big-bang/lesson-43.html" }
          ]
        },
        {
          title: "模組 H｜宇宙暴脹理論：解決視界、平坦性與磁單極問題",
          courses: [
            { title: "視界問題：為什麼遙遠兩端的宇宙溫度會一樣", url: "topics/big-bang/lesson-44.html" },
            { title: "平坦性問題：為什麼宇宙的密度這麼接近臨界值", url: "topics/big-bang/lesson-45.html" },
            { title: "磁單極問題：大一統理論的副作用與觀測缺席", url: "topics/big-bang/lesson-46.html" },
            { title: "暴脹子場：一個純量場如何驅動指數膨脹", url: "topics/big-bang/lesson-47.html" },
            { title: "完整推導慢滾近似：暴脹子場的運動方程式", url: "topics/big-bang/lesson-48.html" },
            { title: "e-folding數：暴脹要持續多久才能解決三大問題", url: "topics/big-bang/lesson-49.html" },
            { title: "模組總結：暴脹理論如何一次解決三個謎題", url: "topics/big-bang/lesson-50.html" }
          ]
        },
        {
          title: "模組 I｜暴脹的證據與觀測驗證",
          courses: [
            { title: "量子漲落：暴脹如何播下星系形成的種子", url: "topics/big-bang/lesson-51.html" },
            { title: "純量微擾與張量微擾：CMB功率頻譜的預測", url: "topics/big-bang/lesson-52.html" },
            { title: "B模偏振：尋找原初重力波的證據", url: "topics/big-bang/lesson-53.html" },
            { title: "模組總結：暴脹理論目前的證據與尚未解決的爭議", url: "topics/big-bang/lesson-54.html" }
          ]
        },
        {
          title: "模組 J｜暗物質與暗能量：宇宙加速膨脹的推手",
          courses: [
            { title: "星系旋轉曲線：暗物質最早的證據", url: "topics/big-bang/lesson-55.html" },
            { title: "重力透鏡與子彈星系團：暗物質存在的多重證據", url: "topics/big-bang/lesson-56.html" },
            { title: "暗物質候選者：從WIMP到軸子", url: "topics/big-bang/lesson-57.html" },
            { title: "第Ia型超新星：發現宇宙加速膨脹", url: "topics/big-bang/lesson-58.html" },
            { title: "宇宙常數與狀態方程式：暗能量的兩種理解方式", url: "topics/big-bang/lesson-59.html" },
            { title: "模組總結：ΛCDM模型，一個由95%未知成分主導的宇宙", url: "topics/big-bang/lesson-60.html" }
          ]
        },
        {
          title: "模組 K｜大霹靂之前：量子宇宙學與開放問題",
          courses: [
            { title: "奇異點定理：彭羅斯與霍金證明了什麼", url: "topics/big-bang/lesson-61.html" },
            { title: "為什麼奇異點意味著廣義相對論的失效", url: "topics/big-bang/lesson-62.html" },
            { title: "哈妥-霍金無邊界假說：宇宙沒有「開始」的邊界？", url: "topics/big-bang/lesson-63.html" },
            { title: "永恆暴脹與多重宇宙：一個推測性但嚴肅的理論", url: "topics/big-bang/lesson-64.html" },
            { title: "迴圈量子宇宙學：用大反彈取代大霹靂奇異點", url: "topics/big-bang/lesson-65.html" },
            { title: "模組總結：誠實面對「大爆炸之前」這個問題的科學現狀", url: "topics/big-bang/lesson-66.html" }
          ]
        },
        {
          title: "模組 L｜課程總結",
          courses: [
            { title: "課程總結：從奧伯斯悖論到量子宇宙學的完整旅程", url: "topics/big-bang/lesson-67.html" }
          ]
        }
      ]
    },
    {
      id: "lord-of-the-rings",
      category: "fantasy",
      title: "魔戒與中土世界：從創世神話到王者歸來的完整解析",
      description:
        "從托爾金的創世神話《精靈寶鑽》出發，完整解析中土世界的宇宙觀、種族與第一、二紀元的英雄傳說，逐章深度導讀《哈比人》與《魔戒》三部曲全部劇情，橫向剖析死亡、權力、友誼等核心主題與托爾金的寫作技藝，最後收束於第四紀元的尾聲與文化影響——這是中土世界從創世到終章的完整旅程。",
      icon: "💍",
      url: "topics/lord-of-the-rings/index.html",
      modules: [
        {
          title: "模組 A｜托爾金與中土世界的誕生",
          courses: [
            { title: "托爾金生平：語言學家與戰爭倖存者", url: "topics/lord-of-the-rings/lesson-01.html" },
            { title: "造世先於造史：語言學如何催生一整個世界", url: "topics/lord-of-the-rings/lesson-02.html" },
            { title: "《哈比人》到《魔戒》：中土世界的出版史", url: "topics/lord-of-the-rings/lesson-03.html" },
            { title: "中土世界文本體系導覽：精靈寶鑽、未完成的故事與附錄", url: "topics/lord-of-the-rings/lesson-04.html" }
          ]
        },
        {
          title: "模組 B｜創世神話：埃努林達列與眾神降臨",
          courses: [
            { title: "一如：埃努大樂章與世界的創造", url: "topics/lord-of-the-rings/lesson-05.html" },
            { title: "維拉：亞爾達的守護神", url: "topics/lord-of-the-rings/lesson-06.html" },
            { title: "麥雅與伊斯塔力：五巫師的起源", url: "topics/lord-of-the-rings/lesson-07.html" },
            { title: "米爾寇的不協和音：第一個惡的起源", url: "topics/lord-of-the-rings/lesson-08.html" },
            { title: "模組總結：中土世界的宇宙觀全圖", url: "topics/lord-of-the-rings/lesson-09.html" }
          ]
        },
        {
          title: "模組 C｜精靈紀元的黃金時代與費艾諾的墮落",
          courses: [
            { title: "精靈的甦醒：庫維因恩湖畔的第一批子民", url: "topics/lord-of-the-rings/lesson-10.html" },
            { title: "維林諾的黃金時代與精靈寶鑽的鑄造", url: "topics/lord-of-the-rings/lesson-11.html" },
            { title: "費艾諾：最偉大也最危險的精靈", url: "topics/lord-of-the-rings/lesson-12.html" },
            { title: "兩聖樹之死與米爾寇對精靈寶鑽的竊取", url: "topics/lord-of-the-rings/lesson-13.html" },
            { title: "費艾諾的誓言：諾多族的放逐與冰灣屠殺", url: "topics/lord-of-the-rings/lesson-14.html" },
            { title: "模組總結：驕傲與誓言如何啟動一整個紀元的悲劇", url: "topics/lord-of-the-rings/lesson-15.html" }
          ]
        },
        {
          title: "模組 D｜貝爾蘭的戰爭與英雄悲劇",
          courses: [
            { title: "貝爾蘭地理與精靈諸王國", url: "topics/lord-of-the-rings/lesson-16.html" },
            { title: "眾星之戰與聯合軍勢之戰", url: "topics/lord-of-the-rings/lesson-17.html" },
            { title: "貝倫與露西恩：跨越生死的愛情傳說", url: "topics/lord-of-the-rings/lesson-18.html" },
            { title: "胡林之子圖林（一）：詛咒下的少年英雄", url: "topics/lord-of-the-rings/lesson-19.html" },
            { title: "胡林之子圖林（二）：尼奴爾的悲劇終局", url: "topics/lord-of-the-rings/lesson-20.html" },
            { title: "剛多林的陷落與圖爾的逃亡", url: "topics/lord-of-the-rings/lesson-21.html" },
            { title: "埃雅仁迪爾的航行與憤怒之戰", url: "topics/lord-of-the-rings/lesson-22.html" },
            { title: "模組總結：貝爾蘭的沉沒與第一紀元的終結", url: "topics/lord-of-the-rings/lesson-23.html" }
          ]
        },
        {
          title: "模組 E｜第二紀元：努曼諾爾與力量之戒",
          courses: [
            { title: "努曼諾爾的建立：人類的黃金時代", url: "topics/lord-of-the-rings/lesson-24.html" },
            { title: "精靈的力量之戒與凱勒布理鵬的工藝", url: "topics/lord-of-the-rings/lesson-25.html" },
            { title: "安納塔爾：索倫的偽裝與至尊魔戒的鑄造", url: "topics/lord-of-the-rings/lesson-26.html" },
            { title: "精靈與索倫之戰、瑞文戴爾的建立", url: "topics/lord-of-the-rings/lesson-27.html" },
            { title: "努曼諾爾的驕傲、阿爾-法拉聯與世界的變形", url: "topics/lord-of-the-rings/lesson-28.html" },
            { title: "最後聯盟：吉爾加拉德與埃蘭迪爾對索倫之戰", url: "topics/lord-of-the-rings/lesson-29.html" },
            { title: "模組總結：第二紀元如何埋下魔戒的伏筆", url: "topics/lord-of-the-rings/lesson-30.html" }
          ]
        },
        {
          title: "模組 F｜第三紀元前傳：通往魔戒的路",
          courses: [
            { title: "剛鐸與亞爾諾：埃蘭迪爾之子的雙王國", url: "topics/lord-of-the-rings/lesson-31.html" },
            { title: "安格瑪巫王與北方王國的滅亡", url: "topics/lord-of-the-rings/lesson-32.html" },
            { title: "白色議會、戒靈的甦醒與多爾哥多的陰影", url: "topics/lord-of-the-rings/lesson-33.html" },
            { title: "咕嚕與史麥戈：至尊魔戒五百年的下落", url: "topics/lord-of-the-rings/lesson-34.html" },
            { title: "索倫重返魔多、五巫師的角色分野", url: "topics/lord-of-the-rings/lesson-35.html" },
            { title: "模組總結：第三紀元的舞台如何搭建完成", url: "topics/lord-of-the-rings/lesson-36.html" }
          ]
        },
        {
          title: "模組 G｜中土世界的種族與文化深度解析",
          courses: [
            { title: "精靈：不朽者的分支、命運與海之思念", url: "topics/lord-of-the-rings/lesson-37.html" },
            { title: "矮人：七祖、王國與都靈一族的興衰", url: "topics/lord-of-the-rings/lesson-38.html" },
            { title: "哈比人：夏爾的日常與被忽視的堅韌", url: "topics/lord-of-the-rings/lesson-39.html" },
            { title: "人類：努曼諾爾人、洛汗人與野人的分野", url: "topics/lord-of-the-rings/lesson-40.html" },
            { title: "半獸人、食人妖：魔苟斯與索倫的造物", url: "topics/lord-of-the-rings/lesson-41.html" },
            { title: "樹人與中土的自然力量、伊斯塔力的使命", url: "topics/lord-of-the-rings/lesson-42.html" },
            { title: "模組總結：自由民族聯盟的意義", url: "topics/lord-of-the-rings/lesson-43.html" }
          ]
        },
        {
          title: "模組 H｜《哈比人》全書深度導讀",
          courses: [
            { title: "意外的聚會：比爾博與十三矮人", url: "topics/lord-of-the-rings/lesson-44.html" },
            { title: "巨怪、瑞文戴爾與迷霧山脈的險境", url: "topics/lord-of-the-rings/lesson-45.html" },
            { title: "咕嚕與魔戒：黑暗中的謎語遊戲", url: "topics/lord-of-the-rings/lesson-46.html" },
            { title: "比爾博的轉變：從竊賊到英雄", url: "topics/lord-of-the-rings/lesson-47.html" },
            { title: "幽暗密林、荒山與史矛革之死", url: "topics/lord-of-the-rings/lesson-48.html" },
            { title: "五軍之戰與比爾博的返鄉", url: "topics/lord-of-the-rings/lesson-49.html" },
            { title: "模組總結：《哈比人》如何為《魔戒》鋪路", url: "topics/lord-of-the-rings/lesson-50.html" }
          ]
        },
        {
          title: "模組 I｜《魔戒現身》上部：夏爾到瑞文戴爾",
          courses: [
            { title: "夏爾的寧靜與比爾博的告別派對", url: "topics/lord-of-the-rings/lesson-51.html" },
            { title: "佛羅多啟程：黑騎士的追逐", url: "topics/lord-of-the-rings/lesson-52.html" },
            { title: "老林、湯姆·龐巴迪與墳丘岡的古墓屍妖", url: "topics/lord-of-the-rings/lesson-53.html" },
            { title: "躍馬旅店與神秘的行者", url: "topics/lord-of-the-rings/lesson-54.html" },
            { title: "風雲頂之夜：佛羅多負傷", url: "topics/lord-of-the-rings/lesson-55.html" },
            { title: "模組總結：瑞文戴爾與埃爾隆德會議的前奏", url: "topics/lord-of-the-rings/lesson-56.html" }
          ]
        },
        {
          title: "模組 J｜《魔戒現身》下部：遠征隊與凱薩督姆",
          courses: [
            { title: "埃爾隆德會議：魔戒的真相與同盟的形成", url: "topics/lord-of-the-rings/lesson-57.html" },
            { title: "魔戒遠征隊的組成", url: "topics/lord-of-the-rings/lesson-58.html" },
            { title: "卡蘭拉斯山與抉擇：進入摩瑞亞", url: "topics/lord-of-the-rings/lesson-59.html" },
            { title: "凱薩督姆之橋：甘道夫與炎魔的對決", url: "topics/lord-of-the-rings/lesson-60.html" },
            { title: "羅斯洛立安：凱蘭崔爾的贈禮與魔鏡", url: "topics/lord-of-the-rings/lesson-61.html" },
            { title: "模組總結：遠征隊的裂解與波羅莫之死", url: "topics/lord-of-the-rings/lesson-62.html" }
          ]
        },
        {
          title: "模組 K｜《雙城奇謀》上部：分裂的遠征隊與洛汗",
          courses: [
            { title: "波羅莫之死與遠征隊的分裂", url: "topics/lord-of-the-rings/lesson-63.html" },
            { title: "梅里與皮聘：半獸人的俘虜與法貢森林", url: "topics/lord-of-the-rings/lesson-64.html" },
            { title: "樹鬍與樹人的甦醒", url: "topics/lord-of-the-rings/lesson-65.html" },
            { title: "亞拉岡、金靂與勒苟拉斯：追蹤與重逢甘道夫", url: "topics/lord-of-the-rings/lesson-66.html" },
            { title: "洛汗的黃金大廳：巫毒之舌與希優頓王的甦醒", url: "topics/lord-of-the-rings/lesson-67.html" },
            { title: "模組總結：聖盔谷之戰前夕", url: "topics/lord-of-the-rings/lesson-68.html" }
          ]
        },
        {
          title: "模組 L｜《雙城奇謀》下部：山姆佛羅多、咕嚕與艾辛格",
          courses: [
            { title: "聖盔谷之戰", url: "topics/lord-of-the-rings/lesson-69.html" },
            { title: "艾辛格的陷落與薩魯曼的末路", url: "topics/lord-of-the-rings/lesson-70.html" },
            { title: "佛羅多、山姆與咕嚕：死亡沼澤的旅程", url: "topics/lord-of-the-rings/lesson-71.html" },
            { title: "咕嚕的馴服與雙重人格", url: "topics/lord-of-the-rings/lesson-72.html" },
            { title: "西力斯昂哥爾與屍羅的巢穴", url: "topics/lord-of-the-rings/lesson-73.html" },
            { title: "模組總結：山姆的抉擇與佛羅多被俘", url: "topics/lord-of-the-rings/lesson-74.html" }
          ]
        },
        {
          title: "模組 M｜《王者再臨》上部：剛鐸圍城與帕蘭諾平原之戰",
          courses: [
            { title: "山姆營救佛羅多：奧克塔之塔", url: "topics/lord-of-the-rings/lesson-75.html" },
            { title: "剛鐸的召喚：烽火傳訊與皮聘的效忠", url: "topics/lord-of-the-rings/lesson-76.html" },
            { title: "米那斯提力斯的圍城", url: "topics/lord-of-the-rings/lesson-77.html" },
            { title: "死者之路：亞拉岡與死靈大軍", url: "topics/lord-of-the-rings/lesson-78.html" },
            { title: "帕蘭諾平原之戰：洛汗騎兵的到來與希優頓之死", url: "topics/lord-of-the-rings/lesson-79.html" },
            { title: "模組總結：伊歐玟與梅里對戒靈王的一擊", url: "topics/lord-of-the-rings/lesson-80.html" }
          ]
        },
        {
          title: "模組 N｜《王者再臨》下部：末日火山與王者歸來",
          courses: [
            { title: "剛鐸的抉擇：黑門之役的佯攻", url: "topics/lord-of-the-rings/lesson-81.html" },
            { title: "佛羅多與山姆：末日山的最後路程", url: "topics/lord-of-the-rings/lesson-82.html" },
            { title: "咕嚕的最後掙扎與魔戒的毀滅", url: "topics/lord-of-the-rings/lesson-83.html" },
            { title: "索倫的崩潰與中土世界的解放", url: "topics/lord-of-the-rings/lesson-84.html" },
            { title: "亞拉岡加冕：王者歸來", url: "topics/lord-of-the-rings/lesson-85.html" },
            { title: "模組總結：從夏爾之子到中土之王的完整旅程", url: "topics/lord-of-the-rings/lesson-86.html" }
          ]
        },
        {
          title: "模組 O｜主題深度剖析",
          courses: [
            { title: "死亡與永生：精靈與人類的贈禮", url: "topics/lord-of-the-rings/lesson-87.html" },
            { title: "權力與腐化：魔戒作為文學象徵", url: "topics/lord-of-the-rings/lesson-88.html" },
            { title: "小人物的偉大：哈比人與英雄主義的重新定義", url: "topics/lord-of-the-rings/lesson-89.html" },
            { title: "友誼與犧牲：夥伴情誼的力量", url: "topics/lord-of-the-rings/lesson-90.html" },
            { title: "環境與工業：夏爾、艾辛格與托爾金的生態關懷", url: "topics/lord-of-the-rings/lesson-91.html" },
            { title: "模組總結：貫穿中土世界的核心命題", url: "topics/lord-of-the-rings/lesson-92.html" }
          ]
        },
        {
          title: "模組 P｜托爾金的寫作技藝",
          courses: [
            { title: "發明語言與地名學：精靈語背後的邏輯", url: "topics/lord-of-the-rings/lesson-93.html" },
            { title: "附錄的秘密：時間線與被忽略的細節", url: "topics/lord-of-the-rings/lesson-94.html" },
            { title: "伏筆與呼應：從《哈比人》到《王者再臨》", url: "topics/lord-of-the-rings/lesson-95.html" },
            { title: "模組總結：托爾金如何建構一個「真實」的世界", url: "topics/lord-of-the-rings/lesson-96.html" }
          ]
        },
        {
          title: "模組 Q｜第四紀元與尾聲",
          courses: [
            { title: "夏爾的整肅：哈比人的成長與家鄉之戰", url: "topics/lord-of-the-rings/lesson-97.html" },
            { title: "灰港岸：精靈的離去與魔戒使者的贈禮", url: "topics/lord-of-the-rings/lesson-98.html" },
            { title: "第四紀元：人類世界的開始", url: "topics/lord-of-the-rings/lesson-99.html" },
            { title: "模組總結：中土世界故事的終章", url: "topics/lord-of-the-rings/lesson-100.html" }
          ]
        },
        {
          title: "模組 R｜文化影響與現代改編",
          courses: [
            { title: "托爾金的文學遺產：現代奇幻文學的奠基者", url: "topics/lord-of-the-rings/lesson-101.html" },
            { title: "彼得傑克森電影三部曲：忠實與取捨", url: "topics/lord-of-the-rings/lesson-102.html" },
            { title: "模組總結：托爾金學術與粉絲文化", url: "topics/lord-of-the-rings/lesson-103.html" }
          ]
        },
        {
          title: "模組 S｜課程總結",
          courses: [
            { title: "課程總結：從埃努大樂章到王者歸來的完整旅程", url: "topics/lord-of-the-rings/lesson-104.html" }
          ]
        }
      ]
    },
    {
      id: "warcraft",
      category: "games",
      title: "魔獸世界：從創世神話到巫妖王殞落的完整編年史",
      description:
        "從艾澤拉斯的泰坦創世神話、古神的甦醒、太古之戰與大分裂講起，完整梳理獸人與人類的三次大戰（《魔獸爭霸》I、II、III 戰役），深入阿薩斯王子墮落成巫妖王的核心悲劇，一路走到《魔獸世界》經典、燃燒的遠征、巫妖王之怒——直到艾薩斯在冰冠堡壘殞落的完整編年史。",
      icon: "⚔️",
      url: "topics/warcraft/index.html",
      modules: [
        {
          title: "模組 A｜魔獸系列導覽與創作背景",
          courses: [
            { title: "暴雪娛樂與魔獸系列的誕生", url: "topics/warcraft/lesson-01.html" },
            { title: "從RTS到MMO：三個時代的敘事轉變", url: "topics/warcraft/lesson-02.html" },
            { title: "艾澤拉斯的宇宙觀導覽", url: "topics/warcraft/lesson-03.html" },
            { title: "時間線與紀元劃分", url: "topics/warcraft/lesson-04.html" }
          ]
        },
        {
          title: "模組 B｜泰坦創世神話：宇宙與艾澤拉斯的誕生",
          courses: [
            { title: "虛空與偉大的黑暗之外", url: "topics/warcraft/lesson-05.html" },
            { title: "泰坦的甦醒與艾澤拉斯世界靈魂", url: "topics/warcraft/lesson-06.html" },
            { title: "泰坦守護者的誕生與艾澤拉斯的整備", url: "topics/warcraft/lesson-07.html" },
            { title: "五大巨龍聖盟的授權", url: "topics/warcraft/lesson-08.html" },
            { title: "模組總結：泰坦神話的完整圖景", url: "topics/warcraft/lesson-09.html" }
          ]
        },
        {
          title: "模組 C｜古神的甦醒與泰坦守護者的征服",
          courses: [
            { title: "古神：克蘇恩與夥伴們的黑暗低語", url: "topics/warcraft/lesson-10.html" },
            { title: "永恆之戰：泰坦對古神的鎮壓", url: "topics/warcraft/lesson-11.html" },
            { title: "巨魔帝國的興起", url: "topics/warcraft/lesson-12.html" },
            { title: "模組總結", url: "topics/warcraft/lesson-13.html" }
          ]
        },
        {
          title: "模組 D｜永恆之井與暗夜精靈的黃金時代",
          courses: [
            { title: "永恆之井的魔法起源", url: "topics/warcraft/lesson-14.html" },
            { title: "卡多雷帝國與艾薩拉女王", url: "topics/warcraft/lesson-15.html" },
            { title: "神秘法師議會的成立", url: "topics/warcraft/lesson-16.html" },
            { title: "瑪法里恩與泰蘭德：德魯伊教義的起源", url: "topics/warcraft/lesson-17.html" },
            { title: "模組總結", url: "topics/warcraft/lesson-18.html" }
          ]
        },
        {
          title: "模組 E｜燃燒軍團首次入侵：太古之戰",
          courses: [
            { title: "薩格拉斯與燃燒軍團的野心", url: "topics/warcraft/lesson-19.html" },
            { title: "艾薩拉女王的野心與入侵之門", url: "topics/warcraft/lesson-20.html" },
            { title: "伊利丹的雙生：瑪法里恩之弟的抉擇", url: "topics/warcraft/lesson-21.html" },
            { title: "諸神一戰：薩格拉斯的封印", url: "topics/warcraft/lesson-22.html" },
            { title: "模組總結", url: "topics/warcraft/lesson-23.html" }
          ]
        },
        {
          title: "模組 F｜大分裂：艾澤拉斯大陸的破碎",
          courses: [
            { title: "永恆之井的崩潰與大分裂", url: "topics/warcraft/lesson-24.html" },
            { title: "瑪爾斯特隆的誕生與暗夜精靈的凡人化", url: "topics/warcraft/lesson-25.html" },
            { title: "上層精靈流亡與那伽的誕生", url: "topics/warcraft/lesson-26.html" },
            { title: "模組總結", url: "topics/warcraft/lesson-27.html" }
          ]
        },
        {
          title: "模組 G｜德拉諾的獸人：薩滿信仰與惡魔血液的墮落",
          courses: [
            { title: "德拉諾的獸人氏族與元素信仰", url: "topics/warcraft/lesson-28.html" },
            { title: "德萊尼的抵達與衝突", url: "topics/warcraft/lesson-29.html" },
            { title: "古爾丹與基爾加丹的操縱", url: "topics/warcraft/lesson-30.html" },
            { title: "惡魔之血：獸人的墮落", url: "topics/warcraft/lesson-31.html" },
            { title: "模組總結", url: "topics/warcraft/lesson-32.html" }
          ]
        },
        {
          title: "模組 H｜第一次戰爭：黑暗之門開啟",
          courses: [
            { title: "黑暗之門的開啟與獸人的入侵", url: "topics/warcraft/lesson-33.html" },
            { title: "萊恩國王之死與暴風城的陷落", url: "topics/warcraft/lesson-34.html" },
            { title: "洛薩的撤退：倖存者的長征", url: "topics/warcraft/lesson-35.html" },
            { title: "模組總結", url: "topics/warcraft/lesson-36.html" }
          ]
        },
        {
          title: "模組 I｜第二次戰爭：部落與聯盟的全面對抗",
          courses: [
            { title: "聯盟的成立與獸人的擴張", url: "topics/warcraft/lesson-37.html" },
            { title: "卡格拉爾與制海權之戰", url: "topics/warcraft/lesson-38.html" },
            { title: "杜隆坦之死與奧格瑞姆接掌部落", url: "topics/warcraft/lesson-39.html" },
            { title: "模組總結：獸人的敗亡與集中營", url: "topics/warcraft/lesson-40.html" }
          ]
        },
        {
          title: "模組 J｜第三次戰爭：薩爾與新部落的誕生",
          courses: [
            { title: "薩爾的覺醒與逃離集中營", url: "topics/warcraft/lesson-41.html" },
            { title: "先知梅迪夫的指引", url: "topics/warcraft/lesson-42.html" },
            { title: "卡加斯的抉擇：燃燒之刃氏族的清算", url: "topics/warcraft/lesson-43.html" },
            { title: "新家園：杜隆塔爾的建立", url: "topics/warcraft/lesson-44.html" },
            { title: "模組總結", url: "topics/warcraft/lesson-45.html" }
          ]
        },
        {
          title: "模組 K｜第三次戰爭：阿薩斯的墮落",
          courses: [
            { title: "瘟疫的初現與斯坦索姆的抉擇", url: "topics/warcraft/lesson-46.html" },
            { title: "霜之哀傷：阿薩斯與冰霜寶劍的契約", url: "topics/warcraft/lesson-47.html" },
            { title: "弒父：洛丹倫的陷落", url: "topics/warcraft/lesson-48.html" },
            { title: "阿薩斯與吉安娜的訣別", url: "topics/warcraft/lesson-49.html" },
            { title: "死亡騎士的誕生", url: "topics/warcraft/lesson-50.html" },
            { title: "模組總結：一個王子如何成為怪物", url: "topics/warcraft/lesson-51.html" }
          ]
        },
        {
          title: "模組 L｜第三次戰爭：暗夜精靈與海加爾山之戰",
          courses: [
            { title: "瑪法里恩的甦醒與伊利丹的釋放", url: "topics/warcraft/lesson-52.html" },
            { title: "燃燒軍團的登陸", url: "topics/warcraft/lesson-53.html" },
            { title: "海加爾山防衛戰：三大種族首次聯手", url: "topics/warcraft/lesson-54.html" },
            { title: "阿克蒙德之死", url: "topics/warcraft/lesson-55.html" },
            { title: "模組總結", url: "topics/warcraft/lesson-56.html" }
          ]
        },
        {
          title: "模組 M｜冰封王座：伊利丹的放逐與復仇",
          courses: [
            { title: "背叛的代價：伊利丹被放逐外域", url: "topics/warcraft/lesson-57.html" },
            { title: "瓦許姬與納迦的結盟", url: "topics/warcraft/lesson-58.html" },
            { title: "凱爾薩斯與血精靈的墮落", url: "topics/warcraft/lesson-59.html" },
            { title: "黑暗神殿的建立", url: "topics/warcraft/lesson-60.html" },
            { title: "模組總結", url: "topics/warcraft/lesson-61.html" }
          ]
        },
        {
          title: "模組 N｜冰封王座：阿薩斯與新任巫妖王",
          courses: [
            { title: "阿薩斯與奈奧祖：兩個怨靈的合而為一", url: "topics/warcraft/lesson-62.html" },
            { title: "冰封王座的鎔鑄", url: "topics/warcraft/lesson-63.html" },
            { title: "巫妖王對抗伊利丹", url: "topics/warcraft/lesson-64.html" },
            { title: "克爾蘇加德的復活", url: "topics/warcraft/lesson-65.html" },
            { title: "模組總結：巫妖王的統治開始", url: "topics/warcraft/lesson-66.html" }
          ]
        },
        {
          title: "模組 O｜大災變前夕：部落聯盟格局底定",
          courses: [
            { title: "瓦里安烏瑞恩失蹤與暴風城的重建", url: "topics/warcraft/lesson-67.html" },
            { title: "薩爾成為部落大酋長", url: "topics/warcraft/lesson-68.html" },
            { title: "模組總結：邁向世界之戰的舞台", url: "topics/warcraft/lesson-69.html" }
          ]
        },
        {
          title: "模組 P｜魔獸世界經典：奧妮克希亞、安其拉與納克薩瑪斯",
          courses: [
            { title: "黑龍公主的陰謀：奧妮克希亞的偽裝", url: "topics/warcraft/lesson-70.html" },
            { title: "灰谷之戰：部落聯盟正式開戰", url: "topics/warcraft/lesson-71.html" },
            { title: "安其拉之門：克蘇恩的威脅", url: "topics/warcraft/lesson-72.html" },
            { title: "納克薩瑪斯與克爾蘇加德的巫妖王棋局", url: "topics/warcraft/lesson-73.html" },
            { title: "模組總結", url: "topics/warcraft/lesson-74.html" }
          ]
        },
        {
          title: "模組 Q｜燃燒的遠征：外域與黑暗神殿",
          courses: [
            { title: "黑暗之門重啟：遠征外域", url: "topics/warcraft/lesson-75.html" },
            { title: "伊利丹的統治與黑暗神殿的攻略", url: "topics/warcraft/lesson-76.html" },
            { title: "凱爾薩斯的背叛與太陽井的爭奪", url: "topics/warcraft/lesson-77.html" },
            { title: "光輝之願號：伊利丹的最終戰", url: "topics/warcraft/lesson-78.html" },
            { title: "太陽井的淨化", url: "topics/warcraft/lesson-79.html" },
            { title: "模組總結", url: "topics/warcraft/lesson-80.html" }
          ]
        },
        {
          title: "模組 R｜巫妖王之怒：北裂境遠征與阿薩斯的終局",
          courses: [
            { title: "天災入侵：死亡騎士的覺醒", url: "topics/warcraft/lesson-81.html" },
            { title: "北裂境登陸與部落聯盟的競逐", url: "topics/warcraft/lesson-82.html" },
            { title: "血色十字軍與遺忘者的復仇", url: "topics/warcraft/lesson-83.html" },
            { title: "風暴峭壁：亡靈天災的核心", url: "topics/warcraft/lesson-84.html" },
            { title: "冰冠堡壘的圍攻", url: "topics/warcraft/lesson-85.html" },
            { title: "巫妖王的最終戰：泰瑞納斯之魂的低語", url: "topics/warcraft/lesson-86.html" },
            { title: "博瓦爾弗塔根成為新任巫妖王", url: "topics/warcraft/lesson-87.html" },
            { title: "模組總結：一個時代的終結", url: "topics/warcraft/lesson-88.html" }
          ]
        },
        {
          title: "模組 S｜課程總結",
          courses: [
            { title: "課程總結：從泰坦創世到巫妖王殞落的完整旅程", url: "topics/warcraft/lesson-89.html" }
          ]
        }
      ]
    },
    {
      id: "starcraft",
      category: "games",
      title: "星海爭霸：從星靈起源到虛空之遺的完整戰史",
      description:
        "從最古老的星靈宇宙觀與艾蒙的墮落講起，完整梳理《星海爭霸》原版三大種族戰役、《母巢之戰》資料片，一路走到《星海爭霸II》三部曲——自由之翼、蟲群之心、虛空之遺——的完整劇情，並收錄《新星秘密行動》等外傳故事，橫向剖析三個種族的敘事風格與凱瑞甘的角色弧光。",
      icon: "🛸",
      url: "topics/starcraft/index.html",
      modules: [
        {
          title: "模組 A｜星海爭霸系列導覽與創作背景",
          courses: [
            { title: "暴雪娛樂與星海爭霸的誕生", url: "topics/starcraft/lesson-01.html" },
            { title: "三個種族的敘事結構：為何獨特", url: "topics/starcraft/lesson-02.html" },
            { title: "系列時間線與版本沿革", url: "topics/starcraft/lesson-03.html" },
            { title: "文本體系導覽", url: "topics/starcraft/lesson-04.html" }
          ]
        },
        {
          title: "模組 B｜宇宙觀：星靈、艾蒙的墮落與蟲群的起源",
          courses: [
            { title: "星靈：宇宙中最古老的種族", url: "topics/starcraft/lesson-05.html" },
            { title: "純化與吞噬：星靈對待凡種的兩種道路", url: "topics/starcraft/lesson-06.html" },
            { title: "艾蒙的墮落：黑暗之聲的誕生", url: "topics/starcraft/lesson-07.html" },
            { title: "大群體意識與蟲群的創造", url: "topics/starcraft/lesson-08.html" },
            { title: "模組總結", url: "topics/starcraft/lesson-09.html" }
          ]
        },
        {
          title: "模組 C｜人類：聯邦到殖民地的建立背景",
          courses: [
            { title: "地球的過度擁擠與流放船隊", url: "topics/starcraft/lesson-10.html" },
            { title: "科普魯魯星區的殖民與聯邦的建立", url: "topics/starcraft/lesson-11.html" },
            { title: "高壓統治：聯邦的暗面", url: "topics/starcraft/lesson-12.html" },
            { title: "模組總結", url: "topics/starcraft/lesson-13.html" }
          ]
        },
        {
          title: "模組 D｜星海爭霸原版：人類戰役",
          courses: [
            { title: "邊陲叛軍：吉姆·雷諾與馬薩拉星", url: "topics/starcraft/lesson-14.html" },
            { title: "蟲族入侵與聯邦的崩潰", url: "topics/starcraft/lesson-15.html" },
            { title: "阿克圖魯斯·孟斯克與科拉爾之子", url: "topics/starcraft/lesson-16.html" },
            { title: "莎拉·凱瑞甘的犧牲", url: "topics/starcraft/lesson-17.html" },
            { title: "新任皇帝的誕生：孟斯克的背叛", url: "topics/starcraft/lesson-18.html" },
            { title: "模組總結", url: "topics/starcraft/lesson-19.html" }
          ]
        },
        {
          title: "模組 E｜星海爭霸原版：蟲族戰役",
          courses: [
            { title: "大群體意識：統治者的低語", url: "topics/starcraft/lesson-20.html" },
            { title: "凱瑞甘的感染與蛻變", url: "topics/starcraft/lesson-21.html" },
            { title: "首席執行官與腦蟲的階層", url: "topics/starcraft/lesson-22.html" },
            { title: "神族聖地艾爾的淪陷", url: "topics/starcraft/lesson-23.html" },
            { title: "模組總結", url: "topics/starcraft/lesson-24.html" }
          ]
        },
        {
          title: "模組 F｜星海爭霸原版：神族戰役",
          courses: [
            { title: "神族社會：階級、議會與黑暗聖堂", url: "topics/starcraft/lesson-25.html" },
            { title: "塔薩達爾與長老議會的決裂", url: "topics/starcraft/lesson-26.html" },
            { title: "淨化艾爾：絕望的抉擇", url: "topics/starcraft/lesson-27.html" },
            { title: "澤拉圖與黑暗聖堂武士的復仇", url: "topics/starcraft/lesson-28.html" },
            { title: "模組總結", url: "topics/starcraft/lesson-29.html" }
          ]
        },
        {
          title: "模組 G｜母巢之戰：聯合地球指揮部的入侵",
          courses: [
            { title: "雷諾遊擊隊與新聯邦", url: "topics/starcraft/lesson-30.html" },
            { title: "聯合地球指揮部：地球的鐵腕統治", url: "topics/starcraft/lesson-31.html" },
            { title: "杜加爾上將的野心與地球艦隊的征服", url: "topics/starcraft/lesson-32.html" },
            { title: "三方角力下的脆弱聯盟", url: "topics/starcraft/lesson-33.html" },
            { title: "模組總結", url: "topics/starcraft/lesson-34.html" }
          ]
        },
        {
          title: "模組 H｜母巢之戰：蟲群女王的復仇",
          courses: [
            { title: "凱瑞甘的背叛與蟲后的誕生", url: "topics/starcraft/lesson-35.html" },
            { title: "大群體意識的毀滅", url: "topics/starcraft/lesson-36.html" },
            { title: "三方混戰：地球、蟲群與神族", url: "topics/starcraft/lesson-37.html" },
            { title: "凱瑞甘一統蟲群", url: "topics/starcraft/lesson-38.html" },
            { title: "模組總結", url: "topics/starcraft/lesson-39.html" }
          ]
        },
        {
          title: "模組 I｜母巢之戰：神族的流亡與重生",
          courses: [
            { title: "艾爾的最終淪陷", url: "topics/starcraft/lesson-40.html" },
            { title: "大遷徙：逃向沙拉克絲", url: "topics/starcraft/lesson-41.html" },
            { title: "塔薩達爾的犧牲", url: "topics/starcraft/lesson-42.html" },
            { title: "澤拉圖與黑暗聖堂武士的復仇", url: "topics/starcraft/lesson-43.html" },
            { title: "模組總結：星海爭霸原版的完整落幕", url: "topics/starcraft/lesson-44.html" }
          ]
        },
        {
          title: "模組 J｜自由之翼：雷諾遊擊隊與凱瑞甘的救贖",
          courses: [
            { title: "四年後：雷諾的沉淪", url: "topics/starcraft/lesson-45.html" },
            { title: "莫比斯基金會與異種神器的線索", url: "topics/starcraft/lesson-46.html" },
            { title: "海伯利安號的旅程", url: "topics/starcraft/lesson-47.html" },
            { title: "淨化蟲群：莫比斯基金會的真正計畫", url: "topics/starcraft/lesson-48.html" },
            { title: "去感染凱瑞甘的抉擇", url: "topics/starcraft/lesson-49.html" },
            { title: "尾聲：新的威脅浮現", url: "topics/starcraft/lesson-50.html" },
            { title: "模組總結", url: "topics/starcraft/lesson-51.html" }
          ]
        },
        {
          title: "模組 K｜蟲群之心：凱瑞甘的回歸與復仇",
          courses: [
            { title: "凱瑞甘的囚禁與逃亡", url: "topics/starcraft/lesson-52.html" },
            { title: "重新奪回蟲群：進化的力量", url: "topics/starcraft/lesson-53.html" },
            { title: "對孟斯克的復仇", url: "topics/starcraft/lesson-54.html" },
            { title: "戰場上的盟友與犧牲", url: "topics/starcraft/lesson-55.html" },
            { title: "混合體的初次現身", url: "topics/starcraft/lesson-56.html" },
            { title: "凱瑞甘重新蛻變為蟲后", url: "topics/starcraft/lesson-57.html" },
            { title: "模組總結", url: "topics/starcraft/lesson-58.html" }
          ]
        },
        {
          title: "模組 L｜虛空之遺：神族的最終聖戰",
          courses: [
            { title: "亞塔尼斯與神族的分裂", url: "topics/starcraft/lesson-59.html" },
            { title: "卡拉的重建與神族大團結", url: "topics/starcraft/lesson-60.html" },
            { title: "艾丹之矛：奪回艾爾", url: "topics/starcraft/lesson-61.html" },
            { title: "深入虛空：艾蒙的真面目", url: "topics/starcraft/lesson-62.html" },
            { title: "三大種族的最終聯盟", url: "topics/starcraft/lesson-63.html" },
            { title: "艾蒙的殞落", url: "topics/starcraft/lesson-64.html" },
            { title: "尾聲：新紀元的開端", url: "topics/starcraft/lesson-65.html" },
            { title: "模組總結", url: "topics/starcraft/lesson-66.html" }
          ]
        },
        {
          title: "模組 M｜外傳：新星秘密行動與其他故事",
          courses: [
            { title: "新星：幽靈計畫的道德灰色地帶", url: "topics/starcraft/lesson-67.html" },
            { title: "秘密行動三部曲摘要", url: "topics/starcraft/lesson-68.html" },
            { title: "其他外傳小說與短篇概覽", url: "topics/starcraft/lesson-69.html" },
            { title: "模組總結", url: "topics/starcraft/lesson-70.html" }
          ]
        },
        {
          title: "模組 N｜主題與寫作技藝深度剖析",
          courses: [
            { title: "三個種族，三種敘事風格", url: "topics/starcraft/lesson-71.html" },
            { title: "凱瑞甘的角色弧光：從人類到蟲后到救贖", url: "topics/starcraft/lesson-72.html" },
            { title: "家人、犧牲與忠誠：貫穿全系列的情感核心", url: "topics/starcraft/lesson-73.html" },
            { title: "電子競技與星海爭霸的文化地位", url: "topics/starcraft/lesson-74.html" },
            { title: "模組總結", url: "topics/starcraft/lesson-75.html" }
          ]
        },
        {
          title: "模組 O｜課程總結",
          courses: [
            { title: "課程總結：從星靈創世到虛空之遺的完整旅程", url: "topics/starcraft/lesson-76.html" }
          ]
        }
      ]
    },
    {
      id: "networking",
      category: "tech",
      title: "網路服務架構與原理：從電纜訊號到自架站台的完整旅程",
      description:
        "從OSI/TCP-IP分層模型與實體訊號講起，完整解析乙太網路怎麼區分你我的訊號、IP路由與TCP傳輸的運作機制、資料中心的真實樣貌，逐步拆解一次HTTP請求從輸入網址到畫面出現的完整生命週期，深入HTTPS加密、網頁伺服器架構與Docker容器技術，最後親自動手用Docker把網站架上線，並收錄微服務、Kubernetes、SDN等現代雲端網路架構專題。",
      icon: "🌐",
      url: "topics/networking/index.html",
      modules: [
        {
          title: "模組 A｜網路是什麼：分層模型與基礎概念",
          courses: [
            { title: "OSI七層模型 vs TCP/IP四層模型", url: "topics/networking/lesson-01.html" },
            { title: "封裝與解封裝：資料如何一層層包裝", url: "topics/networking/lesson-02.html" },
            { title: "為什麼要分層：模組化設計的智慧", url: "topics/networking/lesson-03.html" },
            { title: "課程地圖：從電纜訊號到瀏覽器畫面的完整旅程", url: "topics/networking/lesson-04.html" }
          ]
        },
        {
          title: "模組 B｜實體層：訊號如何在電纜與空氣中傳遞",
          courses: [
            { title: "位元如何變成電壓、光或無線電波", url: "topics/networking/lesson-05.html" },
            { title: "雙絞線、同軸電纜、光纖的差異", url: "topics/networking/lesson-06.html" },
            { title: "多工技術：分時、分頻、分碼怎麼讓大家共用一條線", url: "topics/networking/lesson-07.html" },
            { title: "乙太網路實體層的演進：從Hub到現代網路", url: "topics/networking/lesson-08.html" },
            { title: "模組總結", url: "topics/networking/lesson-09.html" }
          ]
        },
        {
          title: "模組 C｜資料鏈結層：MAC位址與區域網路交換",
          courses: [
            { title: "MAC位址：每張網卡獨一無二的身分證", url: "topics/networking/lesson-10.html" },
            { title: "集線器 vs 交換器：為什麼你的訊號不會被隔壁看到", url: "topics/networking/lesson-11.html" },
            { title: "CSMA/CD與碰撞網域", url: "topics/networking/lesson-12.html" },
            { title: "VLAN：如何在同一台交換器上隔離不同群組", url: "topics/networking/lesson-13.html" },
            { title: "模組總結", url: "topics/networking/lesson-14.html" }
          ]
        },
        {
          title: "模組 D｜網路層：IP位址與路由",
          courses: [
            { title: "IP位址的結構：網路位址與主機位址", url: "topics/networking/lesson-15.html" },
            { title: "子網路遮罩與CIDR", url: "topics/networking/lesson-16.html" },
            { title: "路由器如何決定封包的下一步", url: "topics/networking/lesson-17.html" },
            { title: "NAT：為什麼你家很多設備能共用一個公網IP", url: "topics/networking/lesson-18.html" },
            { title: "模組總結：IPv4耗盡與IPv6", url: "topics/networking/lesson-19.html" }
          ]
        },
        {
          title: "模組 E｜傳輸層：TCP與UDP的可靠與快速之爭",
          courses: [
            { title: "連接埠：同一台機器怎麼同時處理多個服務", url: "topics/networking/lesson-20.html" },
            { title: "TCP三向交握：連線建立的完整過程", url: "topics/networking/lesson-21.html" },
            { title: "TCP的可靠傳輸機制：確認、重傳、視窗控制", url: "topics/networking/lesson-22.html" },
            { title: "UDP：犧牲可靠換取速度", url: "topics/networking/lesson-23.html" },
            { title: "模組總結：壅塞控制與協定選擇", url: "topics/networking/lesson-24.html" }
          ]
        },
        {
          title: "模組 F｜資料中心：網際網路的骨幹",
          courses: [
            { title: "資料中心裡面到底有什麼：機櫃、電力與散熱", url: "topics/networking/lesson-25.html" },
            { title: "骨幹網路與網際網路交換中心(IXP)", url: "topics/networking/lesson-26.html" },
            { title: "CDN：把內容送到離你最近的地方", url: "topics/networking/lesson-27.html" },
            { title: "資料中心的備援與高可用性設計", url: "topics/networking/lesson-28.html" },
            { title: "模組總結", url: "topics/networking/lesson-29.html" }
          ]
        },
        {
          title: "模組 G｜從輸入網址到畫面出現：完整請求生命週期",
          courses: [
            { title: "DNS解析：網域名稱怎麼變成IP位址", url: "topics/networking/lesson-30.html" },
            { title: "建立TCP連線與TLS交握", url: "topics/networking/lesson-31.html" },
            { title: "HTTP請求的組成與發送", url: "topics/networking/lesson-32.html" },
            { title: "伺服器端處理請求的完整流程", url: "topics/networking/lesson-33.html" },
            { title: "瀏覽器接收回應、渲染網頁", url: "topics/networking/lesson-34.html" },
            { title: "模組總結：整合時間軸全覽", url: "topics/networking/lesson-35.html" }
          ]
        },
        {
          title: "模組 H｜HTTP協定深度解析",
          courses: [
            { title: "HTTP方法、狀態碼與標頭", url: "topics/networking/lesson-36.html" },
            { title: "HTTP/1.1、HTTP/2、HTTP/3的演進", url: "topics/networking/lesson-37.html" },
            { title: "Cookie與Session：網站如何記住你", url: "topics/networking/lesson-38.html" },
            { title: "快取機制：瀏覽器與伺服器怎麼省流量", url: "topics/networking/lesson-39.html" },
            { title: "模組總結", url: "topics/networking/lesson-40.html" }
          ]
        },
        {
          title: "模組 I｜HTTPS與網路安全基礎",
          courses: [
            { title: "為什麼需要加密：中間人攻擊的風險", url: "topics/networking/lesson-41.html" },
            { title: "對稱加密與非對稱加密", url: "topics/networking/lesson-42.html" },
            { title: "TLS交握完整流程", url: "topics/networking/lesson-43.html" },
            { title: "憑證與憑證頒發機構(CA)：如何信任一個網站", url: "topics/networking/lesson-44.html" },
            { title: "模組總結：常見網路攻擊手法概覽", url: "topics/networking/lesson-45.html" }
          ]
        },
        {
          title: "模組 J｜網頁伺服器架構",
          courses: [
            { title: "靜態內容 vs 動態內容", url: "topics/networking/lesson-46.html" },
            { title: "Web伺服器(nginx/Apache)的角色", url: "topics/networking/lesson-47.html" },
            { title: "反向代理與負載平衡", url: "topics/networking/lesson-48.html" },
            { title: "應用程式伺服器與資料庫的分工", url: "topics/networking/lesson-49.html" },
            { title: "模組總結：三層式架構全貌", url: "topics/networking/lesson-50.html" }
          ]
        },
        {
          title: "模組 K｜虛擬化與容器技術：Docker基礎",
          courses: [
            { title: "為什麼需要虛擬化：從實體機到虛擬機", url: "topics/networking/lesson-51.html" },
            { title: "容器 vs 虛擬機的本質差異", url: "topics/networking/lesson-52.html" },
            { title: "Docker核心概念：映像檔、容器、Dockerfile", url: "topics/networking/lesson-53.html" },
            { title: "Docker指令與常用工作流程", url: "topics/networking/lesson-54.html" },
            { title: "Docker Compose：多容器服務編排", url: "topics/networking/lesson-55.html" },
            { title: "模組總結", url: "topics/networking/lesson-56.html" }
          ]
        },
        {
          title: "模組 L｜動手架站：從零到上線",
          courses: [
            { title: "選擇你的伺服器：VPS、雲端主機、家用主機", url: "topics/networking/lesson-57.html" },
            { title: "用Docker部署一個簡單網站", url: "topics/networking/lesson-58.html" },
            { title: "網域名稱與DNS設定", url: "topics/networking/lesson-59.html" },
            { title: "申請並設定HTTPS憑證(Let's Encrypt)", url: "topics/networking/lesson-60.html" },
            { title: "模組總結：上線後的監控與維運基礎", url: "topics/networking/lesson-61.html" }
          ]
        },
        {
          title: "模組 M｜進階主題：現代網路與雲端架構",
          courses: [
            { title: "雲端運算的服務模式：IaaS、PaaS、SaaS", url: "topics/networking/lesson-62.html" },
            { title: "BGP與網際網路的骨幹路由：ISP之間怎麼互聯", url: "topics/networking/lesson-63.html" },
            { title: "現代資料中心網路拓撲：Spine-Leaf架構", url: "topics/networking/lesson-64.html" },
            { title: "軟體定義網路(SDN)：控制平面與資料平面的分離", url: "topics/networking/lesson-65.html" },
            { title: "微服務架構：從單體應用到服務拆分", url: "topics/networking/lesson-66.html" },
            { title: "API閘道與服務網格(Service Mesh)", url: "topics/networking/lesson-67.html" },
            { title: "容器編排：Kubernetes核心概念", url: "topics/networking/lesson-68.html" },
            { title: "無伺服器運算(Serverless)與事件驅動架構", url: "topics/networking/lesson-69.html" },
            { title: "全球負載平衡與邊緣運算(Edge Computing)", url: "topics/networking/lesson-70.html" },
            { title: "模組總結：現代網路架構全貌", url: "topics/networking/lesson-71.html" }
          ]
        },
        {
          title: "模組 N｜課程總結",
          courses: [
            { title: "課程總結：從電纜訊號到雲端架構的完整旅程", url: "topics/networking/lesson-72.html" }
          ]
        }
      ]
    },
    {
      id: "marvel-mcu",
      category: "fantasy",
      title: "漫威電影宇宙：從復仇者集結到多元宇宙的完整英雄誌",
      description:
        "以漫威電影宇宙（MCU）為主軸，逐部解析無限傳奇（第一至第三階段）與多元宇宙傳奇（第四、五階段）所有電影與影集的完整劇情，並透過角色專題深度介紹復仇者聯盟核心成員、蜘蛛人的世界、銀河守護者、黑豹家族、洛基與時間變異管理局等所有在電影裡出現過的重要角色，最後收錄漫畫原作宇宙（地球616）的補充篇，介紹電影與漫畫分歧之處。",
      icon: "🦸",
      url: "topics/marvel-mcu/index.html",
      modules: [
        {
          title: "模組 A｜MCU導覽：電影宇宙的誕生與敘事結構",
          courses: [
            { title: "漫威影業的誕生與共享宇宙的實驗", url: "topics/marvel-mcu/lesson-01.html" },
            { title: "無限傳奇 vs 多元宇宙傳奇：兩大敘事弧", url: "topics/marvel-mcu/lesson-02.html" },
            { title: "電影與影集的關係：Disney+如何改變敘事方式", url: "topics/marvel-mcu/lesson-03.html" },
            { title: "課程地圖：故事線與角色深度解析雙軌並行", url: "topics/marvel-mcu/lesson-04.html" }
          ]
        },
        {
          title: "模組 B｜第一階段：復仇者聯盟的集結",
          courses: [
            { title: "鋼鐵人：一個軍火商的自我救贖", url: "topics/marvel-mcu/lesson-05.html" },
            { title: "無敵浩克", url: "topics/marvel-mcu/lesson-06.html" },
            { title: "鋼鐵人2：軍備與私心", url: "topics/marvel-mcu/lesson-07.html" },
            { title: "雷神索爾：阿斯嘉王子的放逐", url: "topics/marvel-mcu/lesson-08.html" },
            { title: "美國隊長：復仇者先鋒", url: "topics/marvel-mcu/lesson-09.html" },
            { title: "復仇者聯盟：集結完成", url: "topics/marvel-mcu/lesson-10.html" }
          ]
        },
        {
          title: "模組 C｜第二階段：個體與集體的裂痕",
          courses: [
            { title: "鋼鐵人3：創傷後的鋼鐵人", url: "topics/marvel-mcu/lesson-11.html" },
            { title: "雷神索爾2：黑暗世界", url: "topics/marvel-mcu/lesson-12.html" },
            { title: "美國隊長2：酷寒戰士", url: "topics/marvel-mcu/lesson-13.html" },
            { title: "星際異攻隊：宇宙的新面孔", url: "topics/marvel-mcu/lesson-14.html" },
            { title: "復仇者聯盟2：奧創紀元", url: "topics/marvel-mcu/lesson-15.html" },
            { title: "蟻人：最小的英雄", url: "topics/marvel-mcu/lesson-16.html" }
          ]
        },
        {
          title: "模組 D｜第三階段（上）：內戰與新戰力加入",
          courses: [
            { title: "美國隊長3：英雄內戰", url: "topics/marvel-mcu/lesson-17.html" },
            { title: "奇異博士：魔法的介入", url: "topics/marvel-mcu/lesson-18.html" },
            { title: "星際異攻隊2", url: "topics/marvel-mcu/lesson-19.html" },
            { title: "蜘蛛人：返校日", url: "topics/marvel-mcu/lesson-20.html" },
            { title: "雷神索爾3：諸神黃昏", url: "topics/marvel-mcu/lesson-21.html" },
            { title: "黑豹：瓦干達的覺醒", url: "topics/marvel-mcu/lesson-22.html" },
            { title: "模組總結", url: "topics/marvel-mcu/lesson-23.html" }
          ]
        },
        {
          title: "模組 E｜第三階段（下）：無限之戰到終局之戰",
          courses: [
            { title: "復仇者聯盟3：無限之戰", url: "topics/marvel-mcu/lesson-24.html" },
            { title: "蟻人與黃蜂女", url: "topics/marvel-mcu/lesson-25.html" },
            { title: "驚奇隊長", url: "topics/marvel-mcu/lesson-26.html" },
            { title: "復仇者聯盟4：終局之戰", url: "topics/marvel-mcu/lesson-27.html" },
            { title: "蜘蛛人：離家日", url: "topics/marvel-mcu/lesson-28.html" },
            { title: "模組總結：無限傳奇的完整落幕", url: "topics/marvel-mcu/lesson-29.html" }
          ]
        },
        {
          title: "模組 F｜第四階段：多元宇宙傳奇的開端",
          courses: [
            { title: "汪達幻視：悲傷催生的異常", url: "topics/marvel-mcu/lesson-30.html" },
            { title: "獵鷹與酷寒戰士", url: "topics/marvel-mcu/lesson-31.html" },
            { title: "洛基：時間變異管理局", url: "topics/marvel-mcu/lesson-32.html" },
            { title: "黑寡婦", url: "topics/marvel-mcu/lesson-33.html" },
            { title: "尚氣與十環傳奇", url: "topics/marvel-mcu/lesson-34.html" },
            { title: "永恆族", url: "topics/marvel-mcu/lesson-35.html" },
            { title: "蜘蛛人：無家日", url: "topics/marvel-mcu/lesson-36.html" },
            { title: "奇異博士2與雷神索爾4：多元宇宙的代價", url: "topics/marvel-mcu/lesson-37.html" }
          ]
        },
        {
          title: "模組 G｜第五階段：新的威脅浮現",
          courses: [
            { title: "蟻人與黃蜂女：量子狂熱", url: "topics/marvel-mcu/lesson-38.html" },
            { title: "星際異攻隊3", url: "topics/marvel-mcu/lesson-39.html" },
            { title: "驚奇隊長2與新世代英雄", url: "topics/marvel-mcu/lesson-40.html" },
            { title: "死侍與金鋼狼", url: "topics/marvel-mcu/lesson-41.html" },
            { title: "雷霆特工隊", url: "topics/marvel-mcu/lesson-42.html" },
            { title: "模組總結：康的時代", url: "topics/marvel-mcu/lesson-43.html" }
          ]
        },
        {
          title: "模組 H｜復仇者聯盟核心七人",
          courses: [
            { title: "鋼鐵人東尼史塔克：天才、創傷與犧牲", url: "topics/marvel-mcu/lesson-44.html" },
            { title: "美國隊長史蒂夫羅傑斯：時代錯位的理想主義者", url: "topics/marvel-mcu/lesson-45.html" },
            { title: "雷神索爾：從傲慢王子到真正的英雄", url: "topics/marvel-mcu/lesson-46.html" },
            { title: "浩克布魯斯班納：雙重人格的和解", url: "topics/marvel-mcu/lesson-47.html" },
            { title: "黑寡婦娜塔莎：贖罪的一生", url: "topics/marvel-mcu/lesson-48.html" },
            { title: "鷹眼克林特：凡人英雄", url: "topics/marvel-mcu/lesson-49.html" },
            { title: "神盾局與尼克福瑞：幕後的操盤手", url: "topics/marvel-mcu/lesson-50.html" }
          ]
        },
        {
          title: "模組 I｜復仇者聯盟二代成員與神盾局盟友",
          courses: [
            { title: "幻視：人工智慧與人性的追尋", url: "topics/marvel-mcu/lesson-51.html" },
            { title: "汪達：緋紅女巫的誕生", url: "topics/marvel-mcu/lesson-52.html" },
            { title: "戰爭機器羅德斯", url: "topics/marvel-mcu/lesson-53.html" },
            { title: "獵鷹山姆威爾森：新任美國隊長", url: "topics/marvel-mcu/lesson-54.html" },
            { title: "巴奇：酷寒戰士到白狼", url: "topics/marvel-mcu/lesson-55.html" },
            { title: "瑪莉亞希爾與神盾局幹員群像", url: "topics/marvel-mcu/lesson-56.html" }
          ]
        },
        {
          title: "模組 J｜阿斯嘉眾神：雷神的世界",
          courses: [
            { title: "女武神：瓦爾基麗的救贖", url: "topics/marvel-mcu/lesson-57.html" },
            { title: "海姆達爾與阿斯嘉守護者", url: "topics/marvel-mcu/lesson-58.html" },
            { title: "奧丁與弗麗嘉：王室的秘密", url: "topics/marvel-mcu/lesson-59.html" },
            { title: "科爾格與阿斯嘉遺民", url: "topics/marvel-mcu/lesson-60.html" }
          ]
        },
        {
          title: "模組 K｜蜘蛛人的世界",
          courses: [
            { title: "彼得帕克：鄰家英雄的成長", url: "topics/marvel-mcu/lesson-61.html" },
            { title: "MJ與彼得的感情線", url: "topics/marvel-mcu/lesson-62.html" },
            { title: "奈德、梅嬸與荷根：帕克的支持系統", url: "topics/marvel-mcu/lesson-63.html" },
            { title: "禿鷹與反派們：街頭英雄的敵人", url: "topics/marvel-mcu/lesson-64.html" },
            { title: "模組總結", url: "topics/marvel-mcu/lesson-65.html" }
          ]
        },
        {
          title: "模組 L｜銀河守護者全員解析",
          courses: [
            { title: "星爵：從地球混混到宇宙英雄", url: "topics/marvel-mcu/lesson-66.html" },
            { title: "卡魔拉與德克斯", url: "topics/marvel-mcu/lesson-67.html" },
            { title: "火箭與格魯特", url: "topics/marvel-mcu/lesson-68.html" },
            { title: "星雲、螳螂與亞當戰士", url: "topics/marvel-mcu/lesson-69.html" },
            { title: "索恩與薩諾斯家族的悲劇", url: "topics/marvel-mcu/lesson-70.html" }
          ]
        },
        {
          title: "模組 M｜奇異博士、黑豹與瓦干達",
          courses: [
            { title: "奇異博士史傳奇：傲慢與救贖", url: "topics/marvel-mcu/lesson-71.html" },
            { title: "王：卡瑪泰姬的守護者", url: "topics/marvel-mcu/lesson-72.html" },
            { title: "克莉絲汀與美洲隊長：多元宇宙的新血", url: "topics/marvel-mcu/lesson-73.html" },
            { title: "黑豹家族：蘇睿與帝查拉", url: "topics/marvel-mcu/lesson-74.html" },
            { title: "歐克伊、娜奇雅與朵拉米拉潔", url: "topics/marvel-mcu/lesson-75.html" },
            { title: "M巴庫與拉蒙妲王太后", url: "topics/marvel-mcu/lesson-76.html" }
          ]
        },
        {
          title: "模組 N｜驚奇隊長、尚氣與永恆族：新世代英雄",
          courses: [
            { title: "驚奇隊長卡蘿丹佛斯", url: "topics/marvel-mcu/lesson-77.html" },
            { title: "莫妮卡蘭波與驚奇少女卡蜜拉", url: "topics/marvel-mcu/lesson-78.html" },
            { title: "尚氣與徐夏靈", url: "topics/marvel-mcu/lesson-79.html" },
            { title: "文武：十環傳奇的真相", url: "topics/marvel-mcu/lesson-80.html" },
            { title: "永恆族全員解析", url: "topics/marvel-mcu/lesson-81.html" },
            { title: "模組總結", url: "topics/marvel-mcu/lesson-82.html" }
          ]
        },
        {
          title: "模組 O｜蟻人、女浩克與月光騎士：Disney+英雄群像",
          courses: [
            { title: "史考特朗恩與霍普：蟻人與黃蜂女", url: "topics/marvel-mcu/lesson-83.html" },
            { title: "珍妮特與漢克皮姆", url: "topics/marvel-mcu/lesson-84.html" },
            { title: "女浩克珍妮佛沃特斯", url: "topics/marvel-mcu/lesson-85.html" },
            { title: "月光騎士馬克史貝特", url: "topics/marvel-mcu/lesson-86.html" }
          ]
        },
        {
          title: "模組 P｜X戰警與多元宇宙新勢力",
          courses: [
            { title: "X戰警如何進入MCU：多元宇宙的橋樑", url: "topics/marvel-mcu/lesson-87.html" },
            { title: "神奇四超人的加入", url: "topics/marvel-mcu/lesson-88.html" },
            { title: "死侍與金鋼狼：多元宇宙的清道夫", url: "topics/marvel-mcu/lesson-89.html" },
            { title: "模組總結", url: "topics/marvel-mcu/lesson-90.html" }
          ]
        },
        {
          title: "模組 Q｜洛基的世界與時間變異管理局",
          courses: [
            { title: "洛基：從反派到變異體管理者", url: "topics/marvel-mcu/lesson-91.html" },
            { title: "莫比亞斯：TVA的執法者", url: "topics/marvel-mcu/lesson-92.html" },
            { title: "希薇：另一個洛基變體", url: "topics/marvel-mcu/lesson-93.html" },
            { title: "芮絲蕾娜法官與「他一直存在」", url: "topics/marvel-mcu/lesson-94.html" },
            { title: "模組總結", url: "topics/marvel-mcu/lesson-95.html" }
          ]
        },
        {
          title: "模組 R｜雷霆特工隊：反派轉正的英雄們",
          courses: [
            { title: "葉蓮娜與紅衛士", url: "topics/marvel-mcu/lesson-96.html" },
            { title: "幽靈與美國特工", url: "topics/marvel-mcu/lesson-97.html" },
            { title: "模組總結", url: "topics/marvel-mcu/lesson-98.html" }
          ]
        },
        {
          title: "模組 S｜大反派全覽：薩諾斯、齊爾蒙格與康",
          courses: [
            { title: "薩諾斯的哲學：滅霸的滅世邏輯", url: "topics/marvel-mcu/lesson-99.html" },
            { title: "齊爾蒙格：正義的另一種面貌", url: "topics/marvel-mcu/lesson-100.html" },
            { title: "康：多元宇宙的征服者", url: "topics/marvel-mcu/lesson-101.html" },
            { title: "模組總結", url: "topics/marvel-mcu/lesson-102.html" }
          ]
        },
        {
          title: "模組 T｜漫畫宇宙補充篇",
          courses: [
            { title: "地球616：漫畫原作與電影的分歧點", url: "topics/marvel-mcu/lesson-103.html" },
            { title: "內戰、無限手套：漫畫版與電影版的差異", url: "topics/marvel-mcu/lesson-104.html" },
            { title: "X戰警與變種人在漫畫裡的漫長歷史", url: "topics/marvel-mcu/lesson-105.html" },
            { title: "秘密戰爭與多元宇宙概念的漫畫起源", url: "topics/marvel-mcu/lesson-106.html" },
            { title: "模組總結", url: "topics/marvel-mcu/lesson-107.html" }
          ]
        },
        {
          title: "模組 U｜課程總結",
          courses: [
            { title: "課程總結：從復仇者集結到多元宇宙的完整英雄誌", url: "topics/marvel-mcu/lesson-108.html" }
          ]
        }
      ]
    },
    {
      id: "fantastic-beasts",
      category: "fantasy",
      title: "神奇動物與葛林戴華德：哈利波特前傳全紀錄",
      description:
        "聚焦「神奇動物」前傳三部曲（2016-2022），以紐特·斯卡曼德的冒險為主線逐部解析劇情，並深入追溯蓋勒·葛林戴華德的崛起、他與少年鄧不利多之間的禁忌情誼、血誓的由來與終結，最後銜接回哈利波特正傳裡那場傳說中的1945年決鬥，補完你所熟悉的魔法世界的另一段身世。",
      icon: "🧳",
      url: "topics/fantastic-beasts/index.html",
      modules: [
        {
          title: "模組 A｜序幕：魔法世界的另一段時空",
          courses: [
            { title: "為什麼哈利波特需要一部「前傳」", url: "topics/fantastic-beasts/lesson-01.html" },
            { title: "時間軸重建：1926年到1998年之間發生了什麼", url: "topics/fantastic-beasts/lesson-02.html" },
            { title: "J.K.羅琳的新身分：從小說家到編劇", url: "topics/fantastic-beasts/lesson-03.html" }
          ]
        },
        {
          title: "模組 B｜紐特·斯卡曼德：與神奇動物為伍的人",
          courses: [
            { title: "赫夫帕夫的怪咖：紐特在霍格華茲的日子", url: "topics/fantastic-beasts/lesson-04.html" },
            { title: "那只神奇的行李箱：紐特的魔法動物保育學", url: "topics/fantastic-beasts/lesson-05.html" },
            { title: "模組總結：一個不太像英雄的英雄", url: "topics/fantastic-beasts/lesson-06.html" }
          ]
        },
        {
          title: "模組 C｜神奇動物在哪裡：1926紐約大冒險",
          courses: [
            { title: "開場：一只逃脫的行李箱與一位麻雞", url: "topics/fantastic-beasts/lesson-07.html" },
            { title: "美國魔法國會：MACUSA與它的高壓統治", url: "topics/fantastic-beasts/lesson-08.html" },
            { title: "新塞冷慈善會：貝爾邦夫人的恐怖育幼院", url: "topics/fantastic-beasts/lesson-09.html" },
            { title: "反常自閉症：什麼是奧不斯克瑞爾", url: "topics/fantastic-beasts/lesson-10.html" },
            { title: "蒂娜與奎妮：戈斯坦姊妹的處境", url: "topics/fantastic-beasts/lesson-11.html" },
            { title: "假面下的葛雷夫斯：波西瓦爾·葛雷夫斯的真實身分", url: "topics/fantastic-beasts/lesson-12.html" },
            { title: "克雷登斯的爆發：紐約上空的黑色風暴", url: "topics/fantastic-beasts/lesson-13.html" },
            { title: "落網：葛林戴華德首度現身與被捕", url: "topics/fantastic-beasts/lesson-14.html" },
            { title: "模組總結：一場屠殺記憶的收尾", url: "topics/fantastic-beasts/lesson-15.html" }
          ]
        },
        {
          title: "模組 D｜蓋勒·葛林戴華德的崛起",
          courses: [
            { title: "都姆斯特朗的天才：葛林戴華德的少年時代", url: "topics/fantastic-beasts/lesson-16.html" },
            { title: "高錐客洞的夏天：與年輕鄧不利多相遇", url: "topics/fantastic-beasts/lesson-17.html" },
            { title: "為了更大的利益：兩個年輕人的危險理想", url: "topics/fantastic-beasts/lesson-18.html" },
            { title: "尋找死神的聖物：三聖物的誘惑", url: "topics/fantastic-beasts/lesson-19.html" },
            { title: "模組總結：一段友誼如何走向決裂的邊緣", url: "topics/fantastic-beasts/lesson-20.html" }
          ]
        },
        {
          title: "模組 E｜鄧不利多家族的傷痕",
          courses: [
            { title: "阿蕊安娜·鄧不利多：一個被隱藏的妹妹", url: "topics/fantastic-beasts/lesson-21.html" },
            { title: "那場三人決鬥：阿蕊安娜之死的真相與謎團", url: "topics/fantastic-beasts/lesson-22.html" },
            { title: "血誓：阿不福思、阿不思與葛林戴華德的約定", url: "topics/fantastic-beasts/lesson-23.html" },
            { title: "模組總結：鄧不利多終生無法擺脫的愧疚", url: "topics/fantastic-beasts/lesson-24.html" }
          ]
        },
        {
          title: "模組 F｜罪與罰：巴黎的葛林戴華德",
          courses: [
            { title: "越獄：從魔法部押解車上的逃亡", url: "topics/fantastic-beasts/lesson-25.html" },
            { title: "尋找克雷登斯：一場跨海的追蹤", url: "topics/fantastic-beasts/lesson-26.html" },
            { title: "蕾塔·萊斯壯的秘密：一樁換嬰事件", url: "topics/fantastic-beasts/lesson-27.html" },
            { title: "紐特的抉擇：鄧不利多交付的任務", url: "topics/fantastic-beasts/lesson-28.html" },
            { title: "奎妮與雅各：一段被禁止的戀情", url: "topics/fantastic-beasts/lesson-29.html" },
            { title: "巴黎集會：葛林戴華德的演說與預言", url: "topics/fantastic-beasts/lesson-30.html" },
            { title: "蕾塔的犧牲：地下墓穴的訣別", url: "topics/fantastic-beasts/lesson-31.html" },
            { title: "模組總結：一場集會揭露的野心藍圖", url: "topics/fantastic-beasts/lesson-32.html" }
          ]
        },
        {
          title: "模組 G｜血統之謎：克雷登斯是誰",
          courses: [
            { title: "從歐布斯坎特到血緣線索：克雷登斯的身世追查", url: "topics/fantastic-beasts/lesson-33.html" },
            { title: "「你是我的血親」：葛林戴華德的誘惑話術", url: "topics/fantastic-beasts/lesson-34.html" },
            { title: "模組總結：一個關於歸屬感的操弄", url: "topics/fantastic-beasts/lesson-35.html" }
          ]
        },
        {
          title: "模組 H｜鄧不利多的秘密：柏林與不丹的布局",
          courses: [
            { title: "集結：鄧不利多召集的五人小隊", url: "topics/fantastic-beasts/lesson-36.html" },
            { title: "麒麟誕生：不丹的魔法聖獸", url: "topics/fantastic-beasts/lesson-37.html" },
            { title: "選舉之爭：國際巫師聯合會最高理事長之戰", url: "topics/fantastic-beasts/lesson-38.html" },
            { title: "假麒麟：葛林戴華德的死靈法術", url: "topics/fantastic-beasts/lesson-39.html" },
            { title: "雅各的任務：一個麻瓜的臥底工作", url: "topics/fantastic-beasts/lesson-40.html" },
            { title: "賴利·希克斯與邦蒂：新面孔的任務分工", url: "topics/fantastic-beasts/lesson-41.html" },
            { title: "柏林的陷阱：一場刻意設下的騙局", url: "topics/fantastic-beasts/lesson-42.html" },
            { title: "不丹的決選：選舉現場的驚天逆轉", url: "topics/fantastic-beasts/lesson-43.html" },
            { title: "模組總結：這一次，鄧不利多贏了嗎", url: "topics/fantastic-beasts/lesson-44.html" }
          ]
        },
        {
          title: "模組 I｜麒麟與國際巫師聯合會",
          courses: [
            { title: "麒麟的魔法：純潔之心的試煉", url: "topics/fantastic-beasts/lesson-45.html" },
            { title: "國際巫師聯合會：魔法世界的聯合國", url: "topics/fantastic-beasts/lesson-46.html" },
            { title: "模組總結：一場選舉如何決定魔法世界的命運", url: "topics/fantastic-beasts/lesson-47.html" }
          ]
        },
        {
          title: "模組 J｜血誓的終結",
          courses: [
            { title: "打破約定：那只裝著血液的墜飾", url: "topics/fantastic-beasts/lesson-48.html" },
            { title: "直球對決：鄧不利多終於能出手了嗎", url: "topics/fantastic-beasts/lesson-49.html" },
            { title: "紐蒙迦德的高塔：葛林戴華德的最終結局", url: "topics/fantastic-beasts/lesson-50.html" },
            { title: "模組總結：一段仇恨如何劃下（暫時的）句點", url: "topics/fantastic-beasts/lesson-51.html" }
          ]
        },
        {
          title: "模組 K｜銀幕外的故事與課程總結",
          courses: [
            { title: "停在第三部：為什麼「神奇動物」系列沒有拍完", url: "topics/fantastic-beasts/lesson-52.html" },
            { title: "銜接正傳：1945年那場傳說中的決鬥", url: "topics/fantastic-beasts/lesson-53.html" },
            { title: "全課程總結：前傳如何補完了哈利波特的世界觀", url: "topics/fantastic-beasts/lesson-54.html" }
          ]
        }
      ]
    },
    {
      id: "diablo",
      category: "games",
      title: "暗黑破壞神全紀錄：從崔斯特瑞姆到聖休亞瑞的永恆之戰",
      description:
        "從聖休亞瑞的創世神話與天使惡魔的永恆戰爭出發，完整解析暗黑破壞神1、2（毀滅之王資料片）、3（奪魂之鐮資料片）、4四部曲的主線劇情：崔斯特瑞姆的惡夢、黑暗流浪者的墮落、三巨頭與四小魔的興衰、天堂水晶拱頂之戰，直到莉莉絲率領聖休亞瑞邁入嶄新的黑暗時代，最後收錄怨恨之鎧資料片的番外概覽。",
      icon: "👹",
      url: "topics/diablo/index.html",
      modules: [
        {
          title: "模組 A｜序幕：聖休亞瑞的世界觀",
          courses: [
            { title: "天堂與地獄：一場永恆的戰爭", url: "topics/diablo/lesson-01.html" },
            { title: "聖休亞瑞：介於天使與惡魔之間的世界", url: "topics/diablo/lesson-02.html" },
            { title: "七大魔王：三巨頭與四小魔的位階", url: "topics/diablo/lesson-03.html" },
            { title: "涅法雷姆：人類為什麼讓兩方都忌憚", url: "topics/diablo/lesson-04.html" }
          ]
        },
        {
          title: "模組 B｜創世神話：伊納里斯與莉莉絲的禁忌",
          courses: [
            { title: "阿努與塔瑟梅特：創世神話的起源", url: "topics/diablo/lesson-05.html" },
            { title: "伊納里斯：放逐自己的墮落天使", url: "topics/diablo/lesson-06.html" },
            { title: "莉莉絲：墨菲斯托之女的禁忌之戀", url: "topics/diablo/lesson-07.html" },
            { title: "模組總結：一段被隱藏的創世秘史", url: "topics/diablo/lesson-08.html" }
          ]
        },
        {
          title: "模組 C｜暗黑破壞神首部曲：崔斯特瑞姆的惡夢",
          courses: [
            { title: "崔斯特瑞姆小鎮：降臨在寧靜小鎮的災難", url: "topics/diablo/lesson-09.html" },
            { title: "里奧瑞克國王的瘋狂", url: "topics/diablo/lesson-10.html" },
            { title: "大主教拉薩魯斯的背叛", url: "topics/diablo/lesson-11.html" },
            { title: "地下大教堂：深入地底的試煉", url: "topics/diablo/lesson-12.html" },
            { title: "霍拉德林的封印史：三兄弟如何被鎖進靈魂石", url: "topics/diablo/lesson-13.html" },
            { title: "屠夫、黑騎士與地牢裡的試煉者", url: "topics/diablo/lesson-14.html" },
            { title: "大魔王戴布羅：恐懼之王的真面目", url: "topics/diablo/lesson-15.html" },
            { title: "致命的抉擇：將靈魂石刺入自己的額頭", url: "topics/diablo/lesson-16.html" },
            { title: "模組總結：黑暗流浪者的誕生", url: "topics/diablo/lesson-17.html" }
          ]
        },
        {
          title: "模組 D｜霍拉德林教團的秘密史",
          courses: [
            { title: "霍拉迪姆的先知使命", url: "topics/diablo/lesson-18.html" },
            { title: "塔爾拉夏的犧牲與瘋狂", url: "topics/diablo/lesson-19.html" },
            { title: "模組總結：被遺忘在沙漠裡的秘密", url: "topics/diablo/lesson-20.html" }
          ]
        },
        {
          title: "模組 E｜暗黑破壞神II 第一幕：盜賊營地與安達莉爾",
          courses: [
            { title: "二十年後：黑暗流浪者的蹤跡", url: "topics/diablo/lesson-21.html" },
            { title: "盜賊營地：凱夏與亞卡拉", url: "topics/diablo/lesson-22.html" },
            { title: "血鴉的悲劇：曾經的盜賊女王", url: "topics/diablo/lesson-23.html" },
            { title: "焦土修道院與安達莉爾的巢穴", url: "topics/diablo/lesson-24.html" },
            { title: "模組總結：痛苦之王的殞落", url: "topics/diablo/lesson-25.html" }
          ]
        },
        {
          title: "模組 F｜暗黑破壞神II 第二幕：魯高因與杜瑞爾",
          courses: [
            { title: "沙漠中的港口：魯高因城", url: "topics/diablo/lesson-26.html" },
            { title: "亞特瑪與凱恩的線索：霍拉德林的下落", url: "topics/diablo/lesson-27.html" },
            { title: "圖魯斯特神殿的機關與試煉", url: "topics/diablo/lesson-28.html" },
            { title: "塔爾拉夏之墓：杜瑞爾的甦醒", url: "topics/diablo/lesson-29.html" },
            { title: "模組總結：被釋放的戴布羅", url: "topics/diablo/lesson-30.html" }
          ]
        },
        {
          title: "模組 G｜暗黑破壞神II 第三幕：卡拉忠與墨菲斯托",
          courses: [
            { title: "卡拉忠叢林：庫拉斯特的衰敗", url: "topics/diablo/lesson-31.html" },
            { title: "巫毒教與死靈法師的傳說", url: "topics/diablo/lesson-32.html" },
            { title: "強制法球：墨菲斯托的操縱之手", url: "topics/diablo/lesson-33.html" },
            { title: "庫拉斯特議會神殿的決戰", url: "topics/diablo/lesson-34.html" },
            { title: "模組總結：憎恨之王的下場", url: "topics/diablo/lesson-35.html" }
          ]
        },
        {
          title: "模組 H｜暗黑破壞神II 第四幕：地獄之戰與魔王本尊",
          courses: [
            { title: "混沌避難所：泰瑞爾的求援", url: "topics/diablo/lesson-36.html" },
            { title: "天使議會的分裂與掙扎", url: "topics/diablo/lesson-37.html" },
            { title: "混沌聖所：三兄弟的最終團聚", url: "topics/diablo/lesson-38.html" },
            { title: "模組總結：暫時的勝利", url: "topics/diablo/lesson-39.html" }
          ]
        },
        {
          title: "模組 I｜毀滅之王資料片 第五幕：阿瑞特山與巴爾",
          courses: [
            { title: "哈羅蓋特：蠻族的最後堡壘", url: "topics/diablo/lesson-40.html" },
            { title: "巴爾的追擊：世界之石的誘惑", url: "topics/diablo/lesson-41.html" },
            { title: "冰封王座：安雅與蠻族五英雄", url: "topics/diablo/lesson-42.html" },
            { title: "泰瑞爾的抉擇：摧毀世界之石", url: "topics/diablo/lesson-43.html" },
            { title: "模組總結：一個時代的終結", url: "topics/diablo/lesson-44.html" }
          ]
        },
        {
          title: "模組 J｜二十年的寧靜與崩解的預兆",
          courses: [
            { title: "崔斯特瑞姆的重建與流言", url: "topics/diablo/lesson-45.html" },
            { title: "天上墜落的星辰", url: "topics/diablo/lesson-46.html" },
            { title: "模組總結：被喚醒的暗黑三部曲", url: "topics/diablo/lesson-47.html" }
          ]
        },
        {
          title: "模組 K｜暗黑破壞神III 第一幕：崔斯特瑞姆的星辰",
          courses: [
            { title: "莉亞與凱恩：墜星之下的相遇", url: "topics/diablo/lesson-48.html" },
            { title: "舊崔斯特瑞姆大教堂的亡魂", url: "topics/diablo/lesson-49.html" },
            { title: "骷髏王里奧瑞克再臨", url: "topics/diablo/lesson-50.html" },
            { title: "莉亞的秘密：亞德莉亞的真正目的", url: "topics/diablo/lesson-51.html" },
            { title: "模組總結：憂鬱之王的甦醒", url: "topics/diablo/lesson-52.html" }
          ]
        },
        {
          title: "模組 L｜暗黑破壞神III 第二幕：卡爾敦與偽裝的貝利爾",
          courses: [
            { title: "卡爾敦：沙漠中的黃金之城", url: "topics/diablo/lesson-53.html" },
            { title: "哈坎皇帝的真面目", url: "topics/diablo/lesson-54.html" },
            { title: "蛛后的巢穴與大主教的瘋狂", url: "topics/diablo/lesson-55.html" },
            { title: "欺詐之王貝利爾的真身", url: "topics/diablo/lesson-56.html" },
            { title: "模組總結：謊言之王的末路", url: "topics/diablo/lesson-57.html" }
          ]
        },
        {
          title: "模組 M｜暗黑破壞神III 第三幕：城塞之戰與阿祖莫丹",
          courses: [
            { title: "巴斯堤恩要塞：對抗地獄大軍的最後防線", url: "topics/diablo/lesson-58.html" },
            { title: "天空之橋與惡魔大軍的猛攻", url: "topics/diablo/lesson-59.html" },
            { title: "罪孽之王阿祖莫丹的降臨", url: "topics/diablo/lesson-60.html" },
            { title: "模組總結：地獄之門的開啟", url: "topics/diablo/lesson-61.html" }
          ]
        },
        {
          title: "模組 N｜暗黑破壞神III 第四幕：天堂之戰與大魔王的回歸",
          courses: [
            { title: "水晶拱頂：天堂本體的危機", url: "topics/diablo/lesson-62.html" },
            { title: "泰瑞爾的犧牲與墮落天使的覺悟", url: "topics/diablo/lesson-63.html" },
            { title: "大魔王戴布羅：莉亞身軀裡的終極融合", url: "topics/diablo/lesson-64.html" },
            { title: "模組總結：恐懼之王的第二次殞落", url: "topics/diablo/lesson-65.html" }
          ]
        },
        {
          title: "模組 O｜奪魂之鐮資料片：馬爾薩伊爾與死亡天使",
          courses: [
            { title: "智慧天使馬爾薩伊爾的失落", url: "topics/diablo/lesson-66.html" },
            { title: "黑色靈魂石與人類靈魂的浩劫", url: "topics/diablo/lesson-67.html" },
            { title: "韋斯馬奇的淪陷", url: "topics/diablo/lesson-68.html" },
            { title: "潘達莫尼恩要塞的最終決戰", url: "topics/diablo/lesson-69.html" },
            { title: "一個新守護者的誕生", url: "topics/diablo/lesson-70.html" },
            { title: "模組總結：暗黑三部曲故事線的完結", url: "topics/diablo/lesson-71.html" }
          ]
        },
        {
          title: "模組 P｜從天堂到聖休亞瑞：莉莉絲回歸的序章",
          courses: [
            { title: "沉寂的世界：暗黑四部曲前的聖休亞瑞", url: "topics/diablo/lesson-72.html" },
            { title: "光明座堂與莉莉絲信徒的暗中集結", url: "topics/diablo/lesson-73.html" },
            { title: "模組總結：黑暗即將再臨的預兆", url: "topics/diablo/lesson-74.html" }
          ]
        },
        {
          title: "模組 Q｜暗黑破壞神IV：莉莉絲的復仇",
          courses: [
            { title: "開場：血月下的召喚儀式", url: "topics/diablo/lesson-75.html" },
            { title: "唐納神父與復仇者妮瑞兒", url: "topics/diablo/lesson-76.html" },
            { title: "莉莉絲的回歸：憎恨母親的降臨", url: "topics/diablo/lesson-77.html" },
            { title: "卡吉斯坦荒原的動盪", url: "topics/diablo/lesson-78.html" },
            { title: "史卡斯波洛的黑暗低語", url: "topics/diablo/lesson-79.html" },
            { title: "伊納里斯的覺醒與抉擇", url: "topics/diablo/lesson-80.html" },
            { title: "決戰前夕：兵臨光明座堂", url: "topics/diablo/lesson-81.html" },
            { title: "最終戰役：聖休亞瑞的命運抉擇", url: "topics/diablo/lesson-82.html" },
            { title: "模組總結：血脈之王的落幕（暫時的）", url: "topics/diablo/lesson-83.html" }
          ]
        },
        {
          title: "模組 R｜番外：怨恨之鎧資料片與未來展望",
          courses: [
            { title: "納罕圖的呼喚：墨菲斯托的蹤跡", url: "topics/diablo/lesson-84.html" },
            { title: "妮瑞兒的抉擇與憎恨石的下落", url: "topics/diablo/lesson-85.html" },
            { title: "模組總結：暗黑破壞神的故事還沒說完", url: "topics/diablo/lesson-86.html" }
          ]
        },
        {
          title: "模組 S｜課程總結",
          courses: [
            { title: "全課程總結：從崔斯特瑞姆的一場惡夢，到席捲聖休亞瑞的永恆戰爭", url: "topics/diablo/lesson-87.html" }
          ]
        }
      ]
    },
    {
      id: "ios-game-dev",
      category: "tech",
      title: "iOS遊戲開發入門到上架：用Xcode做出你的第一款App Store遊戲",
      description:
        "從零開始學用 Xcode、Swift 與 SpriteKit 開發 iOS 遊戲：實作一款打磚塊風格的休閒益智遊戲，掌握場景管理、物理引擎、碰撞偵測與遊戲狀態機，接著整合 AdMob 廣告與計算收入，最後完整走過 Apple Developer Program 註冊、App Store Connect 設定與審查提交流程。",
      icon: "📱",
      url: "topics/ios-game-dev/index.html",
      modules: [
        {
          title: "模組 A｜起步：認識iOS遊戲開發的世界",
          courses: [
            { title: "蘋果開發生態系總覽：Apple Developer、App Store、iOS版本現況", url: "topics/ios-game-dev/lesson-01.html" },
            { title: "Xcode、Swift、SpriteKit：三個名詞分別是什麼", url: "topics/ios-game-dev/lesson-02.html" },
            { title: "模組總結：這門課要一起做出什麼", url: "topics/ios-game-dev/lesson-03.html" }
          ]
        },
        {
          title: "模組 B｜Swift語言快速上手",
          courses: [
            { title: "變數、常數與基本型別", url: "topics/ios-game-dev/lesson-04.html" },
            { title: "Optional：處理「可能不存在的值」", url: "topics/ios-game-dev/lesson-05.html" },
            { title: "函式與閉包", url: "topics/ios-game-dev/lesson-06.html" },
            { title: "流程控制：條件判斷與迴圈", url: "topics/ios-game-dev/lesson-07.html" },
            { title: "struct與class的差異", url: "topics/ios-game-dev/lesson-08.html" },
            { title: "protocol與擴充功能基礎", url: "topics/ios-game-dev/lesson-09.html" },
            { title: "模組總結：Swift基礎回顧", url: "topics/ios-game-dev/lesson-10.html" }
          ]
        },
        {
          title: "模組 C｜Xcode與SpriteKit環境設置",
          courses: [
            { title: "安裝Xcode與Apple ID登入", url: "topics/ios-game-dev/lesson-11.html" },
            { title: "免費開發者帳號能做到哪裡，付費方案又解鎖了什麼", url: "topics/ios-game-dev/lesson-12.html" },
            { title: "建立你的第一個SpriteKit專案", url: "topics/ios-game-dev/lesson-13.html" },
            { title: "模組總結：Xcode專案結構導覽", url: "topics/ios-game-dev/lesson-14.html" }
          ]
        },
        {
          title: "模組 D｜SpriteKit核心概念",
          courses: [
            { title: "SKScene：遊戲畫面的容器", url: "topics/ios-game-dev/lesson-15.html" },
            { title: "SKNode節點樹：遊戲物件怎麼組織", url: "topics/ios-game-dev/lesson-16.html" },
            { title: "SKSpriteNode：讓圖片動起來", url: "topics/ios-game-dev/lesson-17.html" },
            { title: "座標系統：SpriteKit的座標邏輯", url: "topics/ios-game-dev/lesson-18.html" },
            { title: "模組總結：update與遊戲迴圈", url: "topics/ios-game-dev/lesson-19.html" }
          ]
        },
        {
          title: "模組 E｜觸控與使用者輸入",
          courses: [
            { title: "觸控事件的基本處理", url: "topics/ios-game-dev/lesson-20.html" },
            { title: "手勢辨識器", url: "topics/ios-game-dev/lesson-21.html" },
            { title: "模組總結：把觸控轉換成遊戲動作", url: "topics/ios-game-dev/lesson-22.html" }
          ]
        },
        {
          title: "模組 F｜實作專案①：打磚塊遊戲——基礎架構",
          courses: [
            { title: "專案初始化與場景規劃", url: "topics/ios-game-dev/lesson-23.html" },
            { title: "建立球拍", url: "topics/ios-game-dev/lesson-24.html" },
            { title: "建立球", url: "topics/ios-game-dev/lesson-25.html" },
            { title: "磚塊陣列排版", url: "topics/ios-game-dev/lesson-26.html" },
            { title: "模組總結：場景切換與開始畫面", url: "topics/ios-game-dev/lesson-27.html" }
          ]
        },
        {
          title: "模組 G｜實作專案②：物理引擎與碰撞",
          courses: [
            { title: "physics body設定", url: "topics/ios-game-dev/lesson-28.html" },
            { title: "重力、速度與反彈", url: "topics/ios-game-dev/lesson-29.html" },
            { title: "碰撞偵測delegate", url: "topics/ios-game-dev/lesson-30.html" },
            { title: "碰撞分類（Collision Category）", url: "topics/ios-game-dev/lesson-31.html" },
            { title: "模組總結：球、球拍、磚塊的完整互動", url: "topics/ios-game-dev/lesson-32.html" }
          ]
        },
        {
          title: "模組 H｜實作專案③：遊戲邏輯與狀態管理",
          courses: [
            { title: "分數系統", url: "topics/ios-game-dev/lesson-33.html" },
            { title: "生命值系統", url: "topics/ios-game-dev/lesson-34.html" },
            { title: "勝負判定邏輯", url: "topics/ios-game-dev/lesson-35.html" },
            { title: "重新開始與暫停", url: "topics/ios-game-dev/lesson-36.html" },
            { title: "模組總結：完整的遊戲狀態機", url: "topics/ios-game-dev/lesson-37.html" }
          ]
        },
        {
          title: "模組 I｜音效與視覺效果",
          courses: [
            { title: "音效播放", url: "topics/ios-game-dev/lesson-38.html" },
            { title: "粒子特效", url: "topics/ios-game-dev/lesson-39.html" },
            { title: "簡單動畫讓遊戲更有手感", url: "topics/ios-game-dev/lesson-40.html" },
            { title: "模組總結：讓遊戲從「能玩」變成「好玩」", url: "topics/ios-game-dev/lesson-41.html" }
          ]
        },
        {
          title: "模組 J｜遊戲美術資源基礎",
          courses: [
            { title: "免費／合法素材哪裡找", url: "topics/ios-game-dev/lesson-42.html" },
            { title: "Sprite Sheet基礎概念", url: "topics/ios-game-dev/lesson-43.html" },
            { title: "App Icon設計規範", url: "topics/ios-game-dev/lesson-44.html" },
            { title: "模組總結：用Figma／Canva做簡易素材", url: "topics/ios-game-dev/lesson-45.html" }
          ]
        },
        {
          title: "模組 K｜資料儲存與遊戲設定",
          courses: [
            { title: "UserDefaults基礎", url: "topics/ios-game-dev/lesson-46.html" },
            { title: "儲存最高分與遊戲進度", url: "topics/ios-game-dev/lesson-47.html" },
            { title: "模組總結：簡易設定畫面", url: "topics/ios-game-dev/lesson-48.html" }
          ]
        },
        {
          title: "模組 L｜效能優化與除錯基礎",
          courses: [
            { title: "Xcode除錯器與中斷點", url: "topics/ios-game-dev/lesson-49.html" },
            { title: "Instruments效能檢測入門", url: "topics/ios-game-dev/lesson-50.html" },
            { title: "模組總結：SpriteKit常見效能陷阱", url: "topics/ios-game-dev/lesson-51.html" }
          ]
        },
        {
          title: "模組 M｜App內廣告整合",
          courses: [
            { title: "廣告的兩大類型：強制彈出型 vs 使用者主動點開型（以及第三種：橫幅廣告）", url: "topics/ios-game-dev/lesson-52.html" },
            { title: "廣告收入怎麼算：eCPM、曝光次數與填充率", url: "topics/ios-game-dev/lesson-53.html" },
            { title: "常見廣告聯播網選擇：為什麼新手從AdMob開始最簡單", url: "topics/ios-game-dev/lesson-54.html" },
            { title: "申請AdMob帳號與建立廣告單元", url: "topics/ios-game-dev/lesson-55.html" },
            { title: "在Xcode安裝並初始化Google Mobile Ads SDK", url: "topics/ios-game-dev/lesson-56.html" },
            { title: "實作橫幅廣告（Banner Ad）", url: "topics/ios-game-dev/lesson-57.html" },
            { title: "實作插頁廣告（Interstitial Ad）：強制型廣告的觸發時機與頻率拿捏", url: "topics/ios-game-dev/lesson-58.html" },
            { title: "實作獎勵型廣告（Rewarded Ad）：讓玩家自願看廣告換獎勵", url: "topics/ios-game-dev/lesson-59.html" },
            { title: "模組總結：使用者追蹤透明度（ATT）合規要求與上架前的廣告檢查清單", url: "topics/ios-game-dev/lesson-60.html" }
          ]
        },
        {
          title: "模組 N｜準備上架：Apple Developer Program",
          courses: [
            { title: "註冊Apple Developer Program（年費美金99元）", url: "topics/ios-game-dev/lesson-61.html" },
            { title: "憑證與簽章概念", url: "topics/ios-game-dev/lesson-62.html" },
            { title: "App ID與Provisioning Profile", url: "topics/ios-game-dev/lesson-63.html" },
            { title: "模組總結：上架前的帳號檢查清單", url: "topics/ios-game-dev/lesson-64.html" }
          ]
        },
        {
          title: "模組 O｜App Store Connect設定",
          courses: [
            { title: "建立App紀錄", url: "topics/ios-game-dev/lesson-65.html" },
            { title: "名稱、副標題與描述文案", url: "topics/ios-game-dev/lesson-66.html" },
            { title: "螢幕截圖規範與App預覽影片", url: "topics/ios-game-dev/lesson-67.html" },
            { title: "Icon上傳與App內購項目設定", url: "topics/ios-game-dev/lesson-68.html" },
            { title: "模組總結：定價與上架地區設定", url: "topics/ios-game-dev/lesson-69.html" }
          ]
        },
        {
          title: "模組 P｜上架審核：App Store審查指南",
          courses: [
            { title: "App Store審查指南總覽", url: "topics/ios-game-dev/lesson-70.html" },
            { title: "最常見的退件原因", url: "topics/ios-game-dev/lesson-71.html" },
            { title: "隱私權「營養標籤」", url: "topics/ios-game-dev/lesson-72.html" },
            { title: "模組總結：隱私權政策要求", url: "topics/ios-game-dev/lesson-73.html" }
          ]
        },
        {
          title: "模組 Q｜提交與發布流程",
          courses: [
            { title: "Archive封存與上傳", url: "topics/ios-game-dev/lesson-74.html" },
            { title: "TestFlight內測", url: "topics/ios-game-dev/lesson-75.html" },
            { title: "送出審查", url: "topics/ios-game-dev/lesson-76.html" },
            { title: "模組總結：發布管理與被退件怎麼辦", url: "topics/ios-game-dev/lesson-77.html" }
          ]
        },
        {
          title: "模組 R｜上架後：基礎行銷與版本迭代",
          courses: [
            { title: "ASO基礎：關鍵字優化與商店頁面轉換率", url: "topics/ios-game-dev/lesson-78.html" },
            { title: "蒐集使用者回饋與初期評分策略", url: "topics/ios-game-dev/lesson-79.html" },
            { title: "規劃版本更新與內容迭代", url: "topics/ios-game-dev/lesson-80.html" },
            { title: "模組總結：廣告之外——App內購買與付費下載的簡介比較", url: "topics/ios-game-dev/lesson-81.html" }
          ]
        },
        {
          title: "模組 S｜課程總結",
          courses: [
            { title: "全課程總結：從新手到獨立開發者的下一步", url: "topics/ios-game-dev/lesson-82.html" }
          ]
        }
      ]
    },
    {
      id: "ai-workflow",
      category: "tech",
      title: "AI工作流全紀錄：用Ollama＋n8n打造你的地端自動化系統",
      description:
        "從安裝地端 LLM 執行工具 Ollama 開始，學會用它的 API 讓外部工具呼叫地端模型，接著上手開源工作流平台 n8n，把 AI 步驟串進信件、試算表、Slack 與資料庫；並補齊 RAG 文件問答、Agent 工具呼叫、排程、錯誤處理與安全性，最終建立一套資料全程留在自己環境裡的地端 AI 自動化系統。",
      icon: "🤖",
      url: "topics/ai-workflow/index.html",
      modules: [
        {
          title: "模組 A｜序幕：什麼是AI工作流，為什麼要接地端LLM",
          courses: [
            { title: "什麼是AI工作流：把LLM變成可重複執行的自動化系統", url: "topics/ai-workflow/lesson-01.html" },
            { title: "為什麼要接地端LLM：隱私、成本、離線與資料主權", url: "topics/ai-workflow/lesson-02.html" },
            { title: "這門課會用到的兩個核心工具：Ollama與n8n", url: "topics/ai-workflow/lesson-03.html" },
            { title: "模組總結：這門課要一起做出什麼", url: "topics/ai-workflow/lesson-04.html" }
          ]
        },
        {
          title: "模組 B｜地端LLM基礎：安裝與執行Ollama",
          courses: [
            { title: "安裝Ollama", url: "topics/ai-workflow/lesson-05.html" },
            { title: "拉取並執行你的第一個地端模型", url: "topics/ai-workflow/lesson-06.html" },
            { title: "模型選擇：參數量、量化與硬體門檻的取捨", url: "topics/ai-workflow/lesson-07.html" },
            { title: "Ollama常用CLI指令", url: "topics/ai-workflow/lesson-08.html" },
            { title: "模組總結：地端LLM已經在你的電腦上跑起來了", url: "topics/ai-workflow/lesson-09.html" }
          ]
        },
        {
          title: "模組 C｜Ollama的API",
          courses: [
            { title: "Ollama的REST API：讓外部工具能呼叫地端LLM", url: "topics/ai-workflow/lesson-10.html" },
            { title: "用curl測試API：確認地端LLM真的能被呼叫", url: "topics/ai-workflow/lesson-11.html" },
            { title: "OpenAI相容格式：為什麼這件事很重要", url: "topics/ai-workflow/lesson-12.html" },
            { title: "模組總結：地端LLM準備好被工作流呼叫了", url: "topics/ai-workflow/lesson-13.html" }
          ]
        },
        {
          title: "模組 D｜n8n基礎：安裝與編輯器導覽",
          courses: [
            { title: "安裝n8n：Docker vs npm兩種方式", url: "topics/ai-workflow/lesson-14.html" },
            { title: "n8n編輯器導覽：節點、連線與畫布", url: "topics/ai-workflow/lesson-15.html" },
            { title: "觸發器（Trigger）：工作流怎麼被啟動", url: "topics/ai-workflow/lesson-16.html" },
            { title: "模組總結：建立你的第一個空白工作流", url: "topics/ai-workflow/lesson-17.html" }
          ]
        },
        {
          title: "模組 E｜n8n核心概念",
          courses: [
            { title: "節點之間的資料傳遞：JSON結構", url: "topics/ai-workflow/lesson-18.html" },
            { title: "n8n表達式（Expression）：動態取用前一個節點的資料", url: "topics/ai-workflow/lesson-19.html" },
            { title: "常用節點類型：IF、Switch、Set、Merge", url: "topics/ai-workflow/lesson-20.html" },
            { title: "模組總結：資料在工作流裡是怎麼流動的", url: "topics/ai-workflow/lesson-21.html" }
          ]
        },
        {
          title: "模組 F｜讓n8n接上Ollama",
          courses: [
            { title: "HTTP Request節點：呼叫Ollama API的通用做法", url: "topics/ai-workflow/lesson-22.html" },
            { title: "n8n內建的AI節點：LangChain整合與聊天模型節點", url: "topics/ai-workflow/lesson-23.html" },
            { title: "兩種接法的比較：HTTP Request vs 內建AI節點", url: "topics/ai-workflow/lesson-24.html" },
            { title: "模組總結：完成第一次n8n呼叫地端LLM", url: "topics/ai-workflow/lesson-25.html" }
          ]
        },
        {
          title: "模組 G｜實作範例①：第一個自動化流程",
          courses: [
            { title: "情境設定：一個貫穿全課程的自動化範例", url: "topics/ai-workflow/lesson-26.html" },
            { title: "建立觸發器：Webhook或排程開始", url: "topics/ai-workflow/lesson-27.html" },
            { title: "串上LLM處理節點", url: "topics/ai-workflow/lesson-28.html" },
            { title: "執行測試與查看結果", url: "topics/ai-workflow/lesson-29.html" },
            { title: "模組總結：從觸發到AI回應的完整迴路", url: "topics/ai-workflow/lesson-30.html" }
          ]
        },
        {
          title: "模組 H｜資料前處理與Prompt設計",
          courses: [
            { title: "為什麼Prompt要模板化，而不是寫死", url: "topics/ai-workflow/lesson-31.html" },
            { title: "用n8n的Set節點整理輸入資料", url: "topics/ai-workflow/lesson-32.html" },
            { title: "System Prompt與User Prompt的分工", url: "topics/ai-workflow/lesson-33.html" },
            { title: "模組總結：讓Prompt能重複套用在不同輸入上", url: "topics/ai-workflow/lesson-34.html" }
          ]
        },
        {
          title: "模組 I｜AI輸出的後處理與路由",
          courses: [
            { title: "為什麼要讓LLM輸出結構化資料（JSON）", url: "topics/ai-workflow/lesson-35.html" },
            { title: "解析LLM回傳的JSON", url: "topics/ai-workflow/lesson-36.html" },
            { title: "用IF/Switch節點依照AI的判斷分流", url: "topics/ai-workflow/lesson-37.html" },
            { title: "模組總結：AI從「回答問題」變成「做決策」", url: "topics/ai-workflow/lesson-38.html" }
          ]
        },
        {
          title: "模組 J｜串接外部系統",
          courses: [
            { title: "串接Email：讀取與寄送", url: "topics/ai-workflow/lesson-39.html" },
            { title: "串接Google試算表：讀寫資料", url: "topics/ai-workflow/lesson-40.html" },
            { title: "串接Slack／通訊軟體：發送通知", url: "topics/ai-workflow/lesson-41.html" },
            { title: "串接資料庫：寫入結構化紀錄", url: "topics/ai-workflow/lesson-42.html" },
            { title: "模組總結：完整的端到端自動化流程", url: "topics/ai-workflow/lesson-43.html" }
          ]
        },
        {
          title: "模組 K｜錯誤處理與流程穩定性",
          courses: [
            { title: "為什麼地端LLM需要更謹慎的錯誤處理", url: "topics/ai-workflow/lesson-44.html" },
            { title: "n8n的錯誤處理節點與重試機制", url: "topics/ai-workflow/lesson-45.html" },
            { title: "模組總結：讓工作流在失敗時不會整個中斷", url: "topics/ai-workflow/lesson-46.html" }
          ]
        },
        {
          title: "模組 L｜RAG基礎",
          courses: [
            { title: "為什麼要RAG：LLM不知道你的私有資料", url: "topics/ai-workflow/lesson-47.html" },
            { title: "文件切塊（Chunking）與向量嵌入（Embedding）概念", url: "topics/ai-workflow/lesson-48.html" },
            { title: "向量資料庫是什麼", url: "topics/ai-workflow/lesson-49.html" },
            { title: "模組總結：RAG的完整運作流程", url: "topics/ai-workflow/lesson-50.html" }
          ]
        },
        {
          title: "模組 M｜在n8n中實作簡易RAG",
          courses: [
            { title: "用Ollama產生嵌入向量", url: "topics/ai-workflow/lesson-51.html" },
            { title: "在n8n中串接向量資料庫節點", url: "topics/ai-workflow/lesson-52.html" },
            { title: "把檢索結果餵回LLM：完整RAG流程", url: "topics/ai-workflow/lesson-53.html" },
            { title: "模組總結：讓你的自動化流程能查詢私有文件", url: "topics/ai-workflow/lesson-54.html" }
          ]
        },
        {
          title: "模組 N｜AI Agent與工具呼叫基礎",
          courses: [
            { title: "什麼是工具呼叫（Tool Calling）", url: "topics/ai-workflow/lesson-55.html" },
            { title: "n8n的AI Agent節點基礎", url: "topics/ai-workflow/lesson-56.html" },
            { title: "讓Agent決定該用哪個工具", url: "topics/ai-workflow/lesson-57.html" },
            { title: "模組總結：從固定流程到自主決策的一步之遙", url: "topics/ai-workflow/lesson-58.html" }
          ]
        },
        {
          title: "模組 O｜排程與長期自動化",
          courses: [
            { title: "排程觸發器：讓工作流定期自動執行", url: "topics/ai-workflow/lesson-59.html" },
            { title: "Webhook觸發器：被動接收外部事件", url: "topics/ai-workflow/lesson-60.html" },
            { title: "模組總結：讓自動化流程真正無人值守運作", url: "topics/ai-workflow/lesson-61.html" }
          ]
        },
        {
          title: "模組 P｜監控、日誌與除錯",
          courses: [
            { title: "n8n的執行紀錄與除錯畫面", url: "topics/ai-workflow/lesson-62.html" },
            { title: "監控地端LLM的資源使用狀況", url: "topics/ai-workflow/lesson-63.html" },
            { title: "模組總結：工作流出問題時該從哪裡查起", url: "topics/ai-workflow/lesson-64.html" }
          ]
        },
        {
          title: "模組 Q｜安全性與資料隱私考量",
          courses: [
            { title: "地端部署的網路隔離與存取控制", url: "topics/ai-workflow/lesson-65.html" },
            { title: "保護暴露在外的Webhook端點", url: "topics/ai-workflow/lesson-66.html" },
            { title: "模組總結：地端不等於自動安全", url: "topics/ai-workflow/lesson-67.html" }
          ]
        },
        {
          title: "模組 R｜效能優化：地端LLM的資源管理",
          courses: [
            { title: "GPU／CPU資源與併發請求的取捨", url: "topics/ai-workflow/lesson-68.html" },
            { title: "量化模型的效能與品質權衡", url: "topics/ai-workflow/lesson-69.html" },
            { title: "模組總結：什麼時候該考慮升級到vLLM等生產環境方案", url: "topics/ai-workflow/lesson-70.html" }
          ]
        },
        {
          title: "模組 S｜課程總結",
          courses: [
            { title: "全課程總結：從一台電腦到一套能跑的地端AI自動化系統", url: "topics/ai-workflow/lesson-71.html" }
          ]
        }
      ]
    },
    {
      id: "ai-workflow-map",
      category: "tech",
      title: "AI工作流全景圖：目前有哪些工具、怎麼組、怎麼選",
      description:
        "盤點目前檯面上所有主要的 AI 工作流做法——從對話式助理、無碼自動化平台、程式框架與 Agent SDK、AI 編碼工具，到地端自架、RAG 知識庫與辦公室 AI；並補齊 MCP 等互通標準、五種工作流設計模式、Agent 的能力邊界、評測監控與成本控制，最後用一張決策樹與六個真實情境帶你選出該用哪一組。",
      icon: "🗺️",
      url: "topics/ai-workflow-map/index.html",
      modules: [
        {
          title: "模組 A｜序幕：什麼是「AI工作流」",
          courses: [
            { title: "從「跟AI聊天」到「讓AI幹活」：工作流的定義", url: "topics/ai-workflow-map/lesson-01.html" },
            { title: "這門課的地圖：工具層、模式層、治理層", url: "topics/ai-workflow-map/lesson-02.html" },
            { title: "一組座標軸：雲端↔地端、無碼↔寫程式、固定↔自主", url: "topics/ai-workflow-map/lesson-03.html" },
            { title: "模組總結：怎麼用這張地圖看懂任何一個新工具", url: "topics/ai-workflow-map/lesson-04.html" }
          ]
        },
        {
          title: "模組 B｜第一類：對話式AI工作台",
          courses: [
            { title: "ChatGPT／Claude／Gemini：三家通用助理的定位差異", url: "topics/ai-workflow-map/lesson-05.html" },
            { title: "專案、記憶與自訂指令：把一次性對話變成可重複流程", url: "topics/ai-workflow-map/lesson-06.html" },
            { title: "檔案、Canvas／Artifacts 與資料分析：對話框裡的小工作流", url: "topics/ai-workflow-map/lesson-07.html" },
            { title: "連接器與外掛：讓助理讀得到信箱、行事曆與雲端硬碟", url: "topics/ai-workflow-map/lesson-08.html" },
            { title: "模組總結：什麼情況「一個對話視窗」其實就夠了", url: "topics/ai-workflow-map/lesson-09.html" }
          ]
        },
        {
          title: "模組 C｜第二類：無碼／低碼自動化編排",
          courses: [
            { title: "Zapier 與 Make：把AI塞進既有SaaS流程", url: "topics/ai-workflow-map/lesson-10.html" },
            { title: "n8n：可自架的開源編排平台", url: "topics/ai-workflow-map/lesson-11.html" },
            { title: "Dify／Coze／Flowise／Langflow：以LLM為核心的應用建構器", url: "topics/ai-workflow-map/lesson-12.html" },
            { title: "Power Automate 與企業內建方案", url: "topics/ai-workflow-map/lesson-13.html" },
            { title: "怎麼挑：觸發器生態、節點數量、可自架性與計價模式", url: "topics/ai-workflow-map/lesson-14.html" },
            { title: "模組總結：無碼平台的能力邊界在哪裡", url: "topics/ai-workflow-map/lesson-15.html" }
          ]
        },
        {
          title: "模組 D｜第三類：程式框架與 Agent SDK",
          courses: [
            { title: "為什麼有了平台還是有人要寫程式", url: "topics/ai-workflow-map/lesson-16.html" },
            { title: "LangChain／LangGraph：鏈式流程與狀態圖", url: "topics/ai-workflow-map/lesson-17.html" },
            { title: "LlamaIndex 等 RAG 導向框架", url: "topics/ai-workflow-map/lesson-18.html" },
            { title: "Agent SDK：Claude Agent SDK、OpenAI Agents SDK", url: "topics/ai-workflow-map/lesson-19.html" },
            { title: "多Agent框架：CrewAI、AutoGen 與角色分工的真實效益", url: "topics/ai-workflow-map/lesson-20.html" },
            { title: "模組總結：什麼時候該從畫布走向程式碼", url: "topics/ai-workflow-map/lesson-21.html" }
          ]
        },
        {
          title: "模組 E｜第四類：AI編碼工作流",
          courses: [
            { title: "補全 vs 對話 vs 代理：三代編碼AI", url: "topics/ai-workflow-map/lesson-22.html" },
            { title: "IDE型：Cursor、GitHub Copilot、Windsurf", url: "topics/ai-workflow-map/lesson-23.html" },
            { title: "終端／代理型：Claude Code、Codex、Aider、Cline", url: "topics/ai-workflow-map/lesson-24.html" },
            { title: "非同步代理：丟一個issue，收一個PR", url: "topics/ai-workflow-map/lesson-25.html" },
            { title: "規格、審查與測試：讓AI寫的程式碼可被信任", url: "topics/ai-workflow-map/lesson-26.html" },
            { title: "模組總結：開發流程被改寫的部分，與沒被改寫的部分", url: "topics/ai-workflow-map/lesson-27.html" }
          ]
        },
        {
          title: "模組 F｜第五類：地端與自架方案",
          courses: [
            { title: "Ollama、LM Studio、llama.cpp：個人電腦上的模型執行器", url: "topics/ai-workflow-map/lesson-28.html" },
            { title: "vLLM 與生產級推論服務", url: "topics/ai-workflow-map/lesson-29.html" },
            { title: "Open WebUI／AnythingLLM：自架的對話與知識庫前端", url: "topics/ai-workflow-map/lesson-30.html" },
            { title: "開源模型現況：能力落差與硬體門檻", url: "topics/ai-workflow-map/lesson-31.html" },
            { title: "模組總結：資料主權的代價與收益", url: "topics/ai-workflow-map/lesson-32.html" }
          ]
        },
        {
          title: "模組 G｜知識與資料：RAG 與知識庫工作流",
          courses: [
            { title: "RAG 的骨架：切塊、嵌入、檢索、生成", url: "topics/ai-workflow-map/lesson-33.html" },
            { title: "向量資料庫盤點：pgvector、Qdrant、Chroma、Weaviate", url: "topics/ai-workflow-map/lesson-34.html" },
            { title: "現成知識庫產品：NotebookLM 與各平台內建知識庫", url: "topics/ai-workflow-map/lesson-35.html" },
            { title: "進階檢索：混合檢索、重排序、GraphRAG 與長脈絡的擠壓", url: "topics/ai-workflow-map/lesson-36.html" },
            { title: "模組總結：什麼時候該做RAG，什麼時候根本不用", url: "topics/ai-workflow-map/lesson-37.html" }
          ]
        },
        {
          title: "模組 H｜內容生產工作流：圖像、影音與聲音",
          courses: [
            { title: "圖像：ComfyUI 的節點式工作流 vs 雲端生成服務", url: "topics/ai-workflow-map/lesson-38.html" },
            { title: "影片：文生影片與AI剪輯目前真正能用的位置", url: "topics/ai-workflow-map/lesson-39.html" },
            { title: "語音：TTS、語音轉文字與會議紀錄流程", url: "topics/ai-workflow-map/lesson-40.html" },
            { title: "音樂與配樂生成", url: "topics/ai-workflow-map/lesson-41.html" },
            { title: "模組總結：一條可重複的內容生產線長什麼樣", url: "topics/ai-workflow-map/lesson-42.html" }
          ]
        },
        {
          title: "模組 I｜辦公與知識工作流",
          courses: [
            { title: "文件、簡報、試算表：Microsoft 365 Copilot 與 Google Workspace", url: "topics/ai-workflow-map/lesson-43.html" },
            { title: "筆記與第二大腦：Notion AI、Obsidian 外掛與個人知識管理", url: "topics/ai-workflow-map/lesson-44.html" },
            { title: "溝通協作：Slack／Teams 裡的AI", url: "topics/ai-workflow-map/lesson-45.html" },
            { title: "模組總結：個人生產力流程的重新設計", url: "topics/ai-workflow-map/lesson-46.html" }
          ]
        },
        {
          title: "模組 J｜互通標準：讓工具彼此連得起來",
          courses: [
            { title: "工具呼叫（Tool Calling）：AI 能動手的基本機制", url: "topics/ai-workflow-map/lesson-47.html" },
            { title: "MCP：把資料源與工具接上模型的通用介面", url: "topics/ai-workflow-map/lesson-48.html" },
            { title: "OpenAI 相容 API：模型可替換性的關鍵", url: "topics/ai-workflow-map/lesson-49.html" },
            { title: "Agent 之間的協作與跨系統標準", url: "topics/ai-workflow-map/lesson-50.html" },
            { title: "模組總結：標準化如何降低你的選型風險", url: "topics/ai-workflow-map/lesson-51.html" }
          ]
        },
        {
          title: "模組 K｜工作流設計模式",
          courses: [
            { title: "Prompt Chaining：把大任務切成可驗證的小步", url: "topics/ai-workflow-map/lesson-52.html" },
            { title: "Routing：先分類再處理", url: "topics/ai-workflow-map/lesson-53.html" },
            { title: "平行化與多路投票", url: "topics/ai-workflow-map/lesson-54.html" },
            { title: "Orchestrator–Worker：主控與子任務", url: "topics/ai-workflow-map/lesson-55.html" },
            { title: "Evaluator–Optimizer：讓AI審自己的稿", url: "topics/ai-workflow-map/lesson-56.html" },
            { title: "模組總結：先選模式，再選工具", url: "topics/ai-workflow-map/lesson-57.html" }
          ]
        },
        {
          title: "模組 L｜Agent：從固定流程到自主決策",
          courses: [
            { title: "Workflow 與 Agent 的分界線", url: "topics/ai-workflow-map/lesson-58.html" },
            { title: "Agent 迴圈：規劃、行動、觀察、修正", url: "topics/ai-workflow-map/lesson-59.html" },
            { title: "記憶、脈絡與長任務", url: "topics/ai-workflow-map/lesson-60.html" },
            { title: "Human-in-the-loop：把人放回關鍵節點", url: "topics/ai-workflow-map/lesson-61.html" },
            { title: "模組總結：什麼任務適合交給Agent，什麼不適合", url: "topics/ai-workflow-map/lesson-62.html" }
          ]
        },
        {
          title: "模組 M｜評測、監控與成本",
          courses: [
            { title: "為什麼AI流程一定要有一組評測集", url: "topics/ai-workflow-map/lesson-63.html" },
            { title: "可觀測性工具：LangSmith、Langfuse 等", url: "topics/ai-workflow-map/lesson-64.html" },
            { title: "成本結構：token、快取、模型分級與路由", url: "topics/ai-workflow-map/lesson-65.html" },
            { title: "延遲與使用者體驗", url: "topics/ai-workflow-map/lesson-66.html" },
            { title: "模組總結：能被衡量，才能被改善", url: "topics/ai-workflow-map/lesson-67.html" }
          ]
        },
        {
          title: "模組 N｜風險、安全與治理",
          courses: [
            { title: "幻覺與可驗證性：輸出把關的設計方式", url: "topics/ai-workflow-map/lesson-68.html" },
            { title: "Prompt Injection 與不可信輸入", url: "topics/ai-workflow-map/lesson-69.html" },
            { title: "權限最小化、金鑰與稽核軌跡", url: "topics/ai-workflow-map/lesson-70.html" },
            { title: "法遵與資料落地：企業導入最常卡住的地方", url: "topics/ai-workflow-map/lesson-71.html" },
            { title: "模組總結：治理不是煞車，是能上路的條件", url: "topics/ai-workflow-map/lesson-72.html" }
          ]
        },
        {
          title: "模組 O｜選型與落地",
          courses: [
            { title: "一張決策樹：從需求走到工具組合", url: "topics/ai-workflow-map/lesson-73.html" },
            { title: "三種標準配置：個人、小團隊、企業", url: "topics/ai-workflow-map/lesson-74.html" },
            { title: "導入節奏：先自動化哪一個流程才不會失敗", url: "topics/ai-workflow-map/lesson-75.html" },
            { title: "六個情境拆解：從需求到完整工作流", url: "topics/ai-workflow-map/lesson-76.html" },
            { title: "模組總結：工具會換，架構不會", url: "topics/ai-workflow-map/lesson-77.html" }
          ]
        },
        {
          title: "模組 P｜趨勢與課程總結",
          courses: [
            { title: "這一年變化最快的三件事", url: "topics/ai-workflow-map/lesson-78.html" },
            { title: "什麼是短期噪音，什麼是長期結構", url: "topics/ai-workflow-map/lesson-79.html" },
            { title: "全課程總結：把地圖折起來，開始動手", url: "topics/ai-workflow-map/lesson-80.html" }
          ]
        }
      ]
    },
    {
      id: "naruto",
      category: "anime",
      title: "火影忍者全紀錄：劇情、人物與忍界設定完整解析",
      description:
        "以原作漫畫 700 話為主線，完整拆解《火影忍者》：從查克拉、忍術體系、血繼限界與三大瞳術，到六道仙人與九尾之夜的前史；再依篇章講完第一部與疾風傳——中忍考試、佐助脫離、曉與尾獸、宇智波滅族真相、第四次忍界大戰到終末之谷，最後收在仇恨的連鎖與傳承結構等主題論。",
      icon: "🍥",
      url: "topics/naruto/index.html",
      modules: [
        {
          title: "模組 A｜序幕：作品與這個世界怎麼讀",
          courses: [
            { title: "火影忍者是什麼：岸本齊史、連載歷程與作品結構", url: "topics/naruto/lesson-01.html" },
            { title: "忍者世界的地理與政治：五大國與五大忍村", url: "topics/naruto/lesson-02.html" },
            { title: "忍者的階級與制度：從忍者學校到影", url: "topics/naruto/lesson-03.html" },
            { title: "貫穿全作的三條線：成長、輪迴與和平", url: "topics/naruto/lesson-04.html" },
            { title: "模組總結：閱讀路線與常見的理解陷阱", url: "topics/naruto/lesson-05.html" }
          ]
        },
        {
          title: "模組 B｜查克拉與忍術體系",
          courses: [
            { title: "查克拉是什麼：身體能量與精神能量的結合", url: "topics/naruto/lesson-06.html" },
            { title: "五種性質變化：火風雷土水的相剋關係", url: "topics/naruto/lesson-07.html" },
            { title: "形態變化與螺旋丸：查克拉的另一個維度", url: "topics/naruto/lesson-08.html" },
            { title: "忍術、體術、幻術：三大分野與各自的破解法", url: "topics/naruto/lesson-09.html" },
            { title: "封印術、時空間忍術與禁術", url: "topics/naruto/lesson-10.html" },
            { title: "模組總結：力量的階梯與它的代價", url: "topics/naruto/lesson-11.html" }
          ]
        },
        {
          title: "模組 C｜血繼限界與三大瞳術",
          courses: [
            { title: "寫輪眼：從勾玉到萬花筒的階梯", url: "topics/naruto/lesson-12.html" },
            { title: "萬花筒的代價與永恆萬花筒", url: "topics/naruto/lesson-13.html" },
            { title: "輪迴眼與六道之力", url: "topics/naruto/lesson-14.html" },
            { title: "白眼與日向一族的宗家分家", url: "topics/naruto/lesson-15.html" },
            { title: "血繼限界與血繼淘汰：木遁、冰遁、熔遁與塵遁", url: "topics/naruto/lesson-16.html" },
            { title: "模組總結：血統如何決定命運", url: "topics/naruto/lesson-17.html" }
          ]
        },
        {
          title: "模組 D｜前史一：忍界的起源",
          courses: [
            { title: "大筒木輝夜與神樹：查克拉的由來", url: "topics/naruto/lesson-18.html" },
            { title: "六道仙人：忍宗的創始與九隻尾獸的誕生", url: "topics/naruto/lesson-19.html" },
            { title: "因陀羅與阿修羅：兄弟對立的原型", url: "topics/naruto/lesson-20.html" },
            { title: "戰國時代：千手柱間與宇智波斑", url: "topics/naruto/lesson-21.html" },
            { title: "模組總結：木葉的建立與火影的傳承", url: "topics/naruto/lesson-22.html" }
          ]
        },
        {
          title: "模組 E｜前史二：三忍到九尾之夜",
          courses: [
            { title: "三次忍界大戰：忍村制度的代價", url: "topics/naruto/lesson-23.html" },
            { title: "傳說中的三忍：自來也、綱手、大蛇丸", url: "topics/naruto/lesson-24.html" },
            { title: "神無毘橋之戰：卡卡西、帶土與琳", url: "topics/naruto/lesson-25.html" },
            { title: "波風水門與漩渦玖辛奈", url: "topics/naruto/lesson-26.html" },
            { title: "模組總結：九尾之亂與鳴人出生的那一夜", url: "topics/naruto/lesson-27.html" }
          ]
        },
        {
          title: "模組 F｜第一部①：第七班的起點",
          courses: [
            { title: "漩渦鳴人：被排斥的孩子與九尾封印", url: "topics/naruto/lesson-28.html" },
            { title: "第七班成立：卡卡西的鈴鐺測驗", url: "topics/naruto/lesson-29.html" },
            { title: "波之國篇：再不斬與白", url: "topics/naruto/lesson-30.html" },
            { title: "白之死：「忍者是什麼」的第一次追問", url: "topics/naruto/lesson-31.html" },
            { title: "鳴人、佐助與小櫻：第七班的初期關係", url: "topics/naruto/lesson-32.html" },
            { title: "模組總結：第七班學到的第一課", url: "topics/naruto/lesson-33.html" }
          ]
        },
        {
          title: "模組 G｜第一部②：中忍考試",
          courses: [
            { title: "第一場試驗：一場要你作弊的考試", url: "topics/naruto/lesson-34.html" },
            { title: "死之森：大蛇丸的登場與咒印", url: "topics/naruto/lesson-35.html" },
            { title: "預賽群像：十場對戰與各自的課題", url: "topics/naruto/lesson-36.html" },
            { title: "寧次 vs 雛田：日向一族的宿命", url: "topics/naruto/lesson-37.html" },
            { title: "一個月的修行：千鳥、自來也與通靈之術", url: "topics/naruto/lesson-38.html" },
            { title: "模組總結：中忍考試的三層結構", url: "topics/naruto/lesson-39.html" }
          ]
        },
        {
          title: "模組 H｜第一部③：木葉崩潰與尋找綱手",
          courses: [
            { title: "正式賽開幕：鳴人 vs 寧次", url: "topics/naruto/lesson-40.html" },
            { title: "木葉崩潰作戰：砂隱與音隱的奇襲", url: "topics/naruto/lesson-41.html" },
            { title: "三代 vs 大蛇丸：屍鬼封盡與穢土轉生", url: "topics/naruto/lesson-42.html" },
            { title: "鳴人 vs 我愛羅：兩個人柱力的對照", url: "topics/naruto/lesson-43.html" },
            { title: "尋找綱手：鼬與鬼鮫登場、三忍再會", url: "topics/naruto/lesson-44.html" },
            { title: "模組總結：三代之死與木葉的重整", url: "topics/naruto/lesson-45.html" }
          ]
        },
        {
          title: "模組 I｜第一部④：佐助脫離與追擊戰",
          courses: [
            { title: "佐助的動搖：從屋頂之戰到接受咒印", url: "topics/naruto/lesson-46.html" },
            { title: "音之四人眾與咒印二階段", url: "topics/naruto/lesson-47.html" },
            { title: "鹿丸的第一次帶隊：五對五追擊戰", url: "topics/naruto/lesson-48.html" },
            { title: "追擊戰各場對戰詳解", url: "topics/naruto/lesson-49.html" },
            { title: "終末之谷：鳴人 vs 佐助 第一戰", url: "topics/naruto/lesson-50.html" },
            { title: "模組總結：第一部的結束與兩年半的空白", url: "topics/naruto/lesson-51.html" }
          ]
        },
        {
          title: "模組 J｜疾風傳①：我愛羅救出與曉登場",
          courses: [
            { title: "兩年後的第七班：重逢與第二次鈴鐺測驗", url: "topics/naruto/lesson-52.html" },
            { title: "我愛羅被擄：曉的行動開始", url: "topics/naruto/lesson-53.html" },
            { title: "蠍與千代婆婆：傀儡對決", url: "topics/naruto/lesson-54.html" },
            { title: "迪達拉與卡卡西：神威首次亮相", url: "topics/naruto/lesson-55.html" },
            { title: "我愛羅之死與千代的犧牲", url: "topics/naruto/lesson-56.html" },
            { title: "模組總結：曉的輪廓與尾獸收集計畫", url: "topics/naruto/lesson-57.html" }
          ]
        },
        {
          title: "模組 K｜疾風傳②：天地橋、佐井與大蛇丸線",
          courses: [
            { title: "第七班改組：佐井與大和", url: "topics/naruto/lesson-58.html" },
            { title: "天地橋任務：與佐助重逢", url: "topics/naruto/lesson-59.html" },
            { title: "佐井的來歷：根與志村團藏", url: "topics/naruto/lesson-60.html" },
            { title: "佐助在音忍的兩年與大蛇丸之死", url: "topics/naruto/lesson-61.html" },
            { title: "模組總結：三年的裂痕", url: "topics/naruto/lesson-62.html" }
          ]
        },
        {
          title: "模組 L｜疾風傳③：飛段角都與阿斯瑪之死",
          courses: [
            { title: "不死二人組：飛段與角都", url: "topics/naruto/lesson-63.html" },
            { title: "阿斯瑪之死", url: "topics/naruto/lesson-64.html" },
            { title: "鹿丸的復仇與風遁螺旋手裏劍", url: "topics/naruto/lesson-65.html" },
            { title: "模組總結：第一次真正失去老師", url: "topics/naruto/lesson-66.html" }
          ]
        },
        {
          title: "模組 M｜疾風傳④：自來也之死與佩恩襲擊木葉",
          courses: [
            { title: "自來也 vs 佩恩：雨隱之戰", url: "topics/naruto/lesson-67.html" },
            { title: "密碼與線索：自來也留下的訊息", url: "topics/naruto/lesson-68.html" },
            { title: "妙木山修行：仙人模式", url: "topics/naruto/lesson-69.html" },
            { title: "佩恩襲擊木葉：村子被毀", url: "topics/naruto/lesson-70.html" },
            { title: "鳴人 vs 佩恩：從復仇到理解", url: "topics/naruto/lesson-71.html" },
            { title: "模組總結：全作的中點與主題的第一次完成", url: "topics/naruto/lesson-72.html" }
          ]
        },
        {
          title: "模組 N｜疾風傳⑤：五影會談與鼬的真相",
          courses: [
            { title: "團藏上位與五影會談", url: "topics/naruto/lesson-73.html" },
            { title: "佐助 vs 鼬：最終對決", url: "topics/naruto/lesson-74.html" },
            { title: "宇智波滅族的真相", url: "topics/naruto/lesson-75.html" },
            { title: "佐助的轉向：從復仇者到摧毀木葉", url: "topics/naruto/lesson-76.html" },
            { title: "佐助 vs 團藏，與鳴人的第二次相對", url: "topics/naruto/lesson-77.html" },
            { title: "模組總結：真相如何改變一切", url: "topics/naruto/lesson-78.html" }
          ]
        },
        {
          title: "模組 O｜疾風傳⑥：第四次忍界大戰 上",
          courses: [
            { title: "開戰：忍者聯軍的組成與指揮", url: "topics/naruto/lesson-79.html" },
            { title: "穢土轉生軍團：與死者作戰", url: "topics/naruto/lesson-80.html" },
            { title: "鳴人的修行：與九喇嘛和解", url: "topics/naruto/lesson-81.html" },
            { title: "奇拉比與八尾：另一種人柱力", url: "topics/naruto/lesson-82.html" },
            { title: "各戰場詳解：第一階段的主要對戰", url: "topics/naruto/lesson-83.html" },
            { title: "模組總結：戰爭第一階段的結算", url: "topics/naruto/lesson-84.html" }
          ]
        },
        {
          title: "模組 P｜疾風傳⑦：第四次忍界大戰 下",
          courses: [
            { title: "十尾降臨與帶土的真面目", url: "topics/naruto/lesson-85.html" },
            { title: "四代火影歸來：歷代火影參戰", url: "topics/naruto/lesson-86.html" },
            { title: "斑復活與六道之力", url: "topics/naruto/lesson-87.html" },
            { title: "邁特凱的八門遁甲：死門", url: "topics/naruto/lesson-88.html" },
            { title: "大筒木輝夜與黑絕的真相", url: "topics/naruto/lesson-89.html" },
            { title: "模組總結：戰爭的結束與最後的未竟之事", url: "topics/naruto/lesson-90.html" }
          ]
        },
        {
          title: "模組 Q｜終末之谷與結局",
          courses: [
            { title: "鳴人 vs 佐助：最終戰", url: "topics/naruto/lesson-91.html" },
            { title: "佐助的答案與無限月讀的解除", url: "topics/naruto/lesson-92.html" },
            { title: "戰後的忍界與各角色的結局", url: "topics/naruto/lesson-93.html" },
            { title: "模組總結：700 話的收束", url: "topics/naruto/lesson-94.html" }
          ]
        },
        {
          title: "模組 R｜人物詳解①：第七班與木葉同期",
          courses: [
            { title: "漩渦鳴人：從空位到中心", url: "topics/naruto/lesson-95.html" },
            { title: "宇智波佐助：四次轉向的軌跡", url: "topics/naruto/lesson-96.html" },
            { title: "春野櫻：成長、限制與作品的處理問題", url: "topics/naruto/lesson-97.html" },
            { title: "旗木卡卡西：被過去綁住的半生", url: "topics/naruto/lesson-98.html" },
            { title: "奈良鹿丸與豬鹿蝶", url: "topics/naruto/lesson-99.html" },
            { title: "日向雛田與日向寧次", url: "topics/naruto/lesson-100.html" },
            { title: "洛克·李、邁特凱與砂隱三姊弟", url: "topics/naruto/lesson-101.html" }
          ]
        },
        {
          title: "模組 S｜人物詳解②：師長世代與歷代火影",
          courses: [
            { title: "初代千手柱間與二代千手扉間", url: "topics/naruto/lesson-102.html" },
            { title: "三代猿飛日斬與志村團藏", url: "topics/naruto/lesson-103.html" },
            { title: "四代波風水門與漩渦玖辛奈", url: "topics/naruto/lesson-104.html" },
            { title: "自來也：追尋答案的人", url: "topics/naruto/lesson-105.html" },
            { title: "綱手與大蛇丸：兩種面對死亡的方式", url: "topics/naruto/lesson-106.html" },
            { title: "大和、佐井與上忍群像", url: "topics/naruto/lesson-107.html" }
          ]
        },
        {
          title: "模組 T｜人物詳解③：曉與反派群像",
          courses: [
            { title: "宇智波鼬：全作犧牲最多的人", url: "topics/naruto/lesson-108.html" },
            { title: "長門與小南：理想如何變成災難", url: "topics/naruto/lesson-109.html" },
            { title: "宇智波帶土：想要一個琳還活著的世界", url: "topics/naruto/lesson-110.html" },
            { title: "宇智波斑：被歷史部分證明的悲觀主義者", url: "topics/naruto/lesson-111.html" },
            { title: "曉其他成員：鬼鮫、蠍、迪達拉、飛段、角都與絕", url: "topics/naruto/lesson-112.html" },
            { title: "模組總結：反派的共同結構", url: "topics/naruto/lesson-113.html" }
          ]
        },
        {
          title: "模組 U｜設定細節總整理",
          courses: [
            { title: "尾獸與人柱力全解", url: "topics/naruto/lesson-114.html" },
            { title: "通靈獸、忍具與戰鬥道具", url: "topics/naruto/lesson-115.html" },
            { title: "各村與地理總覽", url: "topics/naruto/lesson-116.html" },
            { title: "月之眼計畫的完整邏輯", url: "topics/naruto/lesson-117.html" },
            { title: "模組總結：設定表的使用方式", url: "topics/naruto/lesson-118.html" }
          ]
        },
        {
          title: "模組 V｜主題論",
          courses: [
            { title: "仇恨的連鎖與打破它的四種嘗試", url: "topics/naruto/lesson-119.html" },
            { title: "什麼是忍者：工具、人與規則", url: "topics/naruto/lesson-120.html" },
            { title: "傳承的結構：父子、師徒與世代", url: "topics/naruto/lesson-121.html" },
            { title: "模組總結：作品的成就與限制", url: "topics/naruto/lesson-122.html" }
          ]
        },
        {
          title: "模組 W｜續作概述與課程總結",
          courses: [
            { title: "續作與外傳概述，以及全課程總結", url: "topics/naruto/lesson-123.html" }
          ]
        }
      ]
    },
    {
      id: "one-piece",
      category: "anime",
      title: "海賊王全紀錄：劇情、人物與世界觀完整解析（未完結）",
      description:
        "完整拆解《ONE PIECE》的三個層次：先建立四海與偉大航路的地理、惡魔果實與覺醒、霸氣、世界政府與天龍人，以及空白的一百年與古代兵器；再依篇章講完從東海的集結、阿拉巴斯坦、頂上戰爭，到和之國與最終章艾格赫德，並附懸賞金與未回收伏筆整理。作品仍在連載，課程明確標示取材範圍。",
      icon: "🏴‍☠️",
      url: "topics/one-piece/index.html",
      modules: [
        {
          title: "模組 A｜序幕：這部作品怎麼讀",
          courses: [
            { title: "海賊王是什麼：尾田榮一郎與連載結構", url: "topics/one-piece/lesson-01.html" },
            { title: "大海賊時代的起點：羅傑的遺言", url: "topics/one-piece/lesson-02.html" },
            { title: "伏筆式敘事：這部作品的閱讀方法", url: "topics/one-piece/lesson-03.html" },
            { title: "取材範圍與連載進度說明", url: "topics/one-piece/lesson-04.html" },
            { title: "模組總結：三條主線——夥伴、自由與繼承的意志", url: "topics/one-piece/lesson-05.html" }
          ]
        },
        {
          title: "模組 B｜世界觀①：地理與航海",
          courses: [
            { title: "四海與偉大航路：世界的基本地理", url: "topics/one-piece/lesson-06.html" },
            { title: "記錄指針與偉大航路的航海術", url: "topics/one-piece/lesson-07.html" },
            { title: "聖地瑪莉喬亞、魚人島與關鍵地點", url: "topics/one-piece/lesson-08.html" },
            { title: "新世界：氣候、規則與四皇的分割", url: "topics/one-piece/lesson-09.html" },
            { title: "模組總結：地理如何決定劇情結構", url: "topics/one-piece/lesson-10.html" }
          ]
        },
        {
          title: "模組 C｜世界觀②：惡魔果實體系",
          courses: [
            { title: "惡魔果實是什麼：三大分類與代價", url: "topics/one-piece/lesson-11.html" },
            { title: "超人系：想像力決定強度", url: "topics/one-piece/lesson-12.html" },
            { title: "動物系：古代種、幻獸種與人造果實", url: "topics/one-piece/lesson-13.html" },
            { title: "自然系與覺醒", url: "topics/one-piece/lesson-14.html" },
            { title: "模組總結：果實體系的設計邏輯", url: "topics/one-piece/lesson-15.html" }
          ]
        },
        {
          title: "模組 D｜世界觀③：霸氣與戰鬥體系",
          courses: [
            { title: "霸氣是什麼：見聞色與武裝色", url: "topics/one-piece/lesson-16.html" },
            { title: "霸王色：王的資質", url: "topics/one-piece/lesson-17.html" },
            { title: "六式、劍術與各類武術體系", url: "topics/one-piece/lesson-18.html" },
            { title: "模組總結：戰鬥體系的階梯", url: "topics/one-piece/lesson-19.html" }
          ]
        },
        {
          title: "模組 E｜世界觀④：世界權力結構",
          courses: [
            { title: "世界政府與加盟國、世界會議", url: "topics/one-piece/lesson-20.html" },
            { title: "天龍人、五老星與伊姆", url: "topics/one-piece/lesson-21.html" },
            { title: "海軍：組織、三大將與正義的形式", url: "topics/one-piece/lesson-22.html" },
            { title: "王下七武海與四皇：兩種平衡裝置", url: "topics/one-piece/lesson-23.html" },
            { title: "模組總結：三大勢力的平衡與崩解", url: "topics/one-piece/lesson-24.html" }
          ]
        },
        {
          title: "模組 F｜世界觀⑤：空白的一百年",
          courses: [
            { title: "歷史正文與奧哈拉的悲劇", url: "topics/one-piece/lesson-25.html" },
            { title: "空白的一百年與古代王國", url: "topics/one-piece/lesson-26.html" },
            { title: "三大古代兵器", url: "topics/one-piece/lesson-27.html" },
            { title: "D之一族與「神的天敵」", url: "topics/one-piece/lesson-28.html" },
            { title: "模組總結：世界的核心矛盾", url: "topics/one-piece/lesson-29.html" }
          ]
        },
        {
          title: "模組 G｜東海篇：草帽一夥的集結",
          courses: [
            { title: "出航：魯夫、香克斯與那頂草帽", url: "topics/one-piece/lesson-30.html" },
            { title: "索隆：三刀流與那個約定", url: "topics/one-piece/lesson-31.html" },
            { title: "娜美與可可亞西村：阿龍篇", url: "topics/one-piece/lesson-32.html" },
            { title: "騙人布與西羅布村", url: "topics/one-piece/lesson-33.html" },
            { title: "香吉士與海上餐廳巴拉蒂", url: "topics/one-piece/lesson-34.html" },
            { title: "東海終戰與踏上偉大航路", url: "topics/one-piece/lesson-35.html" },
            { title: "模組總結：東海篇的敘事模板", url: "topics/one-piece/lesson-36.html" }
          ]
        },
        {
          title: "模組 H｜偉大航路前半：磁鼓與阿拉巴斯坦",
          courses: [
            { title: "偉大航路第一站：惠斯特里亞與拉普安", url: "topics/one-piece/lesson-37.html" },
            { title: "磁鼓王國與喬巴", url: "topics/one-piece/lesson-38.html" },
            { title: "阿拉巴斯坦：克洛克達爾與巴洛克工作社", url: "topics/one-piece/lesson-39.html" },
            { title: "薇薇與阿拉巴斯坦的抉擇", url: "topics/one-piece/lesson-40.html" },
            { title: "妮可·羅賓的加入與歷史正文的登場", url: "topics/one-piece/lesson-41.html" },
            { title: "過渡篇章與空島的線索", url: "topics/one-piece/lesson-42.html" },
            { title: "模組總結：世界規則的第一次揭露", url: "topics/one-piece/lesson-43.html" }
          ]
        },
        {
          title: "模組 I｜空島篇",
          courses: [
            { title: "上天空：空島的世界與規則", url: "topics/one-piece/lesson-44.html" },
            { title: "香朵拉的歷史與四百年的仇恨", url: "topics/one-piece/lesson-45.html" },
            { title: "艾涅爾與「神」的統治", url: "topics/one-piece/lesson-46.html" },
            { title: "黃金鐘與那段文字：全作最大的伏筆之一", url: "topics/one-piece/lesson-47.html" },
            { title: "模組總結：空島篇的重新評價", url: "topics/one-piece/lesson-48.html" }
          ]
        },
        {
          title: "模組 J｜司法島篇：水之七島與 CP9",
          courses: [
            { title: "水之七島：梅利號的判決", url: "topics/one-piece/lesson-49.html" },
            { title: "佛朗基與湯姆的過去", url: "topics/one-piece/lesson-50.html" },
            { title: "CP9 與世界政府的暗殺部隊", url: "topics/one-piece/lesson-51.html" },
            { title: "羅賓的選擇：「我想活下去」", url: "topics/one-piece/lesson-52.html" },
            { title: "對世界政府宣戰：燒毀那面旗", url: "topics/one-piece/lesson-53.html" },
            { title: "梅利號的葬禮", url: "topics/one-piece/lesson-54.html" },
            { title: "模組總結：司法島篇為什麼是高峰", url: "topics/one-piece/lesson-55.html" }
          ]
        },
        {
          title: "模組 K｜恐怖三桅船到香波地群島",
          courses: [
            { title: "恐怖三桅船與布魯克", url: "topics/one-piece/lesson-56.html" },
            { title: "香波地群島：奴隸拍賣與天龍人", url: "topics/one-piece/lesson-57.html" },
            { title: "巴索羅繆·熊：全員被打散", url: "topics/one-piece/lesson-58.html" },
            { title: "冥王雷利與兩年之約", url: "topics/one-piece/lesson-59.html" },
            { title: "模組總結：第一次徹底的失敗", url: "topics/one-piece/lesson-60.html" }
          ]
        },
        {
          title: "模組 L｜頂上戰爭篇",
          courses: [
            { title: "推進城：地獄的六層", url: "topics/one-piece/lesson-61.html" },
            { title: "艾斯的身世與白鬍子海賊團", url: "topics/one-piece/lesson-62.html" },
            { title: "馬林福特：開戰", url: "topics/one-piece/lesson-63.html" },
            { title: "艾斯之死與白鬍子最後的宣告", url: "topics/one-piece/lesson-64.html" },
            { title: "戰後：黑鬍子崛起與世界重整", url: "topics/one-piece/lesson-65.html" },
            { title: "模組總結：頂上戰爭改變了什麼", url: "topics/one-piece/lesson-66.html" }
          ]
        },
        {
          title: "模組 M｜魚人島篇",
          courses: [
            { title: "兩年後的重聚與進入新世界", url: "topics/one-piece/lesson-67.html" },
            { title: "魚人島的歷史：歧視、泰格與奧托哈伊", url: "topics/one-piece/lesson-68.html" },
            { title: "新魚人海賊團與白星公主", url: "topics/one-piece/lesson-69.html" },
            { title: "模組總結：魚人島篇的主題與伏筆", url: "topics/one-piece/lesson-70.html" }
          ]
        },
        {
          title: "模組 N｜龐克哈薩德與多雷斯羅薩",
          courses: [
            { title: "龐克哈薩德：凱撒與人體實驗", url: "topics/one-piece/lesson-71.html" },
            { title: "多雷斯羅薩：玩具與被遺忘的人", url: "topics/one-piece/lesson-72.html" },
            { title: "多佛朗明哥與德雷斯羅薩的十年", url: "topics/one-piece/lesson-73.html" },
            { title: "四檔與多雷斯羅薩決戰", url: "topics/one-piece/lesson-74.html" },
            { title: "藤虎與七武海制度的動搖", url: "topics/one-piece/lesson-75.html" },
            { title: "模組總結：新世界第一場國家級勝利", url: "topics/one-piece/lesson-76.html" }
          ]
        },
        {
          title: "模組 O｜卓武與全蛋糕島",
          courses: [
            { title: "卓武島：與凱多的第一次照面", url: "topics/one-piece/lesson-77.html" },
            { title: "香吉士的身世：傑爾馬66", url: "topics/one-piece/lesson-78.html" },
            { title: "全蛋糕島：大媽的靈魂王國", url: "topics/one-piece/lesson-79.html" },
            { title: "卡塔庫栗：見聞色的極限", url: "topics/one-piece/lesson-80.html" },
            { title: "婚禮之戰與逃離", url: "topics/one-piece/lesson-81.html" },
            { title: "模組總結：香吉士線的收束", url: "topics/one-piece/lesson-82.html" }
          ]
        },
        {
          title: "模組 P｜和之國 上：二十年前與鬼島前夜",
          courses: [
            { title: "和之國：鎖國、階級與污染", url: "topics/one-piece/lesson-83.html" },
            { title: "光月御田與二十年前", url: "topics/one-piece/lesson-84.html" },
            { title: "赤鞘九人男與桃之助", url: "topics/one-piece/lesson-85.html" },
            { title: "凱多與百獸海賊團", url: "topics/one-piece/lesson-86.html" },
            { title: "鬼島襲擊：聯軍的組成", url: "topics/one-piece/lesson-87.html" },
            { title: "模組總結：和之國上半的佈局", url: "topics/one-piece/lesson-88.html" }
          ]
        },
        {
          title: "模組 Q｜和之國 下：鬼島決戰",
          courses: [
            { title: "屋頂之戰：五人對兩名四皇", url: "topics/one-piece/lesson-89.html" },
            { title: "各戰場：大看板與飛六胞", url: "topics/one-piece/lesson-90.html" },
            { title: "五檔：太陽神尼卡", url: "topics/one-piece/lesson-91.html" },
            { title: "凱多敗北與大媽的結局", url: "topics/one-piece/lesson-92.html" },
            { title: "開國與新四皇", url: "topics/one-piece/lesson-93.html" },
            { title: "模組總結：和之國的收束", url: "topics/one-piece/lesson-94.html" }
          ]
        },
        {
          title: "模組 R｜最終章：艾格赫德",
          courses: [
            { title: "貝加龐克與艾格赫德", url: "topics/one-piece/lesson-95.html" },
            { title: "五老星的真面目", url: "topics/one-piece/lesson-96.html" },
            { title: "巴索羅繆·熊的一生", url: "topics/one-piece/lesson-97.html" },
            { title: "廣播、古代兵器與世界政府的行動", url: "topics/one-piece/lesson-98.html" },
            { title: "模組總結：最終章的開場", url: "topics/one-piece/lesson-99.html" }
          ]
        },
        {
          title: "模組 S｜最終章：目前的世界情勢",
          courses: [
            { title: "目前的世界情勢與艾爾巴夫", url: "topics/one-piece/lesson-100.html" },
            { title: "模組總結：連載中作品的閱讀策略", url: "topics/one-piece/lesson-101.html" }
          ]
        },
        {
          title: "模組 T｜人物詳解①：草帽一夥",
          courses: [
            { title: "蒙其·D·魯夫：想成為最自由的人", url: "topics/one-piece/lesson-102.html" },
            { title: "羅羅亞·索隆：從不改變目標的人", url: "topics/one-piece/lesson-103.html" },
            { title: "娜美：不可取代的專業", url: "topics/one-piece/lesson-104.html" },
            { title: "騙人布：會怕的英雄", url: "topics/one-piece/lesson-105.html" },
            { title: "文斯莫克·香吉士：兩個身分之間", url: "topics/one-piece/lesson-106.html" },
            { title: "托尼托尼·喬巴：想成為萬能藥", url: "topics/one-piece/lesson-107.html" },
            { title: "妮可·羅賓：想知道真相的人", url: "topics/one-piece/lesson-108.html" },
            { title: "佛朗基與布魯克", url: "topics/one-piece/lesson-109.html" },
            { title: "模組總結：甚平與一艘船的意義", url: "topics/one-piece/lesson-110.html" }
          ]
        },
        {
          title: "模組 U｜人物詳解②：四皇與頂點的男人們",
          courses: [
            { title: "哥爾·D·羅傑與冥王雷利", url: "topics/one-piece/lesson-111.html" },
            { title: "白鬍子愛德華·紐蓋特", url: "topics/one-piece/lesson-112.html" },
            { title: "紅髮香克斯", url: "topics/one-piece/lesson-113.html" },
            { title: "夏洛特·玲玲（BIG MOM）", url: "topics/one-piece/lesson-114.html" },
            { title: "百獸凱多", url: "topics/one-piece/lesson-115.html" },
            { title: "黑鬍子馬歇爾·D·汀奇", url: "topics/one-piece/lesson-116.html" },
            { title: "模組總結：四皇體制與時代交替", url: "topics/one-piece/lesson-117.html" }
          ]
        },
        {
          title: "模組 V｜人物詳解③：海軍與世界政府",
          courses: [
            { title: "卡普與戰國：舊世代的海軍", url: "topics/one-piece/lesson-118.html" },
            { title: "三大將：赤犬、青雉、黃猿", url: "topics/one-piece/lesson-119.html" },
            { title: "新世代的海軍：藤虎、克比與斯摩格", url: "topics/one-piece/lesson-120.html" },
            { title: "CP0、五老星與伊姆", url: "topics/one-piece/lesson-121.html" },
            { title: "模組總結：正義的多重面貌", url: "topics/one-piece/lesson-122.html" }
          ]
        },
        {
          title: "模組 W｜人物詳解④：革命軍、七武海與各族群",
          courses: [
            { title: "蒙其·D·龍與革命軍", url: "topics/one-piece/lesson-123.html" },
            { title: "薩波與艾斯：兄弟三人的約定", url: "topics/one-piece/lesson-124.html" },
            { title: "王下七武海全解", url: "topics/one-piece/lesson-125.html" },
            { title: "最惡世代與超新星", url: "topics/one-piece/lesson-126.html" },
            { title: "各族群與國家", url: "topics/one-piece/lesson-127.html" },
            { title: "模組總結：世界的群像", url: "topics/one-piece/lesson-128.html" }
          ]
        },
        {
          title: "模組 X｜設定細節總整理",
          courses: [
            { title: "船與航海道具", url: "topics/one-piece/lesson-129.html" },
            { title: "懸賞金全解讀", url: "topics/one-piece/lesson-130.html" },
            { title: "時間線年表", url: "topics/one-piece/lesson-131.html" },
            { title: "文化、貨幣與生活設定", url: "topics/one-piece/lesson-132.html" },
            { title: "模組總結：細節的作用", url: "topics/one-piece/lesson-133.html" }
          ]
        },
        {
          title: "模組 Y｜伏筆與主題論",
          courses: [
            { title: "未回收伏筆總整理", url: "topics/one-piece/lesson-134.html" },
            { title: "主流推測與它們的依據（非官方）", url: "topics/one-piece/lesson-135.html" },
            { title: "主題論：自由、繼承的意志與笑容", url: "topics/one-piece/lesson-136.html" },
            { title: "模組總結：這部作品的成就與限制", url: "topics/one-piece/lesson-137.html" }
          ]
        },
        {
          title: "模組 Z｜課程總結",
          courses: [
            { title: "全作結構回顧", url: "topics/one-piece/lesson-138.html" },
            { title: "全課程總結與重讀建議", url: "topics/one-piece/lesson-139.html" }
          ]
        }
      ]
    },
    {
      id: "dragon-ball",
      category: "anime",
      title: "七龍珠全紀錄：劇情、人物與力量體系完整解析（超篇未完結）",
      description:
        "以鳥山明原作為準，完整拆解《七龍珠》原作、Z、超三個階段：先建立氣與武術、許願規則、賽亞人與外星種族、破壞神與天使體系；再依篇章講完武道會與紅緞帶軍、賽亞人來襲、弗利沙、人造人與沙魯、魔人布歐，到超篇的力量大會。附變身系統全表與招式圖鑑，取材範圍不包含 GT。",
      icon: "🐉",
      url: "topics/dragon-ball/index.html",
      modules: [
        {
          title: "模組 A｜序幕：作品與這門課怎麼讀",
          courses: [
            { title: "七龍珠是什麼：鳥山明與連載歷程", url: "topics/dragon-ball/lesson-01.html" },
            { title: "武打漫畫的傳統與這部作品的定位", url: "topics/dragon-ball/lesson-02.html" }
          ]
        },
        {
          title: "模組 B｜氣與武術體系",
          courses: [
            { title: "氣是什麼：身體與精神合一的能量", url: "topics/dragon-ball/lesson-03.html" },
            { title: "賽亞人的瀕死成長與戰鬥力數值", url: "topics/dragon-ball/lesson-04.html" },
            { title: "大猿化：變身系統的起點", url: "topics/dragon-ball/lesson-05.html" },
            { title: "模組總結：力量體系的三個基礎規則", url: "topics/dragon-ball/lesson-06.html" }
          ]
        },
        {
          title: "模組 C｜七龍珠與許願規則",
          courses: [
            { title: "地球龍珠與神龍", url: "topics/dragon-ball/lesson-07.html" },
            { title: "那美克星龍珠與波爾龍", url: "topics/dragon-ball/lesson-08.html" },
            { title: "模組總結：死亡不再是終點", url: "topics/dragon-ball/lesson-09.html" }
          ]
        },
        {
          title: "模組 D｜賽亞人與外星種族",
          courses: [
            { title: "賽亞人：戰鬥民族的興衰", url: "topics/dragon-ball/lesson-10.html" },
            { title: "那美克星人與弗利沙一族", url: "topics/dragon-ball/lesson-11.html" },
            { title: "人造人與生物兵器", url: "topics/dragon-ball/lesson-12.html" },
            { title: "模組總結：威脅來源的三種類型", url: "topics/dragon-ball/lesson-13.html" }
          ]
        },
        {
          title: "模組 E｜眾神與宇宙結構",
          courses: [
            { title: "界王與界王神：舊有的神明體系", url: "topics/dragon-ball/lesson-14.html" },
            { title: "破壞神與天使：創造與毀滅的平衡", url: "topics/dragon-ball/lesson-15.html" },
            { title: "身勝手之極意：超越變身的境界", url: "topics/dragon-ball/lesson-16.html" },
            { title: "模組總結：世界觀的完整版圖", url: "topics/dragon-ball/lesson-17.html" }
          ]
        },
        {
          title: "模組 F｜原作：少年悟空篇",
          courses: [
            { title: "與布爾瑪相遇：第一次集龍珠的冒險", url: "topics/dragon-ball/lesson-18.html" },
            { title: "龜仙人與第21屆天下第一武道會", url: "topics/dragon-ball/lesson-19.html" },
            { title: "紅緞帶軍篇", url: "topics/dragon-ball/lesson-20.html" },
            { title: "比克大魔王篇與第22、23屆武道會", url: "topics/dragon-ball/lesson-21.html" },
            { title: "模組總結：原作篇的敘事特徵", url: "topics/dragon-ball/lesson-22.html" }
          ]
        },
        {
          title: "模組 G｜Z①：賽亞人來襲",
          courses: [
            { title: "拉帝茲登場：賽亞人身世的揭露", url: "topics/dragon-ball/lesson-23.html" },
            { title: "悟空的犧牲與一年的等待", url: "topics/dragon-ball/lesson-24.html" },
            { title: "那巴與貝吉塔的戰役", url: "topics/dragon-ball/lesson-25.html" },
            { title: "模組總結：賽亞人篇的完整弧線", url: "topics/dragon-ball/lesson-26.html" }
          ]
        },
        {
          title: "模組 H｜Z②：那美克星與弗利沙",
          courses: [
            { title: "尋找龍珠：抵達那美克星", url: "topics/dragon-ball/lesson-27.html" },
            { title: "基紐特戰隊", url: "topics/dragon-ball/lesson-28.html" },
            { title: "悟空抵達與超級賽亞人的首次覺醒", url: "topics/dragon-ball/lesson-29.html" },
            { title: "模組總結：一個象徵的誕生", url: "topics/dragon-ball/lesson-30.html" }
          ]
        },
        {
          title: "模組 I｜Z③：人造人與沙魯篇",
          courses: [
            { title: "特南克斯的警告與三年準備期", url: "topics/dragon-ball/lesson-31.html" },
            { title: "人造人17號與18號登場", url: "topics/dragon-ball/lesson-32.html" },
            { title: "沙魯的完全體之路", url: "topics/dragon-ball/lesson-33.html" },
            { title: "孫悟飯的覺醒", url: "topics/dragon-ball/lesson-34.html" },
            { title: "模組總結：一個關於期待的篇章", url: "topics/dragon-ball/lesson-35.html" }
          ]
        },
        {
          title: "模組 J｜Z④：魔人布歐篇",
          courses: [
            { title: "世界大會重啟與比比迪的野心", url: "topics/dragon-ball/lesson-36.html" },
            { title: "魔人布歐的釋放與分裂", url: "topics/dragon-ball/lesson-37.html" },
            { title: "邪惡布歐的最終形態與元氣彈的完成", url: "topics/dragon-ball/lesson-38.html" },
            { title: "模組總結：Z篇的完整弧線", url: "topics/dragon-ball/lesson-39.html" }
          ]
        },
        {
          title: "模組 K｜超①：神與神、復活的F",
          courses: [
            { title: "破壞神比魯斯登場", url: "topics/dragon-ball/lesson-40.html" },
            { title: "弗利沙的復仇：黃金形態", url: "topics/dragon-ball/lesson-41.html" },
            { title: "模組總結：重新定義力量尺標", url: "topics/dragon-ball/lesson-42.html" }
          ]
        },
        {
          title: "模組 L｜超②：力量大會",
          courses: [
            { title: "宇宙生存戰的規則", url: "topics/dragon-ball/lesson-43.html" },
            { title: "各宇宙代表隊", url: "topics/dragon-ball/lesson-44.html" },
            { title: "身勝手之極意的完成與贏家的代價", url: "topics/dragon-ball/lesson-45.html" },
            { title: "模組總結：一次規模的極致展示", url: "topics/dragon-ball/lesson-46.html" }
          ]
        },
        {
          title: "模組 M｜超③：劇場版布羅利與超級英雄",
          courses: [
            { title: "布羅利：賽亞人身世的補完", url: "topics/dragon-ball/lesson-47.html" },
            { title: "超級英雄：紅緞帶軍的重組", url: "topics/dragon-ball/lesson-48.html" },
            { title: "模組總結：劇情部分的完整回顧", url: "topics/dragon-ball/lesson-49.html" }
          ]
        },
        {
          title: "模組 N｜人物詳解①：悟空一脈",
          courses: [
            { title: "孫悟空：純粹的戰鬥之心", url: "topics/dragon-ball/lesson-50.html" },
            { title: "貝吉塔：從征服者到守護者", url: "topics/dragon-ball/lesson-51.html" },
            { title: "孫悟飯、悟天與特南克斯", url: "topics/dragon-ball/lesson-52.html" },
            { title: "模組總結：一個家族的完整圖譜", url: "topics/dragon-ball/lesson-53.html" }
          ]
        },
        {
          title: "模組 O｜人物詳解②：地球人夥伴",
          courses: [
            { title: "克林：凡人的極限與意義", url: "topics/dragon-ball/lesson-54.html" },
            { title: "天津飯與比克", url: "topics/dragon-ball/lesson-55.html" },
            { title: "模組總結：凡人在宇宙敘事裡的位置", url: "topics/dragon-ball/lesson-56.html" }
          ]
        },
        {
          title: "模組 P｜人物詳解③：反派群像",
          courses: [
            { title: "弗利沙：優雅外表下的絕對暴力", url: "topics/dragon-ball/lesson-57.html" },
            { title: "沙魯：對完美的病態執著", url: "topics/dragon-ball/lesson-58.html" },
            { title: "魔人布歐：純真與兇殘的一體兩面", url: "topics/dragon-ball/lesson-59.html" },
            { title: "模組總結：反派設計的三種邏輯", url: "topics/dragon-ball/lesson-60.html" }
          ]
        },
        {
          title: "模組 Q｜人物詳解④：眾神與宇宙勢力",
          courses: [
            { title: "界王神與老界王神", url: "topics/dragon-ball/lesson-61.html" },
            { title: "比魯斯與烏薩", url: "topics/dragon-ball/lesson-62.html" },
            { title: "模組總結：從敵人到相處對象", url: "topics/dragon-ball/lesson-63.html" }
          ]
        },
        {
          title: "模組 R｜設定細節總整理",
          courses: [
            { title: "變身系統全表", url: "topics/dragon-ball/lesson-64.html" },
            { title: "招式圖鑑", url: "topics/dragon-ball/lesson-65.html" },
            { title: "地理與宇宙結構總覽", url: "topics/dragon-ball/lesson-66.html" },
            { title: "模組總結：細節如何支撐長篇連載", url: "topics/dragon-ball/lesson-67.html" }
          ]
        },
        {
          title: "模組 S｜主題論與課程總結",
          courses: [
            { title: "超越極限：貫穿全作的核心命題", url: "topics/dragon-ball/lesson-68.html" },
            { title: "夥伴的力量與元氣彈的象徵", url: "topics/dragon-ball/lesson-69.html" },
            { title: "成就與限制：一次誠實的評價", url: "topics/dragon-ball/lesson-70.html" },
            { title: "全課程總結與重讀建議", url: "topics/dragon-ball/lesson-71.html" }
          ]
        }
      ]
    },
    {
      id: "fullmetal-alchemist",
      category: "anime",
      title: "鋼之鍊金術士全紀錄：世界觀、劇情與人物完整解析",
      description:
        "以原作漫畫／Brotherhood 版本為準，完整拆解等價交換的鍊金術原理、賢者之石與人柱力、阿梅斯特里斯的軍事體制與伊修瓦爾戰爭的黑暗真相；再依時間線講完人體鍊成的代價、北方布里格斯要塞、疤痕的復仇線，到父親的真面目與完結篇。2003 年版動畫的不同結局僅作簡要說明，不混入主線劇情。",
      icon: "⚗️",
      url: "topics/fullmetal-alchemist/index.html",
      modules: [
        {
          title: "模組 A｜序幕：這部作品怎麼讀",
          courses: [
            { title: "鋼之鍊金術士是什麼：荒川弘與連載背景", url: "topics/fullmetal-alchemist/lesson-01.html" },
            { title: "等價交換：規則與哲學的雙重身分", url: "topics/fullmetal-alchemist/lesson-02.html" }
          ]
        },
        {
          title: "模組 B｜鍊金術的原理與等價交換",
          courses: [
            { title: "鍊成陣的運作原理", url: "topics/fullmetal-alchemist/lesson-03.html" },
            { title: "國家鍊金術師制度", url: "topics/fullmetal-alchemist/lesson-04.html" },
            { title: "模組總結：從規則到禁忌", url: "topics/fullmetal-alchemist/lesson-05.html" }
          ]
        },
        {
          title: "模組 C｜賢者之石與人柱力",
          courses: [
            { title: "賢者之石：無視等價交換的存在", url: "topics/fullmetal-alchemist/lesson-06.html" },
            { title: "人柱力：真相與代價的轉嫁", url: "topics/fullmetal-alchemist/lesson-07.html" },
            { title: "增幅鍊成與國家鍊成陣", url: "topics/fullmetal-alchemist/lesson-08.html" },
            { title: "模組總結：一個關於代價的完整寓言", url: "topics/fullmetal-alchemist/lesson-09.html" }
          ]
        },
        {
          title: "模組 D｜阿梅斯特里斯的地理與軍事體制",
          courses: [
            { title: "阿梅斯特里斯的軍區劃分", url: "topics/fullmetal-alchemist/lesson-10.html" },
            { title: "「人形兵器」：國家鍊金術師的實際處境", url: "topics/fullmetal-alchemist/lesson-11.html" },
            { title: "模組總結：一個軍事化的國家", url: "topics/fullmetal-alchemist/lesson-12.html" }
          ]
        },
        {
          title: "模組 E｜伊修瓦爾戰爭與國家的秘密",
          courses: [
            { title: "伊修瓦爾戰爭的起因與經過", url: "topics/fullmetal-alchemist/lesson-13.html" },
            { title: "戰爭真正的目的：國家鍊成陣的用途", url: "topics/fullmetal-alchemist/lesson-14.html" },
            { title: "模組總結：世界觀的完整版圖", url: "topics/fullmetal-alchemist/lesson-15.html" }
          ]
        },
        {
          title: "模組 F｜人體鍊成的代價與踏上旅程",
          courses: [
            { title: "母親之死與人體鍊成的決定", url: "topics/fullmetal-alchemist/lesson-16.html" },
            { title: "人體鍊成的失敗與代價", url: "topics/fullmetal-alchemist/lesson-17.html" },
            { title: "洛克貝爾一家與溫麗", url: "topics/fullmetal-alchemist/lesson-18.html" },
            { title: "模組總結：一趟贖罪與尋找的旅程", url: "topics/fullmetal-alchemist/lesson-19.html" }
          ]
        },
        {
          title: "模組 G｜拉魯獸重站與軍方陰謀",
          courses: [
            { title: "疤痕登場：對國家鍊金術師的復仇", url: "topics/fullmetal-alchemist/lesson-20.html" },
            { title: "拉魯獸重站的地下秘密", url: "topics/fullmetal-alchemist/lesson-21.html" },
            { title: "與疤痕的初次交手", url: "topics/fullmetal-alchemist/lesson-22.html" },
            { title: "模組總結：懸念的佈局", url: "topics/fullmetal-alchemist/lesson-23.html" }
          ]
        },
        {
          title: "模組 H｜人造七宗罪初登場",
          courses: [
            { title: "拉斯特與格拉托尼", url: "topics/fullmetal-alchemist/lesson-24.html" },
            { title: "恩維與軍方高層的關係", url: "topics/fullmetal-alchemist/lesson-25.html" },
            { title: "模組總結：故事性質的轉變", url: "topics/fullmetal-alchemist/lesson-26.html" }
          ]
        },
        {
          title: "模組 I｜北方軍與布里格斯",
          courses: [
            { title: "布里格斯要塞：凍土上的獨立王國", url: "topics/fullmetal-alchemist/lesson-27.html" },
            { title: "阿姆斯特朗家族", url: "topics/fullmetal-alchemist/lesson-28.html" },
            { title: "人造人工廠與身體秘密的追查", url: "topics/fullmetal-alchemist/lesson-29.html" },
            { title: "模組總結：一個潛在的盟友基地", url: "topics/fullmetal-alchemist/lesson-30.html" }
          ]
        },
        {
          title: "模組 J｜疤痕的過去與伊修瓦爾線",
          courses: [
            { title: "疤痕的真實身世", url: "topics/fullmetal-alchemist/lesson-31.html" },
            { title: "馬爾寇兄妹與倖存者的處境", url: "topics/fullmetal-alchemist/lesson-32.html" },
            { title: "模組總結：戰爭沒有真正的贏家", url: "topics/fullmetal-alchemist/lesson-33.html" }
          ]
        },
        {
          title: "模組 K｜父親的真面目與國家鍊成陣",
          courses: [
            { title: "「父親」的真面目", url: "topics/fullmetal-alchemist/lesson-34.html" },
            { title: "大總統普萊德的身分", url: "topics/fullmetal-alchemist/lesson-35.html" },
            { title: "月蝕之日的計畫", url: "topics/fullmetal-alchemist/lesson-36.html" },
            { title: "模組總結：一切懸念的匯聚點", url: "topics/fullmetal-alchemist/lesson-37.html" }
          ]
        },
        {
          title: "模組 L｜伊修瓦爾內戰終戰與大決戰",
          courses: [
            { title: "舊部隊的反叛與盟友的集結", url: "topics/fullmetal-alchemist/lesson-38.html" },
            { title: "馬斯坦的復仇與抉擇", url: "topics/fullmetal-alchemist/lesson-39.html" },
            { title: "與父親及七宗罪的總決戰", url: "topics/fullmetal-alchemist/lesson-40.html" },
            { title: "模組總結：一場集體的勝利", url: "topics/fullmetal-alchemist/lesson-41.html" }
          ]
        },
        {
          title: "模組 M｜結局與代價的清算",
          courses: [
            { title: "等價交換的最終償還", url: "topics/fullmetal-alchemist/lesson-42.html" },
            { title: "兄弟倆各自的選擇", url: "topics/fullmetal-alchemist/lesson-43.html" },
            { title: "戰後的阿梅斯特里斯", url: "topics/fullmetal-alchemist/lesson-44.html" },
            { title: "模組總結：劇情部分的完整回顧", url: "topics/fullmetal-alchemist/lesson-45.html" }
          ]
        },
        {
          title: "模組 N｜人物詳解①：愛德華與阿爾馮斯",
          courses: [
            { title: "愛德華·艾爾利克：義肢與心理創傷", url: "topics/fullmetal-alchemist/lesson-46.html" },
            { title: "阿爾馮斯·艾爾利克：沒有身體的靈魂", url: "topics/fullmetal-alchemist/lesson-47.html" },
            { title: "模組總結：一段共同承擔的旅程", url: "topics/fullmetal-alchemist/lesson-48.html" }
          ]
        },
        {
          title: "模組 O｜人物詳解②：軍方群像",
          courses: [
            { title: "洛伊·馬斯坦：野心與贖罪", url: "topics/fullmetal-alchemist/lesson-49.html" },
            { title: "莉莎·霍克愛與亞歷克斯·阿姆斯特朗", url: "topics/fullmetal-alchemist/lesson-50.html" },
            { title: "模組總結：體制內的多元光譜", url: "topics/fullmetal-alchemist/lesson-51.html" }
          ]
        },
        {
          title: "模組 P｜人物詳解③：七宗罪",
          courses: [
            { title: "七宗罪的血緣結構", url: "topics/fullmetal-alchemist/lesson-52.html" },
            { title: "格里德：渴望自由的存在", url: "topics/fullmetal-alchemist/lesson-53.html" },
            { title: "模組總結：弱點的具象化", url: "topics/fullmetal-alchemist/lesson-54.html" }
          ]
        },
        {
          title: "模組 Q｜人物詳解④：其他重要角色",
          courses: [
            { title: "疤痕：復仇者的完整定位", url: "topics/fullmetal-alchemist/lesson-55.html" },
            { title: "溫麗與馬爾寇兄妹", url: "topics/fullmetal-alchemist/lesson-56.html" },
            { title: "模組總結：一部由角色支撐的作品", url: "topics/fullmetal-alchemist/lesson-57.html" }
          ]
        },
        {
          title: "模組 R｜設定細節總整理",
          courses: [
            { title: "鍊金術符號與陣式圖鑑", url: "topics/fullmetal-alchemist/lesson-58.html" },
            { title: "國家鍊金術師名冊", url: "topics/fullmetal-alchemist/lesson-59.html" },
            { title: "地圖與軍區總覽", url: "topics/fullmetal-alchemist/lesson-60.html" },
            { title: "人造七宗罪對照表與模組總結", url: "topics/fullmetal-alchemist/lesson-61.html" }
          ]
        },
        {
          title: "模組 S｜主題論與課程總結",
          courses: [
            { title: "等價交換：從鍊金術法則到人生哲學", url: "topics/fullmetal-alchemist/lesson-62.html" },
            { title: "戰爭創傷與救贖的可能", url: "topics/fullmetal-alchemist/lesson-63.html" },
            { title: "家人、傳承與兩兄弟的成長弧線", url: "topics/fullmetal-alchemist/lesson-64.html" },
            { title: "成就與限制：一次誠實的評估", url: "topics/fullmetal-alchemist/lesson-65.html" },
            { title: "全課程總結與重讀建議", url: "topics/fullmetal-alchemist/lesson-66.html" }
          ]
        }
      ]
    },
    {
      id: "prince-of-tennis",
      category: "anime",
      title: "網球王子全紀錄：劇情、人物與必殺技體系完整解析",
      description:
        "完整解析橫跨二十七年的《網球王子》系列：先建立網球規則、必殺技的分類與無我境界三門、日本中學部活體制與校際勢力版圖；再依時間線講完原作 42 卷的都大會、關東與全國大賽決賽對立海大，到《新網球王子》的 U-17 合宿、世界盃，以及二〇二六年八月完結的真・大結局。",
      icon: "🎾",
      url: "topics/prince-of-tennis/index.html",
      modules: [
        {
          title: "模組 A｜序幕：作品與這門課怎麼讀",
          courses: [
            { title: "網球王子是什麼：許斐剛與連載歷程", url: "topics/prince-of-tennis/lesson-01.html" },
            { title: "版本地圖：原作、新網王與劇場版的時間線", url: "topics/prince-of-tennis/lesson-02.html" },
            { title: "這門課怎麼讀：模組結構說明", url: "topics/prince-of-tennis/lesson-03.html" }
          ]
        },
        {
          title: "模組 B｜網球規則基礎",
          courses: [
            { title: "計分方式與一場比賽的結構", url: "topics/prince-of-tennis/lesson-04.html" },
            { title: "單打、雙打與團體賽的出場順序", url: "topics/prince-of-tennis/lesson-05.html" },
            { title: "模組總結：規則如何轉化為戲劇性", url: "topics/prince-of-tennis/lesson-06.html" }
          ]
        },
        {
          title: "模組 C｜必殺技體系①：物理系技法",
          courses: [
            { title: "必殺技的分類原則", url: "topics/prince-of-tennis/lesson-07.html" },
            { title: "旋轉與落點：物理系的基本原理", url: "topics/prince-of-tennis/lesson-08.html" },
            { title: "干擾系技法：作用於對手的招式", url: "topics/prince-of-tennis/lesson-09.html" },
            { title: "模組總結：招式體系的結構性作用", url: "topics/prince-of-tennis/lesson-10.html" }
          ]
        },
        {
          title: "模組 D｜必殺技體系②：無我境界與三門",
          courses: [
            { title: "無我境界：概念與觸發條件", url: "topics/prince-of-tennis/lesson-11.html" },
            { title: "三門①：百鍊自得與才氣煥發", url: "topics/prince-of-tennis/lesson-12.html" },
            { title: "三門②：天衣無縫之極致", url: "topics/prince-of-tennis/lesson-13.html" },
            { title: "模組總結：境界體系的整體評價", url: "topics/prince-of-tennis/lesson-14.html" }
          ]
        },
        {
          title: "模組 E｜部活體制與校際版圖",
          courses: [
            { title: "日本中學部活體制與正選選拔", url: "topics/prince-of-tennis/lesson-15.html" },
            { title: "賽事階梯：都大會、關東大賽與全國大賽", url: "topics/prince-of-tennis/lesson-16.html" },
            { title: "模組總結：校際版圖與強校分布", url: "topics/prince-of-tennis/lesson-17.html" }
          ]
        },
        {
          title: "模組 F｜原作①：入部與都大會",
          courses: [
            { title: "越前龍馬入部：天才少年的起點", url: "topics/prince-of-tennis/lesson-18.html" },
            { title: "校內排名賽與正選的集結", url: "topics/prince-of-tennis/lesson-19.html" },
            { title: "都大會：不動峰與初期對手", url: "topics/prince-of-tennis/lesson-20.html" },
            { title: "模組總結：開局的結構設計", url: "topics/prince-of-tennis/lesson-21.html" }
          ]
        },
        {
          title: "模組 G｜原作②：關東大賽",
          courses: [
            { title: "關東大賽的賽制與參賽勢力", url: "topics/prince-of-tennis/lesson-22.html" },
            { title: "聖魯道夫與山吹：戰術型對手", url: "topics/prince-of-tennis/lesson-23.html" },
            { title: "冰帝學園：規模與華麗的壓迫", url: "topics/prince-of-tennis/lesson-24.html" },
            { title: "手塚的傷與隊伍的重整", url: "topics/prince-of-tennis/lesson-25.html" },
            { title: "模組總結：關東大賽的整體評價", url: "topics/prince-of-tennis/lesson-26.html" }
          ]
        },
        {
          title: "模組 H｜原作③：全國大賽前半",
          courses: [
            { title: "全國大賽的開場與青學的處境", url: "topics/prince-of-tennis/lesson-27.html" },
            { title: "比嘉中：粗暴網球的衝擊", url: "topics/prince-of-tennis/lesson-28.html" },
            { title: "四天寶寺：關西強豪的雙面性", url: "topics/prince-of-tennis/lesson-29.html" },
            { title: "手塚的回歸與青學的完全體", url: "topics/prince-of-tennis/lesson-30.html" },
            { title: "模組總結：全國大賽前半的結構", url: "topics/prince-of-tennis/lesson-31.html" }
          ]
        },
        {
          title: "模組 I｜原作④：全國大賽決賽（原作完結）",
          courses: [
            { title: "立海大附屬：絕對王者的構造", url: "topics/prince-of-tennis/lesson-32.html" },
            { title: "決賽前半：各自的最終試煉", url: "topics/prince-of-tennis/lesson-33.html" },
            { title: "龍馬對幸村：原作的最終一戰", url: "topics/prince-of-tennis/lesson-34.html" },
            { title: "模組總結：原作的完結與評價", url: "topics/prince-of-tennis/lesson-35.html" }
          ]
        },
        {
          title: "模組 J｜新網王①：U-17 合宿",
          courses: [
            { title: "新網球王子的舞台轉換", url: "topics/prince-of-tennis/lesson-36.html" },
            { title: "淘汰制度與中學生的逆襲", url: "topics/prince-of-tennis/lesson-37.html" },
            { title: "合宿訓練體系與技術進化", url: "topics/prince-of-tennis/lesson-38.html" },
            { title: "模組總結：合宿篇的功能定位", url: "topics/prince-of-tennis/lesson-39.html" }
          ]
        },
        {
          title: "模組 K｜新網王②：世界盃前半",
          courses: [
            { title: "U-17 世界盃的賽制與參賽國", url: "topics/prince-of-tennis/lesson-40.html" },
            { title: "分組賽：日本隊的初期考驗", url: "topics/prince-of-tennis/lesson-41.html" },
            { title: "準決賽：日本對德國與手塚的對決", url: "topics/prince-of-tennis/lesson-42.html" },
            { title: "模組總結：世界盃前半的評價", url: "topics/prince-of-tennis/lesson-43.html" }
          ]
        },
        {
          title: "模組 L｜新網王③：世界盃決賽",
          courses: [
            { title: "西班牙隊：世界最強的構造", url: "topics/prince-of-tennis/lesson-44.html" },
            { title: "決賽對戰：日本隊的逐場突破", url: "topics/prince-of-tennis/lesson-45.html" },
            { title: "模組總結：決賽的敘事評價", url: "topics/prince-of-tennis/lesson-46.html" }
          ]
        },
        {
          title: "模組 M｜新網王④：大結局",
          courses: [
            { title: "越前兄弟：龍馬與龍雅的關係線", url: "topics/prince-of-tennis/lesson-47.html" },
            { title: "最終戰：龍馬對龍雅的決著", url: "topics/prince-of-tennis/lesson-48.html" },
            { title: "三年後：系列的最後一頁", url: "topics/prince-of-tennis/lesson-49.html" }
          ]
        },
        {
          title: "模組 N｜番外：劇場版與 OVA 總整理",
          courses: [
            { title: "劇場版《二人武士》與《英國式庭球城決戰》", url: "topics/prince-of-tennis/lesson-50.html" },
            { title: "OVA《全國大賽篇》與《跡部的禮物》", url: "topics/prince-of-tennis/lesson-51.html" },
            { title: "《Game of Future》與番外總結", url: "topics/prince-of-tennis/lesson-52.html" }
          ]
        },
        {
          title: "模組 O｜人物①：青學正選",
          courses: [
            { title: "越前龍馬：天才的成長難題", url: "topics/prince-of-tennis/lesson-53.html" },
            { title: "手塚國光與大石秀一郎", url: "topics/prince-of-tennis/lesson-54.html" },
            { title: "不二周助與乾貞治", url: "topics/prince-of-tennis/lesson-55.html" },
            { title: "菊丸、河村、桃城與海堂", url: "topics/prince-of-tennis/lesson-56.html" }
          ]
        },
        {
          title: "模組 P｜人物②：冰帝與立海大",
          courses: [
            { title: "跡部景吾與冰帝學園", url: "topics/prince-of-tennis/lesson-57.html" },
            { title: "幸村精市與真田弦一郎", url: "topics/prince-of-tennis/lesson-58.html" },
            { title: "兩校其他重要成員", url: "topics/prince-of-tennis/lesson-59.html" }
          ]
        },
        {
          title: "模組 Q｜人物③：其他強校群像",
          courses: [
            { title: "四天寶寺：關西的享樂主義", url: "topics/prince-of-tennis/lesson-60.html" },
            { title: "六角、不動峰與其他學校", url: "topics/prince-of-tennis/lesson-61.html" },
            { title: "模組總結：校際群像的整體設計", url: "topics/prince-of-tennis/lesson-62.html" }
          ]
        },
        {
          title: "模組 R｜人物④：U-17 與海外選手",
          courses: [
            { title: "U-17 日本代表的高中生群體", url: "topics/prince-of-tennis/lesson-63.html" },
            { title: "世界盃的各國代表選手", url: "topics/prince-of-tennis/lesson-64.html" },
            { title: "越前南次郎與越前龍雅", url: "topics/prince-of-tennis/lesson-65.html" }
          ]
        },
        {
          title: "模組 S｜設定細節總整理",
          courses: [
            { title: "境界與能力層級全表", url: "topics/prince-of-tennis/lesson-66.html" },
            { title: "校際勢力圖與賽事階梯總覽", url: "topics/prince-of-tennis/lesson-67.html" },
            { title: "模組總結：設定細節的整體作用", url: "topics/prince-of-tennis/lesson-68.html" }
          ]
        },
        {
          title: "模組 T｜主題論與課程總結",
          courses: [
            { title: "享受網球：貫穿全作的核心命題", url: "topics/prince-of-tennis/lesson-69.html" },
            { title: "團體與個人：一個運動題材的悖論", url: "topics/prince-of-tennis/lesson-70.html" },
            { title: "成就與限制：一次誠實的評估", url: "topics/prince-of-tennis/lesson-71.html" },
            { title: "全課程總結與重讀建議", url: "topics/prince-of-tennis/lesson-72.html" }
          ]
        }
      ]
    },
    {
      id: "chuka-ichiban",
      category: "anime",
      title: "中華一番全紀錄：世界設定、劇情與人物完整解析（未完結）",
      description:
        "完整解析《中華一番!》系列全部五個版本：清末的地域菜系、特級廚師制度、以「心意」為最高判準的評審體系與黑暗料理界，再依時間線講完原作的拜師與五虎星大戰、《真・中華一番!》的最終決戰，到二〇一七年起連載至今的《極》：裏料理界、殉死篇與冥界篇。注意：《極》仍在連載，課程會標示取材進度。",
      icon: "🥢",
      url: "topics/chuka-ichiban/index.html",
      modules: [
        {
          title: "模組 A｜序幕：作品與版本地圖",
          courses: [
            { title: "中華一番是什麼：小川悅司與系列全貌", url: "topics/chuka-ichiban/lesson-01.html" },
            { title: "版本地圖：五個版本的關係與差異", url: "topics/chuka-ichiban/lesson-02.html" },
            { title: "這門課怎麼讀：模組結構與連載進度標示", url: "topics/chuka-ichiban/lesson-03.html" }
          ]
        },
        {
          title: "模組 B｜世界設定①：清末中國與料理界",
          courses: [
            { title: "清末中國：時代背景與料理的地位", url: "topics/chuka-ichiban/lesson-04.html" },
            { title: "地方菜系與料理界的地理版圖", url: "topics/chuka-ichiban/lesson-05.html" },
            { title: "模組總結：世界觀的基本框架", url: "topics/chuka-ichiban/lesson-06.html" }
          ]
        },
        {
          title: "模組 C｜世界設定②：特級廚師制度",
          courses: [
            { title: "特級廚師制度的等級與權威", url: "topics/chuka-ichiban/lesson-07.html" },
            { title: "特級廚師考試的內容與難度", url: "topics/chuka-ichiban/lesson-08.html" },
            { title: "模組總結：制度與個人的關係", url: "topics/chuka-ichiban/lesson-09.html" }
          ]
        },
        {
          title: "模組 D｜世界設定③：料理對決的規則",
          courses: [
            { title: "料理對決的形式與規則", url: "topics/chuka-ichiban/lesson-10.html" },
            { title: "評審體系與美味的判準", url: "topics/chuka-ichiban/lesson-11.html" },
            { title: "模組總結：料理對決的敘事結構", url: "topics/chuka-ichiban/lesson-12.html" }
          ]
        },
        {
          title: "模組 E｜世界設定④：傳說廚具",
          courses: [
            { title: "傳說廚具的體系與由來", url: "topics/chuka-ichiban/lesson-13.html" },
            { title: "廚具與使用者：資質與心境的門檻", url: "topics/chuka-ichiban/lesson-14.html" },
            { title: "模組總結：廚具體系的整體評價", url: "topics/chuka-ichiban/lesson-15.html" }
          ]
        },
        {
          title: "模組 F｜世界設定⑤：黑暗料理界",
          courses: [
            { title: "黑暗料理界的組織與目的", url: "topics/chuka-ichiban/lesson-16.html" },
            { title: "黑暗料理界的手法與社會危害", url: "topics/chuka-ichiban/lesson-17.html" },
            { title: "模組總結：世界設定的整體整合", url: "topics/chuka-ichiban/lesson-18.html" }
          ]
        },
        {
          title: "模組 G｜原作①：出身與拜師",
          courses: [
            { title: "劉昴星的出身與母親的教誨", url: "topics/chuka-ichiban/lesson-19.html" },
            { title: "拜師與初期的修行", url: "topics/chuka-ichiban/lesson-20.html" },
            { title: "模組總結：起點階段的結構任務", url: "topics/chuka-ichiban/lesson-21.html" }
          ]
        },
        {
          title: "模組 H｜原作②：特級廚師考試",
          courses: [
            { title: "考試的形式與初期關卡", url: "topics/chuka-ichiban/lesson-22.html" },
            { title: "考試中的對手與黑暗料理界的陰影", url: "topics/chuka-ichiban/lesson-23.html" },
            { title: "模組總結：考試篇的結構成就", url: "topics/chuka-ichiban/lesson-24.html" }
          ]
        },
        {
          title: "模組 I｜原作③：各地對決與伙伴集結",
          courses: [
            { title: "陽泉酒家與各地的料理對決", url: "topics/chuka-ichiban/lesson-25.html" },
            { title: "伙伴群的集結與定位", url: "topics/chuka-ichiban/lesson-26.html" },
            { title: "模組總結：旅程階段的整體評價", url: "topics/chuka-ichiban/lesson-27.html" }
          ]
        },
        {
          title: "模組 J｜原作④：五虎星與黑暗料理界大戰",
          courses: [
            { title: "五虎星：黑暗料理界的頂尖戰力", url: "topics/chuka-ichiban/lesson-28.html" },
            { title: "與五虎星的逐一對決", url: "topics/chuka-ichiban/lesson-29.html" },
            { title: "模組總結：原作階段的完結", url: "topics/chuka-ichiban/lesson-30.html" }
          ]
        },
        {
          title: "模組 K｜續篇：真・中華一番!",
          courses: [
            { title: "真・中華一番的定位與續接方式", url: "topics/chuka-ichiban/lesson-31.html" },
            { title: "黑暗料理界的真相與最終決戰", url: "topics/chuka-ichiban/lesson-32.html" },
            { title: "模組總結：續篇的完結與評價", url: "topics/chuka-ichiban/lesson-33.html" }
          ]
        },
        {
          title: "模組 L｜極①：十三回忌與新篇章的開端",
          courses: [
            { title: "極篇的起點：十三回忌與返鄉", url: "topics/chuka-ichiban/lesson-34.html" },
            { title: "太極料理宗與新的對立結構", url: "topics/chuka-ichiban/lesson-35.html" },
            { title: "模組總結：極篇開端的結構設計", url: "topics/chuka-ichiban/lesson-36.html" }
          ]
        },
        {
          title: "模組 M｜極②：裏料理界與父親的過去",
          courses: [
            { title: "裏料理界的結構與重整", url: "topics/chuka-ichiban/lesson-37.html" },
            { title: "劉瑪利的過去與宿命的糾葛", url: "topics/chuka-ichiban/lesson-38.html" },
            { title: "模組總結：兩代人的對照", url: "topics/chuka-ichiban/lesson-39.html" }
          ]
        },
        {
          title: "模組 N｜極③：殉死與犧牲",
          courses: [
            { title: "極篇的沉重轉折：犧牲的描寫", url: "topics/chuka-ichiban/lesson-40.html" },
            { title: "模組總結：沉重段落的敘事功能", url: "topics/chuka-ichiban/lesson-41.html" }
          ]
        },
        {
          title: "模組 O｜極④：冥界篇（連載中）",
          courses: [
            { title: "冥界篇的開端：主角之死", url: "topics/chuka-ichiban/lesson-42.html" },
            { title: "冥界篇的主題與可能方向", url: "topics/chuka-ichiban/lesson-43.html" }
          ]
        },
        {
          title: "模組 P｜動畫改編差異整理",
          courses: [
            { title: "一九九七年動畫版的改編特徵", url: "topics/chuka-ichiban/lesson-44.html" },
            { title: "二〇一九年動畫《極》的重製方向", url: "topics/chuka-ichiban/lesson-45.html" },
            { title: "模組總結：版本差異的整體判斷", url: "topics/chuka-ichiban/lesson-46.html" }
          ]
        },
        {
          title: "模組 Q｜人物①：昴星與伙伴",
          courses: [
            { title: "劉昴星：不變的信念與成長", url: "topics/chuka-ichiban/lesson-47.html" },
            { title: "梅麗、紹安與四郎", url: "topics/chuka-ichiban/lesson-48.html" },
            { title: "模組總結：伙伴群的設計評價", url: "topics/chuka-ichiban/lesson-49.html" }
          ]
        },
        {
          title: "模組 R｜人物②：五虎星",
          courses: [
            { title: "五虎星的整體結構與分工", url: "topics/chuka-ichiban/lesson-50.html" },
            { title: "五虎星的動機與轉化", url: "topics/chuka-ichiban/lesson-51.html" },
            { title: "模組總結：反派群像的評價", url: "topics/chuka-ichiban/lesson-52.html" }
          ]
        },
        {
          title: "模組 S｜人物③：反派與極篇新角色",
          courses: [
            { title: "黑暗料理界的高層與核心反派", url: "topics/chuka-ichiban/lesson-53.html" },
            { title: "極篇的新角色與新勢力", url: "topics/chuka-ichiban/lesson-54.html" },
            { title: "模組總結：反派設計的演進", url: "topics/chuka-ichiban/lesson-55.html" }
          ]
        },
        {
          title: "模組 T｜設定總表、主題論與總結",
          courses: [
            { title: "設定總表：制度、廚具與勢力", url: "topics/chuka-ichiban/lesson-56.html" },
            { title: "料理為誰而做：全作的核心命題", url: "topics/chuka-ichiban/lesson-57.html" },
            { title: "成就與限制：一次誠實的評估", url: "topics/chuka-ichiban/lesson-58.html" },
            { title: "全課程總結與追讀建議", url: "topics/chuka-ichiban/lesson-59.html" }
          ]
        }
      ]
    },
    {
      id: "evangelion",
      category: "anime",
      title: "新世紀福音戰士全紀錄：四版本、世界設定與人物完整解析",
      description:
        "完整解析《新世紀福音戰士》四條結局各不相同的故事線：先用版本地圖釐清電視版、舊劇場版、貞本漫畫版與新劇場版四部曲的分歧點，再建立第二次衝擊、使徒與 AT 力場、EVA 的生命體本質與人類補完計畫；接著依序講完四條線的劇情與收束。宗教符號部分只說明其敘事與視覺功能，不附會神學解釋。",
      icon: "🩸",
      url: "topics/evangelion/index.html",
      modules: [
        {
          title: "模組 A｜序幕：作品與四版本地圖",
          courses: [
            { title: "新世紀福音戰士是什麼：庵野秀明與製作背景", url: "topics/evangelion/lesson-01.html" },
            { title: "版本地圖：四條故事線的分歧", url: "topics/evangelion/lesson-02.html" },
            { title: "這門課怎麼讀：結構與詮釋原則", url: "topics/evangelion/lesson-03.html" },
            { title: "模組總結：閱讀這部作品的準備", url: "topics/evangelion/lesson-04.html" }
          ]
        },
        {
          title: "模組 B｜世界設定①：第二次衝擊與 2015 年的世界",
          courses: [
            { title: "第二次衝擊：世界的起點事件", url: "topics/evangelion/lesson-05.html" },
            { title: "第三新東京市與 2015 年的社會", url: "topics/evangelion/lesson-06.html" },
            { title: "模組總結：世界背景的敘事功能", url: "topics/evangelion/lesson-07.html" }
          ]
        },
        {
          title: "模組 C｜世界設定②：使徒與 AT 力場",
          courses: [
            { title: "使徒的定義與共同特徵", url: "topics/evangelion/lesson-08.html" },
            { title: "AT 力場：從物理屏障到心之壁", url: "topics/evangelion/lesson-09.html" },
            { title: "使徒的分類與戰鬥模式", url: "topics/evangelion/lesson-10.html" },
            { title: "模組總結：使徒設定的整體評價", url: "topics/evangelion/lesson-11.html" }
          ]
        },
        {
          title: "模組 D｜世界設定③：EVA 的本質",
          courses: [
            { title: "EVA 的真實身分", url: "topics/evangelion/lesson-12.html" },
            { title: "插入栓、同步率與 LCL", url: "topics/evangelion/lesson-13.html" },
            { title: "暴走、初號機與 Dummy Plug", url: "topics/evangelion/lesson-14.html" },
            { title: "模組總結：EVA 設定的主題承載", url: "topics/evangelion/lesson-15.html" }
          ]
        },
        {
          title: "模組 E｜世界設定④：NERV、SEELE 與補完計畫",
          courses: [
            { title: "NERV 的組織與真實目的", url: "topics/evangelion/lesson-16.html" },
            { title: "SEELE 與死海文書", url: "topics/evangelion/lesson-17.html" },
            { title: "人類補完計畫：核心設計與版本差異", url: "topics/evangelion/lesson-18.html" },
            { title: "模組總結：設定體系的完整閉環", url: "topics/evangelion/lesson-19.html" }
          ]
        },
        {
          title: "模組 F｜電視版①：前半的使徒戰",
          courses: [
            { title: "電視版開場：被召喚的少年", url: "topics/evangelion/lesson-20.html" },
            { title: "使徒戰與角色的逐步登場", url: "topics/evangelion/lesson-21.html" },
            { title: "模組總結：電視版前半的結構任務", url: "topics/evangelion/lesson-22.html" }
          ]
        },
        {
          title: "模組 G｜電視版②：中盤的崩壞",
          courses: [
            { title: "戰鬥代價的真實化", url: "topics/evangelion/lesson-23.html" },
            { title: "角色心理的逐步瓦解", url: "topics/evangelion/lesson-24.html" },
            { title: "模組總結：中盤轉向的評價", url: "topics/evangelion/lesson-25.html" }
          ]
        },
        {
          title: "模組 H｜電視版③：終盤與第 25、26 話",
          courses: [
            { title: "終盤：補完計畫的發動", url: "topics/evangelion/lesson-26.html" },
            { title: "第 25、26 話：內容、意圖與爭議", url: "topics/evangelion/lesson-27.html" },
            { title: "模組總結：電視版的整體評價", url: "topics/evangelion/lesson-28.html" }
          ]
        },
        {
          title: "模組 I｜舊劇場版：Air／真心為你",
          courses: [
            { title: "舊劇場版的定位與 DEATH & REBIRTH", url: "topics/evangelion/lesson-29.html" },
            { title: "Air／真心為你：外部世界的真相", url: "topics/evangelion/lesson-30.html" },
            { title: "模組總結：舊劇場版的評價", url: "topics/evangelion/lesson-31.html" }
          ]
        },
        {
          title: "模組 J｜漫畫版：貞本義行的詮釋",
          courses: [
            { title: "漫畫版的定位與主要差異", url: "topics/evangelion/lesson-32.html" },
            { title: "漫畫版的結局與詮釋", url: "topics/evangelion/lesson-33.html" }
          ]
        },
        {
          title: "模組 K｜新劇場版①：序與破",
          courses: [
            { title: "新劇場版的定位與《序》", url: "topics/evangelion/lesson-34.html" },
            { title: "《破》：明確的轉向", url: "topics/evangelion/lesson-35.html" }
          ]
        },
        {
          title: "模組 L｜新劇場版②：Q",
          courses: [
            { title: "《Q》：十四年的空白", url: "topics/evangelion/lesson-36.html" },
            { title: "模組總結：《Q》的評價與定位", url: "topics/evangelion/lesson-37.html" }
          ]
        },
        {
          title: "模組 M｜新劇場版③：終",
          courses: [
            { title: "《終》：與過去的和解", url: "topics/evangelion/lesson-38.html" },
            { title: "最終決戰與系列的收束", url: "topics/evangelion/lesson-39.html" },
            { title: "模組總結：四條故事線的最終比較", url: "topics/evangelion/lesson-40.html" }
          ]
        },
        {
          title: "模組 N｜番外：外傳與衍生作品",
          courses: [
            { title: "遊戲改編與外傳作品", url: "topics/evangelion/lesson-41.html" },
            { title: "學園版與其他衍生漫畫", url: "topics/evangelion/lesson-42.html" }
          ]
        },
        {
          title: "模組 O｜人物①：碇真嗣與碇源堂",
          courses: [
            { title: "碇真嗣：逃避與面對", url: "topics/evangelion/lesson-43.html" },
            { title: "碇源堂：鏡像中的父親", url: "topics/evangelion/lesson-44.html" },
            { title: "模組總結：父子關係作為全作核心", url: "topics/evangelion/lesson-45.html" }
          ]
        },
        {
          title: "模組 P｜人物②：綾波零與明日香",
          courses: [
            { title: "綾波零：存在的疑問", url: "topics/evangelion/lesson-46.html" },
            { title: "明日香：驕傲背後的匱乏", url: "topics/evangelion/lesson-47.html" },
            { title: "模組總結：三名駕駛員的鏡像結構", url: "topics/evangelion/lesson-48.html" }
          ]
        },
        {
          title: "模組 Q｜人物③：NERV 成員",
          courses: [
            { title: "葛城美里：監護人與復仇者", url: "topics/evangelion/lesson-49.html" },
            { title: "赤木律子與其他 NERV 成員", url: "topics/evangelion/lesson-50.html" }
          ]
        },
        {
          title: "模組 R｜人物④：渚薰與 SEELE",
          courses: [
            { title: "渚薰：無條件的接納", url: "topics/evangelion/lesson-51.html" },
            { title: "SEELE 與冬月：幕後的成年人", url: "topics/evangelion/lesson-52.html" }
          ]
        },
        {
          title: "模組 S｜設定總表與名詞辭典",
          courses: [
            { title: "EVA 機體全表", url: "topics/evangelion/lesson-53.html" },
            { title: "使徒對照與專有名詞辭典", url: "topics/evangelion/lesson-54.html" },
            { title: "模組總結：設定體系的整體評價", url: "topics/evangelion/lesson-55.html" }
          ]
        },
        {
          title: "模組 T｜主題論與課程總結",
          courses: [
            { title: "核心命題：人為什麼難以與他人相處", url: "topics/evangelion/lesson-56.html" },
            { title: "宗教符號的實際作用", url: "topics/evangelion/lesson-57.html" },
            { title: "成就與限制：一次誠實的評估", url: "topics/evangelion/lesson-58.html" },
            { title: "全課程總結與觀看建議", url: "topics/evangelion/lesson-59.html" }
          ]
        }
      ]
    },
    {
      id: "slam-dunk",
      category: "anime",
      title: "灌籃高手全紀錄：籃球設定、劇情與人物完整解析",
      description:
        "完整解析井上雄彥《灌籃高手》原作 31 卷：先建立看懂比賽所需的基礎——計分尺度、籃板與犯規這些決定勝負的隱形因素、盯人與區域防守、單敗淘汰體制與神奈川的勢力版圖；再依序講完櫻木入部、三井壽的回歸、海南的第一次敗北，到全國大賽的山王工業戰，並正面處理原作急促收尾的爭議。另整理動畫缺口與《THE FIRST SLAM DUNK》。",
      icon: "🏀",
      url: "topics/slam-dunk/index.html",
      modules: [
        {
          title: "模組 A｜序幕：作品與這門課怎麼讀",
          courses: [
            { title: "灌籃高手是什麼：井上雄彥與連載背景", url: "topics/slam-dunk/lesson-01.html" },
            { title: "版本地圖：原作、動畫與劇場版", url: "topics/slam-dunk/lesson-02.html" },
            { title: "這門課怎麼讀：模組結構說明", url: "topics/slam-dunk/lesson-03.html" }
          ]
        },
        {
          title: "模組 B｜設定①：籃球規則基礎",
          courses: [
            { title: "得分方式與比賽的基本結構", url: "topics/slam-dunk/lesson-04.html" },
            { title: "籃板、犯規與失誤", url: "topics/slam-dunk/lesson-05.html" },
            { title: "防守體系：盯人與區域", url: "topics/slam-dunk/lesson-06.html" }
          ]
        },
        {
          title: "模組 C｜設定②：位置分工與戰術",
          courses: [
            { title: "五個位置的分工", url: "topics/slam-dunk/lesson-07.html" },
            { title: "基本戰術：快攻、陣地戰與擋拆", url: "topics/slam-dunk/lesson-08.html" },
            { title: "模組總結：規則如何成為戲劇", url: "topics/slam-dunk/lesson-09.html" }
          ]
        },
        {
          title: "模組 D｜設定③：高中籃球體制",
          courses: [
            { title: "賽事階梯：從縣預賽到全國大賽", url: "topics/slam-dunk/lesson-10.html" },
            { title: "神奈川的勢力版圖", url: "topics/slam-dunk/lesson-11.html" },
            { title: "模組總結：制度背景的敘事支撐", url: "topics/slam-dunk/lesson-12.html" }
          ]
        },
        {
          title: "模組 E｜劇情①：入部與湘北的成形",
          courses: [
            { title: "櫻木花道的起點", url: "topics/slam-dunk/lesson-13.html" },
            { title: "赤木剛憲與湘北的核心", url: "topics/slam-dunk/lesson-14.html" },
            { title: "流川楓與宮城良田", url: "topics/slam-dunk/lesson-15.html" },
            { title: "模組總結：湘北成形的結構意義", url: "topics/slam-dunk/lesson-16.html" }
          ]
        },
        {
          title: "模組 F｜劇情②：三井的回歸與翔陽戰",
          courses: [
            { title: "三井壽的兩年空白", url: "topics/slam-dunk/lesson-17.html" },
            { title: "回歸後的三井與湘北的完整化", url: "topics/slam-dunk/lesson-18.html" },
            { title: "翔陽戰：第一場真正的硬仗", url: "topics/slam-dunk/lesson-19.html" },
            { title: "模組總結：三井線的完整評價", url: "topics/slam-dunk/lesson-20.html" }
          ]
        },
        {
          title: "模組 G｜劇情③：海南大附屬戰",
          courses: [
            { title: "海南大附屬：縣內霸主的構造", url: "topics/slam-dunk/lesson-21.html" },
            { title: "比賽經過與赤木的受傷", url: "topics/slam-dunk/lesson-22.html" },
            { title: "敗北的意義與湘北的重整", url: "topics/slam-dunk/lesson-23.html" }
          ]
        },
        {
          title: "模組 H｜劇情④：陵南戰與全國門票",
          courses: [
            { title: "陵南：與海南並列的頂尖", url: "topics/slam-dunk/lesson-24.html" },
            { title: "陵南戰的經過與關鍵轉折", url: "topics/slam-dunk/lesson-25.html" },
            { title: "晉級全國的意義與賽前準備", url: "topics/slam-dunk/lesson-26.html" }
          ]
        },
        {
          title: "模組 I｜劇情⑤：全國大賽豐玉戰",
          courses: [
            { title: "豐玉高中：粗暴風格的挑戰", url: "topics/slam-dunk/lesson-27.html" },
            { title: "豐玉戰的經過與湘北的應對", url: "topics/slam-dunk/lesson-28.html" },
            { title: "模組總結：通往山王之戰", url: "topics/slam-dunk/lesson-29.html" }
          ]
        },
        {
          title: "模組 J｜劇情⑥：山王工業戰（上）",
          courses: [
            { title: "山王工業：絕對王者的構造", url: "topics/slam-dunk/lesson-30.html" },
            { title: "開場的壓制與二十分差", url: "topics/slam-dunk/lesson-31.html" },
            { title: "湘北的反擊與戰術調整", url: "topics/slam-dunk/lesson-32.html" },
            { title: "模組總結：山王戰上半的結構", url: "topics/slam-dunk/lesson-33.html" }
          ]
        },
        {
          title: "模組 K｜劇情⑦：山王工業戰（下）與結局",
          courses: [
            { title: "赤木、三井與宮城的極限", url: "topics/slam-dunk/lesson-34.html" },
            { title: "流川對澤北與櫻木的覺悟", url: "topics/slam-dunk/lesson-35.html" },
            { title: "決勝的最後時刻", url: "topics/slam-dunk/lesson-36.html" },
            { title: "原作的結局與收尾爭議", url: "topics/slam-dunk/lesson-37.html" }
          ]
        },
        {
          title: "模組 L｜番外：劇場版與後日談",
          courses: [
            { title: "TV 動畫與舊劇場版", url: "topics/slam-dunk/lesson-38.html" },
            { title: "THE FIRST SLAM DUNK：作者的再詮釋", url: "topics/slam-dunk/lesson-39.html" },
            { title: "十日後與角色的後續", url: "topics/slam-dunk/lesson-40.html" }
          ]
        },
        {
          title: "模組 M｜人物①：湘北先發五人",
          courses: [
            { title: "櫻木花道：從門外漢到關鍵球員", url: "topics/slam-dunk/lesson-41.html" },
            { title: "流川楓與赤木剛憲", url: "topics/slam-dunk/lesson-42.html" },
            { title: "三井壽與宮城良田", url: "topics/slam-dunk/lesson-43.html" }
          ]
        },
        {
          title: "模組 N｜人物②：安西教練與湘北其他成員",
          courses: [
            { title: "安西教練：教練角色的典範", url: "topics/slam-dunk/lesson-44.html" },
            { title: "湘北的其他成員", url: "topics/slam-dunk/lesson-45.html" },
            { title: "模組總結：湘北群像的完整結構", url: "topics/slam-dunk/lesson-46.html" }
          ]
        },
        {
          title: "模組 O｜人物③：神奈川的對手",
          courses: [
            { title: "牧紳一與海南大附屬", url: "topics/slam-dunk/lesson-47.html" },
            { title: "仙道彰與陵南、翔陽", url: "topics/slam-dunk/lesson-48.html" }
          ]
        },
        {
          title: "模組 P｜人物④：全國強校",
          courses: [
            { title: "澤北榮治：全國第一的孤獨", url: "topics/slam-dunk/lesson-49.html" },
            { title: "山王的其他成員與全國強校", url: "topics/slam-dunk/lesson-50.html" },
            { title: "模組總結：對手群像的整體評價", url: "topics/slam-dunk/lesson-51.html" }
          ]
        },
        {
          title: "模組 Q｜設定總表與戰力對照",
          courses: [
            { title: "球隊戰力對照總表", url: "topics/slam-dunk/lesson-52.html" },
            { title: "賽事階梯與劇情對照", url: "topics/slam-dunk/lesson-53.html" },
            { title: "模組總結：結構設計的整體評價", url: "topics/slam-dunk/lesson-54.html" }
          ]
        },
        {
          title: "模組 R｜主題論",
          courses: [
            { title: "天才與努力：作品的核心對話", url: "topics/slam-dunk/lesson-55.html" },
            { title: "青春的有限性：時間作為主題", url: "topics/slam-dunk/lesson-56.html" },
            { title: "成就與限制：一次誠實的評估", url: "topics/slam-dunk/lesson-57.html" }
          ]
        },
        {
          title: "模組 S｜課程總結",
          courses: [
            { title: "全課程總結與重讀建議", url: "topics/slam-dunk/lesson-58.html" },
            { title: "延伸閱讀與相關課程", url: "topics/slam-dunk/lesson-59.html" }
          ]
        }
      ]
    },
    {
      id: "death-note",
      category: "anime",
      title: "死亡筆記本全紀錄：規則體系、鬥智與主題完整解析",
      description:
        "完整解析《DEATH NOTE 死亡筆記本》全 12 卷：先建立這部作品的敘事引擎——死亡筆記的完整規則體系（尤其是放棄後失憶這條最重要的佈局工具）、死神與死神之眼、L 的推理方法論；再依序講完基拉的誕生、L 登場與電視挑釁、全作最經典的失憶計謀、L 之死，到尼亞與梅洛接手的最終對決與月的結局。",
      icon: "📓",
      url: "topics/death-note/index.html",
      modules: [
        {
          title: "模組 A｜序幕：作品與版本地圖",
          courses: [
            { title: "死亡筆記本是什麼：作者與連載背景", url: "topics/death-note/lesson-01.html" },
            { title: "版本地圖：原作、動畫與改編", url: "topics/death-note/lesson-02.html" },
            { title: "這門課怎麼讀：結構與閱讀原則", url: "topics/death-note/lesson-03.html" }
          ]
        },
        {
          title: "模組 B｜設定①：死亡筆記的規則體系",
          courses: [
            { title: "基本規則：筆記如何運作", url: "topics/death-note/lesson-04.html" },
            { title: "進階規則：操控死亡的細節", url: "topics/death-note/lesson-05.html" },
            { title: "規則的漏洞與被隱瞞的規則", url: "topics/death-note/lesson-06.html" }
          ]
        },
        {
          title: "模組 C｜設定②：死神與死神之眼",
          courses: [
            { title: "死神與死神界", url: "topics/death-note/lesson-07.html" },
            { title: "死神之眼與壽命交易", url: "topics/death-note/lesson-08.html" },
            { title: "模組總結：設定作為敘事引擎", url: "topics/death-note/lesson-09.html" }
          ]
        },
        {
          title: "模組 D｜設定③：推理框架與鬥智邏輯",
          courses: [
            { title: "L 的推理方法論", url: "topics/death-note/lesson-10.html" },
            { title: "夜神月的行動邏輯", url: "topics/death-note/lesson-11.html" },
            { title: "模組總結：鬥智作品的成立條件", url: "topics/death-note/lesson-12.html" }
          ]
        },
        {
          title: "模組 E｜劇情①：基拉的誕生",
          courses: [
            { title: "筆記的獲得與最初的選擇", url: "topics/death-note/lesson-13.html" },
            { title: "基拉現象與社會的反應", url: "topics/death-note/lesson-14.html" },
            { title: "模組總結：起點階段的結構", url: "topics/death-note/lesson-15.html" }
          ]
        },
        {
          title: "模組 F｜劇情②：L 登場與第一次交鋒",
          courses: [
            { title: "L 的登場與電視挑釁", url: "topics/death-note/lesson-16.html" },
            { title: "警方的介入與月的滲透", url: "topics/death-note/lesson-17.html" },
            { title: "模組總結：第一階段的攻防評價", url: "topics/death-note/lesson-18.html" }
          ]
        },
        {
          title: "模組 G｜劇情③：第二基拉與彌海砂",
          courses: [
            { title: "第二基拉的出現", url: "topics/death-note/lesson-19.html" },
            { title: "彌海砂：崇拜與利用", url: "topics/death-note/lesson-20.html" },
            { title: "模組總結：第二基拉篇的結構作用", url: "topics/death-note/lesson-21.html" }
          ]
        },
        {
          title: "模組 H｜劇情④：黃道社篇與失憶計謀",
          courses: [
            { title: "失憶計謀：全作最大的佈局", url: "topics/death-note/lesson-22.html" },
            { title: "黃道社篇與局勢的推進", url: "topics/death-note/lesson-23.html" },
            { title: "模組總結：佈局階段的評價", url: "topics/death-note/lesson-24.html" }
          ]
        },
        {
          title: "模組 I｜劇情⑤：L 之死",
          courses: [
            { title: "L 的最後推理", url: "topics/death-note/lesson-25.html" },
            { title: "L 之死與敘事意義", url: "topics/death-note/lesson-26.html" }
          ]
        },
        {
          title: "模組 J｜劇情⑥：尼亞與梅洛",
          courses: [
            { title: "繼承者的登場：尼亞與梅洛", url: "topics/death-note/lesson-27.html" },
            { title: "新局勢與基拉的體制化", url: "topics/death-note/lesson-28.html" },
            { title: "模組總結：後半段的結構評價", url: "topics/death-note/lesson-29.html" }
          ]
        },
        {
          title: "模組 K｜劇情⑦：最終對決與結局",
          courses: [
            { title: "最終對決的佈局", url: "topics/death-note/lesson-30.html" },
            { title: "結局與月的最後時刻", url: "topics/death-note/lesson-31.html" },
            { title: "模組總結：結局的整體評價", url: "topics/death-note/lesson-32.html" }
          ]
        },
        {
          title: "模組 L｜番外：短篇、小說與改編",
          courses: [
            { title: "後續短篇與小說", url: "topics/death-note/lesson-33.html" },
            { title: "影視改編與其差異", url: "topics/death-note/lesson-34.html" }
          ]
        },
        {
          title: "模組 M｜人物①：夜神月",
          courses: [
            { title: "夜神月的心理構造", url: "topics/death-note/lesson-35.html" },
            { title: "月與周圍人的關係", url: "topics/death-note/lesson-36.html" }
          ]
        },
        {
          title: "模組 N｜人物②：L",
          courses: [
            { title: "L 的角色構造與方法論", url: "topics/death-note/lesson-37.html" },
            { title: "L 的魅力來源與失敗的意義", url: "topics/death-note/lesson-38.html" }
          ]
        },
        {
          title: "模組 O｜人物③：尼亞、梅洛與搜查本部",
          courses: [
            { title: "尼亞與梅洛的角色分析", url: "topics/death-note/lesson-39.html" },
            { title: "搜查本部與夜神總一郎", url: "topics/death-note/lesson-40.html" }
          ]
        },
        {
          title: "模組 P｜人物④：死神與彌海砂",
          courses: [
            { title: "流克與雷姆：兩種死神", url: "topics/death-note/lesson-41.html" },
            { title: "彌海砂的完整角色分析", url: "topics/death-note/lesson-42.html" }
          ]
        },
        {
          title: "模組 Q｜設定總表與時間線",
          courses: [
            { title: "死亡筆記規則全表與事件時間線", url: "topics/death-note/lesson-43.html" },
            { title: "模組總結：設定完整性的評價", url: "topics/death-note/lesson-44.html" }
          ]
        },
        {
          title: "模組 R｜主題論",
          courses: [
            { title: "正義的定義：作品的核心提問", url: "topics/death-note/lesson-45.html" },
            { title: "權力的腐蝕與規則的敘事價值", url: "topics/death-note/lesson-46.html" },
            { title: "成就與限制：一次誠實的評估", url: "topics/death-note/lesson-47.html" }
          ]
        },
        {
          title: "模組 S｜課程總結",
          courses: [
            { title: "全課程總結與重讀建議", url: "topics/death-note/lesson-48.html" }
          ]
        }
      ]
    },
    {
      id: "conan-main-plot",
      category: "anime",
      title: "名偵探柯南主線全解析：黑衣組織線完整整理（未完結）",
      description:
        "只講主線、不含日常單元案件的《名偵探柯南》黑衣組織線完整整理。先建立 APTX4869 與幼化的機制、組織的階層與酒名代號、FBI／CIA／公安三方角力，再依揭露順序講完主線九個階段——從新一被下藥、灰原哀的叛離、赤井與緋色系列，到波本＝降谷零與 RUM 的確認。注意：本作仍在連載，取材截至 FILE.1150 前後。",
      icon: "🔍",
      url: "topics/conan-main-plot/index.html",
      modules: [
        {
          title: "模組 A｜序幕：作品與主線的取捨",
          courses: [
            { title: "名偵探柯南是什麼：青山剛昌與連載規模", url: "topics/conan-main-plot/lesson-01.html" },
            { title: "只講主線：取捨說明與課程範圍", url: "topics/conan-main-plot/lesson-02.html" },
            { title: "這門課怎麼讀：模組結構說明", url: "topics/conan-main-plot/lesson-03.html" }
          ]
        },
        {
          title: "模組 B｜設定①：APTX4869 與幼化",
          courses: [
            { title: "APTX4869：作品的起點設定", url: "topics/conan-main-plot/lesson-04.html" },
            { title: "解藥與暫時性恢復", url: "topics/conan-main-plot/lesson-05.html" },
            { title: "模組總結：起點設定的評價", url: "topics/conan-main-plot/lesson-06.html" }
          ]
        },
        {
          title: "模組 C｜設定②：黑衣組織的架構",
          courses: [
            { title: "組織的性質與酒名代號規則", url: "topics/conan-main-plot/lesson-07.html" },
            { title: "組織的階層結構與主要成員", url: "topics/conan-main-plot/lesson-08.html" }
          ]
        },
        {
          title: "模組 D｜設定③：各國情報機關",
          courses: [
            { title: "FBI、CIA 與日本公安的三方角力", url: "topics/conan-main-plot/lesson-09.html" },
            { title: "臥底設定的運作與風險", url: "topics/conan-main-plot/lesson-10.html" }
          ]
        },
        {
          title: "模組 E｜主線①：起點",
          courses: [
            { title: "工藤新一與組織的第一次接觸", url: "topics/conan-main-plot/lesson-11.html" },
            { title: "初期的追查與資訊的匱乏", url: "topics/conan-main-plot/lesson-12.html" }
          ]
        },
        {
          title: "模組 F｜主線②：灰原哀與雪莉",
          courses: [
            { title: "灰原哀的登場", url: "topics/conan-main-plot/lesson-13.html" },
            { title: "組織的追查與持續的威脅", url: "topics/conan-main-plot/lesson-14.html" },
            { title: "模組總結：資訊格局的轉變", url: "topics/conan-main-plot/lesson-15.html" }
          ]
        },
        {
          title: "模組 G｜主線③：貝爾摩德篇",
          courses: [
            { title: "貝爾摩德：變裝與不可捉摸的立場", url: "topics/conan-main-plot/lesson-16.html" },
            { title: "月影島與紐約的回憶", url: "topics/conan-main-plot/lesson-17.html" },
            { title: "模組總結：貝爾摩德篇的定位", url: "topics/conan-main-plot/lesson-18.html" }
          ]
        },
        {
          title: "模組 H｜主線④：赤井秀一與 FBI",
          courses: [
            { title: "赤井秀一與 FBI 的登場", url: "topics/conan-main-plot/lesson-19.html" },
            { title: "衝突的升級與雙方的損耗", url: "topics/conan-main-plot/lesson-20.html" },
            { title: "模組總結：三方格局的形成", url: "topics/conan-main-plot/lesson-21.html" }
          ]
        },
        {
          title: "模組 I｜主線⑤：緋色系列",
          courses: [
            { title: "赤井的「死亡」與其疑點", url: "topics/conan-main-plot/lesson-22.html" },
            { title: "緋色系列的真相揭露", url: "topics/conan-main-plot/lesson-23.html" },
            { title: "模組總結：緋色系列的定位", url: "topics/conan-main-plot/lesson-24.html" }
          ]
        },
        {
          title: "模組 J｜主線⑥：基爾與雙重間諜",
          courses: [
            { title: "基爾的雙重身分", url: "topics/conan-main-plot/lesson-25.html" },
            { title: "模組總結：臥底線的展開", url: "topics/conan-main-plot/lesson-26.html" }
          ]
        },
        {
          title: "模組 K｜主線⑦：波本與公安線",
          courses: [
            { title: "波本的多重身分", url: "topics/conan-main-plot/lesson-27.html" },
            { title: "公安線與臥底格局的完成", url: "topics/conan-main-plot/lesson-28.html" }
          ]
        },
        {
          title: "模組 L｜主線⑧：羽田浩司事件與 RUM 之謎",
          courses: [
            { title: "羽田浩司事件：十七年前的案件", url: "topics/conan-main-plot/lesson-29.html" },
            { title: "臨終留言的解讀與 RUM 的線索", url: "topics/conan-main-plot/lesson-30.html" }
          ]
        },
        {
          title: "模組 M｜主線⑨：RUM 的回收與最新進展",
          courses: [
            { title: "RUM 的身分揭曉", url: "topics/conan-main-plot/lesson-31.html" },
            { title: "烏丸蓮耶與組織首領之謎", url: "topics/conan-main-plot/lesson-32.html" }
          ]
        },
        {
          title: "模組 N｜番外：主線相關劇場版",
          courses: [
            { title: "主線相關劇場版的篩選", url: "topics/conan-main-plot/lesson-33.html" },
            { title: "主線相關劇場版的個別整理", url: "topics/conan-main-plot/lesson-34.html" }
          ]
        },
        {
          title: "模組 O｜人物①：柯南與灰原哀",
          courses: [
            { title: "工藤新一／江戶川柯南", url: "topics/conan-main-plot/lesson-35.html" },
            { title: "灰原哀的完整角色分析", url: "topics/conan-main-plot/lesson-36.html" }
          ]
        },
        {
          title: "模組 P｜人物②：組織幹部",
          courses: [
            { title: "琴酒：組織的執行者", url: "topics/conan-main-plot/lesson-37.html" },
            { title: "貝爾摩德、RUM 與其他幹部", url: "topics/conan-main-plot/lesson-38.html" }
          ]
        },
        {
          title: "模組 Q｜人物③：赤井秀一與安室透",
          courses: [
            { title: "赤井秀一與安室透的對照", url: "topics/conan-main-plot/lesson-39.html" },
            { title: "兩人與柯南的關係", url: "topics/conan-main-plot/lesson-40.html" }
          ]
        },
        {
          title: "模組 R｜設定總表與主線時間線",
          courses: [
            { title: "代號對照表與身分總整理", url: "topics/conan-main-plot/lesson-41.html" },
            { title: "主線時間線總覽", url: "topics/conan-main-plot/lesson-42.html" }
          ]
        },
        {
          title: "模組 S｜主題論與課程總結",
          courses: [
            { title: "主題論：身分、信任與長期追查", url: "topics/conan-main-plot/lesson-43.html" },
            { title: "成就與限制：一次誠實的評估", url: "topics/conan-main-plot/lesson-44.html" },
            { title: "全課程總結與追讀建議", url: "topics/conan-main-plot/lesson-45.html" }
          ]
        }
      ]
    },
    {
      id: "sailor-moon",
      category: "anime",
      title: "美少女戰士全紀錄：世界設定、五大篇章與人物完整解析",
      description:
        "完整解析《美少女戰士》：先用版本地圖釐清原作漫畫、九〇年代動畫、Crystal 系列與真人版的差異，再建立銀千年王國與前世轉生、銀水晶的生命代價、以行星為框架的戰士體系；接著依原作五個篇章講完劇情，從黑暗王國篇到星光戰士篇，並整理舊動畫的原創內容與不同結局，最後以「溫柔作為力量」的主題論收束。",
      icon: "🌙",
      url: "topics/sailor-moon/index.html",
      modules: [
        {
          title: "模組 A｜序幕：作品與四條版本線",
          courses: [
            { title: "美少女戰士是什麼：武內直子與作品地位", url: "topics/sailor-moon/lesson-01.html" },
            { title: "版本地圖：四條版本線", url: "topics/sailor-moon/lesson-02.html" },
            { title: "原作五篇章的結構總覽", url: "topics/sailor-moon/lesson-03.html" },
            { title: "這門課怎麼讀：模組結構說明", url: "topics/sailor-moon/lesson-04.html" }
          ]
        },
        {
          title: "模組 B｜設定①：銀千年王國與前世",
          courses: [
            { title: "銀千年王國：前世的設定", url: "topics/sailor-moon/lesson-05.html" },
            { title: "轉生與記憶的覺醒", url: "topics/sailor-moon/lesson-06.html" },
            { title: "模組總結：前世設定的整體評價", url: "topics/sailor-moon/lesson-07.html" }
          ]
        },
        {
          title: "模組 C｜設定②：銀水晶與變身道具",
          courses: [
            { title: "銀水晶：核心力量的設定", url: "topics/sailor-moon/lesson-08.html" },
            { title: "變身道具的體系與層級", url: "topics/sailor-moon/lesson-09.html" },
            { title: "變身的意義與儀式性", url: "topics/sailor-moon/lesson-10.html" }
          ]
        },
        {
          title: "模組 D｜設定③：戰士體系",
          courses: [
            { title: "守護星與行星力量", url: "topics/sailor-moon/lesson-11.html" },
            { title: "內部戰士與外部戰士的分野", url: "topics/sailor-moon/lesson-12.html" },
            { title: "Sailor Crystal 與力量的本質", url: "topics/sailor-moon/lesson-13.html" },
            { title: "模組總結：戰士體系的整體評價", url: "topics/sailor-moon/lesson-14.html" }
          ]
        },
        {
          title: "模組 E｜設定④：敵對勢力通論",
          courses: [
            { title: "敵對勢力的共通結構", url: "topics/sailor-moon/lesson-15.html" },
            { title: "各篇敵人代表的主題威脅", url: "topics/sailor-moon/lesson-16.html" },
            { title: "模組總結：設定體系的整合", url: "topics/sailor-moon/lesson-17.html" }
          ]
        },
        {
          title: "模組 F｜劇情①：黑暗王國篇",
          courses: [
            { title: "覺醒與戰士的集結", url: "topics/sailor-moon/lesson-18.html" },
            { title: "前世的揭露與地場衛", url: "topics/sailor-moon/lesson-19.html" },
            { title: "四天王與黑暗王國的結局", url: "topics/sailor-moon/lesson-20.html" },
            { title: "模組總結：第一篇的結構評價", url: "topics/sailor-moon/lesson-21.html" }
          ]
        },
        {
          title: "模組 G｜劇情②：黑月一族篇",
          courses: [
            { title: "小小兔與未來的水晶東京", url: "topics/sailor-moon/lesson-22.html" },
            { title: "黑月一族與被排除者的憤怒", url: "topics/sailor-moon/lesson-23.html" },
            { title: "小小兔的成長與第二篇結局", url: "topics/sailor-moon/lesson-24.html" }
          ]
        },
        {
          title: "模組 H｜劇情③：無限學園篇",
          courses: [
            { title: "外部戰士的登場與立場", url: "topics/sailor-moon/lesson-25.html" },
            { title: "土星戰士與犧牲的兩難", url: "topics/sailor-moon/lesson-26.html" },
            { title: "死亡巴斯達與第三篇結局", url: "topics/sailor-moon/lesson-27.html" },
            { title: "模組總結：第三篇的倫理討論", url: "topics/sailor-moon/lesson-28.html" }
          ]
        },
        {
          title: "模組 I｜劇情④：死亡之月篇",
          courses: [
            { title: "死亡之月馬戲團與夢的設定", url: "topics/sailor-moon/lesson-29.html" },
            { title: "小小兔的成長線與這一篇的核心", url: "topics/sailor-moon/lesson-30.html" },
            { title: "第四篇的結局與主題收束", url: "topics/sailor-moon/lesson-31.html" }
          ]
        },
        {
          title: "模組 J｜劇情⑤：星光戰士篇與結局",
          courses: [
            { title: "星光戰士與銀河的規模", url: "topics/sailor-moon/lesson-32.html" },
            { title: "Shadow Galactica 與最終的威脅", url: "topics/sailor-moon/lesson-33.html" },
            { title: "最終決戰與原作結局", url: "topics/sailor-moon/lesson-34.html" },
            { title: "模組總結：原作五篇的整體評價", url: "topics/sailor-moon/lesson-35.html" }
          ]
        },
        {
          title: "模組 K｜舊動畫版的改編差異",
          courses: [
            { title: "舊動畫的整體改編方向", url: "topics/sailor-moon/lesson-36.html" },
            { title: "各期的原創內容與結構差異", url: "topics/sailor-moon/lesson-37.html" },
            { title: "播映版本的改動與相關討論", url: "topics/sailor-moon/lesson-38.html" },
            { title: "模組總結：版本差異的整體判斷", url: "topics/sailor-moon/lesson-39.html" }
          ]
        },
        {
          title: "模組 L｜番外：前身作品、劇場版與真人版",
          courses: [
            { title: "前身作品《Codename: Sailor V》", url: "topics/sailor-moon/lesson-40.html" },
            { title: "劇場版與短篇作品", url: "topics/sailor-moon/lesson-41.html" },
            { title: "真人版與其他改編", url: "topics/sailor-moon/lesson-42.html" },
            { title: "模組總結：番外作品的整體定位", url: "topics/sailor-moon/lesson-43.html" }
          ]
        },
        {
          title: "模組 M｜人物①：月野兔與內部戰士",
          courses: [
            { title: "月野兔：從普通女孩到守護者", url: "topics/sailor-moon/lesson-44.html" },
            { title: "水星與火星戰士", url: "topics/sailor-moon/lesson-45.html" },
            { title: "木星與金星戰士", url: "topics/sailor-moon/lesson-46.html" }
          ]
        },
        {
          title: "模組 N｜人物②：外部戰士",
          courses: [
            { title: "天王星與海王星", url: "topics/sailor-moon/lesson-47.html" },
            { title: "冥王星與土星戰士", url: "topics/sailor-moon/lesson-48.html" },
            { title: "模組總結：外部戰士的群像評價", url: "topics/sailor-moon/lesson-49.html" }
          ]
        },
        {
          title: "模組 O｜人物③：地場衛、小小兔與月家",
          courses: [
            { title: "地場衛的角色與功能", url: "topics/sailor-moon/lesson-50.html" },
            { title: "小小兔的完整角色線", url: "topics/sailor-moon/lesson-51.html" }
          ]
        },
        {
          title: "模組 P｜人物④：反派群像",
          courses: [
            { title: "反派設計的共通原則", url: "topics/sailor-moon/lesson-52.html" },
            { title: "各篇反派的個別分析", url: "topics/sailor-moon/lesson-53.html" },
            { title: "模組總結：反派群像的整體評價", url: "topics/sailor-moon/lesson-54.html" }
          ]
        },
        {
          title: "模組 Q｜設定總表",
          courses: [
            { title: "戰士全表與能力對照", url: "topics/sailor-moon/lesson-55.html" },
            { title: "篇章與敵人對照總表", url: "topics/sailor-moon/lesson-56.html" }
          ]
        },
        {
          title: "模組 R｜主題論",
          courses: [
            { title: "溫柔作為力量：全作的核心命題", url: "topics/sailor-moon/lesson-57.html" },
            { title: "對魔法少女類型的重構", url: "topics/sailor-moon/lesson-58.html" },
            { title: "成就與限制：一次誠實的評估", url: "topics/sailor-moon/lesson-59.html" }
          ]
        },
        {
          title: "模組 S｜課程總結",
          courses: [
            { title: "全課程總結與觀賞建議", url: "topics/sailor-moon/lesson-60.html" },
            { title: "延伸閱讀與相關課程", url: "topics/sailor-moon/lesson-61.html" }
          ]
        }
      ]
    },
    {
      id: "cardcaptor-sakura",
      category: "anime",
      title: "庫洛魔法使全紀錄：魔法設定、劇情與人物完整解析",
      description:
        "完整解析 CLAMP《庫洛魔法使》原作 12 卷與續篇《透明牌篇》16 卷（二〇二四年完結）：庫洛牌體系與屬性、兩名守護者、以失去最重要的感情為代價的最終之審判，再依序講完收集篇、與親近之人的對決、小櫻牌的轉化，以及續篇的力量失效與透明牌之謎。注意：《透明牌篇》動畫僅涵蓋前段，完整結局只在漫畫中。",
      icon: "🌸",
      url: "topics/cardcaptor-sakura/index.html",
      modules: [
        {
          title: "模組 A｜序幕：作品與版本地圖",
          courses: [
            { title: "庫洛魔法使是什麼：CLAMP 與作品定位", url: "topics/cardcaptor-sakura/lesson-01.html" },
            { title: "版本地圖：漫畫、動畫與續篇", url: "topics/cardcaptor-sakura/lesson-02.html" },
            { title: "這門課怎麼讀：模組結構說明", url: "topics/cardcaptor-sakura/lesson-03.html" }
          ]
        },
        {
          title: "模組 B｜設定①：庫洛牌體系",
          courses: [
            { title: "庫洛牌的基本設定", url: "topics/cardcaptor-sakura/lesson-04.html" },
            { title: "屬性分類與牌卡體系", url: "topics/cardcaptor-sakura/lesson-05.html" },
            { title: "收服的機制與封印之鑰", url: "topics/cardcaptor-sakura/lesson-06.html" }
          ]
        },
        {
          title: "模組 C｜設定②：魔法體系",
          courses: [
            { title: "西方魔法與東方道術的並置", url: "topics/cardcaptor-sakura/lesson-07.html" },
            { title: "魔力的性質與成長", url: "topics/cardcaptor-sakura/lesson-08.html" },
            { title: "模組總結：魔法體系的整體設計", url: "topics/cardcaptor-sakura/lesson-09.html" }
          ]
        },
        {
          title: "模組 D｜設定③：守護者與審判",
          courses: [
            { title: "兩名守護者的設定", url: "topics/cardcaptor-sakura/lesson-10.html" },
            { title: "最終之審判的設定與意義", url: "topics/cardcaptor-sakura/lesson-11.html" },
            { title: "模組總結：守護者體系的設計", url: "topics/cardcaptor-sakura/lesson-12.html" }
          ]
        },
        {
          title: "模組 E｜設定④：庫洛．里德與傳承",
          courses: [
            { title: "庫洛．里德：創造者的設定", url: "topics/cardcaptor-sakura/lesson-13.html" },
            { title: "傳承的結構與轉生的設定", url: "topics/cardcaptor-sakura/lesson-14.html" }
          ]
        },
        {
          title: "模組 F｜劇情①：庫洛牌收集篇",
          courses: [
            { title: "開場與收集的開始", url: "topics/cardcaptor-sakura/lesson-15.html" },
            { title: "單元結構與收集的節奏", url: "topics/cardcaptor-sakura/lesson-16.html" },
            { title: "主角的成長與能力的建立", url: "topics/cardcaptor-sakura/lesson-17.html" }
          ]
        },
        {
          title: "模組 G｜劇情②：李小狼與競爭關係",
          courses: [
            { title: "李小狼的登場與立場", url: "topics/cardcaptor-sakura/lesson-18.html" },
            { title: "從競爭到合作的關係轉變", url: "topics/cardcaptor-sakura/lesson-19.html" }
          ]
        },
        {
          title: "模組 H｜劇情③：最終之審判",
          courses: [
            { title: "審判的啟動與對決", url: "topics/cardcaptor-sakura/lesson-20.html" },
            { title: "審判的結果與收集篇的收束", url: "topics/cardcaptor-sakura/lesson-21.html" }
          ]
        },
        {
          title: "模組 I｜劇情④：小櫻牌篇與艾利歐",
          courses: [
            { title: "艾利歐的登場與新的試煉", url: "topics/cardcaptor-sakura/lesson-22.html" },
            { title: "小櫻牌的轉化與力量的獨立", url: "topics/cardcaptor-sakura/lesson-23.html" },
            { title: "模組總結：第二階段的意義", url: "topics/cardcaptor-sakura/lesson-24.html" }
          ]
        },
        {
          title: "模組 J｜劇情⑤：原作結局",
          courses: [
            { title: "原作的收尾與感情的處理", url: "topics/cardcaptor-sakura/lesson-25.html" },
            { title: "原作的整體評價", url: "topics/cardcaptor-sakura/lesson-26.html" }
          ]
        },
        {
          title: "模組 K｜續篇：透明牌篇",
          courses: [
            { title: "透明牌篇的定位與開端", url: "topics/cardcaptor-sakura/lesson-27.html" },
            { title: "透明牌的設定與新的謎團", url: "topics/cardcaptor-sakura/lesson-28.html" },
            { title: "續篇的主題與情感重心", url: "topics/cardcaptor-sakura/lesson-29.html" },
            { title: "續篇的結局與整體評價", url: "topics/cardcaptor-sakura/lesson-30.html" }
          ]
        },
        {
          title: "模組 L｜番外：劇場版與動畫差異",
          courses: [
            { title: "兩部劇場版的內容與定位", url: "topics/cardcaptor-sakura/lesson-31.html" },
            { title: "動畫與漫畫的差異整理", url: "topics/cardcaptor-sakura/lesson-32.html" }
          ]
        },
        {
          title: "模組 M｜人物①：木之本櫻與家人",
          courses: [
            { title: "木之本櫻：主角的完整分析", url: "topics/cardcaptor-sakura/lesson-33.html" },
            { title: "木之本家與家庭描寫", url: "topics/cardcaptor-sakura/lesson-34.html" }
          ]
        },
        {
          title: "模組 N｜人物②：同學群像",
          courses: [
            { title: "李小狼與大道寺知世", url: "topics/cardcaptor-sakura/lesson-35.html" },
            { title: "其他同學與配角群像", url: "topics/cardcaptor-sakura/lesson-36.html" }
          ]
        },
        {
          title: "模組 O｜人物③：守護者與魔法師",
          courses: [
            { title: "兩名守護者的角色分析", url: "topics/cardcaptor-sakura/lesson-37.html" },
            { title: "庫洛．里德與艾利歐", url: "topics/cardcaptor-sakura/lesson-38.html" }
          ]
        },
        {
          title: "模組 P｜設定總表：三代牌卡",
          courses: [
            { title: "三代牌卡的對照總表", url: "topics/cardcaptor-sakura/lesson-39.html" },
            { title: "劇情階段與對應模組總表", url: "topics/cardcaptor-sakura/lesson-40.html" }
          ]
        },
        {
          title: "模組 Q｜主題論",
          courses: [
            { title: "成長：沒有創傷的成長故事", url: "topics/cardcaptor-sakura/lesson-41.html" },
            { title: "感情的多樣性與作品的立場", url: "topics/cardcaptor-sakura/lesson-42.html" },
            { title: "CLAMP 的敘事特色", url: "topics/cardcaptor-sakura/lesson-43.html" },
            { title: "成就與限制：一次誠實的評估", url: "topics/cardcaptor-sakura/lesson-44.html" }
          ]
        },
        {
          title: "模組 R｜課程總結",
          courses: [
            { title: "全課程總結與閱讀建議", url: "topics/cardcaptor-sakura/lesson-45.html" }
          ]
        }
      ]
    },
    {
      id: "pokemon-anime",
      category: "anime",
      title: "寶可夢動畫全紀錄：世界設定、歷代主線與人物完整解析（未完結）",
      description:
        "完整梳理一九九七年開播至今的寶可夢電視動畫主線：先處理最令人混亂的系列分期問題，再建立訓練家制度、道館與聯盟的階梯與各世代對戰機制；接著依地方順序講完九段主線，從關都到新無印的世界冠軍賽與二〇二三年小智篇的收束，並記錄仍在連載的新系列。另有劇場版體系、人物模組與各式速查表。",
      icon: "⚡",
      url: "topics/pokemon-anime/index.html",
      modules: [
        {
          title: "模組 A｜序幕：系列分期與主線的取捨",
          courses: [
            { title: "寶可夢動畫是什麼：規模與系列分期", url: "topics/pokemon-anime/lesson-01.html" },
            { title: "只講主線：取捨的標準", url: "topics/pokemon-anime/lesson-02.html" },
            { title: "這門課怎麼讀：模組結構說明", url: "topics/pokemon-anime/lesson-03.html" },
            { title: "主線的整體弧線預覽", url: "topics/pokemon-anime/lesson-04.html" }
          ]
        },
        {
          title: "模組 B｜設定①：訓練家制度與聯盟",
          courses: [
            { title: "訓練家制度與旅程的規則", url: "topics/pokemon-anime/lesson-05.html" },
            { title: "精靈球與夥伴關係的設定", url: "topics/pokemon-anime/lesson-06.html" },
            { title: "道館與聯盟的賽制", url: "topics/pokemon-anime/lesson-07.html" }
          ]
        },
        {
          title: "模組 C｜設定②：屬性相剋與對戰",
          courses: [
            { title: "屬性相剋的基本邏輯", url: "topics/pokemon-anime/lesson-08.html" },
            { title: "對戰的實際運作與戰術層次", url: "topics/pokemon-anime/lesson-09.html" },
            { title: "模組總結：對戰體系的整體評價", url: "topics/pokemon-anime/lesson-10.html" }
          ]
        },
        {
          title: "模組 D｜設定③：各世代機制",
          courses: [
            { title: "進化與早期的力量體系", url: "topics/pokemon-anime/lesson-11.html" },
            { title: "超級進化與 Z 招式", url: "topics/pokemon-anime/lesson-12.html" },
            { title: "極巨化與太晶化", url: "topics/pokemon-anime/lesson-13.html" }
          ]
        },
        {
          title: "模組 E｜劇情①：無印篇",
          courses: [
            { title: "起點：小智與皮卡丘的相遇", url: "topics/pokemon-anime/lesson-14.html" },
            { title: "關都地方的旅程與聯盟", url: "topics/pokemon-anime/lesson-15.html" },
            { title: "橘子群島與城都地方", url: "topics/pokemon-anime/lesson-16.html" },
            { title: "模組總結：無印篇的整體評價", url: "topics/pokemon-anime/lesson-17.html" }
          ]
        },
        {
          title: "模組 F｜劇情②：AG 豐緣篇",
          courses: [
            { title: "豐緣地方與新旅伴", url: "topics/pokemon-anime/lesson-18.html" },
            { title: "豐緣聯盟與戰鬥開拓區", url: "topics/pokemon-anime/lesson-19.html" }
          ]
        },
        {
          title: "模組 G｜劇情③：DP 神奧篇",
          courses: [
            { title: "神奧地方與最強的勁敵", url: "topics/pokemon-anime/lesson-20.html" },
            { title: "神奧聯盟與敗北的重量", url: "topics/pokemon-anime/lesson-21.html" },
            { title: "模組總結：DP 篇的成就", url: "topics/pokemon-anime/lesson-22.html" }
          ]
        },
        {
          title: "模組 H｜劇情④：BW 合眾篇",
          courses: [
            { title: "BW 的重置與爭議的來源", url: "topics/pokemon-anime/lesson-23.html" },
            { title: "合眾聯盟與這一期的實際內容", url: "topics/pokemon-anime/lesson-24.html" },
            { title: "模組總結：如何評價 BW", url: "topics/pokemon-anime/lesson-25.html" }
          ]
        },
        {
          title: "模組 I｜劇情⑤：XY 卡洛斯篇",
          courses: [
            { title: "XY 的修正與新的旅伴", url: "topics/pokemon-anime/lesson-26.html" },
            { title: "卡洛斯聯盟：最接近的一次", url: "topics/pokemon-anime/lesson-27.html" },
            { title: "模組總結：XY 的成就與遺憾", url: "topics/pokemon-anime/lesson-28.html" }
          ]
        },
        {
          title: "模組 J｜劇情⑥：SM 阿羅拉篇",
          courses: [
            { title: "SM 的形式轉向", url: "topics/pokemon-anime/lesson-29.html" },
            { title: "阿羅拉聯盟與首次奪冠", url: "topics/pokemon-anime/lesson-30.html" },
            { title: "模組總結：SM 的重新評價", url: "topics/pokemon-anime/lesson-31.html" }
          ]
        },
        {
          title: "模組 K｜劇情⑦：新無印與世界冠軍賽",
          courses: [
            { title: "新無印的結構改變", url: "topics/pokemon-anime/lesson-32.html" },
            { title: "世界冠軍賽與登頂世界第一", url: "topics/pokemon-anime/lesson-33.html" },
            { title: "模組總結：新無印的收尾功能", url: "topics/pokemon-anime/lesson-34.html" }
          ]
        },
        {
          title: "模組 L｜劇情⑧：小智篇的完結",
          courses: [
            { title: "《目標是寶可夢大師》的性質", url: "topics/pokemon-anime/lesson-35.html" },
            { title: "小智篇的收尾與最後的畫面", url: "topics/pokemon-anime/lesson-36.html" }
          ]
        },
        {
          title: "模組 M｜新系列（連載中）",
          courses: [
            { title: "新系列的開始與新主角", url: "topics/pokemon-anime/lesson-37.html" },
            { title: "新系列的進展與現況", url: "topics/pokemon-anime/lesson-38.html" }
          ]
        },
        {
          title: "模組 N｜番外：劇場版體系",
          courses: [
            { title: "劇場版的整體體系", url: "topics/pokemon-anime/lesson-39.html" },
            { title: "兩條劇場版線的區分", url: "topics/pokemon-anime/lesson-40.html" },
            { title: "模組總結：劇場版的整體定位", url: "topics/pokemon-anime/lesson-41.html" }
          ]
        },
        {
          title: "模組 O｜人物①：小智與皮卡丘",
          courses: [
            { title: "小智：二十六年的角色分析", url: "topics/pokemon-anime/lesson-42.html" },
            { title: "皮卡丘與這段關係的分析", url: "topics/pokemon-anime/lesson-43.html" }
          ]
        },
        {
          title: "模組 P｜人物②：歷代旅伴",
          courses: [
            { title: "旅伴制度的功能與更替邏輯", url: "topics/pokemon-anime/lesson-44.html" },
            { title: "前期旅伴：小霞、小剛與城都時期", url: "topics/pokemon-anime/lesson-45.html" },
            { title: "中期旅伴：小遙、小光與雙主線結構", url: "topics/pokemon-anime/lesson-46.html" },
            { title: "後期旅伴：合眾、卡洛斯、阿羅拉與新無印", url: "topics/pokemon-anime/lesson-47.html" }
          ]
        },
        {
          title: "模組 Q｜人物③：火箭隊",
          courses: [
            { title: "武藏、小次郎與喵喵的角色設計", url: "topics/pokemon-anime/lesson-48.html" },
            { title: "火箭隊的敘事功能", url: "topics/pokemon-anime/lesson-49.html" },
            { title: "火箭隊的收尾與模組總結", url: "topics/pokemon-anime/lesson-50.html" }
          ]
        },
        {
          title: "模組 R｜人物④：勁敵與各地要角",
          courses: [
            { title: "勁敵制度：從小茂到真司", url: "topics/pokemon-anime/lesson-51.html" },
            { title: "後期勁敵與冠軍層級的對手", url: "topics/pokemon-anime/lesson-52.html" },
            { title: "各地要角：博士、道館與惡役組織", url: "topics/pokemon-anime/lesson-53.html" }
          ]
        },
        {
          title: "模組 S｜設定總表：地方、聯盟與系列對照",
          courses: [
            { title: "地方與系列對照總表", url: "topics/pokemon-anime/lesson-54.html" },
            { title: "小智的歷屆聯盟成績表", url: "topics/pokemon-anime/lesson-55.html" },
            { title: "世界設定名詞總表", url: "topics/pokemon-anime/lesson-56.html" }
          ]
        },
        {
          title: "模組 T｜主題論與課程總結",
          courses: [
            { title: "主題論①：旅行作為敘事母題", url: "topics/pokemon-anime/lesson-57.html" },
            { title: "主題論②：不變的主角", url: "topics/pokemon-anime/lesson-58.html" },
            { title: "主題論③：人與寶可夢的關係倫理", url: "topics/pokemon-anime/lesson-59.html" },
            { title: "課程總結：一部還在走的作品", url: "topics/pokemon-anime/lesson-60.html" }
          ]
        }
      ]
    },
    {
      id: "doraemon",
      category: "anime",
      title: "哆啦A夢全紀錄：世界設定、主線劇情與「最終回」的實情",
      description:
        "完整整理《哆啦A夢》的主線：學年誌連載制度如何決定作品的結構特徵、二十二世紀的機器人社會與四次元口袋的道具體系，再講完哆啦A夢為何被派來、他的誕生與耳朵顏色的來歷、一九七一至七四年三個真實存在的告別回，以及〈大雄的結婚前夜〉的未來線。另闢模組釐清「最終回」問題——作品因作者逝世而無結局，「電池耗盡」版實為二次創作。",
      icon: "🔔",
      url: "topics/doraemon/index.html",
      modules: [
        {
          title: "模組 A｜序幕：連載形態、學年誌制度與「主線」的取法",
          courses: [
            { title: "這部作品到底是什麼", url: "topics/doraemon/lesson-01.html" },
            { title: "學年誌制度如何決定了作品的形狀", url: "topics/doraemon/lesson-02.html" },
            { title: "沒有結局的作品：作者之死與「完結」的定義", url: "topics/doraemon/lesson-03.html" },
            { title: "本課程的主線取法與模組地圖", url: "topics/doraemon/lesson-04.html" }
          ]
        },
        {
          title: "模組 B｜設定①：二十二世紀與時間旅行",
          courses: [
            { title: "二十二世紀的社會樣貌", url: "topics/doraemon/lesson-05.html" },
            { title: "時間旅行的規則與矛盾處理", url: "topics/doraemon/lesson-06.html" },
            { title: "未來社會與現代日本的對照", url: "topics/doraemon/lesson-07.html" }
          ]
        },
        {
          title: "模組 C｜設定②：四次元口袋與道具體系",
          courses: [
            { title: "四次元口袋與道具的取得方式", url: "topics/doraemon/lesson-08.html" },
            { title: "道具的功能分類", url: "topics/doraemon/lesson-09.html" },
            { title: "代表性道具的設計巧思", url: "topics/doraemon/lesson-10.html" },
            { title: "道具的限制與作品的倫理立場", url: "topics/doraemon/lesson-11.html" }
          ]
        },
        {
          title: "模組 D｜五人關係結構",
          courses: [
            { title: "五人組的角色配置", url: "topics/doraemon/lesson-12.html" },
            { title: "依賴與扶持：核心關係的張力", url: "topics/doraemon/lesson-13.html" },
            { title: "封閉的世界與它的邊界", url: "topics/doraemon/lesson-14.html" }
          ]
        },
        {
          title: "模組 E｜劇情①：哆啦A夢為什麼來",
          courses: [
            { title: "第一回：從未來之國千里迢迢而來", url: "topics/doraemon/lesson-15.html" },
            { title: "世修：派遣者的動機", url: "topics/doraemon/lesson-16.html" },
            { title: "原本的未來：大雄的人生預告", url: "topics/doraemon/lesson-17.html" }
          ]
        },
        {
          title: "模組 F｜劇情②：哆啦A夢的誕生",
          courses: [
            { title: "出廠：一台有瑕疵的量產機", url: "topics/doraemon/lesson-18.html" },
            { title: "耳朵與顏色：兩個外觀變化的來歷", url: "topics/doraemon/lesson-19.html" },
            { title: "性格、弱點與哆啦美", url: "topics/doraemon/lesson-20.html" }
          ]
        },
        {
          title: "模組 G｜劇情③：離別的回",
          courses: [
            { title: "第一次告別：哆啦A夢回到未來去", url: "topics/doraemon/lesson-21.html" },
            { title: "第二次告別：一個關於自立的問題", url: "topics/doraemon/lesson-22.html" },
            { title: "〈再見了，哆啦A夢〉", url: "topics/doraemon/lesson-23.html" },
            { title: "〈哆啦A夢回來了〉與模組總結", url: "topics/doraemon/lesson-24.html" }
          ]
        },
        {
          title: "模組 H｜劇情④：未來線與〈大雄的結婚前夜〉",
          courses: [
            { title: "未來線：被改變之後的人生", url: "topics/doraemon/lesson-25.html" },
            { title: "〈大雄的結婚前夜〉", url: "topics/doraemon/lesson-26.html" },
            { title: "靜香的選擇與感情線的處理", url: "topics/doraemon/lesson-27.html" },
            { title: "未來的家庭與模組總結", url: "topics/doraemon/lesson-28.html" }
          ]
        },
        {
          title: "模組 I｜關於「最終回」的實情",
          courses: [
            { title: "為什麼會有這麼多「最終回」", url: "topics/doraemon/lesson-29.html" },
            { title: "最有名的假結局：同人誌事件的來龍去脈", url: "topics/doraemon/lesson-30.html" },
            { title: "其他流傳的說法與它們的問題", url: "topics/doraemon/lesson-31.html" },
            { title: "事實清單與模組總結", url: "topics/doraemon/lesson-32.html" }
          ]
        },
        {
          title: "模組 J｜《大長編》①：體系與結構",
          courses: [
            { title: "《大長編哆啦A夢》是什麼", url: "topics/doraemon/lesson-33.html" },
            { title: "《大長編》的固定結構", url: "topics/doraemon/lesson-34.html" },
            { title: "角色在異境中的變化", url: "topics/doraemon/lesson-35.html" }
          ]
        },
        {
          title: "模組 K｜《大長編》②：代表作解析",
          courses: [
            { title: "起點：《大雄的恐龍》", url: "topics/doraemon/lesson-36.html" },
            { title: "《大雄的宇宙小戰爭》與《大雄與鐵人兵團》", url: "topics/doraemon/lesson-37.html" },
            { title: "《大雄的日本誕生》與《大雄與雲之王國》", url: "topics/doraemon/lesson-38.html" },
            { title: "遺作與《大長編》的收束", url: "topics/doraemon/lesson-39.html" }
          ]
        },
        {
          title: "模組 L｜番外：動畫版本與劇場版體系",
          courses: [
            { title: "三個電視動畫版本", url: "topics/doraemon/lesson-40.html" },
            { title: "兩個主要版本的差異", url: "topics/doraemon/lesson-41.html" },
            { title: "劇場版體系與正史地位", url: "topics/doraemon/lesson-42.html" },
            { title: "版本差異速查與模組總結", url: "topics/doraemon/lesson-43.html" }
          ]
        },
        {
          title: "模組 M｜人物①：大雄與哆啦A夢",
          courses: [
            { title: "大雄：一個被誤解的主角", url: "topics/doraemon/lesson-44.html" },
            { title: "大雄的處境與作品的立場", url: "topics/doraemon/lesson-45.html" },
            { title: "哆啦A夢：照顧者的角色分析", url: "topics/doraemon/lesson-46.html" },
            { title: "兩人關係的總結", url: "topics/doraemon/lesson-47.html" }
          ]
        },
        {
          title: "模組 N｜人物②：靜香、胖虎與小夫",
          courses: [
            { title: "靜香：作品的良心", url: "topics/doraemon/lesson-48.html" },
            { title: "胖虎：暴力與義氣的並存", url: "topics/doraemon/lesson-49.html" },
            { title: "小夫：最貼近讀者的角色", url: "topics/doraemon/lesson-50.html" }
          ]
        },
        {
          title: "模組 O｜人物③：家人與周邊角色",
          courses: [
            { title: "大雄的家人", url: "topics/doraemon/lesson-51.html" },
            { title: "出木杉、老師與班上的其他人", url: "topics/doraemon/lesson-52.html" },
            { title: "未來的角色與其他機器人", url: "topics/doraemon/lesson-53.html" }
          ]
        },
        {
          title: "模組 P｜設定總表",
          courses: [
            { title: "人物速查表", url: "topics/doraemon/lesson-54.html" },
            { title: "設定與道具速查表", url: "topics/doraemon/lesson-55.html" },
            { title: "作品體系與主線回目速查表", url: "topics/doraemon/lesson-56.html" }
          ]
        },
        {
          title: "模組 Q｜主題論",
          courses: [
            { title: "主題論①：不勞而獲的誘惑與代價", url: "topics/doraemon/lesson-57.html" },
            { title: "主題論②：依賴與自己站起來", url: "topics/doraemon/lesson-58.html" },
            { title: "主題論③：不完美的人如何被肯定", url: "topics/doraemon/lesson-59.html" },
            { title: "主題論④：為什麼它能跨越半世紀", url: "topics/doraemon/lesson-60.html" }
          ]
        },
        {
          title: "模組 R｜課程總結",
          courses: [
            { title: "課程總結：整條主線的輪廓", url: "topics/doraemon/lesson-61.html" },
            { title: "延伸建議與取材說明", url: "topics/doraemon/lesson-62.html" }
          ]
        }
      ]
    },
    {
      id: "complex-numbers",
      category: "math",
      title: "複數到底在做什麼：從三次方程式到旋轉、訊號與量子",
      description:
        "專為「會算但想像不出來」的人設計：不從 i² = -1 出發，而是從三次方程式為何非得繞道負數開根號講起；再給出關鍵的那張圖——複數住在平面上，加法是平移、乘法是旋轉加縮放，i² = -1 是「轉兩次九十度」的結果。接著推出棣美弗與尤拉公式，並展示它在交流電、訊號、量子力學與控制系統裡真正的用途。",
      icon: "🌀",
      url: "topics/complex-numbers/index.html",
      modules: [
        {
          title: "模組 A｜序幕：為什麼你想像不出來",
          courses: [
            { title: "問題出在「虛數」這個名字", url: "topics/complex-numbers/lesson-01.html" },
            { title: "你其實已經在用它了", url: "topics/complex-numbers/lesson-02.html" },
            { title: "本課程的策略：從問題出發，不從定義出發", url: "topics/complex-numbers/lesson-03.html" },
            { title: "課程地圖與閱讀路徑", url: "topics/complex-numbers/lesson-04.html" }
          ]
        },
        {
          title: "模組 B｜複數不是憑空發明的",
          courses: [
            { title: "起點的誤會：不是為了解 x² + 1 = 0", url: "topics/complex-numbers/lesson-05.html" },
            { title: "三次方程式與那個繞不過去的路口", url: "topics/complex-numbers/lesson-06.html" },
            { title: "邦貝利的決定：先算下去再說", url: "topics/complex-numbers/lesson-07.html" },
            { title: "從中間值到真正的數", url: "topics/complex-numbers/lesson-08.html" }
          ]
        },
        {
          title: "模組 C｜幾何轉向：複數是平面上的動作",
          courses: [
            { title: "把複數畫在平面上", url: "topics/complex-numbers/lesson-09.html" },
            { title: "加法就是平移", url: "topics/complex-numbers/lesson-10.html" },
            { title: "乘法就是旋轉加縮放", url: "topics/complex-numbers/lesson-11.html" },
            { title: "i 的四次循環與旋轉的證據", url: "topics/complex-numbers/lesson-12.html" }
          ]
        },
        {
          title: "模組 D｜極座標與尤拉公式",
          courses: [
            { title: "模與輻角：複數的另一種寫法", url: "topics/complex-numbers/lesson-13.html" },
            { title: "極座標下的乘法與棣美弗定理", url: "topics/complex-numbers/lesson-14.html" },
            { title: "尤拉公式：e^(iθ) 到底是什麼", url: "topics/complex-numbers/lesson-15.html" },
            { title: "e^(iπ) + 1 = 0 的真正意思", url: "topics/complex-numbers/lesson-16.html" }
          ]
        },
        {
          title: "模組 E｜為什麼「旋轉」這麼重要",
          courses: [
            { title: "波，就是旋轉的影子", url: "topics/complex-numbers/lesson-17.html" },
            { title: "世界上有多少東西在振盪", url: "topics/complex-numbers/lesson-18.html" },
            { title: "為什麼複數是描述振盪的最佳語言", url: "topics/complex-numbers/lesson-19.html" }
          ]
        },
        {
          title: "模組 F｜應用①：交流電與相量",
          courses: [
            { title: "交流電的麻煩：不同步", url: "topics/complex-numbers/lesson-20.html" },
            { title: "相量：把一條波壓成一個複數", url: "topics/complex-numbers/lesson-21.html" },
            { title: "阻抗：把三種元件統一成一個數", url: "topics/complex-numbers/lesson-22.html" },
            { title: "完整例題：RC 電路從頭算到尾", url: "topics/complex-numbers/lesson-23.html" }
          ]
        },
        {
          title: "模組 G｜應用②：訊號、頻率與傅立葉的入口",
          courses: [
            { title: "任何訊號，都是一堆旋轉疊起來的", url: "topics/complex-numbers/lesson-24.html" },
            { title: "為什麼用複數指數而不用 sin 和 cos", url: "topics/complex-numbers/lesson-25.html" },
            { title: "頻域是什麼，以及往下走的路", url: "topics/complex-numbers/lesson-26.html" }
          ]
        },
        {
          title: "模組 H｜應用③：量子力學——複數不可取代之處",
          courses: [
            { title: "在量子力學裡，複數不是選項", url: "topics/complex-numbers/lesson-27.html" },
            { title: "相位：看不見卻決定一切的東西", url: "topics/complex-numbers/lesson-28.html" },
            { title: "這個案例告訴我們什麼", url: "topics/complex-numbers/lesson-29.html" }
          ]
        },
        {
          title: "模組 I｜應用④：控制、電腦繪圖與碎形",
          courses: [
            { title: "控制系統：一個點的位置決定機器會不會失控", url: "topics/complex-numbers/lesson-30.html" },
            { title: "電腦繪圖：旋轉不必用矩陣", url: "topics/complex-numbers/lesson-31.html" },
            { title: "碎形：一條簡單規則造出的無限複雜", url: "topics/complex-numbers/lesson-32.html" }
          ]
        },
        {
          title: "模組 J｜代數的完整性",
          courses: [
            { title: "代數基本定理：所有方程式都有解", url: "topics/complex-numbers/lesson-33.html" },
            { title: "「一定有解」在實務上的價值", url: "topics/complex-numbers/lesson-34.html" },
            { title: "為什麼不繼續擴充下去", url: "topics/complex-numbers/lesson-35.html" }
          ]
        },
        {
          title: "模組 K｜常見誤解與心理障礙",
          courses: [
            { title: "五個常見誤解", url: "topics/complex-numbers/lesson-36.html" },
            { title: "為什麼中學教法讓人想不出來", url: "topics/complex-numbers/lesson-37.html" },
            { title: "複數、向量與矩陣的關係", url: "topics/complex-numbers/lesson-38.html" }
          ]
        },
        {
          title: "模組 L｜動手驗證",
          courses: [
            { title: "動手一：看複數乘法在轉什麼", url: "topics/complex-numbers/lesson-39.html" },
            { title: "動手二：用旋轉疊出一個方波", url: "topics/complex-numbers/lesson-40.html" },
            { title: "動手三：畫出曼德博集合", url: "topics/complex-numbers/lesson-41.html" }
          ]
        },
        {
          title: "模組 M｜速查總表",
          courses: [
            { title: "運算速查：代數與幾何對照", url: "topics/complex-numbers/lesson-42.html" },
            { title: "公式速查：極座標與指數形式", url: "topics/complex-numbers/lesson-43.html" },
            { title: "應用速查：各領域的對照表", url: "topics/complex-numbers/lesson-44.html" }
          ]
        },
        {
          title: "模組 N｜總結",
          courses: [
            { title: "一句話回答：複數到底在做什麼", url: "topics/complex-numbers/lesson-45.html" },
            { title: "延伸路徑與課程總結", url: "topics/complex-numbers/lesson-46.html" }
          ]
        }
      ]
    },
    {
      id: "laplace-transform",
      category: "math",
      title: "拉普拉斯轉換：從傅立葉出發，把微分方程變成看圖",
      description:
        "完整講解拉普拉斯轉換是什麼、為什麼長那樣、實際怎麼用。不從定義式出發，而是先講傅立葉，再指出它處理不了發散訊號、也沒有納入初始條件的機制；只要先乘上 e^(-σt) 再做傅立葉，拉普拉斯轉換就自己長出來了。接著建立微分性質、轉換表與部分分式，走完解微分方程、轉移函數與穩定性、電路與控制入門。前置知識為複數。",
      icon: "📐",
      url: "topics/laplace-transform/index.html",
      modules: [
        {
          title: "模組 A｜序幕：這東西在解決什麼問題",
          courses: [
            { title: "問題起點：微分方程很難解", url: "topics/laplace-transform/lesson-01.html" },
            { title: "轉換法的核心想法", url: "topics/laplace-transform/lesson-02.html" },
            { title: "三個轉換的關係地圖", url: "topics/laplace-transform/lesson-03.html" },
            { title: "課程地圖與前置知識", url: "topics/laplace-transform/lesson-04.html" }
          ]
        },
        {
          title: "模組 B｜前置：複數指數與本徵函數",
          courses: [
            { title: "e^(st) 是什麼：衰減乘上旋轉", url: "topics/laplace-transform/lesson-05.html" },
            { title: "本徵函數：為什麼偏偏是指數", url: "topics/laplace-transform/lesson-06.html" },
            { title: "線性非時變：這套方法成立的前提", url: "topics/laplace-transform/lesson-07.html" }
          ]
        },
        {
          title: "模組 C｜先講傅立葉：把訊號拆成頻率",
          courses: [
            { title: "傅立葉級數：週期訊號的拆解", url: "topics/laplace-transform/lesson-08.html" },
            { title: "正交性：為什麼可以這樣拆", url: "topics/laplace-transform/lesson-09.html" },
            { title: "傅立葉轉換：非週期訊號怎麼辦", url: "topics/laplace-transform/lesson-10.html" },
            { title: "頻域怎麼用", url: "topics/laplace-transform/lesson-11.html" },
            { title: "傅立葉的限制：它處理不了什麼", url: "topics/laplace-transform/lesson-12.html" }
          ]
        },
        {
          title: "模組 D｜從傅立葉到拉普拉斯",
          courses: [
            { title: "補救的想法：先把它壓下來", url: "topics/laplace-transform/lesson-13.html" },
            { title: "公式自己長出來", url: "topics/laplace-transform/lesson-14.html" },
            { title: "收斂區域", url: "topics/laplace-transform/lesson-15.html" },
            { title: "兩個轉換的關係總結", url: "topics/laplace-transform/lesson-16.html" }
          ]
        },
        {
          title: "模組 E｜定義與基本性質",
          courses: [
            { title: "定義式逐項拆解", url: "topics/laplace-transform/lesson-17.html" },
            { title: "微分性質：整套方法的引擎", url: "topics/laplace-transform/lesson-18.html" },
            { title: "線性、積分與尺度", url: "topics/laplace-transform/lesson-19.html" },
            { title: "兩個位移性質", url: "topics/laplace-transform/lesson-20.html" },
            { title: "初值與終值定理", url: "topics/laplace-transform/lesson-21.html" }
          ]
        },
        {
          title: "模組 F｜常用轉換表與怎麼記",
          courses: [
            { title: "基本轉換表", url: "topics/laplace-transform/lesson-22.html" },
            { title: "怎麼從三條推出整張表", url: "topics/laplace-transform/lesson-23.html" },
            { title: "速查表與典型分母的辨識", url: "topics/laplace-transform/lesson-24.html" }
          ]
        },
        {
          title: "模組 G｜反轉換：部分分式法",
          courses: [
            { title: "反轉換為什麼可以查表", url: "topics/laplace-transform/lesson-25.html" },
            { title: "相異實根的拆解", url: "topics/laplace-transform/lesson-26.html" },
            { title: "重根與複數根", url: "topics/laplace-transform/lesson-27.html" },
            { title: "完整流程與錯誤清單", url: "topics/laplace-transform/lesson-28.html" }
          ]
        },
        {
          title: "模組 H｜怎麼用①：解常微分方程",
          courses: [
            { title: "標準流程五步驟", url: "topics/laplace-transform/lesson-29.html" },
            { title: "例題一：RC 電路的充電", url: "topics/laplace-transform/lesson-30.html" },
            { title: "例題二：二階系統與三種阻尼", url: "topics/laplace-transform/lesson-31.html" },
            { title: "帶輸入的情況與零狀態分離", url: "topics/laplace-transform/lesson-32.html" }
          ]
        },
        {
          title: "模組 I｜怎麼用②：轉移函數與系統行為",
          courses: [
            { title: "轉移函數 H(s)", url: "topics/laplace-transform/lesson-33.html" },
            { title: "極點與零點", url: "topics/laplace-transform/lesson-34.html" },
            { title: "穩定性判準", url: "topics/laplace-transform/lesson-35.html" },
            { title: "由極點圖讀出系統行為", url: "topics/laplace-transform/lesson-36.html" }
          ]
        },
        {
          title: "模組 J｜怎麼用③：迴旋積分與系統響應",
          courses: [
            { title: "迴旋積分與卷積定理", url: "topics/laplace-transform/lesson-37.html" },
            { title: "脈衝響應與階躍響應", url: "topics/laplace-transform/lesson-38.html" },
            { title: "為什麼工程師都在 s 域工作", url: "topics/laplace-transform/lesson-39.html" }
          ]
        },
        {
          title: "模組 K｜怎麼用④：電路分析實戰",
          courses: [
            { title: "元件的 s 域模型", url: "topics/laplace-transform/lesson-40.html" },
            { title: "完整例題：RLC 串聯電路", url: "topics/laplace-transform/lesson-41.html" },
            { title: "帶初始儲能的電路與模組總結", url: "topics/laplace-transform/lesson-42.html" }
          ]
        },
        {
          title: "模組 L｜控制系統入門",
          courses: [
            { title: "開迴路與閉迴路", url: "topics/laplace-transform/lesson-43.html" },
            { title: "PID 控制器", url: "topics/laplace-transform/lesson-44.html" },
            { title: "根軌跡與波德圖的概念", url: "topics/laplace-transform/lesson-45.html" }
          ]
        },
        {
          title: "模組 M｜三個轉換的完整對照",
          courses: [
            { title: "傅立葉 vs 拉普拉斯：何時用哪個", url: "topics/laplace-transform/lesson-46.html" },
            { title: "Z 轉換：離散版的拉普拉斯", url: "topics/laplace-transform/lesson-47.html" },
            { title: "三個轉換總對照表", url: "topics/laplace-transform/lesson-48.html" }
          ]
        },
        {
          title: "模組 N｜常見混淆與陷阱",
          courses: [
            { title: "s 到底是什麼（它不是頻率）", url: "topics/laplace-transform/lesson-49.html" },
            { title: "計算上的十個陷阱", url: "topics/laplace-transform/lesson-50.html" },
            { title: "什麼時候拉普拉斯不能用", url: "topics/laplace-transform/lesson-51.html" }
          ]
        },
        {
          title: "模組 O｜速查總表",
          courses: [
            { title: "轉換對照速查表", url: "topics/laplace-transform/lesson-52.html" },
            { title: "解題流程圖", url: "topics/laplace-transform/lesson-53.html" }
          ]
        },
        {
          title: "模組 P｜總結",
          courses: [
            { title: "整門課的一條線", url: "topics/laplace-transform/lesson-54.html" },
            { title: "延伸路徑與課程總結", url: "topics/laplace-transform/lesson-55.html" }
          ]
        }
      ]
    },
    {
      id: "cryptography",
      category: "math",
      title: "密碼學全解析：從恩尼格瑪的齒輪到後量子時代",
      description:
        "完整講解密碼學的原理與歷史，以恩尼格瑪為核心案例：六個部件與完整訊號路徑、親手算出約 1.59×10^20 的金鑰空間，以及反射器造成的兩個結構缺陷如何讓它被波蘭與布萊切利園破解。後半進入現代——完美保密、AES、數論工具、迪菲—赫爾曼、RSA 完整推導、橢圓曲線、簽章與後量子標準。主線是：密碼系統的失敗幾乎從不發生在數學上。",
      icon: "🔐",
      url: "topics/cryptography/index.html",
      modules: [
        {
          title: "模組 A｜序幕：密碼學到底在解決什麼",
          courses: [
            { title: "三個目標：保密、驗證、完整", url: "topics/cryptography/lesson-01.html" },
            { title: "柯克霍夫原則：安全只能靠金鑰", url: "topics/cryptography/lesson-02.html" },
            { title: "為什麼自己發明的加密法一定會被破", url: "topics/cryptography/lesson-03.html" },
            { title: "課程地圖與閱讀路徑", url: "topics/cryptography/lesson-04.html" }
          ]
        },
        {
          title: "模組 B｜古典密碼與它們怎麼被破",
          courses: [
            { title: "替換式密碼", url: "topics/cryptography/lesson-05.html" },
            { title: "頻率分析：九世紀就有的破法", url: "topics/cryptography/lesson-06.html" },
            { title: "維吉尼爾多表密碼", url: "topics/cryptography/lesson-07.html" },
            { title: "古典密碼的共同弱點", url: "topics/cryptography/lesson-08.html" }
          ]
        },
        {
          title: "模組 C｜恩尼格瑪①：機器的構造",
          courses: [
            { title: "為什麼會有這台機器", url: "topics/cryptography/lesson-09.html" },
            { title: "六個部件", url: "topics/cryptography/lesson-10.html" },
            { title: "電流走一遍：完整的訊號路徑", url: "topics/cryptography/lesson-11.html" },
            { title: "轉子怎麼進位：凹口與雙重步進", url: "topics/cryptography/lesson-12.html" },
            { title: "三種設定：轉子順序、環設定、起始位置", url: "topics/cryptography/lesson-13.html" }
          ]
        },
        {
          title: "模組 D｜恩尼格瑪②：金鑰空間與致命缺陷",
          courses: [
            { title: "親手算一次金鑰空間", url: "topics/cryptography/lesson-14.html" },
            { title: "致命缺陷：字母不會變成自己", url: "topics/cryptography/lesson-15.html" },
            { title: "互反性：加密與解密是同一個動作", url: "topics/cryptography/lesson-16.html" },
            { title: "操作流程與那個致命的習慣", url: "topics/cryptography/lesson-17.html" }
          ]
        },
        {
          title: "模組 E｜恩尼格瑪③：怎麼被破的",
          courses: [
            { title: "波蘭人先破的：雷耶夫斯基的洞見", url: "topics/cryptography/lesson-18.html" },
            { title: "循環儀、炸彈機與穿孔紙", url: "topics/cryptography/lesson-19.html" },
            { title: "一九三九年七月：華沙的交接", url: "topics/cryptography/lesson-20.html" },
            { title: "圖靈的炸彈機：用矛盾排除", url: "topics/cryptography/lesson-21.html" },
            { title: "對角板、海軍與人為疏失", url: "topics/cryptography/lesson-22.html" }
          ]
        },
        {
          title: "模組 F｜恩尼格瑪④：留下的教訓",
          courses: [
            { title: "破的不是演算法，是使用方式", url: "topics/cryptography/lesson-23.html" },
            { title: "現代密碼學學到的四件事", url: "topics/cryptography/lesson-24.html" },
            { title: "常見迷思與影視誤解", url: "topics/cryptography/lesson-25.html" }
          ]
        },
        {
          title: "模組 G｜現代密碼學的起點",
          courses: [
            { title: "夏農與完美保密", url: "topics/cryptography/lesson-26.html" },
            { title: "一次性密碼本", url: "topics/cryptography/lesson-27.html" },
            { title: "維諾那計畫：重複使用的代價", url: "topics/cryptography/lesson-28.html" }
          ]
        },
        {
          title: "模組 H｜對稱式加密",
          courses: [
            { title: "區塊加密的基本結構", url: "topics/cryptography/lesson-29.html" },
            { title: "DES 與它的終結", url: "topics/cryptography/lesson-30.html" },
            { title: "AES：公開競賽選出的標準", url: "topics/cryptography/lesson-31.html" },
            { title: "加密模式：為什麼企鵝還看得見", url: "topics/cryptography/lesson-32.html" }
          ]
        },
        {
          title: "模組 I｜數論工具箱",
          courses: [
            { title: "模運算：時鐘上的算術", url: "topics/cryptography/lesson-33.html" },
            { title: "輾轉相除法與模反元素", url: "topics/cryptography/lesson-34.html" },
            { title: "費馬小定理與尤拉定理", url: "topics/cryptography/lesson-35.html" },
            { title: "快速冪：怎麼算 m 的兩千位次方", url: "topics/cryptography/lesson-36.html" },
            { title: "質數與因數分解的不對稱", url: "topics/cryptography/lesson-37.html" }
          ]
        },
        {
          title: "模組 J｜公鑰革命",
          courses: [
            { title: "金鑰分發：對稱式加密解決不了的事", url: "topics/cryptography/lesson-38.html" },
            { title: "迪菲—赫爾曼金鑰交換", url: "topics/cryptography/lesson-39.html" },
            { title: "離散對數問題", url: "topics/cryptography/lesson-40.html" },
            { title: "誰先想到的", url: "topics/cryptography/lesson-41.html" }
          ]
        },
        {
          title: "模組 K｜RSA 完整解析",
          courses: [
            { title: "產生金鑰的五個步驟", url: "topics/cryptography/lesson-42.html" },
            { title: "為什麼解得回來", url: "topics/cryptography/lesson-43.html" },
            { title: "小數字完整實例", url: "topics/cryptography/lesson-44.html" },
            { title: "實務細節：課本版的 RSA 不安全", url: "topics/cryptography/lesson-45.html" }
          ]
        },
        {
          title: "模組 L｜橢圓曲線",
          courses: [
            { title: "曲線上的那個奇怪加法", url: "topics/cryptography/lesson-46.html" },
            { title: "為什麼 256 位元抵得上 3072 位元", url: "topics/cryptography/lesson-47.html" },
            { title: "現在用在哪裡", url: "topics/cryptography/lesson-48.html" }
          ]
        },
        {
          title: "模組 M｜雜湊函數",
          courses: [
            { title: "雜湊在做什麼", url: "topics/cryptography/lesson-49.html" },
            { title: "MD5 與 SHA-1 的破解史", url: "topics/cryptography/lesson-50.html" },
            { title: "密碼儲存：加鹽與慢雜湊", url: "topics/cryptography/lesson-51.html" },
            { title: "雜湊的其他應用", url: "topics/cryptography/lesson-52.html" }
          ]
        },
        {
          title: "模組 N｜數位簽章與信任鏈",
          courses: [
            { title: "簽章：反過來用的公鑰", url: "topics/cryptography/lesson-53.html" },
            { title: "憑證與信任鏈", url: "topics/cryptography/lesson-54.html" },
            { title: "一次加密連線裡發生了什麼", url: "topics/cryptography/lesson-55.html" }
          ]
        },
        {
          title: "模組 O｜隨機性",
          courses: [
            { title: "為什麼亂數是整個密碼學的地基", url: "topics/cryptography/lesson-56.html" },
            { title: "亂數怎麼來的", url: "topics/cryptography/lesson-57.html" },
            { title: "亂數造成的真實災難", url: "topics/cryptography/lesson-58.html" }
          ]
        },
        {
          title: "模組 P｜後量子密碼",
          courses: [
            { title: "秀爾演算法：為什麼公開金鑰全部有危險", url: "topics/cryptography/lesson-59.html" },
            { title: "對稱式與雜湊的處境", url: "topics/cryptography/lesson-60.html" },
            { title: "後量子標準與先收割後解密", url: "topics/cryptography/lesson-61.html" }
          ]
        },
        {
          title: "模組 Q｜常見誤解與實務原則",
          courses: [
            { title: "十個常見誤解", url: "topics/cryptography/lesson-62.html" },
            { title: "不要自己實作密碼學", url: "topics/cryptography/lesson-63.html" },
            { title: "真實失敗案例的共同模式", url: "topics/cryptography/lesson-64.html" }
          ]
        },
        {
          title: "模組 R｜速查總表",
          courses: [
            { title: "演算法對照表", url: "topics/cryptography/lesson-65.html" },
            { title: "恩尼格瑪速查", url: "topics/cryptography/lesson-66.html" },
            { title: "名詞與流程速查", url: "topics/cryptography/lesson-67.html" }
          ]
        },
        {
          title: "模組 S｜總結",
          courses: [
            { title: "四千年的一條線", url: "topics/cryptography/lesson-68.html" },
            { title: "延伸路徑與課程總結", url: "topics/cryptography/lesson-69.html" }
          ]
        }
      ]
    },
    {
      id: "quantum-computing",
      category: "tech",
      title: "量子電腦：原理、演算法與應用的誠實評估",
      description:
        "完整講解量子電腦的原理與應用，並提供判讀相關宣稱的方法。先破除「同時嘗試所有答案」等三個常見誤解，再建立疊加、機率幅、測量與糾纏的正確圖像；接著拆解秀爾與格羅弗演算法、量子模擬，比較超導、離子阱、光子、中性原子與拓樸五條硬體路線與錯誤更正，最後談後量子密碼與判讀新聞的七個問題。前置知識為複數。",
      icon: "⚛️",
      url: "topics/quantum-computing/index.html",
      modules: [
        {
          title: "模組 A｜序幕：它是什麼，更重要的是不是什麼",
          courses: [
            { title: "三個必須先破除的誤解", url: "topics/quantum-computing/lesson-01.html" },
            { title: "優勢從哪裡來，以及為什麼那麼窄", url: "topics/quantum-computing/lesson-02.html" },
            { title: "現在到哪了", url: "topics/quantum-computing/lesson-03.html" },
            { title: "課程地圖與前置知識", url: "topics/quantum-computing/lesson-04.html" }
          ]
        },
        {
          title: "模組 B｜前置：你需要的量子力學",
          courses: [
            { title: "疊加：不是「同時在兩個地方」", url: "topics/quantum-computing/lesson-05.html" },
            { title: "機率幅與干涉：全部的關鍵", url: "topics/quantum-computing/lesson-06.html" },
            { title: "測量：為什麼只能讀一次", url: "topics/quantum-computing/lesson-07.html" },
            { title: "糾纏：不是超距傳訊", url: "topics/quantum-computing/lesson-08.html" }
          ]
        },
        {
          title: "模組 C｜量子位元",
          courses: [
            { title: "位元與量子位元", url: "topics/quantum-computing/lesson-09.html" },
            { title: "布洛赫球：把量子位元畫出來", url: "topics/quantum-computing/lesson-10.html" },
            { title: "多量子位元：那個指數", url: "topics/quantum-computing/lesson-11.html" },
            { title: "指數成長常被誤用的地方", url: "topics/quantum-computing/lesson-12.html" }
          ]
        },
        {
          title: "模組 D｜量子閘與電路",
          courses: [
            { title: "單量子位元閘", url: "topics/quantum-computing/lesson-13.html" },
            { title: "兩量子位元閘與糾纏的製造", url: "topics/quantum-computing/lesson-14.html" },
            { title: "量子電路圖怎麼讀", url: "topics/quantum-computing/lesson-15.html" }
          ]
        },
        {
          title: "模組 E｜演算法①：干涉是唯一的武器",
          courses: [
            { title: "最小的量子加速", url: "topics/quantum-computing/lesson-16.html" },
            { title: "相位反衝：核心技巧", url: "topics/quantum-computing/lesson-17.html" },
            { title: "所有量子演算法的共同骨架", url: "topics/quantum-computing/lesson-18.html" }
          ]
        },
        {
          title: "模組 F｜演算法②：秀爾",
          courses: [
            { title: "因數分解怎麼變成找週期", url: "topics/quantum-computing/lesson-19.html" },
            { title: "量子傅立葉轉換在做什麼", url: "topics/quantum-computing/lesson-20.html" },
            { title: "秀爾演算法完整流程", url: "topics/quantum-computing/lesson-21.html" },
            { title: "破 RSA 需要多大的量子電腦", url: "topics/quantum-computing/lesson-22.html" }
          ]
        },
        {
          title: "模組 G｜演算法③：格羅弗",
          courses: [
            { title: "振幅放大的幾何圖像", url: "topics/quantum-computing/lesson-23.html" },
            { title: "為什麼只有平方根，以及它夠不夠用", url: "topics/quantum-computing/lesson-24.html" }
          ]
        },
        {
          title: "模組 H｜演算法④：量子模擬與其他",
          courses: [
            { title: "費曼的原始動機", url: "topics/quantum-computing/lesson-25.html" },
            { title: "化學與材料：現實的進展", url: "topics/quantum-computing/lesson-26.html" },
            { title: "最佳化與量子退火", url: "topics/quantum-computing/lesson-27.html" },
            { title: "量子機器學習的現實評估", url: "topics/quantum-computing/lesson-28.html" }
          ]
        },
        {
          title: "模組 I｜硬體①：五條技術路線",
          courses: [
            { title: "超導電路：目前的主流", url: "topics/quantum-computing/lesson-29.html" },
            { title: "離子阱與其他路線", url: "topics/quantum-computing/lesson-30.html" }
          ]
        },
        {
          title: "模組 J｜硬體②：退相干與錯誤更正",
          courses: [
            { title: "退相干：最根本的敵人", url: "topics/quantum-computing/lesson-31.html" },
            { title: "量子錯誤更正為什麼那麼難", url: "topics/quantum-computing/lesson-32.html" },
            { title: "距離容錯還有多遠", url: "topics/quantum-computing/lesson-33.html" }
          ]
        },
        {
          title: "模組 K｜現況、優越性爭議與時程",
          courses: [
            { title: "「量子優越性」到底宣稱了什麼", url: "topics/quantum-computing/lesson-34.html" },
            { title: "怎麼判讀一則量子電腦新聞", url: "topics/quantum-computing/lesson-35.html" },
            { title: "為什麼要現在就關心", url: "topics/quantum-computing/lesson-36.html" }
          ]
        },
        {
          title: "模組 L｜應用：對密碼學的衝擊",
          courses: [
            { title: "哪些密碼會倒，哪些不會", url: "topics/quantum-computing/lesson-37.html" },
            { title: "量子金鑰分發：它是什麼，不是什麼", url: "topics/quantum-computing/lesson-38.html" }
          ]
        },
        {
          title: "模組 M｜量子資訊的其他成果",
          courses: [
            { title: "不可複製定理", url: "topics/quantum-computing/lesson-39.html" },
            { title: "量子隱形傳態：不是瞬間移動", url: "topics/quantum-computing/lesson-40.html" },
            { title: "貝爾不等式與 2022 年諾貝爾物理獎", url: "topics/quantum-computing/lesson-41.html" }
          ]
        },
        {
          title: "模組 N｜速查總表",
          courses: [
            { title: "概念與名詞速查", url: "topics/quantum-computing/lesson-42.html" },
            { title: "判讀與決策速查", url: "topics/quantum-computing/lesson-43.html" }
          ]
        },
        {
          title: "模組 O｜總結",
          courses: [
            { title: "整門課的一條線", url: "topics/quantum-computing/lesson-44.html" },
            { title: "延伸路徑與課程總結", url: "topics/quantum-computing/lesson-45.html" }
          ]
        }
      ]
    },
    {
      id: "nobel-physics",
      category: "nobel",
      title: "諾貝爾物理獎：一百二十五年的完整地圖",
      description:
        "從一九〇一年到最新年度的諾貝爾物理獎完整整理，設計成每年十月可自行擴充。先講清楚規則——最多三人、不追授、不頒給機構——因為大部分爭議與遺珠都是規則直接造成的。一九〇一至二〇〇五年以四張大表加分析呈現，二〇〇六年後每年獨立一課。最後分析時間差的規律、遺珠的三種成因與物理學重心的六個時期。",
      icon: "🏅",
      url: "topics/nobel-physics/index.html",
      modules: [
        {
          title: "模組 A｜序幕：獎項制度與課程結構",
          courses: [
            { title: "諾貝爾獎的規則", url: "topics/nobel-physics/lesson-01.html" },
            { title: "物理獎的領域分布與趨勢", url: "topics/nobel-physics/lesson-02.html" },
            { title: "課程結構與怎麼新增新年度", url: "topics/nobel-physics/lesson-03.html" }
          ]
        },
        {
          title: "模組 B｜大表：一九〇一至一九二五",
          courses: [
            { title: "一九〇一至一九二五年物理獎總表", url: "topics/nobel-physics/lesson-04.html" },
            { title: "第一個二十五年的形勢：實驗壓倒理論", url: "topics/nobel-physics/lesson-05.html" }
          ]
        },
        {
          title: "模組 C｜大表：一九二六至一九五〇",
          courses: [
            { title: "一九二六至一九五〇年物理獎總表", url: "topics/nobel-physics/lesson-06.html" },
            { title: "黃金年代的兩條主線", url: "topics/nobel-physics/lesson-07.html" }
          ]
        },
        {
          title: "模組 D｜大表：一九五一至一九七五",
          courses: [
            { title: "一九五一至一九七五年物理獎總表", url: "topics/nobel-physics/lesson-08.html" },
            { title: "分裂的物理學：粒子與凝態", url: "topics/nobel-physics/lesson-09.html" }
          ]
        },
        {
          title: "模組 E｜大表：一九七六至二〇〇五",
          courses: [
            { title: "一九七六至二〇〇五年物理獎總表", url: "topics/nobel-physics/lesson-10.html" },
            { title: "三十年的三個趨勢與大表的收尾", url: "topics/nobel-physics/lesson-11.html" }
          ]
        },
        {
          title: "模組 F｜逐年精讀：二〇〇六至二〇一〇",
          courses: [
            { title: "二〇〇六年：宇宙微波背景的精密量測", url: "topics/nobel-physics/lesson-12.html" },
            { title: "二〇〇七年：巨磁阻與硬碟革命", url: "topics/nobel-physics/lesson-13.html" },
            { title: "二〇〇八年：對稱性破缺", url: "topics/nobel-physics/lesson-14.html" },
            { title: "二〇〇九年：光纖與影像感測器", url: "topics/nobel-physics/lesson-15.html" },
            { title: "二〇一〇年：石墨烯", url: "topics/nobel-physics/lesson-16.html" }
          ]
        },
        {
          title: "模組 G｜逐年精讀：二〇一一至二〇一五",
          courses: [
            { title: "二〇一一年：宇宙正在加速膨脹", url: "topics/nobel-physics/lesson-17.html" },
            { title: "二〇一二年：操控單一量子系統", url: "topics/nobel-physics/lesson-18.html" },
            { title: "二〇一三年：希格斯機制", url: "topics/nobel-physics/lesson-19.html" },
            { title: "二〇一四年：藍光發光二極體", url: "topics/nobel-physics/lesson-20.html" },
            { title: "二〇一五年：微中子有質量", url: "topics/nobel-physics/lesson-21.html" }
          ]
        },
        {
          title: "模組 H｜逐年精讀：二〇一六至二〇二〇",
          courses: [
            { title: "二〇一六年：物質的拓撲相", url: "topics/nobel-physics/lesson-22.html" },
            { title: "二〇一七年：重力波", url: "topics/nobel-physics/lesson-23.html" },
            { title: "二〇一八年：光鑷與超短脈衝雷射", url: "topics/nobel-physics/lesson-24.html" },
            { title: "二〇一九年：宇宙學理論與系外行星", url: "topics/nobel-physics/lesson-25.html" },
            { title: "二〇二〇年：黑洞", url: "topics/nobel-physics/lesson-26.html" }
          ]
        },
        {
          title: "模組 I｜逐年精讀：二〇二一至二〇二五",
          courses: [
            { title: "二〇二一年：複雜系統與氣候模型", url: "topics/nobel-physics/lesson-27.html" },
            { title: "二〇二二年：糾纏與貝爾不等式", url: "topics/nobel-physics/lesson-28.html" },
            { title: "二〇二三年：阿秒脈衝", url: "topics/nobel-physics/lesson-29.html" },
            { title: "二〇二四年：人工神經網路的物理基礎", url: "topics/nobel-physics/lesson-30.html" },
            { title: "二〇二五年：電路中的巨觀量子行為", url: "topics/nobel-physics/lesson-31.html" }
          ]
        },
        {
          title: "模組 J｜橫向主題分析",
          courses: [
            { title: "時間差：從發現到獲獎要等多久", url: "topics/nobel-physics/lesson-32.html" },
            { title: "遺珠、規則與代表性", url: "topics/nobel-physics/lesson-33.html" },
            { title: "重心遷移：物理學的關注點怎麼變的", url: "topics/nobel-physics/lesson-34.html" }
          ]
        },
        {
          title: "模組 K｜總結與持續追蹤",
          courses: [
            { title: "每年十月：怎麼追蹤與判讀", url: "topics/nobel-physics/lesson-35.html" },
            { title: "總結：一百二十五年的物理學", url: "topics/nobel-physics/lesson-36.html" }
          ]
        }
      ]
    },
    {
      id: "nobel-chemistry",
      category: "nobel",
      title: "諾貝爾化學獎：一百二十五年的完整地圖",
      description:
        "從一九〇一年到最新年度的諾貝爾化學獎完整整理，設計成每年十月可自行擴充。以「做出新東西、看見舊東西、看懂機制」分類，一九〇一至二〇〇五年以四張大表加分析呈現，二〇〇六年後每年獨立一課、固定六段格式。最後橫向分析獲獎時間差、化學獎為何越來越常頒給生物學家，以及遺珠與女性得主的實際數字。",
      icon: "🧪",
      url: "topics/nobel-chemistry/index.html",
      modules: [
        {
          title: "模組 A｜序幕：化學獎的性格與課程結構",
          courses: [
            { title: "化學獎的規則與它獨有的難題", url: "topics/nobel-chemistry/lesson-01.html" },
            { title: "化學獎的領域分布與趨勢", url: "topics/nobel-chemistry/lesson-02.html" },
            { title: "課程結構與怎麼新增新年度", url: "topics/nobel-chemistry/lesson-03.html" }
          ]
        },
        {
          title: "模組 B｜大表：一九〇一至一九二五",
          courses: [
            { title: "一九〇一至一九二五年化學獎總表", url: "topics/nobel-chemistry/lesson-04.html" },
            { title: "哈伯與化學的雙面性", url: "topics/nobel-chemistry/lesson-05.html" }
          ]
        },
        {
          title: "模組 C｜大表：一九二六至一九五〇",
          courses: [
            { title: "一九二六至一九五〇年化學獎總表", url: "topics/nobel-chemistry/lesson-06.html" },
            { title: "大分子觀念的建立", url: "topics/nobel-chemistry/lesson-07.html" }
          ]
        },
        {
          title: "模組 D｜大表：一九五一至一九七五",
          courses: [
            { title: "一九五一至一九七五年化學獎總表", url: "topics/nobel-chemistry/lesson-08.html" },
            { title: "從描述到預測：化學變成一門理論科學", url: "topics/nobel-chemistry/lesson-09.html" }
          ]
        },
        {
          title: "模組 E｜大表：一九七六至二〇〇五",
          courses: [
            { title: "一九七六至二〇〇五年化學獎總表", url: "topics/nobel-chemistry/lesson-10.html" },
            { title: "三十年的三個趨勢與大表的收尾", url: "topics/nobel-chemistry/lesson-11.html" }
          ]
        },
        {
          title: "模組 F｜逐年精讀：二〇〇六至二〇一〇",
          courses: [
            { title: "二〇〇六年：真核轉錄的分子機制", url: "topics/nobel-chemistry/lesson-12.html" },
            { title: "二〇〇七年：固體表面的化學", url: "topics/nobel-chemistry/lesson-13.html" },
            { title: "二〇〇八年：綠色螢光蛋白", url: "topics/nobel-chemistry/lesson-14.html" },
            { title: "二〇〇九年：核糖體的結構", url: "topics/nobel-chemistry/lesson-15.html" },
            { title: "二〇一〇年：鈀催化交叉偶聯", url: "topics/nobel-chemistry/lesson-16.html" }
          ]
        },
        {
          title: "模組 G｜逐年精讀：二〇一一至二〇一五",
          courses: [
            { title: "二〇一一年：準晶", url: "topics/nobel-chemistry/lesson-17.html" },
            { title: "二〇一二年：G 蛋白偶聯受體", url: "topics/nobel-chemistry/lesson-18.html" },
            { title: "二〇一三年：複雜化學系統的多尺度模型", url: "topics/nobel-chemistry/lesson-19.html" },
            { title: "二〇一四年：超解析螢光顯微術", url: "topics/nobel-chemistry/lesson-20.html" },
            { title: "二〇一五年：DNA 修復機制", url: "topics/nobel-chemistry/lesson-21.html" }
          ]
        },
        {
          title: "模組 H｜逐年精讀：二〇一六至二〇二〇",
          courses: [
            { title: "二〇一六年：分子機器", url: "topics/nobel-chemistry/lesson-22.html" },
            { title: "二〇一七年：低溫電子顯微術", url: "topics/nobel-chemistry/lesson-23.html" },
            { title: "二〇一八年：定向演化與噬菌體展示", url: "topics/nobel-chemistry/lesson-24.html" },
            { title: "二〇一九年：鋰離子電池", url: "topics/nobel-chemistry/lesson-25.html" },
            { title: "二〇二〇年：基因編輯剪刀", url: "topics/nobel-chemistry/lesson-26.html" }
          ]
        },
        {
          title: "模組 I｜逐年精讀：二〇二一至二〇二五",
          courses: [
            { title: "二〇二一年：不對稱有機催化", url: "topics/nobel-chemistry/lesson-27.html" },
            { title: "二〇二二年：點擊化學與生物正交化學", url: "topics/nobel-chemistry/lesson-28.html" },
            { title: "二〇二三年：量子點", url: "topics/nobel-chemistry/lesson-29.html" },
            { title: "二〇二四年：蛋白質設計與結構預測", url: "topics/nobel-chemistry/lesson-30.html" },
            { title: "二〇二五年：金屬有機骨架", url: "topics/nobel-chemistry/lesson-31.html" }
          ]
        },
        {
          title: "模組 J｜橫向主題分析",
          courses: [
            { title: "化學獎的三種類型與時間差", url: "topics/nobel-chemistry/lesson-32.html" },
            { title: "邊界、遺珠與代表性", url: "topics/nobel-chemistry/lesson-33.html" }
          ]
        },
        {
          title: "模組 K｜總結與持續追蹤",
          courses: [
            { title: "每年十月：怎麼追蹤與擴充", url: "topics/nobel-chemistry/lesson-34.html" },
            { title: "總結：一百二十五年的化學", url: "topics/nobel-chemistry/lesson-35.html" }
          ]
        }
      ]
    },
    {
      id: "statistics-doe",
      category: "math",
      title: "統計學、假設檢定與實驗設計：完整推導",
      description:
        "從機率公理一路推導到實驗設計，每一個公式都推出來而不是背下來。五個部分依序走過機率與動差生成函數、卡方 t F 三大抽樣分布、假設檢定（含奈曼—皮爾森引理、p 值誤用與複製危機）、線性模型與變異數分析，以及費雪三原則、因子與分數因子設計、反應曲面法，最後以一個把不良率從 8% 降到 0.6% 的案例收尾。前置知識為微積分與線性代數。",
      icon: "📊",
      url: "topics/statistics-doe/index.html",
      modules: [
        {
          title: "模組 A｜序幕：為什麼需要統計學",
          courses: [
            { title: "變異是常態，不是雜訊", url: "topics/statistics-doe/lesson-01.html" },
            { title: "母體、樣本、參數、統計量", url: "topics/statistics-doe/lesson-02.html" },
            { title: "課程地圖：從抽樣分布到實驗設計", url: "topics/statistics-doe/lesson-03.html" }
          ]
        },
        {
          title: "模組 B｜機率的骨架",
          courses: [
            { title: "三條公理與機率的基本性質", url: "topics/statistics-doe/lesson-04.html" },
            { title: "條件機率、貝氏定理與偽陽性悖論", url: "topics/statistics-doe/lesson-05.html" },
            { title: "獨立性與辛普森悖論", url: "topics/statistics-doe/lesson-06.html" },
            { title: "計數：排列、組合與超幾何", url: "topics/statistics-doe/lesson-07.html" }
          ]
        },
        {
          title: "模組 C｜隨機變數、期望值與動差生成函數",
          courses: [
            { title: "隨機變數、分布函數與變數變換", url: "topics/statistics-doe/lesson-08.html" },
            { title: "期望值與它的線性性質", url: "topics/statistics-doe/lesson-09.html" },
            { title: "變異數：定義、性質與加法公式", url: "topics/statistics-doe/lesson-10.html" },
            { title: "相關係數與柯西—施瓦茲不等式", url: "topics/statistics-doe/lesson-11.html" },
            { title: "動差生成函數：整門課的主力工具", url: "topics/statistics-doe/lesson-12.html" }
          ]
        },
        {
          title: "模組 D｜重要分布及其推導",
          courses: [
            { title: "離散分布家族：從白努利到負二項", url: "topics/statistics-doe/lesson-13.html" },
            { title: "卜瓦松分布：二項的極限", url: "topics/statistics-doe/lesson-14.html" },
            { title: "常態分布與高斯積分", url: "topics/statistics-doe/lesson-15.html" },
            { title: "指數與 Gamma 分布", url: "topics/statistics-doe/lesson-16.html" },
            { title: "中央極限定理及其限制", url: "topics/statistics-doe/lesson-17.html" }
          ]
        },
        {
          title: "模組 E｜抽樣分布：三大分布的完整推導",
          courses: [
            { title: "抽樣分布：統計量自己的分布", url: "topics/statistics-doe/lesson-18.html" },
            { title: "卡方分布的推導", url: "topics/statistics-doe/lesson-19.html" },
            { title: "為什麼除以 n−1：不偏性與 Helmert 變換", url: "topics/statistics-doe/lesson-20.html" },
            { title: "t 分布的密度推導", url: "topics/statistics-doe/lesson-21.html" },
            { title: "F 分布的密度推導", url: "topics/statistics-doe/lesson-22.html" }
          ]
        },
        {
          title: "模組 F｜估計理論",
          courses: [
            { title: "點估計、不偏性與均方誤差分解", url: "topics/statistics-doe/lesson-23.html" },
            { title: "動差法與最大概似估計", url: "topics/statistics-doe/lesson-24.html" },
            { title: "分數函數與 Fisher 資訊量", url: "topics/statistics-doe/lesson-25.html" },
            { title: "Cramér–Rao 下界", url: "topics/statistics-doe/lesson-26.html" },
            { title: "信賴區間與樞紐量", url: "topics/statistics-doe/lesson-27.html" }
          ]
        },
        {
          title: "模組 G｜假設檢定的邏輯與結構",
          courses: [
            { title: "檢定的邏輯：為什麼只能拒絕", url: "topics/statistics-doe/lesson-28.html" },
            { title: "兩種錯誤、顯著水準與檢定力", url: "topics/statistics-doe/lesson-29.html" },
            { title: "p 值的精確定義", url: "topics/statistics-doe/lesson-30.html" },
            { title: "檢定力函數與樣本數規劃", url: "topics/statistics-doe/lesson-31.html" }
          ]
        },
        {
          title: "模組 H｜奈曼—皮爾森與似然比",
          courses: [
            { title: "奈曼—皮爾森引理", url: "topics/statistics-doe/lesson-32.html" },
            { title: "一致最強檢定與單調概似比", url: "topics/statistics-doe/lesson-33.html" },
            { title: "廣義似然比檢定與 Wilks 定理", url: "topics/statistics-doe/lesson-34.html" },
            { title: "證明 t 檢定就是似然比檢定", url: "topics/statistics-doe/lesson-35.html" }
          ]
        },
        {
          title: "模組 I｜常見檢定的逐一推導",
          courses: [
            { title: "單樣本 z 檢定與 t 檢定", url: "topics/statistics-doe/lesson-36.html" },
            { title: "兩樣本 t 檢定與合併變異數", url: "topics/statistics-doe/lesson-37.html" },
            { title: "Welch 檢定與 Satterthwaite 自由度", url: "topics/statistics-doe/lesson-38.html" },
            { title: "成對 t 檢定與配對的價值", url: "topics/statistics-doe/lesson-39.html" },
            { title: "比例的檢定與區間", url: "topics/statistics-doe/lesson-40.html" },
            { title: "變異數的檢定與它的脆弱性", url: "topics/statistics-doe/lesson-41.html" }
          ]
        },
        {
          title: "模組 J｜卡方檢定與無母數方法",
          courses: [
            { title: "適合度檢定：為什麼是 Σ(O−E)²/E", url: "topics/statistics-doe/lesson-42.html" },
            { title: "獨立性檢定與費雪精確檢定", url: "topics/statistics-doe/lesson-43.html" },
            { title: "符號檢定與 Wilcoxon 符號秩檢定", url: "topics/statistics-doe/lesson-44.html" },
            { title: "Mann–Whitney 與 Kruskal–Wallis", url: "topics/statistics-doe/lesson-45.html" }
          ]
        },
        {
          title: "模組 K｜p 值的誤用、多重比較與複製危機",
          courses: [
            { title: "顯著結果有多可信：把貝氏定理用回來", url: "topics/statistics-doe/lesson-46.html" },
            { title: "多重比較與族群錯誤率", url: "topics/statistics-doe/lesson-47.html" },
            { title: "偽發現率與 Benjamini–Hochberg 程序", url: "topics/statistics-doe/lesson-48.html" },
            { title: "p-hacking、分岔小徑與複製危機", url: "topics/statistics-doe/lesson-49.html" },
            { title: "效果量、區間與貝氏因子", url: "topics/statistics-doe/lesson-50.html" }
          ]
        },
        {
          title: "模組 L｜簡單線性迴歸",
          courses: [
            { title: "最小平方法：正規方程式的推導", url: "topics/statistics-doe/lesson-51.html" },
            { title: "估計量的性質與誤差變異數", url: "topics/statistics-doe/lesson-52.html" },
            { title: "平方和分解與 R²", url: "topics/statistics-doe/lesson-53.html" },
            { title: "係數檢定、信賴帶與預測區間", url: "topics/statistics-doe/lesson-54.html" }
          ]
        },
        {
          title: "模組 M｜多元迴歸的矩陣形式",
          courses: [
            { title: "矩陣形式與正規方程式", url: "topics/statistics-doe/lesson-55.html" },
            { title: "帽子矩陣與槓桿值", url: "topics/statistics-doe/lesson-56.html" },
            { title: "高斯—馬可夫定理", url: "topics/statistics-doe/lesson-57.html" },
            { title: "共線性、部分 F 檢定與模型診斷", url: "topics/statistics-doe/lesson-58.html" }
          ]
        },
        {
          title: "模組 N｜變異數分析",
          courses: [
            { title: "為什麼需要變異數分析", url: "topics/statistics-doe/lesson-59.html" },
            { title: "平方和的分解", url: "topics/statistics-doe/lesson-60.html" },
            { title: "均方的期望值：F 檢定為何成立", url: "topics/statistics-doe/lesson-61.html" },
            { title: "事後比較：Tukey 與 Scheffé", url: "topics/statistics-doe/lesson-62.html" },
            { title: "雙因子變異數分析與交互作用", url: "topics/statistics-doe/lesson-63.html" }
          ]
        },
        {
          title: "模組 O｜實驗設計的三原則",
          courses: [
            { title: "觀察與實驗：因果從哪裡來", url: "topics/statistics-doe/lesson-64.html" },
            { title: "費雪的三原則", url: "topics/statistics-doe/lesson-65.html" },
            { title: "女士品茶：隨機化檢定的原型", url: "topics/statistics-doe/lesson-66.html" },
            { title: "區集化的效益與實驗規劃", url: "topics/statistics-doe/lesson-67.html" }
          ]
        },
        {
          title: "模組 P｜基本實驗設計",
          courses: [
            { title: "完全隨機設計", url: "topics/statistics-doe/lesson-68.html" },
            { title: "隨機完全區集設計", url: "topics/statistics-doe/lesson-69.html" },
            { title: "拉丁方與希臘拉丁方", url: "topics/statistics-doe/lesson-70.html" },
            { title: "巢狀設計與變異成分", url: "topics/statistics-doe/lesson-71.html" }
          ]
        },
        {
          title: "模組 Q｜二水準因子設計",
          courses: [
            { title: "為什麼一次改一個因子是錯的", url: "topics/statistics-doe/lesson-72.html" },
            { title: "2^k 的編碼與正交性", url: "topics/statistics-doe/lesson-73.html" },
            { title: "效果的估計與變異數", url: "topics/statistics-doe/lesson-74.html" },
            { title: "Yates 演算法與模型的建立", url: "topics/statistics-doe/lesson-75.html" },
            { title: "無重複設計：常態機率圖與 Lenth 法", url: "topics/statistics-doe/lesson-76.html" }
          ]
        },
        {
          title: "模組 R｜分數因子設計",
          courses: [
            { title: "半分數設計與產生元", url: "topics/statistics-doe/lesson-77.html" },
            { title: "定義關係與別名結構的推導", url: "topics/statistics-doe/lesson-78.html" },
            { title: "解析度與設計的選擇", url: "topics/statistics-doe/lesson-79.html" },
            { title: "篩選設計與摺疊", url: "topics/statistics-doe/lesson-80.html" }
          ]
        },
        {
          title: "模組 S｜反應曲面法",
          courses: [
            { title: "一階模型與最陡上升路徑", url: "topics/statistics-doe/lesson-81.html" },
            { title: "中心點與曲率檢定", url: "topics/statistics-doe/lesson-82.html" },
            { title: "二階模型與中央合成設計", url: "topics/statistics-doe/lesson-83.html" },
            { title: "標準點分析與曲面的判讀", url: "topics/statistics-doe/lesson-84.html" }
          ]
        },
        {
          title: "模組 T｜進階主題與實務總結",
          courses: [
            { title: "因子設計的區集化與混淆", url: "topics/statistics-doe/lesson-85.html" },
            { title: "裂區設計：兩個誤差項", url: "topics/statistics-doe/lesson-86.html" },
            { title: "穩健設計與田口方法的爭議", url: "topics/statistics-doe/lesson-87.html" },
            { title: "最適設計與設計的評價", url: "topics/statistics-doe/lesson-88.html" },
            { title: "完整案例與批判性閱讀清單", url: "topics/statistics-doe/lesson-89.html" }
          ]
        }
      ]
    },
    {
      id: "dc-universe",
      category: "fantasy",
      title: "DC 宇宙全解：從一九三八年到多重宇宙的神話工程",
      description:
        "以漫畫為主體、影視為分支，完整梳理 DC 八十七年的歷史、角色與設計原理：黃金到青銅時代的演變、危機與重啟的循環、黑暗時代的解構浪潮、四條互不相通的電影路線、電視與動畫為何常勝於電影，以及三巨頭、綠燈軍團、閃電俠家族、魔法層、青少年團隊與大反派陣容的逐一深入，最後收束到多重宇宙結構、宇宙論與必讀經典清單。",
      icon: "🦇",
      url: "topics/dc-universe/index.html",
      modules: [
        {
          title: "模組 A｜DC 導覽：超級英雄類型的發源地",
          courses: [
            { title: "一九三八年的那一格", url: "topics/dc-universe/lesson-01.html" },
            { title: "DC 的五個時代", url: "topics/dc-universe/lesson-02.html" },
            { title: "為什麼 DC 這麼難改編", url: "topics/dc-universe/lesson-03.html" },
            { title: "課程地圖：四軌並行", url: "topics/dc-universe/lesson-04.html" }
          ]
        },
        {
          title: "模組 B｜黃金時代與白銀時代",
          courses: [
            { title: "三巨頭的誕生與早期樣貌", url: "topics/dc-universe/lesson-05.html" },
            { title: "審查法典：一本書如何幾乎殺死一個產業", url: "topics/dc-universe/lesson-06.html" },
            { title: "白銀時代的復興：重做一切", url: "topics/dc-universe/lesson-07.html" },
            { title: "多重宇宙的發明", url: "topics/dc-universe/lesson-08.html" },
            { title: "白銀時代的怪異：那些荒謬故事的邏輯", url: "topics/dc-universe/lesson-09.html" }
          ]
        },
        {
          title: "模組 C｜青銅時代：漫畫長大了",
          courses: [
            { title: "綠燈俠與綠箭俠：社會議題進入漫畫", url: "topics/dc-universe/lesson-10.html" },
            { title: "蝙蝠俠回歸黑暗", url: "topics/dc-universe/lesson-11.html" },
            { title: "第四世界：DC 的神話層", url: "topics/dc-universe/lesson-12.html" },
            { title: "後果開始存在：青銅時代的死亡與代價", url: "topics/dc-universe/lesson-13.html" }
          ]
        },
        {
          title: "模組 D｜危機與重啟的循環",
          courses: [
            { title: "為什麼要親手毀掉多重宇宙", url: "topics/dc-universe/lesson-14.html" },
            { title: "無限地球危機：完整解析", url: "topics/dc-universe/lesson-15.html" },
            { title: "危機之後：三巨頭的重新設定", url: "topics/dc-universe/lesson-16.html" },
            { title: "零時、無限危機、最終危機", url: "topics/dc-universe/lesson-17.html" },
            { title: "閃點、新52、重生與無限邊疆", url: "topics/dc-universe/lesson-18.html" }
          ]
        },
        {
          title: "模組 E｜黑暗時代：解構的年代",
          courses: [
            { title: "《守護者》：把超級英雄放進現實檢驗", url: "topics/dc-universe/lesson-19.html" },
            { title: "《黑暗騎士歸來》：老去的蝙蝠俠", url: "topics/dc-universe/lesson-20.html" },
            { title: "《致命玩笑》與敘事的代價", url: "topics/dc-universe/lesson-21.html" },
            { title: "黑暗時代的後果：模仿的代價", url: "topics/dc-universe/lesson-22.html" }
          ]
        },
        {
          title: "模組 F｜前 DCEU：三個經典系列",
          courses: [
            { title: "一九七八年《超人》：讓觀眾相信人能飛", url: "topics/dc-universe/lesson-23.html" },
            { title: "提姆波頓的《蝙蝠俠》：哥德式哥譚", url: "topics/dc-universe/lesson-24.html" },
            { title: "《蝙蝠俠與羅賓》：一個系列如何崩壞", url: "topics/dc-universe/lesson-25.html" },
            { title: "諾蘭三部曲（上）：開戰時刻與黑暗騎士", url: "topics/dc-universe/lesson-26.html" },
            { title: "諾蘭三部曲（下）：黎明昇起與遺產", url: "topics/dc-universe/lesson-27.html" }
          ]
        },
        {
          title: "模組 G｜DCEU 完整解析（上）",
          courses: [
            { title: "《鋼鐵英雄》：查克史奈德的超人", url: "topics/dc-universe/lesson-28.html" },
            { title: "《蝙蝠俠對超人：正義曙光》", url: "topics/dc-universe/lesson-29.html" },
            { title: "《自殺突擊隊》（2016）：後製的災難", url: "topics/dc-universe/lesson-30.html" },
            { title: "《神力女超人》：DCEU 的高峰", url: "topics/dc-universe/lesson-31.html" },
            { title: "《正義聯盟》：兩個版本的故事", url: "topics/dc-universe/lesson-32.html" }
          ]
        },
        {
          title: "模組 H｜DCEU 完整解析（下）",
          courses: [
            { title: "《水行俠》與《沙贊》：轉向明亮", url: "topics/dc-universe/lesson-33.html" },
            { title: "《猛禽小隊》與《神力女超人 1984》", url: "topics/dc-universe/lesson-34.html" },
            { title: "《自殺突擊隊：集結》與《和平使者》", url: "topics/dc-universe/lesson-35.html" },
            { title: "《黑亞當》與《沙贊2》", url: "topics/dc-universe/lesson-36.html" },
            { title: "《閃電俠》與《水行俠2》：DCEU 的收場", url: "topics/dc-universe/lesson-37.html" }
          ]
        },
        {
          title: "模組 I｜Elseworlds 與新 DCU",
          courses: [
            { title: "《小丑》：一部不屬於任何宇宙的電影", url: "topics/dc-universe/lesson-38.html" },
            { title: "《蝙蝠俠》（2022）：偵探路線的回歸", url: "topics/dc-universe/lesson-39.html" },
            { title: "新 DCU 的第一章：《超人》（2025）", url: "topics/dc-universe/lesson-40.html" },
            { title: "版本地圖：哪個是哪個", url: "topics/dc-universe/lesson-41.html" }
          ]
        },
        {
          title: "模組 J｜真人影集宇宙",
          courses: [
            { title: "《超人前傳》：十年的成長故事", url: "topics/dc-universe/lesson-42.html" },
            { title: "《綠箭俠》與 Arrowverse 的建立", url: "topics/dc-universe/lesson-43.html" },
            { title: "《閃電俠》《超女》《明日傳奇》與跨界事件", url: "topics/dc-universe/lesson-44.html" },
            { title: "影集版《無限地球危機》：電視完成了電影做不到的事", url: "topics/dc-universe/lesson-45.html" },
            { title: "《泰坦》《末日巡邏隊》《高譚》《潘尼沃斯》：其他路線", url: "topics/dc-universe/lesson-46.html" }
          ]
        },
        {
          title: "模組 K｜DC 動畫宇宙",
          courses: [
            { title: "《蝙蝠俠動畫系列》：為什麼它是標準答案", url: "topics/dc-universe/lesson-47.html" },
            { title: "《超人動畫影集》與 DCAU 的擴張", url: "topics/dc-universe/lesson-48.html" },
            { title: "《正義聯盟》與《正義聯盟無限》", url: "topics/dc-universe/lesson-49.html" },
            { title: "《少年悍將》與《少年正義》：兩種青少年英雄敘事", url: "topics/dc-universe/lesson-50.html" },
            { title: "DC 動畫電影：改編漫畫的主要管道", url: "topics/dc-universe/lesson-51.html" }
          ]
        },
        {
          title: "模組 L｜超人與超人家族",
          courses: [
            { title: "克拉克肯特：三個身分的真正結構", url: "topics/dc-universe/lesson-52.html" },
            { title: "能力、極限與氪石的分類學", url: "topics/dc-universe/lesson-53.html" },
            { title: "露薏絲蓮恩與星球日報", url: "topics/dc-universe/lesson-54.html" },
            { title: "超級女孩、超少年與超人家族", url: "topics/dc-universe/lesson-55.html" },
            { title: "超人的哲學：為何不殺，為何不統治", url: "topics/dc-universe/lesson-56.html" }
          ]
        },
        {
          title: "模組 M｜蝙蝠俠與蝙蝠家族",
          courses: [
            { title: "布魯斯韋恩：哪一個才是面具", url: "topics/dc-universe/lesson-57.html" },
            { title: "不殺原則與高譚的旋轉門", url: "topics/dc-universe/lesson-58.html" },
            { title: "羅賓的傳承：四個人與一個位置", url: "topics/dc-universe/lesson-59.html" },
            { title: "蝙蝠女與神諭：從失去到重新定義", url: "topics/dc-universe/lesson-60.html" },
            { title: "阿福：唯一有資格說不的人", url: "topics/dc-universe/lesson-61.html" },
            { title: "高譚市作為角色：一座不能被治好的城市", url: "topics/dc-universe/lesson-62.html" }
          ]
        },
        {
          title: "模組 N｜神力女超人與亞馬遜",
          courses: [
            { title: "黛安娜：使者而非戰士", url: "topics/dc-universe/lesson-63.html" },
            { title: "創作起源：一個心理學家的設計", url: "topics/dc-universe/lesson-64.html" },
            { title: "亞馬遜、天堂島與希臘諸神", url: "topics/dc-universe/lesson-65.html" },
            { title: "能力、神器與戰鬥風格", url: "topics/dc-universe/lesson-66.html" }
          ]
        },
        {
          title: "模組 O｜綠燈俠軍團與情緒光譜",
          courses: [
            { title: "情緒光譜：把情緒寫成物理定律", url: "topics/dc-universe/lesson-67.html" },
            { title: "地球的綠燈俠們：四種意志", url: "topics/dc-universe/lesson-68.html" },
            { title: "守護者、歐亞星與軍團的制度問題", url: "topics/dc-universe/lesson-69.html" },
            { title: "辛尼斯托：一個有道理的反派", url: "topics/dc-universe/lesson-70.html" },
            { title: "《最黑暗之夜》與白燈：死亡作為主題", url: "topics/dc-universe/lesson-71.html" }
          ]
        },
        {
          title: "模組 P｜閃電俠家族與神速力",
          courses: [
            { title: "四代閃電俠：DC 最成功的傳承", url: "topics/dc-universe/lesson-72.html" },
            { title: "神速力：把速度寫成宇宙的基礎結構", url: "topics/dc-universe/lesson-73.html" },
            { title: "逆閃電：以恨為動力的鏡像", url: "topics/dc-universe/lesson-74.html" },
            { title: "《閃點》：一次善意的災難", url: "topics/dc-universe/lesson-75.html" }
          ]
        },
        {
          title: "模組 Q｜正義聯盟的其他核心",
          courses: [
            { title: "亞瑟庫瑞：一個被嘲笑了五十年的角色", url: "topics/dc-universe/lesson-76.html" },
            { title: "亞特蘭提斯與七海王國", url: "topics/dc-universe/lesson-77.html" },
            { title: "火星獵人：聯盟真正的核心", url: "topics/dc-universe/lesson-78.html" },
            { title: "綠箭俠與街頭層級的英雄", url: "topics/dc-universe/lesson-79.html" },
            { title: "鋼骨、沙贊、原子俠與聯盟名單的變化", url: "topics/dc-universe/lesson-80.html" }
          ]
        },
        {
          title: "模組 R｜正義聯盟黑暗與 Vertigo",
          courses: [
            { title: "康斯坦丁：一個會讓朋友死掉的主角", url: "topics/dc-universe/lesson-81.html" },
            { title: "沼澤異形與「綠色」：一次徹底的重新定義", url: "topics/dc-universe/lesson-82.html" },
            { title: "死亡俠、扎坦娜與正義聯盟黑暗", url: "topics/dc-universe/lesson-83.html" },
            { title: "《睡魔》與無盡家族", url: "topics/dc-universe/lesson-84.html" },
            { title: "Vertigo：成人漫畫廠牌的興衰", url: "topics/dc-universe/lesson-85.html" }
          ]
        },
        {
          title: "模組 S｜青少年英雄與其他團隊",
          courses: [
            { title: "少年悍將的三個世代", url: "topics/dc-universe/lesson-86.html" },
            { title: "自殺突擊隊：被強迫的英雄主義", url: "topics/dc-universe/lesson-87.html" },
            { title: "超級英雄軍團：一千年後的遺產", url: "topics/dc-universe/lesson-88.html" },
            { title: "末日巡邏隊：把超能力寫成創傷", url: "topics/dc-universe/lesson-89.html" }
          ]
        },
        {
          title: "模組 T｜大反派全覽",
          courses: [
            { title: "小丑：一個沒有起源的角色", url: "topics/dc-universe/lesson-90.html" },
            { title: "雷克斯路瑟：人類最好的論點", url: "topics/dc-universe/lesson-91.html" },
            { title: "達克賽德與反生命方程式", url: "topics/dc-universe/lesson-92.html" },
            { title: "布萊尼亞克與佐德將軍", url: "topics/dc-universe/lesson-93.html" },
            { title: "拉斯奧古與影武者聯盟", url: "topics/dc-universe/lesson-94.html" },
            { title: "黑亞當、末日與貓女：三種灰色地帶", url: "topics/dc-universe/lesson-95.html" }
          ]
        },
        {
          title: "模組 U｜多重宇宙與宇宙論",
          courses: [
            { title: "五十二個地球：多重宇宙的當代結構", url: "topics/dc-universe/lesson-96.html" },
            { title: "源頭之牆、造物主與宇宙的邊界", url: "topics/dc-universe/lesson-97.html" },
            { title: "新神族與第四世界", url: "topics/dc-universe/lesson-98.html" },
            { title: "監視者與更高存在", url: "topics/dc-universe/lesson-99.html" },
            { title: "《末日鐘聲》：DC 對自己的檢討", url: "topics/dc-universe/lesson-100.html" }
          ]
        },
        {
          title: "模組 V｜必讀經典與遊戲改編",
          courses: [
            { title: "《王國降臨》：關於世代與退場的作品", url: "topics/dc-universe/lesson-101.html" },
            { title: "《全明星超人》：如果只剩一年", url: "topics/dc-universe/lesson-102.html" },
            { title: "《漫長的萬聖節》與《元年》", url: "topics/dc-universe/lesson-103.html" },
            { title: "《黑暗之夜：金屬》與當代大事件", url: "topics/dc-universe/lesson-104.html" },
            { title: "阿卡漢系列與《不義聯盟》：遊戲改編", url: "topics/dc-universe/lesson-105.html" }
          ]
        },
        {
          title: "模組 W｜課程總結",
          courses: [
            { title: "八十七年的神話工程", url: "topics/dc-universe/lesson-106.html" }
          ]
        }
      ]
    },
    {
      id: "four-classics",
      category: "wuxia",
      title: "四大名著懶人包：三國演義·水滸傳·西遊記·紅樓夢全解析",
      description:
        "用「作者與成書背景、劇情詳解、人物詳解」三個角度，完整拆解中國古典文學四大名著：《三國演義》的亂世群雄與三分天下、《水滸傳》一百零八將的聚義與悲劇、《西遊記》取經團隊的九九八十一難、《紅樓夢》賈府興衰與大觀園兒女的悲歡離合，四部作品份量對稱，方便交叉比較，用現代白話一次讀懂中國古典小說的巔峰之作。",
      icon: "📜",
      url: "topics/four-classics/index.html",
      modules: [
        {
          title: "模組 A｜序：什麼是四大名著",
          courses: [
            { title: "四大名著是怎麼被選出來的：一個逐漸形成的文學經典化過程", url: "topics/four-classics/lesson-01.html" },
            { title: "成書年代與體裁：從說書到章回小說", url: "topics/four-classics/lesson-02.html" },
            { title: "模組總結：這門課會怎麼帶你認識這四部書", url: "topics/four-classics/lesson-03.html" }
          ]
        },
        {
          title: "模組 B｜三國演義：作者與成書背景",
          courses: [
            { title: "羅貫中其人：一個資料稀少的作者", url: "topics/four-classics/lesson-04.html" },
            { title: "從陳壽《三國志》到民間說書：三國故事的成形過程", url: "topics/four-classics/lesson-05.html" },
            { title: "模組總結：「七分實三分虛」的歷史小說", url: "topics/four-classics/lesson-06.html" }
          ]
        },
        {
          title: "模組 C｜三國演義：劇情詳解（上）",
          courses: [
            { title: "黃巾之亂與群雄並起", url: "topics/four-classics/lesson-07.html" },
            { title: "董卓亂政與十八路諸侯討董", url: "topics/four-classics/lesson-08.html" },
            { title: "官渡之戰：曹操統一北方", url: "topics/four-classics/lesson-09.html" },
            { title: "三顧茅廬與隆中對", url: "topics/four-classics/lesson-10.html" },
            { title: "赤壁之戰：三分天下的關鍵一役", url: "topics/four-classics/lesson-11.html" },
            { title: "模組總結：從亂世到三分天下的雛形", url: "topics/four-classics/lesson-12.html" }
          ]
        },
        {
          title: "模組 D｜三國演義：劇情詳解（下）",
          courses: [
            { title: "劉備入蜀與漢中之戰", url: "topics/four-classics/lesson-13.html" },
            { title: "關羽敗走麥城", url: "topics/four-classics/lesson-14.html" },
            { title: "夷陵之戰與劉備託孤", url: "topics/four-classics/lesson-15.html" },
            { title: "諸葛亮北伐：六出祁山", url: "topics/four-classics/lesson-16.html" },
            { title: "三國歸晉：一個時代的終結", url: "topics/four-classics/lesson-17.html" },
            { title: "模組總結：三國演義的敘事弧線全貌", url: "topics/four-classics/lesson-18.html" }
          ]
        },
        {
          title: "模組 E｜三國演義：人物詳解",
          courses: [
            { title: "曹操：奸雄還是英雄", url: "topics/four-classics/lesson-19.html" },
            { title: "劉備：仁德之君的另一面", url: "topics/four-classics/lesson-20.html" },
            { title: "諸葛亮：智絕的形象是怎麼被塑造出來的", url: "topics/four-classics/lesson-21.html" },
            { title: "關羽、張飛：義絕與勇將", url: "topics/four-classics/lesson-22.html" },
            { title: "孫權與江東文武", url: "topics/four-classics/lesson-23.html" },
            { title: "模組總結：三國演義的人物群像", url: "topics/four-classics/lesson-24.html" }
          ]
        },
        {
          title: "模組 F｜水滸傳：作者與成書背景",
          courses: [
            { title: "施耐庵其人：另一個謎樣的作者", url: "topics/four-classics/lesson-25.html" },
            { title: "從《大宋宣和遺事》到梁山好漢：水滸故事的演變", url: "topics/four-classics/lesson-26.html" },
            { title: "模組總結：一部關於「官逼民反」的小說", url: "topics/four-classics/lesson-27.html" }
          ]
        },
        {
          title: "模組 G｜水滸傳：劇情詳解（上）",
          courses: [
            { title: "魯智深拳打鎮關西", url: "topics/four-classics/lesson-28.html" },
            { title: "林沖夜奔梁山", url: "topics/four-classics/lesson-29.html" },
            { title: "武松打虎與血濺鴛鴦樓", url: "topics/four-classics/lesson-30.html" },
            { title: "智取生辰綱", url: "topics/four-classics/lesson-31.html" },
            { title: "宋江上山與梁山排座次", url: "topics/four-classics/lesson-32.html" },
            { title: "模組總結：一百零八將是怎麼聚集起來的", url: "topics/four-classics/lesson-33.html" }
          ]
        },
        {
          title: "模組 H｜水滸傳：劇情詳解（下）",
          courses: [
            { title: "兩贏童貫、三敗高俅", url: "topics/four-classics/lesson-34.html" },
            { title: "招安：梁山的轉折點", url: "topics/four-classics/lesson-35.html" },
            { title: "征遼與平定田虎、王慶", url: "topics/four-classics/lesson-36.html" },
            { title: "征方臘：好漢們的悲劇結局", url: "topics/four-classics/lesson-37.html" },
            { title: "模組總結：從聚義到悲劇收場", url: "topics/four-classics/lesson-38.html" }
          ]
        },
        {
          title: "模組 I｜水滸傳：人物詳解",
          courses: [
            { title: "宋江：及時雨還是投降派", url: "topics/four-classics/lesson-39.html" },
            { title: "魯智深與武松：兩種不同的江湖正義", url: "topics/four-classics/lesson-40.html" },
            { title: "林沖：被逼上梁山的典型", url: "topics/four-classics/lesson-41.html" },
            { title: "李逵：忠義與莽撞的矛盾體", url: "topics/four-classics/lesson-42.html" },
            { title: "吳用與梁山的智謀團隊", url: "topics/four-classics/lesson-43.html" },
            { title: "模組總結：一百零八將的性格光譜", url: "topics/four-classics/lesson-44.html" }
          ]
        },
        {
          title: "模組 J｜西遊記：作者與成書背景",
          courses: [
            { title: "吳承恩其人：從落第書生到寫出神魔小說", url: "topics/four-classics/lesson-45.html" },
            { title: "從玄奘取經到神魔演義：西遊故事的演變", url: "topics/four-classics/lesson-46.html" },
            { title: "模組總結：一部披著取經外衣的諷刺小說", url: "topics/four-classics/lesson-47.html" }
          ]
        },
        {
          title: "模組 K｜西遊記：劇情詳解（上）",
          courses: [
            { title: "石猴出世與大鬧天宮", url: "topics/four-classics/lesson-48.html" },
            { title: "五行山下五百年", url: "topics/four-classics/lesson-49.html" },
            { title: "唐僧出世與奉旨取經", url: "topics/four-classics/lesson-50.html" },
            { title: "收伏孫悟空", url: "topics/four-classics/lesson-51.html" },
            { title: "收伏豬八戒與沙悟淨", url: "topics/four-classics/lesson-52.html" },
            { title: "模組總結：取經團隊的組成", url: "topics/four-classics/lesson-53.html" }
          ]
        },
        {
          title: "模組 L｜西遊記：劇情詳解（下）",
          courses: [
            { title: "三打白骨精", url: "topics/four-classics/lesson-54.html" },
            { title: "車遲國鬥法", url: "topics/four-classics/lesson-55.html" },
            { title: "三借芭蕉扇", url: "topics/four-classics/lesson-56.html" },
            { title: "天竺國與真假公主", url: "topics/four-classics/lesson-57.html" },
            { title: "九九八十一難修成正果", url: "topics/four-classics/lesson-58.html" },
            { title: "模組總結：西遊記的取經結構", url: "topics/four-classics/lesson-59.html" }
          ]
        },
        {
          title: "模組 M｜西遊記：人物詳解",
          courses: [
            { title: "孫悟空：從叛逆者到護法者", url: "topics/four-classics/lesson-60.html" },
            { title: "豬八戒：慾望與人性的化身", url: "topics/four-classics/lesson-61.html" },
            { title: "唐僧：軟弱還是堅定的另一種詮釋", url: "topics/four-classics/lesson-62.html" },
            { title: "沙悟淨與各路神仙妖怪", url: "topics/four-classics/lesson-63.html" },
            { title: "模組總結：西遊記的人物象徵意義", url: "topics/four-classics/lesson-64.html" }
          ]
        },
        {
          title: "模組 N｜紅樓夢：作者與成書背景",
          courses: [
            { title: "曹雪芹其人：從富貴到落魄的家族史", url: "topics/four-classics/lesson-65.html" },
            { title: "紅樓夢的版本之謎：八十回與後四十回", url: "topics/four-classics/lesson-66.html" },
            { title: "脂硯齋批語與紅學研究", url: "topics/four-classics/lesson-67.html" },
            { title: "模組總結：一部「一把辛酸淚」的自傳性小說", url: "topics/four-classics/lesson-68.html" }
          ]
        },
        {
          title: "模組 O｜紅樓夢：劇情詳解（上）",
          courses: [
            { title: "女媧補天與絳珠仙草：神話楔子", url: "topics/four-classics/lesson-69.html" },
            { title: "賈府的興盛與大觀園的建立", url: "topics/four-classics/lesson-70.html" },
            { title: "黛玉進賈府", url: "topics/four-classics/lesson-71.html" },
            { title: "寶黛初會與金玉良緣的伏筆", url: "topics/four-classics/lesson-72.html" },
            { title: "元妃省親", url: "topics/four-classics/lesson-73.html" },
            { title: "模組總結：賈府盛世的鋪陳", url: "topics/four-classics/lesson-74.html" }
          ]
        },
        {
          title: "模組 P｜紅樓夢：劇情詳解（下）",
          courses: [
            { title: "大觀園的詩社與青春歲月", url: "topics/four-classics/lesson-75.html" },
            { title: "抄檢大觀園：盛極而衰的轉折", url: "topics/four-classics/lesson-76.html" },
            { title: "寶黛愛情的悲劇", url: "topics/four-classics/lesson-77.html" },
            { title: "賈府的衰敗與抄家", url: "topics/four-classics/lesson-78.html" },
            { title: "白茫茫大地真乾淨：結局的多重解讀", url: "topics/four-classics/lesson-79.html" },
            { title: "模組總結：從烈火烹油到落了片白茫茫大地", url: "topics/four-classics/lesson-80.html" }
          ]
        },
        {
          title: "模組 Q｜紅樓夢：人物詳解",
          courses: [
            { title: "賈寶玉：一個反抗禮教的貴族公子", url: "topics/four-classics/lesson-81.html" },
            { title: "林黛玉：才情與悲劇性格", url: "topics/four-classics/lesson-82.html" },
            { title: "薛寶釵：世故還是另一種真誠", url: "topics/four-classics/lesson-83.html" },
            { title: "王熙鳳：精明能幹的悲劇管家", url: "topics/four-classics/lesson-84.html" },
            { title: "賈母與賈府的女性群像", url: "topics/four-classics/lesson-85.html" },
            { title: "模組總結：紅樓夢的人物群像與判詞", url: "topics/four-classics/lesson-86.html" }
          ]
        },
        {
          title: "模組 R｜課程總結",
          courses: [
            { title: "全課程總結：四大名著為什麼歷久不衰", url: "topics/four-classics/lesson-87.html" }
          ]
        }
      ]
    },
    {
      id: "string-theory",
      category: "science",
      title: "超弦理論入門：一條弦，如何試圖統一宇宙的四大作用力",
      description:
        "用比喻與圖解取代密集推導，淺顯易懂地認識超弦理論：從廣義相對論與量子力學的衝突出發，理解為什麼要把點粒子換成一條會震動的弦、重力子如何自動冒出來、額外維度與卡拉比-丘流形、五種弦論如何被 M 理論統一、D-膜與全息原理，最後誠實面對它至今仍未被實驗證實的爭議。不推導方程式，但邏輯鏈完整。",
      icon: "🎻",
      url: "topics/string-theory/index.html",
      modules: [
        {
          title: "模組 A｜序幕：為什麼需要一個新的理論",
          courses: [
            { title: "廣義相對論與量子力學：兩個各自成功、卻互相衝突的理論", url: "topics/string-theory/lesson-01.html" },
            { title: "黑洞中心與大霹靂瞬間：兩個理論同時失靈的地方", url: "topics/string-theory/lesson-02.html" },
            { title: "什麼是「量子重力」：物理學最大的未解之謎", url: "topics/string-theory/lesson-03.html" },
            { title: "弦理論登場：把點粒子換成一條會震動的弦", url: "topics/string-theory/lesson-04.html" },
            { title: "模組總結：這門課要帶你認識什麼", url: "topics/string-theory/lesson-05.html" }
          ]
        },
        {
          title: "模組 B｜核心概念：從點粒子到弦",
          courses: [
            { title: "點粒子模型的極限：為什麼「無限小」在數學上會出問題", url: "topics/string-theory/lesson-06.html" },
            { title: "弦：一維延展的基本物件", url: "topics/string-theory/lesson-07.html" },
            { title: "開弦與閉弦：兩端固定與首尾相連", url: "topics/string-theory/lesson-08.html" },
            { title: "弦的張力與普朗克長度：小到超乎想像的尺度", url: "topics/string-theory/lesson-09.html" },
            { title: "模組總結：從「是什麼」到「弦在做什麼」", url: "topics/string-theory/lesson-10.html" }
          ]
        },
        {
          title: "模組 C｜弦的震動與基本粒子",
          courses: [
            { title: "震動模式決定一切：弦論的核心洞察", url: "topics/string-theory/lesson-11.html" },
            { title: "質量從哪裡來：震動能量與愛因斯坦的E=mc²", url: "topics/string-theory/lesson-12.html" },
            { title: "自旋是什麼：震動模式如何對應到粒子的量子數", url: "topics/string-theory/lesson-13.html" },
            { title: "一條弦，無數種粒子：弦論如何統一物質與作用力", url: "topics/string-theory/lesson-14.html" },
            { title: "模組總結：從一條弦到一整個粒子動物園", url: "topics/string-theory/lesson-15.html" }
          ]
        },
        {
          title: "模組 D｜重力子：弦論最著名的預言",
          courses: [
            { title: "重力子是什麼：傳遞重力的假想粒子", url: "topics/string-theory/lesson-16.html" },
            { title: "閉弦的無質量自旋二模式：重力子為什麼「自動」出現", url: "topics/string-theory/lesson-17.html" },
            { title: "這為什麼是件大事：弦論如何意外解決了量子重力問題", url: "topics/string-theory/lesson-18.html" },
            { title: "模組總結：一個沒人特別去找、卻自己冒出來的粒子", url: "topics/string-theory/lesson-19.html" }
          ]
        },
        {
          title: "模組 E｜額外維度：為什麼我們的世界不只三維空間",
          courses: [
            { title: "數學要求：弦論的方程式在幾維空間才自洽", url: "topics/string-theory/lesson-20.html" },
            { title: "十維與十一維：不同版本弦論的維度需求", url: "topics/string-theory/lesson-21.html" },
            { title: "捲曲的維度：為什麼我們感覺不到多出來的空間", url: "topics/string-theory/lesson-22.html" },
            { title: "一個生活化比喻：花園水管與螞蟻的視角", url: "topics/string-theory/lesson-23.html" },
            { title: "模組總結：維度不是抽象數字，是具體的空間結構", url: "topics/string-theory/lesson-24.html" }
          ]
        },
        {
          title: "模組 F｜卡拉比-丘流形與緊化",
          courses: [
            { title: "緊化是什麼：把多餘維度「捲」到看不見的尺度", url: "topics/string-theory/lesson-25.html" },
            { title: "卡拉比-丘流形：一種特殊形狀的六維空間", url: "topics/string-theory/lesson-26.html" },
            { title: "形狀決定物理：不同的捲曲方式，對應不同的粒子世界", url: "topics/string-theory/lesson-27.html" },
            { title: "模組總結：弦論的「多重宇宙」問題從這裡開始", url: "topics/string-theory/lesson-28.html" }
          ]
        },
        {
          title: "模組 G｜超對稱：弦論的必要夥伴",
          courses: [
            { title: "對稱性在物理學裡的角色", url: "topics/string-theory/lesson-29.html" },
            { title: "超對稱是什麼：玻色子與費米子的鏡像夥伴", url: "topics/string-theory/lesson-30.html" },
            { title: "為什麼弦論需要超對稱才能自洽", url: "topics/string-theory/lesson-31.html" },
            { title: "模組總結：超弦理論名字裡的「超」是什麼意思", url: "topics/string-theory/lesson-32.html" }
          ]
        },
        {
          title: "模組 H｜五種弦論與M理論的統一",
          courses: [
            { title: "一開始的困惑：物理學家發現了五種不同的弦論", url: "topics/string-theory/lesson-33.html" },
            { title: "五種弦論分別是什麼：簡單認識它們的差異", url: "topics/string-theory/lesson-34.html" },
            { title: "對偶性：看似不同的理論，其實是同一件事的不同面貌", url: "topics/string-theory/lesson-35.html" },
            { title: "M理論：威滕的統一構想", url: "topics/string-theory/lesson-36.html" },
            { title: "模組總結：從五個拼圖到一張更大的地圖", url: "topics/string-theory/lesson-37.html" }
          ]
        },
        {
          title: "模組 I｜D-膜：弦論裡的延伸物體",
          courses: [
            { title: "不只是弦：弦論裡還有更高維度的物體", url: "topics/string-theory/lesson-38.html" },
            { title: "D-膜是什麼：開弦端點固定的地方", url: "topics/string-theory/lesson-39.html" },
            { title: "D-膜如何改變我們對弦論的理解", url: "topics/string-theory/lesson-40.html" },
            { title: "模組總結：從一維的弦到多維的膜", url: "topics/string-theory/lesson-41.html" }
          ]
        },
        {
          title: "模組 J｜全息原理與AdS/CFT",
          courses: [
            { title: "全息原理：一個空間的資訊，可能藏在它的邊界上", url: "topics/string-theory/lesson-42.html" },
            { title: "AdS/CFT對應：馬爾達西那的重大發現", url: "topics/string-theory/lesson-43.html" },
            { title: "這件事為什麼重要：連接弦論與其他物理領域", url: "topics/string-theory/lesson-44.html" },
            { title: "模組總結：弦論意外打開的一扇新窗", url: "topics/string-theory/lesson-45.html" }
          ]
        },
        {
          title: "模組 K｜黑洞與弦論",
          courses: [
            { title: "黑洞熵：貝肯斯坦與霍金留下的謎題", url: "topics/string-theory/lesson-46.html" },
            { title: "弦論如何計算黑洞熵：一次漂亮的驗證", url: "topics/string-theory/lesson-47.html" },
            { title: "模組總結：弦論在黑洞物理上交出的成績單", url: "topics/string-theory/lesson-48.html" }
          ]
        },
        {
          title: "模組 L｜爭議與挑戰：弦論真的是對的嗎",
          courses: [
            { title: "最大的問題：至今沒有直接的實驗證據", url: "topics/string-theory/lesson-49.html" },
            { title: "弦論地景：10^500種可能的宇宙，哪一個是我們的", url: "topics/string-theory/lesson-50.html" },
            { title: "可否證性的爭論：弦論還算是一個科學理論嗎", url: "topics/string-theory/lesson-51.html" },
            { title: "另一條路：迴圈量子重力等競爭理論簡介", url: "topics/string-theory/lesson-52.html" },
            { title: "模組總結：誠實面對一個尚未被證實的理論", url: "topics/string-theory/lesson-53.html" }
          ]
        },
        {
          title: "模組 M｜課程總結",
          courses: [
            { title: "全課程總結：從一條弦，到理解宇宙最深層結構的嘗試", url: "topics/string-theory/lesson-54.html" }
          ]
        }
      ]
    },
    {
      id: "adventure-time",
      category: "fantasy",
      title: "探險活寶全紀錄：Ooo大陸的故事線與人物深度剖析",
      description:
        "深入解析卡通《探險活寶》：從蘑菇戰爭後的Ooo大陸世界觀開始，梳理冰霸王的真實身分、馬瑟琳與冰霸王的羈絆、巫妖的威脅、芬恩尋父之旅、芬妮與凱克的平行宇宙、GOLB與大結局等主線故事弧，並用獨立模組深度剖析芬恩、傑克、泡泡糖公主、冰霸王、馬瑟琳等核心角色，最後探討這部披著兒童卡通外皮的作品，為什麼能同時打動孩子與大人。",
      icon: "🍭",
      url: "topics/adventure-time/index.html",
      modules: [
        {
          title: "模組 A｜序幕：什麼是探險活寶",
          courses: [
            { title: "一部披著兒童卡通外皮的深刻作品", url: "topics/adventure-time/lesson-01.html" },
            { title: "誕生故事：潘德頓·沃德與這個世界的由來", url: "topics/adventure-time/lesson-02.html" },
            { title: "模組總結：這門課要怎麼帶你認識這個世界", url: "topics/adventure-time/lesson-03.html" }
          ]
        },
        {
          title: "模組 B｜世界觀：蘑菇戰爭後的Ooo大陸",
          courses: [
            { title: "蘑菇戰爭：一場核災之後的世界", url: "topics/adventure-time/lesson-04.html" },
            { title: "Ooo大陸各王國巡禮", url: "topics/adventure-time/lesson-05.html" },
            { title: "魔法與科技並存的奇幻邏輯", url: "topics/adventure-time/lesson-06.html" },
            { title: "人類的稀有：芬恩為什麼特別", url: "topics/adventure-time/lesson-07.html" },
            { title: "模組總結", url: "topics/adventure-time/lesson-08.html" }
          ]
        },
        {
          title: "模組 C｜芬恩與傑克：兄弟情誼的起點",
          courses: [
            { title: "芬恩：森林裡長大的最後人類男孩", url: "topics/adventure-time/lesson-09.html" },
            { title: "傑克：會伸縮變形的魔法狗", url: "topics/adventure-time/lesson-10.html" },
            { title: "兩兄弟的羈絆：領養與家人的意義", url: "topics/adventure-time/lesson-11.html" },
            { title: "芬恩的成長弧線：從衝動少年到獨當一面", url: "topics/adventure-time/lesson-12.html" },
            { title: "模組總結", url: "topics/adventure-time/lesson-13.html" }
          ]
        },
        {
          title: "模組 D｜故事線①：冰霸王的真實身分",
          courses: [
            { title: "初登場的冰霸王：一個滑稽的反派", url: "topics/adventure-time/lesson-14.html" },
            { title: "賽門·佩崔科夫：戴上皇冠之前的他", url: "topics/adventure-time/lesson-15.html" },
            { title: "皇冠的詛咒：力量與瘋狂的代價", url: "topics/adventure-time/lesson-16.html" },
            { title: "逐漸揭露的真相：冰霸王故事線裡的線索", url: "topics/adventure-time/lesson-17.html" },
            { title: "模組總結：一個令人心碎的悲劇反派", url: "topics/adventure-time/lesson-18.html" }
          ]
        },
        {
          title: "模組 E｜故事線②：馬瑟琳與冰霸王的羈絆",
          courses: [
            { title: "馬瑟琳：千年吸血鬼皇后的日常", url: "topics/adventure-time/lesson-19.html" },
            { title: "蘑菇戰爭倖存的孩子：年幼的馬瑟琳", url: "topics/adventure-time/lesson-20.html" },
            { title: "賽門與瑪西：一段被遺忘的守護關係", url: "topics/adventure-time/lesson-21.html" },
            { title: "從父女般的情誼到彼此陌生", url: "topics/adventure-time/lesson-22.html" },
            { title: "模組總結", url: "topics/adventure-time/lesson-23.html" }
          ]
        },
        {
          title: "模組 F｜故事線③：巫妖的威脅",
          courses: [
            { title: "巫妖是誰：終結一切生命的古老存在", url: "topics/adventure-time/lesson-24.html" },
            { title: "首次交手：巫妖的初登場", url: "topics/adventure-time/lesson-25.html" },
            { title: "巫妖與蘑菇戰爭的關聯", url: "topics/adventure-time/lesson-26.html" },
            { title: "多次交手：貫穿全劇的終極反派", url: "topics/adventure-time/lesson-27.html" },
            { title: "模組總結", url: "topics/adventure-time/lesson-28.html" }
          ]
        },
        {
          title: "模組 G｜故事線④：芬恩尋父之旅",
          courses: [
            { title: "一個關於父親的謎團", url: "topics/adventure-time/lesson-29.html" },
            { title: "馬丁·蒙頓：芬恩找到的生父", url: "topics/adventure-time/lesson-30.html" },
            { title: "島嶼特輯：一趟令人失望卻重要的旅程", url: "topics/adventure-time/lesson-31.html" },
            { title: "模組總結", url: "topics/adventure-time/lesson-32.html" }
          ]
        },
        {
          title: "模組 H｜故事線⑤：芬妮與凱克的平行宇宙",
          courses: [
            { title: "平行宇宙的設定：如果芬恩是女生", url: "topics/adventure-time/lesson-33.html" },
            { title: "芬妮與凱克的故事線", url: "topics/adventure-time/lesson-34.html" },
            { title: "這條支線為什麼重要", url: "topics/adventure-time/lesson-35.html" },
            { title: "模組總結", url: "topics/adventure-time/lesson-36.html" }
          ]
        },
        {
          title: "模組 I｜大結局：GOLB與Ooo的終章",
          courses: [
            { title: "GOLB：比巫妖更古老的威脅", url: "topics/adventure-time/lesson-37.html" },
            { title: "「與我同行」：最終季的收尾", url: "topics/adventure-time/lesson-38.html" },
            { title: "Ooo大陸的下一步", url: "topics/adventure-time/lesson-39.html" },
            { title: "模組總結", url: "topics/adventure-time/lesson-40.html" }
          ]
        },
        {
          title: "模組 J｜人物剖析：主角團",
          courses: [
            { title: "芬恩深度剖析：英雄旅程與心理成長", url: "topics/adventure-time/lesson-41.html" },
            { title: "傑克深度剖析：看似隨性背後的智慧", url: "topics/adventure-time/lesson-42.html" },
            { title: "BMO深度剖析：一個機器人的自我認同", url: "topics/adventure-time/lesson-43.html" },
            { title: "主角團的家庭結構", url: "topics/adventure-time/lesson-44.html" },
            { title: "模組總結", url: "topics/adventure-time/lesson-45.html" }
          ]
        },
        {
          title: "模組 K｜人物剖析：泡泡糖公主",
          courses: [
            { title: "泡泡糖公主：科學家統治者的雙面性", url: "topics/adventure-time/lesson-46.html" },
            { title: "糖果王國的統治邏輯與代價", url: "topics/adventure-time/lesson-47.html" },
            { title: "泡泡糖公主與芬恩的複雜關係", url: "topics/adventure-time/lesson-48.html" },
            { title: "模組總結", url: "topics/adventure-time/lesson-49.html" }
          ]
        },
        {
          title: "模組 L｜人物剖析：冰霸王與馬瑟琳",
          courses: [
            { title: "冰霸王：全劇最複雜的角色之一", url: "topics/adventure-time/lesson-50.html" },
            { title: "記憶與身分：冰霸王故事線背後的隱喻", url: "topics/adventure-time/lesson-51.html" },
            { title: "馬瑟琳：搖滾與孤獨的千年生命", url: "topics/adventure-time/lesson-52.html" },
            { title: "馬瑟琳的音樂與情感表達", url: "topics/adventure-time/lesson-53.html" },
            { title: "模組總結", url: "topics/adventure-time/lesson-54.html" }
          ]
        },
        {
          title: "模組 M｜人物剖析：配角群像",
          courses: [
            { title: "火焰公主：芬恩的另一段感情線", url: "topics/adventure-time/lesson-55.html" },
            { title: "棉花糖公主：喜劇擔當的另一面", url: "topics/adventure-time/lesson-56.html" },
            { title: "企鵝根特：一個充滿謎團的角色", url: "topics/adventure-time/lesson-57.html" },
            { title: "其他重要配角巡禮", url: "topics/adventure-time/lesson-58.html" },
            { title: "模組總結", url: "topics/adventure-time/lesson-59.html" }
          ]
        },
        {
          title: "模組 N｜主題與意義",
          courses: [
            { title: "成長是什麼：這部劇怎麼處理「長大」這件事", url: "topics/adventure-time/lesson-60.html" },
            { title: "死亡、失去與記憶：意外深刻的生命議題", url: "topics/adventure-time/lesson-61.html" },
            { title: "戰爭之後：末日設定如何反思現實", url: "topics/adventure-time/lesson-62.html" },
            { title: "模組總結：為什麼一部兒童卡通能感動大人", url: "topics/adventure-time/lesson-63.html" }
          ]
        },
        {
          title: "模組 O｜課程總結",
          courses: [
            { title: "全課程總結：Ooo大陸教會我們的事", url: "topics/adventure-time/lesson-64.html" }
          ]
        }
      ]
    },
    {
      id: "mythology",
      category: "mythology",
      title: "神話學全紀錄：希臘·羅馬·北歐·埃及·中國·日本六大神話體系",
      description:
        "橫跨六大文明的神話故事與人物詳解：希臘的奧林帕斯眾神與特洛伊戰爭、羅馬如何改造希臘神話打造建國起源、北歐的九界與諸神黃昏、埃及的來世信仰與法老王權、中國從盤古女媧到八仙的完整神系、日本記紀裡的天照大神，最後用比較神話學看六者共通的洪水、創世與英雄旅程母題。",
      icon: "🏺",
      url: "topics/mythology/index.html",
      modules: [
        {
          title: "模組 A｜神話總論",
          courses: [
            { title: "什麼是神話：從口傳故事到文明信仰核心", url: "topics/mythology/lesson-01.html" },
            { title: "比較神話學：不同文明的神話為什麼常常「撞名」", url: "topics/mythology/lesson-02.html" },
            { title: "這門課的讀法：六大神話體系怎麼安排", url: "topics/mythology/lesson-03.html" }
          ]
        },
        {
          title: "模組 B｜希臘神話（一）：創世與眾神的誕生",
          courses: [
            { title: "卡奧斯與蓋亞：希臘神話的創世秩序", url: "topics/mythology/lesson-04.html" },
            { title: "泰坦與奧林帕斯：克洛諾斯弒父、宙斯推翻泰坦的權力更迭", url: "topics/mythology/lesson-05.html" },
            { title: "十二主神總覽：奧林帕斯的神界秩序", url: "topics/mythology/lesson-06.html" },
            { title: "宙斯：眾神之王的權柄與風流韻事", url: "topics/mythology/lesson-07.html" },
            { title: "赫拉、波賽頓、黑帝斯：天空之外的三大權柄", url: "topics/mythology/lesson-08.html" },
            { title: "雅典娜、阿波羅、阿提米絲：智慧、光明與野性的神", url: "topics/mythology/lesson-09.html" }
          ]
        },
        {
          title: "模組 C｜希臘神話（二）：英雄傳說與特洛伊戰爭",
          courses: [
            { title: "海克力士：十二項苦役與贖罪之路", url: "topics/mythology/lesson-10.html" },
            { title: "帕修斯：蛇髮女妖美杜莎的傳說", url: "topics/mythology/lesson-11.html" },
            { title: "忒修斯與米諾陶：克里特迷宮的英雄考驗", url: "topics/mythology/lesson-12.html" },
            { title: "伊底帕斯：命運無法逃脫的悲劇", url: "topics/mythology/lesson-13.html" },
            { title: "特洛伊戰爭的起源：金蘋果與帕里斯的抉擇", url: "topics/mythology/lesson-14.html" },
            { title: "特洛伊戰爭：阿基里斯、赫克托與十年圍城", url: "topics/mythology/lesson-15.html" },
            { title: "奧德修斯的返鄉之路：《奧德賽》十年漂流", url: "topics/mythology/lesson-16.html" },
            { title: "希臘神話總結：命運、傲慢與人神關係的核心命題", url: "topics/mythology/lesson-17.html" }
          ]
        },
        {
          title: "模組 D｜羅馬神話：希臘的繼承與羅馬的自我建構",
          courses: [
            { title: "羅馬神話與希臘神話的關係：借用、改名與在地化", url: "topics/mythology/lesson-18.html" },
            { title: "羅馬眾神對照表：朱比特、朱諾、瑪爾斯與希臘諸神的異同", url: "topics/mythology/lesson-19.html" },
            { title: "埃涅阿斯：特洛伊遺民與羅馬建國的神話起點", url: "topics/mythology/lesson-20.html" },
            { title: "羅穆盧斯與雷穆斯：母狼哺育與羅馬城的建立", url: "topics/mythology/lesson-21.html" },
            { title: "雅努斯與維斯塔：羅馬獨有的神祇與信仰", url: "topics/mythology/lesson-22.html" },
            { title: "羅馬神話總結：一個帝國如何用神話打造自己的起源故事", url: "topics/mythology/lesson-23.html" }
          ]
        },
        {
          title: "模組 E｜北歐神話（一）：九界宇宙觀與眾神",
          courses: [
            { title: "世界之樹：尤克特拉希爾與北歐神話的九個世界", url: "topics/mythology/lesson-24.html" },
            { title: "奧丁：智慧、犧牲與盧恩符文的代價", url: "topics/mythology/lesson-25.html" },
            { title: "索爾：雷神之槌與巨人的世仇", url: "topics/mythology/lesson-26.html" },
            { title: "洛基：亦正亦邪的搗亂者與眾神的宿命", url: "topics/mythology/lesson-27.html" },
            { title: "芙蕾雅與芙麗嘉：北歐神話中的女神們", url: "topics/mythology/lesson-28.html" },
            { title: "女武神與英靈殿：戰死者的歸宿", url: "topics/mythology/lesson-29.html" }
          ]
        },
        {
          title: "模組 F｜北歐神話（二）：諸神的黃昏",
          courses: [
            { title: "洛基之子：芬里爾狼、耶夢加得與海爾", url: "topics/mythology/lesson-30.html" },
            { title: "巴德爾之死：洛基的陰謀與悲劇的開端", url: "topics/mythology/lesson-31.html" },
            { title: "諸神的黃昏：拉格納洛克的預言與終局之戰", url: "topics/mythology/lesson-32.html" },
            { title: "拉格納洛克之後：世界的重生", url: "topics/mythology/lesson-33.html" },
            { title: "北歐神話總結：一個「知道自己會輸」的神話體系有多特別", url: "topics/mythology/lesson-34.html" }
          ]
        },
        {
          title: "模組 G｜埃及神話：尼羅河畔的神祇與來世信仰",
          courses: [
            { title: "埃及神話的世界觀：太陽神拉與尼羅河的秩序", url: "topics/mythology/lesson-35.html" },
            { title: "創世神話：努恩、阿圖姆與埃及的多重創世版本", url: "topics/mythology/lesson-36.html" },
            { title: "歐西里斯、伊西斯與賽特：一場謀殺開啟的神話核心", url: "topics/mythology/lesson-37.html" },
            { title: "荷魯斯：為父復仇與法老王權的神聖來源", url: "topics/mythology/lesson-38.html" },
            { title: "阿努比斯與來世信仰：木乃伊、審判與正義之羽", url: "topics/mythology/lesson-39.html" },
            { title: "拉、阿蒙與阿頓：太陽神信仰的演變與阿肯那頓的宗教改革", url: "topics/mythology/lesson-40.html" },
            { title: "貝斯特與其他重要神祇：埃及神話裡的動物神系統", url: "topics/mythology/lesson-41.html" },
            { title: "埃及神話總結：神話如何撐起一整套政治與宗教制度", url: "topics/mythology/lesson-42.html" }
          ]
        },
        {
          title: "模組 H｜中國神話（一）：創世與早期神祇",
          courses: [
            { title: "盤古開天：中國神話的創世敘事", url: "topics/mythology/lesson-43.html" },
            { title: "女媧：造人、補天與中國神話裡的母性神格", url: "topics/mythology/lesson-44.html" },
            { title: "三皇五帝：從神話走向信史的過渡人物", url: "topics/mythology/lesson-45.html" },
            { title: "后羿射日與嫦娥奔月：一對神話夫妻的悲劇", url: "topics/mythology/lesson-46.html" },
            { title: "精衛填海與夸父追日：中國神話裡的意志母題", url: "topics/mythology/lesson-47.html" },
            { title: "黃帝與蚩尤：涿鹿之戰與華夏起源神話", url: "topics/mythology/lesson-48.html" }
          ]
        },
        {
          title: "模組 I｜中國神話（二）：道教神祇與民間信仰",
          courses: [
            { title: "西王母：從凶神到瑤池仙境之主的形象演變", url: "topics/mythology/lesson-49.html" },
            { title: "玉皇大帝與天庭體系：中國神話的官僚化宇宙觀", url: "topics/mythology/lesson-50.html" },
            { title: "八仙過海：八位仙人的身世與各自的法寶", url: "topics/mythology/lesson-51.html" },
            { title: "龍王與四海信仰：中國神話裡的水神體系", url: "topics/mythology/lesson-52.html" },
            { title: "城隍、灶神與土地公：貼近生活的民間信仰神祇", url: "topics/mythology/lesson-53.html" },
            { title: "中國神話總結：神話如何跟儒釋道信仰交織在一起", url: "topics/mythology/lesson-54.html" }
          ]
        },
        {
          title: "模組 J｜日本神話：記紀神話與天皇的起源",
          courses: [
            { title: "《古事記》與《日本書紀》：日本神話的兩大文本來源", url: "topics/mythology/lesson-55.html" },
            { title: "伊邪那岐與伊邪那美：國土生成與黃泉的訣別", url: "topics/mythology/lesson-56.html" },
            { title: "天照大神：天岩戶神話與皇室的太陽血統", url: "topics/mythology/lesson-57.html" },
            { title: "須佐之男：八岐大蛇與草薙劍的傳說", url: "topics/mythology/lesson-58.html" },
            { title: "大國主：國讓神話與出雲信仰", url: "topics/mythology/lesson-59.html" },
            { title: "天孫降臨：瓊瓊杵尊與天皇家系的神話起點", url: "topics/mythology/lesson-60.html" },
            { title: "日本神話總結：神話如何一路連結到日本的皇室與神社信仰", url: "topics/mythology/lesson-61.html" }
          ]
        },
        {
          title: "模組 K｜總結與比較",
          courses: [
            { title: "洪水神話比較：諾亞方舟之外，還有哪些「重來一次」的故事", url: "topics/mythology/lesson-62.html" },
            { title: "創世模式比較：從混沌到秩序的不同路徑", url: "topics/mythology/lesson-63.html" },
            { title: "英雄旅程比較：喬瑟夫·坎伯的「英雄之旅」在六大神話中的印證", url: "topics/mythology/lesson-64.html" },
            { title: "課程總結：神話為什麼直到今天依然重要", url: "topics/mythology/lesson-65.html" }
          ]
        }
      ]
    },
    {
      id: "dan-brown",
      category: "wuxia",
      title: "丹布朗小說全紀錄：符號、密碼與蘭登教授的世界",
      description:
        "從丹布朗的創作背景與寫作公式出發，逐部深度導讀《數位密碼》《天使與魔鬼》《詭恐行動》《達文西密碼》《失落的符號》《地獄》《起源》七部作品的故事設定與主題演變，再橫向剖析角色塑造、反派設計與敘事手法，誠實面對真實與虛構的爭議，最後總覽電影改編與文化影響。",
      icon: "🗝️",
      url: "topics/dan-brown/index.html",
      modules: [
        {
          title: "模組 A｜認識丹布朗：作者與創作背景",
          courses: [
            { title: "丹布朗是誰：從音樂人、教師到暢銷驚悚小說家", url: "topics/dan-brown/lesson-01.html" },
            { title: "創作起源與寫作風格：符號學、密碼與「章末鉤子」公式", url: "topics/dan-brown/lesson-02.html" },
            { title: "蘭登系列全覽：一張地圖看懂五部曲的時間軸與場景", url: "topics/dan-brown/lesson-03.html" },
            { title: "出版史：從《數位密碼》的沉寂到《達文西密碼》的全球爆紅", url: "topics/dan-brown/lesson-04.html" },
            { title: "模組總結：讀懂丹布朗小說的三個關鍵字", url: "topics/dan-brown/lesson-05.html" }
          ]
        },
        {
          title: "模組 B｜《數位密碼》：解碼機器與監控爭議",
          courses: [
            { title: "故事背景：NSA、解碼機器TRANSLTR與監控爭議的初登場", url: "topics/dan-brown/lesson-06.html" },
            { title: "蘇珊·佛萊契與大衛·貝克：雙線敘事的初次嘗試", url: "topics/dan-brown/lesson-07.html" },
            { title: "模組總結：丹布朗式懸疑公式的雛形", url: "topics/dan-brown/lesson-08.html" }
          ]
        },
        {
          title: "模組 C｜《天使與魔鬼》：符號學家的初登場",
          courses: [
            { title: "羅柏·蘭登首度登場：符號學家的角色設定", url: "topics/dan-brown/lesson-09.html" },
            { title: "梵蒂岡、光明會傳說與反物質危機", url: "topics/dan-brown/lesson-10.html" },
            { title: "宗教與科學的對立主題", url: "topics/dan-brown/lesson-11.html" },
            { title: "羅馬地標與「符號路徑」：一座城市變成解謎地圖", url: "topics/dan-brown/lesson-12.html" },
            { title: "模組總結：蘭登系列公式正式成形", url: "topics/dan-brown/lesson-13.html" }
          ]
        },
        {
          title: "模組 D｜《詭恐行動》：獨立作品裡的科學驚悚",
          courses: [
            { title: "獨立作品：政治角力、NASA與科學造假疑雲", url: "topics/dan-brown/lesson-14.html" },
            { title: "瑞秋·賽克斯頓：不靠蘭登也能撐起的女主角", url: "topics/dan-brown/lesson-15.html" },
            { title: "模組總結：與蘭登系列風格的異同", url: "topics/dan-brown/lesson-16.html" }
          ]
        },
        {
          title: "模組 E｜《達文西密碼》：引爆全球現象",
          courses: [
            { title: "羅浮宮命案：蘭登與蘇菲的第二次冒險", url: "topics/dan-brown/lesson-17.html" },
            { title: "聖杯傳說與抹大拉的馬利亞：核心懸案的設定邏輯", url: "topics/dan-brown/lesson-18.html" },
            { title: "達文西畫作與隱藏符碼：解謎章節如何推進劇情", url: "topics/dan-brown/lesson-19.html" },
            { title: "天主教會、主業會的爭議與各地抗議聲浪", url: "topics/dan-brown/lesson-20.html" },
            { title: "為什麼是這一本：暢銷現象背後的行銷與時機", url: "topics/dan-brown/lesson-21.html" },
            { title: "模組總結：一本小說如何掀起全球性的宗教辯論", url: "topics/dan-brown/lesson-22.html" }
          ]
        },
        {
          title: "模組 F｜《失落的符號》：蘭登系列的美國轉向",
          courses: [
            { title: "場景轉向美國：共濟會與華盛頓特區的符號地圖", url: "topics/dan-brown/lesson-23.html" },
            { title: "神秘學、意識科學與美國建國神話的交織", url: "topics/dan-brown/lesson-24.html" },
            { title: "彼得·索羅門與馬拉克：反派動機的心理化設計", url: "topics/dan-brown/lesson-25.html" },
            { title: "模組總結：蘭登系列的「在地化」實驗", url: "topics/dan-brown/lesson-26.html" }
          ]
        },
        {
          title: "模組 G｜《地獄》：但丁神曲與人口危機",
          courses: [
            { title: "但丁《神曲》與人口過剩危機的結合", url: "topics/dan-brown/lesson-27.html" },
            { title: "佛羅倫斯的藝術地景：從烏菲茲到韋奇奧宮", url: "topics/dan-brown/lesson-28.html" },
            { title: "柏特蘭·佐布里斯特：當反派的動機開始「有道理」", url: "topics/dan-brown/lesson-29.html" },
            { title: "模組總結：道德灰色地帶的敘事實驗", url: "topics/dan-brown/lesson-30.html" }
          ]
        },
        {
          title: "模組 H｜《起源》：AI、宗教與大哉問",
          courses: [
            { title: "人工智慧、宗教與「我們從哪裡來」的大哉問", url: "topics/dan-brown/lesson-31.html" },
            { title: "西班牙的建築與藝術場景：從古根漢到聖家堂", url: "topics/dan-brown/lesson-32.html" },
            { title: "艾德蒙·基爾許與AI角色溫斯頓：科技神諭的敘事實驗", url: "topics/dan-brown/lesson-33.html" },
            { title: "模組總結：科技與信仰衝突的當代命題", url: "topics/dan-brown/lesson-34.html" }
          ]
        },
        {
          title: "模組 I｜角色與敘事手法深度剖析",
          courses: [
            { title: "羅柏·蘭登：學者英雄的塑造與侷限", url: "topics/dan-brown/lesson-35.html" },
            { title: "女性角色群像：從蘇珊到安柏拉的類型演變", url: "topics/dan-brown/lesson-36.html" },
            { title: "反派設計：從單純惡意到意識形態驅動的轉變", url: "topics/dan-brown/lesson-37.html" },
            { title: "丹布朗的敘事公式：短章節、雙線交織與最後轉折", url: "topics/dan-brown/lesson-38.html" },
            { title: "模組總結：符號學元素如何真正驅動情節", url: "topics/dan-brown/lesson-39.html" }
          ]
        },
        {
          title: "模組 J｜真實與虛構：爭議與查證",
          courses: [
            { title: "歷史與藝術史細節的真實度爭議：學界與教會的反駁", url: "topics/dan-brown/lesson-40.html" },
            { title: "各部作品引發的實際社會迴響：官方回應與觀光效應", url: "topics/dan-brown/lesson-41.html" },
            { title: "如何區分小說的戲劇化與真實史料：讀者的查核習慣", url: "topics/dan-brown/lesson-42.html" },
            { title: "模組總結：驚悚小說與史實查核之間的分寸", url: "topics/dan-brown/lesson-43.html" }
          ]
        },
        {
          title: "模組 K｜文化影響與改編",
          courses: [
            { title: "電影改編：湯姆漢克斯與朗霍華的蘭登三部曲", url: "topics/dan-brown/lesson-44.html" },
            { title: "對「符號驚悚」類型小說的開創與後續影響", url: "topics/dan-brown/lesson-45.html" },
            { title: "全球熱潮與各地取景地的觀光效應", url: "topics/dan-brown/lesson-46.html" },
            { title: "模組總結：一個類型小說門派的誕生", url: "topics/dan-brown/lesson-47.html" }
          ]
        },
        {
          title: "模組 L｜課程總結",
          courses: [
            { title: "課程總結：從《數位密碼》到《起源》的完整旅程", url: "topics/dan-brown/lesson-48.html" }
          ]
        }
      ]
    },
    {
      id: "star-wars",
      category: "fantasy",
      title: "星際大戰全紀錄：從創作背景到絕地與西斯的傳承",
      description:
        "從喬治盧卡斯的創作背景出發，依序深度導讀原初、前傳、後傳三部曲與衍生電影劇集，再橫向剖析原力與絕地哲學、天行者家族的三代恩怨、核心角色塑造與世界觀設定，最後總覽特效革命、周邊產業與粉絲文化帶來的深遠影響。",
      icon: "🌌",
      url: "topics/star-wars/index.html",
      modules: [
        {
          title: "模組 A｜認識星際大戰：喬治盧卡斯與創作背景",
          courses: [
            { title: "喬治盧卡斯是誰：從獨立電影人到打造一個銀河系", url: "topics/star-wars/lesson-01.html" },
            { title: "創作起源：黑澤明、坎伯「英雄旅程」與太空歌劇的融合", url: "topics/star-wars/lesson-02.html" },
            { title: "九部曲全覽：三個三部曲的拍攝順序與故事時間軸的落差", url: "topics/star-wars/lesson-03.html" },
            { title: "出版與發行史：從1977年的獨立奇蹟到迪士尼併購後的擴張", url: "topics/star-wars/lesson-04.html" },
            { title: "模組總結：一張地圖看懂正史、外傳與衍生作品的關係", url: "topics/star-wars/lesson-05.html" }
          ]
        },
        {
          title: "模組 B｜原初三部曲：一個傳奇的誕生（4-6集）",
          courses: [
            { title: "《曙光乍現》：路克·天行者的英雄旅程起點", url: "topics/star-wars/lesson-06.html" },
            { title: "死星、原力與絕地騎士：世界觀基礎設定的建立", url: "topics/star-wars/lesson-07.html" },
            { title: "《帝國大反擊》：黑暗降臨與那句經典的身世轉折", url: "topics/star-wars/lesson-08.html" },
            { title: "尤達與絕地訓練：智慧導師原型的塑造", url: "topics/star-wars/lesson-09.html" },
            { title: "《絕地大反攻》：救贖、犧牲與帝國的終結", url: "topics/star-wars/lesson-10.html" },
            { title: "模組總結：為什麼原初三部曲奠定了現代大片的敘事典範", url: "topics/star-wars/lesson-11.html" }
          ]
        },
        {
          title: "模組 C｜前傳三部曲：英雄如何墮落成惡魔（1-3集）",
          courses: [
            { title: "《幽靈威脅》：貿易同盟、原力預言與安納金的出場", url: "topics/star-wars/lesson-12.html" },
            { title: "《複製人全面進攻》：禁忌之戀與複製人軍團的伏筆", url: "topics/star-wars/lesson-13.html" },
            { title: "《西斯大帝的復仇》：安納金如何一步步走向黑暗西斯大帝之路", url: "topics/star-wars/lesson-14.html" },
            { title: "政治操弄與共和國的崩壞：帕爾帕丁的長期布局", url: "topics/star-wars/lesson-15.html" },
            { title: "模組總結：一部悲劇三部曲的爭議與重新評價", url: "topics/star-wars/lesson-16.html" }
          ]
        },
        {
          title: "模組 D｜後傳三部曲：新世代的傳承與爭議（7-9集）",
          courses: [
            { title: "《原力覺醒》：芮的身世之謎與第一軍團的崛起", url: "topics/star-wars/lesson-17.html" },
            { title: "《最後的絕地武士》：對「英雄旅程」公式的顛覆與粉絲反彈", url: "topics/star-wars/lesson-18.html" },
            { title: "《天行者的崛起》：三部曲收官的爭議與敘事調整", url: "topics/star-wars/lesson-19.html" },
            { title: "為什麼後傳三部曲的評價如此兩極", url: "topics/star-wars/lesson-20.html" },
            { title: "模組總結：一個系列如何面對創作方向不一致的挑戰", url: "topics/star-wars/lesson-21.html" }
          ]
        },
        {
          title: "模組 E｜衍生電影與劇集：擴張中的銀河系",
          courses: [
            { title: "外傳電影：《俠盜一號》與《韓索羅》的定位與敘事實驗", url: "topics/star-wars/lesson-22.html" },
            { title: "《曼達洛人》：如何重新贏回觀眾信任的關鍵作品", url: "topics/star-wars/lesson-23.html" },
            { title: "《歐比王肯諾比》《安道爾》等劇集：角色前傳與政治驚悚的新嘗試", url: "topics/star-wars/lesson-24.html" },
            { title: "動畫系列：《複製人之戰》與《叛亂》的正史地位", url: "topics/star-wars/lesson-25.html" },
            { title: "模組總結：串流時代的星際大戰擴張策略", url: "topics/star-wars/lesson-26.html" }
          ]
        },
        {
          title: "模組 F｜原力與絕地哲學",
          courses: [
            { title: "原力是什麼：光明面、黑暗面與平衡的概念設計", url: "topics/star-wars/lesson-27.html" },
            { title: "絕地武士團：紀律、無執念與制度性的盲點", url: "topics/star-wars/lesson-28.html" },
            { title: "西斯教條：兩人法則與權力慾望的哲學", url: "topics/star-wars/lesson-29.html" },
            { title: "原力使用者的能力系統：從念力到預知的設定演變", url: "topics/star-wars/lesson-30.html" },
            { title: "模組總結：一套融合東方哲學與西方英雄敘事的原創信仰系統", url: "topics/star-wars/lesson-31.html" }
          ]
        },
        {
          title: "模組 G｜天行者家族：貫穿九部曲的血脈",
          courses: [
            { title: "安納金·天行者：從天選之子到黑武士的完整弧線", url: "topics/star-wars/lesson-32.html" },
            { title: "路克·天行者：拒絕黑暗面的第二代英雄", url: "topics/star-wars/lesson-33.html" },
            { title: "莉亞公主／歐嘉納：反抗軍領袖與被隱藏的身世", url: "topics/star-wars/lesson-34.html" },
            { title: "韓·索羅與家族的羈絆：一個外人如何成為天行者的一部分", url: "topics/star-wars/lesson-35.html" },
            { title: "凱羅·忍／班·索羅：第三代的墮落與救贖", url: "topics/star-wars/lesson-36.html" },
            { title: "模組總結：三代人的宿命與選擇", url: "topics/star-wars/lesson-37.html" }
          ]
        },
        {
          title: "模組 H｜其他核心角色深度剖析",
          courses: [
            { title: "尤達與歐比王：兩種絕地導師典型的比較", url: "topics/star-wars/lesson-38.html" },
            { title: "帕爾帕丁：系列史上最有耐心的反派布局", url: "topics/star-wars/lesson-39.html" },
            { title: "達斯維達：從安納金到黑武士，聲音、面具與人物形象的塑造", url: "topics/star-wars/lesson-40.html" },
            { title: "R2-D2與C-3PO：貫穿全系列的雙人喜劇與敘事功能", url: "topics/star-wars/lesson-41.html" },
            { title: "藍多、丘巴卡與反抗軍配角群像", url: "topics/star-wars/lesson-42.html" },
            { title: "芮、芬恩與波·戴姆龍：後傳三部曲的新世代主角", url: "topics/star-wars/lesson-43.html" },
            { title: "模組總結：星際大戰角色塑造的共通手法", url: "topics/star-wars/lesson-44.html" }
          ]
        },
        {
          title: "模組 I｜世界觀與科技設定",
          courses: [
            { title: "銀河共和國到銀河帝國：政治體制的興衰", url: "topics/star-wars/lesson-45.html" },
            { title: "星際艦隊與武器系統：死星、鈦戰機與千年鷹號", url: "topics/star-wars/lesson-46.html" },
            { title: "克隆人軍團與風暴兵：士兵身分的設計演變", url: "topics/star-wars/lesson-47.html" },
            { title: "外星種族圖鑑：從伍基人到赫特人的世界觀豐富度", url: "topics/star-wars/lesson-48.html" },
            { title: "模組總結：一個橫跨政治、軍事、種族的完整銀河系統", url: "topics/star-wars/lesson-49.html" }
          ]
        },
        {
          title: "模組 J｜文化影響與產業現象",
          courses: [
            { title: "特效革命：工業光魔如何改變電影特效產業", url: "topics/star-wars/lesson-50.html" },
            { title: "周邊產業：玩具、主題樂園與有史以來最成功的授權模式", url: "topics/star-wars/lesson-51.html" },
            { title: "粉絲文化：同人創作、爭議與「正史」設定的多次重編", url: "topics/star-wars/lesson-52.html" },
            { title: "對後續科幻／太空歌劇作品的深遠影響", url: "topics/star-wars/lesson-53.html" },
            { title: "模組總結：一個系列如何變成一種全球性的流行文化語言", url: "topics/star-wars/lesson-54.html" }
          ]
        },
        {
          title: "模組 K｜課程總結",
          courses: [
            { title: "課程總結：從1977年的獨立奇蹟到跨媒體銀河帝國的完整旅程", url: "topics/star-wars/lesson-55.html" }
          ]
        }
      ]
    },
    {
      id: "chinese-history",
      category: "history",
      title: "中國歷史全紀錄：從神話到當代",
      description:
        "從神話傳說時代出發，依序深度導讀夏商周、春秋戰國、歷代大一統與分裂王朝，一路走到近代的內憂外患、民國的動盪與中華人民共和國的建國與改革開放，並橫向比較中央集權、科舉制度、儒家思想與統一分裂週期等貫穿全史的主題。",
      icon: "🐉",
      url: "topics/chinese-history/index.html",
      modules: [
        {
          title: "模組 A｜導論：如何研究中國歷史",
          courses: [
            { title: "信史與傳說：考古學、甲骨文與「證據等級」的概念", url: "topics/chinese-history/lesson-01.html" },
            { title: "朝代循環史觀：一個好用卻也容易誤導的框架", url: "topics/chinese-history/lesson-02.html" },
            { title: "這門課的時間軸地圖：從三皇五帝到21世紀", url: "topics/chinese-history/lesson-03.html" }
          ]
        },
        {
          title: "模組 B｜神話與傳說時代：三皇五帝",
          courses: [
            { title: "盤古開天、女媧補天：創世神話與早期宇宙觀", url: "topics/chinese-history/lesson-04.html" },
            { title: "三皇傳說：燧人氏、伏羲氏、神農氏的文化英雄敘事", url: "topics/chinese-history/lesson-05.html" },
            { title: "五帝傳說：黃帝、堯、舜與「禪讓」政治理想的建構", url: "topics/chinese-history/lesson-06.html" },
            { title: "大禹治水與夏朝的傳說起源：神話如何過渡到信史", url: "topics/chinese-history/lesson-07.html" }
          ]
        },
        {
          title: "模組 C｜夏商：信史的開端",
          courses: [
            { title: "夏朝的考古爭議：二里頭文化與「最早的中國」", url: "topics/chinese-history/lesson-08.html" },
            { title: "商朝：甲骨文、占卜與王權的宗教基礎", url: "topics/chinese-history/lesson-09.html" },
            { title: "商朝的滅亡：牧野之戰與「天命」觀念的誕生", url: "topics/chinese-history/lesson-10.html" }
          ]
        },
        {
          title: "模組 D｜西周：封建與禮樂",
          courses: [
            { title: "封建制度：分封諸侯與宗法制的運作邏輯", url: "topics/chinese-history/lesson-11.html" },
            { title: "禮樂文明：周公制禮作樂與儒家日後的理想投射", url: "topics/chinese-history/lesson-12.html" },
            { title: "西周的衰亡：烽火戲諸侯傳說與平王東遷", url: "topics/chinese-history/lesson-13.html" }
          ]
        },
        {
          title: "模組 E｜春秋戰國：禮崩樂壞與百家爭鳴",
          courses: [
            { title: "春秋五霸：尊王攘夷與舊秩序的最後掙扎", url: "topics/chinese-history/lesson-14.html" },
            { title: "孔子與儒家：仁與禮的思想體系", url: "topics/chinese-history/lesson-15.html" },
            { title: "老莊與道家：無為而治的另一種政治想像", url: "topics/chinese-history/lesson-16.html" },
            { title: "法家與變法：商鞅變法如何為秦國奠基", url: "topics/chinese-history/lesson-17.html" },
            { title: "墨家、名家與其他諸子：百家爭鳴的思想盛況", url: "topics/chinese-history/lesson-18.html" },
            { title: "戰國七雄：合縱連橫與統一前夜的軍事外交", url: "topics/chinese-history/lesson-19.html" }
          ]
        },
        {
          title: "模組 F｜秦：一統與速亡",
          courses: [
            { title: "秦始皇統一六國：郡縣制取代封建制的關鍵轉折", url: "topics/chinese-history/lesson-20.html" },
            { title: "書同文、車同軌：中央集權的制度建設", url: "topics/chinese-history/lesson-21.html" },
            { title: "焚書坑儒與嚴刑峻法：高壓統治的代價", url: "topics/chinese-history/lesson-22.html" },
            { title: "秦朝速亡：陳勝吳廣起義與楚漢相爭的伏筆", url: "topics/chinese-history/lesson-23.html" }
          ]
        },
        {
          title: "模組 G｜漢：帝國定型",
          courses: [
            { title: "楚漢相爭：劉邦與項羽的性格對照", url: "topics/chinese-history/lesson-24.html" },
            { title: "文景之治：休養生息與「無為而治」的實踐", url: "topics/chinese-history/lesson-25.html" },
            { title: "漢武帝：獨尊儒術、開拓疆域與中央集權的強化", url: "topics/chinese-history/lesson-26.html" },
            { title: "絲路的開通：張騫通西域與東西方交流的起點", url: "topics/chinese-history/lesson-27.html" },
            { title: "王莽篡漢與東漢的建立：帝國中期的制度危機", url: "topics/chinese-history/lesson-28.html" }
          ]
        },
        {
          title: "模組 H｜三國兩晉南北朝：分裂與融合",
          courses: [
            { title: "黃巾之亂與群雄並起：東漢崩壞的開端", url: "topics/chinese-history/lesson-29.html" },
            { title: "三國鼎立：曹操、劉備、孫權的戰略格局", url: "topics/chinese-history/lesson-30.html" },
            { title: "西晉短暫統一與八王之亂：內耗如何招致外患", url: "topics/chinese-history/lesson-31.html" },
            { title: "五胡十六國：民族大遷徙與衝突", url: "topics/chinese-history/lesson-32.html" },
            { title: "南北朝對峙：門閥政治與佛教的興盛", url: "topics/chinese-history/lesson-33.html" },
            { title: "孝文帝漢化改革：民族融合的關鍵案例", url: "topics/chinese-history/lesson-34.html" }
          ]
        },
        {
          title: "模組 I｜隋唐：盛世與轉折",
          courses: [
            { title: "隋朝統一：科舉制度與大運河的長遠影響", url: "topics/chinese-history/lesson-35.html" },
            { title: "隋朝速亡：與秦朝的相似模式比較", url: "topics/chinese-history/lesson-36.html" },
            { title: "貞觀之治：唐太宗與「以史為鑑」的治國理念", url: "topics/chinese-history/lesson-37.html" },
            { title: "武則天：中國歷史上唯一的女皇帝", url: "topics/chinese-history/lesson-38.html" },
            { title: "開元盛世：唐玄宗前期的巔峰與轉折", url: "topics/chinese-history/lesson-39.html" },
            { title: "安史之亂：盛世崩壞的轉捩點", url: "topics/chinese-history/lesson-40.html" },
            { title: "唐朝後期：藩鎮割據與宦官專權", url: "topics/chinese-history/lesson-41.html" }
          ]
        },
        {
          title: "模組 J｜宋（含五代）：文治巔峰與積弱",
          courses: [
            { title: "五代十國：唐末藩鎮割據的延續與亂局", url: "topics/chinese-history/lesson-42.html" },
            { title: "陳橋兵變與杯酒釋兵權：宋朝重文抑武的立國基礎", url: "topics/chinese-history/lesson-43.html" },
            { title: "宋朝的經濟與文化：商業革命與科技發展的高峰", url: "topics/chinese-history/lesson-44.html" },
            { title: "王安石變法：改革理想與政治鬥爭", url: "topics/chinese-history/lesson-45.html" },
            { title: "積弱的軍事：與遼、西夏、金的長期對峙", url: "topics/chinese-history/lesson-46.html" }
          ]
        },
        {
          title: "模組 K｜元：蒙古治下的中國",
          courses: [
            { title: "蒙古帝國的崛起：成吉思汗與橫跨歐亞的征服", url: "topics/chinese-history/lesson-47.html" },
            { title: "忽必烈建元：草原帝國如何統治中原", url: "topics/chinese-history/lesson-48.html" },
            { title: "四等人制與元朝的統治矛盾", url: "topics/chinese-history/lesson-49.html" },
            { title: "元朝速亡：紅巾軍起義與朱元璋的崛起", url: "topics/chinese-history/lesson-50.html" }
          ]
        },
        {
          title: "模組 L｜明：集權高峰",
          courses: [
            { title: "朱元璋建明：廢除宰相與皇權集中的極致", url: "topics/chinese-history/lesson-51.html" },
            { title: "靖難之役與永樂盛世：鄭和下西洋的世界視野", url: "topics/chinese-history/lesson-52.html" },
            { title: "內閣制度與宦官政治：皇權集中後的制度變形", url: "topics/chinese-history/lesson-53.html" },
            { title: "倭寇與海禁：明朝的海洋政策困境", url: "topics/chinese-history/lesson-54.html" },
            { title: "明朝中後期：張居正改革與黨爭內耗", url: "topics/chinese-history/lesson-55.html" }
          ]
        },
        {
          title: "模組 M｜清：盛世到衰亡",
          courses: [
            { title: "滿洲崛起與清軍入關：明清易代的關鍵", url: "topics/chinese-history/lesson-56.html" },
            { title: "康雍乾盛世：疆域擴張與文字獄的雙面", url: "topics/chinese-history/lesson-57.html" },
            { title: "閉關鎖國：對外政策如何錯失時代轉型", url: "topics/chinese-history/lesson-58.html" },
            { title: "人口壓力與內部危機：盛世表象下的隱憂", url: "topics/chinese-history/lesson-59.html" },
            { title: "白蓮教、太平天國：清朝中期的內部動亂", url: "topics/chinese-history/lesson-60.html" }
          ]
        },
        {
          title: "模組 N｜近代：鴉片戰爭到帝制終結",
          courses: [
            { title: "鴉片戰爭：中西衝突與不平等條約的開端", url: "topics/chinese-history/lesson-61.html" },
            { title: "太平天國與洋務運動：內憂外患下的自強嘗試", url: "topics/chinese-history/lesson-62.html" },
            { title: "甲午戰爭與戊戌變法：東亞秩序的翻轉與改革挫敗", url: "topics/chinese-history/lesson-63.html" },
            { title: "義和團與八國聯軍：排外情緒與帝國的最後屈辱", url: "topics/chinese-history/lesson-64.html" },
            { title: "辛亥革命：帝制終結與共和的誕生", url: "topics/chinese-history/lesson-65.html" }
          ]
        },
        {
          title: "模組 O｜民國：軍閥、抗戰與內戰",
          courses: [
            { title: "北洋政府與軍閥割據：共和初年的混亂", url: "topics/chinese-history/lesson-66.html" },
            { title: "五四運動與新文化運動：思想啟蒙的浪潮", url: "topics/chinese-history/lesson-67.html" },
            { title: "國共合作與分裂：北伐統一與清黨", url: "topics/chinese-history/lesson-68.html" },
            { title: "抗日戰爭：從九一八到八年全面抗戰", url: "topics/chinese-history/lesson-69.html" },
            { title: "國共內戰：1949年之前的最後對決", url: "topics/chinese-history/lesson-70.html" }
          ]
        },
        {
          title: "模組 P｜中華人民共和國前期：建國到改革開放",
          courses: [
            { title: "1949年建國：新政權的初期建設", url: "topics/chinese-history/lesson-71.html" },
            { title: "土地改革與計畫經濟：早期的社會改造", url: "topics/chinese-history/lesson-72.html" },
            { title: "大躍進與三年困難時期：政策失誤的教訓", url: "topics/chinese-history/lesson-73.html" },
            { title: "文化大革命：十年動盪的成因與影響", url: "topics/chinese-history/lesson-74.html" }
          ]
        },
        {
          title: "模組 Q｜當代中國：改革開放至今",
          courses: [
            { title: "1978年改革開放：鄧小平與經濟轉型的起點", url: "topics/chinese-history/lesson-75.html" },
            { title: "經濟崛起：從計畫經濟到「世界工廠」", url: "topics/chinese-history/lesson-76.html" },
            { title: "21世紀的中國：全球化下的機遇與挑戰", url: "topics/chinese-history/lesson-77.html" }
          ]
        },
        {
          title: "模組 R｜橫向專題：制度、經濟與思想文化的貫穿觀察",
          courses: [
            { title: "中央集權的演變：從封建到郡縣、再到現代國家", url: "topics/chinese-history/lesson-78.html" },
            { title: "科舉制度千年史：選才制度如何形塑社會流動", url: "topics/chinese-history/lesson-79.html" },
            { title: "儒家思想的興衰起伏：從官方意識形態到近代反思", url: "topics/chinese-history/lesson-80.html" },
            { title: "中國歷史上的統一與分裂週期：一個長時段的觀察", url: "topics/chinese-history/lesson-81.html" }
          ]
        },
        {
          title: "模組 S｜課程總結",
          courses: [
            { title: "課程總結：從神話創世到當代中國的完整旅程", url: "topics/chinese-history/lesson-82.html" }
          ]
        }
      ]
    },
    {
      id: "wwi",
      category: "history",
      title: "第一次世界大戰全紀錄：從火藥桶到停戰協定",
      description:
        "從民族主義、軍備競賽與同盟體系的戰前氛圍出發，逐一深讀薩拉熱窩事件、西線壕溝戰、東線戰事與其他戰場的關鍵戰役，接續俄國革命、美國參戰到百日攻勢的戰爭終局，並剖析戰爭對社會的衝擊，以及巴黎和會如何為二十年後的另一場戰爭埋下伏筆。",
      icon: "🪖",
      url: "topics/wwi/index.html",
      modules: [
        {
          title: "模組 A｜戰爭的遠因：一個火藥桶是怎麼堆起來的",
          courses: [
            { title: "民族主義、帝國主義與社會達爾文主義：戰前歐洲的思想氣候", url: "topics/wwi/lesson-01.html" },
            { title: "軍備競賽：無畏艦競賽與總體戰思維的成形", url: "topics/wwi/lesson-02.html" },
            { title: "兩大陣營的形成：三國同盟與三國協約", url: "topics/wwi/lesson-03.html" },
            { title: "「歐洲病夫」的衰落：鄂圖曼帝國與巴爾幹半島的權力真空", url: "topics/wwi/lesson-04.html" },
            { title: "兩次巴爾幹戰爭：戰前的預演", url: "topics/wwi/lesson-05.html" }
          ]
        },
        {
          title: "模組 B｜引爆點：從薩拉熱窩到全面開戰",
          courses: [
            { title: "薩拉熱窩事件：斐迪南大公夫婦遇刺的經過", url: "topics/wwi/lesson-06.html" },
            { title: "七月危機：一封最後通牒如何引發連鎖反應", url: "topics/wwi/lesson-07.html" },
            { title: "同盟義務的骨牌效應：外交失控的深層原因", url: "topics/wwi/lesson-08.html" },
            { title: "施里芬計畫：德國的兩線作戰賭注", url: "topics/wwi/lesson-09.html" },
            { title: "「聖誕節前結束戰爭」：各國開戰初期的樂觀誤判", url: "topics/wwi/lesson-10.html" }
          ]
        },
        {
          title: "模組 C｜西線：壕溝裡的絞肉機",
          courses: [
            { title: "馬恩河戰役：施里芬計畫的破產與陣地戰的開端", url: "topics/wwi/lesson-11.html" },
            { title: "壕溝戰的形成：鐵絲網、機槍與無人地帶", url: "topics/wwi/lesson-12.html" },
            { title: "凡爾登戰役：「讓法國把血流盡」的消耗戰略", url: "topics/wwi/lesson-13.html" },
            { title: "索姆河戰役：史上最血腥的一天與坦克的初登場", url: "topics/wwi/lesson-14.html" },
            { title: "帕森達勒（第三次伊珀爾戰役）：泥沼中的僵局", url: "topics/wwi/lesson-15.html" },
            { title: "新式武器：毒氣、飛機、坦克如何改變戰爭型態", url: "topics/wwi/lesson-16.html" }
          ]
        },
        {
          title: "模組 D｜東線與其他戰場",
          courses: [
            { title: "坦能堡戰役：興登堡與魯登道夫的崛起", url: "topics/wwi/lesson-17.html" },
            { title: "布魯西洛夫攻勢：俄軍最後的高光時刻", url: "topics/wwi/lesson-18.html" },
            { title: "加里波利之戰：邱吉爾的賭注與澳紐軍團的犧牲", url: "topics/wwi/lesson-19.html" },
            { title: "中東戰場：阿拉伯起義與鄂圖曼帝國的瓦解", url: "topics/wwi/lesson-20.html" },
            { title: "日德蘭海戰與無限制潛艇戰：海上的角力", url: "topics/wwi/lesson-21.html" }
          ]
        },
        {
          title: "模組 E｜俄國革命與東線的終結",
          courses: [
            { title: "沙俄的崩潰：戰爭壓力如何催化二月革命", url: "topics/wwi/lesson-22.html" },
            { title: "十月革命與布爾什維克奪權", url: "topics/wwi/lesson-23.html" },
            { title: "布列斯特-立陶夫斯克條約：俄國退出戰爭的代價", url: "topics/wwi/lesson-24.html" }
          ]
        },
        {
          title: "模組 F｜美國參戰與戰爭終結",
          courses: [
            { title: "盧西塔尼亞號事件與美國中立立場的動搖", url: "topics/wwi/lesson-25.html" },
            { title: "齊默爾曼電報：壓垮中立的最後一根稻草", url: "topics/wwi/lesson-26.html" },
            { title: "美國參戰對兵力與物資的實質影響", url: "topics/wwi/lesson-27.html" },
            { title: "魯登道夫攻勢：德國的最後豪賭", url: "topics/wwi/lesson-28.html" },
            { title: "百日攻勢：同盟國陣營的骨牌式崩潰", url: "topics/wwi/lesson-29.html" },
            { title: "1918年11月11日：停戰協定的簽署", url: "topics/wwi/lesson-30.html" }
          ]
        },
        {
          title: "模組 G｜這場戰爭如何改變了世界與人",
          courses: [
            { title: "壕溝士兵的日常：戰壕熱、砲彈休克與戰爭創傷", url: "topics/wwi/lesson-31.html" },
            { title: "傷亡統計與「迷惘的一代」", url: "topics/wwi/lesson-32.html" },
            { title: "女性角色的轉變：後方生產動員與戰後參政權", url: "topics/wwi/lesson-33.html" },
            { title: "1918年西班牙流感：戰爭陰影下的全球大流行", url: "topics/wwi/lesson-34.html" }
          ]
        },
        {
          title: "模組 H｜巴黎和會與埋下下一場戰爭的種子",
          courses: [
            { title: "巴黎和會：三巨頭的角力與理想主義的侷限", url: "topics/wwi/lesson-35.html" },
            { title: "凡爾賽條約：戰爭責任條款與鉅額賠款", url: "topics/wwi/lesson-36.html" },
            { title: "民族自決原則：新國家的誕生與遺留問題", url: "topics/wwi/lesson-37.html" },
            { title: "國際聯盟的成立與結構性侷限", url: "topics/wwi/lesson-38.html" },
            { title: "模組總結：一份和約如何為二十年後的戰爭埋下伏筆", url: "topics/wwi/lesson-39.html" }
          ]
        },
        {
          title: "模組 I｜課程總結",
          courses: [
            { title: "課程總結：從火藥桶到停戰協定的完整旅程", url: "topics/wwi/lesson-40.html" }
          ]
        }
      ]
    },
    {
      id: "wwii",
      category: "history",
      title: "第二次世界大戰全紀錄：從凡爾賽的裂痕到廣島的閃光",
      description:
        "從凡爾賽條約留下的裂痕、經濟大蕭條與法西斯崛起出發，依序深讀歐洲閃電戰、東線大戰、北非地中海戰場、太平洋戰爭與中國戰場的關鍵戰役，接續盟軍反攻、原子彈與終戰，並正視猶太人大屠殺等人道災難，最後檢視戰後清算與新秩序的誕生。",
      icon: "💣",
      url: "topics/wwii/index.html",
      modules: [
        {
          title: "模組 A｜戰爭的遠因：從凡爾賽到法西斯崛起",
          courses: [
            { title: "凡爾賽條約的遺產：德國的屈辱感與經濟崩潰", url: "topics/wwii/lesson-01.html" },
            { title: "惡性通膨與經濟大蕭條：極端主義滋長的土壤", url: "topics/wwii/lesson-02.html" },
            { title: "義大利法西斯：墨索里尼與極權統治的原型", url: "topics/wwii/lesson-03.html" },
            { title: "納粹的崛起：希特勒、啤酒館政變與國會縱火案", url: "topics/wwii/lesson-04.html" },
            { title: "日本軍國主義：從大正民主到軍部專政", url: "topics/wwii/lesson-05.html" },
            { title: "綏靖政策：英法為何一再退讓", url: "topics/wwii/lesson-06.html" }
          ]
        },
        {
          title: "模組 B｜歐洲戰事的序幕",
          courses: [
            { title: "德國的擴張：萊茵蘭進駐、奧地利合併、蘇台德區", url: "topics/wwii/lesson-07.html" },
            { title: "慕尼黑協定：「我們這個時代的和平」", url: "topics/wwii/lesson-08.html" },
            { title: "德蘇互不侵犯條約：意識形態對手的權宜聯手", url: "topics/wwii/lesson-09.html" },
            { title: "閃擊波蘭：1939年9月的開戰", url: "topics/wwii/lesson-10.html" }
          ]
        },
        {
          title: "模組 C｜閃電戰的巔峰：1939-1941年西歐",
          courses: [
            { title: "假戰與冬季戰爭：蘇聯入侵芬蘭", url: "topics/wwii/lesson-11.html" },
            { title: "閃擊西歐：荷比盧與法國的迅速崩潰", url: "topics/wwii/lesson-12.html" },
            { title: "敦克爾克大撤退", url: "topics/wwii/lesson-13.html" },
            { title: "不列顛戰役：英國的空中防禦戰", url: "topics/wwii/lesson-14.html" },
            { title: "大西洋海戰：狼群戰術與護航體系", url: "topics/wwii/lesson-15.html" }
          ]
        },
        {
          title: "模組 D｜東線：史上最血腥的戰場",
          courses: [
            { title: "巴巴羅薩行動：德國入侵蘇聯的豪賭", url: "topics/wwii/lesson-16.html" },
            { title: "莫斯科保衛戰：閃擊戰神話的第一次破滅", url: "topics/wwii/lesson-17.html" },
            { title: "史達林格勒戰役：轉捩點的巷戰絞肉機", url: "topics/wwii/lesson-18.html" },
            { title: "庫斯克會戰：史上最大規模的坦克會戰", url: "topics/wwii/lesson-19.html" },
            { title: "蘇軍反攻：從巴格拉基昂行動到柏林戰役", url: "topics/wwii/lesson-20.html" }
          ]
        },
        {
          title: "模組 E｜北非與地中海戰場",
          courses: [
            { title: "沙漠之狐：隆美爾與北非拉鋸戰", url: "topics/wwii/lesson-21.html" },
            { title: "阿拉曼戰役：北非戰局的轉折", url: "topics/wwii/lesson-22.html" },
            { title: "西西里島登陸與義大利投降", url: "topics/wwii/lesson-23.html" }
          ]
        },
        {
          title: "模組 F｜太平洋戰爭的爆發",
          courses: [
            { title: "日本的南進政策與資源封鎖", url: "topics/wwii/lesson-24.html" },
            { title: "珍珠港事變：奇襲與美國參戰", url: "topics/wwii/lesson-25.html" },
            { title: "日軍初期的閃電擴張：東南亞與太平洋島鏈", url: "topics/wwii/lesson-26.html" },
            { title: "中途島海戰：太平洋戰爭的轉捩點", url: "topics/wwii/lesson-27.html" },
            { title: "瓜達卡納爾島戰役：消耗戰的開端", url: "topics/wwii/lesson-28.html" }
          ]
        },
        {
          title: "模組 G｜中國戰場與亞洲戰事",
          courses: [
            { title: "中日戰爭與二戰的交會：從盧溝橋到珍珠港", url: "topics/wwii/lesson-29.html" },
            { title: "中緬印戰場與駝峰航線", url: "topics/wwii/lesson-30.html" },
            { title: "東南亞的日軍占領與抵抗運動", url: "topics/wwii/lesson-31.html" }
          ]
        },
        {
          title: "模組 H｜歐洲戰場的反攻",
          courses: [
            { title: "諾曼第登陸：大君主作戰的規劃與執行", url: "topics/wwii/lesson-32.html" },
            { title: "解放法國：從諾曼第到巴黎光復", url: "topics/wwii/lesson-33.html" },
            { title: "突出部之役：希特勒最後的西線反撲", url: "topics/wwii/lesson-34.html" },
            { title: "雅爾達會議：戰後秩序的預先劃分", url: "topics/wwii/lesson-35.html" },
            { title: "柏林戰役與希特勒之死：第三帝國的終結", url: "topics/wwii/lesson-36.html" }
          ]
        },
        {
          title: "模組 I｜太平洋戰場的島嶼跳躍",
          courses: [
            { title: "跳島戰術：麥克阿瑟與尼米茲的戰略分歧", url: "topics/wwii/lesson-37.html" },
            { title: "塞班島、關島：馬里亞納群島爭奪戰", url: "topics/wwii/lesson-38.html" },
            { title: "雷伊泰灣海戰：史上最大規模海戰", url: "topics/wwii/lesson-39.html" },
            { title: "硫磺島戰役：折缽山上的旗幟", url: "topics/wwii/lesson-40.html" },
            { title: "沖繩戰役：本土決戰的預演與神風特攻", url: "topics/wwii/lesson-41.html" }
          ]
        },
        {
          title: "模組 J｜大屠殺與戰爭中的人道災難",
          courses: [
            { title: "猶太人大屠殺：從紐倫堡法案到最終解決方案", url: "topics/wwii/lesson-42.html" },
            { title: "集中營體系：奧斯威辛與滅絕營的運作", url: "topics/wwii/lesson-43.html" },
            { title: "其他受害群體：羅姆人、身心障礙者、政治犯", url: "topics/wwii/lesson-44.html" },
            { title: "亞洲戰場的戰爭暴行與戰後究責爭議", url: "topics/wwii/lesson-45.html" },
            { title: "戰爭中的平民苦難：轟炸、圍城與難民潮", url: "topics/wwii/lesson-46.html" }
          ]
        },
        {
          title: "模組 K｜原子彈與戰爭終結",
          courses: [
            { title: "曼哈頓計畫：原子彈的研發競賽", url: "topics/wwii/lesson-47.html" },
            { title: "廣島與長崎：原子彈的使用與爭議", url: "topics/wwii/lesson-48.html" },
            { title: "日本投降：終戰詔書與麥克阿瑟受降", url: "topics/wwii/lesson-49.html" },
            { title: "模組總結：科技如何終結了人類史上最慘烈的戰爭", url: "topics/wwii/lesson-50.html" }
          ]
        },
        {
          title: "模組 L｜戰後清算與新秩序的誕生",
          courses: [
            { title: "紐倫堡大審與東京審判：戰爭罪責的司法清算", url: "topics/wwii/lesson-51.html" },
            { title: "聯合國的成立：從國際聯盟的失敗中學到的教訓", url: "topics/wwii/lesson-52.html" },
            { title: "雅爾達體系與冷戰的序幕", url: "topics/wwii/lesson-53.html" }
          ]
        },
        {
          title: "模組 M｜課程總結",
          courses: [
            { title: "課程總結：從凡爾賽的裂痕到廣島閃光的完整旅程", url: "topics/wwii/lesson-54.html" }
          ]
        }
      ]
    },
    {
      id: "attack-on-titan",
      category: "anime",
      title: "進擊的巨人全解：從高牆到地鳴的一百三十九話",
      description:
        "以漫畫 139 話為主體，逐層拆解《進擊的巨人》：三道牆的規格與階級設計、純潔巨人與九大巨人的完整設定、道路與始祖尤米爾的兩千年、艾爾迪亞與馬萊的互為加害史、立體機動裝置與雷槍的技術演進，並依篇章走完全部劇情，最後收束到人物剖析、自由與循環的主題論、動畫改編與結局爭議。全程劇透，採東立譯名。",
      icon: "🧱",
      url: "topics/attack-on-titan/index.html",
      modules: [
        {
          title: "模組 A｜導論：兩個世界",
          courses: [
            { title: "兩個世界：牆內與牆外", url: "topics/attack-on-titan/lesson-01.html" },
            { title: "連載史：2009–2021", url: "topics/attack-on-titan/lesson-02.html" },
            { title: "這門課怎麼讀：四條軸線與名詞速查", url: "topics/attack-on-titan/lesson-03.html" },
            { title: "完整年表：從兩千年前到第 139 話", url: "topics/attack-on-titan/lesson-04.html" }
          ]
        },
        {
          title: "模組 B｜地理與政治",
          courses: [
            { title: "帕拉迪島與三道牆", url: "topics/attack-on-titan/lesson-05.html" },
            { title: "牆內地理：五個區與地下街", url: "topics/attack-on-titan/lesson-06.html" },
            { title: "牆內政體：王政、貴族、壁教", url: "topics/attack-on-titan/lesson-07.html" },
            { title: "牆外世界：馬萊、中東聯合、希茲爾國", url: "topics/attack-on-titan/lesson-08.html" },
            { title: "全球情勢：巨人為何開始過期", url: "topics/attack-on-titan/lesson-09.html" }
          ]
        },
        {
          title: "模組 C｜巨人學（一）：純潔巨人",
          courses: [
            { title: "生理總論：陽光、後頸、不需進食", url: "topics/attack-on-titan/lesson-10.html" },
            { title: "分類：普通種、奇行種、無垢巨人", url: "topics/attack-on-titan/lesson-11.html" },
            { title: "巨人怎麼被製造：脊髓液與注射", url: "topics/attack-on-titan/lesson-12.html" },
            { title: "巨人化的物理：閃電、蒸氣、再生、硬化", url: "topics/attack-on-titan/lesson-13.html" }
          ]
        },
        {
          title: "模組 D｜巨人學（二）：九大巨人",
          courses: [
            { title: "總論：十三年之咒與繼承規則", url: "topics/attack-on-titan/lesson-14.html" },
            { title: "始祖巨人：座標、道路、記憶改寫", url: "topics/attack-on-titan/lesson-15.html" },
            { title: "進擊的巨人：看見未來的繼承者", url: "topics/attack-on-titan/lesson-16.html" },
            { title: "超大型巨人與鎧之巨人", url: "topics/attack-on-titan/lesson-17.html" },
            { title: "女巨人與顎之巨人", url: "topics/attack-on-titan/lesson-18.html" },
            { title: "獸之巨人與車力巨人", url: "topics/attack-on-titan/lesson-19.html" },
            { title: "戰鎚巨人與九大總表", url: "topics/attack-on-titan/lesson-20.html" }
          ]
        },
        {
          title: "模組 E｜道路、尤米爾與座標",
          courses: [
            { title: "道路（Paths）的機制", url: "topics/attack-on-titan/lesson-21.html" },
            { title: "始祖尤米爾：兩千年的奴隸", url: "topics/attack-on-titan/lesson-22.html" },
            { title: "王家血統與不戰之約", url: "topics/attack-on-titan/lesson-23.html" },
            { title: "座標的三次啟動", url: "topics/attack-on-titan/lesson-24.html" }
          ]
        },
        {
          title: "模組 F｜歷史：艾爾迪亞與馬萊",
          courses: [
            { title: "尤米爾．弗利茲與那條生物", url: "topics/attack-on-titan/lesson-25.html" },
            { title: "艾爾迪亞帝國的一千七百年", url: "topics/attack-on-titan/lesson-26.html" },
            { title: "巨人大戰與馬萊崛起", url: "topics/attack-on-titan/lesson-27.html" },
            { title: "卡爾．弗利茲王與樂園的高牆", url: "topics/attack-on-titan/lesson-28.html" },
            { title: "收容區、臂章與戰士制度", url: "topics/attack-on-titan/lesson-29.html" },
            { title: "復權派、雷斯家與 845 年的起點", url: "topics/attack-on-titan/lesson-30.html" }
          ]
        },
        {
          title: "模組 G｜科技與軍事",
          courses: [
            { title: "立體機動裝置：完整原理", url: "topics/attack-on-titan/lesson-31.html" },
            { title: "四大兵團與長距離索敵陣形", url: "topics/attack-on-titan/lesson-32.html" },
            { title: "對巨人武器演進：雷槍與對人立體機動", url: "topics/attack-on-titan/lesson-33.html" },
            { title: "馬萊軍事科技：飛船、鐵道砲、艦隊", url: "topics/attack-on-titan/lesson-34.html" }
          ]
        },
        {
          title: "模組 H｜劇情（1）：序幕與托洛斯特",
          courses: [
            { title: "845 年：瑪利亞之牆陷落", url: "topics/attack-on-titan/lesson-35.html" },
            { title: "難民與奪還作戰：二十五萬人", url: "topics/attack-on-titan/lesson-36.html" },
            { title: "104 期訓練兵團", url: "topics/attack-on-titan/lesson-37.html" },
            { title: "托洛斯特攻防戰（上）", url: "topics/attack-on-titan/lesson-38.html" },
            { title: "托洛斯特攻防戰（下）與軍法會議", url: "topics/attack-on-titan/lesson-39.html" }
          ]
        },
        {
          title: "模組 I｜劇情（2）：女巨人",
          courses: [
            { title: "第 57 次壁外調查", url: "topics/attack-on-titan/lesson-40.html" },
            { title: "女巨人與里維班的覆滅", url: "topics/attack-on-titan/lesson-41.html" },
            { title: "斯托黑斯區攻防：亞妮的正體", url: "topics/attack-on-titan/lesson-42.html" },
            { title: "牆中的巨人", url: "topics/attack-on-titan/lesson-43.html" }
          ]
        },
        {
          title: "模組 J｜劇情（3）：巨人中的巨人",
          courses: [
            { title: "烏托匹亞區與尤米爾的秘密", url: "topics/attack-on-titan/lesson-44.html" },
            { title: "鎧與超大型的正體", url: "topics/attack-on-titan/lesson-45.html" },
            { title: "希斯特莉亞的身世與座標覺醒", url: "topics/attack-on-titan/lesson-46.html" },
            { title: "尤米爾的選擇與離去", url: "topics/attack-on-titan/lesson-47.html" }
          ]
        },
        {
          title: "模組 K｜劇情（4）：王政篇",
          courses: [
            { title: "中央憲兵與肯尼．阿卡曼", url: "topics/attack-on-titan/lesson-48.html" },
            { title: "王政真相：雷斯家與第一之王", url: "topics/attack-on-titan/lesson-49.html" },
            { title: "洞窟裡的禮拜堂", url: "topics/attack-on-titan/lesson-50.html" },
            { title: "女王希斯特莉亞與改革之後", url: "topics/attack-on-titan/lesson-51.html" }
          ]
        },
        {
          title: "模組 L｜劇情（5）：希干希納決戰",
          courses: [
            { title: "出發：瑪利亞之牆奪還作戰", url: "topics/attack-on-titan/lesson-52.html" },
            { title: "獸之巨人的投石", url: "topics/attack-on-titan/lesson-53.html" },
            { title: "艾爾文的最後衝鋒", url: "topics/attack-on-titan/lesson-54.html" },
            { title: "那個選擇：阿爾敏與艾爾文", url: "topics/attack-on-titan/lesson-55.html" },
            { title: "地下室的三本日記", url: "topics/attack-on-titan/lesson-56.html" }
          ]
        },
        {
          title: "模組 M｜格里沙與復權派",
          courses: [
            { title: "費依之死與復權派", url: "topics/attack-on-titan/lesson-57.html" },
            { title: "送往樂園與雷斯家的那一夜", url: "topics/attack-on-titan/lesson-58.html" },
            { title: "一個父親看見的未來", url: "topics/attack-on-titan/lesson-59.html" }
          ]
        },
        {
          title: "模組 N｜劇情（6）：馬萊篇",
          courses: [
            { title: "四年後：馬萊中東戰爭", url: "topics/attack-on-titan/lesson-60.html" },
            { title: "賈碧與法爾可：另一邊的孩子", url: "topics/attack-on-titan/lesson-61.html" },
            { title: "戰士隊的日常：萊納的地獄", url: "topics/attack-on-titan/lesson-62.html" },
            { title: "戰鎚巨人與泰巴家的演說", url: "topics/attack-on-titan/lesson-63.html" },
            { title: "宣戰佈告與莎夏之死", url: "topics/attack-on-titan/lesson-64.html" }
          ]
        },
        {
          title: "模組 O｜劇情（7）：帕拉迪島之戰",
          courses: [
            { title: "耶格爾派與義勇兵", url: "topics/attack-on-titan/lesson-65.html" },
            { title: "安樂死計劃", url: "topics/attack-on-titan/lesson-66.html" },
            { title: "艾連被捕與軍事政變", url: "topics/attack-on-titan/lesson-67.html" },
            { title: "吉克與艾連在道路中的對峙", url: "topics/attack-on-titan/lesson-68.html" },
            { title: "地鳴發動：始祖尤米爾的選擇", url: "topics/attack-on-titan/lesson-69.html" }
          ]
        },
        {
          title: "模組 P｜劇情（8）：地鳴與結局",
          courses: [
            { title: "超大型巨人群踏平世界", url: "topics/attack-on-titan/lesson-70.html" },
            { title: "反抗軍：昨日的敵人", url: "topics/attack-on-titan/lesson-71.html" },
            { title: "飛空艇與天空之戰", url: "topics/attack-on-titan/lesson-72.html" },
            { title: "最終決戰：巨人的骨骸與九大再臨", url: "topics/attack-on-titan/lesson-73.html" },
            { title: "第 139 話逐格細讀", url: "topics/attack-on-titan/lesson-74.html" }
          ]
        },
        {
          title: "模組 Q｜人物",
          courses: [
            { title: "艾連．葉卡", url: "topics/attack-on-titan/lesson-75.html" },
            { title: "三笠．阿卡曼與阿卡曼一族", url: "topics/attack-on-titan/lesson-76.html" },
            { title: "阿爾敏．亞魯雷特", url: "topics/attack-on-titan/lesson-77.html" },
            { title: "里維．阿卡曼", url: "topics/attack-on-titan/lesson-78.html" },
            { title: "艾爾文．史密斯與韓吉．佐耶", url: "topics/attack-on-titan/lesson-79.html" },
            { title: "104 期群像", url: "topics/attack-on-titan/lesson-80.html" },
            { title: "萊納．布朗", url: "topics/attack-on-titan/lesson-81.html" },
            { title: "吉克．葉卡與亞妮．雷恩哈特", url: "topics/attack-on-titan/lesson-82.html" },
            { title: "馬萊戰士隊與軍政人物", url: "topics/attack-on-titan/lesson-83.html" }
          ]
        },
        {
          title: "模組 R｜主題、改編與收束",
          courses: [
            { title: "「自由」的四種意思", url: "topics/attack-on-titan/lesson-84.html" },
            { title: "循環的暴力與森林的比喻", url: "topics/attack-on-titan/lesson-85.html" },
            { title: "加害者與被害者的互換", url: "topics/attack-on-titan/lesson-86.html" },
            { title: "動畫四季：WIT 到 MAPPA", url: "topics/attack-on-titan/lesson-87.html" },
            { title: "外傳、劇場版與周邊", url: "topics/attack-on-titan/lesson-88.html" },
            { title: "結局爭議：兩派論點", url: "topics/attack-on-titan/lesson-89.html" },
            { title: "伏筆總表、常見誤解與重看指南", url: "topics/attack-on-titan/lesson-90.html" }
          ]
        }
      ]
    },
    {
      id: "llm-models",
      category: "tech",
      title: "LLM 模型全解：從訓練到讀懂一張 Model Card",
      description:
        "完整拆解大型語言模型：一個模型由哪三件套組成、Transformer 的參數量如何精確計算、scaling law 怎麼決定該練多大餵多少資料、預訓練與後訓練各做了什麼、LoRA 與 QLoRA 的原理，以及 GGUF、GPTQ、Q4_K_M、8x7B 這些名詞的意思，最後收束到 VRAM 計算、推理引擎選擇與選型決策樹。",
      icon: "🧠",
      url: "topics/llm-models/index.html",
      modules: [
        {
          title: "模組 A｜導論：一個模型從無到有",
          courses: [
            { title: "什麼是「一個模型」：權重、架構、tokenizer 三件套", url: "topics/llm-models/lesson-01.html" },
            { title: "訓練四階段全景：從一張顯卡到一個 checkpoint", url: "topics/llm-models/lesson-02.html" },
            { title: "為什麼 Hugging Face 上的名字這麼亂", url: "topics/llm-models/lesson-03.html" },
            { title: "名詞速查表：六十個縮寫一次列完", url: "topics/llm-models/lesson-04.html" }
          ]
        },
        {
          title: "模組 B｜文字怎麼變成數字",
          courses: [
            { title: "Token 與 tokenizer：BPE 與 SentencePiece", url: "topics/llm-models/lesson-05.html" },
            { title: "Embedding：把 token 變成向量", url: "topics/llm-models/lesson-06.html" },
            { title: "為什麼中文比英文吃 token", url: "topics/llm-models/lesson-07.html" },
            { title: "位置編碼：從絕對位置到 RoPE", url: "topics/llm-models/lesson-08.html" },
            { title: "vocab 大小如何吃掉參數", url: "topics/llm-models/lesson-09.html" }
          ]
        },
        {
          title: "模組 C｜Transformer 骨架",
          courses: [
            { title: "注意力機制：Q、K、V 在算什麼", url: "topics/llm-models/lesson-10.html" },
            { title: "Multi-head attention 與它的參數帳", url: "topics/llm-models/lesson-11.html" },
            { title: "FFN／MLP：大部分參數其實在這裡", url: "topics/llm-models/lesson-12.html" },
            { title: "殘差、RMSNorm 與 SwiGLU", url: "topics/llm-models/lesson-13.html" },
            { title: "一層 block 的完整參數計算", url: "topics/llm-models/lesson-14.html" },
            { title: "Decoder-only 為什麼贏了", url: "topics/llm-models/lesson-15.html" }
          ]
        },
        {
          title: "模組 D｜參數量是怎麼決定的",
          courses: [
            { title: "四個旋鈕：d_model、n_layers、n_heads、FFN 比例", url: "topics/llm-models/lesson-16.html" },
            { title: "參數量公式：手算一個 7B 模型", url: "topics/llm-models/lesson-17.html" },
            { title: "寬 vs 深：同參數量下的取捨", url: "topics/llm-models/lesson-18.html" },
            { title: "GQA 與 MQA：KV head 怎麼省記憶體", url: "topics/llm-models/lesson-19.html" },
            { title: "為什麼永遠是 7B、8B、13B、70B", url: "topics/llm-models/lesson-20.html" },
            { title: "實作：從 config.json 反推任何模型的參數量", url: "topics/llm-models/lesson-21.html" }
          ]
        },
        {
          title: "模組 E｜Scaling Law：該練多大、餵多少",
          courses: [
            { title: "算力預算：C ≈ 6ND 這個公式", url: "topics/llm-models/lesson-22.html" },
            { title: "Kaplan 2020 與 Chinchilla 2022", url: "topics/llm-models/lesson-23.html" },
            { title: "為什麼現在大家都 over-train", url: "topics/llm-models/lesson-24.html" },
            { title: "推理成本進入公式：訓練一次、跑一億次", url: "topics/llm-models/lesson-25.html" },
            { title: "決策表：給定預算怎麼選 N 與 D", url: "topics/llm-models/lesson-26.html" }
          ]
        },
        {
          title: "模組 F｜預訓練：資料與過程",
          courses: [
            { title: "資料從哪來：Common Crawl、FineWeb、The Pile", url: "topics/llm-models/lesson-27.html" },
            { title: "資料清洗：去重、品質分類、過濾", url: "topics/llm-models/lesson-28.html" },
            { title: "資料配方與課程式訓練", url: "topics/llm-models/lesson-29.html" },
            { title: "訓練迴圈：loss、learning rate schedule、warmup", url: "topics/llm-models/lesson-30.html" },
            { title: "分散式訓練：DP、TP、PP、FSDP 與 ZeRO", url: "topics/llm-models/lesson-31.html" },
            { title: "一次預訓練要花多少錢、多少卡、多少天", url: "topics/llm-models/lesson-32.html" }
          ]
        },
        {
          title: "模組 G｜後訓練：從會接話到會做事",
          courses: [
            { title: "Base model 為什麼不能直接用", url: "topics/llm-models/lesson-33.html" },
            { title: "SFT：指令微調與 chat template", url: "topics/llm-models/lesson-34.html" },
            { title: "RLHF：reward model 與 PPO", url: "topics/llm-models/lesson-35.html" },
            { title: "DPO 家族：ORPO、KTO、SimPO", url: "topics/llm-models/lesson-36.html" },
            { title: "GRPO 與可驗證獎勵：推理模型怎麼練出來的", url: "topics/llm-models/lesson-37.html" },
            { title: "蒸餾：R1-Distill-Qwen-7B 這種名字是什麼意思", url: "topics/llm-models/lesson-38.html" }
          ]
        },
        {
          title: "模組 H｜微調：你自己做得到的部分",
          courses: [
            { title: "全參數微調 vs PEFT", url: "topics/llm-models/lesson-39.html" },
            { title: "LoRA：低秩分解在做什麼", url: "topics/llm-models/lesson-40.html" },
            { title: "QLoRA：4-bit 基底加 LoRA", url: "topics/llm-models/lesson-41.html" },
            { title: "adapter、merged 與多 LoRA 切換", url: "topics/llm-models/lesson-42.html" },
            { title: "該微調、該 RAG、還是該改 prompt", url: "topics/llm-models/lesson-43.html" }
          ]
        },
        {
          title: "模組 I｜MoE：AxB 到底什麼意思",
          courses: [
            { title: "稀疏模型的想法：不是每個 token 都要全部參數", url: "topics/llm-models/lesson-44.html" },
            { title: "Router 與 expert：一次選幾個", url: "topics/llm-models/lesson-45.html" },
            { title: "讀懂 8x7B：Mixtral 為何是 47B 而不是 56B", url: "topics/llm-models/lesson-46.html" },
            { title: "讀懂 A3B：總參數與活躍參數的命名", url: "topics/llm-models/lesson-47.html" },
            { title: "MoE 的代價：VRAM 全載、通訊開銷、負載不均", url: "topics/llm-models/lesson-48.html" }
          ]
        },
        {
          title: "模組 J｜數值精度與量化原理",
          courses: [
            { title: "FP32、FP16、BF16、FP8：位元怎麼分配", url: "topics/llm-models/lesson-49.html" },
            { title: "為什麼 BF16 打敗 FP16", url: "topics/llm-models/lesson-50.html" },
            { title: "量化的本質：壓到 4 bit 失去了什麼", url: "topics/llm-models/lesson-51.html" },
            { title: "PTQ 與 QAT：事後量化與訓練中量化", url: "topics/llm-models/lesson-52.html" },
            { title: "每權重位元數（bpw）與品質的關係", url: "topics/llm-models/lesson-53.html" },
            { title: "校準資料與 imatrix 在做什麼", url: "topics/llm-models/lesson-54.html" }
          ]
        },
        {
          title: "模組 K｜量化格式全解",
          courses: [
            { title: "GGUF：它是容器格式，不是演算法", url: "topics/llm-models/lesson-55.html" },
            { title: "讀懂 Q4_K_M：K-quant 命名規則全表", url: "topics/llm-models/lesson-56.html" },
            { title: "IQ 系列與 imatrix 量化", url: "topics/llm-models/lesson-57.html" },
            { title: "GPTQ：逐層最小化誤差", url: "topics/llm-models/lesson-58.html" },
            { title: "AWQ：保護最重要的那些權重", url: "topics/llm-models/lesson-59.html" },
            { title: "EXL2、bitsandbytes、MLX、FP8：其餘格式與該選誰", url: "topics/llm-models/lesson-60.html" }
          ]
        },
        {
          title: "模組 L｜讀懂一張 Model Card",
          courses: [
            { title: "命名結構拆解：組織／家族－尺寸－變體－量化", url: "topics/llm-models/lesson-61.html" },
            { title: "變體後綴全表：Base、Instruct、Chat、it、Thinking", url: "topics/llm-models/lesson-62.html" },
            { title: "社群後綴：distill、abliterated、uncensored、merge", url: "topics/llm-models/lesson-63.html" },
            { title: "檔案清單：safetensors、config.json、tokenizer、shard", url: "topics/llm-models/lesson-64.html" },
            { title: "授權與 gated repo", url: "topics/llm-models/lesson-65.html" },
            { title: "誰做的量化：發佈者的差異", url: "topics/llm-models/lesson-66.html" }
          ]
        },
        {
          title: "模組 M｜跑起來：硬體與記憶體帳",
          courses: [
            { title: "VRAM 公式：權重、KV cache、啟動值、開銷", url: "topics/llm-models/lesson-67.html" },
            { title: "KV cache 怎麼算，為什麼長 context 這麼貴", url: "topics/llm-models/lesson-68.html" },
            { title: "Context length、RoPE scaling 與 YaRN", url: "topics/llm-models/lesson-69.html" },
            { title: "推理引擎：llama.cpp、Ollama、LM Studio、vLLM、SGLang", url: "topics/llm-models/lesson-70.html" },
            { title: "塞不下時的手段：offload、mmap、量化 KV cache", url: "topics/llm-models/lesson-71.html" },
            { title: "對照表：你的硬體能跑哪些模型", url: "topics/llm-models/lesson-72.html" }
          ]
        },
        {
          title: "模組 N｜評測與選型",
          courses: [
            { title: "常見 benchmark 各測什麼", url: "topics/llm-models/lesson-73.html" },
            { title: "為什麼 benchmark 分數會騙人", url: "topics/llm-models/lesson-74.html" },
            { title: "人類偏好評測與競技場", url: "topics/llm-models/lesson-75.html" },
            { title: "自己建 eval set", url: "topics/llm-models/lesson-76.html" },
            { title: "選型決策樹：從需求走到模型與量化等級", url: "topics/llm-models/lesson-77.html" }
          ]
        },
        {
          title: "模組 O｜總結",
          courses: [
            { title: "開源權重與商用 API：什麼時候用哪邊", url: "topics/llm-models/lesson-78.html" },
            { title: "從零到一：把一個模型跑起來的完整清單", url: "topics/llm-models/lesson-79.html" },
            { title: "常見誤解十五條", url: "topics/llm-models/lesson-80.html" },
            { title: "名詞總表與延伸閱讀", url: "topics/llm-models/lesson-81.html" }
          ]
        }
      ]
    },
    {
      id: "video-at-scale",
      category: "tech",
      title: "影音平台的規模工程：YouTube 到底需要多少頻寬、機器與電力",
      description:
        "從一支影片的位元組開始，一路推導到十億人規模的基礎設施：頻寬、CDN、儲存、轉碼、機器數量與電力全部算出來。涵蓋位元率階梯、HLS/DASH 與 ABR、transit 與 peering 的計費、長尾與快取命中率、糾刪碼、專用晶片與 PUE，最後收束到每次觀看的實際成本，以及四種平台為何走向完全不同的架構。",
      icon: "📺",
      url: "topics/video-at-scale/index.html",
      modules: [
        {
          title: "模組 A｜先把規模感建立起來",
          courses: [
            { title: "一個影片請求到底是多少位元組", url: "topics/video-at-scale/lesson-01.html" },
            { title: "從一個人到十億人：把數字乘上去", url: "topics/video-at-scale/lesson-02.html" },
            { title: "三個決定一切的數字：位元率、同時在線、尖峰倍率", url: "topics/video-at-scale/lesson-03.html" },
            { title: "動手算：YouTube 的頻寬需求", url: "topics/video-at-scale/lesson-04.html" },
            { title: "為什麼「買頻寬」這句話本身是誤解", url: "topics/video-at-scale/lesson-05.html" }
          ]
        },
        {
          title: "模組 B｜影片本身：位元組從哪來",
          courses: [
            { title: "影格、解析度、色深：未壓縮有多可怕", url: "topics/video-at-scale/lesson-06.html" },
            { title: "壓縮原理：為什麼影片能壓到千分之一", url: "topics/video-at-scale/lesson-07.html" },
            { title: "編碼器演進：H.264、VP9、H.265、AV1", url: "topics/video-at-scale/lesson-08.html" },
            { title: "位元率階梯與 ABR", url: "topics/video-at-scale/lesson-09.html" },
            { title: "一支影片變成十幾個檔案", url: "topics/video-at-scale/lesson-10.html" },
            { title: "各畫質的實際位元率對照表", url: "topics/video-at-scale/lesson-11.html" }
          ]
        },
        {
          title: "模組 C｜串流怎麼送",
          courses: [
            { title: "不是下載也不是串流：HLS 與 DASH 的分段機制", url: "topics/video-at-scale/lesson-12.html" },
            { title: "播放器怎麼決定畫質：ABR 演算法與緩衝區", url: "topics/video-at-scale/lesson-13.html" },
            { title: "TCP、QUIC 與影片：為什麼影片走 HTTP", url: "topics/video-at-scale/lesson-14.html" },
            { title: "首幀時間與卡頓率：使用者真正在意的指標", url: "topics/video-at-scale/lesson-15.html" },
            { title: "直播與點播的根本差異", url: "topics/video-at-scale/lesson-16.html" }
          ]
        },
        {
          title: "模組 D｜頻寬的物理與金錢",
          courses: [
            { title: "頻寬到底是什麼：水管比喻為何會誤導", url: "topics/video-at-scale/lesson-17.html" },
            { title: "網際網路的三層結構", url: "topics/video-at-scale/lesson-18.html" },
            { title: "Transit、Peering、IX：三種連法與三種帳單", url: "topics/video-at-scale/lesson-19.html" },
            { title: "95th percentile 計費：為什麼尖峰決定價格", url: "topics/video-at-scale/lesson-20.html" },
            { title: "算錢：100 Tbps 如果全走 transit", url: "topics/video-at-scale/lesson-21.html" },
            { title: "為什麼大公司最後都自己蓋網路", url: "topics/video-at-scale/lesson-22.html" }
          ]
        },
        {
          title: "模組 E｜為什麼一個機房不夠",
          courses: [
            { title: "光速的限制：RTT 與體驗", url: "topics/video-at-scale/lesson-23.html" },
            { title: "集中式架構的三個死因", url: "topics/video-at-scale/lesson-24.html" },
            { title: "長尾分布：1% 的影片佔 90% 的流量", url: "topics/video-at-scale/lesson-25.html" },
            { title: "快取命中率：整個 CDN 的核心指標", url: "topics/video-at-scale/lesson-26.html" },
            { title: "從中心到邊緣：分層快取架構", url: "topics/video-at-scale/lesson-27.html" }
          ]
        },
        {
          title: "模組 F｜CDN：真正在送影片的那一層",
          courses: [
            { title: "CDN 不只是「離你比較近的伺服器」", url: "topics/video-at-scale/lesson-28.html" },
            { title: "自建 vs 商用 CDN：成本的分水嶺", url: "topics/video-at-scale/lesson-29.html" },
            { title: "PoP、edge、mid-tier、origin 四層", url: "topics/video-at-scale/lesson-30.html" },
            { title: "內嵌式 CDN：把機器放進 ISP 機房", url: "topics/video-at-scale/lesson-31.html" },
            { title: "預先填充：離峰時段把貨搬過去", url: "topics/video-at-scale/lesson-32.html" },
            { title: "導流：使用者怎麼被指到正確那台機器", url: "topics/video-at-scale/lesson-33.html" }
          ]
        },
        {
          title: "模組 G｜儲存（一）：到底存了什麼",
          courses: [
            { title: "一支影片上傳後產生的完整檔案清單", url: "topics/video-at-scale/lesson-34.html" },
            { title: "原始檔要不要留：留與不留的代價", url: "topics/video-at-scale/lesson-35.html" },
            { title: "縮圖、字幕、metadata：容易被忽略的部分", url: "topics/video-at-scale/lesson-36.html" },
            { title: "動手算：每天長出多少資料", url: "topics/video-at-scale/lesson-37.html" },
            { title: "冷熱分層：99% 的影片沒人看", url: "topics/video-at-scale/lesson-38.html" },
            { title: "十年後怎麼辦：資料只增不減", url: "topics/video-at-scale/lesson-39.html" }
          ]
        },
        {
          title: "模組 H｜儲存（二）：怎麼存才不會壞",
          courses: [
            { title: "硬碟會壞：年故障率乘上規模", url: "topics/video-at-scale/lesson-40.html" },
            { title: "複本 vs 糾刪碼", url: "topics/video-at-scale/lesson-41.html" },
            { title: "為什麼還在用機械硬碟", url: "topics/video-at-scale/lesson-42.html" },
            { title: "分散式檔案系統：從 GFS 到現代", url: "topics/video-at-scale/lesson-43.html" },
            { title: "靜默損壞與定期掃描", url: "topics/video-at-scale/lesson-44.html" }
          ]
        },
        {
          title: "模組 I｜轉碼：最貴的那道工",
          courses: [
            { title: "上傳之後發生什麼：轉碼管線全圖", url: "topics/video-at-scale/lesson-45.html" },
            { title: "轉碼要多少算力", url: "topics/video-at-scale/lesson-46.html" },
            { title: "為什麼要做專用晶片", url: "topics/video-at-scale/lesson-47.html" },
            { title: "分級轉碼：熱門影片才值得用好編碼器", url: "topics/video-at-scale/lesson-48.html" },
            { title: "動手算：每天 72 萬小時要多少台轉碼機", url: "topics/video-at-scale/lesson-49.html" }
          ]
        },
        {
          title: "模組 J｜機器數量：把帳算出來",
          courses: [
            { title: "伺服器的四種角色與各自規格", url: "topics/video-at-scale/lesson-50.html" },
            { title: "Edge 要幾台", url: "topics/video-at-scale/lesson-51.html" },
            { title: "儲存要幾台", url: "topics/video-at-scale/lesson-52.html" },
            { title: "轉碼要幾台", url: "topics/video-at-scale/lesson-53.html" },
            { title: "總表：一個 YouTube 規模的機隊", url: "topics/video-at-scale/lesson-54.html" }
          ]
        },
        {
          title: "模組 K｜資料中心本身",
          courses: [
            { title: "裡面長什麼樣：機櫃、冷熱通道、走線", url: "topics/video-at-scale/lesson-55.html" },
            { title: "電力：為什麼單位是 MW 而不是台數", url: "topics/video-at-scale/lesson-56.html" },
            { title: "PUE：那個 1.1 代表什麼", url: "topics/video-at-scale/lesson-57.html" },
            { title: "冷卻：從空調到液冷", url: "topics/video-at-scale/lesson-58.html" },
            { title: "資料中心網路：Clos 與 spine-leaf", url: "topics/video-at-scale/lesson-59.html" },
            { title: "選址：電、水、光纖、稅、天氣", url: "topics/video-at-scale/lesson-60.html" }
          ]
        },
        {
          title: "模組 L｜可靠度與營運",
          courses: [
            { title: "一萬台機器每天會壞幾台", url: "topics/video-at-scale/lesson-61.html" },
            { title: "沒有「不會故障」，只有「壞了沒人發現」", url: "topics/video-at-scale/lesson-62.html" },
            { title: "容量規劃：為什麼要留四成餘裕", url: "topics/video-at-scale/lesson-63.html" },
            { title: "尖峰事件：世界盃、跨年、大片上架", url: "topics/video-at-scale/lesson-64.html" },
            { title: "監控與 SRE：怎麼知道系統是正常的", url: "topics/video-at-scale/lesson-65.html" }
          ]
        },
        {
          title: "模組 M｜成本結構與商業模式",
          courses: [
            { title: "一次觀看到底花多少錢", url: "topics/video-at-scale/lesson-66.html" },
            { title: "成本四塊：頻寬、儲存、運算、人", url: "topics/video-at-scale/lesson-67.html" },
            { title: "為什麼廣告養得起這件事", url: "topics/video-at-scale/lesson-68.html" },
            { title: "規模經濟的門檻：為什麼小公司做不了", url: "topics/video-at-scale/lesson-69.html" },
            { title: "用商用服務要多少錢：對照表", url: "topics/video-at-scale/lesson-70.html" }
          ]
        },
        {
          title: "模組 N｜別人怎麼做",
          courses: [
            { title: "Netflix：片庫小、畫質高、可預測", url: "topics/video-at-scale/lesson-71.html" },
            { title: "直播平台：不能快取的那個難題", url: "topics/video-at-scale/lesson-72.html" },
            { title: "短影音：為什麼比長影片更難", url: "topics/video-at-scale/lesson-73.html" },
            { title: "社群平台的影片：自動播放的代價", url: "topics/video-at-scale/lesson-74.html" }
          ]
        },
        {
          title: "模組 O｜總結",
          courses: [
            { title: "從一萬人到一億人的演進路線", url: "topics/video-at-scale/lesson-75.html" },
            { title: "常見誤解十二條", url: "topics/video-at-scale/lesson-76.html" },
            { title: "名詞總表、公式總表與延伸閱讀", url: "topics/video-at-scale/lesson-77.html" }
          ]
        }
      ]
    },
    {
      id: "spaceflight",
      category: "science",
      title: "飛向太空：阿波羅登月的每一步與飛向火星的軌道計算",
      description:
        "從牛頓的兩條定律推導出軌道力學，再用它把阿波羅登月的每一腳點火算出來：TLI 3.14、LOI 0.92、下降 2.0、上升 1.86、TEI 1.0 km/s，全部附算式並與實測對照。涵蓋 vis-viva 與克卜勒方程、Lambert 問題、火箭方程與分節、動力下降與 1202 警報、再入走廊，最後延伸到霍曼轉移、重力助推與火星 EDL。",
      icon: "🚀",
      url: "topics/spaceflight/index.html",
      modules: [
        {
          title: "模組 A｜先建立規模感",
          courses: [
            { title: "上太空難在哪：不是「高」，是「快」", url: "topics/spaceflight/lesson-01.html" },
            { title: "三個必須記住的數字：7.8、11.2、9.8", url: "topics/spaceflight/lesson-02.html" },
            { title: "從地表到月球的完整能量帳", url: "topics/spaceflight/lesson-03.html" },
            { title: "阿波羅計畫的量級：人、錢、時間", url: "topics/spaceflight/lesson-04.html" },
            { title: "這門課會算出哪些數字、用什麼工具", url: "topics/spaceflight/lesson-05.html" }
          ]
        },
        {
          title: "模組 B｜軌道力學（一）：從牛頓到圓錐曲線",
          courses: [
            { title: "牛頓的大砲：軌道是一直往下掉卻掉不到地面", url: "topics/spaceflight/lesson-06.html" },
            { title: "二體問題：從 F = ma 寫出運動方程", url: "topics/spaceflight/lesson-07.html" },
            { title: "化簡成相對運動：重力參數 μ 的由來", url: "topics/spaceflight/lesson-08.html" },
            { title: "角動量守恆：為什麼軌道是平面的", url: "topics/spaceflight/lesson-09.html" },
            { title: "能量守恆與 vis-viva 的推導", url: "topics/spaceflight/lesson-10.html" },
            { title: "解微分方程：軌道方程與圓錐曲線", url: "topics/spaceflight/lesson-11.html" },
            { title: "克卜勒三定律：從推導結果反讀回去", url: "topics/spaceflight/lesson-12.html" },
            { title: "圓、橢圓、拋物線、雙曲線：四種軌道與判別", url: "topics/spaceflight/lesson-13.html" },
            { title: "軌道六要素：用六個數字描述一條軌道", url: "topics/spaceflight/lesson-14.html" }
          ]
        },
        {
          title: "模組 C｜軌道力學（二）：改變軌道與求解",
          courses: [
            { title: "Δv 是太空旅行的貨幣", url: "topics/spaceflight/lesson-15.html" },
            { title: "霍曼轉移：兩圈之間最省的走法", url: "topics/spaceflight/lesson-16.html" },
            { title: "動手算：LEO 到 GEO 要多少 Δv", url: "topics/spaceflight/lesson-17.html" },
            { title: "克卜勒方程：偏近點角與牛頓法求根", url: "topics/spaceflight/lesson-18.html" },
            { title: "從時間反推位置：軌道傳播", url: "topics/spaceflight/lesson-19.html" },
            { title: "Lambert 問題：給兩點與飛行時間，求那條軌道", url: "topics/spaceflight/lesson-20.html" },
            { title: "Oberth 效應：為什麼在近地點加速最划算", url: "topics/spaceflight/lesson-21.html" },
            { title: "改變軌道面有多貴", url: "topics/spaceflight/lesson-22.html" },
            { title: "數值積分：RK4、步長與能量漂移", url: "topics/spaceflight/lesson-23.html" }
          ]
        },
        {
          title: "模組 D｜火箭方程：質量比的殘酷",
          courses: [
            { title: "齊奧爾科夫斯基方程式的推導", url: "topics/spaceflight/lesson-24.html" },
            { title: "比衝（Isp）到底是什麼", url: "topics/spaceflight/lesson-25.html" },
            { title: "質量比的殘酷：為什麼 90% 都是燃料", url: "topics/spaceflight/lesson-26.html" },
            { title: "為什麼一定要分節：多節火箭的最佳化", url: "topics/spaceflight/lesson-27.html" },
            { title: "動手算：把 45 噸送上月球轉移軌道要多大的火箭", url: "topics/spaceflight/lesson-28.html" }
          ]
        },
        {
          title: "模組 E｜土星五號與阿波羅載具全解",
          courses: [
            { title: "全疊構型：110 公尺裡裝了什麼", url: "topics/spaceflight/lesson-29.html" },
            { title: "S-IC 第一節：五具 F-1 與那 168 秒", url: "topics/spaceflight/lesson-30.html" },
            { title: "S-II 第二節：液氫的工程難題", url: "topics/spaceflight/lesson-31.html" },
            { title: "S-IVB 第三節：唯一能二次點火的那一節", url: "topics/spaceflight/lesson-32.html" },
            { title: "指揮艙 CM：三個人住的那個錐體", url: "topics/spaceflight/lesson-33.html" },
            { title: "服務艙 SM：推進、電力、氧氣", url: "topics/spaceflight/lesson-34.html" },
            { title: "登月艙 LM：唯一在真空中設計的載人載具", url: "topics/spaceflight/lesson-35.html" }
          ]
        },
        {
          title: "模組 F｜帶了什麼上去",
          courses: [
            { title: "生命維持：氧氣、二氧化碳、水、熱", url: "topics/spaceflight/lesson-36.html" },
            { title: "電力：燃料電池與電池", url: "topics/spaceflight/lesson-37.html" },
            { title: "食物與水：八天份怎麼算", url: "topics/spaceflight/lesson-38.html" },
            { title: "A7L 太空衣：一件衣服就是一艘太空船", url: "topics/spaceflight/lesson-39.html" },
            { title: "導航電腦 AGC 的 72 KB", url: "topics/spaceflight/lesson-40.html" },
            { title: "科學儀器、工具與帶回來的東西", url: "topics/spaceflight/lesson-41.html" }
          ]
        },
        {
          title: "模組 G｜發射：從點火到地球停泊軌道",
          courses: [
            { title: "為什麼在佛羅里達往東射", url: "topics/spaceflight/lesson-42.html" },
            { title: "發射窗口怎麼決定", url: "topics/spaceflight/lesson-43.html" },
            { title: "T-0 到 T+12 分鐘：逐秒時序", url: "topics/spaceflight/lesson-44.html" },
            { title: "重力轉彎與 Max Q：上升軌跡的最佳化", url: "topics/spaceflight/lesson-45.html" },
            { title: "分節與拋罩：每一次丟東西都是為了質量比", url: "topics/spaceflight/lesson-46.html" },
            { title: "停泊軌道：為什麼要先繞地球兩圈", url: "topics/spaceflight/lesson-47.html" }
          ]
        },
        {
          title: "模組 H｜TLI：算出飛向月球的那一腳",
          courses: [
            { title: "問題的形式：要多快才能到月球", url: "topics/spaceflight/lesson-48.html" },
            { title: "逃逸速度與「差一點逃逸」的軌道", url: "topics/spaceflight/lesson-49.html" },
            { title: "動手算：TLI 需要多少 Δv", url: "topics/spaceflight/lesson-50.html" },
            { title: "為什麼要瞄準月球未來的位置：Lambert 的實際應用", url: "topics/spaceflight/lesson-51.html" },
            { title: "自由返回軌道：一個救命的設計", url: "topics/spaceflight/lesson-52.html" },
            { title: "轉位、抽出與對接", url: "topics/spaceflight/lesson-53.html" }
          ]
        },
        {
          title: "模組 I｜地月轉移途中的四天",
          courses: [
            { title: "中途修正：為什麼四次就夠", url: "topics/spaceflight/lesson-54.html" },
            { title: "導航：三種定位方法與誤差橢球", url: "topics/spaceflight/lesson-55.html" },
            { title: "被動熱控：那個每小時三圈的翻滾", url: "topics/spaceflight/lesson-56.html" },
            { title: "影響球：什麼時候「歸月球管」", url: "topics/spaceflight/lesson-57.html" },
            { title: "途中的日常：睡覺、吃飯、上廁所", url: "topics/spaceflight/lesson-58.html" }
          ]
        },
        {
          title: "模組 J｜LOI：進入月球軌道",
          courses: [
            { title: "到了月球為什麼不會自己被抓住", url: "topics/spaceflight/lesson-59.html" },
            { title: "動手算：LOI 需要多少 Δv", url: "topics/spaceflight/lesson-60.html" },
            { title: "為什麼在月球背面點火", url: "topics/spaceflight/lesson-61.html" },
            { title: "從橢圓到圓：LOI-2 與降軌", url: "topics/spaceflight/lesson-62.html" },
            { title: "月球重力異常（mascon）與軌道衰減", url: "topics/spaceflight/lesson-63.html" }
          ]
        },
        {
          title: "模組 K｜下降與著陸",
          courses: [
            { title: "分離與 DOI：降到 15 公里", url: "topics/spaceflight/lesson-64.html" },
            { title: "動力下降 PDI 的三個階段", url: "topics/spaceflight/lesson-65.html" },
            { title: "為什麼不能用霍曼轉移直接落地", url: "topics/spaceflight/lesson-66.html" },
            { title: "重力轉向導引：P63/P64/P66 的數學", url: "topics/spaceflight/lesson-67.html" },
            { title: "1202 警報：那台電腦到底發生什麼事", url: "topics/spaceflight/lesson-68.html" },
            { title: "最後 150 公尺：人工接手與燃料餘裕", url: "topics/spaceflight/lesson-69.html" }
          ]
        },
        {
          title: "模組 L｜月面",
          courses: [
            { title: "著陸後第一件事：待命起飛檢查", url: "topics/spaceflight/lesson-70.html" },
            { title: "出艙：減壓、下梯、第一步", url: "topics/spaceflight/lesson-71.html" },
            { title: "月面活動：採樣、儀器、月球車", url: "topics/spaceflight/lesson-72.html" },
            { title: "待多久由什麼決定", url: "topics/spaceflight/lesson-73.html" }
          ]
        },
        {
          title: "模組 M｜上升、會合與對接",
          courses: [
            { title: "上升節：一具沒有備份的引擎", url: "topics/spaceflight/lesson-74.html" },
            { title: "動手算：從月面到月球軌道要多少 Δv", url: "topics/spaceflight/lesson-75.html" },
            { title: "會合的幾何：追趕、相位與 CW 方程", url: "topics/spaceflight/lesson-76.html" },
            { title: "共橢圓會合（CDH / TPI）", url: "topics/spaceflight/lesson-77.html" },
            { title: "對接與轉移", url: "topics/spaceflight/lesson-78.html" },
            { title: "拋棄上升節：撞月球的科學用途", url: "topics/spaceflight/lesson-79.html" }
          ]
        },
        {
          title: "模組 N｜TEI、返航與再入",
          courses: [
            { title: "TEI：回家那一腳要多少 Δv", url: "topics/spaceflight/lesson-80.html" },
            { title: "返程中途修正與精度要求", url: "topics/spaceflight/lesson-81.html" },
            { title: "再入走廊：那 2 度的窗口怎麼算出來", url: "topics/spaceflight/lesson-82.html" },
            { title: "再入的物理：11 km/s 的熱與 Allen–Eggers 解", url: "topics/spaceflight/lesson-83.html" },
            { title: "燒蝕熱盾與黑障", url: "topics/spaceflight/lesson-84.html" },
            { title: "降落傘、濺落與回收", url: "topics/spaceflight/lesson-85.html" }
          ]
        },
        {
          title: "模組 O｜逐次任務與失敗案例",
          courses: [
            { title: "阿波羅 1 號到 10 號：每一次解決了什麼", url: "topics/spaceflight/lesson-86.html" },
            { title: "阿波羅 11 號：逐時間軸重走一次", url: "topics/spaceflight/lesson-87.html" },
            { title: "阿波羅 13 號：故障樹與那些手算", url: "topics/spaceflight/lesson-88.html" },
            { title: "阿波羅 14–17 號與 J 型任務", url: "topics/spaceflight/lesson-89.html" }
          ]
        },
        {
          title: "模組 P｜飛向火星",
          courses: [
            { title: "從繞地球到繞太陽：參考系換了", url: "topics/spaceflight/lesson-90.html" },
            { title: "地火霍曼轉移：為什麼是 259 天", url: "topics/spaceflight/lesson-91.html" },
            { title: "發射窗口：26 個月一次與 porkchop plot", url: "topics/spaceflight/lesson-92.html" },
            { title: "動手算：去火星要多少 C3 與 Δv", url: "topics/spaceflight/lesson-93.html" },
            { title: "重力助推：免費的 Δv 從哪來", url: "topics/spaceflight/lesson-94.html" },
            { title: "抵達火星的三種方式：飛掠、環繞、著陸", url: "topics/spaceflight/lesson-95.html" },
            { title: "EDL 那七分鐘：從 5.6 km/s 到 0", url: "topics/spaceflight/lesson-96.html" },
            { title: "通訊、電力與火星探測器帶了什麼", url: "topics/spaceflight/lesson-97.html" }
          ]
        },
        {
          title: "模組 Q｜總結",
          courses: [
            { title: "月球 vs 火星：兩張 Δv 總表", url: "topics/spaceflight/lesson-98.html" },
            { title: "公式總表與名詞索引", url: "topics/spaceflight/lesson-99.html" },
            { title: "如果今天重做一次：Artemis 與現代方案", url: "topics/spaceflight/lesson-100.html" }
          ]
        }
      ]
    },
    {
      id: "leetcode",
      category: "tech",
      title: "LeetCode 題解：思路、圖解與 Python 實作",
      description:
        "一題一頁、持續累積的 LeetCode 解題筆記。每一題都附英文題目敘述與中文翻譯、完整的範例與限制條件，再把所有值得知道的解法一個一個拆開講：從暴力法開始，說明它為什麼慢，再一步步優化到最佳解，需要的地方補上圖解。全部用 Python，附複雜度對照表與邊界條件檢查清單。",
      icon: "🧩",
      url: "topics/leetcode/index.html",
      modules: [
        {
          title: "第 001–025 題",
          courses: [
            { title: "1. Two Sum 兩數之和", url: "topics/leetcode/problem-0001.html" },
            { title: "2. Add Two Numbers 兩數相加", url: "topics/leetcode/problem-0002.html" },
            { title: "3. Longest Substring Without Repeating Characters 無重複字元的最長子字串", url: "topics/leetcode/problem-0003.html" },
            { title: "4. Median of Two Sorted Arrays 兩個有序陣列的中位數", url: "topics/leetcode/problem-0004.html" },
            { title: "5. Longest Palindromic Substring 最長回文子字串", url: "topics/leetcode/problem-0005.html" },
            { title: "6. Zigzag Conversion Z 字形變換", url: "topics/leetcode/problem-0006.html" },
            { title: "7. Reverse Integer 整數反轉", url: "topics/leetcode/problem-0007.html" },
            { title: "8. String to Integer (atoi) 字串轉換整數", url: "topics/leetcode/problem-0008.html" },
            { title: "9. Palindrome Number 回文數", url: "topics/leetcode/problem-0009.html" },
            { title: "10. Regular Expression Matching 正規表示式匹配", url: "topics/leetcode/problem-0010.html" },
            { title: "11. Container With Most Water 盛最多水的容器", url: "topics/leetcode/problem-0011.html" },
            { title: "12. Integer to Roman 整數轉羅馬數字", url: "topics/leetcode/problem-0012.html" },
            { title: "13. Roman to Integer 羅馬數字轉整數", url: "topics/leetcode/problem-0013.html" },
            { title: "14. Longest Common Prefix 最長公共前綴", url: "topics/leetcode/problem-0014.html" },
            { title: "15. 3Sum 三數之和", url: "topics/leetcode/problem-0015.html" },
            { title: "16. 3Sum Closest 最接近的三數之和", url: "topics/leetcode/problem-0016.html" },
            { title: "17. Letter Combinations of a Phone Number 電話號碼的字母組合", url: "topics/leetcode/problem-0017.html" },
            { title: "18. 4Sum 四數之和", url: "topics/leetcode/problem-0018.html" },
            { title: "19. Remove Nth Node From End of List 刪除鏈結串列的倒數第 N 個節點", url: "topics/leetcode/problem-0019.html" },
            { title: "20. Valid Parentheses 有效的括號", url: "topics/leetcode/problem-0020.html" },
            { title: "21. Merge Two Sorted Lists 合併兩個有序串列", url: "topics/leetcode/problem-0021.html" },
            { title: "22. Generate Parentheses 括號生成", url: "topics/leetcode/problem-0022.html" },
            { title: "23. Merge k Sorted Lists 合併 K 個升序串列", url: "topics/leetcode/problem-0023.html" },
            { title: "24. Swap Nodes in Pairs 兩兩交換串列中的節點", url: "topics/leetcode/problem-0024.html" },
            { title: "25. Reverse Nodes in k-Group K 個一組翻轉串列", url: "topics/leetcode/problem-0025.html" }
          ]
        },
        {
          title: "第 026–050 題",
          courses: [
            { title: "26. Remove Duplicates from Sorted Array 刪除有序陣列中的重複項", url: "topics/leetcode/problem-0026.html" },
            { title: "27. Remove Element 移除元素", url: "topics/leetcode/problem-0027.html" },
            { title: "28. Find the Index of the First Occurrence in a String 找出字串中第一個匹配項的下標", url: "topics/leetcode/problem-0028.html" },
            { title: "29. Divide Two Integers 兩數相除", url: "topics/leetcode/problem-0029.html" },
            { title: "30. Substring with Concatenation of All Words 串聯所有單詞的子串", url: "topics/leetcode/problem-0030.html" },
            { title: "31. Next Permutation 下一個排列", url: "topics/leetcode/problem-0031.html" },
            { title: "32. Longest Valid Parentheses 最長有效括號", url: "topics/leetcode/problem-0032.html" },
            { title: "33. Search in Rotated Sorted Array 搜尋旋轉排序陣列", url: "topics/leetcode/problem-0033.html" },
            { title: "34. Find First and Last Position of Element in Sorted Array 在排序陣列中查找元素的第一個和最後一個位置", url: "topics/leetcode/problem-0034.html" },
            { title: "35. Search Insert Position 搜尋插入位置", url: "topics/leetcode/problem-0035.html" },
            { title: "36. Valid Sudoku 有效的數獨", url: "topics/leetcode/problem-0036.html" },
            { title: "37. Sudoku Solver 解數獨", url: "topics/leetcode/problem-0037.html" },
            { title: "38. Count and Say 外觀數列", url: "topics/leetcode/problem-0038.html" },
            { title: "39. Combination Sum 組合總和", url: "topics/leetcode/problem-0039.html" },
            { title: "40. Combination Sum II 組合總和 II", url: "topics/leetcode/problem-0040.html" },
            { title: "41. First Missing Positive 缺失的第一個正數", url: "topics/leetcode/problem-0041.html" },
            { title: "42. Trapping Rain Water 接雨水", url: "topics/leetcode/problem-0042.html" },
            { title: "43. Multiply Strings 字串相乘", url: "topics/leetcode/problem-0043.html" },
            { title: "44. Wildcard Matching 通配符匹配", url: "topics/leetcode/problem-0044.html" },
            { title: "45. Jump Game II 跳躍遊戲 II", url: "topics/leetcode/problem-0045.html" },
            { title: "46. Permutations 全排列", url: "topics/leetcode/problem-0046.html" },
            { title: "47. Permutations II 全排列 II", url: "topics/leetcode/problem-0047.html" },
            { title: "48. Rotate Image 旋轉圖像", url: "topics/leetcode/problem-0048.html" },
            { title: "49. Group Anagrams 字母異位詞分組", url: "topics/leetcode/problem-0049.html" },
            { title: "50. Pow(x, n) Pow(x, n)", url: "topics/leetcode/problem-0050.html" }
          ]
        },
        {
          title: "第 051–075 題",
          courses: [
            { title: "51. N-Queens N 皇后", url: "topics/leetcode/problem-0051.html" },
            { title: "52. N-Queens II N 皇后 II", url: "topics/leetcode/problem-0052.html" },
            { title: "53. Maximum Subarray 最大子陣列和", url: "topics/leetcode/problem-0053.html" },
            { title: "54. Spiral Matrix 螺旋矩陣", url: "topics/leetcode/problem-0054.html" },
            { title: "55. Jump Game 跳躍遊戲", url: "topics/leetcode/problem-0055.html" },
            { title: "56. Merge Intervals 合併區間", url: "topics/leetcode/problem-0056.html" },
            { title: "57. Insert Interval 插入區間", url: "topics/leetcode/problem-0057.html" },
            { title: "58. Length of Last Word 最後一個單詞的長度", url: "topics/leetcode/problem-0058.html" },
            { title: "59. Spiral Matrix II 螺旋矩陣 II", url: "topics/leetcode/problem-0059.html" },
            { title: "60. Permutation Sequence 排列序列", url: "topics/leetcode/problem-0060.html" },
            { title: "61. Rotate List 旋轉串列", url: "topics/leetcode/problem-0061.html" },
            { title: "62. Unique Paths 不同路徑", url: "topics/leetcode/problem-0062.html" },
            { title: "63. Unique Paths II 不同路徑 II", url: "topics/leetcode/problem-0063.html" },
            { title: "64. Minimum Path Sum 最小路徑和", url: "topics/leetcode/problem-0064.html" },
            { title: "65. Valid Number 有效數字", url: "topics/leetcode/problem-0065.html" },
            { title: "66. Plus One 加一", url: "topics/leetcode/problem-0066.html" },
            { title: "67. Add Binary 二進位求和", url: "topics/leetcode/problem-0067.html" },
            { title: "68. Text Justification 文字左右對齊", url: "topics/leetcode/problem-0068.html" },
            { title: "69. Sqrt(x) x 的平方根", url: "topics/leetcode/problem-0069.html" },
            { title: "70. Climbing Stairs 爬樓梯", url: "topics/leetcode/problem-0070.html" },
            { title: "71. Simplify Path 簡化路徑", url: "topics/leetcode/problem-0071.html" },
            { title: "72. Edit Distance 編輯距離", url: "topics/leetcode/problem-0072.html" },
            { title: "73. Set Matrix Zeroes 矩陣置零", url: "topics/leetcode/problem-0073.html" },
            { title: "74. Search a 2D Matrix 搜尋二維矩陣", url: "topics/leetcode/problem-0074.html" },
            { title: "75. Sort Colors 顏色分類", url: "topics/leetcode/problem-0075.html" }
          ]
        },
        {
          title: "第 076–100 題",
          courses: [
            { title: "76. Minimum Window Substring 最小覆蓋子串", url: "topics/leetcode/problem-0076.html" },
            { title: "77. Combinations 組合", url: "topics/leetcode/problem-0077.html" },
            { title: "78. Subsets 子集", url: "topics/leetcode/problem-0078.html" },
            { title: "79. Word Search 單詞搜索", url: "topics/leetcode/problem-0079.html" },
            { title: "80. Remove Duplicates from Sorted Array II 刪除有序陣列中的重複項 II", url: "topics/leetcode/problem-0080.html" },
            { title: "81. Search in Rotated Sorted Array II 搜尋旋轉排序陣列 II", url: "topics/leetcode/problem-0081.html" },
            { title: "82. Remove Duplicates from Sorted List II 刪除排序串列中的重複元素 II", url: "topics/leetcode/problem-0082.html" },
            { title: "83. Remove Duplicates from Sorted List 刪除排序串列中的重複元素", url: "topics/leetcode/problem-0083.html" },
            { title: "84. Largest Rectangle in Histogram 柱狀圖中最大的矩形", url: "topics/leetcode/problem-0084.html" },
            { title: "85. Maximal Rectangle 最大矩形", url: "topics/leetcode/problem-0085.html" },
            { title: "86. Partition List 分隔串列", url: "topics/leetcode/problem-0086.html" },
            { title: "87. Scramble String 擾亂字串", url: "topics/leetcode/problem-0087.html" },
            { title: "88. Merge Sorted Array 合併兩個有序陣列", url: "topics/leetcode/problem-0088.html" },
            { title: "89. Gray Code 格雷編碼", url: "topics/leetcode/problem-0089.html" },
            { title: "90. Subsets II 子集 II", url: "topics/leetcode/problem-0090.html" },
            { title: "91. Decode Ways 解碼方法", url: "topics/leetcode/problem-0091.html" },
            { title: "92. Reverse Linked List II 反轉串列 II", url: "topics/leetcode/problem-0092.html" },
            { title: "93. Restore IP Addresses 復原 IP 位址", url: "topics/leetcode/problem-0093.html" },
            { title: "94. Binary Tree Inorder Traversal 二元樹的中序走訪", url: "topics/leetcode/problem-0094.html" },
            { title: "95. Unique Binary Search Trees II 不同的二元搜尋樹 II", url: "topics/leetcode/problem-0095.html" },
            { title: "96. Unique Binary Search Trees 不同的二元搜尋樹", url: "topics/leetcode/problem-0096.html" },
            { title: "97. Interleaving String 交錯字串", url: "topics/leetcode/problem-0097.html" },
            { title: "98. Validate Binary Search Tree 驗證二元搜尋樹", url: "topics/leetcode/problem-0098.html" },
            { title: "99. Recover Binary Search Tree 復原二元搜尋樹", url: "topics/leetcode/problem-0099.html" },
            { title: "100. Same Tree 相同的樹", url: "topics/leetcode/problem-0100.html" }
          ]
        },
        {
          title: "第 101–125 題",
          courses: [
            { title: "101. Symmetric Tree 對稱二元樹", url: "topics/leetcode/problem-0101.html" },
            { title: "102. Binary Tree Level Order Traversal 二元樹的層序走訪", url: "topics/leetcode/problem-0102.html" },
            { title: "103. Binary Tree Zigzag Level Order Traversal 二元樹的鋸齒層序走訪", url: "topics/leetcode/problem-0103.html" },
            { title: "104. Maximum Depth of Binary Tree 二元樹的最大深度", url: "topics/leetcode/problem-0104.html" },
            { title: "105. Construct Binary Tree from Preorder and Inorder Traversal 從前序與中序走訪序列建構二元樹", url: "topics/leetcode/problem-0105.html" },
            { title: "106. Construct Binary Tree from Inorder and Postorder Traversal 從中序與後序走訪序列建構二元樹", url: "topics/leetcode/problem-0106.html" },
            { title: "107. Binary Tree Level Order Traversal II 二元樹的層序走訪 II", url: "topics/leetcode/problem-0107.html" },
            { title: "108. Convert Sorted Array to Binary Search Tree 將有序陣列轉換為二元搜尋樹", url: "topics/leetcode/problem-0108.html" },
            { title: "109. Convert Sorted List to Binary Search Tree 將有序鏈結串列轉換為二元搜尋樹", url: "topics/leetcode/problem-0109.html" },
            { title: "110. Balanced Binary Tree 平衡二元樹", url: "topics/leetcode/problem-0110.html" },
            { title: "111. Minimum Depth of Binary Tree 二元樹的最小深度", url: "topics/leetcode/problem-0111.html" },
            { title: "112. Path Sum 路徑總和", url: "topics/leetcode/problem-0112.html" },
            { title: "113. Path Sum II 路徑總和 II", url: "topics/leetcode/problem-0113.html" },
            { title: "114. Flatten Binary Tree to Linked List 二元樹展開為鏈結串列", url: "topics/leetcode/problem-0114.html" },
            { title: "115. Distinct Subsequences 不同的子序列", url: "topics/leetcode/problem-0115.html" },
            { title: "116. Populating Next Right Pointers in Each Node 填充每個節點的下一個右側節點指標", url: "topics/leetcode/problem-0116.html" },
            { title: "117. Populating Next Right Pointers in Each Node II 填充每個節點的下一個右側節點指標 II", url: "topics/leetcode/problem-0117.html" },
            { title: "118. Pascal's Triangle 楊輝三角", url: "topics/leetcode/problem-0118.html" },
            { title: "119. Pascal's Triangle II 楊輝三角 II", url: "topics/leetcode/problem-0119.html" },
            { title: "120. Triangle 三角形最小路徑和", url: "topics/leetcode/problem-0120.html" },
            { title: "121. Best Time to Buy and Sell Stock 買賣股票的最佳時機", url: "topics/leetcode/problem-0121.html" },
            { title: "122. Best Time to Buy and Sell Stock II 買賣股票的最佳時機 II", url: "topics/leetcode/problem-0122.html" },
            { title: "123. Best Time to Buy and Sell Stock III 買賣股票的最佳時機 III", url: "topics/leetcode/problem-0123.html" },
            { title: "124. Binary Tree Maximum Path Sum 二元樹中的最大路徑和", url: "topics/leetcode/problem-0124.html" },
            { title: "125. Valid Palindrome 驗證回文串", url: "topics/leetcode/problem-0125.html" }
          ]
        },
        {
          title: "第 126–150 題",
          courses: [
            { title: "126. Word Ladder II 單詞接龍 II", url: "topics/leetcode/problem-0126.html" },
            { title: "127. Word Ladder 單詞接龍", url: "topics/leetcode/problem-0127.html" },
            { title: "128. Longest Consecutive Sequence 最長連續序列", url: "topics/leetcode/problem-0128.html" },
            { title: "129. Sum Root to Leaf Numbers 求根節點到葉節點數字之和", url: "topics/leetcode/problem-0129.html" },
            { title: "130. Surrounded Regions 被圍繞的區域", url: "topics/leetcode/problem-0130.html" },
            { title: "131. Palindrome Partitioning 分割回文串", url: "topics/leetcode/problem-0131.html" },
            { title: "132. Palindrome Partitioning II 分割回文串 II", url: "topics/leetcode/problem-0132.html" },
            { title: "133. Clone Graph 複製圖", url: "topics/leetcode/problem-0133.html" },
            { title: "134. Gas Station 加油站", url: "topics/leetcode/problem-0134.html" },
            { title: "135. Candy 分發糖果", url: "topics/leetcode/problem-0135.html" },
            { title: "136. Single Number 只出現一次的數字", url: "topics/leetcode/problem-0136.html" },
            { title: "137. Single Number II 只出現一次的數字 II", url: "topics/leetcode/problem-0137.html" },
            { title: "138. Copy List with Random Pointer 複製帶隨機指標的鏈結串列", url: "topics/leetcode/problem-0138.html" },
            { title: "139. Word Break 單詞拆分", url: "topics/leetcode/problem-0139.html" },
            { title: "140. Word Break II 單詞拆分 II", url: "topics/leetcode/problem-0140.html" },
            { title: "141. Linked List Cycle 環形鏈結串列", url: "topics/leetcode/problem-0141.html" },
            { title: "142. Linked List Cycle II 環形鏈結串列 II", url: "topics/leetcode/problem-0142.html" },
            { title: "143. Reorder List 重排鏈結串列", url: "topics/leetcode/problem-0143.html" },
            { title: "144. Binary Tree Preorder Traversal 二元樹的前序走訪", url: "topics/leetcode/problem-0144.html" },
            { title: "145. Binary Tree Postorder Traversal 二元樹的後序走訪", url: "topics/leetcode/problem-0145.html" },
            { title: "146. LRU Cache LRU 快取", url: "topics/leetcode/problem-0146.html" },
            { title: "147. Insertion Sort List 對鏈結串列進行插入排序", url: "topics/leetcode/problem-0147.html" },
            { title: "148. Sort List 排序鏈結串列", url: "topics/leetcode/problem-0148.html" },
            { title: "149. Max Points on a Line 直線上最多的點數", url: "topics/leetcode/problem-0149.html" },
            { title: "150. Evaluate Reverse Polish Notation 逆波蘭表達式求值", url: "topics/leetcode/problem-0150.html" }
          ]
        },
        {
          title: "第 151–175 題",
          courses: [
            { title: "151. Reverse Words in a String 反轉字串中的單詞", url: "topics/leetcode/problem-0151.html" },
            { title: "152. Maximum Product Subarray 乘積最大子陣列", url: "topics/leetcode/problem-0152.html" },
            { title: "153. Find Minimum in Rotated Sorted Array 尋找旋轉排序陣列中的最小值", url: "topics/leetcode/problem-0153.html" },
            { title: "154. Find Minimum in Rotated Sorted Array II 尋找旋轉排序陣列中的最小值 II", url: "topics/leetcode/problem-0154.html" },
            { title: "155. Min Stack 最小堆疊", url: "topics/leetcode/problem-0155.html" },
            { title: "160. Intersection of Two Linked Lists 相交鏈結串列", url: "topics/leetcode/problem-0160.html" },
            { title: "162. Find Peak Element 尋找峰值", url: "topics/leetcode/problem-0162.html" },
            { title: "164. Maximum Gap 最大間距", url: "topics/leetcode/problem-0164.html" },
            { title: "165. Compare Version Numbers 比較版本號", url: "topics/leetcode/problem-0165.html" },
            { title: "166. Fraction to Recurring Decimal 分數到小數", url: "topics/leetcode/problem-0166.html" },
            { title: "167. Two Sum II - Input Array Is Sorted 兩數之和 II - 輸入有序陣列", url: "topics/leetcode/problem-0167.html" },
            { title: "168. Excel Sheet Column Title Excel 表欄位名稱", url: "topics/leetcode/problem-0168.html" },
            { title: "169. Majority Element 多數元素", url: "topics/leetcode/problem-0169.html" },
            { title: "171. Excel Sheet Column Number Excel 表欄位序號", url: "topics/leetcode/problem-0171.html" },
            { title: "172. Factorial Trailing Zeroes 階乘後的零", url: "topics/leetcode/problem-0172.html" },
            { title: "173. Binary Search Tree Iterator 二元搜尋樹迭代器", url: "topics/leetcode/problem-0173.html" },
            { title: "174. Dungeon Game 地下城遊戲", url: "topics/leetcode/problem-0174.html" }
          ]
        },
        {
          title: "第 176–200 題",
          courses: [
            { title: "179. Largest Number 最大數", url: "topics/leetcode/problem-0179.html" },
            { title: "187. Repeated DNA Sequences 重複的 DNA 序列", url: "topics/leetcode/problem-0187.html" },
            { title: "188. Best Time to Buy and Sell Stock IV 買賣股票的最佳時機 IV", url: "topics/leetcode/problem-0188.html" },
            { title: "189. Rotate Array 輪轉陣列", url: "topics/leetcode/problem-0189.html" },
            { title: "190. Reverse Bits 顛倒二進位位元", url: "topics/leetcode/problem-0190.html" },
            { title: "191. Number of 1 Bits 位元 1 的個數", url: "topics/leetcode/problem-0191.html" },
            { title: "198. House Robber 打家劫舍", url: "topics/leetcode/problem-0198.html" },
            { title: "199. Binary Tree Right Side View 二元樹的右視圖", url: "topics/leetcode/problem-0199.html" },
            { title: "200. Number of Islands 島嶼數量", url: "topics/leetcode/problem-0200.html" }
          ]
        }
      ]
    },
    {
      id: "resident-evil",
      category: "games",
      title: "惡靈古堡全紀錄：病毒、保護傘與三十年的生存恐怖",
      description:
        "從 1966 年非洲那朵始祖之花講起，完整拆解病毒族譜、保護傘公司與它的後繼組織，再一代一代講完 0 代到 8 代、代號維若妮卡與啟示錄的劇情（含各重製版的改動）；另有安德森真人電影六部曲、2021 重啟、Netflix 影集與 CG 動畫的故事，最後以完整時間線與「恐怖與動作的鐘擺」收束。",
      icon: "🧟",
      url: "topics/resident-evil/index.html",
      modules: [
        {
          title: "模組 A｜序幕：系列導覽與創作背景",
          courses: [
            { title: "惡靈古堡是什麼：Capcom、三上真司與 1996 年", url: "topics/resident-evil/lesson-01.html" },
            { title: "《Sweet Home》的血脈：生存恐怖如何誕生", url: "topics/resident-evil/lesson-02.html" },
            { title: "兩個名字：Biohazard 與 Resident Evil", url: "topics/resident-evil/lesson-03.html" },
            { title: "這門課怎麼讀：遊戲正史、外傳與電影的分層", url: "topics/resident-evil/lesson-04.html" },
          ],
        },
        {
          title: "模組 B｜設定①：病毒族譜",
          courses: [
            { title: "始祖病毒與始祖之花：一切的源頭", url: "topics/resident-evil/lesson-05.html" },
            { title: "T 病毒與它的變種", url: "topics/resident-evil/lesson-06.html" },
            { title: "G 病毒、T-Veronica 與 T-Abyss", url: "topics/resident-evil/lesson-07.html" },
            { title: "不是病毒的那些：寄生蟲、C 病毒、黴菌與 Cadou", url: "topics/resident-evil/lesson-08.html" },
          ],
        },
        {
          title: "模組 C｜設定②：保護傘公司與它的敵人",
          courses: [
            { title: "三位創辦人：史賓賽、馬可斯、艾許佛", url: "topics/resident-evil/lesson-09.html" },
            { title: "保護傘的組織結構與生化兵器產業", url: "topics/resident-evil/lesson-10.html" },
            { title: "保護傘倒台之後：BSAA、TerraSave、FBC 與「連結」", url: "topics/resident-evil/lesson-11.html" },
            { title: "模組總結：企業惡意作為系列的敘事引擎", url: "topics/resident-evil/lesson-12.html" },
          ],
        },
        {
          title: "模組 D｜前傳：惡靈古堡 0",
          courses: [
            { title: "始發列車：麗貝卡與比利", url: "topics/resident-evil/lesson-13.html" },
            { title: "馬可斯的復仇與水蛭女王", url: "topics/resident-evil/lesson-14.html" },
            { title: "模組總結：0 代在時間線上的位置", url: "topics/resident-evil/lesson-15.html" },
          ],
        },
        {
          title: "模組 E｜一代：洋館事件",
          courses: [
            { title: "S.T.A.R.S. 與阿爾發小隊：事件的開端", url: "topics/resident-evil/lesson-16.html" },
            { title: "史賓賽洋館的探索與 T 病毒的真相", url: "topics/resident-evil/lesson-17.html" },
            { title: "威斯克的背叛與暴君", url: "topics/resident-evil/lesson-18.html" },
            { title: "四個主角、四條路線與結局分歧", url: "topics/resident-evil/lesson-19.html" },
            { title: "2002 重製版：麗莎・特雷弗與新增的內容", url: "topics/resident-evil/lesson-20.html" },
          ],
        },
        {
          title: "模組 F｜二代：浣熊市的陷落",
          courses: [
            { title: "里昂與克萊兒：兩條交錯的路線", url: "topics/resident-evil/lesson-21.html" },
            { title: "警察局的構造與艾妲・王的目的", url: "topics/resident-evil/lesson-22.html" },
            { title: "威廉・柏金與 G 病毒", url: "topics/resident-evil/lesson-23.html" },
            { title: "雪莉・柏金與親子主題", url: "topics/resident-evil/lesson-24.html" },
            { title: "2019 重製版：改動、取捨與新的敘事", url: "topics/resident-evil/lesson-25.html" },
          ],
        },
        {
          title: "模組 G｜三代：最後的逃脫",
          courses: [
            { title: "吉兒・華倫泰與追跡者", url: "topics/resident-evil/lesson-26.html" },
            { title: "卡洛斯與傭兵部隊：另一個視角", url: "topics/resident-evil/lesson-27.html" },
            { title: "浣熊市的毀滅與政府的決定", url: "topics/resident-evil/lesson-28.html" },
            { title: "2020 重製版：被刪掉的內容與爭議", url: "topics/resident-evil/lesson-29.html" },
          ],
        },
        {
          title: "模組 H｜代號維若妮卡：艾許佛家的終局",
          courses: [
            { title: "洛克佛島與克萊兒的被捕", url: "topics/resident-evil/lesson-30.html" },
            { title: "艾弗雷德與艾希莉亞：雙生子的瘋狂", url: "topics/resident-evil/lesson-31.html" },
            { title: "T-Veronica 與南極基地", url: "topics/resident-evil/lesson-32.html" },
            { title: "模組總結：家族衰亡作為系列的另一條主題線", url: "topics/resident-evil/lesson-33.html" },
          ],
        },
        {
          title: "模組 I｜四代：歐洲村莊與寄生蟲",
          courses: [
            { title: "六年後的里昂：總統千金綁架案", url: "topics/resident-evil/lesson-34.html" },
            { title: "村莊、城堡、島嶼：三段式的舞台", url: "topics/resident-evil/lesson-35.html" },
            { title: "光明教會、薩德勒與寄生蟲的支配", url: "topics/resident-evil/lesson-36.html" },
            { title: "克勞薩、艾妲與威斯克的佈局", url: "topics/resident-evil/lesson-37.html" },
            { title: "遊戲設計的轉向：從恐怖到動作", url: "topics/resident-evil/lesson-38.html" },
            { title: "2023 重製版：敘事重寫與角色重塑", url: "topics/resident-evil/lesson-39.html" },
          ],
        },
        {
          title: "模組 J｜五代：非洲與威斯克的終局",
          courses: [
            { title: "克里斯與希娃：奇久州的任務", url: "topics/resident-evil/lesson-40.html" },
            { title: "吉兒的失蹤與洗腦", url: "topics/resident-evil/lesson-41.html" },
            { title: "尤洛波洛斯與威斯克的死", url: "topics/resident-evil/lesson-42.html" },
            { title: "模組總結：系列如何處理長期反派的收束", url: "topics/resident-evil/lesson-43.html" },
          ],
        },
        {
          title: "模組 K｜六代：四條戰線",
          courses: [
            { title: "四個劇本的結構與 C 病毒", url: "topics/resident-evil/lesson-44.html" },
            { title: "里昂與海倫娜：陶德市與總統之死", url: "topics/resident-evil/lesson-45.html" },
            { title: "克里斯與皮爾斯：中國與遂行部隊", url: "topics/resident-evil/lesson-46.html" },
            { title: "傑克與雪莉：威斯克之子", url: "topics/resident-evil/lesson-47.html" },
            { title: "艾妲線、卡菈・拉德梅斯與新保護傘", url: "topics/resident-evil/lesson-48.html" },
          ],
        },
        {
          title: "模組 L｜啟示錄系列",
          courses: [
            { title: "啟示錄：吉兒、女王芝諾比亞號與 T-Abyss", url: "topics/resident-evil/lesson-49.html" },
            { title: "啟示錄 2：克萊兒、摩伊拉與監視之島", url: "topics/resident-evil/lesson-50.html" },
            { title: "艾利克斯・威斯克與「第三種威斯克」", url: "topics/resident-evil/lesson-51.html" },
            { title: "模組總結：外傳如何補完主線的空白", url: "topics/resident-evil/lesson-52.html" },
          ],
        },
        {
          title: "模組 M｜七代：貝克一家",
          courses: [
            { title: "伊森・溫特斯與杜爾維的農莊", url: "topics/resident-evil/lesson-53.html" },
            { title: "貝克一家：傑克、瑪格麗特、路卡斯", url: "topics/resident-evil/lesson-54.html" },
            { title: "伊芙琳、黴菌與「E 型」的真相", url: "topics/resident-evil/lesson-55.html" },
            { title: "第一人稱的回歸：系列如何找回恐怖", url: "topics/resident-evil/lesson-56.html" },
            { title: "克里斯的登場與藍色保護傘", url: "topics/resident-evil/lesson-57.html" },
          ],
        },
        {
          title: "模組 N｜八代：村莊",
          courses: [
            { title: "三年後：蘿絲的誘拐與東歐村莊", url: "topics/resident-evil/lesson-58.html" },
            { title: "四大領主①：蒂米崔斯庫夫人的城堡", url: "topics/resident-evil/lesson-59.html" },
            { title: "四大領主②：貝內維恩托的人偶之家", url: "topics/resident-evil/lesson-60.html" },
            { title: "四大領主③：莫羅的水庫與海森堡的工廠", url: "topics/resident-evil/lesson-61.html" },
            { title: "米蘭達之母、巨型真菌與伊森的結局", url: "topics/resident-evil/lesson-62.html" },
            { title: "蘿絲的黃金線：DLC 與下一世代的預告", url: "topics/resident-evil/lesson-63.html" },
          ],
        },
        {
          title: "模組 O｜最新作與未來",
          courses: [
            { title: "惡靈古堡 Requiem：目前可以確定與尚待補充的部分", url: "topics/resident-evil/lesson-64.html" },
            { title: "系列的下一步：三條可能的路線", url: "topics/resident-evil/lesson-65.html" },
          ],
        },
        {
          title: "模組 P｜電影①：安德森真人電影六部曲",
          courses: [
            { title: "真人電影版的定位：為什麼要創造愛麗絲", url: "topics/resident-evil/lesson-66.html" },
            { title: "第一部（2002）：蜂巢與紅后", url: "topics/resident-evil/lesson-67.html" },
            { title: "第二部（2004）：啟示錄——浣熊市與追跡者", url: "topics/resident-evil/lesson-68.html" },
            { title: "第三、四部：大滅絕與陰陽界——荒漠、複製人與亞開迪亞", url: "topics/resident-evil/lesson-69.html" },
            { title: "第五、六部：天譴日與最終章——模擬設施與愛麗絲的身世", url: "topics/resident-evil/lesson-70.html" },
          ],
        },
        {
          title: "模組 Q｜電影②：重啟、影集與 CG 動畫",
          courses: [
            { title: "浣熊市：歡迎光臨（2021）：回到遊戲一二代", url: "topics/resident-evil/lesson-71.html" },
            { title: "Netflix 真人影集（2022）：改編的取捨與爭議", url: "topics/resident-evil/lesson-72.html" },
            { title: "CG 動畫三部曲：惡化、詛咒與血仇", url: "topics/resident-evil/lesson-73.html" },
            { title: "死亡之島（2023）與無限黑暗影集", url: "topics/resident-evil/lesson-74.html" },
          ],
        },
        {
          title: "模組 R｜橫向分析",
          courses: [
            { title: "完整時間線：從 1966 年到最新作", url: "topics/resident-evil/lesson-75.html" },
            { title: "病毒族譜全表與生化兵器圖鑑", url: "topics/resident-evil/lesson-76.html" },
            { title: "人物關係總表：S.T.A.R.S.、保護傘與 BSAA", url: "topics/resident-evil/lesson-77.html" },
            { title: "遊戲、電影與小說的正史分層", url: "topics/resident-evil/lesson-78.html" },
          ],
        },
        {
          title: "模組 S｜主題論",
          courses: [
            { title: "恐怖與動作的鐘擺：系列三十年的路線擺盪", url: "topics/resident-evil/lesson-79.html" },
            { title: "企業、政府與失控的科學", url: "topics/resident-evil/lesson-80.html" },
            { title: "重製版的意義：什麼該改、什麼不該改", url: "topics/resident-evil/lesson-81.html" },
          ],
        },
        {
          title: "模組 T｜課程總結",
          courses: [
            { title: "全課程總結與遊玩順序建議", url: "topics/resident-evil/lesson-82.html" },
          ],
        },
      ],
    },
    {
      id: "silent-hill",
      category: "games",
      title: "沈默之丘全解析：霧、罪與那座會回應你的小鎮",
      description:
        "從 Team Silent 與 1999 年講起，先建立小鎮的三層世界、教團的信仰與「怪物是症狀不是敵人」這套設計語法，再一代一代講完 1 到 4 代、西方工作室時期、P.T. 與 Silent Hill f 的劇情，另有三部電影的故事，最後以結局全表與心理恐怖的技藝收束。",
      icon: "🌫️",
      url: "topics/silent-hill/index.html",
      modules: [
        {
          title: "模組 A｜序幕：系列導覽與創作背景",
          courses: [
            { title: "沈默之丘是什麼：Konami、Team Silent 與 1999 年", url: "topics/silent-hill/lesson-01.html" },
            { title: "心理恐怖與生存恐怖：和惡靈古堡的分道揚鑣", url: "topics/silent-hill/lesson-02.html" },
            { title: "山岡晃的音樂與伊藤暢達的怪物設計", url: "topics/silent-hill/lesson-03.html" },
            { title: "這門課怎麼讀：正史、外傳與電影的分層", url: "topics/silent-hill/lesson-04.html" },
          ],
        },
        {
          title: "模組 B｜設定①：小鎮本身",
          courses: [
            { title: "沈默之丘這個地方：地理、歷史與觀光鎮的表皮", url: "topics/silent-hill/lesson-05.html" },
            { title: "霧之世界與裏世界：兩層現實的規則", url: "topics/silent-hill/lesson-06.html" },
            { title: "教團的信仰：神、聖母與太陽的光輪", url: "topics/silent-hill/lesson-07.html" },
            { title: "白色克勞蒂亞與 PTV：藥物、儀式與經濟", url: "topics/silent-hill/lesson-08.html" },
          ],
        },
        {
          title: "模組 C｜設定②：怪物的語法",
          courses: [
            { title: "怪物不是敵人，是症狀：象徵化的設計原則", url: "topics/silent-hill/lesson-09.html" },
            { title: "三角頭：為什麼它只屬於二代", url: "topics/silent-hill/lesson-10.html" },
            { title: "模組總結：這套語法在哪幾作成立、哪幾作失效", url: "topics/silent-hill/lesson-11.html" },
          ],
        },
        {
          title: "模組 D｜一代（1999）：哈利・梅森",
          courses: [
            { title: "失蹤的女兒：開場與小鎮的第一層", url: "topics/silent-hill/lesson-12.html" },
            { title: "艾蕾莎・吉爾斯派：七年前的火與儀式", url: "topics/silent-hill/lesson-13.html" },
            { title: "達莉亞、考夫曼與麗莎：三個大人的真相", url: "topics/silent-hill/lesson-14.html" },
            { title: "神的誕生與多重結局", url: "topics/silent-hill/lesson-15.html" },
            { title: "模組總結：一代確立了什麼", url: "topics/silent-hill/lesson-16.html" },
          ],
        },
        {
          title: "模組 E｜二代（2001）：詹姆斯・桑德蘭",
          courses: [
            { title: "死去三年的妻子寄來的信", url: "topics/silent-hill/lesson-17.html" },
            { title: "瑪麗與瑪莉亞：同一張臉的兩種存在", url: "topics/silent-hill/lesson-18.html" },
            { title: "安琪拉與艾迪：兩條平行的罪", url: "topics/silent-hill/lesson-19.html" },
            { title: "三角頭與「懲罰」的自我投射", url: "topics/silent-hill/lesson-20.html" },
            { title: "結局分歧：Leave、In Water、Maria 與其他", url: "topics/silent-hill/lesson-21.html" },
            { title: "2024 重製版：Bloober Team 的改編與評價", url: "topics/silent-hill/lesson-22.html" },
          ],
        },
        {
          title: "模組 F｜三代（2003）：希瑟・梅森",
          courses: [
            { title: "十七年後：購物中心與另一個世界", url: "topics/silent-hill/lesson-23.html" },
            { title: "希瑟＝雪柔＝艾蕾莎：身分的三重疊合", url: "topics/silent-hill/lesson-24.html" },
            { title: "克勞蒂亞、文森與教團的分裂", url: "topics/silent-hill/lesson-25.html" },
            { title: "神的降生與一代的正式收束", url: "topics/silent-hill/lesson-26.html" },
            { title: "模組總結：三代作為續篇的完成度", url: "topics/silent-hill/lesson-27.html" },
          ],
        },
        {
          title: "模組 G｜四代（2004）：亨利・湯森",
          courses: [
            { title: "被封住的房間：從公寓看出去的世界", url: "topics/silent-hill/lesson-28.html" },
            { title: "華特・蘇利文與二十一聖禮", url: "topics/silent-hill/lesson-29.html" },
            { title: "沈默之丘之外：本作與小鎮的關係", url: "topics/silent-hill/lesson-30.html" },
            { title: "模組總結：四代的爭議與再評價", url: "topics/silent-hill/lesson-31.html" },
          ],
        },
        {
          title: "模組 H｜西方工作室時期",
          courses: [
            { title: "Origins（2007）：崔維斯與一代的前史", url: "topics/silent-hill/lesson-32.html" },
            { title: "Homecoming（2008）：亞歷克斯與牧羊人之谷", url: "topics/silent-hill/lesson-33.html" },
            { title: "Shattered Memories（2009）：心理側寫與一代的重構", url: "topics/silent-hill/lesson-34.html" },
            { title: "Downpour（2012）：墨菲・潘德頓與贖罪", url: "topics/silent-hill/lesson-35.html" },
            { title: "Book of Memories 與其他外傳", url: "topics/silent-hill/lesson-36.html" },
            { title: "模組總結：為什麼這段時期普遍被認為走偏了", url: "topics/silent-hill/lesson-37.html" },
          ],
        },
        {
          title: "模組 I｜空白與復活",
          courses: [
            { title: "P.T. 與被取消的《Silent Hills》", url: "topics/silent-hill/lesson-38.html" },
            { title: "小島秀夫、吉勒摩・戴托羅與那條走廊", url: "topics/silent-hill/lesson-39.html" },
            { title: "2022 年的復活宣言：一次公布的所有企劃", url: "topics/silent-hill/lesson-40.html" },
            { title: "Ascension 與 The Short Message：兩次實驗", url: "topics/silent-hill/lesson-41.html" },
          ],
        },
        {
          title: "模組 J｜Silent Hill f（2025）",
          courses: [
            { title: "1960 年代的日本：戎ヶ丘與時代背景", url: "topics/silent-hill/lesson-42.html" },
            { title: "清水雛子與她的怪物", url: "topics/silent-hill/lesson-43.html" },
            { title: "竜騎士 07 的劇本與「美しさ」的主題", url: "topics/silent-hill/lesson-44.html" },
            { title: "模組總結：把小鎮搬離小鎮之後還成立嗎", url: "topics/silent-hill/lesson-45.html" },
          ],
        },
        {
          title: "模組 K｜電影①：沈默之丘（2006）",
          courses: [
            { title: "克里斯多福・甘斯的改編策略", url: "topics/silent-hill/lesson-46.html" },
            { title: "蘿絲、莎朗與艾蕾莎：電影版的故事", url: "topics/silent-hill/lesson-47.html" },
            { title: "電影與一代的異同：哪些改動是對的", url: "topics/silent-hill/lesson-48.html" },
          ],
        },
        {
          title: "模組 L｜電影②：啟示錄（2012）與重返（2026）",
          courses: [
            { title: "啟示錄：改編三代的得與失", url: "topics/silent-hill/lesson-49.html" },
            { title: "重返沈默之丘：甘斯回歸與二代的改編", url: "topics/silent-hill/lesson-50.html" },
            { title: "模組總結：為什麼沈默之丘特別難改編", url: "topics/silent-hill/lesson-51.html" },
          ],
        },
        {
          title: "模組 M｜橫向分析",
          courses: [
            { title: "完整時間線與作品關係圖", url: "topics/silent-hill/lesson-52.html" },
            { title: "怪物圖鑑與象徵對照表", url: "topics/silent-hill/lesson-53.html" },
            { title: "結局全表：每一作的所有結局與觸發條件", url: "topics/silent-hill/lesson-54.html" },
          ],
        },
        {
          title: "模組 N｜主題論",
          courses: [
            { title: "罪與罰：作品如何處理無法被原諒的事", url: "topics/silent-hill/lesson-55.html" },
            { title: "小鎮到底是什麼：三種解釋與它們的證據", url: "topics/silent-hill/lesson-56.html" },
            { title: "心理恐怖的技藝：聲音、留白與不解釋", url: "topics/silent-hill/lesson-57.html" },
          ],
        },
        {
          title: "模組 O｜課程總結",
          courses: [
            { title: "全課程總結與遊玩順序建議", url: "topics/silent-hill/lesson-58.html" },
          ],
        },
      ],
    },
    {
      id: "disney-animation",
      category: "fantasy",
      title: "迪士尼動畫正典：從白雪公主到星願的劇情全紀錄",
      description:
        "一部電影一堂課，依official「動畫正典」順序完整走過迪士尼動畫工作室從 1937《白雪公主》到最新作品的劇情、角色與幕後故事，依黃金時代、白銀時代、文藝復興、復興時代等歷史分期分組，戰時六部選集片合併一課概述，每一課都有完整劇情、主要角色表與一則幕後花絮或爭議說明。",
      icon: "🏰",
      url: "topics/disney-animation/index.html",
      modules: [
        {
          title: "模組 A｜黃金時代 Golden Age（1937–1942）",
          courses: [
            { title: "白雪公主 Snow White and the Seven Dwarfs（1937）", url: "topics/disney-animation/lesson-01.html" },
            { title: "木偶奇遇記 Pinocchio（1940）", url: "topics/disney-animation/lesson-02.html" },
            { title: "幻想曲 Fantasia（1940）", url: "topics/disney-animation/lesson-03.html" },
            { title: "小飛象 Dumbo（1941）", url: "topics/disney-animation/lesson-04.html" },
            { title: "小鹿斑比 Bambi（1942）", url: "topics/disney-animation/lesson-05.html" },
          ],
        },
        {
          title: "模組 B｜戰時選集片時期（1942–1949）",
          courses: [
            { title: "戰時選集片六部曲：致候吾友到伊老師與蟾蜍先生", url: "topics/disney-animation/lesson-06.html" },
          ],
        },
        {
          title: "模組 C｜白銀時代 Silver Age（1950–1967）",
          courses: [
            { title: "仙履奇緣 Cinderella（1950）", url: "topics/disney-animation/lesson-07.html" },
            { title: "愛麗絲夢遊仙境 Alice in Wonderland（1951）", url: "topics/disney-animation/lesson-08.html" },
            { title: "小飛俠彼得潘 Peter Pan（1953）", url: "topics/disney-animation/lesson-09.html" },
            { title: "小姐與流氓 Lady and the Tramp（1955）", url: "topics/disney-animation/lesson-10.html" },
            { title: "睡美人 Sleeping Beauty（1959）", url: "topics/disney-animation/lesson-11.html" },
            { title: "101 忠狗 One Hundred and One Dalmatians（1961）", url: "topics/disney-animation/lesson-12.html" },
            { title: "石中劍 The Sword in the Stone（1963）", url: "topics/disney-animation/lesson-13.html" },
            { title: "森林王子 The Jungle Book（1967）", url: "topics/disney-animation/lesson-14.html" },
          ],
        },
        {
          title: "模組 D｜青銅／黑暗時代（1970–1988）",
          courses: [
            { title: "貓兒歷險記 The Aristocats（1970）", url: "topics/disney-animation/lesson-15.html" },
            { title: "羅賓漢 Robin Hood（1973）", url: "topics/disney-animation/lesson-16.html" },
            { title: "小熊維尼歷險記 The Many Adventures of Winnie the Pooh（1977）", url: "topics/disney-animation/lesson-17.html" },
            { title: "救難小英雄 The Rescuers（1977）", url: "topics/disney-animation/lesson-18.html" },
            { title: "狐狸與獵狗 The Fox and the Hound（1981）", url: "topics/disney-animation/lesson-19.html" },
            { title: "黑神鍋傳奇 The Black Cauldron（1985）", url: "topics/disney-animation/lesson-20.html" },
            { title: "妙妙探 The Great Mouse Detective（1986）", url: "topics/disney-animation/lesson-21.html" },
            { title: "奧麗華歷險記 Oliver & Company（1988）", url: "topics/disney-animation/lesson-22.html" },
          ],
        },
        {
          title: "模組 E｜文藝復興時代 Renaissance（1989–1999）",
          courses: [
            { title: "小美人魚 The Little Mermaid（1989）", url: "topics/disney-animation/lesson-23.html" },
            { title: "救難小英雄澳洲歷險記 The Rescuers Down Under（1990）", url: "topics/disney-animation/lesson-24.html" },
            { title: "美女與野獸 Beauty and the Beast（1991）", url: "topics/disney-animation/lesson-25.html" },
            { title: "阿拉丁 Aladdin（1992）", url: "topics/disney-animation/lesson-26.html" },
            { title: "獅子王 The Lion King（1994）", url: "topics/disney-animation/lesson-27.html" },
            { title: "風中奇緣 Pocahontas（1995）", url: "topics/disney-animation/lesson-28.html" },
            { title: "鐘樓怪人 The Hunchback of Notre Dame（1996）", url: "topics/disney-animation/lesson-29.html" },
            { title: "大力士 Hercules（1997）", url: "topics/disney-animation/lesson-30.html" },
            { title: "花木蘭 Mulan（1998）", url: "topics/disney-animation/lesson-31.html" },
            { title: "泰山 Tarzan（1999）", url: "topics/disney-animation/lesson-32.html" },
          ],
        },
        {
          title: "模組 F｜實驗時代（1999–2008）",
          courses: [
            { title: "幻想曲 2000 Fantasia 2000（1999）", url: "topics/disney-animation/lesson-33.html" },
            { title: "恐龍 Dinosaur（2000）", url: "topics/disney-animation/lesson-34.html" },
            { title: "變身國王 The Emperor's New Groove（2000）", url: "topics/disney-animation/lesson-35.html" },
            { title: "亞特蘭提斯：失落的帝國 Atlantis: The Lost Empire（2001）", url: "topics/disney-animation/lesson-36.html" },
            { title: "星際寶貝 Lilo & Stitch（2002）", url: "topics/disney-animation/lesson-37.html" },
            { title: "星銀島 Treasure Planet（2002）", url: "topics/disney-animation/lesson-38.html" },
            { title: "熊的傳說 Brother Bear（2003）", url: "topics/disney-animation/lesson-39.html" },
            { title: "放牛吃草 Home on the Range（2004）", url: "topics/disney-animation/lesson-40.html" },
            { title: "四眼天雞 Chicken Little（2005）", url: "topics/disney-animation/lesson-41.html" },
            { title: "未來小子 Meet the Robinsons（2007）", url: "topics/disney-animation/lesson-42.html" },
            { title: "閃電狗 Bolt（2008）", url: "topics/disney-animation/lesson-43.html" },
          ],
        },
        {
          title: "模組 G｜復興時代 Revival（2009–2023）",
          courses: [
            { title: "公主與青蛙 The Princess and the Frog（2009）", url: "topics/disney-animation/lesson-44.html" },
            { title: "魔髮奇緣 Tangled（2010）", url: "topics/disney-animation/lesson-45.html" },
            { title: "小熊維尼 Winnie the Pooh（2011）", url: "topics/disney-animation/lesson-46.html" },
            { title: "無敵破壞王 Wreck-It Ralph（2012）", url: "topics/disney-animation/lesson-47.html" },
            { title: "冰雪奇緣 Frozen（2013）", url: "topics/disney-animation/lesson-48.html" },
            { title: "大英雄天團 Big Hero 6（2014）", url: "topics/disney-animation/lesson-49.html" },
            { title: "動物方城市 Zootopia（2016）", url: "topics/disney-animation/lesson-50.html" },
            { title: "海洋奇緣 Moana（2016）", url: "topics/disney-animation/lesson-51.html" },
            { title: "無敵破壞王 2：網路大暴走 Ralph Breaks the Internet（2018）", url: "topics/disney-animation/lesson-52.html" },
            { title: "冰雪奇緣 2 Frozen II（2019）", url: "topics/disney-animation/lesson-53.html" },
            { title: "尋龍使者 Raya and the Last Dragon（2021）", url: "topics/disney-animation/lesson-54.html" },
            { title: "魔法滿屋 Encanto（2021）", url: "topics/disney-animation/lesson-55.html" },
            { title: "奇異世界 Strange World（2022）", url: "topics/disney-animation/lesson-56.html" },
            { title: "星願 Wish（2023）", url: "topics/disney-animation/lesson-57.html" },
          ],
        },
        {
          title: "模組 H｜近期作品",
          courses: [
            { title: "動物方城市 2 Zootopia 2（2025）", url: "topics/disney-animation/lesson-58.html" },
          ],
        },
      ],
    },
    {
      id: "pixar-animation",
      category: "fantasy",
      title: "皮克斯動畫全紀錄：從玩具總動員到最新作品",
      description:
        "一部電影一堂課，依上映順序完整走過皮克斯動畫工作室從 1995《玩具總動員》到最新作品的劇情、角色與幕後故事，依草創期、黃金期、近十年三個階段分組，每一課都有完整劇情、主要角色表與一則幕後花絮或主題解析，與姊妹主題《迪士尼動畫正典》各自獨立收錄，方便日後分頭擴充。",
      icon: "💡",
      url: "topics/pixar-animation/index.html",
      modules: [
        {
          title: "模組 I｜草創期（1995–2004）",
          courses: [
            { title: "玩具總動員 Toy Story（1995）", url: "topics/pixar-animation/lesson-01.html" },
            { title: "蟲蟲危機 A Bug's Life（1998）", url: "topics/pixar-animation/lesson-02.html" },
            { title: "玩具總動員 2 Toy Story 2（1999）", url: "topics/pixar-animation/lesson-03.html" },
            { title: "怪獸電力公司 Monsters, Inc.（2001）", url: "topics/pixar-animation/lesson-04.html" },
            { title: "海底總動員 Finding Nemo（2003）", url: "topics/pixar-animation/lesson-05.html" },
            { title: "超人特攻隊 The Incredibles（2004）", url: "topics/pixar-animation/lesson-06.html" },
          ],
        },
        {
          title: "模組 J｜黃金期（2006–2015）",
          courses: [
            { title: "汽車總動員 Cars（2006）", url: "topics/pixar-animation/lesson-07.html" },
            { title: "料理鼠王 Ratatouille（2007）", url: "topics/pixar-animation/lesson-08.html" },
            { title: "瓦力 WALL-E（2008）", url: "topics/pixar-animation/lesson-09.html" },
            { title: "天外奇蹟 Up（2009）", url: "topics/pixar-animation/lesson-10.html" },
            { title: "玩具總動員 3 Toy Story 3（2010）", url: "topics/pixar-animation/lesson-11.html" },
            { title: "汽車總動員 2 Cars 2（2011）", url: "topics/pixar-animation/lesson-12.html" },
            { title: "勇敢傳說 Brave（2012）", url: "topics/pixar-animation/lesson-13.html" },
            { title: "怪獸大學 Monsters University（2013）", url: "topics/pixar-animation/lesson-14.html" },
            { title: "腦筋急轉彎 Inside Out（2015）", url: "topics/pixar-animation/lesson-15.html" },
            { title: "恐龍當家 The Good Dinosaur（2015）", url: "topics/pixar-animation/lesson-16.html" },
          ],
        },
        {
          title: "模組 K｜近十年（2016–2022）",
          courses: [
            { title: "海底總動員：多莉去哪兒 Finding Dory（2016）", url: "topics/pixar-animation/lesson-17.html" },
            { title: "汽車總動員 3 Cars 3（2017）", url: "topics/pixar-animation/lesson-18.html" },
            { title: "可可夜總會 Coco（2017）", url: "topics/pixar-animation/lesson-19.html" },
            { title: "超人特攻隊 2 Incredibles 2（2018）", url: "topics/pixar-animation/lesson-20.html" },
            { title: "玩具總動員 4 Toy Story 4（2019）", url: "topics/pixar-animation/lesson-21.html" },
            { title: "1/2 的魔法 Onward（2020）", url: "topics/pixar-animation/lesson-22.html" },
            { title: "靈魂急轉彎 Soul（2020）", url: "topics/pixar-animation/lesson-23.html" },
            { title: "路卡的夏天 Luca（2021）", url: "topics/pixar-animation/lesson-24.html" },
            { title: "青春變形記 Turning Red（2022）", url: "topics/pixar-animation/lesson-25.html" },
            { title: "光年正傳 Lightyear（2022）", url: "topics/pixar-animation/lesson-26.html" },
          ],
        },
        {
          title: "模組 L｜最新作品（2023–）",
          courses: [
            { title: "元素方城市 Elemental（2023）", url: "topics/pixar-animation/lesson-27.html" },
            { title: "腦筋急轉彎 2 Inside Out 2（2024）", url: "topics/pixar-animation/lesson-28.html" },
            { title: "艾利歐 Elio（2025）", url: "topics/pixar-animation/lesson-29.html" },
            { title: "最新動向：往後的皮克斯作品", url: "topics/pixar-animation/lesson-30.html" },
          ],
        },
      ],
    },
    {
      id: "dj-turntable",
      category: "music",
      title: "DJ 器材與轉盤原理：從黑膠物理到現場混音的完整拆解",
      description:
        "從黑膠溝槽如何刻錄聲音、唱頭怎麼把震動變回電訊號講起，一路拆解轉盤馬達、混音台訊號路徑、抓拍與刷碟兩大核心技巧，再到 CDJ、Timecode Vinyl、MIDI 控制器的數位化演進，最後收在效果器、現場臨場判斷與一套入門器材建議。",
      icon: "🎧",
      url: "topics/dj-turntable/index.html",
      modules: [
        {
          title: "模組 A｜序幕：DJ 文化與器材的演化",
          courses: [
            { title: "什麼是「打碟」：從嘻哈街頭到舞廳 DJ 台", url: "topics/dj-turntable/lesson-01.html" },
            { title: "器材演化史：從留聲機到 CDJ 與數位控制器", url: "topics/dj-turntable/lesson-02.html" },
            { title: "認識一套完整的 DJ 系統：訊號流程總覽圖", url: "topics/dj-turntable/lesson-03.html" },
          ],
        },
        {
          title: "模組 B｜黑膠唱片的物理原理",
          courses: [
            { title: "聲音怎麼被刻進一條螺旋溝槽", url: "topics/dj-turntable/lesson-04.html" },
            { title: "唱頭與唱針：怎麼把溝槽震動變回電訊號", url: "topics/dj-turntable/lesson-05.html" },
            { title: "RIAA 等化：為什麼黑膠訊號要先「等化」才能放大", url: "topics/dj-turntable/lesson-06.html" },
            { title: "轉速與直徑：33⅓、45 轉背後的取捨", url: "topics/dj-turntable/lesson-07.html" },
            { title: "黑膠的天敵：跳針、靜電與磨損", url: "topics/dj-turntable/lesson-08.html" },
          ],
        },
        {
          title: "模組 C｜唱盤機械結構",
          courses: [
            { title: "直驅 vs 皮帶驅動：兩種轉盤馬達設計", url: "topics/dj-turntable/lesson-09.html" },
            { title: "轉盤的心臟：扭力與抖動（Wow & Flutter）", url: "topics/dj-turntable/lesson-10.html" },
            { title: "唱臂與循軌：怎麼讓唱針精準地待在溝槽裡", url: "topics/dj-turntable/lesson-11.html" },
            { title: "止滑墊（Slipmat）與制動：手動介入唱盤運轉的關鍵", url: "topics/dj-turntable/lesson-12.html" },
            { title: "音高推桿（Pitch Fader）：怎麼微調轉速去對拍", url: "topics/dj-turntable/lesson-13.html" },
            { title: "Technics SL-1200：定義一個世代的傳奇轉盤", url: "topics/dj-turntable/lesson-14.html" },
          ],
        },
        {
          title: "模組 D｜混音台與訊號路徑",
          courses: [
            { title: "混音台的角色：訊號從哪裡進、從哪裡出", url: "topics/dj-turntable/lesson-15.html" },
            { title: "Phono vs Line：輸入端切換為什麼那麼重要", url: "topics/dj-turntable/lesson-16.html" },
            { title: "Channel EQ 與 Gain Staging：讓兩軌音量與音色一致", url: "topics/dj-turntable/lesson-17.html" },
            { title: "Crossfader 與 Line Fader：切歌的兩種手法", url: "topics/dj-turntable/lesson-18.html" },
            { title: "Cue 耳機系統：怎麼在吵雜舞池裡先「偷聽」下一首歌", url: "topics/dj-turntable/lesson-19.html" },
            { title: "VU 表與訊號健康：怎麼避免削波失真", url: "topics/dj-turntable/lesson-20.html" },
          ],
        },
        {
          title: "模組 E｜核心技巧①：抓拍與節奏對齊",
          courses: [
            { title: "BPM 是什麼：用數字量化音樂的節奏", url: "topics/dj-turntable/lesson-21.html" },
            { title: "Beatmatching by ear：用耳朵聽出兩首歌的節奏差", url: "topics/dj-turntable/lesson-22.html" },
            { title: "用 Pitch Fader 微調轉速的實戰邏輯", url: "topics/dj-turntable/lesson-23.html" },
            { title: "Phase 對齊：不只是速度一樣，拍點還要疊在一起", url: "topics/dj-turntable/lesson-24.html" },
            { title: "從漸入漸出到 Blend：混音的基本過渡手法", url: "topics/dj-turntable/lesson-25.html" },
          ],
        },
        {
          title: "模組 F｜核心技巧②：刷碟 Scratching",
          courses: [
            { title: "刷碟是什麼：Grandmaster Flash 與嘻哈 DJ 怎麼把「跳針」變成樂器", url: "topics/dj-turntable/lesson-26.html" },
            { title: "Baby Scratch 與 Forward/Backward Scratch：最基本的手部動作", url: "topics/dj-turntable/lesson-27.html" },
            { title: "Crossfader Scratch：手怎麼配合切換器做出節奏", url: "topics/dj-turntable/lesson-28.html" },
            { title: "Transform、Chirp、Flare：進階刷碟手法圖解", url: "topics/dj-turntable/lesson-29.html" },
            { title: "Battle DJ 文化：DMC 世界賽與刷碟競技", url: "topics/dj-turntable/lesson-30.html" },
          ],
        },
        {
          title: "模組 G｜數位化浪潮",
          courses: [
            { title: "CDJ 是什麼：怎麼用光碟／USB 模擬轉盤的手感", url: "topics/dj-turntable/lesson-31.html" },
            { title: "Jog Wheel：怎麼用一個轉輪同時模擬刷碟與快轉", url: "topics/dj-turntable/lesson-32.html" },
            { title: "Timecode Vinyl 與 DVS：怎麼用一張特製黑膠控制電腦裡的 MP3", url: "topics/dj-turntable/lesson-33.html" },
            { title: "rekordbox、Serato、Traktor：主流 DJ 軟體怎麼分工", url: "topics/dj-turntable/lesson-34.html" },
            { title: "MIDI 控制器：沒有轉盤也能打碟的另一條路", url: "topics/dj-turntable/lesson-35.html" },
            { title: "類比手感 vs 數位便利：業界的世代辯論", url: "topics/dj-turntable/lesson-36.html" },
          ],
        },
        {
          title: "模組 H｜效果器與現場演出",
          courses: [
            { title: "Echo、Filter、Reverb：DJ 效果器怎麼加進訊號鏈", url: "topics/dj-turntable/lesson-37.html" },
            { title: "Loop 與 Sampler：即時重組一段音樂", url: "topics/dj-turntable/lesson-38.html" },
            { title: "現場演出的臨場反應：怎麼讀舞池、抓氣氛", url: "topics/dj-turntable/lesson-39.html" },
            { title: "DJ Mix 怎麼被錄下來與直播", url: "topics/dj-turntable/lesson-40.html" },
          ],
        },
        {
          title: "模組 I｜總結與入門建議",
          courses: [
            { title: "該從黑膠、CDJ 還是控制器入門？新手決策框架", url: "topics/dj-turntable/lesson-41.html" },
            { title: "一套入門器材清單與預算分級", url: "topics/dj-turntable/lesson-42.html" },
            { title: "課程總結：從機械原理到現場演出的完整拼圖", url: "topics/dj-turntable/lesson-43.html" },
          ],
        },
      ],
    }
  ]
};
