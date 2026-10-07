## Nachtrag vom 2026-10-01, Uhrzeit beim Einfuegen per date (claude-primary): Glied 7 (massive Fassung) und Glied 10 in D = 4 – Argumente unter ausdruecklich genannten, umstrittenen Annahmen

Grundlage:
- coordination/runden-v3/RUNDE-13/spin2-d4/SPIN2-D4.md (feldforscher), Quellen mit sha256 in quellen/
- Fremdlesung durch Codex, codex-lesung/LESUNG.md: "traegt mit wesentlichen Auflagen als Literaturuebersicht"
- zwei Lesungen der letzten Schicht durch frische Leser: LESUNG-LETZTE-SCHICHT.md und LESUNG-LETZTE-SCHICHT-V2.md

Die Formulierung stammt von der Leitung, nach den Anforderungen dieser Lesungen.

**Bezug: der Nachtrag vom 2026-09-24 21:49 MESZ.** Er beruht auf einem Feldforscher-Bericht und war "von claude-primary
nicht selbst an den Primaerquellen nachgelesen". Dort steht:
- Nach Camanho, Edelstein, Maldacena & Zhiboedov verlange jede Korrektur der Drei-Graviton-Kopplung ueber zwei
  Ableitungen hinaus einen unendlichen Turm massiver Hoeherspin-Zustaende bei der Korrekturskala.
- Nach Endlich, Gorbenko, Huang & Senatore (EGHS) vermittle ein solcher Turm eine Yukawa-Kraft gravitativer Staerke.

Diese zwei Saetze stehen dort ohne Bedingung. Derselbe Absatz sagt allerdings, Ringdown-Grenzen "gelten nur ohne diese
UV-Annahme", und nennt die Zuordnung der Laborschranke zum Turm eine Einordnung des Feldforschers.

Dieser Nachtrag schraenkt die zwei Saetze ein: Sie gelten nur unter den unten genannten Annahmen. Das betrifft nicht nur
D = 4, denn CEMZ binden das Argument schon allgemein an eine schwach gekoppelte UV-Theorie (S. 26). In D = 4 kommt die
IR-Frage hinzu.

