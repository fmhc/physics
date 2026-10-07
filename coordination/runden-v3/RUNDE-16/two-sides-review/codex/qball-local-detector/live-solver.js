/**
 * Live CPU solver of the spherically symmetric (l=0) 3D complex scalar PDE.
 * This is a radial PDE, not a Cartesian 3D simulation. A 3D renderer may
 * reconstruct spherical shells from these genuinely evolved radial values.
 *
 * U(S)=S-S²+S³/2, q=r exp(i omega t) psi, p=q_t, pi=p-i omega q:
 * q_tt=q_rr+2i omega p+(omega²-1+2|q/r|²-1.5|q/r|⁴)q-2 sigma pi.
 * q(0)=q(R)=0; fourth-order differences use odd ghost extensions.
 * Classical RK4 uses dt=0.2h. No prerecorded evolution or time interpolation.
 * A second, unperturbed nonlinear field is evolved simultaneously.
 *
 * Optional linear=true evolves the perturbation about the static input f:
 * z_tt=z_rr+2i omega z_t+(omega²-D)z-C conjugate(z)-2 sigma(z_t-i omega z),
 * D=1-4f²+4.5f⁴, C=-2f²+3f⁴. The displayed field is baseline+z.
 * Its full nonlinear energy is a comparison diagnostic, NOT a conserved
 * energy of that linearized equation; sample().balanceApplicable is false.
 *
 * Sponge: sigma=((r-(R-15))/15)^4 in the outer 15 units, zero elsewhere.
 * It damps physical psi_t, not rotating p alone. This is an approximate
 * absorbing layer plus an outer Dirichlet wall, not an exact radiation BC.
 * Reflections and finite-domain effects remain possible.
 *
 * E=4pi integral[|pi|²+|q_r-q/r|²+r²U(|q/r|²)]dr,
 * Q=-8pi integral Im(conjugate(q)pi)dr.
 * The sponge contributes E_dot=-16pi integral sigma|pi|²dr,
 * Q_dot=+16pi integral sigma Im(conjugate(q)pi)dr.
 * These sink rates are integrated with the same RK4 stage weights. Absorbed
 * charge is signed; energy sink is nonnegative. E+absorbedEnergy and
 * Q+absorbedCharge are balance diagnostics. Spatial differentiation and
 * Simpson quadrature approximate continuum E,Q: they are not exact discrete
 * invariants. All computation occurs on the browser CPU executing step().
 */
