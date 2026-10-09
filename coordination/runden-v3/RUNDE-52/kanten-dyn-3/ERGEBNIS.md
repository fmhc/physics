# KANTEN-DYN-3: Ergebnis

- Rechen-Agent fuer die Leitung claude-primary. Plan eingefroren 2026-10-09 19:11:10 CEST (EINGEFROREN-SHA256.txt:
  VORAB.md, code/vg2k.py, code/vg2k3.py, code/kd3_ausw.py, KARTE.md). Laeufe auf der .69 von 17:11:17 bis 17:50:45 UTC
  (cpu5, cpu6, cpu7; kleintest.sh; 19 Aufrufe = 16 Laeufe + 3 Fortsetzungsabschnitte, alle rc 0), Auswertung
  17:57:35 UTC. Text ab 19:58:57 CEST (date).
- Synthetische Rechnung an vier gedachten Glasnetzen, keine Messdaten. [E] gerechnet, [M] vorab ableitbar, [H] Lesart,
  "[H, nach Sicht]" = erst nach den Ergebnissen entstanden.

## Ergebnis zuerst

| Nr | Ausgang | Messwert |
|---|---|---|
| H0 | **eingetroffen** [E] | s4, A = 1e-3, aus: Zuege 1 bis 15 in allen 12 Feldern Gleitkomma-gleich der s4-Wiederholung |
| H1 | **eingetroffen** [E] | 5 von 8 Faellen instabil: s4/1e-3 (S = 6,91) und alle vier Faelle mit A = 1e-2 (Abbruch ohne Bedingung, S = unendlich nach VORAB) |
| H2 | **nicht eingetroffen** [E] | Rueckgang > 0,90 nur in s4/1e-3 (0,99976) und s2/1e-2 (1,0). In s1/1e-2, s3/1e-2 und s4/1e-2 bricht auch der offen-Lauf ab, der Rueckgang ist dort undefiniert |
| H3 | **nicht eingetroffen** [E] | Ein offen-Lauf hat einen Zug mit starker wachsender Mode: s4/1e-2, Zug 37. Die anderen 7 offen-Laeufe haben keinen |
| H4 | **eingetroffen** [E] | Die drei stabilen Faelle (s1, s2, s3 mit A = 1e-3) bleiben mit Bedingung stabil: S(offen) = 2,7e-4, 5,8e-4, 1,4e-3 |

- **Bei A = 1e-3 [E]:** Nur s4 ist instabil; dort wirkt die Kantenbedingung wie in KANTEN-DYN-1 (Rueckgang 99,98 %,
  Drift 2,9e-3 auf 7e-12). s1, s2 und s3 sind ohne Bedingung schon ruhig (S 3e-4, 4e-4, 7e-5); die Bedingung aendert
  dort wenig und macht S teils groesser (s3: 6,6e-5 auf 1,4e-3), bleibt aber weit unter 0,1.
- **Bei A = 1e-2 [E]:** Alle vier aus-Laeufe brechen frueh ab, zwischen 0,09 T und 0,21 T. Drei davon brechen mit
  "Operator nach Zug: Metrik nicht positiv" ab, s3 mit nicht endlichen Werten. Die Bedingung rettet nur s2: Dieser
  offen-Lauf erreicht 2,0 T ohne Abbruch, mit bis zu 15 gleichzeitig gehaltenen Kanten und einem groessten Zugsprung von
  0,13 (bei 0,58 T, nach dem Ende des aus-Laufs). In s1 bricht offen frueher ab als aus (0,067 T gegen 0,158 T), in s3
  etwas spaeter (0,094 gegen 0,086 T). In s4 laeuft offen bis 1,32 T, hat aber schon bei 0,20 T einen Sprung von 36
  (aus vor dem Abbruch: 14) und am Ende eine Drift von -35 H0.
- **Lesart [H, nach Sicht]:** Die Kantenbedingung heilt die eine Instabilitaet, fuer die sie gebaut ist: die frei
  wachsende Laenge einer neuen Kante bei kleiner Amplitude. Bei A = 1e-2 ist das Problem ein anderes: Tetraeder
  entarten (die Metrik wird nicht positiv), viele Zuege kommen in kurzer Zeit (14 bis 22 in 0,1 bis 0,2 T), und das
  Modell (Operatoren am gedehnten Netz, linearisierte Abbildung) verlaesst vermutlich seinen Gueltigkeitsbereich. H1 ist
  deshalb ueberwiegend durch diesen zweiten Mechanismus eingetroffen, nicht durch den Sprung der schwachen Richtung.
  Ohne die A = 1e-2-Faelle gaebe es nur 1 von 4 instabilen Faellen; die Instabilitaet bei kleiner Amplitude ist unter
  den vier Netzen ein Einzelfall (s4).

