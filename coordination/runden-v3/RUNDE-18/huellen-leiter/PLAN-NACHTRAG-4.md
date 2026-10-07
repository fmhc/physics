# PLAN-NACHTRAG-4 (HUELLEN-LEITER) - NACHTRAEGLICH

- Geschrieben ab 14:31 CEST (date), nach Laufbeginn, nach Sicht der Paare 111 und 112 (Stufe 1). L2 bis L5 waren noch
  nicht ausgewertet.
- **Befund:** Ab Paar 111 (Zeilen 111/112, R ~ 39,5 bis 40) wechselt s auf allen Kurven zugleich von Unterzeile zu
  Unterzeile das Vorzeichen (Paar 111: 34 Wechsel in den Unterzeilen gegen 8 zwischen den Zeilen; Paar 112: 86 gegen 2;
  Betrag |s| dabei glatt, z. B. 0,29 ... 0,38 auf k = 1). Ein gemeinsamer Vorzeichenwechsel aller Kurven ist ein
  Rechenartefakt, kein Befund.
- **Diagnose [H, nicht gerechnet]:** Im Inneren grosser Baelle ist chi ~ e^(-1,17 (R - r)) und faellt fuer R > ~31
  unter die Rundungsgrenze (~1e-16) des Profils; das berechnete chi hat dort zufaelliges Vorzeichen. Die Kopplung
  2 f chi saet damit in die regulaere c-Loesung eine b-Komponente, die im Inneren mit e^(1,77 r) waechst (R = 40:
  ~1e-16 * e^71 ~ 1e14). s = m_ac an m_bc = 0 wird dann von diesem Rundungsanteil bestimmt und wechselt mit dem
  Vorzeichen des Rundungs-chi. Exakt waere dieser Anteil positiv und nur ~e^(0,6 R).
- **Folge (Wertung):** Gewertet werden nur Paare mit Index <= 109 (Zeilen 0 bis 110, omega^2 >= 0,76354, R <= 39,2).
  Darunter (auch die Insel aus Nachtrag 2) wird nichts gewertet; die Daten werden nur als Diagnose erwaehnt.
  Gegenprobe der Grenze: Bis Paar 110 stimmen Wechselzahl der Unterzeilen und der Zeilen ueberein (Stufe 1), und die
  Stellen beider Stufen werden abgeglichen.
- Keine neue Rechnung mit Abschneiden der Kopplung (das waere die Behebung: Kopplung 2 f chi = 0, wo chi unter ~1e-12
  liegt). Dafuer reicht die Zeitbox nicht; Empfehlung fuer eine Folgerunde.
- Ablauf: Alle Bloecke unterhalb Zeile 125 werden nicht mehr begonnen (Vorbelegung, Stoppdateien). Bereits laufende
  Auftraege laufen zu Ende (keine Prozesse beendet).
