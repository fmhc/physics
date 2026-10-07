# EIS-1: Ergebnis (Code-Agent fuer die Leitung, Runde 34, explorativ)

- Gerechnet auf der .69 (kleintest.sh; Spuren cpu, cpu2 und nach Bitte der Koordination cpu3; nie mehr als zwei
  zugleich):
  - Versionsproben 16:30:06 und 16:30:34 UTC: Python 3.12.3, numpy 2.4.4, scipy 1.18.0, kein numba, gcc 13.3.0.
    Der Monte-Carlo-Kern ist deshalb C (gcc -O2 in der Spur uebersetzt, per ctypes geladen).
  - Rauchlaeufe 16:38:46 bis 16:40:07 UTC (Gittergroessen 2 und 6, keine echte). Rauch-Auswertungen 16:41:58,
    16:45:15 (rc = 1: leerer Bereich bei L = 6 nach der neuen Untergrenze, Schutz eingebaut) und 16:46:00.
  - Echte Laeufe 16:46:41 bis 17:16:58 UTC (18:46 bis 19:17 CEST), alle gewerteten mit rc = 0:
    - Stabnetze und Zaehlungen 16:46:41 bis 16:49:36 UTC
    - sechs gewertete Spin-Eis-Laeufe zu je ~530 s (vier mit L = 12, zwei mit L = 8)
    - ein siebter Start (eis_L8_s2 auf cpu2) nach 33 s gestoppt und auf cpu3 wiederholt (Selbstanzeigen)
  - Auswertung (code/auswertung.py) 17:17:22 bis 17:17:49 UTC.
  - Zusatzauswertung (code/zusatz.py, nach den Laeufen geschrieben, nur berichtet, keine Urteile) 17:17:56 bis
    17:18:07 UTC.
