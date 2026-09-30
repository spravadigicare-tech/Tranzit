# Tranzit — Shipment and split-cargo UI

> **Status: CONFIRMED UI DIRECTION — UI-D23, 2026-09-30.** The player accepted a Shipment detail focused on actual cargo location, continuation and deadline risk; one Shipment remains one commercial item even when split into multiple physical CargoLots and Trips. The overview includes a directly accessible parts list and a compact transport-chain view, with routine allocation automated and exceptions inspectable. Exact dimensions, column widths and localized labels remain visual-design work. This specification is not an implemented or tested UI.

Read with [UI_UX_DESIGN.md](UI_UX_DESIGN.md), especially UI-D07 (floating windows), UI-D09 (exact-object links) and UI-D15 (minimalism/tooltips). [UI_COMMERCIAL.md](UI_COMMERCIAL.md) owns the surrounding contract/Transport Plan workspace. [GAME_DESIGN.md](GAME_DESIGN.md), especially Sections 11.0.1, 11.9–11.11, 12 and 32, owns Shipment/CargoLot identity, physical custody, reservations, loading priority, Transport Plans and Trips. [V1_SCOPE.md](V1_SCOPE.md), Section 5, owns the first-release split-shipment requirement. This document changes presentation only.

## 1. Shipment overview

The Shipment detail answers three questions immediately:

1. **Where is the cargo physically now?**
2. **How is each part expected to continue?**
3. **Will the complete Shipment satisfy its delivery obligation?**

Keep the Shipment as the main commercial identity even when execution splits it into several CargoLots, allocations, vehicles or Trips. Do not create a second player-facing Shipment just because 100 t travel as 40 + 40 + 20 t or because onward capacity later recombines them differently.

The header identifies the Shipment, commodity/passenger-group type where applicable, ordered quantity and units, origin, destination, linked customer/contract, current overall fulfilment state and contractual delivery deadline.

Directly below, show a compact quantity reconciliation such as:

- delivered/accepted;
- physically in transit;
- physically waiting/stored;
- loading/unloading/handling;
- remaining at origin where applicable;
- exception/recovery quantity where applicable.

Every visible quantity must reconcile to the authoritative Shipment/CargoLot ledger. Categories that overlap in the underlying model must not be added as independent totals.

Example, illustrative only:

> Shipment 0284 · Timber · 100 t
>
> Delivered: 40 t · In transit: 40 t · Waiting at terminal: 20 t
>
> 20 t currently has no confirmed onward allocation.
>
> Open Transport Plan · Review options

Do not label a Shipment complete because one part arrived. Completion follows its actual delivery policy and accepted delivered quantity.

Show the contractual deadline separately from any estimated completion of the whole Shipment. If a supported ETA cannot be calculated, show Unknown / Not currently estimable rather than treating the last reserved Trip as guaranteed arrival.

## 2. Compact transport chain

Show the current versioned Transport Plan as a compact ordered chain, for example:

**Factory → road collection → freight terminal → rail service → destination terminal → consignee**

Each leg identifies its execution type, responsible operator, endpoints, planned/current state and any material dependency. Specific Lines, Patterns, Trips, terminals, vehicles, external transport orders, customers and contracts use UI-D09 links.

The chain is a plan/execution representation, not a single moving Shipment marker. A split Shipment can have different CargoLots on different legs at the same moment. Selecting a CargoLot highlights its current physical location and relevant completed/current/future legs without implying the other portions are there too.

A plan leg may exist before cargo reaches it. Distinguish:

- proposed future leg;
- reserved/allocated future movement;
- physically ready for that movement;
- loading/handling;
- actually onboard/in transit;
- unloaded/transferred;
- completed/accepted delivery.

Changing or reserving a future leg does not change the CargoLot's physical location.

## 3. Direct CargoLot / shipment-parts list

The overview includes a compact, directly accessible list of the Shipment's current physical portions. It is not hidden only in a tooltip.

Each row exposes:

