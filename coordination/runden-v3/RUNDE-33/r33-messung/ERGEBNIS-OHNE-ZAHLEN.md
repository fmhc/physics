# R33 Messseite: Ergebnis ohne Zahlen (Code-Agent, Blindtest weit draussen, beta = 1)

- Code-Agent (Claude, Anthropic) im Auftrag der Leitung claude-primary. Beginn 2026-10-03 14:01:28 CEST (date).
  Geschrieben ab 14:56:47 CEST (date); Ende in der letzten Zeile.
- **Rauchlauf** (nur bekannte Sprossen k = 0, -1, -2 und z >= 112): .69, 12:20:43 bis 12:23:22 UTC, 12 Aufrufe ueber
  rauch.sh, alle rc = 0; dazu eine Syntaxprobe und ein zweiter kette-Aufruf auf den Rauchdaten (Selbstanzeige 2).
- **Plan eingefroren** 14:28:05 CEST (PLAN.md.eingefroren-20261003-142805, sha256 682f2fd6...), vor jeder echten
  Rechnung; ANKUENDIGUNG.txt vorher geschrieben, von der Leitung um 14:28:43 an Codex weitergeleitet (RUNDE-33.md).
- **Echte Laeufe** (code/start.sh, einmal per nohup): .69, 12:28:13 bis 12:54:41 UTC (26,5 min Wanduhr), 62 Aufrufe,
  alle rc = 0.
- **Versiegelt:** lauf-69/MESSUNG-R33-VERSIEGELT.json (chmod a-w, ebenso auf der .69), sha256 in MESSUNG-HASH.txt.
- Markierungen: [A] Festlegung im Plan, [N] nach dem Einfrieren (nur Darstellung). Alles gilt im linearen, radialen
  Zweikanalmodell (l = 0, abgeschnittener Rand): numerische Evidenz im Modell, keine Labormessung.
- **Diese Datei nennt keine Lagen** (omega^2, eps, z, Fenstergrenzen, Radien) der Fortsetzungen k = -3 .. -25. Zahlen
  stehen nur fuer die bekannten Sprossen k = 0, -1, -2, fuer Genauigkeiten und fuer Laufzeiten.

## Ergebnis zuerst

1. **Gesamtstatus: vollstaendig.** Alle 23 Fortsetzungen k = -3 .. -25 sind nach den eingefrorenen Kriterien gemessen;
   keine ist UNRESOLVED. Die Ziele k = -10, -18 und -25 sind OK.
2. **Unsicherheitsklasse:** alle 23 in Klasse A (Unsicherheit in z = 1/eps unter 1e-3; groesste unter 1e-4). Die
   Lage stammt in allen 23 Faellen aus dem Gitter h = 0,02.
3. **Eindeutigkeit:** In jedem der 23 Fenster gab es auf dem Abtastgitter genau einen Vorzeichenwechsel und genau eine
   verfeinerte Wurzel. Jede Abtastzeile hat im ganzen rho-Fenster genau eine Nullstelle von L1 (ein einziger Ast).
   Die Umlaeufe wechseln ohne Ausnahme ab (+1, -1, +1, ... ab k = -3, anschliessend an -1 bei k = -2), in allen 23
   Rechtecken mit aufgeloester Phase, die dasselbe ergibt (groesster Phasensprung unter 0,3 rad).
4. **Hash der versiegelten Datei:** 034df190a68dadbc9c9df0e332d71c6e2ad1f61be72c9033ff9f20f096179084.
5. **Kontrollen:** k = 0, -1, -2 kamen auf beiden Gittern auf hoechstens 5e-12 in omega^2 an die RUNDE-31-Werte
   heran (Auftrag: < 1e-6), mit den Umlaeufen -1, +1, -1.

## Warum ein neues Verfahren noetig war

