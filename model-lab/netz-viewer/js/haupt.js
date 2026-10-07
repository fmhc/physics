// SPDX-License-Identifier: Apache-2.0
// SPDX-FileCopyrightText: 2026 Finn Malte Hinrichsen
// Netz-Ansicht: spielt Datensaetze im Format netz-gpu/1 ab. Rechnet keine Physik.
import * as THREE from '../vendor/three/three.module.js';
import { Ansicht } from './ansicht.js';
import { DateiQuelle, BildSpeicher, findeDatensaetze, pruefeManifest } from './quelle.js';
import { ProbeQuelle } from './probe.js';
import { gemeinsameUniforms, eckTextur, fuelleEckTextur, texturBreite, KantenEbene, SplatEbene, FlussEbene, RahmenEbene, anzeigename } from './ebenen.js';
import { el, SYMBOL, abschnitt, regler, wahl, zeile, ebenenKarte, legende, zeichneVerlauf, meldung } from './oberflaeche.js';
import { zahl, ganz, megabyte, datum } from './format.js';

const P = new URLSearchParams(location.search);
if (P.has('foto')) document.documentElement.classList.add('foto');
// Kinomodus (?ui=0): nur das Bild, ohne Tafeln (fuer Vorschaubilder)
const OHNE_UI = P.get('ui') === '0';
if (OHNE_UI) document.documentElement.classList.add('ohne-ui');
const VORLADEN = 4;

const zustand = {
  bild: 0,
  spielt: false,
  tempo: 8,
  schleife: true,
  laedt: false,
  anfrage: 0,
  letzterSchritt: 0,
  ueber: 1,
  verschAn: true,
  schnitt: { modus: 'aus', achse: 2, lage: 0, dicke: 1 },
  uploadMs: null,
  zeichnungen: 0,
  zeichnungenProS: 0,
  bildwechsel: 0,
  bildwechselProS: 0,
};

let ansicht;
let speicher;
let manifest;
let gemeinsam;
let ebenen = [];
let netzEbene = null;
let groessenNachName = new Map();
let verschG = null;
let N = 0;
let ortAnzahl = {};
const ui = {};
const gewarnt = new Set();

// ---------------------------------------------------------------- Start
async function start() {
  const ladeText = document.getElementById('laden-text');
  let quelle;
  try {
    if (P.has('probe')) {
      const n = Math.max(3, Math.min(64, parseInt(P.get('n') ?? '12', 10) || 12));
      const bilder = Math.max(2, Math.min(480, parseInt(P.get('bilder') ?? '48', 10) || 48));
      ladeText.textContent = `Probe-Netz ${n}³ wird erzeugt …`;
      await new Promise((r) => setTimeout(r, 20));
      quelle = new ProbeQuelle({ n, bilder });
    } else if (P.has('d')) {
      quelle = new DateiQuelle(P.get('d'));
    } else {
      // Feste Startseite (oeffentliche Fassung): <meta name="netz-start" content="./">
      const fest = document.querySelector('meta[name="netz-start"]');
      if (fest) {
        location.replace(fest.getAttribute('content') || './');
        return;
      }
      await startseite();
      return;
    }
    manifest = await quelle.manifest();
    const pruefung = pruefeManifest(manifest);
    for (const h of pruefung.hinweise) meldung(h, 'hinweis', 12000);
    if (pruefung.fehler.length) throw new Error(`Manifest unbrauchbar: ${pruefung.fehler.join('; ')}`);

    const groessen = manifest.groessen ?? [];
    groessenNachName = new Map(groessen.map((g) => [g.name, g]));
    const komp = (g) => g.komponenten ?? 1;
    const eckSkalare = groessen.filter((g) => g.ort === 'ecke' && komp(g) === 1);
    const kantenSkalare = groessen.filter((g) => g.ort === 'kante' && komp(g) === 1);
    const dreieckSkalare = groessen.filter((g) => g.ort === 'dreieck' && komp(g) === 1);
    const rahmenG = groessen.find((g) => g.ort === 'ecke' && komp(g) === 4);
    verschG = groessen.find((g) => g.ort === 'ecke' && komp(g) === 3 && g.name === 'verschiebung') ?? groessen.find((g) => g.ort === 'ecke' && komp(g) === 3) ?? null;

    ladeText.textContent = 'Netz wird geladen …';
    const netz = await quelle.netz({ mitDreiecken: dreieckSkalare.length > 0 });
    N = manifest.netz.N_ecken;
    pruefeNetz(netz);
    ortAnzahl = { ecke: N, kante: netz.kanten ? netz.kanten.length / 2 : 0, dreieck: netz.dreiecke ? netz.dreiecke.length / 3 : 0 };

    await document.fonts.load('500 44px "IBM Plex Mono"').catch(() => null);
    ansicht = new Ansicht(document.getElementById('buehne'), { hdr: P.get('hdr') !== '0', versatz: !OHNE_UI });
    const zoom = Number(P.get('zoom'));
    if (zoom > 0) ansicht.zoom = Math.min(8, zoom);
    const belichtung = Number(P.get('belichtung'));
    if (belichtung > 0) ansicht.renderer.toneMappingExposure = belichtung;
    const { box, ursprung, periodisch } = boxBestimmen(netz.ecken);
    const kantenLaenge = mittlereKante(netz, box, periodisch);
    ansicht.setzeBox(box, ursprung);

    gemeinsam = gemeinsameUniforms();
    gemeinsam.uLage.value = eckTextur(N, netz.ecken, 3);
    gemeinsam.uVersch.value = eckTextur(N);
    gemeinsam.uTexBreite.value = texturBreite(N);
    gemeinsam.uBox.value.set(...box);
    gemeinsam.uUrsprung.value.copy(ursprung);
    const defines = periodisch ? { PERIODISCH: '' } : {};

    // Ebenen
    if (netz.kanten) {
      netzEbene = new KantenEbene({ kanten: netz.kanten, gemeinsam, defines, kantenGroessen: kantenSkalare });
      ebenen.push(netzEbene);
    } else {
      meldung('netz/kanten.u32 fehlt: Netz und Dehnung werden nicht gezeigt', 'hinweis', 10000);
    }
    for (const g of eckSkalare) ebenen.push(new SplatEbene({ groesse: g, anzahl: N, gemeinsam, defines, kantenLaenge }));
    if (netz.dreiecke && dreieckSkalare.length) {
      const da = new THREE.InstancedBufferAttribute(zuFloat(netz.dreiecke), 3);
      for (const g of dreieckSkalare) ebenen.push(new FlussEbene({ groesse: g, dreieckAttr: da, gemeinsam, defines, kantenLaenge }));
    }
    if (rahmenG) ebenen.push(new RahmenEbene({ groesse: rahmenG, anzahl: N, gemeinsam, defines, kantenLaenge }));
    for (const e of ebenen) ansicht.szene.add(e.objekt);

    anfangsSichtbarkeit(eckSkalare);
    anfangsEinstellungen();
    speicher = new BildSpeicher(quelle);
    speicher.beiAenderung = () => { ui.pufferBedarf = true; };

    baueOberflaeche(quelle);
    ansicht.blick(P.get('blick') ?? 'schraeg');
    ansicht.setzeSchnittAnzeige(zustand.schnitt);
    setzeSchnitt(zustand.schnitt);
    tastatur();

    const startBild = Math.max(0, Math.min(manifest.frames.length - 1, parseInt(P.get('bild') ?? '0', 10) || 0));
    await zeigeBild(startBild);
    document.getElementById('laden').classList.add('fertig');
    if (P.get('spielen') === '1') setzeSpielen(true);
    ansicht.renderer.setAnimationLoop(schleife);
    webgpuPruefen();
    if (P.has('mess')) messen(Number(P.get('mess')) || 6);
  } catch (f) {
    document.getElementById('laden').classList.add('fertig');
    meldung(f.message ?? String(f), 'fehler');
    throw f;
  }
}

