# Tranzit — Art Direction

> **Status:** focused living visual specification. Confirmed decisions are authoritative for the game's presentation unless a higher-level gameplay rule requires otherwise.
>
> **Relationship to other documents:** [GAME_DESIGN.md](GAME_DESIGN.md) owns the high-level model-world/stylized-realism requirement and world mechanics. This document expands the visual execution of that direction. [UI_UX_DESIGN.md](UI_UX_DESIGN.md) owns interaction and interface behaviour. [V1_CONTENT_MANIFEST.md](V1_CONTENT_MANIFEST.md) owns minimum content counts and authoring targets.
>
> The goal is not photorealism or maximum polygon density. Tranzit should look convincing because the world is compositionally coherent, physically readable, atmospherically lit and visibly alive.

## 1. Core visual thesis

The target is **atmospheric simple realism** with a strong miniature/model-world presentation.

The visual position sits broadly between the readability and pleasant model-world presentation of a transport-building game and the heavier, more functional industrial credibility of a detailed logistics/economy simulation. Tranzit should be less dependent on tiny geometric detail than either extreme.

Key principles:

- believable real-world proportions and construction logic;
- selective simplification instead of low-poly caricature;
- slightly softened/stylized materials rather than photoreal surfaces;
- strong silhouettes and roof shapes;
- Central-European urban and industrial identity;
- lighting, atmosphere, weather and seasonal change as primary image-quality drivers;
- enough local life that a close view feels like looking at a functioning miniature world;
- no visual detail that materially harms strategic readability.

The world should be attractive in good weather without becoming toy-like or oversaturated. Industrial and older areas may feel dirty, worn and functional without making the whole game visually grey.

## 2. Camera, scale and miniature presentation

The game uses a 3D top-down strategy camera with:

- free horizontal rotation;
- a relatively broad pitch/tilt range;
- no first-person requirement;
- no requirement to descend to literal street or eye level;
- a close zoom that can approach the world from roughly above-rooftop height, so vehicles, roofs, yards, stations and street life can be appreciated as a miniature scene.

The camera should support both strategic overview and attractive close observation. Close assets therefore need to remain convincing from above and at an oblique angle, but do not need FPS-grade surface detail.

Use **slight visual scale exaggeration only where necessary for readability**. Vehicles, tracks, road furniture and other operationally important forms may be subtly enlarged or their characteristic features strengthened relative to the landscape.

The miniature/model-world feeling must come primarily from the elevated oblique camera, composition, lighting and the ability to observe a whole functioning scene at once. **Do not push proportions, depth of field, material treatment or asset simplification into an overt toy/model-railway aesthetic.** The intended world remains substantially realistic in scale and appearance.

Roofs and upper silhouettes are especially important because they remain visible in the closest normal camera.

## 3. Geometry and detail budget

Use a **simple-realism asset rule**:

> Model geometry that changes silhouette, volume, function or spatial reading. Use materials/textures for most small surface detail.

### 3.1 Ordinary buildings

Ordinary buildings should use real geometry for elements such as:

- roof form and roof height;
- chimneys;
- dormers;
- major balconies;
- bay windows and prominent projections;
- strong cornices or parapets where they materially shape the silhouette;
- entrances and large openings;
- rear wings and significant annexes;
- visible courtyards, sheds and outbuildings where relevant.

Prefer materials, normal maps or other inexpensive surface treatment for details such as:

- ordinary window-frame subdivisions;
- masonry joints;
- tiny ornament;
- small cracks and plaster texture;
- minor pipes, fittings and hardware.

Do not turn an ordinary residential building into a hero asset by modelling every decorative element. The visual budget is better spent on block composition, roof variation, believable spacing and environmental life.

### 3.2 Landmarks and special buildings

Historically important landmarks, major stations, distinctive factories, civic buildings and other visually unique anchors may receive higher geometric detail.

Major existing cities should include recognizable real landmarks where practical. As cities develop over decades, later economic centres may also gain period-appropriate new visual anchors such as civic, commercial, industrial, transport or cultural buildings. A landmark is normally a consequence of development, not an automatic centre-spawn token.

### 3.3 Industrial sites

Industrial facilities must be readable by function before the player opens a UI panel. Prioritize:

- overall massing;
- hall and shed forms;
- chimneys;
- tanks, silos and storage forms;
- loading areas and ramps;
- rail/road access;
- yards;
- cranes and other large handling equipment where relevant.

Tiny mechanical components are secondary unless they materially define the facility type.

## 4. Cities, economic centres, streets and blocks

### 4.1 Economic centre means the simulation object

An **economic centre** is the existing simulation unit defined in GAME_DESIGN Sections 6.2 and 10.5. It is not merely a visual downtown point.

A city/locality can contain several economic centres, including residential, commercial, industrial, station/freight and later suburban centres. The current balancing target keeps an ordinary centre compact enough for the whole-centre walk-access abstraction, with the 800 m target / 1,000 m split-review rules owned by V1_CONTENT_MANIFEST.

Visually, one economic centre can contain **many streets and many blocks**. A rough result such as 10–30 streets in a developed centre is plausible, but **street count is never a formation rule**. Dense historical areas may contain many short streets, while an industrial centre of similar physical span may contain only a few large access roads.

Economic-centre boundaries must follow the physical and sustained urban structure. Do not generate a circular 800 m visual bubble and then fill it with streets.

### 4.2 Organic Central-European street structure

Cities must not default to clean rectangular grids.

Street networks should react to:

- historical through-routes;
- terrain and slope;
- rivers and crossings;
- railways and stations;
- industry;
- earlier settlement;
- parcel boundaries;
- later planned development;
- period-specific planning styles.

A historic centre, nineteenth-century expansion, interwar district, industrial quarter, socialist housing estate and modern suburb should not share one street-generation pattern.

### 4.3 Block and parcel filling

Roads and streets create irregular polygonal blocks. Development should then fill the **actual block shape**, rather than placing independent rectangular buildings at fixed intervals.

The visual/world-generation hierarchy is:

> street network → irregular block polygons → parcel/access logic → buildings and usable open space

Parcels should normally face or access a street. Their shapes and sizes can vary. Awkward remnants do not need to be force-filled with a building; they may become:

- gardens;
- courtyards;
- passages;
- small squares;
- yards;
- sheds;
- workshops;
- landscaped gaps;
- later parking;
- industrial service space;
- undeveloped plots.

The objective is a believable European block fabric, not perfect parcel optimization.

### 4.4 Growth over time

An existing economic centre may physically grow while space and activity allow. Growth can:

- extend streets;
- add secondary streets;
- fill previously open blocks;
- densify existing blocks;
- replace some older structures with larger ones;
- change land use;
- accumulate new local landmarks.

As the actual simulation creates/splits new economic centres, urban growth may connect them visually into one continuous city. The player may see one continuous built-up area even though several economic centres remain distinct passenger-access and activity units.

The art system must therefore support **incremental urban growth**, not only whole prebuilt city snapshots.

## 5. Historical vehicle visual language

Vehicles are based on real historical technology but use fictionalized player-facing manufacturers/models under the existing vehicle-content rules.

Visual treatment:

- preserve the main recognizable construction and silhouette of the historical inspiration;
- keep defining proportions, wheel arrangement/body form, cab/window language and other major cues;
- do not require exact museum-grade reproduction of every fitting;
- simplify tiny mechanical detail that is not readable from the supported camera;
- allow fictional variants that use the same technical family/base while visibly differing in equipment, body treatment or period-appropriate design details;
- body repaint alone is not a distinct functional model.

A player should recognize the type and era from shape before reading its name.

## 6. Lighting and atmosphere

Lighting and atmosphere are primary quality features, not polish added after asset production.

### 6.1 General lighting

Use:

- natural but slightly restrained colour;
- warmer direct sunlight where appropriate;
- somewhat cooler skylight/shadows;
- clear directional shadows;
- enough ambient fill that shadowed infrastructure remains readable;
- atmospheric distance/haze;
- restrained post-processing;
- no mandatory heavy depth-of-field that obscures operations.

Do not force one mood onto every condition. A bright summer afternoon can be pleasant and warm; a wet November day can be cold, grey and low-contrast.

### 6.2 Day/night cycle

Run a full visual day/night cycle tied to the shared game clock.

The world transitions through morning, day, evening, night and dawn. The deepest-darkness period should be **short, approximately one game hour as an initial art target**, and remains tunable for readability.

