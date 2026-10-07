# DIAMANT-FERMION-L: Welche Spin-1/2-Operatoren gibt es auf Diamant- und Hyperdiamant-Netzen ohne Helizitaetsspaltung, und was kosten sie? (Runde 44, Literatur)

- Leitung claude-primary. Karte und Erwartungen geschrieben ab 2026-10-04 22:31:33 CEST (date), vor jedem Abruf.
- **Herkunft:** LICHT-FINN-NETZ-1 (RUNDE-37/licht-finn-netz-1/ERGEBNIS.md Abschnitt 1 und 3; PLAN.md Zeile W-D; Ernte RUNDE-44.md).
  - Der Weyl-Operator auf Finns Diamant-Netz (H0_ij = (i/2) A (sigma.n_ij) e^{ik.d_ij}, 4x4) ist fuehrend ein isotroper masseloser Dirac.
  - Ein Term zweiter Ordnung, proportional zu i sigma.q mit q = (k_y k_z, k_z k_x, k_x k_y), spaltet die Zweige linear: a1 = +-0,354 laengs 110, null laengs 100 und 111 [E, vorab abgeleitet vom Agenten].
  - Als Licht verlangte das l < 0,2 l_P. Fuer Fermionen fehlt die Einordnung.
- **Luecken:**
  - L6: Haendigkeit bzw. Fermionen auf Finns Geometrie.
  - L5: Masse ohne Verlust; unitaere Dirac-Automaten sind im Projekt bekannt.
- Kennzeichen: [S] an der Quelle (Zeile/Abschnitt), [S Abstract], [L] Gedaechtnis, [M] Mathematik, [ES], [H].

## Ableitbarkeitsprobe und Projektsuche (vor der Karte)

- **Projektsuche** (Creutz, Borici, hyperdiamond, minimal doubling, Karsten/Wilczek, Fu/Kane/Mele):
  - Creutz kommt im Projekt nur als Einschluss 1980 vor (GLUONEN-L).
  - Minimal verdoppelte Fermionen auf dem Hyperdiamant und Diamant-Dirac-Modelle sind im Projekt nicht gelesen.
- **Schreibtisch der Leitung [M, ungeprueft]:**
  - Ist sigma ein axialer Vektor (T1) und q eine T2-Form, dann enthaelt T1 x T2 unter der Gruppe O keine Invariante. Der Term sigma.q ist dann verboten.
  - Unter T bzw. T_d ist er erlaubt.
  - Ein Operator, dessen Knoten die Drehungen um 90 Grad mitnimmt (beim Diamanten nur als 4_1-Schraube mit Untergittertausch), koennte die Spaltung also verbieten. Das ist zu pruefen, nicht gezeigt.
- **Literatur aus dem Gedaechtnis [L], zu pruefen:**
  - Creutz 2008 ("four-dimensional graphene", Hyperdiamant, minimal verdoppelte chirale Fermionen); Borici 2008.
  - Bedaque/Buchoff/Tiburzi/Walker-Loud 2008: minimal verdoppelte Fermionen brechen die hyperkubische Symmetrie und brauchen Gegenterme.
  - Fu/Kane/Mele 2007: Diamant-Gitter mit Dirac-Punkten an den drei X-Punkten.
  - Jacobson/Liberati/Mattingly 2003: Synchrotron-Schranke fuer Lorentz-Verletzung von Elektronen.

## Auftrag (feldforscher)

1. **Fermionen auf Diamant und Hyperdiamant:**
   - Welche Operatoren gibt es: Zahl der Dirac- bzw. Weyl-Punkte und ihre Lage, Symmetrien, Doppler?
   - Hat einer davon langwellig ein isotropes Tempo ohne Term zweiter Ordnung, der die Helizitaeten spaltet?
   - Welche Gegenterme bzw. Abstimmungen braucht er?
2. **Pruefung des Schreibtischs:** Verbietet die volle Punktgruppe (mit Schraubachse) den Term sigma.q? Gibt es dazu eine Quelle?
3. **Schranken fuer Elektronen:** Wie stark ist helizitaetsabhaengige Dispersion der Dimension 5 fuer Elektronen eingeschraenkt (Synchrotron des Krebsnebels u. a.)? Was folgte fuer l, wenn der W-D-Operator das Elektron waere (von Hand [M], mit Konvention der Quelle)?
4. **Gegensweep:** Gibt es Saetze, die so etwas auf Netzen mit Tetraedergeometrie allgemein ausschliessen (Nielsen-Ninomiya-artig fuer Isotropie, Read 2017 fuer Haendigkeit)?

## Erwartungen (vor jedem Abruf)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| DF1 | [H] Es gibt einen bekannten Spin-1/2-Operator auf dem 3D-Diamant (oder Hyperdiamant), dessen langwelliges Tempo isotrop ist und keine Helizitaetsspaltung zweiter Ordnung hat | 50 % |
| DF2 | [H] Jeder bekannte Diamant- bzw. Hyperdiamant-Fermionenoperator mit hoechstens minimaler Verdopplung bricht eine Gittersymmetrie und braucht mindestens einen abgestimmten Gegenterm | 65 % |
| DF3 | [H] Helizitaetsabhaengige Elektronen-Dispersion der Dimension 5 ist so stark eingeschraenkt, dass der W-D-Operator als Elektron l weit unter der Planck-Laenge verlangte | 85 % |

**Bedeutung (vorab):**
- **DF1 trifft ein:** Fuer Fermionen auf Finns Netz gibt es einen Bauweg ohne lineare Lorentz-Verletzung. Naechster Schritt waere eine Rechenkarte auf Finns Netz.
- **DF2 trifft ein:** Fermionen auf Finns Netz kosten wie das Tempo-Problem (L2) eine Abstimmung.
- **DF3 trifft ein:** Der naive Weyl-Operator auf Finns Netz ist auch als Elektron ausgeschlossen.

## Rahmen

- feldforscher, Zeitbox 60 min, hoechstens 8 gezielte Abrufe (arXiv-API oder arxiv.org per WebFetch), keine Websuche.
- Erwartung mit date-Zeit vor jedem Abruf in ARBEITSFELD.md.
- Schreiben nur in RUNDE-37/diamant-fermion-l/.
