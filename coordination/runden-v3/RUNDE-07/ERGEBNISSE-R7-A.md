# Runde 7, Auswertung A: RING und R5F

Auswerter: Anthropic-Agent (Opus 5.5) im Auftrag der Leitung claude-primary. Explorativ (v3), keine formale Bestaetigung.
Beginn 2026-09-30 04:59:51 CEST, Ende 2026-09-30 05:19:09 CEST (beide mit date gemessen).

## 0. Grundlage und Vorbehalte

- **Gelesen, RING:**
  - ring/PLAN.md
  - ring/lauf-69/: rauchtest/, ausgabe/ (profile, wirbel grob/fein/L3, teilung grob/fein/L3, vierer grob/fein/L3),
    ausgabe-saat/ (wirbel grob), LAUF1.log, LAUF2.log
  - Alle neun Aufrufe liefen mit rc = 0.
- **Gelesen, R5F:**
  - r5f/PLAN.md
  - r5f/lauf-69/: ausgabe-tod/, ausgabe-fuettern/ (mechanik, raster55, raster70), ausgabe-kavitation/, rauch-cpu/,
    LAUF1.log bis LAUF5.log
  - ausgabe-kavitation/ enthaelt zwei Berichte: raster (GPU, 100 Laeufe, T = 600) und raster_0.72 (CPU-Ausweg, 25
    Laeufe, T = 400).
- **kav-box laeuft noch.**
  - LAUF3.log: start 02:55:20 UTC. Gesichert sind die Rohdaten L200 grob, L200 fein und L400 grob.
  - Es gibt keine Ende-Zeile und keinen Bericht.
  - Alles, was an Box L = 400 und `--sehrfein` haengt, steht unten als "laeuft noch"; die Leitung liefert nach.
- **Hintergrund gelesen:** RUNDE-05.md, RUNDE-06/ERGEBNISSE-R6-C.md, README.md (v3), RUNDE-07.md.
- **Zahlen:**
  - Die Zahlen stammen aus den Berichten (txt) und den zugehoerigen ergebnis.json.
  - "von Hand" markiert einfache Differenzen oder Zaehlungen von Berichtszeilen.
  - Log-Zeiten sind UTC.
- **L1 bei RING:** Die RING-Vorhersagen wurden nach PLAN 0.2 vor der lokalen Vorschau im Kopf festgelegt, aber erst
  danach niedergeschrieben. L1 gilt dort nur mit Vorbehalt.

## 1. Tests

### RING-W: Wirbelball aus dem mitdrehenden Ring (`wirbel`; grob T = 3000, fein T = 1000)

Laeufe:
- grob: N6_dreh+, N8_dreh+, N6_dreh+_s1e-2 und N8_dreh+_s1e-2 (wirbel-a); N6_dreh+_s1e-3, N6_dreh+_s1e-4 und
  N8_ruhend (wirbel-b)
- fein: N6_dreh+, N8_dreh+, N6_dreh+_s1e-2

| Nr. | Vorhersage (PLAN 2.3, knapp) | Ergebnis | Bewertung |
|---|---|---|---|
| A1 | Solange ein Klumpen: W = 1 auf allen sicheren Kreisen r = 2 bis 8 in >= 95 % der Analysen ab T/2; ein +1-Wirbel in r < 4, kein Gegenwirbel (p 0,85) | Kein Klumpen hielt bis T/2 = 1500 (grob); Anteil W = 1 ab T/2 in allen 7 grob-Laeufen "-" oder 0,000. fein ab t = 500 (Klumpen- und Zerfallsphase gemischt): N6 0,195 (41 sichere Analysen), N8 0,551 (89). Windung am Ende 0 auf allen Kreisen r = 1 bis 8 in allen 10 Laeufen; sichere Kreise gibt es dabei nur in den drei N8-Laeufen N8_dreh+ grob/fein und N8_ruhend (dort W = 0), sonst ist das Feld zerlaufen. Windung waehrend der Klumpenphase: nicht im Bericht. | nicht auswertbar |
| A2 | J/Q (Fenster) bei t = 250 bis 500 zwischen 0,95 und 1,05 (p 0,8); spaet 1,00 +- 0,02, falls ein Klumpen bleibt (p 0,7) | t = 250 / 500: N6 0,9570 / 0,9711; N8 0,9815 / 0,9891; fein gleich auf 1e-4. Es bleibt kein Klumpen; spaetes J/Q (grob) -0,030 bis +0,014. | getroffen (erster Teil); zweiter Teil entfaellt |
| A3 | omega_eff innerhalb 2 % von omega_m1(Q_w) und naeher an m = 1 als an m = 0 (p 0,6) | Nur fein N8 hat einen Vergleich; das spaete Mittel ab t = 500 enthaelt die Zerfallsphase (Q_w 151,5, std 66,9): omega_eff/omega_m1 1,0082, omega_eff/omega_m0 1,0338. Alle anderen Laeufe: "m = 1 gleicher Ladung: ausserhalb des Profilgitters". omega_eff bei t = 500: N6 0,7558, N8 0,7458. Ein Vergleichswert gleicher Ladung zu diesem Zeitpunkt: nicht im Bericht. | teilweise (formal getroffen, nur im Mischfenster) |
| A4 | spaet L2(m = 1) < 0,15 und >= 30 % kleiner als L2(m = 0) (p 0,55); E/Q hoechstens 3 % ueber m = 1 (p 0,5) | fein N8 spaet: L2(m = 1) 0,463, L2(m = 0) 0,521; E/Q 2,1 % unter m = 1. Zeitreihe L2(m = 1): N8 0,0574 bei t = 250 (fein 0,0525), 0,4627 bei 500; N6 Minimum 0,379 (fein) bzw. 0,390 (grob) bei t = 500. | Profil verfehlt; E/Q formal getroffen |
| A5 | vor Vorschau: N6 bleibt bis 3000 (p 0,6), N8 bleibt (p 0,65). Nach Vorschau: N6 zerfaellt nach t = 350 bis 700 in 3 Klumpen, Rate etwa 0,08 (p 0,45); N8 bleibt laenger ganz als N6 (p 0,6) | Teilung: N6 bei 535 (fein 515), N8 bei 710 (fein 720). Fensterladung unter 1/2: N6 ab 678,5 (631), N8 ab 1005 (804). N6: A_l-Maximum l = 2 0,865, l = 3 0,218. Zahl der Toechter: nicht im Hauptbericht (n Ende 0). | vor Vorschau verfehlt; nach Vorschau teilweise (Zeitfenster und "N8 laenger als N6" getroffen; "3 Klumpen" nicht belegt, l = 2 dominiert) |
| A6 | s1e-2: Zerfall in 3 Klumpen vor t = 100 (p 0,7); Zerfallszeit waechst je Dekade Saat um 25 bis 40 (p 0,5) | Teilung bei s1e-2: N6 50, N8 60 (Fensterladung unter 1/2: 128 bzw. 152,5). N6-Reihe fuer Saat 1e-2 / 1e-3 / 1e-4 / 0: Teilung 50 / 95 / 145 / 535, also 45 und 50 je Dekade (von Hand). Fensterkriterium: 128 / 139 / 207, also 11 und 68 je Dekade (von Hand). | teilweise (vor t = 100 getroffen; Zuwachs je Dekade verfehlt; "3 Klumpen" nicht im Bericht) |
| A7 | N8_ruhend: ein Klumpen ab t = 5 bis 15 mit W = 1 (p 0,85); Klumpen-J/Q bei t = 500 zwischen 0,95 und 1,05 (p 0,6); danach wie N8_dreh+ (p 0,5) | Ein Klumpen ab t = 10. J/Q: 0,614 (t = 0), 0,757 (100), 0,973 (250), 0,989 (500). L2(m = 1) bei t = 500: 0,029. Teilung bei 665 (N8_dreh+: 710), Fensterladung unter 1/2 ab 812,5. W in der Klumpenphase: nicht im Bericht. | getroffen (ausser W: nicht im Bericht) |

