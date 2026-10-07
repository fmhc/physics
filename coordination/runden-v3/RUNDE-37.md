# Runde 37 (v3), eroeffnet 2026-10-04 02:29:05 CEST

- Leitung claude-primary. Runde 36 laeuft noch aus: REGGE-SCHAUM-1 (Leitung, cpu6) und der Gegenleser der
  Anschauungsseite sind offen; danach Abschluss mit Journaleintrag.
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [H] Hypothese, [E] hier gerechnet.

## Eingang

1. **Schreibtisch nach REGEL-1 (RUNDE-36/REGEL.md, Abschnitt 8):**
   - Die Regel "Kruemmungsmuster kostet nichts" ist die freie Umbenennung der Zeit. Gu/Wen Gl. 23 ist die
     Lapse-Verschiebung [L/M].
   - Dieselbe Symmetrie verlangt Energie als Quelle (gleiches Fallen) [H/M].
   - Ein Raum-Netz mit eigener Bewegungsenergie je Kante gaebe dagegen lambda = -1/2, also c = 1/5 [M].
   - Das spricht fuer ein Raumzeit-Netz statt eines Raum-Netzes mit aeusserer Uhr [H].
2. **Fokus:** Q-Baelle (stille Schwingung) und die Herkunft der Regge-Wirkung in Finns Netzbild.

## Karten

| Karte | Inhalt | Stand |
|---|---|---|
| V-1-PRAEZISION | Leck der stillen Wandschwingung bei eps < 0 mit erweiterter Genauigkeit: c = 2 pi? Vorfaktor? | Test, gestartet |
| PONZANO-1 | 6j-Symbole auf Tetraederkanten: Regge-Wirkung in der Phase, Pachner-Zug exakt, Gewicht der 2-3-Summe | Test, gestartet |

## Gestartet

- 2026-10-04 02:29:05 CEST: V-1-PRAEZISION (Spuren cpu3 und cpu4, Zeitbox 120 min) und PONZANO-1 (Spur cpu, Zeitbox 90 min).
  - Aktive Agenten 3 von 3: Gegenleser der Seite, V-1-PRAEZISION, PONZANO-1.
  - Die Leitung rechnet REGGE-SCHAUM-1 (Runde 36) auf cpu6.
- 2026-10-04 02:50:08 CEST: Finn: "Ok weiter entwickeln".
  - Schreibtisch RUNDE-37/RAUMZEIT-NETZ.md: drei Lesarten (Regge bzw. Spinschaum, Kausalmenge, CDT), Ort von Finns
    Bausteinen, sechs gereihte Karten, Weiche lokal oder ohne Ruhesystem.
  - KAUSAL-1 (Leitung selbst, p4000a als CPU-Lauf): alle vier Vorhersagen eingetroffen.
    - L/N = ln N - 1,42 (8,24 bei N = 16 000).
    - Rapiditaetsdichte 0,96 bis 1,03.
    - Ein Raumzeit-Netz ohne Ruhesystem hat keine festen Nachbarn.
    - Selbstanzeige: K0-Lesart nach dem Rauchwert festgelegt. Abschaetzung: erledigt.
- REGGE-SCHAUM-1 (Runde 36) geerntet: Schaum gibt dasselbe G auf 0,02 %; RS0 an Schlaefli und Symmetrie verfehlt (1e-10).
- 2026-10-04 02:52:26 CEST: Runde 36 geschlossen (Abschlusstabelle in RUNDE-36.md). Journal claude-runde-v3-36-20261004 nach pruefen (0 Befunde nach Titelkuerzung; der erste Titel hatte drei M5-Markierungen fuer Zahlen) veroeffentlicht. Sicherung .69 -> TS440 lief 02:16 durch (rc 0).

### Ernte PONZANO-1 (RUNDE-37/ponzano-1/ERGEBNIS.md; eingetragen 2026-10-04 03:01:51 CEST)

- Code-Agent, Plan eingefroren 02:48:23, Spur cpu. Gegengelesen an lauf-69/auswertung.json und ERGEBNIS.md.
- **Urteile:** PO0, PO1 und PO2 eingetroffen; PO3 nicht eingetroffen.
- **Kernbefunde (exakte Mathematik; die Hauptaussagen sind Literatur, also vorab ableitbar):**
  - Das 6j-Symbol folgt fuer grosse Spins der Ponzano-Regge-Formel: Abweichung 3,0e-4 bzw. 6,6e-4 bei lambda = 100,
    Steigung -0,96 bzw. -0,75. In der Spinfolge liegen alle 193 Vorzeichenwechsel im Intervall der Kosinus-Nullstellen.
    Regges Wirkung steckt also in der Phase der Drehimpulskopplung.
  - Ohne echtes Tetraeder: ln abs(6j) = -8,63 - 2,29 lambda (R^2 = 0,999996).
  - Biedenharn-Elliott (Pachner 2-3), Orthogonalitaet und die 24 Symmetrien gelten exakt rational. 15 831 Vergleiche mit
    sympy sind gleich. Die Umbenennungsfreiheit gilt in 3D also exakt.
  - PO3 nicht eingetroffen: Der Betrags-Schwerpunkt der 2-3-Summe liegt 28 bis 34 % unter der flachen Laenge x* und
    folgt der Huellkurve.
- **Beschreibend:** Die vorzeichenbehaftete Summe sammelt ihren Wert genau an zwei Stellen.
  - Am flachen Schluss x* (Fehlwinkel 0) trifft sie den Ponzano-Regge-Term auf 0,02 bis 2,1 %.
  - An einer gefalteten Einbettung x_fold trifft sie den gefalteten Term auf 0,01 bis 0,25 %.
  - Dazwischen heben sich die Summanden weg (Betragssumme 13- bis 1409-mal groesser).
  - Regges Bewegungsgleichung (flacher Schluss) entsteht also aus Interferenz der Phase, nicht aus dem Gewicht.
- **Kontrollen:**
  - exakt gegen mpmath 3e-51
  - Summe gleich Produkt 6,5e-50
  - Cayley-Menger gegen Einbettung 2e-50; Defizit bei x* 3e-50
  - Winkelkonvention vor dem Einfrieren am gleichseitigen Tetraeder geprueft
- **Selbstanzeigen:**
  - Zwei geschaetzte Zeiten im eingefrorenen Plan (nicht per date).
  - PO3 war vorab fast ableitbar; PO1 bei Form B knapp (-0,751 gegen -0,7).
  - Auswertungscode nach dem Einfrieren geschrieben, vor dem Ansehen gesichert.
  - Vermerke in auswertung.json von Hand nachgetragen (Maschinenfassung daneben, gleich).
- **Bedeutung fuer Finns Bild [L/H]:** Schreibt man Drehimpulse auf die Striche eines Tetraeders, steckt Regges Wirkung
  schon in der Quantenmechanik.
  - Der Pachner-Zug, die Umbenennungsfreiheit in 3D, ist eine exakte Identitaet.
  - Flachheit, also Einsteins Gleichung in 3D, entsteht durch Interferenz.
  - Das ist 3D-Schwerkraft ohne Wellen; in 4D gilt es nur naeherungsweise (Spinschaum) [L].
- **Abschaetzung:** erledigt. Folgeidee [H]: 4D-Gegenstueck (EPRL-Ecke) als Literaturkarte; geparkt.
- 2026-10-04 03:06:38 CEST: Zweiter Gegenleser der Anschauungsseite (02:35 bis 02:59): **KORRIGIEREN**.
  - Alle 41 Zahl- und Rechenangaben richtig. Alte Befunde: 24 erledigt, B3 und B20 teilweise. Neue Befunde: 17.
  - **C1 (hoch):** Dasselbe "Aufblas"-Minus war oben Ursache, beim Balkenbild Bremse der Anziehung. Beides stimmt, aber in
    zwei Rechenbildern (Hamilton-Kraftfluss gegen kovariant 4D).
  - **Weitere:**
    - REGEL-1-Zahlen ohne RG3-Vermerk.
    - "Uhren" statt Zeitzaehlung (Lapse ist Eichfreiheit, echte Uhren nicht).
    - Annahmen zu c = 1/5 unvollstaendig. Ein Diamant-Netz ist nicht richtungsgleich: Spurfreie Verformungen kosten dort
      keine Bewegungsenergie (Rechnung des Pruefers).
    - Strenge Regeln als dritte Zutat fehlten.
  - **Leitung:** Fassung 3 mit beiden Buchfuehrungen benannt, dritter Kasten "strenge Regeln", Zeitzaehlung, Geltungen,
    REGGE-SCHAUM-1 und KAUSAL-1.
  - Als Version 3 veroeffentlicht, weiter als Entwurf; dritter frischer Leser gestartet.
