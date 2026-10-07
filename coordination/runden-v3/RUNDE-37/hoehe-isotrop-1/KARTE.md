# HOEHE-ISOTROP-1: Kann die Hebehoehe (Finns vierte Richtung) das kurzwellige Wuerfelmuster des Lichts auf V aufheben? (Runde 49, Fast Lane nach REGULAER-V-1)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 13:19:09 CEST (date), vor jeder Rechnung.
- **Herkunft [P]:**
  - REGULAER-V-1 (RUNDE-37/regulaer-v-1/ERGEBNIS.md): V hat eine Hebehoehe (Gewichtskammer der Dimension 9 bzw. 79). Innerhalb der Kammer aendert sich die l = 4-Anisotropie beta des gewichteten Laplace bis zum 4-Fachen; die Grundgeschwindigkeit bleibt c = 1. Nachtrag nach Sicht: Mit zwei verschieden schweren Lochmitten (F-43m-Schnitt) wechselt beta das Vorzeichen.
  - LICHT-FINN-NETZ-1 (RUNDE-37): Maxwell auf V langwellig isotrop; omega/(c k) = 1 + a2 (kl)^2 + ...; kubisches Kurzwellen-Muster; bedingte LHAASO-Schranke l < 7,0e-28 m (Achsen) bzw. 6,1e-28 m (Raumdiagonalen), aus a2.
  - KUBISCH-ANKER-L: l = 4-Schranken 9 Groessenordnungen schwaecher als die LHAASO-n = 2-Schranke.
  - Finns Schwerpunkt "Lichtgeschwindigkeit im Netz"; Finns Frage nach einer "temporären 4. Dimension".
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Ableitbarkeitsprobe (Leitung)

- **Vorab ableitbar [M]:**
  - Wechselt beta im F-43m-Schnitt stetig das Vorzeichen, gibt es dort einen Punkt mit beta = 0 (Zwischenwertsatz). Die Existenz ist also Kontrolle, keine Vorhersage.
  - Gewichte wirken nicht auf die Regge-Wirkung bei festen Kantenlaengen (de Goes [S, VIERTE-KOORDINATE-L]); Schwerewellen bleiben davon unberuehrt.
  - Die LHAASO-n = 2-Schranke greift am **richtungsgemittelten** a2 (Laufzeit bzw. Schwelle), nicht nur am l = 4-Anteil. beta = 0 allein hebt die Schranke deshalb nicht auf, solange das gemittelte a2 bleibt.
- **Nicht ableitbar:**
  - ob am Punkt beta = 0 (skalarer Laplace) auch der l = 4-Anteil des Lichts (Maxwell mit gewichteten *1, *2) verschwindet
  - ob sich das gemittelte a2 des Lichts in der Kammer veraendern oder auf null bringen laesst
  - was dann von der LHAASO-Schranke bleibt

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| HI0 | Kontrolle [P, M]: Der Code gibt beta aus REGULAER-V-1 an drei Stichpunkten auf 1e-6 wieder, und im F-43m-Schnitt gibt es einen Punkt mit beta = 0 innerhalb der Kammer | 90 % |
| HI1 | [H] Am Punkt beta = 0 ist auch der l = 4-Anteil von a2 beim Licht (Maxwell, gewichtete *1 und *2) kleiner als 1e-3 seines Werts bei w = Kammermitte | 40 % |
| HI2 | [H] Das richtungsgemittelte a2 des Lichts bleibt in der ganzen Kammer negativ (unterlichtschnell) und aendert sich um hoechstens den Faktor 2 | 55 % |
| HI3 | [H] Die bedingte LHAASO-Schranke an l aendert sich zwischen Kammermitte und beta-Nullpunkt um weniger als den Faktor 3 | 55 % |

**Bedeutung (vorab):**
- **HI1 trifft ein:** Die vierte Richtung (Hoehe) kann das kubische Kurzwellen-Muster des Lichts auf Finns Netz aufheben. Die Richtungsabhaengigkeit des Lichts waere dann erst in hoeherer Ordnung da.
- **HI2 und HI3 treffen ein:** Fuer die Datenschranke zaehlt das gemittelte a2; die Hoehe aendert die Schranke kaum. Das Muster ist dann nur fuer Richtungstests wichtig (KUBISCH-ANKER-L: heute 9 Groessenordnungen zu schwach).
- **HI2 verfehlt (a2 laesst sich auf null bringen):** Licht waere auf Finns Netz bis (kl)^4 ohne Dispersion; die LHAASO-n = 2-Schranke verloere ihren Griff [H, dann Nachrechnung Pflicht].

## Rahmen

- Code-Agent. Code aus RUNDE-37/regulaer-v-1/code (Kammer, gewichtete Sterne) und RUNDE-37/licht-finn-netz-1 (Maxwell auf V, a2, LHAASO-Umrechnung) kopieren, dort nichts aendern.
- Gewichtete Hodge-Sterne fuer Maxwell (*1 und *2 aus dem Potenzdiagramm) im Plan herleiten und mit einer Identitaet pruefen (z. B. Summe *1 l lᵀ = Vol I bei Gewichten).
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren p4000a und p4000b. Je Lauf hoechstens 10 min. Zeitbox 120 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
- Synthetisch, keine Messdatenbestaetigung.
