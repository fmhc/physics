# STILLE-GITTER-2: Ergebnis (Code-Agent, Runde 24, explorativ)

- Code-Agent (Claude, Anthropic) im Auftrag der Leitung claude-primary. Beginn 2026-10-02 23:49:02 CEST (date).
- Rauchlaeufe R1 bis R3 (h = 0,45, 0,22, 0,21; in keinem echten Lauf): .69, 22:00:43 bis 22:11:18 UTC.
- Plan eingefroren 2026-10-03 00:11:56 CEST (PLAN.md.eingefroren-20261003-001156), nach den Rauchlaeufen und vor jedem
  echten Lauf.
  - Code: code/stille_gitter2.py, sha256 70b81d84e24af9a747854e1db9d862ded72c36a925e1b8eb1aca174e3d6f05e7
  - Auswertung: code/auswertung2.py, sha256 3e487ed48ef2d6f997dd510f71685c29c164e284fe73b9017e680865628398a1
  - Beide vor dem Einfrieren geschrieben, lokal = .69, schreibgeschuetzt.
- **K0** (Quadratgitter, Sterne A und B bei h = 0,3): .69, 22:12:16 bis 22:16:08 UTC, beide rc = 0.
  - Mechanisch ausgewertet 22:16:17 UTC: bestanden.
- **Hauptlaeufe** (Dreiecksgitter, h = 0,5 / 0,4 / 0,3 / 0,25 / 0,2): .69, 22:16:23 bis 22:21:02 UTC.
  - Alle rc = 0, je 18 Punkte, nichts fehlt.
- Auswertung mechanisch mit auswertung2.py auf der .69 (kleintest.sh, cpu3): 22:21:25 UTC, ueber lauf/gesamt (Kopie der
  sieben Scan-Dateien). Tabellen lokal mit jq aus lauf-69/.
- Ergebnis geschrieben ab 2026-10-03 00:25:51 CEST (date); Ende in der letzten Zeile.
- Explorativ (v3). Deutungen [H, Modell M1, 2D, Sprosse n = 7, Q-Ball auf einem Gitterpunkt, nur A1-Sektor].

## Ergebnis zuerst

1. **Auch auf dem Dreiecksgitter bleibt die stille Mode fast still.**
   - Restbreite am Minimum: 1,83e-8 (h = 0,5) bis 8,7e-12 (h = 0,2).
   - **Gamma_min ~ h^(8,34 +- 0,06)**; die oertlichen Exponenten fallen von 8,66 auf 8,11 (zwischen h = 0,25 und 0,2).
   - TG1 ist eingetroffen.
2. **Der Rest geht praktisch ganz in den cos 6theta-Kanal (l = 6).**
   - Der l = 6-Anteil am Fluss (r = 20) ist bei allen h mindestens 0,99998. l = 0 und l = 12 liegen unter 2e-5.
   - TG2 ist eingetroffen.
3. **Bei gleichem Abstand ist das Dreiecksgitter das stillste der drei Gitter-Rezepte.**
   - Bei h = 0,3: 2,39e-10 gegen 4,0e-9 (isotroper 9-Punkt-Stern) und 2,3e-5 (5-Punkt-Stern). TG3 ist eingetroffen.
   - Das Verhaeltnis zum 9-Punkt-Stern sinkt von 18,0 (h = 0,5) auf 16,3 (h = 0,2).
   - [H, nachtraeglich] Es laeuft gegen 16 = (5760/1440)^2, das Quadrat des Verhaeltnisses der Anisotropie-Amplituden
     (Schaetzung der Karte).
4. **Die Sprosse wandert wie h^2**: q = 2,20 +- 0,02. Die h^2-Extrapolation liegt 3,8e-6 unter 0,529266. TG0 ist
   eingetroffen.
   - [H] Die Sprosse liegt fast auf der von Stern A (Abstand ~ -1,6e-4 h^4). Beide Sterne haben bis h^4 dieselben
     isotropen Fehlerterme.
