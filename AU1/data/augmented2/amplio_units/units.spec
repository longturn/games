
[spec]

; Format and options of this spec file:
options = "+Freeciv-2.6-spec"

[info]

; Apolyton Tileset created by CapTVK with thanks to the Apolyton Civ2
; Scenario League.

; Special thanks go to:
; Alex Mor and Captain Nemo for their excellent graphics work
; in the scenarios 2194 days war, Red Front, 2nd front and other misc graphics. 
; Fairline for his huge collection of original Civ2 unit spanning centuries
; Bebro for his collection of mediveal units and ships

artists = "
    Alex Mor [Alex]
    Allard H.S. Höfelt [AHS]
    Bebro [BB]
    Captain Nemo [Nemo][MHN]
    CapTVK [CT] <thomas@worldonline.nl>
    Curt Sibling [CS]
    Erwan [EW]
    Fairline [GB]
    GoPostal [GP]
    Oprisan Sorin [Sor]
    Tanelorn [T]
    Paul Klein Lankhorst / GukGuk [GG]
    Andrew ''Panda´´ Livings [APL]
    Vodvakov
    J. W. Bjerk / Eleazar <www.jwbjerk.com>
    qwm
    FiftyNine
	XYZ
	Alex Mor
	acelanceloet (Devian Art)
	Link293 (turbosquid.com)
	Bebro
	GriffonSpade
	VladimirSlavik
	CapTVK
	sourboy
	Kinboat
	Wahazar
	shadedancer619
	dunnoob
	Wyrmshadow 
	Mouse
	PikkaBird
	andythenorth
	Clinton Wood
"

[file]
gfx = "amplio2/units"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 64
dy = 48
pixel_border = 1

tiles = { "row", "column", "tag"
				; Scenario League tags in brackets
  0,  0, "u.armor"		; [Nemo]
;  0,  1, "u.howitzer"		; [Nemo]
  0,  2, "u.battleship"		; [Nemo]
  0,  3, "u.bomber"		; [GB]
  0,  4, "u.cannon"		; [CT]
  0,  5, "u.caravan"		; [Alex] & [CT]
  0,  6, "u.carrier"		; [Nemo]
  0,  7, "u.catapult"		; [CT]
  0,  8, "u.horsemen"		; [GB]
  0,  9, "u.chariot"		; [BB] & [GB]
  0, 10, "u.cruiser"		; [Nemo]
  0, 11, "u.diplomat"		; [Nemo]
  0, 12, "u.fighter"		; [Sor]
  0, 13, "u.frigate"		; [BB]
  0, 14, "u.ironclad"		; [Nemo]
  0, 15, "u.knights"		; [BB]
  0, 16, "u.legion"		; [GB]
  0, 17, "u.mech_inf"		; [GB]
;  0, 18, "u.warriors"		; [GB]
  0, 19, "u.musketeers"		; [Alex] & [CT]
  1,  0, "u.nuclear"		; [Nemo] & [CS]
  1,  1, "u.phalanx"		; [GB] & [CT]
  1,  2, "u.riflemen"		; [Alex]
  1,  3, "u.caravel"		; [BB]
  1,  4, "u.settlers"		; [MHN]
  1,  5, "u.submarine"		; [GP]
  1,  6, "u.transport"		; [Nemo]
  1,  7, "u.trireme"		; [BB]
  1,  8, "u.archers"		; [GB]
  1,  9, "u.cavalry"		; [Alex]
  1, 10, "u.cruise_missile"	; [CS]
  1, 11, "u.destroyer"		; [Nemo]
  1, 12, "u.dragoons"		; [GB]
  1, 13, "u.explorer"		; [Alex] & [CT]
  1, 14, "u.freight"		; [CT] & qwm
  1, 15, "u.galleon"		; [BB]
  1, 16, "u.partisan"		; [BB] & [CT]
  1, 17, "u.pikemen"		; [T]
  2,  0, "u.marines"		; [GB]
  2,  1, "u.spy"		; [EW] & [CT]
  2,  2, "u.engineers"		; [Nemo] & [CT]
  2,  3, "u.artillery"		; [GB]
  2,  4, "u.helicopter"		; [T]
  2,  5, "u.alpine_troops"	; [Nemo]
  2,  6, "u.stealth_bomber"	; [GB]
  2,  7, "u.stealth_fighter"	; [Nemo] & [AHS]
  2,  8, "u.aegis_cruiser"	; [GP]
  2,  9, "u.paratroopers"	; [Alex]
  2, 10, "u.elephants"		; [Alex] & [GG] & [CT]
  2, 11, "u.crusaders"		; [BB]
  2, 12, "u.fanatics"		; [GB] & [CT]
  2, 13, "u.awacs"		; [APL]
  2, 14, "u.worker"		; [GB]
  2, 15, "u.leader"		; [GB]
  2, 16, "u.barbarian_leader"	; FiftyNine
  2, 17, "u.migrants"		; Eleazar
  2, 19, "u.train"		; Eleazar
}

