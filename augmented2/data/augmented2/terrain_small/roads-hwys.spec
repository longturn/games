
[spec]

; Format and options of this spec file:
options = "+Freeciv-2.6-spec"

[info]

artists = "
    Andreas Røsdal (hex mode)
"

[file]
gfx = "augmented2/terrain_small/roads-highways"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 64
dy = 32
pixel_border = 1

tiles = { "row", "column","tag"


; hwys

  0,    0, "road.hwy_isolated"
  0,    1, "road.hwy_n"
  0,    2, "road.hwy_ne"
  0,    3, "road.hwy_e"
  0,    4, "road.hwy_se"
  0,    5, "road.hwy_s"
  0,    6, "road.hwy_sw"
  0,    7, "road.hwy_w"
  0,    8, "road.hwy_nw"

}
