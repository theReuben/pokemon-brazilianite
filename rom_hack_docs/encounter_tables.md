# Pokemon Encounters by Route

> Encounters are distributed across Emerald's routes to match the original game's power scaling and progression. Regional variants, cross-gen evolutions, and newer Pokemon are placed thematically alongside the route environments (desert, volcanic, forest, water, etc.).

> **Note:** This document reflects the actual encounter data in `wild_encounters.json`. FR/LG (Kanto) areas are not included.

## Slot System Reference

All encounter slots are fixed by the engine. Every slot must be assigned a Pokemon — unassigned slots repeat the first Pokemon. Rates shown are cumulative across all slots a Pokemon occupies.

| Encounter Type | Slots | Slot Rates |
|----------------|-------|------------|
| Grass / Cave   | 12    | 1:20, 2:20, 3:10, 4:10, 5:10, 6:10, 7:5, 8:5, 9:4, 10:4, 11:1, 12:1 |
| Surf           | 5     | 1:60, 2:30, 3:5, 4:4, 5:1 |
| Rock Smash     | 5     | 1:60, 2:30, 3:5, 4:4, 5:1 |

Fishing uses a shared pool of **10 slots** split across three rods. Slot numbers in the area tables below use this global numbering:

| Rod       | Slots | Slot Rates |
|-----------|-------|------------|
| Old Rod   | 1-2   | 1:70, 2:30 |
| Good Rod  | 3-5   | 3:60, 4:20, 5:20 |
| Super Rod | 6-10  | 6:40, 7:40, 8:15, 9:4, 10:1 |

-----

## Starters

The player chooses one of three starter Pokemon at the beginning of their journey:

|Pokemon |Type |Evolution 1     |Evolution 2       |
|--------|-----|----------------|------------------|
|Turtwig |Grass|Grotle (Lv 18)  |Torterra (Lv 32)  |
|Fuecoco |Fire |Crocalor (Lv 16)|Skeledirge (Lv 36)|
|Totodile|Water|Croconaw (Lv 18)|Feraligatr (Lv 30)|

-----

## Early Game (Badges 0-1)

### Route 101

*Littleroot Town to Oldale Town — Simple grassy path, a trainer's first steps.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Bidoof|Normal|Grass|2-4|1-2|40%|
|Fletchling|Normal/Flying|Grass|2-4|3-4|20%|
|Ledyba|Bug/Flying|Grass|2-4|5-6|20%|
|Nymble|Bug|Grass|2-4|7-8|10%|
|Meowth|Normal|Grass|2-4|9-12|10%|

-----

### Route 102

*Oldale Town to Petalburg City — Gentle route with ponds and tall grass.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Smoliv|Grass/Normal|Grass|3-5|1-2|40%|
|Tarountula|Bug|Grass|3-5|3-4|20%|
|Pikipek|Normal/Flying|Grass|3-5|5-6|20%|
|Paldean Wooper|Poison/Ground|Grass|3-5|7-12|20%|
|Dewpider|Water/Bug|Surf|3-8|1|60%|
|Poliwag|Water|Surf|3-8|2|30%|
|Araquanid|Water/Bug|Surf|3-8|3|5%|
|Poliwhirl|Water|Surf|3-8|4|4%|
|Bibarel|Normal/Water|Surf|3-8|5|1%|
|Poliwag|Water|Old Rod|3-5|1-2|100%|
|Poliwag|Water|Good Rod|3-5|3-5|100%|
|Poliwhirl|Water|Super Rod|5-10|6-7|80%|
|Araquanid|Water/Bug|Super Rod|8-15|8|15%|
|Dewpider|Water/Bug|Super Rod|5-10|9-10|5%|

-----

### Route 103

*North of Oldale Town — Grassy headland with water access.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Snubbull|Fairy|Grass|4-6|1-4|60%|
|Blipbug|Bug|Grass|4-6|5-8|30%|
|Alolan Meowth|Dark|Grass|4-6|9-12|10%|
|Dewpider|Water/Bug|Surf|5-15|1|60%|
|Binacle|Rock/Water|Surf|5-15|2|30%|
|Poliwag|Water|Surf|5-15|3|5%|
|Clobbopus|Fighting|Surf|5-15|4|4%|
|Araquanid|Water/Bug|Surf|5-15|5|1%|
|Poliwag|Water|Old Rod|5-10|1-2|100%|
|Clobbopus|Fighting|Good Rod|8-15|3-4|80%|
|Binacle|Rock/Water|Good Rod|8-15|5|20%|
|Barbaracle|Rock/Water|Super Rod|10-15|6-7|80%|
|Grapploct|Fighting|Super Rod|10-15|8|15%|
|Araquanid|Water/Bug|Super Rod|10-15|9-10|5%|

-----

### Route 104

*Petalburg City to Rustboro City (South) — Coastal path with sandy beaches and flower patches.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Bounsweet|Grass|Grass|5-8|1-2|40%|
|Combee|Bug/Flying|Grass|5-8|3-6|40%|
|Teddiursa|Normal|Grass|5-8|7-10|18%|
|Dewpider|Water/Bug|Grass|5-8|11-12|2%|
|Dewpider|Water/Bug|Surf|5-8|1|60%|
|Poliwag|Water|Surf|5-8|2|30%|
|Dewpider|Water/Bug|Surf|5-8|3-5|10%|
|Poliwag|Water|Old Rod|5-8|1-2|100%|
|Poliwag|Water|Good Rod|5-8|3-4|80%|
|Dewpider|Water/Bug|Good Rod|5-8|5|20%|
|Dewpider|Water/Bug|Super Rod|5-8|6-7|80%|
|Araquanid|Water/Bug|Super Rod|8-15|8|15%|
|Poliwhirl|Water|Super Rod|8-12|9-10|5%|

-----

### Petalburg Woods

*Dense forest between the two halves of Route 104 — Dark canopy, bug-type haven.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Grubbin|Bug|Grass|6-9|1-2|40%|
|Tarountula|Bug|Grass|6-9|3-4|20%|
|Murkrow|Dark/Flying|Grass|6-9|5-6|20%|
|Noibat|Flying/Dragon|Grass|6-9|7-8|10%|
|Toxel|Electric/Poison|Grass|7-9|9-12|10%|

-----

## Pre-3rd Badge

### Route 116

*Rustboro City to Rusturf Tunnel — Rocky terrain near the quarry and tunnel entrance.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Alolan Geodude|Rock/Electric|Grass|8-11|1-2|40%|
|Nosepass|Rock|Grass|8-11|3-4|20%|
|Galarian Farfetch'd|Fighting|Grass|8-11|5-6|20%|
|Galarian Meowth|Steel|Grass|8-10|7-8|10%|
|Hisuian Voltorb|Electric/Grass|Grass|9-11|9-12|10%|

-----

### Rusturf Tunnel

*Cave connecting Route 116 and Verdanturf Town — Dusty, partially collapsed construction site.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Timburr|Fighting|Cave|8-12|1-2|40%|
|Solosis|Psychic|Cave|8-11|3-4|20%|
|Drifloon|Ghost/Flying|Cave|9-12|5-6|20%|
|Galarian Yamask|Ground/Ghost|Cave|9-12|7-8|10%|
|Elekid|Electric|Cave|8-11|9-12|10%|

-----

### Granite Cave 1F

*Cave near Dewford Town — Dark cave with rare Pokemon.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Noibat|Flying/Dragon|Cave|8-12|1-4|60%|
|Timburr|Fighting|Cave|8-12|5-8|30%|
|Alolan Geodude|Rock/Electric|Cave|9-12|9-10|8%|
|Nosepass|Rock|Cave|9-12|11|1%|
|Noibat|Flying/Dragon|Cave|10-13|12|1%|

-----

### Granite Cave B1F

*Deeper level of Granite Cave — Rock formations and nesting bats.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Noibat|Flying/Dragon|Cave|9-13|1-4|60%|
|Alolan Geodude|Rock/Electric|Cave|9-13|5-8|30%|
|Timburr|Fighting|Cave|9-13|9-10|8%|
|Nosepass|Rock|Cave|10-13|11|1%|
|Noibat|Flying/Dragon|Cave|11-14|12|1%|
|Alolan Geodude|Rock/Electric|Rock Smash|8-13|1|60%|
|Nosepass|Rock|Rock Smash|10-13|2|30%|
|Alolan Geodude|Rock/Electric|Rock Smash|8-13|3-5|10%|

