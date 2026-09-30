# Tranzit — UI/UX design

> **Status: PARTIALLY CONFIRMED DESIGN — remaining details are proposals.** Updated on 2026-09-30 during the interface discussion with the player.
>
> **Confirmed:** UI-D01, a restrained contemporary dark interface over the model world; UI-D02, movable floating management/detail windows; UI-D04, ordinary windows and planning do not automatically pause/resume the game, and planning remains available during manual pause; UI-D06, a fixed bottom navigation/status/time bar; UI-D07, resizing, multiple windows, reusable selection details with content pinning, minimize/restore and remembered/recoverable layout; the critical-event part of UI-D08, automatic pause enabled by default for critical incidents; UI-D09, contextual links between windows and directly from mentions of specific objects; UI-D10, an operations-first vehicle overview with a small model preview that may be static; UI-D11, freely editable Line-planning cards, persistent unlaunched plans and an explicit readiness/activation decision; UI-D12, the same Line window/cards after launch, with a live operational overview, scoped variants/Trips and clearly separated future changes. The top-level navigation groups in UI-D05 are confirmed; detailed taxonomy and the object glossary remain proposals. These directions guide UI implementation within the existing release scope.
>
> **Still open or proposed:** application-focus and precise pause-menu behaviour under the remaining part of UI-D08, exact visual tokens and dimensions, secondary-control placement, information density outside the confirmed vehicle and Line overviews, detailed terminology and the remaining workflows below. Approval of specific decisions does not approve unrelated pause triggers or every earlier proposal. A written design is not an implemented or tested UI.
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

Proposed organizing principles, while preserving the existing simulation requirements and the specific confirmed rules below:

- Start with a concise summary; expose operational detail through deliberate expansion. The operations-first vehicle overview is confirmed in Section 5.2, the Line-planning card overview in Section 6.1 and the active Line overview in Section 6.4; the general density of other screens remains proposed.
- Reuse consistent inspector components and one coherent selection model across the map, lists, alerts and planners. Shared components do not mean only one fixed window may exist.
- Connect each important problem to its cause, affected objects and available corrective action. Direct contextual object links are confirmed in Section 4.1.
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
| Event access | Compact incident/decision indicator in the bar, opening the event view | Bar access, contextual object links and critical-event pause confirmed; detailed event-window layout remains proposed |

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

Contextual object links use the same window/selection system under Section 4.1, not a second set of unrelated pop-ups. Preserve pinned identities and meaningful source context when following a link.

A maximize/expand-and-restore control for large tables/planners remains an optional refinement. Its exact behaviour and the minimized-window switcher's placement are not locked by this decision. Avoid introducing an obligatory desktop-style task button for every open window.

Opening, moving, resizing, pinning, minimizing or closing ordinary windows does not automatically pause, resume or change simulation speed. Apply the confirmed normal-UI/manual-pause rules in Section 9.1. Critical incidents independently trigger the pause in Section 7.2, including while a planner is open; application-focus and precise pause-menu behaviour remain open under the remaining part of UI-D08.

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

The five top-level navigation groups below are accepted for the bottom bar, alongside Build. Their detailed contents and object terminology remain proposals, not an approved final taxonomy for every screen. Contextual links between those screens are confirmed separately in Section 4.1.

| Main group | Proposed contents |
|---|---|
| Operations / Provoz | Lines and Patterns, concrete departures/Trips, duties, capacity orders, operational incidents |
| Business / Obchod | Opportunities, tenders, bids, contracts, shipments and transport plans, partners/external transport |
| Assets / Majetek | Physical fleet, marketplace and deliveries, owned/rented facilities, maintenance, inventories/supplies, construction projects |
| Company / Firma | Offices/branches, aggregate staff and qualifications, directors/managers and permissions, finances/loans, licences/concessions and expansion |
| World / Svět | Cities and firms, competitors, public authorities, research/adoption and news |

Construction is a contextual world tool as well as an entry from Assets, not a second independent asset database.

The same object can be reached from several contexts without being duplicated in the simulation. A station selected from the map, a capacity warning or the asset list resolves to the same station identity and shared inspector components, even when presented in a separate window. Navigation grouping must not hide a required workflow from the implementation brief.

### 4.1 Confirmed contextual object links and connected windows — UI-D09

**Windows and their contents must be interconnected. When a message or another UI view mentions a specific game object, the player can click that object's word/name directly to open its detail.** The player explicitly requested this on 2026-09-30. A mention of a particular vehicle opens that vehicle, not the general fleet list or its catalogue model.

Apply this consistently to notifications, incident explanations, detail windows, relationship fields, tables, planners and history entries wherever they reference identifiable inspectable objects. Relevant targets include vehicles, Lines, Service Patterns, Trips, stations/depots, companies, contracts, shipments and construction projects. This is navigation between existing systems, not a new simulation entity or permission to add otherwise excluded features.

Illustrative message; the bold object names represent inline links in the implemented UI:

> **Vehicle 014** is waiting for repairs at **Brno depot**. Its next **Trip at 08:20** is at risk.

Each linked phrase opens its exact referenced object. From the vehicle's detail, its Line, current/next Trip and assigned depot can likewise be opened directly when those relationships exist. The player should not need to close the message, navigate to Assets and search for the vehicle by name.

Interaction and identity rules:

