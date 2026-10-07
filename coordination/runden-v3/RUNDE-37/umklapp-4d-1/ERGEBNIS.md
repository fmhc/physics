# UMKLAPP-4D-1: Ergebnis (Code-Agent fuer die Leitung claude-primary, Versuch ohne Karte)

- Versuch ohne Karte (Finn, 05.10.: "einfach machen und ausprobieren"): kein eingefrorener Plan, keine
  Vorhersagetabelle, kein frischer Leser. Alles sind synthetische, lineare Gitterrechnungen um flach (Glas N = 128,
  Bloch k = 0), keine Messdaten.
- Kennzeichen: [E] hier gerechnet, [M] Mathematik, [P] Projektdatei, [H] Lesart oder Hypothese, [N] nach Sicht ergaenzt.
- Zeiten (date; die .69 schreibt UTC, CEST = UTC + 2): Start 17:04:23 CEST. Rauchtest 15:14:56 bis 15:15:49 UTC.
  Hauptketten 15:17:33 bis 15:39:02 UTC, Nachlauf h = 2^-12 fuer s4 f5 15:40:48 bis 15:42:06 UTC, Auswertung 15:42:09 UTC.
  Text ab 17:43 CEST.

## 1. Ergebnis zuerst

1. **Mit M_eff ist der Geometriesprung viel kleiner [E].** Bei mu = -1e-3 betraegt der Median von |dH|/H0 ueber
   24 Zuege mit A2 4,8e-4 (R) bzw. 8,7e-4 (P), mit M_eff 3,9e-8 (R) bzw. 1,15e-6 (P). M_eff ist in 24 von 24 Zuegen
   kleiner, im Median um den Faktor 1,1e4 (R; Spanne 444 bis 2,8e7) bzw. 1,2e3 (P; 58 bis 4,7e4).
2. **Der M_eff-Sprung faellt wie |mu|^1, der A2-Sprung nicht [E].**
   - P: An allen 32 gepaarten Schritten (24-mal von -1e-3 auf -1e-4, 8-mal von -1e-4 auf -1e-5) faellt der Sprung je
     Zehntel in mu um den Faktor 9,4 bis 14,9. Das ergibt p = 0,97 bis 1,17.
   - R: In 15 von 24 Zuegen ebenso (9,8 bis 11,4). In den uebrigen 9 Zuegen bleibt ein Rest, der nicht mit mu faellt.
     Wo geprueft (s4 f5 X, s1 f0 Y), haengt er an h. Bei s4 f5 X liegt er bei 2,4e-12 bzw. 2,5e-12 mit h = 2^-10 und bei
     1,3e-13 mit h = 2^-12. Er faellt also um den Faktor
     18 bis 20 je Viertelung von h (h^2 gaebe 16; bei 2^-12 liegt der Wert schon im Bodenbereich). Darunter liegt ein
     Boden um 1e-13 absolut (1e-9 relativ), der bei kleinerem h eher waechst [H: Rundung].
   - A2: Verhaeltnis 0,85 bis 1,04, also kein Abfall.
3. **Der ganze Sprung ist kinetisch, in beiden Formen [E].** Das Potential bleibt stetig (|dV|/H0 <= 1,1e-14). Mit der
   flachen Fortsetzung der neuen Kante ist auch die 3D-Regge-Form B nach Rueckzug gleich (Abweichung <= 5,4e-14). [M]
   erwartet: Die Doppelpyramide bleibt flach, die Regge-Wirkung aendert sich beim Pachner-Zug nicht.
4. **Lesart [H]:** Der Sprung unter Form A2 ist ein Artefakt der gesetzten Traegheit. Mit der Traegheit aus der
   4D-Wirkung geht er an der Kosphaerizitaet (mu -> 0) linear gegen null, sauber in P und in R bis auf den h-Rest. Das
   gilt nur fuer diesen Aufbau (Abschnitt 6).
5. **M_eff macht auf dem Glas keine Probleme [E].** In allen 84 Netzen der Hauptlaeufe (28 Ausgangsnetze, 56 nach dem
   Zug) gilt:
   - genau 128 negative Richtungen (= Ecken), keine statische Richtung;
   - D_0 positiv definit;
   - Potential = B auf 3,2e-5, kappa = -0,50000005 bis -0,50000011;
   - A_red = S^T M_eff^-1 S positiv definit vor und nach jedem Zug.
   Das TT-Tempo omega/|k1| liegt bei 0,885 bis 0,968 (A2: 2,09 bis 2,53). Eine umgekehrte Hubfolge aendert die
   Spruenge um hoechstens 2e-6 relativ (P: <= 5e-9; nur s1 f0 geprueft).

