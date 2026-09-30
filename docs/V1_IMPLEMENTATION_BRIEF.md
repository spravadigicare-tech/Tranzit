# Tranzit — First playable implementation brief for OpenCode

Prepared: 2026-09-30.
Status: implementation handoff, not implemented software or a passing test report.
Baseline inspected: `spravadigicare-tech/Tranzit`, main commit `0ff59b98d8b9bdcbe3fec32299086bdcdb306c44`. That baseline contains AGENTS.md, README.md and two design documents; it has no Unity project, scenes, game code or production assets. Reinspect the actual working tree before starting because it may have advanced since this handoff.

## 1. Delivery objective

Build the first genuinely playable Tranzit game. A player must be able to start a company in 1900, establish and staff branches, arrange legal/access rights, acquire and physically receive vehicles, establish operating facilities, secure business, construct infrastructure, publish passenger/freight services, run physical transport, receive revenue, pay real costs, survive disruption, maintain equipment, compete, delegate and expand. The player must be able to save during these operations, close the game and continue without changing the simulation outcome.

The final deliverable is an offline Windows game with a coherent 3D world and complete Czech/English interaction, not only a simulator library, project scaffold, feature list, menu, isolated minigame or editor-only demonstration.

Implement iteratively. A first vertical slice is an internal milestone and does not fulfil this release definition. All milestones below belong to one V1 delivery target. Do not declare V1 finished because one train moves or a collection of panels exists.

## 2. Documents and authority

Read AGENTS.md first. Then:

1. [V1_SCOPE.md](V1_SCOPE.md): approved first-release boundary and cross-system clarifications, including cargo splitting and lasting vehicle availability.
2. [GAME_DESIGN.md](GAME_DESIGN.md): full mechanics; read completely once, then reread affected sections for each feature.
3. [CONTRACT_CANCELLATION.md](CONTRACT_CANCELLATION.md): binding early-exit, capacity-release and renewal distinctions.
4. This brief, [V1_CONTENT_MANIFEST.md](V1_CONTENT_MANIFEST.md) and [V1_ACCEPTANCE_TESTS.md](V1_ACCEPTANCE_TESTS.md).

The core design still describes the wider base game. Water, tram, trolleybus and metro systems and later new-game presets are not first-release requirements. Conversely, an included road/rail mechanic does not become optional merely because its first implementation is difficult. Do not build aircraft or playable pre-1900 content.

Architecture, numerical defaults, catalogue counts and test workloads in this handoff are engineering decisions, not additional historical facts or claims of user-approved balancing. They may be improved with a documented rationale while preserving the approved product scope.

## 3. Required repository and release outputs

Create a real Unity project at the repository root unless inspection finds an established project location. Commit Assets, Packages, ProjectSettings, assembly definitions and required .meta files. Use text serialization and stable GUIDs. Ignore Library, Temp, Logs, Obj and local caches. Do not replace the repository with a single generated script or a runtime scene generator that still needs undocumented manual wiring.

Expected deliverables:

| Deliverable | Required evidence |
|---|---|
| Unity project | Clean checkout opens with the pinned editor and resolves packages; no missing scripts/assets |
| Windows build | Standalone x64 build launches to the menu and runs offline without the Editor |
| Reproducible build/test entry points | PowerShell scripts with documented editor-path configuration, exit codes, logs and timeouts |
| Game content | Bundled regional world, historical initialization, catalogues, translations, coherent models/materials/audio |
| Automated tests | Unit, integration and Unity interaction tests with machine-readable results |
| Playability verification | Manual walkthroughs on the real build, screenshots or recordings from that build, known-issue report |
| Performance report | Actual hardware/settings/build/seed/workload, observed frame timing and simulation-speed ratio |
| Developer documentation | Architecture decisions, data schema, save format, asset pipeline, build/run instructions |
| Progress ledger | Requirement IDs mapped to implementation files, tests, evidence and remaining defects |

