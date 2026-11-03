# -*- coding: utf-8 -*-
"""〈資訊安全與駭客攻防〉（sec_）共用：課程包裝與 SCLIB 互動元件（class="sc-w"）。

  pwd     密碼強度與破解時間
  hash    雜湊與加鹽（內建 SHA-256）
  sqli    SQL 注入模擬（純前端假資料庫）
  xss     XSS 與輸出跳脫（只顯示、不執行）
  phish   釣魚訊息辨識測驗
"""
from md_common import make_with
from cc_common import wdg, LS, M, D, KATEX
from qt_common import BASEJS

SC_NOTE = u"本課程只介紹攻擊的原理與防禦方法，所有示範都是在瀏覽器內的模擬，不會連線到任何系統。未經授權入侵他人系統是違法行為（刑法第 358～363 條妨害電腦使用罪）；想練習請使用合法的靶場與 CTF。"
F = D


def scw(t, q=u"", **cfg):
    cfg.update({"t": t, "q": q})
    return wdg("sc-w", cfg)


SCLIB = r"""
(function () {
  if (window.__scLib) return; window.__scLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#e07a2f', GN = '#2e9e5b', RD = '#e0505a', GY = '#9aa3ad';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function row(root) { var d = el('div', 'margin:4px 0'); root.appendChild(d); return d; }
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;'); }
  function inp(root, lab, val, w) { var l = el('label', 'display:block;font-size:0.9em;margin:6px 0 2px', lab); var i = document.createElement('input'); i.type = 'text'; i.value = val; i.spellcheck = false; i.autocomplete = 'off';
    i.style.cssText = 'width:' + (w || '100%') + ';box-sizing:border-box;padding:6px 8px;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:0.95em;border:1px solid var(--border);border-radius:6px;background:var(--surface);color:var(--text)'; l.appendChild(document.createElement('br')); l.appendChild(i); root.appendChild(l); return i; }
  function code(html) { return '<pre style="white-space:pre-wrap;word-break:break-all;margin:6px 0;padding:8px 10px;border-radius:6px;background:var(--surface);border:1px solid var(--border);font-size:0.88em;line-height:1.5">' + html + '</pre>'; }
  function exb(root, list, cb) { var b = row(root); b.appendChild(el('span', 'font-size:0.85em;color:var(--text-muted);margin-right:4px', '試試看：')); list.forEach(function (q, i) { var x = btn(q[0], i); x.onclick = function () { cb(q); }; b.appendChild(x); }); return b; }

  /* ---------- SHA-256（純 JS，UTF-8） ---------- */
  function sha256(str) { var ascii = unescape(encodeURIComponent(str)); function rr(v, a) { return (v >>> a) | (v << (32 - a)); }
    var mp = Math.pow, mw = mp(2, 32), res = '', words = [], bl = ascii.length * 8, hash = [], k = [], pc = 0, comp = {}, i, j;
    for (var c = 2; pc < 64; c++) { if (!comp[c]) { for (i = 0; i < 313; i += c) comp[i] = c; hash[pc] = (mp(c, .5) * mw) | 0; k[pc++] = (mp(c, 1 / 3) * mw) | 0; } }
    hash = hash.slice(0, 8); ascii += '\x80'; while (ascii.length % 64 - 56) ascii += '\x00';
    for (i = 0; i < ascii.length; i++) { j = ascii.charCodeAt(i); words[i >> 2] |= j << ((3 - i) % 4) * 8; }
    words[words.length] = ((bl / mw) | 0); words[words.length] = bl;
    for (j = 0; j < words.length;) { var w = words.slice(j, j += 16), old = hash; hash = hash.slice(0, 8);
      for (i = 0; i < 64; i++) { var w15 = w[i - 15], w2 = w[i - 2], a = hash[0], e = hash[4];
        var t1 = hash[7] + (rr(e, 6) ^ rr(e, 11) ^ rr(e, 25)) + ((e & hash[5]) ^ ((~e) & hash[6])) + k[i] + (w[i] = (i < 16) ? w[i] : (w[i - 16] + (rr(w15, 7) ^ rr(w15, 18) ^ (w15 >>> 3)) + w[i - 7] + (rr(w2, 17) ^ rr(w2, 19) ^ (w2 >>> 10))) | 0);
        var t2 = (rr(a, 2) ^ rr(a, 13) ^ rr(a, 22)) + ((a & hash[1]) ^ (a & hash[2]) ^ (hash[1] & hash[2]));
        hash = [(t1 + t2) | 0].concat(hash); hash[4] = (hash[4] + t1) | 0; }
      for (i = 0; i < 8; i++) hash[i] = (hash[i] + old[i]) | 0; }
    for (i = 0; i < 8; i++) for (j = 3; j + 1; j--) { var b = (hash[i] >> (j * 8)) & 255; res += ((b < 16) ? 0 : '') + b.toString(16); }
    return res; }
  window.__scSha = sha256;

  /* ---------- 密碼強度 ---------- */
  var COMMON = ['123456', '123456789', '12345678', 'password', 'qwerty', '111111', '12345', '1234567', 'abc123', 'iloveyou', '000000', 'a123456', 'aa123456', '1qaz2wsx', 'qwerty123', '123123', 'zxcvbnm', 'password1', 'admin', 'welcome', 'letmein', 'monkey', 'dragon', 'football', 'sunshine', 'princess', 'qazwsx', 'asdfgh', '654321', '666666', '888888', '520520', '5201314', 'taiwan', 'admin123', 'p@ssw0rd', 'passw0rd'];
  function human(s) { if (s < 1) return '<b style="color:' + RD + '">瞬間</b>'; var u = [[60, '秒'], [3600, '分鐘'], [86400, '小時'], [86400 * 365, '天'], [86400 * 365 * 1e4, '年'], [86400 * 365 * 1e8, '萬年'], [Infinity, '億年']], d = [1, 60, 3600, 86400, 86400 * 365, 86400 * 365 * 1e4, 86400 * 365 * 1e8];
    if (s > 86400 * 365 * 1.38e10) return '<b style="color:' + GN + '">超過宇宙年齡（138 億年）</b>';
    for (var i = 0; i < u.length; i++) if (s < u[i][0]) { var v = s / d[i], col = s < 86400 ? RD : s < 86400 * 365 * 100 ? OR : GN; return '<b style="color:' + col + '">' + (v < 10 ? v.toFixed(1) : Math.round(v).toLocaleString()) + ' ' + u[i][1] + '</b>'; }
    return '<b style="color:' + GN + '">超過宇宙年齡</b>'; }
  function analyze(p) { var low = p.toLowerCase(), de = low.replace(/@/g, 'a').replace(/0/g, 'o').replace(/1/g, 'l').replace(/3/g, 'e').replace(/\$/g, 's').replace(/5/g, 's'), why = [];
    if (!p) return { bits: 0, why: ['請輸入一個「範例」密碼（不要輸入你真正在用的密碼）'] };
    if (COMMON.indexOf(low) >= 0 || COMMON.indexOf(de) >= 0 || COMMON.indexOf(low.replace(/[0-9!]+$/, '')) >= 0 && low.replace(/[0-9!]+$/, '').length >= 5) { why.push('在<b>常見密碼清單</b>中（或只是加上幾個數字、把字母換成符號）——攻擊者第一批就會試'); return { bits: 10, why: why }; }
    var N = 0; if (/[a-z]/.test(p)) N += 26; if (/[A-Z]/.test(p)) N += 26; if (/[0-9]/.test(p)) N += 10; if (/[^a-zA-Z0-9]/.test(p)) N += 33;
    var bits = p.length * Math.log2(N), alt;
    if (/^(19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])$/.test(p) || /^(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(19|20)?\d{2}$/.test(p)) { alt = Math.log2(120 * 366); why.push('看起來是<b>生日／日期</b>：一百多年的日期只有約四萬種'); bits = Math.min(bits, alt); }
    if (/^09\d{8}$/.test(p)) { why.push('看起來是<b>手機號碼</b>：容易被查到，可能性也只有一億種'); bits = Math.min(bits, Math.log2(1e8)); }
    if (/^[A-Z][12]\d{8}$/i.test(p)) { why.push('看起來是<b>身分證字號</b>：很多人知道，而且格式固定'); bits = Math.min(bits, 30); }
    var pat = why.length > 0;
    if (new Set(p.split('')).size <= 2 && p.length > 2) { why.push('幾乎<b>全是同一個字元</b>'); bits = Math.min(bits, 8); pat = true; }
    if (!pat && /(.)\1\1/.test(p)) { why.push('有<b>重複字元</b>'); bits -= 6; }
    if (!pat && /(abc|bcd|cde|123|234|345|456|567|678|789|qwe|wer|asd|sdf|zxc|xcv)/i.test(p)) { why.push('含有<b>順序或鍵盤排列</b>（abc、123、qwe…）'); bits -= 8; }
    var ws = p.split(/[\s\-_.]+/).filter(function (x) { return /^[a-zA-Z]{3,}$/.test(x); });
    if (ws.length >= 3 && ws.join('').length >= p.replace(/[\s\-_.]/g, '').length - 2) { alt = ws.length * Math.log2(7776); why.push('由 <b>' + ws.length + ' 個單字</b>組成的密碼片語：以「攻擊者知道你用單字表（7,776 字）」的最壞情況估算，每個字約 12.9 位元'); bits = Math.min(bits, alt); }
    if (p.length < 8) why.push('<b>太短</b>：少於 8 個字元'); else if (p.length >= 14) why.push('<b>長度足夠</b>：長度是強度最重要的因素');
    if (N <= 10) why.push('只有數字：每一位只有 10 種可能');
    return { bits: Math.max(bits, 1), why: why, N: N }; }
  function initPwd(root, cfg) { head(root, cfg.q); var i = inp(root, '輸入一個範例密碼（只在你的瀏覽器中計算，不會送出）', cfg.v || 'P@ssw0rd2024'), v = el('div'), inf; root.appendChild(v); inf = info(root);
    exb(root, [['19990815'], ['Tp!7x'], ['P@ssw0rd'], ['iloveyou520'], ['correct-horse-battery-staple'], ['k9#Vq2!mZr7$Lw']], function (q) { i.value = q[0]; up(); });
    root.insertBefore(root.lastChild, v);
    function up() { var a = analyze(i.value), g = Math.pow(2, a.bits) / 2, rows = [['線上猜測（網站有限速，每秒 10 次）', 10], ['離線破解：bcrypt 等慢雜湊（每秒約 1 萬次）', 1e4], ['離線破解：MD5 等快雜湊，一張高階顯卡（每秒約 1,000 億次）', 1e11]];
      v.innerHTML = '<table style="border-collapse:collapse;width:100%;margin-top:8px;font-size:0.9em">' + rows.map(function (r) { return '<tr><td style="padding:4px 6px;border-bottom:1px solid var(--border)">' + r[0] + '</td><td style="padding:4px 6px;border-bottom:1px solid var(--border);text-align:right">' + human(g / r[1]) + '</td></tr>'; }).join('') + '</table>';
      inf.innerHTML = '估計強度約 <b>' + Math.round(a.bits) + ' 位元</b>（約 2<sup>' + Math.round(a.bits) + '</sup> 種可能，平均猜一半就中）。' + (a.why.length ? '<br>• ' + a.why.join('<br>• ') : '') +
        '<br><span style="color:var(--text-muted);font-size:0.9em">粗略估算：真實的破解工具會用字典、規則與外洩密碼庫，常見模式會比這裡更快被破。最好的做法是用密碼管理器產生隨機密碼，並開啟多因素驗證。</span>'; }
    i.oninput = up; up(); }

  /* ---------- 雜湊與加鹽 ---------- */
  function initHash(root, cfg) { head(root, cfg.q); var P = { salt: 0 }, b = row(root), A = inp(root, '使用者 A 的密碼', 'sunshine'), B = inp(root, '使用者 B 的密碼', 'sunshine'), v = el('div'), inf;
    [['不加鹽', 0], ['加鹽', 1]].forEach(function (q) { var x = btn(q[0], q[1]); x.onclick = function () { P.salt = q[1]; mark(b, P.salt); up(); }; b.appendChild(x); }); mark(b, 0);
    var sa = 'f3a9c2', sb = '7be014'; root.appendChild(v); inf = info(root);
    function rnd() { var s = ''; for (var i = 0; i < 6; i++) s += '0123456789abcdef'[Math.floor(Math.random() * 16)]; return s; }
    var rb = btn('重新產生鹽'); rb.onclick = function () { sa = rnd(); sb = rnd(); up(); }; b.appendChild(rb);
    function hl(h, o) { var r = ''; for (var i = 0; i < h.length; i++) r += o && h[i] !== o[i] ? '<span style="color:' + OR + ';font-weight:bold">' + h[i] + '</span>' : h[i]; return r; }
    function up() { var a = A.value, bb = B.value, ha = sha256(P.salt ? sa + a : a), hb = sha256(P.salt ? sb + bb : bb), same = ha === hb;
      v.innerHTML = code('<b>使用者 A</b>' + (P.salt ? '　鹽 = ' + sa : '') + '\nSHA-256(' + esc(P.salt ? sa + a : a) + ')\n= ' + ha + '\n\n<b>使用者 B</b>' + (P.salt ? '　鹽 = ' + sb : '') + '\nSHA-256(' + esc(P.salt ? sb + bb : bb) + ')\n= ' + hl(hb, ha));
      inf.innerHTML = (same ? '<b style="color:' + RD + '">兩個雜湊值完全相同</b>：資料庫外洩後，攻擊者一眼就知道 A 和 B 用了同一個密碼；也能用事先算好的「彩虹表」直接查出常見密碼。' :
        a === bb && P.salt ? '<b style="color:' + GN + '">密碼一樣，雜湊值卻完全不同</b>：每個人有自己的隨機鹽，攻擊者必須對每個帳號分別暴力破解，彩虹表也失效了。鹽不需要保密，和雜湊值存在一起即可。' :
        '密碼只要差一個字元，雜湊值就幾乎完全不同（橘色是不同的位置）——這叫<b>雪崩效應</b>。') +
        '<br>雜湊是<b>單向</b>的：從雜湊值無法算回密碼，只能一個一個猜。但 SHA-256 太快了（顯卡每秒可算數十億次），儲存密碼應使用 <b>bcrypt、scrypt、Argon2</b> 這類刻意設計得很慢的演算法。'; }
    A.oninput = up; B.oninput = up; up(); }

  /* ---------- SQL 注入模擬 ---------- */
  var USERS = [{ id: 1, username: 'admin', password: 'S3cure!Adm1n', role: '管理員' }, { id: 2, username: 'alice', password: 'wonderland', role: '一般會員' }, { id: 3, username: 'bob', password: 'builder42', role: '一般會員' }];
  function tok(s) { var t = [], i = 0, m; while (i < s.length) { var c = s[i];
      if (/\s/.test(c)) { i++; continue; }
      if (s.substr(i, 2) === '--' || c === '#') { t.push({ k: 'cmt', v: s.slice(i) }); break; }
      if (c === ';') { t.push({ k: 'semi', v: s.slice(i) }); break; }
      if (c === "'") { var j = i + 1, v = ''; while (true) { if (j >= s.length) throw '字串沒有結束（引號不成對）'; if (s[j] === "'") { if (s[j + 1] === "'") { v += "'"; j += 2; continue; } break; } v += s[j++]; } t.push({ k: 'str', v: v }); i = j + 1; continue; }
      if ((m = /^\d+/.exec(s.slice(i)))) { t.push({ k: 'num', v: m[0] }); i += m[0].length; continue; }
      if ((m = /^[A-Za-z_]\w*/.exec(s.slice(i)))) { var u = m[0].toUpperCase(); t.push(u === 'AND' || u === 'OR' || u === 'NOT' ? { k: u } : { k: 'id', v: m[0] }); i += m[0].length; continue; }
      if ((m = /^(<>|!=|>=|<=|=|<|>)/.exec(s.slice(i)))) { t.push({ k: 'op', v: m[0] }); i += m[0].length; continue; }
      if (c === '(' || c === ')') { t.push({ k: c }); i++; continue; }
      throw '無法辨識的字元：' + c; }
    return t; }
  function evalWhere(src, row) { var t = tok(src), p = 0, extra = null; t = t.filter(function (x) { if (x.k === 'cmt' || x.k === 'semi') { extra = x; return false; } return true; });
    function pk() { return t[p]; } function nx() { return t[p++]; }
    function val() { var x = nx(); if (!x) throw '語法錯誤：缺少值'; if (x.k === 'str' || x.k === 'num') return x.v; if (x.k === 'id') { var n = x.v.toLowerCase(); if (!(n in row)) throw '未知的欄位：' + x.v; return String(row[n]); } if (x.k === '(') { var r = expr(); if (!nx() || t[p - 1].k !== ')') throw '括號不成對'; return r ? '1' : '0'; } throw '語法錯誤：在「' + (x.v || x.k) + '」附近'; }
    function cmp() { var a = val(); if (pk() && pk().k === 'op') { var o = nx().v, b = val(), na = +a, nb = +b, num = !isNaN(na) && !isNaN(nb) && a !== '' && b !== ''; var x = num ? na : a, y = num ? nb : b;
        return o === '=' ? x == y : o === '<>' || o === '!=' ? x != y : o === '<' ? x < y : o === '>' ? x > y : o === '<=' ? x <= y : x >= y; } return a !== '' && a !== '0'; }
    function fac() { if (pk() && pk().k === 'NOT') { nx(); return !fac(); } return cmp(); }
    function term() { var r = fac(); while (pk() && pk().k === 'AND') { nx(); r = fac() && r; } return r; }
    function expr() { var r = term(); while (pk() && pk().k === 'OR') { nx(); r = term() || r; } return r; }
    var r = expr(); if (p < t.length) throw '語法錯誤：在「' + (t[p].v || t[p].k) + '」附近'; return { ok: r, extra: extra }; }
  function initSqli(root, cfg) { head(root, cfg.q); var P = { safe: 0 }, b = row(root), U = inp(root, '帳號', 'alice'), W = inp(root, '密碼', 'wonderland'), v = el('div'), inf;
    [['字串拼接（有漏洞）', 0], ['參數化查詢（安全）', 1]].forEach(function (q) { var x = btn(q[0], q[1]); x.onclick = function () { P.safe = q[1]; mark(b, P.safe); up(); }; b.appendChild(x); }); mark(b, 0);
    exb(root, [['正常登入', 'alice', 'wonderland'], ['密碼錯誤', 'alice', '1234'], ["' OR '1'='1", 'x', "' OR '1'='1"], ["admin'--", "admin'--", '隨便打'], ['引號不成對', "O'Brien", 'x']], function (q) { U.value = q[1]; W.value = q[2]; up(); });
    root.appendChild(v); inf = info(root);
    function up() { var u = U.value, w = W.value, q, rows = [], err = null, ex = null;
      if (P.safe) { q = "SELECT * FROM users WHERE username = <b>?</b> AND password = <b>?</b>\n參數 1 = " + esc(JSON.stringify(u)) + '\n參數 2 = ' + esc(JSON.stringify(w)); rows = USERS.filter(function (r) { return r.username === u && r.password === w; }); }
      else { var where = "username = '" + u + "' AND password = '" + w + "'";
        q = 'SELECT * FROM users WHERE ' + esc("username = '") + '<span style="color:' + OR + ';font-weight:bold">' + esc(u) + '</span>' + esc("' AND password = '") + '<span style="color:' + OR + ';font-weight:bold">' + esc(w) + '</span>' + esc("'");
        try { USERS.forEach(function (r) { var e = evalWhere(where, r); ex = e.extra; if (e.ok) rows.push(r); }); } catch (e) { err = e; } }
      v.innerHTML = code(q) + (err ? '<div style="color:' + RD + '">資料庫錯誤：' + esc(err) + '</div>' : '<div>查到 <b>' + rows.length + '</b> 筆：' + (rows.length ? rows.map(function (r) { return r.username + '（' + r.role + '）'; }).join('、') : '無') + '</div>');
      var bypass = rows.length && !(rows.length === 1 && rows[0].username === u && rows[0].password === w);
      inf.innerHTML = err ? '使用者的輸入<b>破壞了 SQL 的語法</b>。光是錯誤訊息，就告訴攻擊者「這裡有注入點」；正式網站不應該把資料庫錯誤顯示給使用者。' :
        bypass ? '<b style="color:' + RD + '">登入被繞過了！</b>系統會以第一筆「' + rows[0].username + '（' + rows[0].role + '）」的身分登入。使用者輸入的引號提早結束了字串，後面的文字被當成 <b>SQL 指令</b>執行' + (ex && ex.k === 'cmt' ? '；<code>--</code> 讓後面的密碼檢查變成註解' : '') + '。' :
        rows.length ? '帳號密碼正確，正常登入。' : '帳號或密碼錯誤，登入失敗。';
      inf.innerHTML += P.safe ? '<br><b>參數化查詢</b>：SQL 指令的結構先送給資料庫，使用者的輸入只會被當成「資料」，不管裡面有幾個引號都不會變成指令——這是防禦 SQL 注入的根本方法。' : '<br>（模擬的資料庫，只支援 WHERE 子句的比較、AND、OR、NOT、括號與註解。另外，真正的系統不應該存明文密碼。）'; }
    U.oninput = up; W.oninput = up; up(); }

  /* ---------- XSS（只顯示，不執行） ---------- */
  function initXss(root, cfg) { head(root, cfg.q); var P = { ctx: 0 }, b = row(root), I = inp(root, '使用者輸入的留言', 'Hello <b>world</b>!'), v = el('div'), inf;
    [['放進網頁內文', 0], ['放進屬性值', 1], ['放進連結網址', 2]].forEach(function (q) { var x = btn(q[0], q[1]); x.onclick = function () { P.ctx = q[1]; mark(b, P.ctx); up(); }; b.appendChild(x); }); mark(b, 0);
    exb(root, [['普通留言', 'Hello <b>world</b>!'], ['script 標籤', '<script>alert(document.cookie)<\/script>'], ['圖片 onerror', '<img src=x onerror=alert(1)>'], ['跳出屬性', '" onmouseover="alert(1)'], ['javascript: 網址', 'javascript:alert(1)']], function (q) { I.value = q[1]; up(); });
    root.appendChild(v); inf = info(root);
    var HR = 'hr' + 'ef';
    function tpl(x) { return P.ctx === 0 ? '<div class="comment">' + x + '</div>' : P.ctx === 1 ? '<input value="' + x + '">' : '<a ' + HR + '="' + x + '">我的網站</a>'; }
    function up() { var s = I.value, raw = tpl(s), safe = P.ctx === 2 && /^\s*(javascript|data|vbscript):/i.test(s) ? tpl('#blocked') : tpl(esc(s)), bad = [];
      if (P.ctx === 0) { if (/<script/i.test(s)) bad.push('&lt;script&gt; 標籤會被執行'); if (/<\w+[^>]*\son\w+\s*=/i.test(s)) bad.push('事件屬性（onerror、onload…）會執行 JavaScript'); if (/<(iframe|object|embed|svg)/i.test(s)) bad.push('可以嵌入外部內容或 SVG 指令碼'); }
      if (P.ctx === 1 && /"/.test(s)) { bad.push('雙引號提早結束了屬性值'); if (/on\w+\s*=/i.test(s)) bad.push('後面的文字變成新的事件屬性'); }
      if (P.ctx === 2 && /^\s*(javascript|data|vbscript):/i.test(s)) bad.push('javascript: 網址被點擊時會執行程式碼');
      var tags = P.ctx === 0 && /<\w/.test(s) && !bad.length;
      v.innerHTML = '<div style="font-size:0.9em;margin-top:6px"><b>直接把輸入接進 HTML</b></div>' + code(esc(raw)) + '<div style="font-size:0.9em"><b>先跳脫再輸出</b></div>' + code(esc(safe));
      inf.innerHTML = (bad.length ? '<b style="color:' + RD + '">危險！</b>如果直接輸出，瀏覽器會把這段輸入當成程式碼：' + bad.join('；') + '。攻擊者可以偷走其他使用者的 Cookie、冒用他們的身分操作。' :
        tags ? '輸入裡有 HTML 標籤，直接輸出會改變網頁的版面（這次還不會執行程式，但已經代表輸出沒有被處理）。' : (esc(s) !== s ? '這段輸入含有特殊字元，但在<b>這個位置</b>還不會被當成程式碼——換一個位置（試試上面三個按鈕）就可能出事，所以一律跳脫最安全。' : '這段輸入沒有特殊字元，兩種方式的結果一樣。')) +
        '<br><b>跳脫</b>把 &lt; &gt; &quot; &amp; 等字元換成 HTML 實體，瀏覽器只會把它們「顯示」出來' + (P.ctx === 2 ? '；網址還必須<b>檢查開頭是 http: 或 https:</b>，因為 javascript: 本身沒有特殊字元可以跳脫' : '') + '。現代框架（React、Vue）預設都會自動跳脫，再加上 CSP 作為第二道防線。<br><span style="color:var(--text-muted);font-size:0.9em">本工具只顯示 HTML 原始碼，不會真的執行你輸入的內容。</span>'; }
    I.oninput = up; up(); }

  /* ---------- 釣魚辨識測驗 ---------- */
  var PH = [
    { k: '簡訊', f: '+886 9xx-xxx-xxx', b: '【通行費】您的車輛有一筆逾期通行費 NT$128 未繳，今日未繳將加收罰鍰 NT$3,000，請立即點擊繳費：https://etc-tw-pay.top/q8', p: 1, c: ['製造急迫感與罰款恐嚇', '網址不是官方網域（.top 結尾的陌生網址）', '一般個人門號發送'] },
    { k: 'Email', f: 'it-support@yourcompany-security.com', b: '您好，您的公司信箱即將達到容量上限，請在 24 小時內登入以下頁面驗證帳號，否則信箱將被停用。', p: 1, c: ['寄件網域和公司網域不同（多了 -security）', '要求「登入驗證」、限時 24 小時', '真正的 IT 部門很少用這種方式要你輸入密碼'] },
    { k: '簡訊', f: '（你常用的電商 App 推播）', b: '您訂購的商品已出貨，預計明天送達。訂單詳情請開啟 App 查看。', p: 0, c: ['沒有附連結，請你自己開 App', '沒有要求提供個資或付款', '內容和你最近真的有下單相符'] },
    { k: 'LINE', f: '（朋友的帳號）', b: '在嗎？我手機壞了，可以幫我收一下驗證碼嗎？等等會傳到你的手機，收到後截圖給我。', p: 1, c: ['帳號可能已被盜用', '「驗證碼」是用來登入或綁定你的帳號——給出去就等於交出帳號', '先打電話給本人確認'] },
    { k: 'Email', f: 'service@bank-notify.com.tw.verify-login.net', b: '親愛的客戶：系統偵測到您的帳戶有異常登入，請點擊連結重新設定網路銀行密碼。', p: 1, c: ['真正的網域要看最後一段：verify-login.net，不是銀行', '「帳戶異常」是最常見的釣魚藉口', '銀行不會用 Email 連結要你重設密碼'] },
    { k: '電話', f: '自稱「165 反詐騙專線」的來電，顯示號碼開頭 +', b: '您的帳戶涉及洗錢案件，必須配合「監管帳戶」把存款轉出，並且不能告訴家人。', p: 1, c: ['公務機關不會要求轉帳或「監管帳戶」', '來電號碼開頭有 + 是國際來電', '要求保密、不能告訴家人是詐騙的典型特徵'] },
    { k: 'Email', f: '（公司 HR 的正式信箱）', b: '提醒：年度資安教育訓練將於下週三下午舉行，請至內部學習平台報名（平台網址請從公司內網首頁進入）。', p: 0, c: ['寄件者是已知的內部信箱', '沒有要求輸入帳密，並請你從已知的入口進入', '沒有急迫或恐嚇的語氣'] },
    { k: '簡訊', f: '（某快遞）', b: '您的包裹因地址不完整無法投遞，請於 12 小時內補填資料並支付 NT$25 重新配送費：https://bit.ly/3xYz', p: 1, c: ['短網址隱藏了真正的目的地', '小額付款是為了騙取信用卡資料', '你根本不記得有寄送中的包裹'] },
  ];
  function initPhish(root, cfg) { head(root, cfg.q); var i = 0, sc = 0, done = [], card = el('div'), bb = row(root), inf; root.insertBefore(card, bb); inf = info(root);
    var y = btn('這是釣魚／詐騙'), n = btn('看起來正常'), nx = btn('下一題 →'); bb.appendChild(y); bb.appendChild(n); bb.appendChild(nx);
    function show() { var q = PH[i]; card.innerHTML = '<div style="border:1px solid var(--border);border-radius:8px;padding:10px 12px;margin:6px 0;background:var(--surface)"><div style="font-size:0.85em;color:var(--text-muted)">第 ' + (i + 1) + ' / ' + PH.length + ' 題　' + q.k + '　來自：' + esc(q.f) + '</div><div style="margin-top:6px;line-height:1.7">' + esc(q.b) + '</div></div>';
      inf.innerHTML = done[i] === undefined ? '你的判斷是？' : res(); }
    function res() { var q = PH[i], ok = done[i] === q.p; return (ok ? '<b style="color:' + GN + '">答對了！</b>' : '<b style="color:' + RD + '">再想想。</b>') + '這則是<b>' + (q.p ? '釣魚／詐騙' : '正常訊息') + '</b>。線索：<br>• ' + q.c.join('<br>• ') + '<br>目前得分 ' + sc + ' / ' + done.filter(function (x) { return x !== undefined; }).length; }
    function ans(a) { if (done[i] !== undefined) return; done[i] = a; if (a === PH[i].p) sc++; inf.innerHTML = res(); }
    y.onclick = function () { ans(1); }; n.onclick = function () { ans(0); }; nx.onclick = function () { i = (i + 1) % PH.length; show(); };
    show(); }

  var INIT = { pwd: initPwd, hash: initHash, sqli: initSqli, xss: initXss, phish: initPhish };
  function boot() { document.querySelectorAll('.sc-w').forEach(function (root) { if (root.__done) return; root.__done = 1;
    var cfg = JSON.parse(root.getAttribute('data-cfg')); var fn = INIT[cfg.t]; if (fn) fn(root, cfg); }); }
  if (document.readyState === 'complete') boot(); else window.addEventListener('load', boot);
})();
"""


def make(icon=u"🛡️", note=SC_NOTE):
    return make_with(icon, note, [("sc-w", SCLIB)])


lesson = make()