- Make links recognizable with a consistent affordance, hover feedback and visible keyboard focus; do not rely on colour alone. The text link itself is actionable, not only a separate generic Details button. Support mouse click and keyboard activation in Czech and English, including inflected names and wrapped text.
- Carry a typed stable object reference with the UI text/relationship, optionally identifying a relevant detail section. Resolve by identity, not by searching rendered/localized words, vehicle model, row number or current map selection. Two identically named vehicles must remain distinguishable; renaming an object must not retarget an older message to another one.
- Use the shared window manager from Section 3.2. Focus/restore an already open matching detail first; otherwise use an available unpinned inspector or open one when needed. Never replace a pinned object's identity. Explicit Open in new window remains available under the same rules; ordinary navigation must not produce duplicate editable copies unnecessarily.
- Preserve the source message/list/planner and meaningful edits. When reusing the source detail window to show a related object, provide a way back to the prior context; when opening/focusing another window, retain the source window. Do not silently discard drafts, filters or scroll position during a chain of links.
- Opening a detail is distinct from the explicit Locate/Follow action. A normal text link should not unexpectedly move the world camera, teleport an asset, issue an order, acknowledge/resolve an incident or change speed/pause. It works during manual and critical-event pause without resuming time.
- Live detail shows the object's current authoritative state; a historical message retains its event-time meaning. For example, an old delay message may open a vehicle that has since arrived. Make that distinction readable rather than rewriting the old incident or presenting its snapshot as live state.
- If the original object is no longer available, open its retained history/read-only record where available, or show an explicit unavailable-state explanation. Do not crash, invent a replacement or redirect silently to a different vehicle of the same model/name. Sold assets retain only the inspection/control rights the player actually has; a link grants no new ownership or access.
- Link meaningful specific references, not every generic word. A general concept such as capacity may have contextual help, but must not pretend to target a unique asset. Multiple possible objects require a clearly labelled related-object list rather than guessing. Keep actual business/operational actions separate from navigation links.

Implementation guidance: represent links as structured rich-text spans/reference tokens and reusable object-reference controls using the existing stable IDs and presentation models. Treat message text and player-entered names as text, not executable markup or arbitrary commands. Revalidate the target when activated and restored from a save; do not depend on the target's rendered GameObject being loaded. Navigating to a remote object does not activate an inactive region or bypass information availability.

These direct object links are part of V1 interaction. They do **not** make the future deep nested-glossary/tooltip pattern in GAME_DESIGN Section 1.1 mandatory now. Entity navigation and optional concept explanations are different interactions.

### 4.2 Proposed player-facing vocabulary

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

## 5. Inspector contents

### 5.1 Proposed shared structure

The shared inspector is a reusable window/content pattern, not a mandatory singleton at the right edge. Use a consistent structure with object-specific content rather than identical empty tabs everywhere. This general template remains proposed; contextual links in Section 4.1, the vehicle-specific view in Section 5.2 and the Line-specific views in Sections 6.1 and 6.4 are confirmed.

1. **Header:** name, type, owner and current status; window movement and controls; locate/follow and content pinning where meaningful under the confirmed selection policy.
2. **Summary:** a few relevant facts, the next event and the most important unresolved problem.
3. **Details:** relevant tabs/sections for operation, connections, costs, resources and history.
4. **Actions:** one clear primary action and contextual alternatives; destructive/commercial actions open an impact preview.

Lists should preserve selection, scroll position and active edits during refresh. Sorting/filtering should be visible; automatic refresh should not move a row away from a pointer just before confirmation. Empty states should explain the next legitimate step rather than merely say "No data".

### 5.2 Confirmed vehicle overview and compact model preview — UI-D10

**The default vehicle detail is an operational overview, with a small preview of the vehicle model. A static model image is sufficient; a large illustration or live camera feed is not required.** The player confirmed the smaller, operations-first view on 2026-09-30 and explicitly allowed a static model preview.

Prioritize the vehicle's name/model, current activity and any material problem, then its actual location, current load/passenger occupancy as applicable, destination/current service and next planned task/departure. Keep this useful summary visible without first opening a long technical-parameter or accounting list. Display absent assignments and unavailable estimates honestly; a vehicle in storage has no invented next Trip.

The model thumbnail supports recognition rather than dominating the window. A cached/prerendered still of the correct model is an acceptable implementation. Do not require an animated, rotatable 3D viewer, dedicated live world camera or a separately running miniature vehicle simulation. The static image does not freeze the actual vehicle's status, location or load information. Identify it as a model preview rather than evidence of the vehicle's current physical location, condition or assembled consist.

Illustrative summary only; actual values must come from simulation data, and named objects/related tasks link under Section 4.1:

> Vehicle 014 · Preparing · Brno freight terminal
>
> Small static model preview
>
> Next departure 08:20 · Planned capacity 60 t · Loaded 40 t
>
> Not ready: loading is incomplete. Expected completion 08:24.
>
> Open Trip · Show loading operation · Inspect allowed recovery

The selected detail still refers to one concrete physical asset, not all assets sharing its model. In a train context, distinguish the selected locomotive/wagon from its current consist and Trip; a locomotive thumbnail must not imply a fixed train composition or define cargo capacity.

Follow related consist/service details through their existing identities.

Keep technical parameters, detailed costs and history available through secondary tabs/sections. The suggested labels remain Overview / Přehled, Operation / Provoz, Technical condition / Technický stav, Costs / Náklady and History / Historie; their exact wording and grouping are not locked by approval of the summary/thumbnail. Exact preview dimensions and placement remain visual-design work, subject to readable 1080p and enlarged CZ/EN UI. A missing preview must not block inspection or show another model as though it were correct.

Do not invent completion estimates or offer impossible recovery. Fueling remains part of existing between-Trip scheduling, not a new compulsory Refuel button on every vehicle. The static preview changes presentation cost only; it never replaces the physical vehicles or their required visible world operations.

## 6. Planning and Line-management workflows

### 6.1 Confirmed card-based Line planning, saved drafts and readiness — UI-D11

