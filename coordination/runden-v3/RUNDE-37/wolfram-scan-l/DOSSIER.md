# WOLFRAM-SCAN-L: Dossier. Was bietet das Wolfram Physics Project fuer ein Weltmodell, das passt? (Runde 41, Literatur und Werkzeug)

- feldforscher fuer Leitung claude-primary. Recherche 2026-10-04 14:08:52 bis 14:38:01 CEST, Dossier ab 14:42:59 (date).
- Grundlage: KARTE.md (E1 bis E5) und Auftragserweiterung von Finn ("check das komplett durch"). Protokoll aller Abrufe,
  Zitate, Gestrichenes: ARBEITSFELD.md. Seitenkarte mit Lesestand: SEITENKARTE.md. Lokale Kopien: quellen/.
- Kennzeichen: [S] an der lokalen Kopie selbst gelesen (Abruf-Nr., Seite bzw. Zeile), [S-Abstract] nur Abstract gelesen,
  [S-Projekt] Projektdatei gelesen, [L] Gedaechtnis, [L?] unsicher, [M] eigene Herleitung, [ES] eigener Schluss,
  [H] Hypothese, [G] im Projekt gerechnet.
- 53 von 60 Abrufen (3 ohne Inhalt: 403, 404, Host unbekannt). Keine Websuche. Kein Rechnen.

## 1. Ergebnis zuerst

1. **Kein eigener "Modell-Explorer":** gemeint sein kann nur die Registry (75 gelistete Regeln, weitere existieren; je
   Regel ein fertiges Notebook mit Bildern; Dimension und Kausalinvarianz nirgends als Zahl) (A2, A29-A32, A52) [S].
2. **Belegt ist Mathematik unter Annahmen, nicht Physik an Daten:** SR, Einstein und QM unter Kausalinvarianz,
   Dimensionserhaltung, Ergodizitaet und gesetzter Born-Regel (A35 S. 35-38, A36 Gl. 29); keine bestaetigte Vorhersage.
3. **Spin 1/2 und 3+1 fehlen:** nur Vermutungen (2021) und Fermi-Statistik in Strings (2025); keine Regel mit
   3+1-Kausalgraph; Wolfram 2026: "we don't ... know why ... 3 dimensions of space" (A37, A47, A4 S. 283-285, A50) [S].
4. **Fuer Finns Weiche:** Wolfram-Kausalgraphen haben im Kleinen feste Nachbarn [M]; Gorard raeumt das ein und rettet
   Lorentz nur durch Vergroeberung (A34 S. 31-32) [S]. Mikroskopisch Seite (A); ob grob (B)-artig: offen, Karte K1.
5. E2 und E3 der Leitung im Kern bestaetigt; E1 verletzt; E4 und E5 teils (Abschn. 3).

## 2. Erwartungsverstoesse (das eigentliche Ergebnis, wichtigstes zuerst)

| Nr | Erwartet | Gefunden | Fundstelle |
|---|---|---|---|
| V1 | E5 und Karte: Kausalgraphen sind kausalmengen-aehnlich (Ue3), Lorentz-Gleichverteilung offen | Mikroskopisch das Gegenteil einer Poisson-Kausalmenge. Eigene Herleitung aus der Definition "edge between events A and B if the input to B involves output from A" (TI S. 362): jedes Ereignis hat hoechstens so viele Eingangskanten wie die Regel links Relationen hat und hoechstens so viele Ausgangskanten wie rechts; Links sind Teilmenge der Kausalkanten, also beschraenkte Linkzahl [M]. Gorard: Streuungen haben "almost surely infinite" viele Links; "it might at first appear that the average out-degree ... would need to be infinite in order to maintain compatibility with Lorentz symmetry"; Antwort: "coarse-graining over the underlying (microscopic) causal network", effektiver Grad "may be unbounded, even if the out-degree ... in the underlying (microscopic) is bounded". Lorentz-Kovarianz heisst dort: "the orderings of timelike-separated updating events are always preserved across all inertial reference frames". Schulprojekt 2024: Hoechstgrad 15 bleibt, Streuung hat 23 | A34 S. 27-28, 31-32 (Z. 1363-1378, 1567-1651) [S]; A25 [S]; A38 Z. 117-160 [S]; [M] |
| V2 | E1: Registry mit Eigenschaften je Regel (Wachstum, Dimension, Kausalinvarianz); "Modell-Explorer" | Keine dynamischen Kennzahlen. Liste: nur Nummer, Signatur, Vorschaubild; Sortiermenue mit leeren Platzhaltern "[[Sort by OptionX]]". Eintrag: Notebook-Vorlage mit Bildern ("Effective dimension versus radius" als Kurve), kein Kommentar, keine Kausalinvarianz. WolframModelData: 16 Eigenschaften nur der Regel selbst (Rule, RuleSignature, InitialCondition, ...). Webliste 75 Eintraege, wm44586 existiert ausserhalb. Kein Explorer-Werkzeug | A2 Z. 86-94 [S]; A29 Z. 25-182 [S]; A32 Z. 27-59 [S]; A31 [S]; A5, A52 [S] |
| V3 | Karte: Kandidatenregeln, die zu 3+1 und Kausalinvarianz passen | Keine. TI: Dimensions-Beispielregel {{x,y},{x,z}} -> {{x,y},{x,w},{y,w},{z,w}} raeumlich ~2,6, aber "C_t ~ 2.2^t ... exponential growth ... increasing causal disconnection"; endlich-dimensionale Kausalgraphen nur mit "dimension 2". Ankuendigung 2020: "2.7 is not 3". Wolfram 2026: "we don't ... know why the universe ... has (at least approximately) 3 dimensions". Leuenberger 2021: Kausalmengen und Wolfram-Projekt "leave open" die Erzeugung eines 3+1-Minkowski-Graphen aus einfachen Regeln | A4 S. 283-285 [S]; A56 Z. 218-219 [S]; A50 Z. 130 [S]; A49 (2110.03388) [S-Abstract] |
| V4 | E3: Spin hoechstens Stichwort | Mehr als ein Stichwort, aber kein Ergebnis: "it seems as if Fermi-Dirac statistics may be associated with multiway graphs where we see only non-merging branches ... Spinors may then turn out to be as straightforward as being associated with directed rather than undirected spatial hypergraphs" (2021). Dez. 2025: "Leibnizian strings ... exhibit a Fermi-Dirac distribution ... an abstraction of a N-fermion system". Kerndokumente 2020: "fermion", "Pauli", "chiral" 0 Treffer | A37 Z. 113-114 [S]; A47 (2512.20587) [S-Abstract]; A4, A35, A36 grep [S] |
| V5 | E2: Programm ohne bestaetigte Vorhersage | Bestaetigt, aber es gibt Zahlen, und sie widersprechen sich: Oligonen "fairly small multiples of 10^-30 eV" (TI) gegen "10^-20 electron masses" (Glossar, also etwa 5e-15 eV [ES]); Knotenzahl 10^358 (TI-Tabelle, mit "?") gegen 10^400 (Glossar); das Plakat nennt "10^400 steps", die TI-Tabelle ~10^119 Gesamt-Updates bzw. ~10^477 Einzelereignisse (je mit "?"); Elementarlaenge 10^-93 m (2020) gegen 10^-90 m "somewhat unreliable" (2021). Die TI-Oligonenskala liegt 8 Groessenordnungen unter der im selben Satz zitierten Schranke ">~10^-22 eV" [ES]. Offene Begutachtung der TI: genau ein Gutachten (Promotion ausserhalb der Physik, Abschn. 8.9). Veroeffentlicht in Complex Systems, "Founded by Stephen Wolfram in 1987" | A4 S. 416-418 [S]; A9 [S]; A39 [S]; A37 Z. 129 [S]; A43 (eingebettete Daten) [S]; A51 Z. 8 [S] |
| V6 | E4: Kritik an Kausalinvarianz als Lorentz-Ersatz | Die gelesene Fachkritik (Aaronson 2002) ist eine Bell-Kritik an einem anderen Regime: Kausalinvarianz + "no preferred inertial frames" + Bell-Verletzung + Regeln "on a fixed graph, not on a distribution or superposition over graphs" schliessen sich aus. Das Programm von 2020 ist ein Multiway-Modell mit gesetzter Born-Regel; kein Wolfram-Dokument zitiert Aaronson. Die Lorentz-Valenz-Frage stellt Gorard selbst. Eine Fachkritik der Lorentz-Herleitung fand ich ohne Websuche nicht: nach Recherchestand nicht belegt | A45 Abschn. 3.2 (Z. 405-506) [S]; grep A4, A34-A36 [S]; A34 S. 31-32 [S] |
| V7 | Lesart W "Werkzeug" heisst: Netz mit eigener Dynamik als Generator | Das Programm nutzt Hypergraphen inzwischen auch als Rechengitter fuer bekannte Gleichungen: CCZ4-Einstein-Gleichungen "defined in terms of Wolfram model evolution over discrete (spatial) hypergraphs", mit "very strong" Annahmen. Dort ist die ART eingesetzt, nicht hergeleitet | A49 (2303.07282) [S-Abstract]; A37 Z. 77 [S] |
| V8 | (keine Erwartung) Projektstand | Fachartikel bis 2023, Livestreams bis 29. Okt. 2023, Q&A-Antworten Feb. bis Mai 2020 (eine von Mai 2019), Bulletin-Adressen tot (404 bzw. Host unbekannt). Aber 130 Notebooks 2026 (Astrobiologie 29, Fehlersuche 24, Spiele 23, ML 10, "Infrageometry" 9; kein Titel zu Teilchen oder Spin) und WolframModelData 6.0.1 vom 31. Juli 2026 | A6, A41, A19-A23, A53, A55, A48, A32 [S] |

