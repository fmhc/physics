/* STRING-1 (Runde 35): Monte-Carlo-Kerne fuer das Strommodell (Wurm) und das Villain-Winkelmodell.
 * Uebersetzt auf der .69 (kein Rechenlauf): gcc -O2 -shared -fPIC -o string_kern.so string_kern.c -lm
 * Geladen von string_mc.py per ctypes.
 *
 * Gitter: d-dimensionaler Torus, V = L^d Plaetze, Platzindex x = sum_mu x_mu L^mu.
 *   nb[x*2d + k]: Nachbar von x in Richtung k; k = 2 mu: +e_mu, k = 2 mu + 1: -e_mu.
 *   Kante (x, mu) verbindet x und x + e_mu; Fluss n[x*d + mu], positiv = von x nach x + e_mu.
 *   Divergenz div(x) = Abfluss - Zufluss = sum_mu (n[x,mu] - n[x - e_mu, mu]).
 *
 * Wurm (Prokof'ev/Svistunov), erweiterter Raum {(n, I, M): div n = delta_M - delta_I}, M = Schwanz (Quelle),
 * I = Kopf (Senke). Gewicht pi(n, I, M) = exp(-(K/2) sum_e n_e^2) * w(D), D = I - M (Verschiebung, Index wie Platz).
 *   Zug A: Richtung k gleichverteilt (W. 1/2d). Der Kopf geht ueber die Kante nach I' = nb[I][k], der Fluss in
 *     Laufrichtung f steigt um 1 (k gerade: n_e += 1; k ungerade: n_e -= 1 auf der Kante (I', mu)).
 *     Rueckzug: von I' die Gegenrichtung (W. 1/2d), Fluss in dessen Laufrichtung +1, also n_e zurueck.
 *     Vorschlag symmetrisch, Annahme min(1, exp(-(K/2)((f+1)^2 - f^2)) * w(D')/w(D)): detailliertes Gleichgewicht.
 *   Zug B: Ist danach I = M (geschlossen), wird die Lage x = I = M gleichverteilt neu gezogen. Alle V Lagen haben
 *     dasselbe Gewicht (w(0), gleiches n), also erhaelt B pi. Die Kette A, B, A, B, ... erhaelt pi.
 *   Messung: nach jedem Schritt (A, dann B) hist[D] += 1. Dann ist Z(D)/Z(0) = (hist[D]/w[D]) / (hist[0]/w[0]).
 *
 * Villain-XY: Gewicht je Kante V(phi) = sum_{m=-MM}^{MM} exp(-(KV/2)(phi - 2 pi m)^2), phi auf [-pi, pi) reduziert,
 *   KV = 1/K. Berechnet als exp(-(KV/2) phi^2) * sum_m c_m q^m mit q = exp(2 pi KV phi), c_m = exp(-2 pi^2 KV m^2).
 *   Optional Platzfaktor (1 + hz cos theta_x) mit hz = 2 z, z = exp(-mu/T) (Paarbildung, S6).
 *   Metropolis je Platz: theta' = theta + delta (2u - 1).
 */
#include <stdint.h>
#include <math.h>

static inline uint64_t rotl(const uint64_t x, int k) { return (x << k) | (x >> (64 - k)); }

static inline uint64_t naechste(uint64_t *s) { /* xoshiro256** */
    const uint64_t result = rotl(s[1] * 5, 7) * 9;
    const uint64_t t = s[1] << 17;
    s[2] ^= s[0]; s[3] ^= s[1]; s[1] ^= s[2]; s[0] ^= s[3];
    s[2] ^= t; s[3] = rotl(s[3], 45);
    return result;
}

/* gleichverteilt in [0, n) aus den oberen Bits (Verzerrung < n / 2^64) */
static inline uint32_t bis(uint64_t r, uint32_t n) { return (uint32_t)(((__uint128_t)r * n) >> 64); }

/* gleichverteilt in [0, 1) mit 53 Bit */
static inline double gleich01(uint64_t *s) { return (double)(naechste(s) >> 11) * 0x1.0p-53; }

#define FMAX 200 /* Tabelle exp(-(K/2)(2 f + 1)) fuer |f| <= FMAX, sonst exp direkt */

/* Wurm-Kern. zustand: [0] = I, [1] = M, [2] = D. gew: w[D] (Laenge V) oder NULL (w = 1).
 * z: [0] Versuche, [1] angenommen, [2] Schritte im geschlossenen Sektor, [3] groesstes |n| nach Annahme,
 *    [4] Zuege mit |f| > FMAX (exp direkt) */
