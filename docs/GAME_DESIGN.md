# Tranzit — Living Game Design

> **Status:** Living source of truth. This document describes the current agreed design. It is not a chronological idea log.
>
> **Maintenance rule:** Before adding or changing any feature, review all affected sections and resolve contradictions. Remove or rewrite obsolete decisions instead of appending conflicting alternatives.

## 1. Vision

Tranzit is a long-form transport and business simulation built in Unity. The player starts as a tiny regional carrier around 1820 and can grow into a multinational transport group over roughly 100–150 hours of a normal campaign.

The game should feel like a living model railway / model world viewed from above: a large stylized but believable Central European world that changes physically, economically and technologically over two centuries.

Core pillars:

1. **Physical continuity** — vehicles, rolling stock and infrastructure physically exist in the world. They do not teleport, magically reverse direction or disappear into menus.
2. **Deep but scalable simulation** — the economy, cities, industries, passengers and competitors should feel alive, but use aggregation, event-driven logic, caching and simulation LOD instead of brute-force per-agent simulation.
3. **Historical technological progression** — technology changes what the player can build, how the company is managed and what markets exist.
4. **Progressive delegation** — early game is hands-on; later, managers, dispatchers and information systems automate increasingly large parts of the company.
5. **Dynamic economy** — transport demand should emerge from companies, cities, supply chains, passengers, state contracts and technology rather than from arbitrary cargo generators.
6. **Infrastructure matters** — depots, terminals, stations, sidings, turning facilities, maintenance bases, storage, access rights and track capacity are gameplay, not decoration.
7. **The world responds to the player** — good transport can change city growth, industrial geography and regional prosperity.

## 2. World, map and regions

### 2.1 Geography

The first playable world is based on real European geography, initially focused on Central Europe. The first production scope should prioritize areas corresponding to modern Czechia plus nearby Central European regions; Germany, Austria, Hungary and Poland are natural early expansion targets.

The map must be physically large enough that major cities have meaningful space between them. Travel should feel like travel, not like moving between adjacent miniature towns.

The long-term architecture must allow a procedural map generator later, but the initial world is authored from real geography.

### 2.2 Region identity

Regions differ naturally rather than through arbitrary game bonuses:

- terrain and relief,
- city density,
- typical industries and resources,
- agricultural character,
- historical architecture,
- infrastructure,
- population and economic potential.

The Czech lands should visibly feel different from Austria, Hungary, Saxony, Bavaria, Poland, etc.

### 2.3 Terrain

The world is not grid-based.

Roads, rails, canals and other linear infrastructure use free-form spline placement. Buildings can be freely rotated. Snapping exists only where physical connections are required.

Terrain is geographically distinct by region: hills, plains, mountains, forests, fields, rivers and other landforms should reflect the region.

### 2.4 Unlocking countries and regions

The world outside the active territory exists only as a lightweight macro layer until unlocked.

Entering a country requires real expansion rather than a simple unlock button:

- appropriate national licence/concession,
- a local branch or acquisition,
- a physical connection or credible access route.

A national agreement initially grants access to roughly 1–3 regions depending on price, reputation and negotiated conditions. Further regions must be acquired individually.

Regions have different values based on population, industries, resources, infrastructure, strategic location and market potential.

Terms can be negotiated with the state, e.g. higher entry fee, infrastructure commitment, required services or local employment in exchange for cheaper/broader access.

When a region becomes active, it is instantiated directly at the current historical date from its macro state. It does not simulate every year since 1820 retroactively. Once activated, it remains simulated.

### 2.5 World outside the active map

Inactive Europe and the wider world are not fully simulated, but the player receives period-appropriate newspaper/world-news items, potentially with stylized illustrations, so the world feels larger than the active map.

These reports can foreshadow technologies, economic changes and future expansion opportunities.

## 3. Time and historical progression

The campaign begins around **1820**.

The world is historically anchored but not fully deterministic:

- major political and technological shifts happen approximately in their real periods,
- exact years and severity can vary,
- smaller economic events can diverge significantly between campaigns.

Historically, the 1820 Czech lands are part of the Austrian Empire. Austria-Hungary only appears later if the timeline reaches the relevant historical transition.

The game should take around **100–150 hours** to move from 1820 to roughly 2020 under normal play, with time controls available.

Technology should not be only year-gated. Historical year is the baseline, but research can bring some technologies forward within plausible bounds.

## 4. Visual direction

### 4.1 Camera and presentation

- 3D top-down strategy camera.
- Free camera rotation.
- Strong diorama/model-world/model-railway feeling.
- The player should feel like they are building and managing a living miniature world.
- No first-person mode is required.

### 4.2 Art direction

Stylized realism: visually believable but slightly illustrated/stylized rather than photorealistic.

