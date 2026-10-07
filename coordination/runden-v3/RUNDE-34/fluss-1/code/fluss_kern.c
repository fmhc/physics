/* FLUSS-1 (Runde 34): Monte-Carlo-Kerne fuer Pfeile auf den Kanten eines Netzes.
 * Wird von fluss_mc.py innerhalb der Kleintest-Spur mit gcc -O2 uebersetzt und per ctypes geladen.
 *
 * Konvention: Kante e hat kopf[e] (Ende in +n_c-Richtung ihrer Richtungsklasse c) und schwanz[e].
 *   s[e] = +1 heisst: Pfeil schwanz -> kopf; s[e] = -1: Pfeil kopf -> schwanz.
 *   Je Ecke v und Platz k (0..G-1): inz[v*G+k] = Kante, vz[v*G+k] = +1 wenn v kopf dieser Kante ist, sonst -1,
 *   nb[v*G+k] = andere Ecke. Pfeil zeigt in v hinein  <=>  s[e] * vz = +1.
 *   Ladung q_v = sum_k s[e_k] * vz_k = (rein - raus).
 * Netz A (Pyrochlor-Kanten, G = 6): Eisregel q = 0; Defekte q = +2 / -2.
 * Netz B (srs-Netz, G = 3): Regel q in {+1, -1} an jeder Ecke.
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

/* gleichverteilt in [0, n) aus den oberen Bits (Multiplikation, Verzerrung < n / 2^64) */
static inline uint32_t bis(uint64_t r, uint32_t n) { return (uint32_t)(((__uint128_t)r * n) >> 64); }

static inline int ladung(const int8_t *s, const int32_t *inz, const int8_t *vz, int32_t v, int G) {
    int q = 0;
    for (int k = 0; k < G; k++) q += s[inz[v * G + k]] * vz[v * G + k];
    return q;
}

/* alle Ladungen (Kontrolle von aussen) */
void ladungen(const int8_t *s, const int32_t *inz, const int8_t *vz, int32_t nv, int32_t G, int32_t *q_aus) {
    for (int32_t v = 0; v < nv; v++) q_aus[v] = ladung(s, inz, vz, v, G);
}

/* Netz A, Paar-Sektor (zwei Defekte). def[0] = Ecke mit q = +2, def[1] = Ecke mit q = -2.
 * Zug: Defekt w mit W. 1/2, Platz k mit W. 1/6. Der +2-Defekt springt nur ueber einen hineinzeigenden Pfeil,
 * der -2-Defekt nur ueber einen hinauszeigenden: Umklappen, der Defekt sitzt danach an der anderen Ecke.
 * Waere die andere Ecke der Gegendefekt (Vernichtung), wird abgelehnt. Vorschlag symmetrisch, Ablehnung = Bleiben:
 * gleichverteilt ueber alle Zustaende mit genau diesen zwei Defekten.
 * z: 0 angenommen, 1 abgelehnt (Richtung), 2 abgelehnt (Vernichtung), 3 Eisregel-Fehler lokal, 4 Stichproben,
 *    5..8 Untergitter (v % 4) des +2-Defekts in den Stichproben */
int64_t paar_laufe(int64_t nschritte, int32_t m_stich, int8_t *s, const int32_t *inz, const int8_t *vz,
                   const int32_t *nb, const int32_t *koord, int32_t periode, int32_t *def, uint64_t *rng,
                   int64_t *hist, int64_t *z) {
    const int G = 6;
    int32_t countdown = m_stich;
    for (int64_t n = 0; n < nschritte; n++) {
        uint64_t r = naechste(rng);
        int w = (int)(r & 1u);
        int k = (int)bis(r, 6u);
        int32_t v = def[w];
        int32_t slot = v * G + k;
        int32_t e = inz[slot];
        int richtung = s[e] * vz[slot];   /* +1: zeigt in v hinein */
        int soll = (w == 0) ? 1 : -1;
        if (richtung != soll) {
            z[1]++;
        } else {
            int32_t u = nb[slot];
            if (u == def[1 - w]) {
                z[2]++;
            } else {
                s[e] = (int8_t)(-s[e]);
                def[w] = u;
                z[0]++;
                int qa = ladung(s, inz, vz, v, G);
                int qn = ladung(s, inz, vz, u, G);
                if (qa != 0 || qn != 2 * soll) z[3]++;
            }
        }
        if (--countdown == 0) {
            countdown = m_stich;
            int32_t a = def[0], b = def[1];
            int32_t dx = koord[3 * a] - koord[3 * b];
            int32_t dy = koord[3 * a + 1] - koord[3 * b + 1];
            int32_t dz = koord[3 * a + 2] - koord[3 * b + 2];
            if (dx < 0) dx = -dx;
            if (dy < 0) dy = -dy;
            if (dz < 0) dz = -dz;
            if (dx > periode - dx) dx = periode - dx;
            if (dy > periode - dy) dy = periode - dy;
            if (dz > periode - dz) dz = periode - dz;
            hist[dx * dx + dy * dy + dz * dz]++;
            z[4]++;
            z[5 + (a & 3)]++;
        }
    }
    return 0;
}

