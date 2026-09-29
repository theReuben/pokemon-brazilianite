EverGrandeCity_PhoebesRoom_MapScripts::
	map_script MAP_SCRIPT_ON_LOAD, EverGrandeCity_PhoebesRoom_OnLoad
	map_script MAP_SCRIPT_ON_WARP_INTO_MAP_TABLE, EverGrandeCity_PhoebesRoom_OnWarp
	map_script MAP_SCRIPT_ON_FRAME_TABLE, EverGrandeCity_PhoebesRoom_OnFrame
	.byte 0

EverGrandeCity_PhoebesRoom_OnWarp:
	map_script_2 VAR_TEMP_1, 0, EverGrandeCity_PhoebesRoom_EventScript_PlayerTurnNorth
	.2byte 0

EverGrandeCity_PhoebesRoom_EventScript_PlayerTurnNorth::
	turnobject LOCALID_PLAYER, DIR_NORTH
	end

EverGrandeCity_PhoebesRoom_OnFrame:
	map_script_2 VAR_ELITE_4_STATE, 1, EverGrandeCity_PhoebesRoom_EventScript_WalkInCloseDoor
	.2byte 0

EverGrandeCity_PhoebesRoom_EventScript_WalkInCloseDoor::
	lockall
	call PokemonLeague_EliteFour_EventScript_WalkInCloseDoor
	setvar VAR_ELITE_4_STATE, 2
	releaseall
	end

EverGrandeCity_PhoebesRoom_OnLoad:
	call_if_set FLAG_DEFEATED_ELITE_4_PHOEBE, EverGrandeCity_PhoebesRoom_EventScript_ResetAdvanceToNextRoom
	call_if_eq VAR_ELITE_4_STATE, 2, EverGrandeCity_PhoebesRoom_EventScript_CloseDoor
	end

EverGrandeCity_PhoebesRoom_EventScript_ResetAdvanceToNextRoom::
	call PokemonLeague_EliteFour_EventScript_ResetAdvanceToNextRoom
	return

EverGrandeCity_PhoebesRoom_EventScript_CloseDoor::
	call PokemonLeague_EliteFour_EventScript_CloseDoor
	return

EverGrandeCity_PhoebesRoom_EventScript_Phoebe::
	lock
	faceplayer
	goto_if_set FLAG_DEFEATED_ELITE_4_PHOEBE, EverGrandeCity_PhoebesRoom_EventScript_PostBattleSpeech
	playbgm MUS_ENCOUNTER_ELITE_FOUR, FALSE
	msgbox EverGrandeCity_PhoebesRoom_Text_IntroSpeech, MSGBOX_DEFAULT
	trainerbattle_no_intro TRAINER_PHOEBE, EverGrandeCity_PhoebesRoom_Text_Defeat
	goto EverGrandeCity_PhoebesRoom_EventScript_Defeated
	end

EverGrandeCity_PhoebesRoom_EventScript_PostBattleSpeech::
	goto_if_unset FLAG_RECEIVED_PEPPY_MAC, EverGrandeCity_PhoebesRoom_EventScript_GivePeppyMac
	msgbox EverGrandeCity_PhoebesRoom_Text_DrinkIt, MSGBOX_DEFAULT
	release
	end

EverGrandeCity_PhoebesRoom_EventScript_Defeated::
	setflag FLAG_DEFEATED_ELITE_4_PHOEBE
	call PokemonLeague_EliteFour_SetAdvanceToNextRoomMetatiles
	goto EverGrandeCity_PhoebesRoom_EventScript_GivePeppyMac
	end

EverGrandeCity_PhoebesRoom_EventScript_GivePeppyMac::
	msgbox EverGrandeCity_PhoebesRoom_Text_PostBattleSpeech, MSGBOX_DEFAULT
	giveitem ITEM_PEPPY_MAC
	goto_if_eq VAR_RESULT, FALSE, EverGrandeCity_PhoebesRoom_EventScript_BagFull
	setflag FLAG_RECEIVED_PEPPY_MAC
	msgbox EverGrandeCity_PhoebesRoom_Text_DrinkIt, MSGBOX_DEFAULT
	release
	end

EverGrandeCity_PhoebesRoom_EventScript_BagFull::
	msgbox EverGrandeCity_PhoebesRoom_Text_BagFull, MSGBOX_DEFAULT
	release
	end

EverGrandeCity_PhoebesRoom_Text_IntroSpeech:
	.string "I'm PRAESTA of the ELITE FOUR.\p"
	.string "You got past the old man, then.\p"
	.string "So you'll have heard about the peppy\n"
	.string "mac.\p"
	.string "Eleven cans a day, that man. Says it\n"
	.string "sharpens him up.\p"
	.string "Beat me and I'll stand you one.$"

EverGrandeCity_PhoebesRoom_Text_Defeat:
	.string "Hah!\n"
	.string "Consider my peppy mac quapt.$"

EverGrandeCity_PhoebesRoom_Text_PostBattleSpeech:
	.string "A can, as promised.$"

EverGrandeCity_PhoebesRoom_Text_DrinkIt:
	.string "No sugar in it. All the taste, they\n"
	.string "reckon. Maximum taste.\p"
	.string "Drink it before the next room.\n"
	.string "You'll want to be awake for that one.$"

EverGrandeCity_PhoebesRoom_Text_BagFull:
	.string "Your BAG's full.\p"
	.string "I'll keep it cold. Come back when\n"
	.string "you've room for it.$"