function zuFloat(arr) {
  const f = new Float32Array(arr.length);
  for (let i = 0; i < arr.length; i++) f[i] = arr[i];
  return f;
}

function pruefeNetz(netz) {
  const m = manifest.netz;
  if (netz.ecken.length !== 3 * N) throw new Error(`ecken.f32 hat ${ganz(netz.ecken.length)} Werte, erwartet 3 × N_ecken = ${ganz(3 * N)}`);
  const pruefe = (arr, k, soll, name) => {
    if (!arr) return;
    if (Number.isFinite(soll) && arr.length !== k * soll) throw new Error(`${name} hat ${ganz(arr.length)} Werte, erwartet ${k} × ${ganz(soll)}`);
    let max = 0;
    for (let i = 0; i < arr.length; i++) if (arr[i] > max) max = arr[i];
    if (max >= N) throw new Error(`${name}: Eckindex ${max} ≥ N_ecken ${N}`);
  };
  pruefe(netz.kanten, 2, m.N_kanten, 'kanten.u32');
  pruefe(netz.dreiecke, 3, m.N_dreiecke, 'dreiecke.u32');
}

function boxBestimmen(ecken) {
  const lo = [Infinity, Infinity, Infinity];
  const hi = [-Infinity, -Infinity, -Infinity];
  for (let i = 0; i < ecken.length; i += 3) {
    for (let c = 0; c < 3; c++) {
      const v = ecken[i + c];
      if (v < lo[c]) lo[c] = v;
      if (v > hi[c]) hi[c] = v;
    }
  }
  const periodisch = Boolean(manifest.netz.periodisch);
  let box = Array.isArray(manifest.netz.box) && manifest.netz.box.length === 3 ? manifest.netz.box.map(Number) : null;
  if (!box || box.some((b) => !(b > 0))) box = hi.map((h, c) => Math.max(h - lo[c], 1e-6));
  const eps = 1e-4 * Math.max(...box);
  const inNull = lo.every((l, c) => l >= -eps && hi[c] <= box[c] + eps);
  const ursprung = new THREE.Vector3(...(inNull ? [0, 0, 0] : lo));
  return { box, ursprung, periodisch };
}

function mittlereKante(netz, box, periodisch) {
  const k = netz.kanten;
  const e = netz.ecken;
  if (!k || k.length === 0) return Math.cbrt((box[0] * box[1] * box[2]) / Math.max(N, 1));
  const schritt = Math.max(1, Math.floor(k.length / 2 / 20000));
  let summe = 0;
  let zahlK = 0;
  for (let i = 0; i < k.length / 2; i += schritt) {
    const a = k[2 * i];
    const b = k[2 * i + 1];
    let q = 0;
    for (let c = 0; c < 3; c++) {
      let d = e[3 * b + c] - e[3 * a + c];
      if (periodisch) d -= box[c] * Math.round(d / box[c]);
      q += d * d;
    }
    summe += Math.sqrt(q);
    zahlK += 1;
  }
  return summe / zahlK;
}

function anfangsSichtbarkeit(eckSkalare) {
  const liste = P.get('ebenen');
  if (liste !== null) {
    const namen = liste.split(',').map((s) => s.trim()).filter(Boolean);
    for (const e of ebenen) e.setzeSichtbar(e === netzEbene ? namen.includes('netz') : namen.includes(e.groesse.name));
    return;
  }
  const ersterSkalar = eckSkalare.find((g) => g.name === 'skalar_betrag2') ?? eckSkalare[0];
  for (const e of ebenen) {
    e.setzeSichtbar(Boolean(e === netzEbene || (ersterSkalar && e.groesse === ersterSkalar)));
  }
}

