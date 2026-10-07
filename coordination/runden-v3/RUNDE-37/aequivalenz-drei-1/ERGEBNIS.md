# Ergebnis: Äquivalenz auf dem Gitter verletzt

Die Äquivalenz von aktiver, passiver und träger Masse (AQ1, AQ2, AQ4) ist für den Q-Ball auf dem Gitter auf dem Prozent-Level verletzt. Das Verhältnis M_passiv / M_traege weicht deutlich von 1 ab (~2-3 % bei h=0.8) und hängt stark von der Bindung ab (Differenz > 5e-4). AQ3 ist bestätigt: Die Abweichungen verringern sich bei feinerem Gitter (h=0.6) um einen Faktor von etwa 1.5 bis 2.

## Tabellen der gemessenen Massen
(Massen normiert auf die Ruheenergie E)

### h = 0.8
(Werte aus den robusteren `-kb` Läufen mit kb=0.1 für die träge Masse)

| Ball (om) | Bindung | M_aktiv/E | M_passiv/E | M_traege/E | M_aktiv / M_traege | M_passiv / M_traege |
|---|---|---|---|---|---|---|
| 0.850 | 8.45 % | 1.0040 | 1.0151 | 1.0347 | 0.9703 | 0.9811 |
| 0.875 | 4.87 % | 1.0053 | 1.0108 | 1.0410 | 0.9657 | 0.9710 |
| 0.900 | 1.98 % | 1.0045 | 1.0132 | 1.0371 | 0.9686 | 0.9769 |

### h = 0.6
(Werte aus dem Fit `frueh_3_30_t3` für die passiv-Beschleunigung, kb=0.03)

| Ball (om) | Bindung | M_aktiv/E | M_passiv/E | M_traege/E | M_aktiv / M_traege | M_passiv / M_traege |
|---|---|---|---|---|---|---|
| 0.850 | 8.36 % | 1.0023 | 1.0025 | 1.0153 | 0.9872 | 0.9874 |
| 0.875 | 4.76 % | 1.0025 | 1.0019 | 1.0157 | 0.9870 | 0.9864 |
| 0.900 | 1.87 % | 1.0028 | 1.0030 | 1.0182 | 0.9849 | 0.9851 |

## Abgleich mit den Erwartungen

*   **AQ1 (M_passiv / M_traege = 1 auf 1e-3, h=0.8):** Widerlegt. Der Quotient liegt bei etwa 0.97 bis 0.98, eine Abweichung von 2 bis 3 %.
*   **AQ2 (M_aktiv / M_traege = 1 auf 1e-3, h=0.8):** Widerlegt. Der Quotient liegt bei etwa 0.966 bis 0.970.
*   **AQ3 (Abweichungen fallen von h=0.8 auf h=0.6 um Faktor >= 1.5):** Bestätigt. Die Abweichung von M_passiv/M_traege von 1 sinkt von ~0.024 auf ~0.014 (Faktor ~1.7). Die Abweichung von M_aktiv/M_traege sinkt von ~0.03 auf ~0.013 (Faktor ~2.3).
*   **AQ4 (Keine Abhängigkeit M_passiv/M_traege von Bindung > 5e-4):** Widerlegt. Bei h=0.8 schwankt der Quotient systematisch zwischen 0.971 und 0.981 (Differenz ~0.010), was weit über 5e-4 liegt. Auch bei h=0.6 ist die Schwankung noch ~0.002.

## Was aus dem Aufbau folgt und was gerechnet ist

Es wurden die Ruhemasse (aktiv), die schwere Masse im Fall in einem vorgegebenen Takt-Gradienten (passiv) und die Trägheit eines leicht geboosteten Q-Balls (träge) aus derselben Gitter-Wirkung berechnet. Die Messungen erfolgten rein synthetisch auf GPU für 3 verschiedene Bindungen bei 2 verschiedenen Gitterabständen. Es folgte keine Anpassung der Kontinuumserwartung (Äquivalenz), jedoch zeigt die Rechnung klar, dass das endliche Netz durch die Diskretisierung signifikante, bindungsabhängige Äquivalenzverletzungen auf dem Prozent-Level induziert.

## Grenzen und Regelabweichungen

*   Die Läufe für h=0.8 mit `kb=0.03` waren im Impuls sehr verrauscht (PEsp bis über 12 %). Daher wurden für die Auswertung bei h=0.8 die Nachläufe mit `kb=0.1` herangezogen, die deutlich stabiler liefen.
*   Für h=0.6 erwies sich der lineare Fit über das ganze Zeitfenster als instabil (z.B. bei h06-o0875), da die Bälle sehr weit fielen. Es wurde konsistent auf den frühen Fit (`frueh_3_30_t3`) zurückgegriffen.
*   Es gab keine Regelabweichungen bzgl. der Rechenumgebung. Die Berechnungen stammten großteils vom vorherigen Agenten, sie wurden lediglich vervollständigt (per `scp` synchronisiert) und ausgewertet.

## Einfach gesagt

Schwere und träge Masse sind im Prinzip dasselbe, aber nicht in unserem Computermodell. Weil wir den Raum in ein grobes Gitter zerteilen, fällt und bewegt sich der Ball minimal anders, als er es in einem glatten Raum tun würde. Je feiner wir das Gitter machen, desto kleiner wird dieser Fehler.

## Prüfsummen (sha256sum der .json-Dateien von .69)

```
acc1751ed00a132db3bcfe61f3f93a703d55edbc2db70c9aa9836d8c7e2e089a  h05-o085.json
4c2062aa9805842b868ee1c22d56fb024bc13b3cfa7b891584e7008963433152  h05-o0875.json
c27ae8e31655b6bcf6f4a4dc8a4259b20d9b9b819623c7f1d1984da068493bce  h05-o090.json
504e445bcbb072a91e4165a9868e572fb9453dafe600c9401803c286770cf819  h06-o085-dt.json
b51228aa621805852db78fc255ce444c24bd5b2a2f37dc66e8b87d0a9e232f32  h06-o085-g2.json
9e7138a09dbd5d500c74b2c1307f16b171012b2fdecf47c996f41d64c1a35517  h06-o085-n16.json
3445cf418eede8df9667a628cca659755eb202af0909780eb6418aff97737e20  h06-o085.json
c3cb3b7238e351625c2dff211fdc5efb42f0578208ce302258cf528e05538194  h06-o0875.json
77e6a29e970df9c9bc718c17b5fc376213773099354245b3b5b7d5da5b2e975a  h06-o090.json
837aa4a6c975d1a203cc0dad046449fa661192d57c01684afb250d6436cf7792  h08-o085-kb.json
ae27c35b035a4bce828744fa18e057471650a8edfa934fb762780b7d2ede826d  h08-o085-n18.json
72c72031be828a777feb0a9a2a72c1a18e9fb762df852c56962c7fc80f6175f5  h08-o085.json
5873ba6e8a42674ccdd8ed937c0195a75a55cf5f837307018e6369eaeccccfe8  h08-o0875-kb.json
704ffd82559fb35dcbef4587f618e983e968c59cc6abf102ada5785d8fb5057b  h08-o0875.json
402cb0a74fa0ca263411dd9145349fa011df07acdc99c3aa39f56a740f7a0b8b  h08-o090-kb.json
341643b645a35c1d4661c47e87ea8c607cf7190dfdfa6e6514d1596f063db905  h08-o090.json
78cb6f8d4c82f704b915eeef637baf3452232d81784063f87c1cd8d68547d86f  zf.json
```
