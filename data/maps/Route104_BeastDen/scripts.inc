Route104_BeastDen_MapScripts::
	map_script MAP_SCRIPT_ON_RESUME, Route104_BeastDen_OnResume
	.byte 0

Route104_BeastDen_OnResume:
	call_if_set FLAG_SYS_CTRL_OBJ_DELETE, Route104_BeastDen_EventScript_TryRemoveLegendary
	end

Route104_BeastDen_EventScript_TryRemoveLegendary::
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_ne VAR_RESULT, B_OUTCOME_CAUGHT, Common_EventScript_NopReturn
	removeobject VAR_LAST_TALKED
	return

Route104_BeastDen_EventScript_Raikou::
	lockall
	@ Committing to this legendary drives the other(s) from the den for good.
	goto_if_ne VAR_BEAST_DEN_CHOICE, 0, Route104_BeastDen_EventScript_Raikou_Battle
	msgbox Route104_BeastDen_Text_ChooseWarning, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Route104_BeastDen_EventScript_Decline
	setvar VAR_BEAST_DEN_CHOICE, 1
	setflag FLAG_HIDE_BEAST_DEN_ENTEI
	setflag FLAG_HIDE_BEAST_DEN_SUICUNE
	@ Hide flags only apply on respawn, so clear them from the map now too.
	removeobject LOCALID_BEAST_DEN_ENTEI
	removeobject LOCALID_BEAST_DEN_SUICUNE
Route104_BeastDen_EventScript_Raikou_Battle::
	waitse
	playmoncry SPECIES_RAIKOU, CRY_MODE_ENCOUNTER
	delay 40
	waitmoncry
	setwildbattle SPECIES_RAIKOU, 50
	setflag FLAG_SYS_CTRL_OBJ_DELETE
	special BattleSetup_StartLegendaryBattle
	waitstate
	clearflag FLAG_SYS_CTRL_OBJ_DELETE
	@ Deliberately no FLAG_DEFEATED_* here: a failed catch or a KO lets it respawn.
	releaseall
	end

Route104_BeastDen_EventScript_Entei::
	lockall
	@ Committing to this legendary drives the other(s) from the den for good.
	goto_if_ne VAR_BEAST_DEN_CHOICE, 0, Route104_BeastDen_EventScript_Entei_Battle
	msgbox Route104_BeastDen_Text_ChooseWarning, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Route104_BeastDen_EventScript_Decline
	setvar VAR_BEAST_DEN_CHOICE, 2
	setflag FLAG_HIDE_BEAST_DEN_RAIKOU
	setflag FLAG_HIDE_BEAST_DEN_SUICUNE
	@ Hide flags only apply on respawn, so clear them from the map now too.
	removeobject LOCALID_BEAST_DEN_RAIKOU
	removeobject LOCALID_BEAST_DEN_SUICUNE
Route104_BeastDen_EventScript_Entei_Battle::
	waitse
	playmoncry SPECIES_ENTEI, CRY_MODE_ENCOUNTER
	delay 40
	waitmoncry
	setwildbattle SPECIES_ENTEI, 50
	setflag FLAG_SYS_CTRL_OBJ_DELETE
	special BattleSetup_StartLegendaryBattle
	waitstate
	clearflag FLAG_SYS_CTRL_OBJ_DELETE
	@ Deliberately no FLAG_DEFEATED_* here: a failed catch or a KO lets it respawn.
	releaseall
	end

Route104_BeastDen_EventScript_Suicune::
	lockall
	@ Committing to this legendary drives the other(s) from the den for good.
	goto_if_ne VAR_BEAST_DEN_CHOICE, 0, Route104_BeastDen_EventScript_Suicune_Battle
	msgbox Route104_BeastDen_Text_ChooseWarning, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Route104_BeastDen_EventScript_Decline
	setvar VAR_BEAST_DEN_CHOICE, 3
	setflag FLAG_HIDE_BEAST_DEN_RAIKOU
	setflag FLAG_HIDE_BEAST_DEN_ENTEI
	@ Hide flags only apply on respawn, so clear them from the map now too.
	removeobject LOCALID_BEAST_DEN_RAIKOU
	removeobject LOCALID_BEAST_DEN_ENTEI
Route104_BeastDen_EventScript_Suicune_Battle::
	waitse
	playmoncry SPECIES_SUICUNE, CRY_MODE_ENCOUNTER
	delay 40
	waitmoncry
	setwildbattle SPECIES_SUICUNE, 50
	setflag FLAG_SYS_CTRL_OBJ_DELETE
	special BattleSetup_StartLegendaryBattle
	waitstate
	clearflag FLAG_SYS_CTRL_OBJ_DELETE
	@ Deliberately no FLAG_DEFEATED_* here: a failed catch or a KO lets it respawn.
	releaseall
	end

Route104_BeastDen_EventScript_Decline::
	releaseall
	end

Route104_BeastDen_Text_ChooseWarning:
	.string "The air here is thick with power.\n"
	.string "The others watch you closely…\p"
	.string "If you raise a hand against this one,\n"
	.string "the rest will surely flee for good.\p"
	.string "Challenge it?$"
