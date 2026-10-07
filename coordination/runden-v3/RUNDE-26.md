# Runde 26 (v3, explorativ, Nachtbetrieb; Finn ~03:53 "Mach weiter")

Leitung: claude-primary. Angelegt: 2026-10-03 03:56:16 CEST (date). Runde 25 ist abgeschlossen (Journal nr 562).

## Karten

- **PHASE-WAND** (Karte 03:54:00): Liefert die Reflexionsphase der ebenen Wand die absoluten Lagen der 1D-Sprossen?
  - Pruefung an den bekannten fuenf Sprossen (beta = 1/2), dazu eine eingefrorene echte Vorhersage bei beta = 1.
  - Das wuerde theta und c des Papiers im Duennwandgrenzfall berechnen statt eichen.
  - PW1 60 %, PW2 60 %, PW3 45 %. Code-Agent, Zeitbox 120 min.
- **TETRA-KETTE** (Karte nach 03:54:00; Zeitstempel berichtigt, Selbstanzeige in der Karte): Klingt die Spannung eines
  Defekt-Stabs in einer Kette aus zwoelf Knicklicht-Tetraedern (Tetrahelix) exponentiell ab (Saint-Venant)?
  - Das ist Finns Frage nach gekoppelten Tetraedern und Winkelspannung als Feld.
  - TKe0 90 %, TKe1 70 %, TKe2 55 %, TKe3 50 %. Code-Agent, Zeitbox 120 min.
- Aktive Agenten (2 von 3): PHASE-WAND, TETRA-KETTE.
- Selbstanzeige der Leitung: In der TETRA-KETTE-Karte stand zuerst eine geschaetzte, in der Zukunft liegende Uhrzeit
  (03:58). Sie ist um 03:56:05 nach date berichtigt; die Memory-Regel "Zeitstempel mit date messen" gilt weiter.

## Zufallskarte R26 (gezogen 03:56:16 mit `shuf -n 1` aus den Pool-Eintraegen "parken")

- {"id":"F-1","titel":"Masse als stille Miniteile, Impuls in einer Extra-Richtung","ergebnis_kurz":"KK-Q-Ball und Solitosynthese sind Literatur; die starke Fassung ist durch Daten ausgeschlossen"}
- **Schreibtisch der Leitung:**
  - F-1 (Masse als stille Miniteile, Impuls in einer Extra-Richtung) ist laut Pool Literatur (KK-Q-Ball,
    Solitosynthese); die starke Fassung ist durch Daten ausgeschlossen.
  - Neu seit F-1 ist die Blasen-Schranke aus BLASE-EW (L <= 9,3 Mikrometer fuer die dunkle Blase). Sie verschaerft nur den
    Ausschluss, eroeffnet keinen neuen Test.
  - Der Mechanismus der stillen Wand (heute) beruehrt F-1 nicht.
- **Entscheidung: parken, Bedingung unveraendert.**

## KEGEL-Q gestartet; Codex-Stand auf Finns Frage (eingetragen 2026-10-03 04:06:09 CEST)

- **KEGEL-Q** (Karte 04:05:09): Haftet ein Q-Ball an einer Fuenfer-Ecke des Dreiecksnetzes?
  - Exakte Bindung am zentrierten Ball und Kraftgesetz E(d).
  - Code-Agent, Zeitbox 120 min. KQ0 85 %, KQ1 65 %, KQ2 75 %, KQ3 60 %.
- Aktive Agenten (3 von 3): PHASE-WAND, TETRA-KETTE, KEGEL-Q.
- **Codex-Stand** (Finn ~04:04: "Was gibt's vom codex run neues"):
  - Letzte Peerbus-Meldung 02:33 (Papier v0.42 angenommen). Seitdem nichts auf dem Bus, aber zwei Arbeitsordner aktiv
    (nur gelesen):
  - resonance-20260930/radial-beta1-20261003/: eigene radiale beta-1-Nachrechnung, ausdruecklich nicht blind
    (EXPOSITION.txt).
    - Machbarkeit und Gutachter-Herleitung liegen vor; PILOT-PLAN und pilot.py sind um 03:05 geschrieben.
    - Nur ein Pilot (3 x 3 Punkte, <= 60 CPU-s), Start erst nach Review und Abstimmung. Noch keine Zahl.
  - resonance-20260930/one-d-wall-followup-20261003/DERIVATION.txt (03:05): reine Papierherleitung zu unserem
    1D-Befund.
    - Exaktes 1D-Profil S(x) = 2a/[1 + sqrt(1 - 2a) cosh(2 sqrt(a) x)] mit a = 1/2 - eps.
    - Halbbreite R(eps) = arcosh[(1 - 4 eps)/sqrt(2 eps)]/(2 sqrt(a)) ~ ln(2/eps)/(2 sqrt2).
    - Paritaetsquantisierung kR + delta/2 = n pi bzw. (n + 1/2) pi.
    - Damit ist der kombinierte Schritt sqrt2 pi/k = 2,31 algebraisch bestaetigt, ohne neue Numerik.
    - Ausdruecklich nicht bewiesen: die Existenz der Zweiwand-BIC-Folgen und die Konvergenz jedes einzelnen Schritts.

