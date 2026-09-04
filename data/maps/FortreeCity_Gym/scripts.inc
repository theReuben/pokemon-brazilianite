FortreeCity_Gym_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, FortreeCity_Gym_OnTransition
	map_script MAP_SCRIPT_ON_WARP_INTO_MAP_TABLE, FortreeCity_Gym_OnWarp
	.byte 0

FortreeCity_Gym_OnTransition:
	special RotatingGate_InitPuzzle
	setflag FLAG_TEMP_HIDE_FOLLOWER @ Hide follower bc of rotating gates
	end

FortreeCity_Gym_OnWarp:
	map_script_2 VAR_TEMP_0, VAR_TEMP_0, FortreeCity_Gym_EventScript_InitRotatingGates
	.2byte 0

@ NOTE: This rotating gate puzzle makes use of VAR_TEMP_0 - VAR_TEMP_3
FortreeCity_Gym_EventScript_InitRotatingGates::
	special RotatingGate_InitPuzzleAndGraphics
	end

FortreeCity_Gym_EventScript_Winona::
	trainerbattle_single TRAINER_WINONA_1, FortreeCity_Gym_Text_WinonaIntro, FortreeCity_Gym_Text_WinonaDefeat, FortreeCity_Gym_EventScript_WinonaDefeated, NO_MUSIC
	specialvar VAR_RESULT, ShouldTryRematchBattle
	goto_if_eq VAR_RESULT, TRUE, FortreeCity_Gym_EventScript_WinonaRematch
	goto_if_unset FLAG_RECEIVED_TM_AERIAL_ACE, FortreeCity_Gym_EventScript_GivePoisonFang2
	msgbox FortreeCity_Gym_Text_WinonaPostBattle, MSGBOX_DEFAULT
	release
	end

FortreeCity_Gym_EventScript_WinonaDefeated::
	message FortreeCity_Gym_Text_ReceivedFeatherBadge
	waitmessage
	call Common_EventScript_PlayGymBadgeFanfare
	msgbox FortreeCity_Gym_Text_ExplainFeatherBadgeTakeThis, MSGBOX_DEFAULT
	setflag FLAG_DEFEATED_FORTREE_GYM
	setflag FLAG_BADGE06_GET
	setvar VAR_0x8008, 6
	call Common_EventScript_SetGymTrainers
	call FortreeCity_Gym_EventScript_GivePoisonFang
	closemessage
	delay 30
	playfanfare MUS_REGISTER_MATCH_CALL
	msgbox FortreeCity_Gym_Text_RegisteredWinona, MSGBOX_DEFAULT
	waitfanfare
	closemessage
	delay 30
	setflag FLAG_ENABLE_WINONA_MATCH_CALL
	setvar VAR_SCOTT_FORTREE_CALL_STEP_COUNTER, 0
	setflag FLAG_SCOTT_CALL_FORTREE_GYM
	release
	end

FortreeCity_Gym_EventScript_GivePoisonFang2::
	giveitem ITEM_TM_POISON_FANG
	goto_if_eq VAR_RESULT, FALSE, Common_EventScript_ShowBagIsFull
	msgbox FortreeCity_Gym_Text_ExplainPoisonFang, MSGBOX_DEFAULT
	setflag FLAG_RECEIVED_TM_AERIAL_ACE
	release
	end

FortreeCity_Gym_EventScript_GivePoisonFang::
	giveitem ITEM_TM_POISON_FANG
	goto_if_eq VAR_RESULT, FALSE, Common_EventScript_BagIsFull
	msgbox FortreeCity_Gym_Text_ExplainPoisonFang, MSGBOX_DEFAULT
	setflag FLAG_RECEIVED_TM_AERIAL_ACE
	return

