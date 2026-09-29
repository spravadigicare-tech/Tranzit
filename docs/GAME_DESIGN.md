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

Passenger demand can be seasonal, but the strength and composition of seasonality must be historically plausible. Early-game leisure/tourism demand is limited compared with later eras and should grow only as income, free time, transport accessibility, urbanization and relevant destinations develop. Seasonal passenger peaks can include holiday/leisure travel, commuting cycles, fairs/events and later mass tourism, but the game must not project modern travel behaviour backwards into 1820.

Passenger demand also has historically grounded daily and weekly rhythms. Work shifts, market days, school schedules, religious/rest days, weekends and later modern commuting patterns can shape peaks, but the profile must evolve by era rather than using one modern 24/7 template for the whole campaign.

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

Ordinary employees are aggregated rather than simulated as persistent individual people.

The workforce is split by operational role so the game stays simple without breaking facility capacity.

### 8.1 Company-wide mobile operating staff

Drivers, train crews and similar mobile operating staff are pooled **across the whole company** by qualification rather than being permanently tied to a specific region or depot.

The game tracks aggregated availability such as:

- number of qualified train drivers,
- road-vehicle drivers,
- conductors/on-board crews where required,
- licence/vehicle-type qualifications,
- usable shift/work-hour capacity.

A Trip consumes the required crew capacity for its duration. If the company does not have enough qualified staff, the Trip cannot be staffed or must be cancelled/rescheduled.

Crew capacity also respects aggregated **shift and rest requirements**. The game does not track an individual driver's sleep schedule, but longer, overnight or continuous operations consume more effective staffing capacity because legal/safe rest and crew rotation must be covered.

Long-distance or long-duration Trips can require crew changes. The service planner should show when a service needs:

- one crew for the full Trip,
- a planned crew change,
- multiple crews for continuous/night operation,
- additional onboard staff because of service class or regulations.

Crew-change requirements are handled as operational planning constraints rather than persistent individual-person simulation. The game may use defined eligible change locations such as major stations, depots or terminals, but it does not require the player to assign named ordinary employees.

The UI must translate staffing needs into understandable requirements such as:

- train-driver hours/day,
- road-driver hours/day,
- number of effective full-time crews required,
- peak crew requirement,
- additional staffing required for night/weekend patterns.

The game does **not** simulate individual crew members commuting between Praha and Ostrava or require staff-repositioning trains. This is intentionally abstracted to avoid low-value micromanagement.

Expansion into another region therefore does not require maintaining a separate arbitrary pool of drivers there, although local licences/language/regulatory requirements may still require the company to have the appropriate qualified staff category where historically/gameplay relevant.

### 8.2 Facility-bound staff

Employees whose work directly determines the capacity of a physical facility remain allocated to that facility or local operation, for example:

- mechanics/workshop staff,
- station and terminal staff,
- warehouse/loading staff,
- local office/admin staff,
- local dispatch/yard staff where the facility requires them,
- safety/security/cleaning where relevant.

This preserves existing physical systems: a workshop with too few mechanics really repairs vehicles more slowly, and an understaffed terminal really handles less cargo.

Company HR can still recruit and rebalance these employees at a higher level, and later managers can automate staffing targets.

### 8.3 Business/administrative staff

Sales, contract, HR and general administrative capacity can be aggregated at company/division/office level depending on the system they support.

Insufficient staffing creates concrete operational consequences such as slower maintenance, reduced opening hours, delayed handling, inability to cover all Trips or weaker contract-processing capacity.

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

### 10.3 Historical and seasonal demand

Commodity importance changes over time.

Examples:

- coal becomes critical in the industrial age and later declines relatively,
- oil and gas rise later,
- electricity systems alter energy demand,
- modern renewables change demand again.

Demand can also be seasonal where the underlying economy supports it. Examples include harvests, food processing, heating fuel, construction seasons and other recurring production/consumption cycles.

Seasonality must come from the actual simulated business/population context rather than flat global multipliers. Its intensity and cargo mix can change by era, region, technology and economic development.

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

Contracts can be seasonal or have seasonal volume profiles when the underlying customer demand is seasonal. A seasonal contract must show its expected calendar profile before signing, including peak months/periods, expected baseline volume and likely surge range. Historical plausibility applies: early eras should not generate modern mass-tourism or modern consumption patterns simply because the calendar says summer/winter.

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

### 11.7 Customer-driven contract expansion

A customer's real economic growth can increase transport demand during an existing relationship.

When a factory, mine, city or other customer expands production/consumption beyond the original contracted volume, it may first offer the incumbent carrier an extension or amendment to the existing contract rather than automatically creating an unrelated tender.

The offer must show:

- current contracted volume,
- new requested volume,
- whether the increase is permanent, seasonal or temporary,
- additional reserved capacity required,
- estimated additional wagons/vehicles/traction,
- terminal/storage and infrastructure impact,
- revised price/revenue,
- any change in SLA, penalties or exclusivity.

A strong relationship can give the incumbent carrier first negotiation rights or a limited response window, but never guarantees that the extra business is awarded automatically.

