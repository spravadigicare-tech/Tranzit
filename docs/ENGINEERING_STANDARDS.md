# Tranzit — Engineering standards and performance contract

Status: persistent implementation standard for V1 and later work.  
Updated: 2026-10-01.

This document defines engineering conventions, architecture boundaries, performance rules and quality gates. It does not override gameplay design. If it conflicts with GAME_DESIGN, V1_SCOPE or another owning gameplay specification, fix the implementation/engineering assumption rather than silently changing the game.

## 1. Engineering goals

Build Tranzit as a long-lived simulation product, not a disposable prototype.

Every implementation choice should support:

- deterministic and inspectable simulation state;
- physical continuity of vehicles, cargo and infrastructure;
- a very large streamed world;
- 0.5x–16x simulation speeds on one authoritative clock;
- event-driven/coarse-tick economy rather than per-frame simulation;
- save/load from the beginning;
- Czech/English localization from the beginning;
- player and AI using the same authoritative rules;
- explainable outcomes with structured reason data;
- content-driven historical progression;
- testability outside Unity presentation where practical;
- profiling-driven optimization rather than speculative rewrites.

Do not trade away core invariants merely to make the first vertical slice easier.

## 2. Project structure and dependency direction

Use clear assembly/module boundaries. The exact folder names may evolve, but dependency direction must remain one-way and explicit.

Recommended logical layers:

1. **Domain/Core**
   - stable IDs and typed value objects;
   - game calendar/time;
   - money and units;
   - commands/events/reason codes;
   - deterministic RNG interfaces;
   - content-definition contracts;
   - no UnityEngine dependency.

2. **Simulation**
   - authoritative mutable world state;
   - transport, capacity, inventory, firms, passengers, economy, contracts, staff, maintenance and incidents;
   - event/tick scheduling;
   - no dependency on GameObjects/UI.

3. **Planning**
   - read-only projections and feasibility checks;
   - uses the same validators, ledgers and route/capacity authority as execution;
   - must not maintain a parallel “fake” simulation rule set.

4. **Application**
   - command validation and atomic commit;
   - player/AI entry points;
   - queries/presentation models;
   - transaction/idempotency boundaries.

5. **Persistence**
   - versioned save DTOs/snapshots;
   - migrations;
   - atomic file replacement and recovery;
   - deterministic restore of authoritative state.

6. **World/Content**
   - geography preprocessing;
   - content JSON import/validation;
   - historical initialization;
   - asset/content references.

7. **Unity Presentation**
   - streamed/chunked GameObjects and pooled visual proxies;
   - camera, terrain, spline meshes, animation, audio, VFX;
   - never the sole authority for simulation state.

8. **UI**
   - UI Toolkit presentation and interaction;
   - localized labels;
   - no business rules duplicated in view code.

9. **Editor/Tests/Build**
   - content import tools;
   - automated tests;
   - fixtures;
   - build scripts and CI helpers.

Avoid circular assembly references. Domain/Core and Simulation must remain usable in plain .NET-style tests without loading scenes.

## 3. Source, namespace and naming conventions

Use C# with nullable reference types enabled where compatible.

Conventions:

- namespaces follow project domain rather than scene/folder accidents, e.g. `Tranzit.Core`, `Tranzit.Simulation.Transport`, `Tranzit.UI`;
- public types/members: PascalCase;
- private fields: `_camelCase`;
- locals/parameters: camelCase;
- interfaces use `I...` only when an abstraction boundary is real;
- enums use singular type names and explicit values when persisted;
- stable persisted/content IDs are strings or strongly typed ID wrappers, never Unity instance IDs;
- avoid abbreviations unless they are canonical domain terms;
- one authoritative meaning per term: Line, ServicePattern, Trip, Shipment, CargoLot, TransportPlan, TripAllocation, etc.;
- do not invent synonyms in code for canonical domain objects.

