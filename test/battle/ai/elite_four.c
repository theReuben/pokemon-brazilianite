#include "global.h"
#include "test/battle.h"
#include "battle_ai_util.h"

// The flag set the ELITE FOUR and the CHAMPION carry in trainers.party. On bare
// AI_FLAG_BASIC_TRAINER they only ever reached for their best damaging move, so
// the hazards, recovery and phazing on their sets never came out; POWERFUL_STATUS
// and HP_AWARE are what let those moves win a turn. Deliberately not
// AI_FLAG_SMART_TRAINER - that pulls in AI_FLAG_OMNISCIENT, and an ELITE FOUR that
// plays against your actual sets reads as unfair rather than clever.
#define ELITE_FOUR_AI_FLAGS (AI_FLAG_BASIC_TRAINER | AI_FLAG_POWERFUL_STATUS | AI_FLAG_HP_AWARE)

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
