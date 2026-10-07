# VOLUMEN-G2-1: Ergebnis

- Rechen-Agent fuer die Leitung claude-primary.
- Zeiten (date; .69 in UTC, CEST = UTC + 2):
  - Karte 03:30:56 CEST, VORAB.md ab 03:35:14 CEST, vor jeder Rechnung.
  - Rauchtest 01:39 UTC, V0 01:41 bis 02:05 UTC, Hauptlaeufe 01:48 bis 02:30 UTC, Gegenprobe 02:01 bis 02:24 UTC.
  - Nach der Sitzungspause der Leitung: Fortsetzung von g-s1-b1 (Perioden 8 bis 10) 12:40 bis 12:46 UTC.
  - Alles ueber kleintest.sh (cpu2, cpu3, cpu4), je Abschnitt hoechstens 480 s. df vor jedem Start: 17 GB frei.
  - Text ab 14:48 CEST.
- Kennzeichen: [E] gerechnet, [M] Schreibtisch, [P] Projektdatei, [L] Literatur aus dem Gedaechtnis, [S Abstract]
  nur Abstract gelesen, [H] Hypothese. Alles synthetisch an gedachten Netzen, keine Messdaten.

## 1. Ergebnis zuerst

1. **V0 haelt [E].** Der Integrator ist die implizite Mitte mit Lagrange-Multiplikator, die Operatoren sind fest.
   - In allen vier Netzen liegt die Energie ueber 10 Perioden bei hoechstens 1,3e-10 relativ.
   - Die Volumenbedingung ist auf hoechstens 1e-14 relativ erfuellt.
   - Ohne Bedingung liegt die Energie bei 1e-13.
   - Mit Nachfuehrung je Periode entstehen Spruenge von hoechstens 8e-6. M_eff behaelt dabei 128 negative Richtungen.
2. **Mit Volumenbedingung laufen s1, s2 und s3 zehn Perioden durch; ohne Bedingung bricht jedes Netz ab [E].**
   - Ohne Bedingung bricht s1 nach 1,7 Perioden ab, s2 nach 1,2, s3 nach 0,12 und s4 nach 7,2 Perioden.
   - Der Grund ist jedes Mal "Metrik nicht positiv" beim Operatorbau nach einem Zug.
   - In s1 und s2 gingen Energiespruenge von 9 bzw. 11 H0 voraus.
   - Mit Bedingung (max \|H - H0\|/H0): s2 1,05e-3, s3 7,2e-4, s1 2,8e-3. s1 heizt dabei langsam und gleichmaessig.
3. **Mechanismus [E]: Die Bedingung entfernt die starke wachsende Mode nach den Zuegen.**
   - Ohne Bedingung hat das Spektrum nach etwa jedem zweiten Zug eine Mode mit omega^2 von -1e7 bis -4e7. Ihre
     Wachstumsrate liegt bei 3000 bis 6000 je Zeiteinheit, weit ueber omega_max = 60 bis 160.
   - Mit Volumenbedingung bleibt sie in s1, s2 und s3 nach keinem der 133 Zuege. In s4 bleibt sie nach 4 von 46 Zuegen.
   - Uebrig bleiben nur fast neutrale Moden mit omega^2 ~ -1e-5. Sie stehen auch ohne jeden Zug im Spektrum (V0 P).
   - Auf der Tangente der Bedingung ist die Traegheit in s1 bis s3 nach allen Zuegen positiv definit.
4. **Gegenprobe mit einer zufaelligen linearen Einzelbedingung (Zusatz, nach den ersten Zwischenergebnissen gewaehlt)
   [E]:**
   - s1 und s2 laufen in die Kaskade (\|H - H0\| > 100 H0); die starke Mode bleibt dort.
   - s3 laeuft durch, mit 8e-2 statt 7e-4.
   - Die Volumenbedingung wirkt also gezielter als eine beliebige Einzelbedingung. Das ist eine Stichprobe mit nur einem
     Zufallsvektor je Netz.
5. **Zwei Befunde sprechen dagegen [E]:**
   - Die Zwangskraft ist nicht klein. Ohne Zuege ist sie 30 bis 38 % der Netzkraft (s2 bis s4, s1 2 %), mit Zuegen 52
     bis 88 %. In der A_r-Metrik (Beschleunigung) ist sie gleich gross wie die Netzkraft (Verhaeltnis 1,00).
   - s4 mit Bedingung hat eine Episode bei 1,4 und 2,4 Perioden. Dort bleibt die starke Mode nach 4 Zuegen. Die
     Zugspruenge erreichen 6,9 H0, die Projektionen -2,5 H0. Die Energie bleibt danach bei 0,16 H0.
   - Im selben s4-Lauf traegt der Integrator 2,9e-3 Restdrift ausserhalb der gebuchten Spruenge. Die Ursache ist offen.