FortreeCity_Gym_EventScript_WinonaRematch::
	trainerbattle_rematch_double TRAINER_WINONA_1, FortreeCity_Gym_Text_WinonaPreRematch, FortreeCity_Gym_Text_WinonaRematchDefeat, FortreeCity_Gym_Text_WinonaRematchNeedTwoMons
	msgbox FortreeCity_Gym_Text_WinonaPostRematch, MSGBOX_AUTOCLOSE
	end

FortreeCity_Gym_EventScript_Jared::
	trainerbattle_single TRAINER_JARED, FortreeCity_Gym_Text_JaredIntro, FortreeCity_Gym_Text_JaredDefeat
	msgbox FortreeCity_Gym_Text_JaredPostBattle, MSGBOX_AUTOCLOSE
	end

FortreeCity_Gym_EventScript_Edwardo::
	trainerbattle_single TRAINER_EDWARDO, FortreeCity_Gym_Text_EdwardoIntro, FortreeCity_Gym_Text_EdwardoDefeat
	msgbox FortreeCity_Gym_Text_EdwardoPostBattle, MSGBOX_AUTOCLOSE
	end

FortreeCity_Gym_EventScript_Flint::
	trainerbattle_single TRAINER_FLINT, FortreeCity_Gym_Text_FlintIntro, FortreeCity_Gym_Text_FlintDefeat
	msgbox FortreeCity_Gym_Text_FlintPostBattle, MSGBOX_AUTOCLOSE
	end

FortreeCity_Gym_EventScript_Ashley::
	trainerbattle_single TRAINER_ASHLEY, FortreeCity_Gym_Text_AshleyIntro, FortreeCity_Gym_Text_AshleyDefeat
	msgbox FortreeCity_Gym_Text_AshleyPostBattle, MSGBOX_AUTOCLOSE
	end

FortreeCity_Gym_EventScript_Humberto::
	trainerbattle_single TRAINER_HUMBERTO, FortreeCity_Gym_Text_HumbertoIntro, FortreeCity_Gym_Text_HumbertoDefeat
	msgbox FortreeCity_Gym_Text_HumbertoPostBattle, MSGBOX_AUTOCLOSE
	end

FortreeCity_Gym_EventScript_Darius::
	trainerbattle_single TRAINER_DARIUS, FortreeCity_Gym_Text_DariusIntro, FortreeCity_Gym_Text_DariusDefeat
	msgbox FortreeCity_Gym_Text_DariusPostBattle, MSGBOX_AUTOCLOSE
	end

FortreeCity_Gym_EventScript_GymGuide::
	lock
	faceplayer
	goto_if_set FLAG_DEFEATED_FORTREE_GYM, FortreeCity_Gym_EventScript_GymGuidePostVictory
	msgbox FortreeCity_Gym_Text_GymGuideAdvice, MSGBOX_DEFAULT
	release
	end

FortreeCity_Gym_EventScript_GymGuidePostVictory::
	msgbox FortreeCity_Gym_Text_GymGuidePostVictory, MSGBOX_DEFAULT
	release
	end

FortreeCity_Gym_EventScript_LeftGymStatue::
	lockall
	goto_if_set FLAG_BADGE06_GET, FortreeCity_Gym_EventScript_GymStatueCertified
	goto FortreeCity_Gym_EventScript_GymStatue
	end

FortreeCity_Gym_EventScript_RightGymStatue::
	lockall
	goto_if_set FLAG_BADGE06_GET, FortreeCity_Gym_EventScript_GymStatueCertified
	goto FortreeCity_Gym_EventScript_GymStatue
	end

FortreeCity_Gym_EventScript_GymStatueCertified::
	msgbox FortreeCity_Gym_Text_GymStatueCertified, MSGBOX_DEFAULT
	releaseall
	end

FortreeCity_Gym_EventScript_GymStatue::
	msgbox FortreeCity_Gym_Text_GymStatue, MSGBOX_DEFAULT
	releaseall
	end

