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
    // Safari 有時不觸發 onvoiceschanged，補一次延遲重試
    setTimeout(pickVoice, 500);
  }

  function speak(text, rate) {
    if (!supported) return false;
    window.speechSynthesis.cancel();
    var u = new SpeechSynthesisUtterance(text);
    u.lang = 'ko-KR';
    if (koreanVoice) u.voice = koreanVoice;
    u.rate = rate || 0.85;
    window.speechSynthesis.speak(u);
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

  window.KoreanAudio = { speak: speak, isSupported: function () { return supported; } };
})();
