# Tranzit — Depot, garage and workshop UI

> **Status: CONFIRMED UI DIRECTION — UI-D16, 2026-09-30.** The player accepted the depot/garage/workshop proposal: a compact operational overview, directly accessible vehicle lists, task-based cards and linked supported Lines, without mandatory manual service scheduling or an embedded schematic/live camera. Exact dimensions, column widths and localized labels remain visual-design work. This specification is not an implemented or tested UI.

Read with [UI_UX_DESIGN.md](UI_UX_DESIGN.md), particularly UI-D07 (windows), UI-D09 (object links), UI-D15 (minimalism/tooltips), and the existing pause rules. [GAME_DESIGN.md](GAME_DESIGN.md), Sections 15–18 and 32.6, owns asset support, maintenance, facility roles, supplies, duties and physical movement. [V1_SCOPE.md](V1_SCOPE.md) owns release scope; [CONTRACT_CANCELLATION.md](CONTRACT_CANCELLATION.md) owns applicable early-exit settlement. This focused document owns presentation only and does not add transport modes or new dispatch/repair rules.

## 1. One window, actual facility roles

Use the shared movable/resizable detail window with name, facility type, owner, actual operating state, player access and an explicit Locate on map action. Identify the roles the site actually provides: operating/dispatch base, parking/storage and maintenance/workshop. A site may combine these roles, but a garage or parking yard does not automatically contain a workshop.

The overview answers: **Which vehicles are here, what is happening to them, and what prevents their next use?** Show a small set of relevant counts and the main actionable bottleneck. For example, present on site, undergoing maintenance and waiting for service. Label counts so subsets are not mistaken for additional vehicles. A vehicle waiting at another site is not physically here merely because it has a booking here.

When there is a problem, show a concise cause, impact and handling state, with direct links to the vehicle, service job, supplies and affected Trip/Line where available. Distinguish a problem already handled within authorized policy from one awaiting the player's decision. Unknown completion times stay unknown; an expected time is not a guarantee. Keep material blockers visible, with supporting calculations and limits in hover/focus explanations rather than permanent paragraphs.

Information must respect the player's rights and available knowledge. A public or rented facility is not an invitation to inspect competitors' private fleet plans, costs or staffing. Opening or following a link never changes the camera, time state or simulation authority by itself.

## 2. Direct vehicle list

Provide a compact vehicle list directly from the overview, expandable to the full list. A count or a route through the global fleet screen is not sufficient. Use these three views:

| View | Meaning |
|---|---|
| On site / Právě v areálu | Vehicles physically at this facility, with their actual task: parked, preparing, fueling, being serviced or waiting, as applicable |
| Expected / Očekávaná | Known planned or active arrivals for preparation, parking or service; distinguish assigned future work, booked visits, vehicles actually en route and conditional estimates |
| Linked vehicles / Navázaná vozidla | Vehicles with this site configured for an operating, parking or maintenance role, including those currently elsewhere; show the role and whether the relationship is inherited, preferred, required or a fallback where the existing model records it |

Each row identifies the concrete vehicle and model, current activity/location when known, facility relationship, service/arrival status, next relevant use and any material readiness problem. Show estimated completion or arrival only when supported by actual planning data. Expose the dated Trip/duty interval so a vehicle's service can be compared with its next assignment. Missing next work is an honest empty state, not an invented departure.

Vehicle, Trip, duty, facility and Line references use UI-D09 exact-object links. For rail vehicles, distinguish locomotives and wagons from their current or planned consist; expose components without counting a train and its components as separate extra capacity. Repeated visits or multiple future tasks on one vehicle are inspectable assignments, not new physical vehicles.

These views may overlap; their counts must not be added as independent fleet totals. An assignment to this facility does not imply physical presence or guaranteed service capacity. A draft-only visit proposal remains explicitly a proposal and cannot appear as a confirmed arrival or consume resources. Criteria-based requirements without concrete assets are separately labelled requirements, not invented vehicle rows.

Refresh from relevant state changes while preserving selection, filters and scroll position. Distinguish a delayed delivery, cancelled visit or replacement assignment from a new vehicle. Retain access to useful past service/visit records through existing history, without leaving a departed vehicle in the On site view.

## 3. Openable task cards

Keep the default overview compact. Use consistent card groups with a brief status/summary, then open details as needed; do not require a sequence of steps.

| Card | Summary and detail |
|---|---|
| Operation and preparation / Provoz a příprava | Current vehicle/consist preparation, physical shunting where applicable, fueling/cleaning and other authorized tasks; what is queued, its blocking reason and effect on the next service |
| Maintenance and repairs / Údržba a opravy | Current work, service queue, scheduled visits, supported service levels and available workshop capacity; vehicle links, expected completion and unmet prerequisites |
| Supplies / Zásoby | Actual stocks with units, shortages, accepted deliveries and expected arrival where known; open the shared UI-D32 Procurement workspace for orders, suppliers and reorder policies |
| Capacity and equipment / Kapacita a vybavení | Parking, workshop positions, shunting and installed service capability separately, with current occupancy, relevant future commitments and actual bottlenecks |
| Staff / Personál | Required aggregate professions/qualifications and available qualified capacity, with shortages and links to the existing staffing workflow |
| Costs and agreements / Náklady a smlouvy | Period-labelled operating costs, rented capacity, external service and supply agreements, charges and renewal/expiry dependencies |

Adapt cards to the site. Do not fill a parking-only site with empty repair or catering settings. Where a service is relevant but unavailable, explain whether equipment, compatible staff, supply or contracted access is missing. An upgrade remains a real project under existing rules, not a card that instantly creates usable capacity.