**A Line is planned through independently openable cards, not a guided sequence. The player can work in any order, leave the Line as an unlaunched future plan, return later and explicitly launch it when ready.** Confirmed on 2026-09-30. This replaces the earlier wizard/stage proposal; do not require Next/Back steps or a completed previous card to open another one.

#### Card overview and editing

New Line opens a movable planning window with a compact overview of cards. Each card shows its subject, a brief configuration summary, readiness status and the main missing dependency or problem. Clicking it opens that area's editable detail; returning to the overview preserves other work. Use the same freely navigable card model for later edits, not a second mandatory wizard. Section 6.4 defines the confirmed active-service overview added to this same window after launch.

Use these functional card groups consistently across planning and active-service views; exact localized labels and visual dimensions remain subject to layout validation:

| Card | Editable content and visible dependencies |
|---|---|
| Route and stops / Trasa a zastávky | Ordered endpoints/stops, optional via/avoid constraints, compatible route and access; distinguish intended/planned stops from usable physical endpoints |
| Operating plan / Provozní režim | Pattern, service days, exact/interval/demand-driven departures, dwell/turnaround and intended start; use the shared game calendar |
| Vehicles / Vozidla | Vehicle/consist requirements, assignment criteria or pinned assets, expected fleet demand, real availability/delivery and conflicting commitments |
| Staff and facilities / Personál a zázemí | Qualified aggregate crews, operating base, parking, maintenance, energy/service and handling coverage as applicable |
| Rights and capacity / Oprávnění a kapacita | Licences, local presence, relevant municipal permission, access and shared Capacity Orders; distinguish a request/quote from an accepted agreement |
| Economics and obligations / Ekonomika a závazky | Applicable tariffs, estimated revenue/costs with units and assumptions, real commitments, outstanding dependencies and activation consequences |

A missing route may prevent a fleet/travel-time calculation, but it does not prevent opening the Vehicles card and saving intended requirements. Show "Cannot evaluate until route is specified" rather than forcing the player back to the first card or inventing a result. Changing one card retains the others' values, marks affected results stale and explains conflicts instead of silently clearing the plan. Card details use the confirmed object links and window/pinning rules. Cards must be compact enough for a useful overview, not oversized decorative website tiles.

#### A persistent plan, not an active service

The incomplete record is a saved Line/Service Pattern **design draft**, separate from activated commercial operation. The operational prerequisites in GAME_DESIGN Section 32 remain required for creating/running the commercial service; their absence does not prevent storing its incomplete design. This adds a durable planning workspace, not an alternative operating hierarchy or an exemption from those prerequisites.

- A draft may contain only part of the route, proposed vehicle requirements or another partial configuration. Missing access, vehicles, staff, facilities or unresolved validation does not block saving the draft. Keep invalid/incomplete editor inputs out of authoritative executable schedules while retaining useful unfinished work.
- Provide Save plan separately from Launch/Activate, with clear saved/unsaved feedback. Persist the draft in the campaign save, with a stable identity and editable contents; it survives closing its window, saving/loading the game and returning in a later session. It must not exist only inside a currently open window. Preserve unsaved edits or ask before discarding them under the shared window rules.
- Show unlaunched plans in the Line management view, clearly distinguishable/filterable from operating and suspended services. A future idea is not an operational failure. It must not create missing-departure/SLA alerts or critical auto-pause merely because its cards are incomplete.
- A draft can remain unlaunched indefinitely. An optional intended start date is a planning target, not an automatic activation command, public timetable or guarantee. Passing that target marks the plan for review, not as an operated/missed Trip, and does not delete it. Saving, all-green readiness, closing a window, loading a save or unpausing never launches it automatically.
- Merely saving or evaluating a draft does not advertise service, sell tickets, generate executable Trips/preparation jobs, dispatch vehicles, move cargo, buy anything or reserve fleet/crew/infrastructure capacity. Hypothetical timetable previews must be visibly separate from actual Trips and reservations.

The player may separately acquire vehicles, build facilities or accept access/capacity agreements while preparing the plan. Those are real, explicitly accepted actions through the existing systems, with their own costs and obligations. Keeping the Line unlaunched does not suspend their fees; deleting or changing the draft does not cancel/refund those commitments. Show their links and costs even before launch. A draft itself is not a capacity reservation: two drafts may consider the same resources, but cannot both later acquire the same unavailable capacity.

#### Readiness is separate from completion and operation

Keep an overall readiness summary visible alongside the cards: what is missing, which dependencies are only expected, what has actually been secured and whether the selected service can be activated. Do not reduce this to a percentage of filled fields. Suggested status wording:

| Readiness state | Meaning |
|---|---|
| Not filled in / Nevyplněno | Required planning input is missing |
| Needs resolution / Vyžaduje dořešení | A concrete incompatibility, shortage or missing right blocks activation |
| Pending dependency / Čeká na zajištění | For example a delivery, project completion, licence decision or capacity request is pending; an estimate is not a completed prerequisite |
| Needs recheck / Nutno ověřit | Required inputs are unknown or an earlier result became stale |
| Verified for activation / Ověřeno pro spuštění | Relevant hard requirements pass for the displayed service, intended start and assessed operating period; any warnings and actual commitment status remain visible |

Exact labels/colours are presentation details. Use text/icons as well as colour. Distinguish a complete form, a feasible forecast and secured contractual capacity. A sold resource, expired right, changed route, delayed delivery or new conflicting duty invalidates the relevant readiness, not the stored plan. Recheck on relevant changes and explicit checks; do not rerun the whole network for every dormant draft every frame. A restored cached result cannot authorize activation without fresh validation.

