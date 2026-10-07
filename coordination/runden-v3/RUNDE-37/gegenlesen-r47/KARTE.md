# GEGENLESEN-R47: Frischer Leser fuer vier Ergebnisse der Runde 47 ohne unabhaengigen Gegenleser

- Leitung claude-primary. Karte und Erwartungen geschrieben ab 2026-10-05 08:34:25 CEST (date), vor jeder Pruefung.
- **Anlass:** Die vier Ergebnisse gehen in den Journaleintrag der Runde 47, in GEMEINSAMES-NETZ v4 und in Berichte an Finn. Keines hatte einen unabhaengigen Leser.
  - TAKT-UMKLAPP-1: Finns Vorrang-Karte
  - TT-GLAS-2: "frischer Gegenleser fehlt"
  - OKTA-SCHATTEN-1: "kein Gegenlesen"
  - KAC-DIAMANT-WICK-1
- **Gedaechtnisregeln:**
  - "Karten vor Veroeffentlichung gegenlesen"
  - "Gegenlesen in beide Richtungen": jede Zahl im Text gegen die Datei, und jede Datei-Zahl, die ein Urteil traegt, gegen den Text
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Pruefauftrag je Ergebnis (nur lokale Dateien, keine Netzabrufe)

1. **TAKT-UMKLAPP-1** (RUNDE-37/takt-umklapp-1/):
   - HT0-Rest (<= 6,6e-16, 252 k, 76 Netze), HT1' (Vorzeichen *1 und *2 auf V), HT2-Zaehlungen (13 bis 148 negative Richtungen; Gleichheit mit den UMKLAPP-1-Zahlen 15/19/15/14, 70/64/71/75, 142/131/147, 30), HT3 (1 122 von 1 124), TU1 (26 von 26 gegen 10 von 26)
   - jeweils gegen lauf-69/ bzw. nachtrag-69/
   - Nachtrag 4.5 a: P1 1/6 gegen umkreisbasiert 1/4 am Ecktetraeder (0, e1, e2, e3); diese Handrechnung der Leitung steht in RUNDE-47.md und wird ebenfalls geprueft
2. **TT-GLAS-2** (RUNDE-37/tt-glas-2/):
   - TG2-1 (keine wachsende Mode an 112 k-Klassen in 24 Netzen; 6 Nullmoden bei Gamma)
   - TG2-2 ((a) = (b) auf 1e-5; 7,1 % gegen 15,3 % bzw. 5,7 % gegen 11,4 %)
   - TG2-3 (4,66 +- 0,28 % bei N = 1024, 6,8 % bei N = 512, Exponent -0,56 bzw. -0,52)
   - TG2-0 (1,9e-9)
   - jeweils gegen auswertung-69/ bzw. die Laufdateien
   - Ist die OOM-Wiederholung auf p4000b mit demselben eingefrorenen Code belegt (sha256)?
3. **OKTA-SCHATTEN-1** (RUNDE-37/okta-schatten-1/):
   - OS0/OS1 (8 flache Baender ohne Sechsecke; keine Nullmode an 789 k mit Sechsecken; c = 1; a2 -0,0365 bis -0,0642; c^2 = 8q/(1 + 2q))
   - OS2 (H3 wachsend in 3 von 13 bzw. 12 von 23 Richtungen; [210] -0,28)
   - R12 (Spanne 3,9e-7); Rhombendodekaeder W^+ B W = -2 L_{*1} an 524 k
   - jeweils gegen lauf-69/
   - Ist "OS3 inhaltlich nicht entscheidbar" gegen den eingefrorenen Code ("eingetroffen") sauber begruendet, oder wurde eine Regel nach Sicht gelockert (Gedaechtnis "Kontrollen nicht nach Befund lockern")?
4. **KAC-DIAMANT-WICK-1** (RUNDE-37/kac-diamant-wick-1/):
   - Schreibtisch: Nelson-Masse m = hbar/(2D); c_eff = Wurzel(2/3) c bzw. c; m = 1,5 hbar lambda/c^2 bzw. hbar lambda/c^2; Grenzgeschwindigkeiten c, 0,816 c, c/Wurzel(3); Streuungen 1,45e-4 und 1,63e-4
   - gegen lauf-69/haupt.json
   - Wurde die Formschwelle wirklich erst nach der Schreibtischrechnung, aber vor der Rechnung gesetzt? Pruefe es an den mtime-Werten und an EINGEFROREN-SHA256.txt.
5. **Alle vier:** Stimmen die Abschnitte "Ergebnis zuerst" und "Einfach gesagt" mit den Tabellen ueberein? Gibt es Saetze, die staerker sind als die Daten?

## Erwartungen (vor jeder Pruefung)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| GR1 | Die tragenden Zahlen von TAKT-UMKLAPP-1 stimmen mit den Dateien | 85 % |
| GR2 | Die tragenden Zahlen von TT-GLAS-2 stimmen mit den Dateien | 85 % |
| GR3 | OKTA-SCHATTEN-1: Zahlen stimmen; die OS3-Wertung ist sauber begruendet, ohne nachtraegliche Lockerung | 75 % |
| GR4 | KAC-DIAMANT-WICK-1: Die Schreibtischformeln stimmen und decken sich mit haupt.json | 85 % |
| GR5 | In mindestens einem der vier "Ergebnis zuerst"- oder "Einfach gesagt"-Abschnitte steht eine Zahl oder ein Satz, der von der Quelle abweicht oder staerker ist | 45 % |
| GR6 | Die Handrechnung der Leitung (P1 1/6 gegen umkreisbasiert 1/4 am Ecktetraeder) stimmt | 90 % |

**Bedeutung (vorab):**
- **GR1 bis GR4 und GR6 treffen ein:** Die Ergebnisse gehen unveraendert ins Journal und in v4.
- **GR5 trifft ein:** Die A-Liste wird vor dem Journal eingearbeitet, mit Berichtigung im Rundenprotokoll.

## Rahmen

- Frischer Leser (pruefer-opus), kein Autor dieser Ergebnisse. Keine Netzabrufe, keine Rechnungen auf der .69.
- Lokal lesen mit cat, sed, grep und jq (nur lesen). Kein python, awk oder perl, auch kein awk-Fragment in einer Pipe.
- Ausgabe RUNDE-37/gegenlesen-r47/GEGENLESEN.md mit A-Liste (vor Journal und v4 zu berichtigen), B-Liste und C-Liste, je mit Fundstelle.
- Zeitbox 60 min.
