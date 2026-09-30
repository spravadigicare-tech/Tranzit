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
| [UI/UX Design](docs/UI_UX_DESIGN.md) | Confirmed window/bar/pause/link rules, compact vehicle overview and persistent card-based Line plans; remaining proposals and decision status |
| [Content Manifest](docs/V1_CONTENT_MANIFEST.md) | Initial authoring and balancing targets, world/assets/catalogues and benchmark fixtures |
| [Acceptance Tests](docs/V1_ACCEPTANCE_TESTS.md) | End-to-end player journeys, failure/regression cases and evidence-based release gates |
| [Implementation Status](docs/IMPLEMENTATION_STATUS.md) | Current implementation/test evidence and next executable task |
| [Data Pipeline](docs/DATA_PIPELINE.md) | Defined date-import convention and still-required data-production work |
| [Consistency Audit](docs/CONSISTENCY_AUDIT.md) | Review coverage, resolved contradictions and limits of documentation verification |

The handoff is documentation. It does **not** mean a Unity project, playable build, asset library or passing benchmark already exists. Check Implementation Status and the actual files for current progress.

## UI/UX design

[UI/UX Design](docs/UI_UX_DESIGN.md) owns the confirmed interface directions, contextual navigation, vehicle overview and card-based Line planning, and records remaining proposals for other inspector contents, shipment/construction workflows, notification layout and other open decisions.

**Confirmed:** a restrained contemporary dark interface, movable/resizable floating management/detail windows, multiple views, reusable ordinary selection details with content pinning, explicit opening in another window, minimize/restore, remembered/recoverable layout and a fixed bottom navigation/status/time bar. The top-level navigation is Build, Operations, Business, Assets, Company and World. The bottom bar replaces mandatory permanent left/top strips; contextual construction tools do not remove it. Ordinary object clicks reuse an unpinned detail rather than opening a new window every time. Pinning retains the object's identity while its data stays live.

**Connected windows and inline object links:** references to specific vehicles, stations, Lines, Trips, contracts and other inspectable objects are directly clickable in messages, detail windows, tables and planners. A vehicle mention opens that exact vehicle, not a fleet search or catalogue model. Reuse/focus existing windows, preserve pinned identities and drafts, and keep a path back to the source. Links use stable identities, work with keyboard and mouse in CZ/EN, and handle historical/unavailable targets without guessing a replacement. Navigation does not issue an order, jump the camera or resume a pause. Section 4.1 / UI-D09 owns the full rule; this does not make future deep nested tooltips mandatory.

**Vehicle detail:** the confirmed default is a compact operational overview with current activity/problem, location, applicable load/destination and next task, plus a small preview of the correct vehicle model. A static model image is sufficient; no live camera feed or animated 3D viewer is required. Actual vehicle information remains live and separate from the thumbnail. Detailed technical parameters, costs and history stay in secondary views; exact tab labels/dimensions remain design work. See Section 5.2 / UI-D10.

**Line planning:** use independently openable cards, not a guided wizard. The player can edit in any order, save an incomplete Line/Pattern design, close it and continue in a later session. Unlaunched plans remain visible separately from operating services. The overview shows actual dependencies and readiness, distinguishing filled inputs, forecasts, pending work and secured rights/resources. Saving a draft does not operate a service, reserve resources or create sales/Trips; separately accepted purchases and agreements still have real costs. Launch is an explicit, freshly validated commitment, never a consequence of filling every card or reaching an intended start date. Active Pattern edits still use future versions and existing impact checks. Section 6.1 / UI-D11 owns the full rule, including save/load, stale readiness and activation safeguards.

**Normal UI and pause:** ordinary windows, Line planning and construction previews do not automatically pause/resume the game or change its selected speed. During manual pause, camera/inspection and all planning tools remain available, while the shared simulation clock and time-driven operations stay stopped. Closing a planner never releases the manual pause; resuming never silently submits a draft or catches up the real time spent paused. See UI-D04 and Section 9.1 of the UI document for the confirmed rule and its command-safety boundaries.

**Critical incidents:** automatic pause is enabled by default for critical events requiring prompt player attention, including while a planner is open. Ordinary delays and routine problems handled within authorized policies do not interrupt play. Show the cause, impact and available response; preserve planning and require an explicit player action to resume. Closing or acknowledging a notice does not restart time. Deduplicate unchanged incidents across repeated alerts and save/load; a new critical incident or material escalation may pause again. Section 7.2 and the critical-event part of UI-D08 own this rule and its event-boundary/persistence safeguards.

**Still open or proposed:** application-focus and precise pause-menu behaviour in the remaining part of UI-D08, detailed event-override settings, exact styling/dimensions and secondary-control placement, information density outside the confirmed vehicle and Line-planning overviews, detailed navigation contents/object terminology and other unresolved workflows. Follow the decision statuses in the UI document; acceptance of specific rules does not approve every proposal or change unrelated gameplay. Its confirmed-direction checks describe evidence still to collect, not an implemented or tested UI.

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
