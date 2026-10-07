# QUANT-1: Ergebnis (Rechen-Agent fuer die Leitung claude-primary, Runde 50, ohne Einfrieren und ohne frischen Leser)

- **Ablauf (Zeiten per date; die .69 schreibt UTC, CEST = UTC + 2):**
  - Start 2026-10-05 17:58:08 CEST. Karte gelesen, Vorhandenes gelesen (SCHWERE-MASSE-V: Papier-I-Potential, Netz V).
  - Code q1.py Version 1 hochgeladen 18:10; Rauchlauf, Netzaufbau, freie Theorie und klassische Familie 18:10:25 bis
    18:12:56 CEST.
  - VORAB.md (Einschleifen-Erwartung) geschrieben ab 18:12:39 CEST, vor der ersten Produktions-Ergebnisdatei.
  - 18:16: Fehler in Version 1 gefunden (feste Trajektorienlaenge, Abschnitt 6.2); Laeufe gestoppt, Version 2 ab
    18:17:13 CEST. Alle Zahlen in den Tabellen stammen aus Version 2.
  - 18:24: Spur cpu6 umgeplant (Kopplungsscan auf L = 4 statt L = 6 und zweiter L = 8-Replik), weil die Fehler auf
    kleinen Verschiebungen groesser sind als erwartet (Abschnitt 6.4).
  - Methodenhinweise von ag-phy-lat (ueber die Leitung, waehrend der Laeufe) in Abschnitt 7 beruecksichtigt; deshalb
    18:53 die freie Kontrolle auf L = 4 nachgereicht.
  - Letzter Produktionslauf fertig 19:11:43 CEST, letzte Auswertung 19:11:51 CEST.
- 14 Produktionslaeufe (Version 2), 2 verworfene Laeufe (Version 1), 1 Rauchlauf, 9 Hilfslaeufe (Netz, freie Theorie,
  klassische Familie, Hartree) und 13 Auswertungsaufrufe, alle ueber kleintest.sh auf der .69, nur Spuren cpu5 und
  cpu6. Synthetische Gitterrechnung (numpy/scipy, 1 Thread), keine Messdaten.
- **Kennzeichen:** [E] gerechnet, [M] eigene Mathematik (nicht gegengelesen), [P] Projektdatei, [L] Literatur aus dem
  Gedaechtnis, nicht geprueft, [H] Hypothese, [F] Festlegung.
- **Einheiten:** Gittereinheiten a = 1 (kubisch) bzw. l_P = 1 (Netz V), hbar = 1, Zeitschritt dt = 1, T = 32
  Zeitschritte (lam = 30: T = 16). Massenparameter m = 0,5, also Gitterabstand h = m a = 0,5 in Q-Ball-Laengen.
  Kopplung lam = zeta (Bezeichnung von ag-phy-lat), g6 = lam^2/(2 m^2) (Papier-I-Form, beta = 1/2).

## 1. Ergebnis zuerst

1. **Keine gebundenen Zustaende aus 2 bis 5 Quanten** [E]. Bei schwacher Kopplung (lam = 0,1 und 0,25) ist
   E(Q) - Q m_1 nicht von der freien Kontrolle zu unterscheiden. Beispiel L = 4: Bindung je Teilchen b_2 =
   0,0010 +- 0,0007 (lam = 0,25) gegen 0,0007 +- 0,0010 (frei). Die erwartete Kastenverschiebung (Hartree erster
   Ordnung, L = 4: dE_2 = -0,004, also b_2 = +0,002) ist mit der Messung (0,0003 +- 0,0012 ueber der Kontrolle) ebenso
   vertraeglich wie null.
2. **Ab lam = 1 stossen sich die Quanten ab** [E]. L = 4, lam = 1, minus freie Kontrolle: E(2) - 2 m_1 = +0,016
   +- 0,003, E(3) - 3 m_1 = +0,051 +- 0,011, E(4) - 4 m_1 = +0,115 +- 0,029 (je 4 bis 5 Standardfehler). Das waechst
   etwa mit der Zahl der Paare Q(Q-1)/2 und betraegt die Haelfte bis zwei Drittel der Hartree-Erwartung erster
   Ordnung. Ursache [M]: Der stabilisierende Sextik-Term (g6 = lam^2/(2 m^2)) gibt ueber die Quantenschwankungen eine
   abstossende Paarkraft 9 g6 G0, die ab lam etwa 0,38 die Anziehung lam ueberwiegt (VORAB.md).
3. **Einteilchenmasse** [E]: frei 0,4938 +- 0,0022 (exakt 0,4949); lam = 0,1: 0,440 (-12 % gegen m); lam = 0,25:
   0,384 bis 0,387 kubisch (-22 bis -23 %), 0,425 auf V (-15 %); lam = 1: 0,59; lam = 3: 1,29; lam = 10: 2,23 (L = 4 und 8
   gleich); lam = 30: hoechstens 3,05. Kubisch trifft die selbstkonsistente Hartree-Masse bei lam = 0,25 auf 0,3 %.
4. **Klassischer Q-Ball** [M, E]: Quantenzahl N = Q_QB/lam. Einen klassischen Q-Ball mit N Quanten gibt es erst ab
   lam N >= 112, gebunden ab lam N >= 141,5. Fuer N <= 5 gibt es bis lam = 22 keinen klassischen Vergleich. Bei
   lam = 30 (E_cl(4)/4 = 0,506, E_cl(5)/5 = 0,498 in Gittereinheiten) wiegt ein einzelnes Quant nach Messung
   (Obergrenze 3,05) und Hartree (3,32) etwa sechsmal so viel wie m; E(4) und E(5) sind dort nicht messbar.
