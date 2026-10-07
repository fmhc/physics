# SPIN2-D4-2: Traegt die M_E-Methode (Bellazzini u. a.) externe Gravitonen und den Dreipunkt-Vertex?

- feldforscher, Runde 13 (v3, explorativ), Auftrag claude-primary, Karte RUNDE-13/spin2-d4-2/KARTE.md
- Start 2026-10-01 21:28:29 CEST (date). Zeitbox 50 min, also bis etwa 22:18 CEST.

## BERICHT (geschrieben ab 2026-10-01 21:42:11 CEST, date davor)

Belege im Arbeitsfeld darunter (E0-E6, R1-R5, Z-1, Z-2, Gegensweep G1-G4). Lesetiefe: [A] an der Quelle mit Seite und
Gleichung, [S] nur Abstract, [L?] Gedaechtnis, [H] Hypothese, [ES] eigener Schluss. Abkuerzungen: CHLPSD = Caron-Huot, Li,
Parra-Martinez, Simmons-Duffin 2022; BBIRRS = Bellazzini, Berman, Isabella, Riva, Romano, Sciotti 2025/26; FRS = Fernandez,
Ruhdorfer, Serra 2026. Seiten sind gedruckte Seitenzahlen.

### Kurzfazit (10 Zeilen)

1. **Ausgang nach der Scheiterregel: "nur mit neuer Annahme".** Die D = 4-Lage bleibt bedingt, wie im Nachtrag.
2. **Externe Gravitonen traegt der Rahmen, und das ist schon benutzt:** FRS (arXiv:2603.15755v2, Anh. F, S. 46-47 [A]) schreiben IR-endliche Summenregeln mit A_E fuer die Vier-Graviton-MHV-Amplitude und begrenzen g4 (C^4) mit log(q/E). Die Bausteine stehen in BBIRRS [A]: masselose Soft-Faktoren ohne kollineare Divergenz (S. 6), harter Hamiltonian mit h = +-2 (S. 10).
3. **Den Dreipunkt-Vertex g^3 traegt das bisher nicht.** CHLPSD gewinnen die g^3-Schranke aus den spin-2/3-Regeln mit Graviton-Pol und der Ableitung der spin-4-Regel (Gl. 2.31-2.32, 3.3a [A]). FRS haben davon nur den spin-4-Teil in A_E-Form; dort steht g3^2 im t-Glied (S. 33, Gl. 4.39 [A]). Die spin-2/3-Regeln mit Pol fehlen in A_E-Form.
4. **Die neue Annahme betrifft die Ordnung in G, nicht Kreuzung oder Helizitaet.** Jeder g^3-Beitrag traegt einen Faktor G (CHLPSD Gl. 2.7a-c [A]). M_E ist aber nur in fuehrender Ordnung in G bei festem G_E unitaer, Schranken gelten "+ O(GM^2)" (BBIRRS Gl. 4.6, 5.17, S. 11, 18 [A]). Fuer eine scharfe Schranke wie Gl. 4.4 braucht es eine von zwei Zusatzannahmen, die BBIRRS selbst nennen: "the high-energy amplitude is well approximated by a meromorphic function", ausdruecklich "stronger than simply assuming a weakly-coupled UV completion" (S. 13, 30); oder Unitaritaet eine Ordnung weiter, als "future work" offen (S. 30).
5. **Schon gerechnet?** g4 mit externen Gravitonen: ja (FRS 2026). g^3 mit M_E: nach Recherchestand nicht belegt. Gesucht habe ich nur in den INSPIRE-Zitaten beider Arbeiten (alle 23 bzw. die neuesten 80 von 195, nach Abstracts) und in einem Volltext, ohne Websuche.
6. **Fehlende Rechnung, als Karte:** die spin-2/3-Summenregeln der Vier-Graviton-MHV-Amplitude (B2, B3, mit Graviton-Pol) in M_E-Form. Dazu gehoeren ein Fehlerbudget der O(G)-Reste und eine Definition der Spin-4-Luecke ohne das Mehrgraviton-Kontinuum.
7. Selbstanzeigen S1-S6 unten. Einfach gesagt am Ende.

### Pflicht-Tabelle: Annahmen und Observablen fuer externe Gravitonen (Vorgabe Codex-Lesung)

| Zeile | CHLPSD (harter Schnitt m_IR) | M_E (BBIRRS; FRS fuer Gravitonen) | fuer Gravitonen in M_E |
|---|---|---|---|
| Asymptotische Zustaende | Gravitonen, Baumniveau, "neglect loops within the EFT" (S. 5 [A]); D = 4 nur mit m_IR (S. 16 [A]) | harte Zustaende mit abgespaltenem Weinberg-Faktor, Gl. 2.4, 3.8; masselose Aeussere: Gl. 3.7, "no collinear singularity arises in gravity" (S. 6 [A]); harter Hilbertraum mit "physical helicity modes h = +-2" (S. 10 [A]); FRS Gl. F.1 fuer vier masselose Aeussere (S. 46 [A]) | **vorhanden** |
| IR-sichere Groesse | Funktional von m_IR bis M, psi ~ 65 p bei p -> 0, Gl. 3.3a (S. 16 [A]) | Funktionale "int_E^qmax dq psi(q) Im M_E" mit "psi(q) -> q as q -> 0", Gl. 4.9-4.10 (S. 12 [A]); FRS "p in [E, q]" (S. 47 [A]) | **vorhanden** (gleiche Funktionalklasse); fuer spin-2-Graviton-Regeln **nicht ausgeschrieben** |
| Unitaritaet inkl. Reste | Partialwellen 0 <= Im a <= 1 bzw. 2, Gl. 2.13-2.15 (S. 7 [A]); Gl. 3.4a braucht nur die Diagonale (S. 12, 16 [A]); 4.4 nimmt Matrix-Dichten (Anh. C, txt Z. 2281-2312 [A]) | harte Amplitude exakt unitaer, auch mit harten Gravitonen (S. 10-11 [A]); M_E nur fuer M^(0)(G_E), Gl. 4.6 mit "⪰ 0" (S. 11 [A]); Reste O(GM^2), Gl. 5.17 (S. 18 [A]); Negativitaet grosser l "O(G) ... parametrically subleading" (S. 30 [A]); FRS setzen Gl. 4.10 einfach an (S. 25, 29 [A]) | fuehrende Ordnung **vorhanden**; fuer g^3 **nur mit neuer Annahme** (Ordnung G, siehe Kurzfazit 4) |
| Kreuzung | Summenregeln mit gleichen Kopplungen in mehreren Regeln, "this reflects crossing symmetry" (S. 12 [A]) | "Crossing symmetry is manifest" ueber skalare W_ij (S. 7 (c) [A]); "Lorentz (little-group) covariance" (S. 7 (b) [A]) | **vorhanden, formal**; fuer Helizitaetsamplituden nicht eigens gezeigt. [ES] W ist skalar, die Helizitaetsstruktur bleibt die der vollen Amplitude |
| Regge, Dispersion | verschmierte Schranke Gl. 2.22-2.23 als Annahme, helizitaetsabhaengig Gl. 2.25 (S. 9-10 [A]) | Gravitation: aus Haering/Zhiboedov [100] bei eps > 0 plus Eikonal, Gl. 3.9-3.12, "only in the scaling limit" (S. 7-8 [A]); FRS: "given the assumed Regge behaviour" (S. 25 [A]) | **vorhanden mit Vorbehalt**: [100] gilt fuer d > 4; 4D-Helizitaeten in d Dimensionen nehmen FRS ohne Begruendung an (S. 29 [A], G2) |
| Abbildung der kubischen Kopplung | g^3 = alpha3 + i alpha~3 (Gl. 2.11, S. 6 [A]); -B2 = 16 pi G/p^2 + 2 pi G|g^3|^2 p^6 (Gl. 2.31a, S. 11 [A]); -B4 = 2 g4 + (4 pi G|g^3|^2 + g5) p^2 (Gl. 2.32a, S. 12 [A]) | BBIRRS: keine Graviton-Wilsonkoeffizienten. FRS: g3 nur in (g3^2/M_Pl^2 + g5/2) t der spin-4-Regel (Gl. 4.39, S. 33 [A]); keine g3-Schranke | **fehlt.** [ES] Der Pol wird in M_E zu G_E verstaerkt; der g^3-Term bleibt O(G) und liegt damit in der Groessenordnung des unkontrollierten Rests |
| Deutung der Hoeherspin-Spektralskala | M = Masse des leichtesten Zustands mit Spin >= 4; "States with spin greater than two are genuinely gravitational, and assumed to have mass above the cutoff, m > M" (S. 5 [A]); Zweiteilchen-Zustaende zugelassen (S. 25, 34; [A] laut LESUNG-LETZTE-SCHICHT, hier nicht neu gelesen) | Zwischenzustaende X ohne weiche Gravitonen (S. 11 [A]); in fuehrender Log-Ordnung treten G_E^2-Schleifenterme auf (BBIRRS Gl. 7.4, S. 27 [A], Pion-Fall) | **fehlt.** [ES] Harte Mehrgraviton-Zustaende mit J >= 4 gibt es bei jeder Energie; M muss nach Abzug des EFT-berechenbaren Teils definiert werden. Das tut keine gelesene Quelle |