- In RUNDE-31 wurden die zwei regulaeren Loesungen y_a, y_b getrennt bis zum Anschluss integriert. Im Kern waechst die
  geschlossene Kanalloesung exponentiell, beide Loesungen werden fast parallel, und die Messgroesse s entsteht aus
  einer Ausloeschung. Im Rauchlauf wuchs sie um 10^5,5 bis 10^6,3 bei den bekannten Sprossen und um 10^17,0 bis
  10^17,3 bei z = 112 bis 115, also etwa um 10^(0,30 R). Fuer die Ziele hiess das 10^9 bis 10^15.
- Bei z = 112 bis 115 lieferte das RUNDE-31-Verfahren s um zwei bis drei Groessenordnungen falsch, an einer der drei
  Zeilen mit falschem Vorzeichen. Damit waere die Messung bei den fernen Zielen gescheitert.
- **Stabilisiert (Godunov/Conte):** Die zwei Loesungen werden alle 8 Schritte orthonormiert. Mathematisch bleibt alles
  gleich: dieselben Nullstellen in rho, dasselbe Vorzeichen von s, dieselben Umlaufzahlen (positiver Faktor bzw.
  orientierungstreue Abbildung, PLAN.md Abschnitt 3). Numerisch verschwindet die Ausloeschung: Orthonormierung alle
  2, 8 oder 32 Schritte gab bei R ~ 57 dasselbe s auf 1e-12 relativ.
- Das Profil wird skalar per Bisektion geschossen (gleiche Regeln wie bic2.profil, Gegenprobe: gleich auf 1e-12),
  50-mal schneller. Physik, Gitter und Raender sind die von RUNDE-31.

## Ablauf (PLAN.md, eingefroren)

- **Fenster** [L]: fuer k = -3 .. -25 der Reihe nach [z_(k+1) + b/2, z_(k+1) + 3b/2], b = b_inf = 2,6186, z_(k+1) die
  zuletzt gemessene Lage (h = 0,02); Start bei k = -2 aus RUNDE-31 (sprossen.json, sha256 4267791b...).
- **Phase 1, Abtastung:** 209 feste Zeilen im Abstand dz = b_inf/8 ueber den ganzen Bereich, in dem die Fenster liegen
  konnten (13 Abschnitte, Randzeilen doppelt gerechnet). Je Zeile Profil, 1001 rho-Punkte, Nullstellen von L1, s.
- **Phase 2, Wurzeln:** jeder der 26 Vorzeichenwechsel (23 in den Fenstern, 3 jenseits des letzten Fensters) per
  Illinois in omega^2 auf h = 0,04 verfeinert (Klammer <= 1e-10, hoechstens 6 Schritte), dazu ein Umlauf-Rechteck auf
  den zwei Startzeilen.
- **Phase 3:** jede Wurzel neu auf h = 0,02 aus der engen Klammer +-1e-5 und als Randprobe mit Aussenrand + 20.
- **Phase 4, kette:** die Fensterlogik mechanisch nach PLAN.md Abschnitt 4; Ergebnisdatei, dann versiegelt.

## Kriterien und Ausgang (je Fenster, PLAN.md Abschnitt 4)

| Kriterium | Ausgang (23 Fenster) |
|---|---|
| (a1) Abtastung deckt erweitertes Fenster, Luecke <= dz | 23 von 23 (je 10 oder 11 Zeilen) |
| (a2) genau eine Nullstelle von L1 je Zeile, Zielast, gleiche Richtung, stetiger Ast | 23 von 23 (Astsprung zwischen Nachbarzeilen hoechstens 2e-4 in rho) |
| (a3) doppelt gerechnete Randzeilen gleiches Vorzeichen | 12 von 12 Randzeilen |
| (a4) Rauschreserve des Vorzeichens (|s| > 1e-12 * groesster Einzelterm) | 23 von 23 |
| (a5) keine Beinahe-Nullstelle (5 %-Regel) | 23 von 23, keine Zeile auffaellig |
| (b1) alle Wechsel verfeinert, genau eine Wurzel im Fenster | 23 von 23, je genau ein Wechsel im erweiterten Fenster |
| (b2) Wurzel h = 0,04 konvergiert, Wechsel bestaetigt, Ast konsistent | 23 von 23 |
| (b3) Umlauf +-1, wechselnd | 23 von 23 |
| (b4) h = 0,02 konvergiert, Gitterdifferenz <= 1e-6 | 23 von 23 (Gitterdifferenz 6,8e-9 bis 1,7e-8 in omega^2) |
| (b5) Unsicherheit in z < 0,05, Abstand zu den Fensterraendern groesser | 23 von 23 |
| berichtet: Phase aufgeloest und gleich der Kreuzung | 23 von 23 |
| berichtet: Randprobe (Aussenrand + 20) | 23 von 23 gerechnet, Verschiebung hoechstens 2e-15 in omega^2 |

