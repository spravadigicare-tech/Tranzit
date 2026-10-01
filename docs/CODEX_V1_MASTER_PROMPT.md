# Codex — Autonomous Tranzit V1 implementation assignment

Status: persistent execution assignment.  
Updated: 2026-10-01.

You are implementing **Tranzit V1** in this repository.

Your job is not to prepare another plan and stop. Your job is to **carry the repository from its current documentation/content state to a complete, playable, tested offline Windows V1**, using the approved design as the product authority and continuing autonomously through the implementation milestones.

## 1. Read this before coding

Read, in this order:

1. `AGENTS.md`
2. `docs/CODEX_V1_MASTER_PROMPT.md` — this file
3. `docs/ENGINEERING_STANDARDS.md`
4. `docs/TODO.md`
5. `docs/IMPLEMENTATION_STATUS.md`
6. `docs/V1_SCOPE.md`
7. the complete `docs/GAME_DESIGN.md`
8. `docs/CONTRACT_CANCELLATION.md`
9. `docs/V1_IMPLEMENTATION_BRIEF.md`
10. `docs/V1_CONTENT_MANIFEST.md`
11. `docs/V1_ACCEPTANCE_TESTS.md`
12. `docs/DATA_PIPELINE.md`
13. relevant focused UI/art/vehicle specifications for the subsystem you are implementing.

Do not reinterpret summaries as overriding owning specifications.

Current known repository state at creation of this assignment:
- design/UI/content documentation is extensive;
- vehicle authoring data exists under `content/vehicles/`;
- documentation/content validators and CI exist;
- no Unity project/gameplay implementation was present at the last reviewed state.

Reinspect the actual repository and toolchain before relying on that snapshot.

## 2. Mission

Deliver the approved first playable V1 as a coherent game, not a scaffold.

V1 must include:

- Windows desktop, offline;
- 1900 new-game preset;
- continued historical/technology progression after 1900;
- rail freight;
- rail passengers;
- road freight;
- intercity buses;
- local buses;
- the approved Czechia + adjoining Germany/Poland/Austria/Slovakia world;
- real geography/settlement context and historically plausible authored starting state;
- existing public/third-party infrastructure and competing companies;
- player company founding through a real loan/setup process;
- real physical vehicle/cargo/infrastructure continuity;
- dynamic economy, firms, commodity flows and passenger demand;
- construction, access/capacity, maintenance, workforce, licences, contracts, finance, AI competitors and delegation as specified;
- Czech and English UI;
- coherent 3D stylized/model-world presentation;
- complete save/load;
- required tests and release evidence.

Do not implement:
- water/tram/trolleybus/metro for V1;
- aircraft;
- playable pre-1900 Early Ages content;
- 1925/1950/1975 new-game presets for V1;
- a separate passenger connection-agreement/protected-transfer/connection-hold subsystem.

Passenger inter-operator cooperation in current scope is the defined **partner-capacity-sale through-ticket** mechanism only. Ordinary transfers exist when schedules, interchange and ticket entitlement permit them.

## 3. Autonomy contract

Work autonomously.

Do **not** stop after each milestone and ask for permission to continue.

Do **not** ask the user to re-decide product questions already answered in the repository.

Make routine decisions yourself, including:
- folder structure;
- assembly boundaries;
- data structures;
- package choices;
- coding patterns;
- technical architecture details;
- internal APIs;
- initial performance budgets;
- balancing implementation where the content manifest explicitly treats values as configurable defaults;
- temporary art-production workflow;
- test-fixture details.

Use `docs/ENGINEERING_STANDARDS.md` as the default engineering policy.

Ask the user only when all of the following are true:

1. the issue is a genuine product/design decision rather than engineering implementation;
2. the owning specifications do not already answer it;
3. different answers would materially change player-facing behavior or approved scope;
4. proceeding with a reversible engineering default would be inappropriate.

When a major decision is genuinely required:
- do not block unrelated work;
- record the exact question and affected systems in TODO;
- continue every non-blocked task;
- ask one concise, decision-ready question with the relevant tradeoff.

Never invent a user decision merely to avoid implementation work.

## 4. Core implementation strategy

Build vertically and incrementally.

