// SPDX-License-Identifier: Apache-2.0
// SPDX-FileCopyrightText: 2026 Finn Malte Hinrichsen
// Bausteine der Bedienoberflaeche (DOM). Keine Physik, kein three.js.
import { zahl } from './format.js';
import { FARBSKALEN, zeichneSkala, bezug } from './farben.js';

export function el(tag, eigenschaften = {}, ...kinder) {
  const e = document.createElement(tag);
  for (const [k, v] of Object.entries(eigenschaften)) {
    if (v === undefined || v === null || v === false) continue;
    if (k === 'class') e.className = v;
    else if (k === 'text') e.textContent = v;
    else if (k === 'html') e.innerHTML = v;
    else if (k === 'style') setzeStil(e, v);
    else if (k.startsWith('on')) e.addEventListener(k.slice(2), v);
    else e.setAttribute(k, v === true ? '' : v);
  }
  for (const k of kinder.flat()) if (k !== null && k !== undefined && k !== false) e.append(k);
  return e;
}

/**
 * Stil ueber das CSSOM setzen, nie als style-Attribut: Unter der Richtlinie style-src 'self'
 * blockiert der Browser style-Attribute (auch per setAttribute), CSSOM-Zuweisungen aber nicht.
 */
export function setzeStil(e, text) {
  for (const teil of String(text).split(';')) {
    const i = teil.indexOf(':');
    if (i > 0) e.style.setProperty(teil.slice(0, i).trim(), teil.slice(i + 1).trim());
  }
}

export const SYMBOL = {
  anfang: '<svg viewBox="0 0 16 16"><path d="M3 2h2v12H3zM14 2v12L6 8z"/></svg>',
  zurueck: '<svg viewBox="0 0 16 16"><path d="M3 2h2v12H3zM13 3v10L6.5 8z"/></svg>',
  spielen: '<svg viewBox="0 0 16 16"><path d="M4 2l10 6-10 6z"/></svg>',
  pause: '<svg viewBox="0 0 16 16"><path d="M3.5 2h3v12h-3zM9.5 2h3v12h-3z"/></svg>',
  vor: '<svg viewBox="0 0 16 16"><path d="M11 2h2v12h-2zM3 3v10l6.5-5z"/></svg>',
  ende: '<svg viewBox="0 0 16 16"><path d="M11 2h2v12h-2zM2 2v12l8-6z"/></svg>',
};

export function abschnitt(titel, ...kinder) {
  return el('div', { class: 'abschnitt' }, el('div', { class: 'abschnitt-kopf', text: titel }), ...kinder);
}

function zuRegler(r, v) {
  return r.log ? Math.log10(v) : v;
}
function vonRegler(r, x) {
  return r.log ? 10 ** x : x;
}

/** Schieberegler; r: {titel, min, max, schritt, wert, log, format} */
export function regler(r, beiAenderung) {
  const format = r.format ?? ((v) => zahl(v, 2));
  const ausgabe = el('output', { text: format(r.wert) });
  const min = zuRegler(r, r.min);
  const max = zuRegler(r, r.max);
  const schritt = r.log ? (max - min) / 200 : r.schritt;
  const eingabe = el('input', { type: 'range', min, max, step: schritt, 'aria-label': r.titel });
  eingabe.value = zuRegler(r, r.wert);
  eingabe.addEventListener('input', () => {
    const v = vonRegler(r, Number(eingabe.value));
    ausgabe.textContent = format(v);
    beiAenderung(v);
  });
  const knoten = el('label', { class: 'regler' }, el('span', { class: 'regler-name', text: r.titel }), eingabe, ausgabe);
  knoten.setzen = (v) => {
    eingabe.value = zuRegler(r, v);
    ausgabe.textContent = format(v);
  };
  return knoten;
}

/** Segmentwahl; optionen: [[wert, text], ...] */
export function wahl(optionen, wert, beiAenderung) {
  const knoepfe = optionen.map(([w, t]) => el('button', { type: 'button', text: t, 'data-wert': w, class: w === wert ? 'an' : '' }));
  const knoten = el('div', { class: 'wahl', role: 'group' }, knoepfe);
  const setzen = (w) => knoepfe.forEach((k) => k.classList.toggle('an', k.dataset.wert === String(w)));
  knoepfe.forEach((k) => k.addEventListener('click', () => {
    setzen(k.dataset.wert);
    beiAenderung(k.dataset.wert);
  }));
  knoten.setzen = setzen;
  return knoten;
}

export function zeile(titel, inhalt) {
  return el('div', { class: 'zeile' }, el('span', { class: 'regler-name', text: titel }), inhalt);
}

export function skalaAuswahl(aktuell, beiAenderung, nurDivergent = null) {
  const s = el('select', { 'aria-label': 'Farbskala' });
  for (const [name, f] of Object.entries(FARBSKALEN)) {
    if (nurDivergent !== null && Boolean(f.divergent) !== nurDivergent) continue;
    const o = el('option', { value: name, text: f.titel });
    if (name === aktuell) o.selected = true;
    s.append(o);
  }
  s.addEventListener('change', () => beiAenderung(s.value));
  return s;
}

export function muster(skala) {
  const c = el('canvas', { class: 'muster', width: 46, height: 7 });
  zeichneSkala(c, skala);
  return c;
}

