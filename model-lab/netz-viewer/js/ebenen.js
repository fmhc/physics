// SPDX-License-Identifier: Apache-2.0
// SPDX-FileCopyrightText: 2026 Finn Malte Hinrichsen
// Darstellungsebenen. Jede Ebene: ein three.js-Objekt, Regler-Beschreibungen fuer die Oberflaeche,
// die Liste der Groessen, die sie je Bild braucht, und setzeWerte() fuer den Upload.
import * as THREE from '../vendor/three/three.module.js';
import { GEMEINSAM, WERT, KANTEN_VS, LINIE_FS, SPLAT_VS, SPLAT_FS, FLUSS_VS, FLUSS_FS, RAHMEN_VS } from './shader.js';
import { lutTextur, bezug, standardSkala } from './farben.js';

export const ANZEIGENAME = {
  skalar_betrag2: 'Materie |φ|²',
  energie: 'Energiedichte',
  takt: 'Takt N − 1',
  dehnung: 'Dehnung δl/l',
  fluss: 'Lichtfluss',
  rahmen: 'Drehrahmen',
  verschiebung: 'Verschiebung',
};
export const anzeigename = (name) => ANZEIGENAME[name] ?? name;

// ---------- Texturen fuer Ecken ----------
export function texturBreite(n) {
  return n > 1024 * 2048 ? 4096 : 1024;
}

function datenTextur(daten, b, h) {
  const t = new THREE.DataTexture(daten, b, h, THREE.RGBAFormat, THREE.FloatType);
  t.minFilter = THREE.NearestFilter;
  t.magFilter = THREE.NearestFilter;
  t.generateMipmaps = false;
  t.needsUpdate = true;
  return t;
}

export function eckTextur(n, quelle = null, komponenten = 3) {
  const b = texturBreite(n);
  const h = Math.max(1, Math.ceil(n / b));
  const d = new Float32Array(b * h * 4);
  const t = datenTextur(d, b, h);
  if (quelle) fuelleEckTextur(t, quelle, n, komponenten);
  return t;
}

export function fuelleEckTextur(t, quelle, n, komponenten = 3) {
  const d = t.image.data;
  for (let i = 0; i < n; i++) {
    for (let c = 0; c < komponenten; c++) d[4 * i + c] = quelle[komponenten * i + c];
  }
  t.needsUpdate = true;
}

export function gemeinsameUniforms() {
  return {
    uLage: { value: null },
    uVersch: { value: null },
    uUeber: { value: 0 },
    uTexBreite: { value: 1024 },
    uBox: { value: new THREE.Vector3(1, 1, 1) },
    uUrsprung: { value: new THREE.Vector3() },
    uSchnitt: { value: new THREE.Vector4(-1, 0, 1, 0) },
    uSchleier: { value: 0.55 },
    uSchleierBereich: { value: new THREE.Vector2(0, 1) },
    uHellFaktor: { value: 1 },
  };
}

function wertUniforms(groesse, skala) {
  const b = bezug(groesse);
  return {
    uLut: { value: lutTextur(skala) },
    uNeutral: { value: b.neutral },
    uSpanne: { value: b.spanne },
    uDivergent: { value: b.divergent ? 1 : 0 },
    uSchwelle: { value: 0 },
  };
}

function zuFloat(arr) {
  const f = new Float32Array(arr.length);
  for (let i = 0; i < arr.length; i++) f[i] = arr[i];
  return f;
}