Recommended document paths to create during implementation: `docs/IMPLEMENTATION_STATUS.md`, `docs/ARCHITECTURE.md`, `docs/BUILD_AND_RUN.md`, `docs/SAVE_FORMAT.md`, `docs/DATA_PIPELINE.md`, `docs/KNOWN_ISSUES.md`, `docs/TEST_RESULTS.md` and `docs/PERFORMANCE.md`. Do not populate results with invented successful runs.

## 4. Technical baseline

### 4.1 Engine and packages

Default to a supported patch of Unity 6.3 LTS, C# and URP. Unity's release page identifies 6.3 as an LTS line [R1]; URP is its prebuilt render pipeline [R2]. This does not assert a particular latest patch or installed toolchain. Verify the available stable patch before creating the project, record it in ProjectVersion.txt and document the exact choice. If a compatible existing project already exists, do not casually migrate it.

Use released, editor-compatible packages for Input System, Localization, Splines and Unity Test Framework. Use UI Toolkit for the management UI unless an existing project or demonstrated requirement justifies another consistent solution. Verify package versions in Package Manager and pin both manifest and lockfile. Avoid preview packages and paid plugins as a hidden requirement.

Unity Splines can provide geometry authoring [R3], but does not implement a railway topology, interlocking, dispatch or path reservation system. Unity Localization provides localization infrastructure [R4], not translated game content. Those responsibilities remain part of this project.

Start with a testable plain-C# simulation and efficient data-oriented containers. Use Jobs/Burst or Entities selectively when profiling and package compatibility justify them. Do not rewrite the entire game into DOTS before delivering an integrated loop, and do not use thousands of per-entity MonoBehaviour Update methods instead.

### 4.2 Boundaries

Suggested assemblies/modules:

| Module | Authority |
|---|---|
| Domain/Core | IDs, time/calendar, money, units, definitions, commands, events, reason codes |
| Simulation | World state and ordered execution; transport, inventories, resources, firms and policy systems |
| Planning | Read-only proposals using the same feasibility rules and ledgers as execution |
| Application | Player/AI command entry, atomic validation/commit, state queries and presentation models |
| Persistence | Versioned state snapshots, migrations, validation and atomic file replacement |
| World/Content | Geographic preprocessing, manifests, runtime content loading and historical initialization |
| Unity Presentation | Camera, terrain/chunks, pooled visual proxies, spline meshes, animation and audio |
| UI | Localized user workflows, explanations, selection, charts and confirmations |
| Editor/Tests | Content validation, asset baking, headless fixtures, build scripts and automated tests |

Keep the domain/simulation free of GameObject/Transform authority. UI and AI issue the same validated commands. The rendering layer observes state and cannot independently decide arrivals, payments, loading completion or vehicle availability. Definition authoring may use ScriptableObjects, but copy validated immutable definitions into simulation data; do not mutate global asset definitions as per-save state.

Recommended directory families: `Assets/Tranzit/Core`, `Simulation`, `Planning`, `Application`, `Persistence`, `Presentation`, `UI`, `Content`, `Editor`, `Tests/EditMode` and `Tests/PlayMode`; `Tools` for build/preprocessing; `DataSources` for provenance metadata, not secret credentials. These names may be adapted consistently.

### 4.3 Shared state, transactions and explanations

Use stable IDs rather than scene references. All assets, facilities, companies, cargo portions, bookings, contracts, allocations, jobs and graph elements have persistent identities. Money and cargo quantities use integer/fixed-point representations with checked arithmetic and an explicit rounding rule. Distances/geometry use appropriate precision and documented tolerances.

A command has an identity, expected state/version where needed, validation result, quoted effects and an atomic commit. Revalidating before commit prevents a stale planner preview from spending already committed money or booking sold capacity. Repeated commands/events must not double-charge, deliver twice or duplicate assets. Physical stages still take time after a successful commercial transaction.

Central ledgers cover money postings, cargo inventory/custody, segment-specific capacity, vehicle duties, staff capacity, workshop/handling resources and access commitments. Maintain separate ledger types but shared IDs and dependency links; do not build incompatible approximate copies in the Contract Planner, AI and dispatcher.

