# Dex Change Worksheet

Every Pokemon in the regional dex, with the typing and base stats it currently
builds with. Generated from the game data - do not hand-edit anything except the
**Changes** column.

## How to use this

Write what you want changed in the Changes column. Leave it blank for anything
you're happy with. Free text is fine, but these forms are unambiguous:

| To change | Write |
|-----------|-------|
| Typing | `type: Grass/Steel` (or `type: Grass` to make it single) |
| Every base stat | `stats: 80/120/70/60/70/100` (HP/Atk/Def/SpA/SpD/Spe) |
| One base stat | `spe: 110` or `atk: +15` |
| An evolution | `evo: level 32 -> Gyarados` or `evo: Water Stone -> Ludicolo` |
| A learnset | `learn: 25 Flamethrower, 31 Slack Off` |
| Move access | `moves: +Earthquake, -Tackle` |
| An ability | `ability: +Levitate` or `ability: Overgrow / Chlorophyll` |

Several changes for one Pokemon go in the same cell, separated by `;` - for
example `type: Grass/Steel; spe: 110; evo: level 40 -> Torterra`.

Regenerate after edits are applied with `python3 dev_scripts/dex_worksheet.py`;
your Changes column is preserved.

## Forms

Where a dex entry covers a family with several forms, these are the ones the
stats below refer to: Castform (Normal), Rotom (base), Toxtricity (Amped),
Meowstic (Male), Gimmighoul (Chest), Hisuian Basculin (White-Striped),
Basculegion (Male).

## The dex


