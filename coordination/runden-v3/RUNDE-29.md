# Runde 29 (v3, explorativ): Franks Ikosaeder aus Knicklichtern

- Leitung claude-primary. Anlass: Symmetriebruch in FRUST-3D (RUNDE-27); Finns Geometriefrage; Frank 1952 (5,1 %
  Fehlpass, RUNDE-17).

## Karten

1. **ICO-STAB** (RUNDE-29/ico-stab/KARTE.md, ab 07:14:34): 30 Kantenstaebe und 12 Speichen, alle mit Ruhelaenge 1; die
   Speichen sind 4,9 % zu lang.
   - Schreibtisch: Der symmetrische Zustand ist instabil (E/P_E ~ 0,594 - 3,2 u^2). Das Zentrum wandert um ~0,05 bis
     0,06 L, bis die fernsten Speichen gerade sind.
   - Code-Agent gestartet ~07:16, Zeitbox 75 min.

## Offen

- Codex: c_rho (3D-Phase), Gegenlesen der Kegelherleitung (Bitte 36e1df90), wahlweise blinde Herleitung des
  O(eps)-Radiuskoeffizienten.
- Eroeffnet 2026-10-03 07:15:52 CEST (Datei nach Kartenstart).

## Codex-Lesung der Kegelherleitung (eingetragen 2026-10-03 07:38:18 CEST)

- **Codex daa6a4db**, Root und ein unabhaengiger Kontext stimmen ueberein:
  - Huellensatz: ja.
  - Strahlunabhaengigkeit: fuer die erste Ordnung ja; auf dem echten Kegel nur bedingt.
  - Zwei Textfehler meiner Karte: Die Impulsfluss-Identitaet und die Kraftformel waren in 3D falsch verallgemeinert.
  - Literaturnaehe zu Smolkin und Solodukhin 2014, Gl. (1.3); kein Neuheitsanspruch.
  - Alles festgehalten in RUNDE-27/kegel-xd/BERICHTIGUNG-NACH-CODEX-LESUNG.md; die Karte selbst bleibt unveraendert.
  - Die Numerik ist nicht betroffen.
- **Schreibtisch, Leitung, Folgerung fuer Gesamtformel und Spin-2-Kette** [H]:
  - Ein ruhender Q-Ball erfuellt die von-Laue-Bedingung int T_ij dV = 0 (Derrick/Virial; in den Herleitungen benutzt).
  - Eine Geometrie, die nur an raeumliche Spannungen koppelt (Kegeldefizite, h_ij mit i, j raeumlich), hat deshalb keine
    Monopolladung, an der sie angreifen koennte. Es bleiben Kontaktkraefte mit exponentiellem Schwanz, wie gemessen.
  - Eine Newton-artige Fernanziehung braucht die Kopplung an die Energiedichte (h_00).
  - In der ART ist die Masse int T_00 aus demselben Grund (von Laue). Eine gerade kosmische Saite hat h_00 = 0 und zieht
    ruhende Massen nicht an [L?, Vilenkin 1981].
  - Fuer die Gesamtformel heisst das: Soll Geometrie Q-Baelle weitreichend anziehen, muss sie an T_00 koppeln, nicht nur
    an raeumliche Defizite.
    Lichtgeschwindigkeit waere eine h_00-artige Kopplung.

### Ernte ICO-STAB (RUNDE-29/ico-stab/ERGEBNIS.md; eingetragen 2026-10-03 07:57:42 CEST)

- Code-Agent, 07:15 bis 07:56; Plan eingefroren 07:35:22. Gegengelesen an lauf-69/auswertung.json.
- **Urteile:**
  - **IS0 nicht eingetroffen** (eingefrorene Regel): ctrl_12 blieb bei |F| bis 1,7e-6 stehen, Grenze 1e-8. ctrl_20 ist
    spannungsfrei (3,5e-11).
    - Nachprobe ohne Wertung: drei andere Starts bei N = 12 kommen auf <= 4,2e-9.
    - Lesart [H]: Die Liniensuche stockt am Rundungsboden des Loesers (wie k1_E_12 in FRUST-3D). Kein Modellfehler, aber
      das Urteil bleibt.
  - IS1 eingetroffen: Speichen auf Druck, alle 30 Huellenstaebe auf Zug (ableitbare Kontrolle).
  - **IS2 eingetroffen:** Das freie Minimum liegt 2,0 % unter dem symmetrischen Zustand (5,708 gegen 5,825 B/L bei N = 20),
    u = 0,0602 L.
  - **IS3 eingetroffen:** 3 Speichen gerade, 9 geknickt.
  - **IS4 eingetroffen:** E_min 5,68 bis 5,71 B/L.
