// SPDX-License-Identifier: Apache-2.0
// SPDX-FileCopyrightText: 2026 Finn Malte Hinrichsen
// Renderer, Kamera, Orbit-Steuerung, Hintergrund, Box-Rahmen, Schnittanzeige, GPU-Zeitmessung.
import * as THREE from '../vendor/three/three.module.js';
import { OrbitControls } from '../vendor/three/OrbitControls.js';

// Farben werden so ausgegeben, wie sie in den Tabellen stehen (keine Umrechnung linear/sRGB).
THREE.ColorManagement.enabled = false;

function hintergrund() {
  const b = 1280;
  const h = 800;
  const c = document.createElement('canvas');
  c.width = b;
  c.height = h;
  const g = c.getContext('2d');
  const r = g.createRadialGradient(b * 0.52, h * 0.44, 30, b * 0.5, h * 0.5, b * 0.72);
  r.addColorStop(0, '#0f1a2b');
  r.addColorStop(0.5, '#08101b');
  r.addColorStop(1, '#020409');
  g.fillStyle = r;
  g.fillRect(0, 0, b, h);
  const bild = g.getImageData(0, 0, b, h);
  const d = bild.data;
  for (let i = 0; i < d.length; i += 4) {
    const z = (Math.random() - 0.5) * 6;
    d[i] += z;
    d[i + 1] += z;
    d[i + 2] += z * 1.2;
  }
  g.putImageData(bild, 0, 0);
  const t = new THREE.CanvasTexture(c);
  t.colorSpace = THREE.NoColorSpace;
  return t;
}

class GpuZeit {
  constructor(gl) {
    this.gl = gl;
    this.ext = gl.getExtension('EXT_disjoint_timer_query_webgl2');
    this.offen = [];
    this.aktiv = null;
    this.ms = null;
  }
  beginn() {
    if (!this.ext || this.offen.length > 3) return;
    this.aktiv = this.gl.createQuery();
    this.gl.beginQuery(this.ext.TIME_ELAPSED_EXT, this.aktiv);
  }
  ende() {
    if (!this.aktiv) return;
    this.gl.endQuery(this.ext.TIME_ELAPSED_EXT);
    this.offen.push(this.aktiv);
    this.aktiv = null;
  }
  abholen() {
    const gl = this.gl;
    while (this.offen.length) {
      const q = this.offen[0];
      if (!gl.getQueryParameter(q, gl.QUERY_RESULT_AVAILABLE)) break;
      const getrennt = gl.getParameter(this.ext.GPU_DISJOINT_EXT);
      const ns = gl.getQueryParameter(q, gl.QUERY_RESULT);
      if (!getrennt) this.ms = this.ms === null ? ns / 1e6 : 0.85 * this.ms + 0.15 * (ns / 1e6);
      gl.deleteQuery(q);
      this.offen.shift();
    }
  }
}

function textSprite(text, farbe, hoehe) {
  const c = document.createElement('canvas');
  const g = c.getContext('2d');
  const px = 44;
  g.font = `500 ${px}px "IBM Plex Mono", monospace`;
  const breite = Math.ceil(g.measureText(text).width) + 16;
  c.width = breite;
  c.height = px + 16;
  g.font = `500 ${px}px "IBM Plex Mono", monospace`;
  g.fillStyle = farbe;
  g.textBaseline = 'middle';
  g.fillText(text, 8, c.height / 2 + 2);
  const t = new THREE.CanvasTexture(c);
  t.colorSpace = THREE.NoColorSpace;
  t.minFilter = THREE.LinearFilter;
  const s = new THREE.Sprite(new THREE.SpriteMaterial({ map: t, transparent: true, depthTest: false, depthWrite: false }));
  s.scale.set((hoehe * c.width) / c.height, hoehe, 1);
  s.renderOrder = 10;
  return s;
}

/** Kann die GPU in Float- bzw. HalfFloat-Puffer zeichnen? (Voraussetzung fuer den HDR-Puffer) */
function hdrMoeglich() {
  const c = document.createElement('canvas');
  const gl = c.getContext('webgl2');
  if (!gl) return false;
  const ok = Boolean(gl.getExtension('EXT_color_buffer_float') || gl.getExtension('EXT_color_buffer_half_float'));
  const verlust = gl.getExtension('WEBGL_lose_context');
  if (verlust) verlust.loseContext();
  return ok;
}

