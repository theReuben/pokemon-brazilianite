DewfordTown_Gym_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, DewfordTown_Gym_OnTransition
	.byte 0

DewfordTown_Gym_OnTransition:
	call DewfordTown_Gym_EventScript_SetFlashLevel
	end

DewfordTown_Gym_EventScript_SetFlashLevel::
	goto_if_defeated TRAINER_BRAWLY_1, DewfordTown_Gym_EventScript_SetLightsOn
	call DewfordTown_Gym_EventScript_CountTrainersDefeated
	copyvar VAR_0x8001, VAR_0x8000
	goto_if_eq VAR_0x8000, 0, DewfordTown_Gym_EventScript_SetFlashLevel7
	goto_if_eq VAR_0x8000, 1, DewfordTown_Gym_EventScript_SetFlashLevel6
	goto_if_eq VAR_0x8000, 2, DewfordTown_Gym_EventScript_SetFlashLevel5
	goto_if_eq VAR_0x8000, 3, DewfordTown_Gym_EventScript_SetFlashLevel4
	goto_if_eq VAR_0x8000, 4, DewfordTown_Gym_EventScript_SetFlashLevel3
	goto_if_eq VAR_0x8000, 5, DewfordTown_Gym_EventScript_SetFlashLevel2
	goto DewfordTown_Gym_EventScript_SetFlashLevel1

DewfordTown_Gym_EventScript_SetLightsOn::
	setflashlevel 0
	return

@ Brightest
DewfordTown_Gym_EventScript_SetFlashLevel1::
	setflashlevel 1
	return

DewfordTown_Gym_EventScript_SetFlashLevel2::
	setflashlevel 2
	return

DewfordTown_Gym_EventScript_SetFlashLevel3::
	setflashlevel 3
	return

DewfordTown_Gym_EventScript_SetFlashLevel4::
	setflashlevel 4
	return

DewfordTown_Gym_EventScript_SetFlashLevel5::
	setflashlevel 5
	return

DewfordTown_Gym_EventScript_SetFlashLevel6::
	setflashlevel 6
	return

@ Darkest
DewfordTown_Gym_EventScript_SetFlashLevel7::
	setflashlevel 7
	return

DewfordTown_Gym_EventScript_BrightenRoom::
	call DewfordTown_Gym_EventScript_CountTrainersDefeated
	nop1
	goto_if_eq VAR_0x8000, VAR_0x8001, DewfordTown_Gym_EventScript_NoLightChange
	copyvar VAR_0x8001, VAR_0x8000
	goto_if_eq VAR_0x8000, 1, DewfordTown_Gym_EventScript_AnimateFlash1Trainer
	goto_if_eq VAR_0x8000, 2, DewfordTown_Gym_EventScript_AnimateFlash2Trainers
	goto_if_eq VAR_0x8000, 3, DewfordTown_Gym_EventScript_AnimateFlash3Trainers
	goto_if_eq VAR_0x8000, 4, DewfordTown_Gym_EventScript_AnimateFlash4Trainers
	goto_if_eq VAR_0x8000, 5, DewfordTown_Gym_EventScript_AnimateFlash5Trainers
	goto_if_eq VAR_0x8000, 6, DewfordTown_Gym_EventScript_AnimateFlash6Trainers

DewfordTown_Gym_EventScript_NoLightChange::
	return

@ NOTE: A little confusingly, a larger animateflash param value is a smaller flash radius
DewfordTown_Gym_EventScript_AnimateFlash1Trainer::
	playse SE_SWITCH
	animateflash 6
	call DewfordTown_Gym_EventScript_SetFlashLevel
	return

DewfordTown_Gym_EventScript_AnimateFlash2Trainers::
	playse SE_SWITCH
	animateflash 5
	call DewfordTown_Gym_EventScript_SetFlashLevel
	return

DewfordTown_Gym_EventScript_AnimateFlash3Trainers::
	playse SE_SWITCH
	animateflash 4
	call DewfordTown_Gym_EventScript_SetFlashLevel
	return

DewfordTown_Gym_EventScript_AnimateFlash4Trainers::
	playse SE_SWITCH
	animateflash 3
	call DewfordTown_Gym_EventScript_SetFlashLevel
	return

DewfordTown_Gym_EventScript_AnimateFlash5Trainers::
	playse SE_SWITCH
	animateflash 2
	call DewfordTown_Gym_EventScript_SetFlashLevel
	return