## 2. Tabellen

### 2.1 V0 (Arm a, keine Zuege, A = 1e-3, 10 Perioden)

| Netz | Stufe, h | max \|dH\|/H0 ohne | max \|dH\|/H0 mit | \|V - V0\|/V0 mit | \|V - V0\|/V0 ohne (frei) | Fc/Fn rms (A_r-Metrik) | cos(TT, Normale) |
|---|---|---|---|---|---|---|---|
| s1 | F, 1 | 5,3e-14 | 3,9e-12 | 4,9e-15 | 3,9e-6 | 0,023 (0,037) | 5,0e-4 |
| s2 | F, 1 | 3,5e-14 | 1,3e-10 | 9,8e-15 | 3,0e-5 | 0,35 (0,58) | 4,1e-3 |
| s2 | F, 0,5 | 6,4e-13 | 3,3e-11 | 9,3e-15 | 3,0e-5 | 0,35 (0,58) | 4,1e-3 |
| s3 | F, 1 | 1,4e-13 | 2,5e-11 | 2,3e-15 | 4,5e-5 | 0,38 (0,65) | 8,5e-3 |
| s4 | F, 1 | 1,4e-13 | 1,3e-10 | 1,0e-14 | 3,6e-5 | 0,30 (0,50) | 8,7e-3 |
| s2 | P, 1 | 8,6e-7 | 7,8e-6 | 9,5e-15 | 3,0e-5 | 0,34 (0,57) | |
| s4 | P, 1 | 8,5e-7 | 8,1e-6 | 1,0e-14 | 3,6e-5 | 0,30 (0,50) | |

- Stufe P: Die Spruenge der Nachfuehrung summieren sich zu -7,5e-7 / -3,1e-6 (s2 ohne / mit) und -1,1e-7 / +7,0e-6
  (s4). Die Integratordrift ohne die Spruenge liegt bei hoechstens 8e-11.
- Bei allen 18 Nachfuehrungen bleibt M_n_neg = 128, und S bleibt gleich (Abstand 0). Das strenge Kriterium meldet je
  1 bis 3 "wachsende" Moden (omega^2 ~ -1e-5), auch ohne jeden Zug.
- Rauchtest [E]: V(x = 0) = \|det LV\| = 128 auf 1e-16 genau. Der analytische Gradient stimmt mit finiten Differenzen
  auf 1e-8 bis 5e-6 ueberein (Rauschen der Differenzen).
- Startprojektion auf die Tangente: H0 aendert sich um -1e-7 (s1) bis -3e-5 (s4). Beide Arme starten aus demselben
  Zustand.
- Newton: In hoechstens 1 Schritt je V0-Lauf konvergierte G(x_m) nicht voll; die Bedingung wurde trotzdem erzwungen.

### 2.2 V1 bis V3 (Arm b, Lesart P, Stufe P, h = 1, A = 1e-3, 10 Perioden)

| Netz | Arm | Ende (Perioden) | Abbruch | Zuege (Ausn. HG) | max \|dH\|/H0 | dH Ende | Summe Zug / Proj. / Nachf. | Drift ohne Spruenge |
|---|---|---|---|---|---|---|---|---|
| s1 | ohne | 1,66 | Metrik nicht positiv | 8 (2) | 9,0 | 9,0 | 9,0 / - / -2,5e-5 | 1e-11 |
| s1 | Volumen | 10 | - | 40 (10) | 2,8e-3 | 2,6e-3 | 1,2e-3 / 1,4e-3 / 5,6e-5 | -1,5e-10 |
| s1 | Zufall | 5,54 | Kaskade > 100 H0 | 20 (7) | 200 | 200 | 178 / 23 / -1e-4 | 2e-10 |
| s2 | ohne | 1,20 | Metrik nicht positiv | 9 (2) | 11,3 | 0,056 | 0,056 / - / 3,0e-5 | 6e-13 |
| s2 | Volumen | 10 | - | 52 (10) | 1,05e-3 | 9,3e-4 | 9,3e-4 / -3,5e-4 / 3,5e-4 | -2,1e-9 |
| s2 | Zufall | 1,52 | Kaskade > 100 H0 | 14 (2) | 126 | 126 | 1980 / -1853 / -2e-5 | 9e-9 |
| s3 | ohne | 0,12 | Metrik nicht positiv | 2 (1) | 8,0e-5 | -8,0e-5 | -8,0e-5 / - / 0 | 2e-13 |
| s3 | Volumen | 10 | - | 41 (10) | 7,2e-4 | -7,2e-4 | -1,7e-3 / 1,1e-3 / -1,4e-4 | -2,9e-11 |
| s3 | Zufall | 10 | - | 50 (13) | 8,3e-2 | 2,6e-2 | -7,0e-2 / 9,6e-2 / -2,2e-4 | 5e-12 |
| s4 | ohne | 7,24 | Metrik nicht positiv | 16 (1) | 3,2e-4 | -3,2e-4 | -1,1e-4 / - / -2,1e-4 | -5e-13 |
| s4 | Volumen | 10 | - | 46 (11) | 4,8 | 0,158 | 2,79 / -2,63 / -5,7e-3 | 2,9e-3 |

