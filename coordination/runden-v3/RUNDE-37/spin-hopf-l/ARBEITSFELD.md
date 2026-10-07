# ARBEITSFELD SPIN-HOPF-L (feldforscher, Runde 37)

- Start: 2026-10-04 04:20:01 CEST (date). Zeitbox 75 min, also Ende spaetestens 05:35 CEST.
- Arbeitsdatei nach Feld-Regel 5: Ich lese sie vor jedem Schritt neu. Gestrichenes wird markiert, nicht geloescht.
  Offene Rueckfragen stehen unten und wandern mit.
- Kennzeichen: [S] an der Quelle gelesen, [L] Gedaechtnis, [L?] unsicher, [H] Hypothese, **[ES]** eigener Schluss.
- Abrufbudget: hoechstens 15 WebFetch, keine WebSearch.

## 0. Gelesen vor dem ersten Abruf (lokal)

- KARTE.md (Fragen 1-5, E1-E5, Bedeutung): gelesen 04:20.
- SPIN-KONSTRUKTION-codex.md, vollstaendig (Z. 1-1003): gelesen 04:20.
  Kern: B.5, also X = C x S^2, phi in C, n in S^2, b(n) = (v/2)(n1 + i n2), s = |phi|^2 + |b|^2,
  Potential U(s) - gJ Re[(phi^* b)^2] + mu^2 v^2 (1 - n3), Faddeev-Term kappa H^2.
  - Gemeinsame U(1): phi -> e^{i a} phi und (n1 + i n2) -> e^{i a}(n1 + i n2), Vakuum Nordpol fest.
  - Bei g = 0 zwei getrennt erhaltene Ladungen.
  - Offen ist die Bindung (Abschnitt 5: D = (E_sep - E_mix)/E_sep).
  - FR-Paritaetsregel: q/hbar in Z + h/2 (nach Krusch-Speight Gl. 4.5).
- Memory project-spin-halb-nicht-moeglich.md: gelesen 04:20.

## 1. Gegensweep vorgezogen: Hat das Projekt die Bindungsfrage schon angefasst?

Die Karte nennt keine Projektvorarbeit, das ist auffaellig. Ein grep nach Hopf/Q-lump/isospinning
(ohne gesperrte Pfade) fand:
- coordination/literatur-20260924/CXS2-TORE-astra-20260924.md (astra, Paket X2b: Schranken und Eintrittsbedingungen fuer
  die Bindung B.5, ohne Rechnung)
- coordination/resonance-20260930/qball-hopf-{pilot,3d,radial-relax,localmode,breathing,phase-radiation,angular-check}
  und hopf-charge-window: Hier sind offenbar Q-Ball-Hopf-Laeufe gerechnet worden!
- coordination/runden-v3/RUNDE-10/hopf1/ (hopf1.py, Laeufe)
-> PRUEFEN, bevor ich eine Rechenkarte vorschlage (sonst schlage ich Gerechnetes erneut vor).

### 1a. Befund aus den Projektdateien (gelesen 04:21-04:25, lokal, nur Text)

- **CXS2-TORE-astra-20260924.md** (astra, 24.09.):
  - Kopfzeile: Schranken entscheiden die Bindung nicht.
  - Hat Harland/Jaeykkae/Shnir/Speight arXiv:1301.2923 (Abschnitt 2, 3.2), Krusch/Speight hep-th/0503067 (4.5), (5.1)-(5.2),
    Ward hep-th/9811176 und Hirayama hep-th/0602192 gelesen [S bei astra].
  - VK-Schranke E_FH >= 2^(5/2) 3^(3/8) pi^2 v sqrt(kappa) |h|^(3/4).
  - Festladungsreduktion: E_q = V + q^2/(2 Lambda).
  - Alter Q-Ball am Nordpol ist transversal (in n-Richtung) strikt positiv. Um den reinen Hopftraeger ist der phi-Kanal
    positiv, falls omega^2 < 11/32.
  - Literaturtabelle Abschnitt 7: Die Zusammenstellung B.5 ist "eigene Konstruktion", es gab keine systematische
    Prioritaetssuche.
- **qball-hopf-pilot** (30.09., OpenAI ag-phy-coordination, TS440-CPU):
  - Feste Trialprofile, nicht relaxiert. Die Kreuzidentitaet U(x+y) - U(x) - U(y) = xy[-2 + 1,5(x+y)] ist < 0 fuer
    x + y < 4/3, das Vorzeichen also vorab ableitbar.
  - Mit freier Ladungsaufteilung (q = 189,14, gemeinsame Rotation) liegt der ueberlagerte Zustand 0,963 % unter der
    getrennten Familienreferenz; Omega ~ 0,577.
  - Nur ein Variationswert, keine Bindung bewiesen. Der zentrierte Paarterm ist ~0 (axiale Auswahlregel).
- **qball-hopf-3d** (30.09.):
  - Der geladene Hopftraeger (phi = 0, q = 189, Omega ~ 0,984) zeigt einen lokalen Hyperbolizitaetsverlust
    (chi ~ 1,09 > 1, speed^2 ~ -0,094).
  - Deshalb KEIN Zeitschritt, keine 3D-Dynamik.
  - ROTATIONSGRENZE.txt: Harland et al. 1301.2923 nennen zwei Grenzen, (i) den Verlust der positiven Zielmetrik der
    Pseudoenergie und (ii) die Strahlungsschwelle. In B.5-Normierung kippt (i) bei Omega^2 > 1/2.
