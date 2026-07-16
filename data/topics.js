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
            { title: "奧伯斯悖論：為什麼夜空是黑的" },
            { title: "哈伯定律與宇宙膨脹的發現" },
            { title: "大霹靂理論：時間線與三大關鍵證據" },
            { title: "宇宙微波背景輻射：宇宙的嬰兒照" },
            { title: "大霹靂核合成：輕元素從哪裡來" },
            { title: "宇宙暴脹：解決視界問題與平坦性問題" },
            { title: "暗能量與 ΛCDM 標準模型" },
            { title: "宇宙的命運：熱寂、大擠壓還是大撕裂" }
          ]
        },
        {
          title: "模組 G｜實戰應用",
          courses: [
            { title: "星圖與觀星：認識自己頭頂上的星空" },
            { title: "公民科學與天文新聞：怎麼參與真實研究、讀懂報導" },
            { title: "總結：還沒解決的大問題，以及怎麼持續追蹤宇宙研究" }
          ]
        }
      ]
    }
  ]
};
