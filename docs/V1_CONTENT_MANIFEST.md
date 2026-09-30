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

Initial target: at least 12 meaningful cargo/operating-supply definitions. Use historically appropriate packaging and technology. Recommended functional coverage includes coal, timber, processed wood, grain, milled/food products, perishable produce/dairy, ore, metal/steel products, stone/building materials, liquid fuel or other industrial liquids, manufactured goods and indivisible machinery. Water and traction feed/consumables may be additional supplies.

The catalogue must exercise bulk mass, volume-limited goods, indivisible units, perishable/temperature-sensitive cargo and a restricted/hazardous handling case. Standardized modern container/pallet systems must not appear in 1900 merely because the generic allocation engine supports them; introduce them with the appropriate later content.

At least four complete linked economic chains must operate, including extraction/agriculture, processing and a real consumer. At least one chain supplies vehicle operations, one supplies construction, one contains perishable cargo and one supports a multi-leg road/rail transfer. Example authoring chains are timber → processed wood → construction, grain → food processing → city consumption, ore/energy → metal products → manufacturing, and local food → distribution → consumers. Exact recipes and ratios are balancing data, with explicit unit conversions.

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
