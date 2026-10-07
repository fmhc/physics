Urteil: GR1, GR2, GR3, GR4 und GR6 eingetroffen; GR5 eingetroffen (A-Liste mit 2 zu starken Kernsaetzen: A1 TAKT-UMKLAPP-1, A2 TT-GLAS-2; keine falsche Zahl, kein falsches Urteil)

# GEGENLESEN-R47: Frischer Leser fuer TAKT-UMKLAPP-1, TT-GLAS-2, OKTA-SCHATTEN-1, KAC-DIAMANT-WICK-1

- Leser: pruefer-opus (Haus Anthropic, frischer Agent, kein Autor der vier Ergebnisse)
- Bindend: RUNDE-37/gegenlesen-r47/KARTE.md, sha256 fe686ec1e1d9a20c24e4fc0d74e917ea3a28454f6f363968b119de6989f43a03 (beim Start gemessen, 59 Zeilen, 662 Woerter)
- Kennzeichen: [M] gemessen/gelesen in Datei, [E] Erwartung, [P] Pruefschluss, [S] Selbstanzeige, [L] Literatur/Lehrbuch, [H] Hypothese/Handrechnung

## 1. Zeiten

- Beginn: 2026-10-05 08:35:25 CEST (date)
- Zwischenstaende per date: 08:40:11 (TAKT-UMKLAPP-1 geprueft), 08:43:17 (TT-GLAS-2), 08:45:58 (OKTA-SCHATTEN-1), 08:49:32 (KAC-DIAMANT-WICK-1), 08:51:45 und 08:54:20 (Abschnitte 2 bis 7).
- Ende: 2026-10-05 08:55:14 CEST (date, gemessen vor dem Eintragen dieser Zeile). Dauer 08:35:25 bis 08:55:14 = 19 min 49 s, Zeitbox 60 min eingehalten.
- Reihenfolge: TAKT-UMKLAPP-1, TT-GLAS-2, OKTA-SCHATTEN-1, KAC-DIAMANT-WICK-1 (Vorrang laut Auftrag eingehalten). Alle vier sind vollstaendig geprueft.

## 2. Ergebnis zuerst

1. **Keine falsche Zahl, kein falsches Urteil.** Alle tragenden Zahlen der vier Ergebnisse stimmen mit ihren Dateien (GR1 bis GR4 eingetroffen). Die Kopf- und Schreibtischrechnungen habe ich von Hand nachvollzogen: a2-Form, c^2 = 8q/(1 + 2q), Dirac-Masse, Nelson-Beziehung, 9/8 und die Streuungen.
2. **Zwei zu starke Kernsaetze (A-Liste, GR5 eingetroffen):**
   - A1: TAKT-UMKLAPP-1 nennt den negativen Takt "die ganze Instabilitaet". Die eigenen Daten zeigen mehr wachsende Moden als negative Richtungen, wo A_red nicht positiv definit ist (V2-Z-Arm 2 gegen 1 und 5 gegen 4; UMKLAPP-1 f = 0,2 74 gegen 70 usw.).
   - A2: TT-GLAS-2 nennt das Glas "in der ganzen Brillouin-Zone stabil". Gerechnet sind 112 Klassen eines 6^3-Gitters.
3. **Die vier Pruefpunkte bestehen:**
   - OS3 "inhaltlich nicht entscheidbar" ist eine Verschaerfung, keine Lockerung.
   - Die KAC-Formschwelle stand 7 s vor dem Hauptlauf im eingefrorenen Plan, in Kenntnis der Schreibtischwerte und offen angezeigt.
   - Die p4000b-Wiederholung lief mit dem eingefrorenen dk.py (Hash in jeder Ausgabe).
   - HT3 bleibt korrekt "verfehlt". Nur "inhaltlich an allen Punkten" stuetzt sich auf eine nach Sicht gewaehlte Schwelle (B2).
4. **Handrechnung der Leitung stimmt (GR6):** An der Kante 0-e1 des Ecktetraeders ist P1 = 1/6 und umkreisbasiert = 1/4. Beide erfuellen die Summenregel 3 |T| = 1/2, am regulaeren Tetraeder sind beide 0,0589.
5. **Unschaerfen (B-Liste):** vor allem B1 ("Noetig ist nur ein positiver Takt", nicht getestet), B3 ("sogar etwas steiler"), B6 und B7 (Einfach-gesagt-Saetze in KAC und OKTA) und B5 (kein Code-Hash in haupt.json).

## 3. Urteile GR1 bis GR6

Nach dem Wortlaut der Karte (gegenlesen-r47/KARTE.md, Z. 41 bis 48), Erwartungen unveraendert.

| Nr | Erwartung (Karte) | Wahrsch. | Urteil | Fundstelle |
|---|---|---|---|---|
| GR1 | Die tragenden Zahlen von TAKT-UMKLAPP-1 stimmen mit den Dateien | 85 % | **eingetroffen** | Anhang A.1. HT0 (6,6e-16 / 5,5e-16, 252 k, c = 8), HT1' (1/720, 12 x -8/9), HT2 (821 bis 1 668; 13 bis 148 an allen 100 k), Gleichheit 15/19/15/14, 70/64/71/75, 142/131/147, 30 an klein-100-1 gegen umklapp-1/ERGEBNIS.md Z. 166 bis 170, HT3 1 122 von 1 124, TU1 26/26 gegen 10/26, alle 26 Zeilen von 4.3 gegen auswertung.md. Kein Zahlenfehler; die Satzstaerke steht unter A1 |
| GR2 | Die tragenden Zahlen von TT-GLAS-2 stimmen mit den Dateien | 85 % | **eingetroffen** | Anhang A.2. auswertung.json TG2-0 bis TG2-3 und exponent, tabellen.md Z. 82 bis 114, Mittel und SD von Hand. Die OOM-Wiederholung ist per skript_sha256 747f4f03... und argv in allen vier p4000b-Dateien belegt |
| GR3 | OKTA-SCHATTEN-1: Zahlen stimmen; die OS3-Wertung ist sauber begruendet, ohne nachtraegliche Lockerung | 75 % | **eingetroffen** | Anhang A.3. licht.json und schwer.json gegen Text; a2-Form und c^2 = 8q/(1 + 2q) von Hand an 7 von 7 q. OS3: Plan-Regel "nicht entscheidbar" (Z-Gueltigkeit, PLAN 4), Code-Ausgabe "eingetroffen" offen genannt. Die Ersetzung nach Sicht nimmt einen Treffer weg und lockert nichts; inhaltlich richtig (B9) |
| GR4 | KAC-DIAMANT-WICK-1: Die Schreibtischformeln stimmen und decken sich mit haupt.json | 85 % | **eingetroffen** | Anhang A.4. c_eff, m, D, Nelson m = hbar/(2D), Grenzgeschwindigkeiten und beide Streuungen (1,455e-4 und 1,637e-4 von Hand gegen 1,453e-4 und 1,631e-4) unabhaengig hergeleitet; haupt.json stimmt in allen Stellen. Die Formschwelle stand 7 s vor H1 fest (mtime, Einfrierliste) |
| GR5 | In mindestens einem der vier "Ergebnis zuerst"- oder "Einfach gesagt"-Abschnitte steht eine Zahl oder ein Satz, der von der Quelle abweicht oder staerker ist | 45 % | **eingetroffen** | A1 (TAKT-UMKLAPP-1 Z. 77 und Z. 368 bis 369, dazu Z. 290), A2 (TT-GLAS-2 Z. 68); dazu B4, B6, B7, B8 in "Einfach gesagt" bzw. "Ergebnis zuerst" |
| GR6 | Die Handrechnung der Leitung (P1 1/6 gegen umkreisbasiert 1/4 am Ecktetraeder) stimmt | 90 % | **eingetroffen** | Abschnitt 7: w_01(P1) = -(1/6)(grad phi0 . grad phi1) = 1/6; *1(01) = Quadrat der Seite 1/2 in x = 1/2 = 1/4; Summenregel und regulaeres Tetraeder (0,0589) bestaetigt |