function anfangsEinstellungen() {
  const d = P.get('darstellung');
  if (d === 'kugel' || d === 'splat') for (const e of ebenen) if (e instanceof SplatEbene) e.setzeModus(d);
  const f = P.get('fluss');
  if (f === 'punkte' || f === 'flaechen') for (const e of ebenen) if (e instanceof FlussEbene) e.setzeModus(f);
  if (P.get('netz') === 'deckend' && netzEbene) netzEbene.setzeModus('deckend');
  if (P.get('skala') === 'bild') for (const e of ebenen) if (e.skalaWahl) e.skalaModus = 'bild';
  const ra = Number(P.get('rahmenanteil'));
  if (ra > 0) for (const e of ebenen) if (e instanceof RahmenEbene) e.setze('anteil', Math.min(1, ra));
  const u = Number(P.get('ueber'));
  if (Number.isFinite(u) && P.has('ueber')) zustand.ueber = Math.max(0, u);
  const t = Number(P.get('tempo'));
  if (t > 0) zustand.tempo = t;
  const s = P.get('schnitt');
  if (s) {
    const [modus, achse, lage, dicke] = s.split(',');
    const a = { x: 0, y: 1, z: 2 }[achse] ?? 2;
    zustand.schnitt = {
      modus: ['scheibe', 'unter', 'ueber'].includes(modus) ? modus : 'aus',
      achse: a,
      lage: Number.isFinite(Number(lage)) ? Number(lage) : ansicht.box[a] / 2,
      dicke: Number(dicke) > 0 ? Number(dicke) : 1.5,
    };
  } else {
    zustand.schnitt.lage = ansicht.box[2] / 2;
    zustand.schnitt.dicke = Math.max(1, ansicht.box[2] / 8);
  }
}

// ---------------------------------------------------------------- Bilder
function irgendwasSichtbar() {
  return ebenen.some((e) => e.sichtbar);
}

function benoetigt() {
  const namen = new Set();
  for (const e of ebenen) for (const n of e.benoetigt()) namen.add(n);
  if (verschG && zustand.verschAn && zustand.ueber > 0 && irgendwasSichtbar()) namen.add(verschG.name);
  return [...namen];
}

function anwenden(name, arr, i) {
  const g = groessenNachName.get(name);
  const soll = (ortAnzahl[g.ort] ?? 0) * (g.komponenten ?? 1);
  if (arr.length !== soll) {
    const s = `${name}:${arr.length}`;
    if (!gewarnt.has(s)) {
      gewarnt.add(s);
      meldung(`${name} in Bild ${i}: ${ganz(arr.length)} Werte statt ${ganz(soll)}; nicht angezeigt`, 'fehler', 10000);
    }
    return;
  }
  for (const e of ebenen) {
    if (e.sichtbar && e.groesse && e.groesse.name === name && e.bildNr !== i) {
      e.setzeWerte(name, arr);
      e.bildNr = i;
      e.letzteWerte = arr;
      if (e.skalaModus === 'bild') {
        e.skalaAnpassen();
        ui.legendenBedarf = true;
      }
    }
  }
  if (verschG && name === verschG.name && ui.verschBild !== i) {
    fuelleEckTextur(gemeinsam.uVersch.value, arr, N, 3);
    ui.verschBild = i;
  }
}

async function zeigeBild(i) {
  const nr = ++zustand.anfrage;
  zustand.laedt = true;
  const namen = benoetigt();
  try {
    const daten = await Promise.all(namen.map((n) => speicher.hole(i, n).then((a) => [n, a])));
    if (nr !== zustand.anfrage) return false;
    const t0 = performance.now();
    for (const [n, a] of daten) anwenden(n, a, i);
    const ms = performance.now() - t0;
    zustand.uploadMs = zustand.uploadMs === null ? ms : 0.8 * zustand.uploadMs + 0.2 * ms;
    if (zustand.bild !== i) zustand.bildwechsel += 1;
    zustand.bild = i;
    gemeinsam.uUeber.value = verschG && zustand.verschAn ? zustand.ueber : 0;
    aktualisiereZeit();
    ansicht.bedarf = true;
    vorladen(i);
    return true;
  } catch (f) {
    if (nr === zustand.anfrage) {
      meldung(`Bild ${i + 1}: ${f.message ?? f}`, 'fehler', 8000);
      setzeSpielen(false);
    }
    return false;
  } finally {
    if (nr === zustand.anfrage) zustand.laedt = false;
  }
}

function vorladen(i) {
  const namen = benoetigt();
  const B = manifest.frames.length;
  for (let k = 1; k <= VORLADEN; k++) {
    let j = i + k;
    if (j >= B) {
      if (!zustand.schleife) break;
      j %= B;
    }
    for (const n of namen) speicher.hole(j, n).catch(() => {});
  }
}

function schritt(d) {
  const B = manifest.frames.length;
  let j = zustand.bild + d;
  if (j >= B) j = zustand.schleife ? 0 : B - 1;
  if (j < 0) j = zustand.schleife ? B - 1 : 0;
  zeigeBild(j);
}

function setzeSpielen(an) {
  zustand.spielt = an;
  if (ui.spielKnopf) {
    ui.spielKnopf.innerHTML = an ? SYMBOL.pause : SYMBOL.spielen;
    ui.spielKnopf.setAttribute('aria-label', an ? 'Pause' : 'Abspielen');
  }
}

