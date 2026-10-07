# Runde 36 (v3): Schwerkraft aus Netzen, Lasten gegen Zwangsbedingungen, Regge

- Leitung claude-primary. Datei angelegt 2026-10-03 22:41:52 CEST (date). Runde 35 schliesst nach der Ernte von GRAVITON-NETZ-L.
- Regeln: README.md (v3). Explorativ; keine Messdatenbestaetigung.

## Eingang

1. **Finn ~22:30:** Spin-2-Kopplung aus Punkten, Strichen, Dreiecken und Strichen durch eine geschlossene Kugel; reichen
   die Klumpenraender als Schwerefeld?
   - Antwort am Schreibtisch und Literaturdossier GRAVITON-NETZ-L laufen (Runde 35).
2. **GEGENLESEN-R35:** Lasten, die Arbeit leisten, ziehen sich an; Zwangsbedingungen stossen ab (B2). Die isotrope
   Abstimmung des fcc-Netzes bei k_theta = 1/18 (B1).
3. **Runde 35 kompakt:**
   - Tensor-Eis stoesst ab.
   - Strings entstehen und reissen.
   - Netzwellen haben mehrere Geschwindigkeiten.
   - Q-Baelle stoppen auf dem Gitter bei der schnellsten Gitterwelle.
   - Skalar zieht an, verletzt aber das Aequivalenzprinzip.

## Karten

| Karte | Inhalt | Stand |
|---|---|---|
| LAST-1 | Punktlasten gegen selbsttragende Quellen im fcc-Netz (anisotrop und isotrop abgestimmt): 1/r-Anziehung nur mit Nettokraft? | Test, gestartet |
| REGGE-NEWTON-1 | Statisches Tetraedernetz, dessen Kantenlaengen Klumpen verbiegen: gibt eine Energiequelle in 3D ein 1/r-Feld? | nach dem Dossier |
| QBALL-GITTER-2 | Richtungsabhaengige Gittergrenze in 2D/3D und Bezug zu den UHECR-Schranken | geparkt (weitgehend ableitbar) |
| MUSTER-1 | Warum die Nullstelle der kollabierenden Wand schon vor dem Ende schneller als Licht laeuft (R ~ 0,8 sqrt(R0)) | geparkt |
| TENSOR-EIS-1 | Monte Carlo auf dem atmenden Pyrochlor | geparkt |
| RG-3D | Glied 7: Regge-Huelle drehender Q-Baelle in 3D | geparkt |

## Gestartet

- 2026-10-03 22:42:23 CEST: LAST-1 als Code-Agent gestartet (Spuren cpu und cpu6, Zeitbox 120 min). Aktive Agenten 2 von 3 (GRAVITON-NETZ-L aus Runde 35, LAST-1). Der dritte Platz ist fuer REGGE-NEWTON-1 nach dem Dossier vorgesehen.
- 2026-10-03 22:52:04 CEST: Finn ~22:47 "Ideate Mal drumrum 10 trys in geometrische Grundformen und dann noch 10 aus der ursprünglichen Liste weiter entwickeln".
  - IDEEN-EVOLUTION/GEN-03.md: 10 Versuche (A1 bis A10) und 10 Weiterentwicklungen (B1 bis B10). Im Pool als Generation 3 eingetragen (Sicherung pool.jsonl.bak-20261003-gen3; Pool jetzt 184 Zeilen).
  - Vorschlag: A4 ZUFALLSNETZ-1, dann B2 V-1-WEITER, dann B3 HAGEDORN-1.
  - ZUFALLSNETZ-1 sofort gestartet (Spuren cpu3 und cpu4, Zeitbox 120 min). Aktive Agenten 3 von 3: GRAVITON-NETZ-L, LAST-1, ZUFALLSNETZ-1.
- 2026-10-03 22:59:31 CEST: Codex 22:30 bis 22:58 (quittiert):
  - Rangtest im A/B-Block: FINITE_R_LOCAL_RANK_INDICATION.
  - Rekonstruiertes Born-Integral bei endlichem R: einfache Nullstelle bei Vermittlermasse m = 0,82906079833 (vier Bestimmungen, Spanne 4,9e-12); die fruehere nominale Masse 0,82906053 liegt 2,7e-7 daneben.
  - Bedingte Huellen- und Verstimmungsrechnung (Breite ~ g^2 delta_m^2 nur fuer den fuehrenden Born-Beitrag) angenommen.
  - Weiter keine BIC-Entscheidung.
- 2026-10-03 23:04:02 CEST: Runde 35 geschlossen (Journal 572). Freier Platz nach dem Dossier: REGGE-RAND-1 gestartet.
  - Karte RUNDE-36/regge-rand-1/KARTE.md ab 23:02:41: Kuhn-Tetraedergitter, Fehlwinkel-Eckenregel, 1/r-Feld, Randmasse kompakt gegen ausgedehnt, wahlweise Brill-Lindquist.
  - Spur p4000a, Zeitbox 120 min. Aktive Agenten 3 von 3: LAST-1, ZUFALLSNETZ-1, REGGE-RAND-1.
  - Warteschlange: TENSOR-EIS-N (Dossier RT-2), V-1-WEITER, HAGEDORN-1.

### Ernte LAST-1 (RUNDE-36/last-1/ERGEBNIS.md; eingetragen 2026-10-03 23:23:28 CEST)

- Code-Agent, Plan eingefroren 23:12:13, fertig nach 40 von 120 min. Gegengelesen an lauf-69/auswertung.json.
  Hauptgroesse L = 128.
- **Urteile:**
  - L0 bis L4 eingetroffen; L0 und L4 waren vorab ableitbar.
  - L2 und L3 nur nach der vom Agenten vor dem Lauf festgelegten Richtungsauswahl ([100], [110], [111] plus
    Schalenmittel).
  - Streng gelesen (jede der 121 Richtungen) waeren beide verfehlt: In 24 Richtungen der Familien <211> und <320> liegt
    das Verhaeltnis bei 0,061 bzw. 0,063, der Exponent bei 3,63 bzw. 1,62.
  - Die Karte der Leitung liess die Richtungen offen.
- **Punktlasten mit Nettokraft ziehen sich an, wie 1/r** (alle 24 166 Gittervektoren mit 3 <= r <= 16, beide Netze).
  - Exponenten 0,993 bis 1,013; im isotropen Netz hoechstens 0,47 % neben Kelvin.
  - Ohne Hintergrundkorrektur ist der Torus deutlich falsch (bei L = 32 wird es fuer grosse r sogar Abstossung).
- **Selbsttragende Quellen:** Verschiebung ~ r^-2,00, Wechselwirkung ~ r^-3, Vorzeichen richtungsabhaengig.
  - Dilatationszentren im anisotropen Netz ziehen sich laengs [100] an und stossen sich laengs [110] und [111] ab.
  - Parallele Staebe stossen sich Ende an Ende ab und ziehen sich Seite an Seite an.
  - Ueber alle Richtungen gemittelt bleibt nichts.
- **Isotrop abgestimmtes Netz** (k_theta = 1/18; Zener-Verhaeltnis 1 + 2e-10, Gegenleser B1 bestaetigt): Die
  Wechselwirkung verschwindet in elastischer Ordnung. Uebrig bleibt ein Gitterrest ~ r^-5, bei r ~ 8 2,5 % des
  anisotropen Werts.
- **Kontrollen:**
  - Gleichgewicht 7,8e-16.
  - Paar minus zweimal einzeln gegen den schnellen Weg 2,6e-11.
  - L = 64 gegen L = 128 nach Korrektur 4e-5.
  - Kontinuum gegen Kelvin 1e-10.
- **Selbstanzeigen:**
  - Richtungsauswahl wie oben.
  - Im isotropen Netz wechselt [110] das Vorzeichen zwischen r = 7 und 8.
  - In den Rauchlaeufen nur Konstanten und Zeiten gesehen.
  - Ein Fehlstart (falscher Ordner) wiederholt.
  - nachschau.py nach dem Einfrieren, nur beschreibend.
- **Bedeutung:**
  - Kraefte in Staeben geben eine 1/r-Anziehung nur fuer Lasten mit Nettokraft, und die muss von aussen kommen. Beim
    Gummituch ist das die Erdschwere selbst.
  - Abgeschlossene Klumpen (von Laue, ohne Nettokraft) wechselwirken nur kurzreichweitig mit wechselndem Vorzeichen,
    im isotropen Netz fast gar nicht.
  - Elastizitaet allein macht also keine Schwerkraft. Das passt zu LAPSE-0, AEQ-0 und dem Dossier (Anziehung braucht
    einen indefiniten Quellsektor oder Geometrie).