Prefer small cohesive types over “Manager” god classes.

A service may coordinate a subsystem; it must not silently become a global mutable service locator.

## 4. State, identity and transactions

Every authoritative entity that survives frames, scene loads or saves has a stable ID.

Rules:

- Unity GameObject/component identity is presentation-only;
- IDs remain stable through save/load, streaming and renaming;
- ownership/location/custody changes are explicit state transitions;
- one physical asset/cargo quantity has one authoritative current location;
- reservations never move physical state;
- commands that spend money, reserve finite capacity, transfer ownership, create agreements or complete deliveries must be idempotent;
- retries/reloads must not duplicate money postings, cargo, vehicles, contracts or events;
- use transaction IDs/command IDs where a repeated external/UI invocation could occur.

Prefer explicit state machines for important lifecycles such as orders, construction, agreements, Trips, maintenance, incidents and saves.

## 5. Time and scheduling

Use the canonical GameTime/GameDate model everywhere.

Never:

- use DateTime/TimeSpan as the authoritative gameplay calendar for recurring game periods;
- assume Gregorian month lengths;
- run economy/production/AI logic every frame;
- make simulation outcomes depend on render frame rate.

Use scheduled events/coarse ticks:

- movement/occupancy: as required by physical simulation;
- economy/market/development: canonical coarse cadence;
- AI strategic planning: bounded cadence and event-triggered reevaluation;
- UI queries: event-driven/cached refresh.

Implement a central scheduler suitable for millions of future operations without scanning every entity every tick. A heap/calendar queue/timing-wheel approach is acceptable; choose based on profiling and simplicity.

At high speed, process all logically required events in order. Do not “skip” occupancy, payments, deadlines, loading or state transitions to reach 16x.

## 6. Numeric conventions

### Money

Use fixed-point integer accounting.

Recommended internal unit:
- 1 money = 100 subunits.

Rules:
- no floating-point authoritative ledger balances;
- rounding policy must be explicit and tested;
- one posting is recorded once;
- forecasts may use decimal/double internally but convert to disclosed estimates and never mutate ledger state.

### Physical quantities

Use explicit units in names/types:
- metres;
- kilometres where presentation/import requires it;
- kilograms/tonnes;
- litres;
- kWh/MWh-equivalent where defined;
- seconds/minutes in game time.

Do not mix unit systems implicitly.

Use double precision for authoritative world/geographic coordinates and route distances. Unity local rendering coordinates may use float after origin rebasing.

## 7. Determinism and RNG

Use deterministic RNG streams owned by simulation state.

Requirements:

- no `UnityEngine.Random` in authoritative simulation;
- derive named/subsystem streams from a root campaign seed;
- persist RNG state where future outcomes depend on it;
- avoid order-dependent randomness from hash/dictionary iteration;
- tests can replay a failure from seed + save/state.

Bit-for-bit equality across all CPUs is not required unless explicitly feasible, but logical outcomes and integer accounting must be stable inside the supported runtime/build with declared numeric tolerances.

## 8. Collections and data access

Select collections for access patterns, not convenience.

Hot-path rules:

- avoid LINQ in high-frequency simulation loops;
- avoid per-tick allocations;
- reuse buffers/pools for temporary route/capacity calculations;
- prefer indexed arrays/lists and dictionaries keyed by stable IDs;
- use spatial indices for geographic queries;
- maintain reverse indices for ownership, station/Line membership, reservations and affected dependencies;
- update caches incrementally on relevant events.

Do not repeatedly scan all firms, all vehicles or the whole transport graph for local decisions.

## 9. Routing and network performance

Road and rail routing must be cacheable and invalidation-aware.

General strategy:

- immutable/stable network topology portions get version IDs;
- route/path cache keys include relevant compatibility/access constraints and topology/version state;
- invalidate only affected regions/edges when infrastructure changes;
- use A* or another justified shortest-path algorithm for local route planning;
- introduce hierarchical/multi-level routing for long-distance large-world queries when profiling requires it;
- batch similar route queries where possible.