- **hopf-charge-window** (30.09.): Bei sigma = 0,25 und q0/4 gibt es einen radial stationaeren Kandidaten mit Omega = 0,402
  < 0,707, Paargate PASS. Bei q0/2 ist Omega = 0,7106 knapp ueber der Schwelle, Gate FAIL. Keine Zeitentwicklung.
- **source-audit/SPIN-HALB-ANSCHLUESSE.txt** (30.09.): Krusch/Speight v2 Einleitung, Paragraf 3 und 4 gelesen
  [S bei Codex/OpenAI].
  - Ungerade Hopf-Ladung erlaubt die FR-Fermion-Wahl.
  - Ein HTML-Satz in Paragraf 4 hat eine verdrehte Paritaetsformulierung; darauf nichts gruenden.

**[ES] Folge fuer diese Karte:**
- Die Karte (04:18) nennt diese Vorarbeit nicht. Frage 1 (isospinning) ist in der Projektlage schon teilweise
  beantwortet (1301.2923 gelesen).
- Frage 4 ist durch Pilot und 3D-Befund schon numerisch angefasst: Variationsvorteil ~1 %, aber ein Dynamikverbot oberhalb
  Omega^2 ~ 1/2.
- Die Rechenkarte muss daran anschliessen, nicht neu anfangen.

### 1b. [ES] Spannung, die beim Lesen auffiel (vor jedem Abruf notiert, 04:25)

- Das Q-Ball-Fenster des alten Potentials ist 1/2 < omega^2 < 1, also omega in (0,7071; 1).
- Die hinreichende Hyperbolizitaetsbedingung fuer die starr isorotierende Faddeev-Textur in B.5 ist Omega^2 < 2 sigma = 1/2.
- Damit sind beide Fenster **disjunkt**. Ein gemeinsam rotierender Verbund (bei g != 0 erzwingt die Phasenkopplung eine
  gemeinsame Frequenz) kann nicht zugleich im freien Q-Ball-Fenster und im sicheren Texturfenster liegen.
- Moeglicher Ausweg: phi ist als gebundene Mode im anziehenden Topf der Textur gefangen. Das effektive Massenquadrat ist
  U'(y) - G y >= 11/32 (astra S3), also ist omega^2 < 1/2 fuer den gefangenen phi-Anteil moeglich. Der Pilot fand
  Omega ~ 0,577, also Omega^2 ~ 0,333 < 0,5, das passt.
- In 2D hat jeder netto anziehende Topf mindestens einen gebundenen Zustand [L: Simon 1976], in 3D nicht zwingend.
  -> Pruefgroesse fuer die Rechenkarte: Liegt omega_0^2 der gefangenen Mode unter 1/2?

## 2. Abrufliste (URL, Zeit per date, Erwartung vorher, Ergebnis)

