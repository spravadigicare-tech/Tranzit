# Tranzit — Construction planning and project UI

> **Status: CONFIRMED UI DIRECTION — UI-D18, 2026-09-30.** The player accepted map-first construction, a compact floating catalogue and tools, independently editable project cards, persistent unstarted plans, explicit project launch and a live construction-progress overview. Exact visual tokens, dimensions and secondary controls remain design work. This specification is not an implemented or tested UI.

Read with [UI_UX_DESIGN.md](UI_UX_DESIGN.md): UI-D07 governs windows, UI-D09 exact-object links, UI-D15 minimalism/tooltips, and UI-D04/UI-D08 time control. This focused document owns the now-confirmed construction presentation and elaborates the short construction proposal in its Section 6.3. [GAME_DESIGN.md](GAME_DESIGN.md), especially Sections 19–26, owns access, physical facilities, contractors, logistics, terrain, corridors and demolition. [V1_SCOPE.md](V1_SCOPE.md), Section 2, owns the release boundary. [CONTRACT_CANCELLATION.md](CONTRACT_CANCELLATION.md) governs applicable agreement settlement, not a universal construction refund formula.

## 1. Catalogue and map tools

**Build / Stavět** on the fixed bottom bar opens a compact movable catalogue. Group available items by the player's task: rail infrastructure, passenger/freight facilities and appropriate operating, parking, maintenance and road-access infrastructure. Show relevant technology/access limitations without flooding the catalogue with unrelated future modes. V1 remains rail and road; this UI does not add motorways, unrestricted urban-road redesign, water, tram, trolleybus or metro construction.

Selecting an item activates placement on the main world map and exposes its parameters in a small floating tool window. Keep bottom navigation and time controls accessible. Use the existing window/input system: interacting with a control must not place track or pan the map behind it.

For linear infrastructure, keep type/standard, track count where applicable, available electrification, proposed length, estimated cost and the main geometric or permission problem visible. Present a design-speed/standard setting as a requirement constrained by actual geometry and technology, not a slider that makes any curve support that speed. For buildings/modules, show the selected item, footprint/orientation, required connection and relevant placement constraints.

Put supporting grade/radius values, earthworks, material breakdown and cost causes in hover/focus tooltips or expanded details. A geometry violation or material permission/cost warning remains visible; do not hide the only reason a proposal is invalid in a tooltip. Keep estimates, unknown inputs and actual commitments distinguishable.

Placement uses free-form/spline geometry, freely oriented facilities and valid physical connection snapping, not a world grid. Terrain changes are project earthworks, not a free standalone terrain brush. Existing rail connections require their normal ownership/access agreement. A preview does not install electrification or create a working power supply.

## 2. Preview and durable project plan

While drawing/editing, the proposed route or building is a **ghost preview**, not usable infrastructure. The player can change control points, orientation, modules or uncommitted sections without executing demolition or paying construction costs merely for editing. Protect meaningful unsaved work using the shared window rules.

**Prepare project / Připravit projekt** opens the project overview with cards. It does not accept a contractor quote, reserve land, purchase materials, start earthworks or close operating infrastructure. This is navigation into a persistent planning workspace, not the first binding step of a wizard.

Provide **Save plan / Uložit plán** separately from **Start project / Zahájit projekt**. An incomplete plan can be saved and revisited indefinitely, even when funds, land, permissions, materials or a contractor are missing. Persist its stable identity, proposed geometry, settings, dependencies and working assumptions in the campaign save. It survives closing all its windows and loading the campaign in a later session.

Expose saved plans in the existing construction-project list, with clear plan-versus-started/completed status and direct access from the catalogue or Assets. The exact project-list layout is not fixed here. An optional target start date is only a planning target: passing it, completing all cards, loading a save or unpausing never starts a draft automatically. An unstarted idea cannot generate missed-construction incidents merely because its inputs are incomplete.

A drawn corridor is not a reserved corridor. Merely displaying/saving it does not stop city development, exclude competitors, change terrain or consume capacity. Acquiring/reserving a real wider corridor under GAME_DESIGN Section 24 is a separate explicit action with the existing rights and costs.

## 3. Independently editable cards

Use the same card groups before and after launch. Each collapsed card has a short summary, a meaningful readiness/status indication and a main issue when relevant. Open them in any order, save partially completed work and return later. Missing prerequisites can prevent calculation or launch, not access to another card.

