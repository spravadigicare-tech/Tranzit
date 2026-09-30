# Tranzit — Vehicle and crew duties UI

> **Status: CONFIRMED UI DIRECTION — UI-D31, 2026-09-30.** The player accepted one Operations workspace for vehicle duties and aggregate crew duties, with a compact timeline, explainable physical transitions, conflict-focused views, actual-versus-planned execution history and automatic dispatcher construction by default. Exact visual dimensions, timeline density, labels and optional editing affordances remain design work. This specification is not an implemented or tested UI.

Read with [UI_UX_DESIGN.md](UI_UX_DESIGN.md), especially UI-D09 (exact-object links), UI-D12 (Line workspace), UI-D15 (minimalism/tooltips), UI-D24 (events), UI-D25 (Trip detail) and UI-D30 (maintenance). [GAME_DESIGN.md](GAME_DESIGN.md), especially Section 32.6 (vehicle duties, turnaround, preparation, disruption recovery) and Section 32.7 (crew duties and crew recovery), owns duty mechanics. This document presents those mechanics and does not add another scheduler.

## 1. Entry and purpose

Use **Operations → Duties / Provoz → Oběhy** as the primary workspace.

Provide three main views:

- **Vehicles / Vozidla**
- **Crews / Posádky**
- **Conflicts / Konflikty**

The workspace answers:

1. What work will each concrete vehicle/consist perform over time?
2. Are the physical transitions between tasks actually feasible?
3. How do aggregate crew-duty blocks cover that operation?
4. Which current delay, maintenance event or shortage threatens later work?

Vehicle and crew duties are related but distinct. A vehicle can continue while one crew duty ends and another begins.

## 2. Vehicle duty detail

A vehicle duty shows one concrete or criteria-backed sequence of tasks over time.

Typical task types:

- commercial Trip;
- deadhead/repositioning;
- turnaround;
- fueling/charging;
- cleaning/service preparation;
- maintenance/inspection;
- shunting/consist change;
- parking/stabling;
- depot departure/return;
- other canonical preparation/recovery task.

Illustrative vertical detail:

> **Locomotive 104 · today**
>
> 05:10 Praha depot  
> preparation
>
> **06:00 Praha → Brno**  
> R12 / Trip 014
>
> 09:12 Brno  
> turnaround 28 min
>
> **09:40 Brno → Praha**  
> R12 / Trip 021
>
> 12:53 Praha  
> water/service check
>
> **14:10 Praha → Plzeň**  
> R7 / Trip 044
>
> 17:20 Plzeň depot  
> stabled

The vehicle does not permanently belong to one Line. Cross-Line duties are first-class when physically feasible.

## 3. Physical transition validation

Every adjacent duty task must expose whether the transition is feasible.

For example:

> Trip R12 ends Brno 09:12  
> next Trip R7 starts Praha 09:40
>
> **Duty infeasible**
>
> Fastest valid repositioning requires 3 h 04 min.

Do not show only “schedule conflict”.

The explanation can include:

- actual arrival location;
- next required start location;
- repositioning travel time;
- minimum turnaround;
- fueling/charging/service requirement;
- consist/shunting requirement;
- maintenance requirement;
- route/access/capacity requirement;
- crew-change dependency where relevant.

If several tasks overlap physically, the minimum turnaround calculation follows the canonical parallel/sequential rules from GAME_DESIGN. Explain the resulting minimum rather than simply summing all task durations.

Example:

> Arrival 10:42  
> passenger exchange: 4 min  
> fueling: 7 min  
> partially parallel  
> minimum next departure: 10:53

A planned next departure at 10:48 is therefore short by 5 min.

## 4. Multi-vehicle timeline

Provide a horizontal timeline for comparing several duties.

Example:

| Vehicle | 06:00 | 08:00 | 10:00 | 12:00 | 14:00 |
|---|---|---|---|---|---|
| Loco 104 | R12 → | turnaround | ← R12 | service | R7 → |
| Loco 117 | R4 → | R4 → | depot | maintenance | maintenance |
| Loco 121 | reserve | reserve | R9 → | R9 → | turnaround |

Use text/icons/patterns in addition to colour.

Useful scopes:

- today;
- next day;
- next 7 days;
- another selected period where useful.

The timeline is an inspection/planning surface, not a minute-by-minute mandatory timetable editor.

Clicking a block opens the exact Trip, maintenance job, movement, workshop/depot or duty subsection.

## 5. Automatic duty construction by default

The dispatcher normally constructs vehicle duties automatically from real Trips and constraints.

The player may apply high-level overrides already supported by the core mechanics:

- pin a specific vehicle/consist to a duty;
- force two compatible Trips into one duty;
- prevent two Trips from sharing a duty;
- require return to a chosen depot/base;
- insert a preferred fueling/maintenance stop;
- lock part/all of a generated duty;
- exclude a vehicle/model/fleet group from selected work where the assignment rules allow it.

Every override is revalidated.

If impossible, explain the exact reason:

> Cannot link Trip 014 and Trip 018.  
> Trip 014 ends in Brno 09:12.  
> Trip 018 starts in Praha 10:00.  
> Minimum physical repositioning time: 3 h 04 min.

