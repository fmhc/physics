# SCHWARZES-LOCH: Was passiert auf Finns Netz V bei sehr starker Masse? (Folgeauftrag zu BETA-NETZ-V, ohne Karte)

- Code-Agent fuer die Leitung claude-primary. Anlass: Finns Frage "ist das mit der masse ggf der effekt der in einem
  schwarzen loch auftritt und verstaerkt oder so?". Kein Plan-Einfrieren, kein frischer Leser.
- Zeiten (date; .69 in UTC, CEST = UTC + 2):
  - Start 2026-10-05 18:01:27 CEST.
  - Laeufe 16:03:05 bis 16:57:54 UTC, alle rc = 0, ueber kleintest.sh (cpu8, cpu9, cpu10), df vor jedem Start (18 GB
    frei).
  - Text ab 18:58:36 CEST.
- Kennzeichen: [E] gerechnet, [M] eigene Herleitung, [L] Literatur aus dem Gedaechtnis, ungeprueft, [H] Hypothese,
  [N] nach Sicht auf Gitterzahlen festgelegt. Alles synthetisch, keine Messdaten.
- Einheiten: s = Gesamtstaerke der Quelle (wie BETA-NETZ-V; linear M = 0,05627 s l_P). R0 = Kugelradius in l_P.
  x = M_iso/(2 R0), Kompaktheit 2M/R = 4x/(1 + x)^2 (R = Flaechenradius des Kugelrands). Ein Horizont am Rand hiesse
  x = 1 bzw. 2M/R = 1. N_mitte = Takt in der Kugelmitte, geteilt durch den Takt im Fernfeld.

## 1. Ergebnis zuerst

1. **Der Takt in der Kugelmitte geht auf V gegen 0, bevor ein Horizont entsteht [E].**
   - L = 12, R0 = 2: N_mitte = 0,0001 bei s = 63; bis s = 63,75 konvergiert die Loesung noch, mit N_mitte < 0.
   - L = 16: N_mitte 0,0366 bei s = 60 (R0 = 2) und 0,0429 bei s = 84 (R0 = 3). Der Nulldurchgang liegt also bei etwa
     63,5 bis 64,5 bzw. 92 bis 93 [Kopf, linear extrapoliert].
   - Dabei ist 2M/R = 0,93 bis 0,96 und x = 0,58 bis 0,66 < 1. Kein Flaechenradius-Minimum (kein Hals); alle Tetraeder
     gueltig (kleinster sin des Diederwinkels 0,40).
2. **Das entspricht fast genau der ART mit Druck (TOV), nicht der ART ohne Druck [E].**
   - Gleiche Quelle mit isotropem Druck (TOV): die Loesungsfamilie endet bei s* = 63,52 (R0 = 2) bzw. 95,28 (R0 = 3).
     Dort gilt N_mitte -> 0 und Zentraldruck -> unendlich; 2M/R* = 0,912.
   - N_mitte(s) des Gitters liegt bei R0 = 2 innerhalb von 0,015 (L = 12) bzw. 0,008 (L = 16) an TOV, bei R0 = 3 bis
     0,03 darunter (Tabelle).
   - Die Masse aus der Takt-Abnahme (Tolman/Komar) gleicht der Masse aus den Laengen (ADM): Gitter K/M = 0,98 bis 1,06,
     TOV 1.
   - Ohne Druck (Kontinuum, nur Zwang und Spur der statischen Gleichung, so wie bestellt) gibt es keine Grenze: N_mitte
     bleibt positiv (0,36 bei s = 64, 0,24 bei 2M/R = 1). Dieses Modell ist aber keine Loesung der ART (K/M = 0,53 bis
     0,99 statt 1).
3. **Warum [M, H]:**
   - Ruhender Staub ohne Druck ist in der ART nie statisch; die Bianchi-Identitaet verlangt rho grad N = 0.
   - Auf dem Netz nimmt der Eichrest M lam genau diesen Fehlbetrag auf. lam wirkt wie N mal eine Haltespannung, also wie
     ein Druck [H, gestuetzt durch die TOV-Naehe].
   - lam bleibt endlich (hoechstens 0,0095) und waechst linear in s. In ART-Sprache waere der Druck p = lam/N an der
     Nullstelle unendlich.