FortreeCity_Gym_Text_GymGuideAdvice:
	.string "Yo, how's it going, CHAMPION-\n"
	.string "bound {PLAYER}?\p"
	.string "FORTREE GYM is the snake GYM.\p"
	.string "There are only six snakes. That's it.\n"
	.string "That's all of them.\p"
	.string "You'll meet every one on the way in,\n"
	.string "then WINONA brings all six at once.\p"
	.string "Bring something that isn't scared of\n"
	.string "the ground. Go for it!$"

FortreeCity_Gym_Text_GymGuidePostVictory:
	.string "You did it!\n"
	.string "And you still have all your ankles!$"

FortreeCity_Gym_Text_JaredIntro:
	.string "Six weeks I've been camped in here.\p"
	.string "You get used to the sound.\n"
	.string "You never get used to the sound.$"

FortreeCity_Gym_Text_JaredDefeat:
	.string "You…\n"
	.string "You're strong…$"

FortreeCity_Gym_Text_JaredPostBattle:
	.string "Rule one of camping in the FORTREE\n"
	.string "GYM: check the sleeping bag.\p"
	.string "Rule two: check it again.\p"
	.string "There is no rule three. Rule two\n"
	.string "covers it.$"

FortreeCity_Gym_Text_EdwardoIntro:
	.string "People ask why we pitch tents in\n"
	.string "a GYM.\p"
	.string "Nobody wants to sleep on the floor\n"
	.string "in here. Nobody.$"

FortreeCity_Gym_Text_EdwardoDefeat:
	.string "Constricted…\n"
	.string "Comprehensively…$"

FortreeCity_Gym_Text_EdwardoPostBattle:
	.string "The world is huge, and there are\n"
	.string "countless tough TRAINERS.\p"
	.string "Most of them sleep indoors, though.\n"
	.string "Cowards, all of them.$"

FortreeCity_Gym_Text_FlintIntro:
	.string "There's no need for WINONA, our GYM\n"
	.string "LEADER, to deal with you!\p"
	.string "I've got a tent and a snake.\n"
	.string "That's plenty good enough for you!$"

FortreeCity_Gym_Text_FlintDefeat:
	.string "WINONA, I…\n"
	.string "I lost!$"

FortreeCity_Gym_Text_FlintPostBattle:
	.string "WINONA is cute and she's strong.\n"
	.string "She's the ultimate LEADER!\p"
	.string "She sleeps with all six of them.\n"
	.string "Blush…$"

FortreeCity_Gym_Text_AshleyIntro:
	.string "WINONA taught me personally!\p"
	.string "First lesson was where to put your\n"
	.string "hands. Second lesson was the same.$"

FortreeCity_Gym_Text_AshleyDefeat:
	.string "I was beaten…$"

FortreeCity_Gym_Text_AshleyPostBattle:
	.string "Thanks to WINONA, the people of\n"
	.string "FORTREE can live without fear.\p"
	.string "They live in the trees, mind you.\n"
	.string "But without fear.$"

FortreeCity_Gym_Text_HumbertoIntro:
	.string "When WINONA takes to battle, her face\n"
	.string "shines with beautiful determination…\p"
	.string "So does the ZYGARDE. Different\n"
	.string "reasons.\p"
	.string "I'm not letting you witness either!$"

FortreeCity_Gym_Text_HumbertoDefeat:
	.string "Urk!\n"
	.string "I couldn't stop you.$"

FortreeCity_Gym_Text_HumbertoPostBattle:
	.string "You'd better watch it!\n"
	.string "Don't get distracted staring at WINONA\l"
	.string "or you'll stand on something.\p"
	.string "Everything in here is something.$"

FortreeCity_Gym_Text_DariusIntro:
	.string "You'd better know that there are all\n"
	.string "sorts of snakes.\p"
	.string "Six. There are six sorts.$"

FortreeCity_Gym_Text_DariusDefeat:
	.string "You seem to know your stuff!$"

