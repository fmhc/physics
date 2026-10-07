Urteil: einfuegen nach genannten Aenderungen (11 Auflagen A, 3 redaktionelle Auflagen R, 4 Empfehlungen E; Abschnitt 5)

# Lesung der letzten Schicht: NACHTRAG-ENTWURF.md (spin2-d4)

- Leser: pruefer-opus (Haus Anthropic), frischer Leser
- Auftrag: Leitung claude-primary, Auftrag direkt in der Nachricht (keine BRIEF-Datei genannt)
- Beginn (date): 2026-10-01 21:07:28 CEST
- Zeitbox: 25 min
- Gelesen: NACHTRAG-ENTWURF.md ganz (39 Zeilen, mtime 21:07); codex-lesung/LESUNG.md ganz; Quellstellen per grep/sed:
  CEMZ 1407.5597v1.txt (S. 6, 24-27, 43, 49, 65-67), CHLPSD quellen/2201.06602.txt (S. 2, 6, 16-17, 25, 27, 34, 35),
  Bellazzini quellen/2512.13780v2.txt (S. 30-31, Lit. [2], [31], [39], [41]), Bucciotti RUNDE-11/.../2605.00089.txt (S. 21-22).
  Kontext nur gezielt: SPIN2-D4.md (Z. 26-27, 97, 109-110, 130, 182, 290-292, 543), WARUM-SPIN-2.md (Markenlegende Z. 7-10,
  Nachtrag 24.09. Z. 539), RUNDE-12/cemz-ebene/CEMZ-EBENE.md (Z. 1-30, 190-200), RUNDE-11/cemz-mess/quellen/1704.01590.txt (EGHS S. 13).
- Seitenzuordnung: gedruckte Seitenmarken im Text ("- 25 -" bzw. "25"), Seite N = Text zwischen Marke N-1 und Marke N.

## 1. Zahlen, Seiten, Gleichungen, Zitate gegen die Quelltexte

