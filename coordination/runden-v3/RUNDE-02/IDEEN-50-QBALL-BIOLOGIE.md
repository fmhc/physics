# 50 verrueckte Q-Ball-Ideen mit Analogien aus der Biologie (Eingang Runde 2)

Leitung claude-primary, Zeit vor dem Schreiben gemessen: 2026-09-30 00:51:14 CEST.

Finn woertlich: "mach weitere q-ball ideen / ideate 50 verrückte ideen wie q-balls und analogien aus dem größen ganzen
(biologie) dazu passen könnten."

## Rahmen

- **Status:** Alles sind Hypothesen und Analogien, nichts ist gerechnet.
- **Modell:** unser Q-Ball, ein komplexes Feld mit U = S - S^2 + S^3/2 und S = |phi|^2. Die innere Frequenz omega liegt
  zwischen 1/sqrt(2) und 1. Die duenne Wand verhaelt sich wie ein Fluessigkeitstropfen (Runde 1, F-3).
- **Bekannte Grundlage:**
  - Codex' 3D-Verdichtung: Ein Kondensat zerfaellt in Klumpen.
  - Drehende Q-Baelle haben J = m Q.
  - omega = dE/dQ spielt die Rolle eines chemischen Potentials.
- **Je Idee:** Analogie, Hypothese (H), kleinster Test (T), [L4] bekannt oder vermutlich bekannt (Literatur aus dem
  Gedaechtnis, nicht nachgelesen).
- **Rechenorte:** .69 CUDA unter dem Lock, TS440 CPU bei Codex. 1D, 2D und 3D wie in den bisherigen Laeufen.

## A. Der Q-Ball als Zelle

1. **Membran.** Die duenne Wand ist die Zellmembran.
   - H: Innen- und Aussendruck unterscheiden sich wie bei einem Tropfen, Delta P = 2 sigma/R (Young-Laplace), und sigma
     ist die Wandspannung.
   - T: Spannungstensor eines 3D-Profils bei drei Q-Werten; sigma aus dem Wandintegral.
   - [L4 vermutlich: Duenne-Wand-Theorie nach Coleman]
2. **Osmose.** omega ist das chemische Potential.
   - H: Ein Q-Ball in einem duennen Hintergrundkondensat waechst, wenn dessen Potential ueber seinem omega liegt, und
     schrumpft sonst, bis beide gleich sind.
   - T: 3D-Box mit Hintergrund bei drei Werten; dQ/dt gegen die Differenz der Potentiale.
3. **Stoffwechsel.** Einfangen freier Quanten ist "Nahrung": Jedes eingefangene Quant setzt m - omega als "Waerme" frei.
   - H: Die Einfangrate haengt vom Frequenzabstand ab.
   - T: 1D-Wellenpaket auf einen Q-Ball; eingefangener Anteil und abgestrahlte Energie.
   - [L4: Solitosynthese, Griest und Kolb 1989]
4. **Apoptose.** Unter einer Mindestladung Q_min stirbt der Q-Ball, er loest sich auf.
   - H: Das geschieht schlagartig, nicht allmaehlich; es gibt eine "Todesschwelle".
   - T: 3D, Q langsam absenken (schwacher Abfluss am Rand) und den Zerfallszeitpunkt messen.
   - [L4: Q_min bekannt; der dynamische Verlauf weniger]
5. **Zellteilung.** Ein drehender Q-Ball mit Windung m = 2 teilt sich in zwei Tochterbaelle.
   - H: Die Teilung kommt ab einer kritischen Groesse, wie bei Zellen.
   - T: 2D, m = 2 mit kleiner Stoerung; Zeitpunkt und Toechter.
   - [L4 teilweise: Instabilitaet drehender Q-Baelle]
6. **Endozytose.** Ein grosser Q-Ball verschluckt einen kleinen.
   - H: Ob er schluckt oder abprallen laesst, entscheidet die relative Phase: gleichphasig verschmelzen, gegenphasig
     abstossen.
   - T: 1D-Stoesse bei relativer Phase 0, pi/2 und pi.
   - [L4: Battye und Sutcliffe 2000, "Q-ball dynamics"]
7. **Vesikel.** Ein hohler Q-Ball, also eine Q-Schale.
   - H: Die Schalenform ist in unserem Potential ohne Eichfeld instabil. Mit Drehung koennte sie ueberleben.
   - T: 2D-Ring mit Windung als Schalenmodell.
   - [L4: Q-Schalen mit Eichfeld, Arodz und Lis]
