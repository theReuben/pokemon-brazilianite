# Regional Dex

This is the definitive list of Pokemon available in Pokemon Brazilianite. All wild encounters, gifts, and static encounters should only use Pokemon from this list.

It is also the source of the in-game Pokedex. After editing the table, run
`python3 dev_scripts/regional_dex_gen.py` to rewrite `enum HoennDexOrder` and
`sHoennToNationalOrder` to match; `--check` reports drift without writing.

The dex is keyed by national dex number, which has no per-form entries, so a
regional form shares its base species' slot - Meowth's three forms are one dex
entry and Persian's two are another, making 150 rows into 147 dex slots.

The list is exactly what the player can get before the post-game.
`python3 dev_scripts/obtainable.py` derives that set from the encounter tables,
statics, gifts, eggs, trades and starters, then closes over evolution and
breeding; it currently agrees with this list entry for entry. Trainer-only
species are deliberately not in this list and do not appear in the Pokedex.

Order: starters first, then roughly the order the player can catch things, then
the paradox pair and the legendaries. `python3 dev_scripts/dex_reorder.py`
rebuilds the middle from encounter levels, moving each family as a block.

## Pokemon List

| #   | Pokemon            | Type              | Family / Notes                  |
|-----|--------------------|-------------------|---------------------------------|
| 1   | Turtwig            | Grass             | Starter                         |
| 2   | Grotle             | Grass             | Starter evolution               |
| 3   | Torterra           | Grass/Ground      | Starter final                   |
| 4   | Fuecoco            | Fire              | Starter                         |
| 5   | Crocalor           | Fire              | Starter evolution               |
| 6   | Skeledirge         | Fire/Ghost        | Starter final                   |
| 7   | Totodile           | Water             | Starter                         |
| 8   | Croconaw           | Water             | Starter evolution               |
| 9   | Feraligatr         | Water             | Starter final                   |
| 10  | Ledyba             | Bug/Flying        |                                 |
| 11  | Ledian             | Bug/Flying        |                                 |
| 12  | Bidoof             | Normal            |                                 |
| 13  | Bibarel            | Normal/Water      |                                 |
| 14  | Nymble             | Bug               |                                 |
| 15  | Lokix              | Bug/Dark          |                                 |
| 16  | Meowth             | Normal            |                                 |
| 17  | Alolan Meowth      | Dark              |                                 |
| 18  | Galarian Meowth    | Steel             |                                 |
| 19  | Persian            | Normal            |                                 |
| 20  | Alolan Persian     | Dark              |                                 |
| 21  | Perrserker         | Steel             |                                 |
| 22  | Fletchling         | Normal/Flying     |                                 |
| 23  | Fletchinder        | Fire/Flying       |                                 |
| 24  | Talonflame         | Fire/Flying       |                                 |
| 25  | Tarountula         | Bug               | "spider ball thing"             |
| 26  | Spidops            | Bug               |                                 |
| 27  | Paldean Wooper     | Poison/Ground     |                                 |
| 28  | Clodsire           | Poison/Ground     |                                 |
| 29  | Pikipek            | Normal/Flying     |                                 |
| 30  | Trumbeak           | Normal/Flying     |                                 |
| 31  | Toucannon          | Normal/Flying     |                                 |
| 32  | Smoliv             | Grass/Normal      |                                 |
| 33  | Dolliv             | Grass/Normal      |                                 |
| 34  | Arboliva           | Grass/Normal      |                                 |
| 35  | Gimmighoul         | Ghost             |                                 |
| 36  | Gholdengo          | Steel/Ghost       |                                 |
| 37  | Snubbull           | Fairy             |                                 |
| 38  | Granbull           | Fairy             |                                 |
| 39  | Blipbug            | Bug               |                                 |
| 40  | Dottler            | Bug/Psychic       |                                 |
| 41  | Orbeetle           | Bug/Psychic       |                                 |
| 42  | Teddiursa          | Normal            |                                 |
| 43  | Ursaring           | Normal            |                                 |
| 44  | Ursaluna           | Ground/Normal     |                                 |
| 45  | Bounsweet          | Grass             |                                 |
| 46  | Steenee            | Grass             |                                 |
| 47  | Tsareena           | Grass             |                                 |
| 48  | Toxel              | Electric/Poison   |                                 |
| 49  | Toxtricity         | Electric/Poison   |                                 |
| 50  | Combee             | Bug/Flying        |                                 |
| 51  | Vespiquen          | Bug/Flying        |                                 |
| 52  | Dewpider           | Water/Bug         |                                 |
| 53  | Araquanid          | Water/Bug         |                                 |
| 54  | Poliwag            | Water             | Poli family                     |
| 55  | Poliwhirl          | Water             | Poli family                     |
| 56  | Poliwrath          | Water/Fighting    | Poli family                     |
| 57  | Politoed           | Water             | Poli family                     |
| 58  | Murkrow            | Dark/Flying       |                                 |
| 59  | Honchkrow          | Dark/Flying       |                                 |
| 60  | Noibat             | Flying/Dragon     |                                 |
| 61  | Noivern            | Flying/Dragon     |                                 |
| 62  | Grubbin            | Bug               |                                 |
| 63  | Charjabug          | Bug/Electric      | "bus"                           |
| 64  | Vikavolt           | Bug/Electric      |                                 |
| 65  | Timburr            | Fighting          |                                 |
| 66  | Gurdurr            | Fighting          |                                 |
| 67  | Conkeldurr         | Fighting          |                                 |
| 68  | Solosis            | Psychic           | "cell"                          |
| 69  | Duosion            | Psychic           | "two cell"                      |
| 70  | Reuniclus          | Psychic           |                                 |
| 71  | Alolan Geodude     | Rock/Electric     |                                 |
| 72  | Alolan Graveler    | Rock/Electric     |                                 |
| 73  | Alolan Golem       | Rock/Electric     |                                 |
| 74  | Galarian Farfetch'd | Fighting          |                                 |
| 75  | Sirfetch'd         | Fighting          |                                 |
| 76  | Elekid             | Electric          |                                 |
| 77  | Electabuzz         | Electric          |                                 |
| 78  | Electivire         | Electric          |                                 |
| 79  | Nosepass           | Rock              |                                 |
| 80  | Probopass          | Rock/Steel        |                                 |
| 81  | Hisuian Voltorb    | Electric/Grass    |                                 |
| 82  | Hisuian Electrode  | Electric/Grass    |                                 |
| 83  | Drifloon           | Ghost/Flying      |                                 |
| 84  | Drifblim           | Ghost/Flying      |                                 |
| 85  | Galarian Yamask    | Ground/Ghost      |                                 |
| 86  | Runerigus          | Ground/Ghost      |                                 |
| 87  | Binacle            | Rock/Water        |                                 |
| 88  | Barbaracle         | Rock/Water        |                                 |
| 89  | Clobbopus          | Fighting          |                                 |
| 90  | Grapploct          | Fighting          |                                 |
| 91  | Pansage            | Grass             | Elemental monkey                |
| 92  | Simisage           | Grass             | Elemental monkey                |
| 93  | Pansear            | Fire              | Elemental monkey                |
| 94  | Simisear           | Fire              | Elemental monkey                |
| 95  | Panpour            | Water             | Elemental monkey                |
| 96  | Simipour           | Water             | Elemental monkey                |
| 97  | Hippopotas         | Ground            |                                 |
| 98  | Hippowdon          | Ground            |                                 |
| 99  | Glimmet            | Rock/Poison       |                                 |
| 100 | Glimmora           | Rock/Poison       |                                 |
| 101 | Alolan Grimer      | Poison/Dark       |                                 |
| 102 | Alolan Muk         | Poison/Dark       |                                 |
| 103 | Magby              | Fire              |                                 |
| 104 | Magmar             | Fire              |                                 |
| 105 | Magmortar          | Fire              |                                 |
| 106 | Klawf              | Rock              |                                 |
| 107 | Tirtouga           | Water/Rock        | Cover Fossil, Devon Corp        |
| 108 | Carracosta         | Water/Rock        | Cover Fossil line               |
| 109 | Archen             | Rock/Flying       | Plume Fossil, Devon Corp        |
| 110 | Archeops           | Rock/Flying       | Plume Fossil line               |
| 111 | Galarian Slowpoke  | Psychic           |                                 |
| 112 | Galarian Slowbro   | Poison/Psychic    |                                 |
| 113 | Galarian Slowking  | Poison/Psychic    |                                 |
| 114 | Espurr             | Psychic           |                                 |
| 115 | Meowstic           | Psychic           |                                 |
| 116 | Spheal             | Ice/Water         |                                 |
| 117 | Sealeo             | Ice/Water         |                                 |
| 118 | Walrein            | Ice/Water         |                                 |
| 119 | Orthworm           | Steel             |                                 |
| 120 | Castform           | Normal            | Gift at Weather Institute       |
| 121 | Vanillite          | Ice               |                                 |
| 122 | Vanillish          | Ice               |                                 |
| 123 | Vanilluxe          | Ice               |                                 |
| 124 | Tropius            | Grass/Flying      |                                 |
| 125 | Kecleon            | Normal            | Static, Route 120               |
| 126 | Porygon            | Normal            | Static, Aqua Hideout            |
| 127 | Porygon2           | Normal            |                                 |
| 128 | Porygon-Z          | Normal            |                                 |
| 129 | Yanma              | Bug/Flying        |                                 |
| 130 | Yanmega            | Bug/Flying        |                                 |
| 131 | Hisuian Basculin   | Water             |                                 |
| 132 | Basculegion        | Water/Ghost       |                                 |
| 133 | Hisuian Qwilfish   | Dark/Poison       |                                 |
| 134 | Overqwil           | Dark/Poison       |                                 |
| 135 | Feebas             | Water             |                                 |
| 136 | Milotic            | Water             |                                 |
| 137 | Rotom              | Electric/Ghost    |                                 |
| 138 | Roaring Moon       | Dragon/Dark       | Paradox                         |
| 139 | Iron Valiant       | Fairy/Fighting    | Paradox                         |
| 140 | Raikou             | Electric          | Beast Den, one of three         |
| 141 | Entei              | Fire              | Beast Den, one of three         |
| 142 | Suicune            | Water             | Beast Den, one of three         |
| 143 | Galarian Articuno  | Psychic/Flying    | Storm Roost, one of three       |
| 144 | Galarian Zapdos    | Fighting/Flying   | Storm Roost, one of three       |
| 145 | Galarian Moltres   | Dark/Flying       | Storm Roost, one of three       |
| 146 | Tapu Koko          | Electric/Fairy    | Tapu Grotto, one of four        |
| 147 | Tapu Lele          | Psychic/Fairy     | Tapu Grotto, one of four        |
| 148 | Tapu Bulu          | Grass/Fairy       | Tapu Grotto, one of four        |
| 149 | Tapu Fini          | Water/Fairy       | Tapu Grotto, one of four        |
| 150 | Rayquaza           | Dragon/Flying     | Sky Pillar                      |

## Summary

- **Total**: 150 Pokemon
- **Starters**: 3 lines (Turtwig, Fuecoco, Totodile)
- **Regional forms**: Alolan (Grimer, Muk, Meowth, Persian, Geodude, Graveler, Golem), Galarian (Slowpoke, Slowbro, Slowking, Meowth, Perrserker, Farfetch'd, Yamask), Hisuian (Qwilfish, Voltorb, Electrode, Basculin), Paldean (Wooper)
- **Paradox Pokemon**: Roaring Moon, Iron Valiant
- **Gift Pokemon**: Castform (Weather Institute), Tirtouga, Archen
- **Legendaries**: one of Raikou/Entei/Suicune, one of the Galarian birds, one of the tapus, plus Rayquaza
- **Fossils**: Cover Fossil (Tirtouga) and Plume Fossil (Archen), revived at Devon Corp