The player can:

- accept the expansion,
- accept only part of it,
- negotiate revised commercial terms,
- decline it.

If the incumbent declines or cannot credibly provide the additional capacity, the customer can tender the incremental volume to competitors while keeping the original contract in place where practical.

This creates natural growth paths: a small early contract can expand into a strategically important account as the customer's business grows.

Capacity feasibility uses the same transparent physical accounting as reserved-capacity commitments; the game must warn about concrete fleet, depot, terminal or infrastructure bottlenecks before acceptance.

### 11.8 Early termination and breach

Long-running contracts can end before their planned expiry.

Either side can terminate according to the contract's agreed rules, including notice periods, break clauses, breach thresholds and financial penalties.

Possible customer-side termination reasons include:

- repeated SLA failures,
- failure to provide guaranteed or reserved capacity,
- serious cargo damage/spoilage,
- repeated missed deliveries,
- regulatory or licence loss,
- insolvency or operational collapse of the carrier.

Possible carrier-side termination reasons include:

- persistent customer non-payment,
- customer failure to provide agreed minimum volume,
- unsafe or impossible operating conditions,
- loss of legal access that cannot reasonably be resolved,
- strategic withdrawal where the contract permits early exit.

Voluntary early termination without a contractual cause is possible only where the contract allows it and can trigger:

- termination fee / liquidated damages,
- repayment of bonuses or incentives where specified,
- customer relationship damage,
- relevant reputation impact,
- loss of exclusivity or preferred-carrier status.

The UI must show the expected consequences before the player confirms termination.

A breach should not cause an arbitrary immediate cancellation unless the contract explicitly allows it. Most long-term agreements should use escalating enforcement:

1. warning / breach notice,
2. cure period or corrective-action requirement,
3. contractual penalty,
4. possible renegotiation or temporary restriction,
5. termination if the breach remains unresolved or is severe enough.

Serious one-off failures can skip parts of this escalation where the contract clearly defines them as material breach.

The same rules apply to AI companies and customers; they cannot cancel contracts without a valid contractual or simulated reason.

### 11.9 Cargo batches

Cargo is simulated in batches, not per kilogram/item.

A batch tracks type, quantity, origin, destination, deadline/quality constraints and contract.

### 11.10 Multi-leg logistics

One customer contract can contain multiple transport legs and modes.

Cargo can physically wait in storage between legs.

Example:

farm → wagon → local terminal → warehouse → regional train → hub → long-distance train → local truck → customer.

### 11.11 Perishability and special requirements

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

Passenger platform function is defined by the passenger-station modules in Section 20: platform length, access, circulation and amenities affect what services the station can handle and how efficiently passengers transfer.

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

The same high-level capacity philosophy is used for constrained passenger stations: operators buy/reserve station-call slots against finite station capacity, then the station dynamically assigns the actual compatible platform for each Trip. Station-slot capacity and line-section capacity remain separate constraints and both must be available.

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

### 14.1 Physical train composition and shunting

Every locomotive and wagon is an individual asset.

Trains are physically assembled and disassembled on real track.

A consist cannot be changed through a menu without the required physical movements.

Moving wagons between sidings, platforms, loading tracks, storage tracks and assembled consists requires real **shunting movements**.

Shunting can be performed by:

- a dedicated shunting locomotive/vehicle,
- a normal line locomotive temporarily taken away from line work,
- period-appropriate simpler methods in very early/small facilities where plausible.

Dedicated shunters are physical fleet assets with their own location, fuel/energy use, maintenance state and parking requirement.

The player does not need to micromanage every coupling action by default. A yard/dispatcher can generate and execute the necessary shunting plan automatically, but the locomotives, wagons, tracks and movements must still physically exist.

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

### 14.4 Locomotive exchange and local traction bases

A long-distance Service Pattern may change locomotives en route, but a locomotive exchange should only exist where it is operationally justified by **local traction availability**.

Typical valid reasons include:

- electrified section changing to non-electrified section,
- incompatible electrification system,
- major traction/performance requirement change,
- route-specific technical or regulatory compatibility,
- historically plausible operating practice where a local traction base serves a distinct corridor.

A planned exchange point must have a suitable **local operating/dispatch depot or traction base** with compatible locomotives physically available for that onward segment, or another equivalent nearby facility that can realistically stage them.

The planner should not recommend an exchange where both locomotives would have to deadhead from the same distant depot just to swap places. In that case the exchange normally adds pointless movements and should be rejected unless another explicit operational constraint makes it necessary.

For a planned exchange, the local onward locomotive is normally staged from its own nearby depot/pool. The incoming locomotive is then:

- sent to local parking/service,
- reassigned to another local Trip,
- or later returned through useful work/repositioning.

The locomotive exchange is a physical station/yard operation:

1. train arrives on a suitable track;
2. incoming locomotive uncouples and physically clears the consist;
3. onward locomotive physically approaches and couples;
4. required checks/preparation occur;
5. the Trip continues.

The exchange consumes real track/yard capacity and adds dwell time.

The Service Pattern planner can automatically suggest valid exchange points only when all of the following are true:

- onward traction is actually required or materially advantageous,
- the station/yard geometry supports the operation,
- a suitable local traction base exists,
- the regional pool can credibly provide the required onward locomotive,
- the added dwell and shunting capacity are accounted for.

If no valid local traction base exists, the system should normally recommend one of:

- use a locomotive capable of the entire route,
- build/establish a **small standalone traction base** at a suitable point,
- upgrade an existing parking/operating facility with traction-base modules,
- change the route,
- shorten the service,
- use another compatible traction solution.

Later technologies such as multi-system, dual-mode or otherwise more versatile vehicles can remove exchange points and thereby reduce dwell time, fleet complexity and station capacity usage.

### 14.5 Passenger classes and comfort

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

Vehicles must physically travel to an appropriate **maintenance facility** for service.

Maintenance facilities are distinct from ordinary parking/storage facilities. A location may provide both functions, but this is not required.

A vehicle or vehicle group can have an assigned/preferred maintenance facility, with allowed fallbacks where configured. The assigned facility must actually support the required vehicle type and maintenance level.

If a workshop is full, vehicles wait physically in yards/parking or at another valid holding location.

Remote fleets without nearby maintenance suffer real downtime because vehicles must travel farther for inspections and repairs.

Self-propelled vehicles travel to maintenance under their own power when their condition and route permit it.

Non-powered rail vehicles such as passenger/freight wagons must be **physically hauled to maintenance** if the workshop is not located in the same yard.

The preferred transfer hierarchy is:

1. use an available compatible line/transfer locomotive from the relevant depot or regional pool;
2. consolidate multiple wagons requiring the same transfer where practical;
3. if no suitable line locomotive is available, a compatible shunting locomotive may perform the transfer as a fallback.

Using a shunting locomotive outside normal yard work is deliberately inefficient. Compared with a line locomotive it can have:

- much lower maximum speed,
- lower practical towing capacity,
- fewer wagons per transfer,
- greater journey time,
- higher disruption per transported wagon,
- restrictions on which main-line routes it may legally/technically use.

A slow maintenance transfer occupies real track sections/slots and can therefore reduce corridor capacity or delay other trains. The planner must show this consequence before dispatch where material.

A shunter fallback is allowed only when the specific locomotive and route are technically and legally compatible; the game must not use it as a universal escape hatch.

If no valid locomotive can haul a wagon to the assigned maintenance facility, the wagon remains out of service until suitable traction or another valid maintenance solution is available.

After service, the vehicle/wagon must also physically return to an operational or parking location; it does not teleport back to a line or pool.

### 16.3 Operational failures and rail recovery

Most vehicle faults should **degrade operation rather than immediately immobilize the vehicle**.

Typical non-critical locomotive/vehicle faults can cause:

- reduced maximum speed,
- reduced traction/power,
- higher fuel/energy consumption,
- reduced reliability for the remainder of the Trip,
- loss of some comfort/service equipment,
- a requirement to visit maintenance after completing the current reasonable operating task.

If the train can still move safely, the preferred behaviour is to finish the current delivery/service where practical, unload/drop off passengers or cargo as planned, and then travel physically to a suitable maintenance facility.

The UI and dispatcher must make the degraded state visible and may recommend withdrawing the vehicle earlier when continuing would create excessive risk or disruption.

A fully immobilizing failure on the main line is intentionally rare.

When a locomotive/train becomes unable to move:

1. the affected track section becomes physically blocked;
2. dispatching checks whether other trains can route around the obstruction;
3. if there is no usable bypass or passing route, trains already committed toward the blockage may have to stop and **reverse/back out to the nearest suitable station, siding, crossover or junction** to clear the corridor;
4. a compatible rescue/recovery locomotive must physically travel to the failed train;
5. the failed locomotive or entire consist is then physically hauled to the nearest suitable safe location or maintenance facility.

Recovery traction can come from:

- an available line/transfer locomotive,
- another compatible locomotive reassigned from nearby service,
- a shunting locomotive only as a constrained last-resort option where route, speed and towing limits permit.

The dispatcher should choose a recovery plan that minimizes total network disruption, but it cannot teleport trains, ignore directionality or pass through occupied track.

Backing/reversing movements must respect train direction, signalling/infrastructure and available crossovers. If the current consist cannot reverse normally, the recovery plan may need another locomotive attached at the opposite end or another physically valid movement.

A blocked single-track section can therefore create real knock-on disruption until the failed train is removed. Double-track or bypass infrastructure can greatly reduce the impact.

Because severe immobilizations are rare, the player should not routinely micromanage rescue operations. Dispatch automation can generate the recovery plan, while the player is shown:

- where the blockage is,
- which services are affected,
- selected rescue locomotive,
- estimated clearance time,
- any trains that must reverse/reroute,
- expected capacity and delay impact.

Poor maintenance, severe faults or extreme conditions can increase the chance of an immobilizing failure, but normal well-maintained operation should make such events exceptional.

### 16.4 Infrastructure maintenance

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

### 17.1 Regional fleet pools and facility roles

