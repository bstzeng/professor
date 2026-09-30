# -*- coding: utf-8 -*-
"""macOS 課程:模組 H(進階與疑難排解)。"""
from mac_common import *

_TERMINAL = svg(
    title(u"終端機:Mac 底層其實是 Unix"),
    window(80, 44, 480, 120, True, u"終端機 — bash"),
    mono(100, 90, u"你的名字@Mac ~ % ls", 11, GREEN),
    mono(100, 110, u"Desktop  Documents  Downloads", 10, MUTED),
    mono(100, 130, u"你的名字@Mac ~ % pwd", 11, GREEN),
    mono(100, 150, u"/Users/你的名字", 10, MUTED),
    T(320, 184, u"終端機讓你用「打指令」的方式操作 Mac 的 Unix 底層——不用怕,平常完全不需要它", 9.5, ACC),
    T(320, 208, u"但看懂幾個基本指令(ls 列出、cd 切換、pwd 現在在哪)能幫你理解檔案結構,偶爾也很方便", 9.5),
)

_FORCEQUIT = svg(
    title(u"App 沒回應:Mac 版的「工作管理員」"),
    box(30, 46, 270, 108, u"強制結束", [u"⌘⌥⎋(Command Option Esc)", u"跳出清單,選當掉的 App",
                                    u"按「強制結束」", u"或蘋果選單  →強制結束"], RED),
    box(340, 46, 270, 108, u"活動監視器", [u"應用程式 →工具程式", u"看每個程式的 CPU、記憶體", u"對應 Windows 工作管理員",
                                      u"能結束卡住的程序"], BLUE),
    T(320, 176, u"App 轉圈圈沒反應?先等一下,真的卡死就 ⌘⌥⎋ 強制結束它,重開通常就好", 9.5, ACC),
    T(320, 200, u"想看「什麼程式在吃 CPU/記憶體/電」,用活動監視器,它就是 Mac 的工作管理員", 9.5),
)

