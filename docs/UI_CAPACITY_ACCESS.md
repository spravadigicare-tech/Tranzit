# Tranzit — Infrastructure capacity and access UI

> **Status: CONFIRMED UI DIRECTION — UI-D26, 2026-09-30.** The player accepted one coordinated capacity/access workflow driven by a Line/Service Pattern requirement rather than manual purchase of individual track sections; explicit request/offer/accepted states; practical impact of alternative time windows; multi-owner summaries; and a company-wide overview of active capacity/access agreements. Exact visual dimensions, heatmap treatment, column widths and localized labels remain design work. This specification is not an implemented or tested UI.

Read with [UI_UX_DESIGN.md](UI_UX_DESIGN.md), especially UI-D09 (exact-object links), UI-D11/UI-D12 (Line planning and active Lines), UI-D15 (minimalism/tooltips), UI-D17 (commercial context) and UI-D25 (concrete Trip detail). [GAME_DESIGN.md](GAME_DESIGN.md), Sections 13.2–13.2.1, 19–20 and 32.2–32.4, owns rail/station capacity products, the canonical Capacity Order, access agreements, timetable construction and dynamic platform/track assignment. [CONTRACT_CANCELLATION.md](CONTRACT_CANCELLATION.md) owns ordinary early rail/station capacity release settlement. This document specifies presentation and workflow, not a second capacity ledger or a new timetable simulator.

## 1. One coordinated Capacity Order

The normal player workflow begins from a real service requirement:

**“Operate this Service Pattern with this calendar/frequency/window” → determine required route and station capacity → obtain compatible offers/rights → explicitly accept the result.**

The player should not normally purchase every line section, junction and station call separately.

Open **Capacity and access / Kapacita a přístupy** contextually from:

- a Line or Service Pattern's Rights and capacity card;
- the Contract Planner when a proposed transport solution requires capacity;
- a concrete dependency/problem link;
- the company-wide Operations capacity/access overview.

The contextual header always states the owning planning scope: Line, Service Pattern/version, validity period/calendar and requested service level/frequency. A generic capacity window must not hide which service or contract requirement generated the request.

The workflow reuses the canonical Capacity Order. It expands the selected Service Pattern into all required rail-section and station-call rights and coordinates the involved owners. No UI action creates a parallel reservation or a second source of truth.

## 2. Compact order overview

The order summary should immediately answer:

1. Which service and period is being protected?
2. Which required owners/sections/stations are covered?
3. Which dependency is still unresolved?
4. What accepted/offered timing does this imply?
5. What will it cost and for how long?

Illustrative presentation:

> R12 Praha–Brno · Weekdays
>
> Requested: 1 departure / 60 min
>
> Validity: Month 4 → Month 12
>
> Route capacity: secured
>
> Praha station calls: secured
>
> Pardubice: awaiting offer
>
> Brno station calls: secured
>
> **1 dependency blocks protected activation**

This is a summary of authoritative states. “Route secured” does not mean every numbered track/platform is permanently assigned, and “station capacity secured” means station-call capacity, not ownership of a specific platform.

## 3. Request, offer and active commitment are different states

Keep the commercial/operational lifecycle explicit. At minimum distinguish:

- **Draft requirement** — still only part of an uncommitted Line/contract plan;
- **Requested / submitted** — a real capacity request has been sent to the relevant owner(s) where the game models that step;
- **Awaiting owner / pending** — no binding compatible result yet;
- **Offered / proposed** — owner has returned a compatible offer/time window/terms, not yet accepted by the player;
- **Accepted / committed future** — agreement is binding for its effective future period;
- **Active** — agreement is currently valid/usable for the displayed date;
- **Expiring / renewal pending / renewal blocked** — current term is active but the next term is unresolved;
- **Released / expired / cancelled / refused** — no current right for the affected future scope.

Exact labels can be refined but must not collapse an offer into an active reservation.

