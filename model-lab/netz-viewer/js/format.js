// SPDX-License-Identifier: Apache-2.0
// SPDX-FileCopyrightText: 2026 Finn Malte Hinrichsen
// Zahlen fuer die Oberflaeche: deutsches Komma, echtes Minuszeichen, wissenschaftliche Schreibweise mit Hochzahlen.

const HOCH = { '-': '⁻', 0: '⁰', 1: '¹', 2: '²', 3: '³', 4: '⁴', 5: '⁵', 6: '⁶', 7: '⁷', 8: '⁸', 9: '⁹' };

export function hoch(n) {
  return String(n).split('').map((z) => HOCH[z] ?? z).join('');
}

function deutsch(s) {
  return s.replace('.', ',').replace('-', '−');
}

/** Zahl mit `sig` gueltigen Stellen; sehr kleine und grosse Betraege als m·10^e. */
export function zahl(x, sig = 3) {
  if (x === null || x === undefined || !Number.isFinite(x)) return '–';
  if (x === 0) return '0';
  const a = Math.abs(x);
  if (a >= 1e-3 && a < 1e5) {
    const stellen = Math.min(8, Math.max(0, sig - 1 - Math.floor(Math.log10(a))));
    return deutsch(x.toFixed(stellen));
  }
  let e = Math.floor(Math.log10(a));
  let m = x / 10 ** e;
  if (Math.abs(Number(m.toFixed(sig - 1))) >= 10) {
    m /= 10;
    e += 1;
  }
  return `${deutsch(m.toFixed(sig - 1))}·10${hoch(e)}`;
}

/** Ganze Zahl mit schmalem Leerzeichen als Tausendertrenner. */
export function ganz(n) {
  if (!Number.isFinite(n)) return '–';
  return Math.round(n).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
}

/** Bytes lesbar (MB mit einer Nachkommastelle). */
export function megabyte(bytes) {
  return `${deutsch((bytes / 1048576).toFixed(bytes < 10485760 ? 1 : 0))} MB`;
}

/** ISO-Zeitstempel als 05.10.2026, 17:30 (lokale Zeit des Browsers). */
export function datum(iso) {
  if (!iso) return '';
  const d = new Date(iso);
  if (Number.isNaN(d.getTime())) return String(iso);
  const z = (n) => String(n).padStart(2, '0');
  return `${z(d.getDate())}.${z(d.getMonth() + 1)}.${d.getFullYear()}, ${z(d.getHours())}:${z(d.getMinutes())}`;
}