Do not generate hundreds of empty classes for the whole game before one integrated loop works.

Each milestone must leave the game more playable and must add:
- authoritative state;
- persistence;
- tests;
- localized UI;
- presentation;
- diagnostics/profiling;
- updated implementation evidence.

Use the same domain rules for:
- player execution;
- AI execution;
- planner/forecast validation.

Never create a fake “AI shortcut economy”, fake player preview rules or UI-only capacity model.

## 5. M0 — Reproducible foundation

Goal: create the real game project and the architecture that later systems can safely build on.

### Required work

1. Inspect installed Unity/toolchain.
2. Choose and pin a current compatible stable Unity editor and package set.
3. Create the Unity project at the repository root unless an implementation already exists.
4. Use URP unless the current project proves another approved choice is already established.
5. Create assembly/module boundaries consistent with ENGINEERING_STANDARDS.
6. Enable text serialization/stable project metadata.
7. Establish:
   - typed/stable IDs;
   - GameDate/GameTime;
   - single authoritative simulation clock;
   - speed controls 0.5x/1x/2x/4x/8x/16x/pause;
   - fixed-point money;
   - explicit physical units;
   - deterministic RNG;
   - command/result/reason-code model;
   - event scheduler;
   - transaction/idempotency primitives;
   - save schema/versioning skeleton;
   - atomic save writer;
   - localization setup;
   - common UI theme/components;
   - structured logging/profiler markers.
8. Establish content import/validation from existing repository data.
9. Add build/test scripts with:
   - explicit Unity path configuration;
   - logs;
   - exit codes;
   - bounded timeout behavior.
10. Add CI-friendly tests where the environment permits.

### Architecture requirements from day one

- Simulation state is separate from rendering.
- GameObjects are not authoritative.
- Domain/Simulation can be tested without loading the world scene.
- Save/load is integrated from the first playable state.
- No per-frame economy/AI simulation.
- No global scene searches in runtime hot paths.
- No frame-rate-dependent outcomes.
- No `UnityEngine.Random` in authoritative simulation.
- No floating-point ledger balances.
- No hidden service-locator architecture.
- No giant singleton that owns the entire game.

### M0 exit gate

Do not call M0 complete until actual evidence exists for:
- clean project compile;
- test command;
- standalone menu/build launch where local toolchain permits;
- clock/calendar tests;
- speed invariance tests for equal simulated elapsed time;
- money/idempotency tests;
- save round-trip of core state;
- localization switching baseline.

Record exact commands/results in IMPLEMENTATION_STATUS.

## 6. M1 — Visible world and small road business

Goal: one legitimate small-company road-freight loop that already uses real systems.

### Build

- geographic world fixture suitable for a starting area;
- chunked/streamed presentation foundation;
- camera/pan/rotate/zoom/picking;
- public road graph;
- road routing/access restrictions;
- company founding;
- founding loan;
- office/branch;
- director/staff;
- basic licences;
- one real customer/supplier flow;
- market/opportunity discovery;
- vehicle market;
- purchase/order/delivery of a real authored road vehicle;
- depot/garage/parking;
- loading/unloading endpoints;
- fuel/operating cost;
- one-off/contract road cargo;
- authoritative money postings;
- visible trip movement;
- physical cargo custody;
- save/reload mid-operation;
- first usable Finance/Company/Market/Fleet/Trip/Shipment UI;
- Czech/English strings for the complete loop.

### Optimization from first slice

Do not hardcode the fixture into core logic.

Use:
- stable graph IDs;
- route cache with topology/access versioning;
- spatial index/chunks;
- pooled vehicle presentation;
- event-driven cargo/economy updates;
- bounded query models for UI.

### M1 exit gate

From New Game:
- found company;
- establish office;
- staff it;
- obtain required rights;
- acquire/receive vehicle;
- secure real business;
- physically collect cargo;
- transport it;
- deliver to the actual endpoint;
- receive payment;
- pay costs;
- save during trip;
- reload without duplication or teleportation.

The loop must be playable through UI without debug commands.

## 7. M2 — Rail and construction

Goal: real railway construction and operation integrated into the same economy.

### Build