A black or near-black night sky is acceptable. The world itself must remain readable through:

- moonlight;
- skylight/ambient night illumination;
- historically appropriate artificial lighting;
- vehicle lights;
- station and industrial lighting;
- readable material response and silhouettes.

Night must never turn normal construction and operation into a visibility test.

Artificial-light density and technology should evolve historically. A 1900 town can have genuinely dark outskirts and sparse warm lamps; later cities become much more extensively illuminated.

## 7. Weather and seasons

Weather should **materially transform the appearance of the world**, not merely add a screen-space particle effect.

### 7.1 Rain and wet conditions

Rain may affect:

- surface darkness;
- wet roads and roofs;
- puddles or localized standing water where technically appropriate;
- reflections/highlights without turning everything into a mirror;
- atmospheric visibility;
- mist/haze;
- rain visibility in lamps and headlights;
- ground/mud appearance.

### 7.2 Snow and winter

Snow may visibly accumulate on:

- ground;
- roofs;
- fields;
- vegetation;
- infrastructure surfaces where appropriate.

Traffic, maintenance and clearing can create visually different travelled/cleared surfaces where feasible. Snowfall can become visually heavy while preserving operational readability.

### 7.3 Seasonal change

Seasonal transition should be gradual, not an instant palette swap.

Target seasonal identities:

- **spring:** fresh lighter vegetation, wetter ground and transitional conditions;
- **summer:** fuller vegetation, stronger sun, mature/dry field states and long daylight;
- **autumn:** harvested fields, yellow/brown vegetation, rain and fog potential;
- **winter:** bare deciduous trees, reduced vegetation colour, short daylight and snow when weather supports it.

Seasonal state must remain geographically/climatically believable rather than making every region change identically on the same frame.

## 8. Vegetation, landscape detail and environmental props

Vegetation uses **realistic placement and density with simplified/stylized individual assets**.

Forests should have:

- irregular edges;
- varied tree heights;
- species/age variation where useful;
- occasional clearings and density variation;
- no visible placement grid.

Fields should be visually defined by their shape, crop/ground state, cultivation direction and seasonal appearance rather than by rendering every plant.

### 8.1 Environmental life through props

Use small environmental props to make close views feel lived-in without inflating the base-building mesh budget.

Period- and context-appropriate examples include:

- fences and gates;
- wells;
- benches;
- street lamps;
- utility/telephone poles;
- sheds and small shelters;
- barrels, crates, timber stacks and later pallets;
- coal/aggregate piles;
- signs and street furniture;
- parked carts/vehicles;
- garden elements;
- small service structures;
- appropriate advertisements/posters where legible and historically suitable.

Props should reinforce the place, period and function. Do not scatter decorative clutter uniformly across the map.

## 9. Visible life and activity

Target **medium-to-high visible life** at close zoom without requiring full persistent person simulation.

Representative visual activity may include:

- pedestrians where useful;
- workers around stations, yards and industry;
- period-appropriate carts, horses and road traffic;
- smoke/steam from active facilities and traction;
- loading/service activity;
- platform activity;
- local movement and idle behaviour.

The visual layer can use simulation LOD and representative agents as long as it does not contradict the actual operating state. A visually busy facility must not imply production or loading that the simulation says is inactive.

Human characters can remain stylized/simple enough for the miniature presentation; exact character-detail rules remain open.

## 10. UI visual character

The already-confirmed interface remains a **restrained contemporary dark UI**.

Its visual personality should sit between:

- neutral modern management software;
- subtle technical/industrial/transport references.

Use technical character through typography, iconography, line/diagram language, boards and small visual cues rather than through heavy railway ornament. Do not make the main UI a historical skin that must be rebuilt every decade.

Historical character primarily comes from the world, vehicles, news/documents and specialist surfaces such as the station board.

Exact palette, font family, spacing and design tokens remain implementation-level visual work unless later testing reveals a product-level decision.

## 11. Production priorities

When time, performance or asset budget forces a choice, prefer in this order:

1. correct physical form and functional readability;
2. strong silhouette and roofscape;
3. believable city/block/industrial composition;
4. lighting and shadows;
5. weather, seasons and atmosphere;
6. material quality and variation;
7. environmental props and visible life;
8. microgeometry visible only at unusually close inspection.