| Nr | Zeit | URL | Erwartung vorher (1 Satz) | Ergebnis | Verstoss? |
|---|---|---|---|---|---|
| A1 | 04:26 (Erw. vorher) / abgerufen 04:26 | arxiv.org/abs/1301.6803 | [L?] ID = Battye/Haberichter "Classically isospinning Hopf solitons": Ladungen ~1-7 im massiven FS-Modell numerisch, Existenz bis Massenschwelle omega -> m, bei hohem omega Formwechsel | [S] ID stimmt. Battye/Haberichter, PRD 87, 105003 (2013). Volle 3D-Relaxation, Hopf-Ladung bis 8, SF-Modell "with mass terms". Symmetriebruch zugelassen; "transmutations", neue Loesungstypen, Umordnung des Minimalspektrums; der Typ des niedrigsten Solitons kann wechseln. Zur Hoechstfrequenz sagt das Abstract nichts. | Teilweise: Formwechsel wie erwartet, aber staerker (Typwechsel des Grundzustands); Frequenzgrenze offen |
| A2 | 04:26 / 04:26 | arxiv.org/abs/1301.2923 | Harland et al. "Isospinning hopfions": E(Q,N)-Kurven, Existenz bis Schwelle, zwei Grenzen (Metrikverlust, Strahlung) wie im Projekt schon gelesen; dazu Abstract-Formulierung | [S] Harland/Jaeykkae/Shnir/Speight, J. Phys. A 46 (2013) 225402. Pseudoenergie bei festem omega, Gradientenabstieg ohne Symmetrieannahme. "generically, the shape of a soliton is independent of omega", die Groesse waechst monoton mit omega. Ein elastisches Stabmodell mit einem Parameter erklaert das meiste. | **JA, Verstoss gegen A1/A2 zusammen:** Zwei Gruppen, gleiches Jahr, gleiches Modell: "Form unabhaengig von omega" gegen "Grundzustandstyp wechselt" -> Regel 1 (zwei Regime) |
| A4 | 04:28 / 04:28 (Text-Abruf scheiterte, PDF lokal gespeichert, S. 1-11, 17-19 per Read gelesen 04:28-04:29) | arxiv.org/pdf/1301.6803 | BH-Volltext: Potential m^2(1-n3) (ggf. zweites), omega < m als Existenzgrenze; Groesse divergiert bei omega -> m; Stellungnahme zu Harland: Unterschied durch Massenwert/Potential oder durch Ladungen mit fast entarteten Typen | [S] Gl. (2): V_I = 2 mu^2(1-phi3), V_II = mu^2(1-phi3^2); mu = 1. Gitter (201)^3, dx = 0,1, Differenzen 4. Ordnung. Feste Isospinladung K, omega = K/U33 (Gl. 9, 10). S. 11: "for mu <= 1 there exists a maximal frequency omega_max = mu"; jenseits davon keine stabile Loesung (lineare Stabilitaetsanalyse). Fuer **N = 1-3 bleibt der Typ**, nur die Groesse waechst; E und U33 divergieren bei omega = mu. Ab N = 4 Umformungen (4A22 -> Link ab omega >= 0,60). "Note added" S. 18: Harland et al. rechneten meist mit **mu = 2 und V_II**; Unterschiede "could be due to the different potential choice or ... mu". S. 17: Beide Quantisierungen (bosonisch, FR) setzen voraus, dass Zentrifugaleffekte die Symmetrien nicht brechen. S. 5-6: Der axiale Typ A_{n,m} ist ein Baby-Skyrmion mit Windung m, entlang eines Rings eingebettet, Phase 2 pi n verdreht. | **Erwartung zu omega_max bestaetigt.** Moderator fuer V1 an der Quelle benannt (s. V1). Neu: B.5 liegt im Regime "Metrikverlust vor Strahlung" (s. V2) |
| A5 | 04:28 / 04:28 | arxiv.org/abs/0804.1357 | [L?] Radu/Volkov Review "Stationary ring solitons in field theory - knots and vortons": Knoten (FS) und Vortonen (geladene, stromtragende Ringe im U(1)xU(1)-Modell), Existenz numerisch, Stabilitaet der Vortonen offen | [S] Phys. Rep. 468 (2008) 101-151. Statische Knoten, "attempts to gauge them", Bedingungen gegen Abstrahlung rotierender Loesungen, spinning Q-balls "twisted and gauged", spinning skyrmions, erste explizite globale Vortonen (elliptisches RWP, nicht abstrahlend). | nein (bestaetigt; Stabilitaet im Abstract nicht behandelt) |
| A6 | 04:28 / 04:28 | arxiv.org/abs/1303.3044 | [L?] Garaud/Radu/Volkov "Stable cosmic vortons": Vortonen im globalen Witten-Modell, dynamisch stabil in einem Parameterbereich -> Vorbild "Noether-Ladung bleibt an topologischem Ring" | [S] PRL 111, 171602 (2013). **Geeichtes** U(1)xU(1)-Modell (nicht global). Die meisten Vortonen sind instabil und zerfallen; nur "thick vortons with small radius" behalten ihre Form in der nichtlinearen 3+1-Entwicklung. | **teilweise Verstoss:** Erwartet war ein Stabilitaetsbereich, gefunden: Stabilitaet ist die Ausnahme (Ecke dick und klein); Modell geeicht |
| A7 | 04:28 / 04:28 | arxiv.org/abs/cond-mat/0106152 | [L?] Babaev/Faddeev/Niemi: geladenes Zweikomponenten-Kondensat -> Einheitsvektor n plus Dichte plus Strom; Knotensolitonen behauptet (Faddeev-artige Zerlegung von C^2) | [S] PRB 65, 100512 (2002). Zweikomponenten-GL/GP, abgebildet auf eine Version des O(3)-Sigma-Modells; "hidden O(3) symmetry", "allows for the formation of stable knotted solitons" (Behauptung, MgB2). | nein (bestaetigt). [L?] Spaetere Gegenarbeit (Jaeykkae/Speight ~2010, "supercurrent coupling destabilizes knot solitons") noch nicht geprueft |
| A11 | 04:33 / 04:33 | arxiv.org/abs/0812.1493 | [L?, ID unsicher] Speight "Supercurrent coupling in the Faddeev-Skyrme model": Kopplung der Textur an ein Einform-Feld (Superstrom) wie im BFN-Modell zerstoert die Stabilitaet (Skyrmionen/Knoten koennen schrumpfen oder sind nicht mehr stabil) | [S] ID stimmt. J. Geom. Phys. 60 (2010) 599. Die Superstrom-Kopplung "destroys the topological stability"; "no globally stable knot solitons"; lokale Minimierer moeglich. Das gekoppelte Einheits-Hopfion auf S^3 ist "unstable for all R". Das stellt die BFN-Vermutung in Frage. | nein (bestaetigt; zugleich Gegenbeispiel zu A7) |
| A12 | 04:33 / 04:33 | arxiv.org/abs/1404.4867 | [L?, ID unsicher] Shnir/Zhilin "Gauged hopfions": FS-Modell mit U(1)-Eichung der Isorotation; elektrisch geladene, isorotierende Hopfionen existieren in einem Bereich; Ladung haengt am Knoten (gleiches Feld) | [S] ID stimmt. PRD 89, 105010 (2014). U(1)-geeichtes FS + Maxwell. **Statische** axiale Loesungen mit nicht ganzzahligem toroidalem Magnetfluss, **leichter** als die ungeeichten A11/A21 und mit wachsender Kopplung leichter; bei starker Kopplung zwei quantisierte Fluesse. Die untere topologische Schranke sei neu zu ueberdenken. | **teilweise Verstoss:** nicht elektrisch geladen und isorotierend, sondern statisch magnetisch; Eichkopplung senkt die Masse und greift die Schranke an |
| A13 | 04:34 / 04:34 | arxiv.org/html/1301.2923 | Harland et al. Volltext: Potential V_II mit mu = 2 (laut BH); beide Grenzen (Metrikverlust bei omega = 1 in ihrer Normierung, Strahlung bei omega = mu); bei mu = 2 also omega_max = 1; Q-Lumps (Leese) als 2D-Vorbild zitiert | [S, ueber WebFetch-Auszug, nicht als Bild gelesen] Gl. 1.1: (1/2) d phi.d phi - (1/4)(d phi x d phi)^2 - Potential vom Typ mu^2(1-phi3^2); Gl. 2.10 wurde als "(1-psi3^2)^2" wiedergegeben, das ist **verdaechtig, nicht verwenden**. Paragraf 2: zwei Grenzen, omega1 = 1 (Radius der Zielsphaere) und omega2 = mu (Mesonmasse); F_omega ist "no longer bounded below for omega > omega1 = 1". Meist mu = 2, groesstes untersuchtes omega = 1. Paragraf 3.2 (unendliche Strings): Maximum "around 1.4", also ueber 1. Gl. 5.1 (Stabmodell): E = E0/sqrt(1 - (omega/omega*)^2), E^2 = E0^2 + (A/C) J^2; bei grossem J wachsen E, Traegheit und Groesse linear in J, omega -> konstant. Paragraf 2: "conservation of T+V-omega J does not directly imply that saddle points of F_omega are unstable". **Q-Balls und Q-Lumps werden nicht erwaehnt.** | Teilverstoss: kein Leese-Zitat (Q-Lump-Erwartung falsch). Sonst Bestaetigung von V2/V3 an der Quelle, mit Zusatz: Loesungen gibt es auch jenseits der hinreichenden Schwelle (Strings bis ~1,4) |
| A14 (Gegensweep) | 04:35 / 04:36 | arxiv.org/html/hep-th/0503067 | Gl. (4.5) und Umgebung: Bei ungeradem Q sind 2pi-Raumdrehung und 2pi-Isodrehung beide nicht zusammenziehbar. Fermionische Wahl ergibt halbzahligen Spin UND halbzahlige Isospin-Eigenwerte der U(1) (Codex: q in Z + h/2). Bei geradem Q ganzzahlig. | [S, WebFetch-Auszug] Spin: "L and J are half integer if and only if Q is odd". Isospin: "K3 and I3 are also half integer if and only if Q is odd". Gl. (4.5): N = Q/(2pi)(Q alpha - beta), gerade oder ungerade. Warnung: Im Modulraum M ist die 2pi-Schleife "noncontractible of order 2, independent of n (and Q)". Daher "we must thus choose bosonic quantization for Q even, it is not imposed on us by the topology of M". **Nicht uebernommen:** Die Deutung des Auszugs, Fermion sei bei ungeradem Q "erzwungen", und "mit Potentialterm" (das ist der Stabilisierungsterm). Beides widerspricht dem Projekt-Audit und Giulini. | nein (Codex-Regel q in Z + h/2 an der Quelle bestaetigt) |
| A8 | 04:31 / 04:31 | arxiv.org/abs/1309.3907 | [L?] Battye/Haberichter "Isospinning baby Skyrmion solutions": 2+1, B = 1 bis ~6, altes und neues Baby-Skyrme-Modell; Existenz bis omega -> mu; bei hohem omega Zerfall in Bestandteile bei B >= 2; Gitter ~ 200^2 bis 500^2 | [S] ID stimmt, PRD 88, 125016 (2013). Volle 2D-Relaxation mit Pionmassen-Analogon. Stabile Loesungen "for all angular frequencies omega <= min(mu,1)". Ladung-B-Loesungen zerfallen ab einer kritischen Frequenz in B Einerbausteine; bei grossem mu bricht B = 2 die Rotationssymmetrie. Gitter im Abstract nicht genannt. | **Bestaetigt, mit Zugewinn:** min(mu,1) bestaetigt V2 an der Quelle (die "1" ist die Metrikschwelle) |
| A9 | 04:31 / 04:31 | arxiv.org/abs/1010.2217 | [L?, ID unsicher] Jaeykkae/Speight "Supercurrent coupling destabilizes knot solitons": Kopplung der S^2-Textur an Dichte/Strom des Zweikomponentenmodells laesst Knoten schrumpfen bzw. zerfallen -> Gegenbeispiel zu "Kopplung haelt" | [S] **Falsche Zuordnung:** 1010.2217 ist Jaeykkae/Speight "Easy plane baby skyrmions", PRD 82, 125030 (2010). Potential (1/2) phi3^2, Einerskyrmion = gebundener Zustand zweier Halb-Lumps; Minimierer B = 1-14, 18, 32. | **JA, Verstoss gegen mein Gedaechtnis:** Die Journalangabe "PRD 82, 125030", die ich der Supercurrent-Arbeit zuschrieb, gehoert zu dieser Arbeit. Supercurrent-Behauptung bleibt [L?] |
| A10 | 04:31 / 04:31 | arxiv.org/abs/1304.6021 | [L?, ID unsicher] Kobayashi/Nitta "Torus knots as Hopfions": Hopfion als verdrehter Wirbelring (Baby-Skyrmion-Schlauch mit U(1)-Modul-Windung) im FS-Modell mit Potential -> Bruecke Hopfion <-> Vorton | [S] ID stimmt, PLB 728 (2014) 314. Erweitertes FS-Modell mit ferromagnetischem Potential. (P,Q)-Torusknoten aus abs(Q) Sine-Gordon-Kinkstrings, verdreht entlang toroidaler Domaenenwaende; Hopf-Ladung PQ. | teilweise (Konstruktion ueber Domaenenwand-Kinks, nicht ueber Wirbelring mit Modul; fuer die Bindungsfrage nur am Rand) |
| A3 | 04:26 / 04:26 | arxiv.org/abs/hep-th/0503067 | Krusch/Speight: "Hopf-Solitonen fermionisch quantisierbar, wenn Hopf-Ladung ungerade"; Grundzustaende bis Q ~ 7 | [S] CMP 264 (2006) 391. "Hopf solitons can be quantized as fermions if their Hopf charge is odd." Grundzustaende bis Q = 7. | nein (bestaetigt, eine Zeile) |

