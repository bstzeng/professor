# -*- coding: utf-8 -*-
"""macOS 課程:模組 C(找程式、開程式、裝程式)。"""
from mac_common import *

_NOTEPAD = svg(
    title(u"你要找的「記事本」:Mac 的文字工具"),
    box(20, 46, 190, 116, u"TextEdit", [u"最接近記事本", u"在「應用程式」裡", u"純文字或格式文字都行",
                                       u"（格式 →製作純文字）"], GREEN),
    box(225, 46, 190, 116, u"備忘錄 Notes", [u"隨手筆記最方便", u"自動儲存、跨裝置同步", u"可放清單、圖片",
                                          u"多數人日常首選"], BLUE),
    box(430, 46, 190, 116, u"其他選擇", [u"程式碼:免費的 VS Code", u"筆記:一堆免費 App", u"文書:Pages（免費）",
                                     u"或 Word"], ORANGE),
    T(320, 184, u"想要「開啟就打字」的純記事本感覺 → 用 TextEdit;想要「隨手記、自動存」→ 用備忘錄", 9.5, ACC),
    T(320, 208, u"TextEdit 預設會存成有格式的 .rtf;要純文字 .txt,選「格式 →製作純文字」", 9.5),
)

_SPOTLIGHT = svg(
    title(u"Spotlight:Mac 最強的「開始功能表」"),
    keys(240, 44, [(u"⌘", 44, ACC), (u"空白", 64, ACC)]),
    R(160, 100, 320, 34, ACC, "var(--surface)", 8, 1.5),
    T(180, 122, u"🔍", 13, MUTED, "start"), T(210, 122, u"備忘錄|", 12, TXT, "start"),
    T(320, 160, u"打幾個字,它幾乎瞬間找到:", 10, ACC),
    [T(320, 182 + i * 20, s, 9.5, MUTED) for i, s in enumerate([
        u"App(打「備忘」開備忘錄)、檔案、資料夾",
        u"檔案內的文字、郵件、聯絡人",
        u"算式(直接打 12*8)、單位換算、匯率、查字典"])],
    T(320, 262, u"這是 Mac 使用者最常用的動作:什麼都先按 ⌘空白 搜尋,比一層層點快太多", 9.5, ACC),
)

_DOCK = svg(
    title(u"Launchpad 與 Dock:擺放常用 App"),
    box(30, 46, 270, 108, u"Dock（螢幕下方那條）", [u"放常用 App 的架子", u"拖 App 圖示上去＝釘住", u"點一下就開",
                                             u"右邊放最小化的視窗、垃圾桶"], BLUE),
    box(340, 46, 270, 108, u"Launchpad", [u"像 iPhone 的 App 總覽", u"所有 App 一頁頁排開", u"用觸控板張開拇指四指開",
                                        u"或用 Spotlight 更快"], GREEN),
    T(320, 176, u"新手最實用:把每天用的 App 從 Launchpad 或 Spotlight 拖到 Dock,以後一點就開", 9.5, ACC),
    T(320, 200, u"Dock 上圖示下方有小點＝該 App 正在執行;可以調大小、位置、自動隱藏", 9.5),
)

_STORE = svg(
    title(u"兩種安裝來源"),
    box(30, 46, 270, 108, u"App Store", [u"Apple 官方商店", u"經過審核,較安全", u"一鍵安裝、自動更新",
                                       u"移除也很乾淨"], GREEN),
    box(340, 46, 270, 108, u"網路下載", [u".dmg / .pkg 自己裝", u"選擇更多(很多好軟體不在商店)", u"要自己確認來源可信",
                                     u"認明開發者、官方網站"], ORANGE),
    T(320, 176, u"優先用 App Store;商店沒有的,到「官方網站」下載,別從來路不明的地方抓", 9.5, ACC),
    T(320, 200, u"第一次開網路下載的 App,Mac 會確認「你確定要開嗎」(Gatekeeper 把關),正常軟體按開啟即可", 9.5),
)

_UNINSTALL = svg(
    title(u"移除 App:為什麼不是「解除安裝程式」"),
    box(30, 46, 270, 100, u"大部分 App", [u"App 是一包東西", u"直接拖到垃圾桶", u"＝移除",
                                       u"或 Launchpad 長按→刪除"], GREEN),
    box(340, 46, 270, 100, u"少數複雜軟體", [u"有附「解除安裝程式」", u"或用 .pkg 裝的", u"照它的方式移除",
                                        u"（驅動、防毒等）"], ORANGE),
    T(320, 172, u"因為 Mac 的 App 自成一包,丟垃圾桶就等於解除安裝,不必像 Windows 跑一個解除安裝精靈", 9.5, ACC),
    T(320, 196, u"殘留的設定檔通常很小、放在 Library,不影響使用;想徹底清乾淨可用專門的清理工具", 9.5),
)

