# RAUM-GAS-L: Kann der Raum ein Gas bzw. eine Fluessigkeit aus Netzpunkten sein, und was sagen Literatur und Daten dazu? (Runde 48, Finn-Auftrag)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 09:41:43 CEST (date), vor jedem Abruf.
- **Finn (05.10., kurz vor 09:41), woertlich:** "Was ist mit Gasen?"
- **Lesart der Leitung** (im Gespraech nach Kristall, Glas und Cristobalit): Gefragt ist der dritte Zustand von Finns Netz neben Kristall (fest, geordnet) und Glas (fest, ungeordnet), also Gas bzw. Fluessigkeit. Die Punkte bewegen sich frei, die Tetraeder bauen sich laufend neu (Umklappen als Stroemung). Andere Lesarten (z. B. Gase als Materie im Modell) meldet der Agent nur, wenn er sie in den Quellen findet.
- **Projektstand [P]:**
  - Glasnetze sind stabil, die TT-Spanne faellt ~N^-0,5 (TT-GLAS-1, TT-GLAS-2; mit Einschraenkung: gerechnet an 112 k-Klassen des 6^3-Gitters).
  - Delaunay-Umklappen haelt das Netz waehrend laufender Wellen stabil. Die Energie bleibt dabei aber nicht erhalten: 0,2 bis 0,5 % je Zug, mit J = 1 je Zelle (TAKT-DYNAMIK-1). Ein Gas klappt staendig; das ist die Kernfrage.
  - Flache 2-3-Zuege aendern die Regge-Energie nicht (UMKLAPP-1). Die Rueckstellkraft der Schwerewellen ist Kruemmung, nicht Scherfestigkeit.
  - Phasen der dynamischen Triangulierung (Knaeuel, verzweigte Polymere; CDT-Schaumphase) [P: WELTKRISTALL-L, BABY-UNIVERSUM-L].
  - Projektsuche (09:41, alle Dateitypen, Ausschluesse): Volovik, Gruppenfeldtheorie-Kondensate, viskoelastische Uebergaenge und Moving-Mesh-Verfahren sind im Projekt nicht gelesen.
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Fragen

1. **Raum als Quantenfluessigkeit bzw. Kondensat:**
   - Volovik (suprafluides Helium-3, "Universe in a helium droplet")
   - Gruppenfeldtheorie-Kondensate (Oriti u. a.)
   - weitere Ansaetze, die den Raum als Fluessigkeit oder Gas fassen
   - Was ist dort gezeigt, was nur gedeutet?
2. **Querwellen in Fluessigkeiten:** Gase und Fluessigkeiten tragen Scherwellen nur oberhalb einer Frequenz 1/tau (Maxwell-Viskoelastik, "k-Luecke"). Gilt das fuer Schwerewellen in einem "fluessigen" Netz, oder entkoppelt die Kruemmungs-Rueckstellkraft davon?
3. **Daten:**
   - Schwerewellen sind von Nanohertz (Pulsar-Timing) bis Kilohertz (LIGO/Virgo) beobachtet.
   - Welche Schranken gibt es fuer Daempfung, Viskositaet bzw. Dispersion von Schwerewellen ueber kosmische Strecken?
   - Was folgt daraus fuer eine Umordnungszeit tau eines Raum-Gases?
4. **Verfahren:** Moving-Mesh-Verfahren (z. B. AREPO: Voronoi bzw. Delaunay bewegter Punkte) gelten als erhaltend, weil Flaechen beim Umklappen durch null gehen. Wie erhalten sie Masse, Impuls und Energie? Was laesst sich fuer Finns Netz uebernehmen?
5. **Phasen:** Gibt es in DT, CDT oder Kausalmengen eine Phase, die einem Gas entspricht, und wie verhaelt sie sich (Dimension, Wellen)?

## Ableitbarkeitsprobe (Leitung, verkettet)

- **Vorab ableitbar [M, L]:**
  - Eine einfache Fluessigkeit hat keinen statischen Schermodul. Querwellen gibt es nur fuer omega tau > 1 (Maxwell) [L].
  - Flache Pachner-Zuege lassen die Regge-Energie unveraendert [P].
  - Ob ein Gas-Netz Schwerewellen bei omega tau < 1 traegt, haengt deshalb daran, ob die Rueckstellkraft wie Scherung oder wie Kruemmung wirkt. Das ist nicht ableitbar.
- **Nicht ableitbar:** Literaturstand zu 1, 4 und 5; die Datenschranken zu 3; und die Antwort auf die Scherung-oder-Kruemmung-Frage.

## Vorhersagen (vor jedem Abruf)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| RG1 | [L?] In Volovik-Modellen (suprafluides He-3-A) entstehen fuer Quasiteilchen wirksame Metrik und Eichfelder; Einstein-Dynamik der Metrik entsteht dort nicht von selbst | 75 % |
| RG2 | [L?] Gruppenfeldtheorie-Kondensate liefern eine Friedmann-artige Dynamik der Raumgroesse; Schwerewellen bzw. Rueckwirkung sind dort hoechstens in Anfaengen behandelt | 65 % |
| RG3 | [H] Es gibt Schranken fuer eine Daempfung bzw. Viskositaet von Schwerewellen aus beobachteten Signalen (LIGO/Virgo, ggf. Pulsar-Timing), und sie sind stark genug, um ein Raum-Gas mit Umordnungszeit ueber einer Schwingungsdauer auszuschliessen, falls die Wellen scherartig sind | 55 % |
| RG4 | [L?] Moving-Mesh-Verfahren erhalten Masse, Impuls und Energie ueber Umklappungen exakt, weil die betroffenen Flaechen durch null gehen | 60 % |
| RG5 | [H] In DT, CDT oder Kausalmengen gibt es keine Phase, die als "Gas" mit flachem, isotropem Grenzfall und Schwerewellen gilt | 55 % |

**Bedeutung (vorab):**
- **RG3 und RG4 treffen ein:** Ein Raum-Gas ist nur moeglich, wenn das Umklappen die Wellenenergie exakt erhaelt, wie bei Moving-Mesh-Verfahren. Dann geht es mit HODGE-MASSE-1 als Rechenkarte weiter (GAS-NETZ-1).
- **RG1 und RG2:** Der Raum als Fluessigkeit ist ein bekanntes Forschungsbild. Neu waere bei Finn die Netzform mit Umklappen.
- **RG5 verfehlt:** Es gibt ein Vorbild aus der Quantengravitation, und das wird gelesen.

## Rahmen

- feldforscher, Zeitbox 60 min, hoechstens 15 Netzabrufe; WebSearch, arXiv, INSPIRE, OpenAlex, freie Verlagsseiten.
- Schreibt nur in RUNDE-37/raum-gas-l/.
- Literatur, keine Rechnung. Eine Rechenkarte GAS-NETZ-1 (thermisch bewegte Ecken, laufendes Delaunay, Wellen) folgt erst nach HODGE-MASSE-1.