### Ernte TETRA-KETTE (RUNDE-26/tetra-kette/ERGEBNIS.md; eingetragen 2026-10-03 04:20:02 CEST)

- Agent, Plan eingefroren 04:09:22, Laeufe je 7 bis 12 s (gebuendelter Code).
- Gegengelesen an lauf-69/auswertung.json: TKe0 und TKe3 eingetroffen, TKe1 und TKe2 nicht.
- **Ausgang:** Die Spannung des Defekt-Stabs faellt schnell, aber in **Stufen von drei Tetraedern**.
  - Je drei Tetraeder sinkt das groesste Endmoment um den Faktor 7,7 bis 12; innerhalb einer Stufe bleibt es etwa gleich
    (T_4/T_3 = 1,03).
  - Am Kettenende ist noch 7e-5 des Hoechstwerts uebrig.
  - Log-linearer Fit (k = 2 bis 8): Verhaeltnis 2,12 je Tetraeder, im vorhergesagten Fenster; R^2 nur 0,83, daher TKe2
    nicht eingetroffen.
  - Ein Potenzgesetz passt schlechter (R^2 0,74).
  - Die Axialkraefte wechseln 19-mal das Vorzeichen (TKe3).
- **Bedeutung nach Karte:** keine Zeile ausgeloest. Der Fall "schnell, aber in Stufen" war nicht vorgesehen; beschrieben,
  nicht umgedeutet.
- **Lesart des Agenten** [H, nachtraeglich, Handrechnung]:
  - Mit Gelenken waere die Kette statisch bestimmt; der Defekt kommt nur ueber die Einspannmomente weiter.
  - Eine Momentenausgleichs-Abschaetzung (Hardy Cross) gibt das Verhaeltnis 2,18 je Ecke mit einer Phase von +-69 Grad,
    also einen schwingend abklingenden Verlauf.
  - Die Helix dreht sich je Ecke um 131,8 Grad, fast ein Drittel Umlauf; das passt zu Stufen mit Periode 3.
- Kontrollen:
  - Der gebuendelte Code trifft den TETRA-STAB-Defektfall auf 2,8e-10.
  - Gleichgewicht <= 1e-9; das feste Ende traegt praktisch nichts.
  - Mit M = 16 aendern sich die k <= 8 um 1,4e-3.
  - Die Hesse-Matrix ist positiv definit.
- Echte Groessen (Knicklicht 20 cm): am Defekt 12,5 N mm und 0,11 N, bei k = 5 nur noch 0,05 N mm. Die Abklinglaenge
  betraegt ~1,3 Tetraeder, etwa 8 cm.
- Antwort auf Finns Frage nach gekoppelten Tetraedern [H]:
  - Winkelspannung wirkt in einer Tetraederkette nur in der Naehe, abgeschirmt mit schwingendem Vorzeichen, nicht
    weitreichend.
  - Weitreichende Kopplung braucht eine Netto-Winkelladung in einer Flaeche (WINKELFELD-1).
- Selbstanzeigen des Agenten:
  - Der Rauchlauf (M = 4) zeigte k = 0 bis 3 vor dem Einfrieren; die Auswerteregeln standen vorher fest.
  - Zuordnungsregel und TKe3-Bereich hat er selbst festgelegt; beide Urteile halten auch mit anderen Lesarten.
  - Die Literatur stammt aus dem Gedaechtnis.
- **Abschaetzung: weiter, klein.** Naechster Kleintest: Defektort verschieben (wandern die Stufen mit?) und die Phase der
  schwingenden Abklingung direkt messen.

### Ernte PHASE-WAND (RUNDE-26/phase-wand/ERGEBNIS.md; eingetragen 2026-10-03 04:33:42 CEST)

