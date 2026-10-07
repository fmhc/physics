Urteil: weitergabefaehig nach den A-Befunden. 5 A-, 14 B-, 9 C-Befunde. Neue Rechnungen in 2.3, 3.1, 3.2, 4 und 5 halten von Hand; zu stark sind Einarbeitungsstand, "R1 stabil", York-Zeit, Folge in Abschnitt 5 und das "Einfach gesagt".

# Blinde Zweitmeinung zu GRUNDGLEICHUNG-SKIZZE Fassung 2.1

- Pruefgegenstand: /home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-49/GRUNDGLEICHUNG-SKIZZE-v2.1.md
- sha256 beim Lesebeginn: aed2d07b8a490aa5a52347b4a2d7ac61260d1a288f28c63a20598743d8475276 (22543 Byte, 233 Zeilen)
- Start: 05.10.2026 11:47:53 CEST (per date gemessen)
- Ende: 05.10.2026 12:11:24 CEST (per date gemessen; Dauer 23 min 31 s = 12:11:24 - 11:47:53)
- Leser: frischer Claude-Leser, blind; nur Papier und Kopf, keine Rechnerrechnung
- Literatur aus dem Gedaechtnis ist mit [L] gekennzeichnet.

## 0. Lesestand

- Nach 11:47:59 (date): Fassung 2.1 vollstaendig gelesen (233 Zeilen), danach Leser-BEFUNDE zu Fassung 2 vollstaendig (442 Zeilen) und Codex-Gegenblick vollstaendig (80 Zeilen).
- Keine BRIEF-Datei mit sha256 genannt; Grundlage ist die Nachricht der Leitung, woertlich befolgt.
- Danach, bis 12:04:51 (date): Quellen nachgeschlagen: HODGE-MASSE-1/ERGEBNIS.md Abschnitte 2 bis 4.4; LUND-REGGE-MASSE-1/ERGEBNIS.md Abschnitte 2, 4.4, 5.1, 5.2; RUNDE-48.md Zeilen 408 bis 517 und per grep (Friedman, Bahr, DANZER-NAEHERUNG-2). Fassung 2 nicht geoeffnet. Nach dem Lesen von 2.1 sah ich nur eine grep-Zeile daraus (Bahr, Zeile 80); ihre uebrigen Wortlaute kenne ich nur aus den Zitaten der Leser-BEFUNDE.
- Kennzeichen hier: [M] von mir von Hand gerechnet (Rechenwege in Abschnitt 8), [P] Projektdatei mit Fundstelle, [L] Gedaechtnis, ungeprueft.

## 1. A-Befunde (sachlich falsch oder zu stark, muss geaendert werden)

Anforderungen an den Wortlaut; formulieren muss der Autor.

### A1 Einarbeitungsstand meldet die Spurbindung als erledigt (Abschnitt 0)

- Zitate:
  - "Punkt 1 ist teilweise eingearbeitet: Shift-Interpolation (Abschnitt 1) und Spurbindung (2.2) ja."
  - "Leser und Codex zu Fassung 2: alle sieben A-Befunde eingearbeitet"
- Begruendung:
  - 2.2 sagt selbst "Bindung im Code [P, mit Vorbehalt]" und "Am Code zu bestaetigen (Leser B8)". Abschnitt 8 fuehrt unter "Offen" Nr. 2 "Spurbindung am Code bestaetigen". Abschnitt 0 widerspricht also 2.2 und 8.
  - Codex (Gegenblick v2, Punkt 3) verlangt vor jedem Vergleich den Abgleich von Variablen, Volumenfaktoren, Koeffizienten und Constraints. Benannt ist bisher nur die Kette A2_t K_t = 1, nichts davon am Code.
  - "alle sieben eingearbeitet": A5 und A7 sind nur teilweise umgesetzt, A6 gerade wegen dieses Satzes (Tabelle Abschnitt 4; hier A4, A5).
- Anforderung: Abschnitt 0 nennt die Spurbindung als "Kette benannt, am Code offen". Je A-Befund steht dort der wirkliche Stand oder ein Verweis auf die Restpunkte.

### A2 "R1 stabil, RH nicht" widerspricht den eigenen Zahlen in 2.3 (Abschnitt 4, Energie)

- Zitat: "Die Stabilitaetstests pruefen das Vorzeichen der quadratischen reduzierten Energie fuer zwei Reduktionen. Sie widersprechen sich (R1 stabil, RH nicht)."
- Begruendung [P]:
  - 2.3 desselben Dokuments: "B mit R1 ... Bei grossem k waechst es (V an 142 von 511 k), auf Glas an jedem k (27 bis 33 Moden)". Quelle LUND-REGGE-MASSE-1 Tab. 4.4: wachsend an 142 (V), 28 (S), 12 (A15) von 511 k. HODGE-MASSE-1 Tab. 4.2 A2LR1: Glas neg 28 / 31 / 33 / 28.
  - Ohne wachsende Moden ist also nicht "R1", sondern nur die Paarung A1R1 bzw. A2R1. Mit der Literaturform B wachsen Moden unter R1 und unter RH.
  - Gerechnet wurden drei Reduktionen, nicht zwei (R2 = A2LR2 in Tab. 4.2).
  - Auch fuer A1R1 und A2R1 fehlt die vertikale Positivitaet: 1 bis 88 negative Richtungen von K auf der Eichung (HODGE-MASSE-1 Abschnitt 2 Punkt 5, Tab. 4.3).
- Anforderung: Stabilitaet an die Paarung binden, nicht an die Reduktion. B unter R1 und RH instabil nennen (unter R2 eine Mode auf Glas s2) und den Vorbehalt der vertikalen Positivitaet erwaehnen.

### A3 York-Zeit als "globale Zeitfunktion auf geschlossenen Raeumen" (Abschnitt 4, "Fuer Finns Takt-Bild")

