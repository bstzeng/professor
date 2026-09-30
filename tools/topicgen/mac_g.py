# -*- coding: utf-8 -*-
"""macOS 課程:模組 G(和 iPhone／iPad 的整合)。"""
from mac_common import *

_ECOSYSTEM = svg(
    title(u"生態系的威力:裝置之間無縫接力"),
    [C(150 + i * 170, 90, 40, [BLUE, GREEN, ORANGE][i], "var(--surface)", 2) for i in range(3)],
    [T(150 + i * 170, 94, s, 10, [BLUE, GREEN, ORANGE][i]) for i, s in enumerate([u"Mac", u"iPhone", u"iPad"])],
    P("M190 90 H310", MUTED, sw=1.5, dash="4 3"), P("M360 90 H480", MUTED, sw=1.5, dash="4 3"),
    T(320, 150, u"用同一個 Apple ID 登入,三台裝置就像一台", 10, ACC),
    [T(320, 174 + i * 20, s, 9.5, MUTED) for i, s in enumerate([
        u"接力:在 iPhone 看的網頁,在 Mac 接著看",
        u"隔空投送:檔案、照片在裝置間直接傳,不用線、不用雲",
        u"通用剪貼簿:在 iPhone 複製,在 Mac 貼上"])],
    T(320, 250, u"這是很多人「回不去」的原因:裝置之間的無縫協作,是 Apple 生態系最大的優勢", 9.5, ACC),
)

_CONTINUITY = svg(
    title(u"三個最實用的接力功能"),
    box(20, 46, 190, 116, u"接力 Handoff", [u"iPhone 上開的網頁、", u"郵件、備忘錄…", u"Mac 的 Dock 會出現圖示",
                                         u"點一下接著做"], BLUE),
    box(225, 46, 190, 116, u"隔空投送 AirDrop", [u"裝置之間直接傳檔", u"照片、檔案、網址", u"不用傳輸線、不用雲端",
                                            u"快又方便"], GREEN),
    box(430, 46, 190, 116, u"通用剪貼簿", [u"在 iPhone 複製一段字", u"直接在 Mac ⌘V 貼上", u"反過來也行",
                                      u"完全自動,不用設定"], ORANGE),
    T(320, 184, u"前提:同一個 Apple ID、開啟藍牙與 Wi-Fi、裝置靠近。設定裡確認「接力」是開的", 9.5, ACC),
    T(320, 208, u"AirDrop 傳照片給旁邊的人超好用:打開分享 →AirDrop →選對方,幾秒就傳完", 9.5),
)

_MESSAGES = svg(
    title(u"訊息、電話與 FaceTime 都在 Mac 上"),
    box(30, 46, 270, 104, u"在 Mac 收發", [u"iMessage:藍色泡泡訊息", u"簡訊:綠色泡泡(需 iPhone 中繼)",
                                       u"電話:透過 iPhone 在 Mac 接打", u"FaceTime:視訊通話"], BLUE),
    box(340, 46, 270, 104, u"為什麼方便", [u"工作時不用一直拿手機", u"用電腦鍵盤打字回訊息",
                                      u"電話響了在 Mac 就能接", u"複製貼上、傳檔都順"], GREEN),
    T(320, 176, u"用同一個 Apple ID 登入「訊息」和「FaceTime」App,iPhone 的訊息與來電就會同步到 Mac", 9.5, ACC),
    T(320, 200, u"簡訊(綠泡泡)要在 iPhone 開「簡訊轉傳」;iMessage(藍泡泡)則自動同步", 9.5),
)

_PHOTOS = svg(
    title(u"照片、iCloud 與跨裝置同步"),
    flow([(u"iPhone 拍照", u""), (u"上傳 iCloud", u"照片圖庫"),
          (u"Mac「照片」App", u"自動出現"), (u"任何裝置", u"都看得到")],
         44, h=58, colors=[BLUE, GREEN, ACC, ORANGE]),
    T(320, 128, u"開啟「iCloud 照片」後,iPhone 拍的照片會自動出現在 Mac 的「照片」App,不用傳線", 10, ACC),
    T(320, 152, u"編輯、刪除也會同步:在 Mac 修個圖,iPhone 上也跟著改", 9.5),
    T(320, 176, u"注意:照片同步會佔 iCloud 空間;空間不足時,可開「最佳化儲存空間」讓本機只留小圖", 9.5),
    T(320, 200, u"重要照片建議額外備份(Time Machine 或另一個雲端),雞蛋別放同一個籃子", 9.5, MUTED),
)

