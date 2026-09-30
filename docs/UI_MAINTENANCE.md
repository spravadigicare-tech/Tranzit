# Tranzit — Maintenance planning UI

> **Status: CONFIRMED UI DIRECTION — UI-D30, 2026-09-30.** The player accepted one maintenance-planning workspace over the existing vehicle-maintenance, workshop-capacity and physical-transfer mechanics. The UI must distinguish preventive targets from hard limits, show future workshop/fleet conflicts, compare own and external service with real travel/capacity, and keep routine servicing automated within player policy. Exact visual dimensions, labels, preset names and balancing thresholds remain design/content work. This specification is not an implemented or tested UI.

Read with [UI_UX_DESIGN.md](UI_UX_DESIGN.md), especially UI-D09 (exact-object links), UI-D15 (minimalism/tooltips), UI-D16 (facility/workshop detail), UI-D22 (fleet) and UI-D25 (Trip detail). [GAME_DESIGN.md](GAME_DESIGN.md), especially Sections 15.4, 16 and 32.6, owns maintenance policy, hard limits, workshop/service-provider capacity, physical movement, fleet reserve, preparation and disruption recovery. This document presents those mechanics; it does not add a second maintenance scheduler.

## 1. Entry and purpose

Use **Assets → Maintenance / Majetek → Údržba** as the primary fleet-wide maintenance workspace.

The default top-level views are:

- **Plan / Plán**
- **In progress / Probíhá**
- **Vehicles at risk / Vozidla v riziku**
- **Workshop capacity / Kapacita dílen**

The overview answers four questions:

1. Which vehicles need maintenance soon?
2. Which workshop/service jobs are already committed or active?
3. Which future Trips/duties are threatened by maintenance timing?
4. Where is workshop/service capacity itself the bottleneck?

Illustrative summary:

> 12 vehicles require service within 14 days  
> 4 currently in service  
> 2 conflict with future Trips  
> 1 approaching a hard limit  
>
> Main bottleneck: Brno workshop is full next week

Do not replace this with one opaque fleet-health percentage.

## 2. Planned maintenance list

Use a compact, filterable list that compares policy target, hard limit, location/service path and future operational impact.

Suggested columns:

| Field | Meaning |
|---|---|
| Vehicle | Exact physical asset/model |
| Service/inspection | Required work or current maintenance category |
| Preventive target | Player-policy target or recommended service point |
| Hard limit | Legal/safety/manufacturer/technical dispatch limit |
| Current margin | Remaining km/hours/calendar margin in applicable units |
| Preferred service location | Own/external provider and actual compatibility |
| Planned service window | Booked or proposed time, clearly distinguished |
| Travel/positioning | Time/route needed to reach and later leave service |
| Next affected work | Trip/duty/Line impacted, if any |
| Status/problem | Conflict, missing slot, missing part, unavailable provider, etc. |

Example:

| Vehicle | Service | Target | Hard limit | Where | Window | Impact |
|---|---|---|---|---|---|---|
| Loco 104 | periodic | +760 km | +3,520 km | Brno | tomorrow | no conflict |
| Bus 32 | inspection | +2 days | +6 days | external service | day 3 | conflict with Trip |
| Coach 18 | repair | now | not dispatchable | Praha | waiting for part | 3 Trips affected |

A proposal is not a confirmed workshop booking. “Preferred workshop” is not physical location. Show those distinctions explicitly.

## 3. Preventive target versus hard limit

This distinction is mandatory and visible.

- **Preventive target** comes from maintenance policy and may be advanced or deferred within allowed policy.
- **Hard limit** cannot be exceeded by dispatch policy or player override.

If a planned duty would cross only the preventive target:

> Service target would be exceeded by this duty.  
> Hard limit remains valid.  
> Policy permits deferral.

The UI may offer:
- service before duty;
- defer within policy;
- find another service window;
- use another vehicle.

If a duty would cross the hard limit:

> This vehicle cannot legally/safely cover the duty before required service.

Do not expose an Ignore/Force dispatch action.

## 4. Maintenance policy hierarchy

Expose the existing inheritance hierarchy:

**Company default → fleet group / vehicle category / model → specific vehicle override**

Always show the effective source.

Example:

> Company default: Standard  
> Heavy road fleet: inherited  
> Bus 32: custom override

Provide simple policy presets as editing conveniences, for example:

- Conservative
- Standard
- Higher utilization
- Custom

Presets must map to real explicit settings, not hidden reliability buffs.

Relevant visible settings can include:

- target service point as % of allowed interval;
- minimum remaining km/hours/time before assigning long work;
- preferred workshop/service-provider strategy;
- whether service may be advanced into an idle workshop window;
- how far preventive service may be deferred while remaining before hard limit;
- minimum post-service margin before intensive work;
- external-service fallback allowed/forbidden where contract/provider access exists.

After choosing a preset, show the actual resulting values.

## 5. Policy trade-off preview

When policy changes materially, show qualitative/quantitative effects that can actually be supported:

- more/fewer planned services;
- higher/lower workshop demand;
- more/less expected planned downtime;
- stronger/weaker fleet-reserve requirement;
- more/fewer predicted target conflicts;
- change in how close fleet is operated to hard limits.

