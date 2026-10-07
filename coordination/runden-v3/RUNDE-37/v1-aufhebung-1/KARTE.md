# V1-AUFHEBUNG-1: Verschwindet der Abstrahlungsfehler auf Finns Netz V, wenn die Energie der Sterne mitgerechnet wird? (Runde 48, Fast Lane nach GLAS-STRAHLUNG-1)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 10:24:30 CEST (date), vor jeder Rechnung.
- **Herkunft [P]:** GLAS-STRAHLUNG-1 (RUNDE-37/glas-strahlung-1/ERGEBNIS.md), Nebenbefund auf V, nicht eigens gegengelesen.
  - Rechnet man bei Kreisbahnen den Energiekanal V1 mit (Quelle V1 + Spannung + Impuls J), heben sich nn-Leck und V1 auf V mit J_iso fast auf.
  - Die Lagenabhaengigkeit von G_rad/G_N liegt dann bei 0,999985 bis 1,000003 statt +-0,15 %, 9- bis 11-mal unter der Doppelpulsar-Schranke 1,3e-4. Das ist stabil bei kleinem k (Nachtrag kl = 0,005 bis 0,04).
  - Mit J = 1 hebt es sich nicht auf.
  - "12-mal ueber dem Doppelpulsar" (IMPULS-NETZ-1, SKALAR-SEKTOR-L, SKALAR-MISCH-1) beruhte auf Bahnen ohne V1.
- **Dazu:** SKALAR-MISCH-1 fand auf V einen exakt TT-isotropen Gewichtspunkt (Kegel 0,0214, Sechseck 1,141 relativ zu Finn; Spanne 3,7e-11; stabil an 511 k). Den Gang rechnete es ohne V1.
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Ableitbarkeitsprobe (Leitung, Bausteine verkettet)

- **Kette [L, ES]:**
  - In der linearisierten ART strahlt nur der TT-Anteil einer **erhaltenen** Quelle (Energie, Impuls und Spannung zusammen); Laengs- und Spurteile heben sich dort wegen der Erhaltung auf [L].
  - Mit V1, Spannung und J ist die Quelle auf dem Netz vollstaendig. Der Rest der Lagenabhaengigkeit sollte dann nur von der Richtungsabhaengigkeit der TT-Ausbreitung kommen: J_iso hat 1,1e-5 und ergibt einen Rest der Ordnung 1e-5, passend zu 0,999985 bis 1,000003.
  - **Vorhersage der Kette:** Am exakt isotropen Punkt aus SKALAR-MISCH-1 faellt der Rest mit V1 weiter, bis zur Rechengenauigkeit oder bis zu einem Gitterrest der Ordnung (kl)^2.
- **Nicht ableitbar:**
  - ob die Kette auf dem Netz gilt (Erhaltung der Netzquelle; nn-Kanal)
  - wie gross ein Gitterrest bei endlichem kl ist
  - ob der Rest wirklich mit der TT-Spanne skaliert
- **Kennzahlen-Abgleich:** Netz V, Gewichtspunkte J_iso (TT-ISO-1) und SKALAR-MISCH-1-Punkt; kein neues Netz.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| VA0 | Kontrolle: Unabhaengige Nachrechnung des Nebenbefunds auf V mit J_iso und V1 gibt 0,999985 bis 1,000003 (auf 2e-6) fuer dieselben Bahnen | 85 % |
| VA1 | [ES-Kette] Am exakt isotropen Punkt (SKALAR-MISCH-1) ist mit V1 die Lagenabhaengigkeit unter 1e-6 | 55 % |
| VA2 | Kontrolle: Mit J = 1 und V1 bleibt die Lagenabhaengigkeit ueber 1e-3 (GLAS-STRAHLUNG-1: keine Aufhebung) | 80 % |
| VA3 | [H] Ueber die Gewichtskurve "E-Masse = T2-Masse" aus SKALAR-MISCH-1 waechst der Rest mit V1 ungefaehr proportional zur TT-Spanne (Korrelation mindestens 0,9 auf mindestens 5 Punkten) | 50 % |

**Bedeutung (vorab):**
- **VA0 und VA1 treffen ein:** Auf Finns Kristallnetz mit passend gewaehlten Traegheiten sind GW170817 (Isotropie) und der Doppelpulsar (Abstrahlung) zugleich erfuellt. Der fruehere Befund "12-mal ueber dem Doppelpulsar" war eine Folge der unvollstaendigen Quelle. Die Gewichte bleiben eine Abstimmung, wenn auch an einem einzigen Punkt.
- **VA3 trifft ein:** Die Restleckage ist nur eine Folge der TT-Anisotropie. Wer die Isotropie loest, loest auch den Doppelpulsar.
- **VA0 verfehlt:** Der Nebenbefund haelt nicht. Dann wird er in GLAS-STRAHLUNG-1 als Berichtigung vermerkt.

## Rahmen

- Code-Agent. Code aus glas-strahlung-1/code (inkl. Nachtraege), impuls-netz-1/code und skalar-misch-1/code kopieren, dort nichts aendern.
- Unabhaengigkeit: VA0 nicht durch blosses Wiederabspielen der Nachtrag-Dateien. Den Aufbau aus PLAN und Code nachvollziehen, die V1-Quelle selbst pruefen (Formel, Vorzeichen, Normierung) und dann rechnen.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren p4000a und p4000b, sonst cpu und cpu7. Je Lauf hoechstens 10 min. Zeitbox 120 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
- Synthetisch, keine Messdatenbestaetigung.
