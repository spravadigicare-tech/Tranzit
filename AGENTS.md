# AGENTS.md — Tranzit project rules

This repository contains **Tranzit**, a Unity transport/business simulation.

## Source of truth

Before implementing or proposing gameplay/system changes, read:

- `docs/GAME_DESIGN.md` — the core game design. Section 3 is authoritative for start dates, the shared calendar, speed controls and Early Ages scope.
- `docs/CONTRACT_CANCELLATION.md` — the current focused rules for proportionate cancellation fees, early slot release and the distinction from non-renewal. Required for contract, capacity, renewal, finance and manager-permission changes.

Together these form the **living source of truth**, not a historical log. Focused specifications elaborate the relevant core sections; do not treat them as optional notes or maintain contradictory versions of a rule.

When a design decision changes:

1. Read the complete relevant sections first.
2. Identify every existing rule/system affected by the change.
3. Resolve contradictions instead of appending a second conflicting rule.
4. Rewrite/remove obsolete text in `docs/GAME_DESIGN.md` and any affected focused specification.
5. Only then implement the change.
6. Keep code and documentation aligned in the same change whenever possible.

## Mandatory consistency review

For every new feature, explicitly check interactions with:

- physical continuity of vehicles/assets,
- the shared time/calendar model and selected start year,
- base-game versus Early Ages DLC scope,
- technology progression,
- economy and contracts,
- ownership/licensing/state rules,
- infrastructure capacity and geometry,
- maintenance and workforce,
- management/delegation,
- regional unlocking and inactive-world simulation,
- AI competitors,
- performance/simulation LOD,
- UI/player comprehensibility and explainability/no-hidden-mechanics requirements.

Do not implement a feature in isolation if it breaks an existing system.

## Core design constraints

### Physical continuity

Vehicles and rolling stock never teleport, magically reverse or disappear into abstract depots.

A remote asset may be simulated without rendering, but its logical position/state must remain continuous.

Train composition changes require actual physical operations.

### Scale/performance

Design for a very large world from the beginning.

Prefer:

- event-driven logic,
- cached calculations,
- coarse economic ticks,
- simulation LOD,
- batched cargo,
- aggregated population,
- aggregate inactive regions.

Avoid:

- per-frame economic simulation,
- persistent per-person simulation for entire cities,
- repeated full-network pathfinding,
- deep per-component vehicle simulation unless specifically approved.

### No grid world

Infrastructure is free-form/spline based. Buildings can rotate freely. Snapping is used only for real connections.

### Progressive automation

Early game can be hands-on. Later game must remain manageable through managers, dispatchers and technology without deleting the underlying physical rules.

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

UI may later surface this through hover/focus tooltips, pinned explanations and nested highlighted terms. Do not hardwire simulation logic to one specific tooltip implementation, but keep explanation data available so the UI can expose it.

### Historical plausibility and content scope

The base-game default/earliest start is **1900**, with selectable new-game years **1900, 1925, 1950 and 1975**.

The pre-1900 playable period, intended to start around **1820**, is reserved for the first planned DLC, **Early Ages**. Do not implement that earlier startup progression as a mandatory base-game requirement. Preserve shared systems and historically surviving older assets where relevant to the selected date.

Initialize the world's technology, economy, population, borders, infrastructure, competitors and vehicle catalogue for the selected start year. A small new player company does not reset the entire world to an earlier era. Do not force later starts to re-research already established historical inventions; actual equipment, facilities and staffing still need to be acquired.

### Unified calendar and time controls

Use the single simulation clock defined in `docs/GAME_DESIGN.md`, Section 3:

- 7 days per week;
- **14 days per month**, exactly two weeks;
- **12 months and 168 days per year**;
- 24 hours per day, 60 minutes per hour, 60 seconds per minute;
- **1 real second = 1 game minute at 1×**;
- speed controls **0.5×, 1×, 2×, 4×, 8×, 16×**;
- slowest running speed **0.5×**, maximum **16×**.

Do not reintroduce an independently accelerated historical calendar, the retired 100–150-hour campaign target or speeds above 16×. Year 2020 is a duration reference, not a mandatory game ending.

Timetables, slot windows, transfers, cargo ageing, crews, maintenance, production, construction, finances, research, contracts, cancellation and renewals must use the same game-time units. Never assume Gregorian month lengths or a 365-day financial year. Content dates outside days 1–14 require a documented conversion; do not invent that still-open mapping silently.

Validate calendar rollover, seasonal/cross-year patterns, billing and resource accounting, and mid-operation speed changes. Equivalent simulated elapsed time must not yield different economic accounting because a different speed was selected. Optimize rendering and update scheduling rather than skip movements, reservations or essential events to claim 16× performance. Benchmark the maximum setting on developed networks before claiming it is sustained.

### Scope discipline

Do not add major unapproved systems just because they are realistic. Tranzit aims for depth where it creates transport/business decisions, not simulation for its own sake.

## Architecture

Do not invent or lock in a technical architecture before checking the current Unity project and the design requirements.

When introducing a new subsystem:

- keep simulation state separable from rendering,
- keep data definitions extensible across eras/regions,
- use the shared calendar/time model instead of local conflicting clocks,
- make systems work with simulation LOD,
- avoid hardcoding specific cities, regions or vehicle models into core logic,
- prefer deterministic/state-driven simulation where practical,
- keep save/load compatibility in mind from the beginning.

## Development behavior

Before substantial work:

1. inspect the existing repository;
2. inspect the current design source of truth;
3. identify affected systems;
4. explain any required design compromise in the change/commit;
5. update documentation if the design changes.

Never silently change agreed gameplay behavior just to make implementation easier.
