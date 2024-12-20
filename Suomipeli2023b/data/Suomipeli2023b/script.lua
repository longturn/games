-- Copyright (c) 2007-2020 Freeciv21 and Freeciv contributors. This file is
--   part of Freeciv21. Freeciv21 is free software: you can redistribute it
--   and/or modify it under the terms of the GNU General Public License
--   as published by the Free Software Foundation, either version 3
--   of the License,  or (at your option) any later version.
--   You should have received a copy of the GNU General Public License
--   along with Freeciv21. If not, see https://www.gnu.org/licenses/.

-- This file is for lua-functionality that is specific to a given
-- ruleset. When freeciv loads a ruleset, it also loads script
-- file called 'default.lua'. The one loaded if your ruleset
-- does not provide an override is default/default.lua.


-- Place Ruins at the location of the destroyed city.
function city_destroyed_callback(city, loser, destroyer)
  city.tile:create_extra("Ruins", NIL)
  -- continue processing
  return false
end

signal.connect("city_destroyed", "city_destroyed_callback")

-- Check if there is certain terrain in ANY CAdjacent tile.
function adjacent_to(tile, terrain_name)
  for adj_tile in tile:circle_iterate(1) do
    if adj_tile.id ~= tile.id then
      local adj_terr = adj_tile.terrain
      local adj_name = adj_terr:rule_name()
      if adj_name == terrain_name then
        return true
      end
    end
  end
  return false
end

-- Check if there is certain terrain in ALL CAdjacent tiles.
function surrounded_by(tile, terrain_name)
  for adj_tile in tile:circle_iterate(1) do
    if adj_tile.id ~= tile.id then
      local adj_terr = adj_tile.terrain
      local adj_name = adj_terr:rule_name()
      if adj_name ~= terrain_name then
        return false
      end
    end
  end
  return true
end