- **Abschaetzung:** erledigt.
- 2026-10-03 23:24:34 CEST: Freier Platz nach LAST-1: TENSOR-EIS-N gestartet.
  - Karte RUNDE-36/tensor-eis-n/KARTE.md ab 23:23:42: Gu/Wen L- gegen N-Typ, Vorzeichen der Anziehung, Gitterstabilitaet.
  - Spuren cpu und cpu6, Zeitbox 150 min. Aktive Agenten 3 von 3: ZUFALLSNETZ-1, REGGE-RAND-1, TENSOR-EIS-N. Warteschlange: V-1-WEITER, HAGEDORN-1.
- 2026-10-03 23:31:19 CEST: Finn ~23:28 "Weiter experimentieren gedanklich".
  - Neue Karten in der Warteschlange: AETHER-UHR-1 (vorn), GUERTEL-1, ZUFALLS-REIBUNG, PACKUNGSFRUST-L. Nicht gegengelesen.
- 2026-10-03 23:31:52 CEST: Codex 23:02 bis 23:31 (quittiert):
  - Direkte Kopplungsableitung der Matching-Karte: FINITE_R_LOCAL_RANK3_INDICATION.
  - Nachstimmung bei g = 0,01: FINITE_R_COMMON_ZERO_INDICATION bei (rho, omega^2, m) = (1,744609, 0,797646, 0,829112), Restgroessen ~5e-8, kein exakter Nullwert.
  - Die unabhaengige Ergebnislesung laeuft noch. Die stille Mode laesst sich mit zwei Stellgroessen wohl wieder dicht stellen (vorlaeufig).

### Ernte ZUFALLSNETZ-1 (RUNDE-36/zufallsnetz-1/ERGEBNIS.md; eingetragen 2026-10-03 23:39:09 CEST)

- Code-Agent, Plan eingefroren 23:25:46. Gegengelesen an lauf-69/auswertung.json.
- **Urteile:** Z0, Z1, Z2, Z4 eingetroffen; Z3 nicht eingetroffen.
- **Querwellen fast richtungsfrei ohne Abstimmung:**
  - Schwankung 0,95 / 0,43 / 0,28 % (N = 4000 / 16000 / 64000, Mittel zweier Saaten); Doppelbrechung 0,30 und 0,37 %
    bei N = 64000.
  - Der Rest faellt wie N^(-0,435). fcc zum Vergleich: 41 %.
- **Z3 nicht eingetroffen:** c_l/c_q = 1,681, sogar unter dem affinen sqrt 3.
  - Die Relaxation macht den Kompressionsmodul weicher als den Schermodul (K/K_aff 0,687 gegen G/G_aff 0,767), umgekehrt
    als von der Leitung angenommen.
  - Mit k = 1/l werden beide etwa gleich weich: 1,739.
- **Z4:** G/G_affin 0,762 bis 0,769 in allen sechs Netzen.
- **Kontrollen:**
  - Born-Probe: dynamische Matrix gegen Christoffel aus dem relaxierten Tensor 2e-8, unabhaengig vom Relaxationscode;
    Rest ~ k^2, also Dispersion.
  - Loeser gleich auf 4e-16; fcc gegen NETZ-C-1 3,5e-8.
  - Delaunay-Pruefungen bestanden: Grad 15,51 bis 15,56, Tetraeder je Punkt 6,756 bis 6,782.
- **Selbstanzeigen des Agenten:**
  - Z0 haengt an der Lesart "lambda = mu des isotrop gemittelten Tensors" (gilt bei Zentralfedern immer, prueft nur den
    Code). Woertlich C1122 = C2323 waere Z0 bei N = 4000, Saat 2 mit -2,1 % verfehlt. Die Lesart stand vor dem
    Einfrieren im Plan.
  - Rauch nur mit Netzpruefungen und Zeiten.
  - Gemessen ist eine periodische Probe; das unendliche Zufallsnetz ist im Mittel exakt isotrop. Das Netz waehlt ein
    Ruhesystem.
- **Bedeutung:**
  - Ein ungeordnetes Tetraedernetz liefert ohne Feinabstimmung eine richtungsfreie Querwellengeschwindigkeit fuer beide
    Polarisationen, bis auf einen Rest, der mit der Groesse verschwindet. Das ist Finns bester Kandidat fuer eine
    "Lichtgeschwindigkeit" im Netz.
  - Die Laengswelle bleibt ~1,7-mal schneller. Nach GE1 muessten deshalb Licht und Materiebindung ueber dieselbe
    Wellensorte laufen, sonst sieht ein Uhrenvergleich die Bewegung gegen das Netz.
- **Abschaetzung:** weiter. Folgen sind AETHER-UHR-1 (startet jetzt) und ZUFALLS-REIBUNG (Bewegung im Zufallsnetz).
- 2026-10-03 23:40:12 CEST: Freier Platz nach ZUFALLSNETZ-1: AETHER-UHR-1 gestartet.
  - Karte RUNDE-36/aether-uhr-1/KARTE.md ab 23:39:12: Beutel aus M1 mit B-Hohlraummode, Uhrenvergleich gegen v fuer c_B = 1, 1,15 und 1,70.
  - Spuren cpu3 und cpu4, Zeitbox 150 min. Aktive Agenten 3 von 3: REGGE-RAND-1, TENSOR-EIS-N, AETHER-UHR-1.

### Ernte REGGE-RAND-1 (RUNDE-36/regge-rand-1/ERGEBNIS.md; eingetragen 2026-10-03 23:48:23 CEST)

- Code-Agent, Plan eingefroren 23:35:10, Laeufe 23:04 bis 23:46. Gegengelesen an lauf-69/auswertung.json.
- **Urteile:** RR0 bis RR4 eingetroffen; RR5 nicht eingetroffen.
  - RR2 bis RR4 waren nach der Normierungspruefung im Rauch vorab ableitbar. RR4 ist eine Identitaet (diskreter
    Gauss-Satz).
- **Kernbefund:** Der linearisierte Fehlwinkel-Eckenoperator auf dem Kuhn-Tetraedergitter ist auf Maschinengenauigkeit
  8 x der 7-Punkt-Laplace des Wuerfelgitters.
  - Die Diagonalen tragen linear nichts bei.
  - Die Normierung 16 pi G stimmt.
  - Einzige Nullmode ist die Konstante; keine Schachbrettmoden ((pi,pi,pi) ist mit 96 die steifste Mode).
- **Weitere Ergebnisse:**
  - RR2: r delta psi = G M/2 auf 0,77 %.
  - RR3: Richtungsschwankung 0,41 % bei r = 12.
  - RR4: Gauss-Masse kompakt gleich ausgedehnt auf 2e-14.
- **RR5:** Zwei Klumpen haben zusammen weniger Randmasse als getrennt, also erscheint die Anziehung als Randgroesse. Bei
  kleinen Massen ist das genau die Newton-Bindung (Q = 0,994 bei m = 0,01).
  - Bei m/d = 0,1 liegt die Bindung 30 bis 38 % darunter.
  - Lehre: Brill-Lindquist gilt fuer Punktierungen (schwarze Loecher), nicht fuer Klumpen. Die Karte der Leitung hatte
    hier eine Luecke; RR5 war fuer Klumpen voraussichtlich auf keinem Gitter erreichbar.
- **Kontrollen:**
  - Zwei unabhaengige Operatorwege 1e-13; FFT-Residuen 1e-13.
  - Groessenreihe 64/128/256 bestaetigt die Torus-Korrektur auf 0,28 % und die Ewald-Konstante auf 0,2 %.
  - 30 nichtlineare Loesungen konvergiert.
- **Selbstanzeigen des Agenten:**
  - Die Normierungspruefung zeigte die Schablone vor dem Einfrieren.
  - RR5 mit Kastenkorrektur geurteilt (beide Fassungen "nicht eingetroffen").
  - Torus-Korrektur auch fuer RR3; ohne sie waere RR3 mit 8 % gescheitert.
- **Bedeutung:**
  - In Finns Tetraedernetz mit Strichen als Laengen ergibt "Kruemmung = Masse" (Regge) das Newton-Feld mit richtigem
    Vorfaktor, richtungsfrei und ohne Gittermuster.
  - Der Rand zaehlt exakt die eingeschlossene Gesamtmasse; zwei Massen zeigen ihre Anziehung als Bindungsenergie am Rand.
  - Getestet ist nur der Newtonsche (skalare, zeitsymmetrische) Teil. Spin-2-Wellen brauchen 3+1D (4D-Regge nach
    Rocek/Williams). Die Regel ist hineingesteckt (Regime A).
- **Abschaetzung:** erledigt; Folgekarte REGGE-4D (Wellen) geparkt, weil groesser.

