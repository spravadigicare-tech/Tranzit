# Tranzit — UI/UX design

> **Status: PARTIALLY CONFIRMED DESIGN — remaining details are proposals.** Updated on 2026-09-30 during the interface discussion with the player.
>
> **Confirmed:** UI-D01, a restrained contemporary dark interface over the model world; UI-D02, individual management/detail panels in movable floating windows rather than a mandatory fixed right inspector. These directions guide UI implementation within the existing release scope.
>
> **Still proposed:** a fixed bottom bar, suggested tentatively by the player, and its contents; detailed window behaviour, information density, terminology and the remaining workflows below. Do not treat confirmation of the visual/window direction as approval of every detail. A written design is not an implemented or tested UI.
>
> Existing requirements referenced in Section 1 remain binding. Keep this owning UI document and affected summaries/acceptance criteria consistent when a decision changes; retain explicit status for unresolved choices. Do not use presentation decisions to override gameplay or silently add release scope.

## 1. Existing requirements and document responsibility

Read these owners rather than treating the summaries below as replacement rules:

| Owner | Relevant existing requirement |
|---|---|
| [V1_SCOPE.md](V1_SCOPE.md), Sections 1 and 6 | Offline Windows, mouse/keyboard, complete Czech/English presentation, one accounting token `money`, full save/load; first-release modes and start preset remain unchanged |
| [GAME_DESIGN.md](GAME_DESIGN.md), Sections 1.1 and 3 | Explainable outcomes; shared simulation calendar and time controls; nested tooltips are a future interaction pattern, not a newly mandatory V1 feature |
| [GAME_DESIGN.md](GAME_DESIGN.md), Sections 11.0.1, 11.9 and 32 | Separate contracts, shipments, physical cargo portions, transport plans, Lines, Service Patterns and Trips; preserve their existing capacity and lifecycle rules |
| [GAME_DESIGN.md](GAME_DESIGN.md), Sections 13.2–13.2.1 and 32.2–32.3 | One Capacity Order workflow linked to Service Patterns; feasible slot windows, calendar and routing; no mandatory expert track-by-track timetable editing |
| [CONTRACT_CANCELLATION.md](CONTRACT_CANCELLATION.md) | Cancellation/release consequences, per-owner and total costs, prepaid settlement and distinction from non-renewal |
| [V1_IMPLEMENTATION_BRIEF.md](V1_IMPLEMENTATION_BRIEF.md), Sections 4 and 8–9 | Shared selection, validated commands, side-effect-free previews, required player workflows, onboarding, readable 1080p UI and adjustable scale |

This document owns the confirmed UI directions explicitly identified in Section 11 and develops the remaining presentation proposals. It does not replace the architecture brief, choose new packages, change simulation rules, add transport modes, or reduce V1 to the screens described here. The proposed sections are not automatically additional release gates.

## 2. Interface direction

**The world is the primary workspace. The interface helps the player understand a situation and act on it without repeatedly losing the map.**

Proposed organizing principles, while preserving the existing simulation requirements:

- Start with a concise summary; expose operational detail through deliberate expansion.
- Reuse consistent inspector components and one coherent selection model across the map, lists, alerts and planners. Shared components do not mean only one fixed window may exist.
- Connect each important problem to its cause, affected objects and available corrective action.
- Keep commercial commitments, planned operations and physical execution visibly distinct.
- Make routine operations delegable under the existing rules; do not add manual wagon, refuelling or ordinary-driver tasks merely to fill a screen.
- Treat planning and committing as different states. Closing a preview does not purchase, cancel, build or move anything.

### Confirmed visual direction — UI-D01

Use a restrained, contemporary **dark interface over the model-world graphics**. The player confirmed this direction. A light or heavily period-styled main interface is no longer an equally pending default choice.

