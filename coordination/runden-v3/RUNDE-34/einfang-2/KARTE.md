# EINFANG-2: Bremsen viele Fuenfer-Ecken einen Q-Ball bis zum Einfang? (Runde 34)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-03 18:29:17 CEST (date), vor jeder Rechnung.
- **Anlass:** Finn ~18:28: "mach den Folgetest mit mehreren Fuenfer-Ecken". Folgeidee aus EINFANG-1 (RUNDE-34.md):
  Jeder Durchgang kostet rund die Haelfte der Bewegungsenergie, also koennten mehrere Fuenfer-Stellen einen Ball
  schrittweise abbremsen und schliesslich festhalten [H].

## Schreibtisch (vor jeder Rechnung)

- **Geometrie:** Oberflaeche eines Ikosaeders mit Kante a, jede Flaeche in nu^2 gleichseitige Dreiecke der Kante h = a/nu
  zerlegt.
  - Die innere Geometrie ist ueberall flach, ausser an den 12 Ecken: dort Fuenfer-Spitzen mit Defizit pi/3.
  - Auf diesem Netz sind die Kotangens-Gewichte ueberall gleich (1/sqrt 3). Die Flaechengewichte sind sqrt(3)/2 h^2 bzw.
    5/6 davon an den Spitzen.
  - Damit ist es genau das KEGEL-Q- bzw. EINFANG-1-Modell, nur mit zwoelf Spitzen auf einer geschlossenen Flaeche.
- **Abstaende:** a = 40 gibt Spitzenabstand 40, viel groesser als Ball (R_halb = 6,26 bei Q = 200) und Reichweite der
  Haftung (~R_halb + 3). Bei h = 0,3 sind das ~177 000 Knoten.
- **EINFANG-1-Zahlen fuer frontale Durchgaenge:** Austritt bei 0,69 v (v = 0,05), Verlust 45 bis 66 % der
  Bewegungsenergie, Boden ~0,009, Einfang unter v ~ 0,011.
  - Erwartung fuer v0 = 0,05 (K = 0,20): Nach k frontalen Durchgaengen K_k ~ 0,2 * 0,5^k. Nach etwa 4 bis 5 Durchgaengen
    liegt K unter ~0,009, dann folgt der Einfang.
  - Seitliche Durchgaenge kosten weniger, die Bahn wird abgelenkt.
- **Unbekannt:**
  - Wie oft eine Bahn ueberhaupt nahe an Spitzen vorbeifuehrt.
  - Ob die gespeicherte Atmung beim naechsten Durchgang Energie an die Bewegung zurueckgibt.
  - Ob Abstrahlung auf der geschlossenen Flaeche zurueckkommt. Dafuer gibt es keinen Schwamm. Abstrahlung bleibt im
    System und kann den Ball wieder treffen.
- **Ableitbarkeit:** E2-1 ist eine Kontrolle (EINFANG-1 nachbilden). E2-2 und E2-3 sind offen. Projekt-grep: Dynamik
  mit mehreren Defekten wurde nie gerechnet.

## Test (Code-Agent)

- **Netz:** Ikosaeder-Oberflaeche wie oben, a = 40, h = 0,3; zweites h oder zweiter Zeitschritt als Probe fuer den
  Hauptlauf.
- **Kontrolle E2-0:** flacher periodischer Torus (ebenes Dreiecksnetz) mit gleicher Flaeche und gleichem h.
- **Modell:** M1, beta = 1/2, Q = 200; Zeitentwicklung, Ball, Boost und Messgroessen wie EINFANG-1
  (RUNDE-34/einfang-1/code/einfang.py).
- **Start:** Ball in der Mitte einer Kante, frontal auf eine Spitze zu, v0 = 0,05.
  - Zusatzlauf v0 = 0,1.
  - Zusatzlauf v0 = 0,05 mit Kurs leicht neben die Spitze (Stossparameter ~R_halb/2), nur berichtet.
- **Laufdauer:** T_end = 8000 (oder bis zum Einfang mit Nachweis), in Abschnitten <= 10 min mit gespeichertem Zustand.
- **Messgroessen:**
  - Bahn auf der Flaeche
  - Abstand zur naechsten Spitze
  - Geschwindigkeit und Bewegungsenergie des Schwerpunkts
  - Ladung und Energie im Ball, Atmungsamplitude
  - Liste der nahen Durchgaenge (Mindestabstand zu einer Spitze < 3) mit K davor und danach
  - **Einfang:** Der Ball bleibt bis T_end innerhalb R_halb + 6 = 12,3 um dieselbe Spitze und wendet dort mindestens
    zweimal. Die Grenze ist wegen der Wendeweite 10,8 in EINFANG-1 weiter gefasst als dort.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| E2-0 | Kontrolle Torus, v0 = 0,05, T = 4000: Geschwindigkeit innerhalb 5 %, Ladung innerhalb 1 % erhalten | 85 % |
| E2-1 | Ikosaeder, erster frontaler Durchgang (v0 = 0,05): Austrittsgeschwindigkeit 0,60 bis 0,80 v0, wie EINFANG-1 (0,69) | 80 % |
| E2-2 | Ikosaeder, v0 = 0,05: Einfang an einer Spitze vor T_end = 8000 | 55 % |
| E2-3 | Ueber alle nahen Durchgaenge faellt K im Mittel um >= 30 % je Durchgang; kein Durchgang erhoeht K um mehr als 10 % | 60 % |

**Bedeutung (vorab):**
- E2-2 und E2-3 treffen ein: Mehrere Fuenfer-Stellen wirken als Bremse ueber innere Moden und fangen bewegte Q-Baelle
  ein [H]. Auf einer facettierten Kugel sammeln sich Q-Baelle an den Spitzen, auch wenn sie mit Schwung starten.
- E2-3 trifft ein, E2-2 nicht: Die Bremsung wirkt, aber die Bahnen treffen die Spitzen zu selten. Beschreiben, wie oft.
- E2-3 trifft nicht ein (Rueckgabe aus der Atmung, Wiederaufnahme der Abstrahlung): Die Bremse ist schwaecher als gedacht.
  Beschreiben.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh (P4000- oder CPU-Spur; je <= 10 min, Abschnitte mit
  gespeichertem Zustand).
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 150 min.
