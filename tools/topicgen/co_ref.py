# -*- coding: utf-8 -*-
"""電腦從零開始:兩個參考頁——名詞與年表速查、互動開機流程逐步圖。"""
from co_common import LS, NOTE

_TERMS = [
    [u"位元 bit", u"最小資料單位,只有 0 或 1(對應開關的關/開)", LS(1)],
    [u"電晶體", u"電控的開關,是 CPU 的物理基礎", LS(1)],
    [u"邏輯閘", u"AND/OR/NOT,用開關做出「判斷」的積木", LS(2)],
    [u"正反器", u"能「記住」一個 bit 的電路,靠回授維持", LS(4)],
    [u"CPU", u"處理器,真正做運算的地方", LS(5)],
    [u"時脈 / GHz", u"讓零件對齊步伐的節拍;GHz=每秒幾十億拍", LS(6)],
    [u"機器碼", u"CPU 直接執行的一串數字(位元組)", LS(9)],
    [u"組合語言", u"用 MOV、ADD 等助憶符號寫的低階語言", LS(10)],
    [u"儲存程式架構", u"程式也放在記憶體、被當資料執行(馮諾伊曼)", LS(11)],
    [u"取指循環", u"抓取→解碼→執行,CPU 的心跳", LS(12)],
    [u"bootstrap / boot", u"開機自舉:小程式載入大程式的接力", LS(13)],
    [u"ROM", u"唯讀記憶體,斷電不消失,放開機第一段程式", LS(14)],
    [u"BIOS", u"燒在 ROM 裡的開機程式;新機多為 UEFI", LS(14)],
    [u"reset vector", u"CPU 通電後跳去的固定位址(硬體寫死)", LS(15)],
    [u"POST", u"開機自檢:先確認硬體堪用", LS(16)],
    [u"開機磁區", u"磁碟前 512 位元組,含開機載入器,標記 55 AA", LS(17)],
    [u"作業系統 OS", u"管硬體/檔案/記憶體/程式的「總管」", LS(20)],
    [u"中斷 interrupt", u"裝置或程式「舉手」請 CPU 處理", LS(21)],
    [u"CP/M", u"DOS 的前輩,早期微電腦的主流 OS", LS(22)],
    [u"MS-DOS", u"IBM PC 時代的主流作業系統", LS(24)],
    [u"命令列 C:\\", u"打字下指令的文字介面", LS(25)],
    [u"FAT", u"DOS 的檔案系統;後代仍用於隨身碟/記憶卡", LS(26)],
    [u"INT 21h", u"程式呼叫 DOS 服務的窗口(軟體中斷)", LS(27)],
    [u"常規記憶體 640K", u"DOS 程式能自由用的記憶體上限", LS(28)],
    [u"GUI 圖形介面", u"視窗、圖示、滑鼠的圖形操作方式", LS(31)],
    [u"像素 pixel", u"螢幕上的一個點;點陣模式能單獨控制", LS(32)],
    [u"事件驅動", u"程式開好視窗後「等你動作」再反應", LS(33)],
    [u"GDI", u"Windows 的繪圖中間人,隱藏顯卡差異", LS(36)],
    [u"訊息迴圈", u"取訊息→分派→反應,視窗程式的心臟", LS(37)],
    [u"保護模式", u"新 CPU 能定址更多記憶體、保護各程式領地", LS(38)],
    [u"合作式多工", u"程式「自願讓位」輪流用 CPU;一個卡住全體卡", LS(39)],
    [u"搶佔式多工", u"由系統強制分配時間,較可靠", LS(39)],
    [u"UEFI", u"取代傳統 BIOS 的新韌體,開機接力精神不變", LS(42)],
]

_TIMELINE = [
    [u"1940 年代", u"第一批電子電腦(如 ENIAC):靠接線與開關「寫程式」", LS(7)],
    [u"1940 年代中", u"「儲存程式」概念成形(馮諾伊曼架構),程式=資料", LS(11)],
    [u"1970 年代末", u"CP/M 成為早期 8 位元微電腦的主流作業系統", LS(22)],
    [u"1981", u"IBM PC 問世(開放架構);MS-DOS 隨之而來", LS(23)],
    [u"1980 年代中", u"早期 Windows 出現:跑在 DOS 上的圖形環境", LS(35)],
    [u"1990 前後", u"Windows 3.0 讓圖形介面漸受重視", LS(40)],
    [u"1992 前後", u"Windows 3.1:視窗真正走向普及", LS(40)],
    [u"1990 年代中", u"更整合的圖形系統出現,DOS 逐漸退居幕後", LS(42)],
]