int64_t wurm_laufe(int64_t nschritte, int32_t d, int32_t V, const int32_t *nb, int32_t *n, int32_t *zustand,
                   const double *gew, double halbK, uint64_t *rng, int64_t *hist, int64_t *z) {
    static double tab[2 * FMAX + 1];
    for (int f = -FMAX; f <= FMAX; f++) tab[f + FMAX] = exp(-halbK * (double)(2 * f + 1));
    const int zd = 2 * d;
    int32_t I = zustand[0], M = zustand[1], D = zustand[2];
    int64_t nmax = z[3];
    for (int64_t t = 0; t < nschritte; t++) {
        uint64_t r = naechste(rng);
        int k = (int)bis(r, (uint32_t)zd);
        int mu = k >> 1;
        int32_t J = nb[(int64_t)I * zd + k];
        int64_t e;
        int f;
        if ((k & 1) == 0) { e = (int64_t)I * d + mu; f = n[e]; }
        else              { e = (int64_t)J * d + mu; f = -n[e]; }
        int32_t D2 = nb[(int64_t)D * zd + k];
        double a;
        if (f >= -FMAX && f <= FMAX) a = tab[f + FMAX];
        else { a = exp(-halbK * (double)(2 * f + 1)); z[4]++; }
        if (gew) a *= gew[D2] / gew[D];
        z[0]++;
        if (a >= 1.0 || gleich01(rng) < a) {
            if ((k & 1) == 0) n[e] += 1; else n[e] -= 1;
            int64_t an = n[e] < 0 ? -(int64_t)n[e] : (int64_t)n[e];
            if (an > nmax) nmax = an;
            I = J; D = D2;
            z[1]++;
        }
        if (I == M) {
            z[2]++;
            int32_t x = (int32_t)bis(naechste(rng), (uint32_t)V);
            I = x; M = x; /* D bleibt 0 */
        }
        hist[D]++;
    }
    z[3] = nmax;
    zustand[0] = I; zustand[1] = M; zustand[2] = D;
    return 0;
}

/* Wurm mit Paarbildung (S6): dynamische Ladungen q_x in {-1, 0, 1}, Gewicht zf^|q_x|, Gauss-Gesetz
 * div n = q + delta_M - delta_I. Zuege: mit W. 1 - pC Zug A (wie oben, q unveraendert), mit W. pC Zug C:
 * Kopf springt nach I' (gleichverteilt), q_I -= 1, q_I' += 1 (erlaubt, wenn danach |q| <= 1); n unveraendert, das
 * Gauss-Gesetz bleibt erfuellt. Vorschlag symmetrisch (Rueckweg: von I' nach I, gleichverteilt), Annahme
 * min(1, zf^(Delta sum |q|) w(D')/w(D)). Danach Zug B wie oben. Die Mischung pi-erhaltender Kerne erhaelt pi.
 * z wie oben, zusaetzlich z[5] Sprungversuche, z[6] angenommene Spruenge. */