Return structured reason codes with inputs, affected IDs, constraint thresholds and proposed remedies. Codes might include `Cargo.NotReady`, `Capacity.ProtectedConflict`, `Route.NoCompatiblePath`, `Crew.QualificationShortage`, `Workshop.NoCompatibleSlot` and `Save.ContentVersionMismatch`. Localize their presentation, not their identity.

Planning previews are side-effect free. A grouped Capacity Order may coordinate several owners, but cannot leave a service advertised as fully protected after a partial purchase failure. Keep every accepted agreement and its costs explicit; abort/release temporary holds safely.

### 4.4 Simulation execution and scale

Use one fixed-resolution simulation timestamp, for example Int64 milliseconds, with an event queue ordered by timestamp, event phase and stable sequence ID. Choose and document a causal order for simultaneous arrivals, completed handling, readiness cutoffs, allocations and departures. A cargo lot is ready only after its handling-complete event. Identical timestamps must not randomly turn into a successful or missed connection.

Wall-clock elapsed time produces a simulation-time budget using the approved multiplier. Advance to chronological events/trajectory boundaries; integrate movement as needed between them. A renderer frame is not a simulation tick. Do not drive all logic by Unity Time.timeScale or by a once-per-real-second economic coroutine.

Use network positions (edge/path ID and distance along it) plus orientation and real consist geometry. Swept movement and reservation transitions must protect short sections, junctions and the full train length even when a frame spans many game seconds. Release a block only after the tail clears. Use kinematic route-following; full-wheel rigidbody physics is not required.

Replan on relevant events and bounded scheduled reviews. Cache by graph/service/contract versions; invalidate affected subgraphs rather than the whole map. Generate upcoming Trips within a rolling horizon, not every departure for a century. Longer commitments use validated recurring patterns and bounded reservation windows, not infinite concrete objects.

Active-region simulation and visual streaming are different. An active region remains simulated after its terrain/vehicles leave the camera. Inactive regions remain macro state until legally activated. Activation transfers ownership/state exactly once and cannot generate duplicate customers, trains or inventory. Visible pedestrians/private traffic are representative proxies of aggregate state, not a new source of demand.

If hardware cannot sustain selected speed, report measured requested versus achieved speed. Do not silently advance finance/history ahead of transport or drop essential events. Use rendering culling, work scheduling and bounded caches; a stress-test shortfall is a defect/report item, not permission to fake 16x.

### 4.5 Persistence

Use a versioned save envelope with schema version, build version, content-manifest hash, save ID, simulation time and checksum. Write to a temporary file and replace the target only after a valid complete write; keep a last-known-good backup. Respect storage failures and cancellation without deleting the previous good save.

Serialize authoritative state and random-stream positions. Include future events or enough validated state to reconstruct them exactly once; never both restore an event and regenerate its duplicate. A snapshot must correspond to a consistent simulation boundary, even when disk writing happens asynchronously.

Loading validates IDs, content versions, graph connectivity references, ledger conservation and reservations before admitting new commands. Unsupported/newer saves fail with an actionable explanation. Migrations must be explicit and tested; never silently discard cargo/contracts because a definition changed.

Default controls/settings: manual named slots, autosave with three rotating slots at a configurable five-real-minute interval, quicksave F5, quickload F9 with overwrite/loss confirmation, and Continue pointing to the newest valid compatible save. These are implementation defaults and remappable. No game time advances while the load operation is incomplete.

## 5. World and content production

Build one authored, versioned world covering the approved geography, not a random miniature map labelled with real city names. Terrain/water/settlement locations come from provenance-tracked geography; historical population, industry, road/rail layers, jurisdictions and operators are authored or sourced separately for 1900.

The preprocessing pipeline must validate and produce offline runtime chunks, graph data, settlement anchors, historical overlays, material/biome data, catalogue manifests and source/attribution records. Pin data versions and hashes. Bake before release; gameplay must not query OSM, map tiles or a terrain API.

