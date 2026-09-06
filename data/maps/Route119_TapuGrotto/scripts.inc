Route119_TapuGrotto_MapScripts::
	map_script MAP_SCRIPT_ON_RESUME, Route119_TapuGrotto_OnResume
	.byte 0

Route119_TapuGrotto_OnResume:
	call_if_set FLAG_SYS_CTRL_OBJ_DELETE, Route119_TapuGrotto_EventScript_TryRemoveLegendary
	end

Route119_TapuGrotto_EventScript_TryRemoveLegendary::
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_ne VAR_RESULT, B_OUTCOME_CAUGHT, Common_EventScript_NopReturn
	removeobject VAR_LAST_TALKED
	return

Route119_TapuGrotto_EventScript_TapuKoko::
	lockall
	@ Committing to this legendary drives the other(s) from the den for good.
	goto_if_ne VAR_TAPU_GROTTO_CHOICE, 0, Route119_TapuGrotto_EventScript_TapuKoko_Battle
	msgbox Route119_TapuGrotto_Text_ChooseWarning, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Route119_TapuGrotto_EventScript_Decline
	setvar VAR_TAPU_GROTTO_CHOICE, 1
	setflag FLAG_HIDE_TAPU_GROTTO_LELE
	setflag FLAG_HIDE_TAPU_GROTTO_BULU
	setflag FLAG_HIDE_TAPU_GROTTO_FINI
	@ Hide flags only apply on respawn, so clear them from the map now too.
	removeobject LOCALID_TAPU_GROTTO_LELE
	removeobject LOCALID_TAPU_GROTTO_BULU
	removeobject LOCALID_TAPU_GROTTO_FINI
Route119_TapuGrotto_EventScript_TapuKoko_Battle::
	waitse
	playmoncry SPECIES_TAPU_KOKO, CRY_MODE_ENCOUNTER
	delay 40
	waitmoncry
	setwildbattle SPECIES_TAPU_KOKO, 50
	setflag FLAG_SYS_CTRL_OBJ_DELETE
	special BattleSetup_StartLegendaryBattle
	waitstate
	clearflag FLAG_SYS_CTRL_OBJ_DELETE
	@ Deliberately no FLAG_DEFEATED_* here: a failed catch or a KO lets it respawn.
	releaseall
	end

Route119_TapuGrotto_EventScript_TapuLele::
	lockall
	@ Committing to this legendary drives the other(s) from the den for good.
	goto_if_ne VAR_TAPU_GROTTO_CHOICE, 0, Route119_TapuGrotto_EventScript_TapuLele_Battle
	msgbox Route119_TapuGrotto_Text_ChooseWarning, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Route119_TapuGrotto_EventScript_Decline
	setvar VAR_TAPU_GROTTO_CHOICE, 2
	setflag FLAG_HIDE_TAPU_GROTTO_KOKO
	setflag FLAG_HIDE_TAPU_GROTTO_BULU
	setflag FLAG_HIDE_TAPU_GROTTO_FINI
	@ Hide flags only apply on respawn, so clear them from the map now too.
	removeobject LOCALID_TAPU_GROTTO_KOKO
	removeobject LOCALID_TAPU_GROTTO_BULU
	removeobject LOCALID_TAPU_GROTTO_FINI
Route119_TapuGrotto_EventScript_TapuLele_Battle::
	waitse
	playmoncry SPECIES_TAPU_LELE, CRY_MODE_ENCOUNTER
	delay 40
	waitmoncry
	setwildbattle SPECIES_TAPU_LELE, 50
	setflag FLAG_SYS_CTRL_OBJ_DELETE
	special BattleSetup_StartLegendaryBattle
	waitstate
	clearflag FLAG_SYS_CTRL_OBJ_DELETE
	@ Deliberately no FLAG_DEFEATED_* here: a failed catch or a KO lets it respawn.
	releaseall
	end

Route119_TapuGrotto_EventScript_TapuBulu::
	lockall
	@ Committing to this legendary drives the other(s) from the den for good.
	goto_if_ne VAR_TAPU_GROTTO_CHOICE, 0, Route119_TapuGrotto_EventScript_TapuBulu_Battle
	msgbox Route119_TapuGrotto_Text_ChooseWarning, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Route119_TapuGrotto_EventScript_Decline
	setvar VAR_TAPU_GROTTO_CHOICE, 3
	setflag FLAG_HIDE_TAPU_GROTTO_KOKO
	setflag FLAG_HIDE_TAPU_GROTTO_LELE
	setflag FLAG_HIDE_TAPU_GROTTO_FINI
	@ Hide flags only apply on respawn, so clear them from the map now too.
	removeobject LOCALID_TAPU_GROTTO_KOKO
	removeobject LOCALID_TAPU_GROTTO_LELE
	removeobject LOCALID_TAPU_GROTTO_FINI
Route119_TapuGrotto_EventScript_TapuBulu_Battle::
	waitse
	playmoncry SPECIES_TAPU_BULU, CRY_MODE_ENCOUNTER
	delay 40
	waitmoncry
	setwildbattle SPECIES_TAPU_BULU, 50
	setflag FLAG_SYS_CTRL_OBJ_DELETE
	special BattleSetup_StartLegendaryBattle
	waitstate
	clearflag FLAG_SYS_CTRL_OBJ_DELETE
	@ Deliberately no FLAG_DEFEATED_* here: a failed catch or a KO lets it respawn.
	releaseall
	end

Route119_TapuGrotto_EventScript_TapuFini::
	lockall
	@ Committing to this legendary drives the other(s) from the den for good.
	goto_if_ne VAR_TAPU_GROTTO_CHOICE, 0, Route119_TapuGrotto_EventScript_TapuFini_Battle
	msgbox Route119_TapuGrotto_Text_ChooseWarning, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Route119_TapuGrotto_EventScript_Decline
	setvar VAR_TAPU_GROTTO_CHOICE, 4
	setflag FLAG_HIDE_TAPU_GROTTO_KOKO
	setflag FLAG_HIDE_TAPU_GROTTO_LELE
	setflag FLAG_HIDE_TAPU_GROTTO_BULU
	@ Hide flags only apply on respawn, so clear them from the map now too.
	removeobject LOCALID_TAPU_GROTTO_KOKO
	removeobject LOCALID_TAPU_GROTTO_LELE
	removeobject LOCALID_TAPU_GROTTO_BULU
Route119_TapuGrotto_EventScript_TapuFini_Battle::
	waitse
	playmoncry SPECIES_TAPU_FINI, CRY_MODE_ENCOUNTER
	delay 40
	waitmoncry
	setwildbattle SPECIES_TAPU_FINI, 50
	setflag FLAG_SYS_CTRL_OBJ_DELETE
	special BattleSetup_StartLegendaryBattle
	waitstate
	clearflag FLAG_SYS_CTRL_OBJ_DELETE
	@ Deliberately no FLAG_DEFEATED_* here: a failed catch or a KO lets it respawn.
	releaseall
	end

Route119_TapuGrotto_EventScript_Decline::
	releaseall
	end

Route119_TapuGrotto_Text_ChooseWarning:
	.string "The air here is thick with power.\n"
	.string "The others watch you closely…\p"
	.string "If you raise a hand against this one,\n"
	.string "the rest will surely flee for good.\p"
	.string "Challenge it?$"
