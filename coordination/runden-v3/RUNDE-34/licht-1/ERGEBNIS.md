# LICHT-1: Ergebnis (Code-Agent fuer claude-primary, Runde 34, explorativ)

- **Gerechnet** auf der .69 ueber kleintest.sh. Die .69-Uhr laeuft in UTC; CEST = UTC + 2.
  - Spur cpu: Teil A (radial) 17:18:12 bis 17:21:46 UTC, Statik n = 3 von 17:21:46 bis 17:25:51 UTC.
  - Spur p4000a (CUDA, Quadro P4000, float64): Zeitentwicklung 17:22:15 bis 17:27:54 UTC (der erste Lauf wartete ab
    17:18:11 auf die Spur).
  - Endgueltige Auswertung 17:27:57 UTC, Bild 17:28:04 UTC (Spur cpu). Nie mehr als eine P4000- und eine CPU-Spur
    zugleich; cpu2 und cpu5 nicht benutzt.
  - Alle rc = 0. Laengster Lauf 4 min 05 s (Statik n = 3); keine Fortsetzung noetig.
  - Ausserhalb des Plans (Selbstanzeigen 3 und 4): radial-q099 und radial-q099-rmax (Nachtrag), statik-n3-h0.3-B und
    eine vorlaeufige Auswertung.
- **Eingefroren** um 19:17:59 CEST, vor der ersten echten Rechnung:
  - PLAN.md.eingefroren-20261003-191759
  - code/licht.py.eingefroren-20261003-191759 (sha256 beginnt mit 31ead78bd2ed3547)
  - code/laufplan.eingefroren-20261003-191759.tar (Spurskripte)
  - code/kegel_q.py unveraendert aus RUNDE-26 (sha256 beginnt mit 4de64b080729204c)
- **Rohdaten:** lauf-69/
  - radial-*.json, statik-n3-h0.3.json, li-t3-*.json (Bahnen alle 0,5 Zeiteinheiten), Logs
  - auswertung.json mit den mechanischen Urteilen; Bild v(t): v-t.png
  - Rauchlaeufe: rauch-69/ (Bild rauch-t3.png).
- Geschrieben ab 19:22:58 CEST (date).
- **Einheiten:** Modell M1 in 2D, Masse 1, Lichtgeschwindigkeit c = 1. Q = 200: Ruheenergie 157,301 (radial) bzw.
  157,288 (Netz h = 0,3), R_half = 6,26.

## Ergebnis zuerst

1. **Teil A: Eine Kegelmulde macht einen Q-Ball (Q = 200) hoechstens 0,42 c schnell.**
   - Aus der Ruhe kommend erreicht er am Muldengrund v_Grund = 0,135 / 0,194 / 0,242 / 0,287 / 0,334 c an Spitzen
     mit 5 / 4 / 3 / 2 / 1 Dreiecken.
   - Fuer Kontinuumskegel (s = 12 / 24) sind es 0,363 / 0,380 c. Der exakte Grenzwert s -> unendlich ist 0,418 c,
     mit B_inf = E - omega_c Q = 15,88, also 10,1 % der Ballenergie.
   - Die Duennwand-Zahlen der Karte liegen 2 bis 5 % unter dem exakten B; v aendert sich dadurch um 1 bis 2 %.
   - s = 48 rechnete der Loeser nicht (Selbstanzeige 3).
2. **Das Dreier-Netz traegt.**
   - B_gitter(s = 2) = 4,8193 gegen exakt 4,8236 (-0,09 %).
   - Der ruhende Kegelball auf der Spitze bleibt stehen (Drift 6e-6, Energie 2e-6 relativ).
3. **Die statische Mulde der Dreier-Spitze ist ein Schnapper.**
   - V(d) steigt von -4,82 (d = 0) glatt bis -3,02 (d = 9); dabei sitzt der Ball noch auf der Spitze
     (|phi|^2 dort 1,03).
   - Bei d = 10 springt V auf -0,054; der Ball hat sich geloest (|phi|^2 an der Spitze 0,035).
   - d ist der harmonische Schwerpunkt (Koordinate wie KEGEL-Q).