A saved Line draft alone does not submit a Capacity Order. Conversely, a separately accepted capacity agreement remains a real cost/obligation even if the Line draft is later changed or deleted.

Repeated clicks, multiple open windows and save/load cannot create duplicate capacity commitments.

## 4. Task-based capacity cards

Use independently openable groups, not a wizard:

| Card | Content |
|---|---|
| Route and owners / Trasa a vlastníci | Required corridor/sections, infrastructure owners, physical/access compatibility, missing infrastructure connection agreements and any owner refusal |
| Time capacity / Časová kapacita | Requested frequency/windows, offered/accepted arrival/departure windows, tolerance and resulting planned midpoint times |
| Stations and terminals / Stanice a terminály | Required station-call capacity, validity and compatibility; no default dedicated numbered platform promise |
| Price and terms / Cena a podmínky | Reservation fees, expected per-use charges, access class/priority, important restrictions and per-owner breakdown |
| Validity and renewal / Platnost a obnovení | Effective dates/calendar, notice/expiry, Auto-renew, future renewal state and any next-term blockers |

The cards adapt to the service. A simple unconstrained road access case does not need railway slot controls merely because the screen is shared. V1 rail remains the main capacity-order use case; road access/congestion retains its simpler mechanics.

Hard blockers remain visible in the overview. Secondary details such as why a slot window is unusually wide/tight, tolerance calculation inputs or detailed owner terms can live in tooltips/opened detail.

## 5. Requested time, accepted window and planned time

Never show one timestamp as if it represented all stages.

Distinguish:

- player's preferred/anchor time or requested broad operating window;
- owner-offered arrival/departure slot window;
- accepted slot window and tolerance;
- planned/published midpoint time derived under the timetable rules;
- actual Trip time later during execution.

Example:

> Preferred departure: 10:20
>
> Offered slot: 10:28–10:34
>
> Resulting planned departure: **10:31**
>
> Difference from preference: +11 min

When the offer materially shifts the service, show the **practical impact before acceptance**, such as:

- connection becomes invalid or weaker;
- another planned passenger transfer becomes more or less viable;
- vehicle duty/turnaround becomes infeasible;
- additional vehicle/crew may be needed;
- contract/SLA window is missed;
- station/route access conflict appears elsewhere;
- service frequency becomes uneven;
- expected journey/operating cost changes where the simulation can support the estimate.

Use the same Line/Trip/duty/connection feasibility rules rather than a separate UI approximation. A consequence is an estimate until the final capacity and service plan are committed.

Offer actions can include **Accept**, **Review alternatives**, **Find nearest available capacity**, shift/reduce frequency or another already supported route/station option. Do not require manual signalling-block reconstruction.

## 6. Capacity timeline/availability presentation

For the relevant route/station and selected period, use a compact timeline/heatmap or equivalent readable view for states such as:

- available;
- tight;
- unavailable;
- owner refused access;
- already reserved/committed;
- unknown/not yet evaluated.

A colour heatmap alone is insufficient; provide text/icon legend and accessible details.

The view should support inspecting why the complete service cannot be supplied without forcing the player to read every section. Expand only the problematic or selected segment/owner by default.

Capacity shown as “free” must be scoped: physical spare occupancy, sellable capacity, the player's existing contractual right and compatible capacity for this service are different concepts. Do not imply the player can use another operator's or owner's spare physical space without access rights.

## 7. Multiple infrastructure owners in one order

A Service Pattern crossing several owners remains **one coordinated Capacity Order from the player's perspective**, with inspectable underlying agreements.

Example:

> Infrastructure owner A — accepted
>
> Infrastructure owner B — awaiting response
>
> Brno terminal — offer ready

Show:

- one overall readiness state;
- total expected reservation cost;
- total expected per-use charges where meaningful;
- per-owner breakdown;
- each owner's current lifecycle state;
- route/station segment affected by refusal or alternative offer;
- applicable effective dates and access class.

The Service Pattern is not fully protected until all required components are secured for the relevant scope.

