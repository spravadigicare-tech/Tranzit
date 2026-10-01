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
| Public infrastructure contracts | V1 includes all three confirmed public corridor/infrastructure models: state-owned infrastructure with player service operating right, Build–Operate–Transfer concession, and publicly co-funded private infrastructure with explicit funding/access/service conditions |
| Passenger cooperation | Bilateral partner-capacity sales can create a two-operator **single-journey through ticket** with directional Line scope and money/km settlement. The seller must operate part of the journey; partner-only resale, recursive resale and shared multi-company weekly/monthly passes are outside required V1. Capacity resale alone does not coordinate or protect the transfer; passenger connection-agreement mechanics remain separately specified work. |
| Player start | Small, mode-neutral company financed by one of three favourable founding loans; no free branch, fleet or depot |
| Currency | One accounting unit named `money`; compact UI amounts may use one dedicated neutral coin/token icon as shorthand, but no real-world currency symbols, historical currency switching or foreign-exchange subsystem |
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

Use the explicit conversion in GAME_DESIGN Section 3.4 and [DATA_PIPELINE.md](DATA_PIPELINE.md). Source dates are validated and retained; imported days are proportionally mapped to 1–14, while game-authored dates are not remapped. This is a documented engineering convention, not an additional historical fact or gameplay clock. The pipeline still requires actual sourced geographic/historical content.

## 4. Historical vehicles remain usable and discoverable

The no-end-year rule applies to the whole game, not only V1. Its complete definition is now in [GAME_DESIGN Section 15.11](GAME_DESIGN.md#1511-enduring-historical-vehicle-availability): permanent model discoverability, finite actual offers, serviceable physical assets, economic external-support scarcity and a real in-house support alternative. Horse-drawn equipment can survive into 1900 without enabling an Early Ages start.

This section is a release reminder, not a second vehicle-availability specification.

## 5. One shipment, multiple physical lots and Trips

The canonical model and complete invariants are in [GAME_DESIGN Section 11.9](GAME_DESIGN.md#119-shipments-and-physical-cargo-lots). `Shipment` is the commercial consignment, `CargoLot` its independently located physical portion, `TransportPlan` the versioned execution chain and `TripAllocation` the quantity reserved on a specific Trip/stop interval. There is no competing batch subsystem.

V1 must support one 100 t shipment using 40 + 40 + 20 t inbound and 70 + 30 t onward capacity after actual transfer handling, preserving quantity, age, quality, obligations and lineage. Reservation changes never move physical cargo. The sole freight-priority policy is in GAME_DESIGN Section 11.0.1, including responsibility-aware cutoffs and protected recovery.

## 6. Save, interaction and presentation requirements

Persist all gameplay authority, including moving assets, wagon orientation/coupling, incomplete handling/shunting, fuel, maintenance, crews and rest capacity, cargo/reservations, Trip/Pattern versions, contracts and renewal state, money postings, AI commitments, queues, construction stages, land edits, technology, active/macro regions, calendar and random-stream state.

Loading a save must not rebuild a newly random world and merely restore the player's balance. Do not serialise the camera/rendered GameObjects as the sole game state. Manual load and quickload finish safely paused by default. The save can retain the previously selected running-speed preference, but loading does not immediately resume simulation.

Save writes must be failure-safe/atomic: an interrupted or failed replacement must preserve the previous valid save rather than corrupting both states. Manual saves, a distinct quicksave slot/rotation and rotating autosaves are required. Autosave cadence uses real elapsed application play time rather than game time, so 16× does not autosave sixteen times more often than 1×. Save/load cannot finalize an uncommitted draft or replay a transaction.

Saves are presented primarily by campaign/company identity with clear manual/quicksave/autosave type, game date/time, real save timestamp and compatibility state. Incompatible/corrupt saves explain the detected reason. Loading, returning to the main menu or quitting warns only when actual unsaved campaign progress or relevant dirty drafts would be lost; Save and exit proceeds only after a successful save.

Czech and English must include failure explanations, confirmations, tutorials, financial breakdowns and empty states, not only navigation labels. The accounting unit remains `money` in both languages; compact UI amounts may use the confirmed neutral UI icon. Use localised number formatting independently from that unit.

Player-facing graphics cannot be debug primitives with labels. Simple original modular assets are acceptable if they form a coherent world and support physical recognition and readable interaction. Vehicle movement, construction stages, junctions, coupling and cargo operations must have visible counterparts. Graphics are developed alongside milestones, not left until after simulation completion.

## 7. Interpretation and change control

This scope narrows the first release's modes and starting presets, not the long-term design or the operational depth of included modes. Rules for water/tram/trolleybus/metro in the core remain future content, not missing V1 tests.

[V1_IMPLEMENTATION_BRIEF.md](V1_IMPLEMENTATION_BRIEF.md) defines architecture, work order and subsystem delivery. [V1_CONTENT_MANIFEST.md](V1_CONTENT_MANIFEST.md) provides initial numerical/content targets selected for implementation; those numbers are adjustable defaults, not previously approved user facts. [V1_ACCEPTANCE_TESTS.md](V1_ACCEPTANCE_TESTS.md) defines evidence required before calling the game V1.

Resolve genuine contradictions in the affected authoritative text rather than appending contradictory rules. Do not use performance, unavailable assets or a small first milestone as an excuse to silently remove physical continuity, AI parity, agreed territory, offline operation or core mechanics. Record an actual blocker and continue non-blocked work; an incomplete build remains explicitly incomplete.