4. **Unterschied zur ART [E, H]:**
   - Auf dem Netz endet die Familie bei N_mitte = 0 nicht. Sie laeuft glatt zu N_mitte < 0 weiter (-0,0027, -0,0061,
     -0,0112 bei s = 63,25; 63,5; 63,75), also mit rueckwaerts laufender Zeit in der Mitte, physikalisch sinnlos.
   - Bei s = 64 haben zwei Versuche nicht konvergiert (236 bzw. 48 Schritte). Beide blieben auf demselben Restniveau stehen
     (RG etwa 5e-6). dN/ds wurde zwischen 63 und 63,75 doppelt so steil.
   - Lesart [H]: Umkehrpunkt (groesste Staerke) knapp unter s = 64. Nicht entschieden; es fehlt eine Fortsetzung mit N
     statt s als Parameter.
5. **Zu Finns Frage:**
   - Die Nahfeld-Abweichung von beta aus BETA-NETZ-V (unter etwa 4 Kantenlaengen) ist ein Gittereffekt der zweiten
     Ordnung bei beliebig kleiner Masse. Ein Effekt eines Schwarzen Lochs ist sie nicht: dessen Groesse ware M, hier
     winzig.
   - Bei sehr starker Masse zeigt das Netz das Verhalten kompakter Sterne der ART: Die Uhr in der Mitte bleibt stehen,
     bevor ein Horizont entsteht. Was danach kommt (Kollaps zum Schwarzen Loch), braucht Dynamik und ist nicht gerechnet.

## 2. Tabellen [E]

R0 = 2 (61 Quellecken). Gitter L = 12 und L = 16; Kontinuum mit Druck (TOV) und ohne Druck, gleiche Quelle und
Kopplung. x und 2M/R sind fuer beide Kontinuum-Modelle gleich, weil der Zwang weder N noch p enthaelt [M].

| s | N_mitte L12 | N_mitte L16 | N_mitte TOV | N_mitte ohne Druck | 2M/R L12 / L16 / Kontinuum |
|---|---|---|---|---|---|
| 1 | 0,9598 | 0,9599 | 0,9592 | 0,9600 | 0,054 / 0,054 / 0,054 |
| 8 | 0,7324 | 0,7353 | 0,7326 | 0,7652 | 0,330 / 0,328 / 0,332 |
| 16 | 0,5438 | 0,5506 | 0,5497 | 0,6369 | 0,526 / 0,520 / 0,526 |
| 32 | 0,2852 | 0,2975 | 0,3003 | 0,4952 | 0,755 / 0,742 / 0,740 |
| 48 | 0,1172 | 0,1304 | 0,1288 | 0,4159 | 0,883 / 0,865 / 0,850 |
| 56 | 0,0540 | 0,0662 | 0,0599 | 0,3876 | 0,925 / 0,907 / 0,886 |
| 60 | 0,0248 | 0,0366 | 0,0285 | 0,3753 | 0,943 / 0,925 / 0,901 |
| 62 | 0,0093 | 0,0215 (nicht konv.) | 0,0134 | 0,3695 | 0,952 / 0,933 / 0,907 |
| 63 | 0,0001 | - | 0,0061 | 0,3667 | 0,957 / - / 0,911 |
| 63,5 | -0,0061 | - | 0,0025 (Ende bei 63,52) | 0,3654 | 0,959 / - / 0,912 |
| 63,75 | -0,0112 | - | keine Loesung | 0,3647 | 0,961 / - / 0,913 |
| 64 | nicht konvergiert (zweimal) | - | keine Loesung | 0,3640 | - |

R0 = 3 (187 Quellecken), Gitter L = 16:

| s | N_mitte Gitter | N_mitte TOV | N_mitte ohne Druck | 2M/R Gitter / Kontinuum |
|---|---|---|---|---|
| 8 | 0,8016 | 0,8090 | 0,8261 | 0,238 / 0,242 |
| 32 | 0,4277 | 0,4538 | 0,5783 | 0,613 / 0,615 |
| 64 | 0,1511 | 0,1802 | 0,4383 | 0,842 / 0,821 |
| 80 | 0,0621 | 0,0819 | 0,3964 | 0,908 / 0,875 |
| 84 | 0,0429 | 0,0599 | 0,3876 | 0,921 / 0,886 |
| 87 | 0,0285 (nicht konv.) | 0,0439 | 0,3813 | 0,931 / 0,894 |
| 95,28 | - | 0 (Ende) | - | - / 0,912 |

- Kontinuum ohne Druck weiter: 2M/R erreicht 1 bei s = 154 (R0 = 2) bzw. 228 (R0 = 3) mit N_mitte = 0,235. Danach faellt
  2M/R, weil sich ausserhalb der Kugel ein Hals bildet (x > 1). Kein Umkehrpunkt bis s = 4096 (N_mitte 0,042).