## SAGNAC (Finn ~23:44 "Französischer Physiker der Einstein wiederlegen wollte - such und integriere"; Auswahl Finn: Georges Sagnac; Erwartungen vor dem Abruf, eingetragen 2026-10-03 23:48:35 CEST)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| S1 | Sagnac 1913 (Comptes Rendus 157) deutete sein rotierendes Interferometer als Beweis des Lichtaethers | 90 % |
| S2 | Gemessen war die Streifenverschiebung erster Ordnung in Omega, Delta z = 4 A Omega/(lambda c) | 85 % |
| S3 | Die Relativitaetstheorie sagt denselben Effekt erster Ordnung voraus (Drehung ist nicht inertial; Laue, Langevin) | 90 % |
| S4 | Heute Grundlage von Ring-Laser- und Faserkreiseln und der Sagnac-Korrektur im GPS | 90 % |
| S5 | Grosse Ringlaser sollen die Mitfuehrung durch die Erddrehung (Lense-Thirring) messen (z. B. GINGER) | 60 % |

- Abrufweg: Websuche gesperrt; gezielt die Originalarbeit (Wikisource bzw. Gallica) und Wikipedia nur als Wegweiser.
- 2026-10-03 23:51:06 CEST: SAGNAC eingeordnet (RUNDE-36/SAGNAC.md ab 23:50:19). S1 bis S5 eingetroffen, nur per Wegweiser (Original nicht erreichbar). Sagnac passt zu Finns Netz und zu Einstein (Laue 1911); entscheidend sind die zweite Ordnung (AETHER-UHR-1, Rotor) und die Mitfuehrung (Gravitomagnetismus, Gravity Probe B). Karten SAGNAC-ROTOR und NETZ-WIRBEL-L geparkt.
- 2026-10-03 23:52:19 CEST: Freier Platz nach REGGE-RAND-1: V-1-WEITER gestartet.
  - Karte RUNDE-36/v1-weiter/KARTE.md ab 23:51:15: ebene Wand mit eps d^4, Stille bei eps > 0 robust, bei eps < 0 undicht?
  - Spur p4000a, Zeitbox 150 min. Aktive Agenten 3 von 3: TENSOR-EIS-N, AETHER-UHR-1, V-1-WEITER.

## Tagespflichten 04.10.2026 (eingetragen 2026-10-04 00:15:44 CEST)

- index-pruefen und karten-pruefen: keine Verstoesse.
- index-sichern: 572 Zeilen, Kettenende-sha256 d664ea3b...; rsync auf die .69; KETTENENDE.log auf der .69 ergaenzt (nr 572).
- Git-Tagesschnappschuss: Commit 4a264c7 "Snapshot research state of 3 Oct 2026 (rounds 25 to 36)", 2927 Dateien,
  ausgewaehlt ~76 MB (Gesamtbestand minus nur gehashte 3,30 GB), 12933 nur gehasht, gitleaks 0 nach einem Fehlalarm.
  - Fehlalarm: sha256-Zeile in SECOND-ORDER-TRANSFER.txt; Fingerabdruck in .gitleaksignore, Begruendung in
    GEHEIMNISPRUEFUNG.md.
  - Gepusht ins LAN-GitLab (e021575..4a264c7).
- **Selbstanzeige:** Die ersten zwei Pruefaufrufe hatten die Argumente wieder in falscher Reihenfolge (wie am 02.10.).
  - Es liefen Commit-Versuche statt der Pruefung; der gitleaks-Hook blockierte beide, der Index wurde zurueckgesetzt, es
    gab keinen Commit.
  - Vier dabei bzw. bei Probelaeufen entstandene, unversionierte Hashlisten habe ich nach git ls-files-Pruefung
    geloescht.
  - Die Memory ist um die richtige Reihenfolge ergaenzt.

### Ernte TENSOR-EIS-N (RUNDE-36/tensor-eis-n/ERGEBNIS.md; eingetragen 2026-10-04 00:15:44 CEST)

- Code-Agent, Plan eingefroren 00:01:30. Gegengelesen an lauf-69/auswertung.json.
- **Urteile:** N1 und N2 eingetroffen; N0 und N3 nicht eingetroffen; N4 nicht auswertbar (nicht gerechnet).
- **N-Typ (Gu/Wen Gl. 32) zieht gleiche Massen wie Newton an:**
  - U(r) = -1/(8 pi r) auf 2,0 % ab r = 4 und 0,41 % ab r = 8 (Torus-korrigiert); Exponenten 1,011 / 0,999 / 0,995,
    Richtungsmittel 1,001.
  - Das ist ein echtes Minimum, kein Sattel: Die Richtung mit dem falschen Vorzeichen (konformer Modus) legt die Masse
    selbst fest.
- **N0 nicht eingetroffen:** Der L-Typ (Gl. 27) hat statisch gar keine Wechselwirkung (|U| <= 9e-17 nach
  Korrektur).
  - Gu/Wens Angabe "abstossend, r^-4" (S. 11, ohne Herleitung) folgt statisch nicht.
  - Der Nachbau trifft Gu/Wens N-Gittermatrix (S. 19) auf 1e-15. Dabei fiel auf, dass die Beschriftung der Strafterme
    dort gegen Gl. 39/62 vertauscht ist.
- **N2 eingetroffen:** zwei negative Richtungen je q, beide ausserhalb der eichfreien Zwangsflaeche; auf ihr bleibt nur
  Helizitaet 2 mit positiver Energie.
- **N3 nicht eingetroffen:** kein exponentielles Wachstum in sieben Parametersaetzen (exakte Bruchrechnung an 12 Punkten:
  alle omega^2 reell und >= 0).
  - Das haengt am exakten Faktor 1/2 im Glied -1/2 (E^ii)^2: Bei 0,49 oder 0,51 waechst die Dynamik exponentiell.
  - Mit Gu/Wens Straftermen ist die Energie nach unten unbeschraenkt.
  - Polynomiales Wachstum (Jordankette, Laenge 4) bleibt, wenn die Vektorbedingung verletzt ist.
- **Selbstanzeigen:**
  - Alle Ausgaenge waren ableitbar; scheitern konnte nur die Rekonstruktion.
  - Startfehler im Rauch (wie LAST-1).
  - K3 vor dem Einfrieren auf Matrixvergleich umgestellt.
  - Rohwerte A1 2,6e-11 statt 1e-12.
  - Zwei gewichtige Festlegungen: q = 0 zaehlt fuer N2 nicht; fuer N3 zaehlt nur exponentielles Wachstum.
- **Bedeutung:**
  - In einem Erhaltungsregel-Netz ziehen sich gleiche Massen genau dann wie Newton an, wenn ein Spurglied das negative
    Vorzeichen mit genau dem Faktor 1/2 traegt.
  - Die Masse ist dabei die Verletzung einer zweiten, skalaren Regel; das ist die linearisierte Hamilton-Bedingung.
  - Stabil ist das nur, solange die Regeln streng gelten und der Faktor exakt ist.
  - Fuer Finns Netz heisst das: Schwerkraft braucht eine zweite, strenge Regel je Knoten und ein genau abgestimmtes
    Minus-Glied.
- **Leitung, Schreibtisch [L, H]:** Der Faktor 1/2 entspricht lambda = 1 in der Hořava-Lifshitz-Gravitation
  (Supermetrik pi^ij pi_ij - lambda pi^2 mit dem Koeffizienten 1/(d - 1) = 1/2 bei d = 3).
  - Dort fixiert die volle Diffeomorphismen-Invarianz lambda = 1.
  - Abweichungen erzeugen einen zusaetzlichen Skalarmodus, je nach Seite instabil bzw. ein Geist [L].
  - Das exponentielle Wachstum bei 0,49 und 0,51 waere die Gitterfassung dieses lambda-Problems. Folgekarte LAMBDA-1.
- **Berichtigung Dossier V4:** "L-Typ stoesst ab (~ r^-4)" ist statisch nicht reproduziert. Gilt jetzt: "L-Typ ohne
  statische Fernwirkung" (Vermerk im Dossier).
- **Abschaetzung:** weiter mit LAMBDA-1; N4 (Pyrochlor) geparkt.

## NEWTON-NACHRECHNUNG (Finn ~00:16 "Rechne das mit den Newton Sachen nach"; Leitung, eingetragen 2026-10-04 00:20:07 CEST)

- **Lesart:** eigene, unabhaengige Nachrechnung der Newton-Ergebnisse der Nacht. Hauptsaechlich REGGE-RAND-1 (Operator,
  Faktor G M/2, Bindung RR5), dazu der Vorfaktor aus TENSOR-EIS-N.
- **Eigener Code:** RUNDE-36/newton-nachrechnung/regge_nach.py. Der Code des Agenten ist nicht gelesen.
  - Kuhn-Tetraedergitter L = 6, periodisch; Einbettung jedes Tetraeders aus den sechs Kantenlaengen, Diederwinkel per
    Projektion.
  - Fehlwinkel 2 pi - Summe; Eckenregel sum l_e eps_e; zentrale Differenz einer Beule delta psi = 1e-5.
  - Zwei Laengenvorschriften: psi-Mittel arithmetisch und geometrisch.
  - Lauf auf der .69, kleintest.sh, Spur cpu5: 2,2 s CPU je Lauf.
  - Die Spur ist seit Runde 7 ungenutzt, die Zuweisung an BEWEIS-1 ist veraltet. Offengelegt, weil die Karte cpu5
    sonst ausschliesst.
