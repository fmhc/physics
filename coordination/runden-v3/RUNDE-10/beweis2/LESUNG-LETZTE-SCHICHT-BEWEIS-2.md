Urteil: letzte Schicht traegt mit Auflagen (L1 bis L4 Text, L5 optional; nichts blockierend, Strenge von T1 und T2 unberuehrt).

# Lesung der letzten Schicht, BEWEIS-2 (Neustart)

- Leser: frischer Leser, Haus Anthropic (Claude), im Auftrag der Leitung claude-primary
- Beginn (date): 2026-09-30 19:35:19 CEST
- Ende (date): 2026-09-30 19:48:21 CEST (Dauer 13 min 2 s, gerechnet als 48:21 - 35:19)
- Quote: 10 von 11 Auflagen umgesetzt (Anthropic A1 bis A6, OpenAI A1 bis A3 und Codehinweis), 1 teilweise
  (OpenAI A4, n-Reste). 58 neue oder geaenderte Zahlen geprueft, 0 falsch.
- Zeitbox: 25 min
- Nicht gelesen: LESUNG-LETZTE-SCHICHT-BEWEIS-2.abgebrochen-1330.md (bewusst, Frische)
- Gegenstand: BEWEIS-2.md, BEWEIS-2-PLAN.md, STAND.md (neue Fassungen), Vorfassungen *.bak-20260930-1313 nur zum Abgleich, LESUNG-BEWEIS-2.md, resonance-20260930/beweis2-fremdlesung/GESAMT-REVIEW.txt, zertifikat/

## 0. Hashes und Zertifikat

- sha256 BEWEIS-2.md = 3ad62460291f3a2d... (stimmt mit dem Auftrag), BEWEIS-2-PLAN.md = 0f8f0790dd8b262e... (stimmt),
  STAND.md = c852f4b901aa4b66..., LESUNG-BEWEIS-2.md = 47e351658bf9c774..., GESAMT-REVIEW.txt = 01522f7e919c85f3...
- zertifikat/: `sha256sum -c SHA256SUMS.txt` ergibt 37 OK, keine Abweichung; SHA256SUMS.txt hat 37 Zeilen, der Ordner
  hat 37 weitere Dateien, jede steht in der Liste. Alle mtimes <= 12:41, also vor der Einarbeitung (ab 13:13).
  Die Aussage "zertifikat/ unveraendert" ist damit bestaetigt (gegen die eigene Summendatei; einen aelteren,
  unabhaengig abgelegten Hash der Summendatei habe ich nicht geprueft).

## 1. Vorwaerts: Auflagen -> Stelle -> umgesetzt

Vorbemerkung: Die OpenAI-Lesung ist an die Vorfassungen gebunden (EINGANGSBINDUNG fe83a463... und 099f6335...);
das sind genau die sha256 von BEWEIS-2.md.bak-20260930-1313 und BEWEIS-2-PLAN.md.bak-20260930-1313. Die
Anthropic-Lesung hat A1 bis A6 (A6 optional), nicht nur A1 bis A5 wie im Auftrag genannt; ich pruefe alle sechs.