5. **Lesart [H]:** In diesem Modell ist ein Q-Ball kein Zweier oder Dreier, sondern ein Vielteilchen-Zustand aus
   mindestens 112/lam Quanten, bei schwacher Kopplung also aus Hunderten. Kleine Ladungen bilden ein Gas fast freier,
   ab lam = 1 sich abstossender Quanten.
6. **Netz V** [E]: laeuft technisch wie das kubische Gitter (freie Kontrolle: <|phi|^2> = 0,190783 +- 0,000062 gegen
   exakt 0,190785; m_1 = 0,4965 +- 0,0073). Bei lam = 0,25 ist m_1 auf V 0,425 statt 0,387; die Hartree-Naeherung
   mit gemitteltem Tadpole liegt auf V dort 12 % unter der Messung (kubisch 0,3 %). Paarverschiebungen auf V sind bei
   2 300 bis 4 000 Trajektorien mit null vertraeglich.

## 2. Tabellen

### Tabelle 1: Kopplung, m_1, E(Q), Bindung je Teilchen, E_cl(Q) [E]

- m_1: Plateau der cosh-Masse (tau >= 2); * = nur tau = 1, kein Plateau (Obergrenze).
- E(Q): log-effektive Energie des Produktkorrelators zwischen tau = 0 und 1. Das ist eine Obergrenze der
  Grundzustandsenergie; fuer lam <= 1 stimmen die Plateauwerte (Tabelle 2) innerhalb der Fehler.
- Bindung je Teilchen b_Q = -(E(Q) - Q m_1)/Q aus dem Verhaeltnis C_Q / C_1^Q zwischen tau = 0 und 1; positiv heisst
  gebunden. Die Zeilen "frei" zeigen das Nullniveau dieses Schaetzers.
- Fehler in Klammern auf die letzten Stellen; Jackknife mit Bins zu 32 Trajektorien.
- E_cl(Q): klassische Q-Ball-Energie E_cl(N) = (m/lam) E_QB(lam N) in Gittereinheiten (Abschnitt 5). "keiner (N_min)":
  Fuer N <= 5 gibt es keinen klassischen Q-Ball; der kleinste haette N_min = 112/lam Quanten.

| Gitter | lam | Traj. | m_1 | E(2) | E(3) | E(4) | E(5) | b_2 | b_3 | b_4 | b_5 | E_cl(Q) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| kub. L=8 | 0 (frei) | 5 095 | 0,4901(54) | 0,9874(79) | 1,465(22) | 1,906(60) | 2,29(15) | 0,0026(26) | 0,0079(65) | 0,020(15) | 0,039(30) | - |
| kub. L=4 | 0 (frei) | 49 905 | 0,4938(22) | 0,9881(33) | 1,4770(76) | 1,961(17) | 2,452(36) | 0,0007(10) | 0,0024(22) | 0,0045(40) | 0,0045(71) | - |
| V L=4 | 0 (frei) | 3 609 | 0,4965(73) | 1,008(11) | 1,506(24) | 1,991(56) | 2,46(12) | 0,0002(32) | 0,0025(68) | 0,007(13) | 0,012(24) | - |
| kub. L=4 | 0,1 | 35 504 | 0,4399(19) | 0,8791(30) | 1,3083(68) | 1,726(16) | 2,130(36) | 0,0015(9) | 0,0049(20) | 0,0096(38) | 0,0150(72) | keiner (1 120) |
| kub. L=4 | 0,25 | 68 525 | 0,3838(14) | 0,7620(22) | 1,1385(52) | 1,506(13) | 1,857(32) | 0,0010(7) | 0,0025(15) | 0,0055(31) | 0,0106(64) | keiner (448) |
| kub. L=8 | 0,25 | 9 695 | 0,3873(32) | 0,7694(48) | 1,150(12) | 1,517(31) | 1,843(87) | 0,0003(14) | 0,0019(34) | 0,0059(77) | 0,016(17) | keiner (448) |
| V L=4 | 0,25 | 3 980 | 0,4247(60) | 0,8442(79) | 1,268(18) | 1,711(40) | 2,188(83) | 0,0037(24) | 0,0031(50) | -0,0019(89) | -0,012(16) | keiner (448) |
| kub. L=4 | 1 | 37 470 | 0,5860(31) | 1,1986(44) | 1,820(10) | 2,465(25) | 3,150(64) | -0,0072(14) | -0,0145(30) | -0,0241(61) | -0,038(13) | keiner (112) |
| kub. L=8 | 1 | 7 704 | 0,5923(56) | 1,1760(74) | 1,790(20) | 2,428(53) | 3,04(13) | -0,0051(26) | -0,0136(61) | -0,024(13) | -0,024(26) | keiner (112) |
| V L=4 | 1 | 2 294 | 0,768(25) | 1,559(30) | 2,350(77) | 3,19(25) | 4,0(6) | -0,0058(93) | -0,009(23) | -0,02(6) | -0,02(13) | keiner (112) |
| kub. L=4 | 3 | 22 047 | 1,286(18) (nur tau=2) | 2,556(17) | 3,814(65) | 5,04(23) | 6,5(1,0) | -0,0043(71) | 0,002(21) | 0,01(6) | -0,02(20) | keiner (38) |
| kub. L=4 | 10 | 9 058 | 2,229(15)* | 4,50(12) | 6,2(7) | - | - | -0,02(6) | 0,16(25) | - | - | keiner (12) |
| kub. L=8 | 10 | 2 419 | 2,228(29)* | 4,50(26) | 6,5(2,1) | - | - | -0,02(12) | 0,06(70) | - | - | keiner (12) |
| kub. L=6, T=16 | 30 | 11 697 | 3,047(44)* | 5,6(6) | - | 6,9(1,8) | 7,5(3,2) | nicht deutbar | - | nicht deutbar | nicht deutbar | E_cl(4) = 2,025; E_cl(5) = 2,488 |