-----

### Granite Cave B2F

*Deepest level of Granite Cave — Where Steven trains.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Noibat|Flying/Dragon|Cave|9-14|1-4|60%|
|Alolan Geodude|Rock/Electric|Cave|9-14|5-8|30%|
|Timburr|Fighting|Cave|9-14|9-10|8%|
|Nosepass|Rock|Cave|10-14|11|1%|
|Solosis|Psychic|Cave|10-13|12|1%|
|Alolan Geodude|Rock/Electric|Rock Smash|8-13|1|60%|
|Nosepass|Rock|Rock Smash|10-13|2|30%|
|Alolan Geodude|Rock/Electric|Rock Smash|8-13|3-5|10%|

-----

### Route 110

*Slateport City to Mauville City — Long route with the Cycling Road overpass.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Bibarel|Normal/Water|Grass|16-19|1-2|40%|
|Ledian|Bug/Flying|Grass|16-18|3-5|30%|
|Trumbeak|Normal/Flying|Grass|16-19|6-8|20%|
|Spidops|Bug|Grass|16-18|9-12|10%|
|Dewpider|Water/Bug|Surf|15-30|1|60%|
|Binacle|Rock/Water|Surf|15-30|2|30%|
|Poliwag|Water|Surf|15-30|3|5%|
|Clobbopus|Fighting|Surf|15-30|4|4%|
|Araquanid|Water/Bug|Surf|15-30|5|1%|
|Poliwag|Water|Old Rod|15-20|1-2|100%|
|Clobbopus|Fighting|Good Rod|18-25|3-4|80%|
|Binacle|Rock/Water|Good Rod|18-25|5|20%|
|Barbaracle|Rock/Water|Super Rod|20-25|6-7|80%|
|Grapploct|Fighting|Super Rod|20-25|8|15%|
|Araquanid|Water/Bug|Super Rod|20-25|9-10|5%|

-----

### Route 117

*Mauville City to Verdanturf Town — Lush flower fields near the Pokemon Day Care.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Steenee|Grass|Grass|17-20|1-2|40%|
|Pansage|Grass|Grass|17-20|3-4|20%|
|Pansear|Fire|Grass|17-20|5-6|20%|
|Panpour|Water|Grass|17-20|7-8|10%|
|Dolliv|Grass/Normal|Grass|17-20|9-12|10%|
|Dewpider|Water/Bug|Surf|17-25|1|60%|
|Poliwag|Water|Surf|17-25|2|30%|
|Araquanid|Water/Bug|Surf|17-25|3|5%|
|Poliwhirl|Water|Surf|17-25|4|4%|
|Bibarel|Normal/Water|Surf|17-25|5|1%|
|Poliwag|Water|Old Rod|17-22|1-2|100%|
|Poliwag|Water|Good Rod|19-25|3|60%|
|Poliwhirl|Water|Good Rod|20-25|4-5|40%|
|Poliwhirl|Water|Super Rod|22-25|6-7|80%|
|Araquanid|Water/Bug|Super Rod|22-25|8|15%|
|Dewpider|Water/Bug|Super Rod|20-25|9-10|5%|

-----

## Mid Game (Badges 3-5)

### Route 111

*North of Mauville City — Scorching desert with perpetual sandstorm.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Hippopotas|Ground|Grass|22-26|1-2|40%|
|Klawf|Rock|Grass|22-25|3-4|20%|
|Orthworm|Steel|Grass|23-26|5-6|20%|
|Alolan Graveler|Rock/Electric|Grass|22-25|7-8|10%|
|Hippowdon|Ground|Grass|24-26|9-12|10%|
|Dewpider|Water/Bug|Surf|20-30|1|60%|
|Poliwag|Water|Surf|20-30|2|30%|
|Araquanid|Water/Bug|Surf|20-30|3|5%|
|Poliwhirl|Water|Surf|20-30|4|4%|
|Bibarel|Normal/Water|Surf|20-30|5|1%|
|Poliwag|Water|Old Rod|20-25|1-2|100%|
|Poliwag|Water|Good Rod|22-30|3|60%|
|Poliwhirl|Water|Good Rod|23-30|4-5|40%|
|Poliwhirl|Water|Super Rod|25-30|6-7|80%|
|Araquanid|Water/Bug|Super Rod|25-30|8|15%|
|Dewpider|Water/Bug|Super Rod|23-30|9-10|5%|
|Alolan Geodude|Rock/Electric|Rock Smash|10-15|1|60%|
|Nosepass|Rock|Rock Smash|10-15|2|30%|
|Alolan Geodude|Rock/Electric|Rock Smash|10-15|3-5|10%|

-----

### Fiery Path

*Volcanic tunnel on Route 112 — Geothermal vents and magma-warmed stone.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Glimmet|Rock/Poison|Cave|20-24|1-5|70%|
|Alolan Geodude|Rock/Electric|Cave|20-23|6-12|30%|

-----

### Route 112

*Route to Mt. Chimney — Volcanic slopes with sulfurous vents and ashen soil.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Alolan Grimer|Poison/Dark|Grass|20-24|1-2|40%|
|Magby|Fire|Grass|20-24|3-8|50%|
|Simisear|Fire|Grass|22-24|9-12|10%|

-----

### Jagged Pass

*Descent from Mt. Chimney — Steep volcanic slopes with loose rock.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Magby|Fire|Grass|21-21|1-2|40%|
|Klawf|Rock|Grass|21-21|3|10%|
|Magby|Fire|Grass|20-20|4|10%|
|Solosis|Psychic|Grass|20-20|5|10%|
|Klawf|Rock|Grass|20-20|6|10%|
|Solosis|Psychic|Grass|21-21|7|5%|
|Klawf|Rock|Grass|22-22|8|5%|
|Magby|Fire|Grass|22-22|9|4%|
|Solosis|Psychic|Grass|22-22|10|4%|
|Magby|Fire|Grass|22-22|11|1%|
|Solosis|Psychic|Grass|22-22|12|1%|

-----

### Route 113

*Fallarbor Town approach — Blanketed in volcanic ash, an eerie grey landscape.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Espurr|Psychic|Grass|21-25|1-2|40%|
|Magmar|Fire|Grass|22-25|3-4|20%|
|Galarian Slowpoke|Psychic|Grass|21-25|5-6|20%|
|Dottler|Bug/Psychic|Grass|21-24|7-8|10%|
|Gimmighoul|Ghost|Grass|23-25|9-12|10%|

-----

### Route 114

*Fallarbor Town to Meteor Falls — Rugged terrain with waterfalls and rocky pools.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Spheal|Ice/Water|Grass|22-27|1-4|60%|
|Gurdurr|Fighting|Grass|23-27|5-8|30%|
|Clobbopus|Fighting|Grass|22-25|9-12|10%|
|Spheal|Ice/Water|Surf|22-27|1|60%|
|Poliwhirl|Water|Surf|23-27|2|30%|
|Clobbopus|Fighting|Surf|22-25|3|5%|
|Spheal|Ice/Water|Surf|22-27|4-5|5%|
|Poliwag|Water|Old Rod|22-27|1-2|100%|
|Poliwag|Water|Good Rod|22-27|3|60%|
|Poliwhirl|Water|Good Rod|23-27|4-5|40%|
|Spheal|Ice/Water|Super Rod|22-27|6-7|80%|
|Clobbopus|Fighting|Super Rod|22-25|8|15%|
|Grapploct|Fighting|Super Rod|23-27|9-10|5%|
|Alolan Geodude|Rock/Electric|Rock Smash|20-25|1|60%|
|Nosepass|Rock|Rock Smash|22-25|2|30%|
|Alolan Geodude|Rock/Electric|Rock Smash|20-25|3-5|10%|

-----

### Meteor Falls