**Bedeutung nach Karte (vorab, Z. 51 bis 52):** GR1 bis GR4 und GR6 treffen ein: Die Zahlen gehen unveraendert ins Journal und in v4. GR5 trifft ein: A1 und A2 werden vor dem Journal eingearbeitet, mit Berichtigung im Rundenprotokoll. A1 betrifft auch den Leitungstext RUNDE-47.md (HT2-Punkt der Ernte TAKT-UMKLAPP-1).

## 4. A-Liste (vor Journal und GEMEINSAMES-NETZ v4 zu berichtigen)

Falsche Zahlen oder falsche Urteile habe ich in keinem der vier Ergebnisse gefunden. Die A-Liste besteht aus zwei zu starken Kernsaetzen.

**A1 TAKT-UMKLAPP-1: "die ganze Instabilitaet" ist staerker als die eigenen Daten [P].**
- **Ist:**
  - ERGEBNIS Z. 77 (Ergebnis zuerst 3): "Zufaelliges Umklappen macht den Takt indefinit, und das ist die ganze Instabilitaet [E]."
  - Z. 290 (Abschnitt 5, Punkt 2): "Damit ist jede Instabilitaet aus Umklappen eine negative Richtung des Takts: n_-(B_red) = n_-(P)."
  - Z. 368 bis 369 (Einfach gesagt): "und genau dort wachsen Stoerungen von selbst an: Das war die Instabilitaet aus UMKLAPP-1, Stueck fuer Stueck nachgezaehlt."
  - Gleichlautend RUNDE-47.md, Eintrag "Ernte TAKT-UMKLAPP-1", Punkt HT2 (Z. 120 beim Lesen um 08:52; die Datei waechst): "Die Instabilitaet sitzt also ganz im Takt."
- **Beleg:**
  - Die Zahl wachsender Moden liegt ueber n_-(B_red) = n_-(P), wo A_red nicht positiv definit ist. V2-Z-Arm: wachsend 2 bzw. 5 gegen n_-(B_red) = n_-(P) = 1 bzw. 4. Quellen: auswertung.md, Stabilitaetstabelle Zeilen V2; per jq einzige Z-Faelle mit n_wachsend_max != B_red_neg_max, beide mit A_red_pd_alle = false; ERGEBNIS 4.3 selbst, Z. 222 bis 223.
  - UMKLAPP-1, f = 0,2: wachsend 74/68/75/79 gegen B_red negativ 70/64/71/75, bei N = 256 151/139/154 gegen 142/131/147 (umklapp-1/ERGEBNIS.md Z. 167 und 170).
  - "Genau dort": Eine raeumliche Zuordnung zu den negativen Flaechen ist nicht gerechnet. Bis zu 4 negative *1 liessen P psd und das Netz stabil (Teil B, a = 1e-3; ERGEBNIS Z. 291 bis 292).
- **Soll (Inhalt, Wortlaut beim Autor):**
  - Der Anteil der Instabilitaet, der in B_red sitzt, kommt ganz aus dem Takt: n_-(B) = V an allen gerechneten Traegheitspunkten, also n_-(B_red) = n_-(P).
  - Wo die Bewegungsenergie A_red nicht positiv definit ist (V2-Z-Arm; UMKLAPP-1 f = 0,2), kommen weitere wachsende Moden hinzu.
  - In allen 52 Teil-B-Netzen fiel "instabil" mit "P nicht psd" zusammen.
  - Einfach gesagt ohne "genau dort" und ohne "Stueck fuer Stueck"; stattdessen: "die Zahl der negativen Richtungen von B_red stimmt mit UMKLAPP-1 ueberein".

**A2 TT-GLAS-2: "in der ganzen Brillouin-Zone" ist staerker als das gerechnete Gitter [P].**
- **Ist:** ERGEBNIS Z. 68 (Ergebnis zuerst 1, fett): "Das Glas bleibt in der ganzen Brillouin-Zone stabil [E]."
- **Beleg:**
  - Gerechnet sind 112 Klassen des 6^3-Gitters je Netz (auswertung.json TG2-1: n_punkte_summe 2688 = 24 x 112).
  - ERGEBNIS Abschnitt 5 sagt selbst: "Geprueft sind nur die mit der Superzelle vertraeglichen k (6^3-Gitter); zwischen den Gitterpunkten und fuer das nicht periodische Glas ist das eine Lesart."
  - Der Kartenwortlaut TG2-1 lautet "im ganzen k-Gitter".
- **Soll:** "an allen 112 Klassen des 6^3-k-Gitters der Superzelle stabil (24 Netze)". Gleiches gilt fuer jede Uebernahme in Journal und v4.

## 5. B-Liste (Unschaerfen)

- **B1 TAKT-UMKLAPP-1, Ergebnis zuerst 5 (Z. 87 bis 89):** "Umklappen ist ein stabiler Taktschritt, solange der Takt positiv bleibt ... Noetig ist nur ein positiver Takt."
  - Das ist eine Hinreichend-Aussage. Belegt ist der Zusammenfall "stabil genau dann, wenn P psd" in 52 Teil-B-Netzen (und auf V).
  - Der direkte Test ist nach Z. 317 bis 318 "nicht gerechnet". n_-(B) = V ist nach Z. 319 offen ("ob n_-(B) = V ein Satz ist"), ebenso, ob A_red positiv definit bleibt.
  - Dieselbe Luecke steht in RUNDE-47.md, "Selbstanzeige der Leitung [M]" (Z. 128 um 08:52): "dann mit HT0 P psd, und mit HT3 stabil". Dafuer braucht es zusaetzlich n_-(B) = V und A_red positiv definit.
  - Soll: als [H] mit genau diesen zwei Zusatzbedingungen.