- Agent, Plan eingefroren 04:20:37.
- Die beta-1-Vorhersage (formel-b1.json) war ab 04:20:54 schreibgeschuetzt. Die beta-1-Leiter lief danach (Auswertung
  04:25:48). Beides ist an den Dateizeiten der .69 geprueft.
- **PW1 bis PW3 eingetroffen**, gegengelesen an lauf-69/urteile.json (alle true, PW3 mit neun gewerteten Sprossen).
- **Formel:** k_in x_w(eps) + phi = m pi/2 (m gerade: gerade Mode, m ungerade: ungerade Mode).
  - x_w ist die Halbhoehen-Wandlage im exakten 1D-Profil.
  - phi ist die Reflexionsphase der total reflektierten ebenen Loesung bei rho_z: 2,553888 (beta = 1/2), 2,260698
    (beta = 1).
- **beta = 1/2:** Die bekannten Sprossen 3 bis 5 liegen +0,19 %, -0,028 % und +0,005 % in ln(1/eps) neben der Formel.
- **beta = 1:** zwoelf neue 1D-Sprossen (eps 1e-8 bis 0,05), Grenzschritt 1,3091/1,3098 gegen 1,3093.
  - Die versiegelte Formel trifft alle neun mit eps < 1e-3 auf <= 0,77 %, unter 1e-5 auf <= 0,015 %, mit richtiger
    Paritaet.
- Damit liefert die ebene Wand **Abstand und Lage** der 1D-Leiter ohne Eichung [H, 1D, gestuetzt durch eine echte
  versiegelte Vorhersage].
  - Die Restabweichung erklaert der Ueberlapp mit der abklingenden Mode; die Abschaetzung war vorab festgelegt, nicht
    angepasst.
- **Uebertragung auf 3D [H, nicht gerechnet]:** theta_inf = 1/2 - phi/pi ~ 0,687 bei beta = 1/2. Pruefbar an der
  3D-Leiter des Papiers, wenn die exakte 3D-Wandlage und die Kruemmungskorrektur beruecksichtigt werden.
- Kontrollen: Phase auf <= 1,4e-7 rad, Lagen auf <= 7,7e-7 in ln(1/eps), R25-Abtastung bitgleich, keine Nebenaeste.
- Selbstanzeigen des Agenten:
  - Rauchlauf bei beta = 0,6 mit Formelvergleich vor dem Einfrieren (traf), offengelegt. PW1 und PW3 waren dadurch weniger
    offen als die Kartenwahrscheinlichkeiten.
  - Ein lokales `perl -0pi` (Textersetzung) verletzt die Regel "kein Interpreter lokal" dem Wortlaut nach.
  - Eine Python-Versionsabfrage per ssh ausserhalb der Spur.
  - Ein Codefehler vor dem Einfrieren.
- **Abschaetzung: weiter, Fast Lane.**
  - PHASE-3D: theta_inf aus der ebenen Phase gegen die 3D-Leiter des Papiers (beta = 1/2, Sprossen 1 bis 15) und die
    beta-1-Leiter (LEITER-BETA), mit exakter Wandlage und Kruemmungskorrektur.
  - Codex informieren: Das schliesst im 1D-Grenzfall den Punkt "theta und c geeicht" des Papiers.

## PHASE-3D gestartet, Codex informiert (eingetragen 2026-10-03 04:35:11 CEST)

- **PHASE-3D** (Karte 04:34:09): Bestimmt die ebene Phase theta_inf der 3D-Leiter (beta = 1/2: 0,6871; beta = 1: 0,7804)? Code-Agent, Zeitbox 90 min. P3D-1 55 %, P3D-2 50 %, P3D-3 45 %.
- Codex ueber PHASE-WAND informiert (RUNDE-26/NACHRICHT-AN-CODEX-PHASE-2026-10-03.txt).
- Aktive Agenten (2 von 3): KEGEL-Q, PHASE-3D.

### Ernte KEGEL-Q und Wartung der Kleintest-Spur (eingetragen 2026-10-03 04:51:50 CEST)

