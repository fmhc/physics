# SPIN-HOPF-L: Dossier (Runde 37, Literaturkarte)

- **Bearbeitung:**
  - feldforscher fuer claude-primary; Start 2026-10-04 04:20:01 CEST, Dossier geschrieben ab 04:44:25 CEST (date).
  - Arbeitsdatei mit allen Abrufen, Zeiten, Erwartungen vor dem Abruf, Verstoessen und Gestrichenem:
    `ARBEITSFELD.md` im selben Ordner.
- **Kennzeichen:**
  - [S] selbst an der Quelle gelesen. Die Art steht jeweils dabei: Abstract, Seitenbild oder WebFetch-Auszug.
  - [S-Projekt] hat ein anderes Projekthaus an der Quelle gelesen; ich uebernehme es aus der Projektdatei.
  - [L] bzw. [L?] Gedaechtnis; [H] Hypothese; **[ES]** eigener Schluss.
- **Umfang:**
  - 14 von 15 erlaubten Abrufen, keine Websuche (gesperrt), keine Rechnung.
  - Nach Regel 7 gibt es deshalb kein "widerlegt" und kein "gibt es nicht", nur "in dieser Stichprobe nicht gefunden".

## 0. Ergebnis zuerst

1. **Drehende (isospinning) Hopf-Solitonen sind Literatur.**
   - Quellen: Battye/Haberichter 2013 (3D, Hopf-Ladung bis 8) und Harland/Jaeykkae/Shnir/Speight 2013 [S].
   - Sie existieren bis zu einer Hoechstfrequenz omega_max = min(Masse, Metrikschwelle).
   - Bei Hopf-Ladung 1 bis 3 bleibt die Gestalt, nur die Groesse waechst. Energie und Traegheitsmoment divergieren an der
     Schwelle [S].
2. **Finkelstein-Rubinstein:**
   - Ungerade Hopf-Ladung darf fermionisch quantisiert werden. Dann sind Spin **und** Isospin halbzahlig, gerade Ladung
     bleibt bosonisch [S].
   - Codex' Regel q in Z + h/2 fuer B.5 ist damit fuer den S^2-Teil an der Quelle gedeckt. Die Uebertragung auf
     C x S^2 (der C-Faktor ist zusammenziehbar) ist Codex' Ableitung [S-Projekt].
3. **Fuer den Kern (eine fremde Q-Ball-Ladung bleibt an einer S^2-Textur haengen) fand ich in dieser Stichprobe kein
   direktes Vorbild.**
   - Naechste Verwandte sind Vortonen, also Ladung eines zweiten Felds an einem Wirbelring. Sie sind meist instabil,
     nur dicke kleine sind stabil [S].
   - Gegenbeispiel: Eine Superstrom-Kopplung zerstoert die Stabilitaet von Knoten [S].
4. **B.5 [ES]:**
   - Die reine Potentialkopplung laesst die topologische Energieschranke stehen.
   - Entscheidend ist die gemeinsame Frequenz Omega = dE/dq relativ zu 1/sqrt(2). Bei v = kappa = 1 sind freies
     Q-Ball-Fenster und sicheres Texturfenster disjunkt; das ist schon Projektbestand.
   - Ein **in** der Textur gefangenes phi-Kondensat darf aber darunter liegen, lokal bis Omega^2 ~ 0,148 (g = 1).
5. **Groesster Erwartungsverstoss:** Die Karte setzt bei null an, das Projekt hat seit 24./30.09.:
   - Tore (astra);
   - einen 3D-Variationspiloten mit 0,96 % Vorteil bei fairer Ladungsteilung;
   - eine Dynamiksperre (chi > 1 bei Omega ~ 0,98);
   - einen gescheiterten Relaxationsversuch (der Knoten wickelt sich auf dem Gitter ab).
6. **Vorschlag: Rechenkarte QB-BS-2D.** Das ist B.5 in 2+1 (Baby-Skyrmion B = 1 plus phi). Der Grad ist dort per
   Randbedingung erzwungen. Radiale Stufen dauern Sekunden, 2D-Stufen Minuten. Der Kerntest ist min_q Omega^2(q) < 1/2.

## 1. Erwartungsverstoesse (das Wichtigste zuerst)

**V0 (Gegensweep GS1, Projektlage). Erwartet (implizit in der Karte): Die Bindungsfrage ist literarisch und rechnerisch
offen.**
- Gefunden: astra-Tore vom 24.09. [S-Projekt]. Sie lasen schon Harland et al., Krusch/Speight, Ward und Hirayama.
- Weiter gefunden, alles vom 30.09.:
  - **qball-hopf-pilot:** Mit fairer Ladungsteilung liegt der ueberlagerte Zustand 0,963 % unter der getrennten
    Familienreferenz, Omega ~ 0,577. Beides sind nur Variationswerte.
  - **qball-hopf-3d:** Der geladene Hopftraeger hat chi ~ 1,09 > 1 bei Omega ~ 0,98, also komplexe charakteristische
    Geschwindigkeiten. Deshalb lief kein Zeitschritt.
  - **hopf-charge-window:** Bei q0/4 gibt es einen radial stationaeren Kandidaten mit Omega = 0,40.
  - **RUNDE-10/hopf1:** 283 von 283 Produktlagen sind anziehend, die Q-Ball-Wand bindet am staerksten. Die Relaxation
    scheiterte, weil der h = 1-Knoten sich auf dem Gitter abwickelte.
  - **RUNDE-03/tests2d-r3/KNOTEN-PAPIER.md:**
    - Dort steht, dass das Fenster bei v = kappa = 1 leer ist.
    - CX-1 waehlte deshalb kappa = 1/4.