- **B2 TAKT-UMKLAPP-1, HT3 (Pruefpunkt 4):** Das Urteil "verfehlt" bleibt stehen und ist ueberall so genannt: ERGEBNIS Z. 81 bis 82, Tabelle 3, Z. 112 bis 114, Selbstanzeige 1, RUNDE-47.md Z. 121. Die Darstellung ist korrekt.
  - Zu stark ist nur "Inhaltlich steht HT3 an allen Punkten" (Z. 113). Das stuetzt sich auf eine Lueckenschwelle (10 x groesste Eichnull), die nach Sicht der Werte an 4 Punkten gewaehlt wurde (Nachtrag 4.5 b, Selbstanzeige 3). Soll: "Mit einer nachtraeglich gewaehlten Lueckenschwelle gilt die Identitaet auch an den 2 Punkten (beschreibend)."
  - Beobachtung ohne Folge fuers Urteil: Die eingefrorene Wortlaut-Regel (PLAN 5) bildet den Kartenvorbehalt "sofern B seine Zahl negativer Richtungen behaelt" als Korrekturterm (n_-(B) - V) ab, nicht als Ausschluss. Woertlich gelesen laegen die 2 Punkte (n_-(B) = 255 mit der eingefrorenen Schwelle) ausserhalb der Praemisse. Eine Umdeutung jetzt waere eine Lockerung nach Sicht; das Urteil bleibt "verfehlt".
- **B3 TT-GLAS-2, Ergebnis zuerst 3 (Z. 81), "sogar etwas steiler":** p = -0,564 (Bootstrap -0,648 bis -0,484) schliesst -0,47 nur knapp aus. Mit dem Nachtrag ist p = -0,533 (-0,614 bis -0,452), und -0,47 liegt im Bereich. Die 4 Plan-Netze N = 512 lagen niedrig (Selbstanzeige 9). Zudem stammen -0,47 (TT-GLAS-1) und -0,56 aus verschiedenen N-Bereichen. Soll: "haelt (Exponent -0,56, mit Nachtrag -0,53)" ohne "steiler".
- **B4 TT-GLAS-2, Einfach gesagt (Z. 266):** "mit Schwerewellen aller Wellenlaengen geprueft, die in die Rechenzelle passen". Gerechnet ist nur das 6^3-Gitter, wie in A2. Soll: Wellen, die in einen sechsfach groesseren Wuerfel passen, oder "auf einem Gitter von Wellenlaengen".
- **B5 KAC-DIAMANT-WICK-1, Beleg Code-Lauf:** haupt.json traegt keinen Code-Hash, und es gibt keine .69-seitige Einfrierliste. Die Bindung des Hauptlaufs an das eingefrorene kac_wick.py ist nur mittelbar (siehe A.4). Fuer kuenftige Laeufe: skript_sha256 in die Ausgabe, wie bei TT-GLAS-2.
- **B6 KAC-DIAMANT-WICK-1, Einfach gesagt (Z. 202):** "entsteht ein Teilchen mit Masse". Abschnitt 3 sagt selbst, das Ergebnis trage "relativistische Teilchenwelle" nicht, nur "massive, isotrope Welle im langsamen Grenzfall". Soll: "entsteht eine Welle mit Masse".
- **B7 OKTA-SCHATTEN-1, Einfach gesagt (Z. 234) und Abschnitt 5 (Z. 172):** "wie schnell, bestimmen genau diese Flaechen" bzw. "Das Tempo haengt nur an ihrer Kopplung".
  - Nach der eigenen Formel 1/c^2 = s1/(4 w_H) + s1/(2 w_D) (4.1, [K]) haengt c auch an der Dreieckskopplung w_D. q = w_H/w_D ist ein Verhaeltnis, und fuer q gegen unendlich geht c gegen 2 (Dreiecke begrenzen).
  - Soll: "zusammen mit den Dreiecksflaechen (Reihenschaltung)". Ergebnis zuerst 2 ("setzt die Sechseck-Kopplung q = w_H/w_D") ist so richtig.
- **B8 OKTA-SCHATTEN-1, Ergebnis zuerst 4 (Z. 51) und Einfach gesagt:** "Isotrop ist die Wabe nur mit dem Oktaeder als starrer, ganzer Zelle" bzw. "hilft das Oktaeder nur, wenn ...". Das "nur" gilt fuer die gerechneten Zerlegungen (H3, Z8, D1x/y/z) und eine Lesart der Bewegungsgewichte (Selbstanzeige 8). Soll: "unter den gerechneten Zerlegungen".
- **B9 OKTA-SCHATTEN-1, OS3 fuer Journal und v4:** Beide Angaben mitnehmen, nicht nur "nicht entscheidbar". Nach Plan ist OS3 nicht entscheidbar. Die Kartenwortlaut-Regel gibt mechanisch "eingetroffen" aus, ein Artefakt (max/min - 1 bei negativem omega^2). Inhaltlich ist OS3 nicht entscheidbar; als frischer Leser bestaetige ich diese Wertung (A.3). Ergebnis zuerst 3 (Z. 49 bis 50) nennt nur "OS3 nicht entscheidbar"; das ist die Plan-Wertung und richtig, aber ohne den Hinweis auf die Code-Ausgabe.

## 6. C-Liste (Kleinigkeiten)

- **C1 TAKT-UMKLAPP-1, Ergebnis zuerst 1:** "auf allen 24 weiteren Netzen und 52 Teil-B-Netzen". Teil A hat 28 Netze; V_D und S_D (Rest 9,6e-16 bzw. 5,5e-16) fehlen in der Zaehlung. Die Leitungszahl "76 weitere Netze" (RUNDE-47.md, HT0) ist 24 + 52 und folgt dieser Zaehlung.
- **C2 TAKT-UMKLAPP-1, Z. 79 und 289:** In "genau V negative Richtungen" ist V die Eckenzahl, zugleich aber der Name des Netzes V. Vorschlag: "|V| (Eckenzahl)".
- **C3 TAKT-UMKLAPP-1, Tabelle 3, HT2 (Z. 99):** "n_-(P) = 70 / 65 / 71 / 76 ... an allen 100 k" liest sich wie ein fester Wert. Es ist der Hoechstwert ueber k; je k schwankt n_-(P) (64 bis 65, 69 bis 71, 75 bis 76, 142 bis 143, 130 bis 131, 146 bis 148). Die Gleichheit mit UMKLAPP-1 (Ergebnis zuerst 3) gilt an klein-100-1. Vorschlag: "(Hoechstwert ueber k; an klein-100-1 gleich UMKLAPP-1)".
- **C4 RUNDE-47.md, HT3-Punkt (Z. 121 um 08:52):** "einen Eigenwert von etwa -7e-10". Das gilt nur fuer Saat 2 (-6,7e-10); bei Saat 3 sind es -2,9e-10 (ERGEBNIS 4.5 b).
- **C5 TT-GLAS-2, Z. 80:** "unprojiziert ist A3 exakt isotrop ((e): 0,00 %)". Das ist [M] exakt, numerisch aber <= 2,9e-5 (4.2, Pruefgroessen). Vorschlag: "(e) <= 3e-5".
- **C6 TT-GLAS-2:** Die Ergebnisdateien unterscheiden p4000a und p4000b nicht (info.gpu = "Quadro P4000"). Die Spur steht nur in den Lognamen und Logzeilen.
- **C7 TT-GLAS-2, Ergebnis zuerst 1:** Dass A_red bei Gamma in allen 24 Netzen genau eine negative Richtung hat (4.1, Lesart globale Skalierung [H]), steht nur in 4.1. "Es gibt keine negative ... Mode" stimmt fuer omega^2. Der Hinweis gehoerte aber in den Kernabschnitt, weil eine negative Richtung der Bewegungsmatrix eine eigene Frage ist.
- **C8 OKTA-SCHATTEN-1, Z. 62:** "an allen 524 k (auf 1e-8)". Die Spannweiten von kappa sind 4,5e-9 (R12), 1,42e-8 (D1z) und 1,27e-8 (H3). Vorschlag: "auf 1,5e-8".
- **C9 OKTA-SCHATTEN-1:** urteile.OS2.gruende_23 ist auf 20 von 30 Gruenden gekuerzt. Die Zahl "12 von 23" folgt nur aus p23 (12 Richtungen mit negativer Mode, von mir per jq gezaehlt).
- **C10 OKTA-SCHATTEN-1, Z. 42:** "Neu gemessen" fuer eine Rechnung. Der Kopf sagt "Keine Messdaten". Vorschlag: "Neu gerechnet".
- **C11 KAC-DIAMANT-WICK-1:** Die Karte nennt fuer KW1 "\|k\| = 0,05 (in Einheiten der Gitterkonstante)", gerechnet ist mit der Bindungslaenge l. Das ist die strengere Wahl (in a-Einheiten 2,7e-5 statt 1,45e-4) und offen angezeigt (Selbstanzeige 3); kein Einfluss aufs Urteil.

