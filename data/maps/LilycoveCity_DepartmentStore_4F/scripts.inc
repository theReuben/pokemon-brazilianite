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
	message gText_HowMayIServeYou
	waitmessage
	pokemart LilycoveCity_DepartmentStore_4F_Pokemart_DefenseTMs
	msgbox gText_PleaseComeAgain, MSGBOX_DEFAULT
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
	.string "Hmm…\p"
	.string "A TM on the left counter…\n"
	.string "Or something to hold on the right…\p"
	.string "It's no easy matter to decide what\n"
	.string "a POKéMON should carry.$"

LilycoveCity_DepartmentStore_4F_Text_FiftyDifferentTMs:
	.string "The TMs here can be used over and\n"
	.string "over now.\p"
	.string "I bought BLIZZARD once and taught it\n"
	.string "to my whole team.$"

LilycoveCity_DepartmentStore_4F_Text_PokemonOnlyHaveFourMoves:
	.string "I'd like to get all the different TMs,\n"
	.string "but a POKéMON learns only four moves.$"