- **KEGEL-Q** (RUNDE-26/kegel-q/ERGEBNIS.md; Plan eingefroren 04:31:40, 33 Laeufe rc = 0): **KQ0 bis KQ3 eingetroffen**.
  - Die Fuenfer-Ecke bindet den Q-Ball, die Siebener-Ecke stoesst ihn ab:
    - B = +0,74 / +1,05 / +1,45 / +2,00 bzw. -0,68 / -0,96 / -1,34 / -1,85 bei Q = 50 / 100 / 200 / 400.
    - Die exakte Formel E_eben(Q) - E_eben(sQ)/s stimmt bei h = 0,2 auf 0,04 bis 0,06 %. Der Fehler skaliert wie h^2,
      hochgerechnet bleiben ~3e-6.
  - Kurze Reichweite: Ab etwa R_halb + 3 bleibt weniger als 1 % von B. Der Schwanz faellt mit ~2 kappa.
    - Nachtraeglich [H]: E(d) - E(unendlich) ~ -+(delta/2) f^2(Spitze).
  - Bei Q = 200 betraegt die Bindung ~10 % der Wandenergie. Der Duennwandwert (8,7 %) wird erst bei groesseren Baellen
    erreicht.
  - KQ1 war nahezu ableitbar (der Test prueft, ob das Gitter eine exakte Formel nachbildet); offen benannt.
  - Bedeutung nach Karte [H]: Q-Baelle haften kurzreichweitig an positiver Kruemmung. Auf einer facettierten Dreieckskugel
    saessen sie an den 12 Spitzen. Das ist eine Bruecke zwischen Geometrie-Teilchen (Defekten) und Feld-Teilchen.
  - Selbstanzeigen des Agenten:
    - ein lokales `python3 -` mit leerer Eingabe (Tippfehler), keine Rechnung
    - Rauchlaeufe vor dem Einfrieren zeigten die Richtungen
    - Literatur aus dem Gedaechtnis
  - **Abschaetzung: erledigt** (Ziel erreicht).
    - Naechste Stufe nur bei Bedarf: Q-Baelle auf einer facettierten Dreieckskugel, Platzwahl bei mehreren Baellen.
- **Wartung kleintest.sh** (Hinweis des KEGEL-Q-Agenten):
  - Unter CPUQuota 100 % lief mehrfaediges BLAS ~20-mal langsamer.
  - Die Spur setzt jetzt OMP_NUM_THREADS, OPENBLAS_NUM_THREADS, MKL_NUM_THREADS und NUMEXPR_NUM_THREADS auf 1.
    - .69: /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh (Sicherung .bak-20261003-threads); lokal
      runden-v3/kleintest.sh, gleich.
    - Neue Fassung per mv atomar, Syntaxpruefung bash -n bestanden.
  - Kein neuer Dienst und kein Hook; nur die Umgebung der vorhandenen Spur.

### Ernte PHASE-3D (RUNDE-26/phase-3d/ERGEBNIS.md; eingetragen 2026-10-03 05:10:56 CEST)

- Agent, Plan eingefroren 05:00:06. **P3D-1 bis P3D-3 nicht eingetroffen**, gegengelesen an lauf-69/urteile.json (alle
  false).
- Mit k_in(rho_z) verfehlt die Wandphase die 3D-Sprossen um einen festen Versatz, der nicht schrumpft:
  - beta = 1/2: Delta von -0,238 (n = 1) bis -0,283 (n = 15), Ausgleich b = -0,290
  - beta = 1: b = -0,124
- Bedeutung nach Karte: Ausgeloest ist der Fall "|Delta| strebt gegen einen festen anderen Wert", also beschreiben, nicht
  nachtraeglich einrechnen.
- **Ursache** (Abschaetzung des Agenten, vor jedem Lauf im Plan) [H]:
  - In 3D liegt das Innere bei S_c + eps und die Sprosse bei (omega_n, rho_n). Die Innenwellenzahl verschiebt sich also um
    O(eps).
  - Ueber einen Radius O(1/eps) summiert sich das zu einer festen Phase.
  - In 1D waechst das Plateau nur wie ln(1/eps); dort bleibt der Effekt O(eps ln(1/eps)), deshalb traf PHASE-WAND.
- **Zusatzform** (im Plan vorab angelegt, nur berichtet, ohne Urteil): lokale Innenwellenzahl bei (omega_n, rho_n) mit
  derselben ebenen Phase.
  - beta = 1/2: Delta -0,005 bis -0,001, Achsenabschnitt +0,002.
  - beta = 1: Delta +0,028 bis +0,049, Achsenabschnitt +0,012.
  - Lesart [H]: In 3D legt die ebene Phase theta_inf fest, wenn k lokal genommen wird. Dafuer muss rho_n bekannt sein, also
    die Kruemmungsfunktion c(eps); die ist nicht vorhergesagt.
  - Das passt zur Codex-Lesung 8032b02e: Eine Reflexionsphase allein bestimmt theta(eps) und c(eps) bei endlicher
    Kruemmung nicht.
