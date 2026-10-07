# SCHACHBRETT-KAUSAL-1: Ergebnis (Code-Agent fuer die Leitung, Runde 38, explorativ)

- Gerechnet auf der .69 nur ueber kleintest.sh: Spuren cpu7 und p4000a (nur CPU), hoechstens zwei Laeufe zugleich.
- **Zeiten** (date; .69 in UTC, CEST = UTC + 2):
  - Start 06:19:19 CEST. Ein Literaturabruf (Johnstons Doktorarbeit, PDF lokal gelesen).
  - Rauch 04:43:56 bis 04:49:23 UTC. Plantext ab 06:47:17 CEST.
  - **Eingefroren 06:49:50 CEST:**
    - PLAN.md.eingefroren-20261004-064950
    - code/*.eingefroren-20261004-064950
    - sha256 in code/pruefsummen-einfrieren.txt
  - Hauptlaeufe 04:49:59 bis 04:56:39 UTC: 8 Starts, alle rc = 0, kein Abbruch.
  - Auswertung 04:56:51 bis 04:56:57 UTC. Text ab 06:59:21 CEST.
- **Hashes:**
  - Alle 65 Laufdateien tragen die sha256 des eingefrorenen kausal_dirac.py (7b6f3fb5...): 32 Pakete, 32 Punktquelle,
    1 Codeprobe.
  - Die 64 Feldlaeufe nennen dazu kausal_welle.py (2f897e12..., unveraendert aus KAUSAL-WELLE-1).
  - schachbrett.json, kontinuum.json und auswertung.json tragen die eingefrorenen Hashes (71d49b70..., 8b6f1cc8...,
    5ef8ec75...).
  - Plan und Code sind nach dem Einfrieren unveraendert (sha256sum -c um 06:58:59 CEST).
- **Kennzeichen:**
  - [S] an der Quelle gelesen; [L] Literatur aus dem Gedaechtnis, [L?] unsicher; [H] Hypothese
  - [M] eigene Mathematik; [E] hier gerechnet (synthetisch, keine Messdaten); [F] Festlegung des Plans
- **Quellen:**
  - **[S]** S. P. Johnston, "Quantum Fields on Causal Sets", Doktorarbeit, Imperial College London 2010,
    arXiv:1010.5514v1. Die Nummer stimmt.
    - Kapitel 6 "Spin-half Particles" (S. 142 bis 152) enthaelt zwei Skizzen, aber keine fertige Bauweise.
    - **6.3, Schachbrett ueber "chain intervals":** Die Konstanten A und B sind offen. Wortlaut: "Calculating these
      matrices explicitly is difficult". Dazu setzt (6.11) K_++ = K_-- [M: kann R und L nicht trennen].
    - **6.4, Wurzel des Propagators:** Wortlaut: "This remains a task for future work."
  - **[S, aus KAUSAL-WELLE-1]** Johnston, arXiv:0806.3083: (3.5), (3.23), (3.31).
  - **[S nur als Zitat bei Johnston]** Feynman/Hibbs 1965, Jacobson/Schulman 1984; die Originale nicht gelesen.

## 1. Ergebnis zuerst

1. **Ein 1+1-Fermion laeuft auf der Kausalmenge im Mittel wie im Kontinuum, wenn man Feynmans Zickzack umgruppiert
   [M, E].**
   - Jedes Element ist ein Paar von Richtungswechseln. Die Ecke dazwischen liegt am Schnitt der Lichtstrahlen zweier
     aufeinanderfolgender Elemente.
   - Dann ist die Zickzack-Summe Johnstons Kettensumme mit Stop-Amplitude -m^2/(2 rho). Lichtstrahlen braucht man nur an
     Quelle und Messpunkt; dort rechne ich sie analytisch.
   - Das Saatmittel trifft das Kontinuum an 90 von 92 Pruefpunkten innerhalb 3 SE (rho = 800; bei rho = 200: 89 von 92).
     Geprueft sind beide Propagator-Komponenten bis tau = 16 und zwei Wellenpakete.
   - Das war im Mittel vorab ableitbar (PLAN 1.4). Nicht ableitbar sind die Ergebnisse 2 bis 4.
2. **Das Rauschen faellt wie rho^(-1/2) [E].**
   - Steigung -0,496 (Propagator -0,498, Pakete -0,487).
   - Die relative Streuung (geometrisches Mittel) sinkt von 8,9 % auf 4,4 %.
3. **Stabil [E]:** Die Paketnorm liegt hoechstens 5 % (rho = 200) bzw. 1,6 % (rho = 800) ueber dem Kontinuum. Zuwachs ueber
   die Laufstrecke 20/m: G <= 1,014.
4. **Zitterbewegung auf dem Netz [E]:**
   - Die reine R-Quelle wechselt zwischen den Komponenten: Der R-Anteil schwingt zwischen 0,30 und 0,85.
   - Kreisfrequenz 1,98 ~ 2m (Kontinuum), langsam gedaempft.
   - Das Saatmittel folgt der Kurve auf 0,025 (rho = 200) bzw. 0,005 (rho = 800).
5. **Die Kontrolle SK0 ist verfehlt [E]:**
   - Feynmans ungenormtes Schachbrett weicht bei eps = 0,01 um bis zu 0,0295 ab, Schwelle 1e-2. Der Fehler ist erster
     Ordnung (Steigung 1,04).
   - Nur bis tau = 1 haelt es die Schwelle.
   - Ursache [M]: Jeder Schritt vergroessert die Amplitude um sqrt(1 + m^2 eps^2). Normiert sind es 0,0034 (beschreibend).
   - Das war vor dem Einfrieren aus dem Rauch bekannt.
   - **Urteile:** SK0 nicht eingetroffen, SK1, SK2 und SK3 eingetroffen.

## 2. Urteile

Mechanisch nach PLAN.md (eingefroren 06:49:50 CEST) durch code/auswertung.py; Werte in lauf-69/auswertung.json. Die
Felder "vermerk" sind per jq nachgetragen; ohne sie ist die Datei identisch mit lauf-69/auswertung.maschine.json (diff).

| Nr | Vorhersage (Kurzform) | Wahrsch. | Urteil | Kartenwortlaut | Werte |
|---|---|---|---|---|---|
| SK0 | Schachbrett trifft Dirac-Propagator auf <= 1e-2 bei eps = 0,01, Steigung 1 +- 0,2 | 85 % | **nicht eingetroffen** | gleich | E(0,01) = 0,0295 (S_RR, zeta = 1, tau = 12); Steigung 1,040 (im Band) |
| SK1 | [H] Saatmittel trifft Kontinuum an >= 90 % der Pruefpunkte in 3 SE (rho = 800) | 35 % | **eingetroffen** | gleich | 90 von 92 (97,8 %); Propagator 78 von 80, Pakete 12 von 12; groesste Abweichung 3,98 SE |
| SK2 | [H] relative Streuung faellt mit Steigung -0,5 +- 0,15 (200 -> 800) | 45 % | **eingetroffen** | gleich | -0,496 |
| SK3 | Norm waechst um hoechstens Faktor 1,5 gegen Kontinuum | 50 % | **eingetroffen** | gleich | G <= 1,014 in 4 von 4 Faellen; max R = 1,050 |

- **SK0, Pruefbereich (PLAN 6.1, vor dem Einfrieren offengelegt):**
  - Die Karte nennt keinen Pruefbereich. Mit den geerbten Pruefpunkten (t bis 24,7) liegt das Schachbrett ab tau = 2
    ueber der Schwelle.
  - Schwelle und Pruefpunkte standen vor dem Rauch im Code und sind unveraendert. Urteil nach Wortlaut = Urteil nach Plan.
- **SK1, vorab ableitbar (PLAN 1.4 und 6.2):**
  - Die 35 % der Karte bezogen sich auf eine naheliegende Link-Bauweise.
  - Fuer die Eckpaar-Kette folgt E[psi] = Kontinuum aus der Kettenentwicklung (Poisson, Palm).
  - Eingetroffen heisst hier: Umgruppierung, Herleitung und Code stimmen. Es ist kein offener Physikbefund.
- **Meine Vorab-Erwartung** (PLAN 5.1): SK0 nicht (aus dem Rauch bekannt), SK1 ein (90 %), SK2 ein (75 %), SK3 ein
  (90 %). Keine Abweichung.
- **Bedeutung nach der Karte (vorab):**
  - Ausgeloest ist der Zweig "SK1 bis SK3 treffen ein: Auf einem Raumzeit-Netz ohne Ruhesystem laeuft auch ein Fermion (die
    1+1-Fassung eines Elektrons) im Mittel wie im glatten Raum."
  - Einschraenkungen in Abschnitt 6.

## 3. Tabellen

### 3.1 SK0: Schachbrett gegen Kontinuum [E]

| eps | max. Abweichung (80 Pruefwerte) | normiert (beschreibend) |
|---|---|---|
| 0,02 | 0,0620 | 0,0070 |
| 0,01 | **0,0295** | 0,0034 |
| 0,005 | 0,0144 | 0,0017 |
| 0,0025 | 0,0071 | 0,00085 |
| Steigung | 1,040 | 1,014 |

- "Normiert" heisst: mit dem Faktor (1 + m^2 eps^2)^(-t/(2 eps)) multipliziert, also ohne den Normzuwachs des Schritts.
- **Groesste Abweichung je tau bei eps = 0,01** (ueber zeta und Komponente):

  | tau | 0,5 | 1 | 2 | 3 | 5 | 8 | 12 | 16 |
  |---|---|---|---|---|---|---|---|---|
  | Abw. | 0,0032 | 0,0056 | 0,0122 | 0,0109 | 0,0175 | 0,0202 | 0,0295 | 0,0164 |

  - Sie liegt jeweils bei S_RR und zeta = +1. Dort ist S_RR am groessten (Faktor e^zeta).
  - S_LR bleibt bei <= 0,012 (zeta = -1, tau = 16).
  - Das passt zur Schreibtisch-Formel (PLAN 1.3), Fehler etwa (m^2 eps/2) t abs(S): bei tau = 12, zeta = 1 ist das
    0,005 * 18,5 * 0,30 = 0,028.
- Binomialprobe (Rekursion gegen geschlossene Pfadzaehlung): 1,3e-15.
- Bild lauf-69/schachbrett_fehler.png.

### 3.2 Propagator auf der Kausalmenge: relative Streuung ueber 16 Saaten (zeta = 0) [E]

| tau | 0,5 | 1 | 2 | 3 | 5 | 8 | 12 | 16 |
|---|---|---|---|---|---|---|---|---|
| S_LR, rho = 200 | 0,008 | 0,029 | 0,143 | 0,072 | 0,152 | 0,196 | 0,518 | 0,120 |
| S_LR, rho = 800 | 0,006 | 0,010 | 0,065 | 0,037 | 0,059 | 0,070 | 0,310 | 0,071 |
| S_RR glatt, rho = 200 | 0,005 | 0,016 | 0,034 | 0,085 | 0,103 | 0,177 | 0,223 | 0,563 |
| S_RR glatt, rho = 800 | 0,004 | 0,007 | 0,016 | 0,047 | 0,054 | 0,100 | 0,172 | 0,296 |

- S_LR bei tau = 12 liegt nahe einer Nullstelle von J0 (J0(12) = 0,048). Daher der grosse Relativwert.
- S_RR hat am Ende einen analytischen Lichtstrahl (Gewicht V_x - V_y).
  - Es streut in derselben Groessenordnung wie S_LR. Der grosse Relativwert bei tau = 16 kommt vom kleinen Betrag dort
    (abs(S_RR) = 0,045 bei zeta = 0).
  - Es faellt ebenso mit rho (Steigung Propagator gesamt -0,498).
- Saatmittel gegen Kontinuum fuer zeta = -1 und 0: lauf-69/saatmittel_kontinuum.png. Die Punkte liegen auf den
  Bessel-Kurven.

### 3.3 Pakete an den Pruefpunkten [E]

| Paket | t | Komp. | abs(psi) Kontinuum | rel. Streuung 200 | rel. Streuung 800 | Abw. in SE (800) |
|---|---|---|---|---|---|---|
| zitter | 3 | R | 0,815 | 0,042 | 0,024 | 0,92 |
| zitter | 3 | L | 0,211 | 0,148 | 0,080 | 0,09 |
| zitter | 13 | R | 0,165 | 0,273 | 0,105 | 0,52 |
| zitter | 13 | L | 0,380 | 0,083 | 0,057 | 0,80 |
| zitter | 23 | R | 0,062 | 0,499 | 0,322 | 1,24 |
| zitter | 23 | L | 0,312 | 0,130 | 0,072 | 0,90 |
| bewegt | 12 | R | 7,448 | 0,117 | 0,055 | 1,16 |
| bewegt | 12 | L | 2,786 | 0,115 | 0,054 | 1,17 |
| bewegt | 22 | R | 7,359 | 0,109 | 0,050 | 1,48 |
| bewegt | 22 | L | 2,745 | 0,110 | 0,051 | 1,53 |
| bewegt | 32 | R | 7,237 | 0,127 | 0,058 | 0,94 |
| bewegt | 32 | L | 2,690 | 0,126 | 0,059 | 0,96 |

- Beim bewegten Paket haben R und L dieselbe relative Streuung. Die Rekursion laeuft je Komponente getrennt; gemeinsam
  ist nur die Streuung (Punktlage).

### 3.4 Norm (Fenster) gegen Kontinuum, R = Saatmittel(n)/n_c [E]

| rho | Paket | R Anfang | R Ende | G | max R |
|---|---|---|---|---|---|
| 200 | zitter | 1,009 | 1,023 | 1,014 | 1,050 |
| 200 | bewegt | 1,017 | 1,027 | 1,009 | 1,037 |
| 800 | zitter | 0,998 | 1,002 | 1,003 | 1,009 |
| 800 | bewegt | 1,003 | 1,009 | 1,006 | 1,016 |

- R - 1 faellt etwa wie 1/rho. Das ist die Rauschleistung E abs(delta psi)^2, kein Anwachsen.
- Das Kontinuum haelt die Norm im Fenster auf 4e-4 (zitter 2,8981 -> 2,8970; bewegt 567,56 -> 567,77).
- Max abs(psi) an Elementen: 9,3 (rho = 200) bzw. 8,4 (rho = 800), alles endlich. Bild lauf-69/norm_t.png.

### 3.5 Komponentenwechsel (beschreibend) [E]

- **zitter:**
  - Anteil abs(psi_R)^2 an der Norm (Fenster): 0,85 bei t = 3, dann Schwingung zwischen etwa 0,30 und 0,82, langsam
    gedaempft (0,45 bis 0,72 bei t ~ 21; Werte aus dem Bild abgelesen).
  - Kreisfrequenz aus den Nulldurchgaengen des Kontinuums: 1,984, also nahe 2m. Etwas Abweichung ist zu erwarten, weil
    das Paket Impulse um 0 mit omega_k = sqrt(1 + k^2) >= m enthaelt [M].
  - Saatmittel gegen Kontinuum: groesste Abweichung 0,025 (rho = 200), 0,0051 (rho = 800).
  - Das Streuband je Saat ist schmal (lauf-69/komponentenwechsel.png).
- **bewegt:**
  - R-Anteil konstant 0,8782 (positiver Spinor bei eta = 1: e/(2 cosh 1) = 0,881).
  - Saatmittel auf 1,6e-4 bzw. 5e-5 genau.

## 4. Kontrollen

- **Codeprobe** (rho = 5, N = 1982, beide Pakete):
  - CDQ-Rekursion gegen dichte Loesung (I + a A) psi = s: 2,5e-15
  - Zuschauersummen (auch V-gewichtet) gegen Maskensumme: 3,0e-15
  - analytische Quellterme s_R, s_L gegen direkte Gauss-Legendre-Quadratur an 5 Punkten: <= 3,6e-13
- **Kontinuum, zwei unabhaengige Wege:**
  - k-Raum (Duhamel exakt, D'' auf die skalare Loesung) gegen direkte Faltung mit dem analytischen Dirac-Propagator
    (delta-Teil als Strahlintegral, J0- und J1-Teile 2D): <= 4,4e-15 (zitter) und <= 2,9e-13 (bewegt), 6 Pruefpunkte.
  - Damit sind S = D'' G, Normierung und Vorzeichen der J1-Teile und die delta-Teile doppelt bestaetigt.
  - Normanteil am Klassenrand <= 4,3e-31.
- **Unverzerrtheit, beschreibend:**
  - Signierte Abweichungen der 80 Propagatortests: Mittel +0,16 SE (rho = 200), -0,37 SE (rho = 800).
  - Korrelation zwischen den Dichten: -0,23. Ein gemeinsamer Fehler wuerde bei beiden Dichten dieselbe Richtung zeigen.
- **Ausreisser:**
  - Ueber 2 SE liegen 10 von 92 (rho = 800) bzw. 12 von 92 (rho = 200), ueber 3 SE 2 bzw. 3.
  - Fuer unabhaengige t-Verteilungen mit 15 Freiheitsgraden waeren ~6 bzw. ~0,8 zu erwarten.
  - Die Tests sind nicht unabhaengig: Die 40 Propagatorpunkte einer Saat stammen aus einer Streuung. Benachbarte tau und
    zeta teilen den Grossteil ihrer Vergangenheit. Beispiel rho = 800: S_LR bei tau = 1 und zeta = 0 / 1 liegen bei -3,98 /
    -2,0 SE in derselben Richtung.
  - Ob das den Ueberschuss ganz erklaert, habe ich nicht geprueft (Selbstanzeige 5).
- **Laufzeit:**
  - Pakete rho = 800: N = 2,58 Mio., 28,7 bis 30,2 s je Saat; rho = 200: 6,5 bis 7,4 s
  - Punktquelle: 0,5 s bzw. 2,2 s
  - Schachbrett 1,5 s, Kontinuum 9 s
  - Wandzeit der Hauptlaeufe ~7 min (cpu7 6 min 40 s, p4000a parallel 3 min 55 s)

## 5. Latten (v3)

- **L1 kann scheitern:**
  - SK0 ist gescheitert.
  - SK1 konnte nur an einem Fehler in Umgruppierung, Herleitung oder Code scheitern, denn der Erwartungswert ist
    ableitbar. Das ist eine schwache Latte.
  - SK2 haette an einem anderen Exponenten scheitern koennen. Moeglich waere das beim V-gewichteten Zuschauer gewesen,
    oder bei Paketen, deren Rauschen ueber den ganzen Zukunftskegel waechst.
  - SK3 haette an einer Instabilitaet der Rekursion scheitern koennen.
- **L2 Gegenprobe:**
  - dichte Loesung, Maskensumme, Quadratur der Quellen
  - k-Raum gegen direkte Faltung (zwei Herleitungen von S)
  - Binomialsumme, zwei Dichten, zwei Pakete
  - normiertes Schachbrett
- **L3 Numerik:** 1e-15 bis 3e-13; Schachbrett bilinear interpoliert (Fehler O(eps^2), kleiner als der gemessene
  O(eps)-Fehler).
- **L4 schon bekannt:**
  - Schachbrett -> Dirac in 1+1 [S als Zitat: Feynman/Hibbs 1965; Jacobson/Schulman 1984].
  - Johnstons Skizzen fuer Spin 1/2 auf Kausalmengen, ohne fertige Bauweise [S, Kap. 6].
  - Jede Dirac-Komponente in 1+1 erfuellt die Klein-Gordon-Gleichung [L, Lehrbuch].
  - Die Umgruppierung in Eckpaare und die Rueckfuehrung auf Johnstons Kettensumme habe ich selbst hergeleitet [M]. Sie kann
    in der Literatur stehen [L?].
  - Dass das ungenormte Schachbrett die Norm nicht erhaelt, ist vermutlich bekannt; normierte Fassungen gibt es
    [L?, etwa Skopenkov/Ustinov zu "Feynman checkers"].
- **L5 Messbezug:** keiner (synthetisch, 1+1, freies Feld).

## 6. Bedeutung

- **Fuer Ue3 und Weg 3 [E, M]:**
  - In 1+1 braucht ein Fermion im Inneren des Netzes keine Lichtstrahlen.
  - Feynmans Zickzack laesst sich so umgruppieren, dass jedes Element ein Paar von Richtungswechseln ist. Die Ecke
    dazwischen liegt dann am Schnitt der Lichtstrahlen zweier Elemente.
  - Uebrig bleibt Johnstons Kettensumme ueber alle Relationen. Sie ist unverzerrt, ihr Rauschen faellt wie rho^(-1/2),
    und sie ist stabil.
  - Die Chiralitaet (R oder L) steckt nur an den Enden, an Quelle und Messpunkt. Dort kommen die Lichtrichtungen aus der
    Einbettung (halb-intrinsisch).
- **Johnstons Ansatz 6.3 [M]:**
  - Er setzt K_++ = K_--, benutzt also nur die Kausalordnung.
  - Im Kontinuum ist S_RR/S_LL = e^(2 zeta). Die R/L-Information muss deshalb von aussen kommen, etwa aus den zwei
    linearen Ordnungen (u- und v-Ordnung) der 2D-Ordnung.
  - Ob diese Zerlegung intrinsisch bis auf Vertauschung eindeutig ist, bleibt offen [L?].
- **Grenzen:**
  - Im Mittel war das Ergebnis vorab ableitbar.
  - Links werden nicht benutzt. Ein reines Link-Zickzack habe ich nicht gerechnet. Der Schreibtisch dazu (PLAN 1.5)
    erwartet Verzerrung und Rauschen ohne Fall mit rho, wegen der logarithmisch verteilten Linklaengen [H].
  - **Spin 1/2 in 3+1 bleibt offen [H]:** Die Umgruppierung nutzt, dass es in 1+1 genau zwei Lichtrichtungen gibt und ein
    Eckpaar ein Punkt der Ebene ist. In 3+1 ist schon das Kontinuums-Schachbrett nicht einfach [S als Zitat: Feynman
    unveroeffentlicht, Jacobson/Schulman].
- **SK0 [M, E]:**
  - Feynmans Regel (Amplitude 1 geradeaus, -i m eps je Ecke) ist nicht unitaer. Ihr Fehler waechst wie (m^2 eps/2) t.
  - Fuer lange Laufzeiten muss man normieren. Mit Normierung faellt der Fehler hier auf etwa ein Neuntel (0,0295 ->
    0,0034 bei eps = 0,01).
  - Das gilt fuer jedes Gitter-Schachbrett, das als Kontrolle dienen soll [H].

## 7. Selbstanzeigen

1. **Keine Interpreterstarts ausserhalb des Starters**, auch keine Versionsproben. Lokal kein python, awk oder perl.
   - Benutzt: jq, grep, sed, sha256sum, date, ssh, scp.
   - Dazu Datei- und Textbefehle: cp, mkdir, chmod, ls, diff, cat, head, tail, sort, uniq, wc, tr, du.
   - Gewartet habe ich mit until-Schleifen. Ein direktes "sleep 45" lehnte das Werkzeug ab.
2. **SK0 vor dem Einfrieren gesehen** (erlaubt, PLAN 8):
   - Pruefpunkte und Fehlermass standen vorher im Code und blieben unveraendert.
   - Meine "Erwartung" zu SK0 in PLAN 5.1 ist deshalb keine Vorhersage.
3. **Hauptbauweise im Mittel vorab ableitbar** (PLAN 1.4). SK1 traegt deshalb wenig Information ueber die Physik. Das
   Neue sind Streuung, Stabilitaet, Komponentenverhalten und die Umgruppierung selbst [M].
4. **Halb-intrinsisch:** Die Lichtrichtungen kommen an Quelle und Messpunkt aus der Einbettung (U, V). Die Rekursion selbst
   nutzt nur die Kausalordnung. Die beschreibende zweite Bauweise (Link-Zickzack) ist nicht gerechnet. Gruende: Zeitbox und
   offene Gewichtswahl.
5. **Ausreisser:** 2 bzw. 3 Tests liegen ueber 3 SE, mehr als bei unabhaengigen Tests zu erwarten.
   - Ich schreibe das der Korrelation der Tests zu. Gezeigt habe ich es nicht.
   - Gegen eine Verzerrung sprechen: die Herleitung; keine gemeinsame Richtung zwischen den Dichten (Korrelation -0,23);
     die Pakete mit 12 von 12 Tests innerhalb 1,6 SE bei rho = 800 (bei rho = 200 einer bei 2,7 SE).
6. **Pruefpunkte:** von KAUSAL-WELLE-1 geerbt, zeta auf -1 bis 1 erweitert, weil R und L nicht symmetrisch sind [F]. Die
   L-Quelle ist nur ueber die Spiegelung abgedeckt, nicht eigens gerechnet.
7. **Pakete [F]:** "zitter" hat omega = 0 und ist kein Teilchenzustand. Ich habe es gewaehlt, um die Zitterbewegung zu
   zeigen. Fenster W = 34 (zitter) und 16 (bewegt), nur aus dem Kontinuum.
8. **SK2** buendelt 92 Pruefgroessen, auch solche nahe Nullstellen. Die Steigung haengt nur vom Verhaeltnis der Streuungen
   ab, nicht vom Kontinuumswert.
9. **Speicheranzeige:** systemd meldet "Memory peak" ~0,3 MB (Zaehlung der Huelle). Kein Lauf ueberschritt MemoryMax 4G
   (alle rc = 0).
10. **Kein frischer Gegenleser** fuer Herleitung, Code und Text.
11. **Literatur:** ein WebFetch; das PDF habe ich lokal mit dem Lesewerkzeug gelesen (Seiten 1 bis 8 und 142 bis 153).
    Jacobson/Schulman und Feynman/Hibbs kenne ich nur aus Johnstons Zitat.
12. **Code-Hinweis "Fenwick O(N log N)":** benutzt ist die CDQ-Rekursion O(N log^2 N) aus KAUSAL-WELLE-1, unveraendert.
13. **Zeitbox:** Start 06:19:19 CEST; Text ab 06:59:21 CEST; Abschluss 07:03:15 CEST (date), also 44 min von 120.

## 8. Naechste Schritte [H]

- **Intrinsische Lichtrichtungen:**
  - u- und v-Ordnung aus der 2D-Ordnung selbst gewinnen (Zerlegung in zwei lineare Ordnungen).
  - Pruefen, ob R/L damit bis auf Vertauschung eindeutig ist.
- **Link-Zickzack als Gegenprobe** auf kleinem Gebiet: Traegt die Linkdichte-Vorhersage (Verzerrung, Rauschen ohne Fall)?
- **3+1:** Gibt es eine Eckpaar-Umgruppierung fuer ein 3+1-Schachbrett, etwa auf Ketten mit Richtungsmarken?
- **Mehrere Fermionen:** Antivertauschung ueber Johnstons Pauli-Jordan-Ansatz (6.25), (6.26) [S].

## 9. Dateien

- PLAN.md, PLAN.md.eingefroren-20261004-064950
- code/:
  - schachbrett.py, kausal_dirac.py, kontinuum_dirac.py, auswertung.py
  - kausal_welle.py (aus KAUSAL-WELLE-1)
  - je mit *.eingefroren-20261004-064950; pruefsummen-einfrieren.txt
- lauf-69/:
  - paket-r{200,800}-s{1..16}.json/.npz, punkt-r{200,800}-s{1..16}.json, probe-r5-s1.json
  - kont/ (kontinuum.json/.npz), sb/ (schachbrett.json)
  - Logs
  - auswertung.json (mit Vermerken), auswertung.maschine.json, aw/ (Originalausgabe)
- **Bilder** (lauf-69/):
  - schachbrett_fehler.png: Fehler gegen Schritt, dazu je tau
  - saatmittel_kontinuum.png: Propagator je Komponente, Profile der Pakete
  - streuung_rho.png: relative Streuung gegen rho
  - norm_t.png: Norm gegen t
  - komponentenwechsel.png: R-Anteil gegen t
- rauch-69/: Rauchlaeufe (Schachbrett, Kontinuum, Codeprobe, Zeit) und Logs der Pfadprobe.
- Auf der .69: /home/fmh/fmhc-physics-remote/runde38-schachbrett/ (code/, rauch/, lauf/).

## 10. Einfach gesagt

Ein Elektron in einer vereinfachten Welt mit nur einer Raumrichtung kann man sich als Teilchen vorstellen, das immer mit
Lichtgeschwindigkeit nach links oder rechts rennt und ab und zu umkehrt; Feynman hat gezeigt, dass die Summe ueber alle
diese Zickzack-Wege genau die Gleichung des Elektrons ergibt. Auf einem zufaelligen Netz aus Raumzeit-Punkten gibt es
keine Lichtstrahlen zum Geradeauslaufen, deshalb haben wir die Wege anders sortiert: Jeder Netzpunkt steht fuer zwei
Umkehrungen, und die geraden Stuecke dazwischen braucht man nicht mehr einzeln. So laeuft das Teilchen im Mittel ueber
viele Netze genau wie im glatten Raum, samt seinem typischen Hin- und Herzittern zwischen Links- und Rechtslaufen; das
Rauschen halbiert sich bei viermal dichterem Netz, und nichts schaukelt sich auf. Die Kontrolle auf dem regelmaessigen
Schachbrett war bei langen Laufzeiten ungenauer als vorhergesagt, weil Feynmans einfache Regel die Wahrscheinlichkeit
langsam aufblaeht. Das ist eine Computerrechnung in einer Spielzeugwelt, keine Messung, und ob es in unserer Welt mit drei
Raumrichtungen und echtem Spin auch geht, ist offen.