- Unsicherheit je Sprosse = Gitterdifferenz + Endklammer (hoechstens 8,6e-11) + Rauschmass (hoechstens 1,6e-18) +
  Randprobe, alles in omega^2; durch eps^2 geteilt in z. Sie wird von der Gitterdifferenz bestimmt.
- Doppelt gerechnete Randzeilen: gleiche Vorzeichen; der Betrag von s weicht bis 27 % ab, weil jeder Abschnitt seinen
  eigenen Anschluss r_m hat und s nur bis auf einen positiven Faktor festliegt. Deshalb vergleicht (a5) nur innerhalb
  eines Abschnitts.

## Kontrollen an den bekannten Sprossen (Rauchlauf, Zahlen bekannt)

| Sprosse | h = 0,04 (gegen R31 h004) | h = 0,02 (gegen R31 h002) | Umlauf Kreuzung / Phase |
|---|---|---|---|
| k = 0 | 0,7785854193053 (+7,6e-13) | 0,7785854399004 (+5,5e-13) | -1 / -1 |
| k = -1 | 0,7766066086376 (-1,5e-12) | 0,7766066277135 (-2,3e-12) | +1 / +1 |
| k = -2 | 0,7748827580576 (+4,7e-12) | 0,7748827758194 (+4,6e-12) | -1 / -1 |

- k = -1 lief zusaetzlich als ganze Kette (Abtastung, Wurzel, Gitter, Randprobe, Fensterlogik ab k = 0): genau eine
  Sprosse im Fenster, 1/eps = 37,584620297 (R31: 37,58462029), Klasse A, alle harten Kriterien erfuellt.
- Gleichwertigkeit mit RUNDE-31 zwischen bekannten Sprossen (z = 36,28 und 38,88): Nullstelle von L1 gleich der von
  L(y_b) auf 2e-15, Vorzeichen von s gleich.

## Laufzeiten und Budget

| Phase | Aufrufe | Rechenzeit | groesster Aufruf |
|---|---|---|---|
| 1 Abtastung | 13 | 21,6 min | 121 s |
| 2 Wurzeln h = 0,04 (+ Wiederholungen) | 8 + 8 | 20,6 min | 193 s |
| 3 Gitter h = 0,02 (+ Wiederholungen) | 8 + 8 | 31,1 min | 277 s |
| 3 Randprobe (+ Wiederholungen) | 8 + 8 | 21,7 min | 188 s |
| 4 kette | 1 | 3 s | 3 s |

- Zusammen 62 Aufrufe (38 plus 24 Wiederholungen, die alle leer waren: keine Klammer fehlte), 95 min Rechenzeit, 26,5 min
  Wanduhr auf vier Spuren (cpu, cpu2, cpu3, cpu4). Angekuendigt waren 38 plus bis zu 24, etwa 2 h CPU und 30 bis 45 min
  Wanduhr. Rauchlauf: 12 Aufrufe, 7 min Rechenzeit.

## Latten (v3)

- **L1 (kann scheitern): ja.** Alle Kriterien und die Fensterregel standen vor dem ersten echten Lauf fest; jedes
  Fenster haette UNRESOLVED werden koennen, die Genauigkeit haette an (b4) oder (b5) scheitern koennen.
