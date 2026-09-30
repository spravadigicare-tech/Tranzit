# Tranzit — Trip detail and execution UI

> **Status: CONFIRMED UI DIRECTION — UI-D25, 2026-09-30.** The player accepted an operations-first detail for one concrete Trip: a prominent stop/call progression, planned-versus-actual-versus-estimated timing, explainable delay, segment-specific passenger/cargo capacity, pre-departure readiness, live execution and retained historical results after completion. Exact visual dimensions, secondary columns and localized labels remain design work. This specification is not an implemented or tested UI.

Read with [UI_UX_DESIGN.md](UI_UX_DESIGN.md), especially UI-D07 (floating windows), UI-D09 (exact-object links), UI-D12 (Line and Trip access), UI-D15 (minimalism/tooltips) and UI-D24 (events). [GAME_DESIGN.md](GAME_DESIGN.md), especially Sections 13.2–13.2.1 and 32.2–32.6, owns timetable/slot windows, Line/Pattern/Trip identity, conditional stops, dynamic routing/platform allocation, connection recovery, fleet assignment and duties. [UI_STATIONS.md](UI_STATIONS.md) owns station boards; [UI_SHIPMENTS.md](UI_SHIPMENTS.md) owns Shipment/CargoLot presentation. This document presents one concrete Trip and does not add manual driving or a second dispatcher.

## 1. Trip identity and purpose

A **Trip / Jízda** is one concrete dated execution of a Service Pattern. Its detail answers immediately:

1. Where is this Trip in its execution?
2. How does actual/estimated timing compare with the plan?
3. What vehicle/consist, crew and capacity are actually involved?
4. What currently threatens completion or downstream obligations?

The window identifies the Line, Pattern/variant, service date, origin/destination or direction, planned departure identity and current Trip state. Cross-midnight Trips retain the service date and stable identity so two departures with the same clock time are not confused.

Do not create a Trip detail before a concrete Trip exists. For demand-driven or conditional service that has not generated a Trip yet, show the Pattern/condition in the Line UI instead.

A cancelled Trip remains the same inspectable Trip with its cancellation reason/history. A completed Trip remains available as history; it does not disappear from the operational record.

## 2. Compact live header

At the top show a concise execution summary, for example:

> R12 · Praha → Brno · planned departure 10:20
>
> **Running · +7 min**
>
> Current location/leg: between Kolín and Pardubice
>
> Expected destination arrival: 13:24 (+4 min)
>
> Consist: Locomotive 362 + 5 coaches · Passengers onboard: 184

Use real values only. When ETA or location precision is unavailable, say so.

Keep current Trip state separate from delay and from incident severity. A Trip can be running late without a player-decision incident, or be on time while another readiness problem threatens a future call.

Provide explicit **Show on map / Zobrazit na mapě** and links to the Line, Pattern, vehicle/consist and duty. Normal object links do not move the camera.

## 3. Stop/call progression is the main body

The primary visual structure is a compact vertical or adaptive sequence of the Trip's commercial/operational calls, not a parameter table.

For each relevant stop/call show:

- station/terminal;
- planned arrival and departure where applicable;
- actual arrival/departure for completed calls;
- current estimate for future calls where supported;
- delay relative to the named planned event;
- current known platform/stand assignment, including changed/provisional/unknown state;
- boarding/alighting or loading/unloading summary where relevant;
- conditional-call state and reason;
- material problem or disruption.

Past calls are visibly completed, the current call/leg is emphasized and future calls remain planned/estimated. **Planned, actual and estimated times must be visually and textually distinguishable**, not only coloured differently.

A platform/stand assignment is dynamic. Show the real current assignment when known; before assignment show Pending/Unknown rather than an invented permanent platform. A changed platform remains visible in Trip history and station information according to the available passenger-information technology.

For a conditional/on-request call, show whether this concrete Trip will call, skip or has not yet resolved the condition, plus the actual reason where available. A pass-through-only location must not be presented as a commercial boarding/loading stop.

When a Trip uses an authorized diversion, show the active route deviation and its timing effect. Do not silently rewrite the Line's nominal route.

## 4. Explainable delay and recovery

A delay number must be drillable into its causal history and remaining recovery.

Example, illustrative only:

> Current delay: +12 min
>
> +8 min waiting for route capacity before Kolín
> +5 min extended loading
> −1 min recovered using planned running-time margin
>
> Expected destination delay: +7 min

The breakdown uses actual structured events/reason codes. Do not attribute a delay to “traffic” or “operations” when the simulation knows the specific capacity conflict, dwell overrun, connection hold, vehicle restriction or other cause.

Distinguish:

- base/expected running time;
- planned running time;
- remaining running-time recovery margin;
- dwell/stop delay;
- turnaround/duty buffer;
- rail/station slot tolerance.

Do not imply that recovery margin permits speeding beyond vehicle, infrastructure or safety limits. If a Trip is outside its protected slot, say so and link to the relevant capacity state where inspectable.

