# Tranzit — Fleet, vehicle marketplace and delivery UI

> **Status: CONFIRMED UI DIRECTION — UI-D22, 2026-09-30.** The player accepted one vehicle workspace with Fleet, Vehicle Market and Orders and deliveries, compact physical-asset lists, model-to-offer comparison, contextual acquisition from missing capacity and explicit delivery/readiness information. Exact dimensions, column widths and localized labels remain visual-design work. This specification is not an implemented or tested UI.

Read with [UI_UX_DESIGN.md](UI_UX_DESIGN.md): UI-D07 governs floating windows, UI-D09 exact-object links, UI-D10 the small static vehicle preview, UI-D13 planned/active Line rosters and UI-D15 minimalism/tooltips. [GAME_DESIGN.md](GAME_DESIGN.md), Sections 15–18, 30.1 and 32.6, owns acquisition, enduring model availability, maintenance, physical delivery, the shared External Transport Order, duties and asset commitments. [V1_SCOPE.md](V1_SCOPE.md) retains first-release modes and historical availability. [UI_FINANCE.md](UI_FINANCE.md) and [CONTRACT_CANCELLATION.md](CONTRACT_CANCELLATION.md) govern relevant presentation/settlement boundaries. This document specifies UI, not a second vehicle market or new allocation rules.

## 1. One vehicle workspace

**Assets → Vehicles / Majetek → Vozidla** opens a shared movable/resizable window with three views: **Fleet / Flotila**, **Vehicle Market / Trh vozidel**, and **Orders and deliveries / Objednávky a dodání**. Reuse/focus existing matching views, preserve the source planner and apply common pinning, minimize/restore and navigation behaviour.

The views answer respectively: what assets the company controls, what can be acquired, and what still has to happen before ordered assets can enter operation. An order, catalogue model and physical vehicle are different identities, not three copies of a fleet asset. Fleet is not the Line-specific vehicle roster; both are views of the same assets and assignments.

Use compact lists, restrained small previews and task-based filters. Keep actual status, important issues, units, time scope and relevant actions visible; use hover/focus explanations for supporting parameters and full details for histories/settings. Navigation does not move the camera, change pause/speed or issue a business command.

## 2. Fleet: actual vehicles and time-specific availability

The Fleet view lists concrete assets the company owns or currently controls under an applicable lease/rental. A purchased vehicle still at the seller can appear here, clearly marked as awaiting delivery and not yet available for normal dispatch. An unbuilt factory order or an unassigned duty requirement is not an existing vehicle row.

| Row information | Meaning |
|---|---|
| Small model preview, name and model | Recognition plus the exact asset identity; the static thumbnail is not a live location/condition view |
| Status and current activity | What the vehicle is actually doing, including idle, preparation, operation, repair or pending delivery where applicable |
| Physical location | Actual facility, route or other known location, separate from preferred depot or intended receiving point |
| Current/next use | Relevant dated Trip/duty and Line, with planned or committed assignment status |
| Availability | Feasibility for a stated date/time window and requirement, not merely whether the asset is moving now |
| Main issue | A meaningful defect, service deadline, delivery dependency or assignment conflict |

Search/filter/sort by relevant mode/type, use, condition, location/base, ownership/control and availability. Provide quick access to idle assets, vehicles under repair and upcoming maintenance. Keep idle and available distinct. Preserve filters, selection and scroll during updates; do not move a row out from under a pending action.

Availability includes existing duties, preparation/repositioning, energy, maintenance and reserve obligations under the canonical fleet rules. Being company-owned, parked or serviceable does not alone make a vehicle free for a new duty. Show the relevant scope and explain the conflicting use; unknown feasibility is not an available badge. Read-only filtering cannot reserve or release an asset.

Clicking the vehicle opens its existing operations-first detail. Line, Trip, depot and maintenance references are independent exact-object links. Reuse the existing service-policy and disposal workflows rather than inventing new maintenance, sale or scrapping rules here. Respect rights on leased assets.

For rail, distinguish locomotives, wagons and actual consists. Grouping may expose a consist and its components, but unique physical-asset counts and capacity must not count both as additional assets. A locomotive's preview or nominal power is not the train's cargo capacity. Shared assets remain time-assigned resources, not permanently duplicated vehicles on each Line.

## 3. Vehicle Market: models and concrete offers

### 3.1 Model discovery

Present a searchable/filterable model catalogue with small static previews, role, applicable capacity, maximum speed, traction/energy and a concise summary of actual offers. Secondary dimensions, load limits, service capability and operating-cost assumptions belong in tooltip/detail. A model's maximum speed is not promised route speed; estimated running costs identify their basis.

Opening a model compares available acquisition sources together:

| Source | Information needed to compare |
|---|---|
| Manufacturer order / Objednávka z výroby | Unit price, allowed configuration, quantity, production estimate, first/last unit readiness and delivery |
| Dealer stock / Nové ze skladu | Actual seller/location, available units and configurations, price and collection/delivery needs |
| Used / Ojeté | Exact physical asset, price, age, condition, mileage/hours, known service history and present location |
| Lease or rental / Pronájem nebo leasing | Upfront/recurring charges, term, usage/return conditions, maintenance responsibility and actual delivery plan |

These are acquisition sources in the same marketplace, not four independent pricing or inventory systems. Offer and source filters can support direct access to a specific listing without forcing a model-selection detour every time. Model-first browsing is a useful default, not a mandatory wizard. Exact comparative layout remains visual-design work.

Sources exist only when the current era, provider and simulation support them. Do not guarantee leasing, custom configurations, heavy road delivery or dealer inventory merely because the UI can display those options. Manufacturer/dealer names follow the fictional-brand rules.

### 3.2 Identity, stock and old models

A model definition is not stock. Used listings and existing stock resolve to concrete assets; a manufacturing offer represents future production under real capacity. Show what is known and what must be checked again before acceptance. A second buyer can acquire finite stock before the player confirms; explain the changed availability rather than substituting another used vehicle silently.

Once introduced, a model remains searchable under GAME_DESIGN Section 15.11. If there is no current seller/manufacturing offer, display **No current offer / Bez aktuální nabídky**, not an artificial end-year purchase ban. Preserve actual availability, condition, compatibility and maintenance-support differences; do not fabricate stock to fill an empty results list.

## 4. Acquisition from a capacity requirement

**Find suitable vehicles / Najít vhodná vozidla** from a Line, contract or other supported planner opens this same market with the known requirements prefilled. Keep a visible context header naming the source plan, missing quantity/capability and required date. Allow inspection and removal/change of filters without modifying the source requirement itself.

Technical compatibility, delivery feasibility and readiness by the needed date are separate checks. Consider the existing production estimate, transport waiting time, transit, receiving site and necessary inspection/preparation. A technically suitable model can still arrive too late. Unknown delivery feasibility remains visible; do not mark every candidate as ready.

Returning to the planner preserves its incomplete cards and chosen context. Selecting an offer to evaluate is not a purchase or a guaranteed allocation. After a confirmed acquisition, expose the actual order as a dependency; the Line remains unlaunched until explicitly activated. Do not force early serial-number assignment where criteria-based capacity planning permits selection later.

## 5. Purchase or lease review

Use independently accessible sections **Vehicle and configuration / Vozidlo a konfigurace**, **Price and terms / Cena a podmínky**, and **Delivery and receipt / Dodání a převzetí**. Preserve partial inputs during comparison and navigation; do not reintroduce a mandatory Next/Back flow.

Before acceptance, show the exact offer or physical assets, supported configuration, quantity, seller, amount payable now, later committed payments, important conditions, production timing, receiving point and delivery status. Money uses the literal `money` token and the shared game-time rate/calendar rules. Unknown transport cost is not zero, and an indicative total is not a locked quote.

Distinguish included delivery, separately quoted delivery, an accepted transport order and delivery not yet arranged. Accepting an estimate does not silently buy transport or promise arrival. Acquisition and transport are separate agreements even when reviewed together; any accepted bundle must disclose both commitments and avoid charging an included service twice.

The player may buy a vehicle and arrange movement later where the existing rules permit. Warn before purchase that it remains at the seller, cannot yet enter normal dispatch and may incur disclosed storage/holding charges. An unready depot or missing compatible route cannot be bypassed by choosing its name as a destination.

Revalidate stock, offer terms, quantity, ownership/control, available funds and applicable permissions at confirmation. Material changes return for review. Repeated submissions or parallel windows cannot buy the same vehicle twice, overbook production or duplicate payment. Editing or closing a purchase view does not cancel an accepted agreement.

## 6. Orders and deliveries: follow each stage

Use a compact order list with supplier/model, ordered quantity, current fulfilment status, destination, supported expected dates and the main dependency or delay. Opening an order exposes its units and related production/delivery records.

Illustrative summary only:

> Order: 5 freight wagons
>
> 2 received · 1 in transit · 2 in production
>
> Open delivery · Open received vehicles · Open linked plan

Use real ordered/fulfilled counts. In this example the three groups are disjoint; do not add overlapping ready, produced and delivered counters as if they were extra units. Orders with no completed assets link to real order/production records rather than invented serial-number vehicles. Part deliveries expose which concrete units exist and where they are.