Operational vehicles are not normally hard-bound to one Line. By default, compatible vehicles belong to a **regional fleet pool** and dispatching assigns actual assets to Trips as needed.

The dispatcher must choose from real physical assets and consider:

- current vehicle location,
- compatibility with the Service Pattern,
- passenger/cargo capacity,
- traction and route feasibility,
- maintenance condition and upcoming service,
- fuel/energy requirements,
- reserved-capacity commitments,
- deadhead/repositioning distance and time,
- parking/yard capacity,
- maintenance-facility capacity,
- other already-assigned Trips.

Tranzit distinguishes three facility roles:

1. **Operating/dispatch depot** — configured primarily on a Line or Service Pattern; this is where the service is normally staged, dispatched, turned around or recovered.
2. **Parking/storage facility** — where an idle vehicle or wagon can physically stand when it is not needed in active service.
3. **Maintenance facility** — where the vehicle is physically sent for inspections, servicing or repair.

For rail operations, an operating/dispatch depot can also act as a **local traction base** for locomotive exchange. This means it keeps suitable locomotives physically available to work onward segments from that location.

A traction base can also be built as a smaller standalone facility. It is cheaper and simpler than a full depot and is intended for local locomotive staging rather than heavy maintenance.

A basic traction base can include:

- a small number of locomotive parking/staging tracks,
- access/turnaround track geometry,
- period-appropriate fuel, coal or water supply where required,
- basic crew/operational facilities,
- light inspection or minor servicing only where the selected module supports it.

It does **not** automatically provide:

- heavy maintenance,
- large workshop capacity,
- wagon repair,
- major overhauls,
- extensive storage yards.

A typical early or mid-game traction base may hold only 2–4 locomotives. Its purpose is to support locomotive exchanges, helper/banking operations, rescue coverage or a remote cluster of Lines without forcing the player to build a full maintenance depot.

Locomotives based there still need a separate compatible maintenance facility for heavier scheduled work and must physically travel there when service is due.

The same modular principle applies to **road-vehicle operating bases**.

A small road base can provide only what a local bus/truck fleet actually needs, for example:

- physical parking spaces,
- basic dispatch/crew facilities,
- period-appropriate fuel storage/pumps or later charging infrastructure,
- washing/basic inspection where installed.

It does **not** require a full mechanical workshop.

Heavier scheduled maintenance and repairs can be centralized in a larger regional road maintenance facility. Buses/trucks must physically drive there when service is due, creating real downtime and travel cost.

This makes it viable to operate several cheap local parking/dispatch bases around a region while maintaining one larger workshop, instead of forcing the player to duplicate expensive maintenance infrastructure everywhere.

A small road base can later be upgraded modularly with:

- more parking,
- fuel/charging capacity,
- light-service bays,
- full workshop modules,
- spare-parts storage.

**Tram, trolleybus and metro depots/garages are different:** their basic depot type always includes a minimum workshop/maintenance capability. The player does not build a pure parking-only depot for these modes.

A basic tram/trolleybus/metro depot therefore includes:

- vehicle storage/parking,
- dispatch access,
- basic inspection and routine maintenance workshop capacity,
- required power infrastructure for the vehicle type,
- basic operational staff facilities.

Metro depots must also be physically connected to the metro network they serve.

Larger/heavier maintenance capacity can still require expansion modules or a larger central workshop, but every tram/trolleybus/metro depot can perform routine service by default.

One site can provide more than one role, but it does not have to. A cheap road parking yard therefore does not need a full workshop, and a regional road fleet can share a more distant maintenance base.

A Line or Service Pattern can define:

- preferred/primary operating depot,
- one or more allowed fallback operating depots,
- required operating depot where operationally necessary.

Vehicles/rolling stock can separately define:

- preferred parking facility,
- preferred maintenance facility,
- allowed fallback facilities.

To avoid micromanagement, parking and maintenance assignments can be inherited from a regional pool, vehicle class or fleet group, with optional overrides for individual assets.

These assignments are planning preferences, not teleport destinations. The actual physical location of every asset remains authoritative.

A vehicle allocated from another location must physically deadhead/reposition to the service start, consuming time, infrastructure capacity, fuel/energy and potentially crew resources.

When a Trip finishes, the dispatcher may keep the asset near the next useful work rather than forcing an unnecessary return to a parking facility. If it becomes idle, it must eventually occupy a real valid parking/storage location.

When maintenance becomes due, the asset must physically travel to a suitable maintenance facility. It does not matter whether that facility is the same site used by the Line for operations or parking.

Parking and workshop capacity are real. If a facility is full, additional assets cannot be hidden inside it.

Dispatch automation must not double-book assets, exceed physical parking/workshop capacity or silently consume capacity reserved for contracts. If a timetable cannot be covered, the planner must explain the concrete shortage.

### 17.2 Shunting capability

Any rail depot, yard or freight/passenger facility that regularly assembles, disassembles or rearranges consists needs sufficient **shunting capability**.

A larger active operating depot should normally have at least one dedicated shunting locomotive/vehicle available. Larger yards may need several, and shunting capacity can become a real bottleneck.