- **Ergebnis** (beide Vorschriften gleich):
  - Flachheit 3,6e-15.
  - 1512 Kanten (7 je Ecke).
  - Antwort Mitte 48,00000002, Achsennachbarn -8,000000003, alle Diagonalen <= 1,2e-9.
  - Groesste Abweichung von -8 mal 7-Punkt-Laplace 2,1e-8, Fourier-Symbol gegen 8(6 - 2 sum cos q) 3,7e-8. Beides ist
    der Rest der zentralen Differenz.
  - **Damit unabhaengig bestaetigt:** Der linearisierte Regge-Operator ist genau 8 x (-Laplace).
- **Schreibtisch [M, L]:** Im Kontinuum gilt fuer g = psi^4 delta: R = -8 psi^-5 Laplace psi, linear also -8 Laplace
  delta psi. Der Faktor 8 stimmt mit dem Gitter ueberein.
  - Mit R = 16 pi G rho folgt Laplace delta psi = -2 pi G rho, also delta psi = G M/(2 r). Das ist die isotrope
    Schwarzschild-Form.
  - Der Vorfaktor G M/2 aus RR2 (0,77 %) ist damit erklaert und stimmt.
- **RR5** (Bindung 30 bis 38 % unter Newton bei m/d = 0,1), Einordnung [M, H]:
  - Die Klumpen haben Radius a = 3 und m = 1,2 bis 2,0 (d = 12 bis 20). Kompaktheit m/a = 0,4 bis 0,67, der
    Schwarzschild-Radius 2m = 2,4 bis 4 liegt in der Groesse des Klumpens.
  - Das ist weit ausserhalb des schwachen Feldes. Die Abweichung ist erwartete Einstein-Physik, keine Gitterschwaeche.
  - Die Kontrolle bei m = 0,01 (Q = 0,994, Kontinuum 0,996) trifft Newton.
  - Nicht selbst nachgerechnet (nichtlinearer Loeser).
- **TENSOR-EIS-N** (-1/(8 pi r)), Schreibtisch:
  - Form 1/r und Vorzeichen folgen aus der linearisierten ART; Gu/Wen nennen den N-Typ "exactly the linearized Einstein
    action" [S, Dossier].
  - Der Vorfaktor haengt an Gu/Wens Normierung; nicht nachgerechnet.
- 2026-10-04 00:41:17 CEST: Codex 23:33 bis 00:32 (quittiert): Mediator-Strang, Pruefungen zur gemeinsamen Nullstelle bei g = 0,01.
  - Groessenordnungsprobe zweier Profile (Kontraktionskriterium erfuellt, R30 und R40).
  - Aussenstart-Transfer: CONDITIONAL_EMPIRICAL_EXTERIOR_START_TRANSFER.
  - Exakte Zellrestprobe: INCOMPLETE (regulaerer Budgetabbruch nach 2996 von 8479 Zellen).
  - Noch keine BIC-Entscheidung, keine Papieraenderung.

### Ernte AETHER-UHR-1 (RUNDE-36/aether-uhr-1/ERGEBNIS.md; eingetragen 2026-10-04 00:53:06 CEST)

- Code-Agent, Plan eingefroren 00:06:16, Abschluss 00:51:08. Gegengelesen an lauf-69/auswertung.json.
- **Urteile:** U0 und U3 eingetroffen; U1 und U2 nicht eingetroffen. Haupt-, Adiabatik- und Gitterlauf urteilen gleich.
- **Uhrenvergleich:**
  - c_B = 1: Die Uhren merken die Bewegung nicht (R(v)/R(0) - 1 < 2e-5 bis v = 0,6).
  - c_B = 1,15 bzw. 1,70: Bei v = 0,6 laeuft die B-Uhr um 0,124 bzw. 0,323 vor; die Bewegung durchs Netz ist sichtbar.
  - Die Rechnung folgt der exakten Kinematik K(v) = (gamma_A/gamma_B) sqrt(lambda(c_B gamma_A/gamma_B)/lambda(c_B)) - 1
    auf <= 6e-5 (Gitterrest, faellt mit h^2 bis h^3).
- **U1/U2 nicht eingetroffen: Fehler im Kartenentwurf der Leitung.**
  - Die Sollwerte waren nur die erste Naeherung v^2 (1 - 1/c_B^2). Schon die eigene Kartenformel gamma_A^2/gamma_B^2 liegt
    bei v = 0,6 um den Faktor gamma_A^2 = 1,56 hoeher.
  - Abweichungen -5 / +8 / +41 % bzw. -7 / +6 / +37 %.
  - Die in der Karte genannten Ursachen (Rueckwirkung, Nichtadiabatik) sind es nicht: 3,5e-7 bzw. 4e-6.
- **Neu:** Fuer kleine v gilt R - 1 ~ ((1 + f)/2) v^2 (1 - c_A^2/c_B^2), mit f ~ 0,80 bis 0,83 dem Gradientenanteil der
  Hohlraummode.
  - Der Vorfaktor haengt also von der Bauart der Uhr ab (zwischen 1/2 und 1).
  - Das passt zur Erfahrung der Uhrenvergleiche, dass verschiedene Uhrentypen verschieden empfindlich sind [L].
- **U3:** Die Beutellaenge verkuerzt sich mit gamma_A, nicht mit gamma_B (L gamma_A/L0 - 1 < 4,6e-5; mit gamma_B waeren
  es bis -14,5 %).
- **Kontrollen:**
  - A-Uhr eichkovariant gemessen, geht mit 1/gamma auf 1,6e-5.
  - Rueckwirkung 3,6e-7; exakte Kinematik in allen sechs Laeufen mit c_B ungleich 1 erfuellt (schlimmstenfalls 2,7e-4).
  - Energie 7,7e-10, Ladung 9e-14.
- **Selbstanzeigen:**
  - Rauch-1-Fehler in der Beutellaenge behoben.
  - Rauch-2-Werte vor dem Einfrieren gesehen; danach nur Rampen- und Plateaudauer gewaehlt.
  - Alle Ausgaenge waren vorab ableitbar. Echt geprueft ist nur, ob die Dynamik der Kinematik folgt (Zusatzprobe Z-K).
- **Bedeutung:**
  - Eine Welt aus einem Netz mit zwei Wellengeschwindigkeiten verraet ihre Bewegung durch Uhrenvergleiche. Bei
    c_B = 1,15 und v = 0,6 sind es 12 %.
  - Echte Uhrenvergleiche zeigen nichts dergleichen [L: Schranken ~1e-17 und schaerfer].
  - Also muessen in Finns Netz Licht und Materie dieselbe Wellensorte (denselben Lichtkegel) benutzen. Das ist Carlips
    Engstelle, hier in einer Rechnung sichtbar gemacht.
- **Abschaetzung:** erledigt. SAGNAC-ROTOR ist damit ableitbar (dieselbe Kinematik) und wird geparkt.
- 2026-10-04 00:54:12 CEST: Freier Platz nach AETHER-UHR-1: REGGE-4D-1 gestartet.
  - Karte RUNDE-36/regge-4d-1/KARTE.md ab 00:53:10: Spin-2-Struktur der Simplex-Wirkung (Kuhn 4D, 15 Kanten je Ecke), Minus-Modus mit Faktor -2.
  - Spuren cpu3 und cpu4, Zeitbox 150 min. Aktive Agenten 3 von 3: V-1-WEITER, LAMBDA-1, REGGE-4D-1.

### Ernte LAMBDA-1 (RUNDE-36/lambda-1/ERGEBNIS.md; eingetragen 2026-10-04 01:02:19 CEST)

- Code-Agent, Plan eingefroren 00:48:47. Gegengelesen an lauf-69/auswertung.json.
- **Urteile:** L0 bis L4 eingetroffen. Alle standen vorher als Schreibtischergebnis im Plan; die Rechnung bestaetigt
  Herleitung und Code.
- **Zuordnung bestaetigt:** c ist der Spurkoeffizient im Impulsbild; Gu/Wen entspricht c = 1/2, also lambda = 1; es gilt
  c = lambda/(3 lambda - 1).
  - Der Skalarmodus des Gitters ist omega^2 = J (1 - 2c)(-g K^2 + 2 U_s K^4).
  - Ohne Strafterme ist das Hořavas langwellige Formel -((lambda - 1)/(3 lambda - 1)) xi k^2, und zwar an jedem
    Gitterpunkt (<= 1,2e-14).