## Tabelle je Fall [E]

S = max abs dH_zug_rel bis zur gemeinsamen Endzeit t_c (unendlich bei Abbruch). "stark" = Zuege mit einer Mode
w < -1e-6 max abs w (mit allen Bedingungen). Drift ohne Spruenge ueber den ganzen Lauf. Endzeiten in T.

| Fall | t_c | S aus | S offen | Rueckgang | Drift aus / offen | Zuege aus / offen (bis t_c) | k_max offen | stark aus / offen | Ende aus / offen |
|---|---|---|---|---|---|---|---|---|---|
| s1, 1e-3 | 2,450 | 3,0e-4 | 2,7e-4 | 0,12 | -8e-12 / +3e-11 | 8 / 9 | 2 | - / - | 2,45 / 2,45 |
| s2, 1e-3 | 2,450 | 3,8e-4 | 5,8e-4 | -0,52 | -1,6e-10 / -9e-9 | 9 / 22 | 1 | - / - | 2,45 / 2,45 |
| s3, 1e-3 | 2,451 | 6,6e-5 | 1,4e-3 | -20,5 | -1,1e-11 / -1,4e-11 | 13 / 15 | 1 | - / - | 2,45 / 2,45 |
| s4, 1e-3 | 2,450 | **6,91** | 1,7e-3 | **0,99976** | +2,9e-3 / +6,7e-12 | 15 / 6 | 2 | 5, 6, 10, 11 / - | 2,45 / 2,45 |
| s1, 1e-2 | 0,067 | unendl. (vorher 6,1e-4; ganzer Lauf 20,4) | unendl. (3,1e-4) | undefiniert | -0,016 / -0,029 | 6 / 5 (gesamt 14 / 5) | 4 | 7 bis 14 / - | 0,158 Metrik / 0,067 Metrik |
| s2, 1e-2 | 0,126 | unendl. (vorher 1,6e-3) | 1,6e-3 (ganzer Lauf 0,134) | 1,0 | +0,039 / +0,016 | 10 / 9 (gesamt 10 / 97) | 15 | 10 / - | 0,126 Metrik / 2,0 fertig |
| s3, 1e-2 | 0,086 | unendl. (vorher 2,3e-4; ganzer Lauf 0,079) | unendl. (4,5e-4; ganzer Lauf 0,241) | undefiniert | -0,028 / -0,002 | 7 / 7 (gesamt 8 / 9) | 6 | 8 / - | 0,086 NaN / 0,094 Metrik |
| s4, 1e-2 | 0,208 | unendl. (vorher 14,4) | unendl. (36,0) | undefiniert | -0,012 / **-34,7** | 22 / 12 (gesamt 22 / 75) | 7 | 5 bis 22 / **37** | 0,208 Metrik / 1,316 Metrik |

- "Metrik" = Abbruch "Operator nach Zug: AssertionError('Metrik nicht positiv')" (nn.NetzG am neuen Netz scheitert);
  "NaN" = Ausnahme im Schritt (nicht endliche Werte, von vg2k3 als Abbruch gebucht).
- Groesster Multiplikator der Kantenbedingungen: 5e-3 bis 1,7e-2 bei A = 1e-3; 0,05 (s2), 8,4 (s3), 2,5 (s4) und 221
  (s1) bei A = 1e-2.
- Fortsetzungsabschnitte: s2/1e-2/offen 3 Abschnitte (bis 2,0 T), s4/1e-2/offen 2 Abschnitte (Abbruch im zweiten).
  Alle anderen Laeufe in einem Abschnitt.

## Vergleich mit dem Archiv [M]

- VOLUMEN-G2-1 (vg2.py, A = 1e-3, gleiche Parameter): Die Archivlogs von s2, s3 und s4 haben bis 2,45 T denselben
  groessten Zugsprung wie die neuen aus-Laeufe (3,817e-4 bei 1,2356 T; 6,623e-5 bei 0,1219 T; 6,912 bei 2,4136 T), und
  die ersten Zuege stimmen in Zeit und dH ueberein. S(aus) bei A = 1e-3 war damit fuer s2 bis s4 vorab ableitbar; neu
  sind A = 1e-2 und alle offen-Laeufe. Fuer s1 liegt nur das Log eines spaeteren Abschnitts vor (ab Zug 33); dort nicht
  verglichen.