### Tabelle 2: Plateauwerte, Hartree-Vergleich und HMC-Kontrollen [E, M]

- m_1 Hartree: selbstkonsistent, M^2 = m^2 - 4 lam G(M^2) + 18 g6 G(M^2)^2, E = 2 asinh(M/2) (q1a.py hartree, je
  Gitter und T). lam = 0,1: nur Einschleife (L = 8). dE_2 Hartree: Kastenverschiebung erster Ordnung
  -lam_eff Q(Q-1)/(4 M^2 Vol) mit lam_eff = lam - 9 g6 G (fuer lam >= 1 nur als Richtung brauchbar).
- Plateau E(2), dE_2: tau ab 1, solange der Fehler unter 0,06 bleibt; "-" = kein Plateau nach dieser Regel.

| Gitter | lam | m_1 Hartree | E(2) Plateau | dE_2 Plateau | dE_2 Hartree 1. Ordn. | Akzeptanz | <exp(-dH)> | tau_int max |
|---|---|---|---|---|---|---|---|---|
| kub. L=8 | 0 | 0,4949 (exakt) | 0,970(18) | -0,009(14) | 0 | 0,901 | 1,0016(69) | 1,73 |
| kub. L=4 | 0 | 0,4949 (exakt) | 0,9889(75) | +0,0004(57) | 0 | 0,738 | 0,9967(67) | 1,99 |
| V L=4 | 0 | 0,4949 (exakt) | 1,000(22) | -0,005(19) | 0 | 0,778 | 1,002(24) | 2,39 |
| kub. L=4 | 0,1 | 0,443 (Einschl., L=8) | 0,8803(62) | -0,0019(45) | etwa -0,003 (von Hand) | 0,874 | 0,9995(28) | 1,32 |
| kub. L=4 | 0,25 | 0,3826 | 0,7595(41) | -0,0074(29) | -0,0038 | 0,732 | 1,0003(57) | 1,81 |
| kub. L=8 | 0,25 | 0,3861 | 0,785(10) | +0,0049(68) | -0,0005 | 0,899 | 0,9981(44) | 1,54 |
| V L=4 | 0,25 | 0,3727 | 0,835(15) | -0,015(10) | -0,0003 | 0,829 | 0,989(13) | 1,44 |
| kub. L=4 | 1 | 0,6358 | 1,182(11) | +0,0093(94) | +0,030 | 0,768 | 1,0031(73) | 1,80 |
| kub. L=8 | 1 | 0,6238 | 1,195(20) | +0,019(17) | +0,0037 | 0,920 | 1,0023(45) | 1,71 |
| V L=4 | 1 | 0,8007 | - | - | +0,0045 | 0,806 | 0,993(25) | 2,10 |
| kub. L=4 | 3 | 1,4531 | - | - | +0,043 | 0,856 | 0,9995(48) | 1,64 |
| kub. L=4 | 10 | 2,4657 | - | - | +0,074 | 0,948 | 1,0006(22) | 1,14 |
| kub. L=8 | 10 | 2,4657 | - | - | +0,0093 | 0,928 | 1,0001(58) | 1,25 |
| kub. L=6, T=16 | 30 | 3,3188 | - | - | +0,041 | 0,789 | 1,0035(97) | 1,45 |

## 3. Abgleich mit Q1 bis Q3 (beschreibend)

- **Q1 (80 %, Einteilchenmasse bei schwacher Kopplung auf 20 % am Massenparameter):** teils getroffen.
  - lam = 0,1: m_1 = 0,440, also 12 % unter m = 0,5 (innerhalb von 20 %).
  - lam = 0,25: 22 bis 23 % unter m auf dem kubischen Gitter (L = 4 und 8), 15 % auf V. Kubisch knapp ausserhalb.
  - Die Verschiebung ist der Gitter-Tadpole (-4 lam G0 mit G0 ~ 1/a^2), also ein Abschneide-Effekt; die
    selbstkonsistente Hartree-Masse beschreibt sie kubisch auf 0,3 %. Im Kontinuum waere sie Massenrenormierung.
- **Q2 (55 %, gebundene Zustaende fuer Q = 2 und 3, Bindung je Teilchen waechst mit Q):** nicht getroffen.
  - Bei lam = 0,1 und 0,25 ist b_Q nicht von der freien Kontrolle unterscheidbar (L = 4: b_2 = 0,0015(9) bzw.
    0,0010(7) gegen 0,0007(10); b_3 = 0,0049(20) bzw. 0,0025(15) gegen 0,0024(22)).
  - Der Plateauwert dE_2 = -0,0074 +- 0,0029 (lam = 0,25, L = 4) saehe allein wie 2,5 sigma Anziehung aus; gegen die
    freie Kontrolle (+0,0004 +- 0,0057) bleiben 1,2 sigma. Auf L = 8 ist er +0,0049 +- 0,0068.
  - Ab lam = 1 kehrt sich das Vorzeichen um: Abstossung, je Teilchen mit Q wachsend (b_2 bis b_5 = -0,007 bis
    -0,038 auf L = 4).
  - Selbst eine schwache Anziehung haette im Kasten E(Q) < Q m_1 mit wachsender Bindung je Teilchen gegeben; das folgt
    aus dem Aufbau (erste Ordnung, Q(Q-1)/Vol) und waere kein Bindungszustand (Abschnitt 4).
