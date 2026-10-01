# Tranzit — UI/UX design

> **Status: PARTIALLY CONFIRMED DESIGN — remaining details are proposals.** Updated on 2026-09-30 during the interface discussion with the player.
>
> **Confirmed:** UI-D01, a restrained contemporary dark interface over the model world; UI-D02, movable floating management/detail windows; UI-D04, ordinary windows and planning do not automatically pause/resume the game, and planning remains available during manual pause; UI-D06, a fixed bottom navigation/status/time bar; UI-D07, resizing, multiple windows, reusable selection details with content pinning, minimize/restore and remembered/recoverable layout; the critical-event part of UI-D08, automatic pause enabled by default for critical incidents; UI-D09, contextual links between windows and directly from mentions of specific objects; UI-D10, an operations-first vehicle overview with a small model preview that may be static; UI-D11, freely editable Line-planning cards, persistent unlaunched plans and an explicit readiness/activation decision; UI-D12, the same Line window/cards after launch, with a live operational overview, scoped variants/Trips and clearly separated future changes; UI-D13, a directly accessible list of planned and actively deployed vehicles from Line capacity planning onwards; UI-D14, station/terminal presentation in the focused UI_STATIONS specification; UI-D15, a minimalist, clear and consistent interface throughout the game, with secondary information in contextual hover/focus tooltips and intuitively grouped functions; focused UI-D16–UI-D23 specifications cover depots, commercial work, construction, finance, company/workforce, map opportunities, fleet acquisition and split Shipments; UI-D24 covers the event centre and notifications; UI-D25 covers one concrete Trip's readiness, live execution, segment capacity and retained history; UI-D26 covers coordinated infrastructure capacity/access ordering and the company-wide capacity-agreement overview; UI-D27 requires every external-company detail to expose all agreements between that company and the player's company; UI-D28 covers City and Region views with directional demand, firms/industry, transport, opportunities, player presence, municipal agreements and knowledge provenance; UI-D29 covers tariffs, integrated Line systems and single/weekly/monthly ticket products; UI-D30 covers fleet-wide maintenance planning, preventive-target versus hard-limit visibility and workshop/provider capacity; UI-D31 covers vehicle duties, aggregate crew duties, physical transitions and duty conflicts; UI-D32 covers company-wide procurement, physical supplies, supplier relationships and reorder rules; UI-D33 covers licences, permits and market entry; UI-D34 confirms a dedicated neutral money icon as the compact player-facing shorthand for the single `money` accounting unit; UI-D35 covers New Game and opening-only real company founding/onboarding; UI-D36 covers the main menu, save/load, pause-menu lifecycle and settings; UI-D37 completes the adaptive external-company/competitor detail around UI-D27, with known operation/assets, products/services, relationship/history, ownership and information boundaries; UI-D38 confirms one simple Technology workspace where research/knowledge unlocks concrete options and only genuine company systems use a separate adoption project; UI-D39 confirms ownership/acquisitions with AI-managed controlled subsidiaries, a small set of owner directives/interventions, explicit intra-group transactions and physical infrastructure-market continuity; UI-D40 confirms one simple World News/history feed for meaningful historical, economic, infrastructure and company changes with concrete known player impact and strict separation from operational incidents; UI-D41 confirms the final HUD/navigation composition and global search. The top-level navigation and detailed taxonomy are confirmed by UI-D05/UI-D41; canonical player-facing CZ/EN terminology is fixed in UI_GLOSSARY.md. These directions guide UI implementation within the existing release scope.
>
> **Still open or proposed:** exact visual tokens and dimensions, secondary-control placement and implementation-level layouts not explicitly locked by the focused specifications. The global minimalist information hierarchy is confirmed; this does not approve every proposed screen or unrelated pause trigger. A written design is not an implemented or tested UI.
>
> Existing requirements referenced in Section 1 remain binding. Keep this owning UI document and affected summaries/acceptance criteria consistent when a decision changes; retain explicit status for unresolved choices. Do not use presentation decisions to override gameplay or silently add release scope.

## 1. Existing requirements and document responsibility

Read these owners rather than treating the summaries below as replacement rules:

| Owner | Relevant existing requirement |
|---|---|
| [V1_SCOPE.md](V1_SCOPE.md), Sections 1 and 6 | Offline Windows, mouse/keyboard, complete Czech/English presentation, one accounting token `money`, full save/load; first-release modes and start preset remain unchanged |
| [GAME_DESIGN.md](GAME_DESIGN.md), Sections 1.1 and 3 | Explainable outcomes; shared simulation calendar and time controls; deep nested tooltips remain a future pattern, while first-layer contextual tooltips are now required under UI-D15 |
| [GAME_DESIGN.md](GAME_DESIGN.md), Sections 11.0.1, 11.9 and 32 | Separate contracts, shipments, physical cargo portions, transport plans, Lines, Service Patterns and Trips; preserve their existing capacity and lifecycle rules |
| [GAME_DESIGN.md](GAME_DESIGN.md), Sections 13.2–13.2.1 and 32.2–32.3 | One Capacity Order workflow linked to Service Patterns; feasible slot windows, calendar and routing; no mandatory expert track-by-track timetable editing |
| [CONTRACT_CANCELLATION.md](CONTRACT_CANCELLATION.md) | Cancellation/release consequences, per-owner and total costs, prepaid settlement and distinction from non-renewal |
| [V1_IMPLEMENTATION_BRIEF.md](V1_IMPLEMENTATION_BRIEF.md), Sections 4 and 8–9 | Shared selection, validated commands, side-effect-free previews, required player workflows, onboarding, readable 1080p UI and adjustable scale |
| [UI_STATIONS.md](UI_STATIONS.md) | Confirmed UI-D14: station/terminal overview, separate station-style arrival/departure board and serving-Line information; embedded station schematic deferred |
| [UI_EVENTS.md](UI_EVENTS.md) | Confirmed UI-D24: Needs decision / In progress / Information / History event centre, root-cause grouping, toasts and Follow notifications; UI-D08 still owns critical auto-pause |
| [UI_CAPACITY_ACCESS.md](UI_CAPACITY_ACCESS.md) | Confirmed UI-D26: coordinated Service Pattern Capacity Order, request/offer/accepted states, multi-owner impact/cost review and company-wide capacity/access overview |
| [UI_EXTERNAL_COMPANIES.md](UI_EXTERNAL_COMPANIES.md) | Confirmed UI-D27/UI-D37: complete adaptive external-company/competitor detail, all bilateral agreements, known operation/assets, products/services, relationship/history and ownership, with source/time/permission boundaries |
| [UI_TECHNOLOGY.md](UI_TECHNOLOGY.md) | Confirmed UI-D38: simple Technology workspace, research/knowledge unlocks concrete options, physical upgrades stay in owning systems and only genuine company systems use adoption |
| [UI_OWNERSHIP.md](UI_OWNERSHIP.md) | Confirmed UI-D39: ownership vs control; controlled subsidiaries stay AI-managed while the owner can set broad direction, issue concrete directives and transfer capital/assets; infrastructure acquisition/sale preserves physical state and obligations |
| [UI_NEWS.md](UI_NEWS.md) | Confirmed UI-D40: World News/history feed, significant historical/economic/company/infrastructure changes, concrete known player impact and strict separation from UI-D24 incidents |
| [UI_NAVIGATION.md](UI_NAVIGATION.md) | Confirmed UI-D41: final upper HUD + grouped bottom navigation + global search respecting information visibility |
| [UI_CITIES_REGIONS.md](UI_CITIES_REGIONS.md) | Confirmed UI-D28: City detail and Region overview with directional demand, firms/industry, transport, opportunities, player presence, municipal agreements, trends and information-provenance limits |
| [UI_TARIFFS.md](UI_TARIFFS.md) | Confirmed UI-D29: company/global tariffs, integrated groups of Lines with shared rates, ticket products including weekly/monthly passes, real sales/reservation capability and effective-dated changes |
| [UI_MAINTENANCE.md](UI_MAINTENANCE.md) | Confirmed UI-D30: fleet-wide maintenance plan, preventive targets vs hard limits, policy inheritance, dated workshop/provider capacity and future Trip/fleet-reserve conflicts |
| [UI_DUTIES.md](UI_DUTIES.md) | Confirmed UI-D31: vehicle-duty timelines, aggregate crew-duty blocks, physical transition validation, conflict view and planned-versus-actual execution history |
| [UI_PROCUREMENT.md](UI_PROCUREMENT.md) | Confirmed UI-D32: location-specific physical inventory, purchase orders, suppliers, reorder rules, shortage projection and real transport responsibility |
| [UI_LICENCES_MARKETS.md](UI_LICENCES_MARKETS.md) | Confirmed UI-D33: Markets and regions / Licences / Permits / Applications, critical-path readiness and strict separation of market entry, activity licence, local presence and physical access |
| [UI_NEW_GAME.md](UI_NEW_GAME.md) | Confirmed UI-D35: short New Game setup, real in-world branch/company founding and Full/Basics/Off opening tutorial that ends after first functioning transport |
| [UI_SYSTEM_MENU.md](UI_SYSTEM_MENU.md) | Confirmed UI-D36: main menu, campaign-organized saves, atomic save/load safety, independent pause-menu reason, Esc priority and settings categories |