No generic overall capacity score replaces identifiable constraints. For example, occupied service positions and a queue do not prove that adding parking will improve repair throughput. On inspection, distinguish incompatible vehicles, missing parts, absent qualifications, no free workshop slot and blocked physical access. A queue's vehicles must occupy real valid holding locations under the physical-service rules.

Keep inventory quantities distinct from ordered quantities, reorder proposals and forecast consumption. Renewing a supply agreement does not refill storage; opening a Supplies card does not place an order. Show own/contracted capacity and any shared commitments without double-booking. A site's own workshop remains dependent on suitable equipment, people, parts, time and costs, including support for older models.

## 4. Lines supported by this site

Include a compact **Supported Lines / Navázané linky** list with a route to its full details. Show the Line, relevant Patterns, this facility's role and material dependency problems. Possible roles come from existing relationships: primary/fallback operating base or actual parking/maintenance support through assigned fleet and duties. Do not invent a direct Line-level maintenance assignment where the model instead assigns maintenance to a vehicle or fleet group.

Separate configured preferences from actual scheduled use and distinguish current operation from unlaunched proposals. Group a Line by stable identity with its roles/variants; one Line using several services is not several independent Lines. Link directly to the Line, relevant Pattern, affected vehicle/duty or agreement. This list does not mean passengers board at a depot or that every supported Line makes a commercial station call here.

## 5. Ownership, automation and state safety

At an owned site, offer permitted facility management, service policies, staffing, supply and development workflows. At a third-party site, emphasize the player's reservations, supported services, access conditions, charges and provider information the player is entitled to see. A rental does not grant control over the owner's workforce, equipment or queue. Any permitted priority or policy change must remain within existing contracts, budgets and dispatch/safety rules.

Routine preparation and maintenance stay automated under the existing dispatcher/manager policies. The player observes work, sets permitted rules, provides capacity and resolves exceptions; they need not click Refuel, repair every vehicle manually or sequence each wagon movement. This screen does not add an unrestricted queue-priority override. A closed UI window does not cancel a job, release capacity or undo a purchase.

Vehicles must physically reach a compatible facility; a remote wagon needs valid hauling. A full workshop, unavailable shunter or missing parts cannot be bypassed by changing a row or preferred site. Previewing a solution is not committing it. Accepted procurement, service and access agreements retain their costs and obligations even when a linked Line remains a plan or is suspended. Apply existing impact/settlement rules before changes, rather than hiding consequences in a tooltip.

All views remain inspectable during manual or critical-event pause. Their navigation does not pause/resume or advance preparation, loading, repair, inventory or finance. A critical incident uses the shared incident/pause mechanism; list refresh must not generate repeat incidents.

Use stable identities and shared queries, not independent UI inventories or job queues. Save/load restores the authoritative vehicles, jobs, reservations and supplies and then reconstructs the views without duplicate tasks or payments. Presentation refresh should be event-driven/bounded, not full-network recalculation for every open window.

## 6. No embedded schematic or live camera in this design

Use readable lists/cards and the existing world map. An internal track/parking/workshop schematic and a live 3D camera are not required for this approved UI and should not be added as a delivery dependency. The physical layout, occupancy, shunting and visible world operations remain real; only the extra embedded visualization is omitted.

## 7. Acceptance evidence to collect

These scenarios supplement the existing UI acceptance contract in [V1_ACCEPTANCE_TESTS.md](V1_ACCEPTANCE_TESTS.md). They describe tests to implement and run, not results already obtained.

| ID | Scenario and expected evidence |
|---|---|
| DEPUI-A01 | Inspect a road parking base, rail operating yard and combined workshop site. Actual roles, applicable cards and actionable bottlenecks are clear; no automatic workshop capability or empty unrelated controls. |
| DEPUI-A02 | Compare On site, Expected and Linked vehicles with an off-site assigned vehicle, incoming visit, conditional proposal, departed vehicle and multiple jobs for one asset. Identity, location, commitment and unique counts remain correct. Follow exact vehicle/Trip/Line links and distinguish train components. |
| DEPUI-A03 | Test a full workshop, incompatible vehicle, missing qualification, missing parts and blocked transfer. Show the specific blocker and any supported estimate without inventing capacity, teleporting or automatically ordering. Pending deliveries remain separate from stock. |
| DEPUI-A04 | Inspect the same owned versus rented/third-party site and supported-Line relationships, including a fallback and an unlaunched Line. Respect inspection/control rights; do not expose competitors' private plans, create passenger calls or waive agreed costs. |
| DEPUI-A05 | Observe automatic preparation/repair and policy-based recovery without compulsory per-vehicle clicks. Minimize/close the UI, switch filters and follow links during running and paused states; no hidden job cancellation, time change or new incident occurs. |
| DEPUI-A06 | Save/load during service and after an assignment change. Rebuild the same lists, jobs and relationships without duplicate resources/reservations/payments. Check absent estimates and renamed/unavailable link targets. |
| DEPUI-A07 | Verify compact CZ/EN views and enlarged UI, shared window controls, keyboard-accessible tooltips and visible important blockers/costs. Complete depot inspection and navigation without an embedded schematic or live camera. |

## 8. Decision record

| ID | Decision | Status |
|---|---|---|
| UI-D16 | Depot/garage/workshop overview, On site/Expected/Linked vehicle lists, six task-based card groups, supported-Line information, ownership-aware controls and automatic routine work; no embedded schematic/live-camera requirement | CONFIRMED on 2026-09-30 |

This decision elaborates the accepted proposal within existing mechanics. It does not settle unrelated UI choices, add transport modes, require named ordinary-worker management or authorize new spending/dispatch policies.