-- Add random labels to the map.
function place_map_labels()
  local rivers = 0
  local deeps = 0
  local oceans = 0
  local lakes = 0
  local swamps = 0
  local glaciers = 0
  local tundras = 0
  local deserts = 0
  local plains = 0
  local grasslands = 0
  local jungles = 0
  local forests = 0
  local hills = 0
  local mountains = 0

  local selected_river = 0
  local selected_deep = 0
  local selected_ocean = 0
  local selected_lake = 0
  local selected_swamp = 0
  local selected_glacier = 0
  local selected_tundra = 0
  local selected_desert = 0
  local selected_plain = 0
  local selected_grassland = 0
  local selected_jungle = 0
  local selected_forest = 0
  local selected_hill = 0
  local selected_mountain = 0

  -- Count the tiles that has a terrain type that may get a label.
  for place in whole_map_iterate() do
    local terr = place.terrain
    local tname = terr:rule_name()

    if place:has_extra("River") then
      rivers = rivers + 1
    elseif tname == "Deep Ocean" then
      deeps = deeps + 1
    elseif tname == "Ocean" then
      oceans = oceans + 1
    elseif tname == "Lake" then
      lakes = lakes + 1
    elseif tname == "Swamp" then
      swamps = swamps + 1
    elseif tname == "Glacier" then
      glaciers = glaciers + 1
    elseif tname == "Tundra" then
      tundras = tundras + 1
    elseif tname == "Desert" then
      deserts = deserts + 1
    elseif tname == "Plains" then
      plains = plains + 1
    elseif tname == "Grassland" then
      grasslands = grasslands + 1
    elseif tname == "Jungle" then
      jungles = jungles + 1
    elseif tname == "Forest" then
      forests = forests + 1
    elseif tname == "Hills" then
      hills = hills + 1
    elseif tname == "Mountains" then
      mountains = mountains + 1
    end
  end

  -- Decide if a label should be included and, in case it should, where.
    if random(1, 100) <= rivers then
      selected_river = random(1, rivers)
    end
    if random(1, 100) <= deeps then
      selected_deep = random(1, deeps)
    end
    if random(1, 100) <= oceans then
      selected_ocean = random(1, oceans)
    end
    if random(1, 100) <= lakes then
      selected_lake = random(1, lakes)
    end
    if random(1, 100) <= swamps then
      selected_swamp = random(1, swamps)
    end
    if random(1, 100) <= glaciers then
      selected_glacier = random(1, glaciers)
    end
    if random(1, 100) <= tundras then
      selected_tundra = random(1, tundras)
    end
    if random(1, 100) <= deserts then
      selected_desert = random(1, deserts)
    end
    if random(1, 100) <= plains then
      selected_plain = random(1, plains)
    end
    if random(1, 100) <= grasslands then
      selected_grassland = random(1, grasslands)
    end
    if random(1, 100) <= jungles then
      selected_jungle = random(1, jungles)
    end
    if random(1, 100) <= forests then
      selected_forest = random(1, forests)
    end
    if random(1, 100) <= hills then
      selected_hill = random(1, hills)
    end
    if random(1, 100) <= mountains then
      selected_mountain = random(1, mountains)
    end

  -- Place the included labels at the location determined above.
  for place in whole_map_iterate() do
    local terr = place.terrain
    local tname = terr:rule_name()

    if place:has_extra("River") then
      selected_river = selected_river - 1
      if selected_river == 0 then
        if tname == "Hills" then
          place:set_label(_("Varkaankuru"))
        elseif tname == "Mountains" then
          place:set_label(_("Rautahammas"))
        elseif tname == "Tundra" then
          place:set_label(_("Kaukainen Tundra"))
        elseif random(1, 100) <= 50 then
          place:set_label(_("Koskinen"))
        else
          place:set_label(_("Kaljakuru"))
        end
      end
    elseif tname == "Deep Ocean" then
      selected_deep = selected_deep - 1
      if selected_deep == 0 then
        if random(1, 100) <= 50 then
          place:set_label(_("Vetehinen"))
        else
          place:set_label(_("Vesimaa"))
        end
      end
    elseif tname == "Ocean" then
      selected_ocean = selected_ocean - 1
      if selected_ocean == 0 then
        if surrounded_by(place, "Ocean") then
          place:set_label(_("Riuttapaikka"))
        elseif adjacent_to(place, "Deep Ocean") then
          place:set_label(_("Pohjanne"))
        else
          -- Coast
          place:set_label(_("Isostelija"))
        end
      end
    elseif tname == "Lake" then
      selected_lake = selected_lake - 1
      if selected_lake == 0 then
        if surrounded_by(place, "Lake") then
          place:set_label(_("Suursaimaa"))
        elseif not adjacent_to(place, "Lake") then
          -- Isolated
          place:set_label(_("Umpilampi"))
        else
          place:set_label(_("Kalakko"))
        end
      end
    elseif tname == "Swamp" then
      selected_swamp = selected_swamp - 1
      if selected_swamp == 0 then
        if not adjacent_to(place, "Swamp") then
          place:set_label(_("Teuravuoma"))
        elseif adjacent_to(place, "Ocean") then
          place:set_label(_("Lehtovaara"))
        else
          place:set_label(_("Ojanpohja"))
        end
      end
    elseif tname == "Glacier" then
      selected_glacier = selected_glacier - 1
      if selected_glacier == 0 then
        if surrounded_by(place, "Glacier") then
          place:set_label(_("Kohmelo"))
        elseif not adjacent_to(place, "Glacier") then
          place:set_label(_("Umpivesi"))
        elseif adjacent_to(place, "Ocean") then
          place:set_label(_("Laajalahti"))
        else
          place:set_label(_("Railopaikka"))
        end
      end
    elseif tname == "Tundra" then
      selected_tundra = selected_tundra - 1
      if selected_tundra == 0 then
          place:set_label(_("Kolo"))
      end
    elseif tname == "Desert" then
      selected_desert = selected_desert - 1
      if selected_desert == 0 then
        if surrounded_by(place, "Desert") then
          place:set_label(_("Yyteri"))
        elseif not adjacent_to(place, "Desert") then
          place:set_label(_("Speden Hiekkakuoppa"))
        elseif random(1, 100) <= 50 then
          place:set_label(_("7 Velikultaa"))
        else
          place:set_label(_("Soramonttujen Soramonttu"))
        end
      end
    elseif tname == "Plains" then
      selected_plain = selected_plain - 1
      if selected_plain == 0 then
        if adjacent_to(place, "Ocean") then
          place:set_label(_("Pitkulainen Yyteri"))
        elseif random(1, 100) <= 50 then
          place:set_label(_("Mudakko"))
        else
          place:set_label(_("Paasivaara"))
        end
      end
    elseif tname == "Grassland" then
      selected_grassland = selected_grassland - 1
      if selected_grassland == 0 then
        if adjacent_to(place, "Ocean") then
          place:set_label(_("Marmorimaa"))
        elseif random(1, 100) <= 50 then
          place:set_label(_("Kalavalan Temppeli"))
        else
          place:set_label(_("Pirunpelto"))
        end
      end
    elseif tname == "Jungle" then
      selected_jungle = selected_jungle - 1
      if selected_jungle == 0 then
        if surrounded_by(place, "Jungle") then
          place:set_label(_("Tropiikkimaa"))
        elseif adjacent_to(place, "Ocean") then
          place:set_label(_("Maanalainen Joki"))
        else
          place:set_label(_("Suppa"))
        end
      end
    elseif tname == "Forest" then
      selected_forest = selected_forest - 1
      if selected_forest == 0 then
        if adjacent_to(place, "Mountains") then
          place:set_label(_("Lumottu Kivikko"))
        elseif random(1, 100) <= 50 then
          place:set_label(_("Varttihehtaarin Puisto"))
        else
          place:set_label(_("Sellupuisto"))
        end
      end
    elseif tname == "Hills" then
      selected_hill = selected_hill - 1
      if selected_hill == 0 then
        if not adjacent_to(place, "Hills") then
          if adjacent_to(place, "Mountains") then
            place:set_label(_("Suuri Vuoristo"))
          else
            place:set_label(_("Korkean Paikan Kammo"))
          end
        elseif random(1, 100) <= 50 then
          place:set_label(_("Ihmeiden Ihme"))
        else
          place:set_label(_("Nukkelaakso"))
        end
      end
    elseif tname == "Mountains" then
      selected_mountain = selected_mountain - 1
      if selected_mountain == 0 then
        if surrounded_by(place, "Mountains") then
          place:set_label(_("Paikoista Korkein"))
        elseif not adjacent_to(place, "Mountains") then
          place:set_label(_("Amigan Vuori"))
        elseif adjacent_to(place, "Ocean") then
          place:set_label(_("Kivikko"))
        elseif random(1, 100) <= 50 then
          place:set_label(_("Tarmo Mannin Temppeli"))
        else
          place:set_label(_("Puukkojunkkarien Muistomerkki"))
        end
      end
    end
  end
  return false
end

signal.connect("map_generated", "place_map_labels")
