Urteil: Kein Kandidat passt zur gemessenen Welt; der Stand ist ein Baukasten auf vier getrennten Buehnen. Am meisten
Inhalt hat Finns Pfeil-Eis-Netz (K-A), aber nur mit Feinabstimmung der Tempi haltbar; strukturell vertraeglich ist nur
das Ereignis-Netz mit Zahl = Volumen (K-B), und das fast ungetestet. Groesste Luecke: das Standardmodell. Befunde zum
Stand: 2 A, 7 B, 9 C.

# WELTMODELL-REVIEW-1: Fachliches Review des Projektstands gegen "ein Weltmodell, das passt"

- Pruefer: pruefer-opus (Haus Anthropic, frisch). Beginn 2026-10-04 13:38:41 CEST (date).
- Auftrag: RUNDE-37/weltmodell-review-1/KARTE.md, sha256 084df8731306c1e0d478b043b14eb0fcfd775358ff288af36e1e5405e5c5a902
  (selbst gemessen; die Leitung hat keinen Soll-Hash genannt).
- Kennzeichen: [ES] eigener Schluss des Pruefers, [H] Hypothese; Projektkennzeichen ([E]/[G]/[M]/[S]/[L]/[H]) werden
  aus den Quellen uebernommen und dort, wo ich sie fuer falsch halte, als Befund gefuehrt.
- Schreibtisch, keine Laeufe; Literaturabrufe werden unten gezaehlt.

## Ergebnis zuerst

1. **Das Projekt hat heute kein Weltmodell, das zu den gemessenen Tatsachen passt, sondern einen Baukasten [ES].** Die
   Teilstuecke sind auf vier getrennten Buehnen gerechnet: festes Raum-Netz mit aeusserer Uhr, Regge-Raumzeit-Gitter,
   euklidisches Zufallsnetz und Kausalmenge. Keine Buehne traegt mehr als einen der vier Kernbausteine (Schwerkraft,
   Licht, Fermionen, Lorentz-Invarianz) in gezeigter Form, und fast alles ist eingesetzt statt entstanden.
2. **Am meisten traegt Finns Tetraeder-Netz mit Pfeil-Eis** (statisches Coulomb-Gesetz aus der Eisregel, noch keine
   Lichtwellen; Fermion-Statistik; Gravitonen). Aber ein
   festes Netz hat ein Ruhesystem. Licht- und Gravitontempo sind dort unabhaengige Groessen, die nach GW170817 auf 1e-15
   gleich sein muessen; Collins u. a. erwarten ohne starke Feinabstimmung Verletzungen im Prozentbereich. Dazu sind die
   Gravitonen doppelt, und das Fadenend-Fermion ist spinlos (TWIST-SPIN-1).
3. **Der einzige Kandidat ohne strukturelle Verletzung ist das Ereignis-Netz mit Zahl = Volumen (Kausalmenge), vor
   allem weil an ihm fast nichts gerechnet ist.** Massive Materie laeuft dort in 3+1 noch nicht stabil; Fermionen und
   Licht fehlen. Die Schwerkraft aus Materie ist nur euklidisch gezeigt, in 4D zwischen Kugel und Torus
   widerspruechlich und nach XI-KUGEL-1 zu rund 70 % eine Eigenschaft des Netzes statt des Kontinuumsmechanismus.
4. **Die groesste Luecke ist das Standardmodell selbst.** Chirale Fermionen, nichtabelsche Eichgruppe, drei
   Generationen und Massen kommen in keinem Kandidaten vor; die Gitter-Fermionen des Projekts sind vektorartig und
   tragen Verdoppler.
5. **Der Weichenstand v5 stimmt in den Zahlen**, ist aber in Urteilswoertern und Auslassungen zu optimistisch (A1
   Verdoppler, A2 "4D teilweise"; Abschnitt 6).

## 1. Bestandsaufnahme

Spalte "Herkunft": **eingesetzt** = von Hand in die Regel gelegt; **entstanden** = aus einfacheren Regeln gefolgt;
**algebraisch** = nur Vertauschungsregeln, keine Dynamik. Zahlen an den genannten ERGEBNIS-Dateien bzw. per jq an
lauf-69/auswertung.json geprueft (KUGEL-1, KUGEL-2, WILSON-2D).

| Baustein | Netzart / Modell | Stand (Kurzform) | Kennzeichen | Herkunft |
|---|---|---|---|---|
| Substrat (A) | Regge-Kuhn-Gitter 4D; Finns Tetraeder-/Pyrochlor-Netz; raeumliches Zufallsnetz mit aeusserer Uhr | feste Hintergruende; keine Dynamik des Netzes selbst gerechnet | [G] | eingesetzt |
| Substrat (B-eukl.) | Poisson-Delaunay auf S^2/S^4, T^2/T^4, euklidisch, "Zahl = Volumen" | feste Hintergrundgeometrie, gemittelt ueber Punktwuerfe; keine Summe ueber Geometrien | [G] | eingesetzt |
| Substrat (B) | Poisson-Kausalmenge im Minkowski-Diamanten 1+1 und 3+1 | feste Realisierungen; Dynamik der Ordnung nicht gerechnet | [G] | eingesetzt |
| Substrat (C) | CDT | nur Literatur | [S/L] | - |
| Materie, bosonisch | M1: ein komplexer Skalar, U(S) = S - S^2 + S^3/2 (Papier I, main.tex Z. 17-18); M2 (Huelle); geladene Q-Baelle | lineare Anregungen, stille Stellen; Q-Ball auf Pyrochlor 0,8 % unter dem Kontinuum (QBALL-PYRO-1) | [G/M] | eingesetzt (Feld und Potential) |
| Materie, Fermionen | QCA auf BCC (8 Zustaende); eingesetzter Weyl-Spinor (Zufallsnetz 3D); Dirac/Wilson 2D; Fadenenden mit Levin/Wen-Twist; Dyon | QCA: je Automat 4 Kegel bei k = 0 und je 4 an H, P, P'; Masse koppelt zwei Kopien entgegengesetzter Chiralitaet, Verdoppler an P, P' meist masselos (QCA-BCC-RUECK-1, QCA-DIRAC-T-1). Zufallsnetz: Kegel sauber, aber rho(0) = 0,463 je Knoten (im Fenster eps = 0,2 685 Kegel-Einheiten statt einer). 2D: Schwerkraft-Antwort nicht die eines Dirac-Fermions | [G/M] | eingesetzt bzw. algebraisch |
| Halber Spin | QCA, Dyon, Fadenenden, Kausalmenge | QCA: Darstellung gewaehlt; Dyon: Spin und Statistik aus derselben e-m-Paarung [P: DYON-STATISTIK-L, dort S]; **Fadenenden auf Finns Netz: Fermion-Statistik (TWIST-PYRO-1), aber spinlos** (echte Darstellung von T, nicht 2T; Invarianten +1; mit fester Projektion sind die Drehungen keine Symmetrie der Huepfer, bei fester Teilchenzahl Fluss 0 ueberall), vorab ableitbar bis auf den Fluss (TWIST-SPIN-1, ERGEBNIS Z. 17-38; jq: Plan TS1 nein, TS2 entfaellt; Zusatzstufe TS1 ja, TS2 nein); Kausalmenge: Rahmen je Punkt noetig (SPIN-KAUSAL-L) | [G/M/S] | eingesetzt bzw. algebraisch; halber Spin nirgends entstanden |
| Licht / Eichfelder | Pfeil-Eis auf Pyrochlor-Kanten | klassische Coulomb-Phase (FLUSS-1, RUNDE-34): statisches Coulomb-Gesetz aus der Eisregel (Paarpotential mit p = 0,963 +- 0,070, Korrelationen r^-3,01, Pinch-Punkte), per Monte Carlo, **ohne Dynamik, also ohne Lichtwellen**; Photonen (Quanten-Pfeil-Eis) auf Finns Netz nicht gerechnet; nur U(1) | [G] | entstanden (statisch, aus Eisregel) |
| Schwerkraft eingebaut | Regge 4D; kubisches Raum-Netz mit eingebauter Regel (REGEL-1, RUNDE-36) | Regge: Newton und gamma = 1 im Fernfeld, einige Prozent Abweichung bis ~10 Maschen (REGGE-ZEIT-1); zwei Polarisationen mit c (REGGE-WELLE-1). Kubisch: zwei Polarisationen, Newton mit Q-Ball-Quellen, gleiches Fallen nur bei Energiekopplung | [G], vorab ableitbar | eingesetzt |
| Schwerkraft Tensor-Eis | Finns Netz, Bauweise B1 | zwei Kopien, 4 statt 2 Gravitonen, Newton je Kopie; ohne Zwang an 98 % der k wachsend; Zwangsflaeche von Hand | [G] | eingesetzt (Eisregel und Zwang) |
| Schwerkraft induziert | (B-eukl.) | 2D: universelle Anomalie getroffen (1,075 +- 0,071 und 0,92 +- 0,12 auf unabhaengigen Netzen; 0,89 +- 0,14 in WILSON-2D auf Saaten von DIRAC-2D, also nicht unabhaengig). 4D: R-Koeffizient auf S^4 negativ fuer die Formfamilie C, S, Q (-1,46 bis -1,65); Torus +1,24 +- 0,50 (umgerechnet); Gs-Lesart +4,21 (Modell verworfen). **XI-KUGEL-1:** Kipppunkt xi* = 0,555 +- 0,018 statt 1/6 (22 SE daneben; jq: 0,5552 +- 0,0177, Steigung 2,9047 +- 0,0040); ein Eigenzeit-Regler mit dem gemessenen Netzmoment gaebe -0,48 statt -1,61, also stammen rund 70 % des Glieds aus Gitter-Eigenheiten [ES des Agenten, mit g0 als Reglermoment]; mit konsistenter Masse xi* = 1,25 +- 0,04 (ERGEBNIS Z. 25-46) | [E] | entstanden, aber ueberwiegend Reglereigenschaft (INDUZIERT-G-L, XI-KUGEL-1) |
| Selbstkopplung der Schwerkraft | - | nirgends gerechnet | - | - |
| Gemeinsames Tempo (P1) | (A) Pfeil-Eis; (A) Laengen-Netz; (B) | Pfeil-Eis: eigenes Tempo je Sorte [S Levin/Wen]; Laengen-Netz klassisch gemeinsam [ES, Patch-Test L]; Kausalmenge: gemeinsame Ordnung [ES/H] | gemischt | - |
| 1/2-Regel (P3) | Regge; Raum-Netz mit Uhr; Tensor-Eis; CDT | eingebaut bei Regge; Raum-Netz mit je Kante eigener Bewegungsenergie: lambda = -1/2, c = 1/5 (REGEL.md Abschn. 8; Rechnung von mir nachgerechnet, siehe 6, C-Befund); Tensor-Eis nur langwellig | [M/G] | eingesetzt oder verfehlt |
| Dimension 3+1 | alle | in jeder Rechnung eingegeben (2D, 3D, 1+1, 3+1, S^4); spektrale Dimension per Beutel-Teilchen messbar (RUNDE-24) | [G] | eingesetzt |
| Teilchen: Punkt oder Welle | (B) | Punkt: Varianz 1/4 je Schritt, Heizen (KAUSAL-SWERVE-1); Welle 1+1 im Mittel exakt (KAUSAL-WELLE-1); 3+1: Mittel waechst fuer massive Felder exponentiell, Abhilfe Ordnung fuer Ordnung mit Feinabstimmung und Rauschen > Signal (KAUSAL-WELLE-4D, -4D-SCHICHT-1/2); Literatur: keine stabile 4D-Familie bekannt (KAUSAL-4D-STABIL-L) | [G/S] | - |
| Messdatenbezug | KS-1 / "M1" weite Doppelsterne (Gaia) | "im Auswerteregime der Scheinsignale, nicht unterscheidbar"; DR4 am 2.12. | Daten | nicht an das Weltmodell gekoppelt |