_CHEAT_BODY = [
    ("p", u"這一頁把整門課的關鍵名詞整理成一張表,再附上一條大致的時間軸,方便隨時查閱。"
          u"想一步步看電腦開機時到底發生什麼,可以到<a href=\"boot-sequence.html\">互動開機流程</a>。"),
    ("h", u"1. 關鍵名詞速查"),
    ("t", [u"名詞", u"白話解釋", u"課程"], _TERMS),
    ("h", u"2. 大致時間軸(年份為概略)"),
    ("p", u"下面的年份是<strong>概略、示意</strong>,用來建立「先後順序」的感覺,而非精確史料;"
          u"確切日期與版本細節,請查閱權威的科技史資料。"),
    ("t", [u"時期", u"發生了什麼", u"課程"], _TIMELINE),
    ("h", u"3. 三個最該記住的重點"),
    ("ol", [u"<strong>電腦=簡單東西的層層堆疊</strong>:開關→邏輯→運算→記憶→CPU→OS→視窗,每層用下一層堆出來(" + LS(43) + u")。",
            u"<strong>開機是接力,不是瞬間</strong>:硬體用 reset vector 起頭,再靠「小程式載入大程式」把 OS 叫醒(" + LS(18) + u")。",
            u"<strong>Windows(3.1)蓋在 DOS 上</strong>:早期它是 DOS 之上的圖形環境,不是獨立作業系統(" + LS(35) + u")。"]),
    ("h", u"4. 破解幾個常見迷思"),
    ("t", [u"迷思", u"正解", u"課程"],
     [[u"「DOS 是 Windows 的一部分」", u"反了:早期 Windows 跑在 DOS 上", LS(35)],
      [u"「開機是瞬間的事」", u"是一連串載入的接力", LS(18)],
      [u"「CPU 很聰明」", u"它只是超快地「看到數字就動作」", LS(9)],
      [u"「640K 是廠商小氣」", u"源於當年 CPU 定址上限與設計", LS(28)],
      [u"「命令列已淘汰」", u"仍是專家與伺服器的利器", LS(30)]]),
    ("raw", u'<p style="color:var(--text-muted);font-size:0.9em">🧭 %s</p>' % NOTE),
]

CHEATSHEET = {
    "file": "cheatsheet.html",
    "title": u"名詞與年表速查表",
    "h1": u"電腦從零開始:名詞與年表速查表",
    "icon": u"📇",
    "description": u"位元、邏輯閘、BIOS、開機磁區、DOS、GDI、保護模式… 一頁看懂本課關鍵名詞,加上大致時間軸與常見迷思",
    "body": _CHEAT_BODY,
}

# ---------- 互動開機流程逐步圖 ----------