- "Ausn. HG": 2-3-Zug an einer Flaeche, die am Hintergrund Delaunay ist (mu_hg > 0); so definiert wie in UMKLAPP-FOLGE-1.
- Energie je Periode mit Volumenbedingung [E]:
  - s1 steigt fast linear, etwa 2,6e-4 je Periode (2,3e-4, 4,7e-4, ..., 2,6e-3).
  - s2 schwankt zwischen -8e-5 und 9,3e-4.
  - s3 faellt gleichmaessig auf -7,2e-4.
  - s4 springt in Periode 3 auf 0,166 und bleibt danach bei 0,16 bis 0,18.
- Die Zugfolge ist bis zum ersten Ausnahmezug in beiden Armen gleich: s1 bei t/T = 0,536, s2 bei 0,509, s3 bei 0,12.
  Ab dort laufen die Bahnen auseinander.

### 2.3 Spektrum nach den Zuegen (negative Richtungen, Definitheit, wachsende Moden)

| Lauf | Zuege | M_n_neg max | Zuege mit M_n_neg > 128 / auf Kern(c) > 128 | A_r indefinit | kin. neg. auf der Tangente (max) | starke Mode (omega^2 < -1) ohne / mit Bedingung | omega_max mit/ohne (max) |
|---|---|---|---|---|---|---|---|
| s1 Volumen | 40 | 130 | 20 / 6 | 20 | 0 | 18 / **0** | 0,96 |
| s2 Volumen | 52 | 130 | 25 / 19 | 25 | 0 | 25 / **0** | 0,99 |
| s3 Volumen | 41 | 130 | 20 / 10 | 20 | 0 | 20 / **0** | 1,00 |
| s4 Volumen | 46 | 131 | 24 / 13 | 24 | 1 | 24 / **4** | **1,45** |
| s1 Zufall | 20 | 130 | 11 / 11 | 11 | 2 | 11 / 8 | 1,01 |
| s2 Zufall | 14 | 130 | 7 / 7 | 6 | 1 | 6 / 2 | 1,40 |
| s3 Zufall | 50 | 130 | 23 / 23 | 23 | 0 | 23 / 0 | 1,03 |

- Die Spalte "ohne" ist im selben Lauf am selben Zustand ausgewertet, nur ohne Bedingung. Die Arme ohne Bedingung haben
  nach dem ersten Ausnahmezug dasselbe Bild: omega^2 = -1,15e7 (s2), -1,26e7 (s3), -9,8e6 (s4).
- Die "starke Mode" ist die eine Richtung, die beim Ausnahmezug dazukommt:
  - M_eff hat dann 130 statt 128 negative Richtungen, auf Kern(c) 129.
  - Die Volumenbedingung senkt das Kartenmass also nur um 1, wie das Interlacing in AG2 vorgibt [M, P].
  - Trotzdem nimmt sie die starke Mode dynamisch heraus.
- In s4 faellt die starke Mode mit der Bedingung bei t/T = 1,41 und 2,41 nicht weg. Genau dort liegen die Energiespruenge.

## 3. Abgleich mit V0 bis V3 (beschreibend, Karte unveraendert)

- **V0 (65 %): eingetroffen.**
  - Energie hoechstens 1,3e-10 und Bedingung hoechstens 1e-14, beides unter den Schwellen 1e-8 bzw. 1e-10. Kein
    Abbruch.
  - h = 0,5 und h = 1 sind gleich gut.
  - Das gilt fuer feste Operatoren (Stufe F). Mit Nachfuehrung (Stufe P) kommen die gebuchten Spruenge dazu
    (hoechstens 8e-6). Sie sind kein Integratorfehler; sie messen die fehlenden dM/dl-Terme.
