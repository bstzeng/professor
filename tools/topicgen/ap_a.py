# -*- coding: utf-8 -*-
"""套裝應用程式的架構：模組 A（組成）、B（介面怎麼運作）、C（文件與編輯）。"""
from sa_common import *

lesson = make_lesson("ap")

_STACK = svg(
    title(u"應用程式的分層架構"),
    layers([(u"介面層（Presentation）", u"視窗、按鈕、畫面：顯示與接收操作", BLUE),
            (u"應用層（Application）", u"使用情境：開檔、存檔、匯出、套用濾鏡", TEAL),
            (u"領域層（Domain）", u"核心概念與規則：文件、段落、圖層", PURPLE),
            (u"基礎設施層（Infrastructure）", u"檔案、資料庫、網路、作業系統 API", ORANGE)], y=44),
    T(320, 222, u"依賴方向由上往下；領域層不知道畫面長什麼樣，所以同一套核心可以配不同介面", 9.5, ACC),
)

_ROUTES = svg(
    title(u"三種開發路線"),
    box(14, 46, 196, 140, u"原生", [u"Swift／C#／C++", u"直接呼叫系統 UI", u"效能與整合最好", u"每個平台各寫一份"], BLUE),
    box(222, 46, 196, 140, u"跨平台框架", [u"Qt、Flutter、", u".NET MAUI、React Native", u"一份程式多平台", u"外觀與系統略有差異"], GREEN),
    box(430, 46, 196, 140, u"網頁技術（Electron 等）", [u"HTML／CSS／JS", u"網頁開發者就能寫", u"VS Code、Slack、Discord", u"記憶體與容量較大"], ORANGE),
    T(320, 210, u"選擇取決於團隊、效能需求與要支援的平台，沒有絕對的好壞", 9.5, ACC),
)

_TREE = svg(
    title(u"視窗裡的元件樹"),
    box(250, 36, 140, 30, u"Window", [], GRAY),
    box(60, 90, 140, 30, u"MenuBar", [], BLUE), box(250, 90, 140, 30, u"SplitView", [], BLUE), box(440, 90, 140, 30, u"StatusBar", [], BLUE),
    box(170, 146, 130, 30, u"FileTree", [], TEAL), box(340, 146, 130, 30, u"Editor", [], TEAL),
    box(340, 196, 130, 30, u"Scrollbar", [], GREEN),
    P("M320 66 V78 H130 V90 M320 78 V90 M320 78 H510 V90 M320 120 V134 H235 V146 M320 134 H405 V146 M405 176 V196", MUTED, sw=1.2),
    T(320, 248, u"版面配置由上往下傳遞「可用空間」，由下往上回報「需要的大小」", 9.5, ACC),
)

_MVC = svg(
    title(u"MVC：模型、視圖、控制器"),
    box(240, 40, 160, 56, u"模型（Model）", [u"資料與規則"], PURPLE),
    box(60, 150, 160, 56, u"視圖（View）", [u"顯示畫面"], BLUE),
    box(420, 150, 160, 56, u"控制器（Controller）", [u"處理操作"], GREEN),
    A(222, 178, 418, 178, MUTED), T(320, 172, u"使用者操作轉給控制器", 9, MUTED),
    A(500, 150, 400, 90, MUTED), T(470, 116, u"更新模型", 9, MUTED, "start"),
    A(240, 90, 140, 150, MUTED), T(170, 116, u"通知變更", 9, MUTED, "end"),
    T(320, 236, u"同一個模型可以有多個視圖（例如試算表的表格與圖表同時更新）", 9.5, ACC),
)

_MVVM = svg(
    title(u"MVVM：資料繫結讓視圖自動更新"),
    box(20, 70, 170, 70, u"View", [u"宣告：這個文字框", u"綁到 Name"], BLUE),
    box(235, 70, 170, 70, u"ViewModel", [u"Name、IsSaving", u"SaveCommand"], TEAL),
    box(450, 70, 170, 70, u"Model", [u"Customer", u"儲存規則"], PURPLE),
    P("M190 98 H233 M233 112 H190", GREEN, sw=2), T(212, 92, u"雙向繫結", 8.5, GREEN), A(405, 105, 448, 105, MUTED),
    T(320, 172, u"ViewModel 不認識任何按鈕或文字框，所以可以不開視窗就做單元測試", 9.5, ACC),
)