DewfordTown_Gym_EventScript_AnimateFlash6Trainers::
	playse SE_SWITCH
	animateflash 1
	call DewfordTown_Gym_EventScript_SetFlashLevel
	return

DewfordTown_Gym_EventScript_AnimateFlashFullBrightness::
	playse SE_SWITCH
	animateflash 0
	call DewfordTown_Gym_EventScript_SetFlashLevel
	return

DewfordTown_Gym_EventScript_CountTrainersDefeated::
	setvar VAR_0x8000, 0
	goto_if_not_defeated TRAINER_TAKAO, DewfordTown_Gym_EventScript_CheckJocelyn
	addvar VAR_0x8000, 1
DewfordTown_Gym_EventScript_CheckJocelyn::
	goto_if_not_defeated TRAINER_JOCELYN, DewfordTown_Gym_EventScript_CheckLaura
	addvar VAR_0x8000, 1
DewfordTown_Gym_EventScript_CheckLaura::
	goto_if_not_defeated TRAINER_LAURA, DewfordTown_Gym_EventScript_CheckBrenden
	addvar VAR_0x8000, 1
DewfordTown_Gym_EventScript_CheckBrenden::
	goto_if_not_defeated TRAINER_BRENDEN, DewfordTown_Gym_EventScript_CheckCristian
	addvar VAR_0x8000, 1
DewfordTown_Gym_EventScript_CheckCristian::
	goto_if_not_defeated TRAINER_CRISTIAN, DewfordTown_Gym_EventScript_CheckLilith
	addvar VAR_0x8000, 1
DewfordTown_Gym_EventScript_CheckLilith::
	goto_if_not_defeated TRAINER_LILITH, DewfordTown_Gym_EventScript_StopCountingTrainers
	addvar VAR_0x8000, 1
DewfordTown_Gym_EventScript_StopCountingTrainers::
	return

DewfordTown_Gym_EventScript_Brawly::
	trainerbattle_single TRAINER_BRAWLY_1, DewfordTown_Gym_Text_BrawlyIntro, DewfordTown_Gym_Text_BrawlyDefeat, DewfordTown_Gym_EventScript_BrawlyDefeated, NO_MUSIC
	specialvar VAR_RESULT, ShouldTryRematchBattle
	goto_if_eq VAR_RESULT, TRUE, DewfordTown_Gym_EventScript_BrawlyRematch
	goto_if_unset FLAG_RECEIVED_TM_BULK_UP, DewfordTown_Gym_EventScript_GiveGymTM2
	msgbox DewfordTown_Gym_Text_BrawlyPostBattle, MSGBOX_DEFAULT
	release
	end

DewfordTown_Gym_EventScript_BrawlyDefeated::
	call DewfordTown_Gym_EventScript_AnimateFlashFullBrightness
	message DewfordTown_Gym_Text_ReceivedKnuckleBadge
	waitmessage
	call Common_EventScript_PlayGymBadgeFanfare
	msgbox DewfordTown_Gym_Text_KnuckleBadgeInfoTakeThis, MSGBOX_DEFAULT
	setflag FLAG_DEFEATED_DEWFORD_GYM
	setflag FLAG_BADGE02_GET
	addvar VAR_PETALBURG_GYM_STATE, 1
	call_if_eq VAR_PETALBURG_GYM_STATE, 6, Common_EventScript_ReadyPetalburgGymForBattle
	setvar VAR_0x8008, 2
	call Common_EventScript_SetGymTrainers
	call DewfordTown_Gym_EventScript_GiveGymTM
	closemessage
	delay 30
	playfanfare MUS_REGISTER_MATCH_CALL
	msgbox DewfordTown_Gym_Text_RegisteredBrawly, MSGBOX_DEFAULT
	waitfanfare
	closemessage
	delay 30
	setflag FLAG_ENABLE_BRAWLY_MATCH_CALL
	setvar VAR_ROXANNE_CALL_STEP_COUNTER, 0
	setflag FLAG_ENABLE_ROXANNE_FIRST_CALL
	release
	end

DewfordTown_Gym_EventScript_GiveGymTM::
	giveitem ITEM_TM_MEGA_DRAIN
	goto_if_eq VAR_RESULT, 0, Common_EventScript_BagIsFull
	msgbox DewfordTown_Gym_Text_ExplainMegaDrain, MSGBOX_DEFAULT
	setflag FLAG_RECEIVED_TM_BULK_UP
	return