This document owns the confirmed UI directions explicitly identified in Section 11 and develops the remaining presentation proposals. It does not replace the architecture brief, choose new packages, change simulation rules, add transport modes, or reduce V1 to the screens described here. The proposed sections are not automatically additional release gates.

## 2. Interface direction

**The world is the primary workspace. The interface helps the player understand a situation and act on it without repeatedly losing the map.**

Apply the confirmed global principles in Section 2.1 across all screens, together with the specific confirmed rules below:

- Start with a concise summary; expose supporting information through contextual tooltips and deliberate detail expansion. The vehicle and Line overviews below are specific applications, not the only screens covered by this principle.
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

### 2.1 Confirmed global minimalism, tooltips and consistency — UI-D15

**The entire UI must be minimalist, clear, intuitively grouped and visually consistent. Move supporting information into hover/focus tooltips and expandable details instead of displaying every explanation and parameter permanently.** The player explicitly requested these rules for the whole game on 2026-09-30 and authorized their elaboration. They apply to existing and future screens, not only vehicle or Line details. Exact design tokens and per-screen dimensions remain implementation work.

#### Three information levels

| Level | What belongs here |
|---|---|
| Visible overview | Object identity, scope/date/period and units, meaningful current status, a few relevant operating facts, the main blocker or decision, and discoverable primary actions |
| Contextual tooltip | Definitions, what an icon means, metric calculation basis, contributing factors, supporting parameter values, estimate assumptions, limits and concise reasons behind a status |
| Opened detail | Complete tables, histories, comparisons, editable settings, complex causal chains and explicit commercial/operational actions |

Minimalism means reducing visual noise, not removing management depth or hiding necessary decisions. Keep cards compact, related values aligned and decoration restrained. Use readable spacing rather than huge website-style tiles, tiny type or a wall of labels. Long technical lists and repetitive explanatory paragraphs should not dominate the default view.

A blocker such as "Missing compatible vehicle" remains visible; its exact compatibility checks and alternatives can be in the tooltip/detail. A status such as "Out of slot" remains visible; hover can explain the applicable time window and contributing delay. These are illustrative presentations of existing rules, not new thresholds. Unknown, estimated and stale values must already be identifiable in the overview; a tooltip must not be the first place that reveals a displayed fact was only a guess.

Never hide the only indication of a critical incident, failed save, invalid command, unsaved change, activation blocker or material financial consequence behind hover. Confirmation screens retain readable totals, affected objects, effective dates and required cost/obligation disclosures. A short tooltip may elaborate them; it cannot replace the established impact review. Required vehicle rosters, serving-Line lists and station boards remain directly accessible under UI-D13/UI-D14, not replaced with tooltip-only lists or a single unexplained count.

#### Tooltip interaction and content

Provide reusable first-layer tooltips for meaningful metrics, statuses, abbreviated/icon controls and explanatory terms. Do not add redundant popups to every self-explanatory word. Use consistent visible affordances, such as an information marker or underlined explanatory term where useful. Distinguish an object link that opens a detail from a term that explains a concept; preserve direct object navigation under UI-D09.

Show tooltips after a short intentional real-time hover delay and through equivalent keyboard focus/help interaction. Exact timing is a shared adjustable implementation value, not a game-time delay. Hover is not the sole route to essential information: offer focusable help or a click-open details path, including for disabled actions whose controls cannot receive focus.

Keep the first layer short: what the value/status means, its main cause or breakdown, and a route to more detail when needed. Do not put whole forms or long scrollable management tables into a transient hover popup. An explanation containing links must remain reachable while the pointer/focus enters it; moving from its trigger must not immediately dismiss it. Let the player dismiss it without closing a window or losing a draft. Reposition/wrap it within the viewport at enlarged UI scales; do not cover the trigger or necessary confirmation controls when avoidable. Use a stable click-open detail for longer reading, not an obligatory chain of nested tooltips.

Tooltips use the same structured reasons, values, units, timestamps and object IDs as the main view. They cannot invent causes, stale prices or forecasts, leak unavailable information, or execute commands on hover. Where live data changes, keep the explanation coherent with the value being explained. Opening/dismissing a tooltip does not pause/resume, alter reservations, acknowledge incidents or generate simulation work. Timed presentation still works during manual and critical-event pause.

First-layer hover/focus explanations are required in V1. The deep nested-glossary pattern described in GAME_DESIGN Section 1.1 remains deferred; this decision neither requires infinite tooltip nesting nor defers ordinary tooltips until after V1.

#### Intuitive grouping and one design system

Group functions by the player's task, not by internal simulation modules. Keep related information and its corrective actions together. Reuse the established cards, contextual links and window behaviours instead of creating a new navigation convention per screen. Within comparable windows, keep summary, details and action placement predictable. Preserve the non-linear Line planner; intuitive grouping is not permission to reinstate a mandatory wizard.

Keep primary actions visible and secondary actions in a consistently labelled menu or detail area. Irrelevant functions need not occupy empty cards, but a relevant unavailable function must explain what is missing. Distinguish Save plan, Activate/Apply, Cancel editing and Terminate service consistently; never use the same ambiguous button to mean discarding a draft in one screen and ending a paid commitment in another.

Implement shared style tokens and components for typography, spacing, surfaces, borders, corner treatment, icons, buttons, fields, cards, tables, links, tooltips and window chrome. The same semantic state uses the same wording, icon and colour role across screens, with text/focus cues rather than colour alone. Line-identification colours are distinct from warning/critical status styling. Avoid bespoke per-screen control designs and duplicated navigation to different copies of the same object.