[extra]
sprites =
	{	"tag", "file"
		"u.mg_infantry", "augmented2/amplio_units/mg_infantry_a"
		"u.rpg_infantry", "augmented2/amplio_units/rpg_infantry_a"
		"u.railgun_destroyer", "augmented2/amplio_units/zumwalt_a"
		"u.autonomous_war_mech", "augmented2/amplio_units/warmech_a"
		"u.super_soldiers", "augmented2/amplio_units/super_soldiers_a"
		"u.drone", "augmented2/amplio_units/drone_a"
		"u.antimatter_fighter", "augmented2/amplio_units/antimatter_fighter_a"
		"u.antimatter_bomber", "augmented2/amplio_units/antimatter_bomber_a"
		"u.jet_fighter", "augmented2/amplio_units/jet_fighter_a"
		"u.technical", "augmented2/amplio_units/technical_a"
		"u.balloon", "augmented2/amplio_units/balloon_a"
		"u.anti_aircraft_gun", "augmented2/amplio_units/anti_aircraft_gun_a"
		"u.arquebusiers", "augmented2/amplio_units/arquebusiers_a"
		"u.marksman", "augmented2/amplio_units/marksman_a"
		"u.line_infantry", "augmented2/amplio_units/line_infantry_a"
		"u.halberdier", "augmented2/amplio_units/halberdier_a"
		"u.sniper", "augmented2/amplio_units/sniper_a"  				
		"u.arbalest", "augmented2/amplio_units/arbalest_a"
		"u.grenadier", "augmented2/amplio_units/grenadier_a"
		"u.stormtrooper", "augmented2/amplio_units/stormtrooper_a"
		"u.turret_cannon", "augmented2/amplio_units/turret_cannon_a"
		"u.turret_aa_gun", "augmented2/amplio_units/turret_aa_gun_a"
		"u.torpedo", "augmented2/amplio_units/torpedo_a"
		"u.armoured_train", "augmented2/amplio_units/armoured_train_a"
		"u.self_propelled_gun", "augmented2/amplio_units/self_propelled_gun_a"
		"u.reactive_armor", "augmented2/amplio_units/reactive_armor_a"
		"u.bombard", "augmented2/amplio_units/bombard_a"
		"u.gun_howitzer", "augmented2/amplio_units/gun_howitzer_a"
		"u.ballista", "augmented2/amplio_units/ballista_a"
;		"u.cannon", "augmented2/amplio_units/cannon_a"
		"u.galley", "augmented2/amplio_units/galley_a"
		"u.cog", "augmented2/amplio_units/cog_a"
		"u.monitor", "augmented2/amplio_units/monitor_a"
		"u.paddle_steamer", "augmented2/amplio_units/paddle_steamer_a"
		"u.patrol_boat", "augmented2/amplio_units/patrol_boat_a"
		"u.steam_barge", "augmented2/amplio_units/steam_barge_a"
		"u.diesel_barge", "augmented2/amplio_units/diesel_barge_a"
		"u.howitzer", "augmented2/amplio_units/self_propelled_howitzer_a"
		"u.vikings", "augmented2/amplio_units/viking_a"
		"u.corsairs", "augmented2/amplio_units/corsair_a"
		"u.battering_ram", "augmented2/amplio_units/battering_ram_a"
		"u.longboat", "augmented2/amplio_units/Longship3a"
		"u.flagship_frigate", "augmented2/amplio_units/Flagship_Frigate_a"
		"u.aak", "augmented2/amplio_units/Aak_a"
		"u.raft", "augmented2/amplio_units/raft_a"
		"u.Abomb", "augmented2/amplio_units/Abomb_a"
		"u.GBU", "augmented2/amplio_units/GBU_a"
		"u.zeppelin", "augmented2/amplio_units/zeppelin_a"
		"u.airplane", "augmented2/amplio_units/airplane_a"
		"u.strike_aircraft", "augmented2/amplio_units/strike_aircraft_a"
		"u.nuclear_submarine", "augmented2/amplio_units/nuclear_submarine_a"
		"u.strike_jet", "augmented2/amplio_units/strike_jet_a"
		"u.riot_police", "augmented2/amplio_units/riot_police_a"
		"u.navy_seals", "augmented2/amplio_units/navy_seals_a"
		"u.slave", "augmented2/amplio_units/slave_a"
		"u.mounted_samurai", "augmented2/amplio_units/mounted_samurai_a"
		"u.samurai", "augmented2/amplio_units/samurai_a"
		"u.junk", "augmented2/amplio_units/junk_a"
		"u.mounted_archery", "augmented2/amplio_units/mounted_archery_a"
		"u.dromedari", "augmented2/amplio_units/dromedari_a"
		"u.janissaries", "augmented2/amplio_units/janissaries_a"
		"u.AT-gun", "augmented2/amplio_units/AT-gun_a"
		"u.ninja", "augmented2/amplio_units/ninja_a"
		"u.tribe", "augmented2/amplio_units/tribe_a"
		"u.messenger", "augmented2/amplio_units/messenger_a"
		"u.hunters", "augmented2/amplio_units/hunters_a"
		"u.canoes", "augmented2/amplio_units/canoes_a"
		"u.swordsmen", "augmented2/amplio_units/swordsmen_a"
		"u.crusaders_horse", "augmented2/amplio_units/crusaders_horse_a"
		"u.bicycle_infantry", "augmented2/amplio_units/bicycle_infantry_a"
		"u.mounted_inf", "augmented2/amplio_units/mounted_inf_a"
		"u.lancers", "augmented2/amplio_units/lancers_a"
		"u.dragoon", "augmented2/amplio_units/dragoon_a"
		"u.militia", "augmented2/amplio_units/militia_a"
		"u.missile", "augmented2/amplio_units/missile_a"
		"u.armor_car", "augmented2/amplio_units/armor_car_a"
		"u.atv_infantry", "augmented2/amplio_units/ATV_infantry_a"
		"u.builder", "augmented2/amplio_units/builders_a"
		"u.clipper", "augmented2/amplio_units/clipper_a"
		"u.freighter", "augmented2/amplio_units/freighter_a"
		"u.jetliner", "augmented2/amplio_units/jetliner_PikkaBird"
		"u.brig", "augmented2/amplio_units/brig_a"
		"u.pirates_brig", "augmented2/amplio_units/pirates_brig_a"
		"u.kon-tiki_raft", "augmented2/amplio_units/kon-tiki_raft_a"
		"u.pirates", "augmented2/amplio_units/pirates_a"
		"u.tactical_abm", "augmented2/amplio_units/freeciv-sam-patriot-3b"
		"u.streltsy", "augmented2/amplio_units/streltsy_a"
		"u.hovercraft", "augmented2/amplio_units/hovercraft_a"
		"u.skirmishers", "augmented2/amplio_units/skirmishers_a"
		"u.scout", "augmented2/amplio_units/scout_a"
		"u.wagenburg", "augmented2/amplio_units/wagenburg_a"
		"u.floating_bridge", "augmented2/amplio_units/floating_bridge_defensegovClintonWood"
		"u.cart", "augmented2/amplio_units/cart_a"
; swapped standard graphics
		"u.warriors", "augmented2/amplio_units/warriors_a"
	}