Rail:
- keep physical graph/topology separate from commercial Line/Pattern definitions;
- block/section/platform occupancy is authoritative;
- dynamic routing cannot bypass access, gauge, traction, length, direction or capacity constraints.

Road:
- model enough lane/direction/turn restrictions and queue/capacity state for gameplay;
- do not build an FPS-level driving simulator;
- private traffic can remain aggregated.

## 10. Simulation LOD and world streaming

Simulation LOD changes detail, never business truth.

Use at least conceptual levels such as:
- detailed active area;
- standard active region;
- remote/inactive macro simulation.

Rules:
- logical IDs, ownership, quantities, elapsed time, contracts and financial outcomes survive LOD changes;
- streaming/unstreaming visual chunks never creates/destroys authoritative assets;
- origin rebasing changes presentation coordinates only;
- remote movement may be event/segment based rather than frame-integrated, but must preserve continuity and capacity commitments;
- do not instantiate persistent GameObjects for the entire world.

Use chunked terrain/world loading and pooled presentation proxies.

## 11. Unity presentation practices

Prefer:
- URP;
- GPU instancing;
- LOD Groups or equivalent asset LOD strategy;
- shared materials/material variants;
- object pooling for frequently streamed visual proxies;
- baked/static data where appropriate;
- async/streamed loading for world chunks;
- culling and bounded particle/VFX systems.

Avoid:
- thousands of empty MonoBehaviour Update methods;
- `FindObjectOfType`/scene scans in normal runtime loops;
- runtime reflection-heavy dependency injection;
- one GameObject per simulated person/cargo unit;
- material instantiation per object;
- unbounded UI element creation for historical lists.

Use Jobs/Burst selectively for proven CPU-heavy pure-data work. Do not convert the whole project to ECS/DOTS before profiling demonstrates a need.

## 12. UI architecture

Use UI Toolkit unless an existing implemented project proves another consistent choice is required.

UI rules:

- view code reads presentation/query models and submits commands;
- no direct mutation of simulation entities from controls;
- no gameplay rules duplicated in USS/UXML/MonoBehaviours;
- reusable components for cards, tables, money, dates, status, reason lists and confirmations;
- virtualize long lists;
- preserve stable selection/pinned identity across live refresh;
- all player-facing text goes through localization keys except genuine authored proper names/content;
- Czech and English are implemented together, not translated at the end;
- keyboard/focus equivalents exist for hover-only explanation.

Use the final UI-D41 navigation and floating-window conventions.

## 13. Save/load architecture

Save/load is a foundational subsystem, not an end-of-project feature.

Requirements:

- versioned save schema;
- stable entity IDs and references;
- atomic write to temporary file then validated replacement;
- preserve prior valid save if write/replace fails;
- checksum/content-version validation where useful;
- explicit migrations between supported schema versions;
- quicksave/manual/autosave separation;
- restore paused by default;
- persist authoritative simulation, not rendered GameObjects;
- save during movement, handling, construction, maintenance and transactions without duplication or rollback corruption.

Every new authoritative subsystem must define its persistence representation and round-trip test when introduced.

## 14. Content/data conventions

Existing JSON under `content/vehicles/` is canonical authoring data.

New configurable gameplay content should be versioned and data-driven where reasonable.

Rules:
- stable English IDs;
- localized display names separate from IDs;
- schema validation for machine-authored content;
- real-world inspirations only in provenance/source fields where fictionalization is required;
- no hardcoded model/city/company lists inside simulation algorithms;
- balancing constants live in versioned config/content rather than scattered magic numbers;
- every “temporary” balancing constant has a named setting and unit.

Do not use ScriptableObjects as the only durable source for externally authored/versioned data when JSON/content files are canonical. Imported runtime assets may reference baked ScriptableObjects or binary representations if generated deterministically from source content.