- 2026-10-04 03:06:38 CEST: PONZANO-1 geerntet (siehe oben). Freie Plaetze: REGGE-ZEIT-1 gestartet (Spuren cpu und cpu6) und der dritte Leser.
  Aktive Agenten 3 von 3: V-1-PRAEZISION, REGGE-ZEIT-1, dritter Leser.

### Ernte V-1-PRAEZISION (RUNDE-37/v1-praezision/ERGEBNIS.md; eingetragen 2026-10-04 03:18:16 CEST)

- Code-Agent, Plan eingefroren 02:59:38, Spuren cpu3 und cpu4. Gegengelesen an lauf-69/auswertung.json und ERGEBNIS.md.
- **Urteile:** PR2 (knapp, mit Vermerk) und PR3 eingetroffen; PR0 und PR1 nicht eingetroffen.
- **Kernbefunde (Taylor-Reihen mit 60 bzw. 40 Stellen):**
  - Das Leck ist an sechs Punkten aufgeloest: P = 8,69e-17 (eps = -1e-2) bis 1,55e-49 (-2e-3).
  - Genauigkeit: ln P auf >= 16 Stellen gleich; Flussbilanz < 1e-56; bei eps = +3e-3 Leck 6,9e-115.
  - **PR1:** Mit der einfachen Form 1/sqrt(abs(eps)) ist c = 6,149 statt 2 pi, also 2,1 % zu klein (q = -0,39). Die Form
    passt trotzdem: groesster Rest 0,022 in ln P (PR3).
  - **PR2:** Mit der genauen Wellenzahl K_B des Hauptkanals (69 bis 87 % des Lecks) ist der Polabstand d = pi - 0,28 %
    (q = -2,0). Auch die Kanaele A und B einzeln und der Hintergrundschwanz geben pi auf 0,2 bis 0,5 %.
  - Die Herleitung der Leitung (Polabstand pi der logistischen Wand) traegt also. Meine Abkuerzung c = 2 pi mit
    k = 1/sqrt(abs(eps)) ist nur die fuehrende Naeherung (K_B liegt 0,6 bis 3,2 % darunter).
- **Vermerke:**
  - **PR2:** Die Kanalformel der Karte (Leitung) war falsch: Das Vorzeichen passt nicht zur Dispersion, und sie setzt rho
    statt der Kanalfrequenz ein. Der Agent hat K_B vor dem Einfrieren im Plan begruendet festgelegt. Mit der
    Kartenformel woertlich: -2,54 %, also nicht eingetroffen.
  - **PR0** scheitert nur am Vergleich mit V-1-WEITER-A (-7,4 %, Schwelle 5 %). Gegen V-1-WEITER-B sind es -1,4 %.
    Ursache ist die Schwanzwahl im Hintergrund, eine Modellwahl, deren Einfluss nicht gemessen ist. Im Modell D stimmt die
    Methode auf 1,8e-6.
- **Selbstanzeigen:** Ein Rauchlauf bei eps > 0 lief ueber und wurde gestoppt; Kontrolle deshalb mit f0-Hintergrund
  (vor dem Einfrieren im Plan). Fuenf falsche Zahlen im eigenen Entwurf vor Abgabe berichtigt (offengelegt).
- **Bedeutung fuer Papier I:**
  - Die stille Wandschwingung ist bei gitterartiger Erweichung nur exponentiell schwach undicht. Das Leck folgt
    P ~ A abs(eps)^q exp(-2 pi K_B), wobei pi der Polabstand der Wand ist.
  - Bis 1e-49 gemessen; die Modellabhaengigkeit (Schwanzwahl) liegt bei ~6 % in P.
- **Abschaetzung:** erledigt. Robustheitsabsatz fuer Papier I moeglich (Text noch nicht geschrieben).
- 2026-10-04 03:19:15 CEST: Freier Platz nach V-1-PRAEZISION: CDT-HORAVA-L gestartet (feldforscher, Literatur, nur gezielte arXiv-Abrufe, Zeitbox 75 min).
  - Gegensweep zur eigenen Hypothese "Raum-Netz mit Uhr kann die 1/2 nicht von selbst".
  - Aktive Agenten 3 von 3: REGGE-ZEIT-1, dritter Leser der Seite, CDT-HORAVA-L.
- 2026-10-04 03:20:44 CEST: Schleifendurchlauf.
  - Codex (quittiert): Die nodale Cj-Huelle 694,34 (statt 996,90) gibt nu <= 1,2101 (vorher 1,7375). Noetig waere < 1;
    weiter NOT_CERTIFIED, naechster Methodentest geplant.
  - Scout-Lauf 20261004T010216Z, 29 Kandidaten. Eingespeist in IDEEN-EVOLUTION/pool.jsonl als Generation 4 (Sicherung
    pool.jsonl.bak-20261004-gen4):
    - S1 QBALL-PYRO-1 (arXiv 2606.15855: Solitonen und kompakte Flachbandzustaende auf dem Pyrochlor-Gitter)
    - S2 REGGE-TORSION-L (arXiv 2610.00593: Regge mit Torsion)
    - S3 STRING-EINDEUTIG-L (arXiv 2610.02124: Eindeutigkeit von String-Amplituden, Glieder 7 und 10)
    - dazu K1 KAUSAL-3D, R1 REGGE-WELLE-1, R2 QBALL-AUF-REGGE
- 2026-10-04 03:40:02 CEST: Dritter Gegenleser der Seite (03:06 bis 03:31): **KORRIGIEREN**.
  - Alle 32 Zahlen richtig; 18 alte Befunde erledigt; C1 zum Teil offen; neu D1 bis D11.
  - **D1:** "ln N - 1,42 Striche je Punkt" ist L/N; der Grad ist doppelt so gross (16,48 bei N = 16 000). Dieselbe
    Fehllesung stand in KAUSAL-1/ERGEBNIS.md (Berichtigung angehaengt) und in meiner Meldung an Finn.
  - **D2:** "ruhig" uneinheitlich. **D3:** "von beiden Pruefern" falsch. **D4:** Preis des Raumzeit-Netzes (nicht lokal)
    fehlte.
  - **Leitung:** Fassung 4 nur mit den verlangten Korrekturen; C1 mit der Lesart "ein 4D-Modus traegt beide
    Minuszeichen" [M, Ueberlegung, an keiner Quelle geprueft]. Als Version 4 veroeffentlicht, weiter Entwurf; vierte
    Lesung beim naechsten freien Platz.
- 2026-10-04 03:40:02 CEST: Freier Platz nach dem dritten Leser: QBALL-PYRO-1 gestartet (Spuren cpu3 und cpu4, Zeitbox 120 min).
  - Exakte Ring-Q-Baelle auf Sechserringen des Pyrochlor-Gitters (flache Bande), Stabilitaet und Beweglichkeit.
  - Aktive Agenten 3 von 3: REGGE-ZEIT-1, CDT-HORAVA-L, QBALL-PYRO-1.
- 2026-10-04 03:47:04 CEST: Schleifendurchlauf.
  - Codex (quittiert): Quellbasis V2 vollstaendig, NOT_CERTIFIED; nu-Tor weiter nicht bestanden.
  - An Codex gesendet (Peerbus 8a4cd56f, kind result, Hinweis an den Codex-Faden ohne bestaetigte Zustellung): Angebot
    der Ergebnisse von V-1-WEITER und V-1-PRAEZISION fuer den Abschnitt Gitterrobustheit von Papier I
    (paper-v41-grid-robustness). Keine Bitte um Lauf; Entscheidung bei Codex bzw. Finn.

### Ernte CDT-HORAVA-L (RUNDE-37/cdt-horava-l/DOSSIER.md; eingetragen 2026-10-04 03:54:30 CEST)

- feldforscher, 15 von 15 gezielten Abrufen, keine Websuche; Abgabe 03:53:11.
- **Erwartungen:**
  - E1 teilweise: Form wie Einstein (de Sitter), aber der kinetische Term ist positiv und kommt aus dem Abzaehlen der
    Triangulierungen. lambda ist aus V(t) nicht bestimmbar.
  - E2 eingetroffen: Lifshitz-artiges Phasendiagramm; B-C_b zweiter Ordnung, C_b-C_dS zweiter oder hoeherer.
  - E3 eingetroffen: 2D-CDT gleich projizierbare 2D-HL-Gravitation mit lambda < 1, Lambda > 0.
  - E4 nach Recherchestand eingetroffen (keine 4D-Messung), dem Sinn nach verletzt (2+1-Messung existiert).
  - E5 halb: Die Bewegungsenergie kommt aus der Entropie; sie landet aber im selben positiv definiten Bereich wie unser
    c = 1/5.