// ---------------------------------------------------------------- Schleife
function schleife(jetzt) {
  if (ansicht.steuerung.update()) ansicht.bedarf = true;
  if (zustand.spielt && !zustand.laedt && jetzt - zustand.letzterSchritt >= 1000 / zustand.tempo) {
    zustand.letzterSchritt = jetzt;
    const B = manifest.frames.length;
    if (zustand.bild + 1 >= B && !zustand.schleife) setzeSpielen(false);
    else schritt(1);
  }
  if (ansicht.bedarf || zustand.dauer) {
    ansicht.bedarf = false;
    ansicht.zeichne(gemeinsam);
    zustand.zeichnungen += 1;
  }
  ansicht.gpu.abholen();
  if (ui.pufferBedarf) {
    ui.pufferBedarf = false;
    zeichnePuffer();
  }
  if (!ui.letzteLeistung || jetzt - ui.letzteLeistung > 500) {
    const dt = ui.letzteLeistung ? (jetzt - ui.letzteLeistung) / 1000 : 1;
    zustand.zeichnungenProS = zustand.zeichnungen / dt;
    zustand.bildwechselProS = zustand.bildwechsel / dt;
    zustand.zeichnungen = 0;
    zustand.bildwechsel = 0;
    ui.letzteLeistung = jetzt;
    aktualisiereLeistung();
  }
  if (ui.legendenBedarf && (!ui.letzteLegende || jetzt - ui.letzteLegende > 250)) {
    ui.legendenBedarf = false;
    ui.letzteLegende = jetzt;
    baueLegenden();
  }
}

// ---------------------------------------------------------------- Schnitt
function setzeSchnitt(s) {
  zustand.schnitt = s;
  const a = s.modus === 'aus' ? -1 : s.achse;
  gemeinsam.uSchnitt.value.set(a, s.lage, s.dicke, s.modus === 'unter' ? 1 : s.modus === 'ueber' ? 2 : 0);
  // additive Ebenen: in einer duennen Scheibe liegen weniger Splats auf dem Sichtstrahl, maessig aufhellen
  gemeinsam.uHellFaktor.value = s.modus === 'scheibe' ? Math.min(4, Math.max(1, Math.sqrt(ansicht.box[s.achse] / Math.max(s.dicke, 1e-3)))) : 1;
  ansicht.setzeSchnittAnzeige(s);
  ansicht.bedarf = true;
}