Copernicus GLO-30 is a candidate elevation source, but its documentation describes a modern digital surface model including buildings/vegetation, not a ready-made historical bare-earth terrain [R5]. Smooth/clean or replace inappropriate surface features and author necessary historical corrections. Do not claim modern data reconstructs 1900 automatically. OSM is a possible geometry source subject to its actual ODbL and attribution requirements [R6]. Review each selected dataset's redistribution conditions; do not assume that any map visible on the web may be bundled.

Separate current administrative labels used to describe geographic coverage from historical jurisdiction data. The release must carry a documented 1900 jurisdiction layer and recorded, date-converted historical transitions where content covers them. Research and cite real historical facts when authoring that data; this brief is not a historical boundary dataset.

Provide explicit entry/exit and import points at the world boundary. Once an imported asset enters the active world, it uses normal physical movement. No hidden teleportation across an active map.

Use a coarse world overview and finer streamed local chunks. Test seams, river continuity, track/road endpoint matching, picking and floating-origin shifts. Route lengths cannot change as a consequence of LOD or camera distance. Persistent construction/terrain edits overlay immutable base chunks and survive unload/reload.

A small verified development fixture is acceptable while building the pipeline, but it is labelled a fixture and does not fulfil the full-world release gate. If source acquisition is blocked, retain a concrete blocker and work on other systems; do not silently present a flat fictional substitute as the agreed map.

## 6. Functional subsystem contract and design traceability

The following rows define minimum operational behaviour, not just class names. Every row needs a player-visible workflow, actual state effects, save/load coverage and tests.

| ID | Core design sections | Required first-release behaviour |
|---|---|---|
| SYS-01 | 1–5, 41 | Shared clock, no-grid world, logical physical continuity, streamed presentation, reproducible simulation and structured explanations |
| SYS-02 | 2–3, 6, 35–36 | 1900 world, legal region expansion, aggregate inactive world, season/day cycles, demand changes, visible city development and historical/technology events |
| SYS-03 | 7–9, 28 | Physical branches, office setup/equipment/staff/workload, named directors/managers, salary/qualified labour supply, delegation permissions, reputation and customer-specific history |
| SYS-04 | 10–11 | Firms with inventories, production/consumption, capacity and cash-flow constraints; real cargo/passenger opportunities, tenders, bids, contracts, SLA, bonuses, renegotiation, expansion, cancellation and renewal |
| SYS-05 | 11–12, 30 | Contract/shipment transport plans, split lots, multi-leg routing, physical storage, cutoffs, allocation protection, recovery and external carrier procurement |
| SYS-06 | 13–14, 19–20 | Road/rail compatibility, railway section and station capacity, dynamic tracks/platforms, access ownership/charges, coordinated capacity ordering and actual occupancy |
| SYS-07 | 14–18 | Per-asset fleet, physical shunting/turning, consistent duties, manufacturer/dealer/used/lease acquisition, delivery, fuel/supplies, service, retrofit, rescue and scrapping |
| SYS-08 | 21–26, 39 | Land/corridors, construction contractors/materials/stages, earthworks through projects, bridges/tunnels, closures/upgrades, demolition and whole/partial infrastructure transactions |
| SYS-09 | 6, 14.5, 31–34 | Aggregate passenger OD choice and waiting queues, actual ticket channels/tariffs/reservations, capacity by leg/zone, crowding/service factors, transfers, missed-connection recovery and permitted local bus service |
| SYS-10 | 11, 32 | Line → versioned Service Pattern → dated Trip, calendars, slot-driven timetables, fixed/criteria/hybrid consists, vehicle/crew duties, preparation, disruption policies, suspension and resumption |
| SYS-11 | 15–18, 27–28, 40 | Technology introduction/adoption, non-vehicle research, enduring historic models and economically changing external support; own workshop alternatives |
| SYS-12 | 29–30, 39 | Autonomous carriers and constrained suppliers, real bids/services and physical assets, insolvency, shares/acquisitions, separate controlled subsidiaries with Autonomous/Managed/Direct-control modes, explicit intra-group transactions, optional integration, infrastructure ownership continuity and partnerships |
| SYS-13 | 9, 11, 19, 38–39 | One money ledger, quotes/payment schedules, favourable startup debt, later borrowing, operating cash flow, selling assets, distress/restructuring and eventual failure |
| SYS-14 | 16, 25, 35–37 | Wear, speed restrictions, breakdowns, closures, weather impacts and rare serious incidents, with causality, recovery and proportional consequences; UI-D40 presents significant world/historical context separately from UI-D24 operational incidents |
| SYS-15 | 1.1, 4 + V1_SCOPE | Complete localized UI, camera/selection/construction interaction, coherent graphics, basic audio, readable explanations and onboarding |
| SYS-16 | V1_SCOPE + 41–43 | Full persistence, validated content, build/run instructions, regression tests, soak/performance results and truthful release status |