_BOOT_HTML = u"""<div class="content-figure" style="text-align:left">
  <p style="margin:0 0 12px">點<strong>下一步</strong>,一步步看電腦從按下電源到進入系統,每一棒發生了什麼。
  這是把<a href="lesson-18.html">第 18 課</a>的開機一條龍,做成可以逐步點看的版本。</p>
  <div id="bs-stage" style="display:flex;flex-direction:column;gap:8px;max-width:560px"></div>
  <div style="margin-top:14px;display:flex;gap:10px;align-items:center;flex-wrap:wrap">
    <button id="bs-prev" style="padding:7px 16px;border-radius:8px;border:1px solid var(--border);background:var(--surface);color:var(--text);cursor:pointer">← 上一步</button>
    <button id="bs-next" style="padding:7px 16px;border-radius:8px;border:1px solid var(--accent);background:var(--accent);color:#fff;cursor:pointer">下一步 →</button>
    <button id="bs-reset" style="padding:7px 16px;border-radius:8px;border:1px solid var(--border);background:var(--surface);color:var(--text);cursor:pointer">重來</button>
    <span id="bs-count" style="color:var(--text-muted);font-size:0.9em"></span>
  </div>
  <div id="bs-detail" style="margin-top:14px;padding:14px 16px;border:1px solid var(--border);border-radius:10px;background:var(--surface);min-height:64px"></div>
</div>
<script>
(function () {
  var steps = [
    {t: '① 按下電源 / CPU 重置', d: '供電穩定後 CPU 重置,程式計數器指向一個「出廠寫死」的固定位址(reset vector)。這一步不靠任何軟體——起點是硬體本身規定的。'},
    {t: '② BIOS 起跑', d: 'reset vector 對應到 ROM,於是燒在晶片裡的 BIOS 成為全機第一段被執行的程式。ROM 斷電不消失,所以開機瞬間它就在那裡。'},
    {t: '③ POST 開機自檢', d: 'BIOS 先幫硬體做體檢:CPU、記憶體、顯示、鍵盤是否正常。早期螢幕可能還沒好,所以用「嗶」聲回報——一聲代表一切正常。'},
    {t: '④ 尋找可開機的磁碟', d: 'BIOS 依設定的順序,找一顆「可以開機」的裝置(硬碟、軟碟、隨身碟…)。'},
    {t: '⑤ 讀取開機磁區(512 位元組)', d: '把該磁碟最前面的 512 位元組(開機磁區)讀進記憶體,檢查結尾是不是暗號 55 AA。是,才相信「這顆碟真的能開機」。'},
    {t: '⑥ 開機載入器接棒', d: '這一小段程式(開機載入器)接手,去把真正龐大的作業系統核心載入記憶體——典型的「小程式載入大程式」。'},
    {t: '⑦ 作業系統接管(DOS)', d: 'OS 完成載入、接管全機。你看到 C:\\> ,能用命令列、檔案系統與系統服務。到這裡,電腦才算真正「醒來」。'},
    {t: '⑧ 啟動圖形環境(Windows)', d: '在 DOS 之上再啟動 Windows:用 GDI 畫視窗、用訊息迴圈回應操作、用保護模式掙脫 640K、用多工並存程式。最後你看見桌面。'}
  ];
  var cur = 0;
  var stage = document.getElementById('bs-stage');
  var detail = document.getElementById('bs-detail');
  var count = document.getElementById('bs-count');
  function render() {
    stage.innerHTML = steps.map(function (s, i) {
      var on = i <= cur;
      var isNow = i === cur;
      var bg = isNow ? 'var(--accent)' : (on ? 'var(--surface)' : 'var(--surface)');
      var col = isNow ? '#fff' : (on ? 'var(--text)' : 'var(--text-muted)');
      var bd = isNow ? 'var(--accent)' : 'var(--border)';
      var op = on ? '1' : '0.5';
      return '<div style="padding:9px 13px;border:1px solid ' + bd + ';border-radius:8px;background:' + bg +
        ';color:' + col + ';opacity:' + op + ';font-size:0.95em;transition:all .15s">' + s.t + '</div>';
    }).join('');
    detail.innerHTML = '<strong>' + steps[cur].t + '</strong><br><span style="color:var(--text-muted)">' + steps[cur].d + '</span>';
    count.textContent = '第 ' + (cur + 1) + ' / ' + steps.length + ' 步';
    document.getElementById('bs-prev').disabled = (cur === 0);
    document.getElementById('bs-next').disabled = (cur === steps.length - 1);
  }
  document.getElementById('bs-next').addEventListener('click', function () { if (cur < steps.length - 1) { cur++; render(); } });
  document.getElementById('bs-prev').addEventListener('click', function () { if (cur > 0) { cur--; render(); } });
  document.getElementById('bs-reset').addEventListener('click', function () { cur = 0; render(); });
  render();
})();
</script>"""

BOOTSEQ = {
    "file": "boot-sequence.html",
    "title": u"互動開機流程",
    "h1": u"互動開機流程:一步步看電腦怎麼把自己叫醒",
    "icon": u"⚙️",
    "description": u"從按下電源到進入系統,點「下一步」逐步看每一棒發生什麼:reset vector、BIOS、POST、開機磁區、載入 OS、啟動 Windows",
    "body": [
        ("p", u"開機看似一瞬間,其實是一連串「小程式載入大程式」的接力(" + LS(13) + u")。"
              u"這個互動小工具,讓你<strong>逐步</strong>走過每一棒,把" + LS(18) + u"的流程看得更清楚。"),
        ("raw", _BOOT_HTML),
        ("h", u"看的時候可以留意"),
        ("ul", [u"<strong>前兩棒是「硬體起頭」</strong>:reset vector 與 BIOS 都不靠軟體,這正是雞生蛋問題的解法(" + LS(15) + u")。",
                u"<strong>中間每一棒都在「載入下一棒」</strong>:小而可靠的先跑,把大而複雜的逐步喚醒(" + LS(17) + u")。",
                u"<strong>最後兩棒才是我們熟悉的畫面</strong>:DOS 接管、再疊上 Windows 桌面(" + LS(35) + u")。"]),
        ("p", u"提醒:這是<strong>簡化的示意流程</strong>,對應傳統 BIOS + DOS + Windows 的年代。"
              u"現代電腦改用 UEFI、開機細節不同,但「一棒接一棒把自己叫醒」的大原則不變(" + LS(42) + u")。"),
        ("raw", u'<p style="color:var(--text-muted);font-size:0.9em">🧭 %s</p>' % NOTE),
    ],
}

REFERENCES = [CHEATSHEET, BOOTSEQ]
