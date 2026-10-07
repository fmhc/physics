# Z2-SCHUTZ-1: Wie gut schuetzt Finns Netz das Spin-Vorzeichen? (Runde 49, Vorschlag aus KRUEMMUNG-SPANNUNG-SPIN-L)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 12:48:27 CEST (date), vor jeder Rechnung.
- **Herkunft:**
  - Finn, 05.10.2026: "Könnte dann Krümmung zu Spin / Richtung werden" und "Oder eine Drehdimension dann quasi mit Spin".
  - Kartenvorschlag 6.1 aus KRUEMMUNG-SPANNUNG-SPIN-L (RUNDE-37/kruemmung-spannung-spin-l/DOSSIER.md), Vorhersagen woertlich. Zusaetze der Leitung sind markiert.
- **Projektbefunde [P]:**
  - GUERTEL-FINN-NETZ-1: Ein Einheitsquaternion-Feld (SU(2)) auf Finns Diamant-Netz legt 720 Grad stetig ab (Guertel-Trick), ein SO(2)-Feld nicht. Der Ast ueber 360 Grad ist ein Sattel, keine Rast; theta_max = 540 Grad.
  - TORSION-STEIF-1: 4 freie, kruemmungsfreie Rahmendrehungen je Zelle; sie tragen keine Z_2-Schleife (KRUEMMUNG-SPANNUNG-SPIN-L, Schreibtisch).
  - VIERTE-KOORDINATE-L: Eine Drehdimension gibt Spin nur bei Kopplung an die Raumdrehungen; bei der 600-Zelle ist ein halber Hopf-Umlauf eine volle Rahmendrehung.
  - Projektsuche (Barriere, NEB, "string method", Z2) in den Kartenordnern: nur fachfremde Treffer (RUNDE-16).
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Frage

Auf dem Diamant-Netz aus GUERTEL-FINN-NETZ-1 haelt man den Kern um 360 Grad verdreht fest. Wie hoch ist die kleinste Energiebarriere ins unverdrehte Feld? Waechst sie mit der Netzgroesse (topologischer Schutz) oder bleibt sie gleich (nur Energieschutz)?

## Ableitbarkeitsprobe (aus dem DOSSIER, von der Leitung nachgeprueft)

- **Vorab ableitbar [M, S, P]:**
  - Z_2-Schleifen gibt es fuer jedes SO(3)-Rahmennetz, pi_1(SO(3)^N) = (Z_2)^N [M].
  - Die 4 linearen Rahmen-Nullmoden tragen keine Z_2, weil R^4 zusammenziehbar ist [M].
  - Henkel und Linsenraeume sind nicht spinoriell (Giulini 2009, S. 28 [S]).
  - Der Weg 720 Grad -> 0 laeuft ohne Gittersprung (GF2 [P]).
  - Der Weg 360 Grad -> 0 braucht einen Gittersprung: Eine Bindung muss ueber omega = pi, die Sonde q_a . q_b wird <= 0. Die Bindungsenergie 4(1 - (q_a . q_b)^2) = 2(1 - cos omega) haengt nur von q_a . q_b ab [M; GUERTEL-PLAN].
  - Weil SO(3)^N zusammenhaengt und die Energie glatt ist, ist die Barriere endlich [M].
  - Groessenordnung: Eine Bindung bei omega = pi kostet 4 [ES].
  - **[Zusatz Leitung]:** Eine endliche Barriere je Bindung heisst: Auf einem Gitter ist das Spin-Vorzeichen hoechstens energetisch geschuetzt, solange kein Mechanismus Gittersprung verbietet. ZS2 (Barriere unabhaengig von der Groesse) ist damit naheliegend; offen ist, ob der kleinste Weg mehr als eine Bindung braucht.
- **Nicht vorab ableitbar:** die genaue Barriere auf dem kleinsten Energieweg, ihre Abhaengigkeit von Kugelradius und Kerngroesse, die Form des Sattels.

## Vorhersagen (vor jeder Rechnung, aus dem DOSSIER)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| ZS0 | Kontrolle: Der Wegrechner gibt fuer 420 -> -300 Grad einen monoton fallenden Weg ohne Sprung mit den GF2-Endenergien auf 1e-6 relativ | 85 % |
| ZS1 | [H] Die Barriere 360 -> 0 Grad liegt bei allen drei Kugelgroessen zwischen 2 und 8 (Energieeinheiten der Guertel-Energie) | 50 % |
| ZS2 | [H] Die Barriere aendert sich zwischen den drei Kugelgroessen um weniger als 20 % | 60 % |
| ZS3 | [H] Am Sattel liegen mehr als 50 % der Barrierenenergie in hoechstens 6 Bindungen | 50 % |

**Bedeutung (vorab, aus dem DOSSIER):**
- **ZS2 trifft ein:** Auf Finns Netz ist das Spin-Vorzeichen nur energetisch geschuetzt, unterhalb einer festen Energie je Bindung. Exakter halber Spin braucht dann eine Zusatzregel, die Gittersprung verbietet (Zulaessigkeit, Luescher-Typ [L]).
- **ZS2 scheitert (Barriere waechst):** Das Netz schuetzt die Z_2 kollektiv, und es entsteht ein echter topologischer Sektor.

## Kontrollen

- SO(2)-Feld als Gegenprobe (GF0 [P]: entdrillt nicht).
- Die Endpunkte muessen echte Minima sein (Hesse positiv bis auf Eichmoden).
- Zwei Wegverfahren (z. B. Nudged Elastic Band und String-Methode) muessen dieselbe Barriere auf 5 % geben.

## Rahmen

- Code-Agent. Code aus RUNDE-37/guertel-finn-netz-1/code kopieren, dort nichts aendern. Drei Kugelgroessen (im Plan, mindestens bis zur Groesse aus GUERTEL-FINN-NETZ-1).
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu und cpu7. Je Lauf hoechstens 10 min. Zeitbox 120 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
- Synthetisch (Modellfeld), keine Messdatenbestaetigung.