The station-style board in UI_STATIONS may have its approved specialist row/lettering treatment while retaining common window controls, links, focus, status semantics and readability. Consistency does not erase its character or restore the deferred schematic. Adapt columns and card layout to window size, Czech/English text and UI scale without hiding indispensable information. No new branded palette, exact font or pixel values are approved here.

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
| Event access | Compact incident/decision indicator in the bar, opening the event view | CONFIRMED with UI-D24 event-centre layout; critical-event pause remains owned by UI-D08 |

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

Opening, moving, resizing, pinning, minimizing or closing ordinary windows does not automatically pause, resume or change simulation speed. Apply the confirmed normal-UI/manual-pause rules in Section 9.1. Critical incidents independently trigger the pause in Section 7.2, including while a planner is open. Pause-menu behaviour is confirmed by UI-D36; focus-loss/return behaviour is confirmed under UI-D08 with an independent configurable pause reason.

### 3.3 Confirmed HUD and bottom navigation — UI-D06 / UI-D41

UI-D41 refines UI-D06 into the final HUD composition.

Use:

- **upper-left:** Menu, player-company identity, current cash and compact period result;
- **upper-right:** global Search and Layers/map-view controls;
- **bottom-left:** distinct + Build / + Stavět action;
- **bottom-centre:** one grouped management cluster: Operations, Business, Assets | Company, World;
- **bottom-right:** event/decision indicator, game date/time, pause and speed.

The functional wireframe and final navigation taxonomy are owned by [UI_NAVIGATION.md](UI_NAVIGATION.md).

Do not put company/cash/search/layers back into the bottom bar. Controlled subsidiaries remain AI-managed under UI-D39, so there is no subsidiary direct-control selector.

The bottom bar opens floating windows/catalogues rather than becoming a large dashboard. Build remains visually distinct because it enters a world-placement/construction workflow.

### 3.4 Confirmed compact money presentation — UI-D34

The game still has one accounting unit named `money`. For compact player-facing amounts, use one dedicated **neutral coin/token icon** instead of repeating the word “money” beside every number.

Examples are presentation patterns, not a locked icon asset:

> [money icon] 42,000  
> [money icon] −690

Apply the icon consistently in places such as:

- bottom-bar cash;
- price and fee fields;
- offer/order summaries;
- finance cards/tables;
- construction/acquisition confirmations;
- tariffs and ticket prices;
- licence/application fees.

In dense tables, the icon can appear once in the amount-column header instead of in every cell when the unit is unambiguous.

The icon is **not a real-world currency symbol**. Do not use $, €, Kč or a changing historical currency glyph. It does not change the canonical data/unit name, fixed-point/integer accounting, localization rules or absence of foreign exchange.

Use the textual unit name `money` when clarity requires it, including:

- tooltip/focus explanation of the icon;
- accessibility/screen-reader labels;
- text-only exports/logs or other surfaces that cannot render the icon;
- explanatory prose where the unit would otherwise be ambiguous.

A screen reader should receive an amount such as “42,000 money”, not only “42,000”. The icon cannot be the sole indication of positive/negative, cost/revenue or affordability state; retain signs, wording and semantic status cues. Its exact drawing, stroke/fill and pixel dimensions remain part of the shared icon-system visual design.

## 4. Navigation and final information architecture

UI-D41 in [UI_NAVIGATION.md](UI_NAVIGATION.md) owns the final taxonomy.

Top-level management groups are:

- **Operations / Provoz**
- **Business / Obchod**
- **Assets / Majetek**
- **Company / Firma**
- **World / Svět**

Build / Stavět remains a distinct action rather than another management list.

Global Search and Map Layers are upper-right HUD tools, not World menu items.

The same object can be reached from several contexts without duplication. Contextual links continue to follow UI-D09.

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

These direct object links are part of V1 interaction. They do **not** make the future deep nested-glossary/tooltip pattern in GAME_DESIGN Section 1.1 mandatory now. Entity navigation and contextual explanations are distinct interactions; ordinary hover/focus tooltips follow confirmed Section 2.1.

### 4.2 Confirmed player-facing vocabulary

[UI_GLOSSARY.md](UI_GLOSSARY.md) owns the canonical CZ/EN player-facing terminology.

Core names include:

| Domain identity | Czech | English |
|---|---|---|
| Line | Linka | Line |
| Service Pattern | Varianta linky | Service pattern |
| Trip | Jízda | Trip |
| Shipment | Zásilka | Shipment |
| CargoLot | Část zásilky | Cargo portion |
| TransportPlan | Přepravní plán | Transport plan |
| CapacityOrder | Objednávka kapacity | Capacity order |

Use natural contextual grammar where useful, but do not collapse distinct domain identities. Stable English data IDs do not change and raw code type names are not normal player-facing text.

## 5. Inspector contents

### 5.1 Proposed shared structure

The shared inspector is a reusable window/content pattern, not a mandatory singleton at the right edge. Use a consistent structure with object-specific content rather than identical empty tabs everywhere. This detailed template remains proposed within the confirmed global hierarchy in Section 2.1; contextual links in Section 4.1, the vehicle-specific view in Section 5.2 and the Line-specific views in Sections 6.1 and 6.4 are confirmed. UI_STATIONS defines the confirmed station-specific contents.

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

### 5.3 Confirmed external-company and competitor detail — UI-D37

[UI_EXTERNAL_COMPANIES.md](UI_EXTERNAL_COMPANIES.md) owns one adaptive company detail with Overview, Operation and network, Products and services, Our agreements, Relationship and history, and Ownership. A company may simultaneously be a competitor, customer, supplier, carrier, manufacturer or facility provider without separate identities or mutually exclusive screens. Known assets are inspected within Operation and network; irrelevant cards need not become empty dashboards.

UI-D27's complete bilateral agreement list remains directly accessible. Offers lead to their existing fleet, maintenance, construction, procurement, commercial or External Transport Order workflows. Public services, observations, contractual/commercial knowledge and estimates retain their source, date and permission boundaries. Old sightings are not current fleet totals or live tracking, and linked competitor details cannot reveal private duties, bids, accounts or unrelated agreements.

Known ownership, distributions and company history are inspectable, including retained identity after acquisition or dissolution. UI-D37 does not decide acquisition transaction mechanics, create control rights from a minority holding, or finalize the separate world-news workflow. Those remain tracked in [TODO.md](TODO.md).

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
| Vehicles / Vozidla | Vehicle/consist requirements, assignment criteria or pinned assets, expected fleet demand, real availability/delivery and conflicting commitments; expose the planned/active roster under UI-D13 in Section 6.4 as soon as capacity is planned, including before launch |
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

Do not force every track/platform to be selected. Preserve automatic compatible routing, the distinction between requested times, accepted slot windows, planned midpoints and physical occupancy, and the existing Capacity Order/Auto-renew workflow. All planning remains available in pause under Section 9.1; card navigation and saving a design are not time-control or physical-work commands. Binding commitments during pause follow GAME_DESIGN Section 3.4.1: explicit validated commitment is allowed at the paused timestamp, while time-driven execution remains stopped.

### 6.2 Confirmed commercial and Shipment presentation — UI-D17 / UI-D23

The detailed commercial workspace is owned by [UI_COMMERCIAL.md](UI_COMMERCIAL.md) under UI-D17. It keeps Market, Opportunities, Offers and Contracts distinct; Market can automatically project a selected commodity's local surplus/deficit and reference prices onto the main map; public tenders use concrete compliant service proposals with sealed rival bids and transparent published scoring; persistent non-linear drafts remain separate from submission; and accepted commercial obligations link to real Transport Plans, Lines, Trips, facilities and Shipments.