Suggested treatment within that direction: charcoal/slate panels, warm light text, clear typography, modest corner rounding and sparse accents. Keep the map visually dominant. Avoid parchment textures, heavy ornamental frames, neon glow and oversized website-like cards. These details are visual recommendations, not locked colour/font/spacing tokens or a requirement for an additional theme.

Historical character can come from the world, vehicle illustrations, documents and news without rebuilding the entire navigation as the decades advance. A modern-looking UI must not grant modern communication, forecasting or management capabilities before their actual availability. Show only data the game permits, with its timestamp, precision and source where relevant.

Do not inherit Digicare or another product's branding without approval. Exact colours, fonts, opacity and spacing remain to be designed.

## 3. Main screen and floating windows

### 3.1 Confirmed window model — UI-D02

Individual management and object-detail panels use **movable floating windows**. The player can place them where needed over the map, rather than having to work in a permanently docked right-hand inspector. This supersedes the previous fixed-right-inspector recommendation.

Use a consistent window shell and content components. A window's screen position changes presentation only, never an asset's logical position or an operation's state. Do not introduce mandatory side docking as a substitute for free placement.

The overall composition below is a proposal around that confirmed window model, not a pixel-perfect wireframe:

| Element | Purpose | Status |
|---|---|---|
| Central world | Normal 3D map interaction and contextual overlays, with windows placed by the player | Map-first organizing proposal |
| Movable floating windows | Object inspectors, company/asset/business views and planning workspaces | Movable-window direction CONFIRMED; detailed controls proposed below |
| Fixed bottom bar | Main navigation, construction entry, important status and time controls | PROPOSED from the player's tentative suggestion |
| Contextual tools | Construction catalogue/options or the current planner's actions, in a floating tool window or temporary area above the bottom bar | PROPOSED; exact placement unresolved |
| Event access | Compact incident/decision indicator with a window for the grouped event list | PROPOSED; exact position unresolved |

The recommended composition no longer requires a permanent left navigation rail or a separate full-width top status strip. Their functions can be consolidated into the proposed bottom bar. This consolidation is not yet a confirmed requirement.

### 3.2 Proposed window behaviour — UI-D07

Free movement is confirmed; the following refinements still need approval or later interface validation:

| Behaviour | Recommendation |
|---|---|
| Moving | Drag the title bar; do not start a map pan or construction action through the window |
| Size | Resize useful management/detail windows within content-aware minimum sizes; allow large tables and planners to expand and restore their previous size/position |
| Multiple windows | Allow related views together, such as station capacity, a Line and a vehicle; do not restrict the system to the old one-inspector-plus-one-comparison proposal |
| Ordinary selection | Reuse an unpinned selection inspector for ordinary map clicks, reducing accidental window proliferation |
| Pinning | Pin the inspector's **object identity**, so selecting another object does not replace its contents. Pinning does not freeze live data, lock window position or imply always-on-top |
| Open separately | Provide an explicit open-in-new-window action. Normally focus an existing matching object/view window rather than creating duplicate editable copies |
| Minimize/close | Minimize without discarding a draft; expose minimized windows through an accessible window switcher, potentially from the bottom bar. Closing a meaningful dirty draft asks before discarding; closing never terminates a committed contract |
| Focus and input | Clicking a window brings it forward. Only the focused context receives keyboard input; scrolling, dragging or clicking inside UI cannot affect the world behind it |
| Optional snapping | Gentle edge/window snapping can help arrangement, but free movement remains possible and docking is never compulsory |
| Layout persistence | Remember useful window geometry as UI preferences, separately from simulation authority. Revalidate restored object references; restoring a layout never issues gameplay commands |
| Recoverability | Keep title bars and essential controls reachable after resolution/UI-scale changes; offer Reset window layout. With the proposed bar, keep normal floating windows within the usable area above it |

Ordinary-selection reuse and content pinning are recommendations, not a settled selection policy. Do not silently interpret the player's request for floating windows as approval of these specific behaviours.

