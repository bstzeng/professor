# -*- coding: utf-8 -*-
"""〈嵌入式系統與微控制器〉（kem_）：全部課程（第 1～28 課）與互動元件。"""
from kx_base import *

JS = r"""
  /* 1. PWM */
  function initPwm(root, cfg) { head(root, cfg.q); var P = { d: 30, f: 1000 }, view = el('div');
    var g = el('div', 'display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:0 12px'); root.appendChild(g);
    var us = [slider(g, '工作週期（Duty cycle）', 0, 100, 1, P.d, function (x) { return x + '%'; }, 'd', function (x) { P.d = x; draw(); }), slider(g, 'PWM 頻率', 50, 20000, 50, P.f, function (x) { return x >= 1000 ? f1(x / 1000) + ' kHz' : x + ' Hz'; }, 'f', function (x) { P.f = x; draw(); })];
    root.appendChild(view); var inf = info(root);
    function draw() { var o = '', X0 = 40, W = 420, hi = 30, lo = 110, per = W / 4, d = P.d / 100, path = 'M' + X0 + ' ' + lo;
      for (var k = 0; k < 4; k++) { var x = X0 + k * per; if (d > 0) path += ' L' + n1(x) + ' ' + hi + ' L' + n1(x + per * d) + ' ' + hi + ' L' + n1(x + per * d) + ' ' + lo; path += ' L' + n1(x + per) + ' ' + lo; }
      o += ln(X0, lo, X0 + W, lo, 'var(--border)', 1) + pa(path, BL, 2.5) + tx(X0 - 6, hi + 4, '3.3V', 10, 'var(--text-muted)', 'end') + tx(X0 - 6, lo + 4, '0V', 10, 'var(--text-muted)', 'end');
      var avg = lo - (lo - hi) * d; o += ln(X0, avg, X0 + W, avg, OR, 2, 'stroke-dasharray="6 4"') + tx(X0 + W + 4, avg + 4, '平均 ' + f2(3.3 * d) + 'V', 10.5, OR, 'start');
      o += tx(X0 + per / 2, 136, '一個週期 = ' + (1000 / P.f >= 1 ? f2(1000 / P.f) + ' ms' : f1(1e6 / P.f) + ' μs'), 10, 'var(--text-muted)');
      var b = Math.round(255 * Math.pow(d, 0.6)); o += ci(570, 50, 28, 'rgb(' + b + ',' + Math.round(b * 0.85) + ',30)', '#999', 1.5) + tx(570, 96, 'LED 亮度', 10, 'var(--text)');
      var ang = d * 300; o += ci(570, 135, 22, 'none', 'var(--text-muted)', 1.5) + ln(570, 135, 570 + 20 * Math.sin(ang * Math.PI / 180), 135 - 20 * Math.cos(ang * Math.PI / 180), RD, 3) + tx(570, 172, '馬達轉速 ≈ ' + Math.round(d * 100) + '%', 10, 'var(--text)');
      view.innerHTML = svgw('0 0 640 180', o);
      var flick = P.f < 100 ? '<span style="color:' + RD + '">頻率太低，LED 會肉眼可見地閃爍、馬達會抖動！</span>' : P.f < 20000 ? 'LED 已經不會閃爍；但這個頻率落在人耳聽得到的範圍，馬達可能發出「嗡嗡」聲，所以馬達驅動常用 20 kHz 以上。' : '頻率夠高，眼睛和馬達都只「感覺」到平均值。';
      inf.innerHTML = '腳位只能輸出 0 或 3.3 V，但快速地開關，讓「開」的時間占 <b>' + P.d + '%</b>，等效的平均電壓就是 3.3 × ' + f2(d) + ' = <b>' + f2(3.3 * d) + ' V</b>。<br>' + flick + small('LED 亮度用人眼近似的非線性感受示意；實際的馬達轉速還受到負載與驅動電路影響。'); }
    us.forEach(function (u) { u(); });
  }

  /* 2. ADC 量化 */
  function initAdc(root, cfg) { head(root, cfg.q); var P = { n: 3, fs: 16 }, view = el('div');
    var g = el('div', 'display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:0 12px'); root.appendChild(g);
    var us = [slider(g, 'ADC 解析度', 1, 12, 1, P.n, function (x) { return x + ' 位元（' + Math.pow(2, x) + ' 階）'; }, 'n', function (x) { P.n = x; draw(); }), slider(g, '一個週期取樣幾點', 4, 64, 1, P.fs, function (x) { return x + ' 點'; }, 'fs', function (x) { P.fs = x; draw(); })];
    root.appendChild(view); var inf = info(root);
    function draw() { var L = Math.pow(2, P.n), a = [], q = [], e = 0, M = 0;
      for (var t = 0; t <= 1.0001; t += 0.002) a.push([t, 1.65 + 1.5 * Math.sin(2 * Math.PI * t)]);
      for (var k = 0; k <= P.fs; k++) { var tt = k / P.fs, v = 1.65 + 1.5 * Math.sin(2 * Math.PI * tt), code = Math.min(L - 1, Math.floor(v / 3.3 * L)), qv = (code + 0.5) * 3.3 / L; q.push([tt, qv]); if (k < P.fs) q.push([(k + 1) / P.fs, qv]); e += (v - qv) * (v - qv); M = Math.max(M, Math.abs(v - qv)); }
      view.innerHTML = chart(640, 240, [{ d: a, c: GY, n: '真實的類比電壓', w: 1.5 }, { d: q, c: BL, n: 'ADC 讀到的數值（取樣並保持）', w: 2.2 }], { x0: 0, x1: 1, y0: 0, y1: 3.3, xl: '時間（一個週期）', yl: '電壓（V）' });
      var lsb = 3.3 / L;
      inf.innerHTML = '<b>' + P.n + ' 位元</b>的 ADC 把 0～3.3 V 切成 <b>' + L + '</b> 階，每一階（1 LSB）= 3.3 ÷ ' + L + ' = <b>' + (lsb >= 0.01 ? f2(lsb) + ' V' : f2(lsb * 1000) + ' mV') + '</b>；最大量化誤差約半階。理想的訊雜比約 6.02 × ' + P.n + ' + 1.76 ≈ <b>' + f1(6.02 * P.n + 1.76) + ' dB</b>。<br>' +
        (P.fs < 8 ? '<span style="color:' + OR + '">取樣點太少，波形的形狀幾乎看不出來——取樣率至少要大於訊號最高頻率的兩倍（取樣定理）。</span>' : '每多 1 個位元，階數加倍、誤差減半。常見的 MCU 內建 10～12 位元 ADC；音訊常用 16～24 位元。') + small('示意：輸入為 0.15～3.15 V 的正弦波；實際的 ADC 還有雜訊、非線性與參考電壓誤差。'); }
    us.forEach(function (u) { u(); });
  }

  /* 3. 按鍵彈跳 */
  function initBounce(root, cfg) { head(root, cfg.q); var P = { db: 0, seed: 3 }, view = el('div'), sig = [];
    var bb = bar(root), nb = btn('🔁 再按一次按鍵'); bb.appendChild(nb); nb.onclick = function () { P.seed++; build(); draw(); };
    var u1 = slider(root, '去彈跳等待時間', 0, 30, 1, P.db, function (x) { return x === 0 ? '0（不處理）' : x + ' ms'; }, 'db', function (x) { P.db = x; draw(); });
    root.appendChild(view); var inf = info(root);
    function build() { var r = rng(P.seed * 131 + 7), s = []; for (var t = 0; t < 100; t += 0.25) s.push(0);
      function bounce(t0, to) { var t = t0, n = 4 + Math.floor(r() * 6), st = to; for (var i = 0; i < n; i++) { var w = 0.3 + r() * (1.6 - i * 0.12); for (var k = Math.round(t / 0.25); k < Math.round((t + w) / 0.25) && k < s.length; k++) s[k] = st; t += w; st = 1 - st; } for (var k2 = Math.round(t / 0.25); k2 < s.length; k2++) s[k2] = to; return t; }
      var a = 10 + r() * 6; bounce(a, 1); var b2 = 55 + r() * 10; for (var k = Math.round((a + 8) / 0.25); k < Math.round(b2 / 0.25); k++) s[k] = 1; bounce(b2, 0); sig = s; }
    function draw() { var o = '', X0 = 30, W = 590, raw = '', deb = '', st = 0, cand = 0, since = 0, presses = 0, rawP = 0, prev = 0;
      function X(i) { return X0 + i * 0.25 / 100 * W; }
      sig.forEach(function (v, i) { raw += (i ? 'L' : 'M') + n1(X(i)) + ' ' + (v ? 30 : 70); if (v === 1 && prev === 0) rawP++; prev = v;
        if (P.db === 0) { if (v !== st) { st = v; if (v === 1) presses++; } } else { if (v !== cand) { cand = v; since = 0; } else since += 0.25; if (cand !== st && since >= P.db) { st = cand; if (st === 1) presses++; } }
        deb += (i ? 'L' : 'M') + n1(X(i)) + ' ' + (st ? 110 : 150); });
      o += tx(X0, 20, '按鍵腳位的原始訊號', 10.5, 'var(--text-muted)', 'start') + pa(raw, RD, 1.8) + tx(X0, 100, '程式判斷的狀態', 10.5, 'var(--text-muted)', 'start') + pa(deb, GN, 2.2);
      [0, 20, 40, 60, 80, 100].forEach(function (t) { o += tx(X0 + t / 100 * W, 172, t + ' ms', 9.5, 'var(--text-muted)'); });
      view.innerHTML = svgw('0 0 640 180', o);
      inf.innerHTML = '你只按了 <b>1</b> 次，但機械接點在接觸與放開的瞬間會彈跳好幾次：原始訊號出現了 <b>' + rawP + '</b> 次上升緣。程式判斷為 <b>' + presses + '</b> 次按下' + (presses === 1 ? '，<span style="color:' + GN + '">✔ 正確</span>。' : '，<span style="color:' + RD + '">✘ 錯誤</span>。') + '<br>' +
        (P.db === 0 ? '每一次變化都當真，一次按鍵就會被當成好多次。' : P.db < 5 ? '等待時間太短，有些彈跳還是會漏網。' : P.db > 25 ? '雖然正確，但反應變慢了；快速連按時可能漏掉。' : '<b>軟體去彈跳</b>：狀態改變後，等它穩定一段時間（常見 5～20 ms）才承認。') + small('彈跳的次數與時間為隨機示意；也可以用 RC 濾波加上施密特觸發器做硬體去彈跳。'); }
    build(); u1();
  }

  /* 4. 輪詢與中斷 */
  function initIrq(root, cfg) { head(root, cfg.q); var P = { T: 20, seed: 1 }, view = el('div');
    var u1 = slider(root, '輪詢的間隔', 1, 50, 1, P.T, function (x) { return x + ' ms'; }, 'T', function (x) { P.T = x; draw(); });
    var bb = bar(root), nb = btn('🎲 換一組事件'); bb.appendChild(nb); nb.onclick = function () { P.seed++; draw(); };
    root.appendChild(view); var inf = info(root);
    function draw() { var r = rng(P.seed * 97 + 5), ev = []; for (var i = 0; i < 6; i++) ev.push(5 + r() * 185); ev.sort(function (a, b) { return a - b; });
      var o = '', X0 = 30, W = 590; function X(t) { return X0 + t / 200 * W; }
      o += tx(X0, 16, '外部事件（例如感測器送來資料）', 10.5, 'var(--text-muted)', 'start') + tx(X0, 76, '輪詢：每 ' + P.T + ' ms 檢查一次', 10.5, 'var(--text-muted)', 'start') + tx(X0, 136, '中斷：事件一發生，硬體立刻通知 CPU', 10.5, 'var(--text-muted)', 'start');
      for (var t = 0; t <= 200; t += P.T) o += ln(X(t), 84, X(t), 104, GY, 1.2);
      var lp = 0, mx = 0; ev.forEach(function (e) { var pt = Math.ceil(e / P.T) * P.T, lat = pt - e; lp += lat; mx = Math.max(mx, lat);
        o += pa('M' + n1(X(e)) + ' 24 l-5 -8 l10 0 Z', RD, 1, RD) + ln(X(e), 26, X(e), 50, RD, 1.5) + rc(X(e), 88, Math.max(1.5, X(pt) - X(e)), 12, 'rgba(230,126,34,0.45)', null, 0) + ci(X(pt), 94, 4, OR) + rc(X(e), 146, Math.max(2, X(e + 0.6) - X(e)), 14, GN, null, 0) + ln(X(e), 140, X(e), 166, GN, 1.5); });
      [0, 50, 100, 150, 200].forEach(function (t) { o += tx(X(t), 186, t + ' ms', 9.5, 'var(--text-muted)'); });
      view.innerHTML = svgw('0 0 640 194', o);
      inf.innerHTML = '輪詢：平均延遲 <b>' + f1(lp / ev.length) + ' ms</b>、最壞 <b>' + f1(mx) + ' ms</b>（橘色），而且 CPU 在 200 ms 內醒來檢查了 <b>' + Math.floor(200 / P.T + 1) + '</b> 次，其中大多數什麼都沒有。<br>中斷：延遲通常只有<b>微秒</b>等級（綠色），沒有事件時 CPU 可以去做別的事，甚至進入睡眠省電。<br>代價：中斷服務程式（ISR）要寫得很短、注意共用變數（加 volatile、關中斷保護），否則會出現難以重現的錯誤。' + small('數字為示意；實際的中斷延遲取決於 MCU、時脈與優先權設定。'); }
    u1();
  }
"""
KEMLIB = lib("kem-w", "__kemLib", JS, {"pwm": "initPwm", "adc": "initAdc", "bounce": "initBounce", "irq": "initIrq"})
lesson, W = kit(u"🔌", "kem-w", KEMLIB, u"本課以 ARM Cortex-M 等常見的 32 位元微控制器為主要例子；暫存器名稱與細節依晶片與廠商而異，實作時請以晶片的資料手冊與參考手冊為準。")

