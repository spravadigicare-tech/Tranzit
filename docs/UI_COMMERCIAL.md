# Tranzit — Commercial opportunities, offers and contracts UI

> **Status: CONFIRMED UI DIRECTION — UI-D17, refined 2026-10-01.** The player approved one commercial area with Market, Opportunities, Offers and Contracts; compact list-based overviews; editable saved offer/tender drafts; transparent market intelligence; and direct navigation from commercial commitments into Shipments, Transport Plans, Lines, Trips and physical operation. Exact wording, columns and visual dimensions remain design work. This specification is not an implemented or tested UI.

Read with [UI_UX_DESIGN.md](UI_UX_DESIGN.md), especially UI-D09 (contextual object links), UI-D15 (global minimalism/tooltips/consistency), shared floating-window behaviour and pause rules. [GAME_DESIGN.md](GAME_DESIGN.md), especially Sections 10–12, owns demand, Opportunity Board rules, Contract Planner, contracts, Transport Plans, cargo and service endpoints. [CONTRACT_CANCELLATION.md](CONTRACT_CANCELLATION.md) owns proportionate cancellation and early capacity release. This document owns presentation only.

## 1. Commercial workspace

Open **Business / Obchod** from the fixed bottom bar into one movable/resizable commercial window with four primary commercial views:

1. **Market / Trh** — structural local supply/demand/reference-price intelligence before a concrete customer job exists;
2. **Opportunities / Příležitosti** — discoverable real jobs, customer requests and public/private tenders;
3. **Offers / Nabídky** — saved drafts and already submitted bids/offers;
4. **Contracts / Smlouvy** — binding accepted agreements and their operational fulfilment.

Other Business navigation entries such as Shipments, Procurement & suppliers and Tariffs & tickets remain separate canonical workspaces rather than being folded into these four views.

Keep these states visually and semantically separate. An opportunity is not yet a company commitment. A saved offer draft is not submitted. A submitted bid is not a won contract. A contract is not the same object as a Line, Shipment or Trip.

Use compact lists as the default. Do not present the three views as giant dashboard tiles. Preserve filters, sorting, selection and scroll during live refresh. Important object/customer/Line/Shipment references use exact-object links under UI-D09.

## 2. Market / Trh

The Market view helps the player discover **where transport demand may emerge** before a concrete contract/opportunity exists.

It presents known local commodity-market information derived from the simulated economy.

### 2.1 Commodity overview

Default rows can show:

- commodity;
- selected city/locality market;
- local production;
- local consumption;
- surplus/deficit;
- local reference price;
- recent price trend;
- known major producers/buyers where information permits.

The view must distinguish real known values from estimates/stale information.

### 2.2 Commodity detail and map

Opening a commodity automatically activates the corresponding commodity-market analysis on the **main map** while the Market window remains open. The map presents local **surplus/deficit and reference price together** for each visible/known city/locality market; exact glyph, shading and label treatment remain visual implementation work.

One city/locality normally corresponds to one commodity market and one local reference-price signal. Large cities may contain several evolving **economic centres/neighbourhoods**—for example centre, residential districts, industrial zones or freight clusters—but these are internal spatial/economic nodes, not separate price markets. Firms/facilities remain real physical origins/destinations and deliveries between two centres inside the same city still require physical transport.

The Market detail may show the city's internal economic centres as context: where known producers, consumers, jobs, population and freight/passenger hubs are concentrated. Do not assign a second reference price to those centres or imply that a new district creates a new market.

The same information can therefore be inspected spatially across the map.

Example:

> Jihlava — timber  
> Production: 420 t/month  
> Consumption: 160 t/month  
> Net surplus: +260 t/month  
> Reference price: 18 money/t
>
> Brno — timber  
> Production: 80 t/month  
> Consumption: 390 t/month  
> Net deficit: −310 t/month  
> Reference price: 27 money/t

This does not guarantee that any specific firm will sign a contract or that a route is profitable.

The displayed price is a **local reference price**, not an automatic buy/sell price. When a concrete seller or buyer is opened, show the relevant reference alongside the actual quoted/negotiated commercial terms where known, without exposing private reservation prices or margins.

Market values are dynamic. If real freight flows reduce a surplus at the origin and a deficit at the destination, the displayed local prices and imbalance must update accordingly. A corridor that was initially highly attractive can become less attractive as it successfully integrates those markets.

Where legitimate information exists, the player can drill into known producers/buyers and their company detail.

### 2.3 Transport-market signal