Very small or early facilities may operate without a dedicated shunter by using a line locomotive or historically appropriate simpler methods. This is allowed, but it consumes line-locomotive time and reduces operational efficiency.

Shunting workload is driven by real activity such as:

- attaching/detaching passenger or freight wagons,
- moving wagons to loading/unloading tracks,
- transferring vehicles to storage tracks,
- moving locomotives to fuel/water/service facilities,
- re-forming consists for different Trips,
- moving vehicles in/out of workshops.

The UI should expose a clear yard/depot capacity indicator such as expected shunting workload versus available shunting capacity, rather than forcing the player to schedule each movement manually.

If shunting capacity is insufficient:

- consist preparation takes longer,
- departures can be delayed,
- loading tracks/sidings stay occupied longer,
- line locomotives may be borrowed for shunting if the player allows it,
- the planner should identify shunting as the actual bottleneck.

Shunting capability evolves historically. Later technologies can reduce labour/time requirements and introduce more efficient dedicated shunters or yard equipment, but physical movement is never replaced by teleportation.

Dedicated shunters are usually assigned to a facility/yard rather than to a passenger or freight Line. They still need parking and maintenance facilities under the same physical rules as other vehicles.

Shunters can also be used as a **fallback wagon-transfer locomotive** for maintenance or other necessary local repositioning when no suitable line/transfer locomotive is available. This removes the shunter from normal yard work for the duration of the trip and therefore reduces shunting capacity at its home facility.

Because shunters are optimized for yard work rather than main-line hauling, such transfers are slow and limited in train length. They consume real main-line capacity and can become an intentionally visible operational penalty for under-investing in suitable transfer traction or maintenance coverage.

## 18. Energy and operating supplies

Fuel and many operating supplies are real goods.

Examples:

- coal,
- diesel/petrol,
- water,
- lubricants,
- parts,
- catering supplies.

Road operating bases may therefore need real fuel deliveries, or later sufficient electrical charging/grid capacity, depending on the vehicles assigned there.

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

A private infrastructure owner can reserve part of its capacity for its own services before offering the remainder to other operators.

However, depending on country, era, licence terms and infrastructure importance, the state/regulator can impose **open-access obligations** on strategically important private infrastructure.

Open-access rules can require the owner to:

- make a minimum share of usable capacity available to third parties,
- publish transparent access prices,
- avoid discriminatory refusal where compatible capacity exists,
- preserve emergency/public-service access,
- participate in capacity allocation or dispute-resolution rules.

The exact obligation is a legal/regulatory property of the infrastructure and jurisdiction, not a universal rule for every private siding or local station.

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

Passenger stations are **modular physical facilities**, not single abstract buildings.

A passenger rail station can be assembled from functional elements such as:

- platform tracks,
- passenger platforms of configurable length,
- station/entrance building,
- waiting areas,
- ticketing/booking facilities where historically relevant,
- shelters/canopies,
- toilets and basic amenities,
- pedestrian access paths,
- stairs/ramps,
- footbridges or underpasses,
- concourse/transfer halls,
- baggage/service facilities,
- later retail/commercial modules,
- parking and P+R,
- taxi/drop-off space,
- adjacent bus/tram/trolleybus/metro interchange modules.

Not every station needs every module. A rural halt can be extremely simple, while a major hub can grow into a large multi-modal complex.

Station capability and passenger experience emerge from its real modules and layout.

Relevant station effects can include:

- maximum train length served,
- number of simultaneous trains,
- passenger throughput,
- transfer walking time,
- boarding/alighting speed,
- shelter/comfort,
- ticketing/processing capacity,
- accessibility,
- interchange quality,
- operating/staff requirements.

Platform length is physical. A train that is longer than the usable platform cannot be treated as fully accommodated without an explicit operational rule/penalty.

Passenger circulation matters at an aggregated level. The game does not need to simulate every person through every doorway, but station design should calculate practical flow constraints from entrances, platforms and connections. Representative visible pedestrians should follow the actual layout.

A station can therefore become a bottleneck even when the surrounding railway still has track capacity.

### 20.1 Passenger station progression

Available station modules evolve with history and technology.

Early stations can rely on small buildings, simple platforms and manual ticketing.

Later eras can unlock:

- larger covered platforms,
- improved passenger circulation,
- underpasses/footbridges,
- electric lighting,
- modern information systems,
- escalators/lifts where appropriate,
- automated ticketing,
- integrated urban-transport interchanges,
- larger commercial/concourse facilities.

A station can evolve in two main ways:

1. **Extension / modular growth** — keep the existing station building and add new halls, wings, platforms, circulation links or interchange modules around it.
2. **Full replacement** — demolish the existing main station building or selected major station modules and construct a larger/newer replacement.

Full replacement is a real construction project, not an instant upgrade. It can require:

- demolition time/cost,
- construction materials and contractor capacity,
- temporary passenger access or temporary station facilities,
- reduced station throughput during construction,
- temporary closure of affected entrances/platforms where necessary,
- municipal/state approval where the site is regulated,
- heritage approval or prohibition if the original structure is protected.