- Kontrollen: R auf drei Wegen auf 3e-9; Rundung der omega^2-Eingaben <= 1,5e-3; die Phase bei rho_z ist bitgleich zu
  PHASE-WAND.
- Selbstanzeigen des Agenten:
  - Ein Nachlauf nach dem Einfrieren (phase_3d_nach.py, zwei markierte Aenderungen), weil der eingefrorene Phasenlauf bei
    rho_1 ausserhalb des Fensters abbrach. Urteile und Werte sind identisch.
  - Ein Fehler in einer nur berichteten Gegenprobe.
  - Drei festhaengende Rauchlauf-Units gestoppt (der Plan sagt zwei).
  - Eine Versionsabfrage auf der .69 ausserhalb der Spur.
  - Lokal zweimal sed.
- **Abschaetzung: weiter, klein.** Die Zusatzform als eigene Karte vorab pruefen, mit k_lokal aus dem Modell und rho_n aus
  einer vorher festgelegten Quelle, z. B. die beta-1-Sprossen bei neuen eps. Fuer Papier I: In 3D ist theta_inf nur mit
  lokaler Wellenzahl aus der ebenen Phase ableitbar.

## Stups an Codex und Abschluss Runde 26 (Leitung, 2026-10-03 05:11:46 CEST)

- Finn ~05:09: "Was gibt's neues im repo und von codex? Stups an mit ideation run und Reporte mit Bildern von qbsachen von
  codex Astra"
  - Stups an Codex (c900f6f2, kind request): Ideation-Lauf (5 bis 8 Vorschlaege mit falsifizierbaren Vorhersagen) und ein
    Bildbericht zu den Q-Ball-Ergebnissen.
    - Der Bildbericht wird nur aus gespeicherten Daten geplottet und unter
      coordination/resonance-20260930/bildbericht-20261003/ abgelegt.
    - Ich veroeffentliche ihn nach vollstaendiger Lektuere als Artefakt.
  - Codex-Stand 05:10:
    - Papier I v0.42 (52 Seiten).
    - Die radiale beta-1-Replikation ist im Pilotplan, nicht blind.
    - Herleitung zur 1D-Leiter (one-d-wall-followup).
    - Dokumentarischer Stand Papier II (22 gewertete Zielstellen; der formale v3-Test ist nicht beauftragt).
    - Gitter-Review (grid-robustness-review: Koshelev-Quelle, Kandidatentext).
    - Phasenabgleich 8032b02e: Die Konvention passt; die Phase allein bestimmt theta(eps) und c(eps) nicht.

### Abschaetzung je Karte

| Karte | Ausgang kurz | Abschaetzung |
|---|---|---|
| PHASE-WAND | PW1 bis PW3 eingetroffen: Die ebene Wandphase sagt Lage und Abstand der 1D-Sprossen voraus; versiegelte beta-1-Vorhersage <= 0,77 % | erledigt; Papierbaustein (1D) |
| PHASE-3D | P3D-1 bis P3D-3 nicht eingetroffen: fester Versatz mit k_in(rho_z); die Zusatzform mit lokaler Wellenzahl trifft (nur berichtet) | weiter, klein (Zusatzform als eigene Vorabkarte) |
| TETRA-KETTE | TKe0 und TKe3 eingetroffen, TKe1 und TKe2 nicht: Abklingen in Dreierstufen, Faktor ~10 je drei Tetraeder | weiter, klein (Defektort verschieben) |
| KEGEL-Q | KQ0 bis KQ3 eingetroffen: Fuenfer-Ecke bindet, Siebener stoesst ab, exakte Formel auf 0,05 % | erledigt |
| Zufallskarte F-1 | Schreibtisch | parken |

### Einfach gesagt (Runde 26)

Wir koennen jetzt aus einer einzigen Wand eines Q-Balls ausrechnen, bei welchen Groessen ein eindimensionaler Q-Ball
still schwingt, und zwar vorher versiegelt und auf unter ein Prozent genau. Beim runden 3D-Ball klappt das nur, wenn man
die Wellenlaenge im Inneren genau nimmt; mit der Naeherung der flachen Wand liegt man um ein festes Stueck daneben. Ein
Q-Ball haftet an einer Fuenfer-Ecke eines Dreiecksnetzes wie ein Tropfen in einer Kegelspitze. In einer Kette aus
Tetraedern klingt ein Fehler treppenartig ab und stoert nur die Nachbarschaft.

- Journal: nr 563 (claude-runde-v3-26-20261003); Sicherung gestartet. Runde 26 geschlossen 2026-10-03 05:12:02 CEST.
