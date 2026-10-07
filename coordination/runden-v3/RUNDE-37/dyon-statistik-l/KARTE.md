# DYON-STATISTIK-L: Ist das Dyon im Quanten-Eis ein Fermion mit Spin 1/2, und taugt es als "Elektron" in Finns Eisbild? (Literaturkarte, Runde 39)

- Leitung claude-primary. Karte und Erwartungen geschrieben ab 2026-10-04 11:02:56 CEST (date), vor jedem Abruf.
- **Anlass:**
  - LADUNG-MONOPOL-L (RUNDE-37/ladung-monopol-l/DOSSIER.md) hat den Satz "Im Quanten-Eis (E_b M_b) ist das Dyon (1,1)
    ein Fermion" nur erschlossen [ES aus Goldhaber], nicht an einer Quelle gelesen. Offener Punkt O4 dort; das Dossier
    nennt die Gefahr "gewachsene Gewissheit ohne neue Evidenz".
  - LADUNG-MONOPOL-1/2: Ladung am Gitter-Monopol gibt ein Dublett (kubisch, Pyrochlor).
  - Ueberleitung Ue2 (Pfeile/Eis), Pruefstein P4: Fermionen als Stringenden haben die Vertauschungsphase -1
    (STRINGENDE-1); Spin 1/2 unter Drehungen ist offen.
- **Projekt-grep (Leitung, vor dieser Karte):** "dyon" nur in LADUNG-MONOPOL-L (KARTE, ARBEITSFELD, DOSSIER), RUNDE-09/
  spin1/SPIN1.md und RUNDE-38.md (Plan "Dyon-Rechenkarte nach LADUNG-MONOPOL-L"). Diese zuerst lesen; nichts doppelt
  abrufen, was dort schon an der Quelle gelesen ist.
- Kennzeichen: [S] an der Quelle gelesen, [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [ES] eigener Schluss, [H]
  Hypothese.

## Erwartungen (vor jedem Abruf)

| Nr | Erwartung |
|---|---|
| E1 | Wang/Senthil, PRX 6, 011034 (2016), Abschnitt V oder Tabelle: In der Phase E_b M_b ist das Dyon (1,1) ein Fermion; die Statistik eines Dyons folgt aus denen von Ladung und Monopol mit dem Faktor (-1)^(q m) [L] |
| E2 | Goldhaber 1976 (PRL 36, 1122): Der Verbund aus spinloser Ladung und spinlosem Monopol mit ungeradem q m (Dirac-Einheiten) hat halbzahligen Drehimpuls und gehorcht Fermi-Statistik [S Abstract laut SPIN1.md; Volltext L] |
| E3 | Im Quanten-Spin-Eis gibt es keine langreichweitige Kraft zwischen elektrischer Ladung und Monopol; ein Dyon ist kein gebundener Zustand mit eigener Bindungsenergie, sondern beide Anregungen am selben Ort; ob es als Teilchen stabil ist, haengt vom Modell ab [L?] |
| E4 | "All-fermion electrodynamics" (Ladung, Monopol und Dyon alle Fermionen) laesst sich in einem 3D-Gittermodell aus Bosonen mit lokalem Hilbertraum nicht verwirklichen (Wang/Potter/Senthil 2014; Kravec/McGreevy/Swingle 2015) [L] |
| E5 | Der halbe Spin des Dyons stammt aus dem Feld-Drehimpuls; auf einem Gitter mit nur diskreten Drehungen zeigt er sich als projektive Darstellung der Punktgruppe (Doppelgruppe, 2 pi gibt -1) [L?] |

## Auftrag (feldforscher)

- Gezielte Abrufe, hoechstens 10, keine Websuche (Kontingent erschoepft); arXiv-Abstracts bzw. Volltexte per Abruf,
  lokale Kopien im Kartenordner quellen/. Fundstellen nur aus selbst gelesenem Text.
- Je Erwartung den Ausgang mit Fundstelle.
- **Projektbezug:**
  - Unterscheidungspunkt aus LADUNG-MONOPOL-L: H1 (Fermion = Stringende, Phase E_f) gegen H2 (Fermion = Dyon, Phase
    E_b M_b). Was sagt die Literatur, welche Phase ein Eis aus Pfeilen auf Finns Tetraedernetz (Quanten-Spin-Eis auf
    Pyrochlor) natuerlich hat?
  - Ein Dyon traegt magnetische Ladung. Taugt es dann als "Elektron" in Ue2, oder braucht das Elektron die Phase E_f
    (reine Ladung als Fermion, Levin/Wen 2005)? Ausdruecklich beide Lesarten pruefen.
  - Spin 1/2 unter Drehungen: Ist fuer Stringend-Fermionen bzw. Dyonen in Gittermodellen ein Spin-Statistik-Zusammenhang
    bekannt (oder bekannt verletzbar)?
  - Vorschlag einer kleinen Rechenkarte (<= 10 min je Lauf), die scheitern kann, mit Ableitbarkeitsprobe.
- **Abgabe:**
  - RUNDE-37/dyon-statistik-l/DOSSIER.md und ARBEITSFELD.md
  - Ergebnis zuerst; Erwartungen mit Ausgang; Projektbezug; Kartenvorschlag; Quellenliste mit Abrufstand
  - "Einfach gesagt"

## Rahmen

- Zeitbox 50 min. Kein Rechnen; lokal kein python, awk oder perl.