class Basis {
  constructor() {
    this.sichtbar = false;
    this.regler = [];
    this.modi = null;
    this.skala = null;
    this.groesse = null;
    this.bildNr = -1;
    // Skala: 'lauf' = feste Manifest-Grenzen (Standard, ueber Bilder vergleichbar), 'bild' = groesster Betrag im Bild
    this.skalaWahl = false;
    this.skalaModus = 'lauf';
    this.spanneBild = null;
    this.letzteWerte = null;
  }
  setzeSichtbar(an) {
    this.sichtbar = an;
    this.objekt.visible = an;
  }
  setze(schluessel, wert) {
    const r = this.regler.find((x) => x.schluessel === schluessel);
    if (r) r.wert = wert;
    if (this.uniforms[schluessel]) this.uniforms[schluessel].value = wert;
  }
  setzeSkala(name) {
    this.skala = name;
    this.uniforms.uLut.value = lutTextur(name);
  }
  /** Spanne nach Skalenmodus setzen; bei 'bild' aus den zuletzt angewandten Werten. */
  skalaAnpassen() {
    if (!this.groesse || !this.uniforms || !this.uniforms.uSpanne) return;
    const b = bezug(this.groesse);
    this.spanneBild = null;
    if (this.skalaModus === 'bild' && this.letzteWerte) {
      let m = 0;
      const a = this.letzteWerte;
      for (let i = 0; i < a.length; i++) {
        const d = Math.abs(a[i] - b.neutral);
        if (d > m) m = d;
      }
      this.spanneBild = m > 0 ? m : b.spanne;
    }
    const s = this.spanneBild ?? b.spanne;
    this.uniforms.uSpanne.value = s;
    if (this.punkte) this.punkte.uniforms.uSpanne.value = s;
  }
  benoetigt() {
    return this.sichtbar && this.groesse ? [this.groesse.name] : [];
  }
}

// ---------- Netz als Linien ----------
export class KantenEbene extends Basis {
  constructor({ kanten, gemeinsam, defines, kantenGroessen }) {
    super();
    const n = kanten.length / 2;
    this.id = 'netz';
    this.titel = 'Netz';
    this.anzahl = n;
    this.kantenGroessen = kantenGroessen;
    this.groesse = kantenGroessen[0] ?? null;
    this.skala = this.groesse ? standardSkala(this.groesse) : 'berlin';
    this.unter = this.groesse ? `Kanten · Farbe ${this.groesse.name}` : 'Kanten';

    const g = new THREE.InstancedBufferGeometry();
    g.setAttribute('position', new THREE.Float32BufferAttribute([0, 0, 0, 1, 0, 0, 2, 0, 0, 3, 0, 0], 3));
    g.setAttribute('aKante', new THREE.InstancedBufferAttribute(zuFloat(kanten), 2));
    this.wert = new THREE.InstancedBufferAttribute(new Float32Array(n), 1);
    this.wert.setUsage(THREE.DynamicDrawUsage);
    g.setAttribute('aWert', this.wert);
    g.instanceCount = n;

    // sichtbare Linienlaenge je Bildpunkt waechst etwa wie N_k^(2/3): Grundhelligkeit entsprechend daempfen
    const grund = Math.min(0.3, Math.max(0.006, 0.18 * Math.pow(24000 / Math.max(n, 1), 2 / 3)));
    this.uniforms = {
      ...gemeinsam,
      ...wertUniforms(this.groesse ?? { min: -1, max: 1 }, this.skala),
      uMitWert: { value: 0 },
      uGrund: { value: grund },
      uGrundFarbe: { value: new THREE.Vector3(0.44, 0.53, 0.66) },
      uGamma: { value: 0.6 },
    };
    this.material = new THREE.ShaderMaterial({
      uniforms: this.uniforms,
      vertexShader: GEMEINSAM + WERT + KANTEN_VS,
      fragmentShader: LINIE_FS,
      defines,
      transparent: true,
      depthWrite: false,
      blending: THREE.AdditiveBlending,
    });
    this.objekt = new THREE.LineSegments(g, this.material);
    this.objekt.frustumCulled = false;
    this.objekt.renderOrder = 1;

    this.regler = [
      { schluessel: 'uGrund', titel: 'Grundnetz', min: 0.002, max: 1, schritt: 0.001, wert: grund, log: true },
      { schluessel: 'uSchwelle', titel: 'Schwelle', min: 0, max: 0.95, schritt: 0.01, wert: 0 },
      { schluessel: 'uGamma', titel: 'Kontrast', min: 0.2, max: 2, schritt: 0.05, wert: 0.6, format: (v) => `γ ${v.toFixed(2).replace('.', ',')}` },
    ];
    this.modi = { titel: 'Darstellung', wahl: [['leuchtend', 'leuchtend'], ['deckend', 'deckend']], wert: 'leuchtend' };
    this.skalaWahl = true;
  }
  setzeModus(m) {
    this.modi.wert = m;
    const deckend = m === 'deckend';
    this.material.transparent = !deckend;
    this.material.depthWrite = deckend;
    this.material.blending = deckend ? THREE.NormalBlending : THREE.AdditiveBlending;
    this.material.needsUpdate = true;
  }
  setzeFarbGroesse(groesse) {
    this.groesse = groesse;
    this.uniforms.uMitWert.value = 0;
    this.bildNr = -1;
    if (!groesse) return;
    const b = bezug(groesse);
    this.uniforms.uNeutral.value = b.neutral;
    this.uniforms.uSpanne.value = b.spanne;
    this.uniforms.uDivergent.value = b.divergent ? 1 : 0;
  }
  setzeWerte(name, arr) {
    this.wert.array.set(arr);
    this.wert.needsUpdate = true;
    this.uniforms.uMitWert.value = 1;
  }
}