| Entwurf (Zeile) | Angabe | Befund an der Quelle |
|---|---|---|
| Z. 5 | Urteil der Lesung "traegt mit wesentlichen Auflagen als Literaturuebersicht" | stimmt (LESUNG Z. 3, in ASCII-Umschrift) |
| Z. 9-10 | CEMZ arXiv:1407.5597, Abschn. 3.5, S. 25-26, eigener D = 4-Abschnitt | stimmt ("3.5. Scattering of Gravitons in Four Dimensions", Inhaltsverz. S. 25, Abschnitt endet vor Marke 26) |
| Z. 11 | IR-Logarithmus mit Vergleichskriterium nach Gao-Wald | stimmt: "modifying the causality criterion in the form suggested by Gao and Wald, who define it by comparing to the behavior of the same metric far away" (S. 25) |
| Z. 11-12 | gerade und ungerade Dreipunktkorrektur "getrennt untersucht" | **stimmt nicht**: S. 26 "Let us now discuss the parity violating structure, together with the parity preserving one"; Gl. (3.20) enthaelt gamma und gamma* gemeinsam. Siehe B1 |
| Z. 13 | Fussnote 23, S. 49, Turm in D = 4 | stimmt: "the existence of an infinite tower of higher spin states is clear in D = 4" (Fn. 23, Seitenmarke 49) |
| Z. 14 | Zeitmaschine Anhang G nur D > 4 | Inhalt stimmt: "The conclusion is that in D > 4 we can construct closed time-like curve" (S. 67), Bedingung (G.2) mit Exponent D-4 (S. 66). Satzbau falsch herum, siehe B2 |
| Z. 15 | Caron-Huot, Li, Parra-Martinez, Simmons-Duffin 2022, arXiv:2201.06602, dispersiv | stimmt (Titelblatt v1, 17 Jan 2022; Abstract "dispersion relations"). "ohne Zeitmaschine" steht nicht in CHLPSD (grep "time machine": 0 Treffer), gedeckt nur allgemein durch Bucciotti S. 22 (S-Matrix-Weg braucht keinen CTC-Nachweis), siehe B12 |
| Z. 16 | Gl. (2.11), S. 6, gerade oder ungerade | stimmt: (2.11) "g^3 = alpha3 + i alpha~3", S. 6 oben "real and imaginary part representing parity-even and parity-odd couplings" |
| Z. 17 | S. 35; Gl. (4.4) und Abb. 8 auf S. 27; Spin 4 | Seiten stimmen ((4.4) und Bildunterschrift Fig. 8 "spin-4 mass gap M" vor Marke 27; Schluss S. 35 "a spin-4 particle must exist"). "bei etwa dieser Skala" stimmt nicht mit der Ungleichung, siehe B3 |
| Z. 18 | Zweiteilchenzustand S. 25, 34 | Seiten stimmen (S. 25: "the lightest higher-spin states, which are two-particle states, is M = 2m"; S. 34: "two-particle states of some light fields that couple to us only through gravity"). Schluss "nicht zwingend ein neues Elementarteilchen" ueberzieht, siehe B4 |
| Z. 19 | IR-Schnitt, S. 16-17 | Seiten stimmen (S. 16: "regulate by adding an infrared cutoff mIR << M, and accept that this causes negativity at large impact parameters"; S. 17: "only become negative at some large b"). Kern fehlt, siehe B5 |
| Z. 20 | Turm nur referiert, S. 25 | stimmt: "Ref. [7] further argued that an infinite tower of higher-spin states needed to appear" ([7] = CEMZ); "tower" kommt im ganzen Text nur dort vor |
| Z. 20 | SM-Kopplung offen, S. 2 | stimmt: "The task of bounding their couplings to Standard Model fields is left to future work." |
| Z. 22 | Bellazzini arXiv:2512.13780v2, S. 30, Zitat | **woertlich richtig**: "Introducing hard IR cutoffs by hand [31,39,41] does not resolve the issue" (Auslassung ersetzt nur die Klammer [31,39,41]); Seite 30 stimmt |
| Z. 23 | [39] ist Caron-Huot u. a. | stimmt ([39] S. Caron-Huot, Y.-Z. Li, J. Parra-Martinez, D. Simmons-Duffin). Die Kritik gilt [31,39,41]; CEMZ ist dort [2] und nicht darunter, siehe B6 |
| Z. 24 | IR-endlicher Weg, endliche Detektoraufloesung, S. 31 | stimmt ("working with the IR-finite M_E ... acquires a physical meaning in terms of detector resolution ... should not be taken to zero") |
| Z. 26 | Bucciotti u. a. 2026, arXiv:2605.00089, S. 21-22, "derselbe IR-Effekt" | Fundstelle stimmt (S. 21 "this second approach encounters the same infrared logarithm"; S. 21-22 "This logarithm in D = 4 is the scattering-amplitude manifestation of the same IR effect we identify geometrically"). Vergleichsglied fehlt, siehe B7 |
| Z. 27 | Satz nur fuer stationaere, asymptotisch Schwarzschild-artige Hintergruende | stimmt fuer Theorem 3.1 (S. 21: "for any stationary asymptotically-Schwarzschild spacetime ... (Theorem 3.1)"); "Satz" doppeldeutig, siehe B7 |
| Z. 35 | CEMZ-EBENE, Runde 12, 1 bis 35 km | stimmt mit CEMZ-EBENE.md Kurzfazit Nr. 1 ("Fuer alle l_eff in [1, 35] km"); nicht durch Quelle/Lesung gedeckt, aber durch Projektdatei; Pfad fehlt (B12) |

Gesamtbild Teil 1: Alle Seiten- und Gleichungsangaben stimmen, das einzige woertliche Zitat stimmt. Falsch ist eine
Inhaltsangabe (Z. 11-12 "getrennt"); dazu kommen Reichweitenfehler (B3, B4, B8) und ein umgedrehter Satzbau (B2).

## 2. Anforderungen aus LESUNG.md (Abschnitte 2 bis 5) gegen den Entwurf

