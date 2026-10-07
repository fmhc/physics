Urteil: weitergabefaehig nach den A-Befunden. 2 A-, 3 B- und 11 C-Befunde. A1 bis A3 und B1 bis B7 des dritten Lesers sind umgesetzt, nur B5 teilweise. Zu stark sind der Kontinuumssatz "keine ruhende Lage mit Materie" auf dem Modell-Torus (A1) und die unimodulare Zeit als Scheibungs-Alternative bzw. "Uhr fuer das ganze Netz" (A2).

# Vierter Leser: GRUNDGLEICHUNG-SKIZZE Fassung 2.3 (letzte Schicht)

- Beginn: 2026-10-05 12:41:48 CEST (date)
- Ende: 2026-10-05 12:59:32 CEST (T=$(date +%H:%M:%S)). Dauer 17 min 44 s, von Hand: 12:59:48 waeren 18 min, 12:59:32 liegt 16 s davor.
- sha256 von Fassung 2.3 bei Beginn und Ende gleich: bfa4b3a5b13d5036ebd63ca7ed593a9229aae90fce0a34033a743afa4a6e8b7b (246 Zeilen). Das Dokument ist nicht veraendert.
- Gelesen: RUNDE-49/GRUNDGLEICHUNG-SKIZZE-v2.3.md (vollstaendig), RUNDE-37/grundgleichung-v22-leser/BEFUNDE.md, diff gegen v2.2, Projektquellen laut Auftrag
- Rolle: frischer, unabhaengiger Leser; Anforderungen und Gegenfaelle, kein Vertragswortlaut. Rechenwege von Hand, Literatur aus dem Gedaechtnis als [L].

## 1. A-Befunde (falsch oder zu stark, muss geaendert werden)

Hier stehen nur Anforderungen. Den Wortlaut schreibt der Autor.

### A1 "Keine statische oder momentan ruhende Lage mit Materie auf dem Modell-Torus": Kontinuumssatz ohne Kennzeichen auf das Netz uebertragen, rho >= 0 fehlt (Abschnitt 5 Zeile 180; Abschnitt 0 Zeile 24)

- Zitate:
  - Z. 180: "**Auf dem Modell-Torus aus Abschnitt 1 mit Lambda = 0 gibt es nach dem T^3-Satz (Abschnitt 4) keine statische oder momentan ruhende Lage mit Materie.**"
  - Z. 24: "... und statische Lagen mit Materie gibt es auf dem Modell-Torus mit Lambda = 0 nicht (Abschnitt 5)."
- Begruendung:
  1. **Der Satz gilt fuer glatte Metriken.** Der T^3-Satz (Schoen/Yau, Gromov/Lawson) ist im Dokument selbst nur [L]. Der "Modell-Torus aus Abschnitt 1" ist aber ein stueckweise flaches Regge-Netz mit fester Delaunay-Zerlegung. Seine Hamilton-Bedingung bei p = 0 und Lambda = 0 lautet nach 2.2 je Ecke:
     - -(1/8 pi G) Summe_e w_ve l_e eps_e + H_v^Mat = 0, also Summe_e w_ve l_e eps_e = 8 pi G H_v^Mat.
     - Verlangt ist also, dass eine **gewichtete Eckensumme** der Fehlwinkel >= 0 ist. Dass jeder einzelne Fehlwinkel eps_e >= 0 ist, folgt daraus nicht.
     - Summiert ueber alle Ecken gilt Summe_v w_ve = 1/2 + 1/2 = 1, also Summe_e l_e eps_e = 8 pi G E_Mat > 0. Das allein verbietet nichts. Auch im Kontinuum ist ein positives Integral von sqrt(g) R auf T^3 erlaubt [M]: Mit g = u^4 g_flach gilt R_g u^5 = -8 Laplace u, also Integral R_g dV_g = -8 Integral u Laplace u = 8 Integral |grad u|^2 > 0. Verboten ist erst R >= 0 an jedem Punkt.
     - Ob nichtnegative Eckensummen auf einem Regge-T^3 Flachheit erzwingen, ist nirgends gezeigt.
     - Eine polyedrische Fassung des Satzes kenne ich nur fuer Kegelwinkel <= 2 pi an jeder einzelnen Kante, also eps_e >= 0 [L, Li/Mantoulidis 2019, unsicher]. Diese Bedingung stellt das Modell nicht.
  2. **Das Dokument kennzeichnet die gleiche Uebertragung an anderer Stelle als Hypothese.** Abschnitt 4, Z. 146, sagt zum Lapse-Argument: "Diskret [H]: Dasselbe gilt, wenn ...". Hier steht die Uebertragung dagegen fett, ohne Kennzeichen und in Abschnitt 0 sogar als "Berichtigung".
  3. **Die Bedingung rho >= 0 fehlt.** Der T^3-Punkt in Abschnitt 4 (Z. 144) nennt sie, Z. 180 und Z. 24 nicht. Das Dokument fuehrt U < 0 selbst als eigenen Fall (Z. 145).
     - Wo U < 0 ist, kann rho = |phidot|^2 + |grad phi|^2 + U negativ werden. Dann gilt R = 16 pi G rho >= 0 nicht mehr, und der Satz greift nicht.
     - Fuer einen statischen Skalar gibt die integrierte Lapse-Gleichung (K = 0, Lambda = 0): Integral N (rho + S_T) = -2 Integral N U = 0. U muss also das Vorzeichen wechseln. Das schliesst im Dokument nichts aus.
