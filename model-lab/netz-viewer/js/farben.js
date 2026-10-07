// SPDX-License-Identifier: Apache-2.0
// SPDX-FileCopyrightText: 2026 Finn Malte Hinrichsen
// Farbskalen als 256er-Tabellen (Textur fuer die Shader, Leinwand fuer die Legende).
// Inferno, Magma, Viridis: Stuetzstellen der matplotlib-Skalen in Zehntelschritten (lineare Naeherung).
// Die beiden divergenten Skalen haben eine dunkle Mitte, damit der Bezugswert auf dunklem Grund verschwindet.
import * as THREE from '../vendor/three/three.module.js';

export const FARBSKALEN = {
  inferno: { titel: 'Inferno', stopps: ['#000004', '#160b39', '#420a68', '#6a176e', '#932667', '#bc3754', '#dd513a', '#f37819', '#fca50a', '#f6d746', '#fcffa4'] },
  magma: { titel: 'Magma', stopps: ['#000004', '#140e36', '#3b0f70', '#641a80', '#8c2981', '#b73779', '#de4968', '#f7705c', '#fe9f6d', '#fecf92', '#fcfdbf'] },
  viridis: { titel: 'Viridis', stopps: ['#440154', '#482878', '#3e4989', '#31688e', '#26828e', '#1f9e89', '#35b779', '#6ece58', '#b5de2b', '#fde725'] },
  eis: { titel: 'Eis', stopps: ['#03051a', '#1a1d4b', '#29397b', '#2a5e9c', '#2f85b0', '#43aabd', '#73cbc9', '#b2e5dc', '#e9f8f3'] },
  berlin: { titel: 'Blau–Orange, dunkle Mitte', divergent: true, stopps: ['#c6e1ff', '#6fa9ea', '#2f68a6', '#1a3250', '#13161d', '#4a2116', '#a0452a', '#e7834e', '#ffd3ad'] },
  licht: { titel: 'Violett–Gold, dunkle Mitte', divergent: true, stopps: ['#efc8ff', '#b77be6', '#7341a8', '#382252', '#121318', '#493915', '#a37a21', '#e4b23a', '#fff1ba'] },
};

/** Standardskala je Groesse: bekannte Namen fest, sonst nach Vorzeichenlage. */
export function standardSkala(groesse) {
  const fest = { skalar_betrag2: 'inferno', energie: 'viridis', takt: 'eis', dehnung: 'berlin', fluss: 'licht' };
  const divergent = bezug(groesse).divergent;
  const f = fest[groesse.name];
  // feste Zuordnung nur, wenn der Skalentyp zu den Manifest-Grenzen passt (z. B. Takt mit beiden Vorzeichen)
  if (f && Boolean(FARBSKALEN[f].divergent) === divergent) return f;
  if (groesse.name === 'fluss' || groesse.name === 'energie') return divergent ? 'licht' : 'viridis';
  return divergent ? 'berlin' : 'magma';
}

function hexZuRgb(h) {
  const n = parseInt(h.slice(1), 16);
  return [(n >> 16) & 255, (n >> 8) & 255, n & 255];
}

export function lutDaten(name, n = 256) {
  const stopps = FARBSKALEN[name].stopps.map(hexZuRgb);
  const aus = new Uint8Array(n * 4);
  for (let i = 0; i < n; i++) {
    const t = (i / (n - 1)) * (stopps.length - 1);
    const j = Math.min(Math.floor(t), stopps.length - 2);
    const f = t - j;
    for (let c = 0; c < 3; c++) aus[4 * i + c] = Math.round(stopps[j][c] * (1 - f) + stopps[j + 1][c] * f);
    aus[4 * i + 3] = 255;
  }
  return aus;
}

const texturen = new Map();
export function lutTextur(name) {
  if (!texturen.has(name)) {
    const t = new THREE.DataTexture(lutDaten(name), 256, 1, THREE.RGBAFormat, THREE.UnsignedByteType);
    t.minFilter = THREE.LinearFilter;
    t.magFilter = THREE.LinearFilter;
    t.wrapS = THREE.ClampToEdgeWrapping;
    t.wrapT = THREE.ClampToEdgeWrapping;
    t.generateMipmaps = false;
    t.needsUpdate = true;
    texturen.set(name, t);
  }
  return texturen.get(name);
}

export function zeichneSkala(leinwand, name) {
  const g = leinwand.getContext('2d');
  const b = leinwand.width;
  const h = leinwand.height;
  const d = lutDaten(name, b);
  const bild = g.createImageData(b, h);
  for (let y = 0; y < h; y++) {
    for (let x = 0; x < b; x++) {
      const o = 4 * (y * b + x);
      bild.data[o] = d[4 * x];
      bild.data[o + 1] = d[4 * x + 1];
      bild.data[o + 2] = d[4 * x + 2];
      bild.data[o + 3] = 255;
    }
  }
  g.putImageData(bild, 0, 0);
}

/**
 * Bezugswert und Spanne einer Groesse aus den festen Manifest-Grenzen.
 * - min < 0 < max: divergent um 0, Spanne = groesserer Betrag.
 * - max <= 0 (z. B. Takt N-1): Bezug max, Staerke waechst nach unten.
 * - sonst: Bezug min, Staerke waechst nach oben.
 */
export function bezug(g) {
  const lo = Number(g.min);
  const hi = Number(g.max);
  if (!Number.isFinite(lo) || !Number.isFinite(hi) || hi <= lo) {
    return { neutral: 0, spanne: 1, divergent: false, fallend: false, ok: false };
  }
  if (lo < 0 && hi > 0) return { neutral: 0, spanne: Math.max(-lo, hi), divergent: true, fallend: false, ok: true };
  if (hi <= 0) return { neutral: hi, spanne: hi - lo, divergent: false, fallend: true, ok: true };
  return { neutral: lo, spanne: hi - lo, divergent: false, fallend: false, ok: true };
}
