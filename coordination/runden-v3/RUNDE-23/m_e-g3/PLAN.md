# PLAN M_E-G3 (Theoriekarte RUNDE-16/m_e-g3/KARTE.md, Ausfuehrender Anthropic-Agent)

- Start der Sitzung 2026-10-02 22:10:55 CEST (date). Plan geschrieben ab 22:31:10 CEST (date). Zeitbox 150 min, also bis
  etwa 00:40 CEST.
- Frage, Vorabklassen A bis D und Vorhersage der Leitung gelten unveraendert (KARTE.md). Ich werte nur.
- Marken: [S] gelesen, [L?] nur Abstract oder Zitat, [ES] eigener Schluss, [E] eigene Rechnung.
- Abkuerzungen: CHLPSD = 2201.06602 (lokal v1-Text und PDF, RUNDE-13/spin2-d4/quellen/); BBIRRS = Bellazzini u. a.
  2512.13780v2 (ebd.); FRS = 2603.15755v2 (RUNDE-13/spin2-d4-2/quellen/). Seiten = gedruckte Seiten.

## 0. Lesestand vor dem Plan (offen gelegt)

Gelesen vor diesem Plan [S]: KARTE.md samt Nachtrag; SPIN2-D4-2.md ganz; codex-lesung/LESUNG.md (A1-A7);
WARUM-SPIN-2.md Glieder 7, 10 und Nachtraege ab 01.10.; CHLPSD Abschn. 2.1-2.4, 3.1-3.2 (mit PDF-Bild S. 10-12, 16-17, 19),
3.4-3.5, 4.1-4.2, Anh. A (PDF-Bild S. 38-39); BBIRRS Abschn. 1-5 (S. 1-18); FRS Abschn. 2 (S. 4-9), 4 (S. 24-34),
Anh. F (PDF-Bild S. 46-47).

Schon vor dem Einfrieren von Hand gerechnet (beim Lesen, nicht spaeter als "vorab" ausgeben):
- H1 [E, von Hand]: Aus CHLPSD (3.3a) mit (2.31a,b) und (2.32a) folgt |g^3|^2 M^8 <= 37,84 log(M/m_IR) - 45,45, also
  (3.4a), **nur wenn** der g5-Anteil von -5 d/dp^2 B4 weggelassen wird. Mit ihm steht zusaetzlich -5 g5 M^10/(27,49 pi G).
  Gleiches Muster bei (3.4b). Wird in W5a numerisch nachgeprueft.
- H2 [E, von Hand]: Woerterbuch g3 (Abschnitt 1 unten). Wird in W1 gegen (4.39)/(2.32a) gegengeprueft.

## 1. Normierungswoerterbuch g3 (Auflage A2), Stand vor der Rechnung