- Gitter-M kommt aus dem Fernfit (Psi = c0 + c1/r + c2 r^2, r von R0 + 1,5 bis L/2; Rest <= 0,5 %). Bei grossem s liegt es
  ueber dem Kontinuum, bei L = 12 mehr als bei L = 16 (x bei s = 56: 0,571 / 0,533 / 0,496): ein Torus-Effekt. 2M/R des
  Gitters ist deshalb zu hoch, am meisten bei L = 12.
- R0 = 3: Schon linear liegt das Gitter tiefer (s = 1: 1 - N_mitte = 0,0285 gegen 0,0275). Die diskrete Kugel ist etwas
  kompakter als die Kontinuumskugel [Kopf]. Daher setzt auch der Nulldurchgang etwas frueher ein (etwa 92 bis 93 gegen
  95,3).

## 3. Was gerechnet wurde

- **Gitter (code/bn_sl.py, bn.py unveraendert importiert):**
  - dieselbe nichtlineare Statik wie in BETA-NETZ-V: Eckenregel R1, exakte Diederwinkel, Takt je Ecke, isotrope
    Eichung, Eichrest ueber M lam, k = 0 nicht geloest
  - Quelle: Kugel um die Lochmitte C1, sigma je Ecke proportional zum Eckvolumen, ohne Druck
  - Rest per Index-Sammlung; gleich bn.Netz.rest auf 1e-16 (Modus test)
  - Loeser: Anderson (m = 8) auf dem Quasi-Newton-Schritt mit flacher KKT. Fortsetzung in s mit linearem Praediktor
    und gespeicherten Zwischenstaenden, Ziel Schrittweite < 1e-10.
  - Konvergiert in 5 bis 50 Schritten; Endreste RF, RG 1e-13 bis 3e-12.
- **Kontinuum ohne Druck (code/bn_ode.py):** Lap Psi = -E/(8 LP Psi) und div(Psi^2 grad N) = N E/(4 LP).
  - E ist die feste Koordinaten-Energiedichte, die Kopplung dieselbe wie auf dem Netz (linear identisch:
    M = 0,05627 s).
  - Schuss ueber phi(0) = 1, t = s/A^2, RK4 mit 6000 Schritten; Halbierung aendert N_mitte um 2e-14.
- **Kontinuum mit Druck (code/bn_tov.py) [N]:** dazu TOV dp/dr = -(rho + p) N'/N mit p(R0) = 0 und Spur
  (1 + 3 p/rho). Zwang, Spur, TOV und Regularitaet ergeben die volle kugelsymmetrische Einstein-Gleichung [M]. Probe
  K/M = 1 auf 1e-13.
- **Vergleich:** code/bn_vergleich2.py (bn_vergleich.py ohne TOV), gleiche s.

## 4. Was am Aufbau liegt und was gerechnet ist

- **Aufbau [M, L]:**
  - Die Quelle ist Staub mit fester Energie je Ecke. Statisch geht das nur mit einer Haltespannung, die auf dem Netz der
    Eichmultiplikator liefert, nicht ein Stoff mit Zustandsgleichung.
  - Dass der Takt vor dem Horizont stehen bleibt, ist ART-Wissen fuer Sterne mit Druck (Buchdahl 1959: 2M/R < 8/9 bei
    nach aussen nicht wachsender Dichte [L]). Hier waechst die Eigendichte E/Psi^6 nach aussen, deshalb liegt die
    Grenze bei 0,912 statt 8/9.
  - Ohne Haltespannung (bestelltes Kontinuum ohne Druck) gibt es keine Grenze, aber auch keine ART-Loesung.
- **Gerechnet [E]:**
  - Das Netz waehlt ohne Zutun die TOV-nahe Loesung. N_mitte(s) stimmt bei R0 = 2 auf 0,015 (L = 12) bzw. 0,008
    (L = 16) und bei R0 = 3 auf 0,03, die Endstaerke auf etwa 1 % (R0 = 2) bzw. 3 % (R0 = 3).
  - Tolman-Masse gleich ADM-Masse auf 6 %.
  - Kein Hals, kein entarteter Tetraeder.
  - Die Familie laeuft durch N = 0 hindurch und kommt kurz danach nicht weiter.

## 5. Grenzen

1. Statisch, ohne Dynamik: Ob und wie die Kugel kollabiert, ist nicht gerechnet.
2. lam als Druck ist eine Lesart [H]; die Haltespannung des Netzes ist nicht isotrop vorgegeben. Geprueft sind nur
   N_mitte, M und K/M, nicht das Spannungsprofil.
