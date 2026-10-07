# Runde 14 (v3): Q-Stern mit voller Rechnung, Fremdlesung M_E

Leitung: claude-primary. Angelegt: 2026-10-01 23:29:38 CEST (date). Explorativ, keine formale Bestaetigung. Runde 13 ist abgeschlossen
(RUNDE-13.md: Abschaetzung, Einfach gesagt; Journal claude-runde-v3-13-20261001, Index nr 550; Sicherung .69 -> TS440 r13 rc = 0).

## Rahmen

- Rechenorte: .69 ueber kleintest.sh (CPU-Spuren), jeder Aufruf hoechstens 10 min. Hoechstens drei Agenten.
- Die Websuche ist aufgebraucht; Literatur nur ueber arXiv-API, INSPIRE und direkte Abrufe.
- Offene Entscheidungen Finns: unveraendert (Ollama-Stopp, restic-Aufraeumen, APS-Zugang, Budget fuer grosse 3D-Laeufe).
- Codex: Paper v0.21 kanonisch (neuer Abschnitt "Direction of the exterior field"), DETUNING-1 abgeschlossen,
  ZWEIFELD-BIC in Arbeit.

## Karten

| Karte | Herkunft | Frage | wer |
|---|---|---|---|
| Q-STERN-2 | R13 Q-STERN | Wohin wandert die stille Stelle n = 1 unter schwacher Eigengravitation, in voller Rechnung erster Ordnung (mit delta Phi) und bei kleiner Kompaktheit? | Code-Agent |
| M_E-FREMDLESUNG | R13 SPIN2-D4-2 | Fremdlesung des Ergebnisses "nur mit neuer Annahme", bevor die fehlende Rechnung (Spin-2/3-Summenregeln in M_E-Form) auf die Liste kommt | Codex (angefragt) |
| Taegliche Pflichten 02.10. | Routine | Werkzeugtore, Index-Sicherung, Git-Tagesschnappschuss | Leitung, nach Mitternacht |

## Laufend (eingetragen 2026-10-01 23:30:48 CEST)

- **Q-STERN-2:** Code-Agent ab ~23:31. Karte RUNDE-14/q-stern2/KARTE.md, Vorhersage 23:29:53.
  - Vorhersagen: V1 (Cowling trifft die Steigung -4,5 alpha) ~75 %; V2 (voll: negativ, 0,3- bis 3-fache Verschiebung)
    ~65 %; V3 (gesehen bei beiden alpha) ~85 %.
- **M_E-FREMDLESUNG:** an Codex angefragt (Peerbus 74dce689).

### Taegliche Pflichten 02.10. (eingetragen 2026-10-02 00:09:25 CEST)

- Werkzeugtore: index-pruefen und karten-pruefen ohne Verstoss.
- index-sichern 00:01:13: 550 Zeilen, Kettenende 56c9f658...; rsync auf die .69 rc = 0; Zeile im Aussenanker
  KETTENENDE.log (22:01:24 UTC, nr 550).
- Git-Tagesschnappschuss f726adb "Snapshot research state of 1 Oct 2026 (evening, rounds 12 to 14)", gepusht
  (c90c7de..f726adb).
  - 2714 Dateien vorgemerkt, Groesse vorab nachgezaehlt (106,8 MB, gleiche Regel wie das Skript).
  - gitleaks: 48 Fehlalarme, sha256-Pruefsummen in Codex-Dateien von source-shaping-20261001. Per .gitleaksignore,
    Begruendung in GEHEIMNISPRUEFUNG.md. Kein --no-verify.
- Selbstanzeige: Der erste Skriptaufruf hatte die Argumente in falscher Reihenfolge, dadurch lief ein Commit-Versuch statt
  der Pruefung. Der Hook hat blockiert, der Index wurde zurueckgesetzt, und es entstand kein Commit.

### Q-STERN-2 (Code-Agent, 23:31 bis 00:17; RUNDE-14/q-stern2/ERGEBNIS.md; Karte 23:29:53, PLAN eingefroren 23:56:28, Laeufe danach bis 00:15; eingetragen 2026-10-02 00:19:11 CEST)

- **Ausgang nach der Regel: gesehen in allen vier Faellen** (alpha_1 und alpha_2, jeweils voll und Cowling).
  - Umlauf -1 auf beiden Stufen, Rechteck aufgeloest (0,37 bis 0,38 rad), Stufen auf 1,3e-8 gleich, K3 auf 2,5e-10.
  - Sonst kein s-Wechsel im Fenster.
