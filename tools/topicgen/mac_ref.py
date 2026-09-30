# -*- coding: utf-8 -*-
"""macOS 課程:兩個參考頁——Windows→Mac 對照速查表、互動快捷鍵練習器。"""
import json
from mac_common import LS

_SOFTWARE = [
    [u"記事本 Notepad", u"TextEdit／備忘錄", LS(13)],
    [u"檔案總管 Explorer", u"Finder", LS(7)],
    [u"小畫家 Paint", u"預覽程式（標註）／繪圖 App", LS(14)],
    [u"小算盤 Calculator", u"計算機／Spotlight 打算式", LS(15)],
    [u"工作管理員 Task Manager", u"活動監視器", LS(39)],
    [u"控制台 Control Panel", u"系統設定", LS(29)],
    [u"命令提示字元 CMD", u"終端機 Terminal", LS(38)],
    [u"剪取工具 Snipping Tool", u"⌘⇧4 截圖（內建）", LS(20)],
    [u"檔案總管的「本機」", u"Finder 側邊欄（沒有 C 槽）", LS(6)],
    [u"設定 Settings", u"系統設定", LS(29)],
    [u"開始功能表", u"Spotlight（⌘空白）／Launchpad", LS(15)],
    [u"工作列", u"Dock", LS(16)],
]

_SHORTCUTS = [
    [u"複製 / 貼上 / 剪下", u"Ctrl+C / V / X", u"⌘C / ⌘V / ⌘X"],
    [u"復原 / 重做", u"Ctrl+Z / Ctrl+Y", u"⌘Z / ⌘⇧Z"],
    [u"全選 / 存檔 / 尋找", u"Ctrl+A / S / F", u"⌘A / ⌘S / ⌘F"],
    [u"列印", u"Ctrl+P", u"⌘P"],
    [u"關閉視窗", u"Ctrl+W / Alt+F4", u"⌘W"],
    [u"結束程式", u"Alt+F4", u"⌘Q"],
    [u"切換程式", u"Alt+Tab", u"⌘Tab（切 App）"],
    [u"切換同程式視窗", u"—", u"⌘`"],
    [u"搜尋", u"Win 鍵", u"⌘空白（Spotlight）"],
    [u"截圖（全螢幕 / 選取）", u"PrtSc / Win+Shift+S", u"⌘⇧3 / ⌘⇧4"],
    [u"強制結束當掉程式", u"Ctrl+Alt+Del", u"⌘⌥⎋"],
    [u"刪除檔案", u"Delete", u"⌘⌫（Command＋刪除）"],
    [u"重新命名", u"F2", u"選檔案按 Enter"],
    [u"切換輸入法", u"Win+空白 / Shift", u"⌃空白"],
]

_TERMS = [
    [u"C:\\ 磁碟", u"根目錄 /（沒有磁碟代號）", LS(6)],
    [u"反斜線 \\ 路徑", u"斜線 / 路徑", LS(6)],
    [u"捷徑 Shortcut", u"替身 Alias", LS(7)],
    [u"隱藏副檔名", u"預設隱藏（可開啟顯示）", LS(8)],
    [u"安裝精靈 Setup.exe", u"拖到「應用程式」（.dmg）", LS(10)],
    [u"解除安裝程式", u"拖到垃圾桶", LS(18)],
    [u".exe 執行檔", u".app（其實是資料夾）", LS(9)],
    [u"登錄檔 Registry", u"Library 裡的 .plist 設定檔", LS(12)],
    [u"回收桶", u"垃圾桶", LS(18)],
    [u"最大化", u"全螢幕（綠燈）/ 並排", LS(25)],
    [u"檔案總管的位址列", u"⌘⇧G 輸入路徑", LS(7)],
    [u"系統還原", u"Time Machine", LS(33)],
]