Show delay propagation downstream as an estimate, not a guaranteed future fact. If the dispatcher has already chosen an authorized recovery action, show that handling state. If player authority is required, use the event-centre model in UI-D24.

## 5. Pre-departure readiness

The same Trip detail is useful before departure. Show a compact readiness strip/list such as:

- vehicle/consist;
- crew;
- route/access and relevant slots;
- station-call readiness;
- platform/stand assignment where already known, otherwise correctly pending;
- fueling/energy/preparation where required;
- passenger boarding or cargo loading/readiness;
- critical connection/contract dependencies.

Example:

> Departure in 42 min
>
> Vehicle ✓ · Crew ✓ · Route/slot ✓
>
> Platform: not yet assigned
>
> Loading: 78% complete
>
> Risk: 20 t protected contract cargo is not physically ready.

A pending platform alone is not a blocker when dynamic allocation is normal and station-call capacity is valid. Conversely, accepted route/station capacity does not prove that vehicle, crew, cargo or energy is ready.

Readiness uses authoritative current state and expected completion only where supported. Opening the Trip does not force preparation, reserve an asset or create a recovery command.

## 6. Segment-specific passenger and cargo capacity

Trip capacity is route-segment specific. Do not reduce a multi-stop service to one unexplained “80% occupancy” figure.

For passenger service, expose an adaptive segment view showing relevant measures such as:

- seated/standing/berth capacity by applicable zone/class;
- confirmed reservations;
- onboard passengers;
- forecast/walk-up demand where available;
- passengers boarding/alighting;
- compatible free capacity;
- denied boarding/waiting consequences where they actually occur.

Example:

> Praha → Kolín: 95% seated utilization
>
> Kolín → Pardubice: 82%
>
> Pardubice → Brno: 63%

The basis and period/event must be inspectable. A period average is not the same as this Trip's current segment occupancy.

For freight, show compatible capacity by route segment and commercial allocation tier where useful:

> Praha → Kolín
>
> Protected contract allocation: 120 t
>
> Confirmed one-off: 40 t
>
> Spot allocation: 30 t
>
> Compatible free capacity: 60 t

Do not treat nominal tonnes as usable for incompatible cargo. Segment release occurs only after actual unloading. A future reservation is not already loaded cargo.

Specific Shipments/CargoLots can be opened from the capacity/cargo detail under UI-D23. Do not list every CargoLot in the default header if a compact aggregate is sufficient.

## 7. Task-based detail cards

Below the progression, use compact independently openable groups:

| Card | Content |
|---|---|
| Vehicle / consist / Vozidlo / souprava | Actual assigned vehicle(s), consist composition, substitutions, traction exchanges and relevant physical assignment state |
| Capacity and passengers/cargo / Kapacita a cestující/náklad | Segment-specific occupancy/allocations, reservations, compatible free capacity, waiting/denied demand and linked Shipments where relevant |
| Crew and preparation / Posádka a příprava | Qualified crew capacity, duty/crew-change state, preparation, fueling/charging, cleaning/service work and remaining readiness |
| Operation and infrastructure / Provoz a infrastruktura | Actual route, diversion, rail/road restrictions, station-call/route capacity state, slot/tolerance information and current platform/stand assignments |
| Events and history / Události a historie | Delay causes, platform changes, substitutions, incidents, dispatcher recovery, cancellations and Trip-specific historical events |

Use the same global components and object links. Hide irrelevant sections rather than showing empty freight fields on a passenger bus or passenger fields on a freight-only Trip.

The Trip detail exposes **Open duty / Otevřít oběh** into the confirmed UI-D31 workspace in [UI_DUTIES.md](UI_DUTIES.md), scoped to the relevant vehicle/consist and time. It does not require the player to manually build every duty or named crew assignment.

## 8. Vehicle/consist and duty continuity

Show the concrete vehicle/consist actually assigned once assignment exists. Criteria-based coverage before serial assignment must remain clearly distinct from the concrete asset selected for this Trip.

For rail, expose locomotives and coaches/wagons without double-counting the consist and its components as extra fleet/capacity. If a traction exchange or consist change is planned, show where and when it occurs and the physical readiness of the replacement assets.

Substitution history retains both original and replacement assignment. A replaced vehicle is not rewritten as though it was never planned.

The current/next duty relationship can explain downstream consequences:

> Trip arrives Brno +12 min
>
> Same vehicle is planned for Trip 14:10 after 18 min turnaround.
>
> Current predicted available turnaround: 6 min.

Do not treat the next Trip as already delayed unless the scheduling/recovery system actually predicts that result.

## 9. Passenger connections and freight transfers

Show protected passenger connections and material freight-transfer dependencies when they affect this Trip.

For protected passengers, the Trip can show:

- connecting incoming/outgoing Trip;
- number/capacity requirement;
- planned/minimum transfer time;
- hold-policy state;
- current risk;
- authorized hold/rebooking action.

A connection hold must respect slot, duty and downstream constraints. High company priority does not override another operator's stronger infrastructure rights.

