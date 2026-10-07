# B-BALL-LEITER: Hat ein Q-Ball im flachen Log-Potential stille Stellen? (Runde 13, Vorschlag T3 aus X-BAELLE)

- Leitung: claude-primary. Karte, Regel und Vorhersage geschrieben ab 2026-10-01 19:06:50 CEST (date), vor jeder
  Codezeile und jedem Lauf.
- Herkunft: RUNDE-12/x-baelle/X-BAELLE.md, Abschnitt T3. Frage: Gilt die Leiter stiller Stellen fuer die ganze
  Q-Ball-Klasse, oder ist sie an das Sextik-Potential U = S - S^2 + S^3/2 gebunden?
- Datennaehe: Q-Baelle in flachen Richtungen supersymmetrischer Modelle (B-Baelle) sind Dunkle-Materie-Kandidaten mit
  Suchschranken (Super-K u. a.; X-BAELLE). Ein Messsignal ist dieser Test nicht, nur eine Klassenfrage.

## Modell

- Potential: flach, logarithmisch, U(S) = ln(1 + S) in Einheiten mit Vakuummasse 1 (U'(0) = 1). **Die genaue Form muss
  der Agent vor dem ersten Lauf an einer Primaerquelle pruefen** (arXiv-API oder INSPIRE nach Titel und Autor suchen,
  keine Nummer raten). Die Quelle (Gleichung, Seite) kommt in PLAN.md. Weicht die Literaturform ab (etwa
  M^4 ln(1 + |phi|^2/M^2) mit anderer Normierung), wird sie dimensionslos umgerechnet; die Rechnung bleibt dieselbe
  Klasse.
- Q-Baelle existieren fuer 0 < omega^2 < 1 (U(S)/S faellt von 1 gegen 0).
- Radiale Linearisierung l = 0 wie im 3D-Code fuer das Sextik-Modell (zwei Kanaele omega + rho und omega - rho,
  Schwelle 1), nur mit U'(S) und U''(S) des neuen Potentials.

## Schritt 0, Schreibtisch und kleiner Rechenschritt vor der Suche (bindend, Ergebnis in PLAN.md vor dem Einfrieren)

- Nackter geschlossener Kanal wie in RUNDE-10 bzw. AFM-KANAL-1: Hat er bei den gewaehlten omega einen gebundenen Zustand,
  der im Kontinuum des offenen Kanals liegt (1 - omega < rho < 1 + omega)?
- Gibt es keinen, ist "nicht gesehen" vorhersagbar. Dann wird der Test als Mechanismus-Bestaetigung gefuehrt, nicht als
  offene Frage, und das steht so im Bericht.

## Suche

- Drei omega^2-Baender, je mindestens 11 Zeilen: [0,30; 0,40], [0,50; 0,60], [0,70; 0,80].
- Je Zeile s(rho) bzw. die Nullstellen von L(y_b) mit feiner Abtastung (mindestens 4000 rho-Punkte im Fenster oder
  direkte Nullstellensuche), zwei Gitterstufen h und h/2. Umlauf-Rechtecke zwischen benachbarten Zeilen, aufgeloest
  heisst groesster Phasensprung < 0,4 rad.
- Der Agent darf die Baender vor dem Einfrieren verschieben, wenn Schritt 0 einen besseren Bereich nennt. Danach nicht
  mehr.

## Positivkontrolle (bindend)

- K1: Derselbe Code mit dem Sextik-Potential findet die bewiesene Stelle omega^2 = 0,797677, rho = 1,744618 auf 1e-4,
  Umlauf +-1 auf beiden Stufen. Verfehlt K1: nicht auswertbar.
- K2: Profil-Probe des Log-Balls. Ladung Q(omega) und Energie E(omega) auf zwei Gittern auf 1e-4 gleich.

## Regel (bindend)

- **Gesehen:** In mindestens einem Band ein aufgeloestes Rechteck mit Umlauf +-1 auf beiden Stufen, mit Vorzeichenwechsel
  von s, Lagen zwischen den Stufen auf 1e-3 gleich.
- **Nicht gesehen:** In keinem Band ein Vorzeichenwechsel von s, alle Rechtecke aufgeloest mit Umlauf 0, K1 bestanden.
- **Unentschieden:** alles andere.

## Vorhersage (Leitung, vor jedem Lauf)

- K1 besteht: ~85 %.
- Schritt 0 findet einen nackten Zustand im Kontinuum: ~60 %.
- Gesehen (mindestens eine stille Stelle in den drei Baendern): ~45 %. Dafuer spricht, dass die Sextik-Stelle n = 1 im
  dicken Ball sitzt und nicht an die Duennwand gebunden ist. Dagegen spricht, dass das Log-Potential keine Duennwandgrenze
  hat und der Kanal-Topf anders aussieht.
- Falls gesehen: Lage rho zwischen 1,5 und 1,95 (Haeufung nahe 2m, Boussaid/Comech laut X-BAELLE [S]).

## Rahmen

Code-Agent. Nur .69 ueber kleintest.sh (CPU-Spuren), jeder Aufruf hoechstens 10 min Wanduhr. Laufzeit vorab mit einem
Rauchtest messen (lokal <= 120 s, ein Thread, nice 19). Zwischenergebnisse nach jeder Zeile speichern.
