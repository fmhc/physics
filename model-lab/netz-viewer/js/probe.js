// SPDX-License-Identifier: Apache-2.0
// SPDX-FileCopyrightText: 2026 Finn Malte Hinrichsen
// Probe-Datensatz im Format netz-gpu/1, im Browser erzeugt (?probe=1).
// Netz: periodisches BCC-Tetraedernetz (nicht Netz V): Ecken auf dem Wuerfelgitter plus Zellmitten,
// je Zelle 2 Ecken, 14 Kanten, 24 Dreiecke, 12 Tetraeder (Euler 2 - 14 + 24 - 12 = 0).
// Felder: analytisches Testmuster, KEINE Rechnung und keine Messdaten. Es soll nur zeigen,
// ob die Ansicht Indizes, Periodizitaet, Farbskalen und Zeitleiste richtig behandelt.
//   verschiebung: Welle mit Plus-Polarisation laeuft in z (in der Boxmitte wie h+, periodisch gefaltet)
//   dehnung:      geometrisch aus derselben (nicht ueberhoehten) Verschiebung, also passend zur Anzeige
//   skalar_betrag2, energie, takt: Gauss-Klumpen auf einer Kreisbahn, dazu Wellenenergie in Baendern
//   fluss:        zirkular polarisierte Lichtwelle in x, Fluss = B · n · Flaeche je Dreieck
//   rahmen:       Igel-Textur um den Klumpen, die sich mit der Zeit um z dreht

const TAU = 2 * Math.PI;

export class ProbeQuelle {
  constructor({ n = 12, bilder = 48 } = {}) {
    this.art = 'probe';
    this.n = n;
    this.L = n;
    this.bilder = bilder;
    this.T = n; // Periode in a/c: die Lichtwelle laeuft genau einmal (mal Wellenzahl) durch die Box
    this.dt = this.T / bilder;
    this.a = 1e-3; // Dehnungsamplitude
    this.ueber = 40; // Ueberhoehung der Anzeige-Verschiebung
    this.sigma = Math.max(1.0, n / 12);
    this.B0 = 1.4;
    this.baueNetz();
    this.vorrechnen();
  }