Opening, moving, resizing or pinning windows does not itself authorize a new pause policy. Explicit pause and loading retain their existing rules; ordinary-panel, planning, focus and urgent-event auto-pause remain UI-D04.

### 3.3 Proposed fixed bottom bar — UI-D06

Use one stable bottom control area, not a second row of every possible game command. Suggested grouping:

| Area | Proposed contents |
|---|---|
| Left | Menu/company identity, cash and an optional compact financial-period result with its period stated |
| Centre | Build, Operations, Business, Assets, Company and World; access to search/map overlays without a permanent left rail |
| Right | Game date/time, pause and the existing speed controls; a compact incident/decision indicator |

Exact grouping and density remain open. The bar should open floating windows, catalogues or menus instead of becoming a large permanent dashboard. Clicking Build opens the construction catalogue; contextual placement options appear separately without replacing the primary navigation/time controls.

A minimized-window switcher is proposed, not a requirement to add a desktop-style button for every open window. Use grouping/overflow where necessary and validate with Czech/English text and larger UI scales. Keep essential time/pause controls and a way back to all main functions accessible. Do not lock exact heights, button counts or pixel widths before 1080p/scale validation.

Global search should locate known objects by name and type, such as a city, Line, vehicle or contract, without requiring the player to remember which module owns it. It must respect available information and active/macro-region boundaries; searching does not unlock a region.

## 4. Proposed navigation and information architecture

The five navigation groups below are candidates for the bottom bar, not a fixed left sidebar or an approved final menu structure.

| Main group | Contents |
|---|---|
| Operations / Provoz | Lines and Patterns, concrete departures/Trips, duties, capacity orders, operational incidents |
| Business / Obchod | Opportunities, tenders, bids, contracts, shipments and transport plans, partners/external transport |
| Assets / Majetek | Physical fleet, marketplace and deliveries, owned/rented facilities, maintenance, inventories/supplies, construction projects |
| Company / Firma | Offices/branches, aggregate staff and qualifications, directors/managers and permissions, finances/loans, licences/concessions and expansion |
| World / Svět | Cities and firms, competitors, public authorities, research/adoption and news |

Construction is a contextual world tool as well as an entry from Assets, not a second independent asset database.

The same object can be reached from several contexts without being duplicated in the simulation. A station selected from the map, a capacity warning or the asset list resolves to the same station identity and shared inspector components, even when presented in a separate window. Navigation grouping must not hide a required workflow from the implementation brief.

### Proposed player-facing vocabulary

| Domain identity | Czech label candidate | English label candidate |
|---|---|---|
| Line | Linka | Line |
| Service Pattern | Varianta linky | Service pattern |
| Trip | Jízda; contextual description such as dnešní odjezd | Trip |
| Shipment | Zásilka | Shipment |
| CargoLot | Část zásilky | Cargo portion |
| TransportPlan | Přepravní plán | Transport plan |
| CapacityOrder | Objednávka kapacity | Capacity order |

Labels are candidates, not a final localization glossary. Stable English data IDs do not change. A shipment is not a contract and a reserved cargo portion is not necessarily loaded cargo. Do not expose raw IDs as the normal player-facing explanation, but retain identity for support/debugging.

## 5. Proposed shared inspector contents

The shared inspector is a reusable window/content pattern, not a mandatory singleton at the right edge. Use a consistent structure with object-specific content rather than identical empty tabs everywhere:

1. **Header:** name, type, owner and current status; window movement and controls; locate/follow and content pinning where meaningful under the proposed selection policy.
2. **Summary:** a few relevant facts, the next event and the most important unresolved problem.
3. **Details:** relevant tabs/sections for operation, connections, costs, resources and history.
4. **Actions:** one clear primary action and contextual alternatives; destructive/commercial actions open an impact preview.

Example vehicle summary, using illustrative values only:

> Train 014 · Preparing · Brno freight terminal
>
> Next departure 08:20 · Planned capacity 60 t · Loaded 40 t
>
> Not ready: loading is incomplete. Expected completion 08:24.
>
> Open Trip · Show loading operation · Inspect allowed recovery