_CHEAT_BODY = [
    ("p", u"這一頁把 Windows 和 Mac 的<strong>軟體、快捷鍵、名詞</strong>做三張對照表,方便你隨時查。"
          u"想邊玩邊記快捷鍵,可以到<a href=\"shortcut-quiz.html\">互動快捷鍵練習器</a>。"),
    ("h", u"1. 軟體對照"),
    ("t", [u"Windows", u"Mac", u"課程"], _SOFTWARE),
    ("h", u"2. 快捷鍵對照"),
    ("p", u"最重要的一句話:大部分 <strong>Ctrl 換成 ⌘</strong> 就對了(" + LS(19) + u")。"),
    ("t", [u"動作", u"Windows", u"Mac"], _SHORTCUTS),
    ("h", u"3. 名詞與概念對照"),
    ("t", [u"Windows", u"Mac", u"課程"], _TERMS),
    ("h", u"4. 七個最重要的心態轉換"),
    ("ol", [u"把「Ctrl」的反射換成「⌘」(" + LS(19) + u")。",
            u"什麼都先按「⌘＋空白」搜尋(" + LS(15) + u")。",
            u"找不到功能?抬頭看螢幕最上方的選單列(" + LS(5) + u")。",
            u"關視窗 ≠ 結束 App,⌘Q 才是結束(" + LS(4) + u")。",
            u"沒有 C 槽 D 槽,所有東西在同一棵樹 / 底下(" + LS(6) + u")。",
            u"安裝＝拖到「應用程式」,移除＝丟垃圾桶(" + LS(10) + u")。",
            u"一定要設 Time Machine 備份(" + LS(33) + u")。"]),
]

CHEATSHEET = {
    "file": "cheatsheet.html",
    "title": u"Windows → Mac 對照速查表",
    "h1": u"Windows → Mac 對照速查表",
    "icon": u"🍎",
    "description": u"軟體、快捷鍵、名詞三張對照表,加上七個最重要的心態轉換,給 Windows 老手快速查閱",
    "body": _CHEAT_BODY,
}

# ---------- 互動快捷鍵練習器 ----------

_QUIZ = [
    {"q": u"複製選取的文字", "a": u"⌘C", "opts": [u"⌘C", u"Ctrl+C", u"⌥C", u"⌃C"]},
    {"q": u"貼上", "a": u"⌘V", "opts": [u"⌘V", u"Ctrl+V", u"⇧V", u"⌃V"]},
    {"q": u"結束（真正關掉）目前的 App", "a": u"⌘Q", "opts": [u"⌘Q", u"⌘W", u"Alt+F4", u"⌘⌫"]},
    {"q": u"關閉目前的視窗（不結束 App）", "a": u"⌘W", "opts": [u"⌘W", u"⌘Q", u"紅燈", u"⌘⇧W"]},
    {"q": u"打開 Spotlight 搜尋", "a": u"⌘空白", "opts": [u"⌘空白", u"⌃空白", u"⌘F", u"Win 鍵"]},
    {"q": u"截取整個螢幕", "a": u"⌘⇧3", "opts": [u"⌘⇧3", u"⌘⇧4", u"PrtSc", u"⌘3"]},
    {"q": u"自己框選範圍截圖", "a": u"⌘⇧4", "opts": [u"⌘⇧4", u"⌘⇧3", u"Win+Shift+S", u"⌘4"]},
    {"q": u"切換不同的 App", "a": u"⌘Tab", "opts": [u"⌘Tab", u"Alt+Tab", u"⌘`", u"⌃Tab"]},
    {"q": u"在同一個 App 的多個視窗間切換", "a": u"⌘`", "opts": [u"⌘`", u"⌘Tab", u"⌘~", u"⌃Tab"]},
    {"q": u"強制結束當掉（轉彩球）的 App", "a": u"⌘⌥⎋", "opts": [u"⌘⌥⎋", u"Ctrl+Alt+Del", u"⌘Q", u"⌘⌫"]},
    {"q": u"復原上一步", "a": u"⌘Z", "opts": [u"⌘Z", u"Ctrl+Z", u"⌘Y", u"⌥Z"]},
    {"q": u"尋找", "a": u"⌘F", "opts": [u"⌘F", u"Ctrl+F", u"⌘S", u"⌘G"]},
    {"q": u"存檔", "a": u"⌘S", "opts": [u"⌘S", u"Ctrl+S", u"⌘⇧S", u"⌘D"]},
    {"q": u"把選取的檔案丟到垃圾桶", "a": u"⌘⌫", "opts": [u"⌘⌫", u"Delete", u"⌫", u"⌘D"]},
]

