// LeetCode 題解主題的左側題目列表。
//
// 每個題目頁只要在 <body> 上加 data-topic-id="leetcode" 與 data-problem="<題號>"，
// 並放一個 <div id="lc-sidebar">，這支腳本就會從 data/topics.js 讀出完整題目清單、
// 依模組分組渲染，並把目前這一題標成 active。
//
// 因此「新增一題」只需要兩件事：
//   1. 新增 topics/leetcode/problem-XXXX.html
//   2. 在 data/topics.js 的 leetcode 主題裡加一筆 course
// 既有的題目頁不需要重新產生。

(function () {
  const sidebar = document.getElementById("lc-sidebar");
  if (!sidebar) return;

  const topicId = document.body.getAttribute("data-topic-id") || "leetcode";
  const current = document.body.getAttribute("data-problem");
  const topics = (window.SITE_DATA && window.SITE_DATA.topics) || [];
  const topic = topics.find((t) => t.id === topicId);
  if (!topic || !topic.modules) return;

  // 題目頁與 data/topics.js 的 url（相對站台根目錄）之間的換算。
  const base = window.SITE_BASE || "";

  const total = topic.modules.reduce(
    (sum, m) => sum + (m.courses ? m.courses.length : 0),
    0
  );

  // course.title 的格式是「1. Two Sum 兩數之和」，把開頭的題號拆出來單獨顯示。
  function splitNumber(title) {
    const m = /^(\d+)\.\s*(.*)$/.exec(title);
    return m ? { num: m[1], text: m[2] } : { num: "", text: title };
  }

  const html = [
    '<h2 class="lc-sidebar-title">題目列表</h2>',
    '<span class="lc-sidebar-count">共 ' + total + " 題</span>",
  ];

  topic.modules.forEach((module) => {
    html.push(
      '<p class="lc-nav-group-label">' + escapeHTML(module.title) + "</p>"
    );
    html.push('<ul class="lc-nav-list">');
    (module.courses || []).forEach((course) => {
      const parts = splitNumber(course.title);
      const isActive = current && parts.num === String(Number(current));
      html.push(
        '<li><a class="lc-nav-item' +
          (isActive ? " is-active" : "") +
          '" href="' +
          base +
          course.url +
          '"' +
          (isActive ? ' aria-current="page"' : "") +
          '><span class="lc-nav-num">' +
          escapeHTML(parts.num) +
          '</span><span class="lc-nav-text">' +
          escapeHTML(parts.text) +
          "</span></a></li>"
      );
    });
    html.push("</ul>");
  });

  sidebar.innerHTML = html.join("");

  // 題目變多之後，讓側邊欄自動捲到目前這一題。
  const active = sidebar.querySelector(".lc-nav-item.is-active");
  if (active && sidebar.scrollHeight > sidebar.clientHeight) {
    active.scrollIntoView({ block: "nearest" });
  }

  function escapeHTML(s) {
    return String(s).replace(/[&<>"']/g, (c) => ({
      "&": "&amp;",
      "<": "&lt;",
      ">": "&gt;",
      '"': "&quot;",
      "'": "&#39;",
    }[c]));
  }
})();