5. **Randmethode und Rechenboden.**
   - Neue Randmethode: radiale PML ueber komplexe Knotenkoordinaten in der FEM-(Kotangens-)Form.
   - K0 bestanden: Auf dem Quadratgitter trifft sie RUNDE-23 auf +1,6e-5 (A) und -1,1e-5 (B), relativ.
   - Rechenboden 3e-15 bis 6e-14; alle Breiten liegen mindestens 1200-fach darueber.
   - Bedeutung nach Karte: Die Regel gilt auch fuer C6. Der Exponent folgt aus der Ordnung der niedrigsten
     Anisotropie, der Abstrahlkanal aus ihrer Winkelzahl [H, 2D, M1].

## Vorab gegen Ausgang

Mechanisch nach PLAN.md Abschnitt 5 (auswertung2.py, lauf-69/auswertung/auswertung.json); fuenf Karten-h, alle ueber dem
Rechenboden.

| Nr | Vorhersage (Karte) | Wahrsch. | Ausgang |
|---|---|---|---|
| K0 | Quadratgitter, gleiche Randmethode: Restbreite bei h = 0,3 auf 5 % wie RUNDE-23 (2,3375e-5 und 3,9974e-9) | Pflicht | **bestanden**: 2,33754e-5 (+1,6e-5) und 3,99735e-9 (-1,1e-5) |
| TG0 | omega_r^2(h) = omega_r^2(0) + c h^2 (Exponent 2 +- 0,4), Extrapolation innerhalb +-3e-5 um 0,529266 | 70 % | **eingetroffen**: q = 2,195 +- 0,022; Extrapolation (h^2, h <= 0,3) 0,5292622 (-3,8e-6) |
| TG1 | Gamma_min ~ h^p mit p = 8 +- 1,5, aus mindestens drei h ueber dem Rechenboden | 55 % | **eingetroffen**: p = 8,344 +- 0,059 aus fuenf h, alle ueber dem Boden |
| TG2 | am Minimum >= 80 % des abgestrahlten Flusses in l = 6, fuer alle h <= 0,4 | 60 % | **eingetroffen**: 0,999998 / 1,000001 / 1,000002 / 1,000015 (h = 0,4 / 0,3 / 0,25 / 0,2) |
| TG3 | bei h = 0,3 ist Gamma_min(Dreieck) kleiner als 4,0e-9 | 55 % | **eingetroffen**: 2,386e-10, also 16,8-mal kleiner |

- Anteile ueber 1 bei TG2: Die l = 0-Anteile sind dort leicht negativ (bis -1,5e-5). Das ist Rauschen der
  Kreiszerlegung in der Hoehe 1e-5 des Gesamtflusses.

**Bedeutung (nach Karte):**
- TG1 und TG2 treffen ein, also gilt die erste Zeile der Karte: "Die Regel gilt auch fuer C6. Der Exponent folgt aus der
  Ordnung der niedrigsten Anisotropie, der Abstrahlkanal aus ihrer Winkelzahl [H, 2D, M1]."
  - Quadrat, 5-Punkt: Anisotropie cos 4theta in h^2, Breite ~h^4,15, Kanal l = 4 (RUNDE-23)
  - Quadrat, 9-Punkt: cos 4theta in h^4, ~h^8,36, l = 4 (RUNDE-23)
  - Dreieck, 7-Punkt: cos 6theta in h^4, ~h^8,34, l = 6 (hier)
- TG3 trifft ein: "Bei gleichem Abstand ist das Dreiecksgitter das stillste der drei gerechneten."
  - Es braucht dafuer nur 7 Punkte je Stern, der 9-Punkt-Stern 9.
  - Je Flaeche hat das Dreiecksgitter bei gleichem Abstand h aber 2/sqrt3 = 1,15-mal so viele Knoten.
- **Einschraenkungen:**
  - ein Modell (M1), 2D, eine Sprosse (n = 7), Q-Ball auf einem Gitterpunkt, nur der A1-Sektor
  - drei Sterne auf zwei Gittern; unregelmaessige Graphen sind nicht getestet
  - [H] Die Regel ist weiter das Gesetz Gamma ~ (Symmetriebruch)^2 fuer gestoerte BICs (RUNDE-23, L4), mit der
    Anisotropie-Amplitude des Sterns als Bruchparameter. Neu ist hier nur die Bestaetigung fuer eine zweite
    Gittersymmetrie und einen anderen Kanal.

## Tabellen