*Ancient cave system with falling water — Rare Pokemon and fossils.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Noibat|Flying/Dragon|Cave|16-16|1|20%|
|Noibat|Flying/Dragon|Cave|17-17|2|20%|
|Noibat|Flying/Dragon|Cave|18-18|3|10%|
|Noibat|Flying/Dragon|Cave|15-15|4|10%|
|Noibat|Flying/Dragon|Cave|14-14|5|10%|
|Gimmighoul|Ghost|Cave|16-16|6|10%|
|Gimmighoul|Ghost|Cave|18-18|7|5%|
|Gimmighoul|Ghost|Cave|14-14|8|5%|
|Noibat|Flying/Dragon|Cave|19-19|9|4%|
|Noibat|Flying/Dragon|Cave|20-20|10|4%|
|Noibat|Flying/Dragon|Cave|19-19|11|1%|
|Noibat|Flying/Dragon|Cave|20-20|12|1%|
|Noibat|Flying/Dragon|Surf|20-30|1|60%|
|Noivern|Flying/Dragon|Surf|25-35|2|30%|
|Gimmighoul|Ghost|Surf|20-30|3|5%|
|Spheal|Ice/Water|Surf|20-30|4|4%|
|Clobbopus|Fighting|Surf|20-30|5|1%|
|Poliwag|Water|Old Rod|5-10|1-2|100%|
|Poliwag|Water|Good Rod|10-30|3-4|80%|
|Poliwhirl|Water|Good Rod|10-30|5|20%|
|Poliwhirl|Water|Super Rod|25-30|6|40%|
|Poliwhirl|Water|Super Rod|30-35|7|40%|
|Poliwhirl|Water|Super Rod|20-25|8|15%|
|Poliwhirl|Water|Super Rod|35-40|9|4%|
|Poliwhirl|Water|Super Rod|40-45|10|1%|

-----

### Route 115

*North of Rustboro City — Rocky coastal cliffs accessible via Surf.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Granbull|Fairy|Grass|27-30|1-8|90%|
|Simisage|Grass|Grass|28-31|9-12|10%|
|Binacle|Rock/Water|Surf|27-30|1|60%|
|Hisuian Qwilfish|Dark/Poison|Surf|27-31|2|30%|
|Simipour|Water|Surf|28-31|3|5%|
|Binacle|Rock/Water|Surf|27-30|4-5|5%|
|Poliwag|Water|Old Rod|27-32|1-2|100%|
|Clobbopus|Fighting|Good Rod|30-35|3-4|80%|
|Binacle|Rock/Water|Good Rod|30-35|5|20%|
|Barbaracle|Rock/Water|Super Rod|32-35|6-7|80%|
|Grapploct|Fighting|Super Rod|32-35|8|15%|
|Araquanid|Water/Bug|Super Rod|32-35|9-10|5%|
|Binacle|Rock/Water|Rock Smash|27-30|1|60%|
|Nosepass|Rock|Rock Smash|27-30|2|30%|
|Binacle|Rock/Water|Rock Smash|27-30|3-5|10%|

-----

### New Mauville (Entrance)

*Decommissioned power plant beneath Mauville City — Electric-type habitat (entrance area).*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Hisuian Voltorb|Electric/Grass|Cave|24-24|1|20%|
|Elekid|Electric|Cave|24-24|2|20%|
|Hisuian Voltorb|Electric/Grass|Cave|25-25|3|10%|
|Elekid|Electric|Cave|25-25|4|10%|
|Hisuian Voltorb|Electric/Grass|Cave|23-23|5|10%|
|Elekid|Electric|Cave|23-23|6|10%|
|Hisuian Voltorb|Electric/Grass|Cave|26-26|7|5%|
|Elekid|Electric|Cave|26-26|8|5%|
|Hisuian Voltorb|Electric/Grass|Cave|22-22|9|4%|
|Elekid|Electric|Cave|22-22|10|4%|
|Hisuian Voltorb|Electric/Grass|Cave|22-22|11|1%|
|Elekid|Electric|Cave|22-22|12|1%|

-----

### New Mauville (Inside)

*Deeper interior of the power plant — Rare Electric-types prowl the generator rooms.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Hisuian Voltorb|Electric/Grass|Cave|24-24|1|20%|
|Elekid|Electric|Cave|24-24|2|20%|
|Hisuian Voltorb|Electric/Grass|Cave|25-25|3|10%|
|Elekid|Electric|Cave|25-25|4|10%|
|Hisuian Voltorb|Electric/Grass|Cave|23-23|5|10%|
|Elekid|Electric|Cave|23-23|6|10%|
|Hisuian Voltorb|Electric/Grass|Cave|26-26|7|5%|
|Elekid|Electric|Cave|26-26|8|5%|
|Hisuian Voltorb|Electric/Grass|Cave|22-22|9|4%|
|Elekid|Electric|Cave|22-22|10|4%|
|Hisuian Electrode|Electric/Grass|Cave|26-26|11|1%|
|Electabuzz|Electric|Cave|26-26|12|1%|

-----

## Mid-Late Game (Badges 5-6)

### Route 118

*East of Mauville City — Grassy route split by a wide river.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Charjabug|Bug/Electric|Grass|28-31|1-2|40%|
|Fletchinder|Fire/Flying|Grass|28-31|3-4|20%|
|Electabuzz|Electric|Grass|28-32|5-6|20%|
|Duosion|Psychic|Grass|29-32|7-8|10%|
|Persian|Normal|Grass|29-32|9-12|10%|
|Hisuian Basculin|Water|Surf|28-32|1|60%|
|Poliwag|Water|Surf|28-32|2|30%|
|Dewpider|Water/Bug|Surf|28-32|3|5%|
|Araquanid|Water/Bug|Surf|28-32|4|4%|
|Poliwhirl|Water|Surf|28-32|5|1%|
|Poliwag|Water|Old Rod|28-32|1-2|100%|
|Poliwag|Water|Good Rod|28-32|3|60%|
|Poliwhirl|Water|Good Rod|29-32|4-5|40%|
|Hisuian Basculin|Water|Super Rod|28-32|6-7|80%|
|Araquanid|Water/Bug|Super Rod|28-32|8|15%|
|Poliwhirl|Water|Super Rod|29-32|9|4%|
|Dewpider|Water/Bug|Super Rod|28-32|10|1%|

-----

### Route 119

*Mauville to Fortree City — Long, rain-soaked jungle route with the Weather Institute.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Ursaring|Normal|Grass|30-34|1-2|40%|
|Lokix|Bug/Dark|Grass|30-33|3-6|40%|
|Tropius|Grass/Flying|Grass|30-34|7-8|10%|
|Toxtricity|Electric/Poison|Grass|31-34|9-10|8%|
|Vespiquen|Bug/Flying|Grass|31-34|11-12|2%|
|Hisuian Basculin|Water|Surf|30-34|1|60%|
|Dewpider|Water/Bug|Surf|30-34|2|30%|
|Araquanid|Water/Bug|Surf|30-34|3|5%|
|Poliwhirl|Water|Surf|30-34|4|4%|
|Feebas|Water|Surf|30-33|5|1%|
|Poliwag|Water|Old Rod|30-33|1-2|100%|
|Poliwhirl|Water|Good Rod|30-33|3-4|80%|
|Feebas|Water|Good Rod|30-33|5|20%|
|Feebas|Water|Super Rod|30-33|6-8|95%|
|Milotic|Water|Super Rod|31-34|9-10|5%|

-----

### Weather Institute

*Inside Route 119 — Research facility studying weather patterns. Castform is given as a gift by a grateful researcher after clearing the institute of Team Magma/Aqua.*

|Pokemon |Type  |Encounter    |Level|Slots|Rate|
|--------|------|-------------|-----|-----|----|
|Castform|Normal|Gift (Static)|25   |—    |1×  |

-----

### Route 120

*Fortree City area — Misty route with tall grass and ancient bridges.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Yanma|Bug/Flying|Grass|31-34|1-2|40%|
|Perrserker|Steel|Grass|31-34|3-4|20%|
|Drifblim|Ghost/Flying|Grass|31-35|5-6|20%|
|Vikavolt|Bug/Electric|Grass|31-35|7-8|10%|
|Hisuian Electrode|Electric/Grass|Grass|32-35|9-12|10%|
|Dewpider|Water/Bug|Surf|31-38|1|60%|
|Poliwag|Water|Surf|31-38|2|30%|
|Araquanid|Water/Bug|Surf|31-38|3|5%|
|Poliwhirl|Water|Surf|31-38|4|4%|
|Bibarel|Normal/Water|Surf|31-38|5|1%|
|Poliwag|Water|Old Rod|31-36|1-2|100%|
|Poliwag|Water|Good Rod|33-38|3|60%|
|Poliwhirl|Water|Good Rod|34-38|4-5|40%|
|Poliwhirl|Water|Super Rod|36-38|6-7|80%|
|Araquanid|Water/Bug|Super Rod|36-38|8|15%|
|Dewpider|Water/Bug|Super Rod|34-38|9-10|5%|

