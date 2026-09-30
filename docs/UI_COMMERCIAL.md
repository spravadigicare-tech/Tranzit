# Tranzit — Commercial opportunities, offers and contracts UI

> **Status: CONFIRMED UI DIRECTION — UI-D17, 2026-09-30.** The player approved one commercial area with Opportunities, Offers and Contracts; compact list-based overviews; editable saved offer drafts; and direct navigation from commercial commitments into Shipments, Transport Plans, Lines, Trips and physical operation. Exact wording, columns and visual dimensions remain design work. This specification is not an implemented or tested UI.

Read with [UI_UX_DESIGN.md](UI_UX_DESIGN.md), especially UI-D09 (contextual object links), UI-D15 (global minimalism/tooltips/consistency), shared floating-window behaviour and pause rules. [GAME_DESIGN.md](GAME_DESIGN.md), especially Sections 10–12, owns demand, Opportunity Board rules, Contract Planner, contracts, Transport Plans, cargo and service endpoints. [CONTRACT_CANCELLATION.md](CONTRACT_CANCELLATION.md) owns proportionate cancellation and early capacity release. This document owns presentation only.

## 1. Commercial workspace

Open **Business / Obchod** from the fixed bottom bar into one movable/resizable commercial window with three top-level views:

1. **Opportunities / Příležitosti** — discoverable real market opportunities;
2. **Offers / Nabídky** — saved drafts and already submitted bids/offers;
3. **Contracts / Smlouvy** — binding accepted agreements and their operational fulfilment.

Keep these states visually and semantically separate. An opportunity is not yet a company commitment. A saved offer draft is not submitted. A submitted bid is not a won contract. A contract is not the same object as a Line, Shipment or Trip.

Use compact lists as the default. Do not present the three views as giant dashboard tiles. Preserve filters, sorting, selection and scroll during live refresh. Important object/customer/Line/Shipment references use exact-object links under UI-D09.

## 2. Opportunities

### 2.1 Opportunity Board

Implement the existing Opportunity Board as a dense but readable list that scales from a small local company to a larger operator. Only opportunities the company can legitimately discover under the simulation rules appear.

The default row shows only the information needed to decide whether to inspect it:

- customer/authority;
- passenger/cargo purpose and cargo family where relevant;
- origin and destination;
- one-off/recurring/tender character;
- important deadline/start date;
- required volume/capacity in real units;
- offered or indicative commercial value where actually known;
- concise feasibility state;
- status such as new/viewed/bid submitted/expiring.

Use tooltips for secondary qualification requirements, margin assumptions, licence details and the reason behind a feasibility label. Material submission deadlines or blockers remain visible and are not tooltip-only.

Filters should cover the existing relevant Opportunity Board dimensions without forcing all controls onto one line. Group them by task, such as transport, geography/customer, commercial type, timing/value and feasibility. Support clear-all. Search and sort are visible. More advanced saved filter presets can remain a later refinement if not otherwise required.

### 2.2 Feasibility summary

A row can say, for example, **Ready**, **Requires investment**, **Missing licence/access**, **Capacity conflict** or **Not yet evaluated**, using the underlying structured reasons. This is an aid, not an automatic bid decision.

Hover/focus explains the main concrete reasons. Clicking the status opens the relevant evaluation/detail. Never calculate a fake percentage of readiness or hide uncertainty. Customer forecast volume remains labelled as forecast unless contract terms guarantee it.

## 3. Opportunity detail and offer drafting

Opening an opportunity keeps the source list available and opens/focuses its detail. Show a compact commercial summary first: customer, requirement, dates, guaranteed versus estimated quantities, offered/bid price, SLA, bonuses/penalties, qualifications and deadline.

### 3.1 Non-linear offer cards

Use independently openable cards, not a mandatory Next/Back wizard. The player may work on an offer over time and in any order.

Suggested functional groups:

| Card | Purpose |
|---|---|
| Terms / Podmínky | Customer requirement, quantities, dates, SLA, bonuses, penalties, exclusions and qualifications |
| Transport solution / Přepravní řešení | Proposed Transport Plan, modes, own/external legs, existing/new Lines, endpoints and transfer/storage points |
| Capacity and resources / Kapacita a zdroje | Fleet, staff, facilities, handling/storage, licences, infrastructure/station access and other dependencies |
| Price and economics / Cena a ekonomika | Bid/accepted price basis, expected costs, margin estimate, assumptions, risk and sensitivity where data exists |
| Commitments and readiness / Závazky a připravenost | What is merely planned, pending, actually secured or blocking submission/acceptance |
| Submission / Podání nabídky | Deadline, current offer version, required confirmation and actual submission action |