int64_t wurm_paare_laufe(int64_t nschritte, int32_t d, int32_t V, const int32_t *nb, int32_t *n, int8_t *q,
                         int32_t *zustand, const double *gew, double halbK, double zf, double pC, uint64_t *rng,
                         int64_t *hist, int64_t *z) {
    static double tab[2 * FMAX + 1];
    for (int f = -FMAX; f <= FMAX; f++) tab[f + FMAX] = exp(-halbK * (double)(2 * f + 1));
    double zpot[5]; /* zf^k fuer k = -2..2 */
    zpot[0] = 1.0 / (zf * zf); zpot[1] = 1.0 / zf; zpot[2] = 1.0; zpot[3] = zf; zpot[4] = zf * zf;
    const int zd = 2 * d;
    const uint64_t schwelle = (uint64_t)(pC * 18446744073709551616.0);
    int32_t I = zustand[0], M = zustand[1], D = zustand[2];
    int64_t nmax = z[3];
    for (int64_t t = 0; t < nschritte; t++) {
        if (naechste(rng) < schwelle) {
            /* Zug C */
            int32_t J = (int32_t)bis(naechste(rng), (uint32_t)V);
            z[5]++;
            if (J != I) {
                int qa = q[I], qb = q[J];
                int qa2 = qa - 1, qb2 = qb + 1;
                if (qa2 >= -1 && qb2 <= 1) {
                    int dk = (qa2 < 0 ? -qa2 : qa2) - (qa < 0 ? -qa : qa) + (qb2 < 0 ? -qb2 : qb2) - (qb < 0 ? -qb : qb);
                    /* Verschiebung D' = J - M komponentenweise mod L; L = zustand[3] (Kantenlaenge) */
                    int32_t L = zustand[3];
                    int32_t idx = 0, st = 1, jj = J, mm = M;
                    for (int mu = 0; mu < d; mu++) {
                        int32_t cj = jj % L, cm = mm % L;
                        jj /= L; mm /= L;
                        int32_t c = cj - cm; if (c < 0) c += L;
                        idx += c * st; st *= L;
                    }
                    double a = zpot[dk + 2];
                    if (gew) a *= gew[idx] / gew[D];
                    if (a >= 1.0 || gleich01(rng) < a) {
                        q[I] = (int8_t)qa2; q[J] = (int8_t)qb2; I = J; D = idx; z[6]++;
                    }
                }
            }
        } else {
            /* Zug A */
            uint64_t r = naechste(rng);
            int k = (int)bis(r, (uint32_t)zd);
            int mu = k >> 1;
            int32_t J = nb[(int64_t)I * zd + k];
            int64_t e;
            int f;
            if ((k & 1) == 0) { e = (int64_t)I * d + mu; f = n[e]; }
            else              { e = (int64_t)J * d + mu; f = -n[e]; }
            int32_t D2 = nb[(int64_t)D * zd + k];
            double a;
            if (f >= -FMAX && f <= FMAX) a = tab[f + FMAX];
            else { a = exp(-halbK * (double)(2 * f + 1)); z[4]++; }
            if (gew) a *= gew[D2] / gew[D];
            z[0]++;
            if (a >= 1.0 || gleich01(rng) < a) {
                if ((k & 1) == 0) n[e] += 1; else n[e] -= 1;
                int64_t an = n[e] < 0 ? -(int64_t)n[e] : (int64_t)n[e];
                if (an > nmax) nmax = an;
                I = J; D = D2;
                z[1]++;
            }
        }
        if (I == M) {
            z[2]++;
            int32_t x = (int32_t)bis(naechste(rng), (uint32_t)V);
            I = x; M = x;
        }
        hist[D]++;
    }
    z[3] = nmax;
    zustand[0] = I; zustand[1] = M; zustand[2] = D;
    return 0;
}

/* Gauss-Gesetz mit dynamischen Ladungen: Zahl der Plaetze mit div(x) != q_x + delta_M(x) - delta_I(x). */
int64_t gauss_pruefen_q(int32_t d, int32_t V, const int32_t *nb, const int32_t *n, const int8_t *q, int32_t I, int32_t M) {
    const int zd = 2 * d;
    int64_t fehler = 0;
    for (int32_t x = 0; x < V; x++) {
        int64_t dv = 0;
        for (int mu = 0; mu < d; mu++) {
            int32_t xm = nb[(int64_t)x * zd + 2 * mu + 1];
            dv += (int64_t)n[(int64_t)x * d + mu] - (int64_t)n[(int64_t)xm * d + mu];
        }
        int64_t soll = (int64_t)q[x] + (x == M ? 1 : 0) - (x == I ? 1 : 0);
        if (dv != soll) fehler++;
    }
    return fehler;
}

/* Vollpruefung des Gauss-Gesetzes: Zahl der Plaetze mit div(x) != delta_M(x) - delta_I(x). */
int64_t gauss_pruefen(int32_t d, int32_t V, const int32_t *nb, const int32_t *n, int32_t I, int32_t M) {
    const int zd = 2 * d;
    int64_t fehler = 0;
    for (int32_t x = 0; x < V; x++) {
        int64_t dv = 0;
        for (int mu = 0; mu < d; mu++) {
            int32_t xm = nb[(int64_t)x * zd + 2 * mu + 1];
            dv += (int64_t)n[(int64_t)x * d + mu] - (int64_t)n[(int64_t)xm * d + mu];
        }
        int64_t soll = (x == M ? 1 : 0) - (x == I ? 1 : 0);
        if (dv != soll) fehler++;
    }
    return fehler;
}

/* ln V(phi) fuer das Villain-Gewicht, MM Terme je Seite; cm[m] = exp(-2 pi^2 KV m^2), m = 0..MM */
static inline double villain_ln(double phi, double KV, const double *cm, int MM) {
    const double zpi = 6.283185307179586476925286766559;
    phi -= zpi * floor((phi + 0.5 * zpi) / zpi); /* auf [-pi, pi) */
    double q = exp(zpi * KV * phi), qi = 1.0 / q;
    double s = cm[0], qm = 1.0, qim = 1.0;
    for (int m = 1; m <= MM; m++) { qm *= q; qim *= qi; s += cm[m] * (qm + qim); }
    return -0.5 * KV * phi * phi + log(s);
}