-----

### Route 121

*Fortree to Lilycove City — Wide grassy plains leading to the coast.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Honchkrow|Dark/Flying|Grass|33-37|1-4|60%|
|Tsareena|Grass|Grass|33-37|5-8|30%|
|Vanillish|Ice|Grass|33-36|9-12|10%|
|Hisuian Qwilfish|Dark/Poison|Surf|33-37|1|60%|
|Hisuian Basculin|Water|Surf|33-37|2|30%|
|Overqwil|Dark/Poison|Surf|33-37|3|5%|
|Poliwhirl|Water|Surf|33-37|4|4%|
|Dewpider|Water/Bug|Surf|33-37|5|1%|
|Poliwag|Water|Old Rod|33-37|1-2|100%|
|Poliwhirl|Water|Good Rod|33-37|3-4|80%|
|Hisuian Qwilfish|Dark/Poison|Good Rod|33-37|5|20%|
|Hisuian Qwilfish|Dark/Poison|Super Rod|33-37|6-7|80%|
|Overqwil|Dark/Poison|Super Rod|33-37|8|15%|
|Hisuian Basculin|Water|Super Rod|33-37|9|4%|
|Araquanid|Water/Bug|Super Rod|33-37|10|1%|

-----

## Late Game (Badges 6-8)

### Route 122

*Water route to Mt. Pyre — Somber waters surrounding the sacred mountain.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Galarian Slowbro|Poison/Psychic|Surf|34-38|1|60%|
|Hisuian Qwilfish|Dark/Poison|Surf|34-38|2|30%|
|Poliwhirl|Water|Surf|34-38|3|5%|
|Galarian Slowbro|Poison/Psychic|Surf|34-38|4-5|5%|
|Poliwhirl|Water|Old Rod|34-38|1-2|100%|
|Poliwhirl|Water|Good Rod|34-38|3|60%|
|Hisuian Qwilfish|Dark/Poison|Good Rod|34-38|4-5|40%|
|Hisuian Qwilfish|Dark/Poison|Super Rod|34-38|6-7|80%|
|Overqwil|Dark/Poison|Super Rod|35-38|8|15%|
|Poliwrath|Water/Fighting|Super Rod|35-38|9|4%|
|Galarian Slowbro|Poison/Psychic|Super Rod|34-38|10|1%|

-----

### Mt. Pyre (Interior)

*Sacred mountain for departed Pokemon — Ghostly atmosphere (Floors 1F–6F).*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Probopass|Rock/Steel|Cave|35-38|1-5|70%|
|Galarian Yamask|Ground/Ghost|Cave|35-38|6-12|30%|

-----

### Mt. Pyre (Exterior)

*Outside grounds of Mt. Pyre — Grassy cliffs overlooking the sea.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Alolan Persian|Dark|Grass|35-38|1-4|60%|
|Meowstic|Psychic|Grass|34-37|5-8|30%|
|Runerigus|Ground/Ghost|Grass|34-38|9-12|10%|

-----

### Route 123

*East of Mt. Pyre to Route 118 — Berry-rich grasslands along the coast.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Alolan Muk|Poison/Dark|Grass|33-37|1-4|60%|
|Arboliva|Grass/Normal|Grass|33-37|5-8|30%|
|Toucannon|Normal/Flying|Grass|33-36|9-10|8%|
|Sirfetch'd|Fighting|Grass|34-37|11-12|2%|
|Hisuian Basculin|Water|Surf|33-37|1|60%|
|Poliwhirl|Water|Surf|33-37|2|30%|
|Hisuian Basculin|Water|Surf|33-37|3-5|10%|
|Poliwag|Water|Old Rod|33-37|1-2|100%|
|Poliwhirl|Water|Good Rod|33-37|3-4|80%|
|Hisuian Basculin|Water|Good Rod|33-37|5|20%|
|Hisuian Basculin|Water|Super Rod|33-37|6-7|80%|
|Politoed|Water|Super Rod|35-38|8|15%|
|Basculegion|Water/Ghost|Super Rod|35-38|9|4%|
|Araquanid|Water/Bug|Super Rod|35-38|10|1%|

-----

### Route 124

*Lilycove to Mossdeep — Deep ocean route with dive spots.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Poliwrath|Water/Fighting|Surf|35-40|1|60%|
|Barbaracle|Rock/Water|Surf|35-40|2|30%|
|Araquanid|Water/Bug|Surf|35-39|3|5%|
|Milotic|Water|Surf|35-40|4|4%|
|Poliwrath|Water/Fighting|Surf|35-40|5|1%|
|Poliwag|Water|Old Rod|35-40|1-2|100%|
|Poliwhirl|Water|Good Rod|35-40|3|60%|
|Clobbopus|Fighting|Good Rod|35-40|4-5|40%|
|Barbaracle|Rock/Water|Super Rod|35-40|6-7|80%|
|Grapploct|Fighting|Super Rod|35-40|8|15%|
|Araquanid|Water/Bug|Super Rod|35-39|9|4%|
|Milotic|Water|Super Rod|35-40|10|1%|

-----

### Route 125

*Waters near Shoal Cave — Cold currents and rocky shallows.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Sealeo|Ice/Water|Surf|35-40|1|60%|
|Grapploct|Fighting|Surf|35-39|2|30%|
|Galarian Slowking|Poison/Psychic|Surf|35-40|3|5%|
|Sealeo|Ice/Water|Surf|35-40|4-5|5%|
|Poliwag|Water|Old Rod|35-40|1-2|100%|
|Spheal|Ice/Water|Good Rod|35-40|3-4|80%|
|Clobbopus|Fighting|Good Rod|35-40|5|20%|
|Sealeo|Ice/Water|Super Rod|35-40|6-7|80%|
|Grapploct|Fighting|Super Rod|35-39|8|15%|
|Walrein|Ice/Water|Super Rod|35-40|9|4%|
|Galarian Slowking|Poison/Psychic|Super Rod|35-40|10|1%|

-----

### Shoal Cave

*Tidal cave near Mossdeep — Ice Pokemon habitat that changes with the tides.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Noibat|Flying/Dragon|Cave|26-26|1|20%|
|Spheal|Ice/Water|Cave|26-26|2|20%|
|Noibat|Flying/Dragon|Cave|28-28|3|10%|
|Spheal|Ice/Water|Cave|28-28|4|10%|
|Noibat|Flying/Dragon|Cave|30-30|5|10%|
|Spheal|Ice/Water|Cave|30-30|6|10%|
|Noibat|Flying/Dragon|Cave|32-32|7|5%|
|Spheal|Ice/Water|Cave|32-32|8|5%|
|Noivern|Flying/Dragon|Cave|32-32|9|4%|
|Spheal|Ice/Water|Cave|32-32|10|4%|
|Noivern|Flying/Dragon|Cave|32-32|11|1%|
|Spheal|Ice/Water|Cave|32-32|12|1%|
|Spheal|Ice/Water|Surf|30-40|1|60%|
|Sealeo|Ice/Water|Surf|32-42|2|30%|
|Walrein|Ice/Water|Surf|35-45|3|5%|
|Vanillite|Ice|Surf|30-40|4|4%|
|Vanillish|Ice|Surf|32-42|5|1%|
|Spheal|Ice/Water|Old Rod|30-40|1-2|100%|
|Sealeo|Ice/Water|Good Rod|32-42|3-4|80%|
|Vanillite|Ice|Good Rod|30-40|5|20%|
|Walrein|Ice/Water|Super Rod|35-45|6-7|80%|
|Vanillish|Ice|Super Rod|32-42|8|15%|
|Vanilluxe|Ice|Super Rod|35-45|9-10|5%|

-----

### Route 126

