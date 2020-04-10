[spec]

options = "+Freeciv-2.6-spec"

[info]

artists = "
    Tim F. Smith
    Daniel Speyer (mix)
    Frederic Rodrigo (mix)
    Andreas Røsdal (hex mode)
    GriffonSpade
    Wahazar
"

[extra]

sprites =
	{	"tag", "file"

;"t.l0.taiga1", "augmented2/terrain_small/tundra_base"  ;terrain-small.spec
;"t.l1.taiga1", "augmented2/terrain/blank"

; it is already in original spec: "t.l0.jungle1", "augmented2/terrain_small/jungle_base"
;"t.l1.jungle1", "augmented2/terrain/blank"

"t.l0.mangrove1", "augmented2/terrain_small/mangrove1_s"
"t.l1.mangrove1", "augmented2/terrain/blank"
}

[file]
gfx = "augmented2/terrain_small/forest2"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 64
dy = 32
pixel_border = 1

tiles = { "row", "column", "tag"

;taigas as overlay
;Center

 0,  0, "t.l1.taiga_n0e0se0s0w0nw0"
 0,  0, "t.l1.taiga_n0e1se0s0w0nw0"
 0,  0, "t.l1.taiga_n0e0se0s1w0nw0"
 0,  0, "t.l1.taiga_n0e1se0s1w0nw0"
 0,  0, "t.l1.taiga_n0e0se0s0w0nw1"
 0,  0, "t.l1.taiga_n0e1se0s0w0nw1"
 0,  0, "t.l1.taiga_n0e0se0s1w0nw1"
 0,  0, "t.l1.taiga_n0e1se0s1w0nw1"
 0,  0, "t.l1.taiga_n0e0se1s0w0nw0"
 0,  0, "t.l1.taiga_n0e1se1s0w0nw0"
 0,  0, "t.l1.taiga_n0e0se1s1w0nw0"
 0,  0, "t.l1.taiga_n0e1se1s1w0nw0"
 0,  0, "t.l1.taiga_n0e0se1s0w0nw1"
 0,  0, "t.l1.taiga_n0e1se1s0w0nw1"
 0,  0, "t.l1.taiga_n0e0se1s1w0nw1"
 0,  0, "t.l1.taiga_n0e1se1s1w0nw1"

;North
 0,  1, "t.l1.taiga_n1e0se0s0w0nw0"
 0,  1, "t.l1.taiga_n1e1se0s0w0nw0"
 0,  1, "t.l1.taiga_n1e0se0s1w0nw0"
 0,  1, "t.l1.taiga_n1e1se0s1w0nw0"
 0,  1, "t.l1.taiga_n1e0se0s0w0nw1"
 0,  1, "t.l1.taiga_n1e1se0s0w0nw1"
 0,  1, "t.l1.taiga_n1e0se0s1w0nw1"
 0,  1, "t.l1.taiga_n1e1se0s1w0nw1"
 0,  1, "t.l1.taiga_n1e0se1s0w0nw0"
 0,  1, "t.l1.taiga_n1e1se1s0w0nw0"
 0,  1, "t.l1.taiga_n1e0se1s1w0nw0"
 0,  1, "t.l1.taiga_n1e1se1s1w0nw0"
 0,  1, "t.l1.taiga_n1e0se1s0w0nw1"
 0,  1, "t.l1.taiga_n1e1se1s0w0nw1"
 0,  1, "t.l1.taiga_n1e0se1s1w0nw1"
 0,  1, "t.l1.taiga_n1e1se1s1w0nw1"

;West
 0,  2, "t.l1.taiga_n0e0se0s0w1nw0"
 0,  2, "t.l1.taiga_n0e1se0s0w1nw0"
 0,  2, "t.l1.taiga_n0e0se0s1w1nw0"
 0,  2, "t.l1.taiga_n0e1se0s1w1nw0"
 0,  2, "t.l1.taiga_n0e0se0s0w1nw1"
 0,  2, "t.l1.taiga_n0e1se0s0w1nw1"
 0,  2, "t.l1.taiga_n0e0se0s1w1nw1"
 0,  2, "t.l1.taiga_n0e1se0s1w1nw1"
 0,  2, "t.l1.taiga_n0e0se1s0w1nw0"
 0,  2, "t.l1.taiga_n0e1se1s0w1nw0"
 0,  2, "t.l1.taiga_n0e0se1s1w1nw0"
 0,  2, "t.l1.taiga_n0e1se1s1w1nw0"
 0,  2, "t.l1.taiga_n0e0se1s0w1nw1"
 0,  2, "t.l1.taiga_n0e1se1s0w1nw1"
 0,  2, "t.l1.taiga_n0e0se1s1w1nw1"
 0,  2, "t.l1.taiga_n0e1se1s1w1nw1"

;NorthWest
 0,  3, "t.l1.taiga_n1e0se0s0w1nw0"
 0,  3, "t.l1.taiga_n1e1se0s0w1nw0"
 0,  3, "t.l1.taiga_n1e0se0s1w1nw0"
 0,  3, "t.l1.taiga_n1e1se0s1w1nw0"
 0,  3, "t.l1.taiga_n1e0se0s0w1nw1"
 0,  3, "t.l1.taiga_n1e1se0s0w1nw1"
 0,  3, "t.l1.taiga_n1e0se0s1w1nw1"
 0,  3, "t.l1.taiga_n1e1se0s1w1nw1"
 0,  3, "t.l1.taiga_n1e0se1s0w1nw0"
 0,  3, "t.l1.taiga_n1e1se1s0w1nw0"
 0,  3, "t.l1.taiga_n1e0se1s1w1nw0"
 0,  3, "t.l1.taiga_n1e1se1s1w1nw0"
 0,  3, "t.l1.taiga_n1e0se1s0w1nw1"
 0,  3, "t.l1.taiga_n1e1se1s0w1nw1"
 0,  3, "t.l1.taiga_n1e0se1s1w1nw1"
 0,  3, "t.l1.taiga_n1e1se1s1w1nw1"

;improved jungle
;Center
 1,  0, "t.l1.jungle_n0e0se0s0w0nw0"
 1,  0, "t.l1.jungle_n0e1se0s0w0nw0"
 1,  0, "t.l1.jungle_n0e0se0s1w0nw0"
 1,  0, "t.l1.jungle_n0e1se0s1w0nw0"
 1,  0, "t.l1.jungle_n0e0se0s0w0nw1"
 1,  0, "t.l1.jungle_n0e1se0s0w0nw1"
 1,  0, "t.l1.jungle_n0e0se0s1w0nw1"
 1,  0, "t.l1.jungle_n0e1se0s1w0nw1"
 1,  0, "t.l1.jungle_n0e0se1s0w0nw0"
 1,  0, "t.l1.jungle_n0e1se1s0w0nw0"
 1,  0, "t.l1.jungle_n0e0se1s1w0nw0"
 1,  0, "t.l1.jungle_n0e1se1s1w0nw0"
 1,  0, "t.l1.jungle_n0e0se1s0w0nw1"
 1,  0, "t.l1.jungle_n0e1se1s0w0nw1"
 1,  0, "t.l1.jungle_n0e0se1s1w0nw1"
 1,  0, "t.l1.jungle_n0e1se1s1w0nw1"

;North
 1,  1, "t.l1.jungle_n1e0se0s0w0nw0"
 1,  1, "t.l1.jungle_n1e1se0s0w0nw0"
 1,  1, "t.l1.jungle_n1e0se0s1w0nw0"
 1,  1, "t.l1.jungle_n1e1se0s1w0nw0"
 1,  1, "t.l1.jungle_n1e0se0s0w0nw1"
 1,  1, "t.l1.jungle_n1e1se0s0w0nw1"
 1,  1, "t.l1.jungle_n1e0se0s1w0nw1"
 1,  1, "t.l1.jungle_n1e1se0s1w0nw1"
 1,  1, "t.l1.jungle_n1e0se1s0w0nw0"
 1,  1, "t.l1.jungle_n1e1se1s0w0nw0"
 1,  1, "t.l1.jungle_n1e0se1s1w0nw0"
 1,  1, "t.l1.jungle_n1e1se1s1w0nw0"
 1,  1, "t.l1.jungle_n1e0se1s0w0nw1"
 1,  1, "t.l1.jungle_n1e1se1s0w0nw1"
 1,  1, "t.l1.jungle_n1e0se1s1w0nw1"
 1,  1, "t.l1.jungle_n1e1se1s1w0nw1"

;West
 1,  2, "t.l1.jungle_n0e0se0s0w1nw0"
 1,  2, "t.l1.jungle_n0e1se0s0w1nw0"
 1,  2, "t.l1.jungle_n0e0se0s1w1nw0"
 1,  2, "t.l1.jungle_n0e1se0s1w1nw0"
 1,  2, "t.l1.jungle_n0e0se0s0w1nw1"
 1,  2, "t.l1.jungle_n0e1se0s0w1nw1"
 1,  2, "t.l1.jungle_n0e0se0s1w1nw1"
 1,  2, "t.l1.jungle_n0e1se0s1w1nw1"
 1,  2, "t.l1.jungle_n0e0se1s0w1nw0"
 1,  2, "t.l1.jungle_n0e1se1s0w1nw0"
 1,  2, "t.l1.jungle_n0e0se1s1w1nw0"
 1,  2, "t.l1.jungle_n0e1se1s1w1nw0"
 1,  2, "t.l1.jungle_n0e0se1s0w1nw1"
 1,  2, "t.l1.jungle_n0e1se1s0w1nw1"
 1,  2, "t.l1.jungle_n0e0se1s1w1nw1"
 1,  2, "t.l1.jungle_n0e1se1s1w1nw1"

;NorthWest
 1,  3, "t.l1.jungle_n1e0se0s0w1nw0"
 1,  3, "t.l1.jungle_n1e1se0s0w1nw0"
 1,  3, "t.l1.jungle_n1e0se0s1w1nw0"
 1,  3, "t.l1.jungle_n1e1se0s1w1nw0"
 1,  3, "t.l1.jungle_n1e0se0s0w1nw1"
 1,  3, "t.l1.jungle_n1e1se0s0w1nw1"
 1,  3, "t.l1.jungle_n1e0se0s1w1nw1"
 1,  3, "t.l1.jungle_n1e1se0s1w1nw1"
 1,  3, "t.l1.jungle_n1e0se1s0w1nw0"
 1,  3, "t.l1.jungle_n1e1se1s0w1nw0"
 1,  3, "t.l1.jungle_n1e0se1s1w1nw0"
 1,  3, "t.l1.jungle_n1e1se1s1w1nw0"
 1,  3, "t.l1.jungle_n1e0se1s0w1nw1"
 1,  3, "t.l1.jungle_n1e1se1s0w1nw1"
 1,  3, "t.l1.jungle_n1e0se1s1w1nw1"
 1,  3, "t.l1.jungle_n1e1se1s1w1nw1"


;mangrove overlay like jungle
;Center
 1,  0, "t.l1.mangrove_n0e0se0s0w0nw0"
 1,  0, "t.l1.mangrove_n0e1se0s0w0nw0"
 1,  0, "t.l1.mangrove_n0e0se0s1w0nw0"
 1,  0, "t.l1.mangrove_n0e1se0s1w0nw0"
 1,  0, "t.l1.mangrove_n0e0se0s0w0nw1"
 1,  0, "t.l1.mangrove_n0e1se0s0w0nw1"
 1,  0, "t.l1.mangrove_n0e0se0s1w0nw1"
 1,  0, "t.l1.mangrove_n0e1se0s1w0nw1"
 1,  0, "t.l1.mangrove_n0e0se1s0w0nw0"
 1,  0, "t.l1.mangrove_n0e1se1s0w0nw0"
 1,  0, "t.l1.mangrove_n0e0se1s1w0nw0"
 1,  0, "t.l1.mangrove_n0e1se1s1w0nw0"
 1,  0, "t.l1.mangrove_n0e0se1s0w0nw1"
 1,  0, "t.l1.mangrove_n0e1se1s0w0nw1"
 1,  0, "t.l1.mangrove_n0e0se1s1w0nw1"
 1,  0, "t.l1.mangrove_n0e1se1s1w0nw1"

;North
 1,  1, "t.l1.mangrove_n1e0se0s0w0nw0"
 1,  1, "t.l1.mangrove_n1e1se0s0w0nw0"
 1,  1, "t.l1.mangrove_n1e0se0s1w0nw0"
 1,  1, "t.l1.mangrove_n1e1se0s1w0nw0"
 1,  1, "t.l1.mangrove_n1e0se0s0w0nw1"
 1,  1, "t.l1.mangrove_n1e1se0s0w0nw1"
 1,  1, "t.l1.mangrove_n1e0se0s1w0nw1"
 1,  1, "t.l1.mangrove_n1e1se0s1w0nw1"
 1,  1, "t.l1.mangrove_n1e0se1s0w0nw0"
 1,  1, "t.l1.mangrove_n1e1se1s0w0nw0"
 1,  1, "t.l1.mangrove_n1e0se1s1w0nw0"
 1,  1, "t.l1.mangrove_n1e1se1s1w0nw0"
 1,  1, "t.l1.mangrove_n1e0se1s0w0nw1"
 1,  1, "t.l1.mangrove_n1e1se1s0w0nw1"
 1,  1, "t.l1.mangrove_n1e0se1s1w0nw1"
 1,  1, "t.l1.mangrove_n1e1se1s1w0nw1"

;West
 1,  2, "t.l1.mangrove_n0e0se0s0w1nw0"
 1,  2, "t.l1.mangrove_n0e1se0s0w1nw0"
 1,  2, "t.l1.mangrove_n0e0se0s1w1nw0"
 1,  2, "t.l1.mangrove_n0e1se0s1w1nw0"
 1,  2, "t.l1.mangrove_n0e0se0s0w1nw1"
 1,  2, "t.l1.mangrove_n0e1se0s0w1nw1"
 1,  2, "t.l1.mangrove_n0e0se0s1w1nw1"
 1,  2, "t.l1.mangrove_n0e1se0s1w1nw1"
 1,  2, "t.l1.mangrove_n0e0se1s0w1nw0"
 1,  2, "t.l1.mangrove_n0e1se1s0w1nw0"
 1,  2, "t.l1.mangrove_n0e0se1s1w1nw0"
 1,  2, "t.l1.mangrove_n0e1se1s1w1nw0"
 1,  2, "t.l1.mangrove_n0e0se1s0w1nw1"
 1,  2, "t.l1.mangrove_n0e1se1s0w1nw1"
 1,  2, "t.l1.mangrove_n0e0se1s1w1nw1"
 1,  2, "t.l1.mangrove_n0e1se1s1w1nw1"

;NorthWest
 1,  3, "t.l1.mangrove_n1e0se0s0w1nw0"
 1,  3, "t.l1.mangrove_n1e1se0s0w1nw0"
 1,  3, "t.l1.mangrove_n1e0se0s1w1nw0"
 1,  3, "t.l1.mangrove_n1e1se0s1w1nw0"
 1,  3, "t.l1.mangrove_n1e0se0s0w1nw1"
 1,  3, "t.l1.mangrove_n1e1se0s0w1nw1"
 1,  3, "t.l1.mangrove_n1e0se0s1w1nw1"
 1,  3, "t.l1.mangrove_n1e1se0s1w1nw1"
 1,  3, "t.l1.mangrove_n1e0se1s0w1nw0"
 1,  3, "t.l1.mangrove_n1e1se1s0w1nw0"
 1,  3, "t.l1.mangrove_n1e0se1s1w1nw0"
 1,  3, "t.l1.mangrove_n1e1se1s1w1nw0"
 1,  3, "t.l1.mangrove_n1e0se1s0w1nw1"
 1,  3, "t.l1.mangrove_n1e1se1s0w1nw1"
 1,  3, "t.l1.mangrove_n1e0se1s1w1nw1"
 1,  3, "t.l1.mangrove_n1e1se1s1w1nw1"

}


