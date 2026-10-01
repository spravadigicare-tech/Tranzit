# Tranzit — V1 content and balancing manifest

Prepared: 2026-09-30. Status: required authoring targets; no assets or datasets are claimed to exist yet.

Read with [V1_SCOPE.md](V1_SCOPE.md), [V1_IMPLEMENTATION_BRIEF.md](V1_IMPLEMENTATION_BRIEF.md) and [GAME_DESIGN.md](GAME_DESIGN.md).

## 1. How to use this manifest

The approved requirements are in V1_SCOPE. Counts, proposed fictional catalogue IDs, budgets and performance workloads below are implementation defaults selected to make those requirements testable. They are not historical facts, exact user-approved balancing or an instruction to buy asset packs.

Create machine-readable manifests for vehicles, facilities, cargo, recipes, technology, tariffs, loans, regions and art. Keep stable IDs, schema versions, localization keys, source/provenance, applicability dates and content dependencies. Do not hardcode balancing inside UI or dispatch code.

A content row is complete only when its definition, physical asset/prefab, costs, compatibility, UI, save support and relevant test exist. A list of 100 vehicle names without models and supported operation does not satisfy the catalogue minimum. Recolours do not count as distinct functional models.

Initial numerical targets may be changed with a short recorded rationale and updated tests, but not by removing an approved mode, feature, territory or historical-progression mechanism. Missing critical content is a release blocker rather than an invisible default object.

## 2. World coverage and initial state

### Geographic coverage

The final V1 world covers the full territory corresponding to present-day Czechia and adjoining playable territory in Germany, Poland, Austria and Slovakia. The exact clipping polygon must be committed as data and documented before building the final world. This is a geographic coverage description, not a political map for 1900.

Initial authoring target: at least 60 named settlements, of which at least 40 are within the Czech coverage and at least 20 are distributed across the four adjoining countries' coverage. Every adjoining country has an accessible authored region and a useful route/market connection where geographically plausible. The terrain cannot consist only of narrow disconnected corridors between a few towns.

Include the major Czech urban/industrial hubs and useful surrounding smaller towns. Potential cross-border anchors include Dresden, Nuremberg, Vienna, Bratislava and Wroclaw; verify the final extent, positions and historical transport connections during authoring. These are coverage suggestions, not a claim that their historical routes have been researched in this handoff.

Every named settlement has a real sourced position, population/economic scale appropriate to the authored year, recognizable settlement footprint, local road access, relevant customers/services and commercial-coverage identity. Do not count 60 text labels on empty ground as 60 settlements.

Initial target: at least eight distinguishable economic/terrain regions inside the Czech coverage plus one in each adjoining coverage. Region boundaries are game operating units with sourced geographic anchors; do not present them as exact historical administrative borders unless verified.

### Active and macro state

A new game activates the selected starting area under the agreed rules. Other authored regions are available for later expansion, initially represented economically at macro level. Existing operators, import flows and pre-start history are initialized for 1900. Activating a region materializes that same evolving state once, not an untouched copy of the starting map.

At least three documented starting areas must support a legitimate small-road opening and a larger rail-capable opening using third-party infrastructure. Each selectable starting region must have a useful feasibility description rather than a silently impossible opening. If a region cannot support a selected loan tier, explain the constraint before confirmation.

### Existing physical economy

Initial target: at least 80 operating customer/supplier sites over the full authored world, distributed by settlement size and regional character. A small town does not need an implausible full industrial chain. Sites have real endpoints, inventories, production/consumption and supply relationships.

Provide public/third-party rail and roads, stations, appropriate workshops, manufacturers/dealers, construction contractors, commercial offices and operating facilities before the player arrives. Use scale-appropriate existing operators and fleets. Full-world assets do not all require detailed rendering at once.

The initial economy needs stocked inventories, qualified labour, supply sellers and contractor logistics sufficient to avoid bootstrap deadlocks. Those are explicit seeded world resources, not periodic free injections into the player's balance or warehouse.

## 3. Initial vehicle catalogue

All brands and model names are fictional. Research the plausibility of technology, dates, performance and appearance before finalizing. The IDs below identify roles, not exact approved real-world models.

### Available 1900 roles