The detailed Shipment view is owned by [UI_SHIPMENTS.md](UI_SHIPMENTS.md) under UI-D23. One Shipment remains one commercial consignment while its CargoLots can have different physical locations, handling states and future allocations. The directly accessible parts list distinguishes physical custody from reservations, and replanning one portion cannot rewrite completed handling or unrelated portions.

These focused specifications preserve GAME_DESIGN Sections 11.0.1 and 11.9: no duplicate cargo ledger, no teleporting through reservation edits, no hidden profitability-priority replacement and no second Contract Planner.

### 6.3 Confirmed construction workflow — UI-D18

[UI_CONSTRUCTION.md](UI_CONSTRUCTION.md) owns the confirmed map-first construction presentation. Build opens compact tools over the world; drawing creates an uncommitted ghost; Prepare project opens independently editable cards; incomplete project plans persist across sessions; and Start project is a separate freshly validated commitment.

The same project workspace continues after launch with physical stage/progress, current and next work, supported completion estimates, costs and linked blockers. Explicitly acquired land, accepted contractor/supplier agreements and purchased materials remain real commitments even while the project plan itself is unstarted.

This presentation does not change GAME_DESIGN Sections 19–26: construction remains time/material/contractor constrained, free-form rather than grid based, and physically staged. A draft is not usable infrastructure, a saved corridor is not automatically reserved land and completion is never instantaneous.

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
| Vehicles | Planned and currently deployed vehicles in the directly accessible roster below, plus upcoming coverage/shortages; a count or requirements editor alone is insufficient, and inclusion never implies permanent attachment to this Line |
| Staff and facilities | Qualified staffing and operating-base/service coverage, with actual maintenance, handling, energy or supply bottlenecks |
| Rights and capacity | Valid access/slots, missing or at-risk commitments and relevant agreement expiry/renewal; open the coordinated UI-D26 Capacity Order/agreement view in [UI_CAPACITY_ACCESS.md](UI_CAPACITY_ACCESS.md) |
| Economics and obligations | Result and utilization for a visibly selected period, plus material contractual risks; drill into actual revenues, costs and commitments |

Cards have a heading, a few useful facts and an issue indicator when needed. They reflow from columns in wider windows to a readable vertical arrangement in narrower windows; do not replace them with oversized decorative tiles or hide essential controls at larger UI scales.

Metrics use the existing simulation/reporting data and the selected Line/Pattern scope. Label game-time periods and distinguish actual results from forecasts. Explain the basis of utilization and financial totals on inspection; do not mix onboard load, reserved capacity and a period average, or double-count shared assets, Trips or costs across cards/variants. Missing observations show insufficient data, not invented zeroes or a new hidden scoring system. No new accounting model or fixed profitability threshold is approved here.

#### Confirmed planned and active vehicle roster — UI-D13

**The Line must show a list of its planned and actively deployed vehicles as soon as its capacity is planned.** Explicitly requested on 2026-09-30. Expose a compact Vehicles on this Line list directly in the Line overview, expandable to the full roster and also reachable through the Vehicles card. Do not substitute only a vehicle count, a list of Trips or a requirements editor. The roster is available in an unlaunched plan as well as during operation; it does not wait for the first departure or final confirmation of every infrastructure slot.

Use the existing fleet-capacity plan, duty requirements and actual assignments as the source. Before enough information exists to calculate them, show the missing inputs rather than hiding the feature or inventing vehicles. Once requirements or specific assignments exist, show them immediately even if other cards remain incomplete.

| Entry | What it represents |
|---|---|
| Planned vehicle | A known physical vehicle proposed, pinned or assigned to future work on this Line; distinguish a draft proposal, a candidate and an actual reservation rather than calling all three secured |
| Actively deployed vehicle | A concrete vehicle currently executing work for this Line; state whether it is preparing/repositioning, boarding/loading, running or turning around, with the relevant assignment |
| Requirement without a concrete vehicle | A separately labelled duty/type/capacity requirement awaiting serial-number assignment, or a real coverage shortage. It is not an invented asset and is not counted among concrete vehicles |

Rows expose the vehicle's name/identifier and model, its planned/current relationship to the Line, relevant variant, dated Trip or duty/time interval, current task/location when known, and any assignment or readiness problem. Show applicable capacity with units and context. Vehicle names and available Trip/duty/facility references open their exact details under Section 4.1. If no concrete Trip or vehicle yet exists, link to the real Pattern/requirement instead of fabricating a target. Exact column widths and compact/expanded presentation remain layout work.

Provide All, Planned and Active views, with unassigned requirements/coverage gaps visible alongside the roster. For a pure draft, no vehicle is labelled actively deployed on that draft merely because it is currently working elsewhere. A real vehicle may have a current and a future assignment here; present one identifiable asset row with inspectable assignments rather than inflate the unique-vehicle count. Keep Line/variant, date or planning horizon, and current-versus-future-version scope explicit. Past-only assignments belong in accessible history rather than appearing as current deployment.

GAME_DESIGN Section 32.6 retains ownership of fleet assignment, duties and preparation timing. Criteria-based planning may reserve compatible time/capability for confirmed work before selecting serial-number vehicles. Show that coverage separately from "not yet assigned" and from a genuine shortage; delayed serial selection alone is not a new blocker. Display known pinned/assigned IDs immediately and show identifiable candidates only as candidates. Neither a capacity estimate nor a purchased track/station slot supplies a physical vehicle. Listing a candidate must not pin, reserve, purchase, move or permanently attach it. An unlaunched draft remains nonbinding under Section 6.1, while separately accepted commitments remain binding.

For trains, distinguish a planned consist requirement from the actual assembled consist, with access to its known locomotives and wagons. Label whether a count refers to consists, physical assets or duties; never add locomotive capacity to coach/wagon capacity or double-count a train and its components. A vehicle shared across Lines/variants remains one physical asset with time-specific duties in the same ledger, not another free vehicle in each roster.

Update the roster from actual assignment changes: preparation, departure, completion, substitution, breakdown, maintenance, delivery delay, reassignment and relevant plan edits. Explain uncovered work and keep the replacement and original assignment history traceable. Preserve selection and scroll position during refresh. Restored drafts/assignments must rebuild the same view after save/load, revalidating stale availability without creating reservations or Trips. Opening or filtering this list does not change simulation time, and the view remains usable during manual or critical-event pause.

#### Running Trips and upcoming departures

Provide a compact expandable Running and upcoming Trips list directly from the overview, without requiring the player to edit the timetable. Each row identifies the concrete Trip, direction/destination, current state and useful timing: planned time versus actual/estimated departure or arrival and delay. Name which event a delay refers to. Assigned vehicle/consist and station references are separate contextual links when available; opening the row opens that exact Trip using the confirmed UI-D25 detail in [UI_TRIPS.md](UI_TRIPS.md).

All Trips opens the full dated list with problem/status filters. Keep cancelled Trips inspectable with their cancellation reason and history; do not remove them from the player's account of what happened. Preserve selection and scroll position during live refresh. Display the service date for cross-midnight journeys and enough identity to distinguish different Trips sharing a departure time.

Demand-driven services show their real condition, such as Waiting for cargo: 32 of the required 40 t, and any applicable latest-departure limit. This is illustrative, not a fixed load threshold. Do not invent a scheduled time or a guaranteed estimate when it is unknown. Before a concrete Trip exists, identify the item as a service/departure condition and link to the relevant Pattern, not a fabricated Trip. A cargo-ready quantity is not automatically already loaded; preserve the existing readiness/custody distinctions.

