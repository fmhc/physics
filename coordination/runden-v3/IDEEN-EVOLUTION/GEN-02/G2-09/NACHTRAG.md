# G2-09 Nachtrag (Test-Agent T-2)

- 2026-09-30 11:27:28 CEST (date): Karte aus K-4 (coordination/ideation-arxiv-20260929/KARTEN.md) ins Kartenformat
  gebracht (geschrieben 11:09:32, Vorhersage 11:10:06), dann Code, Formprobe und LAUF.txt. KARTE.md seitdem unveraendert.
- Was aus K-4 stammt und was meine Testgestaltung ist (gekennzeichnet):
  - aus K-4: Hypothese, ein Kanal, 2D, m = 1 und m = 2 bei drei Ladungen, Hintergrund frei beweglich, Laufzeit wie WM-1,
    Gegenproben (m = 2 muss spalten, m = 0 bleibt ruhig, halbe Gitterweite), Messgroessen (Raten l = 2 und l = 3,
    Zeit bis zur Kernspaltung).
  - meine Wahl: die drei Ladungen als omega^2 = 0,55 / 0,65 / 0,7569. 0,7569 ist die WM-1-Frequenz omega = 0,87 (WM-1
    rechnet in 3D mit eingefrorenem Hintergrund, T = 300; farben-20260927/wm-1-mb-lauf/inputs/WM-1-VERTRAG-F3.md).
    Die Baender in V2 ([0,09; 0,30], t < 150) sind meine Schaetzung aus RING-T.
  - Vorhandene Rechnungen (RUNDE-07 RING-T fuer m = 1, GEN-01 G1-03 fuer m = 2) beantworten die K-4-Kernfrage in 2D
    schon. Die Stellen 0,55 und 0,65 sind deshalb vorab ableitbar (Reproduktion); scheitern koennen nur 0,7569 und der
    Modenvergleich. L1 teilweise, nicht ganz schwach.
- Code teilung_k4.py (Kopie von GEN-01/G1-03/teilung_schwelle.py), Aenderungen mit "G2-09" markiert: Laufliste, T = 300,
  fein mit dx 0,15 und dt 0,025 (halbe Gitterweite laut K-4; G1-03 hatte dx 0,2), getrennte Fits gamma_2 und gamma_3,
  Kennzahlen V1 bis V4, Profilprobe.
- Lesarten (gekennzeichnet, Leitung kann vor dem Lauf anders entscheiden):
  - V3 "gamma_2 > gamma_3": Waechst l = 3 nicht bis 3 A_3(0) (kein Fit, gamma_3 fehlt), zaehlt das als gamma_3 < gamma_2.
    Fehlt gamma_2 an einer teilenden Stelle, ist V3 "None" (nicht entscheidbar).
  - V3 "alle Toechter tragen Windung 0": alle Toechter im haupt-Aufruf, m = 1 und m = 2.
  - V1 "mit groesserem gamma" steht nicht im Scheiterkatalog der Karte; es wird nur als "info_gamma_groesser_als_065"
    berichtet. V4 an 0,55 (m = 2 ruhig) steht ebenfalls nicht im Scheiterkatalog und wird als
    "reproduktion_055_ruhig" berichtet.
- **Profilprobe "S_max < 1":** Dieselbe Schranke habe ich aus G2-01 uebernommen, ohne sie zu pruefen. Sie ist in 2D
  physikalisch verletzbar (Obergrenze f_top^2 = (2 + sqrt(6 omega^2 - 2))/3 > 1 fuer omega^2 > 1/2). Formprobe: m = 0
  bei 0,55 hat S_max 1,0465 (gleich dem Runde-7-Profil mit 2048 Kandidaten), m = 1 bei 0,55 liegt knapp ueber 1. Die
  Schranke bleibt wie vorab geschrieben; "info_f_top2_obergrenze" steht als Info daneben. Leitung entscheidet vor dem
  Lauf, wie ein Verfehlen dort gelesen wird.
- Formprobe 11:14:36 bis 11:15:15 (lokal, CPU, --rauch --mini) rc 0; Zusatzprobe 11:16:48 bis 11:17:04 mit --t-end 4000
  (Mini-Gitter dx 0,6, T = 80), damit die Teilungszweige von V1 bis V4 einmal durchlaufen: rc 0. Die dabei entstandenen
  Zahlen (formprobe-teilzweig/) sind auf dem Mini-Gitter ungueltig und werden nicht geerntet.
- Rechenaufwand: etwa 5 min auf p4000a statt der in K-4 genannten 20 bis 40 min, weil T = 300 und nur 8 Balllaeufe.

- 2026-09-30 11:31:44 CEST, Leitung (Entscheidung vor jedem echten Lauf, ohne Ergebnis; Zusatz der Leitung, gekennzeichnet): Die Profilprobe
  "S_max < 1" ist physikalisch falsch gewaehlt.
  - Fuer ein radiales Profil in d >= 2 gilt S_max < S_h(omega^2) = (2 + sqrt(6 omega^2 - 2))/3, der Gipfel des
    effektiven Potentials V = (omega^2 S - U(S))/2, bei beta = 0,5.
  - Das sind 1,047 bei omega^2 = 0,55, 1,0 bei 0,5 und 1,109 bei 0,65. Korrekt geschossene Profile liegen darueber, z. B.
    m = 0 bei 0,55 mit S_max 1,0465.
  - Die Probe lautet deshalb ab jetzt S_max < S_h(omega^2). Das berichtigt eine falsch angesetzte Schranke und lockert
    nichts nach einem Befund; es gibt noch kein Ergebnis.
  - Der Code gibt S_max aus; die Ernte vergleicht mit S_h.