3. Der Torus treibt das Gitter-M bei grossem s nach oben (L12 gegen L16). Fuer L -> unendlich ist kein Wert extrapoliert.
4. Zwei Radien (R0 = 2, 3), eine Mitte (C1), ein Netz (V).
5. Ob es auf dem Netz eine groesste Staerke (Umkehrpunkt) gibt, ist offen [H]; die Fortsetzung in N fehlt.
6. **Zusatz "Ecken frei verschieben": nicht gerechnet.**
   - Die KKT im k-Raum hat eine ortsunabhaengige Eichbedingung; ein lokales Freigeben braucht einen Loeser im Ortsraum.
   - In der Kugel ist lam ausserdem die physikalisch noetige Haltespannung. Freigegebene Ecken nahmen sie weg; dann gibt
     es in der ART keine statische Loesung.
   - Fuer das Nahfeld-beta der Punktquelle waere es der richtige Test (Loesbarkeitsbedingung zweiter Ordnung). Das ist
     aufwendiger als der Zeitrahmen.

## 6. Regelabweichungen und Selbstanzeigen

1. **Python auf der .69 ausserhalb kleintest.sh:** Um 18:37:43 CEST stand in einem ssh-Befehl versehentlich
   `python3 -c 1 2>/dev/null`. Das war ein Leeraufruf ohne Rechnung, mit Umleitung nach /dev/null auf der .69.
2. **ssh mit Eingabe aus /dev/null:** In Warteschleifen habe ich lokal `< /dev/null` benutzt. Das liest nur und schreibt
   nicht; ab 18:43 habe ich `ssh -n` genommen. Die ssh-Steuerdatei in /tmp stammt aus der vorhandenen ssh-Konfiguration,
   nicht von mir.
3. **jq auf der .69 hat Anzeigewerte gerundet und multipliziert;** gerechnet wurde damit nichts.
4. **bn_ode.py nach dem ersten Lauf geaendert:** Die Gueltigkeitspruefung hatte die Werte jenseits der Singularitaet
   durchgelassen. Die erste Ausgabe ist ueberschrieben, die Sicherung geloescht. Die erste Tabelle war nur bis s = 512
   (R0 = 2) bzw. 64 (R0 = 3) gueltig, die zweite stimmt dort mit ihr ueberein.
5. **Nach Sicht [N]:** bn_tov.py und bn_vergleich2.py sind entstanden, nachdem das Gitter vom Kontinuum ohne Druck
   abwich. Die feinen Staerken 63,25 bis 64 und die Lesart "Umkehrpunkt" kamen nach der Sicht auf s = 64.
6. **Im Kopf gerechnet:** Nulldurchgaenge bei L = 16 (lineare Extrapolation), die Aussage "etwa 1 % bzw. 3 %", "dN/ds
   doppelt so steil" und die Kompaktheit der diskreten Kugel (3,6 %).
7. **Zwischenstaende:** 15 Zustandsdateien (z-*.npz, zusammen etwa 80 MB) liegen nur auf der .69 in sl/; lokal ist
   nichts davon kopiert.

## 7. Einfach gesagt

Wir haben eine immer schwerere Kugel ins Netz gesetzt und geschaut, wie langsam die Uhr in ihrer Mitte geht. Ab einer
bestimmten Masse bleibt die Uhr in der Mitte ganz stehen, und zwar fast genau dort, wo das auch Einsteins Theorie fuer
einen Stern mit Druck sagt, also noch bevor ein Schwarzes Loch (Horizont) entsteht. Was danach passiert, also der
Zusammensturz zum Schwarzen Loch, kann diese ruhende Rechnung nicht zeigen.

## 8. Dateien

- code/: bn_sl.py (Gitter), bn_ode.py (Kontinuum ohne Druck), bn_tov.py (mit Druck), bn_vergleich.py,
  bn_vergleich2.py.
- sl-69/: alle json, log und txt der .69 (Rauchlauf test-L6, rauch-L6; Reihen L12-R2-a/b/c/e, L16-R2-a bis e,
  L16-R3-a bis e; ode, tov, vergleich-1, vergleich).
- PRUEFSUMMEN-SL-69.txt (auf der .69 erzeugt, 61 Dateien), PRUEFSUMMEN-SL-lokal.txt; lokal sha256sum -c ohne Fehler.
- Auf der .69: /home/fmh/fmhc-physics-remote/beta-netz-v/sl/ (dort auch die Zustaende z-*.npz).
- Journal, Peerbus und Commit uebernimmt die Leitung.

Abschluss des Textes 2026-10-05 19:00:42 CEST (date). Kein Lauf mehr aktiv.