- Anforderung:
  - Z. 180 und Z. 24 an das Kontinuum (T^3-Satz [L]) und an rho >= 0 binden (beim Q-Ball: U >= 0).
  - Fuer das diskrete Modell den Satz als [H] fuehren, wie in Z. 146. Alternativ die noetige diskrete Aussage als offen nennen: "nichtnegative gewichtete Eckensummen auf einem Regge-T^3 erzwingen Flachheit".
  - Dasselbe gilt fuer Z. 23, "K = 0 ist auf dem geschlossenen Torus nur in linearer Naeherung zulaessig": "im Kontinuum" ergaenzen. Die diskrete Fassung ist in Abschnitt 4 [H].

### A2 Unimodulare Zeit als "Alternative" zur Zeitscheibung und als "Uhr fuer das ganze Netz": Zaehler und Scheibung vermengt, Projektbezug zu stark (Abschnitt 4 Z. 157 bis 161; "Einfach gesagt" letzter Satz)

- Zitate:
  - Z. 158: "Sie waechst bei jeder Blaetterung mit N > 0, auch auf dem ruhenden Torus (Zuwachs Volumen mal Eigenzeit) [M]. Anders als die York-Zeit taugt sie dort als Uhr."
  - Z. 160: "WELTKRISTALL-L hat daraus "Finns Takt zaehlt Volumen" gelesen [P]."
  - Z. 246: "Als Uhr fuer das ganze Netz kommen zwei Kandidaten in Frage: ... oder das Zaehlen des vierdimensionalen Volumens; die zweite laeuft auch in einem ruhenden, geschlossenen Raum weiter."
- Was haelt (von Hand): Die Wachstumsaussage stimmt, wenn man Henneaux/Teitelboim zugrunde legt [L]. Es gilt d(Tau_U)/dt = Integral N sqrt(h) d^3x > 0 fuer N > 0. Auf dem ruhenden Torus mit N = const ist das N V. Der Preis "Lambda als Integrationskonstante" stimmt ebenfalls [L].
- Begruendung:
  1. **Zwei verschiedene Dinge.**
     - Die York-Zeit ist eine Scheibungsbedingung. K = tau legt fest, welche Scheibe "jetzt" ist; N folgt dann aus -Laplace N + W N = d tau/dt.
     - Die unimodulare Zeit ist in der Form des Dokuments (zu Lambda konjugiert, Zuwachs = 4-Volumen) eine einzige globale Zahl. Das Dokument sagt selbst, dass sie "bei jeder Blaetterung" waechst. Damit waehlt sie keine Blaetterung aus.
     - Rechenweg [M]: Man verschiebt eine Scheibe um delta t(x) entlang der Normalen. Dann aendert sich die Zahl um delta Tau_U = Integral delta t N sqrt(h). Nun waehlt man delta t > 0 im Gebiet A und delta t < 0 im Gebiet B, mit gleich grossen Beitraegen. Dann ist delta Tau_U = 0, obwohl die Scheibe eine andere ist.
     - Bei Henneaux/Teitelboim bleibt die Hamilton-Bedingung oertlich; nur ihr globaler Anteil wird zur Zeitgleichung [L, Henneaux/Teitelboim 1989; Unruh 1989]. Der Lapse bleibt also oertlich frei.
     - Folge: Alternative 2 ersetzt keine Scheibungsbedingung. Das Torus-Hindernis von K = 0 (die Lapse-Gleichung) beruehrt sie nicht.
  2. **"Uhr fuer das ganze Netz" heisst fuer Finn ein gemeinsames Jetzt.** Das liefert die York-Zeit, aber nicht die unimodulare Zeit allein. Fuer eine Scheibung braucht es eine Zusatzregel, z. B.:
     - Finns globaler Lapse N = const. Das ist in der ART die geodaetische Scheibung; mit Materie laeuft sie in Fokussierung bzw. Kaustiken [L].
     - Gleiches 4-Volumen je Zelle und Takt, also N_t V_t = const. Das entspricht der festen Volumenform nach Unruh [L], einem verdichteten Lapse. Es ist **nicht** der globale Lapse.
     - Keine der beiden Regeln steht im Dokument.
  3. **Projektbezug.** WELTKRISTALL-L (DOSSIER Z. 193 bis 195) fuehrt "Finns Takt zaehlt Volumen ... woertlich Gielen/Rieds unimodulare Zeit" als Schreibtisch [M, ES]. Die Aussage steht dort nur im Collins/Williams-Modell mit 600-Zellen-Schnitten, also homogen; die Scheibung gibt dort die Symmetrie vor.
     - Fuer ein ungleichmaessiges Netz bleibt genau die Scheibungsfrage offen.
     - Das Dokument fuehrt die Aussage als [P] und ohne diese Einschraenkung.
     - Die Aussagen zu Henneaux/Teitelboim sind [L], nicht [M, P].
     - "euklidisches Regge" stammt aus der Abstract-Zusammenfassung des Scouts (RUNDE-49.md Z. 69, [S Abstract]).
  4. **Der Vorteil "laeuft im ruhenden geschlossenen Raum weiter" betrifft den leeren, flachen Torus.** Nach dem Dokument selbst gibt es im Kontinuum mit Lambda = 0 und rho >= 0 keinen ruhenden Torus mit Materie. Auf dem leeren, flachen Torus zaehlen auch N = const und die Killing-Zeit. Tragfaehig ist der Vorteil fuer die linearen Rechnungen um diesen Hintergrund, und so sollte er dastehen.
