Route111_StormRoost_MapScripts::
	map_script MAP_SCRIPT_ON_RESUME, Route111_StormRoost_OnResume
	.byte 0

Route111_StormRoost_OnResume:
	call_if_set FLAG_SYS_CTRL_OBJ_DELETE, Route111_StormRoost_EventScript_TryRemoveLegendary
	end

Route111_StormRoost_EventScript_TryRemoveLegendary::
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_ne VAR_RESULT, B_OUTCOME_CAUGHT, Common_EventScript_NopReturn
	removeobject VAR_LAST_TALKED
	return

Route111_StormRoost_EventScript_ArticunoGalar::
	lockall
	@ Committing to this legendary drives the other(s) from the den for good.
	goto_if_ne VAR_STORM_ROOST_CHOICE, 0, Route111_StormRoost_EventScript_ArticunoGalar_Battle
	msgbox Route111_StormRoost_Text_ChooseWarning, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Route111_StormRoost_EventScript_Decline
	setvar VAR_STORM_ROOST_CHOICE, 1
	setflag FLAG_HIDE_STORM_ROOST_ZAPDOS
	setflag FLAG_HIDE_STORM_ROOST_MOLTRES
Route111_StormRoost_EventScript_ArticunoGalar_Battle::
	waitse
	playmoncry SPECIES_ARTICUNO_GALAR, CRY_MODE_ENCOUNTER
	delay 40
	waitmoncry
	setwildbattle SPECIES_ARTICUNO_GALAR, 50
	setflag FLAG_SYS_CTRL_OBJ_DELETE
	special BattleSetup_StartLegendaryBattle
	waitstate
	clearflag FLAG_SYS_CTRL_OBJ_DELETE
	@ Deliberately no FLAG_DEFEATED_* here: a failed catch or a KO lets it respawn.
	@ The others slip away only once the battle is over, so they are not
	@ seen vanishing before it starts.
	removeobject LOCALID_STORM_ROOST_ZAPDOS
	removeobject LOCALID_STORM_ROOST_MOLTRES
	releaseall
	end

Route111_StormRoost_EventScript_ZapdosGalar::
	lockall
	@ Committing to this legendary drives the other(s) from the den for good.
	goto_if_ne VAR_STORM_ROOST_CHOICE, 0, Route111_StormRoost_EventScript_ZapdosGalar_Battle
	msgbox Route111_StormRoost_Text_ChooseWarning, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Route111_StormRoost_EventScript_Decline
	setvar VAR_STORM_ROOST_CHOICE, 2
	setflag FLAG_HIDE_STORM_ROOST_ARTICUNO
	setflag FLAG_HIDE_STORM_ROOST_MOLTRES
Route111_StormRoost_EventScript_ZapdosGalar_Battle::
	waitse
	playmoncry SPECIES_ZAPDOS_GALAR, CRY_MODE_ENCOUNTER
	delay 40
	waitmoncry
	setwildbattle SPECIES_ZAPDOS_GALAR, 50
	setflag FLAG_SYS_CTRL_OBJ_DELETE
	special BattleSetup_StartLegendaryBattle
	waitstate
	clearflag FLAG_SYS_CTRL_OBJ_DELETE
	@ Deliberately no FLAG_DEFEATED_* here: a failed catch or a KO lets it respawn.
	@ The others slip away only once the battle is over, so they are not
	@ seen vanishing before it starts.
	removeobject LOCALID_STORM_ROOST_ARTICUNO
	removeobject LOCALID_STORM_ROOST_MOLTRES
	releaseall
	end

Route111_StormRoost_EventScript_MoltresGalar::
	lockall
	@ Committing to this legendary drives the other(s) from the den for good.
	goto_if_ne VAR_STORM_ROOST_CHOICE, 0, Route111_StormRoost_EventScript_MoltresGalar_Battle
	msgbox Route111_StormRoost_Text_ChooseWarning, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Route111_StormRoost_EventScript_Decline
	setvar VAR_STORM_ROOST_CHOICE, 3
	setflag FLAG_HIDE_STORM_ROOST_ARTICUNO
	setflag FLAG_HIDE_STORM_ROOST_ZAPDOS
Route111_StormRoost_EventScript_MoltresGalar_Battle::
	waitse
	playmoncry SPECIES_MOLTRES_GALAR, CRY_MODE_ENCOUNTER
	delay 40
	waitmoncry
	setwildbattle SPECIES_MOLTRES_GALAR, 50
	setflag FLAG_SYS_CTRL_OBJ_DELETE
	special BattleSetup_StartLegendaryBattle
	waitstate
	clearflag FLAG_SYS_CTRL_OBJ_DELETE
	@ Deliberately no FLAG_DEFEATED_* here: a failed catch or a KO lets it respawn.
	@ The others slip away only once the battle is over, so they are not
	@ seen vanishing before it starts.
	removeobject LOCALID_STORM_ROOST_ARTICUNO
	removeobject LOCALID_STORM_ROOST_ZAPDOS
	releaseall
	end

Route111_StormRoost_EventScript_Decline::
	releaseall
	end

Route111_StormRoost_Text_ChooseWarning:
	.string "The air here is thick with power.\n"
	.string "The others watch you closely…\p"
	.string "If you raise a hand against this one,\n"
	.string "the rest will surely flee for good.\p"
	.string "Challenge it?$"