_QUIZ_HTML = u"""<div class="content-figure" style="text-align:left">
  <div id="sq-card" style="border:1px solid var(--border);border-radius:12px;padding:20px;background:var(--surface)">
    <div id="sq-progress" style="color:var(--text-muted);font-size:0.85em"></div>
    <div id="sq-q" style="font-size:1.2em;font-weight:bold;margin:10px 0 16px">　</div>
    <div id="sq-opts" style="display:grid;grid-template-columns:repeat(2,1fr);gap:10px"></div>
    <div id="sq-fb" style="margin-top:14px;min-height:24px"></div>
    <button id="sq-next" style="display:none;font:inherit;margin-top:10px;padding:8px 18px;border-radius:8px;cursor:pointer;border:1px solid var(--border);background:var(--surface);color:var(--text)">下一題 ▶</button>
  </div>
  <p id="sq-score" style="margin:12px 0 0;color:var(--text-muted)"></p>
</div>
<script>
(function () {
  var QUIZ = %(quiz)s;
  var i = 0, correct = 0, answered = false, order = [];
  function shuffle(a){ a=a.slice(); for(var j=a.length-1;j>0;j--){var k=Math.floor(Math.random()*(j+1)),t=a[j];a[j]=a[k];a[k]=t;} return a; }
  var $ = function(id){ return document.getElementById(id); };
  function esc(s){ return String(s).replace(/[&<>]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;'}[c];}); }
  function start(){ order = shuffle(QUIZ.map(function(_,n){return n;})); i=0; correct=0; render(); }
  function render(){
    answered = false;
    var item = QUIZ[order[i]];
    $('sq-progress').textContent = '第 ' + (i+1) + ' / ' + order.length + ' 題';
    $('sq-q').textContent = 'Mac 上要「' + item.q + '」,按哪個?';
    $('sq-fb').textContent = ''; $('sq-next').style.display = 'none';
    var box = $('sq-opts'); box.innerHTML = '';
    shuffle(item.opts).forEach(function(op){
      var b = document.createElement('button');
      b.textContent = op;
      b.style.cssText = 'font:inherit;padding:12px;border-radius:8px;cursor:pointer;border:1.5px solid var(--border);background:var(--surface);color:var(--text)';
      b.onclick = function(){ pick(op, item.a, b); };
      box.appendChild(b);
    });
  }
  function pick(op, ans, btn){
    if (answered) return; answered = true;
    var buttons = $('sq-opts').querySelectorAll('button');
    buttons.forEach(function(b){
      b.disabled = true;
      if (b.textContent === ans) b.style.borderColor = '#5aa469', b.style.color = '#5aa469';
    });
    if (op === ans) { correct++; $('sq-fb').innerHTML = '<span style="color:#5aa469">✓ 答對了!</span>'; }
    else { btn.style.borderColor = '#e0605a'; btn.style.color = '#e0605a';
           $('sq-fb').innerHTML = '<span style="color:#e0605a">✗ 正確答案是 ' + esc(ans) + '</span>'; }
    $('sq-next').style.display = 'inline-block';
    $('sq-next').textContent = (i+1 < order.length) ? '下一題 ▶' : '看成績 🎉';
  }
  $('sq-next').onclick = function(){
    if (i+1 < order.length) { i++; render(); }
    else {
      $('sq-q').textContent = '練習完成!';
      $('sq-opts').innerHTML = ''; $('sq-fb').textContent = '';
      var pct = Math.round(correct/order.length*100);
      $('sq-score').textContent = '你答對 ' + correct + ' / ' + order.length + ' 題(' + pct + '%%)。';
      var b = document.createElement('button');
      b.textContent = '再玩一次 ↻';
      b.style.cssText = 'font:inherit;margin-top:6px;padding:8px 18px;border-radius:8px;cursor:pointer;border:1px solid var(--border);background:var(--surface);color:var(--text)';
      b.onclick = function(){ $('sq-score').textContent=''; b.remove(); start(); };
      $('sq-card').appendChild(b);
      $('sq-next').style.display = 'none'; $('sq-progress').textContent = '';
    }
  };
  start();
})();
</script>""" % {"quiz": json.dumps(_QUIZ, ensure_ascii=False)}

QUIZ = {
    "file": "shortcut-quiz.html",
    "title": u"互動快捷鍵練習器",
    "h1": u"互動快捷鍵練習器",
    "icon": u"⌨️",
    "description": u"用選擇題練習 Mac 的常用快捷鍵:看情境、選按鍵,立刻知道對錯,幫你把 ⌘ 的習慣練成肌肉記憶",
    "body": [
        ("p", u"這個小測驗幫你把 Mac 快捷鍵練熟。看情境,從四個選項挑出正確的按鍵組合,答完立刻知道對錯。"
              u"不確定的話,可以先複習 " + LS(19) + u"、" + LS(20) + u"。"),
        ("raw", _QUIZ_HTML),
        ("p", u"訣竅:大部分 Windows 的 <strong>Ctrl 換成 ⌘</strong> 就對了(" + LS(19) + u")。"
              u"多玩幾次,這些組合就會變成你的反射動作。"),
    ],
}

REFERENCES = [CHEATSHEET, QUIZ]