- Zitat: "Kandidat fuer mehr ist die York-Zeit, eine globale Zeitfunktion auf geschlossenen Raeumen."
- Begruendung [M, R9 in Abschnitt 8; L]:
  - Die York-Zeit tau = K ist nur dann eine Zeit, wenn tau sich von Scheibe zu Scheibe aendert.
  - Auf einer statischen Raumzeit mit geschlossenen Scheiben ist jede geschlossene CMC-Flaeche maximal (tau = 0), sofern Ric(n,n) >= 0 gilt. Das zeigt das Killing-Argument in R9.
  - Gerade auf dem ruhenden flachen Torus, dem Hintergrund der in 2.3 und 6 genannten Netzrechnungen, ist tau also konstant null und keine Zeit.
  - Zusaetzlich [L, Schoen/Yau 1979; Gromov/Lawson 1980]: T^3 traegt keine Metrik mit R >= 0 ausser der flachen. Mit Lambda = 0, rho >= 0 und K = 0 gibt die Hamilton-Bedingung R = K:K + 16 pi G rho >= 0. Maximale Daten auf T^3 sind dann schon flach, ruhend und leer.
  - Dass es eine CMC-Blaetterung gibt, ist auf geschlossenen Raeumen nicht allgemein gesichert, sondern ein Satz mit Voraussetzungen [L, Marsden/Tipler; Gerhardt; Andersson/Moncrief].
  - Das "Einfach gesagt" deutet die Bedingung an ("waechst oder schrumpft"), Abschnitt 4 nicht.
- Anforderung:
  - Die Bedingung nennen: Das Volumen muss sich aendern, tau darf nicht konstant sein. Auf dem ruhenden flachen Torus gibt es keine York-Zeit.
  - Die Folge fuer das Netz nennen: Die York-Zeit verlangt einen sich ausdehnenden oder schrumpfenden Hintergrund, also einen Wechsel gegenueber den in 2.3 und 6 genannten Rechnungen.
  - Die Existenz als [L] mit Voraussetzungen kennzeichnen.

### A4 Die "Folge" in Abschnitt 5 gilt nur statisch; das Staub-Beispiel ist nicht statisch

- Zitate:
  - "Beispiele: ... ruhender Staub hat Kruemmung ohne Spannung."
  - "Folge: Erst Fehlwinkel, Lapse-Term (Uhrengefaelle) und Materiespannung zusammen ergeben die diskrete Einsteingleichung. Der Schwerkraft-Anteil steckt also im ungleichen Gang der Uhren."
- Begruendung:
  - (a) Die Kantengleichung lautet pdot_e = -dH_tot/dq_e. Bei p ungleich 0 tragen der Bewegungsanteil (Form A oder B, quadratisch in p) und pdot selbst bei. Nur bei p = 0 und pdot = 0 (statisch) bleiben die drei genannten Terme uebrig. Codex (Gegenblick v2, Punkt 4) verlangte ausdruecklich, den vollen gewichteten Hamiltonian "einschliesslich kinetischer und Materieterme" zu variieren. Die "Folge" steht als eigener Punkt ohne das "ruhend" des Punkts davor und liest sich allgemein.
  - (b) Der Lambda-Term aus dem ersten Punkt von Abschnitt 5 fehlt in der Aufzaehlung.
  - (c) Ruhender Staub ist nicht statisch [M, R10]. Er hat Kruemmung ohne Spannung. Die Kantengleichung schliesst dort aber ueber pdot ungleich 0, denn der Staub beginnt zu fallen. Als Gegenbeispiel zu "Kruemmung = Spannung" taugt er, als Beispiel fuer die "Folge" nicht.
  - (d) Die Kantengleichung ist der ij-Teil. Die Hamilton-Bedingung H_v = 0 (Kruemmung gegen Energiedichte) ist eine eigene Gleichung. "die diskrete Einsteingleichung" sagt mehr.
  - (e) "Der Schwerkraft-Anteil steckt also im ungleichen Gang der Uhren" ist die bekannte Lesart des Newton-Grenzfalls [L]. Abschnitt 5 leitet sie nicht her; die Ueberschrift fuehrt sie trotzdem unter [M].
- Anforderung:
  - "Folge" auf den statischen Fall beschraenken (p = 0, pdot = 0) und den Lambda-Term nennen.
  - Fuer Bewegung die Terme in p und pdot nennen, die Hamilton-Bedingung getrennt.
  - Den Staub als "momentan ruhend, nicht statisch" kennzeichnen.
  - Den Uhren-Satz als Lesart kennzeichnen ([H] bzw. [L]).

### A5 "Einfach gesagt" ist an zwei Stellen staerker als der Text

- Zitate:
  - Satz 2: "Die Traegheit aus der Literatur macht Schwerewellen nur zusammen mit einer bestimmten Eckenregel richtungsgleich, und genau dann schaukeln sich Stoerungen auf."
  - Satz 5: "... fuer mehr braucht es eine Zeit, in der der Raum ueberall gleich schnell waechst oder schrumpft."
- Begruendung:
  - (a) Satz 2 laesst "bisher" und "unter den gerechneten Regeln" weg. 2.3 sagt selbst: "Gerechnet ist nur: Isotropie ohne Abstimmung gab es bisher nur mit B und RH" und "keinen allgemeinen Ausschluss" (Codex 3).
  - (b) "genau dann" ist falsch. Mit der Literaturtraegheit wachsen Stoerungen auch unter R1, wo sie richtungsabhaengig ist (2.3: V an 142 von 511 k, Glas an jedem k; nach LUND-REGGE-MASSE-1 Tab. 4.4 auch S an 28 und A15 an 12). Die Instabilitaet haengt also nicht an der Richtungsgleichheit. Auf V ist die Richtungsgleichheit zudem nicht trennbar (Ritz 3,16 %).
  - (c) Satz 5 sagt "braucht es", also notwendig. Der Text sagt "Kandidat" und "Pruefen". Dazu kommt die Bedingung aus A3.
- Anforderung:
  - Satz 2: "bisher, in den gerechneten Paarungen"; ohne "genau dann". Gesagt werden sollte, dass mit der Literaturtraegheit Stoerungen unter R1 und unter RH wachsen (unter R2 nur auf einem von vier Glasnetzen).
  - Satz 5 als Kandidat mit Bedingung formulieren.
  - Kleinere Punkte zum selben Absatz: B9 ("nur kleine Wellen"), B14 ("echte vierdimensionale Zeit"), A4 ("bei ruhender Materie" heisst statisch).

## 2. B-Befunde (ungenau, fehlende Bedingung)

### B1 Homogenitaet mit Shiftterm; das Zeichen s doppelt belegt (2.3, Form B)

