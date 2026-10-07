# Auftrag BEWEIS-1: Rechnergestuetzter Beweis der strahlungsfreien Atmungsmode des 3D-Q-Balls

- Leitung: claude-primary. Brief geschrieben ab 2026-09-30 05:33:52 CEST (date).
- Anlass: Finn im Chat, 05:19: "bau einen beweis".
- Karte in Runde 7 (v3, explorativ). Ein Beweis ist allerdings entweder vollstaendig oder ein Geruest mit benannten Luecken.
- Diese Datei ist der woertliche Auftrag an den Beweis-Agenten. Zusaetze der Leitung, die ueber die Vorgaben der v3-Regeln
  hinausgehen, sind mit **[Leitung]** markiert.

## 0. Ziel

Mit strenger Rechnerunterstuetzung beweisen:
- Rechnerunterstuetzung heisst Kugel- bzw. Intervallarithmetik plus analytische Lemmata fuer Schwaenze und Restglieder.
- Modell: Linearisierung der 3D-NLKG um den Q-Ball mit U(S) = S - S^2 + S^3/2.
- Aussage: Bei einem omega* mit omega*^2 nahe 0,79767679 gibt es eine eingebettete Eigenfrequenz rho* nahe 1,74461754.
  - Sektor l = 0.
  - Die Eigenfunktion faellt exponentiell ab.
  - Das ist ein gebundener Zustand im Kontinuum (BIC): In linearer Ordnung strahlt diese Atmung nicht ab.

## 1. Modell (selbst nachpruefen, nicht glauben)

- **NLKG:** phi_tt - Laplace phi + U'(|phi|^2) phi = 0 mit U(S) = S - S^2 + beta S^3 und beta = 1/2.
  - U'(S) = 1 - 2S + 3 beta S^2
  - U''(S) = -2 + 6 beta S
- **Q-Ball:** phi = f(r) e^{i omega t} mit f'' + (2/r) f' = (U'(f^2) - omega^2) f, f'(0) = 0, f > 0 und f -> 0.
  - Positive radiale Loesungen gibt es fuer omega^2 im Intervall (1 - 1/(4 beta), 1) = (0,5; 1).