export class RadialSimulation {
  constructor({ profile, epsilon = 0.02, linear = false, absorber = true, h = 0.2, R = 80 } = {}) {
    if (!profile || !Array.isArray(profile.r) || profile.r.length < 4) {
      throw new TypeError('A genuine exported radial initial profile is required.');
    }
    if (![epsilon, h, R].every(Number.isFinite) || h <= 0 || R < 30) {
      throw new RangeError('epsilon, h and R must be finite; h>0 and R>=30.');
    }
    const intervals = Math.round(R / h);
    if (Math.abs(intervals * h - R) > 1e-9 || intervals % 2 || intervals < 80 || intervals > 1600) {
      throw new RangeError('Use an even number of radial intervals between 80 and 1600 (e.g. R80/h.2 or h.1).');
    }
    if (Math.abs(epsilon) > 0.25) throw new RangeError('This small-perturbation explorer supports |epsilon|<=0.25.');
    const length = profile.r.length;
    for (const key of ['f', 'u', 'v']) {
      if (!Array.isArray(profile[key]) || profile[key].length !== length || !profile[key].every(Number.isFinite)) {
        throw new TypeError(`Invalid initial profile array: ${key}`);
      }
    }
    if (!profile.r.every(Number.isFinite) || profile.r[0] !== 0 || profile.r.some((r, i) => i && r <= profile.r[i - 1])) {
      throw new TypeError('Initial radii must start at zero and increase strictly.');
    }
    this.omega2 = Number(profile.omega2);
    this.rho = Number(profile.rho);
    if (!(this.omega2 > 0 && this.omega2 < 1) || !Number.isFinite(this.rho)) throw new RangeError('Invalid profile frequencies.');
    this.omega = Math.sqrt(this.omega2);
    const closedSquared = 1 - (this.omega - this.rho) ** 2;
    if (!(closedSquared > 0)) throw new RangeError('The supplied initial mode must have its stated closed tail.');
    const normalization = Number(profile.normalizer);
    if (!(normalization > 0 && Number.isFinite(normalization))) throw new RangeError('Missing fixed mode normalization.');
    this.N = intervals + 1;
    this.h = h;
    this.R = R;
    this.dt = 0.2 * h;
    this.t = 0;
    this.steps = 0;
    this.epsilon = epsilon;
    this.linear = Boolean(linear);
    this.absorber = Boolean(absorber);
    this.absorberWidth = 15;
    this.failed = false;
    this.r = Float64Array.from({ length: this.N }, (_, i) => i * h);
    this._sigma = new Float64Array(this.N);
    this._D = new Float64Array(this.N);
    this._C = new Float64Array(this.N);
    this._f = new Float64Array(this.N);
    // Layout per field: qRe, qIm, pRe, pIm; primary then baseline.
    this._y = new Float64Array(8 * this.N);
    this._work = new Float64Array(this._y.length);
    this._k = Array.from({ length: 4 }, () => new Float64Array(this._y.length));
    this._rates = Array.from({ length: 4 }, () => new Float64Array(4));
    this._absorbed = new Float64Array(4); // main E,Q; baseline E,Q
    this._initialEnergy = null;
    this._initialCharge = null;
    this._initialBaselineEnergy = null;
    this._initialBaselineCharge = null;
    const last = length - 1;
    const sourceR = profile.r[last];
    const alpha = Math.sqrt(1 - this.omega2);
    const kappa = Math.sqrt(closedSquared);
    let cursor = 0;
    for (let i = 0; i < this.N; i++) {
      const r = this.r[i];
      let f, u, v;
      if (r <= sourceR) {
        while (cursor + 1 < last && profile.r[cursor + 1] < r) cursor++;
        const width = profile.r[cursor + 1] - profile.r[cursor];
        const s = (r - profile.r[cursor]) / width;
        f = profile.f[cursor] + s * (profile.f[cursor + 1] - profile.f[cursor]);
        u = profile.u[cursor] + s * (profile.u[cursor + 1] - profile.u[cursor]);
        v = profile.v[cursor] + s * (profile.v[cursor + 1] - profile.v[cursor]);
      } else {
        // Explicit vacuum-tail initialization beyond the exported R68 data.
        // The BIC's open exterior is set to zero; the closed tail decays.
        f = profile.f[last] * sourceR / r * Math.exp(-alpha * (r - sourceR));
        u = 0;
        v = profile.v[last] * Math.exp(-kappa * (r - sourceR));
      }
      u /= normalization;
      v /= normalization;
      this._f[i] = f;
      const s = f * f;
      this._D[i] = 1 - 4 * s + 4.5 * s * s;
      this._C[i] = -2 * s + 3 * s * s;
      const baseline = r * f;
      this._y[4 * this.N + i] = baseline;
      this._y[i] = (this.linear ? 0 : baseline) + epsilon * (u + v);
      this._y[3 * this.N + i] = epsilon * this.rho * (v - u);
      if (this.absorber && r > R - this.absorberWidth) {
        this._sigma[i] = ((r - R + this.absorberWidth) / this.absorberWidth) ** 4;
      }
    }
    // Endpoint constraints are exact; no r=0 division is used in evolution.
    for (let block = 0; block < 8; block++) {
      this._y[block * this.N] = 0;
      this._y[(block + 1) * this.N - 1] = 0;
    }
    const initial = this.sample();
    this._initialEnergy = initial.energy;
    this._initialCharge = initial.charge;
    this._initialBaselineEnergy = initial.baselineEnergy;
    this._initialBaselineCharge = initial.baselineCharge;
    this.initialMaxDensity = initial.maxDensity;
    this.profileProvenance = profile.provenance || null;
  }