Strong Central/Eastern European identity:

- European street patterns,
- dense historic centres,
- traditional blocks,
- industrial districts,
- later socialist-era housing estates where appropriate,
- suburban growth,
- occasional high-rise landmarks but few generic skyscrapers,
- regional architectural differences,
- historical evolution of building styles.

Cities must not look like generic American grids.

## 5. Simulation architecture principles

These are design constraints, not optional optimizations.

### 5.1 Simulation LOD

Different levels of detail are used depending on relevance and camera distance:

- **Detailed:** visible local movement, station operations, representative pedestrians, physical train movements.
- **Standard:** exact operational state without unnecessary visual/physics detail.
- **Aggregated:** remote areas use scheduled/event-based state transitions rather than continuous simulation.

### 5.2 Event-driven systems

Do not update everything every frame.

Examples:

- economic firms tick daily/weekly/monthly,
- maintenance wear can update after trips/segments,
- route options are cached,
- pathfinding reruns only when relevant topology/service conditions change,
- breakdowns can be scheduled probabilistically at trip start instead of rolled every frame.

### 5.3 Physical continuity

Every player vehicle and relevant rolling-stock asset always has a logical world location.

A vehicle may stop being rendered at distance, but it never logically disappears.

Vehicles cannot:

- teleport to depots,
- magically reverse,
- change train composition through menus without physical shunting/transfer,
- appear in a remote region without transport.

The only abstract boundary is the not-yet-simulated outside world. Imported vehicles enter through defined map entry/import points and then become normal physical assets.

## 6. Population, passengers and cities

### 6.1 Population model

Population is primarily aggregated, not one persistent simulated person per inhabitant.

Demand is generated as origin-destination flows segmented by purpose and passenger type.

Representative visible NPCs are spawned only to visualize real aggregate flows around the camera.

Example:

- simulation says 300 passengers are on a train,
- the rendered scene may show 50–80 representative people,
- the underlying transport count remains 300.

### 6.2 Passenger trip choice

Trips can combine multiple modes and operators:

home/zone → walk/bus/tram → station → train → transfer → local transport → destination zone.

Passenger choice depends on factors such as:

- price,
- travel time,
- frequency,
- reliability,
- number/quality of transfers,
- comfort,
- operator reputation,
- purpose of journey.

Journey purposes include work, business, school, tourism/leisure, family/social visits and other meaningful categories.

Different segments value time, price, comfort and reliability differently.

### 6.3 Private cars

Private motoring grows with technology, household prosperity, road quality and vehicle availability.

Cars compete with public transport and can reduce demand for trains/buses where public transport is unattractive.

Private traffic is economically aggregated and visually represented with traffic agents rather than one permanent simulation object per privately owned car.

Road congestion affects buses and trucks.

The player can later influence modal choice through infrastructure such as:

- P+R,
- parking,
- transport hubs,
- toll roads/highways,
- good interchange design.

### 6.4 City growth

Cities physically expand on the map.

Growth uses both:

1. a historical baseline based on real importance/population trajectory;
2. dynamic simulation based on accessibility, jobs, goods supply, transport quality and regional economy.

Without player intervention, cities should remain broadly plausible historically. Good or bad transport can significantly alter their trajectory.

Urban form evolves over time. Historic cores, industrial districts, interwar growth, later housing estates and modern suburbs should look different.

Protected/historic areas can restrict demolition and construction.

Old industrial sites can become brownfields and later be redeveloped, including adaptive reuse into housing/offices while retaining an industrial visual character.

## 7. Company progression and organization

### 7.1 Early game

The player starts with a very small company:

- one first regional branch/office placed in a chosen city,
- a handful of horse-drawn vehicles,
- limited staff,
- limited capital,
- local contracts and passenger demand.

The first branch is the local commercial hub. Its physical location matters.

### 7.2 Branch reach

Branches have a commercial catchment.

Early on, a branch can only serve nearby customers. Telegraph, telephone and later electronic systems expand this reach. Modern digital ordering largely removes the constraint.

### 7.3 Divisions and subsidiaries

The player begins as one company.

As the company grows, it may create divisions such as Rail, Road, Shipping, Urban Transport and Infrastructure.

A division may later be spun out into a subsidiary with its own:

- finances,
- contracts,
- licences,
- management,
- workforce,
- reputation,
- assets.

Subsidiaries can remain 100% owned, be partly sold, or eventually merged.

### 7.4 Managers and delegation

Managers and important specialists are named individuals. Ordinary staff are aggregated.

Possible management scopes include:

- whole company/division,
- country/region,
- station/depot/terminal,
- group of lines,
- specific line/service.

Manual overrides at a lower level take precedence over higher-level automation.