Exact card names can be refined, but preserve the task grouping and non-linear editing.

A missing route or customer endpoint may prevent full costing without preventing the player from entering a price target or proposed fleet requirement. Mark dependent calculations as unavailable/stale rather than clearing other work.

### 3.2 Offer draft versus submitted offer

Provide **Save draft / Uložit návrh** separately from **Submit offer / Odeslat nabídku**.

A draft:

- survives closing windows and campaign save/load;
- may be incomplete;
- creates no customer commitment merely by being saved;
- does not reserve capacity, buy vehicles, build facilities or sign third-party agreements;
- may link to separately accepted real purchases/access agreements that remain binding independently of the draft.

Submission is explicit and revalidated against the current opportunity deadline/state. Show the submitted commercial terms and material assumptions before confirmation. Repeated clicks cannot create duplicate bids.

After submission, retain the exact submitted version for history. Later editing creates a new permissible revision/amendment proposal only when the commercial process allows it; it must not silently rewrite the submitted bid. If the deadline passes, the draft can remain for history/reuse but cannot be presented as successfully submitted.

Show real states such as Draft, Submitted, Awaiting decision, Needs response, Won/Accepted, Rejected, Withdrawn or Expired only when supported by actual simulation state. Do not fabricate competing bids or a customer decision just to make the UI busy.

## 4. Contracts

### 4.1 Contract overview

The Contracts view lists binding agreements with:

- customer and contract identity;
- passenger/cargo purpose;
- active term/start/end;
- current fulfilment state;
- next material obligation or deadline;
- actual warning/breach/renewal state;
- selected-period revenue/cost/result where available.

Do not reduce contract health to an unexplained green/red score. A concise status may summarize the situation, but tooltip/detail must expose the actual causes.

Opening a contract shows a compact live summary: what the company promised, what is currently happening, the next required action and any player decision. Keep automatic dispatcher/manager recovery distinct from unresolved player action.

### 4.2 Contract cards

Use task-based cards:

| Card | Content |
|---|---|
| Terms and SLA / Podmínky a SLA | Binding quantities, service windows, guarantees, bonuses, penalties, exclusions, effective dates |
| Transport Plan / Přepravní plán | Current versioned fulfilment chain and each physical/contractual leg |
| Shipments / Zásilky | Current, upcoming and historical executions/consignments linked to the contract |
| Capacity and dependencies / Kapacita a závislosti | Reserved service capacity, Lines/Patterns, fleet coverage, endpoints, access, external carrier dependencies |
| Performance / Plnění | Delivered quantities/services, delays, SLA outcomes, causes and recovery history for a selected period |
| Finance / Finance | Invoiced/earned amounts, costs, penalties/bonuses and period-labelled result without mixing forecasts and actuals |
| Renewal and lifecycle / Obnovení a životní cyklus | Auto-renew status, expiry/notice dates, amendments, renegotiation, cancellation/termination actions and consequences |

Keep only relevant cards for the agreement type; one-off jobs need not display an empty recurring-renewal dashboard.

## 5. Transport Plan and operational linkage

The commercial UI must connect the promise to its real execution. In the Transport Plan card, show the ordered origin-to-destination chain as a compact leg list/flow that reflows with window size. Do not require a giant node editor.

For each leg show:

- origin/destination endpoint;
- execution type: existing Line/Pattern, new Line proposal, own ad-hoc movement, external carrier or customer-provided leg;
- responsible operator;
- required/allocated capacity;
- timing/transfer state;
- relevant endpoint/access dependency;
- current problem when material.

Each specific Line, Pattern, Trip, terminal, external order and other inspectable object is directly clickable. A plan leg does not pretend that cargo has physically moved. Reservation, readiness, loading and in-transit states remain distinct.

Where an existing Line is used, expose compatible available/committed capacity using the canonical ledgers. Do not show only nominal tonnes/seats if the relevant cargo/passengers cannot use that capacity. A contract allocation is not duplicated because it appears in both commercial and Line windows.

## 6. Shipments inside a contract

The contract includes a compact Shipment list with filters for current/upcoming/completed/problematic items. Each Shipment remains one commercial consignment even when split into several CargoLots or Trips.

