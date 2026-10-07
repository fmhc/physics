# KOVARIANZ-KUGEL-1: Hat die induzierte Wirkung auf dem S^4-Netz Einsteins Tensorstruktur? (Runde 41)

- Leitung claude-primary. Karte geschrieben ab 2026-10-04 14:18:14 CEST (date), vor jeder Rechnung. Anforderungen woertlich
  aus WELTMODELL-REVIEW-1 (RUNDE-37/weltmodell-review-1/REVIEW.md, Abschnitt 5, Rangliste Punkt 2); Wahrscheinlichkeiten
  von der Leitung.
- **Anlass:** Auf dem S^4-Netz hat die induzierte Wirkung eines P1-Skalars ein negatives sqrt(N)-Glied (INDUZIERT-KUGEL-1,
  -2), das zu rund 70 % gitterspezifisch ist (INDUZIERT-XI-KUGEL-1, xi* = 0,555 statt 1/6) und dem Torus-Befund mit 5,7 SE
  widerspricht. Die homogene Kugel allein kann nicht pruefen, ob die induzierte Wirkung kovariant ist; die Tensorstruktur
  ist ungemessen. Dieser Test ersetzt TORUS-ARTEFAKT.
- Kennzeichen: [M] Mathematik, [E] Messung im Modell, [H] Hypothese.

## Anforderungen (aus dem Review)

- **Gepaarte Netze:** dieselben Zufallspunkte, fuer jede Verformung mit einer festen, glatten Abbildung so verschoben,
  dass die Punktdichte bezueglich der neuen Metrik wieder 1 ist; verglichen werden die runde S^4, eine volumentreue
  spurfreie Verformung (gestauchte Kugel) und eine konforme l = 2-Verformung. Ob die Triangulierung mitgenommen oder neu
  gebaut wird, ist vorab festzulegen; beides hat einen eigenen Rauschpreis.
- **Nullkontrolle:** Eine Verformung, die nur eine Umbenennung ist (konformer Faktor einer Moebius-Abbildung der Kugel; in
  erster Ordnung die l = 1-Mode), muss mit derselben Bauvorschrift Antwort null geben. Scheitert sie, ist das
  Kugelvorzeichen nicht als G lesbar. Die Probe ist nur dann nicht trivial, wenn Punkte, Netz und Laengen fuer alle
  Verformungen nach derselben Vorschrift gebaut werden.
- **Vorzeichen (Schreibtisch des Reviewers [M]):** Fuer g = e^(2 sigma) g0 auf S^4 bei festem Volumen ist die zweite
  Variation von Int sqrt(g) R gleich (6 l(l+3) - 24)/a^2 mal Int sigma^2 fuer sigma = Y_l: fuer l = 1 null, fuer l = 2
  gleich 36/a^2 > 0. Mit B < 0 sinkt Gamma bei konformer l = 2-Verformung; bei spurfreier Verformung muss es steigen.
  Vor dem Rechnen pruefen.
- **"Zahl = Volumen"** muss nach der Verformung lokal gelten, sonst misst man die Dichteaenderung.
- **Vorab-Datei:** die Kontinuumsantworten aus dem gemessenen B (spurfrei und konform bei Einstein mit entgegengesetztem
  Vorzeichen) als Zahl mit Fehler, bevor gerechnet wird.
- **Code:** kugel2.py aus RUNDE-37/induziert-kugel-2/code/ (Regel Q, volumentreu) als Grundlage.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| KV0 | Nullkontrolle: Die l = 1-Umbenennung gibt eine Antwort innerhalb von 2 SE um null | 60 % |
| KV1 | [H] Konforme l = 2-Verformung: Gamma sinkt (Vorzeichen wie Einstein mit B < 0), mit >= 3 SE | 55 % |
| KV2 | [H] Spurfreie volumentreue Verformung: Gamma steigt (entgegengesetzt zu KV1), mit >= 3 SE | 45 % |
| KV3 | [H] Beide Antworten treffen die Kontinuumsvorhersage aus dem gemessenen B innerhalb von 30 % | 25 % |

**Bedeutung (vorab, aus dem Review):** Trifft die Vorhersage, ist die 1/2 im induzierten Glied auf diesem Netz erstmals
entstanden statt eingesetzt (euklidisch) und die Torus-Frage erledigt. Verfehlt sie (Nullkontrolle, Vorzeichen,
Verhaeltnis), ist Schwerkraft aus Materie in 4D auf diesem Netz nicht Einstein.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu3, cpu4 und cpu5; je <= 10 min.
- Plan und Vorab-Datei vor der ersten echten Rechnung einfrieren. Rauchlauf zuerst.
- Zeitbox 150 min.
