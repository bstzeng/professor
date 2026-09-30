# -*- coding: utf-8 -*-
"""晶片 layout：兩個獨立參考頁——術語速查表，與互動式 layout 逐層觀察器。"""
from cl_common import LS, LAYER, T, TXT, BLUE, GREEN, MUTED

# ---------- 速查表 ----------

CHEATSHEET = {
    "file": "cheatsheet.html",
    "title": u"晶片設計速查表",
    "h1": u"晶片設計術語與流程速查表",
    "icon": u"🗂️",
    "description": u"常見術語中英對照、設計流程總表，以及各階段的工具與檔案格式",
    "body": [
        ("p", u"這一頁整理課程中出現的主要術語、流程與檔案格式，點課號可以回到詳細內容。"),
        ("h", u"1. 設計流程與檔案格式"),
        ("t", [u"階段", u"輸入", u"輸出", u"課程"],
         [[u"架構", u"產品需求", u"規格書、架構文件", LS(14)],
          [u"RTL 設計", u"規格", u"Verilog／VHDL（或 C++ 經 HLS）", LS(15) + u"、" + LS(18)],
          [u"邏輯合成", u"RTL、.lib、SDC", u"Gate-level netlist", LS(17)],
          [u"實體設計", u"Netlist、LEF、.lib、SDC", u"DEF／資料庫", LS(20) + u"～" + LS(29)],
          [u"寄生萃取", u"繞線後設計", u"SPEF", LS(29)],
          [u"簽核", u"Netlist、SPEF、GDS", u"時序／功耗／DRC／LVS 報告", LS(30) + u"～" + LS(35)],
          [u"交付", u"整合完成的設計", u"GDSII／OASIS", LS(2) + u"、" + LS(40)],
          [u"FPGA", u"RTL", u"Bitstream", LS(19)]]),
        ("h", u"2. 常見檔案格式"),
        ("t", [u"格式", u"內容", u"課程"],
         [[u"Verilog／SystemVerilog", u"硬體描述；也用來存 gate-level netlist", LS(15)],
          [u"SDC", u"時脈、I/O 延遲等時序限制", LS(17)],
          [u"Liberty（.lib）", u"元件的功能、延遲、功耗模型", LS(12)],
          [u"LEF", u"元件與製程的抽象實體資訊", LS(12)],
          [u"DEF", u"設計的擺放與繞線狀態", LS(20)],
          [u"SPEF", u"寄生電阻電容", LS(29)],
          [u"UPF", u"電源域與低功耗意圖", LS(34)],
          [u"GDSII／OASIS", u"最終的多層幾何圖形", LS(2)]]),
        ("h", u"3. 術語中英對照"),
        ("t", [u"英文", u"中文", u"一句話說明", u"課程"],
         [[u"Wafer／Die", u"晶圓／晶粒", u"整片矽／切下來的一顆晶片", LS(1)],
          [u"Layout", u"佈局", u"晶片各層的幾何圖案", LS(2)],
          [u"FEOL／BEOL", u"前段／後段製程", u"電晶體／金屬導線", LS(3)],
          [u"PDK", u"製程設計套件", u"晶圓廠提供的規則、模型與元件庫", LS(4)],
          [u"Active／Poly", u"擴散區／閘極", u"一條 poly 跨過 active 就是一顆電晶體", LS(5)],
          [u"CMOS", u"互補式金氧半", u"PMOS 與 NMOS 成對的邏輯結構", LS(6)],
          [u"Design rule", u"設計規則", u"寬度、間距、包覆等製程限制", LS(8)],
          [u"FinFET／GAA", u"鰭式／環繞式閘極電晶體", u"閘極從多面包住通道", LS(9)],
          [u"Standard cell", u"標準元件", u"固定高度、預先畫好的邏輯積木", LS(10)],
          [u"PVT corner", u"製程電壓溫度角落", u"元件最快／最慢的條件組合", LS(12)],
          [u"RTL", u"暫存器傳輸層級", u"以時脈週期描述資料流動", LS(15)],
          [u"Synthesis", u"邏輯合成", u"RTL → 邏輯閘 netlist", LS(17)],
          [u"PPA", u"效能、功耗、面積", u"設計最佳化的三個目標", LS(17)],
          [u"HLS", u"高階合成", u"C／C++ → RTL", LS(18)],
          [u"FPGA／ASIC", u"可程式邏輯陣列／特定應用晶片", u"可重新配置／專門製造", LS(19)],
          [u"APR／PnR", u"自動擺放與繞線", u"實體設計的主流程", LS(20)],
          [u"Floorplan", u"平面規劃", u"晶片大小、macro 與 I/O 位置", LS(21)],
          [u"Macro", u"巨集區塊", u"SRAM、類比 IP 等大型預製區塊", LS(21)],
          [u"IR drop／EM", u"電壓降／電遷移", u"電源網路的兩大問題", LS(22)],
          [u"Congestion", u"擁擠度", u"繞線需求超過可用軌道", LS(23)],
          [u"Timing closure", u"時序收斂", u"反覆修正直到時序達標", LS(24)],
          [u"CTS", u"時脈樹合成", u"把時脈平衡地送到所有正反器", LS(25)],
          [u"Skew／Latency", u"時脈偏移／插入延遲", u"時脈到達的時間差／總延遲", LS(26)],
          [u"Via", u"介層窗", u"連接相鄰金屬層", LS(27)],
          [u"Antenna effect", u"天線效應", u"長線在製程中收集電荷損傷閘極", LS(28)],
          [u"Crosstalk", u"串擾", u"相鄰導線的耦合雜訊", LS(29)],
          [u"ECO", u"工程變更", u"後期的局部修改", LS(29)],
          [u"STA／Slack", u"靜態時序分析／時序餘裕", u"檢查所有路徑是否趕得上", LS(30)],
          [u"Setup／Hold", u"建立時間／保持時間", u"資料不能太晚到／不能太早變", LS(30)],
          [u"OCV", u"晶片內變異", u"同一顆晶片上的快慢差異", LS(31)],
          [u"DRC／LVS", u"設計規則檢查／佈局電路比對", u"做不做得出來／接得對不對", LS(32) + u"、" + LS(33)],
          [u"ESD", u"靜電放電", u"I/O 需要保護電路", LS(34)],
          [u"DFM／CMP", u"可製造性設計／化學機械研磨", u"提升良率、保持平坦", LS(35)],
          [u"Common centroid", u"共質心", u"類比元件匹配的排列法", LS(36)],
          [u"Guard ring", u"保護環", u"隔離雜訊、防止閂鎖", LS(37)],
          [u"Tape-out／MPW", u"下線／多專案晶圓", u"交付 GDSII／共用光罩", LS(40)],
          [u"OPC／EUV", u"光學鄰近修正／極紫外光", u"補償曝光變形／更短波長的微影", LS(41)],
          [u"DFT／ATPG／BIST", u"可測試性設計／自動測試圖樣／內建自我測試", u"讓晶片能被測試", LS(42)],
          [u"Chiplet／CoWoS", u"小晶片／台積電 2.5D 封裝", u"多顆晶片封成一個系統", LS(45)]]),
        ("h", u"4. Layout 圖層顏色（本課程的畫法）"),
        ("t", [u"圖層", u"意義"],
         [[LAYER[k][2], d] for k, d in (
             ("nwell", u"PMOS 所在的 N 型井"), ("active", u"電晶體的源極、汲極與通道區域"),
             ("poly", u"閘極"), ("contact", u"從電晶體接到 Metal 1"), ("m1", u"第一層金屬導線"),
             ("via", u"金屬層之間的連接"), ("m2", u"第二層金屬導線"))]),
        ("p", u"不同公司與工具的配色各不相同；這裡只是本課程圖解使用的慣例。"),
    ],
}

