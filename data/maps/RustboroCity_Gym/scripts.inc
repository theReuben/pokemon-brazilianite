RustboroCity_Gym_MapScripts::
	.byte 0

RustboroCity_Gym_EventScript_Roxanne::
	trainerbattle_single TRAINER_ROXANNE_1, RustboroCity_Gym_Text_RoxanneIntro, RustboroCity_Gym_Text_RoxanneDefeat, RustboroCity_Gym_EventScript_RoxanneDefeated, NO_MUSIC
	specialvar VAR_RESULT, ShouldTryRematchBattle
	goto_if_eq VAR_RESULT, TRUE, RustboroCity_Gym_EventScript_RoxanneRematch
	goto_if_unset FLAG_RECEIVED_TM_ROCK_TOMB, RustboroCity_Gym_EventScript_GiveGymTM
	msgbox RustboroCity_Gym_Text_RoxannePostBattle, MSGBOX_DEFAULT
	release
	end

RustboroCity_Gym_EventScript_RoxanneDefeated::
	message RustboroCity_Gym_Text_ReceivedStoneBadge
	waitmessage
	call Common_EventScript_PlayGymBadgeFanfare
	msgbox RustboroCity_Gym_Text_StoneBadgeInfoTakeThis, MSGBOX_DEFAULT
	setflag FLAG_DEFEATED_RUSTBORO_GYM
	setflag FLAG_BADGE01_GET
	setvar VAR_RUSTBORO_CITY_STATE, 1
	addvar VAR_PETALBURG_GYM_STATE, 1
	setvar VAR_0x8008, 1
	call Common_EventScript_SetGymTrainers
	call_if_eq VAR_PETALBURG_GYM_STATE, 6, Common_EventScript_ReadyPetalburgGymForBattle
	goto RustboroCity_Gym_EventScript_GiveGymTM
	end

RustboroCity_Gym_EventScript_GiveGymTM::
	giveitem ITEM_TM_SHOCK_WAVE
	goto_if_eq VAR_RESULT, FALSE, Common_EventScript_ShowBagIsFull
	setflag FLAG_RECEIVED_TM_ROCK_TOMB
	msgbox RustboroCity_Gym_Text_ExplainShockWave, MSGBOX_DEFAULT
	release
	end

RustboroCity_Gym_EventScript_RoxanneRematch::
	trainerbattle_rematch_double TRAINER_ROXANNE_1, RustboroCity_Gym_Text_RoxannePreRematch, RustboroCity_Gym_Text_RoxanneRematchDefeat, RustboroCity_Gym_Text_RoxanneRematchNeedTwoMons
	msgbox RustboroCity_Gym_Text_RoxannePostRematch, MSGBOX_AUTOCLOSE
	end

RustboroCity_Gym_EventScript_Josh::
	trainerbattle_single TRAINER_JOSH, RustboroCity_Gym_Text_JoshIntro, RustboroCity_Gym_Text_JoshDefeat
	msgbox RustboroCity_Gym_Text_JoshPostBattle, MSGBOX_AUTOCLOSE
	end

RustboroCity_Gym_EventScript_Tommy::
	trainerbattle_single TRAINER_TOMMY, RustboroCity_Gym_Text_TommyIntro, RustboroCity_Gym_Text_TommyDefeat
	msgbox RustboroCity_Gym_Text_TommyPostBattle, MSGBOX_AUTOCLOSE
	end

RustboroCity_Gym_EventScript_Marc::
	trainerbattle_single TRAINER_MARC, RustboroCity_Gym_Text_MarcIntro, RustboroCity_Gym_Text_MarcDefeat
	msgbox RustboroCity_Gym_Text_MarcPostBattle, MSGBOX_AUTOCLOSE
	end

RustboroCity_Gym_EventScript_GymGuide::
	lock
	faceplayer
	goto_if_set FLAG_DEFEATED_RUSTBORO_GYM, RustboroCity_Gym_EventScript_GymGuidePostVictory
	msgbox RustboroCity_Gym_Text_GymGuideAdvice, MSGBOX_DEFAULT
	release
	end

RustboroCity_Gym_EventScript_GymGuidePostVictory::
	msgbox RustboroCity_Gym_Text_GymGuidePostVictory, MSGBOX_DEFAULT
	release
	end

