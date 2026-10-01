# AGENTS.md — Tranzit project rules

This repository contains **Tranzit**, a Unity transport/business simulation.

## Source of truth

Before implementing or proposing gameplay/system changes, read:

- `docs/GAME_DESIGN.md` — the core game design. Section 3 is authoritative for the shared calendar, historical progression, the wider start-year model and Early Ages scope.
- `docs/CONTRACT_CANCELLATION.md` — the focused rules for proportionate cancellation fees, early slot release and the distinction from non-renewal. Required for contract, capacity, renewal, finance and manager-permission changes.
- `docs/V1_SCOPE.md` — the approved first-playable release subset and cross-system clarifications, including split shipments and enduring historical vehicle availability.

For implementation work also read:

- `docs/CODEX_V1_MASTER_PROMPT.md` — persistent autonomous implementation assignment and M0–M8 execution contract;
- `docs/ENGINEERING_STANDARDS.md` — mandatory engineering conventions, architecture boundaries, optimization/performance rules and quality practices;
- `docs/V1_IMPLEMENTATION_BRIEF.md` — architecture guidance, subsystem coverage and milestone order;
- `docs/V1_CONTENT_MANIFEST.md` — configurable initial content/balancing targets;
- `docs/V1_ACCEPTANCE_TESTS.md` — required test scenarios and release evidence;
- `docs/TODO.md` — the living backlog of remaining/open/deferred work; read it before substantial work and keep it current when discovering, completing or deferring real tasks;
- `docs/IMPLEMENTATION_STATUS.md` — actual implementation progress, test/build results and evidence; never use TODO completion as implementation evidence;
- `docs/OPENCODE_START.md` — concise entry point that delegates execution to the persistent Codex assignment.

Document responsibility is explicit:

- `GAME_DESIGN.md` owns shared game mechanics, including the calendar (3), cargo identities/invariants (11.9) and enduring vehicle availability (15.11).
- `V1_SCOPE.md` owns the first-release inclusion/exclusion boundary. Its summaries link to the shared mechanics rather than redefine them.
- `CONTRACT_CANCELLATION.md` owns the focused ordinary-cancellation calculation and settlement rules.
- `CODEX_V1_MASTER_PROMPT.md` owns the autonomous implementation workflow; `ENGINEERING_STANDARDS.md` owns engineering conventions/performance practices. Neither may override gameplay. The brief and content manifest own engineering guidance and adjustable defaults, not silent product overrides. `DATA_PIPELINE.md` owns documented import conventions.
- Acceptance scenarios define required evidence; `IMPLEMENTATION_STATUS.md` records only observed progress/results. Neither creates a gameplay exception.

There is no universal "last paragraph wins" rule. A genuine mechanics conflict still requires correcting the owning section and its dependent summaries/tests; do not treat a release-scope document or example as blanket permission to override it.

Run `python3 Tools/check_docs.py`, `python3 Tools/check_vehicle_content.py` when vehicle content data is touched, and `python3 -m unittest discover -s Tools/tests -v` after documentation/content edits. These check documentation/data structure and selected explicit regressions, not the correctness or completion of the unimplemented game.

Together these form the **living source of truth**, not a historical log. The core design describes the wider game; V1_SCOPE explicitly narrows the first release's modes and start presets without deleting the broader design. Focused specifications elaborate core rules and are not optional notes.

When a design decision changes:

1. Read the complete relevant sections first.
2. Identify every existing rule/system affected by the change.
3. Resolve contradictions instead of appending a second conflicting rule.
4. Rewrite/remove obsolete text in the core and affected focused specifications.
5. Only then implement the change.
6. Keep code and documentation aligned in the same change whenever possible.

Do not silently reinterpret a discussion example as overriding an existing contractual guarantee. The canonical cargo rules in GAME_DESIGN Sections 11.0.1 and 11.9 use compatibility and contractual priority tiers, not one unrestricted hidden score.

## Living TODO/backlog discipline

`docs/TODO.md` is the repository's single living backlog for **what remains to be done**.

Use it as follows:

1. **Read TODO before substantial work.** Reconcile the requested task with its current Now / Open decisions / Next / Blocked / Deferred state and the authoritative design documents.
2. **Add newly discovered real work immediately.** If implementation/design work uncovers a missing decision, follow-up, blocker, required reconciliation or test task, add it to TODO instead of relying on chat/session memory.
3. **Keep Now small and actionable.** Move lower-priority work to Next. Use Blocked only for a concrete dependency that prevents progress; use Deferred for intentionally postponed work that is not a blocker.
4. **TODO never overrides the design.** A backlog item is a pointer to work, not a gameplay rule. When a product/design decision changes, update the owning specification first, reconcile affected summaries/tests, then update the TODO entry.
5. **Design done is not implementation done.** When a specification is approved, close the design TODO item after its docs are reconciled. Do not infer that code exists.
6. **Implementation done requires evidence.** When code work completes, update `docs/IMPLEMENTATION_STATUS.md` with actual paths, test/build commands and observed results before closing the corresponding implementation/test TODO item.
7. **Do not duplicate the full project plan.** M0–M8 and SYS-01–SYS-16 stay in the implementation brief/status ledger; release test definitions stay in V1_ACCEPTANCE_TESTS. TODO links to those owners instead of copying them.
8. **Keep Done recently short.** It is only a convenience recap. Git history and canonical design/status documents are the permanent record.
9. **Update TODO in the same change where practical.** A completed, newly blocked or newly discovered task should not leave the backlog knowingly stale.
10. **Before ending substantial work, inspect TODO again.** Record any remaining follow-up, exact blocker and next action so the next session can continue without reconstructing context.

If TODO and IMPLEMENTATION_STATUS disagree, resolve the stale document rather than choosing whichever is more convenient. IMPLEMENTATION_STATUS is authoritative for observed implementation/test evidence; owning design documents are authoritative for accepted behaviour.

## First-playable delivery contract

Implement an actual offline Windows game with coherent 3D graphics, Czech/English UI and full persistence. Do not stop at a scaffold, blank UI, isolated simulation or one moving train and call it V1.

The first release uses the **1900 start only**, with continuing historical/technology progression, **rail and road** for freight/passengers, local/intercity buses, the approved Czech-and-adjoining-region world, one unit named **money**, real competitors and the applicable connected business/operational systems. Passenger inter-operator cooperation is limited to the defined bilateral **partner-capacity-sale through-ticket** mechanism; ordinary transfers create no separate passenger connection-agreement, protected-transfer or hold subsystem. Later start presets and water/tram/trolleybus/metro operation remain future base-game scope. Aircraft remain excluded.

Simple coherent original modular assets are acceptable. Debug primitives with labels are not finished player-facing graphics. Develop presentation, localization, persistence and tests alongside the simulation.

V1_CONTENT_MANIFEST numerical targets are engineering defaults, not user-approved immutable balancing. Improve them transparently without reducing approved scope. Do not reopen product questions already answered in V1_SCOPE.

Milestones M0–M8 are internal delivery stages of the same target. Preserve progress and real evidence in IMPLEMENTATION_STATUS. A documented requirement is not an implemented feature; implemented code is not a passing test; an unrun build must never be reported as tested.

## Mandatory consistency review

For every new feature, explicitly check interactions with:

- physical continuity of vehicles/assets and cargo custody;
- the shared time/calendar model and selected start year;
- base-game, first-playable and Early Ages scope;
- technology progression and lasting support for older equipment;
- economy, inventory and contracts;
- ownership/licensing/state rules;
- infrastructure capacity and geometry;
- maintenance and workforce;
- management/delegation;
- regional unlocking and inactive-world simulation;
- AI competitors;
- performance/simulation LOD;
- save/load and idempotent state transitions;
- UI/player comprehensibility and explainability/no-hidden-mechanics requirements.

Do not implement a feature in isolation if it breaks an existing system.

## Core design constraints

### Physical continuity

Vehicles and rolling stock never teleport, magically reverse or disappear into abstract depots.

A remote asset may be simulated without rendering, but its logical position/state must remain continuous. Train composition changes require actual physical operations. Cargo quantities have one authoritative physical location and are not moved merely by changing a reservation.

### Scale/performance

Design for a very large world from the beginning.

Prefer event-driven logic, cached calculations, coarse economic ticks, simulation LOD, batched cargo, aggregated population and aggregate inactive regions.

Avoid per-frame economic simulation, persistent per-person simulation for entire cities, repeated full-network pathfinding and deep per-component vehicle simulation unless specifically approved.

Rendering distance and origin rebasing cannot change logical positions, route lengths, reservations, costs or outcomes. Preserve full-train occupancy and essential events at every supported speed.

### No grid world

Infrastructure is free-form/spline based. Buildings can rotate freely. Snapping is used only for real connections.

### Progressive automation

Early game can be hands-on. Later game must remain manageable through managers, dispatchers and technology without deleting the underlying physical rules. Managers obey explicit approval/budget policies.

### Explainable simulation / no hidden mechanics

Do not implement material gameplay outcomes as opaque hidden modifiers when the underlying causes can be exposed.

For systems affecting feasibility, pricing, demand, reliability, reputation, contracts, staffing, capacity or disruption, preserve enough structured information to explain:

- what happened;
- which inputs/rules caused it;
- which constraints blocked an action;
- which costs/penalties/bonuses were applied;
- what the player can change to improve the outcome.

Aggregate scores are allowed for readability only when the player can drill down into their contributing factors.

Prefer structured **reason codes / contributing factors / source values** over returning only a final unexplained number or boolean.

UI may surface this through hover/focus tooltips, pinned explanations and nested highlighted terms. Do not hardwire simulation logic to one specific tooltip implementation, but keep explanation data available.

### Historical plausibility and content scope

The wider base-game default/earliest start is **1900**, with later selectable starts **1925, 1950 and 1975**. Only the 1900 preset is required in first-playable V1; the simulation continues beyond that year.

The pre-1900 playable period, intended to start around **1820**, is reserved for the first planned DLC, **Early Ages**. Do not implement that earlier startup progression as a mandatory base-game requirement. Preserve shared systems and historically surviving older assets where relevant to the selected date.

Initialize technology, economy, population, jurisdictions, infrastructure, competitors and vehicle catalogue for the selected year. A small player company does not reset the entire world to an earlier era. Later presets must not force re-research of already established inventions; actual equipment, facilities and staffing still need to be acquired.

An introduced historical model has no hard end-year that removes it from the catalogue or disables serviceable assets. Finite sellers/manufacturers and changing external workshop/parts capability determine actual offers and support. Own equipped/staffed support is a real alternative, not free repair. Do not manufacture unexplained obsolescence penalties or compulsory scrapping.

### Unified calendar and time controls

Use the single simulation clock defined in GAME_DESIGN Section 3:

- 7 days per week;
- **14 days per month**, exactly two weeks;
- **12 months and 168 days per year**;
- 24 hours per day, 60 minutes per hour, 60 seconds per minute;
- **1 real second = 1 game minute at 1x**;
- running speeds **0.5x, 1x, 2x, 4x, 8x, 16x**, plus pause;
- slowest running speed **0.5x**, maximum **16x**.

Do not reintroduce an independently accelerated historical calendar, the retired 100–150-hour campaign target or speeds above 16x. Year 2020 is a duration reference, not a mandatory game ending.

Timetables, slot windows, transfers, cargo ageing, crews, maintenance, production, construction, finances, research, contracts, cancellation and renewals use the same game-time units. Never assume Gregorian month lengths or a 365-day financial year. Historical source dates use the explicit versioned import conversion in GAME_DESIGN Section 3.4 and docs/DATA_PIPELINE.md. Apply it once to source dates, not to already-authored game dates; runtime systems never use Gregorian period arithmetic.

Route length and performance determine game-time travel. Rendering follows the same simulation, not an independently slowed travel clock.

Validate calendar rollover, seasonal/cross-year patterns, billing/resource accounting and mid-operation speed changes. Equivalent simulated elapsed time must not yield different economic accounting because another speed was selected. Optimize rendering/update scheduling rather than skip movement, reservations or essential events to claim 16x performance. Benchmark developed networks before claiming that speed is sustained.

### Scope discipline

Do not add major unapproved systems merely because they are realistic. Tranzit aims for depth where it creates transport/business decisions, not simulation for its own sake.

## Architecture

Inspect the current Unity project and design before locking architecture. The handoff baseline had no Unity project; inspect again rather than assuming that is still true.

When introducing a subsystem:

- keep simulation state separable from rendering;
- share feasibility rules/ledgers among player, AI and planners;
- keep data definitions extensible across eras/regions;
- use the shared calendar instead of local conflicting clocks;
- make systems work with simulation LOD;
- avoid hardcoding cities, regions or vehicle models into core logic;
- prefer deterministic/state-driven simulation where practical;
- implement save/load compatibility and transaction idempotency from the beginning.

Use current compatible stable packages and pin versions. Technical choices and initial balances may be resolved with short documented decisions; do not turn them into another round of already-settled product questions.

## Development behavior

Before substantial work:

1. inspect the actual repository/working tree and preserve unrelated changes;
2. inspect the current source of truth and implementation status;
3. identify affected systems;
4. document any genuine design compromise;
5. update documentation when design changes;
6. implement, test and record actual evidence.

Use bounded process timeouts and logs. Do not await indefinitely a running Editor, game, server or watch process. Keep long-running processes separate with explicit readiness checks.

On interruption, persist completed work, actual test results, blockers and the next executable task. A missing toolchain, credential or dataset must be reported precisely; do not invent a passing build or silently replace the approved world/gameplay.

Never silently change agreed behaviour merely to make implementation easier. Do not force-push or destructively clean user work. Keep all status and completion claims tied to observable evidence.
