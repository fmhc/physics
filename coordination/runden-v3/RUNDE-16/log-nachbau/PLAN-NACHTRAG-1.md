# PLAN-NACHTRAG-1 (LOG-NACHBAU, Runde 16), NACHTRAEGLICH

- Verfasst: 2026-10-02 ab 08:14:51 CEST (date), nach den Hauptlaeufen. Ob die Folgelaeufe gelten, entscheidet die Leitung.
- Anlass:
  - Die Hauptlaeufe nach PLAN.md.eingefroren-20261002-080809 lokalisieren im Log-Modell genau einen Kandidaten bei
    w^2 = 0,925610, rho = 1,837996.
  - Beide Stufen geben Umlauf -1 (roh -1,0000). Der groesste Sprung bleibt nach den geplanten 6 Halbierungsrunden
    bei 2,46 rad (76 Randpunkte).
  - Nach der eingefrorenen Regel ist der Kandidat damit nicht aufgeloest und gilt nicht als gefunden. Dieser Befund
    bleibt stehen.
- Vermutete Ursache (Hypothese):
  - Starke Anisotropie. Auf diesem Ast ist s klein (1e-6 bis 1e-4), G_b aendert sich mit rho um O(1) je Einheit.
  - Am Rand faellt |W| bis 1,8e-6 bei einem Maximum von 3,3e-3. Die Phase dreht in einem Randstueck von etwa 1e-6.
  - 6 Halbierungen von 1,25e-4 reichen dafuer nicht.

## Folgelauf F1 (nachtraeglich)

- Unveraendert:
  - Rechteck (Halbbreiten 1e-3), 16 Anfangspunkte je Kante
  - Halbierungsregel, Kriterium groesster Sprung < 0,4 rad
  - Stufen, Code der Rechnung (stille_n1.py = stille.py plus Unterbefehl "umlauf", der Runden und Halbbreite als
    Argument nimmt)
- Geaendert: hoechstens 24 statt 6 Halbierungsrunden.
- Punkte:
  - je Stufe der in den Hauptlaeufen lokalisierte Log-Punkt dieser Stufe
  - je Stufe der lokalisierte K1-Punkt (Gegenprobe, dass die Aenderung K1 nicht beruehrt)

## Folgelauf F2 (nachtraeglich, informativ)

- Wie F1, aber Halbbreite 1e-4. Zeigt, ob der Umlauf von der Rechteckgroesse abhaengt. Nur fuer den Log-Punkt.

## Auswertung

- Gleiche Regel wie PLAN.md Abschnitt 6.
- F1 und F2 werden getrennt als nachtraeglich berichtet und ersetzen den Hauptbefund nicht.