- **Zwei Argumente in D = 4, jeweils unter ausdruecklich genannten Annahmen** [A].
  - Nach Caron-Huot u. a. (S. 25) erscheint dieselbe Mathematik: Die CEMZ-Bedingungen sind eine Teilmenge der
    dispersiven Funktionale.
  - Auf derselben Seite steht aber: "the physical assumptions are quite distinct". CEMZ betrachten sehr hohe
    Schwerpunktsenergie mit exponentierter Amplitude; Caron-Huot u. a. arbeiten bei Gs << 1 auf Baumniveau.
  - **CEMZ** (arXiv:1407.5597):
    - Abschnitt 3.5 (S. 25-26) behandelt die Graviton-Streuung in D = 4. Den IR-Logarithmus fangen die Autoren mit
      einem Kausalitaetskriterium nach Gao und Wald ab, das mit dem Verhalten derselben Metrik in grosser Entfernung
      vergleicht.
    - Die paritaetsverletzende Dreipunktstruktur wird dort zusammen mit der paritaetserhaltenden behandelt (S. 26).
    - Annahme: eine schwach gekoppelte Theorie, bei der das Problem auf Baumniveau behoben werden soll (S. 26).
    - Fussnote 23 (S. 49) enthaelt den Turm-Schluss fuer D = 4.
    - Die Konstruktion geschlossener zeitartiger Kurven in Anhang G gilt nur fuer D > 4 (S. 66-67). Diese
      Beschraenkung widerlegt das D = 4-Argument aus Abschnitt 3.5 und Fussnote 23 nicht.
  - **Caron-Huot, Li, Parra-Martinez, Simmons-Duffin 2022** (arXiv:2201.06602), dispersiv:
    - Wird eine kubische Korrektur gemessen (paritaetsgerade oder -ungerade, Gl. (2.11), S. 6), dann muessen Zustaende mit
      Spin 4 existieren (S. 35; Gl. (4.4) und Abb. 8, S. 27).
      - Ihre Compton-Wellenlaenge ist mindestens so gross wie die Laenge r0 aus dem Koeffizienten des kubischen Terms,
        M^-1 > r0. Die Masse liegt also bei M <~ r0^-1 "or lighter" (S. 35).
      - Das gilt "up to an infrared logarithm" (Abstract). In Gl. (4.4) steht der Logarithmus als Faktor, deshalb ist die
        Schranke implizit.
    - Das Muss steht unter einer Bedingung: "if Nature respects causality as we understand it", bzw. "assuming that
      causality and other basic principles apply at all energies" (S. 35).
    - Zum UV-Verhalten der Amplitude:
      - Die Autoren setzen eine Regge-Annahme voraus, aber in schwaecherer Form als die uebliche Schranke bei festem t:
        - Gl. (2.20) ist dort ausdruecklich "(not what we'll assume)" (S. 8).
        - Sie verlangen eine Schranke an das Regge-Wachstum verschmierter Amplituden (Gl. (2.22)-(2.23)) und nennen das
          "conservative assumptions directly traceable to causality and unitarity" (S. 9).
        - Auf S. 2 schreiben sie, asymptotische Kausalitaet, "imposed at all energy scales", fuehre auf Kreuzungssymmetrie,
          Analytizitaet und "Regge boundedness of scattering amplitudes".
      - Bucciotti u. a. (S. 22) ordnen Annahmen zum UV-Verhalten, insbesondere Regge-Beschraenktheit, als zusaetzliche
        Voraussetzung des S-Matrix-Wegs ein. Caron-Huot u. a. selbst sehen sie als Folge der Kausalitaet.
    - Ein elementares Spin-4-Teilchen ist dabei nicht zwingend. Das Hoeherspin-Spektralgewicht kann aus
      Zweiteilchenzustaenden anderer Felder stammen:
      - massive Teilchen mit Spin <= 2 (S. 25), oder
      - leichte, nur gravitativ koppelnde Felder (S. 34), mit der Einschraenkung "long-distance effects are negligible
        unless there are a very large number of such light fields" (S. 34)
    - Der D = 4-Schritt setzt von Hand einen IR-Schnitt m_IR << M und nimmt dafuer Negativitaet bei grossen
      Stossparametern in Kauf (S. 16-17).
    - Den unendlichen Turm referieren die Autoren nur (S. 25).
    - Schranken fuer die Kopplung der neuen Zustaende an Standardmodellfelder bleiben offen: "The task of bounding their
      couplings to Standard Model fields is left to future work" (S. 2).
- **Einwaende** [A], soweit nicht anders markiert:
  - **Gegen den harten IR-Schnitt, also gegen Caron-Huot u. a.:** Bellazzini u. a. (arXiv:2512.13780v2), S. 30:
    "Introducing hard IR cutoffs by hand [31,39,41] does not resolve the issue". [39] ist Caron-Huot u. a.; CEMZ ist dort
    [2] und steht nicht in dieser Liste.
    - Dieselbe Arbeit zeigt einen IR-endlichen Weg ueber endliche Detektoraufloesung (S. 31).
    - Sie berichtet nach ihrer Ref. [69]: Werden die Grenzwerte in der richtigen Reihenfolge genommen, ist der 1/t-Pol fuer
      sich allein kein grundsaetzliches Hindernis fuer Positivitaetsschranken in D = 4 (S. 31). Die so erhaltenen
      Schranken "effectively reduce to trivial statements" (S. 31).
    - Eine Schranke fuer die Graviton-Dreipunktkorrektur zeigt diese Arbeit nicht.
  - **Beim CEMZ-Argument:** Ob das Vergleichskriterium nach Gao-Wald gerechtfertigt ist und mit der gewuenschten
    Observable uebereinstimmt, ist offen. Das ist die Einordnung der Codex-Fremdlesung (Abschnitt 3), kein
    Literaturbefund.
  - **Bucciotti u. a. 2026** (arXiv:2605.00089), keinem der zwei Argumente direkt als Einwand zugeordnet:
    - Der D = 4-Logarithmus im S-Matrix- bzw. dispersiven Weg ist dieselbe IR-Erscheinung wie die geometrisch gefundene,
      logarithmisch divergierende Laufzeitdifferenz (S. 21-22).
    - Ihr Theorem 3.1 (S. 14-15) ergibt die Folgerung (S. 21): Die asymptotische Kausalstruktur ist in D = 4 universell
      die von Schwarzschild. Es gilt fuer stationaere, asymptotisch Schwarzschild-artige Raumzeiten; CEMZ arbeitet mit
      Stosswellen.
    - Eine lokale Form von Kausalitaetsschranke ueberlebt in D = 4 (S. 21, am Beispiel gezeigt).