- Zitat: "Die Legendre-Umkehr gibt (1/2) pᵀ M(N)^-1 p + pᵀ B s ..." und direkt danach "M(sN) = M(N)/s, also H(sN) = s H(N)".
- Der Shiftterm pᵀ B s haengt nicht von N ab. Fuer das H der Zeile davor ist H(sN) = s H(N) also falsch [M, R2]. Richtig ist es fuer den Lapse-Teil H_N (Bewegung plus Potential) bzw. bei Shift null; so formuliert es auch Codex ("im shiftfreien kinetischen Ansatz").
- Dasselbe gilt fuer "Nach Euler gilt Summe_v N_v C_v = H": gemeint ist H_N.
- s steht zugleich fuer den Shift und den Skalierungsfaktor.
- Anforderung: Bedingung "Lapse-Teil, ohne Shiftterm" nennen; fuer die Skalierung ein anderes Zeichen.

### B2 Zwei-Zellen-Beispiel ohne seine Voraussetzungen (2.3)

- Zitat: "Zwei Zellen mit einer gemeinsamen Kante geben H = p^2 N1 N2/(2 (N1 + N2))."
- Die Formel gilt fuer einen einzigen gemeinsamen Freiheitsgrad mit Massen m1 = m2 = 1. Allgemein ist H = p^2 N1 N2/(2 (m1 N2 + m2 N1)) [M, R3]. Zwei Regge-Tetraeder haben je sechs Kanten und indefinite M_t.
- [M] traegt das Spielzeugbeispiel. Fuer echte Regge-Zellen ist "generisch nichtlinear" bis zur Zwei-Tetraeder-Probe (Abschnitt 9) plausibel, aber [H].
- Anforderung: Voraussetzungen nennen, Kennzeichen trennen.

### B3 Nichtlokale Form: welches M, und Stabilitaet nur linear (2.3)

- Zitat: "(1/2) Summe_e N_e p^e (M^-1 p)_e ist linear in N und bei gleichem N gleich B ... Die Stabilitaet ist bei gleichem N die von B."
- Linear ist die Form nur mit dem festen M(1) = Summe_t M_t. Mit M(N)^-1 waere sie es nicht. Der Leser zu Fassung 2 hatte das angegeben; 2.1 laesst es weg.
- Gleiche Werte auf der Diagonale heisst nicht gleiche Zwangsbedingungen. Im Beispiel R4 (Massen 1 und 3) gibt B die Ableitungen p^2/32 und 3 p^2/32, die nichtlokale Form p^2/16 und p^2/16. Die Summen stimmen (Euler), die Ableitungen nicht [M]. Die Zwangsflaechen sind also verschieden.
- "Stabilitaet die von B" gilt deshalb nur in linearer Ordnung um p = 0. Dort sind beide Ableitungen von der Ordnung p^2 (B4 des Lesers zu Fassung 2).
- Anforderung: M(1) ausschreiben; den Stabilitaetssatz auf die lineare Ordnung beschraenken.

### B4 Gemischte Form: B_t doppelt belegt; "Ausweg" (2.3)

- In "Bei zellweise verschiedenen B_t wird H quadratisch in s" ist B_t der Shiftoperator je Zelle. In "P_tᵀ B_t v" und "p = Summe_t B_tᵀ P_t" ist B_t Codex' Rekonstruktionsmatrix (Kantenraten zu Zellrate). Dazu kommt "Form B". Die Elimination stimmt [M, R5], die Schreibweise fuehrt zu Fehllesung. Codex schreibt fuer den Shift S.
- Unter "Auswege [H]" steht (iv) als Ausweg, obwohl 2.3 selbst sagt "Ein Trick fuer erste Klasse ist das nicht". Codex: Erst die Dirac-Analyse der Abgleichbedingungen kann einen Ausweg zeigen oder ausschliessen.
- Anforderung: getrennte Zeichen; (iv) als Pruefweg, nicht als Ausweg.

### B5 Der Satz zum Weg ueber Z_s/Z_t ist ungenau (3.1)

- Zitat: "Kaeme die 8 dagegen ueber das Verhaeltnis Z_s/Z_t allein in den Skalar, aenderte sie mit einem Potential die Compton-Laenge in Netzeinheiten".
- Die Compton-Wellenzahl ist k_C^2 = U'(0)/Z_s [M, R6]. Sie aendert sich nur, wenn die 8 ueber Z_s kommt.
- Kommt sie ueber Z_t (Z_t durch 8 geteilt), skaliert sie im Skalar alle omega^2 gleich. Die Compton-Laenge bleibt. Physik aendert sich trotzdem, denn der Skalar laeuft dann mit Tempo Wurzel 8, das Licht mit 1.
- Anforderung: beide Wege getrennt nennen.

### B6 Richtungsgleichheit des Lichts: Begruendung fehlt (3.1)

- Zitat: "Grund fuer die Richtungsgleichheit: Mit umkreisbasierten Dualzellen sind lineare Funktionen diskret harmonisch ..., und es gilt Summe *1 l lᵀ = Vol I".
- Das traegt den Skalar und den elektrischen Teil. Fuer den magnetischen Teil braucht es Summe_f *2_f |f|^2 n_f n_fᵀ = Vol I, ausserdem, dass konstante Felder ohne Korrektor stationaer sind. Beides habe ich von Hand fuer jedes periodische Netz mit umkreisbasiertem Dual nachgerechnet [M, R7]. Die Aussage haelt also.
- Der Leser zu Fassung 2 hatte Maxwell nicht nachgerechnet (R5). DANZER-NAEHERUNG-2 nennt nur Summe *1 l lᵀ (RUNDE-48.md Zeile 494).
- Anforderung: die Licht-Identitaeten nennen oder das Kennzeichen fuer Licht auf [P] beschraenken.

### B7 Die diskrete Uebertragung des Torus-Arguments ist nicht hergeleitet (Abschnitt 4)