_FLUX = svg(
    title(u"單向資料流"),
    flow([u"動作 Action", u"更新函式 Reducer", u"狀態 State", u"畫面 View"], 70, 50, 20, 620, 14, [ORANGE, PURPLE, TEAL, BLUE]),
    P("M545 120 V150 H95 V122", MUTED, sw=1.3), A(95, 126, 95, 121, MUTED), T(320, 166, u"使用者操作產生新的動作", 9.5, MUTED),
    T(320, 196, u"狀態只能透過動作改變 → 任何時刻的畫面都能由「初始狀態＋動作序列」重現", 9.5, ACC),
)

_I18N = svg(
    title(u"多語系：程式碼裡不寫死文字"),
    box(20, 50, 190, 90, u"程式碼", [u"t(“menu.save”)"], BLUE),
    box(240, 50, 180, 90, u"語系檔", [u"zh-TW：儲存", u"en：Save", u"ja：保存"], ORANGE),
    box(450, 50, 170, 90, u"畫面", [u"依使用者語言", u"顯示對應文字"], GREEN),
    A(210, 95, 238, 95, MUTED), A(420, 95, 448, 95, MUTED),
    T(320, 170, u"還要考慮：日期與數字格式、由右到左的語言、文字長度不同造成的版面變化", 9.5, ACC),
)

_DOC = svg(
    title(u"文書軟體的文件模型（概念）"),
    box(260, 36, 120, 30, u"Document", [], PURPLE),
    box(80, 90, 120, 30, u"Section", [], BLUE), box(260, 90, 120, 30, u"Styles", [], GRAY), box(440, 90, 120, 30, u"Metadata", [], GRAY),
    box(20, 146, 110, 30, u"Paragraph", [], TEAL), box(150, 146, 110, 30, u"Table", [], TEAL),
    box(20, 200, 110, 30, u"Run「粗體」", [], GREEN), box(150, 200, 110, 30, u"Cell", [], GREEN),
    P("M320 66 V78 H140 V90 M320 78 V90 M320 78 H500 V90 M140 120 V134 H75 V146 M140 134 H205 V146 M75 176 V200 M205 176 V200", MUTED, sw=1.2),
    T(440, 170, u"畫面上的排版結果（換行、分頁）", 9.5, MUTED, "middle"), T(440, 186, u"是由模型「計算」出來的，不存在模型裡", 9.5, MUTED, "middle"),
)

_BUF = svg(
    title(u"三種文字緩衝區"),
    T(20, 50, u"Gap Buffer：游標處留一段空位", 10, TXT, "start"),
    cells(20, 58, [u"H", u"e", u"l", u"l", u"", u"", u"", u"", u"o", u"!"], 40, 24, [BLUE, BLUE, BLUE, BLUE, None, None, None, None, BLUE, BLUE]),
    T(450, 74, u"在游標處打字只是填空位", 9.5, MUTED, "start"),
    T(20, 116, u"Piece Table：原文唯讀＋新增緩衝＋片段表", 10, TXT, "start"),
    cells(20, 124, [u"原", u"原", u"新", u"新", u"原", u"原", u"原"], 40, 24, [BLUE, BLUE, ORANGE, ORANGE, BLUE, BLUE, BLUE]),
    T(320, 140, u"插入不搬動原文", 9.5, MUTED, "start"),
    T(20, 182, u"Rope：把文字切塊放在平衡樹裡", 10, TXT, "start"),
    C(140, 200, 8, PURPLE, "none"), C(110, 226, 8, PURPLE, "none"), C(170, 226, 8, PURPLE, "none"), P("M134 206 L116 220 M146 206 L164 220", MUTED, sw=1),
    T(220, 214, u"超大檔案中間插入也只需要 O(log n)", 9.5, MUTED, "start"),
)

_CLIP = svg(
    title(u"剪貼簿：同一份資料，多種格式"),
    box(20, 50, 170, 100, u"複製", [u"一段格式化文字"], BLUE),
    box(235, 40, 170, 120, u"剪貼簿", [u"text/plain", u"text/html", u"application/rtf", u"本程式內部格式"], ORANGE),
    box(450, 50, 170, 100, u"貼上", [u"記事本取純文字", u"Word 取 RTF／HTML"], GREEN),
    A(190, 100, 233, 100, MUTED), A(405, 100, 448, 100, MUTED),
    T(320, 188, u"由接收端挑選最豐富、自己看得懂的格式；拖放使用同樣的機制", 9.5, ACC),
)

_RECOVER = svg(
    title(u"安全存檔：先寫暫存檔，再一次取代"),
    flow([u"寫入 doc.tmp", u"確認寫完（fsync）", u"把 doc.tmp 改名為 doc"], 60, 50, 20, 620, 14, [ORANGE, TEAL, GREEN]),
    T(320, 140, u"改名在大多數檔案系統上是「原子」操作：要嘛是舊檔、要嘛是新檔，不會只寫一半", 9.5, ACC),
    T(320, 158, u"自動儲存另存在復原資料夾；程式當掉後下次啟動時詢問是否復原", 9.5, MUTED),
)