Managers have skills and salaries and may provide bonuses in areas such as pricing, reliability, staffing, contract handling or automation.

Management is optional gameplay: HR and routine hiring can increasingly be automated.

## 8. Workforce

Ordinary employees are aggregated by site/region/function, including:

- drivers and train crews,
- mechanics,
- dispatchers,
- station and terminal staff,
- office/admin staff,
- sales/contract staff,
- warehouse staff,
- safety/security/cleaning where relevant.

Insufficient staffing creates concrete operational consequences such as slower maintenance, reduced opening hours, delayed handling or weaker contract capacity.

## 9. Reputation and customer relationships

Reputation is not a single cosmetic score.

The design should support:

- overall company reputation,
- regional reputation,
- potentially service/segment reputation.

Reputation can affect:

- passenger operator choice,
- customer contract decisions,
- public tenders,
- licence negotiations,
- relations with municipalities/states,
- hiring,
- partner-carrier relationships.

Demolition, service quality, reliability, accidents and contract performance can alter reputation.

### 9.1 Customer-specific relationships

Important customers such as factories, mines, municipalities and large commercial firms can also have a direct long-term relationship with each transport operator.

This relationship is separate from general reputation and is built through actual business history, for example:

- completed contracts,
- reliability and on-time performance,
- damage/spoilage rates,
- pricing consistency,
- responsiveness to urgent jobs,
- capacity offered,
- contract breaches,
- length of cooperation.

The system must be transparent. A customer decision must never feel like a hidden arbitrary modifier.

When evaluating or awarding a contract, the UI should show the major reasons for the customer's preference, for example:

- strong existing relationship,
- better historical reliability,
- lower bid,
- higher guaranteed capacity,
- better local reputation,
- prior contract failure,
- insufficient experience with this customer.

A player who currently has a weak relationship must have a credible path to improve it. Customers should offer smaller/less critical jobs or trial contracts that allow a new carrier to prove itself before becoming competitive for major long-term contracts.

Existing relationships are an advantage, not an unbeatable lock-in. A new carrier can win business through better price, service quality, capacity or successful smaller contracts.

Customer relationship evaluation must use cached historical aggregates and contract outcomes rather than expensive continuous AI.

## 10. Economy and industries

### 10.1 Firms

Industrial and commercial firms are economic entities with simplified but real state:

- cash/debt,
- workforce aggregate,
- production capacity,
- input inventories,
- output inventories,
- suppliers/customers,
- orders/contracts,
- profitability,
- ownership.

They do not run expensive continuous AI.

### 10.2 Industrial geography

Industry is dynamic but geographically grounded.

Resource extraction is constrained by plausible deposits and land conditions.

Large deposits may effectively last the full campaign; smaller deposits can deplete and close.

Processing/manufacturing industries are more flexible and can choose locations based on labour, transport, markets and inputs.

New firms and facilities may emerge over time. Existing firms can expand, open new plants, acquire other firms or decline.

### 10.3 Historical commodity demand

Commodity importance changes over time.

Examples:

- coal becomes critical in the industrial age and later declines relatively,
- oil and gas rise later,
- electricity systems alter energy demand,
- modern renewables change demand again.

Industrial decline can leave physical brownfields.

### 10.4 Market accessibility

Firms do not search every destination in Europe every tick.

Regional/market accessibility is cached and updated when relevant transport or economic conditions change.

Better infrastructure can open previously uneconomic markets.

## 11. Contracts and cargo

### 11.1 Contracts are central

Cargo gameplay is primarily contract-driven.

Early game emphasizes direct management of individual jobs and vehicles.

Contract types include:

- one-off shipment,
- recurring/framework contract,
- state/public contract,
- carrier subcontract,
- long-term supply contract.

Contract awards should consider transparent factors such as price, capacity, reliability, relevant reputation and customer-specific relationship history. The player must be able to inspect the important decision factors before or after bidding.

Large customers may reserve their most important contracts for carriers with proven history, while still exposing smaller trial jobs that let new entrants build trust.

### 11.2 Contract award models

Contract complexity scales with importance so routine work does not become paperwork:

1. **Small / routine jobs:** fixed offer; accept or decline.
2. **Medium contracts:** the player mainly bids price and capacity.
3. **Large contracts:** structured tender with price, guaranteed capacity, delivery/service level and contract duration.
4. **Strategic long-term contracts:** structured tender plus limited negotiation over terms such as price, guaranteed volume, duration, service level and penalties.

Negotiation is parameter-based rather than a dialogue mini-game. The UI should immediately show the commercial effect of changing a term.

Routine bidding can later be delegated to commercial managers using player-defined rules such as minimum margin, maximum commitment, customer priority and approval thresholds.

AI competitors must bid from their real available capacity, costs, network access, relationship and strategy. They must not generate fake impossible bids simply to beat the player.

