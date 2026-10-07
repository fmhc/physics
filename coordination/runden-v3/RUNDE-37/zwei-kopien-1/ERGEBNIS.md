# ZWEI-KOPIEN-1: Ergebnis (Code-Agent fuer die Leitung, Runde 43, explorativ)

- **Ablauf (Zeiten per date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 19:48:07 CEST. Letzte eigene Messung vor dem Abbruch (Sitzungslimit): 19:48:45 CEST (.69 17:48:45
    UTC); bis dahin nur gelesen. Wiederaufnahme 21:45:58 CEST (Leitung: 21:45:28).
  - Plantext ab 21:50:52 CEST, Zusatz der Leitung eingetragen ab 21:52:14 CEST, beides vor jeder Rechnung.
  - Eingefroren 2026-10-04 21:58:01 CEST: PLAN.md, code/zk.py, code/zk_auswertung.py, code/zk_bild.py, code/tp.py
    (unveraendert aus TENSOR-EIS-PYRO-1); Kopien *.eingefroren-20261004-215801, Liste in EINGEFROREN-SHA256.txt.
  - Rauchlauf nach dem Einfrieren 19:58:29 bis 19:59:35 UTC (rc = 0, Werte nicht gelesen). Hauptlaeufe 19:59:45 bis
    20:00:50 UTC (cpu8: K2, dann K2e; cpu9: K4), Auswertung 20:00:50 bis 20:00:51 UTC, Bild bis 20:01:02 UTC; alle rc = 0.
  - Nachtrag (nach dem Einfrieren, neue Datei, beschreibend) 20:04:23 bis 20:04:24 UTC. Text ab 22:04:41 CEST.
  - Alle Eingaben der Auswertung nennen zk.py und tp.py mit den eingefrorenen Pruefsummen; die 13 Dateien in
    lauf-69/PRUEFSUMMEN.txt und die 2 in nachtrag-69/PRUEFSUMMEN.txt stimmen lokal (sha256sum -c).
- Alles synthetische Gitterrechnung auf der .69 (CPU, 1 Thread), keine Messdaten.
- **Kennzeichen:** [M] vorab ableitbar (Schreibtisch, PLAN 1), [E] hier gerechnet, [P] im Projekt schon gerechnet,
  [L] Literatur aus dem Gedaechtnis, [F] Festlegung im Plan, [H] Hypothese oder Lesart.
- **Begriffe:** P = Zwangsflaeche wie TENSOR-EIS-PYRO-1 (alle 6 Gauss-Regeln, beide Skalarregeln); R = nur die von K exakt
  erhaltene Resteichung bleibt Regel. K2 = Tetraedermittel (Plan), K2e = Mittel der 3 Kanten an der Ecke (Variante), K4 =
  Produkt der Fehlwinkel-Summen an der Ecke. n0 = Zahl masseloser Helizitaet-2-Zweige bei kleinem k.

## 1. Ergebnis zuerst

1. **Keine Eckkopplung bindet die zwei Kopien zu einer Welt mit genau einem masselosen Gravitonpaar [E].** ZK1 (K2 in
   Band B-b) trifft nicht ein, nach Plan und nach Kartenwortlaut: K2 landet bei allen drei kappa in "kein Band". Laengs der
   12 <110>-Richtungen bekommt genau ein TT-Zweig eine Luecke (omega^2 = 0,0178 kappa), laengs <100> und <111> bleiben alle
   vier masselos.
2. **Diese K2-Luecke ist ein Eichschnitt-Effekt [E, Nachtrag].** Die angehobene Mode laesst sich durch eine Eichung
   vollstaendig aus K2 herausdrehen (Restgehalt <= 9e-33 gegen 0,030 im Vertreter der Lesart P). Nimmt man die von K2
   gebrochenen Eichrichtungen ernst (Lesart R), bleiben alle vier TT-Zweige masselos, aber die zwei neuen Laengsmoden
   haben negative Norm und wachsen an 4 035 von 4 095 Gitter-k: ein Geist (Band B-d bei jedem kappa ab 0,001).
3. **K4 (Kruemmungsordnung) ist linear wirkungslos [E]:** Band B-a bei kappa = 0,01, 0,1 und 1, in P und R gleich; alle
   vier Zweige bleiben masselos mit omega^2/k^2 = 0,25000 (Spanne <= 1,1e-7). ZK2 trifft ein, nach Plan und nach
   Kartenwortlaut. In der kappa-Leiter (L = 8) wird K4 erst ab kappa = 10 instabil (negative Energie an 404 von 511 k);
   bei kappa = 3 noch stabil.
4. **Kontrolle ZK0 trifft ein [E]:** kappa = 0 gibt TENSOR-EIS-PYRO-1 wieder (Tempi auf 4,8e-11, positive Moden an allen
   4 095 Gitter-k gleich).
5. **Schreibtisch [M] und Rechnung:** Schritt 0 verneint (K2 ist unter xi_Ab = Mittel(xi_Auf) nicht invariant; meine
   Formel fuer das Eichbild von K2 stimmt im Code auf 8e-16). Meine Vorab-Erwartung "K2 sieht nur die Spur, also B-a in
   P" war falsch: Sie uebersah, dass der P-Vertreter Eichanteile mit Spur traegt.

## 2. Urteile

Mechanisch nach PLAN.md (eingefroren 21:58:01 CEST) durch code/zk_auswertung.py; Urteile und Kennzahlen in
lauf-69/auswertung.json. Bewertet wird Lesart P (Plan Abschnitt 4).

| Nr | Vorhersage (Kurzform) | Wahrsch. | nach Plan | nach Kartenwortlaut | Band je kappa = 0,01 / 0,1 / 1 (P; Plan = Wortlaut) | Kennzahlen |
|---|---|---|---|---|---|---|
| ZK0 | Kontrolle: kappa = 0 reproduziert B1 (n0 = 4, Tempi auf 1e-8) | 90 % | **eingetroffen** | **eingetroffen** | kappa = 0: B-a | n0 = 4 an allen 26 Richtungen; max abs Abweichung omega^2/k^2 = 4,8e-11, Tempo v = 4,8e-11 (23 Richtungen, beide \|k\|); positive Moden je Gitter-k gleich an 4 095 von 4 095 (4 an 4 092, 2 an den 3 X-Punkten); s = 6,0e-8; kappa = 0 in allen drei Laeufen bitgleich |
| ZK1 | K2 landet in B-b (eine masselose Kombination wie bei Bigravitation) | 35 % | **nicht eingetroffen** | **nicht eingetroffen** | kein Band / kein Band / kein Band | n0 = 3 an den 12 <110>-Richtungen, 4 an <100> und <111>; Delta = 0,0133 / 0,0422 / 0,1333, p = 0,4998 (omega^2 linear in kappa); s = 0,0011 / 0,011 / 0,110; "Kombination" nicht erfuellt (Kopienanteil der masselosen Moden 0,0004 bis 0,9996); kein B-d in P |
| ZK2 | K4 landet in B-a (Kopplung linear wirkungslos) | 50 % | **eingetroffen** | **eingetroffen** | B-a / B-a / B-a | n0 = 4 an allen 26 Richtungen; omega^2/k^2 = 0,25000 in allen Richtungen, s = 6,0e-8 / 6,4e-8 / 1,1e-7; Gitter L = 16 ohne negatives oder komplexes omega^2, ohne negative Norm oder Energie |

- **Bedeutung, wie auf der Karte vorab festgelegt:** Keine der drei Zeilen ist durch die Urteile ausgeloest.
  - "ZK1 trifft ein" nein.
  - "ZK1 verfehlt mit B-c" nein: K2 verfehlt mit "kein Band" (eine Luecke nur laengs <110>), nicht mit B-c.
  - "B-d" nach Plan nein (Lesart P). Beschreibend in Lesart R ja: K2 mit ernst genommener Eichbrechung macht das Netz
    instabil (Abschnitt 3.2).
- **Baender aller Fassungen** (Plan / Kartenwortlaut gleich, ausser wo vermerkt; Gitter L = 16):

| Fassung | Lesart | kappa = 0,01 | kappa = 0,1 | kappa = 1 | n0 je Richtung | Delta (0,01 / 0,1 / 1) | p |
|---|---|---|---|---|---|---|---|
| K2 | P | kein Band | kein Band | kein Band | 3 (<110>), 4 sonst | 0,0133 / 0,0422 / 0,1333 | 0,4998 |
| K2 | R | B-d | B-d | B-d | 4 ueberall | keine | - |
| K4 | P | B-a | B-a | B-a | 4 ueberall | keine | - |
| K4 | R (= P, K M = 0) | B-a | B-a | B-a | 4 ueberall | keine | - |
| K2e | P | kein Band | kein Band | kein Band | 3 (<100>), 2 sonst | 0,0298 / 0,0943 / 0,2981 | 0,49997 |
| K2e | R | B-d | B-d | B-d | 2 bis 4 | 0,0385 / 0,1217 / 0,3849 | 0,49998 |

- **Agenten-Vorhersagen** (PLAN 5; in keinem Urteil):

| Nr | Ergebnis |
|---|---|
| V1 | eingetroffen: ZK0, Tempo-Abweichung 4,8e-11 (<= 1e-10) |
| V2 | **verfehlt**: K2 (P) "kein Band", nicht B-a (n0 = 3 laengs <110>) |
| V3 | eingetroffen: K4 B-a bei 0,01 und 0,1, auch bei 1; kappa_c in der Leiter zwischen 3 und 10 (im vorhergesagten Bereich 0,1 bis 30) |
| V4 | eingetroffen: K2e n0 = 3 genau an den 6 <100>-Richtungen, sonst 2; p = 0,49997 |
| V5 | **im Wesentlichen verfehlt**: 4 masselose TT-Moden ja; aber keine weitere masselose Mode und keine Luecke, stattdessen negative Norm und Wachstum (Norm-Frage: negativ) |
| V6 | eingetroffen: s(K2, P, kappa = 1) = 0,110 > 1 % |

## 3. Was die Rechnung zeigt

### 3.1 K2 in Lesart P: Luecke nur laengs <110>, und sie haengt am Eichschnitt [E]

- Laengs der 12 <110>-Richtungen hat ein Zweig omega^2 = 0,017778 kappa (bei \|k\| = 1e-3 und 2e-3 gleich, TT-Anteil 1,000);
  das ist (4/225) kappa. Laengs <100> verschiebt sich ein Zweig auf omega^2/k^2 = 0,25 (1 + kappa/9); laengs <111> bleibt
  alles bei 0,25.
- **Nachtrag** (code/nachtrag_eichschnitt.py, nachtrag-69/eichschnitt.json; importiert das eingefrorene zk.py unveraendert;
  omega^2 gleich dem Hauptlauf auf 0,0): Fuer alle 48 angehobenen Moden (12 Richtungen x 2 \|k\| x kappa = 0,1 und 1) ist
  der K2-Gehalt des P-Vertreters |F a|^2 = 0,0296 (= 4/135), das Minimum ueber die Eichbahn aber <= 8,8e-33. Es gilt
  omega^2/(kappa |F a|^2) = 0,6000 bis 0,6003. Fuer die masselosen Moden ist |F a|^2 <= 1,1e-7.
- **Lesart [M, H]:** Der P-Vertreter steht im Kantenmass senkrecht auf dem Eichbild. Dieses Mass ist kubisch anisotrop
  (Nebendiagonale doppelt so schwer wie die Diagonale), also enthaelt der Vertreter mancher TT-Moden Laengs-Eichanteile mit
  Spur. K2 ist nicht eichinvariant und bestraft genau diesen Anteil. Fuer jede angehobene Mode gibt es einen Eichvertreter
  ohne K2-Gehalt [E]; eine Eichfixierung ohne Luecke fuer alle Moden zugleich habe ich nicht gerechnet. Die P-Luecke ist
  damit keine eichinvariante Masse.

### 3.2 K2 in Lesart R: alle TT-Zweige masselos, aber ein Geist [E]

- K M hat an allen 50 Pruef-k Rang 2 (wie in PLAN 1.2 vorhergesagt): je Kopie ist die Laengs-Eichung gebrochen, die
  Quer-Eichungen bleiben exakt, eine diagonale Eichung entsteht nicht.
- Mit den 2 gebrochenen Richtungen als Freiheitsgraden (Dimension 6 statt 4):
  - n0 = 4 an allen 26 Richtungen; laengs <110> laeuft ein Zweig mit omega^2/k^2 = 1/3 statt 1/4, unabhaengig von kappa.
  - Die 2 neuen Moden haben negative Bewegungsenergie (A_phys < 0) an 4 035 von 4 095 Gitter-k und an 36 von 52
    kleinen Punkten; dort ist omega^2 < 0 (kleinstes omega^2 relativ -0,03 / -0,30 / -1,0 bei kappa = 0,01 / 0,1 / 1).
    B + kappa K bleibt ueberall >= 0, die Instabilitaet ist also ein Geist (negative Norm), keine negative Energie.
  - Schon bei kappa = 0,001 (Leiter) ist das so.
- Lesart [L, H]: Das entspricht dem Kontinuumsbefund, dass ein Massenterm, der nicht die Fierz-Pauli-Form hat (hier nur die
  Spur der Differenz), einen Geist traegt; die Ursache im Gitter ist das Spurglied -1/2 der Bewegungsenergie (A0 je
  Tetraeder ist auf gleichmaessiger Dehnung negativ).

### 3.3 K4: Mischung ohne Masse [E]

- Fehlwinkel sind eichinvariant (K M = 4e-16 relativ, Rang 0); P und R sind gleich.
- Die vier masselosen Zweige bleiben bei 0,25 (alle Richtungen). Ab kappa = 0,1 sind die Eigenmoden Mischungen beider
  Kopien (Kopienanteil 0,49 bis 0,52; bei kappa = 1 0,499 bis 0,500). Das ist entartete Stoerungsrechnung: Weil die
  Kopplung erst in Ordnung k^4 wirkt, bleiben Summe und Differenz masselos [M]. Bei endlichem k spalten die Zweige
  (Bild, Gamma -> K und Gamma -> L).
- Leiter (L = 8): B-a fuer kappa <= 3; ab kappa = 10 negative Energie (B'_phys < 0) an 404 von 511 k (30: 482, 100: 490),
  ohne negative Norm.

### 3.4 K2e (Variante, beschreibend) [E]

- Wie am Schreibtisch erwartet: Masse fuer die Nebendiagonal-Anteile der Differenz. n0 = 3 genau an den 6 <100>-Richtungen
  (dort bleibt h_yy - h_zz der Differenz masselos), sonst 2; bei kappa = 1 Luecken omega^2 = 4/9 ([100]), 4/45 und 4/9
  ([110]), 1/6 doppelt ([111]); p = 0,49997.
- Ob diese Luecken eichinvariant sind, ist nicht geprueft (der Nachtrag rechnet nur K2). In Lesart R ist auch K2e ein
  Geist (A_phys < 0 an 4 035 von 4 095 k).

### 3.5 Konkurrenzzustand (Leitung) [E]

- Lesart P, alle Fassungen, Haupt-kappa: kein negatives oder komplexes omega^2 am Gitter L = 16 (kleinstes relativ
  -7e-16, Rundung), keine negative Norm oder Energie, keine weitere masselose Mode ohne Helizitaet 2, keine Mode
  "unklar". Neben den gesuchten Zweigen gibt es dort keinen tieferen Zustand.
- Lesart R (K2, K2e): Ja, die wachsenden Geist-Moden sind ein Zustand unter dem Vakuum (Abschnitt 3.2).
- K4 ab kappa = 10: negative Energie, also ein tieferer Zustand.

### 3.6 Zusatz Leitung 21:5x, beschreibend: Isotropie der verbleibenden masselosen TT-Zweige [E]

omega^2/k^2 je Zweig (masselos und Helizitaet 2), bei \|k\| = 1e-3 und 2e-3 gleich auf 1e-6 (Ausnahme R, [110]: 0,333315
gegen 0,333258 bei kappa = 0,01); Spanne = max/min - 1.

| Netz | kappa | Lesart | [100] | [110] | [111] | Spanne drei Richtungen (1e-3 / 2e-3) | Spanne 26 Richtungen (1e-3 / 2e-3) |
|---|---|---|---|---|---|---|---|
| ungekoppelt | 0 | P | 4 x 0,25000 | 4 x 0,25000 | 4 x 0,25000 | 5,8e-8 / 2,5e-7 | 6,0e-8 / 2,5e-7 |
| K4 | 0,01 / 0,1 / 1 | P und R | 4 x 0,25000 | 4 x 0,25000 | 4 x 0,25000 | <= 1,1e-7 / 4,5e-7 | <= 1,1e-7 / 4,5e-7 |
| K2 | 0,01 / 0,1 / 1 | P | 3 x 0,25; 0,250278 / 0,252778 / 0,277778 | 0,25; 0,25; 0,250003 / 0,250028 / 0,250278 (dritter Zweig) | 4 x 0,25000 | 0,00111 / 0,0111 / 0,1111 (= kappa/9) | ebenso |
| K2 | 0,01 / 0,1 / 1 | R | 4 x 0,25000 | 0,25; 0,25; 0,250008 / 0,250077 / 0,250762; 0,3333 | 4 x 0,25000 | 0,333 | 0,333 |
| K2e | 0,01 / 0,1 / 1 | P | 0,25; 0,25; 0,250069 / 0,250694 / 0,256944 | 0,25; 0,250003 / 0,250028 / 0,250278 | 2 x 0,25000 | 0,00028 / 0,0028 / 0,0278 (= kappa/36) | ebenso |
| K2e | 0,01 / 0,1 / 1 | R | 3 x 0,25000 | 2 x 0,25000 | 0,0833 (2 x); 0,25 (2 x) | 2,0 | 2,0 |

- Lesart: K4 erhaelt die Isotropie (wie ohne Kopplung). K2 und K2e machen in P einen Zweig linear in kappa
  richtungsabhaengig (bei kappa = 1 um 11 % bzw. 2,8 %), in R um 33 % bzw. 200 %. Fuer die Frage der Leitung heisst das:
  Die isotrope Kopplung ist die wirkungslose (K4); die wirksamen (K2, K2e) zerstoeren die Isotropie, und zwar in der
  eichabhaengigen Lesart P schwaecher als in R.

## 4. Kontrollen

- Operatoren (50 Zufalls-k): B hermitesch 2e-16, K hermitesch 0, B M 5e-16, c M 7e-16 (relativ); K2 und K2e positiv
  semidefinit (kleinster Eigenwert -3e-16 relativ); K4 indefinit (wie gewollt).
- Schreibtischformeln im Code: K2 und K2e bei k = 0 fuer gleichfoermige Dehnung (Spur/3 bzw. (Spur + s_a^T h s_a)/6) auf
  2e-16 bzw. 9e-16; Eichbild F M von K2 gegen (8/3)(u, e^{2ik.r_a} conj(u)) auf 7,8e-16; Rang K M = 2 (K2), 4 (K2e), 0 (K4)
  an allen 50 k.
- ZK0 gegen TENSOR-EIS-PYRO-1: Abschnitt 2. Physikalische Dimension in P an allen 4 095 k gleich 4; in R 6 (K2) bzw. 8
  (K2e), gebrochene Richtungen 2 bzw. 4 an allen k.
- Klassen: keine Mode "unklar" in P. In R: K2 je 2 an den 8 <111>-Richtungen (die gebrochenen Moden mit omega^2 nahe 0),
  K2e 1 bis 2 je Richtung (z. B. [100] 1, [110] 2, [111] 2 bei kappa = 0,1).
- Latten:
  - L1 (kann scheitern): ZK1 und ZK2 waren nicht vollstaendig ableitbar; ZK1 ist an der Richtungsabhaengigkeit gescheitert,
    ZK2 haette an Instabilitaet scheitern koennen (tut es ab kappa = 10).
  - L2 (Gegenprobe): bitgleiches kappa = 0 in drei Laeufen, Referenz TENSOR-EIS-PYRO-1, Nachtrag Eichbahn.
  - L3 (Numerik): Identitaeten 1e-16 bis 1e-15; Tempi 5e-11.
  - L4 (schon bekannt): Bigravitation, Fierz-Pauli-Geist, BDGH [L]; die Zwei-Kopien-Struktur [P].
  - L5 (Messbezug): keiner.

## 5. Bedeutung [M, E, H]

- Eine oertliche Eckkopplung ohne neue Bauteile macht aus Finns zwei Welten keine Schwerkraft plus massive Zusatzmode.
  - Die Kruemmungs-Kopplung K4 ist im Langwelligen wirkungslos (Erwartung von BDGH fuer masselose Zweige: Kopplung im
    Kontinuum trivial). Bei grossem kappa macht sie das Netz instabil.
  - Die Dehnungs-Kopplung K2 bricht nur die Laengs-Eichung je Kopie, nicht zu einer diagonalen Eichung. In der
    Zwangsflaechen-Lesart erzeugt sie eine richtungsabhaengige Scheinmasse, die vom Eichschnitt abhaengt; in der
    ehrlichen Lesart einen Geist.
- Der einzige gerechnete Weg zu einer Welt bleibt die Fuellung der Loecher (EINE-WELT-LOCH-1): Dort entscheidet die
  Eichstruktur, nicht eine Kopplung.
- [H] Eine Bigravitations-artige Bindung braeuchte einen Massenterm in Fierz-Pauli-Form fuer die ganze Differenz und eine
  diagonale Eichung auf dem Gitter; beides liefert keine der beiden Eckkopplungen.
- **Dimensionsvergleich (AGENTS.md):** gerechnet nur das 3D-Netz. In 2+1 Dimensionen gibt es keine Gravitonen (0
  Polarisationen), die Frage entfaellt. Die Spur-Aussage (mittlere Kantendehnung eines regulaeren Simplex = Spur/d) gilt in
  jeder Dimension [M]; die Richtungsabhaengigkeit (<110> bzw. <100>) haengt am Pyrochlor-Netz und am Kantenmass, ist also
  nicht ohne Rechnung auf andere Dimensionen uebertragbar.
- Grenzen: linear, klassisch; Bewegungsenergie und Reduktion wie TENSOR-EIS-PYRO-1 (R1). Keine Aussage ueber Kopplung an
  die Energie (Marolf).

## 6. Selbstanzeigen

1. **Unterbrechung:** Letzte eigene Messung vor dem Abbruch 19:48:45 CEST, Wiederaufnahme 21:45:58 CEST. Vor dem Abbruch
   nur gelesen; keine Datei geschrieben, nichts gerechnet. Die Gedanken aus dieser Zeit stehen erst im Plantext ab 21:50:52.
2. **Hintergrund-Ausgaben im Sitzungs-Scratchpad:** Die zwei Rauchlauf-Befehle liefen als Hintergrundaufgaben. Das
   Werkzeug schrieb ihre Kurzausgabe (rc und letzte Logzeilen) nach /tmp/claude-1000/.../tasks/. Das kann der Scratchpad
   der Leitung sein; danach nur noch Vordergrund-Befehle. Sonst keine Datei ausserhalb des Kartenordners und des
   .69-Ordners zwei-kopien-1.
3. **Rauchlauf anders als in PLAN 6:** K2 lief mit L = 16 und Referenz (statt L = 4), um den ZK0-Pfad zu pruefen; dazu
   Auswertung und Bild auf den Rauchdaten. Gelesen habe ich nur rc, Zeiten, Dateiliste und Laufzeitzeilen, keine
   Ergebniswerte. Am Code wurde nach dem Einfrieren nichts geaendert.
4. **Schreibtisch-Fehler:** PLAN 1.3 (und V2) sagte fuer K2 in P das Band B-a voraus. Das ist falsch: Ich habe den
   P-Vertreter als reine TT-Dehnung behandelt, er traegt aber Eichanteile mit Spur (Nachtrag). Auch die Erwartung fuer
   Lesart R (PLAN 1.4: weitere masselose Mode und Luecke) traf nicht zu (Geist).
5. **Nachtrag nach dem Einfrieren:** eigene Datei (code/nachtrag_eichschnitt.py), eingefrorenes zk.py unveraendert
   importiert, kein Urteil. Er beantwortet nur, ob die P-Luecke von K2 am Eichschnitt haengt; fuer K2e nicht gerechnet.
6. **Bild:** Die Legende ueberdeckt den Bildtitel teilweise (Schoenheitsfehler im eingefrorenen zk_bild.py; nicht
   geaendert).
7. **Lesarten mit Gewicht:** Die Urteile stehen auf Lesart P und der Tetraedermittel-Lesart von K2 [F]. Die Ecken-Lesart
   (K2e) gaebe ebenfalls "kein Band" (n0 = 3 laengs <100>), Lesart R "B-d". ZK1 waere also in keiner der vier Kombinationen
   eingetroffen. Fuer K4 legt die Karte die Kanten an der Ecke nicht fest; die Lesart "Skalarkruemmung je Kopie" waere auf
   der Zwangsflaeche identisch null (B-a, ableitbar).
8. **kappa-Werte [F]:** 0,01 / 0,1 / 1 in den Einheiten von tp.py (g = 1). Das Urteil zu ZK2 haengt daran: Ab kappa = 10
   waere K4 B-d (Leiter, L = 8).
9. **Plan und Kartenwortlaut** unterscheiden sich nur in "Kombination" (ZK1), der B-d-Definition und Tempo statt
   omega^2/k^2 (ZK0); an keinem Urteil aendert das etwas.
10. **Kein frischer Leser** (Zeitbox). Lokal kein python, awk oder perl; jq nur lesend. Auf der .69 python nur ueber
    kleintest.sh (cpu8, cpu9), Skripte per scp auf .neu und mv.

## 7. Einfach gesagt

Finns Netz zerfaellt in zwei Welten, jede mit eigener Schwerkraft, die sich gegenseitig nicht spueren. Wir haben getestet,
ob eine einfache Verbindung an den Ecken die zwei Welten so zusammenklebt, dass nur eine Schwerkraftwelle masselos bleibt
und die andere schwer wird. Die sanfte Verbindung (ueber die Kruemmung) aendert bei langen Wellen gar nichts: Alle vier
Wellen bleiben masselos und laufen in alle Richtungen gleich schnell. Die harte Verbindung (ueber die Kantenlaengen) macht
eine Welle nur in manchen Richtungen schwer, und das ist ein Rechentrick der Beschreibung; rechnet man ehrlich, entsteht
eine Geistermode, die das Netz instabil macht. Eine Welt bekommt man bisher nur, wenn man die Loecher des Netzes fuellt.

## 8. Dateien

- PLAN.md, PLAN.md.eingefroren-20261004-215801, EINGEFROREN-SHA256.txt
- code/: zk.py (Laeufe), zk_auswertung.py (Urteile), zk_bild.py (Bild), tp.py (unveraendert), je mit eingefrorener Kopie;
  nachtrag_eichschnitt.py (Nachtrag).
- lauf-69/: zk-K2.json, zk-K4.json, zk-K2e.json, auswertung.json, spektrum.png (Spektrum-Bild), Logs, PRUEFSUMMEN.txt.
- rauch-69/: Logs des Rauchlaufs. nachtrag-69/: eichschnitt.json, nt.log, PRUEFSUMMEN.txt.
- Auf der .69: /home/fmh/fmhc-physics-remote/zwei-kopien-1/ (code/, ref/, rauch/, lauf/, nachtrag/).