## 7. Handrechnung Ecktetraeder (0, e1, e2, e3)

Gegenstand: RUNDE-47.md, Eintrag "Ernte TAKT-UMKLAPP-1" (Z. 124 beim Lesen um 08:52) und takt-umklapp-1/ERGEBNIS.md Selbstanzeige 2 (Z. 330 bis 331): "Kante 0-e1 mit P1 1/6, umkreisbasiert 1/4". Eigene Rechnung, ohne Rechner [H]:

**Geometrie.** v0 = 0, v1 = e1, v2 = e2, v3 = e3. Volumen |T| = 1/6. Kanten 01, 02, 03 mit Laenge 1, Kanten 12, 13, 23 mit Laenge Wurzel2.

**(a) P1 (lineare finite Elemente, 3D-Kotangens).**
- Baryzentrische Funktionen: phi1 = x, phi2 = y, phi3 = z, phi0 = 1 - x - y - z. Gradienten: grad phi0 = (-1, -1, -1), grad phi1 = (1, 0, 0), grad phi2 = (0, 1, 0), grad phi3 = (0, 0, 1).
- Steifigkeit K_ij = |T| grad phi_i . grad phi_j, Kantengewicht w_ij = -K_ij.
- w_01 = -(1/6)(-1) = **1/6**; ebenso w_02 = w_03 = 1/6.
- w_12 = -(1/6)(0) = 0; ebenso w_13 = w_23 = 0.
- Gegenprobe mit der Kotangensformel w_01 = (1/6) l_23 cot theta_23. Die Gegenkante 23 hat l_23 = Wurzel2. Der Diederwinkel an 23 liegt zwischen den Flaechen x = 0 (Aussennormale (-1, 0, 0)) und x + y + z = 1 (Aussennormale (1, 1, 1)/Wurzel3). Damit cos theta = -n_a . n_b = 1/Wurzel3, sin theta = Wurzel(2/3), cot theta = 1/Wurzel2. Also w_01 = (1/6) Wurzel2 (1/Wurzel2) = 1/6. Stimmt.

**(b) Umkreisbasierter Hodge-Stern *1 = |duale Flaeche in T| / |Kante|.**
- Umkreismitten: Kante 01: m = (1/2, 0, 0). Dreieck 012 (rechtwinklig in 0): Mitte der Hypotenuse, (1/2, 1/2, 0). Dreieck 013: (1/2, 0, 1/2). Tetraeder: c_T = (1/2, 1/2, 1/2), denn |c|^2 = |c - e_i|^2 gibt jede Koordinate 1/2.
- Der duale Anteil der Kante 01 in T ist das Viereck m, (1/2, 1/2, 0), c_T, (1/2, 0, 1/2). Es liegt in der Ebene x = 1/2, senkrecht zur Kante, und ist ein Quadrat der Seite 1/2.
- Vorzeichen nach der Hoehenformel |*e ∩ T| = Summe ueber die zwei Flaechen f an e von (1/2) h_(e,f) h_(f,T). Dabei ist h_(e,f) der Abstand von m zur Flaechen-Umkreismitte, positiv zur Gegenecke in f. h_(f,T) ist der Abstand von der Flaechen-Umkreismitte zu c_T, positiv zur Gegenecke von f.
  - Flaeche 012: h = +1/2 (zu v2), h = +1/2 (c_T bei z = 1/2, v3 bei z = 1), Beitrag 1/8.
  - Flaeche 013: ebenso 1/8.
  - Summe 1/4. Mit |e| = 1 folgt *1(01) = **1/4**.
- Gegenprobe Kante 12: Flaeche 012 traegt 0, weil die Umkreismitte die Kantenmitte ist. Flaeche 123 (gleichseitig, Seite Wurzel2): h_(e,f) = Inkreisradius = Wurzel2/(2 Wurzel3) = 1/Wurzel6. h_(f,T) = (c_T - (1/3, 1/3, 1/3)) . (-(1, 1, 1)/Wurzel3) = -(1/2)/Wurzel3 = -1/(2 Wurzel3), denn c_T liegt jenseits der Flaeche 123 (x + y + z = 3/2 > 1). Beitrag (1/2)(1/Wurzel6)(-1/(2 Wurzel3)) = -1/(12 Wurzel2). Dann *1(12) = -1/(12 Wurzel2)/Wurzel2 = **-1/24**.

**(c) Summenregel als Kontrolle.** Summe_e l_e^2 w_e = 3 |T| = 1/2 fuer beide Gewichte:
- P1: 3 x 1 x 1/6 + 3 x 2 x 0 = 1/2.
- Umkreisbasiert: 3 x 1 x 1/4 + 3 x 2 x (-1/24) = 3/4 - 1/4 = 1/2.

Beide erfuellen die Regel und sind trotzdem verschieden. Das passt zu ERGEBNIS 4.5 a ("beide erfuellen sum l^2 w = 3 V").

**(d) Regulaeres Tetraeder, Kante a (Zusatzangabe der Leitung "je 0,0589").**
- Umkreisbasiert, aus Symmetrie und Summenregel: 6 a^2 w = 3 |T| mit |T| = a^3/(6 Wurzel2), also w = a/(12 Wurzel2).
- P1: w = (1/6) a cot(arccos(1/3)) = (1/6) a (1/3)/Wurzel(8/9) = a/(12 Wurzel2).
- Gleich; bei a = 1: 1/(12 x 1,41421) = 1/16,971 = 0,0589.

**Urteil [P]:** Die Handrechnung der Leitung stimmt: P1 1/6, umkreisbasiert 1/4 an der Kante 0-e1, beide gleich 0,0589 am regulaeren Tetraeder. GR6 eingetroffen. Im 3D-Ecktetraeder liegt die Umkreismitte ausserhalb (x + y + z = 3/2), daher die negativen umkreisbasierten Anteile der langen Kanten. P1 und umkreisbasiert sind also in 3D verschiedene Operatoren, wie TAKT-UMKLAPP-1 4.5 a numerisch zeigt.

