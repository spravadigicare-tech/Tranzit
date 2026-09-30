# Tranzit — UI/UX design

> **Status: PARTIALLY CONFIRMED DESIGN — remaining details are proposals.** Updated on 2026-09-30 during the interface discussion with the player.
>
> **Confirmed:** UI-D01, a restrained contemporary dark interface over the model world; UI-D02, movable floating management/detail windows; UI-D06, a fixed bottom navigation/status/time bar; UI-D07, resizing, multiple windows, reusable selection details with content pinning, minimize/restore and remembered/recoverable layout. The top-level navigation groups in UI-D05 are confirmed; detailed taxonomy and the object glossary remain proposals. These directions guide UI implementation within the existing release scope.
>
> **Still open or proposed:** pause behaviour, exact visual tokens and dimensions, secondary-control placement, information density, detailed terminology and the remaining workflows below. The player's acceptance of the bottom-bar/window proposal does not approve all earlier proposals. A written design is not an implemented or tested UI.
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

The accepted composition is a map workspace with floating windows and a fixed bottom bar, not a pixel-perfect wireframe:

| Element | Purpose | Status |
|---|---|---|
| Central world | Normal 3D map interaction and contextual overlays, with windows placed by the player | Main workspace; detailed overlays remain proposed |
| Movable floating windows | Object inspectors, company/asset/business views and planning workspaces | CONFIRMED under UI-D02 and UI-D07 |
| Fixed bottom bar | Main navigation, construction entry, important status and time controls | CONFIRMED under UI-D06 |
| Contextual tools | Construction catalogue/options or the current planner's actions, separate from the persistent bar | Separation confirmed; floating tool window versus temporary area above the bar remains unresolved |
| Event access | Compact incident/decision indicator in the bar, opening the event view | Bar access confirmed; detailed event-window behaviour remains proposed |

Use the bottom bar instead of a mandatory permanent left navigation rail or separate full-width top status strip. Contextual windows may contain their own navigation/status without duplicating the entire global control system. Keep the bottom bar reachable while ordinary windows are open.

### 3.2 Confirmed window behaviour — UI-D07

The player accepted the proposed window controls and the reusable-inspector/content-pinning approach. Exact dimensions, secondary controls and implementation details still require interface validation.

| Behaviour | Accepted rule |
|---|---|
| Moving | Drag the title bar; do not start a map pan or construction action through the window |
| Size | Resize useful management/detail windows within content-aware minimum sizes so vehicle details can remain compact and management tables can be larger |
| Multiple windows | Allow related views together, such as station capacity, a Line and a vehicle; do not restrict the system to the old one-inspector-plus-one-comparison proposal |
| Ordinary selection | Reuse an unpinned selection inspector for ordinary map clicks, reducing accidental window proliferation |
| Pinning | Pin the inspector's **object identity**, so selecting another object does not replace its contents. Pinning does not freeze live data, lock window position or imply always-on-top |
| Open separately | Provide an explicit open-in-new-window action. Normally focus an existing matching object/view window rather than creating duplicate editable copies |
| Minimize/close | Minimize without discarding a draft; expose minimized windows through an accessible window switcher. Closing a meaningful dirty draft asks before discarding; closing never terminates a committed contract |
| Focus and input | Clicking a window brings it forward. Only the focused context receives keyboard input; scrolling, dragging or clicking inside UI cannot affect the world behind it |
| Optional snapping | Gentle edge/window snapping may assist arrangement, but free movement remains possible and docking is never compulsory. Adding snap assistance is optional, not a separate release gate |
| Layout persistence | Remember useful window geometry as UI preferences, separately from simulation authority. Revalidate restored object references; restoring a layout never issues gameplay commands |
| Recoverability | Keep title bars and essential controls reachable after resolution/UI-scale changes; offer Reset window layout. Keep normal floating windows within the usable area above the bottom bar |

Normal selection example: select vehicle A, then vehicle B; the same unpinned detail window now shows B. Pin B, then select station C; B remains visible and live, while C uses another unpinned detail window. Further ordinary selections reuse that unpinned window. A pinned detail is not replaced merely because the map selection changes. Retain meaningful dirty edits or ask before discarding them; selection reuse is not permission to lose a draft.

A maximize/expand-and-restore control for large tables/planners remains an optional refinement. Its exact behaviour and the minimized-window switcher's placement are not locked by this decision. Avoid introducing an obligatory desktop-style task button for every open window.

Opening, moving, resizing or pinning windows does not itself authorize a new pause policy. Explicit pause and loading retain their existing rules; ordinary-panel, planning, focus and urgent-event auto-pause remain UI-D04.

### 3.3 Confirmed fixed bottom bar — UI-D06

Use one compact, stable bottom control area, not a second row of every possible game command. The player accepted the following functional grouping:

| Area | Contents |
|---|---|
| Left | Menu and cash; company identity and a compact financial-period result may supplement these, with the result's period stated |
| Centre | Build / Stavět, Operations / Provoz, Business / Obchod, Assets / Majetek, Company / Firma and World / Svět |
| Right | Game date/time, pause and the existing speed controls; a compact incident/decision indicator |

The bar opens floating windows, catalogues or menus instead of becoming a large permanent dashboard. Clicking Build opens the construction catalogue; contextual placement options appear separately without replacing the primary navigation/time controls. The exact choice of a floating construction-tool window versus a temporary area above the bar remains open.