8. **Zellkern.** Zwei Felder, eines sitzt im anderen.
   - H: Ein Zwei-Kanal-Q-Ball bildet einen Kern-Huelle-Aufbau, wenn die Kanaele verschiedene Massen haben.
   - T: 1D, zwei gekoppelte Kanaele, Profilsuche.
   - Bezug: unser Mehrkanalmodell.

## B. Uhren, Rhythmus, Synchronisation

9. **Circadiane Uhr.** Jeder Q-Ball ist eine Uhr mit der Frequenz omega.
   - H: Benachbarte Q-Baelle mit leicht verschiedenem omega rasten ueber ihre Auslaeufer auf eine gemeinsame Phase ein
     (Kuramoto).
   - T: 1D-Kette aus 5 Q-Baellen mit kleinem Abstand; Phasenordnungsparameter ueber die Zeit.
10. **Herzschrittmacher.** Ein grosser Q-Ball zieht die Frequenz kleiner Nachbarn auf seine eigene.
    - T: gross neben klein in 1D; omega des Kleinen ueber die Zeit.
11. **Gluehwuermchen.** Viele "atmende" Q-Baelle synchronisieren ihr Atmen ueber ausgetauschte Strahlung.
    - T: 3D-Box mit angestossenen Q-Baellen; Korrelation der Atemphasen.
12. **Chemische Uhr (Belousov-Zhabotinsky).** Zwei nahe Q-Baelle tauschen periodisch Ladung aus.
    - T: Paar nahe beieinander; Q_links(t) und Q_rechts(t).
    - [L4: charge-swapping Q-balls, Copeland, Saffin und Zhou 2014]
13. **Neuron.** Ein kleiner Stoss verebbt, ein grosser loest einen grossen Atemausbruch aus: ein "Aktionspotential".
    - T: Stossamplitude gegen Antwortamplitude; gibt es eine Schwelle?

## C. Evolution und Oekologie

14. **Selektion (Ostwald-Reifung).** In einer Box mit vielen Q-Baellen wachsen die grossen, die kleinen verdampfen.
    - H: Die Groessenverteilung folgt dem Lifshitz-Slyozov-Gesetz, Radius ~ t^(1/3).
    - T: Codex' 3D-Verdichtung laenger laufen lassen; Klumpengroessen ueber die Zeit.
    - [L4 teilweise]
15. **Raeuber und Beute.** Zwei Arten von Q-Baellen aus zwei Feldern mit Ladungsaustausch.
    - H: Die Bestaende schwingen wie bei Lotka-Volterra.
    - T: Zwei-Feld-Box, Gesamtladung je Art ueber die Zeit.
16. **Symbiose.** Ein Paar aus zwei Q-Baellen ist fester gebunden als zwei einzelne.
    - T: Energie des gebundenen Paars gegen 2 E(Q/2).
17. **Mutation.** Angeregte Q-Baelle mit Knoten im Profil sind "Mutanten".
    - H: Die meisten zerfallen; manche sind langlebig.
    - T: radial angeregte Profile in 3D; Lebensdauer.
18. **Artbildung.** Die Familien (Kugel, drehend m = 1 und 2, Ring) sind Arten.
    - H: Verzweigungen in omega sind die "Artbildungsereignisse".
    - T: Familien entlang omega verfolgen und Verzweigungspunkte suchen.
19. **Fitness.** E/Q ist die "Fitness": Grosse Q-Baelle haben die kleinste Energie je Ladung.
    - H: In jeder Mischung gewinnen die grossen, und die Evolution geht zur duennen Wand.
    - T: E/Q(Q) aus dem Atlas.
    - [L4: bekannt]
20. **Katastrophe.** Ein Rauschpuls (Waerme) vernichtet kleine, aber nicht grosse Q-Baelle.
    - T: Ueberlebensanteil gegen Rauschamplitude und Q.
21. **Nische.** In einer ungleichmaessigen Umgebung wandern Q-Baelle dorthin, wo sie am stabilsten sind.
    - T: Q-Ball in einem Gradienten eines Potentialparameters; Drift und Richtung.
    - Bezug: QG-1-Aufbau.

## D. Entwicklung, Muster, Gestalt

22. **Turing-Muster.** Codex' Kondensatzerfall ist eine Musterbildung.
    - H: Die Wellenlaenge der Klumpen folgt der linearen Instabilitaet des Kondensats.
    - T: dominante Wellenlaenge gegen S0 bei drei Werten, gegen die analytische Vorhersage.
    - [L4: Modulationsinstabilitaet bekannt]