// ---------------------------------------------------------------- Oberflaeche
function baueOberflaeche(quelle) {
  const m = manifest;
  document.getElementById('titel').textContent = m.titel ?? 'ohne Titel';
  document.title = `${m.titel ?? 'Netz'} · Netz-Ansicht`;
  const erzeugt = m.erzeugt ? `erzeugt ${datum(m.erzeugt)}` : '';
  document.getElementById('erzeugt').textContent = [erzeugt, quelle.art === 'probe' ? 'Probe-Modus' : ''].filter(Boolean).join(' · ');

  // ---------- links: Ebenen
  const links = document.getElementById('ebenen');
  const karten = [];
  for (const e of ebenen) {
    const zusatz = [];
    if (e === netzEbene && e.kantenGroessen.length) {
      const s = el('select', { 'aria-label': 'Farbe des Netzes' },
        e.kantenGroessen.map((g) => el('option', { value: g.name, text: anzeigename(g.name) })),
        el('option', { value: '', text: 'einfarbig' }));
      s.addEventListener('change', () => {
        const g = groessenNachName.get(s.value) ?? null;
        e.setzeFarbGroesse(g);
        karte.unter.textContent = g ? `Kanten · Farbe ${g.name}` : 'Kanten · einfarbig';
        nachladen();
      });
      zusatz.push(zeile('Farbe nach', s));
    }
    const karte = ebenenKarte(e, {
      beiSichtbar: (an) => {
        e.setzeSichtbar(an);
        nachladen();
      },
      beiRegler: (k, v) => {
        e.setze(k, v);
        ansicht.bedarf = true;
        if (k === 'uSchwelle') baueLegenden();
      },
      beiModus: (mo) => {
        e.setzeModus(mo);
        ansicht.bedarf = true;
      },
      beiSkala: (sk) => {
        e.setzeSkala(sk);
        ansicht.bedarf = true;
        baueLegenden();
      },
      beiSkalaModus: (mo) => {
        e.skalaModus = mo;
        e.skalaAnpassen();
        ansicht.bedarf = true;
        baueLegenden();
      },
      zusatz,
    });
    karten.push(karte);
  }
  links.append(abschnitt('Ebenen', karten));

  if (verschG) {
    const kaest = el('input', { type: 'checkbox', class: 'kaestchen' });
    kaest.checked = zustand.verschAn;
    kaest.addEventListener('change', () => {
      zustand.verschAn = kaest.checked;
      gemeinsam.uUeber.value = zustand.verschAn ? zustand.ueber : 0;
      nachladen();
    });
    links.append(abschnitt('Verschiebung',
      el('label', { class: 'schalter-klein' }, kaest, el('span', { text: `${verschG.name} anzeigen` })),
      el('div', { style: 'height:6px' }),
      regler({ titel: 'Überhöhung', min: 0.1, max: 50, wert: zustand.ueber, log: true, format: (v) => `× ${zahl(v, 2)}` }, (v) => {
        zustand.ueber = v;
        gemeinsam.uUeber.value = zustand.verschAn ? v : 0;
        nachladen();
      }),
      el('div', { class: 'legende-text', style: 'margin:4px 0 6px', text: `${verschG.bedeutung ?? ''} · zusätzlich zum Faktor im Datensatz` })));
  }

  // Schnitt
  const s = zustand.schnitt;
  const lageRegler = regler({ titel: 'Lage', min: 0, max: ansicht.box[s.achse], schritt: 0.01, wert: s.lage }, (v) => setzeSchnitt({ ...zustand.schnitt, lage: v }));
  const dickeRegler = regler({ titel: 'Dicke', min: 0.1, max: Math.max(...ansicht.box), schritt: 0.01, wert: s.dicke }, (v) => setzeSchnitt({ ...zustand.schnitt, dicke: v }));
  links.append(abschnitt('Schnitt',
    el('div', { class: 'ebene-regler', style: 'margin-left:0' },
      zeile('Modus', wahl([['aus', 'aus'], ['scheibe', 'Scheibe'], ['unter', 'unter'], ['ueber', 'über']], s.modus, (mo) => setzeSchnitt({ ...zustand.schnitt, modus: mo }))),
      zeile('Achse', wahl([['0', 'x'], ['1', 'y'], ['2', 'z']], String(s.achse), (a) => setzeSchnitt({ ...zustand.schnitt, achse: Number(a) }))),
      lageRegler,
      dickeRegler)));

  // Ansicht
  const boxKaest = el('input', { type: 'checkbox', class: 'kaestchen' });
  boxKaest.checked = true;
  boxKaest.addEventListener('change', () => {
    ansicht.boxGruppe.visible = boxKaest.checked;
    ansicht.bedarf = true;
  });
  links.append(abschnitt('Ansicht',
    el('div', { class: 'ebene-regler', style: 'margin-left:0' },
      el('div', { class: 'knopf-reihe' }, [['schraeg', 'schräg'], ['vorn', 'von vorn (xz)'], ['oben', 'von oben (xy)'], ['seite', 'von der Seite (yz)']].map(([w, t]) =>
        el('button', { class: 'knopf', type: 'button', text: t, onclick: () => ansicht.blick(w) }))),
      el('label', { class: 'schalter-klein', style: 'margin-top:4px' }, boxKaest, el('span', { text: 'Box und Achsen' })),
      regler({ titel: 'Tiefenschleier', min: 0, max: 0.95, schritt: 0.01, wert: gemeinsam.uSchleier.value }, (v) => {
        gemeinsam.uSchleier.value = v;
        ansicht.bedarf = true;
      }),
      ansicht.hdr
        ? regler({ titel: 'Belichtung', min: 0.05, max: 4, wert: ansicht.renderer.toneMappingExposure, log: true, format: (v) => `× ${zahl(v, 2)}` }, (v) => {
          ansicht.renderer.toneMappingExposure = v;
          ansicht.bedarf = true;
        })
        : null)));

  // ---------- rechts: Infofeld
  const r = document.getElementById('rechts');
  ui.zeit = el('div', { class: 'zeit-gross' });
  ui.bildnr = el('span', { class: 'bildnr' });
  const n = m.netz;
  const tabelle = el('dl', { class: 'tabelle' });
  const eintrag = (k, v) => tabelle.append(el('dt', { text: k }), el('dd', { text: v }));
  eintrag('Netz', [n.typ, Array.isArray(n.zellen) ? `${n.zellen.join('×')} Zellen` : null].filter(Boolean).join(' · '));
  const anz = (v) => (Number.isFinite(v) ? ganz(v) : '–');
  eintrag('Ecken', `${ganz(N)} · Kanten ${anz(n.N_kanten)}`);
  eintrag('Dreiecke', `${anz(n.N_dreiecke)} · Tetr. ${anz(n.N_tetraeder)}`);
  eintrag('Box', `${ansicht.box.map((b) => zahl(b, 3)).join(' × ')} ${einheitKurz('laenge')} · ${n.periodisch ? 'periodisch' : 'offen'}`);
  eintrag('Bilder', `${ganz(m.frames.length)}${m.frames.length > 1 ? ` · Δ ${zahl(zeitVon(1) - zeitVon(0), 3)}` : ''}`);
  if (m.einheiten?.zeit) eintrag('Achse', m.einheiten.zeit);
  if (typeof m.hinweis_bilder === 'string' && m.hinweis_bilder) eintrag('Hinweis', m.hinweis_bilder);
  r.append(abschnitt('Lauf', el('div', { class: 'zeit-zeile' }, ui.zeit, ui.bildnr), tabelle));

  // Diagnose
  const diag = m.diagnose && typeof m.diagnose === 'object' ? Object.entries(m.diagnose) : [];
  ui.diagnose = [];
  if (diag.length) {
    const kinder = [];
    for (const [name, werte] of diag) {
      const reihe = Array.isArray(werte) ? werte.map(Number) : [Number(werte)];
      const wert = el('span', { class: 'diagnose-wert' });
      const c = el('canvas');
      const endlich = reihe.filter(Number.isFinite);
      let spanne = '';
      if (endlich.length > 1) {
        const lo = Math.min(...endlich);
        const hi = Math.max(...endlich);
        const mittel = endlich.reduce((a, b) => a + b, 0) / endlich.length;
        spanne = `Spanne ${zahl(hi - lo, 2)}${Math.abs(mittel) > 0 ? ` · relativ ${zahl((hi - lo) / Math.abs(mittel), 2)}` : ''}`;
      }
      const block = el('div', { class: 'diagnose' }, el('span', { class: 'diagnose-name', text: name }), wert, reihe.length > 1 ? c : null, spanne ? el('span', { class: 'diagnose-spanne', text: spanne }) : null);
      if (kinder.length >= 5) block.hidden = true;
      kinder.push(block);
      ui.diagnose.push({ reihe, wert, c, jeBild: reihe.length === m.frames.length });
    }
    if (diag.length > 5) {
      const mehr = el('button', { class: 'knopf', type: 'button', text: `alle ${diag.length} Reihen zeigen` });
      mehr.addEventListener('click', () => {
        for (const b of kinder) b.hidden = false;
        mehr.remove();
        aktualisiereZeit();
      });
      kinder.push(mehr);
    }
    r.append(abschnitt('Diagnose', kinder));
  }

  ui.legenden = el('div');
  r.append(abschnitt('Legende', ui.legenden));
  ui.leistung = el('div', { class: 'leistung' });
  r.append(abschnitt('Leistung', ui.leistung));
  const q = m.quelle ?? {};
  r.append(abschnitt('Quelle', el('div', { class: 'quelle' },
    [q.code && `Code: ${q.code}`, q.herkunft && `Herkunft: ${q.herkunft}`, q.lauf && `Lauf: ${q.lauf}`, q.hinweis && `Hinweis: ${q.hinweis}`]
      .filter(Boolean).map((t) => el('div', { text: t })))));

  baueZeitleiste();
  baueLegenden();
}

