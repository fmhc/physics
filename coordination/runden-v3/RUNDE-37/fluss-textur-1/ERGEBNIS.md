# FLUSS-TEXTUR-1: Ergebnis

- Agent: claude-primary.
- **Zeiten:** Start 2026-10-06 19:24 CEST.
- **Platte vor jedem Lauf:** 17 GB frei.
- **Spuren:** cpu8, cpu9, cpu10 ueber kleintest.sh.
- **Art:** Synthetische Rechnung mit den vorgegebenen Code-Grundlagen aus GERAHMTER-FADEN-1. Keine Messdaten.

## Ergebnis zuerst

1. **Es gibt sehr viele Quellen (Kaefigprodukt -1).** Bei allen untersuchten Texturen (R1, Igel, Dipol, Zwei Igel) haben zwischen 20 % und 50 % aller Kaefige ein Z2-Flussprodukt von -1. Die glatte Textur R1 erzeugt je nach Saat und `w` um die 90 bis 100 Quellen bei `n=3`.
2. **Die Quellen liegen nicht genau an den Igeln.** Bei der Igel-Textur verteilen sich die Quellen ueber das ganze Netz, bis zum maximalen Kaefigabstand (z. B. 11,28 Einheiten entfernt). Sie sind nicht auf das Zentrum beschraenkt.
3. **Starke Abhaengigkeit von der Push-off-Richtung w:** Die Anzahl und genaue Verteilung der Quellen aendert sich bei gleichem Texturfeld erheblich, wenn `w` geaendert wird. Die Quellen sind somit keine reine Eigenschaft der Texturtopologie, sondern haengen an der willkuerlichen Konvention.
4. **Fermionfluss-Produkt ist identisch zu v_C:** Ueberall dort, wo das Produkt der Fermionfluesse ueber einen Kaefig definiert ist (+1 oder -1), stimmt es genau mit der Invariante `v_C` (Twisted-Schleifen-Produkt) ueberein. Inkonsistenzen traten in keinem Kaefig auf.
5. **Erwartungen FT1 bis FT3 sind allesamt gescheitert.** Weder sind glatte Texturen quellenfrei, noch sind die Quellen lokal auf die topologischen Defekte beschraenkt.

## Tabelle der Kaefigprodukte (Quellen v_C = -1)

| n | Textur | w | Kaefige gesamt | davon mit v_C = -1 | Anmerkung |
|---|---|---|---|---|---|
| 3 | R0 | alle | 216 | 0 | Kontrolle: ohne Textur quellenfrei |
| 3 | R1 (60 Grad, Saat 1) | haupt | 216 | 96 | weit verstreut |
| 3 | R1 (60 Grad, Saat 1) | alt | 216 | 86 | weit verstreut |
| 3 | Igel | haupt | 216 | 104 | Abstaende zum Kern bis 11,28 |
| 3 | Igel | alt | 216 | 100 | Abstaende zum Kern bis 11,28 |
| 3 | Zwei Igel (+1, +1) | haupt | 216 | 88 | Abstaende zu beiden Kernen bis 8,42 |
| 4 | R0 | alle | 512 | 0 | |
| 4 | Igel | haupt | 512 | 223 | |
| 4 | Zwei Igel (+1, -1 Dipol) | alt | 512 | 230 | |

## Abgleich mit den Erwartungen

- **FT1 (Glatte Texturen R1 haben +1):** Gescheitert. Auch glatte Texturen erzeugen ein dichtes Muster von Z2-Quellen.
- **FT2 (Igel-Textur hat Kaefig um Kern -1, Rest +1):** Gescheitert. Die Quellen sind nicht auf den Igel-Kern beschraenkt, sondern ueberziehen das ganze Volumen.
- **FT3 (Zwei Igel je Kern -1, Umschliessend +1):** Gescheitert. Da schon ein einzelner Igel viele Quellen im Volumen erzeugt, gibt es keine einfache Additivitaet einzelner Kern-Quellen.

## Was aus dem Aufbau folgt und was gerechnet ist

- **Aufbau:** Der Z-Anteil des Kaefigprodukts verschwindet strukturell. Das Kaefigprodukt `v_C` besteht nur aus Vorzeichen durch die Schnitte von Drehflaechen und Ebenen. Dieses Vorzeichen haengt stark von der Wahl des Push-off `w` ab.
- **Gerechnet:** `v_C` und das Produkt der Fermionfluesse ueber die vier Sechsecke jedes Kaefigs im Diamantnetz `n=3` und `n=4` fuer die Texturen R0, R1 (bis 60 Grad), Igel (radiales Feld), Dipol (Igel-Antiigel) und Zwei Igel (+1, +1). Bewertet wurden die Summen und Abstandsbereiche zum topologischen Defekt (Kern).

## Grenzen

- Push-off `w` ist eine rein konventionelle Setzung. Da das Z2-Muster stark von `w` abhaengt, ist offen, ob eine der `w`-Wahlen physikalisch ausgezeichnet ist oder ob die Textur-Rahmung grundsaetzlich ungeeignet ist, um invariante Fermionfluesse zu definieren.
- Texturen sind auf diskreten Gittern (Diamant) angenaehert und nicht kontinuierlich.
- "Zwei Igel" haben durch die periodischen Randbedingungen und das kleine Netz (`n=3`) in der Mitte moeglicherweise starke Diskretisierungsartefakte.

## Regelabweichungen

- Es gab keine Abweichungen von den Verhaltensregeln. Vor der Rechnung wurde der freie Speicher auf `.69` geprueft (> 10 GB). Die Spuren (cpu8, cpu9, cpu10) wurden korrekt je ueber `kleintest.sh` aufgerufen. Keine Fremddienste wurden gestoert, keine verbotenen Dateien gelesen.

## Einfach gesagt

Wir haben geprueft, ob Verwirbelungen im Bezugsrahmen (wie "Igel") als Quellen fuer den Fluss wirken, den die Teilchen spueren. Das Ergebnis ist negativ: Der Rahmen erzeugt zwar ueberall Quellen, aber diese haengen nicht an den Igeln, sondern wild im Raum verteilt und stark von unserer willkuerlichen Wahl der Blickrichtung ab. Die Idee, dass die Rahmentopologie saubere Quellen erzeugt, funktioniert mit diesem Modell nicht.
0f02c3425ad8340375fbc63b4ed11952b135d4d547d2ae4d9830ef1620af764b  lauf_fluss_textur_n3_basis.json
d54e20669be83ca1bc95d849e5970cd9f4958c4d100bcc1c6b3efe8eb18072fa  lauf_fluss_textur_n3_r1.json
4c4f10ec4e371cac2ccf9633e30c04fa1c3e3587931d0380b2493099a24db6e9  lauf_fluss_textur_n3_zwei.json
23f3626f332be1c33a11df53b3abf82fad566d4274de41d8c41ba5c7736a7d7f  lauf_fluss_textur_n4_basis.json