**Dreiecksgitter (7-Punkt-Stern).**
- Gamma = -Im rho am Minimum. "Fit" ist das Minimum der Parabel aus der S3-Runde; "direkt" die Rechnung bei x*.
- Boden = |MIN - DOPPEL| + |MIN - P2|.
- F-Anteile: Fluss des offenen Kanals v am MIN-Punkt, Kanaele cos(6 j theta).

| h | omega_r^2(h) | Gamma_min (Fit) | sigma Fit | Gamma direkt | Boden | Gamma/Boden | a | Re rho | F0 / F6 / F12 (r = 20) | F6 (r = 22,5) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0,5 | 0,5302200 | 1,8322e-8 | 1,3e-11 | 1,8320e-8 | 5,5e-14 | 3,3e5 | 2776 | 1,557828 | 1,2e-5 / 0,99998 / 6,2e-6 | 0,99998 |
| 0,4 | 0,5298558 | 2,6545e-9 | 1,0e-12 | 2,6542e-9 | 3,1e-15 | 8,6e5 | 2951 | 1,557312 | 1,2e-6 / 0,999998 / 9,7e-7 | 0,999997 |
| 0,3 | 0,5295897 | 2,3862e-10 | 2,1e-13 | 2,3851e-10 | 6,8e-15 | 3,5e4 | 3084 | 1,556930 | -6e-7 / 1,000001 / 7e-8 | 1,000000 |
| 0,25 | 0,5294889 | 5,3327e-11 | 1,7e-13 | 5,3232e-11 | 4,3e-15 | 1,2e4 | 3136 | 1,556783 | -2,4e-6 / 1,000002 / 1,7e-8 | 1,000000 |
| 0,2 | 0,5294079 | 8,7304e-12 | 1,6e-13 | 8,6367e-12 | 7,1e-15 | 1,2e3 | 3178 | 1,556665 | -1,5e-5 / 1,000015 / 2,6e-9 | 0,999999 |

**Fit-Exponenten** (Unsicherheit: Standardfehler bzw. Kovarianz des Fits, ohne die Abweichung von reiner Potenzform):

| Groesse | Dreieck (hier) | Quadrat B, RUNDE-23 (gleiche fuenf h) |
|---|---|---|
| p (log Gamma_min gegen log h) | 8,344 +- 0,059 | 8,45 +- 0,07 |
| oertlich 0,2-0,25 / 0,25-0,3 / 0,3-0,4 / 0,4-0,5 | 8,11 / 8,22 / 8,37 / 8,66 | 8,18 / 8,28 / 8,48 / 8,85 |
| q (omega_r^2 = w0 + c h^q) | 2,195 +- 0,022 (w0 = 0,5292837) | 2,26 |
| Extrapolation w0' (linear in h^2, h <= 0,3) | 0,5292622 (-3,8e-6) | -7,5e-6 |
| c' (Steigung in h^2) | 3,637e-3 | 4,875e-3 (mit h = 0,15; Stern A dort 3,631e-3) |

- Die oertlichen Exponenten fallen zu kleinem h monoton und laufen auf 8 zu, wie bei Stern B. Die Korrekturen hoeherer
  Ordnung sind beim Dreieck etwas kleiner.
- Wie in RUNDE-23 nimmt q im Dreiparameter-Fit den h^4-Anteil mit; gewertet ist nach Plan w0'.

**Vergleich mit RUNDE-23 bei gleichem h** (Gamma_min, Fit; nur berichtet):

| h | 5-Punkt (A) / Dreieck | 9-Punkt (B) / Dreieck |
|---|---|---|
| 0,5 | 1,1e4 | 17,99 |
| 0,4 | 2,9e4 | 17,25 |
| 0,3 | 9,8e4 | 16,75 |
| 0,25 | 2,1e5 | 16,56 |
| 0,2 | 5,1e5 | 16,29 |

- Mit den direkten Werten statt der Fit-Werte: B/Dreieck = 17,99 / 17,25 / 16,76 / 16,58 / 16,45.

## K0-Nachweis

Dieselbe Randmethode und derselbe Code wie beim Dreieck, nur `--typ sq`; Startwerte = Minima von RUNDE-23.

