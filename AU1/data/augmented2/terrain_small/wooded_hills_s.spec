
[spec]

; Format and options of this spec file:
options = "+Freeciv-2.6-spec"

[info]

artists = "
    Andreas Røsdal (hex mode)
"

[file]
gfx = "augmented2/terrain_small/wooded_hills_s"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 64
dy = 32
pixel_border = 1

tiles = { "row", "column","tag"


;hills as overlay

 0,  0, "t.l1.wooded_hills_n0e0se0s0w0nw0"
 0,  1, "t.l1.wooded_hills_n1e0se0s0w0nw0"
 0,  2, "t.l1.wooded_hills_n0e1se0s0w0nw0"
 0,  3, "t.l1.wooded_hills_n1e1se0s0w0nw0"
 0,  4, "t.l1.wooded_hills_n0e0se0s1w0nw0"
 0,  5, "t.l1.wooded_hills_n1e0se0s1w0nw0"
 0,  6, "t.l1.wooded_hills_n0e1se0s1w0nw0"
 0,  7, "t.l1.wooded_hills_n1e1se0s1w0nw0"
 1,  0, "t.l1.wooded_hills_n0e0se0s0w1nw0"
 1,  1, "t.l1.wooded_hills_n1e0se0s0w1nw0"
 1,  2, "t.l1.wooded_hills_n0e1se0s0w1nw0"
 1,  3, "t.l1.wooded_hills_n1e1se0s0w1nw0"
 1,  4, "t.l1.wooded_hills_n0e0se0s1w1nw0"
 1,  5, "t.l1.wooded_hills_n1e0se0s1w1nw0"
 1,  6, "t.l1.wooded_hills_n0e1se0s1w1nw0"
 1,  7, "t.l1.wooded_hills_n1e1se0s1w1nw0"

 ; The below sprites are duplicates of the previous sprites,
 ; since there aren't yet graphics for the extra hex directions.
 
 0,  0, "t.l1.wooded_hills_n0e0se0s0w0nw1"
 0,  1, "t.l1.wooded_hills_n1e0se0s0w0nw1"
 0,  2, "t.l1.wooded_hills_n0e1se0s0w0nw1"
 0,  3, "t.l1.wooded_hills_n1e1se0s0w0nw1"
 0,  4, "t.l1.wooded_hills_n0e0se0s1w0nw1"
 0,  5, "t.l1.wooded_hills_n1e0se0s1w0nw1"
 0,  6, "t.l1.wooded_hills_n0e1se0s1w0nw1"
 0,  7, "t.l1.wooded_hills_n1e1se0s1w0nw1"
 1,  0, "t.l1.wooded_hills_n0e0se0s0w1nw1"
 1,  1, "t.l1.wooded_hills_n1e0se0s0w1nw1"
 1,  2, "t.l1.wooded_hills_n0e1se0s0w1nw1"
 1,  3, "t.l1.wooded_hills_n1e1se0s0w1nw1"
 1,  4, "t.l1.wooded_hills_n0e0se0s1w1nw1"
 1,  5, "t.l1.wooded_hills_n1e0se0s1w1nw1"
 1,  6, "t.l1.wooded_hills_n0e1se0s1w1nw1"
 1,  7, "t.l1.wooded_hills_n1e1se0s1w1nw1"
 0,  0, "t.l1.wooded_hills_n0e0se1s0w0nw0"
 0,  1, "t.l1.wooded_hills_n1e0se1s0w0nw0"
 0,  2, "t.l1.wooded_hills_n0e1se1s0w0nw0"
 0,  3, "t.l1.wooded_hills_n1e1se1s0w0nw0"
 0,  4, "t.l1.wooded_hills_n0e0se1s1w0nw0"
 0,  5, "t.l1.wooded_hills_n1e0se1s1w0nw0"
 0,  6, "t.l1.wooded_hills_n0e1se1s1w0nw0"
 0,  7, "t.l1.wooded_hills_n1e1se1s1w0nw0"
 1,  0, "t.l1.wooded_hills_n0e0se1s0w1nw0"
 1,  1, "t.l1.wooded_hills_n1e0se1s0w1nw0"
 1,  2, "t.l1.wooded_hills_n0e1se1s0w1nw0"
 1,  3, "t.l1.wooded_hills_n1e1se1s0w1nw0"
 1,  4, "t.l1.wooded_hills_n0e0se1s1w1nw0"
 1,  5, "t.l1.wooded_hills_n1e0se1s1w1nw0"
 1,  6, "t.l1.wooded_hills_n0e1se1s1w1nw0"
 1,  7, "t.l1.wooded_hills_n1e1se1s1w1nw0"
 0,  0, "t.l1.wooded_hills_n0e0se1s0w0nw1"
 0,  1, "t.l1.wooded_hills_n1e0se1s0w0nw1"
 0,  2, "t.l1.wooded_hills_n0e1se1s0w0nw1"
 0,  3, "t.l1.wooded_hills_n1e1se1s0w0nw1"
 0,  4, "t.l1.wooded_hills_n0e0se1s1w0nw1"
 0,  5, "t.l1.wooded_hills_n1e0se1s1w0nw1"
 0,  6, "t.l1.wooded_hills_n0e1se1s1w0nw1"
 0,  7, "t.l1.wooded_hills_n1e1se1s1w0nw1"
 1,  0, "t.l1.wooded_hills_n0e0se1s0w1nw1"
 1,  1, "t.l1.wooded_hills_n1e0se1s0w1nw1"
 1,  2, "t.l1.wooded_hills_n0e1se1s0w1nw1"
 1,  3, "t.l1.wooded_hills_n1e1se1s0w1nw1"
 1,  4, "t.l1.wooded_hills_n0e0se1s1w1nw1"
 1,  5, "t.l1.wooded_hills_n1e0se1s1w1nw1"
 1,  6, "t.l1.wooded_hills_n0e1se1s1w1nw1"
 1,  7, "t.l1.wooded_hills_n1e1se1s1w1nw1"

}