- **Kernbefund [S]:** Wo lambda in CDT bestimmt ist, liegt es nicht bei Einstein.
  - 2D: exakt lambda < 1.
  - 2+1, Budd 2011 (Tagungsarbeit, zwei uneinige Methoden): lambda_eff ~ 0,03 bis ~ 0,49 < 1/2. Am Phasenuebergang
    steigt es auf 1/2.
  - In 4D keine Messung gefunden.
- **Zuordnung c = lambda/(d lambda - 1)** steht woertlich bei Ambjorn/Glaser/Sato/Watabiki 2013, Gl. (6) [S]. Unsere
  Formel ist damit an der Quelle bestaetigt.
- **Budd/Loll modellieren die CDT-Zeit als vorab festgelegten Lapse ohne Hamilton-Bedingung**, mit einem zusaetzlichen
  lokalen Freiheitsgrad [S]. Das ist genau unser Fall "Netz mit aeusserer Uhr".
- **Schaerfung der Weiche [ES]:** Es geht nicht um "Raum- gegen Raumzeit-Netz", sondern um "nur globale Schichtzeit gegen
  eine lokal frei umstellbare Zeit".
- **Selbstanzeigen:**
  - Einmal awk benutzt, nur lesend (gegen die Regel, im Dossier vermerkt).
  - Websuche-Regel 7 nicht erfuellbar.
  - "Euklidisch positiv" gegen "lorentzsch stabil" ist nicht geprueft.
- **Bedeutung:** CDT spricht nicht gegen die Hypothese der Leitung; es stuetzt sie in 2+1 mit einer (duennen) Messung. Ein
  geschichtetes Tetraedernetz braucht eine lokal frei umstellbare Uhr, sonst landet es abseits von Einstein.
- **Abschaetzung:** erledigt. Folgeidee [H]: lambda in einem eigenen kleinen geschichteten Netz aus Form- und Volumenmoden
  messen (Budd-Methode); geparkt.
- 2026-10-04 03:55:13 CEST: Seite Fassung 5 (Version 5): Fassung 4 plus ein Absatz zum CDT-Befund. Vierter frischer Leser gestartet. Aktive Agenten 3 von 3: REGGE-ZEIT-1, QBALL-PYRO-1, vierter Leser.

### Ernte REGGE-ZEIT-1 (RUNDE-37/regge-zeit-1/ERGEBNIS.md; eingetragen 2026-10-04 03:59:47 CEST)

- Code-Agent, Plan eingefroren 03:48:52, Spuren cpu und cpu6. Gegengelesen an lauf-69/auswertung.json und ERGEBNIS.md.
- **Urteile:** Z0 eingetroffen; Z1, Z2 und Z3 nicht eingetroffen (Z3 nicht deutbar).
- **Kernbefund:** Fern der Masse gibt das 4D-Laengennetz mit Zeitkanten Newton und Einsteins gamma = 1. Nahe der Masse
  liegt es einige Prozent zu hoch.
  - x-Achse, L = 32: gamma = 1,087 (r = 6), 1,023 (r = 10), 1,014 (r = 14), etwa 1 + 2,2/r^2. Die G-Staerke faellt von
    1,042 auf 1,010 (etwa 1 + 1,6/r^2).
  - Unabhaengig vom Torus (gamma(6) = 1,0874 / 1,0872 / 1,0872 fuer L = 24 / 32 / 64), also ein Gittereffekt bei kleinem
    Abstand.
  - L = 64 (nur Bericht): gamma = 1,0038 und G-Staerke 1,0029 bei r = 24.
  - Die Zeitkanten werden nahe der Masse kuerzer (Rotverschiebung). Das Newton-Potential aus den Zeitkanten trifft auf
    L = 64 fuer r = 6 bis 14 auf 0,3 bis 0,8 %.
  - **3D-Kontrolle:** Fehlwinkel nur an der Weltlinie (sonst 1,4e-14), dort 8 pi G M auf 5e-15. "Masse = Fehlwinkel" in
    2+1 als Identitaet bestaetigt.
- **Strukturbefunde:**
  - Die tote Hyperdiagonale (fuenfte Nullmode aus REGGE-4D-1) kostet keine Wirkung, veraendert aber Fehlwinkel, gerade
    an (tau, x)- und (y, z)-Dreiecken. Einzelne Fehlwinkel sind damit nicht festgelegt.
  - Der Agent legte sie vor dem Einfrieren je Impuls auf die kleinsten Fehlwinkel fest. Die erste Regel war nicht
    periodisch und wurde verworfen.
  - **Kartenfehler der Leitung:** Ein Fehlwinkel misst die Kruemmung der Ebene senkrecht zum Dreieck. (tau, x)-Dreiecke
    sehen R_yzyz (Kalibrierung exakt 1,000). Bei gamma = 1 aendert das nichts.
- **Kontrollen:**
  - flach 1,8e-15
  - Ableitungen auf zwei Wegen 3,8e-12
  - Eichmoden aendern Fehlwinkel um 5e-13
  - zwei Eichungen gleich auf 1e-11
  - Torus-Korrektur 5e-4 bei r <= 10
- **Selbstanzeigen:**
  - Z3: Das 2x2-System auf der Diagonale war fast singulaer (Kondition 204 bis 828, Sperre erst ab 1000), also gamma = -29
    statt "nicht auswertbar". Beschreibend: kinematisch 0,82 bis 0,95, auf L = 64 0,989 (r = 28).
  - Einmal lokal awk als Durchreichfilter benutzt (Regelverstoss, ohne Wirkung).
  - Vermerke per jq nachgetragen; Maschinenfassung daneben.
- **Bedeutung:**
  - Im Laengennetz mit Zeitkanten koppelt die Masse ueber ihre Eigenzeit. Das Netz gibt fern der Masse Newton und die
    doppelte Lichtablenkung (gamma = 1).
  - Nahe der Masse (unter ~10 Maschen) stoert vermutlich die tote Hyperdiagonale des regelmaessigen Kuhn-Gitters [H].
- **Abschaetzung:** weiter. Folge: REGGE-4D-SCHIEF-1, ein verzerrtes 4D-Gitter ohne rechte Winkel. Dort sollte die
  fuenfte Nullmode verschwinden, und die Naehe der Masse sollte sauberer werden.
- 2026-10-04 04:01:02 CEST: Freier Platz nach REGGE-ZEIT-1: REGGE-4D-SCHIEF-1 gestartet (Spuren cpu und cpu6, Zeitbox 120 min).
  - Schiefes 4D-Kuhn-Gitter ohne rechte Winkel: Verschwindet die fuenfte Nullmode, bleibt der Fingerabdruck, wird gamma nahe der Masse sauberer?
  - Aktive Agenten 3 von 3: QBALL-PYRO-1, vierter Leser, REGGE-4D-SCHIEF-1.
- 2026-10-04 04:09:09 CEST: Finn: "Weiter. Was bedeutet das? Haben wir ein Teilchenmodell?"
  - Antwort: Nein, ein Baukasten (Q-Baelle, Pfeil-Eis-Coulomb, Strings, Laengennetz-Schwerkraft).
  - Es fehlen Spin 1/2, Quantenmechanik, die Verbindungen der Bausteine und ein Spektrum.
  - Finn danach: "Mach weiter".
  - Karte QBALL-LADUNG-1 (geladene Q-Baelle, groesste Ladung) vorbereitet, Start beim naechsten freien Platz.
  - **Spin 1/2 laut Memory, entschieden am 23.09.:** Die unveraenderte Formel kann keinen Spin 1/2 tragen (zusammenziehbarer
    Konfigurationsraum, also nur bosonisch). Codex' Umbau C x S^2 behaelt den alten Q-Ball und gibt Spin 1/2 aus dem
    bekannten Hopf/FR-Mechanismus (eingesetzt, nicht hergeleitet). Offen: Binden Hopftraeger und Amplitudenladung?
    Quelle literatur-20260923/SPIN-KONSTRUKTION-codex.md.
- 2026-10-04 04:23:32 CEST: Finn: "Mach mehr Agent Plätze". Grenze von 3 auf 5 gleichzeitige Agenten angehoben (Memory: Neuausrichtung,
  Nachtrag). Spuren auf der .69 sind jetzt der Engpass.
  - Gestartet: SPIN-HOPF-L (feldforscher, Literatur) und REGGE-WELLE-1 (Spuren p4000b, cpu5).
  - Vierter Leser der Seite: KORRIGIEREN. Keine Zahl falsch, C1-Rechnung bestaetigt (der 4D-Aufblasmodus traegt beide
    Minuszeichen, zeitlich ganz Minus 2, raeumlich zu 1/3 Minus 1 und zu 2/3 Lapse). Der CDT-Absatz sagt zu viel (E2 bis
    E5); C1-Rest, D2 und D6 teilweise. Seite bleibt Entwurf; Fassung 6 folgt.
