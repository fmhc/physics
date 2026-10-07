# T4.3: C1-Korrektur der Bootstrap-Gewichte, Neulauf durch claude-x1

- Zeit: 2026-09-12 01:32 UTC (Lauf 2 auf .69), Register 04:20
- Quelle: claude-x1, coordination/t4-grenzverhalten-20260911-v2.md (SHA 89379b57...), ergebnis.json (SHA 92a5a52f...), Skript funktionsfamilie_grenz69_v2.py (SHA a1a82819...), astra-Review 8/8 PASS; Verdichtung T4-ERGEBNIS-kurz.json von claude-primary
- Ergebnis: Fehler aus Runde 5 (codex-jury-a, C1) bestaetigt und behoben: Berichtsgewicht w*sqrt(mult) statt w*mult in der Bootstrap-Streuung; Fit unberuehrt. Gewichtspruefung gegen explizite Zeilenvervielfachung: relative Abweichung hoechstens 3,7e-16, alte Variante 1,16 Prozent daneben. Neue gepaarte sd gegen F10: F8 0,25 (vorher 0,24), F2 2,58 (2,90), Originalformen 5,74/9,96 (6,8/11,9). Alle nominalen Werte bitgleich zu Lauf 1. Streuungen Faktor 1,18 bis 1,19 groesser, Abstaende in sd 10 bis 20 Prozent kleiner, kein Befund kippt; vorab benannte Erwartung eingetreten.
- Bedeutung: T4.3 im Laufregister angelegt (offen, ersetzt T4.2), Hauptregister-Nachtrag. Einschraenkung (Standardform F2 ueber 2 sd) bleibt. Runde 7 erst nach Nutzerfreigabe oder Tageswechsel (Marken).
