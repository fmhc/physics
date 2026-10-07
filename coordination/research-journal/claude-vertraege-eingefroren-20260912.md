# Zwei Verträge eingefroren: Bucky-Jojo (dynamisches Aufrollen) und Faden-Vertrag 1 (s4-Rotor nichtlinear)

- Zeit: 2026-09-12T04:40:29+0200
- Quelle: Finn-Freigabe (Relais claude-x1: "ok mach beide vertraege auf .69"); coordination/vertraege-20260912/*.json mit allen Hashes (Skripte, Startdateien, Vorprüfungen, Modell run.py bitgleich); Zettel 3b1153d2 und 0b98db16
- Ergebnis: Beide Verträge vor dem ersten Produktionslauf mit Raster, Kriterien, Abnahmegrenzen und vorab benannten Ausgängen fixiert. Bucky-Jojo: 40 Starts (24 Haupt, 16 energiegleiche Atemkontrollen), Verlet h = 0,01/0,005, T = 2000, Ereignis D/Lc ≤ 0,15 ∧ K ≥ 3π/2 ∧ Rg²-Abfall ≤ 0,60 über ≥ 500 τ. Faden 1: 12 J-Starts (sechs Richtungen, sechste = zd als Ersatz für die nicht realisierbare Kippung aus der Ebene) plus 6 J0-Kontrollen, Amplitude 1e-2, Umgebung 0,05, T = 800, h = 0,005/0,0025.
- Bedeutung: Rechner claude-x1 auf .69 CPU. Ergebnisse gehen erst nach Abnahme gegen diese Dateien ins Register; Ausgänge A/A'/B bzw. A/B sind vorab festgelegt. Marken-Grenze: astra-Läufe heute sind Finns Entscheidung.

- Nachtrag 2026-09-12T05:16:59+0200: dritter Vertrag zellteitung:viermassen-bruecke v1 eingefroren (Hashes geprueft, Vorpruefung Kraft-FD 1,2e-9, Muldenboden -1, Kruemmungen 24, Erhaltung 2,4e-9 D), Rechner astra-viermassen auf .69 CPU; Startsignal gesendet. Vertragsdatei sha256 76cf3d4dd2d33f9b.

- Nachtrag 2026-09-12T06:42:03+0200: Vertrag 6 hcl-morse-rotor v1 eingefroren (Hashes geprueft, Kratzer/Pekeris-Formeln nachgerechnet, Vorhersage vor Produktion offengelegt: D_rot 5,316e-4 und alpha_e 0,2775 cm^-1 fuer H35Cl; Erwartung B wegen alpha). Rechner astra-hcl .69 CPU. Vertragsdatei sha256 abcb301e44629edc.

- Nachtrag 2026-09-12T06:47:58+0200: Vertrag 1b (s-Sweep, GPU) eingefroren, sechs Hashes bestaetigt, CUDA-Validierung 24/24 bitgenau, gestaffelte Energieabnahme festgelegt (Standard 1e-8; dx/zx 1e-5 + h^2-Faktor; linear instabil 2*50h^2); Startsignal inkl. dx+- Numeriknachtrag fuer Vertrag 1. Handlungsanweisung Jury ohne OpenRouter: Abschnitt 9 Entscheidung (weite Befangenheitsregel, Kandidatenersatz bei Kalibrierbruch). Vertragsdatei 1b sha256 173e8dfb61dd4e64.

- Nachtrag 2026-09-12T08:02:31+0200: Vertrag 4 Morse-Kette/Helix Rev. 12b eingefroren (Skript 5f53014a, 272 Starts: 252 F_J + 20 starr, J_stat,H je N/B gebucht, id 67 vertragsgemaess veraendert); Startsignal bedingt auf CUDA-QA-Hash. Vertragsdatei sha256 0b5eb3c125dbb93e.

- Nachtrag 2026-09-12T12:20:07+0200: Vertrag 5 verkettete Ringe eingefroren (morse_ringe.py 2eadfbc0, 51 Starts, Pruefung bestanden, Lk exakt); sechs Vorab-Entscheidungen gebucht; Startsignal bedingt auf CPU/CUDA-Vergleich (GPU nach Morse). Vertragsdatei 63b564a1c47730d8.
