// 博雅書院 CSS 選擇器 / XPath 練習區
//
// 用法：
//   <div class="selector-playground" data-mode="css">
//     <div class="selector-playground-sample">
//       <!-- 練習用的範例 HTML，會實際被選擇器搜尋 -->
//     </div>
//     <div class="selector-playground-controls">
//       <input type="text" class="selector-playground-input" placeholder="輸入 CSS 選擇器，例如 .price">
//       <button type="button" class="selector-playground-run">套用</button>
//     </div>
//     <p class="selector-playground-result"></p>
//   </div>
//
// data-mode="css" 用 querySelectorAll；data-mode="xpath" 用 document.evaluate。
// 符合的元素會加上 .selector-match 類別（黃色底色高亮），方便直接看到
// 選到了哪些節點，而不只是看數字。

(function () {
  'use strict';

  function clearHighlights(sample) {
    sample.querySelectorAll('.selector-match').forEach(function (el) {
      el.classList.remove('selector-match');
    });
  }

  function runCssSelector(sample, selector) {
    return sample.querySelectorAll(selector);
  }

  function runXPath(sample, expr) {
    var result = document.evaluate(
      expr, sample, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null
    );
    var nodes = [];
    for (var i = 0; i < result.snapshotLength; i++) {
      nodes.push(result.snapshotItem(i));
    }
    return nodes;
  }

  function init() {
    var playgrounds = document.querySelectorAll('.selector-playground');
    playgrounds.forEach(function (el) {
      var sample = el.querySelector('.selector-playground-sample');
      var input = el.querySelector('.selector-playground-input');
      var button = el.querySelector('.selector-playground-run');
      var result = el.querySelector('.selector-playground-result');
      var mode = el.dataset.mode || 'css';
      if (!sample || !input || !button || !result) return;

      var apply = function () {
        clearHighlights(sample);
        var query = input.value.trim();
        if (!query) {
          result.textContent = '請先輸入選擇器';
          result.classList.remove('has-error');
          return;
        }
        try {
          var matches = mode === 'xpath'
            ? runXPath(sample, query)
            : runCssSelector(sample, query);
          matches.forEach(function (node) {
            if (node.nodeType === 1) node.classList.add('selector-match');
          });
          result.textContent = '符合 ' + matches.length + ' 個元素';
          result.classList.remove('has-error');
        } catch (e) {
          result.textContent = '⚠ 選擇器語法錯誤：' + e.message;
          result.classList.add('has-error');
        }
      };

      button.addEventListener('click', apply);
      input.addEventListener('keydown', function (e) {
        if (e.key === 'Enter') { e.preventDefault(); apply(); }
      });
    });
  }

  document.addEventListener('DOMContentLoaded', init);
})();