- **Bedeutung:**
  - Fragen 1 und 4 der Karte waren intern schon zum Teil beantwortet.
  - Neu in diesem Dossier sind: die Aufloesung des Literaturwiderspruchs (V1), die Kopplungsart als Moderator (V4), die
    Schwellenformel an der Quelle (V2) und das gefangene Regime (V3*).

**V1 (A1, A2, A4). Erwartet: Isospin blaeht die Hopf-Solitonen bis zur Schwelle auf, die Form bleibt.**
- Gefunden: Zwei Gruppen am gleichen Modell 2013 widersprechen sich.
  - Harland et al.: "generically, the shape of a soliton is independent of omega" [S, Abstract].
  - Battye/Haberichter (BH): "the solution type of the lowest energy soliton can change" [S, Abstract].
- Nach Regel 1 sind das zwei Regime, mit an der Quelle benannten Moderatoren [S, BH-Volltext als Seitenbild]:
  - (1) **Hopf-Ladung N.** Fuer 1 <= N <= 3 ist "the solution type ... the same as the one in the static case, only the
    soliton's size grows" (BH S. 11). Umordnungen treten erst ab N = 4 auf, wo statische Typen fast gleich schwer sind
    (BH Tab. I).
  - (2) **Potential und Massenwert.** BH rechnen mit mu = 1 und V_I = 2 mu^2 (1 - phi3), Harland et al. meist mit
    mu = 2 und V_II. BH: Unterschiede "could be due to the different potential choice or to the different choice of
    the mass parameter" (BH S. 18).
- **Fuer unser h = 1** sagen beide Quellen dasselbe: Die Gestalt bleibt.

**V4 (A11, A12). Erwartet (still): Ein zusaetzliches Feld an der Textur laesst deren Topologie in Ruhe.**
- Gefunden:
  - Speight 2010: Die Superstrom-Kopplung "destroys the topological stability ... there can be no globally stable knot
    solitons" [S, Abstract]. Das gekoppelte Einheits-Hopfion auf S^3 ist "unstable for all R".
  - Shnir/Zhilin 2014: Geeichte Hopfionen sind **leichter** als ungeeichte. Die untere topologische Schranke sei neu zu
    ueberdenken [S, Abstract].
- Zwei Regime mit dem Moderator **Kopplungsart** [ES]:
  - Eine Ableitungs- bzw. Vektorkopplung an den Faddeev-Term greift die Schranke an.
  - B.5 koppelt nur ueber das Potential. Mit V >= c s >= 0 (Codex B.5, astra) und unveraendertem Sigma- und
    kappa-Term gilt weiter E >= E_FH >= VK-Konstante mal |h|^(3/4).
- **Bedeutung:** In B.5 steht der Knoten nicht zur Disposition, nur die Ladung. Jede spaetere Ableitungskopplung
  (etwa Strom-Strom) wuerde das aendern.

**V2 (A4, A8, A13). Erwartet (E1): Die Grenze liegt "wie beim Q-Ball" bei omega -> Masse.**
- Gefunden [S]:
  - BH 2013: "for mu <= 1 there exists a maximal frequency omega_max = mu" (S. 11).
  - Baby-Skyrmionen sind stabil "for all angular frequencies omega <= min(mu,1)" (BH 2013b, Abstract).
  - Harland et al. nennen zwei Grenzen, omega1 = 1 (Zielsphaere, Pseudoenergie "no longer bounded below") und
    omega2 = mu (Masse) [S, WebFetch-Auszug].
- Uebertragen auf B.5 [ES-Rechnung]:
  - Die Metrikschwelle ist Omega^2 < v^2/(2 kappa) = 1/2. Die n-Masse ist sqrt(3) (Projekt: Nordpolmasse^2 = 3).
  - Das Verhaeltnis sqrt(6) ~ 2,45 entspricht BH-mu ~ 2,45. B.5 liegt also im Regime **"Metrikverlust vor
    Strahlung"**, naeher an Harland (mu = 2) als an BH (mu = 1).
- Zusatz [S, Auszug]:
  - Bei unendlichen Strings fanden Harland et al. Loesungen bis omega ~ 1,4 ("exceeds the expected value of 1").
  - Ein Sattel der Pseudoenergie ist nicht automatisch dynamisch instabil.

**V3\* (Korrektur meines eigenen Zwischenstands, ARBEITSFELD Abschnitt 5).**
- ~~"Disjunkte Fenster bei v = kappa = 1" als neuer Befund~~: Das ist Projektbestand (KNOTEN-PAPIER).
- Neu ist nur folgende Praezisierung [ES]: Die Unterkante 1/2 < omega^2 gilt fuer einen **freien** Q-Ball.
  - Ein Kondensat im Inneren der Textur sieht das effektive Potential W(x) = U(x+y) - U(y) - G x y.
  - Die lokale Duennwand-Bedingung lautet omega^2 > min_x W(x)/x. Bei y = 1/4, G = 1 ist das
    0,34375 - 0,625 x + 0,5 x^2, minimal **0,148** bei x = 0,625. Bei G = 0 sind es 0,398.
- Das ist nur eine notwendige Bedingung. Sie zeigt aber: Das "leere Fenster" ist fuer einen gefangenen Verbund nicht
  zwingend leer. Der Pilotwert Omega ~ 0,577 liegt genau dort.
- Bei G = 0 entfaellt der Konflikt ganz: Die Phasen sind unabhaengig, die Textur darf ruhen [ES].

**Kleinere Verstoesse:**
- **A6:** Vortonen sind meist instabil und zerfallen. Nur "thick vortons with small radius" ueberstehen die 3+1-Dynamik,
  und das Modell ist geeicht [S].
- **A9:** Mein Gedaechtnis ordnete "PRD 82, 125030" der Superstrom-Arbeit zu. Es gehoert zu "Easy plane baby
  skyrmions" [S].
- **A12:** Die "geeichten Hopfionen" sind statisch und magnetisch, nicht elektrisch geladen und isorotierend [S].
- **A13:** Harland et al. erwaehnen Q-Lumps nicht. Leese 1991 bleibt [L].