## 2. Was gerechnet wurde

- **Faelle [P]:** 12 der 32 gespeicherten Faelle aus KANON-TRANSFER-1 / UEBERGABE-KONFLUENZ-1 (Saat/Nr/Art):
  1/0 D, 1/2 T, 1/3 K, 1/6 K, 2/0 D, 2/3 K, 2/5 K, 3/1 D, 3/4 K, 3/7 K, 4/2 D, 4/5 K.
  - Zuege X und Y, je als erster 2-3-Zug auf der Ausgangszerlegung.
  - Gerechnet bei mu = -1e-3 (gespeicherte Lagen) und mu = -1e-4 (Newton wie kanon.fall), also 24 Zuege je mu.
  - [N] Zusaetzlich mu = -1e-5 fuer die Faelle 1/0, 1/2, 2/5 und 3/4 (8 Zuege).
- **M_eff aus der 4D-Wirkung [E]:**
  - Je Zerlegung ein Zeltgitter (rk.Gitter) ueber der ganzen periodischen Box als Grundzelle, Bloch k = 0. Vor dem Zug
    hat die Box je nach Saat 850 bis 873 Tetraeder und 978 bis 1001 Kanten, nach dem Zug ein Tetraeder und eine Kante
    mehr. Hubfolge nach
    Eckindex (wie V-A: Rang b = b, Hoehe b/128 mal h), h = 2^-10. Ergebnis: 2084 bis 2132 4D-Kanten.
  - Bloecke wie uw.bloecke2 (Schema ls, Fassung B, Schur ueber den Gitterrest mit n_L = 594 bis 618).
  - Bei k = 0 reell gerechnet: Alle Phasen sind 1, die Faktoren i^p sind herausgezogen. Gegenprobe gegen den
    komplexen Code auf V bei k = 0: S_2 stimmt auf 6e-12, S_0 auf 8e-13, S_1 auf 1,5e-11.
  - M_eff = S_2 auf q (eine Zeile je Raumkante), ueber uv.Zuordnung in tg-Kanten.
  - Zeit je M_eff: 23 bis 26 s.
- **3D-Hamiltonform:** td.Netz (dieselbe S als Komplement von [M, c, 1_E], dasselbe B_red), aber A = M_eff^-1 statt
  A2. Also A_red = S^T M_eff^-1 S, wie in uv.reduktion [P].
- **Zustand:** TT-Mode wie in KANON-TRANSFER-1 (td.tt_mode, A_Q = 1e-3, Phase 1), jeweils mit der eigenen Form
  bestimmt.
- **Uebergabe:** td.abbilden unveraendert, Lesarten R und P.
- **Vergleich A2:** im selben Lauf neu gerechnet (wie kanon.py). 48 von 48 Werten sind gleich den gespeicherten
  KANON-TRANSFER-1-Werten (Abweichung 0).
- **Kontrolllaeufe [N]:**
  - Hubfolge umgekehrt (s1 f0, mu = -1e-3 und -1e-4);
  - h = 2^-12 (s1 f0 mu = -1e-3 und -1e-4; s4 f5 nach Sicht des R-Rests).

## 3. Regel fuer die neue Kante

- **Geometrie nach dem Zug:** Das Zeltgitter wird ueber der neuen Zerlegung neu gebaut (gleiche Lagen, Hubfolge, h).
  Die neue Kante d-e ist dort eine eigene Raumkante mit Prismen-Simplizes ueber den drei neuen Tetraedern. M_eff
  danach hat eine Kante mehr.
- **Lesart R (Laengen und Raten stetig):** Laenge und Rate der neuen Kante kommen aus der flachen Fortsetzung der
  Doppelpyramide: a_de = j . a_9 und adot_de = j . adot_9, mit j = Linearisierung des flachen Abstands d-e nach den
  9 Kanten (td.jrow_flach). Danach Projektion auf die neue Zwangsflaeche.
- **Lesart P (Impulse stetig):** Gemeinsame Kanten behalten den Impuls, die neue Kante bekommt p_de = 0, danach
  Projektion.
  - Das ist der Kotangentialhub derselben Einbettung J (alte -> neue Kanten): J^T p_neu = p_alt vor der Projektion [M].