_ALT = svg(
    title(u"Windows 常用軟體的 Mac 對應"),
    R(30, 40, 580, 24, LINE, "none", 4), T(150, 57, u"Windows", 10, BLUE), T(430, 57, u"Mac", 10, GREEN),
    [[T(60, 88 + i * 26, w, 9.5, TXT, "start"), T(350, 88 + i * 26, m, 9.5, TXT, "start")]
     for i, (w, m) in enumerate([
        (u"記事本 Notepad", u"TextEdit／備忘錄"),
        (u"檔案總管 Explorer", u"Finder"),
        (u"小畫家 Paint", u"預覽程式(可簡單標註)／免費繪圖 App"),
        (u"小算盤 Calculator", u"計算機(或直接在 Spotlight 打算式)"),
        (u"工作管理員 Task Manager", u"活動監視器"),
        (u"控制台 Control Panel", u"系統設定"),
        (u"命令提示字元 CMD", u"終端機 Terminal"),
        (u"小畫家截圖／剪取工具", u"⌘⇧4 截圖(內建)")])],
    T(320, 300, u"更完整的對照,見本主題的「Windows → Mac 對照速查表」參考頁", 9.5, ACC),
)

MODULES = [(u"模組 C｜找程式、開程式、裝程式", [

lesson(u"你要找的「記事本」:Mac 的內建文字工具",
  u"直接回答你的困惑:Mac 的記事本在哪?",
  [u"知道 Mac 有哪些內建文字工具",
   u"區分 TextEdit 與備忘錄的用途",
   u"知道純文字怎麼存"],
  [("p", u"你提到「在 Windows 用記事本記錄,在 Mac 找不到類似的」。這一課直接解決。"
        u"Mac 其實有好幾個對應的工具,只是名字和位置不同。"),
   ("FIGX", _NOTEPAD, "0 0 640 226", u"TextEdit 最接近記事本;備忘錄適合隨手記;還有很多其他選擇。"),
   ("h", u"1. TextEdit:最接近記事本"),
   ("p", u"<strong>TextEdit</strong> 在「<strong>應用程式</strong>」資料夾裡(或用 Spotlight 打「TextEdit」)。"
        u"它就是 Mac 內建的文字編輯器。有一個要注意的點:它預設會存成<strong>有格式的 .rtf</strong>,"
        u"如果你要像記事本那樣的<strong>純文字 .txt</strong>,在選單選「<strong>格式 →製作純文字</strong>」再存。"),
   ("h", u"2. 備忘錄:更方便的隨手記"),
   ("p", u"如果你只是想<strong>隨手記東西</strong>,更推薦內建的「<strong>備忘錄</strong>」App:"
        u"打開就能寫、<strong>自動儲存</strong>(不用按存檔)、還能跨 iPhone/iPad 同步,可以放清單、圖片、表格。"
        u"很多人日常筆記都用它。"),
   ("h", u"3. 其他選擇"),
   ("ul", [u"<strong>寫程式</strong>:裝免費的 <strong>VS Code</strong>(和 Windows 上一樣)。",
           u"<strong>正式文件</strong>:Mac 內建免費的 <strong>Pages</strong>(對應 Word),或裝 Word。",
           u"<strong>純筆記</strong>:App Store 有很多免費筆記 App。"]),
   ("p", u"所以「Mac 沒有記事本」是個誤會——它有,只是叫 TextEdit,而且你可能會更喜歡用備忘錄。"
        u"要快速打開任何一個,用 <strong>Spotlight</strong>(" + LS(15) + u")最快。")],
  u"按 ⌘＋空白鍵打開 Spotlight,打「textedit」按 Enter,TextEdit 就開了。試著在裡面選「格式 →製作純文字」,體驗一下純文字模式。",
  [u"Mac 上最接近記事本的內建程式是哪一個?",
   u"TextEdit 要存成純文字 .txt,要選什麼選單?",
   u"想隨手記、還能跨裝置同步,用哪個 App?"],
  fig=None),

lesson(u"Windows 常用軟體的 Mac 對應表",
  u"你在 Windows 慣用的那些小工具,在 Mac 都叫什麼",
  [u"對照常見 Windows 軟體的 Mac 版本",
   u"知道去哪找這些工具",
   u"建立「換名字」的習慣"],
  [("p", u"很多困擾其實只是「同一個工具換了名字」。這一課把 Windows 常用軟體對應到 Mac,"
        u"你會發現大部分東西 Mac 都有,只是叫法不同。"),
   ("FIGX", _ALT, "0 0 640 316", u"Windows 常用軟體與它們的 Mac 對應。"),
   ("h", u"1. 對照表"),
   ("t", [u"Windows", u"Mac", u"在哪找"],
    [[u"記事本", u"TextEdit／備忘錄", u"應用程式(" + LS(13) + u")"],
     [u"檔案總管", u"Finder", u"Dock 最左邊的藍笑臉(" + LS(7) + u")"],
     [u"小畫家", u"預覽程式(簡單標註)／繪圖 App", u"應用程式／App Store"],
     [u"小算盤", u"計算機", u"或直接在 Spotlight 打算式"],
     [u"工作管理員", u"活動監視器", u"應用程式 →工具程式(" + LS(39) + u")"],
     [u"控制台", u"系統設定", u"蘋果選單  →系統設定(" + LS(29) + u")"],
     [u"命令提示字元", u"終端機", u"應用程式 →工具程式(" + LS(38) + u")"],
     [u"剪取工具", u"⌘⇧4 截圖", u"內建快捷鍵(" + LS(20) + u")"]]),
   ("h", u"2. 怎麼找到它們"),
   ("p", u"這些內建工具大多在<strong>「應用程式」資料夾</strong>裡,比較底層的(活動監視器、終端機)在其中的"
        u"<strong>「工具程式」</strong>子資料夾。但最快的方法永遠是:<strong>按 ⌘空白,打名字</strong>(" + LS(15) + u")。"),
   ("h", u"3. 商業軟體多半也有 Mac 版"),
   ("p", u"Office(Word、Excel、PowerPoint)、Chrome、LINE、Zoom、Photoshop 等大牌軟體都有 Mac 版,"
        u"到官方網站或 App Store 下載即可。少數只有 Windows 的軟體,可以找 Mac 上的替代品,"
        u"或用虛擬機(進階,本課不深入)。"),
   ("p", u"完整的對照(含快捷鍵、名詞)整理在本主題的「Windows → Mac 對照速查表」,可以加入書籤隨時查。")],
  u"挑三個你在 Windows 最常用的軟體,用 Spotlight 找找看它們的 Mac 版或對應工具。大部分你都能立刻找到。",
  [u"Windows 的「工作管理員」在 Mac 叫什麼?",
   u"Windows 的「控制台」對應到 Mac 的什麼?",
   u"找這些內建工具最快的方法是什麼?"],
  fig=None),

lesson(u"Spotlight:什麼都用搜尋的「開始功能表」",
  u"學會這一個功能,你的 Mac 使用效率會直接翻倍",
  [u"學會叫出並使用 Spotlight",
   u"知道它能做的事遠不只找檔案",
   u"養成「先搜尋」的習慣"],
  [("p", u"如果這門課只能記一件事,就是這個:<strong>Spotlight</strong>。"
        u"它是 Mac 的「超級搜尋」,取代了 Windows 那種在開始功能表裡層層點的習慣。"),
   ("FIGX", _SPOTLIGHT, "0 0 640 285", u"按 ⌘＋空白鍵叫出 Spotlight,打字就能找到並執行幾乎任何東西。"),
   ("h", u"1. 怎麼用"),
   ("p", u"按 <strong>⌘＋空白鍵</strong>,螢幕中央跳出一個搜尋框,打幾個字,按 Enter 就執行。就這麼簡單。"),
   ("h", u"2. 它能做的事遠不只找檔案"),
   ("ul", [u"<strong>開 App</strong>:打「備忘」就跳出備忘錄,按 Enter 打開——比在 Launchpad 找快多了。",
           u"<strong>找檔案、資料夾</strong>,甚至<strong>檔案裡的文字</strong>。",
           u"<strong>當計算機</strong>:直接打 <code>12*8+5</code>,答案立刻出現。",
           u"<strong>單位/匯率換算</strong>:打 <code>100 usd</code>、<code>5 公里 英里</code>。",
           u"<strong>查字典、查天氣、查股價</strong>。"]),
   ("h", u"3. 養成「先搜尋」的習慣"),
   ("p", u"Windows 老手常反射性地去<strong>翻資料夾、找圖示</strong>。在 Mac,請改成反射性地<strong>按 ⌘空白</strong>:"),
   ("ul", [u"要開任何 App → ⌘空白打名字。",
           u"要找任何檔案 → ⌘空白打關鍵字。",
           u"要算個數、換個單位 → ⌘空白直接打。"]),
   ("p", u"這一個習慣的改變,會解決你之前大量「東西在哪」的困擾。"
        u"(小提醒:⌘空白預設也可能是切換輸入法的鍵,如果衝突,可到系統設定調整,見 " + LS(22) + u"。)")],
  u"現在就按 ⌘＋空白鍵,打「12*8」看它算出 96,再打一個 App 的名字按 Enter 打開它。接下來一週,強迫自己都用 Spotlight 開 App。",
  [u"叫出 Spotlight 的快捷鍵是什麼?",
   u"除了找檔案和開 App,Spotlight 還能做什麼?(舉兩個)",
   u"Windows 老手該把什麼反射動作換成「按 ⌘空白」?"],
  fig=None),

lesson(u"Launchpad 與 Dock:擺放常用 App 的兩種方式",
  u"除了搜尋,還有兩個地方放你的常用程式",
  [u"認識 Dock 的用途",
   u"認識 Launchpad",
   u"學會把常用 App 釘到 Dock"],
  [("p", u"Spotlight 適合<strong>快速開任何東西</strong>,但你每天用的那幾個 App,放在<strong>看得到、點得到</strong>的地方更方便。"
        u"Mac 有兩個地方:Dock 和 Launchpad。"),
   ("FIGX", _DOCK, "0 0 640 220", u"Dock 是螢幕下方的常用 App 架子;Launchpad 像 iPhone 的 App 總覽。"),
   ("h", u"1. Dock:螢幕下方那條"),
   ("p", u"<strong>Dock</strong> 是螢幕下方(或側邊)那條放 App 圖示的架子,類似 Windows 的工作列。"),
   ("ul", [u"點圖示就<strong>打開或切換</strong>到那個 App。",
           u"把 App 圖示<strong>拖到 Dock 上</strong>,就<strong>釘住</strong>了,以後常駐在那(拖出去放開就移除)。",
           u"Dock <strong>中間的分隔線右邊</strong>放最小化的視窗、最近用過的 App 和<strong>垃圾桶</strong>。",
           u"圖示<strong>下方有小點</strong>＝該 App 正在執行(" + LS(4) + u")。"]),
   ("h", u"2. Launchpad:所有 App 一次看"),
   ("p", u"<strong>Launchpad</strong> 像 iPhone 的主畫面,把<strong>所有 App</strong> 一頁頁大圖示排開。"
        u"用<strong>觸控板拇指加三指(或四指)捏合</strong>可以叫出來,或在 Dock/Spotlight 找它。"
        u"適合<strong>瀏覽</strong>你裝了哪些 App;但要<strong>快速開</strong>某個已知的 App,還是 Spotlight 最快。"),
   ("h", u"3. 建議的擺法"),
   ("p", u"把你<strong>每天必用</strong>的幾個 App(瀏覽器、郵件、備忘錄…)釘到 Dock,一點就開;"
        u"其他偶爾用的,用 Spotlight 叫出來就好,不必全塞進 Dock。"
        u"Dock 可以在系統設定裡調大小、位置、要不要自動隱藏。")],
  u"把你最常用的一個 App(例如瀏覽器)從 Spotlight 打開後,在 Dock 圖示上右鍵 →「選項 →保留在 Dock」,它就釘住了。以後一點就開。",
  [u"Dock 是什麼?類似 Windows 的什麼?",
   u"怎麼把一個 App 釘到 Dock 上?",
   u"要快速打開一個已知的 App,用 Dock、Launchpad 還是 Spotlight?"],
  fig=None),

lesson(u"App Store vs. 網路下載:兩種安裝來源與安全性",
  u"軟體要去哪裝?兩個來源,以及怎麼裝得安全",
  [u"區分 App Store 與網路下載",
   u"知道各自的優缺點",
   u"理解 Mac 的安裝安全把關"],
  [("p", u"在 Mac 裝軟體有兩條路:官方的 <strong>App Store</strong>,和從<strong>網路下載</strong>自己裝(就是 " + LS(10) + u"的 .dmg/.pkg)。"),
   ("FIGX", _STORE, "0 0 640 220", u"App Store 官方審核較安全;網路下載選擇多,但要自己確認來源。"),
   ("h", u"1. 兩種來源"),
   ("t", [u"", u"App Store", u"網路下載"],
    [[u"來源", u"Apple 官方商店", u"軟體的官方網站等"],
     [u"安全", u"經過審核,較安全", u"要自己確認來源可信"],
     [u"安裝", u"一鍵,自動更新", u"下載 .dmg/.pkg 自己裝"],
     [u"選擇", u"有限(有些好軟體不在商店)", u"多"]]),
   ("h", u"2. 安全把關:Gatekeeper"),
   ("p", u"Mac 有一道叫 <strong>Gatekeeper</strong> 的防線:第一次打開<strong>從網路下載的 App</strong> 時,"
        u"會跳出「這是從網路下載的,你確定要打開嗎?」正常軟體按<strong>「打開」</strong>即可。"
        u"這用到了 " + FMT(10, u"檔案格式課的「來自網路標記」與數位簽章") + u"的概念——確認軟體來源與完整性。"),
   ("h", u"3. 怎麼裝得安心"),
   ("ul", [u"<strong>優先用 App Store</strong>:最省事也最安全。",
           u"商店沒有的,到<strong>官方網站</strong>下載,別從搜尋結果的廣告或來路不明的網站抓。",
           u"看到「無法打開,因為來自未識別的開發者」,先確認你信任這個來源,再到<strong>系統設定 →隱私權與安全性</strong>按「仍要打開」。",
           u"不確定的檔案,別急著開(" + FMT(62, u"偽裝與惡意檔案") + u")。"]),
   ("p", u"養成從可信來源安裝的習慣,Mac 本身的把關再加上你的判斷,就能大幅降低中招的機會。")],
  u"打開 App Store(Dock 或 Spotlight),隨便搜一個你想要的免費 App,體驗一鍵安裝有多簡單。裝好的 App 會自動出現在 Launchpad。",
  [u"App Store 和網路下載,哪個通常比較安全?",
   u"第一次打開網路下載的 App 時,Mac 會做什麼?",
   u"商店裡沒有的軟體,應該去哪裡下載?"],
  fig=None),

lesson(u"移除 App:為什麼不是「解除安裝程式」",
  u"在 Mac 移除軟體,大多只要一個動作:丟垃圾桶",
  [u"理解 Mac 移除 App 的原理",
   u"學會正確移除 App",
   u"知道少數例外的處理"],
  [("p", u"Windows 移除軟體要跑「解除安裝程式」或去「新增/移除程式」。"
        u"Mac 大部分時候<strong>簡單得多</strong>——因為 App 是一包東西(" + LS(9) + u")。"),
   ("FIGX", _UNINSTALL, "0 0 640 216", u"大部分 App 直接丟垃圾桶就移除;少數複雜軟體有專屬解除方式。"),
   ("h", u"1. 大部分:丟垃圾桶就好"),
   ("p", u"因為一個 App 就是<strong>「應用程式」資料夾裡的一包東西</strong>,移除它只要:"),
   ("ul", [u"在「應用程式」裡找到那個 App,<strong>拖到垃圾桶</strong>(或右鍵 →移到垃圾桶)。",
           u"或在 <strong>Launchpad</strong> 裡<strong>長按</strong>圖示,等它抖動,點<strong>刪除</strong>(這招主要對 App Store 裝的有效)。",
           u"最後<strong>清空垃圾桶</strong>,就真的刪掉了。"]),
   ("h", u"2. 少數例外"),
   ("p", u"有些比較複雜的軟體(防毒、驅動程式、虛擬機、某些用 .pkg 裝的)會裝到系統多個位置,"
        u"它們通常<strong>附一個「解除安裝程式」</strong>,或在官網說明怎麼移除。這種就照它的方式來,別只是丟垃圾桶。"),
   ("h", u"3. 殘留的設定檔"),
   ("p", u"App 移除後,可能在 <code>Library</code> 裡留下一點<strong>設定檔</strong>(" + LS(12) + u"),"
        u"通常很小、不影響使用,也方便你之後重裝時保留設定。"
        u"如果想<strong>徹底清乾淨</strong>,可以用專門的移除工具(例如 AppCleaner 這類免費軟體),它會幫你把相關的殘留一起找出來刪掉。"),
   ("p", u"所以「Mac 怎麼解除安裝」的答案,大多數時候就是:<strong>拖到垃圾桶,清空</strong>。就這麼直接。")],
  u"如果你裝了不需要的 App,試著把它從「應用程式」拖到垃圾桶,再清空垃圾桶。感受一下 Mac 移除軟體有多乾脆。",
  [u"Mac 移除大部分 App 的方法是什麼?",
   u"為什麼不需要像 Windows 那樣跑解除安裝精靈?",
   u"哪種軟體移除時要特別照它的方式來?"],
  fig=None),
])]
