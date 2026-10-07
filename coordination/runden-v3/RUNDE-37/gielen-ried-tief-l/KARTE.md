# GIELEN-RIED-TIEF-L: Was zeigt "Unimodular boundary time for Regge calculus" genau, und was folgt fuer Finns Takt? (Runde 49, Finns Auftrag)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 12:23:53 CEST (date), vor jedem Abruf.
- **Herkunft:** Finn, 05.10.2026, Eingang vor 12:23:53, woertlich: "Check das Tetraeder netz Artikel Ding direkt intensiv". Gemeint ist Gielen/Ried, arXiv 2610.03479 (02.10.2026), vom arXiv-Scout gemeldet.
- **Projektbefunde [P]** (nicht als neu fuehren):
  - WELTKRISTALL-L (RUNDE-37/weltkristall-l/DOSSIER.md und ARBEITSFELD.md) hat v1 schon an der Quelle gelesen:
    - Abschn. III: "unimodular time has an interpretation as a volume time".
    - Abschn. IV: Die verfeinerte 600-Zellen-Fassung [5] (Dittrich/Gielen/Schander 2022) passt besser zum Kontinuum.
    - Abschn. V: Klassisch sind die Loesungen "mostly the same as the ones of standard Regge calculus". Unterschiede: die Rolle von Lambda und "the constraint that compact spacetimes without boundary must have zero 4-volume". Beide Modelle beruhen auf der 5-Zelle.
    - Schreibtisch dort [ES]: Im Collins/Williams-Modell mit 600-Zellen-Schnitten ist der unimodulare Zeitschritt das 4-Volumen der Schicht, also eine Zaehlung. "Finns Takt zaehlt Volumen" ist damit Gielen/Rieds unimodulare Zeit.
  - GRUNDGLEICHUNG-SKIZZE-v2.2 (RUNDE-49), Abschnitt 4: Maximale Scheibung K = 0 ist auf dem geschlossenen Torus nur in linearer Naeherung zulaessig; York-Zeit braucht ein sich aenderndes Volumen.
  - SKALAR-SEKTOR-L: Ein globaler Takt im projizierbaren Horava-Sinn scheidet nach heutigem Stand aus.
  - REGIME-K-1 laeuft (euklidische 4D-Regge-Hesse mit Zeltstangen).
- Kennzeichen: [M], [S] (mit Abschnitt, Gleichung oder Seite), [S Abstract], [L], [P], [ES], [H].

## Ableitbarkeitsprobe (Leitung)

- **Vorab ableitbar [M]:**
  - Bei Henneaux-Teitelboim ist die unimodulare Zeit T zu Lambda konjugiert; T(2) - T(1) ist das 4-Volumen zwischen den Scheiben [L, Standard].
  - **Monotonie:** Die unimodulare Zeit waechst bei jeder Blaetterung mit N > 0, auch auf einem ruhenden, geschlossenen Torus (Zuwachs Volumen mal Eigenzeit). Anders als die York-Zeit (dort konstant null) taugt sie also auch auf dem ruhenden Torus als Uhr.
  - In einer Regge-Zerlegung ist das 4-Volumen die Summe der 4-Simplex-Volumina. Bei gleich grossen Bausteinen ist es eine Zaehlung.
- **Nicht ableitbar:**
  - was die Arbeit genau rechnet (Modell, Gleichungen, Kontinuumslimes)
  - wie die Bedingung "geschlossene Raumzeit ohne Rand hat 4-Volumen null" zustande kommt und was sie fuer periodische Rechnungen (Torus in der Zeit, Bloch) bedeutet
  - ob sich die unimodulare Zeit als oertlicher bzw. globaler Takt in einer Zeltstangen- oder 3+1-Entwicklung auf einem allgemeinen Netz nutzen laesst
  - was die bekannten Einwaende gegen unimodulare Zeit als Uhr bedeuten (Unruh/Wald 1989; Kuchar 1991)