# ---------- 互動 layout 觀察器 ----------

INV = [("nwell", 60, 20, 240, 125), ("active", 105, 70, 150, 50), ("active", 105, 170, 150, 42),
       ("poly", 172, 55, 16, 172), ("poly", 150, 122, 50, 24),
       ("contact", 125, 88, 10, 10), ("contact", 221, 88, 10, 10), ("contact", 125, 186, 10, 10),
       ("contact", 221, 186, 10, 10), ("contact", 170, 129, 10, 10),
       ("m1", 60, 28, 240, 22), ("m1", 60, 250, 240, 22), ("m1", 118, 40, 24, 70), ("m1", 118, 176, 24, 86),
       ("m1", 214, 80, 24, 126), ("m1", 214, 150, 86, 16), ("m1", 60, 126, 104, 16)]

NAND = [("nwell", 40, 20, 280, 120), ("active", 80, 70, 200, 48), ("active", 80, 172, 200, 40),
        ("poly", 140, 55, 14, 172), ("poly", 206, 55, 14, 172),
        ("contact", 96, 87, 10, 10), ("contact", 173, 87, 10, 10), ("contact", 252, 87, 10, 10),
        ("contact", 96, 186, 10, 10), ("contact", 252, 186, 10, 10),
        ("m1", 40, 28, 280, 20), ("m1", 40, 250, 280, 20), ("m1", 90, 38, 22, 66), ("m1", 246, 38, 22, 66),
        ("m1", 167, 80, 22, 60), ("m1", 167, 128, 101, 16), ("m1", 246, 128, 22, 78), ("m1", 90, 180, 22, 82)]

