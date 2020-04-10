[spec]

options = "+Freeciv-2.6-spec"

[info]

artists = "
		Peter Arbor <peter.arbor@gmail.com> (original terrain)
		Unknown Battle For Wesnoth Artist (trees)
		GriffonSpade
"

;[extra]
;sprites =
;	{	"tag", "file"
;"t.l0.taiga1", "augmented2/terrain/tundra_base"
;"t.l1.taiga1", "augmented2/terrain/blank"
;}

[file]
gfx = "augmented2/terrain/forests2"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 126
dy = 64
pixel_border = 1

tiles = { "row", "column", "tag"
;taigas as overlay
;Center

 0,  0, "t.l2.taiga_n0e0se0s0w0nw0"
 0,  0, "t.l2.taiga_n0e1se0s0w0nw0"
 0,  0, "t.l2.taiga_n0e0se0s1w0nw0"
 0,  0, "t.l2.taiga_n0e1se0s1w0nw0"
 0,  0, "t.l2.taiga_n0e0se0s0w0nw1"
 0,  0, "t.l2.taiga_n0e1se0s0w0nw1"
 0,  0, "t.l2.taiga_n0e0se0s1w0nw1"
 0,  0, "t.l2.taiga_n0e1se0s1w0nw1"
 0,  0, "t.l2.taiga_n0e0se1s0w0nw0"
 0,  0, "t.l2.taiga_n0e1se1s0w0nw0"
 0,  0, "t.l2.taiga_n0e0se1s1w0nw0"
 0,  0, "t.l2.taiga_n0e1se1s1w0nw0"
 0,  0, "t.l2.taiga_n0e0se1s0w0nw1"
 0,  0, "t.l2.taiga_n0e1se1s0w0nw1"
 0,  0, "t.l2.taiga_n0e0se1s1w0nw1"
 0,  0, "t.l2.taiga_n0e1se1s1w0nw1"

;North
 0,  1, "t.l2.taiga_n1e0se0s0w0nw0"
 0,  1, "t.l2.taiga_n1e1se0s0w0nw0"
 0,  1, "t.l2.taiga_n1e0se0s1w0nw0"
 0,  1, "t.l2.taiga_n1e1se0s1w0nw0"
 0,  1, "t.l2.taiga_n1e0se0s0w0nw1"
 0,  1, "t.l2.taiga_n1e1se0s0w0nw1"
 0,  1, "t.l2.taiga_n1e0se0s1w0nw1"
 0,  1, "t.l2.taiga_n1e1se0s1w0nw1"
 0,  1, "t.l2.taiga_n1e0se1s0w0nw0"
 0,  1, "t.l2.taiga_n1e1se1s0w0nw0"
 0,  1, "t.l2.taiga_n1e0se1s1w0nw0"
 0,  1, "t.l2.taiga_n1e1se1s1w0nw0"
 0,  1, "t.l2.taiga_n1e0se1s0w0nw1"
 0,  1, "t.l2.taiga_n1e1se1s0w0nw1"
 0,  1, "t.l2.taiga_n1e0se1s1w0nw1"
 0,  1, "t.l2.taiga_n1e1se1s1w0nw1"

;West
 0,  2, "t.l2.taiga_n0e0se0s0w1nw0"
 0,  2, "t.l2.taiga_n0e1se0s0w1nw0"
 0,  2, "t.l2.taiga_n0e0se0s1w1nw0"
 0,  2, "t.l2.taiga_n0e1se0s1w1nw0"
 0,  2, "t.l2.taiga_n0e0se0s0w1nw1"
 0,  2, "t.l2.taiga_n0e1se0s0w1nw1"
 0,  2, "t.l2.taiga_n0e0se0s1w1nw1"
 0,  2, "t.l2.taiga_n0e1se0s1w1nw1"
 0,  2, "t.l2.taiga_n0e0se1s0w1nw0"
 0,  2, "t.l2.taiga_n0e1se1s0w1nw0"
 0,  2, "t.l2.taiga_n0e0se1s1w1nw0"
 0,  2, "t.l2.taiga_n0e1se1s1w1nw0"
 0,  2, "t.l2.taiga_n0e0se1s0w1nw1"
 0,  2, "t.l2.taiga_n0e1se1s0w1nw1"
 0,  2, "t.l2.taiga_n0e0se1s1w1nw1"
 0,  2, "t.l2.taiga_n0e1se1s1w1nw1"

;NorthWest
 0,  3, "t.l2.taiga_n1e0se0s0w1nw0"
 0,  3, "t.l2.taiga_n1e1se0s0w1nw0"
 0,  3, "t.l2.taiga_n1e0se0s1w1nw0"
 0,  3, "t.l2.taiga_n1e1se0s1w1nw0"
 0,  3, "t.l2.taiga_n1e0se0s0w1nw1"
 0,  3, "t.l2.taiga_n1e1se0s0w1nw1"
 0,  3, "t.l2.taiga_n1e0se0s1w1nw1"
 0,  3, "t.l2.taiga_n1e1se0s1w1nw1"
 0,  3, "t.l2.taiga_n1e0se1s0w1nw0"
 0,  3, "t.l2.taiga_n1e1se1s0w1nw0"
 0,  3, "t.l2.taiga_n1e0se1s1w1nw0"
 0,  3, "t.l2.taiga_n1e1se1s1w1nw0"
 0,  3, "t.l2.taiga_n1e0se1s0w1nw1"
 0,  3, "t.l2.taiga_n1e1se1s0w1nw1"
 0,  3, "t.l2.taiga_n1e0se1s1w1nw1"
 0,  3, "t.l2.taiga_n1e1se1s1w1nw1"

}

