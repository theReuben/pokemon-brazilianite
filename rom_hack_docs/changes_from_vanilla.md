# What Brazilianite changes

A summary of how Pokemon Brazilianite differs from the game it grew out of.

## First, the baseline

Brazilianite is built on **pokeemerald-expansion**, not on vanilla Emerald
directly. A large share of the difference a player will notice comes from the
engine rather than from anything designed here: the Fairy type, the
physical/special split, abilities, moves and items through Generation 9, Mega
Evolution, Terastallisation, and modern damage and experience formulas are all
inherited.

Everything below is what has been changed *on top of* that.

## The region

| | |
|---|---|
| **Starters** | Turtwig, Fuecoco and Totodile, in place of the Hoenn three |
| **Regional dex** | Cut to **135 Pokemon**, listed in `regional_dex.md` |
| **Wild encounters** | Every Hoenn encounter table rewritten to draw only from that dex |
| **Fossils** | Cover Fossil (Tirtouga) and Plume Fossil (Archen), revived at Devon Corp |

The dex leans on regional forms - Alolan, Galarian, Hisuian and Paldean - plus
two Paradox Pokemon, rather than the Hoenn roster.

## Cast

The villainous teams are rewritten from the ground up.

| Vanilla | Brazilianite |
|---------|--------------|
| Team Aqua | **Team Algorithm** |
| Team Magma | **Team Blockchain** |
| Archie / Maxie | **Julian** (both leaders) |

Both teams use redrawn sprites built from Team Galactic art, have their own
trainer classes, and were given new motives - the plot beats through Mt Pyre and
Sootopolis were rewritten to match, and the GPU turns out to stand for Groudon
Processing Unit.

Gym leaders and the Elite Four are largely recast:

| Role | Vanilla | Brazilianite |
|------|---------|--------------|
| Rustboro | Roxanne | LIL JON |
| Dewford | Brawly | MERLOT |
| Mauville | Wattson | LUFFY |
| Petalburg | Norman | MAMA BOSA |
| Mossdeep | Tate & Liza | Mr&Mrs P |
| Elite Four | Sidney | JUMBLES |
| Elite Four | Phoebe | PRAESTA |
| Elite Four | Glacia | HUSH |
| Elite Four | Drake | VARGNA |
| Champion | Wallace | JAKE |

Flannery, Winona and Juan keep their names. The player's mother and father swap
roles, with Norman becoming MAMA BOSA. One gym is themed around anime
characters, with custom trainer classes and dialogue to match.

## Progression

**A hard level cap.** Pokemon at or above the cap gain no experience at all, and
Rare Candies cannot push past it. The cap rises with badges:

| Badges | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | Champion |
|--------|---|---|---|---|---|---|---|---|----------|
| Cap    | 15 | 19 | 24 | 29 | 31 | 33 | 42 | 46 | 58 |

**The Champion cannot be walked past** - the pre-league fight is mandatory.

## Quality of life

- **Reusable TMs** - buy one, use it forever
- **Exp. Share** as a Gen 6 key item that toggles party-wide experience
- **Move relearner in the party menu**, no NPC required
- **Follower Pokemon**, HGSS style, including overworld weather forms for
  Castform and Cherrim, and Transform/Illusion followers copying wild Pokemon
- **IVs and EVs shown as numbers** on the summary screen
- **Evolution held items usable from the bag**, Legends: Arceus style
- **Shiny odds raised to 1/512** from 1/8192
- **Both bikes at once** - Rydel hands over the Mach Bike and Acro Bike
  together, so there is no trekking back to Mauville to swap

### New items

| Item | What it does |
|------|--------------|
| **Endless Candy** | A Rare Candy that never runs out |
| **Cap Candy** | Raises a Pokemon straight to the current level cap |
| **Friend Band** | Held item for the three friendship evolutions in the dex |
| **Castformite** | Mega Stone for Castform |

The two candies are in the bag from the start.

## Building a team

The intent is that a competitive team is bought and tuned rather than ground
out.

**The Lilycove Department Store** was rebuilt around it:

- **2F** - the modern Poke Balls, full medicine counter, X items
- **3F** - vitamins, PP Up and PP Max, Ability Capsule and Ability Patch, Bottle
  Caps and Gold Bottle Caps, and all 21 mints
- **4F** - twelve TMs, and a held-item counter carrying Leftovers, Focus Sash,
  the Choice trio, Life Orb, Assault Vest, Eviolite, Heavy-Duty Boots and more

The held-item counter is gated behind the eighth badge, and a shopper on the
floor says so.

**Vitamins raise 50 EVs instead of 10**, so a full 252/252/4 spread costs
13 vitamins per Pokemon rather than 53.

**The Game Corner funds it.** The slot machines were retuned - the chance of
drawing for a Special at three coins rises from roughly 5% to 18%, and straight
7s from 25-50/256 to 100-125/256, landing a 300-coin jackpot about every eleven
spins. A cashier beside the coins clerk buys coins back for money, and coins are
worth 100 either way rather than 20. Because the buy and sell rates match, the
profit has to come off the machines rather than the exchange. Together these
take a fully kitted team of six from roughly fourteen hours of slots to about
one.

## The legendary dens

Three caves, each holding a set of legendaries that **vanish the moment you
commit to one**:

| Cave | Route | Choose one of |
|------|-------|---------------|
| Beast Den | 104 | Raikou, Entei, Suicune |
| Storm Roost | 111 | Galarian Articuno, Zapdos, Moltres |
| Tapu Grotto | 119 | Tapu Koko, Lele, Bulu, Fini |

All are level 50 and gated behind the eighth badge, with a hiker standing in
each doorway until then. Picking a fight with one drives the others off for
good - but losing, fleeing or knocking it out leaves the one you chose in place,
so a failed catch costs nothing.

## Pokemon changes

Species edited away from their official data:

| Pokemon | Change |
|---------|--------|
| Feraligatr | now Water/Dark |
| Politoed | now Water/Fairy, SpA 90 to 100, learns Moonblast on evolving |
| Tropius | Def 83 to 103, SpD 87 to 107 (BST 460 to 500) |
| Timburr | now Fighting/Grass, learns Leaf Blade at 22 and Wood Hammer at 24 |
| Gurdurr | now Fighting/Steel, learns Bullet Punch on evolving |
| Conkeldurr | now Fighting/Ground, learns Earthquake on evolving |
| Orthworm | HP 70 to 100, Spe 65 to 95 (BST 480 to 540) |
| Combee | both genders now evolve into Vespiquen |
| Clobbopus | now Fighting/Water |
| Grapploct | now Fighting/Water |
| Carracosta | Atk 108 to 128, SpD 65 to 115 (BST 495 to 565) |

Castform also gains Mega forms that learn all four terrains and Terrain Pulse.

Requested changes are tracked in `dex_changes.md`, which is generated from the
game data by `dev_scripts/dex_worksheet.py`.

## Trainers

- **Team Algorithm** fields machines and data: Magnemite, Voltorb, Klink,
  Grimer, Porygon and Ditto on grunts; Rotom, Magneton, Metang, Muk and Porygon2
  on admins; Porygon2 with an Eviolite, Metagross and Genesect on Julian
- **Team Blockchain** fields mining and coins: Meowth, Roggenrola, Yamper,
  Rockruff and Gimmighoul on grunts; Persian, Gigalith, Boltund and Lycanroc on
  admins; Zoroark, Gholdengo and, in the final fight only, Zacian
- Several of those species are **deliberately not in the regional dex** - the
  teams field hardware the player cannot catch
- **Trainers turn to face the player** before battling
- **The rival calls on the Pokenav**, with encounter scripts across Littleroot,
  Oldale, Rustboro, Lavaridge and Routes 103 to 119
- Elite Four and Champion teams rebuilt, with the Champion holding a second,
  harder team for the rematch

## Not changed

The Hoenn map itself is intact - the same towns, routes and gyms in the same
places, aside from the three legendary dens added to Routes 104, 111 and 119,
and the story beats follow Emerald's shape.