| Family | Initial minimum | Required distinctions |
|---|---:|---|
| Steam locomotives | 4 | Small yard/tank engine; economical local mixed-service engine; passenger-oriented engine; freight-oriented engine |
| Freight rolling stock | 6 | Open bulk wagon; covered general cargo; flat/long-load wagon; liquid tank where plausible; insulated/refrigerated family appropriate to the date; heavy/large-load variant with real compatibility limits |
| Passenger rolling stock | 4 | Basic coach; higher-comfort/class coach; luggage/service function; longer-distance accommodation or another genuinely different period-appropriate passenger product |
| Road freight | 4 | Horse-drawn freight; small early motor vehicle; larger early motor or steam freight option; specialized body/load variant |
| Road passengers | 2 | Horse-drawn omnibus; period-plausible motor passenger vehicle |
| Service/recovery capacity | Functional coverage | Real assets/providers for yard work, towing/rescue, vehicle delivery and operating supplies; compatible existing roles can be reused instead of inventing unnecessary models |

This gives at least 20 distinguishable initial catalogue definitions. Each required body/load type needs compatible facilities and demand. Do not force new technologies into 1900 merely to hit a count; use a plausible variant or record why a role is introduced later while preserving a workable starting fleet.

Horse operations use aggregate animal traction, food/water/rest/service requirements and stable capacity. Do not implement breeding or persistent individual animal life simulation. Their visual models must include the vehicle and traction, not a motor-truck silhouette with a horse label.

### Progression after the starting year

The 1900-only preset is not a 1900-only technology catalogue. Supply a coherent successor sequence through interwar, mid-century, later-century and modern rail/road operation. At least one meaningful successor in each broad content stage must exist for rail freight traction, rail passenger service, road freight and buses. Definitions must have actual usable assets and required infrastructure, not future names without prefabs.

The sequence must exercise steam, electric and diesel rail operation; changing road propulsion/performance; improved passenger products; safer/higher-capacity signalling; workshop capabilities; communications/office centralization; and later logistics/information tools. Dates are authored and validated, not invented in core code. Not every region must receive every technology simultaneously.

At least two real progression steps must materially change each of: traction/service performance, infrastructure capacity, loading/maintenance capability and office/dispatch capability. A colour change or hidden income multiplier is not a progression step.

Keep a content coverage manifest identifying which date ranges have authored history, catalogues and economic assumptions. The calendar and free-play do not stop at the last event or in 2020. Do not claim an extensively authored modern world if only the 1900 set was delivered. Missing promised progression remains visible in the release status.

### Definition requirements

For every vehicle model define:

- introduction date, technology prerequisites, region applicability and fictional manufacturer;
- dimensions, empty mass, load/volume/positions or passenger capacity zones;
- traction/power, speed, acceleration/braking envelope and operating consumption;
- gauge/coupling/control, route/load/clearance and energy compatibility;
- physical facing, permitted reverse operations and consist-end position; run-around and actual turning are distinct capabilities;
- required staff/qualification and service/facility families; passenger through-circulation capability and any resulting aggregate ticketing dwell;
- purchase/manufacturing basis, order lead-time inputs, depreciation and operating costs;
- maintenance intervals, workshop requirements, parts/support family and retrofits;
- usable prefab/mesh, coupling and access anchors, visual LODs, materials, animation and sound references;
- source/plausibility notes and localization keys.

Do not add `available_until` as a hard purchase/operation gate. Physical dealer/used inventory and manufacturer offers remain finite and observable. A missing supplier is not the same as a retired technology definition.

## 4. Cargo, supply chains and passenger markets

### Cargo minimum

Initial target: at least 12 meaningful cargo/operating-supply definitions. Use historically appropriate packaging and technology. The 1900 food economy should use several concrete transportable commodities rather than one generic food item; baseline coverage includes **grain, flour/bakery products, meat, dairy products, and fruit/vegetables** where the regional economy supports them. Recommended wider functional coverage also includes coal, timber, processed wood, ore, metal/steel products, liquid fuel or other industrial liquids, manufactured goods and indivisible machinery. **Construction materials remain separate physical commodities rather than one generic building-material cargo family**, with baseline 1900 coverage for stone/gravel, bricks, cement, processed timber and steel products where regionally appropriate.

For the baseline 1900 heavy-industry chain, keep **coal** as the single player-facing solid-fuel/reductant commodity; do not add coke as a separate transport commodity. The chain can therefore use coal + iron ore → iron/steel production → metal products/machinery without a dedicated coke cargo entry.