| #   | Pokemon             | Type              | HP  | Atk | Def | SpA | SpD | Spe | BST | Changes |
|-----|---------------------|-------------------|-----|-----|-----|-----|-----|-----|-----|---------|
| 1   | Turtwig             | Grass             | 55  | 68  | 64  | 45  | 55  | 31  | 318 |  |
| 2   | Grotle              | Grass             | 75  | 89  | 85  | 55  | 65  | 36  | 405 |  |
| 3   | Torterra            | Grass/Ground      | 95  | 109 | 105 | 75  | 85  | 56  | 525 |  |
| 4   | Fuecoco             | Fire              | 67  | 45  | 59  | 63  | 40  | 36  | 310 |  |
| 5   | Crocalor            | Fire              | 81  | 55  | 78  | 90  | 58  | 49  | 411 |  |
| 6   | Skeledirge          | Fire/Ghost        | 104 | 75  | 100 | 110 | 75  | 66  | 530 |  |
| 7   | Totodile            | Water             | 50  | 65  | 64  | 44  | 48  | 43  | 314 |  |
| 8   | Croconaw            | Water             | 65  | 80  | 80  | 59  | 63  | 58  | 405 |  |
| 9   | Feraligatr          | Water/Dark        | 85  | 105 | 100 | 79  | 83  | 78  | 530 |  |
| 10  | Poliwag             | Water             | 40  | 50  | 40  | 40  | 40  | 90  | 300 |  |
| 11  | Poliwhirl           | Water             | 65  | 65  | 65  | 50  | 50  | 90  | 385 |  |
| 12  | Poliwrath           | Water/Fighting    | 90  | 95  | 95  | 70  | 90  | 70  | 510 |  |
| 13  | Politoed            | Water/Fairy       | 90  | 75  | 75  | 100 | 100 | 70  | 510 |  |
| 14  | Ledyba              | Bug/Flying        | 40  | 20  | 30  | 40  | 80  | 55  | 265 |  |
| 15  | Ledian              | Bug/Flying        | 55  | 35  | 50  | 55  | 110 | 85  | 390 |  |
| 16  | Murkrow             | Dark/Flying       | 60  | 85  | 42  | 85  | 42  | 91  | 405 |  |
| 17  | Honchkrow           | Dark/Flying       | 100 | 125 | 52  | 105 | 52  | 71  | 505 |  |
| 18  | Teddiursa           | Normal            | 60  | 80  | 50  | 50  | 50  | 40  | 330 |  |
| 19  | Ursaring            | Normal            | 90  | 130 | 75  | 75  | 75  | 55  | 500 |  |
| 20  | Ursaluna            | Ground/Normal     | 130 | 140 | 105 | 45  | 80  | 50  | 550 |  |
| 21  | Tropius             | Grass/Flying      | 99  | 68  | 103 | 72  | 107 | 51  | 500 |  |
| 22  | Spheal              | Ice/Water         | 70  | 40  | 50  | 55  | 50  | 25  | 290 |  |
| 23  | Sealeo              | Ice/Water         | 90  | 60  | 70  | 75  | 70  | 45  | 410 |  |
| 24  | Walrein             | Ice/Water         | 110 | 80  | 90  | 95  | 90  | 65  | 530 |  |
| 25  | Bidoof              | Normal            | 59  | 45  | 40  | 35  | 40  | 31  | 250 |  |
| 26  | Bibarel             | Normal/Water      | 79  | 85  | 60  | 55  | 60  | 71  | 410 |  |
| 27  | Hippopotas          | Ground            | 68  | 72  | 78  | 38  | 42  | 32  | 330 |  |
| 28  | Hippowdon           | Ground            | 108 | 112 | 118 | 68  | 72  | 47  | 525 |  |
| 29  | Pansage             | Grass             | 50  | 53  | 48  | 53  | 48  | 64  | 316 |  |
| 30  | Simisage            | Grass             | 75  | 98  | 63  | 98  | 63  | 101 | 498 |  |
| 31  | Pansear             | Fire              | 50  | 53  | 48  | 53  | 48  | 64  | 316 |  |
| 32  | Simisear            | Fire              | 75  | 98  | 63  | 98  | 63  | 101 | 498 |  |
| 33  | Panpour             | Water             | 50  | 53  | 48  | 53  | 48  | 64  | 316 |  |
| 34  | Simipour            | Water             | 75  | 98  | 63  | 98  | 63  | 101 | 498 |  |
| 35  | Timburr             | Fighting/Grass    | 75  | 80  | 55  | 25  | 35  | 35  | 305 |  |
| 36  | Gurdurr             | Fighting/Steel    | 85  | 105 | 85  | 40  | 50  | 40  | 405 |  |
| 37  | Conkeldurr          | Fighting/Ground   | 105 | 140 | 95  | 55  | 65  | 45  | 505 |  |
| 38  | Solosis             | Psychic           | 45  | 30  | 40  | 105 | 50  | 20  | 290 |  |
| 39  | Duosion             | Psychic           | 65  | 40  | 50  | 125 | 60  | 30  | 370 |  |
| 40  | Reuniclus           | Psychic           | 110 | 65  | 75  | 125 | 85  | 30  | 490 |  |
| 41  | Noibat              | Flying/Dragon     | 40  | 30  | 35  | 45  | 40  | 55  | 245 |  |
| 42  | Noivern             | Flying/Dragon     | 85  | 70  | 80  | 97  | 80  | 123 | 535 |  |
| 43  | Grubbin             | Bug               | 47  | 62  | 45  | 55  | 45  | 46  | 300 |  |
| 44  | Charjabug           | Bug/Electric      | 57  | 82  | 95  | 55  | 75  | 36  | 400 |  |
| 45  | Vikavolt            | Bug/Electric      | 77  | 70  | 90  | 145 | 75  | 43  | 500 |  |
| 46  | Bounsweet           | Grass             | 42  | 30  | 38  | 30  | 38  | 32  | 210 |  |
| 47  | Steenee             | Grass             | 52  | 40  | 48  | 40  | 48  | 62  | 290 |  |
| 48  | Tsareena            | Grass             | 72  | 120 | 98  | 50  | 98  | 72  | 510 |  |
| 49  | Toxel               | Electric/Poison   | 40  | 38  | 35  | 54  | 35  | 40  | 242 |  |
| 50  | Toxtricity          | Electric/Poison   | 75  | 98  | 70  | 114 | 70  | 75  | 502 |  |
| 51  | Hisuian Qwilfish    | Dark/Poison       | 65  | 95  | 85  | 55  | 55  | 85  | 440 |  |
| 52  | Overqwil            | Dark/Poison       | 85  | 115 | 95  | 65  | 65  | 85  | 510 |  |
| 53  | Tarountula          | Bug               | 35  | 41  | 45  | 29  | 40  | 20  | 210 |  |
| 54  | Spidops             | Bug               | 60  | 79  | 92  | 52  | 86  | 35  | 404 |  |
| 55  | Nymble              | Bug               | 33  | 46  | 40  | 21  | 25  | 45  | 210 |  |
| 56  | Lokix               | Bug/Dark          | 71  | 102 | 78  | 52  | 55  | 92  | 450 |  |
| 57  | Orthworm            | Steel             | 100 | 85  | 145 | 60  | 55  | 95  | 540 |  |
| 58  | Glimmet             | Rock/Poison       | 48  | 35  | 42  | 105 | 60  | 60  | 350 |  |
| 59  | Glimmora            | Rock/Poison       | 83  | 55  | 90  | 130 | 81  | 86  | 525 |  |
| 60  | Roaring Moon        | Dragon/Dark       | 105 | 139 | 71  | 55  | 101 | 119 | 590 |  |
| 61  | Iron Valiant        | Fairy/Fighting    | 74  | 130 | 90  | 120 | 60  | 116 | 590 |  |
| 62  | Combee              | Bug/Flying        | 30  | 30  | 42  | 30  | 42  | 70  | 244 |  |
| 63  | Vespiquen           | Bug/Flying        | 70  | 80  | 102 | 80  | 102 | 40  | 474 |  |
| 64  | Galarian Slowpoke   | Psychic           | 90  | 65  | 65  | 40  | 40  | 15  | 315 |  |
| 65  | Galarian Slowbro    | Poison/Psychic    | 95  | 100 | 95  | 100 | 70  | 30  | 490 |  |
| 66  | Galarian Slowking   | Poison/Psychic    | 95  | 65  | 80  | 110 | 110 | 30  | 490 |  |
| 67  | Alolan Grimer       | Poison/Dark       | 80  | 80  | 50  | 40  | 50  | 25  | 325 |  |
| 68  | Alolan Muk          | Poison/Dark       | 105 | 105 | 75  | 65  | 100 | 50  | 500 |  |
| 69  | Meowth              | Normal            | 40  | 45  | 35  | 40  | 40  | 90  | 290 |  |
| 70  | Alolan Meowth       | Dark              | 40  | 35  | 35  | 50  | 40  | 90  | 290 |  |
| 71  | Galarian Meowth     | Steel             | 50  | 65  | 55  | 40  | 40  | 40  | 290 |  |
| 72  | Persian             | Normal            | 65  | 70  | 60  | 65  | 65  | 115 | 440 |  |
| 73  | Alolan Persian      | Dark              | 65  | 60  | 60  | 75  | 65  | 115 | 440 |  |
| 74  | Perrserker          | Steel             | 70  | 110 | 100 | 50  | 60  | 50  | 440 |  |
| 75  | Alolan Geodude      | Rock/Electric     | 40  | 80  | 100 | 30  | 30  | 20  | 300 |  |
| 76  | Alolan Graveler     | Rock/Electric     | 55  | 95  | 115 | 45  | 45  | 35  | 390 |  |
| 77  | Alolan Golem        | Rock/Electric     | 80  | 120 | 130 | 55  | 65  | 45  | 495 |  |
| 78  | Galarian Farfetch'd | Fighting          | 52  | 95  | 55  | 58  | 62  | 55  | 377 |  |
| 79  | Sirfetch'd          | Fighting          | 62  | 135 | 95  | 68  | 82  | 65  | 507 |  |
| 80  | Hisuian Voltorb     | Electric/Grass    | 40  | 30  | 50  | 55  | 55  | 100 | 330 |  |
| 81  | Hisuian Electrode   | Electric/Grass    | 60  | 50  | 70  | 80  | 80  | 150 | 490 |  |
| 82  | Elekid              | Electric          | 45  | 63  | 37  | 65  | 55  | 95  | 360 |  |
| 83  | Electabuzz          | Electric          | 65  | 83  | 57  | 95  | 85  | 105 | 490 |  |
| 84  | Electivire          | Electric          | 75  | 123 | 67  | 95  | 85  | 95  | 540 |  |
| 85  | Magby               | Fire              | 45  | 75  | 37  | 70  | 55  | 83  | 365 |  |
| 86  | Magmar              | Fire              | 65  | 95  | 57  | 100 | 85  | 93  | 495 |  |
| 87  | Magmortar           | Fire              | 75  | 95  | 67  | 125 | 95  | 83  | 540 |  |
| 88  | Paldean Wooper      | Poison/Ground     | 55  | 45  | 45  | 25  | 25  | 15  | 210 |  |
| 89  | Clodsire            | Poison/Ground     | 130 | 75  | 60  | 45  | 100 | 20  | 430 |  |
| 90  | Snubbull            | Fairy             | 60  | 80  | 50  | 40  | 40  | 30  | 300 |  |
| 91  | Granbull            | Fairy             | 90  | 120 | 75  | 60  | 60  | 45  | 450 |  |
| 92  | Nosepass            | Rock              | 30  | 45  | 135 | 45  | 90  | 30  | 375 |  |
| 93  | Probopass           | Rock/Steel        | 60  | 55  | 145 | 75  | 150 | 40  | 525 |  |
| 94  | Castform            | Normal            | 70  | 70  | 70  | 70  | 70  | 70  | 420 |  |
| 95  | Drifloon            | Ghost/Flying      | 90  | 50  | 34  | 60  | 44  | 70  | 348 |  |
| 96  | Drifblim            | Ghost/Flying      | 150 | 80  | 44  | 90  | 54  | 80  | 498 |  |
| 97  | Yanma               | Bug/Flying        | 65  | 65  | 45  | 75  | 45  | 95  | 390 |  |
| 98  | Yanmega             | Bug/Flying        | 86  | 76  | 86  | 116 | 56  | 95  | 515 |  |
| 99  | Rotom               | Electric/Ghost    | 50  | 50  | 77  | 95  | 77  | 91  | 440 |  |
| 100 | Galarian Yamask     | Ground/Ghost      | 38  | 55  | 85  | 30  | 65  | 30  | 303 |  |
| 101 | Runerigus           | Ground/Ghost      | 58  | 95  | 145 | 50  | 105 | 30  | 483 |  |
| 102 | Vanillite           | Ice               | 36  | 50  | 50  | 65  | 60  | 44  | 305 |  |
| 103 | Vanillish           | Ice               | 51  | 65  | 65  | 80  | 75  | 59  | 395 |  |
| 104 | Vanilluxe           | Ice               | 71  | 95  | 85  | 110 | 95  | 79  | 535 |  |
| 105 | Fletchling          | Normal/Flying     | 45  | 50  | 43  | 40  | 38  | 62  | 278 |  |
| 106 | Fletchinder         | Fire/Flying       | 62  | 73  | 55  | 56  | 52  | 84  | 382 |  |
| 107 | Talonflame          | Fire/Flying       | 78  | 81  | 71  | 74  | 69  | 126 | 499 |  |
| 108 | Espurr              | Psychic           | 62  | 48  | 54  | 63  | 60  | 68  | 355 |  |
| 109 | Meowstic            | Psychic           | 74  | 48  | 76  | 83  | 81  | 104 | 466 |  |
| 110 | Binacle             | Rock/Water        | 42  | 52  | 67  | 39  | 56  | 50  | 306 |  |
| 111 | Barbaracle          | Rock/Water        | 72  | 105 | 115 | 54  | 86  | 68  | 500 |  |
| 112 | Pikipek             | Normal/Flying     | 35  | 75  | 30  | 30  | 30  | 65  | 265 |  |
| 113 | Trumbeak            | Normal/Flying     | 55  | 85  | 50  | 40  | 50  | 75  | 355 |  |
| 114 | Toucannon           | Normal/Flying     | 80  | 120 | 75  | 75  | 75  | 60  | 485 |  |
| 115 | Dewpider            | Water/Bug         | 38  | 40  | 52  | 40  | 72  | 27  | 269 |  |
| 116 | Araquanid           | Water/Bug         | 68  | 70  | 92  | 50  | 132 | 42  | 454 |  |
| 117 | Blipbug             | Bug               | 25  | 20  | 20  | 25  | 45  | 45  | 180 |  |
| 118 | Dottler             | Bug/Psychic       | 50  | 35  | 80  | 50  | 90  | 30  | 335 |  |
| 119 | Orbeetle            | Bug/Psychic       | 60  | 45  | 110 | 80  | 120 | 90  | 505 |  |
| 120 | Clobbopus           | Fighting/Water    | 50  | 68  | 60  | 50  | 50  | 32  | 310 |  |
| 121 | Grapploct           | Fighting/Water    | 80  | 118 | 90  | 70  | 80  | 42  | 480 |  |
| 122 | Smoliv              | Grass/Normal      | 41  | 35  | 45  | 58  | 51  | 30  | 260 |  |
| 123 | Dolliv              | Grass/Normal      | 52  | 53  | 60  | 78  | 78  | 33  | 354 |  |
| 124 | Arboliva            | Grass/Normal      | 78  | 69  | 90  | 125 | 109 | 39  | 510 |  |
| 125 | Klawf               | Rock              | 70  | 100 | 115 | 35  | 55  | 75  | 450 |  |
| 126 | Gimmighoul          | Ghost             | 45  | 30  | 70  | 75  | 70  | 10  | 300 |  |
| 127 | Gholdengo           | Steel/Ghost       | 87  | 60  | 95  | 133 | 91  | 84  | 550 |  |
| 128 | Feebas              | Water             | 20  | 15  | 20  | 10  | 55  | 80  | 200 |  |
| 129 | Milotic             | Water             | 95  | 60  | 79  | 100 | 125 | 81  | 540 |  |
| 130 | Hisuian Basculin    | Water             | 70  | 92  | 65  | 80  | 55  | 98  | 460 |  |
| 131 | Basculegion         | Water/Ghost       | 120 | 112 | 65  | 80  | 75  | 78  | 530 |  |
| 132 | Tirtouga            | Water/Rock        | 54  | 78  | 103 | 53  | 45  | 22  | 355 |  |
| 133 | Carracosta          | Water/Rock        | 74  | 128 | 133 | 83  | 115 | 32  | 565 |  |
| 134 | Archen              | Rock/Flying       | 55  | 112 | 45  | 74  | 45  | 70  | 401 |  |
| 135 | Archeops            | Rock/Flying       | 75  | 140 | 65  | 112 | 65  | 110 | 567 |  |