- **L2 (Gegenprobe): teilweise.** Bekannte Sprossen, zwei Gitter, Randprobe, doppelte Randzeilen, Phasenumlauf
  unabhaengig von der Kreuzungszaehlung, Orthonormierungstakt 2/8/32. Es gibt kein zweites, unabhaengig geschriebenes
  Programm (gleiches Physikmodul wie RUNDE-31).
- **L3 (Numerik): ja.** Klasse A in allen 23 Faellen; die Grenze setzt das Gitter, nicht die Rundung.
- **L4 (schon bekannt):** RUNDE-13, -24, -26, -31 im Projekt; die Orthonormierung nach Godunov/Conte ist ein
  Standardverfahren fuer steife Randwertprobleme. Literatur nicht gesucht.
- **L5 (Messbezug): nein.** Modellintern (linear, radial, l = 0).

## Grenzen

- Nur zwei Gitter (h = 0,04 und 0,02); h = 0,02 startete in der engen Klammer um die h = 0,04-Wurzel.
- Abtastung im Abstand dz = b_inf/8: ein zusaetzliches Sprossenpaar mit Abstand unter dz zwischen zwei Zeilen schliesst
  sie nicht beweisartig aus; (a5) und die Ein-Ast-Pruefung machen es unwahrscheinlich.
- Die Gitterdifferenz waechst leicht mit dem Radius; eine dritte Stufe (h = 0,01) fehlt wie in RUNDE-13/24/31.

## Selbstanzeigen

1. **RUNDE-33.md gelesen** (Auftrag nannte den Leitungstext): Er enthaelt die Form der Primaervorhersage
   z0(j) - C1/[K z0(j)] und das Tor 0,10, keine Konstanten. Die Fensterregel war davon unabhaengig woertlich vorgegeben.
2. **Zaehlfehler im eingefrorenen Plan:** Abschnitt 2 nennt "13 Aufrufe" im Rauchlauf; es waren 12 ueber rauch.sh,
   dazu eine Syntaxprobe und ein zweiter kette-Aufruf (14 zusammen). Nach dem Einfrieren nicht geaendert.
3. **Code-Fassungen:** Die Rauchlaeufe zeilen/wurzel liefen mit der Vorfassung von r33_stab.py (e1a04938...). Vor dem
   Einfrieren geaendert (nur kette: Begruendungstext bei fehlender Abdeckung, Kriterium a4) und auf den Rauchdaten
   erneut gerechnet; im Plan vermerkt. Seit dem Einfrieren sind Plan, Code und Skripte unveraendert (sha256 unten).
4. **Profil anders gesucht als RUNDE-31** (skalare Bisektion statt 1024 Kandidaten je Runde), Regeln gleich; Gegenprobe
   im Rauchlauf (gleich auf 1e-12), Lagen der bekannten Sprossen auf 5e-12 gleich.
5. **Rho-Bezug** fuer die Astwahl mit Steigung 0,881 (aus den drei R31-Sprossen), R31 nahm 0,86; nur Astwahl, da jede
   Zeile genau eine Nullstelle von L1 im ganzen rho-Fenster hatte.
6. **Eigene Sicht auf die Werte:** Ich habe die Lagen der Fortsetzungen nicht angesehen. Alle Zusammenfassungen liefen
   per jq-Filter ohne Lagen (code/bericht.jq [N] und Einzelabfragen: Status, Klassen, Zaehlungen, Genauigkeitsmaxima).
   Nach der Auswertung [N] habe ich per jq (nur wahr/falsch ausgegeben) eine Plausibilitaetsprobe der Abstaende
   aufeinanderfolgender Sprossen gemacht und gezaehlt, wo die 26 verfeinerten Wurzeln liegen: 23 sind die Kette, keine
   liegt vor dem ersten Fenster oder zwischen Fenstern, 3 liegen hinter dem letzten. Die Bedingung der Abstandsprobe
   nenne ich erst nach der Entblindung; sie aendert keinen Status.