This does **not** merge extraction sites. Resource industries remain distinct by deposit/resource and facility type: for example coal mine, iron-ore mine, stone/gravel quarry and other later resource-specific extraction sites. A generic universal `Mine` must not replace their different resources, geography, output commodities and operating characteristics.

Keep **iron and steel as separate player-facing commodities** in the 1900 industrial catalogue. Downstream recipes specify their actual material requirements independently: a firm/process may require iron, steel, or **both as separate simultaneous inputs**. Do not treat iron and steel as generic substitutes or silently collapse them into one metal input.

For the baseline textile chain, use one aggregated input commodity **textile raw materials** rather than separate wool/cotton cargo entries. Keep downstream **textiles/fabric** and **clothing/garments** as distinct commodities so the chain remains: textile raw materials → textiles/fabric → clothing/garments → retail/final consumption.

The textile/consumer-goods chain must support **historical recipe evolution**. Later-era recipes may add newly relevant inputs such as dyes, industrial chemicals, synthetic fibres or other historically appropriate materials. These later inputs are introduced through dated content/technology availability, not by player level, and should create new transport flows rather than silently changing output for free.

Author recipe versions/upgrades explicitly. Existing facilities keep their current recipe version until a real modernization project completes; technology availability alone must not rewrite every active plant. Content should therefore define the modernization prerequisites/cost/duration and the old/new recipe differences needed by the simulation.

Modernization content also defines the temporary **capacity-reduction factor** during the upgrade. Default authoring should preserve partial production rather than require full shutdown; full closure is exceptional and must be explicitly authored if ever needed.

Keep **crude oil**, **raw natural gas**, **processed/distribution gas**, and **refined fuels** as separate economic products.

Add **industrial chemicals** as their own transportable commodity/product family rather than treating “chemicals” as a hidden umbrella modifier. Chemical plants can consume appropriate feedstocks and produce industrial chemicals, which then become explicit physical inputs for later chains such as plastics, dyes, fertilizers, resins/adhesives and selected manufactured goods/furniture processes where historically appropriate. Crude oil and raw natural gas are primary/extractive inputs tied to suitable deposits/regions. Refined fuels are downstream products of crude-oil processing. Raw natural gas must be treated/processed before it becomes distribution-quality gas for city/industrial consumption.

The gas economy evolves historically. Around the 1900 start, cities can also obtain **town/distribution gas from coal-based gasworks** where regionally appropriate; later, processed natural gas can increasingly replace that production route. This uses **one canonical downstream commodity ID for distribution gas**. Coal-gas works and later natural-gas treatment plants are alternative production routes feeding the same city/industrial gas demand; do not create separate "town gas" and "natural gas for cities" commodities unless a future design explicitly requires materially different consumer handling.

Distribution gas is primarily a utility-network product rather than ordinary wagon/truck freight. Do not require generic rail/road vehicles to transport pipeline gas. If LPG or another transportable gas-derived liquid is added later, model it as a separate cargo definition with its own handling rules. Water and traction feed/consumables may be additional supplies.

Do not split consumer goods down to individual retail SKUs. The purpose of the extra food categories is to create distinct production, perishability/handling and transport decisions, not to simulate every product sold by a shop.

The catalogue must exercise bulk mass, volume-limited goods, indivisible units, perishable/temperature-sensitive cargo and a restricted/hazardous handling case. Standardized modern container/pallet systems must not appear in 1900 merely because the generic allocation engine supports them; introduce them with the appropriate later content.

At least four complete linked economic chains must operate, including extraction/agriculture, processing and a real **final-use sink**. No authored chain may terminate at a producer/intermediate commodity with no downstream use.

The ultimate sink of every chain must be part of the city/urban economy, directly or indirectly: household-facing retail/services, construction/buildings, utilities, public institutions, transport/operating consumption, or another final-use activity that ultimately supports city population, employment, services or development. Intermediate industrial firms can of course consume each other's outputs, but every chain must eventually reach one of these final-use sinks.

Use a generic final commodity **consumer goods** for manufactured retail products that do not justify their own gameplay-relevant category. Keep clearly distinct categories such as food groups, clothing/garments and furniture separate where their production, handling or demand creates meaningful transport decisions. Do not proliferate dozens of retail SKUs solely for realism.

