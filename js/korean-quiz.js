// 韓文拼音聽力練習頁的出題邏輯。
// 採用「洗牌袋」出題法：先把全部題目洗牌排成一個佇列，依序出完一輪
// 才重新洗牌——保證亂數出題的同時，短時間內不會重複同一題，
// 也保證每一輪都能練到全部 100 句，比單純每次全隨機更適合練習情境。

(function () {
  'use strict';

  var ALL = (window.KOREAN_QUIZ_SENTENCES || []).slice();
  var queue = [];
  var current = null;
  var answered = 0;
  var round = 1;

  var els = {};

  function shuffle(arr) {
    var a = arr.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var tmp = a[i];
      a[i] = a[j];
      a[j] = tmp;
    }
    return a;
  }

  function refillQueue() {
    queue = shuffle(ALL);
  }

  function nextQuestion() {
    if (queue.length === 0) {
      refillQueue();
      round += 1;
    }
    current = queue.pop();
    render();
  }

  function render() {
    if (!current) return;
    els.koText.textContent = current.ko;
    els.category.textContent = current.cat || '';
    els.answerBox.hidden = true;
    els.roText.textContent = current.ro;
    els.zhText.textContent = current.zh;
    els.showAnswerBtn.hidden = false;
    els.progress.textContent =
      '第 ' + round + ' 輪 · 本輪剩餘 ' + queue.length + ' / ' + ALL.length + ' 題 · 已作答 ' + answered + ' 題';
  }

  function showAnswer() {
    els.answerBox.hidden = false;
    els.showAnswerBtn.hidden = true;
    answered += 1;
    els.progress.textContent =
      '第 ' + round + ' 輪 · 本輪剩餘 ' + queue.length + ' / ' + ALL.length + ' 題 · 已作答 ' + answered + ' 題';
  }

  function playCurrent() {
    if (!current || !window.KoreanAudio) return;
    window.KoreanAudio.speak(current.ko);
  }

  function init() {
    els.koText = document.getElementById('quiz-ko-text');
    els.category = document.getElementById('quiz-category');
    els.answerBox = document.getElementById('quiz-answer');
    els.roText = document.getElementById('quiz-ro-text');
    els.zhText = document.getElementById('quiz-zh-text');
    els.showAnswerBtn = document.getElementById('quiz-show-answer');
    els.playBtn = document.getElementById('quiz-play');
    els.nextBtn = document.getElementById('quiz-next');
    els.progress = document.getElementById('quiz-progress');

    if (!els.koText || ALL.length === 0) return;

    els.showAnswerBtn.addEventListener('click', showAnswer);
    els.playBtn.addEventListener('click', playCurrent);
    els.nextBtn.addEventListener('click', nextQuestion);

    refillQueue();
    nextQuestion();
  }

  document.addEventListener('DOMContentLoaded', init);
})();