Readiness uses the existing shared feasibility rules/ledgers, including compatible fleet and preparation, qualified staff, facilities, local presence/licences, municipal conditions where applicable, endpoints, energy, slots, sales channels and transport obligations. Do not require specific serial-number vehicles earlier than the canonical criteria-based assignment/preparation rules require. Check the relevant future period, not only the instant when the player opens the card. A future dependency may be shown as conditional; never label a merely expected delivery, unaccepted slot quote or unbuilt endpoint as actually secured/usable.

#### Explicit launch and later changes

Launch/Activate is a separate action with a current readiness and consequence review. It identifies which Patterns/versions and effective time are being committed, shows costs/agreements and remaining warnings, and revalidates before applying any commitment. Hard blockers prevent activation but never prevent continuing to edit/save the draft. A business-risk warning such as uncertain revenue is not automatically a physical/legal blocker. Repeated clicks or parallel windows cannot double-book or activate twice.

A Line can include operating Patterns and separate unfinished proposals. Show readiness for the intended activation scope; an unrelated unfinished variant must not be silently launched or falsely make all existing operation unready. Keep plan lifecycle (unlaunched versus activated) separate from the current readiness assessment. A fully ready draft can intentionally remain a draft.

For an already active Pattern, card edits prepare a future version under GAME_DESIGN Section 32.2, never rewrite running Trips or turn the operating Line back into a no-obligation draft. Preserve the explicit effective date, impact checks, sold bookings/cargo allocations, old/new slot transition and contractual settlement. Suspension, closure and early capacity release retain their own actions and consequences.

Do not force every track/platform to be selected. Preserve automatic compatible routing, the distinction between requested times, accepted slot windows, planned midpoints and physical occupancy, and the existing Capacity Order/Auto-renew workflow. All planning remains available in pause under Section 9.1; card navigation and saving a design are not time-control or physical-work commands. This decision does not settle the separately unresolved timing of binding commands during pause.

### 6.2 Proposed contract and shipment planning

Start from the opportunity/contract or shipment, not necessarily from building a new Line. Show a readable origin-to-destination chain with its own-service and external legs. Allow reuse of existing feasible services under the canonical allocation rules.

A split-shipment view should show, for each physical portion:

- quantity and actual location/custody;
- handling/readiness state;
- next reserved Trip and stop interval, distinct from the Trip currently carrying it;
- timing, connection risk, age/quality and contractual obligation where relevant.

Example presentation can illustrate the existing 100 t shipment split across multiple Trips, but every displayed total must reconcile to the actual ledger. A total such as "100 t allocated" must never imply "100 t already loaded". Changing a reservation cannot visually relocate cargo or restart its age.

The default experience should help plan at shipment/contract level. Detailed manual allocations remain governed by the existing rules; do not force individual-lot micromanagement or replace protected priority tiers with a new hidden score.

### 6.3 Proposed construction workflow

Proposed flow: select tool → place/edit free-form preview → inspect geometry and effects → review project → commit.

The review distinguishes one-time and recurring costs, land/access permissions, materials, contractors, expected duration and affected operation. Invalid geometry is highlighted with a cause and an available remedy. Keep snapping limited to valid physical connections, not an invented world grid.

An uncommitted ghost is not infrastructure and clearing it is not paid demolition. Committing creates a real construction project under the existing rules; completion is not instantaneous. Editing/removing existing infrastructure uses its own permission, closure and cost checks. Construction planning remains available during manual pause under Section 9.1; physical construction progress still requires advancing simulation time.

### 6.4 Confirmed active Line detail and future-change separation — UI-D12

**Keep the same Line window, card groups and recognizable arrangement before and after launch. Once operating, add a live operational overview above the cards rather than replacing planning with an unrelated management interface.** The player accepted this proposal on 2026-09-30. Section 6.1 continues to govern drafts/readiness, and GAME_DESIGN Section 32 remains the owner of Line/Pattern/Trip mechanics and lifecycle actions.

#### Header and operational overview

The header shows the Line name, identifying colour, transport mode/purpose and lifecycle state, with explicit Show route on map, window pinning and an actions menu. Colour supplements text; it is not the only way to identify the Line. Keep normal window movement, resizing and bottom-bar access.

Immediately below, show a compact summary of current operation: running Trips, the next departure or demand-driven waiting state, and problems requiring player decisions. Counts and next-event details must have a clear scope and time reference. An active Line can legitimately have no Trip running right now; do not call it suspended merely because the next service is later.

Keep **lifecycle state**, **current operational health** and **readiness of a proposed change** separate. An operating Line with one failed vehicle is not automatically an unlaunched or suspended Line. Conversely, a green future proposal does not prove the active service has no incident.

Show important incidents with cause, impact, handling status and available response. Distinguish Requires your decision from Dispatcher handling; do not imply that an authorized automatic recovery must be performed a second time by the player. With no decision needed, collapse the issue area to a concise neutral message, not a large empty panel. If incidents are still being handled, do not label the entire operation problem-free. Group common causes using Section 7.2 and use direct object links from Section 4.1.

Illustrative content only:

> R12 · Praha–Brno · Passenger rail · Operating
>
> Running Trips: 2 · Next departure: 10:20 · Requires your decision: 1 incident
>
> The 10:20 Trip is at risk: Vehicle 014 is unavailable and no authorized replacement is secured.
>
> Open Trip · Open vehicle · Review available response

Display actual simulation state or clearly identified estimates, not these example values. Opening the window or following a link does not change time state; critical-event pause remains the separate confirmed rule.

#### The same cards, now with current operating information

Reuse the six functional groups in Section 6.1 and their editing/navigation model. On an active Line, the collapsed cards expose current facts and relevant problems as well as configuration:

| Card | Compact active-service summary |
|---|---|
| Route and stops | Route identity, stop count and relevant closure/restriction; drill into stops, routing constraints and the map |
| Operating plan | Service days/frequency or departure condition, next departure and affected Trips; drill into calendars and actual journeys |
| Vehicles | Coverage of upcoming Trips and actual shortages/assignments; do not imply every asset is permanently attached to this Line |
| Staff and facilities | Qualified staffing and operating-base/service coverage, with actual maintenance, handling, energy or supply bottlenecks |
| Rights and capacity | Valid access/slots, missing or at-risk commitments and relevant agreement expiry/renewal; drill into the existing agreements |
| Economics and obligations | Result and utilization for a visibly selected period, plus material contractual risks; drill into actual revenues, costs and commitments |

Cards have a heading, a few useful facts and an issue indicator when needed. They reflow from columns in wider windows to a readable vertical arrangement in narrower windows; do not replace them with oversized decorative tiles or hide essential controls at larger UI scales.

Metrics use the existing simulation/reporting data and the selected Line/Pattern scope. Label game-time periods and distinguish actual results from forecasts. Explain the basis of utilization and financial totals on inspection; do not mix onboard load, reserved capacity and a period average, or double-count shared assets, Trips or costs across cards/variants. Missing observations show insufficient data, not invented zeroes or a new hidden scoring system. No new accounting model or fixed profitability threshold is approved here.

#### Running Trips and upcoming departures

Provide a compact expandable Running and upcoming Trips list directly from the overview, without requiring the player to edit the timetable. Each row identifies the concrete Trip, direction/destination, current state and useful timing: planned time versus actual/estimated departure or arrival and delay. Name which event a delay refers to. Assigned vehicle/consist and station references are separate contextual links when available; opening the row opens that Trip.

All Trips opens the full dated list with problem/status filters. Keep cancelled Trips inspectable with their cancellation reason and history; do not remove them from the player's account of what happened. Preserve selection and scroll position during live refresh. Display the service date for cross-midnight journeys and enough identity to distinguish different Trips sharing a departure time.

Demand-driven services show their real condition, such as Waiting for cargo: 32 of the required 40 t, and any applicable latest-departure limit. This is illustrative, not a fixed load threshold. Do not invent a scheduled time or a guaranteed estimate when it is unknown. Before a concrete Trip exists, identify the item as a service/departure condition and link to the relevant Pattern, not a fabricated Trip. A cargo-ready quantity is not automatically already loaded; preserve the existing readiness/custody distinctions.

#### Variants and scope

Use All variants / a specific variant inside the same Line window. All variants summarizes actual operation across the Line; selecting a Pattern scopes the overview, cards, Trip list and results to it. Always show the current scope and distinguish common settings from mixed values. Opening one variant cannot silently edit or apply a setting to every other variant.

Operating, suspended and unlaunched variants remain distinguishable. A future express proposal may sit beside running basic/weekend variants, but its incomplete cards are planning work, not an operational fault of the running Line. Keep any separately accepted real costs/obligations visible under Section 6.1. Aggregate operation must not include hypothetical Trips, ticket sales or projected revenues as if they had occurred. Filtering the UI never changes activation or commercial obligations.

#### Current operation versus a future change

Provide **Prepare change / Připravit změnu** from the active Line/Pattern view. The player edits and saves a future proposal through the same cards in any order while current operation continues. Keep the current effective configuration and the working change clearly labelled, with a direct way to inspect each; they are not two competing authoritative services.

Example:

> Current operation: departures every 60 minutes.
>
> Working change, not applied: departures every 30 minutes. One additional suitable vehicle and revised capacity are still needed.

Save plan stores the proposed settings and readiness only. It does not apply them. A separately committed future version shows its accepted effective date/time and commitment state, distinct from an uncommitted target date. Before applying, show the affected Patterns/versions, effective time, readiness and consequences for fleet, slots, tickets, cargo and contracts. Revalidate with the shared rules; stale or partial checks cannot authorize activation.

Follow GAME_DESIGN Section 32.2 for version boundaries, already generated future Trips, running Trips, reservations and slot transition. Do not rewrite a running Trip or cancel/recreate it merely because the overview has changed. An uncommitted change can remain unfinished while the old version runs; a published/committed future version retains its actual obligations and cannot be treated as a cost-free draft. Preserve both operational state and saved proposals across save/load without duplicate generation or automatic draft activation.

Expose Suspend Line/Pattern and Close Line/Pattern as distinct, clearly labelled actions with scope and impact confirmation, not a casual one-click on/off switch. They use the existing lifecycle, replacement-service, cancellation and capacity-retention rules. Closing this UI window is unrelated to closing a service.

Exact pixel dimensions, wording and secondary presentation remain visual-design work. This decision confirms the window composition and interactions above, not new dispatch priorities, vehicle allocation rules, performance measurements or completed UI implementation.

## 7. Problem explanation and notifications

### 7.1 Proposed presentation of problems

Use the same problem model in planners, inspectors, lists and the event area:

**What happened → why → operational/commercial impact → available action.**

Specific objects mentioned in these explanations must be directly clickable under confirmed Section 4.1, regardless of the final notification layout. A generic Details button does not replace inline links to distinct referenced vehicles, facilities or Trips.

Example, illustrative rather than a fixed balancing rule:

> Departure cannot be activated: the planned train is longer than every accessible platform at this stop.
>
> Inspect platform limits · Change consist · Review another compatible stop

Separate **hard blockers**, **risks/warnings**, **information** and **completed events**. An actionable warning is not silently promoted to a blocker, and a hard physical/legal constraint cannot be bypassed by dismissing a warning.

