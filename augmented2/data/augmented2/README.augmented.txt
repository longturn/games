=================================
Augmented2 Ruleset for Freeciv v2.6
=================================

WIKI PAGE:
----------

https://freeciv.fandom.com/wiki/Augmented2_ruleset_modpack

BUG TRACKING:
https://github.com/Wahazar/augmented2/issues
(please do not open tickets related with this modpack on freeciv bugtracker)

----------

OBJECTIVES:
-----------

- Larger time span, from neolithic up to future techs.

- Iso-hex topology, initial city radius 1 (6+1 workable tiles) expandable to 2 (Agriculture Farming) and later to 3

- Relatively fast expansion at the beginning (cheap Tribes) and less exponential growth later (progressive upkeep)

- Better balanced and more sophisticated technology tree, 62 new techs.
  Facultative advance paths based on Asiatic culture (Arab, Hindu, Chinese, Japonese) 
  - not required for mainstream technology path, but granting some extra units/buildings/wonders.

- Clearly distinctive tiers of military unit classes: 
  defensive infantry, assault infantry, fast assault units, reconnaissance, 
  direct fire artillery, plunging fire artillery, peacekeepers, turrets etc.

- Well defined tiers of ships classes: river/coastal merchants, river/coastal warships, ocean merchants, ocean warships. 

- Ships and armoured train have decreased attack alone, but can be equipped with turret guns (destroyer and patrol boat also torpedos). 
- Submarines can carry torpedos (nuclear submarine also missiles). 
- Bombers, strike aircrafts/advanced fighters can carry bombs (and torpedos). 

- Enginners can carry other unit.

- New buildings and wonders, adopted to the new technology tree. 
  Some industrial improvements give additional bonus from certain tiles.
  City radius depend on city size and improvements.

- Some building and especially wonders require certain level of Culture Points. These can be earned 
  each turn from some other buildings, or granted by special events.

- New governments and altered governments properties.

- Upkeep cost depend on unit type and tier.

- Smooth changes in upkeep system between different government systems.

- No additional income from caravan arrival and decreased income from traderoutes.

INFO:
-----

- Help texts have been updated, so the info showed ingame already takes into account the changed rules. 
  Note that some graphical tables from the Manual will not match (mainly Terrains and Governments), 
  so better use graphics from augmented2 wiki or the spreadsheet tables in /doc dir as reference.

- Help pages on freeciv wiki: https://freeciv.fandom.com/wiki/Augmented2_ruleset_modpack


CORE CHANGES:
-------------

- Every unit pays some kind of Upkeep cost, for example 1 food, 1 gold in case of medieval infantry, 
  or 1 shield, 1 food, 1 gold in case of gunpowder era infantry. 
  There is no abrupt change of upkeep system after revolution, each goverment pays all 3 upkeep prices, 
  however free upkeep threshold for shield and gold depend on government. Food upkeep is scalable with city size as usual.

- Units lose one Veteran level when auto-upgraded by Metallurgy tech, Leonardo Workshop or DARPA wonders.

- Movement bonus on Railroads apply only for Train, Merchant and Small Land units. 
  There is no movement bonus for Rivers except of Small Land and Merchant.

- Some key techs require no holes in its tech roots. To acquire a tech you must know its
  prerequisites, and you cannot lose a tech that another depends on (see colour of tech).

- Enabled risk of Plague at cities with population greater than 4. Chances
  reduced by the buildings Aqueduct/Water Treatment, Sewer System, Lazaretto/Hospital
  and the wonders: Pasteur Institute and Cure for Cancer.

FOODBOX:
--------

not changed yet

TERRAIN:
--------

- Transforming terrain from forest/to forest possible with Forestry tech.

- Dirt road or river is required to add shield to rough terrain such Hills, Forest, Jungle, Mountains or Taiga.

- Jungles receive +1 Shield (2/1/0) with Railroad on its tile and Railway Station in city. 
  Swamps can be irrigated for +1 Food (to 2/0/0), next irrigation convert them to grassland. 
  Tundras can be mined for +1 Shield (instead of irrigated)
  and receive +1 Trade when roaded (up to 1/1/1).

- Deserts with a river receive 1 extra Food from irrigation (total 2),
  unless they have an Oasis; this simulates a growth boost like Nile
  floods.

- Irrigation possible with Agriculture Farming tech, and can be performed if River or Lake is adjacent to tile, 
  or another irrigated tile is cardinally adjacent. Electricity allow to irrigate if Sea is cardinally adjacent, 
  and Recycling allow to irrigate without any restrictions.

- Mountains give extra vision range for small reconnaissance units. Cities can not be placed over
  Mountains. Regular military units can't go into unroaded mountains, except of spec-ops units.