At least one chain supplies vehicle operations, one supplies construction, one contains perishable cargo and one supports a multi-leg road/rail transfer. Exact recipes and ratios are balancing data, with explicit unit conversions.

### Commodity grouping and recipe rules

Player-facing commodities are **logistics/economic groups, not individual SKUs**. Split a product into its own commodity only when the distinction creates a meaningful difference in origin geography, handling/storage, compatible vehicles, perishability/hazard, historical transition, contract market or final demand.

A facility recipe may require **multiple physical inputs in parallel**. There is no one-input/one-output assumption. For example:

- a machinery plant can require steel + metal products + basic/modern spare-parts inputs;
- modern furniture can require processed wood + industrial chemicals + textiles or plastics;
- modern consumer manufacturing can require plastics + metal products + electronics + textiles;
- advanced workshops can require modern spare parts + lubricants/technical fluids + electronics.

All mandatory inputs are independently stocked and consumed. Missing one required input constrains the part of production that depends on it; another abundant input cannot silently substitute unless the facility has a separately authored recipe/version that explicitly permits that alternative. Optional inputs can improve throughput/quality only when a real authored rule exists.

### Canonical 1900 chain network

The first-playable 1900 economy uses the following **commodity groups and chain families**. A regional fixture need not contain every industry, but the content set and simulation must support these identities and relationships.

| Chain / sector | Main physical inputs | Output group(s) | Final use / downstream demand |
|---|---|---|---|
| Forestry | resource/land | timber | processed wood, paper, construction |
| Sawmill / wood processing | timber | processed wood | furniture, construction, manufactured goods |
| Furniture | processed wood; later recipes may also require textiles, chemicals, plastics or metal products | furniture | furniture retail / city consumption |
| Paper | timber/processed wood + energy; later chemicals where applicable | paper products | offices, public institutions, retail/consumer goods and packaging use |
| Grain | agricultural production | grain | flour/bakery products, selected later food processing |
| Bakery / milling | grain + energy | flour/bakery products | food retail / city consumption |
| Livestock / meat | livestock | meat | food retail / city consumption |
| Dairy | dairy production | dairy products | food retail / city consumption |
| Produce | fruit/vegetables | fruit/vegetables | food retail / city consumption |
| Textiles | textile raw materials + energy | textiles/fabric | clothing, furniture/upholstery, later consumer manufacturing |
| Clothing | textiles/fabric | clothing/garments | clothing retail / city consumption |
| Aggregates | quarry/resource | stone/gravel | construction and infrastructure |
| Bricks | local mineral/clay resource + coal/energy | bricks | buildings and infrastructure |
| Cement | local mineral/limestone resource + coal/energy | cement | buildings and infrastructure |
| Glass | local mineral inputs + coal/energy | glass | buildings, city consumption and later manufactured goods |
| Iron production | iron ore + coal | iron | steel, metal products, machinery |
| Steel production | iron + coal/energy | steel | metal products, machinery, construction, spare parts |
| Metalworking | iron and/or steel | metal products | construction, machinery, spare parts, manufactured goods |
| Machinery | iron and/or steel + metal products | machinery | factories, utilities, construction, transport investment/modernization |
| Basic spare parts | iron/steel + metal products + machinery-sector inputs | basic spare parts | older vehicles, workshops, factories, utilities and infrastructure maintenance |
| Coal economy | coal | fuel/energy input | steam transport, industry, heating, electricity and gasworks |
| Distribution gas | coal → gasworks | distribution gas | city/industrial utility demand through gas network |
| Electricity | coal/other historically available generation inputs | electricity | city, industry and later electric transport through power network |
| Petroleum | crude oil | refined fuels | transport, industry and selected utility/city use; initially regional/limited |
| Lubricants / technical fluids | refined fuels and/or chemical processing | lubricants/technical fluids | vehicles, workshops and industrial machinery |
| General manufacturing | processed wood + textiles/fabric + metal products + paper products and other recipe-specific inputs | consumer goods | retail / city consumption |

**Construction projects are multi-input consumers.** A project can require stone/gravel + bricks + cement + processed wood + iron/steel/metal products + glass in parallel according to project type/era. Construction must not consume a single generic “building materials” token.

**Furniture, clothing, paper products, glass and consumer goods remain separate final/intermediate groups** because they create materially different upstream chains or handling/demand. Minor retail variants inside those groups remain abstracted.