### Erwartungsverstoesse (das Wichtigste zuerst)

**V1 (gross): M_E ist schon auf externe Gravitonen angewandt, nur nicht auf g^3.** Erwartet hatten die Karte ("Gerechnet ist
das bisher nur fuer Pionen mit Photon und Graviton"), SPIN2-D4 (R11, E13) und meine E3/E5(c): keine Anwendung auf Gravitonen.
Gefunden habe ich FRS 2026, Anh. F (S. 46-47 [A]): A_E nach BBIRRS, Vier-Graviton-MHV-Summenregel, Schranke Gl. F.10 auf g4 mit
log(q/E). Im Abstract steht davon nichts. ~~Mein Abstract-Filter haette die Arbeit uebersehen; gefunden habe ich sie ueber das
Stichwort "three-point" und den Volltext.~~ (berichtigt beim Rueckwaertslesen: Der Filter zeigte die Arbeit, schon im
E3-Durchgang. Aus dem Abstract ist die A_E-Anwendung aber nicht zu erkennen; SPIN2-D4 R2 hatte die Arbeit danach als "betrifft
fuehrende (quartische) Operatoren, nicht direkt g^3" abgelegt. Erst der Volltext zeigte Anh. F.) Korrigierte Erwartung: Die Frage "laesst der Rahmen Gravitonen zu" ist fuer die
MHV-Amplitude praktisch entschieden. Offen ist nur der Vertex.

**V2 (gross): Das Hindernis ist die Ordnung in G, nicht Helizitaet 2.** Die Karte vermutete (55 %), dass Unitaritaet oder Kreuzung
"fuer Helizitaet 2 mit Detektormittelung" eine Zusatzannahme brauchen. Gefunden habe ich anderes. Helizitaet 2 ist eingebaut
(S. 10 [A]), und Kreuzung folgt ueber skalare Faktoren (S. 7 [A]). Der Engpass liegt woanders: Alle g^3-Terme tragen G
(CHLPSD 2.7a-c [A]), M_E ist aber nur bis auf O(GM^2) kontrolliert (Gl. 5.17 [A]). Die beiden Auswege nennen BBIRRS selbst
(S. 13, 30 [A]). Korrigierte Erwartung: Ausgang "nur mit neuer Annahme" wie vorhergesagt, aber die Annahme ist eine
UV-Annahme (meromorphe Amplitude) oder eine Unitaritaetsaussage eine Ordnung weiter.

**V3 (mittel): BBIRRS schliessen masselose Aeussere nicht aus, sie bauen sie fuer Gravitation ein.** Erwartet (E1a, 60 %):
Massenpflicht wegen kollinearer Divergenzen. Gefunden: Die Massenpflicht gilt nur fuer QED ("massive charged particles",
S. 7, 13 [A]). Fuer Gravitation stehen der masselose Soft-Faktor (Gl. 3.7) und das Eikonal "considering neutral massless
particles" (Gl. 4.12, S. 12 [A]) ausdruecklich da.

**V4 (mittel): Die explizite CHLPSD-Schranke braucht keine Matrix-Positivitaet.** Erwartet (E2b): Matrix ueber
Helizitaetskanaele. Gefunden: Gl. 3.4a nutzt "only B^(1) ... MHV" und zwei positive Diagonal-Dichten (S. 12, 16 [A]); nur die
optimale 4.4 nimmt Matrix-Dichten (Anh. C [A]). Fuer eine erste M_E-Fassung reicht also die MHV-Amplitude, und die hat FRS
schon in M_E-Form fuer die spin-4-Regel.

**V5 (klein): Bei FRS treibt g3 nichts.** Erwartet (E5a): g3 treibt den negativen Lauf von g4. Gefunden: "they do not because of
helicity selection rules [40]" (S. 9 [A]); Treiber sind Skalare mit sigma-C^2-Kopplung.

**V6 (klein): Regge wird fuer Gravitation hergeleitet, nicht gesetzt.** Erwartet (E1d): Annahme. Gefunden: aus [100] bei
eps > 0 plus Eikonal (S. 7-8 [A]). Fuer QED angenommen (Gl. 3.15 [A]).

Bestaetigt (je eine Zeile): E1(b) Unitaritaet nur fuehrend im Skalierungslimes; E1(e) Abschn. 7 nur Pionen; E2(a) alle
g^3-Terme mit G; E2(c) Funktionale ab m_IR mit psi ~ p; E3 23 Zitate, keine M_E-Anwendung auf g^3; E5(b, d) FRS nur g4,
keine Spin-4-Aussage; E6/G1 FRS setzen Partialwellen-Unitaritaet an, ohne eigene Aussage fuer A_E.

### Vorab gegen Ausgang

| Erwartung (Zeit) | Wortlaut kurz | Ausgang |
|---|---|---|
| Karte (vor 21:28) | "nur mit neuer Annahme", Grund Unitaritaet/Kreuzung fuer Helizitaet 2, ~55 % | **Ausgang getroffen, Grund teilweise verfehlt** (V2): Unitaritaet ja, aber wegen der Ordnung in G, nicht wegen Helizitaet 2; Kreuzung kein Hindernis |
| Karte | "ja, direkt" ~20 %, "nein" ~25 % | beides nicht eingetreten |
| Karte | g^3-Schranke mit M_E bis 10/2026 gerechnet, ~15 % | nach Recherchestand nicht belegt; Nachbarfall g4 gerechnet (V1) |
| E0 (21:28:37) | letzte Schicht nannte "Bellazzini widerlegt CHLPSD" ueberzogen | teilweise verletzt (klein): ueberzogen waren "Regime B im Ergebnis", "physikalisch ununterscheidbar", Literaturbreite, Einheit von G_E |
| E1 (21:30) | (a) Gravitonen ausgeschlossen, (b) Unitaritaet nur fuehrend, (c) Kreuzung nur Skalare, (d) Regge gesetzt, (e) nur Pionen | (a) verletzt (V3), (b) bestaetigt, (c) teilweise verletzt, (d) teilweise verletzt (V6), (e) bestaetigt |
| E2 (21:35:30) | (a) alles O(G), (b) Matrix-Positivitaet, (c) Schnitt als untere Grenze, (d) Regge-Annahme | (a), (c), (d) bestaetigt; (b) teilweise verletzt (V4) |
| E3 (21:37) | Bellazzini-Zitate: keine M_E-Anwendung auf Gravitonen | fuer g^3 bestaetigt; fuer Gravitonen ueberhaupt durch R5 verletzt (V1), weil FRS darunter ist |
| E4 (21:37) | CHLPSD-Zitate: keine IR-sichere 4.4 | bestaetigt (nur Abstracts, neueste 80 von 195) |
| E5 (21:38) | FRS: g3 treibt Lauf; nur g4; M_E nur zitiert; keine Spin-4-Aussage | (a) verletzt (V5), (b) bestaetigt, (c) verletzt (V1), (d) bestaetigt |
| E6 (21:40) | FRS uebernehmen keine Unitaritaetsgarantie fuer A_E | bestaetigt |

### Weg und fehlende Rechnung (fuer die Leitung; alles hier ist [ES], keine Quelle rechnet es)

- Ausgangspunkt waere FRS Anh. F (A_E fuer vier Gravitonen, Smearing p in [E, q]). Die spin-4-Regel B_0^4h mit
  (g3^2/M_Pl^2 + g5/2) t liegt dort schon vor (Gl. 4.39 [A]); sie entspricht dem Baustein d/dp^2 B4 in CHLPSD 3.3a. Zu
  ergaenzen waeren die spin-2/3-Regeln der MHV-Amplitude (CHLPSD B2^(1), B3^(1), Gl. 2.31), verschmiert ab E mit
  Funktionalen der Klasse psi ~ p (CHLPSD 3.3a).
- Ordnungszaehlung: Der Pol 16 pi G/p^2 gibt nach dem Smearing einen Term der Ordnung G log(M/E), also G_E. Der g^3-Term
  2 pi G|g^3|^2 p^6 bleibt O(G). Ohne Zusatzannahme kann die Rechnung deshalb hoechstens eine Schranke in fuehrender
  Log-Ordnung liefern, |g^3|^2 M^8 <= c log(M/E) + O(1). Die Konstante -27,6 aus Gl. 4.4 liegt dann im unkontrollierten
  Rest. Das ist eine Zaehlung, keine Rechnung.
- Scheiterregel fuer die Folgekarte: Bleiben die nicht log-verstaerkten Ein-Schleifen-Reste des B2-Smearings O(G), dann
  steht die Schranke in fuehrender Log-Ordnung ohne neue Annahme. Tragen sie selbst ein log(M/E), etwa aus den
  Doppel-Logs in FRS Gl. F.3, dann haengt auch der fuehrende Koeffizient an Termen, die M_E nicht kontrolliert, und die
  Lage bleibt "nur mit neuer Annahme".

### Unterscheidungspunkte

- **U1 (traegt M_E g^3 oder nicht):** Die Lesarten trennen sich nur, wo |g^3|^2 M^8 von der Ordnung log(M/E) ist, also am Rand
  des CHLPSD-Gebiets. Fuer |g^3|^2 M^8 = O(1) liegt der g^3-Term im Rest, und keine der beiden Lesarten sagt etwas
  [ES]. Entscheiden kann das die fehlende Rechnung oben, keine Messung.
- **U2 (CHLPSD mit m_IR gegen M_E mit E):** Sie unterscheiden sich (i) in der Konstante und den O(G)-Resten und (ii) dort, wo
  G_E = G M^2 log(M/E) nicht mehr klein ist. Dort endet die Kontrolle von M_E; die Baumformel von CHLPSD laesst sich weiter
  hinschreiben, ist aber nach BBIRRS S. 30 [A] wertlos. Eine Messung, die (i) oder (ii) trennt, kann ich nicht nennen. Das ist
  keine Aussage "physikalisch ununterscheidbar" (Codex-Auflage), sondern: nicht gefunden.

### Gegensweep (Arbeitsfeld G1-G4)

1. G1 **geprueft:** FRS setzen Partialwellen-Unitaritaet bei fester Ordnung an (S. 25, 29 [A]) und uebernehmen A_E nur "in
   the limit considered in [41]" (S. 46 [A]). V1 zeigt also, dass die Form uebertragbar ist. Dass die Unitaritaetsgarantie
   fuer externe Gravitonen gilt, zeigt sie nicht.
2. G2 nicht geprueft: Vertraeglichkeit der Dimensionsregularisierung (eps > 0) mit 4D-Helizitaeten; FRS nehmen sie an (S. 29).
3. G3 nicht geprueft: IR-sichere g^3-Schranken auf anderen Wegen ohne Zitat von BBIRRS/CHLPSD (Energiekorrelatoren 2512.23791,
   Coulomb-Moden 2606.19432, DWPT 2609.16896, de Sitter). Ohne Websuche bleibt das offen.
4. G4 nur [ES]: Ob BBIRRS' Zaehlung "c M^2n << G_E" (S. 27) sich auf Graviton-Koeffizienten uebertragen laesst, steht nirgends.

### Kalibrierung

- (a) Gemessen: nichts. Diese Runde ist reine Theorie-Lage.
- (b) Nuetzlich verdichtet: die Pflicht-Tabelle und die Ordnungsfrage. Der Engpass ist O(G) gegen O(G_E), nicht Helizitaet.
- (c) Gewachsene Gewissheit ohne neue Evidenz: Nach Z-1 stieg meine Sicherheit fuer "Gravitonen formal zugelassen". Die
  Evidenz dafuer lieferte erst R5 (FRS). Die Sicherheit fuer "g^3 nicht gerechnet" ist schwach, weil der Fund FRS gezeigt hat,
  dass Abstract-Filter Anwendungen in Anhaengen uebersehen.

### Quellenliste (Lesetiefe, sha256)

| Quelle | URL | Tiefe | sha256 |
|---|---|---|---|
| Bellazzini, Berman, Isabella, Riva, Romano, Sciotti, Positivity with Long-Range Interactions, v2 (2026) | https://arxiv.org/abs/2512.13780 | [A] S. 1-18, 27-32, Lit. [31], [39], [41], [69], [100] | PDF 2050cd823fd459614bc69344b628a9238d3b7596ea5dc799c939f4720ecf8104; txt 8ca07766e5cfb52e074781cb0607138bb62cf963d00d292ca582d86f2a8fe0cf (beide RUNDE-13/spin2-d4/quellen/) |
| Caron-Huot, Li, Parra-Martinez, Simmons-Duffin, Causality constraints on corrections to Einstein gravity, JHEP 05 (2023) 122 | https://arxiv.org/abs/2201.06602 | [A] S. 5-7, 9-13, 15-17, 26-27; Anh. C nur txt Z. 2281-2312 | PDF 86365bcb25e81c062dbbdb14ff3a2ff454f4f33ea94efec79c4323e31bfc53d4; txt f56c588bb7225c67a4d02fd2eba3b77e17653265bb69d8e3a9c14e2252b4ab42 (spin2-d4/quellen/) |
| Fernandez, Ruhdorfer, Serra, Negative running of gravitational positivity, v2 (13.04.2026) | https://arxiv.org/abs/2603.15755 | [A] S. 1-3, 9 (Abschn. 2.3), 25, 28-30, 33-34, 46-47; Gl. 4.39 und 4.41 am PDF-Bild geprueft | PDF 49231977859b3ac1b07a4788c0729d47cb529ed123f56230ef6f8112705453d2; txt 0cdd2fc79f6244ea787775bbe7afd72a161b5881554d0c68cf79b85d37766918 (spin2-d4-2/quellen/) |
| INSPIRE refersto:recid:3093263 (= 2512.13780), 23 Treffer, mostrecent | https://inspirehep.net/api/literature?q=refersto%3Arecid%3A3093263 | [S] Titel und Abstracts | 98eeffffddf19b16c6b683daa902c47487404232030ac67710f5d48db3c1d164 |
| INSPIRE refersto:recid:2012035 (= 2201.06602), 195 Treffer, neueste 80 | https://inspirehep.net/api/literature?q=refersto%3Arecid%3A2012035 | [S] Titel und Abstracts | 2536d06df3a83ec1155eac89b68260f0ce5de72ebb41c56731fcaab7a15f4c43 |
| Calisto, Cheung, Remmen, Sciotti, Tarquini 2026, The Equivalence Principle at High Energies Completes the Spectrum | https://arxiv.org/abs/2605.20319 | [S] (INSPIRE-Abstract) | in insp-bell-r3.json |
| Berman, Aspects of the Perturbative S-matrix Bootstrap (Dissertation 2026) | INSPIRE, ohne arXiv-Nummer | [S] | in insp-bell-r3.json |
| Haering, Zhiboedov, Gravitational Regge bounds (BBIRRS [100]) | https://arxiv.org/abs/2202.08280 | nur ueber BBIRRS S. 7 und SPIN2-D4 R10 [A dort] | spin2-d4/quellen/ |

### Selbstanzeigen

- **S1:** Zwei Eintragszeiten im Arbeitsfeld waren geschaetzt ("21:37" bei R1/Z-1, "21:41" bei R2), gemessen waren
  21:35:14 und 21:36:48. Beide sind durchgestrichen und berichtigt. Danach habe ich jede Zeit per date in die Zeile geschrieben.
- **S2:** Eine falsche Nebenangabe: "Serra ist Coautor von [43]". Dort steht F. Serra, bei FRS J. Serra. Durchgestrichen und
  berichtigt; fuer den Befund ohne Belang.
- **S3:** Meine INSPIRE-Auswertung war ein Abstract-Filter. FRS stand in beiden Trefferlisten. Gelesen habe ich die
  Arbeit erst, weil das Abstract "three-point" und "gravitons" enthaelt; Anhang F steht dort nicht. "g^3 nicht gerechnet"
  gilt deshalb nur fuer den Suchstand. Andere Arbeiten koennten A_E ebenso in einem Anhang verwenden.
- **S4:** Die INSPIRE-Abfragen liefen ueber refersto:recid statt refersto:arxiv wie in der Auftragsnachricht, weil die
  arxiv-Syntax in SPIN2-D4 (S3) 141444 Treffer gab. Die recid-Zuordnung stammt aus SPIN2-D4 R3/R11.
- **S5:** Die Ordnungszaehlung ("Weg und fehlende Rechnung", U1, Tabelle Zeile "Abbildung") ist mein Schluss [ES], keine
  Rechnung. Ins Kurzfazit ist sie nur als benannte Luecke eingegangen, nicht als Ergebnis.
- **S6:** Werkzeuge: nur WebFetch (eine PDF-Binaerablage), INSPIRE-API per curl, pdftotext, grep, sed, jq, sha256sum, date,
  Read mit Seitenangabe. Kein python, kein awk, kein git, kein Peerbus, keine Unteragenten, keine Websuche. Geschrieben nur in
  RUNDE-13/spin2-d4-2/. Gesperrte Pfade habe ich nicht gelesen.

### Einfach gesagt

Die Frage war, ob eine neue Rechenmethode der Bellazzini-Gruppe auch fuer Gravitonen funktioniert. Die Methode umgeht das
Problem, dass in vier Dimensionen manche Rechnungen bei sehr grossen Abstaenden unendlich werden, und zwar mit einem Detektor
von endlicher Groesse. Fuer gewoehnliche Gravitonen hat eine andere Gruppe das 2026 schon gemacht. Fuer die besondere
Dreifach-Kopplung, um die es uns geht, hat es nach unserem Suchstand noch niemand gerechnet. Der Grund: Ihr Beitrag ist so
klein, dass er im Rest verschwindet, den die Methode nicht im Griff hat. Man braucht also entweder eine zusaetzliche
Annahme oder eine genauere Methode. Deshalb bleibt die Verbindung in vier Dimensionen vorerst eine Folgerung mit Bedingung.

---

## ARBEITSFELD

### Offene Rueckfragen (wandern mit)

- R1: Laesst der M_E-Rahmen externe Gravitonen (Helizitaet +-2) zu?
- R2: Was fehlt fuer eine g^3-Schranke wie CHLPSD Gl. (4.4) ohne harten IR-Schnitt?
- R3: Hat jemand bis Okt. 2026 das schon gerechnet (INSPIRE refersto 2512.13780 und 2201.06602)?

### Protokoll der Abrufe (Erwartung vor Abruf, mit date)

- E0 (2026-10-01 21:28:37 CEST), interne Lektuere SPIN2-D4.md, LESUNG.md, LESUNG-LETZTE-SCHICHT.md:
  Erwartung: SPIN2-D4 haelt D = 4 fuer "bedingt"; die Bedingung ist der harte IR-Schnitt (impact-parameter-Schnitt
  b_min bzw. Smearing ueber p <= M) bei CHLPSD; Bellazzini S. 30/31 wird als Kritik plus Alternative gelesen; die
  letzte Schicht hat vermutlich die Aussage "Bellazzini widerlegt CHLPSD" oder "M_E loest D = 4" als ueberzogen
  markiert.
- E0-Befund (Eintrag 21:30): **teilweise verletzt (klein).** Als ueberzogen galten nicht "Bellazzini widerlegt CHLPSD",
  sondern (Codex LESUNG Kopf, Abschn. 4, 5; LETZTE-SCHICHT B9): "Regime B im Ergebnis", "physikalisch ununterscheidbar",
  "noch nicht durchgerechnet" als Literaturaussage, und die Einheit G_E = G log(M/E) (Codex: G_E = G M^2 log(M/E), Gl. 1.1).
  Fuer diese Runde wichtig aus Codex Abschn. 2: "S. 17-18 gibt endliche Aufloesungsschranken mit kontrollierten O(GM^2)-Resten;
  Unitaritaet wird im Detektorskalierungslimes begruendet. Endliches E allein ist nicht der ganze Annahmensatz." und Abschn. 5:
  "Ein blosser Ersatz m_IR -> E ist keine Herleitung." -> Diese Runde darf nicht "m_IR -> E" als Ergebnis ausgeben.

- E1 (2026-10-01 21:30 CEST, date oben 21:29:49), lokaler Volltext Bellazzini 2512.13780v2.txt, Abschn. 1-5, 7, 8
  (Gliederung: 2 Stripped and Hard Amplitudes, 3 Analytic Stripped Amplitudes, 4 Unitarity, 4.4 Faddeev-Kulish,
  5 Dispersion Relations, 7 Positivity Bounds with Gravity, 8 Summary):
  Erwartung:
  (a) Die Konstruktion (Soft-Exponential abspalten, "stripped" Amplitude) ist aus Weinbergs universellen Soft-Faktoren
      gebaut und haengt nur von Impulsen/Ladungen der externen Linien ab; formal also auch fuer masselose externe Linien
      mit Helizitaet, aber die Autoren schreiben ausdruecklich massive bzw. pionartige externe Zustaende
      (m > 0) vor, weil masselose externe Teilchen kollineare Divergenzen bringen (Abschn. 4.3 "Collinear enhancements").
      ~60 %, dass externe Gravitonen ausdruecklich ausgeschlossen oder als "future work" genannt sind.
  (b) Unitaritaet nur bis auf O(G M^2)- bzw. O(G_E)-Reste und nur im Grenzfall E -> 0 mit festem G_E (Detektorskalierung).
  (c) Kreuzung: fuer die stripped Amplitude bewiesen fuer skalare externe Teilchen (s-u-Kreuzung), Helizitaet nicht behandelt.
  (d) Regge-Annahme: wird fuer M_E bzw. stripped Amplitude gesetzt (|M| < s^2 fuer feste t), nicht hergeleitet.
  (e) Abschn. 7 Gravitation: Schranke auf Pion-Koeffizienten g2 mit Graviton-Austausch; kein R^3, kein Spin-4.

- **R1 (Eintrag ~~21:37~~ 21:35, date davor 21:35:14; "21:37" war geschaetzt, Selbstanzeige S1) Bellazzini, Berman, Isabella, Riva, Romano, Sciotti, arXiv:2512.13780v2, lokaler Text
  RUNDE-13/spin2-d4/quellen/2512.13780v2.txt (sha256 8ca07766...e0cf; PDF 2050cd82...4f2a), gelesen S. 1-18, 27-32.
  Seiten = gedruckte Seitenmarken (Seite N = Text zwischen Marke N-1 und N). [A]** Befund gegen E1:
  - (a) **VERLETZT (gross) -> Z-1.** Kein Ausschluss externer Gravitonen, kein "future work" dazu. Stattdessen:
    - S. 6, Gl. (3.7): Soft-Exponential fuer m_i = m_j = 0 ausdruecklich angegeben; "the mu^2 within the logarithm cancels
      in the product ... due to momentum conservation, ensuring that no collinear singularity arises in gravity - in
      contrast with the QED expression (3.5)".
    - S. 7 (a): "as long as we work with massive charged particles, collinear singularities are also absent" und S. 13
      (4.3): "When the charged particles carry a finite mass (as we assume here)" - die Massenbedingung betrifft QED.
      S. 13: "There are no collinear divergences instead in gravity".
    - S. 10: "Everything said for QED carries over to gravity: one may start from a fully gauge-fixed Hamiltonian where
      only the physical helicity modes h = +-2 propagate with positive norm". S. 10-11: S_E^hard unitaer, "the identity is
      restricted to hard photons and gravitons"; S. 11: "the unitarity of hard amplitudes is an exact statement, and does
      not rely on the scaling limit (1.1) - it is only the connection with M_E that does."
    - S. 12, Gl. (4.12): Eikonal-Imaginaerteil "in the presence of gravity (considering neutral massless particles for
      simplicity)".
    - S. 7 (b): "Lorentz (little-group) covariance. This follows immediately, since W_ij is a Lorentz scalar."
    - Aber: Alle ausgefuehrten Beispiele sind Pionen (S. 2, Abschn. 6-7); externe Gravitonen werden nirgends
      ausgeschrieben (grep "four-graviton"/"graviton scattering": nur Literaturtitel).
  - (b) **bestaetigt**: Unitaritaet von M_E nur fuer M^(0)(G_E), fuehrend in G bei festem G_E (S. 10, Gl. 4.1-4.2;
    S. 11 Gl. 4.6; S. 12 Gl. 4.10 mit "psi(q) -> q as q -> 0"). Schranken: "A_n[psi, M_E](G_E, G) + O(GM^2) >= 0" (S. 18,
    Gl. 5.17). Negativitaet aus grossen l: "finite, scale as O(G) ... parametrically subleading" (S. 30).
  - (c) **teilweise verletzt**: Kreuzung allgemein ueber die skalaren Faktoren W_ij begruendet (S. 7 (c)), nicht nur
    fuer Skalare; fuer Helizitaetsamplituden nicht ausgeschrieben.
  - (d) **teilweise verletzt**: Fuer Gravitation wird Regge nicht gesetzt, sondern aus Haering/Zhiboedov [100] bei
    eps > 0 (D = 4 + 2 eps!) plus Eikonal hergeleitet (S. 7-8, Gl. 3.9-3.12), "only in the scaling limit" (S. 8). Fuer
    QED angenommen (Gl. 3.15).
  - (e) **bestaetigt**: Abschn. 7 nur pi0 pi0 mit Graviton, Schranken (7.5)-(7.7) auf c2,0 und c3,1 (S. 27-28).
  - Zusatz, nicht vorhergesagt: S. 30: "Remarkably, subleading tree-level O(alpha, G) contributions can also be controlled
    quantitatively, provided one assumes more about the UV completion. If the UV remains in a tree-level regime - namely,
    the high-energy amplitude is well approximated by a meromorphic function ... or weakly-coupled stringy gravitational
    completions [2] - ... the tree-level O(alpha, G) terms remain under control. This is stronger than simply assuming a
    weakly-coupled UV completion ... It is really an assumption about the leading analytic structure of the amplitudes."
    Ebenso S. 13 (Ende 4.2). S. 30: "control unitarity to subleading order in the scaling limit ... something we hope to
    explore in future work"; S. 32: "future challenge ... corrections beyond the leading-log approximation".
  - S. 27: "we restrict our analysis to the configuration of couplings satisfying c_n,k M^2n << G_E" (Pion-Gravitation).
- **Analysezyklus Z-1 (Eintrag ~~21:37~~ 21:35, date davor 21:35:14; "21:37" war geschaetzt, Selbstanzeige S1) - warum der Rahmen Gravitonen formal zulaesst, die g^3-Schranke aber nicht direkt:**
  - [ES] Die Bausteine fuer externe Gravitonen stehen da (masselose Soft-Faktoren, Hard-Hamiltonian mit h = +-2,
    exakte Hard-Unitaritaet, kreuzungsfeste skalare W_ij, Regge ueber [100] und Eikonal). Formal: **zugelassen**.
  - [ES] Aber: In reiner Graviton-Streuung ist jede Selbstkopplung O(G), auch der R^3-Austausch (CHLPSD: Vorfaktor 8 pi G
    bzw. G|g^3|^2, S. 6-7, noch zu pruefen in R2). Kontrolliert ist in M_E nur M^(0)(G_E), also fuehrende Ordnung in G bei
    festem G_E; der Rest ist "+ O(GM^2)" (Gl. 5.17). Eine g^3-Schranke vergleicht aber O(G)-Groessen: g^3-Terme gegen den
    (log-verstaerkten) Graviton-Pol. Damit liegt g^3 im unkontrollierten Rest, **ausser**
    (i) mit Bellazzinis Zusatzannahme "UV im Baumregime, meromorph" (S. 13, 30), die O(G)-Baumterme kontrolliert, oder
    (ii) in einer Doppelskalierung |g^3|^2 M^8 ~ log(M/E): dann ist der |g^3|^2-Term von der Ordnung G_E und wird
    fuehrend; die Schranke gaelte dann nur in fuehrender Log-Ordnung (Koeffizient des log, nicht die Konstante -27,6).
    (ii) steht nirgends in der Literatur, die ich gelesen habe; es ist mein Schluss nach dem Muster von S. 27.
  - Korrigierte Erwartung: Ausgang "nur mit neuer Annahme" wird wahrscheinlicher, aber aus einem anderen Grund als die
    Karte vermutet: nicht Kreuzung oder Unitaritaet fuer Helizitaet 2, sondern die **Ordnung in G**, in der g^3 sitzt.

- E2 (2026-10-01 21:35:30 CEST, date davor 21:35:22), lokaler Volltext CHLPSD 2201.06602.txt, Abschn. 2 (Amplituden), 2.3
  (Annahmen), 3.1-3.2 (Summenregeln, IR), 4.1 (Gl. 4.4): Erwartung:
  (a) Alle Niedrigenergie-Koeffizienten der Vier-Graviton-Amplitude tragen einen Faktor G (8 pi G/(stu), G|g^3|^2, g4 ~ G/M^4);
      g^3 steht linear in den helizitaetsverletzenden Amplituden und quadratisch in der MHV-Amplitude f(s,u).
  (b) Gl. 4.4 braucht eine Matrix-Positivitaet ueber Helizitaetskanaele (Spektraldichten als positive 2x2-Matrizen), also
      Unitaritaet mit Nicht-Diagonalelementen.
  (c) Der IR-Schnitt sitzt in der unteren Grenze der p-Integration (p >= m_IR) der Funktionale; die Funktionale gehen
      bei p -> 0 wie p (wie Bellazzinis psi(q) -> q).
  (d) Regge: verschmierte Schranke als Annahme (Gl. 2.22-2.23), gestuetzt auf Kausalitaet; fuer D = 4 nicht bewiesen.

- **R2 (Eintrag ~~21:41~~ 21:36, date davor 21:36:48; "21:41" geschaetzt, Selbstanzeige S1) CHLPSD, arXiv:2201.06602v1, lokaler Text RUNDE-13/spin2-d4/quellen/2201.06602.txt
  (sha256 f56c588b...ab42; PDF 86365bcb...53d4), S. 5-6, 11-13, 15-17, 26-27 (gedruckte Marken "- N -"). [A]** Befund gegen E2:
  - (a) **bestaetigt.** S. 5, Gl. (2.7a): f_low(s,u) = 8 pi G/(stu) + (2 pi G su/t)|g^3|^2 + g4 + g5 t + ... + O(loops);
    S. 6, Gl. (2.11): g4 = 8 pi G (alpha4 + alpha4'), "we absorbed a factor of 8 pi G in three-point couplings but not in
    four-point couplings". S. 5: "neglect loops within the EFT. States with spin greater than two are genuinely
    gravitational, and assumed to have mass above the cutoff, m > M."
    S. 11, Gl. (2.31a): -B2^(1)(p^2)|low = 16 pi G/p^2 + 2 pi G |g^3|^2 p^6 + O(matter and loops) -> der Graviton-Pol traegt
    1/p^2 (gibt das log), der g^3-Term nicht. S. 12, Gl. (2.32a): -B4^(1)|low = 2 g4 + (4 pi G|g^3|^2 + g5) p^2 + ...
  - (b) **teilweise verletzt.** Die explizite Schranke (3.4a) |g^3|^2 M^8 <= 37,8 log(M/m_IR) - 45,4 - F_matter (S. 17)
    braucht nur die MHV-Summenregel B^(1) ("These use only B^(1) (2.26): fixed-u dispersion relation for the MHV
    amplitude", S. 16) und nur Diagonal-Positivitaet (S. 12, Gl. 2.33: |c++|^2, |c+-|^2 >= 0). Die optimale (4.4) (S. 27)
    nimmt "all improved sum rules B2^imp and B3^imp with nmax = 6" und dazu Vorwaerts-Ableitungen von B4; dort sind die
    schweren Dichten Matrizen (Anh. C, txt Z. 2281-2312).
  - (c) **bestaetigt.** (3.3a), S. 16: Integral von m_IR bis M, Wellenfunktion p(1-p)^3(65 + ...), also ~ 65 p bei p -> 0;
    "Notice the lower cutoff m_IR makes the functionals infrared-safe." Dazu S. 16: "In principle the spin-4 sum rules
    should also be smeared to make them rigorously valid, but ... this is a technical modification, which we will ignore
    here."
  - (d) bestaetigt (wie SPIN2-D4 R1, S. 8-10).
- **[ES] Folge aus R1 + R2 (Eintrag ~~21:41~~ 21:36, geschaetzt, S1):** Die Funktionale von CHLPSD gehoeren zur selben Klasse wie Bellazzinis
  (psi ~ q bei kleinem q, untere Grenze statt q = 0). Formal entsteht die M_E-Fassung, indem m_IR -> E gesetzt wird. Das
  ist aber keine Herleitung (Codex). Massgeblich ist die Ordnung: Auf der rechten Seite steht 16 pi G x 65 log(M/E) ~
  G_E (fuehrend). Auf der linken Seite steht G|g^3|^2 M^8, und das ist O(G), solange |g^3|^2 M^8 = O(1). Der Rest
  "+ O(GM^2)" (Bellazzini Gl. 5.17) ist von derselben Ordnung wie die Konstante -45,4 bzw. -27,6. In fuehrender
  Ordnung bliebe hoechstens |g^3|^2 M^8 <= c log(M/E) + O(1) mit c aus dem Pol-Koeffizienten. Das ist eine Skizze,
  keine Rechnung, und sie gehoert nicht ins Kurzfazit.

- E3 (2026-10-01 21:37:04 CEST), INSPIRE refersto:recid:3093263 (= 2512.13780), sort=mostrecent, mit Abstracts:
  Erwartung: 23 bis 26 Treffer (SPIN2-D4 R11: 23 um 20:28 heute). Keine Arbeit wendet M_E auf Vier-Graviton-Streuung
  oder auf g^3 an (~85 %). Hoechstens eine Arbeit nennt externe Gravitonen mit M_E als Ausblick. Nach dem 20:28-Abruf
  heute keine neuen Eintraege.
- E4 (gleiche Zeit), INSPIRE refersto:recid:2012035 (= 2201.06602), sort=mostrecent, die neuesten 60 mit Abstracts:
  Erwartung: keine Arbeit leitet Gl. 4.4 IR-sicher (ohne m_IR) her (~85 %). Treffer mit "infrared"/"IR" im Abstract
  betreffen Skalare, Photonen oder D > 4. Hoechstens eine Arbeit mit D = 4 und Graviton-Streuung und einem neuen
  IR-Regulator (z. B. de Sitter, Eikonal).

- **R3/R4 (Eintrag 2026-10-01 21:38:06 CEST) INSPIRE, Ablage quellen/insp-bell-r3.json, quellen/insp-chlpsd-r4.json. [S]**
  - E3 **bestaetigt** (eine Zeile): 23 Treffer wie um 20:28; keine Arbeit wendet M_E auf Vier-Graviton-Streuung oder g^3 an.
    Naechstliegend nur 2605.20319 (Calisto u. a., Vollstaendigkeit aus Aequivalenzprinzip, Baumniveau), Berman-Dissertation
    (Coautor; "theories with long-range forces in four spacetime dimensions", nur Abstract).
  - E4 **im Kern bestaetigt, ein Kandidat offen:** 195 Zitate gesamt, die neuesten 80 mit Abstract gefiltert. Keine Arbeit
    leitet Gl. 4.4 IR-sicher her (nach Abstracts). Offener Kandidat: Fernandez, Ruhdorfer, Serra, arXiv:2603.15755
    "Negative running of gravitational positivity": D = 4, Gravitonen, "certain non-minimal three-point interactions induce a
    negative running", Schranken "accounting for graviton loops", "after smearing over the momentum transfer, are argued
    to dominate". Fuer Gravitonen ist die nichtminimale Dreipunktkopplung R^3 [ES]. -> Volltext R5.
    Reichweite: nur INSPIRE-Zitate der zwei Arbeiten (neueste 80 bzw. alle 23), nur Abstracts; keine Websuche.
- E5 (2026-10-01 21:38:06 CEST), Volltext Fernandez/Ruhdorfer/Serra 2603.15755 (PDF per WebFetch):
  Erwartung: (a) Fuer Gravitonen ist die nichtminimale Dreipunktkopplung g^3 (R^3); sie treibt den negativen Lauf des
  R^4-Koeffizienten g4 (beta ~ G |g^3|^2 ...). (b) Die Schranken sind fuer g4 (fuehrende Operatoren), nicht fuer g^3
  selbst. (c) IR-Behandlung: Verschmieren ueber q mit einer unteren Grenze (harter Schnitt oder E); M_E von Bellazzini
  wird zitiert, aber nicht als Werkzeug fuer externe Gravitonen ausgebaut (~65 %). (d) Keine Spin-4-Aussage.

- **R5 (Eintrag 2026-10-01 21:40:05 CEST) Fernandez, Ruhdorfer, Serra, "Negative running of gravitational positivity", arXiv:2603.15755v2 (13.04.2026),
  quellen/2603.15755v2.pdf (WebFetch-Binaerablage, pdftotext -layout). Gedruckte Seite N = PDF-Seite N+1; (4.39) am PDF-Bild geprueft. [A]**
  Befund gegen E5: **(c) VERLETZT (gross) -> Z-2**; (a) verletzt; (b), (d) bestaetigt.
  - **M_E ist auf externe Gravitonen schon angewandt**, Anh. F "IR-finite sum rules" (S. 46-47): "In [41] [= Bellazzini
    u. a. 2512.13780], analytic, crossing-symmetric, and Lorentz-invariant amplitudes free of gravitational soft divergences
    have been constructed, A_E = lim A/W" mit W fuer masselose Aeussere (F.1); (F.7) die Ein-Schleifen-GR-Beitraege zur
    Graviton-Dispersionsrelation B_0^4h mit log(-t/E^2); "After smearing the sum rules, in d = 4 dimensions yet with momentum
    transfer p in [E, q] ... we obtain IR-finite bounds on the running coefficient of the leading scalar, photon, and
    graviton EFT amplitudes", (F.10): g4(s) >= -8 zeta_h log(q/E)/(q^2 s (4 pi M_Pl)^2) + ... Grenzfall (F.4):
    M_Pl -> unendlich, E -> 0, s log(-t/E^2)/(4 pi M_Pl)^2 fest (wie Bellazzini Gl. 1.1).
  - Aber nur fuer **g4** (C^4, Vier-Graviton-MHV), und nur ueber die **spin-4-subtrahierte** Summenregel. S. 33, (4.39):
    M_Pl^4 B_0^4h|tree = g4 - (g3^2/M_Pl^2 + g5/2) t + O(t/M^2) -> g3 steht dort nur im t-unterdrueckten Glied; "in contrast
    with the scalar and photon cases, there is no gravitational term at tree level" (S. 33). Die spin-2-Summenregel mit
    Graviton-Pol, aus der CHLPSD die g^3-Schranke holen (CHLPSD 2.31a, 3.3a), wird fuer Gravitonen nicht aufgestellt.
  - (a) verletzt: g3 treibt den negativen Lauf nicht: Die Amplitude mit einer g3-Einsetzung "do not [contribute] because
    of helicity selection rules [40]" (Abschn. 2.3, txt Z. 549-553). Treiber fuer C^4 sind Skalare mit sigma C^2-Kopplung.
  - Hauptteil rechnet in d = 4 - 2 eps: "our bounds strictly apply only for eps != 0, or alternatively be interpreted
    qualitatively by keeping in mind that 1/eps can effectively be traded by a finite logarithm; see App. F" (S. 3, Fn. 1).
    S. 30: Dimensionsregularisierung statt "an IR cutoff on the range of momentum transfers, p > 1/m_IR [10, 18, 25]" hat
    "the advantage of preserving positivity at large impact parameters" ([18] = CHLPSD).
  - (d) bestaetigt: keine Spin-4- oder Hoeherspin-Aussage.
- **Analysezyklus Z-2 (gleicher Eintrag):**
  - Die Karten-Frage "Laesst der Rahmen externe Gravitonen zu?" ist durch eine Folgearbeit **praktisch beantwortet: ja,
    fuer die Vier-Graviton-MHV-Amplitude und g4**, mit derselben Gruppe im Umfeld (~~Serra ist Coautor von [43] Beadle u. a.~~ falsch: dort F. Serra, hier J. Serra; berichtigt 21:40;
    Bellazzini u. a. danken "Jaime Fernandez" und "Javi Serra", S. 32). Damit faellt mein Z-1-Vorbehalt "nirgends ausgeschrieben" fuer externe
    Gravitonen; er bleibt fuer g^3.
  - Was fuer g^3 fehlt, ist jetzt enger: die **spin-2-subtrahierten** Graviton-Summenregeln (B2, B3 mit 16 pi G/p^2-Pol und
    2 pi G|g^3|^2 p^6) in M_E-Form. Genau dort sitzt der log-verstaerkte Pol, der in M_E zu G_E wird, und genau dort steht
    g^3 nur in O(G). FRS umgehen das, weil fuer g4 die spin-4-Regel reicht.
  - Korrigierte Erwartung: "Hat das schon jemand gerechnet?" -> nach Recherchestand (INSPIRE-Zitate beider Arbeiten,
    Abstracts, ein Volltext): **g4 ja (FRS 2026, Anh. F), g^3 nein.** Mein E3-Filter (nur Abstracts) haette FRS uebersehen;
    gefunden nur ueber CHLPSD-Zitate und Volltext. Reichweite der Aussage "g^3 nein" ist damit schwach.

### Gegensweep (Eintrag 2026-10-01 21:40:47 CEST): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

- G1: Dass FRS mit "A_E" auch Bellazzinis **Unitaritaetsgarantie** uebernehmen. Bellazzini kontrolliert nur M^(0)(G_E);
  FRS vergleichen aber ein Baumniveau-g4 mit einem Ein-Schleifen-GR-Term, also Ordnungen jenseits von M^(0). Moeglich,
  dass FRS die UV-Positivitaet bei fester Ordnung einfach annehmen. -> **wird geprueft (E6).**
- G2: Dass die Dimensionsregularisierung (eps > 0, also D > 4) mit 4D-Helizitaetsamplituden f, g, h vertraeglich ist
  (in D > 4 hat das Graviton mehr Polarisationen; die Regge-Herleitung [100] gilt fuer d > 4). Nicht geprueft.
- G3: Dass nur Arbeiten, die 2512.13780 oder 2201.06602 zitieren, eine IR-sichere g^3-Schranke enthalten koennen.
  Andere IR-sichere Wege (Energiekorrelatoren 2512.23791, Coulomb-Moden 2606.19432, DWPT 2609.16896, de Sitter) koennten
  ohne diese Zitate auskommen. Nicht geprueft (keine Websuche).
- G4: Dass die von mir angesetzte Ordnungszaehlung (g^3-Terme O(G), Rest O(GM^2)) die von Bellazzini ist. Bellazzini
  Abschn. 7 setzt c M^2n << G_E und behaelt trotzdem Schranken mit "+ O(G)" (S. 27); fuer Gravitonen-Koeffizienten
  steht eine solche Zaehlung nirgends. Nur [ES].
- E6 (gleiche Zeit), FRS Abschn. 4.2 "Smearing, IR regularization, and UV positivity" (S. 28-30), txt Z. 1769-1925:
  Erwartung: FRS nehmen die UV-Positivitaet (Im der Partialwellen >= 0 oberhalb M) ohne Bezug auf Bellazzinis Skalierungs-
  limes an; App. F ersetzt nur 1/eps durch log(q/E). Damit ist ihre Graviton-Anwendung eine IR-endliche Umschreibung bei
  fester Ordnung, keine Uebertragung der Unitaritaetsaussage (~60 %).
- **G1/E6-Befund (Eintrag 2026-10-01 21:42:05 CEST): bestaetigt (eine Zeile).** FRS setzen Unitaritaet als Partialwellen-Schranke (4.10) "0 <= rho_J^{h+h+} <= 2, 0 <= rho_J^{h+h-} <= 1" (S. 25) fuer die d-dimensionale Amplitude ("the unitarity of the S-matrix in d dimensions remains as in Eq. (4.10) [25, 73]", S. 29) und ersetzen in Anh. F nur 1/eps durch log; eine eigene Unitaritaetsaussage fuer A_E mit externen Gravitonen geben sie nicht ("In the limit considered in [41]", S. 46). Zu G2 traegt das bei: FRS nehmen 4D-Helizitaeten in d Dimensionen an, ohne es zu begruenden [A, S. 29].

### Protokollschluss (2026-10-01 21:45:55 CEST)

- Bericht oben geschrieben ab 21:42:11. Danach berichtigt: Kurzfazit 3 und "Weg" (g^3 steckt bei CHLPSD auch in der
  spin-4-Ableitung, Gl. 2.32a und 3.3a; FRS 4.39 ist dieser Baustein), Quellenliste ohne ungeprueftes "Lit. [2]",
  Zweiteilchen-Seiten als "laut LESUNG-LETZTE-SCHICHT" markiert, Suchumfang im Kurzfazit 5 genauer.
- quellen/SHA256SUMS.txt: 4 Dateien (2603.15755v2.pdf/.txt, insp-bell-r3.json, insp-chlpsd-r4.json). Die uebrigen Quellen
  liegen mit Hash in RUNDE-13/spin2-d4/quellen/SHA256SUMS.txt.
- Offene Rueckfragen R1-R3 (oben): R1 beantwortet (ja, FRS fuer MHV/g4); R2 beantwortet als benannte Luecke (spin-2/3-Regeln
  in A_E-Form, Ordnung G); R3 nach Recherchestand: g4 ja, g^3 nicht belegt. Neu offen: G2, G3.
