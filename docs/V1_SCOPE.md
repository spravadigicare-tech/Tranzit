# Tranzit — V1 scope and cross-system rules

Status: implementation specification prepared on 2026-09-30. This is a specification, not a claim that a playable build exists.

Read with [GAME_DESIGN.md](GAME_DESIGN.md) and [CONTRACT_CANCELLATION.md](CONTRACT_CANCELLATION.md). The full game design remains the long-term specification. This document defines the first playable release subset and elaborates the decisions confirmed during the V1 discussion. It does not replace the existing operational, contractual or physical rules.

## 1. Approved first-playable scope

| Area | First playable V1 |
|---|---|
| Product | A genuinely playable transport/business game, not a technology demonstration, UI mockup or collection of isolated systems |
| Platform | Windows desktop; keyboard and mouse; offline play |
| New-game date | 1900 only; 1925, 1950 and 1975 remain later base-game start presets, not deleted design goals |
| Progression | The common calendar continues after 1900. A single starting preset does not freeze technology, economics or historical progression in 1900 |
| Modes | Rail freight, rail passengers, road freight, intercity buses and local bus operations |
| Excluded V1 modes | Water transport, trams, trolleybuses, metro and aircraft. The first four retain their place in the wider design; aircraft remain outside current scope |
| World | All territory corresponding to present-day Czechia plus adjoining parts of Germany, Poland, Austria and Slovakia; active-region unlocking and the inactive macro world remain functional |
| Geography | Real settlement locations, rivers and relief; a historically plausible authored 1900 world, not an exact reconstruction of every historical property |
| Names | Real cities/landmarks; fictional transport companies, commercial firms, manufacturers and vehicle brands; familiar Czech city names in Czech UI |
| Existing world | Working third-party/public roads, railways, stations, firms and competitors already exist at game start |
| Player start | Small, mode-neutral company financed by one of three favourable founding loans; no free branch, fleet or depot |
| Currency | One accounting unit, literally `money`; no currency symbols, historical currency switching or foreign-exchange subsystem |
| Language | Complete Czech and English UI; stable English code/data IDs; localization from the start |
| Presentation | Cohesive 3D stylized realism/model-world appearance; recognizable vehicles, architecture, terrain, infrastructure and physical operations |
| AI | Real competing carriers with money, vehicles, staff, infrastructure, contracts and constrained operations; no fabricated bids or unlimited resources |
| Persistence | New Game, Continue, manual slots, autosave, quicksave and quickload; complete simulation persistence |
| Completion | Every applicable main mechanic is playable through UI, linked to the simulation and tested; cover normal failures and meaningful edge cases, not only the happy path |

Single-player without an account/server dependency is the engineering default for this offline first build. Multiplayer is not an added V1 requirement.

## 2. Construction scope

Rail construction includes free-form splines, junctions/switches and valid crossings, multiple tracks, passenger platforms/stations, freight terminals, industrial sidings, operating/parking yards, depots, workshops, run-around facilities, turntables/triangles, bridges, tunnels and signalling. Electrification and corresponding equipment follow their actual technology availability; do not globally unlock future equipment at the 1900 start.

Road play primarily uses the existing public road network. Player construction includes appropriate depots/garages, maintenance and parking, passenger stops/terminals, cargo endpoints and short private/access roads. V1 does not require a player motorway-construction game or unrestricted redesign of existing urban streets. The public network must nevertheless be operational, connected and affected by genuine restrictions and congestion.

Building remains a real project: land/access, permissions, contractor capacity, cost, duration, materials, physical stages and the operational impact of closures are not bypassed. A construction preview is not a completed asset. A cancelled unbuilt preview is not a paid demolition.

## 3. One time and distance model

Retain GAME_DESIGN Section 3 as the authoritative clock:

- 60 simulation seconds/minute, 60 minutes/hour, 24 hours/day;
- 7 days/week, 14 days/month, 12 months/year, 168 days/year;
- at 1x, one real second advances one game minute;
- running speeds 0.5x, 1x, 2x, 4x, 8x and 16x, plus pause;
- no separate accelerated year clock, skipped operating days or speeds above 16x.

Distance and operating speed determine the trip duration in simulation units. The time ratio does not, by itself, define a spatial scale. Use geographic route lengths in metres and calculate segment time from actual operating performance, restrictions, acceleration/braking and dwell. Render that same movement, not another slower representation with a separate arrival clock.

Implementation default: authoritative geographic/projected positions and route lengths use double-precision metres; Unity rendering uses local metre-scale coordinates with origin rebasing and streamed chunks. Rebasing changes only the presentation origin, never the distance ledger or asset location.

Analytical fixture: a 60 km segment at a constant 60 km/h with no stops/acceleration takes one game hour. That is 60 real seconds at 1x, 120 at 0.5x and 3.75 at 16x. These are unit-test expectations, not promised frame-rate measurements.

Vehicle movement, preparation, transfers, crews, production, maintenance, construction, billing, interest, research, contracts and history consume this same clock. A short track section or coupling operation may finish within a rendered frame at high speed; the simulator must still process its ordered events and occupancy boundaries.

Pause and application focus are separate from time speed. The default is no simulation advancement while paused and no offline catch-up after closing the game. UI, camera, loading and save timers may use real time because they do not create simulated economic activity.

### Historical date input

The core design correctly leaves the exact real-date conversion to content authoring. Before importing a historical event outside days 1–14, choose and explicitly document the conversion in GAME_DESIGN Section 3.4 and the data-pipeline specification. This is a routine implementation convention, not another product question for the user. Preserve original source dates, validate them first and store valid game dates separately. Events mapped onto the same game day need deterministic order and explicit prerequisites. No consumer may silently fall back to Gregorian runtime billing or create invalid game days. This handoff does not claim that a particular conversion formula has already been approved.

## 4. Historical vehicles remain usable and discoverable

The user explicitly requested no artificial end of vehicle availability. A model has an introduction date, but not a hard retirement date that removes it from the catalogue or disables existing assets.

Keep separate:

1. technology/model existence;
2. physical assets already in the world;
3. finite dealer/used inventory;
4. actual manufacturing or special-order offers;
5. maintenance capability and parts/support availability;
6. technical, safety and route compatibility.

Once introduced, a model stays searchable. Existing assets can be owned, resold, repaired and operated indefinitely while technically serviceable and compatible. Do not make a calendar rollover delete a model, expire its technology or force scrapping. If there is no available seller or manufacturer, show `no current offer`, not `unavailable after year X`.

Ordinary new production of an old model can decline or end through manufacturer economics and capability; that is not a global purchase ban. Used stock comes from real assets. Where a manufacturer retains the relevant capability, new/special-order production can be offered with finite capacity, cost and lead time. Do not guarantee unlimited stock or fabricate a used asset to satisfy a search.

As technology becomes uncommon, fewer independent workshops may retain suitable equipment, skills and supplies. External repair quotes can then reflect a longer journey, scarcity of compatible workshop slots, specialist labour or difficult parts procurement. Providers must expose those reasons, not apply an unexplained annual obsolescence multiplier.

A player-owned compatible workshop, trained workforce and retained know-how can preserve support. This is not free maintenance: staff, equipment, materials, capacity and downtime still cost money. In-house work can be economical at sufficient utilisation; it is not universally cheaper than outsourcing.

Keep physical age/condition separate from technological obsolescence. Repair needs can grow with actual wear, and an old design can remain less efficient than a new design. Do not increase an unchanged engine's fuel consumption merely because a new year/model arrived. Existing safety and compatibility rules still apply, but do not invent a technology-wide retirement prohibition to defeat this decision.

Horse-drawn freight vehicles and omnibuses are valid surviving 1900 equipment beside early motor or steam-powered road vehicles where plausible. They need compatible stable/service facilities, staff and operating supplies at an aggregate level. Do not add a horse-breeding or per-animal life simulator. Their survival does not enable the pre-1900 Early Ages start.

