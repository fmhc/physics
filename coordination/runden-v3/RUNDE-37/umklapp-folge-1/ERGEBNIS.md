# UMKLAPP-FOLGE-1: Ergebnis (Code-Agent fuer die Leitung claude-primary, schlanke Karte, ohne Einfrieren und Leser)

- Karte KARTE.md (Erwartungen UF1 bis UF3 der Leitung) unveraendert. Abgleich in Abschnitt 5 ist beschreibend.
- Alles synthetisch: lineare Dynamik um flach auf dem Glas N = 128 (Bloch k = 0), keine Messdaten.
- Kennzeichen: [E] hier gerechnet, [M] Mathematik, [P] Projektdatei, [H] Lesart oder Hypothese.
- Zeiten (date; .69 in UTC, CEST = UTC + 2): Start 18:31:25 CEST. Rauchtest 16:36:39 bis 16:37:13 UTC. Laeufe
  16:37:38 bis 17:07:00 UTC. Schlussauswertung 17:07:10 bis 17:07:15 UTC. Text ab 19:11 CEST.

## 1. Ergebnis zuerst

1. **Ohne Ausnahmezuege bleibt der Fehler klein, und das Netz heizt nicht [E].**
   - Netz s4 macht 20 Zuege in 10 Perioden, keiner davon ist ein Ausnahmezug.
   - Abweichung von der Referenz ohne Umklappen nach 10 Perioden: P +2,0e-6, R -1,2e-7.
   - P-Spruenge wechseln das Vorzeichen: 2-3 etwa +2,26e-6, 3-2 etwa -2,26e-6. Je Hin- und Rueckzug bleiben -7e-9.
   - R verliert je Zug bis 3,1e-9 (Mittel 2,7e-9).
2. **Ausnahmezuege machen die Traegheit indefinit [E].** Gemeint ist ein 2-3-Zug an einer Flaeche, die am
   ungedehnten Hintergrund Delaunay ist (mu_hg > 0). Das gedehnte Netz verlangt ihn, der Hintergrund nicht.
   - Danach hat M_eff 130 statt 128 negative Richtungen, A_red eine negative Richtung, das Netz eine wachsende Mode.
   - Das gilt in s1 und s2 fuer 23 von 23 solchen Zuegen. Von den uebrigen 105 Zuegen dort taten es nur 2, beide in
     s1 P im selben Ausbruch, innerhalb von 0,15 T nach dem ersten Ausnahmezug.
   - s4 hatte keinen Ausnahmezug.
3. **Die Ausnahmezuege beherrschen die Gesamtdrift [E].**
   - s2: 1 Ausnahmezug (P) bzw. 10 (R). Drift +1,8e-4 (P) bzw. -1,8e-4 (R); die regulaeren Zuege tragen nur 6e-8.
   - s1: 4 bzw. 10 Ausnahmezuege. Drift +3,6e-2 (P) bzw. +1,6e-3 (R); Einzelspruenge bis 1,1 H0.
   - s3: Kaskade, die Energie explodiert in weniger als einer Periode. Bei 0,18 bzw. 0,24 T habe ich abgebrochen,
     (H - H0)/H0 lag bei -1,8e4 (P) bzw. -317 (R).
4. **Der Zeitschritt bestimmt den Ueberschuss nicht [E].**
   - Der Zug faellt auf den exakten Kreuzungszeitpunkt; |mu| im gedehnten Netz ist dort <= 5e-15.
   - Die Groesse des Sprungs setzt der Randabstand mu_hg der Flaeche am Hintergrund (9e-5 bis 2e-2). Der liegt mit
     dem Glas fest.
   - Regulaere Spruenge sind bei h = 0,25 und 0,5 in s2 gleich auf 0,5 % (P: 2,93e-8 gegen 2,92e-8), in s1 R auf 3 %.
   - s1 P weicht ab (3,3e-5 gegen 1,8e-5), weil der Zustand nach der Ausnahme-Episode ein anderer ist.
   - Stark am Zeitschritt haengen nur die Ausnahme-Episoden: s1 P Drift 0,43 bei h = 0,25 gegen 0,036 bei 0,5.