**Livestock is a physical cargo** where the transport/region supports it. Meat is a separate downstream commodity. The design does not require raw milk as a separate V1 cargo; dairy production can output dairy products directly at this abstraction.

Brickworks may use local on-site clay/mineral resources rather than creating a dedicated clay cargo. Cement and glass plants may likewise use suitable local mineral inputs while still requiring transported fuel/other inputs. Add a mineral as a transport commodity only when moving it creates meaningful logistics.

Iron and steel remain independent. A downstream recipe can require iron, steel, or both simultaneously. Steel is not a universal upgrade token and neither commodity substitutes for the other unless a separate recipe explicitly says so.

### Maintenance and installed-base demand

The economy must create freight not only from **new production**, but from the installed asset base.

Use two spare-parts generations:

- **basic spare parts** — older/mechanical vehicles, machinery, factories, workshops, utilities and infrastructure;
- **modern spare parts** — later equipment and systems; typical recipe inputs include metal products + plastics + industrial chemicals + electronics.

Older assets keep consuming basic spare parts after modern parts appear. A modern workshop/factory can require several supplies in parallel, for example modern spare parts + lubricants/technical fluids + electronics.

Routine operating supplies also evolve: steam equipment uses coal/water; combustion equipment increasingly uses refined fuels + lubricants; electric equipment shifts energy demand to electricity while still requiring physical maintenance supplies.

### Historical chain expansion

Later development adds new **groups** and new recipe dependencies rather than replacing the whole graph at once.

| Later commodity group | Typical production / parallel inputs | Typical downstream demand |
|---|---|---|
| raw natural gas | extraction | gas treatment, industrial chemicals, selected industry |
| distribution gas | treated natural gas **or** legacy coal gasworks | city/industry utility demand; one canonical downstream gas product |
| industrial chemicals | oil/gas/coal/other authored feedstocks + energy | plastics, fertilizer, paper/textile processing, furniture, medical supplies, consumer manufacturing |
| fertilizer | industrial chemicals | grain, produce and other agriculture as a production input |
| plastics | industrial chemicals + energy | consumer goods, furniture, machinery, modern spare parts, electronics |
| electronics | metal products + plastics + industrial chemicals + electricity | consumer goods, modern machinery, modern spare parts, utilities/transport systems |
| medical supplies | industrial chemicals + plastics + textiles/glass where applicable | hospitals, pharmacies/public institutions and city consumption |
| modern spare parts | metal products + plastics + industrial chemicals + electronics | modern vehicles, factories, utilities and infrastructure |
| LPG / transportable gas products where authored | gas/oil processing | tank-compatible city/industry/transport demand |

**Electronics includes semiconductor chips/components.** Do not create a separate player-facing “chips” commodity. As technology advances, the internal sophistication of the electronics recipe can increase through higher chemical, plastics, metal-products and electricity requirements, plant modernization and more demanding production conditions.

Synthetic fibres are likewise normally represented as a newer input route into the existing **textile raw materials / textiles** chain rather than a mandatory separate cargo group. Add a separate cargo only if later content demonstrates a real logistics reason.

### How chains evolve and displace each other

Historical development changes both recipes and market shares.

- Coal can lose transport, heating, gasworks and electricity demand to refined fuels, electricity, natural gas and later generation technologies.
- Natural-gas treatment can take over production of the same distribution-gas product from coal gasworks.
- Plastics can replace part of wood, metal, glass or textile demand in specific modernized recipes.
- Electronics can replace part of mechanical/electromechanical content in machinery, spare parts and consumer goods.
- Fertilizer and machinery can raise/change agricultural output and therefore downstream food freight.
- Paper, plastics and other materials can change packaging/consumer-manufacturing recipes without creating a separate SKU for every packaging type.

Displacement is **use-specific, gradual and regional**. A new commodity does not globally erase its predecessor. Old firms keep their current recipe until they modernize; old assets keep consuming the supplies they genuinely require.

Do not add a commodity merely because it existed historically. It must create a distinct sourcing, transport, storage/handling, investment, maintenance or demand decision.

Consumption/production cannot create free inventory. A recipe is an explicit conversion, with declared waste/loss where used. Cargo conservation tests concern transportation quantities; production is an authorized inventory transformation, not a false invariant violation.

Cooling/ice/refrigeration, packaging and hazardous handling require corresponding equipment and supplies or a genuine provider that supplies them. A refrigerated wagon definition alone does not supply infinite cooling.

