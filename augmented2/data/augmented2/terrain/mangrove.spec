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
;"t.mangrove_color", "augmented2/terrain/tundra_base"
;"t.blend.mangrove", "augmented2/terrain/blank"
;"t.l0.mangrove1", "augmented2/terrain/ocean_base"
"t.l1.mangrove1", "augmented2/terrain/mangrove1"
}

[file]
gfx = "augmented2/terrain/forests2"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 126
dy = 64
pixel_border = 1

tiles = { "row", "column", "tag"
;mangroves as overlay
;Center

 2,  0, "t.l2.mangrove_n0e0se0s0w0nw0"
 2,  0, "t.l2.mangrove_n0e1se0s0w0nw0"
 2,  0, "t.l2.mangrove_n0e0se0s1w0nw0"
 2,  0, "t.l2.mangrove_n0e1se0s1w0nw0"
 2,  0, "t.l2.mangrove_n0e0se0s0w0nw1"
 2,  0, "t.l2.mangrove_n0e1se0s0w0nw1"
 2,  0, "t.l2.mangrove_n0e0se0s1w0nw1"
 2,  0, "t.l2.mangrove_n0e1se0s1w0nw1"
 2,  0, "t.l2.mangrove_n0e0se1s0w0nw0"
 2,  0, "t.l2.mangrove_n0e1se1s0w0nw0"
 2,  0, "t.l2.mangrove_n0e0se1s1w0nw0"
 2,  0, "t.l2.mangrove_n0e1se1s1w0nw0"
 2,  0, "t.l2.mangrove_n0e0se1s0w0nw1"
 2,  0, "t.l2.mangrove_n0e1se1s0w0nw1"
 2,  0, "t.l2.mangrove_n0e0se1s1w0nw1"
 2,  0, "t.l2.mangrove_n0e1se1s1w0nw1"

;North
 2,  1, "t.l2.mangrove_n1e0se0s0w0nw0"
 2,  1, "t.l2.mangrove_n1e1se0s0w0nw0"
 2,  1, "t.l2.mangrove_n1e0se0s1w0nw0"
 2,  1, "t.l2.mangrove_n1e1se0s1w0nw0"
 2,  1, "t.l2.mangrove_n1e0se0s0w0nw1"
 2,  1, "t.l2.mangrove_n1e1se0s0w0nw1"
 2,  1, "t.l2.mangrove_n1e0se0s1w0nw1"
 2,  1, "t.l2.mangrove_n1e1se0s1w0nw1"
 2,  1, "t.l2.mangrove_n1e0se1s0w0nw0"
 2,  1, "t.l2.mangrove_n1e1se1s0w0nw0"
 2,  1, "t.l2.mangrove_n1e0se1s1w0nw0"
 2,  1, "t.l2.mangrove_n1e1se1s1w0nw0"
 2,  1, "t.l2.mangrove_n1e0se1s0w0nw1"
 2,  1, "t.l2.mangrove_n1e1se1s0w0nw1"
 2,  1, "t.l2.mangrove_n1e0se1s1w0nw1"
 2,  1, "t.l2.mangrove_n1e1se1s1w0nw1"

;West
 2,  2, "t.l2.mangrove_n0e0se0s0w1nw0"
 2,  2, "t.l2.mangrove_n0e1se0s0w1nw0"
 2,  2, "t.l2.mangrove_n0e0se0s1w1nw0"
 2,  2, "t.l2.mangrove_n0e1se0s1w1nw0"
 2,  2, "t.l2.mangrove_n0e0se0s0w1nw1"
 2,  2, "t.l2.mangrove_n0e1se0s0w1nw1"
 2,  2, "t.l2.mangrove_n0e0se0s1w1nw1"
 2,  2, "t.l2.mangrove_n0e1se0s1w1nw1"
 2,  2, "t.l2.mangrove_n0e0se1s0w1nw0"
 2,  2, "t.l2.mangrove_n0e1se1s0w1nw0"
 2,  2, "t.l2.mangrove_n0e0se1s1w1nw0"
 2,  2, "t.l2.mangrove_n0e1se1s1w1nw0"
 2,  2, "t.l2.mangrove_n0e0se1s0w1nw1"
 2,  2, "t.l2.mangrove_n0e1se1s0w1nw1"
 2,  2, "t.l2.mangrove_n0e0se1s1w1nw1"
 2,  2, "t.l2.mangrove_n0e1se1s1w1nw1"

;NorthWest
 2,  3, "t.l2.mangrove_n1e0se0s0w1nw0"
 2,  3, "t.l2.mangrove_n1e1se0s0w1nw0"
 2,  3, "t.l2.mangrove_n1e0se0s1w1nw0"
 2,  3, "t.l2.mangrove_n1e1se0s1w1nw0"
 2,  3, "t.l2.mangrove_n1e0se0s0w1nw1"
 2,  3, "t.l2.mangrove_n1e1se0s0w1nw1"
 2,  3, "t.l2.mangrove_n1e0se0s1w1nw1"
 2,  3, "t.l2.mangrove_n1e1se0s1w1nw1"
 2,  3, "t.l2.mangrove_n1e0se1s0w1nw0"
 2,  3, "t.l2.mangrove_n1e1se1s0w1nw0"
 2,  3, "t.l2.mangrove_n1e0se1s1w1nw0"
 2,  3, "t.l2.mangrove_n1e1se1s1w1nw0"
 2,  3, "t.l2.mangrove_n1e0se1s0w1nw1"
 2,  3, "t.l2.mangrove_n1e1se1s0w1nw1"
 2,  3, "t.l2.mangrove_n1e0se1s1w1nw1"
 2,  3, "t.l2.mangrove_n1e1se1s1w1nw1"

}