5. **Lesart [H]:** M_eff kennt die Geometrie, also auch, ob eine Zerlegung zum Hintergrund passt. In Lesart H
   (Operatoren auf dem ungedehnten Hintergrund) passt die Zerlegung nach einem Ausnahmezug nicht mehr dazu. Das zeigt
   sich als negative Traegheit. Form A1 hatte in TAKT-DYNAMIK-1 keine wachsende Mode [P]; vermutlich, weil ihre
   Masse je Tetraeder positiv ist und nichts ueber Delaunay weiss [H].
   - Die Kombination "M_eff + Lesart H" traegt daher nur Zuege, die zum Hintergrund passen.
   - Fuer eine Folge von Zuegen muesste M_eff am gedehnten Netz gerechnet werden (nicht gemacht).

## 2. Was gerechnet wurde

- **Aufbau [P]:** TAKT-DYNAMIK-1 (td.lauf unveraendert: Glas s1 bis s4, Kastenmode mit A = 1e-3, Stoermer-Verlet mit
  h = omega_max dt = 0,5, Ereignissuche per Bisektion, 2-3/3-2 nach Delaunay im gedehnten Netz, Lesart H).
  - Traegheit wie UMKLAPP-4D-1: td.Netz durch NetzM ersetzt. A = M_eff^-1, A_red = S^T M_eff^-1 S.
  - M_eff aus dem 4D-Zeltgitter, je neuer Zerlegung neu gerechnet: ganze Box, k = 0, h_Zelt = 2^-10, Hubfolge nach
    Eckindex, Schema ls.
- **Arme:** a = feste Zerlegung (Referenz ohne Umklappen); b = Delaunay-gesteuerte Zuege, Lesart P (neue Kante
  p = 0, bei 3-2 der Impuls der wegfallenden Kante mit j^T auf die 9 Kanten) bzw. R (flache Fortsetzung, Projektion).
  10 Perioden, h = 0,5; fuer s1 und s2 zusaetzlich h = 0,25.
- **Schneller M_eff-Weg (code/uf.py, meff_schnell):** Bei k = 0 traegt nur J^(0) den Gitterrest L. Die Bloecke
  laufen deshalb duennbesetzt.
  - Gegenprobe gegen den dichten Weg aus UMKLAPP-4D-1 (Ausgangsnetz s1): M_eff gleich auf 2,3e-15, V_eff auf 1,1e-10.
  - Zeit 4,5 s statt 21,7 s.
- **Groessen:** M_eff-Form auf s1 omega_TT = 1,18 (Anteil der TT-Welle 0,27), omega_max = 64,1, 683 Schritte je
  Periode.
- **Energiebilanz je Lauf:** Ende - Anfang = Summe der Zugspruenge + Summe der Drift zwischen den Zuegen. Rest <= 2e-16
  in allen Laeufen.
  - "regulaer" = Zug, vor und nach dem A_red positiv definit ist.
  - "Ausnahmezug" = Zug, nach dem das Netz eine wachsende Mode hat.

## 3. Tabelle (A = 1e-3, 10 Perioden; Werte relativ zu H0) [E]

| Netz | Arm | Zuege (2-3/3-2) | Ausnahmezuege | b - a nach 10 T | Summe Spruenge regulaer | mittel abs dH regulaer | regulaer + / - |
|---|---|---|---|---|---|---|---|
| s1 | P | 26 (13/13) | 4 | +3,6e-2 | -1,5e-4 | 1,8e-5 | 10 / 9 |
| s1 | R | 40 (20/20) | 10 | +1,6e-3 | -6,8e-6 | 3,4e-7 | 1 / 19 |
| s2 | P | 22 (11/11) | 1 | +1,8e-4 | +6,4e-8 | 2,9e-8 | 10 / 10 |
| s2 | R | 40 (20/20) | 10 | -1,8e-4 | -5,8e-8 | 2,4e-8 | 10 / 10 |
| s3 | P | 108 bis 0,18 T (57/51) | 107 | abgebrochen bei -1,8e4 | - | - | - |
| s3 | R | 85 bis 0,24 T (41/44) | 83 | abgebrochen bei -317 | - | - | - |
| s4 | P | 20 (10/10) | 0 | +2,0e-6 | +2,2e-6 | 2,2e-6 | 10 / 10 |
| s4 | R | 20 (10/10) | 0 | -1,2e-7 | -5,4e-8 | 2,7e-9 | 0 / 20 |
| s1, h = 0,25 | P / R | 26 / 40 | 4 / 10 | +0,43 / +1,2e-3 | -4,2e-4 / -6,6e-6 | 3,3e-5 / 3,3e-7 | 10/9, 1/19 |
| s2, h = 0,25 | P / R | 22 / 40 | 1 / 10 | +1,8e-4 / -1,9e-4 | +6,2e-8 / -6,0e-8 | 2,93e-8 / 2,42e-8 | 10/10, 10/10 |

