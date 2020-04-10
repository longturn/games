[spec]

options = "+Freeciv-2.6-spec"

artists = "
		Peter Arbor <peter.arbor@gmail.com> (original terrain)
		Unknown Battle For Wesnoth Artist (trees)
		GriffonSpade
"

[extra]

sprites =
	{	"tag", "file"

"t.mangrove_color", "augmented2/terrain/tundra_base"
"t.blend.mangrove", "augmented2/terrain/blank"
"t.l0.mangrove1", "augmented2/terrain/ocean_base"

}

[file]
;gfx = "augmented2/terrain/forests2"
gfx = "hexemplio/water1"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 126
dy = 64
pixel_border = 1

tiles = { "row", "column", "tag"
;mangroves as overlay

 2, 0,  "t.l1.mangrove_cell_u000"
 2, 1,  "t.l1.mangrove_cell_u100"
 2, 2,  "t.l1.mangrove_cell_u010"
 2, 3,  "t.l1.mangrove_cell_u110"
 2, 4,  "t.l1.mangrove_cell_u001"
 2, 5,  "t.l1.mangrove_cell_u101"
 2, 6,  "t.l1.mangrove_cell_u011"
 2, 7,  "t.l1.mangrove_cell_u111"

}

[file]
gfx = "hexemplio/water2"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 64
dy = 32
pixel_border = 1

tiles = { "row", "column","tag"

; coast cell sprites.  See doc/README.graphics
 2, 0,  "t.l1.mangrove_cell_d000"
 2, 1,  "t.l1.mangrove_cell_d100"
 2, 2,  "t.l1.mangrove_cell_d010"
 2, 3,  "t.l1.mangrove_cell_d110"
 2, 4,  "t.l1.mangrove_cell_d001"
 2, 5,  "t.l1.mangrove_cell_d101"
 2, 6,  "t.l1.mangrove_cell_d011"
 2, 7,  "t.l1.mangrove_cell_d111"


}

[file]
gfx = "hexemplio/water3"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 47
dy = 32
pixel_border = 1

tiles = { "row", "column","tag"

 2, 0,  "t.l1.mangrove_cell_l000"
 2, 0,  "t.l1.mangrove_cell_l010"
 2, 1,  "t.l1.mangrove_cell_l100"
 2, 1,  "t.l1.mangrove_cell_l110"
 2, 2,  "t.l1.mangrove_cell_l001"
 2, 2,  "t.l1.mangrove_cell_l011"
 2, 3,  "t.l1.mangrove_cell_l101"
 2, 3,  "t.l1.mangrove_cell_l111"

 2, 4,  "t.l1.mangrove_cell_r000"
 2, 4,  "t.l1.mangrove_cell_r010"
 2, 5,  "t.l1.mangrove_cell_r100"
 2, 5,  "t.l1.mangrove_cell_r110"
 2, 6,  "t.l1.mangrove_cell_r001"
 2, 6,  "t.l1.mangrove_cell_r011"
 2, 7,  "t.l1.mangrove_cell_r101"
 2, 7,  "t.l1.mangrove_cell_r111"

}


