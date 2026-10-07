# LESUNG-BS2000: Battye/Sutcliffe, "Q-ball Dynamics" (2000), Volltextlesung gegen unsere Karten

- Auftrag BS-2000 der Leitung claude-primary (Finn 01.10.: "jo prüf das noch mal in einem subagent:
  https://arxiv.org/html/hep-th/0003252v1").
- Bearbeiter: Subagent (Claude), Start 2026-10-01 17:36:10 CEST (date). Zeitbox 40 min.
- Aufbau: BERICHT oben (wird zuletzt gefuellt), ARBEITSFELD darunter (chronologisch, nichts geloescht; Gestrichenes
  mit ~~ ~~ markiert).

---------------------------------------------------------------------------------------------------------------------

## BERICHT

Bericht geschrieben ab 17:50:19 (date). Quelle: Volltext arXiv:hep-th/0003252v1, Lesetiefe [A] fuer Text,
Gleichungen und alle Bildunterschriften; die Bilder selbst nicht angesehen. sha256 in quellen/SHA256SUMS.txt.

### Kurzfazit

- B&S rechnen in **genau unserem Modell**: U = f^2 (1 + (1 - f^2)^2) mit L = (1/2)|d phi|^2 ist U(S) = S - S^2 + S^3/2
  bei x, t -> 2x, 2t, also omega = omega_BS/2. Probe: Q0 = 2,4415 aus Chem 8 = 2 Q_BS. Ihre Befunde gelten 1:1.
- Sie zeigen nur Zweierstoesse (und Q/Anti-Q). Dreierstoss und ruhender dritter Ball fehlen, ebenso ein
  Abstandsgesetz und jede lineare oder eingebettete Mode. Fuer die Leiter sind sie kein Vorlaeufer.
- Chem 8: Die Leitungsaussage traegt, nutzt die Quelle aber zu wenig. Die paarweise Vorzeichenregel ergibt in unserer
  exp(-i omega t)-Konvention die pruefbare Vorhersage "der grosse Klumpen ist B (x > 0)" [ES].
- Chem 1: Das Ergebnis "erklaert" traegt. Die bessere Quelle ist B&S Gl. (3.3), der Ueberlappterm in der Ladung. Das
  "Pendeln zwischen den Baellen" ist an der Messstelle eine Schwebung der Ueberlappladung; dass sich Ladung zwischen
  den Kernen bewegt, ist nicht gezeigt [ES].
- LADUNGSTAUSCH-1 bleibt unberuehrt, weil B&S ein anderes Regime abtasten. Im Paper v0.9 fehlt B&S als Quelle des
  Modells.

### Erwartungsverstoesse (wichtigste zuerst; Details Arbeitsfeld 6)

1. Modellidentitaet statt nur "gleiche Familie" (40 % vorab). Damit faellt jeder Uebertragungsvorbehalt weg.
2. Chem 1: B&S sehen bei fast unseren Werten "virtually no charge transfer" (Abb. 11). Eine Frequenzdifferenz ist
   bei ihnen "not on a similar footing" wie eine Phasendifferenz (S. 16/17). Gl. (3.3) gibt das Trennpunktgesetz
   der Karte wieder. Lokal (S4) folgen die Mittel je Anfangsphase -cos(phi0) und sind so gross wie die Amplitude;
   das ist ein Bezugsversatz, keine Flussrichtung.
3. Chem 8: B&S liefern mehr als "paarweiser Uebertrag bekannt": Vorzeichenregel, Betrag gegen alpha (kleineres alpha
   gibt mehr Gesamtuebertrag), und "the smaller Q-ball moves at a greater speed". Letzteres erklaert den
   T = 600-Befund (kleine Klumpen verlassen den Bereich).
4. Q/Anti-Q: Vernichtung ist bei B&S meist unvollstaendig; vollstaendig nur in einem schmalen v-Fenster.
5. B&S widersprechen Axenides u. a. in der Deutung des Rechtwinkel-Auslaufs: Spaltung statt Geometrie. Die Leitung
   zitiert beide als gleichgerichtet.

### Literaturstand (Fragen A bis D, je [A] mit Fundstelle; Volltext im Arbeitsfeld 3)

- **A Stoesse.** Gleiche Ladung, 1D:
  - alpha = 0: Verschmelzung plus zwei Spaltprodukte (Abb. 3);
  - alpha = pi: Abstossung ohne Ladungsaenderung (Abb. 8);
  - 0 < alpha < pi: Uebertrag vom vorauslaufenden Ball, danach Abstossung (Abb. 9, 10; Gl. 3.6 bis 3.8);
  - alpha < 0: Richtung umgekehrt (S. 13);
  - Geschwindigkeit: Durchgang bei v = 0,3, zweiter Anlauf bei 0,28 (Abb. 6, 7);
  - Spaltung durch Stauchung (Gl. 3.4, 3.5; Abb. 4).

  Ungleiche Ladung: ruhend kaum Uebertrag; geboostet haengt der Betrag an der Phase beim Kontakt (Abb. 11, 12; S. 16).

  2D: Stossparameter mit 0 / pi / pi/4 (Abb. 13 bis 15); grosse Baelle zeigen Rechtwinkel-Spaltung,
  vier Baelle oder Uebertrag plus Spaltung (Abb. 16 bis 18); v-Reihe Abb. 19 bis 21.

  3D: kleine Baelle wie 1D (S. 26); grosse bilden Schleifen (Abb. 22 bis 25).
- **B Mehrkoerper.** Nur Zweier-Anfangszustaende (Gl. 3.2; S. 3, S. 31). Mehrere Baelle entstehen nur als Produkte.
- **C Abstand.** Kein Gesetz. Belegt ist nur: Der Ueberlappterm ist "exponentially small in a" (S. 8), eps^2 ist das
  Ueberlappintegral (S. 13), Driften senkt eps^2 (S. 15).
- **D Anregungen.** 1D, gestauchter Ball: Atmung "persists for many cycles with a slowly decreasing amplitude" bis
  t = 3000 (Abb. 5). Stossprodukte schwingen und strahlen (S. 11, Abb. 19). Stabilitaet wird nur referiert (S. 4 bis
  6). Nichts zu Moden oder stillen Stellen.

### Frage E, Urteile (Begruendung Arbeitsfeld 5)

1. Chem 8 -> **gestuetzt, aber zu schwach genutzt**: der paarweise Teil [A]; Dreierfall nicht bei B&S; Verwerfen der
   Katalyse beruht auf eigener Messung.
2. Chem 1 -> **Ergebnis gestuetzt, Einordnung zu schwach, Wortlaut "Pendeln zwischen den Baellen" zu stark** (Quelle
   Gl. 3.3 statt Lehrbuch-Tunnelstrom).
3. LADUNGSTAUSCH-1 -> **gestuetzt im bisherigen Umfang** (B&S nicht einschlaegig; Regime eng/ruhend gegen
   weit/geboostet).
4. BIC-Leiter -> **keine Folge; Literaturabschnitt zu schwach** (B&S als Modellquelle nachtragen).

### Regime und Moderatoren (Arbeitsfeld 7)

- gleiche gegen ungleiche Frequenz: gebundene Phase mit kumulativem Uebertrag, gegen laufende Phase mit Schwebung;
- ruhend gegen geboostet;
- enger Startueberlapp (CSZ, LADUNGSTAUSCH-1) gegen weit und geboostet (B&S Abschn. 6);
- kleine gegen grosse Ladung (Spaltung).

### Unterscheidungspunkte (Arbeitsfeld 8)

- Chem 8: Bahn des groessten Klumpens; X0-Variation bei festem v.
- Chem 1: Messung an den Kernen statt auf der Halbachse. Ein Trennpunkt am grossen Ball trennt nicht.
- R3: Anfangsphase variieren bei d = 8 oder 10.

### Gegensweep (Arbeitsfeld 9)

- Geprueft:
  - Potential gegen Lesefehler;
  - Phasenkonvention: unsere ist umgekehrt;
  - a = d/2;
  - Chem-1-Baelle sind frei;
  - Zitierpaar Axenides/B&S.
- Offen:
  - NPB gegen v1;
  - Bilder nicht angesehen;
  - 24-Monats-Suche nicht moeglich, weil das WebSearch-Budget der Sitzung erschoepft ist (200 von 200). Deshalb
    keine Aussage ueber Folgeliteratur.

### Offene Fragen und Quellen

Siehe Arbeitsfeld 11 und 12.

---------------------------------------------------------------------------------------------------------------------

## ARBEITSFELD

### 0. Kontext gelesen vor den Erwartungen (17:36:10 bis 17:36:59)

- RUNDE-10/chem8/KARTE.md (inkl. "L4, erster Blick", nur Abstracts), RUNDE-11/chem8-mitte/KARTE.md,
  RUNDE-11/chem1/KARTE.md, RUNDE-10.md Abschnitt LADUNGSTAUSCH-1 (Z. 235 bis 258) und L4-Zeile (Z. 501),
  RUNDE-11.md Abschnitte Chem 1 (Z. 132 ff.), Chem 8 Mitte (Z. 300 ff.), Tabelle (Z. 381/382),
  model-lab/papers/qball-bic-ladder-20260930/sections/LITERATURE.tex und LITERATURE-SOURCES.txt, main.tex Z. 82 bis 117.
- Unser Modell (main.tex Z. 82/83): L = |d phi|^2 - U(|phi|^2), U(S) = S - S^2 + beta S^3, beta = 1/2, Masse 1,
  omega_c^2 = 1 - 1/(4 beta) = 1/2, also omega in (0,707; 1). 1D-Karten nutzen omega^2 = 0,6 / 0,7 / 0,8.
- B&S stehen bisher NICHT in LITERATURE.tex des Paper-Entwurfs v0.9 (Zitate dort: Coleman 1985, Kovtun 2018,
  Ciurla 2024, Friedrich/Wintgen 1985, Yu/Lu 2025).

### 1. Vorab-Erwartungen (geschrieben 2026-10-01 17:36:59 CEST laut date, VOR dem Oeffnen des Volltexts)

Grundlage: nur Erinnerung aus Trainingsdaten (unsicher) und die Abstract-Zitate der Leitung. Wahrscheinlichkeiten
sind grobe Selbsteinschaetzung.

- **E1 Potential:** sextisches Polynom in |phi|, Familie U = |phi|^2 - |phi|^4 + beta |phi|^6 (oder gleichwertig
  umskaliert). Gleiche Familie wie unseres: etwa 60 %; genau beta = 1/2: etwa 40 %. Frequenzfenster
  (omega_-, 1) mit omega_-^2 = 1 - 1/(4 beta).
- **E2 Stoesse (Frage A):** 1D-Kopfstoesse mit relativer Phase: in Phase -> Anziehung/Verschmelzung, Gegenphase ->
  Abstossung/Abprallen, dazwischen Ladungsuebertrag, Richtung durch das Vorzeichen der Phasendifferenz bestimmt.
  Bei ungleichen omega laeuft die relative Phase in der Zeit (daher die "zeitabhaengigen Phasen" des Abstracts).
  2D/3D: Verschmelzung, Durchdringung bei hoher v, eventuell 90-Grad-Streuung. "Fission": ein angeregter oder
  instabiler Ball zerfaellt in zwei. Etwa 75 %, dass die Phasenabhaengigkeit des Uebertrags so explizit gezeigt ist.
- **E3 Mehrkoerper (Frage B):** kein Dreierstoss, kein ruhender dritter Ball. Etwa 85 %.
- **E4 Abstandsgesetz (Frage C):** kein quantitatives Abstandsgesetz des Ladungsuebertrags. Etwa 75 %. Moeglich
  (etwa 30 %): eine qualitative oder asymptotische Aussage, die Wechselwirkung falle exponentiell mit dem Abstand
  (Schwanzueberlapp), eventuell mit cos(Phasendifferenz).
- **E5 Anregungen/Atmung/Abstrahlung (Frage D):** Stabilitaetskriterium ueber Q(omega) bzw. E(Q) und
  Spaltungsstabilitaet (Fission) wahrscheinlich (etwa 70 %); Stossprodukte als angeregte, schwingende, strahlende
  Baelle qualitativ erwaehnt (etwa 50 %); nichts zu eingebetteten Moden, stillen Stellen, nicht strahlenden
  Anregungen (etwa 90 %).
- **E6 Q/Anti-Q:** Q-Anti-Q-Stoesse eventuell als Vernichtung behandelt (etwa 50 %); ein langlebiger
  Ladungstausch-Ball (Charge-swapping, CSZ 2014) wird NICHT beschrieben (etwa 80 %).
- **E7 Entscheidungen (Frage E), vorab:**
  1. Chem 8: "paarweiser Ladungsuebertrag beschrieben" gestuetzt; "Dreierstoss" nicht abgedeckt; das Wort
     "beschreibt" ist richtig, solange keine Dreierbehauptung aus B&S abgeleitet wird.
  2. Chem 1: B&S liefern kein Abstandsgesetz; die Einordnung als Lehrbuch-Tunnelstrom bleibt [L?]. Moeglicher
     Vorlaeufer: Erklaerung des Pendelns ueber laufende relative Phase (Periode 2 pi/(omega1 - omega2)).
  3. LADUNGSTAUSCH-1: B&S nicht einschlaegig (CSZ 2014 bleibt die Quelle).
  4. BIC-Leiter: kein Vorlaeufer, kein Widerspruch; hoechstens Kontext (Stossprodukte strahlen ab).
- Was mich am meisten ueberraschen wuerde (Verstoss-Kandidaten): ein Dreierstoss bei B&S; ein Abstandsgesetz;
  eine langlebige, kaum strahlende Anregung (Vorlaeufer der Leiter); ein anderes Potential (dann waere die
  Uebertragbarkeit auf unser Modell fraglich).

### 2. Quelle (abgerufen 17:37:31, date)

- arXiv-HTML https://arxiv.org/html/hep-th/0003252v1 -> quellen/hep-th-0003252v1.html (HTTP 200, 236611 Byte),
  sha256 4d2f53b8892f5deeb10ef9ea6c10dc12f165dbdcb2fdaad366b2dc8bf6d39a6b.
- arXiv-PDF https://arxiv.org/pdf/hep-th/0003252v1 -> quellen/hep-th-0003252v1.pdf (40 Seiten, 792434 Byte),
  sha256 3f9c4dd7480dcb52756b284301624da8077fa790e4b48185c4ecf4bbedfd9cc1.
- pdftotext -layout -> quellen/hep-th-0003252v1.txt (1170 Zeilen),
  sha256 f850070a92a61f97277c5b6ae9d0c0b40ffd427983340f0267a250943f76622e. Alle drei in quellen/SHA256SUMS.txt.
- arXiv-Abstractseite (17:44): nur v1 (28.03.2000), "37 pages, including figures", kein Journal-ref-Feld. Die
  gedruckte Fassung Nucl. Phys. B590 (2000) 329 habe ich NICHT gegen v1 verglichen.
- **Lesetiefe:** [A] fuer den gesamten Text, alle Gleichungen (2.1) bis (3.8) und alle Abbildungsunterschriften
  (Abb. 1 bis 30), gelesen in der Textfassung Zeile 1 bis 1170. Die Abbildungsbilder selbst habe ich NICHT angesehen
  (Ladungsdichte-Plots); Aussagen ueber Abbildungen stuetzen sich auf Unterschrift und Fliesstext.
- Seitenzahlen unten = Seitenzahl im arXiv-PDF (Fusszeile).

### 3. Lesung, Befunde mit Fundstelle (17:37:31 bis 17:44:09)

**Modell (Frage 5)**
- [A] Abschn. 2, Gl. (2.1): L = (1/2) d phi d phibar - U(|phi|); Gl. (2.10): U(f) = f^2 (1 + (1 - f^2)^2)
  = 2 f^2 - 2 f^4 + f^6; omega_+ = 2, omega_- = sqrt 2, Q-Baelle fuer sqrt 2 < omega < 2 (S. 5). Feldgleichung
  Gl. (3.1): phi_tt - lap phi + 2 phi (2 - 4|phi|^2 + 3|phi|^4) = 0, "valid for any value of D".
- [A] "In this paper we will mainly be concerned with the type I potential, although we have also studied the type II
  case" (S. 5); Typ II = f^2, f^3, f^4 (Gl. 2.8). Fazit S. 39: einige Laeufe mit Typ II wiederholt, "same qualitative
  results".
- **[ES] Umrechnung (Kopfrechnung, kein Rechner):** B&S-Gleichung (3.1) = 4 x unsere Gleichung
  phi_tt - lap phi + (1 - 2S + 1,5 S^2) phi = 0 (Code chem8_dicht.py Z. 8 bis 9, main.tex Z. 82 bis 88). Mit
  x_unser = 2 x_BS, t_unser = 2 t_BS, gleicher Feldamplitude ist das **dasselbe Modell**:
  omega_unser = omega_BS / 2, kappa_unser = kappa_BS / 2, v gleich, Q_unser = 2^D Q_BS (bei unserer Konvention
  Q = 2 omega Int f^2, Code Z. 177). Fenster sqrt 2 < omega_BS < 2 <-> 0,707 < omega < 1 (unser omega_c^2 = 1/2).
  - Probe gegen unsere Zahl: B&S Gl. (2.11)/(2.12) (exaktes 1D-Profil; die pdftotext-Fassung von (2.12) ist
    verstuemmelt, ich habe Q = omega Int f^2 aus (2.11) selbst integriert) ergibt bei omega_BS = 2 sqrt 0,7 = 1,673
    Q_BS = sqrt2 omega artanh((2 - sqrt(2 omega^2 - 4))/(sqrt2 sqrt(4 - omega^2))) = etwa 1,2208, also
    Q_unser = 2,4416. Chem 8 nennt Q0 = 2,4415. Uebereinstimmung auf etwa 1e-4 (Kopfrechnung, Rundung).
  - Parameter-Tabelle: B&S omega = 1,5 / 1,6 / 1,8 <-> unser omega^2 = 0,5625 / 0,64 / 0,81. Unsere Karten: 0,6 / 0,7 /
    0,8 <-> omega_BS = 1,549 / 1,673 / 1,789. Leiter (main.tex Tab.): B&S 1,5 liegt zwischen n = 6 (0,5694) und n = 7
    (0,5599); B&S 1,8 knapp ueber n = 1 (0,7977).
  - Codekonvention: unser Ball ist psi = f exp(-i omega gamma (t - v (x - x0)) + i phase) (chem8_dicht.py Z. 182 bis
    192), B&S phi = exp(+i omega t) f (Gl. 2.4, 3.2). Unsere Konfiguration mit Phasen p_j entspricht der B&S-
    Konfiguration mit Phasen -p_j (komplex konjugiert). Wichtig fuer jede Richtungsaussage unten.
- Numerik B&S [A]: 1D 1000 Punkte, dx = 0,1, dt = 0,02, absorbierende Raender (S. 7); 2D 200^2, dx = 0,2, dt = 0,05
  (S. 17); 3D Uebersicht 100^3, Detail 300^3 mit dx = 0,3, dt = 0,03 (S. 26/28).

**Frage A: Stoesse**
- [A] 1D, gleiche Ladung, in Phase (Abb. 3, omega = 1,5, a = 4, alpha = 0, Ruhe): langsame Anziehung, Verschmelzung zu
  einem grossen Ball mit etwas weniger als der Summenladung; der Rest geht in zwei kleine Spaltprodukte ("fission").
  Kleinere Baelle: keine Spaltung, der eine Ball "oscillates for some time, with a decreasing amplitude" (S. 11).
- [A] Spaltung durch Verformung: Skalierung (3.4) x -> lambda x, phi -> sqrt(lambda) phi bei fester Ladung; Q = 8,4,
  lambda = 1,6: Teilung in zwei gleiche Teile (Abb. 4); Mass Delta(Q) = (2E(Q/2) - E(Q))/E(Q), Gl. (3.5), monoton
  fallend in Q (S. 10).
- [A] 1D Geschwindigkeit (Abb. 6, 7): omega = 1,5, a = 10, v = 0,3: Durchdringung mit Ladungsverlust durch Strahlung;
  v = 0,28: Durchdringung, Rueckkehr, Verschmelzung im zweiten Anlauf.
- [A] Relative Phase, gleiche Ladung: alpha = pi: Abstossung, "simply drift apart with no change in their shape or
  charge" (S. 11/12, Abb. 8). alpha = pi/9: "charge transfer": linker Ball verliert an rechten, beide bleiben getrennt
  bei sehr kleinem Ueberlapp, danach Abstossung; **"the smaller Q-ball moves at a greater speed than the larger one"**
  (S. 12, Abb. 9).
- [A] Abb. 10 (Ladung auf x > 0 gegen t, alpha = pi/9, pi/4, pi/2): kleineres alpha -> langsamere Anfangsrate, aber
  **groessere Gesamtuebertragung**; alpha = 0 als glatter Grenzfall "totaler Uebertrag" (Verschmelzung), alpha = pi
  kein Uebertrag; **alpha < 0: gleicher Betrag, umgekehrte Richtung** (S. 13).
- [A] Mechanisches Modell Gl. (3.6) bis (3.8): zwei festgehaltene gleiche Baelle mit Phasen theta1(t), theta2(t);
  L = (1/2) M (theta1'^2 + theta2'^2) - eps^2 cos(theta1 - theta2) - 4M, M = Int f^2, eps^2 = 4 Int f(|x+a|) f(|x-a|) dx
  ("small interaction coefficient", Ueberlappintegral); theta1'' - theta2'' = (2 eps^2/M) sin(theta1 - theta2). Fuer
  alpha in (0, pi) waechst theta1' -> Ball 1 verliert Ladung; Anfangsrate maximal bei alpha = pi/2 (S. 13/14). Grenzen
  von den Autoren selbst genannt: festes Profil, feste Orte; Auseinanderdriften "will also serve to cut-off the relative
  phase dynamics since it will correspond to reducing the eps^2 coefficient" (S. 15). Quantitativ "a more
  sophisticated analysis is required" (S. 15); Verweis auf Ahn/MacKay/Sepulchre (diskrete Breather, Ref. [18]) und
  angekuendigtes Battye/MacKay/Sutcliffe "An effective Hamiltonian for Q-ball dynamics" (Ref. [11], "in preparation").
- [A] **Gl. (3.3):** Gesamtladung der Zwei-Ball-Ansatzes Q = Q_omega1 + Q_omega2 + (omega1 + omega2) cos(alpha)
  Int f_omega1(|x+a|) f_omega2(|x-a|) dx; der letzte Term "exponentially small in the separation parameter a". Die
  Autoren folgern: Energie gegen Phase oder gegen Abstand aus dem Ansatz zu bestimmen hiesse Konfigurationen mit
  verschiedenem Q zu vergleichen; Aufloesung vertagt auf Ref. [11] (S. 8).
- [A] **Ungleiche Ladungen (S. 16, Abb. 11, 12):** relative Anfangsphase verliert an Bedeutung, weil sie auch ohne
  Wechselwirkung nicht erhalten bleibt. omega1 = 1,8, omega2 = 1,5, a = 3, alpha = 0, Ruhe: **"the two Q-balls repel and
  there is virtually no charge transfer since the solitons never get close enough"**; mit Anfangsphase ebenfalls
  "virtually no charge transfer". Mit Boost (a = 6, v = 0,2) Durchdringung und Uebertrag; **"The amount of charge
  transferred depends on the value of the relative phase as the Q-balls collide"**, gleichwertig zur Aenderung des
  Startabstands (Kollisionszeit x Frequenzdifferenz). "one might have naively expected that an initial difference in
  the rotation speeds would be on a similar footing to an initial phase difference, but this is clearly not the case"
  (S. 16/17).
- [A] 2D (Abschn. 4): Stoss mit Stossparameter (omega = 1,6, +-(6, 3), v = 0,05): alpha = 0 Verschmelzung mit
  Drehimpuls (Abb. 13), alpha = pi Abstossung (Abb. 14), alpha = pi/4 Anziehung, Uebertrag, Abstossung (Abb. 15).
  Kopfstoss omega = 1,5, +-(10, 0), v = 0,4: alpha = 0 Rechtwinkel-Auslauf durch Spaltung, ausdruecklich NICHT als
  Modulraum-90-Grad-Streuung gedeutet (Abb. 16, S. 21; Widerspruch zu Axenides u. a. [13]); alpha = pi: jeder Ball
  spaltet, vier Baelle (Abb. 17); alpha = pi/2: Uebertrag plus Spaltung, zwei kleine und zwei grosse (Abb. 18).
  omega = 1,6: v = 0,4 ein Ball nach Schwingung (Abb. 19), v = 0,6 vier kleine plus viel Strahlung (Abb. 20), v = 0,8
  Durchgang (Abb. 21).
- [A] 3D (Abschn. 5): Uebersicht 100^3: kleine Baelle in Phase verschmelzen, Gegenphase stossen ab, "any other phase"
  Uebertrag (S. 26). Grosse Baelle (omega = 1,5, +-(15,0,0), v = 0,4): Ring/Schleife senkrecht zur Stossachse (Abb. 22),
  alpha = pi zwei Schleifen (Abb. 23), alpha = pi/2 zwei ungleich geladene Schleifen, "the smaller one having a higher
  speed" (Abb. 24); v = 0,8 drei Schleifen (Abb. 25); Stabilitaet von Schleifen vertagt (Ref. [20]).
- [A] Q/Anti-Q (Abschn. 6, 2D und 3D, "also prevalent in both one and three dimensions" S. 33): Vernichtung meist
  unvollstaendig, Abprallen bei kleinem v, Durchgang bei grossem v; vollstaendige Vernichtung nur in einem kleinen
  Fenster um ein v_c(omega) (Fussnote 5); Deutung: Uebertrag zwischen entgegengesetzten Ladungen = Vernichtung, und
  "charge transfer never takes place fully in 2-Q-ball interactions" (S. 31). Beispiele: omega = 1,8, +-(6,0),
  v = 0,3: Teilvernichtung, Durchgang (Abb. 26); omega = 1,5, v = 0,3: vollstaendige Vernichtung "during a complicated
  oscillatory interaction" (Abb. 27); v = 0,6 Spaltung (Abb. 28); 3D +-(10/15,0,0): v = 0,3 kaum Vernichtung (Abb. 29),
  v = 0,6 zwei Schleifen, fast vollstaendige Vernichtung (Abb. 30).
- [A] Fazit (Abschn. 7, S. 33/34): Schluesselparameter relative Phase, Einfallsgeschwindigkeit, Ladung. Uebertrag
  "analogous to that observed in discrete breather systems", "often has to be induced by making the solitons come
  together via a Lorentz boost. With no Lorentz boost such breather systems naturally repel".

**Frage B: Mehrkoerper**
- [A] Alle Anfangszustaende sind Zwei-Ball-Zustaende (Ansatz Gl. 3.2; Einleitung S. 3: "general situations of two
  interacting Q-balls"; Abschn. 6 beginnt "we have studied in detail 2-Q-ball interactions"). Mehr als zwei Baelle
  kommen nur als Produkte vor (zwei Spaltprodukte Abb. 3; vier Baelle Abb. 17, 18, 20; Schleifen in 3D). **Kein
  Dreierstoss, kein ruhender dritter Ball.**

**Frage C: Abstandsgesetz**
- [A] Kein quantitatives Abstandsgesetz, kein Fit, keine Zerfallskonstante. Nur qualitativ: Ueberlappterm in Q
  "exponentially small in a" (S. 8); eps^2 ist das Ueberlappintegral (S. 13); Driften senkt eps^2 (S. 15); a = 3 bei
  ungleichen Baellen "never get close enough" (S. 16).

**Frage D: Anregungen, Atmung, Abstrahlung**
- [A] Gestauchter Ball Q = 5,6, lambda = 1,6 (1D): "breather-like motion in which two structures initially begin to
  form but then recombine. This motion persists for many cycles with a slowly decreasing amplitude until it eventually
  settles down" (bei t = 3000 fast gleich dem ungestoerten Ball) (S. 10/11, Abb. 5). Kleine Stauchung: Schwingung und
  Rueckkehr, "to be expected since these Q-balls are stable" (S. 10).
- [A] Stossprodukte schwingen und strahlen ab (S. 11; 2D Abb. 19 "oscillates for some time before settling down ...
  after a small amount of charge has been dissipated through radiation", S. 26).
- [A] Stabilitaet nur referiert: Duennwandgrenze (Coleman), zweite Variation, Kusenko [14], Stuart [15], Multamaeki/
  Vilja [19]; 1D: E/Q faellt mit Q -> stabil gegen Zerfall in kleinere Baelle (S. 4 bis 6); 3D hat bei diesem Potential
  eine untere Ladungsschranke (S. 6).
- [A] **Nichts** zu linearen Moden, Spektrum, eingebetteten Moden, nicht strahlenden Anregungen, Lebensdauern als
  Zahl oder zu angeregten Q-Baellen in 3D ausserhalb von Stoessen.

### 4. Gegensweep-Suchen, Erwartung vor jedem Abruf (geschrieben ab 17:45:20, date)

- S1 (Suche "Q-ball collisions three Q-balls / multi-soliton", letzte 24 Monate): Erwartung: neuere Stossarbeiten
  (2D/3D, Ladungstausch, Spinning) gibt es; einen Dreierstoss mit ruhendem dritten Ball finde ich nicht.
- S2 (Suche nach Ref. [11] Battye/MacKay/Sutcliffe "effective Hamiltonian"): Erwartung: nie erschienen.
- S3 (Suche "Q-ball interaction relative phase asymptotic force separation"): Erwartung: asymptotische
  Kraftformeln mit cos(Phase) und e^{-kappa d} existieren (etwa Bowcock/Foster/Sutcliffe 2009); ein Abstandsgesetz
  des Ladungsuebertrags fuer ungleiche Baelle finde ich nicht.

- 17:47 Suchbudget: WebSearch meldet 200 von 200 Aufrufen der Sitzung verbraucht; S1 bis S3 NICHT ausgefuehrt. Folge: keine Aussage ueber Folgeliteratur, Status 'nach Recherchestand nicht geprueft'.
- S4 (lokal, 17:47:22 vor Abruf): RUNDE-11/chem1/lauf-69/t1_bericht.txt. Erwartung: mittleres dQ_klein je phi0 ist bei d >= 14 klein und ohne systematisches Vorzeichenmuster; bei d = 12 klein, schwach phasenabhaengig.
- S4 Ergebnis (17:47 bis 17:48): **Erwartung verletzt.** t1_bericht.txt, d = 12: mittleres dQ_klein je phi0 = 0, pi/2,
  pi, 3pi/2 = -0,0491 / -0,0051 / +0,0593 / +0,0111 bei Amplitude 0,0540 und Phasenmittel 0,0040. Die Mittel je Phase
  sind also so gross wie die Amplitude und folgen -cos(phi0); bei d = 14 bis 20 dasselbe Muster (z. B. d = 20:
  -0,00070 / +0,00070 bei Amplitude 0,00073). Code chem1_abstand.py Z. 309 bis 314, 330/331: zwei anfangs ruhende,
  freie Baelle (nicht festgehalten), Trennpunkt fest bei x = 0.
  - [ES] Fuer eine reine Schwingung dQ(t) = A [cos(dw t + phi0) - cos(phi0)] ist das Zeitmittel genau -A cos(phi0).
    Das Muster ist damit der Bezugsversatz einer Schwingung gegen ihren Startwert. Die Urteilszeile des Codes
    "Richtung folgt der Anfangsphase (Josephson)" beschreibt dann den Startpunkt auf der Schwingung, keine
    Flussrichtung.

### 5. Abgleich mit den Karten (Frage E), ab 17:48:28

**[ES] Vorzeichenregel in unserer Konvention.** B&S: bei alpha in (0, pi) verliert der in der Drehrichtung
vorauslaufende Ball (Abb. 9: linker Ball mit Phase +alpha verliert). Unser Code dreht mit exp(-i omega t). Komplexe
Konjugation laesst die Feldgleichung unveraendert und macht aus unseren Phasen p_j die B&S-Phasen -p_j. Folge: **bei
uns gibt der Ball mit der kleineren Codephase an den mit der groesseren ab** (Phasendifferenz in (0, pi)).

**Entscheidung 1, Chem 8** (Leitung: "paarweiser Ladungsuebertrag beschrieben", "Katalysebild verworfen", "der
grosse Klumpen ist nicht C", "Ladungsumverteilung im Dreierstoss").
- [A] Paarweiser, phasenabhaengiger Uebertrag ist in B&S gezeigt: Abschn. 3 Abb. 9 und 10, Gl. (3.6) bis (3.8), 2D
  Abb. 15, 3D Text S. 26. Die Aussage der Leitung traegt.
- [A] Dreierstoss: kommt nicht vor. Das Verwerfen der Katalyse stuetzt sich allein auf unsere Messung (Chem 8 Mitte),
  nicht auf B&S.
- [ES] B&S sagen mehr, als die Leitung genutzt hat, und daraus folgt eine pruefbare Vorhersage fuer die offene Frage
  "welcher Ball traegt die Ladung":
  - Bruecke: Codephasen A = 0 < C = dphi/2 < B = dphi. Mit der Regel oben fliesst Ladung A -> C -> B. Vorhersage:
    Der grosse Klumpen ist B, also bei x > 0, und A wird der kleinste.
  - Sperre bei dphi = pi ist das Spiegelbild der Bruecke: Spiegelung x -> -x plus globale Phase -pi bildet
    (0, pi/2, pi) auf (0, 3pi/2, pi) ab. Das erklaert "sperre gleich bruecke" bei pi als exakte Symmetrie. Bei
    3pi/4 hat die Sperre |alpha| = 5pi/8 je Paar statt 3pi/8, liegt also naeher am abstossenden Kanal; passend
    dazu verschmilzt sie nicht. B&S zeigen den Betrag des Uebertrags nur fuer alpha <= pi/2 (Abb. 10).
  - [A] "the smaller Q-ball moves at a greater speed than the larger one" (S. 12; Abb. 24). Das passt zum
    T = 600-Befund aus Chem 8: Die kleinen Klumpen verlassen den Messbereich, der grosse bleibt.
  - Vorbehalt: Die Regel gilt bei B&S fuer gleiche, ruhende oder symmetrisch geboostete Baelle. In Chem 8 ruht C,
    waehrend A und B laufen. Deren Phase dreht im Labor mit omega/gamma, sie laufen gegen C also um etwa
    delta = omega (1 - 1/gamma) t_Kontakt, grob omega v X0 / 2, vor (Kopfrechnung: v = 0,1 etwa 0,5 rad, v = 0,25
    etwa 1,3 rad). Das bricht die Symmetrie der beiden Paare (dphi/2 - delta gegen dphi/2 + delta) und kann die
    glatte Kuppe in v mitformen. B&S S. 16 sagen genau das fuer ungleiche Baelle: Die Phase beim Kontakt zaehlt, und
    sie ist gleichwertig zum Startabstand.
- **Urteil 1: gestuetzt, aber zu schwach genutzt.** "Ladungsumverteilung im Dreierstoss" ist richtig und vorsichtig
  formuliert. Die Bemerkung "nur Abstract gelesen" ist jetzt erledigt.

**Entscheidung 2, Chem 1** (Leitung: Pendeln faellt exponentiell, kappa_mittel an der Mitte, Trennpunkt-Abhaengigkeit,
"Lehrbuch-Tunnelstrom, kein Messbezug", parken "erklaert").
- [A] Ein Abstandsgesetz fehlt bei B&S. Einschlaegig ist aber Gl. (3.3) mit S. 8: Die Ladung zweier Baelle enthaelt
  den Ueberlappterm (omega1 + omega2) cos(alpha) Int f1 f2, und Ladung (wie Energie) einer ueberlappenden
  Konfiguration haengt an alpha. Bei ungleichen omega laeuft alpha in der Zeit (S. 16).
- [ES] Zwischen den Baellen ist f1 f2 proportional zu e^{-(kappa1 + kappa2) d/2} e^{(kappa2 - kappa1) x}. Der Anteil
  links von x0 schwingt mit der Schwebung dw = |omega1 - omega2|, mit der Amplitude
  e^{-kappa_mittel d + (kappa2 - kappa1) x0}. Das ist genau das Gesetz der Karte, einschliesslich der Faktoren
  1,45 und 0,69. Der Wronski-Strom der Leitung ist dieselbe Groesse, nur ueber die Kontinuitaetsgleichung gesehen
  (Probe: omega1^2 - omega2^2 = kappa2^2 - kappa1^2 bei kappa^2 = 1 - omega^2). Es gibt also keine zwei
  konkurrierenden Deutungen, sondern eine.
- [ES] Haengt die Amplitude von x0 ab, dann schwingt nach der Kontinuitaetsgleichung die Ladung im Spalt selbst. Ein
  von x0 unabhaengiger Durchfluss von Kern zu Kern hat in der Trennpunkt-Tabelle der Karte hoechstens einige Prozent
  Anteil (Verhaeltnisse 1,438 bis 1,447 gegen 1,448). Das "Pendeln zwischen kleinem und grossem Ball" ist an der
  Messstelle also eine Schwebung der Ueberlappladung. Dass sich Ladung zwischen den Kernen bewegt, ist damit nicht
  gezeigt.
- [A] B&S Abb. 11 bei fast unseren Werten (omega_BS = 1,8/1,5, a = 3, also omega^2 = 0,81/0,5625, d = 12): "repel
  and there is virtually no charge transfer". Das ist ein Urteil nach Augenmass auf Dichtebildern; ein Effekt von
  2 % ist dort nicht sichtbar. Kein Widerspruch zu Chem 1 V3 (kein Nettofluss). Zusatz: Die Baelle stossen sich
  bei B&S ab; in Chem 1 sind sie frei, d driftet also womoeglich waehrend T = 400. Nicht geprueft.
- [A] S. 16/17: Eine Frequenzdifferenz steht "not on a similar footing" wie eine Phasendifferenz. Das spricht gegen
  ein Josephson-Bild fuer ungleiche Baelle im Sinn eines echten Uebertrags.
- **Urteil 2: Ergebnis gestuetzt, Einordnung zu schwach, Wortlaut zu stark.** "parken, erklaert" traegt. Die bessere
  Quelle fuer "die Zerfallskonstante haengt am Messpunkt" ist B&S Gl. (3.3) mit S. 8, nicht ein Lehrbuch-Tunnelstrom
  [L?]. Der Wortlaut "Ladung pendelt zwischen den Baellen" behauptet mehr, als gemessen ist.
- [ES] Herkunft der Karte (R3: d = 10 klein -> gross, d = 8 gross -> klein, "Elektronegativitaet = omega"): B&S S. 16
  bieten eine Gegenhypothese an. Bei ungleichen Baellen entscheidet die Phase beim Kontakt, und die haengt vom
  Startabstand ab. Ein Richtungswechsel zwischen d = 8 und 10 waere dann ein Phaseneffekt, keine Regel. R3-Datei
  nicht gelesen.

**Entscheidung 3, LADUNGSTAUSCH-1** (Tauschball aus eng gestartetem Q/Anti-Q-Paar, Kriterium CSZ 2014, Tauschfrequenz
Omega_2 - Omega_1).
- [A] B&S Abschn. 6: nur weit getrennte, geboostete Paare (2D +-(6,0), entspricht bei uns d = 24; 3D +-(10..15)).
  Vernichtung meist unvollstaendig; Abb. 27 "complicated oscillatory interaction" vor vollstaendiger Vernichtung
  (Bild nicht angesehen). Ein langlebiger Tauschzustand kommt nicht vor; ebenso keine eng gestarteten ruhenden Paare.
- [A] Fussnote 4 S. 31: Q/Anti-Q als Uebertrag mit maximaler Differenz der Drehgeschwindigkeiten. Begrifflich nah an
  "Tausch", ohne Zahl.
- **Urteil 3: unberuehrt (gestuetzt im bisherigen Umfang).** B&S sind weder Vorlaeufer noch Widerspruch, weil sie ein
  anderes Regime abgetastet haben (Moderator: Startueberlapp und Startgeschwindigkeit). CSZ 2014 bleibt die Quelle.

**Entscheidung 4, BIC-Leiter / Paper v0.9 Literatur.**
- [A] Bei B&S stehen keine linearen Moden, keine eingebetteten Moden und keine nicht strahlenden Anregungen. Atmung
  kommt nur in 1D vor (Abb. 5, gestauchter Ball, "slowly decreasing amplitude", t <= 3000, bei uns 6000). Das passt
  zu "1D hat keine stillen Stellen" (RUNDE-10) und zum Bild langlebiger Quasinormalmoden (Ciurla 2024, laut
  LITERATURE.tex). Es ist kein Vorlaeufer und kein Widerspruch.
- [ES] Neu und wichtig fuer das Paper: **B&S rechnen in genau unserem Modell** (U = f^2 (1 + (1 - f^2)^2) mit
  L = (1/2)|d phi|^2 entspricht U(S) = S - S^2 + S^3/2 bei x, t -> 2x, 2t). LITERATURE.tex v0.9 nennt B&S nicht.
  Empfehlung: B&S als fruehere Nutzung desselben Potentials (Dynamik in 1D bis 3D) zitieren und die Umrechnung
  angeben. Ein Prioritaetskonflikt entsteht nicht. B&S 3D-Laeufe bei omega_BS = 1,5 liegen bei omega^2 = 0,5625,
  also zwischen den Sprossen n = 6 und n = 7; zu Atmung dort sagen B&S nichts.
- **Urteil 4: keine Folge fuer die Leiter; Literaturabschnitt zu schwach (fehlende Modellquelle).**

**Frage 5, Modellvergleich:** identisch bis auf Einheiten (siehe 3.). B&S-Ergebnisse sind direkt uebertragbar, auch
Zahlen: omega = omega_BS/2, Laengen und Zeiten x 2, v gleich, Q x 2^D. Typ II (f^2, f^3, f^4) haben B&S nur
stichprobenhaft gerechnet.

### 6. Vorab gegen Ausgang (Regel 3), ab 17:49:14

Bestaetigt, je eine Zeile:
- E3 kein Dreierstoss, kein ruhender dritter Ball: bestaetigt [A].
- E4 kein quantitatives Abstandsgesetz, nur "exponentially small in a": bestaetigt [A].
- E5 Stabilitaet nur referiert, Produkte schwingen und strahlen, nichts zu eingebetteten Moden: bestaetigt [A].
- E6b kein langlebiger Tauschball: bestaetigt [A].
- E2 Grundmuster (0 verschmilzt, pi stoesst ab, dazwischen Uebertrag mit Vorzeichen): bestaetigt [A].

Verletzt (voller Zyklus oben, korrigierte Erwartung jeweils dahinter):
- **V-1 (E1):** Ich hatte 60 % auf "gleiche Familie" und nur 40 % auf exakt beta = 1/2 gesetzt. Ergebnis: exakt
  unser Modell bis auf x, t -> 2x, 2t (Gl. 2.10, 3.1; Q0-Probe). Korrektur: B&S-Zahlen sind ohne Modellvorbehalt
  uebertragbar; die Schreibweise f^2 (1 + (1 - f^2)^2) mit L = (1/2)|d phi|^2 verdeckt das auf den ersten Blick.
- **V-2 (E7.2 und S4):** Erwartet war ein Josephson-Vorlaeufer fuer das Pendeln in Chem 1. Ergebnis: B&S sehen bei
  fast unseren Parametern "virtually no charge transfer" (Abb. 11). Sie lehnen ausdruecklich ab, eine
  Frequenzdifferenz wie eine Phasendifferenz zu behandeln (S. 16/17). Mit Gl. (3.3) liefern sie den Ueberlappterm,
  der das Trennpunktgesetz der Karte vollstaendig wiedergibt. Dazu S4: Die Mittel je Anfangsphase sind so gross wie
  die Amplitude und folgen -cos(phi0). Erwartet hatte ich "klein". Korrektur: Chem 1 misst eine Schwebung der
  Ueberlappladung. Ob zwischen den Kernen Ladung wandert, ist offen.
- **V-3 (E7.1):** Erwartet war "gestuetzt, mehr nicht". Ergebnis: B&S liefern eine Vorzeichenregel, den Betrag in
  Abhaengigkeit von alpha und die Regel "kleiner Ball schneller". Daraus folgt in unserer Konvention eine pruefbare
  Vorhersage fuer Chem 8 (B traegt den grossen Klumpen bei der Bruecke), und der T = 600-Befund wird erklaert.
- **V-4 (E6a):** Ich hatte 50 % auf "Vernichtung" gesetzt. Ergebnis: Die Kernaussage ist, dass Vernichtung meist
  unvollstaendig bleibt (Teilvernichtung ueber Uebertrag) und nur in einem schmalen v-Fenster vollstaendig ist.
- **V-5 (nebenbei):** B&S widersprechen Axenides u. a. [13], die die Leitung in Chem 8 L4 nebeneinander zitiert, in
  der Deutung des Rechtwinkel-Auslaufs (S. 3, S. 21 mit Fussnote 2). Fuer B&S ist das Spaltung durch Stauchung und
  keine Geometrie.

### 7. Regime und Moderatoren (Regel 1)

- Gleiche gegen ungleiche Frequenz (Moderator dw gegen Kopplung eps^2/M, [ES] nach Gl. 3.8):
  - Bei gleichem omega ist die Phase "gebunden" und der Uebertrag kumulativ (Abb. 9, 10).
  - Bei ungleichem omega laeuft die Phase. Dann gibt es nur eine Schwebung und keinen Nettouebertrag ohne Boost
    (Abb. 11; Chem 1).
  - Chem 1 und B&S Abb. 11 widersprechen sich nicht. Sie messen verschiedene Groessen: das Integral ueber die
    Halbachse mit einer Aufloesung von etwa 1e-3, gegen Dichtebilder nach Augenmass.
- Ruhend gegen geboostet: Uebertrag zwischen ungleichen Baellen braucht nach B&S Annaeherung (S. 16, Fazit S. 34).
- Stossversuch gegen Startueberlapp: LADUNGSTAUSCH-1 und CSZ starten eng und ruhend, B&S Abschn. 6 weit und
  geboostet. Das sind verschiedene Regime, kein Widerspruch.
- Kleine gegen grosse Ladung: Spaltung und Rechtwinkel-Auslauf vor allem bei omega_BS = 1,5 (omega^2 = 0,5625),
  bei 1,6 nur in einem engen v-Fenster (S. 26).

### 8. Unterscheidungspunkte (Regel 2)

- Chem 8, wer traegt den grossen Klumpen: "B&S-Kette A -> C -> B" gegen "C aus der Mitte gestossen".
  - Trennend ist die Bahn des groessten Klumpens.
  - Kette: Er kommt von x > 0 (B) und laeuft langsam nach aussen.
  - Gestossenes C: Er startet bei x = 0.
  - Kosten: Klumpenorte ueber t; Code vorhanden (Klumpenfinder).
- Chem 8, Ursache des v-Fensters: "kinetische Schwelle" gegen "Phase beim Kontakt" (Zeitdilatation mal Laufzeit).
  - Trennend ist ein veraenderter Startabstand X0 bei festem v.
  - Phasenbild: Das Fenster wandert etwa wie delta = omega v X0/2.
  - Kinetisches Bild: Das Fenster bleibt stehen.
- Chem 1, Schwebung gegen Kerntransport.
  - Trennend ist eine Messung an den Kernen: Scheitelwert f(0) oder Ortsfrequenz jedes Balls ueber t, statt der
    Ladung auf einer Halbachse.
  - Schwebung: Die Kerne bleiben fest, nur der Spalt schwingt.
  - Kerntransport: Die Kerne schwingen gegenphasig.
  - Ein Trennpunkt am Ort des grossen Balls trennt NICHT, weil beide Bilder dort e^{-kappa_min d} geben.
- R3-Richtungsregel "Elektronegativitaet" gegen "Phase beim Kontakt" (B&S S. 16): Bei festem d = 8 oder 10 die
  Anfangsphase variieren. Feste Richtung spricht fuer die Regel, Vorzeichenwechsel fuer die Phase.

### 9. Gegensweep (Regel 4): Was war selbstverstaendlich und ungeprueft?

- G1 Ist das Potential aus pdftotext richtig gelesen? **Geprueft** auf drei Wegen: Feldgleichung (3.1), exaktes
  Profil (2.11) und Q0 = 2,4415 aus Chem 8. Passt.
- G2 Hat unser Code dieselbe Phasenkonvention wie B&S? **Geprueft: nein**, er nutzt exp(-i omega t)
  (chem8_dicht.py Z. 182 bis 192). Jede Richtungsaussage kehrt sich in Codephasen um (Abschn. 5).
- G3 Ist a der halbe Abstand? **Geprueft:** Gl. (3.2), Baelle bei x = +-a, also d = 2a.
- G4 Sind die Chem-1-Baelle festgehalten? **Geprueft: nein**, sie sind frei (chem1_abstand.py Z. 309 bis 331). Nach
  B&S Abb. 11 stossen sie sich ab. Ob d waehrend T = 400 driftet, habe ich nicht geprueft (x_l wird im Code
  berechnet, Z. 342).
- G5 Ist arXiv v1 gleich der NPB-Fassung? **Nicht geprueft.** arXiv hat nur v1.
- G6 Die Abbildungsbilder habe ich nicht angesehen. "virtually no charge transfer" ist das Augenmass der Autoren.
- G7 Folgeliteratur der letzten 24 Monate (Dreierstoesse, Abstandsgesetz, Ref. [11]): **nicht gesucht**, weil das
  Suchbudget erschoepft ist. Darum steht hier kein "gibt es nicht" ueber andere Literatur; der Stand ist "nach
  Recherchestand nicht geprueft".
- G8 Die Leitung zitiert Axenides u. a. und B&S als gleichgerichtet. **Geprueft: nicht gleichgerichtet** in der
  Deutung der Rechtwinkelstreuung (V-5).

### 10. Kalibrierung

- (a) Gemessen:
  - die B&S-Simulationsaussagen ([A], ihre Laeufe, ohne Fehlerangaben, grossenteils nach Augenmass);
  - unsere Kartenzahlen (aus den Karten, nicht neu gerechnet).
- (b) Nuetzlich verdichtet ([ES]):
  - Modellidentitaet: algebraisch, dazu die Q0-Probe von Hand;
  - die Uebersetzung der Vorzeichenregel;
  - das Schwebungsbild fuer Chem 1: deckt Trennpunktgesetz und Phasenmuster ab, ist aber nicht gegen
    Kerntransport getestet.
- (c) Gewachsene Gewissheit ohne neue Evidenz:
  - die Chem-8-Vorhersage "B traegt": abgeleitet aus einer Regel, die B&S nur fuer zwei gleiche Baelle zeigen, nicht
    fuer laufende gegen ruhende und nicht fuer drei Baelle;
  - die Schranke "Durchfluss hoechstens einige Prozent": Kopfrechnung an sechs Tabellenwerten; die x0 = -2-Werte
    weichen ohnehin um bis 4 % ab.
- **Warnzeichen:** Meine Sicherheit im Schwebungsbild ist waehrend der Arbeit gestiegen, waehrend die Frage zerfiel
  (Spalt gegen Kerne, Halbachse gegen Kernfrequenz). Aus Gl. (3.3) folgt bei festen Profilen sogar eine schwankende
  Gesamtladung. Die Erhaltung erzwingt also ausgleichende Kernaenderungen; wo sie sitzen, ist nicht gemessen. Darum
  heisst das Urteil "Kerntransport nicht gezeigt", nicht "kein Kerntransport".

### 11. Offene Fragen

1. Chem 8: Bahn des groessten Klumpens (Vorhersage: B, x > 0, bei der Bruecke fuer beide dphi).
2. Chem 8: Wandert das v-Fenster mit X0?
3. Chem 1: Schwingen die Kerne (f(0), Ortsfrequenz)? Driftet d (x_l liegt vor)?
4. R3: Haengt die Richtung des Nettoflusses bei d = 8 und 10 von der Anfangsphase ab?
5. Ist Ref. [11] (Battye/MacKay/Sutcliffe, effektiver Hamilton) je erschienen? Gibt es Folgearbeiten zu
   Mehrballstoessen? Beides nicht gesucht (G7).
6. NPB-Fassung gegen arXiv v1.

### 12. Quellen

- R. A. Battye, P. M. Sutcliffe (2000), "Q-ball Dynamics", Nucl. Phys. B590, 329; arXiv:hep-th/0003252v1,
  https://arxiv.org/abs/hep-th/0003252 , https://arxiv.org/html/hep-th/0003252v1 , https://arxiv.org/pdf/hep-th/0003252v1
  (Lesetiefe [A], Text und Bildunterschriften, Bilder nicht angesehen).
- Innerhalb der Arbeit zitiert, NICHT von mir gelesen: Axenides/Komineas/Perivolaropoulos/Floratos, hep-ph/9910388
  (B&S Ref. [13]); Ahn/MacKay/Sepulchre 1999 (Ref. [18]); Battye/MacKay/Sutcliffe "in preparation" (Ref. [11]).
- Lokal gelesen: RUNDE-10/chem8/KARTE.md, RUNDE-11/chem8-mitte/KARTE.md, RUNDE-11/chem1/KARTE.md,
  RUNDE-11/chem1/lauf-69/t1_bericht.txt, RUNDE-10.md (LADUNGSTAUSCH-1, L4), RUNDE-11.md (Chem 1, Chem 8 Mitte),
  chem8_dicht.py (Z. 1 bis 9, 176 bis 192, 327 bis 350), chem1_abstand.py (grep-Zeilen), Paper v0.9 main.tex
  (Z. 82 bis 117, Tabelle Leiter), sections/LITERATURE.tex, LITERATURE-SOURCES.txt.

- Ende der Bearbeitung: 2026-10-01 17:51:06 CEST (date). Nichts gerechnet ausser Kopfrechnung (als [ES] markiert); kein python/awk, kein ssh/git/Peerbus.