| LESUNG | Anforderung | Entwurf | Stand |
|---|---|---|---|
| Kopf | "Regime B im Ergebnis" und "nur eine Erwartung" nicht uebernehmen | beides fehlt im Entwurf | umgesetzt |
| 2 | CHLPSD D = 4-Hoeherspinschluss S. 35, (4.4) | Z. 16-17 | umgesetzt, aber Ungleichung zu "etwa" verwischt (B3) |
| 2 | IR-Schnitt von Hand, zugelassene Negativitaet, S. 16-17, "zentrale Einschraenkung" | Z. 19 nennt Schnitt, nicht die Negativitaet | teilweise (B5) |
| 2 | Abb. 8 / (4.4) auf S. 27, (2.11) S. 6 | Z. 16-17 | umgesetzt |
| 2 | Schranke implizit (M auch im Logarithmus) | nicht erwaehnt; "bei etwa dieser Skala" ueberdeckt es | teilweise (B3) |
| 2 | "neuer elementarer Spin-4-Koerper" zu stark; Zweiteilchenzustaende S. 25, 34 | Z. 18 | umgesetzt, aber ueberzogen ins Gegenteil (B4) |
| 2 | Turm in CHLPSD nur referiert, S. 25 | Z. 20 | umgesetzt |
| 2 | SM-Kopplung offen S. 2, kein alpha ~ 1, CEMZ-EBENE folgt nicht allein | Z. 20, 35-36 | umgesetzt; "keiner der gelesenen Quellen" kollidiert mit EGHS (B8) |
| 2 | Bellazzini S. 30, [39]; kein Nachweis, dass jedes D = 4-Verfahren scheitert | Z. 22-23, 31 | umgesetzt; Zuordnung der Kritik unklar (B6) |
| 2 | M_E liefert keine fertige Graviton-Riemann^3-Schranke ("nicht gezeigt", Beispiele Pionen) | Z. 25 "noch nicht durchgerechnet" | ueberzogen zur Literaturaussage (B9) |
| 2 | Bucciotti: S. 21-22; Satz beschraenkt auf stationaer/asymptotisch Schwarzschild; S. 21 lokale Hyperbolizitaetsschranke; keine allgemeine D = 4-Schrankenfreiheit | Z. 26-27 | teilweise: Inhalt des Satzes und lokale Schranke fehlen (B7) |
| 2 | Haering/Zhiboedov, Chang/Parra-Martinez, Beadle, Fn. 14, G_E-Einheiten | nicht verwendet | kein Verstoss (nichts einseitig zitiert) |
| 3 | CEMZ selbst: Paragraph 3.5 S. 25-26, Fn. 23 S. 49; D > 4-Beschraenkung des Anhangs widerlegt das D = 4-Argument nicht | Z. 10-14 | umgesetzt, aber Z. 14 sagt grammatisch das Umgekehrte (B2); "getrennt" falsch (B1) |
| 3 | fairer Streitpunkt: ob das Vergleichs-/IR-Kriterium (Gao-Wald) gerechtfertigt und mit der gewuenschten Observable identisch ist | nicht genannt; "Umstritten ist die IR-Behandlung" belegt nur Kritik am harten Schnitt | fehlt (B6) |
| 3 | Bellazzini konstruktive Seite "ebenso deutlich": S. 31 Pol nicht fuer sich allein Hindernis, eigener IR-endlicher UV/IR-Zusammenhang | Z. 24 nur Detektorweg | teilweise (B13, Empfehlung) |
| 4 | getrennte Aussagen 1-4; Nr. 2: Turmargument "unter spezifischem Kausalitaets-/UV-Rahmen" | Z. 8, 29-30 nennen nur "Kausalitaets- bzw. IR-Annahmen" | UV-Rahmen fehlt (B10) |
| 4 | Nr. 3: regulatorunabhaengige Uebertragung nicht geschlossen | Z. 31-32 | umgesetzt |
| 4 | Nr. 4: massive Spektren nicht das masselose Glied 7; Dreipunktkorrektur nicht jede Abweichung | Z. 33-34 | umgesetzt; aber Z. 29 spricht ohne "massive Fassung" von Glied 7 (B11) |
| 4 | K1 "im Ergebnis getroffen" entfaellt oder "Vorabklassen unzureichend; differenzierter Ausgang" | Entwurf nennt keine Vorabklassen, spricht aber in Z. 37 von "beide Lesarten" | siehe B14 |
| 5 | Nicht uebernehmen: "im Labor- und Kosmosbereich sind A und B gleich"/"physikalisch ununterscheidbar"; Kopfrechnungen 30 km, Faktoren 2,4-2,8, exp(-3e78) | Z. 37-38: nur "im Labor", nur "Kopfrechnungen zur noetigen Detektoraufloesung" | teilweise (B14): die Faktoren 2,4-2,8 sind laut SPIN2-D4.md Z. 97/290-292 die (log)^(1/8)-Faktoren der CHLPSD-Schranke, keine Detektoraufloesung |
| 5 | Kernsatz-Vorschlag (konkrete Argumente unter expliziten Annahmen; Umsetzung umstritten; Reparaturarbeiten schliessen Kette nicht; keine bedingungslose Kopplung, keine allgemeine Unmoeglichkeit) | Z. 8, 21, 31-32 | umgesetzt; Z. 31 laesst offen, Unmoeglichkeit wovon (B15) |

Staerker als die Lesung erlaubt: Z. 18 (B4), Z. 25 (B9), Z. 36 durch Weglassen von EGHS (B8).
Schwaecher oder fehlend: Z. 19 Negativitaet (B5), UV-Rahmen (B10), Streitpunkt des CEMZ-Kriteriums (B6), Inhalt des Bucciotti-Satzes (B7).