// ---------- Gauss-Splats (Ecken oder Dreiecksmitten) ----------
const SPLAT_VORGABEN = {
  skalar_betrag2: { hell: 0.95, schwelle: 0.02, gamma: 0.9 },
  energie: { hell: 0.55, schwelle: 0.06, gamma: 1.0 },
  takt: { hell: 0.4, schwelle: 0.12, gamma: 1.4 },
};

export class SplatEbene extends Basis {
  constructor({ groesse, anzahl, gemeinsam, defines, kantenLaenge, dreieckAttr = null, wertAttr = null, id = null }) {
    super();
    this.id = id ?? `splat-${groesse.name}`;
    this.groesse = groesse;
    this.titel = anzeigename(groesse.name);
    this.unter = groesse.name + (dreieckAttr ? ' · Dreiecksmitten' : ' · Ecken');
    this.skala = standardSkala(groesse);
    this.anzahl = anzahl;
    const v = SPLAT_VORGABEN[groesse.name] ?? { hell: 0.6, schwelle: 0.05, gamma: 1.0 };

    const g = new THREE.InstancedBufferGeometry();
    g.setAttribute('position', new THREE.Float32BufferAttribute([-1, -1, 0, 1, -1, 0, 1, 1, 0, -1, 1, 0], 3));
    g.setIndex([0, 1, 2, 0, 2, 3]);
    this.wert = wertAttr ?? new THREE.InstancedBufferAttribute(new Float32Array(anzahl), 1);
    this.wert.setUsage(THREE.DynamicDrawUsage);
    g.setAttribute('aWert', this.wert);
    if (dreieckAttr) g.setAttribute('aDreieck', dreieckAttr);
    g.instanceCount = anzahl;
    this.geteilt = Boolean(wertAttr);

    const radius = (dreieckAttr ? 0.55 : 0.95) * kantenLaenge;
    // additive Splats summieren sich entlang des Sichtstrahls (~ Kubikwurzel der Anzahl): Vorgabe danach daempfen
    const dichte = Math.min(1, Math.max(0.12, 15 / Math.cbrt(Math.max(anzahl, 1))));
    this.uniforms = {
      ...gemeinsam,
      ...wertUniforms(groesse, this.skala),
      uRadius: { value: radius },
      uMinAnteil: { value: 0.35 },
      uHell: { value: (dreieckAttr ? 0.5 : v.hell) * dichte },
      uGamma: { value: v.gamma },
      uModus: { value: 0 },
    };
    this.uniforms.uSchwelle.value = dreieckAttr ? 0.25 : v.schwelle;
    this.material = new THREE.ShaderMaterial({
      uniforms: this.uniforms,
      vertexShader: GEMEINSAM + WERT + SPLAT_VS,
      fragmentShader: SPLAT_FS,
      defines: dreieckAttr ? { ...defines, ORT_DREIECK: '' } : defines,
      transparent: true,
      depthWrite: false,
      blending: THREE.AdditiveBlending,
    });
    this.objekt = new THREE.Mesh(g, this.material);
    this.objekt.frustumCulled = false;
    this.objekt.renderOrder = 3;

    this.regler = [
      { schluessel: 'uRadius', titel: 'Größe', min: 0.05 * kantenLaenge, max: 4 * kantenLaenge, schritt: 0.01 * kantenLaenge, wert: radius, log: true },
      { schluessel: 'uHell', titel: 'Helligkeit', min: 0.02, max: 4, schritt: 0.01, wert: this.uniforms.uHell.value, log: true },
      { schluessel: 'uSchwelle', titel: 'Schwelle', min: 0, max: 0.95, schritt: 0.01, wert: this.uniforms.uSchwelle.value },
    ];
    this.modi = { titel: 'Darstellung', wahl: [['splat', 'Splat'], ['kugel', 'Kugel']], wert: 'splat' };
    this.skalaWahl = true;
  }
  setzeModus(m) {
    this.modi.wert = m;
    const kugel = m === 'kugel';
    this.uniforms.uModus.value = kugel ? 1 : 0;
    this.material.transparent = !kugel;
    this.material.depthWrite = kugel;
    this.material.blending = kugel ? THREE.NormalBlending : THREE.AdditiveBlending;
    this.material.needsUpdate = true;
  }
  setzeWerte(name, arr) {
    this.wert.array.set(arr);
    this.wert.needsUpdate = true;
  }
}

