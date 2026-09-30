# -*- coding: utf-8 -*-
"""心率與有氧運動：兩個參考頁——速查表、互動心率區間計算器。"""
import json
from hr_common import LS, SAFETY, ZONES, LT_ZONES, MAXHR_FORMULAS

_SAFE = (u"raw", u'<p style="color:var(--text-muted);font-size:0.9em">🩺 %s</p>' % SAFETY)

CHEATSHEET = {
    "file": "cheatsheet.html",
    "title": u"心率與有氧速查表",
    "h1": u"心率與有氧運動速查表",
    "icon": u"🗂️",
    "description": u"公式、五區間的感受與訓練目的、談話測試對照、常見正常值與警訊，一頁查完",
    "body": [
        ("p", u"這一頁整理課程中最常用到的公式與數字。想直接算出自己的區間，請到"
              u"<a href=\"hr-zone-calculator.html\">心率區間計算器</a>。"),
        ("h", u"1. 公式"),
        ("t", [u"項目", u"公式", u"課程"],
         [[u"心輸出量", u"心率 × 每搏輸出量", LS(3)],
          [u"攝氧量（菲克方程式）", u"心輸出量 × 動靜脈含氧差", LS(11)],
          [u"最大心率（常用）", u"220 − 年齡", LS(5)],
          [u"最大心率（較推薦）", u"208 − 0.7 × 年齡（Tanaka）", LS(5)],
          [u"儲備心率", u"最大心率 − 靜止心率", LS(16)],
          [u"Karvonen 目標心率", u"（最大心率 − 靜止心率）× % ＋ 靜止心率", LS(16)],
          [u"% 最大心率 ↔ % 最大攝氧量", u"% 最大心率 ≈ 0.64 × % 最大攝氧量 ＋ 37", LS(12)],
          [u"1 MET", u"3.5 mL／kg／分 的攝氧量", LS(11)]]),
        ("h", u"2. 五區間"),
        ("t", [u"區間", u"% 最大心率", u"% 乳酸閾值心率", u"談話測試", u"主要目的"],
         [[z[0], u"%d～%d%%" % (z[1], z[2]),
           (u"&lt; %d%%" % lt[2]) if i == 0 else (u"%d%% 以上" % lt[1] if i == 4 else u"%d～%d%%" % (lt[1], lt[2] - 1)),
           z[3], z[4]] for i, (z, lt) in enumerate(zip(ZONES, LT_ZONES))]),
        ("p", u"不同品牌、教練的區間切法不同；選一種方法固定使用，並用談話測試校正（" + LS(16) + u"、" + LS(17) + u"）。"),
        ("h", u"3. 自覺強度對照"),
        ("t", [u"RPE（0～10）", u"Borg（6～20）", u"感受", u"大約區間"],
         [[u"1～2", u"7～10", u"很輕鬆，可以唱歌", u"Z1"],
          [u"3～4", u"11～12", u"輕鬆，可以完整聊天", u"Z2"],
          [u"5～6", u"13～14", u"有點吃力，只能說短句", u"Z3"],
          [u"7～8", u"15～17", u"吃力，只能說幾個字", u"Z4"],
          [u"9～10", u"18～20", u"極度吃力，說不出話", u"Z5"]]),
        ("h", u"4. 常見參考值（成人，約略）"),
        ("t", [u"項目", u"約略範圍", u"課程"],
         [[u"靜止心率", u"60～100（規律運動者常低於 60）", LS(4)],
          [u"1 分鐘心率恢復（緩走）", u"12 下以內偏慢；20 下以上良好", LS(23)],
          [u"最大攝氧量", u"一般成人約 30～45 mL／kg／分；頂尖耐力選手 70～85 以上", LS(13)],
          [u"第一閾值心率", u"約 70～80% 最大心率", LS(14)],
          [u"第二閾值心率", u"約 85～92% 最大心率", LS(14)],
          [u"世界衛生組織每週建議", u"中等強度 150～300 分鐘，或高強度 75～150 分鐘；另加 2 天肌力", LS(34)]]),
        ("h", u"5. 讓心率偏高的常見原因"),
        ("t", [u"原因", u"大約影響", u"課程"],
         [[u"長時間運動（心率飄移）", u"一小時可多 10～20 下", LS(26)],
          [u"高溫、潮濕", u"同配速多約 10 下以上", LS(27)],
          [u"脫水", u"每流失 1% 體重約多 3～5 下", LS(27)],
          [u"初到高海拔", u"靜止心率多 5～15 下", LS(27)],
          [u"發燒", u"每升高 1°C 約多 10 下", LS(28)],
          [u"睡眠不足、壓力、飲酒", u"靜止心率上升、HRV 下降", LS(28)]]),
        ("h", u"6. 立即停止運動的警訊"),
        ("ul", [u"胸痛、胸悶、壓迫感，延伸到手臂、下巴或背部。",
                u"頭暈、眼前發黑、昏倒。",
                u"與強度不相稱的呼吸困難。",
                u"心跳突然非常快、亂跳或漏拍。",
                u"冒冷汗、噁心、臉色蒼白。"]),
        ("p", u"症狀沒有很快緩解，或出現胸痛、昏厥，請立即撥打 119（" + LS(36) + u"）。"),
        _SAFE,
    ],
}

