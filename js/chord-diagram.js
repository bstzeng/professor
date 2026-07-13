// 和弦指法圖產生器，支援任意弦數（吉他 6 弦、烏克麗麗 4 弦皆可）。
// 資料格式見 data/chords.js（吉他，[低音 E, A, D, G, B, 高音 e]）、
// data/ukulele-chords.js（烏克麗麗，[G, C, E, A]），由左到右，符合面對指板時的視覺順序。
// 用法：在 HTML 裡放 <div class="chord-diagram-slot" data-chord="C"></div>，
// 若不是讀取預設的 window.CHORD_DATA，再加上 data-chord-source="UKULELE_CHORD_DATA" 這類屬性，
// 頁面載入後呼叫 renderAllChordDiagrams()。

function renderChordDiagram(container, chord) {
  const numStrings = chord.strings.length;
  const numFrets = 4;
  const width = 120;
  const height = 150;
  const left = 15;
  const top = 30;
  const gridW = 90;
  const gridH = 80;
  const dx = gridW / (numStrings - 1);
  const dy = gridH / numFrets;

  const parts = [];
  parts.push(`<svg viewBox="0 0 ${width} ${height}" class="chord-diagram" role="img" aria-label="${chord.name} 和弦指法圖">`);
  parts.push(`<text x="${width / 2}" y="14" class="chord-name" text-anchor="middle">${chord.name}</text>`);

  if (chord.startFret > 1) {
    parts.push(`<text x="${left - 8}" y="${top + dy * 0.7}" class="chord-fret-num" text-anchor="end">${chord.startFret}</text>`);
  } else {
    parts.push(`<rect x="${left - 1}" y="${top - 3}" width="${gridW + 2}" height="3" class="chord-nut"/>`);
  }

  for (let f = 0; f <= numFrets; f++) {
    const y = top + f * dy;
    parts.push(`<line x1="${left}" y1="${y}" x2="${left + gridW}" y2="${y}" class="chord-line"/>`);
  }
  for (let s = 0; s < numStrings; s++) {
    const x = left + s * dx;
    parts.push(`<line x1="${x}" y1="${top}" x2="${x}" y2="${top + gridH}" class="chord-line"/>`);
  }

  if (chord.barre) {
    const y = top + (chord.barre.fret - chord.startFret + 0.5) * dy;
    const x1 = left + chord.barre.fromString * dx;
    const x2 = left + chord.barre.toString * dx;
    parts.push(`<line x1="${x1}" y1="${y}" x2="${x2}" y2="${y}" class="chord-barre"/>`);
  }

  chord.strings.forEach((s, i) => {
    const x = left + i * dx;
    if (s.fret === "x") {
      parts.push(`<text x="${x}" y="${top - 10}" class="chord-mute" text-anchor="middle">×</text>`);
    } else if (s.fret === 0) {
      parts.push(`<circle cx="${x}" cy="${top - 10}" r="4.5" class="chord-open"/>`);
    } else {
      const rel = s.fret - chord.startFret + 1;
      const y = top + (rel - 0.5) * dy;
      parts.push(`<circle cx="${x}" cy="${y}" r="7.5" class="chord-dot"/>`);
      if (s.finger) {
        parts.push(`<text x="${x}" y="${y + 3}" class="chord-finger" text-anchor="middle">${s.finger}</text>`);
      }
    }
  });

  parts.push("</svg>");
  container.innerHTML = parts.join("");
}

function renderAllChordDiagrams(selector) {
  const sel = selector || ".chord-diagram-slot";
  document.querySelectorAll(sel).forEach((el) => {
    const key = el.getAttribute("data-chord");
    const sourceName = el.getAttribute("data-chord-source") || "CHORD_DATA";
    const source = window[sourceName];
    const chord = source && source[key];
    if (chord) renderChordDiagram(el, chord);
  });
}