- **Q3 (40 %, E(Q) fuer das groesste erreichbare Q auf 10 % an der klassischen Energie):** nicht pruefbar.
  - Fuer Q <= 5 gibt es klassische Q-Baelle erst ab lam >= 22,4; bei allen Kopplungen bis 10 fehlt der Vergleichswert.
  - Bei lam = 30 waere E_cl(4) = 2,025 und E_cl(5) = 2,488. Gemessen ist nur m_1 <= 3,05 (Obergrenze aus tau = 0
    bis 1; Hartree 3,32); vermutlich wiegt also schon ein Quant mehr als E_cl(4). Der Produktkorrelator fuer Q = 4 faellt von tau = 0 auf 1 um exp(-6,9 +- 1,8): weder wie vier freie
    Quanten (exp(-12,2), 3 sigma) noch wie ein Zustand bei E_cl(4) (exp(-2,0), 2,7 sigma). Bei schweren
    Verteilungsraendern ist das nicht deutbar (offener Punkt, Abschnitt 8).

## 4. Was aus dem Aufbau folgt und was echt gerechnet ist

- **Vorab ableitbar, ohne Simulation [M]:**
  - Freie Theorie: m_1 = 2 asinh(m/2) = 0,49493 auf dem kubischen Gitter und auf V (Lap 1 = 0, der s0-gewichtete
    Nullimpuls-Operator ist exakt Eigenmode), dazu dE_Q = 0 (Wick). Die freien Laeufe pruefen nur den Code.
  - N = Q_QB/lam und E_cl(N) = (m/lam) E_QB(lam N): Klassische Vergleichswerte gibt es erst ab lam N >= 112. Dass Q3
    fuer N <= 5 bei lam <= 22 nicht pruefbar ist, stand vor der Rechnung fest.
  - Kastenverschiebung erster Ordnung, dE_Q = -lam_eff Q(Q-1)/(4 m^2 Vol): Jede schwache Nettoanziehung gibt im Kasten
    E(Q) < Q m_1 mit wachsender Bindung je Teilchen. Der zweite Teil von Q2 waere bei Anziehung automatisch erfuellt.
  - Einschleife (VORAB.md): lam_eff = lam - 9 g6 G0 = lam - 2,62 lam^2 (kubisch). Anziehung nur bis lam = 0,38,
    hoechstens 0,095; ein gebundener Zweier braucht nichtrelativistisch etwa 8 m = 4 (Watson-Integral, grob). Keine
    Bindung war also die Vorab-Erwartung, die Abstossung ab etwa lam = 0,4 ebenfalls.
  - Hartree-Massen (q1a.py hartree): kubisch L = 8 fertig 18:33:21, L = 4 18:41:17 CEST, also vor dem Lesen der
    kubischen wechselwirkenden Ergebnisse (18:45:49 bzw. 18:50); fuer V (18:49:06) erst nach dem V-Ergebnis (18:34).
- **Echt gerechnet [E]:**
  - die Massen bei Wechselwirkung und wie gut Hartree sie trifft: kubisch 0,3 % (lam = 0,25); Hartree 5 bis 9 % zu
    hoch (lam = 1), 13 % (lam = 3), 11 % (lam = 10), mindestens 9 % (lam = 30); auf V 12 % zu tief (lam = 0,25) bzw.
    4 % zu hoch (lam = 1).
  - dass die schwache Anziehung bei lam <= 0,25 unter der Messgrenze bleibt (|dE_2| unter etwa 0,005 auf L = 4).
  - die Abstossung bei lam = 1 mit 4 bis 5 sigma gegen die freie Kontrolle, ihr Wachstum mit der Paarzahl und ihre
    Groesse (die Haelfte bis zwei Drittel von Hartree erster Ordnung).
  - die Grenzen der Methode: Rauschen, Plateaus und die Starkkopplungsgrenze (Abschnitt 6.4).
- **Nicht gezeigt:** Ob die Abstossung auf L = 8 wie 1/Vol kleiner wird. L = 8, lam = 1 gibt dE_2 = +0,010 +- 0,005
  roh (L = 4: +0,0145 +- 0,0028); die 1/Vol-Erwartung waere +0,002 (1,6 sigma Abstand). Werte zwischen tau = 0 und 1
  koennen kurzzeitige Anteile enthalten, die nicht wie 1/Vol fallen.

## 5. Umrechnung zwischen Gitter und klassischem Q-Ball [M]

- Gitterwirkung (euklidisch, periodisch in allen Richtungen):
  S = sum_t [ (1/dt) sum_v s0 |phi_v(t+1) - phi_v(t)|^2 + dt sum_e s1 |(D phi)_e|^2 + dt sum_v s0 U_g(|phi_v|^2) ],
  U_g(S) = m^2 S - lam S^2 + g6 S^3, g6 = lam^2 / (2 m^2).
  - Kubisch: s0 = 1, s1 = 1. Netz V: s0 = *0, s1 = *1 (Sterne an der Kammermitte wie SCHWERE-MASSE-V), Laengen in l_P.