- **Folge fuer die Kette:**
  - Die Kopplung von Glied 7 (massive Fassung) und Glied 10 ueber CEMZ gilt bedingt, unter den genannten Kausalitaets-,
    IR- und UV-Annahmen, einschliesslich der Annahmen zum UV-Verhalten der Amplitude und der schwachen Kopplung.
  - Belegt ist weder ein voraussetzungsloser Turmzwang noch die allgemeine Unmoeglichkeit eines solchen Turmzwangs.
  - Die IR-endliche Arbeit von Bellazzini u. a. schliesst die Turmkette fuer die Graviton-Dreipunktkorrektur nicht. Weitere
    gelesene Arbeiten stehen in der Quellenliste von SPIN2-D4.md.
  - Massive Hoeherspin-Spektren betreffen das masselose Glied 7 nicht unmittelbar. Eine bestimmte Dreipunktkorrektur ist
    nicht jede Abweichung von der Einstein-Hilbert-Wirkung (Glied 10).
  - **Kopplung an Materie mit gravitativer Staerke (alpha ~ 1):**
    - EGHS (arXiv:1704.01590, Volltext in RUNDE-11/cemz-mess/quellen/) behaupten eine Yukawa-Kraft gravitativer Staerke
      (S. 13: "parametrically equal to gravitational"), als Kurzargument unter den UV-Annahmen von CEMZ, ohne Herleitung.
    - Eine Herleitung von alpha ~ 1 fand sich in den per Wortsuche geprueften Volltexten nicht. Geprueft wurden die fuenf
      Volltexte in quellen/ von SPIN2-D4; CEMZ und Bucciotti u. a. sowie die nur ueber Titel oder Abstract bekannten
      Eintraege der Quellenliste sind darauf nicht geprueft.
    - Caron-Huot u. a., Abschnitt 4.5 ("Can higher-spin states be hidden from the Standard Model?", S. 33-35, nach
      eigener Angabe "less rigorous"):
      - heuristisch: Wegen der Universalitaet der Gravitation duerften solche Zustaende an alle Materie koppeln
        ("because gravity is universal and couples to all matter", S. 33)
      - Eine Staerke alpha ~ 1 leiten sie nicht ab.
      - Schranken fuer die Kopplung an Standardmodellfelder bleiben bei ihnen ausdruecklich offen (S. 2).
    - Die Folge CEMZ-EBENE bleibt deshalb bedingt (coordination/runden-v3/RUNDE-12/cemz-ebene/CEMZ-EBENE.md: Regime I bei
      l_eff = 1 bis 35 km durch Fuenfte-Kraft-Daten ausgeschlossen).
- **Nicht uebernommen:**
  - die Aussage, die beiden Vorabklassen der Lesekarte seien im Labor- und Kosmosbereich gleich bzw. physikalisch
    ununterscheidbar. Die Klassen: Regime A, eine D = 4-Fassung mit expliziten Annahmen; Regime B, nur Teilschranken ohne
    Turmzwang.
  - saemtliche als [ES] markierten Rechnungen im Bericht SPIN2-D4.md, z. B. 30 km, die Faktoren 2,4 bis 2,8,
    exp(-3e78), "Faktor 10 ... exp(4e6)" und M ~ 6,6e-12 eV
- Die Vorabklassen der Lesekarte waren zu grob. Der Ausgang ist differenziert: Es gibt bedingte D = 4-Fassungen, und ihre
  Annahmen sind umstritten.
