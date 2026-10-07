# QBALL-HADRON-1, Teil 2: Plan (vor den Hauptlaeufen, wird eingefroren)

- Geschrieben ab 2026-10-05 06:20:53 CEST (date), nach LOGIK.md (Teil 1, Rohdatenprobe, Entscheidung) und nach sieben
  Rauchtests (Abschnitt 6). Vorhersagen QH0 bis QH2 und ihre Bedeutung stehen unveraendert in KARTE.md.
- Explorativ (v3). Synthetische Rechnung im Modell M1 (U(S) = S - S^2 + S^3/2), keine Messdatenbestaetigung.
- "Stabil" wie DIM-LEITER: E < Q bzw. VK-stabil; in 2D zusaetzlich die lineare Ringstabilitaet nach HAGEDORN-1/-2
  (A-Regel), nur beschreibend.

## 1. Methode

- **E bei festem Q direkt [M]:** Mit Q = 2 omega N (N = Int f^2) ist omega^2 N = Q^2/(4N), also
  E = G[f] + Q^2/(4 N[f]) =: E_Q[f], G = Int [|grad f|^2 + Zentrifugalterm + U(f^2)]. Stationaere Punkte von E_Q sind
  Q-Baelle mit omega = Q/(2N). Der Ball des unteren Asts ist ein Minimum von E_Q im Ansatz. Kein omega-Raster, keine
  Interpolation (die Schwaeche der Altdaten, LOGIK.md Abschnitt 6).
- **Numerik (code/festq.py):** zellzentriertes Gitter, diskretes Funktional mit analytischem Gradienten, L-BFGS-B
  (scipy) in skalierten Variablen f sqrt(W). Erst Gitter 2h, dann h (Start interpoliert). Richardson
  E_R = (4 E_h - E_2h)/3 ist der Hauptwert.
  - radial (2D, Windung m; D = 3, 4 nur m = 0)
  - axi3: f(rho, z), gerade Paritaet (Halbraum z >= 0), J = m Q
  - dop4: f(rho1, rho2), Windungen (m1, m2), J1 = m1 Q, J2 = m2 Q
- **Gegenproben je Loesung:** Virial E = omega Q + (2/D) K; Rest der diskreten Feldgleichung; Randwert von f; E < Q
  und omega < 1 (gebunden); h gegen 2h.
- **Gegenproben gegen Fremdcode:**
  - 2D gegen RG-1 (Schiessen): Rauchtest an drei RG-1-Zeilen (omega^2 = 0,55, m = 0, 1, 2) bei deren Q:
    E_R = 185,862917 / 297,311263 / 506,834558 gegen 185,862916 / 297,311263 / 506,834557 (rel. <= 2e-9) [E, Rauch].
  - 3D m = 0 gegen DIM-LEITER d3.json, 4D m = 0 gegen d4.json (Hermite auf deren dichtem omega^2-Raster).
- **2D, Weg A (Karte):** RG-1-Code (Kopie, unveraendert) mit dichten Zeilen omega^2 = 0,52 bis 0,70 in Schritten
  0,0025 (73 Werte, code/w2-dicht.txt), m = 0 bis 4, h0 = 0,01 und 0,005 (L3). E(m) bei Q = 300 bis 1400 durch Hermite
  mit dE/dQ = omega auf den kurzen Intervallen.
- **QH0, Codeweg:** RG-1-Kopie, Standardtabelle neu auf der .69 (tabelle --h 0.01, Voreinstellungen), dann bahn;
  Exponent der Rotorprobe bei Q = 300.

## 2. Laeufe (.69, kleintest.sh, 1 Thread, je hoechstens 10 min; Spuren cpu und cpu7)

