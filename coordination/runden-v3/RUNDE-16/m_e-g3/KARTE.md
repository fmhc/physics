# M_E-G3: IR-endliche Schranke fuer die Graviton-Dreipunktkorrektur in D = 4? (Theoriekarte, an Codex)

- Leitung: claude-primary. Karte, Vorabklassen und Vorhersage geschrieben ab 2026-10-02 07:44:33 CEST (date), vor jeder
  Rechnung.
- Auftrag Finn, 02.10.: "mach weiter, gib die Theoriekarte an Codex". Ausfuehrender: Codex (OpenAI).
- Schwerpunkt: die zwei schwaechsten Glieder der Spin-2-Kette, Glied 7 (massive Fassung) und Glied 10, in D = 4.

## Herkunft

- RUNDE-13/spin2-d4/: SPIN2-D4.md, Codex-Fremdlesung, vier Lesungen der letzten Schicht. Der Nachtrag in
  coordination/art-grenzen-20260921/WARUM-SPIN-2.md vom 2026-10-01 21:56:56 sagt: In D = 4 gilt die Kopplung nur unter
  umstrittenen Kausalitaets-, IR- und UV-Annahmen.
- RUNDE-13/spin2-d4-2/: SPIN2-D4-2.md und die Codex-Fremdlesung codex-lesung/LESUNG.md (traegt mit Auflagen A1 bis A7).
  - Die M_E-Methode von Bellazzini u. a. (2512.13780v2) traegt externe Gravitonen; siehe Fernandez/Ruhdorfer/Serra
    (2603.15755v2), Anhang F, fuer g4.
  - Fuer g^3 fehlt die Kontrolle der subfuehrenden Unitaritaet. Eine log-verstaerkte Schranke ist weder hergeleitet noch
    ausgeschlossen (A1).
  - Die Normierungen von g3 bei Caron-Huot u. a. (2201.06602) und bei Fernandez u. a. sind verschieden (A2).

## Frage (Wortlaut nach der Codex-Fremdlesung, Abschnitt 5)

Lassen sich fuer die Vier-Graviton-MHV-Amplitude verschmierte M_E-B2/B3-Funktionale samt benoetigtem B4-Anteil
konstruieren, deren Unitaritaetsrest fuer eine ausdruecklich festgelegte Skalierung von |g3|^2 M^8 gleichmaessig
kontrolliert ist?

## Vorabklassen (bindend; neu mit einer Klasse fuer eine fehlende Herleitung)

- **A:** Eine Schranke an |g3|^2 (oder an x = |g3|^2 M^8) wird ohne neue physikalische Annahme hergeleitet. Der Rest ist
  fuer die festgelegte Skalierung gleichmaessig kontrolliert.
- **B:** Eine Schranke gibt es nur mit einer benannten Zusatzannahme, etwa einer meromorphen UV-Baumamplitude nach
  Bellazzini S. 13 oder einer anderen, die die Arbeit ausdruecklich nennt.
- **C:** Die Herleitung bleibt offen. Der fehlende Schritt ist genau benannt (z. B. eine Restabschaetzung der
  subfuehrenden Unitaritaet bei Skalierung x ~ log(M/E)), ohne dass er widerlegt ist.
- **D:** Im M_E-Rahmen ist g^3 nicht zu begrenzen, mit Begruendung (Gegenbeispiel oder Struktursatz).

## Vorhersage (Leitung, vor jeder Rechnung)

- A ~10 %, B ~35 %, C ~45 %, D ~10 %.
- Falls A oder B: Die Schranke hat die Form x <= c log(M/E) + O(1). c weicht um hoechstens einen Faktor 3 vom
  CHLPSD-Koeffizienten ab, umgerechnet auf dieselbe Normierung von g3 (Gl. (4.4): 24,9). ~50 %.

## Vorgaben

- Codex arbeitet nach eigenen Regeln: Plan, Nichtautor-Review, eingefrorene Rechnung, Root-Abnahme.
- Rechnungen auf der .69 nur nach dem bisherigen Muster (CPU11, nice19, ein Thread), kein neuer Dienst.
- Normierungswoerterbuch g3 (CHLPSD gegen FRS) zuerst und ausdruecklich (Auflage A2).
- Keine Literaturaussage "noch niemand gerechnet"; nur "in diesen Quellen nicht gerechnet".
- Ausgabe:
  - Bericht in coordination/runden-v3/RUNDE-16/m_e-g3/codex/ (oder einem Codex-Pfad mit Verweis hierher)
  - Ausgang nach den Vorabklassen A bis D
  - Kurzmeldung per Peerbus (kind result)
- Danach liest die Leitung einen frischen Anthropic-Leser (pruefer-opus) dagegen, bevor etwas in WARUM-SPIN-2.md
  eingeht.
- Grosse Budgets entscheidet Finn. Braucht die Karte mehr als kleine Laeufe, meldet Codex das vorher.

## Nachtrag (Leitung, 2026-10-02 22:01:07 CEST): Ausfuehrender gewechselt

- Finn, 02.10. ~22:05: "mach den spin2 dings".
- Stand: Codex hat die Karte seit 07:45 angenommen, aber nicht bearbeitet (CODEX-BLICK, R22). In seiner Antwort von 21:52
  bestaetigt er sie als offen, mit Vorrang fuer Finns Direktauftraege.
- **Ab jetzt rechnet ein Agent im Haus Anthropic** (Opus 5.5, ein Agent mit grossem Zeitbudget statt mehrerer kleiner).
  Arbeitsordner: coordination/runden-v3/RUNDE-23/m_e-g3/.
- Frage, Vorabklassen A bis D und Vorhersage der Leitung (A ~10 %, B ~35 %, C ~45 %, D ~10 %; Folgevorhersage zu c) bleiben
  **unveraendert**.
- Die Vorgaben gelten sinngemaess:
  - Normierungswoerterbuch g3 zuerst (A2)
  - keine Aussage "noch niemand gerechnet"
  - kleine Rechnungen nur auf der .69 ueber kleintest.sh
- Gegenlesung danach durch ein anderes Haus (Codex), bevor etwas in WARUM-SPIN-2.md eingeht. Codex ist per Peerbus
  informiert.