// ---------- Fluss: leuchtende Dreiecke oder Splats in den Dreiecksmitten (ein Werte-Puffer fuer beide) ----------
export class FlussEbene extends Basis {
  constructor({ groesse, dreieckAttr, gemeinsam, defines, kantenLaenge }) {
    super();
    this.id = `fluss-${groesse.name}`;
    this.groesse = groesse;
    this.titel = anzeigename(groesse.name);
    this.unter = `${groesse.name} · Dreiecke`;
    this.skala = standardSkala(groesse);
    const anzahl = dreieckAttr.count;
    this.wert = new THREE.InstancedBufferAttribute(new Float32Array(anzahl), 1);
    this.wert.setUsage(THREE.DynamicDrawUsage);

    const g = new THREE.InstancedBufferGeometry();
    g.setAttribute('position', new THREE.Float32BufferAttribute([0, 0, 0, 1, 0, 0, 2, 0, 0], 3));
    g.setAttribute('aDreieck', dreieckAttr);
    g.setAttribute('aWert', this.wert);
    g.instanceCount = anzahl;

    this.uniforms = {
      ...gemeinsam,
      ...wertUniforms(groesse, this.skala),
      uHell: { value: 0.3 },
      uGamma: { value: 1.2 },
      uSchrumpf: { value: 0.86 },
      uKante: { value: 0.9 },
    };
    this.uniforms.uSchwelle.value = 0.3;
    this.material = new THREE.ShaderMaterial({
      uniforms: this.uniforms,
      vertexShader: GEMEINSAM + WERT + FLUSS_VS,
      fragmentShader: FLUSS_FS,
      defines,
      transparent: true,
      depthWrite: false,
      side: THREE.DoubleSide,
      blending: THREE.AdditiveBlending,
    });
    this.flaechen = new THREE.Mesh(g, this.material);
    this.flaechen.frustumCulled = false;
    this.flaechen.renderOrder = 2;

    this.punkte = new SplatEbene({ groesse, anzahl, gemeinsam, defines, kantenLaenge, dreieckAttr, wertAttr: this.wert, id: `${this.id}-punkte` });
    this.punkte.uniforms.uHell.value = 0.3;
    this.punkte.uniforms.uSchwelle.value = 0.3;
    this.punkte.objekt.visible = false;

    this.objekt = new THREE.Group();
    this.objekt.add(this.flaechen, this.punkte.objekt);

    this.regler = [
      { schluessel: 'uHell', titel: 'Helligkeit', min: 0.01, max: 3, schritt: 0.01, wert: 0.3, log: true },
      { schluessel: 'uSchwelle', titel: 'Schwelle', min: 0, max: 0.95, schritt: 0.01, wert: 0.3 },
      { schluessel: 'uSchrumpf', titel: 'Flächengröße', min: 0.2, max: 1, schritt: 0.01, wert: 0.86 },
      { schluessel: 'uRadius', titel: 'Punktgröße', min: 0.05 * kantenLaenge, max: 3 * kantenLaenge, schritt: 0.01 * kantenLaenge, wert: this.punkte.uniforms.uRadius.value, log: true },
    ];
    this.modi = { titel: 'Darstellung', wahl: [['flaechen', 'Flächen'], ['punkte', 'Punkte']], wert: 'flaechen' };
    this.skalaWahl = true;
  }
  setze(schluessel, wert) {
    const r = this.regler.find((x) => x.schluessel === schluessel);
    if (r) r.wert = wert;
    if (this.uniforms[schluessel]) this.uniforms[schluessel].value = wert;
    if (this.punkte.uniforms[schluessel]) this.punkte.uniforms[schluessel].value = wert;
  }
  setzeModus(m) {
    this.modi.wert = m;
    this.flaechen.visible = m !== 'punkte';
    this.punkte.objekt.visible = m === 'punkte';
  }
  setzeSkala(name) {
    super.setzeSkala(name);
    this.punkte.setzeSkala(name);
  }
  setzeWerte(name, arr) {
    this.wert.array.set(arr);
    this.wert.needsUpdate = true;
  }
}