| Stern | h | omega_r^2 (hier / RUNDE-23) | Gamma_min Fit (hier) | RUNDE-23 | relativ | Gamma direkt (hier / RUNDE-23) | Boden | F0 / F4 / F8 (r = 20) |
|---|---|---|---|---|---|---|---|---|
| A | 0,3 | 0,5295910 / 0,5295910 | 2,337538e-5 | 2,3375e-5 | +1,6e-5 | 2,337529e-5 / 2,337529e-5 | 6,5e-11 | 0,013 / 0,979 / 0,007 (RUNDE-23 ebenso) |
| B | 0,3 | 0,5297012 / 0,5297012 | 3,997355e-9 | 3,9974e-9 | -1,1e-5 | 3,99692e-9 / 3,99701e-9 | 1,8e-14 | 0,000 / 1,000 / 0,000 |

- Gegen die ungerundeten Werte von RUNDE-23 (2,3375381e-5 und 3,9974341e-9): A +1e-8, B -2,0e-5.
- Bei B ist der Abstand (8e-14) so gross wie der eigene P1/P2-Abstand von RUNDE-23 bei h = 0,3 (7e-14).
- Re rho stimmt auf 1e-9 (A 1,5569344, B 1,5570905), die Kruemmung a auf 0,01 (3062,9 und 3027,7).
- Schranke 5 %; erreicht sind 2e-5.
- **Vorgeschichte (Rauchlaeufe, PLAN.md Abschnitt 2):** Mit RUNDE-23s PML-Werten in radialer Form (Einsatz bei r = 24,
  Dicke 16, quadratisch) fehlten am Minimum absolut 5e-11 (Dreieck) bis 1e-10 (B).
  - Bei h = 0,45 waren das 7e-3 bzw. 8e-4 relativ; K0 haette das noch bestanden.
  - Bei kleinem h haette dieser Fehler den Rechenboden bestimmt.
  - Der Fehler fiel mit spaeterem Einsatz (r = 30) und glatterem Profil (p = 3). Darum P1 = 30/22/3/3 und
    P2 = 34/26/2/3, beides vor dem Einfrieren.

## Kontrollen

- **Numerik ueber alle 126 Punkte** der sieben gewerteten Laeufe (Scans und P2):
  - Residuum ||Q(rho) x|| <= 2,6e-14 (x normiert); Arnoldi gegen Nachverfeinerung <= 6,9e-15.
  - Q-Ball-Newton max|F| <= 9,1e-12.
  - Die Auswahl war immer eindeutig: l0-Anteil der gewaehlten Mode >= 0,9965 (Quadrat A) bzw. >= 0,99999 (Dreieck).
  - Laengste Einzelrechnung 21,4 s (P2 von K0B), laengster Lauf 278 s (T020), alle unter 10 min.
- **Suche:** In allen sieben Laeufen lag das S1-Minimum innen (keine Randerweiterung) und der S3-Scheitel im Fenster
  (keine zweite S3-Runde).
- **Fit gegen direkt:** Das Fit-Minimum liegt ueber der direkten Rechnung bei x*.
  - Relativ 9e-5 (h = 0,5), 1,2e-4, 4,5e-4, 1,8e-3 und 1,1e-2 (h = 0,2); absolut bei kleinem h ~1e-13.
  - Das liegt in der Fit-Unsicherheit (1,6e-13 bei h = 0,2), aber ueber dem geplanten Boden; der Boden enthaelt die
    Fit-Unsicherheit nicht (wie B015 in RUNDE-23).
  - Mit den direkten Werten waere p = 8,354 statt 8,344 (oertlich 8,15 / 8,23 / 8,38 / 8,66). Kein Urteil aendert sich.
  - Auch mit diesem Abstand als Boden liegt h = 0,2 noch 93-fach darueber.
- **Rechenboden:** Die PML-Probe dominiert ausser bei h = 0,2 (DOPPEL 3,2e-15, P2 3,9e-15). Relativ zur Breite: 3e-6
  (h = 0,5) bis 8e-4 (h = 0,2).

**Nebenbefunde (nachtraeglich, ohne Wertung):**
- **Kontinuumsgrenze** (Zwei-Punkt-Richardson h = 0,2 und 0,25, linear in h^2):
  - omega_r^2(0) = 0,5292640, gegen 0,5292654 +- 2e-6 (F7b, RUNDE-12)
  - Re rho(0) = 1,5564551, gegen rho* = 1,556457
  - Kruemmung a(0) = 3253, gegen 57^2 = 3249
  - Der Abstand von 1,4e-6 ist groesser als in RUNDE-23 (h = 0,15 und 0,2); dort lag das kleinste h tiefer.