- **Kriterium 2.4:**
  - "Wirbelball": nicht erfuellt, kein Klumpen hielt bis T.
  - "Wirbelball auf Zeit":
    - Die Zerfallszeit waechst mit ln(1/Saat): 50, 95, 145.
    - A1 und die Frequenz in der Klumpenphase fehlen im Bericht.
    - J/Q 1,00 +- 0,03 bei t = 250 bis 500 halten nur die N8-Laeufe; N6 liegt bei t = 250 bei 0,957.
- **Vorwissen aus Runde 6:** Die ringe-Laeufe in R6 endeten bei T = 500 mit "ein Klumpen mit Windung 1". R7 zeigt den
  Bruch bei 515 bis 720, also kurz danach.
- **L3: bestanden (3 von 3).**
  - N6: Bruch 535/515, max|dJ/Q| 1,5e-5, max|domega/omega| 1,3e-4
  - N8: Bruch 710/720, 2,0e-4, 5,7e-4
  - N6_s1e-2: Bruch 50/50
  - Das Kriterium gilt nur vor dem Bruch; danach laufen grob und fein auseinander (Abschnitt 3).
- **Latten:** L1 Vorbehalt, L2 ja, L3 bestanden, L4 teilweise, L5 mittelbar.
- **Vorschlag: parken.** Der Ringklumpen ist nur zeitweise m = 1-aehnlich und zerfaellt in allen zehn Laeufen, mit
  Saat frueher; die Frage "stabiler Wirbelball" ist damit im Bericht mit "nur auf Zeit" beantwortet.

### RING-T: Teilungsschwelle des ruhenden m = 1-Balls (`teilung`; grob T = 3000, fein T = 1500)

| Vorhersage (PLAN 3.3) | Ergebnis | Bewertung |
|---|---|---|
| 0,55 ruhig bis 3000 (p 0,85) | keine Teilung; J/Q 0,9999; W = 1 in 100 % | getroffen |
| 0,65: Teilung bei 40 bis 60, gamma 0,08 bis 0,11, l = 2, zwei Toechter mit W = 0 (p 0,9) | Teilung bei 50, gamma 0,0925, l_dom 2; Toechter Q 35,9 und 34,8, beide W 0 | getroffen |
| 0,575 ruhig (p 0,65) | ruhig | getroffen |
| 0,59 ruhig (p 0,6) | ruhig, grob und fein | getroffen |
| 0,60 ruhig (p 0,5) | Teilung bei t = 1045, gamma 0,0041, l_dom 2, Toechter W 0 | verfehlt |
| 0,625 geteilt (p 0,6) | Teilung bei 75 (grob und fein), gamma 0,0641 | getroffen |
| Schwelle zwischen 0,60 und 0,625 (p 0,4); zwischen 0,575 und 0,60 (p 0,25); anderswo (p 0,35) | zwischen 0,59 und 0,60 (Q 157,1 bis 138,8), also im Fach mit p 0,25 | Hauptoption verfehlt |
| wo geteilt: l_dom = 2, Toechter W = 0 (p 0,8); gamma faellt zur Schwelle hin monoton (p 0,7) | l_dom 2 in 3 von 3, alle Toechter W 0; gamma 0,0925, 0,0641, 0,0041 | getroffen |
| Selbstprobe: stabile Baelle Profil-L2 < 0,05, J/Q 1,000 +- 0,005 (p 0,9) | L2 0,00098 / 0,00116 / 0,00134; J/Q 0,99989 / 0,99985 / 0,99985 | getroffen |

- **Einordnung der Ringklumpen** (Vergleich aus PLAN 8; der Bericht zieht ihn nicht selbst):
  - Q_w bei t = 500: N6 164,2, N8 211,6, N8_ruhend 198,0. Alle liegen ueber der Schwellenladung 138,8 bis 157,1.
  - E/Q bei t = 500: 0,8911 / 0,8662 / 0,8720.
  - Profiltabelle m = 1: 0,866 bei Q 168,7; 0,873 bei Q 157,1; 0,858 bei Q 182,6; 0,850 bei Q 199,4; 0,841 bei Q 219,8.
  - Die Klumpen tragen also mehr Energie je Ladung als ein m = 1-Ball benachbarter Ladung.
