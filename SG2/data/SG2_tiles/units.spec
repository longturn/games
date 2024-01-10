
[spec]

; Format and options of this spec file:
options = "+Freeciv-spec-Devel-2019-Jul-03"

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
"

[file]
gfx = "SG2_tiles/units"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 64
dy = 48
pixel_border = 1

tiles = { "row", "column", "tag"
				; Scenario League tags in brackets
  0,  0, "u.armor"		; [Nemo]
  0,  1, "u.howitzer"		; [Nemo]
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
  0, 18, "u.warriors"		; [GB]
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
  1, 18, "u.raider"		; GriffonSpade
  1, 19, "u.navytroops"		; Sketlux (XYZ)
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
  2, 18, "u.knarr"		; Sketlux (XYZ)
  2, 19, "u.scholar"		; Sketlux (XYZ)
  3,  0, "u.barge"    		; Sketlux
  3,  1, "u.tribal_worker"   	; modded_by_Sketlux (XYZ)
  3,  2, "u.immigrant"  	; 
  3,  3, "u.scribe"     	; 
  3,  4, "u.inventor"    	; modded_by_Sketlux (XYZ)
  3,  5, "u.canoe"   		; Sketlux (XYZ)
  3,  6, "u.scientist"  	; Sketlux (XYZ)
  3,  7, "u.infantry"   	; 
  3,  8, "u.operative"  	; Sketlux (XYZ)
  3,  9, "u.nsubmarine" 	; 
  3, 10, "u.fusion_bomber" 	; Sketlux (XYZ)
  3, 11, "u.longboat"  		; Sketlux (XYZ)
  3, 12, "u.srcaravel" 		; modded_by_Sketlux (XYZ)
  3, 13, "u.missile" 		; 
  3, 14, "u.cruise_missile" 	; 
  3, 15, "u.fusion_missile" 	; 
  3, 16, "u.trebuchet" 		; HF & louis94
  3, 17, "u.pirogue"		; Ngunjaca
  3, 18, "u.cog"		; Ngunjaca
  3, 19, "u.pcutter"		; VladimirSlavik
  4,  0, "u.militia"		; GriffonSpade
  4,  1, "u.mounted_militia"	; GriffonSpade
  4,  2, "u.transport_aircraft"	; Sketlux (XYZ)
  4,  3, "u.jet_fighter"	; Sketlux (XYZ)
  4,  4, "u.tribal_knarr"	; Sketlux (XYZ)
  4,  5, "u.mobile_howitzer"	; GriffonSpade
  4,  6, "u.dromedarii"		; moded_by_Sketlux (XYZ)
  4,  7, "u.sam"		; VladimirSlavik  
  4,  8, "u.arbalest"		; Sketlux (XYZ)
  4,  9, "u.advanced_warrior"   ; GriffonSpade
  4, 10, "u.scout"		; GriffonSpade
  4, 11, "u.mounted_archer"	; GriffonSpade
  4, 12, "u.quinquireme"	; Ngunjaca
  4, 12, "u.migrants"		; 
  4, 13, "u.nuclearbomb"	;
  4, 14, "u.cargoair"		; Sketlux (XYZ)
  4, 15, "u.fusion_fighter"	; 
  4, 16, "u.flagship_frigate"	; modded_by_Sketlux (XYZ)
  4, 17, "u.fusion_armor"	; 
  4, 18, "u.brig"		; Sketlux (XYZ)
  4, 19, "u.fusion_battleship"	;
  5,  0, "u.early_fighter"	; GriffonSpade
  5,  1, "u.early_bomber"	; Sketlux (XYZ)
  5,  2, "u.early_jet_fighter"	; VladimirSlavik
  5,  3, "u.advanced_bomber"	; GriffonSpade
  5,  4, "u.attack_aircraft"	; modded_by_Sketlux (XYZ)
  5,  5, "u.advanced_attack_aircraft"	; Sketlux (XYZ)
  5,  6, "u.early_armor"	; Sketlux (XYZ)
  5,  7, "u.advanced_armor"	; VladimirSlavik
  5,  8, "u.tank_hunter"	; GriffonSpade
  5,  9, "u.technical"		; VladimirSlavik
  5,  10, "u.transport_helicopter" 	; Sketlux (XYZ)
  5,  11, "u.gunship_helicopter"; Sketlux (XYZ)	
  5,  12, "u.motorized_infantry" 	; Sketlux (XYZ)
  5,  13, "u.samurai"		; Sketlux (XYZ)
  5,  14, "u.halberdier" 	; modded_by_Sketlux (XYZ)
  5,  15, "u.grenadier" 	; Sketlux (XYZ)
  5,  16, "u.stormtrooper" 	; Sketlux (XYZ)
  5,  17, "u.mounted_infantry" 	; modded_by_Sketlux (XYZ)
  5,  18, "u.early_submarine" 	; modded_by_Sketlux (XYZ)
  5,  19, "u.zeppelin"	 	; Sketlux (XYZ)
  6,   0, "u.dredger"		; VladimirSlavik
  6,   1, "u.monitor"		; Sketlux (XYZ)
  6,   2, "u.tachanka"		; Sketlux (XYZ)
  6,   3, "u.armored_car"	; Sketlux (XYZ) 
  6,   4, "u.armored_train"     ; Sketlux (XYZ) 
}