## 3. Absolute Woerter gegen die Quellen

| Zeile | Wort/Aussage | Gegenprobe | Ergebnis |
|---|---|---|---|
| 14 | "gilt **nur** fuer D > 4" | CEMZ S. 66-67: Schluss nur fuer D > 4 formuliert; (G.2) "(r_S/b)^(D-4) >> 1" ist in D = 4 nicht erfuellbar | haelt |
| 17 | "**muss** es ... geben" | CHLPSD S. 35 knuepft das Muss an zwei Bedingungen: "if a higher-derivative correction were measured" **und** "if Nature respects causality as we understand it"; S. 35 Kopf: "assuming that causality and other basic principles apply at all energies" | haelt nur mit der zweiten Bedingung; im Satz fehlt sie (B10) |
| 18 | "**nicht zwingend** ein neues Elementarteilchen" | S. 25: Zweiteilchenzustaende aus "massive particles of mass m and spin two or less"; S. 34: "two-particle states of some light fields that couple to us only through gravity", dazu Einschraenkung "long-distance effects are negligible unless there are a very large number of such light fields" | haelt nicht in dieser Breite (B4) |
| 20 | "referieren sie **nur**" | grep "tower" im ganzen CHLPSD-Text: einziger Treffer S. 25 | haelt |
| 25 | "**noch nicht** durchgerechnet" | Bellazzini: Beispiele pi+pi+ mit Photon/Graviton (Textzeile 1714); fuer die Literatur insgesamt keine Suche; LESUNG Abschn. 6: kein Satz "es existiert keine weitere Arbeit" | haelt nur fuer die gelesene Arbeit (B9) |
| 27 | "gilt **nur** fuer stationaere ..." | Bucciotti S. 21, Theorem 3.1 "for any stationary asymptotically-Schwarzschild spacetime" | haelt als Geltungsbereich des Theorems |
| 31 | "**Weder** ... **noch** ... belegt" | LESUNG Kopf und Abschn. 5 | haelt; Bezugswort fehlt (B15) |
| 33 | "**nicht unmittelbar**", "**nicht jede** Abweichung" | LESUNG Abschn. 4 Nr. 4 | haelt |
| 36 | "in **keiner** der gelesenen Quellen hergeleitet" | EGHS 1704.01590 S. 13: "these new particles would mediate a new force between all Standard Model particles ... the strength will be parametrically equal to gravitational"; CEMZ-EBENE.md Kurzfazit Nr. 4 stuetzt alpha ~ 1 genau darauf [A]; WARUM-SPIN-2.md Z. 539 (Nachtrag 24.09.) ebenso | haelt nur, wenn "gelesene Quellen" auf die vier Nachtragsquellen begrenzt und EGHS ausdruecklich eingeordnet wird (B8) |

## 4. Ungedeckte Aussagen (weder Quelle noch Lesung)

1. Z. 11-12 "getrennt untersucht": widerspricht CEMZ S. 26 ("together with") - B1.
2. Z. 18 "nicht zwingend ein neues Elementarteilchen": weder Quelle noch Lesung (LESUNG verneint nur den "neuen elementaren Spin-4-Koerper") - B4.
3. Z. 25 "noch nicht durchgerechnet" als Literaturaussage: ungedeckt - B9.
4. Z. 15 "ohne Zeitmaschine": in CHLPSD nicht ausgesprochen; sachlich gedeckt durch Bucciotti S. 22 ("The S-matrix approach has the practical advantage of not requiring a verification that closed timelike curves can be constructed"), aber dort nicht zitiert - B12.
5. Z. 35 "Runde 12, Fuenfte Kraft bei 1 bis 35 km": nicht aus Quelle/Lesung, aber durch CEMZ-EBENE.md Kurzfazit Nr. 1 gedeckt; Pfad fehlt - B12.
6. Z. 8 "zwei konkrete Argumente": als zwei Methoden gedeckt; CHLPSD S. 25 sagt aber "CEMZ constraints are built into dispersive sum rules, they are a subset of the functionals" - Unabhaengigkeit ist nicht gedeckt - B16 (Empfehlung).
7. Z. 26 "nennen den Logarithmus denselben IR-Effekt": gedeckt, aber ohne Vergleichsglied missverstaendlich - B7.

## 5. Befundliste (Fundstelle, Problem, Beleg, Anforderung)

Kennzeichen: **A** = Auflage (vor dem Einfuegen zu erfuellen), **R** = redaktionelle Auflage, **E** = Empfehlung.
Ich formuliere keinen Ersatztext; die Anforderung beschreibt nur, was der Satz leisten muss.