# ---------- 互動計算器 ----------

_INPUT = (u'style="font:inherit;width:6.5em;padding:6px 8px;border-radius:6px;border:1px solid var(--border);'
          u'background:var(--surface);color:var(--text)"')
_BTN = (u'style="font:inherit;padding:8px 16px;margin:4px 8px 4px 0;border-radius:8px;cursor:pointer;'
        u'border:1px solid var(--border);background:var(--surface);color:var(--text)"')

_ZC = ["#8a8f98", "#4a90c2", "#5aa469", "#ff8a65", "#e0605a"]
_DATA = {
    "zones": [[z[0], z[1], z[2], z[3]] for z in ZONES],
    "lt": [[a, b, c] for a, b, c in LT_ZONES],
    "colors": _ZC,
    "formulas": [name for name, f in MAXHR_FORMULAS],
}

_CALC_HTML = u"""<div class="content-figure" style="text-align:left">
  <div style="display:flex;flex-wrap:wrap;gap:12px 20px;align-items:flex-end">
    <label>年齡<br><input type="number" id="hz-age" min="10" max="100" value="40" INPUT></label>
    <label>靜止心率<br><input type="number" id="hz-rest" min="30" max="120" value="60" INPUT></label>
    <label>實測最大心率（選填）<br><input type="number" id="hz-max" min="100" max="230" placeholder="—" INPUT></label>
    <label>乳酸閾值心率（選填）<br><input type="number" id="hz-lt" min="90" max="220" placeholder="—" INPUT></label>
  </div>
  <div style="margin-top:10px">
    <button type="button" id="hz-calc" BTN>計算</button>
    <button type="button" id="hz-reset" BTN>還原範例</button>
  </div>
  <p id="hz-msg" style="margin:10px 0 0;color:var(--text-muted)"></p>
  <div id="hz-out" style="overflow-x:auto"></div>
</div>
<script>
(function () {
  var D = DATA;
  var $ = function (id) { return document.getElementById(id); };
  var out = $('hz-out'), msg = $('hz-msg');
  function num(id) { var v = parseFloat($(id).value); return isNaN(v) ? null : v; }
  function r(x) { return Math.round(x); }
  function table(head, rows) {
    var h = '<table><thead><tr>' + head.map(function (c) { return '<th>' + c + '</th>'; }).join('') + '</tr></thead><tbody>';
    rows.forEach(function (row) { h += '<tr>' + row.map(function (c) { return '<td>' + c + '</td>'; }).join('') + '</tr>'; });
    return h + '</tbody></table>';
  }
  function chip(i, name) {
    return '<span style="display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:6px;background:' + D.colors[i] + '"></span>' + name;
  }
  function calc() {
    var age = num('hz-age'), rest = num('hz-rest'), mmax = num('hz-max'), lt = num('hz-lt');
    if (age === null || age < 10 || age > 100) { msg.textContent = '請輸入 10～100 之間的年齡。'; out.innerHTML = ''; return; }
    if (rest === null || rest < 30 || rest > 120) { msg.textContent = '請輸入 30～120 之間的靜止心率。'; out.innerHTML = ''; return; }
    var est = [220 - age, 208 - 0.7 * age, 207 - 0.7 * age, 211 - 0.64 * age];
    var maxhr = mmax !== null ? mmax : r(est[1]);
    if (maxhr <= rest + 20) { msg.textContent = '最大心率必須明顯高於靜止心率，請檢查輸入。'; out.innerHTML = ''; return; }
    msg.textContent = '使用的最大心率：' + maxhr + (mmax !== null ? '（實測）' : '（Tanaka 公式估計）') +
      '；儲備心率：' + (maxhr - rest) + '。';
    var h = '<h3>最大心率公式比較</h3>' +
      table(['公式', '估計值'], D.formulas.map(function (f, i) { return [f, r(est[i])]; }));
    h += '<h3>最大心率百分比法</h3>' + table(['區間', '% 最大心率', '心率範圍', '感受'],
      D.zones.map(function (z, i) { return [chip(i, z[0]), z[1] + '～' + z[2] + '%', r(maxhr * z[1] / 100) + '～' + r(maxhr * z[2] / 100), z[3]]; }));
    h += '<h3>儲備心率法（Karvonen）</h3>' + table(['區間', '% 儲備心率', '心率範圍'],
      D.zones.map(function (z, i) {
        return [chip(i, z[0]), z[1] + '～' + z[2] + '%',
          r(rest + (maxhr - rest) * z[1] / 100) + '～' + r(rest + (maxhr - rest) * z[2] / 100)];
      }));
    if (lt !== null) {
      if (lt >= maxhr || lt <= rest) {
        h += '<p>乳酸閾值心率應介於靜止心率與最大心率之間，請檢查輸入。</p>';
      } else {
        h += '<h3>乳酸閾值心率法（LTHR ' + lt + '）</h3>' + table(['區間', '% LTHR', '心率範圍'],
          D.lt.map(function (z, i) {
            var lo = i === 0 ? '—' : r(lt * z[1] / 100);
            var hi = i === 4 ? Math.min(maxhr, r(lt * z[2] / 100)) : r(lt * z[2] / 100) - 1;
            var pct = i === 0 ? '低於 ' + z[2] + '%' : (i === 4 ? z[1] + '% 以上' : z[1] + '～' + (z[2] - 1) + '%');
            return [chip(i, z[0]), pct, (i === 0 ? '低於 ' + hi : lo + '～' + hi)];
          }));
      }
    } else {
      h += '<p style="color:var(--text-muted)">填入乳酸閾值心率（見第 31 課的 30 分鐘測試），可再得到以閾值為基準的區間。</p>';
    }
    h += '<p style="color:var(--text-muted)">三種方法的同名區間不會完全一樣；選一種固定使用，並用談話測試確認（能完整說句子＝大約在 Z2 以內）。</p>';
    out.innerHTML = h;
  }
  $('hz-calc').addEventListener('click', calc);
  $('hz-reset').addEventListener('click', function () {
    $('hz-age').value = 40; $('hz-rest').value = 60; $('hz-max').value = ''; $('hz-lt').value = ''; calc();
  });
  ['hz-age', 'hz-rest', 'hz-max', 'hz-lt'].forEach(function (id) {
    $(id).addEventListener('keydown', function (e) { if (e.key === 'Enter') calc(); });
  });
  calc();
})();
</script>""".replace(u"INPUT", _INPUT).replace(u"BTN", _BTN).replace(u"DATA", json.dumps(_DATA, ensure_ascii=False))

