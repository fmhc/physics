# FRUST-3D: Ergebnis (Code-Agent fuer die Leitung, Runde 27, explorativ)

- Gerechnet auf der .69 (kleintest.sh, CPU-Spuren cpu, cpu2, cpu3, cpu4, cpu6):
  - Rauchlaeufe 03:28:21 bis 03:35:22 UTC (05:28 bis 05:35 CEST), Fehlpass anders als echt (Achse-Ruhelaenge 1,03)
  - 17 echte Laeufe 03:36:24 bis 03:45:38 UTC (05:36 bis 05:45 CEST), alle rc = 0. 16 davon endeten bis 03:37:55
    (je 2 bis 64 s); k1_E_12 lief bis an die interne Zeitgrenze (481 s, siehe Selbstanzeigen)
  - Auswertung (code/auswertung.py) 03:45:55 UTC
- Plan und Code eingefroren 05:35:56 CEST (PLAN.md.eingefroren-20261003-053556, code/*.eingefroren-20261003-053556),
  vor dem ersten echten Lauf (05:36:24 CEST). Auswerteregeln ab 05:28:38 CEST; Aenderungen nach dem Rauchlauf stehen
  offen in PLAN.md Abschnitt 6.
- Daten: lauf-69/ (Laeufe, auswertung.json mit den Urteilen), rauch-69/. Code: code/frust_3d.py (sha256 0b9cee16...),
  code/auswertung.py (7d766fad...), code/laeufe.sh.
- Geschrieben ab 05:40:58 CEST (date).
- Einheiten im Modell: B = 1, Stablaenge L = 1; Kraefte in B/L^2, Momente in B/L, Energie in B/L. Echte Groessen wie
  TETRA-STAB (Knicklicht 20 cm, 5 mm, voller LDPE-Stab angenommen, B ~ 7,7e-3 N m^2): B/L^2 = 0,19 N,
  B/L = 38,5 N mm (Biegespannung 3,1 MPa je B/L), Energie B/L = 38,5 mJ. Euler-Last mit Gelenken pi^2 B/L^2 = 1,9 N.

## Ergebnis zuerst

1. **Die 7,36-Grad-Luecke wird fast ganz als Biegung aufgenommen, die Achse wird kaum laenger.**
   - Statt 1,0515 ist die Achse 1,0010 (Gelenke) bzw. 1,0017 (Einspannung) lang, der Ring wird nur um 0,05 % weiter.
   - Den Rest schlucken die Speichen: Die gebogenen werden als Sehne um 1,0 bis 2,4 % kuerzer.
   - Biegeanteil der Energie: 96 % (Gelenke), 93 % (Einspannung).
2. **Vorzeichenmuster:** Achse unter Zug, Speichen unter Druck, **Ring unter Zug** (nicht Druck, wie F1 sagte).
   - Mit Gelenken (N = 20): Achse +24,4, Speichen -9,3 bzw. -10,0, Ring +14,1 (in B/L^2; echt 4,7 N, 1,8 bis 1,9 N,
     2,7 N).
   - Das ist die eine Eigenspannung des Gelenkwerks, (1; -0,40; +0,58), wie vor den Laeufen auf dem Papier gerechnet.
3. **Symmetriebruch mit Gelenken:** Nur die fuenf Speichen an **einer** Spitze knicken aus (Stich 0,098 L, echt
   2 cm). Die fuenf an der anderen bleiben gerade, knapp unter der Euler-Last (0,94).
   - Der Ring rutscht dabei um 0,024 L (5 mm) zur geknickten Seite.
   - Der symmetrische Zustand (alle zehn geknickt) ist instabil [H, Abschaetzung unten]. Beide Anstoesse ("aus", "ein")
     enden im selben Zustand.
4. **Mit Einspannung** sind alle zehn Speichen gebogen (Stich 0,063 und 0,074 L, also wieder leicht ungleich).
   - Kraefte etwa 1,8-mal so gross (Achse +43,8, also 8,4 N), Energie 2,13 gegen 1,24 B/L (82 gegen 48 mJ).
   - Die groessten Endmomente sitzen an den Ringenden der Speichen (bis 0,82 B/L = 32 N mm), an den Spitzen fast
     keine (<= 0,026). Im Stab erreicht das Moment 0,96 B/L (37 N mm, Biegespannung ~3 MPa).
5. **Vorab:** F0 eingetroffen, F1 nicht eingetroffen, F2 nicht eingetroffen nach der eingefrorenen strengen Regel (alle
   Speichen geknickt; schwache Lesart "ein Stab": eingetroffen), F3 eingetroffen. Jeweils gleich bei N = 12 und 20.

## Vorab gegen Ausgang

Mechanisch nach PLAN.md (Messschwelle s = 100 x groesster Gleichgewichtsrest, bei g_12 und g_20 5,2e-9 und 6,2e-9).
Die Urteile stehen in lauf-69/auswertung.json.

| Nr | Vorhersage | Wahrsch. | Ausgang |
|---|---|---|---|
| F0 | Kontrolle: 1 Tetraeder und 4 um eine Kante (offen) spannungsfrei, \|F\| L und \|tau\| < 1e-8 | 90 % | **eingetroffen**: alle acht Laeufe (G und E, N = 12 und 20) \|F\| <= 5,1e-9 (k1_E_12; alle anderen <= 4,9e-10), \|tau\| <= 2,5e-10; der Anstoss ist verschwunden (Stich <= 1,1e-11) |
| F1 | (G) Achse unter Zug, Speichen und Ring unter Druck | 55 % | **nicht eingetroffen**: Achse +24,26 / +24,36 (N = 12 / 20), Speichen -9,25 bis -9,93 / -9,29 bis -9,97, **Ring +14,07 / +14,13 (Zug)** |
| F2 | (G) Mindestens eine gedrueckte Stabart knickt aus (Stich > 1 % L) | 65 % | **nicht eingetroffen** nach der Regel "alle Staebe der Art": Speichen alle gedrueckt, aber nur 5 von 10 geknickt (Stich 0,098; die anderen 5 gerade, Stich < 2e-14). Achse und Ring stehen unter Zug. Schwache Lesart "ein Stab" (nur berichtet): eingetroffen |
| F3 | (E) Energie hoeher als bei (G); ueber 80 % davon Biegung | 55 % | **eingetroffen**: 2,1045 gegen 1,2388 (N = 12), 2,1274 gegen 1,2435 (N = 20), Faktor 1,70 bzw. 1,71; Biegeanteil 92,8 % bzw. 92,7 % |

**Bedeutung (vorab festgelegt) und was davon ausgeloest ist:**
- Fall "F1 bis F3 treffen ein" (Biegung und Ausknicken statt Dehnung, Zug in der Achse; ein Knicklicht-Raum waere an
  jeder Fuenfer-Kante sichtbar verbogen [H]): **nicht ausgeloest**, F1 und F2 sind nicht eingetroffen.
  - Beschreibend gilt der erste Teil trotzdem: Die Luecke wird als Biegung aufgenommen (96 % bzw. 93 %), mit Zug in
    der Achse. Das ist keine ausgeloeste Bedeutung, nur eine Beschreibung.
- Fall "F1 trifft nicht ein: anderes Vorzeichenmuster, mit dem Eigenspannungsvektor beschreiben": **ausgeloest.**
  - Gemessen (G, N = 20, Axialkraft je Art durch die Achsenkraft): Achse 1, Speichen -0,3953 (Mittel), Ring
    +0,5800. Bei N = 12 gleich auf 4 Stellen.
  - Gelenkwerk-Formel mit h, l_s, l_r aus dem Lauf: Speichen -0,3947, Ring +0,5787. Sie nimmt gleiche Speichen und den
    Ring in der Mitte an; die 0,2 % Abweichung kommen aus dem Symmetriebruch (Punkt 3).
  - Grund: An jeder Spitze muss der Achsenzug von fuenf gedrueckten Speichen gehalten werden. Diese druecken die
    Ringecken nach aussen, und der Ring haelt sie nur unter Zug zusammen. Das folgt aus dem Gleichgewicht allein, ohne
    Materialwerte [M].
  - Mit Einspannung bleibt das Muster gleich (Achse +43,8, Speichen -17,1/-17,3, Ring +25,2).

## Lesart [H] (nachtraeglich, ausser dem Schreibtisch in PLAN.md Abschnitt 5)

- **Warum die Achse fast nicht laenger wird:** Ein gerader Stab erreicht die Euler-Last schon bei 0,04 % Stauchung
  (pi^2/Ks); 5 % Laengenfehler als Dehnung kosteten das 130-fache der Euler-Last. Billiger ist es, die Speichen
  auszuknicken: Ein geknickter Stab traegt nur noch etwa die Euler-Last und gibt laengs fast beliebig nach. Mein Schreibtischwert vor den Laeufen: Energie 1,26 B/L, 96 % Biegung,
  Achse +25, Ring +15. Gemessen: 1,24, 96 %, +24,4, +14,1.
- **Warum nur eine Speichenfamilie knickt (Abschaetzung, nicht im Code geprueft):**
  - Verschiebt sich der Ring um dz entlang der Achse, werden die Speichen an einer Seite kuerzer, an der anderen
    laenger.
  - Zehn gedrueckte Speichen geben dafuer eine negative Steifigkeit von etwa -10 P R^2/l^3 ~ -74 B/L^3.
  - Geknickte Speichen sind laengs nur mit P_E/(2L) ~ 4,9 B/L^3 je Stab steif (Elastica); zusammen
    +10 x 4,9 x (h/2l)^2 ~ +13 B/L^3.
  - Der symmetrische Zustand ist danach instabil, der Ring rutscht, bis die Speichen der einen Seite gerade und laengs
    wieder steif sind.
  - Hesse-Matrix im gefundenen Zustand: fuenf Nullrichtungen (Drehung der fuenf geknickten Speichen um ihre Sehne,
    |EW| <= 2,2e-11), danach 0,012 und 0,015 (positiv): stabil.
- **Einspannung:** Die eingespannten Speichen sind laengs steifer (Druck 1,74-fache Euler-Last mit Gelenken). Der
  kleinste Hesse-Eigenwert ist 7,8e-4 bis 1,1e-3, also fast null: Der Zustand liegt knapp neben derselben Verzweigung,
  daher die leichte Ungleichheit (Stich 0,063 gegen 0,074, Ring 0,004 L verschoben).

## Tabellen je Lagerung (N = 20; in Klammern N = 12)

**(G) Gelenke, Lauf g_20 (Anstoss aus):**

| Stabart | Axialkraft (B/L^2) | echt (N) | Stich (L) | Sehne | Moment im Stab max (B/L) | Euler-Verhaeltnis |
|---|---|---|---|---|---|---|
| Achse | +24,360 (+24,258) | +4,7 | 0 | 1,00095 | 0 | Zug |
| Speichen an A (gerade) | -9,289 (-9,250) | -1,8 | < 2e-14 | 0,99964 | 2e-13 | 0,94 |
| Speichen an B (geknickt) | -9,970 (-9,929) | -1,9 | 0,0982 (0,0984) | 0,97551 | 0,979 (0,977) = 38 N mm, 3,1 MPa | 1,01 |
| Ring | +14,128 (+14,069) | +2,7 | 0 | 1,00055 | 0 | Zug |

- Endmomente: 0 (Gelenk). Querkraft an den Stabenden <= 1,5e-11 (Endkraft entlang der Sehne, wie bei einem Gelenk).
- Energie 1,24352 (1,23884) B/L = 48 mJ: Biegung der geknickten Speichen 1,1948; Dehnung Achse 0,0116, Speichen 0,0177,
  Ring 0,0195. Biegeanteil 96,1 %.
- Achse 1,00095; Ringradius 0,85112 (Soll mit Ring 1: 0,85065); Ring 0,5243 unter A, die Mitte waere 0,5005.
- Welche Spitze knickt, legt der Rechenweg fest (hier stets B, in allen G-Laeufen und im Rauchlauf; vermutlich wegen
  der Lager, A fest und B frei in z [H]). Gespiegelt ist es dieselbe Energie.

**(E) Einspannung, Lauf e_20 (gewertet, gleich e_aus_20):**

| Stabart | Axialkraft (B/L^2) | echt (N) | Stich (L) | Sehne | Endmoment Spitze / Ring (B/L) | Moment im Stab max | Euler-Verh. |
|---|---|---|---|---|---|---|---|
| Achse | +43,750 (+43,233) | +8,4 | 0 | 1,00171 | 1e-13 | 0 | Zug |
| Speichen an A | -17,126 (-16,935) | -3,3 | 0,0629 (0,0638) | 0,98955 | 0,0018 / 0,676 | 0,804 | 1,74 |
| Speichen an B | -17,316 (-17,105) | -3,3 | 0,0744 (0,0743) | 0,98553 | 0,026 / 0,821 = 32 N mm | 0,962 = 37 N mm, 3,0 MPa | 1,75 |
| Ring | +25,234 (+24,940) | +4,9 | 0,0065 | 1,00052 | 0,650 / 0,647 | 0,504 | Zug |

- Querkraft an den Enden: Speichen bis 0,84, Ringstaebe 1,29 B/L^2.
- Abweichung von der Einspannrichtung: Speichen an der Spitze <= 0,04 Grad, am Ring 0,9 bis 1,2 Grad; Ringstaebe
  0,93 Grad.
- Energie 2,12738 (2,10450) B/L = 82 mJ. Biegung innen: Speichen 1,6976, Ring 0,1504; Einspannterme: Speichen 0,0708,
  Ring 0,0526; Dehnung: Achse 0,0374, Speichen 0,0566, Ring 0,0621. Biegeanteil 92,7 %.
- Achse 1,00171; Ringradius 0,85110; Ring 0,5048 unter A (Mitte 0,5009).
- Wunschrichtungen M: bei A Achse-Speiche 59,998 Grad, benachbarte Speichen 61,198 Grad; bei r_0 Speiche-Speiche
  60,004, Speiche-Ring 59,401, Ring-Ring 108,000.

**Variante K (nur berichtet), Lauf ek_20:** Einspannrichtungen der geschlossenen Bipyramide mit Achse 1,0515.
- Energie 2,17585 (2,15272), also 2,3 % mehr als M. Achse +45,19; Speichen -17,07 (A) und -17,73 (B); Ring +25,30.
- Staerker ungleich: Stich 0,044 und 0,086; Ring 0,514 unter A.
- Die Wahl der Wunschrichtungen aendert die Zahlen also um wenige Prozent, nicht das Bild.

## Kontrollen

- **F0** (1 Tetraeder und 4 offen, G und E, N = 12 und 20): spannungsfrei, siehe Tabelle. Newton 5 bis 6 Schritte
  bis zum Rundungsboden; k1_G_12 brauchte 49, k1_E_12 lief bis an die Zeitgrenze (Selbstanzeigen).
- **Gleichgewicht:**
  - Rest der freien Komponenten: Hauptlaeufe <= 9,4e-11, Kontrollen <= 1,1e-9 (k1_E_12: 9,9e-9).
  - Reaktionen an den Lagern: Hauptlaeufe Kraft <= 5,1e-11, Moment <= 3,3e-10; Kontrollen <= 1,2e-9. Das Gebilde ist
    in sich ausgeglichen, die Lager tragen nichts.
  - Gradient am Ende <= 4,6e-10 (Hauptlaeufe). In keinem echten Lauf war ein Stoss aus einem Sattel noetig.
- **Gelenk-Probe (G):** Querkraft an den Stabenden <= 1,5e-11, die Endkraft liegt also auf der Sehne.
- **Gitter N = 12 gegen 20:**
  - G: Energie 0,38 %, Axialkraefte 0,42 %, Stich 0,21 %.
  - E: Energie 1,08 %, Axialkraefte 1,17 %, Stich der Speichen 0,13 %, der Ringstaebe 3,2 %. K: 1,06 %.
  - Alle Urteile gleich.
- **Knickrichtung (G):** g_ein_20 gegen g_20: Energie gleich auf 1,4e-13, Axialkraefte auf 2,1e-11. Auch mit dem
  Anstoss nach innen knickt dieselbe Speichenfamilie (an B).
- **Ast (E):** e gegen e_aus: Energie gleich auf 8e-14, Axialkraefte auf 1,1e-8 (beide N). Ohne und mit Anstoss derselbe
  Zustand.
- **Stabilitaet:**
  - G: fuenf Nullrichtungen (|EW| <= 2,2e-11), danach 0,012 und 0,015 (N = 20) bzw. 0,016 und 0,020 (N = 12).
  - E: kleinster Eigenwert 7,8e-4 (N = 20) bzw. 1,1e-3 (N = 12); K: 6,6e-3 bzw. 1,1e-2.
  - Alle positiv (stabil). Bei E ist der Abstand zur Verzweigung klein.
  - Die Zahlen haengen von N ab, weil die Koordinaten nicht massegewichtet sind; aussagekraeftig ist das Vorzeichen.
- **Schreibtisch gegen Rechnung (G):** Energie 1,26 gegen 1,24; Achse +25 gegen +24,4; Ring +15 gegen +14,1;
  Biegeanteil 96 % gegen 96,1 %. Der Schreibtisch nahm zehn gleich geknickte Speichen mit Stich 0,07 an. Das war falsch:
  Es knicken fuenf, mit 0,098.

## Latten (v3)

- L1: ja. F1 und F2 (streng) sind gescheitert.
- L2: ja. Die Kontrollen (1 und 4 Tetraeder) laufen durch denselben Code; der Schreibtischwert fuer G (Energie,
  Kraefte, Biegeanteil) stand vor den Laeufen in PLAN.md und trifft auf wenige Prozent.
- L3: ja. N = 12 und 20, Urteile gleich; zwei Anstoesse je Lagerung; zwei Wunschrichtungen (M, K) fuer E.
- L4: teilweise.
  - Ein Stabwerk mit einem ueberzaehligen Stab hat genau eine Eigenspannung; das Vorzeichenmuster folgt aus dem
    Gleichgewicht (Pellegrino und Calladine) [L].
  - Nachknick-Verhalten und axiale Weichheit geknickter Staebe (Elastica) sind Lehrbuchstoff [L].
  - Fuer den Symmetriebruch (nur eine Speichenfamilie knickt) in einer frustrierten Bipyramide habe ich nicht gesucht
    (keine Websuche in diesem Auftrag).
- L5: nein, aber machbar. 16 Knicklichter mit Verbindern: Vorhersage [H] fuer lose Verbinder: an einer Spitze fuenf
  sichtbar gebogene Speichen (~2 cm Stich), an der anderen fuenf gerade; mit festen Verbindern alle zehn gebogen
  (1,3 bis 1,5 cm).

## Literatur [L, aus dem Gedaechtnis, Angaben nicht nachgeprueft]

- S. Pellegrino, C. R. Calladine, Int. J. Solids Struct. 22 (1986) 409 ("Matrix analysis of statically and
  kinematically indeterminate frameworks"): Eigenspannungen und Mechanismen, Maxwell-Zaehlregel.
- S. P. Timoshenko, J. M. Gere, Theory of Elastic Stability (1961): Elastica, Nachknicken, P/P_E ~ 1 + Delta/(2L).
- J. M. T. Thompson, G. W. Hunt, A General Theory of Elastic Stability (1973): Verzweigung und Symmetriebruch.
- J.-F. Sadoc, R. Mosseri, Geometrical Frustration (1999): fuenf Tetraeder um eine Kante, 600-Zelle (siehe RUNDE-17).

## Selbstanzeigen

- **Regel nach dem Rauchlauf nicht gelockert:** Der Rauchlauf rauchG (anderer Fehlpass) zeigte schon vor dem Einfrieren,
  dass nur eine Speichenfamilie knickt. Die F2-Regel ("alle Staebe der Art") stand vorher fest (05:28:38 gegen Lesen um
  05:29:28) und blieb. Nach der wortnaeheren schwachen Lesart der Karte waere F2 eingetroffen. Welche Lesart die Karte
  meinte, entscheidet die Leitung; mechanisch gilt die eingefrorene.
- Nach dem Rauchlauf geaendert (offen in PLAN.md Abschnitt 6): Sattelflucht im Loeser (rauchE lief zuerst in einen
  Sattel) und feines Gitter N = 20 statt 24 (Laufzeit). In keinem echten Lauf war ein Stoss noetig.
- Der Rauchlauf zeigte auch die Groessenordnung von F3 (Biegeanteil 0,81 bei kleinerem Fehlpass) vor den echten
  Laeufen.
- code/laeufe.sh (Startskript) habe ich nach dem Einfrieren geschrieben; es setzt nur die Lauftabelle aus PLAN.md
  Abschnitt 2 um (Argumente wie dort).
- Die Wunschrichtungen M (Mittel ueber die Tetraeder, Luecke gleichmaessig verteilt) sind meine Festlegung; die Karte
  liess das offen. Variante K aendert die Energie um 2,3 %.
- **k1_E_12 (Kontrolle) endete an der internen Zeitgrenze (480 s), nicht am Rundungsboden.**
  - Der Gradient blieb bei 1,38e-8 stehen, knapp ueber der Abbruchschwelle 1e-8 meines Loesers. Jeder Schritt trieb die
    Verschiebung auf 6e7 und kam nur 2e-10 weit.
  - Die Kraefte liegen trotzdem bei <= 5,1e-9, also unter der F0-Grenze 1e-8, aber nur um den Faktor 2. Der Lauf ist
    gewertet, weil die Spur ihn nicht abbrach (rc = 0) und die interne Zeitgrenze im Plan steht.
  - Ursache ist eine Schwaeche der Abbruchregel am Rundungsboden, keine Physik [H]: k1_E_20, k4_E_12 und k4_E_20
    enden nach 5 bis 6 Schritten mit Gradient <= 9e-10.
- Grenzen: keine Torsion, ideal starre Verbinder, keine Beruehrung zwischen Staeben, kein Eigengewicht. Knicklicht-Zahlen
  fuer einen vollen Stab; echte sind hohl. Die Stabilitaet ist nur ueber die Hesse-Matrix geprueft, nicht durch
  Stoerung im Grossen; ein tieferer Zustand mit anderer Knickverteilung ist nicht ausgeschlossen.

## Einfach gesagt

Fuenf gleiche Tetraeder passen nicht ganz um eine gemeinsame Kante, es bleibt ein Spalt von gut 7 Grad. Baut man sie
trotzdem aus 16 gleich langen, biegsamen Staeben zusammen, muss etwas nachgeben. Die Rechnung zeigt: Die Mittelachse wird
gezogen, der Ring aussen herum auch, und die zehn schraegen Speichen werden gedrueckt und biegen sich. Ueberraschend:
Wenn die Staebe in den Ecken locker sitzen, biegen sich nur die fuenf Speichen an einer Spitze, die anderen fuenf bleiben
gerade. Sitzen die Staebe fest in den Ecken, biegen sich alle zehn, und das Ganze speichert fast doppelt so viel Spannung.
