# DOPPELSPALT-L: Dossier (feldforscher, Finn-Auftrag "alternative Ideen zum Doppelspaltexperiment")

- Start 2026-10-05 05:06:38 CEST (date), Dossier ab 05:27:22 CEST (date). Karte: KARTE.md (DS1 bis DS5 unveraendert).
- Abrufe: 10 von 10 verbraucht (A1 Fehlschlag HTTP 429, A4a HTTP 404 mitgezaehlt), Websuche 2 von 2 (beide liefen).
  Protokoll mit Erwartung vor jedem Abruf: ARBEITSFELD.md, Abschnitt 3. Quellenkopie: quellen/A4-...pdf (Darrow/Bush).
- Kennzeichen:
  - [S] an der Quelle gelesen, mit Abschnitt bzw. Gleichung
  - [S Abstract] Abstract gelesen; "(Zus.)" heisst: nur ueber die WebFetch-Zusammenfassung, Wortlaut nicht garantiert
  - [L] Literatur aus dem Gedaechtnis, bibliografisch sicher, in diesem Lauf nicht gelesen
  - [L?] unsicher, oder nur aus einer Suchmaschinen-Zusammenfassung
  - [M] Vorab-Entscheidung der Leitung (Karte)
  - [ES] eigener Schluss
  - [H] Hypothese

## 1. Ergebnis zuerst

1. **Klassische Pilotwellen koennen Fraunhofer-Muster erzeugen, allerdings nur im Modell und mit der falschen Laenge.**
   - Darrow und Bush (PRR 7, 033288, 2025) treffen mit einem klassischen Lagrange-Modell Einzel- und
     Doppelspalt-Fraunhofer: chi^2/nu = 1,36 bzw. 0,89, gegen 17,6 bzw. 11,0 fuer einen Gauss [S Abschn. III].
   - Das Modell: Teilchen mit Compton-Zitterbewegung im Klein-Gordon-Feld.
   - Die Streifenlaenge ist aber lambda_eff = (b/68)^2 lambda_dB [S Gl. (3)], also nicht h/p, und gilt nur fuer
     langsame Teilchen [S Fig. 7b].
   - Tropfen-Experimente bleiben bei "nein" [S Abstract (Zus.), Ellegaard/Levinsen 2020].
2. **Der Pruefstein heisst I3, und Nichtlinearitaet macht I3 != 0. Das ist inzwischen gemessen, nicht nur gerechnet.**
   - Namdar u. a. (arXiv:2112.06965) zeigen experimentell: "nonlinear evolution can in fact lead to higher-order
     interference" [S Abstract].
   - Beste gefundene Einzelphotonen-Schranke: 3,96(523) x 10^-4 (Vogl u. a. 2021) [S Abstract (Zus.)].
   - Jedes Q-Ball- bzw. Soliton-Teilchenmodell muss I3 in der Einzelteilchen-Statistik klein halten.
   - Fuer massive Teilchen ist die Latte vermutlich nur ~1e-2 [L?].
3. **Welche Laenge setzt beim klassischen Q-Ball die Streifen? Auf dem Papier ist das nicht die de-Broglie-Laenge.**
   - Die innere Phase eines bewegten Q-Balls hat die Wellenlaenge 2 pi/(gamma omega v).
   - Die Quantenmechanik des ganzen Balls verlangt 2 pi/(gamma M v).
   - Das Verhaeltnis M/omega liegt zwischen Q und 1,41 Q (im Projektmodell) [ES, Abschn. 6]. Bei klassischem
     Q >> 1 ist die Phasenwelle also Q-mal zu lang.
   - Molekuel-Interferometrie bestaetigt h/(M v) mit der Gesamtmasse [L].
   - Darrow/Bush zeigen aber, dass auch eine dritte, kopplungsabhaengige Laenge herauskommen kann. Nur eine Rechnung
     entscheidet.
4. **Soliton-Doppelspalt ist nicht ganz neu.**
   - Es gibt ein "soliton interference model" (arXiv:1508.06837): Ein Soliton teilt sich an den Spalten und vereint
     sich wieder; das Muster verschwindet, wenn der Spaltabstand groesser als das Soliton ist [L?, nur
     Suchmaschinen-Zusammenfassung].
   - Es gibt auch GPE-Wellenpakete im Doppelspalt (2005, 2016) [S Abstract (Zus.)].
   - Einen Q-Ball-Doppelspalt mit dem Vergleich omega gegen M habe ich nicht gefunden, also nach Recherchestand nicht
     belegt.
   - Er hat aber genau de Broglies Zutat: eine innere Schwingung, mit der er die Zeitdehnung erklaert und auf

## 2. Urteile DS1 bis DS5

| Nr | Erwartung (Karte, unveraendert) | Urteil | Beleg |
|---|---|---|---|
| DS1 | Nachpruefungen des Tropfen-Doppelspalts fanden kein quantenartiges Muster (80 %) | **eingetroffen, mit Nuance** | Ellegaard/Levinsen 2020: "the answer is no" [S Abstract (Zus.)]. Darrow/Bush 2025 ueber die Nachpruefungen: Couder/Fort "contested on statistical grounds [13,14]" (Andersen 2015, Bohr 2016), "more refined, repeatable experiments [15,16] reveal quantitatively different diffraction patterns", "coherent double-slit diffraction patterns have been observed" [15 = Pucci 2018, 16 = Ellegaard/Levinsen 2020], "relatively sharp peaks" [S Einl., Abschn. IV, Anh. A]. Andersen 2015 und Pucci 2018 selbst nicht gelesen. |
| DS2 | Sinha 2010 <= 1e-2, spaeter <= 1e-3 (70 %) | **eingetroffen in der Groessenordnung, knapp** | Vogl u. a. 2021 (Einzelphotonen, hBN): 3,96(523) x 10^-4, 1-sigma-Grenze ~0,9e-3, 2 sigma ~1,4e-3 [S Abstract (Zus.)]. Conlon u. a. 2023: kappa = 0,002 +- 0,004 [S Abstract (Zus.)]. Sinha 2010 "< 1e-2" nur [L] und Projekt (gitter-checkliste.json W3 [S]). Schaerfer als 4e-4 im 24-Monats-Fenster: nicht gefunden. |
| DS3 | Keine Arbeit rechnet ein Q-Ball-artiges Soliton im Doppelspalt mit omega gegen M (55 %) | **nicht entschieden, Tendenz verfehlt** | Soliton-Interferenzmodell arXiv:1508.06837 mit Teilen und Vereinen, Phasen- und Frequenzabhaengigkeit [L?, nicht gelesen]. GPE-Wellenpakete im Doppelspalt: Nakamura u. a. 2005, Ngek u. a. 2016 [S Abstract (Zus.)]. Der genaue Vergleich omega gegen M ist in nichts Gelesenem enthalten. Websuche W2 ohne 2024-26-Treffer dazu, also nach Recherchestand nicht belegt. |
| DS4 | Nichtlineare Abwandlungen geben im Allgemeinen I3 != 0 (70 %) | **eingetroffen, aber mit anderer Belegbasis** | Namdar u. a. 2021, Experiment: "this is only true under specific assumptions, typically single-particles undergoing linear evolution. Here we experimentally show that nonlinear evolution can in fact lead to higher-order interference" [S Abstract]. Kanthak u. a. 2024: Sorkin-Parameter != 0 fuer ein GPE-Kondensat [W1-Zusammenfassung, L?]. Sorkin 1994 und Ududec u. a. 2011 sind Mass- bzw. GPT-Rahmen, keine Aussagen ueber nichtlineare QM [L]. |
| DS5 | Margalit 2015: Sichtbarkeit sinkt, wenn die innere Uhr den Wegzeitunterschied aufzeichnet (75 %) | **eingetroffen** | arXiv:1505.05765: "entanglement between the clock's time and its path yields 'which path' information, which affects the visibility of the clock's self-interference" [S Abstract (Zus.)]. |