Where enough information exists, the Market view can also show a transport-market perspective for a corridor/commodity, such as:

- known or estimated freight demand volume;
- known competing carrier/service presence;
- observed/known transport-rate range;
- currently constrained or abundant transport capacity.

These are reference signals, not a hidden profitability score.

Avoid labels such as "best route" or opaque opportunity percentages. Show the underlying quantities/prices/capacity context instead.

### 2.4 Relationship to Opportunities

Market intelligence and Opportunities are separate:

- **Market** shows structural supply/demand/price imbalances;
- **Opportunities** shows concrete jobs, tenders and offers from real counterparties.

Actions from Market can navigate to known producers/buyers, search/filter Opportunities for that commodity/area, or start a relevant planning workflow where one exists. They must not fabricate a customer contract.

Three player paths are supported:

1. **React** to an already discoverable Opportunity.
2. **Propose a connection** between a legitimately known producer and buyer, pairing their real supply/demand with a transport offer. The seller and buyer still decide their own commodity transaction; the player does not purchase/resell the commodity as a speculative trader.
3. **Prepare a strategic corridor/service** from the observed market imbalance and let real firms use it if it becomes a competitive transport option.

If aggregate market intelligence shows a deficit but the player's company does not know a concrete buyer, show that information gap instead of revealing the hidden firm. Operational commodity purchases for the player's own coal, electricity, fuel, parts, construction materials and similar needs continue through Procurement & suppliers.

## 3. Opportunities

### 3.1 Opportunity Board

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

### 3.2 Feasibility summary

A row can say, for example, **Ready**, **Requires investment**, **Missing licence/access**, **Capacity conflict** or **Not yet evaluated**, using the underlying structured reasons. This is an aid, not an automatic bid decision.

Hover/focus explains the main concrete reasons. Clicking a missing legal requirement opens the exact market-entry/licence/permit dependency in the confirmed UI-D33 [UI_LICENCES_MARKETS.md](UI_LICENCES_MARKETS.md); physical infrastructure-access gaps continue to use their owning capacity/access workflow. Clicking other statuses opens their relevant evaluation/detail. Never calculate a fake percentage of readiness or hide uncertainty. Customer forecast volume remains labelled as forecast unless contract terms guarantee it.

## 4. Opportunity detail and offer drafting

Opening an opportunity keeps the source list available and opens/focuses its detail. Show a compact commercial summary first: customer, requirement, dates, guaranteed versus estimated quantities, offered/bid price, SLA, bonuses/penalties, qualifications and deadline.

### 4.1 Non-linear offer cards

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

### 4.2 Offer draft versus submitted offer

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


### 4.3 Public tender proposal and scoring

A public/state/municipal tender is an Opportunity, not a separate top-level screen. It is clearly typed/filterable as **Public tender / Veřejný tendr**.

The tender detail shows before bidding:

- contracting authority and public need;
- mandatory served points/corridor and mode where prescribed;
- minimum frequency/capacity;
- required operating window, start date and contract duration;
- maximum journey time or other service-level constraint where applicable;
- required comfort/quality where applicable;
- qualification/history thresholds;
- published scoring factors and their weights;
- public contract/subsidy terms and material penalty/termination rules.

The player submits a **concrete service plan** using the same Line/Pattern proposal model as normal planning. A bid can extend an existing Line, prepare a future version or propose a new Line/Pattern. It may choose a different operational solution from another bidder, but the UI must block submission until every mandatory tender condition is satisfied or legitimately planned to be satisfied by the required start date.

Scoring is transparent. **Price/requested operating subsidy has the largest normal weight**, while published tenders can also consider:

- operating reliability for the relevant mode (for example rail versus road);
- company commercial reliability, such as contract fulfilment, promised launch dates and timely payments/fees;
- comfort/service quality from the concrete proposed service where relevant;
- company reputation.

Do not merge these into an unexplained single reputation/reliability number. New carriers or a carrier entering a new mode use the mildly positive baseline defined by the core design until real history exists.

Before the deadline, rival bids remain sealed. The player can see the scoring formula, their own known factors and a cost/revenue/subsidy estimate, but not a rival's submitted price or plan. Price points that depend on the final bid set are explicitly labelled as provisional/unknown.

After award, show the public result with the published scoring breakdown for each legitimately public compliant bid, including why the winning proposal won.

Winning commits the service outcomes promised by the tender, not immutable internal implementation. During the contract the player may change exact vehicles, detailed timetable or internal allocation if the service continues to meet the binding corridor/stops, minimum frequency/capacity, journey-time, comfort/quality and reliability terms. Falling below them exposes the real warning/penalty/cure/termination state.