ORDER = ["nwell", "active", "poly", "contact", "m1"]

DESC = {
    "nwell": u"N 型井：PMOS 必須做在這個區域裡。",
    "active": u"擴散區：電晶體的源極、汲極與通道所在的地方。",
    "poly": u"閘極：一條 poly 跨過 active，就形成一顆電晶體。",
    "contact": u"接觸窗：把電晶體的源極、汲極與閘極，往上連到第一層金屬。",
    "m1": u"第一層金屬：電源軌（VDD／GND）、輸入、輸出與電晶體之間的連線。",
}


def _cell_svg(cell_id, shapes, labels, hidden=False):
    groups = []
    for k in ORDER:
        c, op, _ = LAYER[k]
        rects = "".join(
            u'<rect x="%d" y="%d" width="%d" height="%d" rx="%d" fill="%s" fill-opacity="%g" stroke="%s" stroke-width="1.2"/>'
            % (x, y, w, h, 1 if k == "contact" else 2, c, op, c)
            for kk, x, y, w, h in shapes if kk == k)
        groups.append(u'<g data-layer="%s">%s</g>' % (k, rects))
    style = u' style="display:none"' if hidden else u""
    return (u'<svg id="%s" class="content-diagram lv-cell" viewBox="0 0 360 290" xmlns="http://www.w3.org/2000/svg"%s>'
            u'%s%s</svg>') % (cell_id, style, u"".join(groups), labels)


_INV_LABELS = (T(180, 44, "VDD", 10, TXT) + T(180, 266, "GND", 10, TXT)
               + T(66, 120, u"輸入 A", 9, BLUE, "start") + T(296, 180, u"輸出 Y", 9, BLUE, "end")
               + T(265, 100, "PMOS", 9, GREEN, "start") + T(265, 196, "NMOS", 9, GREEN, "start"))
_NAND_LABELS = (T(180, 42, "VDD", 10, TXT) + T(180, 266, "GND", 10, TXT)
                + T(147, 240, "A", 10, "#e0605a") + T(213, 240, "B", 10, "#e0605a") + T(300, 148, "Y", 10, BLUE))

_TOGGLES = u"".join(
    u'<label style="display:inline-flex;align-items:center;gap:6px;margin:4px 12px 4px 0;cursor:pointer">'
    u'<input type="checkbox" value="%s" checked>'
    u'<span style="display:inline-block;width:14px;height:14px;border-radius:3px;background:%s;opacity:%g;border:1px solid %s"></span>'
    u'%s</label>' % (k, LAYER[k][0], max(LAYER[k][1], 0.35), LAYER[k][0], LAYER[k][2])
    for k in ORDER)

_BTN = (u'style="font:inherit;padding:6px 14px;margin:4px 8px 4px 0;border-radius:8px;cursor:pointer;'
        u'border:1px solid var(--border);background:var(--surface);color:var(--text)"')