_VIRT = svg(
    title(u"虛擬化清單：一百萬列只建立看得到的那幾十列"),
    R(220, 40, 200, 160, BLUE, "none", 4, 2), T(430, 50, u"可見區域", 10, BLUE, "start"),
    [R(230, 46 + i * 22, 180, 18, MUTED, LINE, 2, 1, op=0.5) for i in range(7)],
    [T(320, 59 + i * 22, u"第 %d 列" % (5001 + i), 9.5, TXT) for i in range(7)],
    T(120, 60, u"第 1～5000 列", 10, MUTED), T(120, 76, u"（沒有元件，只有高度）", 9, MUTED),
    T(520, 180, u"第 5008～1000000 列", 10, MUTED), T(520, 196, u"（沒有元件）", 9, MUTED),
    T(320, 228, u"捲動時重複使用同一批列元件，只換內容；記憶體與速度都和總列數無關", 9.5, ACC),
)

_COLLAB = svg(
    title(u"協同編輯：兩人同時改同一份文件"),
    box(20, 46, 190, 100, u"A 在位置 0 插入「嗨」", [], BLUE), box(430, 46, 190, 100, u"B 刪除位置 3 的字", [], GREEN),
    box(225, 46, 190, 100, u"衝突怎麼辦？", [u"B 的「位置 3」", u"在 A 插入後", u"已經變成位置 4"], RED),
    T(320, 176, u"OT（操作轉換）：伺服器依序轉換彼此的操作；CRDT：資料結構本身保證合併結果一致", 9.5, ACC),
    T(320, 194, u"Google 文件以 OT 聞名；Figma、許多新工具採用 CRDT 或其變形", 9.5, MUTED),
)

EVQ = {"t": "evq", "q": u"<b>事件迴圈模擬</b>：產生事件，觀察主執行緒如何一個一個處理。"}