- Anforderung:
  - In Alternative 2 sagen, dass die unimodulare Zeit zaehlt, aber keine Scheiben auswaehlt. Der Lapse bleibt oertlich frei [L]. Eine Scheibung braucht eine Zusatzregel; die Moeglichkeiten als [H] bzw. [L] nennen.
  - "Anders als die York-Zeit taugt sie dort als Uhr" auf das Zaehlen beschraenken, z. B. "als Zaehler".
  - Kennzeichen berichtigen:
    - Henneaux/Teitelboim: [L]
    - "euklidisch": [S Abstract, Scout]
    - WELTKRISTALL-L: [M, ES], nur im homogenen 600-Zellen-Modell
  - "Einfach gesagt": ein Halbsatz, dass die zweite Uhr zaehlt, aber nicht festlegt, welche Momente im ganzen Netz gleichzeitig sind. "Kommen in Frage" darf bleiben, mit "wird geprueft".
  - Abschnitt 7 ("die Entscheidung haengt an GIELEN-RIED-TIEF-L") entsprechend anpassen. Die Scheibungsfrage beantwortet eine Literaturkarte nicht allein.

## 2. B-Befunde (knapp)

- **B1 R gegen P: "umkehrbar" steht nur bei R (Abschnitt 6, Z. 194).**
  - Zitat: "R ist reihenfolgefest (bis 1,6e-13) und umkehrbar, verliert aber Energie ... P traegt im Impuls eine kleine Reihenfolgespur ... und gewinnt Energie".
  - Die Quelle sagt etwas anderes: "P: umkehrbar, gewinnt Energie" (UEBERGABE-KONFLUENZ-1 Z. 239) und "Die Impuls-Uebergabe (P) ist statisch umkehrbar" (Z. 227). Ihre Negativliste (Z. 298) haelt fest: "P ist umkehrbar und hat nur eine kleine Spur".
  - Gerechnet ist nur die statische Umkehr. "Nicht gerechnet: ... dynamische Zeitumkehr" (Z. 282).
  - Die dritte Bedingung, die symplektische Struktur, ist "fuer keine der beiden geprueft" (Z. 240).
  - Anforderung: "statisch umkehrbar" bei beiden nennen oder bei keiner. Einen Halbsatz ergaenzen, dass die Symplektik fuer beide ungeprueft ist.
- **B2 Skalar unter R: Die Umskalierung von pi verschwindet bei einem exakten Zug (Abschnitt 6, Z. 195) [M, Leser, nicht gegengelesen].**
  - Zitat: "In R wird pi_v mit *0'_v/*0_v umskaliert; das aendert die globale U(1)-Ladung und verletzt beim geladenen Skalar Gauss nach dem Zug. P erhaelt beides."
  - Das Dokument setzt in Z. 189 selbst: Das umkreisbasierte Dual einer Kante ist die Voronoi-Facette. Dann ist *0_v die Voronoi-Zelle von v. Sie haengt nur an den Eckenlagen, nicht an der Zerlegung.
  - Bei einem 2-3-Zug genau an der Kosphaerizitaet ("am Zug") ist die Bipyramide flach, und beide Zerlegungen sind Delaunay. Damit gilt *0'_v = *0_v.
  - Rechenweg in 2D, vier Punkte auf einem Kreis mit Mittelpunkt O:
    - Diagonale ac: Anteil von a = (a, m_ab, O, m_ac) vereinigt mit (a, m_ac, O, m_ad), also das Vieleck (a, m_ab, O, m_ad).
    - Diagonale bd: a liegt nur in abd, Anteil = (a, m_ab, O, m_ad).
    - Das ist dasselbe Vieleck. In 3D gilt das ebenso fuer die gemeinsame Umkugel.
  - Der Faktor *0'/*0 - 1 ist also proportional dazu, wie weit der Zug nach der Kosphaerizitaet ausgefuehrt wird. Bei 3-2-Zuegen kommt die Kruemmung der entfernten Kante hinzu.
  - Am exakten 2-3-Zug fallen R und P fuer den Skalar zusammen. Das Argument "P erhaelt Ladung" betrifft also den Ueberschuss im Zeitschritt bzw. gekruemmte 3-2-Zuege.
  - Die Quelle fuehrt die Ladungsaussage als "[M, nicht gerechnet]" (Z. 231). Im Dokument steht sie ohne Kennzeichen unter [P].
  - Anforderung: Kennzeichen [M, nicht gerechnet] setzen und die Groessenordnung (Ueberschuss bzw. Kruemmung) nennen. Die Abwaegung "je Sektor" entsprechend abschwaechen. Die Schlussfolgerung "Wahl offen" bleibt.