## 3. Erwartungen E1-E5 (aus KARTE, unveraendert) und laufender Stand

| Nr | Erwartung | Wahrsch. | Stand |
|---|---|---|---|
| E1 | Drehende Hopf-Solitonen numerisch gerechnet; Existenz bis zu einer groessten Drehfrequenz | 65 % | **eingetroffen**, praezisiert (04:42): Die Grenze ist min(Masse, Metrikschwelle), nicht immer die Masse (A4, A8, A13) |
| E2 | FR-fermionisch fuer manche Hopf-Ladungen erlaubt, fuer andere nicht | 60 % | **eingetroffen** (A3, A14): ungerade ja, gerade nein; Isospin ebenfalls halbzahlig genau bei ungerade |
| E3 | Gebundene Zustaende S^2-Textur + komplexer Skalar (Q-Lumps o.ae.) mit stabiler Bindung | 55 % | **teilweise**: Ladung im selben Feld ja (A1, A2, A8); Ladung eines zweiten Felds an einem topologischen Ring nur Vortonen, meist instabil (A6); Textur plus Zusatzfeld kann die Topologie zerstoeren (A11). Den Kernfall Q-Ball plus S^2-Textur in dieser Stichprobe nicht gefunden |
| E4 | Fuer genau Codex' Kopplung keine Literatur | 70 % | **nicht pruefbar** (keine Suche erlaubt, Regel 7). Indiz dafuer: 14 Abrufe ohne Treffer; astra: keine Prioritaetssuche |
| E5 [H] | 2+1-Gegenstueck in <= 10 min je Lauf rechenbar | 50 % | **teilweise / plausibel, nicht gemessen**: BH rechnen 2D voll (A8); radiale Reduktion in Sekunden (Projektanalogie); 2D-Zeitlauf grenzwertig |

