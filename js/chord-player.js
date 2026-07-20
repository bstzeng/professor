// 博雅書院 互動和弦播放器
// 用 Web Audio API 即時合成音高，零音檔、零後端。
// 用法（點擊即播放，行為由 data-* 屬性決定）：
//   <span class="cp" data-note="A4">A4</span>
//   <span class="cp" data-chord="Cmaj7">Cmaj7</span>
//   <span class="cp" data-interval="C4,E4">大三度</span>
//   <span class="cp" data-scale="C4,D4,E4,F4,G4,A4,B4,C5">C 大調音階</span>
//   <button class="cp-btn" data-progression="C,G,Am,F">▶ 播放整組</button>
// SVG 內的元素（如鍵盤琴鍵）加上 data-note 即可點擊，不需 .cp 樣式。

(function () {
  'use strict';

  let ctx = null;
  let master = null;

  function ensureCtx() {
    if (!ctx) {
      const AC = window.AudioContext || window.webkitAudioContext;
      if (!AC) return null;
      ctx = new AC();
      const comp = ctx.createDynamicsCompressor();
      comp.threshold.value = -18;
      comp.ratio.value = 6;
      master = ctx.createGain();
      master.gain.value = 0.9;
      master.connect(comp);
      comp.connect(ctx.destination);
    }
    if (ctx.state === 'suspended') ctx.resume();
    return ctx;
  }

  const OFFSETS = { C: 0, D: 2, E: 4, F: 5, G: 7, A: 9, B: 11 };

  function accVal(s) {
    let v = 0;
    for (const ch of s) {
      if (ch === '#' || ch === '♯') v += 1;
      else if (ch === 'b' || ch === '♭') v -= 1;
    }
    return v;
  }

  // "C4"、"F#3"、"B♭4"（無數字時預設第 4 八度）→ MIDI 音號
  function noteToMidi(name) {
    const m = /^\s*([A-Ga-g])([#♯b♭]*)(\d)?\s*$/.exec(name);
    if (!m) return null;
    const oct = m[3] === undefined ? 4 : parseInt(m[3], 10);
    return 12 * (oct + 1) + OFFSETS[m[1].toUpperCase()] + accVal(m[2]);
  }

  // 和弦字尾 → 半音音程堆疊
  const SHAPES = {
    '': [0, 4, 7], 'm': [0, 3, 7], 'dim': [0, 3, 6], 'aug': [0, 4, 8],
    '7': [0, 4, 7, 10], 'maj7': [0, 4, 7, 11], 'M7': [0, 4, 7, 11],
    'm7': [0, 3, 7, 10], 'm7b5': [0, 3, 6, 10], 'm7♭5': [0, 3, 6, 10],
    'dim7': [0, 3, 6, 9], 'sus2': [0, 2, 7], 'sus4': [0, 5, 7],
    'add9': [0, 4, 7, 14], '6': [0, 4, 7, 9], 'm6': [0, 3, 7, 9],
    '9': [0, 4, 7, 10, 14], 'maj9': [0, 4, 7, 11, 14], 'm9': [0, 3, 7, 10, 14],
    '11': [0, 4, 7, 10, 14, 17], '13': [0, 4, 7, 10, 14, 21]
  };

  // "Cmaj7"、"F#m7b5"、"C/E" → MIDI 音號陣列（根音落在 C3 起算的音域）
  function parseChord(sym) {
    let s = sym.trim();
    let bassMidi = null;
    const slash = s.split('/');
    if (slash.length === 2) {
      s = slash[0].trim();
      const bm = /^([A-G])([#♯b♭]*)$/.exec(slash[1].trim());
      if (bm) bassMidi = 36 + ((((OFFSETS[bm[1]] + accVal(bm[2])) % 12) + 12) % 12);
    }
    const m = /^([A-G])([#♯b♭]*)(.*)$/.exec(s);
    if (!m || !(m[3] in SHAPES)) return null;
    const pc = (((OFFSETS[m[1]] + accVal(m[2])) % 12) + 12) % 12;
    const root = 48 + pc;
    const notes = SHAPES[m[3]].map(i => root + i);
    if (bassMidi !== null) {
      while (bassMidi >= notes[0]) bassMidi -= 12;
      notes.unshift(bassMidi);
    }
    return notes;
  }

  // 單顆音的合成：三角波為主體＋高八度正弦增亮，低通濾波修飾，撥弦式衰減
  function tone(midi, at, dur, vel) {
    const c = ensureCtx();
    if (!c) return;
    const t0 = c.currentTime + at;
    const f = 440 * Math.pow(2, (midi - 69) / 12);
    const env = c.createGain();
    env.gain.setValueAtTime(0.0001, t0);
    env.gain.linearRampToValueAtTime(vel, t0 + 0.012);
    env.gain.exponentialRampToValueAtTime(Math.max(vel * 0.25, 0.001), t0 + dur * 0.5);
    env.gain.exponentialRampToValueAtTime(0.0001, t0 + dur);
    const lp = c.createBiquadFilter();
    lp.type = 'lowpass';
    lp.frequency.value = Math.min(f * 5, 7000);
    env.connect(lp);
    lp.connect(master);
    [[1, 'triangle', 1], [2, 'sine', 0.25]].forEach(function (spec) {
      const o = c.createOscillator();
      o.type = spec[1];
      o.frequency.value = f * spec[0];
      const og = c.createGain();
      og.gain.value = spec[2];
      o.connect(og);
      og.connect(env);
      o.start(t0);
      o.stop(t0 + dur + 0.05);
    });
  }

  // 各播放模式：回傳總長（秒），供視覺回饋使用
  function playNote(n) {
    const m = noteToMidi(n);
    if (m === null) return 0;
    tone(m, 0, 1.3, 0.5);
    return 1.4;
  }

  // 和弦：先琶音（一顆一顆聽出組成音）、再齊響
  function playChord(sym) {
    const ns = parseChord(sym);
    if (!ns) return 0;
    ns.forEach(function (n, i) { tone(n, i * 0.17, 1.1, 0.4); });
    const tBlock = ns.length * 0.17 + 0.45;
    ns.forEach(function (n) { tone(n, tBlock, 1.9, 0.33); });
    return tBlock + 2.0;
  }

  // 音程：兩音先後、再同時
  function playInterval(list) {
    const ms = list.map(noteToMidi);
    if (ms.some(function (m) { return m === null; })) return 0;
    tone(ms[0], 0, 0.8, 0.5);
    tone(ms[1], 0.7, 0.8, 0.5);
    ms.forEach(function (m) { tone(m, 1.65, 1.7, 0.42); });
    return 3.5;
  }

  // 音階：依序彈奏，末音延長
  function playScale(list) {
    const ms = list.map(noteToMidi);
    if (ms.some(function (m) { return m === null; })) return 0;
    ms.forEach(function (m, i) {
      tone(m, i * 0.33, i === ms.length - 1 ? 1.3 : 0.6, 0.48);
    });
    return ms.length * 0.33 + 1.4;
  }

  // 和弦進行：逐個輕刷（30ms 錯開模擬刷弦）
  function playProgression(chords) {
    let t = 0;
    chords.forEach(function (sym) {
      const ns = parseChord(sym);
      if (ns) ns.forEach(function (n, i) { tone(n, t + i * 0.03, 1.7, 0.34); });
      t += 0.9;
    });
    return t + 1.2;
  }

  function splitList(s) {
    return s.split(',').map(function (x) { return x.trim(); }).filter(Boolean);
  }

  document.addEventListener('click', function (e) {
    const el = e.target.closest('[data-chord],[data-note],[data-interval],[data-scale],[data-progression]');
    if (!el) return;
    let secs = 0;
    if (el.dataset.chord) secs = playChord(el.dataset.chord);
    else if (el.dataset.note) secs = playNote(el.dataset.note);
    else if (el.dataset.interval) secs = playInterval(splitList(el.dataset.interval));
    else if (el.dataset.scale) secs = playScale(splitList(el.dataset.scale));
    else if (el.dataset.progression) secs = playProgression(splitList(el.dataset.progression));
    if (secs > 0) {
      el.classList.add('cp-playing');
      setTimeout(function () { el.classList.remove('cp-playing'); }, Math.min(secs, 6) * 1000);
    }
  });

  const css = [
    '.cp{cursor:pointer;color:var(--gold);border-bottom:1px dashed var(--gold);padding:0 .18em;border-radius:4px;white-space:nowrap;transition:background .15s}',
    '.cp::after{content:" ♪";font-size:.78em;opacity:.65}',
    '.cp:hover{background:rgba(212,180,100,.13);background:color-mix(in srgb,var(--gold) 14%,transparent)}',
    '.cp.cp-playing{background:rgba(212,180,100,.26);background:color-mix(in srgb,var(--gold) 26%,transparent)}',
    '.cp-btn{cursor:pointer;font:inherit;font-size:.95em;color:var(--gold);background:transparent;border:1px solid var(--gold);border-radius:999px;padding:.32em 1.1em;margin:.3em 0;transition:background .15s}',
    '.cp-btn:hover{background:rgba(212,180,100,.13);background:color-mix(in srgb,var(--gold) 14%,transparent)}',
    '.cp-btn.cp-playing{background:rgba(212,180,100,.26);background:color-mix(in srgb,var(--gold) 26%,transparent)}',
    'svg [data-note],svg [data-chord],svg [data-interval],svg [data-scale]{cursor:pointer}',
    'svg .cp-playing{opacity:.62}'
  ].join('\n');
  const styleEl = document.createElement('style');
  styleEl.textContent = css;
  document.head.appendChild(styleEl);

  window.ChordPlayer = {
    noteToMidi: noteToMidi,
    parseChord: parseChord,
    playNote: playNote,
    playChord: playChord,
    playInterval: playInterval,
    playScale: playScale,
    playProgression: playProgression
  };
})();
