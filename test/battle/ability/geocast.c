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