## 8. Selbstanzeigen

1. **Werkzeuge ueber die Auftragsliste hinaus, alle nur lesend:**
   - ls (Dateizeiten), sha256sum (Pruefpunkte 2 und 3 verlangen Hashvergleiche), date, cd und for-Schleifen in Bash.
   - Kein python, awk oder perl, keine Shell-Arithmetik, kein Netz, nichts auf der .69. Geschrieben habe ich nur diese Datei.
2. **jq mit Auswahl und Zaehlung:** Mit min, max, unique, length und select habe ich vorhandene Werte herausgesucht bzw. gezaehlt: n_-(P) je k, Richtungen mit negativer Mode in H3, Streuung der uebrigen Paare, Z-Faelle mit wachsend != B_red. Summen, Mittel, SD und Verhaeltnisse habe ich nur im Kopf gerechnet, mit Rechenweg in Abschnitt 7 und im Anhang. Die Grenze zu "Rechnen auf dem Rechner" ist bei min/max eng; ich zeige es deshalb an.
3. **Zeilennummern in RUNDE-47.md:** Die Datei wurde waehrend der Pruefung fortgeschrieben; der Ernte-Eintrag rueckte um eine Zeile. Alle Angaben beziehen sich auf den Stand 08:52 (date). Eigene falsche Zeilenangaben fuer TAKT-UMKLAPP-1 (Z. 216/293), OKTA-SCHATTEN-1 (Z. 53) und B1 (Z. 86, 320) habe ich vor dem Abschluss per grep berichtigt.
4. **Nicht geprueft:**
   - die Einzelwerte an allen 252 bzw. 100 k (nur die Aggregatfelder und die takt_zeilen-Minima und -Maxima);
   - die P1-Kantenwerte auf V (1/60 bis 1/2, 4.5 a);
   - a4 und Doppelbrechung des Lichts (OKTA 4.1) sowie die bedingte Schranke 1,1e-27 m (LICHT-FINN-NETZ-1);
   - die Nachtrags-Gerade von TT-GLAS-2 (-0,533; ~2,2e4);
   - Ghose an der Quelle;
   - HKV 2013 (Delaunay => alle dualen Volumina >= 0) nur aus Wissen [L], nicht an der Quelle.
   Die Laufzeit-Tabellen habe ich nur stichprobenweise geprueft (bz-Dienstlaufzeiten, Zonentabelle 9 Zeilen).
5. **Blindheit:** Das Startverzeichnis war gegenlesen-r45. Ich habe es weder gelistet noch gelesen, ebenso keinen anderen gegenlesen-Ordner. RUNDE-47.md (Ernte-Text der Leitung) habe ich auftragsgemaess gelesen; er enthaelt die Lesart der Leitung und kann mein Urteil vorgepraegt haben.
6. **Rollentrennung:** Die Soll-Angaben in A und B sind Inhaltsanforderungen. Die Formulierungen in Anfuehrung sind Vorschlaege; den Wortlaut legt der Autor fest.

## Anhang: Pruefnotizen je Ergebnis

### A.1 TAKT-UMKLAPP-1 (Stand 08:40 CEST, date)