- **L3: bestanden.** 0,59 ruhig/ruhig; 0,625 Teilung 75/75, gamma 0,0641/0,0641. Fuer 0,60 gibt es keinen feinen Lauf.
- **Latten:** L1 Vorbehalt, L2 ja, L3 bestanden, L4 ja, L5 mittelbar.
- **Vorschlag: parken.** Die Schwelle liegt zwischen 0,59 und 0,60; offen ist nur ein feiner Lauf bei 0,60, dessen
  spaete Teilung (t = 1045, gamma 0,0041) bisher nur grob gerechnet ist.

### RING-V: Vierer-Ring mit Windung 2 pi/4 (`vierer`; grob T = 2000, fein T = 1000)

| Lauf | Vorhersage (PLAN 4.3) | Ergebnis | Bewertung |
|---|---|---|---|
| n4_windung | Symmetriebruch mit gamma 0,05 bis 0,10, t_Bruch 380 bis 600 (p 0,7); Klasse Ladungstausch oder verschmolzen (p 0,75) | Ladungstausch; t_Bruch 543, gamma 0,0534, verschmolzen bei 580; danach r = 34,4 bei t = 800; Q-Verlust bis T 0,99 | getroffen |
| n4_windung_sym | gebunden im Sektor (p 0,55); Periode 120 bis 200 (p 0,6); Drehung -3e-3 bis -8e-3 (p 0,7) | gebunden bis 2000 (fein bis 1000). r 5,549 bis 6,199, Mittel 5,898; Drift 1,2e-5 (+0,004 r0); Periode 160,0 (fein 166,7); Drehrate -3,34e-3; Spreizung auf Rundungsniveau (hoechstens 3,7e-16); Q-Verlust 5,2e-4 | getroffen |
| Saaten | t_Bruch(1e-3) < t_Bruch(1e-6) < t_Bruch(0); dt_Bruch x gamma / ln 1000 zwischen 0,7 und 1,3 (p 0,6) | 81,5 < 195 < 543; Verhaeltnis 0,907 (dt 113,5, gamma 0,0552) | getroffen |
| n4_gegen | r(t) bis t = 300 gleich n4_windung auf 1e-10, J und Drehrate entgegengesetzt (p 0,97) | max dr/r bis 300: 1,3e-15, J-Summe 1,1e-15; Drehrate +3,34e-3 gegen -3,35e-3 | getroffen |
| n4_gleich | verschmolzen bis t = 10 (p 0,95) | verschmolzen bei t = 5 | getroffen |
| Luecke 6 | l6 bricht spaeter und mit kleinerem gamma (p 0,6); l6_sym gebunden (p 0,45) | l6: Ladungstausch bei 1030, gamma 0,0275; l6_sym gebunden bis 2000 (Periode 500) | getroffen |
| l8_sym | fast ruhend, "gebunden" nach Kriterium (p 0,6) | "auseinander" ab t = 612; r waechst an allen Reihenzeiten von 8,37 auf 14,70 (t = 2000); Drift +0,333 r0 | verfehlt |
| Gesamtantwort | symmetrischer Zustand gebunden, aber instabil (p 0,5) | gebunden im C4-Sektor (Luecke 4 und 6); ohne Sektor Bruch durch Ladungstausch | getroffen |

- **L3: bestanden.**
  - sym: max|dr/r| 6,6e-4, Klasse gleich
  - s1e-6: max|dr/r| 3,8e-4, t_Bruch 195/195, gamma 0,0552/0,0537
- **Latten:** L1 Vorbehalt, L2 ja, L3 bestanden, L4 teilweise, L5 nein.
- **Vorschlag: verwerfen** (als Verbund). Gebunden ist der Vierer nur unter erzwungener C4-Symmetrie, die PLAN 9 selbst
  ein numerisches Mittel nennt. Jede Unsymmetrie waechst mit gamma 0,053 bis 0,055, und bei Luecke 8 laufen die Baelle
  auseinander.

### RING-K: Kontrollen (Bilanz, Schranken, L3)

| Vorhersage (PLAN 5) | Ergebnis | Bewertung |
|---|---|---|
| Bilanz in allen Laeufen unter Toleranz (p 0,9); Q-Rest unter 1e-4 (p 0,8) | Ueber Toleranz in allen Laeufen mit grossem Randverlust: wirbel 10 von 10; teilung 3 von 6 grob und 1 von 2 fein (die geteilten); vierer 6 von 9 grob und 1 von 2 fein. Dort Q-Rest 1,1e-3 bis 5,3e-3 (Toleranz 1e-3), J-Rest bis 3,7e-2 (Toleranz 3e-3), E-Rest bis 1,1e-2 (Toleranz 1e-3). Laeufe mit kleinem Randverlust: Q-Rest 3,4e-8 bis 3,5e-6. | verfehlt |
| L3 bestanden: wirbel (p 0,75), teilung (p 0,85), vierer (p 0,8) | alle drei bestanden | getroffen |
| Schranken alle erfuellt (p 0,85); am ehesten reisst "Profil eingeschachtelt" | "Profil eingeschachtelt" false in 9 von 10 wirbel-Laeufen. "omega_eff < 1" false in 5 von 10 (spaetes Fenster nach dem Zerlaufen, omega_eff 1,004 bis 1,010). Dazu die Bilanz (oben). | verfehlt |