## 5. Shipment splitting: one order, many physical portions

Use one canonical naming model. `Shipment` is a commercial consignment belonging to an optional customer contract. `CargoLot` is an independently located physical portion of that shipment. It is the executable batch concept called CargoBatch in the core design, not a second competing cargo subsystem.

`TransportPlan` describes the route/responsibility chain. A contract may provide a reusable plan template; a shipment uses a versioned instance/execution plan. `PlanLeg` describes one required physical transfer. `TripAllocation` reserves a quantity of a cargo lot on a specific Trip between boarding/loading and alighting/unloading endpoints.

Suggested identities and responsibilities:

| Object | Responsibility |
|---|---|
| Shipment | Ordered quantity, origin/destination, commodity, contract, deadline, service obligations, split/delivery policy and summary |
| CargoLot | Exact quantity, physical location/carrier, current leg, quality/age, handling-unit membership and lineage |
| TransportPlan / PlanLeg | Ordered feasible endpoints, modes/operators, transfer dependencies, valid alternatives and plan version |
| TripAllocation | Lot/quantity, Trip and occupied route segments, physical capacity pool, state, reservation protection and reason codes |
| HandlingOperation | Actual loading, unloading, transshipment and quantity moved between authoritative locations |
| Capacity ledger | Segment-specific reservations for actual resources; no double-booked wagons, seats, mass, volume or handling slots |

A shipment does not permanently belong to one Trip, Line or partition. Example: 100 t uses 40 + 40 + 20 t inbound Trips, then 70 + 30 t outbound Trips after physically arriving and becoming ready at the transfer point. Keep one shipment in UI. A remaining quantity can wait without a Trip allocation.

### Units and indivisibility

Represent cargo quantities in integer base units/fixed precision, not uncontrolled floating-point subtraction. Definitions declare the unit, mass/volume conversion, allowed split increment and any indivisible handling units. Do not universally assume 1 t is the minimum.

A pallet, vehicle, container or oversized machine can be indivisible. Commodity divisibility does not imply its current packaging can be split without a real repacking operation. Entire-shipment `do_not_split` and `deliver_together` are different contractual conditions; do not silently infer one from the other.

Loading 63 t of remaining mass capacity with a 5 t split increment admits at most 60 t, subject to volume, positions, route load and other constraints. No rounding creates or destroys cargo.

### Physical and commercial invariants

- Every positive physical quantity has exactly one authoritative location: a facility/vehicle or an explicit handling state with precisely accounted source/destination quantities.
- A reservation changes a plan/capacity ledger, not the cargo's physical location.
- For each shipment: created quantity equals undelivered physical quantity plus accepted delivered quantity plus explicitly recorded loss/spoilage/return disposition, with no duplicated terminal state.
- Partial delivery contributes only the accepted quantity. Full completion follows the contract's delivery policy, not the first arriving lot.
- Rebooking one part cannot cancel or reset the other parts' progress.
- A future-leg reservation may exist before arrival if backed by the predecessor plan and compatible capacity. Loading cannot occur before actual arrival, required handling and readiness.
- Do not interpret `required minus all allocations ever created` as waiting cargo. Completed/cancelled historical allocations and reservations on several legs would double-count it. Derive unreserved quantity for the selected lot/leg from live reservations against that lot's currently eligible quantity. Keep an event/audit history separately.
- Segment capacity is released after actual unloading. Cargo from A to B and cargo from B to C can reuse capacity; cargo from A to C blocks both segments.
- Different qualities, deadlines, contracts, indivisible units or custody states must not be merged in a way that loses obligations. Lots may share a visual pile or vehicle while remaining distinct records.
- Combining compatible lots never resets cargo age, spoilage exposure, cost basis or responsibility. Preserve constituent state or do not merge.
- Destination storage and transfer handling capacity are real; arriving cargo cannot disappear into a full warehouse.