RustboroCity_Gym_EventScript_LeftGymStatue::
	lockall
	goto_if_set FLAG_BADGE01_GET, RustboroCity_Gym_EventScript_GymStatueCertified
	goto RustboroCity_Gym_EventScript_GymStatue
	end

RustboroCity_Gym_EventScript_RightGymStatue::
	lockall
	goto_if_set FLAG_BADGE01_GET, RustboroCity_Gym_EventScript_GymStatueCertified
	goto RustboroCity_Gym_EventScript_GymStatue
	end

RustboroCity_Gym_EventScript_GymStatueCertified::
	msgbox RustboroCity_Gym_Text_GymStatueCertified, MSGBOX_DEFAULT
	releaseall
	end

RustboroCity_Gym_EventScript_GymStatue::
	msgbox RustboroCity_Gym_Text_GymStatue, MSGBOX_DEFAULT
	releaseall
	end

RustboroCity_Gym_EventScript_RegisterRoxanne::
	lockall
	pokenavcall RustboroCity_Gym_Text_RoxanneRegisterCall
	waitmessage
	delay 30
	playfanfare MUS_REGISTER_MATCH_CALL
	msgbox RustboroCity_Gym_Text_RegisteredRoxanne, MSGBOX_DEFAULT
	waitfanfare
	closemessage
	delay 30
	setflag FLAG_ENABLE_ROXANNE_MATCH_CALL
	clearflag FLAG_ENABLE_ROXANNE_FIRST_CALL
	releaseall
	end

RustboroCity_Gym_Text_GymGuideAdvice:
	.string "Yo, how's it going?\p"
	.string "Listen, my friend! Would you like to\n"
	.string "become the CHAMPION?\p"
	.string "I'm no TRAINER, not me, but I can\n"
	.string "sure give you winning advice.\p"
	.string "So! This is the ROCK GYM.\p"
	.string "And before you ask, no, not that\n"
	.string "kind of rock. Everybody asks.\p"
	.string "LIL WAYNE runs the place, and every\n"
	.string "POKéMON in here gets TURNT.\p"
	.string "Bring something that doesn't mind\n"
	.string "getting LIT!\p"
	.string "Come see me afterwards, if you beat\n"
	.string "the GYM LEADER.\p"
	.string "Well, go for it!$"

RustboroCity_Gym_Text_GymGuidePostVictory:
	.string "Whoa! What a breathtaking victory!\n"
	.string "My cheering must've worked!\p"
	.string "Well. My cheering, and the six\n"
	.string "amplifiers behind me.\p"
	.string "Great!\n"
	.string "Check your TRAINER CARD.\p"
	.string "SHOTS! SHOTS! SHOTS! should be\n"
	.string "properly recorded on it.\p"
	.string "In other words…\p"
	.string "You've licked the salt and\n"
	.string "sucked the lime!\p"
	.string "That's got to feel awesome!$"

RustboroCity_Gym_Text_JoshIntro:
	.string "Don't take us GYM TRAINERS lightly!\n"
	.string "I've been practising my bars!$"

RustboroCity_Gym_Text_JoshDefeat:
	.string "You were too good for me…$"

RustboroCity_Gym_Text_JoshPostBattle:
	.string "Get it? It's a pun. Cos\n"
	.string "we like music and drinking.$"

RustboroCity_Gym_Text_TommyIntro:
	.string "If you can't beat me, you won't stand\n"
	.string "a chance against LIL WAYNE!$"

RustboroCity_Gym_Text_TommyDefeat:
	.string "Wow! You've got some potential!$"

RustboroCity_Gym_Text_TommyPostBattle:
	.string "LIL WAYNE is tougher than\n"
	.string "Nigerian hair.\p"
	.string "Young Money millionaire!$"

RustboroCity_Gym_Text_MarcIntro:
	.string "Did you know LIL WAYNE was\n"
	.string "also on Down?\p"
	.string "You know, Jay Sean\n"
	.string "even if the sky is falling down.$"

RustboroCity_Gym_Text_MarcDefeat:
	.string "Oh, man oh man!\n"
	.string "Our challenger is one feisty customer!$"

RustboroCity_Gym_Text_MarcPostBattle:
	.string "It's a really underrated track\p"
	.string "Well, maybe not underrated\n"
	.string "but people forget it.$"

