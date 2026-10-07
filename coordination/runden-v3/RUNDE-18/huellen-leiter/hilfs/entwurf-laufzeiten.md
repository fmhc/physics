
### Laufzeiten (.69, kleintest.sh, Service runtime; Start = Ende minus Laufzeit, UTC)

| Lauf | Spur | Ende | Dauer | rc | gewertet |
|---|---|---|---|---|---|
| V0 Zeilenliste | cpu | 12:00:23 | 0,5 s | 0 | ja |
| Profile Stufe 1 / Stufe 2 | cpu / cpu2 | 12:10:35 | je 600 s (Grenze) | 1 | ja |
| Profile Stufe 2 weiter / weiter2 | cpu2 | 12:20:36 / 12:21:25 | 600 s (Grenze) / 49,8 s | 1 / 0 | ja |
| Profile Stufe 1 weiter | cpu | 12:19:13 | 50,8 s | 0 | ja |
| K1 Stufe 1 / Stufe 2 | cpu3 / cpu4 | 12:01:07 / 12:01:38 | 31,7 s / 62,6 s | 0 | ja |
| Diagnose Profil-Newton | cpu3 | 12:03:26 | ~5 s | 0 | nein |
| Block Stufe 1, 0-50 / 50-90 | cpu3 | 12:07:10 / 12:11:03 | 153,8 s / 232,6 s | 0 | ja |
| Block Stufe 1, 90-125 | cpu3 | 12:27:57 | 600 s (Grenze) | 1 | ja bis Paar 109 |
| Block Stufe 2, 0-50 / 50-80 | cpu4 | 12:12:22 / 12:18:55 | 302,7 s / 320,4 s | 0 | ja |
| Block Stufe 2, 80-105 | cpu4 | 12:31:16 | 600 s (Grenze) | 1 | ja |
| Block Stufe 2, 105-125 | cpu4 | 12:44:34 | 600 s (Grenze) | 1 | ja bis Paar 109 |
| Lueckenfueller Stufe 2, 80-105 | cpu2 | 12:33:17 | 100,9 s | 0 | ja |
| Reparatur (Nachtrag 1) Stufe 1, 50-90 / Stufe 2, 50-80 | cpu4 / cpu2 | 12:34:34 / 12:36:17 | 197,4 s / 180,4 s | 0 | ja |
| Reparatur Stufe 1 0-50, Stufe 2 0-50 (nichts zu tun) | cpu4, cpu3 | 12:18:55, 12:37:59 | je < 1 s | 0 | ja |
| L1-Rechteck Stufe 1 / Stufe 2 | cpu4 | 12:13:34 / 12:21:16 | 72,1 s / 141,0 s | 0 | ja |
| Auswertung Stellen | cpu2 | 12:37:30 | 1,9 s | 0 | ja |
| Stichprobe Rechteck Stufe 1 / Stufe 2 | cpu2 / cpu3 | 12:38:39 / 12:40:13 | 68,7 s / 134,2 s | 0 | ja |
| Endauswertung / Abbildungen | cpu2 | 12:40:14 / 12:40:17 | 0,5 s / 3,4 s | 0 | ja |
| Block Stufe 2, 168-180 / 180-192 | cpu3 / cpu | 12:17:57 / 12:18:22 | 414,6 s / 466,4 s | 0 | nein |
| Block Stufe 2, 192-203 / 255-262 / 155-168 | cpu / cpu2 / cpu3 | 12:29:13 / 12:31:36 / 12:37:58 | je 600 s (Grenze) | 1 | nein |
| Block Stufe 1, 250-262 | cpu | 12:39:13 | 600 s (Grenze) | 1 | nein |
| Stopp- und Platzhalter-Aufrufe (14 Stueck) | alle | bis 12:44:40 | je < 1 s | 0 | - |