function einheitKurz(art) {
  const e = manifest.einheiten?.[art] ?? '';
  return e.split(' ')[0] || '';
}

/** Beschriftung der Bildachse: meist Zeit t; manche Laeufe tragen einen Parameter (z. B. Drehwinkel in Grad). */
function zeitAchse() {
  const e = manifest.einheiten?.zeit ?? '';
  if (/winkel/i.test(e)) return { name: 'Winkel', einheit: /grad/i.test(e) ? '°' : '' };
  return { name: 't', einheit: einheitKurz('zeit') };
}

function zeitVon(i) {
  const f = manifest.frames[i];
  return Number(f?.zeit ?? i);
}

function baueZeitleiste() {
  const z = document.getElementById('zeitleiste');
  const B = manifest.frames.length;
  const knopf = (sym, titel, fn, klasse = '') => el('button', { type: 'button', class: klasse, title: titel, 'aria-label': titel, html: sym, onclick: fn });
  ui.spielKnopf = knopf(SYMBOL.spielen, 'Abspielen', () => setzeSpielen(!zustand.spielt), 'spielen');
  const transport = el('div', { class: 'transport' },
    knopf(SYMBOL.anfang, 'Erstes Bild (Pos1)', () => zeigeBild(0)),
    knopf(SYMBOL.zurueck, 'Bild zurück (←)', () => schritt(-1)),
    ui.spielKnopf,
    knopf(SYMBOL.vor, 'Bild vor (→)', () => schritt(1)),
    knopf(SYMBOL.ende, 'Letztes Bild (Ende)', () => zeigeBild(B - 1)));
  ui.spur = el('input', { type: 'range', min: 0, max: Math.max(0, B - 1), step: 1, 'aria-label': 'Bild' });
  ui.spur.value = zustand.bild;
  ui.spur.addEventListener('input', () => zeigeBild(Number(ui.spur.value)));
  ui.puffer = el('canvas', { class: 'spur-puffer' });
  const za = zeitAchse();
  const marken = el('div', { class: 'spur-marken' }, el('span', { text: `${za.name} = ${zahl(zeitVon(0), 3)}` }), el('span', { text: `${ganz(B)} Bilder` }), el('span', { text: `${za.name} = ${zahl(zeitVon(B - 1), 3)}` }));
  const spur = el('div', { class: 'spur' }, ui.spur, ui.puffer, marken);
  ui.zeitKlein = el('div', { class: 'zeit-gross' });
  const anzeige = el('div', { class: 'zeitanzeige' }, ui.zeitKlein);
  const tempo = el('select', { 'aria-label': 'Tempo' }, [1, 2, 4, 8, 12, 24, 30, 60].map((t) => el('option', { value: t, text: `${t} Bilder/s` })));
  tempo.value = String([1, 2, 4, 8, 12, 24, 30, 60].reduce((a, b) => (Math.abs(b - zustand.tempo) < Math.abs(a - zustand.tempo) ? b : a)));
  zustand.tempo = Number(tempo.value);
  tempo.addEventListener('change', () => { zustand.tempo = Number(tempo.value); });
  const schl = el('input', { type: 'checkbox', class: 'kaestchen' });
  schl.checked = zustand.schleife;
  schl.addEventListener('change', () => { zustand.schleife = schl.checked; });
  ui.tafelKnopf = el('button', { type: 'button', class: 'knopf tafel-knopf', text: 'Tafeln', title: 'Seitentafeln ein/aus (T)', 'aria-pressed': 'true', onclick: () => tafelnUmschalten() });
  if (window.innerWidth < 820) tafelnUmschalten(false);
  z.append(transport, spur, anzeige,
    el('label', { class: 'tempo' }, el('span', { text: 'Tempo' }), tempo),
    el('label', { class: 'schalter-klein' }, schl, el('span', { text: 'Schleife' })),
    ui.tafelKnopf);
  aktualisiereZeit();
}

function tafelnUmschalten(an) {
  const sichtbar = an ?? document.body.classList.contains('tafeln-aus');
  document.body.classList.toggle('tafeln-aus', !sichtbar);
  if (ui.tafelKnopf) ui.tafelKnopf.setAttribute('aria-pressed', String(sichtbar));
  if (ansicht) ansicht.bedarf = true;
}

function zeichnePuffer() {
  const c = ui.puffer;
  if (!c) return;
  const B = manifest.frames.length;
  const b = c.clientWidth || 600;
  if (c.width !== b) {
    c.width = b;
    c.height = 3;
  }
  const g = c.getContext('2d');
  g.clearRect(0, 0, b, 3);
  const namen = benoetigt();
  if (!namen.length) return;
  const voll = speicher.geladeneBilder(namen);
  g.fillStyle = 'rgba(159,179,207,0.45)';
  for (const i of voll) {
    const x0 = B > 1 ? (i / (B - 1)) * (b - 1) : 0;
    g.fillRect(Math.round(x0) - 1, 0, Math.max(2, Math.ceil(b / B) - 1), 3);
  }
}