Do not silently accept an impossible manual duty and fail at runtime.

## 6. Planned duty versus actual execution

Keep the planned duty and today's actual execution distinct.

Example:

> Planned asset: Loco 104  
> Actual from 09:40: Loco 117  
> Reason: technical failure of Loco 104

Do not rewrite history as though Loco 117 was always planned.

Retain:

- original planned assignment;
- actual replacement;
- time/effective task where substitution occurred;
- cause/reason;
- downstream replanning;
- resolved/cancelled future duty tasks.

A recalculated future duty may change, but completed historical work remains stable.

## 7. Delay propagation through the duty

When a current Trip is delayed, show the effect on later work using the same authoritative prediction as Trip/recovery systems.

Example:

> **R12 / Trip 014**
>
> expected arrival: +12 min
>
> Next task of same consist:
>
> R12 / Trip 021  
> planned turnaround: 18 min  
> physical minimum: 11 min  
> available after current delay: 6 min
>
> **Next Trip at risk**

If dispatcher recovery exists:

> Dispatcher is preparing Loco 117 as substitute.  
> Expected delay of next Trip after recovery: +2 min.

This is an estimate until execution occurs.

The workspace must distinguish:

- current Trip delay;
- consumed turnaround buffer;
- predicted downstream delay;
- confirmed substitution/recovery;
- unresolved risk.

Do not propagate a delay as a guaranteed fact if reserve substitution or another authorized recovery may still resolve it.

## 8. Maintenance and fueling interaction

Maintenance/fueling/service tasks are normal duty tasks and link to UI-D30.

A duty cannot use a vehicle while it is physically committed to maintenance.

From the duty timeline show:

- planned maintenance window;
- hard-limit conflict;
- preventive service target conflict;
- workshop/provider;
- travel to/from service;
- service completion estimate;
- next operational task.

A maintenance proposal does not consume the vehicle until it becomes a real scheduled commitment under the owning rules.

Similarly, fueling/charging consumes actual location/time/facility capacity. A duty cannot assume invisible refueling at an unsupported stop.

## 9. Crew duties remain aggregate

The **Crews** view does not assign named ordinary employees.

Show aggregate qualified duty blocks.

Example:

> **Train-driver duty A**
>
> Praha 05:30  
> R12 Praha → Brno  
> duty ends 09:20
>
> **Crew change — Brno**
>
> **Train-driver duty B**
>
> Brno 09:35  
> R12 Brno → Praha  
> duty ends 13:00

The same train/vehicle may continue while the crew block changes.

A crew duty can expose:

- qualification/category;
- Trip segments covered;
- start/end;
- breaks/rest;
- crew-change location;
- legal/safe duration margin;
- reserve capacity used;
- recovery state/problem.

No individual commuting-home, meal, name-by-name ordinary-worker scheduling or permanent named driver roster is introduced.

## 10. Aggregate crew-capacity overview

Show practical demand and reserve by crew category and selected period.

Example:

> **Train drivers**
>
> Peak requirement: 5.4 crew-equivalents  
> available qualified capacity: 7.0  
> reserve: 1.6
>
> **Conductors**
>
> Peak requirement: 3.2  
> available: 3.5  
> reserve: 0.3 — tight

The values must reconcile with company workforce planning.

Clicking an issue shows which duty blocks create the peak.

Do not imply 0.8 crew-equivalent is a literal partial person physically driving. It is aggregate staffing capacity for planning.

## 11. Crew change feasibility

A crew change is valid only at an operationally suitable location and within legal/safe duty constraints.

A conflict explanation can show:

> Duty would exceed allowed duration before the next valid crew-change point.

or:

> Brno change planned at 09:25, but delayed incoming Trip is now expected 09:41.  
> Replacement crew block starts another task at 09:45.

The dispatcher applies the company crew-recovery policy from GAME_DESIGN Section 32.7.

Possible authorized recovery remains:

- draw from qualified reserve;
- wait within configured maximum;
- reduce non-mandatory onboard staffing where permitted;
- cancel Trip if mandatory crew cannot be supplied.

The UI does not allow a Trip to depart without legally/technically mandatory crew.

## 12. Conflict view

The **Conflicts** view contains only meaningful problems in the selected horizon.

Examples:

> **3 conflicts in next 7 days**
>
> Critical — Loco 104  
> maintenance overlaps R12 / Trip 021
>
> Warning — Brno bus pool  
> 1 compatible reserve vehicle for 3 concurrent protected duties
>
> Warning — Train-driver capacity  
> shortage of 0.8 crew-equivalent Friday 06:00–08:30

Each row exposes:

- affected duty/vehicle/crew category;
- exact time range;
- cause;
- practical consequence;
- current handling state;
- direct route to relevant corrective workflow.

Group one root cause where appropriate; do not create one conflict row for every downstream Trip when one unavailable vehicle is the common cause.

If a conflict becomes a critical player-decision incident, UI-D24 handles the notification/pause behaviour.

## 13. Criteria-based future duties

Months/days ahead, a duty may be a **vehicle requirement** rather than a serial-number asset.

Show this explicitly:

> Intercity coach duty  
> 05:30–17:10  
> ≥50 seats  
> compatible with Lines A and B  
> fueling opportunity 10:20  
> concrete vehicle not yet assigned

This is valid planned coverage, not a missing vehicle, if the shared capacity ledger confirms compatible coverage.

At the preparation horizon, actual vehicle assignment appears without creating a second duty or reservation.

Pinned/fixed duties can show concrete asset identities earlier.

## 14. Rail consists and component continuity

For rail, distinguish:

- duty of a complete consist/trainset;
- locomotive-specific duty;
- individual coach/wagon component commitments where consist changes require it.

Do not double-count one train and all components as separate available duties.

A consist change or locomotive exchange must show:

- location;
- uncoupling/coupling/shunting requirement;
- replacement asset availability;
- required infrastructure;
- minimum time;
- resulting duty continuity.

A menu edit cannot instantaneously reform a consist.

## 15. Filtering and navigation

Useful filters include:

- vehicle/fleet group;
- Line/Pattern;
- depot/base;
- mode;
- task type;
- conflict only;
- maintenance involved;
- reserve involved;
- selected period.

From a Trip, vehicle, Line, maintenance job or event, **Open duty / Otevřít oběh** opens this workspace scoped to the relevant identity/time.

From the duty, direct links return to those exact objects.

Normal navigation does not move the camera; Locate remains explicit.

## 16. Historical and completed duties

Keep completed duties inspectable for operational analysis.

A historical duty preserves:

- planned tasks;
- actual tasks;
- substitutions;
- delays;
- maintenance/service;
- deadhead movements;
- crew changes;
- cancellations;
- recovery actions;
- final affected Trips.

Do not retroactively rewrite old planned assignments after duty regeneration.

Historical duty detail can support questions such as:

- Why did this vehicle end the day at another depot?
- Why was a later Trip delayed?
- Which substitute consumed reserve?
- Where did additional empty mileage come from?

## 17. Save/load and live refresh

Persist canonical duty identities/templates/requirements, locked overrides, actual assignments and completed execution through the owning systems.

After save/load:

- concrete duties do not duplicate;
- criteria-based requirements do not create fake assets;
- completed tasks remain completed;
- active Trip/duty continuity is preserved;
- maintenance/service bookings remain consistent;
- crew capacity is not double-reserved;
- historical planned-versus-actual assignment survives.

Live refresh preserves selected duty, filters, timeline zoom and scroll where practical.

Opening or filtering the workspace does not pause/resume, dispatch, assign a vehicle or create a crew duty.

## 18. Acceptance evidence to collect

| ID | Required scenario |
|---|---|
| DUTYUI-A01 | Build one vehicle duty containing Trips from two Lines, deadhead, turnaround, fueling and parking. All physical transitions are visible and feasible; the asset is not treated as permanently belonging to one Line. |
| DUTYUI-A02 | Attempt an impossible cross-city Trip link and a turnaround below physical minimum. Each conflict exposes exact location/time/transition causes rather than only a generic scheduling error. |
| DUTYUI-A03 | Use the multi-vehicle timeline across today and 7 days with running, reserve, maintenance and criteria-based future duties. Counts/assets are not duplicated and unknown concrete assignment stays explicit. |
| DUTYUI-A04 | Delay Trip A so the same vehicle's Trip B becomes at risk, then allow dispatcher substitution. Show consumed turnaround buffer, predicted impact and actual recovery without rewriting history. |
| DUTYUI-A05 | Substitute Loco 117 for planned Loco 104 mid-day. Historical planned and actual assignments remain separately inspectable after completion/save-load. |
| DUTYUI-A06 | Schedule preventive service and a hard-limit service conflict from UI-D30. Duty and maintenance views show identical commitments; one asset cannot be both in workshop and on Trip. |
| DUTYUI-A07 | Build aggregate train-driver/conductor duty blocks with a crew change. Vehicle continues while crew changes; no named ordinary employee or impossible change point is introduced. |
| DUTYUI-A08 | Create crew shortage and duty-duration overrun. Company recovery policy uses reserve/wait/reduced optional staff/cancellation only where permitted and never dispatches without mandatory crew. |
| DUTYUI-A09 | Force one root-cause vehicle failure affecting several later Trips. Conflict/event views group the cause while exact affected duties/Trips remain inspectable. |
| DUTYUI-A10 | Save/load with locked duty overrides, an active Trip, future criteria-based assignment, ongoing maintenance and crew blocks. No duplicate assignment/reservation/task appears; CZ/EN and enlarged UI remain usable. |

## 19. Decision record

| ID | Decision | Status |
|---|---|---|
| UI-D31 | Operations workspace with Vehicles / Crews / Conflicts views, physical vehicle-duty timelines, explainable transitions, planned-versus-actual execution, aggregate crew-duty blocks and automatic dispatcher construction with validated high-level overrides | CONFIRMED on 2026-09-30 |

UI-D31 complements UI-D01–UI-D30. GAME_DESIGN Sections 32.6–32.7 remain authoritative for duty construction, turnaround, preparation, fleet assignment, crew capacity and disruption recovery.