For freight, show cargo readiness cutoff, transfer readiness and responsibility when a protected CargoLot may miss the Trip. The Trip detail must not call carrier-delayed cargo a customer no-show.

Detailed Shipment/CargoLot history remains in UI_SHIPMENTS; the Trip view shows only the impact relevant to this execution.

## 10. Completed and cancelled Trip

After completion, the same detail becomes a historical execution record.

Keep:

- planned versus actual call times;
- final arrival/departure delays;
- actual route/diversions;
- actual vehicle/consist and substitutions;
- passenger/cargo quantities by relevant segment;
- completed loading/unloading/boarding events;
- incidents and recovery actions;
- relevant connection outcomes;
- realized Trip-attributable revenue/cost postings where the finance model can attribute them.

Example:

> **Completed**
>
> Origin departure: +7 min
>
> Destination arrival: +4 min
>
> Passengers carried: 184
>
> Protected connections: 3 maintained
>
> Incidents: 1
>
> Open financial breakdown · Open event history

Do not invent exact profit allocation for shared costs when the accounting model cannot attribute them cleanly. Any displayed financial result must state its basis and period/object scope and link to UI-D19.

A cancelled Trip remains inspectable with when/why it was cancelled, what physical work/cargo/passenger state existed, recovery/refund/rebooking consequences and which authority/policy made the decision. Cancellation does not imply onboard cargo/passengers teleported back or assets became instantly free.

## 11. Own versus other operators

The player may inspect public/available Trip information for another operator where the simulation makes it known, especially station-board calls. Show only appropriate public operational facts such as published/known times, operator, route, current communicated delay and platform.

Do not expose another operator's private vehicle cost, crew plan, cargo allocations, internal recovery policy or commercial margins merely because its Trip is visible at a shared station.

Player commands/actions appear only where the player has authority.

## 12. Refresh, save/load and input safety

Live timing, assignment and capacity changes update without destroying the player's scroll/selection or reopening collapsed cards.

Save/load preserves the concrete Trip identity, version, actual calls, vehicle/consist assignment, onboard/reserved capacity, incident/recovery history and relationship to the duty/Line/Pattern.

Loading must not:

- regenerate the Trip under a new ID;
- reset actual call times;
- turn estimates into actuals;
- duplicate passenger/cargo reservations;
- forget cancellation;
- rewrite a running Trip to a newly edited Pattern version.

Opening, filtering or inspecting the Trip does not pause/resume time or issue a dispatch command. Critical events still follow UI-D08/UI-D24.

## 13. Acceptance evidence to collect

| ID | Required scenario |
|---|---|
| TRIPUI-A01 | Open a passenger Trip before departure, while running and after completion. The same identity retains readiness, live progression and historical actuals without generating a replacement Trip. |
| TRIPUI-A02 | At several calls verify planned, actual and estimated times plus dynamic platform state; changed/provisional/unknown platforms are distinguished and do not imply a dedicated platform. |
| TRIPUI-A03 | Cause delay through route capacity, dwell/loading and an authorized recovery margin. The displayed causal breakdown reconciles to current delay and never implies unsafe extra speed. |
| TRIPUI-A04 | Inspect passenger capacity on several origin-destination segments with reservations, walk-up demand and denied boarding. Segment figures reconcile to the actual capacity ledger. |
| TRIPUI-A05 | Inspect freight capacity with protected/one-off/spot allocations and actual unload/release across segments. Nominal incompatible capacity is not presented as free compatible capacity. |
| TRIPUI-A06 | Test criteria-based assignment, concrete assignment, substitution, consist change and next-duty conflict. Assets and consists are not double-counted and original assignment history remains visible. |
| TRIPUI-A07 | Test conditional stop, skipped call, diversion, protected passenger connection and freight cutoff. The Trip exposes the real reason and links to relevant Pattern, station, Shipment and event details. |
| TRIPUI-A08 | Cancel a Trip with affected reservations/cargo, then save/load. Cancellation reason, physical state, recovery history and stable links persist without teleportation or duplicate reservations. |
| TRIPUI-A09 | Inspect another operator's public Trip from a station board. Public timing/status is visible but private fleet/cost/cargo/crew data and player commands are not leaked. |
| TRIPUI-A10 | Verify CZ/EN, enlarged UI, paused/running use and live refresh. Opening/hovering/following links never changes speed, assignment or operational state. |

## 14. Decision record

| ID | Decision | Status |
|---|---|---|
| UI-D25 | Concrete Trip detail with prominent stop/call progression, explicit planned/actual/estimated timing, explainable delay/recovery, segment-specific capacity, pre-departure readiness, live vehicle/crew/infrastructure state and retained completed/cancelled history | CONFIRMED on 2026-09-30 |

UI-D25 complements UI-D01–UI-D24. It does not change Trip generation, timetable construction, dispatch priority, platform allocation, fleet assignment, capacity priority, cargo custody or connection-recovery mechanics.