- Mit phi = (m / sqrt(lam)) psi und x = y / m wird daraus S = (1/lam) S_QB[psi], mit dem Potential aus Papier I,
  U(s) = s - s^2 + s^3/2, in Q-Ball-Einheiten.
  - lam steht also genau an der Stelle von hbar. Das klassische Modell legt lam nicht fest; die Quantentheorie hat genau
    diese eine Kopplung (dazu h = m a als Gitterabstand).
  - Das ist dieselbe Normierung wie zeta im Entwurf von ag-phy-lat (S/hbar = I/zeta, lambda_4 = zeta,
    lambda_6 = zeta^2/2 in d = 3).
- Ladung: Ganzzahlige Quantenladung N (Zahl der Quanten) und klassische Ladung Q_QB = 2 om Integral f^2 d^3y haengen
  ueber N = Q_QB / lam zusammen.
- Energie: E_Gitter = (m / lam) E_QB. Klassische Vorhersage fuer N Quanten: E_cl(N) = (m / lam) E_QB(Q_QB = lam N),
  also E_cl(N) / (N m) = E_QB / Q_QB. Nicht E_QB(N).
- Klassische Familie (q1.py klass, Kontinuum, Schiessverfahren wie sm.qball_kont) [E]:
  - Kontrolle gegen SCHWERE-MASSE-V: om = 0,8 / 0,9 / 0,95 gibt Q = 1 172,34 / 174,04 / 115,01 und
    E = 997,91 / 171,08 / 116,80, wie dort.
  - Kleinste Ladung Q_min = 111,96 bei om = 0,965 (om-Raster 0,005), dort E/Q = 1,0172: nicht gebunden.
  - Gebunden (E < m Q) erst ab Q_QB = 141,5 (om etwa 0,92).
  - Fuer Q_QB > Q_min nehme ich den Ast mit kleinerem om (dQ/dom < 0), also die tiefere Energie.
- Folge [M]: Einen klassischen Q-Ball mit N Quanten gibt es erst ab lam N >= 112, gebunden erst ab lam N >= 141,5.
  - N = 5 / 4 / 3 / 2: lam >= 22,4 / 28,0 / 37,3 / 56,0 (Existenz) bzw. 28,3 / 35,4 / 47,2 / 70,8 (Bindung).
  - Bei lam = 0,25 / 1 / 3 / 10 haette der kleinste klassische Q-Ball 448 / 112 / 38 / 12 Quanten.
  - Die semiklassische Naeherung braucht lam << 1, dann ist N = Q_QB / lam >> 100. Q-Baelle aus 2 oder 3 Quanten
    liegen deshalb immer tief im Quantenbereich.

## 6. Methode und Kontrollen

### 6.1 Aufbau [E]

- HMC mit Omelyan-2MN-Integrator (lambda = 0,19318), Massen s0/dt je Ecke, Metropolis-Test auf exp(-dH).
  Schrittweite in 500 Thermalisierungs-Trajektorien auf Akzeptanz 0,75 bis 0,93 geregelt, danach fest.
- Mittlere Trajektorienlaenge tau = 2; Version 2 zieht die Schrittzahl je Trajektorie gleichverteilt aus [n/2, 3n/2].
- Messung nach jeder Trajektorie: O_1(t) = sum_v s0 phi_v(t); lokal O_Q = sum_v s0 phi_v^Q; Produkt
  P_Q = O_1^Q / Vol^(Q-1); Korrelatoren C(tau) = (1/T) sum_t Re <O(t+tau)^* O(t)> fuer Q = 1 bis 5 (Q >= 2: 2x2-Matrix
  lokal/Produkt). Gespeichert sind nur die Korrelatoren (float32) und die Endkonfiguration.
- Auswertung (q1a.py): Bins zu 32 Trajektorien (Fehler gegen Binbreite 4 bis 512 flach, Abschnitt 6.3), Jackknife.
  - m_1: cosh-effektive Masse von C_1, Plateau ab tau = 2.
  - E(Q): log-effektive Energie des Produktkorrelators, Plateau ab tau = 1.
  - dE_Q = E(Q) - Q m_1 aus dem Verhaeltnis C_Q / C_1^Q (log-Massen beider Seiten). So heben sich die Rueckwaerts- und
    Waermeanteile der periodischen Zeitachse in der freien Theorie exakt weg (Wick: C_Q^pp = Q! C_1^Q / Vol^(2(Q-1))).
  - Plateau-Regel [F, nach Sicht der freien Kontrolle gewaehlt]: gewichtetes Mittel ueber die zusammenhaengenden tau
    ab dem Startwert, solange der Jackknife-Fehler unter 0,03 (m_1) bzw. 0,06 (E, dE) liegt.
  - Zusaetzlich 2x2-GEVP (t0 = 1) aus lokalem und Produktoperator. Wo es ein Plateau gibt (lam <= 1), stimmt der
    GEVP-Grundzustand mit dem Produktoperator ueberein (z. B. E(2) = 0,7595 beide bei lam = 0,25, L = 4); der lokale
    Operator allein ist bis tau = 1 bis 2 von angeregten Zustaenden belastet.
- Netz V (L = 4 Zellen): 640 Ecken, 4 352 Kanten, Vol = 362,04 l_P^3, s0 von 0,0557 bis 1,170 l_P^3, s1 von 0,0866 bis
  0,771 l_P. Laplace mal konstant <= 4,2e-15. Groesster Eigenwert von s0^-1/2 Lap s0^-1/2: 20,70 (kubisch 12).
  Sterne aus sm.stern_daten (SCHWERE-MASSE-V, sha256 62cefc60..., unveraendert).