DewfordTown_Gym_EventScript_GiveGymTM2:
	giveitem ITEM_TM_MEGA_DRAIN
	goto_if_eq VAR_RESULT, 0, Common_EventScript_ShowBagIsFull
	msgbox DewfordTown_Gym_Text_ExplainMegaDrain, MSGBOX_DEFAULT
	setflag FLAG_RECEIVED_TM_BULK_UP
	release
	end

DewfordTown_Gym_EventScript_BrawlyRematch::
	trainerbattle_rematch_double TRAINER_BRAWLY_1, DewfordTown_Gym_Text_BrawlyPreRematch, DewfordTown_Gym_Text_BrawlyRematchDefeat, DewfordTown_Gym_Text_BrawlyRematchNeedTwoMons
	msgbox DewfordTown_Gym_Text_BrawlyPostRematch, MSGBOX_AUTOCLOSE
	end

DewfordTown_Gym_EventScript_Takao::
	trainerbattle_single TRAINER_TAKAO, DewfordTown_Gym_Text_TakaoIntro, DewfordTown_Gym_Text_TakaoDefeat, DewfordTown_Gym_EventScript_TakaoBrightenRoom
	msgbox DewfordTown_Gym_Text_TakaoPostBattle, MSGBOX_AUTOCLOSE
	end

DewfordTown_Gym_EventScript_TakaoBrightenRoom::
	call DewfordTown_Gym_EventScript_BrightenRoom
	release
	end

DewfordTown_Gym_EventScript_Jocelyn::
	trainerbattle_single TRAINER_JOCELYN, DewfordTown_Gym_Text_JocelynIntro, DewfordTown_Gym_Text_JocelynDefeat, DewfordTown_Gym_EventScript_JocelynBrightenRoom
	msgbox DewfordTown_Gym_Text_JocelynPostBattle, MSGBOX_AUTOCLOSE
	end

DewfordTown_Gym_EventScript_JocelynBrightenRoom::
	call DewfordTown_Gym_EventScript_BrightenRoom
	release
	end

DewfordTown_Gym_EventScript_Laura::
	trainerbattle_single TRAINER_LAURA, DewfordTown_Gym_Text_LauraIntro, DewfordTown_Gym_Text_LauraDefeat, DewfordTown_Gym_EventScript_LauraBrightenRoom
	msgbox DewfordTown_Gym_Text_LauraPostBattle, MSGBOX_AUTOCLOSE
	end

DewfordTown_Gym_EventScript_LauraBrightenRoom::
	call DewfordTown_Gym_EventScript_BrightenRoom
	release
	end

DewfordTown_Gym_EventScript_Brenden::
	trainerbattle_single TRAINER_BRENDEN, DewfordTown_Gym_Text_BrendenIntro, DewfordTown_Gym_Text_BrendenDefeat, DewfordTown_Gym_EventScript_BrendenBrightenRoom
	msgbox DewfordTown_Gym_Text_BrendenPostBattle, MSGBOX_AUTOCLOSE
	end

DewfordTown_Gym_EventScript_BrendenBrightenRoom::
	call DewfordTown_Gym_EventScript_BrightenRoom
	release
	end

DewfordTown_Gym_EventScript_Cristian::
	trainerbattle_single TRAINER_CRISTIAN, DewfordTown_Gym_Text_CristianIntro, DewfordTown_Gym_Text_CristianDefeat, DewfordTown_Gym_EventScript_CristianBrightenRoom
	msgbox DewfordTown_Gym_Text_CristianPostBattle, MSGBOX_AUTOCLOSE
	end

DewfordTown_Gym_EventScript_CristianBrightenRoom::
	call DewfordTown_Gym_EventScript_BrightenRoom
	release
	end

DewfordTown_Gym_EventScript_Lilith::
	trainerbattle_single TRAINER_LILITH, DewfordTown_Gym_Text_LilithIntro, DewfordTown_Gym_Text_LilithDefeat, DewfordTown_Gym_EventScript_LilithBrightenRoom
	msgbox DewfordTown_Gym_Text_LilithPostBattle, MSGBOX_AUTOCLOSE
	end

DewfordTown_Gym_EventScript_LilithBrightenRoom::
	call DewfordTown_Gym_EventScript_BrightenRoom
	release
	end

