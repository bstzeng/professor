// 博雅書院 韓文點擊發聲功能
// 用瀏覽器內建的語音合成（Web Speech API）唸出韓文，零音檔、零後端。
// 效果依裝置與瀏覽器而定：桌機 Chrome 通常有韓文語音，部分手機瀏覽器可能沒有。
//
// 用法（點擊即發聲，行為由 data-ko 屬性決定）：
//   <span class="ko" data-ko="안녕하세요">안녕하세요</span>
//   可選 data-ko-rate="1" 覆寫預設語速（預設 0.85，稍慢以利學習）

(function () {
  'use strict';

  var koreanVoice = null;
  var supported = !!(window.speechSynthesis && window.SpeechSynthesisUtterance);
  // 持續持有目前的 utterance 物件：Chrome/Safari 有個已知的坑——
  // 如果 utterance 沒有被外部變數引用住，垃圾回收機制可能在語音引擎
  // 真正開始念之前就把它回收掉，導致「呼叫了 speak() 卻完全沒聲音」。
  var currentUtterance = null;

  function pickVoice() {
    if (!supported) return;
    var voices = window.speechSynthesis.getVoices() || [];
    koreanVoice =
      voices.find(function (v) { return v.lang === 'ko-KR'; }) ||
      voices.find(function (v) { return v.lang && v.lang.indexOf('ko') === 0; }) ||
      null;
  }

  if (supported) {
    pickVoice();
    window.speechSynthesis.onvoiceschanged = pickVoice;
    // Safari 有時不觸發 onvoiceschanged，補幾次延遲重試
    setTimeout(pickVoice, 300);
    setTimeout(pickVoice, 1000);
    setTimeout(pickVoice, 3000);
  }

  function speak(text, rate) {
    if (!supported) return false;
    // 某些瀏覽器在 cancel() 之後立刻 speak() 會把新的 utterance
    // 靜默丟掉；也有瀏覽器會把整個佇列卡在「暫停」狀態，先 resume()
    // 保險起見。
    window.speechSynthesis.cancel();
    window.speechSynthesis.resume();
    var u = new SpeechSynthesisUtterance(text);
    u.lang = 'ko-KR';
    if (koreanVoice) u.voice = koreanVoice;
    u.rate = rate || 0.85;
    currentUtterance = u;
    setTimeout(function () {
      window.speechSynthesis.speak(u);
    }, 30);
    return true;
  }

  document.addEventListener('click', function (e) {
    var el = e.target.closest('[data-ko]');
    if (!el) return;
    var rate = el.dataset.koRate ? parseFloat(el.dataset.koRate) : undefined;
    var ok = speak(el.dataset.ko, rate);
    if (!ok) return;
    el.classList.add('ko-playing');
    setTimeout(function () { el.classList.remove('ko-playing'); }, 1500);
  });

  var css = [
    '.ko{cursor:pointer;color:var(--gold);border-bottom:1px dashed var(--gold);padding:0 .18em;border-radius:4px;white-space:nowrap;transition:background .15s}',
    '.ko::after{content:" 🔊";font-size:.78em;opacity:.65}',
    '.ko:hover{background:rgba(212,180,100,.13);background:color-mix(in srgb,var(--gold) 14%,transparent)}',
    '.ko.ko-playing{background:rgba(212,180,100,.26);background:color-mix(in srgb,var(--gold) 26%,transparent)}',
    '.ko-btn{cursor:pointer;font:inherit;font-size:.95em;color:var(--gold);background:transparent;border:1px solid var(--gold);border-radius:999px;padding:.32em 1.1em;margin:.3em 0;transition:background .15s}',
    '.ko-btn:hover{background:rgba(212,180,100,.13);background:color-mix(in srgb,var(--gold) 14%,transparent)}',
    'svg [data-ko]{cursor:pointer}',
    'svg .ko-playing{opacity:.62}'
  ].join('\n');
  var styleEl = document.createElement('style');
  styleEl.textContent = css;
  document.head.appendChild(styleEl);

  window.KoreanAudio = {
    speak: speak,
    isSupported: function () { return supported; },
    // 除錯用：列出瀏覽器目前偵測到的所有語音，以及有沒有找到韓文語音。
    // 在瀏覽器主控台輸入 KoreanAudio.listVoices() 即可查看。
    listVoices: function () {
      if (!supported) { console.log('此瀏覽器不支援 Web Speech API'); return []; }
      var voices = window.speechSynthesis.getVoices() || [];
      console.log('偵測到 ' + voices.length + ' 個語音：', voices.map(function (v) { return v.lang + ' — ' + v.name; }));
      console.log('目前選用的韓文語音：', koreanVoice ? (koreanVoice.lang + ' — ' + koreanVoice.name) : '（找不到，會用系統預設語音朗讀）');
      return voices;
    }
  };
})();
