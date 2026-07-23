// 博雅書院 韓文點擊發聲功能
//
// 播放策略（依序嘗試，前者失敗才用後者）：
//   1. 預先錄好的真人語音檔（audio/ko/<百分比編碼文字>.mp3）——
//      不依賴訪客電腦有沒有安裝韓文語音，任何裝置、任何瀏覽器都能聽到
//      一樣的聲音。用 tools/gen-korean-audio.py 產生。
//   2. 瀏覽器內建語音合成（Web Speech API）——當該句子還沒有錄好的
//      音檔時的備用方案，效果依訪客裝置而定。
//
// 用法（點擊即發聲，行為由 data-ko 屬性決定）：
//   <span class="ko" data-ko="안녕하세요">안녕하세요</span>
//   可選 data-ko-rate="1" 覆寫語音合成備用方案的語速（預設 0.85）

(function () {
  'use strict';

  var koreanVoice = null;
  var supported = !!(window.speechSynthesis && window.SpeechSynthesisUtterance);
  // 持續持有目前的 utterance 物件：Chrome/Safari 有個已知的坑——
  // 如果 utterance 沒有被外部變數引用住，垃圾回收機制可能在語音引擎
  // 真正開始念之前就把它回收掉，導致「呼叫了 speak() 卻完全沒聲音」。
  var currentUtterance = null;

  // 從載入這個檔案的 <script src="...js/korean-audio.js"> 反推站台根目錄，
  // 藉此算出音檔資料夾的正確相對路徑，不論這支腳本被哪個深度的頁面引用。
  function getSiteBase() {
    var scripts = document.getElementsByTagName('script');
    for (var i = 0; i < scripts.length; i++) {
      var src = scripts[i].getAttribute('src') || '';
      if (src.indexOf('korean-audio.js') !== -1) {
        return src.replace(/js\/korean-audio\.js.*$/, '');
      }
    }
    return '';
  }
  var AUDIO_BASE = getSiteBase() + 'audio/ko/';

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

  function speakViaSynthesis(text, rate) {
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

  // 嘗試播放預先錄好的音檔，回傳 Promise：resolve＝真的播放成功，
  // reject＝找不到音檔或播放失敗（呼叫端應接著呼叫語音合成備用方案）。
  function playRecording(text) {
    return new Promise(function (resolve, reject) {
      var url = AUDIO_BASE + encodeURIComponent(text) + '.mp3';
      var audio = new Audio(url);
      var settled = false;
      audio.addEventListener('error', function () {
        if (settled) return;
        settled = true;
        reject(new Error('no recording for: ' + text));
      });
      audio.addEventListener('playing', function () {
        if (settled) return;
        settled = true;
        resolve();
      });
      var p = audio.play();
      if (p && typeof p.catch === 'function') {
        p.catch(function (err) {
          if (settled) return;
          settled = true;
          reject(err);
        });
      }
    });
  }

  function speak(text, rate) {
    playRecording(text).catch(function () {
      speakViaSynthesis(text, rate);
    });
    return true;
  }

  document.addEventListener('click', function (e) {
    var el = e.target.closest('[data-ko]');
    if (!el) return;
    var rate = el.dataset.koRate ? parseFloat(el.dataset.koRate) : undefined;
    speak(el.dataset.ko, rate);
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
    // 除錯用：檢查某句韓文有沒有預錄音檔，在主控台輸入
    // KoreanAudio.hasRecording('안녕하세요').then(console.log)
    hasRecording: function (text) {
      return fetch(AUDIO_BASE + encodeURIComponent(text) + '.mp3', { method: 'HEAD' })
        .then(function (res) { return res.ok; })
        .catch(function () { return false; });
    },
    // 除錯用：列出瀏覽器目前偵測到的所有語音合成備用語音，
    // 在瀏覽器主控台輸入 KoreanAudio.listVoices() 即可查看。
    listVoices: function () {
      if (!supported) { console.log('此瀏覽器不支援語音合成備用方案（Web Speech API）'); return []; }
      var voices = window.speechSynthesis.getVoices() || [];
      console.log('語音合成備用方案偵測到 ' + voices.length + ' 個語音：', voices.map(function (v) { return v.lang + ' — ' + v.name; }));
      console.log('目前選用的韓文備用語音：', koreanVoice ? (koreanVoice.lang + ' — ' + koreanVoice.name) : '（找不到，會用系統預設語音朗讀）');
      console.log('提示：已錄製的句子會優先播放 audio/ko/ 底下的真人語音檔，不受此清單影響。');
      return voices;
    }
  };
})();