- **Begruendung:** Es ist die einfachste Regel, unter der die Doppelpyramide flach bleibt. Der Fehlwinkel an d-e ist
  null, das Potential ist exakt stetig (Abschnitt 1, Punkt 3).

## 4. Tabelle

Relativer Sprung |dH|/H0 je Zug; H0 ist die Geometrieenergie vor dem Zug in der jeweiligen Form (A2 bzw. M_eff). A2 ist
bei -1e-3 und -1e-4 praktisch gleich (Verhaeltnis 0,85 bis 1,04), deshalb steht A2 nur bei -1e-3. In der
M_eff-R-Spalte steht in Klammern das Vorzeichen bei -1e-3. Werte aus lauf-69/auswertung.json [E].

| Saat/Nr/Art | Zug | A2 R (-1e-3) | A2 P (-1e-3) | M_eff R: -1e-3 / -1e-4 / -1e-5 | M_eff P: -1e-3 / -1e-4 / -1e-5 |
|---|---|---|---|---|---|
| 1/0 D | X | 5.91e-4 | 5.49e-4 | 6.46e-9 (-) / 6.42e-10 / 6.13e-11 | 2.21e-6 / 2.15e-7 / 2.24e-8 |
| 1/0 D | Y | 3.04e-4 | 3.22e-2 | 1.58e-8 (-) / 6.43e-10 / 8.66e-10 | 6.88e-7 / 5.72e-8 / 5.93e-9 |
| 1/2 T | X | 4.30e-4 | 8.16e-4 | 5.99e-8 (-) / 6.03e-9 / 5.87e-10 | 8.29e-8 / 8.24e-9 / 8.08e-10 |
| 1/2 T | Y | 2.24e-4 | 7.37e-4 | 1.00e-7 (-) / 1.01e-8 / 1.01e-9 | 2.18e-6 / 2.18e-7 / 2.25e-8 |
| 1/3 K | X | 2.92e-4 | 4.90e-4 | 2.68e-8 (-) / 1.96e-9 | 1.29e-6 / 1.28e-7 |
| 1/3 K | Y | 3.29e-4 | 8.46e-3 | 2.59e-9 (+) / 3.60e-9 | 2.95e-6 / 2.87e-7 |
| 1/6 K | X | 8.41e-4 | 1.60e-2 | 4.63e-8 (-) / 4.49e-9 | 3.54e-7 / 3.45e-8 |
| 1/6 K | Y | 7.15e-5 | 7.81e-4 | 6.00e-9 (-) / 5.27e-10 | 1.81e-6 / 1.81e-7 |
| 2/0 D | X | 1.08e-4 | 3.88e-3 | 2.25e-8 (-) / 4.74e-10 | 1.40e-5 / 1.00e-6 |
| 2/0 D | Y | 1.17e-3 | 1.97e-3 | 5.34e-8 (-) / 5.34e-9 | 9.25e-8 / 9.28e-9 |
| 2/3 K | X | 1.94e-3 | 6.41e-3 | 2.60e-7 (-) / 2.57e-8 | 1.72e-6 / 1.68e-7 |
| 2/3 K | Y | 2.97e-4 | 9.31e-4 | 1.49e-7 (-) / 1.50e-8 | 1.71e-7 / 1.71e-8 |
| 2/5 K | X | 4.58e-5 | 4.43e-3 | 1.03e-7 (-) / 6.81e-9 / 2.80e-9 | 1.97e-5 / 1.32e-6 / 1.32e-7 |
| 2/5 K | Y | 5.51e-4 | 6.36e-4 | 3.72e-9 (-) / 8.11e-11 / 2.78e-10 | 3.75e-6 / 3.75e-7 / 3.99e-8 |
| 3/1 D | X | 2.33e-3 | 1.01e-4 | 7.52e-8 (-) / 7.50e-9 | 1.15e-7 / 1.15e-8 |
| 3/1 D | Y | 5.11e-4 | 1.67e-3 | 1.84e-11 (-) / 1.01e-9 | 1.38e-6 / 1.38e-7 |
| 3/4 K | X | 4.44e-4 | 4.99e-4 | 5.44e-8 (-) / 5.26e-9 / 3.13e-10 | 7.44e-7 / 7.41e-8 / 7.56e-9 |
| 3/4 K | Y | 9.58e-4 | 1.33e-5 | 1.34e-7 (-) / 1.34e-8 / 1.31e-9 | 1.95e-7 / 1.96e-8 / 1.98e-9 |
| 3/7 K | X | 2.97e-3 | 1.42e-2 | 1.41e-8 (-) / 1.38e-9 | 2.31e-6 / 2.27e-7 |
| 3/7 K | Y | 7.30e-4 | 1.78e-3 | 8.10e-8 (-) / 8.00e-9 | 9.50e-7 / 9.51e-8 |
| 4/2 D | X | 3.50e-4 | 5.61e-4 | 1.00e-8 (-) / 1.02e-9 | 1.34e-8 / 1.34e-9 |
| 4/2 D | Y | 1.34e-3 | 7.94e-4 | 1.42e-7 (-) / 1.37e-8 | 6.35e-7 / 6.35e-8 |
| 4/5 K | X | 5.09e-4 | 1.69e-2 | 3.25e-8 (+) / 3.42e-8 | 9.62e-6 / 9.19e-7 |
| 4/5 K | Y | 6.92e-5 | 5.86e-5 | 1.52e-8 (-) / 4.38e-10 | 1.00e-6 / 1.01e-7 |
| **Median (n = 24)** | | **4.77e-4** | **8.74e-4** | **3.94e-8 / 4.88e-9 / 7.27e-10 (n = 8)** | **1.15e-6 / 1.15e-7 / 1.50e-8 (n = 8)** |