- Zitat: "Diskret gilt dasselbe, solange d0ᵀ *1 d0 positiv semidefinit ist (*1 >= 0)."
- Das setzt voraus, dass die diskrete Lapse-Gleichung die Form d0ᵀ *1 d0 N = -*0 W N mit diskretem W >= 0 hat. Der Operator kommt aber aus {K_v, H_w} und damit aus dem gewichteten Schlaefli-Term (Summe (N_e' - N_ref) l_e' d eps_e'/d l_e, Abschnitt 5). Ob er d0ᵀ *1 d0 ist, zeigt 2.1 nicht; Abschnitt 4 fuehrt die Poisson-Matrix selbst unter "Zu berechnen".
- Anforderung: als [H] oder mit dieser Bedingung kennzeichnen.

### B8 W >= 0 ist im eigenen Materiesektor nicht gesichert (Abschnitt 4; Codex 4)

- Zitate: "Bei Lambda = 0 und W >= 0 ... bleibt nur N = 0", "Folge: K = 0 ist auf dem Torus nur linear ... zulaessige Eichung", Abschnitt 0: "K = 0 ist auf dem geschlossenen Torus nur linear zulaessig."
- Codex (Gegenblick v2, Punkt 4): Das Vorzeichen von rho + S im konkreten Materiesektor ist gesondert zu bestimmen. 2.1 nimmt das nicht auf.
- Fuer das komplexe Feld mit L = |phidot|^2 - |grad phi|^2 - U gilt rho + S = 4 |phidot|^2 - 2U [M, R9].
  - Negativ ist das fuer jede statische Lage mit U > 0.
  - Im Q-Ball-Schwanz (U ~ m^2 |phi|^2, phi ~ e^(i omega t)) ist es negativ, wenn omega^2 < m^2/2.
- Dann gilt nur noch "nicht generisch". Die Folge bleibt generisch richtig, das "nur" braucht aber die Bedingung.
- Anforderung: Bedingung (Lambda = 0, W >= 0, sonst generisch) in Abschnitt 0 und in der Folge nennen; Vorzeichen von rho + S fuer den Q-Ball als Pruefpunkt.

### B9 "traegt nur kleine Wellen" (Abschnitt 4 und Einfach gesagt)

- Zitat: "Als maximale Scheibung traegt er auf dem Torus nur kleine Wellen."
- Genau gilt: K = 0 ist nur in linearer Naeherung zulaessig. In der vollen Theorie erzwingt schon eine kleine Welle (W > 0 irgendwo) N = 0. Nach dem Satz in A3 [L] gibt es auf T^3 mit Lambda = 0 und rho >= 0 ueberhaupt keine maximalen Daten mit Welle.
- "nur kleine Wellen" kann Finn als "kleine Wellen gehen" lesen.
- Anforderung: "nur in der Naeherung kleiner Wellen" o. ae.; den T^3-Satz als [L] ergaenzen, er stuetzt die Folge unmittelbar.

### B10 Volumenmode: Pruefung fuer B mit R1 liegt schon vor (Abschnitt 4, Energie)

- Zitat: "Negative Richtungen bei k = 0 sind vor der Deutung "Instabilitaet" auf sie zu pruefen."
- LUND-REGGE-MASSE-1 (eine der im Kopf genannten Ernten) hat das fuer B mit R1 getan (Tab. 4.4, Spurdiagnose):
  - Auf den Kristallen ist die globale konforme Richtung die einzige negative bei k = 0 und waechst nicht.
  - Die wachsenden Richtungen liegen am Nullkegel der lambda = 1-Form (Spuranteil 0,334 bis 0,337), nicht auf der konformen Richtung.
  - Auf Glas sind bei k = 0 (Gamma) 28 bis 33 von 29 bis 34 negativen Richtungen wachsend.
- Eine einzige globale Mode erklaert nicht die negativen Richtungen im Kasten: A1RH 9, A2RH 5, A2LR1 28, A2LRH 46 von 481 (HODGE-MASSE-1 4.4). Lokale Spurrichtungen haben nach DeWitt ebenfalls negative Bewegungsenergie.
- Anforderung: den Stand aus LUND-REGGE-MASSE-1 eintragen; die Pruefung auf lokale Spurrichtungen erweitern.

### B11 "Auf dem Torus ist das offen" (Abschnitt 4, K = 0 als eigenes Gesetz) - als Frage

- Hat K = 0 als eigenes Gesetz dieselbe Lapse-Gleichung, dann greift dasselbe Torus-Argument, und auch dort bleibt nur N = 0. Ob die Lapse-Gleichung dieselbe ist, kann ich ohne SKALAR-SEKTOR-L nicht entscheiden.
- Anforderung: pruefen und "offen" gegebenenfalls schaerfen.

### B12 Die Pruefliste fuehrt die globale Impulsrekonstruktion nicht (Abschnitt 8)

- Abschnitt 0 nennt sie offen (Codex 4), Abschnitt 8 "Offen" enthaelt sie nicht. Sie entscheidet, ob Form A und die gemischte Form dieselben Kantenimpulse meinen.
- Anforderung: als eigenen Punkt aufnehmen.

### B13 "Bekannt sind drei Regime" (Abschnitt 6)

- RUNDE-48.md Zeile 460 kennzeichnet die drei Regime ausdruecklich als "Kern [ES]" von LAMBDA-TURING-L, nicht als Literatur.
- "(Joe)" belegt laut LT4 (Zeile 459), dass monotones Umklappen in 3D scheitern kann. "nicht eindeutig" ist eine Zuspitzung dieses Befunds.
- Anforderung: [ES] kennzeichnen; Joe mit dem Wortlaut von LT4.

### B14 "echte vierdimensionale Zeit" (Einfach gesagt)

- REGIME-K-1 rechnet die euklidische Bloch-Hesse der 4D-Regge-Wirkung (RUNDE-48.md 11:41:09). "echte" laesst an eine lorentzsche Zeitentwicklung denken; die wird nicht gerechnet. Laut 2.3 beantwortet (ii) die Frage nach dem freien Lapse ausserdem nicht.
- Anforderung: neutral, etwa "die Bewegungsenergie aus einer vierdimensionalen Wirkung".

## 3. C-Befunde (Stil)

- **C1 "Takt" allein:** Zeile 11 sagt: "Das Wort "Takt" allein wird hier nicht mehr benutzt." Das "Einfach gesagt" schreibt "Finns Takt als "maximale Zeitscheiben"".
- **C2 Vorzeichen und Variable der Kantenkraft (Abschnitt 5):**
  - "Kantenkraft ... nach q_e = l_e^2 gleich -eps_e/(16 pi G l_e)" ist dH/dq_e. Die Kraft pdot_e = -dH/dq_e hat das umgekehrte Vorzeichen [M, R10].
  - Der Lambda-Beitrag steht als dV/dl_e, also nach l, der Kruemmungsteil nach q. Nach q waere es (Lambda/8 pi G) dV/dl_e mal 1/(2 l_e).
- **C3 "gleich gross wie der Fehlwinkel" (Abschnitt 5):** Der Leser zu Fassung 2 schrieb "dieselbe Ordnung". "gleich gross" sagt mehr; genau gegengleich ist es nur im statischen Vakuum.
- **C4 HM0-Zahlen ohne Einheit (2.2):** "(1,02 bis 1,36, spurfrei 0,019 bis 0,039)". In der Quelle heisst es "spurfrei nur 0,019 bis 0,039 des Kontinuumswerts". Ob Verhaeltnis oder Abweichung gemeint ist, bleibt offen (Selbstanzeige des Lesers zu Fassung 2). "(1,2e-13)" heisst in der Quelle "hoechstens 1,2e-13".
- **C5 B mit R1 auf den Kristallen (2.3):** Genannt ist nur V (142 von 511 k). S (28) und A15 (12) fehlen, ebenso das erste instabile kl (0,94 / 2,17 / 2,02; LUND-REGGE-MASSE-1 Abschnitt 2 Punkt 3).
- **C6 Kuerzel weiter ohne Aufloesung:** "Codex Rang 8" (3.2) und "HKV 2013" (6) [L: Hirani/Kalyanaraman/VanderZee]. Das war schon C2 des Lesers zu Fassung 2.
- **C7 Friedman/Jack (2.3):** 2.1 schreibt "werden durch Konsistenz bestimmt". Codex (Punkt 2) schreibt "bestimmt werden koennen", RUNDE-48.md Zeile 246 "bleiben ... nicht erhalten". Bei "nur Abstract" passt das vorsichtigere Modalverb.
- **C8 Verweise ohne Formel:** "das reelle 1/2-Schema" (3.2) steht in 2.1 nirgends ausgeschrieben. Y_s und Y_t (3.1) kommen in H^EM (3.2) nicht vor, sind dort also stillschweigend 1. Je eine Zeile genuegt.
- **C9 N0 im ungefixten Modell (3.1, optional):** Bei freien N_v laesst sich ein konstanter Faktor N0 in N_v aufnehmen. Die Setzung ist dann reine Konvention. Ein Halbsatz macht klar, dass physikalisch nur das Verhaeltnis der Tempi zwischen den Sektoren zaehlt.

## 4. Einarbeitungstabelle (A1 bis A7 aus Fassung 2, Codex 1 bis 5)

| Befund | Stand | Begruendung (Restpunkte hier) |
|---|---|---|
| A1 zwei "nur" | umgesetzt | Strahl-Linearitaet, nichtlokale Form und Grad-0/Euler stehen da. Rest: Bedingungen und Schreibweise (B1, B3) |
| A2 Glas-/Kristallsatz | umgesetzt | Zahlen stimmen (Abschnitt 5); neue LUND-REGGE-Zahlen richtig eingeordnet. Rest: C5 |
| A3 Zeiteinheit in den Formeln | umgesetzt | N0 = Wurzel 8 in Skalar, Licht und Geometrie; Rechnung richtig (R6). Rest: B5, B6, C8 |
| A4 K = 0 auf dem Torus | umgesetzt | Torus-Argument, Nullmode, CMC und Moncrief stehen da. Neu zu stark: York-Zeit (A3 hier); Bedingungen B7 bis B9 |
| A5 Kruemmung = Spannung | teilweise | Der gewichtete Schlaefli-Term ist richtig (R10), die "Folge" verallgemeinert ueber den statischen Fall hinaus (A4 hier) |
| A6 Einarbeitungsstand | teilweise | D_v ehrlich "nur benannt", s-Interpolation in Abschnitt 1. "Spurbindung ja" ist neu zu stark (A1 hier) |
| A7 Einfach gesagt | teilweise | Die drei benannten Saetze sind berichtigt; neue Ueberzeichnung (A5 hier) |
| Codex 1 Legendre/Linearitaet | umgesetzt | Invertierbarkeit, Dirac-Algorithmus, Gegenbeispiel unabhaengige Bloecke, Homogenitaet. Rest: B1, B2 |
| Codex 2 A und B verschieden, gemischte Form | umgesetzt | "Setzung", Summe lokaler Inversen, Shift global/je Zelle, gemischte Form, Friedman/Jack nur Abstract, Regime K. Rest: B4, C7 |
| Codex 3 kein Struktur-No-Go | teilweise | In 2.3 sauber. Abschnitt 4 ("R1 stabil") und das "Einfach gesagt" ("nur ... genau dann") verallgemeinern wieder (A2, A5 hier) |
| Codex 4 Konvention, Positivitaet, Abschnitt 5 | teilweise | Komplexe Normierung und Faktor-8-Koeffizienten gebunden. Offen: Vorzeichen rho + S (B8), Impulsrekonstruktion fehlt in der Pruefliste (B12), volle Variation mit Bewegungstermen (A4 hier) |
| Codex 5 Kleinsttest | umgesetzt | Zwei-Tetraeder-Probe und Schlaefli-Probe in Abschnitt 9 Punkt 3 (als Plan) |

## 5. Projektzahlen gegen Quellen (Auftrag C)

| Stelle | Dokument | Quelle | Ergebnis |
|---|---|---|---|
| 2.2 | A2 1,02 bis 1,36, spurfrei 0,019 bis 0,039; Lund-Regge 1,2e-13 | HODGE-MASSE-1 Abschnitt 3, HM0 | stimmt (Lesart C4) |
| 2.2 | A2_t K_t = 1 auf 1,6e-9 | HODGE-MASSE-1 4.2, Code-Gegenproben | stimmt |
| 2.3 | V: A1R1 6,34 %, A2R1 5,92 % | Tab. 4.2: 6,339 %, 5,924 % | stimmt |
| 2.3 | ohne wachsende Moden nur A1R1, A2R1 (sieben Netze, Kasten) | Tab. 4.2 (ohne * und neg); 4.4 Kasten "Positiv nur A1R1 und A2R1"; LUND-REGGE-MASSE-1 5.1 (511 k: A1R1 hier gerechnet, A2R1 [P]) | stimmt |
| 2.3 | B mit RH ~1e-7 (S, A15), V Ritz 3,16 %, Glas Ritz 3,5e-6 bis 7,7e-6 | Tab. 4.2: 1,34e-7, 7,53e-8; V Ritz 3,16 %; Glas 4,5e-6 / 7,7e-6 / 6,0e-6 / 3,5e-6 | stimmt |
| 2.3 | je 1 wachsende Mode auf V, S, A15; Glas 46 bis 50 | Tab. 4.2: neg 1 / 1 / 1; Glas 48 / 50 / 47 / 46 | stimmt |
| 2.3 | B mit R1: V 10,6 %, S 0,74 %, A15 4,7 % | Tab. 4.2 A2LR1: 10,56 / 0,743 / 4,69 %; LUND-REGGE-MASSE-1 2.1 | stimmt |
| 2.3 | V an 142 von 511 k | LUND-REGGE-MASSE-1 Tab. 4.4: 142 | stimmt (S 28, A15 12 fehlen: C5) |
| 2.3 | Glas an jedem k, 27 bis 33 Moden | LUND-REGGE-MASSE-1 Abschnitt 2 Punkt 3: "27 bis 33 je Spannenpunkt"; LR3 dort: 28 bis 33; Tab. 4.4 Gamma: 28 / 31 / 33 / 28 | stimmt mit Abschnitt 2; die Quelle ist selbst uneinheitlich (27 oder 28) |
| 2.3 | Ursache c^+ p = 0, Masse exakt kontinuumsgleich | LUND-REGGE-MASSE-1 5.1; LR0 <= 5,6e-14 (RUNDE-48.md Zeile 452) | stimmt |
| 2.3 | Glas waechst mit RH (A1, A2, A2L), mit A2LR1 je Netz, mit A2LR2 in einem von vier | Tab. 4.2: A1RH neg 10 / 9 / 10 / 9; A2RH neg 6 / 5 / 7 / 6; A2LRH 48 bis 50 und 46; A2LR1 28 bis 33; A2LR2 nur s2 neg 1 | stimmt |
| 6 | 1,26e-3 / 3,93e-3 / 1,17e-3, hoechstens 3,1e-2; Glas N = 128, A = 1e-3, s1 bis s3, s4 ohne Zug, A2R1 | Tab. 4.4 A2R1: 1,26e-3 / 3,93e-3 / 1,17e-3; Max 3,48e-3 / 3,12e-2 / 5,27e-3; s4 0 Zuege | stimmt |
| 6 | 9 Freiheitsgrade = 5 . 3 - 6 | 15 - 6 = 9 | stimmt |
| 3.1 | DANZER-NAEHERUNG-2 | RUNDE-48.md Zeile 494: Skalar und Maxwell "auf jedem periodischen Netz exakt isotrop (Summe *1 l l^T = Vol I)" | stimmt; Begruendung fuer Licht siehe B6 |
| 8 | V1-AUFHEBUNG-1: auf V mit abgestimmten Gewichten vertraeglich | RUNDE-48.md Zeile 417: mit V1 + S + J_iso abs(G - 1) <= 1,5e-5, 9-mal unter 1,3e-4 | stimmt |
| 6 | Henkel und RP^3 nicht spinoriell | RUNDE-48.md Zeile 430 [S] | stimmt |
| 2.3, 5, 6 | DANZER-TT-1, REGIME-K-1, SPLITTER-FREI-1, UEBERGABE-KONFLUENZ-1, KRUEMMUNGS-SANDHAUFEN-2D-1 laufen | RUNDE-48.md Zeile 512 (Stand 11:42) | stimmt |

- Rundungen von Hand: 6,339 auf 6,34; 5,924 auf 5,92; 10,56 auf 10,6; 0,743 auf 0,74; 4,69 auf 4,7; 3,12e-2 auf 3,1e-2. Alle richtig.

## 6. Urteil

**Weitergabe an Finn als Arbeitsstand: ja nach den A-Befunden.**

- Neu und von Hand richtig sind:
  - Legendre mit Shift
  - Homogenitaet (mit Bedingung B1)
  - Zwei-Zellen-Beispiel (mit Bedingung B2)
  - nichtlokale Form, linear mit M(1)
  - gemischte Form
  - Zeiteinheit N0 = Wurzel 8 mit den Folgen fuer Skalar, Licht und Geometrie
  - komplexe Normierung
  - Torus-Argument im Kontinuum
  - gewichteter Schlaefli-Term
- Alle Projektzahlen in 2.3 und 6 stimmen mit den Quellen.
- Die fuenf A-Befunde betreffen Wortlaut und Bedingungen, keine Rechnung:
  - Stand der Spurbindung (A1)
  - "R1 stabil" (A2)
  - York-Zeit ohne Bedingung (A3)
  - "Folge" in Abschnitt 5 ueber den statischen Fall hinaus (A4)
  - zwei Saetze im "Einfach gesagt" (A5)
- Ein Neubau ist nicht noetig. Nach den Aenderungen sollte ein frischer Leser die letzte Schicht lesen, vor allem Abschnitt 0, Abschnitt 5 und das "Einfach gesagt".

## 7. Selbstanzeigen

- **Werkzeuge:** nur date, ls, wc, sha256sum, grep (lesend), mkdir fuer den vorgegebenen Ordner sowie Read. Geschrieben habe ich nur diese Datei (Write und Edit). Kein Interpreter, kein awk, kein ssh, kein git, kein Peerbus.
- **Ordnernamen:** `ls -la` auf RUNDE-37 zeigte die Namen anderer Karten- und Leserordner, darunter regime-k-1, danzer-tt-1, splitter-frei-1 und uebergabe-konfluenz-1. Geoeffnet habe ich keinen davon.
- **grep ueber die vorgegebenen Quellen hinaus:**
  - Ein grep nach "Bahr" ueber coordination/runden-v3 mit allen Pflicht-Ausschluessen. Er listete Dateinamen auf, unter anderem Quellen-XML in RUNDE-11 und RUNDE-34 sowie Fassung 1.
  - Danach habe ich die Trefferzeilen in RUNDE-41.md, RUNDE-46.md, pachner-takt-1/ERGEBNIS.md und Fassung 2 gelesen (je eine bis zwei Zeilen), um das [S] bei Bahr/Dittrich einzuordnen. Kein Befund stuetzt sich darauf.
  - Fassung 2 habe ich erst nach dem vollstaendigen Lesen von 2.1 beruehrt, und nur diese eine grep-Zeile.
- **Nicht selbst geprueft:**
  - A2R1 an allen 511 k (nur [P] aus LUND-REGGE-MASSE-1 5.1)
  - SKALAR-SEKTOR-L (B11 deshalb als Frage)
  - REGGE-KINETIK-L und DANZER-NAEHERUNG-2 (nur ueber RUNDE-48.md und den Codex-Text)
  - Code (Spurbindung)
- **Literatur aus dem Gedaechtnis [L], an keiner Quelle geprueft:** Schoen/Yau, Gromov/Lawson (T^3 ohne R >= 0 ausser flach), Variationsformel der mittleren Kruemmung, Marsden/Tipler, Gerhardt, Andersson/Moncrief, hydrostatisches Gleichgewicht, Hirani/Kalyanaraman/VanderZee. Jahreszahlen und Einzelheiten koennen abweichen.
- **Grenzen meiner Rechnungen:**
  - R7 ist eine Schreibtischrechnung fuer die fuehrende Ordnung in k. Sie setzt vorzeichenbehaftete Duallaengen und ein nicht entartetes Netz voraus.
  - R4 ist ein Spielzeugbeispiel und kein Regge-Netz.
- **Zeiten:** Alle Uhrzeiten stammen aus date. Die Lesestand-Zeilen nennen nur gemessene Grenzen (11:47:59, 12:04:51). Den Zeitpunkt, zu dem ich mit dem Lesen fertig war, habe ich nicht gemessen.

## 8. Rechenwege (von Hand, ohne Rechner)

### R1 Legendre mit Shift (2.3): haelt

- p = dL/dqdot = Summe_t M_t v/N_t = M(N) v, also qdot = M(N)^-1 p + B s.
- H = pᵀ qdot - L = pᵀ M^-1 p + pᵀ B s - (1/2) pᵀ M^-1 p = (1/2) pᵀ M(N)^-1 p + pᵀ B s. Wie im Dokument.
- Mit dem stueckweise linearen Shift aus Eckwerten und q_e = l_e^2 ist (B s)_e = 2 (x_b - x_a).(s_b - s_a) auf dem flachen Netz in jeder Zelle gleich. Verschiedene B_t entstehen erst ohne gemeinsamen Rahmen (gekruemmt).

### R2 Homogenitaet (B1)

- M(cN) = Summe_t M_t/(c N_t) = M(N)/c, also (1/2) pᵀ M(cN)^-1 p = c (1/2) pᵀ M(N)^-1 p.
- Der Term pᵀ B s bleibt mit Faktor 1 statt c. Damit gilt H(cN) = c H_N(N) + pᵀ B s, und das ist ungleich c H(N), solange pᵀ B s ungleich 0 ist.

### R3 Zwei Zellen, ein gemeinsamer Freiheitsgrad (B2)

- L = (1/2) qdot^2 (m1/N1 + m2/N2) gibt p = (m1/N1 + m2/N2) qdot und H = p^2 N1 N2/(2 (m1 N2 + m2 N1)).
- Mit m1 = m2 = 1 entsteht die Formel des Dokuments. Nichtlinear: f = N1 N2/(N1 + N2) hat f(1,1) = 1/2, aber (f(2,0) + f(0,2))/2 = 0.
- Unabhaengige Bloecke M1 = diag(1,0), M2 = diag(0,1): M(N)^-1 = diag(N1, N2), H = (N1 p1^2 + N2 p2^2)/2, also linear. Wie im Dokument.

### R4 Nichtlokale Form gegen B: gleiche Werte, verschiedene Zwangsbedingungen (B3)

- Spielzeug: ein Freiheitsgrad, Massen m1 = 1, m2 = 3, Kantenlapse N_e = (N1 + N2)/2.
- B: H_B = p^2 N1 N2/(2 (N2 + 3 N1)). Bei (1,1): p^2/8.
  - dH_B/dN1 = (p^2/2) N2^2/(N2 + 3 N1)^2 = (p^2/2)(1/16) = p^2/32.
  - dH_B/dN2 = (p^2/2) 3 N1^2/(N2 + 3 N1)^2 = 3 p^2/32. Summe 4 p^2/32 = p^2/8 (Euler).
- Nichtlokal mit M(1) = 1 + 3 = 4: H_nl = (1/2) ((N1 + N2)/2) p (p/4) = p^2 (N1 + N2)/16. Bei (1,1): p^2/8, gleich.
  - dH_nl/dN1 = dH_nl/dN2 = p^2/16, also nicht p^2/32 und 3 p^2/32.
- Beide Ableitungen sind von der Ordnung p^2. Linear um p = 0 stimmen die Zwangsbedingungen deshalb ueberein, darueber nicht.

### R5 Gemischte Form (2.3): haelt

- Stationaer in P_t: B_t v - N_t G_t^-1 P_t = 0, also P_t = G_t B_t v/N_t.
- Eingesetzt: Summe_t [vᵀ B_tᵀ G_t B_t v/N_t - vᵀ B_tᵀ G_t B_t v/(2 N_t)] = Summe_t vᵀ M_t v/(2 N_t) mit M_t = B_tᵀ G_t B_t. Das ist die Lund-Regge-Form. p = dL/dqdot = Summe_t B_tᵀ P_t.

### R6 Zeiteinheit (3.1): haelt, mit B5

- H_tot = N0 H gibt qdot = N0 dH/dp und pdot = -N0 dH/dq, also t' = N0 t. Alle omega^2 werden mit N0^2 multipliziert.
- Skalar: L = (1/N0) Z_t *0 |phidot|^2 - N0 [Z_s Summe *1 |dphi|^2 + *0 U]. Variation nach phi* gibt Z_t *0 phi'' = -N0^2 Z_s d0ᵀ *1 d0 phi - N0^2 *0 U'(S) phi. Mit Z_s = Z_t und N0^2 = 8 ist das -Z_t T phi - ... Wie im Dokument.
- Langwellig gilt omega^2 = N0^2 [(Z_s/Z_t) k^2 + U'(0)/Z_t]. Gleichheit der beiden Terme bei (Z_s/Z_t) k^2 = U'(0)/Z_t, also k_C^2 = U'(0)/Z_s. Das haengt nur an Z_s (B5).
- Licht: Adot = N0 E/*1 und Edot = -N0 d1ᵀ *2 d1 A ergeben *1 A'' = -N0^2 d1ᵀ *2 d1 A. Wie im Dokument.
- Geometrie, TT-Teil im Kontinuum: H enthaelt 16 pi G pi:pi + (1/64 pi G) (grad h):(grad h). Daraus hdot = 32 pi G N0 pi und pidot = N0 Laplace h/(32 pi G), also hddot = N0^2 Laplace h. G kuerzt sich.

### R7 Licht richtungsgleich auf jedem periodischen Netz mit umkreisbasiertem Dual (B6)

- **Flaechen-Identitaet:**
  - Je Tetraeder t mit Umkreismittelpunkt c_t gilt delta_ij Vol(t) = Summe_{f in t} |f| (g_f - c_t)_i (n_f)_j (Gauss; g_f Schwerpunkt, n_f aeussere Normale).
  - Zerlegung: g_f - c_t = (c_f - c_t) + (g_f - c_f). Der Umkreismittelpunkt des Tetraeders projiziert auf den der Flaeche, also ist c_f - c_t = h_{f,t} n_f, und g_f - c_f steht senkrecht auf n_f.
  - Summiert ueber t heben sich die Terme mit g_f - c_f paarweise weg: gleicher Vektor, entgegengesetzte Normalen, periodisch ohne Rand.
  - Es bleibt Vol I = Summe_f |f| (h_{f,t1} + h_{f,t2}) n_f n_fᵀ = Summe_f |f| |f*| n_f n_fᵀ = Summe_f *2_f |f|^2 n_f n_fᵀ (vorzeichenbehaftete Duallaengen).
- **Kein Korrektor:**
  - Konstantes B: (d1 A)_f = |f| B.n_f exakt (Stokes). *2 macht daraus |f*| B.n_f, das ist B mal Dualkante, weil die Dualkante parallel zu n_f liegt. d1ᵀ davon an der Kante e ist die Zirkulation eines konstanten Felds um das geschlossene Dualpolygon e*, also 0.
  - Konstantes E (E^e = *1_e E.l_e): (d0ᵀ E)_v = -E.(Summe |e*| n_e) = 0, weil die Voronoi-Zelle geschlossen ist.
- **Folge:** Mit Summe *1 l lᵀ = Vol I (Leser zu Fassung 2, R5) sind langwellig Permittivitaet und Permeabilitaet gleich I. Damit gilt omega^2 = N0^2 k^2 fuer beide Polarisationen und jede Richtung. Das ist eine Schreibtischrechnung fuer die fuehrende Ordnung in k.

### R8 Komplexe Normierung (3.2): haelt

- pi = dL/dphidot = Z_t *0 phidot*. H = pi phidot + pi* phidot* - L = 2 Z_t *0 |phidot|^2 - Z_t *0 |phidot|^2 + V = |pi|^2/(Z_t *0) + V.
- phi = (phi1 + i phi2)/Wurzel 2 gibt |phidot|^2 = (phi1dot^2 + phi2dot^2)/2, also p_i = Z_t *0 phi_idot und pi = (p1 - i p2)/Wurzel 2.
- Dann |pi|^2/(Z_t *0) = (p1^2 + p2^2)/(2 Z_t *0). Symplektisch: pi phidot + c.c. = 2 Re[(p1 - i p2)(phi1dot + i phi2dot)/2] = p1 phi1dot + p2 phi2dot. Wie im Dokument.

### R9 Torus, York-Zeit, rho + S (A3, B8, B9)

- **Lapse-Gleichung:**
  - Spur der Entwicklungsgleichung: dK/dt = -Laplace N + N (R + K^2) + 4 pi G N (S - 3 rho) - 3 N Lambda.
  - Mit der Hamilton-Bedingung R + K^2 = K:K + 16 pi G rho + 2 Lambda wird daraus dK/dt = -Laplace N + N (K:K + 4 pi G (rho + S) - Lambda). Wie im Dokument; das Torus-Argument haelt im Kontinuum.
- **Killing-Argument [M; Variationsformel L]:**
  - Statische Raumzeit, zeitartiges Killingfeld xi, geschlossene CMC-Flaeche mit Wert tau, u = -<xi, n> > 0.
  - Der Isometriefluss erhaelt die mittlere Kruemmung. Weil tau auf der Flaeche konstant ist, faellt der Tangentialteil weg, und es bleibt 0 = -Laplace u + (K:K + Ric(n,n)) u.
  - Integriert: Integral (K:K + Ric(n,n)) u = 0. Mit u > 0 und Ric(n,n) >= 0 (flach: 0) folgt K_ij = 0, also tau = 0.
- **T^3 [L]:** Bei K = 0 und Lambda = 0 gibt die Hamilton-Bedingung R = K:K + 16 pi G rho >= 0. Auf T^3 hat nur die flache Metrik R >= 0. Dann ist R = 0, also K_ij = 0 und rho = 0.
- **rho + S** fuer L = |phidot|^2 - |grad phi|^2 - U, Signatur (-,+,+,+), T_mn = 2 Re(d_m phi* d_n phi) + g_mn L:
  - rho = 2 |phidot|^2 - L = |phidot|^2 + |grad phi|^2 + U.
  - S = 2 |grad phi|^2 + 3 L = 3 |phidot|^2 - |grad phi|^2 - 3U.
  - rho + S = 4 |phidot|^2 - 2U. Fuer phi = f e^(i omega t) und U ~ m^2 f^2 im Schwanz ist das (4 omega^2 - 2 m^2) f^2, negativ bei omega^2 < m^2/2.

### R10 Abschnitt 5 (A4, C2)

- **Gewichteter Schlaefli-Term:** d/dl_e Summe_e' N_e' l_e' eps_e' = N_e eps_e + Summe_e' N_e' l_e' d eps_e'/dl_e. Wegen Schlaefli kann man N_ref mal 0 abziehen. Wie im Dokument.
- **Vorzeichen:** H_kr = -(1/8 pi G) Summe N_e l_e eps_e. Bei N = 1 ist dH/dl_e = -eps_e/(8 pi G) und dH/dq_e = -eps_e/(16 pi G l_e). Die Kraft ist pdot_e = +eps_e/(16 pi G l_e).
- **Ruhender Staub ist nicht statisch** (Kontinuum):
  - Hydrostatisches Gleichgewicht: d_i p = -(rho + p) d_i ln N [L]. Bei Staub (p = 0) folgt d_i N = 0, wo rho > 0.
  - Die Lapse-Gleichung mit K_ij = 0 und S = 3p gibt Laplace N = N (4 pi G (rho + 3p) - Lambda). Bei Lambda = 0 und konstantem N im Staub folgt 0 = 4 pi G N rho, ein Widerspruch.
  - Momentan ruhender Staub hat also pdot ungleich 0.