One owner's acceptance does not authorize use of another owner's infrastructure. A refusal cannot be hidden behind an overall average readiness score.

## 8. Station-call capacity, not dedicated platforms

Station capacity and corridor capacity are separate real constraints and both belong in the coordinated workflow.

Default station rights are **station-call slots**, not permanently numbered platforms. The order can show the required calls, accepted windows, access product, station services/capabilities and expected occupancy/dwell separately.

Actual compatible platforms/tracks are dynamically assigned to each concrete Trip under the station rules. Before assignment, Trip and station views show Pending/Unknown rather than inventing a platform.

If an exceptional contract truly grants a dedicated platform/track or a physical service requires one, show that explicit exceptional right. It is not the default capacity-product model.

## 9. Company-wide Capacity and access overview

Provide a separate **Operations → Capacity and access / Provoz → Kapacita a přístupy** overview of the company's real active/future agreements and dependencies.

The default list helps find:

- paid capacity currently unused or materially underused;
- agreements approaching expiry;
- Auto-renew scheduled/pending/blocked;
- capacity whose next term no longer covers its linked service;
- constrained/tight corridors or stations;
- Lines/Patterns dependent on each agreement;
- contracts/Shipments dependent on the protected service;
- accepted future capacity not yet active;
- released/expired capacity retained in history.

Each row shows owner, scope/corridor/facility, product/access class, validity, recurring reservation cost, usage or linked service context, renewal state and main issue. Avoid one generic utilization score when section/station/time-window detail is what matters.

Filters can include owner, rail/station/facility access type, active/future/expiring, used/underused, Line/Pattern and renewal state.

Direct links open the agreement/order, affected Line/Pattern, station/terminal, owner or Finance source where available.

## 10. Underused capacity and strategic review

The overview may flag a capacity agreement as worth reviewing when actual or planned service uses materially less than the protected commitment.

This is a **decision aid**, not automatic cancellation.

Explain:

- what is paid for;
- what services currently depend on it;
- how much future committed service uses it;
- whether the apparent underuse is temporary/seasonal;
- next notice/renewal date;
- expected cost to keep versus applicable cost to release/reduce where known.

Do not call capacity “wasted” solely because no train is physically occupying it at this instant. Protected future windows and seasonal obligations are real value/commitments.

## 11. Renewal, reduction and early release

Auto-renew follows the canonical shared renewal rules. The UI shows current term separately from:

- scheduled but not yet committed renewal;
- already committed future term;
- renewal awaiting owner;
- renewal needing player approval;
- renewal blocked/refused.

Turning Auto-renew off does not cancel the active term.

For reduction/early release, open an explicit impact/settlement review under [CONTRACT_CANCELLATION.md](CONTRACT_CANCELLATION.md). Show:

- exact calls/windows/agreements and owners affected;
- effective release date;
- per-owner fee/settlement;
- one total immediate settlement;
- prepaid credit/refund and outstanding charges;
- future reservation cost avoided;
- affected Lines/Patterns;
- customer/passenger/freight obligations and connections;
- remaining rights after a partial reduction.

Released capacity returns to the owner. The player cannot resell or transfer rail/station slots to another operator.

Releasing a slot changes future rights only. It does not stop a currently running train, teleport it, cancel customer contracts, delete a Line or automatically free physically occupied infrastructure.

If the player suspends a Line, show the ongoing cost of retained capacity and offer the existing keep/release/reduce choices rather than silently cancelling or retaining years of slots.

## 12. Owned infrastructure and third-party rights

Where the player owns infrastructure, distinguish:

- capacity reserved for the player's own services;
- capacity already sold/committed to third parties;
- operational reserve;
- remaining sellable capacity.

Ownership does not permit the player to displace a third party's stronger already-contracted right after it has been sold.

Where the player is the buyer/user of foreign infrastructure, show only terms and capacity information the company is entitled to know. Do not reveal competitors' private agreements or internal owner economics.

Private owners may refuse access under the core rules. “Physical room exists” does not mean “access can be bought”.