This is not permission to use debug primitives as final art. It is a rule for spending detail where the supported camera actually benefits.

## 12. Terrain and rural landscape

### 12.1 Landscape structure

The countryside should not read as a generic green terrain surface with isolated objects placed on top.

Roads, tracks, paths, watercourses, settlement edges, forest boundaries and other durable physical features divide the landscape into **irregular land-use polygons**. Those polygons can become fields, meadows, pasture, orchards, vineyards, woodland, gardens, wetlands, bare/working ground or other regionally and historically appropriate uses.

Use the same spatial principle as urban blocks:

> physical boundaries → irregular land polygon → land use → visual treatment

Avoid arbitrary rectangular field decals or a visible global placement grid.

### 12.2 Fields and rural parcels

Fields follow their actual polygon shape. Cultivation direction, crop rows, mowing/orchard pattern and other surface cues should respond to the parcel geometry rather than ignoring it.

Do not model every plant. Field identity should come mainly from:

- polygon shape;
- crop/ground colour;
- cultivation direction;
- surface/height variation;
- edge treatment;
- vehicle/work traces;
- seasonal state.

At close zoom, inexpensive spatial vegetation/detail layers may prevent fields from looking completely flat.

Use **hedges, field margins, ditches, tree lines, remnant vegetation, fences and farm tracks** where appropriate. These edge elements are important to the Central-European landscape identity and should not be replaced by perfectly clean parcel seams.

### 12.3 Historical evolution of land structure

Rural land structure may change over decades as the simulated economy, settlement and historical development change.

The visual/world system must be able to support:

- parcel subdivision or consolidation;
- removal or creation of some field boundaries;
- changing farm tracks;
- orchards or other land uses appearing/disappearing;
- urban expansion consuming rural parcels;
- changes in field scale and landscape openness between eras/regions.

This should make a 1900 landscape visibly capable of becoming different by the late twentieth/early twenty-first century. Do not implement it as one global year-triggered cosmetic swap; it should follow the actual authored/simulated land development rules.

### 12.4 Forests

Vegetation placement should be realistic in density while individual tree assets remain simplified/stylized enough for performance and the supported camera.

Forests should have:

- irregular edges;
- varied height and density;
- species/age variation where useful;
- occasional clearings;
- transitional edge vegetation;
- no visible placement grid.

Do not normally cut forest against open ground with one perfectly sharp line. Use scattered trees, scrub, margins or other transition where the geography and land use support it.

### 12.5 Terrain relief

The world uses real geography. Preserve believable real relief rather than globally exaggerating mountain/valley height for spectacle.

Terrain source data may be cleaned/smoothed to remove inappropriate noise and modern surface artefacts, but major and medium-scale geographic forms must remain recognizable. Use lighting, atmosphere and material variation to emphasize relief instead of distorting it.

### 12.6 Rivers and water

Rivers are physical landscape features, not blue spline lines.

They should support:

- believable varying width;
- irregular banks;
- bank vegetation;
- shallower edge treatment;
- sky/light reflection;
- subtle flow cues;
- gravel/sand/working banks where appropriate;
- floodplain, side-arm or wetland character where geographically justified.

Water rendering should prioritize visual quality and readability over expensive fluid simulation. A river should visibly shape the surrounding landscape rather than appear cut into an otherwise unchanged ground material.

## 13. Roads, railways and infrastructure ageing

### 13.1 Roads and paths

Roads and paths must read as physical infrastructure embedded in the terrain rather than a flat texture spline.

Depending on route class, era and terrain, road construction may visibly include:

- cut-and-fill earthworks;
- shallow embankments and cuttings;
- drainage ditches;
- shoulders/verges;
- culverts;
- retaining walls;
- bridges;
- curbs, sidewalks and later-era roadside engineering.

Road visual classes evolve historically. A 1900 network can include field tracks, unpaved roads, gravel/macadam roads, paved urban streets and better main routes; later eras add asphalt/concrete surfaces, broader carriageways, markings, barriers, lighting and period-appropriate junction treatment.

Upgrading a road should normally preserve its historical alignment unless the player/world actually rebuilds or reroutes it.

Roadside detail is contextual rather than uniformly scattered. Period- and place-appropriate elements may include tree lines, fences/gates, wells, shrines/crosses, drainage, utility/telegraph poles, grass verges and field access tracks.

