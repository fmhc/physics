# TETRA-STAB und TETRA-KIPP: Ergebnis (Leitung, Runde 24, explorativ)

- Gerechnet von der Leitung auf der .69 (kleintest.sh, CPU-Spuren):
  - zehn TETRA-STAB-Laeufe 23:52 bis 00:03 UTC (01:52 bis 02:03 CEST)
  - fuenf TETRA-KIPP-Laeufe 00:04 bis 00:11 UTC
  - alle rc = 0, Gradient am Ende <= 1,8e-9
- Karte und Code eingefroren 01:52:34; Zusatzkarte KIPP eingefroren 02:04:26 (Code unveraendert).
- Auswertung mit jq auf lauf-69/. Geschrieben ab 02:12:01 CEST (date).
- Einheiten im Modell: Biegesteifigkeit B = 1, Stablaenge L = 1. Kraefte in B/L^2, Momente in B/L.

## Ergebnis zuerst

1. **Im symmetrischen Fall tragen die Kontaktpunkte nur Biegemomente, keine Kraefte.**
   - Jeder Stab wird ein Kreisbogen nach innen mit konstantem Moment tau = 2 B alpha/L (bei 5 Grad: 0,17453; Soll
     0,17453).
   - Die Kraefte sind praktisch null (<= 8e-11).
   - An jeder Ecke heben sich die drei Momente auf (Rest <= 4e-13).
   - Die Kantenlaenge folgt a = (L/alpha) sin alpha auf 3e-6.
   - Das gilt bis 35 Grad (Abweichung des Moments <= 6e-4).
2. **Ein einzelner staerker gebogener Stab (AB mit 10 statt 5 Grad) erzeugt Kraefte an allen Kontaktpunkten.**
   - AB steht dann unter **Zug** (+0,30 B/L^2) und traegt das groesste Moment (0,315, +81 %).
   - Die vier Nachbarstaebe stehen unter **Druck** (-0,091) mit Querkraft. Ihre Endmomente sind ungleich: 0,232 an A und B,
     0,143 an C und D.
   - Der Gegenstab CD steht wieder unter Zug (+0,066), sein Moment steigt nur um 4,5 % (0,1824 gegen 0,1745).
   - Es entsteht ein in sich geschlossenes Muster aus Zug und Druck, aehnlich einer Tensegrity-Vorspannung.
3. **Stabilitaet:** Der kleinste Eigenwert der Hesse-Matrix faellt mit der Neigung: 0,153 (5 Grad), 0,082 (20), 0,054
   (25), 0,027 (30), 0,0013 (35). Bei 40 Grad ist er negativ, mehrere Richtungen sind dann instabil.
   - Das symmetrische Tetraeder kippt also bei etwa **35 Grad** Einspannneigung (Nullstelle linear ~35,3 Grad).
   - Der Stich der Boegen betraegt dort 15 % der Stablaenge.
4. **In echten Groessen** (Knicklicht 20 cm lang, 5 mm dick, als voller LDPE-Stab angenommen, E ~ 0,25 GPa, B ~ 7,7e-3
   N m^2; Groessenordnung, echte Knicklichter sind hohl):

| Fall | Moment am Kontaktpunkt | Biegespannung dort | Kraft |
|---|---|---|---|
| 5 Grad symmetrisch | 6,7 N mm | 0,55 MPa | 0 |
| 20 Grad symmetrisch | 27 N mm | 2,2 MPa | 0 |
| 35 Grad (Kippgrenze) | 47 N mm | 3,8 MPa | 0 |
| Defekt AB 10 Grad | bis 12 N mm (AB) | bis 1,0 MPa | Zug AB 0,057 N, Druck Nachbarn 0,017 N |

   - Die Spannungen liegen deutlich unter der Fliessgrenze von Polyethylen (~10 MPa).
   - Die Kraefte sind winzig (Gramm-Bereich); die Last steckt fast ganz in den Momenten.
5. **Lesart [H]:**
   - Das nach innen gebogene Tetraeder ist ein vorgespannter, kraftfreier Koerper. Seine Spannung sitzt als sich
     aufhebende Biegemomente in den Ecken, wie eine "neutrale" Winkelladung (vgl. WINKELFELD-1).
   - Ein Defekt ist dagegen eine Quelle: Seine Vorspannung verteilt sich als Zug-Druck-Muster ueber den ganzen Koerper.

## Vorab gegen Ausgang