/* Netz A, Eis-Sektor: n_wuermer geschlossene Wuermer.
 * Je Wurm: eine Kante gleichverteilt umklappen (es entstehen +2 am alten Pfeilanfang, -2 am alten Pfeilende);
 * dann waehlt der +2-Defekt je Schritt einen seiner 6 Plaetze gleichverteilt und springt nur ueber einen
 * hineinzeigenden Pfeil (sonst Bleiben), bis er den -2-Defekt erreicht (Vernichtung, wieder ein Eiszustand).
 * Erweiterter Zustandsraum: Eiszustaende (Gewicht 1) und Zwei-Defekt-Zustaende (Gewicht 6/E), detailliertes
 * Gleichgewicht; die Folge der Eiszustaende nach jedem Wurm ist gleichverteilt (induzierte Kette).
 * z: 0 Versuche, 1 Umklappungen, 2 Wuermer, 3 Eisregel-Fehler lokal, 4 laengster Wurm (Versuche) */
int64_t wurm_laufe(int64_t n_wuermer, int8_t *s, const int32_t *inz, const int8_t *vz, const int32_t *nb,
                   const int32_t *kopf, const int32_t *schwanz, int32_t ne, uint64_t *rng, int64_t *z) {
    const int G = 6;
    for (int64_t w = 0; w < n_wuermer; w++) {
        int32_t e = (int32_t)bis(naechste(rng), (uint32_t)ne);
        int32_t plus, minus;
        if (s[e] > 0) { plus = schwanz[e]; minus = kopf[e]; }
        else          { plus = kopf[e];    minus = schwanz[e]; }
        s[e] = (int8_t)(-s[e]);
        z[1]++;
        {
            int qp = ladung(s, inz, vz, plus, G), qm = ladung(s, inz, vz, minus, G);
            if (qp != 2 || qm != -2) z[3]++;
        }
        int64_t versuche = 0;
        while (1) {
            int k = (int)bis(naechste(rng), 6u);
            int32_t slot = plus * G + k;
            int32_t f = inz[slot];
            versuche++;
            if (s[f] * vz[slot] != 1) continue;
            int32_t u = nb[slot];
            s[f] = (int8_t)(-s[f]);
            z[1]++;
            int qa = ladung(s, inz, vz, plus, G);
            int qn = ladung(s, inz, vz, u, G);
            if (u == minus) {
                if (qa != 0 || qn != 0) z[3]++;
                break;
            }
            if (qa != 0 || qn != 2) z[3]++;
            plus = u;
        }
        z[0] += versuche;
        z[2]++;
        if (versuche > z[4]) z[4] = versuche;
    }
    return 0;
}

/* Netz B (srs, G = 3): n_versuche Vorschlaege, je eine Kante gleichverteilt. Pfeil a -> b darf umklappen, wenn danach
 * beide Enden in {+1, -1} liegen, also genau dann, wenn q_a = -1 und q_b = +1 (danach q_a = +1, q_b = -1).
 * Gleichverteilung ueber alle erlaubten Zustaende (symmetrischer Vorschlag, Ablehnung = Bleiben).
 * q[] wird mitgefuehrt; nach jedem angenommenen Zug werden beide Enden aus s neu berechnet (Kontrolle).
 * z: 0 angenommen, 1 abgelehnt, 2 Regel-Fehler lokal */
int64_t srs_laufe(int64_t n_versuche, int8_t *s, int8_t *q, const int32_t *inz, const int8_t *vz,
                  const int32_t *kopf, const int32_t *schwanz, int32_t ne, uint64_t *rng, int64_t *z) {
    const int G = 3;
    for (int64_t n = 0; n < n_versuche; n++) {
        int32_t e = (int32_t)bis(naechste(rng), (uint32_t)ne);
        int32_t a, b;
        if (s[e] > 0) { a = schwanz[e]; b = kopf[e]; } else { a = kopf[e]; b = schwanz[e]; }
        if (q[a] == -1 && q[b] == 1) {
            s[e] = (int8_t)(-s[e]);
            q[a] = 1; q[b] = -1;
            z[0]++;
            int qa = ladung(s, inz, vz, a, G), qb = ladung(s, inz, vz, b, G);
            if (qa != 1 || qb != -1) z[2]++;
        } else {
            z[1]++;
        }
    }
    return 0;
}