| Field | Meaning |
|---|---|
| Quantity | Exact CargoLot quantity and unit; preserve indivisible handling units/split increments |
| Actual location/custody | Physical facility, vehicle or explicit handling state |
| Current physical state | Waiting, loading, loaded/in transit, unloading, delivered/accepted, recovery, etc. |
| Current Trip/vehicle | Exact current movement where one exists |
| Next planned movement | Next live reservation/Trip/leg if one exists, distinctly labelled as future |
| Readiness | Whether this portion can actually make the next movement and why not if blocked |
| Deadline/risk | Relevant delivery or transfer risk, with responsibility/cause where known |

Example:

| Quantity | Physical location | State | Next step |
|---|---|---|---|
| 40 t | Consignee | Accepted | Complete |
| 40 t | Train / Trip 014 | In transit | Unload at destination |
| 20 t | Freight terminal | Waiting | No confirmed onward allocation |

A row opens the exact CargoLot/portion detail or focused Shipment subsection. Vehicle, Trip, terminal, allocation and contract references are separately clickable.

The same CargoLot can have a future Trip reservation while physically waiting in a warehouse. Show both facts without making the reservation look like movement.

Do not derive waiting cargo from all historical allocations. Cancelled/completed allocations remain history; live unreserved quantity comes from the canonical current-leg state and reservations.

## 4. Status and responsibility

For a problem, show the specific affected quantity and its effect on the complete Shipment.

Examples:

> 20 t missed the connection because the player's collection leg arrived late. Dispatcher is evaluating recovery.

or

> 30 t were not ready before the customer-side cutoff. Reserved capacity was released under the applicable terms.

Keep responsibility visible where known:

- customer-side;
- carrier/player-side;
- player-contracted subcontractor;
- qualifying infrastructure/external disruption;
- unknown/not yet determined.

Rebooking does not erase the original cause or contractual consequence. A recovery movement is the next operational action, not proof that the missed connection never happened.

Where the dispatcher/manager is already handling the exception within authorized policy, say so. Player attention is requested only when actual authority or a decision is needed.

## 5. Task-based cards

Keep the default overview compact and expose four main detail groups.

| Card | Content |
|---|---|
| Transport Plan / Přepravní plán | Ordered legs, operators, endpoints, reservations, connections, current plan version and valid alternatives/recovery proposals |
| Cargo and requirements / Náklad a požadavky | Quantity, commodity, split increment, indivisible units, handling/storage/temperature/hazard requirements and delivery policy |
| Deadlines and obligations / Termíny a závazky | Contract deadline, SLA/delivery conditions, responsibility, guarantees, penalties/compensation exposure and current risk |
| History and costs / Historie a náklady | Physical handling events, allocation/replanning history, custody changes, incurred transport/handling costs and material exception explanations |

Cards reuse actual objects and postings. They do not create duplicate schedules, cargo ledgers or financial totals.

For a non-contract Shipment, hide irrelevant contractual fields rather than filling the UI with empty SLA boxes. For a simple single-Trip Shipment, the same structure may collapse to a very concise view.

## 6. Split, merge and physical invariants

The UI must remain correct when:

- one Shipment splits into several CargoLots;
- a CargoLot is further split according to its allowed increment/handling units;
- compatible portions later share one vehicle or visual pile while remaining separate records;
- several inbound CargoLots become available for different onward Trip allocations;
- only part of a lot loads;
- a Trip is cancelled while cargo is already partly loaded;
- a future allocation is superseded;
- cargo waits between legs;
- storage is full;
- a perishable/quality-sensitive portion degrades differently from another portion.

Never use presentation merging to reset age, quality, cost basis, contract responsibility or lineage. Never duplicate quantity by showing a parent Shipment amount and its CargoLots as if both were physical stock.

If the simulation combines compatible CargoLots internally while preserving constituent obligations, the UI can visually group them, but the player must still be able to inspect distinct obligations where they matter.

A cancelled Trip is not proof that onboard cargo is back in storage. Preserve the actual custody until physical unloading/recovery occurs.

## 7. Routine automation and manual intervention

Default play should operate at Shipment/contract level. The dispatcher and allocation system use the canonical compatibility and commercial-priority rules to choose capacity, split/rebook cargo and recover routine disruptions within permitted policies.