- Kopplungen nach Kompaktheitsziel: alpha_1 = 0,00087 (2|Phi(0)| am Ort 0,0101), alpha_2 = 0,0027 (0,0305).
- Lagen omega^2 / rho:
  - voll: 0,79291 / 1,73953 (alpha_1) und 0,78364 / 1,72976 (alpha_2)
  - Cowling: 0,79280 / 1,73973 und 0,78331 / 1,73014
- **[ES] Verschiebung ~ -0,47 x Kompaktheit.** Die Rueckwirkung (delta Phi) macht sie in omega^2 nur ~2 % kleiner
  (voll : Cowling = 0,979 bzw. 0,977).
- Kontrollen:
  - K1, K2 und K3 bestanden; K4 reproduziert Q-STERN bitgleich.
  - K5 (Poisson-Rest < 1e-8) nur in einem von vier Faellen erfuellt, sonst 1,2e-8 bis 3,0e-8. Nach der Karte macht das
    nichts unauswertbar.
- Abweichung beim Auslesen, die Regel bleibt:
  - Mit psi ist das System nicht symmetrisch, der Wronski-Satz gilt nicht mehr.
  - W kommt aus einer exakten 3+2-Loesungsbedingung; bei alpha = 0 ist das das alte W (K1).
  - Pole in W der ersten Fassung sind vor dem Einfrieren behoben.
- Vorab gegen Ausgang (Leitung):
  - V2 (voll negativ, 0,3- bis 3-fach gegen Cowling) getroffen (0,98-fach).
  - V3 (gesehen bei beiden alpha) getroffen.
  - V1 haengt an der Lesart, beide stehen hier, keine wird nachtraeglich bevorzugt:
    - Nach dem Wortlaut ("diese Lagen", 0,7932 und 0,7842) getroffen: Cowling-Verschiebung das 1,09- bzw. 1,07-fache.
    - Nach der Steigungs-Lesart (-4,5 alpha bei den tatsaechlichen alpha) bei alpha_1 verfehlt (1,24-fach, erlaubt +-20 %),
      bei alpha_2 getroffen (1,18-fach).
- Selbstanzeigen des Agenten:
  - cp, diff und tr lokal benutzt (erlaubte Textwerkzeuge, aber nicht auf der Liste)
  - den K5-Massstab nicht vorab gegen die Rechengenauigkeit geprueft
  - die Lokalisierung hatte Vorrang statt eines eigenen Budgets
- **Bedeutung [H], Gesamtformel:**
  - Die bewiesene stille Stelle ueberlebt schwache Eigengravitation (Kompaktheit bis 0,03, Newton, erste Ordnung) und
    wandert berechenbar, um etwa -0,47 x Kompaktheit.
  - Die Rueckwirkung der Schwingung auf das Potential ist ein Effekt von etwa 2 %.
  - Fuer Laborbaelle ist das bedeutungslos. Fuer Bosonensterne verschiebt es die Lage messbar.

### M_E-FREMDLESUNG (Codex, 23:38 bis 23:40; RUNDE-13/spin2-d4-2/codex-lesung/LESUNG.md; eingetragen 2026-10-02 00:50:34 CEST)

- **Urteil: "TRAEGT MIT AUFLAGEN".**
  - Getragen:
    - Der Quellenfund zu externen Gravitonen, mit Fernandez/Ruhdorfer/Serra, Anhang F (F.7, F.10). Die alte Aussage "nur
      Pionen" ist damit verworfen.
    - Die Diagnose einer fehlenden g^3-Rechnung.
  - **Zu stark ist das Fazit "nur mit neuer Annahme".**
    - A1: Bei fester dimensionsloser Kopplung x = |g3|^2 M^8 sind die g^3-Beitraege O(GM^2) und liegen im Rest. Fuer x von
      der Groessenordnung log(M/E) kann G x aber so gross werden wie der verschmierte Pol. Eine log-verstaerkte Schranke
      (x <= c log(M/E) + O(1)) ist weder hergeleitet noch ausgeschlossen.
    - A3: Die Kontrolle der subfuehrenden Unitaritaet ist eine fehlende Herleitung, nicht notwendig eine neue
      physikalische Annahme. Die meromorphe UV-Baumstruktur ist ein belegter hinreichender Zusatzweg, kein notwendiger.
  - Weitere Auflagen:
    - A2: Die Normierungen von g3 bei Caron-Huot u. a. und Fernandez u. a. sind verschieden und nicht gleichzusetzen.
    - A4: Endliches G_E heisst nicht G_E << 1; die Rahmenkontrolle endet nicht allgemein dort.
    - A5: Die Regge-Aussagen bei Bellazzini haben zwei getrennte Beweiswege.
    - A6: Die Dimensionsfortsetzung bei Fernandez u. a. ist nicht "ohne Begruendung" (Fn. 18).
    - A7: Fernandez u. a. v2 ist vom 10.04.2026.
  - Literaturaussagen nur als "in diesen Quellen nicht gerechnet", nie "noch niemand gerechnet".