### 6.2 Was nicht geklappt hat: Version 1 mit fester Trajektorienlaenge [E]

- Der erste freie Kontrolllauf (k8-l0, Version 1, 5 868 Trajektorien) gab <|phi|^2> = 0,143777 +- 0,000058.
  Exakt ist 0,145552 (q1.py frei). Das sind 1,22 % oder 30 Standardfehler zu wenig.
- Ursache [M, Lehrbuchwissen L]: Bei fester Trajektorienlaenge tau kehrt eine freie Mode mit omega tau nahe k pi auf
  denselben Betrag zurueck. Solche Moden thermalisieren nicht aus dem kalten Start.
- Abhilfe: Schrittzahl je Trajektorie zufaellig (Version 2). Der freie Lauf k8-l0-v2 (5 095 Trajektorien) gibt
  0,145476 +- 0,000036 (-0,05 %, 2,1 Standardfehler).
- Gestoppt bzw. verworfen: k8-l0 (Version 1, nur als Beleg ausgewertet) und v4-l0.25 (Version 1, nach etwa 3 min
  gestoppt, nicht ausgewertet).

### 6.3 Kontrollen [E]

- **Freie Theorie, kubisch L = 8, T = 32 (k8-l0-v2), gegen die exakte Rechnung (q1.py frei):**
  - m_1 = 0,4901 +- 0,0054; exakt 2 asinh(m/2) = 0,49493 (Gitterdispersion, 1 % unter m).
  - C_1(tau) MC/exakt fuer tau = 0 bis 4: 0,993(5), 0,992(7), 0,996(11), 1,006(16), 1,012(26).
  - Wick-Test C_Q^pp / (Q! C_1^Q / Vol^(2(Q-1))) bei tau = 0 / 1: Q = 2: 1,005(3) / 1,010(7); Q = 3: 1,017(11) /
    1,041(26); Q = 4: 1,039(26) / 1,124(77); Q = 5: 1,076(56) / 1,305(206). Bis Q = 3 sauber, bei Q = 4 und 5 zeigen
    die schweren Raender der Verteilung eine leichte Unterschaetzung der Fehler.
  - Plateau dE_2 = -0,009 +- 0,014 und dE_3 = +0,019 +- 0,050: vertraeglich mit exakt 0.
- **Freie Theorie, kubisch L = 4, T = 32 (k4-l0-v2, 49 905 Trajektorien):** <|phi|^2> = 0,150904 +- 0,000044 gegen
  exakt 0,150962; m_1 = 0,4938 +- 0,0022; C_1 MC/exakt bei tau = 0 bis 4: 0,997(2), 0,997(3), 0,998(4), 0,998(7),
  0,994(11); Wick-Test bei tau = 0 / 1: Q = 2: 0,998(1) / 1,000(3), Q = 3: 0,994(4) / 1,002(9), Q = 4: 0,988(9) /
  1,005(21), Q = 5: 0,977(15) / 0,999(42).
  - Nullniveau des Bindungsschaetzers (tau = 0 bis 1): b_2 bis b_5 = 0,0007(10), 0,0024(22), 0,0045(40), 0,0045(71),
    alle mit 0 vertraeglich, aber leicht positiv. Gegen dieses Niveau sind die schwachen Kopplungen gelesen.
- **Freie Theorie auf V (v4-l0-v2, 3 609 Trajektorien):** <|phi|^2> = 0,190783 +- 0,000062 gegen exakt 0,190785;
  m_1 = 0,4965 +- 0,0073; C_1 MC/exakt bei tau = 0 bis 4: 1,002(7), 0,992(10), 0,986(14), 0,972(22), 0,904(37) (bei
  tau = 4 2,6 sigma tief, wenig Statistik); Wick-Test Q = 2 bis 5 bei tau = 0: 1,001(5), 1,004(13), 1,005(26),
  1,002(43).
- **Akzeptanz und HMC-Identitaet <exp(-dH)> = 1:** Tabelle 2. Akzeptanz 0,73 bis 0,95; <exp(-dH)> in allen 14
  Laeufen innerhalb von 1 Standardfehler bei 1.
- **Reversibilitaet** (je Lauf drei Hin-und-Rueck-Trajektorien nach der Thermalisierung): |delta phi| <= 1,8e-14,
  |delta H| <= 7,3e-12.
- **Autokorrelation** (Wolff-Fenster): tau_int = 0,7 bis 2,4 Trajektorien fuer |phi|^2, C_1(0, 2, 4), C_2(1); Fehler
  gegen Binbreite ab B = 4 flach (L = 4, lam = 0,25: Fehler von m_1 bei tau = 4 0,0046 bis 0,0050 fuer B = 32 bis
  512). Gewaehlt B = 32.
- **Freie Theorie auf V [M]:** Weil Lap 1 = 0, ist A_k s0 = (c_k + m^2) s0. Der s0-gewichtete Nullimpuls-Korrelator
  ist auf V deshalb exakt derselbe wie auf dem kubischen Gitter (m_1 = 0,49493). Das ist eine Folge des Aufbaus, kein
  Befund.

### 6.4 Genauigkeitsgrenze [E, M]