Public-service contracts may be fixed-term or explicitly indefinite. Indefinite/strategic opportunities can publish stricter history/qualification requirements. Expiry, authority termination, operator notice or serious unresolved breach can lead to a new tender rather than silently extending the old award.

## 5. Contracts

### 5.1 Contract overview

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

### 5.2 Contract cards

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

## 6. Transport Plan and operational linkage

The commercial UI must connect the promise to its real execution. In the Transport Plan card, show the ordered origin-to-destination chain as a compact leg list/flow that reflows with window size. Do not require a giant node editor.

For each leg show:

- origin/destination endpoint;
- execution type: existing Line/Pattern, new Line proposal, own ad-hoc movement, external carrier or customer-provided leg;
- responsible operator;
- required/allocated capacity;
- timing/transfer state;
- relevant endpoint/access dependency;
- contractual handover point and whether responsibility continues beyond a public terminal to the final firm;
- for a customer-provided leg, the known usable basis: own local vehicle capacity, private siding/loading facility or procured external carrier;
- current problem when material.

Each specific Line, Pattern, Trip, terminal, external order and other inspectable object is directly clickable. A plan leg does not pretend that cargo has physically moved. Reservation, readiness, loading and in-transit states remain distinct.

When the counterparty offers terminal pickup/delivery or a private industrial siding, present it as a concrete operating option in the proposal—not as an invisible simplification. Show whether the customer capability is currently available/adequate for the proposed quantity and time window where that information is contractually known.

Where an existing Line is used, expose compatible available/committed capacity using the canonical ledgers. Do not show only nominal tonnes/seats if the relevant cargo/passengers cannot use that capacity. A contract allocation is not duplicated because it appears in both commercial and Line windows.

## 7. Shipments inside a contract

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

## 8. Contract lifecycle actions

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

## 9. Minimalism, tooltips and permissions

Apply UI-D15 throughout:

- lists show decisive commercial facts first;
- tooltips explain terms, calculation basis, feasibility causes and SLA/status contributions;
- complete terms, histories and editable policies live in opened details;
- deadlines, binding prices, penalties, blockers and confirmation consequences remain visible.

Do not reveal competitors' private bids, internal cost assumptions or confidential contracts unless gameplay rules explicitly make that information available. A public tender exposes its rules/weights and, after award where legitimately public, the material result breakdown; rival submissions stay sealed before the deadline.

Disabled Submit/Accept actions explain the blocker and link to the corrective workflow where possible. A tooltip or link never submits a bid, accepts a contract, acknowledges a breach or changes simulation time.

## 10. Acceptance evidence to collect

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
| COMUI-A09 | Open timber in Market. The main map automatically shows known city/locality markets with surplus/deficit and local reference prices together while the Market window remains usable. Inspect one large city with several economic centres: all centres share the city's market reference signal, their firms/endpoints remain physically distinct, and cargo never teleports between them. |
| COMUI-A10 | From a real known producer with surplus, compare a known buyer in a deficit market, inspect reference versus concrete commercial terms and propose a transport connection. Both counterparties evaluate real supply/demand; no player commodity ownership, fabricated buyer or fabricated cargo is created. |
| COMUI-A11 | Submit a public tender using a concrete extension/new-Line proposal. Invalid mandatory conditions block submission with exact reasons. Rival bids remain sealed before deadline; after award the published weighted price/reliability/commercial-reliability/comfort/reputation breakdown explains the outcome. |
| COMUI-A12 | Operate an awarded public-service contract, change internal vehicle/timetable implementation while retaining all binding service outcomes, then trigger isolated and repeated failures. Verify progressive reliability/penalty/cure behaviour and eventual legitimate termination/re-tender without one minor incident instantly cancelling the contract. |

## 11. Decision record

| ID | Decision | Status |
|---|---|---|
| UI-D17 | One commercial workspace with Market, Opportunities, Offers and Contracts; commodity Market auto-projects surplus/deficit + reference price onto the main map; Market can lead to real producer/buyer transport proposals without commodity speculation; public tenders use concrete compliant service plans, sealed rival bids and transparent published weighted scoring; persistent drafts remain separate from submission and contracts link directly to real execution | CONFIRMED on 2026-09-30; refined on 2026-10-01 |

UI-D17 complements UI-D01–UI-D16. Core market formation, freight-contract/open-carriage rules and public-tender award mechanics remain owned by GAME_DESIGN; this document defines their commercial presentation and workflow.