The row should identify:

- quantity and commodity/passenger-group requirement;
- origin/destination;
- current high-level fulfilment state;
- next deadline/leg;
- delivered versus remaining quantity;
- material exception or recovery state.

Clicking opens the Shipment detail; the commercial list itself must not imply that reserved quantity is already loaded or delivered. Split lots remain inspectable from that detail with their actual physical locations and next allocations.

A missed transfer, rebooking or external recovery does not erase the original failure/SLA consequence. Preserve direct links from the commercial obligation to the responsible Trip, Line, vehicle, terminal or partner order where the simulation knows it.

## 7. Contract lifecycle actions

Keep **Amend/Renegotiate**, **Renew/Auto-renew**, **Do not renew**, **Suspend/replace service where contractually relevant**, and **Terminate/Cancel contract** visually distinct.

Never make cancellation a casual toggle. Before a binding change, show:

- exact agreement/scope affected;
- effective date;
- contract/customer consequences;
- termination/cancellation liability where applicable;
- prepaid/outstanding amounts when relevant;
- operational dependencies and capacity that remain or can be released;
- Shipments/Lines/services needing recovery.

Follow CONTRACT_CANCELLATION for ordinary early release/cancellation calculations. Turning Auto-renew off is not early cancellation. Ending a Line does not automatically end the customer contract, and ending a contract does not silently demolish infrastructure or teleport/remove cargo.

## 8. Minimalism, tooltips and permissions

Apply UI-D15 throughout:

- lists show decisive commercial facts first;
- tooltips explain terms, calculation basis, feasibility causes and SLA/status contributions;
- complete terms, histories and editable policies live in opened details;
- deadlines, binding prices, penalties, blockers and confirmation consequences remain visible.

Do not reveal competitors' private bids, internal cost assumptions or confidential contracts unless gameplay rules explicitly make that information available. A public tender can reveal its public terms without exposing rival submissions.

Disabled Submit/Accept actions explain the blocker and link to the corrective workflow where possible. A tooltip or link never submits a bid, accepts a contract, acknowledges a breach or changes simulation time.

## 9. Acceptance evidence to collect

These scenarios extend the UI evidence contract; they are not claims of implementation.

| ID | Required scenario |
|---|---|
| COMUI-A01 | Browse a large Opportunity Board with combined filters/sort/search. Known versus undiscovered opportunities follow commercial-coverage rules; visible feasibility states expose real reasons without fake percentages or hidden essential deadlines. |
| COMUI-A02 | Open an opportunity, edit offer cards out of order, save an incomplete draft, close/reopen and save/load. No customer commitment, resource reservation or purchase occurs from drafting alone. |
| COMUI-A03 | Submit after a fresh validation, then verify the submitted version is preserved and duplicate clicks cannot create duplicate bids. Test expiry, rejection and a permitted revision without rewriting history. |
| COMUI-A04 | Open an active contract with linked Transport Plan, Lines, Shipments, Trips and facilities in several floating windows. Exact-object links preserve identity/context and no duplicate capacity/cargo state is created by navigation. |
| COMUI-A05 | Execute a split multi-leg Shipment. Contract overview, Shipment row and Plan legs agree with authoritative physical/capacity state; reserved, loaded, in-transit and delivered quantities are not conflated. |
| COMUI-A06 | Trigger customer-side delay, carrier-side missed transfer and external recovery. Commercial obligations and SLA consequences stay traceable through replanning rather than disappearing when cargo is rebooked. |
| COMUI-A07 | Exercise renewal/non-renewal and early termination. Show notice/effective dates, cancellation settlement and remaining operational dependencies; no unrelated Line, slot, cargo or asset is silently deleted. |
| COMUI-A08 | Verify CZ/EN, enlarged UI, tooltips/focus access, running/manual-pause/critical-pause use and save/load. Opening commercial windows or hovering explanations never changes time or executes a commercial command. |

## 10. Decision record

| ID | Decision | Status |
|---|---|---|
| UI-D17 | One commercial workspace with Opportunities, Offers and Contracts; compact list views; non-linear persistent offer drafts separated from submission; contract views directly linked to Transport Plans, Shipments, Lines, Trips and real operational fulfilment | CONFIRMED on 2026-09-30 |

UI-D17 complements UI-D01–UI-D16. It does not change contract economics, customer behaviour, capacity priority, cargo identity or cancellation rules.