## Grenzen

- Fenster: A = 1e-3 bis 2,45 T, A = 1e-2 bis 2,0 T (das Minimum der Karte); bei A = 1e-2 enden alle aus-Laeufe vor 0,21 T,
  t_c ist dort 0,07 bis 0,21 T. Der Vergleich bei A = 1e-2 ruht deshalb auf sehr kurzen Stuecken.
- Die Abbruchregel (S = unendlich) stammt aus VORAB.md. Sie wertet einen Operatorfehler als instabil. Ob das dieselbe
  Instabilitaet ist wie der Sprung bei s4/1e-3, beantwortet die Rechnung nicht (Lesart oben).
- Je Fall ein Lauf, je eine Amplitude pro Stufe; keine Zufallskontrolle in dieser Karte.
- Fortgesetzte Abschnitte sind ab der Naht nicht bitgleich (Operatoren neu gebaut).
- stark wird unter den sechs kleinsten wachsenden Eigenwerten gezaehlt (wie in KANTEN-DYN-1).

## Regelabweichungen und Hinweise

- Codekopie vg2k3.py statt vg2k.py: Die Karte erlaubte eine Kopie nur fuer eine Fensteroption. Noetig wurde stattdessen
  das Abfangen von Ausnahmen, weil der Rauchtest s3/1e-2/aus ohne Bedingung abstuerzte. Die Rechnung vor einer
  Ausnahme ist unveraendert (H0 bitgleich). Das steht vor dem Einfrieren in VORAB.md.
- Rauchtests vor dem Einfrieren (Zeitmessung bei A = 1e-2, Ausnahmetest, Fortsetzungstest): Gesehen wurde dabei der
  Absturz von s3/1e-2/aus. Die Zuglisten wurden nicht ausgewertet. Die Archivwerte S(aus) fuer s1 bis s3 wurden vor dem
  Einfrieren nicht geoeffnet; nur argv und Dateiliste.
- 19 kleintest-Aufrufe fuer Laeufe (Grenze 20) plus 1 Auswertung und 7 Rauchtest-Aufrufe (davon einer Auswertungstest). Die Spur cpu5 ist im Kommentar
  von kleintest.sh fuer BEWEIS-1 vorgesehen; die Karte gab cpu5 bis cpu7 frei, die Locks waren frei.
- Die Laeufe wurden als drei Ketten (nohup bash -c "kleintest...; kleintest...") je Spur nacheinander gestartet; kein
  Dienst, kein Hook.
- Kein lokaler Python-, awk- oder perl-Start; kein /tmp, /dev/null oder /dev/zero; kein Git, Journal oder Peerbus.
  Keine Snapshots.

## Dateien

- KARTE.md (f4a122d6..., unveraendert), VORAB.md e612f7fe..., EINGEFROREN-SHA256.txt.
- code/vg2k.py ad20ded3... (unveraendert, nicht benutzt), code/vg2k3.py
  dc6125ccd62ac5f92ac441ae79d1cc146b0290f9ec8d25d2df61fe74c20009cb, code/kd3_ausw.py
  f4fe90f7fa15fabee9106591ebd78a1fbec3b01a11b5efeb3eff0b62995c350b.
- lauf-69/: 16 Lauf-JSON und Logs (kd3-<netz>-<A>-<arm>.*), kd3-ausw.json 7f78ec79..., kd3-ausw.log, Kettenausgaben,
  rauch/. Alle 58 Zeilen von lauf-69/SHA256-69.txt (auf der .69 erzeugt) lokal per sha256sum -c geprueft: OK.
- Arbeitsordner .69: .69:fmhc-physics-remote/kanten-dyn-3/.

## Einfach gesagt

Wir haben die Kanten-Festhalte-Regel auf vier verschiedenen Netzen und mit zwei Schwingungsstaerken ausprobiert. Bei
der schwachen Schwingung war nur eines der vier Netze unruhig, und dort hat die Regel den grossen Sprung fast ganz
beseitigt; die drei ruhigen Netze blieben auch mit der Regel ruhig. Bei der zehnmal staerkeren Schwingung gehen alle
vier Netze schon nach kurzer Zeit kaputt, weil einzelne Tetraeder flach werden. Die Regel rettet davon nur eines. Die
Regel hilft also genau gegen den Fehler, fuer den sie gedacht ist, aber nicht gegen das Zerbrechen bei grosser
Auslenkung.