- **Muster der Bilanz:**
  - Der Q-Rest waechst mit der geschluckten Menge.
  - Er sinkt von grob zu fein etwa auf die Haelfte: N6 5,1e-3 -> 2,5e-3; teilung 0,625 4,8e-3 -> 2,4e-3; vierer s1e-6
    4,4e-3 -> 2,1e-3.
  - Nach PLAN 1.3 misst der Q-Rest nur den Quadraturfehler der Verlustrate, denn Q ist im Verlet-Verfahren exakt
    erhalten.
  - Eine Verletzung von Q, J oder E zeigen die Berichte damit nicht; die Messung der geschluckten Menge verfehlt aber die
    vorab gesetzte Toleranz.
- **Latten:** L1 ja, L2 ja, L3 entfaellt, L4 entfaellt, L5 entfaellt.
- **Vorschlag:** entfaellt (Kontrolle). Vor weiterer Nutzung der Bilanz die Verlustraten-Quadratur pruefen.

### R5F-a: Tod unter Q_min (`tod`; 3D radial, grob T = 4000, fein T = 2000)

| Nr. | Vorhersage (PLAN 4a) | Ergebnis | Bewertung |
|---|---|---|---|
| V-a1 | Dauerabfluss: t90 = 652 +- 5, t10 = 852 +- 10, omega vor Tod 1,007 +- 0,002, Q_in(t90)/Q_min = 0,775 +- 0,01. Stopp 0,9: t90 = 652 +- 5 | t90 651,5 (fein 650,5); t10 851,5 (851,5); omega 1,0070 (1,0069); Q_in(t90)/Q_min 0,7781 (0,7805). Stopp 0,9: t90 651,5 (650,5) | getroffen |
| V-a2 | Dauer t10 - t90 (r < 25) = (25 - R_E)/v_g auf 30 %; Kern r < 10: Dauer <= 0,5 x Fenster | Gemessene Dauer 192,5 bis 204,5 gegen Formel 84,2 bis 89,7, also mehr als das Doppelte. Kern: 89,5 bis 97,5 gegen Fenster 192,5 bis 204,5. Kern-t90 582,5 bis 583 (Klumpen 44,5) liegt vor Fenster-t90 650,5 bis 652,5 (Klumpen 105,0 bis 105,5). | teilweise (Formel verfehlt, Kern getroffen; Gegenhypothese "gleich schnell" nicht gesehen) |
| V-a3 | Linie vor dem Tod bei Omega +1,000 bis +1,015, Asym > 0,9 | Stopp-Laeufe und Dauerabfluss: +0,9692 bis +0,9698 (Anteil 0,50), Anteil unter der Luecke 0,03, Asym +1,00 (Fenster 441,5 bis 642,5, dOmega 0,0313). Klumpen: +1,0068 (fein +1,0058), Asym +1,00. | teilweise (Asym getroffen; Linie nur beim Klumpen im Band) |
| V-a4 | Hauptfrage: Rest zerlaeuft, kein fruehes Plateau (Stopp 0,95 / 0,9 / 0,8, Klumpen); Gegenhypothese Oszillon | Klasse "zerlaeuft" in 4 von 4, grob und fein; fruehes Plateau: nein. E_in/E_ref nach t10 + 500: 0,005 bis 0,006; bei T (grob, T = 4000) 0,003 bis 0,016. S_max spaet 1,7e-5 bis 4,0e-5 (grob) bzw. 3,2e-5 bis 7,8e-5 (fein). Spaete Linie +1,0035 (grob), +1,0134 bis +1,0261 (fein), Asym +1,00. | getroffen; Oszillon nicht gesehen |
| V-a5 | Stopp 0,95 stirbt, t50 - t_stop zwischen 50 und 500; Stopp 1,05 lebt bis T: q_rel(T) > 0,9, Linie +0,93 bis +0,96, Asym > 0,95 | Stopp 0,95: t_stop 560,5, t50 710,0, Differenz 149,5 (von Hand). Stopp 1,05: lebt; Linie +0,9454 (fein +0,9455), Asym +1,00. q_rel(T) als Zahl: nicht im Bericht (Q_in spaet 117,42, Q_min 111,8441). | getroffen |
| V-a6 | Gegenproben ohne Abfluss: \|dQ_in\|, \|dE_in\| < 1e-3; Linie +0,8944 bzw. +0,9487, Anteil > 0,5, Asym > 0,95 | 0,80: -7,8e-8 / -4,2e-9; 0,90: -9,5e-7 / -8,8e-7 (grob). Linie +0,8942 (Anteil 0,53) bzw. +0,9485 (0,67); Asym +1,00 | getroffen |

- **L3:** 22 von 26 Kenngroessen, Klasse gleich in 8 von 8.
  - Die vier NEIN: t50 und Dauer bei Stopp 1,05 sind nan (der Ball lebt).
  - E_spaet_rel der beiden Gegenproben: Effekt 4,0e-8 bzw. 1,2e-6, etwa so gross wie die Aenderung.
- **Plausibilitaet:** E_tot-Anstieg nach dem Stopp hoechstens 2,5e-7; q_rel max 1,0000; kein E_in > E_tot.
- **Latten:** L1 ja, L2 ja, L3 bestanden, L4 teilweise, L5 nein.
- **Vorschlag: parken.** Im radialen Modell (nur l = 0) zerlaeuft der Rest in allen vier Laeufen unter Q_min ohne
  kugeliges Oszillon. Offen bleibt nur, warum die Aufloesung mehr als doppelt so lange dauert wie das v_g-Bild.

### R5F-b: Fuettern unter der Schwelle (`fuettern`; 1D; mechanik 21, raster55 und raster70 je 74 Ball+Paket-Laeufe)