- **B3 SPLITTER-FREI-1 einseitig zusammengefasst (2.3, Z. 88).**
  - Zitat: "Splitter sind nicht die Ursache: Auf splitterarmem Glas bleiben A1RH 4 bis 7 und A2RH 4 bis 6 wachsende Moden je k".
  - Die Quelle setzt fett dagegen: "Aber die Zellform ist nicht gleichgueltig [E, H]" (ERGEBNIS Z. 246 bis 249):
    - A1RH faellt von 9 bis 10 auf 4 bis 7 (etwa -40 %), Lund-Regge mit R1 von 28 bis 33 auf 20 bis 24. Nur A2RH bleibt etwa gleich.
    - Im Nachtrag nach Sicht faellt A1RH bei q >= 0,25 auf 3.
  - Ohne die Ausgangszahl liest sich "bleiben 4 bis 7" wie "unveraendert".
  - Das Ergebnis traegt [E, ES] und wurde ohne frischen Leser geerntet (RUNDE-49.md Z. 72).
  - Anforderung: die Ausgangszahlen und den Halbsatz "die Zahl faellt mit besserer Zellform, verschwindet aber nicht" ergaenzen.

## 3. C-Befunde (knapp)

- **C1 (0, Z. 23):** "K = 0 ist ... nur in linearer Naeherung zulaessig" steht jetzt ohne Bedingung. In 2.2 hiess es noch "bei Lambda = 0 und W >= 0 ..., sonst nicht generisch".
  - Bei Lambda < 0 und rho + S_T < 0 an einer Stelle ist K = 0 nicht ausgeschlossen, nur nicht generisch. Abschnitt 4 nennt den Fall selbst (Z. 145).
  - Vorschlag: "(Lambda >= 0, rho >= 0; sonst nicht generisch)". Dazu "im Kontinuum" (A1).
- **C2 (6, Z. 194 bis 196):**
  - Die Zeile "Gueltigkeit: ... statische Paarprobe ..." gibt die Grenzen von UEBERGABE-KONFLUENZ-1 an. Die Energiezahlen stammen aber aus TAKT-DYNAMIK-1, einer dynamischen Bahn.
  - Bei -2,4 bis -12,7 % fehlt "A = 1e-3" (Quelle Z. 238).
  - Vorschlag: die Grenzen beider Karten getrennt nennen.
- **C3 (4, Z. 155):** "Wo W < 0 ist (rho + S_T < 0, siehe oben)": W kann auch durch Lambda > 0 negativ werden.
  - Auf CMC-Scheiben hilft K:K >= tau^2/3. Rechenweg: K:K = |K_spurfrei|^2 + K^2/3.
  - Vorschlag: "z. B." einfuegen oder Lambda > 0 nennen.
- **C4 (2.3, 5, 6):** "ohne frischen Leser" steht nur bei KRUEMMUNGS-SANDHAUFEN-2D-1. Ohne frischen Leser geerntet wurden laut RUNDE-49.md (Z. 43, 56, 72) auch UEBERGABE-KONFLUENZ-1, DANZER-TT-1 und SPLITTER-FREI-1.
- **C5 (B5 des dritten Lesers, Rest):**
  - K steht weiter fuer mehrere Dinge:
    - die Spur der aeusseren Kruemmung (laut Begriffen)
    - Steifigkeit in "1 bis 88 negative Richtungen von K auf der Eichung" (Z. 166, im selben Abschnitt wie K = 0)
    - "{K_v, H_w}" und "Regime K"
  - T steht fuer:
    - den Takt-Operator
    - die Zerlegung (Z. 29)
    - die Zeit in K = K(T)
    - den Spannungstensor T_ij
    - den Torus T^3
  - Vorschlag: mindestens in Abschnitt 4 eigene Zeichen fuer die Steifigkeit und fuer die Zeit verwenden.
- **C6 (5, Z. 177 f.):** "nur im offenen, asymptotisch flachen Raum" passt nicht zu "(bei Lambda ungleich 0 auch ueber den Lambda-Term)". Mit Lambda ungleich 0 ist ein Raum nicht asymptotisch flach. "bzw. als oertliche Bilanz" deckt den Fall zwar, aber ein Halbsatz wuerde ihn klarer machen.
- **C7 (4, Z. 151):**
  - Die Rechnung setzt voraus, dass das Potential an der Horava-Ecke das der ART ist, also N sqrt(g)(R - 2 Lambda), ohne a_i-Terme und ohne hoehere Ableitungen. Das steht nicht da; der dritte Leser hat es nur in seinen Selbstanzeigen erwaehnt.
  - Ich habe c und beide Klammern unabhaengig von Hand nachgerechnet (Abschnitt 5 hier). Das Kennzeichen "nicht gegengelesen" laesst sich auf "von einem zweiten Leser von Hand nachgerechnet" aendern.