  _laplacian(y, offset, i) {
    const n = this.N;
    const denominator = 12 * this.h * this.h;
    if (i === 1) return (-y[offset + 3] + 16 * y[offset + 2] - 29 * y[offset + 1]) / denominator;
    if (i === n - 2) return (-y[offset + n - 4] + 16 * y[offset + n - 3] - 29 * y[offset + n - 2]) / denominator;
    return (-y[offset + i + 2] + 16 * y[offset + i + 1] - 30 * y[offset + i] + 16 * y[offset + i - 1] - y[offset + i - 2]) / denominator;
  }

  _derivative(a, i) {
    const n = this.N, h = this.h;
    if (i === 0) return (8 * a[1] - a[2]) / (6 * h);
    if (i === n - 1) return (a[n - 3] - 8 * a[n - 2]) / (6 * h);
    if (i === 1) return (-a[1] + 8 * a[2] - a[3]) / (12 * h);
    if (i === n - 2) return (a[n - 4] - 8 * a[n - 3] + a[n - 2]) / (12 * h);
    return (a[i - 2] - 8 * a[i - 1] + 8 * a[i + 1] - a[i + 2]) / (12 * h);
  }

  _rhs(y, out, rates) {
    const n = this.N, w = this.omega;
    out.fill(0);
    rates.fill(0);
    for (let field = 0; field < 2; field++) {
      const o = field * 4 * n;
      for (let i = 1; i < n - 1; i++) {
        const qr = y[o + i], qi = y[o + n + i];
        const pr = y[o + 2 * n + i], pi = y[o + 3 * n + i];
        const sigma = this._sigma[i];
        out[o + i] = pr;
        out[o + n + i] = pi;
        let fr, fi;
        if (field === 0 && this.linear) {
          fr = (this.omega2 - this._D[i] - this._C[i]) * qr;
          fi = (this.omega2 - this._D[i] + this._C[i]) * qi;
        } else {
          const s = (qr * qr + qi * qi) / (this.r[i] * this.r[i]);
          const factor = this.omega2 - 1 + 2 * s - 1.5 * s * s;
          fr = factor * qr;
          fi = factor * qi;
        }
        out[o + 2 * n + i] = this._laplacian(y, o, i) - 2 * w * pi + fr - 2 * sigma * (pr + w * qi);
        out[o + 3 * n + i] = this._laplacian(y, o + n, i) + 2 * w * pr + fi - 2 * sigma * (pi - w * qr);
      }
    }
    // Sink quadrature at this actual RK stage. Linear mode uses its displayed
    // baseline+perturbation field, but no nonlinear balance claim is made.
    for (let i = 1; i < n - 1; i++) {
      const sigma = this._sigma[i];
      if (sigma === 0) continue;
      const weight = i % 2 ? 4 : 2;
      for (let field = 0; field < 2; field++) {
        const o = field * 4 * n;
        const extra = field === 0 && this.linear ? 4 * n : -1;
        const qr = y[o + i] + (extra >= 0 ? y[extra + i] : 0);
        const qi = y[o + n + i] + (extra >= 0 ? y[extra + n + i] : 0);
        const pr = y[o + 2 * n + i] + (extra >= 0 ? y[extra + 2 * n + i] : 0) + w * qi;
        const pi = y[o + 3 * n + i] + (extra >= 0 ? y[extra + 3 * n + i] : 0) - w * qr;
        rates[2 * field] += weight * sigma * (pr * pr + pi * pi);
        rates[2 * field + 1] += -weight * sigma * (qr * pi - qi * pr);
      }
    }
    const factor = 16 * Math.PI * this.h / 3;
    for (let i = 0; i < 4; i++) rates[i] *= factor;
  }