| Nr. | Vorhersage (PLAN 4b) | Ergebnis | Bewertung |
|---|---|---|---|
| V-b1 | dQ ~ eps^p mit p = 2,0 +- 0,15 bei nu = 2,2 und 2,8 | p 1,997 / 2,003 (2,2) und 1,989 / 1,990 (2,8), grob/fein. C_nach bei 2,2 fuer eps 0,0025 bis 0,05: 6,00e-2 bis 6,12e-2 | getroffen |
| V-b2 | unter der Schwelle Ort 10/20 >= 0,8 und dE/dQ = nu auf 10 %; ueber der Schwelle dE/dQ = omega auf 10 % | nu 2,2: Ort 0,894 bis 0,966; dE/dQ 2,109 bis 2,141 (sigma 4 bis 16). nu 2,125: dE/dQ 2,063 bis 2,141. nu 2,8: 0,742 bis 0,743 (omega 0,7416). Ausnahmen bei kleinem oder vermischtem C: nu 2,2 sigma 32 (C 8,7e-5) 1,316; nu 2,4 sigma 4 1,871 | getroffen (bis auf zwei Randfaelle) |
| V-b3 | 0,55 nahe nu_r: kappa = 2 Gamma = 0,0102 auf 30 %; 0,70 nahe nu_r: kappa < 1e-3 | 0,55 bei nu 2,125: 8,4e-3 bis 1,00e-2 (sigma 4 bis 32). 0,70 an der Spitze: 1,3e-4 bis 1,43e-4 (2 Gamma_1D laut Bericht 1,3e-4) | getroffen |
| V-b4 | Spitze bei 2,118 (0,55) bzw. 2,330 (0,70), auf 0,03 (sigma 32) bzw. 0,05 (sigma 8). Zwischen Spitze + 0,1 und Schwelle faellt C (sigma 32) um mindestens den Faktor 10. Ueber der Schwelle Born-Hoehe (0,55: 0,04 bis 0,07). Atmungslinie bei Re rho 1,377 bzw. 1,494 auf 0,03 | Spitzen: 0,55 bei 2,1208 / 2,1196 (sigma 8) und 2,1244 / 2,1236 (sigma 32); 0,70 bei 2,3296 / 2,3280 und 2,3302 / 2,3289. Kleinstes C im Zwischenbereich 1,8e-5 (0,55) bzw. 9,1e-7 (0,70), bei Spitzen-C 0,131 bzw. 7,7e-3. Erster Wert ueber der Schwelle (0,55): 4,43e-2 / 4,51e-2. Atmung 1,3778 (0,55) sowie 1,4931 / 1,4945 (0,70). Im selben Zwischenbereich liegt eine zweite Spitze (Abschnitt 3). | getroffen; zweite Spitze nicht vorhergesagt |
| V-b5 | nu 2,4: C faellt von sigma 8 auf 32 um mindestens den Faktor 10 (Auslaeufer). nu 2,125: C_ankunft faellt hoechstens um den Faktor 3. nu 2,2: C(sigma 4)/C(sigma 8) zwischen 0,3 und 3 (H1 verlangt etwa 100) | 2,4: 4,73e-2 -> 3,13e-2 (grob). 2,125: C_ankunft 0,207 -> 0,657, steigt also. 2,2: 6,52e-2 zu 6,00e-2 | teilweise (2,4 verfehlt) |
| V-b6 | C_R5(0,55; 2,2; eps 0,01; sigma 8) = 0,024 +- 0,005 | 2,43e-2 (fein 2,39e-2) | getroffen |
| V-b7 | \|Bilanz_Q\| < 1e-3; unter der Schwelle 0 <= R, T <= 1 | \|Bilanz_Q\| hoechstens 9,9e-6 (Energie hoechstens 4,1e-4). R -0,0014 bis 0,254, T bis 1,0000; "plaus ok" in 338 von 338 Berichtszeilen | getroffen (R bei nu 2,475 knapp unter 0) |

- **L3:**
  - mechanik: C_nach 21 von 21, kappa 20 von 21
  - raster55: C_nach 73 von 76, kappa 53 von 74
  - raster70: C_nach 61 von 76, kappa 37 von 66
  - nu_peak in allen vier Rastern ok (Aenderung 0,0008 bis 0,0016)
  - Die Ausfaelle liegen an Flanken mit kleinem C (bis 1,8e-3) oder bei kappa nahe 0.
- **Latten:** L1 ja, L2 ja, L3 ueberwiegend, L4 teilweise, L5 nein.
- **Vorschlag: weiter.** Lage, Abklingrate und Atmungslinie trafen den vorab bekannten 1D-Pol bei beiden Baellen, die
  Aufnahme ist linear, und die zweite, nicht vorhergesagte Spitze unter der Schwelle ist eine offene, pruefbare Frage.

### R5F-c: Kavitation im dichten Kondensat (`kavitation`; raster 100 Laeufe, L = 200, T = 600; 0,72 zusaetzlich auf CPU mit T = 400; box laeuft noch)

| Nr. | Vorhersage (PLAN 4c) | Ergebnis | Bewertung |
|---|---|---|---|
| V-c1 | Kontrollen ohne Delle: rms/S0 < 1e-3 | grob 6,0e-5 / 1,2e-5 / 1,3e-4 / 8,0e-5; fein 1,3e-5 / 2,2e-6 / 3,1e-5 / 2,2e-5 (S0 0,70 / 0,72 / 0,75 / 0,80) | getroffen |
| V-c2 | heilt/heilt-nicht in >= 80 % der Laeufe ohne "unklar"; Unterklasse (Klumpen gegen Kaverne) in >= 60 % | 86 von 91 (grob und fein). Genau getroffen: 65 (fein 66) von 96 Dellen. Unterklasse bei Laeufen, die vorhergesagt und tatsaechlich kavitieren: 34 von 55 (fein 35 von 55; Zaehlung von Hand) | getroffen (Unterklasse knapp) |
| V-c3 | Klassen grob/fein gleich in >= 90 %; t_kav besteht L3; L = 400 gibt gleiche Klasse und Lueckendichte (Faktor 1,5); sehrfein aendert keine Klasse | Klasse gleich 99 von 100; t_kav 56 von 57. L = 400 und sehrfein: laeuft noch | teilweise (L3 getroffen, Box laeuft noch) |
| Gegenhypothese (L1) | flache oder knappe Dellen zerfallen; oder tiefe, breite Dellen (dF_Pfad_max deutlich ueber F_b) heilen; oder die Klasse haengt von dx oder L ab | flach 0 von 16 und knapp 0 von 16 kavitiert. Die 5 Fehltreffer heilen trotz Vorhersage "kavitiert"; alle sind schmal: 0,70 / 0,72 / 0,75 mittel w = 1, 0,75 mittel w = 2, 0,80 tief w = 1, mit Pfad-Max/F_b 1,08 bis 8,42. dx: 1 Abweichung in 100 (nur Unterklasse). L: laeuft noch | in der vorab genannten Form nicht gesehen; schmale Dellen heilen |