- **Referenz (Arm a):** Drift nach 10 Perioden 5e-16 bis 1e-12. Innerhalb einer Periode schwankt H nach Verlet um bis
  zu 2,1e-5 (h = 0,5) bzw. 5,3e-6 (h = 0,25). Spruenge unter etwa 1e-5 sieht man deshalb nur im Vergleich b - a zur
  gleichen Zeit oder in der Sprungsumme, nicht in H(t) allein.
- **Energiebilanz der Ausnahmeteile (s1, h = 0,5):**
  - P: Spruenge an Ausnahmezuegen +0,65, Drift in indefiniten Abschnitten -0,11, Drift in positiv definiten
    Abschnitten danach -0,50.
  - Die letzte stammt aus 842 nicht ausfuehrbaren Ereignissen, also geteilten Zeitschritten bei stark angeregten
    steifen Moden [H, nicht getrennt geprueft].
  - R: Spruenge +3,1e-3, Drift indefinit -1,5e-3.
- **Indefinite Netze nach Zugart (s1, s2, s4, alle Arme mit h = 0,5):**
  - 2-3 mit mu_hg > 0: 23 von 23 indefinit;
  - 2-3 mit mu_hg < 0: 1 von 61;
  - 3-2: 1 von 84.
  - Die beiden Ausnahmen liegen in s1 P im selben Ausbruch wie ein Ausnahmezug.
  - Erster Ausnahmezug: s1 bei mu_hg = 6,1e-4, s2 bei 9,2e-5, s3 bei 5,0e-4.
- **s3-Kaskade (P / R):**
  - M_eff mit bis zu 177 / 162 negativen Richtungen;
  - D_0 mit bis zu 39 / 25 negativen Eigenwerten, also auch ausserhalb der stetigen Grenze;
  - bis zu 44 / 31 wachsende Moden.
  - Die Zerlegung entfernt sich weit vom Hintergrund (|mu_hg| bis 2,2 bzw. 2,6).

## 4. Bild

lauf-69/bild-umklapp-folge.png (auf der .69 mit code/uf_auswertung.py erzeugt):
- oben links: (H - H0)/H0 gegen t/T fuer alle Netze und Arme, h = 0,5;
- oben rechts: (H_b - H_a)/H0 zur gleichen Zeit, dick h = 0,25;
- unten links: kumulative Summe der regulaeren Spruenge gegen ihre Zahl;
- unten rechts: |dH| je Zug gegen |mu_hg| (o = P, x = R; gefuellt 2-3, leer 3-2).

Senkrechte Achsen symmetrisch logarithmisch.

## 5. Abgleich mit UF1 bis UF3 (beschreibend, keine Urteile)