- Der Nullimpuls-Operator O_1 ist in jeder Konfiguration nur eine einzige Mode. Sein Rauschen faellt nicht mit dem
  Volumen, das Signal faellt wie exp(-m_1 tau). Bei 5 000 bis 10 000 Trajektorien auf L = 8 ist der Fehler auf dE_2
  deshalb etwa 0,003 bis 0,005 (tau = 0 bis 1) bzw. 0,007 bis 0,017 (Plateau); die erwarteten Kastenverschiebungen
  bei schwacher Kopplung sind 5e-4 (L = 8) bzw. 4e-3 (L = 4).
- Auf L = 4 kosten Trajektorien ein Achtel; mit 68 525 Trajektorien erreicht dE_2 dort +-0,003.
- Bei starker Kopplung (m_1 >= 1,3) faellt das Signal schon von tau = 0 auf 1 um den Faktor 3,6 (Q = 1) bzw. 13
  (Q = 2); dort gibt es nur Werte aus tau = 0 bis 1 ohne Plateau (in der Tabelle mit * markiert). Effektive Massen aus
  tau = 0 bis 1 sind Obergrenzen der Grundzustandsenergie (positive Spektralsumme), keine Messwerte des Plateaus.

## 7. Methodenhinweise von ag-phy-lat (Entwurf model-lab/papers/qball-quantization-20261005-en-codex/) [P]

1. **Wirkungsnormierung zeta:** Hier ist zeta = lam (Abschnitt 5). Gewaehlt und dokumentiert: lam = 0 (frei), 0,1,
   0,25, 1, 3, 10, 30. "Schwach" ist nur lam <= 0,25: Dort liegt die gemessene Einteilchenmasse innerhalb von 1 % an
   der selbstkonsistenten Hartree-Masse (kubisch), und m_1 liegt 12 bis 23 % unter m. Ab lam = 1 ist die Theorie auf
   dem Gitter stark gekoppelt (m_1/m = 1,2 bei lam = 1 bis etwa 6 bei lam = 30), und die klassische Umrechnung mit dem
   nackten m verliert ihren Sinn. Die klassische Energie ist E_cl(zeta n)/zeta, nicht E_cl(n); so ist sie hier auch
   gerechnet.
2. **Freie Gauss-Kontrolle:** mitgerechnet (Abschnitt 6.3). C_Q^pp = Q! C_1^Q ist auf der periodischen Zeitachse
   eine Potenz des cosh-Propagators; deshalb nehme ich dE_Q aus dem Verhaeltnis C_Q / C_1^Q mit log-Massen auf beiden
   Seiten, nicht aus E(Q) - Q m_1(cosh). Wick-Test, Plateau, Autokorrelation und Binbreite sind geprueft. Die freie
   Kontrolle (L = 4 und 8, V) zeigt kein signifikantes Scheinsignal, aber ein leicht positives Nullniveau des
   Bindungsschaetzers (b_2 = 0,0007 +- 0,0010 auf L = 4). Ohne diese Kontrolle haette ich den Plateauwert
   dE_2 = -0,0074 +- 0,0029 bei lam = 0,25 als 2,5-sigma-Anziehung gelesen; gegen die Kontrolle sind es 1,2 sigma.
3. **Stationaerer Ast ist nicht automatisch Grundzustand:** Bei Q_QB < 141,5 liegt der klassische Q-Ball ueber
   N m, ist also hoechstens metastabil gegen N einzelne Quanten. E_cl ist deshalb nur fuer lam N > 141,5 eine
   Grundzustandsvorhersage (und auch dort erst in fuehrender Ordnung in lam).
- Kein Doppellauf: ag-phy-lat rechnet keine Massen; das Spektrum hier ist das einzige.

## 8. Grenzen, Regelabweichungen, Selbstanzeigen

1. **Ohne Einfrieren und ohne frischen Leser** (Finn, 05.10.). Die Plateau-Regel habe ich nach Sicht der freien
   Kontrolle festgelegt [F], vor dem Lesen der wechselwirkenden Ergebnisse. VORAB.md (18:12:39 CEST) enthaelt die
   Einschleifen-Erwartung; die Hartree-Rechnung (q1a.py hartree) wurde 18:26:42 CEST eingereiht, nach den ersten
   Rohlaeufen; zeitliche Reihenfolge zum Lesen der Ergebnisse in Abschnitt 4.
2. **Version 1 war falsch** (Abschnitt 6.2). Die beiden Version-1-Laeufe sind nicht in den Tabellen. Ich habe dafuer
   zwei eigene Ketten gestoppt, eine eigene Unit (systemctl --user stop) und einen eigenen wartenden flock-Prozess
   auf der .69 beendet. Fremde Prozesse habe ich nicht beruehrt.
3. **Nur ein Gitterabstand (h = m a = 0,5), nur beta = 1/2, nur T = 32 (L = 6: T = 16).** Kontinuumsgrenze und
   Abhaengigkeit von beta sind offen. Die Kopplungsabhaengigkeit der Masse ist ueberwiegend ein Abschneide-Effekt
   (Tadpole mit G0 ~ 1/a^2), im Kontinuum waere sie eine Massenrenormierung.