- **Kavitierende Dellen je Tiefe** (grob, Zaehlung von Hand): flach 0/16, knapp 0/16, mittel 10/16, tief 15/16,
  sehr tief 16/16, voll 16/16.
- **Energiekriterium:**
  - Kein Lauf mit Pfad-Max/F_b < 1 kavitierte, grob und fein.
  - Kavitation ab Pfad-Max/F_b 1,01 (w = 4).
  - Geheilt trotz Pfad-Max/F_b >= 1 haben neun Laeufe: vier knappe Dellen (1,00 bis 1,04) und die fuenf schmalen
    (1,08 bis 8,42).
- **L3: bestanden** (Klasse 99 von 100, t_kav 56 von 57). Abweichungen:
  - 0,70 sehr tief w = 4: Kaverne/zerfaellt
  - 0,80 tief w = 8: t_kav 9/12
- **Zusatzprobe CPU gegen GPU** (0,72, T = 400 gegen T = 600): t_kav und groesste Leerlaenge in 14 von 14 gemeinsamen
  kavitierenden Laeufen gleich.
- **Plausibilitaet:** Q-Drift hoechstens 1,3e-15, E-Drift hoechstens 7,4e-5; "plaus ok" 100 von 100 (grob und fein).
- **Latten:** L1 ja, L2 ja, L3 bestanden, L4 vermutlich, L5 Analogie.
- **Vorschlag: weiter.** Das vorab berechnete Energiekriterium trennt heilt/heilt-nicht in 86 von 91 Laeufen, ohne einen
  Fall "kavitiert unter der Barriere"; ob die Klassen bei L = 400 und dx/4 halten, zeigt erst der noch laufende
  Box-Aufruf.

## 2. Kernfragen (nur aus den Berichten)

### RING

- **Ist der Klumpen aus dem mitdrehenden Ring ein m = 1-Q-Ball?** Zeitweise aehnlich, am Ende nicht.
  - **Windung:**
    - In der Klumpenphase nicht im Hauptbericht.
    - Fein ab t = 500 (gemischt mit dem Zerfall): Anteil W = 1 0,551 (N8) bzw. 0,195 (N6).
    - Am Ende W = 0 auf allen Kreisen r = 1 bis 8 in allen Laeufen (sichere Kreise nur in drei N8-Laeufen).
  - **J/Q:**
    - Bei t = 250 bis 500: 0,957 bis 0,989 (N6, N8, N8_ruhend).
    - Am Ende -0,030 bis +0,014, weil kein Klumpen bleibt.
    - N8 grob hinterlaesst einen m = 0-Ball: Q_w 35,66, J/Q -0,0002, W = 0, Profil-L2 gegen m = 0 0,0021,
      omega_eff/omega_m0 0,99998.
  - **Frequenz:**
    - omega_eff bei t = 500: 0,7458 (N8), 0,7558 (N6).
    - Ein Vergleich mit m = 1 gleicher Ladung existiert nur im gemischten spaeten Fenster von fein N8: 1,008 zu
      m = 1, 1,034 zu m = 0.
  - **Profil:**
    - L2 gegen m = 1: Minimum 0,029 (N8_ruhend, t = 500) bzw. 0,053 bis 0,057 (N8, t = 250).
    - Bei N6 nie unter 0,379.
    - E/Q der Klumpen liegt bei t = 500 ueber dem m = 1-Wert benachbarter Ladung.
- **Haelt er lange oder zerfaellt er mit Stoerung?** Er zerfaellt.
  - Ohne Saat: Teilung bei 515 bis 535 (N6), 710 bis 720 (N8), 665 (N8_ruhend).
  - Mit Saat 1e-2: bei 50 (N6) bzw. 60 (N8). Die N6-Reihe 50 / 95 / 145 / 535 waechst mit ln(1/Saat).
  - Die Ladung geht an die Randschicht: Q_Box am Ende 0,339 von 174,3 (N6 grob).
- **Ist der Vierer-Ring gebunden oder bricht er?** Gebunden nur im erzwungen symmetrischen Sektor; sonst bricht er.
  - Im C4-Sektor bis T = 2000 gebunden: Radius 5,55 bis 6,20, Periode 160 (fein 167); dasselbe bei Luecke 6.
  - Ohne Sektor Ladungstausch bei t = 543 (gamma 0,053); mit Saat 1e-6 bei 195, mit 1e-3 bei 81,5.
  - Danach entfernen sich die Baelle (r = 34,4 bei t = 800); bis T geht die Ladung fast ganz an die Randschicht
    (Q-Verlust 0,99).
  - Bei Luecke 8 laufen sie auch symmetrisch auseinander.

### R5F

- **Ist der Rest unter Q_min ein Oszillon?** Nicht gesehen (nur radial, l = 0).
  - Alle vier Laeufe unter Q_min zerlaufen, grob und fein.
  - S_max spaet 1,7e-5 bis 7,8e-5; E_in/E_ref nach t10 + 500 hoechstens 0,006.
  - Spaete Linie ueber 1 (+1,0035 bis +1,0261), Asym +1,00; kein fruehes Plateau.