#### Variants and scope

Use All variants / a specific variant inside the same Line window. All variants summarizes actual operation across the Line; selecting a Pattern scopes the overview, cards, vehicle roster, Trip list and results to it. Always show the current scope and distinguish common settings from mixed values. Opening one variant cannot silently edit or apply a setting to every other variant.

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

### 7.1 Confirmed event/problem presentation — UI-D24

Use the same problem model in planners, inspectors, lists and the event area:

**What happened → why → operational/commercial impact → available action.**

Specific objects mentioned in these explanations must be directly clickable under confirmed Section 4.1, regardless of the final notification layout. A generic Details button does not replace inline links to distinct referenced vehicles, facilities or Trips.

Example, illustrative rather than a fixed balancing rule:

> Departure cannot be activated: the planned train is longer than every accessible platform at this stop.
>
> Inspect platform limits · Change consist · Review another compatible stop

Separate **hard blockers**, **risks/warnings**, **information** and **completed events**. An actionable warning is not silently promoted to a blocker, and a hard physical/legal constraint cannot be bypassed by dismissing a warning.

Group repeated messages about the same incident, show its affected services and allow drill-down. Avoid one pop-up per delayed train when one closure is the cause. Keep information and routine successful automatic actions in history; surface decisions needing player authority. A manager action should show its cause and the policy/budget that authorized it.

Colours supplement icons and text, never carry status alone. Distinguish unseen/acknowledged presentation, being handled, awaiting a decision and resolved where these states exist. Critical-event automatic pause is confirmed separately in Section 7.2. The detailed event-centre layout, root-cause grouping, restrained toast behaviour, historical record and optional per-object Follow presentation are confirmed in [UI_EVENTS.md](UI_EVENTS.md) under UI-D24. Opening an ordinary event window is not itself a pause trigger.

V1 explanations use first-layer hover/focus tooltips under Section 2.1, with an accessible click-open detail for longer explanations. Keep the important problem and main cause visible; tooltips elaborate them. Deep nested tooltips are not a new V1 requirement.

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

V1 does **not** provide a per-event-type auto-pause matrix. Settings expose only the global **Auto-pause on critical incidents** toggle, default On. An optional **Informational toasts** On/Off setting controls lightweight toast presentation only; it never deletes event-centre records, changes incident severity or affects simulation. UI-D36 resolves pause-menu transitions with independent pause reasons.

Application focus is also confirmed. **Pause when game loses focus** defaults On. Focus loss adds its own pause reason without changing the remembered running speed. Regaining focus removes only that focus-loss reason: a game that was otherwise running resumes at the remembered speed, while manual, critical-event, pause-menu or load-safe pause reasons remain. If the setting is Off, focus loss/return does not alter simulation time.

## 8. Confirmed map layers and opportunity discovery — UI-D21

[UI_MAP_LAYERS.md](UI_MAP_LAYERS.md) owns the detailed layer presentation. Keep the normal world clean and expose one primary analytical layer at a time, with a legend, relevant filters and explicit Off.

Confirmed layer groups cover:

| Layer | Primary question |
|---|---|
| Lines and network | Where do services run and connect? |
| Capacity and restrictions | Where is current/planned capacity constrained or usefully free? |
| Ownership and access | Who owns an asset and what rights can the company actually use? |
| Demand and opportunities | What known jobs, unmet demand, spare-capacity matches or growth potential are worth investigating? |
| Facilities and commercial coverage | Which relevant operating, maintenance, supply, handling or branch capabilities support the selected task? |
| Construction and plans | What is proposed, under construction, completed or disrupted? |

Opportunity discovery is first-class: the map distinguishes actual discoverable jobs/tenders from evidence-backed potential such as underserved passenger flows, freight gaps, compatible return-leg capacity or seasonal/growth demand. It never fabricates customers, guarantees profit, exposes unknown/private information or treats lack of knowledge as zero demand.

Overlay values distinguish observed facts, forecasts, reservations and contractual capacity. Selecting/hovering a layer is navigation/analysis only; it does not reserve resources, submit bids, start projects or activate services. Inactive regions retain their existing macro-information boundary rather than becoming fully simulated because the player opens a layer.

## 9. Input, scale, time and state safety

Carry forward the implementation brief's existing input/save defaults rather than choosing conflicting bindings here. Any new shortcuts should be remappable and respect text-field focus. UI-D36 confirms Escape priority: cancel/leave the current transient placement/action first; protect meaningful dirty editing/drafts; otherwise open/close the pause menu. Escape does not terminate a contract or indiscriminately close every window.

### 9.1 Confirmed normal-UI and manual-pause behaviour — UI-D04

**Ordinary windows, Line planning and construction planning do not automatically stop the game. The player pauses manually when they need time to think; all planning remains available in that pause.** This decision was confirmed by the player on 2026-09-30. A critical incident can independently pause the game under Section 7.2; it is the incident, not the open planner, that triggers that pause.

- Opening, closing, minimizing, restoring, moving or resizing an ordinary management/detail/planning window does not change whether the game is running or paused, and does not change the selected speed. Entering or leaving a construction preview or Line planner follows the same rule. Closing a planner must not release a manual pause.
- While the game is running, the player can inspect ongoing operations and prepare plans at the selected simulation speed. The existing pause/time controls remain accessible while these windows are open.
- During manual pause, the camera, selection, windows and planning tools remain usable. The player can inspect information, draft track/building layouts, configure Line/Pattern proposals, prepare orders and review feasibility/cost previews. Pausing must not turn those editors into read-only screens or require running time merely to edit a plan.
- The shared simulation clock does not advance during pause. Vehicle movement, physical construction, loading/unloading, maintenance/repairs and all other time-driven work remain stopped. Production, cargo ageing, staff rest, research, periodic finance, contract deadlines and AI operation cannot continue on a separate background clock. Presentation/UI response may still use real time without creating simulated progress.
- Physical work continues only after simulation time resumes, from the paused state. Real time spent planning in pause is not accumulated as a simulation catch-up budget. Opening or closing a window cannot cause a catch-up jump.
- Planning is not commitment. A draft or ghost remains free of operating/commercial side effects in either time state; saving a Line draft under Section 6.1 changes stored planning data only. Neither unpausing nor closing the planner silently accepts it, books capacity or places a purchase/construction order.
- **Binding commands are allowed during pause.** After explicit confirmation and normal revalidation, a purchase/order/agreement/application/project launch or other binding command commits once at the current game timestamp. Immediate ledger/reservation/ownership effects defined by that transaction may occur, but all time-driven processing and physical work make zero progress until simulation time resumes. Non-immediate counterparty responses stay pending. Pause never creates free work or bypasses availability, permissions, capacity or consequences. GAME_DESIGN Section 3.4.1 owns the canonical rule.

Show the actual pause/running state and selected speed clearly. Continue to use the existing game clock/calendar, including its supported speed choices and 14-day months; do not use a Gregorian date picker for game dates. The existing rule that no simulation advances during incomplete loading remains unchanged.