## 13. Map integration

From a Capacity Order or company overview, provide **Show on map** to highlight:

- requested/accepted route;
- involved stations;
- owner boundaries where useful;
- missing/refused capacity segment;
- tight sections;
- affected alternative route when comparing an offer.

This may use the confirmed UI-D21 capacity/ownership layers. Map inspection does not modify the order.

Changing a Line route invalidates/rechecks affected capacity dependencies but must not silently cancel already accepted agreements. Existing rights remain real contracts until explicitly amended/released/expired.

## 14. Save/load, live changes and state safety

Persist order/agreement identity, owner breakdown, request/offer/acceptance versions, validity, renewal state, slot windows/tolerance, linked Service Pattern/version and settlement history.

After save/load:

- an accepted order remains accepted;
- an offer does not become active;
- a pending owner result is not regenerated as a duplicate;
- a released slot is not recreated;
- already charged acceptance/release settlements are not posted twice;
- Line readiness revalidates stale dependencies without manufacturing new capacity.

If infrastructure changes, an owner alters a still-unaccepted offer, or a future service version changes, mark affected evaluations stale and explain the changed dependency. Do not rewrite historical agreements.

Opening, filtering, hovering or comparing alternatives does not reserve/release capacity, submit an order, change pause/speed or edit the Line.

## 15. Acceptance evidence to collect

| ID | Required scenario |
|---|---|
| CAPUI-A01 | From a Service Pattern, open one Capacity Order covering multiple rail sections and station calls across several owners. The default view remains service-level, with drill-down rather than one manual purchase per section. |
| CAPUI-A02 | Request a preferred time that cannot be supplied. Show an alternative slot window, resulting midpoint time and concrete connection/duty/SLA impacts before acceptance; no offer becomes binding by merely viewing it. |
| CAPUI-A03 | Test Draft, Requested/Pending, Offered, Accepted future, Active, Expiring/Renewal pending and Released/Expired states through save/load. No state is silently promoted and repeated clicks do not duplicate reservations/payments. |
| CAPUI-A04 | Confirm station-call capacity at a constrained station, then dynamically assign/change the actual platform for a Trip. The Capacity Order never implies a permanent numbered platform unless an explicit exceptional right exists. |
| CAPUI-A05 | Open the company-wide overview and identify unused/underused, expiring, renewal-blocked and constrained agreements. Direct links reach exact Lines/Patterns/stations/agreement/finance details without creating new commitments. |
| CAPUI-A06 | Reduce/release part of a multi-owner recurring order. Show per-owner and total settlement, prepaid reconciliation, future cost avoided and affected services; released rights return to owners and no customer/Line is silently cancelled. |
| CAPUI-A07 | Suspend a Line with paid capacity. Verify keep/release/reduce choices, ongoing retained cost and fresh capacity requirement if released capacity is later needed again. |
| CAPUI-A08 | Test player-owned infrastructure with own reserved capacity and guaranteed third-party rights. Ownership does not override already contracted higher-priority access. |
| CAPUI-A09 | Change route/service calendar after capacity was accepted. Preserve the real agreement, mark mismatched readiness/dependencies and require explicit amendment/release rather than silently rewriting the contract. |
| CAPUI-A10 | Verify CZ/EN, enlarged UI, map highlighting, paused/running inspection and live refresh. Browsing timelines/heatmaps or alternatives never reserves/releases capacity or changes time. |

## 16. Decision record

| ID | Decision | Status |
|---|---|---|
| UI-D26 | One coordinated Capacity Order driven by Service Pattern requirements, explicit request/offer/accepted states, practical timing-impact review, multi-owner breakdown and a company-wide Operations overview of actual capacity/access agreements | CONFIRMED on 2026-09-30 |

UI-D26 complements UI-D01–UI-D25. It does not change capacity products, slot-priority rights, dynamic track/platform assignment, timetable midpoint rules, access ownership, cancellation settlement or renewal mechanics.