Sections 33–34 apply to local buses only in V1. Section 13.3 and water-specific facilities are deferred with the mode. Section 42 remains the explicit wider deferred list. Do not silently delete basic acquisitions/shares from Section 29.1 under the excuse that finance is simple; conversely do not introduce a speculative stock-exchange simulator.

### 6.1 Make the new company start possible without cheats

Seed a working economy, not a dependency deadlock. There must be genuine existing contractors, suitable office space, labour pools, vehicle sellers, compatible maintenance providers, supply sellers and external carriers in viable starting areas. These entities have real finite resources and commitments.

A new company cannot need a player-built railway to buy its first road vehicle or need its own transport fleet to obtain the office that unlocks every opportunity. Contractor-supplied construction logistics and third-party delivery/maintenance are existing design paths; implement them.

The small founding loan must support at least one legitimate small-road opening with office(s), necessary director/staff, permissions, vehicle, endpoints, support and working capital. The standard/large tiers should offer wider viable choices, including a modest rail opening using leased/third-party infrastructure where the balance permits. Do not promise every opening in every region with every tier.

Discovery remains branch/locality based until company technology broadens it. Before a branch is operational, the UI may preview premises/seller/setup costs and public aggregate market indicators, not reveal the hidden routine local Opportunity Board or allow acceptance of undiscovered jobs. Eligible public/direct opportunities still follow Section 7.2. Setup previews do not grant branch benefits. Starter recommendations are real purchasable plans, not free fleet/branch templates.

### 6.2 Network operation and dispatch

Build geometry validation before activating a network: joins, curvature, gradients, gauge/clearance, axle load, platform fit, power systems and turnability. Signal/block objects represent operational resource protection. A global capacity estimate is not collision protection.

Distinguish commercial rail/station slot windows from actual track/platform occupancy. Timetable construction validates the complete chain of offered-window midpoints, running margins and dwell under the core design. Early slot tolerance never authorizes leaving a published passenger boarding stop early. Dynamic routing cannot change published commercial stops or violate access/traction requirements. An operational deadlock requires a safe, explainable recovery plan; no train deletion or arbitrary nudging.

Steam equipment may perform only explicitly supported reverse/run-around/turning movements. A permitted reverse movement is a real kinematic operation with any applicable limits, not teleportation or an instantaneous 180-degree model flip. Coupling and decoupling use actual asset orientation, track geometry, crew/equipment and capacity.

Roads have connected lane/direction/turning restrictions, intersection conflicts, endpoint entrances, road capacity, queues and turning/loading space at useful granularity. A bounded kinematic queue/intersection model is sufficient; a full urban driving simulator is not. Private traffic is aggregated and represented visually. Freight must not be delivered because a truck passed near the destination without visiting its loading point.

### 6.3 Business and recovery integration

Reuse one requirement checker for pre-contract quotes, Pattern activation, AI bids and final Trip readiness. Forecast and actual state remain distinct: a projected available locomotive is not a vehicle physically on the departure track.

Contracts can be signed against a credible future investment plan, but construction, licences, staffing and delivery remain real dependencies. Auto-renew does not automatically purchase supporting services, force a tender win or accept changed price/scope beyond accepted clauses.

External Transport Orders cover subcontracted cargo legs, vehicle delivery, materials/fuel and specialist movements. Providers consume genuine equipment/crew/route capacity. Do not create a different fake delivery system inside every marketplace.