## 2. Erwartungen E1 bis E5: Urteil mit Beleg

| Nr | Erwartung (Karte) | Urteil | Beleg |
|---|---|---|---|
| E1 | Drehende Hopf-Solitonen numerisch gerechnet; Existenz bis zu einer groessten Drehfrequenz | **eingetroffen**, praezisiert | BH 2013 (bis N = 8, volle 3D-Relaxation, omega_max = mu fuer mu <= 1, E und U33 divergieren bei omega = mu) [S]; Harland et al. 2013 (zwei Grenzen 1 und mu) [S]. Praezisierung: Die Grenze ist min(Masse, Metrikschwelle). Fuer B.5 bindet die Metrikschwelle 1/sqrt(2), nicht die Masse [ES]. |
| E2 | FR-fermionisch fuer manche Hopf-Ladungen erlaubt, fuer andere nicht | **eingetroffen** | Krusch/Speight 2006: "Hopf solitons can be quantized as fermions if their Hopf charge is odd" [S, Abstract]. Spin und Isospin sind "half integer if and only if Q is odd" [S, Auszug Abschn. 4]. Bei geradem Q ist bosonisch zu waehlen; die Modulraum-Topologie allein erzwingt das nicht [S, Auszug]. |
| E3 | Gebundene Zustaende S^2-Textur + komplexer Skalar mit stabiler Bindung | **teilweise** | (a) Ladung im **selben** Feld: ja, isorotierende Hopf-Solitonen und Baby-Skyrmionen [S], Hopf-Q-Baelle auf S^3 [S-Projekt, Abstract]. (b) Ladung eines **zweiten** Felds an einem topologischen Ring: Vortonen, meist instabil [S]. (c) Textur plus Dichte/Strom (BFN 2002, "stable knotted solitons" behauptet) [S], von Speight 2010 in Frage gestellt [S]. Den Kernfall "S^2-Textur plus eigenes Q-Ball-Feld, stabil gebunden" habe ich in dieser Stichprobe nicht gefunden. |
| E4 | Fuer genau Codex' Kopplung keine Literatur | **nicht pruefbar** | Ohne Websuche ist Abwesenheit nicht feststellbar (Regel 7). Schwaches Indiz dafuer: Keine der 11 Arbeiten zeigt nach Abstract bzw. Auszug ein Modell aus S^2-Textur plus eigenem Q-Ball-Feld mit gemeinsamem U(\|phi\|^2+\|b\|^2) und Paartransfer, und keine Projektquelle nennt eines. Die Volltexte sind nicht durchsucht. astra: "keine systematische Prioritaetssuche". |
| E5 [H] | 2+1-Gegenstueck in <= 10 min je Lauf | **teilweise (plausibel, nicht gemessen)** | BH rechnen isorotierende Baby-Skyrmionen voll in 2D [S]. Projektanalogie: sechs radiale 1D-Relaxationen samt chi-Karten in 20 CPU-s (hopf-charge-window) [S-Projekt]. 2D-Relaxation und 2D-Zeitlauf nach Abschaetzung 3 bis 8 min [ES]; Zeitlauf grenzwertig. |

## 3. Fragen 1 bis 5: kurze Antworten

1. **Isospinning Hopf-Solitonen:**
   - Ja: BH 2013, Hopf-Ladung bis 8, volle 3D-Relaxation bei fester Isospinladung; Harland et al. 2013 bei fester
     Frequenz [S].
   - Stabil bis omega_max = mu (fuer mu <= 1), allgemein bis min(Masse, Metrikschwelle). Energie und Traegheit divergieren
     an der Schwelle [S].
   - Energie-Ladung im Stabmodell: E = E0/sqrt(1 - (omega/omega*)^2) bzw. E^2 = E0^2 + (A/C) J^2 [S, Auszug Gl. 5.1].
   - Bei grossem J wachsen E, Traegheit und Groesse linear in J, waehrend omega gegen eine Konstante strebt [S, Auszug].
     Das ist Q-Ball-artig (E/J -> konstant) [ES].
   - Ab N = 4 ordnet Isospin die Grundzustandstypen um [S].
2. **Fermionische Hopf-Ladungen:**
   - Genau die ungeraden [S]. Spin und Isospin sind dann halbzahlig [S, Auszug].
   - Die Wahl bleibt eine Zusatzannahme der Quantisierung (Projekt-Audit, Codex/Giulini [S-Projekt]).
   - BH warnen: Bosonische Kollektivkoordinaten wie FR-Quantisierung setzen voraus, dass Zentrifugaleffekte die
     Symmetrien nicht brechen. Bei N = 5, 6, 8 tun sie es [S].
3. **Gebundene Zustaende S^2-Textur + komplexes Feld:**
   - Ladung im selben Feld: gut belegt (isorotierende Hopfionen und Baby-Skyrmionen [S]; Q-Lumps [L, nicht geprueft]).
   - Zweitfeld-Ladung an topologischem Defekt: Vortonen, stabil nur dick und klein [S].
   - Textur gekoppelt an Strom oder Eichfeld: Die Topologie kann ihren Schutz verlieren (Speight) oder die Schranke wird
     unterlaufen (Shnir/Zhilin) [S].
   - Direkter Fall Q-Ball plus Hopfion oder Baby-Skyrmion: in dieser Stichprobe nicht gefunden.