- The discovery of Copper Mining allow mining, but without any effect on hills, Bronze Working allow production of mines.

- Mines+Railroads in mountains and deserts give extra Shield production, if Cement Plant and Railroad Station is builded in city. 
  Mines+Railroads on coal give extra trade point in above case. 

- Mines+Railroads on coal give extra Shield production, if Steel Plant and Railroad Station is builded in city. 
  Mines+Railroads on iron give extra trade point in above case. 

- Forest give extra Shield production, if Textille Mill is builded in city. 

- Mines on deserts give extra Shield production, if Manufacture is builded in city. 
- Mines on coal give extra gold production in above case, or if Coal Power and Railroad Station plant is builded in city. 

- The discovery of Refining allows to upgrade the mines placed on
  Deserts and Glaciers to Oil Wells (+2 Shields in total). Refinery gains additional gold from each Oil Well on Oil.

- Deep ocean tiles must be mined (resulting in an Oil Platform) in order to
  take advantage of the shield bonus from Offshore Platforms. Refinery in city is required.

- Pollution may appear in Ocean tiles, and Transports or Barges can clean it
  without the need of Workers/Engineers. Jungles and Forests are less
  affected by global warming.

- Environmentalism allow to make Wind Turbine on hills with irrigation.

- No minimum city output. City central tile simply gets  +1 Shield, and without mine, +1 Food 

- Tile transform is possible when Combustion tech is known (with some earlier exception for steam barge).

- Terrain transformation pattern -
see doc/terraintransform.png


DEFENSE:
--------

- Halved the terrain defense bonuses, now more similar to civ3 values:

TERRAIN                        
Forest, Swamp  	    	 +25%     
Hills, Jungle            +50%     
Mountains                +100%    

RIVER                    +25%     

VETERAN:
Recruit                  +25%     
Veteran                  +50%     
Hardened                 +75%     
Elite                    +100%    
Veteran Elite            +125%    

FORTIFIED                +50%     
(only military units can fortify; inside cities, they are
always considered fortified)

BASE             VS LAND  VS SEA   VS AIR   VS MISSILE/BOMB
Fort             +50%     +50%     +0%      +0%
Fortress         +100%    +100%    +50%     +50%
Airstrip         +0%      +0%      +50%     +50%
Airbase          +50%     +50%     +100%    +100%

CITY             VS LAND  VS SEA   VS AIR   VS MISSILE/BOMB
Ruins	  	 +25% for Small Land
Town (Pop<=8)    +50%     +0%      +0%      +0%
City (Pop>8)     +100%    +50%     +0%      +0%

Buildings each add:
Palisade         +50% (+50% against Horses)
Walls            +100%    +0%      +0%      +0%
Bunkers          +100%    +0%      +0%      +100%
Great Wall(W)    +50%     +0%      +0%      +0%
Coastal Defense  +0%      +100%    +0%      +0%
SAM Battery      +0%      +0%      +100%    +0%
SDI Defense      +0%      +0%      +0%      +100%/50%

- Every City of any size receives an inherent Defend_Bonus = +50%
  against all kinds of land units except of Train and Turrets.

- Every City with Pop>8 receives an additional free Defend_Bonus = +50%
  against land units.

- Walls effect not apply against plunging fire units. 

- Great Wall gives additional Defend_Bonus = +50% against Land units,
  and prevents population loss in any allied city when a defending unit loses.

Total Defense = (UNIT DEFENSE) * (100+TERRAIN)/100 * (100+RIVER)/100
 * (100+CITY+BASE)/100 * (100+FORTIFIED)/100 * (100+VETERAN)/100
(Same as classic rules).


GOVERNMENTS:
------------

1. 
All governments pay shield, food and gold upkeep, however upkeep free differ depending on government. 
For example Monarchy have 4 unit shield upkeep free, but only 3 units gold upkeep free, 
while First Republic only 1 unit shield  upkeep free, but 4 units gold upkeep free. 
Food upkeep depend only on city size (except of Communism, which offer more free food).

2. Neither government is immune on bribery or revolting (except of cities with Palace etc, or Fascism without Statue of Liberty). 
However cost of such actions depend on government, and sometimes on Wonders 
(for example, 200% for inciting revolt in case of Democracy without Slavery Abolition, 1000 % with)

