// 博雅書院 可執行 JavaScript 程式碼區塊
//
// 用法：
//   <div class="code-playground">
//     <div class="code-playground-bar">
//       <span class="code-playground-label">試試看</span>
//       <button type="button" class="code-playground-run">▶ 執行</button>
//     </div>
//     <textarea class="code-playground-input" spellcheck="false">let x = 5;
// console.log(x + 10);</textarea>
//     <pre class="code-playground-output" hidden></pre>
//   </div>
//
// 程式碼在使用者自己的瀏覽器分頁裡執行（跟直接打開瀏覽器主控台輸入程式碼
// 是同一件事），不會送到任何伺服器，也不會影響其他使用者。如果頁面上
// 另外放了一個帶有固定 id 的 <div>（例如 id="demo-target"），
// 學生的程式碼可以用一般的 document.getElementById(...) 直接操作它，
// 這樣就能示範真正的 DOM 操作，而不只是印出文字結果。
//
// 程式碼一律包在 async 函式裡執行，所以可以直接在最上層寫 await
// （例如 await fetch(...)），不需要學生自己包一層 async。
// console.log 是「全域接管、依目前作用中的練習區即時輸出」的設計——
// 這樣 setTimeout、Promise、await 等非同步程式碼裡的 console.log，
// 即使在按下執行之後才真正被呼叫，也能正確顯示在對的練習區裡，
// 而不是漏接或印到瀏覽器自己的主控台。

(function () {
  'use strict';

  var nativeLog = console.log;
  var activeOutput = null;   // 目前「作用中」的輸出區塊
  var activeLines = [];

  function formatArg(a) {
    if (a instanceof Error) return a.message;
    if (typeof a === 'object' && a !== null) {
      try { return JSON.stringify(a); } catch (e) { return String(a); }
    }
    return String(a);
  }

  // 全域只接管一次 console.log；所有練習區共用同一個接管邏輯，
  // 依「目前作用中的輸出區塊」決定要印到哪裡。
  console.log = function () {
    nativeLog.apply(console, arguments);
    if (!activeOutput) return;
    var line = Array.prototype.slice.call(arguments).map(formatArg).join(' ');
    activeLines.push(line);
    activeOutput.textContent = activeLines.join('\n');
    activeOutput.hidden = false;
  };

  function appendError(output, message) {
    activeLines.push('⚠ 錯誤：' + message);
    output.textContent = activeLines.join('\n');
    output.hidden = false;
    output.classList.add('has-error');
  }

  function run(textarea, output) {
    activeOutput = output;
    activeLines = [];
    output.classList.remove('has-error');
    output.textContent = '';
    output.hidden = false;

    var code = textarea.value;
    try {
      // 包成 async IIFE，讓學生可以直接在最上層寫 await
      var runner = new Function(
        'return (async function () {\n' + code + '\n})()'
      );
      var promise = runner();
      if (promise && typeof promise.then === 'function') {
        promise
          .then(function (result) {
            if (result !== undefined) {
              activeLines.push('→ ' + formatArg(result));
              output.textContent = activeLines.join('\n');
            }
            if (activeLines.length === 0) {
              output.textContent = '（沒有輸出——試試看加一行 console.log(...)）';
            }
          })
          .catch(function (err) {
            appendError(output, err && err.message ? err.message : String(err));
          });
      }
    } catch (e) {
      appendError(output, e.message);
    }
  }

  function init() {
    var playgrounds = document.querySelectorAll('.code-playground');
    playgrounds.forEach(function (el) {
      var textarea = el.querySelector('.code-playground-input');
      var button = el.querySelector('.code-playground-run');
      var output = el.querySelector('.code-playground-output');
      if (!textarea || !button || !output) return;

      var resize = function () {
        textarea.style.height = 'auto';
        textarea.style.height = textarea.scrollHeight + 'px';
      };
      resize();
      textarea.addEventListener('input', resize);

      button.addEventListener('click', function () {
        run(textarea, output);
      });
    });
  }

  document.addEventListener('DOMContentLoaded', init);
})();