*Deep waters with underwater caverns — Access to Sootopolis City.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Electivire|Electric|Grass|37-41|1-8|90%|
|Alolan Golem|Rock/Electric|Grass|37-41|9-12|10%|
|Hisuian Basculin|Water|Surf|36-41|1|60%|
|Politoed|Water|Surf|36-41|2|30%|
|Reuniclus|Psychic|Surf|36-41|3|5%|
|Hisuian Basculin|Water|Surf|36-41|4-5|5%|
|Poliwag|Water|Old Rod|36-41|1-2|100%|
|Hisuian Basculin|Water|Good Rod|36-41|3-4|80%|
|Poliwhirl|Water|Good Rod|36-41|5|20%|
|Basculegion|Water/Ghost|Super Rod|37-41|6-7|80%|
|Politoed|Water|Super Rod|36-41|8|15%|
|Araquanid|Water/Bug|Super Rod|36-41|9|4%|
|Milotic|Water|Super Rod|36-41|10|1%|

-----

### Route 127

*Open ocean east of Mossdeep — Treacherous deep waters.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Alolan Golem|Rock/Electric|Grass|37-41|1-8|90%|
|Conkeldurr|Fighting|Grass|37-41|9-12|10%|
|Hisuian Qwilfish|Dark/Poison|Surf|36-41|1|60%|
|Hisuian Basculin|Water|Surf|36-41|2|30%|
|Overqwil|Dark/Poison|Surf|36-41|3|5%|
|Basculegion|Water/Ghost|Surf|37-41|4|4%|
|Hisuian Qwilfish|Dark/Poison|Surf|36-41|5|1%|
|Poliwhirl|Water|Old Rod|36-41|1-2|100%|
|Hisuian Qwilfish|Dark/Poison|Good Rod|36-41|3-4|80%|
|Hisuian Basculin|Water|Good Rod|36-41|5|20%|
|Overqwil|Dark/Poison|Super Rod|36-41|6-7|80%|
|Basculegion|Water/Ghost|Super Rod|37-41|8|15%|
|Grapploct|Fighting|Super Rod|36-41|9|4%|
|Barbaracle|Rock/Water|Super Rod|36-41|10|1%|

-----

### Route 128

*Approach to Ever Grande City — Powerful currents near the Pokemon League.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Magmortar|Fire|Grass|38-42|1-8|90%|
|Ursaring|Normal|Grass|38-42|9-12|10%|
|Poliwrath|Water/Fighting|Surf|37-42|1|60%|
|Walrein|Ice/Water|Surf|37-42|2|30%|
|Barbaracle|Rock/Water|Surf|37-42|3|5%|
|Poliwrath|Water/Fighting|Surf|37-42|4-5|5%|
|Poliwhirl|Water|Old Rod|37-42|1-2|100%|
|Hisuian Basculin|Water|Good Rod|37-42|3-4|80%|
|Hisuian Qwilfish|Dark/Poison|Good Rod|37-42|5|20%|
|Hisuian Qwilfish|Dark/Poison|Super Rod|37-42|6-7|80%|
|Overqwil|Dark/Poison|Super Rod|38-42|8|15%|
|Grapploct|Fighting|Super Rod|38-42|9|4%|
|Walrein|Ice/Water|Super Rod|38-42|10|1%|

-----

### Magma Hideout

*Team Magma's secret volcanic base — Deep within Mt. Chimney.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Alolan Geodude|Rock/Electric|Cave|27-27|1|20%|
|Glimmet|Rock/Poison|Cave|28-28|2|20%|
|Alolan Geodude|Rock/Electric|Cave|28-28|3|10%|
|Glimmet|Rock/Poison|Cave|30-30|4|10%|
|Alolan Geodude|Rock/Electric|Cave|29-29|5|10%|
|Alolan Geodude|Rock/Electric|Cave|30-30|6-7|15%|
|Alolan Graveler|Rock/Electric|Cave|30-30|8-9|9%|
|Alolan Graveler|Rock/Electric|Cave|31-31|10|4%|
|Alolan Graveler|Rock/Electric|Cave|32-32|11|1%|
|Alolan Graveler|Rock/Electric|Cave|33-33|12|1%|

-----

### Seafloor Cavern (Entrance)

*Entrance to the deep underwater cave — Surf and Fishing access.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Hisuian Qwilfish|Dark/Poison|Surf|30-40|1|60%|
|Overqwil|Dark/Poison|Surf|30-40|2|30%|
|White-Striped Basculin|Water|Surf|30-40|3|5%|
|Poliwhirl|Water|Surf|30-40|4|4%|
|Araquanid|Water/Bug|Surf|30-40|5|1%|
|Poliwhirl|Water|Old Rod|30-40|1-2|100%|
|Hisuian Qwilfish|Dark/Poison|Good Rod|30-40|3-4|80%|
|White-Striped Basculin|Water|Good Rod|30-40|5|20%|
|Overqwil|Dark/Poison|Super Rod|35-40|6-7|80%|
|Basculegion (Male)|Water/Ghost|Super Rod|35-40|8|15%|
|Grapploct|Fighting|Super Rod|35-40|9|4%|
|Araquanid|Water/Bug|Super Rod|35-40|10|1%|

-----

### Seafloor Cavern (Rooms)

*Deep underwater cave rooms — Where the ancient legendary rests.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Noibat|Flying/Dragon|Cave|30-30|1|20%|
|Noibat|Flying/Dragon|Cave|31-31|2|20%|
|Noibat|Flying/Dragon|Cave|32-32|3|10%|
|Noibat|Flying/Dragon|Cave|33-33|4|10%|
|Noibat|Flying/Dragon|Cave|28-28|5|10%|
|Noibat|Flying/Dragon|Cave|29-29|6|10%|
|Noibat|Flying/Dragon|Cave|34-34|7|5%|
|Noibat|Flying/Dragon|Cave|35-35|8|5%|
|Noivern|Flying/Dragon|Cave|34-34|9|4%|
|Noivern|Flying/Dragon|Cave|35-35|10|4%|
|Noivern|Flying/Dragon|Cave|33-33|11|1%|
|Noivern|Flying/Dragon|Cave|36-36|12|1%|

-----

### Cave of Origin (Entrance)

*Sacred cave in Sootopolis — Entrance hall.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Noibat|Flying/Dragon|Cave|30-30|1|20%|
|Noibat|Flying/Dragon|Cave|31-31|2|20%|
|Noibat|Flying/Dragon|Cave|32-32|3|10%|
|Noibat|Flying/Dragon|Cave|33-33|4|10%|
|Noibat|Flying/Dragon|Cave|28-28|5|10%|
|Noibat|Flying/Dragon|Cave|29-29|6|10%|
|Noibat|Flying/Dragon|Cave|34-34|7|5%|
|Noibat|Flying/Dragon|Cave|35-35|8|5%|
|Noivern|Flying/Dragon|Cave|34-34|9|4%|
|Noivern|Flying/Dragon|Cave|35-35|10|4%|
|Noivern|Flying/Dragon|Cave|33-33|11|1%|
|Noivern|Flying/Dragon|Cave|36-36|12|1%|

-----

### Cave of Origin (1F / Deeper Floors)

*Deeper chambers of the Cave of Origin — Home of ancient power. Gimmighoul lurk among the rocks.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Noibat|Flying/Dragon|Cave|30-30|1|20%|
|Noibat|Flying/Dragon|Cave|31-31|2|20%|
|Noibat|Flying/Dragon|Cave|32-32|3|10%|
|Gimmighoul (Chest)|Ghost|Cave|30-30|4|10%|
|Gimmighoul (Chest)|Ghost|Cave|32-32|5|10%|
|Gimmighoul (Chest)|Ghost|Cave|34-34|6|10%|
|Noibat|Flying/Dragon|Cave|33-33|7|5%|
|Noibat|Flying/Dragon|Cave|34-34|8|5%|
|Noivern|Flying/Dragon|Cave|34-34|9|4%|
|Noivern|Flying/Dragon|Cave|35-35|10|4%|
|Noivern|Flying/Dragon|Cave|33-33|11|1%|
|Noivern|Flying/Dragon|Cave|36-36|12|1%|

-----

### Sootopolis City