4. **Folgen fuer Codex' C x S^2:**
   - **Kopplung, die die Ladung haelt:**
     - Klassisch braucht es eine anziehende Ueberlappung. B.5 hat sie schon: Der Dichte-Kreuzterm xy[-2 + 1,5(x+y)] < 0
       fuer x + y < 4/3 ist vorab ableitbar [S-Projekt].
     - Dazu eine gemeinsame Frequenz in allen Fenstern:
       - Bei G = 0 gibt es keinen Konflikt, die Textur darf ruhen.
       - Bei G != 0 muss der Knoten mitdrehen; hinreichend ist Omega^2 < v^2/(2 kappa).
     - Die Kopplung muss eine Potentialkopplung bleiben (V4).
   - **Quantenmechanisch [ES aus A14]:** Im fermionischen Zweig hat der Knoten mit ungeradem h stets halbzahligen
     Isospin. Mindestens eine halbe Ladungseinheit bleibt also topologisch am Knoten; der Rest bindet nur energetisch.
   - **Gegenbeispiele:**
     - Eine Abloesung einer Q-Ball-Ladung von einem Hopfion fand ich nicht beschrieben.
     - Analoge Fehlschlaege: Vortonen zerfallen meist [S]; Superstrom-Kopplung zerstoert Knoten [S]; Isospin ordnet
       Hopf-Typen ab N = 4 um [S].
     - Im Projekt: chi > 1 beim geladenen Hopftraeger mit Omega ~ 0,98, Zeitentwicklung dort nicht wohlgestellt
       [S-Projekt].
5. **2+1-Gegenstuecke:**
   - Isorotierende Baby-Skyrmionen (BH 2013b): stabil fuer omega <= min(mu,1). B >= 2 zerfaellt ab einer kritischen
     Frequenz in B Einerbausteine [S].
   - Der axiale Hopf-Typ A_{n,m} ist ein Baby-Skyrmion mit Windung m, entlang eines Rings eingebettet und um 2 pi n
     verdreht (BH S. 5-6) [S]. Das 2D-Modell ist also der Querschnitt des 3D-Knotens.
   - Der Hopf-Term in 2+1 gibt Solitonen beliebigen Spin (Anyonen) und aendert die klassischen Gleichungen nicht
     (Wilczek/Zee 1983) [L, nicht geprueft]. Das 2D-Modell testet deshalb nur die Bindung, nicht den Spin.

## 4. Literaturstand nach Thema (mit Quellen)

- **Isorotierende Hopf-Solitonen:**
  - BH 2013, PRD 87, 105003 [S, Seitenbild]:
    - Modell mit Lagrangedichte (1/(32 pi^2 sqrt 2)){d phi.d phi - (1/2)(d phi x d phi)^2 - V}.
    - Potentiale V_I = 2 mu^2 (1 - phi3) und V_II = mu^2 (1 - phi3^2); mu = 1.
    - Gitter (201)^3, dx = 0,1, Differenzen 4. Ordnung.
    - Feste Isospinladung K, omega = K/U33.
    - omega_max = mu fuer mu <= 1 aus linearer Stabilitaetsanalyse.
    - N = 1-3 typtreu, N = 4 (4A22 -> Link ab omega >= 0,60), N = 5, 6, 8 mit geaenderten Symmetrien.
  - Harland et al. 2013, J. Phys. A 46, 225402 [S, Abstract und Auszug]:
    - Pseudoenergie bei festem omega, Gradientenabstieg ohne Symmetrieannahme.
    - Gestalt generisch omega-unabhaengig, Groesse waechst monoton.
    - Elastisches Stabmodell mit einem Parameter. Zwei Grenzen 1 und mu.
- **Fermionische Quantisierung:** Krusch/Speight 2006, CMP 264, 391 [S]. Ungerade Q fermionisch moeglich; Spin und
  Isospin halbzahlig genau bei ungeradem Q; Grundzustaende bis Q = 7.
- **2+1:** BH 2013b, PRD 88, 125016 [S]. omega <= min(mu,1), Zerfall von B >= 2 bei hohem omega.
- **Zweitfeld-Ladung an topologischem Ring:**
  - Radu/Volkov 2008, Phys. Rep. 468, 101 [S, Abstract]: Knoten, Versuche sie zu eichen, rotierende Q-Baelle
    "twisted and gauged", Bedingungen gegen Abstrahlung, erste globale Vortonen.
  - Garaud/Radu/Volkov 2013, PRL 111, 171602 [S, Abstract]: geeichtes Witten-Modell; die meisten Vortonen zerfallen,
    dicke kleine sind stabil.
- **Textur plus Zusatzfeld:**
  - Babaev/Faddeev/Niemi 2002, PRB 65, 100512 [S]: Zweikomponenten-Kondensat -> O(3)-Sigma-Modell, Knoten behauptet.
  - Speight 2010, J. Geom. Phys. 60, 599 [S]: Superstrom-Kopplung, keine global stabilen Knoten.
  - Shnir/Zhilin 2014, PRD 89, 105010 [S]: geeichte Hopfionen leichter, Flussquantisierung.
- **Randstaendig:**
  - Kobayashi/Nitta 2014, PLB 728, 314 [S]: Torusknoten aus Sine-Gordon-Kinkstrings auf toroidalen Domaenenwaenden,
    Hopf-Ladung PQ.
  - Jaeykkae/Speight 2010, PRD 82, 125030 [S]: Easy-plane-Baby-Skyrmionen, Einerskyrmion aus zwei Halb-Lumps. Nur durch
    meinen Fehlabruf gelesen.

## 5. Regime und Moderatoren

