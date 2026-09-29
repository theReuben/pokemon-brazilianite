#include "global.h"
#include "test/battle.h"

// PRAESTA's CASTFORM: a Castformite, Forecast until it Mega Evolves into Geocast,
// and a set that is three terrains and a Terrain Pulse to fire off them.
#define PRAESTA_AI_FLAGS (AI_FLAG_BASIC_TRAINER | AI_FLAG_POWERFUL_STATUS | AI_FLAG_HP_AWARE | AI_FLAG_SMART_TERA)

// HEATRAN is Fire/Steel, so Terrain Pulse off Grassy Terrain is 0.25x, off Misty
// Terrain 0.5x and off Psychic Terrain neutral - the three terrains are three
// clearly different moves against it.
AI_SINGLE_BATTLE_TEST("Geocast AI picks its terrain by typing on the turn it Mega Evolves")
{
    GIVEN {
        AI_FLAGS(PRAESTA_AI_FLAGS);
        PLAYER(SPECIES_HEATRAN);
        OPPONENT(SPECIES_CASTFORM) { Item(ITEM_CASTFORMITE); Ability(ABILITY_FORECAST);
            Moves(MOVE_TERRAIN_PULSE, MOVE_GRASSY_TERRAIN, MOVE_MISTY_TERRAIN, MOVE_PSYCHIC_TERRAIN); }
    } WHEN {
        TURN { MOVE(player, MOVE_CELEBRATE); EXPECT_MOVE(opponent, MOVE_PSYCHIC_TERRAIN, gimmick: GIMMICK_MEGA); }
    }
}

AI_SINGLE_BATTLE_TEST("Geocast AI fires Terrain Pulse off a bad terrain rather than let a kill go")
{
    GIVEN {
        AI_FLAGS(PRAESTA_AI_FLAGS);
        PLAYER(SPECIES_HEATRAN) { HP(1); Moves(MOVE_GRASSY_TERRAIN, MOVE_FLASH_CANNON); }
        OPPONENT(SPECIES_CASTFORM_MEGA) { Ability(ABILITY_GEOCAST);
            Moves(MOVE_TERRAIN_PULSE, MOVE_GRASSY_TERRAIN, MOVE_MISTY_TERRAIN, MOVE_PSYCHIC_TERRAIN); }
    } WHEN {
        TURN { MOVE(player, MOVE_GRASSY_TERRAIN); }
        TURN { MOVE(player, MOVE_FLASH_CANNON); EXPECT_MOVE(opponent, MOVE_TERRAIN_PULSE); }
    }
}
