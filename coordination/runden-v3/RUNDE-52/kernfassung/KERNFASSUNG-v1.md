# KERNFASSUNG v1: Das verbindliche Modellblatt (Runde 52, Schritt 1 des Codex-Plans)

- Synthese-Agent fuer die Leitung claude-primary. Arbeitsbeginn 2026-10-10 02:15:47 CEST (date), Text ab 02:22:06 CEST
  (date). Nur Schreibtisch: keine Rechnung, kein Lauf.
- Grundlage: codex-gesamtreview/REVIEW.md (Abschn. 2, 3, 5, 6), BERICHTIGUNG-NACH-CODEX-REVIEW.md, GESAMTMODELL-ENTWURF-v2,
  LOOP-REVIEW-20261009, EMERGENZ-INVENTUR, RUNDE-50/GRUNDGLEICHUNG-v3, RUNDE-49/GR-PRUEFLISTE-v2, die ERGEBNIS-Dateien
  in RUNDE-52, S301-AUDIT und T2/T2B/T2C/T2D, review-response-20261008/RESPONSE.md, oeffentliche README/RESULTS.
- Kennzeichen: [E] im Projekt gerechnet, [M] vorab ableitbar, [L] Literatur aus dem Gedaechtnis, [S] an der Quelle
  gelesen, [H] Hypothese bzw. Vorschlag dieses Agenten, **[W]** Modellwahl (gesetzt, nicht hergeleitet).
- Status: **Entwurf zur Entscheidung durch Finn** (Abschn. 4). Bis dahin gilt: Positive Befunde beziehen sich nur auf
  die Fassung, in der sie gerechnet wurden (Spalte "Fassung" in Abschn. 2).
- **Offen: REGGE-ZWANG-CODEX.md lag bei Abschluss nicht vor.** Die Zwangsbedingung der neuen Kante steht deshalb
  unten ausdruecklich als Modellwahl (F1), nicht als Folge der Regge-Wirkung.

## 1. Das Modellblatt (Kernfassung K, Vorschlag)