**Lesart der Bestandsaufnahme [ES]:**

1. **Fast alles ist eingesetzt, wenig ist entstanden.** Entstanden (nicht eingegeben und nicht vorab abgeleitet) sind
   vor allem: das statische Coulomb-Gesetz (emergentes U(1), ohne Wellen) aus der Eisregel (FLUSS-1), die 2D-Anomalie
   aus dem Zittern eines Skalars, das
   Vorzeichen des 4D-R-Koeffizienten auf S^4 (nach XI-KUGEL-1 in der Lesart des Agenten [ES dort, mit g0 als
   Reglermoment] zu rund 70 % gitterspezifisch, also ueberwiegend eine Eigenschaft dieses Netzes und nicht der
   Kontinuumsmechanismus nach Sakharov), dazu unerwuenschte Eigenschaften wie die doppelten
   Gravitonen und das raue Band. Netz, Dimension, Signatur, Feldinhalt, Potential, Spinordarstellung, Regge-Wirkung und
   die Zwangsflaeche des Tensor-Eises sind eingegeben.
2. **Kein Baustein des Standardmodells ist vorhanden.** Keine nichtabelsche Eichgruppe, keine chiralen Fermionen, kein
   Higgs, keine Generationen, keine Massenhierarchie. Die Fermionen des Projekts sind vektorartig (Masse koppelt zwei
   entgegengesetzte Chiralitaeten, QCA-DIRAC-T-1) und kommen mit Verdopplern bzw. einem rauen Band.
3. **Keine Netzdynamik.** Jede Rechnung laeuft auf einem festen oder gemittelten Hintergrund. Was ein Weltmodell am
   Substrat erklaeren muss (warum dieses Netz, warum 3+1, warum flach im Grossen), ist nirgends gerechnet.
4. **"Q-Baelle M1/M2" und "M1 weite Doppelsterne" sind zwei verschiedene Dinge mit demselben Namen** (Papier I gegen
   KS-1). Der Messdatenstrang prueft eine Abweichung von Newton bei kleiner Beschleunigung, die keiner der
   Weltmodell-Kandidaten vorhersagt; er ist kein Test des Weltmodells (C-Befund in 6).
5. **Selbstanzeige:** Beim Suchen des Datenstrangs habe ich die Gedaechtnisnotiz project-m1-auswerteregime-dr4.md
   gelesen; sie enthaelt eine Zeile zum KS-1-DR3-Ausgang. Ich verwende sie nicht und gebe sie nicht wieder. Eine
   KS-1-Ergebnisdatei habe ich nicht geoeffnet.

## 2. Innere Passung

**Die Buehnen.** Die Spalte (A) des Weichenstands enthaelt zwei verschiedene Buehnen, die man trennen muss [ES]:

- **A1, Raum-Netz mit aeusserer Uhr:** Finns Diamant-/Pyrochlor-Netz (Pfeil-Eis, Tensor-Eis, Fadenenden), das
  raeumliche Zufallsnetz (SPIN-ZUFALLSNETZ-1) und die QCA (Zeit in globalen Schritten).
- **A2, Raumzeit-Gitter mit Zeitkanten:** Regge-Kuhn in 4D (REGGE-WELLE-1, -SCHIEF-1, REGGE-ZEIT-1). Hier ist die
  Zeit-Umbenennung (Lapse) eingebaut, in A1 nicht (REGEL.md Abschn. 8).
- Dazu **B-eukl.** (euklidisch, ohne Zeit), **B** (Kausalmenge) und **C** (nur Literatur).

**Welche Bausteine auf welcher Buehne stehen [ES, aus Abschnitt 1]:**

| Buehne | Schwerkraft | Licht (U(1)) | Fermionen | kein Ruhesystem | Materie-Wellen 3+1 |
|---|---|---|---|---|---|
| A1 Finns Netz | Tensor-Eis: doppelt, Zwang von Hand | nur statisches Coulomb-Gesetz (FLUSS-1), keine Lichtwellen | nur Austauschvorzeichen, spinlos (TWIST-SPIN-1) | nein | Q-Ball klassisch ja |
| A1 andere Gitter | kubisch mit eingebauter Regel (REGEL-1) | - | QCA auf BCC (Verdoppler); Spinor auf Zufallsnetz (raues Band) | nein | Q-Ball als Quelle (REGEL-1) |
| A2 Regge | eingebaut, Fernfeld richtig | nicht gerechnet | nicht gerechnet | nur langwellig | nicht gerechnet |
| B-eukl. | induziert: 2D ja, 4D widerspruechlich (Kugel gegen Torus) und ueberwiegend gitterspezifisch (XI-KUGEL-1) | - | 2D: nicht die Dirac-Antwort | Frage stellt sich euklidisch nicht | - |
| B Kausalmenge | nicht gerechnet | - | 1+1 im Mittel | ja | massiv instabil im Mittel |

**Befund [ES]: Keine Buehne traegt mehr als einen der vier Kernbausteine (Schwerkraft, Licht, Fermionen,
Lorentz-Invarianz) in einer Form, die als gezeigt gelten kann.** Am meisten traegt Finns Netz (A1): drei Bausteine,
jeder nur teilweise. Das ist ein Ergebnis zugunsten Finns Bild, das der Weichenstand so nicht ausspricht, aber es ist
zugleich die Buehne mit dem schwersten aeusseren Problem (Abschnitt 3).

**Kombinationen im Einzelnen:**

1. **Schwerkraft aus Materie (B-eukl.) mit irgendeinem lorentzschen Baustein: nicht vereinbar ohne Zusatzannahme [ES].**
   Ein lokales euklidisches Zufallsnetz hat kein lokales lorentzsches Gegenstueck ohne Ruhesystem: Zu einem Sprinkling
   gibt es keinen Graphen endlicher Valenz, der mit Lorentz-Invarianz vertraeglich ist [S: Bombelli/Henson/Sorkin,
   Abstract]. Das Netz ist also entweder ein Regler fuer ein
   Kontinuum (dann ist das Netz nicht die Welt, und das Ergebnis haengt am Regler, INDUZIERT-G-L) oder der euklidische
   Schatten einer Kausalmenge (das ist die Hypothese der Spalte, nicht gezeigt). Die Kausalmenge ist nicht lokal, das
   Delaunay-Netz lokal; schon deshalb ist die Uebertragung nicht selbstverstaendlich.
2. **Induzierte Schwerkraft mit Regge- oder Tensor-Eis-Schwerkraft: schliessen sich als Erklaerung aus [ES].** Ue1
   verlangt Kanten ohne eigene Steifigkeit; Regge und Tensor-Eis setzen eine eigene Steifigkeit ein. Beides zusammen
   ist rechnerisch moeglich (die Kehrwerte von G addieren sich), aber dann erklaert das Zittern der Materie die
   Schwerkraft nicht mehr. Ein Weltmodell muss einen der drei Wege waehlen.
3. **Gravitonen doppelt (TENSOR-EIS-PYRO-1):** Massen in verschiedenen Kopien spueren sich exakt nicht. Das ist mit
   gleichem Fallen und "alles zieht alles an" unvereinbar, solange Materie in beiden Kopien sitzen kann. Der Ausweg
   "Werte nur auf einer Tetraedersorte" [H] ist eine neue Bauregel, kein Befund.
4. **Licht und Gravitonen auf Finns Netz:** beide auf den Pyrochlor-Kanten, also zwei Variablen je Kante (Pfeil und
   Laenge). Widerspruchsfrei, aber ungekoppelt gerechnet. Das Pfeil-Eis ist nur statisch gerechnet (FLUSS-1); ein
   Photon des Quanten-Pfeil-Eises haette ein eigenes, frei einstellbares Tempo (Levin/Wen stimmen t ab [P:
   LICHT-GLEICH-L, dort S-lokal]), unabhaengig vom Graviton-Tempo (omega^2/k^2 = 0,25 in Netzeinheiten). P1 und P2
   sind dort offen, nicht erfuellt.
5. **QCA-Fermionen und Finns Netz: verschiedene Gitter [ES].** Die vollsymmetrischen Automaten leben auf BCC; auf dem
   Diamantnetz gibt es Spin-1/2-Kegel generisch nur mit der kleinen Gruppe L_2 (QCA-DIAMANT-4, Ergebnis 2). Ein
   Fermion "auf Finns Netz" ist damit nur das Fadenende des Pfeil-Eises. Nach TWIST-SPIN-1 ist es dort ein
   **spinloses Fermion**: Statistik -1, Spin ganzzahlig. Spin und Statistik kommen auf dem Gitter nicht aus derselben
   Verdrehung; halber Spin braucht mindestens zwei Zustaende je Knoten (eingesetzt) oder entsteht erst in einer
   Bandstruktur mit Fluss pi von Hand (wie bei Levin/Wen). Innerhalb von K-A stehen damit Statistik (aus dem Pfeil-Eis)
   und Spin (aus einer Zusatzstruktur) auf verschiedenen Bauteilen [ES]; in einer lorentzinvarianten Welt waere ein
   spinloses Fermion verboten (Spin-Statistik-Satz [L]).