**B1 (A) - Z. 11-12, "getrennt untersucht".**
Problem: Inhaltsangabe widerspricht der Quelle. Beleg: CEMZ S. 26 "Let us now discuss the parity violating structure,
together with the parity preserving one"; Gl. (3.20)-(3.22) behandeln gamma (+++) und gamma* (---) in einer Matrix.
Anforderung: kein "getrennt"; die Angabe muss mit "together with" vereinbar sein. LESUNG Abschn. 3 sagt nur
"analysieren die paritaetsgerade/-ungerade Dreipunktkorrektur".

**B2 (A) - Z. 14, "Das D = 4-Argument widerlegt sie damit nicht."**
Problem: Bei ueblicher Lesart (Subjekt zuerst) sagt der Satz, das D = 4-Argument widerlege die Zeitmaschinen-Konstruktion
nicht. Gemeint ist laut LESUNG Abschn. 3 das Umgekehrte: "die D>4-Beschraenkung der speziellen CTC-Konstruktion im Anhang
[widerlegt] nicht das gesamte D=4-Argument". "Das D = 4-Argument" und "sie" sind beide im Nominativ und im Akkusativ formgleich.
Anforderung: Subjekt und Objekt eindeutig machen: Die D > 4-Beschraenkung der Konstruktion in Anhang G widerlegt das
D = 4-Argument (Abschn. 3.5, Fn. 23) nicht. Optional die Fundstelle S. 66-67 nennen.

**B3 (A) - Z. 17, "muss es bei etwa dieser Skala Hoeherspin-Spektralgewicht ... geben".**
Problem: (a) "dieser Skala" hat im Entwurf kein Bezugswort. (b) Die Quelle gibt eine Ungleichung, keine Groessenordnung
"etwa": S. 35 "a spin-4 particle must exist whose Compton wavelength is at least as long as the length r0: M^-1 > r0" und
"new higher-spin states must exist with mass M <~ r0^-1 or lighter"; S. 17 "a heavy state at the mass M or lighter".
(c) (4.4) enthaelt log(M/mIR); Abstract: "up to an infrared logarithm"; LESUNG Abschn. 2: "Die Schranke bleibt implizit".
Anforderung: Die Skala benennen (Laenge r0 aus dem Riem^3-Koeffizienten). Die Aussage als obere Schranke der Masse
wiedergeben ("hoechstens ... oder leichter"), nicht als "etwa". Den IR-Logarithmus als Vorbehalt nennen.

**B4 (A) - Z. 18, "nicht zwingend ein neues Elementarteilchen".**
Problem: Das ist staerker als Quelle und Lesung. Die LESUNG verneint nur "Ein neuer elementarer Spin-4-Koerper muss
entstehen". In beiden Quellbeispielen braucht es weitere Felder. S. 25: "a loop of massive particles of mass m and spin two
or less", M = 2m. S. 34: "two-particle states of some light fields that couple to us only through gravity"; dort folgt
sofort die Einschraenkung "long-distance effects are negligible unless there are a very large number of such light fields".
Der Satz steht zudem unter der Marke [A] aus Z. 8 und waere damit als quellengeprueft ausgewiesen.
Anforderung: Nur verneinen, dass ein elementares Hoeherspin-(Spin-4-)Teilchen zwingend ist. Erkennbar machen, dass der
Zweiteilchenzustand aus anderen (massiven, Spin <= 2, bzw. leichten, nur gravitativ koppelnden) Feldern besteht. Die
S. 34-Einschraenkung nicht weglassen, wenn S. 34 als Beleg dient.

**B5 (R) - Z. 19, "IR-Schnitt bei grossen Stossparametern".**
Problem: Der Satz vermischt Schnitt und Folge und laesst den Kern weg. Der Schnitt ist m_IR << M als untere Impulsgrenze der
Funktionale. Die Folge ist in Kauf genommene Negativitaet bei grossen b. Beleg: S. 16 "regulate by adding an infrared
cutoff mIR << M, and accept that this causes negativity at large impact parameters"; S. 17 "only become negative at some
large b". LESUNG Abschn. 2: "Das ist eine zentrale Einschraenkung". Genau dies greift Bellazzinis Zitat in Z. 22 an.
Anforderung: Nennen, dass die Positivitaet bei grossen Stossparametern aufgegeben wird (Negativitaet zugelassen) und dass der
Schnitt von Hand gesetzt ist, damit der Leser den Bezug zu Z. 22 sieht.