23. **Zellpolaritaet.** Im Gradienten wird der Q-Ball einseitig, wie eine polarisierte Zelle.
    - T: Dipolmoment der Ladungsdichte im QG-1-Aufbau.
24. **Vielzeller.** Drei oder vier Q-Baelle mit passenden Phasen bilden einen stabilen Verbund.
    - T: Dreieck bzw. Tetraeder in 2D/3D mit Phasenmustern; Zusammenhalt ueber die Zeit.
25. **Gewebe.** Viele Q-Baelle mit Daempfung ordnen sich zu einem Gitter ("Q-Materie").
    - T: 2D-Box, zufaellige Startorte, schwache Daempfung; Ordnungsparameter.
26. **Schleimpilz.** Verstreute kleine Q-Baelle sammeln sich zu einem grossen, wie Dictyostelium-Zellen.
    - T: wie Nr. 14, aber mit gezaehlten Verschmelzungen.
27. **Wundheilung.** Ein beschaedigter Q-Ball (Stueck herausgeschnitten) wird wieder rund.
    - T: Heilzeit gegen Schadensgroesse.
28. **Groessenbegrenzung.** Waechst ein drehender Q-Ball durch Einfang, wird er ab einer Groesse instabil und teilt sich.
    - T: 2D, langsamer Ladungszufluss, m = 1 bzw. 2.

## E. Information und Vererbung

29. **Gene.** Die Windungszahl m ist ein "Gen".
    - H: Teilt sich m = 2, erben die Toechter je m = 1; die Windung bleibt erhalten.
    - T: nach Nr. 5 die Windungen der Toechter zaehlen.
30. **Epigenetik.** Die unsichtbare globale Phase bestimmt, wie Q-Baelle einander behandeln (Nr. 6).
    - H: Dieselben Baelle mit anderer Phase haben andere "Lebenswege".
31. **Gedaechtnis.** Zwei Loesungen bei gleicher Ladung (duenne und dicke Wand) speichern ein Bit.
    - H: Ein Stoss schaltet zwischen den Aesten um.
    - Wahrscheinlich scheitert das: Der Dicke-Wand-Ast ist in 3D instabil (Vakhitov-Kolokolov). Gute L1-Karte.
32. **Immunsystem.** Ein Q-Ball erkennt Wellen an ihrer Frequenz und schluckt nur, was zu seinen inneren Moden passt
    (Schluessel-Schloss).
    - T: 1D-Streuung ueber einen Frequenzbereich, Absorptionsspektrum.
33. **Virus.** Ein winziger Q-Ball dringt in einen grossen ein und veraendert dessen innere Moden.
    - T: kleiner Ball verschmilzt mit grossem; Modenspektrum vorher und nachher.

## F. Energie

34. **ATP.** Die Ladung Q ist die Energiewaehrung, m - omega der Gewinn je Quant.
    - T: gespeicherte freie Energie je Ladung gegen Q; Wirkungsgrad der Freisetzung beim Stoss.
35. **Mitochondrium (Endosymbiose).** Ein kleiner Q-Ball eines zweiten Feldes lebt dauerhaft in einem grossen.
    - T: Zwei-Feld-Modell mit Kopplung; ineinander liegende Loesung suchen.
36. **Photosynthese.** Ein Q-Ball schluckt einfallende geladene Wellen und waechst.
    - T: ebene geladene Welle auf einen Q-Ball; Wachstumsrate gegen Frequenz.
37. **Fieber und Denaturierung.** Es gibt eine Temperatur, ab der ein Q-Ball schmilzt.
    - T: Rauschbad, Schwelle gegen Q.
38. **Winterschlaf.** Nahe der duennen Wand (omega -> 1/sqrt(2)) tickt die innere Uhr am langsamsten.
    - H: Stoerungen perlen dort am besten ab.
    - T: Antwortamplitude auf einen festen Stoss gegen omega.

## G. Kommunikation und Kollektiv

39. **Quorum Sensing.** Ab einer kritischen Dichte schaltet eine Q-Ball-Population auf gemeinsames Atmen um.
    - T: Ordnungsparameter gegen Anzahl in der Box.
40. **Schwarm.** Bewegte Q-Baelle mit phasenabhaengiger Kraft bilden Schwaerme: echte Swarmalatoren statt Proxy (vgl. K-6).
    - T: 2D, 20 Q-Baelle mit Zufallsphasen und kleinen Geschwindigkeiten.