/* Villain-Gewicht einzeln (fuer die Pruefung des Abschnitts von aussen) */
double villain_ln_aussen(double phi, double KV, const double *cm, int32_t MM) { return villain_ln(phi, KV, cm, MM); }

/* Villain-Metropolis. th: Winkel (V), lnv: Kantenwerte ln V (V*d, wird hier zu Beginn neu berechnet),
 * stride[mu] = L^mu. Je Durchgang alle Plaetze der Reihe nach; nach jedem Durchgang Messung (wenn messen != 0):
 * korr[mu*(R+1) + r] += sum_x cos(theta_x - theta_{x + r e_mu}), r = 0..R (R = L/2); m2 += |sum_x e^{i theta}|^2 / V^2.
 * z: [0] Versuche, [1] angenommen, [2] Messungen. cs: Arbeitsfeld 2V. */
int64_t villain_laufe(int64_t ndurch, int32_t messen, int32_t d, int32_t L, int32_t V, const int32_t *nb,
                      const int32_t *stride, double *th, double *lnv, double KV, const double *cm, int32_t MM,
                      double hz, double delta, uint64_t *rng, double *korr, double *m2, double *cs, int64_t *z) {
    const int zd = 2 * d;
    const double zpi = 6.283185307179586476925286766559;
    const int R = L / 2;
    for (int32_t x = 0; x < V; x++)
        for (int mu = 0; mu < d; mu++) {
            int32_t y = nb[(int64_t)x * zd + 2 * mu];
            lnv[(int64_t)x * d + mu] = villain_ln(th[y] - th[x], KV, cm, MM);
        }
    double neu_v[16];
    for (int64_t s = 0; s < ndurch; s++) {
        for (int32_t x = 0; x < V; x++) {
            double alt = th[x];
            double tn = alt + delta * (2.0 * gleich01(rng) - 1.0);
            if (tn >= zpi) tn -= zpi;
            if (tn < 0.0) tn += zpi;
            double dS = 0.0; /* Aenderung von ln(Gewicht) */
            for (int mu = 0; mu < d; mu++) {
                int32_t yp = nb[(int64_t)x * zd + 2 * mu];
                int32_t ym = nb[(int64_t)x * zd + 2 * mu + 1];
                double vp = villain_ln(th[yp] - tn, KV, cm, MM);
                double vm = villain_ln(tn - th[ym], KV, cm, MM);
                neu_v[2 * mu] = vp; neu_v[2 * mu + 1] = vm;
                dS += vp - lnv[(int64_t)x * d + mu] + vm - lnv[(int64_t)ym * d + mu];
            }
            if (hz != 0.0) dS += log(1.0 + hz * cos(tn)) - log(1.0 + hz * cos(alt));
            z[0]++;
            if (dS >= 0.0 || gleich01(rng) < exp(dS)) {
                th[x] = tn;
                for (int mu = 0; mu < d; mu++) {
                    int32_t ym = nb[(int64_t)x * zd + 2 * mu + 1];
                    lnv[(int64_t)x * d + mu] = neu_v[2 * mu];
                    lnv[(int64_t)ym * d + mu] = neu_v[2 * mu + 1];
                }
                z[1]++;
            }
        }
        if (messen) {
            double sc = 0.0, ss = 0.0;
            for (int32_t x = 0; x < V; x++) {
                double c = cos(th[x]), si = sin(th[x]);
                cs[2 * x] = c; cs[2 * x + 1] = si; sc += c; ss += si;
            }
            *m2 += (sc * sc + ss * ss) / ((double)V * (double)V);
            for (int mu = 0; mu < d; mu++) {
                int32_t st = stride[mu];
                for (int r = 0; r <= R; r++) {
                    double acc = 0.0;
                    for (int32_t x = 0; x < V; x++) {
                        int32_t xm = (x / st) % L;
                        int32_t ym = xm + r; if (ym >= L) ym -= L;
                        int32_t y = x + (ym - xm) * st;
                        acc += cs[2 * x] * cs[2 * y] + cs[2 * x + 1] * cs[2 * y + 1];
                    }
                    korr[mu * (R + 1) + r] += acc;
                }
            }
            z[2]++;
        }
    }
    return 0;
}
