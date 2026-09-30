# -*- coding: utf-8 -*-
"""檔案格式解剖學：兩個參考頁——魔術數字速查表、互動檔案解剖器。"""
from fmt_common import LS

# ---------- 速查表 ----------

_MAGIC_ROWS = [
    [u"PNG", u"89 50 4E 47 0D 0A 1A 0A", u"點陣圖（無損）", u"區塊：IHDR/IDAT/IEND", LS(13)],
    [u"JPG", u"FF D8 FF", u"照片（有損）", u"標記：SOI…SOS…EOI", LS(22)],
    [u"GIF", u"47 49 46 38（GIF8）", u"調色盤動圖", u"LZW、≤256 色", LS(15)],
    [u"BMP", u"42 4D（BM）", u"點陣圖（幾乎不壓）", u"由下往上、BGR", LS(12)],
    [u"TIFF", u"49 49 或 4D 4D", u"專業影像", u"標籤式、大小端都有", LS(16)],
    [u"PDF", u"25 50 44 46（%PDF）", u"跨裝置文件", u"物件＋xref，從檔尾讀", LS(45)],
    [u"ZIP", u"50 4B 03 04（PK..）", u"壓縮／封裝", u"DEFLATE、從檔尾讀", LS(44)],
    [u"gzip", u"1F 8B", u"單檔壓縮", u"DEFLATE", LS(9)],
    [u"7z", u"37 7A BC AF 27 1C", u"高壓縮封裝", u"固實壓縮", LS(47)],
    [u"RAR", u"52 61 72 21（Rar!）", u"壓縮封裝", u"有修復記錄", LS(47)],
    [u"MP3", u"49 44 33（ID3）或 FF FB", u"有損聲音", u"影格＋ID3 標籤", LS(33)],
    [u"WAV", u"52 49 46 46（RIFF）", u"未壓縮聲音", u"RIFF 容器、PCM", LS(30)],
    [u"FLAC", u"66 4C 61 43（fLaC）", u"無損聲音", u"完全還原", LS(35)],
    [u"MIDI", u"4D 54 68 64（MThd）", u"樂譜（非聲音）", u"事件＋VLQ 時間", LS(38)],
    [u"MP4", u"…66 74 79 70（ftyp）", u"影片容器", u"box：moov/mdat", LS(41)],
    [u"OLE（舊 doc）", u"D0 CF 11 E0", u"舊版 Office", u"檔中檔（複合文件）", LS(46)],
    [u"SQLite", u"53 51 4C 69 74 65（SQLite）", u"單檔資料庫", u"分頁、B-tree", LS(53)],
    [u"Class（Java）", u"CA FE BA BE", u"Java 位元組碼", u"給虛擬機執行", LS(38)],
    [u"ELF（Linux 執行檔）", u"7F 45 4C 46（.ELF）", u"執行檔", u"見姊妹課程", LS(2)],
    [u"EXE（Windows）", u"4D 5A（MZ）", u"執行檔", u"見姊妹課程", LS(2)],
]

_CHEAT_BODY = [
    ("p", u"這一頁把課程裡出現的格式整理成速查表，方便快速查閱。「魔術數字」是檔案開頭用來辨識格式的位元組（" + LS(2) + u"）。"
          u"也可以到<a href=\"file-inspector.html\">互動檔案解剖器</a>，直接拆解你自己的檔案。"),
    ("h", u"1. 常見格式的魔術數字與結構"),
    ("t", [u"格式", u"魔術數字（十六進位）", u"用途", u"結構重點", u"課程"], _MAGIC_ROWS),
    ("h", u"2. 三種壓縮的分類"),
    ("t", [u"類型", u"代表格式", u"特性"],
     [[u"無損（可完全還原）", u"PNG、FLAC、ZIP、7z", u"程式、文件、去背圖、典藏音樂（" + LS(6) + u"）"],
      [u"有損（丟掉感官察覺不到的）", u"JPG、MP3、AAC、影片", u"照片、聲音、影片（" + LS(10) + u"）"],
      [u"共用引擎 DEFLATE", u"ZIP、gzip、PNG", u"LZ77＋霍夫曼（" + LS(9) + u"）"]]),
    ("h", u"3. 反覆出現的設計概念"),
    ("t", [u"概念", u"說明", u"出現在"],
     [[u"魔術數字", u"開頭幾個位元組決定真正的格式", u"幾乎所有格式（" + LS(2) + u"）"],
      [u"區塊／容器", u"長度＋類型的積木，利於擴充與相容", u"PNG、MP4、ZIP、WAV（" + LS(5) + u"）"],
      [u"從檔尾讀", u"目錄放檔尾，方便增刪與快速跳讀", u"ZIP、PDF、MP4（" + LS(44) + u"）"],
      [u"大端 vs. 小端", u"多位元組整數的排列順序", u"PNG 大端、BMP／ZIP 小端（" + LS(3) + u"）"],
      [u"純文字＋結構", u"人機都可讀，但有編碼／換行陷阱", u"SVG、JSON、SRT、eml（" + LS(51) + u"）"],
      [u"容器 ≠ 編碼", u"外包裝和內部壓縮方式是兩回事", u"MP4、MKV、OGG（" + LS(39) + u"）"]]),
    ("h", u"4. 安全備忘"),
    ("ul", [u"副檔名可偽造，看<strong>魔術數字</strong>才準；打開系統的「顯示副檔名」（" + LS(62) + u"）。",
            u"危險的是<strong>可執行內容</strong>（.exe、巨集、腳本）與<strong>軟體漏洞</strong>，純資料檔相對安全。",
            u"檔案裡藏的常比你看到的多：EXIF 位置（" + LS(23) + u"）、PDF 遮不掉的文字（" + LS(45) + u"）、隱寫術（" + LS(63) + u"）。",
            u"重要資料靠<strong>備份與冗餘</strong>，不是事後修復（" + LS(61) + u"）。"]),
]