### 11.3 Exclusivity

Large or strategic contracts can include exclusivity.

An exclusive contract can guarantee the carrier all or most of a customer's defined transport volume for the covered flow, period or commodity.

In return, the carrier accepts stronger obligations such as:

- guaranteed minimum capacity,
- stricter reliability/service-level targets,
- stronger penalties for failure,
- potentially reserved fleet/infrastructure capacity,
- limited ability to reject individual shipments within the agreed range.

Exclusivity is optional and must be priced as a risk/reward trade-off. It can create stable revenue and deepen customer relationships, but can become costly if the carrier overcommits.

The customer must still have emergency fallback rights where the contract explicitly allows them, for example after repeated SLA breaches or when the carrier cannot accept the guaranteed volume.

### 11.4 Performance bonuses

Medium, large and strategic contracts can include optional bonus tiers above the minimum SLA.

Examples:

- contract requires delivery within 48 hours, but average delivery under 30 hours earns a higher rate;
- contract requires 95% on-time performance, while 99% earns a periodic performance bonus;
- contract guarantees a minimum monthly volume, while handling surge volume without failure earns an additional payment;
- exceptionally low damage/spoilage can improve payout for sensitive cargo.

Bonuses must be visible before signing and tied to measurable contract KPIs. They should reward operational excellence rather than create hidden modifiers.

Performance above the contractual minimum can also improve customer-specific relationship history and relevant reputation, but the direct financial bonus and the relationship/reputation effect remain separate systems.

### 11.5 Reserved capacity commitments

Some medium, large and strategic contracts can require the carrier to keep a defined amount of transport capacity available for the customer, including surge/emergency capacity that may not be used every day.

This must be completely transparent and expressed in both commercial and physical terms before signing.

The contract planner should show, for the proposed route and service pattern:

- guaranteed tonnes/passengers per period,
- maximum surge requirement,
- response window,
- estimated number and type of wagons/vehicles required,
- locomotives/traction required,
- terminal/storage requirements,
- expected infrastructure capacity consumption,
- estimated staff requirement,
- how much of the player's currently available fleet would become committed,
- what spare capacity remains after accepting the contract.

For example, instead of only displaying "reserve 200 t capacity", the UI should translate that into something like "requires approximately 8 compatible wagons and 1 suitable locomotive available within 24 hours on this corridor" based on the player's current rolling stock and route.

Reserved capacity is a real commitment, not a hidden score. Assets do not necessarily need to sit idle permanently: they may perform other work when scheduling still guarantees the contracted response time. Dispatch automation may manage this later, but it must never allocate committed assets in a way that silently makes the SLA impossible.

If current fleet, depot, terminal or infrastructure capacity cannot credibly satisfy the commitment, the game must warn the player before the bid is submitted and explain the bottleneck.

AI competitors are subject to the same capacity accounting and cannot promise reserve capacity they cannot realistically provide.

### 11.6 Contract renegotiation

Long-running contracts can be reopened when material operating conditions change.

Valid triggers can include:

- major fuel or energy price shocks,
- border closures or regulatory changes,
- loss of access to a previously valid route,
- major infrastructure disruption,
- exceptional input-cost inflation,
- customer-requested volume or SLA changes,
- mutually agreed strategic restructuring.

Renegotiation is not a free escape from a bad deal. The requesting side must state what changed and propose concrete revised terms.

Possible changes include:

- price,
- guaranteed volume,
- reserved capacity,
- delivery/service-level target,
- contract duration,
- penalties,
- exclusivity.

The counterparty can accept, reject or make a counteroffer.

The UI must show why the other party reacts the way it does, using transparent factors such as the size of the cost shock, existing relationship, alternative carriers, contract performance and remaining contract duration.

A weak justification or repeated attempts to reopen favourable terms can damage customer relationship and reputation. A genuine external shock should carry much smaller or no reputational penalty.

Contracts may also contain pre-agreed adjustment clauses, such as fuel-price indexing or automatic rate review at defined intervals, reducing the need for manual renegotiation.

Commercial managers may later handle routine renegotiations within player-defined limits, while material strategic changes can require player approval.

### 11.7 Cargo batches

Cargo is simulated in batches, not per kilogram/item.

A batch tracks type, quantity, origin, destination, deadline/quality constraints and contract.

### 11.8 Multi-leg logistics

One customer contract can contain multiple transport legs and modes.

Cargo can physically wait in storage between legs.

Example:

farm → wagon → local terminal → warehouse → regional train → hub → long-distance train → local truck → customer.

### 11.9 Perishability and special requirements

Cargo can have properties such as:

- perishability,
- temperature requirement,
- fragility,
- hazard class,
- handling requirements.

