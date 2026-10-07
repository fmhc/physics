# NETZ-DYN-1: Ergebnis (Bau- und Rechenagent, Claude-Subagent fuer die Leitung claude-primary)

- Arbeit ab 2026-10-06 20:23:48 CEST (date). Vorab-Datei VORAB.md 20:31:10 (vor dem ersten Lauf), Nachtrag fuer die
  zweite Welle 21:23:40 (vor deren Ergebnissen). Erste Rechnung 20:43:49. Abschluss: siehe Fuss.
- Synthetisch, keine Messdaten. Karte (D1 bis D7) unveraendert.
- Rohdaten: lauf-69/ (JSON je Lauf, Logs, Kettenskripte in lauf-69/ketten/), Code: code/, Pruefsummen: PRUEFSUMMEN.txt.

## Ergebnis zuerst

1. **Gebaut und geprueft; Stufen S0, S1, S2 durchlaufen, aber nur bei kleinen Volumina.** Ein Kern rechnet 1+1D,
   3+1D mit Zeitschichten (CDT) und 4D ohne Schichten (DT). Alle sieben Zugarten nach AJL werden angenommen, Zug und
   Umkehrzug gleich haeufig, und alle Pruefungen sind in jedem Lauf bestanden: Mannigfaltigkeit, Schichten, Euler-Zahlen,
   Feldkonsistenz. U(1), SU(2) und Rahmen wirken ueber exakte Rosenbluth-Gewichte auf die Geometrie zurueck.
2. **D1 (1+1D) knapp verfehlt.** d_s = 2,00 bis 2,02 bei grossen sigma, wie die Literatur. Die Hausdorff-Dimension liegt
   aber knapp ueber dem Fenster 1,8 bis 2,2: Groessenskalierung des mittleren Abstands 2,23 (N2 = 4000 gegen
   16000), lokale Steigung der Schalen 2,30 bis 2,35 bei beiden Groessen. Das flache Kontrollnetz gibt mit derselben
   Methode genau 2,000.
3. **D2 und D3 nicht entschieden: Die Volumina sind zu klein.** CDT bei (k0, Delta) = (2,2; 0,6) und (2,2; 0,0) hat ein
   d_s-Maximum von 4,1 bei sigma ~ 100. Ebenso liegen DT ohne Schichten (3,9 bis 4,2) und das unveraenderte Startnetz
   (3,9). Ein Plateau gibt es nirgends, auch nicht bei N4 ~ 23000: Dort liegt das Maximum bei 4,23 (sigma 108), es ist
   breiter, aber kaum hoeher; das Startnetz gleicher Groesse hat 3,91. Das Maximum bildet also die Groesse des kleinen
   4D-Torus ab; die Dynamik hebt es nur um 0,24 (N4 ~ 7000) bzw. 0,32 (N4 ~ 23000) ueber das Startnetz. Bei k0 = 5,0 sinkt es
   auf 3,7, die Profile streuen staerker und Superpunkte erscheinen. Das ist eine k0-Abhaengigkeit, aber keine
   aufgeloeste Phasengrenze.
4. **Felder: starke Rueckwirkung, D4 im Wortlaut gescheitert und nicht konventionsfrei, D5 im Maximumsbereich
   eingetroffen.** Der Einbau einer Ecke ((2,8)-Zug) kostet mit U(1) (beta = 2) und Rahmen (J = 1) im Mittel -14,9 im
   Logarithmus des Gewichts, mit dem Rahmen allein -3,1, mit SU(2) (beta = 2,5) -21,0. Die Lage gleicher Eckenbilanz
   verschiebt sich dadurch grob um dk0 ~ +6 bis +8 (U(1) + Rahmen), ~ +6 (SU(2)) bzw. ~ +3 (Rahmen). Das ist weit ueber 10 % von
   k0 = 2,2. Diese Verschiebung ist aber so gross wie die Normierungskonvention des Feldmasses (3 ln 2 pi = 5,5;
   ln 2 pi^2 = 3,0) und daher keine konventionsfreie Phasenaussage. Mit Feldern bei k0 = 10,2 stellt sich N0/N4 = 0,040 bis 0,041 ein wie ohne Felder bei k0 = 2,2, und (2,8) und (8,2) sind wieder im Gleichgewicht (3838 / 3881 statt 5 / 136); die Abschaetzung stimmt also grob. Der Rahmen
   allein aendert d_s bei sigma 10 bis 120 um hoechstens 0,21, im Abfall (sigma 200) um 0,47.
5. **Superpunkte (D6, D7).** Im geschichteten Netz bei k0 = 2,2 gibt es keine, mit und ohne Felder; der groesste Grad
   bleibt unter dem 4-Fachen des Mittels (Schwelle 5). Ohne Schichten (DT) und bei k0 = 5,0 treten sie auf, mit Lebensdauern
   bis 976 Sweeps (DT) bzw. 174 Sweeps (CDT). Alle Superpunkte am Ende der Laeufe sind Ecken des Startnetzes, deren Grad gewachsen ist, waehrend neue Ecken kleiner
   Ordnung den Mittelwert senkten; keine neue Ecke wurde Superpunkt. Das spricht fuer einen Rest des Starts plus
   relative Schwelle, nicht fuer von selbst entstehende Superpunkte. Die U(1)-Ladung ist an allen gemessenen gewoehnlichen Ecken
   exakt 0. An Superpunkten mit U(1) gab es keine Messung, weil in den Feldlaeufen keine Superpunkte entstanden: D7 ist
   nicht pruefbar.

## Aufbau