- **Kommt die Aufnahme unter der Schwelle von der inneren Resonanz, und ist sie linear?** Linear ja; Lage und
  Lebensdauer passen zum vorab bekannten Pol. Dazu kommt eine zweite, nicht vorhergesagte Spitze.
  - Linear: p = 1,99 bis 2,00; C haengt nicht von eps ab (6,0e-2 bis 6,1e-2).
  - Spitzenlage: 2,1196 bis 2,1244 gegen nu_r 2,1183 (0,55); 2,3280 bis 2,3302 gegen 2,3305 (0,70).
  - Abklingrate: 8,4e-3 bis 1,00e-2 gegen 2 Gamma 1,0e-2 (0,55); 1,3e-4 bis 1,43e-4 (0,70).
  - Atmungslinie bei Re rho; dE/dQ nahe nu; Ort 10/20 um 0,9.
  - Paket-Auslaeufer (H1): C(sigma 4)/C(sigma 8) = 6,52e-2 zu 6,00e-2 statt etwa 100; nicht gesehen.
  - Zweite Spitze: bei 0,55 um nu 2,375, bei 0,70 um 2,625, beide unter der Schwelle.
- **Ist die Kavitation echt, und wo liegt die Schwelle?** Gegen Aufloesung (dx/2), Rechengeraet und Kontrollen
  robust; der Test gegen Boxgroesse und dx/4 laeuft noch.
  - Klasse grob/fein 99 von 100; t_kav CPU gegen GPU 14 von 14 gleich; Kontrollen homogen.
  - Schwelle in der Tiefe: Dellen bis S_min 0,637 heilen alle (32 von 32 inklusive flach); ab S_min 0,5 kavitieren
    10 von 16, ab 0,3 15 von 16.
  - Schwelle in der Energie: ohne Ausnahme erst ab Pfad-Max/F_b >= 1,01. Schmale Dellen (w = 1 bis 2) heilen auch
    bei 1,08 bis 8,42.

## 3. Auffaelligkeiten

1. **RING-Bilanz gerissen.**
   - Betroffen sind alle Laeufe mit grossem Randverlust (Q-Rest bis 5,3e-3, J-Rest bis 3,7e-2, E-Rest bis 1,1e-2).
   - Der Rest halbiert sich fein etwa.
   - Nach PLAN 1.3 ist das ein Quadraturfehler der Verlustrate, keine Erhaltungsverletzung. Die vorab gesetzte
     Toleranz ist trotzdem verfehlt.
2. **Windung in der Klumpenphase fehlt.**
   - Die Hauptberichte geben die Windung nur am Ende und als Anteil ab T/2. Weil alle Klumpen vor T/2 zerfallen, ist
     A1 nicht auswertbar.
   - Nur der Rauchtest (T = 150, laut Bericht "Zahlen ungueltig") zeigt W = 1 auf allen Kreisen fuer N6_dreh+,
     N8_dreh+ und N8_ruhend, dazu "n Ende 3" fuer die Saatlaeufe. Das ist nur ein Hinweis.
3. **Nach dem Bruch nicht aufloesungsstabil** (ausserhalb des L3-Kriteriums).
   - N8 bei t = 1000: Q_w 121,5 (grob) gegen 43,6 (fein).
   - Ende: 1 Klumpen (grob, m = 0) gegen 2 (fein).
   - Groesste A_l: l = 3 0,494 (grob, bis 3000) gegen l = 2 0,917 (fein, bis 1000).
4. **Bruchmode bei N6 ohne Saat:** l = 2 dominiert (0,865 gegen l = 3 0,218). Das widerspricht der Vorschau-Aussage
   "3 Klumpen, l = 3". Mit Saat 1e-2 sind l = 2 und l = 3 beide gross (0,917 und 0,859).
5. **Frueherer Befund nur kurz vor dem Bruch gemessen.**
   - R6 ringe (T = 500, "Klumpen mit Windung 1") und R5 Vierer (T = 500, "blieb zusammen") lagen knapp vor den Bruechen
     bei 515 bis 720 bzw. 543.
   - Die Spreizung des Vierers bei t = 500 betraegt in R7 grob 0,0096; PLAN 0.2 nennt fuer R5 0,31.
   - Ohne Saat haengt die Bruchzeit am Rundungsniveau (PLAN 9).
6. **Teilung bei 0,60 spaet und langsam:** t = 1045, gamma 0,0041. Sie setzt die Schwelle unter die Hauptvorhersage;
   ein feiner Lauf dazu fehlt.
7. **l8_sym laeuft auseinander:** r waechst an allen Reihenzeiten, J_Box bleibt 9,4866. Ausserdem dreht l6 mit +1,06e-4
   gegen l4 mit -3,35e-3.
8. **Tod, Laufzeitbild und Spektrum.**
   - Die Dauer ist mehr als doppelt so lang wie (25 - R_E)/v_g.
   - Die Phase sagt omega 1,007 vor dem Tod, die Spektrallinie im Fenster 441,5 bis 642,5 aber +0,969. Mit dOmega 0,0313
     ist das vorhergesagte Band 1,000 bis 1,015 schmaler als die Aufloesung.
   - E_in/E_ref steigt nach t10 + 500 wieder (Stopp-Laeufe grob): 0,005 bis 0,006 (+500), 0,008 bis 0,009 (+1000),
     0,014 bis 0,016 (T = 4000). Die Ursache steht nicht im Bericht.
   - Stopp 0,8 stoppt erst bei t = 732,4, nach t50 = 707,5. Bis dahin ist der Lauf identisch mit dem Dauerabfluss,
     also keine unabhaengige Stopp-Probe.
   - Das Vor-Tod-Fenster des Klumpens ist mit [-104,5; 95,5] angegeben, beginnt also vor t = 0 (dOmega 0,0654).
9. **Fuettern, zweite Spitze unter der Schwelle.**
   - 0,55, sigma 32: C 0,115 bei nu 2,375 (fein 0,110), kappa 3,3e-3, dE/dQ 2,37.
   - 0,70, sigma 32: C 1,55e-3 bei nu 2,625 (fein 1,44e-3), kappa 2,5e-5, dE/dQ 2,61. Schwellen: 2,483 bzw. 2,673.
   - Die Kurzzeile des Berichts ("kleinstes C zwischen Spitze + 0,1 und Schwelle") erfuellt V-b4, verschweigt aber die
     zweite Spitze. Sie erklaert auch die verfehlte V-b5-Erwartung bei nu 2,4.
