# WOLFRAM-RUHE-1: Ergebnis (Runde 42, Code-Agent fuer Leitung claude-primary)

- Geschrieben ab 2026-10-04 17:48:55 CEST (date). Karte 17:22:24, Plan ab 17:35:31, Rauchlauf 17:43:29-17:43:36,
  eingefroren 17:46:04, Hauptlaeufe 17:46:29-17:46:46, Auswertung 17:47:15-17:47:18 (Zeiten aus date bzw. Starter-Log,
  .69-Zeiten UTC + 2 h).
- Rechnungen nur auf der .69 ueber kleintest.sh (cpu6, cpu7), je Lauf <= 16 s, <= 116 MB. Dateien: PLAN.md (+ eingefrorene
  Kopie), EINGEFROREN-SHA256.txt, code/, rauch-69/, lauf-69/ (auswertung.json, r_eta.png, PRUEFSUMMEN.txt).
- Kennzeichen: [M] Mathematik, [E] Messung im Modell, [L] Literatur, [S] Quelle selbst gelesen, [H] Hypothese.

## 1. Ergebnis zuerst

1. **Die "lorentzartige" 2D-Regel R2 ist keine 1+1-Raumzeit.** Ihre Kausalordnung ist eine **Kette** (totale Ordnung):
   genau 1 Ereignis je Generation in 50 000 von 50 000 Generationen, jedes Ereignis haengt vom vorigen ab (Kettenprobe
   1,000) [E]. Das war vorab ableitbar: Die Regel verbraucht und erzeugt je Ereignis genau eine "Marke" {x,y,y}; ab
   Ereignis 3 gibt es nur noch eine, also nur einen aktiven Ort (PLAN Abschn. 2) [M]. Der Lauf bestaetigt die Rechnung.
2. **WR1 verfehlt** (Plan und Kartenwortlaut). Kartenwortlaut knapp: geodaetischer Kegel-Exponent 2,25 (Fenster t 20-81;
   Rauchlauf 2,24) statt 1,8-2,2; die lokale Steigung wandert von 1,9 auf 2,3, eine saubere Potenz ist es nicht [E].
   Front-Test und Generationskegel scheitern deutlich (s_b = 0; D_gen = 0,98, also Kette) [E].
3. **WR2 nicht geprueft** (Abbruch nach Karte). Die Schraegstellung eta ist fuer R2 gar nicht definiert (c^2 = -1e-17,
   der Generationskegel waechst wie T + 1). Alle 6000 gezogenen R2-Intervalle sind Ketten: L = N, r = sqrt(N)/2 genau
   (4,2 bei N ~ 70 bis 18,9 bei N ~ 1400) [E, vorab M]. Das Ruhesystem ist hier eine absolute Zeitordnung.