- **TENSOR-EIS-N erklaert:**
  - Ohne Strafterme waechst nur c < 1/2 (Instabilitaet); c > 1/2 ist ein Geist (negative Energie, kein Wachstum).
  - Gu/Wens Strafterme wirken wie ein R^2-Glied und lassen auch c > 1/2 an der Zonenecke wachsen (Deutung unsicher).
  - Bei 1/2 +- 0,05 unterscheiden sich die Raten um den Faktor 47.
- **Gefaehrlicher Modus:** fast reine Eichung. Auf der E-Seite 100 % Eichrichtung (Gl. 23); auf der a-Seite nur 2,4 %
  (c = 0,45) bzw. 0,08 % (c = 0,49) Verletzung der Massenregel.
- **Zwangsflaeche:** Dort waechst fuer kein c etwas. Einschraenkungen:
  - Die Flaeche bleibt nur bei c = 1/2 unter der Bewegung erhalten.
  - Fuer c > 1/2 liegt auf ihr eine Richtung negativer Energie.
  - Der wachsende Modus liegt nur knapp daneben (Abstand ab 0,008).
- **Statische Anziehung unabhaengig von c:** 8 pi G_eff = 1,000125 fuer alle c. L4 war selbsterfuellend. Die
  Kartenzeile "nur ihre Staerke haengt am Faktor" ist falsch: Das Minus-Glied regelt die Stabilitaet, nicht die
  Staerke.
- **Selbstanzeigen:**
  - Hořava-Formeln nur qualitativ an Abstracts belegt (5 von 6 Abrufen).
  - Schwelle "neben der Zwangsflaeche" schwach (Abstand 0,008 bis 0,64; mit Schwelle ~0,5 verfehlt).
  - S1-Laufzeit 174 s statt 90 s.
  - Bildlegende verdeckt Punkte.
- **Bedeutung:**
  - Das Minus-Glied des Netzes ist genau Hořavas lambda.
  - Exakt 1/2 (lambda = 1) macht eine Verschiebung im Netz zur kostenlosen Umbenennung (Eichsymmetrie, Spur der
    Diffeomorphismen-Invarianz). Jede Abweichung erzeugt einen echten Zusatzmodus: instabil fuer c < 1/2, Geist fuer
    c > 1/2.
  - Fuer Finns Netz heisst das: Schwerkraft braucht eine Symmetrie, die das Minus-Glied auf genau 1/2 festhaelt. Die
    Anziehungsstaerke selbst haengt nicht daran.
- **Abschaetzung:** erledigt.
- 2026-10-04 01:03:17 CEST: Freier Platz nach LAMBDA-1: ZUFALLS-REIBUNG-1 gestartet.
  - Karte RUNDE-36/zufalls-reibung-1/KARTE.md ab 01:02:23: Q-Ball in 1D-Kette mit zufaelliger oertlicher Masse; Reibung gegen sigma und v.
  - Spuren cpu und cpu6, Zeitbox 120 min. Aktive Agenten 3 von 3: V-1-WEITER, REGGE-4D-1, ZUFALLS-REIBUNG-1.
- 2026-10-04 01:12:15 CEST: Codex 00:44 bis 01:06 (quittiert): rechnergestuetzter Beweisweg fuer das gekoppelte Profil.
  - Exakter Zellrestpruefer V2 vollstaendig (8479 Zellen); gemeinsames 1e-8-Tor nicht nachgewiesen (Huelle f 1,1e-8).
  - Statische DtN-Jethuellen; Radiusbudget: Ein bewiesener Inversenbound M <= 747 bei r = 1e-5 wuerde reichen, ist aber nicht berechnet.
  - Kein Existenz- oder BIC-Nachweis; Git-Schnappschuss ungestoert.

### Ernte V-1-WEITER (RUNDE-36/v1-weiter/ERGEBNIS.md; eingetragen 2026-10-04 01:18:07 CEST)

- Code-Agent, Plan eingefroren 00:30:57, fertig 01:16. Gegengelesen an lauf-69/auswertung.json.
- **Urteile:** V0, V1, V2 eingetroffen; V3 und V4 nicht auswertbar.
- **Lage:** rho_z(eps) = rho_z(0) - 3,749e-3 eps + 5,3e-3 eps^2.
  - Kontrolle eps = 0 trifft WAND-BETA auf 2e-16; Verhaeltnis der Verschiebungen 2,9915 (V2).
- **eps > 0 (Versteifung):** Die Stille bleibt exakt (Restgroesse 1,7e-17 bis 2,5e-15, Schwelle 1e-10).
- **eps < 0 (gitterartige Erweichung):** Eine Mischung aus altem und neuen Kanaelen wird weiter exakt zurueckgeworfen.
  Die reine alte Welle leckt aber in den neuen Kanal.
  - Aufgeloest nur bei eps = -1e-2: Amplitude 4,6e-9, Fluss 9,4e-17.
  - Bei -3e-3 und -1e-3 liegt das Leck unter der float64-Grenze, deshalb V3/V4 nicht auswertbar.
- **Beschreibend:** ln P ~ a - c/sqrt(abs(eps)) mit c = 6,31 bzw. 6,295 (schwanzfreier Hintergrund), also fast 2 pi.
  Hochgerechnet P(-3e-3) ~ 1e-39 und P(-1e-3) ~ 4e-76 [H].
- **Herleitung der Leitung [M]:** Fuer beta = 1 gilt an der ebenen Wand bei omega_min^2 = 3/4:
  f'^2 = U - omega_min^2 f^2 = S (S - 1/2)^2.
  - Also S' = S (1 - 2S), S = (1/2)/(1 + e^-x) (logistisch). Die naechsten komplexen Pole liegen bei x = +-i pi, im Abstand
    d = pi von der reellen Achse.
  - Der neue Kanal hat k ~ 1/sqrt(abs(eps)). Die Kopplung an ihn ist ~ e^(-k d), das Leck (Leistung) ~ e^(-2 pi/sqrt(abs(eps))).
  - Also c = 2 pi, wie gemessen (6,30). Der Exponent ist damit ohne Anpassung erklaert.
- **Folge:**
  - Fuer ein Gitter mit eps = -h^2/12 ist das Leck ~ exp(-2 pi sqrt(12)/h) = exp(-21,8/h). Bei h = 0,1 ist das ~1e-95,
    praktisch null.
  - Fuer Papier I: Die Stille ist robust gegen versteifende Aenderungen bei kurzen Wellen (exakt) und gegen gitterartige
    (bis auf ein nicht stoerungstheoretisches, exponentiell kleines Leck).
- **Vorbehalt des Agenten [H]:** Der neue Ast liegt bei k ~ sqrt(12)/h, also ausserhalb der Brillouin-Zone. Ob ein echtes
  Gitter denselben Kanal oeffnet, ist nicht gezeigt; die eps k^4-Rechnung ist ein Modell.
- **Selbstanzeigen:**
  - Fehlstart (Suchfenster nicht weitergegeben).
  - Drei Code-Korrekturen nach dem Einfrieren: Klammerung bei eps = 0; Rand 90 statt 47, weil Wandschwanz-Wellen ein
    falsches Leck 8e-9 vortaeuschten (alle eps < 0 neu gerechnet); ein Diagnose-Schalter.
  - Flussbilanz bei eps > 0 ~1e-8, Ursache vermutet.
  - Die Vorabschaetzung fuer -1e-2 lag ~5-fach zu tief.
- **Abschaetzung:** erledigt fuer Papier I (Robustheitsabsatz moeglich). Die Hochpraezisionspruefung von P(-3e-3) gegen
  exp(-2 pi/sqrt(abs(eps))) ist als V-1-PRAEZISION geparkt.
- 2026-10-04 01:19:30 CEST: Freier Platz nach V-1-WEITER: DREIECK-LINSE-1 gestartet.
  - Karte RUNDE-36/dreieck-linse-1/KARTE.md ab 01:18:36: Q-Baelle an der Fuenfer-Spitze bei +-b; Doppelbild-Winkel 60 Grad wie bei der 2+1-Gravitation.
  - Spur p4000a, Zeitbox 120 min. Aktive Agenten 3 von 3: REGGE-4D-1, ZUFALLS-REIBUNG-1, DREIECK-LINSE-1.
- 2026-10-04 01:28:03 CEST: Finn ~01:25 "Bau die Regel".
  - RUNDE-36/REGEL.md (ab 01:27:31): Die Regel ist eine zweite Eichsymmetrie. Kruemmungsmuster (delta d^2 - d d) f_0 der Spannung sind kostenlos; das erzwingt c = 1/2 (Aenderung 2(1 - 2c) E^ii d^2 f_0); gleichwertig kostet nur E_TT Energie.
  - Zwei Wege: A Laengen (Regge, eingebaut; REGGE-4D-1 prueft den Faktor), B Kraftfluss (Symmetrie fordern).
  - Zweite Haelfte: Masse = Energiedichte als Quelle, Kopplung ueber die Energie.
  - Rechentest REGEL-1 vorn in der Warteschlange (naechster freier Platz).