Perishable goods lose value or become unusable if delivered too slowly or without appropriate cold-chain capability.

## 12. Storage and terminals

### 12.1 Storage

Stations have small implicit handling/storage capacity for minor shipments.

Large volumes require physical storage infrastructure.

Examples:

- general warehouse,
- cold storage,
- coal yard,
- silos,
- tanks.

Storage has real capacity. If full, cargo must wait elsewhere, remain in vehicles or be rerouted.

### 12.2 Cargo platforms and modules

Cargo handling infrastructure is modular.

A basic freight platform may handle one cargo family.

More expensive facilities can support multiple modules, e.g. up to several cargo types.

Large logistics terminals can connect platform/track infrastructure to adjacent warehouses, tanks, silos or yards.

Specialized facilities are more efficient than universal ones.

Passenger platforms are not generic freight handling points. Freight trains may pass through compatible tracks but cannot normally perform cargo handling there.

### 12.3 Handling time

Loading/unloading takes time based on:

- cargo,
- infrastructure,
- workforce,
- technology,
- platform/track length,
- handling equipment.

Handling improves historically with mechanization, pumps, cranes, conveyors, containers, etc.

## 13. Transport modes

Initial/primary modes:

- horse-drawn/road,
- railway,
- inland water/shipping,
- urban transport: bus, tram, trolleybus, metro.

Aircraft are explicitly out of current scope.

### 13.1 Roads

Road capacity is simpler than rail slotting.

Vehicles need physical/legal access and are affected by congestion, surface quality, weather and restrictions.

Roads may be public, municipal, state-owned or private/tolled.

### 13.2 Railways

Rail is capacity- and geometry-constrained.

Track is divided into meaningful operational sections between stations/junctions rather than tiny segments.

Each section has practical capacity influenced by:

- number of tracks,
- signalling,
- passing loops,
- speeds,
- traffic mix,
- technology.

The player normally requests service capacity, not exact second-by-second paths.

Possible capacity products:

- guaranteed,
- standard,
- flexible.

Real train movement still uses local section/block reservations. A train reserves only near-future sections, not its entire route.

### 13.3 Water

Open navigable water does not use railway-style path slots.

Gameplay focuses on:

- licences/access rights,
- ports,
- locks,
- canals,
- bottlenecks,
- water depth,
- terminal capacity.

The player can build canals and modify waterways, subject to cost, technology and permission.

## 14. Rail operations and rolling stock

### 14.1 Physical train composition

Every locomotive and wagon is an individual asset.

Trains are physically assembled and disassembled on real track.

A consist cannot be changed through a menu without the required physical movements.

### 14.2 Direction and turning

Vehicles respect directionality.

Steam locomotives and other one-directional equipment cannot magically reverse at a terminus.

Possible solutions include:

- run-around tracks,
- turntables,
- reversing triangles,
- second locomotive,
- later bidirectional trainsets.

### 14.3 Train feasibility

Before dispatch, the game calculates whether a consist can physically operate the planned route based on weight, traction, gradients and infrastructure.

The player should not discover a predictable traction problem only after the train stalls.

Heavy trains may need helpers/bank engines on specific sections.

### 14.4 Passenger classes and comfort

Rail can offer different classes from early periods.

Over time the player can add comfort/service features such as:

- improved seating,
- heating,
- lighting,
- toilets,
- dining,
- sleeping accommodation,
- air conditioning,
- service/baggage functions.

Comfort expectations rise over time.

A retrofit can extend usefulness, but cannot make a fundamentally obsolete vehicle equal to a modern one.

## 15. Vehicle lifecycle

### 15.1 Purchase and manufacturing

Vehicle manufacturers are real economic firms in the world, but simulated at a calmer level than transport operators.

They have:

- factories,
- material demand,
- workforce,
- production capacity,
- order backlog,
- expansion potential.

Vehicles use fictional manufacturers/models inspired by real historical technology, not real trademarks.

New vehicles are ordered and physically produced over time. Production lead times depend on factory capacity and input supply.

Completed vehicles must physically reach the player's network.

### 15.2 Used vehicle market

Used vehicles come from actual sellers.

Listings occupy real storage/depot space for the seller.

Unsold vehicles can be discounted and eventually scrapped.

Imports from inactive foreign regions enter through defined import points and are physically delivered into the active world.

### 15.3 Retrofit

Vehicles and wagons can receive period-appropriate retrofits.

Retrofit can improve condition, comfort or systems and extend life, but only within structural limits.

### 15.4 Scrapping

Assets can be physically sent to appropriate scrapping/disposal facilities. Material value can be partially recovered.

## 16. Maintenance

### 16.1 Vehicle maintenance model

Each player vehicle has a lightweight individual state:

- condition,
- age,
- mileage/hours,
- last major service,
- base reliability,
- limited active faults if needed.

No deep per-component maintenance simulator is required.

Risk also depends on the quality of the surrounding maintenance system:

- mechanics,
- workshop capacity,
- utilization,
- distance to suitable facilities,
- equipment,
- parts/supplies.

### 16.2 Physical service

Vehicles must physically travel to appropriate depots/workshops.

If a workshop is full, vehicles wait physically in yards/parking.

Remote fleets without nearby maintenance suffer real downtime because vehicles must travel farther.

### 16.3 Infrastructure maintenance

Track/road infrastructure has aggregated condition by meaningful section.

Maintenance depends on workforce, bases, equipment, budget and age.

Poor maintenance should first create:

- speed restrictions,
- delays,
- closures,
- repair work,

before becoming a serious accident risk.

Infrastructure maintenance can be done in-house or outsourced.

## 17. Depots and operating facilities

Depots are physical infrastructure, not menus.

Rail depot layout can include:

- arrival track,
- storage/sidings,
- service hall,
- coal/water/fuel,
- turning facilities,
- departure route.

Poor depot geometry can create real operational inefficiency.

Road vehicles need garages/parking/service facilities.

## 18. Energy and operating supplies

Fuel and many operating supplies are real goods.

Examples:

- coal,
- diesel/petrol,
- water,
- lubricants,
- parts,
- catering supplies.

Depots/stations maintain real inventories.

The player can:

1. buy delivered supply,
2. buy at source and transport it personally,
3. buy at source and hire another carrier,
4. use a recurring supply contract.

Automatic reorder thresholds can be configured and later delegated.

Electricity is purchased through physical grid connections/capacity rather than moved as cargo wagons.

## 19. Infrastructure ownership and access

Infrastructure can be:

- state/public,
- municipal,
- privately owned.

### 19.1 Public infrastructure

A state may commission construction and retain ownership.

It can later tender transport services over the infrastructure.

### 19.2 Private infrastructure

The player can finance and own infrastructure and charge access fees.

Building private rail should be very expensive so sharing existing infrastructure is often rational.

### 19.3 Connection agreements

The player cannot simply place a switch into someone else's track.

Connecting to foreign infrastructure requires a connection agreement/permit.

Terms can include:

- one-time fee,
- ongoing fee,
- capacity contribution,
- financing upgrades,
- guaranteed access rights.

## 20. Stations, terminals and infrastructure capacity

Stations and terminals can also be publicly or privately owned.

Other operators may pay for platform, track, storage and terminal use.

Rail infrastructure capacity is strategic, not a detailed timetable simulator by default.

The UI should communicate capacity simply, e.g. utilization per section and peak bottlenecks.

Advanced timetable tools may exist later, but are not mandatory for normal play.

## 21. Construction

### 21.1 Contractors

The player does not instantly build infrastructure.

Construction is delivered by external construction companies or, later, a player-owned construction division.

There are:

- many smaller contractors for local/simple works,
- fewer large contractors capable of major railways, highways, tunnels and canals.

Contractors have real capacity, specialization, price, technology and utilization.

### 21.2 Contractor priority market

Projects can purchase higher priority.

A contractor has guaranteed and flexible capacity. Competitors may outbid for some flexible capacity, but cannot arbitrarily steal an entire signed project.

Reallocation happens in bounded intervals, not constant bid ping-pong.

There is a practical capacity ceiling: money cannot create nonexistent workers/equipment.

### 21.3 Construction stages

Construction is visible in simplified physical stages such as:

- preparation/groundworks,
- under construction,
- completed.

Long projects progress along their route rather than the whole project appearing half-built everywhere.

### 21.4 Construction logistics

Large projects consume real materials such as timber, stone, steel, ballast and concrete.

The player chooses whether:

- the construction company supplies/logistics everything,
- the player supplies materials,
- responsibility is split.

Construction sites have temporary storage.

Lack of material can halt a stage.

### 21.5 Temporary construction infrastructure

Contractors can automatically establish simplified temporary site infrastructure such as:

- access roads,
- storage areas,
- site huts/camps,
- equipment yards.

These are mainly operational/visual and should not require heavy micromanagement.

After completion, relevant temporary roads can be removed, retained or converted.

### 21.6 Technological construction progress

Construction speed and capability improve historically through mechanization and specialized equipment, including later track-laying/maintenance trains.

## 22. Terrain engineering

Terraforming is not a free standalone brush.

Terrain modification is permitted only as part of a building/infrastructure project or modification.

Earthworks are real project scope requiring:

- excavation/fill,
- machines,
- workers,
- time,
- potentially transported materials.

## 23. Bridges and tunnels

Bridges and tunnels have period-specific structural technologies.

Options differ in:

- cost,
- construction time,
- load limit,
- speed limit,
- span/capability,
- lifespan,
- maintenance.

Old bridges may become inadequate for later heavier/faster vehicles and require reinforcement or replacement.

## 24. Construction corridors and future-proofing

When building linear infrastructure, the player may acquire/reserve a wider corridor than immediately needed.

Example: build one track today but reserve land/earthworks for a second track later.

Reserved corridors prevent normal city development inside them and make future expansion cheaper/easier.

## 25. Infrastructure upgrades under operation

Infrastructure is upgraded section by section.

If geometry permits, operation can continue with reduced capacity:

- one track closed while another handles bidirectional traffic,
- staged electrification,
- signalling upgrades,
- platform extensions.

Single-track routes may require full closures, work windows or construction of a parallel track first.

The project planner should show expected capacity impacts and possible diversions.

## 26. Land and demolition

Land under company infrastructure is an asset, managed by corridor/site rather than individual parcels.

Land value changes over time as cities grow.

An old depot on the edge of town can later become valuable central land.

Demolition in built-up areas is handled at project level rather than negotiating every house individually.

Projects show:

- affected buildings,
- protected structures,
- compensation cost,
- approval status,
- reputation impact.

Public-interest expropriation may be possible through the state under suitable conditions, at significant cost/reputation impact.

Brownfields/abandoned buildings are easier to redevelop.

## 27. Technology and research

Technology broadly follows historical chronology, but research can accelerate access within plausible limits.

Possible research capacity progression:

- one basic research slot,
- own research department/centre,
- external research contract,
- later additional capacity.

Technology has prerequisites.

Progression includes not only vehicles but also:

- construction methods,
- signalling,
- electrification,
- communications,
- dispatching,
- maintenance,
- business systems,
- logistics automation.

## 28. Automation and information technology

Technological progress changes how much manual management is required.

Possible progression:

- local paper-based offices,
- telegraph,
- telephone,
- centralized dispatch,
- electromechanical systems,
- computer planning,
- modern electronic ordering/API-like systems.

Automation makes a large modern company manageable without removing the underlying physical simulation.

## 29. Competitors and company market

AI transport companies are profit-seeking economic actors.

They have:

- capital,
- vehicles,
- staff,
- contracts,
- costs,
- infrastructure,
- regional presence.

They can grow, shrink, sell assets or fail.

Early competition is mostly regional. Competition increases naturally as networks and regions connect.

### 29.1 Ownership and acquisitions

The player can buy shares in competitors, receive dividends, acquire controlling stakes or buy them outright.

Acquired companies can remain independent subsidiaries or be integrated.

Companies can also own industrial firms or other business assets, but direct factory-building is not a primary early-game focus.

## 30. Carrier cooperation

Transport companies can be both competitors and partners.

### 30.1 Cargo subcontracting

A customer may contract the player for an end-to-end move, while parts are subcontracted to other carriers.

Cooperation can range from:

- one-off subcontract,
- framework partner agreement,
- reserved partner capacity,
- integrated network cooperation.

Cargo transfer remains physical through real terminals/storage.

The prime contractor remains responsible to the customer and can seek SLA compensation from a failing subcontractor.

### 30.2 Passenger cooperation

Passenger cooperation is based on fixed services and seats.

Possible arrangements:

- through-ticketing,
- sale of partner seats,
- reserved seat allocations,
- integrated transfer/rebooking arrangements.

A through journey can use multiple operators under one itinerary/ticket.

Missed connections and reliability influence passenger attractiveness.

## 31. Pricing

Early game pricing is manually controlled.

Later, pricing can be delegated to managers by scope:

- division,
- region,
- group of lines,
- specific service.

Managers can optimize within player-defined constraints such as target margin, occupancy or competitive position.

Lower-level manual settings override delegated policies.

## 32. Passenger services in the early game

Regular passenger lines are available from the start.

Low early demand means low frequencies and small vehicles may be the only profitable choice.

The player can also use demand-driven departure policies, e.g.:

- depart when X passengers are booked,
- or after a maximum wait time.

Over time, demand growth supports more frequent and higher-capacity scheduled services.

## 33. Urban transport

Supported urban modes:

- buses,
- trams,
- trolleybuses,
- metro.

Urban transport follows the same physical rules:

- real vehicles,
- depots,
- maintenance,
- staff,
- power/infrastructure,
- physical capacity.

Urban networks feed intercity stations and can materially influence passenger demand.

### 33.1 Municipal operators

Cities can own normal transport companies that behave as local competitors/operators.

A hybrid model is used:

- cities maintain a minimum service,
- municipal operators can run services directly,
- cities can tender routes, areas or entire networks to private operators.