4. **Teil B, Dynamik:** Der Ball (v0 = 0,01, d0 = 25) faellt in die Mulde.
   - Beim ersten Durchgang (t = 1487,8) erreicht der Ladungsfluss v_rms = 0,2058. Die Energieerhaltung mit dem
     B desselben Netzes gibt v_E = 0,2422. Das sind -15,04 %: L2 ist knapp nicht eingetroffen.
   - Bei h = 0,2 sind es -14,97 % (eingetroffen), daher der Vermerk "nicht konvergiert". Bei dt = 0,05 sind es
     -15,08 %.
   - Zweiter Durchgang (t = 1570,2): v_rms = 0,1869, also langsamer (L3 eingetroffen).
5. **Der Ball bremst vor allem durch Verformung (innere Anregung), weniger durch Abgabe nach aussen, nicht durch das
   Gitter.** Das Budget ist nachtraeglich gerechnet [H], Selbstanzeige 9.
   - Beim ersten Durchgang (t = 1487,5) hat der Ball 0,84 Ladung abgegeben; ausserhalb der Ballscheibe liegen 0,91.
   - Davon ist 0,62 nur die Ruheenergie der abgegebenen Ladung (omega = 0,734 je Ladung). Netto nach aussen gingen
     0,29, also 6 % von K0 + B = 4,83.
   - Im Ball stecken dann 4,53 ueber der Ruheenergie des Kegelballs gleicher Ladung. v_rms = 0,206 entspricht 3,32
     Bewegungsenergie (69 %). Der Rest von 1,21 (25 %) steckt in Verformung und Atmung; max |phi|^2 steigt bis 1,206
     bei t = 1499,5.
   - Der Ball kehrt bei x_S = 7,93 um (V = -3,44, t = 1529), also tief in der Mulde: Der Verlust im ersten Durchgang
     ist 3,44 (71 % von K0 + B). Er bleibt gefangen.
   - Aufteilung dieses Verlusts: 2,37 innere Anregung (69 %) und netto 1,07 nach aussen (31 %). Bis dahin hat der Ball
     2,85 Ladung (1,4 %) abgegeben.
   - Zum Vergleich EINFANG-1 (Fuenfer-Ecke): Dort gingen 92 bis 95 % des Verlusts in Atmung und nur 5 bis 8 % nach
     aussen. Die spitzere Ecke gibt also mehr nach aussen ab.
6. **Die Koordinaten-Schwerpunkte taugen an der Spitze nicht als Tachometer.**
   - Der harmonische Schwerpunkt von EINFANG-1 zeigt beim Durchgang |dx/dt| = 1,71 > c, weil er dort singulaer ist.
   - Der axiale Schwerpunkt springt (0,347), das Feldmaximum springt (bis 7,2).
   - Gewertet ist deshalb, wie im Plan festgelegt, der koordinatenfreie Ladungsfluss v_rms.

## Vorab gegen Ausgang

| Nr | Vorhersage (Karte) | Ausgang (mechanisch nach PLAN.md, lauf-69/auswertung.json) |
|---|---|---|
| L0 | Kontrolle: Die exakte Abbildung bei s = 1,2 trifft B = 1,4465 (KEGEL-Q, Q = 200) auf 0,2 % (90 %) | **eingetroffen**: B(1,2) = 1,446502, Abweichung +1,7e-6 |
| L1 | Grundgeschwindigkeit aus Teil A: n = 4: 0,15 bis 0,23; n = 3: 0,19 bis 0,29; n = 1: 0,26 bis 0,40; fuer alle s unter 0,45 (75 %) | **eingetroffen**: 0,1937 / 0,2421 / 0,3345; groesstes v aller gerechneten s 0,3804 (s = 24), Grenzwert s -> unendlich 0,4183 |
| L2 | Teil B: Die hoechste gemessene Schwerpunktgeschwindigkeit beim ersten Durchgang liegt innerhalb 15 % des Werts aus Energieerhaltung mit dem statischen B(s = 2) desselben Netzes (70 %) | **nicht eingetroffen, Vermerk "nicht konvergiert"**: v_rms,max = 0,20578 gegen v_E = 0,24221, also -15,04 %. dt = 0,05: 0,20569 (-15,08 %, gleiches Urteil). h = 0,2: 0,20595 (-14,97 %, anderes Urteil) |
| L3 | Teil B: Beim zweiten Durchgang ist die Hoechstgeschwindigkeit kleiner als beim ersten (85 %) | **eingetroffen**: v_rms,max = 0,18694 < 0,20578; beide Konvergenzproben gleich (0,18682 < 0,20569; 0,18702 < 0,20595) |

