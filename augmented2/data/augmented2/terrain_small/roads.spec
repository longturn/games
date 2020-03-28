
[spec]

; Format and options of this spec file:
options = "+Freeciv-2.6-spec"

[info]

artists = "
    GriffonSpade
"

[file]
gfx = "augmented2/terrain_small/roadss"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 64
dy = 32
pixel_border = 1

tiles = { "row", "column","tag"
; pawed roads

  0,    0, "road.road_isolated"
  0,    1, "road.road_n"
  0,    2, "road.road_ne"
  0,    3, "road.road_e"
  0,    4, "road.road_se"
  0,    5, "road.road_s"
  0,    6, "road.road_sw"
  0,    7, "road.road_w"
  0,    8, "road.road_nw"

}