PWM = W({"t": "pwm", "q": u"PWM：用開關做出「中間值」"})
ADC = W({"t": "adc", "q": u"ADC：把類比電壓變成數字"})
BOUNCE = W({"t": "bounce", "q": u"按一次，為什麼算成好幾次？"})
IRQ = W({"t": "irq", "q": u"輪詢還是中斷？"})


MODULES = [
(u"模組 A｜基礎", [

lesson(u"什麼是嵌入式系統", u"藏在萬物裡的電腦",
  [u"理解嵌入式系統的定義", u"區分微控制器與微處理器", u"了解嵌入式系統的特性"],
  [("h", u"看不見的電腦"),
   ("p", u"<strong>嵌入式系統</strong>是為了特定功能、被「嵌入」在某個設備裡的電腦：洗衣機、微波爐、冷氣遙控器、汽車的煞車系統（ABS）、心律調節器、智慧手錶、無人機的飛控……一台現代汽車裡可能有數十到上百個微控制器。全世界每年出貨的微控制器數量以<strong>數百億顆</strong>計，遠遠超過個人電腦與手機。"),
   ("h", u"微控制器與微處理器"),
   ("t", [u"", u"微控制器（MCU）", u"微處理器（MPU）"], [[u"組成", u"CPU、Flash、RAM、週邊全部做在一顆晶片上", u"主要是 CPU，記憶體與週邊在外面"], [u"記憶體", u"Flash 幾十 KB～幾 MB，RAM 幾 KB～幾百 KB", u"RAM 數 GB"], [u"作業系統", u"沒有（裸機）或小型的 RTOS", u"Linux、Windows、Android"], [u"價格與功耗", u"幾十元台幣、微安培～毫安培", u"數百元以上、瓦特等級"], [u"例子", u"STM32、ESP32、AVR（Arduino）、RP2040", u"手機與電腦的處理器、樹莓派"]]),
   ("h", u"嵌入式系統的特性"),
   ("ul", [u"<strong>專用</strong>：只做一件事，而且要做得可靠。", u"<strong>資源有限</strong>：記憶體以 KB 計，每一個位元組都要省著用。", u"<strong>即時</strong>：煞車、安全氣囊必須在規定的時間內反應（" + LS(19) + u"）。", u"<strong>低功耗</strong>：一顆鈕扣電池要撐好幾年（" + LS(20) + u"）。", u"<strong>與實體世界互動</strong>：讀取感測器、控制馬達與燈光（見" + X("phone-sensors", u"手機感測器") + u"、" + X("motors-power-electronics", u"馬達與電力電子") + u"）。", u"<strong>長壽命</strong>：工業設備可能要運作十年以上，不能隨便當機或更新。"]),
   ("h", u"課程地圖"),
   ("t", [u"模組", u"內容"], [[u"A 基礎", u"MCU 架構、開發流程、暫存器、位元操作"], [u"B 週邊", u"GPIO、按鍵、中斷、計時器、PWM、ADC、DAC"], [u"C 通訊", u"UART、I²C、SPI、CAN、USB、無線"], [u"D 系統", u"狀態機、RTOS、低功耗、看門狗、Bootloader"], [u"E 實務", u"除錯、資安、實作案例"]]),
  ],
  u"嵌入式系統是為特定功能嵌入設備中的電腦，如洗衣機、ABS、心律調節器、無人機飛控，汽車內可能有數十到上百個 MCU，每年出貨數百億顆；MCU 把 CPU Flash RAM 週邊做在一顆晶片上，記憶體以 KB 計、裸機或 RTOS、便宜低功耗（STM32 ESP32 AVR RP2040），MPU 需外部記憶體跑 Linux 等；特性有專用、資源有限、即時、低功耗、與實體世界互動、長壽命。",
  [u"微控制器和微處理器有什麼不同？", u"舉出三個生活中的嵌入式系統。", u"為什麼嵌入式系統特別重視即時性與低功耗？"]),

lesson(u"微控制器的架構", u"一顆晶片裡的小電腦",
  [u"認識 MCU 的主要組成", u"理解哈佛架構與匯流排", u"了解常見的 MCU 家族"],
  [("h", u"晶片裡有什麼"),
   ("ul", [u"<strong>CPU 核心</strong>：例如 ARM Cortex-M0／M3／M4／M7、RISC-V、8 位元的 AVR。", u"<strong>Flash</strong>：存放程式與常數，斷電不會消失。", u"<strong>SRAM</strong>：存放變數與堆疊，斷電就消失。", u"<strong>時脈系統</strong>：內部 RC 振盪器或外部石英晶體，經過 PLL 倍頻成系統時脈（數 MHz 到數百 MHz）。", u"<strong>週邊</strong>：GPIO、計時器、ADC、UART、I²C、SPI、USB、DMA……", u"<strong>中斷控制器</strong>（Cortex-M 的 NVIC）（" + LS(8) + u"）。"]),
   ("h", u"匯流排與哈佛架構"),
   ("p", u"許多 MCU 採用<strong>哈佛架構</strong>（或修改的哈佛架構）：指令和資料走不同的匯流排，CPU 可以同時抓指令與讀寫資料（見" + X("comp-arch", u"計算機結構") + u"）。週邊掛在較慢的週邊匯流排上，透過匯流排橋接與 CPU 溝通。"),
   ("h", u"DMA"),
   ("p", u"<strong>DMA</strong>（直接記憶體存取）讓週邊與記憶體之間直接搬資料，不需要 CPU 一個位元組一個位元組地搬：例如 ADC 連續取樣的結果自動存進陣列、UART 收到的資料自動放進緩衝區。CPU 可以同時做別的事，或去睡覺。"),
   ("h", u"常見的家族"),
   ("t", [u"家族", u"特色"], [[u"AVR（ATmega328P）", u"8 位元，Arduino Uno 的核心，簡單易學"], [u"STM32", u"ST 的 ARM Cortex-M 系列，型號極多，工業界常用"], [u"ESP32", u"內建 Wi-Fi 與藍牙，物聯網的熱門選擇"], [u"RP2040", u"樹莓派基金會推出的雙核 Cortex-M0+，有獨特的可程式 I/O"], [u"Nordic nRF52／nRF54", u"低功耗藍牙裝置常用"]]),
   ("p", u"台灣也有許多 MCU 廠商（例如新唐、盛群），產品廣泛用在家電、電腦週邊與工業控制。"),
   ("h", u"怎麼選 MCU"),
   ("p", u"依需求決定：需要多少腳位與哪些週邊？運算量多大（要不要浮點運算單元）？記憶體夠不夠？功耗預算？價格與供貨？開發工具與社群資源？2021 年前後的全球晶片短缺，讓「買得到」也成為重要的考量。"),
  ],
  u"MCU 包含 CPU 核心（Cortex-M、RISC-V、AVR）、存程式的 Flash、存變數堆疊的 SRAM、內部 RC 或外部晶體經 PLL 倍頻的時脈、週邊與中斷控制器 NVIC；多採哈佛架構指令資料分開匯流排，週邊掛在較慢匯流排；DMA 讓週邊與記憶體直接搬資料；常見家族 AVR（Arduino Uno）、STM32、ESP32（Wi-Fi 藍牙）、RP2040、Nordic nRF，台灣有新唐盛群；選型看腳位週邊、運算、記憶體、功耗、價格供貨與工具社群。",
  [u"Flash 和 SRAM 在 MCU 中各存放什麼？", u"DMA 有什麼好處？", u"選擇 MCU 時要考慮哪些因素？"]),

lesson(u"開發流程與工具鏈", u"從程式碼到晶片",
  [u"了解交叉編譯", u"認識工具鏈的組成", u"了解燒錄與開機流程"],
  [("h", u"交叉編譯"),
   ("p", u"在電腦（x86 或 ARM 的筆電）上寫程式，編譯出另一種處理器（例如 Cortex-M）可以執行的機器碼，叫做<strong>交叉編譯</strong>。常用的工具鏈是 GCC（arm-none-eabi-gcc）、Clang/LLVM，或廠商的商業編譯器（見" + X("compilers", u"編譯器") + u"）。"),
   ("h", u"從原始碼到映像檔"),
   ("ol", [u"<strong>編譯</strong>：每個 .c 檔變成目的檔（.o）。", u"<strong>連結</strong>：依照<strong>連結腳本</strong>（linker script），把程式碼放到 Flash 的位址、變數放到 RAM 的位址。", u"<strong>產生映像檔</strong>：.elf（含除錯資訊）、.bin 或 .hex（純粹要燒進 Flash 的內容）。", u"<strong>燒錄</strong>：透過 SWD／JTAG 除錯器（例如 ST-Link、J-Link），或透過 USB、UART 的 Bootloader（" + LS(22) + u"）。"]),
   ("h", u"開機時發生了什麼"),
   ("ol", [u"上電或重置後，Cortex-M 從 Flash 開頭的<strong>向量表</strong>讀出初始的堆疊指標與重置處理函式的位址。", u"<strong>啟動程式碼</strong>（startup）把 .data 區段的初始值從 Flash 複製到 RAM，把 .bss 區段清為 0。", u"設定時脈（SystemInit）。", u"呼叫 main()——在嵌入式系統中，main() 通常是一個<strong>永遠不會結束</strong>的迴圈。"]),
   ("p", u"這和電腦上執行一個 .exe 的過程有許多相似之處，但沒有作業系統替你準備環境（見" + X("how-exe-runs", u"程式是怎麼跑起來的") + u"）。"),
   ("h", u"開發環境"),
   ("ul", [u"<strong>Arduino IDE</strong>：最容易入門，隱藏了大部分的細節。", u"<strong>廠商 IDE</strong>：例如 STM32CubeIDE、MPLAB，提供圖形化的腳位與時脈設定、自動產生初始化程式碼。", u"<strong>PlatformIO、VS Code 加 CMake</strong>：跨平台、適合專業的專案。", u"<strong>Rust、MicroPython</strong>：新的選擇，前者強調記憶體安全，後者適合快速原型。"]),
   ("h", u"HAL 與暫存器"),
   ("p", u"廠商提供<strong>硬體抽象層</strong>（HAL）函式庫，例如 HAL_GPIO_WritePin()，讓程式容易移植、開發快速；但它可能比較大、比較慢，也隱藏了硬體在做什麼。直接操作<strong>暫存器</strong>（" + LS(4) + u"）最有效率，也最能理解晶片。實務上兩者常常混用。"),
  ],
  u"在電腦上編譯另一種處理器的機器碼為交叉編譯，常用 arm-none-eabi-gcc、Clang 或商業編譯器；流程為編譯成 .o、依連結腳本把程式放 Flash 變數放 RAM、產生 .elf .bin .hex、透過 SWD JTAG 除錯器或 Bootloader 燒錄；Cortex-M 開機從向量表讀堆疊指標與重置函式位址，啟動程式把 .data 複製到 RAM 並清 .bss，設定時脈後呼叫不會結束的 main；開發環境有 Arduino IDE、STM32CubeIDE 等廠商 IDE、PlatformIO VS Code CMake、Rust 與 MicroPython；HAL 易移植但較大較慢，暫存器最有效率，實務常混用。",
  [u"什麼是交叉編譯？", u"連結腳本的作用是什麼？", u"MCU 開機後到進入 main() 之前做了哪些事？"]),

lesson(u"暫存器與記憶體映射", u"用寫記憶體控制硬體",
  [u"理解記憶體映射 I/O", u"學會閱讀暫存器說明", u"理解 volatile 的意義"],
  [("h", u"一切都是位址"),
   ("p", u"在 Cortex-M 中，所有的東西都在同一個 32 位元（4 GB）的位址空間中：Flash 在某一段位址、RAM 在另一段，而每一個週邊的控制<strong>暫存器</strong>也有固定的位址。寫入某個位址，就等於對硬體下指令——這叫做<strong>記憶體映射 I/O</strong>。"),
   ("t", [u"區域（典型的 Cortex-M）", u"位址範圍"], [[u"程式碼（Flash）", u"0x0000_0000 起"], [u"SRAM", u"0x2000_0000 起"], [u"週邊", u"0x4000_0000 起"], [u"Cortex-M 系統控制（NVIC、SysTick）", u"0xE000_0000 起"]]),
   ("h", u"讀懂暫存器"),
   ("p", u"參考手冊會描述每個暫存器的每一個位元：例如某個 GPIO 埠的「輸出資料暫存器」，第 5 個位元控制第 5 支腳的高低。寫程式時："),
   ("p", u"<code>#define GPIOA_ODR (*(volatile uint32_t *)0x40020014)</code><br><code>GPIOA_ODR |= (1u &lt;&lt; 5);   // 讓 PA5 輸出高電位</code>"),
   ("p", u"實務上，廠商會提供標頭檔（例如 CMSIS），把暫存器整理成結構，寫成 <code>GPIOA-&gt;ODR |= (1u &lt;&lt; 5);</code>。"),
   ("h", u"volatile"),
   ("p", u"編譯器為了最佳化，可能會假設「沒有人改過的變數值不會變」，因而省略重複的讀取，或者把連續的寫入合併。但硬體暫存器的值可能隨時被硬體改變（例如一個狀態位元），寫入也有副作用。<strong>volatile</strong> 告訴編譯器：每一次讀寫都必須真的去存取記憶體，不能最佳化掉。被中斷服務程式修改的全域變數也要宣告為 volatile（" + LS(8) + u"）。"),
   ("h", u"讀－改－寫的陷阱"),
   ("p", u"<code>|=</code> 其實是三個步驟：讀出、修改、寫回。如果在讀出與寫回之間發生中斷，而中斷也修改了同一個暫存器，中斷的修改就會被覆蓋。許多 MCU 提供專門的「設定／清除」暫存器（例如 STM32 的 BSRR），或位元帶（bit-banding），讓單一的寫入就能原子地改變一個位元。"),
   ("h", u"資料手冊與參考手冊"),
   ("ul", [u"<strong>資料手冊</strong>（Datasheet）：電氣特性、腳位、封裝、電壓與電流的極限。", u"<strong>參考手冊</strong>（Reference Manual）：每個週邊的運作方式與暫存器的詳細說明，常常超過一千頁。", u"<strong>勘誤表</strong>（Errata）：晶片已知的錯誤與解決方法——遇到怪問題時一定要查。"]),
  ],
  u"Cortex-M 所有東西在同一 32 位元位址空間，Flash 約 0x0000_0000、SRAM 0x2000_0000、週邊 0x4000_0000、系統控制 0xE000_0000，寫入週邊暫存器位址就是對硬體下指令即記憶體映射 I/O；參考手冊描述每個位元，可用指標巨集或 CMSIS 結構操作；volatile 告訴編譯器每次讀寫都要真的存取不可最佳化，ISR 修改的全域變數也要 volatile；|= 是讀改寫三步，中間被中斷可能覆蓋，可用設定清除暫存器如 BSRR 或 bit-banding 原子操作；資料手冊講電氣特性、參考手冊講週邊暫存器、勘誤表列晶片已知錯誤。",
  [u"什麼是記憶體映射 I/O？", u"為什麼硬體暫存器要用 volatile 存取？", u"讀－改－寫為什麼可能出問題？怎麼避免？"]),

lesson(u"C 語言的位元操作", u"嵌入式工程師的基本功",
  [u"熟悉位元運算子", u"學會設定、清除、切換與檢查位元", u"了解位元欄位與遮罩"],
  [("h", u"位元運算子"),
   ("t", [u"運算子", u"意義", u"例子（a = 0b1100, b = 0b1010）"], [[u"&amp;", u"AND", u"a &amp; b = 0b1000"], [u"|", u"OR", u"a | b = 0b1110"], [u"^", u"XOR", u"a ^ b = 0b0110"], [u"~", u"NOT（取反）", u"~a 把每個位元反轉"], [u"&lt;&lt;", u"左移", u"1 &lt;&lt; 3 = 0b1000"], [u"&gt;&gt;", u"右移", u"a &gt;&gt; 2 = 0b0011"]]),
   ("h", u"四個基本動作"),
   ("ul", [u"<strong>設定第 n 位</strong>：<code>reg |= (1u &lt;&lt; n);</code>", u"<strong>清除第 n 位</strong>：<code>reg &amp;= ~(1u &lt;&lt; n);</code>", u"<strong>切換第 n 位</strong>：<code>reg ^= (1u &lt;&lt; n);</code>", u"<strong>檢查第 n 位</strong>：<code>if (reg &amp; (1u &lt;&lt; n)) { ... }</code>"]),
   ("h", u"多位元欄位"),
   ("p", u"許多暫存器的設定是好幾個位元一組。例如某個 2 位元的欄位在第 4～5 位，要把它設成 0b10："),
   ("p", u"<code>reg = (reg &amp; ~(0x3u &lt;&lt; 4)) | (0x2u &lt;&lt; 4);</code>"),
   ("p", u"先用<strong>遮罩</strong>把那兩位清掉，再放入新的值。"),
   ("h", u"固定寬度的整數"),
   ("p", u"不同的平台上 int 的大小可能不同（8 位元的 AVR 上 int 是 16 位元）。嵌入式程式應該使用 <code>&lt;stdint.h&gt;</code> 的 <strong>uint8_t、int16_t、uint32_t</strong> 等型別，明確地指定大小。另外要小心："),
   ("ul", [u"<strong>有號數的右移</strong>：行為依實作而定，位元操作盡量用無號數。", u"<strong>1 &lt;&lt; 31</strong>：如果 1 是有號的 int，可能造成未定義行為，要寫成 <code>1u &lt;&lt; 31</code>。", u"<strong>整數提升</strong>：uint8_t 參與運算時會先被提升為 int，~ 運算的結果可能和預期不同。"]),
   ("h", u"位元組順序"),
   ("p", u"多位元組的數值在記憶體中有兩種存法：<strong>小端序</strong>（低位元組在前，Cortex-M 通常是這樣）與<strong>大端序</strong>（高位元組在前，網路協定常用）。在不同的系統之間交換資料時（" + LS(13) + u"～" + LS(16) + u"），一定要確認位元組順序。"),
  ],
  u"位元運算子有 & | ^ ~ << >>；設定第 n 位 reg |= (1u << n)、清除 reg &= ~(1u << n)、切換 ^=、檢查 reg & (1u << n)；多位元欄位先用遮罩清掉再放入新值；用 stdint.h 的 uint8_t uint32_t 等固定寬度型別，注意有號右移依實作而定、1 << 31 可能未定義應寫 1u、uint8_t 運算時的整數提升；小端序低位元組在前（Cortex-M 通常），大端序高位元組在前（網路協定），交換資料要確認順序。",
  [u"寫出清除暫存器第 3 位的 C 程式碼。", u"為什麼嵌入式程式要用 uint32_t 而不是 int？", u"小端序和大端序有什麼不同？"]),
]),

(u"模組 B｜週邊", [

lesson(u"GPIO", u"點亮第一顆 LED",
  [u"理解 GPIO 的輸入與輸出模式", u"理解推挽與開汲極", u"了解上拉與下拉電阻"],
  [("h", u"Hello World"),
   ("p", u"嵌入式的「Hello World」是讓一顆 LED 閃爍。<strong>GPIO</strong>（通用輸入輸出）腳位可以被程式設定成輸出（控制 LED、繼電器）或輸入（讀取按鍵、開關）。"),
   ("h", u"設定一支腳位"),
   ("ol", [u"<strong>開啟時脈</strong>：為了省電，週邊預設常常是關的，要先打開該 GPIO 埠的時脈——忘記這一步是初學者最常見的錯誤。", u"<strong>設定模式</strong>：輸入、輸出、類比，或「替代功能」（交給 UART、SPI 等週邊使用）。", u"<strong>設定輸出類型</strong>：推挽或開汲極。", u"<strong>設定速度</strong>：切換的速度越快，雜訊與耗電越大。", u"<strong>設定上拉／下拉</strong>。"]),
   ("h", u"推挽與開汲極"),
   ("ul", [u"<strong>推挽</strong>：可以主動輸出高電位，也可以主動拉到低電位，最常用。", u"<strong>開汲極</strong>：只能主動拉低，高電位要靠外部的上拉電阻。好處是可以接到不同電壓的電路，而且多個裝置可以共用一條線（" + LS(14) + u"的 I²C 就是這樣）。"]),
   ("h", u"上拉與下拉"),
   ("p", u"一支沒有接任何東西的輸入腳位是「<strong>浮接</strong>」的，讀到的值會隨雜訊亂跳。<strong>上拉電阻</strong>讓它在沒有訊號時保持高電位，<strong>下拉電阻</strong>則保持低電位。按鍵通常一端接地、另一端接開啟內部上拉的腳位：沒按時讀到 1，按下時讀到 0（" + LS(7) + u"）。"),
   ("h", u"電流與保護"),
   ("ul", [u"每支腳位能提供的電流有限（常見約 8～25 mA），整顆晶片也有總電流的上限。", u"LED 一定要串聯<strong>限流電阻</strong>：例如 3.3 V、LED 壓降約 2 V、想要 5 mA，電阻約 (3.3 − 2) ÷ 0.005 = 260 Ω。", u"馬達、繼電器等大電流的負載，要用電晶體或驅動 IC，並加上保護二極體（見" + X("electronics", u"電子學") + u"）。", u"注意電壓：3.3 V 的 MCU 接到 5 V 的訊號可能燒毀，除非腳位標明「5 V 容忍」。"]),
  ],
  u"嵌入式的 Hello World 是 LED 閃爍，GPIO 可設輸出或輸入；設定步驟為開啟埠時脈（最常忘）、設模式（輸入輸出類比替代功能）、輸出類型、速度、上下拉；推挽可主動輸出高低，開汲極只能拉低需外部上拉，可接不同電壓與共用線如 I²C；浮接輸入會亂跳，上拉保持高下拉保持低，按鍵常接地加內部上拉沒按讀 1 按下讀 0；腳位電流有限約 8～25 mA，LED 要限流電阻（3.3 V 例約 260 Ω），大電流負載用電晶體驅動並加保護二極體，注意 5 V 容忍。",
  [u"設定 GPIO 之前，為什麼要先開啟時脈？", u"推挽和開汲極有什麼不同？", u"為什麼輸入腳位需要上拉或下拉電阻？"]),

lesson(u"按鍵與彈跳", u"按一次算一次",
  [u"理解機械接點的彈跳", u"學會軟體與硬體去彈跳", u"處理長按與連按"],
  [("h", u"接點會彈跳"),
   ("p", u"按鍵是兩片金屬接觸。在按下與放開的瞬間，金屬片會像球落地一樣彈跳好幾次，持續數毫秒到十幾毫秒。MCU 的反應速度是微秒等級，於是會看到一連串快速的 0、1 變化。"),
   BOUNCE,
   ("h", u"軟體去彈跳"),
   ("ul", [u"<strong>延遲確認</strong>：偵測到變化後，等一段時間（例如 10～20 ms）再讀一次，狀態相同才承認。", u"<strong>計數法</strong>：每 1 ms 讀一次，連續 N 次都相同才改變狀態。", u"<strong>移位暫存器法</strong>：每次讀到的值移進一個 8 位元變數，變成 0xFF 或 0x00 才確認——程式非常短。"]),
   ("p", u"避免在中斷服務程式裡用忙碌等待（delay）去彈跳，那會讓整個系統卡住。比較好的做法是用計時器定期掃描按鍵（" + LS(9) + u"）。"),
   ("h", u"硬體去彈跳"),
   ("p", u"在按鍵上加一個 <strong>RC 低通濾波</strong>（電阻加電容），讓電壓變化變得平滑；再接到<strong>施密特觸發器</strong>的輸入（有遲滯，上升與下降的切換電壓不同），就能輸出乾淨的訊號。許多 MCU 的輸入腳位本身就有施密特觸發的特性。"),
   ("h", u"長按、連按與組合鍵"),
   ("p", u"有了乾淨的按下／放開事件，就可以用<strong>狀態機</strong>（" + LS(18) + u"）實作更多功能：按住超過 1 秒算「長按」、在 300 ms 內按兩次算「雙擊」、按住不放每 100 ms 觸發一次「連發」。"),
   ("h", u"按鍵矩陣"),
   ("p", u"需要很多按鍵（例如鍵盤、電話的數字鍵）時，把按鍵排成矩陣：16 個按鍵只需要 4 條列線與 4 條行線。程式輪流把一條列線拉低，讀取各行線，就能知道哪個鍵被按下；同時按多個鍵時，要用二極體避免「鬼鍵」。"),
  ],
  u"按鍵兩片金屬在按下放開時彈跳數毫秒到十幾毫秒，MCU 微秒級反應會看到多次 0 1 變化；軟體去彈跳有延遲確認約 10～20 ms、連續 N 次相同的計數法、8 位元移位成 0xFF 或 0x00 的移位暫存器法，避免在 ISR 中忙碌等待應用計時器定期掃描；硬體以 RC 低通加施密特觸發器；以狀態機實作長按、雙擊與連發；矩陣按鍵 16 鍵只需 4 列 4 行輪流掃描，多鍵同按用二極體防鬼鍵。",
  [u"按鍵彈跳是怎麼發生的？", u"說明一種軟體去彈跳的方法。", u"按鍵矩陣如何節省腳位？"]),

lesson(u"中斷", u"有事就叫我",
  [u"理解中斷的運作流程", u"區分輪詢與中斷", u"學會撰寫安全的中斷服務程式"],
  [("h", u"兩種等待的方式"),
   ("p", u"程式要知道「按鍵被按了」「資料送到了」，有兩種方法：<strong>輪詢</strong>——一直反覆地去檢查；<strong>中斷</strong>——硬體在事件發生時，主動打斷 CPU 正在做的事，跳去執行一段處理程式。"),
   IRQ,
   ("h", u"中斷發生時"),
   ("ol", [u"週邊設定中斷旗標，中斷控制器（NVIC）檢查這個中斷是否開啟、優先權是否夠高。", u"CPU 完成目前的指令，把暫存器（程式計數器、狀態等）自動<strong>推入堆疊</strong>。", u"從<strong>向量表</strong>找到對應的<strong>中斷服務程式</strong>（ISR）並跳過去執行。", u"ISR 結束後，從堆疊恢復暫存器，回到原本被打斷的地方繼續執行。"]),
   ("h", u"優先權與巢狀"),
   ("p", u"每個中斷有優先權：高優先權的中斷可以打斷正在執行的低優先權 ISR（<strong>巢狀中斷</strong>）。安全相關或時間要求嚴格的事件（例如馬達過電流）應該給最高的優先權。"),
   ("h", u"寫 ISR 的守則"),
   ("ul", [u"<strong>越短越好</strong>：只做必要的事（讀資料、設旗標、放進緩衝區），把耗時的工作交給主迴圈。", u"<strong>不要等待</strong>：不要在 ISR 中用 delay 或等待其他事件。", u"<strong>清除中斷旗標</strong>：否則一離開又會立刻再進來，系統卡死。", u"<strong>共用變數</strong>：宣告為 volatile（" + LS(4) + u"）；主程式讀寫多位元組的共用資料時，要短暫地關閉中斷，避免讀到「一半新、一半舊」的值（<strong>競爭條件</strong>）。", u"<strong>不要呼叫不可重入的函式</strong>：例如 printf、malloc。"]),
   ("h", u"其他中斷來源"),
   ("p", u"計時器溢位（" + LS(9) + u"）、ADC 轉換完成、UART 收到資料、DMA 傳完、外部腳位的邊緣變化、看門狗、錯誤（HardFault）……幾乎每個週邊都能產生中斷。善用中斷，是嵌入式程式又快又省電的關鍵。"),
  ],
  u"輪詢一直反覆檢查，中斷由硬體在事件發生時打斷 CPU 執行處理程式；流程為週邊設旗標 NVIC 檢查開啟與優先權、CPU 完成指令把暫存器推入堆疊、從向量表跳到 ISR、結束後恢復並返回；高優先權可打斷低優先權即巢狀中斷；ISR 守則：越短越好只設旗標放緩衝、不等待、清除旗標、共用變數 volatile 並在主程式讀多位元組時短暫關中斷避免競爭條件、不呼叫 printf malloc 等不可重入函式；中斷來源包括計時器、ADC、UART、DMA、外部腳位、看門狗與 HardFault。",
  [u"輪詢和中斷各有什麼優缺點？", u"中斷發生時，CPU 做了哪些事？", u"為什麼 ISR 要寫得越短越好？"]),

lesson(u"計時器", u"MCU 的心跳",
  [u"理解計時器的運作", u"學會計算預除頻與重載值", u"認識計時器的各種用途"],
  [("h", u"一個會數數的電路"),
   ("p", u"<strong>計時器</strong>是一個由時脈驅動、不斷加一（或減一）的計數器。計數到設定的上限時<strong>溢位</strong>，歸零重來，並可以產生中斷。因為它由硬體計數，時間非常精準，也不佔用 CPU。"),
   ("h", u"計算週期"),
   ("p", u"計時器的時脈先經過<strong>預除頻器</strong>（Prescaler，PSC）除頻，再由計數器數到<strong>自動重載值</strong>（ARR）："),
   D(r"f_{\text{update}} = \frac{f_{\text{clk}}}{(\text{PSC}+1)(\text{ARR}+1)}"),
   ("p", u"例如時脈 72 MHz，想要每 1 ms 中斷一次：PSC = 71（除成 1 MHz），ARR = 999（數 1000 下）→ 1 kHz。"),
   ("h", u"計時器的用途"),
   ("ul", [u"<strong>週期性的工作</strong>：每 1 ms 掃描按鍵、每 10 ms 執行控制迴圈。", u"<strong>系統時基</strong>：Cortex-M 內建的 <strong>SysTick</strong> 計時器常用來產生 1 ms 的「滴答」，作為 delay 函式與 RTOS 排程的基礎（" + LS(19) + u"）。", u"<strong>PWM 輸出</strong>（" + LS(10) + u"）。", u"<strong>輸入擷取</strong>：記錄外部訊號邊緣發生的時刻，用來量測頻率、脈波寬度（例如超音波測距、遙控器的紅外線訊號）。", u"<strong>編碼器介面</strong>：讀取馬達編碼器的位置與方向。", u"<strong>觸發其他週邊</strong>：例如定時觸發 ADC 取樣，讓取樣間隔精確（" + LS(11) + u"）。"]),
   ("h", u"不要用忙碌等待"),
   ("p", u"初學者常寫 <code>for (i = 0; i &lt; 100000; i++);</code> 來延遲。這種延遲的時間取決於時脈與編譯器的最佳化（甚至可能被整個最佳化掉），而且 CPU 在等待時什麼都不能做。用計時器的中斷或「記錄時間戳、檢查是否到期」的<strong>非阻塞</strong>寫法，系統才能同時處理多件事。"),
   ("h", u"溢位的陷阱"),
   ("p", u"用 32 位元的毫秒計數器，大約 49.7 天後會溢位歸零。比較時間時要寫成 <code>(now - start) &gt;= interval</code>（利用無號數的環繞特性），而不是 <code>now &gt;= start + interval</code>，才不會在溢位時出錯——歷史上有不少設備在連續運作約 49.7 天後當機，就是這個原因。"),
  ],
  u"計時器是由時脈驅動不斷計數的硬體，到上限溢位歸零並可產生中斷，精準且不佔 CPU；更新頻率 = 時脈 ÷ ((PSC+1)(ARR+1))，72 MHz 例 PSC 71 ARR 999 得 1 kHz；用途有週期性工作、SysTick 1 ms 系統時基、PWM、輸入擷取量頻率脈寬、編碼器介面、定時觸發 ADC；忙碌等待時間不準可能被最佳化掉且 CPU 不能做別的事，應用中斷或非阻塞時間戳；32 位元毫秒計數約 49.7 天溢位，應寫 (now - start) >= interval。",
  [u"時脈 48 MHz，要產生 1 kHz 的中斷，PSC 與 ARR 可以怎麼設？", u"計時器的輸入擷取可以用來做什麼？", u"為什麼比較時間要寫成 (now - start) >= interval？"]),

lesson(u"PWM", u"用數位做出類比",
  [u"理解 PWM 的原理", u"了解 PWM 的應用", u"了解 PWM 頻率的選擇"],
  [("h", u"快速開關"),
   ("p", u"MCU 的腳位只能輸出高或低，但如果用很快的速度開關，負載（LED、馬達）只會「感受」到平均的效果。<strong>脈波寬度調變</strong>（PWM）就是固定頻率、改變每個週期中「開」的比例（<strong>工作週期</strong>）。"),
   PWM,
   ("h", u"用計時器產生 PWM"),
   ("p", u"計時器從 0 數到 ARR（" + LS(9) + u"）；另外設定一個<strong>比較值</strong>（CCR）：計數值小於 CCR 時輸出高，大於時輸出低。工作週期 = CCR ÷ (ARR + 1)。ARR 越大，工作週期的<strong>解析度</strong>越細，但在相同的時脈下 PWM 頻率就越低——兩者要取捨。"),
   ("h", u"應用"),
   ("ul", [u"<strong>LED 調光</strong>：頻率通常要高於數百 Hz 以避免閃爍；手機螢幕的 PWM 調光頻率過低，有些人會覺得眼睛不舒服。", u"<strong>直流馬達調速</strong>：配合 H 橋驅動電路，還能控制正反轉（見" + X("motors-power-electronics", u"馬達與電力電子") + u"）。", u"<strong>伺服馬達</strong>：用 50 Hz、1～2 ms 的脈波寬度指定角度。", u"<strong>蜂鳴器與聲音</strong>：改變頻率發出不同音高。", u"<strong>電源轉換</strong>：切換式電源用 PWM 控制開關，效率遠高於線性穩壓。", u"<strong>簡易 DAC</strong>：PWM 加上 RC 低通濾波，得到平滑的類比電壓（" + LS(12) + u"）。"]),
   ("h", u"互補輸出與死區"),
   ("p", u"驅動 H 橋或三相馬達時，上下兩個開關不能同時導通，否則電源會直接短路（貫穿）。進階的計時器提供<strong>互補輸出</strong>與<strong>死區時間</strong>：一個關掉後，等一小段時間才打開另一個。"),
  ],
  u"MCU 腳位只能高低，快速開關讓負載感受平均效果，PWM 固定頻率改變工作週期；計時器數到 ARR，計數小於 CCR 輸出高，工作週期 = CCR ÷ (ARR+1)，ARR 越大解析度越細但頻率越低；應用有 LED 調光（數百 Hz 以上避免閃爍）、配 H 橋的直流馬達調速、50 Hz 1～2 ms 伺服馬達、蜂鳴器、切換式電源、PWM 加 RC 低通的簡易 DAC；H 橋需互補輸出與死區時間避免上下同時導通的貫穿短路。",
  [u"工作週期 25% 的 3.3 V PWM，平均電壓是多少？", u"PWM 的頻率和解析度之間有什麼取捨？", u"為什麼驅動 H 橋需要死區時間？"]),

lesson(u"ADC", u"讀取真實世界",
  [u"理解 ADC 的解析度與量化誤差", u"了解取樣率與取樣定理", u"學會提高 ADC 的準確度"],
  [("h", u"從電壓到數字"),
   ("p", u"溫度、光線、聲音、壓力等感測器，大多輸出<strong>類比電壓</strong>。<strong>類比數位轉換器</strong>（ADC）把電壓變成數字，程式才能處理。MCU 中最常見的是<strong>逐次逼近型</strong>（SAR）ADC：像猜數字一樣，從最高位元開始，一位一位地比較決定。"),
   ADC,
   ("h", u"換算"),
   D(r"V = \frac{\text{讀值}}{2^{n}} \times V_{\text{ref}}"),
   ("p", u"例如 12 位元 ADC、參考電壓 3.3 V，讀到 2048，電壓約 1.65 V。"),
   ("h", u"取樣率"),
   ("p", u"根據<strong>取樣定理</strong>，取樣頻率必須大於訊號最高頻率的兩倍，否則會出現<strong>混疊</strong>：高頻的訊號偽裝成低頻（見" + X("dsp-filters", u"數位濾波器與 z 轉換") + u"）。因此 ADC 前面常加<strong>抗混疊濾波器</strong>。另外，用計時器觸發取樣，間隔才會穩定（" + LS(9) + u"）；配合 DMA，可以連續取樣而不打擾 CPU（" + LS(2) + u"）。"),
   ("h", u"提高準確度"),
   ("ul", [u"<strong>參考電壓要穩</strong>：參考電壓的誤差直接反映在結果上；可以用內部的參考電壓來校正。", u"<strong>注意輸入阻抗</strong>：ADC 內部的取樣電容需要時間充電，訊號源的阻抗太高時，要延長取樣時間或加緩衝放大器。", u"<strong>減少雜訊</strong>：類比電源要濾波、類比地與數位地妥善處理、轉換時避免切換大電流。", u"<strong>多次平均</strong>：取多次的平均可以降低雜訊；配合過取樣，還能略微提高有效解析度。", u"<strong>校正</strong>：許多 MCU 提供內建的自我校正。"]),
   ("h", u"其他 ADC"),
   ("p", u"需要高解析度的應用（例如電子秤、音訊）常用外接的 <strong>Σ-Δ</strong>（Sigma-Delta）ADC，以極高的速度取樣再數位濾波，可達 16～24 位元；高速的示波器則用管線式或快閃式 ADC。"),
  ],
  u"感測器多輸出類比電壓，ADC 轉成數字，MCU 常見逐次逼近型 SAR 從最高位元逐位比較；電壓 = 讀值 ÷ 2^n × Vref，12 位元 3.3 V 讀 2048 約 1.65 V，每多一位元階數加倍誤差減半，理想 SNR 約 6.02n + 1.76 dB；取樣率須大於最高頻率兩倍否則混疊，前加抗混疊濾波，用計時器觸發配 DMA 連續取樣；提高準確度要穩定參考電壓、注意輸入阻抗延長取樣時間或加緩衝、減少雜訊、多次平均與過取樣、校正；高解析度用 Σ-Δ ADC 達 16～24 位元。",
  [u"12 位元 ADC、參考電壓 3.3 V，1 LSB 是多少？", u"什麼是混疊？如何避免？", u"列出兩種提高 ADC 準確度的方法。"]),

lesson(u"DAC 與類比輸出", u"把數字變回電壓",
  [u"理解 DAC 的原理", u"比較 DAC 與 PWM 濾波", u"了解 DAC 的應用"],
  [("h", u"數位轉類比"),
   ("p", u"<strong>DAC</strong>（數位類比轉換器）把數字變成對應的電壓：輸出電壓 = 數值 ÷ 2<sup>n</sup> × 參考電壓。常見的結構有<strong>電阻梯</strong>（R-2R）：用兩種阻值的電阻組成梯子，每一個位元控制一個開關。"),
   ("h", u"PWM 加濾波"),
   ("p", u"沒有內建 DAC 的 MCU，可以用 PWM 加上 RC 低通濾波器得到類比電壓（" + LS(10) + u"）。但這有取捨：濾波器的截止頻率要遠低於 PWM 頻率才能讓輸出平滑，結果是輸出對變化的反應變慢；而且殘留的漣波會造成雜訊。"),
   ("t", [u"", u"內建或外接 DAC", u"PWM ＋ RC 濾波"], [[u"輸出品質", u"平滑、精準", u"有漣波"], [u"反應速度", u"快", u"慢（受濾波器限制）"], [u"成本", u"需要 DAC 週邊或晶片", u"只需要一個電阻與電容"], [u"適合", u"音訊、波形產生、精密控制", u"緩慢變化的設定值、LED 調光"]]),
   ("h", u"應用"),
   ("ul", [u"<strong>聲音</strong>：用計時器定時、DMA 把音訊樣本送給 DAC，就能播放聲音或語音提示。", u"<strong>波形產生器</strong>：正弦波、三角波、任意波形。", u"<strong>控制電壓</strong>：設定類比電路的參考電壓、偏壓或馬達驅動器的電流上限。", u"<strong>測試</strong>：產生已知的電壓，用來測試 ADC 與類比電路。"]),
   ("h", u"波形的查表法"),
   ("p", u"MCU 上計算 sin() 很耗時。常見的作法是預先把一個週期的波形算好、存成表格（例如 256 點），播放時按照固定的間隔依序輸出；改變輸出的間隔或跳點的步長，就能改變頻率——這就是<strong>直接數位合成</strong>（DDS）的基本概念。"),
   ("h", u"輸出的驅動能力"),
   ("p", u"MCU 內建的 DAC 輸出能力有限，通常只能驅動高阻抗的負載。要推動喇叭或其他較重的負載，必須加上<strong>運算放大器</strong>緩衝或功率放大器（見" + X("electronics", u"電子學") + u"）。"),
  ],
  u"DAC 把數字變電壓，輸出 = 數值 ÷ 2^n × 參考電壓，常見 R-2R 電阻梯；無 DAC 可用 PWM 加 RC 低通，但截止頻率須遠低於 PWM 頻率使反應變慢且有漣波，DAC 平滑精準快適合音訊波形精密控制，PWM 濾波便宜適合緩慢設定值；應用有計時器加 DMA 播放聲音、波形產生器、控制電壓與測試；查表法預存一週期波形，改變間隔或步長調頻即 DDS；內建 DAC 驅動力有限，需運算放大器緩衝或功率放大。",
  [u"DAC 和 PWM 加濾波各有什麼優缺點？", u"什麼是直接數位合成（DDS）？", u"為什麼 DAC 輸出常常需要加運算放大器？"]),
]),

(u"模組 C｜通訊", [

lesson(u"UART", u"最簡單的序列通訊",
  [u"理解非同步序列通訊", u"了解 UART 的資料格式與鮑率", u"學會用 UART 除錯"],
  [("h", u"兩條線"),
   ("p", u"<strong>UART</strong>（通用非同步收發器）只用兩條線：TX（傳送）與 RX（接收），交叉連接（我的 TX 接你的 RX）。沒有共用的時脈線，雙方事先約定好<strong>鮑率</strong>（每秒傳送的位元數，例如 9600、115200），各自用自己的時脈去「對時」。"),
   ("h", u"一個字元的旅程"),
   ("ol", [u"<strong>閒置</strong>：線路保持高電位。", u"<strong>起始位元</strong>：拉低一個位元的時間，通知對方「要開始了」。", u"<strong>資料位元</strong>：通常 8 位元，從最低位元開始傳。", u"<strong>同位元</strong>（可選）：簡單的錯誤檢查。", u"<strong>停止位元</strong>：回到高電位 1 或 2 個位元的時間。"]),
   ("p", u"常見的設定寫成「115200 8N1」：鮑率 115200、8 個資料位元、沒有同位元、1 個停止位元。每個字元實際要傳 10 個位元，所以 115200 鮑大約每秒能傳 11,520 個位元組。"),
   ("h", u"時脈誤差"),
   ("p", u"因為雙方各自計時，兩邊的時脈誤差加起來要小於約 2%～3%，否則在一個字元的最後幾個位元會取樣錯誤。使用不精確的內部 RC 振盪器時，高鮑率可能出問題。"),
   ("h", u"電氣準位"),
   ("ul", [u"<strong>TTL／CMOS 準位</strong>：MCU 直接輸出的 0／3.3 V（或 5 V）。", u"<strong>RS-232</strong>：舊式電腦序列埠，用正負十幾伏特，而且邏輯相反，需要轉換晶片。", u"<strong>RS-485</strong>：用差動訊號，可以傳到上千公尺、多個裝置共用匯流排，工業設備（例如 Modbus 協定）常用。", u"<strong>USB 轉 UART</strong>：今天電腦大多透過 USB 轉序列的轉換器與 MCU 溝通。"]),
   ("h", u"最好的除錯工具"),
   ("p", u"把訊息透過 UART 印到電腦的終端機（printf 除錯），是嵌入式最常用的除錯方法之一（" + LS(23) + u"）。注意：在時間要求嚴格的程式中，大量輸出會拖慢系統，而且不要在 ISR 中呼叫 printf（" + LS(8) + u"）。接收時，建議用中斷或 DMA 把資料放進<strong>環形緩衝區</strong>，主迴圈再慢慢處理。"),
  ],
  u"UART 只用 TX 與 RX 兩條線交叉連接，沒有共用時脈，雙方約定鮑率如 9600 115200 各自對時；一個字元為閒置高電位、起始位元拉低、通常 8 個資料位元從最低位開始、可選同位元、停止位元，115200 8N1 每字元 10 位元約每秒 11,520 位元組；雙方時脈誤差合計須小於約 2%～3%；準位有 TTL/CMOS、正負十幾伏且邏輯相反的 RS-232、差動可傳上千公尺多點的 RS-485（Modbus）、USB 轉 UART；printf 除錯最常用但會拖慢系統不可在 ISR 中呼叫，接收用中斷或 DMA 放環形緩衝區。",
  [u"「115200 8N1」代表什麼？", u"為什麼 UART 對雙方時脈的準確度有要求？", u"RS-485 和 TTL 準位的 UART 有什麼不同？"]),

lesson(u"I²C", u"兩條線串起一群裝置",
  [u"理解 I²C 的匯流排架構", u"了解 I²C 的通訊流程", u"學會處理常見的 I²C 問題"],
  [("h", u"兩條線、多個裝置"),
   ("p", u"<strong>I²C</strong>（Inter-Integrated Circuit，由飛利浦在 1980 年代提出）只用兩條線：<strong>SCL</strong>（時脈）與 <strong>SDA</strong>（資料），就能連接數十個裝置：溫濕度感測器、加速度計、EEPROM、OLED 螢幕、即時時鐘……每個裝置有一個 7 位元的<strong>位址</strong>。"),
   ("h", u"開汲極與上拉"),
   ("p", u"兩條線都是<strong>開汲極</strong>（" + LS(6) + u"）：每個裝置只能把線拉低，放開時由<strong>上拉電阻</strong>拉回高電位。這樣多個裝置同時驅動也不會短路。上拉電阻常見 2.2 kΩ～10 kΩ：太大，訊號上升太慢；太小，耗電與拉低的電流太大。"),
   ("h", u"一次傳輸"),
   ("ol", [u"<strong>起始條件</strong>：SCL 為高時，SDA 由高變低。", u"主控端送出 7 位元位址加上 1 位元的<strong>讀／寫</strong>方向。", u"被叫到的裝置回應 <strong>ACK</strong>（把 SDA 拉低一個時脈）。", u"傳送資料位元組，每個位元組後面都有 ACK／NACK。", u"<strong>停止條件</strong>：SCL 為高時，SDA 由低變高。"]),
   ("p", u"典型的讀取感測器暫存器：起始 → 位址＋寫 → 暫存器編號 → <strong>重複起始</strong> → 位址＋讀 → 讀出資料 → NACK → 停止。"),
   ("h", u"速度"),
   ("p", u"標準模式 100 kHz、快速模式 400 kHz、快速模式加強版 1 MHz，還有更快的高速模式。I²C 適合短距離（同一塊電路板上）、低速的資料。"),
   ("h", u"常見問題"),
   ("ul", [u"<strong>位址衝突</strong>：兩個相同的感測器位址一樣，有些晶片可以用腳位改變位址，否則需要多工器。", u"<strong>忘了上拉電阻</strong>：線永遠是低電位，什麼都不會動。", u"<strong>匯流排卡死</strong>：通訊中途重置，從端可能把 SDA 一直拉低。解法是主控端手動送出 9 個 SCL 脈波讓它釋放。", u"<strong>時脈延展</strong>：從端可以把 SCL 拉低要求主控端等一下，有些主控端不支援。", u"用<strong>邏輯分析儀</strong>觀察波形，是解決 I²C 問題最有效的方法（" + LS(23) + u"）。"]),
  ],
  u"I²C 由飛利浦 1980 年代提出，只用 SCL 時脈與 SDA 資料兩條線連接數十個有 7 位元位址的裝置；兩線開汲極靠上拉電阻（常 2.2～10 kΩ）回高，多裝置不會短路；傳輸為起始條件（SCL 高時 SDA 由高變低）、位址加讀寫位、ACK、資料與每位元組 ACK/NACK、停止條件，讀暫存器需重複起始；速度 100 kHz、400 kHz、1 MHz，適合板上短距低速；常見問題為位址衝突、忘了上拉、匯流排卡死需手動送 9 個 SCL、時脈延展，用邏輯分析儀解決。",
  [u"I²C 為什麼需要上拉電阻？", u"說明一次 I²C 讀取感測器暫存器的流程。", u"I²C 匯流排卡死時怎麼解決？"]),

lesson(u"SPI", u"快速的全雙工通訊",
  [u"理解 SPI 的四條線", u"了解 SPI 的模式", u"比較 UART、I²C 與 SPI"],
  [("h", u"四條線"),
   ("ul", [u"<strong>SCLK</strong>：主控端提供的時脈。", u"<strong>MOSI</strong>：主控端輸出、從端輸入。", u"<strong>MISO</strong>：主控端輸入、從端輸出。", u"<strong>CS</strong>（晶片選擇）：每個從端一條，拉低表示「我在跟你說話」。"]),
   ("p", u"（近年也有改用 COPI／CIPO 等中性名稱的趨勢。）"),
   ("h", u"像交換位元的移位暫存器"),
   ("p", u"SPI 的本質是兩個<strong>移位暫存器</strong>連成一個環：每一個時脈，主控端送出一個位元，同時從端也送回一個位元——傳送和接收<strong>同時</strong>進行（全雙工）。想讀資料時，主控端也必須送出「假資料」來產生時脈。"),
   ("h", u"四種模式"),
   ("p", u"由兩個設定組合而成：<strong>CPOL</strong>（時脈閒置時是高還是低）與 <strong>CPHA</strong>（在第一個還是第二個邊緣取樣），共四種模式（0～3）。主控端與從端的模式必須一致，否則讀到的資料會錯位——這是 SPI 最常見的問題之一，請查從端晶片的資料手冊。"),
   ("h", u"速度與應用"),
   ("p", u"SPI 沒有位址與 ACK，協定簡單，速度可以達到數十 MHz。適合需要大量資料的裝置：TFT 彩色螢幕、SD 記憶卡、外接 Flash、高速 ADC、無線模組。外接 Flash 還有一次傳 4 位元的 <strong>Quad SPI</strong>，速度更快，甚至可以直接執行上面的程式。"),
   ("h", u"三種序列通訊的比較"),
   ("t", [u"", u"UART", u"I²C", u"SPI"], [[u"線數", u"2（TX、RX）", u"2（SCL、SDA）", u"3 ＋ 每個從端一條 CS"], [u"時脈", u"非同步，約定鮑率", u"同步", u"同步"], [u"多裝置", u"點對點（RS-485 可多點）", u"位址，可掛數十個", u"每個從端一條 CS"], [u"速度", u"通常 ≤ 數 Mbps", u"100 kHz～1 MHz", u"可達數十 MHz"], [u"常見用途", u"除錯、GPS、模組通訊", u"感測器、EEPROM", u"螢幕、記憶卡、Flash"]]),
  ],
  u"SPI 有 SCLK 時脈、MOSI 主出從入、MISO 主入從出與每個從端一條 CS 晶片選擇（近年改稱 COPI/CIPO）；本質是兩個移位暫存器成環，每個時脈同時送出與接收即全雙工，讀資料也須送假資料產生時脈；CPOL 與 CPHA 組成四種模式，主從須一致否則錯位；無位址與 ACK、速度數十 MHz，用於 TFT 螢幕、SD 卡、外接 Flash、高速 ADC，Quad SPI 一次 4 位元可直接執行程式；UART 非同步點對點，I²C 兩線位址 100 kHz～1 MHz 用於感測器，SPI 最快用於螢幕記憶卡。",
  [u"SPI 的四條線各是什麼？", u"為什麼說 SPI 是全雙工的？", u"螢幕通常用 SPI 而溫度感測器常用 I²C，為什麼？"]),

lesson(u"CAN 與 USB", u"汽車與電腦的匯流排",
  [u"了解 CAN 匯流排的特性與仲裁", u"了解 USB 的基本架構", u"認識其他工業匯流排"],
  [("h", u"汽車裡的網路"),
   ("p", u"1980 年代，汽車裡的電子控制單元越來越多，點對點的配線又重又複雜。德國的博世公司開發了 <strong>CAN</strong>（控制器區域網路），1986 年發表，讓引擎、變速箱、煞車、儀表板等數十個單元共用一對雙絞線溝通。今天幾乎所有汽車、許多工業設備與醫療器材都使用 CAN。"),
   ("h", u"CAN 的特點"),
   ("ul", [u"<strong>差動訊號</strong>：兩條線 CAN_H 與 CAN_L 的電壓差代表 0 或 1，抗雜訊能力強；匯流排兩端要接 120 Ω 的終端電阻。", u"<strong>以訊息為中心</strong>：沒有「傳給誰」的位址，而是每則訊息有一個 <strong>ID</strong>（代表內容，例如「車速」），所有節點都收得到，各自決定要不要處理。", u"<strong>非破壞性仲裁</strong>：多個節點同時發送時，邊送邊聽；「0」（顯性）會蓋過「1」（隱性），ID 數值較小的訊息會勝出並繼續傳送，輸的節點自動退出、稍後再送——優先權最高的訊息不會延遲，也不會浪費頻寬。", u"<strong>錯誤處理</strong>：CRC 檢查、確認，以及錯誤計數：一直出錯的節點會自動離開匯流排，避免拖垮整個網路。", u"<strong>速度</strong>：傳統 CAN 最高 1 Mbps；<strong>CAN FD</strong> 可以在資料段提高速度並加大資料量。"]),
   ("p", u"汽車維修用的 OBD-II 接頭，就可以讀到車上 CAN 匯流排的部分資料。也因為 CAN 沒有內建的認證，研究者曾展示透過入侵車上的資訊娛樂系統來發送偽造的 CAN 訊息（見" + X("infosec", u"資訊安全") + u"、" + LS(24) + u"）。"),
   ("h", u"USB"),
   ("ul", [u"<strong>主從架構</strong>：一個主機（電腦）管理所有的裝置，裝置只能在主機詢問時回應。", u"<strong>列舉</strong>：裝置插上後，主機讀取它的<strong>描述元</strong>（我是誰、我需要什麼驅動），再分配位址。", u"<strong>類別</strong>：HID（鍵盤滑鼠）、CDC（虛擬序列埠）、MSC（隨身碟）、Audio 等標準類別，電腦有內建的驅動，不必另外安裝。", u"<strong>傳輸類型</strong>：控制、中斷、大量、等時（音訊、視訊）。"]),
   ("p", u"許多 MCU 內建 USB 週邊，配合廠商或開源的 USB 協定堆疊（例如 TinyUSB），就能讓 MCU 變成鍵盤、虛擬序列埠或隨身碟。"),
   ("h", u"其他工業匯流排"),
   ("p", u"工業自動化中還有 Modbus（常跑在 RS-485 上，" + LS(13) + u"）、PROFIBUS、EtherCAT、PROFINET 等；汽車裡也有低成本的 LIN 與高速的車用乙太網路。"),
  ],
  u"博世開發 CAN 1986 年發表讓汽車數十個 ECU 共用一對雙絞線，今用於汽車工業醫療；CAN_H CAN_L 差動訊號兩端 120 Ω 終端電阻、以訊息 ID 為中心所有節點都收到、非破壞性仲裁顯性 0 蓋過隱性 1 使 ID 小者勝出、CRC 確認與錯誤計數使故障節點離線、傳統最高 1 Mbps 與 CAN FD；OBD-II 可讀部分資料，CAN 無認證曾被展示入侵；USB 為主從架構、插上後列舉讀描述元分配位址、HID CDC MSC Audio 標準類別、控制中斷大量等時四種傳輸，MCU 配 TinyUSB 可成鍵盤或虛擬序列埠；其他有 Modbus、PROFIBUS、EtherCAT、LIN、車用乙太網路。",
  [u"CAN 的仲裁是怎麼運作的？為什麼叫「非破壞性」？", u"USB 裝置插上電腦後，發生了什麼事？", u"為什麼 CAN 在汽車資安上有風險？"]),

lesson(u"無線通訊", u"讓裝置連上網",
  [u"比較常見的無線技術", u"了解低功耗藍牙的運作", u"了解物聯網的架構"],
  [("h", u"選擇無線技術"),
   ("t", [u"技術", u"距離", u"速率", u"功耗", u"典型應用"], [[u"低功耗藍牙（BLE）", u"數十公尺", u"約 1～2 Mbps", u"很低", u"手環、耳機配件、感測器、手機配對"], [u"Wi-Fi", u"數十公尺", u"很高", u"高", u"智慧家電、攝影機"], [u"Zigbee／Thread", u"數十公尺（網狀網路）", u"250 kbps", u"低", u"智慧家居、照明（Matter 標準）"], [u"LoRa／LoRaWAN", u"數公里", u"很低（kbps 以下）", u"很低", u"農業、水表、追蹤"], [u"NB-IoT／LTE-M", u"行動網路覆蓋", u"低", u"低", u"智慧電表、共享單車（見" + X("mobile-networks", u"行動通訊網路") + u"）"]]),
   ("p", u"沒有萬用的技術：距離、資料量、電池壽命、成本與基礎建設，必須互相取捨（見" + X("radio-spectrum", u"無線電頻譜") + u"、" + X("rf-antennas", u"天線與射頻工程") + u"）。"),
   ("h", u"低功耗藍牙"),
   ("ul", [u"<strong>廣播</strong>：裝置定期發出短短的廣播封包（「我在這裡」），手機掃描就能發現；Beacon 只靠廣播傳送資料。", u"<strong>連線</strong>：手機（中央）連上裝置（週邊）後，雙方約定好連線間隔，在約好的時間才醒來交換資料，其他時間都在睡覺——這是低功耗的關鍵。", u"<strong>GATT</strong>：資料組織成「服務」與「特徵值」，例如「心率服務」裡的「心率量測值」。"]),
   ("h", u"天線與射頻設計"),
   ("p", u"無線設計中，最容易出問題的往往是射頻部分：天線的位置與周圍的金屬、電路板的接地、匹配網路。許多產品選用已經通過認證的<strong>無線模組</strong>（例如 ESP32 模組），省去射頻設計與法規認證的麻煩。在台灣販售的無線產品，必須通過國家通訊傳播委員會（NCC）的審驗。"),
   ("h", u"物聯網的架構"),
   ("p", u"典型的物聯網系統：<strong>裝置</strong>（MCU 與感測器）→ <strong>閘道器</strong>（把 BLE、Zigbee、LoRa 轉成網際網路）→ <strong>雲端</strong>（用 MQTT 等協定收集資料、儲存、分析）→ <strong>手機 App 或網頁</strong>。裝置端要考慮斷線重連、資料緩存、時間同步與安全的韌體更新（" + LS(22) + u"、" + LS(24) + u"）。"),
  ],
  u"BLE 數十公尺約 1～2 Mbps 很低功耗用於手環感測器，Wi-Fi 高速高功耗用於家電攝影機，Zigbee/Thread 網狀 250 kbps 用於智慧家居 Matter，LoRa 數公里很低速很低功耗用於農業水表，NB-IoT/LTE-M 用於電表共享單車，需權衡距離資料量電池成本；BLE 以廣播被發現（Beacon），連線後約定連線間隔只在約定時間醒來，資料以 GATT 服務與特徵值組織；射頻部分最易出問題，常用已認證模組，台灣需 NCC 審驗；物聯網架構為裝置、閘道器、雲端 MQTT、App，需考慮重連緩存時間同步與安全韌體更新。",
  [u"智慧水表要用哪一種無線技術比較適合？為什麼？", u"低功耗藍牙如何做到省電？", u"為什麼許多產品選用已認證的無線模組？"]),
]),

(u"模組 D｜系統", [

lesson(u"狀態機與主迴圈", u"不用作業系統也能多工",
  [u"理解超級迴圈架構", u"學會用有限狀態機設計程式", u"學會非阻塞的程式寫法"],
  [("h", u"超級迴圈"),
   ("p", u"最簡單的嵌入式程式架構：初始化之後，進入一個永遠執行的 <code>while (1)</code> 迴圈，依序檢查與處理每一件事。這叫做<strong>超級迴圈</strong>。只要每一件事都處理得夠快、不卡住，就能「看起來」同時做很多事。"),
   ("h", u"阻塞的問題"),
   ("p", u"如果程式寫成「點亮 LED → delay(500) → 關掉 → delay(500)」，在等待的 1 秒內，按鍵、通訊都無法處理。解法是<strong>非阻塞</strong>的寫法：記錄上次切換的時間，每次經過迴圈時檢查「時間到了沒」，到了才切換，沒到就立刻去做別的事（" + LS(9) + u"）。"),
   ("h", u"有限狀態機"),
   ("p", u"許多裝置的行為可以用<strong>狀態</strong>與<strong>事件</strong>描述。以一台自動販賣機為例："),
   ("t", [u"目前狀態", u"事件", u"動作", u"下一個狀態"], [[u"等待投幣", u"投入硬幣", u"累加金額", u"已投幣"], [u"已投幣", u"金額足夠且按下按鈕", u"送出商品、計算找零", u"找零中"], [u"已投幣", u"按下退幣", u"退回硬幣", u"等待投幣"], [u"找零中", u"找零完成", u"—", u"等待投幣"]]),
   ("p", u"用 <code>switch (state)</code> 實作，每個狀態只處理它關心的事件。狀態機讓複雜的邏輯變得清楚、容易測試，也能避免「同時處於兩種模式」的錯誤。按鍵的長按與雙擊（" + LS(7) + u"）、通訊協定的解析、電源管理的模式切換，都很適合用狀態機。"),
   ("h", u"事件驅動"),
   ("p", u"結合中斷：ISR 只負責把「事件」放進佇列（" + LS(8) + u"），主迴圈從佇列取出事件，交給狀態機處理。沒有事件時，主迴圈可以讓 CPU 進入睡眠（" + LS(20) + u"）。這種架構簡單、可靠，許多量產的產品都是這樣寫的。"),
   ("h", u"什麼時候不夠用"),
   ("p", u"當工作越來越多、彼此的時間要求差異很大（例如同時要處理網路協定、檔案系統與即時控制），手動切割成小步驟就變得非常困難——這時就需要即時作業系統（" + LS(19) + u"）。"),
  ],
  u"超級迴圈在初始化後進入 while (1) 依序處理每件事，只要不卡住就看似同時多工；delay 阻塞會使等待期間無法處理按鍵通訊，應用記錄時間檢查是否到期的非阻塞寫法；有限狀態機以狀態與事件描述行為，如自動販賣機的等待投幣、已投幣、找零中，用 switch 實作使邏輯清楚可測，適合按鍵、協定解析、電源模式；事件驅動架構由 ISR 放事件進佇列、主迴圈交給狀態機、無事件時睡眠；工作多且時間要求差異大時需要 RTOS。",
  [u"什麼是超級迴圈？它有什麼限制？", u"為什麼要用非阻塞的寫法？", u"用狀態機描述一個紅綠燈的行為。"]),

lesson(u"即時作業系統", u"RTOS 與排程",
  [u"理解即時系統的意義", u"了解 RTOS 的任務與排程", u"理解同步機制與優先權反轉"],
  [("h", u"即時不等於快"),
   ("p", u"<strong>即時系統</strong>的重點是<strong>在期限內</strong>完成，而且可以預測。<strong>硬即時</strong>：錯過期限就是失敗（安全氣囊、心律調節器、飛控）；<strong>軟即時</strong>：偶爾遲到可以容忍（影音播放）。"),
   ("h", u"RTOS"),
   ("p", u"<strong>即時作業系統</strong>（RTOS）讓程式拆成多個<strong>任務</strong>（執行緒），每個任務有自己的堆疊與優先權，看起來像是同時執行。常見的有 <strong>FreeRTOS</strong>（最普及，現由 AWS 維護）、Zephyr、ThreadX、RT-Thread 等。它們通常只有幾 KB，比 Linux 小得多（見" + X("os-dev", u"作業系統開發") + u"）。"),
   ("h", u"搶先式排程"),
   ("p", u"大多數 RTOS 使用<strong>固定優先權的搶先式排程</strong>：永遠執行「準備好」的任務中優先權最高的那一個；高優先權的任務一旦準備好（例如等待的資料到了），會立刻搶走 CPU。相同優先權的任務則輪流執行。SysTick 計時器提供排程用的「滴答」（" + LS(9) + u"）。"),
   ("h", u"任務之間的溝通"),
   ("ul", [u"<strong>佇列</strong>：一個任務放入資料、另一個取出，最常用也最安全。", u"<strong>號誌</strong>（Semaphore）：通知事件發生，例如 ISR 通知某個任務「資料到了」。", u"<strong>互斥鎖</strong>（Mutex）：保護共用資源（例如同一個 UART），同時只能一個任務使用。", u"<strong>事件旗標、任務通知</strong>等。"]),
   ("h", u"優先權反轉"),
   ("p", u"低優先權任務 L 拿著鎖；高優先權任務 H 也需要這個鎖，只好等待；這時中優先權任務 M 搶走了 L 的 CPU，L 無法釋放鎖——結果 H 被 M 間接卡住。1997 年 NASA 的<strong>火星探路者號</strong>在火星上不斷重開機，就是這個問題造成的。工程師從地球上傳指令，開啟互斥鎖的<strong>優先權繼承</strong>（讓持有鎖的 L 暫時升到 H 的優先權），才解決了問題。"),
   ("h", u"RTOS 的常見錯誤"),
   ("ul", [u"<strong>堆疊溢位</strong>：每個任務的堆疊大小要估算清楚，並開啟溢位檢查。", u"<strong>死結</strong>：兩個任務各拿一個鎖、互相等待對方。", u"<strong>在 ISR 中呼叫不允許的 API</strong>：要用專門的「FromISR」版本。", u"<strong>過度設計</strong>：簡單的產品用狀態機就夠了（" + LS(18) + u"）。"]),
  ],
  u"即時系統重點是在期限內完成且可預測，硬即時錯過即失敗（安全氣囊心律調節器飛控），軟即時偶爾遲到可容忍；RTOS 讓程式拆成有自己堆疊與優先權的任務，常見 FreeRTOS（AWS 維護）、Zephyr、ThreadX、RT-Thread 只有幾 KB；固定優先權搶先式排程永遠執行就緒中最高優先權者，同優先權輪流，SysTick 提供滴答；溝通有佇列、號誌、互斥鎖、事件旗標；優先權反轉為 L 持鎖 H 等待 M 搶 CPU，1997 年火星探路者號不斷重開機，地球上傳開啟優先權繼承解決；常見錯誤為堆疊溢位、死結、ISR 呼叫非 FromISR API、過度設計。",
  [u"硬即時和軟即時有什麼不同？", u"搶先式排程是怎麼運作的？", u"什麼是優先權反轉？火星探路者號如何解決？"]),

lesson(u"低功耗設計", u"一顆電池用十年",
  [u"理解 MCU 的功耗來源", u"認識睡眠模式", u"學會估算電池壽命"],
  [("h", u"功耗從哪裡來"),
   ("p", u"CMOS 電路的功耗主要有兩部分：<strong>動態功耗</strong>（電晶體切換時對電容充放電，大約與時脈頻率與電壓的平方成正比）與<strong>靜態功耗</strong>（漏電流）。降低時脈、降低電壓、關掉不用的週邊時脈，都能省電。"),
   ("h", u"睡眠模式"),
   ("t", [u"模式（名稱依晶片而異）", u"狀態", u"典型電流", u"喚醒"], [[u"執行", u"CPU 全速運作", u"數 mA～數十 mA", u"—"], [u"睡眠", u"CPU 停止，週邊照常", u"約 1 mA", u"任何中斷，幾乎立刻"], [u"停止", u"大部分時脈關閉，RAM 保留", u"數 μA", u"外部中斷、RTC，數 μs"], [u"待機／關機", u"幾乎全部關閉，RAM 消失", u"1 μA 以下", u"特定腳位或 RTC，等同重新開機"]]),
   ("p", u"Cortex-M 用 <code>WFI</code>（等待中斷）指令讓 CPU 進入睡眠。"),
   ("h", u"盡快做完、盡量睡覺"),
   ("p", u"低功耗的核心策略：大部分的時間都在最深的睡眠，偶爾醒來<strong>快速</strong>做完工作（量測、傳送），再回去睡。例如一個溫度感測器每分鐘醒來 10 ms，執行時 5 mA、睡眠時 2 μA："),
   D(r"I_{\text{avg}} \approx 5\,\text{mA}\times\frac{10\,\text{ms}}{60\,\text{s}} + 2\,\mu\text{A} \approx 0.83 + 2 = 2.8\,\mu\text{A}"),
   ("p", u"一顆 220 mAh 的 CR2032 鈕扣電池，理論上可以用大約 220 ÷ 0.0028 ≈ 78,000 小時——將近 9 年。（實際上還要考慮電池的自放電、溫度與脈衝電流的影響。）"),
   ("h", u"容易忽略的耗電"),
   ("ul", [u"<strong>浮接的輸入腳位</strong>：會造成漏電，不用的腳位要設成類比或固定電位（" + LS(6) + u"）。", u"<strong>上拉電阻</strong>：按鍵按住時，電流會一直流過上拉電阻。", u"<strong>電源 IC 的靜態電流</strong>：穩壓器本身的耗電可能比睡眠中的 MCU 還大。", u"<strong>LED 與感測器</strong>：不用時要切斷電源。", u"<strong>無線的連線間隔</strong>：BLE 的間隔太短，耗電大增（" + LS(17) + u"）。"]),
   ("h", u"量測功耗"),
   ("p", u"睡眠時的微安培與執行時的毫安培相差上千倍，普通的電錶很難量準。工程師使用專門的電源分析儀或電流量測工具，觀察每一次醒來的電流波形，找出浪費電的地方。"),
  ],
  u"CMOS 功耗有與頻率及電壓平方成正比的動態功耗和漏電的靜態功耗，降時脈電壓關週邊時脈可省電；睡眠 CPU 停週邊照常約 1 mA、停止大部分時脈關閉 RAM 保留數 μA、待機幾乎全關 RAM 消失 1 μA 以下等同重開機，Cortex-M 用 WFI；策略是盡快做完盡量睡覺，每分鐘醒 10 ms 執行 5 mA 睡眠 2 μA 平均約 2.8 μA，220 mAh CR2032 理論約 78,000 小時近 9 年；容易忽略浮接腳位、上拉電阻、穩壓器靜態電流、LED 感測器、BLE 連線間隔；需專門工具量測電流波形。",
  [u"動態功耗和哪些因素有關？", u"一個裝置每 10 秒醒來 5 ms、執行時 10 mA、睡眠 1 μA，平均電流約多少？", u"列出兩個容易被忽略的耗電來源。"]),

lesson(u"看門狗與可靠性", u"當機了怎麼辦",
  [u"理解看門狗計時器的作用", u"了解常見的故障來源", u"學會可靠性的設計原則"],
  [("h", u"看門狗"),
   ("p", u"<strong>看門狗計時器</strong>（Watchdog）是一個獨立的倒數計時器：程式必須定期「餵狗」（重設計時器）；如果程式卡死、跑飛而沒有餵狗，時間一到，看門狗就會<strong>重置</strong>整個 MCU，讓系統重新開始。對於沒有人在旁邊按重開機的設備（例如路邊的感測器、太空船），看門狗是最後一道防線。"),
   ("h", u"正確地餵狗"),
   ("ul", [u"<strong>不要在計時器中斷裡餵狗</strong>：主程式卡死時，中斷可能還在正常執行，看門狗就失去作用了。", u"<strong>確認每個任務都活著</strong>：在 RTOS 中，每個任務定期回報，監控任務確認全部都正常才餵狗（" + LS(19) + u"）。", u"<strong>視窗看門狗</strong>：太早餵狗也算錯誤，可以抓到「跑飛到錯誤的迴圈裡不斷餵狗」的情況。", u"<strong>記錄重置原因</strong>：開機時讀取重置原因的暫存器，知道是看門狗、斷電還是軟體重置，方便追查問題。"]),
   ("h", u"故障從哪裡來"),
   ("ul", [u"<strong>軟體錯誤</strong>：陣列越界、空指標、堆疊溢位、競爭條件（" + LS(8) + u"）。", u"<strong>電源問題</strong>：電壓下降時 MCU 行為異常——開啟<strong>欠壓偵測</strong>（Brown-out），電壓不足時保持在重置狀態。", u"<strong>電磁干擾</strong>：馬達、繼電器、靜電放電造成的雜訊。", u"<strong>宇宙射線</strong>：高能粒子可能翻轉記憶體中的位元（單一事件翻轉），在航太與高海拔特別重要；可用錯誤更正碼（ECC）記憶體保護。", u"<strong>Flash 寫入壽命</strong>：每個 Flash 區塊只能抹寫約一萬到十萬次，頻繁寫入設定值要做<strong>磨損平均</strong>。"]),
   ("h", u"可靠性的原則"),
   ("ul", [u"<strong>防禦式程式設計</strong>：檢查所有的輸入與回傳值，switch 一定要有 default。", u"<strong>安全狀態</strong>：任何錯誤發生時，系統要進入安全的狀態（例如馬達停止、加熱器關閉）。", u"<strong>不使用動態記憶體</strong>：許多安全規範（例如汽車業的 MISRA C）限制或禁止 malloc，避免記憶體碎片與不可預測的行為。", u"<strong>靜態分析與測試</strong>：在電腦上跑單元測試、用工具檢查程式碼。", u"<strong>功能安全標準</strong>：汽車（ISO 26262）、工業（IEC 61508）、醫療（IEC 62304）都有嚴格的開發流程要求。"]),
   ("p", u"歷史的教訓：1980 年代的 Therac-25 放射治療機，因為軟體的競爭條件與缺乏硬體連鎖保護，造成數名病人遭受過量輻射（見" + X("engineering-disasters", u"工程災難") + u"）。"),
  ],
  u"看門狗是獨立倒數計時器，程式須定期餵狗，卡死跑飛未餵就重置 MCU，是無人設備最後防線；不要在計時器中斷中餵狗、RTOS 中確認每任務活著再餵、視窗看門狗抓太早餵、開機記錄重置原因；故障來源有軟體錯誤、電源問題（開欠壓偵測）、電磁干擾、宇宙射線單一事件翻轉（用 ECC）、Flash 寫入壽命約一萬到十萬次需磨損平均；原則為防禦式程式設計、錯誤時進入安全狀態、不用動態記憶體（MISRA C）、靜態分析與測試、功能安全標準 ISO 26262 IEC 61508 IEC 62304；Therac-25 因競爭條件與缺乏硬體連鎖致病人過量輻射。",
  [u"看門狗計時器的作用是什麼？", u"為什麼不應該在計時器中斷裡餵狗？", u"列出三種嵌入式系統的故障來源。"]),

lesson(u"Bootloader 與韌體更新", u"出廠後還能修好",
  [u"理解 Bootloader 的角色", u"了解 OTA 更新的流程", u"學會設計安全可靠的更新機制"],
  [("h", u"Bootloader"),
   ("p", u"<strong>Bootloader</strong> 是開機時最先執行的一小段程式，放在 Flash 的開頭。它決定要直接跳到主程式（應用程式），還是進入更新模式：從 UART、USB、CAN 或無線接收新的韌體，寫入 Flash 的應用程式區。許多 MCU 在出廠時就在 ROM 中內建了 Bootloader，可以透過 UART 或 USB 燒錄（" + LS(3) + u"）。"),
   ("h", u"跳到應用程式"),
   ("p", u"Bootloader 確認應用程式有效（例如檢查 CRC）之後，關閉中斷與週邊，把<strong>向量表</strong>的位置改到應用程式的開頭，設定堆疊指標，再跳到應用程式的重置處理函式。"),
   ("h", u"OTA 更新"),
   ("p", u"<strong>空中更新</strong>（OTA）讓已經賣出去的產品透過網路更新韌體：修正錯誤、修補漏洞、增加功能。汽車、手機、智慧家電都在使用。"),
   ("h", u"不能變成磚頭"),
   ("p", u"更新到一半斷電、網路中斷，或新版韌體有嚴重的錯誤，裝置可能就此無法開機（「變磚」）。可靠的設計："),
   ("ul", [u"<strong>A/B 雙分區</strong>：Flash 中保留兩個應用程式區。新韌體下載到「另一個」分區，完整驗證後才切換；如果新版開機失敗（例如看門狗重置多次，" + LS(21) + u"），自動<strong>回滾</strong>到舊版。", u"<strong>完整性檢查</strong>：CRC 或雜湊值，確認資料沒有損壞。", u"<strong>Bootloader 本身不更新</strong>（或極少更新），確保永遠有一條「回家的路」。", u"<strong>電量檢查</strong>：電池電量不足時不進行更新。"]),
   ("h", u"安全開機與簽章"),
   ("p", u"如果任何人都能上傳韌體，攻擊者就能植入惡意程式。<strong>安全開機</strong>使用<strong>數位簽章</strong>：廠商用私鑰簽署韌體，裝置用內建的公鑰驗證，簽章不符就拒絕執行（見" + X("cryptography", u"密碼學") + u"）。還要防止<strong>降版攻擊</strong>（刻意安裝有漏洞的舊版），通常用一個只能增加的版本計數器。開源的 MCUboot 是常見的安全 Bootloader 實作（" + LS(24) + u"）。"),
  ],
  u"Bootloader 是開機最先執行放在 Flash 開頭的程式，決定跳到應用程式或從 UART USB CAN 無線接收新韌體寫入，許多 MCU ROM 內建；跳轉前驗 CRC、關中斷週邊、改向量表位置、設堆疊指標再跳到重置函式；OTA 空中更新用於汽車手機家電；避免變磚的設計有 A/B 雙分區下載到另一分區驗證後切換失敗自動回滾、CRC 雜湊完整性、Bootloader 本身不更新、電量檢查；安全開機以私鑰簽署公鑰驗證，防降版攻擊用只能增加的版本計數器，MCUboot 是常見實作。",
  [u"Bootloader 的主要工作是什麼？", u"A/B 雙分區如何避免更新失敗變磚？", u"為什麼韌體需要數位簽章？"]),
]),

(u"模組 E｜實務", [

lesson(u"除錯工具", u"看見看不見的訊號",
  [u"了解 SWD／JTAG 除錯", u"學會使用示波器與邏輯分析儀", u"建立系統化的除錯方法"],
  [("h", u"嵌入式除錯的困難"),
   ("p", u"嵌入式系統沒有螢幕、跑得很快、和實體世界互動——錯誤可能來自程式、也可能來自電路、雜訊或時序。工程師需要同時看見「程式在做什麼」與「電線上發生什麼」。"),
   ("h", u"除錯器"),
   ("p", u"透過 <strong>SWD</strong>（Cortex-M 常用的兩線除錯介面）或 <strong>JTAG</strong>，搭配除錯探針（ST-Link、J-Link、CMSIS-DAP）與 GDB，可以："),
   ("ul", [u"設定<strong>中斷點</strong>，程式停在某一行。", u"<strong>單步執行</strong>，查看與修改變數、暫存器、記憶體。", u"<strong>觀察點</strong>：某個變數被寫入時就停下來——抓記憶體被意外覆蓋的利器。", u"讀取週邊暫存器，確認設定是否正確（" + LS(4) + u"）。"]),
   ("p", u"注意：停在中斷點時 CPU 停了，但馬達、通訊對象不會停，可能造成新的問題。"),
   ("h", u"HardFault"),
   ("p", u"Cortex-M 發生嚴重錯誤（存取不存在的位址、除以零、未對齊存取等）時會進入 <strong>HardFault</strong>。從堆疊中取出發生錯誤時的程式計數器（PC）與連結暫存器（LR），再對照 .map 檔或反組譯，就能找到出錯的那一行。"),
   ("h", u"量測儀器"),
   ("ul", [u"<strong>三用電表</strong>：電壓、電阻、通斷——先確認電源對不對。", u"<strong>示波器</strong>：看類比波形、雜訊、上升時間、電源的突波。", u"<strong>邏輯分析儀</strong>：同時看多條數位訊號，並且能<strong>解碼</strong> UART、I²C、SPI 的內容（" + LS(13) + u"～" + LS(15) + u"）。便宜的 USB 邏輯分析儀加上開源軟體（例如 PulseView）就很好用。", u"<strong>GPIO 打點</strong>：在程式中某段開始時拉高一支腳、結束時拉低，用示波器量測執行時間，比 printf 精確且幾乎不影響時序。"]),
   ("h", u"系統化的除錯"),
   ("ol", [u"<strong>重現問題</strong>：找出穩定觸發的條件。", u"<strong>從簡單的開始檢查</strong>：電源、時脈、接線、腳位設定、時脈有沒有開。", u"<strong>二分法</strong>：把問題的範圍一半一半地縮小。", u"<strong>一次只改一個地方</strong>。", u"<strong>讀勘誤表</strong>（" + LS(4) + u"）。", u"<strong>記錄</strong>：問題、原因與解法，下次就不會再踩。"]),
  ],
  u"嵌入式沒有螢幕跑很快且與實體互動，錯誤可能來自程式電路雜訊時序；SWD 或 JTAG 配 ST-Link J-Link CMSIS-DAP 與 GDB 可設中斷點、單步、觀察點、讀週邊暫存器，但停住時外部世界不會停；HardFault 可從堆疊取 PC 與 LR 對照 map 檔找出錯行；三用電表確認電源、示波器看類比波形、邏輯分析儀看多條數位訊號並解碼 UART I²C SPI（PulseView）、GPIO 打點量執行時間；系統化除錯為重現、從簡單檢查、二分法、一次改一處、讀勘誤表、記錄。",
  [u"觀察點（watchpoint）適合用來找什麼樣的錯誤？", u"邏輯分析儀和示波器各適合看什麼？", u"什麼是 GPIO 打點？為什麼比 printf 好？"]),

lesson(u"嵌入式資安", u"物聯網的弱點",
  [u"了解嵌入式裝置面臨的攻擊", u"認識常見的防護措施", u"了解相關的法規趨勢"],
  [("h", u"為什麼裝置是目標"),
   ("p", u"物聯網裝置數量龐大、長期連網、常常很少更新，而且使用者通常不會改預設的密碼。2016 年，<strong>Mirai</strong> 殭屍網路利用預設帳號密碼，感染了大量的網路攝影機與路由器，發動大規模的分散式阻斷服務攻擊，讓美國許多大型網站一度無法連線（見" + X("cyber-incidents", u"資安事件") + u"）。"),
   ("h", u"攻擊的方式"),
   ("ul", [u"<strong>網路攻擊</strong>：預設密碼、未加密的通訊、協定的漏洞、不安全的雲端 API。", u"<strong>實體存取</strong>：打開外殼，透過 UART 主控台或 SWD／JTAG 除錯介面讀出韌體、竄改程式。", u"<strong>韌體分析</strong>：從更新檔或 Flash 中取出韌體，反組譯找出寫死的金鑰與漏洞。", u"<strong>旁通道攻擊</strong>：量測功耗或電磁輻射的變化，推算出加密的金鑰。", u"<strong>故障注入</strong>：在關鍵時刻讓電壓或時脈出現瞬間的異常，讓 CPU 跳過安全檢查。"]),
   ("h", u"防護措施"),
   ("ul", [u"<strong>沒有預設的共用密碼</strong>：每台裝置唯一的憑證或密碼，第一次使用時強制設定。", u"<strong>加密通訊</strong>：TLS、BLE 的安全配對（見" + X("cryptography", u"密碼學") + u"）。", u"<strong>關閉除錯介面</strong>：量產時啟用讀出保護，鎖住 SWD／JTAG。", u"<strong>安全開機與簽章的更新</strong>（" + LS(22) + u"）。", u"<strong>安全元件與 TrustZone</strong>：把金鑰存在專門的安全晶片或隔離的安全區中，即使主程式被攻破也拿不到。", u"<strong>最小權限與縱深防禦</strong>：關閉不用的服務與連接埠。", u"<strong>長期的漏洞修補</strong>：承諾提供多年的安全更新。"]),
   ("h", u"法規"),
   ("p", u"各國開始立法要求連網產品的資安：英國的產品安全與電信基礎設施法（禁止通用的預設密碼等）、歐盟的<strong>網路韌性法案</strong>（Cyber Resilience Act）、美國的網路信任標章計畫；台灣也有物聯網資安標章的檢測制度（例如影像監控系統）。資安正從「加分」變成「上市的基本要求」（見" + X("infosec", u"資訊安全") + u"）。"),
  ],
  u"物聯網裝置數量多長期連網少更新且使用者不改預設密碼，2016 年 Mirai 用預設帳密感染大量攝影機路由器發動 DDoS 使美國大型網站一度無法連線；攻擊有網路攻擊、透過 UART 主控台或 SWD JTAG 實體存取、韌體分析找寫死金鑰、量功耗電磁的旁通道攻擊、電壓時脈異常的故障注入；防護為每台唯一憑證、TLS 與 BLE 安全配對、量產啟用讀出保護鎖除錯介面、安全開機與簽章更新、安全元件與 TrustZone、最小權限縱深防禦、長期修補；法規有英國 PSTI 法、歐盟網路韌性法案、美國網路信任標章、台灣物聯網資安標章。",
  [u"Mirai 殭屍網路利用了什麼弱點？", u"為什麼量產時要鎖住除錯介面？", u"什麼是旁通道攻擊？"]),

lesson(u"實作案例：智慧溫控器", u"把所有東西組合起來",
  [u"把課程的知識整合成一個產品", u"練習系統架構設計", u"理解產品化的考量"],
  [("h", u"需求"),
   ("p", u"設計一個電池供電的智慧溫控器：量測室溫與濕度、顯示在小螢幕上、按鍵設定目標溫度、透過繼電器控制暖氣或冷氣、用低功耗藍牙讓手機查看與設定、電池要用一年以上。"),
   ("h", u"硬體選擇"),
   ("t", [u"功能", u"選擇", u"相關課程"], [[u"MCU", u"內建 BLE 的低功耗 MCU（例如 nRF52 系列）", LS(2) + u"、" + LS(17)], [u"溫濕度", u"I²C 數位感測器", LS(14)], [u"顯示", u"SPI 介面的電子紙或低功耗 LCD", LS(15)], [u"按鍵", u"3 顆，GPIO 加內部上拉", LS(6) + u"、" + LS(7)], [u"控制輸出", u"GPIO 經電晶體驅動繼電器，加保護二極體", LS(6)], [u"電源", u"兩顆 AA 電池，低靜態電流的穩壓器", LS(20)]]),
   ("h", u"軟體架構"),
   ("ul", [u"<strong>事件驅動 ＋ 狀態機</strong>（" + LS(18) + u"）：狀態有「待機」「設定中」「加熱中」「冷卻中」。", u"<strong>RTC 每 30 秒喚醒</strong>：讀溫濕度、執行控制邏輯，其餘時間深度睡眠。", u"<strong>按鍵中斷喚醒</strong>：去彈跳後更新設定（" + LS(7) + u"）。", u"<strong>遲滯控制</strong>：目標 24 °C 時，低於 23.5 °C 才開暖氣、高於 24.5 °C 才關，避免繼電器頻繁開關（見" + X("control-theory", u"控制理論") + u"）。", u"<strong>BLE</strong>：自訂的 GATT 服務提供溫度、目標值與模式。", u"<strong>看門狗與安全狀態</strong>：感測器讀取失敗時關閉輸出（" + LS(21) + u"）。", u"<strong>OTA</strong>：預留 A/B 分區（" + LS(22) + u"）。"]),
   ("h", u"電池壽命估算"),
   ("p", u"睡眠 3 μA；每 30 秒醒來量測 20 ms（3 mA）；BLE 廣播每 2 秒一次、每次約 3 ms、平均 8 mA；電子紙每 5 分鐘更新一次、每次約 1 秒、5 mA。粗略計算平均電流約 3 + 2 + 12 + 17 ≈ 34 μA，兩顆 AA（約 2,500 mAh）理論上可以用好幾年——但繼電器線圈很耗電，要選<strong>閂鎖型</strong>繼電器（只在切換時耗電）。"),
   ("h", u"從原型到產品"),
   ("ul", [u"<strong>原型</strong>：開發板加模組，快速驗證功能。", u"<strong>電路板設計</strong>：把元件畫在自己的電路板上，注意天線與接地（" + LS(17) + u"）。", u"<strong>法規認證</strong>：無線（NCC）、安規、電磁相容。", u"<strong>量產測試</strong>：每一台出廠前自動測試與燒錄唯一的金鑰（" + LS(24) + u"）。", u"<strong>長期維護</strong>：更新、客服與零件停產的對策。"]),
  ],
  u"電池供電智慧溫控器需量溫濕度、顯示、按鍵設定、繼電器控制、BLE 手機設定、電池一年以上；硬體為內建 BLE 低功耗 MCU、I²C 溫濕度感測器、SPI 電子紙、GPIO 按鍵、電晶體驅動繼電器加保護二極體、低靜態電流穩壓器；軟體為事件驅動加狀態機、RTC 每 30 秒喚醒、按鍵中斷去彈跳、遲滯控制避免頻繁開關、GATT 服務、看門狗與感測失敗關閉輸出、A/B 分區 OTA；平均電流約 34 μA，繼電器需選閂鎖型；產品化需原型、電路板、NCC 等認證、量產測試燒金鑰、長期維護。",
  [u"溫控器為什麼要用遲滯控制？", u"為了省電，溫控器的軟體採用了什麼架構？", u"從原型到量產產品，還需要哪些步驟？"]),

lesson(u"總結", u"從點亮 LED 到完整的產品",
  [u"整理整門課的重點", u"了解嵌入式工程師的學習路徑", u"了解嵌入式的未來趨勢"],
  [("h", u"整門課回顧"),
   ("t", [u"模組", u"核心"], [[u"基礎", u"MCU 架構、交叉編譯、記憶體映射暫存器、volatile、位元操作"], [u"週邊", u"GPIO、去彈跳、中斷、計時器、PWM、ADC、DAC"], [u"通訊", u"UART、I²C、SPI、CAN、USB、BLE 與物聯網"], [u"系統", u"狀態機、RTOS 與優先權反轉、低功耗、看門狗、安全的 OTA"], [u"實務", u"除錯工具、資安、實作案例"]]),
   ("h", u"學習路徑建議"),
   ("ol", [u"用 Arduino 或 MicroPython 做出幾個小作品，建立信心。", u"換到 STM32、ESP32 或 RP2040，學會讀參考手冊、直接操作暫存器。", u"買一台便宜的邏輯分析儀，親眼看 UART、I²C、SPI 的波形。", u"學 FreeRTOS 或 Zephyr，寫一個多任務的專案。", u"學基本的電子學與電路板設計（見" + X("electronics", u"電子學") + u"、" + X("digital-logic", u"數位邏輯") + u"）。", u"做一個完整的產品：電池、外殼、無線、更新。"]),
   ("h", u"未來趨勢"),
   ("ul", [u"<strong>RISC-V</strong>：開放的指令集架構，越來越多 MCU 採用。", u"<strong>邊緣 AI</strong>（TinyML）：在 MCU 上直接執行小型的神經網路，例如語音喚醒詞、異常振動偵測，資料不必上傳雲端（見" + X("deep-learning", u"深度學習") + u"）。", u"<strong>Rust</strong>：用記憶體安全的語言開發嵌入式系統，減少緩衝區溢位等錯誤。", u"<strong>Matter 等統一標準</strong>：讓不同品牌的智慧家居互通。", u"<strong>資安法規</strong>：安全從一開始就要設計進去（" + LS(24) + u"）。", u"<strong>能量採集</strong>：用太陽能、振動或無線電波發電，打造不需要換電池的裝置。"]),
   ("p", u"嵌入式系統是軟體與硬體交會的地方：寫下的每一行程式，都會讓真實世界中的某個東西動起來。延伸：" + X("robotics-autonomy", u"機器人與自主系統") + u"、" + X("os-dev", u"作業系統開發") + u"、" + X("phone-sensors", u"手機感測器") + u"。"),
  ],
  u"整門課涵蓋基礎（架構交叉編譯暫存器 volatile 位元操作）、週邊（GPIO 去彈跳中斷計時器 PWM ADC DAC）、通訊（UART I²C SPI CAN USB BLE）、系統（狀態機 RTOS 低功耗看門狗 OTA）、實務（除錯資安案例）；學習路徑為 Arduino 或 MicroPython 入門、換 STM32 ESP32 RP2040 讀參考手冊、邏輯分析儀看波形、學 RTOS、學電子學與電路板、做完整產品；趨勢有 RISC-V、TinyML 邊緣 AI、Rust、Matter、資安法規、能量採集。",
  [u"整理出嵌入式工程師需要的三項核心能力。", u"什麼是 TinyML？", u"如果要開始學嵌入式，你會從哪一步開始？"]),
]),
]