DewfordTown_Gym_EventScript_GymGuide::
	lock
	faceplayer
	goto_if_set FLAG_DEFEATED_DEWFORD_GYM, DewfordTown_Gym_EventScript_GymGuidePostVictory
	msgbox DewfordTown_Gym_Text_GymGuideAdvice, MSGBOX_DEFAULT
	release
	end

DewfordTown_Gym_EventScript_GymGuidePostVictory::
	msgbox DewfordTown_Gym_Text_GymGuidePostVictory, MSGBOX_DEFAULT
	release
	end

DewfordTown_Gym_EventScript_LeftGymStatue::
	lockall
	goto_if_set FLAG_BADGE02_GET, DewfordTown_Gym_EventScript_GymStatueCertified
	goto DewfordTown_Gym_EventScript_GymStatue
	end

DewfordTown_Gym_EventScript_RightGymStatue::
	lockall
	goto_if_set FLAG_BADGE02_GET, DewfordTown_Gym_EventScript_GymStatueCertified
	goto DewfordTown_Gym_EventScript_GymStatue
	end

DewfordTown_Gym_EventScript_GymStatueCertified::
	msgbox DewfordTown_Gym_Text_GymStatueCertified, MSGBOX_DEFAULT
	releaseall
	end

DewfordTown_Gym_EventScript_GymStatue::
	msgbox DewfordTown_Gym_Text_GymStatue, MSGBOX_DEFAULT
	releaseall
	end

DewfordTown_Gym_Text_GymGuideAdvice:
	.string "Yo! How's it going, CHAMPION-\n"
	.string "in-the-making?\p"
	.string "Fair warning: this GYM is dark on\n"
	.string "purpose. It's a cellar.\p"
	.string "MERLOT keeps the lights off because\n"
	.string "he says brightness bruises the fruit.\p"
	.string "Beat a TRAINER and one comes on\n"
	.string "anyway. They're all quietly relieved.\p"
	.string "One more thing. Whatever you did\n"
	.string "in RUSTBORO?\p"
	.string "Don't do it in here.\p"
	.string "Come see me afterwards, if you beat\n"
	.string "the GYM LEADER.\p"
	.string "Well, go for it!$"

DewfordTown_Gym_Text_GymGuidePostVictory:
	.string "Whoa! You really did it!\p"
	.string "And you didn't once say a wine was\n"
	.string "“nice.” That's the hard part.\p"
	.string "Check your TRAINER CARD.\p"
	.string "NOTES OF OAK should be recorded\n"
	.string "on it.$"

DewfordTown_Gym_Text_TakaoIntro:
	.string "I get cherry. Definitely cherry.\p"
	.string "Everyone gets cherry. I got there\n"
	.string "first.$"

DewfordTown_Gym_Text_TakaoDefeat:
	.string "Hm. Overripe.$"

DewfordTown_Gym_Text_TakaoPostBattle:
	.string "Cherry, and a long finish, and\n"
	.string "I am never wrong about the finish.$"

DewfordTown_Gym_Text_JocelynIntro:
	.string "Some people hear “rot” and back away.\p"
	.string "Rot is the whole point.$"

DewfordTown_Gym_Text_JocelynDefeat:
	.string "Corked. Utterly corked.$"

DewfordTown_Gym_Text_JocelynPostBattle:
	.string "Noble rot is how the sweet ones are\n"
	.string "made. Look it up. I'll wait.$"

DewfordTown_Gym_Text_LauraIntro:
	.string "The grove matters more than the\n"
	.string "bottle.\p"
	.string "Terroir. Say it properly.$"

DewfordTown_Gym_Text_LauraDefeat:
	.string "Oh, that's a poor showing.$"

DewfordTown_Gym_Text_LauraPostBattle:
	.string "You can taste the hillside. You can.\n"
	.string "You're simply not trying.$"

DewfordTown_Gym_Text_LilithIntro:
	.string "Mine's mead. I'm aware it isn't wine.\p"
	.string "I've been told. Repeatedly.$"

DewfordTown_Gym_Text_LilithDefeat:
	.string "Fine. FINE.$"

DewfordTown_Gym_Text_LilithPostBattle:
	.string "It's fermented and it's in a glass.\n"
	.string "That's most of the way there.$"

DewfordTown_Gym_Text_BrendenIntro:
	.string "I brought cider.\p"
	.string "Nobody warned me.$"

