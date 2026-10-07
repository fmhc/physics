# GUERTEL-1: Der Guerteltrick als Basis kleinster Bewegungen (720-Grad-Takt, "0 +1 0 -1 0", Kraftuebergang in vier Schritten) und grundsaetzlich (Runde 41)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 14:42:55 CEST (date), vor jeder
  Rechnung.
- **Auftrag von Finn (04.10., Nachricht zwischen 14:38 und 14:42, woertlich):** "teste die gürtel-1 sache durch als basis
  für kleinste bewegungen (sinus 0 +1 0 -1 0 like, 4-takt-motor mäßig, kraftübergang in 4 schritten) und auch
  grundsätzlich"
- **Zusammengelegt mit STRUKTUR-FEDERRING-1** (Finns Federring-Bild, Karte und Bild in RUNDE-37/struktur-federring-1/):
  Die Federring-Analyse (Mechanik, Rastung, freies Ueberdrehen) und der dort angehaengte Drehungs-Cluster gehoeren in
  diesen Auftrag, weil Federring, Guerteltrick und synchrone Drehung dieselbe Mathematik haben (Kopplung, ein Agent).
- **Herkunft:** Idee H3 GUERTEL-1 im Ideenpool ("angebundener Tetraeder-Knoten, 360 gegen 720 Grad, Entwirrungsenergie im
  Netz"; Testpfad "Seile mit Ausschlussvolumen, Energie des Entwirrungswegs"); STRATEGIE-SPIN-20261004.md Weg 2
  ("klassisch ableitbar; welches Vorzeichen die Quantenwelt waehlt, bleibt offen (FR)").
- **Projektbezug:** TWIST-SPIN-1 (Fadenend-Fermion spinlos: ein Zustand je Knoten erlaubt keine projektive Klasse; halber
  Spin braucht mindestens zwei Zustaende je Knoten); SCHACHBRETT-KAUSAL-1 (1+1-Schachbrett mit Faktor i je Umkehr,
  Zitterbewegung); QB-BS-2D; SPIN-HOPF-L.
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [S] an der Quelle gelesen, [ES] eigener Schluss, [H]
  Hypothese, [G] Rechnung.

## Schreibtisch der Leitung (vor der Karte) [M, L, ES; ungeprueft]

- Ein Spin-1/2-Zustand bekommt bei Drehung um theta den Faktor e^(-i theta/2). In 180-Grad-Schritten: 1, -i, -1, +i, 1.
  Der Imaginaerteil laeuft 0, -1, 0, +1, 0, also Finns "Sinus 0 +1 0 -1 0" (bis aufs Vorzeichen); die Periode sind 720
  Grad = vier Schritte [M].
- Viertaktmotor: Ein Arbeitsspiel dauert 720 Grad Kurbelwinkel, die Nockenwelle dreht mit halber Drehzahl. Die
  Nockenwelle ist damit ein mechanisches Bild der Zweifach-Ueberlagerung SU(2) -> SO(3) (Winkel halbiert) [ES].
- Feynman-Schachbrett: Faktor i je Richtungsumkehr; vier Umkehrungen geben i^4 = 1, also ebenfalls ein Viertakt [L].
- Guerteltrick: Die Drehungen bilden eine Gruppe mit einer Schleife, die sich nur doppelt durchlaufen zusammenziehen laesst
  (pi_1(SO(3)) = Z_2). Ein Koerper, der mit Faeden an seiner Umgebung haengt, laesst sich nach 360 Grad nicht entdrillen,
  nach 720 Grad schon [L Dirac].
- Grundsaetzlich [H]: Ein angebundener Rotor je Netzknoten haette einen Konfigurationsraum mit dieser Z_2-Schleife; die
  Paritaet der Verdrillung (verdrillt oder nicht) waere ein zweiter Zustand je Knoten, also genau das, was TWIST-SPIN-1
  vermisst. Welcher Sektor (ganz- oder halbzahlig) in der Quantenwelt gewaehlt wird, legt die Topologie allein nicht fest
  (Finkelstein-Rubinstein) [L].

## Auftrag (Code-Agent; Schreibtisch und Literatur zuerst)

1. **Schreibtisch und Literatur (hoechstens 6 gezielte Abrufe, keine Websuche):** den Schreibtisch oben pruefen und
   berichtigen; Guerteltrick bzw. Tellertrick und SU(2); Schachbrett-Faktor i und Spin 1/2 (Jacobson/Schulman u. a.);
   Finkelstein-Rubinstein; mechanische Spinor-Modelle; dazu die Federring-Fragen aus RUNDE-37/struktur-federring-1/
   KARTE.md (Mechanik, Rastung, Kinks, Synchronisation) knapp. Ergebnis in PLAN.md, bevor gerechnet wird.
2. **Rechnung (kleine Tests):** angebundener Rotor: starrer Koerper in der Mitte (Tetraeder, also ein Knoten von Finns
   Netz) mit vier Faeden in Tetraederrichtung zu festen Ankern auf einer aeusseren Kugel. Faeden als Perlenketten mit
   Dehn- und Biegeenergie und Ausschlussvolumen (Faeden duerfen sich nicht durchdringen, auch nicht den Koerper; ohne das
   wird jede Verdrillung trivial).
   - Protokoll: den Koerper um eine feste Achse in Schritten von 90 bzw. 180 Grad bis 720 Grad (und 1080, 1440 Grad)
     drehen, je Schritt relaxieren; danach je Endwinkel mit festgehaltenem Koerper frei relaxieren (Langevin mit Abkuehlen,
     mehrere Saaten) und die kleinste erreichbare Fadenenergie E_min(theta) bestimmen.
   - Kontrolle in der Ebene: Faeden auf eine Ebene gezwungen; dann darf sich keine Verdrillung aufheben (Windungszahl ganz).
   - Viertakt: Drehmoment auf den Koerper entlang des quasistatischen Wegs 0 bis 720 Grad mit Entwirrung; Zahl und Lage
     der Nulldurchgaenge.
   - Alles mit Plan, Rauchlauf und Einfrieren wie ueblich.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| GT0 | Kontrolle Ebene: E_min waechst mit abs(theta) bei jedem Vielfachen von 360 Grad, keine Rueckkehr auf E_min(0) | 85 % |
| GT1 | [H] Frei im Raum: E_min(720) liegt innerhalb von 10 % bei E_min(0), E_min(360) deutlich darueber (>= 3 SE ueber Saaten) | 50 % |
| GT2 | (ersetzt vor dem Start durch GT2a und GT2b, siehe Berichtigung unten; alter Wortlaut: "genau vier Nulldurchgaenge") | - |
| GT3 | [H] Die Sperre auf dem Entwirrungsweg bei 720 Grad ist endlich und kleiner als die Verdrillungsenergie bei 360 Grad | 40 % |

**Bedeutung (vorab):**
- **GT0 und GT1 treffen ein:** Das Netz-Bild traegt die Zweifach-Struktur des halben Spins mechanisch: ein angebundener
  Knoten unterscheidet 360 von 720 Grad. Das ist klassisch und topologisch erwartet; neu sind die Energien auf Finns
  Tetraeder-Knoten.
- **GT1 verfehlt (Abkuehlen findet den Entwirrungsweg nicht):** Der Trick ist im Prinzip moeglich, aber energetisch bzw.
  kinetisch gesperrt; dann zaehlt die Sperrhoehe (GT3).
- **GT2 trifft ein:** Finns Viertakt ist im Kraftverlauf sichtbar.
- **Grundsaetzlich:** Was folgt fuer halben Spin im Netz (zweiter Zustand je Knoten aus der Verdrillungsparitaet; FR)?
  Als [H] im Bericht, mit Ableitbarkeitsprobe.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, auf der Spur, die bei Start frei ist (cpu3 bis cpu7 bzw.
  p4000a/b); je <= 10 min. Zeitbox 150 min.

## Berichtigung vor dem Start (Leitung, 2026-10-04 14:47:44 CEST; vor jeder Rechnung und vor dem Agentenstart)

- **GT2 war falsch gezielt.** Finns Muster "0 +1 0 -1 0" hat Nullstellen bei 0, 360 und 720 Grad und vier
  Viertel-Schritte (0 bis 180 Grad steigt die Kraft, 180 bis 360 faellt sie auf null, 360 bis 540 negativ, 540 bis 720
  zurueck auf null). "Genau vier Nulldurchgaenge" passt nicht dazu.
- **Ableitbarkeitsprobe [M, ungeprueft; im Plan pruefen]:**
  - E_min(theta) ist 720-periodisch, weil die Klasse des Fadenzustands nur von theta mod 720 abhaengt (Guerteltrick).
  - Hat die Anordnung eine Spiegelebene, die die Drehachse enthaelt, gilt E_min(theta) = E_min(-theta) =
    E_min(720 - theta). Bei Drehung um eine zweizaehlige Achse des Tetraeders liegen zwei Spiegelebenen der Gruppe T_d
    durch die Achse (Ecken (1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1), Achse x, Ebenen y = z und y = -z). Dann sind die
    Nullstelle des Drehmoments bei 360 Grad und die Vorzeichenfolge +, - vorab ableitbar und kein Befund.
  - Die Existenz des Entwirrungswegs bei 720 Grad ist topologisch bekannt [L Dirac]. "Endlich" in GT3 ist deshalb leer;
    nur der Vergleich mit der Verdrillungsenergie bei 360 Grad zaehlt.
  - Nicht ableitbar und deshalb die eigentliche Messung: ob einfaches Abkuehlen den Entwirrungsweg findet (GT1), Energien
    und Sperren (GT3), Zwischenrasten und Lage der Kraftspitze (GT2a), Verhalten ohne Spiegelsymmetrie (GT2b).
- **Neue Vorhersagen (ersetzen GT2):**

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| GT2a | [H] Zweizaehlige Achse: auf dem Weg kleinster Energie keine weitere Nullstelle des Drehmoments in (0, 360) Grad (E_min steigt dort monoton, keine Zwischenrast); Kraftspitze bei 180 +- 45 Grad | 45 % |
| GT2b | [H] Allgemeine Achse ohne Spiegelsymmetrie (Achse vorab im Plan festgelegt): dasselbe Muster, Nullstelle innerhalb 360 +- 30 Grad | 35 % |

- **Zusaetzlich:** Fadenlaenge als Parameter mit mindestens zwei Werten (Konturlaenge 1,3- und 1,8-fach des geraden
  Abstands); der Guerteltrick braucht Schlaffe. GT1 und GT3 je Wert; das Urteil zaehlt fuer den groesseren Wert, der
  kleinere zeigt die Grenze.
- **Spuren beim Start:** cpu (Haupt) und p4000a (geteilt mit WOLFRAM-KEV-SCAN; der Lock regelt die Reihenfolge).
- **Zeitbox:** 180 min wegen der Zusammenlegung mit STRUKTUR-FEDERRING-1 (Literatur hoechstens 10 Abrufe fuer alles).
