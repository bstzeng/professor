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
    { id: "science", label: "物理與宇宙學", icon: "🔭" },
    { id: "life", label: "生活與實用知識", icon: "🧭" },
    { id: "wuxia", label: "武俠小說", icon: "🗡️" },
    { id: "fantasy", label: "奇幻文學與電影宇宙", icon: "📖" },
    { id: "games", label: "電玩遊戲世界觀", icon: "🎮" },
    { id: "mythology", label: "神話與傳說", icon: "🏺" }
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
        "為已有 Python 背景、想寫爬蟲的人設計。目標不是變成前端工程師，而是看懂一個網頁「資料從哪裡來、怎麼被瀏覽器組出來」——DOM 結構、CSS 選擇器與 XPath、JavaScript 語法與非同步請求、分頁與動態載入、追蹤JS算出來的神秘參數，一路橋接到 requests／Selenium／Playwright 的實戰選擇。全程搭配 Python 對照與可直接執行的程式碼練習區。",
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
        "從基礎數學出發的電子電路自學課程。從電壓電流的物理直覺開始，建立直流電路分析、微分方程（RC/RL）、複數與相量（交流電路）這些必要的數學工具箱，再深入濾波器、半導體元件、運算放大器、數位邏輯，最後用一系列麵包板實作專案（LED、交替閃爍電路、感測器、穩壓電源、音訊放大、馬達控制、警報電路）把理論變成動手做的能力。",
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
      id: "music-production",
      category: "music",
      title: "電子音樂製作：從合成器到完整編曲",
      description:
        "承接《創作樂理》的和聲與曲式基礎，這門課專注在電子音樂製作本身的技術知識：減法合成器怎麼從零打造聲音、取樣與節奏編程、主流流行／EDM編曲的段落語言（Intro/Build-up/Drop/Breakdown）、貝斯與側鏈壓縮、混音與母帶基礎，最後完成一趟從聲音設計到完整編曲的製作旅程。軟體無關，概念為主，並與《電子電路》課的濾波器、頻率響應知識互相銜接。",
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
        "完整獨立、自成一套的宇宙學課程：從歷史發展與觀測現象出發，自建廣義相對論工具箱（等效原理、張量、愛因斯坦場方程式），完整推導弗里德曼方程式，深入大霹靂核合成、宇宙微波背景輻射、標準模型早期宇宙時間線（含奈秒尺度的夸克膠子電漿）、暴脹理論的完整推導與證據、暗物質暗能量，最後誠實面對「大爆炸之前發生什麼」這個科學前沿的開放問題。全程完整推導，不省略證明過程。",
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
        "從零開始學習用Xcode、Swift與SpriteKit開發iOS遊戲，透過實作一款打磚塊風格的休閒益智遊戲，掌握場景管理、物理引擎、碰撞偵測與遊戲狀態機等核心概念，接著學會整合AdMob廣告（橫幅、插頁、獎勵型）與計算廣告收入，最後完整走過Apple Developer Program註冊、App Store Connect設定、審查指南與提交發布流程，成為能獨立把作品送上App Store的新手開發者。",
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
        "從安裝地端LLM執行工具Ollama開始，學會用它的API讓外部工具能夠呼叫地端模型，接著上手開源工作流平台n8n，把AI步驟串進信件、試算表、Slack、資料庫等既有系統，打造一套完整的自動化流程；並補齊RAG文件問答、AI Agent工具呼叫、排程自動化、錯誤處理、安全性與地端資源優化等關鍵主題，最終建立起一套資料全程留在自己環境裡的地端AI自動化系統。",
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
        "用比喻與圖解取代密集推導，淺顯易懂地認識超弦理論：從廣義相對論與量子力學的衝突出發，理解為什麼物理學家把點粒子換成一條會震動的弦、重力子如何從弦的震動模式裡「自動」冒出來、額外維度與卡拉比-丘流形是什麼、五種弦論如何被M理論統一、D-膜與全息原理AdS/CFT對應，最後誠實面對這個理論至今仍未被實驗證實的爭議與挑戰。不推導方程式，但邏輯鏈完整不簡化。",
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
        "橫跨六大文明的神話故事與人物深度詳解：希臘神話的奧林帕斯眾神與特洛伊戰爭、羅馬神話如何借用並改造希臘神話打造自己的建國起源、北歐神話的九界宇宙觀與諸神的黃昏、埃及神話的來世信仰與法老王權、中國神話從盤古女媧到玉皇大帝八仙的完整神系、日本神話記紀文本裡的天照大神與天皇起源，最後用比較神話學的視角，看六大體系共通的洪水、創世與英雄旅程母題。",
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
    }
  ]
};