Cargo uses the canonical GAME_DESIGN Section 11.9, referenced by V1_SCOPE Section 5. Implement capacity per usable wagon/vehicle pool and traversed stop interval; tonnes alone are insufficient. Passenger bookings use the same principle of segment occupancy, but keep their own zone/product and reservation rules.

Prepare physical vehicles and crews early enough to cover repositioning, maintenance, shunting, fuel, cleaning and boarding. Partial failures use configured substitution/wait/reduced-capacity/cancel policies. Resolve passenger/cargo consequences after the final feasible consist is selected. No required driver is replaced by a generic service-quality penalty.

Cancellation/lease expiry must not teleport a running asset back to its owner. Stopping a Line preserves its obligations, history and sold tickets and offers an explicit capacity-retention/release choice. Reopening runs readiness checks again.

### 6.4 Economy, competition and development

Production recipes consume inventories and produce defined outputs. Missing inputs affect real production and transport demand. Imports/exports at macro boundaries may use aggregate external supply, but not unlimited free supplies inserted directly into player facilities.

Ordinary employees are aggregate qualified capacity. Named managers/directors use the shared labour market with real availability, salary, relevant skills, workload and budget permissions. AI carriers use the same market and command validation. Avoid omniscient future disruptions, perfect guaranteed bids or camera-dependent cost exemptions.

A minimum AI loop evaluates opportunities, plans feasible investment, bids, procures, staffs, starts a service, maintains it, responds to failures and adjusts or exits. Separate strategy policy from shared execution. City/public operators provide existing services under the same physical/capacity accounting, with explicit public funding if applicable.

Reputation, attractiveness and service quality expose measured factors rather than an opaque all-purpose score. World development reacts to transport access, goods and employment as well as its historical baseline. Later technology changes machinery and management capabilities; it must not simply add +10% profit.

## 7. Milestone sequence

Each milestone includes visible integration, tests and a status update. Continue working on later milestones after a passing gate; do not ask the user to reapprove decisions already in V1_SCOPE. Do not begin by generating skeleton classes for every section without one executable loop.

| Milestone | Work | Exit evidence |
|---|---|---|
| M0 — Reproducible foundation | Inspect working tree/toolchain; pin Unity/packages; project/scenes/build entry; core IDs/units/calendar/events/RNG; content schema; save skeleton; one consistent UI theme | Project compiles; standalone menu opens; clock/units/command/save round-trip tests pass |
| M1 — Visible world and small road business | Verified geographic fixture with evolving production and public roads; camera/picking; offices, loan, staff/licence, stock purchase/delivery, depot, endpoints; one-off road cargo and cash postings | From New Game, establish a company and deliver paid cargo through UI, save/reload mid-trip; actual recognizable vehicle/building models |
| M2 — Railway operation and construction | Track graph/splines, construction/land/cost, junctions/blocks, stations/yards, rail delivery, physical shunting/turning, traction/length checks, rail freight and access slots | Player constructs a useful siding or loop and operates paid rail freight; cannot book/dispatch an incompatible or colliding train |
| M3 — Shared network logistics | Complete Contract/Line/Pattern/Trip hierarchy, physical multi-leg plans, split cargo, capacity ledgers, scheduled/ad-hoc work, cutoffs/recovery, storage and external transport | Split shipment travels road → rail → road over multiple Trips; a cancelled connection triggers valid partial recovery without duplication |
| M4 — Passenger operation | Local/intercity bus and rail passenger services, demand/tariffs, real sales channels, class/zone reservations, queues, transfers and rebooking/refunds | Commercial passenger round trips and a protected transfer work; reduced capacity/late connection yields visible recovery and correct finance |
| M5 — Full business and autonomous competitors | Finish opportunity/tender/contract lifecycle, staff/managers/delegation, loans/distress, autonomous procurement/operation, infrastructure market and basic ownership/acquisitions | Rival wins and runs feasible business, expands/maintains or fails; player can delegate and acquire/sell without duplicated assets/debt |
| M6 — Lifecycle, progression and disruption | Fuel/energy/supplies, all service/retrofit/lease/scrap paths, breakdown/rescue, construction materials/closures, weather/history, technology/office adoption, long-lived equipment/support economics | End-to-end maintenance/rescue/upgrade/renewal tests; old technology stays usable with actual support costs; future-state fixtures do not require new start presets |
| M7 — Full approved world and content | Complete offline geographic coverage, active/macro region transitions, historical initialization, coherent modular art/audio, both locales, onboarding, settings and all content minima | Actual standalone build covers approved territory and content; no placeholder main panel, missing asset or unresolved setup deadlock |
| M8 — Release verification | Run full acceptance suite, cross-system failure matrix, long-run/save tests, benchmarks and manual walkthroughs; fix blockers; package reproducible Windows build | V1 release gates pass with evidence. All unrun/failed tests and material limitations are explicitly listed |