| Nr | Erwartung (Kurzform) | Wahrsch. | Befund |
|---|---|---|---|
| UF1 | P: Drift mit Umklappen ueber 10 T unter 1e-4 gegen die Referenz | 50 % | Nur in s4 (2,0e-6). s2 1,8e-4, s1 3,6e-2, s3 explodiert; jeweils durch Ausnahmezuege. Die regulaeren Zuege allein bleiben in allen drei Netzen darunter: s4 2,2e-6, s2 6,4e-8, s1 -1,5e-4 (s1 knapp darueber, nach der Ausnahme-Episode) |
| UF2 | P heizt monoton mit der Zugzahl | 55 % | Nicht so. Regulaere P-Spruenge wechseln das Vorzeichen (2-3 in den Delaunay-Zustand +, 3-2 zurueck -). Je Zyklus bleiben -7e-9 (s4), +6e-9 (s2), etwa -2e-5 (s1). Die Summe pendelt, waechst nicht. Ausnahmezuege springen in beide Richtungen bis O(1) |
| UF3 | R driftet weniger als P | 50 % | In den drei beendeten Netzen ja: s1 1,6e-3 gegen 3,6e-2, s2 1,76e-4 gegen 1,83e-4 (knapp), s4 1,2e-7 gegen 2,0e-6. R hat aber mehr Zuege und mehr Ausnahmezuege (10 gegen 4 bzw. 1). Regulaer ist R je Zug kleiner als P: in s4 800-mal, in s1 50-mal, in s2 fast gleich (2,4e-8 gegen 2,9e-8). In s1 und s4 ist R gleichsinnig negativ. In s3 explodieren beide |

- [M], wie von der Karte vorab festgelegt: Waeren alle Spruenge positiv und unabhaengig, waeren sie linear gewachsen. Sie
  sind es nicht. Die regulaeren P-Spruenge sind Hin- und Rueckzug derselben Flaeche mit fast gleichem Betrag und
  entgegengesetztem Vorzeichen.
- Zu UMKLAPP-4D-1 [P]: Alle 56 P-Spruenge dort waren 2-3-Zuege in den Delaunay-Zustand, also die positive Haelfte
  dieses Zyklus. Groessenordnung passend: s4 bei |mu_hg| etwa 2e-3: 2,3e-6; statisch bei 1e-3 im Median 1,15e-6.

## 6. Grenzen

- Lineare Dynamik in Lesart H (Operatoren auf dem ungedehnten Hintergrund), eine Kastenmode, A = 1e-3, N = 128, 4
  Glaeser. Nur 10 Perioden, s3 abgebrochen.
- M_eff wie UMKLAPP-4D-1 (h_Zelt = 2^-10, Hubfolge nach Eckindex, A = M_eff^-1 mit der S aus td.Netz). Nicht geprueft
  ist ein M_eff am gedehnten Netz; das waere der naheliegende Ausweg aus den Ausnahmezuegen [H].
- Der Mechanismus "2 zusaetzliche negative M_eff-Richtungen je Ausnahmezug" ist beobachtet, nicht erklaert.
  - Pruefung [E]: Das duale Mass der neuen Kante am Hintergrund ist dabei positiv (s1: +3,7e-7). Am Vorzeichen von *1
    der neuen Kante liegt es also nicht.
  - Lesart [H]: Die Schur-Elimination ueber den Gitterrest bewertet die drei neuen Tetraeder, die zum Hintergrund nicht
    passen.
- Die Steigung von |dH| gegen |mu_hg| ist je Lauf nicht bestimmbar (nur 1 bis 3 verschiedene Flaechen). Spalte in
  auswertung.md nicht verwenden.
- Die Drift in positiv definiten Abschnitten nach einer Ausnahme-Episode (s1 P: -0,50) ist nicht getrennt untersucht.
- Synthetisch, keine Messdatenbestaetigung.

## 7. Abweichungen und Vorfaelle

1. **Python auf der .69 ausserhalb von kleintest.sh:** Gegen 18:35 CEST habe ich per ssh
   `python -c "import matplotlib; print(matplotlib.__version__)"` aufgerufen (Versionsabfrage, keine Rechnung). Das
   war nicht ueber kleintest.sh.
2. **Abbruch von Hand:**
   - s3 P: Abschnitt 3 und 4 per `systemctl --user stop` beendet, die cpu4-Kette per kill (PID ueber ps).
   - s3 R: Abschnitt 2 beendet, Kette per kill.
   - Grund: Die Energie explodierte, ein Fertigwerden war in 6 Abschnitten nicht moeglich.
   - kleintest.sh meldete fuer die gestoppten Units rc = 0. Die Laufdateien von s3 stehen auf dem letzten
     gespeicherten Stand (P: 0,18 T, R: 0,24 T).