- **Lage gegen Stern A:** omega_r^2(Dreieck) - omega_r^2(A, RUNDE-23) = -1,02e-5 / -4,0e-6 / -1,3e-6 / -6e-7 / -3e-7
  (h = 0,5 bis 0,2). Geteilt durch h^4: -1,63e-4 / -1,58e-4 / -1,56e-4 / -1,61e-4 / -1,79e-4, also ~ -1,6e-4 h^4.
  - [H] Das passt zu gleichen isotropen Termen bis h^4 und einer Wirkung der A-Anisotropie in zweiter Ordnung.
  - Die Startwerte des Plans nutzten das schon (aus dem Rauchlauf bei 0,45).
- **Verhaeltnis zum 9-Punkt-Stern:** 17,99 / 17,25 / 16,75 / 16,56 / 16,29, grob 16 + 8 h^2.
  - Ausgleichsgerade in h^2 ueber alle fuenf h: Achsenabschnitt 16,02, Steigung 7,9 (Fit-Werte).
  - Mit den direkten Werten: 16,12 und 7,4.
  - [H] Das ist das Quadrat des Verhaeltnisses der anisotropen Symbol-Anteile, (h^4 k^6/1440) gegen (h^4 k^6/5760).
  - Die Lesart aus RUNDE-23 ("Breite = Quadrat des anisotropen Symbol-Anteils bei der Abstrahl-Wellenzahl") traegt
    damit auch ueber verschiedene Kanaele (l = 4 gegen l = 6).
  - Der Kanal selbst gibt in dieser Naeherung keinen eigenen Faktor.
- **Fernfeld:** Der l = 0-Anteil auf dem Messkreis ist bei h = 0,5 und 0,4 1,2e-5 und 1,2e-6.
  - Die Abschaetzung des Plans (Phase beta = 0,063 h^4 aus der Gitterdispersion, Anteil ~beta^2/2) gibt 7,7e-6 und 1,3e-6.
  - Bei kleinerem h liegt er im Rauschen (|F0| <= 1,5e-5, auch negativ).
  - Der l = 12-Anteil faellt wie ~h^8: 6,2e-6 / 9,7e-7 / 7e-8 / 1,7e-8 / 2,6e-9. Der l = 12-Fluss geht damit wie ~h^16.
  - [H] Das ist die zweite Ordnung der cos 6theta-Anisotropie (cos 6theta mal cos 6theta enthaelt cos 12theta).
- **Wandradius** Achse minus 30 Grad: -0,008 (h = 0,5), sonst zwischen -0,003 und +0,001, ohne saubere Skalierung. Das
  Halbwertsmass ist dafuer zu grob (wie bei Stern B in RUNDE-23).

## Latten (v3)

- **L1 (kann scheitern): ja.**
  - Vier Vorhersagen mit Zahlengrenzen vor jeder Rechnung, dazu die Pflichtkontrolle K0.
  - TG3 haette bei einem anderen Kanalfaktor (l = 6 gegen l = 4) leicht scheitern koennen. Die Karte gab ihm 55 %.
- **L2 (Gegenprobe): ja, teilweise.**
  - K0 ist die Gegenprobe der Randmethode: gleicher Code, anderes Gitter, bekannte Antwort, auf 2e-5 getroffen.
  - Mechanismusprobe: Fernfeldzerlegung (l = 6 statt l = 4) und das Verhaeltnis zu Stern B.
  - Numerische Proben: Doppelrechnung und PML-Probe.
  - Es fehlt weiter eine unabhaengige zweite Methode, etwa eine Zeitentwicklung.
- **L3 (Numerik): ja.**
  - Boden 3e-15 bis 6e-14, alle Breiten >= 1200-fach darueber.
  - Kontinuumsgrenze auf 1,4e-6 (omega_r^2) bzw. 2e-6 (Re rho).
  - Offen:
    - nur eine Randmethode-Familie (radiale FEM-PML) mit zwei Einstellungen
    - nur eine Fernfeld-Definition
    - Fit-Minimum bei h = 0,2 1,1 % ueber der direkten Rechnung (siehe Kontrollen)