*City in a volcanic crater — Surrounded by pristine waters.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Milotic|Water|Surf|35-45|1|60%|
|Araquanid|Water/Bug|Surf|35-45|2|30%|
|Hisuian Basculin|Water|Surf|35-45|3|5%|
|Politoed|Water|Surf|35-45|4|4%|
|Poliwhirl|Water|Surf|35-45|5|1%|
|Poliwhirl|Water|Old Rod|35-45|1-2|100%|
|Hisuian Basculin|Water|Good Rod|35-45|3-4|80%|
|Milotic|Water|Good Rod|35-45|5|20%|
|Milotic|Water|Super Rod|35-45|6-7|80%|
|Politoed|Water|Super Rod|35-45|8|15%|
|Grapploct|Fighting|Super Rod|35-45|9|4%|
|Araquanid|Water/Bug|Super Rod|35-45|10|1%|

-----

### Sky Pillar

*Ancient tower reaching into the clouds — Rayquaza's domain.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Gimmighoul|Ghost|Cave|33-33|1|20%|
|Noivern|Flying/Dragon|Cave|34-34|2|20%|
|Noivern|Flying/Dragon|Cave|35-35|3|10%|
|Gimmighoul|Ghost|Cave|34-34|4|10%|
|Runerigus|Ground/Ghost|Cave|36-36|5|10%|
|Drifblim|Ghost/Flying|Cave|37-37|6|10%|
|Drifblim|Ghost/Flying|Cave|38-38|7|5%|
|Runerigus|Ground/Ghost|Cave|36-36|8|5%|
|Runerigus|Ground/Ghost|Cave|37-37|9|4%|
|Runerigus|Ground/Ghost|Cave|38-38|10|4%|
|Runerigus|Ground/Ghost|Cave|37-37|11|1%|
|Runerigus|Ground/Ghost|Cave|38-38|12|1%|

-----

## Endgame

### Routes 129-131

*Open ocean routes — Vast stretches of deep water between Ever Grande and the mainland.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Talonflame|Fire/Flying|Grass|38-43|1-4|60%|
|Yanmega|Bug/Flying|Grass|39-43|5-8|30%|
|Orbeetle|Bug/Psychic|Grass|39-43|9-12|10%|
|Hisuian Qwilfish|Dark/Poison|Surf|38-43|1|60%|
|Walrein|Ice/Water|Surf|38-43|2|30%|
|Vanilluxe|Ice|Surf|38-43|3|5%|
|Hisuian Qwilfish|Dark/Poison|Surf|38-43|4-5|5%|
|Poliwhirl|Water|Old Rod|38-43|1-2|100%|
|Hisuian Qwilfish|Dark/Poison|Good Rod|38-43|3-4|80%|
|Hisuian Basculin|Water|Good Rod|38-43|5|20%|
|Overqwil|Dark/Poison|Super Rod|38-43|6-7|80%|
|Walrein|Ice/Water|Super Rod|38-43|8|15%|
|Grapploct|Fighting|Super Rod|38-43|9|4%|
|Barbaracle|Rock/Water|Super Rod|38-43|10|1%|

-----

### Routes 132-134

*Strong current routes — Unpredictable tidal waters west of Pacifidlog Town.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Noivern|Flying/Dragon|Grass|39-44|1-8|90%|
|Rotom|Electric/Ghost|Grass|39-44|9-12|10%|
|Hisuian Basculin|Water|Surf|39-44|1|60%|
|Clodsire|Poison/Ground|Surf|39-44|2|30%|
|Hisuian Basculin|Water|Surf|39-44|3-5|10%|
|Poliwhirl|Water|Old Rod|39-44|1-2|100%|
|Hisuian Basculin|Water|Good Rod|39-44|3-4|80%|
|Hisuian Qwilfish|Dark/Poison|Good Rod|39-44|5|20%|
|Overqwil|Dark/Poison|Super Rod|39-44|6-7|80%|
|Basculegion|Water/Ghost|Super Rod|39-44|8|15%|
|Grapploct|Fighting|Super Rod|39-44|9|4%|
|Araquanid|Water/Bug|Super Rod|39-44|10|1%|

-----

## Victory Road

### Victory Road

*The final gauntlet before the Pokemon League — Only the strongest trainers and Pokemon survive here.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Ursaluna|Ground/Normal|Cave|42-50|1-2|40%|
|Conkeldurr|Fighting|Cave|42-48|3-4|20%|
|Roaring Moon|Dragon/Dark|Cave|45-50|5-6|20%|
|Glimmora|Rock/Poison|Cave|42-48|7-8|10%|
|Iron Valiant|Fairy/Fighting|Cave|45-50|9-10|8%|
|Gholdengo|Steel/Ghost|Cave|42-48|11-12|2%|

-----

## Safari Zone (Hoenn)

### Safari Zone South

*Southern area of the Hoenn Safari Zone.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Bounsweet|Grass|Grass|25-25|1|20%|
|Bounsweet|Grass|Grass|27-27|2|20%|
|Solosis|Psychic|Grass|25-25|3|10%|
|Solosis|Psychic|Grass|27-27|4|10%|
|Espurr|Psychic|Grass|25-25|5|10%|
|Pikipek|Normal/Flying|Grass|25-25|6|10%|
|Steenee|Grass|Grass|25-25|7|5%|
|Reuniclus|Psychic|Grass|27-27|8|5%|
|Toxel|Electric/Poison|Grass|25-25|9|4%|
|Reuniclus|Psychic|Grass|27-27|10|4%|
|Toxel|Electric/Poison|Grass|27-27|11|1%|
|Reuniclus|Psychic|Grass|29-29|12|1%|

-----

### Safari Zone North

*Northern area of the Hoenn Safari Zone.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Hippopotas|Ground|Grass|27-27|1|20%|
|Bounsweet|Grass|Grass|27-27|2|20%|
|Hippopotas|Ground|Grass|29-29|3|10%|
|Bounsweet|Grass|Grass|29-29|4|10%|
|Espurr|Psychic|Grass|27-27|5|10%|
|Steenee|Grass|Grass|29-29|6|10%|
|Steenee|Grass|Grass|31-31|7|5%|
|Espurr|Psychic|Grass|29-29|8|5%|
|Meowstic|Psychic|Grass|29-29|9|4%|
|Vikavolt|Bug/Electric|Grass|27-27|10|4%|
|Meowstic|Psychic|Grass|31-31|11|1%|
|Vikavolt|Bug/Electric|Grass|29-29|12|1%|
|Alolan Geodude|Rock/Electric|Rock Smash|15-25|1|60%|
|Nosepass|Rock|Rock Smash|15-25|2|30%|
|Alolan Geodude|Rock/Electric|Rock Smash|15-25|3-5|10%|

-----

### Safari Zone Southwest

*Southwestern area with ponds.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Bounsweet|Grass|Grass|25-25|1|20%|
|Bounsweet|Grass|Grass|27-27|2|20%|
|Solosis|Psychic|Grass|25-25|3|10%|
|Solosis|Psychic|Grass|27-27|4|10%|
|Espurr|Psychic|Grass|25-25|5|10%|
|Pikipek|Normal/Flying|Grass|27-27|6|10%|
|Steenee|Grass|Grass|25-25|7|5%|
|Reuniclus|Psychic|Grass|27-27|8|5%|
|Toxel|Electric/Poison|Grass|25-25|9|4%|
|Reuniclus|Psychic|Grass|27-27|10|4%|
|Toxel|Electric/Poison|Grass|27-27|11|1%|
|Reuniclus|Psychic|Grass|29-29|12|1%|
|Dewpider|Water/Bug|Surf|15-35|1|60%|
|Poliwag|Water|Surf|15-35|2|30%|
|Araquanid|Water/Bug|Surf|15-35|3|5%|
|Poliwhirl|Water|Surf|15-35|4|4%|
|Bibarel|Normal/Water|Surf|15-35|5|1%|
|Poliwag|Water|Old Rod|15-20|1-2|100%|
|Poliwag|Water|Good Rod|17-35|3|60%|
|Poliwhirl|Water|Good Rod|18-35|4-5|40%|
|Poliwhirl|Water|Super Rod|20-35|6-7|80%|
|Araquanid|Water/Bug|Super Rod|20-35|8|15%|
|Dewpider|Water/Bug|Super Rod|18-35|9-10|5%|