## 4. Erwartungsverstoesse (protokolliert, das eigentliche Ergebnis)

- **V1 (04:26, A1+A2):**
  - Erwartet war: Isospin vergroessert die Hopf-Solitonen bis zur Schwelle, sonst Form wie statisch, mit Formwechsel
    hoechstens nahe der Schwelle.
  - Gefunden: Harland et al. sagen "Form generisch unabhaengig von omega, Groesse waechst". Battye/Haberichter sagen "Typ
    des Grundzustands kann wechseln, Transmutationen".
  - Nach Regel 1 zuerst die Moderatoren-Hypothese [H]:
    - (a) **Fast-Entartung des statischen Spektrums je Ladung.** BH betonen "often of similar energy". Wo zwei statische
      Typen fast gleich liegen, ordnet Isospin um; sonst bleibt die Form.
    - (b) **Kontrollgroesse.** Festes omega (Pseudoenergie, Harland) gegen feste Isospinladung J.
    - (c) **Massenterm und Massenwert.**
    - (d) **Abstand zur Schwelle.**
  - Korrigierte Erwartung: "Gestalt bleibt" gilt nur fuer Ladungen mit klar getrenntem statischem Grundzustand. Fuer
    unseren Verbund heisst das: Ladung kann die Topologie-Gestalt umordnen. Q = 1 ist vermutlich im Regime "Form bleibt"
    (Hopfion-Ring ohne Konkurrenten) [H].
  - -> Volltext BH pruefen (A4): Potential, omega-Bereich, Stellung zu Harland.
  - **Aufloesung (04:29, A4 [S]):** Zwei Regime bestaetigt, mit an der Quelle benannten Moderatoren:
    - (1) Hopf-Ladung N: N = 1-3 behalten den Typ, ab N = 4 Umordnung. Das deckt sich mit Harlands "generically".
    - (2) Potential und Massenwert: BH rechnen mu = 1 mit V_I, Harland meist mu = 2 mit V_II. BH nennen das selbst als
      moegliche Ursache der Unterschiede.
    - Fuer h = 1 (unser Fall) liegt "Form bleibt" vor, an zwei Quellen.