- **L4 (schon bekannt): teilweise.**
  - [S] Chow, Nucl. Phys. B 547, 281 (1999), arXiv:hep-lat/9810051, an der Quelle gelesen (S. 1 bis 20):
    - Gl. (2.8), die "one shell discretization" 2n (Mittel ueber die naechsten Nachbarn - phi(0))/rho^2, ist fuer das
      Gitter A_2 ("for n = 2 the hexagonal lattices", S. 9) genau unser 7-Punkt-Stern.
    - Gl. (5.5): skalarer a^2-Fehler E_0 = rho^2 d^4/(4(n+2)), also h^2 d^4/16 in 2D. Das stimmt mit unserem isotropen
      h^2 k^4/16.
    - Abschnitt VII nennt D_4 "the only unexceptional root lattice" mit isotropem a^2-Fehler. Fuer A_2 passt das nicht
      zu unserer Rechnung. Unter C6 gibt es keinen l = 4-Anteil, der a^2-Fehler von A_2 ist isotrop (PLAN.md
      Abschnitt 1). [H] Der Satz meint wohl n >= 3 oder uebersieht n = 2; nicht weiter geprueft.
  - [S, in RUNDE-23 an der Quelle gelesen] Koshelev u. a., PRL 121, 193903 (2018): Q_rad ~ alpha^-2 fuer
    Quasi-BICs. Unser Befund ist dieses Gesetz mit alpha ~ h^4 (cos 6theta-Anteil des Sterns).
  - [S, nur Abstract gelesen] Zhang und Lu, arXiv:2609.29074 (2026), photonischer Kristall mit C6v-Dreiecksgitter:
    - "For at-Gamma BICs, rotational and time-reversal symmetries determine the allowed angular harmonics of the
      leading radiation".
    - Ein C6v-BIC habe dort Q ~ 1/delta^10 (delta = Abweichung des Wellenvektors).
    - [H] Gleiche Logik (Symmetrie waehlt den Kanal, hoehere Symmetrie gibt hoehere Potenz), anderer Parameter.
  - [L?] Frisch, Hasslacher und Pomeau, PRL 56, 1505 (1986): Das Sechseckgitter ist bis zu Tensoren 4. Stufe isotrop
    (Gittergas). Nicht an der Quelle gelesen.
  - [L?] Stille Moden bzw. BICs von Q-Baellen oder Oszillonen auf Dreiecksgittern: nicht gefunden. Das
    Websuch-Kontingent war erschoepft; gesucht nur ueber die arXiv-Schnittstelle (zwei Abfragen).
- **L5 (Messbezug): nein.**
  - [H] Bezug hoechstens zu Gittersimulationen: Auf dem Dreiecksgitter ist die Lebensdauer stiller Moden ein
    Gitterartefakt der Groesse ~h^-8, rund 16-mal laenger als mit dem isotropen 9-Punkt-Stern bei gleichem h.

## Selbstanzeigen

- **Rauchlaeufe vor dem Einfrieren** (h = 0,45, 0,22, 0,21; in keinem echten Lauf, im Plan offengelegt):
  - Sie zeigten die Groessenordnung: Dreieck 7,29e-9 (0,45) und 1,29e-11 (0,21), oertlich ~8,3.
  - Die Vorhersagen der Karte standen vorher fest und sind unveraendert.
  - Die Regeln des Plans standen vor dem Ergebnis von T021 im Entwurf. Danach kamen nur die T021-Zeile, der
    Offenlegungsabsatz und der Wegfall von h = 0,15 hinzu (Zeitgrund, geschaetzt aus N und der Zeit bei h = 0,21,
    nicht gemessen).
- **Randmethode nach dem ersten Rauchlauf geaendert** (vor dem Einfrieren): von 24/16/1,5/2 auf P1 30/22/3/3 und
  P2 34/26/2/3.
  - Grund: P1/P2-Abstand und Vergleich mit RUNDE-23 bei h = 0,45, nicht die Hoehe der Dreiecksbreite.
  - Die eingefrorene P1 ist darum nicht die Einstellung von RUNDE-23. K0 prueft genau diese neue Einstellung.
  - Die Lesart des alten Fehlers (abklingender Schwanz des geschlossenen Kanals u) ist [H] und nicht getrennt geprueft.
    Gestuetzt wird sie nur dadurch, dass der Fehler mit spaeterem Einsatz stark faellt.