MODULES = [(u"模組 G｜和 iPhone／iPad 的整合", [

lesson(u"生態系的威力:接力、隔空投送、通用剪貼簿",
  u"如果你有 iPhone,這是 Mac 最迷人的部分",
  [u"理解 Apple 生態系的協作優勢",
   u"認識接力、隔空投送、通用剪貼簿",
   u"知道啟用的前提"],
  [("p", u"如果你同時有 iPhone(或 iPad),那 Mac 有一整套<strong>跨裝置協作</strong>的功能,"
        u"讓三台裝置<strong>像一台</strong>。這是很多人用了就回不去的原因。"),
   ("FIGX", _ECOSYSTEM, "0 0 640 262", u"同一個 Apple ID 下,Mac、iPhone、iPad 無縫接力。"),
   ("h", u"1. 三個代表功能"),
   ("ul", [u"<strong>接力(Handoff)</strong>:在 iPhone 上看的網頁、寫的郵件,走到電腦前<strong>在 Mac 接著做</strong>。",
           u"<strong>隔空投送(AirDrop)</strong>:檔案、照片在裝置之間<strong>直接傳</strong>,不用線、不用雲。",
           u"<strong>通用剪貼簿</strong>:在 iPhone <strong>複製</strong>,在 Mac <strong>貼上</strong>——完全自動。"]),
   ("h", u"2. 啟用的前提"),
   ("p", u"這些功能要能運作,通常需要:"),
   ("ol", [u"所有裝置登入<strong>同一個 Apple ID</strong>(" + LS(31) + u")。",
           u"開啟<strong>藍牙</strong>和<strong>Wi-Fi</strong>。",
           u"裝置<strong>靠得夠近</strong>。",
           u"在系統設定 →一般 →<strong>「隔空播放與接力」</strong>確認接力是開的。"]),
   ("h", u"3. 沒有 iPhone 也沒關係"),
   ("p", u"如果你目前沒有其他 Apple 裝置,這個模組的功能暫時用不到,可以先跳過,"
        u"專心把前面的 Mac 基本操作練熟。等哪天有了 iPhone,再回來看,你會發現它們串起來有多方便。"),
   ("p", u"接下來兩課,看幾個最實用的整合:接力與傳檔(這課)、訊息與電話(" + LS(36) + u")、照片同步(" + LS(37) + u")。")],
  u"如果你有 iPhone:確認兩台都登入同一個 Apple ID、都開了藍牙和 Wi-Fi。下一課會實際試傳一張照片。",
  [u"接力、隔空投送、通用剪貼簿分別讓你做什麼?",
   u"這些跨裝置功能需要哪些前提?(舉兩個)",
   u"這些功能背後靠什麼帳號串起來?"],
  fig=None),

lesson(u"訊息、電話與 FaceTime 都在 Mac 上",
  u"工作時不用一直拿手機——訊息和電話都能在 Mac 處理",
  [u"知道 Mac 能收發訊息與接打電話",
   u"區分 iMessage 與簡訊",
   u"學會啟用"],
  [("p", u"用 Mac 工作時,一直被手機打斷很煩。好消息是:<strong>iPhone 的訊息和來電,都能同步到 Mac</strong>,"
        u"讓你用電腦鍵盤回訊息、直接在 Mac 接電話。"),
   ("FIGX", _MESSAGES, "0 0 640 220", u"訊息、電話、FaceTime 都能在 Mac 上處理。"),
   ("h", u"1. 訊息:藍泡泡 vs. 綠泡泡"),
   ("t", [u"", u"藍色泡泡", u"綠色泡泡"],
    [[u"是什麼", u"iMessage(Apple 之間)", u"一般簡訊 SMS"],
     [u"怎麼同步到 Mac", u"用同一 Apple ID 登入「訊息」App,自動同步", u"要在 iPhone 開「簡訊轉傳」才會出現在 Mac"]]),
   ("p", u"所以如果你發現<strong>只有藍泡泡</strong>訊息出現在 Mac、<strong>綠泡泡簡訊沒有</strong>,"
        u"到 iPhone 的<strong>設定 →訊息 →簡訊/彩信轉發</strong>,把 Mac 打開就好。"),
   ("h", u"2. 電話"),
   ("p", u"iPhone 響的時候,<strong>Mac 也會跳出來電</strong>,你可以直接在電腦上接、講、掛。"
        u"打電話也行:在 Mac 的聯絡人或 FaceTime 裡點電話號碼,會透過你的 iPhone 撥出。"
        u"(需要兩台在同一個 Wi-Fi,並在 iPhone 開「其他裝置上的通話」。)"),
   ("h", u"3. FaceTime"),
   ("p", u"<strong>FaceTime</strong> 是 Apple 的視訊/語音通話,Mac 內建。"
        u"用 Apple ID 登入就能和其他 Apple 使用者視訊,也能產生連結邀請別人加入(對方用其他裝置也能點進來)。"),
   ("p", u"把這些設定好,你工作時就能<strong>把手機放一邊</strong>,訊息和電話都在眼前的 Mac 處理,順手很多。")],
  u"在 Mac 打開「訊息」App,用你的 Apple ID 登入。如果你有 iPhone,傳一則訊息給自己或朋友,看它在兩台裝置間同步。",
  [u"藍色泡泡和綠色泡泡的訊息有什麼不同?",
   u"綠泡泡簡訊沒出現在 Mac,要去哪裡設定?",
   u"iPhone 來電時,Mac 會怎樣?"],
  fig=None),

lesson(u"照片、iCloud 與跨裝置同步",
  u"手機拍的照片,怎麼自動出現在 Mac?",
  [u"理解 iCloud 照片的同步",
   u"知道編輯也會同步",
   u"注意空間與備份"],
  [("p", u"你用 iPhone 拍照,想在 Mac 上看、整理、修圖——不用傳輸線,靠 <strong>iCloud 照片</strong>自動同步。"),
   ("FIGX", _PHOTOS, "0 0 640 220", u"開啟 iCloud 照片後,iPhone 拍的照片自動出現在 Mac 的「照片」App。"),
   ("h", u"1. 自動同步"),
   ("p", u"在 iPhone 和 Mac 都開啟 <strong>iCloud 照片</strong>(用同一 Apple ID)後:"
        u"iPhone 拍的照片會<strong>上傳 iCloud</strong>,再自動出現在 Mac 的<strong>「照片」App</strong> 裡,反之亦然。"),
   ("h", u"2. 編輯也同步"),
   ("p", u"不只是照片本身,<strong>編輯和刪除也會同步</strong>:你在 Mac 上修個圖、加個相簿,"
        u"iPhone 上也會跟著變。所有裝置看到的是<strong>同一個照片圖庫</strong>。"),
   ("h", u"3. 空間與備份要注意"),
   ("ul", [u"照片同步會<strong>佔用 iCloud 空間</strong>(免費的 5GB 常常不夠,可能要加購)。",
           u"本機空間不足時,可開「<strong>最佳化 Mac 儲存空間</strong>」:本機只留小圖,原圖放雲端,要用時才下載"
           u"(" + LS(11) + u"的雲朵圖示概念)。",
           u"<strong>重要照片建議額外備份</strong>:iCloud 是同步不是備份——在一台刪了,全部都刪。"
           u"用 Time Machine(" + LS(33) + u")或另一個雲端多存一份,雞蛋別放同一個籃子(" + FMT(61, u"備份的重要") + u")。"]),
   ("p", u"設定好之後,你的照片會在所有裝置間流暢地流動,再也不用手動傳來傳去。"
        u"到這裡,和 iPhone/iPad 整合的模組就完成了——如果你有這些裝置,善用它們會讓 Mac 更好用。")],
  u"如果你有 iPhone:在兩台裝置都開啟「iCloud 照片」(設定 →你的名字 →iCloud →照片)。拍一張照,看它幾秒後出現在 Mac 的「照片」App。",
  [u"iPhone 拍的照片怎麼自動出現在 Mac?",
   u"在 Mac 上編輯照片,iPhone 上會怎樣?",
   u"為什麼說「iCloud 是同步不是備份」?重要照片該怎麼辦?"],
  fig=None),
])]
