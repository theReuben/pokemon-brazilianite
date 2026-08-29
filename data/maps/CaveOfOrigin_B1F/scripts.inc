CaveOfOrigin_B1F_MapScripts::
	.byte 0

CaveOfOrigin_B1F_EventScript_Wallace::
	lock
	faceplayer
	msgbox CaveOfOrigin_B1F_Text_WallaceStory, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_CAVE_OF_ORIGIN_WALLACE, Common_Movement_WalkInPlaceFasterUp
	waitmovement 0
	delay 60
	playse SE_PIN
	applymovement LOCALID_CAVE_OF_ORIGIN_WALLACE, Common_Movement_ExclamationMark
	waitmovement 0
	applymovement LOCALID_CAVE_OF_ORIGIN_WALLACE, Common_Movement_Delay48
	waitmovement 0
	delay 30
	applymovement LOCALID_CAVE_OF_ORIGIN_WALLACE, Common_Movement_FacePlayer
	waitmovement 0
	message CaveOfOrigin_B1F_Text_WhereIsRayquaza
	waitmessage
	goto CaveOfOrigin_B1F_EventScript_WheresRayquaza

CaveOfOrigin_B1F_EventScript_WheresRayquaza::
	multichoice 0, 0, MULTI_WHERES_RAYQUAZA, FALSE
	switch VAR_RESULT
	case 0, CaveOfOrigin_B1F_EventScript_AtCaveOfOrigin
	case 1, CaveOfOrigin_B1F_EventScript_AtMtPyre
	case 2, CaveOfOrigin_B1F_EventScript_AtSkyPillar
	case 3, CaveOfOrigin_B1F_EventScript_DontRemember
	goto CaveOfOrigin_B1F_EventScript_DontRemember
	end

CaveOfOrigin_B1F_EventScript_AtCaveOfOrigin::
	message CaveOfOrigin_B1F_Text_ButWereInCaveOfOrigin
	waitmessage
	goto CaveOfOrigin_B1F_EventScript_WheresRayquaza

CaveOfOrigin_B1F_EventScript_AtMtPyre::
	message CaveOfOrigin_B1F_Text_OldLadyDidntMentionThat
	waitmessage
	goto CaveOfOrigin_B1F_EventScript_WheresRayquaza

CaveOfOrigin_B1F_EventScript_DontRemember::
	message CaveOfOrigin_B1F_Text_CantYouRememberSomehow
	waitmessage
	goto CaveOfOrigin_B1F_EventScript_WheresRayquaza

CaveOfOrigin_B1F_EventScript_AtSkyPillar::
	msgbox CaveOfOrigin_B1F_Text_WellHeadToSkyPillar, MSGBOX_DEFAULT
	closemessage
	playse SE_EXIT
	fadescreenspeed FADE_TO_BLACK, 4
	setflag FLAG_WALLACE_GOES_TO_SKY_PILLAR
	setvar VAR_SOOTOPOLIS_CITY_STATE, 3
	removeobject LOCALID_CAVE_OF_ORIGIN_WALLACE
	removeobject LOCALID_CAVE_OF_ORIGIN_JAKES_PSYDUCK
	clearflag FLAG_HIDE_SKY_PILLAR_WALLACE
	fadescreen FADE_FROM_BLACK
	release
	end

CaveOfOrigin_B1F_Text_WallaceStory:
	.string "JAKE: {PLAYER}{KUN}!\p"
	.string "Of course it's you. Of course it is.\p"
	.string "I got the call about SOOTOPOLIS and\n"
	.string "came straight from EVER GRANDE.\p"
	.string "Being the resident treat boy means\n"
	.string "you get the bad news first.\p"
	.string "… … … … … …\n"
	.string "… … … … … …\p"
	.string "GROUDON and KYOGRE, the two brown POKéMON\n"
	.string "wreaking havoc here, are considered\l"
	.string "to be super-ancient POKéMON.\p"
	.string "Dad's been on about them for years.\p"
	.string "And there aren't just two of them.\n"
	.string "There's one more, somewhere.\p"
	.string "A super-ancient POKéMON named\n"
	.string "RAYQUAZA.\p"
	.string "It's said that it was RAYQUAZA that\n"
	.string "becalmed the two combatants in\l"
	.string "the distant past.\p"
	.string "But I've no idea where it is. I've\n"
	.string "read everything Dad has.\l"
	.string "Even those Sarah J Maas books\l"
	.string "with the sexy elf.\l"
	.string "Nothing.$"

CaveOfOrigin_B1F_Text_WhereIsRayquaza:
	.string "JAKE: {PLAYER}{KUN}, do you know where\n"
	.string "RAYQUAZA is?\p"
	.string "You've been everywhere. Think.\n"
	.string "Ireland, Italy, Mexico...\l"
	.string "It could be in any one of those\l"
	.string "places with the same flag.$"

CaveOfOrigin_B1F_Text_ButWereInCaveOfOrigin:
	.string "JAKE: The CAVE OF ORIGIN?\p"
	.string "We're standing in it!\n"
	.string "Come on, you can do better!\p"
	.string "Think about where RAYQUAZA might\n"
	.string "actually be.$"

CaveOfOrigin_B1F_Text_OldLadyDidntMentionThat:
	.string "JAKE: MT. PYRE?\p"
	.string "I went up there myself and the old\n"
	.string "lady never said a word about it.\p"
	.string "I don't think she'd hide something\n"
	.string "like that from me after\l"
	.string "the time we shared in Guam.\p"
	.string "{PLAYER}{KUN}, have another think.$"

CaveOfOrigin_B1F_Text_CantYouRememberSomehow:
	.string "JAKE: Huh? You don't remember?\n"
	.string "Hmm… That's a problem…\p"
	.string "Can't you remember somehow?$"

CaveOfOrigin_B1F_Text_WellHeadToSkyPillar:
	.string "JAKE: The SKY PILLAR?\p"
	.string "That's it!\n"
	.string "It has to be the SKY PILLAR!\p"
	.string "{PLAYER}{KUN}, there's not a moment to lose!\n"
	.string "We're going. Right now!$"