**B6 (A) - Z. 21-23, "Umstritten ist die IR-Behandlung" (ohne Zuordnung).**
Problem: Z. 8-20 stellen zwei Argumente vor. Der Beleg in Z. 22 trifft aber nur eines davon. Bellazzinis Satz richtet sich
gegen [31,39,41]. CHLPSD ist [39]; CEMZ ist bei Bellazzini [2] und steht nicht in dieser Liste. Fuer das CEMZ-Kriterium nennt
die LESUNG (Abschn. 3) einen eigenen Streitpunkt: "ob das konkrete Vergleichs-/IR-Kriterium gerechtfertigt und mit der
gewuenschten Observable identisch ist". Dieser fehlt im Entwurf. Ohne Zuordnung liest man Bellazzinis Kritik als Kritik an
CEMZ.
Anforderung: Fuer jedes der zwei Argumente sagen, welcher Einwand es trifft. Den CEMZ-Streitpunkt nach LESUNG Abschn. 3
aufnehmen. Wird Bucciotti als Einwand gegen das asymptotische (Gao-Wald-)Kriterium gefuehrt, dann nur mit dessen
Geltungsbereich (Theorem 3.1: stationaere, asymptotisch Schwarzschild-artige Raumzeiten; CEMZ arbeitet mit Stosswellen).
Kein Schluss auf andere Hintergruende.

**B7 (A) - Z. 26-27, Bucciotti.**
Problem: (a) "denselben IR-Effekt" ohne Vergleichsglied. Die Quelle setzt den D = 4-Logarithmus des S-Matrix-/dispersiven
Wegs (aus der Gravitonschleife, braucht IR-Regulator) gleich mit dem geometrisch gefundenen Effekt, der logarithmisch
divergierenden Laufzeitdifferenz (S. 21-22). (b) "Ihr Satz" ist doppeldeutig: Theorem oder die eben zitierte Aussage? Wird
"Satz" als Aussage gelesen, beschraenkt Z. 27 faelschlich die Gleichsetzung auf stationaere Hintergruende. Der Inhalt des
Theorems fehlt. (c) LESUNG Abschn. 2: S. 21 enthaelt eine lokale Hyperbolizitaetsschranke, die in D = 4 ueberlebt
("A distinct, local form of causality constraint does, however, survive in D = 4"). Die Lesung verlangt, keine allgemeine
D = 4-Schrankenfreiheit abzuleiten.
Anforderung: Beide Seiten der Gleichsetzung nennen. "Satz" als Theorem 3.1 kennzeichnen und seinen Inhalt in einem Glied
angeben (asymptotische Kausalstruktur in D = 4 universell die von Schwarzschild, S. 21). Die ueberlebende lokale Schranke
erwaehnen oder die Lesart "keine Schranke in D = 4" sonst sicher ausschliessen.