Application-focus loss/return is confirmed under UI-D08: default pause-on-focus-loss uses an independent pause reason and removes only that reason on return; the player can disable this behaviour in Game settings. Precise pause-menu transitions are confirmed by UI-D36. Critical-event auto-pause is confirmed in Section 7.2; do not invent unrelated pause/resume triggers.

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
| UI-A21 | UI-D13, roster from capacity planning onwards | Plan capacity in an unlaunched Line with other cards incomplete and verify a directly accessible vehicle list, not just counts or Trips. Known planned/pinned IDs appear immediately; criteria-based duty requirements and missing coverage are separately labelled without fabricated IDs or early mandatory assignment. Test available candidates versus reservations, purchased infrastructure slots without fleet, plan save/load and paused editing; viewing the list does not reserve, dispatch or activate anything |
| UI-A22 | UI-D13, active roster and assignment continuity | Test planned-to-preparing/running transitions, multiple dated assignments for one asset, substitution, failure, maintenance and reassignment. Verify exact vehicle/Trip/duty links, actual task/location, clear date/variant/current-versus-future scope, and unchanged selection on refresh. Shared vehicles and train/consist components are not double-counted; unassigned-but-covered duties differ from shortages; draft candidates never appear actively deployed on the draft. Save/load preserves assignments and reconstructs the view without new commitments; verify CZ/EN and enlarged UI |
| UI-A23 | UI-D15, progressive information without hidden essentials | Inspect representative vehicle, Line, station, finance and confirmation views. Primary state, scope/units, blockers, important costs and necessary actions remain visible/discoverable; supplementary definitions and breakdowns are in concise tooltips with a route to details. Required rosters and station/Line lists are not reduced to hover-only content. Verify incomplete, critical, estimated, unknown and stale states without having to hunt for warnings |
| UI-A24 | UI-D15, tooltip access and consistent components | Test hover, keyboard focus/help, disabled-action explanations, linked tooltip content, dismissal, moving/resizing windows and enlarged CZ/EN text. Explanations remain readable/reachable and agree with current structured source data. Hover does not issue commands, acknowledge incidents or change pause/speed. Comparable windows reuse control placement, semantic state styles and terminology; the station board retains its approved character. Do not require deep nested tooltips as a V1 gate |
| UI-A25 | UI-D24, event-centre presentation | Trigger a root-cause incident with multiple downstream effects, routine handled events, grouped informational completions and a followed-object update. Verify Needs decision / In progress / Information / History routing, exact-object links, no alert storm, preserved historical snapshots, no auto-resume on acknowledge/close, and no gameplay change from Follow. Detailed scenarios remain in UI_EVENTS.md |
| UI-A26 | UI-D25, concrete Trip detail | Inspect one Trip before departure, while running, after completion and after cancellation. Verify call progression, planned/actual/estimated distinction, causal delay/recovery explanation, dynamic platform state, segment-specific passenger/freight capacity, concrete vehicle/duty links and stable historical identity. Detailed scenarios remain in UI_TRIPS.md |
| UI-A27 | UI-D26, coordinated capacity/access UI | Request a multi-owner Service Pattern capacity order, compare an alternative slot window, accept only after impact/cost review, inspect station-call rights without a dedicated-platform assumption, then reduce/release capacity with per-owner settlement. Verify company-wide agreement overview and no duplicate/implicit reservations. Detailed scenarios remain in UI_CAPACITY_ACCESS.md |
| UI-A28 | UI-D27, external-company agreements | Open a company that is simultaneously customer, infrastructure/facility provider and transport partner. Verify every player-company agreement is directly discoverable with active/future/pending/history separation, one stable identity per underlying agreement, exact links to owning workflows and no leakage of unrelated private contracts. Detailed scenarios remain in UI_EXTERNAL_COMPANIES.md |
| UI-A29 | UI-D28, City and Region world UI | Inspect a City with directional passenger/freight flows, firms, several operators, player presence and municipal agreements, then drill from a Region aggregate into its source. Verify demand source/time scope, opportunity-versus-guarantee distinction, knowledge/provenance limits, municipal agreement completeness and no double-counted regional aggregates. Detailed scenarios remain in UI_CITIES_REGIONS.md |
| UI-A30 | UI-D29, tariffs and integrated tickets | Create a company default tariff and an integrated rail/bus system with shared rates plus single, weekly and monthly products. Verify inherited/overridden values, one fare across covered transfers, 7/14-day validity, pass-versus-reservation distinction, sold-ticket version protection, real sales-channel requirements and one-payment/no-duplicate-revenue accounting. Detailed scenarios remain in UI_TARIFFS.md |
| UI-A31 | UI-D30, maintenance planning | Inspect fleet-wide planned/active maintenance, target-vs-hard-limit conflicts, inherited policy presets, dated workshop bottlenecks and own/external service alternatives. Verify real physical transfer, compatible reserve accounting, no hard-limit override and no duplicate bookings/payments after save/load. Detailed scenarios remain in UI_MAINTENANCE.md |
| UI-A32 | UI-D31, vehicle and crew duties | Inspect a cross-Line vehicle duty with deadhead/turnaround/service, an aggregate crew change, a physical transition conflict and a delay propagating into later work. Verify planned-versus-actual history, criteria-based future assignment, maintenance consistency and no named ordinary-worker micromanagement. Detailed scenarios remain in UI_DUTIES.md |
| UI-A33 | UI-D32, procurement and supplies | Follow one operating supply through on-hand/reserved/ordered/in-transit/received states, trigger projected shortage and reorder, compare supplier/transport responsibility and link downstream facility/maintenance/project impacts. Verify no phantom stock, duplicate purchase/receipt/payment or private supplier-data leak. Detailed scenarios remain in UI_PROCUREMENT.md |
| UI-A34 | UI-D33, licences/permits/market entry | Inspect home and foreign jurisdictions, activity licences, contextual permits and pending applications. Verify market entry/local presence/licence/physical access remain distinct, critical-path readiness is explainable and save/load never duplicates applications or fees. Detailed scenarios remain in UI_LICENCES_MARKETS.md |
| UI-A35 | UI-D34, money-icon presentation | Inspect bottom bar, Finance, offer/contract, procurement, construction, tariff and licence amounts in CZ/EN and enlarged UI. Compact amounts use one neutral icon consistently; tooltip/focus/accessibility/text-only representation identifies `money`; no real-world currency symbol or second currency is introduced |
| UI-A36 | UI-D35, New Game/company founding | Start a 1900 campaign with each loan/tutorial mode, inspect public world information before the first branch, establish the company through real canonical workflows and launch the first real operation. Verify no free assets/licences/customers, no forced transport archetype, tutorial ends after first functioning operation and save/load never replays founding benefits. Detailed scenarios remain in UI_NEW_GAME.md |
| UI-A37 | UI-D36, main menu/save/pause/settings | Create manual/quick/autosaves, load while running/dirty, test failed save, Esc priority and pause-menu entry from running/manual/critical pause, then change graphics/audio/game/control/interface/language settings. Verify atomic save safety, real-time autosave cadence, safe paused load and that closing the menu removes only its own pause reason. Detailed scenarios remain in UI_SYSTEM_MENU.md |
| UI-A38 | UI-D37, adaptive external-company detail | Open one company across competitor/customer/provider roles. Verify six adaptive cards, all bilateral agreements, public service and known-asset boundaries, stale-observation handling, canonical offer workflows, relationship evidence, ownership permissions and retained identity/history after acquisition or dissolution. Detailed scenarios remain in UI_EXTERNAL_COMPANIES.md |
| UI-A39 | UI-D38, technology and research | Research a technology that unlocks a workshop, track standard and object upgrade, then adopt one true company-wide system. Verify no automatic construction/retrofit/vehicle stock, later-start technology does not require pointless rediscovery, research capacity remains simple and every unlock opens its canonical owning workflow. Detailed scenarios remain in UI_TECHNOLOGY.md |
| UI-A40 | UI-D39, ownership/acquisitions/group control | Acquire a minority stake, obtain actual control, issue a Line directive, transfer a used vehicle/capital and buy/sell infrastructure with existing third-party rights. Verify the subsidiary remains AI-managed, resolves real dependencies without cheating, keeps separate ledgers, preserves physical assets/obligations and supports optional integration. Detailed scenarios remain in UI_OWNERSHIP.md |
| UI-A41 | UI-D40, World News/history | Trigger major historical/regulatory, company, infrastructure and economic changes plus routine operational events. Verify one concise news/history feed, provenance/knowledge timing, concrete player-impact links only when known, no operational-event duplication and no auto-pause from ordinary news. Detailed scenarios remain in UI_NEWS.md |
| UI-A42 | UI-D41, final HUD/navigation/search | Verify upper-left company/finance, upper-right Search/Layers, grouped bottom navigation, exact final taxonomy and search over only legitimately known objects/functions. Detailed scenarios remain in UI_NAVIGATION.md |