Reservations must be transactional. Failed validation, duplicate clicks, save/load or two planners selecting the same capacity cannot reserve the same quantity twice. Save IDs, reservation versions and idempotency keys.

### Allocation policy consistent with the core design

Use physical feasibility first, then the commercial tiers already specified in GAME_DESIGN Section 11:

1. protected/guaranteed contractual obligations;
2. firm recurring/framework obligations;
3. confirmed one-off jobs;
4. spot/discretionary cargo.

Within a tier use last feasible departure/deadline risk, quality risk and stable booking/readiness order, with visible policy adjustments. Service class, player preference and margin do not silently break existing protected commitments. Earlier discussion of a single weighted score must not supersede these contractual tiers.

Ageing can improve precedence within an eligible tier and trigger an alert or extra capacity proposal. It cannot guarantee economy cargo will always move when capacity is permanently insufficient or override a guaranteed allocation. Do not promise starvation prevention that the available capacity cannot deliver.

Reservations can pass through Planned, Reserved, Committed, Loading/Loaded, InTransit, Unloaded/Completed, Cancelled and Replanned states. Operational loading states and commercial allocation states may be separate state machines. Define transitions explicitly. A committed or loaded part is not casually moved to another Trip; cancellation requires a feasible physical recovery/unloading operation.

Cutoff release is responsibility-aware. Customer no-show can release the protected space under its terms. Carrier/subcontractor delay preserves the recovery obligation. Recovery cargo cannot silently displace another protected booking. Compare holding within policy, later Trips, extra movements and an External Transport Order. Expose the shortfall if no feasible recovery exists.

On terminal/route/Trip disruption, replan only affected lots and dependencies. Use event-driven bounded-horizon planning, cached routes, a deterministic tie-break and a material-improvement threshold to prevent allocation ping-pong.

## 6. Save, interaction and presentation requirements

Persist all gameplay authority, including moving assets, wagon orientation/coupling, incomplete handling/shunting, fuel, maintenance, crews and rest capacity, cargo/reservations, Trip/Pattern versions, contracts and renewal state, money postings, AI commitments, queues, construction stages, land edits, technology, active/macro regions, calendar and random-stream state.

Loading a save must not rebuild a newly random world and merely restore the player's balance. Do not serialise the camera/rendered GameObjects as the sole game state. The selected speed may be restored, but quickload should finish loading safely paused by default.

Czech and English must include failure explanations, confirmations, tutorials, financial breakdowns and empty states, not only navigation labels. The currency token remains `money` in both languages. Use localised number formatting independently from that token.

Player-facing graphics cannot be debug primitives with labels. Simple original modular assets are acceptable if they form a coherent world and support physical recognition and readable interaction. Vehicle movement, construction stages, junctions, coupling and cargo operations must have visible counterparts. Graphics are developed alongside milestones, not left until after simulation completion.

## 7. Interpretation and change control

This scope narrows the first release's modes and starting presets, not the long-term design or the operational depth of included modes. Rules for water/tram/trolleybus/metro in the core remain future content, not missing V1 tests.

[V1_IMPLEMENTATION_BRIEF.md](V1_IMPLEMENTATION_BRIEF.md) defines architecture, work order and subsystem delivery. [V1_CONTENT_MANIFEST.md](V1_CONTENT_MANIFEST.md) provides initial numerical/content targets selected for implementation; those numbers are adjustable defaults, not previously approved user facts. [V1_ACCEPTANCE_TESTS.md](V1_ACCEPTANCE_TESTS.md) defines evidence required before calling the game V1.

Resolve genuine contradictions in the affected authoritative text rather than appending contradictory rules. Do not use performance, unavailable assets or a small first milestone as an excuse to silently remove physical continuity, AI parity, agreed territory, offline operation or core mechanics. Record an actual blocker and continue non-blocked work; an incomplete build remains explicitly incomplete.