| Name | Spur | Inhalt | geschaetzt |
|---|---|---|---|
| qh1-rg1std | cpu | regge2d.py tabelle --h 0.01 --out lauf/rg1-std-h001 | 1 bis 3 min |
| qh1-rg1bahn | cpu | regge2d.py bahn --tabelle lauf/rg1-std-h001/ergebnis.json --out lauf/rg1-std-bahn | < 10 s |
| qh1-rg1dicht | cpu7 | regge2d.py tabelle --h 0.01 --m 0,1,2,3,4 --w2 (dicht) --ohne-nls --ohne-gitter | ~3 min |
| qh1-rg1dichtl3 | cpu | dasselbe mit --h 0.005 | ~6 min |
| qh1-b2d | cpu7 | festq radial D = 2, m = 0..4, Q = 300, 400, 600, 800, 1000, 1200, 1400, 2000, 3000, 5000, 8000, 12000; h = 0,05; Kasten 1,4 R + 30 | ~2 min |
| qh1-d3a | cpu7 | festq axi3, m = 0..3, Q = 500, 1000, 2000, 3000; h = 0,15; Kasten 2,2 R + 15 | ~4 min |
| qh1-d3b | cpu | festq axi3, m = 0..3, Q = 5000, 10000, 30000; h = 0,15 | ~6 min |
| qh1-d4 | cpu7 | festq dop4, (0,0), (1,0), (1,1), (2,0), Q = 10000, 30000, 100000, 300000; h = 0,2; Kasten 2,2 R + 15 | ~3 min |
| qh1-ausw | cpu | code/auswertung.py ueber alle Ausgaben | < 10 s |

- R ist der Duennwandradius r_kugel(D, Q) aus festq.py. Aufrufe woertlich in code/start_haupt.sh.
- Laeuft ein Lauf an die 10 min, wird er geteilt (neue Datei, gleicher Code), nicht der Code geaendert.

## 3. Groessen

- 2D: E(m) bei festem Q, R2, R3, R4 (Karte), dazu Delta E_2/Delta E_1; je Mitglied omega^2, E/Q, Halbwertsradien,
  A, Stabilitaetsetikett (HAGEDORN-Regel, beschreibend).
- 3D: E(m), m = 0..3, R2, R3; gebunden ja/nein; Form: Ort des Dichtemaximums (rho_max, z_max), Halbwertsradien innen
  und aussen bei z ~ 0, Halbwertshoehe, Energiedichte in der Mitte durch Maximum. **Torus** heisst hier: Maximum der
  Ladungsdichte bei rho_max > 0 und Energiedichte in der Mitte unter der Haelfte des Maximums.
- 4D: E(0,0), E(1,0), E(1,1), E(2,0); R2 laengs (m, 0); **K = (E^2(1,1) - E0^2)/(E^2(2,0) - E0^2)**: Regge 1,
  kleiner Rotor 0,5 (LOGIK.md Abschnitt 3).
- Hadronen: R2 = 1,980, R3 = 2,875 (PDG 2024).

## 4. Eigene Vorhersagen (vor den Hauptlaeufen; die Rauchtests unten sind gesehen)

Die Kartenvorhersagen QH0 bis QH2 bleiben unveraendert. Zusaetzlich, offen gelegt mit Stand:

| Nr | Vorhersage | p | Stand |
|---|---|---|---|
| P1 | 2D, Q = 1000: R2 (m = 0, 1, 2) zwischen 2,1 und 2,6 | 0,6 | vor jeder 2D-Rechnung bei Q = 1000 (Altdaten: 2,13 bis 2,86) |
| P2 | 2D: R2(Q) waechst im stabilen Band mit Q (Richtung Rotor 4) | 0,7 | Schreibtisch LOGIK.md Abschn. 4; nicht gesehen |
| P3 | 3D, Q = 3000: R2 zwischen 1,6 und 2,4; R3 < 3 | 0,5 | **nach Rauchtest r6 (h = 0,3) gebildet: R2 ~ 1,91, R3 ~ 2,65 gesehen**, also kein Blindwert |
| P4 | 3D: fuer m >= 1 Tori nach Abschnitt 3 | 0,7 | Rauchtest ohne Formausgabe angesehen |
| P5 | 4D: K zwischen 0,5 und 0,8 | 0,6 | **vor dem Rauchtest r5 gedacht, dort K ~ 1,5 (Q = 3e4) und 1,44 (1e5) gesehen**; ich lasse P5 so stehen, es wird scheitern |
| P6 | 4D, Q = 10000: (1,1) und (2,0) nicht gebunden | - | im Rauchtest r4 gesehen (E/Q 1,027 und 1,008), keine Vorhersage |