| Feld | Kernfassung K | Herkunft im Projekt |
|---|---|---|
| **Freiheitsgrade** | Kantenlaengen l_e des raeumlichen Netzes (Geometrie); Lapse N_v und Shift als Multiplikatoren je Ecke; U(1)-Kantenfeld A_e mit konjugiertem elektrischen Fluss; ein komplexer Skalar phi_v auf den Ecken. Alles klassisch. | GRUNDGLEICHUNG-v3 Abschn. 2/3 [W] |
| **Raumdimension** | 3, periodisch; Netz V (10 Ecken, 68 Kanten, 116 Dreiecke, 58 Tetraeder je Zelle), gefuellt, Potenzgewichte in der Kammer. S nur als Vergleichsnetz. Die 3 ist eingesetzt, nicht entstanden. | REGULAER-V-1, PRISMA-MAXWELL-1 [W] |
| **Zeit und Wirkung** | **Stetige Zeit, Hamiltonform** (Grenzfall Zeltstange h -> 0 der 4D-Zeltwirkung): H = Summe_v N_v H_v + Shift-Terme + H_Licht + H_Skalar. Potential = 3D-Regge-Form B; Traegheit M_eff aus der 4D-Wirkung. Licht: DEC-Maxwell auf V, elektrische Energie mit \*1, magnetische mit \*2 (Kogut-Susskind-Form). | GRUNDGLEICHUNG-v3 Abschn. 3; UEBERLEITUNG-V-1/-2 [E]; IDEE-07 [M] |
| Zelt und Prisma | Das **Zeltnetz** dient nur zur Herleitung von M_eff und Lapse; ein endlicher Takt ist nicht Kern (instabil fuer grosse h; GW170817 verlangt h/h0 < 3e-8 [ES]). Das **Prisma V x Z** ist die euklidische Kontrollfassung fuer Positivitaet und Reflexionspositivitaet. Die Monte-Carlo-Befunde (QUANT-2/-3) laufen auf dem Zeltnetz mit gesuchten Gewichten, also in einer **anderen Fassung**. | REGIME-K-3, PRISMA-MAXWELL-1, QUANT-2 [E] |
| **Mass / Quantisierung** | **Keine fuer K.** Es gibt kein Mass fuer Geometrie oder Gewichte. Quantisiert ist nur Eichfeld bzw. Skalar auf festem Hintergrund (Zelt, QUANT-1/-2/-3). Reflexionspositivitaet ungeprueft. | RESULTS Befunde 3 bis 5 |
| **Zwangsbedingungen** | (Z1) Eckenregel R1 ueber den Lapse (Multiplikator); (Z2) Gauss je Ecke (U(1)); (Z3) **globale Volumenbedingung** [W, unimodular]; (Z4) **Kantenbedingung**: die beim 2-3-Zug neu erzeugte Laenge wird festgehalten. Z4 ist **zusaetzliche Zwangsdynamik, Modellwahl** (F1); Dittrich/Hoehn legitimieren sie nicht. Z3/Z4 gelten nur, wenn Umklappen zugelassen ist (Erweiterung K+U, Abschn. 3). | KANTEN-TEST-1, KANTEN-DYN-1/2/3, VOLUMEN-G2-1 [E]; BERICHTIGUNG F1 |
| **Parameter** | Gesetzt: Netz V, Topologie, Dimension, Eichgruppe U(1), metrische Kopplung von Licht und Skalar, Skalarpotential (Q-Ball). **Frei:** die Potenzgewichte (L = 1: Fd-3m 2, F-43m 3 Parameter; allgemeiner mehr), die physikalische Kantenlaenge a (nur Schranke), Kopplung e, Skalarparameter, Orientierung des Netzes gegen den Himmel (3 Winkel). **Die Gewichte sind frei**: das E0-Minimum ist kein Prinzip (GEWICHTSFELD-2, T-1 nicht bestanden; BERICHTIGUNG F5). Arbeitsbezug: Kammermitte bzw. Handpunkt (-23/7; -32/7) (a/8)^2. | GEWICHTSPRINZIP-1, GEWICHTSFELD-1/-2 [E] |
| **Physikalische Zeit** | Die Eigenzeit der gemeinsamen Zeltstangen (Lapse); Licht, Skalar und Schwerewellen benutzen dieselbe Uhr. Daraus c_Licht = c_GW bei kl -> 0 [M, folgt aus dem Aufbau]. Euklidische Operatoren (Rohrgang-Transfer, Prisma-Q) sind **keine** physikalische Zeitentwicklung. | LICHT-GLEICHE-UHR [E, M] |
| **Messgroessen** | (a) Dispersion omega(k, Polarisation) von Licht, Skalar und Schwerewelle aus dem **verallgemeinerten** Eigenproblem (Masse \*1 bzw. M_eff), F9; (b) statisches Fernfeld: Takt, Laengen, Lichtablenkung, Shapiro, PPN gamma/beta; (c) Stabilitaet (Zahl negativer omega^2 auf dem physikalischen Raum W); (d) Schranke an a aus (a) gegen Daten. Keine Teilchenmassen, kein PDG-Vergleich in K. | HOEHE-ISOTROP-1, LICHT-ABLENKUNG-V, BETA-NETZ-V, T2/T2C [E] |

- Kurzform von K: **klassische Regge-Maxwell-Skalar-Hamiltonform auf festem V, stetige Zeit, freie Gewichte, freie
  Skala.** Das ist die Architektur von McDonald/Miller 2010 [laut RESULTS-Kopf] auf einem bestimmten Netz. Eigen sind
  die Rechnungen auf V, nicht die Architektur.

## 2. Kernaussagen nach Beweisstand