- free-form spline rail geometry;
- rail graph;
- tracks/junctions/switches/crossings;
- block/section authority;
- stations/platforms/freight terminals;
- industrial siding;
- yards/depots/workshops;
- run-around and turning facilities;
- bridges/tunnels;
- construction planning;
- land/permissions;
- contractors;
- project cost/duration/material quantities;
- physical construction stages;
- closures/temporary capacity impacts;
- track compatibility:
  - gauge;
  - curve;
  - gradient;
  - axle load;
  - length;
  - power/traction where relevant;
- station/route access;
- capacity orders/slots;
- actual track/platform occupancy;
- authored steam locomotive/wagons/coaches;
- physical consist identity/orientation;
- coupling/decoupling;
- shunting;
- legitimate turning/reversing;
- locomotive/wagon purchase and physical delivery;
- rail freight.

### Performance rules

Keep:
- commercial slot windows separate from local block occupancy;
- route/path caches invalidated incrementally;
- train occupancy deterministic;
- remote trains event/segment simulated without losing exact logical position/occupancy commitments.

### M2 exit gate

Player can:
- build a useful rail connection/siding;
- pay real project cost;
- wait through real construction;
- receive/acquire rolling stock;
- form and physically operate a valid consist;
- move paid freight;
- encounter real compatibility/capacity rejection;
- save/load during operation.

No train may teleport, flip direction magically or pass through incompatible/occupied resources.

## 8. M3 — Shared network logistics

Goal: make freight/contracts work across several Trips, modes and carriers.

### Build

- canonical Contract → Shipment → CargoLot → TransportPlan → TripAllocation model;
- Line → ServicePattern → Trip hierarchy;
- scheduled/ad-hoc work;
- split shipments;
- multi-leg transport;
- real transfer handling/storage;
- capacity by actual compatible vehicle/segment;
- freight cutoffs;
- priority tiers from GAME_DESIGN 11.0.1;
- reallocation/recovery;
- external transport orders;
- subcontracting;
- customer terminal pickup/delivery;
- firm-owned local logistics;
- bounded captive intercity road behavior;
- industrial sidings/customer wagons/internal shunting;
- no captive non-transport mainline rail;
- contractual handover boundary;
- cargo age/quality/perishability;
- construction/material/fuel/supply freight reuse of the same logistics machinery.

### M3 exit gate

Pass the canonical 100 t split-shipment scenario:
- road → rail → road;
- 40/40/20 inbound rail split;
- 70/30 onward split after real handling;
- exact quantity/custody conservation;
- one allocation cancellation;
- transfer storage pressure;
- save/load;
- no duplicate reservation;
- no cargo teleportation.

## 9. M4 — Passenger operation

Goal: complete local/intercity bus and rail passenger gameplay without inventing removed mechanics.

### Build

- aggregate OD passenger demand;
- economic-centre access model;
- whole-centre direct station/stop catchment;
- real feeder access between centres;
- itinerary choice;
- walking/interchange cost;
- published timetables;
- ticket sales channels appropriate to era;
- open/optional/required reservations;
- capacity by segment/class/zone;
- queues;
- boarding/alighting;
- dynamic dwell;
- fares/tariffs;
- company integrated ticket systems;
- single/weekly/monthly products;
- period validity on the 7/14-day game calendar;
- group passenger contracts where specified;
- two-operator partner-capacity-sale through tickets;
- directional Line scope;
- money/km settlement;
- positive/zero/negative reseller margin;
- captured tariff/agreement versions;
- ordinary transfer behavior;
- cancellation/capacity-loss re-accommodation/refund for sold obligations.

### Explicit non-feature

Do not create:
- passenger connection agreements;
- protected/guaranteed transfer objects;
- per-connection hold policies;
- automatic partner rebooking rights arising from a transfer;
- shared multi-company period passes;
- recursive capacity resale.

A connecting service does not wait merely because passengers are transferring.

### M4 exit gate

Passenger round trips work on bus/rail with:
- real fares;
- real capacity;
- queues/crowding;
- transfers;
- integrated own-company tickets;
- valid two-operator through ticket;
- exactly-once partner settlement;
- save/load;
- disruption/capacity reduction consequences;
- no invented connection-protection subsystem.

## 10. M5 — Business, AI and ownership