The project planner should show how much of the station can remain operational during each construction stage.

The player can optionally purchase **construction mitigation measures** to reduce the negative impact of the rebuild. These are project-level choices rather than separately micromanaged temporary networks.

Possible mitigation measures include:

- temporary passenger platforms,
- temporary entrance/ticketing building,
- temporary pedestrian routing,
- temporary bus replacement/shuttle service,
- staged platform closures,
- temporary interchange relocation,
- additional contractor shifts/work windows where available.

Each measure has a clear cost and effect, such as:

- higher temporary passenger throughput,
- smaller transfer-time penalty,
- lower reputation impact,
- fewer cancelled Trips,
- shorter effective disruption window.

The UI should compare the expected station impact **with and without** each mitigation option before the player approves the construction plan.

Temporary facilities are physically represented where practical, but their detailed internal management is automated. After the project is complete they are normally removed automatically unless the player explicitly chooses to retain a useful element.

A replacement project does not automatically demolish the whole railway site. Tracks, platforms, buildings and interchange modules can be retained or rebuilt independently where the design permits.

Upgrading a station therefore does not automatically erase its historic fabric. Existing buildings/platforms can remain, be extended, repurposed, replaced or protected depending on the site and era.

Where an old station building is preserved, it may remain as an entrance, secondary hall, commercial space or heritage element inside a much larger modern station complex.

### 20.2 Multimodal interchange

Urban and intercity transport should connect through real station geometry.

A bus terminal, tram stop, trolleybus stop, metro entrance, taxi area or P+R facility can be attached to or placed near a rail station.

Transfer quality depends on actual walking distance, access routes, waiting environment and timetable coordination.

A transfer is therefore better when modes are physically integrated than when passengers must cross a large area or street network.

### 20.3 Station capacity, ownership and access charges

Station capacity is distinct from line/track-section capacity.

A station may be constrained by:

- platform occupancy,
- platform length,
- throat/junction conflicts,
- passenger-flow capacity,
- baggage/cargo handling where relevant,
- shunting/turnaround requirements,
- interchange capacity.

The UI should identify the actual station bottleneck rather than expose one generic capacity percentage.

Station owners can charge other operators for relevant use.

Station access normally has **two commercial components**:

1. **Capacity reservation / station-slot fee** — payment for the right to schedule a defined number of station calls in specified time windows.
2. **Actual usage fee** — charged when the Trip really uses the station and may depend on service type, train length, dwell time and used station services.

Additional charges can apply for:

- terminal services,
- storage/handling,
- interchange facilities,
- shunting/turnaround services,
- exceptional long dwell or overnight occupation where relevant.

A station-call slot is a right to station capacity, **not ownership of a numbered platform**.

### 20.4 Station slots and dynamic platform allocation

Passenger platforms are normally allocated **dynamically to Trips according to station capacity and compatibility**, rather than permanently belonging to one operator.

A station can therefore serve several operators at the same time as long as its real infrastructure can accommodate their services.

Before a regular Service Pattern is activated at a constrained station, the operator normally needs enough **station-call slots** for the planned calls.

Slots are sold/reserved against the station's calculated usable capacity by time window, for example:

- peak-hour calls,
- off-peak calls,
- daily/weekly bundles,
- seasonal service windows.

The station owner cannot sell unlimited slots. The capacity planner maintains:

- safe/usable station-call capacity,
- capacity reserved by the owner for its own services,
- capacity protected for regulatory/open-access obligations where applicable,
- already committed guaranteed third-party capacity,
- standard/flexible commitments,
- operational reserve for disruption where configured,
- remaining sellable capacity.

A private owner can deliberately reserve part of the station's capacity for its own Lines/Service Patterns. Those self-reserved slots consume real station capacity exactly like third-party slots and therefore reduce what can be sold externally.

At regulated or strategically important stations, the state/regulator may require a minimum amount or share of station-call capacity to remain available for third-party operators. The owner cannot reserve or sell that protected capacity in a way that violates the rule.

Peak capacity can therefore become scarce and more expensive.

A Service Pattern with four guaranteed morning calls consumes four relevant capacity rights from that time window even though the actual numbered platform is assigned dynamically later.

The station allocator considers factors such as:

- platform length,
- current and planned platform occupancy,
- arrival/departure direction and accessible track geometry,
- through platform versus terminating/bay platform suitability,
- electrification/traction compatibility where relevant,
- required passenger facilities,
- expected dwell time,
- turnaround/shunting needs,
- throat/junction conflicts,
- contractual access priority.

Operators primarily contract for **station-call capacity**, not necessarily for one permanently numbered platform.

Access agreements can provide different slot products, for example:

- **guaranteed slot** — the owner must provide a compatible platform within the agreed operating window; highest reservation price;
- **standard slot** — normal scheduled access with less contractual protection during major disruption;
- **flexible/ad-hoc slot** — cheapest; used only when spare capacity exists and can be retimed or rejected when the station is constrained.

Unused guaranteed/standard slots still have a reservation cost because the owner has withheld that capacity from other operators.