- **v_E** = sqrt(1 - 1/gamma_E^2) mit gamma_E = 1 + (K0 + B_gitter)/E_fern = 1,030690.
  - K0 = 0,007898 aus v_ein = 0,010021 (2539 Punkte im Fernbereich).
  - B_gitter = 4,819289; E_fern = 157,288170 (Ball bei d = 25 auf demselben Netz).
- **Ableitbarkeit:**
  - L0 war vorab ableitbar. KEGEL-Q (RUNDE-26, radial.json, dr = 0,01) enthaelt B = 1,446502 fuer Q = 200 und
    s = 6/5. Geprueft wurde nur, dass der neue Familienbau dieselbe Zahl gibt.
  - L1 war fast ableitbar. Die Duennwand-Naeherung der Karte liegt 1 bis 2 % neben dem exakten v, die Spannen sind
    15 bis 20 % breit.
  - L2 und L3 konnten scheitern. L2 ist um 0,04 Prozentpunkte gescheitert.

**Bedeutung (nach Karte, Fall "L2 trifft nicht ein"):**
- Karte: "Es gibt einen zusaetzlichen Beschleunigungs- oder Bremsmechanismus (Verformung, Gitter). Beschreiben."
- **Bremsmechanismus: Verformung, dazu etwas Abgabe nach aussen; nicht das Gitter.**
  - Gitter: B_gitter weicht um 0,09 % ab. v_rms,max haengt auf 0,05 % (dt) bzw. 0,08 % (h) am Gitter.
  - Verformung: An der Dreier-Spitze schnappt der Ball an (statischer Sprung von V bei d = 9 bis 10). Er wird dabei
    stark zusammengedrueckt; max |phi|^2 steigt von 1,05 auf 1,21.
  - [H] Beim ersten Durchgang stecken etwa 25 % von K0 + B in Verformung und Atmung, und 6 % sind netto nach aussen
    gegangen. Fuer die Fliessbewegung bleiben 69 %.
  - Als reine Bewegung ergaeben die 4,53 im Ball v = 0,238 (Ruhemasse des Kegelballs 151,85). Das Budget ist
    nachtraeglich gerechnet (Selbstanzeige 9).
- **Fuer Finns Frage** gilt die erste Lesart der Karte trotzdem (L1 und L3 eingetroffen):
  - Kegelmulden beschleunigen Q-Baelle hoechstens auf einen Bruchteil von c (<= 0,42 c), begrenzt durch den
    Oberflaechenanteil der Energie.
  - Eingefangene Baelle werden im naechsten Durchgang langsamer.
  - Die Dynamik bleibt noch etwa 15 % unter der Energieschranke.
- **Einschraenkungen:**
  - Das Urteil von L2 haengt am Mass und an 0,04 Prozentpunkten. v_mean gaebe -27 %, der axiale Schwerpunkt +43 %.
  - Gerechnet ist nur Q = 200, Stossparameter 0, eine Spitze (n = 3).

## Tabelle Teil B (n = 3, Q = 200, R = 60, Schwamm ab r = 45, v0 = 0,01, d0 = 25)

- v_rms, v_mean: koordinatenfreie Fliessgeschwindigkeit der Ladung; v_rms ist das Urteilsmass.
- v_ax: axialer Schwerpunkt; v_x: harmonischer Schwerpunkt (EINFANG-1); beide nur beschreibend.
- Umkehr: groesstes |x_S| zwischen zwei Durchgaengen (harmonischer Schwerpunkt mit |phi|^2, Koordinate von KEGEL-Q);
  V aus der Statik desselben Netzes (h = 0,3).
- Verlust: Durchgang 1 = K0 - V(Umkehr 1), Durchgang 2 = V(Umkehr 1) - V(Umkehr 2). Ein negativer Verlust ist ein
  Gewinn.

