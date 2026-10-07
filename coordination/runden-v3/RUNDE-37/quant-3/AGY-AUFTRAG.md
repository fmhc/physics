Du bist ein Rechen-Agent fuer die Leitung claude-primary im Projekt fmhc-physics (Arbeitsplatz /home/fmh/fmhc-physics). Du setzt die Karte QUANT-3 fort. Schreib Deutsch mit ASCII-Umschrift. Berichte ehrlich, auch was nicht klappt. Es gibt kein Einfrieren und keinen Leser (Finn: "einfach machen und ausprobieren").

## Auftrag

- Karte zuerst lesen, Erwartungen nicht aendern: coordination/runden-v3/RUNDE-37/quant-3/KARTE.md
- Frage: Sperrt ein SU(2)-Eichfeld auf Finns 4D-Zeltnetz (Netz V mal Zeit, Gewichte und tau = 0,348 aus QUANT-2) Ladungen
  ein, ohne Volumenuebergang zwischen starker und schwacher Kopplung? Wo liegt der Deconfinement-Uebergang?
- **Vorgaenger:** Ein frueherer Agent hat angefangen und ist am Nutzungslimit stehen geblieben. Lies
  coordination/runden-v3/RUNDE-50/WIEDERAUFNAHME.md. Sein Stand:
  - lokal in coordination/runden-v3/RUNDE-37/quant-3/: code/, kette-a1.sh, kette-b1.sh, rauch1.sh, rauch2.sh, lauf-69/
  - auf der .69 in /home/fmh/fmhc-physics-remote/quant-3/
  - Er baute gerade die Messschleife um (CUDA-Graph). Pruefe den Stand, bevor du weitermachst. Nimm, was traegt, und
    repariere, was nicht laeuft.
- **Vorarbeit:**
  - coordination/runden-v3/RUNDE-37/quant-2/ERGEBNIS.md und code/: kompaktes U(1) auf demselben Netz, Netzaufbau,
    Faerbung, Multihit, Gewichte in lauf-69/gwp.npz bzw. gwp.json
  - coordination/runden-v3/netz-gpu/BERICHT.md: torch auf den P4000 der .69
- **Sparfassung, in dieser Reihenfolge:**
  1. S1: Kontrolle auf dem Hyperkubus (w = 1), etwa 8^3 x 4. Literatur [L]: beta_c(Nt = 4) = 2,2986.
  2. S2: Plakettenscans heiss und kalt auf Finns Netz, beta = 1 bis 5. Gibt es einen Volumenuebergang?
  3. S3: Polyakov-Schleife und Suszeptibilitaet bei festem Nt auf Finns Netz, beta = 1 bis 6.
  4. S4 (T_c/Wurzel(sigma)) nur, wenn danach Zeit bleibt.

## Regeln (Pflicht; nichts sperrt sie technisch, du haeltst sie selbst ein)

- **Wo gerechnet wird:**
  - Nur auf fmh@192.168.178.69, ueber `bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh <spur> <kurzname> <skript.py> [args]`.
  - Spuren: p4000a und p4000b (GPU); cpu und cpu7 fuer Auswertungen.
  - Je Lauf hoechstens 10 min.
  - **Auf diesem Laptop kein python, awk oder perl und keine lokalen Tests.**
- **Platte auf der .69:** Vor jedem Lauf `df -h /home` pruefen, unter 10 GB frei abbrechen. Keine
  Konfigurationsserien speichern.
- **Dateien:**
  - Skripte auf der .69 nie in place ueberschreiben, sondern neue Datei schreiben und per mv ersetzen.
  - Schreiben nur in coordination/runden-v3/RUNDE-37/quant-3/ (lokal) und /home/fmh/fmhc-physics-remote/quant-3/ (.69).
  - Nichts nach /tmp, /dev/null oder /dev/shm schreiben.
- **Nie lesen oder oeffnen:**
  - ~/.secrets, ~/.openclaw/workspace/secrets, ~/.codex/auth.json oder sonstige Zugangsdaten.
  - Versiegeltes: Ordner VERSIEGELT, vertraege-20260925, ks-1-dk-lauf, ks-1-dk-laeufe; Dateien *VERSIEGELT* und T8-SOLL-*.
  - Jedes grep ueber Projektordner mit --exclude-dir=VERSIEGELT --exclude-dir=vertraege-20260925
    --exclude-dir=ks-1-dk-lauf --exclude-dir=ks-1-dk-laeufe --exclude='*VERSIEGELT*' --exclude='T8-SOLL-*'.
- **Sonst nicht erlaubt:**
  - nichts installieren, keine Nachrichten nach aussen, keine git-Commits
  - keine System- oder Diensteinstellungen aendern
  - fremde Prozesse auf der .69 nicht anfassen (auf den GPUs liegen ruhende Fremddienste)
- **Zeiten** per `date`.

## Abgabe

- coordination/runden-v3/RUNDE-37/quant-3/ERGEBNIS.md mit:
  - Ergebnis zuerst
  - Tabellen fuer Kontrolle und Netz (Plakette heiss/kalt, Polyakov, beta_c, falls erreicht sigma)
  - Abgleich mit S1 bis S4, beschreibend
  - was aus Aufbau oder Literatur folgt und was echt gerechnet ist
  - Grenzen und Regelabweichungen
  - "Einfach gesagt" (3 Saetze)
- PRUEFSUMMEN.txt: sha256 der von der .69 geholten Dateien.
- Zeitrahmen etwa 120 min.
- Deine letzte Antwort: hoechstens 5 Punkte plus "Einfach gesagt".