The final wording/status comes from simulation data. Do not invent a completion estimate or offer an impossible recovery. Fueling remains part of the existing between-Trip scheduling, not a new compulsory Refuel button on every vehicle.

Lists should preserve selection, scroll position and active edits during refresh. Sorting/filtering should be visible; automatic refresh should not move a row away from a pointer just before confirmation. Empty states should explain the next legitimate step rather than merely say "No data".

## 6. Proposed planning workflow

### 6.1 Create or change a Line

Use one guided workspace in a movable planning window, with a persistent summary and access to advanced parameters. Expansion for large tables is proposed; returning from an expanded view should restore the window/map context. Proposed stages:

| Stage | Player task | Feedback |
|---|---|---|
| Route | Choose valid endpoints/stops on the map or from search; add optional via/avoid constraints | Compatible route, access/coverage, distance and operational limits |
| Operation | Set variant, days, departures/interval or existing demand-driven conditions | Game-calendar schedule, estimated travel/dwell/turnaround and connections |
| Resources and rights | Set fleet/consist criteria, operating base and policies; inspect crew and infrastructure needs | Actual shortages, conflicts and linked acquisition/access workflows |
| Capacity order | Review automatically assembled section/station requirements from the Pattern | Owner quotes, windows, calendars, suggested feasible time shifts and applicable renewal/cancellation terms |
| Review and activate | Inspect economics, commitments, readiness and effective date | Clear ready/blocker state and explicit acceptance of costs/obligations |

The capacity stage is a view of the existing Capacity Order system, not a second booking mechanic. Preserve its Auto-renew control and meaningful per-owner breakdown. A recommendation or preview does not reserve capacity, purchase access or guarantee a price. A partial multi-owner purchase cannot display the entire route as protected.

Do not force the player to select every track, lane or permanent platform. Provide optional routing constraints while the dispatcher retains the existing detailed allocation responsibilities. Distinguish requested anchor time, accepted slot window, planned midpoint, occupancy and actual running time.

For an active Pattern, editing creates a future version and shows its effective time and affected bookings, cargo, contracts, slots and resources. Do not overwrite a running Trip. Suspension, permanent closure, renewal and early capacity release are separate actions with the existing impact checks.

### 6.2 Contract and shipment planning

Start from the opportunity/contract or shipment, not necessarily from building a new Line. Show a readable origin-to-destination chain with its own-service and external legs. Allow reuse of existing feasible services under the canonical allocation rules.

A split-shipment view should show, for each physical portion:

- quantity and actual location/custody;
- handling/readiness state;
- next reserved Trip and stop interval, distinct from the Trip currently carrying it;
- timing, connection risk, age/quality and contractual obligation where relevant.

Example presentation can illustrate the existing 100 t shipment split across multiple Trips, but every displayed total must reconcile to the actual ledger. A total such as "100 t allocated" must never imply "100 t already loaded". Changing a reservation cannot visually relocate cargo or restart its age.

The default experience should help plan at shipment/contract level. Detailed manual allocations remain governed by the existing rules; do not force individual-lot micromanagement or replace protected priority tiers with a new hidden score.

### 6.3 Construction

Proposed flow: select tool → place/edit free-form preview → inspect geometry and effects → review project → commit.

The review distinguishes one-time and recurring costs, land/access permissions, materials, contractors, expected duration and affected operation. Invalid geometry is highlighted with a cause and an available remedy. Keep snapping limited to valid physical connections, not an invented world grid.

An uncommitted ghost is not infrastructure and clearing it is not paid demolition. Committing creates a real construction project under the existing rules; completion is not instantaneous. Editing/removing existing infrastructure uses its own permission, closure and cost checks.

## 7. Proposed problem explanation and notifications

Use the same problem model in planners, inspectors, lists and the event area:

**What happened → why → operational/commercial impact → available action.**