| Lauf | h | dt | Durchgang | t | v_rms,max | v_mean,max | v_ax,max | v_x,max | Umkehr x_S | V(Umkehr) | Verlust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| t3-v0.01 (Haupt) | 0,3 | 0,1 | 1 | 1487,8 | **0,2058** | 0,1775 | 0,347 | 1,71 | 7,933 | -3,435 | 3,443 (71 %) |
| | | | 2 | 1570,2 | **0,1869** | 0,1710 | 0,275 | 1,61 | 8,427 | -3,246 | -0,189 |
| t3-v0.01-dt0.05 | 0,3 | 0,05 | 1 | 1488,8 | 0,2057 | 0,1774 | 0,347 | 1,71 | 7,929 | -3,436 | 3,444 |
| | | | 2 | 1571,2 | 0,1868 | 0,1708 | 0,275 | 1,61 | 8,425 | -3,247 | -0,189 |
| t3-v0.01-h0.2 | 0,2 | 0,05 | 1 | 1487,8 | 0,2060 | 0,1774 | 0,346 | 1,71 | 7,931 | (Statik nur h = 0,3) | |
| | | | 2 | 1570,2 | 0,1870 | 0,1710 | 0,275 | 1,62 | 8,424 | | |

- **Energieerhaltung:** v_E = 0,2422 (K0 + B_gitter = 4,827). v_rms,max/v_E = 0,850 (1. Durchgang) und 0,772 (2.).
- **Budget im Hauptlauf** (Ballscheibe Radius 15 um den harmonischen Schwerpunkt; "draussen" = E_tot - E_ball +
  E_damp):

  | t | Ereignis | draussen | Q_ball | max \|phi\|^2 |
  |---|---|---|---|---|
  | 1432,5 | Eintritt (xi_c > -R_c) | 0,0002 | 199,9997 | 1,047 |
  | 1487,5 | 1. Durchgang | 0,909 | 199,158 | 1,056 |
  | 1499,5 | Kompressionsmaximum (draussen und Q_ball bei t = 1500) | 0,887 | 199,182 | 1,206 |
  | 1529 | 1. Umkehr | 3,192 | 197,154 | 1,093 |
  | 1570 | 2. Durchgang | 5,012 | 195,446 | 1,069 |
  | 1650,5 | Laufende | 5,316 | 195,168 | 1,086 |

  - Bis Laufende hat der Schwamm 3,29 Energie und 2,87 Ladung geschluckt.
  - "Draussen" enthaelt die Ruheenergie der abgegebenen Ladung (rund omega = 0,73 bis 0,74 je Ladung). Netto ueber
    diese Ruheenergie hinaus sind es 0,29 (t = 1487,5) und 1,07 (t = 1529).
  - "Draussen" steigt nach t = 1529 weiter, obwohl die Umkehrpunkte danach einen Gewinn zeigen. Die Ballscheibe faengt
    die verformte Wolke nur grob ein, und V(x_S) gilt fuer Q = 200. Diese Zahlen sind beschreibend.
- **Statisches Potential** (n = 3, h = 0,3; V(d) = E(d) - E(25); |phi|^2 an der Spitze):

  | d | 0 | 2 | 4 | 6 | 8 | 9 | 10 | 11 | 12 | 14 | 16 |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | V | -4,8193 | -4,8028 | -4,5700 | -4,0790 | -3,4111 | -3,0245 | -0,0539 | -0,0114 | -0,0028 | -1,8e-4 | -1,2e-5 |
  | \|phi\|^2 Spitze | 1,036 | 1,036 | 1,031 | 1,033 | 1,034 | 1,034 | 0,035 | 0,005 | 0,001 | 7e-5 | 4e-6 |

## Kontrollen

- **Teil A:**
  - Familie: 128 Punkte bis Q = 12 786 (omega^2 = 0,5066), Newton-Rest <= 9,1e-12.
  - Probe dr = 0,005: |Delta B| <= 1,2e-5 (s = 24), |Delta v| <= 1,4e-7.
  - Probe rmax = 120: |Delta B| <= 7e-13.
  - dE/dQ = omega auf 6,1e-9 (s = 1,2), 6,5e-9 (s = 2), 8,2e-8 (s = 6).
  - Alle Q' mit dQ/domega^2 < 0 und E/Q' < 1. f^2 am Rand <= 4,9e-33 bei R_half <= 32,5.
- **Netz (n = 3, h = 0,3, R = 60):** 72 526 Ecken; Grad der Spitze 3, Defekt pi, Euler 1. Innenecken: eine vom Grad 3,
  71 835 vom Grad 6. Auf der Spiegelachse 314 Ecken (Abstand 0,3 vor, 0,52 hinter der Spitze).
- **Statik:** Restgradient <= 4,2e-6. Die Absicherung statik-n3-h0.3-B (d = 0, 25) gibt dasselbe B (4,819289).
- **Netz traegt** (Plan 2.8): alle sechs Bedingungen erfuellt (auswertung.json, teil_b.netz_traegt). Teil B blieb
  bei n = 3.