The player is not required to assign every tonne or pallet manually. Advanced/manual controls may inspect or override eligible allocations where the underlying design allows it, but they must revalidate capacity, physical readiness and protected commitments.

A manual change to one CargoLot or one future allocation does not silently rewrite:

- other parts of the same Shipment;
- running Trips;
- already completed physical handling;
- the contract's reusable Transport Plan template;
- unrelated Shipments using the same Line.

If a recovery proposal requires an additional Trip, external carrier or changed Line capacity, hand off to the existing planners. Do not implement a shipment-only hidden dispatch engine.

## 8. Map and navigation

Provide an explicit **Show on map / Zobrazit na mapě** action for the Shipment and for a selected CargoLot. For a split Shipment, the map can highlight all current physical portions with distinguishable markers and the selected portion emphasized. It must not invent one centroid or moving icon and imply all cargo is there.

Future legs can be shown as planned paths using different line treatment from actual completed/current movement. The map-layer opportunity UI may reveal relevant recovery/transport possibilities, but opening it does not reserve capacity or move cargo.

Normal links open details without moving the camera; Locate remains explicit under UI-D09.

## 9. Save/load and live refresh

Persist Shipment identity, CargoLot quantities/locations/custody, plan versions, live reservations, handling state, responsibility/cause, history and recovery assignments under the canonical save rules.

After save/load, the UI reconstructs the same quantity reconciliation and physical state without:

- duplicating CargoLots;
- recreating completed allocations;
- reloading cargo that was already onboard;
- resetting age/quality;
- losing missed-connection responsibility;
- regenerating a new Shipment because a split exists.

Live refresh preserves selected portion, expanded cards, filters and scroll position. A status can update while the window is open without changing object identity or silently accepting a new plan.

Opening, filtering or inspecting a Shipment never pauses/resumes, moves cargo or changes a reservation. Critical incidents independently follow UI-D08.

## 10. Acceptance evidence to collect

These scenarios define UI evidence to collect when implemented; they are not claims of a passing build.

| ID | Required scenario |
|---|---|
| SHIPUI-A01 | Show a simple unsplit Shipment and a 100 t Shipment split into 40 + 40 + 20 t. Header totals reconcile exactly and the split Shipment remains one commercial item. |
| SHIPUI-A02 | Put portions simultaneously at origin, in terminal storage, on a running Trip and delivered. Each row shows actual physical location/custody and the Shipment has no misleading single moving location. |
| SHIPUI-A03 | Give waiting cargo a future reservation. Verify the row shows physical waiting separately from the booked future Trip; reserving/replanning changes no physical location. |
| SHIPUI-A04 | Reallocate only one portion after a missed connection. Other portions keep their current Trips/history and the reusable contract Transport Plan template is not silently mutated. |
| SHIPUI-A05 | Test partial loading, cancelled Trip with cargo onboard, storage full, indivisible handling units and a perishable portion. Quantity, custody, lineage and quality remain consistent and inspectable. |
| SHIPUI-A06 | Trigger customer-side lateness, carrier-side lateness and a subcontractor/infrastructure issue. Responsibility, recovery and contract consequences remain visible after rebooking. |
| SHIPUI-A07 | Follow Shipment → CargoLot → Trip → vehicle/terminal/Line/contract links and explicit map locate. Pinned windows/source context survive and navigation performs no operational command. |
| SHIPUI-A08 | Save/load during loading, in transit, waiting and recovery. Reopen the Shipment and verify no duplicated cargo/reservations, reset age or fabricated completion. Verify CZ/EN, enlarged UI and pause-state neutrality. |

## 11. Decision record

| ID | Decision | Status |
|---|---|---|
| UI-D23 | Shipment detail centred on physical location, continuation and deadline; one commercial Shipment with a directly accessible CargoLot list, compact Transport Plan chain, clear reserved-vs-physical states and automated routine allocation with inspectable exceptions | CONFIRMED on 2026-09-30 |

UI-D23 complements UI-D01–UI-D22. It does not change cargo identity, loading priority, contract responsibility, Transport Plan versioning, capacity allocation or physical handling mechanics.