Spalten nach Codex Abschn. 3 getrennt: **Herkunft** (ein = mikroskopisch eingesetzt, koll = kollektiv gewonnen);
**Begruendung** (eingesetzt / hergeleitet [M] / gerechnet [E]); **Spezifitaet** (Klasse = gilt fuer die Modellklasse,
V = haengt an V bzw. Gewichten, Diskr = haengt an der Diskretisierung); **Physikalischer Status** (unabh. reproduziert?
skalenkontrolliert? pruefbar?). "Unabhaengig reproduziert" ist **in keiner Zeile erfuellt**: Bitgleiche Kontrollen
zwischen Karten benutzen denselben Code; REPRODUCIBILITY.md (oeffentlich) beansprucht ausdruecklich keine unabhaengige
Nachrechnung.

| Nr | Aussage (Fassung) | Herkunft | Begruendung | Spezifitaet | Physikalischer Status / offen |
|---|---|---|---|---|---|
| 1 | c = 1 langwellig fuer Licht und Skalar; c_Licht = c_GW (K) | ein (gemeinsame Uhr, Divergenzsatz) | [M], [E] 1e-10 | Klasse | Konsistenz; keine Skala noetig. Nicht unabh. reproduziert |
| 2 | Maxwell-Form auf V bzw. V x Z positiv auf dem Nicht-Eich-Raum (K, Prisma) | ein (W > 0) | [M] algebraisch + Kohomologie [L]; [E] 15378 Punkte | V-Kammer | Lipschitz-Zertifikat gescheitert; **Reflexionspositivitaet offen** (F9) |
| 3 | Licht und Skalar bei (ka)^2: isotroper Teil < 0 (subluminal), l = 4-Teil beta_M > 0, Doppelbrechung D (K, DEC auf V) | koll (Gitter) | [E] HOEHE-ISOTROP-1, GEWICHTSPRINZIP-1 (2131 Punkte, Stichprobe) | **V + Gewichte** | Gewichtsabhaengige Familie, keine Vorhersage; "nie isotrop" nur Stichprobe (F2). Physikalische Frequenz aus dem verallgemeinerten Problem (\*1) [M]. Kandidat der Entscheidungsfrage |
| 4 | Schwerewellen richtungsgleich und ohne wachsende Mode, linear (K, stetig) | koll | [E] UEBERLEITUNG-V-2 | V und S, nicht B1 | nur linear um flach; nicht gegengelesen nach Codex |
| 5 | M_eff hat 10 negative Richtungen je k, auf W positiv (K) | koll | [E] T2B; [M] Sylvester | V | Eigenvektoren keine reinen Zwangsrichtungen (bis 0,36 rad); (kl)^2-Rest bricht Kubik (T2), Ursache vermutet |
| 6 | Fernfeld: gamma = 1, Lichtablenkung, Shapiro (K, statisch, linear) | ein (Eichung) / koll | gamma [M] Identitaet; Ablenkung [M] + [E] | Klasse | Kontrolle, keine Vorhersage; Nahfeld < 1,5 Gitterlaengen gewichtsabhaengig |
| 7 | PPN beta = 0,95 +- 0,05 (Variante B), keine Bahn (K, statisch) | koll | [E] BETA-NETZ-V, ohne Karte | Klasse (Regge -> ART [L]) | **Keine Bahnintegration** (S301-AUDIT); Konvergenz nicht gezeigt |
| 8 | Umklapp-Instabilitaet sitzt auf der Laenge der neuen Kante (K+U) | koll (Mechanismus der Rechenvorschrift) | [E] KANTEN-TEST-1 (79 bis 86 %) | Diskr | echter Befund der gewaehlten Dynamik |
| 9 | Kantenbedingung beseitigt sie bei A = 1e-3 (K+U) | **ein** (Z4) | [E] KANTEN-DYN-1/3 | Diskr | **F3:** nur s4 war instabil; bei A = 1e-2 scheitern alle 4 unbedingt, 3 von 4 bedingt (s2 bis 2,0 T, Sprung 0,134). Zweiter Mechanismus (entartete Tetraeder) offen; Kurzfenster, keine nichtlineare Stabilitaet |
| 10 | Volumenbedingung stabilisiert 3 von 4 Netzen (K+U) | **ein** (Z3) | [E] VOLUMEN-G2-1 | Diskr | Zwangskraft 30 bis 88 % der Netzkraft |
| 11 | Kompaktes U(1): Coulomb-Phase, E/abs(k) = 1,01 +- 0,04 (Zelt, MC) | U(1) ein; Phase koll | [E] QUANT-2, L = 2, 3 | Klasse (L-uni) | andere Fassung (Zelt, gesuchte Gewichte); nur "vereinbar mit" masselos/isotrop (F13) |
| 12 | SU(2): Einschluss, Flow-Verhaeltnisse wie Hyperkubus (Zelt, MC) | SU(2) ein | [E] QUANT-3, zwei Abstaende | Klasse | Universalitaetszuordnung, kein Netzbefund |
| 13 | Gewichtsminimum der Nullpunktenergie (K, L = 1) | koll | [E] GF-1; **T-1 gescheitert** (GF-2) | Diskr (Regulator) | **zurueckgenommen** als Prinzip; beta_M/beta_S = 0,815 nur eng bedingt |
| 14 | "Optische Zitter-Mode" (K) | koll | [E] T2C/T2D | V | **F4:** nur hoher Rayleigh-Quotient belegt, keine Eigenmode |
| 15 | Q-Baelle, keine kleinen gebundenen Zustaende (Skalar, MC) | Potential ein | [E] QUANT-1 | Klasse | kleine Netze; keine Teilchen |