### Passenger markets

Supply aggregate segments for work/commuting, school, business, personal/social and leisure travel, with era-appropriate weighting and rhythms. Ordinary passengers are not all identical and do not require persistent individual identities.

Provide at least these functional products: open-board local bus, regular intercity bus, local passenger train and longer-distance rail with differentiated capacity zones. Include both individual demand and one commercial group/public-service contract type. Protected multimodal transfers need actual walking links/endpoints and usable sales channels.

Track seated/standing/accommodation capacity where permitted, class/product, reservations by stop interval, waiting age, current itinerary and recovery. Do not create a seat-number simulator. Quality factors remain separate and explainable.

## 5. Facilities and construction kit

Count functional modules rather than dozens of redundant buildings. The kit must cover:

| Function | Minimum content |
|---|---|
| Branches | Small rented office, standalone branch and integrated hub office; scalable office capacity/equipment/staff |
| Road operation | Parking/garage, workshop, fuel/supply point, horse stable support, passenger stop/terminal and cargo loading point |
| Rail operation | Track/switch/crossing tools, through and terminal stations, freight loading tracks, sidings, parking/yard, operating depot, workshop, turntable or triangle capability, run-around capability |
| Cargo/storage | General warehouse, open bulk yard, grain storage, liquid storage, cold-chain-capable storage and compatible transfer equipment |
| Passenger service | Platform/entrance/access modules, ticket sales, circulation/transfer links and service/amenity modules appropriate to the date |
| Engineering | Bridges, tunnels, earthworks, signalling/operating sections, access roads, project boundaries/corridors and construction stages |
| Later progression | Electrification, contemporary power/fuel support, improved handling/service equipment, later passenger information and office systems |

Every operational facility declares physical footprint/connections, ownership/access, compatible work, capacity units, staffing/equipment, cost, construction prerequisites/duration, maintenance and visual stages. Capacity must have meaningful units: metres, positions, vehicles, tonnes, handling rate, service bays or office workload, not one universal percentage.

Provide more than one useful station size and at least two different yard/station topologies. A single hardcoded demo station cannot validate route building, dynamic platforms, turning and shunting. Bridges and tunnels need proper geometry and limits; they cannot be surface track with a different material.

## 6. Firms, AI and market content

Initial target: at least six transport competitors distributed across the world, with at least two relevant to a supported starting area. They need not all be large or active in every mode. Use private/local/public service profiles with the same resource and contract rules.

Provide at least two providers in each major market category across the full world: compatible construction, maintenance, vehicles/supply and external road/rail transport. Categories can be integrated in the same firm when its real assets support both roles. Do not require a supplier monopoly in every starting town, and do not guarantee a compatible offer for every unusual request.

For core business variation author at least eight reusable opportunity/contract templates: one-off freight, recurring freight, protected/guaranteed flow, seasonal flow, group passenger service, municipal/local bus service, external subcontract and operating-supply/service agreement. The templates produce offers only from real economic demand/capacity.

At least two contractor capability/scale groups, two maintenance support families and differentiated vehicle-source lead times are needed to test real trade-offs. Both new factory orders and finite ready dealer stock must work. Used listings refer to concrete assets. Ownership/share transactions preserve contracts, liabilities and asset IDs.

## 7. Default balancing package

These are starting balancing conventions, not a historical financial reconstruction. Record actual values in a versioned configuration and revise them using measured playthroughs.

- Currency is exactly `money`. Use fixed-point arithmetic, for example 100 internal subunits per money, and make display precision independent of simulation units.
- Three founding-loan tiers have predictable favourable terms. A possible initial convention is 2% nominal annual interest over 20 game years, monthly amortizing repayments and no punitive tier-specific interest increase. The same 168-day year/12-month calendar applies. If using this convention, derive the monthly payment from principal and monthly rate; do not charge accrued interest twice.
- Set the principal of each tier from a tested setup basket, not an arbitrary impressive number. The small basket includes real office setup/director/staff, the necessary licences, endpoint access, one viable road vehicle, delivery and support, plus a working-capital reserve. The standard/large baskets offer broader options and a credible modest rail setup where justified.
- Initial working-capital target: at least two game months of ordinary expenses for the tested recommended opening after its minimum setup costs. This does not guarantee profit for any arbitrary purchase plan.
- Display monthly/annual wages, tariffs, loan charges, fixed facility cost and production rates in explicit game-time units. Distance/wear and consumed fuel remain per real simulated work.
- Initial maintenance policies, service intervals, reserve ratios, penalties and cancellation caps are configurable. Exact fees in CONTRACT_CANCELLATION remain balancing parameters; preserve its bounded, proportionate rule and prepaid-credit reconciliation.
- Expected margins are forecasts from the same cost model, not guaranteed payouts. Test at least one profitable competent opening and one understandable loss-making overcommitment.
- Raising a founding-loan tier changes financing only, not AI intelligence, demand, reputation or hidden difficulty.