| Auflage | Stelle (neue Fassung) | umgesetzt | Bemerkung |
|---|---|---|---|
| Anthropic A1a: Ursache T2-B berichtigen | BEWEIS-2.md 217-238; Ergebnis 16-17; 6 Punkt 6 | ja | Profilzeilen statt l = 1-Zeilen; alle Zahlen per jq bestaetigt (Abschnitt 2 unten) |
| Anthropic A1b: M1-Fehlschlag nennen | 232-234 | ja | M1.rowsum 19,102934, BESTANDEN false |
| Anthropic A1c: l = 1-Breite nur der Zeilensumme der a-(und om-)Zeile in A und B2 zuordnen | 243-249; 6 Punkt 9 | ja | Die Lesung selbst (ihre Zeile 196) meint die a-Zeile mit den Spalten a und om; genau so steht es jetzt da |
| Anthropic A1d: STAND.md neue Zeile, alte bleibt | STAND.md Zeile 32 (neu), Zeile 24 (alt, unveraendert) | ja | diff gegen .bak: nur zwei Zeilen angehaengt |
| Anthropic A2: z0_rho aus den Z-Grenzen | 4.3, Zeilen 171-174 | ja | Mitte der Z-Grenzen stimmt auf alle Stellen (Rechnung in Abschnitt 2) |
| Anthropic A3: Gesamtflag-Satz T1 praezisieren; R < r_j durch Abbruch | 3, Zeilen 106-111 und 121-122; 4.5 Zeile 197 | ja, mit zwei Unschaerfen | N >= 1 und qfac > 1 stehen nicht in den Schrittprotokollen (Befund 3); "bricht der Lauf ab" beschreibt den Code ungenau (Befund 4) |
| Anthropic A4: Plan vor jedem Beweislauf einfrieren (kuenftig) | 6 Punkt 8, Zeilen 380-383; Abschnitt 8 "Offen" | ja, als Vorsatz | mehr ist nachtraeglich nicht moeglich; die Selbststempel sind offen benannt |
| Anthropic A5: Herkunft der l = 1-Breite klaeren, vor weiteren l >= 1-Laeufen | 4.5 Zeilen 250-254; 6 Punkt 9 | ja, als offene Frage | Die Auflage verlangt Klaerung erst vor weiteren Laeufen; als offen gefuehrt, zwei Kandidaten ausdruecklich ungeprueft |
| Anthropic A6 (optional): "BIC = regulaer bei 0" | 5.4 Zeile 336; Plan 4.5 Zeilen 121-122 | ja | |
| A6: Spaltenangabe a/om | 4.5 Zeile 243; 6 Punkt 9 | ja | nur Spalte a; om-Spalte relativ 3,5e-5 bis 5,6e-5 (D_relbreite A, B) |
| A6: rho-Obergrenze T1 | 1, Zeile 45 | ja | ...846998028 ist die richtige Aufrundung von ...8469980272986 (protokoll.Z) |
| A6: Logkopf "L 40" | 6 Punkt 10, Zeilen 391-392 | ja | im zert-Modus gilt `L = args.Lz or d['L']` (pruef-l1-c1f85f81.py:437), im Kontrollmodus `L = d['L']` (:681); "ohne Wirkung" stimmt |
| Anthropic F5 (keine Auflage) | Ergebnis 13-19; 4.5 Zeilen 239-242; 6 Punkt 6 | ja | |
| OpenAI A1: reelle Y_1m-Basis, sonst Y_lm* im zweiten Seitenband | Satz T2 Punkt 4, Zeilen 89-96; Plan 4.1 Zeilen 67-72 | ja | Begruendung im Plan nachgerechnet: conj(psi) bringt in das Seitenband e^{i rho t} den Faktor conj(Z), Schluss nur fuer Z = conj(Y) (bei reellen a, b) |
| OpenAI A2: Ableitungskern erklaeren | Plan 4.4 Zeilen 105-108 | ja | nachgerechnet: K_B = e^{kc r} G_B e^{-kc s} folgt aus Plan Zeile 98 und 102; d_r K_B = kc K_B + e^{kc r}(d_r G_B)e^{-kc s}; K_B(r, r) = 0, also kein Randterm; b2 = (2 + 2/x + 1/x^2)/2 mit x = kc L schrankt den Kern ab |
| OpenAI A3: Reproduktion mit historischem Hash | 7, Zeilen 421-424 | ja | |
| OpenAI A4: n als Leiterzuordnung; Krein kein Stabilitaetssatz | Ergebnis 21; Saetze Punkt 5; 6 Punkt 5 | teilweise | Krein ja; bei n bleiben Ordnungswoerter und eine Knotenaussage stehen (Befund 1) |
| OpenAI "Was die Lesung nicht zeigt" | 6 Punkt 5; "Nicht behauptet" 64-65, 100 | ja | ausser "Einfach gesagt", Satz 1 (Befund 5) |
| OpenAI Codehinweis | 6 Punkt 10, Zeilen 387-390 | ja | vermerkt, Code unveraendert (Hashkette) |