Keep **produced**, **ownership/control obtained**, **awaiting transport**, **in transit**, **received** and **ready for operation** distinct. They are not necessarily one universal linear sequence: stock can be purchased without production waiting, and ownership transfer follows the acquisition terms. A received vehicle may still need an inspection, repair, compatible configuration or other required preparation before use. A sold order does not disappear from history, and a cancelled transport order does not erase the purchased asset.

Show the remaining cause of non-readiness, not just a generic delivery progress bar. Distinguish expected pickup from expected arrival, first from last unit of a batch, and committed transport from an unaccepted proposal. Late production or changed transport capacity updates dependent plans and estimates without rewriting past events.

**Arrange delivery / Zajistit dopravu** uses the existing delivery planning and, when a provider is needed, the single External Transport Order in GAME_DESIGN Section 30.1. Prefill the asset, origin and intended receiving point. Own collection/repositioning and rail haulage remain physical operations under existing rules. A disconnected rail route does not guarantee era-inappropriate heavy road transport; an unavailable feasible method is a real blocker.

Every acquisition method retains physical location, route/access, handling, provider capacity, time and receiving constraints. Opening a delivery in another view never clones its movement or makes a vehicle available early. Readiness in Fleet, Orders, Line rosters, depot expected arrivals and Finance must reconcile to the same authoritative identities and commitments.

## 7. Common presentation and state safety

The workspace and contextual links work during running time, manual pause and critical-event pause without changing those states. UI hover/focus response uses presentation time; physical production, delivery and preparation use the paused/shared simulation clock.

Keep important state and costs visible at the accepted 1080p baseline and enlarged Czech/English UI. Use common components, clear filter scope and accessible help; detailed technical data must not overwhelm the default overview. Do not hide a material purchase restriction or payment inside a tooltip.

Respect ownership and available information: inspecting a seller, model or leased vehicle does not reveal competitors' confidential fleet plans. Apply inherited maintenance policies through existing controls; this UI does not create a different reserve or staffing system.

Save/load restores actual orders, payments, assets, assignments, delivery state and references. Rebuild the views without resubmitting purchases, producing duplicate units or replaying transport. Stale cached availability cannot authorize a new commitment. Use bounded lists/cached reporting and relevant state changes rather than per-frame market-wide feasibility searches.

## 8. Acceptance evidence to collect

These checks complement [V1_ACCEPTANCE_TESTS.md](V1_ACCEPTANCE_TESTS.md). They are required scenarios for the confirmed direction, not passing game tests.

| ID | Required scenario |
|---|---|
| FLUI-A01 | Reach Fleet, Vehicle Market and Orders from one workspace. Inspect actual owned/leased assets, bought-at-seller assets and unbuilt orders; exact links and counts distinguish models, assets, consists and requirements. |
| FLUI-A02 | Compare an idle vehicle with upcoming work, maintenance, reserve or repositioning commitments against a genuinely usable vehicle for the same dated requirement. The view explains the distinction and changes no reservations. |
| FLUI-A03 | Compare supported manufacturer, stock, used and lease sources for a model. Test no current offer for an old introduced model, limited stock, unavailable configuration and a listing sold to another company before confirmation. No asset is fabricated or silently replaced. |
| FLUI-A04 | Open the market from an incomplete Line/contract plan, inspect and change filters, evaluate technical fit versus timely delivery, and return without losing edits or acquiring anything implicitly. A confirmed order appears as a dependency, not an automatic service launch. |
| FLUI-A05 | Confirm a purchase with included delivery, separate transport and delivery deferred. Show immediate/later charges and holding costs correctly; repeated or parallel acceptance does not double-buy or double-charge. |
| FLUI-A06 | Inspect partial production/delivery of a multi-unit order, a delay, unready receiving site and blocked physical delivery. Unit/location totals reconcile across Orders, Fleet, depots, Line rosters and Finance; received is not automatically ready. |
| FLUI-A07 | Verify actual rail haulage or valid road collection through existing systems, and a case with no era-compatible transport provider. No new delivery marketplace, teleportation or guaranteed heavy-haul fallback appears. |
| FLUI-A08 | Use the workspace in CZ/EN, enlarged UI and all supported time states; save/load mid-production, transit and preparation. Context survives and no duplicate assets, postings, orders or movements are created. |

## 9. Decision record

| ID | Decision | Status |
|---|---|---|
| UI-D22 | Shared Fleet / Vehicle Market / Orders and deliveries workspace; compact physical-asset lists, model-to-offer comparison, requirement-prefilled acquisition, explicit terms and physical delivery/readiness tracking | CONFIRMED on 2026-09-30 |

UI-D22 complements the existing vehicle detail and Line roster. It does not approve new vehicle-allocation, ownership, production, lease, maintenance, cancellation or delivery mechanics.