10. **Fuettern bei 0,70 an der Aufloesungsgrenze.**
    - Bei kleinem C reisst L3; dort stehen negative C (sigma 8, nu 1,925 bis 2,075: -4,4e-7 bis -5,2e-6) und sinnlose
      dE/dQ (384,12; -2,05).
    - Werte unter etwa 2,5e-4 (sigma 8) sind nur als obere Schranke zu lesen.
    - Ueber der Schwelle: C 7,7e-4 bzw. 8,4e-4 gegen Born 1,26e-3; dE/dQ bei 2,8 (sigma 8) 0,976 statt omega 0,8367.
    - R leicht negativ (-0,0014) bei 0,55, nu 2,475, sigma 32.
11. **Kavitation, Unterklasse haengt von der Messzeit ab.**
    - 0,72 auf CPU (T = 400) gegen GPU (T = 600): gleiche t_kav und gleiche groesste Leerlaenge, aber andere
      Unterklasse in 7 von 15 kavitierenden Laeufen.
    - Leerlaenge "Mitte": GPU 62 bis 77, CPU 111 bis 123. "Ende": GPU 67 bis 109, CPU meist 33 bis 47 (zweimal 72,8
      und 110,8).
    - Die Klumpenzahl ist in beiden Unterklassen 15 bis 33.
    - Spaete Kavitation (t_kav 409 bei 0,72 mittel w = 2, 298 bei 0,75 tief w = 1) liegt in dem Zeitraum, den PLAN 7
      fuer zurueckkehrenden Schall nennt; der Box-Vergleich laeuft noch.
12. **Bilanzen R5F unauffaellig.**
    - fuettern: \|Bilanz_Q\| hoechstens 9,9e-6.
    - kavitation: Q-Drift hoechstens 1,3e-15, E-Drift hoechstens 7,4e-5.
    - tod: E_tot-Anstieg nach dem Stopp hoechstens 2,5e-7.

## 4. Zusammenfassung

| Test | Kernvorhersage | Ergebnis | Treffer | L3 | L1 / L2 / L3 / L4 / L5 | Vorschlag |
|---|---|---|---|---|---|---|
| RING-W Wirbelball | Klumpen W = 1, J/Q ~ 1, m = 1-Profil; Dauer offen, nach Vorschau Zerfall N6 bei 350 bis 700 | J/Q 0,96 bis 0,99 bei t = 250 bis 500; Profil kurz nahe m = 1 (N8); Teilung 515 bis 720, mit Saat 50 bis 145; am Ende W = 0 | teilweise | bestanden (vor dem Bruch) | Vorbehalt / ja / bestanden / teilweise / mittelbar | parken |
| RING-T Teilungsschwelle | Schwelle 0,60 bis 0,625 | Schwelle 0,59 bis 0,60 (Q 157 bis 139); 0,60 teilt spaet (1045) | teilweise (7 von 9) | bestanden | Vorbehalt / ja / bestanden / ja / mittelbar | parken |
| RING-V Vierer-Ring | im Sektor gebunden, sonst Bruch mit gamma 0,05 bis 0,10 | Sektor gebunden (Luecke 4 und 6); Bruch 543, gamma 0,053; Saatprobe 0,91; l8_sym auseinander | teilweise (7 von 8) | bestanden | Vorbehalt / ja / bestanden / teilweise / nein | verwerfen |
| RING-K Kontrollen | Bilanz in Toleranz; Schranken erfuellt; L3 | Bilanz gerissen bei grossem Randverlust (Q-Rest bis 5,3e-3); Schranken gerissen; L3 3 von 3 | teilweise | - | ja / ja / - / - / - | entfaellt |
| R5F-a Tod | Rest zerlaeuft; kein Oszillon | zerlaeuft 4 von 4; R5 reproduziert; v_g-Bild verfehlt (Faktor > 2) | getroffen (Hauptfrage) | 22 von 26, Klasse 8 von 8 | ja / ja / bestanden / teilweise / nein | parken |
| R5F-b Fuettern | Resonanz an nu_r, linear, kappa = 2 Gamma | Spitzen auf 0,006 an nu_r, p = 2,0, kappa passt; zweite Spitze unter der Schwelle | getroffen (ausser V-b5) | ueberwiegend (nu_peak 4 von 4) | ja / ja / ueberwiegend / teilweise / nein | weiter |
| R5F-c Kavitation | Energiekriterium trennt heilt/zerfaellt; echt | 86 von 91 getroffen; nie Kavitation unter der Barriere; schmale Dellen heilen; Box laeuft noch | teilweise | bestanden (Raster); Box laeuft noch | ja / ja / bestanden / vermutlich / Analogie | weiter |

## Einfach gesagt

Aus einem Ring kleiner Baelle entsteht fuer einige hundert Zeiteinheiten ein drehender Ball, der fast wie der
berechnete Wirbelball aussieht, aber er zerfaellt jedes Mal, und zwar umso frueher, je staerker man ihn am Anfang
stoert. Vier Baelle im Quadrat halten nur zusammen, solange alles exakt symmetrisch bleibt; die kleinste Unsymmetrie
waechst, bis ein Ball den anderen die Ladung abnimmt. Ein Ball unter seiner Mindestgroesse hinterlaesst keinen
pulsierenden Rest, er laeuft einfach auseinander. Dass ein grosser Ball "verbotene" Wellen schluckt, liegt an einer
Eigenschwingung genau dort, wo wir sie vorher ausgerechnet hatten, und die Rechnung fand dazu eine zweite, unerwartete.
Beim dichten Medium sagt unsere Energieregel gut voraus, welche Delle heilt und welche aufreisst; nur sehr schmale
Dellen heilen oefter als erwartet, und die Pruefung mit groesserer Box laeuft noch.