M1 may use a compact fixture; M7 cannot. M5 does not permit earlier fake AI resources: build shared accounting from M0/M1 and incrementally expand AI behaviour. Art, localization and save support start early and continue through every milestone.

## 8. Essential UI and player flow

Keep one selection/context system and reusable parameter/confirmation components. A new player should be able to follow: choose 1900/region/loan → choose office → appoint director and staff → inspect opportunity → compare transport plan → secure dependencies → activate service → inspect revenue and problems. All steps are linked from their context, rather than forcing the player to find a hidden developer panel.

Required player screens/workflows:

| Workflow | Minimum usable presentation |
|---|---|
| Start/pause/settings/save | UI-D35 New Game/real company-founding flow plus UI-D36 main menu, campaign-organized manual/quick/autosaves, atomic save feedback, independent pause reasons, Esc priority and Graphics/Audio/Game/Controls/Interface/Language settings |
| World interaction | Rotate/pan/zoom, selection, follow vehicle, hover details, navigation to an event, legend and network/ownership overlays |
| Construction | Catalogue, ghost preview, rotate/snap, valid/invalid geometry, itemized quote, confirm/cancel, progress and affected operation |
| Company | Branches and workload, salary/crew reserve, managers/delegation, finances/loans, legal access/region expansion, UI-D39 group holdings/subsidiary strategy and active-company context |
| Commercial | Filterable opportunity board, contract planner/readiness/economics, bid/accept/amend/cancel/renew, shipment progress |
| Operations | Lines/Pattern versions/calendars, capacity orders/timeline, duties/fleet assignment, departures, actual delays and action reasons |
| Assets | Marketplace, order/delivery tracking, physical fleet details, workshops/service policies, fuel/storage/support |
| Passenger/cargo detail | Per-leg commitments, actual quantity/capacity, queues/transfers, protected reservations, recovery and cost consequences |
| World/business context | Cities/firms/production, competitors, partnerships, UI-D39 company/infrastructure acquisitions, UI-D38 Technology/research/adoption, UI-D40 World News/history and major disruptions |

Aggregate data must be drillable. A disabled action explains its specific blocker and links to a corrective workflow. Distinguish simulation facts, estimates and commercial promises. No decorative financial chart with invented data.

Provide the UI-D35 opening onboarding only while a new company is being founded. Tutorial mode is Full / Basics only / Off. The startup checklist derives from real branch/staff/licence/asset/operation state, grants nothing for free, and ends after the first functioning transport operation; it must not become a permanent campaign task list. Optional first-use context help may remain dismissible according to tutorial mode. Normal blockers, Needs decision incidents, invalid-action explanations and consequence previews are not tutorial content and remain enabled. Buying/cancelling costly obligations requires a visible consequence preview; preview cancellation itself is free.

## 9. Graphics and audio production rules

Use a coherent diorama palette, believable scale, softened materials, readable silhouettes, directional light/shadows, atmospheric distance and restrained post-processing. Avoid mandatory heavy depth-of-field that makes operational details unreadable. Provide quality tiers, readable UI at 1080p and an adjustable scale for higher resolutions.

Vehicles need wheels/undercarriages, a recognizable propulsion/body shape, coupling points, correct orientation, materials and movement animation. Steam uses economical visible smoke/steam effects at relevant LOD. Cargo/coach silhouettes should be identifiable without labels. Body repaint alone is not a new functional asset.