## 15. Error handling and explainability

Expected gameplay failures are data, not exceptions.

Use structured result/reason objects for:
- compatibility failures;
- insufficient capacity;
- missing licence/access;
- route infeasibility;
- insufficient funds;
- staffing shortages;
- reservation conflicts;
- unavailable provider;
- contract/timetable blockers.

Exceptions are for programmer errors, corrupted state or truly exceptional technical failures.

Every material decision should expose reason codes and contributing values sufficient for UI explanation and debugging.

## 16. Logging and diagnostics

Use structured logging categories with IDs.

Do not spam logs every frame.

For simulation defects, log enough to identify:
- campaign seed;
- simulation timestamp;
- entity IDs;
- command/event ID;
- subsystem;
- reason/failure code.

Development builds should support targeted diagnostic overlays and state inspection. Debug tools must not ship as hidden normal-play cheats.

## 17. Testing strategy

Use the cheapest reliable test layer first.

### Pure/unit tests
Cover:
- calendar;
- money;
- units;
- state transitions;
- allocation/conservation;
- pricing;
- contract calculations;
- validators;
- deterministic RNG;
- save DTO migrations.

### Integration/simulation fixtures
Cover:
- multi-leg logistics;
- network capacity;
- timetable/version transitions;
- passenger/cargo capacity;
- AI/player competition;
- production/economy;
- disruptions;
- save/load at boundaries.

### Property/invariant tests
Continuously assert:
- no negative inventory;
- no duplicated asset ownership;
- cargo conservation;
- capacity bounds;
- idempotent money postings;
- stable references after save/load.

### Unity EditMode/PlayMode
Cover:
- scene/content integration;
- controls;
- streaming;
- selection;
- UI workflows;
- visible construction/vehicle state.

### Standalone/manual
Cover:
- actual Windows build;
- localization/readability;
- graphics/audio;
- onboarding;
- long-session stability.

Never mark a test PASS unless executed.

## 18. Performance budgets and profiling

Do not set fake absolute performance claims before a real Unity baseline. Establish measurable budgets during M0/M1 and record the test machine/settings.

From the first implementation:
- add lightweight profiler markers around simulation phases;
- track event backlog;
- track route-cache hit/miss rates;
- track active/remote entity counts;
- track allocations/GC;
- track save/load duration;
- track requested versus achieved simulation speed.

Performance work order:
1. remove algorithmic full-world scans;
2. fix avoidable allocations/churn;
3. cache/incrementally update repeated calculations;
4. batch work;
5. parallelize pure-data hotspots;
6. use Burst/Jobs where measured benefit exists;
7. change data layout only when profiling justifies it.

Never optimize by deleting required simulation state or changing outcomes.

## 19. Git and change discipline

- preserve unrelated user changes;
- no force-push;
- no destructive cleanup unless explicitly required and safe;
- small coherent commits;
- one commit should leave the repository internally consistent where practical;
- update owning docs/tests together with behavior changes;
- generated caches/build outputs stay ignored;
- do not commit local Unity Library/Temp/Logs/Obj.

Before completing a substantial change:
- run relevant tests;
- run documentation/content validators when applicable;
- run `git diff --check`;
- update TODO/IMPLEMENTATION_STATUS with actual evidence.

## 20. Definition of engineering quality

A feature is not complete because its UI exists or its code compiles.

It is complete at the implemented scope when:
- the authoritative state model exists;
- player and AI use the same core rules where applicable;
- save/load round-trips it;
- failure states are explicit/explainable;
- it has automated tests at the appropriate level;
- relevant UI is usable/localized;
- presentation reflects the physical state;
- measured performance is acceptable for the current milestone workload;
- implementation status records real evidence.

When forced to choose between a quick shortcut that violates an invariant and a narrower but correct implementation slice, choose the correct slice and continue iteratively.
