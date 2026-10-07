# DANZER-L: Gibt es ein Tetraeder-Netz zwischen Kristall und Glas, einen ikosaedrischen Quasikristall, der von selbst isotrop ist? (Runde 45, Finns Weiche "Kristall oder Glas", Zweig Kristall)

- Leitung claude-primary. Karte und Erwartungen geschrieben ab 2026-10-05 04:16:30 CEST (date), vor jedem Abruf.
- **Finn (05.10., gegen 04:15):** zur Netzart "Teste beides". Der Kristall braucht einen Grund fuer seine Abstimmung (TT-GRUND-1: keine natuerliche Massenregel).
- **Idee der Leitung [H, M]:**
  - Unter der Ikosaedergruppe I_h gibt es Invarianten der Kugelflaechenfunktionen erst bei l = 0, 6, 10, ...
  - Damit sind alle Tensoren bis Stufe 5 isotrop: der elastische Tensor, die TT-Masse und -Steifigkeit langwellig, und der k^4-Term von omega^2 beim Licht.
  - Ein ikosaedrisches Netz haette also keine kubische a2-Anisotropie; die erste Richtungsabhaengigkeit kaeme bei l = 6, also eine Ordnung hoeher.
  - Kandidat aus Tetraedern: die Danzer-Pflasterung (ABCK, vier Tetraeder-Sorten, aperiodisch, ikosaedrisch) [L, zu pruefen].
- Kennzeichen: [S], [S Abstract], [L], [M], [ES], [H].

## Ableitbarkeitsprobe und Projektsuche (vor der Karte)

- **Projektsuche:** "Danzer" kommt im Projekt nicht vor. Ikosaedrische Ordnung nur am Rand: Frank-Kasper (RUNDE-34), 600-Zelle (RUNDE-22), harter Tetraeder-Quasikristall (dodekagonal, TETRAEDER-L).
- **Vorab ableitbar [M, zu pruefen]:** die Gruppenaussage oben. Der Agent prueft sie mit der Charaktertafel bzw. den bekannten Molien-Reihen.
- **Nicht ableitbar:**
  - Gibt es die Danzer-Pflasterung so, und ist sie als Netz mit gemeinsamen Ecken bzw. Flaechen fuer Finn brauchbar?
  - Was sagt die Literatur zur isotropen Phononen-Elastizitaet ikosaedrischer Quasikristalle und zu den Phasonen, den zusaetzlichen weichen Moden?

## Auftrag (feldforscher)

1. **Gruppentheorie am Schreibtisch:**
   - Invariante Kugelflaechenfunktionen unter I und I_h.
   - Folge fuer TT-Moden, elastischen Tensor und Lichtdispersion bis zur Ordnung k^4 (omega^2).
   - Wo steht die erste Anisotropie?
2. **Danzer-Pflasterung:** Prototile, Inflation, Ecken- und Kantenstruktur, Koordination. Ist sie ein "Netz aus Tetraedern" im Sinne Finns, und wie unterscheidet sie sich vom Pyrochlor (Ecken teilend)?
3. **Literatur:**
   - Elastizitaet und Phononen ikosaedrischer Quasikristalle (Isotropie, z. B. Levine u. a. 1985) [L, pruefen].
   - Phasonen als zusaetzliche Freiheitsgrade: Waeren sie in einem fundamentalen Netz zusaetzliche masselose Felder?
   - Gibt es Arbeiten zu Gitter-Feldtheorie bzw. Raumzeit-Modellen auf Quasikristallen (Lorentz-Verletzung, Isotropie)?
4. **Gegensweep:**
   - Verliert man mit dem Quasikristall etwas, etwa Bloch-Zerlegung, Translationsinvarianz oder Impulserhaltung?
   - Folgen daraus Beobachtungsgrenzen?

## Erwartungen (vor jedem Abruf)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| DZ1 | [H] Die Danzer-Pflasterung (ABCK) mit vier Tetraeder-Prototilen und ikosaedrischer Symmetrie ist dokumentiert, mit Inflationsregeln | 85 % |
| DZ2 | [M] Unter I_h sind alle Tensoren bis Stufe 5 isotrop; TT-Tempo und Licht-a2 waeren richtungsunabhaengig, die erste Anisotropie stuende bei l = 6 | 80 % |
| DZ3 | [H] Die Literatur bestaetigt isotrope Phononen-Elastizitaet ikosaedrischer Quasikristalle und nennt Phasonen als zusaetzliche weiche Freiheitsgrade | 75 % |

**Bedeutung (vorab):**
- **DZ1 bis DZ3 treffen ein:** Es gibt eine dritte Antwort auf Finns Weiche: ein geordnetes, aber aperiodisches Tetraeder-Netz mit eingebauter Isotropie, ohne Feinabstimmung und ohne Rauschen.
  - Zu pruefen bleiben dann die Phasonen (zusaetzliche Moden) und eine Rechnung auf einer Naeherungszelle [H].
- **DZ2 verfehlt:** Auch ein ikosaedrisches Netz haette Anisotropie bei k^2; dann bleiben nur Kristall mit Abstimmung oder Glas.

## Rahmen

- feldforscher, Zeitbox 60 min, hoechstens 8 Abrufe (arXiv-API oder arxiv.org per WebFetch, Verlagsseiten nur frei), keine Websuche.
- Erwartung mit date-Zeit vor jedem Abruf in ARBEITSFELD.md.
- Schreiben nur in RUNDE-37/danzer-l/.