6. **Q-Baelle und Fermionen:** Q-Baelle sind bosonisch. Fermionisch werden sie im Projekt nur als Dyon (Ladung plus
   Monopol) oder nach einem Umbau des Feldes (Knoten-Weg C x S^2, laut STRATEGIE-SPIN unter "Parken" "radial
   verworfen");
   das Dyon ist nach DYON-STATISTIK-L stark ans Licht gekoppelt (alpha >= 1,45 im Quanten-Spin-Eis, [ES dort]). Ein
   elektronartiges, schwach gekoppeltes Fermion braucht den Fadenend-Weg. Q-Baelle und Elektronen sind also in keinem
   Bild dasselbe Objekt.
7. **Kausalmenge und Punktteilchen:** schliessen sich aus (Varianz 1/4 je Schritt, Heizen); verlangt sind
   ausgedehnte Objekte. Ausgedehnte, massive Felder sind in 3+1 aber gerade die instabilen (Johnstons Mittel waechst,
   KAUSAL-4D-STABIL-L). Auf Buehne B hat damit weder das Punkt- noch das Wellenbild in 3+1 einen funktionierenden
   massiven Vertreter.
8. **Zeitbegriff:** A1 und C haben eine globale Zeit, A2 und B eine lokale. Die 1/2-Regel steht nur dort von selbst,
   wo die Zeit lokal ist (eingebaut in A2, [H] fuer B). Finns Pfeil-Eis (A1) und die 1/2-Regel passen also nicht
   von selbst zusammen; das sagt der Weichenstand richtig.

**Widerspruchsfreie Kombinationen [ES]:** (i) A1: Pfeil-Eis-Licht + Fadenend-Fermionen + Q-Baelle, Schwerkraft als
Tensor-Eis auf einer Tetraedersorte [H]; (ii) A2: Regge-Schwerkraft + darauf gesetzte Felder (Materie auf Regge nicht
gerechnet); (iii) B: Kausalmenge + nichtlokale Wellen + Schwerkraft aus der Benincasa-Dowker-Wirkung [L, nicht
gerechnet]. Die Mischung aus der KARTE (Frage 2) "Schwerkraft aus Materie euklidisch, Wellen auf der Kausalmenge,
Licht und Fermionen im Pfeil-Eis" ist keine Buehne, sondern eine Sammlung; die Schichtidee in
UEBERLEITUNGEN-EMERGENZ.md ("unten Ereignisse oder Pfeile, darueber Laengen, oben Materie") ist ausdruecklich [H].

## 3. Aeussere Passung

Kandidaten (Begruendung in Abschnitt 4): **K-A** Finns Pfeil-Eis-Netz (A1: Tetraeder-Netz, aeussere Uhr; Licht,
Fadenend-Fermionen, Tensor-Eis); **K-B** Ereignis-Netz mit Zahl = Volumen (Kausalmenge; B-eukl. nur als euklidisches
Werkzeug); **K-M** Mischform Laengen-Netz in Raum und Zeit (A2, Regge; Schwerkraft eingebaut oder als Echo der
Materie).

Quellenmarken: **[S]** von mir an der lokalen Kopie gelesen; **[P]** Projektdatei, dort als an der Quelle gelesen
markiert ([A]), von mir nicht an der Primaerquelle geprueft; **[L]** Literatur aus dem Gedaechtnis.

| Messgroesse (Wert, Fundstelle) | K-A Finns Netz | K-B Kausalmenge | K-M Regge-Raumzeit | Projekt-Fundstelle |
|---|---|---|---|---|
| Lorentz-Invarianz, Glieder der Dimension 4: Anisotropie Delta c/c ~ 1e-17; Photonsektor bis 1e-22 bzw. 1e-20; Neutron-Koeffizienten ~1e-29 [P: art-grenzen-20260921/LORENTZ.md Z. 56-59]. Ein Ruhesystem auf Planck-Skala gibt Verletzung "at the percent level ... unless the bare parameters ... are unnaturally strongly fine-tuned" [S: Collins u. a. 2004, Abstract, induziert-g-l/quellen/api-A8.xml] | **verletzt ohne Abstimmung**: festes Netz hat ein Ruhesystem; eigenes Tempo je Sorte | **erfuellt im Prinzip**: keine Vorzugsrichtung [S: Bombelli/Henson/Sorkin, quellen/api-abstracts-1.xml]; im Projekt gezeigt fuer Linkrichtungen (KAUSAL-1), Punktlaeufer (KAUSAL-SWERVE-1: gleich stark in jedem Bezugssystem) und Skalarwellen in 1+1 (KAUSAL-WELLE-1) | **klassisch erfuellt, quantenmechanisch gefaehrdet**: festes Gitter, Ruhesystem an der Masche; Collins gilt [ES] | REGGE-WELLE-1; LICHT-GLEICH-L; KAUSAL-WELLE-1 |
| Planck-unterdrueckte Dispersion: E_QG,1 > 10 E_Pl (linear), E_QG,2 > 6e-8 E_Pl (quadratisch), 95 % [S: LHAASO, RUNDE-34/grb-221009a/quellen/lhaaso-2402.06009.txt Z. 126-127] | Photonen: nicht gerechnet. Gravitonen einer Kopie spalten linear in abs(k) [E] | ohne Vorzugsrichtung keine richtungs- oder bezugssystemabhaengige Lichtgeschwindigkeit [ES/L]; 1+1 im Mittel wie das Kontinuum; 3+1 weicht das Mittel bei endlicher Dichte vom Kontinuum ab (KAUSAL-WELLE-4D); Einzelnetz-Rauschen | quadratisch, unterhalb von c: 1 - v = (1 + Summe n_i^4) k^2/24 [E]; bei Planck-Masche erfuellt [ES]; schiefes Netz zum Teil schneller als Licht [E] | REGGE-WELLE-1, -SCHIEF-1; TENSOR-EIS-PYRO-1 Abschn. 4.2 |
| Zittern und Impulsdiffusion durch Koernigkeit ohne Ruhesystem (nur K-B betroffen) | nicht anwendbar | **ungetestet**: Punktteilchen bei Planck-Schritten ausgeschlossen [P: UEBERLEITUNGEN Ue3, dort L]; Wellen zittern in 1+1 noch um 0,1 bis 2,5 % der Lichtgeschwindigkeit (rho = 50 bis 800, KAUSAL-WELLE-1); Hochrechnung auf Planck-Dichte und Vergleich mit Messschranken fehlen [ES]; Literatur zu Schranken [L?, nicht gelesen] | nicht anwendbar | KAUSAL-SWERVE-1; KAUSAL-WELLE-1 |
| Licht und Schwerkraft gleich schnell: -3e-15 <= c_T - 1 <= 7e-16 [S: Guemruekcueoglu u. a., Gl. (13), licht-gleich-l/quellen/arxiv-1711.08845.txt Z. 145] | **verletzt ohne Abstimmung** (Graviton- und Lichttempo unabhaengige Parameter) | erfuellt im Prinzip (gemeinsame Ordnung) [ES]; Gravitonen nicht gerechnet | Gravitonen mit c [E, eingebaut]; Licht auf Regge nicht gerechnet: **ungetestet** | LICHT-GLEICH-L |
| Aequivalenzprinzip: eta = [-1,5 +- 2,3 +- 1,5]e-15 (MICROSCOPE); aktiv/passiv 3,9e-14 (LLR) [P: LORENTZ.md Z. 45; WARUM-SPIN-2.md Z. 775-782] | **verletzt** im gerechneten Bau: Massen in verschiedenen Kopien ziehen sich nicht an [E]; mit einer Kopie ungetestet | ungetestet | **erfuellt durch Konstruktion** (Masse koppelt an die Eigenzeit, REGGE-ZEIT-1); mit verschiedenen Stoffen nicht geprueft. REGEL-1 zeigte gleiches Fallen nur bei Energiekopplung (Ladungskopplung: abs(eta) = 0,19), auf einem kubischen Raum-Netz mit eingebauter Regel | TENSOR-EIS-PYRO-1; REGGE-ZEIT-1; RUNDE-36 REGEL-1 |
| Newton und ART: gamma - 1 = (2,1 +- 2,3)e-5 (Cassini) [P: LORENTZ.md Z. 217] | Newton 1/r in einer Kopie [E]; gamma nicht gerechnet | ungetestet | Newton und gamma = 1 im Fernfeld [E, Regge eingesetzt]; Gitterabweichung einige Prozent bis ~10 Maschen | REGGE-ZEIT-1 |
| Spin-Statistik | **verletzt im gerechneten Bau**: Fadenende ist ein spinloses Fermion (TWIST-SPIN-1) [G/M]; halber Spin nur mit Zusatzzustaenden oder Fluss pi von Hand [H]; ohne Lorentz-Invarianz ist der Zusammenhang nicht garantiert [L] | offen: Spinoren brauchen Zusatzstruktur | ungetestet | TWIST-PYRO-1; SPIN-KAUSAL-L |
| Chirale Fermionen, SU(3) x SU(2) x U(1) [L: Nielsen/Ninomiya als Huerde fuer Gitter] | **nicht erfuellt**: nur U(1), statisch gerechnet; Fermionen vektorartig, Verdoppler bzw. raues Band | nicht anwendbar bisher (nichts gebaut) | nicht anwendbar bisher | QCA-DIRAC-T-1; QCA-BCC-RUECK-1; SPIN-ZUFALLSNETZ-1 |
| Drei Generationen, Massen, Hierarchien | nicht erklaert (QCA-Masse m freier Parameter) | nicht erklaert | nicht erklaert | - |
| Kosmologische Konstante, ~1e-122 in Planck-Einheiten [L] | Vakuumenergie je Zelle, Abzug noetig: **Feinabstimmung** [M/H, UEBERLEITUNGEN Ue1] | **Plus**: Zahl = Volumen macht den Volumenterm unimodular-artig; Kausalmenge plus Unimodularitaet sagt ein schwankendes Lambda "of order the ambient density" [S: Ahmed/Dodelson/Greene/Sorkin, Abstract]; im Projekt nicht gerechnet, Vertraeglichkeit mit kosmologischen Daten von mir nicht geprueft | wie K-A | INDUZIERT-KUGEL-1 Abschn. 3.2: Gamma/N = 1,21 bis 1,32 je Punkt [E], also ein Vakuumglied der Ordnung 1 je Punkt; mit l_P von etwa 0,9 Abstaenden (Abschn. 3.3, "von Hand") etwa je Planck-Zelle [ES] |
| 3+1 Dimensionen | eingegeben | eingegeben; Entstehen aus Kausalmengen-Dynamik offen [L] | eingegeben (CDT-Literatur: 4D entsteht [L]) | alle Karten |
| Unitaritaet, Stabilitaet | Hamilton-Gitter bzw. QCA unitaer durch Bau [M]; Tensor-Eis ohne Zwang an 98 % der k wachsend [E] | massive Felder in 3+1: Mittel waechst; masseloser BD-Operator UV-instabil [P: KAUSAL-4D-STABIL-L, dort S]: **offen bis negativ** | schiefes Netz: anwachsende Gitterwelle, Vorzeichenwechsel je Zeitschritt [E]; Polchinski-Einwand [H] | KAUSAL-WELLE-4D; REGGE-WELLE-SCHIEF-1 |
| Kuenftig: Quanten-Natur der Schwerkraft (BMV): Verschraenkung nur ueber einen Quanten-Vermittler [S: Bose u. a. 2017, Abstract] | ungetestet; Tensor-Eis waere ein Quantenmodell [H] | ungetestet | ungetestet | in B-eukl. ist die Geometrie nicht quantisiert gerechnet |
| Messdatenstrang: weite Doppelsterne (KS-1) | sagt keine Abweichung vorher [ES] | ebenso | ebenso | Strang nicht an das Weltmodell gekoppelt |

**Urteil je Kandidat [ES]:**

- **K-A:** Zwei harte Verletzungen ohne Abstimmung (Lorentz-Invarianz in Dimension 4; GW170817), zwei im gerechneten
  Bau (gleiches Fallen ueber Kopien; spinloses Fermion nach TWIST-SPIN-1), dazu Standardmodell nicht erreichbar mit
  vektorartigen Fermionen. Haltbar nur,
  wenn eine Schutzsymmetrie die Tempi aller Sorten gleichsetzt; eine solche ist auf Finns Netz nicht bekannt.
- **K-B:** Keine harte Verletzung, aber fast alles **ungetestet**, auch sein eigener Gegentest (Zittern durch die
  Koernigkeit). Strukturell der einzige Kandidat, der Lorentz-Tests ohne Abstimmung bestehen kann, und der einzige, bei dem eine Idee zur kosmologischen Konstante aus dem Bau folgt
  (Zahl = Volumen). Das offene Gegenargument
  ist innen: Materie in 3+1 laeuft bisher nicht stabil, Fermionen und Licht fehlen.
- **K-M:** Besteht die klassischen Schwerkrafttests, weil Regge eingesetzt ist; Licht und Materie darauf ungerechnet;
  Lorentz-Invarianz nur bis zur Quantenkorrektur.

## 4. Kandidaten

### K-A: Finns Pfeil-Eis-Netz (Buehne A1; Ueberleitung 2)

- **Bild:** Tetraeder-Netz (Diamant bzw. Pyrochlor-Kanten) mit aeusserer Uhr. Pfeile = Licht, Enden verdrehter Faeden =
  Fermionen, Tensor-Eis = Gravitonen, Q-Baelle = Materie.
- **Staerken:**
  - die einzige Buehne mit drei Kernbausteinen zugleich, jeder nur teilweise (Abschnitt 2) [ES]
  - lokal, unitaer, mit kleinen Tests erreichbar
  - Existenzbeweis in der Literatur: emergentes Licht plus Fermionen aus einem lokalen Bosonmodell (Levin/Wen) [P:
    TWIST-PYRO-1, DYON-STATISTIK-L, dort S]
  - Q-Ball merkt das Netz kaum (0,82 % bzw. 0,80 %, QBALL-PYRO-1)
- **Schwachstellen:**
  - Ruhesystem; eigenes Tempo je Sorte; nach Collins u. a. [S] und GW170817 [S] nur mit Feinabstimmung haltbar
  - die 1/2 ist auf diesem Netz keine exakte Symmetrie (Spur-Eichdefekt bis 1,0); ohne Zwang waechst an 98 % der
    Gitterpunkte im k-Raum eine Mode
  - Gravitonen doppelt
  - Fadenend-Fermion spinlos (TWIST-SPIN-1); halber Spin nur eingesetzt
  - nur U(1), vektorartige Fermionen; Quanten-Licht auf Finns Netz nicht gerechnet; Tensor-Eis nur linear und klassisch
- **Was ihn retten koennte [H]:** eine Symmetrie des Netzes, die Licht-, Fermion- und Graviton-Tempo aufeinander
  abbildet (Weg b in LICHT-GLEICH-L). Keine ist bekannt.

### K-B: Ereignis-Netz mit Zahl = Volumen (Buehne B; Ueberleitung 3, mit B-eukl. als Werkzeug)

- **Bild:** zufaellig gestreute Ereignisse mit Vorher/Nachher; Volumen = Anzahl; Teilchen als ausgedehnte Wellen;
  Schwerkraft als Echo der Materie oder aus der Benincasa-Dowker-Wirkung.
- **Staerken:**
  - kein Ruhesystem, auch nicht lokal [S: Bombelli/Henson/Sorkin, Abstract: "will not pick out a preferred frame,
    locally or globally"]
  - gemeinsamer Lichtkegel fuer alle Felder durch die Ordnung [ES/L]
  - Idee zur kosmologischen Konstante [S: Ahmed u. a., Abstract]
  - Wellen in 1+1 im Mittel exakt (KAUSAL-WELLE-1)
  - Das euklidische Werkzeug trifft die universelle 2D-Anomalie (zwei unabhaengige Zahlen um 1: 1,075 +- 0,071 und
    0,92 +- 0,12) und gibt auf S^4 das Vorzeichen, das Einstein verlangt, nach XI-KUGEL-1 aber zu rund 70 % aus
    Gitter-Eigenheiten und mit Kipppunkt 0,555 statt 1/6.
- **Schwachstellen:**
  - nicht lokal; nach demselben Satz gibt es keinen Graphen endlicher Valenz, der mit Lorentz-Invarianz vertraeglich
    ist [S]
  - Materie in 3+1 nicht stabil: Johnstons Mittel waechst; Abhilfe kostet je Ordnung eine exakte Bedingung, das
    Einzelnetz-Rauschen waechst (V-00: 1,61) [E]
  - Punkte zittern und heizen
  - Spinoren brauchen Zusatzstruktur; Licht und Eichfelder nicht gebaut
  - Schwerkraft auf der Kausalmenge selbst nicht gerechnet; die induzierte Schwerkraft ist euklidisch, auf einer
    anderen Netzart, und in 4D zwischen Kugel (-1,65 +- 0,05) und Torus (+1,24 +- 0,50) widerspruechlich
  - Dynamik der Ordnung (warum eine Raumzeit-artige Kausalmenge?) offen [L]

### K-M: Laengen-Netz in Raum und Zeit (Buehne A2, Regge bzw. CDT; Ueberleitung 1 auf festem Gitter)

- **Bild:** 4-Simplizes mit Laengen auf Raum- und Zeitkanten; Finns Tetraeder sind die Zeitschnitte
  (RAUMZEIT-NETZ.md, Lesehinweis); Felder sitzen auf denselben Laengen.
- **Staerken:**
  - die einzige Buehne, auf der die klassische Einstein-Struktur steht: Newton, gamma = 1, zwei Polarisationen mit c
    [G]; gleiches Fallen ist hier durch die Kopplung der Masse an die Eigenzeit eingebaut (REGGE-ZEIT-1), gezeigt wurde
    es nur auf einem kubischen Raum-Netz mit eingebauter Regel und nur bei Energiekopplung (REGEL-1, RUNDE-36)
  - lokale Zeit, also die 1/2 eingebaut
  - Gitterkorrekturen im regelmaessigen Netz quadratisch und unter c
- **Schwachstellen:**
  - Schwerkraft eingesetzt; als Echo der Materie auf festen Netzen gescheitert (INDUZIERT-1, INDUZIERT-ZUFALL-2D: nur
    Gitterterme)
  - Ruhesystem an der Masche, also Collins-Problem auf Quantenebene [ES]
  - schiefe Netze doppelbrechend, teils schneller als Licht, mit anwachsender Gitterwelle
  - Licht, Fermionen und Q-Baelle auf Regge nicht gerechnet
  - CDT in 2+1 nicht beim Einstein-Wert [P: CDT-HORAVA-L, dort S, Tagungsarbeit]

### Unterscheidungspunkte

| Paar | Unterscheidungspunkt | Stand |
|---|---|---|
| K-A gegen K-B | Ruhesystem ja/nein: sortenabhaengige Grenzgeschwindigkeiten und Anisotropie (Glieder der Dimension 4) | **schon gemessen**: Schranken 1e-15 bis 1e-29; K-A braucht Feinabstimmung oder eine Schutzsymmetrie, K-B nicht [ES aus S] |
| K-A gegen K-M | globale gegen lokale Zeit: folgt die 1/2 von selbst? | K-M ja (eingebaut), K-A nein (Defekt bis 1,0) [E] |
| K-M gegen K-B | lokal mit Masche-Ruhesystem gegen nicht lokal ohne Ruhesystem; im Experiment: Lorentz-Verletzung auf Quantenebene (K-M) gegen Zittern/Diffusion im Impuls und schwankendes Lambda (K-B) | rechnerisch: Kann K-B Materie in 3+1 stabil tragen? Kann K-M Schwerkraft aus Materie bekommen? |

**Rangfolge der Kandidaten [ES]:** Nach der aeusseren Passung ist **K-B der einzige Kandidat ohne strukturelle
Verletzung**, aber nur, weil fast alles an ihm ungetestet ist. Nach dem Inhalt ist **K-A der reichste**, aber nach
heutigem Wissen nur mit Feinabstimmung mit den Lorentz-Messungen vereinbar. K-M liegt dazwischen: klassische Schwerkraft
vollstaendig, aber eingesetzt, und dasselbe Ruhesystem-Problem wie K-A. Ein "staerkster Kandidat" im Sinn von "passt"
existiert nicht; "kann noch passen" gilt nur fuer K-B.

## 5. Luecken und Rangliste

### Luecken bis "passt"

| Nr | Luecke | Art | vorab ableitbar? | kleiner Test (<= 10 min)? | Erkenntniswert |
|---|---|---|---|---|---|
| L1 | Schutz der Lorentz-Invarianz auf festen Netzen (K-A, K-M) | Begriff, Literatur | **ja, negativ**: Collins u. a. [S]; LICHT-GLEICH-L: Lauf von Planck bis m_e senkt einen Unterschied nur um 0,89 [P, dort ES] | nicht noetig | hoch: entscheidet Weiche A |
| L2 | Tensorstruktur und Kovarianz der induzierten Wirkung in 4D (Kugel gegen Torus; die 1/2 im induzierten Glied) | Rechnung | **nein**: Gitterkovarianz in Ordnung Lambda^2 ist genau das Offene; nur die Kontinuumsvorhersage aus dem gemessenen B ist vorab rechenbar | ja (gepaarte Netze wie KUGEL-1/-2) | hoch: entscheidet, ob Schwerkraft aus Materie in 4D Einstein ist |
| L3 | Uebertragung B-eukl. auf eine lorentzsche Buehne | Begriff, Rechnung | nein | nein | hoch, aber ausser Reichweite kleiner Tests |
| L4 | Massive Materie in 3+1 auf der Kausalmenge | Rechnung | Mittel ja (wie die Restformel in KAUSAL-4D-SCHICHT-2, 3 bis 4 %), Einzelnetz-Rauschen nein | ja (Groessen wie SCHICHT-1/-2) | hoch fuer K-B |
| L5 | Spin 1/2 und Dirac-Ausbreitung der Fadenenden (K-A) | Begriff | **ja**: Fluss 0 (TWIST-SPIN-1) gibt keine Dirac-Kegel; masselose Dirac-Fermionen bei Levin/Wen nur mit eingebautem Fluss pi, und dann vier Kopien [S: hep-th/0507118, lokale Kopie twist-pyro-1/quellen/, Z. 1288-1300 und 1323-1365]; Diamant-Knotenlinien, Pyrochlor-Flachbaender [P: RUNDE-40.md Z. 200, dort L] | nicht noetig | mittel; schon entschieden: nicht von selbst |
| L6 | Chirale Fermionen, nichtabelsche Eichgruppe | Literatur | Forschungsstand, nicht im Projekt | nein | sehr hoch: ohne sie passt kein Kandidat |
| L7 | Doppelte Gravitonen (K-A) | Bauregel | ja: Werte nur auf einer Tetraedersorte gibt eine Kopie, weil die Kopien exakt entkoppeln (TENSOR-EIS-PYRO-1) [ES] | nicht noetig | niedrig |
| L8 | Selbstkopplung der Schwerkraft, nichtlinear | Rechnung | teils (Wald, Deser [P: WARUM-SPIN-2.md Glied 9/10]) | nein | mittel |
| L9 | Kosmologische Konstante (K-B) | Literatur | ja, Literatur | nein | mittel |
| L10 | Netzdynamik: warum dieses Netz, warum 3+1 | Rechnung, Begriff | nein | nein | sehr hoch, ausser Reichweite |
| L11 | Generationen, Massen, Hierarchien | Begriff | nein | nein | ausser Reichweite |

### Rangliste der naechsten Schritte (Anforderungen, kein Vertragswortlaut)

1. **Weiche A nach dem Ableitbaren entscheiden (Schreibtisch und Finn, keine Rechnung).**
   - Frage an Finn: Soll ein Weltmodell mit festem Netz (K-A, K-M) gelten, das die Lorentz-Messungen nur mit
     Feinabstimmung besteht?
   - Vorher als Schreibtischprobe (eine Seite): Gibt es auf Finns Netz eine Symmetrie, die die Tempi aller Sorten
     aufeinander abbildet (Weg b aus LICHT-GLEICH-L)?
   - **Ableitbarkeitsprobe:** Ausgang aus Literatur ableitbar (Collins u. a. [S]; Levin/Wen stimmen t ab [P, dort
     S-lokal]); deshalb keine Rechnung.
   - **Wirkung:** Bei "nein" bleibt Finns Netz ein Baukasten fuer Analogien, nicht das Weltmodell. Bei "ja" muss das
     Weltmodell-Dokument die Abstimmung als Annahme fuehren.
2. **Kovarianztest der induzierten Wirkung auf S^4 (Rechnung, B-eukl.).** Anforderungen:
   - Gepaarte Netze: dieselben Zufallspunkte, fuer jede Verformung mit einer festen, glatten Abbildung so verschoben,
     dass die Punktdichte bezueglich der neuen Metrik wieder 1 ist; verglichen werden die runde S^4, eine volumentreue
     spurfreie Verformung (gestauchte Kugel) und eine konforme l = 2-Verformung. Ob die Triangulierung mitgenommen oder
     neu gebaut wird, ist vorab festzulegen; beides hat einen eigenen Rauschpreis.
   - Nullkontrolle: Eine Verformung, die nur eine Umbenennung ist (konformer Faktor einer Moebius-Abbildung der Kugel;
     in erster Ordnung die l = 1-Mode), muss mit derselben Bauvorschrift Antwort null geben. Scheitert sie, ist das
     Kugelvorzeichen nicht als G lesbar. Die Probe ist nur dann nicht trivial, wenn Punkte, Netz und Laengen fuer alle
     Verformungen nach derselben Vorschrift gebaut werden (wie beim Torus).
   - Zur Kontrolle der Vorzeichen [M, Schreibtisch, von mir gerechnet]: Fuer g = e^(2 sigma) g0 auf S^4 bei festem
     Volumen ist die zweite Variation von Int sqrt(g) R gleich (6 l(l+3) - 24)/a^2 mal Int sigma^2 fuer sigma = Y_l.
     Fuer l = 1 ist das 0 (Umbenennung), fuer l = 2 gleich 36/a^2 > 0. Mit B < 0 sinkt Gamma also bei konformer
     l = 2-Verformung; bei spurfreier Verformung muss es steigen (Kugel als Sattel).
   - "Zahl = Volumen" muss nach der Verformung lokal gelten (siehe erster Punkt), sonst misst man die Dichteaenderung.
   - Vorab-Datei: die Kontinuumsantworten aus dem gemessenen B (spurfrei und konform haben bei Einstein
     entgegengesetztes Vorzeichen) als Zahl mit Fehler.
   - **Ableitbarkeitsprobe:** nicht ableitbar. Ob das Gitter in Ordnung Lambda^2 kovariant ist, ist offen; Kugel und
     Torus widersprechen sich mit 5,7 SE. Vorab ableitbar ist nur die Kontinuumsvorhersage.
   - **Wirkung:** Kann scheitern (Nullkontrolle, Vorzeichen, Verhaeltnis). Trifft die Vorhersage, ist die 1/2 im
     induzierten Glied erstmals entstanden statt eingesetzt (P3, euklidisch, auf diesem Netz) und die Torus-Frage
     erledigt. Verfehlt sie, ist
     Schwerkraft aus Materie in 4D auf diesem Netz nicht Einstein.
   - Ersetzt TORUS-ARTEFAKT aus der Warteschlange; dieses erklaert nur einen Fehler.
3. **Massive Welle in 3+1 auf der Kausalmenge mit der Masse im Kern (Rechnung, K-B).** Anforderungen:
   - Die Masse sitzt im nichtlokalen Kern, nicht ausserhalb (KAUSAL-4D-STABIL-L Punkt 3).
   - Messgroessen: Pol des Mittels (Im omega) und relative Einzelnetz-Streuung gegen die Dichte.
   - Kriterium vorab: Das Mittel ist stabil und die Streuung faellt mit der Dichte. Sonst traegt K-B keine massive
     Materie auf diesem Weg.
   - **Ableitbarkeitsprobe:** Das Mittel ist vorab rechenbar und gehoert in die Vorab-Datei. Das Rauschen ist nicht
     ableitbar; nur dafuer lohnt die Rechnung.
   - Gegenfall: Die Literatur kennt keine stabile 4D-Familie (KAUSAL-4D-STABIL-L); ein Fehlschlag kann am Bau liegen
     statt an der Kausalmenge. Deshalb vorab festlegen, was als Bau- und was als Befundfehler zaehlt.
4. **Literaturkarte "chirale Fermionen und nichtabelsche Eichfelder aus lokalen bosonischen Netzen und auf
   Kausalmengen" (Literatur).**
   - Frage: Kann K-A oder K-B das Standardmodell auch nur im Prinzip tragen (Nielsen/Ninomiya; Spiegel-Fermionen mit
     Wechselwirkung abgeschaltet [L])?
   - **Ableitbarkeitsprobe:** Ausgang ist Forschungsstand, also ableitbar; deshalb Literatur statt Rechnung.
   - **Wirkung:** Ohne einen Weg zu chiralen Fermionen kann kein Kandidat "passen". Das ist die groesste Luecke.
**Waehrend des Reviews erledigt: INDUZIERT-XI-KUGEL-1 (Ergebnis 14:03 gelesen).**
- **Meine Ableitbarkeitsprobe vor dem Lesen [ES, M, grob]:** In erster Ordnung verschiebt xi R phi^2 den
  sqrt(N)-Koeffizienten um xi mal 30,8 mal g0. Herleitung: (1/2) xi (12/a^2) N g0 mit a^2 = 0,1949 sqrt(N);
  6/0,1949 = 30,8. Dabei ist g0 die mittlere, mit den Punktmassen gewichtete Diagonale der Pseudo-Inversen der
  Steifigkeit. Der Kipppunkt ist also xi* = 1,61/(30,8 g0), aus einer flachen Netzzahl vorab abschaetzbar.
- **Ausgang:** Der Agent schreibt dieselbe Beziehung (gamma = 30,78 g0, g0 = 0,094) und nennt XI1 "vorab praktisch
  entschieden". Probe: 1,6126/2,9047 = 0,5552; (0,5552 - 0,1667)/0,0177 = 22 SE. Eigenzeit-Lesart: 2,9047/6 = 0,484,
  also (1,61 - 0,48)/1,61 = 70 % gitterspezifisch.
- **Bedeutung fuer die Rangliste [ES]:** Das Einstein-Vorzeichen auf S^4 ist ueberwiegend eine Eigenschaft dieses
  Netzes und seiner Massendiskretisierung (xi* zwischen 0,52 und 1,25 je nach Konvention). Damit wird Schritt 2 noch
  wichtiger: Ob dieser gitterspezifische Anteil wenigstens kovariant ist, kann nur ein Verformungstest zeigen. Die
  Kugel allein kann das nicht. A2 (Abschnitt 6) wird durch XI-KUGEL-1 gestuetzt.

**Nicht empfohlen:** Bandstruktur der Fadenenden (L5, ableitbar und von der Leitung am 04.10. 12:13 schon verworfen,
RUNDE-40.md Z. 200), Tensor-Eis auf einer Tetraedersorte (L7, ableitbar), weitere Regge-Varianten (eingesetzt),
TORUS-ARTEFAKT (durch Schritt 2 ersetzt).

### Anforderungen an das Weltmodell-Dokument der Leitung

- **W1 Eine Buehne:** Das Wort "Weltmodell" nur fuer einen Kandidaten mit einer Buehne verwenden. Die Sammlung ueber
  alle Netzarten heisst "Baukasten".
- **W2 Herkunft je Baustein:** eingesetzt, entstanden oder algebraisch, dazu Netzart und Kennzeichen (Tabelle wie in
  Abschnitt 1). Belege verschiedener Buehnen nie in einem Satz verbinden, ohne die Buehnen zu nennen.
- **W3 Aeussere Passung mit Zahlen:** Tabelle wie in Abschnitt 3. Jedes "erfuellt" mit "durch Konstruktion" oder
  "entstanden" kennzeichnen.
- **W4 Schwerkraft aus Materie in 4D:** Zu sagen ist: Vorzeichen auf S^4, ueberwiegend gitterspezifisch
  (XI-KUGEL-1), vom Torus widersprochen, Tensorstruktur ungemessen. Keine Formulierung "Einstein entsteht".
- **W5 Fermionen:** Verdoppler (16 Kegel), vektorartige Masse, spinloses Fadenende, BCC statt Finns Netz.
- **W6 K-A nur mit Annahme:** Wird Finns Netz als Weltmodell gefuehrt, steht die Feinabstimmung der Tempi als
  ausdrueckliche Annahme mit den Schranken (GW170817 1e-15; Photonsektor bis 1e-22) im Text.
- **W7 Erste Luecke:** Das Standardmodell (chirale Fermionen, nichtabelsche Eichgruppe, Generationen, Massen) zuerst
  nennen, nicht zuletzt.
- **W8 Datenstrang:** KS-1 bzw. "M1 weite Doppelsterne" nicht als Test des Weltmodells fuehren und vom Q-Ball-Modell M1
  sprachlich trennen.
- **W9 Lesen:** Zahlen aus den Primaerdateien; ein frischer Leser liest das Dokument in beide Richtungen.

## 6. Fehler im Stand (Befunde A/B/C)

Klassen: **A** = falsch oder fuer die Weltmodell-Frage irrefuehrend zu stark, vor Weitergabe zu aendern; **B** = fehlende
Einschraenkung oder zu weiches Urteilswort; **C** = Kennzeichen, Benennung, Kleinigkeit. "v5" = RUNDE-40/WEICHE-STAND-v5.md.
Die Negativliste der KARTE ("das Gegenteil des Torus-Befunds", "ab 8 Zustaenden", "Masse nur mit Inversion", "traegt
Licht und Fermionen", "laeuft" fuer "funktioniert") habe ich per grep in v5 gesucht: nicht mehr vorhanden; "laeuft"
steht nur noch in "Rechnung laeuft" (Z. 25, 66), dort richtig.

### A-Befunde

**A1 (v5 Z. 27, Zeile "Teilchen mit halbem Spin", Spalte A): Die Verdoppler der QCA fehlen, und das Gitter ist nicht
Finns Netz.**
- Quelle: QCA-BCC-RUECK-1, ERGEBNIS Z. 51-52 ("an H, P und P' sitzen je vier weitere Kegel (Verdoppler)") und Z. 144
  ("16 Weyl-Kegel in der Zone"); QCA-DIRAC-T-1, ERGEBNIS Z. 65 ("In Konstruktion (a) und in 13 von 17 Form-P-Treffern
  bleiben an P und P' Kegel, also masselose Verdoppler"); QCA-DIAMANT-4, Ergebnis 2 (auf dem Diamant generisch nur L_2).
- Warum A: Fuer die Weltmodell-Frage entscheidet die Zahl der Teilchensorten (Nielsen/Ninomiya). "Mit 8 gibt es
  welche" und "Masse gibt es mit Inversion" lesen sich als ein Fermion; tatsaechlich sind es 16 Kegel, und die massive
  Bauart laesst masselose Kopien zurueck.
- **Vorschlag im Wortlaut** (an "Masse gibt es mit Inversion (QCA-DIRAC-T-1)" anschliessen): "Jeder gefundene
  8-Zustands-Automat hat ausser den vier Kegeln bei k = 0 je vier weitere an H, P und P' (Verdoppler, zusammen 16); in
  der massiven Bauart bleiben die Verdoppler an P und P' meist masselos (QCA-BCC-RUECK-1, QCA-DIRAC-T-1). Die
  Automaten leben auf BCC, nicht auf Finns Diamant-Netz; dort gibt es Spin-1/2-Kegel generisch nur mit der kleinen
  Gruppe L_2 (QCA-DIAMANT-4)."

**A2 (v5 Z. 25 und Z. 43, Schwerkraft aus Materie in 4D): Urteilswort "teilweise" und "[M]" tragen mehr, als die Kugel
zeigen kann.**
- Quelle: INDUZIERT-KUGEL-1, ERGEBNIS Z. 276-277 ("Das Vorzeichen von B ist aus einer Geometrie gelesen; die konforme
  Mode oder negative Kruemmung sind auf diesem Weg nicht geprueft") und Z. 283-288 (Tensorform als naechster Schritt);
  KUGEL-2 Ergebnis 3 (Gs-Lesart +4,21, Modell verworfen); KU2 per jq: 5,715 SE zwischen Kugel und Torus.
- Warum A: "B < 0 heisst positives G" gilt nur, wenn die induzierte Wirkung die Einstein-Wirkung ist. Das kann die
  homogene Kugel nicht pruefen. Die einzige nicht homogene 4D-Messung (Torus, konforme Mode) gab das Gegenvorzeichen.
  Die Tensorstruktur ist nicht gemessen. "Teilweise" an erster Stelle liest sich als Teilerfolg; belegt ist ein
  Vorzeichen in einer Formfamilie, dem eine zweite Konstruktion mit 5,7 SE widerspricht. Fuer K-B ist das der
  tragende Satz.
- Nachtrag nach XI-KUGEL-1 (fertig waehrend des Reviews): Der Kipppunkt liegt bei xi* = 0,555 +- 0,018 statt bei 1/6
  (22 SE); in der Lesart des Agenten stammen rund 70 % des Glieds aus Gitter-Eigenheiten. Das Vorzeichen ist damit
  ueberwiegend eine Eigenschaft dieses Netzes, nicht der Kontinuumsmechanismus. v6 sollte das in derselben Zelle sagen.
- **Vorschlag im Wortlaut:** In Z. 25 "4D teilweise:" ersetzen durch "4D offen, zwei Konstruktionen widersprechen
  sich:". "das ist Einsteins Vorzeichen [M, unter Kugelsymmetrie]" ersetzen durch "das ist das Vorzeichen, das Einstein
  verlangt, falls die induzierte Wirkung kovariant ist; das kann die homogene Kugel allein nicht pruefen, und die
  Tensorstruktur ist nicht gemessen [M]". In Z. 43 nach "Einsteins Vorzeichen" einfuegen: "(unter der Annahme
  kovarianter Anteile, die die Kugel nicht prueft)".

### B-Befunde

**B1 (v5 Z. 27 und Z. 57-58, Fermionen im Pfeil-Eis): Eine der Leitung bekannte Einschraenkung fehlt; dazu die
Fortschreibung nach TWIST-SPIN-1.**
- Quelle: RUNDE-40.md Z. 200 (Leitung, 12:13:48, also vor v5): masselose Dirac-Fermionen bei Levin/Wen nur mit
  eingebautem Fluss pi; selbst gelesen [S] in twist-pyro-1/quellen/arxiv-hep-th-0507118.txt Z. 1288-1300 (Minimum bei
  Fluss 0: gaps bzw. Fermi-Fluessigkeit) und Z. 1323-1365 (Dirac nur in einer pi-Fluss-Konfiguration, "a total of 4
  massless four component Dirac fermions"). TWIST-SPIN-1: Fluss 0 auf allen Schleifen, Fadenende spinlos.
- **Vorschlag im Wortlaut** (ersetzt "nicht gezeigt: Spin 1/2, Licht (Coulomb-Phase), Kopplung ans Licht"): "Auf Finns
  Netz ist das Fadenende ein spinloses Fermion: Statistik -1, unter den Tetraeder-Drehungen ganzzahliger Spin
  (TWIST-SPIN-1). Es sieht ueberall den Fluss 0 und hat damit keine Dirac-Kegel; masselose Dirac-Fermionen entstehen
  bei Levin/Wen nur mit von Hand eingebautem Fluss pi, und dann in vier Kopien. Nicht gezeigt: Coulomb-Phase, Kopplung
  ans Licht."

**B2 (v5 Z. 27, Spalte B-eukl.): Urteilswort "offen" und fehlendes Soll beim Wilson-Fermion.**
- Quelle: INDUZIERT-WILSON-2D, ERGEBNIS Z. 27 ("Die Schwerkraft-Antwort ist trotzdem nicht die eines
  Dirac-Fermions"); jq: c_eff(W1) = -0,995 +- 0,552. Abstand zu +1: (1 + 0,995)/0,552 = 3,6 SE; W05: (1 + 0,259)/0,56 =
  2,2 SE. Dazu Z. 34: W1 + 4 B = 2,55 +- 0,04 gegen 5 im Kontinuum. Die Ernte sagt es noch: "Die Schwerkraft-Antwort
  stimmt trotzdem nicht" (RUNDE-40.md Z. 325); in v5, dessen Wortlaut laut Kopf den Ernten folgt, fehlt der Satz.
  Einschraenkung aus derselben Ernte: Mit k^6-Glied gibt W1 0,89 +- 1,5, also unentschieden.
- **Vorschlag im Wortlaut:** "offen (2D):" ersetzen durch "bisher nein (2D, Hauptfit; mit k^6-Glied unentschieden):";
  nach "-0,26 +- 0,56 (r = 1/2)" einfuegen: "(Soll +1 fuer ein Dirac-Fermion; 3,6 bzw. 2,2 SE darunter)".

**B3 (v5 Z. 27 und Z. 49): "Band stummer Zustaende" verharmlost.**
- Quelle: SPIN-ZUFALLSNETZ-1, ERGEBNIS Z. 293-297: Das Band wirkt auf "Vakuum und Dirac-See, Waerme,
  Wechselwirkungen", "besonders Eichfelder"; rho(0) = 0,463 je Knoten, im Fenster eps = 0,2 also 685 Kegel-Einheiten
  statt einer (ERGEBNIS Ergebnis 2); ausgedehnt (IPR x N = 1,7). "Stumm" ist es nur fuer langwellige Proben.
- **Vorschlag im Wortlaut:** "stummer Zustaende" ersetzen durch "von Zustaenden, die langwellig kaum sichtbar sind,
  aber nahe Energie null hunderte Male dichter liegen als der Kegel (685-fach im Fenster 0,2) und auf Vakuum, Waerme und
  Eichfelder wirken wuerden".

**B4 (v5 Z. 23 und Z. 60-63, Gravitonen auf Finns Netz): "ja" ohne die Bedingung der Zwangsflaeche.**
- Quelle: TENSOR-EIS-PYRO-1, ERGEBNIS Ergebnis 3 und 5: Zwei Moden je Kopie gibt es "auf der Zwangsflaeche (strenge
  Regeln)"; ohne Zwang waechst an 98 % der Gitter-k eine Mode (Rate bis 2,0). Der Spur-Eichdefekt geht bis 1,0; die
  Zwangsflaeche ist also nicht die Flaeche einer exakten Symmetrie.
- **Vorschlag im Wortlaut:** In Z. 23 nach "ja in einer von drei gerechneten Bauweisen" einfuegen: "und nur mit von Hand
  gesetzten strengen Regeln (ohne sie waechst an 98 % der Gitterpunkte eine Mode)".

**B5 (v5 Z. 28 und Z. 53-56, P1 "Ein Tempo fuer alles", Spalte A): Urteil "teilweise" ohne die Groessenordnung.**
- Quelle: Collins u. a. 2004, Abstract [S, induziert-g-l/quellen/api-A8.xml]: Verletzung "at the percent level, some
  20 orders of magnitude higher than earlier estimates, unless the bare parameters ... are unnaturally strongly
  fine-tuned". GW170817: -3e-15 <= c_T - 1 <= 7e-16 [S, licht-gleich-l/quellen/arxiv-1711.08845.txt Z. 145].
  LICHT-GLEICH-L Ergebnis 4: Luecke 13 bis 20 Groessenordnungen [P, dort ES].
- **Vorschlag im Wortlaut:** "teilweise:" ersetzen durch "klassisch ja, quantenmechanisch nach heutigem Stand nein:"; am
  Zellenende anfuegen: "Nach Collins u. a. (2004) gibt ein Ruhesystem auf Planck-Skala Verletzungen im Prozentbereich,
  ausser bei sehr starker Feinabstimmung; gemessen sind fuer Licht gegen Schwerkraft 1e-15 (GW170817)."

**B6 (STRATEGIE-SPIN-20261004.md Z. 9, "Lage in einem Satz"): "auf Finns Netzen sauber nachbauen" gilt nach
TENSOR-EIS-PYRO-1 nicht mehr.**
- Das Dokument ist von 05:55, vor TENSOR-EIS-PYRO-1. Sauber nachgebaut ist die Schwerkraft auf dem kubischen Netz
  (REGEL-1) und dem Kuhn-Regge-Gitter (REGGE-WELLE-1, REGGE-ZEIT-1). Auf Finns Tetraeder-Netz gibt es sie nur doppelt
  und nur mit von Hand gesetzten strengen Regeln. Die KARTE nennt das Dokument als Quelle fuer das Weltmodell.
- **Vorschlag im Wortlaut** (fuer jede Weiterverwendung): "Einsteins Schwerkraft laesst sich auf kubischen und
  Regge-Gittern sauber nachbauen [G], auf Finns Tetraeder-Netz nur doppelt und mit von Hand gesetzten Regeln
  (TENSOR-EIS-PYRO-1); ueberall war sie hineingesteckt."

**B7 (v5 Z. 58, Lesart "Finns Tetraeder-Netz"): "Licht gibt es klassisch als Coulomb-Phase" ist zu stark.**
- Quelle: FLUSS-1 (RUNDE-34), ERGEBNIS "Ergebnis zuerst": Paarpotential, Pfeil-Korrelationen und Strukturfaktor aus
  Monte Carlo, also eine statische Eigenschaft der Eisregel. Eine Dynamik oder Wellen kommen in der Datei nicht vor
  (grep nach "Welle", "Photon", "Dynamik": kein Treffer). Eine klassische Coulomb-Phase hat ein Coulomb-Gesetz, aber kein
  Licht; Photonen gibt es erst im Quanten-Pfeil-Eis [L: Quanten-Spin-Eis].
- **Vorschlag im Wortlaut:** "Ein Coulomb-Gesetz gibt es auf den Pyrochlor-Kanten als statische Eigenschaft der
  Eisregel (FLUSS-1: Paarpotential etwa 1/r, Korrelationen r^-3); Lichtwellen entstehen erst in einem Quanten-Pfeil-Eis,
  und das ist auf Finns Netz nicht gerechnet."

### C-Befunde

**C1 (v5 Z. 29; RAUMZEIT-NETZ.md Z. 20): "die 1/2-Regel wird zu 1/5" bzw. "gibt von selbst c = 1/5" ohne die Annahme.**
- Nachgerechnet [M]: Mit <n_i n_j n_k n_l> = (Summe der drei delta-Paare)/15 ist <(n.hdot.n)^2> =
  (2 tr(hdot^2) + (tr hdot)^2)/15 = (2/15)(tr(hdot^2) + (1/2)(tr hdot)^2). Also lambda = -1/2 und
  c = lambda/(3 lambda - 1) = (-1/2)/(-5/2) = 1/5. Arithmetik richtig.
- Die Zahl gilt aber nur fuer die Annahme "jede Kante hat eine eigene Bewegungsenergie, Richtungen gleichverteilt"
  (REGEL.md Abschn. 8). Jede Kopplung zwischen Kanten verschiebt lambda.
- **Vorschlag im Wortlaut:** v5 Z. 29: "Raum-Netz mit aeusserer Uhr, wenn jede Kante eine eigene Bewegungsenergie hat:
  die 1/2-Regel wird zu 1/5"; RAUMZEIT-NETZ.md Z. 20: "von selbst" ersetzen durch "bei je Kante eigener
  Bewegungsenergie"; Kennzeichen "[M, Leitung; Arithmetik von WELTMODELL-REVIEW-1 nachgerechnet]".

**C2 (RAUMZEIT-NETZ.md Z. 73): Kennzeichen kann von [L] auf [S] steigen.**
- Bombelli/Henson/Sorkin, Abstract (quellen/api-abstracts-1.xml): "there is no way to associate a finite-valency graph
  to a sprinkling consistently with Lorentz invariance".
- **Vorschlag:** "[S: Bombelli/Henson/Sorkin 2009, Abstract, WELTMODELL-REVIEW-1/quellen/]". Genau gelesen sagt der Satz
  das fuer Netze, die aus einem Sprinkling gebaut sind; fuer jedes lokale Netz in Lorentz-Signatur ist er die Lesart
  der Weiche [ES].

**C3 (KARTE dieses Reviews Z. 15 und Z. 39; Gesamtformel RUNDE-20/-24): Namensgleichheit und Zaehlung.**
- "M1" heisst im Q-Ball-Strang das Einfeldmodell (RUNDE-24.md, Gesamtformel Punkt 1), im Datenstrang die Hypothese zu
  weiten Doppelsternen (KS-1). Im Weltmodell-Dokument getrennt benennen, etwa "Q-Ball-Modell M1" und
  "Doppelstern-Befund M1".
- KARTE Z. 39 nennt "Pruefsteine P1 bis P4"; UEBERLEITUNGEN-EMERGENZ.md definiert P1 bis P6 (P5 Vakuumenergie, P6
  Lokalitaet). Beide fehlenden sind fuer das Weltmodell wichtig (Abschnitt 3).

**C4 (v5 Z. 28 und Z. 55): "Finns Fall" fuer das zusammengesetzte Photon ist eine Lesart.**
- Quelle: LICHT-GLEICH-L Z. 34 und Z. 212-213: Der offene Ausweg betrifft ein zusammengesetztes Eichboson bei starker
  Kopplung (Bednik u. a.: g4 >> 1). Ob Finns Pfeil-Eis-Photon in diesem Sinn zusammengesetzt und stark gekoppelt ist,
  ist nicht gezeigt; das Spin-Eis-Photon der Literatur gilt als schwach gekoppelt (Spinon alpha <= 0,2 [P:
  DYON-STATISTIK-L, dort S]).
- **Vorschlag:** "(Finns Fall)" ersetzen durch "(moeglicherweise Finns Fall [H])".

**C5 (v5 Z. 27): "Masse gibt es mit Inversion" ist unvollstaendig.**
- QCA-DIRAC-T-1, Bedeutung: "Eine saubere Dirac-Masse braucht zusaetzlich eine Inversion (Paritaet) oder eine
  abgestimmte Muenze" (die Quellform Eq. 36).
- **Vorschlag:** "Masse gibt es mit Inversion oder mit der abgestimmten Quellform (QCA-DIRAC-T-1)".

**C6 (UEBERLEITUNGEN-EMERGENZ.md Ue1, "P1 und P2 waeren damit von selbst erfuellt [H]"):** richtig als [H] markiert;
fuer das Weltmodell-Dokument mit dem Zusatz "klassisch" uebernehmen, sonst widerspricht es B5.

**C7 (RAUMZEIT-NETZ.md Z. 47-48): "Das loest AETHER-UHR-1 auf" folgt aus einem [H] und gilt nur klassisch.**
- **Vorschlag:** "Das wuerde AETHER-UHR-1 klassisch aufloesen [H]; quantenmechanisch gilt der Einwand von Collins u. a."

**C8 (UEBERLEITUNGEN-EMERGENZ.md Z. 116): "zittert um 1/4 in der Rapiditaet je Schritt".**
- 1/4 ist die Varianz, die Streuung ist 1/2 (KAUSAL-SWERVE-1, Ergebnis 2: sigma^2 = 0,246 bis 0,252). v5 sagt es
  richtig ("Varianz 1/4 je Schritt (etwa 1/2 Rapiditaet)").
- **Vorschlag:** "zittert je Schritt mit der Varianz 1/4 (Streuung 1/2) in der Rapiditaet".

**C9 (v5 Z. 23): "fuer lange Wellen in allen Richtungen gleich schnell"** stimmt fuer k gegen 0 (omega^2/k^2 =
0,25 in 23 Richtungen auf 3e-5). Die zwei Zweige einer Kopie spalten aber linear in abs(k) auf (bis 5,8e-5 bei
abs(k) = 1e-3; TENSOR-EIS-PYRO-1 Abschn. 4.2): eine Doppelbrechung erster Ordnung. **Vorschlag:** anfuegen "(die zwei
Zweige spalten linear in abs(k) auf, bis 5,8e-5 bei abs(k) = 0,001)".

**Rueckwaerts gelesen (vom Urteil der Quellen zu den Saetzen von v5):** Die Zahlen in v5 stimmen mit den Primaerdateien
ueberein, soweit ich sie geprueft habe: beta_S = -1,6515 +- 0,0524 (t = -31,5), beta_Q = -1,6126 +- 0,0524,
Spanne C, S, Q = 0,196, Torus 1,242 +- 0,504 und 5,715 SE (jq, KUGEL-1/-2); 1,075 +- 0,071 und 0,92 +- 0,12 (ERGEBNIS
-GROB Z. 29, -DIRAC-2D Z. 23); 1,7 +- 1,1, 7,4 +- 2,1, 5,9 +- 1,75 (DIRAC-2D Z. 25 und 97); Wilson -1,00 +- 0,55,
-0,26 +- 0,56, 0,72 +- 0,04 (jq); 3 bis 9 % nicht einbettbar (8,6 % bis 3,1 %); Sprungregeln 10-fach und 30-fach
(0,152 / 0,0147 = 10,3; 0,0147 / 4,36e-4 = 33,7). Die Fehler von v5 sind also keine Zahlenfehler, sondern
Urteilswoerter und fehlende Einschraenkungen (A1, A2, B1 bis B5, B7). Ein Teil davon ging beim Uebertragen aus den
Ernten verloren (B2: "stimmt trotzdem nicht" steht in RUNDE-40.md Z. 325, nicht in v5).

## Rueckwaertsdurchgang

Ueber meinen eigenen Text, jede Zahl und jede starke Aussage gegen die Quelle (begonnen 14:05:48, Stand dieses
Absatzes 14:13:35, beides per date).

**Zahlen nachgeprueft (Quelle in Klammern):** beta_S, beta_Q, Spanne 0,196, 5,715 SE (jq KUGEL-1/-2); xi* 0,5552 +-
0,0177, Steigung 2,9047, beta0 -1,6126 (jq XI-KUGEL-1); c_eff(W1) -0,995 +- 0,552, W05 -0,259 (jq WILSON-2D); TS-Urteile
(jq TWIST-SPIN-1); 1,075, 0,92, 1,7, 7,4, 5,9 (ERGEBNIS-Zeilen wie in C-Abschnitt); 0,82/0,80 % (QBALL-PYRO-1);
omega^2/k^2 = 0,25, 98 %, Defekt 1,0, 5,8e-5 (TENSOR-EIS-PYRO-1); 0,463 und 685 bei eps = 0,2 (SPIN-ZUFALLSNETZ-1);
V-J/V-0/V-00 (KAUSAL-4D-SCHICHT-2); Gamma/N 1,212 bis 1,315 (KUGEL-1 Abschn. 3.2); LHAASO, GW170817, Collins, BHS,
Ahmed u. a., Bose u. a. (lokale Kopien, selbst gelesen); LORENTZ.md Z. 45, 56-59, 217 und WARUM-SPIN-2.md Z. 775-782
(Projektdateien, Marke [P]). Kopfrechnungen: 61,56 = 32 pi^2 sqrt(3/(8 pi^2)); 0,111 x 11,19 = 1,242; 2,893/0,5066 = 5,71;
1,995/0,552 = 3,6; 1,259/0,56 = 2,2; 0,152/0,0147 = 10,3; 0,0147/4,36e-4 = 33,7; 6/0,1949 = 30,8; 1,6126/2,9047 =
0,5552; 2,9047/6 = 0,484; zweite Variation (6 l(l+3) - 24)/a^2.

**Im Rueckwaertsdurchgang berichtigt (eigene Fehler):**
1. "drei unabhaengige Zahlen um 1" in 2D: 0,89 +- 0,14 liegt auf Saaten von DIRAC-2D; jetzt "zwei unabhaengige".
2. "gleiches Fallen" hatte ich der Regge-Buehne zugeschrieben; gezeigt ist es nur auf einem kubischen Raum-Netz mit
   eingebauter Regel (REGEL-1). Abschnitt 1, 3 und 4 berichtigt.
3. "Licht klassisch" fuer Finns Netz: FLUSS-1 ist statisch (Monte Carlo), ohne Wellen. Ueberall auf "statisches
   Coulomb-Gesetz" geaendert; daraus B7.
4. "Entstanden sind nur drei Dinge" war zu absolut; jetzt "vor allem" mit Liste.
5. "kein lorentzsches Gegenstueck" war ohne Beleg; jetzt die genaue Aussage von Bombelli/Henson/Sorkin.
6. "98 % der Moden" stimmte nicht; richtig ist "an 98 % der Gitterpunkte im k-Raum eine Mode".
7. "Isometrie-Bahn" fuer die l = 1-Verformung war falsch; es ist eine konforme Umbenennung (Moebius), keine Isometrie.
8. "Gamma/N 1,21 bis 1,31": richtig bis 1,32 (Torus 1,315).
9. "Codex-Weg" fuer C x S^2 stand in keiner von mir gelesenen Datei; Zuschreibung entfernt.
10. "Die heute haeufig genannte Mischung" war unbelegt; jetzt "die Mischung aus der KARTE".
11. "685 Kegel-Einheiten" ohne Fenster; jetzt "im Fenster eps = 0,2".
12. Die 70-%-Lesart von XI-KUGEL-1 ist die des Agenten; jetzt so markiert.
13. Schritt 2 verlangte zugleich "dieselben Punkte und dieselbe Triangulierung" und "Dichte 1 bezueglich der neuen
    Metrik"; das widerspricht sich bei konformer Verformung. Jetzt: dieselben Zufallspunkte, mit fester Abbildung
    verschoben; Umgang mit der Triangulierung vorab festlegen.
14. Der eigene Gegentest von K-B (Zittern durch Koernigkeit) fehlte in der Tabelle "Aeussere Passung"; als Zeile
    ergaenzt.
15. B2 ergaenzt um die Einschraenkung der Ernte (mit k^6-Glied unentschieden), damit der Vorschlag nicht seinerseits zu
    stark ist.

**Starke eigene Aussagen und ihre Grundlage:**
- "Keine Buehne traegt mehr als einen Kernbaustein in gezeigter Form" [ES]: haengt an meinem Massstab "gezeigt"
  (eingesetzte Regge-Schwerkraft zaehlt als gezeigt, statisches Coulomb-Gesetz nicht als Licht). Mit milderem Massstab
  traegt Finns Netz drei Bausteine teilweise; das steht daneben.
- "K-B ist der einzige ohne strukturelle Verletzung" [ES aus S]: gestuetzt auf Bombelli/Henson/Sorkin (Abstract) und
  darauf, dass nichts Gegenteiliges gerechnet ist; ausdruecklich "weil fast alles ungetestet".
- "K-A nur mit Feinabstimmung" [ES aus S]: Collins u. a. (Abstract), GW170817 (Gl. 13), Levin/Wen stimmen t ab [P].
  Eine Schutzsymmetrie auf Finns Netz habe ich nicht gesucht; "keine bekannt" heisst: in den Projektdateien und meinem
  Wissen keine.

**Nicht an der Primaerquelle geprueft:** Collins u. a., Bombelli/Henson/Sorkin, Ahmed u. a., Bose u. a. nur im Abstract;
alle [P]-Werte (MICROSCOPE, Cassini, LLR, Lorentz-Schranken) nur in den Projektdateien; Nielsen/Ninomiya,
Spin-Statistik-Satz, kosmologische Konstante 1e-122, CDT 4D und Swerve-Schranken aus dem Gedaechtnis [L].

## Einfach gesagt

Das Projekt hat viele Bauteile fuer eine Welt gebaut: eine elektrische Anziehung aus Pfeilen auf einem Netz (Lichtwellen
noch nicht), Schwerkraftwellen, Teilchen, die sich beim Vertauschen wie Elektronen verhalten, und ein Netz aus
zufaelligen Punkten, dessen Zittern Schwerkraft erzeugen koennte. Diese Bauteile stehen aber auf verschiedenen Buehnen, die nicht zusammenpassen, so als haette man
Motor, Raeder und Lenkrad fuer drei verschiedene Autos gebaut. Finns Tetraeder-Netz traegt die meisten Teile, hat aber
eine Lieblingsrichtung im Raum; dann laufen Licht und Schwerkraft nicht von selbst gleich schnell, obwohl Messungen
zeigen, dass sie bis auf ein Billiardstel gleich schnell sind. Ein Netz aus zufaellig verstreuten Ereignissen hat
dieses Problem nicht, aber darauf ist erst wenig gebaut, und schwere Teilchen laufen dort bisher nicht stabil. Die
Schwerkraft aus dem Zittern der Materie hat auf einer vierdimensionalen Kugel zwar das richtige Vorzeichen, doch das
liegt zu rund 70 Prozent an Eigenheiten des Netzes, und auf einem anderen Netz kam das falsche Vorzeichen heraus. Was
in keinem Bild vorkommt, sind die Teilchen unserer Welt mit ihren Eigenschaften, etwa dass die schwache Kraft links-
und rechtsdrehende Teilchen verschieden behandelt. Als Naechstes sollte Finn entscheiden, ob er ein festes Netz mit fein
abgestimmten Tempi will, und eine Rechnung sollte pruefen, ob die Schwerkraft aus dem Zufallsnetz wirklich Einsteins
Form hat.

## Protokoll

- 13:38:41 Beginn, KARTE gelesen.
- 13:53:29 bis 13:53:34 Literaturabrufe: zwei HTTP-Anfragen an export.arxiv.org (die erste ohne Weiterleitung leer),
  drei Abstracts (gr-qc/0605006, astro-ph/0209274, 1707.06050) in quellen/api-abstracts-1.xml (sha256 bc6efefe...).
  Gezaehlt als 3 von 8 Abrufen. Alle uebrigen Quellen sind lokale Kopien anderer Karten.
- 13:54:44 (date beim Lesen) Nachricht der Leitung: TWIST-SPIN-1 fertig. ERGEBNIS.md selbst gelesen, Urteile per jq an
  lauf-69/auswertung.json geprueft; eingearbeitet in Abschnitt 1, 2 und 3.
- 14:03:26 Nachricht der Leitung: INDUZIERT-XI-KUGEL-1 fertig. (Zeit der Lesung per date; die Nachricht selbst traf
  kurz davor ein.) ERGEBNIS Abschn. 1 gelesen, xi*, Steigung und beta0 per jq
  geprueft; eingearbeitet in Abschnitt 1, 2, 4, 5 und A2. Meine Ableitbarkeitsprobe in Abschnitt 5 (Schritt 5 der
  ersten Fassung) stand vor dieser Nachricht im Text.
- 14:05:48 bis 14:16:33 Rueckwaertsdurchgang (15 eigene Berichtigungen, Liste oben), dazu Nachpruefung Torus
  (INDUZIERT-DICHTE-4D Z. 33-34), CDT (CDT-HORAVA-L Z. 24), FLUSS-1 (statisch), Ernte WILSON-2D (RUNDE-40.md Z. 313-335).
- 14:16:33 Ende (date). Dauer 37 min 52 s von 120 min. Literaturabrufe 3 von 8. Keine Laeufe, kein python/awk/perl,
  geschrieben nur in RUNDE-37/weltmodell-review-1/ (REVIEW.md, quellen/api-abstracts-1.xml). Nichts Versiegeltes
  geoeffnet; Selbstanzeige zur Gedaechtnisnotiz siehe Abschnitt 1, Punkt 5.