| Card | Planning content and status |
|---|---|
| Route and objects / Trasa a objekty | Proposed geometry, sections, structures, modules, physical connections, earthworks and compatibility |
| Land and permissions / Pozemky a povolení | Required corridors/sites, ownership or reserved rights, infrastructure connection agreements, regulated/protected structures and approval state |
| Materials / Materiál | Required quantities with units, logistics responsibility, actual stock, ordered/on-route deliveries, future needs and temporary site storage; accepted purchases/suppliers can be inspected through UI-D32 without duplicating the project material ledger |
| Contractors / Dodavatelé | Capable contractors or an available owned construction division, offers, real work capacity, specialization, work windows and accepted commitments |
| Operating impact / Dopad na provoz | Affected routes/facilities, closures, reduced capacity, dependent Lines/Trips/contracts, diversion options and applicable mitigation packages |
| Cost and schedule / Cena a harmonogram | Estimated total and remaining cost, amounts already spent/committed, further payments, proposed stages, target dates and supported completion estimates |

Show a compact overall readiness summary, not a percentage of completed fields. Distinguish missing input, an unresolved blocker, a pending dependency, stale/unknown evaluation and verified readiness for the displayed scope/date. Changing geometry retains other inputs while invalidating affected cost, material, access or timing estimates; it must not silently reset the whole plan.

Readiness uses the actual staged construction rules. Do not require every later-stage material to be physically on site before any work can begin if the valid delivery/stage plan permits later supply. Conversely, a forecast delivery or unsigned contractor quote is not secured capacity. Show what the launch/current stage needs, what later stages depend on and where the schedule remains conditional. Do not invent unrestricted partial-launch mechanics or bypass a required permit by hiding it in another card.

Support the existing logistics choices: contractor-supplied construction, player-supplied materials or split responsibility. Delivered purchases, own transport and hired transport use the existing procurement and External Transport Order systems, not a new construction-only marketplace. Contractors' temporary access/storage infrastructure follows the existing automated project rules rather than mandatory individual placement of every site hut.

## 4. Real preparations and explicit launch

The player may acquire land, secure permissions, accept supplier/contractor agreements or arrange deliveries while the construction plan remains unstarted, through the existing explicit workflows. These are real transactions, not draft edits. Keep their references, cost, validity and status visible in the relevant cards.

Saving/deleting a plan does not refund land, cancel orders or erase accepted commitments. A quote or supplier preference stays nonbinding until actually accepted. Distinguish acquired rights from merely requested rights and actual inventory from ordered or forecast stock.

**Start project** opens a current scope/readiness and consequence review. Show the project/version, intended work and timing, what is already secured, newly accepted agreements/orders, immediate charges, later committed payments, remaining estimates and material operational effects. Revalidate against current geometry, rights, permits, funds/budget, contractor capacity, logistics and affected operation before committing. Hard blockers prevent launch, not saving the plan. No hidden bundle purchase is authorized just because a card is green.

Starting transitions the plan to an executable construction project and accepts only the actions disclosed in that review. Do not charge or reserve already purchased resources a second time. Failed validation or repeated submissions from several windows must not create duplicate projects, orders or postings. A real scheduled start or contractor work window still governs physical work; launch is not instantaneous completion.

The contract terms and existing capacities remain authoritative. Paying for contractor priority cannot create nonexistent workers/equipment or displace protected work without permission. For reconstruction, show reduced capacity and closures, including consequences for third-party commitments. Compare applicable mitigation choices with their real costs and remaining disruption; do not treat them as free capacity.

## 5. Running project overview

Retain the same floating project window/cards after launch. Replace draft-readiness emphasis with **progress, current/next stage, expected completion and the main problem**. Keep project lifecycle, a temporary operating blockage and readiness of a proposed later change separate.

Illustrative display only:

> New railway section · Under construction
>
> Completed work: 42% · Current stage: earthworks · Next: bridge works
>
> Work delayed: 280 t of ballast are still required for the affected stage.

Values come from actual project/work records. A percentage represents measured completed work using an inspectable basis, not spent money, elapsed time or an invented animation. Use stage/section progress when a reliable aggregate is unavailable. An unknown completion date stays unknown; estimates expose dependencies and assumptions.

Long projects progress along their physical route under GAME_DESIGN Section 21.3. The overview links completed, in-progress and future work to its actual site. A partly built bridge or track does not become usable because an overall percentage passed a threshold; operational availability comes from real completion/connectivity/commissioning conditions in the simulation. Planned facilities remain conditional dependencies in Line readiness until actually usable.

