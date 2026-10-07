# TAKT-DYNAMIK-1: Laufen Schwerewellen durch ein Netz, das unterwegs nach Delaunay umklappt, ohne Energie zu verlieren oder zu streuen? (Runde 47, Fast Lane nach TAKT-UMKLAPP-1)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 08:18:29 CEST (date), vor jeder Rechnung.
- **Finn (05.10.):** "Zellen umklappen - wie und mit welchem Mechanismus? Try it." und "Mach takt umklapp jetzt".
- **Herkunft:** TAKT-UMKLAPP-1 (RUNDE-37/takt-umklapp-1/ERGEBNIS.md) [P]:
  - Finns Takt ist P = 8 d0^T *1 d0, umkreisbasiert (HT0).
  - Zufaellige Zuege machen P indefinit, und genau dort wachsen Stoerungen (HT2, HT3).
  - Delaunay-gesteuerte Zuege nach kleinen Eckverschiebungen hielten 26 von 26 Netzen stabil (TU1).
  - **Offen ist die Dynamik:** Bleibt das Netz stabil und energieerhaltend, wenn es waehrend einer laufenden Welle umklappt?
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Rechnung (Code-Agent)

- **Netze:**
  - Delaunay-Glas N = 128 (TT-GLAS-1, Saaten 1 bis 4)
  - V_D (TAKT-UMKLAPP-1)
- **Wellen:**
  - eine laufende TT-Welle bzw. stehende TT-Mode mit Dehnungsamplitude A = 1e-3 und 1e-2
  - je 10 Perioden, symplektischer Integrator, fester Zeitschritt, Konvergenz in dt geprueft
- **Drei Arme:**
  - (a) ohne Umklappen, feste Zerlegung
  - (b) Delaunay-gesteuert:
    - Verletzt eine innere Flaeche im aktuellen (gedehnten) Netz die Delaunay-Bedingung, wird sie flach umgeklappt (2-3 bzw. 3-2).
    - Den Zeitpunkt bestimmt eine Ereignissuche (Bisektion in t).
    - Laenge und Rate einer neuen Kante folgen aus der Geometrie der beteiligten Tetraeder (Cayley-Menger).
  - (c) gleich viele Zufallszuege zu denselben Zeiten
- **Messen:**
  - Energiedrift je Arm
  - Zahl der Zuege je Periode
  - Sprung von P an jedem Zug
  - TT-Amplitude und Phase nach 10 Perioden gegen Arm (a)
  - Anteil in anderen Moden (Streuung)
  - wachsende Moden
- **Die Abbildung des Zustands ueber einen Zug** (Kanten, Raten, Zwangsflaeche) legt der Agent vor der Rechnung im Plan fest, mit einer Schreibtischpruefung an einem einzelnen Zug.

## Ableitbarkeitsprobe (Leitung, vor der Karte; Gegenmittel aus TU1 und KAC: Bausteine verketten)

- **Vorab ableitbar [M]:**
  - **Stetigkeit am Zug:** An einem Delaunay-Uebergang liegen fuenf Ecken auf einer Kugel. Dort ist das umkreisbasierte duale Mass der neuen bzw. wegfallenden Kante bzw. Flaeche null, also ist P am Zug stetig (TD0).
  - **Keine Restspur:** Kehrt die Dehnung zum Ausgangszustand zurueck, also nach vollen Perioden einer Mode, ist die Delaunay-Zerlegung fuer allgemeine Lagen eindeutig. Das Netz kehrt dann zur Ausgangszerlegung zurueck (TD4).
  - **Zahl der Zuege:** Nach UMKLAPP-1 (UK1) verletzt eine Dehnung a etwa 1,2 a der Flaechen. Je Periode kreuzt jede betroffene Flaeche die Schwelle zweimal [P, M]. Die Zahl der Zuege ist also grob vorhersagbar und kein Befund.
  - **Zufallsarm:** Instabilitaet nach Zufallszuegen folgt aus HT2 und HT3 [P].
- **Nicht ableitbar:**
  - die Energiedrift im Arm (b): Am Zug springt die Ableitung von P, und der Integrator verliert dort seine Fehlerschranke;
  - die Streuung der Welle durch die Zuege: Wirkung zweiter Ordnung in A, Groesse offen;
  - der Betrag des Energiesprungs im Arm (c).

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| TD0 | Kontrolle, vorab ableitbar: An jedem Delaunay-Zug ist das duale Mass der neuen bzw. wegfallenden Kante bzw. Flaeche < 1e-10 (relativ), P springt um < 1e-10 (relativ) | 85 % |
| TD1 | [H] Ueber 10 Perioden bei A = 1e-3 bleibt die Energiedrift im Arm (b) unter dem Doppelten der Drift im Arm (a) (gleicher Integrator, gleiches dt) | 55 % |
| TD2 | [H] Im Arm (c) ist die Energiedrift mindestens 10-mal so gross wie im Arm (a), und es treten wachsende Moden auf (der Teil "wachsende Moden" ist aus HT2 und HT3 erwartbar) | 75 % |
| TD3 | [H] Die Streuung durch die Zuege im Arm (b) (TT-Amplitudenverlust gegen Arm (a) nach 10 Perioden) bleibt bei A = 1e-3 unter 1e-3 relativ und waechst von A = 1e-3 zu 1e-2 mindestens wie A^1,5 | 45 % |
| TD4 | Kontrolle, vorab ableitbar: Nach vollen Perioden einer Mode stimmt die Zerlegung zu mindestens 99 % der Flaechen mit der Ausgangszerlegung ueberein; Abweichungen nur an Fast-Gleichstaenden | 85 % |

**Bedeutung (vorab):**
- **TD1 und TD3 treffen ein:** Umklappen als Taktschritt ist dynamisch vertraeglich. Wellen laufen durch ein umklappendes Netz ohne Energieproblem und fast ohne Streuung. Damit ist Finns "Zellen umklappen" als laufender Vorgang moeglich [H].
- **TD1 verfehlt:** Die Zuege brauchen eine bessere Zeitbehandlung (exakte Zugzeiten), oder sie tragen Energie. Das waere ein Hinweis auf einen versteckten Freiheitsgrad.
- **TD3 verfehlt, also starke Streuung:** Die Zuege daempfen bzw. zerstreuen Wellen. Das waere eine moegliche messbare Signatur (Daempfung oder Dispersion von Schwerewellen) und waere gegen Daten zu pruefen [H].

## Rahmen

- Code-Agent, Code aus takt-umklapp-1/code, umklapp-1/code und tt-glas-1/code kopieren, dort nichts aendern.
- Gewichte: umkreisbasiert, also der Takt aus HT0; P1 nicht verwenden.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu8, cpu9 und cpu10. Je Lauf hoechstens 10 min, ein Thread. Zeitbox 150 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256). Ein ehrlicher Teilbericht ist besser als keiner: zuerst A = 1e-3, Arme (a) und (b).
- Synthetisch, keine Messdatenbestaetigung.
