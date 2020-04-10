
[spec]

; Format and options of this spec file:
options = "+Freeciv-2.6-spec"

[info]

artists = "
    Tim F. Smith
    Andreas Røsdal (hex mode)
    Daniel Speyer
    GriffonSpade
"

[file]
gfx = "augmented2/terrain_small/roads_unpaved"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 64
dy = 32
pixel_border = 1

tiles = { "row", "column","tag"


; Unpaved Roads

  0,    0, "road.road_unpaved_isolated"
  0,    1, "road.road_unpaved_n"
  0,    2, "road.road_unpaved_ne"
  0,    3, "road.road_unpaved_e"
  0,    4, "road.road_unpaved_se"
  0,    5, "road.road_unpaved_s"
  0,    6, "road.road_unpaved_sw"
  0,    7, "road.road_unpaved_w"
  0,    8, "road.road_unpaved_nw"


}