## 3. Erwartungen E1 bis E5 mit Ausgang

| Nr | Erwartung (Kurzform) | Ausgang | Fundstelle | Kennz. |
|---|---|---|---|---|
| E1 | Registry bzw. Explorer mit Regeln und Eigenschaften je Regel | **verletzt** (V2): Regeln und Signaturen ja, Eigenschaften nur als Bilder, kein Explorer-Werkzeug | A2, A29-A32, A52 | [S] |
| E2 | SR, ART, QM als Programm hergeleitet, nicht an Daten bestaetigt | **eingetroffen**, mit Nuance V5. SR: "if the underlying rule has causal invariance, its limiting behavior will show relativistic invariance" (TI S. 366), vorgefuehrt nur am Gitter BA->AB; Einstein: unter "asymptotic dimensionality preservation", "weak ergodicity", orthonormalen Hyperkanten und "d^4 x" (A35 S. 35-38); QM: Born-Regel gesetzt (A36 Gl. 29). Vorhersagen: "general predictions about cosmology, astrophysics and quantum processes" ohne Zahl (A24) | A4 S. 363-372, A35, A36, A24 | [S] |
| E3 | Kein Modell als unsere Welt; Teilchen und Spin 1/2 hoechstens skizziert | **eingetroffen** fuer "unsere Welt" ("we have not yet found the specific rule", A19; "encouraging, but not definitive", TI S. 420) und fuer Spin-1/2-Drehverhalten; **teils verletzt** fuer Fermi-Statistik (V4). Teilchen: Analogien (Nicht-Planaritaet, Rule-110-Gleiter), ein Hypergraph-Beispiel; "Existing results in graph theory do not go very far" (TI S. 373); 2021: "We haven't 'found the electron' yet" | A4 S. 372-377, 419-420; A19; A37 Z. 110-114; A47 | [S] |
| E4 | Fachliche Kritik vorhanden | **teils** (V6): Aaronson 2002 (Bell, anderes Regime), Rodriguez Caballero 2021 und Leuenberger 2021 (je Abstract); Lambs Kritik gesperrt (403); die schaerfste Lorentz-Frage kommt aus dem Programm selbst | A45, A49, A46, A34 | [S], [S-Abstract] |
| E5 | Kausalgraphen wie Kausalmengen behandelbar; Lorentz-Gleichverteilung offen | **teils** (V1): formal ja (Halbordnung; Myrheim-Meyer, Mittelpunkt-Skalierung, Benincasa-Dowker anwendbar, Gorard 2011.12174); aber beschraenkte Valenz, und die Ordnungs-Schaetzer "significantly underestimate the limiting dimension ... The reasons for this discrepancy are not currently clear" (S. 50-52). Lorentz-Gleichverteilung nirgends gezeigt | A34 S. 50-52, 31-32 | [S], [M] |

## 4. Werkzeugbeschreibung: Explorer, Registry, Tools (was man damit tun kann)