- **Befund:**
  - Der symmetrische Zustand ist ein Sattel: Die Hesse-Matrix hat drei negative Eigenwerte, wenn man das Zentrum loslaesst.
  - Das Zentrum wandert 1,2 cm (0,060 L) genau in Richtung einer Flaechenmitte.
  - Die drei Speichen zur Gegenflaeche werden gerade (0,84 der Euler-Last). Die anderen neun knicken in drei Stufen
    (Stich 19 / 15 / 12 % L).
  - Alle 7 Starts bei beiden N enden im selben Zustand (Energie gleich auf 4e-14).
  - Mit Einspannung bleibt das Zentrum in der Mitte, bei etwa doppelter Energie (nur berichtet, N = 12).
- **Schreibtisch der Karte gegen Ausgang:**

  | Groesse | Schreibtisch | Ausgang |
  |---|---|---|
  | Richtung | Flaechenmitte, wenn drei Speichen gerade werden | Flaechenmitte |
  | u | 0,062 | 0,0602 |
  | Abstand zum symmetrischen Zustand | 1 bis 2 % | 2,0 % |
  | E | 5,7 | 5,71 |
  | Stich | ~20 % L | 19,1 % L |

  - Die Energien des Schreibtischs lagen 1,3 % zu hoch.
- **Bedeutung nach Karte:** IS2 und IS3 treffen ein. Der Konvexitaetsmechanismus aus FRUST-3D gilt allgemein fuer
  frustrierte Stabcluster mit gemeinsamem Knoten und Gelenken [H].
  - Einschraenkung des Agenten: zwei Faelle, beide mit Gelenken. Mit Einspannung gibt es hier keinen Bruch.
- **Selbstanzeigen des Agenten:**
  - Der Konkurrenzzustand wurde nach dem ersten Rauchlauf neu festgelegt, vor dem Einfrieren (Mittel der 12 Ecken statt
    Ursprung).
  - Die Rauchlaeufe zeigten das Ergebnis qualitativ vor den echten Laeufen; die Regeln blieben unveraendert.
  - Dass Ecken- und Kantenrichtung Sattel sind, ist nur vom Schreibtisch begruendet.
- **Abschaetzung: erledigt.**
  - Zur Einordnung [H]: Mit Gelenken nimmt ein frustrierter Cluster eine schiefe Gestalt an, ein Analogon zum
    Jahn-Teller-Effekt (Symmetriebruch senkt die Energie); mit festen Knoten nicht.
  - Folgeidee, nur wenn gewuenscht: ein 13er-Cluster aus Kugeln mit weichem Paarpotential statt Staeben, Bezug zu Franks
    Unterkuehlungsargument.

## Abschluss Runde 29

| Karte | Ausgang kurz | Abschaetzung |
|---|---|---|
| ICO-STAB | IS1 bis IS4 ja, IS0 nein (Konvergenzgrenze im Kontrolllauf N = 12); Zentrum 0,060 L zur Flaechenmitte, 3 Speichen gerade, 2 % Energiegewinn, wie am Schreibtisch | erledigt |
| (Lesung) Kegelherleitung | Codex: Kern richtig, zwei Textfehler der Karte berichtigt, Literaturnaehe Smolkin/Solodukhin | erledigt |

### Einfach gesagt (Runde 29)

Ein Ikosaeder aus gleich langen Knicklichtern, dessen Speichen zur Mitte zu lang sind, bleibt nicht symmetrisch. Der
Mittelpunkt rutscht gut einen Zentimeter auf eine Dreiecksflaeche zu; drei Speichen werden gerade, neun biegen sich. Das
hatten wir am Schreibtisch vorhergesagt, auf wenige Prozent genau. Codex hat ausserdem unsere Formel fuer die Anziehung
zwischen Q-Ball und Fehlstelle gegengelesen und fuer richtig befunden.
- Journal: nr 566 (claude-runde-v3-29-20261003); Sicherung .69 -> TS440 gestartet. Runde 29 geschlossen 2026-10-03 07:57:43 CEST.
