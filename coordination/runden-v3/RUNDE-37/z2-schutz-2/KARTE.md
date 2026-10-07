# Z2-SCHUTZ-2: Haengt die Barriere des Spin-Vorzeichens auf Finns Netz an der Kerngroesse oder an der Netzgroesse? (Runde 49, Folgekarte aus Z2-SCHUTZ-1)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 14:11:50 CEST (date), vor jeder Rechnung.
- **Herkunft [P]:**
  - Z2-SCHUTZ-1 (RUNDE-37/z2-schutz-1/ERGEBNIS.md): Weg 360 -> 0 Grad auf Finns Diamant-Netz (Einheitsquaternion-Feld, Guertel-Energie). Beschreibend: Barriere 25,03 auf G1 = (10, 20), 41,40 auf G2 = (12, 24), +65 %; Sattel ein kleiner gesprungener Fleck an der Kernoberflaeche mit einem negativen Hesse-Eigenwert. G3 = (14, 28) blieb in einem Zwischenminimum haengen; die Bisektion hatte einen Fehler im Abbruchkriterium.
  - G1 bis G3 skalieren Kern und Kugel zusammen; das Wachsen kann am Kern liegen.
  - Finn: "Oder eine Drehdimension dann quasi mit Spin".
- Kennzeichen: [M], [E], [P], [H].

## Ableitbarkeitsprobe (Leitung)

- **Vorab [M, P]:** Eine Bindung bei omega = pi kostet 4 (Guertel-Energie); die Barriere ist endlich (SO(3)^N zusammenhaengend). Sitzt der Sattel an der Kernoberflaeche, sollte die Barriere mit der Zahl der Bindungen dort wachsen, also etwa mit der Kernoberflaeche, und von der Kugel weit draussen kaum abhaengen.
- **Nicht ableitbar:** die tatsaechliche Abhaengigkeit von Kern- und Kugelradius; ob der Sattel lokal bleibt.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| ZT0 | Kontrolle [P]: Auf G1 = (10, 20) gibt der Code die Barriere 25,03 mit beiden Verfahren (korrigierte Bisektion und CI-NEB) auf 1e-3 relativ wieder | 85 % |
| ZT1 | [H] Bei festem Kern (wie G1) aendert sich die Barriere um weniger als 10 %, wenn der Kugelradius von 20 auf mindestens 28 waechst | 60 % |
| ZT2 | [H] Bei fester Kugel waechst die Barriere mit dem Kernradius etwa wie die Kernoberflaeche (Exponent 1,5 bis 2,5 ueber mindestens drei Kernradien) | 45 % |
| ZT3 | [H] Am Sattel liegen auf allen gueltigen Groessen mindestens 50 % der Barrierenenergie in hoechstens 10 Bindungen | 50 % |

**Bedeutung (vorab):**
- **ZT1 trifft ein:** Das Spin-Vorzeichen ist auf Finns Netz nur oertlich und energetisch geschuetzt (eine endliche Schwelle an der Kernoberflaeche). Exakter halber Spin braucht dann eine Zusatzregel, die Gittersprung verbietet (Zulaessigkeit) [L].
- **ZT1 verfehlt (Barriere waechst mit der Kugel):** Der Schutz ist kollektiv; das waere ein Hinweis auf einen echten topologischen Sektor.

## Rahmen

- Code-Agent. Code aus RUNDE-37/z2-schutz-1/code (eingefroren) kopieren und nur in Kopie aendern: Bisektion mit korrigiertem Abbruchkriterium, bessere Relaxation fuer grosse Kugeln. Die Aenderungen vor dem Einfrieren im Plan begruenden und gegen G1 pruefen (ZT0).
- Raster: fester Kern (wie G1) mit Kugelradien 20, 24, 28 (und groesser, falls in 10 min machbar); feste Kugel mit mindestens drei Kernradien.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu und cpu7. Je Lauf hoechstens 10 min. Zeitbox 120 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
- Synthetisch (Modellfeld), keine Messdatenbestaetigung.
