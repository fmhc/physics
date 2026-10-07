# MATERIE-NETZ-1: Wie antwortet Finns Netz auf eine ruhende Masse, wenn ihre Energie in der Eckregel steckt bzw. nur im Takt? (Runde 45, Finns R1 "Teste beide Varianten"; Q-Ball nur als Materie)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 04:16:30 CEST (date), vor jeder Rechnung.
- **Finn (05.10., gegen 04:15):** zu R1 "Teste beide Varianten"; zu Q-Baellen "Nur fürs Teilchenmodell".
- **Herkunft:**
  - GAMMA-NETZ-L (RUNDE-37/gamma-netz-l/DOSSIER.md, Abschnitt 1, Punkt 2): Statisch ist der Raum eine Eck-Skalierung durch den Takt.
    - a = -(kappa'/kappa_g) W mu plus Eichung, also gamma = 2 kappa'/kappa_g.
    - Ein gemeinsames Hamilton gibt kappa' = kappa_g/2, also gamma = 1 je Ecke [ES, Schreibtisch, nur gegen das Kontinuum geprueft].
    - O2: Das Licht muss Laengen und Takt spueren; mit Takt allein waere es die halbe Ablenkung.
  - Codex-Hinweis (ROOT-REVIEW-2003.txt): PPN-gamma verlangt Lapse, Quellenkopplung und geklaerte Zwangsbedingungen.
  - TT-ISO-1: Die skalare Regel ist auf dem gefuellten Netz auch langwellig zweiter Klasse.
  - Das Modell ist eine-welt-loch-1/code/ew.py (Hamilton-Netz).
- **Zwei Varianten (Finn: beide testen):**
  - V1: Die Energie der Masse geht in die Regel je Ecke ein, und Materie tickt im Takt der Ecke (kappa' = kappa_g/2).
  - V2: Materie tickt nur im Takt der Ecke, die Energie steht nicht in der Eckregel (kappa' = 0).
- **Quelle:** ein ruhendes, kugelfoermiges Energieprofil.
  - Zur Wahl stehen eine Punktquelle auf einer Ecke und ein Q-Ball-Profil (Papier I) als ausgedehnte Quelle.
  - Q-Baelle nur als Materie, keine Q-Ball-Verfeinerung.
- Kennzeichen: [M], [E], [P], [ES], [H].

## Ableitbarkeitsprobe (vor der Karte)

- **Vorab ableitbar [ES, GAMMA-NETZ-L]:** Im Fernfeld gilt gamma = 1 (V1) bzw. gamma = 0 (V2). MN0 ist damit eine Kontrolle der Schreibtischformel auf dem Gitter, keine Messung.
- **Nicht ableitbar:**
  - das Nahfeld (wenige Gitterabstaende)
  - ob die Paar-zweiter-Klasse-Struktur (Spur-Eichdefekt 0,9) die statische Antwort auf dem gefuellten Netz verfaelscht
  - das Vorzeichen der Antwort bei ausgedehnter Quelle
- **Projektsuche:** GAMMA-HAMILTON-1 war als Karte vorgeschlagen und geparkt (kein Messbezug). REGGE-ZEIT-1 und REGGE-4D-SCHIEF-1 geben gamma -> 1 im 4D-Regge-Netz. MATERIE-NETZ-1 stand seit Runde 42 in der Warteschlange.

## Auftrag (Code-Agent)

1. Code aus eine-welt-loch-1/code kopieren, dort nichts aendern. Statische Antwort des Hamilton-Netzes (gefuellt, V; Paarung A1R1) auf eine Energiequelle, in beiden Varianten.
2. **Messgroessen:**
   - Lapse-Stoerung (Takt) und raeumliche Stoerung (Eck-Skalierung bzw. Kantenlaengen) als Funktion des Abstands
   - gamma(r) als ihr Verhaeltnis
   - Vorzeichen (anziehend im Sinne Einsteins?)
   - Nahfeld gegen Fernfeld
   - Unterschied Punktquelle gegen ausgedehnte Quelle
3. **Beschreibend:** Spuert Maxwell auf Finns Netz (Kopplungen aus den Kantenlaengen, Code aus licht-finn-netz-1) die Laengenaenderung? Beispiel: Tempo bei gleichmaessiger Streckung und gleichem Takt.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| MN0 | Kontrolle [vorab ableitbar]: Fernfeld gamma = 1 +- 0,05 in V1 und gamma = 0 +- 0,05 in V2 | 75 % |
| MN1 | [H] Im Nahfeld (r < 3 Gitterabstaende) weicht gamma in V1 um mehr als 10 % vom Fernwert ab | 60 % |
| MN2 | [H] Die statische Antwort hat in beiden Varianten Einsteins Vorzeichen (Takt verlangsamt nahe der Masse) | 75 % |

**Bedeutung (vorab):**
- **MN0 trifft ein:** Die Schreibtischformel haelt auf dem Gitter.
  - V1 (Energie in der Eckregel und Ecktakt) gibt die volle Lichtablenkung, sofern das Licht Laengen und Takt spuert.
  - V2 gibt die halbe Ablenkung und ist durch die Messung der Lichtablenkung ausgeschlossen.
- **MN0 verfehlt in V1:** Die zweite-Klasse-Struktur des gefuellten Netzes veraendert die statische Antwort. Das waere ein Befund gegen die Fuellung [H].

## Rahmen

- Code-Agent.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu5 und cpu10.
- Je Lauf hoechstens 10 min, 1 Thread. Zeitbox 90 min.