Example, illustrative rather than a fixed balancing rule:

> Departure cannot be activated: the planned train is longer than every accessible platform at this stop.
>
> Inspect platform limits · Change consist · Review another compatible stop

Separate **hard blockers**, **risks/warnings**, **information** and **completed events**. An actionable warning is not silently promoted to a blocker, and a hard physical/legal constraint cannot be bypassed by dismissing a warning.

Group repeated messages about the same incident, show its affected services and allow drill-down. Avoid one pop-up per delayed train when one closure is the cause. Keep information and routine successful automatic actions in history; surface decisions needing player authority. A manager action should show its cause and the policy/budget that authorized it.

Colours supplement icons and text, never carry status alone. Distinguish unacknowledged, being handled, awaiting a decision and resolved where these states exist. Whether selected urgent events automatically pause the game remains an explicit open choice, not an assumed mechanic.

V1 explanations must be accessible through focus/click as well as hover. A simple details view or pinned explanation can work without making deep nested tooltips a new V1 requirement.

## 8. Proposed map overlays

Offer a small set of purpose-based overlays instead of displaying every layer at once:

| Overlay | Primary question |
|---|---|
| Network and services | Where do our services go, and how do they connect? |
| Ownership and rights | Who owns this asset, and what can our company actually use? |
| Capacity and congestion | Which sections/facilities constrain the selected operation? |
| Demand and business | What passenger/cargo opportunity is known here? |
| Facility coverage | Which operating, maintenance, supply or handling facilities can support these assets? |
| Projects and disruptions | What is being built, restricted or repaired, and what does it affect? |

Each overlay needs a legend, relevant filters and a visible scope. Overlay values must distinguish observed facts, projections and contractual capacity; lack of data is not zero demand. Vehicle selection should show its actual movement and relevant planned route without changing either. Inactive regions remain the existing macro layer, not secretly fully simulated because an overlay is open.

## 9. Input, scale, time and state safety

Carry forward the implementation brief's existing input/save defaults rather than choosing conflicting bindings here. Any new shortcuts should be remappable and respect text-field focus. Proposed Escape behaviour: leave the current transient action first; warn before discarding a meaningful unsaved plan; only then close/navigate out of the focused window or open the pause menu. Escape does not terminate a contract or indiscriminately close every window.

The exact pause policy for ordinary panels, construction, planning, application focus and urgent incidents is unresolved. No simulation progresses during explicit pause or incomplete loading under the existing rules. Display actual pause/speed clearly; never silently change the selected speed because a management panel opened. Continue to use the existing game clock/calendar, including its supported speed choices and 14-day months; do not use a Gregorian date picker for game dates.

Every costly or irreversible command must be revalidated against current simulation state. If a live preview becomes stale, explain changed prices, availability or affected obligations before accepting a revised commitment. Repeated clicks, including submissions from different windows, cannot duplicate an order/payment. Closing a panel cannot undo a committed transaction. Multiple views use the same authoritative state/command validation, not independent ledgers.

Preserve useful navigation context when opening a corrective workflow and returning to a planner. UI preferences such as scale and proposed window geometry are distinct from save-game authority. Restoring an inspector, filter or uncommitted draft cannot execute a purchase, advance construction or regenerate physical cargo. If an inspected object is no longer available, show its valid history or an explicit unavailable state instead of broken controls. Content pinning never makes a stale object reference authoritative.

Support complete Czech/English text, number formatting, readable contrast, keyboard focus, non-colour status cues and text expansion. Test the established 1080p baseline and enlarged UI on higher-resolution screens; exact panel dimensions and scale steps remain design work. Never truncate a material price, warning, unit or action consequence without a way to read it. Proposed minimum sizes, screen-bound constraints and layout reset must be evaluated together rather than trapping controls off-screen when the viewport becomes smaller.

## 10. Design-validation scenarios

### Confirmed-direction checks