## 2. Rueckwaerts: neue und geaenderte Zahlen gegen zertifikat/

jq nur zum Auslesen; Dyadiken m * 2^e im Kopf umgerechnet, mit log10(2) = 0,30103 und
2^-299 = 10^-90,00797 = 9,8182e-91 (daraus 2^-300 = 4,9091e-91, 2^-294 = 3,1418e-89).

**Ursache T2-B (4.5, Zeilen 219-237; STAND.md Zeile 32), Quelle ZERT-T2-B-L40.json:**
- c-Zeile von Y (export.Y[1]): 1. Eintrag m hat 90 Stellen, 4,83564e89 * 9,8182e-91 = -0,47477; 2. Eintrag 91 Stellen,
  1,02780e90 * 9,8182e-91 = 1,00912; 3. Eintrag 4,74358e90 * 3,1418e-89 = -149,03; 4. Eintrag 1,03468e90 * 3,1418e-89
  = 32,508. Text (-0,4748; 1,0091; -149,0; 32,51): **stimmt**.
- Radien von D (export.DH0_Z, radius_m_e), Spalte a: Zeile 1: 635629269 * 2^-4 = 3,973e7; Zeile 2: 28010829 * 2 =
  5,602e7; Zeile 3: 673630391 * 2^-39 = 673630391 * 1,819e-12 = 1,2253e-3; Zeile 4: 562067713 * 2^-37 = 562067713 *
  7,276e-12 = 4,0896e-3. Text 3,97e7; 5,60e7; 1,23e-3; 4,09e-3: **stimmt**. Relativ (protokoll.D_relbreite):
  4,04e-10 und 1,21e-9, Text 4,0e-10 und 1,2e-9: **stimmt**.
- c-Zeile Spalte a: 0,4748 * 3,97e7 = 1,885e7; 1,0091 * 5,60e7 = 5,651e7; Summe 7,536e7, also **7,54e7 stimmt**.
  Zeilen 3 und 4: 149,0 * 1,23e-3 = 0,1833; 32,51 * 4,09e-3 = 0,1330; Summe 0,316, also **0,32 stimmt**.
- Spalte om: Radien 169813713 * 2^-2 = 4,245e7 und 12516749 * 4 = 5,007e7; 0,4748 * 4,25e7 = 2,018e7, 1,0091 * 5,01e7 =
  5,056e7, Summe 7,07e7 (**stimmt**). Zeilen 3 und 4: 1053808541 * 2^-40 = 9,584e-4 und 879286913 * 2^-38 = 3,1988e-3;
  149,03 * 9,584e-4 = 0,1428, 32,51 * 3,1988e-3 = 0,1040, Summe 0,247, also **0,25 stimmt**.
- delta (Feld delta): a 1,7451e-21, c 6,8874e-15, om 2,2311e-21; Text 1,75e-21, 6,9e-15 bzw. 6,89e-15, 2,23e-21: stimmt.
  Gewichtet: 7,536e7 * 1,7451e-21 = 1,3151e-13, geteilt durch 6,8874e-15 = 19,09; 7,0735e7 * 2,2311e-21 = 1,5782e-13,
  geteilt = 22,91; Summe 42,0. protokoll.zeilensumme_gewichtet = 41,99858: **stimmt** (Text 41,9986).
- Probe fuer delta_c: Y_c * H_0(z0) = 0,4748 * 2,219e-14 - 1,0091 * 1,1272e-14 + (Zeilen 3, 4: etwa 7e-20)
  = 1,0536e-14 - 1,1375e-14 = -8,39e-16; mal 8 = 6,71e-15; dazu 8 |Y_c| eps von etwa 1,7e-16 ergibt etwa 6,88e-15.
  Passt zu delta_c; die Aussage "Breite von H_0,1 <= 2,3e-18" stimmt als Radius (protokoll.H0_z0: +- 2,29e-18).
