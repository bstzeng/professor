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
            { title: "狹義相對論公設與勞侖茲變換" },
            { title: "時空圖、同時性的相對性、時間膨脹與長度收縮" },
            { title: "四維向量與閔可夫斯基度規、不變區間" },
            { title: "相對論性能量動量、四維速度與四維加速度" }
          ]
        },
        {
          title: "模組 B｜數學基礎：張量分析與微分幾何",
          courses: [
            { title: "向量與對偶向量、指標記號與愛因斯坦求和約定" },
            { title: "座標變換與張量的嚴格定義" },
            { title: "度規張量、指標的升降" },
            { title: "流形是什麼：微分幾何的基本語言" },
            { title: "切空間、基底向量與座標卡" },
            { title: "協變導數與克里斯托費爾符號" },
            { title: "平行移動與測地線" },
            { title: "黎曼曲率張量：定義與幾何意義" },
            { title: "里奇張量、里奇純量、比安基恆等式" },
            { title: "愛因斯坦張量與它為何「散度為零」" }
          ]
        },
        {
          title: "模組 C｜廣義相對論的物理",
          courses: [
            { title: "等效原理（弱等效原理與強等效原理）" },
            { title: "測地線方程：重力如何變成「自由落體沿測地線走」" },
            { title: "牛頓極限：如何從 GR 還原出牛頓重力" },
            { title: "應力-能量張量：如何描述物質與能量的分布" },
            { title: "GR 中的守恆律" },
            { title: "愛因斯坦場方程式的推導與物理動機" },
            { title: "宇宙常數與真空場方程式" },
            { title: "線性化場方程式與量綱檢查" }
          ]
        },
        {
          title: "模組 D｜精確解與求解技巧",
          courses: [
            { title: "利用對稱性簡化 EFE：基靈向量" },
            { title: "Schwarzschild 解的推導" },
            { title: "Schwarzschild 幾何：視界與奇異點" },
            { title: "Schwarzschild 時空中的測地線：軌道與水星近日點進動" },
            { title: "光線偏折、重力透鏡、Shapiro 延遲" },
            { title: "Reissner–Nordström 與 Kerr 解概覽" },
            { title: "黑洞熱力學初探" },
            { title: "FRW 度規：宇宙學的時空設定" },
            { title: "Friedmann 方程式" },
            { title: "宇宙學模型：物質／輻射／暗能量主導的宇宙" }
          ]
        },
        {
          title: "模組 E｜現代應用與延伸",
          courses: [
            { title: "線性化重力與重力波的推導" },
            { title: "重力波偵測（LIGO）：物理量如何對應觀測訊號" },
            { title: "GPS 的相對論修正：GR 在日常科技中的實際應用" },
            { title: "數值相對論概覽：EFE 如何在電腦上被解" },
            { title: "微擾方法與後牛頓近似" },
            { title: "ADM 形式（初值問題）簡介" },
            { title: "總結課：完整重走一遍 EFE 推導 + 開放問題" }
          ]
        }
      ]
    }
  ]
};
