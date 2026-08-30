LilycoveCity_DepartmentStore_4F_MapScripts::
	.byte 0

LilycoveCity_DepartmentStore_4F_EventScript_Gentleman::
	msgbox LilycoveCity_DepartmentStore_4F_Text_AttackOrDefenseTM, MSGBOX_NPC
	end

LilycoveCity_DepartmentStore_4F_EventScript_Woman::
	msgbox LilycoveCity_DepartmentStore_4F_Text_FiftyDifferentTMs, MSGBOX_NPC
	end

LilycoveCity_DepartmentStore_4F_EventScript_Youngster::
	msgbox LilycoveCity_DepartmentStore_4F_Text_PokemonOnlyHaveFourMoves, MSGBOX_NPC
	end

LilycoveCity_DepartmentStore_4F_EventScript_ClerkLeft::
	lock
	faceplayer
	message gText_HowMayIServeYou
	waitmessage
	pokemart LilycoveCity_DepartmentStore_4F_Pokemart_AttackTMs
	msgbox gText_PleaseComeAgain, MSGBOX_DEFAULT
	release
	end

	.align 2
LilycoveCity_DepartmentStore_4F_Pokemart_AttackTMs:
	.2byte ITEM_TM_FIRE_BLAST
	.2byte ITEM_TM_THUNDER
	.2byte ITEM_TM_BLIZZARD
	.2byte ITEM_TM_HYPER_BEAM
	.2byte ITEM_TM_EARTHQUAKE
	.2byte ITEM_TM_SHADOW_BALL
	.2byte ITEM_TM_SLUDGE_BOMB
	.2byte ITEM_TM_BRICK_BREAK
	.2byte ITEM_TM_AERIAL_ACE
	.2byte ITEM_TM_ROCK_TOMB
	.2byte ITEM_TM_FACADE
	.2byte ITEM_TM_SHOCK_WAVE
	pokemartlistend

LilycoveCity_DepartmentStore_4F_EventScript_ClerkRight::
	lock
	faceplayer
	goto_if_unset FLAG_BADGE08_GET, LilycoveCity_DepartmentStore_4F_EventScript_ClerkRightNoBadge
	message gText_HowMayIServeYou
	waitmessage
	pokemart LilycoveCity_DepartmentStore_4F_Pokemart_DefenseTMs
	msgbox gText_PleaseComeAgain, MSGBOX_DEFAULT
	release
	end

LilycoveCity_DepartmentStore_4F_EventScript_ClerkRightNoBadge::
	msgbox LilycoveCity_DepartmentStore_4F_Text_EightBadgesOnly, MSGBOX_DEFAULT
	release
	end

	.align 2
LilycoveCity_DepartmentStore_4F_Pokemart_DefenseTMs:
	.2byte ITEM_LEFTOVERS
	.2byte ITEM_FOCUS_SASH
	.2byte ITEM_CHOICE_BAND
	.2byte ITEM_CHOICE_SPECS
	.2byte ITEM_CHOICE_SCARF
	.2byte ITEM_LIFE_ORB
	.2byte ITEM_ASSAULT_VEST
	.2byte ITEM_EVIOLITE
	.2byte ITEM_ROCKY_HELMET
	.2byte ITEM_EXPERT_BELT
	.2byte ITEM_HEAVY_DUTY_BOOTS
	.2byte ITEM_WEAKNESS_POLICY
	.2byte ITEM_SHELL_BELL
	.2byte ITEM_SCOPE_LENS
	.2byte ITEM_KINGS_ROCK
	.2byte ITEM_AIR_BALLOON
	.2byte ITEM_MENTAL_HERB
	.2byte ITEM_BLACK_SLUDGE
	.2byte ITEM_TOXIC_ORB
	.2byte ITEM_FLAME_ORB
	.2byte ITEM_DAMP_ROCK
	.2byte ITEM_SMOOTH_ROCK
	pokemartlistend

LilycoveCity_DepartmentStore_4F_Text_AttackOrDefenseTM:
	.string "The left counter sells TMs to anyone.\p"
	.string "The right one wants all eight BADGES\n"
	.string "before it will serve you.\p"
	.string "I've got seven. I've been staring at\n"
	.string "it for an hour.$"

LilycoveCity_DepartmentStore_4F_Text_FiftyDifferentTMs:
	.string "The TMs here can be used over and\n"
	.string "over now.\p"
	.string "I bought BLIZZARD once and taught it\n"
	.string "to my whole team.$"

LilycoveCity_DepartmentStore_4F_Text_PokemonOnlyHaveFourMoves:
	.string "I'd like to get all the different TMs,\n"
	.string "but a POKéMON learns only four moves.$"

LilycoveCity_DepartmentStore_4F_Text_EightBadgesOnly:
	.string "I'm sorry. This counter serves\n"
	.string "TRAINERS with all eight BADGES.\p"
	.string "Held items decide battles, and the\n"
	.string "LEAGUE would rather they decided\l"
	.string "battles between people who can use\l"
	.string "them.\p"
	.string "Come back with the eighth BADGE and\n"
	.string "the counter is yours.$"