- **Ruhender Kegelball** (t3-ruhe, T = 200): Drift von xi_c 6e-6, |x_S| <= 1,3e-6, E_ball 2e-6 relativ.
  v_rms <= 5e-4; das ist der Boden des Masses.
- **Eichung des Urteilsmasses:** Im Fernbereich ist v_rms = 0,0100 gegen v_ein = 0,01002 aus x(t) (EINFANG-1).
  Im Rauchlauf war v_rms = 0,0498 bei v0 = 0,05.
- **Energiebilanz** max |E_tot + E_damp - E_tot(0)|:
  - 1,0e-2 bei dt = 0,1; 2,5e-3 bei dt = 0,05 (h = 0,3 und 0,2). Das faellt wie dt^2.
  - Die Kompression an der Spitze verstaerkt den Verlet-Fehler (EINFANG-1: 2e-3).
- **Ladungsbilanz** auf 2e-12. Spiegelsymmetrie |Im W| <= 3,8e-8 in allen Laeufen.
- **Konvergenz** v_rms,max: 0,20578 / 0,20569 / 0,20595 (Haupt / dt = 0,05 / h = 0,2) und 0,18694 / 0,18682 / 0,18702.
  Durchgangszeiten auf 1,0, Umkehrpunkte auf 0,004.

## Latten (v3)

- **L1: teilweise.** L2 und L3 konnten scheitern; L2 ist knapp gescheitert. L0 war ableitbar, L1 fast.
- **L2: ja.**
  - Zwei Konvergenzproben.
  - B des Netzes gegen die exakte Abbildung.
  - Ruhender Kegelball, Eichung von v_rms im Fernbereich, Energie- und Ladungsbilanz mit Schwamm.
  - Teil A mit zwei Proben (dr, rmax) und dE/dQ.
- **L3: teilweise.**
  - v_rms,max ist auf 0,1 % konvergiert.
  - Das Urteil von L2 liegt aber innerhalb dieser Streuung an der Grenze (Vermerk "nicht konvergiert").
- **L4: teilweise.**
  - Beschleunigung eines Solitons in einer Potentialmulde, Abstrahlung bei starker Verformung und Einfang sind fuer 1D
    bekannt [L?, aus dem Gedaechtnis, nicht nachgelesen: Kink- und NLS-Soliton-Streuung an Defekten, vgl.
    EINFANG-1].
  - Die Abbildung Kegel -> ebener Ball mit Ladung sQ ist elementar.
  - Fuer 2D-Q-Baelle an Kegelspitzen wurde nicht gesucht.
- **L5: nein.** Kein Messbezug. Moegliche Analogien [H]: Tropfen, die an einer Spitze anschnappen; Abstrahlung
  komprimierter Solitonen.

## Selbstanzeigen

1. **Rauchlauf vor dem Einfrieren** (Q = 150, h = 0,5, R = 30, r_s = 22, v0 = 0,05, d0 = 12):
   - Er zeigte die Tendenz von L2 (v_rms/v_E - 1 = -0,13) und L3.
   - Die Wahl von v_rms als Urteilsmass fiel nach diesem Rauchlauf, weil die drei Koordinatenmasse dort sprangen oder
     divergierten. Offengelegt im Plan, Abschnitt 7.
2. **Code zwischen Rauchlauf und Einfrieren geaendert** (Urteilsmass, Pruefung "Netz traegt").
   - Die eingefrorene Fassung lief auf den Rauchdaten erst nach dem Einfrieren (17:18:11 UTC), ohne Fehler.
3. **s = 48 nicht gerechnet.**
   - loese_Q (brentq) fand keine Vorzeichenklammer, obwohl die Familie bis Q = 12 786 reicht.
   - Nachtrag ausserhalb des Plans: code/licht_nachtrag.py (Kopie von licht.py mit Option --q;
     code/laufplan/spur-nachtrag-cpu.sh) mit q = 0,99 und rmax 90 / 120. Er scheiterte ebenso; s <= 24 gab er auf 1e-9
     gleich wieder.
   - Ursache nicht untersucht [H: Newton aus dem Nachbarprofil landet im Duennwandbereich auf einem falschen Profil].
   - L1 ist davon nicht beruehrt (Grenzwert s -> unendlich exakt).
