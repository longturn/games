[spec]

; Format and options of this spec file:
options = "+Freeciv-2.6-spec"

[info]

artists = "
		Wahazar
		VladimirSlavik
                GriffonSpade
                XYZ
"
; Augmented2 modpack

[file]
gfx = "hexemplio/terrain"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 126
dy = 64
pixel_border = 1

tiles = { "row", "column","tag"

; terrain - layer 0
  0,    2,  "t.l0.wooded_hills1"			

  0,    3,  "t.l0.taiga1"			;[PA]
 
  0,    5,  "t.l0.mangrove1"			;{PA}


; terrain - layer 1
  5,    0,  "t.l1.wooded_hills1"

  5,    0,  "t.l1.taiga1"

;  5,    0,  "t.l1.mangrove1"

}

[extra]

sprites =
	{	"tag", "file"
		"ts.rice", "augmented2/terrain/rice_a"
		"tx.pollution_smoke", "augmented2/terrain/pollution_a"
		"tx.wind_turbine", "augmented2/terrain/wind_turbines_hex"
;		"base.waterlock_fg", "augmented2/terrain/waterlock_fg_a"
;		"base.waterlock_bg", "augmented2/terrain/waterlock_bg_a"

	}