4. **R2 ist nicht kausalinvariant** (vom Standardanfang): 5 von 8 Zufallsreihenfolgen liefern schon bei Tiefe 25 einen
   anderen (nicht-isomorphen) Kausalgraphen, ebenso bei 50 und 100 [E]. Das Lorentz-Argument der TI ("if the underlying
   rule has causal invariance", S. 366) [S] und Gorards Vergroeberung (A34 S. 31-32, fuer kausalinvariante Systeme) [S]
   greifen fuer R2 also nicht. Eine Vergroeberung zu Blaettern macht aus einer Kette ohnehin nur wieder eine Kette [M].
5. **WR0 formal verfehlt (Plan und Kartenwortlaut), in der Sache funktionieren die Kontrollen:** Poisson ohne
   eta-Trend (Steigungen -0,002 bis +0,003, SE <= 0,0034), Gitter r = cosh(eta) exakt mit Steigung 1. Verfehlt wegen
   (i) des vorab benannten Endlichkeitseffekts (Poisson-Median r 0,914 bis 0,953, nur der groesste N-Bin innerhalb 5 %)
   und (ii) eines Fehlers in meinem Plan-Kriterium G(ii) (Selbstanzeige S2).

## 2. Urteile (Regeln aus PLAN.md Abschn. 4 und 6, eingefroren 17:46:04)

| WR | Karte (Wahrsch., unveraendert) | nach Plan | nach Kartenwortlaut | Kennzahlen (Hauptlauf) |
|---|---|---|---|---|
| WR0 | 85 % | **verfehlt** (nur G(ii)) | **verfehlt** (Poisson-Niveau in 4 von 5 N-Bins) | Poisson: Median r 0,914 / 0,926 / 0,934 / 0,944 / 0,953 (N-Bins 50-100 ... 1000-2000, je >= 1054 Intervalle); Steigung r gegen cosh eta -0,0011 / +0,0027 / +0,0011 / -0,0016 / -0,0002. Gitter: max abs(r - cosh eta_Programm) = 0, Steigung 1,000 in allen Bins; r/cosh eta_wahr = 0,969 (16-84 %: 0,968-0,970) im Bin 1000-2000 (Regel: 1 +- 0,02). Programmprobe LIS gegen Graph-Routine: 0 von 40 abweichend |
| WR1 | 55 % | **verfehlt** ((a), (b), (c) alle verfehlt) | **verfehlt** (D_geo = 2,25 > 2,2) | E = 50 000, G = 50 000; D_geo = 2,248 (t 20-81, t_g = 81), lokal 1,91 ... 2,34; Ereignisse je Generation: 1 in allen Generationen, s_b = 0; D_gen = 0,981; Marken: 1 (49 998 Gen.), 2 (2 Gen.); Kettenprobe 1,000; Ein-/Ausgrad max 2/3 |
| WR2 | 60 % | **nicht geprueft** (Abbruch, WR1 nach Plan verfehlt) | **entfaellt** (WR1 nach Kartenwortlaut verfehlt) | eta nicht definiert (Quadratkoeffizient des Generationskegels -1,0e-17); 6000 von 6000 Intervallen mit L = N; Median r = Median sqrt(N)/2 in jedem N-Bin |
| KI (Auftrag, kein WR) | - | **verletzt** | - | D = 25, 50, 100: Saaten 1, 3, 6, 7, 8 nicht isomorph zum Standard, 2, 4, 5 isomorph; gleiche Knoten- und Kantenzahl (D = 100: 100 / 197) |

- Rauchlauf (E = 2e4, 1500 Intervalle je Kontrolle): gleiche Urteile; D_geo 2,237, D_gen 0,981, KI verletzt bei D = 25, 50.
- Diagnosen ohne Urteil: Zufallsreihenfolgen (Saat 1, 2, je 2e4 Ereignisse) ebenfalls 1 Ereignis je Generation und
  Kette; zweiter Anfang {{1,2,2},{1,3,4}} haelt nach einem Ereignis an (kein Partner fuer die neue Marke) [E].

**Bild** lauf-69/r_eta.png: links r(eta) der Kontrollen in den zwei groessten N-Bins mit cosh(eta) (Gitter liegt auf
cosh, Poisson flach knapp unter 1); R2 hat dort keinen Platz (eta nicht definiert). Rechts r gegen N: R2 liegt exakt auf
der Kettenlinie sqrt(N)/2, Poisson bei 0,91-0,95.

## 3. Was das bedeutet

- **Fuer die Karte:** Die Bedeutungsfaelle "WR2 trifft ein / verfehlt" kommen nicht zur Anwendung. Es gilt der in K1
  vorgesehene Fall "Abbruch: Dann ist das Vorzeigebeispiel keine 1+1-Raumzeit, auch das ist ein Ergebnis"
  (wolfram-scan-l/DOSSIER.md Z. 150-152).
- **Fuer Finns Weiche:** R2 steht auf Seite A, in der staerksten Form: Es gibt eine absolute Reihenfolge aller Ereignisse
  (ein einziger "Taktgeber"), nicht nur ein Ruhesystem [E, M]. Dass das im Grossen verschwindet, ist fuer die Ordnung
  ausgeschlossen [M]. Gorards "two-dimensional Lorentzian manifold-like" fuer diese Regel (A34 Fig. 45/46) stuetzt sich
  auf geodaetische Kegel; die Ordnung ist eindimensional [E].
- **Lesart der TI-"Dimension 2"** [H]: Die Kegelzahl ~ t^2 kommt von Fernkanten (Relationen, die viel spaeter wieder
  benutzt werden); vermutlich spiegelt sie die etwa zweidimensionale Flaeche, ueber die der eine aktive Ort wandert, nicht
  Raum plus Zeit. Nicht gesondert getestet.
- **Berichtigung der Karte:** Die Ableitbarkeitsprobe der Karte ("Fuer den Wolfram-Graphen ist r(eta) nicht ableitbar")
  trifft fuer R2 vom Standardanfang nicht zu: r = sqrt(N)/2 folgt aus der Markenzaehlung [M]. Meine Rechnung stand vor
  dem Lauf im Plan (Abschn. 2); die R2-Daten sind daher eine Rechenprobe, keine Messung.
- **Offen:** Ob irgendeine Wolfram-Regel eine Lorentz-artige Ordnung im Grossen hat, bleibt offen. Sie muesste
  kausalinvariant sein und viele Orte zugleich aktualisieren; R2 erfuellt beides nicht [E]. Ein Suchlauf wie K2
  (DOSSIER Abschn. 9) muesste diese zwei Bedingungen zuerst pruefen [H]. Ob die Reihenfolgeabhaengigkeit von R2 nur aus
  der Anfangsphase stammt, ist nicht untersucht.

## 4. Selbstanzeigen

- **S1 (ungewollter Lauf):** Um 17:46 habe ich versehentlich einen Befehl abgesetzt, der rauch.py ein zweites Mal ueber
  den Starter (cpu6, Kurzname wr42-kontr) mit Ausgabe nach /dev/null startete. Keine Datei geschrieben, kein Ergebnis
  gesehen; ob die Unit lief, ist im Nutzer-Journal der .69 nicht sichtbar. Hoechstens etwa 8 s Rechenzeit.
- **S2 (Fehler im Plan-Kriterium G(ii)):** Meine Vorab-Abschaetzung "r/cosh eta_wahr ~ 1 - 1/(a+b+2)" gilt nur fuer
  quadratische Gitterintervalle. Bei schmalen Intervallen (kleines b) weicht eta_wahr = (1/2) ln(a/b) staerker ab (z. B.
  a = 330, b = 5: r/cosh eta_wahr = 0,914) [M, nachtraeglich]. G(ii) wurde nach dem Rauchlauf **nicht** geaendert;
  WR0 nach Plan bleibt "verfehlt". Die Programmprobe G(i) und die Steigung G(iii) bestehen.
- **S3:** WR0 nach Kartenwortlaut war vorab als voraussichtlich verfehlt benannt (Poisson-Endlichkeitseffekt, PLAN
  Abschn. 6); gemessen 0,914 bei N 50-100 gegen meine Schaetzung ~0,90 [L-Formel aus dem Gedaechtnis].
- **S4:** N und L mit Endpunkten gezaehlt (Karte: "Ereignisse dazwischen"), damit die Gitterformel des Dossiers gilt;
  im Plan vorab benannt.
- **S5:** Mit der eta-Definition des Plans (Endpunkte, N, Eichung c) ist die Gitterkontrolle eine Programmprobe
  (r = cosh eta per Konstruktion), keine unabhaengige eta-Pruefung; im Plan vorab benannt.
- **S6:** Poisson-Kontrolle ueber Koordinaten und laengste steigende Teilfolge statt ueber die allgemeine Graph-Routine;
  Gleichheit an 2 x 40 kleinen Intervallen geprueft (0 Abweichungen). Das Gitter lief ueber dieselbe Graph-Routine wie R2.
- **S7:** Die Partnerwahl der Standard-Aktualisierung (aeltester Partner) ist meine Festlegung; die TI legt sie nicht
  fest (S. 243). Fuer die Kettenstruktur spielt sie keine Rolle (Zufallsreihenfolgen ebenfalls Kette), fuer die
  Fernkanten schon (KI verletzt).
- **S8:** Im Bild verdeckt die Legende links den roten Hinweis "R2: eta nicht definiert" teilweise; nach dem Einfrieren
  nicht nachgebessert.
- **S9 (Werkzeuge):** Lokal ausser den freigegebenen Werkzeugen auch ls, cat, wc, head, tail, diff, rm (eine eigene
  Hilfsdatei mit .69-Hashes im Kartenordner, danach geloescht) und einmal sleep 20; keine Interpreter. Auf der .69 nur
  Lesebefehle (ls, sha256sum, journalctl, free, nproc, uptime) ausserhalb des Starters.
- **S10:** Kein frischer Leser hat diese Datei gegengelesen. Die Markenrechnung [M] habe ich allein gefuehrt; der Lauf
  bestaetigt ihre Folgen (1 Ereignis je Generation, Kette), nicht jeden Schritt.

## 5. Einfach gesagt

Wolfram zeigt eine Regel, aus der angeblich eine zweidimensionale Raumzeit wie bei Einstein waechst. Wir haben sie
nachgebaut und gesehen: Es passiert immer nur an einer einzigen Stelle etwas, ein Schritt nach dem anderen, wie ein
Schreibkopf, der ueber eine Flaeche faehrt. Damit haben alle Ereignisse eine feste Reihenfolge, es gibt also eine
absolute Uhr und kein "gleichzeitig woanders", und das verschwindet auch im Grossen nicht. Ausserdem haengt das Ergebnis
davon ab, in welcher Reihenfolge man die Regel anwendet; Wolframs eigenes Relativitaets-Argument setzt voraus, dass genau
das nicht passiert.
Fuer Finns Frage heisst das: Dieses Vorzeigebeispiel ist ein Netz mit fester Uhr (Seite A), kein Beleg fuer
Lorentz-Invarianz.