_TROUBLE = svg(
    title(u"常見疑難排解:先試這幾招"),
    [box(20 + (i % 3) * 205, 46 + (i // 3) * 80, 190, 68, t, [s], c, 10, 8.5)
     for i, (t, s, c) in enumerate([
        (u"App 當掉", u"⌘⌥⎋ 強制結束,再重開", RED),
        (u"整台變慢/怪", u"重新開機(關掉再開)", ORANGE),
        (u"某功能失常", u"檢查該 App 或系統更新", BLUE),
        (u"網路問題", u"關開 Wi-Fi、重開路由器", GREEN),
        (u"周邊沒反應", u"拔插、換孔、看藍牙", PURPLE),
        (u"真的搞不定", u"查 Apple 支援、預約 Genius Bar", TEAL)])],
    T(320, 222, u"八成問題「重新開機」就解決;分清楚是 App、系統還是硬體的問題(見第 3 課的分層思考)", 9.5, ACC),
    T(320, 244, u"開機時按住特定鍵可進入安全模式或回復模式(進階);多數人日常用不到", 9.5, MUTED),
)

_FINALTIPS = svg(
    title(u"給 Windows 老手的最後叮嚀"),
    R(30, 44, 580, 180, ACC, "var(--accent-soft)", 10),
    [T(60, 74 + i * 24, s, 10, TXT, "start") for i, s in enumerate([
        u"1. 把「Ctrl」的反射換成「⌘」——九成快捷鍵問題立刻消失",
        u"2. 什麼都先按「⌘＋空白」搜尋(Spotlight),別再一層層翻",
        u"3. 找不到功能?抬頭看螢幕最上方的選單列",
        u"4. 關視窗 ≠ 結束 App;⌘Q 才是真的結束",
        u"5. 學會觸控板手勢,尤其三指左右滑、三指上滑",
        u"6. 一定要設 Time Machine 備份",
        u"7. 別硬套 Windows 邏輯——先理解 Mac 自己的規則"])],
    T(320, 250, u"恭喜你完成整門課!你已經從「帶著 Windows 腦袋」進化到「用 Mac 的邏輯用 Mac」", 9.5, ACC),
)

MODULES = [(u"模組 H｜進階與疑難排解", [

lesson(u"認識終端機:Mac 底層其實是 Unix",
  u"看一眼 Mac 的底層——不用怕,理解就好",
  [u"知道終端機是什麼",
   u"認識幾個基本指令",
   u"理解它和檔案結構的關係"],
  [("p", u"這一課帶你看一眼 Mac 的<strong>底層</strong>。還記得第一個模組說 macOS 是 Unix 嗎(" + LS(2) + u")?"
        u"<strong>終端機</strong>就是直接和這個 Unix 底層對話的地方。"
        u"<strong>先說清楚:平常你完全不需要用它</strong>,這課只是讓你認識、不再害怕。"),
   ("FIGX", _TERMINAL, "0 0 640 224", u"終端機用「打指令」的方式操作 Unix 底層。"),
   ("h", u"1. 終端機是什麼"),
   ("p", u"<strong>終端機</strong>(在 應用程式 →工具程式,或 Spotlight 打「終端機」)是一個<strong>打指令</strong>的視窗,"
        u"對應 Windows 的「命令提示字元」。你打一行指令、按 Enter,它就執行。"),
   ("h", u"2. 三個看懂就好的指令"),
   ("t", [u"指令", u"作用"],
    [[u"ls", u"列出目前資料夾裡有什麼(list)"],
     [u"cd 資料夾", u"進入某個資料夾(change directory)"],
     [u"pwd", u"顯示我現在在哪個資料夾(印出完整路徑)"]]),
   ("p", u"用 <code>pwd</code> 你會看到熟悉的斜線路徑,例如 <code>/Users/你的名字</code>(" + LS(6) + u")——"
        u"這就把終端機和你學過的檔案結構連起來了。"),
   ("h", u"3. 為什麼值得認識"),
   ("ul", [u"很多網路上的教學(裝開發工具、修設定)會叫你「打開終端機貼上這行指令」,認得它就不會慌。",
           u"它能做一些圖形介面做不到、或很麻煩的事。",
           u"⚠ 但也<strong>別亂貼看不懂的指令</strong>:有些指令威力很大,貼錯可能刪掉重要檔案。只貼你信任來源、看得懂用途的。"]),
   ("p", u"總之:終端機是 Mac 強大的一面,但<strong>日常使用完全不需要</strong>。知道它存在、看得懂基本指令就夠了。")],
  u"打開終端機(Spotlight 打「終端機」),輸入 pwd 按 Enter,看它印出你現在的路徑;再輸入 ls 按 Enter,看它列出檔案。只做這兩個安全的指令就好。",
  [u"終端機對應 Windows 的什麼?",
   u"ls、cd、pwd 三個指令各做什麼?",
   u"為什麼不能隨便貼上看不懂的指令?"],
  fig=None),

lesson(u"當機、卡住、App 沒回應:Mac 版的工作管理員",
  u"程式轉圈圈不動了怎麼辦?這一課教你救場",
  [u"學會強制結束當掉的 App",
   u"認識活動監視器",
   u"知道對應 Windows 的工具"],
  [("p", u"App 卡住轉圈圈、整個沒反應——每台電腦都會遇到。Mac 有對應 Windows「工作管理員」的工具來處理。"),
   ("FIGX", _FORCEQUIT, "0 0 640 220", u"強制結束處理當掉的 App;活動監視器是 Mac 的工作管理員。"),
   ("h", u"1. 強制結束當掉的 App"),
   ("p", u"當一個 App 沒反應(游標變成<strong>轉圈圈的彩球</strong>),先<strong>等幾秒</strong>看它會不會恢復。"
        u"真的卡死了,就<strong>強制結束</strong>它:"),
   ("ul", [u"按 <strong>⌘⌥⎋</strong>(Command＋Option＋Esc),跳出「強制結束」清單,選那個當掉的 App,按<strong>強制結束</strong>。",
           u"或從<strong>蘋果選單  →強制結束</strong>。",
           u"或在 <strong>Dock</strong> 圖示上<strong>按住 ⌥ 右鍵 →強制結束</strong>。"]),
   ("p", u"強制結束後<strong>重開那個 App</strong>,通常就正常了(沒存的資料可能會丟,這點和 Windows 一樣)。"),
   ("h", u"2. 活動監視器:Mac 的工作管理員"),
   ("p", u"想看<strong>每個程式在吃多少資源</strong>?打開<strong>活動監視器</strong>"
        u"(應用程式 →工具程式,或 Spotlight 打「活動監視器」)。它對應 Windows 的<strong>工作管理員</strong>:"),
   ("ul", [u"看每個程序的 <strong>CPU、記憶體、能耗、網路</strong>用量。",
           u"揪出<strong>某個吃掉大量 CPU 或記憶體</strong>、害電腦變慢的程式。",
           u"選中它,按左上角的 <strong>✕</strong> 可以結束它(相當於強制結束)。"]),
   ("p", u"下次電腦變慢、風扇狂轉,打開活動監視器看看是誰在搞鬼,常常一目了然。")],
  u"打開活動監視器,點「CPU」欄排序,看看現在哪個程式最耗 CPU。(先別結束任何東西,只是觀察。)這就是 Mac 的工作管理員。",
  [u"App 當掉(彩球轉圈)時,強制結束的快捷鍵是什麼?",
   u"Mac 對應 Windows「工作管理員」的工具叫什麼?",
   u"想知道哪個程式讓電腦變慢,可以怎麼查?"],
  fig=None),

lesson(u"常見疑難排解與給 Windows 老手的最後叮嚀",
  u"最後一課:排錯的通用招數,以及整門課的重點回顧",
  [u"掌握常見問題的處理順序",
   u"知道何時該求助",
   u"回顧整門課的核心觀念"],
  [("p", u"最後一課,給你一套<strong>通用的排錯思路</strong>,以及整門課最重要的幾個提醒。"),
   ("FIGX", _TROUBLE, "0 0 640 264", u"常見問題先試這幾招;分清楚是 App、系統還是硬體的問題。"),
   ("h", u"1. 排錯的通用順序"),
   ("ol", [u"<strong>某個 App 出問題</strong> → 先<strong>強制結束再重開</strong>它(" + LS(39) + u")。",
           u"<strong>整台怪怪的、變慢</strong> → <strong>重新開機</strong>(關掉再開)。八成問題這一招就解決。",
           u"<strong>某功能失常</strong> → 檢查那個 App 或<strong>系統有沒有更新</strong>(" + LS(34) + u")。",
           u"<strong>網路問題</strong> → 關開 Wi-Fi、重開路由器。",
           u"<strong>周邊(滑鼠、耳機)沒反應</strong> → 拔插、換孔、檢查藍牙。",
           u"<strong>真的搞不定</strong> → 上 Apple 支援網站查,或預約 Apple Store 的技術服務。"]),
   ("p", u"排錯時記得第 3 課的<strong>分層思考</strong>(" + LS(3) + u"):先判斷是 <strong>App、系統、還是硬體</strong>的問題,方向就清楚了。"),
   ("h", u"2. 給 Windows 老手的最後叮嚀"),
   ("FIGX", _FINALTIPS, "0 0 640 234", u"七個最重要的提醒,幫你從 Windows 腦袋切換到 Mac 邏輯。"),
   ("ol", [u"把「Ctrl」的反射<strong>換成「⌘」</strong>(" + LS(19) + u")。",
           u"什麼都先按 <strong>⌘＋空白搜尋</strong>(" + LS(15) + u")。",
           u"找不到功能?<strong>抬頭看螢幕最上方</strong>的選單列(" + LS(5) + u")。",
           u"<strong>關視窗 ≠ 結束 App</strong>,⌘Q 才是結束(" + LS(4) + u")。",
           u"學會<strong>觸控板手勢</strong>(" + LS(21) + u")。",
           u"一定要設 <strong>Time Machine 備份</strong>(" + LS(33) + u")。",
           u"<strong>別硬套 Windows 邏輯</strong>——先理解 Mac 自己的規則。"]),
   ("h", u"3. 恭喜你"),
   ("p", u"從作業系統的血統、檔案結構、找程式裝程式、鍵盤快捷鍵、視窗多工、系統設定,到疑難排解——"
        u"你已經從「<strong>帶著 Windows 腦袋操作 Mac</strong>」進化成「<strong>用 Mac 的邏輯用 Mac</strong>」。"
        u"接下來就是多用、多試,讓這些新習慣變成肌肉記憶。歡迎來到 Mac 的世界!"),
   ("p", u"想更深入了解「檔案、副檔名、.app、磁碟映像」的底層原理,可以接著看姊妹課程 "
        + FMT(1, u"《檔案格式解剖學》") + u"。")],
  u"回頭看看你在第 1 課記下的「最挫折的三件事」。現在,你應該大多都知道怎麼解決了吧?把還沒解決的,用這門課學到的方法或去 Apple 支援查一查。",
  [u"電腦整台變慢或怪怪的,最先該試哪一招?",
   u"排錯時的「分層思考」是指什麼?",
   u"這門課給 Windows 老手最核心的一個提醒是什麼?"],
  fig=None),
])]
