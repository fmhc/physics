# SKALAR-MISCH-1: Traegt die Quer-Laengs-Mischung der Bewegungsenergie die Restleckage auf Finns Netz V, und lassen Gewichte je Tetraederart beide Fehler zugleich verschwinden? (Runde 48, Folgekarte zu SKALAR-SEKTOR-L)

- Leitung claude-primary. Karte geschrieben ab 2026-10-05 09:01:58 CEST (date), vor jeder Rechnung.
- **Herkunft:** Kartenvorschlag aus SKALAR-SEKTOR-L (RUNDE-37/skalar-sektor-l/DOSSIER.md, Abschnitt 9). Frage, Rechnung, SM1, SM2, Ableitbarkeitsprobe und "Kann scheitern" sind **woertlich bindend**.
  - Hintergrund [P]: Die Restleckage aus IMPULS-NETZ-1 kommt nicht von einem Zusatzskalar, sondern vermutlich von einer l = 4-Fehlkopplung an die TT-Moden ueber die langwellige Bewegungsenergie A.
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Frage (woertlich)

- Traegt die langwellige Quer-Laengs-Mischung der reduzierten Bewegungsenergie (nn-Anteil des Kopplungsvektors e_j) den Bahnlagen-Gang 0,004077 der Kreisbahn-Leckage?
- Verschwinden beide mit einer zusaetzlichen Bedingung an die Gewichte je Tetraederart, bei erhaltener TT-Isotropie?

## Rechnung (woertlich; .69, Kleintest-Spur, je Lauf < 10 min)

1. Fuer 200 Richtungen bei kl = 0,01 den nn-Anteil von e_j je TT-Zweig ausgeben (IMPULS-NETZ-1-Code, J_iso).
2. Vorab im Plan die Winkelformel festlegen, die daraus G_rad fuer die 12 Bahnen aus 5.2 vorhersagt; dann vergleichen.
3. Gewichte je Tetraederart (kubisch symmetrisch) so waehlen, dass TT-Spanne und Quer-Laengs-Mischung zugleich klein werden. Die Zahl der freien Gewichte und der Bedingungen vorab zaehlen.

## Vorhersagen (woertlich, vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| SM1 | [H] Die Winkelformel aus Schritt 2 trifft den Koeffizienten 0,004077 auf 10 % | 50 % |
| SM2 | [H] Es gibt Gewichte mit TT-Spanne < 1e-6 und Bahnlagen-Gang < 1e-5 | 30 % |
| SM3 | [H] (Zusatz der Leitung) Es gibt Gewichte, bei denen TT-Spanne und Bahnlagen-Gang beide auf Rechengenauigkeit verschwinden (< 1e-12), also eine exakte Loesung. Nur so koennte ein Kristallnetz GW170817 (~1e-15) ohne Glueck erfuellen | 15 % |

- **Ableitbarkeitsprobe (woertlich):**
  - Vorab ableitbar: C_nn = 0 bei [100] und [111] (Symmetrie, IMPULS-NETZ-1 5.3 [P]); TT-Isotropie mit zwei Verhaeltnissen moeglich (TT-ISO-1 [P]); der isotrope Anteil des Gangs ist +1,35e-4, nicht null (0,6331 statt 3/5) [M].
  - Nicht ableitbar:
    - ob der nn-Anteil allein den Gang traegt; V1 fehlt in der Bahnrechnung, und TT- und nn-Anteil koennen interferieren;
    - ob ein lokaler Gewichtssatz beide Bedingungen zugleich erfuellt.
- **Zusatz der Leitung zur Probe (Kennzahlen-Abgleich):**
  - TT-ISO-1 erreichte mit zwei Verhaeltnissen eine Spanne von ~1e-5, nicht null. SKALAR-SEKTOR-L nennt fuer V mit J_iso 1,1e-5.
  - Vor dem Plan klaeren, ob das ein Rundungsrest der Abstimmung ist oder eine Grenze der Gewichtsfamilie. Davon haengt SM3 ab.
- **Kann scheitern (woertlich):**
  - SM1 verfehlt: Dann sitzt die Leckage anderswo (V1, Reduktion R1), und Kette K2 ist falsch.
  - SM2 verfehlt: Dann kann Netz V mit lokalen Gewichten nicht beides. Es braucht die kovariante 4D-Zeit (Regime K) statt einer gesetzten Bewegungsenergie.
- **Abgrenzung (woertlich):** Das ist nicht Codex Rang 2 (Korrekturbasis der Zwangsdynamik). Hier aendern sich nur die [F]-Gewichte von A; Codex' Arbeit wird nicht nachgerechnet.

## Rahmen

- Code-Agent, Code aus impuls-netz-1/code und tt-iso-1/code kopieren, dort nichts aendern.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu5 und cpu6, ein Thread. Je Lauf hoechstens 10 min. Zeitbox 120 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
- Synthetisch, keine Messdatenbestaetigung.