An operator without a pre-purchased slot may request an ad-hoc call. It is accepted only if real spare station capacity exists, usually at a higher per-call price or with lower priority.

A dedicated platform can still exist as an exceptional contractual or infrastructure rule where operationally justified, but it is not the default model.

The access-planning UI should show, by relevant time window:

- total usable station capacity,
- capacity reserved for the owner's own services,
- regulatory/open-access capacity protected for third parties where applicable,
- already reserved third-party calls,
- remaining sellable slots,
- player's currently owned/reserved slots,
- expected per-call usage charges,
- expected peak congestion,
- the concrete constraint that limits further sales if capacity is exhausted.

If a third-party request is rejected, the UI must state whether the reason is genuine capacity/compatibility, contractual priority, or another explicit rule. A regulated owner cannot hide discriminatory refusal behind an unexplained generic "no capacity" result.

This prevents hidden oversubscription: if the station is effectively full in the 07:00–08:00 window, neither the player nor an AI operator can buy another guaranteed peak slot unless capacity is expanded or another commitment is released.

The allocator should assign a concrete compatible platform when planning/dispatching each Trip. If disruption makes the planned platform unavailable, it can automatically reassign the train to another valid platform.

Dynamic reassignment must still respect physical track access. The game cannot assign a train to a free platform that the train cannot physically reach without conflicting movements or invalid direction changes.

If no compatible platform is available, the train must:

- wait outside/at an approach signal,
- use another permitted station/stop if the Service Pattern allows it,
- be retimed/rerouted by dispatching,
- or have the Trip disrupted/cancelled as a last resort.

The UI should show station utilization and explain why a Trip is waiting, for example: "no compatible 300 m platform available" or "station throat conflict".

To preserve performance, platform allocation is event/schedule driven: it is recalculated when Trips are planned, approach the station or when a relevant disruption/infrastructure change occurs, not continuously every frame.

Rail infrastructure capacity remains strategic rather than requiring a full expert timetable simulator by default.

The UI should communicate section and station utilization clearly, including peak bottlenecks.

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

Large reconstruction projects can also offer optional **operational mitigation packages**. These are higher-level project options that reduce disruption through temporary facilities, staged closures or substitute transport rather than forcing the player to manually build every temporary element.

Mitigation consumes extra money, contractor capacity and sometimes temporary land, so the player chooses between a cheaper disruptive rebuild and a more expensive construction plan that preserves more operating capacity.

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

Demolition rules also apply to the player's own infrastructure. Replacing an existing station building, depot structure or terminal module requires an explicit demolition/redevelopment project rather than an abstract upgrade. If the structure is protected, demolition may be prohibited or require exceptional approval even when the player owns it.

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

## 32. Service lines and timetables

Regular passenger lines are available from the start, and freight services can use either scheduled or demand-driven operating patterns.

Low early passenger demand means low frequencies and small vehicles may be the only profitable choice.

The player can also use demand-driven departure policies, e.g.:

- depart when X passengers are booked,
- depart when minimum cargo load is reached,
- depart when a contracted shipment is ready,
- or after a maximum wait time.

Over time, demand growth supports more frequent and higher-capacity scheduled services.

### 32.1 Service hierarchy: Line → Service Pattern → Trip

All scheduled transport uses a three-level hierarchy:

1. **Line** — the commercial/operational corridor or service family the player manages as one unit.
2. **Service Pattern** — a specific operating variant of that line: route, stop pattern, calendar, vehicle requirements and service rules.
3. **Trip** — one concrete physical movement on a specific date/time using real assigned vehicles/consists.

Example:

- Line: R1 Praha–Brno
  - Pattern: Local — serves all selected intermediate stops
  - Pattern: Express — serves only major stops
  - Pattern: Short-turn — terminates at an intermediate point
  - Pattern: Night/seasonal — different calendar and consist rules
- Trips: the actual 06:00, 08:00, 10:00 departures generated from those patterns.

Lines aggregate business and operating performance across their patterns. Patterns remain individually inspectable for profitability, occupancy, reliability, fleet demand and timetable quality.

The same hierarchy applies to passenger and freight services. Freight patterns can differ by cargo focus, stop logic or demand-driven departure rules.

A Service Pattern should still meaningfully belong to its parent Line. If a proposed variant shares too little route, purpose or operating identity with the parent, the UI should recommend creating a separate Line instead of allowing one line to become an arbitrary container for an entire network.

### 32.2 Service calendars

A line can contain multiple repeating service patterns instead of one permanent timetable.

Each service pattern can define:

- validity period/date range,
- days of week,
- exact departure times and/or repeating intervals,
- time-of-day windows,
- capacity/vehicle requirements,
- optional departure conditions for demand-driven freight/passenger services,
- exceptions such as holidays, temporary closures or special-event service.

Example patterns can include weekday, weekend, summer, winter or harvest-season service.

Early-game services can use sparse exact departures such as Monday/Thursday or one/two departures per day. Later high-frequency rail/urban services can use interval-based patterns.

