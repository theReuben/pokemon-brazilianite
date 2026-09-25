EverGrandeCity_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, EverGrandeCity_OnTransition
	.byte 0

EverGrandeCity_OnTransition:
	call_if_set FLAG_SYS_WEATHER_CTRL, Common_EventScript_SetAbnormalWeather
	end

EverGrandeCity_EventScript_VictoryRoadSign::
	msgbox EverGrandeCity_Text_EnteringVictoryRoad, MSGBOX_SIGN
	end

EverGrandeCity_EventScript_CitySign::
	msgbox EverGrandeCity_Text_CitySign, MSGBOX_SIGN
	end

EverGrandeCity_EventScript_PokemonLeagueSign::
	msgbox EverGrandeCity_Text_EnteringPokemonLeague, MSGBOX_SIGN
	end

@ Fires in the neck below the VICTORY ROAD entrance, before the climb starts.
@ (18, 43) rather than (18, 42) because 42 is where the cave warp lands you, and
@ a coord event only fires when you step onto its tile.
EverGrandeCity_EventScript_MamaBosaLeagueCall::
	setvar VAR_TEMP_2, 1
	goto_if_set FLAG_MAMA_BOSA_LEAGUE_CALL, EverGrandeCity_EventScript_MamaBosaLeagueCallEnd
	goto_if_unset FLAG_BADGE08_GET, EverGrandeCity_EventScript_MamaBosaLeagueCallEnd
	lockall
	setflag FLAG_MAMA_BOSA_LEAGUE_CALL
	pokenavcall EverGrandeCity_Text_MamaBosaLeagueCall
	waitmessage
	waitbuttonpress
	closemessage
	releaseall
EverGrandeCity_EventScript_MamaBosaLeagueCallEnd::
	end

EverGrandeCity_EventScript_SetVisitedEverGrande::
	setflag FLAG_VISITED_EVER_GRANDE_CITY
	setvar VAR_TEMP_1, 1
	end

EverGrandeCity_Text_EnteringVictoryRoad:
	.string "ENTERING VICTORY ROAD$"

EverGrandeCity_Text_EnteringPokemonLeague:
	.string "ENTERING POKéMON LEAGUE\n"
	.string "CENTER GATE$"

EverGrandeCity_Text_CitySign:
	.string "EVER GRANDE CITY\p"
	.string "“The paradise of flowers, the sea,\n"
	.string "and POKéMON.”$"

EverGrandeCity_Text_MamaBosaLeagueCall:
	.string "… … … … … …\n"
	.string "… … … … … Beep!\p"
	.string "MAMA BOSA: {PLAYER}!\p"
	.string "I just heard you beat all eight GYMS!\n"
	.string "I'm almost proud of you.\p"
	.string "Make sure you stock up on all the\n"
	.string "items you can buy in LILYCOVE now,\l"
	.string "and go and see if that weird man\l"
	.string "outside those caves will let you in.\p"
	.string "Make sure you're prepared for the\n"
	.string "ELITE FOUR. I wouldn't want to have to\l"
	.string "hit you with my car again.\p"
	.string "… … … … … …\n"
	.string "… … … … … Click!$"