- Berichtigt gegenueber GESAMTMODELL-ENTWURF-v2 (alte Datei bleibt unveraendert): F1 (Zeile 9, Z4), F2 (Zeile 3), F3
  (Zeile 9), F4 (Zeile 14), F5 (Zeile 13), F9 (Zeilen 2, 3), F13 (Zeile 11).

## 3. Kern und geparkte Varianten

- **Zum Kern K gehoeren:** Abschn. 1 auf festem V. **Erweiterung K+U** (Umklappen mit Z3, Z4) ist ein klar benannter
  Zusatz und kein Teil der Ableitung aus K, solange REGGE-ZWANG-CODEX nicht zeigt, was die Wirkung beim Zug selbst
  verlangt. Zeltnetz und Prisma sind Hilfsfassungen (Abschn. 1).
- **Geparkt** (keine neuen Karten ohne Finns Freigabe; vorhandene Befunde behalten ihre Herkunft):

| Variante | Warum geparkt | Was sie wieder oeffnen wuerde |
|---|---|---|
| Rohrgang (Fermion-Laeufer, Spinor-Transport) | Spinor-Lift eingesetzt; euklidisch, nicht-hermitesch; Dublett nur bedingtes Spektralergebnis; keine Spin-Statistik (F7) | Schritt 5 des Codex-Plans: genau ein Teilchenmechanismus mit Zustand, Strom, Zeitentwicklung |
| psi-Varianten L/K | je Sektor nur Drehung bzw. axiales U(1)-Feld; keine Haendigkeitswahl | wie oben |
| Chirale Kopplung, Domaenenwand (Kaplan) | Chiralitaet am nicht-unitaeren Schritt; Domaenenwand waere gesetzt | Teilchenmechanismus positiv abgeschlossen |
| Gewichtsfeld (Gewichte als dynamisches Feld) | E0-Minimum ist Regulatorbefund (GF-2); weder Wirkung noch Mass fuer Gewichte | Finn-Entscheidung F2 unten: Gewichte als physikalische Variable mit eigener Wirkung und Mass |
| Mindestvolumen / fruehes Umklappen | neue Naturregel aus numerischem Scheitern (F10) | nur als explizite Variante mit eigenem diskriminierendem Test |
| KK-Ring (Radion, Deconstruction) | minimale Kreisvariante analytisch eingeschraenkt; Sinusleiter ableitbar | neue Geometrie mit eigener Skala und Test |
| Brueckenspannung (BRUECKE-1) | Ruhelaengen-Zusatzmodell; langwellig wirkungslos | Datenbezug fehlt |
| Jessen-Flip, Schaum, Kugelzaehlung | Geometrie-Werkzeuge; Schnittzahl ist keine Entropie (F12) | nur als Methode |
| SU(3), Skyrme, Higgsportal | Bausteine ohne Uebergang zu Teilchen (Codex Abschn. 5) | nach Schritt 5 |