Station-specific evidence remains in [UI_STATIONS.md](UI_STATIONS.md), STUI-A01–STUI-A07; global UI-D15 applies there as well.

### Remaining proposed interaction scenarios

These are scenarios for evaluating the remaining proposal, not passing tests or additional approved release gates. Formal gameplay acceptance remains in V1_ACCEPTANCE_TESTS.md.

| Scenario | What the proposed UI should demonstrate |
|---|---|
| Found a company | Find the existing 1900/region/loan, office, staff and licence steps without a hidden setup screen or free assets; remain mode-neutral |
| Track split cargo | Explain where all portions are, what is ready/loaded/reserved and which connection is at risk |
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
| UI-D03 | Information density | Global concise overview, contextual supporting explanations and opened details are confirmed under UI-D15; specific vehicle and Line layouts remain under UI-D10/UI-D11/UI-D12, and unspecified screen layouts still need design | CONFIRMED global principle on 2026-09-30; exact per-screen layouts are not blanket-approved |
| UI-D04 | Normal UI and manual-pause planning | Ordinary windows, Line planning and construction previews never auto-pause/resume or change speed; manual pause retains all planning tools while time-driven simulation remains stopped, under Section 9.1 | CONFIRMED on 2026-09-30 |
| UI-D05 | Navigation and Czech terminology | Top-level groups/detailed navigation are confirmed by UI-D41 and canonical CZ/EN object labels are fixed in UI_GLOSSARY.md | CONFIRMED on 2026-09-30 |
| UI-D06 | Fixed bottom bar | Stable bottom navigation/status/time control area with the functional grouping in Section 3.3, instead of mandatory left/top strips; exact visual dimensions and secondary controls remain open | CONFIRMED on 2026-09-30 |
| UI-D07 | Detailed window interaction | Resizing, multiple views, reusable unpinned detail, content pinning, explicit new-window action, minimize/restore and remembered/recoverable layout under Section 3.2; snapping is optional and never compulsory docking | CONFIRMED on 2026-09-30 |
| UI-D08 | Critical incidents and exceptional pause/notification behaviour | Critical incidents auto-pause by default; routine delays/authorized recovery do not. Pause-menu and focus-loss pauses use independent reasons. Pause on focus loss defaults On and can be disabled. V1 has no per-event auto-pause matrix: only global critical auto-pause and optional informational-toasts toggles | CONFIRMED on 2026-09-30 |
| UI-D09 | Contextual object links | Specific object mentions in messages and other views open that exact object's detail; connected windows share identity, selection/pinning, context preservation and safe historical navigation under Section 4.1 | CONFIRMED on 2026-09-30 |
| UI-D10 | Vehicle detail and model preview | Operations-first default overview with a small correct-model preview; a static image is sufficient and live operational data remains separate, under Section 5.2 | CONFIRMED on 2026-09-30 |
| UI-D11 | Card-based Line planning and unlaunched plans | Independently editable cards instead of a wizard; persistent incomplete/future Line drafts, visible dependency-based readiness and separate explicit activation under Section 6.1 | CONFIRMED on 2026-09-30 |
| UI-D12 | Active Line detail | Same window/cards before and after launch, live operation/issues and actual Trips, explicit variant scope, period-based results and separate future changes/lifecycle actions under Section 6.4 | CONFIRMED on 2026-09-30 |
| UI-D13 | Planned and active Line vehicle list | Directly accessible roster from capacity planning onwards, including unlaunched plans; show known planned/current vehicle identities and assignments, with unassigned requirements/coverage clearly separate; follow Section 6.4 and existing fleet commitment rules | CONFIRMED on 2026-09-30 |
| UI-D14 | Station and terminal UI | Overview/cards, separate station-style arrivals/departures window and serving-Line information; embedded track/platform/stand schematic deferred, as owned by UI_STATIONS.md | CONFIRMED on 2026-09-30 |
| UI-D15 | Global minimalist and consistent UI | Clear concise overviews, supporting information in hover/focus tooltips and opened details, intuitive task grouping and shared visual/interaction components throughout the game; preserve visible critical information under Section 2.1 | CONFIRMED on 2026-09-30 |
| UI-D16 | Depot/garage/workshop UI | Operational facility overview, on-site/expected/linked vehicle lists, task cards and supported Lines; detailed rules in UI_DEPOTS.md | CONFIRMED on 2026-09-30 |
| UI-D17 | Commercial UI | Market, Opportunities, Offers and Contracts; spatial commodity intelligence, producer/buyer transport proposals, transparent public tenders with concrete service plans, persistent drafts and direct linkage from commitments to real execution; detailed rules in UI_COMMERCIAL.md | CONFIRMED on 2026-09-30; refined on 2026-10-01 |
| UI-D18 | Construction UI | Map-first ghost planning, persistent project cards, explicit launch and physical progress; detailed rules in UI_CONSTRUCTION.md | CONFIRMED on 2026-09-30 |
| UI-D19 | Finance UI | Cash/result/commitment overview, source-linked breakdowns, consistent periods and plans separated from binding/posted money; detailed rules in UI_FINANCE.md | CONFIRMED on 2026-09-30 |
| UI-D20 | Company/branches/workforce UI | Company overview, branch coverage/capacity, aggregate professions, named-manager authority, licences and company systems; detailed rules in UI_COMPANY.md | CONFIRMED on 2026-09-30 |
| UI-D21 | Map layers and opportunities | Purpose-based layers diagnose problems and reveal evidence-backed opportunities without fabricating demand or commitments; detailed rules in UI_MAP_LAYERS.md | CONFIRMED on 2026-09-30 |
| UI-D22 | Fleet/market/delivery UI | Fleet, Vehicle Market and Orders/deliveries workspace, model-to-offer distinction and physical readiness; detailed rules in UI_FLEET.md | CONFIRMED on 2026-09-30 |
| UI-D23 | Shipment detail | One Shipment with inspectable CargoLots, physical-location versus reservation distinction, compact transport chain and automated routine allocation; detailed rules in UI_SHIPMENTS.md | CONFIRMED on 2026-09-30 |
| UI-D24 | Events, incidents and notifications | One event centre with Needs decision / In progress / Information / History, stable root-cause grouping, restrained grouped toasts, historical snapshots and optional Follow notifications; UI-D08 remains authoritative for critical auto-pause | CONFIRMED on 2026-09-30 |
| UI-D25 | Concrete Trip detail | Stop/call progression, planned/actual/estimated timing, explainable delay/recovery, segment capacity, pre-departure readiness and retained completed/cancelled history; detailed rules in UI_TRIPS.md | CONFIRMED on 2026-09-30 |
| UI-D26 | Infrastructure capacity and access UI | One coordinated Service Pattern Capacity Order, explicit request/offer/accepted lifecycle, timing-impact review, multi-owner breakdown and company-wide active/future agreement overview; detailed rules in UI_CAPACITY_ACCESS.md | CONFIRMED on 2026-09-30 |
| UI-D27 | External-company bilateral agreements | Every external-company detail directly exposes all agreements between that company and the player's company, separating active/future/pending/history and linking to each canonical owning workflow; surrounding company layout is now confirmed by UI-D37 and City/Region presentation by UI-D28 | CONFIRMED on 2026-09-30 |
| UI-D28 | City and Region world UI | City detail covers population/demand, firms/industry, transport, opportunities, player presence and municipal authority/agreements; demand is directional/time-scoped, trends are inspectable and Region is an aggregation/navigation view respecting knowledge provenance; detailed rules in UI_CITIES_REGIONS.md | CONFIRMED on 2026-09-30 |
| UI-D29 | Tariffs, integrated systems and ticket products | Company/global tariff inheritance, integrated groups of Lines with shared km/zone rules, single/weekly/monthly and other scoped products, explicit sales/reservation capability, sold-product protection and effective-dated changes; detailed rules in UI_TARIFFS.md | CONFIRMED on 2026-09-30 |
| UI-D30 | Maintenance planning UI | Fleet-wide Plan/In progress/Vehicles at risk/Workshop capacity workspace, explicit preventive-target versus hard-limit distinction, inherited policy presets, own/external service comparison and future Trip/reserve conflicts; detailed rules in UI_MAINTENANCE.md | CONFIRMED on 2026-09-30 |
| UI-D31 | Vehicle and crew duties UI | Operations workspace with Vehicles/Crews/Conflicts, physical duty timeline and transition validation, planned-vs-actual execution and aggregate crew duties; detailed rules in UI_DUTIES.md | CONFIRMED on 2026-09-30 |
| UI-D32 | Procurement and supplies UI | Business workspace with Inventory/Orders/Suppliers/Reorder rules, location-specific physical stock, shortage projection, recurring supply agreements, actual delivery responsibility and supplier links; detailed rules in UI_PROCUREMENT.md | CONFIRMED on 2026-09-30 |
| UI-D33 | Licences, permits and market-entry UI | Company workspace with Markets and regions / Licences / Permits / Applications, contextual requests and critical-path readiness while keeping legal, commercial and physical access concepts distinct; detailed rules in UI_LICENCES_MARKETS.md | CONFIRMED on 2026-09-30 |
| UI-D34 | Compact money presentation | Use one dedicated neutral coin/token icon as compact UI shorthand for the single `money` accounting unit; retain textual `money` for accessibility/tooltips/text-only/ambiguous contexts and never use a real-world currency symbol | CONFIRMED on 2026-09-30 |
| UI-D35 | New Game and company founding UI | Short campaign setup followed by real in-world founding with no free branch/fleet/licence/customer or mode archetype; Full/Basics/Off tutorial is opening-only and ends after the first functioning transport operation; detailed rules in UI_NEW_GAME.md | CONFIRMED on 2026-09-30 |
| UI-D36 | Main menu, save/load, pause and settings UI | Compact main menu, campaign-organized manual/quick/autosaves, atomic save safety, safe paused load, independent pause-menu reason, Esc priority, unsaved-exit protection and Graphics/Audio/Game/Controls/Interface/Language settings; detailed rules in UI_SYSTEM_MENU.md | CONFIRMED on 2026-09-30 |
| UI-D37 | External-company and competitor detail | One adaptive company detail with six task-based cards, all UI-D27 agreements, public/known operation/assets, canonical offers, evidence-backed relationship/history and permission-aware ownership; detailed rules in UI_EXTERNAL_COMPANIES.md | CONFIRMED on 2026-09-30 |
| UI-D38 | Technology and research UI | One simple Technology workspace: established technology need not be rediscovered, research/knowledge unlocks concrete buildables/upgrades/capabilities, physical changes remain in owning systems and only genuine company-wide systems use an adoption project; detailed rules in UI_TECHNOLOGY.md | CONFIRMED on 2026-09-30 |
| UI-D39 | Ownership, acquisitions and infrastructure market UI | Separate ownership from control; controlled subsidiaries remain AI-managed while the owner has a deliberately small set of powers: broad direction, concrete owner directives, capital/asset transfers and major-company decisions. Infrastructure sale/acquisition preserves physical state and binding rights; detailed rules in UI_OWNERSHIP.md | CONFIRMED; refined on 2026-09-30 |
| UI-D40 | World News and historical events UI | One simple World News/history feed for meaningful historical, economic, infrastructure and company changes; show concrete known player impact and exact-object links; ordinary news never auto-pauses and UI-D24 remains the operational incident/decision system; detailed rules in UI_NEWS.md | CONFIRMED on 2026-09-30 |
| UI-D41 | Final navigation and global search | Upper-left company/finance HUD, upper-right Search/Layers, bottom Build + grouped Operations/Business/Assets | Company/World + Events/time controls; search navigates only to known objects/functions and never acts as a command palette; detailed rules in UI_NAVIGATION.md | CONFIRMED on 2026-09-30 |