CHEATSHEET = {
    "file": "cheatsheet.html",
    "title": u"格式速查表",
    "h1": u"檔案格式速查表",
    "icon": u"🗂️",
    "description": u"常見格式的魔術數字、用途、結構重點與壓縮分類，加上反覆出現的設計概念與安全備忘",
    "body": _CHEAT_BODY,
}

# ---------- 互動檔案解剖器 ----------

_INSPECTOR_HTML = u"""<div class="content-figure" style="text-align:left">
  <p style="margin:0 0 10px">選一個你電腦裡的檔案（圖片、聲音、壓縮檔、文件都行）。
  <strong>檔案完全不會上傳</strong>，所有分析都在你的瀏覽器裡進行。</p>
  <input type="file" id="fi-file" style="font:inherit">
  <div id="fi-out" style="margin-top:14px"></div>
</div>
<script>
(function () {
  var SIGS = [
    {n:"PNG 影像", b:[0x89,0x50,0x4E,0x47], why:"區塊結構：IHDR/IDAT/IEND"},
    {n:"JPG 照片", b:[0xFF,0xD8,0xFF], why:"標記結構：SOI…SOS…EOI"},
    {n:"GIF 動圖", b:[0x47,0x49,0x46,0x38], why:"調色盤 + LZW"},
    {n:"BMP 點陣圖", b:[0x42,0x4D], why:"幾乎不壓縮，由下往上、BGR"},
    {n:"PDF 文件", b:[0x25,0x50,0x44,0x46], why:"物件 + 交叉參照表"},
    {n:"ZIP / docx / epub / apk", b:[0x50,0x4B,0x03,0x04], why:"DEFLATE 壓縮，或當作容器"},
    {n:"gzip", b:[0x1F,0x8B], why:"DEFLATE"},
    {n:"7z", b:[0x37,0x7A,0xBC,0xAF], why:"固實壓縮"},
    {n:"RAR", b:[0x52,0x61,0x72,0x21], why:"有修復記錄"},
    {n:"MP3（有 ID3）", b:[0x49,0x44,0x33], why:"影格 + ID3 標籤"},
    {n:"MP3（無標籤）", b:[0xFF,0xFB], why:"影格 + ID3 標籤"},
    {n:"WAV / AVI", b:[0x52,0x49,0x46,0x46], why:"RIFF 容器"},
    {n:"FLAC 無損聲音", b:[0x66,0x4C,0x61,0x43], why:"無損壓縮"},
    {n:"MIDI 樂譜", b:[0x4D,0x54,0x68,0x64], why:"事件 + 可變長度時間"},
    {n:"OLE（舊版 Office）", b:[0xD0,0xCF,0x11,0xE0], why:"檔中檔（複合文件）"},
    {n:"SQLite 資料庫", b:[0x53,0x51,0x4C,0x69,0x74,0x65], why:"分頁 + B-tree"},
    {n:"Java class", b:[0xCA,0xFE,0xBA,0xBE], why:"位元組碼，給虛擬機"},
    {n:"ELF（Linux 執行檔）", b:[0x7F,0x45,0x4C,0x46], why:"見姊妹課程"},
    {n:"EXE（Windows 執行檔）", b:[0x4D,0x5A], why:"見姊妹課程"}
  ];
  var input = document.getElementById('fi-file'), out = document.getElementById('fi-out');
  function hex(b) { return ('0' + b.toString(16).toUpperCase()).slice(-2); }
  function esc(s) { return s.replace(/[&<>]/g, function (c) { return {'&':'&amp;','<':'&lt;','>':'&gt;'}[c]; }); }
  function match(bytes) {
    // MP4 的 ftyp 在第 4 位元組
    if (bytes.length >= 8 && bytes[4]===0x66 && bytes[5]===0x74 && bytes[6]===0x79 && bytes[7]===0x70)
      return {n:"MP4 / MOV 影片", why:"box 結構：moov / mdat"};
    for (var i = 0; i < SIGS.length; i++) {
      var s = SIGS[i], ok = true;
      for (var j = 0; j < s.b.length; j++) if (bytes[j] !== s.b[j]) { ok = false; break; }
      if (ok) return s;
    }
    return null;
  }
  input.addEventListener('change', function () {
    var f = input.files[0];
    if (!f) return;
    var r = new FileReader();
    r.onload = function () {
      var all = new Uint8Array(r.result);
      var bytes = all.subarray(0, 64);
      var m = match(all);
      var ext = (f.name.split('.').pop() || '').toLowerCase();
      var html = '<div style="border:1px solid var(--border);border-radius:10px;padding:14px;background:var(--surface)">';
      html += '<div style="margin-bottom:8px"><strong>' + esc(f.name) + '</strong>（' + all.length.toLocaleString() + ' 位元組）</div>';
      if (m) {
        html += '<div style="font-size:1.05em;color:var(--accent);margin-bottom:4px">辨識結果：<strong>' + esc(m.n) + '</strong></div>';
        html += '<div style="color:var(--text-muted);margin-bottom:8px">結構重點：' + esc(m.why) + '</div>';
      } else {
        html += '<div style="color:var(--text-muted);margin-bottom:8px">開頭位元組不在速查表中——可能是純文字，或本課未收錄的格式。</div>';
      }
      // 副檔名是否相符
      var extMap = {png:'PNG',jpg:'JPG',jpeg:'JPG',gif:'GIF',bmp:'BMP',pdf:'PDF',zip:'ZIP',docx:'ZIP',xlsx:'ZIP',pptx:'ZIP',epub:'ZIP',apk:'ZIP',gz:'gzip',mp3:'MP3',wav:'WAV',flac:'FLAC',mid:'MIDI',midi:'MIDI',mp4:'MP4',mov:'MP4',db:'SQLite',sqlite:'SQLite',exe:'EXE'};
      if (m && extMap[ext] && m.n.indexOf(extMap[ext]) === -1 && !(extMap[ext]==='ZIP' && m.n.indexOf('ZIP')>=0)) {
        html += '<div style="color:#e0605a;margin-bottom:8px">⚠ 副檔名是 .' + esc(ext) + '，但內容看起來是「' + esc(m.n) + '」——名不符實，請提高警覺。</div>';
      }
      // hex dump 前 64 位元組
      html += '<div style="font-family:ui-monospace,Menlo,Consolas,monospace;font-size:0.82em;line-height:1.6;white-space:pre;overflow-x:auto">';
      for (var off = 0; off < bytes.length; off += 16) {
        var hexpart = '', asc = '';
        for (var k = 0; k < 16; k++) {
          if (off + k < bytes.length) {
            var bv = bytes[off + k];
            hexpart += hex(bv) + ' ';
            asc += (bv >= 32 && bv < 127) ? String.fromCharCode(bv) : '·';
          } else hexpart += '   ';
        }
        html += ('000' + off.toString(16)).slice(-4).toUpperCase() + '  ' + hexpart + ' ' + esc(asc) + '\\n';
      }
      html += '</div></div>';
      out.innerHTML = html;
    };
    r.readAsArrayBuffer(f.size > 8388608 ? f.slice(0, 8388608) : f);
  });
})();
</script>"""