Group repeated messages about the same incident, show its affected services and allow drill-down. Avoid one pop-up per delayed train when one closure is the cause. Keep information and routine successful automatic actions in history; surface decisions needing player authority. A manager action should show its cause and the policy/budget that authorized it.

Colours supplement icons and text, never carry status alone. Distinguish unacknowledged, being handled, awaiting a decision and resolved where these states exist. Critical-event automatic pause is confirmed separately in Section 7.2; the remaining notification layout is still proposed. Opening an ordinary event window is not itself a pause trigger.

V1 explanations must be accessible through focus/click as well as hover. A simple details view or pinned explanation can work without making deep nested tooltips a new V1 requirement.

### 7.2 Confirmed critical-event automatic pause — critical-event part of UI-D08

**Automatic pause is enabled by default for critical incidents. Ordinary delays and routine problems being handled within authorized dispatch/management policies do not automatically interrupt play.** The player confirmed this choice on 2026-09-30.

Critical means a serious actual operational/business threat requiring prompt player attention, not every warning, red label or invalid uncommitted plan. A major route closure with no feasible authorized recovery is an illustrative case. The incident must expose its cause, affected operation/obligations and why player attention is needed. The detailed event catalogue and numerical severity thresholds still require authoring and validation; they must not silently reclassify routine delays as critical. Physical safety and valid automatic recovery remain simulation responsibilities, not a new manual emergency-driving mechanic.

Implementation safeguards for this decision:

- Trigger on a new critical incident or a material escalation, independently of whether its location/window is visible. Apply the pause at a consistent simulation-event boundary after the triggering atomic transition and required same-time causal processing, before advancing to later game time. Do not wait for a distant UI refresh at 16x, rewind the incident or leave a transaction half-applied.
- Show a prominent, localized explanation that a critical event paused the game, its impact and a route to the relevant detail/available response. Preserve open windows and drafts; keep the map, inspection, planning and time controls usable rather than trapping the player behind a blocking notification.
- Freeze the same shared clock and time-driven systems as in Section 9.1. Do not accumulate paused wall time or an unused pre-pause time budget for later catch-up. Future simulation events remain queued; none are skipped or replayed merely to handle a notification.
- Resume only through an explicit player time-control action. Closing, acknowledging or resolving the notice does not automatically resume time, release an existing manual pause or alter the remembered running speed. The player may resume while an incident remains unresolved; the actual consequences and hard safety constraints still apply.
- Deduplicate by stable incident identity and escalation state. Group downstream alerts from one cause rather than pausing for every affected vehicle. An unchanged incident must not immediately pause again after deliberate resume. A genuinely new critical incident or material escalation can trigger another pause. Events presented while already paused must not create a chain of redundant pauses on resume.
- Preserve the incident's handling/acknowledgement and auto-pause-trigger state across save/load. Reopening a window, refreshing data or loading a presented incident is not a new occurrence. Existing safe-paused loading rules remain unchanged; acknowledgement never resolves an operational incident or deletes its obligations.

Per-event-type overrides were proposed during discussion; their exact settings UI remains proposed. The confirmed critical-event default must work without requiring the player to configure it. Application-focus loss/return and precise pause-menu transitions are still separate unresolved parts of UI-D08.

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

### 9.1 Confirmed normal-UI and manual-pause behaviour — UI-D04

**Ordinary windows, Line planning and construction planning do not automatically stop the game. The player pauses manually when they need time to think; all planning remains available in that pause.** This decision was confirmed by the player on 2026-09-30. A critical incident can independently pause the game under Section 7.2; it is the incident, not the open planner, that triggers that pause.

- Opening, closing, minimizing, restoring, moving or resizing an ordinary management/detail/planning window does not change whether the game is running or paused, and does not change the selected speed. Entering or leaving a construction preview or Line planner follows the same rule. Closing a planner must not release a manual pause.
- While the game is running, the player can inspect ongoing operations and prepare plans at the selected simulation speed. The existing pause/time controls remain accessible while these windows are open.
- During manual pause, the camera, selection, windows and planning tools remain usable. The player can inspect information, draft track/building layouts, configure Line/Pattern proposals, prepare orders and review feasibility/cost previews. Pausing must not turn those editors into read-only screens or require running time merely to edit a plan.
- The shared simulation clock does not advance during pause. Vehicle movement, physical construction, loading/unloading, maintenance/repairs and all other time-driven work remain stopped. Production, cargo ageing, staff rest, research, periodic finance, contract deadlines and AI operation cannot continue on a separate background clock. Presentation/UI response may still use real time without creating simulated progress.
- Physical work continues only after simulation time resumes, from the paused state. Real time spent planning in pause is not accumulated as a simulation catch-up budget. Opening or closing a window cannot cause a catch-up jump.
- Planning is not commitment. A draft or ghost remains free of operating/commercial side effects in either time state; saving a Line draft under Section 6.1 changes stored planning data only. Neither unpausing nor closing the planner silently accepts it, books capacity or places a purchase/construction order. Existing explicit acceptance, validation, versioning and transaction rules still apply. This approval of paused planning is not a new rule for whether binding commands execute immediately or are queued during pause; it cannot be used to invent free work, bypass validation or complete physical stages instantly.

Show the actual pause/running state and selected speed clearly. Continue to use the existing game clock/calendar, including its supported speed choices and 14-day months; do not use a Gregorian date picker for game dates. The existing rule that no simulation advances during incomplete loading remains unchanged.

Application-focus loss/return and precise pause-menu transitions remain unresolved under the remaining part of UI-D08. Critical-event auto-pause is now confirmed in Section 7.2; do not treat it as still undecided or use it to enable unrelated pause/resume triggers.