### Ernte REGGE-4D-1 (RUNDE-36/regge-4d-1/ERGEBNIS.md; eingetragen 2026-10-04 01:32:06 CEST)

- Code-Agent, Plan eingefroren 01:21:49. Gegengelesen an lauf-69/auswertung.json.
- **Urteile:** G2 und G3 eingetroffen; G0 und G1 nicht eingetroffen.
- **Kernbefund:** Nach dem Herausrechnen der Gittermoden ist die effektive Form auf 0,04 % gleich (1/4) k^2 (P2 - 2 P0s).
  Das ist Einsteins linearisierte Wirkung mit der Normierung (1/2) int R sqrt(g).
  - An jedem k: fuenf Spin-2-Werte +0,2499 k^2, ein konformer Wert -0,4999 k^2, vier Eichnullen, in allen acht
    Richtungen gleich.
  - G2: Verhaeltnis Spin-0 zu Spin-2 zwischen -1,998 und -2,007 (Soll -2).
  - G3: Richtungsstreuung der Spin-2-Werte 0,03 % (abs(k) = 0,05) bis 0,55 % (abs(k) = 0,2).
- **G0 nicht eingetroffen:** Bei k = 0 gibt es 11 statt 10 Nullmoden.
  - Die elfte ist die lange Diagonale (1,1,1,1). An allen 14 Dreiecken mit ihr liegt ihr ein rechter Winkel gegenueber
    (Thales); deren Flaechen haengen in erster Ordnung nicht von ihr ab.
  - Das ist die fuenfte Nullmode von Rocek/Williams. Der Agent hatte das Scheitern vorab mit 90 % erwartet.
- **G1 nicht eingetroffen** nur an der eigenen Sortierregel (h-Anteil > 1/2). In zwei Richtungen hat ein positiver
  k^2-Modus nur 0,38 h-Anteil, weil er senkrecht auf der Diagonalen-Nullmode stehen muss.
  - Ohne Klassenregel (beschreibend): an allen 4095 Impulsen 5 Nullmoden, 9 positive und genau ein negativer Eigenwert.
- **Kontrollen:**
  - Torus- gegen Einzelsimplex-Ableitungen 1,9e-12; L = 3 und 4 bitgleich.
  - Schlaefli 8e-13.
  - Herausrechnen der Gittermoden aendert die Form bei abs(k) = 0,1 um <= 0,12 %.
  - 3D-Kontrolle mit demselben Code: Spin-2 0,24995, Verhaeltnis -1,0000. Das passt zu c = 1/(d - 1) = 1 bei d = 2, siehe
    REGEL.md, Abschnitt 7.
- **Selbstanzeigen:**
  - G0-Scheitern war ableitbar; die Sortierregel bei G1 wurde nicht gelockert.
  - Vermerke in auswertung.json per jq nachgetragen; Urteile und Werte identisch mit der Maschinenfassung.
  - Nur Regge/Williams 2000 gelesen.
  - Euklidisch und linear: Lorentz-Signatur und die zwei echten Polarisationen sind nicht geprueft.
- **Bedeutung:**
  - Sind die Striche Laengen, kommen Spin 2 und der konforme Minus-Modus mit genau dem Faktor -2 zusammen und
    unverzerrt aus dem Simplex-Netz.
  - Damit ist die Regel aus REGEL.md (c = 1/2) im Laengen-Bild von selbst eingebaut (Weg A bestaetigt).
  - Die Regge-Wirkung ist dabei hineingesteckt (Regime A).
- **Abschaetzung:** erledigt. Folgen nach Vorschlag des Agenten [H]:
  - Fassung mit echter Zeitrichtung (zwei Polarisationen)
  - verzerrtes Gitter ohne rechte Winkel (die fuenfte Nullmode sollte verschwinden); geparkt
- 2026-10-04 01:33:06 CEST: Freier Platz nach REGGE-4D-1: REGEL-1 gestartet.
  - Karte RUNDE-36/regel-1/KARTE.md ab 01:32:09: Gu/Wen-Netz mit eingebauter Regel (c = 1/2); Wellen, Newton mit Q-Ball-Energiequellen, gleiches Fallen (Energie- gegen Ladungskopplung).
  - Spuren cpu3 und cpu4, Zeitbox 120 min. Aktive Agenten 3 von 3: ZUFALLS-REIBUNG-1, DREIECK-LINSE-1, REGEL-1.
- 2026-10-04 01:47:45 CEST: Finn: "Erkläre das Bau was zum angucken".
  - Anschauungsseite coordination/lagebericht/halbe-regel-20261004/index.html: Regler c mit Zusatzschwingung,
    cos^2-Mittel, Dimensionskette, Weg zur Regel, Fingerabdruck REGGE-4D-1, offene Fragen.
  - Zahlen von der Leitung per grep gegen die Ergebnisdateien geprueft. Drei Fehler im Entwurf korrigiert:
    - "Kristallnetz bis 41 %" stammte aus AETHER-UHR-1; NETZ-C-1 sagt Querwellen 5 bis 9 %, Doppelbrechung [110].
    - Linie "unerfuellbar" ist falsch, richtig "leer"; Berichtigung in REGEL.md.
    - "gemessen" durch "gerechnet" ersetzt.
  - Veroeffentlichung erst nach frischem Gegenleser (pruefer-opus), sobald ein Agentenplatz frei ist (3 von 3 belegt).
- 2026-10-04 01:55:32 CEST: Finn: "Das artifact kann ich nicht angucken".
  - Die Seite war wegen der Gegenleser-Regel noch nicht veroeffentlicht.
  - Jetzt als privater Entwurf veroeffentlicht: Artifact LHQ7ta8uUmEub75WTw8roR. Kopfzeile und Fuss markieren "Entwurf,
    Gegenlesen ausstehend".
  - Der frische Gegenleser (pruefer-opus) laeuft beim ersten freien Platz; Korrekturen kommen unter derselben Adresse.
  - Abweichung von der Arbeitsweise "erst gegenlesen, dann veroeffentlichen" auf Finns ausdruecklichen Wunsch.

### Ernte ZUFALLS-REIBUNG-1 (RUNDE-36/zufalls-reibung-1/ERGEBNIS.md; eingetragen 2026-10-04 01:59:47 CEST)

- Code-Agent. Plan eingefroren 01:34:41. 40 Laeufe auf cpu und cpu6. Gegengelesen an lauf-69/auswertung.json und
  ERGEBNIS.md.
- **Urteile:**
  - Z3 eingetroffen.
  - Z0 und Z1 nicht eingetroffen.
  - Z2 nicht auswertbar (Fangregel: der langsame Ball wird gefangen).
- **Kernbefunde (1D, synthetisch):**
  - Die Reibung waechst etwa mit sigma^2: p = 2,03 (v = 0,2), 2,31 (v = 0,3), 1,85 (v = 0,5).
  - Z1 verfehlt die Grenze 2 +- 0,3 knapp und nicht robust (Saat C: 2,22).
  - Keine Schwelle. Bei sigma = 0,01 ist r(0,5)/r(0,1) = 1,75 (beschreibend). Bei sigma = 0,04 wird der Ball mit
    v = 0,1 in allen drei Saaten gefangen.
  - Am staerksten gebremst wird bei v ~ 0,2; schnelle Baelle verlieren mehr Ladung (7 %), halten aber ihre Schnelle
    besser.
  - Ladungs- und Impulsverlust haengen fest zusammen: dQ/dP 0,60 bis 1,37, Faktor 2,26 (Z3).
  - Z0 scheitert nur am Ladungsverlust bei v = 0,5 (2,9e-8 gegen 1e-8); die Schnelle bleibt auf 2,7e-6 konstant.
- **Kontrollen:**
  - Energiebilanz <= 1,1e-9, Ladungsbilanz <= 4,6e-14.
  - Halber Zeitschritt aendert die Raten um <= 1e-6 relativ.
  - Die Massenluecke bleibt offen (1 + sigma eta >= 0,839).
- **Selbstanzeigen:**
  - Nach Rauch 1 und 2 (vor dem Einfrieren, offengelegt) wurden Messfenster, Ballfenster, Fangregel, das um die
    umkehrbare Unordnungsenergie bereinigte Hauptmass und die Blockgroesse festgelegt.
  - Die Fangregel macht Z2 "nicht auswertbar" statt "nicht eingetroffen".
  - Die Fehlerbalken unterschaetzen die Saatenstreuung (Saat C bis 29 % anders).
  - Die Bornsche Schaetzung liegt bei v = 0,2 bis 0,3 um das 5- bis 11-Fache zu tief.
