# EINFANG-1: Faengt eine Fuenfer-Ecke einen laufenden Q-Ball ein? (Runde 34)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-03 17:49:53 CEST (date), vor jeder Rechnung.
- Anlass:
  - Finn 17:4x "weiter".
  - Offene Frage im Atlas ("Faengt eine Fuenfer-Ecke einen laufenden Q-Ball ein? Gerechnet sind nur Energien").
  - KEGEL-Q (R26): statische Bindung B = 1,45 bei Q = 200 (M1, beta = 1/2, 2D-Dreiecksnetz, h = 0,2), Reichweite etwa
    R_halb + 3.

## Schreibtisch (vor jeder Rechnung)

- Ohne Verluste kann ein Ball, der von weit her (Potential 0) mit kinetischer Energie K > 0 kommt, nicht eingefangen werden.
  Er laeuft durch die Mulde und verlaesst sie mit K.
- **Einfang braucht Verluste:** Abstrahlung oder Anregung innerer Moden (Atmung, Verformung). Diese muessen beim
  Durchgang groesser als K sein.
- **Zahlen bei Q = 200:**
  - E ~ 157,3, also K ~ (1/2) E v^2: 0,79 bei v = 0,1; 0,20 bei v = 0,05; 0,031 bei v = 0,02.
  - Am Muldengrund ist die Geschwindigkeit sqrt(2 (K + B)/E), also ~0,14 auch bei kleinem v.
  - Dauer des Durchgangs ~ 2 R_halb/v_Grund ~ 90.
  - Die Atmungsmoden des Balls haben Perioden in der Groessenordnung 10 bis 60. Der Durchgang ist also nicht streng
    adiabatisch, eine Anregung ist moeglich.
- **Siebener-Ecke** (B = -1,34, abstossend): Bei K < 1,34, also v < ~0,13, wird der Ball zurueckgeworfen. Das folgt aus
  der Energieerhaltung und ist eine Kontrolle.
- Ableitbarkeit:
  - EF1 (kein Einfang bei grossem v) ist nahezu ableitbar, weil die Verluste klein gegen K sein sollten.
  - EF2 (Einfang bei kleinem v) ist offen; das ist die eigentliche Frage.
  - Projekt-grep: Dynamik an Kegeldefekten wurde im Projekt nicht gerechnet.

## Test (Code-Agent)

- **Netz und Modell:** Dreiecksnetz mit Fuenfer- bzw. Siebener-Spitze aus KEGEL-Q (RUNDE-26/kegel-q/code/kegel_q.py,
  Kotangens-Laplace, Flaechengewichte), ebenes Netz als Kontrolle. M1, beta = 1/2, Q = 200.
- **Zeitentwicklung:**
  - phi'' = Laplace(phi) - U'(|phi|^2) phi, explizit (Leapfrog/Stoermer-Verlet) mit Massenmatrix aus den Flaechen
  - Absorbierender Rand (Schwamm) gegen Rueckstrahlung
  - Gitterweite und Zeitschritt nach Stabilitaets- und Konvergenzprobe; zwei Gitterweiten oder zwei Zeitschritte.
- **Start:** statischer Q-Ball (aus dem KEGEL-Q-Loeser auf dem ebenen Netz), naeherungsweise geboostet,
  phi = f(gamma(x - x0)) exp(i omega gamma (t - v x)) bzw. die Netzfassung davon.
  - Start bei x0 = -25 (weit ausserhalb der Reichweite), Kurs frontal auf die Spitze (Stossparameter 0).
- **Geschwindigkeiten:** v = 0,02, 0,05, 0,1 an der Fuenfer-Ecke; v = 0,05 an der Siebener-Ecke; v = 0,05 ohne Defekt.
- **Messgroessen:**
  - Bahn des Ladungsschwerpunkts
  - Energie und Ladung im Ball, abgestrahlte Energie am Schwamm
  - Austrittsgeschwindigkeit
  - "Eingefangen" heisst: Der Schwerpunkt bleibt bis Laufende (mindestens zwei Durchgaenge durch die Spitze bzw. T so
    lang, dass ein freier Ball laengst draussen waere) innerhalb R_halb + 3 der Spitze.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| EF0 | Kontrolle ohne Defekt, v = 0,05: Geschwindigkeit nach t = 400 innerhalb 5 % erhalten, Ladung innerhalb 1 % | 85 % |
| EF1 | Fuenfer-Ecke, v = 0,1 und v = 0,05: kein Einfang, der Ball verlaesst die Mulde | 70 % |
| EF2 | Fuenfer-Ecke, v = 0,02: Einfang (Verlust beim ersten Durchgang groesser als K = 0,031) | 40 % |
| EF3 | Siebener-Ecke, v = 0,05: Der Ball wird vor der Spitze zurueckgeworfen | 90 % |

**Bedeutung (vorab):**
- EF2 trifft ein: Geometrische Defekte koennen langsame Q-Baelle einfangen, Verluste ueber innere Moden bzw. Abstrahlung
  [H]. Q-Baelle in einem Tetraeder- oder Ikosaederraum wuerden sich an Fuenfer-Stellen sammeln.
- EF2 trifft nicht ein: Die Haftung ist bei diesen Geschwindigkeiten rein statisch. Einfang braucht dann zusaetzliche
  Reibung. Beschreiben, wie gross der Verlust je Durchgang war.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh (CPU- oder P4000-Spur; je <= 10 min).
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