3. There is no extra gold per tile in Democracy or Republic 
(unless Women's Suffrage wonder exists, wich gives such effect for Democracy, or extra shield for Republic).
But some governments have bonuses or penalties while producing gold, science or luxury.
For example science and gold is suppressed under Tribalism, while improved under Republic.

4. Additional unhappines is generated proportional to enemy nationality percentage in your city.
It can throw out Tribal, Democracy or Republic gov.

Gov. table reference:
see docs/gov.xls


TECHS:
------
Improved tech tree.
New techs:

* absolutism 
* advanced_rocketry
* agricultural_farming 
* alchemy 
* animal_husbandry 
* antimatter_propulsion 
* artificial_intelligence 
* astronomy 
* biology 
* biotechnology 
* buddhism 
* bushido 
* carpentry 
* chemical_synthesis 
* christianity 
* cinematography
* concrete 
* confucianism 
* copper working
* craft_guilds 
* creative_art 
* desert_code 
* direct_democracy 
* drama
* egalitarianism 
* electromagnetism 
* exploration 
* federation 
* fire_making 
* first_republic 
* forestry 
* fundamentalism 
* general_staff
* glass_working 
* great_unification_theory 
* hastilude
* hinduism 
* imperialism 
* islam 
* jainism
* jet_propulsion 
* leather tanning
* legalism 
* machinery 
* martial_games
* mass_entertainment
* modern_theatre
* modern_warfare 
* nanotechnology 
* offshore_exploration 
* overseas_trade 
* paper_making 
* pastoralism 
* printing_press 
* quantum_theory 
* radar 
* radioactivity 
* saddle_stirrup 
* sailing
* satellite_system 
* screw_propeller 
* shamanism
* shiism
* shinto 
* shogunate 
* sikhism 
* simple_machines 
* slave_trade 
* socialism 
* stone_knapping 
* sunnism
* super_soldiers 
* taoism 
* thalassocracy 
* theory_of_relativity 
* turbine 
* welding_technology
* vedism 
* zaibatsu 


BUILDINGS:
----------

Altered effects - 

Barrack:
Infantry Barracks -
Tier I: Recruits for Small Land, Veteran for Infantry units.
Tier II: Recruits for Small Land, Veteran for Infantry units (trade bonus if Saltpeter tile is workable in city)
Stable Barracks: Recruits for Light Cavalry, Veteran for Heavy Cavalry.
Workshop Barrack: Veteran for Light Cavalry, Wheeled Units, Big Land, Mech. Inf.

Harbour:
Deckhand level for Sea class (cumulative with Lighthouse), 25% faster HP regen for Sea and Coaster.

Supermarket: not required for farmland bonus/creation (second irrigation after Chemical Synthesis), 
instead of, increase granary size.
Add 25% gold city income if Railway Station or Port Facility is builded.

Colosseum: Small Wonder, increase luxury by 50% and make 1 military unhappy citizen content.
Amphitheatre: add 3 luxury points (only 2 with Cinematography) 
Theater add 2 luxury points (4 with Cinematography)

Bank, Stock Exchange: only Tax increase.
Marketplace: overall Trade increase.

Super Highways: 25% Trade increase with Stock Exchange.

New buildings:

Manufacture:
25% city production bonus and pollution, 
bonus trade points from coal mines, bonus shields points from desert mines, 
obsoleted by Corporation

Textille Mill
50% city production, 25% pollution, 
bonus shields points from forest and taiga, bonus trade points from silk, 
require river, 
obsoleted by Plastics

Steel Mill
100% city production bonus and 150% city pollution,
shield bonus from coal mines, trade bonus from iron mines, 
require Railway Station,
conflicting with Research Lab 

Cement Plant
50% city production bonus and 100% city pollution,
shield bonus from mountain or desert mines, trade bonus from coal mines, 
require Railway Station,
conflicting with Research Lab 

Railway Station
Necessary to gain additional bonuses from Railroad tiles. 
Default shield bonus from any railroad decreased to 25%, but railroad together with Railway Station 
yield additional output from some special resources or from mines (together with Steel Mill, Cement Plant or Coal Plant). 
Instant hp regen of train class units.
Increased city radius size with Eiffel Tower or Mass Transit.

Oil Refinery
100% tile production bonus from desert Oil Wells, trade points from Oil Wells on oil field,
required for Oil Shore Platform.

Lazaretto
plague probability 20% less

Hospital
plague probability 20% less (40% less with Pasteur Institure wonder)

Monk Monastery: add 4 science points to the city (and 1 unhappy citizen content, if player posses Buddha Statue).
Shrine Torii: cheap temple improvment (extra 1 unhappy citizen content).
Church: makes 2 unhappy citizens content (3 with J.S. Bach's Cathedral), required for Cathedral.
Mosque: makes 2 unhappy citizens content, additionally neutralizes unhappiness caused by one military unit (Kaaba required).

Note: Sacral building improvments, belonging to different faiths, doesn't mix 
(temple/church/mosque can't exists in same city)

CITY SIZE:
--------

Please note: required hexagon isometric topology.

Initial city workable square radius 1. 
Radius of workable area will grow with:
city size 2 (rect. topo.)
City Hall
Railway Station with
Eiffel Tower or Mass Transit

Initial city vision square radius 8.
City vision area will grow with:
city size 3 with Courthouse,
occupied city with City Walls
city with Watchtower
Airport or Eiffel Tower (with Electricity)

WONDERS:
--------

Altered:
Great Library obsololeted by Computers,
Map Reveal shifted from Apollo to GPS
Shakespeare's Theatre obsoleted by Television.
No pollution reduction form Eiffel Tower (it is used to increase town influence and vision radius)
Women Suffrage: additional trade point/tile in Democracy, or Shield point/tile in Republic. For unhapiness see: Hollywood.
Internet: do not reveal map (use GPS instead).
Great Wall: add defense also to fortress.

New:

Pasteur Institute
1 immediate tech and plague probability 20% less with Hospital 
(together with all water/sewage amenities and Hospital, total protection is 90%, with Cure Cancer, 100%)

Slavery Abolition
Increased min size not causing unhappiness under democracy, but penalty on rich tiles trade (gold gives 5, not 6). 
This small wonder is required for Women's Suffrage.

MIT
1 new tech, 4 bulbs for city, 50% for any research lab

Global Positioning System
Map revealed

LHC
2 new techs, convenient method to achieve Great Unification Theory, which is very expensive

Space lift
Required to make Spaceship Structurals

Hollywood:
Neutralizes the unhappiness caused by aggressively deployed military unit, like original Women Suffrage.
Unlike other wonders, Hollywood has expensive upkeep.

Marie Curie Mobile X-ray fleet
Faster heal of infantry units.

DARPA
Randomly upgrade unit. Small Land military units have Recruit rank (with Barrack, veteran). 
Prerequisite to Internet wonder.

Additional faith wonders:

Leshan Buddha Statue
Add +1 food for each river tile within city radius, neutralises 1 unhappy citizen for each city in the World with Monk Monastery.

Kaaba: Add extra gold from each road tile within city radius. Each Mosque neutralizes unhappiness caused by one military unit.

Angkor Wat: Act as second Palace (but can't be build if Player already have Ecclesiastical Palace or opposite), 
add 4 Luxury point to the city where is located.

Golden Temple: 
Make one more happy citizen for each Temple, Church or Mosque.

Western Wall: 50% defense for city (cumulative with City Walls, not cumulative with Great Wall),
gold bonus as for Colossus (extra trade from each tile generating trade).

Note: different faith wonders (above and Cathedrals or Crusade) doesn't mix 
(can't exists in same country, except of Golden Palace and Western Wall, which are ecumenic).

GREAT/SMALL WONDERS SUMMARY:
---------------------------


BONUS EFFECTS:

25% defense for Small Land class in Ruins
Increased unit vision benefit from Satellite System


UNITS:
------

Caravans and Carts are unique units. Freights, Slaves and freight ships are not unique. 

Following military unit groups:
* Infantry units - defensive or assault infantry - can't move into mountains (some units can attack it).
* fast assault units: LightCavalry - can't move into mountains/glaciers (some units can attack it), Heavy Cavalry - cant go also into Swamps.
* reconnaissance Small Land units (explorers, archers, snipers, peacemakers etc) - can move everywhere;
* direct fire artillery - movement restricted to roads and flat tiles (less restriction for self-propelled units), can't occupy towns, can attack non native tiles;
* plunging fire artillery - movement restricted to roads and flat tiles (less restriction for self-propelled units), ignore walls, bombardment action, can't occupy towns, can attack non native tiles;
* Big Land class - movement more restricted than for regular Land class, but less compared to Wheeled Units. Can't be loaded on some units.
* Turrets - can't move by itself (can reside in cities/forts/airstrips), can be boarded on Sea units/armoured trains, can attack from and at non native tiles;
* Sea class units: can go on Ocean tiles;
* Coaster class units: can go on Coast Ocean, River and Lake tiles;
* Air class units, Helicopters, Missiles: can go everywhere;
* Bombs, Torpedos - can be loaded on Air units (and some Sea units).
* Diplomatic actions and espionage: Messenger, Diplomat, Spy (and unique Corsair, Ninja, Navy Seals), also Explorers and Partisans (limited)

Units reference table: see doc/units.xls or refer to wiki page

TODO:
-----
Stonehenge as cheap small wonder - just +2 science added to city center
Shamanism: Black Monolith small wonder: +2 trade to city center, req for Kaaba.
Copper Working: some copper small wonder as fail safe for Colossus.
Seeker - initial unit for exploring
Polytheism: need Absolutism, not Agriculture
Monotheism: need Code of Laws, not Absolutism
Irrigation possible with Forestry, but works with Agricultural Farming
Add Senate bldg. Has senate govs req. Senate
Windmill: no gold cost
fresh city: some free granary for start
heavy cavalry: terrain defense


Author: Wahazar