CALCULATOR = {
    "file": "hr-zone-calculator.html",
    "title": u"心率區間計算器",
    "h1": u"心率區間計算器：三種算法一次比較",
    "icon": u"🧮",
    "description": u"輸入年齡與靜止心率（可選填實測最大心率、乳酸閾值心率），算出五區間並比較不同公式",
    "body": [
        ("p", u"輸入你的資料後按「計算」。靜止心率請用連續幾天早上醒來時的平均值（" + LS(4) + u"）；"
              u"沒有實測最大心率時，會用 Tanaka 公式估計（" + LS(5) + u"）。"),
        ("raw", _CALC_HTML),
        ("h", u"使用提醒"),
        ("ul", [u"公式估計的最大心率，個人誤差約 ±10 次；有實測值時請優先使用（" + LS(31) + u"）。",
                u"服用 β 阻斷劑等影響心率的藥物、懷孕或有心臟疾病時，這些區間不適用，請以自覺強度與醫師建議為準（"
                + LS(29) + u"、" + LS(37) + u"）。",
                u"區間是訓練的指引，不是精密的界線；天氣、睡眠、疲勞都會讓心率偏移（" + LS(26) + u"～" + LS(28) + u"）。"]),
        _SAFE,
    ],
}

REFERENCES = [CHEATSHEET, CALCULATOR]