- 2026-10-04 04:23:32 CEST: Finn: "Ideate zu 1/2" (gelesen als Spin 1/2).
  - IDEEN-EVOLUTION/GEN-04-SPIN-HALB.md mit zehn Ideen H1 bis H10; acht neu im Pool (Sicherung
    pool.jsonl.bak-20261004-spinhalb).
  - Rang 1: Fermion = Stringende (Levin/Wen); Rang 2: Ladung + Monopol (Goldhaber).
  - STRINGENDE-1 gestartet (Spur p4000a, Zeitbox 90 min). Aktive Agenten 5 von 5: QBALL-PYRO-1, REGGE-4D-SCHIEF-1,
    SPIN-HOPF-L, REGGE-WELLE-1, STRINGENDE-1. Die Leitung rechnet QBALL-LADUNG-1 (p4000a, geteilt).

### Ernte QBALL-PYRO-1 (RUNDE-37/qball-pyro-1/ERGEBNIS.md; eingetragen 2026-10-04 04:33:24 CEST)

- Code-Agent, Plan eingefroren 04:06:59, Spuren cpu3 und cpu4. Gegengelesen an lauf-69/auswertung.json.
- **Urteile:** QP0, QP1 und QP4 eingetroffen; QP2 und QP3 nicht eingetroffen.
- **Kernbefunde:**
  - Exakte Ring-Q-Baelle auf Sechserringen des Pyrochlor-Gitters gibt es fuer jede Amplitude. Flache Baender weichen
    <= 4e-15 ab; der Ring ist exakter Eigenvektor. QP1 war vorab ableitbar und prueft nur den Code.
  - **QP2 umgekehrt:** Die Ringe ueber dem Band (a^2 = 1,5 / 2 / 3) zerfallen mit Raten 0,32 / 0,76 / 1,12, eine
    Instabilitaet nach Art von Vakhitov-Kolokolov. Die Ringe im Band (0,5 / 1) bleiben ueber T = 200 kompakt (Leck 2e-9 bzw.
    5e-8). Das gilt auch mit zweiter Saat, groesserem Gitter und halbem Zeitschritt.
  - **QP3:** a^2 = 1 reisst bei jedem Stoss zu 41 bis 49 % auf. Nur a^2 = 0,5 bleibt ortsfest (<= 0,031 h).
  - **QP4:** Ein gewoehnlicher Q-Ball (h = 0,5, omega^2 = 0,7) liegt 0,82 % (E) bzw. 0,80 % (Q) unter dem Kontinuum und
    laeuft nach einem Stoss 36,4 Gitterabstaende.
- **Kartenfehler der Leitung (im Plan vor dem Einfrieren berichtigt):** Das Volumen je Knoten ist sqrt(2) h^3, nicht h^3.
  Mit h^3 laegen E und Q 29,9 % zu tief, und QP4 waere nicht eingetroffen.
- **Kontrollen:** Ladung 2,7e-14, Energie 7,9e-6; Zeitentwicklung gegen Bogoliubov 2 bis 7 %; Radialloeser gegen
  RUNDE-02 auf 1,6e-6.
- **Selbstanzeigen:**
  - Einmal python -c (Versionspruefung) auf der .69 ausserhalb des Starters, ohne Rechnung.
  - Instabilitaet bei a^2 >= 2,5 schon im Rauch gesehen (offengelegt).
  - QP3 haengt an der Festlegung "stabil = kompakt in QP2".
- **Bedeutung:**
  - Auf Finns Tetraedergitter gibt es neben den gewoehnlichen Q-Baellen ortsfeste Ringzustaende. Stabil sind aber nur
    die schwachen, und wirklich gegen Stoesse fest nur der schwaechste.
  - Gewoehnliche Q-Baelle merken vom Tetraedergitter kaum etwas.
  - "Eingefrorene Materie" als Netz-Kennzeichen ist damit hoechstens fuer schwache Ringe moeglich [H].
- **Abschaetzung:** erledigt; geparkt.
- 2026-10-04 04:35:16 CEST: Freier Platz nach QBALL-PYRO-1: KAUSAL-SWERVE-1 gestartet (Spuren cpu3 und cpu4, Zeitbox 90 min). Laeufer auf einer Kausalmenge: Reibung oder nur Zittern (Swerves)? Aktive Agenten 5 von 5: REGGE-4D-SCHIEF-1, SPIN-HOPF-L, REGGE-WELLE-1, STRINGENDE-1, KAUSAL-SWERVE-1.
- 2026-10-04 04:35:16 CEST: QBALL-LADUNG-1 (Leitung): Familien Fassung 1 geerntet. QL0 eingetroffen: Q, E und f0^2 auf alle gedruckten Stellen der RUNDE-02-Tabelle. Die Klammersuche versagte bei grossem Omega0 und bei duennen Waenden, ein Ende der Familie waere also Rechenfehler. Fassung 2 (robuste Klammer, Gueltigkeitspruefung, Modus zielQ fuer QL1) offengelegt; Laeufe auf p4000a.
- 2026-10-04 04:36:55 CEST: Seite Fassung 6 (Version 6) nach dem vierten Leser.
  - CDT-Absatz auf die Suchgrundlage eingeschraenkt, mit Gegenlesart und dem Hinweis auf eine dritte 1/2.
  - C1: beide Buchfuehrungen mit Grund; Zuschreibung berichtigt. Dazu D2 (Eichdrift ohne Messbares), D6 (Geltung), E7, E8.
  - Fuenfte Lesung beim naechsten freien Platz (5 von 5 belegt). Sicherung index.html.bak-v5.

### Ernte REGGE-4D-SCHIEF-1 (RUNDE-37/regge-4d-schief-1/ERGEBNIS.md; eingetragen 2026-10-04 04:40:39 CEST)

- Code-Agent, Plan eingefroren 04:28:32, Spuren cpu und cpu6. Gegengelesen an lauf-69/auswertung.json.
- **Urteile:** SC0, SC1 und SC2 eingetroffen; SC3 nicht eingetroffen.
- **Kernbefunde:**
  - Im schiefen 4D-Kuhn-Netz (nur Raumachsen verzerrt) verschwindet die tote Hyperdiagonale: 10 Nullmoden bei k = 0 und
    4 bei allgemeinem k, an allen 144 Punkten.
  - Einsteins Form fuer lange Wellen bleibt in physikalischen Koordinaten erhalten: Spin 2 fuenffach gleich auf 0,31 %,
    c0s/c2 = -1,9989 bis -2,0047, Richtungsstreuung 0,11 %.
  - **Aber:** Die Diagonale wird eine Gittermode mit negativer Steifigkeit (-0,38 bei s = 0,1, -0,93 bei s = 0,2, linear
    in s). Bei allgemeinem k gibt es jetzt 9 positive und 2 negative Eigenwerte (Kuhn: 9 und 1).
  - Bei s = 0,2 geht zusaetzlich eine kurzwellige Gittermode durch null: 544 von 4096 Zonenpunkten haben 3 negative
    Werte.
  - Ruhende Masse: Fehlwinkel ohne Festlegung eindeutig. gamma(6) = 1,056 / 1,308 / 1,113 auf den drei schiefen Achsen
    (Kuhn: 1,087). Fern der Masse gegen 1 (L = 48: 1,007 / 1,006 / 0,997). Auf A e_y kommt ein kurzreichweitiger Zusatz
    hinzu (~exp(-r/2,7)); dass er von der Diagonalmode stammt, ist eine Hypothese.
- **Kartenberichtigung (im Plan):** Von den 14 rechten Winkeln verschwinden nur 12; zwei bleiben, weil die Zeitachse
  senkrecht bleibt.
- **Kontrollen:**
  - s = 0 reproduziert REGGE-4D-1 und REGGE-ZEIT-1 (gamma(6) 1,08722717 gegen 1,08722700).
  - Drehprobe 5e-8; L = 24 / 32 / 48 auf 8e-4; Ableitungswege 6,4e-12.
- **Selbstanzeigen:**
  - Zwei Fehlstarts ohne Rechnung.
  - Die negative Mode schon vor dem Einfrieren unbeabsichtigt gesehen.
  - Eine Diagnose nach dem Einfrieren (beschreibend).
  - Vermerke per jq nachgetragen.
- **Bedeutung:**
  - Die tote Diagonale des Kristallnetzes ist der Grenzfall einer Mode, die im schiefen Netz eine verkehrte Steifigkeit
    bekommt. Ein schiefes Netz tauscht einen Fehler gegen einen anderen.
  - Fuer lange Wellen ist Einsteins Form robust, nahe der Masse ist sie es nicht.
  - Fuer Finns Schaumbild [H]: Zufaellige 4D-Laengennetze koennten weitere negative Gittermoden haben, also Instabilitaet
    in der euklidischen Rechnung. Das ist zu pruefen, bevor man "ungeordnet ist besser" sagt.