## 5. Urteilsregeln (vorab)

- **QH0:** eingetroffen, wenn der Codeweg (Standardtabelle neu, bahn) bei Q = 300 einen Exponenten innerhalb
  0,899 +- 0,01 gibt. Der Datenweg (LOGIK.md Abschn. 6: 0,89887) zaehlt nur als Nebenzeile, weil er zwangslaeufig ist.
- **QH1:** bei Q = 1000 (Rotorprobe von RG-1; dort sind m = 0, 1, 2 nach der A-Regel stabil, LOGIK.md Abschn. 6).
  Hauptzahl Weg B (Richardson). Eingetroffen, wenn |R2 - 2| <= 0,2. Weg A muss auf 1e-3 gleich sein, sonst beide
  nennen und als Befund vermerken. R3 (m = 3, Grauzone der A-Regel) nur beschreibend.
- **QH2:** aus LOGIK.md, ohne Rechnung.
- **Regge im Modell (Pruefstein, Erweiterung 1):** nur, wenn R2 = 2 +- 0,2 und R3 = 3 +- 0,3 auf dem ganzen
  stabilen Q-Band der Q-Liste gelten. Sonst "kein Regge-Gesetz bei festem Q".
- **4D:** K >= 0,9 "Regge-artig", K <= 0,6 "rotorartig", dazwischen "weder noch"; K > 1,1 "weder Regge noch Rotor"
  (gemischte Drehung teurer als doppelte Windung).

## 6. Rauchtests (alle .69, kleintest.sh, <= 120 s; rauch/)

| Lauf | Spur | Inhalt | Laufzeit | rc |
|---|---|---|---|---|
| qh1-rauch1 | cpu | radial D = 2, m = 0, 1, 2 bei Q = 238,43 (RG-1-Zeile 0,55, m = 0) | 1,9 s | 0 |
| qh1-rauch2/2b | cpu | radial m = 1 bei Q = 370,21 und m = 2 bei Q = 627,88 (RG-1-Zeilen) | je < 2 s | 0 |
| qh1-rauch3 | cpu7 | axi3 m = 0, 1, Q = 1000, h = 0,3 | 1,7 s | 0 |
| qh1-rauch4 | cpu7 | dop4 Q = 10000, h = 0,4 | 2,2 s | 0 |
| qh1-rauch5 | cpu7 | dop4 Q = 30000 und 100000, h = 0,4 | 6,5 s | 0 |
| qh1-rauch6 | cpu | axi3 m = 0..3, Q = 3000, h = 0,3 | 7,3 s | 0 |
| qh1-rauch7 | cpu | RG-1-Kopie, 15 dichte Zeilen (Zeitprobe) | 7,9 s | 0 |

- Ein Rauchtestversuch (Startbefehl mit relativem Pfad, Verzeichnis falsch) lief nicht an; danach nur absolute Pfade.
- 3D m = 0 bei Q = 1000 (h = 0,3): E_R = 859,58 gegen DIM-LEITER (Hermite, von Hand) 859,58.

## 7. Grenzen

- Ansatz erzwingt Achsensymmetrie (3D) bzw. die doppelte Drehsymmetrie (4D) und gerade Paritaet. Ein Zerfall in
  Teilstuecke ist damit ausgeschlossen; Stabilitaet wird in 3D/4D nicht geprueft.
- E_Q-Minimierung findet nur den unteren Ast. Q_min(m) (Wendepunkt) wird nicht bestimmt, nur "gebunden ja/nein" bei
  den gerechneten Q.
- Klassische Rechnung: J = m Q ist stetig in Q; Quantisierung kommt nicht vor.
