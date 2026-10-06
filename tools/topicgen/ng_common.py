# -*- coding: utf-8 -*-
"""〈親手訓練一個小 LLM〉（ng_）共用工具：Python 範例嵌入（ex、src）與互動元件（NGLIB）。"""
import io
import json
import os
import re
from cc_common import *
from qt_common import BASEJS
import builder as B

HERE = os.path.dirname(os.path.abspath(__file__))
PYDIR = os.path.join(HERE, "ng_py")

NG_NOTE = (u"本課程的 Python 範例都在一台 4 核心 CPU、沒有 GPU 的電腦上實際執行過，頁面上的「執行結果」就是當時的輸出；"
           u"你的數字會因硬體、PyTorch 版本與隨機性而略有不同。語料來自開源的 chinese-poetry 專案（MIT 授權）。")

PUBLISH = ["prepare_data", "tokenizer", "gpt", "train", "sample", "chat", "lora", "hf_qwen_lora", "s01_tensor", "s02_module", "s03_data",
           "s04_char_tok", "s05_bpe", "s06_bigram", "s07_attention", "s08_params", "s09_experiments", "s10_sampling", "s11_kvcache",
           "s12_modern", "s13_instruct_data", "s14_eval"]


def _read(*p):
    return io.open(os.path.join(PYDIR, *p), encoding="utf-8").read()


def _out_block(text):
    return ("raw", u'<div class="code-block" style="background:#14301f;color:#d6f5df">%s</div>' % B.esc(text.rstrip("\n")).replace("\n", "&#10;"))


def ex(name, intro=None, cmd=None, show_src=True, out=None):
    """嵌入一支範例：程式碼＋實際輸出＋下載連結。"""
    blocks = [("raw", u'<p style="margin:18px 0 6px"><strong>🐍 %s.py</strong>　<a href="py/%s.py" download>下載</a>　'
                      u'<span style="color:var(--text-muted);font-size:0.9em">執行：<code>%s</code></span></p>' % (name, name, cmd or u"python %s.py" % name))]
    if intro:
        blocks.append(("p", intro))
    if show_src:
        blocks.append(("code", _read(name + ".py")))
    o = out or name
    if os.path.exists(os.path.join(PYDIR, "_out", o + ".txt")):
        blocks.append(("raw", u'<p style="margin:0 0 6px"><strong>▶ 執行結果</strong>（實際執行的輸出）</p>'))
        blocks.append(_out_block(_read("_out", o + ".txt")))
    return blocks


def output(name, head=None, tail=None, grep=None):
    """只顯示某支程式的輸出（可以只取前幾行或後幾行）。"""
    lines = _read("_out", name + ".txt").rstrip("\n").split("\n")
    if grep:
        lines = [l for l in lines if re.search(grep, l)]
    if head:
        lines = lines[:head]
    if tail:
        lines = lines[-tail:]
    return [("raw", u'<p style="margin:12px 0 6px"><strong>▶ 執行結果</strong></p>'), _out_block("\n".join(lines))]


def src(name, start, end=None):
    """從範例檔中取出一段程式碼：從含有 start 的那一行，到含有 end 的那一行（含）為止；end 省略則取到下一個空行。"""
    lines = _read(name + ".py").split("\n")
    i = next(k for k, l in enumerate(lines) if start in l)
    if end is None:
        j = next((k for k in range(i + 1, len(lines)) if not lines[k].strip()), len(lines)) - 1
    else:
        j = next(k for k in range(i, len(lines)) if end in lines[k])
    return ("code", u"\n".join(lines[i:j + 1]))


def train_curve(name):
    pts = []
    for l in _read("_out", name + ".txt").split("\n"):
        m = re.match(r"step\s+(\d+) \| lr ([\d.e+-]+) \| train loss ([\d.]+) \| val loss ([\d.]+)", l)
        if m:
            pts.append([int(m.group(1)), float(m.group(3)), float(m.group(4)), float(m.group(2))])
    return pts


def _data():
    p = os.path.join(PYDIR, "_out", "data.json")
    d = json.load(io.open(p, encoding="utf-8")) if os.path.exists(p) else {"logits": {}, "poems": []}
    d["curve"] = train_curve("train") if os.path.exists(os.path.join(PYDIR, "_out", "train.txt")) else []
    d["curve2"] = train_curve("train_modern") if os.path.exists(os.path.join(PYDIR, "_out", "train_modern.txt")) else []
    return d


