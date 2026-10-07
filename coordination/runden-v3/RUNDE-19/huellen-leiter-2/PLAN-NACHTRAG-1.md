# PLAN-NACHTRAG-1 (HUELLEN-LEITER-2) - NACHTRAEGLICH

- Geschrieben ab 15:42:52 CEST (date), nach Laufbeginn (Ketten seit 15:34:53). Gesehen hatte ich vorher: Newton-K0 der
  Stufe 1 fuer die Stellen 1 bis 56 (Lagen alt gegen neu gleich auf <= 1,1e-14), Vorzeichenfolgen der neuen Zeilen 0 bis
  94 und die Stellen der Paare 80 bis 94 auf Stufe 2, jeweils gegen Runde 18. Vom Suchbereich (Paare ab 110) ist nichts
  gerechnet und nichts gesehen.
- **Befund (K0-Daten, Stufe 2):** Ab Zeile 89 (R = 28,4) hat s auf den oberen Kurven ein anderes Vorzeichen als in
  Runde 18 (Zeile 89: k = 6, 7; Zeile 94: k = 4 bis 7). In den Paaren 88 bis 94 entstehen Vorzeichenwechsel, die Runde 18
  nicht hat (k = 7 bei R = 27,86; k = 6 bei 28,30; k = 5 bei 29,10; k = 4 bei 30,53), und bekannte Stellen haben den
  umgekehrten Zellen-Umlauf (k = 7 bei 28,45 und 31,00; k = 6 bei 30,12; k = 5 bei 29,12).
- **Folge nach PLAN 3:** K0 kann nicht bestanden werden. Gleichen die Stufe-1-Stellen denen der Stufe 2, gibt es
  zusaetzliche gezaehlte Stellen und andere Umlaeufe (K0a, K0b verletzt); gleichen sie Runde 18, sind die Stellen auf
  den Stufen verschieden und fallen aus der Zaehlung (K0a verletzt). Damit gilt "Abbruch": Der Suchbereich wird nicht
  gerechnet und nicht ausgewertet.
- **Ablauf (nur Ablaufsteuerung):** Die Bloecke des Suchbereichs (Stufe 1 110-124, Stufe 2 110-117 und 117-124, auch die
  zweite Welle auf cpu) werden ueber die Stoppdateien aus/stopp-st1-110-124, aus/stopp-st2-110-117,
  aus/stopp-st2-117-124 (15:42 angelegt) sofort beendet. Die laufenden und wartenden K0-Auftraege laufen zu Ende; die
  K0-Auswertung (auswertung2.py k0) laeuft wie geplant und liefert den formalen Ausgang.
- **Diagnose (nachtraeglich, keine Wertung, kein Ersatz fuer K0):** Ursache der neuen Vorzeichenwechsel.
  - D1: An jeder Stelle der neuen Kette in den Paaren 0 bis 109, die keiner Stelle der Runde 18 im selben Paar auf
    derselben Kurve (Lage auf 1/16 Zeilenabstand) entspricht, je Stufe: Newton (Code 1, newton_E1 auf W, stabilisierte
    Kopplung) ab der Lage der Kette, dann sigma2/sigma1 und Rechteck-Umlauf (cmd_umlauf, unveraendert). Erwartung [H]:
    W = 0 dort, aber ohne Rangabfall (sigma2/sigma1 = O(1)), also Scheinnullstellen mit Zeile c von G = 0; sie entstehen,
    weil die Stabilisierung den Faktor (1 + delta lambda) aus PLAN 2 auf manchen Kurven durch null fuehrt.
  - D2: An den bekannten Stellen mit umgekehrtem Zellen-Umlauf (hoechstens 4 je Stufe, kleinste R zuerst) derselbe
    Aufruf: zeigt, ob der Rechteck-Umlauf von W mit umgekehrt ist (Wechsel der Vorzeichenkonvention von s, nicht der
    Stelle). Die Newton-Lagen dieser Stellen sind in K0c schon gerechnet.
  - Ergebnisse werden nur als Diagnose berichtet; P0 bis P4 werden nach PLAN 3 und 6 gewertet (P0 nach K0, P1 bis P4
    offen).
