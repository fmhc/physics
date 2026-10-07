# NETZ-C-1: Ergebnis (Code-Agent fuer die Leitung, Runde 35, explorativ)

- Gerechnet auf der .69 ueber kleintest.sh, nur Spuren cpu3 und cpu4, hoechstens zwei Laeufe zugleich. cpu6 lief nie.
- Ablauf (Zeiten per date):
  - Start 20:48:56 CEST. Plan ab 21:09:30 CEST.
  - Rauchlauf 1 19:08:48 bis 19:08:56 UTC, ohne Ergebnisgroessen. Rauchlauf 2 19:12:31 bis 19:13:34 UTC.
    Zeitschritt-Rauch um 19:15 UTC.
  - Eingefroren 21:17:15 CEST: PLAN.md.eingefroren-20261003-211715, code/*.eingefroren-20261003-211715, sha256 in
    code/pruefsummen-einfrieren.txt.
  - Hauptlaeufe ab 19:17:15 UTC. Teil A fertig 19:18:19 UTC. Teil B 19:17:15 bis 19:47:42 UTC, alle rc = 0.
  - Auswertung 19:47:58 bis 19:48:09 UTC.
  - Text ab 21:49:52 CEST.
- Alle Laeufe tragen die sha256 der eingefrorenen Skripte (kette.py f371f6df..., netz_a.py af5db850...).
- Daten:
  - lauf-69/: Laufausgaben; netz_a.json/.npz; je Kettenlauf .json, .npz und .log
  - lauf-69/auswertung.json: Urteile
  - rauch-69/: Rauchlaeufe
- Code:
  - eingefroren: code/netz_a.py (Teil A), kette.py (Teil B), auswertung.py, laeufe.sh
  - nur fuer den Rauch: rauch1.sh, rauch2.sh, vergleich.py
- Kennzeichen: [M] vorab ableitbar, [L] Literatur aus dem Gedaechtnis, [L?] unsicher erinnert, [H] Hypothese,
  [E] hier gerechnet.

## 1. Ergebnis

1. **Kein steifes Stabnetz hat eine einzige Wellengeschwindigkeit [E].**
   - In jeder der 403 Richtungen ist die schnellste akustische Welle mindestens 1,27-mal so schnell wie die
     langsamste:
     - fcc-Z 1,414; fcc mit Winkelfedern 1,315; Pyrochlor 1,275; Diamant 1,487.
   - Laengs [110] haben alle steifen Netze zwei verschiedene Querwellen, also Doppelbrechung.
   - Die Querwellen koennen fast isotrop werden: fcc mit Winkelfedern schwankt nur um 5,9 % und 8,7 %, Diamant um
     8,1 % und 5,2 %.
   - Das einzige Netz mit genau einer richtungsfreien Geschwindigkeit ist Diamant mit Zentralfedern (0,4714 in allen
     Richtungen). Dort gibt es aber nur Laengswellen; die Querwellen haben Geschwindigkeit 0, wie in einer Fluessigkeit.
2. **Winkelfedern machen nicht jedes Netz steif [E].**
   - fcc, Pyrochlor und Diamant werden steif. srs (Grad 3) behaelt einen exakten Nullast laengs [110], auf Linien im
     k-Raum.
   - Pyrochlor mit Zentralfedern hat exakte Nullaeste in [100], [110] und [111]. Alle Nullmoden liegen auf den Ebenen
     senkrecht zu den geraden Stablinien. Das war vorab ableitbar [M].
3. **Fehlstellen werden relativistisch, aber nur bis zu einer Grenze, die vom Gitter kommt [E].**
   - Bei h = 0,1 und v <= 0,71 treffen Endgeschwindigkeit und Verkuerzung die Relativitaet auf 0,1 % bzw. 0,25 %.
   - Bei v = 0,94 ist der Kink schon 9 % schmaler, als seine Geschwindigkeit nach der Relativitaet verlangt.
   - Bei Sollwert v = 0,995 erreicht er nur 0,968.
4. **Ohne Reibung waechst gamma nicht ohne Grenze, sondern saettigt [E].**
   - Werte (aus der Energie): 1,78 / 2,61 / 3,86 bei h = 0,5 / 0,25 / 0,125. Im Kontinuum waeren es am Laufende
     13 / 26 / 52.
   - Danach laeuft der Kink mit fester Geschwindigkeit, 1 - v = 0,42 h bis 0,45 h. Die gesamte Kraftleistung
     2 pi F v geht als Gitterwellen verloren (auf 0,03 % nachgerechnet).
   - Kein Kink war je schneller als 1. Der schnellste Fensterwert war 0,968.
5. **Vorhersagen:**
   - eingetroffen: P0, P1, P2, K0, K3, K4, K5
   - nicht eingetroffen: P3 (srs bleibt beweglich; fcc und Diamant mit Winkelfedern schwanken unter 10 %), K1 (q = 10:
     2,7 % zu langsam), K2 (q = 3: gamma 9 % zu gross)
   - Keine Konvergenzprobe gibt ein anderes Urteil.

## 2. Urteile

Mechanisch nach PLAN.md (eingefroren 21:17:15 CEST) durch code/auswertung.py; Werte in lauf-69/auswertung.json.

| Nr | Vorhersage (Kurzform) | Wahrsch. | Urteil | Werte |
|---|---|---|---|---|
| P0 | fcc-Kontrolle 1e-4; Nullmoden = Maxwell | 95 % | **eingetroffen** | groesste Abweichung 3,5e-8 von den geschlossenen Formen; [110]-Polarisationen 1,000; generisch N0 = 0/0/2/6 = max(0, 3n - b) fuer fcc/Pyrochlor/Diamant/srs; fcc ohne Nullmode an allen 4095 k ungleich 0, N0(0) = 3 |
| P1 | jedes steife Netz in jeder Richtung >= 2 Geschwindigkeiten, Verhaeltnis >= 1,15 | 90 % | **eingetroffen** | steif: fcc-Z, fcc-W1, Pyrochlor-W1, Diamant-W1. Kleinstes Ast 3/Ast 1: 1,4142 [100], 1,3152 [111], 1,2748 [100], 1,4867 [100]. Variante W2: 1,4142 / 1,3009 / 1,3874 |
| P2 | Pyrochlor-Z: ein akustischer Ast mit c < 1e-6 in einigen Richtungen | 60 % | **eingetroffen**, vorab ableitbar [M] | Nullaeste in [100] (2), [110] (1), [111] (3), c < 1e-13; in den 400 Fibonacci-Richtungen keiner. Translationsanteil der Nullaeste 1/3 ([100], [110]) bzw. 0,34 bis 0,49 ([111]): gemischt aus Verschiebung und Tetraeder-Gegendrehung |
| P3 | mit Winkelfedern alle steif, jeder Querast schwankt >= 10 % | 70 % | **nicht eingetroffen** | srs-W1 nicht steif (Nullast laengs [110]); Schwankung der Queraeste fcc-W1 5,9 % / 8,7 %, Diamant-W1 8,1 % / 5,2 % (Pyrochlor-W1 29,8 % / 17,1 %). W2 gibt dasselbe Urteil (fcc-W2 4,2 % / 2,7 %) |
| K0 | Energie 1e-6 ohne Kraft und Reibung; v_g,max < 1 | 95 % | **eingetroffen** | H-Abweichung 2,7e-9 (h = 0,1), 2,3e-8 (h = 1); v_g,max = 0,951 / 0,618 / 0,781 / 0,883 / 0,939 fuer h = 0,1 / 1 / 0,5 / 0,25 / 0,125 |
| K1 | h = 0,1: Endgeschwindigkeit innerhalb 2 % von gamma v = pi F/(4 eta) | 80 % | **nicht eingetroffen** | -0,06 % / -0,09 % / -0,82 % / **-2,72 %** fuer q = 0,3 / 1 / 3 / 10 (v_end 0,2872 / 0,7065 / 0,9409 / 0,9679) |
| K2 | h = 0,1, v <= 0,95: gamma (Steigung) innerhalb 3 % von 1/sqrt(1 - v^2) | 75 % | **nicht eingetroffen** | +0,05 % / +0,25 % / **+9,0 %** fuer q = 0,3 / 1 / 3 (gamma 3,220 gegen 2,953). Aus der Energie: -0,05 % / +0,05 % / +4,5 % |
| K3 | kein Kink schneller als 1 (Fensterschnelle <= 1,001) | 95 % | **eingetroffen** | groesster Wert 0,9679 (h = 0,1, q = 10); K4: 0,7775 / 0,8929 / 0,9473 |
| K4 | ohne Reibung gamma bis zu einer Grenze, steigend mit 1/h; gamma_max h in [0,3; 5] | 55 % | **eingetroffen** | gamma_max (Energie) 1,781 / 2,614 / 3,861; gamma_max h = 0,890 / 0,653 / 0,483; alle drei gesaettigt (Steigung im letzten Viertel <= 1,5e-6 gegen Schwelle 3,9e-3); keine Zerstoerung |
| K5 | h = 1, q = 10: Endgeschwindigkeit >= 10 % unter Kontinuum | 50 % | **eingetroffen** | v_end = 0,6814 gegen 0,9950, also 31,5 % darunter |

- **Bedeutung, wie vorab festgelegt:**
  - "K1 bis K3 treffen ein" ist nicht ausgeloest, weil K1 und K2 nicht eingetroffen sind.
    - Beschreibend: Fehlstellen verhalten sich bei kleinem gamma relativistisch, mit der Netzgeschwindigkeit 1 als c
      (Abschnitt 3, B1).
    - Bei gamma h ~ 0,3 bis 0,5 bricht das schon sichtbar.
  - "P1 und P3 treffen ein" ist nicht ausgeloest, weil P3 nicht eingetroffen ist.
    - P1 allein sagt schon: Kein steifes Netz hat eine einzige richtungsfreie Geschwindigkeit. Zwischen schnellster
      und langsamster Welle liegt in jeder Richtung mindestens der Faktor 1,27.
    - Das Licht in einer solchen Welt waere doppelbrechend und richtungsabhaengig, um Prozente.
    - LORENTZ.md: Anisotropie Delta c/c ~ 1e-17 (Herrmann et al. 2009), Photonsektor bis 1e-22. Das ist 15 bis 20
      Groessenordnungen darunter.
  - "K4 trifft ein" ist ausgeloest: Die Relativitaet gilt nur oberhalb der Gitterskala; sehr schnelle Fehlstellen
    merken das Gitter. Das gemessene gamma_max h faellt allerdings mit h (0,89 / 0,65 / 0,48), ist also nicht fest.
  - "P2 trifft ein" ist ausgeloest: Das eckverknuepfte Tetraedernetz liegt an der Grenze zur Beweglichkeit; seine
    Wellengeschwindigkeit verschwindet in [100], [110] und [111]. Das war aus EIS-1 und dem Indexsatz vorab ableitbar
    [M], die Rechnung bestaetigt nur den Code.

## 3. Tabellen

### Teil A

#### Tabelle A1: akustische Geschwindigkeiten in den Symmetrierichtungen (|k| = 1e-3) [E]

- Einheiten:
  - Kantenlaenge 1, Masse 1, Federsteifigkeit 1, k_theta = 0,1
  - Geschwindigkeit in Kanten je sqrt(m/k)
- Aeste 1, 2, 3 = die drei kleinsten Singulaerwerte, nach Groesse sortiert (PLAN 2.3). "0" heisst c < 1e-12.
- Federarten:
  - Z = nur Zentralfedern
  - W1 = Z plus Winkelfeder d(cos theta), Hauptmodell
  - W2 = Z plus Keating-Form d(r_ij . r_il), Variante
- tau = Translationsanteil (1 = reine Verschiebung der ganzen Zelle). Angegeben nur, wo er nicht 1 ist.

| Netz | Feder | [100] Ast 1 / 2 / 3 | [110] Ast 1 / 2 / 3 | [111] Ast 1 / 2 / 3 |
|---|---|---|---|---|
| fcc | Z | 0,7071 / 0,7071 / 1,0000 | 0,5000 / 0,7071 / 1,1180 | 0,5774 / 0,5774 / 1,1547 |
| fcc | W1 | 1,0488 / 1,0488 / 1,5492 | 1,0488 / 1,1402 / 1,4832 | 1,1106 / 1,1106 / 1,4606 |
| fcc | W2 | 1,3784 / 1,3784 / 1,9494 | 1,3229 / 1,3784 / 1,9875 | 1,3416 / 1,3416 / 2,0000 |
| Pyrochlor | Z | 0 / 0 / 0,5000 (tau 1/3, 1/3, 0) | 0 / 0,3536 / 0,4012 (tau 1/3, 0, 0,25) | 0 / 0 / 0 (tau 0,37; 0,34; 0,49) |
| Pyrochlor | W1 | 0,6325 / 0,6325 / 0,8062 | 0,4873 / 0,6325 / 0,9014 | 0,5401 / 0,5401 / 0,9310 |
| Pyrochlor | W2 | 0,8062 / 0,8062 / 1,0488 | 0,6124 / 0,8062 / 1,1726 | 0,6831 / 0,6831 / 1,2111 |
| Diamant | Z | 0 / 0 / 0,4714 | 0 / 0 / 0,4714 | 0 / 0 / 0,4714 |
| Diamant | W1 | 0,4558 / 0,4558 / 0,6777 | 0,4216 / 0,4558 / 0,6995 | 0,4333 / 0,4333 / 0,7066 |
| Diamant | W2 | 0,5040 / 0,5040 / 0,6992 | 0,4216 / 0,5040 / 0,7517 | 0,4508 / 0,4508 / 0,7684 |
| srs | Z | 0 / 0 / 0 (6 Nullaeste) | 0 / 0 / 0 | 0 / 0 / 0 |
| srs | W1 | 0,3397 / 0,3397 / 0,3922 (tau 1, 1, 0) | 0 / 0,2182 / 0,5189 (tau 0,57; 1; 0,43) | 0,2494 / 0,2650 / 0,2650 (tau 0,26; 1; 1) |
| srs | W2 | 0,3651 / 0,3652 / 0,4216 (tau 1, 1, 0) | 0 / 0,2236 / 0,5578 | 0,2717 / 0,2789 / 0,2789 |

- **fcc-Z in c0 = 0,70711:**

  | Richtung | Ast 1 | Ast 2 | Ast 3 |
  |---|---|---|---|
  | [100] | 1 | 1 | 1,41421 |
  | [110] | 0,70711 | 1 | 1,58114 |
  | [111] | 0,81650 | 0,81650 | 1,63299 |

  - Das ist die Tabelle der Karte. Die groesste Abweichung von den geschlossenen Formen ist 3,5e-8.
  - Polarisation laengs [110]: Ast 1 steht auf [1-10], Ast 2 auf [001], je mit Ueberlapp 1,000.
- **Pyrochlor-Z, die sechs untersten Aeste:**

  | Richtung | sechs unterste Aeste | tau |
  |---|---|---|
  | [100] | 0; 0; 0,5; 0,6124; 0,6124; 0,7071 | 1/3; 1/3; 0; 2/3; 2/3; 1 |
  | [110] | 0; 0,3536; 0,4012; 0,4330; 0,5; 0,8812 | |
  | [111] | 0; 0; 0; 0,6455; 0,6455; 0,8165 | |

  - Bei kleinem k gibt es sechs lineare Aeste statt drei: die drei Verschiebungen und die drei Gegendrehungen der
    Tetraeder. Das hatte die Schreibtischrechnung im Plan (Abschnitt 6) erwartet [H, jetzt E].
  - Der Laengsast laengs [100] ist 0,7071 = c_L(fcc)/sqrt 2.
- **srs-W1 laengs [100]:** Ast 3 (0,3922) hat tau = 0, ist also eine lineare optische Mode. Der eigentliche Laengsast ist
  der vierte (0,4797, tau = 1).

#### Tabelle A2: Anisotropie ueber 403 Richtungen, |k| = 1e-3 [E]

- Richtungen: [100], [110], [111] und 400 Fibonacci-Richtungen.

| Netz | Feder | steif | kleinstes Ast 3/Ast 1 (Richtung) | Schwankung max/min - 1 von Ast 1 / 2 / 3 | Ast 1 min..max | Ast 2 min..max | Ast 3 min..max |
|---|---|---|---|---|---|---|---|
| fcc | Z | ja | 1,4142 ([100]) | 41,4 % / 22,5 % / 15,5 % | 0,500..0,707 | 0,577..0,707 | 1,000..1,155 |
| fcc | W1 | ja | 1,3152 ([111]) | 5,9 % / 8,7 % / 6,1 % | 1,049..1,111 | 1,049..1,140 | 1,461..1,549 |
| fcc | W2 | ja | 1,4142 ([100]) | 4,2 % / 2,7 % / 2,6 % | 1,323..1,378 | 1,342..1,378 | 1,949..2,000 |
| Pyrochlor | Z | nein (Nullaeste in 3 Richtungen) | - | - | 0..0,228 | 0..0,354 | 0..0,500 |
| Pyrochlor | W1 | ja | 1,2748 ([100]) | 29,8 % / 17,1 % / 15,5 % | 0,487..0,632 | 0,540..0,632 | 0,806..0,931 |
| Pyrochlor | W2 | ja | 1,3009 ([100]) | 31,7 % / 18,0 % / 15,5 % | 0,612..0,806 | 0,683..0,806 | 1,049..1,211 |
| Diamant | Z | nein (2 Nullaeste ueberall) | - | Ast 3: 0 % (isotrop) | 0 | 0 | 0,4714..0,4714 |
| Diamant | W1 | ja | 1,4867 ([100]) | 8,1 % / 5,2 % / 4,3 % | 0,422..0,456 | 0,433..0,456 | 0,678..0,707 |
| Diamant | W2 | ja | 1,3874 ([100]) | 19,5 % / 11,8 % / 9,9 % | 0,422..0,504 | 0,451..0,504 | 0,699..0,768 |
| srs | Z | nein (6 Nullmoden je k) | - | - | 0 | 0 | 0 |
| srs | W1 | nein (Nullast laengs [110]) | (1,0624 bei [111]) | - | 0..0,340 | 0,218..0,340 | 0,265..0,519 |
| srs | W2 | nein (Nullast laengs [110]) | (1,0266 bei [111]) | - | 0..0,365 | 0,224..0,365 | 0,279..0,558 |

- Die Verfeinerung (Nelder-Mead) findet die Extremwerte in den Symmetrierichtungen. Sie aendert keine Zahl um mehr
  als 1e-8.
- Linearitaet: c(2e-3)/c(1e-3) liegt fuer alle Aeste mit c > 0 zwischen 0,9999995 und 1,0000002.
  - Ausnahme srs-W1/W2 mit +-5e-5, weil dort eine lineare optische Mode nahe liegt (Luecke c4/c3 = 1,05).
- Doppelbrechung laengs [110]: Alle steifen Netze haben dort zwei verschiedene Queraeste, z. B. fcc-W1 1,0488 und
  1,1402, Diamant-W1 0,4216 und 0,4558.

#### Tabelle A3: Nullmoden [E]

| Netz | Feder | Maxwell 3n - b | generisch N0 (64 Punkte) | Gitter 16^3: Punkte mit N0 > 0 | Gitter 12^3 | N0 bei k = 0 |
|---|---|---|---|---|---|---|
| fcc | Z | -3 | 0 | 0 von 4095 | 0 von 1727 | 3 |
| Pyrochlor | Z | 0 | 0 | 1365 von 4095 (N0 = 1: 1260, 2: 45, 3: 60) | 737 von 1727 | 6 |
| Diamant | Z | 2 | 2 | alle 4095 mit N0 = 2 | alle mit 2 | 3 |
| srs | Z | 6 | 6 | alle 4095 mit N0 = 6 | alle mit 6 | 7 |
| fcc, Pyrochlor, Diamant | W1, W2 | - | 0 | 0 | 0 | 3 |
| srs | W1, W2 | - | 0 | 91 von 4095 (N0 = 1) | 67 von 1727 | 4 |

- **Pyrochlor-Z, Lage im k-Raum:**
  - Alle 1365 Nullpunkte (12^3: alle 737) liegen auf Ebenen k . T_e in 2 pi Z. Diese stehen senkrecht zu einer
    <110>-Stablinie.
  - An jedem dieser Punkte ist N0 genau die Zahl dieser Ebenen.
  - Die Zahl waechst wie N^2 (737/144 = 5,1; 1365/256 = 5,3), wie es fuer Ebenen sein muss.
- **srs-W1/W2:** Die Nullpunkte wachsen etwa wie N (67 bei 12, 91 bei 16). Sie liegen also auf Linien im k-Raum,
  darunter die [110]-Linie durch k = 0.
- **Abstand der Nullschwelle:**
  - Als null gezaehlt: s/|k| <= 2e-15.
  - Kleinstes nicht null gezaehltes s/|k|: 0,039 (srs-W1), sonst >= 0,069.

### Teil B

#### Tabelle B1: Endgeschwindigkeit und gamma unter Kraft und Reibung (eta = 0,01, Start aus der Ruhe) [E]

- Spaetes Fenster t in [800, 1000], dt1. Die Probe mit dt2 trifft alle v_end auf 1,3e-6 und alle gamma auf 1e-4.
- Formeln:
  - q = pi F/(4 eta), v_soll = q/sqrt(1 + q^2), gamma_v = 1/sqrt(1 - v_end^2)
  - gamma_St = Steigung (Parabelscheitel)/2, gamma_E = Energie im Fenster/8
  - E aussen = Energie ausserhalb des Fensters [X - 4, X + 4] (Abstrahlung), Mittel ueber das spaete Fenster

| h | q | F | v_soll | v_end | v_end/v_soll - 1 | gamma_v | gamma_St (rel. zu gamma_v) | gamma_E (rel.) | E aussen |
|---|---|---|---|---|---|---|---|---|---|
| 0,1 | 0,3 | 0,00382 | 0,28735 | 0,28718 | -0,06 % | 1,0440 | 1,0445 (+0,05 %) | 1,0434 (-0,05 %) | 0,003 |
| 0,1 | 1 | 0,01273 | 0,70711 | 0,70648 | -0,09 % | 1,4130 | 1,4165 (+0,25 %) | 1,4136 (+0,05 %) | 0,0002 |
| 0,1 | 3 | 0,03820 | 0,94868 | 0,94091 | -0,82 % | 2,9528 | 3,2199 (+9,0 %) | 3,0847 (+4,5 %) | 0,58 |
| 0,1 | 10 | 0,12732 | 0,99504 | 0,96793 | -2,72 % | 3,9804 | 4,8116 (+20,9 %) | 6,5156 (+63,7 %) | 27,2 |
| 1 | 0,3 | 0,00382 | 0,28735 | 0,15612 | -45,7 % | 1,0124 | 1,0366 | 1,0086 | 0,08 |
| 1 | 1 | 0,01273 | 0,70711 | 0,39614 | -44,0 % | 1,0891 | 1,1438 | 1,0932 | 1,6 |
| 1 | 3 | 0,03820 | 0,94868 | 0,53819 | -43,3 % | 1,1865 | 1,2857 | 1,2657 | 9,3 |
| 1 | 10 | 0,12732 | 0,99504 | 0,68141 | -31,5 % | 1,3663 | 1,5188 | 1,8031 | 45,7 |

- **Lesart [H]:**
  - Bei q = 3 und h = 0,1 erfuellt der Kink die Energiebilanz mit seiner Form: gamma_St v = 3,22 x 0,941 = 3,03
    gegen q = 3. Sein Profil ist so steil, wie es die Bilanz verlangt.
  - Seine Geschwindigkeit bleibt aber unter dem relativistischen Wert fuer dieses Profil (0,941 statt 0,950).
  - Eine moegliche Deutung: Die kurzen Wellenanteile des Kinks laufen auf dem Gitter langsamer als 1
    (sin(kh/2)/(kh/2) < 1). Fuer den Kink wirkt dann ein "c" von etwa 0,991.
  - Bei q = 10 traegt die Abstrahlung (E aussen = 27) den groessten Teil der Kraftleistung.
- **h = 1:** Der Kink bewegt sich bei allen vier Kraeften (nicht festgehalten), aber 31 % bis 46 % langsamer als im
  Kontinuum.

#### Tabelle B2: ohne Reibung, F = 0,02, Start aus der Ruhe (K4) [E]

| h | t_end | gamma_max (Energie) | gamma_max h | gamma_max (Steigung) | Endschnelle v | 1 - v | v_g,max des Gitters | Steigung gamma_E im letzten Viertel | E aussen / E gesamt am Ende | gamma Kontinuum bei t_end |
|---|---|---|---|---|---|---|---|---|---|---|
| 0,5 | 828 | 1,781 | 0,890 | 1,814 | 0,7775 | 0,2225 | 0,7808 | +1,5e-6 | 71,5 / 85,7 | 13,0 |
| 0,25 | 1656 | 2,614 | 0,653 | 2,578 | 0,8929 | 0,1071 | 0,8828 | -5,2e-7 | 168,4 / 189,3 | 26,0 |
| 0,125 | 3312 | 3,861 | 0,483 | 3,645 | 0,9473 | 0,0527 | 0,9395 | -1,2e-7 | 365,9 / 396,7 | 52,0 |

- Zerstoerung: keine (ncross = 1, Kinkort stetig, Fensterenergie > 4 bis zum Ende).
- Probe dt2: gamma_max 1,781 / 2,614 / 3,861, Abweichung <= 5e-5. Endschnellen gleich auf 3e-6.
- **Verlauf gamma_E gegen Kontinuum sqrt(1 + (pi F t/4)^2):**

  | t | Kontinuum | h = 0,5 | h = 0,25 | h = 0,125 |
  |---|---|---|---|---|
  | 100 | 1,862 | 1,707 | 1,856 | 1,861 |
  | 200 | 3,297 | 1,780 | 2,600 | 3,261 |
  | 400 | 6,362 | 1,780 | 2,613 | 3,859 |
  | 800 | 12,61 | 1,780 | 2,613 | 3,860 |
  | 1600 | 25,15 | - | 2,614 | 3,860 |
  | 3200 | 50,28 | - | - | 3,860 |

  - Der Kink folgt der relativistischen Kurve, bis er die Grenze erreicht. Dann knickt der Verlauf scharf ab.
- **Energiebilanz im Endzustand:** Die Energie ausserhalb des Kinks waechst mit 0,09771 / 0,11220 / 0,11900 je
  Zeiteinheit. Das ist 2 pi F v = 0,09771 / 0,11220 / 0,11904. Alle zugefuehrte Leistung wird abgestrahlt.
- **Beobachtungen [E]:**
  - Die Endschnelle liegt bei h = 0,25 und 0,125 ueber der groessten Gruppengeschwindigkeit des Gitters, bei h = 0,5
    knapp darunter.
  - 1 - v ist ungefaehr 0,43 h.
  - gamma_max waechst etwa wie h^(-0,55), gamma_max h ist also nicht konstant.
- **Lesart [H], uebertragen:**
  - Waeren Teilchen Fehlstellen eines Netzes, muesste die Netzweite weit unter ihrer um gamma verkuerzten Breite
    liegen.
  - Das gilt bis zu den groessten beobachteten gamma (Protonen der kosmischen Strahlung bis gamma ~ 1e11 [L?]).

## 4. Kontrollen

- **fcc-Z gegen die geschlossenen Formen der Karte:** groesste Abweichung 3,5e-8, Polarisationen laengs [110] 1,000
  (P0).
- **Keating-Pruefung [L] (im Rauch, Plan Abschnitt 8):** Diamant-W2 ist das Keating-Modell.
  - Mit alpha = k/3 und beta = (4/3) k_theta liefern C11 = (alpha + 3 beta)/a und C44 = 4 alpha beta/(a(alpha + beta))
    die Werte 0,31754 und 0,16496.
  - Gerechnet rho c^2 laengs [100]: 0,31754 und 0,16495.
  - Damit sind die Winkelzeilen und die innere Relaxation richtig. Die Keating-Formeln sind aus dem Gedaechtnis; die
    Uebereinstimmung auf 5 Stellen stuetzt beide.
- **Maxwell und Indexsatz:**
  - Generisch ist N0 = max(0, 3n - b) fuer alle vier Zentralfedernetze.
  - Pyrochlor-Z: N0 an jedem Nullpunkt = Zahl der <110>-Ebenen durch diesen Punkt (1365 von 1365). Das passt zu den
    12 L^2 Linien-Eigenspannungen aus EIS-1.
- **Diamant-Z gegen Keating mit beta = 0 [M]:** Laengsast isotrop 0,4714 = sqrt(B/rho) mit B = 0,14434 aus der
  Stabzaehlung. Queraeste 0 ueberall.
- **Richtungen:** Verfeinerung (Nelder-Mead) gegen das 800er Gitter, Abweichung <= 1e-8. 400 gegen 800 Richtungen und
  |k| = 1e-3 gegen 2e-3 geben dieselben Urteile.
- **Linearitaet:** c(2e-3)/c(1e-3) = 1 +- 5e-7 (srs-W1/W2: +- 5e-5).
- **Integrator:**
  - Energieabweichung skaliert wie dt^4. Rauch h = 1: Faktor 16,0 je Halbierung.
  - Hauptlaeufe K4: Faktor 16,0 zwischen dt1 und dt2 bei allen drei h.
  - K0: 2,7e-9 und 2,3e-8 (dt1), 1,7e-10 und 1,5e-9 (dt2).
- **K4-Laeufe, H-Abweichung relativ zu |H(0)|:**
  - Werte: 1,9e-5 / 2,9e-4 / 3,9e-3 (dt1), 1,2e-6 / 1,8e-5 / 2,5e-4 (dt2).
  - |H(0)| ist dort nur ~1, weil der Term -F u die Kinkenergie fast aufhebt. Gegen die Gesamtenergie von 86 bis 397
    ist der Fehler <= 1e-5.
  - Die Urteilsgroessen aendern sich zwischen dt1 und dt2 um <= 5e-5.
- **Checkpoints:** Fortsetzung ueber 10 Abschnitte bitgleich zum ununterbrochenen Lauf (Rauch). Die Hauptlaeufe
  h = 0,125 liefen in 2 bzw. 3 Abschnitten.
- **Rand:** Kein Kink kam naeher als 30 an das rechte Ende (alle Status "fertig").
- **Schnelle-Messung:**
  - Die Zweipunkt-Schnelle (X-Differenz je 0,5) springt bei h = 1 bis 0,986 (K0) bzw. 0,846 (q = 10). Die
    Fensterschnelle ist 0,595 bzw. 0,682. Das ist der erwartete Stufeneffekt des interpolierten Kinkorts.
  - Die Fensterschnelle aus dem Schwerpunkt Xcm ist in den K0- und (1)-Laeufen hoechstens 0,972. Auch sie bleibt
    unter 1. Fuer die K4-Laeufe berechnet auswertung.py sie nicht.

## 5. Selbstanzeigen

1. **Spuren:** Die Leitung hat waehrend der Vorbereitung auf cpu3 und cpu4 umgestellt. Auf cpu6 lief nie etwas.
2. **Reihenfolge:**
   - Rauchlauf 1 (Netzbau, Zeitmessung, Fortsetzungstest) lief vor dem Plan; er zeigt keine Ergebnisgroessen.
   - Rauchlauf 2 lief nach dem Plan und vor dem Einfrieren, mit 20/40 Richtungen.
   - Ich sah dabei vor dem Einfrieren: P0-Pfad erfuellt; srs-W1 und srs-W2 nicht steif; Queraeste von fcc-W1 und
     Diamant-W1 unter 10 %, also P3 nicht eintreffend; P1-Verhaeltnisse >= 1,27; P2-Nullaeste mit tau = 1/3.
   - Keine Regel wurde danach geaendert (PLAN Abschnitt 8).
3. **Zeitschritt nach dem Rauch geaendert, vor dem Einfrieren:**
   - Geplant war dt = h/10 und h/20. Der K0-Rauch bei h = 1 gab mit h/10 eine Energieabweichung von 9,7e-5 (> 1e-6).
   - Festgelegt wurde dt1 = 0,0125 fuer h >= 0,125 (h = 0,1: 0,01), Probe dt2 = dt1/2.
   - Das ist eine numerische Festlegung, die Schwelle 1e-6 blieb. Damit traegt K0 aber eine nach einem Rauchlauf
     gewaehlte Schrittweite.
4. **Codeaenderungen:**
   - vor dem Einfrieren: NaN-Schutz in netz_a.py, Laufnamen in auswertung.py, Laufskript
   - nach dem Einfrieren: keine
5. **Modellwahl Winkelfeder [F]:**
   - Der Hinweis der Leitung ("Keating-artig ueber r_ij . r_il" und "kollineare Paare ohne linearen Term") passt nur
     fuer normierte Kantenvektoren.
   - Hauptmodell ist deshalb W1 = d(cos theta). Das woertliche Keating-Modell W2 ist Variante; seine Urteile fuer P1 und
     P3 sind dieselben.
6. **Sollwerte P0:** Verglichen wurde mit den geschlossenen Formen, nicht mit den dreistelligen Tabellenwerten. Deren
   Rundung allein (bis 6e-4) liegt ueber 1e-4.
7. **Ast-Regel:**
   - Als akustische Aeste zaehlen die drei kleinsten (Vorgabe der Leitung). Dazu gehoeren auch lineare optische Moden:
     Pyrochlor-Z [100] Ast 3 mit tau = 0, srs-W1 [100] Ast 3 mit tau = 0.
   - Die Nullaeste von Pyrochlor-Z sind gemischt (tau 1/3 bis 0,49), nicht reine Verschiebungen.
   - Bei einer Zaehlung nur nach Translationsanteil waere P2 nicht so klar.
8. **Vorab ableitbar [M]:**
   - P2 und die fcc-Teile von P0/P1 sind vorab ableitbar (Plan Abschnitt 6). Ihr "eingetroffen" prueft den Code, nicht
     die Physik.
   - Vorab ableitbar ist auch K0, Teil v_g,max < 1.
9. **gamma fuer K4:**
   - Das Urteil traegt gamma aus der Energie, weil gamma aus der Steigung den Deckel pi/h hat.
   - Der Deckel wurde nicht erreicht (gamma_St h <= 0,91), beide Masse geben dasselbe Urteil.
   - gamma_St und gamma_E unterscheiden sich bei grossem gamma deutlich: bei h = 0,1, q = 10 sind es 4,81 und 6,52.
     Der Kink ist dort kein starres sech-Profil mehr.
10. **Nicht gerechnet:** das optionale Tetraeder-Oktaeder-Fachwerk mit Zusatzdiagonalen (Zeitbox).
11. **Nebenlaeufe ueber kleintest.sh auf cpu3, nicht im Laufskript:**
    - Rauch: 7 Zeitschritt-Kurzlaeufe und 2 Vergleichslaeufe (vergleich.py)
    - die Auswertung selbst
12. **Startbefehl:** Die ssh-Sitzung, die laeufe.sh mit nohup startete, kehrte erst nach Laufende zurueck. Das hatte
    keine Wirkung auf die Laeufe.
13. **Zeitbox:** Start 20:48:56, Text ab 21:49:52 CEST; innerhalb von 120 min.

## 6. Einfach gesagt

Ein Netz aus Staeben leitet Wellen. Aber in jedem steifen Netz laeuft in jeder Richtung die schnellste Welle
mindestens 27 % schneller als die langsamste, und je nach Richtung aendert sich die Geschwindigkeit. Echtes Licht ist in allen Richtungen auf 17
Stellen gleich schnell, ein solches Netz waere also als Lichttraeger viel zu ungleichmaessig. Eine Fehlstelle, die
durch die Kette laeuft, benimmt sich bei kleiner Geschwindigkeit wirklich wie ein Teilchen in der Relativitaet: Sie
wird kuerzer und nie schneller als die Wellen. Wird sie aber so kurz wie der Abstand der Kettenglieder, strahlt sie
alle zugefuehrte Energie ab und wird nicht mehr schneller. Die Relativitaet gilt in einem Netz also nur, solange die
Teilchen viel groesser als die Maschen sind.
