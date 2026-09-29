# AGENTS.md — Tranzit project rules

This repository contains **Tranzit**, a Unity transport/business simulation.

## Source of truth

Before implementing or proposing gameplay/system changes, read:

- `docs/GAME_DESIGN.md` — the core game design.
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
- time/technology progression,
- economy and contracts,
- ownership/licensing/state rules,
- infrastructure capacity and geometry,
- maintenance and workforce,
- management/delegation,
- regional unlocking and inactive-world simulation,
- AI competitors,
- performance/simulation LOD,
- UI/player comprehensibility.

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

### Historical plausibility

The game starts around 1820 and progresses over roughly two centuries. New systems must have sensible historical availability and evolution.

### Scope discipline

Do not add major unapproved systems just because they are realistic. Tranzit aims for depth where it creates transport/business decisions, not simulation for its own sake.

## Architecture

Do not invent or lock in a technical architecture before checking the current Unity project and the design requirements.

When introducing a new subsystem:

- keep simulation state separable from rendering,
- keep data definitions extensible across eras/regions,
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