INSPECTOR = {
    "file": "file-inspector.html",
    "title": u"互動檔案解剖器",
    "h1": u"互動檔案解剖器：拆解你自己的檔案",
    "icon": u"🔬",
    "description": u"在瀏覽器裡選一個本機檔案（不會上傳），辨識它的真實格式、比對副檔名、顯示開頭 64 位元組的十六進位",
    "body": [
        ("p", u"這個工具讓你把課堂上學的「用魔術數字辨識格式」實際用在自己的檔案上。"
              u"<strong>檔案只在你的瀏覽器裡讀取，不會上傳到任何伺服器。</strong>"),
        ("raw", _INSPECTOR_HTML),
        ("h", u"它會告訴你什麼"),
        ("ul", [u"<strong>真實格式</strong>：依開頭的魔術數字判斷，而不是看副檔名（" + LS(2) + u"）。",
                u"<strong>名不符實的警告</strong>：如果副檔名和內容對不上（例如 .jpg 其實是執行檔），會特別提醒（" + LS(62) + u"）。",
                u"<strong>十六進位</strong>：顯示開頭 64 個位元組，就像一個小型 Hex 檢視器（" + LS(1) + u"）。"]),
        ("p", u"試試看：把一個 <code>.docx</code> 丟進來，它會被辨識成 ZIP（" + LS(45) + u"）；"
              u"把一張照片改名成 <code>.txt</code> 再丟進來，它仍會認出真正的格式。"),
    ],
}

REFERENCES = [CHEATSHEET, INSPECTOR]