| Groesse | CHLPSD | FRS |
|---|---|---|
| Metrik, Mandelstam | mostly plus: s = -(p1+p2)^2, t = -(p2+p3)^2, u = -(p1+p3)^2, Gl. (2.4) | alle einlaufend: s = (p1+p2)^2, t = (p1+p3)^2, u = (p1+p4)^2, nach Gl. (2.3) |
| MHV-Amplitude | M(1+2-3-4+) = <23>^4 [14]^4 f(s,u), Gl. (2.1) | A(1h+,2h-,3h-,4h+) = <23>^4 [14]^4 (...), Gl. (2.3) |
| GR-Austausch | f = 8 pi G/(stu), Gl. (2.7a) | 1/(M_Pl^2 stu), Gl. (2.6) |
| Dreipunkt (+++) | (g^3/2) sqrt(8 pi G) ([12][13][23])^2, Gl. (2.6) | g3 [12]^2[23]^2[13]^2/M_Pl^3, S. 9 (txt Z. 551) |
| g3-Term in MHV | 2 pi G |g^3|^2 su/t, Gl. (2.7a) | M_Pl^-4 (g3^2/M_Pl^2) st/u, Gl. (2.3) |
| Kontakt | g4 + g5 t, Gl. (2.7a); g4 = 8 pi G (alpha4 + alpha4'), Gl. (2.11) | M_Pl^-4 (g4 + g5 u), Gl. (2.3) |
| Spin-4-Regel | -B4^(1)|low = 2 g4 + (4 pi G |g^3|^2 + g5) p^2, Gl. (2.32a) | M_Pl^4 B_0^4h|tree = g4 - (g3^2/M_Pl^2 + g5/2) t, Gl. (4.39) |

Abbildung [ES, H2]:
- Kinematik: s_F = s_C, t_F = u_C, u_F = t_C (gleicher Zahlenwert, (p1+p3)^2 bzw. (p2+p3)^2 in der jeweiligen Signatur).
- GR-Glieder gleichsetzen: M_Pl^-2 = 8 pi G, also M_Pl = reduzierte Planckmasse. Voraussetzung: gleiche Gesamtnormierung
  und Phasenkonvention der Amplituden (FRS Fn. 2: |-p> = i|p>); fuer |g3|^2 in der MHV-Amplitude ist die Phase egal.
- g3-Glieder: 2 pi G |g^3|^2 = (8 pi G)^3 g3^2, also **|g^3|^2 = 4 (8 pi G)^2 g3^2 = 4 g3^2/M_Pl^4**, |g^3| = 2|g3|/M_Pl^2.
  Gleiches Ergebnis aus den Dreipunktamplituden: g^3/2 * M_Pl^-1 = g3 M_Pl^-3.
- Kontakte: g4_C = g4_F/M_Pl^4, g5_C = g5_F/M_Pl^4.
- Probe: (2.32a) in FRS-Groessen ergibt -B4^(1) = (2/M_Pl^4)[g4_F + (g3^2/M_Pl^2 + g5_F/2) p^2]; mit t_F = -p^2 ist das
  2 x (4.39)/M_Pl^4. Also B_0^4h(FRS) = -B4^(1)(CHLPSD)/2. Stimmt [E, von Hand].
- Damit x = |g^3|^2 M^8 = 4 (g3_F M^2)^2 (8 pi G M^2)^2.
- G-Grenzfall: bei festem g^3 (CHLPSD; alpha3 fest in der Wirkung mit Vorfaktor 1/16 pi G) haengt x nicht von G ab.
  Bei festem g3_F (FRS; natuerlich g3_F ~ 1/(g* M)^2, Text zu (2.3)) geht x wie G^2 gegen null. Die Zahl 24,9 aus CHLPSD
  (4.4) gilt fuer x in CHLPSD-Normierung.
- Offener Punkt im Woerterbuch: FRS (2.3) schreibt g3^2, nicht |g3|^2. Bei komplexem g3 (paritaetsungerader Anteil) wird
  angenommen, dass |g3|^2 gemeint ist. In W1 an FRS S. 9 pruefen.

## 2. Festgelegte Skalierung (vor der Rechnung)

**Skalierung S:** G -> 0, E -> 0 mit G_E = G M^2 log(M/E) fest (BBIRRS Gl. (1.1)) und
**xi = x/log(M/E) fest**, also x = |g^3|^2 M^8 = xi log(M/E).
- Gleichwertig: y := G M^2 x = xi G_E fest. y misst die kubische R^3-Kopplung der Gravitonen
  (Dreipunkt ~ sqrt(8 pi G) g^3 ~ sqrt(y)) als kurzreichweitige Kopplung, die im Grenzfall endlich bleibt.
- Zweiter Schritt nach S: G_E klein (G_E -> 0), um den Baumkoeffizienten c_0 zu isolieren.
- Gegenprobe ohne S: x fest (x = O(1)). Erwartung: dann liegt jeder g^3-Term im O(G M^2)-Rest (Vorlaeufer).
- Zielaussage, falls A oder B: x <= c log(M/E) + Rest, c in CHLPSD-Normierung, Rest ausdruecklich benannt.

## 3. Erwartungen vor der Rechnung (date 22:31:10, keine Ergebnisdatei existiert)

- E1 (~60 %): Unter S stehen die x-Terme der B2/B3-Regeln in fuehrender Ordnung (O(G_E), O(y)). Damit greift die
  Positivitaet fuehrender Ordnung nach BBIRRS (5.7)-(5.14), und eine Restabschaetzung subfuehrender Unitaritaet wird fuer
  die fuehrende Log-Ordnung nicht gebraucht.
- E2 (~70 %): Exakte Vorwaertslimites (d/dp^2 B4 bei p = 0, verbesserte Regeln (3.11)-(3.13)) sind in M_E nicht
  gleichmaessig kontrolliert, weil die Ein-Schleifen-GR-Glieder bei t -> 0 wie log(-t/E^2)/t gehen (FRS (F.7)).
  Zulaessig sind dann nur ganz verschmierte Funktionale.
- E3 (~60 %): Das einzige ausdruecklich angegebene reine B2/B3-Funktional (CHLPSD Fn. 10, Gl. (3.7)) gibt c_0 = 1598 und
  ist auf allen schweren Zustaenden positiv (Stichprobe). 1598 liegt weit ausserhalb Faktor 3 von 24,9.
- E4 (~50 %): Ein kleines lineares Programm mit reinen B2^(1)/B3^(1)-Funktionalen (Polynomgrad bis 10) erreicht c_0
  zwischen 100 und 1000, nicht unter 75.
- E5 (~65 %): Die Doppel-Logs aus FRS (F.3) gehoeren unter S zur fuehrenden Ordnung (Terme G^2 L^2 = G_E^2) und
  aendern c um einen relativen Anteil O(G_E). Sie sind in der EFT berechenbar, kein Unitaritaetsrest. Die nicht
  log-verstaerkten Ein-Schleifen-Reste bleiben O(G).
- E6 (~55 %): Die Leitung landet bei Klasse A oder B. Mein Gesamtausgang: A mit c weit ueber 75 (40 %), B (25 %),
  C (30 %), D (5 %).

## 4. Arbeitsschritte

- W1 Woerterbuch: Abschnitt 1 gegen FRS S. 9 (g3 reell oder komplex) und (4.39) pruefen.
- W2 Ordnungszaehlung unter S: alle Terme der B2-, B3-, B4-Regeln auf der IR-Seite nach Ordnung (fuehrend O(G_E), O(y),
  Rest O(G M^2)) einordnen: Baum-Pol, Baum-g^3, Kontakte, GR-Ein-Schleife (FRS (F.2), (F.3), (F.7)), gemischte Schleifen
  (g^3 x GR), g^3-Quadrat-Schleifen, Kontakt-Schleifen. Quelle der Positivitaet: BBIRRS (4.6), (4.10), (5.7)-(5.17).
- W3 Scheiterregel (aus SPIN2-D4-2, "Weg und fehlende Rechnung"): Bleiben die nicht log-verstaerkten
  Ein-Schleifen-Reste des B2-Smearings O(G)? Tragen die Doppel-Logs aus (F.3) ein log(M/E) in den fuehrenden
  Koeffizienten, und ist dieser Beitrag kontrolliert oder nicht? Ausdruecklich mit der Impuls-Erhaltung s + t + u = 0.
- W4 Spin-4-Luecke ohne Mehrgraviton-Kontinuum: Definition von M als EFT-Grenze; Zweigraviton-Zustaende unter M als
  EFT-Schleifen, ueber M als positive UV-Dichte.
- W5 Funktionale (Rechnungen nur auf der .69 ueber kleintest.sh, je <= 10 min, ein Thread):
  - W5a: (3.3a) -> (3.4a) nachrechnen, mit und ohne g5.
  - W5b: (3.7) -> 1598 log - 3211 nachrechnen (Normierung K = Int(psi3 p^4 - psi2 p^6)).
  - W5c: Positivitaet von (3.7) auf schweren Zustaenden (m >= M, J bis ~200, ++ und +-) und im Grenzfall m -> unendlich
    bei festem b, mit Glaettung ab p = 0 (BBIRRS (5.9), (5.13)).
  - W5d: kleines LP: maximiere K bei a1 = 1 unter Positivitaet (Gitter in m und J, Grenzfall b, Grossb-Bedingung
    p^2-Koeffizient von psi2 < 0); c_0 = 8 a1/K. Gitterpositivitaet ist kein Beweis; so auch kennzeichnen.
  - W5e (nur [ES]): Vorwaertslimites ueber schmale Glaettung bei E << E' << M; welcher Rest entsteht?
- W6 Fehlerbudget der O(G)-Reste (Tabelle).
- W7 Einordnung A-D (Kriterien unten), c in CHLPSD-Normierung, Abgleich mit der Vorhersage.
- W8 Gegensweep: arXiv-API und Semantic Scholar (Zitate von 2512.13780 und 2603.15755; D = 4, IR-Logs, Regge-Einwaende,
  Chang/Parra-Martinez 2501.17949, Beadle u. a. 2501.18465 liegen lokal vor).
- W9 ERGEBNIS.md nach Vorgabe; ARBEITSFELD.md als Protokoll.

## 5. Bewertungskriterien (meine Lesart der bindenden Klassen, vor der Rechnung)

- A, wenn: (i) unter S die x-Terme in der von BBIRRS kontrollierten fuehrenden Ordnung liegen, (ii) ein ausdruecklich
  angegebenes, in M_E zulaessiges Funktional (ohne exakte Vorwaertslimites) existiert und seine Positivitaet geprueft ist,
  (iii) alle uebrigen Terme gleichmaessig O(G M^2) sind fuer (G_E, xi) in kompakten Mengen, und (iv) keine Annahme ueber
  die von CHLPSD und BBIRRS schon gemachten hinaus noetig ist.
- B, wenn (ii) oder (iii) nur mit einer benannten Zusatzannahme gelingt (z. B. meromorphe UV-Baumamplitude BBIRRS S. 13,
  oder Vorwaertslimites "wie bei CHLPSD").
- C, wenn ein Schritt offen bleibt, den ich genau benennen kann (z. B. funktionale Unitaritaet (4.10) fuer aeussere
  Gravitonen mit Helizitaet nur behauptet, oder Positivitaet nicht pruefbar).
- D, wenn ein Struktursatz oder Gegenbeispiel zeigt, dass unter S keine Schranke moeglich ist.
- Uebertragungen aus BBIRRS, die dort nur "analogous statement holds in gravity" heissen, zaehle ich als Teil des
  M_E-Rahmens, nicht als neue Annahme; ich nenne sie aber einzeln.

## 6. Regeln und Abbruch

- Lokal kein python/awk/bc; Rechnungen nur ueber kleintest.sh auf der .69 (Spuren cpu, cpu2, cpu4, cpu6),
  OMP/OPENBLAS/MKL_NUM_THREADS=1 im Skript. Syntaxpruefung nur dort per py_compile.
- Zeiten nur per date. Heredocs gequotet. Kein git, kein Peerbus, keine Unteragenten. Gesperrte Pfade nicht lesen.
- Abbruch: Wenn um 00:15 das LP nicht steht, ohne LP auswerten (Klasse und c nur aus W5a-c). Wenn W2 zeigt, dass die
  Frage so nicht beantwortbar ist, sauber als C oder D begruenden statt Zeit zu fuellen.