- **C8 (Kopf, Z. 9):** Die Statuszeile nennt als neu nur A1 bis A3, B1 bis B7 und den Absatz zur unimodularen Zeit. Neu sind aber auch:
  - der SPLITTER-FREI-1-Satz in 2.3 (eine neue Ernte)
  - die Neufassung von DANZER-TT-1 (C8 des dritten Lesers)
  - die Aenderungen in den Abschnitten 7, 8 und 9
- **C9 (9, Nr. 4):** "Vorzeichen von rho + S_T" steht dort ohne Bindung an Lambda < 0, U < 0 oder CMC. Abschnitt 8 Nr. 6 bindet sie (B3 des dritten Lesers dort umgesetzt, hier nicht).
- **C10 (4, Z. 150):** "Belastbar ist die Gleichheit nur bei asymptotisch flachem Rand". Die Quelle (SKALAR-SEKTOR-L Z. 255 f.) schreibt "asymptotisch flache, isotrope Kontinuumsfaelle". "Isotrop" und "Kontinuum" fehlen. Fuers Netz verlangt die Quelle genau das: einen isotropen langwelligen Grenzfall und eine Gitter-H erster Klasse. Beides ist "auf dem gefuellten Netz nicht erfuellt" (Z. 103 f.).
- **C11 (4, Z. 148):** "In der vollen Theorie erzwingt schon eine kleine Welle N = 0".
  - Bei Lambda = 0 gibt es maximale Daten mit Welle nach dem T^3-Satz gar nicht, denn R = K:K >= 0.
  - Der Satz traegt erst bei Lambda < 0. Dann ist W = K:K + |Lambda| > 0, also N = 0.
  - Vorschlag: die Reihenfolge der Begruendung ordnen.

## 4. Umsetzung der Befunde des dritten Lesers (A1-A3, B1-B7)