- **Abschaetzung:** weiter. Folge [H]: REGGE-4D-ZUFALL, Zahl der negativen Moden eines zufaelligen 4D-Netzes. Geparkt
  wegen Groesse.
- 2026-10-04 04:41:01 CEST: Freier Platz nach REGGE-4D-SCHIEF-1: fuenfter frischer Leser der Seite (Fassung 6) gestartet. Aktive Agenten 5 von 5: SPIN-HOPF-L, REGGE-WELLE-1, STRINGENDE-1, KAUSAL-SWERVE-1, fuenfter Leser.

### Ernte SPIN-HOPF-L (RUNDE-37/spin-hopf-l/DOSSIER.md; eingetragen 2026-10-04 04:50:06 CEST)

- feldforscher, 14 von 15 gezielten Abrufen, keine Websuche.
- **Erwartungen:**
  - E1 eingetroffen: Drehende Hopf-Knoten gibt es bis zur kleineren von Masse und der Frequenz, ab der die Pseudoenergie
    unbeschraenkt wird. Fuer unser Modell begrenzt 1/sqrt(2).
  - E2 eingetroffen: Ungerade Hopf-Zahl darf fermionisch sein (Krusch/Speight).
  - E3 teilweise: Ladung im selben Feld des Knotens ist belegt. Fuer ein zweites Q-Ball-Feld an einer S^2-Textur, stabil
    gebunden, fand sich kein Vorbild.
  - E4 nicht pruefbar (ohne Websuche).
  - E5 teilweise: 2D-Laeufe nach Schaetzung 3 bis 8 min.
- **Groesster Befund:** Das Projekt hat Vorarbeit, die meine Karte nicht kannte (Fehler der Leitung):
  - RUNDE-03/tests2d-r3/KNOTEN-PAPIER.md; CX-1 waehlte kappa = 1/4.
  - astras Pruefschranken; ein 3D-Pilot mit 0,96 % Vorteil aus Probeprofilen.
  - qball-hopf-3d: Dynamiksperre chi ~ 1,09 bei Omega ~ 0,98.
  - HOPF-1: Der h = 1-Knoten wickelte sich auf dem Gitter ab.
- **Neu [ES]:** Eine im Knoten gefangene Ladungswolke darf tiefer liegen als ein freier Q-Ball (lokal bis Omega^2 ~ 0,148
  bei gJ = 1, notwendige Bedingung).
  - Codex' Regel q in Z + h/2 stimmt an der Quelle. Im fermionischen Zweig bleibt mindestens eine halbe Ladungseinheit am
    Knoten.
- **Vorschlag:** QB-BS-2D (Baby-Skyrmion plus Q-Ball-Feld in 2+1; dort haelt der Rand den Knoten fest). kappa = 1 und
  1/4 vorab gebunden, kein dritter Wert nach Befund (Antwort der Leitung auf O6: ja).
- **Abschaetzung:** weiter, mit QB-BS-2D.
- 2026-10-04 04:51:04 CEST: Freier Platz nach SPIN-HOPF-L: QB-BS-2D gestartet (Spuren cpu und cpu6, Zeitbox 120 min, nur S0 bis S2 radial). Codex per Peerbus informiert (78c45e2a, kind plan). Aktive Agenten 5 von 5: REGGE-WELLE-1, STRINGENDE-1, KAUSAL-SWERVE-1, fuenfter Leser, QB-BS-2D.
- 2026-10-04 04:52:59 CEST: QBALL-LADUNG-1 (Leitung) abgeschlossen: QL0 und QL1 eingetroffen (Delta E ~ e^2, Steigung 1,998 bzw. 1,997), QL2 und
  QL3 nicht auswertbar.
  - Das Schiessverfahren findet das Familienende nicht verlaesslich: Bei e = 0,2 ist das Klassenmuster umgekehrt; bei
    e = 0,05 und 0,1 bricht es ab, waehrend Q noch steigt.
  - Beschreibend fuer e = 0,1: omega^2 hat ein Minimum (0,846) und E/Q eines (0,9416 bei Q ~ 900).
  - Abschaetzung: QL2 als Folgekarte mit Relaxationsloeser geparkt; H2 (Ladung + Monopol) kann auf QL1 aufbauen.

### Ernte STRINGENDE-1 (RUNDE-37/stringende-1/ERGEBNIS.md; eingetragen 2026-10-04 04:58:01 CEST)

- Code-Agent, Plan eingefroren 04:52:25, Spur p4000a. Gegengelesen an lauf-69/auswertung.json.
- **Urteile:** SE0, SE1, SE2 und SE3 eingetroffen (synthetisch, vorab ableitbar).
- **Kernbefunde:**
  - 2D-Torus-Code (12x12): Die Enden einfacher Strings sind Bosonen (e, m: +1). Das Ende des Doppelstrings
    epsilon = e x m ist ein Fermion (-1), in 2412 Messungen mit langen Strings und 20 736 lokalen Messungen.
  - Ursache: e um m gibt -1 (gegenseitige Halbzahligkeit).
  - Gegenprobe: Ladung und Fluss aus zwei unabhaengigen Lagen ergeben ein Boson (808 von 808).
  - 3D: Das Spin-3/2-Modell von Levin/Wen (cond-mat/0302460) laesst sich aus der Quelle nachbauen; seine Stringenden
    geben -1 (138 240 lokale und 301 lange Messungen, 8x8x8). Das bosonische 3D-Vergleichsmodell gibt +1 (301 von 301).
- **Kontrollen:** Fuehrt man ein Bein ueber das Ende eines anderen, kippt das Ergebnis. Die Messung kann also +1 liefern.
- **Kartenberichtigung:** Das Sechserprodukt ist e^(i theta), nicht theta (gleiche Gleichung, umgestellt).
- **Selbstanzeigen:**
  - Einmal python --version auf der .69 ausserhalb des Starters (vor jeder Rechnung, im Plan offengelegt).
  - Das PDF wurde seitenweise als Bild gelesen.
- **Bedeutung [H]:**
  - In bosonischen Netzmodellen koennen Stringenden Fermionen sein. In 2D braucht das zwei Strich-Sorten, die sich
    spueren; in 3D (Levin/Wen) eine besondere innere Bauweise je Knoten (Spin 3/2).
  - Gezeigt ist nur die Vertauschungsphase -1 mit Z_2-Eichfeld, nicht Spin 1/2 unter Drehungen und keine U(1)-Ladung.
  - Vorschlag des Agenten: dasselbe auf einem Gitter mit vier Strichen je Knoten (Diamant, wie Finns Tetraederknoten).
- **Abschaetzung:** weiter, mit dem Diamant-Gegenstueck (Gamma-Matrix-Kitaev-Modell, Literatur Ryu bzw. Wu/Arovas/Hung
  2009 [L]).
- 2026-10-04 04:58:56 CEST: Freier Platz nach STRINGENDE-1: KITAEV-DIAMANT-1 gestartet (Spur p4000a, Zeitbox 120 min). Gamma-Matrix-Kitaev-Modell auf dem Diamantgitter (Tetraederknoten): Fermionen plus Z_2-Eichfeld aus reinen Spins. Aktive Agenten 5 von 5: REGGE-WELLE-1, KAUSAL-SWERVE-1, fuenfter Leser, QB-BS-2D, KITAEV-DIAMANT-1.

### Ernte REGGE-WELLE-1 (RUNDE-37/regge-welle-1/ERGEBNIS.md; eingetragen 2026-10-04 05:05:37 CEST)

- Code-Agent, Plan eingefroren 04:49:55, Spur cpu5, sieben Starts. Gegengelesen an lauf-69/auswertung.json.
- **Urteile:** W0, W1, W2 und W3 eingetroffen. Nach Kartenwortlaut ist W3 nicht eingetroffen: Kartenfehler K1, vor dem
  Einfrieren offengelegt.
- **Kernbefunde (4D-Kuhn-Regge-Netz, Wellen in echter Zeit ueber komplexes k_tau):**
  - Geschwindigkeit:
    - Lange Schwerewellen laufen mit c: |k| = 0,05 gibt v = 0,99979 bis 0,99986; die groesste Abweichung von 1 bei
      |k| <= 0,1 ist 8,3e-4.
    - Kuerzere laufen langsamer, nie schneller: |k| = 0,8 gibt v = 0,9505 (Achsen) bis 0,9669 (Raumdiagonalen), also
      3,31 bis 4,95 % langsamer.
  - Moden:
    - In jeder Richtung genau zwei laufende Moden (Windungszahl 2,000 an 120 Punkten).
    - Sie sind gleich schnell auf 2e-11 bis 1,6e-10 |k| und reell; keine Doppelbrechung, kein Anwachsen.
    - Es sind die zwei raeumlichen TT-Polarisationen (Anteil >= 0,9987).
    - Die drei Richtungen ohne zweite Zeitableitung sind Lapse und Shift (Anteil >= 0,999998).
  - **Beschreibender Nachtrag (nach dem Hauptlauf, nicht geurteilt):**
    - Die Ausbreitung folgt in allen 24 Richtungen und 5 Betraegen der Formel des einfachsten Wuerfelgitters,
      sinh^2(omega/2) = sum_i sin^2(k_i/2), auf 3,5e-9 bis 1,4e-11 in v.
    - Daraus 1 - v ~ (1 + sum n_i^4) k^2/24 (von der Leitung im Kopf nachgerechnet: Achse |k| = 0,8 gibt 0,9505,
      Raumdiagonale 0,9669).
