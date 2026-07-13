// 歌曲頁共用邏輯（左側清單、右側內容，手機版自動切換成清單/內容單頁顯示）。
//
// 用法：頁面先設定 window.SONGBOOK_CHORD_SOURCE 為 "CHORD_DATA"（吉他）或
// "UKULELE_CHORD_DATA"（烏克麗麗），依序載入對應的和弦資料檔、data/songs.js、
// js/chord-diagram.js，最後呼叫 renderSongbook()。
//
// HTML 需要：
//   <div id="songbook" class="songbook">
//     <aside id="songbook-list" class="songbook-list"></aside>
//     <div id="songbook-content" class="songbook-content"></div>
//   </div>

function renderSongbook() {
  const songs = window.SONGS_DATA || [];
  const listEl = document.getElementById("songbook-list");
  const contentEl = document.getElementById("songbook-content");
  const wrapEl = document.getElementById("songbook");
  if (!listEl || !contentEl) return;

  if (songs.length === 0) {
    listEl.innerHTML = `<div class="empty-state">尚未收錄歌曲，敬請期待。</div>`;
    return;
  }

  let activeId = songs[0].id;
  let activeChord = null;

  function chordChip(name) {
    return `<button type="button" class="chord-chip" data-chord-name="${name}">${name}</button>`;
  }

  function renderList() {
    listEl.innerHTML = songs
      .map(
        (s) => `
        <button type="button" class="songbook-item ${s.id === activeId ? "is-active" : ""}" data-song-id="${s.id}">
          <span class="songbook-item-title">${s.title}</span>
          ${s.artist ? `<span class="songbook-item-artist">${s.artist}</span>` : ""}
        </button>
      `
      )
      .join("");

    listEl.querySelectorAll(".songbook-item").forEach((btn) => {
      btn.addEventListener("click", () => {
        activeId = btn.getAttribute("data-song-id");
        activeChord = null;
        renderList();
        renderContent();
        if (wrapEl) wrapEl.classList.add("show-content");
      });
    });
  }

  function renderPreview() {
    const panel = contentEl.querySelector("#chord-preview-panel");
    if (!panel) return;
    if (!activeChord) {
      panel.hidden = true;
      panel.innerHTML = "";
      return;
    }
    const sourceName = window.SONGBOOK_CHORD_SOURCE || "CHORD_DATA";
    const source = window[sourceName];
    const chordData = source && source[activeChord];
    panel.hidden = false;
    if (chordData) {
      panel.innerHTML = `<div class="chord-preview-diagram"></div>`;
      renderChordDiagram(panel.querySelector(".chord-preview-diagram"), chordData);
    } else {
      panel.innerHTML = `<p class="chord-preview-missing">（尚無「${activeChord}」的指法圖）</p>`;
    }
  }

  function renderContent() {
    const song = songs.find((s) => s.id === activeId);
    if (!song) return;

    const metaParts = [];
    if (song.key) metaParts.push(`原調 ${song.key}`);
    if (typeof song.capo === "number") {
      metaParts.push(song.capo > 0 ? `建議 capo ${song.capo}` : "不需要 capo");
    }

    let bodyHtml = "";
    if (song.chordsOnly) {
      bodyHtml = (song.sections || [])
        .map((sec) => {
          const chips = sec.chords.map(chordChip).join("");
          const repeatLabel = sec.repeat ? `<span class="song-section-repeat">× ${sec.repeat}</span>` : "";
          return `
            <div class="song-section">
              <h3>${sec.label}${repeatLabel}</h3>
              <div class="chord-chip-row">${chips}</div>
            </div>
          `;
        })
        .join("");
    } else if (song.lines) {
      bodyHtml =
        `<div class="song-lyric-lines">` +
        song.lines
          .map((line) => {
            const segs = line
              .map(
                (seg) => `
                <span class="song-lyric-seg">
                  ${seg.chord ? chordChip(seg.chord) : ""}
                  <span class="song-lyric-text">${seg.lyric || ""}</span>
                </span>
              `
              )
              .join("");
            return `<div class="song-lyric-line">${segs}</div>`;
          })
          .join("") +
        `</div>`;
    }

    contentEl.innerHTML = `
      <button type="button" class="songbook-back">← 返回清單</button>
      <h2>${song.title}</h2>
      <p class="songbook-meta">${song.artist ? song.artist + "　" : ""}${metaParts.join("　")}</p>
      ${song.note ? `<p class="songbook-note">${song.note}</p>` : ""}
      <div id="chord-preview-panel" class="chord-preview-panel" hidden></div>
      ${bodyHtml}
    `;

    const backBtn = contentEl.querySelector(".songbook-back");
    if (backBtn) {
      backBtn.addEventListener("click", () => {
        if (wrapEl) wrapEl.classList.remove("show-content");
      });
    }

    contentEl.querySelectorAll(".chord-chip").forEach((chip) => {
      chip.addEventListener("click", () => {
        const name = chip.getAttribute("data-chord-name");
        activeChord = activeChord === name ? null : name;
        contentEl.querySelectorAll(".chord-chip").forEach((c) => {
          c.classList.toggle("is-active", c.getAttribute("data-chord-name") === activeChord);
        });
        renderPreview();
        const panel = contentEl.querySelector("#chord-preview-panel");
        if (panel && !panel.hidden) panel.scrollIntoView({ behavior: "smooth", block: "nearest" });
      });
    });

    renderPreview();
  }

  renderList();
  renderContent();
}