- M1: T2-B rowsum 19,102934, BESTANDEN false; B2 rowsum 1,4574382e-4; 19,102934 / 131072 = 1,4574e-4: **stimmt**
  (Text 19,10 und 1,457e-4 = 19,10 / 2^17). Zugleich ist 19,10 gleich dem Spalte-a-Anteil 19,09 der c-Zeile, das
  stuetzt die Zuordnung zum Profilblock.
- T1-B (ZERT-T1-B-L36.json): zeilensumme_gewichtet 0,0845145, M1.rowsum 0,0342172: Text 0,0845 und 0,0342 **stimmt**.

**l = 1-Breite (4.5 Zeilen 243-249; 6 Punkt 9):**
- D_relbreite Zeilen 3, 4, Spalte a: T2-A 1,34e-3 und 1,26e-3; T2-B und B2 1,64e-3 und 1,54e-3. Spanne 1,26e-3 bis
  1,64e-3, gerundet "1,3e-3 bis 1,6e-3": stimmt. "auch in B kaum kleiner als in A" ist schief: in B ist sie groesser
  (1,64e-3 gegen 1,34e-3), siehe Befund 6.
- Y-Zeile a, Eintraege 3 und 4 (T2-A: 77 Stellen, 5,1312e76 * 2^-256 = 5,1312e76 * 8,636e-78 = -0,4431 und
  4,4769e76 * 2^-258 = 4,4769e76 * 2,159e-78 = 0,0967; T2-B/B2: 9,0270e89 * 2^-300 = -0,4431 und 9,8449e88 * 2^-299 =
  0,0967): **stimmt** (-0,443; 0,0967).
- T2-A: Radien Zeilen 3, 4 Spalte a 276164785 * 2^-38 = 1,0047e-3 und 922247689 * 2^-38 = 3,3551e-3; 0,4431 * 1,0047e-3
  + 0,0967 * 3,3551e-3 = 4,452e-4 + 3,243e-4 = 7,695e-4 (Text 7,70e-4). Spalte om: 864074009 * 2^-40 = 7,859e-4 und
  721400157 * 2^-38 = 2,6244e-3; 3,483e-4 + 2,537e-4 = 6,019e-4 (Text 6,02e-4). Verhaeltnis delta_om / delta_a =
  2,70199 / 2,11068 = 1,2802; 6,019e-4 * 1,2802 = 7,706e-4; Summe 1,5401e-3 = protokoll 1,54012e-3: **stimmt**.
- B2: 0,4431 * 1,2253e-3 + 0,0967 * 4,0896e-3 = 5,430e-4 + 3,953e-4 = 9,383e-4; om: 0,4431 * 9,584e-4 + 0,0967 *
  3,1988e-3 = 4,247e-4 + 3,092e-4 = 7,339e-4; 2,23108 / 1,74509 = 1,2785; 7,339e-4 * 1,2785 = 9,383e-4; Summe
  1,8766e-3 = protokoll 1,87687e-3: **stimmt**. Damit ist auch belegt, dass die a-Zeile die groesste Zeilensumme stellt.
- "f im Kastenlauf bei L relativ 2872 (T2-A)": schritte_kasten.relw_f_bei_L = 2871,54: stimmt.

**z0_rho und Abstand (4.3, Zeilen 171-174), Quelle ZERT-T1-A-L32.json und ZERT-T1-B-L36.json:**
- .z0 ist in T1-A und T1-B bitgleich (sha256 der jq-Ausgabe gleich).
- Z-Grenzen rho in T1-A, Nachkommastellen ab der 19.: 80751940687893948893307701 und 84699802729857240974310004;
  Summe 165451743417751189867617705, halbe Summe 82725871708875594933808852,5. Also z0_rho =
  1,690356597328143456 827258717 08..., Text **1,690356597328143456827258717... stimmt**. Die Z-Grenzen von T1-B
  geben dieselbe Summe (82715392199807570527527996 + 82736351217943619340089709), also dieselbe Mitte.