NGLIB = r"""
(function () {
  if (window.__ngLib) return; window.__ngLib = 1;
""" + BASEJS + r"""
  var DATA = __DATA__;
  function info(root) { var p = el('p', 'margin:6px 0 0;line-height:1.65'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div'); root.appendChild(b); return b; }
  function chip(t, c) { return '<span style="display:inline-block;margin:2px;padding:1px 5px;border-radius:4px;background:' + c + ';color:#222;border:1px solid #ccc;font-size:0.92em;white-space:pre">' + t + '</span>'; }
  var PAL = ['#e8f0fa', '#fdf1e3', '#e9f5ec', '#f4ecf8', '#fff6c8', '#e3f4f7'];

  /* ---------- BPE 合併步驟 ---------- */
  function initBPE(root, cfg) {
    head(root, cfg.q); var ta = document.createElement('textarea'); ta.value = cfg.s || DATA.poems.slice(0, 12).join('\n');
    ta.style.cssText = 'width:100%;box-sizing:border-box;height:90px;padding:6px;border:1px solid var(--border);border-radius:8px;background:var(--surface);color:var(--text);font:inherit';
    root.appendChild(ta); var bb = bar(root), b1 = btn('合併一次', 's'), b2 = btn('合併 20 次', 'm'), b3 = btn('↺ 重來', 'r'); [b1, b2, b3].forEach(function (b) { bb.appendChild(b); });
    var view = el('div', 'margin-top:8px;line-height:1.9;max-height:260px;overflow:auto;border:1px solid var(--border);border-radius:8px;padding:6px'), log = el('div', 'margin-top:6px;font-size:0.9em'), p = info(root), seq, merges;
    root.appendChild(view); root.appendChild(log); root.appendChild(p);
    function reset() { seq = Array.from(ta.value); merges = []; draw(); }
    function step() { var cnt = {}, best = null, bc = 0; for (var i = 0; i < seq.length - 1; i++) { if (seq[i] === '\n' || seq[i + 1] === '\n') continue; var k = seq[i] + '\u0001' + seq[i + 1]; cnt[k] = (cnt[k] || 0) + 1; if (cnt[k] > bc) { bc = cnt[k]; best = k; } }
      if (!best || bc < 2) return false; var ab = best.split('\u0001'), out = []; for (var j = 0; j < seq.length; j++) { if (j < seq.length - 1 && seq[j] === ab[0] && seq[j + 1] === ab[1]) { out.push(ab[0] + ab[1]); j++; } else out.push(seq[j]); }
      seq = out; merges.push([ab[0], ab[1], bc]); return true; }
    function draw() { var o = '', ci = 0; seq.forEach(function (t) { if (t === '\n') { o += '<br>'; return; } o += chip(t, t.length > 1 ? PAL[(ci++ % 5) + 1] : '#f3f3f3'); });
      view.innerHTML = o; var chars = Array.from(ta.value).filter(function (c) { return c !== '\n'; }).length, toks = seq.filter(function (t) { return t !== '\n'; }).length;
      log.innerHTML = merges.length ? '最近的合併：' + merges.slice(-6).map(function (m, i) { return '<b>#' + (merges.length - Math.min(6, merges.length) + i + 1) + '</b> 「' + m[0] + '」＋「' + m[1] + '」→「' + m[0] + m[1] + '」（' + m[2] + ' 次）'; }).join('　') : '';
      p.innerHTML = '字數 <b>' + chars + '</b> → token 數 <b>' + toks + '</b>（已合併 ' + merges.length + ' 次，詞彙表多了 ' + merges.length + ' 個新 token）。每一步都找出<b>最常相鄰出現的一對</b>，把它們黏成一個新 token。' +
        '<br><span style="font-size:0.88em;color:var(--text-muted)">為了好讀，這裡從「字」開始合併；真正的 BPE（GPT、Llama）是從 UTF-8 的位元組開始，所以一個中文字可能先被拆成 3 個位元組。</span>'; }
    b1.addEventListener('click', function () { step(); draw(); }); b2.addEventListener('click', function () { for (var i = 0; i < 20; i++) if (!step()) break; draw(); });
    b3.addEventListener('click', reset); ta.addEventListener('change', reset); reset();
  }

  /* ---------- Bigram 機率表 ---------- */
  function initBigram(root, cfg) {
    head(root, cfg.q); var C = {}, text = DATA.poems.join('\n'); for (var i = 0; i < text.length - 1; i++) { var a = text[i], b = text[i + 1]; (C[a] = C[a] || {})[b] = (C[a][b] || 0) + 1; }
    var row = el('div'), inp = document.createElement('input'); inp.value = cfg.c || '月'; inp.maxLength = 1;
    inp.style.cssText = 'width:3em;padding:4px;text-align:center;font-size:1.2em;border:1px solid var(--border);border-radius:6px;background:var(--surface);color:var(--text)';
    row.appendChild(el('span', '', '前一個字：')); row.appendChild(inp); var g = btn('🎲 從這個字開始生成一句', 'g'); row.appendChild(g); root.appendChild(row);
    var view = el('div'), out = el('div', 'margin-top:6px;font-size:1.1em'), p = info(root); root.appendChild(view); root.appendChild(out); root.appendChild(p);
    function next(c) { var r = C[c]; if (!r) return null; var tot = 0, k; for (k in r) tot += r[k]; var x = Math.random() * tot; for (k in r) { x -= r[k]; if (x <= 0) return k; } return k; }
    g.addEventListener('click', function () { var c = inp.value || '月', s = c; for (var i = 0; i < 40; i++) { c = next(c); if (!c || c === '\n') break; s += c; } out.innerHTML = '生成：' + s; });
    function draw() { var c = inp.value, r = C[c] || {}, tot = 0, arr = []; for (var k in r) { tot += r[k]; arr.push([k, r[k]]); } arr.sort(function (a, b) { return b[1] - a[1]; }); arr = arr.slice(0, 12);
      if (!arr.length) { view.innerHTML = ''; p.innerHTML = '這 400 首詩裡沒有出現「' + c + '」，換一個字試試（例如 春、山、雲、不）。'; return; }
      var o = ''; arr.forEach(function (a, i) { var w = a[1] / arr[0][1] * 420; o += tx(60, 18 + i * 22, a[0] === '\n' ? '⏎' : a[0], 13, 'currentColor', 'end') + '<rect x="70" y="' + (5 + i * 22) + '" width="' + n1(w) + '" height="17" rx="3" fill="#3a6ea5"/>' + tx(76 + w, 18 + i * 22, (a[1] / tot * 100).toFixed(1) + '%（' + a[1] + ' 次）', 10, 'currentColor', 'start'); });
      view.innerHTML = svgw('0 0 640 ' + (arr.length * 22 + 10), o);
      p.innerHTML = '在 400 首唐詩裡，「' + c + '」後面一共出現 ' + tot + ' 次。Bigram 模型就是這張表：<b>下一個字的機率 ＝ 這個組合出現的次數 ÷ 前一個字出現的次數</b>。它只看前一個字，所以生成的句子每兩個字還算通順，整句卻不知所云。'; }
    inp.addEventListener('input', draw); draw();
  }

  /* ---------- 因果遮罩 ---------- */
  function initMask(root, cfg) {
    head(root, cfg.q); var w = Array.from(cfg.s || '床前明月光，疑是地上霜'), n = w.length, sel = n - 1, causal = true, bb = bar(root), view = el('div'), p;
    var b1 = btn('因果遮罩：開', 'c'); bb.appendChild(b1); b1.addEventListener('click', function () { causal = !causal; b1.textContent = '因果遮罩：' + (causal ? '開' : '關'); draw(); });
    root.appendChild(view); p = info(root);
    function draw() { var cs = Math.min(40, 520 / n), x0 = 60, y0 = 30, o = '';
      for (var j = 0; j < n; j++) o += tx(x0 + j * cs + cs / 2, y0 - 8, w[j], 12, 'currentColor');
      for (var i = 0; i < n; i++) { o += '<g data-r="' + i + '" style="cursor:pointer">' + tx(x0 - 8, y0 + i * cs + cs / 2 + 4, w[i], 12, i === sel ? '#d0564f' : 'currentColor', 'end');
        for (var j2 = 0; j2 < n; j2++) { var ok = !causal || j2 <= i; o += '<rect x="' + (x0 + j2 * cs) + '" y="' + (y0 + i * cs) + '" width="' + (cs - 2) + '" height="' + (cs - 2) + '" rx="3" fill="' + (ok ? (i === sel ? '#4a9a5e' : 'rgba(74,154,94,0.35)') : 'var(--border)') + '"/>'; } o += '</g>'; }
      view.innerHTML = svgw('0 0 640 ' + (y0 + n * cs + 6), o);
      view.querySelectorAll('g[data-r]').forEach(function (g) { g.addEventListener('click', function () { sel = +g.getAttribute('data-r'); draw(); }); });
      p.innerHTML = '點任一列：「' + w[sel] + '」' + (causal ? '只能看到 <b>' + (sel + 1) + '</b> 個字（自己和前面的字）。訓練時，第 ' + (sel + 1) + ' 個位置要預測的答案是「' + (sel < n - 1 ? w[sel + 1] : '下一個字') + '」，遮罩確保它不能偷看答案。' : '可以看到整句 ' + n + ' 個字——包括答案，模型會直接抄答案，學不到東西。') +
        '<br>一段 ' + n + ' 個字的文字，因為有遮罩，可以<b>同時</b>變成 ' + n + ' 道「猜下一個字」的練習題，這是 Transformer 訓練效率高的原因之一。'; }
    draw();
  }

  /* ---------- 參數與記憶體計算器 ---------- */
  function initParams(root, cfg) {
    head(root, cfg.q); var V = 6758, d = 192, L = 4, T = 80, view = el('div'), p;
    var u1 = slider(root, '詞彙量 V', 100, 160000, 100, V, function (v) { return v.toLocaleString(); }, 'V', function (v) { V = v; draw(); });
    var u2 = slider(root, '向量維度 d（n_embd）', 64, 8192, 64, d, function (v) { return v; }, 'd', function (v) { d = v; draw(); });
    var u3 = slider(root, '層數 L', 1, 80, 1, L, function (v) { return v; }, 'L', function (v) { L = v; draw(); });
    var u4 = slider(root, '上下文長度 T', 16, 8192, 16, T, function (v) { return v; }, 'T', function (v) { T = v; draw(); });
    root.appendChild(view); p = info(root);
    function fmt(x) { return x >= 1e9 ? f2(x / 1e9) + 'B' : x >= 1e6 ? f2(x / 1e6) + 'M' : Math.round(x).toLocaleString(); }
    function draw() { var emb = V * d, pos = T * d, att = L * (4 * d * d + 4 * d), mlp = L * (8 * d * d + 5 * d), ln = L * 4 * d + 2 * d, tot = emb + pos + att + mlp + ln;
      var parts = [[emb, '#3a6ea5', '字 embedding'], [pos, '#8a5cb8', '位置'], [att, '#d9822b', '注意力'], [mlp, '#4a9a5e', 'MLP'], [ln, '#999', 'LayerNorm']], x = 20, o = '';
      parts.forEach(function (q) { var w = q[0] / tot * 600; o += '<rect x="' + n1(x) + '" y="20" width="' + n1(Math.max(w, 0.5)) + '" height="30" fill="' + q[1] + '"/>'; if (w > 60) o += tx(x + w / 2, 40, q[2], 10, '#fff'); x += w; });
      view.innerHTML = svgw('0 0 640 60', o);
      p.innerHTML = '總參數 <b>' + fmt(tot) + '</b>：字 embedding ' + fmt(emb) + '（' + Math.round(emb / tot * 100) + '%）、注意力 ' + fmt(att) + '、MLP ' + fmt(mlp) + '。' +
        '<br>訓練時的記憶體（FP32 ＋ AdamW）：權重 4 bytes、梯度 4 bytes、Adam 的兩個狀態 8 bytes，每個參數約 <b>16 bytes</b> → 約 <b>' + f1(tot * 16 / 1e9) + ' GB</b>，還不含啟動值。' +
        (d === 192 && L === 4 && V === 6758 ? '<br>這是本課程的預設模型：小模型裡，embedding 佔了四成左右。試著把 d 拉到 4096、L 拉到 32、V 拉到 128000，看看 Llama 3 8B 的規模。' : ''); }
    u1(); u2(); u3(); u4();
  }

  /* ---------- 真實的 loss 曲線 ---------- */
  function initLoss(root, cfg) {
    head(root, cfg.q); var view = el('div'), p; root.appendChild(view); p = info(root);
    if (!DATA.curve.length) { p.innerHTML = '（尚無訓練紀錄）'; return; }
    var S = [{ d: DATA.curve.map(function (r) { return [r[0], r[1]]; }), c: '#3a6ea5', n: '訓練損失' }, { d: DATA.curve.map(function (r) { return [r[0], r[2]]; }), c: '#d0564f', n: '驗證損失' }];
    if (cfg.modern && DATA.curve2.length) S.push({ d: DATA.curve2.map(function (r) { return [r[0], r[2]]; }), c: '#4a9a5e', n: 'Llama 風格・驗證', dash: '5 3' });
    view.innerHTML = chart(640, 260, S, { y0: 3, xl: '訓練步數' }) + (cfg.lr ? chart(640, 140, [{ d: DATA.curve.map(function (r) { return [r[0], r[3] * 1000]; }), c: '#8a5cb8', n: '學習率（×10⁻³）' }], { y0: 0, xl: '訓練步數' }) : '');
    var last = DATA.curve[DATA.curve.length - 1];
    p.innerHTML = '這是本課程模型實際訓練時記錄的數字。最後一次評估：訓練損失 <b>' + last[1] + '</b>、驗證損失 <b>' + last[2] + '</b>（困惑度約 ' + Math.round(Math.exp(last[2])) + '，亂猜的困惑度是 6758）。' +
      (cfg.modern && DATA.curve2.length ? '<br>綠色虛線是 Llama 風格的模型：同樣的步數與參數量，最後驗證損失 ' + DATA.curve2[DATA.curve2.length - 1][2] + '。' : ''); }

  /* ---------- 抽樣：真實模型的 logits ---------- */
  function initSample(root, cfg) {
    head(root, cfg.q); var keys = Object.keys(DATA.logits); if (!keys.length) return; var pr = cfg.p || keys[0], T = 1, K = 30, P = 1, bb = bar(root), view = el('div'), out = el('div', 'margin-top:6px'), p;
    keys.forEach(function (k) { var x = btn('「' + k + '」的下一個字', k); x.addEventListener('click', function () { pr = k; mark(bb, k); draw(); }); bb.appendChild(x); }); mark(bb, pr);
    var u1 = slider(root, 'Temperature', 0.05, 2, 0.05, 1, f2, 'T', function (v) { T = v; draw(); });
    var u2 = slider(root, 'Top-k', 1, 30, 1, 30, function (v) { return v; }, 'k', function (v) { K = v; draw(); });
    var u3 = slider(root, 'Top-p', 0.05, 1, 0.05, 1, f2, 'p', function (v) { P = v; draw(); });
    var b = btn('🎲 抽 20 次', 's'); bar(root).appendChild(b); root.appendChild(view); root.appendChild(out); p = info(root);
    function probs() { var L = DATA.logits[pr], e = L.map(function (x) { return Math.exp((x[1] - L[0][1]) / T); }), s = 0; e.forEach(function (v) { s += v; }); var q = e.map(function (v) { return v / s; }), keep = [], c = 0;
      for (var i = 0; i < q.length; i++) { if (i >= K) break; keep.push(i); c += q[i]; if (c >= P) break; } var s2 = 0; keep.forEach(function (i) { s2 += q[i]; }); return q.map(function (v, i) { return keep.indexOf(i) >= 0 ? v / s2 : 0; }); }
    b.addEventListener('click', function () { var q = probs(), r = []; for (var n = 0; n < 20; n++) { var x = Math.random(), c = 0; for (var i = 0; i < q.length; i++) { c += q[i]; if (x <= c) { r.push(DATA.logits[pr][i][0]); break; } } } out.innerHTML = '抽樣結果：' + r.map(function (c) { return chip(c === '\n' ? '⏎' : c, '#e8f0fa'); }).join(''); });
    function draw() { out.innerHTML = ''; var q = probs(), L = DATA.logits[pr], o = '', n = 15; for (var i = 0; i < n; i++) { var w = q[i] * 900; o += tx(40, 16 + i * 20, L[i][0] === '\n' ? '⏎' : L[i][0], 13, q[i] ? 'currentColor' : 'var(--text-muted)', 'end') + tx(96, 16 + i * 20, 'logit ' + L[i][1].toFixed(1), 9, 'var(--text-muted)', 'end') +
        '<rect x="104" y="' + (4 + i * 20) + '" width="' + n1(Math.max(Math.min(w, 470), 0.5)) + '" height="15" rx="3" fill="' + (q[i] ? '#3a6ea5' : 'var(--border)') + '"/>' + tx(110 + Math.min(w, 470), 16 + i * 20, (q[i] * 100).toFixed(1) + '%', 9.5, 'currentColor', 'start'); }
      view.innerHTML = svgw('0 0 640 ' + (n * 20 + 6), o);
      var kept = q.filter(function (v) { return v > 0; }).length;
      p.innerHTML = '這是本課程訓練好的模型，看到「' + pr + '」之後，對下一個字給出的真實 logits（只列前 30 名）。目前有 <b>' + kept + '</b> 個候選字可以被抽到。' +
        '<br>Temperature 小 → 幾乎只選第一名，穩定但重複；大 → 冷門字也有機會，有創意但容易不通。Top-k、top-p 把機率太小的尾巴切掉。'; }
    u1(); u2(); u3();
  }

  function initAll() { document.querySelectorAll('.ng-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ bpe: initBPE, bigram: initBigram, mask: initMask, params: initParams, loss: initLoss, sample: initSample })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
""".replace("__DATA__", json.dumps(_data(), ensure_ascii=False))


def ngw(cfg, maxw=680):
    return wdg("ng-w", cfg, maxw)


nglesson = make_lesson(u"🛠️", NG_NOTE, NGLIB, "ng-w")