The player's acceptance of the bottom-bar/window proposal includes updating one ordinary detail window until it is pinned, rather than opening a new window for every ordinary object click. Normal-window/planning pause behaviour is resolved under UI-D04, critical-event automatic pause under UI-D08, contextual object links under UI-D09, the compact vehicle overview under UI-D10, nonlinear persistent Line planning under UI-D11, the active Line workspace under UI-D12, the planned/active vehicle roster under UI-D13 and station presentation under UI-D14. UI-D15 now applies the minimalist information hierarchy and consistent design principles globally. UI-D16–UI-D33 are confirmed focused screen/workflow specifications, including the event centre under UI-D24, concrete Trip detail under UI-D25, coordinated capacity/access UI under UI-D26, bilateral external-company agreement visibility under UI-D27, City/Region world presentation under UI-D28, integrated tariff/ticket products under UI-D29, fleet-wide maintenance planning under UI-D30, vehicle/crew duties under UI-D31, procurement/supplies under UI-D32 and licences/market entry under UI-D33. UI-D34 is the confirmed global compact money-display rule; UI-D35 is the confirmed New Game/opening company-founding workflow; UI-D36 is the confirmed main-menu/save/pause/settings workflow; UI-D37 completes the external-company/competitor detail without deciding the separate acquisition or news workflows; UI-D38 confirms technology/research presentation without changing Sections 27–28 mechanics; UI-D39 confirms group ownership/acquisition/infrastructure-market workflows with AI-managed subsidiaries and owner directives rather than direct subsidiary control; UI-D40 confirms world-news/history presentation while UI-D24 remains the operational incident system. UI-D08 is fully resolved: UI-D36 owns pause-menu lifecycle, focus loss has an independent configurable pause reason, and V1 intentionally omits detailed per-event auto-pause overrides. Do not reopen those choices or reintroduce the superseded Line-creation wizard. Approval of these decisions does not silently approve every detail in this document.