4. **Zusatzlaeufe ohne Einfluss auf die Urteile:**
   - statik-n3-h0.3-B (d = 0 und 25) als Absicherung gegen die 600-s-Grenze der Hauptstatik.
   - Eine vorlaeufige Auswertung um 17:26:35 UTC vor dem Ende des h = 0,2-Laufs, mit denselben Regeln; Log
     log-auswertung-vorlaeufig.txt.
   - Die endgueltige Auswertung (17:27:57 UTC) hat auswertung.json ueberschrieben.
5. **L2 haengt an 0,04 Prozentpunkten und am Mass.**
   - Die Messgroesse "Schwerpunktgeschwindigkeit" der Karte ist an der Spitze nicht eindeutig. Plan und Ergebnis
     ersetzen sie durch den Ladungsfluss.
   - Ein Leser, der einen anderen Tachometer waehlt, kommt zu einem anderen Urteil (Tabelle oben).
6. **v_rms enthaelt innere Stroemungen** (Atmen, Verformung).
   - Im zweiten Durchgang entspricht v_rms = 0,187 einer Bewegungsenergie von 2,82.
   - Nach den Umkehrpunkten stehen am Grund aber nur etwa 1,38 zur Verfuegung (4,82 - 3,44), also v ~ 0,13.
   - L3 gilt mit beiden Zahlen. Die Ueberhoehung im ersten Durchgang ist nicht bekannt.
7. **Fenster des zweiten Durchgangs:** Es reicht nach Regel bis Laufende. T_nach = 80 ist etwa eine halbe
   Pendelperiode, das Fenster enthaelt also den Anlauf zum dritten Durchgang.
   - v_rms(Laufende) = 0,178 < 0,187, ohne Einfluss.
8. **V(d) springt zwischen d = 9 und 10.** Die lineare Interpolation dort waere bedeutungslos. Die Umkehrpunkte (7,93
   und 8,43) liegen auf dem anhaftenden Ast. Am verformten, angeregten Ball ist V(x_S) nur eine Naeherung.
9. **Nachtraegliche Deutungen [H]:**
   - Das Energiebudget (69 / 25 / 6 % beim Durchgang, 69 / 31 % des Verlusts am Umkehrpunkt) ist aus Zahlen der
     Laufdatei gerechnet, nicht im Plan festgelegt:
     - Ruheenergie des Kegelballs E(0) - omega Delta Q mit omega = 0,7336
     - am Umkehrpunkt E_fern - 0,7449 Delta Q + V(x_S)
     - Bewegungsenergie (gamma(v_rms) - 1) mal Ruhemasse
   - Eine erste Fassung dieses Ergebnisses rechnete die ganze Energie ausserhalb der Ballscheibe als Strahlung (0,91,
     v = 0,2195). Das war falsch, weil die Ruheenergie der abgegebenen Ladung darin steckt; berichtigt vor der Abgabe.
   - Ebenso nachtraeglich: das Anschnappen als Ursache und der Gewinn im zweiten Durchgang (Rueckfluss innerer Energie,
     wie EINFANG-1).
10. **Technik:**
    - Der ssh-Befehl, der die Spuren startete, blieb haengen und wurde im Hintergrund beendet, ohne Einfluss.
    - Die Uhrzeiten der Laeufe stammen aus den .69-Logs (UTC).

## Einfach gesagt

Ein Q-Ball ist ein Feldklumpen, der sich wie ein Tropfen mit Oberflaechenspannung verhaelt. An einer spitzen Ecke des
Netzes spart er Energie, und genau diese Ersparnis kann er beim Hineinfallen in Bewegung verwandeln. Wie viel das
hoechstens ist, laesst sich exakt ausrechnen: selbst an einer unendlich spitzen Ecke nur etwa 42 % der
Lichtgeschwindigkeit, an der spitzesten Netz-Ecke 33 % und an einer Tetraeder-Ecke 24 %. Im Film an der Tetraeder-Ecke
schnappt der Ball an die Spitze und wird zusammengedrueckt; ein Viertel der gewonnenen Energie steckt dann im Wackeln
und Atmen des Balls, ein kleiner Teil fliegt davon. Er erreicht deshalb nur etwa 21 % statt 24 % der
Lichtgeschwindigkeit, knapp mehr als 15 % zu wenig. Danach bleibt er gefangen und pendelt langsamer hin und her;
Lichtgeschwindigkeit erreicht er nie.