- **V2 (04:29, A4 plus Projekt-ROTATIONSGRENZE, [ES]):**
  - Erwartet (E1) war eine Grenze "wie beim Q-Ball", also omega -> Masse. BH bestaetigen omega_max = mu, aber nur fuer
    mu <= 1.
  - In BH-Normierung kippt die Pseudoenergie-Metrik bei omega = 1 (Sigma-Term |grad phi|^2 gegen omega^2 |grad phi3|^2 aus
    dem Skyrme-Term) [ES-Rechnung aus Gl. 1].
  - B.5 (v = mu = kappa = 1) hat die n-Masse sqrt(3) (Projekt: Nordpolmasse^2 = 3) und die Metrikschwelle 1/sqrt(2).
    Das Verhaeltnis Masse/Metrikschwelle ist sqrt(6) ~ 2,45, entspricht also BH-mu ~ 2,45.
  - Damit liegt B.5 im Regime, in dem **der Metrikverlust vor der Strahlung kommt**: naeher an Harland (mu = 2) als an BH
    (mu = 1).
  - Folge: Fuer B.5 ist die relevante Frequenzgrenze 1/sqrt(2), nicht die Masse. Das passt zum Projektbefund chi > 1 bei
    Omega ~ 0,98.
  - **Bestaetigt an der Quelle (04:31, A8 [S]):** Baby-Skyrmionen in 2+1 sind stabil fuer omega <= min(mu,1). Die "1" ist
    genau die Metrikschwelle.
  - Allgemein [ES]: omega_max = min(Masse, sqrt(sigma/kappa_eff)). In B.5 ist das Omega^2 < v^2/(2 kappa).
  - **Hebel:** Ein kleineres kappa oder ein groesseres v verschiebt die Metrikschwelle nach oben. Das Projekt hat den
    Hebel am 30.09. schon angefasst (hopf-charge-window, sigma 0,25 gegen 0,5).
- **V3 (04:31, [ES], aus V2 und Projekt):**
  - Bei v = mu = kappa = 1 sind das freie Q-Ball-Fenster 1/2 < omega^2 < 1 und das sichere Texturfenster Omega^2 < 1/2
    **disjunkt**. Die Grenze liegt bei beiden genau bei 1/2, eine Parameterkoinzidenz:
    - Q-Ball-Kante min U(S)/S = 1/2 bei S = 1;
    - Texturkante v^2/(2 kappa) = 1/2.
  - Ein gemeinsam rotierender Verbund (g != 0) kann daher nur existieren, wenn
    - (i) phi als gefangene Mode unter dem Q-Ball-Fenster sitzt (omega^2 < 1/2; der Pilot fand Omega ~ 0,577), oder
    - (ii) die Textur jenseits der hinreichenden Schwelle trotzdem hyperbolisch bleibt (hopf-charge-window: q0/2 hat chi
      < 1 trotz Omega^2 > 1/2).
  - Der Unterscheidungspunkt zwischen (i) und (ii) ist Omega^2 des Verbunds relativ zu 1/2.
- **V4 (04:33, A11 + A12 [S], gegen meine stille Annahme "Kopplung stoert die Topologie nicht"):**
  - Speight 2010: Die Superstrom-Kopplung zerstoert die topologische Stabilitaet, global stabile Knoten gibt es nicht.
  - Shnir/Zhilin 2014: Die Eichkopplung macht Hopfionen leichter, die untere Schranke ist neu zu ueberdenken.
  - Zwei Regime mit dem Moderator **Kopplungsart** [ES]:
    - Ableitungs- bzw. Vektorkopplung an H_ij greift die VK-Schranke an.
    - Reine Potentialkopplung (B.5) laesst sie stehen: Mit V >= c s >= 0 (Codex B.5, astra) und unveraendertem
      sigma- plus kappa-Term gilt weiter E >= E_FH >= VK |h|^(3/4) [ES aus Projekt-Herleitung].
  - Folge: In B.5 haengt nicht der Knoten an der Kopplung, sondern nur die Ladung. Wird B.5 spaeter um
    Ableitungskopplungen erweitert (z.B. Strom-Strom), faellt diese Sicherheit weg.
- **V5 (04:34, A13 [S]):** Harland et al. zitieren Q-Lumps nicht. Leese bleibt [L]. Zugleich zeigt E(J) bei grossem J
  einen linearen Anstieg mit festem omega, also Q-Ball-artiges Verhalten (E/J -> omega*).
  - [ES] Damit ist die Ladungsverteilung im Zerfallskanal ein Wettbewerb der **Grenzkosten dE/dq**: Q-Ball mit
    E/Q -> 1/sqrt(2) (duennwandig) gegen isorotierenden Hopftraeger mit omega*.
  - Im Gleichgewicht sind beide Omega gleich (Pilot: Omega ~ 0,58, q_phi ~ 123, q_H ~ 66).
- **Kopplungs-/Taktgroesse nach Regel 6 [ES]:**
  - Es gibt drei Wege, wie die Ladung am Knoten Energie spart: Dichtekopplung U(x+y), Paartransfer g und
    Faddeev-Traegheit. Gemeinsame Groesse ist die gemeinsame Frequenz Omega = dE/dq, also das chemische Potential
    der Ladung.
  - Ihre Lage relativ zu drei Schwellen entscheidet:
    - 1/sqrt(2): Q-Ball-Unterkante und zugleich Texturkoerzivitaet bei v = kappa = 1;
    - 1: phi-Masse;
    - sqrt(3): n-Masse.

## 4a. Gegensweep (Regel 4), 04:37

Frage: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

- **GS1 (geprueft, groesster Befund):** "Die Karte steht am Anfang der Bindungsfrage." Falsch.
  - Seit 24./30.09. gibt es astra-Tore, einen 3D-Variationspiloten mit fairer Ladungsteilung (0,96 %), einen
    Hyperbolizitaetsverlust des geladenen Hopftraegers bei Omega ~ 0,98 und einen Ladungsfenster-Lauf.
  - Die Karte zitiert nichts davon. Die Rechenkarte muss an diese Laeufe anschliessen.