- **Paket:** code/netzdyn.py (Kern, Laeufe, Messungen), code/auswertung.py (Tabellen), code/sp_herkunft.py (Herkunft der
  Superpunkte). ew.py und tp.py sind unveraendert aus ueberleitung-v-1/code kopiert (nur fuer Finns Netz V; sha256 wie
  dort). Auf der .69 liegt alles in /home/fmh/fmhc-physics-remote/netz-dyn-1/ (code/, aus/, stand/, logs/, kette-*.sh).
- **Ein dimensionsfreier Kern:** Simplizes als sortierte Eckentupel, jede Ecke hat eine Zeitschicht (periodisch,
  T Schichten). Derselbe Code rechnet 1+1D (d = 2), 3+1D (d = 4) und 4D ohne Schichten.
- **Zeitartige Zuege** = Pachner-Zuege im Raumzeit-Netz: in 4D 2-4, 3-3, 4-2 (bei AJL (2,4), (3,3), (4,2)), in 2D 2-2.
  Ein Zug wird nur angenommen, wenn:
  - der Stern der Teilflaeche die richtige Groesse hat,
  - die neue Gegenflaeche noch nicht existiert,
  - alle neuen Simplizes genau zwei benachbarte Schichten beruehren,
  - weder die entfernte noch die neue Teilflaeche raumartig ist (damit bleibt jede Schicht unveraendert).
- **Raumartige Zuege** = Pachner-Zuege in der Schicht, hochgehoben auf die Kegel darueber und darunter. Aus 3D 1-4, 2-3,
  3-2, 4-1 werden (2,8), (4,6), (6,4), (8,2); in 2D wird 1-2 bzw. 2-1 zu (2,4) bzw. (4,2). Bedingung: Der volle 4D-Stern
  der Schichtflaeche besteht nur aus den Kegeln, mit je einer gemeinsamen Spitze oben und unten.
- **Zugliste [L]:** Ambjoern, Jurkiewicz, Loll, aus dem Gedaechtnis. Die Ergodizitaet ist eine Annahme; die Pruefung im
  Kleinen steht unter Kontrollen.
- **Wirkung (Zaehlform):**
  - 4D-CDT: S = -(k0 + 6 Delta) N0 + k4 N4 + Delta (2 N41 + N32) + eps (N4 - Nz)^2.
  - 2D: S = lam N2 + eps (N2 - Nz)^2.
  - 4D ohne Schichten (DT): S = -k0 N0 + k4 N4 + eps (N4 - Nz)^2.
  - k4 (bzw. lam) wird in der Thermalisierung auf das Zielvolumen nachgefuehrt und dann festgehalten.