| Feld | Regime A | Regime B | Moderator | Beleg |
|---|---|---|---|---|
| Isospin und Gestalt | Typ bleibt, nur Groesse waechst | Grundzustandstyp wechselt, Transmutation | Hopf-Ladung N (Fast-Entartung ab N ~ 4); Potential und mu | BH S. 11, S. 18, Tab. I [S]; Harland Abstract [S] |
| Frequenzgrenze | Strahlungsgrenze omega = Masse | Metrikgrenze omega = 1 (BH-Einheiten) | Verhaeltnis Masse/Metrikschwelle; B.5: sqrt(6) | BH S. 11, BH 2013b, Harland Paragraf 2 [S]; Uebertragung [ES] |
| Zusatzfeld und Topologie | Schranke bleibt | Schranke faellt bzw. wird unterlaufen | Kopplungsart: Potential gegen Ableitung/Eichfeld | Speight 2010, Shnir/Zhilin 2014 [S]; B.5-Seite [ES] |
| Ladung an Ring (Vorton) | stabil | zerfaellt | Dicke und Radius | Garaud et al. 2013 [S] |
| Ladung an Knoten in B.5 | gefangen (Omega^2 < 1/2 moeglich) | ausgequollen (Omega^2 -> 1/2 von oben) | Gesamtladung q; Paarkopplung G (bei G = 0 kein Gleichlauf noetig) | [ES]/[H], Pilot Omega ~ 0,577 [S-Projekt] |

## 6. Unterscheidungspunkte (Regel 2)

- **U1 Harland ("Gestalt bleibt") gegen BH ("Typwechsel"):**
  - Sie laufen nur bei N >= 4 nahe der Schwelle mit gleichem Potential und gleichem mu auseinander.
  - Fuer h = 1 sind sie **nicht unterscheidbar**, denn beide sagen "Gestalt bleibt". Fuer uns ist keine Entscheidung noetig.
- **U2 "Fenster bei kappa = 1 leer" (KNOTEN-PAPIER) gegen "gefangener Verbund unter 1/2" (V3\*):**
  - Messgroesse ist min_q Omega^2(q) auf dem relaxierten phasengekoppelten Ast: unter oder ueber 1/2.
  - Das ist in einer radialen 2+1-Rechnung in Sekunden zugaenglich (P1 unten).
- **U3 Physikalische Bindung gegen Gitterartefakt (HOPF-1):**
  - Die Energie muss ueber der topologischen Schranke liegen. In 2D (v = 1) ist das 2 pi |B| aus dem Sigma-Term, nach
    der Bogomolny-Ungleichung Int |grad n|^2 >= 8 pi |B| [L, Standard].
  - Dazu Konvergenz unter h -> h/2.
  - In der radialen Reduktion ist Abwickeln per Randbedingung ausgeschlossen.
- **U4 chi-Kriterium (hinreichend) gegen tatsaechliche Dynamik (Harland: Sattel ist nicht gleich Instabilitaet):**
  - Man vergleicht 2D-Zeitlaeufe von Zustaenden mit chi_max knapp unter und knapp ueber 1.
  - Bei schlechter Gestelltheit waechst die Rate mit 1/h, sonst bleibt sie beschraenkt.
- **U5 Potentialkopplung (B.5) gegen Ableitungskopplung (Speight):**
  - Pruefgroesse: E_mix >= topologische Schranke fuer alle q.
  - In B.5 ist das per V >= c s vorab gesichert [ES]. Hier gibt es also **keinen** Unterscheidungspunkt innerhalb von B.5.
  - Er entstuende erst, wenn man eine Ableitungskopplung hinzunimmt.

## 7. Vorschlag fuer eine Rechenkarte: QB-BS-2D (Q-Ball am Baby-Skyrmion, 2+1)

**Warum 2+1:**
- (1) Der 3D-Hopf-Typ A_{n,m} ist ein Baby-Skyrmion entlang eines Rings [S, BH S. 5-6]. 2D ist also sein Querschnitt.
- (2) HOPF-1 scheiterte daran, dass sich der h = 1-Knoten auf dem Gitter abwickelte [S-Projekt]. In der radialen
  B = 1-Reduktion erzwingen f(0) = pi und f(inf) = 0 den Grad.
- (3) BH haben isorotierende Baby-Skyrmionen in 2D voll gerechnet [S]. Es gibt also einen Literaturanschluss.
- (4) Kein GPU-Fenster noetig; CX-1 bleibt unberuehrt.

**Modell:**
- Lagrangedichte wie B.5, nur in zwei Raumdimensionen:

  L = |d phi|^2 + (v^2/4) dn.dn - U(|phi|^2 + |b|^2) + G Re[(phi^* b)^2] - mu^2 v^2 (1 - n3) - (kappa/4) H_mn H^mn,

  mit b = (v/2)(n1 + i n2) und U(s) = s - s^2 + s^3/2.
- Parameter, vorab gebunden, keine Nachwahl:
  - v = mu = 1;
  - kappa in {1 (Skelett), 1/4 (CX-1-P\*)};
  - G = gJ in {0, 1}.
- Igel-Ansatz:
  - n = (sin f cos(theta + Omega t), sin f sin(theta + Omega t), cos f).
  - Bei G = 0: phi = h(r) e^{i omega t} (l = 0, zwei Ladungen).
  - Bei G = 1: phi = h(r) e^{i(theta + Omega t)} (l = 1, phasengekoppelt, h(0) = 0). Nur so bleibt der Paarterm
    winkelfrei [ES].
- Festladungsreduktion E_q = V + q^2/(2 Lambda) nach astra, sinngemaess fuer 2D [ES].

**Stufen:**
- **S0 Eichproben:**
  - Statisches B = 1-Profil mit E >= 2 pi |B| und Konvergenz bei Verdopplung von N_r.
  - 2D-Q-Ball-Profile bei drei omega in (1/sqrt 2, 1).
  - Literaturwert fuer das alte Baby-Skyrme-Modell: Er ist vor dem Vertrag an der Quelle zu lesen (Piette/Schroers/
    Zakrzewski 1995, [L]). Ich habe ihn nicht.
- **S1 Referenzaeste (radial):**
  - E_H(q): isorotierendes B = 1 mit phi = 0, bis Omega^2 = 0,95 v^2/(2 kappa) oder bis der Loeser versagt; je Profil
    chi_max.
  - E_Q(q) fuer l = 0 (und l = 1 zum Vergleich).
  - E_sep(q) = min_u [E_H(u) + E_Q(q - u)], einschliesslich der Raender u = 0 und u = q.
