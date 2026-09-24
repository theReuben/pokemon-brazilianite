#include "global.h"
#include "test/battle.h"

SINGLE_BATTLE_TEST("Geocast transforms Mega Castform to match the terrain")
{
    enum Move move;
    PARAMETRIZE { move = MOVE_ELECTRIC_TERRAIN; }
    PARAMETRIZE { move = MOVE_GRASSY_TERRAIN; }
    PARAMETRIZE { move = MOVE_MISTY_TERRAIN; }
    PARAMETRIZE { move = MOVE_PSYCHIC_TERRAIN; }
    GIVEN {
        PLAYER(SPECIES_CASTFORM_MEGA) { Ability(ABILITY_GEOCAST); }
        OPPONENT(SPECIES_WOBBUFFET);
    } WHEN {
        TURN { MOVE(opponent, move); }
    } SCENE {
        ABILITY_POPUP(player, ABILITY_GEOCAST);
        ANIMATION(ANIM_TYPE_GENERAL, B_ANIM_FORM_CHANGE, player);
        MESSAGE("Castform transformed!");
    } THEN {
        switch (move)
        {
        case MOVE_ELECTRIC_TERRAIN:
            EXPECT_EQ(player->species, SPECIES_CASTFORM_MEGA_ELECTRIC);
            break;
        case MOVE_GRASSY_TERRAIN:
            EXPECT_EQ(player->species, SPECIES_CASTFORM_MEGA_GRASSY);
            break;
        case MOVE_MISTY_TERRAIN:
            EXPECT_EQ(player->species, SPECIES_CASTFORM_MEGA_MISTY);
            break;
        case MOVE_PSYCHIC_TERRAIN:
            EXPECT_EQ(player->species, SPECIES_CASTFORM_MEGA_PSYCHIC);
            break;
        default:
            break;
        }
    }
}

SINGLE_BATTLE_TEST("Geocast returns Mega Castform to its base form when the terrain ends")
{
    GIVEN {
        PLAYER(SPECIES_CASTFORM_MEGA) { Ability(ABILITY_GEOCAST); }
        OPPONENT(SPECIES_WOBBUFFET);
    } WHEN {
        // Electric Terrain lasts five turns; the sixth is bare ground
        // again, and the form has to follow it back.
        TURN { MOVE(opponent, MOVE_ELECTRIC_TERRAIN); }
        TURN {}
        TURN {}
        TURN {}
        TURN {}
        TURN {}
    } THEN {
        EXPECT_EQ(player->species, SPECIES_CASTFORM_MEGA);
    }
}

SINGLE_BATTLE_TEST("Geocast does not respond to weather")
{
    GIVEN {
        PLAYER(SPECIES_CASTFORM_MEGA) { Ability(ABILITY_GEOCAST); }
        OPPONENT(SPECIES_WOBBUFFET);
    } WHEN {
        TURN { MOVE(opponent, MOVE_SUNNY_DAY); }
    } THEN {
        // Forecast reads the sky, Geocast reads the ground. Sun must
        // leave the Mega alone, or the two mechanics are fighting over
        // the same Pokemon.
        EXPECT_EQ(player->species, SPECIES_CASTFORM_MEGA);
    }
}

SINGLE_BATTLE_TEST("Forecast does not transform Mega Castform")
{
    GIVEN {
        PLAYER(SPECIES_CASTFORM_MEGA) { Ability(ABILITY_FORECAST); }
        OPPONENT(SPECIES_WOBBUFFET);
    } WHEN {
        TURN { MOVE(opponent, MOVE_RAIN_DANCE); }
    } THEN {
        // The Mega's own form-change table has no weather entries, so
        // even with Forecast forced onto it there is nothing to match.
        EXPECT_EQ(player->species, SPECIES_CASTFORM_MEGA);
    }
}

SINGLE_BATTLE_TEST("Mega Castform stays Mega after switching out and back in")
{
    GIVEN {
        PLAYER(SPECIES_CASTFORM) { Item(ITEM_CASTFORMITE); }
        PLAYER(SPECIES_WOBBUFFET);
        OPPONENT(SPECIES_WOBBUFFET);
    } WHEN {
        TURN { MOVE(player, MOVE_TACKLE, gimmick: GIMMICK_MEGA); }
        TURN { SWITCH(player, 1); }
        TURN { SWITCH(player, 0); }
    } THEN {
        EXPECT_EQ(player->species, SPECIES_CASTFORM_MEGA);
    }
}

AI_SINGLE_BATTLE_TEST("AI sets terrain with Geocast rather than firing an unboosted Terrain Pulse")
{
    GIVEN {
        AI_FLAGS(AI_FLAG_BASIC_TRAINER);
        PLAYER(SPECIES_WOBBUFFET);
        OPPONENT(SPECIES_CASTFORM_MEGA) { Ability(ABILITY_GEOCAST); Moves(MOVE_TERRAIN_PULSE, MOVE_PSYCHIC_TERRAIN, MOVE_MISTY_TERRAIN, MOVE_GRASSY_TERRAIN); }
    } WHEN {
        TURN { EXPECT_MOVES(opponent, MOVE_PSYCHIC_TERRAIN, MOVE_MISTY_TERRAIN, MOVE_GRASSY_TERRAIN); }
        // With a terrain up the form change is done and Terrain Pulse is
        // boosted and STAB, so with no better typing on offer it attacks.
        TURN { EXPECT_MOVE(opponent, MOVE_TERRAIN_PULSE); }
    }
}

AI_SINGLE_BATTLE_TEST("AI picks the Geocast terrain whose typing beats the target")
{
    GIVEN {
        AI_FLAGS(AI_FLAG_BASIC_TRAINER);
        PLAYER(SPECIES_QUAGSIRE);
        OPPONENT(SPECIES_CASTFORM_MEGA) { Ability(ABILITY_GEOCAST); Moves(MOVE_TERRAIN_PULSE, MOVE_PSYCHIC_TERRAIN, MOVE_MISTY_TERRAIN, MOVE_GRASSY_TERRAIN); }
    } WHEN {
        // Grass is 4x on Quagsire, while Psychic and Fairy are neutral.
        TURN { EXPECT_MOVE(opponent, MOVE_GRASSY_TERRAIN); }
    }
}

AI_SINGLE_BATTLE_TEST("AI re-picks its Geocast terrain when the player switches in a better matchup")
{
    GIVEN {
        AI_FLAGS(AI_FLAG_BASIC_TRAINER);
        PLAYER(SPECIES_QUAGSIRE);
        PLAYER(SPECIES_TOXICROAK);
        OPPONENT(SPECIES_CASTFORM_MEGA) { Ability(ABILITY_GEOCAST); Moves(MOVE_TERRAIN_PULSE, MOVE_PSYCHIC_TERRAIN, MOVE_MISTY_TERRAIN, MOVE_GRASSY_TERRAIN); }
    } WHEN {
        TURN { EXPECT_MOVE(opponent, MOVE_GRASSY_TERRAIN); }
        // The AI commits to its move before the switch resolves, so this
        // turn it is still aiming at Quagsire.
        TURN { SWITCH(player, 1); }
        // Now it sees Toxicroak: Poison/Fighting shrugs off a Grass pulse but
        // folds to a Psychic one, so the turn spent swapping pays for itself.
        TURN { EXPECT_MOVE(opponent, MOVE_PSYCHIC_TERRAIN); }
    }
}

