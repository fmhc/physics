/* EIS-1 (Runde 34): Monte-Carlo-Kern fuer klassisches Spin-Eis mit genau zwei Defekten (Q = +1 und Q = -1).
 * Wird von eis_mc.py innerhalb der Kleintest-Spur mit gcc -O2 uebersetzt und per ctypes geladen.
 *
 * Konvention: spin[i] = +1 heisst "zeigt in das obere (up) Tetraeder" (vom down- zum up-Zentrum).
 *   Fuer Tetraeder t: s_t(i) = spin[i] (t oben) bzw. -spin[i] (t unten); "rein" <=> s_t(i) = +1.
 *   Ladung Q_t = sum_i s_t(i) / 2.
 * Zug: Defekt w (0 = plus, 1 = minus) mit W. 1/2, Ecke k seines Tetraeders mit W. 1/4.
 *   plus: nur wenn der Spin dort "rein" zeigt; minus: nur wenn er "raus" zeigt. Dann Umklappen, der Defekt springt ins
 *   Nachbartetraeder dieses Spins. Ist dort der andere Defekt (Vernichtung), wird abgelehnt. Vorschlag symmetrisch,
 *   Ablehnung = Bleiben, also gleichverteilt ueber alle Zustaende mit genau diesen zwei Defekten (T -> 0).
 */
#include <stdint.h>

static inline uint64_t rotl(const uint64_t x, int k) { return (x << k) | (x >> (64 - k)); }

static inline uint64_t naechste(uint64_t *s) { /* xoshiro256** */
    const uint64_t result = rotl(s[1] * 5, 7) * 9;
    const uint64_t t = s[1] << 17;
    s[2] ^= s[0]; s[3] ^= s[1]; s[1] ^= s[2]; s[0] ^= s[3];
    s[2] ^= t; s[3] = rotl(s[3], 45);
    return result;
}

static inline int qsumme(const int8_t *spin, const int32_t *tsite, int32_t t, int32_t nup) {
    int s = spin[tsite[4 * t]] + spin[tsite[4 * t + 1]] + spin[tsite[4 * t + 2]] + spin[tsite[4 * t + 3]];
    return (t < nup) ? s : -s; /* = 2 Q_t */
}

/* zaehler: 0 angenommen, 1 abgelehnt (Orientierung), 2 abgelehnt (Vernichtung), 3 Eisregel-Fehler lokal,
 *          4 Stichproben, 5 plus auf up, 6 minus auf up, 7 gleiche Tetraederart */
int64_t laufe(int64_t nschritte, int32_t m_stich, int8_t *spin, const int32_t *tsite, const int32_t *tup,
              const int32_t *tdown, const int32_t *tkoord, int32_t nup, int32_t periode, int32_t *defekt,
              uint64_t *rng, int64_t *hist, int64_t *z) {
    int32_t countdown = m_stich;
    for (int64_t n = 0; n < nschritte; n++) {
        uint64_t r = naechste(rng);
        int w = (int)(r & 1u);
        int k = (int)((r >> 1) & 3u);
        int32_t t = defekt[w];
        int32_t i = tsite[4 * t + k];
        int oben = t < nup;
        int s = oben ? spin[i] : -spin[i];
        int soll = (w == 0) ? 1 : -1;
        if (s != soll) {
            z[1]++;
        } else {
            int32_t tn = oben ? tdown[i] : tup[i];
            if (tn == defekt[1 - w]) {
                z[2]++;
            } else {
                spin[i] = (int8_t)(-spin[i]);
                defekt[w] = tn;
                z[0]++;
                int qa = qsumme(spin, tsite, t, nup);
                int qn = qsumme(spin, tsite, tn, nup);
                if (qa != 0 || qn != 2 * soll) z[3]++;
            }
        }
        if (--countdown == 0) {
            countdown = m_stich;
            int32_t a = defekt[0], b = defekt[1];
            int32_t dx = tkoord[3 * a] - tkoord[3 * b];
            int32_t dy = tkoord[3 * a + 1] - tkoord[3 * b + 1];
            int32_t dz = tkoord[3 * a + 2] - tkoord[3 * b + 2];
            if (dx < 0) dx = -dx;
            if (dy < 0) dy = -dy;
            if (dz < 0) dz = -dz;
            if (dx > periode - dx) dx = periode - dx;
            if (dy > periode - dy) dy = periode - dy;
            if (dz > periode - dz) dz = periode - dz;
            hist[dx * dx + dy * dy + dz * dz]++;
            z[4]++;
            z[5] += (a < nup);
            z[6] += (b < nup);
            z[7] += ((a < nup) == (b < nup));
        }
    }
    return 0;
}