### 9.2 Shared command and workspace safety

Every costly or irreversible command must be revalidated against current simulation state. If a live preview becomes stale, explain changed prices, availability or affected obligations before accepting a revised commitment. Repeated clicks, including submissions from different windows, cannot duplicate an order/payment. Closing a panel cannot undo a committed transaction. Multiple views use the same authoritative state/command validation, not independent ledgers.

Preserve useful navigation context when opening a corrective workflow and returning to a planner. UI preferences such as scale and window geometry are distinct from save-game authority. Saved Line/Pattern drafts in Section 6.1 belong to campaign planning data, not window geometry, and survive closing their windows. Restoring an inspector, filter or uncommitted draft cannot execute a purchase, advance construction or regenerate physical cargo. If an inspected object is no longer available, show its valid history or an explicit unavailable state instead of broken controls. Content pinning never makes a stale object reference authoritative. Contextual links use the target-validation and history rules in Section 4.1; following a link is navigation, not a business command.

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
| UI-A07 | UI-D04, no automatic pause/resume from ordinary UI | With no unrelated incident/focus trigger, open, move, minimize, restore and close representative detail, Line-planning and construction windows at 0.5x, 1x and 16x; the selected running state/speed stays unchanged. Repeat while manually paused; opening/closing the planner never resumes time. Pause controls remain accessible |
| UI-A08 | UI-D04, useful planning during manual pause | Pause mid-operation, then inspect the map, edit Line and construction proposals and prepare order previews without submitting binding commands. Verify editable UI with unchanged simulation time, vehicle position, physical-job progress, inventories and time-driven accounting. Resume explicitly; work continues from that state, paused wall time is not caught up and drafts are not automatically committed |
| UI-A09 | UI-D08, critical-event automatic pause | With default settings at 0.5x, 1x and 16x, trigger a genuinely critical incident, including with an open planner and an off-screen affected location. Verify a consistent event-boundary pause, localized cause/impact/response access, usable planning and stopped time-driven simulation. Routine delay, authorized routine recovery and an invalid uncommitted plan do not trigger it |
| UI-A10 | UI-D08, pause lifecycle and persistence | Present repeated alerts and multiple affected vehicles from one incident, close/acknowledge its notice, explicitly resume with it unresolved, then save/load. Verify no automatic resume, unchanged running-speed choice, no catch-up, no lost drafts and no repeated pause for the same unchanged incident. A new critical incident/material escalation can pause again. An already active manual/loading pause is never released by incident handling |
| UI-A11 | UI-D09, direct links across windows | In a notification naming a specific vehicle, depot and Trip, activate each inline phrase by mouse and keyboard in CZ/EN and verify the exact target detail. Follow vehicle-to-Line/Trip/depot links, restore an existing minimized target, preserve pinned identities and return to the source/draft context. No generic fleet-search detour, duplicate object/editing copy, hidden order, camera jump or pause/speed change |
| UI-A12 | UI-D09, identity and historical-link safety | Test equal names/models, renamed and sold/scrapped targets, a remote target without a rendered proxy, and an old incident after save/load. Links retain the original stable identity, respect current permissions and distinguish historical text from live detail; missing targets yield retained history or an explicit unavailable state, never a guessed substitute. Generic concepts and arbitrary player text cannot become unintended entity links/commands |
| UI-A13 | UI-D10, operations-first vehicle detail | Open representative road and rail vehicle details with a small static correct-model preview. Identify current activity/problem, actual location, applicable load/destination and next task without a large image or long parameter list; live values update independently of the still image. Verify an idle vehicle, unavailable estimate, missing preview, and locomotive-versus-consist distinction, at 1080p/enlarged UI in CZ/EN. No required live camera, animated model viewer or extra simulation |
| UI-A14 | UI-D11, nonlinear cards and durable drafts | Create a Line plan, edit vehicle requirements before the route, save incomplete cards and navigate out of order. Close all its windows, save/load the campaign and reopen it from the plans view; contents/identity remain, missing inputs do not block saving and no wizard sequence is required. Test CZ/EN, enlarged UI and running/paused editing |
| UI-A15 | UI-D11, trustworthy readiness | Distinguish filled fields, expected delivery/project completion, a slot quote and actual secured capacity. Change route, expire access, delay a delivery and create a competing resource commitment; preserve the draft while marking/rechecking affected readiness. Test missing inputs, a future intended start, expired target date and restored cached results; unknown or stale information never authorizes activation |
| UI-A16 | UI-D11, deliberate activation and no phantom operation | Leave incomplete and all-ready drafts unlaunched across time/save/load: no ticket sales, executable Trips, preparation jobs, reservations or missed-service incidents arise from the draft. Explicitly launch after fresh checks and consequence review; hard blockers prevent launch, not editing/saving; repeated/parallel launch cannot duplicate commitments. Two drafts considering the same resources cannot both overbook them. Separately accepted purchases/access contracts retain costs/obligations when the draft is changed/deleted |
| UI-A17 | UI-D11, active versions and scoped activation | Edit an operating Pattern through cards into a future draft while its old version/running Trips continue. Check effective time, reservations, contracts and capacity transition before activation. An unfinished unrelated variant stays a draft, is not silently launched and does not turn active services into no-obligation plans |
| UI-A18 | UI-D12, one Line workspace and operational health | Open the same Line before/after launch and verify stable card groups/arrangement with the added live summary. Test no current Trip, a vehicle failure, an automatically handled incident and an unresolved player decision; lifecycle, incident handling and draft readiness remain distinct. Verify compact reflow, clear metric periods/bases and unchanged pause state in CZ/EN at 1080p/enlarged UI |
| UI-A19 | UI-D12, actual Trips and variant scope | Inspect current/upcoming and all dated Trips, including delayed, cancelled, cross-midnight and demand-driven cases. Follow exact Trip/vehicle/station links, preserve live-list selection and show unknown times honestly. Switch All variants/specific Pattern with operating, suspended and unlaunched variants; scope stays explicit, hypothetical work is excluded from actual results and no filter edits/activates other Patterns |
| UI-A20 | UI-D12, clearly separated future changes | Prepare and save a future change through the active Line window while old operation continues; visibly distinguish current, uncommitted and committed-future configuration. Verify readiness/effective-time/impact review, unchanged running Trips, no automatic application on save/load and no duplicated commitments. Suspension/closure are separate scoped consequence previews; closing the window does not stop the Line |