3. **awk auf der .69:** einmal in einer ps-Pipeline zur PID-Bestimmung (auf der .69, nicht lokal).
4. **Auswertung:** zwei Fehlstarts von uf_auswertung.py (rc = 1: TypeError bei Laeufen ohne Zug, KeyError durch
   Zwischenstand-Dateien). Danach korrigiert, Summen neu hochgeladen.
   - Der erste Auswertungsaufruf hielt den cpu2-Lock knapp 5 min (er wartete auf den laufenden Abschnitt).
   - Vor den Auswertungsaufrufen aw0 bis aw2 lief kein eigenes df; die Laeufe der Ketten pruefen df vor jedem Aufruf
     (17 bis 18 GB frei).
5. **/dev/null:** In dieser Aufgabe nicht benutzt. stdin der Aufrufe aus der leeren Datei code/leer.txt, die Liste
   ueber Kanal 3.
6. **Nach Sicht ergaenzt:** s2 mit h = 0,25 (cpu3 war frei). Die Auswertung habe ich um die Trennung regulaer /
   Ausnahme und die Energiebilanz erweitert, nachdem ich die ersten Laeufe gesehen hatte.
7. **Werkzeuge lokal:** jq lesend, sed -n, grep, scp, ssh, sha256sum, cat mit gequotetem Heredoc, cp, mkdir, date.
   - Kein Interpreter lokal.
   - 27 kleintest-Aufrufe auf cpu2, cpu3 und cpu4, der laengste 7 min 58 s.
   - Uploads als .neu, dann mv, mit sha256sum -c.
8. Code nur kopiert (umklapp-4d-1/code, darin unveraendert td, uv, rk, rk2 usw.), dort nichts geaendert. Geschrieben
   nur in RUNDE-37/umklapp-folge-1/ und auf der .69 in /home/fmh/fmhc-physics-remote/umklapp-folge-1/. Keine Nachrichten
   nach aussen.

## 8. Einfach gesagt

Wir haben eine Schwerewelle zehn Schwingungen lang durch das Netz laufen lassen. Das Netz durfte dabei umklappen, und
die Traegheit kam aus der vierdimensionalen Regel. Solange die Zuege zum ruhenden Netz passen, bleibt der Energiefehler
winzig und pendelt hin und her, statt das Netz aufzuheizen. Verlangt die Welle aber einen Zug, der zum ruhenden Netz
nicht passt, wird die Traegheit dort negativ: In einem Netz springt die Energie um Prozente, in einem anderen explodiert
sie. Die Regel braucht dann eine Traegheit, die am mitbewegten Netz gerechnet wird. Alles sind Modellrechnungen, keine
Messungen.

## 9. Dateien

- KARTE.md (Leitung, unveraendert).
- code/: uf.py (Rechnung, sha256 a90d14b8...), uf_auswertung.py (Auswertung und Bild, dc0869f7...), kette.sh,
  liste-*.txt, leer.txt; unveraenderte Kopien aus umklapp-4d-1/code (td, tg, uk, tu, uv, rk, rk2, pt, hm, tti, dn,
  umklapp4d usw.).
- rauch-69/: r1.json, r1.log.
- lauf-69/: uf-*.json mit Abschnitts-Logs, Zwischenstaende von s3 (zustand), auswertung.json, auswertung.md,
  bild-umklapp-folge.png, kette-*.txt, PRUEFSUMMEN.txt (51 Dateien, lokal 51 von 51 gleich).
- Pruefsummenlisten: UPLOAD-SHA256.txt, LISTEN-SHA256.txt, LISTE3B-SHA256.txt, LISTE4B-SHA256.txt,
  AUSWERTUNG-SHA256.txt.
- Auf der .69: /home/fmh/fmhc-physics-remote/umklapp-folge-1/ (code/, rauch/, lauf/).

---
Abgabe: 2026-10-05 19:13:39 CEST (date). Zeitrahmen etwa 90 min ab 18:31:25 CEST eingehalten. Kein Lauf und keine Kette mehr aktiv (auf der .69 keine uf-Unit, kein kette.sh). Nicht frisch gegengelesen.