MODULES = [
(u"模組 A｜一個應用程式由什麼組成", [

lesson(u"從畫面到程式的層次",
  u"按下「儲存」之後發生什麼事",
  [u"理解應用程式的層次",
   u"追蹤一個操作的完整路徑",
   u"認識本主題的學習地圖"],
  [steps([(u"使用者按下「儲存」", u"作業系統把滑鼠點擊送進應用程式的事件佇列。", 0),
          (u"介面層收到點擊", u"按鈕元件觸發 <code>onClick</code>，呼叫「儲存」命令。", 1),
          (u"應用層執行命令", u"檢查文件是否有檔名、是否需要另存新檔。", 2),
          (u"領域層序列化文件", u"把文件模型轉成檔案格式的位元組。", 3),
          (u"基礎設施層寫檔", u"透過作業系統 API 安全地寫入磁碟。", 4),
          (u"回報結果", u"標題列的「未儲存」記號消失，狀態列顯示「已儲存」。", [1, 0])],
         u"<b>按下「儲存」的旅程</b>", [u"作業系統", u"介面層", u"應用層", u"領域層", u"基礎設施層"]),
   ("h", u"學習地圖"),
   ("t", [u"模組", u"內容"],
         [[u"A", u"分層、技術路線"], [u"B", u"介面：事件迴圈、MVC／MVVM、非同步"], [u"C", u"文件：資料結構、復原重做、檔案、協同"],
          [u"D", u"外掛、指令、設定、主題、腳本"], [u"E", u"資料庫、網路、授權、安全、隱私"], [u"F", u"專案結構、測試、封裝、更新、當機回報、效能"],
          [u"G", u"拆解文字編輯器、繪圖軟體、聊天軟體"]]),
  ],
  u"一個簡單的操作會穿過介面、應用、領域、基礎設施多個層次；架構就是安排這些層次的責任。",
  [u"按下「儲存」會經過哪些層？",
   u"為什麼要把寫檔放在基礎設施層？",
   u"本主題有哪幾個模組？"]),

lesson(u"分層架構",
  u"每一層只做自己的事",
  [u"認識四層架構",
   u"理解依賴方向",
   u"知道分層帶來的好處"],
  [fig(_STACK, 232, u"應用程式的分層。"),
   code(u"""// 領域層：不認識任何 UI 或檔案系統
class Document {
  paragraphs: Paragraph[] = [];
  insertText(pos: Position, text: string) { /* 規則 */ }
}

// 應用層：協調使用情境，透過介面依賴基礎設施
class SaveDocument {
  constructor(private storage: Storage) {}
  async run(doc: Document, path: string) {
    await this.storage.write(path, serialize(doc));
  }
}"""),
   ("h", u"好處"),
   ("ul", [u"<strong>可測試</strong>：領域層可以不開視窗、不碰磁碟就測試。",
           u"<strong>可替換</strong>：換掉 UI 框架或儲存方式，核心不用改。",
           u"<strong>好分工</strong>：不同的人負責不同層。"]),
  ],
  u"分層讓每層只承擔一種責任，依賴由上往下，核心邏輯不受 UI 與技術細節影響。",
  [u"四層各負責什麼？",
   u"為什麼領域層不應該認識 UI？",
   u"分層對測試有什麼幫助？"]),

lesson(u"原生、跨平台、網頁技術",
  u"三種開發路線的取捨",
  [u"認識三種開發路線",
   u"比較它們的優缺點",
   u"知道知名軟體的選擇"],
  [fig(_ROUTES, 222, u"三種開發路線。"),
   ("t", [u"軟體", u"路線（大致）"],
         [[u"Photoshop、Office（桌面版）", u"原生 C++ 為主，各平台有專屬層"], [u"VS Code、Slack、Discord", u"Electron（網頁技術＋Node.js）"],
          [u"許多工業與科學軟體", u"Qt（C++ 跨平台）"], [u"Apple 自家 App", u"原生 Swift／SwiftUI"]]),
   ("p", u"不論哪條路線，前一課的分層原則都適用：Electron 程式同樣可以把核心邏輯寫成與 UI 無關的模組。"),
  ],
  u"原生效能最好、跨平台框架一份多用、網頁技術開發最快；要依需求與團隊選擇。",
  [u"Electron 的優缺點是什麼？",
   u"為什麼大型專業軟體多用原生？",
   u"跨平台框架和網頁技術有什麼不同？"]),

lesson(u"三個案例預覽",
  u"文字編輯器、繪圖軟體、聊天軟體",
  [u"認識三種典型應用的架構重點",
   u"建立後續課程的參考點",
   u"理解不同應用的不同挑戰"],
  [("t", [u"應用", u"核心資料", u"最大的挑戰", u"詳見"],
         [[u"文字編輯器（VS Code 類）", u"文字緩衝區", u"大檔案、即時語法分析、外掛", LS(38)],
          [u"繪圖軟體（Photoshop 類）", u"圖層、像素、操作歷史", u"記憶體、效能、非破壞性編輯", LS(39)],
          [u"聊天軟體（LINE 桌面版類）", u"訊息、對話、帳號", u"同步、離線、安全、通知", LS(40)]]),
   ("p", u"後面每學到一個概念，都可以想想：它在這三種軟體裡分別怎麼用？"),
  ],
  u"不同的應用有不同的核心資料與挑戰，但都建立在相同的架構原則上。",
  [u"文字編輯器的核心資料是什麼？",
   u"繪圖軟體最大的挑戰是什麼？",
   u"聊天軟體為什麼特別重視同步？"]),
]),

(u"模組 B｜介面怎麼運作", [

lesson(u"事件迴圈",
  u"程式大部分時間都在「等」",
  [u"理解事件驅動的程式",
   u"認識事件迴圈的結構",
   u"體驗主執行緒被卡住"],
  [code(u"""// 所有桌面 UI 框架的核心都是這樣一個迴圈（概念）
while (true) {
    Event e = WaitForEvent();     // 沒事就睡覺，不耗 CPU
    if (e.type == Quit) break;
    Dispatch(e);                  // 交給對應的元件處理
}"""),
   widget(EVQ),
   ("p", u"和遊戲迴圈（" + XL("ga", 5) + u"）相比，事件迴圈在沒有事件時會「睡著」，所以文書軟體閒置時幾乎不用 CPU。"),
   ("p", u"重點：<strong>所有事件都在同一條主執行緒上依序處理</strong>。只要某個事件處理太久，後面的事件（包括重繪畫面）全部排隊——視窗就變成「沒有回應」。"),
  ],
  u"事件迴圈逐一處理事件；任何耗時工作都會卡住整個介面。",
  [u"事件迴圈和遊戲迴圈有什麼不同？",
   u"為什麼一個慢的事件會讓整個視窗沒有回應？",
   u"閒置時事件迴圈在做什麼？"]),

lesson(u"視窗、元件樹與版面配置",
  u"畫面是一棵樹",
  [u"理解元件樹",
   u"認識版面配置的兩個階段",
   u"知道事件如何在樹中傳遞"],
  [fig(_TREE, 258, u"元件樹。"),
   ("ul", [u"<strong>量測與配置</strong>：父元件告訴子元件可用空間，子元件回報需要的大小，最後父元件決定每個子元件的位置。",
           u"<strong>繪製</strong>：由根往下，每個元件畫自己的區域；只有「髒」的區域需要重畫。",
           u"<strong>事件傳遞</strong>：點擊先找到最底層被點到的元件，再一路往上「冒泡」，任何一層都可以處理或攔截。"]),
   ("p", u"網頁的 DOM、iOS 的 UIView、Android 的 View、Qt 的 QWidget 都是同樣的樹狀結構。"),
  ],
  u"介面是元件樹：配置由上而下、尺寸由下而上回報，事件從被點到的元件往上冒泡。",
  [u"版面配置的兩個階段是什麼？",
   u"什麼是事件冒泡？",
   u"為什麼只重畫「髒」的區域？"]),

lesson(u"MVC：模型、視圖、控制器",
  u"資料和畫面分開",
  [u"理解 MVC 的三個角色",
   u"知道 MVC 解決的問題",
   u"認識 MVC 的變形"],
  [fig(_MVC, 248, u"MVC 的三個角色。"),
   code(u"""class CounterModel {             // Model：資料與規則
  count = 0; listeners: (() => void)[] = [];
  increment() { this.count++; this.listeners.forEach(f => f()); }
}
class CounterView {              // View：只負責顯示
  render(m: CounterModel) { label.text = `次數：${m.count}`; }
}
button.onClick = () => model.increment();   // Controller：把操作轉成模型呼叫"""),
   ("p", u"MVC 最大的價值：<strong>同一份資料可以有多個畫面</strong>，而且資料規則不會散落在按鈕事件裡。實務上很多框架把 View 和 Controller 合併，例如 iOS 的 ViewController。"),
  ],
  u"MVC 把資料（Model）、顯示（View）、操作（Controller）分開，讓同一份資料能驅動多個畫面。",
  [u"MVC 的三個角色各負責什麼？",
   u"為什麼不把資料直接放在按鈕事件裡？",
   u"「多個視圖共用模型」有什麼例子？"]),

lesson(u"MVP、MVVM 與資料繫結",
  u"讓畫面自動跟著資料走",
  [u"理解 MVVM 與資料繫結",
   u"比較 MVC、MVP、MVVM",
   u"知道 ViewModel 的可測試性"],
  [fig(_MVVM, 184, u"MVVM 與資料繫結。"),
   ("t", [u"模式", u"中間層", u"特點"],
         [[u"MVC", u"Controller", u"控制器處理輸入；視圖可直接讀模型"], [u"MVP", u"Presenter", u"Presenter 透過介面「命令」被動的視圖"],
          [u"MVVM", u"ViewModel", u"視圖透過繫結自動同步，ViewModel 不知道視圖存在"]]),
   code(u"""// ViewModel：純資料與命令
class EditorVM {
  title = observable("未命名");
  isDirty = observable(false);
  save = command(async () => { await doc.save(); this.isDirty.set(false); });
}
// View（宣告式）：<Label text={vm.title} />  <Button onClick={vm.save} disabled={!vm.isDirty} />"""),
  ],
  u"MVVM 透過資料繫結讓視圖自動更新；ViewModel 不依賴視圖，容易測試。",
  [u"資料繫結是什麼？",
   u"MVP 和 MVVM 的差別在哪？",
   u"為什麼 ViewModel 容易做單元測試？"]),

lesson(u"單向資料流",
  u"狀態只能由動作改變",
  [u"理解單向資料流",
   u"認識 Redux／Elm 架構",
   u"知道它的優缺點"],
  [fig(_FLUX, 210, u"單向資料流。"),
   code(u"""type Action = { type: "add"; text: string } | { type: "toggle"; id: number };

function reducer(state: Todo[], a: Action): Todo[] {   // 純函式：舊狀態＋動作 → 新狀態
  switch (a.type) {
    case "add":    return [...state, { id: Date.now(), text: a.text, done: false }];
    case "toggle": return state.map(t => t.id === a.id ? { ...t, done: !t.done } : t);
  }
}"""),
   ("ul", [u"優點：狀態變化可追蹤、可重播；除錯工具能「時光倒流」。",
           u"優點：天然支援復原（保存舊狀態即可，見 " + LS(14) + u"）。",
           u"缺點：簡單功能也要寫動作與更新函式，樣板程式碼較多。"]),
  ],
  u"單向資料流讓狀態只能透過動作改變，畫面是狀態的函數；可預測、可重播。",
  [u"什麼是純函式？",
   u"單向資料流對除錯有什麼幫助？",
   u"單向資料流的缺點是什麼？"]),

lesson(u"主執行緒為什麼不能卡",
  u"背景工作與非同步",
  [u"理解主執行緒的限制",
   u"學會把工作移到背景",
   u"認識 async／await"],
  [widget(dict(EVQ, q=u"<b>再試一次</b>：先按「重運算」，再打開「放到背景執行緒」比較差異。")),
   code(u"""// ❌ 在主執行緒讀大檔：讀檔期間整個視窗凍結
const data = fs.readFileSync("huge.psd");

// ✅ 非同步：等待期間事件迴圈繼續處理其他事件
const data = await fs.promises.readFile("huge.psd");

// ✅ CPU 密集運算：交給背景執行緒（Worker）
const worker = new Worker("filter.js");
worker.postMessage(pixels);
worker.onmessage = e => showResult(e.data);   // 結果回到主執行緒再更新畫面"""),
   ("h", u"兩條規則"),
   ("ol", [u"耗時的 I/O（讀檔、網路）用非同步。",
           u"耗時的運算（影像處理、壓縮）用背景執行緒。",
           u"<strong>只有主執行緒可以碰 UI 元件</strong>（大多數框架的規定）；背景工作完成後要「回到」主執行緒更新畫面。"]),
   ("p", u"執行緒與同步的底層原理，見 " + XL("os", 30) + u"。"),
  ],
  u"主執行緒只做 UI；I/O 用非同步、運算用背景執行緒，完成後再回主執行緒更新畫面。",
  [u"非同步和多執行緒有什麼不同？",
   u"為什麼背景執行緒不能直接改 UI？",
   u"什麼工作應該放到背景執行緒？"]),

lesson(u"無障礙、深色模式與多語系",
  u"一開始就要放進架構",
  [u"理解無障礙的架構需求",
   u"知道主題切換的設計",
   u"認識多語系的做法"],
  [fig(_I18N, 190, u"多語系的基本做法。"),
   ("t", [u"需求", u"架構上的做法"],
         [[u"螢幕報讀器", u"每個元件提供名稱、角色、狀態（無障礙樹）"], [u"鍵盤操作", u"焦點順序、所有功能都有鍵盤路徑"],
          [u"深色模式", u"顏色用「語意名稱」（背景、強調色），不寫死色碼"], [u"字體放大", u"版面用相對單位，能隨字體伸縮"],
          [u"多語系", u"文字放在語系檔；日期、數字、貨幣用地區化函式"]]),
   ("p", u"這些需求如果事後才補，往往要改遍整個介面；從一開始就用語意化的顏色與文字鍵，成本最低。"),
  ],
  u"無障礙、主題與多語系都是「橫切」需求，應該在一開始就融入元件與資源的設計。",
  [u"深色模式為什麼要用語意化顏色？",
   u"螢幕報讀器需要元件提供什麼資訊？",
   u"多語系除了翻譯還要考慮什麼？"]),
]),

(u"模組 C｜文件與編輯", [

lesson(u"文件模型",
  u"程式裡的「文件」長什麼樣",
  [u"理解文件模型的角色",
   u"區分模型與排版結果",
   u"認識結構化文件"],
  [fig(_DOC, 246, u"文件模型（概念）。"),
   ("p", u"使用者看到的是排好版的頁面，程式裡存的卻是一棵結構樹：章節、段落、表格、帶樣式的文字片段（Run）。排版（換行、分頁）是根據模型和視窗寬度<strong>計算</strong>出來的結果。"),
   code(u"""interface Run { text: string; bold?: boolean; italic?: boolean; }
interface Paragraph { style: string; runs: Run[]; }
interface Document { paragraphs: Paragraph[]; styles: Record<string, Style>; }"""),
   ("p", u"所有編輯操作都是對這棵樹的修改，這讓復原、協同編輯、存檔都有了共同的基礎。"),
  ],
  u"文件模型是軟體的核心資料結構；畫面上的排版是由模型計算出來的，不是模型本身。",
  [u"Run 是什麼？",
   u"為什麼排版結果不存在模型裡？",
   u"文件模型對復原功能有什麼幫助？"]),

lesson(u"文字編輯器的資料結構",
  u"Gap Buffer、Piece Table、Rope",
  [u"理解為什麼不用單一字串",
   u"比較三種文字緩衝區",
   u"親手操作 Piece Table"],
  [("p", u"如果整份文件存成一個字串，在開頭插入一個字就得把後面幾百萬個字元全部往後搬。文字編輯器用特殊的資料結構避免這件事。"),
   fig(_BUF, 238, u"三種文字緩衝區。"),
   widget({"t": "piece", "text": u"今天天氣很好", "q": u"<b>Piece Table</b>：插入或刪除，觀察兩個緩衝區與片段表的變化。"}),
   ("t", [u"結構", u"使用者（大致）", u"特點"],
         [[u"Gap Buffer", u"Emacs", u"游標附近編輯極快"], [u"Piece Table", u"早期 Word、VS Code", u"原文不動，復原容易"],
          [u"Rope", u"許多新編輯器", u"超大檔案友善、適合多游標"]]),
  ],
  u"文字編輯器避免搬動大量字元：Gap Buffer 留空位、Piece Table 記錄片段、Rope 用樹分塊。",
  [u"為什麼不能用單一字串存大文件？",
   u"Piece Table 的原始緩衝區為什麼唯讀？",
   u"Rope 適合什麼情況？"]),

lesson(u"復原與重做：命令模式",
  u"Ctrl+Z 是怎麼做到的",
  [u"理解命令模式",
   u"認識復原與重做堆疊",
   u"知道合併與分組"],
  [widget({"t": "undo", "q": u"<b>復原／重做</b>：執行幾個命令，再按復原、重做，觀察兩個堆疊。"}),
   code(u"""interface Command { do(): void; undo(): void; label: string; }

class InsertText implements Command {
  constructor(private doc: Doc, private pos: number, private text: string) {}
  label = "輸入文字";
  do()   { this.doc.insert(this.pos, this.text); }
  undo() { this.doc.delete(this.pos, this.text.length); }
}

function execute(c: Command) { c.do(); undoStack.push(c); redoStack.length = 0; }"""),
   ("ul", [u"<strong>新操作會清空重做堆疊</strong>：歷史分岔後，舊的未來就消失了。",
           u"<strong>合併</strong>：連續打的字合併成一個「輸入文字」命令，不然要按幾十次復原。",
           u"<strong>分組</strong>：「取代全部」包含上百次修改，要包成一個命令一次復原。",
           u"<strong>另一種做法</strong>：保存整份狀態的快照（單向資料流常用，" + LS(9) + u"）。"]),
  ],
  u"每個操作封裝成有 do／undo 的命令物件，放進堆疊即可復原與重做。",
  [u"為什麼新操作要清空重做堆疊？",
   u"連續打字為什麼要合併成一個命令？",
   u"快照式復原和命令式復原各有什麼優缺點？"]),

lesson(u"選取、剪貼簿與拖放",
  u"複製貼上沒有那麼簡單",
  [u"理解選取的表示方式",
   u"認識剪貼簿的多格式",
   u"知道拖放的流程"],
  [fig(_CLIP, 200, u"剪貼簿的多種格式。"),
   ("ul", [u"<strong>選取</strong>：通常用「錨點＋焦點」兩個位置表示，方向有意義（Shift＋方向鍵是移動焦點）。多游標編輯就是多組選取。",
           u"<strong>剪貼簿</strong>：複製時同時放入多種格式；有些程式只在對方要求時才產生資料（延遲提供）。",
           u"<strong>拖放</strong>：開始拖曳時提供資料與允許的操作（複製／移動），放下時目標端決定接受哪種格式。"]),
   ("p", u"安全提醒：貼上的資料來自外部，HTML 可能含有腳本，必須清理後才能顯示。"),
  ],
  u"選取用錨點與焦點表示；剪貼簿與拖放都以「多格式、由接收端挑選」的方式運作。",
  [u"選取的錨點和焦點有什麼不同？",
   u"為什麼複製時要放入多種格式？",
   u"貼上外部 HTML 時要注意什麼？"]),

lesson(u"檔案格式設計",
  u"二進位、XML、JSON、ZIP 容器",
  [u"比較常見的檔案格式策略",
   u"理解 ZIP 容器格式",
   u"知道版本相容的做法"],
  [("t", [u"策略", u"例子", u"優點", u"缺點"],
         [[u"自訂二進位", u"舊版 .doc、.psd", u"小、讀寫快", u"難除錯、難相容"],
          [u"文字（JSON／XML）", u".svg、許多設定檔", u"可讀、好版本控制", u"大、解析慢"],
          [u"ZIP 容器＋XML／JSON", u".docx、.xlsx、.pptx、.epub", u"結構清楚、圖片獨立存放、壓縮", u"隨機寫入不方便"],
          [u"SQLite 資料庫當檔案", u"Lightroom 目錄、許多 App", u"可部分讀寫、查詢、不易損毀", u"不易人工檢視"]]),
   code(u"""example.docx（其實是 ZIP）
├── [Content_Types].xml
├── word/document.xml      ← 文件內容
├── word/styles.xml
└── word/media/image1.png  ← 圖片獨立存放"""),
   ("p", u"設計原則：檔頭放魔術數字與版本號、未知欄位要能略過、新版本要能讀舊檔。各種實際格式的解剖見 " + XL("ff") + u"。"),
  ],
  u"檔案格式是應用程式的長期承諾；ZIP 容器與 SQLite 是現代常見的折衷選擇。",
  [u".docx 實際上是什麼格式？",
   u"自訂二進位格式有什麼缺點？",
   u"為什麼要在檔頭放版本號？"]),

lesson(u"自動儲存與當機復原",
  u"讓使用者不會失去工作",
  [u"學會安全的存檔流程",
   u"認識自動儲存的設計",
   u"知道當機復原的機制"],
  [fig(_RECOVER, 170, u"安全存檔流程。"),
   code(u"""async function safeSave(path: string, bytes: Uint8Array) {
  const tmp = path + ".tmp";
  await fs.writeFile(tmp, bytes);
  await fsync(tmp);              // 確保真的寫進磁碟，不只停在快取
  await fs.rename(tmp, path);    // 原子取代
}"""),
   ("ul", [u"<strong>自動儲存</strong>：定時或閒置時，在背景把文件存到復原資料夾，不覆蓋使用者的檔案。",
           u"<strong>當機偵測</strong>：啟動時放一個「執行中」標記，正常結束時刪除；下次啟動若標記還在，就知道上次當掉了。",
           u"<strong>版本歷史</strong>：有些軟體保留多個自動版本，讓使用者回到過去。"]),
   ("p", u"為什麼寫入不一定立刻到磁碟？見 " + XL("os", 37) + u" 的頁快取。"),
  ],
  u"安全存檔＝寫暫存檔、fsync、原子改名；自動儲存與當機標記讓意外不至於丟失工作。",
  [u"為什麼不直接覆寫原檔？",
   u"fsync 的作用是什麼？",
   u"程式怎麼知道上次是當機結束的？"]),

lesson(u"大型檔案與虛擬化",
  u"打開 1 GB 的記錄檔",
  [u"理解大型資料的挑戰",
   u"認識虛擬化清單",
   u"知道分頁載入與記憶體映射"],
  [fig(_VIRT, 240, u"虛擬化清單。"),
   ("ul", [u"<strong>虛擬化（窗口化）</strong>：只為看得到的列建立元件，捲動時重複使用。",
           u"<strong>分頁載入</strong>：只讀取目前需要的區段，其餘留在磁碟。",
           u"<strong>記憶體映射檔</strong>：把檔案映射到位址空間，由作業系統按需載入（見 " + XL("os", 22) + u"）。",
           u"<strong>增量處理</strong>：語法上色、搜尋分批進行，不一次處理全部。"]),
   ("p", u"同樣的原則適用於試算表、相簿、聊天記錄：<strong>成本應該和「看得到的量」成正比，而不是和「總量」成正比</strong>。"),
  ],
  u"處理大型資料的關鍵是只處理看得到的部分：虛擬化、分頁載入、記憶體映射。",
  [u"虛擬化清單怎麼節省記憶體？",
   u"記憶體映射檔的好處是什麼？",
   u"「成本與看得到的量成正比」是什麼意思？"]),

lesson(u"協同編輯",
  u"OT 與 CRDT 的概念",
  [u"理解協同編輯的衝突",
   u"認識 OT 與 CRDT",
   u"知道離線編輯的合併"],
  [fig(_COLLAB, 206, u"協同編輯的衝突。"),
   ("t", [u"方法", u"概念", u"特點"],
         [[u"鎖定", u"一次只允許一人編輯某段", u"簡單，但會互相等待"],
          [u"OT（操作轉換）", u"伺服器收到操作後，根據其他人先做的操作調整位置", u"需要中央伺服器排序"],
          [u"CRDT", u"每個字元有全域唯一的 ID，合併規則保證各方最終一致", u"可離線、可點對點，資料量較大"]]),
   ("p", u"協同編輯是命令模式（" + LS(14) + u"）的延伸：每個操作都要能被傳送、轉換、重新套用。"),
  ],
  u"協同編輯要解決同時修改的衝突；OT 靠伺服器轉換操作，CRDT 靠資料結構保證收斂。",
  [u"為什麼兩人同時編輯會產生衝突？",
   u"OT 和 CRDT 的主要差別是什麼？",
   u"CRDT 為什麼適合離線編輯？"]),
]),
]