Provide an economy audit that can explain each tested Trip/Line's revenue, variable operation, allocated fixed cost, access fees, wages, maintenance and debt-service effect. Do not mix operational profitability and cash flow without labels.

## 8. Art, audio and UI content minimum

Provide a coherent material/colour system, recognizable model families and regional architecture. Initial modular building kit target: at least 18 distinct useful shapes/functions spanning housing/urban blocks, rural buildings, industrial sites, offices and transport structures. Variation may come from roofs, facades, height, attachments and materials, but an entire city must not be one scaled cube.

Include forests/trees, fields/ground surfaces, river/water treatment, roads, rail ballast/sleepers, platforms, earthworks, bridges/tunnel portals and site stages. Vehicle and infrastructure LODs must preserve readable functional differences at the relevant zoom levels.

At least a minimal audio set for steam/rail movement, motor/horse road operation, relevant service/terminal action, environment and UI feedback. Use original/procedural or permission-compatible assets; keep source notices. Music and voice acting are not completion requirements.

All primary screens listed in the implementation brief require localized populated, empty, loading, blocked and confirmation states. Every active text key must exist in Czech and English. Use correct Czech diacritics and a font/renderer that supports them; do not commit or distribute unlicensed third-party fonts. Displayed proper names follow the chosen locale rules; stable IDs never change with language.

## 9. Benchmark fixtures and targets

These are engineering targets to measure, not existing benchmark results or promised minimum hardware specifications. Record actual CPU, RAM, GPU, storage, OS, editor/player version, resolution and quality. Do not infer the user's CPU/RAM from a GPU mentioned in another project.

| Fixture | Initial target workload |
|---|---|
| Small opening | One active area, 2–3 commercial localities, 20 player operating vehicles, at least 2 relevant rivals, 500 active cargo/passenger groups |
| Regional network | Several active regions, 250 player operating vehicles, 50 Service Patterns, at least 4 rivals, 10,000 active groups |
| Developed network | Full approved active-world test, 2,000 operating vehicles across all carriers, at least 300 Patterns, 50,000 active groups; separately record actual wagon count and graph size |

An operating vehicle here means a road unit or a train service unit; record physical wagons separately so counts are not manipulated. Test inactive regions and camera distance independently from operational load.

Initial presentation target on a documented reference desktop: stable approximately 60 FPS at 1080p medium in normal small/regional play, with no repeated disruptive hitches; developed-network target at least 30 FPS and measured sustained requested 16x simulation after warm-up. These are goals to validate, not reasons to skip events. Report p50/p95/p99 frame and simulation-step timings, memory/GC, save/load times, queue depth and achieved/requested time ratio.

Use five-real-minute measured intervals after warm-up for each speed/workload and a longer soak for leaks/stability. A headless fixture may simulate years faster for testing, but that is not a new player speed setting. Failure to meet a target needs transparent optimization/limitation reporting; no fabricated pass.

## 10. Source and completion records

Each imported dataset/asset needs source URL or provenance, licence/usage conditions, acquisition/version date, file hash, transformation description and required notice. Keep 1900 historical overlays separate from modern geometry sources. Apply the versioned source-date convention in DATA_PIPELINE.md once; retain the original dates and provenance. Include source credits in the shipped game and accompanying notices as required by the selected licence.

The completed manifest must report: required entries, complete entries, missing entries, validated date coverage, missing translation keys, missing prefabs, incompatible definitions, unsupported dependencies and historical/source review status. Store individual asset/content completion and test evidence in IMPLEMENTATION_STATUS.

A small fixture, list of planned assets or external download instruction is not a bundled release world. A player must not need to run GIS tooling or sign up for a data service to start the final build.