- **Metropolis:** zufaelliges Simplex, zufaellige Teilflaeche, Annahme min(1, N/N' exp(-dS) Feldfaktor). Der Faktor N/N'
  folgt daraus, dass sich die Auswahlwahrscheinlichkeiten von Zug und Umkehrzug fuer jede Zugart genau so verhalten.
  Nachgerechnet fuer (2,8)/(8,2), (4,6)/(6,4), 2-4/4-2, 3-3 und 1-5/5-1. Ein Sweep = N Vorschlaege.
- **Start 3+1D:** Finns gefuelltes Netz V (ew.geometrie('V'): 10 Ecken, 58 Tetraeder je Zelle), periodisch 2x2x2 Zellen
  (80 Ecken, 464 Tetraeder je Schicht), T = 4 Schichten.
  - Treppenzerlegung Tetraeder x Intervall nach globaler Eckenordnung (je Tetraeder ein (4,1), (3,2), (2,3), (1,4)):
    N4 = 7424, N0 = 320, Topologie T^3 x S^1.
  - Groesserer Lauf: 3x3x3 Zellen, N4 = 25056.
  - Eine Zelle allein ist kein Simplizialkomplex (periodische Bilder fallen zusammen), deshalb ab 2x2x2.
- **Felder mit Rueckwirkung** (einzeln zuschaltbar):
  - U(1)-Winkel auf Kanten, Wilson-Wirkung ueber alle Dreiecke mit Gewicht w = 1 (keine Hodge-Gewichte):
    S = bu Summe (1 - cos F).
  - SU(2) auf Kanten (Einheitsquaternionen): S = bs Summe (1 - 1/2 Tr U_Dreieck).
  - SU(2)-Rahmen an den Ecken als O(4)-Rotor mit Nachbarkopplung: S = J Summe_Kanten (1 - R_a . R_b). Das ist nicht
    Variante C aus GERAHMTER-FADEN-1 (Kopplungsgesetz plus Hebungsbuchhaltung); die ist nicht nachgebaut.
  - Neue Kanten bzw. Ecken eines Geometriezugs bekommen ihren Wert aus dem bedingten Waermebad (feste Reihenfolge).
  - Dessen Normierung (Bessel I0 bzw. 2 I1(x)/x) geht als Rosenbluth-Gewicht exakt in die Annahme ein, beim Umkehrzug
    umgekehrt. Die Feldwirkung wirkt damit ohne Naeherung auf die Geometrie zurueck.
  - Mass Haar-normiert (dtheta/2 pi je Kante); nach jedem Geometrie-Sweep ein Waermebad-Sweep ueber alle Kanten und Ecken.
  - Torsion: nicht gebaut.
- **Messgroessen:**
  - Profil N3(t) (raumartige Tetraeder je Schicht).
  - Schalen n(r) im dualen Netz, lokale Hausdorff-Dimension d_H(r) = 1 + dln n/dln r.
  - Rueckkehrwahrscheinlichkeit P(sigma) einer traegen Diffusion (Haltewahrscheinlichkeit 1/2) im dualen Netz,
    d_s(sigma) = -2 dlnP/dln sigma; exakte Verteilungsrechnung, 24 Startpunkte je Messung.
  - Grad je Ecke; Superpunkte (Grad > 5 x Mittel) mit Lebensdauer in Sweeps, gemessen alle 2 Sweeps.
  - Um Ecken: U(1)-Ladung = DeGrand-Toussaint-Fluss durch die raeumliche Huelle, also den Link der Ecke in ihrer
    Schicht (eine 2-Sphaere). Die Orientierung kommt aus einer globalen 4D-Orientierung. Dazu die Igelzahl der
    Rahmenachse R e_z R^-1 auf derselben Huelle.
  - Plakette, Rahmenordnung. Polyakov-Schleife: nicht gebaut.
- **Laeufe:** ueber kleintest.sh auf cpu8 bis cpu11, je Abschnitt hoechstens 540 s (Laufzeit bis 556 s, Grenze 600 s).
  Zwischenstand per pickle (neue Datei + mv, nur der letzte, je 0,5 bis 1,5 MB), df vor jedem Abschnitt (stets 17 GB frei).

## Kontrollen

- **Pruefung im Lauf** (Netz.pruefe, alle 300 bis 500 Sweeps und am Ende). Geprueft wird:
  - jede Facette in genau zwei Simplizes, Sternlisten konsistent, alle Simplizes kausal;
  - jedes raumartige Tetraeder (bzw. jede Ringkante) genau einmal Boden eines (4,1) und einmal Dach eines (1,4);
  - Euler-Zahl der Raumzeit 0 und jeder Schicht 0 (T^3 bzw. Ring);
  - Feldschluessel = Kanten bzw. Ecken.
  - **In allen Laeufen bestanden** (kein Abbruch, chi = 0, chi_schicht = 0 am Ende jedes Laufs).
- **Alle Zugarten angenommen, Zug und Umkehrzug gleich haeufig** (Zeichen des Gleichgewichts):
  - S1-A nach 5189 Sweeps: (2,8) 26552 / (8,2) 26588; (4,6) 8592 / (6,4) 8984; (2,4) 140899 / (4,2) 140688;
    (3,3) 279171.
  - 1+1D (N2 = 16000): (2,4) 891413 / (4,2) 891449; (2,2) 2403031.
  - DT k0 = 2,6: 1-5 101074 / 5-1 100615; 2-4 67667 / 4-2 68545; 3-3 131865.
- **Messmethoden am regulaeren Netz:**
  - 1+1D, flacher Torus (N2 = 16000, T = 80): lokale d_H(r) = 2,000 fuer r = 4 bis 50, d_s = 2,00 (sigma 100 bis 590).
  - 4D-Startnetz V x S^1 ohne Dynamik: d_s-Maximum 3,91 (T = 4, N4 = 7424), 3,96 (T = 8), 3,93 (T = 16) und 3,91 (3x3x3, N4 = 25056), jeweils
    bei sigma 64 bis 85, danach Abfall (Torus). Das ist die Vergleichslinie fuer alle 4D-d_s-Werte.
- **Ladung und Igelzahl:** an 672 gewoehnlichen Ecken (F1, F4, F1b) fuer die Ladung und an 928 (dazu F2) fuer die Igelzahl
  ganzzahlig auf 2e-15 (alle 0). Die
  globale 4D-Orientierung hat 0 Widersprueche (T^3 x S^1 wird als orientierbar erkannt).
- **Codefassungen:** Zuege, Annahme und Messungen blieben ab dem ersten Lauf unveraendert. Spaetere Fassungen von
  netzdyn.py fuegten nur Optionen und Protokollfelder hinzu: Startmessung, k0-Nachfuehrung, Feldgewicht-Protokoll,
  Fortsetzung mit neuen Kopplungen, Messneustart, Felder entfernen. Jeder Abschnitt lud die zu seinem Start gueltige
  Fassung; die Endfassung (sha256 in PRUEFSUMMEN.txt) liest alle Zwischenstaende.
- **Startunabhaengigkeit (s1x-unten):** Der Endzustand des Feldlaufs F1 (N0 = 189, N0/N4 = 0,029) laeuft ohne Felder bei
  (2,2; 0,6) weiter. N0 steigt von 189 auf 265 bis 272; ueber 2705 Sweeps sind N0/N4 = 0,037 und N41/N4 = 0,38 wie bei
  S1-A (0,037; 0,39), und die d_s-Kurve stimmt auf 0,06 ueberein (Maximum 4,20 gegen 4,15). Die Startunabhaengigkeit
  ist damit von unten bestanden (nur dieses eine Paar).

## Tabellen

### S0: 1+1D (Kontrolle D1)

| Lauf | N2 | T | Sweeps (Messbereich) | d_H lokal, r 6 bis 20 | mittlerer Abstand <r> (duales Netz) | d_s (sigma 30) | d_s (sigma 100) | d_s (sigma 590) |
|---|---|---|---|---|---|---|---|---|
| flach (Startnetz) | 16000 | 80 | 0 | 2,000 | (abgeschnitten) | 2,01 | 2,00 | 2,00 |
| s0a2 | 15939 | 80 | 900 bis 1605 (464 Schalen) | 2,35 | 56,27 | 1,84 | 1,95 | 2,02 |
| s0b | 3984 | 40 | 300 bis 2671 (752 Schalen) | 2,30 | 30,30 | 1,85 | 1,94 | 2,00 |
| s0b2 | 3982 | 40 | 2671 bis 4427 (1136 Schalen) | 2,33 | 30,22 | 1,85 | 1,96 | 2,00 |

- Groessenskalierung bei festem T/Wurzel(N2) = 0,63: d_H = ln(N_a/N_b) / ln(<r>_a/<r>_b) = 2,23.
- s0a (erster Abschnitt, Schalen bei r = 60 abgeschnitten) bestaetigt die lokale Steigung: Mittel 2,33 (r 6 bis 20).

### S1 und D3: 4D ohne Felder, Startnetz und DT

Spalten: Sweeps, Zahl der d_s-Messungen (n_P), Mittel N4, N0/N4, N41/N4, k0, k4 (fest nach der Thermalisierung),
relative Streuung des Profils, mittlerer und groesster Grad, Superpunkte je Messung, d_s bei sigma = 10/30/80/120/200,
Maximum (bei sigma).

| Lauf | Sweeps | n_P | N4 | N0/N4 | N41/N4 | k0 | k4 | Profil | Grad mittel | Grad max | SP | d_s 10 | 30 | 80 | 120 | 200 | max (sigma) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Startnetz T = 4 (keine Dynamik) | 0 | 1 | 7424 | 0,043 | 0,50 | - | - | 0 % | 29,2 | 38 | 0 | 3,23 | 3,74 | 3,91 | 3,60 | 1,99 | 3,91 (72) |
| S1-A CDT (2,2; 0,6) | 5189 | 95 | 7084 | 0,037 | 0,39 | 2,2 | 0,84 | 4,3 % | 33,3 | 80 | 0 | 2,74 | 3,38 | 4,08 | 4,12 | 2,91 | 4,15 (104) |
| S1-B CDT (2,2; 0,0) | 5020 | 92 | 7221 | 0,038 | 0,41 | 2,2 | 1,36 | 5,8 % | 32,4 | 84 | 0 | 2,71 | 3,27 | 3,95 | 4,07 | 3,18 | 4,08 (113) |
| S1-C CDT (5,0; 0,6) | 4618 | 84 | 7443 | 0,060 | 0,52 | 5,0 | 0,93 | 7,1 % | 23,0 | 87 | 0,52 | 2,59 | 2,85 | 3,38 | 3,64 | 3,56 | 3,71 (151) |
| Startnetz 3x3x3, T = 4 (keine Dynamik) | 0 | 1 | 25056 | 0,043 | 0,50 | - | - | 0 % | 29,2 | 38 | 0 | 3,25 | 3,81 | 3,90 | 3,80 | 3,40 | 3,91 (64) |
| S1-L3 CDT (2,2; 0,6), 3x3x3 | 2545 | 42 | 23140 | 0,035 | 0,39 | 2,2 | 0,84 | 1,7 % | 35,1 | 70 | 0 | 2,82 | 3,56 | 4,17 | 4,22 | 3,88 | 4,23 (108) |
| s1x-unten CDT (2,2; 0,6), Start: Ende F1 | 2705 | 46 | 6977 | 0,037 | 0,38 | 2,2 | 0,84 | 5,6 % | 33,3 | 82 | 0 | 2,68 | 3,36 | 4,12 | 4,17 | 2,97 | 4,20 (105) |
| DT k0 = 1,5 | 2252 | 37 | 7642 | 0,053 | - | 1,5 | 1,52 | - | 25,2 | 96 | 0,23 | 2,43 | 3,06 | 4,00 | 4,23 | 3,66 | 4,23 (125) |
| DT k0 = 2,6 | 2282 | 37 | 7702 | 0,076 | - | 2,6 | 1,62 | - | 19,5 | 108 | 8,69 | 2,25 | 2,71 | 3,57 | 3,95 | 4,08 | 4,14 (171) |
| DT k0 = 4,0 | 2268 | 37 | 7770 | 0,099 | - | 4,0 | 1,86 | - | 16,4 | 99 | 16,0 | 2,10 | 2,48 | 3,31 | 3,68 | 3,92 | 3,93 (194) |

- Lokale d_H(r) aus den Schalen steigt in allen 4D-Laeufen und im Startnetz bis etwa 4,2 bis 4,5 bei r = 6 bis 8 und
  faellt dann; der Durchmesser des dualen Netzes ist nur etwa 12 bis 14. Bei dieser Groesse ist d_H nicht bestimmbar.
- Die DT-Laeufe driften am Ende noch (N0 steigt: k0 = 2,6 von 733 auf 787, k0 = 4,0 auf 1000). S1-A/S1-B: N0 pendelt
  nach etwa 2500 Sweeps zwischen 230 und 300. S1-C: N0 steigt noch (590 am Ende).

### S2: Felder bei Delta = 0,6 (F1 bis F3, F1b) bzw. 0,0 (F4)

| Lauf | Felder | k0 | k4 | Sweeps | N4 | N0/N4 (Ende) | Plakette | Rahmen m / <R.R> | d_s 10 | 30 | 80 | 120 | 200 | max (sigma) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S1-A (Vergleich) | keine | 2,2 | 0,84 | 5189 | 7084 | 0,037 (0,041) | - | - | 2,74 | 3,38 | 4,08 | 4,12 | 2,91 | 4,15 (104) |
| F1 | U(1) 2 + Rahmen 1 | 2,17 | -0,05 | 2093 | 6910 | 0,034 (0,029) | 0,929 | 0,947 / 0,916 | 2,87 | 3,62 | 4,15 | 3,94 | 2,30 | 4,16 (84) |
| F2 | Rahmen 1 | 2,31 | 0,89 | 1900 | 7142 | 0,033 (0,028) | - | 0,948 / 0,919 | 2,86 | 3,59 | 4,16 | 3,99 | 2,44 | 4,16 (87) |
| F3 | SU(2) 2,5 | 2,16 | -1,28 | 785 | 7658 | 0,038 (0,035) | 0,826 | - | 2,92 | 3,61 | 4,06 | 3,96 | 2,56 | 4,08 (92) |
| F1b | U(1) 2 + Rahmen 1 | 10,2 | -0,06 | 968 | 7310 | 0,041 (0,040) | 0,927 | 0,919 / 0,901 | 2,88 | 3,53 | 4,10 | 4,00 | 2,54 | 4,13 (92) |
| F4 (Delta 0) | U(1) 2 + Rahmen 1 | 2,2 | 0,49 | 2105 | 6831 | 0,031 (0,027) | 0,929 | 0,949 / 0,921 | 2,86 | 3,56 | 4,11 | 3,94 | 2,39 | 4,12 (87) |

Mittlere Logarithmen der Feldgewichte je Zugart (Rueckwirkung; negativ = der Zug wird durch die Felder unterdrueckt):

| Lauf | (2,8) | (8,2) | (2,4) | (4,2) | (4,6) | (6,4) | (3,3) |
|---|---|---|---|---|---|---|---|
| F1 U(1) + Rahmen | -14,88 | +12,44 | -2,33 | +2,28 | -2,40 | +2,29 | -0,07 |
| F4 U(1) + Rahmen, Delta 0 | -14,87 | +12,54 | -2,33 | +2,27 | -2,40 | +2,28 | -0,07 |
| F2 Rahmen | -3,14 | +3,13 | -0,09 | +0,08 | -0,09 | +0,09 | 0 |
| F3 SU(2) | -20,95 | +17,87 | -4,56 | +4,43 | -4,76 | +4,48 | -0,20 |

### Superpunkte (Grad > 5 x Mittel, Messung alle 2 Sweeps)

| Lauf | je Messung | Episoden | davon > 10 Sweeps | laengste (Sweeps) | Herkunft |
|---|---|---|---|---|---|
| alle CDT-Laeufe bei k0 = 2,2 (S1-A, S1-B, S1-L3, s1x-unten, F1 bis F4) und F1b | 0 | 0 | 0 | - | - |
| S1-C (CDT, k0 = 5,0) | 0,52 | 177 | 41 | 174 | am Ende 5 von 5 Startecken |
| DT k0 = 1,5 | 0,23 | 45 | 12 | 78 | am Ende 2 von 2 Startecken |
| DT k0 = 2,6 | 8,69 | 717 | 201 | 976 | am Ende 38 von 38 Startecken |
| DT k0 = 4,0 | 16,0 | 1228 | 372 | 886 | am Ende 51 von 51 Startecken |

## Abgleich mit der Karte (beschreibend)

- **D1** (1+1D, d_H 2,0 +- 0,2; 85 %): **knapp verfehlt.**
  - d_s = 2,00 bis 2,02 bei sigma >= 200 wie erwartet.
  - Die Hausdorff-Dimension liegt mit beiden Schaetzern knapp darueber: Groessenskalierung 2,23, lokale Steigung
    2,30 bis 2,35 bei N2 = 4000 und 16000. Das flache Kontrollnetz gibt mit derselben Methode 2,000.
  - Die Groessenskalierung ist durch die Wahl T ~ Wurzel(N2) teilweise vorgegeben [M], also ein schwacher Test.
  - Ob der Ueberschuss eine Korrektur kleiner Volumina ist (die Literatur hat d_H = 2 exakt [L]) oder aus dem Code
    kommt, ist nicht geprueft. Die Pruefungen, das Zuggleichgewicht und d_s = 2,0 sprechen gegen einen Fehler in
    Zuegen oder Annahme, schliessen ihn aber nicht aus.
- **D2** (3+1D mit Schichten: ausgedehnter Bereich, d_s 3,5 bis 4,5 bei grossen Zeiten; 25 %): **nicht entschieden.**
  - Bei N4 ~ 7000 hat d_s ein Maximum um 4,1, bei N4 ~ 23000 eines von 4,23 (sigma 108, breiter); danach faellt d_s.
    Ein Plateau gibt es nicht. Das Startnetz gleicher Groesse hat jeweils 3,91; die Dynamik hebt das Maximum um 0,24 bzw.
    0,32 und senkt d_s bei kleinen sigma.
  - Dem Wortlaut nach liegt damit der Scheiterfall "kein stabiles Plateau" vor. Dasselbe Maximum zeigen aber das
    unveraenderte Startnetz (3,9) und DT (3,9 bis 4,2). Es liegt also an der Groesse, nicht an Finns Regeln.
  - Eine Phasengrenze ist nicht aufgeloest. Bei k0 = 5,0 sinkt das Maximum auf 3,7, die Profilstreuung steigt von 4 auf
    7 %, und Superpunkte erscheinen. Das ist eine Richtung, aber kein Phasenbefund.
  - Bei kleinen sigma liegt d_s im dynamischen Netz unter dem Startnetz (2,7 gegen 3,2 bei sigma = 10). Ob das die aus
    der Literatur bekannte Absenkung bei kleinen Abstaenden ist [L] oder Gitterrauhigkeit, ist nicht trennbar.
- **D3** (3+1D ohne Schichten: kein Bereich mit d_s 3,5 bis 4,5; 70 %): **nicht entschieden.**
  - DT hat Maxima von 4,23 (k0 = 1,5), 4,14 (2,6) und 3,93 (4,0), kein Plateau.
  - Woertlich "tritt ein solcher Wert auf", aber nur als dasselbe Torusmaximum wie beim Startnetz.
  - Mit wachsendem k0 wandert das Maximum zu groesserem sigma, und d_s bei kleinen sigma sinkt (Richtung verzweigte
    Polymere [L]). Die Laeufe driften aber noch.
- **D4** (U(1) beta = 2 und SU(2) ueber beta_c verschieben die Phasengrenze um < 10 %; 55 %): **im Wortlaut gescheitert,
  aber nicht konventionsfrei; eine Phasengrenze wurde nicht bestimmt.**
  - Gerechnet: die Rueckwirkung auf die Eckenbilanz. Ein (2,8)-Zug kostet mit U(1) + Rahmen -14,9, mit dem Rahmen allein
    -3,1, mit SU(2) -21,0 im mittleren Log-Gewicht.
  - Bei festem k0 = 2,2 faellt N0/N4 mit Feldern von 0,037 (Mittel ohne Felder) auf 0,027 bis 0,029 am Ende (mit SU(2) 0,035). Die Volumen-Nachfuehrung
    verschiebt k4 um -0,9 (U(1) + Rahmen) bzw. -2,1 (SU(2)).
  - Abschaetzung fuer gleiche Eckenbilanz (Mittel der Betraege von (2,8) und (8,2) minus 6 x halbes (2,4)-Gewicht):
    dk0 ~ +6 bis +8 (U(1) + Rahmen), ~ +6 (SU(2)), ~ +3 (Rahmen). Test bei k0 = 10,2 (F1b): N0/N4 = 0,041 (Ende 0,040) wie ohne Felder, (2,8) / (8,2) wieder im Gleichgewicht (3838 / 3881; bei k0 = 2,2 nur 5 / 136). Die d_s-Kurve aendert sich dabei gegen F1 bei sigma 10 bis 120 um hoechstens 0,09, bei sigma 200 um +0,24.
  - Aus dem Aufbau [M]: Ueber Dehn-Sommerville (N1 = 3 N0 + N4/2, N2 = 2 N0 + 2 N4 bei chi = 0) verschiebt jede
    extensive Feld-Freie-Energie k0 und k4. Schon die Wahl dtheta statt dtheta/2 pi je Kante verschiebt k0 um 3 ln 2 pi =
    5,5 und k4 um -0,92; fuer SU(2) bzw. Rahmen sind es 3 ln 2 pi^2 = 8,9 bzw. ln 2 pi^2 = 3,0.
  - Eine Verschiebung "in % der nackten Kopplung" haengt damit von der Normierung ab. Sinnvoll waere der Vergleich bei
    gleicher Physik (gleiches N0/N4, gleiche Profilform); dafuer war die k0-Nachfuehrung zu traege.
- **D5** (Rahmen aendert d_s um < 0,3; 60 %): **im Bereich des Maximums eingetroffen, vorlaeufig.**
  - F2 gegen S1-A, gleiche nackte Kopplungen: Differenzen +0,12 / +0,21 / +0,08 / -0,13 bei sigma = 10 / 30 / 80 / 120,
    aber -0,47 bei sigma = 200 im Abfall.
  - Die N0/N4 unterscheiden sich (0,033 gegen 0,037), und D2 ist nicht entschieden.
  - Zwischen den beiden S1-A-Abschnitten schwankt d_s selbst um 0,05 bis 0,23. Die Grenze 0,3 liegt also nur knapp
    ueber der eigenen Streuung.
- **D6** (in der ausgedehnten Phase keine stabilen Superpunkte, in zerknuellten schon; 60 %): **Muster teilweise wie
  erwartet, Bezug offen.**
  - Im geschichteten Netz bei k0 = 2,2 keine, mit und ohne Felder (groesster Grad unter 4 x Mittel).
  - Ohne Schichten und bei k0 = 5,0 schon, und zwar gerade auf der Seite grosser k0 (viele neue Ecken kleiner Ordnung
    senken den Mittelwert), nicht nur im zerknuellten Bereich.
  - Herkunft (code/sp_herkunft.py, letzter Zwischenstand): Alle Superpunkte sind Ecken des Startnetzes (Ids < 320), in
    S1-C 5 von 5, in DT 2 von 2, 38 von 38 und 51 von 51. Ihr Grad ist von hoechstens 38 im Startnetz auf bis zu 149
    gewachsen. Auch in den CDT-Laeufen ohne Superpunkte sind die Ecken mit den hoechsten Graden alle Startecken. Neue Ecken
    wurden nie Superpunkte, und Startecken werden praktisch nie entfernt. Das ist ein Gedaechtnis des Starts zusammen mit
    der relativen Schwelle, kein Beleg fuer von selbst entstehende Superpunkte.
  - Ob k0 = 2,2 die "ausgedehnte Phase" ist, bleibt offen (D2).
- **D7** (Ladung um Superpunkte im Mittel 0; 70 %): **nicht pruefbar.**
  - In den Laeufen mit U(1) entstanden keine Superpunkte. In DT ist eine Ladung um eine Ecke nicht definiert, weil die
    Huelle dort eine 3-Sphaere ist.
  - An 672 gewoehnlichen Ecken ist Q = 0, an 928 die Igelzahl 0 (beta = 2 und J = 1: geordnet, keine Dirac-Plaketten).
    Zwischen Superpunkten und gewoehnlichen Ecken kann so nicht unterschieden werden.
  - Vorab ableitbar [M]: <Q> = 0 folgt aus der Ladungskonjugation (theta -> -theta laesst Wirkung und Mass gleich); nur
    <|Q|> waere ein Befund.

## Eigene Vorab-Erwartungen (VORAB.md) im Rueckblick

| Nr | Erwartung (kurz) | Wahrsch. | Ausgang |
|---|---|---|---|
| V1 | 1+1D fehlerfrei, d_H 1,8 bis 2,2 | 70 % | fehlerfrei ja; d_H knapp darueber (2,23 bzw. 2,33) |
| V2 | 4D-Kern fehlerfrei, alle sieben Zugarten angenommen | 60 % | eingetroffen |
| V3 | D2 in der Zeit entschieden | 25 % | nicht entschieden (wie erwartet unwahrscheinlich) |
| V4 | zerknuellt bei k0 ~ 1, Delta = 0 mit Superpunkten, keine bei (2,2; 0,6) | 60 % | k0 = 1 nicht gerechnet; (2,2; 0,0) ohne Superpunkte; (2,2; 0,6) ohne |
| V5 | Ladung um Superpunkte im Mittel 0 | 75 % | nicht pruefbar |
| V6 | Felder aendern die Phasenlage nur wenig | 50 % | nicht eingetroffen in nackten Kopplungen (grosse k0/k4-Verschiebung) |
| 2. Welle | s0a2/s0b2: Groessenskalierung 1,8 bis 2,2 | 70 % | knapp verfehlt (2,23) |
| 2. Welle | L = 3: Maximum 3,8 bis 4,4, kein Plateau | 60 % | eingetroffen (4,23, kein Plateau) |
| 2. Welle | F2: d_s-Aenderung < 0,3 | 65 % | im Maximumsbereich ja (<= 0,21), im Abfall nein (0,47) |
| 2. Welle | F3: Eckenzahl sinkt, (2,8)-Gewicht stark negativ | 70 % | eingetroffen ((2,8) -21,0; N0/N4 0,035 am Ende) |
| 2. Welle | F1b bei k0 = 10,2: N0/N4 naeher an 0,04 | 55 % | eingetroffen (0,041) |
| 2. Welle | F4: keine Superpunkte, Ladung 0 | 70 % | eingetroffen |
| 2. Welle | s1x-unten: N0/N4 steigt Richtung 0,035 bis 0,04 | 60 % | eingetroffen (0,037) |

## Was aus Aufbau oder Literatur folgt, was gerechnet ist

- **[L]:**
  - 2D-CDT: d_H = 2, d_s = 2.
  - 4D-CDT: Phasen A, B, C (C_b); in C d_s ~ 4 bei grossen und ~ 2 bei kleinen Abstaenden, bei Volumina 7e4 bis 1,8e5.
  - DT: zerknuellt bzw. verzweigte Polymere (d_s = 4/3), Uebergang erster Ordnung.
  - Zugliste AJL.
  - Alles aus dem Gedaechtnis bzw. aus cdt-horava-l/DOSSIER.md.
- **[M] aus dem Aufbau:**
  - Die Groessenskalierung in 2D ist durch T ~ Wurzel(N2) teilweise vorgegeben.
  - <Q> = 0 folgt aus der Ladungskonjugation.
  - Die nackten k0/k4-Verschiebungen durch Felder haengen von der Massnormierung ab (Dehn-Sommerville).
  - Das d_s-Maximum ~ 4 eines kleinen 4D-Torus zeigt schon das Startnetz.
- **[E] gerechnet:** alle Tabellen oben.
- **Nicht gerechnet:** Phasengrenze, Polyakov-Schleife, Torsion, Variante C des Rahmens, Volumina ueber 2,5e4.

## Grenzen

- **Volumen:** N4 etwa 7000 (2x2x2 Zellen, T = 4) und etwa 23000 (3x3x3). Fuer ein d_s-Plateau um 4 braucht die
  Literatur 7e4 bis 1,8e5 [L]. Bei unseren Groessen bestimmt der kleine Torus die d_s-Kurve.
- **Zeitschichten:** nur T = 4. Kollaps in eine Schicht (Phase B) oder entkoppelte Schichten (Phase A) sind damit kaum
  aufloesbar.
- **Thermalisierung:** N0 relaxiert langsam (wenige (2,8)/(8,2)-Zuege je Sweep), die DT- und k0 = 5-Laeufe driften am
  Ende noch. Alle Zahlen sind Mittel ueber nicht voll thermalisierte Reihen, ohne Fehlerbalken. Als grobe Streuung gilt
  der Unterschied zwischen Abschnitten (d_s 0,05 bis 0,23).
- **k4-Nachfuehrung:** nur in der Thermalisierung; danach haelt der eps-Term das Volumen, das Mittel liegt bis zu 10 %
  unter Nz. Beim ersten L = 3-Lauf schaukelte die Nachfuehrung auf (k4 = 4,5); der Lauf wurde abgebrochen und mit festem
  k4 = 0,84 neu gestartet. Mit k4 = 0,84 schrumpft das L = 3-Volumen auf etwa 23000.
- **k0-Nachfuehrung fuer den Feldvergleich** war zu traege, weil N0 langsamer relaxiert. Die Feldlaeufe sind daher bei
  gleichen nackten Kopplungen zu lesen, nicht bei gleichem N0/N4.
- **Felder:** Gewichte w = 1 statt Hodge-Gewichten. beta_c von SU(2) auf diesem Komplex ist nicht bestimmt; beta = 2,5
  "ueber beta_c" ist [H].
- **Ergodizitaet** ist nicht bewiesen, nur im Kleinen geprueft.
- **Superpunkte:** Die Schwelle ist relativ (5 x mittlerer Grad), und die Startecken werden praktisch nie entfernt
  (Gedaechtnis des Starts). Sinkt der Mittelwert, weil viele neue Ecken kleiner Ordnung entstehen, ueberschreiten alte
  Ecken die Schwelle leichter. Ihr Grad ist zwar gewachsen (bis 149), aber eine absolute Schwelle wuerde anders zaehlen.

## Regelabweichungen

- **/dev/null-Umleitung:** Die erste Fassung der Feldkette (lauf-69/ketten/kette-s2.sh) enthielt `kill -0 PID 2>/dev/null`
  in einer Warteschleife. Sie lief etwa 10 s (einige Aufrufe mit dieser Umleitung, keine Rechnung); dann habe ich sie
  gestoppt und ohne Umleitung ersetzt (kette-s2b.sh).
- **Wartebefehle im Hintergrund:** Drei lokale Wartebefehle (ssh-Abfragen) liefen laenger als die Werkzeuggrenze. Das
  Werkzeug hat sie selbsttaetig in den Hintergrund verschoben, und ihre Ausgabe landete in dessen Aufgabendateien unter
  /tmp/claude-1000/... (ebenso eine bewusst im Hintergrund gestartete Warteschleife und die Ereigniswache). Danach habe ich
  nur noch Wartebefehle mit timeout unter der Grenze benutzt.
- **grep ohne Sperrausschluesse:** Einige grep-Aufrufe auf einzelne eigene Dateien (netzdyn.py, Kettenskripte, eigene
  Logs, Prozesslisten) liefen ohne die Ausschlussflaggen; keiner war rekursiv, keiner beruehrte gesperrte Pfade. Die
  Projekt-greps (CDT, spektrale Dimension) liefen mit den Ausschluessen.
- **Vorab:** VORAB.md vor dem ersten Lauf, Nachtrag fuer die zweite Welle (21:23:40) vor deren Ergebnissen, aber nach
  ihrem Start. Einige Laeufe der ersten Welle (Startnetz-Kontrollen, Punkt (5,0; 0,6), F1) hatten keine eigene Zeile,
  nur die allgemeinen Erwartungen V1 bis V6.
- **Eigene Einheit gestoppt:** den ersten L = 3-Abschnitt per systemctl --user stop (nur die eigene Einheit).
- **Sonst eingehalten:**
  - nur cpu8 bis cpu11 (cpu11 war frei), Laufzeit je Abschnitt hoechstens 556 s, df vor jedem Abschnitt;
  - nichts installiert, keine Nachrichten nach aussen, keine Commits;
  - Python nur ueber kleintest.sh; lokal kein python, awk oder perl, nur Shell-Werkzeuge (jq, scp, ssh, sed, grep,
    sha256sum).

## Fortsetzung (wenn D2 entschieden werden soll)

1. **Kern beschleunigen** (kompiliert, z. B. C oder numba). Python schafft bei N4 = 7000 etwa 4 bis 5 Sweeps/s, bei
   N4 = 23000 etwa 1,3 Sweeps/s. Ein Plateau braucht N4 >= 1e5 und T = 20 bis 80, also etwa Faktor 30 bis 100.
2. **Groessenreihe** bei festem (k0, Delta): N4 = 2e4, 4e4, 8e4, 1,6e5. Ein Plateau gilt nur, wenn das Maximum mit N4
   breiter wird und bei 3,5 bis 4,5 stehen bleibt; immer zusammen mit dem unveraenderten Startnetz gleicher Groesse.
3. **Zusaetzlicher Start mit S^3-Schichten**; die Profilform ("Blob") ist in der Literatur das Kennzeichen der
   ausgedehnten Phase [L].
4. **Phasengrenze:** Abtastung k0 = 2 bis 5 und Delta = 0 bis 0,6 mit N0/N4, Profilstreuung und Grad-Maximum. Danach D4
   mit k0-Nachfuehrung ueber lange Laeufe bei gleichem N0/N4, und die Normierung des Feldmasses vorher festlegen.
5. **Felder:** Hodge-Gewichte, Polyakov-Schleife, Torsion, Variante C des Rahmens. D7 braucht einen geschichteten Lauf mit
   Superpunkten (z. B. k0 = 5) und U(1).

## Einfach gesagt

Wir haben ein Netz gebaut, das sich Schicht fuer Schicht in der Zeit selbst umbaut, und darauf Felder gesetzt (Licht und
eine Art Kompassnadel an jeder Ecke), die beim Umbauen mitreden. Die Bauregeln funktionieren, alle Pruefungen sind
bestanden, und in 2D kommt fast die bekannte Flaeche heraus (2,2 bis 2,35 statt 2,0 fuer die Ausdehnung, genau 2 fuer
die Diffusion). Ob in 4D von selbst ein grosser vierdimensionaler Raum entsteht, konnten wir nicht entscheiden: Unser Netz
ist so klein, dass schon das unveraenderte Startnetz dieselbe Zahl (etwa 4) zeigt. Die Felder druecken die Zahl der Ecken
stark. Superpunkte, also Ecken mit sehr vielen Nachbarn, gab es nur ohne Schichten oder bei grossem k0, nicht im
geschichteten Netz bei den Standardwerten.

## Fuss

- Abschluss: 2026-10-06 21:50:29 CEST (date). Alle Laeufe beendet, keine eigene Einheit mehr aktiv auf der .69.
- Zwischenstaende stand/*.pkl (letzter je Lauf, zusammen etwa 10 MB) bleiben auf der .69 fuer Fortsetzungen; nicht
  lokal kopiert. Lokal: code/, lauf-69/ (JSON, auswertung.md, logs/, ketten/), VORAB.md, PRUEFSUMMEN.txt.