- Kr_rho (export.Kr, T1-B) = 1,69035659732814345682727 +- 1,82e-24. Differenz zu z0 an den Stellen 22 bis 27:
  270000 - 258717 = 11283, also 1,1283e-23 (Text 1,13e-23 **stimmt**). delta_rho (T1-B) = 1,04795e-22;
  1,1283e-23 / 1,04795e-22 = 0,1077, Text **0,108 stimmt**. Kr-Radius 1,82e-24 / 1,04795e-22 = 0,0174, Text 0,017
  stimmt; die Angabe "+- 1,9e-24" ist die Aufrundung von 1,82e-24 (zulaessig, nach aussen).
- T1-Tabelle rho-Obergrenze ...846998028: Aufrundung von ...8469980272986 an der 27. Stelle, stimmt.

**Schrittprotokolle (3, Zeilen 107-111; 4.5 Zeile 197; 4.5 Zeile 215), jq-Filter ohne Arithmetik:**
- Anzahl Eintraege: T1-A 350 / 362, T1-B 487 / 508, T2-A 319 / 338, B2 445 / 472: stimmt mit Text.
- Schritte mit h <= 0 oder h >= R: in allen acht Dateien 0. "0 < h < R in allen Schritten": **stimmt**.
- Schritte mit r_j > 0 und R >= r_j: 0. Aber in jeder Datei gibt es genau einen Schritt mit r_j = 0 (den ersten, R > 0).
  "R < r_j in allen Schritten" stimmt also nur fuer die Schritte mit r_j > 0 (Befund 2).
- Die Schritteintraege haben die Felder R, f_real_oben, f_real_unten, fehlversuche, h, inflationsrunden, r_ende, r_j,
  relw_Y, relw_f, rest. N und qfac stehen nicht darin (Befund 3).

**Nicht nachgerechnet:** H_0, DH_0, Y als Inverse, Kr und die ODE-Einschluesse (wie beide Lesungen); die Newton-Zahlen
und Laufzeiten in 4.1 und 4.4 (unveraendert gegen die Vorfassung).

## 3. Absolute Aussagen

Ich habe Abschnitt 8 und alle Stellen aus dem diff gegen die .bak-Fassungen gelesen: BEWEIS-2.md 14-26, 45, 60-62,
89-98, 106-111, 121-122, 171-174, 197, 217-254, 336, 343-392, 421-454, 463-465; Plan 67-72, 106-108, 121-122; STAND
31-32. Pruefung jeweils gegen Code oder JSON.