DewfordTown_Gym_Text_BrendenDefeat:
	.string "Should've stayed on the boat.$"

DewfordTown_Gym_Text_BrendenPostBattle:
	.string "MERLOT let me stay, at least.\n"
	.string "He put me nearest the door.$"

DewfordTown_Gym_Text_CristianIntro:
	.string "Notes of oak. Notes of leather.\p"
	.string "Notes of a cellar in which someone\n"
	.string "has recently wept.$"

DewfordTown_Gym_Text_CristianDefeat:
	.string "Unbalanced. Like me.$"

DewfordTown_Gym_Text_CristianPostBattle:
	.string "I only drink things older than I am.\n"
	.string "It's getting difficult.$"

DewfordTown_Gym_Text_BrawlyIntro:
	.string "MERLOT: Mind the step. And the dark.\p"
	.string "I am MERLOT, and this is a cellar\n"
	.string "that the LEAGUE insists on calling\l"
	.string "a GYM.\p"
	.string "Most challengers arrive from RUSTBORO\n"
	.string "still slightly shouting.\p"
	.string "Here we are quieter. Here we consider\n"
	.string "what a thing is like, and then we say\l"
	.string "so, at length.\p"
	.string "Let us see what you are like.$"

DewfordTown_Gym_Text_BrawlyDefeat:
	.string "Ah.\p"
	.string "Firm. Structured. Rather more tannin\n"
	.string "than I was expecting.\p"
	.string "I shall be thinking about that one\n"
	.string "for some time.$"

DewfordTown_Gym_Text_ReceivedKnuckleBadge:
	.string "{PLAYER} received NOTES OF OAK\n"
	.string "from MERLOT.$"

DewfordTown_Gym_Text_KnuckleBadgeInfoTakeThis:
	.string "NOTES OF OAK makes all POKéMON\n"
	.string "up to Lv. 30, even those you get in\l"
	.string "trades, obey you.\p"
	.string "It also lets you use the HM move FLASH\n"
	.string "outside of battle.\p"
	.string "You will want FLASH. The cave next\n"
	.string "door is darker than this one, and\l"
	.string "nothing in it has been decanted.\p"
	.string "And take this as well.$"

DewfordTown_Gym_Text_ExplainMegaDrain:
	.string "That TECHNICAL MACHINE is TM52,\n"
	.string "MEGA DRAIN.\p"
	.string "It draws the substance out of\n"
	.string "the other thing and keeps it.\p"
	.string "Pressing, essentially.\p"
	.string "A TM can be used only once, so do\n"
	.string "think before you use it.$"

DewfordTown_Gym_Text_RegisteredBrawly:
	.string "Registered GYM LEADER MERLOT\n"
	.string "in the POKéNAV.$"

DewfordTown_Gym_Text_BrawlyPostBattle:
	.string "MERLOT: Go on to the other GYMS.\p"
	.string "You will meet a young man in MAUVILLE\n"
	.string "who does not sit down.\p"
	.string "Give him my regards. He will not\n"
	.string "remember me.$"

DewfordTown_Gym_Text_GymStatue:
	.string "DEWFORD TOWN POKéMON GYM$"

DewfordTown_Gym_Text_GymStatueCertified:
	.string "DEWFORD TOWN POKéMON GYM\p"
	.string "MERLOT'S CERTIFIED TRAINERS:\n"
	.string "{PLAYER}$"

DewfordTown_Gym_Text_BrawlyPreRematch:
	.string "MERLOT: You again. Good.\p"
	.string "The cellar has moved on since you\n"
	.string "were last down here.\p"
	.string "So, I suspect, have you.$"

DewfordTown_Gym_Text_BrawlyRematchDefeat:
	.string "Still firm. Still structured.\p"
	.string "Still, apparently, better than mine.$"

DewfordTown_Gym_Text_BrawlyPostRematch:
	.string "MERLOT: One learns more from being\n"
	.string "beaten than from being poured.\p"
	.string "I have no idea what I meant by that.$"

DewfordTown_Gym_Text_BrawlyRematchNeedTwoMons:
	.string "MERLOT: You again. Good.\p"
	.string "The cellar has moved on since you\n"
	.string "were last down here.\p"
	.string "So, I suspect…\p"
	.string "Ah. You have brought one POKéMON.\p"
	.string "One does not taste a single wine.\n"
	.string "Fetch another.$"