### 13.2 Railway permanent way

Railways receive a higher functional-detail priority because they are a primary visual subject.

At close supported zoom, railway infrastructure should visibly include:

- two actual rails;
- sleepers/ties;
- ballast;
- geometrically correct turnouts/switches;
- crossings and junction geometry;
- signals;
- period-appropriate lineside poles/wiring/telegraph/electrification equipment;
- larger technical cabinets/markers where useful;
- drainage, embankments and cuttings.

Do not spend geometry on every fastening bolt. Preserve the parts that define railway function and silhouette.

Turnouts and crossings must visually correspond to the actual track graph. Do not render disconnected spline overlaps that trains magically traverse.

Rail corridors may include context-appropriate vegetation, fences, drainage, service paths and technical equipment. Main lines can look more maintained than lightly used sidings or industrial branches.

### 13.3 Visual ageing and maintenance state

Infrastructure should **visually age gradually** without becoming a binary pristine/ruined system.

Ageing cues may include:

- fading/discolouration;
- dirt and soot;
- weathering;
- ballast colour and contamination;
- sleeper wear;
- road-surface patching/fading;
- vegetation encroachment at edges;
- small maintenance repairs;
- patina on structures and buildings.

The intensity should depend on age, environment, infrastructure type and actual maintenance state where that information exists.

Major maintenance, renewal or reconstruction may visibly restore or replace affected surfaces/components. This does not require every maintenance action to swap the entire asset.

Visual condition is an **orientation cue**, never the authoritative technical-state UI. The rendering must not imply a precise failure probability or maintenance threshold that the simulation has not actually reached.

## 14. Bridges, tunnels, earthworks and construction presentation

### 14.1 Earthworks

Road and railway construction must visibly reshape the terrain where required instead of making the route simply follow every terrain undulation.

Supported visual forms include:

- cuttings;
- embankments;
- retaining walls;
- drainage;
- culverts;
- exposed soil/rock;
- reworked slopes;
- access/service tracks where appropriate.

Railways should generally show this more strongly than ordinary roads because route geometry and gradient constraints are stricter.

Earthwork slopes should receive context-appropriate material and vegetation treatment rather than appearing as a bare terrain deformation with no visual transition.

### 14.2 Bridges and viaducts

Bridges should be assembled from a structural family appropriate to era, span, height, load and transport mode rather than stretching one universal prefab to any distance.

A bridge/viaduct may visually compose:

> abutment/portal → span → pier → span → … → abutment

Representative families include:

- masonry/stone arches;
- steel trusses;
- steel girder spans;
- masonry viaducts;
- later reinforced/prestressed concrete;
- later modern steel/concrete forms.

Small drainage or ditch crossings should use culverts/small structures rather than dramatic bridge assets.

Important real historical bridges may be authored as unique landmark assets where appropriate. Player-built infrastructure normally uses modular families that still produce different results through span count, pier height, terrain and alignment.

### 14.3 Tunnels

A tunnel remains a real physical route segment.

Vehicles enter through a portal, continue along the actual underground alignment with its real length/curve/gradient, and leave through another portal. It is never a teleport shortcut.

Surface presentation may include:

- portal;
- approach cutting;
- retaining structures;
- drainage;
- service/technical structures;
- construction access;
- spoil/working areas where relevant.

Tunnel interiors do not need FPS-grade detail for the normal camera.

### 14.4 Visible construction progression

Major construction should progress through visible physical stages rather than changing from ghost to finished asset after a timer.

Representative rail/road stages include:

1. **preparation** — cleared/marked corridor, temporary access and material staging;
2. **earthworks** — excavation, fills, cuttings and embankments;
3. **substructure** — drainage, retaining works, bridge foundations/piers and prepared formation;
4. **track/road structure** — sleepers/rails/ballast or road layers/surface;
5. **completion** — signalling, fencing, roadside/lineside equipment, final landscape treatment.

Different sections of one project may visibly sit at different stages so construction reads as physically progressing through the world.

Bridges should likewise expose a small number of readable phases such as foundations → piers/arches/supports → main structure/deck → completed route. Tunnel construction should visibly affect portal/work areas and associated spoil/access even if every metre of underground excavation is not rendered.