| Befund | Stand | Begruendung (Reste hier) |
|---|---|---|
| A1 Torus-Schluss fuer "K = 0 als Gesetz" | umgesetzt | Randfreie Begruendung steht da (c, beide Klammern) und ist ehrlich als ungegengelesen markiert. Die Horava-Ecke auf geschlossenen Raeumen ist als CMC-Fall gefasst, die Gleichheit mit der ART dort als nicht belegt. Die Nullmoden sind offen genannt. Die Rechnung haelt von Hand (Abschnitt 5). Reste: C7, C10 |
| A2 "Lesart R bevorzugt" | umgesetzt | Abwaegung je Sektor, "Abwaegung der Leitung [H]", "Wahl offen". "Gar nicht uebergeben" ist auf phi beschraenkt, die Gueltigkeit genannt, R und P sind in den Begriffen erklaert, Abschnitt 9 Nr. 5 ist angepasst. Reste: B1 ("umkehrbar" nur bei R), B2 (Ladungsargument nur im Ueberschuss), C2 |
| A3 "beiden gerechneten Eckenregeln" | umgesetzt | "zwei von drei ..., unter der dritten nur vereinzelt". Das passt zu Abschnitt 4 ("eine Mode auf einem von vier Glasnetzen"). Abschnitt 0 ist neu gefasst |
| B1 statische Beispiele auf dem Modell-Torus | umgesetzt, dabei neu ueberdehnt | Die Beispiele sind als "offen, asymptotisch flach bzw. oertlich" markiert, der Satz zum Modell-Torus ist ergaenzt, das "Einfach gesagt" auf "im offenen Raum" eingeschraenkt. Neu zu stark: Kontinuumssatz ohne [H] aufs Netz, rho >= 0 fehlt (A1 hier). Das rho >= 0 fehlte schon in der Anforderung des dritten Lesers; in seiner Begruendung stand es |
| B2 Vorzeichen des Lambda-Terms | umgesetzt | dH/dq_e und Kraft stehen getrennt, in der Kraft -(Lambda/8 pi G)(dV/dl_e)/(2 l_e). Von Hand nachgerechnet (Abschnitt 5) |
| B3 rho + S_T gegen T^3-Satz ordnen | umgesetzt | Im T^3-Satz steht "gleich welches Vorzeichen rho + S_T hat". Der Punkt "Wo das Vorzeichen zaehlt" nennt Lambda < 0, U < 0 und CMC. Abschnitt 8 Nr. 6 ist gebunden. Reste: C1, C9 |
| B4 Tempo auf dem Weg ueber Z_s | umgesetzt | Auf beiden Wegen ist das Tempo Wurzel 8, sie unterscheiden sich nur in der Compton-Laenge. Nachgerechnet: omega^2 = N0^2 (Z_s k^2 + U'(0))/Z_t |
| B5 Zeichen S und K | teilweise | Sh, S, S_T und "Netz S" sind getrennt, die Mindestforderung (S_T in Abschnitt 4) ist erfuellt. K und T sind weiter mehrfach belegt (C5) |
| B6 "nur eine Paarung" | umgesetzt | Zwei Paarungen (A1R1, A2R1), "in den gerechneten Spektren", fehlende Positivitaet auf der Eichung, in Abschnitt 0 und 4 |
| B7 Evidenzart KRUEMMUNGS-SANDHAUFEN-2D-1 | umgesetzt | "ohne frischen Leser", "grobe Verzweigungszahl ~1 im Endzustand ist ein Nachtrag nach Sicht" |

- Die C-Befunde des dritten Lesers C1 bis C10 finde ich alle aufgenommen. C11 verlangte keine Aenderung.
- Abschnitt 0 nennt "B- und C-Befunde ... weitgehend". Das ist zutreffend und eher bescheiden.

## 5. Handpruefungen (Rechenwege)

- **T^3-Satz und Folgerungen (4, Z. 144):**
  - Die Hamilton-Bedingung lautet R + K^2 - K:K = 16 pi G rho + 2 Lambda. Mit K = 0 wird daraus R = K:K + 16 pi G rho + 2 Lambda.
  - Bei Lambda = 0 und rho >= 0 ist R >= 0. Dann ist die Metrik flach [L], also R = 0. Daraus folgt K:K = 0 und rho = 0: flach, ruhend und leer. Das Vorzeichen von rho + S_T geht nicht ein. Stimmt.
  - Bei Lambda > 0 ist R >= 2 Lambda > 0 auf T^3 unmoeglich. Stimmt.
- **Integralargument (Z. 143):**
  - Aus Laplace N = W N folgt Integral N Laplace N = -Integral |grad N|^2 = Integral W N^2.
  - Bei W >= 0 sind beide Seiten 0. Also ist N konstant, und wegen N^2 Integral W = 0 mit Integral W > 0 folgt N = 0. Stimmt; die Bedingung "Lambda = 0" ist zu Recht entfallen, weil W den Lambda-Term enthaelt.
- **rho + S_T (Z. 145):**
  - Mit T_mn = 2 Re(d_m phi* d_n phi) + g_mn L und L = |phidot|^2 - |grad phi|^2 - U gilt:
    - rho = 2|phidot|^2 - L = |phidot|^2 + |grad phi|^2 + U
    - S_T = 2|grad phi|^2 + 3L = 3|phidot|^2 - |grad phi|^2 - 3U
    - Summe: 4|phidot|^2 - 2U
  - Q-Ball-Schwanz: (4 omega^2 - 2 m^2) f^2 < 0 genau dann, wenn omega^2 < m^2/2. Stimmt.
- **CMC-Kriterium (Z. 155):**
  - Ist der kleinste Eigenwert lambda_1 von -Laplace + W positiv, dann ist die Inverse positivitaetserhaltend. Aus d tau/dt > 0 folgt dann N > 0.
  - Rayleigh-Quotient: (Integral |grad u|^2 + W u^2)/Integral u^2 ist bei W >= 0 immer >= 0. Null wird er nur fuer u = const mit Integral W = 0. Bei W >= 0, nicht ueberall 0, ist also lambda_1 > 0. Stimmt (Rest C3).
- **"K = 0 als Gesetz", c und Klammern (Z. 151), unabhaengig nachgerechnet:**
  - Ausgangspunkt: pi^ij = sqrt g (K^ij - lambda g^ij K) und tr pi = sqrt g (1 - 3 lambda) K.
  - Einsetzen: K:K - lambda K^2 = pi:pi/g + 2 lambda K tr pi/sqrt g + (3 lambda^2 - lambda) K^2.
    - Mit K tr pi/sqrt g = (1 - 3 lambda) K^2 wird der K^2-Koeffizient 2 lambda - 6 lambda^2 + 3 lambda^2 - lambda = lambda (1 - 3 lambda).
    - Ergebnis: pi:pi/g + lambda (tr pi)^2/(g (1 - 3 lambda)).
  - Hamiltonsche Spurzahl lambda/(3 lambda - 1); bei lambda = 1 ist das 1/2. Differenz zur ART: 1/2 - lambda/(3 lambda - 1) = (3 lambda - 1 - 2 lambda)/(2 (3 lambda - 1)) = (lambda - 1)/(2 (3 lambda - 1)). Stimmt.
  - Klammer mit F = Integral N c (tr pi)^2/sqrt g:
    - Bausteine: d(tr pi)/d g_kl = pi^kl, d(tr pi)/d pi^kl = g_kl, dF/d pi^kl = 2 N c tr pi g_kl/sqrt g, dF/d g_kl = N c [2 tr pi pi^kl - (1/2)(tr pi)^2 g^kl]/sqrt g.
    - Ergebnis: {tr pi, F} = 2Nc (tr pi)^2/sqrt g - 2Nc (tr pi)^2/sqrt g + (3/2) Nc (tr pi)^2/sqrt g = (3/2) N c (tr pi)^2/sqrt g. Das verschwindet auf tr pi = 0.
    - {tr pi(x), tr pi(y)} = tr pi delta - tr pi delta = 0.
    - Die Beitraege des c-Terms zu gdot und pidot tragen den Faktor tr pi. Die Bewegung auf tr pi = 0 ist also die der ART in maximaler Scheibung. Stimmt (Annahme C7).
- **Unimodulare Zeit (Z. 158):**
  - d(Tau_U)/dt = Integral N sqrt h > 0 fuer N > 0. Auf dem ruhenden Torus ist das N V. Stimmt (Kategorie: A2).
  - Gegenbeispiel zur Scheibung: Unter delta t(x) aendert sich die Zahl um Integral delta t N sqrt h. Bei gegenlaeufigen Verschiebungen gleichen Gewichts ist der Zuwachs 0, obwohl die Scheibe eine andere ist.
- **Kantenkraft (5, Z. 173):**
  - H_Kr = -(1/8 pi G) Summe_e N_e l_e eps_e mit N_e = Summe_v w_ve N_v. Bei N = 1 gilt nach Schlaefli dH_Kr/dl_e = -eps_e/(8 pi G), also dH_Kr/dq_e = -eps_e/(16 pi G l_e), weil dq = 2 l dl.
  - H_Lambda = (Lambda/8 pi G) Summe_t V_t gibt (Lambda/8 pi G)(dV/dl_e)/(2 l_e).
  - Kraft = -dH/dq_e. Beide Vorzeichen stimmen.
  - Ungleiches N: d/dl_e Summe N_e' l_e' eps_e' = N_e eps_e + Summe (N_e' - N_ref) l_e' d eps_e'/d l_e, weil Summe l_e' d eps_e'/d l_e = 0. Stimmt.
