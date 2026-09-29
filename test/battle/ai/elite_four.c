#include "global.h"
#include "test/battle.h"
#include "battle_ai_util.h"

// The flag set the ELITE FOUR and the CHAMPION carry in trainers.party. On plain
// AI_FLAG_BASIC_TRAINER they only ever reached for their best damaging move, so
// the hazards, recovery and phazing on their sets never came out.
#define ELITE_FOUR_AI_FLAGS (AI_FLAG_SMART_TRAINER | AI_FLAG_POWERFUL_STATUS | AI_FLAG_HP_AWARE)

AI_SINGLE_BATTLE_TEST("ELITE FOUR AI sets hazards rather than always attacking")
{
    GIVEN {
        ASSUME(GetMoveEffect(MOVE_STEALTH_ROCK) == EFFECT_STEALTH_ROCK);
        AI_FLAGS(ELITE_FOUR_AI_FLAGS);
        PLAYER(SPECIES_WOBBUFFET);
        PLAYER(SPECIES_WYNAUT);
        OPPONENT(SPECIES_HIPPOWDON) { Moves(MOVE_STEALTH_ROCK, MOVE_EARTHQUAKE, MOVE_SLACK_OFF, MOVE_WHIRLWIND); }
    } WHEN {
        TURN { EXPECT_MOVE(opponent, MOVE_STEALTH_ROCK); }
    }
}