7. **Werkzeuge auf der .69:** Rechnungen nur ueber kleintest.sh (Spuren cpu, cpu2, cpu3, cpu4; nicht cpu5, keine GPU),
   auch die Syntaxprobe (py_compile, legte __pycache__ im Laufordner an). Start per nohup setsid bash. Zur Ueberwachung
   ls, cat, grep, jq, sha256sum, chmod, mkdir, date, dazu cut, wc, sort, head und einmal sed -n nur zur Anzeige von
   Zeilenlaufzeiten (gegen die Liste des Auftrags). Kein pkill/pgrep, nichts in place ueberschrieben.
8. **Lokal:** kein Interpreter (kein python3, perl, awk). Benutzt: jq (auch Summen der Laufzeiten), ssh, scp,
   sha256sum, date, cp, chmod, mkdir, ls, cat, grep, printf, comm sowie bash-Warteschleifen und eine Monitor-Schleife
   (ssh-Abfrage alle 20 bis 30 s) zur Ueberwachung.
9. **Nach dem Einfrieren geschrieben, nur Darstellung** [N]: code/bericht.jq, MESSUNG-HASH.txt, diese Datei.
10. **Sonst:** kein git, kein Peerbus, kein Journal, keine Unteragenten, keine Dienste, Timer oder Hooks; keine Aenderung
    ausserhalb von RUNDE-33/r33-messung/ (lokal) und /home/fmh/fmhc-physics-remote/runde33-messung/ (.69). Rohdaten
    bleiben auf der .69; lokal liegt nur die versiegelte Messdatei.

## Unveraendert seit dem Einfrieren (sha256, lokal = .69)

- PLAN.md = PLAN.md.eingefroren-20261003-142805: 682f2fd6c0d2c71086b5cc9645adf148c3f87cf9657ce8395d88beaa0653e8bb
- code/r33_stab.py: fa7a06ec5f3e7c00b9e0b16abddda9f9e3bcbf1d68fa7ad453690ea457644182
- code/start.sh: 24624192755645198959c16e1bdc930b5c26984ef13371cbc8ff1380dbf4ff4c
- code/rauch.sh: 8d2e63419f456a0239478e3303d4c5f27757671767b1c6d158f64f125ffec772
- code/bic2_3d_suche_v2.py (= RUNDE-31): 6beabc3f0d499df31a20c21fc9a35a2dc028117be5df05badf7863c22eb53c71
- lauf-69/MESSUNG-R33-VERSIEGELT.json: 034df190a68dadbc9c9df0e332d71c6e2ad1f61be72c9033ff9f20f096179084

## Einfach gesagt

Ein Q-Ball kann bei bestimmten Frequenzen schwingen, ohne Wellen abzustrahlen; diese Frequenzen bilden eine Leiter
mit fast gleichen Abstaenden. Ich sollte 23 weitere Sprossen dieser Leiter messen, bis zu sehr grossen Baellen, ohne
die versiegelten Vorhersagen zu kennen. Das alte Rechenverfahren haette dort versagt, weil eine Teilloesung im Inneren
des Balls um bis zu 15 Zehnerpotenzen waechst und die Computergenauigkeit ueberrollt; mit einem Trick, der die
Rechnung unterwegs immer wieder neu ausrichtet, bleibt sie genau. Alle 23 Sprossen sind eindeutig gefunden, jede mit
wechselndem Drehsinn und auf zwei Rechengittern auf mindestens drei Nachkommastellen von 1/eps sicher. Die Werte sind
versiegelt; nur ihr Fingerabdruck (Hash) geht an die Leitung.

---
Letzte Aenderung dieser Datei: 2026-10-03 14:58:36 CEST (date). Zeitbox 150 min ab 14:01:28 eingehalten (rund 58 min).
