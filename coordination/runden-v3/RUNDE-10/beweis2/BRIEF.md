# BRIEF BEWEIS-2: zwei weitere stille Stellen rechnergestuetzt beweisen

- Leitung: claude-primary. Auftrag geschrieben ab 2026-09-30 12:05:26 CEST (date vor dem Schreiben).
- Anlass: Finn, 30.09. mittags, "ja maach weiter" auf die Frage der Leitung, ob der Beweis-Agent weitere Sprossen
  beweisen soll (n = 2 und die erste Schwapp-Stelle) und ob die Leitung bei Codex wegen der Fremdpruefung nachhakt.
- Autor: derselbe Beweis-Agent wie BEWEIS-1 (Haus Anthropic). Lesungen macht danach ein frischer Leser, nicht der Autor.
- Arbeitsordner: lokal coordination/runden-v3/RUNDE-10/beweis2/, auf der .69 /home/fmh/fmhc-physics-remote/runde10-beweis2/.
  BEWEIS-1 (RUNDE-07/beweis/) bleibt unveraendert; Kern und Treiber nur als Kopie unter neuem Namen aendern
  (z. B. bewkern-l.py, pruef-l.py), nie in place. SHA256SUMS.txt im neuen Ordner neu anlegen.

## Ziele

| Ziel | Leiter | l | n | Startwerte (DATENPAKET, RUNDE-09/daten-leiter/DATENPAKET.json) | Quelle im Paket |
|---|---|---|---|---|---|
| T1 | Atmung psi_1 | 0 | 2 | omega^2 = 0,6851289043286388, rho = 1,6903565771078266 | id A02 (A_out-Nullstelle; W-Fit 0,6851289138) |
| T2 | Schwappen psi_1 | 1 | 1 | omega^2 = 0,7544960183525193, rho = 1,826342067337926 | id C01 (Umlauf aufgeloest, h = 0,01) |

- Reihenfolge: erst T1 (nur neue Startwerte, gleicher Satzaufbau), dann T2 (neuer Sektor).
- Nach T1 eine Zwischenmeldung an die Leitung (SendMessage an main), dann T2.

## Was sich fuer T2 (l = 1) aendert, bitte im Plan ausschreiben

1. Radiale Gleichungen mit Zentrifugalterm l(l+1)/r^2 = 2/r^2 in beiden Kanaelen, reduzierte Funktionen A = r a,
   B = r b mit A, B ~ r^(l+1) = r^2 am Ursprung. Profil f ist unveraendert (l = 0), nur bei anderem omega.
2. Start am Ursprung (Lemma T0): regulaerer singulaerer Punkt mit anderem Exponenten. Ein Weg: a = r alpha, dann
   alpha'' + (4/r) alpha' = ... (Struktur wie beim Profil, Koeffizient 2(l+1) statt 2). Strenge Huelle und Rest wie in T0.
3. Schwanz (Lemma J und Jost-Daten J_0): freie Loesungen sind jetzt modifizierte sphaerische Bessel- bzw.
   Riccati-Hankel-Funktionen statt reiner Exponentiale. Entweder exakt einsetzen oder 2/r^2 <= 2/L^2 mit in die
   Stoerung nehmen; die Schranke muss auf ganz Z gelten.
4. Einfachheit (Lemma E) fuer l = 1 neu begruenden. Der Translations-Nullmode (rho = 0) liegt weit weg, trotzdem
   im Plan erwaehnen, warum er nicht stoert.
5. Kanalzahlen: offener Kanal omega + rho, geschlossener omega - rho; die Ungleichungen (Kontinuum, kappa_c^2 > 0)
   aus dem Kasten pruefen.
6. Folgerung Krein (KREIN-1, RUNDE-09/krein1/ERGEBNIS.md): E_2 = 2 rho [(omega + rho)||a||^2 + (rho - omega)||b||^2]
   ist positiv, sobald rho - omega > 0 auf dem Kasten gilt. Fuer T1 und T2 als Korollar mitnehmen (eine Zeile).

## Pflicht vor jedem Beweislauf (vorab heisst: vor der Ergebnisdatei, mtime pruefen)

- Plan BEWEIS-2-PLAN.md mit den geaenderten Lemmata und der Liste der geaenderten Codezeilen.
- Vorab-Zeile je Ziel, mit date gestempelt, vor dem Newton-Lauf: erwarteter Bereich fuer omega^2 und rho aus dem
  Datenpaket (T1: A_out und W-Fit liegen 1e-8 auseinander; T2: Feinwert h = 0,01) und die Negativkontrolle
  (Kastenmitte rho + 4 delta muss verfehlen, rho + delta/4 bestehen), wie in BEWEIS-1.
- Frei-Test mit dem neuen Kern auch fuer l = 1 (f = 0, geschlossene Loesungen: sphaerische Bessel-Funktionen).

## Rechnen

- Nur auf der .69, Spur cpu5 (fuer BEWEIS reserviert), ein Kern, ueber runden-v3/kleintest.sh; jeder Lauf hoechstens
  10 min. Logs mit absolutem Pfad. Keine GPU noetig.
- Lokal (Laptop): kein python/python3/awk, auch keine leeren Aufrufe; jq ist erlaubt. Zeiten nur per date.
- Zwei Zertifizierungen je Ziel wie in BEWEIS-1 (A: Beweislauf, B: anderes L, Gitter, Bitzahl), dazu die
  Empfindlichkeitskontrolle.

## Abgabe

- BEWEIS-2.md im Stil von BEWEIS.md: Satz mit Kasten in dyadischen Grenzen, was nicht behauptet wird, Beweisstruktur,
  Zertifikatstabelle, Unterschiede zu BEWEIS-1 als eigene Tabelle (Zeile fuer Zeile Code und Lemma).
- STAND.md fortlaufend (gleiches Format wie RUNDE-07/beweis/STAND.md).
- Scheitert T2 an einer echten Luecke (z. B. Lemma E), dann die Luecke genau benennen und T1 allein abgeben;
  kein Ausweichen auf schwaechere Aussagen ohne Vermerk.
- Zeitrahmen: hoechstens 2,5 Stunden ab Start. Danach Stand abgeben, auch wenn T2 offen ist.

## Danach (Leitung, nicht Autor)

- Ein frischer Leser liest Plan, Codeunterschiede und BEWEIS-2.md in einem Durchgang (eine Lesung statt drei, weil
  der Kern schon gelesen ist).
- Codex (Haus OpenAI) ist fuer die Fremdlesung von BEWEIS-1 angefragt; BEWEIS-2 folgt dort nach.
