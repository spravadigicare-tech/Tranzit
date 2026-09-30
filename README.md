# Tranzit

A long-form transport and business simulation built in Unity.

The player starts as a small regional carrier and can grow into a multinational transport group while cities, industries, infrastructure and technology evolve around them.

## First playable V1

The first implementation target is a genuinely playable offline Windows game, not a technology demonstration. Its approved scope is:

- one new-game preset: **1900**, with continuing calendar and technological progression;
- **rail and road**, for freight and passengers, including intercity and local buses;
- real geography covering the territory of present-day Czechia plus adjoining parts of Germany, Poland, Austria and Slovakia, with an authored historically plausible 1900 world;
- existing infrastructure, physical vehicles/cargo, real AI competitors and the applicable connected business/operations mechanics;
- cohesive stylized 3D model-world graphics, complete **Czech and English** UI and full save/load;
- one accounting unit named **money**;
- historical vehicle models without artificial end-year removal; finite market offers and changing maintenance support remain economic constraints.

The detailed boundary and cross-system rules are in [V1 Scope](docs/V1_SCOPE.md). Water, tram, trolleybus and metro operation and the later start presets remain wider base-game goals rather than requirements of this first release.

## Start here — OpenCode implementation

Read [OpenCode Start](docs/OPENCODE_START.md), then the linked specifications:

| Document | Purpose |
|---|---|
| [V1 Scope](docs/V1_SCOPE.md) | Approved release subset, time/distance rules, enduring vehicles and shipment splitting |
| [Implementation Brief](docs/V1_IMPLEMENTATION_BRIEF.md) | Architecture, subsystem coverage, M0–M8 work order, UI/art and delivery requirements |
| [UI/UX Design](docs/UI_UX_DESIGN.md) | Confirmed dark/movable-window direction and explicitly separate pending interface proposals; read decision status before implementing details |
| [Content Manifest](docs/V1_CONTENT_MANIFEST.md) | Initial authoring and balancing targets, world/assets/catalogues and benchmark fixtures |
| [Acceptance Tests](docs/V1_ACCEPTANCE_TESTS.md) | End-to-end player journeys, failure/regression cases and evidence-based release gates |
| [Implementation Status](docs/IMPLEMENTATION_STATUS.md) | Current implementation/test evidence and next executable task |
| [Data Pipeline](docs/DATA_PIPELINE.md) | Defined date-import convention and still-required data-production work |
| [Consistency Audit](docs/CONSISTENCY_AUDIT.md) | Review coverage, resolved contradictions and limits of documentation verification |

The handoff is documentation. It does **not** mean a Unity project, playable build, asset library or passing benchmark already exists. Check Implementation Status and the actual files for current progress.

## UI/UX design

[UI/UX Design](docs/UI_UX_DESIGN.md) owns the confirmed interface directions and records the remaining proposals: window behaviour, navigation, inspector contents, planning/construction workflows, notifications and open decisions.

**Partially confirmed:** the player approved a restrained contemporary dark interface and movable floating management/detail windows, replacing the proposed mandatory fixed right inspector. A fixed bottom bar was suggested tentatively and remains proposed, as do its contents, detailed resizing/pinning/minimization behaviour, terminology and other unresolved choices. Follow the decision statuses in that document; approval of these two directions does not approve every proposal or change the gameplay specifications above. Its confirmed-direction checks describe evidence still to collect, not an implemented or tested UI.

## Wider base game and planned DLC

The wider base-game design has selectable new-game starts in **1900, 1925, 1950 and 1975**. Only the 1900 preset is required for the first playable target; it is not yet implemented in the inspected documentation-only baseline. Later presets initialize an appropriate existing world while the player still starts with a small company.

The earlier playable period, intended to begin around **1820**, is reserved for the first planned DLC, **Early Ages**. Historic buildings, steam operations, horse-drawn transport and suitable older vehicles can still be part of the base game where appropriate. The DLC release schedule is not specified.

## Shared time model

- A week has 7 days; a month has **14 days**; a year has **12 months / 168 days**.
- At **1x**, **one real second equals one game minute**.
- Running speeds: **0.5x, 1x, 2x, 4x, 8x and 16x**, plus pause.
- One common clock governs vehicles, operations, economics, construction, contracts, seasons and historical progression.

At uninterrupted 16x, reaching the reference year 2020 takes approximately **504 h from 1900**, **399 h from 1925**, **294 h from 1950**, or **189 h from 1975**. The later starts are wider-design comparisons, not first-release presets. These are mathematical durations assuming the selected simulation rate is sustained, not measured performance or promised completion times. **2020 is not a mandatory ending.**

## Core design documents

- [Living Game Design](docs/GAME_DESIGN.md) — core gameplay source of truth; Section 3 governs the calendar, historical progression and wider start-year model.
- [Contract Cancellation](docs/CONTRACT_CANCELLATION.md) — capped early-exit fees, returned slots and non-renewal.
- [Agent Instructions](AGENTS.md) — mandatory development and consistency rules.

These documents are maintained as living specifications rather than a chronological idea log. V1 Scope narrows delivery scope while the broader Game Design remains intact. Focused rules must be read together, and genuine contradictions must be resolved rather than silently choosing the easier implementation.