- **S2 Gebundene radiale Aeste:**
  - G = 0: ruhende Textur plus phi (q_n = 0), Scan in q_phi.
  - G = 1: gekoppelter l = 1-Ast.
  - Je q messen: Omega(q), D(q) = (E_sep - E_mix)/E_sep, chi_max(q) und J.
- **S3 Volle 2D-Relaxation (nicht axial):**
  - Bei festem q aus drei Starts: phi zentriert (l = 0), phi aussermittig auf dem Ring, phi phasengekoppelt (l = 1).
  - Grad B ueber die topologische Dichte und Energie ueber der Schranke pruefen.
- **S4 2D-Zeitlauf:**
  - Start aus S2/S3, Stoerung 1 %, T = 50.
  - Messen: Anteil der phi-Ladung innerhalb R_c = 3 r_Ring, Drift von Omega, chi ueber der Zeit, Vergleich bei dt/2.

**Vorhersagen (vorab, koennen scheitern):**

| Nr | Vorhersage | Wahrsch. [H] | Scheitert, wenn |
|---|---|---|---|
| P1 (Kern, U2) | Bei kappa = 1, G = 1 hat der gekoppelte radiale Ast min_q Omega^2(q) < 1/2. Es gibt also ein Ladungsfenster im sicheren Texturbereich. | 55 % | Omega^2 >= 1/2 fuer alle q, auf denen der Ast existiert. Dann gilt "Fenster leer" auch fuer gefangene Verbuende. |
| P2 | Die lineare l = 1-Mode (G = 1) im statischen B = 1-Topf existiert, mit omega0^2 < 1. | 45 % | Kein gebundener l = 1-Zustand. Grobe Abschaetzung [ES]: Der Ring liegt bei r ~ 1, die Barriere 1/r^2 ~ 1 ist so tief wie der Topf (0,66). |
| P3 | Bei G = 0, kappa = 1 ist max_q D(q) >= 1 %. | 50 % | max D < 1 % (das Vorzeichen D > 0 ist Kontrolle, nicht Vorhersage) |
| P4 | Bei G = 1 ist der energetisch tiefste Verbund bei festem q **nicht axial** (phi aussermittig am Ring; vgl. HOPF-1 "Wand bindet am staerksten"). | 55 % | Alle aussermittigen Starts relaxieren zum axialen Zustand oder liegen hoeher. |
| P5 (Kern, U4) | Zustaende mit chi_max < 1 halten in S4 mindestens 90 % der phi-Ladung in R_c. Zustaende mit chi_max > 1 zeigen Wachstum auf Gitterskala, das unter h/2 schneller wird. | 60 % | Ladung loest sich trotz chi < 1, oder der Lauf bleibt trotz chi > 1 glatt. |
| P6 | Bei kappa = 1/4 hat der gekoppelte Ast ein q-Intervall mit Omega^2 in (1/2, 1) und chi_max < 1. | 60 % | Kein solches Intervall. |

**Kontrollen (vorab ableitbar, KEINE Vorhersagen):**
- K1: Das Vorzeichen des Dichte-Kreuzterms.
- K2: Omega^2 -> 1/2 von oben bei grossem q (Duennwand).
- K3: J = +-q fuer den axialen gekoppelten Zustand (B = m = 1). Dort wirkt eine Raumdrehung wie die gemeinsame
  U(1) [ES].