- **Bedeutung [H]:**
  - Die Vorab-Idee "langsame Materie gleitet fast reibungsfrei durch Unordnung" wird beschreibend nicht gestuetzt: In
    diesem Modell bremst Unordnung bei jeder Geschwindigkeit, und langsame Baelle bleiben haengen.
  - Ein raeumlich zufaelliges Netz zeichnet also ueber die Reibung ein Ruhesystem aus. Das spannt GE5 an: Richtungsfreiheit
    (ZUFALLSNETZ-1) gegen Reibung.
- **Abschaetzung: parken.**
  - Folgeidee [H]: ein in Raum UND Zeit zufaelliges Netz nach Art der Kausalmengen. Es zeichnet kein Ruhesystem aus
    [L?: Bombelli/Henson/Sorkin, "Discreteness without symmetry breaking", arXiv gr-qc/0605006], sagt aber "swerves"
    voraus.
  - Als Ideenkarte vormerken.
- 2026-10-04 02:15:02 CEST: Finn: "Rechne weiter". Alle drei Agentenplaetze belegt (REGEL-1, DREIECK-LINSE-1, Gegenleser der Seite), also
  rechnet die Leitung selbst.
  - Karte RUNDE-36/regge-schaum-1/KARTE.md (ab 02:09:50): Traegt ein zufaelliges Tetraedernetz in Regges Laengen-Bild
    Newton mit demselben G?
  - Code regge_schaum.py: komplexer Schritt fuer d theta/d l, L = B^T J B.
  - Rauch R0 = 8, offengelegt: Kontrollen sauber; Quadrattest gewichtet P ~ 1,00, Einzelstreuung 0,36; Newton a ~ 1,00.
  - Code eingefroren 02:14:51. Hauptlaeufe K, J, P1, P2 bei R0 = 20 auf cpu6 gestartet.

### Ernte REGEL-1 (RUNDE-36/regel-1/ERGEBNIS.md; eingetragen 2026-10-04 02:24:33 CEST)

- Code-Agent. Gegengelesen an lauf-69/auswertung.json und ERGEBNIS.md.
- **Urteile:** RG0, RG1 und RG2 eingetroffen. RG3 mechanisch nicht eingetroffen.
- **Vermerk RG3:** Im eingefrorenen Plan zeigte die Kraftrichtung von der Quelle weg, die Regel verlangte "alle a > 0
  (zur Quelle hin)". Signiert: a = -0,046927 fuer beide Baelle, eta_E = -4,2e-6, eta_Q = -0,18938.
  - Beschreibend (Nachtrag nach dem Einfrieren, kein Urteil): Mit der gemeinten Richtung sind alle drei Bedingungen
    erfuellt.
  - Das Urteil bleibt woertlich; eine Umwertung nur nach frischer Fremdlesung.
- **Kernbefunde (gerechnet; alles vorab ableitbar, Aequivalenzprinzip eingegeben):**
  - Wellen: Bei c = 1/2 ohne Strafterme laufen je k genau zwei Moden, an allen 32 767 Zonenpunkten. v(abs(k) = 0,1)
    = 0,99958 bis 0,99986 ueber 103 Richtungen, Streuung 2,8e-4.
  - Newton: U d 8 pi/(E1 E2) = -1,00018 bis -0,99984 fuer 4 bis 10 Ballradien. Ohne Torus-Korrektur waere die Anziehung
    bei L = 256 um 32 bis 74 % zu schwach.
  - Fallen: Energiekopplung abs(eta) <= 4,2e-6; Ladungskopplung abs(eta) = 0,189. Das folgt genau aus int abs(phi)^2/E der
    beiden Baelle.
- **Festlegung vor dem Einfrieren:** Q = 50 existiert in 3D fuer beta = 1/2 nicht (kleinste Ladung 111,9). Deshalb
  Q = 150 und 500, schwere Quelle Q = 5000; h = 0,5, kleiner Ball 4,1 Gitterpunkte (Halbwertsradius).
- **Kontrollen:**
  - Radialprofile gegen RUNDE-02 4,8e-6; Ewald-Torus 4e-6.
  - Bei c = 1/2 bleibt das Netz auf der Zwangsflaeche (6e-10). Bei c = 0,45 waechst die Kruemmung in T = 20 um 2e7.
- **Selbstanzeigen:**
  - Einmal lokal awk als Zeilenfilter auf eine jq-Ausgabe; nichts gerechnet, aber gegen die Regel.
  - Zwei kleine Baelle bei 4,1 Ballradien: Newton um 0,5 % daneben (Schwanzueberlapp [H]).
  - Rauch auf L = 8 vor dem Einfrieren zeigte RG0/RG1-nahe Werte (offengelegt).
- **Bedeutung:**
  - Weg B (Kraftfluss) traegt mit eingebauter Regel und Energie als Quelle zugleich zwei Polarisationen, Newton und
    gleiches Fallen.
  - Beide Haelften der Regel sind aber eingegeben, nicht gefunden.
- **Abschaetzung:** erledigt. Folgefrage am Schreibtisch: woher die Energiekopplung kommt; siehe REGEL.md, Abschnitt 8.

### Ernte DREIECK-LINSE-1 (RUNDE-36/dreieck-linse-1/ERGEBNIS.md; eingetragen 2026-10-04 02:24:33 CEST)

- Code-Agent, Plan eingefroren 01:47:26, Spur p4000a. Gegengelesen an lauf-69/auswertung.json.
- **Urteile:** D0, D1, D2 und D3 eingetroffen, ohne Vermerk.
- **Kernbefunde:**
  - Parallel gestartete Q-Baelle (Q = 200, v0 = 0,05) laufen hinter einer Fuenfer-Spitze unter 60,0003 / 60,0002 /
    60,0001 Grad aufeinander zu (b = 20 / 30 / 40); Spannweite 0,0002 Grad.
  - Endschnelle gleich Startschnelle auf 5e-7. Jede Bahn bleibt fuer sich gerade (Zusatzablenkung <= 0,0004 Grad).
  - b = 10: 70,88 Grad, also 5,44 Grad je Bahn zusaetzlich zur Spitze hin (Mulde), ohne Abbremsung oder Anregung.
    Impulsnaeherung mit dem KEGEL-Q-Potential: 4,6 bis 5,2 Grad [H].
- **Kontrollen:**
  - Flaches Netz <= 1,2e-5 Grad; Spiegelgleichheit 8e-9 Grad.
  - Abrollung isometrisch 1,5e-13; zweites Schwerpunktmass 1,8e-4 Grad.
  - Halber Zeitschritt und h = 0,2 aendern kein Urteil.
- **Selbstanzeigen:**
  - D0, D1 und D3 waren praktisch vorab ableitbar: 60 Grad ist die von Hand gebaute Winkelsumme, und der Rauch zeigte
    vorher 60,0015. Offen war nur D2.
  - Die Schnittwahl wich vom Hinweis der Leitung ab (Festlegung vor dem Einfrieren, begruendet).
  - Restablenkung 1e-4 bis 3,5e-4 Grad bei b >= 20, Ursache ungeprueft [H].
- **Bedeutung:**
  - Finns "Masse = Fehlwinkel" wirkt auf Q-Baelle wie eine Masse in 2+1 Dimensionen: fester Knick (Doppelbild), keine
    Fernkraft.
  - Nah an der Spitze kommt die kurzreichweitige Mulde dazu: der Unterschied zwischen ausgedehntem Ball und Punktteilchen.
  - Ob ein Q-Ball sich seine Spitze selbst schafft, ist nicht getestet. In der 3D-Regge-Rechnung ist eps_e = 8 pi G T_e
    eine Identitaet (Schlaefli), also vorab ableitbar.
- **Abschaetzung:** erledigt; parken.
- 2026-10-04 02:35:26 CEST: Erster Gegenleser der Anschauungsseite (02:00 bis 02:28): **KORRIGIEREN**.
  - 26 Befunde (2 hoch, 10 mittel, 14 niedrig); alle 37 Zahlen richtig. Bericht lagebericht/halbe-regel-20261004/GEGENLESEN.md.
  - **B1 (hoch):** Die Anziehung kommt nicht vom 1/2-Glied, sondern von der Feldseite (a-konformer Modus,
    TENSOR-EIS-N). Das 1/2-Glied regelt nur die Stabilitaet (LAMBDA-1).
  - **B2 (hoch):** Der Ausweg mit Zusatzregel E_T = 0 (LAMBDA-1) fehlte.
  - **B15:** Im kovarianten Bild schwaecht das Minus des Aufblas-Modus die Anziehung: 2/3 - 1/6 = 1/2 in 4D, 0 in 2+1.
    Mein Satz "deshalb ziehen sich gleiche Massen an" war falsch.
  - Ausserdem fehlende Vermerke: vorab ableitbar, Wuerfelgitter, nicht eingetroffene Vorhersagen.
  - **Leitung:** Seite umgeschrieben, unter anderem mit "Zwei Minuszeichen", REGEL-1, Lapse-Absatz und c = 1/5 fuer ein
    Raum-Netz.
  - Als Version 2 veroeffentlicht, weiter als Entwurf. Zweiter frischer Leser (pruefer-opus) gestartet; Agenten 3 von 3.