  /** Advance real RK4 steps. Host UI should budget about <=200 steps/second. */
  step(count = 1) {
    if (!Number.isInteger(count) || count < 0 || count > 4096) throw new RangeError('step count must be an integer in [0,4096].');
    if (this.failed) throw new Error('Reset the failed simulation before advancing.');
    const y = this._y, z = this._work, [k1, k2, k3, k4] = this._k;
    const [s1, s2, s3, s4] = this._rates, dt = this.dt;
    for (let step = 0; step < count; step++) {
      this._rhs(y, k1, s1);
      for (let j = 0; j < y.length; j++) z[j] = y[j] + dt * k1[j] / 2;
      this._rhs(z, k2, s2);
      for (let j = 0; j < y.length; j++) z[j] = y[j] + dt * k2[j] / 2;
      this._rhs(z, k3, s3);
      for (let j = 0; j < y.length; j++) z[j] = y[j] + dt * k3[j];
      this._rhs(z, k4, s4);
      for (let j = 0; j < y.length; j++) {
        y[j] += dt * (k1[j] + 2 * k2[j] + 2 * k3[j] + k4[j]) / 6;
        if (!Number.isFinite(y[j])) {
          this.failed = true;
          throw new Error('Nonfinite PDE state: numerical evolution stopped; reset or reduce the perturbation.');
        }
      }
      for (let j = 0; j < 4; j++) this._absorbed[j] += dt * (s1[j] + 2 * s2[j] + 2 * s3[j] + s4[j]) / 6;
      this.steps++;
      this.t = this.steps * dt;
    }
    return this.t;
  }