export class Ansicht {
  constructor(behaelter, { hdr = true, versatz = true } = {}) {
    // HDR: Szene in einen HalfFloat-Puffer (r186: outputBufferType), additives Licht darf ueber 1 steigen,
    // erst der Ausgabe-Durchgang begrenzt weich (Khronos PBR Neutral: unter 0,76 unveraendert).
    this.hdr = false;
    this.versatz = versatz;
    if (hdr && hdrMoeglich()) {
      try {
        this.renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: 'high-performance', outputBufferType: THREE.HalfFloatType });
        this.renderer.toneMapping = THREE.NeutralToneMapping;
        this.hdr = true;
      } catch (f) {
        this.renderer = null;
      }
    }
    if (!this.renderer) this.renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: 'high-performance' });
    this.renderer.outputColorSpace = THREE.LinearSRGBColorSpace;
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    behaelter.append(this.renderer.domElement);
    this.gl = this.renderer.getContext();
    this.szene = new THREE.Scene();
    this.szene.background = hintergrund();
    this.kamera = new THREE.PerspectiveCamera(34, 1, 0.01, 1000);
    this.kamera.up.set(0, 0, 1);
    this.steuerung = new OrbitControls(this.kamera, this.renderer.domElement);
    this.steuerung.enableDamping = true;
    this.steuerung.dampingFactor = 0.14;
    this.steuerung.addEventListener('change', () => { this.bedarf = true; });
    this.gpu = new GpuZeit(this.gl);
    this.mitte = new THREE.Vector3();
    this.radius = 1;
    this.bedarf = true;
    this.cpuMs = null;
    window.addEventListener('resize', () => this.groesse());
    this.groesse();
  }

  rendererName() {
    if (this._rendererName) return this._rendererName;
    const gl = this.gl;
    let name = gl.getParameter(gl.RENDERER);
    if (!name || /^(webkit|mozilla)/i.test(name)) {
      const ext = gl.getExtension('WEBGL_debug_renderer_info');
      if (ext) name = gl.getParameter(ext.UNMASKED_RENDERER_WEBGL) || name;
    }
    this._rendererName = name || 'unbekannt';
    return this._rendererName;
  }

  groesse() {
    const b = window.innerWidth;
    const h = window.innerHeight;
    this.renderer.setSize(b, h);
    // Bildmitte um die halbe Hoehe der Zeitleiste nach oben ruecken (nicht im Kinomodus)
    const dy = this.versatz ? Math.round(Math.min(48, h * 0.06)) : 0;
    this.kamera.aspect = b / (h + 2 * dy);
    this.kamera.setViewOffset(b, h + 2 * dy, 0, 2 * dy, b, h);
    this.kamera.updateProjectionMatrix();
    this.bedarf = true;
  }

  setzeBox(box, ursprung) {
    this.box = box;
    this.ursprung = ursprung;
    this.mitte.set(ursprung.x + box[0] / 2, ursprung.y + box[1] / 2, ursprung.z + box[2] / 2);
    this.radius = 0.5 * Math.hypot(box[0], box[1], box[2]);
    if (this.boxGruppe) this.szene.remove(this.boxGruppe);
    this.boxGruppe = this.baueBox(box, ursprung);
    this.szene.add(this.boxGruppe);
    this.schnittGruppe = new THREE.Group();
    this.szene.add(this.schnittGruppe);
  }

  baueBox(box, o) {
    const gruppe = new THREE.Group();
    const [bx, by, bz] = box;
    const P = (i, j, k) => [o.x + i * bx, o.y + j * by, o.z + k * bz];
    const kanten = [
      [0, 1, 0, 1, 1, 0], [0, 0, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1],
      [1, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 1], [1, 0, 1, 1, 1, 1],
      [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 1, 1], [1, 1, 0, 1, 1, 1],
    ];
    const p = [];
    for (const k of kanten) p.push(...P(k[0], k[1], k[2]), ...P(k[3], k[4], k[5]));
    // Teilstriche an den drei Achsen durch den Ursprung
    const groesst = Math.max(bx, by, bz);
    const schritt = [1, 2, 5, 10, 20, 50, 100].find((s) => groesst / s <= 12) ?? 100;
    const tl = 0.014 * groesst;
    for (let a = 0; a < 3; a++) {
      for (let v = schritt; v < box[a] - 1e-9; v += schritt) {
        const q = [o.x, o.y, o.z];
        q[a] += v;
        const q2 = q.slice();
        q2[(a + 1) % 3] -= tl;
        const q3 = q.slice();
        q3[(a + 2) % 3] -= tl;
        p.push(...q, ...q2, ...q, ...q3);
      }
    }
    const g = new THREE.BufferGeometry();
    g.setAttribute('position', new THREE.Float32BufferAttribute(p, 3));
    gruppe.add(new THREE.LineSegments(g, new THREE.LineBasicMaterial({ color: 0x3f4d61 })));
    // Achsen
    const farben = [0xe0675c, 0x63c47e, 0x5d95e6];
    const namen = ['x', 'y', 'z'];
    for (let a = 0; a < 3; a++) {
      const ende = [o.x, o.y, o.z];
      ende[a] += box[a];
      const ag = new THREE.BufferGeometry();
      ag.setAttribute('position', new THREE.Float32BufferAttribute([o.x, o.y, o.z, ...ende], 3));
      gruppe.add(new THREE.LineSegments(ag, new THREE.LineBasicMaterial({ color: farben[a] })));
      const marke = [o.x, o.y, o.z];
      marke[a] += box[a] * 1.06;
      const s = textSprite(`${namen[a]} ${box[a]}`, `#${farben[a].toString(16).padStart(6, '0')}`, 0.045 * groesst);
      s.position.set(...marke);
      gruppe.add(s);
    }
    return gruppe;
  }

  setzeSchnittAnzeige({ modus, achse, lage, dicke }) {
    const g = this.schnittGruppe;
    while (g.children.length) {
      const c = g.children.pop();
      c.geometry.dispose();
    }
    if (modus === 'aus' || !this.box) return;
    const ebenen = modus === 'scheibe' ? [lage - dicke / 2, lage + dicke / 2] : [lage];
    const a = achse;
    const b = (a + 1) % 3;
    const c = (a + 2) % 3;
    const o = [this.ursprung.x, this.ursprung.y, this.ursprung.z];
    for (const w of ebenen) {
      if (w < 0 || w > this.box[a]) continue;
      const pkt = [];
      for (const [u, v] of [[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]) {
        const q = o.slice();
        q[a] += w;
        q[b] += u * this.box[b];
        q[c] += v * this.box[c];
        pkt.push(...q);
      }
      const geo = new THREE.BufferGeometry();
      geo.setAttribute('position', new THREE.Float32BufferAttribute(pkt, 3));
      const linie = new THREE.Line(geo, new THREE.LineBasicMaterial({ color: 0xf2b134, transparent: true, opacity: 0.8, depthTest: false }));
      linie.renderOrder = 9;
      g.add(linie);
    }
    this.bedarf = true;
  }

  blick(art) {
    const fov = THREE.MathUtils.degToRad(this.kamera.fov);
    const abstand = ((this.radius / Math.tan(fov / 2)) * 1.42) / (this.zoom > 0 ? this.zoom : 1);
    const richtung = {
      schraeg: [0.92, -1.72, 0.98],
      vorn: [0.0, -1.0, 0.0001],
      oben: [0.0, -0.001, 1.0],
      seite: [1.0, 0.0001, 0.0001],
    }[art] ?? [0.92, -1.72, 0.98];
    const v = new THREE.Vector3(...richtung).normalize().multiplyScalar(abstand);
    this.kamera.position.copy(this.mitte).add(v);
    this.kamera.near = abstand / 200;
    this.kamera.far = abstand * 20;
    this.kamera.updateProjectionMatrix();
    this.steuerung.target.copy(this.mitte);
    this.steuerung.update();
    this.bedarf = true;
  }

  zeichne(gemeinsam) {
    const d = this.kamera.position.distanceTo(this.mitte);
    gemeinsam.uSchleierBereich.value.set(Math.max(0, d - this.radius), d + this.radius);
    const t0 = performance.now();
    this.gpu.beginn();
    this.renderer.render(this.szene, this.kamera);
    this.gpu.ende();
    const ms = performance.now() - t0;
    this.cpuMs = this.cpuMs === null ? ms : 0.85 * this.cpuMs + 0.15 * ms;
  }
}