- **Projektzahlen gegen Quellen:**

| Stelle | Dokument | Quelle | Ergebnis |
|---|---|---|---|
| 6 | R reihenfolgefest bis 1,6e-13 | UK-1 Z. 59 f. (Delta_p <= 1,6e-13, Delta_q <= 3,0e-14) | stimmt |
| 6 | P: disjunkt bis 2,8e-7, insgesamt bis 1,3e-5 | UK-1 Z. 69 bis 71, 93 (D-Maximum 2,76e-7) | stimmt |
| 6 | R: -2,4 bis -12,7 % ueber 10 Perioden | UK-1 Z. 237 f. (TAKT-DYNAMIK-1, A = 1e-3) | stimmt, A fehlt (C2) |
| 6 | P: +15 bis +20 % | UK-1 Z. 239 | stimmt |
| 6 | "R ... umkehrbar" | UK-1 Z. 226 f., 239, 298: beide statisch umkehrbar | einseitig (B1) |
| 6 | Ladung und Gauss unter R | UK-1 Z. 231 bis 235 "[M, nicht gerechnet]" | Kennzeichen fehlt (B2) |
| 6 | Gueltigkeit | UK-1 Z. 251 bis 257 | stimmt fuer UK-1 (C2) |
| 2.3 | A1RH 4 bis 7, A2RH 4 bis 6 je k | SF Z. 63 bis 65, 83 | stimmt; Ausgangszahlen fehlen (B3) |
| 2.3 | nicht an den schlechtesten Zellen | SF Z. 59 bis 62, 82 (f hoechstens 0,383, Median 0,169) | stimmt |
| 4 | Horava-Ecke = CMC, lambda wirkt, belastbar nur asymptotisch flach | SKALAR-SEKTOR-L Z. 52 f., 64 bis 66, 115 f., 255 f. | stimmt; "isotrop, Kontinuum" fehlt (C10) |
| 4 | Gielen/Ried: euklidisches Regge, 4-Volumen | RUNDE-49.md Z. 69 [S Abstract, Scout]; WELTKRISTALL-L Z. 185 bis 192 [S] | stimmt als Abstract (A2) |
| 4 | WELTKRISTALL-L: "Finns Takt zaehlt Volumen" | WELTKRISTALL-L Z. 193 bis 195 [M, ES], Collins/Williams-Modell | Kennzeichen [P] zu stark, Einschraenkung fehlt (A2) |
| 4 | waechst auch auf dem ruhenden Torus | RUNDE-49.md Z. 80 (Vorab [M] der Leitung) | stimmt |

## 6. Urteil

**An Finn weitergabefaehig: ja nach den A-Befunden.**

- Die A-Befunde, B1 bis B7 des dritten Lesers und die neuen Rechnungen sind umgesetzt bzw. halten von Hand (T^3-Folgerungen, rho + S_T, CMC-Kriterium, c und Klammern, Kantenkraft mit Lambda, Tempo der zwei Wege). B5 ist nur teilweise umgesetzt. Die Projektzahlen in 2.3, 4 und 6 stimmen mit den Quellen.
- Zu aendern sind zwei Stellen, beide nur im Wortlaut, ohne Neubau:
  - A1: Der Satz "keine statische oder momentan ruhende Lage mit Materie" bezieht sich auf den Modell-Torus, also das Regge-Netz. Belegt ist er nur im Kontinuum ([L]) und nur mit rho >= 0. Er steht in Abschnitt 5 und in Abschnitt 0.
  - A2: Die unimodulare Zeit ist ein Zaehler, keine Scheibungsbedingung. Als "Alternative" zur Zeitscheibung und als "Uhr fuer das ganze Netz" ist sie zu stark gefasst; der Projektbezug zu WELTKRISTALL-L ist als [P] statt [M, ES] gekennzeichnet und nicht auf das homogene Modell eingeschraenkt.