- **Registry of Notable Universe Models** (https://www.wolframphysics.org/universes/) [S A2, A14-A17, A29-A31]:
  - Liste: 5 Seiten zu je 15 Eintraegen (75), Kurzcode ("Short Code: A hash code for a rule", Glossar A9), Signatur
    (z. B. 2_3 -> 3_3), Vorschaubild; Knopf "Random universe"; Sortiermenue mit unausgefuellten Platzhaltern. Die
    Liste ist als Zeichenkette sortiert und endet bei wm1869; weitere Eintraege (wm44586) sind nur direkt erreichbar.
  - Eintrag (Beispiel wm1268): Regeltext, Anfangszustand, Schrittzahl; Abschnitte "Basic Evolution",
    Knoten- und Kantenzahlen mit Formel (FindSequenceFunction), "Causal Graph" (Bild, geschichtet, Abstandsmatrix),
    "Final State Properties" (Gradverteilung, Nachbarschaftsvolumina, "Effective dimension versus radius",
    Nachbarschaftskugeln), "Spreading of Effects" (Nachbarschaftsvolumina im Kausalgraphen), "Other Evolution Orders"
    (zufaellige und andere Reihenfolgen), Zentralitaet und Zyklen. Knoepfe "make editable copy" (Wolfram Cloud) und
    "download notebook". Alles als statische Ausgabe; nichts wird auf der Webseite gerechnet.
  - TI S. 435: Die Registry "contains results on specific examples of our models, including all those explicitly used
    in this document" [S A4].
- **WolframModelData** (Function Repository, "Programmatic API") [S A32]: Kurzcode -> Regel und umgekehrt; 16
  Eigenschaften der Regel (u. a. Rule, RuleSignature, InitialCondition, MaximumArity, RuleComplexity,
  TransformationCount, ReleaseDate); keine Dynamik-Kennzahl. Version 6.0.1 vom 31. Juli 2026.
- **Tools** (/tools/) [S A5, A52, A33]: Funktionen im Wolfram Function Repository (WolframModel, WolframModelPlot,
  WolframModelEvolutionObject, MultiwaySystem, CausalGraph, HypergraphNeighborhoods, HypergraphToGraph u. a.);
  Hands-on-Notebook; Notebook-Archiv (1258 Eintraege); Video-Archiv (431); SetReplace (Wolfram-Language-Paket mit
  C++17-Kern, braucht "Wolfram Language 12.3+", frei als Wolfram Engine; Optionen "EventOrderingFunction",
  "EventSelectionFunction", Hilfsfunktion "CausalDensityDimension"). **Kein Python.** Die TI selbst gibt es als
  rechenbares Notebook (TI S. 435).
- **Was man damit tun kann** [ES]: Regeln ansehen, eine zufaellige ziehen, das Notebook in der Cloud kopieren und mit
  Wolfram Language weiterrechnen. Fuer uns (Python, keine Wolfram Language im Projekt): Regeltexte von den Seiten
  ablesen und die Ersetzung selbst nachbauen. Die Regeln sind kurz; eine Aktualisierung pro Generation ("alle
  passenden, nicht ueberlappenden Stellen", A34 S. 19) ist in Python einfach nachzubauen [ES].

## 5. Literaturstand: belegt, behauptet, offen (je Bereich)

| Bereich | (a) gemessen bzw. gerechnet in der Quelle | (b) hergeleitet unter Annahmen bzw. nuetzlich verdichtet | (c) behauptet ohne neue Evidenz |
|---|---|---|---|
| Raum | Ballwachstum V_r ~ r^2,6 bis 2,7 fuer eine Regel (TI S. 283, A56 Z. 218); "d often does not end up being integer valued ... exponential or more complex behavior is common" (TI S. 360) | Kruemmung aus dem r^2-Glied von V_r (TI S. 360); Graphabstand "akin to a generalized taxicab metric", Riemann erst nach "softening" ueber Ollivier-Ricci und Wasserstein (A27) | "space ... merely an emergent large-scale feature" (TI S. 353) |
| Zeit, Kausalinvarianz | Haeufigkeit der Kausalinvarianz bei Stringregeln nur als Bilder (TI Kap. 5) | Kausalgraph = Halbordnung (TI S. 363); Kausalinvarianz = gleicher Kausalgraph fuer jede Reihenfolge (Glossar A9) | "time is fundamentally different from space" (A19) |
| SR, Lorentz | Gitter BA->AB und gitterartiges Netz (TI S. 364-366; A34 S. 28-30) | Lorentz-Kovarianz als Erhalt zeitartiger Reihenfolgen ueber Blaetterungen (A25, A34 S. 28); "conformal invariance" der Halbordnung (A34 Abstract) | "applies to any rule that has causal invariance" (A56 Z. 377); mikroskopische Valenz nur durch Vergroeberung entkraeftet (A34 S. 32) |
| Schwerkraft | C_t ~ 2,2^t fuer die 2,6-dim. Regel; Kausalgraph-Dimension 2 fuer zwei Regeln (TI S. 283-285); numerische Relativitaet mit Hypergraph-Gitter (2303.07282, Abstract) | Vakuum- und Materie-Einstein-Gleichungen aus Dimensionserhaltung + Ergodizitaet + Orthonormalitaet (TI S. 367-372; A35 S. 35-38); Lambda nur "up to an integration constant" (A22); Benincasa-Dowker als Spezialfall unter Poisson-Annahme (A34 Abstract) | "We know that ... its dynamics satisfy the Einstein equations" (A50 Z. 130, 2026) |
| QM | keine Rechnung an einer Regel fuer Bell bzw. Born gefunden | Multiway-Graph, Beobachter = Blaetterung, Pfad-Drehung e^(iS) (TI S. 381-391); Born-Regel gesetzt (A36 Gl. 29) | CHSH-Verletzung "one is able to prove ... in much the same way as ... de Broglie-Bohm" (A28, A36 S. 53-54) |
| Teilchen, Spin | ein Hypergraph-Beispiel mit "particle-like" Delle (TI S. 376-377); Fermi-Dirac-Verteilung in Multiway-Strings (2512.20587, Abstract) | Teilchen als lokal stabile Strukturen bzw. verbotene Minoren als "combinatorial analog of Noether's theorem" (A36 S. 53) | "Spinors may then turn out to be as straightforward as ... directed ... hypergraphs" (A37 Z. 113) |
| Eichfelder | keine | Eichung = Blaetterung im Multiway-Graphen, Lie-Gruppe als Grenzfall von Permutationen (TI S. 410-412) | "local gauge invariance: consequence of causal invariance in the multiway graph" (TI S. 356) |
| Zahlen, Vorhersagen | keine Messung | Elementarlaenge, Xi ~ 10^116 aus einem "simple model" (TI S. 413-417) | Oligonen als Dunkle Materie, zeta ~ 10^5 Sonnenmassen/s (TI S. 418; A37 Z. 138); "success of our Physics Project" (A50 Z. 120) |

- **Kalibrierung:** (a) ist schmal: einige Wachstumsexponenten, Kegelwachstum, Dimensions-Schaetzer, ein Gradvergleich.
  (b) ist der Kern und hat benannte Annahmen. (c) waechst mit den Jahren ohne neue Rechnung: 2020 "We're glossing
  over lots of details" (A56 Z. 418), 2026 "We know that ... Einstein equations" (A50 Z. 130). Das ist gewachsene
  Gewissheit ohne neue Evidenz.
- **Eigene Drift [ES]:** Meine Sicherheit "Wolfram = Seite (A)" stieg waehrend der Recherche, waehrend sich die Frage in
  "mikroskopisch" und "vergroebert" aufloeste. Belegt ist nur die mikroskopische Seite.

## 6. Regime und Moderatoren (statt "eine Seite irrt") [ES, Belege je Zelle]

| Moderator | Regime 1 | Regime 2 | Was es aufloest |
|---|---|---|---|
| Massstab | mikroskopisch: beschraenkte Valenz, Ruhesystem moeglich [M, S A34] | vergroebert: Gorards effektives Netz mit unbeschraenktem Grad (A34 S. 32) | "Wolfram ist lokal" und "Wolfram ist Lorentz-invariant" widersprechen sich nicht, sie meinen verschiedene Skalen |
| Einzelgeschichte gegen Multiway | Aaronson 2002: ein Graph, Annahme (4) wahr (A45) | Gorard 2020: alle Zweige, Born gesetzt (A36) | Bell-Einwand und Bell-Behauptung treffen verschiedene Modelle |
| Messverfahren | Ordnungs-Schaetzer (Myrheim-Meyer, Mittelpunkt) | Abstands-Schaetzer (geodaetische Kegel) | Dimensionen auf Wolfram-Graphen haengen vom Schaetzer ab (A34 S. 50-52); das ist selbst ein Fingerabdruck "kein Poisson-Netz" [ES] |
| Rolle des Hypergraphen | fundamental: Einstein soll folgen (2020) | Rechengitter: Einstein eingesetzt (CCZ4, 2021/2023) | "Werkzeug" und "Theorie" stehen im Programm nebeneinander |
| Zeitfenster und Gattung | Kerndokumente 2020 (Annahmen benannt) | Essays 2021-2026 (Annahmen weggelassen, Zahlen driften) | Gewissheit steigt mit dem Abstand zu den Rechnungen |

## 7. Unterscheidungspunkte [ES, Formeln M]

| Paar | Wo beide passen | Wo sie messbar auseinanderlaufen | Zugaenglich? |
|---|---|---|---|
| U1: Lesart W ("Lorentz entsteht grob", Gorard) gegen Lesart T ("Ruhesystem bleibt") | quadratische Intervalle (keine Vorzugsrichtung erkennbar) | langgezogene Intervalle: Kennzahl r = L/(2 sqrt N) (L laengste Kette, N Elemente des Intervalls). Poisson in 1+1: r konzentriert sich unabhaengig von der Form; Gitter: r = (a+b+1)/(2 sqrt((a+1)(b+1))) >= ~1 mit Schwanz [M]. W: Schwanz schrumpft mit N; T: bleibt | ja, in silico (Karte K1) |
| U2: Gorards Vergroeberung gegen BHS-Logik (endliche Valenz waehlt eine Richtung) | jede beobachtbare Skala, wenn die Elementarlaenge ~1e-93 m betraegt (TI S. 417) | nur bei einzelnen Kausalkanten | **in der Natur nicht zugaenglich**; empirisch nicht unterscheidbar, solange K1 nicht auch grob eine Spur zeigt |
| U3: Aaronson gegen Gorard (Bell) | Einzelgeschichte ohne Fernfaeden (beide: keine Bell-Verletzung) | eine konkrete Multiway-Regel mit Beobachter-Blaetterung, deren Pfadgewichte CHSH = 2 sqrt 2 liefern (Gorard) oder nur mit gesetzten Wahrscheinlichkeiten (Aaronsons Lehre) | rechnerisch moeglich, in keiner gelesenen Quelle gerechnet |
| U4: Wolfram-Schwerkraft (Dimensionserhaltung) gegen induzierte Schwerkraft (Ue1, Sakharov) | Einstein-Form im Grossen | G haengt bei Sakharov von der Zahl der Felder ab [L], bei Wolfram von "proportionality between node counts and spatial volume" (TI S. 357) | in der Natur nicht; im Modell mit Feldern auf einem gewachsenen Netz [H] |
| U5: Kausalinvarianz als "Zeit umbenennen frei" (P3, die 1/2) gegen Horava-artig (lambda != Einstein-Wert) | kausalinvariante Regeln im Grossen | Regeln ohne Kausalinvarianz: effektives lambda [H] | unklar; nicht gerechnet |

## 8. Was davon fuer unser Weltmodell taugt (Schichten)

| Schicht | Was Wolfram liefert | Was dort ebenso fehlt | Bezug zu unseren Straengen |
|---|---|---|---|
| **Buehne mit Dynamik** | Ein Netz, das aus einer Regel waechst; "space itself is a dynamic construct created and maintained by ongoing updating events" (TI S. 368) [S]. Regelkatalog (Registry, WolframModelData) [S] | Keine Regel mit 3+1-Kausalgraph (V3); Dimension oft nicht ganzzahlig und variabel (TI S. 360); Kausalkegel oft exponentiell (TI S. 283) [S] | Fuellt Finns Spalte (C) "Netz, das selbst schwankt" mit einer vierten Bauart: deterministisch gewachsen statt Summe ueber Netze [ES]. Brauchbar als Netzgenerator fuer unsere vorhandenen Tests (INDUZIERT, Fluss-Eis), nur nicht als 3D-Raum [ES]. Finns Tetraeder: Gorard nennt das Wolfram-Modell eine Verallgemeinerung von CDT mit "pentachora (4-simplices)" (A26) [S]; Pachner-Zuege sind Ersetzungsregeln auf 4-stelligen Hyperkanten, also Wolfram-Regeln; PONZANO-1 benutzt sie bereits [ES]. Ob sie kausalinvariant sind: unbekannt [H] |
| **Ausbreitung und Lorentz** | Endliches c, "related to the fact that the underlying rules involve rewriting hypergraphs only of bounded size" (TI S. 366) [S]; Blaetterungsfreiheit als Lorentz-Kovarianz (A25) [S] | Richtungsunabhaengigkeit von c nur "an aggregate statement" (A54 Z. 213, 337) [S]; kein Ruhesystem-Test; das Programm erwartet selbst "maximum boosts" fuer leichte Teilchen (A37 Z. 130) [S] | Finns Weiche: mikroskopisch Seite (A) [M, S A34]. P1 (ein Lichtkegel fuer alles) ist strukturell erfuellt, wenn alle Materie Netzstruktur ist, wie in Ue3 [ES]. Licht im Netz: dieselbe "Feinstruktur"-Frage wie unsere k^2-Korrekturen in REGGE-WELLE-1 [ES] |
| **Inhalt mit Spin 1/2** | Vermutungen: Fermi-Dirac bei nicht verschmelzenden Zweigen, Spinoren bei gerichteten Hypergraphen (A37) [S]; Fermi-Dirac-Verteilung in Strings 2025 [S-Abstract] | Kein Spin-1/2-Drehverhalten, keine chiralen Fermionen, kein Dirac-Operator in den Kerndokumenten [S] | SPIN-KAUSAL-L: Spin braucht Zusatzstruktur jenseits der Ordnung ("Rahmen je Element") [S-Projekt]. Wolfram-Hyperkanten sind geordnete Tupel (TI S. 3), die Geometrie ignoriert die Ordnung (TI S. 358): das ist lokale Zusatzstruktur, die als Rahmen dienen koennte [H] |
| **Wechselwirkung** | Eichinvarianz aus Kausalinvarianz im Multiway-Graphen behauptet; Lie-Gruppe als Grenzfall (TI S. 410-412); Faserbuendel "started to identify" (A37 Z. 110) [S] | Keine konkrete Eichgruppe; SU(3)xSU(2)xU(1) nur Hoffnung (A37 Z. 112) [S] | Unser Fluss-Eis (U(1) auf Kanten, FLUSS-1) ist konkreter [G]. Wolfram bietet hier nichts Rechenbares [ES] |
| **Schwerkraft** | Einstein-Gleichungen aus Dimensionserhaltung unter benannten Annahmen (A35) [S]; Benincasa-Dowker als Spezialfall unter Poisson-Annahme (A34) [S-Abstract]; Hypergraph als Rechengitter fuer ART (V7) [S-Abstract] | Lambda frei ("up to an integration constant", A22) [S]; keine Herleitung der Vorfaktoren; kein Sakharov-Mechanismus | Dritter Weg neben Regge (Wirkung eingesetzt) und Ue1 (Sakharov) [ES]. Brueckenhypothese zu P3: Kausalinvarianz = Blaetterungsfreiheit = "Zeit umbenennen ist frei"; wenn das in der effektiven Dynamik gilt, waere die 1/2 geschenkt wie in Ue3 [H, nicht gerechnet] |

- **Kausalmengen (Ue3):** Ordnung ja, "Zahl = Volumen" und Poisson nein; Wolfram-Graphen ersetzen keine Streuung, koennten
  aber eine Dynamik fuer Kausalmengen sein (Gorard: klassisches und Quanten-Sequential-Growth als Spezialfall der
  Multiway-Evolution, A34 Abstract) [S-Abstract]. Fuer KAUSAL-4D-SCHICHT (Einzelnetz-Rauschen) gilt [H]: ein
  Wolfram-Netz waere glatter (feste Valenz), aber mit Vorzugsrichtung.
- **Gesamturteil [ES]:** Als **Werkzeug** taugt Wolfram fuer uns als Regelkatalog und Ideengeber fuer gewachsene Netze;
  die Software selbst nicht (Wolfram Language). Als **Theorie** liefert es keine Schicht, die uns fehlt, in belegter
  Form: Buehne ohne 3+1, Lorentz nur vergroebert, Spin 1/2 und Eichgruppe offen, Schwerkraft unter Annahmen. Der
  nuetzlichste Einzelgedanke ist die Gleichsetzung "Kausalinvarianz = Blaetterungsfreiheit", die unsere 1/2-Regel
  (P3) beruehrt.

## 9. Kartenvorschlaege (hoechstens zwei, je <= 10 min auf der .69, Python, ohne Wolfram Language)

### K1 WOLFRAM-RUHE-1: Hat das "lorentzartige" 2D-Vorzeigebeispiel ein verstecktes Ruhesystem?

- **Frage:** Unterscheidet sich die Intervall-Statistik im Kausalgraphen der Regel
  R2 = {{x,y,y},{x,z,u}} -> {{u,v,v},{v,z,y},{x,y,v}} (TI S. 284; bei Gorard "asymptotically-flat causal network with a
  two-dimensional Lorentzian manifold-like limiting structure", A34 Fig. 45) von einer Poisson-Streuung in 1+1?
- **Bau:** Ersetzung in Python nachbauen (Standardreihenfolge: je Generation alle passenden, nicht ueberlappenden
  Stellen), Kausalgraph mitschreiben (Kante, wenn ein Ereignis eine Relation verbraucht, die ein anderes erzeugt hat).
  2e4 bis 1e5 Ereignisse. Zusaetzlich eine zufaellige Reihenfolge als zweite Fassung.
- **Messgroesse (intrinsisch, ohne Einbettung):** zufaellige Paare p < q (ziehen, bis jedes Bin 300 bis 600 Intervalle hat, hoechstens 3e4 Paare) je Graph, Intervallgroesse N und
  die laengste Kette L; r = L/(2 sqrt N) in Bins N = 64-128, ..., 1024-2048; dazu Myrheim-Meyer-Dimension je Intervall.
- **Kontrollen:** (P) Poisson-Diamant in 1+1 (Code aus KAUSAL-1), dort konzentriert sich r unabhaengig von der Form;
  Brightwell/Gregory: <l>/(rho V)^(1/d) -> m_d (Surya 2019, S. 31-32, im Projekt lokal) [S-Projekt]; m_2 = 2 [L]; bei
  endlichem N liegt r unter 1 [L], daher nur gegen die eigene Kontrolle vergleichen. (G) Gitterregel BA->AB (TI S. 364)
  bzw. {{x,y,y},{y,z}} -> {{x,y},{y,z,z}} (A34 Fig. 25): r = (a+b+1)/(2 sqrt((a+1)(b+1))) >= ~1 [M].
- **Vorpruefung mit Abbruch:** (i) Ereignisse je Generation muessen mit der Knotenzahl wachsen (sonst waechst das Netz an
  einer Front, Gegensweep G10); (ii) C_t polynomial mit Exponent 1,7 bis 2,3. Verletzt -> Abbruch und Meldung: Dann ist
  das Vorzeigebeispiel keine 1+1-Raumzeit, auch das ist ein Ergebnis.
- **Entscheidung vorab (Schwellen gegen die eigene Kontrolle, nicht gegen 1):** Gleiche Paar-Ziehung fuer alle Graphen.
  Q50 und Q95 = Median und 95-%-Quantil von r je Bin. "Poisson-artig" wenn |Q50(R2) - Q50(P)| <= 0,05 und
  Q95(R2) <= Q95(P) + 0,05 in allen Bins mit >= 300 Intervallen; "Gitter-artig" wenn Q95(R2) >= Q95(P) + 0,15 in den
  zwei groessten Bins; sonst "unentschieden". Grund [L?, Schaetzung]: Bei N ~ 1500 liegt Q95(P) wegen der
  Tracy-Widom-Streuung schon nahe 1, eine feste Schwelle 1,0 waere zu knapp. Gueltig nur, wenn vorab die Gitterkontrolle G
  "Gitter-artig" und eine zweite, unabhaengige Poisson-Probe "Poisson-artig" ergibt; sonst ist der Test ungueltig.
  Trend des Abstands Q95(R2) - Q95(P) ueber die Bins melden: faellt er, stuetzt das Gorards Vergroeberung (U1, Lesart W);
  bleibt er, Lesart T.
- **Ableitbarkeitsprobe:** (1) P und G sind vorab ableitbar, also nur Kontrollen. (2) Fuer R2 nicht ableitbar: Die
  Regel erzeugt effektive Zufaelligkeit (TI S. 359), keine gelesene Quelle nennt Kettenlaengen fuer Wolfram-
  Kausalgraphen; Gorard meldet nur, dass Ordnungs-Schaetzer die Dimension unterschaetzen, "reasons ... not currently
  clear" (A34 S. 52); Suresh vergleicht nur Grade (A38). (3) Linkzahlen sind wegen beschraenkter Valenz vorab ableitbar
  [M] und daher keine Messgroesse. (4) Projekt-grep "laengste Kette", "longest chain", "Myrheim": nur Literaturnotizen
  (RUNDE-22), keine Rechnung. (5) Kann in beide Richtungen scheitern: ja.
- **Laufzeit:** [ungemessene Schaetzung] wenige Minuten je Graph, Kleintest-Spur.

### K2 WOLFRAM-BUEHNE-1: Gibt es unter kleinen Regeln eine mit 3+1-artigem Kausalgraphen?

- **Frage:** Erzeugt irgendeine Regel kleiner Signatur einen Kausalgraphen mit polynomialem Kegelwachstum C_t ~ t^D,
  D in [3,5; 4,5], bei raeumlichem Ballwachstum V_r ~ r^d mit d in [2,5; 3,5]?
- **Stichprobe:** je 200 zufaellige Regeln der Signaturen 2_2 -> 4_2 und 2_3 -> 3_3 (in Python aufgezaehlt, kein Abruf
  noetig), dazu die "Tetraeder-Familie": Pachner-Zug 1-4 als {{a,b,c,d}} -> {{a,b,c,e},{a,b,e,d},{a,e,c,d},{e,b,c,d}}
  und Zug 2-3 auf zwei Tetraedern mit gemeinsamer Flaeche [ES]. Je Regel 3000 Ereignisse, zwei Groessen.
- **Messgroessen:** Ereignisse je Generation, Exponent von V_r, Wachstumsart von C_t (Anpassung log C gegen log t und
  gegen t), D, d.
- **Bestanden:** mindestens eine Regel mit polynomialem C_t, D und d in den Fenstern, stabil ueber beide Groessen; dann
  K1 in 3+1 fuer diese Regel. **Gescheitert (informativ):** keine; dann gibt es bei kleinen Signaturen keine 3+1-Buehne,
  passend zu TI S. 283-285.
- **Ableitbarkeitsprobe:** Keine Quelle fuehrt Kausalgraph-Dimensionen je Regel (WolframModelData ohne solche
  Eigenschaft, Registry nur Bilder) [S]; die TI meldet exponentielles C_t fuer die "globular" 2_2 -> 4_2-Regeln und nur
  2D-Beispiele [S]. Der Ausgang ist eher negativ zu erwarten, aber nicht ableitbar; fuer die Pachner-Familie spricht
  Wissen aus der dynamischen Triangulierung fuer zerknitterte bzw. verzweigte Netze ohne Wirkung [L?], ebenfalls nicht
  ableitbar fuer deterministische Aktualisierung. Projekt-grep: keine Rechnung zu Hypergraph-Regeln.
- **Laufzeit:** [ungemessene Schaetzung] 400 Regeln mal 3000 Ereignisse in Python: Minuten; Abbruch einer Regel bei
  mehr als 1e5 Relationen.

## 10. Gegensweep-Befunde (Was war so selbstverstaendlich, dass ich es nicht geprueft habe?)

- **Geprueft und verletzt:** G1 "die Webliste der Registry ist vollstaendig" (wm44586 existiert ausserhalb, A31);
  G2 "der Kausalgraph ist das Hasse-Diagramm" (so Gorard A26; Gegenbeispiel: A erzeugt r1, r2; B verbraucht r1, erzeugt
  r3; C verbraucht r2, r3: Kante A->C ist transitiv [M]); G10 "Kausalgraph-Dimension 2 passt zu Raum etwas ueber 2"
  (passt nicht zu d+1 [ES]; moegliche Ursache Front-Wachstum [H]).
- **Geprueft und bestaetigt:** G3 kein Explorer-Werkzeug (A52, grep aller Kopien); G4 Complex Systems von Wolfram
  gegruendet (A51); G5 beschraenkte Valenz (Gorard und Suresh); G6 Spin teils (Fermi-Statistik-Ansaetze vorhanden).
- **Nicht geprueft:** G7 ob das TI-PDF vom April 2020 der gueltigen Fassung entspricht; G8 ob ein Registry-Eintrag
  Raumdimension ~3 zeigt (Bilder nicht ausgewertet); G9 Vollstaendigkeit der arXiv-Phrasensuche (31 Treffer gesamt).

## 11. Offene Fragen

1. Wird das mikroskopische Ruhesystem bei Vergroeberung unsichtbar? (K1)
2. Gibt es ueberhaupt eine Regel mit 3+1-Kausalgraphen? (K2)
3. Warum unterschaetzen Ordnungs-Schaetzer die Dimension auf algorithmischen Kausalmengen? Hypothese: Gitter- bzw.
   Frontcharakter [H].
4. Traegt die Ordnung innerhalb der Hyperkanten einen Rahmen, der Spinoren erlaubt? [H]
5. Ist "Kausalinvarianz = Blaetterungsfreiheit" stark genug, um die 1/2 (P3) festzulegen? [H]
6. Inhalt der "Infrageometry"-Notebooks 2026 (nur Titel gesehen).

## 12. Selbstanzeigen

- **S1:** Einmal lief `awk 'length>0'` als Leerzeilenfilter mit (entgegen "lokal kein awk"); nur 5 Zeilen Vorschau, nicht
  weiterverwendet, kein Einfluss auf Befunde (ARBEITSFELD, nach A6).
- **S2:** A47 und A49 sind Abfragen der arXiv-API (Datenbankabfrage, nicht das Websuch-Werkzeug); als zwei der fuenf
  Zusatz-Abrufe gezaehlt. Die 24-Monats-Pruefung nach Regel 7 beruht nur auf dieser Phrasensuche.
- **S3:** In zwei lokalen Kopien Personendaten ersetzt (E-Mail eines Gutachters in A43, eigene IP-Adresse in A46).
- **S4:** Grosse Dateien in quellen/ (TI-PDF 110 MB, arXiv-PDF 17 MB, Plakat 12 MB).
- **S5:** Vieles nur per grep bzw. Anriss gelesen; der Lesestand steht je Seite in SEITENKARTE.md. Bilder (Registry,
  Kausalgraphen) und Notebook-Ausgaben nicht ausgewertet.
- **S6:** Die Valenz-Herleitung [M] ist meine; gegen zwei Quellen geprueft, nicht von einem zweiten Leser.
- **S7:** "Modell-Explorer = Registry" ist mein Schluss; Finn kann etwas anderes meinen.
- **S8:** Der Widerspruch Oligonen-Masse gegen Dunkle-Materie-Schranke ist [ES]; ob die zitierte Schranke fuer
  Wolframs "ideal gas" gilt, habe ich nicht geprueft.
- **S9:** Mehrere Aussagen beruhen nur auf Abstracts (2512.20587, 2110.03388, 2108.03751, 2303.07282, 2301.12455).
- **S10:** Kein frischer Leser hat dieses Dossier gegengelesen; ein eigener Rueckwaertsdurchgang fand einen Fehler
  ("10^400 nodes" faelschlich auch dem Plakat zugeschrieben, das "10^400 steps" nennt) und eine zu knappe Schwelle in K1;
  beides korrigiert und im ARBEITSFELD (Abschn. 7) vermerkt.

## 13. Quellenliste mit Abrufstand (alle 2026-10-04, lokale Kopie in quellen/)

| Nr | Autor, Jahr, Titel | URL | Abruf |
|---|---|---|---|
| A1 | Wolfram Physics Project, Startseite | https://www.wolframphysics.org/ | 14:10:33 |
| A2, A14-A17 | Registry of Notable Universe Models, Seiten 1-5 | https://www.wolframphysics.org/universes/ (2.html-5.html) | 14:10:52, 14:22:20-14:22:22 |
| A3 | Technical Introduction, Inhaltsverzeichnis | https://www.wolframphysics.org/technical-introduction/ | 14:11:54 |
| A4 | Wolfram, S. (2020): A Class of Models with the Potential to Represent Fundamental Physics (PDF, 448 S.; Complex Systems 29(2), 107-536) | https://www.wolframphysics.org/technical-introduction/inc/Wolfram-ModelsForPhysics.pdf | 14:12:07-14:13:20 |
| A5 | Software Tools | https://www.wolframphysics.org/tools/ | 14:17:54 |
| A6 | Technical Documents (Launch Documents, Bulletins, Schulprojekte, Presse) | https://www.wolframphysics.org/technical-documents/ | 14:17:55 |
| A7 | Q&A Uebersicht | https://www.wolframphysics.org/questions/ | 14:19:09 |
| A8 | Peer Review | https://www.wolframphysics.org/peer-review/ | 14:19:09 |
| A9 | Glossary | https://www.wolframphysics.org/glossary/ | 14:19:10 |
| A10 | Visual Summary (Seite) | https://www.wolframphysics.org/visual-summary/ | 14:19:11 |
| A18 | Bulletins (Weiterleitung: Wolfram Writings, Kategorie Physics) | https://www.wolframphysics.org/bulletins/ | 14:19:11 |
| A19-A23 | Q&A-Kategorien general, scientific-general-interest, relations-to-other-approaches, spacetime-relativity, quantum-mechanics | https://www.wolframphysics.org/questions/<kategorie> | 14:20:20-14:20:24 |
| A24 | Wolfram (2020): Does your theory make predictions? | .../questions/scientific-general-interest/does-your-theory-make-predictions/ | 14:21:31 |
| A25 | Gorard (2020): How can your models be Lorentz invariant? | .../questions/spacetime-relativity/how-can-your-models-be-lorentz-invariant/ | 14:21:32 |
| A26 | Gorard (2020): How do your models relate to causal set theory and CDT? | .../questions/relations-to-other-approaches/how-do-your-models-relate-to-causal-set-theory-and-causal-dynamical-triangulation/ | 14:21:32 |
| A27 | Gorard (2020): Euclidean/Riemannian metric vs. taxicab metric | .../questions/spacetime-relativity/why-do-you-get-a-euclideanriemannian-metric-as-opposed-to-a-taxicab-metric-induced-on-your-hypergraphs/ | 14:21:33 |
| A28 | Gorard (2020): How can your models be consistent with Bell's theorem? | .../questions/quantum-mechanics/how-can-your-models-be-consistent-with-bells-theorem/ | 14:21:33 |
| A29-A31 | Registry-Eintraege wm1268, wm148, wm44586 | https://www.wolframphysics.org/universes/wm1268/ (wm148/, wm44586/) | 14:22:40-14:22:42 |
| A32 | Wolfram, S.; Sandheinrich, B.: WolframModelData (Function Repository, v6.0.1) | https://resources.wolframcloud.com/FunctionRepository/resources/WolframModelData | 14:23:34 |
| A33 | Piskunov, M. u. a.: SetReplace, README | https://raw.githubusercontent.com/maxitg/SetReplace/master/README.md | 14:23:35 |
| A34 | Gorard, J. (2020/2021): Algorithmic Causal Sets and the Wolfram Model, arXiv:2011.12174v2 | https://arxiv.org/pdf/2011.12174 | 14:23:35 |
| A35 | Gorard, J. (2020): Some Relativistic and Gravitational Properties of the Wolfram Model | https://www.wolframcloud.com/obj/wolframphysics/Documents/some-relativistic-and-gravitational-properties-of-the-wolfram-model.pdf | 14:25:54 |
| A36 | Gorard, J. (2020): Some Quantum Mechanical Properties of the Wolfram Model | https://www.wolframcloud.com/obj/wolframphysics/Documents/some-quantum-mechanical-properties-of-the-wolfram-model.pdf | 14:25:55 |
| A37 | Wolfram, S. (2021): The Wolfram Physics Project: A One-Year Update | https://writings.stephenwolfram.com/2021/04/the-wolfram-physics-project-a-one-year-update/ | 14:26:46 |
| A38 | Suresh, A. (2024): Comparing Causal Graphs between String Rewriting and Poisson Sprinkling in Spacetime (Wolfram Winter School) | https://community.wolfram.com/groups/-/m/t/3100485 | 14:26:47 |
| A39 | Visual Summary, PDF | https://www.wolframphysics.org/visual-summary/WolframPhysicsSummary.pdf | 14:29:21 |
| A40 | Working Materials Archive | https://www.wolframphysics.org/archives/index/ | 14:29:30 |
| A41 | Livestreams & Video Archive | https://www.wolframphysics.org/livestreams/ | 14:29:31 |
| A42 | Visual Gallery | https://www.wolframphysics.org/visual-gallery/ | 14:29:33 |
| A43 | Peer Review der TI (eingebettete Gutachten) | https://www.wolframphysics.org/peer-review/a-class-of-models-with-the-potential-to-represent-fundamental-physics/ | 14:29:33 |
| A44 | Q&A computation-theory | https://www.wolframphysics.org/questions/computation-theory | 14:29:34 |
| A45 | Aaronson, S. (2002): Book Review on A New Kind of Science, QIC; arXiv:quant-ph/0206089v2 | https://arxiv.org/pdf/quant-ph/0206089 | 14:31:14 |
| A46 | Lamb, A.: Should You Take Wolfram's Physics Seriously? (Medium) | https://medium.com/swlh/should-you-take-wolframs-physics-seriously-2645e6f4d718 | 14:31:37 (403, kein Inhalt) |
| A47 | arXiv-API, Fenster 2024-10-04 bis 2026-10-04 (1 Treffer: Duendar, Arsiwalla, Elshatlawy 2025, arXiv:2512.20587) | http://export.arxiv.org/api/query (Abfrage im ARBEITSFELD) | 14:31:47 |
| A48 | Working Materials Archive 2026 | https://www.wolframphysics.org/archives/index?i=2026 | 14:30:53 |
| A49 | arXiv-API, neueste 60 (31 Treffer; u. a. Leuenberger 2021, arXiv:2110.03388; Rodriguez Caballero 2021, arXiv:2108.03751; Gorard 2023, arXiv:2303.07282; Gorard/Dannemann-Freitag 2023, arXiv:2301.12455) | http://export.arxiv.org/api/query (Abfrage im ARBEITSFELD) | 14:32:03 |
| A50 | Wolfram, S. (2026): What Ultimately Is There? Metaphysics and the Ruliad | https://writings.stephenwolfram.com/2026/02/what-ultimately-is-there-metaphysics-and-the-ruliad/ | 14:33:00 |
| A51 | Complex Systems (Zeitschrift), Startseite | https://www.complex-systems.com/ | 14:34:06 |
| A52 | Wolfram Physics Project Functions, Guide (Wolfram Cloud) | https://www.wolframcloud.com/obj/wolframphysics/Tools/guide-page | 14:34:07 |
| A53 | Piskunov, M. (2020): Confluence and Causal Invariance (Bulletin) | https://www.wolframphysics.org/bulletins/2020/11/confluence-and-causal-invariance/ | 14:37:21 (404) |
| A54 | Wolfram, S. (2020): Faster than Light in Our Model of Physics: Some Preliminary Thoughts | https://writings.stephenwolfram.com/2020/10/faster-than-light-in-our-model-of-physics-some-preliminary-thoughts/ | 14:37:22 |
| A55 | dasselbe Bulletin, Subdomain | https://bulletins.wolframphysics.org/2020/11/confluence-and-causal-invariance/ | 14:37:41 (Host unbekannt) |
| A56 | Wolfram, S. (2020): Finally We May Have a Path to the Fundamental Theory of Physics... and It's Beautiful | https://writings.stephenwolfram.com/2020/04/finally-we-may-have-a-path-to-the-fundamental-theory-of-physics-and-its-beautiful/ | 14:38:01 |
| Projekt | Surya, S. (2019): The causal set approach to quantum gravity (lokale Kopie, S. 31-32) | RUNDE-22/geometrie-stand/hilfs/surya-1903.11544.txt | kein Abruf |

## 14. Einfach gesagt

Wolframs Projekt baut die Welt aus einem Netz, das nach einer einfachen Regel immer weiter waechst. Einen eigenen
"Modell-Explorer" gibt es auf der Seite nicht, sondern eine Sammlung von Regeln mit fertigen Bildern, die man nur mit
Wolframs eigener Software weiterrechnen kann. Dass aus solchen Netzen Relativitaet und Schwerkraft folgen, ist unter
vielen Annahmen hergeleitet, aber keine Vorhersage ist bestaetigt, und weder halbzahliger Spin noch ein Netz mit drei
Raumrichtungen ist gefunden. Fuer uns zaehlt vor allem: Diese Netze haben im Kleinen feste Nachbarn und damit ein
verstecktes Ruhesystem; ob das im Grossen verschwindet, koennen wir mit einer kleinen Rechnung (K1) pruefen.