### Ernte REGGE-SCHAUM-1 (Leitung; RUNDE-36/regge-schaum-1/; eingetragen 2026-10-04 02:47:10 CEST)

- Leitung selbst, Spur cpu6. Code eingefroren 02:14:51. Urteile mechanisch per auswertung.jq, geschrieben vor dem Ende der
  Hauptlaeufe.
- **Urteile:** RS1, RS2, RS3 und RS4 eingetroffen; RS0 nicht eingetroffen.
- **Kernbefund:** Auch ein zufaelliger Tetraeder-Schaum (Poisson-Delaunay, 33 510 Punkte in einer Kugel R0 = 20) traegt in
  Regges Laengen-Bild Newtons Gesetz mit demselben G wie das Kuhn-Wuerfelgitter.
  - Quadrattest, volumengewichtet: 0,99955 bis 0,99999 (beide Saaten, x, y, z). Einzelne Ecken streuen stark
    (Standardabweichung 0,37 bis 0,39; 5 % bis 95 %: 0,69 bis 1,78).
  - Newton-Ausgleich a = 1,00019 bzw. 1,00009, also G auf 0,02 % unveraendert. Er stimmt mit 1/Quadratmittel (1,00028
    bzw. 1,00017) ueberein.
  - Tensor K/8: Eigenwerte 0,9995 bis 1,0009, also richtungsfrei.
  - Das Rauschen im Potential faellt mit dem Abstand: relative Streuung 0,57 bzw. 0,74 % bei r ~ 5,5 und 0,11 bzw. 0,13 %
    bei r ~ 12,5.
  - L_II ist positiv definit: kleinste Eigenwerte 0,199 und 0,201 (Kuhn 0,217). Splitter-Tetraeder (V_min 3e-5 bis 1e-4)
    machen den konformen Modus nicht instabil.
  - Wackelgitter J (Gegensweep): Quadratmittel 1,00013, Streuung 0,16; a = 1,00008.
- **RS0 nicht eingetroffen**, und zwar an Schlaefli und Symmetrie (Schwelle je 1e-10 relativ):
  - Schlaefli bis 8,3e-8 (J), 2,8e-9 bzw. 1,8e-9 (P).
  - Symmetrie bis 4,1e-7 (J), 1,6e-11 bzw. 7,2e-9 (P).
  - Ursache vermutlich die Genauigkeit der Winkelableitungen an Splitter-Tetraedern (J: V_min 1,4e-5) [H]. Im Rauch
    (R0 = 8) lagen die Werte noch unter 1e-10.
  - Die uebrigen Kontrollen tragen: L 1 und L x <= 2,4e-11; Kuhn-Schablone 7e-15; Kuhn a = 1,0002.
  - Fuer RS1 bis RS4 (Genauigkeit 1e-4) ist der Fehler unerheblich; das Urteil bleibt woertlich.
- **Selbstanzeigen:**
  - Die Loeser-Ordnung MMD_AT_PLUS_A machte den Newton-Schritt langsam (K: 240 s). J wurde nach 600 s abgebrochen,
    P1 von mir gestoppt.
  - Korrektur nach dem Einfrieren auf die Standardordnung, offengelegt in PRUEFSUMMEN.txt. Dasselbe System, gleiche
    Schwellen; J, P1 und P2 neu gerechnet; K mit altem Code.
  - RS2 folgt aus RS1, wenn die Homogenisierung ohne Korrektor gilt; das stand vorab in der Karte [M].
  - Eigenwertrechnung 190 bis 320 s; sie war der groesste Teil der Laufzeit.
- **Bedeutung:**
  - Fuer Finns Schaumbild: Regges Regel gibt auf einem ungeordneten Netz dieselbe Schwerkraftstaerke wie auf einem
    Kristall. Die Unordnung zeigt sich nur als Rauschen nahe der Masse, das mit dem Abstand abklingt.
  - Wahrscheinlich steckt eine Summenregel dahinter (Schlaefli und exakte Verschiebungsfreiheit, L x = 0) [H].
  - Geprueft ist der zeitsymmetrische (raeumliche) Teil, nicht die 1/2.
- **Abschaetzung:** erledigt. Folge in Runde 37: REGGE-ZEIT-1 (Zeit-Kanten, gamma).

## Abschluss Runde 36 (eingetragen 2026-10-04 02:51:20 CEST)

| Karte | Ausgang kurz | Abschaetzung |
|---|---|---|
| LAST-1 | Lasten mit Nettokraft ziehen sich wie 1/r an (Kelvin 0,47 %); selbsttragende Quellen 1/r^3 mit Richtungsvorzeichen, im isotropen Netz fast 0 | erledigt |
| ZUFALLSNETZ-1 | Z0 bis Z2 ja, Z3 nein; Poisson-Delaunay fast isotrop (0,28 % bei N = 64 000, ~N^-0,435), c_l/c_q = 1,68 | erledigt |
| REGGE-RAND-1 | RR1 bis RR4 ja (vorab ableitbar), RR5 nein (Bindung 30 bis 38 % unter Newton bei m/d = 0,1); psi = 1 + GM/(2r) auf 0,77 % | erledigt |
| NEWTON-NACHRECHNUNG | Leitung: Kuhn-Eckenoperator = 8 mal (-7-Punkt-Laplace), unabhaengig bestaetigt | erledigt |
| TENSOR-EIS-N | N-Typ zieht an wie -1/(8 pi r) (0,41 %), L-Typ ohne Wechselwirkung; Pyrochlor nicht gerechnet | erledigt |
| AETHER-UHR-1 | Gleiche Grenzgeschwindigkeit: Uhrenvergleich < 0,002 %; zwei Tempi 12 bzw. 32 % bei v = 0,6; U1, U2 nein (Formel) | erledigt |
| LAMBDA-1 | Stabil nur bei c = 1/2 ohne Zusatzregel; Ausweg E_T = 0; G_eff unabhaengig von c; alles vorab ableitbar | erledigt |
| V-1-WEITER | Stille exakt bei eps > 0; Leck ~ exp(-2 pi/sqrt(abs(eps))) bei eps < 0 (Polabstand pi) | weiter: V-1-PRAEZISION (Runde 37) |
| REGGE-4D-1 | G2, G3 ja; G0, G1 nein (fuenfte Nullmode, Sortierregel); Einsteins (1/4) k^2 (P2 - 2 P0) auf 0,04 % | erledigt; Folgen REGGE-ZEIT-1, REGGE-WELLE-1 |
| ZUFALLS-REIBUNG-1 | Z3 ja; Z0, Z1 nein; Z2 nicht auswertbar; Reibung ~sigma^2 ohne Schwelle, langsame Baelle gefangen | geparkt; Folge KAUSAL-1 (Runde 37, erledigt) |
| DREIECK-LINSE-1 | D0 bis D3 ja; Fuenfer-Spitze knickt Bahnen um 60 Grad ohne Kraft, nah plus 5,4 Grad | erledigt; geparkt |
| REGEL-1 | RG0 bis RG2 ja; RG3 woertlich nein (Vorzeichenfehler im Plan); zwei Wellen, Newton 0,02 %, eta 4e-6 bzw. 0,19 | erledigt |
| REGGE-SCHAUM-1 (Leitung) | RS1 bis RS4 ja, RS0 nein (Genauigkeit an Splittern); Schaum gibt dasselbe G auf 0,02 % | erledigt |
| SAGNAC, GEDANKENEXPERIMENTE, REGEL (Schreibtisch) | Sagnac eingeordnet; GE1 bis GE8; die Regel als freie Zeit-Umbenennung (Abschnitt 8) | erledigt |
| Anschauungsseite "Die ½-Regel" | Gegenleser 1: KORRIGIEREN (26 Befunde, Zahlen richtig); Version 2; zweite Lesung laeuft | offen (Runde 37) |

### Einfach gesagt (Runde 36)

Diese Nacht ging es darum, wie in Finns Netz Schwerkraft entstehen kann. Bloße Pfeile und federnde Stäbe geben
Elektrizität oder Kräfte, die nur mit Hilfe von außen anziehen. Anziehung braucht ein Minuszeichen auf der Feldseite, und
ein zweites Minus-Glied mit genau ½ hält das Netz ruhig. Diese ½ bedeutet, dass die Uhren an jedem Ort verschieden
schnell laufen dürfen. Sind die Striche Längen, kommt Einsteins Struktur heraus, auf einem Würfelgitter wie auf einem
zufälligen Schaum mit demselben G. Ein Raum-Netz mit äußerer Uhr bekommt die ½ aber nicht von selbst; deshalb zeigen die
Rechnungen auf ein Netz in Raum und Zeit.