/** Karte einer Ebene mit Schalter, Farbmuster und Reglern. */
export function ebenenKarte(ebene, { beiSichtbar, beiRegler, beiModus, beiSkala, beiSkalaModus, zusatz = [] }) {
  const kaestchen = el('input', { type: 'checkbox', class: 'kaestchen', 'aria-label': ebene.titel });
  kaestchen.checked = ebene.sichtbar;
  const farbmuster = ebene.skala ? muster(ebene.skala) : null;
  const unter = el('small', { text: ebene.unter });
  const kopf = el('div', { class: 'ebene-kopf' }, kaestchen, el('div', { class: 'ebene-name' }, el('b', { text: ebene.titel }), unter), farbmuster);
  const reglerKnoten = el('div', { class: 'ebene-regler' });
  const karte = el('div', { class: `ebene${ebene.sichtbar ? '' : ' aus'}` }, kopf, reglerKnoten);
  karte.unter = unter;
  kopf.addEventListener('click', (ev) => {
    if (ev.target !== kaestchen) kaestchen.checked = !kaestchen.checked;
    karte.classList.toggle('aus', !kaestchen.checked);
    beiSichtbar(kaestchen.checked);
  });
  for (const z of zusatz) reglerKnoten.append(z);
  for (const r of ebene.regler) reglerKnoten.append(regler(r, (v) => beiRegler(r.schluessel, v)));
  if (ebene.modi) {
    reglerKnoten.append(zeile(ebene.modi.titel, wahl(ebene.modi.wahl, ebene.modi.wert, (m) => beiModus(m))));
  }
  if (ebene.skalaWahl && beiSkalaModus) {
    reglerKnoten.append(zeile('Skala', wahl([['lauf', 'fest (Lauf)'], ['bild', 'je Bild']], ebene.skalaModus, (m) => beiSkalaModus(m))));
  }
  if (ebene.skala) {
    const div = Boolean(FARBSKALEN[ebene.skala]?.divergent);
    reglerKnoten.append(zeile('Farbskala', skalaAuswahl(ebene.skala, (s) => {
      if (farbmuster) zeichneSkala(farbmuster, s);
      beiSkala(s);
    }, div)));
  }
  karte.setzeSichtbar = (an) => {
    kaestchen.checked = an;
    karte.classList.toggle('aus', !an);
  };
  return karte;
}

/** Legende: Farbbalken mit festen Grenzen aus dem Manifest. */
export function legende(groesse, skala, { titel, schwelle = 0, zusatz = '', spanneBild = null }) {
  const b = { ...bezug(groesse) };
  if (spanneBild !== null) b.spanne = spanneBild;
  const c = el('canvas', { width: 256, height: 9 });
  zeichneSkala(c, skala);
  let ticks;
  if (b.divergent) {
    ticks = [[0, -b.spanne], [50, 0], [100, b.spanne]];
  } else if (b.fallend) {
    ticks = [[0, b.neutral], [100, b.neutral - b.spanne]];
  } else {
    ticks = [[0, b.neutral], [50, b.neutral + b.spanne / 2], [100, b.neutral + b.spanne]];
  }
  const tickKnoten = el('div', { class: 'legende-ticks' }, ticks.map(([p, v]) => el('span', { style: `left:${p}%`, text: zahl(v, 2) })));
  const notiz = [];
  if (spanneBild !== null) notiz.push('Skala je Bild, nicht über Bilder vergleichbar');
  if (schwelle > 0) notiz.push(`unter ${Math.round(schwelle * 100)} % der Spanne ausgeblendet`);
  if (!b.ok) notiz.push('min/max fehlen im Manifest');
  if (zusatz) notiz.push(zusatz);
  return el('div', { class: 'legende' },
    el('div', { class: 'legende-kopf' }, el('b', { text: titel }), el('span', { text: groesse.name })),
    c,
    tickKnoten,
    el('div', { class: 'legende-text', text: [groesse.bedeutung, ...notiz].filter(Boolean).join(' · ') }));
}

/** Verlauf einer Diagnosegroesse mit Marke beim aktuellen Bild. */
export function zeichneVerlauf(c, werte, aktuell) {
  const dpr = window.devicePixelRatio || 1;
  const b = c.clientWidth || 250;
  const h = c.clientHeight || 26;
  if (c.width !== Math.round(b * dpr)) {
    c.width = Math.round(b * dpr);
    c.height = Math.round(h * dpr);
  }
  const g = c.getContext('2d');
  g.setTransform(dpr, 0, 0, dpr, 0, 0);
  g.clearRect(0, 0, b, h);
  const endlich = werte.filter(Number.isFinite);
  if (endlich.length < 2) return;
  let lo = Math.min(...endlich);
  let hi = Math.max(...endlich);
  if (hi - lo < 1e-300) {
    lo -= 1;
    hi += 1;
  }
  const x = (i) => 2 + (i / (werte.length - 1)) * (b - 4);
  const y = (v) => h - 3 - ((v - lo) / (hi - lo)) * (h - 6);
  g.strokeStyle = 'rgba(150,172,206,0.18)';
  g.beginPath();
  g.moveTo(0, h - 0.5);
  g.lineTo(b, h - 0.5);
  g.stroke();
  g.strokeStyle = '#9fb3cf';
  g.lineWidth = 1;
  g.beginPath();
  werte.forEach((v, i) => (i === 0 ? g.moveTo(x(i), y(v)) : g.lineTo(x(i), y(v))));
  g.stroke();
  if (aktuell >= 0 && aktuell < werte.length && Number.isFinite(werte[aktuell])) {
    g.fillStyle = '#f2b134';
    g.fillRect(x(aktuell) - 0.5, 0, 1, h);
    g.beginPath();
    g.arc(x(aktuell), y(werte[aktuell]), 2.4, 0, 2 * Math.PI);
    g.fill();
  }
}

export function meldung(text, art = 'fehler', dauer = 0) {
  const m = el('div', { class: `meldung ${art}`, text });
  document.getElementById('meldungen').append(m);
  if (dauer > 0) setTimeout(() => m.remove(), dauer);
  return m;
}