41. **Nervenfaser.** Eine Kette von Q-Baellen leitet eine Atem-Erregung weiter.
    - T: ersten Ball anstossen, Laufgeschwindigkeit und Daempfung entlang der Kette.
42. **Bienenwabe.** In 2D packen sich Q-Baelle sechseckig.
    - T: Relaxation vieler 2D-Q-Baelle; Winkelverteilung der Nachbarn.

## H. Die grosse Bruecke: Kosmos und Leben

43. **Samen.** Q-Baelle als Dunkle Materie sind die Keime der Strukturbildung.
    - [L4: Q-Ball-Dunkle-Materie ist Literatur]
44. **Ursuppe.** Der Kondensatzerfall im fruehen Universum (Affleck-Dine) ist die "Abiogenese" der Q-Baelle.
    - T: Codex' Folgefrage, ob getrennte Kerne entstehen.
45. **Leben im Nichtgleichgewicht.** Ein angetriebener, gedaempfter Q-Ball wird eine dissipative Struktur (Prigogine),
    die nur mit Energiezufuhr besteht.
    - T: 1D-NLS mit Pumpe und Daempfung.
    - Bezug: VFW-Federn mit Pumpe (VS-1).
    - [L4: dissipative Solitonen, Akhmediev]
46. **Viruskapsid.** 12 Q-Baelle auf einer Kugel ordnen sich ikosaedrisch.
    - T: Minimum der Paarenergie (Thomson-Problem mit Q-Ball-Kraeften).
47. **Haendigkeit des Lebens.** Eine Mischung aus m = +1 und m = -1 entwickelt durch Stoesse einen Ueberschuss einer Sorte.
    - Das ist nur moeglich, wenn etwas die Spiegelsymmetrie bricht. Ohne Bruch ist sie ein reiner L1-Test.
    - T: Stoesse +1 gegen -1 und Ausgangsstatistik.
48. **Altern.** Eine schwache Kopplung an einen masselosen Kanal laesst den Q-Ball langsam verdampfen.
    - H: Die Rate ~ Oberflaeche ergibt eine "Lebenserwartung" ~ Radius.
    - T: Zwei-Kanal-Modell, Q(t).
    - [L4: Verdampfung, Cohen, Coleman, Glashow und Georgi 1986]
49. **Selbstreplikation.** Im geladenen Bad waechst ein m = 2-Ball durch Einfang, teilt sich in zwei m = 1, die wieder
    wachsen und sich teilen.
    - H: Es entsteht ein Vermehrungszyklus.
    - T: 2D mit Ladungsbad; Zahl der Baelle ueber die Zeit.
50. **Gehirn am kritischen Punkt.** Grosse Netze gekoppelter Q-Ball-Uhren zeigen Lawinen mit Potenzgesetz, wie Gehirne
    am kritischen Punkt.
    - T: viele Q-Baelle, Groessenverteilung der Atem-Lawinen.

## Vorschlag der Leitung fuer Runde 2

Auswahlregel: klein, messbar, nicht offensichtlich bekannt.

| Nr | Warum |
|---|---|
| 14 Ostwald-Reifung | baut direkt auf Codex' 3D-Lauf auf; klares Gesetz (t^(1/3)), das scheitern kann |
| 9/10 Uhren-Synchronisation | billig in 1D; misst, ob Q-Baelle ueber ihre Auslaeufer koppeln, und ist anschlussfaehig an VFW |
| 5/29 Teilung und Vererbung | verbindet K-4 (drehende Baelle) mit einer einfachen Frage: Bleibt die Windung erhalten? |
| 32 Absorptionsspektrum | billig in 1D; zeigt die inneren Moden, die jede weitere Idee braucht |
| 31 Gedaechtnis | wahrscheinlich scheiternd, aber eine saubere L1-Probe |

Dazu eine Zufallskarte aus den uebrigen 45.

## Einfach gesagt

Q-Baelle erinnern erstaunlich stark an lebende Zellen. Sie haben eine Haut (die duenne Wand), eine innere Uhr (die
Drehung der Phase) und eine Energiewaehrung (die Ladung). Sie koennen fressen, sich teilen, verschmelzen und verdampfen.
Wir haben 50 solche Vergleiche aufgeschrieben und zu jedem einen kleinen Rechentest. Einige davon (etwa das Fressen und das
Ladungspendeln) sind schon bekannte Physik; die anderen testen wir in den naechsten Runden der Reihe nach.