**Bedeutung laut Karte, angewandt:**
- DS2 und DS4 sind eingetroffen. Damit gibt es eine datennahe Latte fuer unsere Teilchenmodelle (Abschn. 4 und 7).
- DS1 ist eingetroffen. Die Warnung gilt aber nur fuer Pilotwellen, die laufend abstrahlen wie die Tropfen.
  - Darrow/Bush nennen die Bedingung, unter der die Warnung entfaellt: Abstrahlung nur bei Beschleunigung, dazu Chaos
    [S Abschn. IV].
  - Fuer "das Netz fuehrt das Teilchen" ist das eine Auflage und kein Verbot [ES].
- DS3 ist nicht entschieden. QBALL-DOPPELSPALT-1 waere nur im Vergleich omega gegen M neu, und erst nach Lektuere von
  1508.06837.

## 2a. Erwartungsverstoesse (das eigentliche Ergebnis, wichtigste zuerst)

1. **V1/V2:**
   - Erwartet: Kein Modell im 24-Monats-Fenster trifft Fraunhofer, und wenn doch, dann mit der emergenten
     de-Broglie-Laenge.
   - Gefunden: Darrow/Bush 2025 treffen Fraunhofer mit lambda_eff = (b/68)^2 lambda_dB [S Gl. (3)].
   - Die eingebaute Compton-Uhr mit "harmony of phases" [S Abschn. II] legt die Streifenlaenge nicht fest. Sie folgt dem
     Impulsuebertrag Feld auf Teilchen, der mit b^2 geht [S Anh. B].
   - Korrigierte Erwartung: Innere Uhr allein reicht nicht fuer h/p.
2. **V5:**
   - Erwartet: "Nichtlinear gibt I3 != 0" sei nur Theorie.
   - Gefunden: Es ist gemessen (Namdar u. a., kohaerente Zustaende im nichtlinearen Medium) [S Abstract].
   - Folge: Der I3-Test trennt Born-Regel-Bruch und nichtlineare Evolution nur, wenn man die Staerke der
     Nichtlinearitaet variiert [ES].
3. **V6:**
   - Erwartet: Es gibt kein Soliton-Doppelspalt-Modell mit innerer Frequenz.
   - Gefunden: arXiv:1508.06837 (2015) [L?].
   - Dessen Kennzeichen d_max ~ Solitongroesse ist eine scharfe, pruefbare Vorhersage (Abschn. 3b).
4. **V3:**
   - Erwartet: Die zwei Merkmale des Modells seien Geschwindigkeitsfreiheit und Phasenharmonie.
   - Gefunden: (1) Lorentz-kovariante Abstrahlung nur bei Beschleunigung, (2) Chaos. Glatte Muster brauchen entweder
     nicht kreuzende Bahnen (Bohm) oder eine nicht differenzierbare Ablenkungsabbildung [S Prop. A1].
5. **V4:**
   - Erwartet: Die Tropfen-Nachpruefungen fanden "kein Muster".
   - Gefunden: Es gab kohaerente Doppelspaltmuster, aber quantitativ anders, mit scharfen Spitzen [S Darrow/Bush ueber
     15, 16].
6. **V8 (Gegensweep):**
   - Die Karte sagt "Sorkin/Dreifachspalt nicht im Projekt".
   - Doch: gitter-checkliste.json, W3 (Snapshot 09.09.), fuehrt den Dreispalt-Test als harte Messung, verknuepft mit
     dem inneren Uhren-Bild. Der Pruefpunkt "Rabi-Runner" steht dort als nicht erledigt [S].
7. **V7:**
   - Erwartet: Im 24-Monats-Fenster eine I3-Schranke von 1e-4 bis 1e-5.
   - Gefunden: keine. Die beste gefundene ist 4e-4 +- 5e-4 (2021) [S Abstract (Zus.)].
8. **V9:**
   - Nicht-klassische Pfade koennen den Sorkin-Parameter in Standard-QM gross machen: |kappa_max| ~ 0,2 in einem
     Materiewellen-Aufbau (Vieira u. a. 2017) [S Abstract (Zus.)]. Die Groesse ist dort anders definiert.
   - Fuer jede numerische I3-Rechnung braucht man deshalb einen linearen Kontrollarm mit gleicher Geometrie [ES].

## 3. Katalog alternativer Erklaerungen