-----

### Safari Zone Northwest

*Northwestern area — Dense vegetation.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Hippopotas|Ground|Grass|27-27|1|20%|
|Bounsweet|Grass|Grass|27-27|2|20%|
|Hippopotas|Ground|Grass|29-29|3|10%|
|Bounsweet|Grass|Grass|29-29|4|10%|
|Pikipek|Normal/Flying|Grass|27-27|5|10%|
|Steenee|Grass|Grass|29-29|6|10%|
|Steenee|Grass|Grass|31-31|7|5%|
|Pikipek|Normal/Flying|Grass|29-29|8|5%|
|Toucannon|Normal/Flying|Grass|29-29|9|4%|
|Vespiquen|Bug/Flying|Grass|27-27|10|4%|
|Toucannon|Normal/Flying|Grass|31-31|11|1%|
|Vespiquen|Bug/Flying|Grass|29-29|12|1%|
|Dewpider|Water/Bug|Surf|15-35|1|60%|
|Poliwag|Water|Surf|15-35|2|30%|
|Araquanid|Water/Bug|Surf|15-35|3|5%|
|Poliwhirl|Water|Surf|15-35|4|4%|
|Bibarel|Normal/Water|Surf|15-35|5|1%|
|Poliwag|Water|Old Rod|15-20|1-2|100%|
|Poliwag|Water|Good Rod|17-35|3|60%|
|Poliwhirl|Water|Good Rod|18-35|4-5|40%|
|Poliwhirl|Water|Super Rod|20-35|6-7|80%|
|Araquanid|Water/Bug|Super Rod|20-35|8|15%|
|Dewpider|Water/Bug|Super Rod|18-35|9-10|5%|

-----

### Safari Zone Southeast

*Southeastern area with varied terrain.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Bounsweet|Grass|Grass|33-33|1|20%|
|Toxel|Electric/Poison|Grass|34-34|2|20%|
|Bounsweet|Grass|Grass|35-35|3|10%|
|Toxel|Electric/Poison|Grass|36-36|4|10%|
|Ledian|Bug/Flying|Grass|34-34|5|10%|
|Tarountula|Bug|Grass|33-33|6|10%|
|Pikipek|Normal/Flying|Grass|35-35|7|5%|
|Snubbull|Fairy|Grass|34-34|8|5%|
|Tropius|Grass/Flying|Grass|36-36|9|4%|
|Noibat|Flying/Dragon|Grass|37-37|10|4%|
|Tropius|Grass/Flying|Grass|39-39|11|1%|
|Noibat|Flying/Dragon|Grass|40-40|12|1%|
|Dewpider|Water/Bug|Surf|15-35|1|60%|
|Poliwag|Water|Surf|15-35|2|30%|
|Araquanid|Water/Bug|Surf|15-35|3|5%|
|Poliwhirl|Water|Surf|15-35|4|4%|
|Bibarel|Normal/Water|Surf|15-35|5|1%|
|Poliwag|Water|Old Rod|15-20|1-2|100%|
|Poliwag|Water|Good Rod|17-35|3|60%|
|Poliwhirl|Water|Good Rod|18-35|4-5|40%|
|Poliwhirl|Water|Super Rod|20-35|6-7|80%|
|Araquanid|Water/Bug|Super Rod|20-35|8|15%|
|Dewpider|Water/Bug|Super Rod|18-35|9-10|5%|

-----

### Safari Zone Northeast

*Northeastern area — Rocky outcrops.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Ledian|Bug/Flying|Grass|33-33|1|20%|
|Teddiursa|Normal|Grass|34-34|2|20%|
|Ledian|Bug/Flying|Grass|35-35|3|10%|
|Teddiursa|Normal|Grass|36-36|4|10%|
|Bounsweet|Grass|Grass|34-34|5|10%|
|Ledyba|Bug/Flying|Grass|33-33|6|10%|
|Pikipek|Normal/Flying|Grass|35-35|7|5%|
|Tarountula|Bug|Grass|34-34|8|5%|
|Magby|Fire|Grass|36-36|9|4%|
|Ursaring|Normal|Grass|37-37|10|4%|
|Magby|Fire|Grass|39-39|11|1%|
|Ursaring|Normal|Grass|40-40|12|1%|
|Klawf|Rock|Rock Smash|15-25|1|60%|
|Alolan Geodude|Rock/Electric|Rock Smash|15-25|2|30%|
|Klawf|Rock|Rock Smash|15-25|3-5|10%|

-----

## Coastal Cities

### Petalburg City

*Hometown of the Gym Leader — River runs through.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Dewpider|Water/Bug|Surf|3-15|1|60%|
|Poliwag|Water|Surf|3-15|2|30%|
|Araquanid|Water/Bug|Surf|3-15|3|5%|
|Poliwhirl|Water|Surf|3-15|4|4%|
|Bibarel|Normal/Water|Surf|3-15|5|1%|
|Poliwag|Water|Old Rod|3-8|1-2|100%|
|Poliwag|Water|Good Rod|5-12|3|60%|
|Poliwhirl|Water|Good Rod|6-12|4-5|40%|
|Poliwhirl|Water|Super Rod|8-12|6-7|80%|
|Araquanid|Water/Bug|Super Rod|8-12|8|15%|
|Dewpider|Water/Bug|Super Rod|6-12|9-10|5%|

-----

### Dewford Town

*Island town with beach access.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Dewpider|Water/Bug|Surf|5-20|1|60%|
|Binacle|Rock/Water|Surf|5-20|2|30%|
|Poliwag|Water|Surf|5-20|3|5%|
|Clobbopus|Fighting|Surf|5-20|4|4%|
|Araquanid|Water/Bug|Surf|5-20|5|1%|
|Poliwag|Water|Old Rod|5-10|1-2|100%|
|Clobbopus|Fighting|Good Rod|8-15|3-4|80%|
|Binacle|Rock/Water|Good Rod|8-15|5|20%|
|Barbaracle|Rock/Water|Super Rod|10-15|6-7|80%|
|Grapploct|Fighting|Super Rod|10-15|8|15%|
|Araquanid|Water/Bug|Super Rod|10-15|9-10|5%|

-----

### Slateport City

*Bustling port city.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Dewpider|Water/Bug|Surf|10-25|1|60%|
|Binacle|Rock/Water|Surf|10-25|2|30%|
|Poliwag|Water|Surf|10-25|3|5%|
|Clobbopus|Fighting|Surf|10-25|4|4%|
|Araquanid|Water/Bug|Surf|10-25|5|1%|
|Poliwag|Water|Old Rod|10-15|1-2|100%|
|Clobbopus|Fighting|Good Rod|13-22|3-4|80%|
|Binacle|Rock/Water|Good Rod|13-22|5|20%|
|Barbaracle|Rock/Water|Super Rod|15-22|6-7|80%|
|Grapploct|Fighting|Super Rod|15-22|8|15%|
|Araquanid|Water/Bug|Super Rod|15-22|9-10|5%|

-----

### Lilycove City

*Coastal city with department store.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Dewpider|Water/Bug|Surf|30-45|1|60%|
|Binacle|Rock/Water|Surf|30-45|2|30%|
|Poliwag|Water|Surf|30-45|3|5%|
|Clobbopus|Fighting|Surf|30-45|4|4%|
|Araquanid|Water/Bug|Surf|30-45|5|1%|
|Poliwag|Water|Old Rod|30-35|1-2|100%|
|Clobbopus|Fighting|Good Rod|33-40|3-4|80%|
|Binacle|Rock/Water|Good Rod|33-40|5|20%|
|Barbaracle|Rock/Water|Super Rod|35-40|6-7|80%|
|Grapploct|Fighting|Super Rod|35-40|8|15%|
|Araquanid|Water/Bug|Super Rod|35-40|9-10|5%|

-----

### Mossdeep City