Goal: turn the transport simulation into the approved business simulation.

### Build

- firms/facilities;
- explicit recipes/inventory;
- final consumers;
- commodity city/locality markets;
- economic centres;
- reference pricing;
- production/consumption;
- contract/opportunity lifecycle;
- producer/buyer transport proposals;
- spot/open freight limits;
- public service tenders;
- sealed competitor bids;
- transparent scoring;
- contract SLAs/bonuses/penalties/cure/termination;
- branches/commercial coverage;
- aggregate workforce;
- managers/directors/delegation;
- licences/market entry;
- financing/loans/distress;
- AI companies using the same money, assets, staff, access and feasibility authority;
- AI opportunity evaluation/procurement/staffing/operation/maintenance/exit;
- shares/acquisition;
- AI-managed subsidiaries;
- infrastructure ownership transactions;
- public infrastructure contract models;
- relationship/history/known-information limits.

### AI architecture

Separate:
- strategy/policy;
- planning;
- shared authoritative execution.

AI may be simpler than the player strategically; it may not cheat physically or financially.

Use bounded decision cadences and event-triggered replanning. Never run every AI company planner every frame.

### M5 exit gate

At least one rival:
- discovers/chooses viable business;
- obtains real resources;
- bids/contracts;
- acquires/uses assets;
- operates service;
- pays costs;
- reacts to failure;
- expands, adjusts or exits.

Player can delegate and perform ownership/acquisition flows without duplicating assets/debt.

## 11. M6 — Lifecycle, progression and disruption

Goal: make a long campaign operationally credible.

### Build

- fuel/energy/supplies;
- maintenance planning;
- wear/condition;
- workshop capability/capacity;
- breakdown/rescue/tow;
- retrofit templates;
- leases;
- sale/scrap physical handover;
- historical technology introduction;
- company adoption/research where genuinely required;
- enduring old vehicle availability;
- changing external support/parts scarcity;
- own-workshop alternative;
- weather;
- closures/disruptions;
- serious incidents;
- world/historical events;
- service suspension/resumption;
- contract renewal;
- construction upgrades;
- city/economic-centre evolution;
- technology-driven changes in demand/production/operations.

### M6 exit gate

Demonstrate:
- maintenance queue;
- breakdown + physical recovery;
- retrofit;
- old technology still usable with real support cost;
- later technology introduction;
- renewal/suspension;
- save/load across all these states.

## 12. M7 — Full world, content and presentation

Goal: replace milestone fixtures with the approved release world/content quality.

### Build/content

- complete approved map coverage;
- terrain/relief/rivers;
- settlement hierarchy;
- historically plausible 1900 infrastructure;
- existing firms/competitors/public services;
- inactive/macro world;
- active-region streaming;
- city architecture and growth;
- economic-centre generation/splitting/merging rules;
- vehicle catalogue integration across history;
- vehicle prefabs/LODs/materials/audio;
- buildings/roads/rail/stations/industry;
- environment/vegetation/fields;
- day/night/weather;
- historically evolving visual language;
- coherent UI polish;
- onboarding;
- settings;
- complete Czech/English;
- required content minima;
- accessibility/readability baseline.

### Performance work

Profile representative developed networks.

Required instrumentation:
- frame p50/p95/p99;
- simulation phase time;
- requested vs achieved speed;
- event backlog;
- active/remote entity counts;
- path cache hit rate;
- allocations/GC;
- memory;
- save/load duration.

Optimize in this order:
1. algorithms/full-world scans;
2. allocations/churn;
3. cache/incremental updates;
4. batching;
5. parallel pure-data work;
6. Burst/Jobs for measured hotspots;
7. data-layout rewrites only if justified.

Do not reduce approved simulation truth to hit a benchmark.

## 13. M8 — Release verification

Goal: prove V1 instead of declaring it.

### Required work

- run full V1 acceptance suite;
- run invariant/property tests;
- run save/reload tests at dangerous boundaries;
- run randomized reproducible simulation tests;
- run performance fixtures at all supported speeds;
- run multi-hour soak;
- run headless multi-year progression where feasible;
- manually verify standalone Windows build;
- verify Czech/English;
- verify onboarding;
- verify graphics/audio;
- verify approved map/content;
- resolve release blockers;
- document any remaining non-blocking limitations.