| Erklaerung | Mechanismus | Vorhersage im Doppelspalt | Abweichung von der QM | Datenlage | Kennzeichen |
|---|---|---|---|---|---|
| Standard-QM (Referenz) | lineare Amplitude, Born-Regel | I2 != 0, I3 = 0 (idealisierte Pfadsumme); Streifen h/(M v) mit Gesamtmasse; ein Klick je Teilchen; D^2 + V^2 <= 1 | Referenz. Bei echten Spalten kappa != 0 durch nicht-klassische Pfade, auch linear | Einzelelektronen-Aufbau (Tonomura 1989; zitiert bei Darrow/Bush [29]); I3-Schranken Abschn. 4 | [L], [S Abstract] |
| de Broglie-Bohm | Teilchen plus Fuehrungswelle psi (linear), v = grad S/m | identisch mit QM im Quantengleichgewicht; Bahnen kreuzen nicht | nur ausserhalb des Gleichgewichts (Valentini) [L] | Kocsis u. a. 2011 (schwach gemessene mittlere Photonenbahnen) [L]; "surreal"-Debatte (ESSW 1992) [L] | [S Prop. A1 ueber Bohm], [L] |
| de Broglies Doppelloesung, Lagrange-Version (Darrow/Bush 2024/25) | Punktteilchen der Masse m, Quelle in reellem KG-Feld der Masse m, Kopplung b; Zitterbewegung bei gamma^-1 omega_c emergent; strahlt nur bei Beschleunigung | Fraunhofer-Form fuer 1 und 2 Spalte (chi^2/nu ~1); lambda_eff = (b/68)^2 lambda_dB | Laenge nicht h/p (b <~ 25 gueltig); Proportionalitaet nur u <~ 0,25 c; Langzeitstatistik "nicht quantenartig" erwartet; keine Verschraenkung | nur Modell (PRR 2025); keine Messung | [S] |
| Darrow 2025, Phasenkopplung | Teilchen koppelt an die komplexe Phase von phi | im Grenzfall u << c exakt Bohm, also Fraunhofer | Wellengeschwindigkeit geht gegen unendlich, "not a compelling example of local ... diffraction" | Modell (Found. Phys. 55, 13) | [S Fussnote 26] |
| Pilotwellen-Hydrodynamik (Couder/Fort 2006) | Tropfen plus Faraday-Welle mit Gedaechtnis, angetriebenes Bad | Muster mit Badwellenlaenge | Laenge ist eine Mediumseigenschaft, nicht h/p; scharfe Spitzen; abhaengig von nicht berichteten Parametern | Nachpruefungen: quantitativ anders (Pucci 2018; Ellegaard/Levinsen 2020 "no"); neu 2025: Primkulov u. a., Pucci u. a. (nur Titel) | [S] ueber Darrow/Bush, [S Abstract (Zus.)], Titel [L] |
| Stochastische Mechanik (Nelson) bzw. SED | Brownsche Bewegung mit Diffusion hbar/2m bzw. Nullpunktfeld | Nelson reproduziert die Schroedinger-Statistik, also wie QM | Mehrzeitkorrelationen (Nelson) [L?]; SED: Probleme bei nichtlinearen Systemen [L?] | kein trennender Doppelspalt-Befund gefunden; im Einteilchen-Doppelspalt nach Recherchestand nicht unterscheidbar | [L], [L?] |
| Groessing u. a., "superklassische Stromalgebra" | emergente QM aus subquantenartigen Stroemen | "absence of third order interferences in three-path systems" | keine angegeben | Theorie | [S Abstract (Zus.)] |
| Objektiver Kollaps (GRW/CSL) | stochastischer nichtlinearer Kollaps; Ensemble-Dynamik linear (Lindblad) | Sichtbarkeitsverlust waechst mit Masse, Trennung und Zeit; I3 = 0 im Ensemble [ES] | Sichtbarkeit bei grossen Massen | Molekuel-Interferometrie bis >25 kDa (Fein u. a. 2019) begrenzt Parameter [L] | [L], [ES] |
| Retrokausal bzw. Transaktion (Cramer; Zwei-Zustands-Vektor) | Angebots- und Bestaetigungswelle bzw. Vor- und Rueckwaertszustand | wie QM, auch verzoegerte Wahl | keine | Verzoegerte-Wahl-Experimente (Jacques u. a. 2007) QM-konform [L]: empirisch nicht unterscheidbar | [L] |
| Zellularautomat ('t Hooft) | deterministischer CA, Superdeterminismus | wie QM (behauptet) | keine zugaengliche | keine trennenden Daten; nicht unterscheidbar | [L] |
| Wolfram-Multiway (Gorard) | Verzweigung im Multiway-System, branchial space | wie QM (Pfadsumme) [L?] | keine benannt | Projekt: Born-Stelle Gl. 29 gelesen, Double-Slit-Notiz nur Titel (SEITENKARTE Z. 57, 74) | [S Projekt], [L?] |
| Quantenmass, Sorkin-Hierarchie und GPTs | Wahrscheinlichkeit als Mass ueber Historien; Stufe 2 = QM | Stufe-3-Theorien: I3 != 0 | I3 != 0; Bezug zur Tsirelson-Schranke (Henson 2014: "lack of third-order interference bounds violation of the CHSH-Bell inequality to 2.883") | I3-Schranken Abschn. 4; Dichtewuerfel (Dakic u. a. 2013) | [S Abstract (Zus.)], [L] |
| Nichtlineare QM (Weinberg 1989; log-NLS) | nichtlineare Schroedinger-Gleichung | I3 != 0 im Allgemeinen; Muster haengt von der Intensitaet ab [ES] | Superposition verletzt; ueberlichtschnelle Signale (Gisin 1990, Polchinski 1991) | Namdar u. a. (nichtlineares Medium, Experiment) [S Abstract]; Projekt W3 [S] | [S Abstract], [L] |
| Zitterbewegung bzw. innere Uhr (de Broglie 1924, Schroedinger 1930, Hestenes) | Teilchen traegt eine Uhr bei M c^2/hbar; bewegte Uhr gibt eine Phasenwelle der Laenge h/p | wie QM, wenn die Uhr bei der Gesamt-Ruheenergie tickt | Hestenes: Channeling-Resonanz (Catillon u. a. 2008) [L?] | Margalit 2015: Uhrzeit als Welcher-Weg-Zeuge senkt die Sichtbarkeit (QM-konform) [S Abstract (Zus.)] | [L], [S Abstract (Zus.)] |
| Soliton-Teilung und Vereinigung (arXiv:1508.06837) | lokalisiertes Soliton (breather-artig) teilt sich an zwei Spalten und vereint sich; Ausgangsrichtung haengt von Phase und Frequenz ab | Interferenzmuster in der Richtungsverteilung; Muster verschwindet fuer Spaltabstand > Solitongroesse | intrinsisches d_max (QM: Kohaerenz durch Praeparation gesetzt) | Atome 54 cm getrennt (Kovachy u. a. 2015) [L], also d_max mindestens 0,5 m fuer Rb | [L?], [ES] |
| Klassisches nichtlineares Feld (GPE-Wellenpaket) | das Feld selbst interferiert, Dichtestreifen | Streifenabstand ~ g^-1/2 (Nakamura 2005; g vermutlich Schwere) | Streifen im Feld, keine Einzelteilchen-Statistik; Laenge pro Konstituent [ES] | Rechnungen 2005, 2016 | [S Abstract (Zus.)] |

## 3a. Regime und Moderatoren (Feldregel 1 und 6)

**Zwei Regime:**
- **R-lin:** Interferenz als Eigenschaft einer linearen Amplitude mit Born-Regel.
  - Dazu gehoeren QM, Bohm, Nelson, Transaktion, CA und Multiway.
  - Alle geben im Einteilchen-Doppelspalt dieselbe Statistik.
- **R-nl:** Interferenz aus klassischer nichtlinearer Teilchen-Wellen-Dynamik.
  - Dazu gehoeren Tropfen, Darrow/Bush, Soliton-Teilung und GPE-Felder.
  - Diese Modelle stimmen in einzelnen Mustern ueberein, ohne die QM-Struktur zu haben.

**Moderatoren, die zwischen den Studien variieren:**

| Moderator | Wirkung | Quelle |
|---|---|---|
| Kopplung Teilchen-Welle b | lambda_eff ~ b^2 lambda_dB; Chaos setzt mit wachsendem b ein, erst an den Spaltraendern | [S Gl. (3), Fig. 6b] |
| Teilchengeschwindigkeit | lambda_eff ~ lambda_dB nur fuer u <~ 0,25 c | [S Fig. 7b] |
| Art der Abstrahlung | laufend (Tropfen: Andersen/Bohr-Vermutung greift) gegen nur bei Beschleunigung (Darrow/Bush: greift nicht) | [S Abschn. IV] |
| Antrieb und Gedaechtnis | unter- gegen ueberkritisches Faraday-Regime | [S Abstract (Zus.), Dunn u. a. 2025, nur Hinweis] |
| Spaltabstand gegen Teilchenausdehnung | Soliton-Teilung nur fuer d < d_max | [L?] |
| Nichtlinearitaet der Evolution | I3 != 0 | [S Abstract, Namdar] |
| Randbedingungen bzw. Nahfeld | I3 != 0 schon linear | [S Abstract (Zus.), De Raedt 2011; Sinha/Vijay/Sinha 2014] |
| Teilchenzahl M | Terme ab Ordnung 2M+1 verschwinden | [S Abstract (Zus.), Pleinert 2018] |

**Kopplung und Takt vor Bauteil (Feldregel 6):**
- Es gibt mindestens vier Wege zu Streifen:
  - Phase der linearen Amplitude
  - Badtakt (Faraday)
  - innere Compton-Uhr plus Feld
  - innere Soliton-Phase omega
- Die gemeinsame Groesse ist der **Takt der Phase, die entlang beider Wege transportiert und am Ende verglichen wird**.
- Die Daten legen ihn fest: Er tickt bei der Gesamt-Ruheenergie M c^2/hbar, denn die Streifen folgen h/(M v) bis zu
  Molekuelen von mehr als 25 kDa [L].
- Die Bauteile liefern verschiedene Takte:
  - Tropfen: Badtakt
  - Darrow/Bush: richtige Uhr, aber eine Laenge durch b verzerrt
  - klassischer Q-Ball: Takt omega pro Quant
- Die Kernfrage an jedes Teilchenmodell lautet darum "Welche Uhr zaehlt?", nicht "welches Bauteil fuehrt" [ES].

## 3b. Unterscheidungspunkte (Feldregel 2)

| Paar | Wo laufen sie messbar auseinander? | Zugaenglich? |
|---|---|---|
| QM gegen Bohm, Nelson, Transaktion, CA, Multiway | nur ausserhalb des Quantengleichgewichts bzw. bei Mehrzeitkorrelationen; im Einteilchen-Doppelspalt nirgends | **empirisch nicht unterscheidbar** im Doppelspalt [ES] |
| QM gegen Darrow/Bush | (i) Streifenlaenge gegen h/p bei Variation von b bzw. bei u > 0,25 c; (ii) Langzeitstatistik; (iii) I3 bei drei Spalten (nicht gerechnet); (iv) Mehrteilchen-Verschraenkung (lokal unmoeglich) | im Modell sofort; Laborgegenstueck fehlt |
| QM gegen Tropfen | Tropfenmasse bei festem Bad variieren: QM-Analogon verlangt lambda ~ 1/(M v), Tropfen behalten die Faraday-Laenge [ES] | im Analoglabor |
| QM gegen Soliton-Teilung | Spaltabstand ueber die Teilchenausdehnung hinaus | zugaenglich und schon gemessen: 54 cm (Kovachy 2015) [L] |
| QM gegen klassischen Q-Ball mit Phasenstreifen | Streifenlaenge lambda_omega = (M/omega) lambda_M, mit M/omega ~ Q | Molekuel-Interferometrie mit Gesamtmasse [L] |
| QM gegen nichtlineare QM | I3 als Funktion der Intensitaet bzw. Nichtlinearitaet. Born-Bruch: I3 unabhaengig von der Intensitaet; nichtlineare Evolution: I3 waechst mit ihr [ES] | zugaenglich (Namdar-Aufbau) |
| QM gegen Kollaps (GRW/CSL) | Sichtbarkeit gegen Masse^2, Trennung und Flugzeit | teilweise; Molekuele >25 kDa [L] |
| klassische gegen quantenmechanische innere Uhr | Klassische Uhr: deterministischer Phasenversatz, durch Nachsortieren nach Uhrstand umkehrbar. Quantenuhr: Sichtbarkeitsverlust durch Verschraenkung, nur durch Loeschen umkehrbar (Margalit) [ES] | zugaenglich (Margalit-Aufbau mit Nachsortierung) |

## 4. Experimente, die trennen (mit Zahlen)

- **I3-Schranken:**
  - Sinha u. a. 2010: Photonen, < 1e-2 [L]; im Projekt als W3 gefuehrt [S].
  - Vogl u. a. 2021: Einzelphotonen aus hBN, 3,96(523) x 10^-4 [S Abstract (Zus.)].
  - Conlon u. a. 2023: kohaerente Zustaende, Homodyn, kappa = 0,002 +- 0,004 [S Abstract (Zus.)].
  - Kanthak u. a. 2024: BEC-Vorschlag, "upper bound of 5.7 x 10^-3 on the statistical deviation" (Status nicht
    geprueft) [S Abstract (Zus.)].
  - Massive Teilchen: Cotter u. a. 2017 (Molekuele) [L?, Zahl nicht geprueft].
  - Mehrteilchen-Variante: Pleinert u. a. 2018, "exponentially more sensitive" [S Abstract (Zus.)].
  - **Stoerterme:**
    - nicht-klassische Pfade, |kappa_max| ~ 0,2 in einem speziellen Aufbau (Vieira 2017) [S Abstract (Zus.)]
    - Gouy-Phase (da Paz 2015) [S Abstract (Zus.)]
    - Nichtlinearitaet (Namdar) [S Abstract]
- **Molekuel-Interferometrie:**
  - C60 (Arndt u. a. 1999) [L]; mehr als 25 kDa bzw. ~2000 Atome (Fein u. a. 2019) [L].
  - Streifen folgen h/(M v) mit der Gesamtmasse [L].
  - Das trennt "Takt pro Konstituent" von "Takt der Gesamtmasse".
- **Innere Uhr:**
  - Margalit u. a. 2015, Atomuhr aus zwei Spinzustaenden: Die Uhrzeit traegt Welcher-Weg-Information und senkt die
    Sichtbarkeit [S Abstract (Zus.)]; Zahlen nicht gelesen.
  - Vorschlag Zych u. a. 2011 [L].
- **Schwache Messung:**
  - Kocsis u. a. 2011: mittlere Photonenbahnen im Doppelspalt, kreuzungsfrei [L].
  - Nach Darrow/Bush Prop. A1 kreuzen dagegen die Einzelbahnen ihres Modells [S].
  - Trennend ist erst der Vergleich des gemessenen mittleren Stroms mit j/rho. Die mittlere Stroemung eines chaotischen
    Modells muss j/rho nicht treffen [ES].
- **Welcher-Weg:**
  - Englert 1996: D^2 + V^2 <= 1 [L].
  - Duerr, Nonn, Rempe 1998: Welcher-Weg ueber innere Atomzustaende ohne Impulsstoss [L].
- **Verzoegerte Wahl, Talbot-Lau, Kapitza-Dirac:**
  - Jacques u. a. 2007 [L]; KDTLI-Molekuel-Interferometer [L?]; Kapitza-Dirac mit Elektronen (Freimund u. a. 2001) [L].
  - Keines davon trennt R-lin-Deutungen voneinander. Alle sind Latten fuer R-nl-Modelle [ES].
- **Grosse Trennung:**
  - Kovachy u. a. 2015: Wellenpakete bis 54 cm getrennt [L].
  - Das ist die Latte gegen jedes d_max-Modell.
- **Ein-Klick-Probe:**
  - Antikorrelation einzelner Photonen (Grangier/Roger/Aspect 1986) [L] und Ladungsquantelung.
  - Ein Teilungsmodell, dessen Haelften sich nicht immer vereinen, verletzt beides [ES].


- **Lokal kein Satz zur Materie-Interferenz bzw. zum Doppelspalt** [S]:
  - QUELLEN-DOSSIER W9: Interferenz der LEP-Kontaktwechselwirkung, nicht Doppelspalt.
  - "dilation is caused by internal oscillations within elementary particles. This was postulated by Louis de Broglie
    in 1924 [2] and was deduced by Erwin Schroedinger in 1930 [3] from the Dirac function"
  - "This internal oscillation is assumed to be circular in order to explain the spin and also the magnetic moment"
- **Anknuepfung [H]:**
  - De Broglies Arbeit von 1924 leitet aus genau dieser inneren Uhr und der "harmony of phases" die Materiewelle ab
    [L]. Darrow/Bush beziehen ihr Modell auf de Broglies Doppelloesung mit innerer Compton-Schwingung und auf die
    "harmony of phases" [S Abschn. I-II].

## 6. Bezug zum Programm [H]

**Finns Netz (das Netz traegt die Welle, das Teilchen ist eine Anregung).**
- Zwei Lesarten:
  - (i) Teilchen = lineares Quant des Netzes: R-lin, gewoehnliches Muster, I3 = 0 bis auf Randglieder [M, vorab
    entschieden].
  - (ii) Teilchen = lokalisierte nichtlineare Anregung, Netzwelle = Pilot: R-nl.
- Fuer (ii) liefert Darrow/Bush die Auflagen:
  - Lorentz-kovariante Abstrahlung nur bei Beschleunigung
  - Chaos
  - Kopplung, die lambda_eff = lambda_dB ergibt [S]
- Auf dem Netz gilt Lorentz-Kovarianz nur bis O((k l)^2). Ein gleichfoermig bewegtes Teilchen strahlt dort
  schwach (Gitterabstrahlung). Die Andersen/Bohr-Vermutung greift dann in kleiner Ordnung wieder [ES].
- Bell-Grenze lokaler Pilotwellen: unveraendert THEORIE-VFW 4.5. Darrow/Bush sagen selbst, ohne Nichtlokalitaet sei
  Verschraenkung unmoeglich [S Abschn. V].

**Q-Ball mit innerer Uhr (Projektmodell U(S) = S - S^2 + S^3/2, m = 1, omega zwischen 0,707 und 1)
[S PAPIER-I Z. 31-37, 64; RUNDE-09 Z. 341].**
- Bewegter Ball: phi = f(gamma(x - v t)) exp(-i omega gamma (t - v x)). Phasenwellenlaenge lambda_omega =
  2 pi/(gamma omega v), Phasengeschwindigkeit 1/v [ES, Lorentz-Transformation].
- QM des ganzen Balls: lambda_M = 2 pi/(gamma M v) mit M = E.
- Derrick-Skalierung in d Dimensionen gibt E - omega Q = (2/d) Integral |grad f|^2 > 0 [ES]. Mit der
  Stabilitaetsbedingung E < m Q folgt omega < E/Q < 1, also **Q < M/omega < Q/omega <= 1,41 Q** [ES].
- Bei klassischem Q >> 1 ist die innere Phasenwelle also Q- bis 1,41 Q-mal laenger als die de-Broglie-Laenge des
  Balls. Sie entspricht der Wellenlaenge eines einzelnen Quants der Energie omega, wie bei Dichtestreifen in
  Kondensaten (pro Atom) [ES].
- Folge: Ein klassischer Q-Ball kann h/(M v) nicht aus seiner Phase holen. Entweder kommt Interferenz von der
  quantisierten Schwerpunktbewegung (dann R-lin, Q-Ball nur als Teilchenstruktur, passend zu Finns Weiche "Q-Baelle nur
  fuers Teilchenmodell"), oder von einer dritten Dynamiklaenge wie bei Darrow/Bush. Das zu klaeren ist Rechnung A1 [H].
- Reichweite: Der Schwanz faellt wie exp(-kappa r) mit kappa = sqrt(1 - omega^2), zwischen 0 und 0,707. Ein
  stabiler Ball strahlt nicht (omega < m) und hat keine eigene Fernwelle durch den anderen Spalt.
  - "Spuert den zweiten Spalt" setzt d <~ R + wenige/kappa voraus [ES].
- Teilung am Spalt: Haelften mit Q1 + Q2 = Q, kontinuierlich. Ist Q die elektrische Ladung, widerspricht nicht
  wiedervereinte Teilung der Ladungsquantelung (G2) [ES].

- Innere Bewegung mit c ist eine de-Broglie-Uhr. Ob sie den richtigen Takt M c^2/hbar hat, ist offen (Abschn. 5) [H].

**Fluss-Eis (FLUSS-1, Licht als Eichfeld auf Pyrochlor)** [S RAUMZEIT-NETZ Z. 42; UEBERLEITUNGEN Z. 20]:
- Emergentes Licht ist im linearen Bereich R-lin.
- Jede Nichtlinearitaet des Eises erschiene als intensitaetsabhaengiges I3 (Namdar-Mechanismus).
- Die Latte dafuer ist kappa = 0,002 +- 0,004 bei kohaerentem Licht (Conlon 2023) [S Abstract (Zus.)], bei deren
  Leistung [H].

## 7. Anstoesse (5), je mit Ableitbarkeitsprobe und Testskizze

**A1: QBALL-DOPPELSPALT-1 (ausgearbeiteter Kartenvorschlag, unten).**

**A2: I3-PILOTWELLE-1.**
- Frage: Erfuellt das Darrow/Bush-Modell bei drei Spalten I3 = 0?
- Ableitbarkeitsprobe:
  - Papier: nein, chaotische Ablenkungsabbildung; es gibt keinen Satz, der Additivitaet erzwingt [ES].
  - Literatur: nicht gefunden, nach Recherchestand nicht belegt. Nur eine Suche "droplet slit" (23 Treffer, kein
    Dreifachspalt); keine gezielte 24-Monats-Suche mehr moeglich.
  - Projekt: nein.
- Testskizze:
  - Gl. (1) in 2D (KG plus Punktquelle), b = 16,7 und 25, Geometrie wie Fig. 3d plus dritter Spalt.
  - 7 Konfigurationen (A, B, C, AB, AC, BC, ABC) x 500 Stossparameter, auf der GPU gebuendelt (.69 Kleintest).
  - kappa mit Bootstrap.
  - Ehrliche Grenze [ES, grob]:
    - Bei ~250 Durchgaengen je Konfiguration ist kappa nur auf etwa +-0,05 bis +-0,1 aufgeloest (Stichproben- bzw.
      Quadraturfehler). Der Kleintest findet also nur grosse I3.
    - Fuer 1e-2 braucht man 1e4 bis 1e5 Laeufe.
    - Werten nur, wenn sich kappa zwischen 500 und 1000 Stossparametern um weniger als die Haelfte der Schwelle
      aendert.
- Vorhersage [H]: |kappa| > 0,1 bei b = 25. Kann scheitern.

**A3: UHR-PROBE-1 (reine Papierrechnung, 0 min).**
- Ein ungleich geteilter Q-Ball hat Haelften mit omega(Q1) != omega(Q2). Klassisch entsteht ein deterministischer
  Phasenversatz Delta phi = Integral (omega1 - omega2) dt, keine Sichtbarkeitsminderung wie bei Margalit.
- Ableitbarkeitsprobe: voll ableitbar aus omega(Q) des vorhandenen Q-Ball-Atlas. Im Duennwandbereich geht
  d omega/dQ gegen 0, der Versatz verschwindet fuer grosse Q [ES]. Literatur: Margalit [S Abstract (Zus.)].
- Testskizze: aus dem Atlas d omega/dQ fuer Q = 50 bis 500 ablesen; Delta phi fuer Delta Q/Q = 10 % und
  T = 2d/v tabellieren.
- Unterscheidungspunkt: Nachsortieren nach Uhrstand stellt die Streifen klassisch wieder her, quantenmechanisch nur
  durch Loeschen.

**A4: DMAX-LATTE-1 (Papier).**
- Teilungsmodelle (1508.06837, Q-Ball) brauchen eine Teilchenausdehnung von mindestens dem Wegabstand.
- Ableitbarkeitsprobe: ableitbar, keine Rechnung. Daten: 54 cm bei Rb (Kovachy 2015) [L], Elektronen-Biprisma
  (Abstand ~um) [L?].
- Testskizze:
  - Fuer ein Teilchen als Q-Ball R + n/kappa in Einheiten der Compton-Laenge des Feldquants ausdruecken.
  - Mit dem Wegabstand vergleichen; noetiges kappa angeben (fuer Elektronen ~1e-7 der Compton-Wellenzahl, falls
    Abstand ~10 um [ES, grob]).
  - Erwartung: Teilungsmodelle sind fuer Elementarteilchen ausgeschlossen, es sei denn, der Schwanz reicht
    makroskopisch weit.

**A5: FLUSS-EIS-I3-1 [H].**
- Laufen Wellenpakete des emergenten Lichts (FLUSS-1) durch eine Drei-Spalt-Maske, waechst kappa mit der Amplitude?
- Ableitbarkeitsprobe: Linear ist I3 = 0 bis auf Randglieder [M]; die Amplitudenabhaengigkeit braucht den
  nichtlinearen Teil des Eis-Hamiltonoperators, nicht ableitbar.
- Testskizze: vorhandener FLUSS-1-Code (nicht geprueft, ob vorhanden), 7 Maskenkonfigurationen, drei Amplituden,
  linearer Kontrollarm gleicher Geometrie. Unter 10 min, falls der Code existiert.

### Kartenvorschlag QBALL-DOPPELSPALT-1 (nur einer ausgearbeitet)

**Frage:**
- Erzeugt ein klassischer 2D-Q-Ball des Projektmodells (beta = 1/2) am Doppel- bzw. Dreifachspalt eine strukturierte
  Ablenkungsstatistik?
- Wenn ja: Folgt die Struktur der inneren Phase (lambda_omega ~ 1/(gamma v)) oder der Geometrie?
- Wie gross ist I3?

**Pflicht vor dem Start:**
- (a) arXiv:1508.06837 an der Quelle lesen (V6): Was ist dort schon gerechnet?
- (b) Projekt-grep "Doppelspalt|double.slit|Q-Ball.*Spalt".
- (c) Ausgangszustand je Gitter pruefen (Memory-Regel): Q-Ball-Profil aus dem Atlas, Ruhetest ohne Spalt, Ladung und
  Energie erhalten.

**Aufbau:**
- 2D, h = 0,25, Gebiet ~128 x 64, dt ~0,05.
- Wand: Zusatzpotential V_w |phi|^2 mit V_w = 4, Dicke 2.
- Spaltbreite w = R, Abstaende d in {R; 1,5 R; 3 R; 2R + 4/kappa}.
- omega in {0,80; 0,90}; v in {0,2; 0,3; 0,45}; 41 Stossparameter.
- Beobachtet je Lauf:
  - Ausgangsklasse (reflektiert / ein Spalt / geteilt / geteilt und wiedervereint)
  - Ablenkwinkel des groessten Ladungsstuecks
  - Ladungsanteile
- **Linearer Kontrollarm:** Klein-Gordon-Wellenpaket gleicher Breite und gleicher Geometrie. Er liefert das
  Rand-kappa (V9), gegen das der Q-Ball verglichen wird.

**Vorhersagen (vorab, jede kann scheitern):**
- **V-Q1 (Reichweite):** Fuer d = 2R + 4/kappa ist das Histogramm der offenen Spalte gleich der Summe der
  Einzelspalt-Histogramme, |I2|/Summe < 0,05.
  - Scheitert, wenn ein Fernmechanismus wirkt, z. B. Abstrahlung bei Beschleunigung als Pilotwelle.
- **V-Q2 (Takt):** Hat das Histogramm fuer d <= 1,5 R eine periodische Struktur, dann skaliert ihre Winkelperiode
  ueber v = 0,2 / 0,3 / 0,45 wie 1/(gamma v), innerhalb +-20 %.
  - Scheitert, wenn sie v-unabhaengig ist (Geometrie bzw. Chaos statt Phase).
  - Keine Struktur: Ausgang "kein Muster", ebenfalls zaehlbar.
- **V-Q3 (I3):** Fuer d <= 1,5 R ist |kappa| >= 0,05 nach Abzug des Rand-kappa aus dem Kontrollarm.
  - Scheitert, wenn |kappa| < 0,05 (die Ballstatistik waere dann effektiv additiv).
- **V-Q4 (Ein-Klick):** Fuer d <= R enden mindestens 20 % der durchgelassenen Laeufe mit zwei getrennten Stuecken
  von je >= 10 % von Q.
  - Scheitert, wenn der Ball fast immer einen Spalt waehlt oder sich vereint.

**Bedeutung (vorab):**
- V-Q2 bestanden: Die Phase der inneren Uhr steuert die Ablenkung, aber mit lambda_omega ~ Q lambda_M. Das ist die
  falsche Laenge fuer Teilchen mit Q >> 1.
- V-Q4 bestanden: Das Ein-Klick-Problem ist im Modell sichtbar.
- Beides zusammen: Interferenz gehoert nicht zum klassischen Q-Ball, sondern zur quantisierten Schwerpunktbewegung.
  Das stuetzt Finns Weiche, Q-Baelle nur fuer die Teilchenstruktur zu verwenden.
- V-Q2 gescheitert (v-unabhaengig): Es gibt kein de-Broglie-artiges Verhalten des klassischen Balls.

**Budget:**
- 2 x 4 x 3 x 41 = 984 Laeufe je Spaltkonfiguration, auf der GPU gebuendelt. Kleintest zuerst mit 1 omega,
  2 d, 2 v, 21 y (84 Laeufe) auf p4000 ueber kleintest.sh.
- Dreifachspalt (7 Konfigurationen) erst nach bestandenem Ruhetest.

**Konvergenzbindung (Schwellen an Gitter und Stichprobe gebunden):**
- V-Q1 und V-Q3 werden nur gewertet, wenn sich |I2|/Summe bzw. kappa zwischen 41 und 81 Stossparametern UND zwischen
  h = 0,25 und h = 0,125 um weniger als 0,02 aendern.
- Sonst ist der Ausgang "unentschieden", nicht "bestanden".

**Abbruch:** Verliert der Ball im Ruhetest ohne Spalt mehr als 1 % Ladung, wird nicht weiter ausgewertet.

## 8. Gegensweep, Kalibrierung, offene Fragen, Selbstanzeigen

**Gegensweep: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?**
- **G1 (geprueft):** "Das Projekt kennt Sorkin nicht".
  - Falsch. gitter-checkliste.json (Snapshot 09.09., Datei 07.09.) W3 [S]: "Die Quantentheorie ist linear
    (Superposition, Born-Regel)". Status hart; Messung "Dreispalt-Test des Sorkin-Parameters: Abweichung unter 1e-2
    bis 1e-3 (Sinha et al. 2010 und Nachfolger)"; Folgekandidat "Ein inneres Uhren-Bild muss als unitaere Dynamik
    formulierbar sein". Pruefung "Rabi-Runner", nicht erledigt.
  - Anstoss A3 knuepft dort an.
- **G2 (benannt, nicht geprueft):** "Ein Teilchen, ein Klick". Teilungsmodelle verletzen Antikorrelation und
  Ladungsquantelung, wenn die Haelften sich nicht vereinen. Daraus wurde V-Q4.
- **G3 (benannt):** "Photonen-I3 gilt fuer Teilchenmodelle".
  - Photonentests mit kohaerenten Zustaenden pruefen die Linearitaet des Lichtfelds plus Detektor.
  - Fuer massive Soliton-Teilchen zaehlen nur massive I3-Tests (Molekuele ~1e-2 [L?]).
  - Die Latte fuer Q-Ball-Teilchen ist also lockerer als die Photonenzahl.
- **G4, G5 (benannt):** Molekuel-h/(M v) und Kovachy 54 cm stammen aus dem Gedaechtnis [L], in diesem Lauf nicht
  abgerufen.

**Kalibrierung:**
- **(a) Gemessen:**
  - I3-Schranken (Photonen 2021, 2023)
  - nichtlineares I3 != 0 (Namdar)
  - Uhr als Welcher-Weg-Zeuge (Margalit)
  - Tropfen-Nachpruefungen "quantitativ anders"
  - Molekuel- und 54-cm-Daten [L]
- **(b) Nuetzlich verdichtet:**
  - Prop. A1: glatt heisst nicht-kreuzend oder chaotisch.
  - lambda_eff ~ b^2 lambda_dB ist ein Modellbefund, keine Messung.
  - M/omega zwischen Q und 1,41 Q [ES].
  - "Welche Uhr zaehlt?" als gemeinsame Takt-Groesse [ES].
- **(c) Gewachsene Gewissheit ohne neue Evidenz:**
  - Meine Ueberzeugung "klassische Q-Baelle erklaeren Interferenz nicht" ist im Lauf gestiegen. Sie stuetzt sich auf
    eine Papierrechnung und auf die Annahme, die Streifen kaemen aus der inneren Phase.
  - Darrow/Bush zeigen eine dritte, kopplungsabhaengige Laenge. **Warnzeichen:** Die Frage hat sich in drei Teilfragen
    aufgeloest (Laenge, Reichweite, I3), waehrend meine Sicherheit stieg.

**Offene Fragen:**
- O2: Welche Laenge setzt die Q-Ball-Statistik? Nur durch Rechnung A1 zu klaeren.
- O4: 1508.06837 lesen.
- O5: Zahlen und Zeitschriftenstatus von Namdar u. a.; Status Kanthak 2024.
- O6: I3 fuer klassische Pilotwellenmodelle, nach Recherchestand nicht belegt.
- O7: Massive I3-Schranken (Cotter 2017 u. a.) an der Quelle pruefen.

**Selbstanzeigen:**
1. A1 ist gescheitert (arXiv-API: HTTP 429 "Rate exceeded", vermutlich geteilt mit dem Scout), A4a lieferte HTTP 404.
   Beide sind als Abrufe gezaehlt.
2. A2, A5, A6, A8 und A9 sind nur ueber WebFetch-Zusammenfassungen gelesen. Zitate dort sind mit "(Zus.)" markiert,
   Wortlaut nicht garantiert. Direkt gelesen habe ich nur A3 (Abstract) und A4 (PDF S. 1-8).
3. W1- und W2-Suchmaschinentexte sind nicht zitierfaehig ([L?]). 1508.06837 ist nicht gelesen; DS3 ist darum
   vorlaeufig.
4. Andersen 2015 und Pucci 2018 nur als Sekundaerzitat bei Darrow/Bush.
5. Das Urteil "nicht belegt" fuer den Q-Ball-Doppelspalt stuetzt sich auf eine Websuche ohne Datumsfilter und eine
   arXiv-Suche. Die 24-Monats-Pruefung ist nur schwach erfuellt.
6. Die Karte nennt Sorkin/Ududec als Beleg fuer DS4. Ich bewerte DS4 mit anderen Quellen und habe die Erwartung selbst
   nicht geaendert.

### Quellenliste

**An der Quelle bzw. im Abstract gelesen (dieser Lauf):**
- Darrow D., Bush J. W. M. (2025), Single-particle Fraunhofer diffraction in a classical pilot-wave model, PRR 7,
  033288, https://arxiv.org/abs/2509.25574 ; Kopie quellen/A4-arxiv-2509.25574-darrow-bush-20261005-051209.pdf
  (S. 1-8, darin Refs [9], [13]-[16], [18], [20], [25], [27]-[30]).
- Ellegaard C., Levinsen M. T. (2020), Interaction of Wave-Driven Particles with Slit Structures,
  https://arxiv.org/abs/2005.12335 (PRE 102, 023115).
- Richardson C. D. u. a. (2014), On the analogy of quantum wave-particle duality with bouncing droplets,
  https://arxiv.org/abs/1410.1373
- Dunn E., Keshavarz B., Dowell E. (2025), Exploratory Study of Chaotic Behavior in Walking Droplets,
  https://arxiv.org/abs/2510.25073
- Hung C.-Y., Hsieh T.-H., Hong T.-M. (2024), Tunneling Time for Walking Droplets, https://arxiv.org/abs/2409.11934
- Vogl T. u. a. (2021), Sensitive single-photon test of extended quantum theory with 2D hBN,
  https://arxiv.org/abs/2103.17209
- Conlon L. O. u. a. (2023), Testing the postulates of quantum mechanics with coherent states of light and homodyne
  detection, https://arxiv.org/abs/2308.03446
- Kanthak S. u. a. (2024), Proposal for a BEC based test of Born's rule using light-pulse atom interferometry,
  https://arxiv.org/abs/2409.04163
- De Raedt H., Michielsen K., Hess K. (2011), Multi-order interference is generally nonzero,
  https://arxiv.org/abs/1103.0121
- Henson J. (2014), Bounding quantum contextuality with lack of third-order interference,
  https://arxiv.org/abs/1406.3281
- Dakic B., Paterek T., Brukner C. (2013), Density cubes and higher-order interference theories,
  https://arxiv.org/abs/1308.2822
- Niestegge G. (2011), Third-order interference and a principle of 'quantumness', https://arxiv.org/abs/1103.0638
- Fussy S. u. a. (2013), Born's Rule as Signature of a Superclassical Current Algebra, https://arxiv.org/abs/1308.5924
- Sinha A., Vijay A. H., Sinha U. (2014), On the superposition principle in interference experiments,
  https://arxiv.org/abs/1412.2198
- Vieira C. u. a. (2017), Exotic looped trajectories in double-slit experiments with matter waves,
  https://arxiv.org/abs/1705.07156
- da Paz I. u. a. (2015), Gouy phase in non-classical paths in triple-slit interference,
  https://arxiv.org/abs/1510.04186
- Quach J. Q. (2016), Which-way double slit experiments and Born rule violation, https://arxiv.org/abs/1610.06401
- Pleinert M.-O., von Zanthier J., Lutz E. (2018), Many-particle interference to test Born's rule,
  https://arxiv.org/abs/1810.08221
- Namdar P. u. a. (2021), Experimental Higher-Order Interference in a Nonlinear Triple Slit,
  https://arxiv.org/abs/2112.06965
- Margalit Y. u. a. (2015), A self-interfering clock as a "which path" witness, https://arxiv.org/abs/1505.05765
- Nakamura K., Nakazono N., Ando T. (2005), Dynamics of Macroscopic Wave Packet Passing through Double Slits,
  https://arxiv.org/abs/cond-mat/0508210
- Ngek I. N., Dikande A. M., Moubissi A. B. (2016), Matter-Wave Fields for Double-Slit Atom Interferometry,
  https://arxiv.org/abs/1610.07860

**Nur Suchtreffer, nicht gelesen [L?]:**
- arXiv:1508.06837 (Soliton-Interferenzmodell), https://arxiv.org/abs/1508.06837
- Radonjic 2023 PRA, https://www.scl.rs/papers/Radonjic2023_PhysRevA.pdf
- Interference in Quantum Mechanics, https://arxiv.org/abs/2508.12940
- lettersonmaterials.com/Upload/Journals/964/43-451.pdf
- https://arxiv.org/abs/2603.15505
- https://arxiv.org/abs/2502.20519
- https://www.arxiv.org/abs/2502.09136
- Oscillons from Q-balls (usal.es)

**Aus dem Gedaechtnis [L], nicht abgerufen:**
- Sinha U. u. a. 2010, Science 329, 418
- Sorkin R. 1994, Mod. Phys. Lett. A 9, 3119
- Ududec C., Barnum H., Emerson J. 2011, Found. Phys. 41, 396
- Kocsis S. u. a. 2011, Science 332, 1170
- Englert B.-G. 1996, PRL 77, 2154
- Arndt M. u. a. 1999, Nature 401, 680
- Fein Y. Y. u. a. 2019, Nat. Phys. 15, 1242
- Kovachy T. u. a. 2015, Nature 528, 530
- Grangier P., Roger G., Aspect A. 1986, EPL 1, 173
- Jacques V. u. a. 2007, Science 315, 966
- Weinberg S. 1989, Ann. Phys. 194, 336
- Gisin N. 1990, Phys. Lett. A 143, 1
- Polchinski J. 1991, PRL 66, 397
- Zych M. u. a. 2011, Nat. Commun. 2, 505
- Freimund D. L. u. a. 2001, Nature 413, 142
- Duerr S., Nonn T., Rempe G. 1998, Nature 395, 33
- 't Hooft G. 2016, The Cellular Automaton Interpretation of QM
- Cramer J. G. 1986, RMP 58, 647
- Nelson E. 1966, Phys. Rev. 150, 1079
- Unsicher [L?]: Cotter J. P. u. a. 2017, Sci. Adv.; Catillon P. u. a. 2008, Found. Phys. 38, 659

**Projekt:**
- THEORIE-VFW.md 4.5 und Q3
- PAPIER-I-ROBUSTHEIT-ENTWURF.md
- RUNDE-09.md Z. 341, RUNDE-16.md Z. 175, 299
- wolfram-scan-l/SEITENKARTE.md Z. 56-57, 74
- dashboard-overview-20260909/snapshot/neue-theorie/gitter-checkliste.json Z. 35-39
- RUNDE-37/RAUMZEIT-NETZ.md Z. 42, UEBERLEITUNGEN-EMERGENZ.md Z. 20

## 9. Einfach gesagt

- Beim Doppelspalt fragt man, warum einzelne Teilchen ein Streifenmuster bilden.
- Die Quantenmechanik sagt: Eine Welle geht durch beide Spalte, und das Teilchen landet dort, wo die Welle stark ist.
  Daraus folgt, dass es bei drei Spalten nichts Neues gibt. Das ist bis auf etwa ein Tausendstel gemessen.
- Ein Forscherpaar hat 2025 gezeigt, dass ein klassisches Teilchen mit eigener "Uhr", das eine Welle mitschleppt, im
  Computer ebenfalls Streifen machen kann. Die Abstaende stimmen aber nur nach Einstellen eines Reglers.
- Fuer unseren Q-Ball heisst das: Seine innere Uhr gibt Streifen, die etwa so viel zu breit sind, wie der Ball Ladung
  hat. Er taugt also gut als Teilchenform, aber vermutlich nicht als Erklaerung der Streifen.
- Ein kleiner Rechentest (QBALL-DOPPELSPALT-1) kann das bestaetigen oder widerlegen.
