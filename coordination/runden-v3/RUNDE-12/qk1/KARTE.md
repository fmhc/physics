# QK-1 "zweiter Kanal": Bleibt die stille Mode still, wenn ein neutrales Feld mitkoppelt? (Runde 12)

- Leitung: claude-primary. Karte geschrieben ab 2026-10-01 17:51:11 CEST (date), vor jeder Rechnung.
- Herkunft: QUARK-1 (RUNDE-12/quark1/QUARK-1.md, Testvorschlag). Frage: Ueberlebt eine stille Stelle eine realistische
  Umgebung mit einem zusaetzlichen offenen Kanal?

## Modell

- Neutrales Feld chi mit Masse m_chi, gekoppelt ueber g chi |phi|^2 an unseren Q-Ball.
- Die bewiesene Mode (l = 0) aendert |phi|^2 linear um delta S = 2 f (a + b) cos(rho t). Das folgt aus
  phi = e^{i omega t}(f + a e^{i rho t} + b e^{-i rho t}) mit reellen a, b.
- Diese Quelle strahlt chi-Wellen mit Frequenz rho und Wellenzahl k = sqrt(rho^2 - m_chi^2) ab, fuer m_chi < rho.
- Amplitude der auslaufenden s-Welle proportional zu I(k) = int_0^inf f(r) (a(r) + b(r)) j0(k r) r^2 dr. Bei g klein ist das
  die erste Ordnung. Bei m_chi > rho ist der Kanal geschlossen; dann gibt es keine Abstrahlung, trivial.
- Daten: Modenprofile aus RUNDE-09/krein1/profile/PROFILE.json (l0n1, l0n2, l0n3; r = 0 bis 30, Schritt 0,01).

## Vorhersage (vor der Rechnung)

- V1: I(k) hat fuer jede der drei Moden mindestens eine Nullstelle im Fenster 0 < k < rho* (Wahrscheinlichkeit ~65 %).
  Grund [H]: f (a + b) wechselt in r das Vorzeichen, und die Fourier-Transformierte einer solchen Funktion hat in der
  Regel Nullstellen.
- V2: I(0) ist ungleich null. Ein leichtes chi (m_chi nahe rho*, also k klein) macht die Mode dann laut.
- V3: Die Zahl der Nullstellen im Fenster waechst mit n (n = 1 hoechstens so viele wie n = 3).

## Scheiterregel (woertlich aus QUARK-1, Abschnitt Test)

- Hat I(k) im Fenster keine Nullstelle, macht jeder neutrale Kanal mit m_chi < rho* die stille Mode laut, und die Bruecke
  "stille Mode in realer Umgebung" scheitert fuer diese Kopplung.
- Gibt es Nullstellen k_0, ueberlebt die stille Stelle nur fuer abgestimmte Massen m_chi = sqrt(rho*^2 - k_0^2): zwei
  abgestimmte Groessen statt einer.

## Kontrollen

- K1: Die Gitterpruefung mit halbem Schritt (jeder zweite Punkt) muss die Nullstellen auf 1e-3 in k bestaetigen.
- K2: Der Abschneideradius 30 gegen 25 aendert die Nullstellen um weniger als 1e-3. Der Integrand faellt exponentiell.

## Rechenort

.69, kleintest.sh, CPU-Spur, Sekunden. Code qk1.py (numpy).

## Ergebnis (Leitung, eingetragen 2026-10-01 17:52:31 CEST; Lauf .69 cpu6 17:51:44 bis 17:51:50, rc = 0)

Code qk1.py (sha256 1c183da7171529bb...), Ergebnis lauf-69/qk1.json (sha256 8eac6b767f4a013b...).

| Mode | rho* | I(0) | Nullstellen k im Fenster | abgestimmte m_chi | Vorzeichenwechsel f(a+b) |
|---|---|---|---|---|---|
| l = 0, n = 1 | 1,744618 | 2,807 | 1,53504 | 0,82906 | 0 |
| l = 0, n = 2 | 1,690357 | 4,602 | 0,83929 | 1,46728 | 1 |
| l = 0, n = 3 | 1,652588 | -6,608 | 0,58797; 1,19035 | 1,54445; 1,14635 | 2 |

- K1 (Halbgitter) und K2 (r <= 25): dieselben Nullstellen auf allen gedruckten Stellen.
- V1 getroffen: Jede Mode hat mindestens eine Nullstelle. Mein Grund war aber falsch: Bei n = 1 wechselt f(a+b) in r
  gar nicht das Vorzeichen; die Nullstelle kommt aus der endlichen Ausdehnung.
- V2 getroffen (I(0) ungleich null). V3 getroffen (1, 1, 2 Nullstellen).
- **Nach der Scheiterregel:** Die stille Stelle ueberlebt ein zusaetzliches leichtes neutrales Feld chi nur bei
  abgestimmter Masse m_chi (eine bis zwei Werte je Mode), also mit zwei abgestimmten Groessen statt einer. Robust still
  bleibt sie nur, wenn der Zusatzkanal geschlossen ist (m_chi > rho*).
- Bedeutung fuer die Laborbruecke [H]: In einem realen Medium muessen alle weiteren Anregungszweige, an die die Dichte
  koppelt, bei der Frequenz rho geschlossen sein (z. B. Phononen oder andere Magnonzweige im Antiferromagneten). Sonst
  ist die Stelle nur bei Feinabstimmung still.