  /** Actual current fields, copied into fresh arrays; no fitted/preset motion.
   * psiRe/psiIm explicitly mean the ROTATING field exp(i omega t) psi=q/r.
   * Laboratory psi is obtained by multiplication by exp(-i omega t).
   * This internal complex phase is not a spatial rotation.
   */
  sample() {
    const n = this.N, y = this._y, w = this.omega;
    const qr = new Float64Array(n), qi = new Float64Array(n);
    const pr = new Float64Array(n), pi = new Float64Array(n);
    const br = y.subarray(4 * n, 5 * n), bi = y.subarray(5 * n, 6 * n);
    const bpr = y.subarray(6 * n, 7 * n), bpi = y.subarray(7 * n, 8 * n);
    for (let i = 0; i < n; i++) {
      qr[i] = y[i] + (this.linear ? br[i] : 0);
      qi[i] = y[n + i] + (this.linear ? bi[i] : 0);
      pr[i] = y[2 * n + i] + (this.linear ? bpr[i] : 0);
      pi[i] = y[3 * n + i] + (this.linear ? bpi[i] : 0);
    }
    const psiRe = new Float64Array(n), psiIm = new Float64Array(n);
    const deltaRe = new Float64Array(n), deltaIm = new Float64Array(n);
    const density = new Float64Array(n), baselineDensity = new Float64Array(n);
    const flux = new Float64Array(n), baselineFlux = new Float64Array(n), deltaFlux = new Float64Array(n);
    let energy = 0, charge = 0, baselineEnergy = 0, baselineCharge = 0;
    let deltaNorm = 0, maxDensity = 0, maxAbsDelta = 0;
    for (let i = 0; i < n; i++) {
      const r = this.r[i], weight = i === 0 || i === n - 1 ? 1 : i % 2 ? 4 : 2;
      const bPsiRe = i ? br[i] / r : this._derivative(br, 0);
      const bPsiIm = i ? bi[i] / r : this._derivative(bi, 0);
      psiRe[i] = i ? qr[i] / r : this._derivative(qr, 0);
      psiIm[i] = i ? qi[i] / r : this._derivative(qi, 0);
      deltaRe[i] = psiRe[i] - bPsiRe;
      deltaIm[i] = psiIm[i] - bPsiIm;
      const s = psiRe[i] ** 2 + psiIm[i] ** 2;
      const bs = bPsiRe ** 2 + bPsiIm ** 2;
      density[i] = s;
      baselineDensity[i] = bs;
      maxDensity = Math.max(maxDensity, s);
      maxAbsDelta = Math.max(maxAbsDelta, Math.hypot(deltaRe[i], deltaIm[i]));
      const labPr = pr[i] + w * qi[i], labPi = pi[i] - w * qr[i];
      const bLabPr = bpr[i] + w * bi[i], bLabPi = bpi[i] - w * br[i];
      const gr = i ? this._derivative(qr, i) - psiRe[i] : 0;
      const gi = i ? this._derivative(qi, i) - psiIm[i] : 0;
      const bgr = i ? this._derivative(br, i) - bPsiRe : 0;
      const bgi = i ? this._derivative(bi, i) - bPsiIm : 0;
      const e = labPr ** 2 + labPi ** 2 + gr ** 2 + gi ** 2 + r * r * (s - s * s + 0.5 * s ** 3);
      const be = bLabPr ** 2 + bLabPi ** 2 + bgr ** 2 + bgi ** 2 + r * r * (bs - bs * bs + 0.5 * bs ** 3);
      energy += weight * e;
      baselineEnergy += weight * be;
      charge += -2 * weight * (qr[i] * labPi - qi[i] * labPr);
      baselineCharge += -2 * weight * (br[i] * bLabPi - bi[i] * bLabPr);
      deltaNorm += weight * ((qr[i] - br[i]) ** 2 + (qi[i] - bi[i]) ** 2);
      flux[i] = i ? -8 * Math.PI * (labPr * gr + labPi * gi) : 0;
      baselineFlux[i] = i ? -8 * Math.PI * (bLabPr * bgr + bLabPi * bgi) : 0;
      // Quadratic difference-field diagnostic, not full nonlinear energy loss.
      deltaFlux[i] = i ? -8 * Math.PI * ((labPr - bLabPr) * (gr - bgr) + (labPi - bLabPi) * (gi - bgi)) : 0;
    }
    const volumeFactor = 4 * Math.PI * this.h / 3;
    energy *= volumeFactor;
    charge *= volumeFactor;
    baselineEnergy *= volumeFactor;
    baselineCharge *= volumeFactor;
    deltaNorm *= volumeFactor;
    const e0 = this._initialEnergy ?? energy, q0 = this._initialCharge ?? charge;
    const be0 = this._initialBaselineEnergy ?? baselineEnergy, bq0 = this._initialBaselineCharge ?? baselineCharge;
    return {
      r: this.r.slice(), psiRe, psiIm, density, baselineDensity, deltaRe, deltaIm, flux, baselineFlux, deltaFlux,
      t: this.t, steps: this.steps, dt: this.dt, h: this.h, R: this.R, N: this.N,
      omega: w, rho: this.rho, epsilon: this.epsilon, linear: this.linear, absorber: this.absorber,
      energy, charge, baselineEnergy, baselineCharge, deltaNorm, maxDensity, maxAbsDelta,
      absorbedEnergy: this._absorbed[0], absorbedCharge: this._absorbed[1],
      energyDrift: (energy - e0) / Math.max(Math.abs(e0), 1e-30),
      energyBalanceDrift: (energy + this._absorbed[0] - e0) / Math.max(Math.abs(e0), 1e-30),
      chargeBalanceDrift: (charge + this._absorbed[1] - q0) / Math.max(Math.abs(q0), 1e-30),
      baselineEnergyBalanceDrift: (baselineEnergy + this._absorbed[2] - be0) / Math.max(Math.abs(be0), 1e-30),
      baselineChargeBalanceDrift: (baselineCharge + this._absorbed[3] - bq0) / Math.max(Math.abs(bq0), 1e-30),
      balanceApplicable: !this.linear,
      fieldFrame: 'rotating: psiRe+i psiIm = exp(i omega t) psi_lab = q/r',
      finite: [energy, charge, baselineEnergy, baselineCharge, deltaNorm, maxDensity].every(Number.isFinite),
      model: 'radial 3D l=0, rotating complex field; spherical reconstruction only',
      boundary: this.absorber ? 'quartic physical-velocity sponge in outer 15 plus Dirichlet wall' : 'Dirichlet wall; reflection expected',
    };
  }
}