- Vorzeichen [E]: Mit M_eff ist dH in Lesart P in 56 von 56 Zuegen positiv (Energiegewinn). In Lesart R ist dH bei
  -1e-3 in 22 von 24 Zuegen negativ. A2 hat gemischte Vorzeichen.
- Verhaeltnis -1e-3/-1e-4 (n = 24): M_eff P im Median 10,0 (9,94 bis 14,9), M_eff R 10,1 (0,018 bis 47). Bei
  -1e-4/-1e-5 (n = 8): M_eff P 9,74 (9,39 bis 10,2). A2: R 1,00 (0,89 bis 1,03), P 1,00 (0,85 bis 1,04).
- Die R-Zuege ausserhalb von "Faktor 10" sind 1/0 Y, 1/3 X, 1/3 Y, 2/0 X, 2/5 X, 2/5 Y, 3/1 Y, 4/5 X und 4/5 Y. Dort
  traegt vermutlich der h-Rest bzw. der Boden mit [H]. Geprueft ist das nur an 1/0 Y und 4/5 X (Abschnitt 5).

## 5. Kontrollen [E]

- **M_eff auf dem Glas:**
  - n_neg = 128 und n_null = 0 in allen 84 Netzen der Hauptlaeufe. In den 18 Netzen der Kontrolllaeufe ebenfalls
    n_neg = 128, D_0 positiv und A_red positiv definit.
  - Kleinster Eigenwertbetrag relativ 7,3e-7 bis 1,8e-4.
  - D_0: 0 negative Eigenwerte, kleinster relativ 8,7e-4 bis 4,4e-3. J regulaer (kleinster relativer Singulaerwert
    1,26e-4 bis 1,35e-4), Rang B_s = 384 = 3 mal 128.
  - Symmetrie der Bloecke <= 7,6e-12.
- **ADM-Form bei h = 2^-10:** V_eff gegen B 1,3e-5 bis 3,2e-5. C = kappa c mit kappa = -0,50000005 bis -0,50000011,
  Rest 2,9e-6 bis 6,4e-6. Das entspricht V und S in UEBERLEITUNG-V-1/-2 [P].
- **Reduzierte Form:** A_red positiv definit in allen Netzen, fuer A2 und fuer M_eff. Der Projektionsrest a nach dem Zug
  liegt im Median bei 1,7 % (M_eff) bzw. 1,4 % (A2). Er aendert das Potential nicht (dV = 0 [E]; Lesart: Eichanteil [H]).
- **Wie stark sich die Massen selbst aendern (Frobenius, beschreibend):**
  - M_eff nach Rueckzug mit J um 2,2 bis 7,9 %. Der Energiesprung der Mode bleibt trotzdem klein (Tabelle); welcher
    Teil der Aenderung die Mode trifft, ist nicht aufgeschluesselt.
  - V_eff (4D) um 1,5e-8 bis 5,4e-7; B (3D-Regge) um <= 5,4e-14.