Use approximately **3–6 visually distinct stages** per major construction family where practical. The goal is readable progress, not construction-worker micromanagement.

### 14.5 Underground / cutaway view

The normal world view keeps terrain opaque. Vehicles entering a tunnel disappear below ground in the ordinary presentation, though a selected/followed underground vehicle may retain a restrained selection cue.

Provide a dedicated **underground/cutaway analysis mode** for tunnel and later underground-transit operation.

In that mode, relevant terrain becomes transparent, faded or sectioned enough to reveal:

- underground route geometry;
- vehicles;
- tunnel intersections;
- underground stations where applicable;
- construction state;
- other relevant subterranean infrastructure.

The cutaway is an analysis/presentation mode only. It does not alter the physical route, simulation, travel time or visibility/knowledge rules.

## 15. Regional and historical architecture

### 15.1 Authoring scope

The world uses real geography and real settlement locations where supported by the authored world data, but **not every town or village is individually hand-modelled**.

Authoring effort should be concentrated on:

- major cities;
- nationally/regionally important settlements;
- distinctive transport/industrial locations;
- major historical landmarks;
- iconic stations, bridges, factories or civic buildings where their identity materially improves the world.

Smaller towns and villages normally use regional/historical procedural or rule-based assembly from reusable kits. Their placement, broad scale, terrain relationship and important through-routes should remain geographically plausible, but ordinary buildings do not need one-to-one historical reconstruction.

### 15.2 Architectural identity

Building appearance should derive from a combination such as:

> function × construction era × region × density × economic level × age/condition

Do not use one national skin per country. Regional architectural identity should emerge through combinations of:

- roof forms;
- materials;
- facade proportions;
- building width/height;
- street relationship;
- rural farm/yard form;
- industrial construction;
- civic/transport architecture;
- colour/material tendencies.

Neighbouring industrial regions may resemble each other more than distant regions inside the same modern country.

### 15.3 Historical layering

Cities should accumulate architecture over time rather than switching to a new era skin.

Representative broad visual eras include:

- **pre-1918 / around 1900:** historic blocks, tenements, row houses, farmsteads, brick industry, period stations and ornamented civic buildings;
- **1918–1945:** continuation of traditional fabric plus modernism/functionalism, expanding suburbs and newer civic/industrial forms;
- **1945–1990:** older fabric remains, while panel/prefabricated housing, larger industrial complexes, cultural/commercial centres and wider infrastructure appear;
- **1990+**: suburban expansion, logistics/retail, modern offices/housing, brownfield redevelopment and restoration of older fabric.

These are visual trends, not hard date unlocks.

### 15.4 Growth, replacement and preservation

Ordinary urban buildings may be replaced, extended, repurposed or densified over time where the city-development simulation supports it.

Possible long-term outcomes include:

- retained building;
- renovation/restoration;
- change of use;
- extension/rear-wing addition;
- replacement by denser/newer development;
- decline;
- protected preservation.

**Most of a historic urban core should remain protected from ordinary redevelopment.** Historic centres should preserve a strong majority of their characteristic street fabric and older buildings over long campaigns.

Protection is stronger for:

- major landmarks;
- heritage/civic/religious buildings;
- highly characteristic historic blocks;
- nationally or locally important structures.

Replacement pressure should therefore occur more strongly in peripheral, transitional, industrial/brownfield and later-developed areas than in the protected historic core.

The protection rule preserves historical identity without freezing the entire city. Non-protected buildings inside or near an old centre can still change where plausible.

### 15.5 Villages and small towns

Small settlements should use organic Central-European structure rather than a clean grid.

Typical elements may include:

- development along historic roads;
- village greens/squares;
- farmsteads with yards and barns;
- gardens/orchards;
- wells;
- fences/gates;
- churches/chapels where appropriate;
- irregular side roads and field access.

A village may expand, merge into a larger built-up area or eventually be absorbed by urban growth. The visual system must support that transition without requiring a bespoke hand-authored model for each settlement.

## 16. Still to define

The following visual areas remain to be specified in this art-direction thread:

- regional rural landscape identities and exact field/crop palette;
- exact pedestrian/character style and animation density;
- detailed VFX language for smoke, steam, dust, mud and construction;
- final UI colour/type/icon tokens;
- LOD/asset technical budgets after the Unity rendering baseline is selected.