| Aussage | Stelle | Pruefung | Ergebnis |
|---|---|---|---|
| "alle 350, 362, 487 und 508 Schritte erfuellen 0 < h < R" | 109 | jq-Filter auf 4 Schrittdateien: 0 Verstoesse | haelt |
| "R < r_j ... bestaetigen es fuer alle Schritte", "R < r_j in allen Schritten", "alle R < r_j" | 111, 197, 142 (alt) | je Datei ein erster Schritt mit r_j = 0 und R > 0; Code prueft nur r_j > 0 (bewkern.py:354-360) | zu weit, Befund 2 |
| "R < r_j steht in keinem Flag" | 110, 122 | protokoll.schritte_*.R_kleiner_rj_alle = true in allen Laeufen (pruef-l0.py:590, pruef-l1.py:638), nicht in M3 | ungenau, Befund 2 |
| "sonst bricht der Lauf ab", "durch Abbruch erzwungen" | 110-111, 122, 197, 439 | integrate faengt den Fehler und verkleinert R (bewkern.py:575-582, bewkern_l1.py:710-725) | Mechanismus falsch, Sache richtig; Befund 4 |
| N >= 1, qfac > 1 "aus den Schrittprotokollen geprueft" | 108-109, 439 | Schritteintraege haben kein N und kein qfac | Quelle falsch, Befund 3 |
| "Sie entstehen fast ganz aus den Profilzeilen" | 221-222 | 7,54e7 gegen 0,32 | haelt |
| "hat mit dem Scheitern von B nichts zu tun" | 244 | gewichteter Beitrag der Zeilen 3, 4 zur c-Zeile etwa 0,32 * 2,5e-7 + 0,25 * 3,2e-7, also etwa 1,6e-7 von 42 | haelt |
| "Ein Fehler in Code oder Lemma liegt nicht vor." | 238 | belegt ist: Fehlschlag ohne Fehler vollstaendig erklaert | zu absolut, Befund 7 |
| "Lemma K gilt fuer jeden Kasten" | 239, 363-364 | OpenAI-Lesung Zeile 61-63 bestaetigt Neuauswertung ueber Z; B- und B2-Schrittdateien bitgleich (cmp) | haelt |
| "Die Negativkontrolle ... erfuellen alle Laeufe ausser ... T2-B" | 372-373 | empfindlichkeitskontrolle in allen 5 JSON: 1/4 besteht und 4/1 verfehlt ausser T2-B | haelt |
| "etwa 0,11 delta daneben" (T1-B und T2-B2) | 369 | T1-B 0,108; T2-B2 rho: Kr 1,8263420301810699562427 +- 3,84e-23 gegen Z-Mitte ...995624216637915, Abstand 5,34e-22 = 0,118 delta_rho (Spanne mit Kr-Radius 0,110 bis 0,127) | vertretbar |
| "Nur dann traegt der gemeinsame Faktor Y_1m beide Seitenbaender" | Plan 69-70 | gilt bei reellen a, b bis auf einen Faktor +-1, +-i je Basisfunktion | haelt |
| "Kein neuer Lauf, keine Aenderung an zertifikat/" | 432 | sha256sum -c 37 OK, mtimes <= 12:41 | haelt |
| "nur Beschreibungsfehler gefunden, die jetzt berichtigt sind" | 464 | A4 (Prozess) und A5 (offene Frage) sind weder Beschreibungsfehler noch berichtigt | zu weit, Befund 5 |
| "bewiesen" | 11, 13, 459 | 11 und 13 mit "rechnergestuetzt, linear"; 459 ohne "linear" | Befund 5 |

## 4. Wortlaut der Grenzen

- **"einfach"**: ueberall als geometrische Vielfachheit 1 (Zeilen 29, 55-56, 86-88, 337, 354, 448); in den Saetzen
  ausdruecklich "bei festen (rho*, omega*)", algebraische Vielfachheit ausgeschlossen (56, 87, 356). Haelt.
- **"eingebettet"**: nur operational (30, 58, 93-94, 357, 448). Haelt.
- **n als Leiteretikett**: in 21, 359-360 und 447 richtig. Es bleiben aber Ordnungs- und Knotenaussagen stehen:
  Ueberschrift 67 "erste Schwapp-Stelle", "Einfach gesagt" 459-460 "die naechste Atmungsschwingung und die erste
  Schwappschwingung", Plan 25 "n = 2 heisst nur: die Eigenfunktion hat mehr Knoten". **Haelt nicht ganz**, Befund 1.
- **Krein-Korollar**: in 60-62, 97-98 und 361 mit "Formel aus KREIN-1, hier nicht neu geprueft, kein
  Stabilitaetssatz". Die Zahlen rechne ich nach: 1,690356597 - 0,827725138 = 0,862631 und 1,826342030 - 0,868617300 =
  0,957725. Haelt.