// ---------- Drehrahmen als Achsenkreuze, ausgeduennt per Hash ----------
export class RahmenEbene extends Basis {
  constructor({ groesse, anzahl, gemeinsam, defines, kantenLaenge }) {
    super();
    this.id = `rahmen-${groesse.name}`;
    this.groesse = groesse;
    this.titel = anzeigename(groesse.name);
    this.unter = `${groesse.name} · Quaternion je Ecke`;
    this.anzahl = anzahl;
    this.anteil = anzahl > 20000 ? 0.15 : anzahl > 5000 ? 0.4 : 1;

    const g = new THREE.InstancedBufferGeometry();
    g.setAttribute('position', new THREE.Float32BufferAttribute([0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 2, 0, 0, 2, 1, 0], 3));
    this.idx = new THREE.InstancedBufferAttribute(new Float32Array(anzahl), 1);
    this.quat = new THREE.InstancedBufferAttribute(new Float32Array(anzahl * 4), 4);
    this.quat.setUsage(THREE.DynamicDrawUsage);
    g.setAttribute('aIdx', this.idx);
    g.setAttribute('aQuat', this.quat);
    this.geometrie = g;
    this.auswahl = new Uint32Array(anzahl);
    this.letzte = null;

    const laenge = 0.6 * kantenLaenge;
    this.uniforms = { ...gemeinsam, uLaenge: { value: laenge }, uGrund: { value: 0.3 } };
    this.material = new THREE.ShaderMaterial({
      uniforms: this.uniforms,
      vertexShader: GEMEINSAM + RAHMEN_VS,
      fragmentShader: LINIE_FS,
      defines,
    });
    this.objekt = new THREE.LineSegments(g, this.material);
    this.objekt.frustumCulled = false;
    this.waehle(this.anteil);

    this.regler = [
      { schluessel: 'anteil', titel: 'Anteil Ecken', min: 0.01, max: 1, schritt: 0.01, wert: this.anteil, format: (v) => `${Math.round(v * 100)} %` },
      { schluessel: 'uLaenge', titel: 'Länge', min: 0.05 * kantenLaenge, max: 1.5 * kantenLaenge, schritt: 0.01 * kantenLaenge, wert: laenge },
      { schluessel: 'uGrund', titel: 'Ruhe-Helligk.', min: 0, max: 1, schritt: 0.01, wert: 0.3 },
    ];
  }
  waehle(anteil) {
    this.anteil = anteil;
    let m = 0;
    const grenze = anteil * 4294967296;
    for (let i = 0; i < this.anzahl; i++) {
      const h = Math.imul(i + 0x9e3779b9, 0x85ebca6b) >>> 0;
      const h2 = Math.imul(h ^ (h >>> 13), 0xc2b2ae35) >>> 0;
      if ((h2 ^ (h2 >>> 16)) >>> 0 < grenze || anteil >= 1) {
        this.auswahl[m] = i;
        this.idx.array[m] = i;
        m += 1;
      }
    }
    this.m = m;
    this.idx.needsUpdate = true;
    this.geometrie.instanceCount = m;
    if (this.letzte) this.setzeWerte(null, this.letzte);
  }
  setze(schluessel, wert) {
    if (schluessel === 'anteil') {
      this.regler[0].wert = wert;
      this.waehle(wert);
      return;
    }
    super.setze(schluessel, wert);
  }
  setzeWerte(name, arr) {
    this.letzte = arr;
    const q = this.quat.array;
    for (let k = 0; k < this.m; k++) {
      const i = this.auswahl[k];
      q[4 * k] = arr[4 * i];
      q[4 * k + 1] = arr[4 * i + 1];
      q[4 * k + 2] = arr[4 * i + 2];
      q[4 * k + 3] = arr[4 * i + 3];
    }
    this.quat.needsUpdate = true;
  }
}
