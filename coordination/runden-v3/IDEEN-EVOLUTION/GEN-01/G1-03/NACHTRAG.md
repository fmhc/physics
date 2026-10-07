# G1-03 Nachtrag (Test-Agent T-2)

- 2026-09-30 08:08:05 CEST (date): Code und Formprobe, KARTE.md unveraendert seit 07:58:24.
- Die Kopie teilung_schwelle.py aendert nur Laufliste, Laufzeit T, Kennzahlen und Plausibilitaetsschranke. Neu sind die
  Argumente --teil und --t-end, dazu die Ausgabenamen teilung_<teil>_<stufe>. Schiessen, Gitter, Zeitschritt, Randschicht,
  Gebietsanalyse und gamma-Fit sind unveraendert (jede Aenderung mit "G1-03" markiert).
- Umsetzung der Karte:
  - V1 "monoton": Die Folge Teilung ja/nein ueber omega^2 springt hoechstens einmal von nein auf ja. Dazu teilt 0,55
    nicht und 0,65 schon.
  - V2: gamma nicht fallend ueber die teilenden Laeufe. Der Nullpunkt der gamma^2-Geraden durch die zwei tiefsten
    teilenden Laeufe liegt bei mindestens (hoechste nicht teilende Stelle - 0,03). Laeufe ohne gamma-Fit fallen dabei
    heraus.
  - L3: gleicher Ausgang und gleiche Toechterzahl, gamma-Aenderung hoechstens 0,2 relativ. Die t_teilung-Pruefung des
    Originals steht nur zur Information daneben.
- Grob und fein laufen als getrennte Aufrufe, weil das Original keinen Zeitwaechter hat. Der fein-Aufruf liest die
  grob-Datei fuer L3 und V1 bis V3.
- Formprobe 08:06 bis 08:07 (lokal, CPU, --rauch --mini): alle drei Aufrufe rc 0. Die Zahlen gelten nicht und werden
  nicht geerntet.