Do not invent precise failure-risk percentages unless the simulation model can defensibly calculate them.

Example:

> More conservative target  
> + 3 additional planned services in next 14 days  
> + Brno workshop becomes overbooked on Day 8  
> + one extra compatible reserve vehicle needed to maintain current timetable  
> wear-related failure risk expected to decrease

The final line can remain qualitative if no robust probability is available.

## 6. Workshop capacity as dated capacity

Workshop/service capacity is time-specific and capability-specific.

Do not show only:

> Capacity: 5 vehicles

Instead show an inspectable planning horizon such as:

> Brno workshop  
> Today: 4 / 5 compatible positions used  
> Tomorrow: 5 / 5  
> Day 8: 5 / 5  
> Day 9: 3 / 5  
>
> 2 planned services do not currently fit.

The detailed cause can be:

- no free compatible service position;
- required equipment unavailable;
- qualified mechanics shortage;
- required parts/material missing;
- provider contract/priority insufficient;
- vehicle cannot physically reach workshop in time;
- transfer/shunting route/capacity missing;
- workshop can perform light service but not the required heavy work.

A parking space is not workshop capacity. A workshop position without staff/parts/equipment may not be usable.

## 7. Own versus external service comparison

When more than one valid maintenance solution exists, compare them using real constraints.

Example:

> **Loco 104**
>
> Own Brno workshop  
> Earliest start: Day 11  
> Service cost: 420 money  
> Total downtime including movement: ~2 days
>
> **Authorized Morava Rail service**  
> Earliest start: Day 7  
> Service cost: 690 money  
> Travel: 5 h
>
> **Praha service partner**  
> Earliest start: Day 8  
> Service cost: 510 money  
> Travel: 9 h

The comparison must include as applicable:

- earliest real service slot;
- compatibility/service level;
- service duration;
- travel/haul/repositioning time both ways;
- price;
- parts availability;
- booking priority/contract;
- next Trip/duty readiness;
- warranty/lease responsibility.

A quoted external slot is not infinite provider capacity. Accepting it creates/uses the real service booking/agreement workflow and actual workshop capacity.

## 8. Maintenance conflicts with future operation

The workspace must identify where planned maintenance interacts with Trips/duties.

Example:

> **Loco 104 requires service before R12 / 10:20**
>
> Running R12 would cross the preventive target.  
> Hard limit remains valid.
>
> Options:
> - service before R12 → replacement locomotive required;
> - defer service → permitted by current policy;
> - find another service window.

For a hard-limit conflict:

> **Hard inspection limit would be exceeded during this duty.**
>
> Vehicle is not valid for assignment unless service is completed first.

Link directly to:

- Trip;
- duty;
- Line/Pattern;
- candidate substitute vehicles;
- workshop/service provider;
- relevant event/problem.

The maintenance planner and Line/fleet planner use the same authoritative assignments/reservations. Do not mark one vehicle simultaneously available for duty and committed to workshop service.

## 9. Routine scheduling and automation

Default operation is automated.

The dispatcher/maintenance planner may, within policy and actual capacity:

- choose a suitable maintenance window;
- advance preventive service into an idle period;
- book/use the preferred valid workshop;
- use an allowed fallback provider;
- arrange normal physical repositioning/transfer;
- protect future hard limits;
- re-evaluate after timetable/fleet/workshop changes.

The player should not click Repair/Service on every vehicle individually.

Manual player actions remain useful for:

- changing maintenance policy;
- selecting/overriding preferred workshop/provider;
- accepting an external service quote/agreement;
- choosing between competing high-impact service windows;
- overriding a specific vehicle within allowed hard constraints.

Managers may later execute routine maintenance decisions under existing delegation rules. They cannot exceed budget/approval rights, hard limits or workshop capacity.

## 10. Planned maintenance versus breakdown repair

Use the same maintenance workspace but distinguish the work type clearly:

- preventive/scheduled maintenance;
- mandatory inspection;
- defect repair;
- post-failure repair/recovery;
- warranty/service-campaign work where applicable.

Example degraded failure:

> **Loco 117 — reduced power**
>
> Safe to complete current Trip under restriction.  
> Must enter workshop afterwards.
>
> Nearest suitable planned service: Brno  
> Transfer after Trip: 48 km
>
> Dispatcher has already scheduled the service.

If the operational-failure rules say the vehicle must stop or reach only a suitable safe point, the maintenance UI must not imply it can simply continue to the preferred workshop under normal power.

Physical recovery remains owned by GAME_DESIGN Section 16.3 and event/Trip UI.

## 11. Fleet-level planning horizon

Provide quick horizon filters such as:

- next 7 days;
- next 14 days;
- next game month;
- custom period where useful.

Summary can show:

> Fleet: 82 vehicles  
> Planned services: 13  
> Active repairs: 4  
> Expected planned maintenance downtime: 9%  
> Effective reserve after planned maintenance: 6 compatible vehicles  
> 2 Lines may fall below reserve target

Every percentage/count states its basis and period.

