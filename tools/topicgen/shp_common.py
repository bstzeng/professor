# -*- coding: utf-8 -*-
"""〈蝦皮的商業模式〉（shp_）共用：沿用 NVLIB（時間軸、卡片、關係圖），另加 SHPLIB——
賣家費用試算（fee）、財報長條圖（bars）、平台飛輪（wheel）。"""
from nv_common import *
from nv_common import NVLIB

SHP_NOTE = (u"財務數字取自 Sea Limited 公布的財報與新聞報導（2026 年 10 月查證），並註明年份與口徑；"
           u"蝦皮的費率、活動與規則經常調整，課程中的費率是 2026 年第三方整理的常見數字，<strong>實際以蝦皮賣家中心公告為準</strong>。"
           u"本課程是商業模式的學習整理，不是投資建議。")

SHPLIB = r"""
(function () {
  if (window.__shpLib) return; window.__shpLib = 1;
""" + BASEJS + r"""
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7'); root.appendChild(p); return p; }
  function money(v) { var s = Math.round(v).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ','); return s; }

  /* ---------- 賣家費用試算 ---------- */
  function fees(o) { var gross = o.price + o.ship, tx = o.price * o.c, pay = gross * o.g, plan = o.plan === 2 ? 60 : o.price * o.f, act = o.price * o.a;
    var total = tx + pay + plan + act, net = o.price - total - o.cost - o.shipCost + o.ship;
    return { tx: tx, pay: pay, plan: plan, act: act, total: total, net: net, rate: o.price > 0 ? total / o.price : 0 }; }
  window.__shpFees = fees;
  function initFee(root, cfg) {
    head(root, cfg.q);
    var o = { price: cfg.price || 500, cost: cfg.cost || 250, ship: 0, shipCost: 0, c: 0.055, g: 0.025, f: 0.06, a: 0, plan: 1 };
    var pb = el('div'); root.appendChild(pb);
    [[1, '免運專案 方案一（成交金額 6%）'], [2, '方案二（每單固定 60 元）']].forEach(function (x) { var b = btn(x[1], x[0]); b.addEventListener('click', function () { o.plan = x[0]; mark(pb, o.plan); draw(); }); pb.appendChild(b); }); mark(pb, 1);
    var us = [slider(root, '商品售價（買家看到的價格）', 50, 5000, 10, o.price, function (v) { return money(v) + ' 元'; }, 'p', function (v) { o.price = v; draw(); }),
      slider(root, '你的進貨成本＋包材', 0, 4000, 10, o.cost, function (v) { return money(v) + ' 元'; }, 'k', function (v) { o.cost = v; draw(); }),
      slider(root, '成交手續費率（依品類與賣家身分不同）', 0, 0.12, 0.005, o.c, function (v) { return f1(v * 100) + '%'; }, 'c', function (v) { o.c = v; draw(); }),
      slider(root, '金流與系統處理費率', 0, 0.05, 0.005, o.g, function (v) { return f1(v * 100) + '%'; }, 'g', function (v) { o.g = v; draw(); }),
      slider(root, '其他活動費用（蝦幣回饋、促銷活動等）', 0, 0.1, 0.005, o.a, function (v) { return f1(v * 100) + '%'; }, 'a', function (v) { o.a = v; draw(); })];
    var out = el('div'), ch = el('div'); root.appendChild(out); root.appendChild(ch);
    us.forEach(function (u) { u(); });
    var p = info(root); p.innerHTML = '簡化假設：買家免運（運費由平台活動處理）、不含廣告費、退貨與營業稅。費率是 2026 年常見的整理數字，可自行調整；實際以蝦皮賣家中心公告為準。';
    function draw() { var r = fees(o), seg = [['成本', o.cost, '#8a8f98'], ['成交手續費', r.tx, '#d0564f'], ['金流與系統處理費', r.pay, '#d9822b'], ['免運專案', r.plan, '#8a5cb8'], ['活動費用', r.act, '#b8941f'], ['你的利潤', Math.max(0, r.net), '#4a9a5e']];
      var tot = seg.reduce(function (s, x) { return s + x[1]; }, 0) || 1, bar = '<div style="display:flex;height:26px;border-radius:6px;overflow:hidden;margin-top:10px">';
      seg.forEach(function (x) { if (x[1] > 0) bar += '<div title="' + x[0] + '" style="width:' + (x[1] / tot * 100) + '%;background:' + x[2] + '"></div>'; }); bar += '</div><div style="display:flex;flex-wrap:wrap;gap:4px 12px;font-size:0.82em;margin-top:4px">';
      seg.forEach(function (x) { bar += '<span><span style="display:inline-block;width:10px;height:10px;border-radius:2px;background:' + x[2] + '"></span> ' + x[0] + ' ' + money(x[1]) + '</span>'; });
      out.innerHTML = bar + '</div><div style="margin-top:8px;line-height:1.7">蝦皮各項費用合計 <b>' + money(r.total) + ' 元</b>（售價的 <b>' + f1(r.rate * 100) + '%</b>）；每賣一件，你賺 <b style="color:' + (r.net >= 0 ? '#4a9a5e' : '#d0564f') + '">' + money(r.net) + ' 元</b>' + (r.net < 0 ? '（虧本！）' : '') + '。</div>';
      var d1 = [], d2 = []; for (var x = 100; x <= 3000; x += 50) { d1.push([x, fees({ price: x, cost: 0, ship: 0, shipCost: 0, c: 0, g: 0, f: o.f, a: 0, plan: 1 }).plan]); d2.push([x, 60]); }
      ch.innerHTML = chart(640, 200, [{ d: d1, c: '#8a5cb8', n: '方案一 6%' }, { d: d2, c: '#2a9d9d', n: '方案二 固定 60 元', dash: '5 4' }], { xl: '單筆訂單商品金額（元）', y0: 0, vl: [{ x: 1000, c: '#d0564f', n: '1,000 元分界' }] }) +
        '<div style="font-size:0.85em;color:var(--text-muted)">免運專案的兩種收費：60 ÷ 6% ＝ 1,000，訂單金額高於 1,000 元時固定 60 元比較划算，低於時 6% 比較划算。</div>'; }
    draw();
  }

  /* ---------- 財報長條圖（可正可負） ---------- */
  function initBars(root, cfg) {
    head(root, cfg.q); var k = 0, bb = el('div'), view = el('div'), p; root.appendChild(bb); root.appendChild(view); p = info(root);
    cfg.series.forEach(function (s, i) { var b = btn(s.n, i); b.addEventListener('click', function () { k = i; mark(bb, k); draw(); }); bb.appendChild(b); }); mark(bb, 0);
    function draw() { var s = cfg.series[k], W = 640, H = 250, L = 50, R = 10, T = 20, B = 30, vals = s.d.map(function (x) { return x[1]; }), mx = Math.max(0, Math.max.apply(null, vals)), mn = Math.min(0, Math.min.apply(null, vals));
      if (mx === mn) mx = mn + 1; var sy = function (v) { return T + (mx - v) / (mx - mn) * (H - T - B); }, n = s.d.length, bw = (W - L - R) / n, g = '';
      nice(mn, mx, 4).forEach(function (v) { g += ln(L, sy(v), W - R, sy(v), 'var(--border)', 0.6, 'stroke-dasharray="2 3"') + tx(L - 5, sy(v) + 3, fmtT(v), 9, 'var(--text-muted)', 'end'); });
      g += ln(L, sy(0), W - R, sy(0), '#999', 1);
      s.d.forEach(function (x, i) { var v = x[1], y0 = sy(Math.max(0, v)), h = Math.abs(sy(v) - sy(0)), cx = L + i * bw + bw / 2, c = v >= 0 ? (s.c || '#3a6ea5') : '#d0564f';
        g += '<g data-i="' + i + '" style="cursor:pointer"><rect x="' + n1(cx - bw * 0.32) + '" y="' + n1(y0) + '" width="' + n1(bw * 0.64) + '" height="' + n1(Math.max(1, h)) + '" fill="' + c + '" rx="2"/>' +
          (v >= 0 || h < 16 ? tx(cx, v >= 0 ? y0 - 4 : y0 + h + 11, (Math.round(v * 100) / 100).toString(), 9.5, c) : tx(cx, y0 + h - 5, (Math.round(v * 100) / 100).toString(), 9.5, '#fff')) + tx(cx, H - 8, x[0], 9.5, 'var(--text-muted)') + '</g>'; });
      g += tx(L - 44, T - 8, s.u || '', 9.5, 'var(--text-muted)', 'start');
      view.innerHTML = svgw('0 0 ' + W + ' ' + H, g); p.innerHTML = s.note || '點長條看說明。';
      view.querySelectorAll('g[data-i]').forEach(function (e) { e.addEventListener('click', function () { var x = s.d[+e.getAttribute('data-i')]; p.innerHTML = '<b>' + x[0] + '</b>：' + x[1] + ' ' + (s.u || '') + (x[2] ? '<br>' + x[2] : ''); }); }); }
    draw();
  }

  /* ---------- 平台飛輪 ---------- */
  function initWheel(root, cfg) {
    head(root, cfg.q); var view = el('div'), p; root.appendChild(view); p = info(root);
    var n = cfg.nodes.length, cx = 320, cy = 160, R = 120, g = '<defs><marker id="shpa" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#999"/></marker></defs>';
    var pos = cfg.nodes.map(function (x, i) { var a = -Math.PI / 2 + i * 2 * Math.PI / n; return [cx + R * 1.55 * Math.cos(a), cy + R * Math.sin(a)]; });
    pos.forEach(function (a, i) { var b = pos[(i + 1) % n], dx = b[0] - a[0], dy = b[1] - a[1], d = Math.sqrt(dx * dx + dy * dy), ux = dx / d, uy = dy / d;
      g += '<line x1="' + n1(a[0] + ux * 58) + '" y1="' + n1(a[1] + uy * 26) + '" x2="' + n1(b[0] - ux * 58) + '" y2="' + n1(b[1] - uy * 26) + '" stroke="#999" stroke-width="2" marker-end="url(#shpa)"/>'; });
    cfg.nodes.forEach(function (x, i) { var a = pos[i]; g += '<g data-i="' + i + '" style="cursor:pointer"><rect x="' + n1(a[0] - 62) + '" y="' + n1(a[1] - 18) + '" width="124" height="36" rx="18" fill="var(--surface)" stroke="' + (x[2] || '#3a6ea5') + '" stroke-width="2"/>' + tx(a[0], a[1] + 4, x[0], 11.5, 'currentColor') + '</g>'; });
    g += tx(cx, cy + 5, cfg.center || '', 13, 'var(--text-muted)');
    view.innerHTML = svgw('0 0 640 320', g); p.innerHTML = cfg.hint || '點任一個環節看說明。';
    view.querySelectorAll('g[data-i]').forEach(function (e) { e.addEventListener('click', function () { var x = cfg.nodes[+e.getAttribute('data-i')]; p.innerHTML = '<b>' + x[0] + '</b>：' + x[1]; }); });
  }

  function initAll() { document.querySelectorAll('.shp-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ fee: initFee, bars: initBars, wheel: initWheel })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""


def shpw(cfg, maxw=720):
    return wdg("shp-w", cfg, maxw)


_base = make_lesson(u"🦐", SHP_NOTE, NVLIB, "nv-w")


def lesson(*a, **k):
    L = _base(*a, **k)
    if any(isinstance(b, tuple) and b[0] == "raw" and 'class="shp-w' in b[1] for b in L.body):
        L.body.insert(0, ("raw", u"<script>%s</script>" % SHPLIB))
    L.body = [b for b in L.body if not (isinstance(b, tuple) and b[0] == "raw" and b[1] == KATEX)]
    return L