function aktualisiereZeit() {
  if (!ui.zeit) return;
  const B = manifest.frames.length;
  const t = zeitVon(zustand.bild);
  const za = zeitAchse();
  const kopf = za.name === 't' ? 't = ' : '';
  const vorsatz = () => (za.name === 't' ? null : el('small', { class: 'zeit-name', text: za.name }));
  ui.zeit.innerHTML = '';
  ui.zeit.append(...[vorsatz(), `${kopf}${zahl(t, 4)}`, el('small', { text: za.einheit })].filter(Boolean));
  ui.zeitKlein.innerHTML = '';
  ui.zeitKlein.append(...[vorsatz(), `${kopf}${zahl(t, 4)}`, el('small', { text: za.einheit })].filter(Boolean));
  const idx = manifest.frames[zustand.bild]?.index;
  ui.bildnr.textContent = `Bild ${zustand.bild + 1} / ${B}${Number.isFinite(idx) && idx !== zustand.bild ? ` · Schritt ${idx}` : ''}`;
  ui.spur.value = zustand.bild;
  for (const d of ui.diagnose) {
    const i = d.jeBild ? zustand.bild : d.reihe.length - 1;
    d.wert.textContent = zahl(d.reihe[i], 6);
    if (d.reihe.length > 1) zeichneVerlauf(d.c, d.reihe, d.jeBild ? zustand.bild : -1);
  }
  ui.pufferBedarf = true;
}

function baueLegenden() {
  if (!ui.legenden) return;
  ui.legenden.innerHTML = '';
  for (const e of ebenen) {
    if (!e.sichtbar) continue;
    if (e instanceof RahmenEbene) {
      ui.legenden.append(el('div', { class: 'legende' },
        el('div', { class: 'legende-kopf' }, el('b', { text: e.titel }), el('span', { text: e.groesse.name })),
        el('div', { class: 'legende-text achsfarben', html: '<i class="achse-x"></i>x <i class="achse-y"></i>y <i class="achse-z"></i>z des gedrehten Rahmens · hell = großer Drehwinkel (bis π), gedämpft = nahe Ruhelage' })));
      continue;
    }
    if (!e.groesse) {
      ui.legenden.append(el('div', { class: 'legende' }, el('div', { class: 'legende-kopf' }, el('b', { text: 'Netz' }), el('span', { text: 'einfarbig' }))));
      continue;
    }
    const schwelle = e.uniforms?.uSchwelle?.value ?? 0;
    const zusatz = e === netzEbene ? 'Grundnetz grau' : '';
    ui.legenden.append(legende(e.groesse, e.skala, { titel: e === netzEbene ? `Netz · ${anzeigename(e.groesse.name)}` : e.titel, schwelle, zusatz, spanneBild: e.spanneBild }));
  }
  if (!ui.legenden.children.length) ui.legenden.append(el('div', { class: 'legende-text', text: 'keine Ebene sichtbar' }));
}

function aktualisiereLeistung() {
  if (!ui.leistung || !ansicht) return;
  const gpu = ansicht.gpu.ms;
  const zeilen = [
    ['Zeichnen', `${gpu !== null ? `GPU ${zahl(gpu, 3)} ms · ` : ''}CPU ${zahl(ansicht.cpuMs ?? NaN, 2)} ms`],
    ['Hochladen', zustand.uploadMs !== null ? `${zahl(zustand.uploadMs, 2)} ms je Bild` : '–'],
    ['Takt', `${zahl(zustand.zeichnungenProS, 3)} Zeichnungen/s · ${zahl(zustand.bildwechselProS, 3)} Bilder/s`],
    ['Speicher', `${speicher.anzahlBilder()} Bilder · ${megabyte(speicher.bytes)}`],
    ['Renderer', `three.js r${THREE.REVISION} · WebGL2${ansicht.hdr ? ' · HalfFloat-Puffer, Tonwert Neutral' : ' · 8-Bit-Puffer'}`],
    ['GPU', ansicht.rendererName()],
    ['WebGPU', ui.webgpu ?? 'wird geprüft …'],
  ];
  ui.leistung.innerHTML = '';
  for (const [k, v] of zeilen) ui.leistung.append(el('div', {}, el('b', { text: `${k} ` }), v));
  if (ui.messung) ui.leistung.append(ui.messung);
}

async function webgpuPruefen() {
  try {
    if (!navigator.gpu) {
      ui.webgpu = 'im Browser nicht angeboten';
      return;
    }
    const adapter = await navigator.gpu.requestAdapter();
    if (!adapter) {
      ui.webgpu = 'angeboten, aber kein Adapter';
      return;
    }
    const info = adapter.info ?? {};
    ui.webgpu = `verfügbar (${[info.vendor, info.architecture].filter(Boolean).join(', ') || 'Adapter ohne Angaben'})`;
  } catch (f) {
    ui.webgpu = `Fehler: ${f.message ?? f}`;
  }
}

function nachladen() {
  baueLegenden();
  gemeinsam.uUeber.value = verschG && zustand.verschAn ? zustand.ueber : 0;
  ansicht.bedarf = true;
  zeigeBild(zustand.bild);
}

function tastatur() {
  window.addEventListener('keydown', (ev) => {
    if (ev.target instanceof HTMLInputElement && ev.target.type !== 'checkbox') return;
    if (ev.target instanceof HTMLSelectElement) return;
    const B = manifest.frames.length;
    if (ev.code === 'Space') {
      ev.preventDefault();
      setzeSpielen(!zustand.spielt);
    } else if (ev.key === 'ArrowRight') {
      ev.preventDefault();
      schritt(1);
    } else if (ev.key === 'ArrowLeft') {
      ev.preventDefault();
      schritt(-1);
    } else if (ev.key === 'Home') {
      zeigeBild(0);
    } else if (ev.key === 'End') {
      zeigeBild(B - 1);
    } else if (ev.key === 'r' || ev.key === 'R') {
      ansicht.blick('schraeg');
    } else if (ev.key === 't' || ev.key === 'T') {
      tafelnUmschalten();
    }
  });
}