Clicking a reserve issue opens the relevant Line/fleet compatibility view rather than a generic warning page.

Do not count an incompatible spare vehicle as reserve simply because it is idle.

## 12. Workshop/provider detail integration

UI-D30 is the fleet-wide planning perspective. UI-D16 remains the detail perspective for a specific depot/garage/workshop.

From maintenance planning:
- click a workshop → open its UI-D16 detail;
- click service queue → open the facility's Maintenance and repairs card;
- click external provider → open the external-company detail and UI-D27 Our agreements where applicable.

From a workshop:
- **Open maintenance plan** can open UI-D30 scoped to that facility/provider.

Both views must show the same jobs/bookings/capacity.

## 13. Parts and supply dependencies

Where the maintenance model requires parts/materials, show their actual state:

- in stock;
- reserved for this job;
- ordered;
- expected arrival;
- unavailable/no supplier;
- compatible substitute where the core rules allow one.

Ordered parts are not inventory.

A job blocked by parts remains visibly blocked even if a workshop position is free.

The maintenance workspace links into the confirmed UI-D32 Procurement workspace in [UI_PROCUREMENT.md](UI_PROCUREMENT.md) for purchase orders, suppliers and reorder rules rather than creating a separate parts marketplace. Maintenance remains authoritative for which part/material the job actually requires and whether it is compatible/reserved.

## 14. Historical/legacy vehicle support

Old vehicles remain serviceable as long as real support exists.

The maintenance UI must explain scarcity through actual causes such as:

- no nearby workshop supports the model;
- specialist mechanic capability unavailable;
- compatible part supply scarce;
- external provider has long queue;
- own workshop lacks required equipment/knowledge.

Do not display “obsolete: +30% maintenance cost” merely because the calendar advanced.

When own workshop capability solves the problem, show its real staffing/equipment/parts/capacity cost.

## 15. Save/load and state safety

Persist maintenance policy inheritance/overrides, planned/accepted service bookings, active jobs, provider agreements, hard-limit state, parts reservations and physical vehicle locations through the owning systems.

After save/load:

- confirmed service bookings remain confirmed;
- proposed windows do not become bookings;
- active repair progress is not restarted;
- workshop slots are not duplicated;
- already used/paid parts/services are not charged twice;
- vehicle mileage/hours/inspection margins are unchanged except for actual simulated progress;
- maintenance conflicts and fleet reserve reconstruct consistently.

Opening, filtering, comparing or changing a **draft policy preview** performs no repair, movement or purchase. Binding policy/application/provider actions use explicit validation.

## 16. Acceptance evidence to collect

| ID | Required scenario |
|---|---|
| MAINTUI-A01 | Open fleet-wide Maintenance with vehicles before preventive target, past target but within hard limit, and at hard limit. Target and hard limit are unmistakably different; hard-limit dispatch cannot be overridden. |
| MAINTUI-A02 | Change company policy, fleet-group override and one vehicle override. Effective source and actual values remain visible; changing a parent updates only inheriting children. |
| MAINTUI-A03 | Compare Conservative/Standard/Higher-utilization policy effects over a 14-day horizon. Workshop demand, planned downtime and reserve conflicts update from real scheduling data without invented exact failure probabilities. |
| MAINTUI-A04 | Fill an own workshop and compare two external service providers with different price, travel and earliest-slot constraints. Accepted choice consumes actual provider/workshop capacity and requires physical vehicle transfer. |
| MAINTUI-A05 | Create one preventive-target conflict and one hard-limit conflict with future Trips. The first can use allowed deferral/substitution; the second blocks assignment until service. |
| MAINTUI-A06 | Trigger a degradable failure that can finish the Trip and an immobilizing failure. Planned post-Trip service and physical recovery remain distinct and link to the same canonical vehicle/job history. |
| MAINTUI-A07 | Block service separately by workshop position, qualification, parts and vehicle-transfer feasibility. Each reason is explicit; freeing an unrelated resource does not falsely clear another blocker. |
| MAINTUI-A08 | Inspect fleet reserve before/after several scheduled services. Compatible reserve is not double-counted across Lines or satisfied by incompatible idle assets. |
| MAINTUI-A09 | Save/load with proposed service windows, confirmed bookings, active repairs and external-provider work. No duplicate slot, job, payment, part reservation or mileage reset occurs. |
| MAINTUI-A10 | Verify CZ/EN, enlarged UI, paused/running inspection and direct links between vehicle, Trip/duty, Line, workshop/provider and agreements. Browsing does not change speed or issue maintenance work. |

## 17. Decision record

| ID | Decision | Status |
|---|---|---|
| UI-D30 | Fleet-wide maintenance planning workspace with Plan / In progress / Vehicles at risk / Workshop capacity views, explicit preventive-target versus hard-limit distinction, inherited policy presets, dated workshop capacity, own-vs-external service comparison, future Trip conflicts and automated routine scheduling | CONFIRMED on 2026-09-30 |

UI-D30 complements UI-D01–UI-D29 and UI-D16 in particular. GAME_DESIGN Sections 15.4 and 16 remain authoritative for mechanics.