- **V1 (45 %): in der Richtung eingetroffen, im Wortlaut knapp verfehlt.**
  - s2 mit Bedingung bleibt ueber 10 Perioden beschraenkt.
  - Das Maximum liegt bei 1,05e-3, also 5 % ueber der Schwelle 1e-3; am Ende sind es 9,3e-4.
  - Ohne Bedingung springt die Energie auf 11 H0, der Lauf bricht bei 1,2 Perioden ab.
  - Das Scheiterkriterium "waechst auch mit Bedingung" ist nicht eingetreten, "bleibt auch ohne beschraenkt" ebenfalls
    nicht.
- **V2 (60 %): nicht eingetroffen.** Das Scheiterkriterium "Die Bedingung stabilisiert auch s1 oder s3" ist eingetreten,
  in beiden Netzen.
  - s1: Ohne Bedingung Kaskade (9 H0) und Abbruch bei 1,7 Perioden. Mit Bedingung 10 Perioden, langsames Heizen auf
    2,6e-3.
  - s3: Ohne Bedingung Abbruch beim ersten Ausnahmezug (0,12 Perioden), mit Bedingung 10 Perioden bei 7e-4.
  - Einschraenkung: Der s3-Abbruch ohne Bedingung ist ein Operatorfehler mit kleiner Energie (8e-5), keine
    Energiekaskade. Der Operator nach dem Zug ist aber genau der mit der starken Mode.
  - Die Momentaufnahme aus AG2 ("in s1 und s3 hilft es nicht") wird dynamisch nicht bestaetigt. Moegliche Erklaerung [H]:
    AG2 zaehlte mit demselben strengen Kriterium. Seine "1 wachsende" in s1 und s3 waeren dann die fast neutralen Moden
    (omega^2 ~ -1e-5), nicht die starke. Nicht nachgeprueft.
- **V3 (50 %): nicht eingetroffen.**
  - Die Zwangskraft liegt schon ohne Zuege bei 30 bis 38 % der Netzkraft (s2 bis s4), mit Zuegen bei 52 bis 88 %.
  - In der A_r-Metrik ist sie gleich gross wie die Netzkraft.
  - Nur s1 ohne Zuege bleibt unter 10 % (2,3 %).
  - Versteifung: in s1 bis s3 keine (omega_max mit Bedingung hoechstens so gross wie ohne). In s4 einmal das 1,45-Fache,
    in der Episode bei 2,4 Perioden.
- **Eigene Erwartungen (VORAB):**
  - E0a eingetroffen, E0b eingetroffen.
  - E1 falsch: s2 mit Bedingung bleibt beschraenkt.
  - E2 falsch: Die Bedingung stabilisiert s1 und s3.
  - E3 falsch: Die Zwangskraft liegt ueber 10 %.
  - E4 falsch: s4 bricht ohne Bedingung bei 7,2 Perioden ab; mit Bedingung gibt es eine 0,16-H0-Episode.

## 4. Was aus dem Aufbau folgt und was gerechnet ist

- Aus dem Aufbau [M]:
  - Bei festen Operatoren erhaelt die implizite Mitte H exakt. V0 prueft also vor allem die Umsetzung (Newton, Gradient,
    Bedingung), nicht die Physik.
  - V(x = 0) = \|det LV\| fuer jede Zerlegung.
  - Eine globale Bedingung senkt die Zahl negativer M_eff-Richtungen um hoechstens 1.
- Gerechnet [E]: alle Tabellenwerte. Insbesondere entfernt die Volumenbedingung die starke Mode in 133 von 133 Zuegen
  (s1 bis s3) bzw. 42 von 46 (s4), die Zufallsbedingung in s1 und s2 nicht.
- Nicht gezeigt: warum gerade das Volumen diese Richtung trifft. [H] Die starke Mode koennte eine Volumenmode der
  fast flachen neuen Tetraeder sein (konformer Anteil). Dazu passt, dass der Arm ohne Bedingung jedes Mal an "Metrik
  nicht positiv" scheitert. Nicht gerechnet.

## 5. Grenzen

- **Kein voller G2.** M_eff und B werden stueckweise nachgefuehrt (bei jedem Zug und je Periode am gedehnten Netz),
  ohne dM/dl in den Kraeften. Das weicht vom Kartenmodell ab; die Spruenge sind gebucht.
- Nur Lesart P, nur A = 1e-3, nur die Glasnetze s1 bis s4 (N = 128). Keine Lesart H (der Zusatz aus VORAB ist aus
  Zeitgruenden entfallen).