- **Keine nichtlineare Stabilitaet**: 356 "keine lineare oder nichtlineare Stabilitaet", 64 "nichtlineare
  Strahlungsfreiheit" nicht behauptet. Haelt im Beweistext. Der erste Satz von "Einfach gesagt" ("schwingen, ohne
  Wellen nach aussen abzugeben") steht ohne "im linearen Modell"; das ist unveraendert seit der Vorfassung (Befund 5).
- **Kein zweites Programm**: 24, 348-350, 452, 464-465. Haelt.

## 5. Befunde (nummeriert)

Kein Befund beruehrt die Strenge von T1 oder T2. Alle 58 geprueften neuen oder geaenderten Zahlen stimmen mit
zertifikat/ ueberein. Die Befunde betreffen Wortlaut, Quellenangaben und eine Zusammenfassung.

1. **n-Reste (Grenze "n nur als Leiteretikett"), mittel, Text.** BEWEIS-2.md:67 "erste Schwapp-Stelle",
   :459-460 "die naechste Atmungsschwingung und die erste Schwappschwingung", BEWEIS-2-PLAN.md:25 "n = 2 heisst nur:
   die Eigenfunktion hat mehr Knoten". "erste" und "naechste" setzen eine lueckenlose Leiter voraus. "hat mehr
   Knoten" ist eine Knotenaussage, fuer die es kein Zertifikat gibt. Beides widerspricht :21 und :359-360 sowie
   OpenAI A4 (GESAMT-REVIEW.txt:87-89). Die Tabelle in Abschnitt 8 meldet A4 als umgesetzt.
2. **"R < r_j in allen Schritten" zu weit, niedrig, Text.** Stellen: :111, :197, :142 (unveraendert), Abschnitt 8
   :439. In allen acht Schrittdateien hat der erste Schritt r_j = 0 und R > 0. Geprueft wird R < r_j nur bei r_j > 0
   (bewkern.py:354-360, bewkern_l1.py:457). Fuer alle Schritte mit r_j > 0 gilt es (jq: 0 Verstoesse). "steht in
   keinem Flag" ist ungenau: Jedes Protokoll fuehrt R_kleiner_rj_alle = true, gebildet als `(R < rj) or rj == 0`
   (pruef-l0.py:590, pruef-l1.py:638). Der Wert steht nur nicht in M3.BESTANDEN.