Specific site, supplier, delivery, material item, facility, Line, Trip and agreement references use UI-D09 where an inspectable object exists. A generic material name opens the relevant supply breakdown; it must not guess one delivery when several exist. Distinguish problems handled by the contractor/authorized manager from decisions requiring the player. Keep counts and financial totals scoped so the same delivery or commitment is not counted again through another window.

## 6. Changes, cancellation and continuity

Editing a started project prepares an explicit change proposal; it cannot overwrite completed work, spent resources or accepted contracts. Show changed scope, readiness, costs, schedule and operating impact before accepting permitted changes. Moving a preview control point cannot relocate a built track, vehicle, load or work site.

Keep **discard unsaved edits**, **delete uncommitted plan**, **change active project**, and any supported **stop/cancel works** action distinct. Cancellation of accepted work follows its actual contract and site obligations. Show outstanding charges, prepaid settlement, retained assets/materials, physical cleanup and affected services where applicable. Do not blindly use the rail-slot cancellation formula for an entire construction contract. Completed infrastructure is removed only through the existing paid/permitted demolition or redevelopment workflow.

Saving and restoring preserve the plan/project link, geometry versions, actual phases, supplier commitments, deliveries, inventories, expenses and history. Reconstruct views from those identities without re-issuing orders. Geometry stored as UI preferences is not authoritative project state.

Opening the catalogue, editing, saving or closing ordinary construction windows does not pause/resume or change speed. Camera, previews and cards work during manual and critical-event pause; time-driven construction, transport and billing do not progress. Resuming never catches up paused wall time or auto-accepts a draft. This UI decision does not independently settle the still-open general processing policy for binding commands submitted while paused.

Use relevant-change invalidation and cached estimates rather than full-network recalculation for every dormant plan each frame. Unknown or stale quotes/readiness cannot authorize launch. Draft display or an off-screen project does not unlock regions or alter simulation detail/physical rules.

## 7. Acceptance evidence to collect

These are required UI scenarios to verify when implemented, not passing game tests. Read with [V1_ACCEPTANCE_TESTS.md](V1_ACCEPTANCE_TESTS.md).

| ID | Required scenario |
|---|---|
| CONUI-A01 | Open the floating catalogue/tools, place and edit rail and road-facility previews, and discard an uncommitted ghost. Bottom controls remain accessible, UI input never places through a window, and no terrain, inventory, money, corridor reservation or live capacity changes from preview alone. |
| CONUI-A02 | Edit project cards out of order, save with missing funds/permissions/contractor, close all windows, save/load and reopen the same plan. Partial contents and identity survive; time, a target date and all-green readiness do not launch it. |
| CONUI-A03 | Explicitly acquire a corridor and order materials while leaving the project unstarted. Distinguish those binding actions from a free draft; deleting/revising the draft does not cancel/refund purchases, and real corridor rights alone affect competing development. |
| CONUI-A04 | Revalidate a stale plan after a changed site, permit, quote or contractor commitment. Verify launch blockers and staged delivery dependencies; later supply need not all be on site at launch, but nonexistent capacity, invalid access and missing current-stage material cannot be hidden. |
| CONUI-A05 | Launch after scope/cost/impact review, including contractor-supplied and player-supplied logistics. Duplicate or parallel confirmations do not double-charge or recreate projects/orders; prior purchases are not bought twice. |
| CONUI-A06 | Observe a long staged project, material shortage, contractor delay and reconstruction with mitigation. Progress follows actual work/site state, estimates identify uncertainty, and no unfinished infrastructure becomes operational from a UI percentage. Follow site/delivery/Line links and verify reduced capacity affects the same real network. |
| CONUI-A07 | Prepare an active-project change or permitted cancellation, then save/load. Completed work, costs, physical materials and contractual liabilities persist; a draft edit cannot relocate them, erase obligations or apply a slot-specific cancellation fee to construction works. |
| CONUI-A08 | Verify running, manual-pause and critical-pause editing in CZ/EN at 1080p/enlarged scale. Tooltips explain secondary values while blockers/cost disclosures remain visible. Restoring windows and resuming time cause no hidden orders, catch-up, duplicated progress or region unlock. |

## 8. Decision record

| ID | Decision | Status |
|---|---|---|
| UI-D18 | Map-first construction with compact floating catalogue/tools; non-linear project cards and persistent unstarted plans; separate acquisition/launch commitments; same-window physical progress and issue overview after launch | CONFIRMED on 2026-09-30 |

This decision does not add modes, independent terraforming, unlimited contractors, free demolition, new procurement engines or automatic launch of completed drafts. The functional card groups and interaction are confirmed; exact pixel styling and cost/progress balancing are not fixed by the illustrative values.