| Nr | Vorhersage | Ausgang |
|---|---|---|
| TE0 | alpha = 0 spannungsfrei, alle |tau|, |F| L < 1e-7 | **eingetroffen**: tau <= 3,6e-14, F <= 5,3e-11 |
| TE1 | 5 Grad: tau = 2 B alpha/L auf 1 %, |F| L < 1e-3 tau, Netto-Moment < 1e-5 tau, a auf 1e-3 | **eingetroffen** bei N = 20 und 40: tau -1,2e-5 bzw. -3e-7 relativ, F <= 3,6e-11, Netto <= 3,7e-13, a +3,2e-6 |
| TE2 | 20 Grad: dieselben Beziehungen auf 2 % | **eingetroffen**: tau -2,0e-4 (N = 20) bzw. -5e-5 (N = 40), a +5e-5 |
| TE3 (i) | groesstes Endmoment an AB | **eingetroffen**: 0,3153 |
| TE3 (ii) | an allen Kontaktpunkten |F| L >= 1e-3 tau_AB | **eingetroffen**: kleinste Kraft 0,066 (CD) >> 3e-4 |
| TE3 (iii) | Moment von CD aendert sich < 20 % | **eingetroffen**: +4,5 % |
| TE4 | Hesse-Matrix bei 5 und 20 Grad positiv definit | **eingetroffen**: kleinste Eigenwerte 0,153 bzw. 0,082 |
| TK1 | Vorzeichenwechsel des kleinsten Eigenwerts zwischen 25 und 40 Grad | **eingetroffen**: zwischen 35 (+0,0013) und 40 Grad (-0,296) |
| TK2 | Bogenbeziehungen bis zum Wechsel auf 1 % | **eingetroffen**: tau-Abweichung <= 6e-4 bis 35 Grad, F ~ 1e-11 |

**Bedeutung (vorab festgelegt):**
- TE1 und TE2: Das nach innen gebogene Tetraeder ist ein vorgespannter Koerper, dessen Kontaktpunkte nur Biegemomente
  tragen. Diese heben sich an jeder Ecke auf; der Koerper ist kraftfrei und "neutral".
- TE3: Ein einzelner Defektstab erzeugt Kraefte an allen Kontaktpunkten, die Spannung verteilt sich ueber das ganze
  Tetraeder.
- TE4: Leichte Vorspannung macht es nicht instabil.
- TK1: Leicht gebogene Knicklichter sind stabil; ab etwa 35 Grad Neigung kippt das symmetrische Tetraeder [H, ohne Torsion].

## Kontrollen

- Gleichgewicht: Kraft- und Momentensumme je Verbinder <= 1e-10. Die Reaktion am festen Verbinder A ist ebenso klein; das
  Gebilde ist in sich im Gleichgewicht.
- Gitterprobe N = 20 gegen 40: Defektfall auf ~1e-3 gleich, symmetrische Faelle auf 1e-4.
- Alle Boegen woelben sich nach innen (Stich nach innen 0,0218 bei 5 Grad = (1 - cos alpha) L/(2 alpha)).

## Latten (v3)

- L1: ja (jede Vorhersage konnte scheitern).
- L2: teilweise. TE1, TE2 und TK2 folgen aus der Elastica (Kreisbogen unter Endmomenten, [L]). Das Modell bestaetigt sie;
  neu sind Defektmuster und Kippgrenze.
- L3: ja (N = 20 und 40).
- L4: Elastica und eingespannte Rahmen sind Lehrbuchstoff. Fuer die Kippgrenze nicht gesucht (Websuche erschoepft).
- L5: nein.

## Selbstanzeigen

- Die Rauchlaeufe (alpha = 3 Grad; Defekt 3/6 Grad) zeigten das symmetrische Ergebnis und das Auftreten von Kraeften schon
  vor dem Einfrieren. Die Vorhersagen standen vorher fest.
- Die Diskretisierung wurde wegen der Laufzeit von N = 50/100 auf 20/40 geaendert, offen im Laufplan vor dem Einfrieren.
- Grenzen: keine Torsion (eine echte Kipp-Torsions-Instabilitaet fehlt), ideal starre Verbinder, kein Eigengewicht, keine
  Reibung. Die Knicklicht-Zahlen nehmen einen vollen Stab an.

## Einfach gesagt

Wir haben ein Tetraeder aus sechs biegsamen Staeben gebaut, deren Enden in den Ecken etwas nach innen geneigt eingespannt
sind, so dass sich jeder Stab zu einem kleinen Bogen nach innen biegt. Ueberraschend einfach: Jeder Stab wird ein
perfekter Kreisbogen, und an den Ecken druecken die Staebe nicht, sie verdrehen nur ein wenig. Diese Verdrehungen heben
sich an jeder Ecke genau auf. Biegt man einen einzigen Stab staerker, entsteht ein Muster aus Zug und Druck im ganzen
Tetraeder. Und ab etwa 35 Grad Neigung wird das Ganze wackelig und kippt in eine andere Form.