3. **Quelle fuer N >= 1 und qfac > 1 falsch, niedrig.** Stellen: :108-109 und Abschnitt 8 :439 ("aus den
   Schrittprotokollen"). Die Schritteintraege haben kein Feld N und kein Feld qfac. Die Werte stehen in parameter und
   kommandozeile (N 64/48 und --q 3; B: 72/44 und --q 4) und erfuellen die Bedingungen. Das Ergebnis stimmt, die
   Herkunftsangabe nicht.
4. **"bricht der Lauf ab" beschreibt den Code falsch, niedrig.** Stellen: :110-111, "durch Abbruch erzwungen" :122,
   :197, :439. apriori wirft Fehler("R >= rj"). integrate faengt diesen Fehler ab und versucht den Schritt mit
   R * 7/10 erneut; erst bei R < 1/1000 bricht der Lauf ab (bewkern.py:575-582, bewkern_l1.py:710-725). Ausserdem ist
   R <= r_j/2 schon durch den Ansatz Rt = min(Rmax, rfrac r_j) mit rfrac = 1/2 gegeben. In der Sache stimmt die
   Aussage: Kein angenommener Schritt hat R >= r_j. Das Wort "Abbruch" stammt schon aus Lesung A3.
5. **Zusammenfassung behauptet mehr als belegt, mittel.** "Einfach gesagt" :463-465: "nur Beschreibungsfehler
   gefunden, die jetzt berichtigt sind".
   - A4/F3/F4 sind Prozessbefunde (Selbststempel, Plan nicht eingefroren). Sie sind nur benannt (:380-383).
   - A5/F8 ist eine offene Frage (:250-254).
   - Die OpenAI-Codehinweise sind nicht umgesetzt (:387-390).
   - Der erste Satz ("schwingen, ohne Wellen nach aussen abzugeben") und "bewiesen" (:459) stehen dort ohne "im
     linearen Modell". Der Satz ist unveraendert, gegen :64 aber zu weit.
   - Die Aenderung von "Einfach gesagt" und die des Abschnitts "Ergebnis" fehlen in der Tabelle von Abschnitt 8 und
     in der Liste STAND.md:31.
6. **Richtung der l = 1-Breite, niedrig, Zahlwort.** :243 sagt "auch in B kaum kleiner als in A". Tatsaechlich ist
   sie in B groesser: 1,64e-3 und 1,54e-3 gegen 1,34e-3 und 1,26e-3 (D_relbreite), obwohl delta_a in B um den
   Faktor 2,11e-20 / 1,745e-21 = 12 kleiner ist. "kastenunabhaengig" (:384) trifft nur B gegen B2.
7. **"Ein Fehler in Code oder Lemma liegt nicht vor." (:238), niedrig, absolut.** Belegt ist nur, dass sich der
   Fehlschlag ohne einen solchen Fehler vollstaendig erklaert: 42,0 = 19,1 + 22,9 aus den Profilzeilen, M1 scheitert
   mit 19,10, und B2 besteht mit allein delta_c mal 2^17. Einen allgemeinen Ausschluss gibt das nicht her; es gibt
   kein zweites Programm (:348-350).
8. **Zitat des OpenAI-Urteils, Hinweis.** :22, :344, :430 und STAND.md:31 sagen "beide traegt mit Auflagen".
   GESAMT-REVIEW.txt:6-13 urteilt je Satz anders: T1 "TRAEGT" (im eingeschraenkten Sinn), T2 "TRAEGT MIT AUFLAGEN".
   A4 betrifft allerdings auch T1. Das ist harmlos, als Zitat aber ungenau.
9. **Gegenfall zu A5, Kandidat 2 (Hinweis, keine Auflage).** In T1-A ist schritte_kasten.relw_f_bei_L = 26282,
   also breiter als 2872 in T2-A. Trotzdem schrumpft bei l = 0 die entsprechende D-Breite von A nach B um den Faktor
   30 (LESUNG-BEWEIS-2.md:205). Nachgeprueft mit D_relbreite, Zeilen 3 und 4, Spalte a: T1-A 7,33e-5 und 5,50e-5,
   T1-B 2,54e-6 und 1,90e-6; 7,33 / 0,254 = 28,9 und 5,50 / 0,190 = 28,9. Ein breites f bei L allein erklaert die
   l = 1-Breite also nicht. Der Text nennt beide
   Kandidaten ungeprueft und behauptet deshalb nicht zu viel.

**Auflagen (Anforderungen, den Wortlaut waehlt der Autor; alle nur Text, keine blockiert):**
- **L1 (zu 1):** Ordnungswoerter und Knotenaussage an "n nur als Leiteretikett" angleichen: Ueberschrift 2, "Einfach
  gesagt", Plan 25.
- **L2 (zu 2):** "R < r_j" auf die Schritte mit r_j > 0 beschraenken und R_kleiner_rj_alle als Protokollwert nennen.
- **L3 (zu 3, 4):** Die Quelle fuer N und qfac (parameter, kommandozeile) und den Mechanismus (Schrittversuch
  verworfen, R verkleinert) richtig angeben.
- **L4 (zu 5):** "Einfach gesagt" auf den Beleg zuruecknehmen (offene Punkte sind nicht berichtigt) und "linear"
  ergaenzen. Die Aenderung in Abschnitt 8 und STAND aufnehmen.
- **L5 (optional, zu 6, 7, 8):** "kaum kleiner" berichtigen, :238 auf "ohne Fehler erklaert" begrenzen und das
  OpenAI-Urteil je Satz zitieren.