RustboroCity_Gym_Text_RoxanneIntro:
	.string "LIL WAYNE: Ay. Welcome to the ROCK\n"
	.string "GYM. You look confused already.\p"
	.string "Everybody walks in here expecting\n"
	.string "boulders. I don't do boulders.\p"
	.string "I do SHOTS!\p"
	.string "Let's see if your POKéMON can keep\n"
	.string "up, let the henny flow!$"

RustboroCity_Gym_Text_RoxanneDefeat:
	.string "Man…\n"
	.string "You took the whole set.\p"
	.string "Alright. Alright! That's how it goes.\p"
	.string "The POKéMON LEAGUE's rules state\n"
	.string "that TRAINERS are to be given this\l"
	.string "if they defeat a GYM LEADER.\p"
	.string "SHOTS! SHOTS! SHOTS!\n"
	.string "Aight, I gotta go record more of\l"
	.string "the spiderverse soundtrack.$"

RustboroCity_Gym_Text_ReceivedStoneBadge:
	.string "{PLAYER} received SHOTS! SHOTS!\n"
	.string "SHOTS! from LIL WAYNE.$"

RustboroCity_Gym_Text_StoneBadgeInfoTakeThis:
	.string "SHOTS! SHOTS! SHOTS! heightens the\n"
	.string "ATTACK power of your POKéMON.\p"
	.string "It also enables them to use the HM move\n"
	.string "CUT outside of battle.\p"
	.string "Please take this with you, too.$"

RustboroCity_Gym_Text_ExplainShockWave:
	.string "That TECHNICAL MACHINE, TM34,\n"
	.string "contains SHOCK WAVE.\p"
	.string "It's ELECTRIC, and it never misses.\n"
	.string "No misses. That's the whole point.\p"
	.string "If you use a TM, it instantly teaches\n"
	.string "the move to a POKéMON.\p"
	.string "Remember, a TM can be used only once,\n"
	.string "so think before you use it.$"

RustboroCity_Gym_Text_RoxannePostBattle:
	.string "Since you are so strong, you should\n"
	.string "challenge other GYM LEADERS.\p"
	.string "Word travels. Music travels faster.$"

RustboroCity_Gym_Text_GymStatue:
	.string "RUSTBORO CITY POKéMON GYM$"

RustboroCity_Gym_Text_GymStatueCertified:
	.string "RUSTBORO CITY POKéMON GYM\p"
	.string "LIL WAYNE'S CERTIFIED TRAINERS:\n"
	.string "{PLAYER}$"

RustboroCity_Gym_Text_RoxanneRegisterCall:
	.string "… … … … … …\n"
	.string "… … … … … Beep!\p"
	.string "LIL WAYNE: Ay, that {PLAYER}?\n"
	.string "It's WAYNE, RUSTBORO CITY.\p"
	.string "I heard from MERLOT you been moving\n"
	.string "up the ranks at a crazy pace.\p"
	.string "I'd rather not sit here thinking\n"
	.string "I can't beat you.\p"
	.string "So I'm rebuilding the whole set.\n"
	.string "Bigger. Louder. Come see it.\p"
	.string "… … … … … …\n"
	.string "… … … … … Click!$"

RustboroCity_Gym_Text_RegisteredRoxanne:
	.string "Registered GYM LEADER LIL WAYNE\n"
	.string "in the POKéNAV.$"

RustboroCity_Gym_Text_RoxannePreRematch:
	.string "LIL WAYNE: Ay, look who's back.\n"
	.string "New set. Same GYM.\p"
	.string "We both been through a lot of battles\n"
	.string "since you were last in here.\p"
	.string "Let's hear what you got.$"

RustboroCity_Gym_Text_RoxanneRematchDefeat:
	.string "Grr…\n"
	.string "Beat again, in my own house…$"

RustboroCity_Gym_Text_RoxannePostRematch:
	.string "LIL WAYNE: I still got things to learn\n"
	.string "about battling POKéMON.\p"
	.string "That's the part I like, though.\n"
	.string "You're never finished.$"

RustboroCity_Gym_Text_RoxanneRematchNeedTwoMons:
	.string "LIL WAYNE: Ay, look who's back.\n"
	.string "New set. Same GYM.\p"
	.string "We both been through a lot of battles\n"
	.string "since you were last in here.\p"
	.string "Let's hear what you…\p"
	.string "Hold up.\n"
	.string "You only brought one POKéMON?\p"
	.string "It's a double set. Go get at least\n"
	.string "one more.$"