- **GS2 (geprueft, A14):** "Die Codex-Regel q in Z + h/2 stimmt." An der Quelle bestaetigt.
  - [ES] Folge: Im fermionischen Zweig traegt der h = 1-Knoten immer eine halbzahlige Restladung. Eine vollstaendige
    Abloesung der Ladung ist quantenmechanisch ausgeschlossen, mindestens 1/2 bleibt.
  - Klassisch ist das bei q ~ 100 bedeutungslos.
- **GS3 (geprueft am Projekttext):** "Die Kopplung laesst die Topologie in Ruhe."
  - Gilt fuer B.5, weil V >= c s >= 0 (Codex, astra) und der sigma- und kappa-Term unveraendert bleiben.
  - Gilt NICHT fuer Ableitungskopplungen (Speight 2010, A11).
- **GS4 (nicht geprueft, [L]):** "In 2D hat jeder netto anziehende Topf einen gebundenen Zustand" (Simon 1976).
  - Wenn das stimmt, ist die Existenz der gefangenen Mode in 2D vorab ableitbar. Die Rechenkarte darf sie dann nicht als
    Vorhersage fuehren, nur ihre Frequenz.
- **GS5 (nicht geprueft, [L]):** "Der Hopf-Term in 2+1 aendert die klassischen Gleichungen nicht" (Wilczek/Zee 1983).
  - Folge: Das 2D-Gegenstueck prueft nur die Bindung, nicht den Spin. Der Spin waere dort ein frei gewaehltes theta.
- **GS6 (teilweise geprueft):** "WebFetch-Auszuege sind woertlich."
  - A13 und A14 kamen ueber ein Zusammenfassungsmodell. Mindestens zwei Deutungen waren schief (Gl. 2.10 bei Harland;
    "forced" bei Krusch/Speight).
  - Nur A4 (BH) habe ich als Seitenbild selbst gelesen.
  - Abstracts A1-A3, A5-A12 sind Abstract-Wortlaut laut Auszug.
- **GS7 (Regelkonflikt):** Regel 7 verlangt vor jedem Negativurteil eine 24-Monats-Websuche. Die Websuche war vom
  Auftraggeber gesperrt. Daher gibt es kein "widerlegt" und kein "gibt es nicht", nur "in dieser Stichprobe nicht gefunden".

## 4b. Kalibrierung, laufend

- **(a) Gemessen** (Literatur oder Projektlauf):
  - omega_max = min(mu, 1) fuer Baby-Skyrmionen; omega_max = mu fuer Hopf-Solitonen bei mu <= 1.
  - Typerhalt fuer N = 1-3.
  - Projektpilot 0,96 % (nur Variationswerte); chi ~ 1,09 bei Omega ~ 0,98.
  - Superstrom-Kopplung zerstoert die Stabilitaet.
- **(b) Verdichtet [ES]:**
  - Taktgroesse Omega = dE/dq mit drei Schwellen.
  - Disjunkte Fenster bei v = kappa = 1.
  - Kopplungsart als Moderator der Topologie-Sicherheit.
- **(c) Gewachsene Gewissheit ohne neue Evidenz:**
  - Mein Eindruck "Bindung wahrscheinlich" kommt vor allem aus dem negativen Kreuzterm. Der ist aber vorab ableitbar
    und belegt keine Bindung relaxierter Zustaende. **Warnzeichen:** Die Sicherheit stieg, waehrend die Frage feiner
    wurde (Fenster, Hyperbolizitaet).

## 5. Offene Rueckfragen (wandern mit)

- ~~R1: Was haben die resonance-20260930/qball-hopf-*-Laeufe ergeben? Liegt die Bindungsfrage dort schon (teilweise)
  vor?~~
  - Beantwortet 04:25 (Abschnitt 1a): teilweise ja, als Variationspilot und Dynamik-Sperre.
- ~~R2: Welche Konvention meint Codex mit "h ungerade -> FR-Minus moeglich"?~~
  - Beantwortet (A3, A14): nur ungerade h; bei geradem h ist die Raumdrehschleife zusammenziehbar.
- ~~R3 (neu, offen): Hat das Projekt die 2D-Variante (Baby-Skyrmion plus phi) je gerechnet?~~
  - Beantwortet 04:39: **Nein**, das echte 2+1-Gegenstueck ist nirgends gerechnet. Aber es gibt mehr Vorarbeit als gedacht:
    - **RUNDE-03/tests2d-r3/KNOTEN-PAPIER.md** (30.09., Opus 5.5): Dort steht mein V3 schon.
      - Ein Verbund mit gemeinsamer Frequenz "braucht 1/2 < omega^2 < min(1, v^2/(2 kappa))".
      - Bei v = kappa = 1 ist das Fenster leer. CX-1 waehlte deshalb kappa = 1/4 (P*).
      - Dazu Harland: min{1, mu} [L].
      - Weitere Quelle: "Hopf Q-balls" von Sanchez-Guillen/Adam/Wereszczynski, EPJC 47, 513 (2006), hep-th/0602008
        [L, nur Abstract].
    - **RUNDE-10/hopf1/ERGEBNIS.md** (30.09., Claude HOPF-1):
      - Produktansatz: 283 von 283 Lagen anziehend. Die Wand des Q-Balls bindet am staerksten, nicht die Mitte.
      - **Die Relaxation scheiterte.** Der h = 1-Knoten wickelte sich auf dem Gitter ab, in 3D und in der
        2D-Achsenreduktion (E unter der VK-Schranke, also Gitterartefakt). Keine Stufe-B-Zahl.
    - CX-1 (Qualifikationsvertrag fuer die Referenzaeste bei kappa = 1/4) wartete bis 29.09. auf ein GPU-Fenster. Der
      heutige Stand ist nicht geprueft.