// ---------------------------------------------------------------- Messmodus (?mess=Sekunden)
async function messen(sekunden) {
  const B = manifest.frames.length;
  ui.messung = el('div', { style: 'margin-top:6px;color:#ffd27a', text: `Messung läuft (${sekunden} s) …` });
  // Erst alle Bilder der sichtbaren Groessen laden (bis zum Speicherbudget), dann nur Upload + Zeichnen messen.
  const namen = benoetigt();
  const vorab = Math.min(B, 24);
  await Promise.all(Array.from({ length: vorab }, (_, i) => Promise.all(namen.map((n) => speicher.hole(i, n)))));
  const gpuWerte = [];
  const cpuWerte = [];
  const upWerte = [];
  const ext = ansicht.gpu.ext;
  const gl = ansicht.gl;
  const t0 = performance.now();
  let k = 0;
  while (performance.now() - t0 < sekunden * 1000) {
    const i = k % vorab;
    const daten = await Promise.all(namen.map((n) => speicher.hole(i, n).then((a) => [n, a])));
    const u0 = performance.now();
    for (const [n, a] of daten) anwenden(n, a, i);
    zustand.bild = i;
    let q = null;
    if (ext) {
      q = gl.createQuery();
      gl.beginQuery(ext.TIME_ELAPSED_EXT, q);
    }
    const c0 = performance.now();
    ansicht.renderer.render(ansicht.szene, ansicht.kamera);
    if (ext) gl.endQuery(ext.TIME_ELAPSED_EXT);
    gl.finish();
    const c1 = performance.now();
    upWerte.push(c0 - u0);
    cpuWerte.push(c1 - c0);
    if (q) gpuWerte.push(q);
    k += 1;
    await new Promise((r) => requestAnimationFrame(r));
  }
  const dauer = (performance.now() - t0) / 1000;
  await new Promise((r) => setTimeout(r, 200));
  const gpuMs = [];
  for (const q of gpuWerte) {
    if (gl.getQueryParameter(q, gl.QUERY_RESULT_AVAILABLE) && !gl.getParameter(ext.GPU_DISJOINT_EXT)) gpuMs.push(gl.getQueryParameter(q, gl.QUERY_RESULT) / 1e6);
    gl.deleteQuery(q);
  }
  const median = (a) => {
    if (!a.length) return NaN;
    const s = [...a].sort((x, y) => x - y);
    return s[Math.floor(s.length / 2)];
  };
  const ergebnis = {
    bilder: k,
    sekunden: Number(dauer.toFixed(2)),
    bilderProSekunde: Number((k / dauer).toFixed(1)),
    uploadMsMedian: Number(median(upWerte).toFixed(3)),
    zeichnenMitFinishMsMedian: Number(median(cpuWerte).toFixed(3)),
    gpuMsMedian: gpuMs.length ? Number(median(gpuMs).toFixed(3)) : null,
    groessen: namen,
    ecken: N,
    kanten: ortAnzahl.kante,
    dreiecke: ortAnzahl.dreieck,
    renderer: ansicht.rendererName(),
    hdr: ansicht.hdr,
    sichererKontext: window.isSecureContext,
    webgpu: ui.webgpu ?? 'Prüfung nicht abgeschlossen',
  };
  ui.messung.textContent = `Messung: ${k} Bilder in ${zahl(dauer, 3)} s (${zahl(k / dauer, 3)} Bilder/s), Upload ${zahl(ergebnis.uploadMsMedian, 3)} ms, Zeichnen+finish ${zahl(ergebnis.zeichnenMitFinishMsMedian, 3)} ms, GPU ${ergebnis.gpuMsMedian ?? '–'} ms (Mediane)`;
  document.body.dataset.messung = JSON.stringify(ergebnis);
  const pre = el('pre', { id: 'messung', style: 'display:none', text: JSON.stringify(ergebnis) });
  document.body.append(pre);
  document.title = `MESSUNG ${JSON.stringify(ergebnis)}`;
  aktualisiereLeistung();
  ansicht.bedarf = true;
  // Ergebnis als Anfrage an den eigenen Testserver: steht dann im Serverlog (Messlauf ohne virtuelle Zeit).
  if (P.get('melden') === '1') fetch(`../messung-ergebnis?${new URLSearchParams({ e: JSON.stringify(ergebnis) })}`).catch(() => null);
}

// ---------------------------------------------------------------- Startseite ohne Datensatz
async function startseite() {
  document.body.classList.add('ohne-daten');
  document.getElementById('laden').classList.add('fertig');
  const liste = await findeDatensaetze();
  const basis = location.pathname;
  const tafel = el('div', { class: 'start-tafel tafel' },
    document.querySelector('#kopf .marke')?.cloneNode(true) ?? el('div', { class: 'marke' }, el('span', { text: 'Netz-Ansicht' })),
    el('h2', { text: 'Kein Datensatz gewählt' }),
    el('p', { text: 'Die Ansicht spielt Datensätze des Rechenkerns (Format netz-gpu/1) ab. Sie rechnet selbst keine Physik.' }),
    liste.length
      ? el('ul', {}, liste.map((d) => el('li', {}, el('a', { href: `${basis}?d=${encodeURIComponent(d.manifest)}`, text: d.name }))))
      : el('p', { html: 'Keine Datensätze unter <code>../datensaetze/</code> gefunden. Aufruf mit <code>?d=pfad/zu/manifest.json</code>.' }),
    el('p', {}, 'Ohne Rechenkern prüfen: ',
      el('a', { href: `${basis}?probe=1`, text: 'Probe-Datensatz (12³)' }), ' · ',
      el('a', { href: `${basis}?probe=1&n=37&ebenen=netz,skalar_betrag2`, text: 'Lastprobe (37³: 101 306 Ecken, 709 142 Kanten)' })),
    el('div', { class: 'pflichtvermerk', text: 'synthetische Modellrechnung · keine Messdaten' }));
  document.body.append(el('div', { class: 'start' }, tafel));
}

start();