## Vorhersagen (vor jedem Abruf)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| GR1 | [S Abstract] Die Arbeit diskretisiert Henneaux-Teitelboim-Gravitation mit euklidischem Regge; die unimodulare Zeit ist eine Randgroesse, zu Lambda konjugiert, und ihr Unterschied ist das eingeschlossene 4-Volumen (Summe der 4-Simplex-Volumina) | 90 % |
| GR2 | [P] Getestet wird nur in symmetriereduzierten Modellen aus 5-Zellen-Schichten; die Ergebnisse stimmen mit frueherer Literatur ueberein | 80 % |
| GR3 | [H] Die Arbeit behandelt weder Lorentz-Signatur noch Materie noch ausbreitende Schwerewellen | 80 % |
| GR4 | [H] Die Bedingung "geschlossene Raumzeit ohne Rand hat 4-Volumen null" macht zeitlich periodische (euklidisch geschlossene) Zerlegungen in der unimodularen Fassung zu Sonderfaellen ohne Volumen; die Arbeit sagt das so oder gleichwertig | 60 % |
| GR5 | [H] Der Kontinuumslimes wird bei festem Unterschied der unimodularen Zeit (festem 4-Volumen zwischen den Raendern) definiert, und die Konvergenz ist nur im reduzierten Modell gezeigt | 70 % |
| GR6 | [H] Die Arbeit gibt ein Rezept, mit dem man auf einer allgemeinen, nicht symmetrischen Zerlegung die unimodulare Zeit als Uhr verwenden kann (nicht nur als Randdatum im Pfadintegral) | 40 % |
| GR7 | [L] Die Einwaende von Unruh/Wald 1989 bzw. Kuchar 1991 (unimodulare Zeit loest das Zeitproblem der Quantengravitation nicht) werden in der Arbeit erwaehnt | 50 % |

**Bedeutung (vorab):**
- **GR1, GR2, GR3 treffen ein:** Die Arbeit liefert die Uhr (4-Volumen zaehlen), aber keine Dynamik fuer Finns Netz. Brauchbar ist sie als Takt-Definition fuer die Grundgleichung (Lambda als Integrationskonstante), nicht als Test der Schwerewellen.
- **GR4 trifft ein:** Unsere periodischen euklidischen Rechnungen (Bloch in der Zeit) sind fuer die unimodulare Fassung nicht direkt geeignet; die Uhr braucht Raender (Anfang und Ende).
- **GR6 trifft ein:** Direkter Weg zu einer Rechnung "Finns Takt = unimodulare Zeit" auf unseren Netzen (Folgekarte).

## Fragen

1. Was genau wird definiert und gerechnet (Abschnitte, Gleichungen)? Wie geht Lambda ein, was sind die Randdaten, wie lautet die diskrete Wirkung?
2. Welche Modelle (5-Zelle, 600-Zelle?) und welche Ergebnisse (Tabellen, Konvergenz, Vergleich mit Kontinuum und frueherer Literatur)?
3. Die Bedingung "4-Volumen null fuer geschlossene Raumzeiten": Herleitung und Folgen.
4. Lorentz-Fassung, Materie, Schwerewellen, kanonische bzw. Zeltstangen-Entwicklung: erwaehnt, ausgeschlossen, als Ausblick?
5. Einwaende und Gegenpositionen (Unruh/Wald 1989, Kuchar 1991, neuere Arbeiten 2024 bis 2026): Was sagen sie, was sagt die Arbeit dazu?
6. Fuer Finns Netz [ES/H]:
   - Kann Finns Takt die unimodulare Zeit sein, und als globale oder als oertliche Uhr?
   - Was hiesse das fuer die Grundgleichung (Lambda als Integrationskonstante statt fest; Verhaeltnis zu K = 0 und York-Zeit; Torus)?
   - Welcher billige Netztest folgt daraus?

## Rahmen

- feldforscher nach Feld-Regeln:
  - Arbeitsdatei ARBEITSFELD.md, Ergebnis DOSSIER.md, beide in diesem Kartenordner.
  - Volltext zuerst (arXiv HTML oder PDF per curl in quellen/).
  - Erwartung vor jedem Abruf, Gegensweep (24 Monate), Erwartungsverstoesse, Negativliste.
- Hoechstens 15 Abrufe, Zeitbox 90 min. Keine Rechnung.
- Literatur, keine Messdatenbestaetigung.
