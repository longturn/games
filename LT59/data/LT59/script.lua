-- Freeciv - Copyright (C) 2007 - The Freeciv Project
--   This program is free software; you can redistribute it and/or modify
--   it under the terms of the GNU General Public License as published by
--   the Free Software Foundation; either version 2, or (at your option)
--   any later version.
--
--   This program is distributed in the hope that it will be useful,
--   but WITHOUT ANY WARRANTY; without even the implied warranty of
--   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
--   GNU General Public License for more details.

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

-- Kill triremes too far away from the coast
function kill_triremes(turn, year)
  local messages = {
    'The crew of your Trireme has rebelled due to low food supply',
    'Your Trireme was hit by scurvy: no survivors',
    'Your Trireme encountered heavy sea and was lost body and property',
    'Trireme lost to an attack by a giant squid',
    'No news from your Trireme: presumed lost',
  }
  for tile in whole_map_iterate() do
    if tile.terrain:class_name() == 'Oceanic' then
      -- can have a trireme there
      for unit in tile:units_iterate() do
        if unit.utype:rule_name() == 'Trireme' then
	  -- found one! Is the coast close enough?
	  local at_coast = false
	  for tile2 in tile:square_iterate(3) do
	    -- look up to 3 tiles away
            if tile2.terrain:class_name() ~= 'Oceanic' then
	      at_coast = true
              break
	    end
	  end
	  -- too far, sorry...
	  if not at_coast then
	    notify.event(player, tile, E.UNIT_LOST_MISC,
	                 messages[random(1, #messages)])
	    unit:kill('fuel')
	  end
        end
      end
    end
  end
  -- continue processing
  return false
end

signal.connect("turn_started", "kill_triremes")