- **Entscheidung der Leitung:** Die Auflagen werden angenommen.
  - Der Ausgang von SPIN2-D4-2 heisst damit: M_E traegt externe Gravitonen. Fuer eine g^3-Schranke fehlt eine Herleitung
    (subfuehrende Unitaritaet), oder man nimmt einen Zusatzweg (meromorphe UV-Amplitude). Ob eine log-verstaerkte
    Schranke moeglich ist, ist offen.
  - Die Vorabklassen der Karte (nein / nur mit neuer Annahme / ja) hatten keine Klasse "fehlende Herleitung, offen".
    Meine Vorhersage "nur mit neuer Annahme ~55 %" gilt deshalb nicht als getroffen; der Ausgang ist differenziert.
  - Meine Chatmeldung an Finn war zu stark: "nur mit einer neuen Annahme" und "verschwindet genau in der Ungenauigkeit
    der Methode". Berichtigung in der naechsten Meldung.
- Folgekarte nach Codex (Abschnitt 5), als Theoriekarte M_E-G3:
  - Frage: Lassen sich fuer die Vier-Graviton-MHV-Amplitude verschmierte M_E-B2/B3-Funktionale samt B4-Anteil
    konstruieren, deren Unitaritaetsrest fuer eine festgelegte Skalierung von |g3|^2 M^8 gleichmaessig kontrolliert ist?
  - Geparkt bis zu einer Entscheidung, wer sie rechnet (Codex oder ein Theorie-Agent). Das ist schwere Theoriearbeit, kein
    kleiner Test.

## Abschaetzung (Leitung, 2026-10-02 00:51:00 CEST, date)

| Karte | Entscheidung | Grund |
|---|---|---|
| Q-STERN-2 | erledigt; Folge parken | Gesehen in allen vier Faellen. Verschiebung ~ -0,47 x Kompaktheit, die Rueckwirkung nur ~2 %. Weiter nur bei Bedarf: andere Stellen (n = 2, l = 1) oder staerkere Gravitation in voller Allgemeiner Relativitaet |
| M_E-FREMDLESUNG | erledigt; Theoriekarte M_E-G3 geparkt | SPIN2-D4-2 traegt mit Auflagen. Fuer g^3 fehlt eine Herleitung; eine log-verstaerkte Schranke ist offen. Die Theoriekarte ist schwer und braucht eine Entscheidung, wer sie rechnet |
| Taegliche Pflichten 02.10. | erledigt | Index, Karten, Sicherung, Aussenanker, Git f726adb gepusht |

- Vorab gegen Ausgang, Leitung:
  - Q-STERN-2: V2 und V3 getroffen; V1 je nach Lesart (Wortlaut getroffen, Steigung 1 von 2).
  - SPIN2-D4-2 (R13-Karte, Wertung nach der Fremdlesung): differenziert, nicht als getroffen gewertet.
- Lehren:
  - Mit Kopplung nach Kompaktheitsziel und Lokalisierung zuerst ist der Gravitationstest in einem Durchgang
    auswertbar.
  - Vorabklassen von Lesekarten brauchen eine Klasse "fehlende Herleitung / offen". Das war der zweite Fall nach SPIN2-D4.
- Selbstanzeigen:
  - Leitung: falsche Argumentreihenfolge beim Git-Skript (kein Commit entstanden); zu starke Chatmeldung zu SPIN2-D4-2.
  - Agent Q-STERN-2: cp, diff und tr lokal; K5-Massstab nicht vorab gegen die Rechengenauigkeit geprueft.

## Einfach gesagt (Rundenende)

Die stille Schwingung unseres Feldballs bleibt erhalten, wenn der Ball seine eigene schwache Schwerkraft spuert. Sie
verschiebt sich dabei nur ein wenig, und zwar ziemlich genau im Verhaeltnis zur Staerke der Schwerkraft. Bei der Frage zur
Spin-2-Kette hat Codex meine Aussage abgeschwaecht: Die neue Rechenmethode ist fuer unseren Fall noch nicht fertig
durchgerechnet. Ob sie mit oder ohne Zusatzannahme zum Ziel kommt, ist offen.

## Rundenabschluss (Leitung, 2026-10-02 00:51:06 CEST)

- Journal claude-runde-v3-14-20261002, Index nr 551, pruefen ohne Befund.
- Sicherung .69 -> TS440 gestartet (Log /home/fmh/sicherung-dot69-ts440-lauf-20261002-r14.log auf der .69).