Terrain needs relief, rivers, forests/fields and settlement structure. Buildings should form recognizable Central-European street/block patterns instead of an American grid. Modular authored assets may be procedurally assembled inside constrained geographic/historical footprints; this is not the deferred random world generator.

Provide actual switch/track connections, bridge spans/supports, tunnel portals and construction stages. The player must see the operation the simulator claims is occurring. Coupling/loading can be visually simplified, but not replaced with teleportation. Use representative pedestrians only where useful.

Basic vehicle, environment and UI audio with volume controls is part of the playable presentation. Music is optional; voice acting is not required. Track origin/licensing for external assets and audio. Do not bundle paid assets without authorization or present generated screenshots as in-engine evidence.

## 10. Validation and release discipline

[V1_ACCEPTANCE_TESTS.md](V1_ACCEPTANCE_TESTS.md) is the test contract. Use property/invariant tests for conservation and atomicity, deterministic integration fixtures for timetables/AI/failures, PlayMode tests for controls/scene integration, and manual standalone-build verification for real UX and graphics.

After each milestone, record requirement ID, files, tested scenario, exact run command/build/seed, result and evidence location. A status of implemented is not a status of tested. `Not run` is required when a toolchain, licence, machine or dataset is unavailable. Compilation is not visual validation; a happy-path video is not an edge-case suite.

No fatal blocker can be waived by calling the build a prototype while presenting it as V1. Release blockers include save corruption, duplication/loss of resources, unsafe collision/teleportation, fabricated AI, no legitimate way to start a business, missing approved territory, required online gameplay, nonfunctional main systems and debug-only presentation.

Use a developer stress/incident harness to reach later dates and failures without asking the player to wait hundreds of hours. Such fixtures do not become unauthorized faster gameplay speeds, free money buttons in normal play or new starting presets.

## 11. Agent execution and interruption handling

First inspect the repository, current branch/status, toolchain and installed packages. Preserve unrelated user changes. Create a working implementation branch using normal repository practice; do not force-push or perform destructive cleanup. Prepare only the small amount of design/ADR work necessary to start M0, then implement.

Prefer small verifiable changes. Every executable command must have a meaningful completion condition and a bounded timeout. Long-running Unity Editor, game, watch, server or log-tail processes must be launched separately with a PID/log and checked explicitly; do not await a process that is designed never to exit. On timeout, inspect the log and failure cause rather than launching more identical processes or waiting indefinitely.

If the Editor/compiler is unavailable, report that exact limitation and do not claim a compiled game. Work on testable nonblocked parts, configuration, content and build automation. Do not ask additional product questions about approved modes, calendar, money, languages or map scope. Routine technical choices go into a short ADR. An actual external credential, paid licence or unsupported environment requirement must not be invented.

At an interruption/context boundary, persist what changed, what really passed/failed, current blockers and the next executable task in IMPLEMENTATION_STATUS.md. The next session resumes from evidence rather than redrafting the plan. Do not mark later gates passed in anticipation of future work.

## 12. Primary technical references

Verified as reference pages during handoff preparation, 2026-09-30. Recheck version-specific APIs when pinning the actual project. These sources document capabilities/conditions, not proof of Tranzit implementation or performance.

- R1: Unity 6 release/support overview — https://unity.com/releases/unity-6
- R2: Unity Manual, Universal Render Pipeline introduction — https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-introduction.html
- R3: Unity Splines manual (reference version 2.8, not a mandatory project pin) — https://docs.unity3d.com/Packages/com.unity.splines@2.8/manual/index.html
- R4: Unity Localization manual (reference version 1.5, not a mandatory project pin) — https://docs.unity3d.com/Packages/com.unity.localization@1.5/manual/index.html
- R5: Copernicus DEM official collection, data type/access and source obligations — https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM
- R6: OpenStreetMap copyright and licence information — https://www.openstreetmap.org/copyright

Actual historical geography/vehicle data needs additional item-level sources and plausibility validation during content production. No historical map data or third-party asset files are supplied by this handoff.