- K4: Nullprobe mit G = 0 und U(x) + U(y) statt U(x+y) ergibt D = 0 (wie Codex' Skelett).
- K5: Grad 1 +- 10^-3 und E >= 2 pi |B|.
- K6: Ladungserhaltung in S4 relativ < 10^-4.

**Laufzeit [ES, nicht gemessen; Rechenort .69 ueber kleintest.sh, Unit-Grenze 600 s laut Arbeitsfeld der Leitung
30.09.]:**
- **S0 bis S2 (radial):**
  - N_r = 2000 bis 4000, Newton oder gebremster Fluss; < 5 s je Astpunkt.
  - Scan mit 30 bis 50 q-Werten < 5 min, ein Thread.
  - Anker: hopf-charge-window, sechs 1D-Relaxationen samt Karten in 20 CPU-s auf TS440 [S-Projekt].
- **S3 (Relaxation):**
  - 256^2 Punkte, h ~ 0,1, 1-3 x 10^4 Schritte gebremster Newton-Fluss.
  - Rechenaufwand: ~2,6 x 10^7 Flop je Schritt, zusammen 3-8 x 10^11 Flop.
  - Ergibt 3 bis 8 min bei 1 bis 2 GFlop/s (numpy, ein Thread). Grenzwertig; Ausweich 192^2.
- **S4 (Zeitlauf):**
  - 192^2 Punkte, RK4 mit dt ~ 0,02 bei h ~ 0,13 (Gleichungen zweiter Ordnung, Lichtgeschwindigkeit 1), T = 50.
  - Rechenaufwand: ~10^4 Auswertungen der rechten Seite, ~3 x 10^11 Flop.
  - Ergibt 3 bis 5 min.
- Vor dem Vertrag: einen Rauchtest messen und die Zahlen ersetzen (Memory "Budget vorab messen").

**Was die Karte nicht zeigt:**
- Spin: In 2+1 waere er ein frei gewaehltes theta [L].
- 3D-Bindung: Kruemmung und Verdrillung des Rings fehlen.
- Quantenmassen.
- Ein positives P1/P5 macht die 3D-Frage (CX-1) lohnender, ersetzt sie aber nicht.

## 8. Gegensweep-Befunde (Regel 4)

| Nr | Selbstverstaendliche Annahme | Geprueft? | Befund |
|---|---|---|---|
| GS1 | Die Karte steht am Anfang der Bindungsfrage | **ja** (Projekt-grep, 6 Dateien gelesen) | Falsch. Siehe V0. |
| GS2 | Codex' Regel q in Z + h/2 stimmt | **ja** (A14) | Fuer den S^2-Teil an der Quelle bestaetigt; die Uebertragung auf C x S^2 bleibt Codex' Ableitung. Folge [ES]: Im fermionischen Zweig bleibt mindestens eine halbe Ladungseinheit am ungeraden Knoten. |
| GS3 | Die Kopplung laesst die Topologie in Ruhe | **ja** (Projekttext gegen A11/A12) | Gilt fuer B.5 (Potential), nicht fuer Ableitungskopplungen. |
| GS4 | In 2D bindet jeder anziehende Topf (Simon 1976) | nein [L] | Gilt nur fuer l = 0. Die gekoppelte l = 1-Mode ist daher eine echte Vorhersage (P2). |
| GS5 | Der Hopf-Term in 2+1 ist klassisch wirkungslos (Wilczek/Zee) | nein [L] | Falls ja, testet 2D nur die Bindung. |
| GS6 | WebFetch-Auszuege sind woertlich | teilweise | Bei A13/A14 zwei schiefe Deutungen des Zusammenfassers erkannt und verworfen (Harland Gl. 2.10; "fermionisch erzwungen"). Weitere sind moeglich. Nur BH als Seitenbild gelesen. |
| GS7 | Regel 7 ist erfuellbar | nein | Websuche gesperrt. Deshalb ist E4 nicht pruefbar, und es gibt keine Negativurteile. |

## 9. Kalibrierung

- **(a) Gemessen** (Literatur oder Projektlauf):
  - omega_max = mu (mu <= 1) und min(mu,1) in 2D.
  - Typtreue fuer N = 1-3.
  - Superstrom-Kopplung zerstoert globale Stabilitaet.
  - Vortonen meist instabil.
  - Spin und Isospin halbzahlig genau bei ungeradem Q.
  - Projekt: 0,963 % Variationsvorteil; chi ~ 1,09 bei Omega ~ 0,98; 283 von 283 Produktlagen anziehend; Relaxation
    gescheitert.
- **(b) Nuetzlich verdichtet [ES]:**
  - Taktgroesse Omega = dE/dq mit den Schwellen 1/sqrt 2, 1 und sqrt 3.
  - B.5 im Regime "Metrik vor Strahlung" (sqrt 6).
  - Kopplungsart als Moderator.
  - Gefangenes Regime mit lokaler Unterkante 0,148.
  - Halbe Ladung topologisch am Knoten.
- **(c) Gewachsene Gewissheit ohne neue Evidenz (Warnzeichen):**
  - Im Lauf stieg mein Eindruck "Bindung ist wahrscheinlich", waehrend die Frage feiner wurde (Fenster, Hyperbolizitaet,
    Abwickeln).
  - Getragen wird er vom negativen Kreuzterm. Der ist vorab ableitbar und sagt ueber relaxierte, dynamisch stabile
    Zustaende nichts.
  - Belastbar ist nur: Anziehung im Produktansatz und ~1 % Variationsvorteil.

## 10. Offene Fragen

- O1: Liegt min_q Omega^2(q) des gefangenen Verbunds unter 1/2? (P1; entscheidet, ob kappa = 1 tragfaehig ist.)
- O2: Ist das chi-Kriterium dynamisch scharf? Harland zeigen Strings bis omega ~ 1,4, also jenseits der hinreichenden
  Schwelle (P5).
- O3: Leese 1991 (Q-Lumps) und Wilczek/Zee 1983 sind nicht an der Quelle gelesen. Beide sind fuer den 2D-Anschluss
  zitierwuerdig, aber nicht auf arXiv.
- O4: E4, also die Prioritaet der B.5-Kopplung, braucht eine Websuche mit 24-Monats-Fenster.
- O5: Wie ist der heutige Stand von CX-1 (kappa = 1/4)? Nicht geprueft. Die Rechenkarte sollte nicht mit CX-1 kollidieren.
- O6 (an Leitung): Soll QB-BS-2D beide kappa-Punkte vorab binden (Vorschlag: ja, 1 und 1/4, kein dritter nach Befund)?

## 11. Selbstanzeigen

1. Die Projektvorarbeit fand ich erst durch einen eigenen grep, nicht ueber die Karte.
   - Mein Zwischenbefund V3 ("disjunkte Fenster") stand als neu im Arbeitsfeld, war aber Projektbestand (KNOTEN-PAPIER).
   - Ich habe ihn dort gestrichen und praezisiert.
2. Ein Abruf (A9) ging auf eine falsch erinnerte Zuordnung ("PRD 82, 125030"). Die richtige Superstrom-Arbeit habe ich
   danach gefunden (A11).
3. A13 (Harland-Volltext) und A14 (Krusch/Speight Abschnitt 4) kenne ich nur als WebFetch-Auszuege eines
   Zusammenfassungsmodells.
   - Zwei Fehldeutungen habe ich erkannt und verworfen; weitere kann ich nicht ausschliessen.
   - Woertlich als Seitenbild gelesen ist nur BH 2013 (S. 1-11, 17-19). Dafuer las ich die von WebFetch abgelegte PDF
     lokal mit dem Read-Werkzeug, ohne zusaetzlichen Abruf.
4. Eigene Rechnungen ohne Fremdpruefung:
   - Metrikschwelle in BH-Einheiten (omega = 1);
   - Verhaeltnis sqrt 6;
   - lokale Unterkante 0,148 bzw. 0,398, nur eine notwendige Bedingung;
   - J = q;
   - Groessenschaetzung fuer P2 (grob).
5. Die Laufzeiten sind geschaetzt, nicht gemessen; lokal wurde nichts gestartet.
6. Regel 7 war nicht erfuellbar. Deshalb ist E4 nicht pruefbar.
7. Nicht geprueft: heutiger CX-1-Stand; Literaturwert fuer das statische Baby-Skyrmion; Simon 1976; Leese 1991;
   Wilczek/Zee 1983.

## 12. Quellenliste

**Selbst gelesen [S]:**
1. Battye, R. A.; Haberichter, M. (2013): Classically isospinning Hopf solitons. Phys. Rev. D 87, 105003.
   https://arxiv.org/abs/1301.6803. Abstract; Volltext S. 1-11, 17-19 als Seitenbild.
2. Harland, D.; Jaeykkae, J.; Shnir, Ya.; Speight, M. (2013): Isospinning hopfions. J. Phys. A 46, 225402.
   https://arxiv.org/abs/1301.2923. Abstract; HTML-Auszug https://arxiv.org/html/1301.2923.
3. Krusch, S.; Speight, J. M. (2006): Fermionic quantization of Hopf solitons. Commun. Math. Phys. 264, 391-410.
   https://arxiv.org/abs/hep-th/0503067. Abstract; HTML-Auszug Abschnitt 4.
4. Battye, R. A.; Haberichter, M. (2013): Isospinning baby Skyrmion solutions. Phys. Rev. D 88, 125016.
   https://arxiv.org/abs/1309.3907. Abstract.
5. Radu, E.; Volkov, M. S. (2008): Stationary ring solitons in field theory - knots and vortons. Phys. Rep. 468,
   101-151. https://arxiv.org/abs/0804.1357. Abstract.
6. Garaud, J.; Radu, E.; Volkov, M. S. (2013): Stable cosmic vortons. Phys. Rev. Lett. 111, 171602.
   https://arxiv.org/abs/1303.3044. Abstract.
7. Babaev, E.; Faddeev, L. D.; Niemi, A. J. (2002): Hidden symmetry and knot solitons in a charged two-condensate Bose
   system. Phys. Rev. B 65, 100512. https://arxiv.org/abs/cond-mat/0106152. Abstract.
8. Speight, J. M. (2010): Supercurrent coupling in the Faddeev-Skyrme model. J. Geom. Phys. 60, 599-610.
   https://arxiv.org/abs/0812.1493. Abstract.
9. Shnir, Ya.; Zhilin, G. (2014): Gauged Hopfions. Phys. Rev. D 89, 105010. https://arxiv.org/abs/1404.4867. Abstract.
10. Kobayashi, M.; Nitta, M. (2014): Torus knots as Hopfions. Phys. Lett. B 728, 314-318.
    https://arxiv.org/abs/1304.6021. Abstract.
11. Jaeykkae, J.; Speight, M. (2010): Easy plane baby skyrmions. Phys. Rev. D 82, 125030.
    https://arxiv.org/abs/1010.2217. Abstract; nur Fehlabruf, siehe Selbstanzeige 2.

**Bibliographie ueber die BH-Literaturliste (S. 18-19) [S], Inhalt nicht gelesen:**
- Finkelstein/Rubinstein, J. Math. Phys. 9, 1762 (1968);
- Faddeev/Niemi, Nature 387, 58 (1997);
- Piette/Schroers/Zakrzewski, Z. Phys. C 65, 165 (1995);
- Vakulenko/Kapitanski, Sov. Phys. Dokl. 24, 433 (1979).

**Projektquellen (gelesen):**
- Codex, SPIN-KONSTRUKTION-codex.md (23./24.09.2026);
- astra, coordination/literatur-20260924/CXS2-TORE-astra-20260924.md (24.09.2026);
- coordination/resonance-20260930/qball-hopf-pilot/{ERGEBNIS.txt, BINDUNG-FORTSCHRITT.txt}, qball-hopf-3d/{ERGEBNIS.txt,
  ROTATIONSGRENZE.txt, SPIN-ANSCHLUSS-KURZ.txt}, hopf-charge-window/ERGEBNIS.txt,
  source-audit/SPIN-HALB-ANSCHLUESSE.txt (alle 30.09.2026);
- coordination/runden-v3/RUNDE-10/hopf1/ERGEBNIS.md (30.09.2026);
- coordination/runden-v3/RUNDE-03/tests2d-r3/KNOTEN-PAPIER.md (30.09.2026), darin [S-Projekt, Abstract]
  Sanchez-Guillen/Adam/Wereszczynski, Hopf solitons and Hopf Q-balls on S^3, EPJC 47, 513 (2006),
  https://arxiv.org/abs/hep-th/0602008.

**Nur Gedaechtnis [L], nicht geprueft:**
- Leese, R. A. (1991): Q-lumps and their interactions, Nucl. Phys. B 366, 283.
- Wilczek, F.; Zee, A. (1983): Linking numbers, spin, and statistics of solitons, Phys. Rev. Lett. 51, 2250.
- Simon, B. (1976): The bound state of weakly coupled Schroedinger operators in one and two dimensions, Ann. Phys. 97, 279.

## Einfach gesagt

Wir wollten wissen, ob ein Knoten im Feld eine Ladung festhalten kann, so wie ein Kreisel seinen Schwung behaelt. Die
Fachliteratur zeigt: Ein Knoten, der sich in sich selbst dreht, bleibt stabil, solange er nicht zu schnell dreht. Ein
Knoten mit ungerader Knotenzahl darf sich sogar wie ein Teilchen mit halbem Spin verhalten, also wie ein Elektron. Ob
aber eine fremde Ladungswolke, unser alter Q-Ball, am Knoten kleben bleibt, hat niemand gezeigt, auch wir noch nicht:
Die beiden ziehen sich an, doch ein sauber berechneter gemeinsamer Zustand fehlt. Als naechsten Schritt schlagen wir ein
flaches Modell in zwei Dimensionen vor, das in wenigen Minuten rechnet und klar scheitern kann.