- **Linearisierung (Herleitung der Leitung):**
  - Ansatz: phi = e^{i omega t} (f + a(x) e^{i rho t} + b(x) e^{-i rho t}) mit reellen a und b.
  - Gleichungen, mit S = f^2:
    - -Laplace a + (U'(S) + U''(S) S - (omega + rho)^2) a + U''(S) S b = 0
    - -Laplace b + (U'(S) + U''(S) S - (omega - rho)^2) b + U''(S) S a = 0
  - In resonanz3d.py, bic2.py und bei Codex nachsehen, ob genau diese Gleichungen gerechnet wurden. Jede Abweichung melden.
- **Sektor l = 0:** a = A(r)/r und b = B(r)/r. Damit gilt:
  - A'' = V_+ A + C B
  - B'' = V_- B + C A
  - mit V_pm = U'(S) + U''(S) S - (omega pm rho)^2 und C = U''(S) S
  - Das System ist reell-symmetrisch. Also ist die Wronski-Form W(Psi, Phi) = Psi . Phi' - Psi' . Phi konstant in r.
- **Kanaele fuer 1 - omega < rho < 1 + omega:**
  - Kanal a ist offen, mit Wellenzahl k = sqrt((omega + rho)^2 - 1).
  - Kanal b ist geschlossen, mit Abfallrate kappa_c = sqrt(1 - (omega - rho)^2).
- **BIC-Bedingung:** Es gibt (A, B) ungleich 0 mit A(0) = B(0) = 0 und A, B in L^2(0, unendlich).

## 2. Bisherige Evidenz (kein Beweis)

- **Anthropic, RUNDE-07/bic2/bic2.py exakt** (h = 0,01):
  - rho* = 1,7446175180 und omega*^2 = 0,797676819
  - Umlaufzahl -1 auf Rechtecken mit dx = 5e-4 und 1e-4
  - kleinstes |W| auf dem Rand 2,0e-5
- **Codex, eigener Zwei-Kanal-Loeser** mit R = 44, 56 und 68:
  - omega*^2 = 0,7976767871108792 und rho* = 1,7446175448365042
  - Die Stufendifferenzen liegen unter 7e-13. Codex schreibt selbst: "keine zertifizierte Fehlerschranke" und "der aktuelle
    numerische Grad ist kein Zertifikat".
  - Quellen: coordination/resonance-20260930/bic-tail/ERGEBNIS.txt, BIC-LITERATUR-NACH-UMLAUF.txt, UMLAUF-CODEX.md,
    3D-ABLEITUNG-CODEX.txt, feshbach-20260930/
- **Codex, nichtlinear:** Die nackte Mode strahlt als endliche Anregung in der zweiten Harmonischen ab; der Fluss waechst
  wie epsilon^4. Der Satz muss deshalb ausdruecklich "linear" heissen.
- **Literatur** (RUNDE-07/L4-BIC-FAMILIE-LITERATUR.md):
  - Vorbild: Ayala, Blanco, Cakoni, Hovsepyan und Vogelius, arXiv:2609.23217. Dort sind Strahlungsnullstellen in der Optik
    rechnergestuetzt bewiesen.
  - Kodimension: Agmon, Herbst und Maad Sasane 2010.
  - Cuccagna und Maeda 2020: Fuer NLS-Grundzustaende werden keine eingebetteten Eigenwerte erwartet.
  - Collot, Germain und Pacherie 2025: In 1D NLS gibt es keine.
- **Theorie-Entwurf:** RUNDE-07/THEORIE-ATMUNGS-NULLSTELLEN.md (Phasenregel, Hypothese).
- **Codes zum Lesen:** RUNDE-06/resonanz3d/resonanz3d.py (Profil und Linearisierung) und RUNDE-07/bic2/bic2.py (W-Funktion,
  Umlaufzahl).

## 3. Vorgeschlagene Architektur [Leitung]

Pruefen, verbessern oder begruendet abweichen.

- **(a) Jost-Loesung Psi_d:**
  - Fuer reelle (rho, omega) im Fenster ist sie bis auf einen Faktor eindeutig durch B ~ e^{-kappa_c r} und A -> 0 fuer
    r -> unendlich.
  - Konstruktion: Volterra-Integralgleichung auf [L, unendlich) mit den freien Loesungen.
  - Die Abweichung der Koeffizienten vom Unendlich-Wert ist durch c f^2 <= c' e^{-2 kappa0 r}/r^2 beschraenkt, mit
    kappa0 = sqrt(1 - omega^2).
  - Kontraktion mit expliziten Konstanten ergibt eine strenge Huelle von Psi_d(L) und Psi_d'(L).
- **(b) F(rho, x) := (A_d(0), B_d(0)):**
  - Rueckwaerts von L nach 0 integrieren. Bei l = 0 hat das System in A, B keine Singularitaet.
  - Lemma: F = 0 genau dann, wenn ein BIC vorliegt. Jede L^2-Loesung ist ein Vielfaches von Psi_d.
  - Gleichwertig: F_i = W(Psi_d, Reg_i) mit den regulaeren Loesungen Reg_i(0) = 0, Reg_i'(0) = e_i.
  - Das ist Codex' F ohne Abschneiden.
- **(c) Profil:**
  - strenge Einschliessung auf [0, L]: Potenzreihe bei r = 0 mit Restabschaetzung, danach Taylor-Schritte mit strengem Rest
  - Schwanzschranke fuer r >= L, per Vergleichslemma oder Kontraktion auf der stabilen Mannigfaltigkeit
  - Eindeutigkeit und Stetigkeit in omega, auf einem von zwei Wegen:
    - selbst: Intervall-Newton bzw. Krawczyk auf einem Anschlussproblem
    - Literatur: Eindeutigkeit positiver radialer Loesungen der kubisch-quintischen Gleichung
      Laplace f = (kappa0^2 - 2 f^2 + 3 beta f^4) f. Kandidaten sind Serrin und Tang 2000 sowie Killip, Oh, Pocovnicu und
      Visan 2017. Die Voraussetzungen an der Quelle pruefen.
- **(d) Nullstelle:**
  - Poincare-Miranda auf einem kleinen Rechteck um (rho*, x*), nach Vorkonditionierung G = M F mit M ~ (DF)^{-1}. Oder eine
    zertifizierte Umlaufzahl.
  - Kantenhuellen ueber Parameterstuecke mit zentrierten Formen: Wert am Stueckmittelpunkt plus strenge Ableitungsschranke,
    noetigenfalls zweiter Ordnung. So wird der Wrapping-Effekt umgangen.
  - Die Stetigkeit von F auf dem ganzen Rechteck folgt aus (a) bis (c).
- **(e) optional:** Eindeutigkeit der Nullstelle im Rechteck (Krawczyk mit einer Huelle von DF).
- **(f) Schluss:**
  - rho* liegt strikt in (1 - omega*, 1 + omega*).
  - Die Eigenfunktion faellt exponentiell ab.
  - Das ist eine Aussage ueber die lineare Gleichung: zeitperiodisch und raeumlich lokalisiert.

## 4. Meilensteine und Abgaben

Alles liegt in RUNDE-07/beweis/.

- **M0, BEWEIS-PLAN.md:**
  - Satz im genauen Wortlaut
  - Lemmaliste
  - analytische Beweise der Schwanzlemmata mit expliziten Konstanten
  - Zertifizierungsalgorithmus
  - Laufzeit, gemessen an einem Probelauf (nicht geschaetzt)
  - Lueckenliste
  - nicht strenge Vorrechnung (float oder mpmath, auf der .69), um L, Rechteck und Stueckzahl zu waehlen, mit Abgleich an
    Codex' Punkt
- **M1:** strenge Profilhuelle an einem Punkt omega
- **M2:** strenge Huelle von F an einem Punkt (rho, x)
- **M3:** Kantenzertifikat plus Poincare-Miranda oder Umlaufzahl; daraus folgt die Existenz
- **M4, BEWEIS.md:**
  - Satz und Beweis
  - Zertifikatsausgaben: Dateien mit sha256
  - Lueckenliste
  - "Einfach gesagt"
- **STAND.md** laufend fortschreiben: Zeit per date, Meilenstein, was gerade laeuft. So kann die Leitung Zwischenstaende
  lesen.
- **[Leitung]** Nach M0 ohne Rueckfrage weiterarbeiten (Fast Lane). Die Leitung laesst den Plan parallel frisch gegenlesen
  und schickt Anmerkungen per Nachricht.
- **[Leitung]** Arbeiten, bis M4 erreicht ist oder ein klarer Blocker vorliegt. Spaetestens nach etwa drei Stunden mit einem
  Zwischenbericht enden: Stand, naechster Schritt, was fehlt. Die Leitung setzt dann fort.

## 5. Strenge-Regeln

- **"Bewiesen"** nur, wenn die ganze Kette streng ist:
  - Kugelarithmetik (python-flint arb/acb/arb_mat, Praezision mindestens 128 bit) fuer jeden Rechenschritt
  - strenge Restglieder fuer jede Reihen- und Taylorabschaetzung
  - analytische Lemmata mit Beweis im Text
- **Kein float64 in der strengen Kette.** float darf nur Startwerte und den Vorkonditionierer liefern, weil die Pruefung
  selbst streng ist.
- **Lueckenliste:** Jede Stelle, die nicht streng ist, kommt mit Grund in die Lueckenliste. Ohne vollstaendige Kette heisst
  das Ergebnis "Beweisgeruest, Luecken: ...", nicht "bewiesen".
- **Literatur:** Zitate nur mit an der Quelle geprueften Aussagen und Voraussetzungen. Sonst mit [L?] markieren und nicht
  tragend verwenden.
- **Kein Lockern nach dem Befund:**
  - Scheitert ein Zertifikat, die Ursache melden.
  - Rechteck, Stueckzahl und Praezision duerfen geaendert werden, jede Aenderung mit Zeit in STAND.md.
- **Wortwahl:**
  - "im linearen Modell"
  - "exakt null" nur fuer eine bewiesene Nullstelle
  - Numerische Evidenz heisst "Evidenz", nicht "Beleg" und nicht "Beweis".

## 6. Betriebsregeln

- **Rechenort:** nur die .69 (fmh@192.168.178.69, ssh -o ProxyJump=none), ueber den vorhandenen Controller.
  - Aufruf aus dem Arbeitsordner /home/fmh/fmhc-physics-remote/runde7-beweis/ (anlegen):
    `bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh <spur> <kurzname> <skript.py> [args]`
  - Spuren: cpu, cpu2 und cpu4. cpu3 belegt EVO-1. Die Spuren sind per Lock geteilt, Aufrufe warten.
  - Jeder Aufruf dauert hoechstens 10 min (RuntimeMaxSec=600, MemoryMax=4G, ein Kern). Lange Rechnungen in Stuecke von
    hoechstens 10 min zerlegen.
  - Das Python dort (/home/fmh/fmhc-physics-gpu-venv/bin/python) nimmt kleintest.sh automatisch. python-flint 0.9.0 (seit
    05:32 von der Leitung installiert) und mpmath 1.3.0 sind vorhanden. Eine GPU ist nicht noetig.
- **Start im Hintergrund**, mit absoluten Logpfaden:
  `nohup setsid bash -c "cd /home/fmh/fmhc-physics-remote/runde7-beweis && bash .../kleintest.sh ... > /home/fmh/fmhc-physics-remote/runde7-beweis/LAUF-x.log 2>&1" < /dev/null &`
  - Nicht zwei nohup-Starts mit `cd X && ... &` in einem ssh-Befehl mischen.
  - Logs sollen "ende ... rc=" enthalten (kommt aus kleintest.sh). Die Leitung beobachtet runde7-beweis/LAUF*.log.
- **Laufende Skripte** nie ueberschreiben: neue Fassung unter neuem Namen hochladen, dann mv.
- **Prozesse:** kein pkill -f, denn das Muster trifft die eigene Shell. Nur per PID beenden.
- **Lokal (Laptop):**
  - Keine Interpreterstarts: kein python, python3 oder `python3 -c 1` lokal, auch nicht als Vorsatz vor grep oder sed.
  - Kein awk. JSON mit jq pruefen.
  - Lokal nur lesen, schreiben, scp und ssh.
- **Heredocs** immer quoten (<<'EOF') oder Write benutzen.
- **Zeiten** nur per date messen, nie schaetzen. Beginn und Ende gehoeren in den Bericht.
- **Nicht oeffnen:**
  - ~/.secrets, ~/.openclaw/workspace/secrets, ~/.codex/auth.json
  - KS-1-Ergebnisse, T8-SOLL-*, coordination/vertraege-20260925/, ks-1-dk-lauf/, ks-1-dk-laeufe/
- **Verboten:** Hooks, Shims, Wrapper, Dienste und Timer. Keine Journaleintraege (macht die Leitung), kein git.
- **Fremde Dateien** (bic2.py, resonanz3d.py, Codex-Ordner) nur lesen, nie aendern.

## 7. Bericht am Ende (an die Leitung)

- hoechstens 5 Punkte, Ergebnis zuerst
- Status je Meilenstein
- Lueckenliste
- Rechenzeiten (gemessen)
- Dateien
- "Einfach gesagt": 3 bis 5 Saetze auf Zehntklass-Niveau
