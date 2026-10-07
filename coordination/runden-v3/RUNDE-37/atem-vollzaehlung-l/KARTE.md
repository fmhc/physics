# ATEM-VOLLZAEHLUNG-L: Wie viele Arten gibt es, Finns Netz mit starren Tetraedern gleichmaessig atmen zu lassen, und was sagt der echte Cristobalit dazu? (Runde 48, datennah, Folgekarte zu CONNOR-HALL-L und ISO-ATEM-1)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 08:59:31 CEST (date), vor jedem Abruf.
- **Herkunft:**
  - **CONNOR-HALL-L** (RUNDE-37/connor-hall-l/DOSSIER.md, N8) schlaegt vor, Formen nach dem Weg von Connor Hill vollstaendig abzuzaehlen statt zufaellig zu suchen.
  - **ISO-ATEM-1** (R42) [P]:
    - Die Zelle mit 8 Tetraedern atmet isotrop (F = lambda I) bei starren Tetraedern.
    - Die P2_13-Schar ist exakt und von Hand ableitbar.
    - Eine zweite Form (Punktgruppe 222, alle 8 Tetraeder kippen gleich) fand sich nur in 600 Zufallsstarts.
    - V/V0 ~ cos^2 phi_m.
- **Projektsuche (08:59, alle Dateitypen, Ausschluesse):**
  - EIS-1 (R34) [P]: Finns Netz ist das beta-Cristobalit-Geruest. Seine Nullmoden sind die starren Einheitsmoden (RUM) auf den Ebenen (xi, xi, zeta) (Hammonds u. a., [L?]).
  - SCHALTER-UND-ATMEN (R42) und die Negativliste R43: "Cristobalit schrumpft beim Erwaermen" ist unbelegt [L?] und darf nicht behauptet werden.
  - Eine Vollzaehlung oder Kipp-Varianten-Liste gibt es im Projekt nicht.
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Fragen (Literatur und Schreibtisch, keine Netzlaeufe)

1. Welche endlichen Kipp-Varianten des idealen beta-Cristobalits mit starren SiO4-Tetraedern kennt die Literatur? Zum Beispiel P2_13 (Wright/Leadbetter), I-42d, P4_12_12 (alpha) und weitere. Welche davon haben eine isotrope Verzerrung F = lambda I?
2. Ist die 222-Form aus ISO-ATEM-1 dort bekannt, und unter welchem Namen?
3. Gibt es eine vollstaendige Abzaehlung, etwa gruppentheoretisch wie Glazers Kippsysteme bei Perowskiten, oder ueber RUM-Zaehlung (Hammonds/Dove, CRUSH)? Was ist infinitesimal bekannt, was endlich?
4. **Daten:** Wie dehnt sich beta-Cristobalit beim Erwaermen tatsaechlich aus, mit gemessenem Koeffizienten? Wie stark ist die negative Waermeausdehnung verwandter Gerueste (z. B. ZrW2O8), die durch RUM erklaert wird? Damit wird der Negativlisten-Satz aus R43 geklaert.
5. **Bezug zu Finns Netz [H]:** Ist Finns "Atmen" (Raum schrumpft bzw. waechst ohne Verformung der Tetraeder) im echten Material als RUM-getriebene Waermeausdehnung sichtbar?

## Ableitbarkeitsprobe (Leitung, verkettet)

- **Vorab ableitbar [M, P]:**
  - die P2_13-Schar (Handformel ISO-ATEM-1)
  - V/V0 ~ cos^2 phi fuer starre Kippungen (Geometrie)
  - Starre Einheitsmoden bei infinitesimaler Amplitude liegen auf ganzen Ebenen, also gibt es unendlich viele infinitesimale Kippmuster (EIS-1, [L?]).
- **Nicht ableitbar:**
  - welche endlichen isotropen Varianten es gibt (Zaehlung)
  - ob die 222-Form bekannt ist
  - der gemessene Ausdehnungskoeffizient

## Vorhersagen (vor jedem Abruf)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| AV1 | [L?] Die P2_13-Schar aus ISO-ATEM-1 entspricht dem Cristobalit-Modell von Wright/Leadbetter (P2_13) | 70 % |
| AV2 | [L?] Die 222-Form ist in der Literatur als Kipp-Variante des Cristobalits bekannt (gleich welcher Name) | 45 % |
| AV3 | [H] Eine vollstaendige Abzaehlung der endlichen Kipp-Varianten mit starren Tetraedern gibt es in der Literatur nicht; bekannt sind nur einzelne Varianten und die infinitesimale RUM-Zaehlung | 55 % |
| AV4 | [L?] Beta-Cristobalit hat einen kleinen bzw. negativen Waermeausdehnungskoeffizienten, und die negative Waermeausdehnung verwandter Gerueste wird durch RUM erklaert | 60 % |

**Bedeutung (vorab):**
- **AV1 und AV4 treffen ein:** Finns "Atmen" ist im echten Material gemessen: Waerme regt Kippungen an und laesst das Geruest schrumpfen bzw. kaum wachsen. Das waere ein datennaher Anker fuer Finns Netzbild als Materialanalogie [H], kein Beleg fuer den Raum.
- **AV3 trifft ein:** Eine eigene Vollzaehlung, also Polynomsysteme je Untergruppe nach Hills Weg, waere neu. Dann folgt ein Kartenvorschlag mit Aufwand.

## Rahmen

- feldforscher, Zeitbox 60 min, hoechstens 15 Netzabrufe; WebSearch, arXiv, OpenAlex, freie Verlagsseiten.
- Schreibt nur in RUNDE-37/atem-vollzaehlung-l/.
- Literatur und Schreibtisch, keine Rechnung auf fremden Rechnern.