- **Korrektur zu V3 (04:39), nicht geloescht, sondern praezisiert:**
  - ~~V3 als neuer eigener Befund~~ -> Die Disjunktheit bei v = kappa = 1 ist **Projektbestand** (KNOTEN-PAPIER,
    CX-1-Autor). Neu ist nur der folgende Zusatz [ES]:
    - Die Bedingung 1/2 < omega^2 gilt fuer einen **freien** Q-Ball. Ein phi-Kondensat **in** der Textur sieht ein
      tieferes effektives Potential.
    - Duennwand-Grenze lokal: omega^2 > min_x [U(x+y) - U(y) - G x y]/x. Bei y = 1/4 und G = 1 ist das
      0,34375 - 0,625 x + 0,5 x^2, minimal 0,148 bei x = 0,625 [ES-Rechnung].
    - Ein **gefangener** Verbund kann also unter 1/2 liegen und damit im sicheren Texturfenster. Das passt zu Omega ~
      0,577 im Piloten.
    - Bei grosser Ladung quillt phi aus der Schale, und Omega^2 -> 1/2 von oben (Duennwand).
    - Vermutung [H]: Omega(q) ist nicht monoton. Das Minimum liegt bei mittlerer Ladung und eventuell unter 1/2.
    - **Damit ist das "leere Fenster" bei kappa = 1 nicht zwingend leer.** Das ist ein Prueffall fuer die Rechenkarte.
- **Lehre aus HOPF-1 fuer die Rechenkarte [ES]:**
  - In der radialen 2+1-Igelreduktion (B = 1, f(0) = pi, f(inf) = 0) ist der Grad durch die Randbedingungen erzwungen.
    Abwickeln ist dort unmoeglich, anders als bei der 3D-Hopfzahl, die im Inneren lebt.
  - Das ist der Hauptgrund fuer 2+1 als ersten Schritt.
- R4 (offen, an Leitung): Soll eine Rechenkarte kappa als Hebel aendern duerfen?
  - Dafuer: kappa = 0,5 oeffnet die Ueberlappung der Fenster.
  - Dagegen: Das ist eine Modellwahl nach Befund, also nicht frei (Memory "Kontrollen nicht nach Befund lockern").
  - **Nachtrag 04:42:** CX-1 hat kappa = 1/4 (P*) bereits vorab festgelegt.
  - Vorschlag: In der Rechenkarte zwei vorab gebundene Punkte rechnen, kappa = 1 (Skelett) und kappa = 1/4 (CX-1-P*).
    Kein drittes kappa nach Befund.
- GS4-Zusatz (04:42, [ES]): Simons Satz betrifft den s-Kanal (l = 0).
  - Die phasengekoppelte Mode bei g = 1 liegt im l = 1-Kanal, mit Zentrifugalbarriere 1/r^2. Ihre Existenz ist daher
    NICHT vorab garantiert und taugt als echte Vorhersage.
  - Bei g = 0 (l = 0) ist die Existenz vermutlich ableitbar, nur die Frequenz nicht.

## 5a. Abschluss

- DOSSIER.md geschrieben ab 04:44:25 CEST, Rueckwaertsdurchgang (Zahlen in Abschnitt 0 gegen den Rumpf) und
  Praezisierungen bis 04:48. Abschluss 2026-10-04 04:48:35 CEST (date), innerhalb der Zeitbox (Ende 05:35).
- Abrufe: 14 von 15 (A1-A14), keine Websuche.
- Lokal: nur Read, Write, Edit, grep, sed, head, ls, find, date. Kein Interpreter, keine Rechnung.
- Die BH-PDF habe ich aus der WebFetch-Ablage mit dem Read-Werkzeug als Seitenbilder gelesen.
- Gesperrte Pfade (VERSIEGELT, vertraege-20260925, KS-1, T8-SOLL, ks-1-dk-lauf/-laeufe) aus allen greps ausgeschlossen
  und nicht geoeffnet.
- Rueckwaertsdurchgang hat zwei Ueberdehnungen berichtigt:
  - E4: "enthaelt nicht", obwohl nur Abstracts gelesen waren;
  - GS2: "an der Quelle gedeckt" gilt nur fuer den S^2-Teil.

## 6. Gestrichenes

- ~~"Jaeykkae/Speight ~2010, Supercurrent coupling destabilizes knot solitons, PRD 82, 125030"~~ (Gedaechtnis):
  - Die Journalangabe gehoert zu "Easy plane baby skyrmions" (A9).
  - Die Superstrom-Arbeit ist von Speight allein, J. Geom. Phys. 60 (2010) 599, arXiv:0812.1493 (A11).
- ~~V3 als eigener neuer Befund~~ -> Projektbestand (KNOTEN-PAPIER), siehe Korrektur in Abschnitt 5.
- ~~"In 2D ist die gefangene Mode garantiert, also keine Vorhersage"~~ -> gilt nur fuer l = 0, siehe GS4-Zusatz.