  baueNetz() {
    const n = this.n;
    const n3 = n * n * n;
    const m = (a) => ((a % n) + n) % n;
    const C = (i, j, k) => (m(i) * n + m(j)) * n + m(k);
    const Z = (i, j, k) => n3 + C(i, j, k);
    const N = 2 * n3;
    const ecken = new Float32Array(3 * N);
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        for (let k = 0; k < n; k++) {
          const c = C(i, j, k);
          const z = Z(i, j, k);
          ecken.set([i, j, k], 3 * c);
          ecken.set([i + 0.5, j + 0.5, k + 0.5], 3 * z);
        }
      }
    }
    const E = [[1, 0, 0], [0, 1, 0], [0, 0, 1]];
    const kanten = new Uint32Array(2 * 14 * n3);
    const dreiecke = new Uint32Array(3 * 24 * n3);
    let ke = 0;
    let de = 0;
    const kante = (a, b) => { kanten[ke++] = a; kanten[ke++] = b; };
    const dreieck = (a, b, c) => { dreiecke[de++] = a; dreiecke[de++] = b; dreiecke[de++] = c; };
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        for (let k = 0; k < n; k++) {
          for (let a = 0; a < 3; a++) {
            const e = E[a];
            kante(C(i, j, k), C(i + e[0], j + e[1], k + e[2]));
            kante(Z(i, j, k), Z(i + e[0], j + e[1], k + e[2]));
            const eb = E[(a + 1) % 3];
            const ec = E[(a + 2) % 3];
            for (let b = 0; b < 2; b++) {
              for (let c = 0; c < 2; c++) {
                // Eckkante C(p)-C(p+e_a) mit einer der vier umgebenden Zellmitten
                dreieck(C(i, j, k), C(i + e[0], j + e[1], k + e[2]),
                  Z(i - b * eb[0] - c * ec[0], j - b * eb[1] - c * ec[1], k - b * eb[2] - c * ec[2]));
                // Mittenkante Z(p)-Z(p+e_a) mit einer der vier umgebenden Ecken
                dreieck(Z(i, j, k), Z(i + e[0], j + e[1], k + e[2]),
                  C(i + e[0] + b * eb[0] + c * ec[0], j + e[1] + b * eb[1] + c * ec[1], k + e[2] + b * eb[2] + c * ec[2]));
              }
            }
          }
          for (let a = 0; a < 2; a++) for (let b = 0; b < 2; b++) for (let c = 0; c < 2; c++) kante(Z(i, j, k), C(i + a, j + b, k + c));
        }
      }
    }
    this.N = N;
    this.ecken = ecken;
    this.kanten = kanten;
    this.dreiecke = dreiecke;
  }

  mi(d) {
    return d - this.L * Math.round(d / this.L);
  }

  vorrechnen() {
    const { N, L, ecken, kanten, dreiecke } = this;
    const S = (u) => (L / TAU) * Math.sin((TAU * (u - L / 2)) / L);
    this.Sx = new Float64Array(N);
    this.Sy = new Float64Array(N);
    for (let i = 0; i < N; i++) {
      this.Sx[i] = S(ecken[3 * i]);
      this.Sy[i] = S(ecken[3 * i + 1]);
    }
    // Kanten: Ruhevektor im Mindestbild
    const nk = kanten.length / 2;
    this.kd = new Float64Array(3 * nk);
    this.kl = new Float64Array(nk);
    for (let e = 0; e < nk; e++) {
      const a = kanten[2 * e];
      const b = kanten[2 * e + 1];
      let q = 0;
      for (let c = 0; c < 3; c++) {
        const d = this.mi(ecken[3 * b + c] - ecken[3 * a + c]);
        this.kd[3 * e + c] = d;
        q += d * d;
      }
      this.kl[e] = Math.sqrt(q);
    }
    // Dreiecke: einheitlich ausrichten (Normale in Richtung w), Mitte x, n·A in y und z
    const nd = dreiecke.length / 3;
    const w = [0.27, 0.48, 0.83];
    this.dx = new Float64Array(nd);
    this.dny = new Float64Array(nd);
    this.dnz = new Float64Array(nd);
    for (let t = 0; t < nd; t++) {
      const i0 = dreiecke[3 * t];
      const i1 = dreiecke[3 * t + 1];
      const i2 = dreiecke[3 * t + 2];
      const u = [0, 1, 2].map((c) => this.mi(ecken[3 * i1 + c] - ecken[3 * i0 + c]));
      const v = [0, 1, 2].map((c) => this.mi(ecken[3 * i2 + c] - ecken[3 * i0 + c]));
      let nx = 0.5 * (u[1] * v[2] - u[2] * v[1]);
      let ny = 0.5 * (u[2] * v[0] - u[0] * v[2]);
      let nz = 0.5 * (u[0] * v[1] - u[1] * v[0]);
      if (nx * w[0] + ny * w[1] + nz * w[2] < 0) {
        dreiecke[3 * t + 1] = i2;
        dreiecke[3 * t + 2] = i1;
        nx = -nx;
        ny = -ny;
        nz = -nz;
      }
      const cx = ecken[3 * i0] + (u[0] + v[0]) / 3;
      this.dx[t] = cx - L * Math.floor(cx / L);
      this.dny[t] = ny;
      this.dnz[t] = nz;
    }
    // Diagnose ueber alle Bilder (nur Eckfelder, billig)
    const dV = (L * L * L) / N;
    this.ladung = [];
    this.energieGesamt = [];
    for (let f = 0; f < this.bilder; f++) {
      const { phi2, energie } = this.eckFelder(f * this.dt, false);
      let q = 0;
      let en = 0;
      for (let i = 0; i < N; i++) {
        q += phi2[i];
        en += energie[i];
      }
      this.ladung.push(q * dV);
      this.energieGesamt.push(en * dV);
    }
  }

  zentrum(t) {
    const w = (TAU * t) / this.T;
    const R = this.L / 5;
    return [this.L / 2 + R * Math.cos(w), this.L / 2 + R * Math.sin(w), this.L / 2];
  }

  eckFelder(t, alles = true) {
    const { N, ecken, sigma } = this;
    const z0 = this.zentrum(t);
    const kg = (TAU * 2) / this.L;
    const phi2 = new Float32Array(N);
    const energie = new Float32Array(N);
    const takt = alles ? new Float32Array(N) : null;
    const sN2 = (1.5 * sigma) ** 2;
    for (let i = 0; i < N; i++) {
      const dx = this.mi(ecken[3 * i] - z0[0]);
      const dy = this.mi(ecken[3 * i + 1] - z0[1]);
      const dz = this.mi(ecken[3 * i + 2] - z0[2]);
      const r2 = dx * dx + dy * dy + dz * dz;
      const p = Math.exp(-r2 / (2 * sigma * sigma));
      const s = Math.sin(kg * ecken[3 * i + 2] - kg * t);
      phi2[i] = p;
      energie[i] = 1.5 * p + 0.3 * s * s;
      if (takt) takt[i] = -0.01 / Math.sqrt(1 + r2 / sN2);
    }
    return { phi2, energie, takt };
  }

  verschiebungWahr(t) {
    const { N, ecken, a } = this;
    const kg = (TAU * 2) / this.L;
    const xi = new Float64Array(3 * N);
    for (let i = 0; i < N; i++) {
      const c = Math.cos(kg * ecken[3 * i + 2] - kg * t);
      xi[3 * i] = a * this.Sx[i] * c;
      xi[3 * i + 1] = -a * this.Sy[i] * c;
    }
    return xi;
  }

  manifest() {
    const { n, L, N } = this;
    const n3 = n * n * n;
    const vmax = Math.ceil(this.ueber * this.a * (L / TAU) * 100) / 100;
    return {
      format: 'netz-gpu/1',
      titel: `Probe: BCC-Tetraedernetz ${n}³ mit Testwelle und Klumpen`,
      erzeugt: new Date().toISOString(),
      netz: { typ: 'Probe-BCC (nicht Netz V)', zellen: [n, n, n], N_ecken: N, N_kanten: 14 * n3, N_dreiecke: 24 * n3, N_tetraeder: 12 * n3, box: [L, L, L], periodisch: true },
      einheiten: { laenge: 'a (Kante der kubischen Zelle)', zeit: 'a/c' },
      groessen: [
        { name: 'skalar_betrag2', ort: 'ecke', komponenten: 1, bedeutung: '|phi|^2, Gauss-Klumpen (Testmuster)', min: 0, max: 1 },
        { name: 'energie', ort: 'ecke', komponenten: 1, bedeutung: 'Energiedichte (Testmuster)', min: 0, max: 1.8 },
        { name: 'dehnung', ort: 'kante', komponenten: 1, bedeutung: 'relative Laengenaenderung delta l / l', min: -this.a, max: this.a },
        { name: 'fluss', ort: 'dreieck', komponenten: 1, bedeutung: 'Lichtfluss B·n·A (Testmuster)', min: -0.5, max: 0.5 },
        { name: 'takt', ort: 'ecke', komponenten: 1, bedeutung: 'Lapse N - 1 (Testmuster)', min: -0.01, max: 0 },
        { name: 'rahmen', ort: 'ecke', komponenten: 4, bedeutung: 'Einheitsquaternion (w, x, y, z)', min: -1, max: 1 },
        { name: 'verschiebung', ort: 'ecke', komponenten: 3, bedeutung: `Anzeige-Verschiebung, ${this.ueber}-fach ueberhoeht`, min: -vmax, max: vmax },
      ],
      frames: Array.from({ length: this.bilder }, (_, i) => ({ index: i, zeit: i * this.dt, ordner: `frames/${String(i).padStart(6, '0')}` })),
      diagnose: { energie_gesamt: this.energieGesamt, ladung: this.ladung },
      quelle: { code: 'netz-viewer/js/probe.js', lauf: 'im Browser erzeugt', hinweis: 'analytisches Testmuster, keine Rechnung, keine Messdaten' },
    };
  }

  async netz() {
    return { ecken: this.ecken, kanten: this.kanten, dreiecke: this.dreiecke };
  }

  async bild(i, name) {
    await new Promise((r) => setTimeout(r, 0));
    const t = i * this.dt;
    const { N } = this;
    if (name === 'skalar_betrag2') return this.eckFelder(t).phi2;
    if (name === 'energie') return this.eckFelder(t).energie;
    if (name === 'takt') return this.eckFelder(t).takt;
    if (name === 'verschiebung') {
      const xi = this.verschiebungWahr(t);
      const v = new Float32Array(3 * N);
      for (let k = 0; k < 3 * N; k++) v[k] = this.ueber * xi[k];
      return v;
    }
    if (name === 'dehnung') {
      const xi = this.verschiebungWahr(t);
      const nk = this.kanten.length / 2;
      const out = new Float32Array(nk);
      for (let e = 0; e < nk; e++) {
        const a = this.kanten[2 * e];
        const b = this.kanten[2 * e + 1];
        const x = this.kd[3 * e] + xi[3 * b] - xi[3 * a];
        const y = this.kd[3 * e + 1] + xi[3 * b + 1] - xi[3 * a + 1];
        const z = this.kd[3 * e + 2] + xi[3 * b + 2] - xi[3 * a + 2];
        out[e] = Math.sqrt(x * x + y * y + z * z) / this.kl[e] - 1;
      }
      return out;
    }
    if (name === 'fluss') {
      const kl = (TAU * 3) / this.L;
      const nd = this.dx.length;
      const out = new Float32Array(nd);
      for (let d = 0; d < nd; d++) {
        const psi = kl * this.dx[d] - kl * t;
        out[d] = this.B0 * (this.dny[d] * Math.cos(psi) + this.dnz[d] * Math.sin(psi));
      }
      return out;
    }
    if (name === 'rahmen') {
      const z0 = this.zentrum(t);
      const s2 = (1.6 * this.sigma) ** 2;
      const Om = (TAU * 2) / this.T;
      const out = new Float32Array(4 * N);
      for (let k = 0; k < N; k++) {
        const dx = this.mi(this.ecken[3 * k] - z0[0]);
        const dy = this.mi(this.ecken[3 * k + 1] - z0[1]);
        const dz = this.mi(this.ecken[3 * k + 2] - z0[2]);
        const r = Math.sqrt(dx * dx + dy * dy + dz * dz);
        const huelle = Math.exp(-(r * r) / (2 * s2));
        const th = Math.PI * huelle;
        const ux = r > 1e-9 ? dx / r : 0;
        const uy = r > 1e-9 ? dy / r : 0;
        const uz = r > 1e-9 ? dz / r : 1;
        const sh = Math.sin(th / 2);
        const hw = Math.cos(th / 2);
        const hx = sh * ux;
        const hy = sh * uy;
        const hz = sh * uz;
        const al = Om * t * huelle;
        const zw = Math.cos(al / 2);
        const zz = Math.sin(al / 2);
        // q = q_z(al) * q_igel
        out[4 * k] = zw * hw - zz * hz;
        out[4 * k + 1] = zw * hx - zz * hy;
        out[4 * k + 2] = zw * hy + zz * hx;
        out[4 * k + 3] = zw * hz + zz * hw;
      }
      return out;
    }
    throw new Error(`Probe kennt die Größe ${name} nicht`);
  }
}
