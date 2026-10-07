# ZELLE600-1: Die 600-Zelle bauen. Finns Tetraeder-Netz auf der 3-Sphaere, mit Pruefung, Kruemmung, Wasserstoff-Muster und Ansicht (Runde 46, Finn-Auftrag)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 06:11:08 CEST (date), vor jeder Rechnung.
- **Finn (05.10., vor 06:11), woertlich:** "Welche 600 Zelle? Bau die"
- **Was sie ist [L]:**
  - Die 600-Zelle ist das regulaere 4D-Polytop {3,3,5}: 120 Ecken auf der 3-Sphaere, 720 Kanten, 1200 Dreiecke, 600 regulaere Tetraeder.
  - Um jede Kante liegen 5 Tetraeder, um jede Ecke 20 (Ikosaeder als Eckfigur), jede Ecke hat 12 Nachbarn.
  - Ecken = die 120 Einheitsquaternionen der binaeren Ikosaedergruppe 2I.
  - Sie ist die einzige Art, den gekruemmten 3D-Raum S^3 lueckenlos mit regulaeren Tetraedern zu fuellen. Im flachen Raum bleibt um jede Kante eine Luecke von 7,36 Grad (Projekt RUNDE-27, GEOMETRIE-XD) [P].
- **Herkunft:** KEGEL-4D-L, Saatidee S5 (laeuft): Nach Fock lebt das Wasserstoffatom auf S^3; die 600-Zelle als Tetraeder-Netz auf S^3 koennte dessen Entartungen 1, 4, 9, 16, ... tragen [H].
- Kennzeichen: [M], [E], [L], [L?], [P], [H].

## Rechnung (Code-Agent)

1. **Bau:**
   - 120 Ecken: 8 Permutationen von (+-1, 0, 0, 0), 16 von (+-1/2, +-1/2, +-1/2, +-1/2), 96 gerade Permutationen von 1/2 (+-phi, +-1, +-1/phi, 0).
   - Kanten: naechste Nachbarn, Laenge 1/phi bei Umkreisradius 1.
   - Dreiecke und Tetraeder als Cliquen.
2. **Pruefen:**
   - Zahlen 120 / 720 / 1200 / 600; Euler-Charakteristik 0 (S^3).
   - 5 Tetraeder je Kante, 20 je Ecke, 12 Nachbarn je Ecke.
   - alle Kanten gleich, alle Tetraeder regulaer.
3. **Kruemmung als Regge-Geometrie:**
   - Der Rand der 600-Zelle ist ein Regge-Netz aus flachen Tetraedern. Jede Kante hat den Fehlwinkel delta = 2 pi - 5 arccos(1/3) = 7,36 Grad.
   - Vergleich Summe(l delta) mit dem Kontinuum (1/2) Integral R dV = 6 pi^2 R fuer S^3 vom Radius R.
4. **Spektrum:**
   - Adjazenz- und Graph-Laplace-Matrix (120 x 120): Eigenwerte und Vielfachheiten.
   - Vergleich mit den Harmonischen auf S^3: Eigenwert k(k+2)/R^2, Vielfachheit (k+1)^2, n = k + 1 nach Fock, also Wasserstoff.
5. **Ansicht:**
   - Selbststaendige HTML-Datei: inline-JavaScript ohne Module, Canvas oder three.js als klassisches Skript von cdnjs, funktioniert per file://.
   - Inhalt:
     - stereographische Projektion der 120 Ecken und 720 Kanten
     - 4D-Drehung per Schieberegler (Ebenen xw, yw, zw)
     - Faerbung nach den Schalen um einen Pol (Ecken je Schale zaehlen und anzeigen)
     - wahlweise hervorgehoben: ein Ring aus 30 Tetraedern (Boerdijk-Coxeter-Helix), falls er sich im Netz findet
   - Dazu ein PNG per headless Chrome mit GPU (Rezept: --use-angle=vulkan --enable-features=Vulkan --enable-gpu --ignore-gpu-blocklist; Datei per file://, kein lokaler Server).

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| Z0 | Kontrolle [L, vorab bekannt]: 120 / 720 / 1200 / 600, Euler 0, 5 Tetraeder je Kante, 20 je Ecke, alle Tetraeder regulaer | 95 % |
| Z1 | [L?] Das Adjazenzspektrum hat 9 verschiedene Eigenwerte mit den Vielfachheiten 1, 4, 9, 16, 25, 36, 9, 16, 4 | 65 % |
| Z2 | [H] Nach steigendem Laplace-Eigenwert geordnet, haben die ersten sechs Niveaus die Vielfachheiten 1, 4, 9, 16, 25, 36, also das Wasserstoff-Muster n^2 fuer n = 1 bis 6; danach bricht es ab | 60 % |
| Z3 | [M] Die Regge-Kruemmung Summe(l delta) liegt innerhalb von 5 % beim Kontinuumswert 6 pi^2 R (Schreibtisch: etwa 57,1 R gegen 59,2 R) | 80 % |
| Z4 | [H] Die Laplace-Eigenwerte der ersten drei angeregten Niveaus folgen dem Kontinuum k(k+2)/3 (relativ zu k = 1) auf 10 % | 55 % |

**Ableitbarkeitsprobe:**
- Z0 und Z3 sind vorab ableitbar (Kontrollen).
- Z1 und Z2 folgen aus der Darstellungstheorie von H4 (Einschraenkung der SO(4)-Harmonischen) und stehen vermutlich in der Literatur [L?]. Die Rechnung prueft das; sie ist keine Messung.
- Neu fuer Finn ist das Bild: ein Wasserstoff-Muster auf einem Tetraeder-Netz, und wo es abbricht.

## Rahmen

- Code-Agent.
- Rechnung (Bau, Spektrum) auf der .69 ueber kleintest.sh, Spur cpu oder cpu2. Je Lauf hoechstens 10 min, ein Thread.
- Die HTML-Ansicht und das PNG sind Darstellung und duerfen lokal entstehen. Kein lokaler Interpreter: kein Python, kein lokaler Server.
- Zeitbox 90 min.