### Release blockers include

- save corruption;
- resource duplication/loss;
- vehicle/cargo teleportation;
- unsafe rail occupancy/collision;
- fabricated AI resources;
- no legitimate start path;
- missing approved modes/territory;
- broken main navigation/workflows;
- required online dependency;
- untranslated critical UI;
- debug primitives/labels standing in for final player-facing presentation;
- unexecuted required acceptance gates being called PASS.

## 14. Cross-cutting implementation checklist

For every subsystem, confirm:

### Authority
- Where does authoritative state live?
- Does rendering merely reflect it?
- Are IDs stable?

### Time
- Does it use GameTime?
- Is it frame-rate independent?
- Does it behave identically across speed multipliers for equal simulated time?

### Money/quantity
- Are units explicit?
- Are ledger postings idempotent?
- Is conservation enforced?

### Player/AI/planner
- Do they use one feasibility authority?
- Is any shortcut cheating?

### Persistence
- What is serialized?
- Is schema versioned?
- Is a round-trip test present?
- Can a save occur mid-operation?

### Explainability
- Are reason codes/contributing values retained?
- Can UI explain a blocked action/outcome?

### Performance
- Is this event-driven/coarse-tick?
- Any accidental full-world scan?
- Any per-frame allocation?
- Any repeated pathfinding that needs caching?

### UI/localization
- Is it reachable through canonical navigation?
- Are CZ/EN strings implemented together?
- Are empty/error/loading states implemented?

### Tests
- Unit/integration/invariant/PlayMode coverage appropriate?
- Was the test actually executed?

## 15. Commit and evidence discipline

Prefer small coherent commits that keep repository state internally valid.

After substantial implementation changes:

1. run relevant tests;
2. run documentation/content validators if their files changed;
3. run `git diff --check`;
4. update `docs/IMPLEMENTATION_STATUS.md` with:
   - date/commit;
   - milestone/SYS IDs;
   - implemented paths;
   - exact test/build command;
   - observed result;
   - failures/blockers;
   - known limitations;
   - next executable task;
5. update `docs/TODO.md` for newly discovered remaining work;
6. continue automatically to the next non-blocked task.

Do not convert “code written” into “implemented and tested” without evidence.

## 16. Handling blockers

Classify blockers precisely.

Examples:
- Unity editor not installed;
- editor licence unavailable;
- required external dataset inaccessible;
- repository permission prevents write;
- platform-specific build cannot be executed in current environment.

When blocked:
- record exact blocker;
- continue all non-blocked work;
- prepare build/test automation and content where useful;
- never fake an observed build/test result;
- never silently shrink V1 scope.

If a blocker only prevents Windows packaging, continue simulation, content, tests and editor work.

## 17. What not to do

Do not:

- rewrite approved gameplay because implementation is difficult;
- turn V1 into a demo;
- stop at architecture/scaffolding;
- postpone save/load, localization, art or tests until the end;
- build parallel rule systems for UI/AI/planner;
- run economy/AI per frame;
- instantiate every person/cargo unit as a persistent GameObject;
- use hidden arbitrary modifiers where the design expects explainability;
- hardcode content IDs into core algorithms;
- make runtime depend on internet services;
- assume every null/estimate in authored content is safe to invent;
- claim benchmarks without measurements;
- claim passing tests that were not run;
- wait indefinitely on Unity/watch/game processes;
- ask the user about already-decided scope;
- create a passenger connection-protection subsystem.

## 18. Final completion condition

You are finished only when the repository contains a reproducible V1 implementation and the actual standalone game satisfies the release contract with recorded evidence.

The final handoff must contain:

- working offline Windows build;
- exact build/run instructions;
- pinned editor/package versions;
- architecture/save/content documentation;
- complete Czech/English main UI;
- approved world/content bundled;
- automated test results;
- acceptance matrix;
- performance report;
- manual standalone walkthrough evidence;
- known issues;
- no false PASS claims.

Until then, keep implementing the next highest-value non-blocked task from M0–M8.

**Start by inspecting the actual repository/toolchain, then execute M0. Do not answer with another broad implementation plan.**
