# DS-EICHUNG-2D-1: Vorab-Datei (vor jeder Rechnung)

- Rechenagent (Claude-Subagent fuer die Leitung claude-primary). Karte und Erwartungen E1 bis E4 bleiben unveraendert.
- Synthetisch, keine Messdaten.

## Messmethoden (genau wie in NETZ-DYN-1, Funktionen unveraendert importiert)

- Netz = duales Netz (Dreiecke bzw. Vierecke als Knoten, Nachbarn ueber gemeinsame Kanten): `netzdyn.schalen`, `netzdyn.rueckkehr`, `netzdyn.ds_kurve`.
- d_s: traege Diffusion (Haltewahrscheinlichkeit 1/2), exakte Verteilungsrechnung, 24 Startpunkte je Konfiguration, sigma bis 600,
  d_s(sigma) = -2 dlnP/dln sigma (zentrale Differenz), gemittelt P ueber Konfigurationen.
- d_H lokal: Schalen n(r) aus 16 Startpunkten je Konfiguration, gemittelt; Steigung von ln n gegen ln r im Fenster r = 6 bis 20
  (Funktion `auswertung.dh_fenster`), d_H = 1 + Steigung; zusaetzlich die zentrale lokale Kurve 1 + dln n / dln r.
- d_H Skalierung: mittlerer Abstand <r> = Summe r n(r) / Summe n(r) aus den gemittelten Schalen (`auswertung.mittl_abstand`),
  d_H = ln(N_a/N_b) / ln(<r>_a/<r>_b) fuer Paare von Groessen (hier auch Anpassung ueber alle Groessen).
- Abweichung bewusst: sch_rmax = 150 wie bei s0a2/s0b2 (volle Schalen), damit <r> nicht abgeschnitten wird; Abschneideflag wird gemeldet.

## Ensemble-Erzeugung

- (a) Gleichfoermige Zufallsviereckskarten der Kugel (2D-Quantengravitation, gleiche Universalitaetsklasse, d_H = 4, d_s = 2 [L])
  ueber die exakte Cori-Vauquelin-Schaeffer-Bijektion (gut markierter Baum, unabhaengige Stichproben, N = 10^3 bis 10^5 Vierecke).
  Pruefung je Probe: Eulerzahl 2, alle Flaechen Vierecke, Dual 4-regulaer. Das sind **Vierecke, nicht Dreiecke**; ein exakter
  Dreieckssampler (Poulalhon-Schaeffer) wurde aus dem Gedaechtnis nicht sicher genug gebaut.
- (b) Zufallstriangulierungen der Kugel (einfach, Dual 3-regulaer) per Flip-Markov-Kette (Start: Doppelpyramide-aehnliche Kugel,
  lange Thermalisierung), nur kleine bis mittlere N (Python, 10-min-Grenze). Aequilibrierung ueber Zeitreihe von <r> geprueft.
- (c) 1+1D-CDT: unveraendertes netzdyn (`--modus cdt2`), Torus T x Ring, mehrere N bis ~6e4. Dazu Pruefung der Aequilibrierung
  (Relaxation des Profils), weil die 16000er Probe in D1 nur ~1600 Sweeps hatte, die 4000er 4400.

## Eigene Erwartungen (vor jeder Rechnung)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| V1 | Viereckskarten: d_s im Plateau (sigma ~ 20 bis 200) bei 2,0 +- 0,1 | 70 % |
| V2 | Viereckskarten: d_H aus <r>-Skalierung im Fenster 3,7 bis 4,3 (Endlichgroessen-Korrekturen von <r> sind gross, N_a/N_b >= 10) | 50 % |
| V3 | Lokale d_H (r 6 bis 20) auf den Viereckskarten liegt unter der Skalierung (unter 4) | 85 % |
| V4 | CDT bei groesserem N: lokale d_H (r 6 bis 20) bleibt >= 2,2 (kein Verschwinden der Verschiebung) | 65 % |
| V5 | CDT: die <r>-Skalierung geht bei gleichgewichtiger Probe auf unter 2,15 (D1-Wert 2,23 ist teilweise Nichtgleichgewicht der 16000er Probe) | 45 % |
| V6 | Lokale Verschiebung (E4) ist auf CDT und DT **nicht** gleich gerichtet: CDT lokal ueber 2, DT lokal unter 4 | 60 % |
| V7 | Urteil: D1 d_H = 2,3 ist ueberwiegend Fensterartefakt des lokalen Schaetzers (Achsenabschnitt in n(r) = a r + b), nicht Fehler im Netzkern | 55 % |

## Was als Ergebnis gilt

- Gemessene Zahlen mit Probenzahl und Streuung; Nichtgleichgewicht und Abschneidung offen melden. Keine Anpassung der Fenster nach dem Befund
  (Fenster r 6 bis 20 und sigma-Bereiche wie in NETZ-DYN-1; weitere Fenster nur zusaetzlich und als solche gekennzeichnet).
- Geschrieben ab 2026-10-07 03:00 ca., Vorab-Datei fertig 2026-10-07 03:05:00 CEST (date), vor dem ersten Lauf.