- Plan und Code eingefroren 18:46:41 CEST (PLAN.md.eingefroren-20261003-184641, code/*.eingefroren-20261003-184641).
  - Das lief im selben Befehl unmittelbar vor dem Start des ersten echten Laufs: cp, chmod und rsync vor dem ssh-Start;
    der erste Lauf meldet 16:46:41 UTC.
  - Aenderungen nach dem Rauchlauf stehen offen in PLAN.md Abschnitt 6.
- Daten: lauf-69/ (Laufausgaben, auswertung.json mit den Urteilen, zusatz.json, auswertung.png), rauch-69/.
- Code: code/gitter.py, eis_kern.c, eis_mc.py, stabnetz.py, auswertung.py, laeufe.sh; nach den Laeufen zusatz.py und
  pruefsummen.py.
  Jeder Lauf schreibt die sha256 seines Skripts (und des C-Kerns) in seine Ausgabe.
- Geschrieben ab 18:54:23 CEST (date), fertiggestellt ab 19:20:00 CEST.
- Einheiten: Kantenlaenge der kubischen Zelle = 1. Pyrochlor-Stab sqrt(2)/4 = 0,354; fcc-Stab sqrt(2)/2 = 0,707;
  Abstand benachbarter Tetraedermitten 0,433. Spin-Eis: F in Einheiten von T. Stabnetze: k = 1, Fehlpass delta = 1.

## Ergebnis zuerst

1. **Spin-Eis (Zaehlregel): entropisches Coulomb, wie in der Literatur.**
   - Bei L = 12: F(r) = a - C r^(-p) mit p = 0,950 (Jackknife +-0,034) und C = 0,159 (+-0,004), anziehend.
   - Die Gauss-Gegenprobe (Gitter-Coulomb auf demselben Torus) gibt im selben Ausgleich p = 0,999 und C = 0,157.
   - Das Monte-Carlo folgt ihr Schale fuer Schale: F_MC = alpha + 0,987 F_G, chi^2 = 3,4 bei 16 Schalen
     (nachtraeglich, zusatz.py).
2. **Pyrochlor-Stabnetz (Kraftregel, isostatisch): Die Kraft eines Fehlpasses laeuft ungedaempft auf genau einer
   geraden Linie, sonst ist sie null.**
   - Alle 4 L Staebe der [011]-Linie durch den Fehlpass-Stab tragen -delta/(4 L) (L = 12: -0,020833; L = 8: -0,03125).
   - Alle anderen Staebe tragen <= 1,1e-15. Exponent entlang der Linie 0,000; in den sechs anderen Kegelgruppen keine
     Kraft ueber der Schwelle.
   - Die Eigenspannungen sind genau die 12 L^2 geraden <110>-Linien: 108, 192, 300 bei L = 3, 4, 5 (dicht), 768 und
     1728 bei L = 8 und 12 (Bloch). Dazu ebenso viele Nullmoden.
3. **Diese Linienkraft verschwindet in grossen Netzen.**
   - Sie faellt mit 1/L, die Energie ist delta^2/(8 L).
   - Ein zweiter Fehlpass spuert den ersten nur auf derselben Linie, dort unabhaengig vom Abstand (delta^2/(4 L)).
   - Eine Fernwirkung in alle Richtungen, wie im Spin-Eis, entsteht nicht.
4. **Steifes Tetraeder-Oktaeder-Netz: Der Fehlpass-Stab traegt -0,500, und die Kraft faellt in [1; 3] langsamer als
   erwartet.**
   - Die Kugel-Huellkurve faellt dort nur mit dem Exponenten 1,74, nicht 3.
   - Von ihren 8 Punkten liegen 3 auf der geraden Stabkette durch den Fehlpass-Stab, die anderen 5 abseits. Beide
     Familien zusammen geben 1,74; die Kette allein faellt mit 2,9, die Staebe abseits mit 2,1 (nachtraeglich,
     zusatz.py).
   - Das Kugelmittel (quadratisch) faellt mit 2,7 in [1; 3] und 2,9 in [3; 5,5] (der zweite Wert nachtraeglich).
5. **Vorab:** E0 eingetroffen, E1 nicht eingetroffen, E2 eingetroffen, E3 eingetroffen.

## Vorab gegen Ausgang

Mechanisch nach PLAN.md (eingefroren 18:46:41 CEST). Die Urteile stehen in lauf-69/auswertung.json.

| Nr | Vorhersage | Wahrsch. | Ausgang |
|---|---|---|---|
| E0 | Spin-Eis: F(r) ist anziehend, und der beste Exponent p liegt in [0,8; 1,2] (Coulomb); Kontrolle aus der Literatur | 80 % | **eingetroffen**: L = 12, Bereich [1,15; 2,28] (16 Schalen), C = 0,1586 > 0, p = 0,950 (Jackknife +-0,034). Seeds einzeln 0,933 / 0,927 / 0,961 / 0,977 |
| E1 | Steifes Tetraeder-Oktaeder-Netz: Stabkraft eines Fehlpasses faellt mit Exponent in [2,5; 3,5] (Elastizitaet, Dipol) | 75 % | **nicht eingetroffen**: Kugel-Huellkurve bei L = 12 in [1; 3] (8 Klassen): Exponent 1,739 (Streuung in ln 0,52). Bei L = 8: 1,61 |
| E2 | Isostatisches Pyrochlor-Netz: in mindestens einer Gitterrichtung faellt die Stabkraft mit Exponent <= 1,5, also deutlich langsamer als im steifen Netz | 55 % | **eingetroffen**: L = 12, Kegel 110_par (entlang des Fehlpass-Stabs): Exponent 0,000 (6 Klassen, alle \|t\| = 0,020833). Alle anderen Kegelgruppen: keine Kraft ueber 1e-9 |
| E3 | Pyrochlor-Netz: Die Zahl der Eigenspannungen waechst mit der Gittergroesse (ausgedehnte Eigenspannungen, wie bei RUM-Gittern), statt konstant zu bleiben | 60 % | **eingetroffen**: 108, 192, 300 bei L = 3, 4, 5 (dichte SVD), also 12 L^2 |

**Bedeutung (vorab festgelegt) und was davon ausgeloest ist:**
- Fall "E0, E1 und E2 treffen ein": **nicht ausgeloest**, weil E1 nicht eingetroffen ist.
  - Beschreibend gilt der erste Teil: Die Zaehlregel ergibt Coulomb (E0).
  - "Eine Kraftregel im isostatischen Netz traegt weit" gilt nur eingeschraenkt: ungedaempft, aber nur auf einer Linie
    und mit einer Kraft, die mit 1/L verschwindet (Punkt 3 oben).
  - "Im steifen nicht" gilt beschreibend auch: Die Kraft faellt, im Kugelmittel weiter aussen fast wie 1/r^3. Nach
    der Regel E1 ist das aber nicht ausgeloest. Das ist eine Beschreibung, keine ausgeloeste Bedeutung.
- Fall "E2 trifft nicht ein": nicht ausgeloest.
- Fall "E0 trifft nicht ein (Werkzeug fehlerhaft)": nicht ausgeloest. Das Werkzeug ist auch unabhaengig geprueft: 0
  Eisregel-Fehler, Gauss-Gegenprobe mit beta = 0,987.

## Lesart [H] (nachtraeglich, ausser dem Schreibtisch in PLAN.md Abschnitt 5)

- **Warum gleiche Ecken so verschiedene Reichweiten geben** (Abzaehlen je Wellenvektor [M]; wo die Eigenspannungen
  liegen, zeigen die Bloch-Zaehlungen und die Antwort [E]):
  - Spin-Eis: Je primitiver Zelle gibt es 4 Spins (Fluesse) und 2 skalare Regeln (je Tetraeder eine). Bei jedem
    Wellenvektor bleiben also 2 freie Flussmoden. Das ist ein divergenzfreies 3D-Feld, also Magnetostatik, und
    Defekte spueren 1/r.
  - Pyrochlor-Stabnetz: 12 Stabkraefte gegen 12 Gleichgewichtsgleichungen (3 je Knoten, 4 Knoten). Bei einem
    allgemeinen Wellenvektor bleibt keine freie Spannung. Nur auf den sechs Ebenen q . n = 0 (n eine <110>-Richtung)
    bleibt je eine; das sind genau die geraden Linien. Es gibt also kein 3D-Kraftfeld, nur Linien.
  - fcc-Netz: 6 Stabkraefte gegen 3 Gleichungen je Knoten, also 3 freie Spannungsmoden bei jedem Wellenvektor. Die
    Antwort legt dann die Vertraeglichkeit fest (elastische Green-Funktion, Fernfeld 1/r^3).
- **Die Linienkraft ist ein Rand- bzw. Torus-Effekt:**
  - Auf dem Torus schliesst sich die Linie; ihre Gesamtlaenge darf sich nicht aendern. Darum steht sie unter
    gleichmaessigem Druck delta/(4 L).
  - In einem offenen oder unendlichen Netz waere ein einzelner Fehlpass spannungsfrei; die 12 L^2 Nullmoden
    (Mechanismen) nehmen ihn auf. Das ist abgeleitet, nicht gerechnet.
  - Zwei Fehlpaesse auf derselben Linie wirken wie Ladungen mit einer Summenregel: Energie (delta_1 + delta_2)^2/(8 L).
    Entgegengesetzte heben sich auf, unabhaengig vom Abstand. Das ist kein 1D-Coulomb (das wuechse linear mit dem
    Abstand).
- **Fuer die "Tetraeder-Ursuppe":** Die Karte vermutete, Fernwirkung brauche Regeln, die das Gleichgewicht allein
  festlegen (isostatisch) oder zaehlen. Nach EIS-1 genauer:
  - Gleichgewicht allein gibt auf diesem Gitter keine Fernwirkung in alle Richtungen, nur Linien mit Kraft ~1/L.
  - Ein 1/r-Gesetz in 3D kommt nur aus der Zaehlregel (Erhaltung je Tetraeder). Das stuetzt TETRAEDER-ANALYSE
    Abschnitt 4.2.
- **Bekannte Gegenstuecke [L?, nicht nachgelesen]:**
  - Das Pyrochlor-Stabnetz ist das 3D-Gegenstueck des Kagome-Gitters. Dort tragen gerade Linien Eigenspannungen und
    Nullmoden (Sun, Souslov, Mao, Lubensky 2012).
  - Seine Nullmoden sind die "rigid unit modes" von beta-Cristobalit, die auf Ebenen (xi, xi, zeta) liegen (Hammonds,
    Dove, Giddy, Heine, Winkler 1996).
  - Das steife Netz ist Gitter-Elastizitaet, und 2D-Elastizitaet ist dual zu einer Tensor-Eichtheorie mit Fraktonen
    (Pretko, Radzihovsky 2018). Das waere eine Spur zu TETRAEDER-ANALYSE Abschnitt 3.2, hier nicht geprueft.
- **Warum das fcc-Netz im Bereich [1; 3] langsamer faellt:**
  - Bis r = 3 sind es nur gut 4 Stablaengen, also Nahfeld.
  - Die Kette durch den Fehlpass-Stab traegt dort die groessten Kraefte (0,049 bei 1,41 gegen 0,013 bei 1,22 abseits).
  - Die Klassen wechseln zwischen Kettenstab und Nicht-Kettenstab. Das gibt ein Zickzack und flacht die Huellkurve ab.
  - In schmalen Kegeln wechseln dazu Achsenstaebe nahe einer Knotenrichtung (1e-5) mit Nachbarn neben der Achse
    (1e-3). Daher die Kegel-Exponenten von -3,0 bis 3,8 (Tabelle).

## Tabellen

**Spin-Eis (Ausgleich a - C r^(-p), Gewichte 1/sigma_F^2):**

| L | Laeufe, Schritte | Bereich (Schalen) | p | C | chi^2 / Freiheitsgrade | Gauss: p, C | ab 0,8 (nur berichtet): p MC / Gauss | beta (Zusatz) |
|---|---|---|---|---|---|---|---|---|
| 12 | 4 Seeds, 167 Bloecke, 8,4e10 | [1,15; 2,28] (16) | **0,950** +-0,034 | 0,1586 +-0,0036 | 47,8 / 13 | 0,999; 0,1567 | 0,855 / 0,847 | 0,987 (chi^2 3,4) |
| 8 | 2 Seeds, 91 Bloecke, 4,6e10 | [1,15; 1,52] (4) | 2,90 +-0,46 | 0,090 | 52,1 / 1 | 2,75; 0,093 | 0,588 / 0,488 | 0,978 (chi^2 0,2) |

- Das Gauss-chi^2 (56,1 bei L = 12 mit denselben Gewichten) zeigt: Der chi^2-Ueberschuss des Monte-Carlo ist
  Gitterstruktur, keine Statistik.
- Bei L = 8 bleiben im eingefrorenen Bereich nur 4 Schalen (1 Freiheitsgrad); der Exponent ist dort nicht
  bestimmbar. Monte-Carlo und Gauss-Gegenprobe liegen trotzdem gleich (2,90 gegen 2,75; beta = 0,978).

Auswahl F(r) (Monte-Carlo, F = 0 bei Gleichverteilung) und Gauss-Gegenprobe F_G = 2 [G(0) - G(r)]:

| r | 0,433 | 0,707 | 1,0 | 1,225 | 1,414 | 1,732 | 2,0 | 2,278 | 3,0 |
|---|---|---|---|---|---|---|---|---|---|
| F, L = 12 (+-0,0002 bis 0,0006) | -0,332 | -0,188 | -0,115 | -0,092 | -0,076 | -0,055 | -0,042 | -0,033 | -0,017 |
| F_G, L = 12 | 0,500 | 0,667 | 0,743 | 0,766 | 0,782 | 0,804 | 0,817 | 0,826 | 0,842 |
| F, L = 8 (+-0,0002 bis 0,0004) | -0,313 | -0,170 | -0,097 | -0,074 | -0,058 | -0,038 | -0,025 | | |

- F_MC - F_G ist von 1,0 bis 3,0 konstant auf +-0,001 (-0,857 bis -0,859); bei 0,707 -0,855, bei 0,433 -0,832.
- Bei Beruehrung (0,433) ist die Anziehung 0,37 T stark (gegen a = 0,040).

**Stabnetze, Exponenten (minus Steigung von log max\|t\| gegen log r, Klassen mit Mitte in [1; L/4]):**

| Gruppe (Winkel zum Fehlpass-Stab) | Pyrochlor L = 12 | Pyrochlor L = 8 | fcc L = 12 | fcc L = 8 |
|---|---|---|---|---|
| Kugel, Maximum (E1-Regel) | 0,000 (6) | 0,000 (3) | **1,74** (8; 0,52) | 1,61 (4; 0,61) |
| Kugel, quadratisches Mittel | 1,00 (6) | 1,07 (3) | 2,69 (8) | 1,95 (4) |
| 110_par (0 Grad) | **0,000** (6) | 0,000 (3) | 3,83 (6; 0,65) | < 3 Klassen |
| 110_senk (90) | keine Kraft | keine Kraft | 3,78 (6; 0,73) | < 3 Klassen |
| 110_60 (60) | keine Kraft | keine Kraft | 2,09 (7; 0,27) | 0,90 (3; 0,16) |
| 100_senk (90) | keine Kraft | keine Kraft | -0,50 (7; 1,06) | -3,43 (3; 0,74) |
| 100_45 (45) | keine Kraft | keine Kraft | -2,96 (7; 1,56) | -3,69 (3; 0,15) |
| 111_35 (35,3) | keine Kraft | keine Kraft | 0,29 (6; 0,69) | < 3 Klassen |
| 111_90 (90) | keine Kraft | keine Kraft | 1,85 (6; 0,66) | < 3 Klassen |

- In Klammern: Zahl der Klassen; Streuung um die Gerade in ln.
- "keine Kraft": kein Stab ueber 1e-9.
- Das Kugelmittel des Pyrochlor-Netzes faellt wie 1/r nur, weil ein Linienstab je Klasse auf ~r^2 Staebe verteilt
  wird.

**Nur berichtet (zusatz.py, nach den Laeufen), fcc L = 12:**

| Groesse | [1; 3] | [3; 5,5] |
|---|---|---|
| Kette durch den Fehlpass-Stab | 2,88 | 3,16 |
| Kugel, quadratisches Mittel | 2,69 | 2,94 |
| Kugel, Maximum | 1,74 | 2,24 |
| Kugel, Maximum ohne die Kette | 2,11 | 2,14 |

- Kraefte entlang der Kette (r: t): 0: -0,500; 0,707: -0,169; 1,414: -0,0495; 2,121: -0,0166; 2,828: -0,0067;
  3,536: -0,0032; 4,243: -0,0018; 4,950: -0,0011; 5,657: -0,00076. Bei L = 8 bis 2,8 gleich auf 3 %, bei 3,5 auf
  7 %.
- Groesste Kraft abseits der Kette: 0,094.

**Zusatz der Karte (zwei Fehlpaesse, nur berichtet):** Die Wechselwirkungsenergie zweier Fehlpaesse in b0 und b ist
delta^2 P(b, b0) = -delta t_b. Ihr Verlauf mit dem Abstand ist also der der Stabkraefte oben. Je Netz und Groesse mit
einem zweiten Fehlpass nachgerechnet (zusatz.py):
- Pyrochlor: delta^2/(4 L) fuer jeden zweiten Fehlpass auf derselben Linie (L = 12: 0,020833 bei r = 1,06), sonst
  <= 1,1e-15. Einzelenergie delta^2/(8 L).
- fcc: 0,0223 bei r = 1,27 (staerkster Stab abseits der Kette), Einzelenergie 0,250.

**Eigenspannungen (Staebe minus Rang) und Nullmoden:**

| L | Pyrochlor dicht | Pyrochlor Bloch | 12 L^2 | Nullmoden | kleinster Singulaerwert != 0 | fcc dicht / Bloch | 12 L^3 + 3 | fcc-Nullmoden |
|---|---|---|---|---|---|---|---|---|
| 3 | 108 | 108 | 108 | 108 | 0,366 | 327 / 327 | 327 | 3 |
| 4 | 192 | 192 | 192 | 192 | 0,276 | 771 / 771 | 771 | 3 |
| 5 | 300 | 300 | 300 | 300 | 0,221 | 1503 / 1503 | 1503 | 3 |
| 8 | | 768 | 768 | 768 | 0,139 | / 6147 | 6147 | 3 |
| 12 | | 1728 | 1728 | 1728 | 0,0925 | / 20739 | 20739 | 3 |

- Groesster als null gezaehlter Singulaerwert <= 3,6e-15, kleinster anderer >= 0,0925: Die Rangzaehlung haengt nicht
  an der Schwelle.
- Der kleinste Nicht-Null-Wert des Pyrochlor-Netzes faellt wie ~1,1/L (weiche Moden neben den Nullmoden-Ebenen).
- Beim fcc-Netz ist er 2 sin(pi/(2L)), also die akustischen Moden.

## Kontrollen

- **Spin-Eis:**
  - Gitter in jedem Lauf: 16 L^3 Ecken, 8 L^3 Tetraeder je 4 Ecken, 48 L^3 Kanten (Laenge^2 = 8/64), 6 Nachbarn je Ecke.
    Jede Mitte ist der Schwerpunkt ihrer Ecken.
  - Eisregel nach jedem Zug (verlassenes Tetraeder 0, neues +-1): 0 Fehler in 1,41e11 Zuegen der sechs gewerteten
    Laeufe (Einlauf und Messung).
  - Nach jedem der 258 Bloecke alle Tetraeder geprueft: genau ein +1 und ein -1 an den gefuehrten Orten, nie \|Q\| = 2.
  - Ablehnung wegen Orientierung 0,250 (Soll 1/4, bei L = 12: 0,2499990). Das bestaetigt: immer genau 3 waehlbare
    Spins, keine Metropolis-Korrektur noetig.
  - Ablehnung wegen Vernichtung 9,1e-5 (L = 12) und 3,0e-4 (L = 8); das Verhaeltnis 3,3 passt zum Volumen
    (12/8)^3 = 3,4.
  - Gegentypen: +1-Defekt auf oberen Tetraedern 0,499994, -1-Defekt 0,500000, gleiche Art 0,49994. Mit der
    rein/raus-Konvention lebt jeder Defekt auf beiden Arten und wechselt sie bei jedem Sprung. Mit der ungestaffelten
    Ising-Summe saehe derselbe Defekt auf oberen Tetraedern wie +1 und auf unteren wie -1 aus.
  - Einlauf: Gesamtmoment vom polarisierten Anfang 15961 (L = 12) bzw. 4728 (L = 8) schon nach 1e8 Schritten auf
    47 bis 176 (L = 12) bzw. 118 und 131 (L = 8), danach Schwankungen bis 460 bzw. 210. Der Einlauf war 2e9 Schritte,
    also mehr als 20-fache Reserve.
  - Seeds (L = 12): p = 0,927 bis 0,977, C = 0,156 bis 0,162. Erste gegen zweite Haelfte je Seed: groesste Abweichung
    in F 0,0011 bis 0,0022 (L = 8: 0,0004 und 0,0007).
  - Endlichkeit: F(r) bei L = 8 und 12 folgt jeweils der Gauss-Gegenprobe auf derselben Groesse (beta = 0,978 und
    0,987).
  - Geschwindigkeit 4,3e7 (L = 12) bzw. 4,6e7 (L = 8) Schritte/s auf einem Kern.
- **Code-Stand:** code/pruefsummen.py (nach den Laeufen, ueber die Spur cpu, 17:22:53 bis 17:25:51 UTC, davon ~3 min
  Warten auf die Spur). Die eingefrorenen Kopien haben dieselbe sha256 wie die in den Laufausgaben vermerkten Skripte:
  eis_mc.py 47d83c9d..., eis_kern.c 5966ab49..., stabnetz.py ccc95f4e..., auswertung.py 36c0ee47.... gitter.py auf der
  .69 = eingefrorene Kopie (9f6b4b1c...).
- **Stabnetze:**
  - Gitterzahlen wie oben; fcc: 12 Nachbarn je Knoten, keine doppelten Staebe.
  - Gleichgewicht der Kraefte max \|C^T t\| <= 2,6e-15. lsqr (istop = 2) gegen Bloch-Projektion <= 1,2e-15.
  - Eigenspannungen dicht = Bloch bei L = 3, 4, 5 (beide Netze).
  - Reziprozitaet (Zusatz): Wechselwirkungsenergie zweier Fehlpaesse = -delta t_b auf <= 6e-16 (vier Faelle).
  - Endlichkeit: Pyrochlor exakt -delta/(4 L) bei L = 8 und 12; fcc-Kraefte bei L = 8 und 12 bis r = 2,8 gleich auf
    3 %, bei 3,5 auf 7 %.

## Latten (v3)

- L1: ja. E1 ist gescheitert. E0 haette am Exponenten scheitern koennen, E2 an fehlender Kraft, E3 an einer konstanten
  Zahl.
- L2: ja.
  - Gauss-Gegenprobe beim Spin-Eis; lsqr gegen Bloch; dicht gegen Bloch; Reziprozitaet.
  - Der Schreibtisch vor den Laeufen traf: C ~ 0,16 (gemessen 0,159), genau 12 L^2 Eigenspannungen, genau
    -delta/(4 L) auf der Linie, genau 12 L^3 + 3 beim fcc-Netz, Fehlpass-Stab ~ -delta/2 (-0,50007).
- L3: ja.
  - Zwei Groessen je Teil, vier bzw. zwei Seeds, Haelften, Gleichgewicht auf 1e-15.
  - Schwach: Die L = 8-Kontrolle des Spin-Eis-Exponenten ist im eingefrorenen Bereich nicht bestimmbar.
- L4: weitgehend bekannt.
  - Entropisches Coulomb der Eis-Defekte (Henley [S]).
  - Kraefte entlang von Linien bzw. Strahlen in isostatischen Packungen (Moukarzel, Tkachenko/Witten [S]).
  - Gerade Linien als Eigenspannungen im Kagome-Gitter, RUM-Ebenen in beta-Cristobalit [L?].
  - Neu fuer das Projekt ist der direkte Vergleich auf demselben Gitter und die exakte Linienkraft -delta/(4 L).
    Vermutlich ist auch das bekannt; ich habe nicht danach gesucht.
- L5: Spin-Eis ja, aus der Literatur (Monopole, Neutronenstreuung). Mechanisch machbar, nicht gemacht: ein Pyrochlor-
  Modell aus gleichen Staeben mit einem zu langen Stab. Vorhersage [H]:
  - Mit freiem Rand ist es spannungsfrei; das Netz weicht ueber Mechanismen aus.
  - Mit festgehaltenen Linienenden steht nur die eine gerade Linie unter Druck.

## Literatur

- [S] C. Castelnovo, R. Moessner, S. L. Sondhi, Nature 451, 42 (2008), arXiv:0710.5515 (Abstract ueber die arXiv-API,
  18:49 CEST): Monopole entstehen im Spin-Eis ("the dipole moment of the underlying electronic degrees of freedom
  fractionalises into monopoles"). Das Coulomb-Gesetz steht nicht im Abstract; im Text ist es nach meiner
  Erinnerung das energetische aus der Dipolwechselwirkung [L?].
- [S] C. L. Henley, "The 'Coulomb phase' in frustrated systems", Annu. Rev. Condens. Matter Phys. (2010),
  doi:10.1146/annurev-conmatphys-070909-104138, arXiv:0912.4531: "defects at which the local constraint is violated
  behave as effective charges with Coulomb interactions".
- [S] C. F. Moukarzel, Phys. Rev. Lett. 81, 1634 (1998), cond-mat/9803120: "Isostaticity is responsible for the
  anomalously large susceptibility to perturbation of these systems"; "The load-stress response function of granular
  materials is critical (power-law distributed) in the isostatic limit".
- [S] A. V. Tkachenko, T. A. Witten, Phys. Rev. E 60, 687 (1999), cond-mat/9811171: "the transmission of force may be
  regarded as unidirectional, in contrast to the transmission of force in an elastic material"; "In two dimensions,
  the stress propagates according to a wave equation".
- [S] dieselben, Phys. Rev. E 62, 2510 (2000), cond-mat/9910250 (nur Abstract-Satz aus derselben Suche): "The response
  to a local perturbing force is concentrated along two characteristic rays".
- [L?] Isakov, Gregor, Moessner, Sondhi, PRL 93, 167204 (2004); Sun, Souslov, Mao, Lubensky, PNAS 109, 12369 (2012);
  Hammonds, Dove, Giddy, Heine, Winkler, Am. Mineral. 81, 1057 (1996); Pretko, Radzihovsky, PRL 120, 195301 (2018).
  Alle aus dem Gedaechtnis, nicht nachgeprueft.

## Selbstanzeigen

- **Untergrenze des E0-Bereichs nach dem Rauchlauf geaendert (0,8 -> 1,15),** vor dem Einfrieren, offen in PLAN.md 6.
  - Grund: Gitterkern bis zur Schale 1,09, in Monte-Carlo und Gauss-Gegenprobe bei L = 6 gleich.
  - Mit der alten Grenze waere E0 ebenfalls eingetroffen (p = 0,855), naeher am Rand.
- **L = 12 mit vier statt zwei Seeds** (nach dem Rauchlauf, vor dem Einfrieren).
- **E1-Regel trotz Zickzack im Rauchlauf beibehalten.**
  - Den Zickzack der fcc-Huellkurve habe ich bei L = 6 gesehen und die Regel nicht geaendert (PLAN.md 6).
  - Der eingefrorene Bereich [1; L/4] liegt fuer das fcc-Netz im Nahfeld. Das Urteil folgt der Regel.
  - Die Zahlen fuer [3; 5,5] und ohne Kette sind nachtraeglich (zusatz.py) und nur berichtet.
- **Die L = 8-Kontrolle des Spin-Eis-Exponenten taugt nicht.** Dass bei [1,15; 0,19 L] nur 4 Schalen bleiben, habe
  ich beim Aendern der Untergrenze uebersehen. Die Endlichkeitskontrolle ist deshalb nur der Vergleich mit der
  Gauss-Gegenprobe (beta = 0,978), nicht der Exponent.
- **E2 und die Kegel-Exponenten:**
  - E2 ist nach der Regel eingetroffen.
  - Mit demselben Mass zeigt auch das steife Netz in drei Kegelgruppen Exponenten <= 1,5, zwei davon negativ. Das ist
    Nahfeld mit Knotenrichtungen und wenigen Staeben je Kegel und Klasse, keine Reichweite.
  - "Deutlich langsamer als im steifen Netz" gilt robust nur so: Pyrochlor konstant auf einer Linie und sonst null;
    fcc ueberall ungleich null, im Kugelmittel mit 2,7 bis 2,9 fallend.
- **Spur cpu2 auf Bitte der Koordination freigegeben:**
  - Um 17:07:45 UTC habe ich laeufe.sh (Hauptprozess und cpu2-Zweig, je per PID) beendet.
  - Den Lauf eis_L8_s2 auf cpu2 habe ich nach 33 s per systemctl --user stop gestoppt. Er hatte keine Ausgabe
    geschrieben; das Log liegt als eis_L8_s2.abgebrochen-cpu2.log.
  - Wiederholt auf cpu3 mit gleichen Argumenten und gleichem Seed, 17:08:09 bis 17:16:58 UTC.
  - Die Auswertung habe ich danach von Hand auf cpu gestartet, mit den Argumenten aus laeufe.sh.
  - Die Nachricht sah ich um ~17:07 UTC. Ob eis_L8_s2 (Start 17:07:13 durch die Lauffolge) vor oder nach ihr begann,
    weiss ich nicht. Ich habe ihn als "weiteren Lauf auf cpu2" behandelt, obwohl die Bitte auch "laufende Jobs nicht
    abbrechen" sagte.
- Einfrieren und Start des ersten Laufs liegen in derselben Sekunde (Reihenfolge im Befehl gesichert, siehe Kopf).
- Die Gauss-Gegenprobe nimmt die Steifigkeit K' = 1/2 an. Gewertet wird nur ihre Form; ihre Staerke trifft das
  Monte-Carlo trotzdem auf 1,3 %.
- Die Ergodizitaet der Defektwanderung ist nur indirekt geprueft: Momentabbau, Seeds, Haelften, Gegenprobe.
- Der Jackknife-Fehler von p (0,034) enthaelt nur Statistik. Die Gitterstruktur (chi^2/Freiheitsgrad 3,7) steckt
  ebenso in der Gegenprobe (p = 0,999).
- Alles linear: kein Knicken der gedrueckten Linie, keine Nichtlinearitaet.
- Bild lauf-69/auswertung.png: Die L = 8-Kurve links ist um ihr eigenes a aus dem entarteten Ausgleich verschoben;
  rechts ueberlappen die Achsenbeschriftungen. Nur zur Ansicht.

## Einfach gesagt

Wir haben dasselbe Gitter aus Ecke an Ecke verbundenen Dreieckspyramiden (Tetraedern) zweimal benutzt. Als "Spin-Eis"
gilt in jedem Tetraeder eine Zaehlregel: zwei Pfeile rein, zwei raus. Zwei Regelverstoesse ziehen sich dann an wie
elektrische Ladungen, mit einer Kraft, die langsam mit dem Abstand abnimmt, genau wie in der Fachliteratur. Baut man
dasselbe Gitter aus gleich langen Staeben und macht einen Stab etwas zu lang, steht nur die eine gerade Stablinie
unter Druck, auf der er liegt; dort ueberall gleich stark, und umso schwaecher, je groesser das ganze Geruest ist,
waehrend alle anderen Staebe entspannt bleiben. Eine Kraft, die in alle Richtungen weit reicht, entsteht hier also nur
aus der Zaehlregel, nicht aus den Staeben.