- **Geschaetzte Endzeit im Plan:** Dort steht fuer R2 "22:03:37 bis ~22:06 UTC". Gemessen (Logs): 22:03:35 bis
  22:04:37 UTC. Das verstoesst gegen die Regel "nur gemessene Zeiten"; der eingefrorene Plan bleibt unveraendert.
- **K0-Startwerte** sind die Minima von RUNDE-23. Die Suche lief voll (S1 +-2e-4), war damit aber leicht.
- **Hilfsskript im Rauchlauf:** lauf/rauch2/diag.sh ruft kleintest.sh je Spur nacheinander fuer zehn PML-Einstellungen
  auf. Es ist eine Schleife fuer die PML-Diagnose, kein Dienst und kein Hook.
- **Fit-Minimum gegen direkte Rechnung** bei h = 0,2: 1,1 %. Gewertet ist nach Plan der Fit-Wert. Mit den direkten
  Werten aendert sich kein Urteil (p = 8,354).
- **Nachtraegliche Pruefungen** stehen getrennt und ohne Wertung: Richardson, Lage gegen A, Verhaeltnis 16, beta^2/2,
  l = 12-Skalierung.
- **Literatur** erst nach den Laeufen (ab 22:22 UTC).
  - Chow 1999 als PDF gelesen; Zhang und Lu nur im Abstract
  - Die arXiv-Suchen liefen ueber export.arxiv.org; eine Websuche war nicht mehr moeglich (Kontingent erschoepft).
- **Lokal kein Python.** Lokal benutzt: jq, sha256sum, rsync, ssh, scp, cp, chmod, mkdir, grep, date und das
  Lese-Werkzeug fuer das PDF von Chow.
- **Speicher:** Die Zeilen "Memory peak" in den Logs gehoeren zum systemd-Huellprozess. Den Speicherbedarf habe ich
  nicht gemessen; MemoryMax 4G wurde nie ueberschritten (alle rc = 0).
- **Sonst:**
  - nur Spuren cpu, cpu2, cpu3, cpu4 und cpu6; nicht cpu5, keine GPU; jeder Lauf unter 10 min
  - kein git, kein Peerbus, kein Journal, keine Unteragenten, keine Aenderung an Karten oder anderen Runden
  - Auf der .69 wurde nichts in place ueberschrieben (Upload als .neu, dann mv)

## Ablage

- lokal: code/ (stille_gitter2.py, auswertung2.py, stille_gitter2.py.rauch1 = Fassung von R1/R2)
- PLAN.md und PLAN.md.eingefroren-20261003-001156 (sha256 6e6b866806633478d9f06bf06f1dd33bcfd1fccaa83445d7da3506d7345fac6f)
- lauf-69/:
  - rauch/, rauch2/, rauch3/ (Rauchlaeufe), rauch-auswertung/ (Probelauf der Auswertung)
  - k0/ (K0A, K0B), k0-auswertung/
  - haupt/ (T050 bis T020, je .json und .log)
  - gesamt/ (Kopie der sieben gewerteten Scans), auswertung/ (gewertet)
- .69: /home/fmh/fmhc-physics-remote/runde24-stille-gitter-2/ (identisch)

## Einfach gesagt

Im Computer ist der Raum ein Gitter aus Punkten. Letztes Mal haben wir gesehen, dass unser "stilles" Teilchen auf einem
Quadratgitter ein bisschen Energie verliert, in einem Muster mit vier Blaettern. Jetzt haben wir ein Gitter aus
Dreiecken genommen, das sechs gleichberechtigte Richtungen hat, so wie die Mittelpunkte von Bienenwaben. Dort leckt das
Teilchen in einem Muster mit sechs
Blaettern und viel weniger: etwa 16-mal weniger als beim besten Quadrat-Rezept, und halbiert man den Punktabstand, wird
es noch einmal etwa 256-mal weniger. Die Regel aus der letzten Runde stimmt also auch hier: Je weniger der Raum eine
Richtung bevorzugt, desto stiller bleibt das Teilchen.

---
Letzte Aenderung dieser Datei: 2026-10-03 00:29:19 CEST (date). Zeitbox 120 min ab 23:49:02 CEST eingehalten.