_VIEWER_HTML = u"""<div class="content-figure" style="text-align:left">
  <div style="margin-bottom:8px">
    <button type="button" class="lv-cellbtn" data-cell="lv-inv" %(btn)s>反相器（NOT）</button>
    <button type="button" class="lv-cellbtn" data-cell="lv-nand" %(btn)s>NAND2</button>
  </div>
  <div style="text-align:center">
    %(inv)s
    %(nand)s
  </div>
  <div class="lv-toggles" style="margin-top:8px">%(toggles)s</div>
  <div style="margin-top:8px">
    <button type="button" id="lv-all" %(btn)s>全部顯示</button>
    <button type="button" id="lv-play" %(btn)s>▶ 逐層疊上去</button>
  </div>
  <p id="lv-desc" style="margin:10px 0 0;color:var(--text-muted);min-height:1.6em">勾選或取消各圖層，看看它們怎麼疊出一個邏輯閘。</p>
</div>
<script>
(function () {
  var desc = %(desc)s;
  var order = %(order)s;
  var boxes = Array.prototype.slice.call(document.querySelectorAll('.lv-toggles input'));
  var descEl = document.getElementById('lv-desc');
  var timer = null;
  function apply() {
    boxes.forEach(function (cb) {
      var groups = document.querySelectorAll('.lv-cell [data-layer="' + cb.value + '"]');
      Array.prototype.forEach.call(groups, function (g) { g.style.display = cb.checked ? '' : 'none'; });
    });
  }
  function stop() { if (timer) { clearTimeout(timer); timer = null; } }
  boxes.forEach(function (cb) {
    cb.addEventListener('change', function () {
      stop(); apply();
      if (cb.checked) descEl.textContent = desc[cb.value];
    });
  });
  document.getElementById('lv-all').addEventListener('click', function () {
    stop(); boxes.forEach(function (cb) { cb.checked = true; }); apply();
    descEl.textContent = '所有圖層疊在一起，就是 layout 工具中看到的畫面。';
  });
  document.getElementById('lv-play').addEventListener('click', function () {
    stop(); boxes.forEach(function (cb) { cb.checked = false; }); apply();
    var i = 0;
    (function step() {
      if (i >= order.length) { timer = null; return; }
      var k = order[i++];
      boxes.forEach(function (cb) { if (cb.value === k) cb.checked = true; });
      apply(); descEl.textContent = desc[k];
      timer = setTimeout(step, 1600);
    })();
  });
  Array.prototype.forEach.call(document.querySelectorAll('.lv-cellbtn'), function (btn) {
    btn.addEventListener('click', function () {
      Array.prototype.forEach.call(document.querySelectorAll('.lv-cell'), function (svg) {
        svg.style.display = svg.id === btn.getAttribute('data-cell') ? '' : 'none';
      });
    });
  });
})();
</script>""" % {
    "btn": _BTN,
    "inv": _cell_svg("lv-inv", INV, _INV_LABELS),
    "nand": _cell_svg("lv-nand", NAND, _NAND_LABELS, hidden=True),
    "toggles": _TOGGLES,
    "desc": "{" + ",".join('"%s":"%s"' % (k, v) for k, v in DESC.items()) + "}",
    "order": "[" + ",".join('"%s"' % k for k in ORDER) + "]",
}

VIEWER = {
    "file": "layout-viewer.html",
    "title": u"互動 layout 觀察器",
    "h1": u"互動 layout 觀察器：逐層看懂一個邏輯閘",
    "icon": u"🔍",
    "description": u"逐層開關 N-well、Active、Poly、Contact、Metal 1，看反相器與 NAND2 是怎麼疊出來的",
    "body": [
        ("p", u"這個小工具搭配" + LS(5) + u"～" + LS(7) + u"使用。選擇一個邏輯閘，勾選或取消下方的圖層，"
              u"或按「逐層疊上去」看它一層一層長出來。"),
        ("raw", _VIEWER_HTML),
        ("h", u"觀察重點"),
        ("ul", [u"<strong>只打開 Active 和 Poly</strong>：每一個紅色跨過綠色的地方，就是一顆電晶體。反相器有 2 顆，NAND2 有 4 顆。",
                u"<strong>打開 N-well</strong>：上半部的電晶體在井裡面，是 PMOS；下半部是 NMOS。",
                u"<strong>NAND2 的下半部</strong>：兩條 poly 之間的擴散區沒有 contact，因為兩顆 NMOS 串聯、共用擴散區（" + LS(7) + u"）。",
                u"<strong>打開 Metal 1</strong>：找找看哪一條是 VDD、哪一條是 GND、輸出從哪裡接出來。"]),
    ],
}

REFERENCES = [CHEATSHEET, VIEWER]