- **Kontrollen:**
  - Drei Wege zu den Nullstellen stimmen ueberein; komplexer Schritt <= 5,7e-9 |k|.
  - n gegen -n 7e-13; S3-Kopie 1,1e-9; Zeitumkehr 2,9e-12.
- **Selbstanzeigen:**
  - Einmal python -c "print(1)" auf der .69 ausserhalb des Starters.
  - TT-Messgroesse vor dem Einfrieren ersetzt (die erste Fassung war nicht eichinvariant); die Schwelle blieb.
  - Rauchlaeufe machten die Urteile absehbar.
  - Vermerke per jq nachgetragen.
- **Bedeutung:**
  - Im regelmaessigen 4D-Laengennetz laufen Schwerewellen fuer lange Wellen mit Lichtgeschwindigkeit, in Einsteins zwei
    Polarisationen; nur ganz kurze Wellen werden langsamer.
  - Das Netz zeichnet bei kurzen Wellen Richtungen und ein Ruhesystem aus (k^2-Korrektur).
  - GW170817 gibt daraus nur die schwache Schranke Maschenweite < ~3 bis 10 cm [H, Zahlen aus dem Gedaechtnis].
  - Warum die Wuerfelgitter-Formel exakt gilt, ist offen.
    - Vermutung der Leitung [L?]: Roček/Williams schrieben die linearisierte Regge-Wirkung des Kuhn-Gitters mit
      Gitter-Differenzen und Gitter-Eichfreiheit. Dann wird der TT-Teil zum Gitter-Laplace, und die Formel folgt.
    - An der Quelle nicht geprueft.
- **Abschaetzung:** weiter. Folge: REGGE-WELLE-SCHIEF-1, dieselbe Messung auf dem schiefen Netz aus REGGE-4D-SCHIEF-1.
  - Doppelbrechung?
  - Wird die Diagonalmode mit negativer Steifigkeit in echter Zeit zu einer wachsenden Welle?
  - Schneller als c bei kurzen Wellen?
- 2026-10-04 05:05:37 CEST: Fuenfter Leser (Fassung 6): OK MIT KLEINIGKEITEN (GEGENLESEN-5.md), 37 von 37 Zahlen richtig; F1 bis F3 vor Wegfall von "Entwurf", F4 freigestellt. Umsetzung in Fassung 7 (Sicherung index.html.bak-v6), dann kurzer frischer Blick auf die geaenderten Saetze.

### Ernte KAUSAL-SWERVE-1 (RUNDE-37/kausal-swerve-1/ERGEBNIS.md; eingetragen 2026-10-04 05:17:34 CEST)

- Code-Agent, Plan eingefroren 04:58:21, Spuren cpu3 und cpu4. Gegengelesen an lauf-69/auswertung.json.
- **Urteile:** KS0 eingetroffen (berichtigt), KS1 und KS2 nicht eingetroffen, KS3 eingetroffen.
  - KS0 nach Kartenwortlaut nicht eingetroffen. Kartenfehler: ln N - 1,42 ist das Mittel ueber alle Punkte; ein Punkt
    bei (u, v) hat ln N + gamma + ln((1-u)(1-v)) Zukunftslinks. Vor der Rechnung offengelegt.
- **Kernbefunde (1+1-Kausalmenge, N = 64 000):**
  - Im Inneren keine Reibung.
    - Gewertet nur Schritte, die im unendlichen Netz gleich ausgefallen waeren (469 605).
    - Mittlere Aenderung +0,0004 +- 0,0007; Steigung gegen eta -0,0005 +- 0,0005.
  - Starkes Zittern: Streuung je Schritt 0,250 in jeder eta-Klasse, vorab als genau 1/4 hergeleitet.
  - Kontrolle ohne Rand: Var = n/4; mittlere Energie waechst wie 1,138^n, also Heizen.
  - Der Rand des endlichen Diamanten erzeugt Scheinreibung (Steigung -0,071 +- 0,001).
    - Die schnellen Laeufer fallen zuerst hinaus; bei n = 50 sind nur 27 bis 31 % sicher im Inneren.
    - Daran scheitern KS1 und KS2 (Kartenzweig "Laeuferregel bzw. Rand zeichnet etwas aus").
- **Selbstanzeigen:**
  - Die Innenregel ist eine Festlegung des Agenten.
  - Ausgaenge weitgehend vorab ableitbar.
  - Laeuferzahl nach dem Rauchlauf erhoeht (Schwellen unveraendert).
  - Einmal das Literal Infinity in auswertung.json (kein Urteil betroffen).
- **Bedeutung [H]:**
  - Ein Raumzeit-Netz ohne Ruhesystem bremst nicht, es heizt.
  - Ein punktfoermiges Teilchen, das je Schritt einem Link folgt, zittert um 1/4 in der Rapiditaet je Schritt. Bei
    Planck-Schritten ist das durch Beobachtung ausgeschlossen [L: Swerve-Schranken, aus dem Gedaechtnis].
  - Teilchen muessen also ausgedehnt sein und ueber viele Punkte mitteln, etwa ein Q-Ball. Das Zittern sollte dann mit
    der Zahl der beteiligten Punkte fallen [H].
- **Abschaetzung:** weiter. Folge: Welle und Q-Ball auf der Kausalmenge (Ueberleitung 3, siehe
  UEBERLEITUNGEN-EMERGENZ.md).
- 2026-10-04 05:17:34 CEST: Finn: "Ideate drei Überleitungen zu einer emergenten Theorie". Ideation der Leitung in RUNDE-37/UEBERLEITUNGEN-EMERGENZ.md.
- 2026-10-04 05:22:35 CEST: Freier Platz nach KAUSAL-SWERVE-1: INDUZIERT-1 gestartet (Ueberleitung 1, Spuren cpu3 und cpu4, Zeitbox 150 min). Drei Ueberleitungen als E1 bis E3 in den Pool (Sicherung pool.jsonl.bak-20261004-emergenz). Aktive Agenten 5 von 5: QB-BS-2D, KITAEV-DIAMANT-1, REGGE-WELLE-SCHIEF-1, Kurzpruefer Seite, INDUZIERT-1.
- 2026-10-04 05:27:24 CEST: Kurzpruefer (GEGENLESEN-6-KURZ.md): OK, keine Auflagen; alle neun Teilpunkte von F1 bis F4 erledigt und
  richtig. Kopf- und Fusszeile wie vorab geprueft ersetzt.
  - Seite als Fassung 7 veroeffentlicht, "Entwurf" entfallen.
  - Freigestellte Glaettungen nicht uebernommen; sie braeuchten einen neuen Blick.
- 2026-10-04 05:27:24 CEST: Freier Platz nach dem Kurzpruefer: KAUSAL-WELLE-1 gestartet (Ueberleitung 3, Zeitbox 120 min).
  - Spuren cpu7 und p4000a (geteilt). cpu7 ist neu im Kleintest-Starter (.69 und Laptop-Kopie, Sicherung
    kleintest.sh.bak-20261004-cpu7, atomar per mv).
  - Aktive Agenten 5 von 5: QB-BS-2D, KITAEV-DIAMANT-1, REGGE-WELLE-SCHIEF-1, INDUZIERT-1, KAUSAL-WELLE-1.

### Ernte QB-BS-2D (RUNDE-37/qb-bs-2d/ERGEBNIS.md; eingetragen 2026-10-04 05:30:02 CEST)

- Code-Agent, Plan eingefroren 05:16:50, Spuren cpu und cpu6. Gegengelesen an lauf-69/auswertung.json.
- **Urteile:**
  - QB0 eingetroffen; QB1, QB2 und QB3 nicht eingetroffen, auch nach Kartenwortlaut.
  - QB4 nach berichtigter Regel nicht eingetroffen, nach Kartenwortlaut eingetroffen.
    - Berichtigung: Bei G = 0 sind beide Ladungen einzeln erhalten, also nur Vergleich mit "ruhender Knoten plus Q-Ball".
    - Das Kartenminimum ueber alle Ladungsteilungen vergleicht mit unerreichbaren Zustaenden (Kartenfehler, vor dem
      Einfrieren offengelegt).