- Abschnitt 0 und "Einfach gesagt" sind sonst nicht staerker als der Text. Ausnahmen: Z. 24 (A1), Z. 23 (C1) und der letzte Satz des "Einfach gesagt" (A2).
- B1 bis B3 (R gegen P, Skalar unter R, SPLITTER-FREI-1) sollten mit erledigt werden. Keiner aendert eine Schlussfolgerung des Dokuments; "Wahl offen" bleibt.

## 7. Selbstanzeigen

- **Auftrag:** Eine BRIEF-Datei mit Pfad und sha256 wurde nicht genannt. Grundlage ist der Auftrag der Leitung in der Nachricht, woertlich befolgt.
- **Reihenfolge:** Vor dem Anlegen der Ausgabedatei liefen zwei lesende Befehle (date fuer die Beginnzeit; ls auf RUNDE-37 und RUNDE-49, um den Ordner zu pruefen).
- **Werkzeuge:**
  - Benutzt: date, ls, wc, sha256sum (mit cut), diff, grep, sed -n (alle lesend) und Read.
  - Geschrieben habe ich nur diese Datei (Write, Edit); der Ordner entstand beim ersten Write.
  - Nicht benutzt: Interpreter, awk, ssh, git, Peerbus, Journal, Unteragenten.
- **grep:** Alle greps liefen auf einzeln benannte Dateien (Fassung 2.3, UEBERGABE-KONFLUENZ-1, SPLITTER-FREI-1, SKALAR-SEKTOR-L, WELTKRISTALL-L), keiner ueber einen Projektordner. Die Pflicht-Ausschluesse waren deshalb nicht noetig.
- **Ordnernamen:** `ls -la` auf RUNDE-37 (erste 80 Zeilen) zeigte Namen anderer Karten- und Leserordner, u. a. grundgleichung-v2-, -v21-, -v22-leser und gielen-ried-tief-l. Geoeffnet habe ich nur die im Auftrag genannten Dateien. Fassung 2.1 habe ich nicht geoeffnet. Einen parallelen Pruefer kenne ich nicht.
- **Lesetiefe:**
  - Vollstaendig gelesen: Fassung 2.3 (246 Zeilen), die BEFUNDE des dritten Lesers, das diff 2.2 gegen 2.3 und RUNDE-49.md (91 Zeilen; darin auch die Protokollzeilen zum Start dieses Lesers).
  - Nur per grep und in Ausschnitten gelesen:
    - UEBERGABE-KONFLUENZ-1: Z. 220 bis 259
    - SPLITTER-FREI-1: Z. 237 bis 296
    - SKALAR-SEKTOR-L: Z. 100 bis 106, 218 bis 224
    - WELTKRISTALL-L: Z. 28 bis 41, 180 bis 207
- **Nicht selbst geprueft:**
  - Codex' Gegenblick (Stand der Codex-Punkte in Abschnitt 0)
  - die A-Befunde des ersten und zweiten Lesers ("alle A-Befunde der drei Leser")
  - TAKT-DYNAMIK-1, HODGE-MASSE-1, LUND-REGGE-MASSE-1 und DANZER-TT-1 (nur ueber RUNDE-49.md bzw. den dritten Leser)
  - die Arbeit von Gielen/Ried selbst
  - der Code
- **Literatur aus dem Gedaechtnis [L], an keiner Quelle geprueft:**
  - Schoen/Yau und Gromov/Lawson
  - Li/Mantoulidis 2019 (unsicher, ob genau so)
  - Henneaux/Teitelboim 1989 und Unruh 1989 (oertliche Hamilton-Bedingung, feste Volumenform)
  - Kaustiken der geodaetischen Scheibung
  - die konforme Transformation in 3D
  - die Form der Horava-Wirkung
- **Eigene Rechnungen [M], ungegengelesen:**
  - A1: positives Integral von R bei konformer Verformung, Eckensummen
  - A2: verschobene Scheibe mit gleichem 4-Volumen
  - B2: Stetigkeit von *0 am exakten Zug; in 2D ausgerechnet, in 3D nur ueber die gemeinsame Umkugel uebertragen
  - C3 und C11
- **Einordnung:**
  - B2 koennte als A gelten: Bestaetigt, nimmt es der Abwaegung R gegen P das Skalar-Bein. Ich habe B gewaehlt, weil "Wahl offen" stehen bleibt und weder Abschnitt 0 noch das "Einfach gesagt" darauf bauen.
  - A1 koennte als B gelten: Schon die Anforderung des dritten Lesers sprach vom Modell aus Abschnitt 1 und liess rho >= 0 weg. Ich habe A gewaehlt, weil der Satz eine fette, absolute "keine"-Aussage ueber das Modell ist, in Abschnitt 0 als Berichtigung steht und gegen die eigene [H]-Regel des Dokuments (Z. 146) verstoesst.
- **Zeiten:** Alle Uhrzeiten stammen aus date. Gemessen: Beginn 12:41:48; Zwischenstaende 12:42:21, 12:48:19, 12:49:47, 12:50:03, 12:54:28 und 12:57:15. Die Zwischenzeiten habe ich direkt per `date '+%H:%M:%S'` abgelesen; nur die Endzeit stammt aus T=$(date +%H:%M:%S).