- Lesart der Bedingung: 3-Volumen fest (4-Volumen bei festem Takt), wie AG2 global. Ein echtes 4-Simplex-Volumen ist im
  Code nicht frei.
- Gegenprobe nur mit einem Zufallsvektor je Netz, nur s1 bis s3. Sie ist erst nach den ersten Zwischenergebnissen
  dazugekommen, also eine Zusatzvorgabe und kein Vorab-Test.
- Zwangskraft-Statistik (rms) nur ueber den letzten Abschnitt je Lauf (s1, s2, s3, s4 mit Bedingung liefen in 2 bis 4
  Abschnitten).
- Die Restdrift von 2,9e-3 in s4 mit Bedingung ist nicht erklaert. Moegliche Ursachen [H]: grosser Multiplikator mal
  Rest der Bedingung, oder die Teilschritte an den Ereignissen.
- Literatur [L] aus dem Gedaechtnis: Henneaux/Teitelboim (unimodular). arXiv:2610.04692 (de Andrade, Neves, Correa
  Silva) nur als [S Abstract]: Es beschreibt einen formalen Hamilton- und Lagrange-Aufbau fuer Systeme mit Bedingungen
  (Barcelos-Wotzasek). Einen numerischen Integrator enthaelt der Abstract nicht; nicht verwendet.

## 6. Regelabweichungen und Pannen

- Lokal kein python, awk oder perl; nur ls, cat, sed, grep auf einzelne eigene Dateien, jq, sha256sum, ssh und scp. Kein
  grep ueber Projektordner.
- Kein /tmp, /dev/null oder /dev/shm von mir gewaehlt. Die Werkzeug-Hintergrundaufrufe schreiben ihre Ausgabe in den
  Sitzungsordner unter /tmp/claude-1000 (Harness).
- Skripte auf der .69 per scp neu angelegt, vor dem ersten Lauf (keine laufende Instanz).
  - vg2.py wurde nach dem Rauchtest und vor V0 lokal geaendert (A_r-gewichtete Kraftstatistik; Fassung 8f2910e5...
    beim Rauchtest, c0546f42... ab V0).
  - Die Gegenprobe ist eine neue Datei (vg2b.py, kette2.sh). Vorlagen fremder Agenten sind unveraendert.
- Panne: Die Fortsetzung von g-s1-b1 nach der Pause hat auf der .69 den Log von Abschnitt 1 (g-s1-b1-1.log)
  ueberschrieben, weil kette.sh nach Abschnittsnummer benennt.
  - Der urspruengliche Log liegt nur lokal (lauf-69/g-s1-b1-1.log, vorher geholt) und steht nicht in der .69-Liste.
  - Der Fortsetzungs-Log liegt lokal als g-s1-b1-4-fortsetzung.log.
- Die erste Laufkette lief mit hoechstens 3 Abschnitten. g-s1-b1 brauchte 4; der vierte Abschnitt lief nach der Pause.
- Kein Journal, kein Peerbus, kein Commit.

## 7. Dateien und Pruefsummen

- Code lokal code/, auf der .69 /home/fmh/fmhc-physics-remote/volumen-g2-1/code/: vg2.py, vg2b.py (Gegenprobe),
  kette.sh, kette2.sh, Listen, zus.jq (nur lokal, Auswertung). Hochgeladene Dateien: UPLOAD-SHA256.txt, auf der .69
  gegengeprueft.
- Ergebnisse: lauf-69/ (V0, Hauptlaeufe, Gegenprobe, Rauchtest, Logs, Kettenprotokolle).
- lauf-69/PRUEFSUMMEN.txt: auf der .69 erzeugt, 61 Dateien. Lokal mit sha256sum -c geprueft (PRUEFSUMMEN-pruef.txt, gleiche
  Summen, Fortsetzungslog unter lokalem Namen): 61 OK.

## 8. Einfach gesagt

Wir haben das Netz beim Umklappen schwingen lassen und dabei sein Gesamtvolumen festgehalten, mit einem Rechenverfahren,
das Energie und Volumen sehr genau erhaelt. Ohne diese Bedingung entsteht nach bestimmten Umklappzuegen eine extrem schnell
wachsende Verformung, und jede Rechnung bricht ab; mit der Bedingung verschwindet sie in drei von vier Netzen ganz, und die
Rechnung laeuft zehn Schwingungen durch. Der Haken: Die Haltekraft der Bedingung ist so gross wie die Kraefte des Netzes
selbst, und im vierten Netz gibt es trotzdem einen grossen Energiesprung, die Bedingung hilft also deutlich, ist aber
kein sanfter Zusatz.