## 4. Entscheidungen fuer Finn (hoechstens 5)

1. **Welche Zeit traegt den Kern?** (A) stetige Hamiltonform auf V, Zelt nur zur Herleitung, Prisma als euklidische
   Kontrolle [Vorschlag]; (B) Prisma V x Z mit endlichem tau als Kern (positiv, aber Kopplung an Regge-Zelte offen);
   (C) Zeltnetz mit endlichem Takt (dann QUANT-2/-3 im Kern, aber negative Gewichte und Taktinstabilitaet).
2. **Was sind die Gewichte?** (A) freie Parameter der Modellfamilie; Aussagen nur als Familie mit Ausschlussbereichen
   [Vorschlag]; (B) physikalisches Feld, dann vorher Wirkung und Mass festlegen (neuer Strang, F5); (C) per Konvention
   auf einen Punkt fixieren (Kammermitte), nur fuer Reproduzierbarkeit, ausdruecklich ohne physikalischen Anspruch.
3. **Gehoert Umklappen zum Kern?** (A) nein: K auf festem V, K+U geparkt bis REGGE-ZWANG-CODEX vorliegt [Vorschlag];
   (B) ja, mit Z3 und Z4 als ausgewiesenen Modellwahlen; (C) ja, aber nur mit den Prae-/Postbedingungen, die Codex aus
   der Wirkung ableitet (Z4 entfaellt, falls sie nicht folgt).
4. **Welcher Lichtsektor?** (A) DEC-Maxwell auf V (doppelbrechend bei (ka)^2, gewichtsabhaengig) [Vorschlag, weil darauf
   alle K-Rechnungen beruhen]; (B) Fluss-Eis M-D auf dem Diamant-Teil (doppelbrechungsfrei, feste Zahlen, aber anderer
   Operator); (C) beide als getrennte Varianten mit je eigener Entscheidungsfrage. Diese Wahl entscheidet die
   Entscheidungsfrage (ENTSCHEIDUNGSFRAGE-v1.md, Abschn. 4).
5. **Physikalische Skala a?** (A) frei, nur Schranken aus Daten [Vorschlag]; (B) a = Planck-Laenge setzen; dann sind
   alle bekannten Netzeffekte unbeobachtbar und das Datenziel laeuft nur ueber Kontinuumskonsistenz; (C) a aus einer
   Kopplung bestimmen (G oder alpha); dafuer gibt es heute keinen Mechanismus.

## Einfach gesagt

Bisher wurden Ergebnisse an leicht verschiedenen Modellen gewonnen: mal mit Zeitschritten als Zelte, mal als Prismen,
mal mit Zusatzregeln. Dieses Blatt legt eine einzige Fassung fest: Finns Netz V im Raum, eine stetige Zeit, Schwerkraft,
Licht und ein Materiefeld auf demselben Netz. Die Gewichte des Netzes und seine wahre Groesse sind darin frei. Die Tabelle
zeigt ehrlich, was eingebaut, was abgeleitet und was nur gerechnet ist; unabhaengig nachgerechnet ist noch nichts.
Finn muss fuenf Weichen stellen, vor allem, welche Zeit und welches Licht zum Kern gehoeren.

---
Abgabe: siehe naechste Zeile (date).
Abgabe: 2026-10-10 02:24:53 CEST (date). REGGE-ZWANG-CODEX.md bei Abgabe: vorhanden