Service calendars must respect actual physical fleet availability. Before activation, the planner calculates the number and type of vehicles/consists required from real cycle times, turnaround, depot movements and maintenance assumptions. If the fleet cannot cover the timetable, the game must explain the shortage rather than creating abstract vehicles.

Timetable templates may later be reused across multiple lines, with local overrides. Managers/dispatch systems can suggest frequency changes based on observed demand, but player overrides remain possible.

### 32.3 Feeder and connection relationships

Connections should normally be planned at **Line or Service Pattern level**, not by manually linking every individual Trip.

The player can declare that one line or service pattern:

- feeds another line,
- should receive passengers from another line,
- should coordinate bidirectionally around a hub.

The timetable planner then calculates suitable departures using:

- actual travel time,
- transfer walking/handling time,
- desired transfer buffer,
- historical reliability/delay distribution,
- service frequency,
- physical vehicle availability.

Example: the player marks a regional bus as a feeder for a specific rail service. The system schedules the bus to arrive early enough for a reliable transfer rather than requiring the player to set every bus arrival manually.

The player can set high-level preferences such as:

- target transfer buffer,
- maximum acceptable wait,
- whether the feeder may wait for a delayed connection,
- which connection has priority.

The system must show the resulting expected transfer quality and any fleet/capacity consequences.

Later dispatching and information technology can automate connection coordination more effectively, but physical travel and actual delays remain real. A connecting vehicle cannot teleport or ignore infrastructure constraints simply because services are linked.

### 32.4 Line-level stop service modes

Stop behaviour is configured on the **Service Pattern** (with optional defaults inherited from its Line), not on the station itself.

A station/terminal only exposes its physical capabilities and access rules. Each line that uses it independently defines how that line should serve the location.

This allows the same station to be:

- mandatory for one regional line,
- conditional/on-request for another line,
- skipped by an express service,
- pass-through only for a freight service.

For each stop entry in a Service Pattern, supported modes include:

- **Mandatory:** this line always calls there when the trip runs.
- **Conditional:** this line calls only when a defined condition is met.
- **On request / booked:** this line skips the stop unless there is real passenger booking, cargo work, pickup/drop-off demand or another configured trigger.
- **Pass-through only:** this line may traverse the station/terminal infrastructure but performs no commercial stop there.

Typical line-level conditional triggers can include:

- passengers booked to board/alight,
- cargo batch assigned for pickup or delivery,
- minimum cargo quantity reached,
- contract-required call,
- operational need such as crew/service activity where applicable.

Freight services should normally skip intermediate freight terminals when that specific service has no assigned work there. This avoids unnecessary dwell time and keeps line capacity usage realistic.

Passenger request stops can be appropriate for low-demand local services, especially in early eras or rural areas. The system should only activate the stop when real underlying demand exists rather than through cosmetic randomness.

Timetable planning must account for both cases:

- base running time when the line skips the stop,
- additional dwell/handling time when that line serves it.

For regular planning, the UI should show expected/typical trip time and a reasonable worst-case or high-load trip time so the player understands how the line's conditional stops affect connections and fleet requirements.

Feeder/connection planning must use the actual expected stop pattern of the relevant lines/service patterns and enough buffer to avoid creating impossible transfers when several conditional stops activate.

Dispatch automation can later decide individual conditional calls automatically within the rules of that line, but the player must always be able to inspect why a specific trip stopped or skipped a location.

### 32.5 Vehicle assignment from fleet pools

Trips normally receive concrete vehicles/consists dynamically from the relevant regional fleet pool rather than from permanently fixed vehicle-to-line assignments.

A Line or Service Pattern can still define:

- required vehicle capabilities,
- preferred consist family/type,
- preferred or required **operating/dispatch depot**,
- fallback operating depots,
- minimum reserve policy.

Parking and maintenance are separate from the Line's operating depot. Individual assets or their fleet group can have separate parking and maintenance facility preferences.

The timetable planner must include real depot-to-service positioning, parking needs, maintenance windows and necessary repositioning movements when calculating required fleet size and feasibility.

If a Service Pattern includes locomotive exchange, the planner must also validate that each exchange point has suitable local traction capacity. It must not assume a replacement locomotive can appear from nowhere or make two locomotives perform pointless long-distance deadheads from the same depot.

A specific vehicle may be manually pinned to a Line/Pattern as an override where the player wants that level of control, but this is not the default operating model.

### 32.6 Crew requirement planning

Service planning must validate both vehicle availability and aggregated crew capacity.

For each Service Pattern, the planner estimates:

- total operating hours,
- peak simultaneous crew demand,
- day/night/weekend staffing burden,
- whether crew changes are required,
- suitable locations for those changes where applicable,
- spare crew margin after the timetable is activated.

The planner should warn when a timetable is technically possible with vehicles but cannot be covered by available qualified staff.

Later managers can automatically adjust staffing targets or propose timetable changes, but they cannot create crew capacity that the company does not actually employ.

Crew planning remains aggregated across the company and does not introduce individual employee pathfinding or home-depot assignment.

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

For tram, trolleybus and metro operations, a basic depot/garage always contains routine workshop capability; parking-only facilities are not the default depot type for these modes.

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
