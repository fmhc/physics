
### sha256

Code (lokal = .69, verglichen):

```
68c0a1fb9195550e4d93384304ba506c78e3239fbe9cd8a95e5571fa4e6bc45b  code/huellen_leiter.py
782058b1443b17a09f84a7f1e1888c593d2382dc8bab0bd2986372ca3308dac2  code/auswertung.py
1d15a38c17d06c71919cf86b425af43a574a04cba9cc2578cc4e29619d4d9b83  code/stille3.py
f831e818b4f2a00f56e281f5972badb1d9ed344dcd2242826ab6b31076917ecb  code/beutel.py
a132bb6f84012598282d6e089c50a9e0e0160e3468e24c2c9b2f190614b1de17  code/diag_profil.py
```

- Fassungen von code/huellen_leiter.py: a7279392... (V0, Profile, K1), 5076f72f... (Option weiter; Bloecke St1 0-50, 50-90; St2 0-50, 50-80, 168-180, 180-192; L1 St1), 1deb8dcf... (Nachtrag 1; St1 90-125; St2 80-105, 192-203, 255-262; L1 St2; Profile weiter), eb6d5986... (Stoppdatei; kein Lauf gestartet), 68c0a1fb... (Endfassung; alle spaeteren Laeufe). Zeilen mit unsicheren Nullstellen aus der Fassung 5076f72f sind mit der Endfassung neu gerechnet (alt-*.json behalten).
- code/auswertung.py: Endfassung 782058b1... (alle Auswertungslaeufe).

Plaene:

```
43ac7d2fb629760f16158f5b368097c9fa0ac2dbf05e14262ccae35444a553f5  PLAN.md.eingefroren-20261002-140012
426ed327df7f88ec6e0e7b9a9ef493c8466f9561eccf854eff8bb47194af08cf  PLAN-NACHTRAG-1.md.eingefroren-20261002-141607
51c76120a81914e5c9e597bb505fa7517936154b3fda1dcb9de11b44214c6604  PLAN-NACHTRAG-2.md.eingefroren-20261002-142129
84a5858c202bf3a0a1d3b108d3a94f2a771f2bfa9240c527be68a0378b4ecdc6  PLAN-NACHTRAG-3.md.eingefroren-20261002-142315
51f56c0e2d79ab5541e8786cbde227c6adb2ae07e5cac038b0517302058becfd  PLAN-NACHTRAG-4.md.eingefroren-20261002-143103
```

Ausgaben (lokal = Spiegel von /home/fmh/fmhc-physics-remote/runde18-huellen-leiter/aus/ ohne *.npz; Profile *.npz nur auf der .69):

```
1f149ff485ab5a0319aa87771708222a44230f1699715b00da4d49419b73b5c3  aus/laeufe/z-st1-*.json (verkettet, Namensfolge, 138 Dateien)
228741408fe12eeb7c899779e627f217c1f99b6c590fef61fe0ea05c3b2ef6c7  aus/laeufe/paar-st1-*.json (verkettet, Namensfolge, 130 Dateien)
5a75203534d39779114fd042d03128d849be2a3c8a1aec29112d8aaab68bdc93  aus/laeufe/z-st2-*.json (verkettet, Namensfolge, 177 Dateien)
819b9ac66512e1917c92d5ac9f4aac6e1f62edd99717d22b292fc26de8dc5196  aus/laeufe/paar-st2-*.json (verkettet, Namensfolge, 154 Dateien)
6c0de5ecf2dda6c8cd05425231ee7bdcd3e57551a3a6a8c8f1e2bdda42a192f7  aus/laeufe/auswertung.json
71d6854e95ad49b1f09bd2c7d695997b1e30ee21430f0fd81f59c37b03322f1f  aus/laeufe/auswertung-final.json
5ce185ec655577131d6eca73cb4e8006aab6294ca4ad91840360caaf0a6ab202  aus/laeufe/stellen.json
ba55b41b79068c078ce42f2b1b8303f5686ee17fa032e2c6db78928dc05237c1  aus/laeufe/umlauf-P-st1.json
1fee9728faf2886ef9d49c189568aceafaae2b414cdb59684f142ed70592f487  aus/laeufe/umlauf-P-st2.json
345b61b53388bfdcb21ca2396f4ed54613b68c08ea71a8e3816ac23a28e69f53  aus/umlauf-L1-st1.json
cdf5cd0448e08bc43ce912b9944c9d7f635c4eb9748192cf93a6b6532db223bb  aus/umlauf-L1-st2.json
d1ae9ff0e11d5667a09ca8457ba54e8417cdada33a40c79f2940eafb85c60c50  aus/k1-st1.json
c19ef929c1fa1518129f9d29b91826a87fbf9726044accbd8cdab88b132c82d2  aus/k1-st2.json
e69ed1c642e27c980adc67c08d82fc18a2bce383ee037793cdc11fbf764e3c3c  aus/abb-stellen.png
52f7a0cd06fe8bec1dacc6a30fd2d7fa4d63e712ab3bd90ab303837fd0779c5e  aus/abb-abstand.png
586c36891558f3ac36d20fbab1c672719f3707cd4dcd954df8bf63d0e5fbc748  aus/zeilen.json
2b043318bbee63d7e6641681c018a5bf65ecfb53ad29477cb86ba8e601eaac96  aus/prof/konvergenz.json
228b3beccbe82f50bb6e7547f60ba8ca9f154bea9a782a5030254f766f50a9a2  aus/prof-st1/profile-info.json
97c59bf85bdedf69a03332964ee615139792aee82e025d5471ae5611f5c2fdee  aus/prof-st2/profile-info.json
```

Hilfsskripte: hilfs/kette.sh, reparatur.sh, start-v1.sh, weiter-p1.sh, weiter-p2.sh, v3-auswertung.sh, konv.jq, l1punkte.jq, kurven.jq, anhang.jq, l1tab.jq; Entwuerfe hilfs/entwurf-*.md.

```
9de50a3e893051901f3365153d0efe27fa521082a2e38ae6bf8cf4db566c97d8  hilfs/kette.sh
527a25934fdda9e10bb4e5d7ba695890d763d1b2270df429107cd318bfc24bfe  hilfs/reparatur.sh
0cc531724c7ac8299ba7f619c1776f60d6f3bf4ee7a91f3c1c33f29f54d22c22  hilfs/start-v1.sh
efcc5f198f97a759735856e514d7d22bcec90f1e2f975c322622b6d947127c42  hilfs/v3-auswertung.sh
2d62aa64a94b2d6f58a0cc6fafb0784cf09860dfbac5fc896f32bbc974649978  hilfs/weiter-p1.sh
ad2f84b061b27b756246d78e70a783effbf07c20ef344c88baa34fea6846bd47  hilfs/weiter-p2.sh
b9a5a691ea2ac1e5628d0675c41863dc988c2412a8f4d330b7f9dca9cced88d0  hilfs/anhang.jq
b432affae065a40564a8e4802dbe33b963f92c7f6a6a09842d35b0d455412fa1  hilfs/konv.jq
b953a2e31ebb2768dd6e69185e40ff22346222dc184605a04d9947ed382624ef  hilfs/kurven.jq
561064418c2321c9d515c2bc0da42306955abd10d2ebdd4fd4aa3fda2d020230  hilfs/l1punkte.jq
08017cae9f579725a624d8a8657f1e38beaf9d4ae45ebbbaed93226b8c19ccf8  hilfs/l1tab.jq
```