- **Kernbefunde (radial, 2+1, Modell B.5):**
  - G = 1 (phasengekoppelt): Der gemischte Zustand liegt immer ueber der getrennten Referenz.
    - kappa = 1: 8,2 bis 8,6 % (Kartenreferenz), 23,7 bis 24,0 % (vorsichtigere Referenz); kappa = 1/4: 10,2 bis
      11,1 %.
    - Gemischte Zustaende gibt es erst ab q = 72,5 bzw. 55.
    - Auf allen gilt Omega^2 > 1/2 (Minimum 0,664).
  - G = 0: Die Ladung haftet an einem ruhenden Knoten, mit hoechstens 1,9 % (kappa = 1) bzw. 1,45 % (kappa = 1/4)
    Bindung.
    - Selbstanzeige: Das Vorzeichen war vorab ableitbar (negativer Kreuzterm in U); neu ist nur die Groesse.
  - Nebenbefund: Der drehende Knoten existiert bei kappa = 1 bis Omega^2 ~ 1, weit ueber der Kartenschwelle.
- **Kontrollen:**
  - Verdopplung von N_r: <= 2,3e-10; Virial <= 1e-8; dE/dq = Omega (Median 1e-4).
  - Nullprobe D = 0 auf 1e-16; Bogomolny-Schranke erfuellt.
- **Selbstanzeigen:**
  - Energiewerte im Rauchlauf vor dem Einfrieren gesehen; die vorsichtigere Referenz kam danach, macht nur strenger.
  - Aufloesung vor dem Einfrieren gesenkt.
  - QB0-Punkt omega = 0,761 statt 0,75.
  - Nur kreisrunder Ansatz; S3 und S4 fehlen.
- **Bedeutung:**
  - Der Weg "Knoten haelt Ladung im Gleichtakt" (C x S^2 mit Paarkopplung) ist in radialer 2D-Form nicht offen.
  - Ohne Gleichtakt haftet die Ladung schwach (~2 %), ueber das gemeinsame Potential.
  - Den Spin selbst prueft 2+1 nicht.
- **Abschaetzung:** parken.
  - G = 1 radial verworfen.
  - G = 0 (schwache Haftung) nur weiter, wenn der C x S^2-Weg wieder Vorrang bekommt; dann S3 (nicht kreisrund) bei
    G = 0.
  - Naechster Spin-1/2-Weg: H2 (Ladung plus Monopol) als Literaturkarte.
- 2026-10-04 05:31:17 CEST: Freier Platz nach QB-BS-2D: LADUNG-MONOPOL-L gestartet (feldforscher, H2, hoechstens 15 Abrufe, Zeitbox 60 min). Aktive Agenten 5 von 5: KITAEV-DIAMANT-1, REGGE-WELLE-SCHIEF-1, INDUZIERT-1, KAUSAL-WELLE-1, LADUNG-MONOPOL-L. Vorgemerkt: GLEICHER-KEGEL-1 (Skalar- gegen Graviton-Dispersion im schiefen Netz), sobald REGGE-WELLE-SCHIEF-1 und INDUZIERT-1 (IN0) vorliegen.

### Ernte KITAEV-DIAMANT-1 (RUNDE-37/kitaev-diamant-1/ERGEBNIS.md; eingetragen 2026-10-04 05:45:29 CEST)

- Code-Agent, Plan eingefroren 05:36:20, Spur p4000a, 2 von 5 Abrufen (Ryu 2009, PDF als Bild gelesen). Gegengelesen an
  lauf-69/auswertung.json.
- **Urteile:** KD0, KD1, KD2 und KD3 eingetroffen (synthetisch, vorab ableitbar).
  - KD2 mit der vorab festgelegten Wahl J0 = 4; bei der Lesart J0 = 2 waere es nicht eingetroffen.
  - KD3 nach Kartenwortlaut nicht auswertbar: Die Quelle nennt keine String-Operatoren; der Agent hat sie nach Levin/Wen
    aus den Huepfern gebildet.
- **Kernbefunde (Ryus Gamma-Matrix-Modell, Diamantgitter, vier Striche je Knoten):**
  - Das Spinmodell ist exakt gleichwertig mit zwei Majorana-Sorten, die in einem statischen Z_2-Feld huepfen.
    - Kleine exakte Diagonalisierungen (4096 bzw. 256 Zustaende) treffen die Majorana-Vorhersage auf ~1e-10.
    - Vertauschte Flusszuordnung gibt 2,2 bis 2,5, der Test trennt also.
  - Erhalten: Fluesse durch die Sechserringe und eine globale U(1)-Ladung; beide Sorten bilden ein komplexes Fermion.
  - Spektrum bei gleichen Kopplungen: keine Luecke, Nullstellen auf Linien (X-W). Volumensteigung 1,78; Linien geben
    ~2, Punkte 3.
  - Luecke genau dann, wenn eine Kopplung groesser ist als die Summe der drei anderen; Luecke = J0 - 3 (13 Werte auf
    1e-16).
  - Vertauschungsphase der Huepfer beider Sorten -1 (3072 von 3072 lokal, 301 von 301 lang). Das gebundene Paar beider
    Sorten ist ein Boson (+1). Die Durchgangsprobe kann +1 liefern.
- **Kartenberichtigungen (vor dem Einfrieren):**
  - Je Bindung zwei Terme, also zwei Majorana-Sorten.
  - KD2-Bedingung "groesser als die Summe der anderen drei".
  - Eq. (24)/(25) der Quelle passen nicht im selben Sektor mit demselben Vorzeichen; fuer H ohne Folgen.
- **Selbstanzeigen:**
  - Ein Code-Fehler im Rauchlauf 1 (Ganzzahltyp) wurde berichtigt.
  - Volumenanteil nach den Rauchlaeufen auf N = 257 umgestellt; die Rauch-Steigung 1,54 lag nahe der Schwelle 1,5.
  - J0 = 4 gewaehlt, als J0 > 3 schon bekannt war.
  - Lokal tr, wc und head als Filter benutzt; auf der .69 Dateiverwaltung und ls ausserhalb des Starters.
- **Grenzen:**
  - Nur Z_2, kein Photon; die U(1) ist global, nicht geeicht.
  - Flussfreier Grundzustand nur fuer L >= 5 getestet (Liebs Satz ist in 3D nicht bewiesen); L = 4 und L = 6 bei J = 1
    sind Ausnahmen (Endlichkeit [H]).
- **Bedeutung [L/H]:**
  - Auf einem Netz mit Tetraederknoten entstehen aus reinen Spins exakt Fermionen plus ein Z_2-Eichfeld.
  - Fuer Ueberleitung 2 fehlen noch das Photon (U(1)) und echte Spin-1/2-Drehung; Kandidat ist LADUNG-MONOPOL-L (laeuft).
- **Abschaetzung:** erledigt. U(1)-Schritt erst nach LADUNG-MONOPOL-L.
- 2026-10-04 05:46:36 CEST: Freier Platz nach KITAEV-DIAMANT-1: HAGEDORN-1 gestartet (Glied 7, aus der Warteschlange seit RUNDE-36; Karte geschaerft: Ringschwingungen statt Zustandszaehlung, die vorab ableitbar waere). Spuren cpu und cpu6, Zeitbox 120 min. Aktive Agenten 5 von 5: REGGE-WELLE-SCHIEF-1, INDUZIERT-1, KAUSAL-WELLE-1, LADUNG-MONOPOL-L, HAGEDORN-1. Pool: B3 auf karte, H9 auf gerechnet (Sicherung pool.jsonl.bak-20261004-hagedorn).
- 2026-10-04 05:52:47 CEST: Finn: "Überleg was wir am besten jetzt machen sollen welche Ideen weiter entwickeln?" und "Wie können wir ggf die spins mit space time symetrien und emergenten Mustern und ggf Ansätzen von Game of Life oder simpligizierungen finden". Antwort der Leitung in RUNDE-37/STRATEGIE-SPIN-20261004.md.

### Ernte REGGE-WELLE-SCHIEF-1 (RUNDE-37/regge-welle-schief-1/ERGEBNIS.md; eingetragen 2026-10-04 05:53:01 CEST)

- Code-Agent, Plan eingefroren 05:32:52, Spuren cpu5 und p4000b. Gegengelesen an lauf-69/auswertung.json.
- **Urteile:**
  - WS0 bis WS5 nach Kartenwortlaut eingetroffen.
  - In der vor dem Einfrieren festgelegten Zensuslesart sind WS3 und WS4 nicht eingetroffen. Kartenluecke K1: "nahe der
    reellen Achse" sieht die neue Mode nicht.