Municipal operator scope is local: city plus agglomeration, with only limited short intercity reach where plausible.

The player can operate urban transport through a group-wide division or dedicated city subsidiaries.

## 34. Roads inside cities

Urban streets are primarily controlled by municipalities/states.

The player cannot freely redraw built-up street networks.

In undeveloped peripheral areas, construction freedom is much greater.

Major urban interventions require approval and compensation and can harm regional reputation.

## 35. Historical events and macroeconomy

History affects the transport business but does not become a war/politics strategy game.

Major events can alter:

- borders,
- licences,
- cross-border access,
- passenger demand,
- commodity demand,
- state contracts,
- material availability,
- prices,
- industrial production.

Wars/conflicts should be represented mainly through economic/regulatory consequences, not combat visuals.

Large accidents/destruction caused directly by historical events should be rare.

Economic booms and recessions should emerge as meaningful operating conditions rather than flat income modifiers.

## 36. Weather and seasons

Weather is visual and operational.

Early technology is more vulnerable to:

- snow,
- mud,
- heavy rain,
- poor roads,
- low water levels.

Technology progressively improves resilience through better surfaces, drainage, snow clearing, vehicles and forecasting.

Most weather disruption should be handled automatically and appear as delay/cost.

Rare major events can require direct player decisions:

- flood,
- severe drought,
- landslide,
- damaged bridge/track.

## 37. Safety and accidents

Major accidents are rare.

Risk is influenced by:

- vehicle condition,
- infrastructure condition,
- maintenance coverage,
- signalling/safety technology,
- traffic intensity,
- weather.

Normal neglect should produce speed restrictions, failures and closures before catastrophic accidents become likely.

Major accidents can have real consequences:

- damaged assets,
- line closure,
- repair costs,
- aggregated casualty impact,
- state scrutiny,
- reputation damage.

## 38. Finance and failure

Finance is intentionally simpler than the operational/economic simulation.

Core tools:

- cash,
- operating cash flow,
- simple bank loans.

No deep bond-market simulator is required.

Infrastructure and land can be sold to states or competitors.

A distressed company can:

- cut services,
- sell vehicles,
- sell infrastructure,
- borrow,
- request limited state emergency financing/restructuring.

Bankruptcy is a process, not an instant failure. Game over occurs only when the company is deeply insolvent with no viable assets/financing path left.

## 39. Infrastructure market

Infrastructure can be bought and sold.

A buyer may:

- continue operating it,
- offer access to other carriers,
- tender services,
- repurpose/rebuild it,
- demolish it and allow urban redevelopment.

Partial asset sales are allowed, e.g. sell the track but keep a depot or station.

## 40. Research, historical vehicles and manufacturers

Real-world trademarks/brands are avoided.

Vehicles and manufacturers are fictional but historically plausible in appearance, parameters and availability.

Manufacturers are economically present enough to make supply, capacity and backlog meaningful, without becoming a separate deep management game.

## 41. Performance non-negotiables

The game must be designed from the first prototype to scale.

Do not build a small-world architecture that assumes later optimization will fix it.

Key expectations:

- simulation LOD,
- event-driven updates,
- cached network paths/options,
- aggregated remote populations and private traffic,
- aggregate inactive-world macro simulation,
- no per-frame economic AI,
- no per-person persistent population simulation,
- no per-component vehicle maintenance simulation,
- physical continuity preserved logically even when rendering is culled.

## 42. Current out-of-scope / deferred

- Aircraft.
- Full procedural world generator.
- Deep factory ownership/building gameplay.
- Deep construction-company side business.
- Full per-person life simulation.
- Detailed mechanical component maintenance.
- Combat/war simulation.
- Scenario/campaign victory objectives.
- Mandatory expert railway timetable editor.

These may be revisited later without compromising the current architecture.

## 43. Cross-system consistency checklist

Every new feature or design change must be checked against at least:

1. Physical continuity — does anything teleport or bypass required movement/infrastructure?
2. Time progression — does it make sense in 1820 and in later eras?
3. Technology — what unlocks or improves it?
4. Economy — who pays, supplies, consumes and profits?
5. Contracts — does it create or consume transport demand?
6. Ownership/licensing — who owns it and who is allowed to use it?
7. Infrastructure capacity — where are the bottlenecks?
8. Workforce/management — who operates it and can it be delegated?
9. Reputation/public authority — are permissions or public consequences involved?
10. Simulation performance — can it run at European scale using aggregation/event-driven logic?
11. Inactive regions — does it require full simulation outside unlocked territory?
12. AI competitors — can AI companies use the same rules without cheating?
13. UI clarity — can the player understand the system without micromanagement?
14. Existing rules — does it contradict any currently agreed rule in this document?

If a conflict appears, update all affected sections before treating the feature as accepted.