4. **Kleine Kaesten:** Auf L = 4 ist m_1 L etwa 1,5 (lam = 0,25) bis 2,3 (lam = 1). Alle Verschiebungen dort sind
   Kastengroessen; der Volumenvergleich mit L = 8 ist nur auf etwa 2 Standardfehler scharf (Abschnitt 4, "Nicht
   gezeigt").
5. **Starke Kopplung (lam >= 3):** nur tau = 0 bis 1 nutzbar (Abschnitt 6.4); dort sind die Werte Obergrenzen.
6. **Q = 4 und 5:** Der Wick-Test zeigt bis 30 % Abweichung bei 1,5 Standardfehlern; die Fehler dort sind eher zu
   klein (schwere Verteilungsraender).
7. **Netz V:** nur L = 4 Zellen (640 Ecken), lam = 0, 0,25, 1, mit 2 300 bis 4 000 Trajektorien. Die
   Hartree-Naeherung mit einem gemittelten G passt auf V schlecht (Abschnitte 1 und 4); eine eckenabhaengige
   Hartree-Rechnung habe ich nicht gemacht.
8. **Werkzeuge lokal:** nur Shell-Bordmittel (cp, mv, mkdir, ls, ps, kill, diff, cat, wc, date, nohup), ssh, scp,
   grep, sed, sha256sum und jq (lesend). Kein python, awk oder perl lokal.
   Einmal lief ein lokaler Warte-Befehl ueber die 10-min-Grenze des Werkzeugs; das Werkzeug legte daraufhin seine
   eigene Ausgabedatei unter /tmp/claude-1000/... an. Das war keine Schreibhandlung von mir, ich nenne es trotzdem.
9. **Laufzeiten:** alle Rechnungen ueber kleintest.sh, nur Spuren cpu5 und cpu6, jeder Lauf <= 9 min 1,2 s, alle
   Rechnungen rc = 0 (Liste in lauf-69/ketten-fertig.txt). Zwei wartende Auswertungsaufrufe (aus-h, aus-i) habe ich
   abgebrochen (rc = 143), weil ich dieselbe Auswertung frueher auf der freien Spur cpu6 gestartet hatte. df vor
   jedem Lauf: 17 bis 18 GB frei. Platte der .69 fuer QUANT-1: 236 MB (keine Konfigurationsserien, nur Korrelatoren
   und je eine Endkonfiguration).
10. **Offener Punkt lam = 30, Q = 4** (Abschnitt 3, Q3): Der Produktkorrelator faellt langsamer als fuer vier freie
    Quanten erwartet (3 sigma), bei schweren Verteilungsraendern und ohne Plateau. Ein Folgelauf mit mehr Statistik und
    dem lokalen Operator (oder kleinerem lam N oberhalb von 112) waere noetig, bevor man daraus etwas liest.
11. **Plateauregel und tau = 0:** Tabelle 1 nutzt die Werte zwischen tau = 0 und 1, weil es bei starker Kopplung nur
    diese gibt. Fuer lam <= 1 stimmen sie mit den Plateaus (Tabelle 2) innerhalb der Fehler.
12. Journal, Peerbus und Commit uebernimmt die Leitung.

## 9. Einfach gesagt

Wir haben das Q-Ball-Feld zum ersten Mal quantenmechanisch auf dem Gitter simuliert und gemessen, ob zwei bis fuenf
Feldteilchen zusammen leichter sind als einzeln. Bei schwacher Kopplung merkt man von einer Anziehung nichts, und ab
mittlerer Kopplung stossen sich die Teilchen sogar ab, weil die Quantenzitterbewegung den abstossenden Teil des
Potentials verstaerkt. Ein klassischer Q-Ball ist in diesem Modell deshalb kein Paar oder Dreier, sondern ein Klumpen
aus mindestens etwa 112 geteilt durch die Kopplung Teilchen, bei schwacher Kopplung also aus Hunderten.

## 10. Dateien

- Lokal (dieser Ordner):
  - code/q1.py (Version 2, sha256 e1fdf3d0...): netz, frei, hmc, aus, klass.
  - code/q1-v1-feste-trajektorie.py (65cad6b7...): Version 1, nur als Beleg fuer Abschnitt 6.2.
  - code/q1a.py (6d4d270b...): Auswertung (aus, stapel), Hartree, sonst wie q1.py.
  - code/kette.sh (523e542e...): lokale ssh-Kette; code/tabelle.jq, code/zeile.jq: lokale Anzeige (jq, lesend).
  - code/sm.py, ew.py, mn.py, rv.py, tp.py, danzer_naeherung.py, licht_netz.py: unveraendert aus
    schwere-masse-v/code (sha256 wie dort, auf der .69 gleich).
  - VORAB.md (sha256 39ad07b4...): Einschleifen-Erwartung vor den Produktionslaeufen.
  - lauf-69/: Logs aller Laeufe und Auswertungen, ketten-fertig.txt, hartree.log.
  - aus-69/: 23 JSON: Auswertungen aller 14 Version-2-Laeufe (Effektivmassen je tau, Plateaus, tau_int,
    Binbreitenscan), k8-l0-v1 (Beleg Abschnitt 6.2), hartree-k8/k4/v4/k6t16, frei-k8/k6/v4, klassisch.
  - rauch-69/: Rauchlauf und Netzaufbau, dazu Kopien von frei-*.json und klassisch.json.
  - PRUEFSUMMEN-69.txt: sha256 von 68 Dateien, auf der .69 erzeugt (19:15 CEST). Die 23 JSON in aus-69/ und die
    Code-Dateien in code/ stimmen damit ueberein (sha256sum -c lokal).
- Auf der .69: /home/fmh/fmhc-physics-remote/quant-1/ (code/, netz/V-L4.npz, lauf/ mit den npz-Korrelatoren und
  Endkonfigurationen, aus/ mit allen JSON).

Abschluss des Textes 2026-10-05 19:17:39 CEST (date). Zeitrahmen etwa 120 min ab 17:58:08 CEST eingehalten. Kein Lauf mehr aktiv.