FortreeCity_Gym_Text_DariusPostBattle:
	.string "Sure, you beat me all right.\n"
	.string "But you'd better watch it! Our LEADER\l"
	.string "WINONA's POKéMON are all business.$"

FortreeCity_Gym_Text_WinonaIntro:
	.string "I am WINONA. I am the LEADER of\n"
	.string "the FORTREE POKéMON GYM.\p"
	.string "I have become one with the six.\n"
	.string "There are only six. I have all six.\p"
	.string "However grueling the battle, we have\n"
	.string "triumphed without limbs…\p"
	.string "Witness the elegant choreography\n"
	.string "of a thing with no shoulders!$"

FortreeCity_Gym_Text_WinonaDefeat:
	.string "Never before have I seen a TRAINER\n"
	.string "command POKéMON with more grace\l"
	.string "than I…\p"
	.string "And I did not have to be told twice\n"
	.string "where the head was.\p"
	.string "In recognition of your prowess,\n"
	.string "I present to you this GYM BADGE.$"

FortreeCity_Gym_Text_ReceivedFeatherBadge:
	.string "{PLAYER} received THE SEVENTH SNAKE\n"
	.string "from WINONA.$"

FortreeCity_Gym_Text_ExplainFeatherBadgeTakeThis:
	.string "With THE SEVENTH SNAKE, POKéMON up\n"
	.string "to LV 70, even those received through\l"
	.string "trades, will obey your every command.\p"
	.string "You will also be able to use\n"
	.string "the HM move FLY outside of battle.\p"
	.string "And this…\n"
	.string "This is a gift from me.$"

FortreeCity_Gym_Text_ExplainPoisonFang:
	.string "TM51 contains POISON FANG.\p"
	.string "A bite that may leave the target\n"
	.string "badly poisoned.\p"
	.string "Every snake in here knows it.\p"
	.string "… … … … … …$"

FortreeCity_Gym_Text_RegisteredWinona:
	.string "Registered GYM LEADER WINONA\n"
	.string "in the POKéNAV.$"

FortreeCity_Gym_Text_WinonaPostBattle:
	.string "Though I fell to you, I will remain\n"
	.string "devoted to all six of them.\p"
	.string "Seven, counting the BADGE.$"

FortreeCity_Gym_Text_GymStatue:
	.string "FORTREE CITY POKéMON GYM$"

FortreeCity_Gym_Text_GymStatueCertified:
	.string "FORTREE CITY POKéMON GYM\p"
	.string "WINONA'S CERTIFIED TRAINERS:\n"
	.string "{PLAYER}$"

FortreeCity_Gym_Text_WinonaPreRematch:
	.string "WINONA: We humans can never escape\n"
	.string "gravity's pull on the ground.\p"
	.string "But by striving for excellence,\n"
	.string "we have the power to soar!\p"
	.string "You have scaled the pinnacle as\n"
	.string "the reigning CHAMPION.\p"
	.string "Please, allow me to see your power\n"
	.string "at full flight!$"

FortreeCity_Gym_Text_WinonaRematchDefeat:
	.string "I failed to reach your height again…$"

FortreeCity_Gym_Text_WinonaPostRematch:
	.string "WINONA: Even though I have lost,\n"
	.string "the wings of my heart remain unbroken.\p"
	.string "I can rise and soar again and\n"
	.string "yet again.\p"
	.string "I am convinced of it!$"

FortreeCity_Gym_Text_WinonaRematchNeedTwoMons:
	.string "WINONA: We humans can never escape\n"
	.string "gravity's pull on the ground.\p"
	.string "But by striving for excellence,\n"
	.string "we have the power to soar!\p"
	.string "You have scaled the pinnacle as\n"
	.string "the reigning CHAMPION.\p"
	.string "Please, allow me to see your power\n"
	.string "at full flight!\p"
	.string "Oh, no… Do you have but one\n"
	.string "POKéMON with you?\p"
	.string "Please return with two POKéMON\n"
	.string "at the very least.$"