*Space center island city.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Dewpider|Water/Bug|Surf|35-45|1|60%|
|Binacle|Rock/Water|Surf|35-45|2|30%|
|Poliwag|Water|Surf|35-45|3|5%|
|Clobbopus|Fighting|Surf|35-45|4|4%|
|Araquanid|Water/Bug|Surf|35-45|5|1%|
|Poliwag|Water|Old Rod|35-40|1-2|100%|
|Clobbopus|Fighting|Good Rod|38-45|3-4|80%|
|Binacle|Rock/Water|Good Rod|38-45|5|20%|
|Barbaracle|Rock/Water|Super Rod|40-45|6-7|80%|
|Grapploct|Fighting|Super Rod|40-45|8|15%|
|Araquanid|Water/Bug|Super Rod|40-45|9-10|5%|

-----

### Pacifidlog Town

*Floating town on Route 131.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Dewpider|Water/Bug|Surf|35-45|1|60%|
|Binacle|Rock/Water|Surf|35-45|2|30%|
|Poliwag|Water|Surf|35-45|3|5%|
|Clobbopus|Fighting|Surf|35-45|4|4%|
|Araquanid|Water/Bug|Surf|35-45|5|1%|
|Poliwag|Water|Old Rod|35-40|1-2|100%|
|Clobbopus|Fighting|Good Rod|38-45|3-4|80%|
|Binacle|Rock/Water|Good Rod|38-45|5|20%|
|Barbaracle|Rock/Water|Super Rod|40-45|6-7|80%|
|Grapploct|Fighting|Super Rod|40-45|8|15%|
|Araquanid|Water/Bug|Super Rod|40-45|9-10|5%|

-----

### Ever Grande City

*Pokemon League gateway.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Dewpider|Water/Bug|Surf|38-48|1|60%|
|Binacle|Rock/Water|Surf|38-48|2|30%|
|Poliwag|Water|Surf|38-48|3|5%|
|Clobbopus|Fighting|Surf|38-48|4|4%|
|Araquanid|Water/Bug|Surf|38-48|5|1%|
|Poliwag|Water|Old Rod|38-43|1-2|100%|
|Clobbopus|Fighting|Good Rod|41-48|3-4|80%|
|Binacle|Rock/Water|Good Rod|41-48|5|20%|
|Barbaracle|Rock/Water|Super Rod|43-48|6-7|80%|
|Grapploct|Fighting|Super Rod|43-48|8|15%|
|Araquanid|Water/Bug|Super Rod|43-48|9-10|5%|

-----

## Other Areas

### Abandoned Ship

*Derelict vessel — Water-type habitat.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Dewpider|Water/Bug|Surf|25-35|1-2|90%|
|Araquanid|Water/Bug|Surf|28-38|3-4|9%|
|Poliwhirl|Water|Surf|25-35|5|1%|
|Poliwag|Water|Old Rod|25-35|1-2|100%|
|Dewpider|Water/Bug|Good Rod|25-35|3-4|80%|
|Araquanid|Water/Bug|Good Rod|28-38|5|20%|
|Araquanid|Water/Bug|Super Rod|28-38|6-7|80%|
|Grapploct|Fighting|Super Rod|30-40|8|15%|
|Milotic|Water|Super Rod|30-40|9-10|5%|

-----

### Underwater (Routes 124/126)

*Diving encounters beneath the sea.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Araquanid|Water/Bug|Surf|35-45|1|60%|
|Dewpider|Water/Bug|Surf|35-45|2|30%|
|Milotic|Water|Surf|35-45|3|5%|
|Hisuian Basculin|Water|Surf|35-45|4|4%|
|Poliwhirl|Water|Surf|35-45|5|1%|

-----

### Altering Cave

*Mysterious cave with unusual encounters.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Gimmighoul|Ghost|Cave|10-10|1|20%|
|Gimmighoul|Ghost|Cave|12-12|2|20%|
|Gimmighoul|Ghost|Cave|8-8|3|10%|
|Gimmighoul|Ghost|Cave|14-14|4|10%|
|Gimmighoul|Ghost|Cave|10-10|5|10%|
|Gimmighoul|Ghost|Cave|12-12|6|10%|
|Gimmighoul|Ghost|Cave|16-16|7|5%|
|Gimmighoul|Ghost|Cave|6-6|8|5%|
|Gimmighoul|Ghost|Cave|8-8|9|4%|
|Gimmighoul|Ghost|Cave|14-14|10|4%|
|Gimmighoul|Ghost|Cave|8-8|11|1%|
|Gimmighoul|Ghost|Cave|14-14|12|1%|

-----

### Artisan Cave

*Post-game cave near the Battle Frontier.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Meowstic|Psychic|Cave|40-40|1|20%|
|Meowstic|Psychic|Cave|41-41|2|20%|
|Meowstic|Psychic|Cave|42-42|3|10%|
|Meowstic|Psychic|Cave|43-43|4|10%|
|Meowstic|Psychic|Cave|44-44|5|10%|
|Meowstic|Psychic|Cave|45-45|6|10%|
|Meowstic|Psychic|Cave|46-46|7|5%|
|Meowstic|Psychic|Cave|47-47|8|5%|
|Meowstic|Psychic|Cave|48-48|9|4%|
|Meowstic|Psychic|Cave|49-49|10|4%|
|Meowstic|Psychic|Cave|50-50|11-12|2%|

-----

### Desert Underpass

*Hidden passage beneath the desert.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Hippopotas|Ground|Cave|38-38|1|20%|
|Blipbug|Bug|Cave|35-35|2|20%|
|Hippopotas|Ground|Cave|40-40|3|10%|
|Dottler|Bug/Psychic|Cave|40-40|4|10%|
|Hippopotas|Ground|Cave|41-41|5|10%|
|Blipbug|Bug|Cave|36-36|6|10%|
|Dottler|Bug/Psychic|Cave|38-38|7|5%|
|Hippopotas|Ground|Cave|42-42|8|5%|
|Blipbug|Bug|Cave|38-38|9|4%|
|Hippopotas|Ground|Cave|43-43|10|4%|
|Dottler|Bug/Psychic|Cave|44-44|11|1%|
|Hippopotas|Ground|Cave|45-45|12|1%|

-----

### Mirage Tower

*Phantom tower in the desert.*

|Pokemon|Type|Encounter|Levels|Slots|Rate|
|-------|----|---------|------|-----|----|
|Hippopotas|Ground|Cave|21-21|1|20%|
|Klawf|Rock|Cave|21-21|2|20%|
|Hippopotas|Ground|Cave|20-20|3|10%|
|Klawf|Rock|Cave|20-20|4|10%|
|Hippopotas|Ground|Cave|20-20|5|10%|
|Klawf|Rock|Cave|20-20|6|10%|
|Hippopotas|Ground|Cave|22-22|7|5%|
|Klawf|Rock|Cave|22-22|8|5%|
|Hippopotas|Ground|Cave|23-23|9|4%|
|Klawf|Rock|Cave|23-23|10|4%|
|Hippopotas|Ground|Cave|24-24|11|1%|
|Klawf|Rock|Cave|24-24|12|1%|

-----

## Special Notes

### Feebas (Route 119)
Feebas appears in Route 119 via fishing (Good Rod slot 5 and Super Rod slots 1-3). This is the primary location to find Feebas, matching the original Emerald's design of making Feebas rare and route-specific.

-----

## Nickname Decoder

For reference, here are the nicknames from the original list and which Pokemon they correspond to:

|Nickname         |Actual Pokemon                                         |Reasoning                                            |
|-----------------|-------------------------------------------------------|-----------------------------------------------------|
|Poli (x4)        |Poliwag, Poliwhirl, Poliwrath, Politoed                |All share the "Poli-" prefix                         |
|simi/pan (x6)    |Pansage, Simisage, Pansear, Simisear, Panpour, Simipour|Elemental monkey families all use Pan-/Simi- prefixes|
|Timbur           |Timburr                                                |Slight misspelling                                   |
|Conkledur        |Conkeldurr                                             |Slight misspelling                                   |
|cell             |Solosis                                                |Single-cell psychic Pokemon                          |
|two cell         |Duosion                                                |"Duo" = two cells merged                             |
|bus              |Charjabug                                              |Resembles a bus/battery box                          |
|spider ball thing|Tarountula                                             |Round, ball-shaped spider Pokemon                    |
|Toucanon         |Toucannon                                              |Slight misspelling                                   |
|Feraligtr        |Feraligatr                                             |Slight misspelling                                   |
|Crocanaw         |Croconaw                                               |Slight misspelling                                   |