- **Kontrolllaeufe (s1 f0, mu = -1e-3 und -1e-4, je X und Y):**
  - Hubfolge umgekehrt: P gleich auf <= 5e-9 relativ, R auf <= 2e-6 (z. B. R X bei -1e-3: -5,9662418e-13 gegen
    -5,9662422e-13).
  - h = 2^-12: P aendert sich um <= 0,5 %, R X um <= 0,5 %. R Y aendert sich um 7 % (-1e-3) bzw. um Faktor 2,5
    (-1e-4: -1,5e-13 gegen -5,9e-14), also im Bodenbereich.
  - [N] s4 f5, h = 2^-12: R X von +2,40e-12 / +2,52e-12 (2^-10) auf -1,34e-13 / +1,28e-13. Der mu-unabhaengige R-Rest
    ist also ein Effekt des endlichen h. P aendert sich um <= 1,7 %.
- **Wiedergabe A2:** 48 von 48 Werten gleich den gespeicherten. Die Lagen bei -1e-3 entsprechen den gespeicherten
  (mu_X = -1,0e-3).
- **Pruefsummen:** lauf-69/PRUEFSUMMEN.txt (77 Dateien), lokal 77 von 77 gleich. UPLOAD-SHA256.txt (28 Dateien) und
  LAUF-CODE-SHA256.txt auf der .69 bestanden.

## 6. Grenzen

- Linear um flach, statische Einzelzuege (Energie direkt vor und nach dem Zug), kein Zeitverlauf. Nur 2-3-Zuege, nur
  Geometrie (kein Skalar, kein Licht).
- Glas N = 128, Bloch k = 0 auf der ganzen Box, eine TT-Mode (k1). Feste Zelthoehe h = 2^-10 (nicht nach h -> 0
  extrapoliert), Schema ls, Fassung B, Hubfolge nach Eckindex (umgekehrt nur an einem Fall geprueft).
- Die Reduktion S (mit c[:, 1:] und 1_E bei k = 0) ist von td.Netz / A2 uebernommen, die Form A = M_eff^-1 von
  uv.reduktion [P]. Ob das die richtige Hamiltonform am Zug ist (etwa gegen (S^T M_eff S)^-1), ist nicht geprueft.
- p ~ 1 ist eine Steigung aus 2 bzw. 3 mu-Werten (je Faktor 10). Das Bild "verschwindet linear an der
  Kosphaerizitaet" gilt nur in diesem Bereich.
- Warum gerade die Kosphaerizitaet zaehlt, obwohl die Regge-Wirkung keine Hodge-Sterne enthaelt, ist offen. [H, nicht
  geprueft]: Die Schur-Elimination des Gitterrests erzeugt Gewichte wie die eines Umkreis-Duals. Ein |mu|^1 passt zu
  dualen Kanten (KANON-TRANSFER-1, Lesart 2 [P]).
- 12 von 32 Faellen, gewaehlt nach Saat und Art, vor jedem M_eff-Wert. Bei der Auswahl kannte ich die A2-Werte aus
  KANON-TRANSFER-1 und habe einige Faelle mit grossem A2-Sprung in P mitgenommen. 1/2 ist der einzige T-Fall.
- Der R-Boden um 1e-13 absolut (1e-9 relativ) ist nicht geklaert. Er waechst bei kleinerem h; Rundung in der
  Schur-Ausloeschung waere eine Erklaerung [H].
- Synthetisch, keine Messdatenbestaetigung.

## 7. Regelabweichungen und Vorfaelle

1. **Plattenvorfall .69 (15:07 bis 15:08 UTC):** nicht betroffen. Uploads 15:14:33 bis 15:14:36 UTC, alle 28 Dateien
   per sha256 bestaetigt (UPLOAD-SHA256.txt). Erster Lauf 15:14:56 UTC. Spaetere Uploads als .neu, dann mv, jeweils mit
   sha256sum -c.
2. **Werkzeug-Hintergrund unter /tmp:** Ein Warte-Befehl (ssh mit until-Schleife, bis zu 600 s) lief ueber die
   Werkzeuggrenze. Das Werkzeug hat ihn in den Hintergrund verschoben, die Ausgabe liegt unter
   /tmp/claude-1000/.../tasks/beeion74u.output. Kein eigener Schreibbefehl, Inhalt nicht gelesen.
3. **/dev/null auf der .69:**
   - Die Kettenaufrufe lesen stdin aus /dev/null, damit systemd-run --pipe die Liste nicht verbraucht.
   - In einem Statusbefehl stand einmal `2>/dev/null` (cat auf der .69).
   - Lokal nichts nach /dev/null, /tmp oder /dev/shm geschrieben.