These checks describe evidence for the two confirmed directions, not completed tests. They do not approve the proposed refinements or replace [V1_ACCEPTANCE_TESTS.md](V1_ACCEPTANCE_TESTS.md).

| ID | Confirmed direction | Evidence to collect when implemented |
|---|---|---|
| UI-A01 | UI-D01, contemporary dark interface | Actual in-game management/detail windows use the agreed dark direction over the model world; no substituted light/parchment primary theme or claim that a generated mockup is in-engine evidence |
| UI-A02 | UI-D02, movable floating windows | Open representative management and object-detail panels and move them to another usable part of the screen; no mandatory fixed-right inspector; moving a window changes no gameplay position/state |

### Remaining proposed interaction scenarios

These are scenarios for evaluating the remaining proposal, not passing tests or additional approved release gates. Formal gameplay acceptance remains in V1_ACCEPTANCE_TESTS.md.

| Scenario | What the proposed UI should demonstrate |
|---|---|
| Found a company | Find the existing 1900/region/loan, office, staff and licence steps without a hidden setup screen or free assets; remain mode-neutral |
| Inspect a vehicle | From map or list, identify location, current task, next departure and actual cause of a delay |
| Arrange related windows | Compare related views, move/resize them and use proposed content pinning without an unrelated selection replacing the pinned identity |
| Recover the workspace | Minimize/restore, change resolution/UI scale and reset the layout without losing access to title bars, controls or dirty drafts |
| Use the proposed bottom bar | Reach navigation/construction and time controls without a mandatory permanent left rail or a window covering the bar |
| Plan a service | Choose endpoints and operation, inspect dependencies and capacity quotes, then understand what activation commits |
| Track split cargo | Explain where all portions are, what is ready/loaded/reserved and which connection is at risk |
| Change a running service | Understand version/effective date and affected commitments without rewriting departed Trips |
| Release capacity | Distinguish non-renewal from early cancellation and see total/per-owner settlement plus dependent services |
| Build infrastructure | Distinguish ghost preview, accepted project and completed usable asset; clicking a floating tool window does not place infrastructure behind it |
| Manage disruption | Navigate from one grouped incident to its cause and a valid authorized response |
| Use CZ/EN and enlarged UI | Complete the same workflow without clipped material information or hover-only actions |
| Save/load and live refresh | Preserve game authority; restored UI state, repeated clicks or parallel views cannot create duplicate commitments |

No Unity UI has been implemented or visually tested as part of this document. Structural documentation checks, when run, do not validate these interaction scenarios.

## 11. Decision status

| ID | Decision | Current direction/recommendation | Status |
|---|---|---|---|
| UI-D01 | Overall visual character | Restrained contemporary dark interface over the model world, with limited historical flavour; exact styling tokens remain open | CONFIRMED on 2026-09-30 |
| UI-D02 | Workspace/window model | Individual management/detail panels are movable floating windows; not a mandatory fixed right inspector | CONFIRMED on 2026-09-30 |
| UI-D03 | Information density | Concise summary first, richer tables/timelines and details on demand | PROPOSED |
| UI-D04 | Pause behaviour | Decide ordinary-panel/planner/construction/focus/urgent-event behaviour explicitly; preserve existing explicit pause/load rules | OPEN |
| UI-D05 | Navigation and Czech terminology | Five proposed navigation groups and plain-language labels from Section 4 | PROPOSED |
| UI-D06 | Fixed bottom bar | Stable bottom navigation/control area instead of mandatory left/top strips; exact contents and grouping unresolved | PROPOSED from the player's tentative suggestion on 2026-09-30 |
| UI-D07 | Detailed window interaction | Resizing, multiple views, selection reuse/content pinning, minimize/restore, optional snapping and layout recovery as described in Section 3.2 | PROPOSED |

Continue by resolving the bottom bar and window-selection behaviour, then refine one concrete end-to-end flow before styling all panels. Approval of one decision does not silently approve the other rows or every detail in this document.