- **Einfrieren [M]:** sha256 von PLAN.md, PLAN.md.eingefroren-20261005-074503, code/tu.py (+ .eingefroren), kette-cpu8/9/10.sh (+ .eingefroren), tg.py, tg_auswertung.py, tp.py, uk.py, ew.py, nachtrag_v.py, mn.py lokal nachgerechnet: alle gleich EINGEFROREN-SHA256.txt und EINGEFROREN-SHA256-69.txt. mtime PLAN.md 07:44:12 < Einfrieren 07:45:03 < Laeufe ab 05:45:19 UTC (= 07:45:19 CEST). Nachtrags-Code (nachtrag_p1.py 07:50:08, nachtrag_ht3.py 07:51:34, pn.py) nicht eingefroren, als Selbstanzeige 3 offen genannt.
- **HT0 [M]:** auswertung.json urteile.HT0: c_V = 7,999999999999998, c_S = 8,0, rest_max_V = 6,606e-16, rest_max_S = 5,462e-16, c-Streuung 4,44e-16, n_k = 252 je Netz, K5 5,46e-16. Text stimmt. Zaehlung "76 Netze": 24 weitere Teil-A-Netze (12 Glas + 12 UMKLAPP-1) + 52 Teil-B-Netze = 76; V_D und S_D (Rest 9,6e-16 bzw. 5,5e-16) sind darin nicht mitgezaehlt (C-Liste).
- **HT1' [M]:** V_stern1_min = 0,0013889 = 1/720, V_stern2_neg = 12, VD_stern2_min = 0,5333, VD_mu_verletzt = 0, VD_zuege n23 = 12, n32 = 0. Text stimmt.
- **HT2 [M]:** stern2_neg 839/860/821/829/1668/1659/1650 (Text "821 bis 1 668" stimmt); P_psd in allen 7 false. Je k (takt_zeilen, 100 k je Netz): kein k mit n_-(P) = 0 in allen 12 UMKLAPP-1-Netzen; Minimum 13 (N128 s4 f0,05), Maximum 148 (N256 s3 f0,2). "13 bis 148, an allen 100 k" stimmt. Max ueber k: 15/19/15/14, 70/65/71/76, 143/131/148, 30 (Tabelle 4.1 stimmt).
- **Gleichheit mit UMKLAPP-1 [M]:** umklapp-1/ERGEBNIS.md Z. 166 bis 170, Spalte "B_red negativ": 15/19/15/14, 70/64/71/75, 30, 142/131/147. In TAKT-UMKLAPP-1 an klein-100-1: n_-(P) = n_-(B_red) = 15/19/15/14, 70/64/71/75, 142/131/147, 30. Gleich, aber nur an klein-100-1; ueber alle k schwankt n_-(P) (64 bis 65, 69 bis 71, 75 bis 76, 142 bis 143, 130 bis 131, 146 bis 148).
- **HT3 [M]:** urteile.HT3: n_punkte 1124, n_identitaet_verletzt 2, n_P_negativ 48, B_null_groesst_rel_max 6,70e-10, B_nichtnull_kleinst_rel_min 1,11e-9. Zaehlung: 2 x 251 (V, V_D) + 2 x 251 (S, S_D) + 12 x 3 + 8 x 3 + 4 x 2 + 52 x 1 = 502 + 502 + 36 + 24 + 8 + 52 = 1124. 48 = 8 x 3 + 4 x 2 + 16 x 1. Die beiden Verletzungen: uk-N256-s2-f0.2 und -s3-f0.2 an klein-100-1 mit n_-(B) = 255. Planregel (PLAN 5) Wortlaut: n_-(B_red) - (n_-(B) - V) = n_-(P); dort 131 - (255 - 256) = 132 != 131 bzw. 147 - (-1) = 148 != 147, also "verfehlt" nach Regel korrekt.
- **TU1 [M]:** D_stabil 1,0; Z_stabil 0,3846 = 10/26. Z stabil je Fall aus auswertung.md: a = 1e-3 stabil ausser s2 und s4 (10 von 12), a = 1e-2 keiner, V2 keiner. Zugsummen a = 1e-3: 2-3 1+1+1+0+4+0+4+1+0+1+0+2 = 15, 3-2 = 15; a = 1e-2: 2-3 = 165, 3-2 = 136 (von Hand summiert). Alle 26 Zeilen der Tabelle 4.3 (Zuege, Z *1/*2, wachsend/B_red/n_-(P), Spannen) gegen auswertung.md Zeile fuer Zeile verglichen: alle gleich.
- **Anteile 4.2 [H, Kopf]:** f = 0,05: *1 185/1076 = 17,2 %, 173/1083 = 16,0 %, 145/1088 = 13,3 %, 168/1063 = 15,8 %, 321/2169 = 14,8 %; *2 248/1896 = 13,1 %, 258/1910 = 13,5 %, 256/1920 = 13,3 %, 245/1870 = 13,1 %, 506/3826 = 13,2 %. f = 0,2: *1 38,7 / 37,3 / 38,6 / 39,6 / 39,2 / 37,4 / 40,4 %; *2 34,8 / 35,4 / 33,6 / 34,8 / 34,3 / 34,2 / 34,6 %. Text "13 bis 17 %, 13 %, 37 bis 40 %, 34 bis 35 %" stimmt (gerundet).
- **Zu starker Satz (A1):** "das ist die ganze Instabilitaet" (Ergebnis zuerst 3) und "jede Instabilitaet aus Umklappen eine negative Richtung des Takts" (5, Punkt 2): Die eigenen Daten zeigen mehr wachsende Moden als negative Richtungen von B_red, wo A_red nicht positiv definit ist: V2-Z-Arm wachsend 2 bzw. 5 gegen n_-(B_red) = n_-(P) = 1 bzw. 4 (auswertung.md, Stabilitaetstabelle, Zeilen V2; ERGEBNIS 4.3 selbst); UMKLAPP-1 f = 0,2 wachsend 74/68/75/79 gegen B_red 70/64/71/75 und N = 256 151/139/154 gegen 142/131/147 (umklapp-1/ERGEBNIS.md Z. 167 und 170). Belegt ist: der B_red-Anteil der Instabilitaet stammt ganz aus P.

### A.2 TT-GLAS-2 (Stand 08:43 CEST, date)

- **Einfrieren [M]:** sha256 lokal nachgerechnet fuer PLAN.md (+ .eingefroren), bz.py, dk.py, dz.py, kette-A/B/C.sh (+ .eingefroren), tg.py, ew.py, tp.py, tg2_auswertung.py (+ .eingefroren-20261005-074009): alle gleich EINGEFROREN-SHA256.txt und -69.txt. PLAN.md mtime 07:19:51 < Einfrieren 07:21:04 < erste Hauptlaeufe 05:21:17 UTC.
- **OOM-Wiederholung (Pruefpunkt 3) [M]:** Belegt.
  - code/nachhol-B.sh (nicht eingefroren, mtime 07:51:47 CEST = 05:51:47 UTC) ruft code/dk.py mit denselben Argumenten wie code/kette-A.sh (eingefroren, 31e018fe...), nur Spur p4000b statt p4000a.
  - Alle vier Ergebnisdateien dk-N1024-s1/s3-r0/r1.json tragen in info: skript_sha256 747f4f03... (= eingefrorenes dk.py), dz ee6ba6b4..., tg ec48a258..., tp 419d7da6..., argv woertlich wie kette-A.
  - Die Logs heissen *-p4000b.log mit spur=p4000b und rc = 0. sha256 der 8 N1024-Dateien lokal gleich PRUEFSUMMEN-lauf.txt (Z. 25 bis 32).
  - Das Skript entstand 8 s vor dem ersten N = 1024-Ergebnis (s2-r0 Ende 05:51:55 UTC), also nach den OOM-Abbruechen (05:50:13 und 05:51:51), aber vor jedem N = 1024-Wert. Keine Lockerung: Ohne Nachholung waere TG2-3 nach PLAN 6 "nicht entscheidbar" (nur 2 Netze); die Nachholung fuehrt nur die geplanten Aufrufe aus.
  - Einschraenkung: Die JSON-Datei selbst unterscheidet p4000a und p4000b nicht ("Quadro P4000"); die Spur steht nur im Log.
- **Zahlen [M]:** auswertung.json: TG2-0 abw_max_dk 1,883e-9, abw_max_bz 6,84e-10; TG2-1 24 von 24 vollstaendig, 0 wachsend, 2688 Punkte, Nullmoden bei Gamma [6], sonst 0; TG2-2 (b)/(c) 15,32/7,12 (128), 11,40/5,67 (256), 13,36/6,39 (alle); TG2-3 0,04661 (Saaten 1 bis 4); Exponent -0,5644 (Bootstrap -0,648 bis -0,484), mit TT-GLAS-1 -0,522, Gerade bei 1024: 4,80 %. Text stimmt in allen Stellen.
- **Kopfrechnung [H]:**
  - N = 1024: (4,31 + 4,67 + 5,00 + 4,67)/4 = 18,65/4 = 4,6625. SD (n-1): Abweichungen -0,3525; +0,0075; +0,3375; +0,0075, Quadrate 0,1243 + 0,0001 + 0,1139 + 0,0001 = 0,2383, /3 = 0,0794, Wurzel 0,282.
  - N = 512: (7,20 + 8,86 + 5,84 + 5,45)/4 = 6,84; Nachtrag (9,05 + 8,92 + 7,30 + 10,41)/4 = 8,92; zusammen 63,03/8 = 7,88.
  - Klassen: 6^3 = 216, selbstkonjugiert 2^3 = 8, (216 - 8)/2 + 8 = 112; 24 x 112 = 2688; 24 x 26 = 624.
  - Hochrechnung ln S = a0 + p ln N mit a0 = 0,8752, p = -0,5644: S(1024) = exp(0,8752 - 0,5644 x 6,931) = exp(-3,037) = 0,048; S = 1 % bei ln N = (0,8752 + 4,6052)/0,5644 = 9,71, N = 1,65e4 (Text "~1,7e4" stimmt); N = 8000: exp(0,8752 - 0,5644 x 8,987) = 0,0150 (Text 1,5 % stimmt).
  - Kleinstes Gitter-k: omega^2 = 4,9 x 0,208^2 = 0,212 und 4,9 x 0,165^2 = 0,133 (Text 0,21 / 0,13 stimmt).
- **Je-Netz-Werte 4.2** gegen auswertung-69/tabellen.md Z. 82 bis 110 verglichen: alle gleich; "(c) groesser als (a) in 2 von 28" (256 s7: 7,72 > 6,91; 512 s1: 9,44 > 7,20) und "(c) instabil in 2 + 4 + 4 = 10 von 28" stimmen.
- **Laufzeiten:** Dienstlaufzeiten bz128 149,8 bis 224,9 s, bz256 p4000a 154,2 bis 190,8 s, p4000b 153,6 bis 179,2 s; Text "150 bis 225", "154 bis 191", "154 bis 179" stimmt.
- **Zu starker Satz (A2):** Ergebnis zuerst 1, Kopfzeile "Das Glas bleibt in der ganzen Brillouin-Zone stabil". Gerechnet sind die 112 Klassen des 6^3-Gitters. ERGEBNIS Abschnitt 5 sagt selbst: "Geprueft sind nur die mit der Superzelle vertraeglichen k (6^3-Gitter); zwischen den Gitterpunkten ... ist das eine Lesart." Auch der Kartenwortlaut TG2-1 sagt "im ganzen k-Gitter".

### A.3 OKTA-SCHATTEN-1 (Stand 08:46 CEST, date)

- **Einfrieren [M]:** sha256 lokal nachgerechnet: PLAN.md (+ .eingefroren), okta.py (+ .eingefroren), ew.py, tp.py, licht_netz.py, tti.py, nachtrag_kinetik.py gleich EINGEFROREN-SHA256.txt; bild_okta.py (+ .eingefroren-074536) gleich NACHTRAG-BILD-SHA256.txt. Einfrieren 07:40:44 CEST, L1 Start 05:40:55 UTC (= 07:40:55 CEST), also danach.
- **OS0/OS1 [M]:** licht.json urteile: OS0 nullmoden_je_k {"2": 789}, n_flach 8, Werte 0 und 8,000; Plan "eingetroffen", Karte "nicht eingetroffen". OS1 nullmoden_max 0, n_flach 2 (bei 8), c_mittel 0,99999999998 / 1,00000000002, Spannweite 6,24e-11 / 8,41e-11; Plan "eingetroffen", Karte "geteilt". a2 (dec): Klassen -0,0364584 / -0,0572917, Minimum -0,0642362, Mittel -0,0546208, spannweite_rel 0,5086. Text stimmt.
- **a2-Form, von Hand [H]:** a2 = -5/64 + S4/24 mit S4 = Summe n_i^4: [100] S4 = 1, -15/192 + 8/192 = -7/192 = -0,036458; [110] S4 = 1/2, -15/192 + 4/192 = -11/192 = -0,057292; [111] S4 = 1/3, -45/576 + 8/576 = -37/576 = -0,064236; Kugel S4 = 3/5, -25/320 + 8/320 = -17/320 = -0,053125. Spanne (37/576 - 7/192) = 16/576 = 1/36 = 0,02778; 0,02778/0,05462 = 0,509. Alles wie im Text.
- **c^2 = 8q/(1 + 2q), von Hand [H]:** q = 1e-3: 0,008/1,002 = 0,007984, c = 0,08935 (Datei 0,089353); q = 1e-2: 0,08/1,02 = 0,07843, c = 0,28006 (0,280056); q = 0,1: 0,8/1,2, c = 0,81650 (0,816497); q = 1/6: (4/3)/(4/3) = 1 (0,99999994); q = 1: 8/3, c = 1,63299 (1,632993); q = 10: 80/21 = 3,8095, c = 1,95180 (1,951800); q = 100: 800/201 = 3,9801, c = 1,99502 (1,995018). 7 von 7 getroffen. Herleitung aus der Reihenformel des Texts: 1/c^2 = s1/(4 w_H) + s1/(2 w_D) = (s1/w_D)(1 + 2q)/(4q), mit s1/w_D = 1,414/2,828 = 1/2 folgt c^2 = 8q/(1 + 2q).
- **OS2 [M]:** schwer.json, varianten.H3: os2_13 n_wachsend 6 von 26 Punkten, Richtungen mit negativer Mode 100, 210, 310 (3 von 13); os2_23 n_wachsend 24 von 46, per jq ueber p23 12 verschiedene Richtungen (100, z2, z3, z6, z8, z9, z13, z14, z15, z16, z18, z19). Kleinstes omega^2/k^2 ueber p13: -0,28291. Gitter L = 8: nk 511, k_mit_negativ 6, k_mit_A_red_nicht_pd 6, k_mit_B_red_nicht_pd 0. Text stimmt. Hinweis: urteile.OS2.gruende_23 ist auf 20 Eintraege gekuerzt (n_gruende 30); die Zahl 12 steht nur in p23, nicht in der Urteilsliste.
- **OS3 [M]:** urteile.OS3: plan "nicht entscheidbar", karte "eingetroffen", spanne_H3 -5,418, spanne_V_neu 0,063388, z_gueltig false. Probe: max/min - 1 = 1,25/(-0,283) - 1 = -4,42 - 1 = -5,42.
- **R12, Rhombendodekaeder [M]:** beschreibend R12 spanne13 3,918e-7, Z8 1,0000, D1z 0,9500. duale.*.takt: kappa R12 -2 (Spannweite 4,5e-9), D1z -2 (1,42e-8), H3 -2 (1,27e-8). 524 k = 511 Gitter-k + 13 kleine k.
- **Pruefpunkt 1, OS3 [P]:** PLAN Abschnitt 4 (eingefroren) gibt fuer OS3 nach Plan die Gueltigkeitsbedingung "H3 muss Z-gueltig sein ... sonst nicht entscheidbar" vor, fuer den Kartenwortlaut nur "Spanne(H3) < 6,34 %". Der Code folgt dem Plan woertlich. Die Wertung des Agenten ersetzt nach Sicht die mechanische Kartenwortlaut-Ausgabe "eingetroffen" durch "nicht entscheidbar".
  - Das ist keine Lockerung: Die Ersetzung nimmt der Vorhersage einen Treffer weg. Inhaltlich ist sie richtig: max/min - 1 ist bei negativem Nenner kein Streumass, und die Karte setzt mit "TT-Spanne" zwei positive Zweige voraus.
  - Beide Werte stehen offen in Tabelle 3 und in Selbstanzeige 3. Die Planregel ist unveraendert.
  - Anmerkung: Wo H3 stabil ist, liegt die Anisotropie bei Faktor ~20 (ERGEBNIS 4.2). Inhaltlich laege daher auch "verfehlt" nahe; "eingetroffen" ist in keiner Lesart haltbar.

### A.4 KAC-DIAMANT-WICK-1 (Stand 08:49 CEST, date)

- **Einfrieren [M]:** sha256 lokal nachgerechnet: PLAN.md = PLAN.md.eingefroren-20261005-081058 = bafe37d7..., kac_wick.py (+ .eingefroren) 326c4760..., bild.py d21efce6..., bild_v2.py (+ .eingefroren-081202) 6cd14342...; alle gleich EINGEFROREN-SHA256.txt. lauf-69/PRUEFSUMMEN.txt (haupt.json 4769860d..., baender.png, baender-v2.png) lokal gleich.
- **Formschwelle (Pruefpunkt 2) [M]:**
  - Die Schwelle steht in PLAN 5 ("Formrest ... ueber 2,8e-3 ... Die Schwelle ist nach der Schreibtischrechnung gesetzt").
  - PLAN.md mtime 08:10:54,43 CEST, bitgleich mit der eingefrorenen Kopie (EINGEFROREN-SHA256.txt: 08:10:58 CEST).
  - H1 laut haupt.json start_unix 1791180665,29. Das sind 131 s nach R0 (rauch.json start_unix 1791180534,26 = 06:08:54 UTC laut PLAN 6), also 06:11:05 UTC = 08:11:05 CEST. Die Schwelle stand demnach 7 s vor dem Hauptlauf fest: "vor der Rechnung" ist belegt.
  - "Nach der Schreibtischrechnung" ist per mtime nicht trennbar, weil beides in derselben Datei steht. Die Tabelle in PLAN 3.4 nennt aber schon die erwarteten Formabweichungen (3,5e-4 bzw. 6,3e-4 bei 0,05). Die Schwelle wurde also in Kenntnis der Schreibtischwerte gewaehlt, und ERGEBNIS Selbstanzeige 2 und PLAN 3.5 sagen das offen.
  - Die Schwelle ist keine Anpassung an Daten: 2,8e-3 ist die Kartenzahl und liegt um Faktor 4,5 bis 8 ueber den Schreibtischwerten.
  - Gesetzt wurde sie nach den Rauchtests R0 (08:08:54 CEST; [100]-Baender bei 0,05, gleich der Schreibtischformel) und R0c (08:10:19 bis 08:10:21, Bild mit 31 Punkten, laut PLAN 6 angesehen). Neue Information ueber den Schreibtisch hinaus lieferten beide nicht. Aus rauch.json ([100]: E1 = -0,00083264, E8 = 2,00083264) folgt von Hand h = 1,00083264, h^2 - 1 = 0,0016660, c_loc^2 = 0,66639, c_loc = 0,81633. Das ist 2,1e-4 unter 0,81650 und damit der Schreibtischwert.
  - Folge: Das KW1-Haupturteil ist vorab ableitbar und keine Messung. Das steht im ERGEBNIS (Kopf, 3, Selbstanzeigen 1 und 2).
- **Zahlen gegen haupt.json [M]:** urteile KW0 eingetroffen, KW1 eingetroffen (beide Regeln), KW1_streng nicht eingetroffen, KW2 nicht eingetroffen (1,4528e-4 / 1,6311e-4, Verhaeltnis 1,12275), KW3 eingetroffen. bestes_paar_wick (1, 8): E0 = Delta = 1; c_eff 0,8164966 bzw. 0,99999999; m 1,49999999 bzw. 1,00000002 (Abw. 1,09e-8 bzw. 7,32e-8); Formrest 3,47e-4 bzw. 6,23e-4 (bis 0,1: 1,38e-3 bzw. 2,47e-3); streng 0 bzw. 8 (alle [111]); D_stoerung 1/3 bzw. 1/2 (Spannweite 2,0e-15 bzw. 2,6e-15); Grenzgeschwindigkeiten numerisch 0,5799/0,8178/1,0000 bzw. 0,5807/0,8182/1,0000 gegen Schreibtisch 0,5774/0,8165/1. Andere Paare mit c_loc^2 > 0: 17 bzw. 11, kleinste Streuung 2,08e-2 bzw. 3,93e-2. Text stimmt in allen Stellen.
- **Schreibtisch unabhaengig von Hand [H]:**
  - Zustaende (A, i), (B, i); H(k) = lambda (I - M) + c K, K = diag(+e_i.k auf A, -e_i.k auf B), u_i = e_i.k, Summe u_i = 0, Summe u_i^2 = (4/3) k^2 (2-Design).
  - Unterstes Niveau s = (1, ..., 1)/Wurzel8, oberstes a = (1, 1, 1, 1, -1, -1, -1, -1)/Wurzel8. <s|K|a> = (1/4) Summe u_i = 0, keine erste Ordnung. K s = (u, -u)/Wurzel8, K a = (u, u)/Wurzel8.
  - Gleichverteilt (P u = 0): M (u, -u) = 0, Zwischenniveau lambda. E_1 = -c^2 (2|u|^2/8)/lambda = -c^2 k^2/(3 lambda); E_8 = 2 lambda + c^2 k^2/(3 lambda). Also c_eff^2/(2 Delta) = c^2/(3 lambda), mit Delta = lambda: c_eff^2 = 2c^2/3, c_eff = 0,8165 c, m = Delta/c_eff^2 = 3 hbar lambda/(2 c^2).
  - Ohne Ruecksprung (P u = -u/3): M (u, -u) = (1/3)(u, -u), Niveau 2 lambda/3: E_1 = -c^2 (|u|^2/4)(3/(2 lambda)) = -c^2 k^2/(2 lambda). Fuer a ist M (u, u) = -(1/3)(u, u), Niveau 4 lambda/3, Abstand 2 lambda/3: E_8 = 2 lambda + c^2 k^2/(2 lambda). Also c_eff = c, m = hbar lambda/c^2.
  - Reelle Fassung, gleiche zweite Ordnung mit (-i c K)^2 = -c^2 K^2: D = c^2/(3 lambda) bzw. c^2/(2 lambda). hbar/(2D) = 3 hbar lambda/(2c^2) bzw. hbar lambda/c^2 = m (Nelson) in beiden Regeln.
  - Grenzgeschwindigkeit max_i |e_i.n| mit e_i = (+-1, +-1, +-1)/Wurzel3: [111] (1 + 1 + 1)/3 = 1; [110] 2/Wurzel6 = 0,8165; [100] 1/Wurzel3 = 0,5774.
  - Streuung: c_loc^2(n) = c_eff^2 + beta(n) k^2 mit beta = a + b S4. Aus PLAN-beta: gleich b = -4/9 (beta_100 = -1/9, beta_110 = 1/9, beta_111 = 1/3 - 4/27 = 5/27); ohne b = -3/4 (-1/2, -1/8, 1/4 - 1/4 = 0). Relative Streuung von c_loc = |b| k^2 Std(S4)/(2 c_eff^2).
  - Std(S4) auf der Kugel: E[S4] = 3/5, E[S4^2] = 3 x 1/9 + 6 x 1/105 = 41/105 = 0,39048, Var = 0,03048, Std = 0,17457.
  - Gleich: (4/9)(0,0025)(0,17457)/(4/3) = 1,455e-4 (Datei 1,453e-4 an 400 Fibonacci-Richtungen). Ohne: (3/4)(0,0025)(0,17457)/2 = 1,637e-4 (Datei 1,631e-4).
  - Verhaeltnis (3/4)/(4/9) x (2/3)/1 = 9/8. Spannweite mit S4 von 1/3 bis 1: (4/9)(0,0025)(2/3)/(4/3) = 5,56e-4 und (3/4)(0,0025)(2/3)/2 = 6,25e-4. Alles wie PLAN 3.4 und Datei.
  - Einheit a: |k| l = 0,05 x Wurzel3/4 = 0,02165, Streuung x (0,433)^2 = 3/16: 1,45e-4 x 0,1875 = 2,72e-5 (Datei 2,73e-5).
- **Beleglücke (B5):** haupt.json enthaelt keinen Code-Hash, und es gibt keine .69-seitige Einfrierliste. Dass H1 mit dem eingefrorenen kac_wick.py lief, ist nur mittelbar belegt (lokale Kopie gleich Einfrierliste; Ergebnis gleich Schreibtisch). Zum Vergleich: TT-GLAS-2 schreibt skript_sha256 in jede Ergebnisdatei.