**B8 (A) - Z. 36, "in keiner der gelesenen Quellen hergeleitet".**
Problem: EGHS (arXiv:1704.01590) S. 13: "these new particles would mediate a new force between all Standard Model particles,
basically through the same set of diagrams ... the strength will be parametrically equal to gravitational". Darauf stuetzen
sich CEMZ-EBENE.md (Kurzfazit Nr. 4, [A]) und der Nachtrag vom 24.09. in WARUM-SPIN-2.md (Z. 539: "vermittelt ein solcher
Turm eine Yukawa-Kraft gravitativer Staerke"). Ein Satz "keiner der gelesenen Quellen" ohne EGHS widerspricht im selben
Dokument stillschweigend dem frueheren Nachtrag. Haltbar ist nur: Es ist ein Kurzargument "within the set of assumptions
about the UV completion made in [13]", keine Herleitung (EGHS S. 13).
Anforderung: Den Kreis der "gelesenen Quellen" benennen. EGHS S. 13 ausdruecklich einordnen (Behauptung mit Kurzargument
unter CEMZ-UV-Annahmen, keine Herleitung) statt sie wegzulassen. Optional CHLPSD S. 2 anfuehren: "static long-range forces
... (also sometimes called fifth forces), are unconstrained by our arguments".

**B9 (A) - Z. 25, "Fuer die kubische Graviton-Korrektur ist er noch nicht durchgerechnet."**
Problem: Der Satz liest sich als Aussage ueber die gesamte Literatur. Gedeckt ist nur "in dieser Arbeit nicht gezeigt"
(LESUNG Abschn. 2: "Nicht gezeigt. Die expliziten Beispiele betreffen Pionen mit EM/Gravitation"). LESUNG Abschn. 6:
"Kein Satz 'bis Oktober 2026 existiert keine weitere Arbeit' folgt daraus." Z. 31-32 des Entwurfs begrenzt richtig ("Die
gelesenen ... Reparaturarbeiten"), Z. 25 nicht.
Anforderung: Auf die gelesene Arbeit bzw. die gelesenen Arbeiten begrenzen, wie in Z. 31-32.

**B10 (A) - Z. 8, 17, 29-30: Annahmen nicht vollstaendig "ausdruecklich genannt".**
Problem: Z. 8 verspricht "ausdruecklich genannte Annahmen". Z. 29-30 nennt nur "Kausalitaets- bzw. IR-Annahmen". Die LESUNG
(Abschn. 4 Nr. 2) spricht vom Turmargument "unter spezifischem Kausalitaets-/UV-Rahmen". Im Entwurf fehlen:
CEMZ S. 26: "We will discuss the case of a weakly coupled theory where the problem should be fixed at tree level";
CHLPSD S. 35: "assuming that causality and other basic principles apply at all energies" und als Bedingung des Muss in Z. 17
"if Nature respects causality as we understand it". EGHS S. 13 bestaetigt die Bindung des Turms an die UV-Annahmen von CEMZ.
Anforderung: Die UV-Annahmen (schwache Kopplung bzw. Behebung auf Baumniveau bei CEMZ; Kausalitaet bei allen Energien bei
CHLPSD) unter die genannten Bedingungen aufnehmen. Das Muss in Z. 17 an seine Kausalitaetsbedingung binden.

**B11 (A) - Z. 29 gegen Z. 33, Glied 7 ohne "massive Fassung".**
Problem: In Z. 29 gilt "die Kopplung der Glieder 7 und 10" bedingt, in Z. 33 betreffen massive Spektren "das masselose
Glied 7 nicht unmittelbar". Zusammen wirkt das widerspruechlich. WARUM-SPIN-2.md fuehrt die Kopplung seit dem 24.09.
ausdruecklich als "Glied 7, massive Fassung, und Glied 10" (Z. 539); Glied 7 selbst heisst "Nicht Spin 3 oder hoeher" (Z. 248).
Anforderung: In Z. 29 dieselbe Bezeichnung wie im Nachtrag vom 24.09. verwenden (massive Fassung von Glied 7), damit Z. 29 und
Z. 33 vereinbar sind.

**B12 (E) - Z. 15 "ohne Zeitmaschine", Z. 35 "1 bis 35 km": Belege fehlen.**
Beleg: CHLPSD erwaehnt keine Zeitmaschine (grep: 0 Treffer). Allgemein gedeckt ist es durch Bucciotti S. 22 ("not
requiring a verification that closed timelike curves can be constructed"). "1 bis 35 km" steht in
RUNDE-12/cemz-ebene/CEMZ-EBENE.md, Kurzfazit Nr. 1.
Anforderung: Fuer beide Angaben eine Fundstelle nennen oder die Angabe streichen.

**B13 (E) - Z. 24, konstruktive Seite Bellazzinis nur halb.**
Beleg: Bellazzini S. 31: "Ref. [69] further showed that, when the limits are taken in the correct order, the 1/t pole is
not by itself the fundamental obstruction to positivity bounds in D = 4". LESUNG Abschn. 3 verlangt die konstruktive Seite
"ebenso deutlich" (dort an die Uebersicht gerichtet).
Anforderung: Pruefen, ob dieser Teil in den Nachtrag gehoert. Er stuetzt Z. 31 ("keine allgemeine Unmoeglichkeit").

**B14 (R) - Z. 37-38, "Nicht uebernommen".**
Problem: (a) LESUNG Abschn. 5 nennt "im Labor- und Kosmosbereich sind A und B gleich" bzw. "physikalisch ununterscheidbar";
der Entwurf nennt nur "im Labor". (b) "Kopfrechnungen zur noetigen Detektoraufloesung" deckt nur E ~ M exp(-3e78). Die Faktoren
2,4-2,8 sind die (log)^(1/8)-Faktoren der CHLPSD-Schranke mit Hubble-Regulator (SPIN2-D4.md Z. 97, 290-292), keine
Detektoraufloesung. 30 km ist deren Eingangsgroesse. (c) "beide Lesarten" ist im Nachtrag nicht eingefuehrt (gemeint:
Karte A/B). Nennt der Nachtrag die Vorabklassen, gilt LESUNG Abschn. 4: nicht "Regime B", sondern sinngemaess
"Vorabklassen unzureichend; differenzierter Ausgang".
Anforderung: Die ausgeschlossene Aussage vollstaendig wiedergeben. Alle [ES]-Kopfrechnungen des Berichts ausschliessen (30 km,
2,4-2,8, exp(-3e78)). "beide Lesarten" erklaeren oder durch einen Verweis ersetzen.

**B15 (R) - Z. 31, "allgemeine Unmoeglichkeit" ohne Bezugswort.**
Beleg: LESUNG Kopf: "weder einen voraussetzungslosen Turmzwang noch dessen allgemeine Unmoeglichkeit".
Anforderung: Nennen, was nicht als unmoeglich belegt ist (Turmzwang bzw. Kopplung).

**B16 (E) - Z. 8, "zwei konkrete Argumente".**
Beleg: CHLPSD S. 25: "CEMZ constraints are built into dispersive sum rules, they are a subset of the functionals enumerated
in the preceding subsection." Zwei Methoden, aber keine voneinander unabhaengigen Stuetzen.
Anforderung: Keine Unabhaengigkeit nahelegen.

**B17 (A) - Gesamter Abschnitt "Folge fuer die Kette": Bezug auf den Nachtrag vom 24.09. fehlt.**
Problem: WARUM-SPIN-2.md Z. 539 (Nachtrag 2026-09-24) sagt ohne Bedingung: "verlangt jede Korrektur der Drei-Graviton-
Kopplung ueber zwei Ableitungen hinaus ... einen unendlichen Turm massiver Hoeherspin-Zustaende bei der Korrekturskala".
Dazu: "Nach EGHS ... vermittelt ein solcher Turm eine Yukawa-Kraft gravitativer Staerke". Der neue Entwurf schraenkt beides ein
(bedingt; alpha ~ 1 nicht hergeleitet; Masse hoechstens auf der Skala). Den frueheren Nachtrag nennt er aber nicht. Bei
unveraenderlichen Nachtraegen findet ein Leser des 24.09.-Absatzes die Einschraenkung sonst nicht.
Anforderung: Den Nachtrag vom 24.09. nennen und angeben, welche seiner Aussagen jetzt nur bedingt gelten.

**B18 (E) - Z. 1, Zeitstempel.**
Beleg: Fruehere Nachtraege tragen eine gemessene Uhrzeit ("vom 2026-09-24 21:49 MESZ", "geschrieben 13:52 MESZ").
Anforderung: Beim Einfuegen die Uhrzeit per date eintragen, keine geschaetzte.

**Nicht beanstandet:** Alle 19 Seiten-, Gleichungs-, Abbildungs-, Fussnoten- und Literaturangaben; das woertliche
Bellazzini-Zitat; die Wiedergabe des Lesungsurteils; Z. 9-10, 13, 16, 20, 22-24 (ausser B6), 31-34 (ausser B11, B15); die
[A]-Marken nach Legende WARUM-SPIN-2.md Z. 7-8 ("am ... Volltext geprueft"), sobald B4 und B9 behoben sind.

## 6. Ende

- Urteil: **einfuegen nach genannten Aenderungen.** Geruest und Belegstellen tragen. Vor dem Einfuegen sind die Auflagen A
  (B1-B4, B6-B11, B17) und R (B5, B14, B15) zu erfuellen. E (B12, B13, B16, B18) nach Ermessen der Leitung.
- Quote:
  - Fundstellen (Seite, Gleichung, Abbildung, Fussnote, Literaturnummer): 19 von 19 stimmen.
  - Woertliche Zitate: 2 von 2 stimmen.
  - Inhaltsangaben: eine falsch (B1).
  - LESUNG-Anforderungen (21 Zeilen, Abschnitt 2 dieser Datei): 11 umgesetzt, davon 6 mit Mangel; 5 teilweise; 2 ueberzogen;
    2 fehlen; 1 nur bedingt einschlaegig.
- Nach der Ueberarbeitung muss ein frischer Leser die geaenderten Saetze erneut gegenlesen, mindestens Z. 14, 17, 18, 25, 36
  und den neuen Bezug auf den 24.09.-Nachtrag.
- Werkzeuge: nur date, ls, grep, sed -n, cut, wc, head. Kein Rechnen auf dem Rechner, kein python/awk/git/Peerbus, keine
  Unteragenten. Gesperrte Pfade nicht geoeffnet. Den Ordner eines parallelen Pruefers nicht geoeffnet.
- Zeiten (date): Beginn 21:07:28, Ende 21:19:03 CEST. Dauer im Kopf: 21:07:28 + 11 min = 21:18:28, + 35 s = 21:19:03,
  also 11 min 35 s; Zeitbox 25 min eingehalten.