4. **Vier Fehlstarts (rc = 1, je etwa 1,4 s):** u4-s1-f0-mu5, u4-s1-f2-mu5, u4-s2-f5-mu5 und u4-s3-f4-mu5. Ursache:
   KeyError, weil KANON-TRANSFER-1 keine Werte bei -1e-5 hat. Neu gestartet ohne --kanon (code/kette5.sh) als ...-mu5c.
   Logs erhalten (fehl-u4-s1-f0-mu5.log, fehl-u4-s2-f5-mu5.log, u4-s1-f2-mu5.log, u4-s3-f4-mu5.log).
5. **Code zwischen Rauchtest und Hauptlaeufen ergaenzt:** Optionen --h, --hubfolge und --muster. Rauchtest mit
   umklapp4d.py a33738e0..., alle Hauptlaeufe mit cfda516a... Der Rechenweg ist unveraendert, A2 und M_eff von s1 f0 X
   sind gleich.
6. **Nach Sicht ergaenzt [N]:** mu = -1e-5 (4 Faelle), h = 2^-12 fuer s4 f5 (wegen des R-Rests), Kontrolllaeufe.
7. **sleep:** nur auf der .69 (until-Schleifen mit sleep 5/6, einzelnes sleep 1 bis 3 nach Starts). Lokal kein sleep.
8. **Lokale Werkzeuge:** jq nur lesend (Anzeige mit -c, del, Objektbau), sed -n zum Ansehen, einmal sed mit Ersetzung
   in eine neue Datei (kette.sh -> kette5.sh), cat mit gequotetem Heredoc fuer Listen und Ketten, cp, scp, ssh,
   sha256sum, grep, ls, wc, date.
   - Kein Interpreter lokal, alle Rechnungen und die Auswertung auf der .69 ueber kleintest.sh (cpu5, cpu6).
   - 41 Aufrufe, der laengste 84 s.
9. Code nur kopiert (kanon-transfer-1/code, ueberleitung-v-2/code), dort nichts geaendert. Geschrieben nur in
   RUNDE-37/umklapp-4d-1/ und auf der .69 in /home/fmh/fmhc-physics-remote/umklapp-4d-1/. Keine Nachrichten nach aussen,
   nichts installiert. Journal, Peerbus und Commit uebernimmt die Leitung.

## 8. Einfach gesagt

Wenn das Netz an einer Stelle umklappt, sprang bisher die Energie der Schwerewelle, weil wir die Traegheit der Kanten
von Hand festgelegt hatten. Nimmt man stattdessen die Traegheit, die aus der vierdimensionalen Raum-Zeit-Regel selbst
folgt, wird der Sprung mindestens etwa 60-fach, meist tausend- bis zehntausendfach kleiner, und er schrumpft weiter, je
naeher das Netz am eigentlichen Umklapppunkt ist. Der alte Sprung kam also von der gesetzten Traegheit und nicht vom
Umklappen selbst; alles sind Rechnungen an einem kleinen Modellnetz, keine Messungen.

## 9. Dateien

- code/: umklapp4d.py (Rechnung), u4_auswertung.py (Auswertung), kette.sh, kette5.sh, liste-cpu5*.txt,
  liste-cpu6*.txt. Unveraenderte Kopien: td, hm_td, tg, uk, tu, tp, ew, mn, tg_auswertung, konfluenz, kanon
  (kanon-transfer-1) sowie rk, rk2, pt, uv, hm, tti, dn, nachtrag_kinetik (ueberleitung-v-2).
- eingabe/: konfluenz-s1..s4.json und kanon-s1..s4.json (Kopien aus kanon-transfer-1).
- rauch-69/: r1.json, r1.log. lauf-69/: u4-*.json und u4x-*.json mit Logs, auswertung.json, auswertung.md,
  kette-*.txt, PRUEFSUMMEN.txt.
- Pruefsummenlisten: UPLOAD-SHA256.txt, LAUF-CODE-SHA256.txt, LISTE-B/C/D-SHA256.txt.
- Auf der .69: /home/fmh/fmhc-physics-remote/umklapp-4d-1/ (code/, eingabe/, rauch/, lauf/).

---
Abgabe: 2026-10-05 17:48:04 CEST (date). Zeitrahmen etwa 90 min ab 17:04:23 CEST eingehalten. Kein Lauf mehr aktiv (auf der .69 keine u4-Unit gelistet). Nicht frisch gegengelesen (Versuch ohne Karte).