- **Kernbefunde (schiefes 4D-Kuhn-Netz, s = 0,1 und 0,2):**
  - Lange Wellen laufen mit c: zwei TT-Moden, reell, abs(v - 1) <= 5,1e-4 bei abs(k) = 0,05.
  - Doppelbrechung bei kurzen Wellen: Aufspaltung bei s = 0,2 und abs(k) = 0,8 zwischen 1,5e-3 und 6,2e-2, in allen 24
    Richtungen.
    - Die exakte Wuerfelgitter-Formel gilt nicht mehr.
  - Schneller als Licht bei s = 0,2 in einzelnen Richtungen, fuer eine Polarisation: v = 1,00355 (0,4) und 1,01002 (0,8);
    der Langwellen-Grenzwert bleibt 1. Bei s = 0,1 ist v ueberall < 1.
  - Die Diagonalmode wird eine eigene Gitterwelle, die je Zeitschritt das Vorzeichen wechselt (Im omega = +-pi), an 229
    von 240 Punkten.
    - Sie ist schwer bei s = 0,1 und leicht bei s = 0,2.
  - An 11 Punkten mit s = 0,2 kippt das Vorzeichenmuster; an 10 davon gibt es rein anwachsende Wurzeln (abs(Im omega) =
    2,57 bis 3,10 je Zeitschritt). Das Netz ist dort instabil.
- **Kontrollen:**
  - s = 0 bitgleich mit REGGE-WELLE-1.
  - Unabhaengiger Ableitungsweg <= 5,7e-9 abs(k); Inversion und Zeitumkehr <= 3,1e-12.
  - Zensus bei s = 0: genau 2 intrinsische Wurzeln.
- **Selbstanzeigen:**
  - Zwei Fehler im Zensusteil vor dem Einfrieren behoben.
  - Rauchlaeufe machten WS2 und die Zensuslesarten absehbar.
  - Eigene Vorhersagen A3 und A9 verfehlt.
  - Nicht gerechnet: ein wirklich zufaelliges Netz.
- **Bedeutung:**
  - Fuer lange Wellen ist das schiefe Netz so gut wie der Kristall.
  - Bei kurzen Wellen verraet es seine Unordnung: Doppelbrechung, teils schneller als Licht, eine Zusatzwelle und bei
    staerkerer Schiefe Instabilitaet.
  - Fuer Finns Schaumbild und Ueberleitung 1: Vor "ungeordnet ist besser" muss die Stabilitaet zufaelliger 4D-Netze
    geprueft sein (REGGE-4D-ZUFALL, geparkt wegen Groesse).
- **Abschaetzung:** erledigt. Folge nur mit Grund: Stabilitaet zufaelliger Netze, falls Ueberleitung 1 traegt
  (INDUZIERT-1).
- 2026-10-04 05:55:52 CEST: Freier Platz nach REGGE-WELLE-SCHIEF-1: QCA-TETRA-1 gestartet (Finns Spin-Frage; Spuren cpu5 und p4000b, Zeitbox 120 min). INDUZIERT-1 per Nachricht um beschreibende Richtungsabhaengigkeit gebeten (Leitungszusatz). Pool H11 bis H13 (Sicherung pool.jsonl.bak-20261004-spinregeln). Aktive Agenten 5 von 5: INDUZIERT-1, KAUSAL-WELLE-1, LADUNG-MONOPOL-L, HAGEDORN-1, QCA-TETRA-1.
- 2026-10-04 05:58:48 CEST: Schleifendurchlauf. Tagespflichten: index-pruefen und karten-pruefen ohne Verstoesse, Index zusaetzlich gesichert und zur .69 kopiert (die Tagessicherung lief schon 00:05). Codex: keine neue Nachricht. Papier-I-Absatz als Entwurf geschrieben (RUNDE-37/PAPIER-I-ROBUSTHEIT-ENTWURF.md) und Codex per Peerbus angeboten (kind result).

## Abschluss Runde 37 (eingetragen 2026-10-04 06:00:21 CEST)

| Karte | Ausgang kurz | Abschaetzung |
|---|---|---|
| KAUSAL-1 (Leitung) | alle vier eingetroffen (Grad berichtigt); Raumzeit-Netz ohne Ruhesystem hat keine festen Nachbarn | erledigt |
| PONZANO-1 | PO0 bis PO2 ja, PO3 nein; Regge-Wirkung in der Phase der 6j-Symbole, Pachner 2-3 exakt (Literatur) | erledigt; EPRL-Literaturkarte geparkt |
| V-1-PRAEZISION | PR2, PR3 ja; PR0, PR1 nein; Leck bis 1e-49 aufgeloest, Polabstand pi auf 0,28 % | erledigt; Absatz fuer Papier I als Entwurf an Codex |
| CDT-HORAVA-L | wo lambda in CDT bestimmt ist, liegt es nicht bei Einstein (2D < 1, 2+1 < 1/2); zwei Lager | erledigt |
| REGGE-ZEIT-1 | Z0 ja; Z1 bis Z3 nein; fern der Masse Newton und gamma = 1, nah einige Prozent zu hoch | erledigt; Folge REGGE-4D-SCHIEF-1 |
| QBALL-PYRO-1 | QP0, QP1, QP4 ja; QP2, QP3 nein; Ringe ueber dem flachen Band zerfallen, im Band stabil | erledigt; geparkt |
| REGGE-4D-SCHIEF-1 | SC0 bis SC2 ja, SC3 nein; die Diagonale wird eine Mode mit negativer Steifigkeit | erledigt |
| SPIN-HOPF-L | E1, E2 ja; E3, E5 teilweise; E4 nicht pruefbar; Projektvorarbeit gefunden; Vorschlag QB-BS-2D | erledigt |
| QBALL-LADUNG-1 (Leitung) | QL0, QL1 ja (Delta E ~ e^2, Steigung 1,998); QL2, QL3 nicht auswertbar (Schiessverfahren) | QL2 geparkt (Relaxationsloeser) |
| STRINGENDE-1 | SE0 bis SE3 ja (vorab ableitbar); Stringenden als Fermionen (2D e x m, 3D Levin/Wen) | erledigt |
| REGGE-WELLE-1 | W0 bis W3 ja (W3 nach Kartenwortlaut nein, K1); Schwerewellen mit c, zwei Polarisationen, exakte Wuerfelgitter-Formel | erledigt |
| KAUSAL-SWERVE-1 | KS0 (berichtigt), KS3 ja; KS1, KS2 nein (Rand); innen keine Reibung, Zittern 1/4 je Schritt, Heizen | erledigt; Folge KAUSAL-WELLE-1 |
| QB-BS-2D | QB0 ja; QB1 bis QB3 nein; QB4 berichtigt nein; Ladung im Gleichtakt nicht gebunden, ohne Gleichtakt ~2 % | geparkt |
| KITAEV-DIAMANT-1 | KD0 bis KD3 ja (vorab ableitbar); Majoranas plus Z_2 auf dem Diamantnetz | erledigt |
| REGGE-WELLE-SCHIEF-1 | WS0 bis WS5 nach Wortlaut ja; Zensus WS3, WS4 nein; Doppelbrechung, teils > c, Zusatzwelle, Instabilitaet bei s = 0,2 | erledigt |
| Schreibtisch | RAUMZEIT-NETZ.md, GEN-04-SPIN-HALB.md, UEBERLEITUNGEN-EMERGENZ.md, STRATEGIE-SPIN-20261004.md, PAPIER-I-ROBUSTHEIT-ENTWURF.md | erledigt |
| Anschauungsseite "Die ½-Regel" | Fassung 7 nach fuenf Lesungen und Kurzpruefung, "Entwurf" entfallen | erledigt |
| uebernommen nach Runde 38 | INDUZIERT-1, KAUSAL-WELLE-1, LADUNG-MONOPOL-L, HAGEDORN-1, QCA-TETRA-1 | laufen |

### Einfach gesagt (Runde 37)

In dieser Runde ging es darum, wie Finns Netz in Raum und Zeit aussehen muss und woher Teilchen mit halbem Spin kommen
koennten. Im Netz aus Laengen laufen lange Schwerewellen genau mit Lichtgeschwindigkeit; ein verzogenes Netz zeigt bei
kurzen Wellen Fehler und wird stellenweise instabil. Ein zufaelliges Netz aus Raumzeit-Punkten bremst Teilchen nicht,
laesst Punktteilchen aber stark zittern; Teilchen muessen dort also ausgedehnt sein. Elektronenartige Teilchen entstehen in
Gittermodellen als Enden von Faeden oder aus Spins auf Tetraederknoten, ein an einem Knoten klebender Q-Ball dagegen
nicht. Die meisten Ergebnisse waren aus der Literatur ableitbar; offen und entscheidend sind die laufenden Tests zur
Schwerkraft aus Materie und zum halben Spin aus einfachen Quantenregeln.
