# PLAN-NACHTRAG-3 (nachtraeglich, vor dem Kontrolllauf eingefroren)

- Geschrieben ab 2026-10-02 09:11:45 CEST (date). Nachtraeglich; D1b-Hauptlauf ist bereits ausgewertet bekannt.
- Anlass: Im D1b-Hauptlauf verlassen Teilchen mit Auslenkung 0,02 die 0,5-Kugel um L4 schon nach etwa 1,4 Umlaeufen,
  viel schneller als die lineare Anwachszeit (32 Umlaeufe bei mu = 0,0386). Ob das Kriterium "Abstand > 0,5" dann
  Instabilitaet misst oder nur grosse nichtlineare Librationen, ist ohne Kontrolle unterhalb mu_R nicht zu sagen.
  Diese Kontrolle fehlte im Plan.
- Zusatzlauf (Kontrolle, kein neuer Befund zu den Vorhersagen): gleiches Protokoll (dt 2 pi/400, 1000 Umlaeufe,
  Auslenkung 0,005 und 0,02, 64 Richtungen, Geschwindigkeit null) bei mu = 0,030, 0,035, 0,038 (linear stabil).
  Modus "kontrolle" in code/d1b_lebensdauer.py.
- Lesart vorab: Entkommen auch unterhalb mu_R viele Teilchen, dann misst die D1b-Lebensdauer mit diesem Kriterium nicht
  die lineare Instabilitaet; D1b-1 und D1b-2 werden dann nur mit diesem Vorbehalt bewertet.
