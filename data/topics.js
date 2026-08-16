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
  topics: [
    {
      id: "guitar",
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
      title: "電子音樂製作：從合成器到完整編曲",
      description:
        "承接《創作樂理》的和聲與曲式基礎，這門課專注在電子音樂製作本身的技術知識：減法合成器怎麼從零打造聲音、取樣與節奏編程、主流流行／EDM編曲的段落語言（Intro/Build-up/Drop/Breakdown）、貝斯與側鏈壓縮、混音與母帶基礎，最後完成一趟從聲音設計到完整編曲的製作旅程。軟體無關，概念為主，並與《電子電路》課的濾波器、頻率響應知識互相銜接。",
      icon: "🎛️",
      url: "topics/music-production/index.html",
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
        }
      ]
    }
  ]
};
