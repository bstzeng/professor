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
            { title: "調號與五度圈：12 個大調的完整地圖" },
            { title: "關係大小調與平行大小調：一張調號、兩種心情" },
            { title: "五度圈的實用功能：和弦親疏、轉調距離一眼看出" },
            { title: "模組總結：聽出一首歌在什麼調——主音引力" }
          ]
        },
        {
          title: "模組 C｜和弦的構造",
          courses: [
            { title: "三和弦：大、小、增、減的堆疊邏輯" },
            { title: "大調順階和弦：I ii iii IV V vi vii° 的完整推導" },
            { title: "小調順階和弦：為什麼小調的 V 常常「借」大三度" },
            { title: "七和弦：maj7、7、m7、m7♭5 的構造與色彩" },
            { title: "轉位與斜線和弦：同一個和弦的不同重心" }
          ]
        },
        {
          title: "模組 D｜和聲進行的邏輯",
          courses: [
            { title: "和弦功能：主—下屬—屬，緊張與解決的引擎" },
            { title: "終止式：樂句怎麼收尾——正格、變格、假終止、半終止" },
            { title: "經典套路解剖（一）：I–V–vi–IV 與卡農進行" },
            { title: "經典套路解剖（二）：低音下行、12 小節藍調、小調套路" },
            { title: "和聲節奏：一小節換幾個和弦，決定歌的步伐" },
            { title: "模組總結：完整拆解三首經典歌的和聲骨架" }
          ]
        },
        {
          title: "模組 E｜替旋律配和弦",
          courses: [
            { title: "旋律與和弦的關係：和弦內音與非和弦音" },
            { title: "配和弦的完整流程：定調、找重拍音、選功能、試聽修正" },
            { title: "同一段旋律的多種配法：重配和聲入門" },
            { title: "經過音、掛留音、倚音：讓旋律離開和弦也好聽" },
            { title: "旋律寫作：動機、重複與變化的平衡" },
            { title: "實作課：從零開始替一段旋律完整配好和弦" }
          ]
        },
        {
          title: "模組 F｜色彩與進階和聲",
          courses: [
            { title: "副屬和弦（V/x）：向別的調借屬和弦" },
            { title: "借用和弦：從小調借來的 ♭VII、♭VI、iv" },
            { title: "sus2、sus4、add9：懸浮與加味" },
            { title: "延伸和弦：9、11、13 的爵士色盤" },
            { title: "轉調技巧：共同和弦轉調、直接轉調、副歌升 key" },
            { title: "調式（modes）：Dorian、Mixolydian 的色彩與流行應用" },
            { title: "模組總結：進階和聲的品味地圖" }
          ]
        },
        {
          title: "模組 G｜節奏、曲式與編曲",
          courses: [
            { title: "歌曲曲式：主歌、副歌、橋段的功能與能量曲線" },
            { title: "律動（groove）：同一組和弦，節奏一改歌就變了" },
            { title: "編曲分層思維：節奏組、和聲組、旋律組、填充" },
            { title: "前奏、間奏、尾奏的寫法" },
            { title: "動態與留白：編曲最常被忽略的維度" }
          ]
        },
        {
          title: "模組 H｜創作實戰",
          courses: [
            { title: "從和弦進行開始寫歌：完整流程示範" },
            { title: "從旋律開始寫歌：完整流程示範" },
            { title: "歌詞與旋律的咬合：斷句、重音與中文聲調" },
            { title: "課程總結：建立你自己的創作工作流程與檢查清單" }
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
    }
  ]
};
