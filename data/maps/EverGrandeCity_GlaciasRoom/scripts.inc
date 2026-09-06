EverGrandeCity_GlaciasRoom_MapScripts::
	map_script MAP_SCRIPT_ON_FRAME_TABLE, EverGrandeCity_GlaciasRoom_OnFrame
	map_script MAP_SCRIPT_ON_LOAD, EverGrandeCity_GlaciasRoom_OnLoad
	map_script MAP_SCRIPT_ON_WARP_INTO_MAP_TABLE, EverGrandeCity_GlaciasRoom_OnWarp
	.byte 0

EverGrandeCity_GlaciasRoom_OnWarp:
	map_script_2 VAR_TEMP_1, 0, EverGrandeCity_GlaciasRoom_EventScript_PlayerTurnNorth
	.2byte 0

EverGrandeCity_GlaciasRoom_EventScript_PlayerTurnNorth::
	turnobject LOCALID_PLAYER, DIR_NORTH
	end

EverGrandeCity_GlaciasRoom_OnFrame:
	map_script_2 VAR_ELITE_4_STATE, 2, EverGrandeCity_GlaciasRoom_EventScript_WalkInCloseDoor
	.2byte 0

EverGrandeCity_GlaciasRoom_EventScript_WalkInCloseDoor::
	lockall
	call PokemonLeague_EliteFour_EventScript_WalkInCloseDoor
	setvar VAR_ELITE_4_STATE, 3
	releaseall
	end

EverGrandeCity_GlaciasRoom_OnLoad:
	call_if_set FLAG_DEFEATED_ELITE_4_GLACIA, EverGrandeCity_GlaciasRoom_EventScript_ResetAdvanceToNextRoom
	call_if_eq VAR_ELITE_4_STATE, 3, EverGrandeCity_GlaciasRoom_EventScript_CloseDoor
	end

EverGrandeCity_GlaciasRoom_EventScript_ResetAdvanceToNextRoom::
	call PokemonLeague_EliteFour_EventScript_ResetAdvanceToNextRoom
	return

EverGrandeCity_GlaciasRoom_EventScript_CloseDoor::
	call PokemonLeague_EliteFour_EventScript_CloseDoor
	return

EverGrandeCity_GlaciasRoom_EventScript_Glacia::
	lock
	faceplayer
	goto_if_set FLAG_DEFEATED_ELITE_4_GLACIA, EverGrandeCity_GlaciasRoom_EventScript_PostBattleSpeech
	playbgm MUS_ENCOUNTER_ELITE_FOUR, FALSE
	msgbox EverGrandeCity_GlaciasRoom_Text_IntroSpeech, MSGBOX_DEFAULT
	trainerbattle_no_intro TRAINER_GLACIA, EverGrandeCity_GlaciasRoom_Text_Defeat
	goto EverGrandeCity_GlaciasRoom_EventScript_Defeated
	end

EverGrandeCity_GlaciasRoom_EventScript_PostBattleSpeech::
	msgbox EverGrandeCity_GlaciasRoom_Text_PostBattleSpeech, MSGBOX_DEFAULT
	release
	end

EverGrandeCity_GlaciasRoom_EventScript_Defeated::
	setflag FLAG_DEFEATED_ELITE_4_GLACIA
	call PokemonLeague_EliteFour_SetAdvanceToNextRoomMetatiles
	msgbox EverGrandeCity_GlaciasRoom_Text_PostBattleSpeech, MSGBOX_DEFAULT
	release
	end

EverGrandeCity_GlaciasRoom_Text_IntroSpeech:
	.string "Welcome. My name is HUSH,\n"
	.string "of the ELITE FOUR.\p"
	.string "It's me. ijiji.\p"
	.string "I gave myself the third room.\n"
	.string "I thought that was modest of me.\p"
	.string "So how are you finding it?\p"
	.string "The region, I mean. The typings I\n"
	.string "moved. The numbers I raised.\p"
	.string "The caves I hid behind eight BADGES.\p"
	.string "I built every bit of it, and I still\n"
	.string "cannot tell you whether it came out\l"
	.string "too hard or not hard enough.\p"
	.string "You're the only one who can settle\n"
	.string "that, and there's only one way you\l"
	.string "get to say it.\p"
	.string "I kept the unkind POKéMON for myself,\n"
	.string "by the way. That felt honest.\p"
	.string "Whenever you're ready.$"

EverGrandeCity_GlaciasRoom_Text_Defeat:
	.string "Ah.\p"
	.string "Not hard enough, I guess.\p"
	.string "Don't look sorry about it. This is\n"
	.string "the only way I ever find out.\p"
	.string "I'm writing it down.$"

EverGrandeCity_GlaciasRoom_Text_PostBattleSpeech:
	.string "Go on through when you're ready.\p"
	.string "He's the last door, and he's head of\n"
	.string "the four of us.\p"
	.string "Head MOD, as well. If you've ever\n"
	.string "been quietly told to behave, that\l"
	.string "was him.\p"
	.string "I built the place.\n"
	.string "He's the one who keeps it civil.$"