### Remaining proposed interaction scenarios

These are scenarios for evaluating the remaining proposal, not passing tests or additional approved release gates. Formal gameplay acceptance remains in V1_ACCEPTANCE_TESTS.md.

| Scenario | What the proposed UI should demonstrate |
|---|---|
| Found a company | Find the existing 1900/region/loan, office, staff and licence steps without a hidden setup screen or free assets; remain mode-neutral |
| Track split cargo | Explain where all portions are, what is ready/loaded/reserved and which connection is at risk |
| Release capacity | Distinguish non-renewal from early cancellation and see total/per-owner settlement plus dependent services |
| Build infrastructure | Distinguish ghost preview, accepted project and completed usable asset; clicking a floating tool window does not place infrastructure behind it |
| Manage disruption | Navigate from one grouped incident to its cause and a valid authorized response; critical-event pause and contextual object links follow the confirmed checks above |
| Use CZ/EN and enlarged UI | Complete the same workflow without clipped material information or hover-only actions |
| Save/load and live refresh | Preserve game authority; restored UI state, repeated clicks or parallel views cannot create duplicate commitments |

No Unity UI has been implemented or visually tested as part of this document. Structural documentation checks, when run, do not validate these interaction scenarios.

## 11. Decision status

| ID | Decision | Current direction/recommendation | Status |
|---|---|---|---|
| UI-D01 | Overall visual character | Restrained contemporary dark interface over the model world, with limited historical flavour; exact styling tokens remain open | CONFIRMED on 2026-09-30 |
| UI-D02 | Workspace/window model | Individual management/detail panels are movable floating windows; not a mandatory fixed right inspector | CONFIRMED on 2026-09-30 |
| UI-D03 | Information density | Operations-first vehicle overview, compact Line-planning cards and active Line overview confirmed under UI-D10/UI-D11/UI-D12; density for other object types/screens remains proposed | PARTIALLY CONFIRMED on 2026-09-30; vehicle and Line overviews |
| UI-D04 | Normal UI and manual-pause planning | Ordinary windows, Line planning and construction previews never auto-pause/resume or change speed; manual pause retains all planning tools while time-driven simulation remains stopped, under Section 9.1 | CONFIRMED on 2026-09-30 |
| UI-D05 | Navigation and Czech terminology | Top-level Provoz, Obchod, Majetek, Firma and Svět alongside Stavět are accepted; detailed contents and object glossary in Section 4 remain proposed | PARTIALLY CONFIRMED on 2026-09-30 |
| UI-D06 | Fixed bottom bar | Stable bottom navigation/status/time control area with the functional grouping in Section 3.3, instead of mandatory left/top strips; exact visual dimensions and secondary controls remain open | CONFIRMED on 2026-09-30 |
| UI-D07 | Detailed window interaction | Resizing, multiple views, reusable unpinned detail, content pinning, explicit new-window action, minimize/restore and remembered/recoverable layout under Section 3.2; snapping is optional and never compulsory docking | CONFIRMED on 2026-09-30 |
| UI-D08 | Critical incidents and remaining exceptional pause triggers | Critical incidents automatically pause by default under Section 7.2; routine delays/authorized routine recovery do not. Application-focus loss/return, precise pause-menu transitions and detailed override settings remain unresolved | PARTIALLY CONFIRMED on 2026-09-30; critical-event default CONFIRMED |
| UI-D09 | Contextual object links | Specific object mentions in messages and other views open that exact object's detail; connected windows share identity, selection/pinning, context preservation and safe historical navigation under Section 4.1 | CONFIRMED on 2026-09-30 |
| UI-D10 | Vehicle detail and model preview | Operations-first default overview with a small correct-model preview; a static image is sufficient and live operational data remains separate, under Section 5.2 | CONFIRMED on 2026-09-30 |
| UI-D11 | Card-based Line planning and unlaunched plans | Independently editable cards instead of a wizard; persistent incomplete/future Line drafts, visible dependency-based readiness and separate explicit activation under Section 6.1 | CONFIRMED on 2026-09-30 |
| UI-D12 | Active Line detail | Same window/cards before and after launch, live operation/issues and actual Trips, explicit variant scope, period-based results and separate future changes/lifecycle actions under Section 6.4 | CONFIRMED on 2026-09-30 |

The player's acceptance of the bottom-bar/window proposal includes updating one ordinary detail window until it is pinned, rather than opening a new window for every ordinary object click. Normal-window/planning pause behaviour is resolved under UI-D04, critical-event automatic pause under UI-D08, contextual object links under UI-D09, the compact vehicle overview under UI-D10, nonlinear persistent Line planning under UI-D11 and the active Line workspace under UI-D12. Do not reopen those choices or reintroduce the superseded Line-creation wizard. Focus/menu details of UI-D08 and the other explicitly proposed details remain undecided. Approval of these decisions does not silently approve every detail in this document.