Provide access to minimized windows without requiring a button for every window. Search/map-overlay placement and secondary shortcuts remain proposals. Use grouping/overflow where necessary and validate with Czech/English text and larger UI scales. Keep essential time/pause controls and a way back to all main functions accessible. Exact heights, spacing, secondary-button counts and pixel widths remain implementation/visual-design work, subject to 1080p/scale validation.

Global search should locate known objects by name and type, such as a city, Line, vehicle or contract, without requiring the player to remember which module owns it. It must respect available information and active/macro-region boundaries; searching does not unlock a region.

## 4. Navigation and proposed detailed information architecture

The five top-level navigation groups below are accepted for the bottom bar, alongside Build. Their detailed contents and object terminology remain proposals, not an approved final taxonomy for every screen.

| Main group | Proposed contents |
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

1. **Header:** name, type, owner and current status; window movement and controls; locate/follow and content pinning where meaningful under the confirmed selection policy.
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

Use one guided workspace in a movable planning window, with a persistent summary and access to advanced parameters. A separate maximize/expand control remains proposed; returning from an expanded view should restore the window/map context. Proposed stages:

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

Preserve useful navigation context when opening a corrective workflow and returning to a planner. UI preferences such as scale and window geometry are distinct from save-game authority. Restoring an inspector, filter or uncommitted draft cannot execute a purchase, advance construction or regenerate physical cargo. If an inspected object is no longer available, show its valid history or an explicit unavailable state instead of broken controls. Content pinning never makes a stale object reference authoritative.

Support complete Czech/English text, number formatting, readable contrast, keyboard focus, non-colour status cues and text expansion. Test the established 1080p baseline and enlarged UI on higher-resolution screens; exact panel dimensions and scale steps remain design work. Never truncate a material price, warning, unit or action consequence without a way to read it. Minimum sizes, screen-bound constraints and layout reset must be evaluated together rather than trapping controls off-screen when the viewport becomes smaller.

## 10. Design-validation scenarios

### Confirmed-direction checks

These checks describe required evidence for the confirmed directions, not completed tests. They do not approve the remaining proposals or replace [V1_ACCEPTANCE_TESTS.md](V1_ACCEPTANCE_TESTS.md).

| ID | Confirmed direction | Evidence to collect when implemented |
|---|---|---|
| UI-A01 | UI-D01, contemporary dark interface | Actual in-game management/detail windows use the agreed dark direction over the model world; no substituted light/parchment primary theme or claim that a generated mockup is in-engine evidence |
| UI-A02 | UI-D02, movable floating windows | Open representative management and object-detail panels and move them to another usable part of the screen; no mandatory fixed-right inspector; moving a window changes no gameplay position/state |
| UI-A03 | UI-D06 and top-level UI-D05, fixed bottom bar | Reach the accepted navigation groups, construction, cash, date/time, pause, speed and incident access from the bottom bar; opening windows or construction tools does not remove those controls; verify CZ/EN and enlarged UI without material clipping |
| UI-A04 | UI-D07, selection reuse and content pinning | Select A then B and verify reuse of the unpinned detail; pin B and select C, verifying B stays live and unchanged in identity while C uses another reusable inspector; open a separate detail explicitly without duplicate simulation objects or silently discarded dirty edits |
| UI-A05 | UI-D07, workspace controls and recovery | Move/resize multiple related views, minimize and restore a draft, change resolution/UI scale and reset the layout; titles, essential controls and the bar remain reachable; restoring geometry changes no game state; do not require optional snap/maximize controls as release gates |
| UI-A06 | UI-D07 and existing command safety, multiple-view input | Clicking, scrolling or dragging inside a window does not select/place/pan the world beneath it; repeated submissions through different windows cannot double-book or double-charge; stale/deleted object references cannot issue valid new commitments |

### Remaining proposed interaction scenarios

These are scenarios for evaluating the remaining proposal, not passing tests or additional approved release gates. Formal gameplay acceptance remains in V1_ACCEPTANCE_TESTS.md.

| Scenario | What the proposed UI should demonstrate |
|---|---|
| Found a company | Find the existing 1900/region/loan, office, staff and licence steps without a hidden setup screen or free assets; remain mode-neutral |
| Inspect a vehicle | From map or list, identify location, current task, next departure and actual cause of a delay |
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
| UI-D05 | Navigation and Czech terminology | Top-level Provoz, Obchod, Majetek, Firma and Svět alongside Stavět are accepted; detailed contents and object glossary in Section 4 remain proposed | PARTIALLY CONFIRMED on 2026-09-30 |
| UI-D06 | Fixed bottom bar | Stable bottom navigation/status/time control area with the functional grouping in Section 3.3, instead of mandatory left/top strips; exact visual dimensions and secondary controls remain open | CONFIRMED on 2026-09-30 |
| UI-D07 | Detailed window interaction | Resizing, multiple views, reusable unpinned detail, content pinning, explicit new-window action, minimize/restore and remembered/recoverable layout under Section 3.2; snapping is optional and never compulsory docking | CONFIRMED on 2026-09-30 |

The player's acceptance of the bottom-bar/window proposal includes updating one ordinary detail window until it is pinned, rather than opening a new window for every ordinary object click. Do not reopen that resolved choice. Next resolve UI-D04, then refine one concrete end-to-end flow before styling all panels. Approval of these decisions does not silently approve the remaining rows or every detail in this document.
