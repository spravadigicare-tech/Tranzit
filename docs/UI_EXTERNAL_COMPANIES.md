# Tranzit — External company, competitor and agreements UI

> **Status: CONFIRMED UI DIRECTION — UI-D27 and UI-D37, 2026-09-30.** UI-D27 requires all agreements between the selected company and the player's company to be directly accessible. UI-D37 confirms the complete adaptive external-company/competitor detail: overview, public/known operation and assets, products/services, our agreements, relationship/history and ownership. One company retains one identity across all of its roles. Exact visual dimensions, column widths and localized labels remain design work. This specification is not an implemented or tested UI.

Read with [UI_UX_DESIGN.md](UI_UX_DESIGN.md), especially UI-D07 (floating windows), UI-D09 (exact-object links), UI-D15 (minimalism/tooltips), UI-D17 (commercial contracts), UI-D19 (finance), UI-D24 (events), UI-D26 (capacity/access) and UI-D34 (money icon). [GAME_DESIGN.md](GAME_DESIGN.md), particularly Sections 7.2, 9–10, 15, 19–21 and 28–30, owns the actual customer, partner, supplier, infrastructure, facility, leasing, service, knowledge and ownership mechanics. [UI_CITIES_REGIONS.md](UI_CITIES_REGIONS.md) owns City/Region presentation. This document must not create a duplicate company, contract, marketplace or intelligence system.

Sections 1–12 preserve UI-D27's bilateral agreement requirements. Sections 15–22 specify the surrounding UI-D37 company detail. The acceptance scenarios and decision record cover both.

## 1. Requirement

When the player opens the detail of another company, the UI must provide a directly accessible **Our agreements / Naše dohody** section showing every real agreement in which:

- the player's company is a party; and
- the selected external company is a party.

This is not limited to transport-customer contracts. If the same external company is simultaneously a customer, infrastructure owner, workshop provider and subcontracting partner, all those relationships must be discoverable from one company detail.

The section must not require the player to remember whether an agreement lives under Business, Operations, Assets or Finance and then search several unrelated lists manually.

## 2. Placement in external-company detail

Place a compact relationship summary near the top of the external-company detail, below the company identity and any high-level relationship state.

Example, illustrative only:

> **Morava Logistics**
>
> Relationship with our company
>
> Active agreements: 4 · Pending proposals: 1 · Next expiry: Month 7, Day 14
>
> **Open all agreements**

Important current warnings can surface beside the summary, for example an agreement nearing expiry, an unpaid item, an access agreement at risk or an amendment awaiting response. Do not turn every ordinary active agreement into a warning.

If there are only one or two agreements, the compact preview can list them directly. If there are many, show the most relevant/urgent rows and provide **All agreements** for the full list.

## 3. What counts as “our agreement”

Show every canonical agreement/committed order between the two companies that already exists in the simulation. Depending on the counterparties and game state, this can include examples such as:

- customer freight/passenger contracts;
- carrier partnership/framework agreements;
- subcontracting or recurring external-transport arrangements;
- one-off External Transport Orders that are still active, in execution or retained in history;
- through-ticket / passenger-cooperation agreements;
- infrastructure access agreements;
- rail/station Capacity Orders and related capacity agreements;
- station/terminal/depot/workshop/facility rental or service access;
- maintenance/service agreements;
- fuel/material/supply agreements;
- vehicle lease/rental agreements;
- property/infrastructure lease or access arrangements;
- other accepted bilateral contracts/committed orders already defined by the core game.

This list is illustrative, not permission to invent a new agreement type.

A vehicle purchase, infrastructure sale or other completed one-off transaction may remain visible in **History** when the underlying system records a transaction/agreement, but it is not presented as an active recurring agreement after completion.

Quotes, discovered opportunities, draft bids and unaccepted proposals are not active agreements.

## 3.1 Bilateral cooperation agreement builder

Recurring bilateral business agreements between two companies can reuse one structured agreement-builder pattern where the underlying contract type supports it. This includes carrier cooperation and recurring supplier agreements; it does not force customer tenders, one-off purchases or unrelated legal objects into one generic contract.


The editor is visually split into the two parties:

> **Our company** | **Selected company**

Supported clauses appear as explicit options under the side that grants the right, pays the rate or accepts the obligation. A clause can therefore be:

- bilateral with different values on each side;
- enabled in only one direction;
- symmetric only when both sides actually agree to identical terms.

Do not force mirrored terms.

For passenger cooperation, the currently defined clause is:

- **Sell partner capacity on through tickets**, independently enabled in each direction.

Passenger connection-agreement clauses are intentionally unspecified until [CONNECTION_AGREEMENTS.md](CONNECTION_AGREEMENTS.md) is redesigned from scratch.

When capacity resale is enabled, configure each party independently in its own column.

Example:

> **Our company**  
> Partner may sell our capacity: ✓  
> Covered Lines: R12 Praha–Brno, R18 Praha–Plzeň  
> Rate owed to us: **0.47 money/km**
>
> **Morava Rail**  
> We may sell their capacity: ✓  
> Covered Lines: MR4 Brno–Vídeň  
> Rate owed to them: **0.42 money/km**

The two directions may have different enabled states, Line scopes and rates.

A **Select all current Lines** convenience action may populate the current list, but the accepted agreement stores explicit Line identities. Newly created Lines are not automatically added.

These are settlement terms between the companies, not the public passenger tariff.

For V1, this clause applies only to a **single-journey two-operator through ticket** containing at least one leg operated by the selling carrier and at least one covered Line of the partner. The agreement is not a general ticket-reseller licence, does not permit recursive resale of a third carrier's capacity, and does not create a shared multi-company weekly/monthly pass.

Show a concise scope note in the clause detail:

- single journeys only;
- current explicit partner Lines;
- public partner fare remains passenger-facing;
- negotiated money/km rate is internal settlement;
- capacity/reservation remains real;
- connection protection/timetable coordination is **not included** by this clause.

When useful, show one or two current fare examples with public partner fare, settlement and resulting margin, including a negative-margin warning when applicable. Examples are calculated from current data and never become guaranteed future prices.

The builder remains intentionally small. Do not expose arbitrary legal text, dozens of generic modifiers or clauses without a real simulation owner.

Submitting creates a pending bilateral proposal. The partner can accept, reject or return a counterproposal with changed explicit terms. Only accepted clauses become binding rights/obligations.

## 4. Active, pending and historical views

Provide clear filters/views:

- **Active / Aktivní** — currently binding and effective agreements;
- **Future committed / Budoucí** — already binding but not effective yet;
- **Pending / Rozjednané** — actual submitted offers, amendments, renewals or counterpart proposals awaiting a decision/response;
- **History / Historie** — expired, completed, rejected, released or terminated agreements/transactions retained for context.

A saved internal draft that has never been submitted to the other company does not appear as a bilateral Pending agreement merely because the player is considering it.

A pending proposal must never look like active capacity, guaranteed revenue, available workshop capacity or another binding right.

## 5. Agreement row

Each agreement row should expose enough information to distinguish its purpose without opening it:

| Field | Meaning |
|---|---|
| Type | Customer contract, capacity/access, maintenance, lease, supply, partnership, external transport order, etc. |
| Our role | Buyer/customer, carrier/provider, lessee, capacity buyer/seller, subcontractor/client, partner, etc. |
| Scope | What service/assets/facility/corridor/commodity the agreement concerns |
| State | Active, future committed, pending response, renewal pending, expiring, completed, terminated, etc. |
| Validity | Start/end or one-off execution window where applicable |
| Next important event | Renewal deadline, expiry, delivery, payment, response deadline or another real obligation |
| Financial basis | Compact fee/price/payment basis where relevant and known to the player |
| Main issue | Only when a material problem, blocker or decision exists |

Do not force every agreement into fields that do not apply. A one-off transport order may show pickup/delivery timing rather than an annual validity term.

Clicking the row opens the canonical detail for that agreement — for example the customer Contract view, Capacity Order, facility agreement, lease, External Transport Order or service contract. Do not create a generic copied agreement detail that can diverge from the owning workflow.

## 6. One agreement, one identity

The same underlying agreement can be referenced from many places:

- external-company detail;
- Line/Pattern;
- station/depot;
- Capacity and access overview;
- Finance;
- Contract/Shipment;
- vehicle/fleet;
- event history.

These are views of **one stable agreement identity**, not separate agreements.

Example: one station-access agreement linked from the station, Line and counterpart company must still have one validity period, one renewal state, one fee ledger and one cancellation settlement.

Do not count the same capacity agreement once per Line, once per station and again as a separate “company agreement” total.

Where one coordinated Capacity Order contains several owner-specific agreements, the selected external company's detail shows the part(s) involving that company and links back to the coordinated order. The company-level row must not pretend that this owner alone grants the complete route capacity.

## 7. Relationship context

The external-company detail may summarize the player's relationship with that company using real history, such as:

- number/type of active agreements;
- current customer/partner/provider roles;
- meaningful recent contract performance;
- unpaid/overdue obligations where the player is entitled to know them;
- upcoming renewal/expiry;
- unresolved disputes/breaches;
- current submitted proposal/amendment.

Do not collapse this into an opaque universal “relationship score” if the underlying causes are available. If a compact qualitative relationship state exists under the core reputation/customer model, make its contributors inspectable.

The company detail should make mixed relationships understandable. The same company can be:

> customer + workshop provider + infrastructure owner

without forcing the UI to pick only one identity.

## 8. Finance and obligations

From an agreement row or the relationship summary, allow direct access to relevant Finance detail.

Show the player's known bilateral financial position where meaningful, such as:

- upcoming payable/receivable amounts;
- outstanding invoices;
- recurring fee basis;
- cancellation/termination exposure only when the applicable workflow can calculate it;
- prepaid amounts/credits where already recorded.

Do not add all contract nominal values together and call the sum “company value” or “exposure” without a meaningful basis.

A pending quote is not an accounts payable item. A forecast customer volume is not receivable cash. Compact amounts use UI-D34's neutral money icon; textual and accessible representations retain the accounting unit.

## 9. Permissions and privacy

Because the player is a party to **our agreements**, their own accepted terms are inspectable even when the counterparty is a private company.

This does not reveal:

- the counterparty's agreements with unrelated competitors;
- private bids from other carriers;
- internal costs/margins;
- private fleet commitments unrelated to the player's contract;
- confidential customer/supplier relationships to which the player is not a party.

Publicly available information can still appear through normal world/company information rules. Section 19 applies this boundary to every field, list, aggregate and linked detail, not only the agreement list.

## 10. Direct navigation

Use UI-D09 exact-object links throughout.

From the counterpart company the player can open:

- agreement detail;
- linked Line/Pattern/Trip;
- station/terminal/depot/workshop;
- Shipment/Contract;
- vehicle/order where relevant;
- Finance posting/breakdown;
- relevant event/incident.

From those objects, the external company name links back to the same company detail.

Opening links does not acknowledge incidents, accept proposals, renew agreements, pay invoices or move the camera unless an explicit Locate action is chosen.

## 11. Search, filters and scale

The full agreement list supports:

- state;
- agreement type;
- our role;
- facility/corridor/region where relevant;
- date/expiry;
- active issue/decision;
- text search.

Preserve filters/selection/scroll during live updates.

For a long-standing partner with many completed one-off orders, history may group or paginate old records while retaining exact access. Do not render the entire decades-long history every frame.

## 12. Save/load and lifecycle safety

Persist stable agreement identities and company relationships through save/load.

After load:

- active agreements remain active;
- pending proposals do not become accepted;
- future committed terms retain their effective dates;
- expired/released agreements remain historical;
- renewal state is not duplicated;
- payments/settlements are not reposted;
- the counterpart company detail reconstructs the same bilateral list.

If one party changes ownership, merges, fails or is acquired, preserve agreement history and follow the actual legal/business successor rules of the core simulation. Do not silently retarget an agreement to another same-named company.

## 13. Acceptance evidence to collect

These scenarios describe evidence to collect when implemented, not a claim of passing gameplay tests.

| ID | Required scenario |
|---|---|
| EXTCO-A01 | Give one external company simultaneous roles as customer, station/facility provider and subcontracting partner. Its detail exposes all player-company agreements in one place without duplicating the underlying contracts. |
| EXTCO-A02 | Show Active, future committed, pending proposal/renewal and historical agreements together. Pending proposals never grant active rights/revenue/capacity. |
| EXTCO-A03 | Open an agreement from the external company, then follow links to Line/station/Finance and back. Every view resolves the same stable agreement identity and values. |
| EXTCO-A04 | Use a multi-owner Capacity Order. Each owner's company detail shows only its own component(s) and links to the coordinated order without claiming full-route coverage. |
| EXTCO-A05 | Verify the counterpart's unrelated private contracts, bids, costs and fleet commitments remain hidden while the player's own agreement terms stay inspectable. |
| EXTCO-A06 | Expire, renew, terminate and complete several agreements, then save/load. Status/history, financial state and counterpart relationships persist without duplicate contracts or postings. |
| EXTCO-A07 | Verify CZ/EN, enlarged UI, filters and large history. Material terms/actions remain accessible without hover-only dependence or rendering every historical record continuously. |
| EXTCO-A08 | Open the same company from a competitor Line, customer contract, workshop and supplier offer. Reuse the same company identity and adaptive six-card structure; no role hides another role or creates a duplicate company detail model. |
| EXTCO-A09 | Inspect public passenger services and partially observed freight operation. Published calendars/fares are correctly scoped; hidden contracts, duties, reserves and loads remain inaccessible through links, counts, sorting, map overlays and tooltips. |
| EXTCO-A10 | Observe the same asset repeatedly, then let its information become stale or its known owner change. Do not duplicate assets or call a historical sighting a current fleet total/live position. Current ownership and operation remain distinct. |
| EXTCO-A11 | Open manufacturer, maintenance, contractor, supply and external-transport offers from a company. Each routes to its existing workflow with context preserved; merely inspecting creates no booking, charge or provider capacity. |
| EXTCO-A12 | Inspect relationship history with good partner performance and competing services simultaneously. Measures retain time period/sample/scope; qualitative labels have real contributing causes rather than a new universal score. |
| EXTCO-A13 | Inspect a minority shareholding, a subsidiary and a company acquired or dissolved in the recorded history. Ownership percentage does not grant invented control or private information; stable original identity, agreements and verified successor links remain. |
| EXTCO-A14 | Save/load with an open pinned company, stale observations, current offers and historical events, including a macro-region company. Knowledge and permissions are revalidated without discovering hidden data, replaying events, activating regions or changing pause state. |
| EXTCO-A15 | Inspect an industrial customer that owns a private siding and limited local pickup vehicle capacity. Show only legitimately known/contractually offered logistics capability. Use it in a freight proposal, then verify the physical customer-provided leg/endpoint uses finite real capacity and no hidden public-carrier service or teleportation appears. |
| EXTCO-A16 | Configure asymmetric passenger capacity resale, inspect a positive- and negative-margin example, then sell one valid two-operator single-journey through ticket. The company detail shows explicit directional Line scope/rate and the sold ticket's captured agreement version; it does not offer partner-only resale, recursive third-carrier resale, shared multi-company period products or connection protection from this clause. |

## 14. Decision record

| ID | Decision | Status |
|---|---|---|
| UI-D27 | Every external-company detail provides a directly accessible, complete view of all agreements between that company and the player's company, with active/future/pending/history separation and links to each canonical owning workflow | CONFIRMED on 2026-09-30 |
| UI-D37 | One adaptive external-company/competitor detail with Overview, Operation and network, Products and services, Our agreements, Relationship and history, and Ownership; public/observed/contractual/commercial/estimated information stays distinct and private operations remain protected | CONFIRMED on 2026-09-30 |

UI-D37 completes the surrounding external-company layout without reopening UI-D27. City/Region presentation is owned by UI-D28, acquisition/ownership transactions by confirmed UI-D39 in [UI_OWNERSHIP.md](UI_OWNERSHIP.md), and World News/history by confirmed UI-D40 in [UI_NEWS.md](UI_NEWS.md). These remain separate canonical workflows rather than extra cards invented inside company detail.

## 15. One adaptive company window — UI-D37

A company can simultaneously be a competitor, customer, subcontractor, manufacturer, supplier, workshop provider, contractor or infrastructure owner. These are roles of one company, not mutually exclusive object types or separate copies of the company.

Open the same movable/resizable detail from the world, a city, an agreement, a vehicle/facility owner link, an offer or a known event. Reuse the shared window manager, content pinning, exact-object links and return-to-source behaviour. Do not replace a pinned company or silently discard edits in the source planner.

The compact header shows name, known activity roles, known operating areas, the player's bilateral agreement summary, our recorded ownership interest where applicable, and a material current event/issue when known. Distinguish activity roles from the company's relationship to the player. Use explicit **Show on map / Zobrazit na mapě** for spatial navigation.

Illustrative header:

> **Morava Rail**
>
> Rail operator · Infrastructure owner · Workshop provider
>
> Known operating areas: Morava, Čechy
>
> Our relationship: 4 active agreements · 1 pending proposal
>
> Our ownership: none

Show known scope, not a fabricated full-world footprint. A role not known to the player must not be revealed simply because the underlying AI has that capability.

### Six task-based cards

| Card | Content |
|---|---|
| Overview / Přehled | Main activity, known geography, current company state, important known events and the player relationship |
| Operation and network / Provoz a síť | Public/known services, facilities, infrastructure and a nested known-assets view; published timetables/fares and observable activity within information rights |
| Products and services / Produkty a služby | Actual known offers and requests, compatible service categories, our open orders and links into canonical marketplaces/planners |
| Our agreements / Naše dohody | The complete UI-D27 list in Sections 1–12; active, future committed, pending and history remain distinct |
| Relationship and history / Vztah a historie | Evidence-backed cooperation/payment/performance history and significant known company events |
| Ownership / Vlastnictví | Known owners/group relationships, our actual shareholding, recorded distributions and current control rights where supported |

Known assets sit within Operation and network rather than becoming a mandatory seventh top-level card. A small goods supplier does not need an empty passenger timetable. Adapt irrelevant sections away while keeping unknown information distinguishable from confirmed absence. Our agreements remains directly reachable, including a clear no-agreements state.

## 16. Public operation, network and known assets

For public passenger services, expose published Line/Pattern, stops, calendar/frequency, available classes/products and published fares within the player's information access. Identify the journey/class/time basis behind any “from” fare; do not imply a sample price is universal. Current disruption/platform/ETA information follows the actual communication capability and observation time.

Opening a rival's Line or Trip uses a permission-filtered detail. Public visibility does not expose internal vehicle duties, tomorrow's spare fleet, private maintenance plans, cargo allocations, current cash, future profit or submitted private tender bids. The same restriction applies from station boards and map layers.

Freight operation can be only partly known. Show an observed movement/corridor where justified; do not infer an exact cargo, customer, quantity, recurring contract or hidden route solely from seeing a train. If the commodity is genuinely known, its source is inspectable.

Known-assets lists distinguish ownership, operation and leasing where known. A vehicle observed working for an operator is not automatically owned by it. Repeated sightings of an identifiable asset count once. Unidentified sightings must not become invented serial-number objects.

An observation is timestamped. “At least 12 locomotives known in the displayed observation period” is not the company's current total or free capacity. Outdated sightings remain historical/last known and cannot indefinitely prove a live fleet lower bound after sales, transfers or scrapping. A last-known location is not a live tracking signal.

Known infrastructure links lead to the actual station, depot, corridor or other permitted asset detail. Distinguish owned infrastructure from access rights and third-party facilities merely used by the company. Aggregation must not count the same asset once per role, Line or subsidiary relationship.

For industrial/customer firms, Operation and network can also expose **legitimately known own-logistics capability** relevant to doing business with the player, such as a customer-owned loading siding, freight yard/dock, or a declared ability to collect/deliver from a named terminal with its own local road capacity. Do not infer or reveal the firm's complete private vehicle fleet from that capability. Contractually offered capability can be shown with the scope needed for the proposal (endpoint, cargo compatibility, quantity/throughput, time window) without exposing unrelated assets.

Where a non-transport firm legitimately has exceptional captive intercity **road** capacity, never summarize this as a blanket "own transport" capability. Show only the known qualifying origin-destination/cargo scope and the bounded usable quantity/time window. A private siding, customer-owned wagons or an industrial shunter never imply customer-operated mainline rail haulage; the rail carrier remains a separate real operator.

## 17. Products and services reuse the owning workflows

This card is a company-scoped entry into existing commercial systems, not a parallel marketplace. Show only actual known offers or a legitimate request-for-offer action. Capability is not guaranteed availability, and opening a quote does not reserve capacity.

| Company role / need | Existing workflow |
|---|---|
| Manufacturer, dealer or vehicle lessor | [Fleet and vehicle market](UI_FLEET.md), scoped to the company/model/offer |
| Workshop or maintenance provider | [Maintenance planning](UI_MAINTENANCE.md), retaining required asset/service/date and physical transfer constraints |
| Construction contractor | [Construction project](UI_CONSTRUCTION.md), retaining actual project requirements and contractor offer context |
| Fuel/material/parts supplier | [Procurement](UI_PROCUREMENT.md), scoped to supplier/item/location and real purchase/delivery terms |
| Infrastructure/facility owner | [Capacity and access](UI_CAPACITY_ACCESS.md) or the canonical facility agreement detail |
| Carrier or specialist transport provider | GAME_DESIGN Section 30.1's shared External Transport Order; no company-only delivery engine |
| Customer with a discoverable requirement | [Commercial opportunity/contract planner](UI_COMMERCIAL.md), using the same known opportunity identity |

Retain the originating planner's requirements when navigating through a company to an offer and back. Freshly validate changing price, expiry, compatibility and finite provider capacity before acceptance. No private provider schedule is disclosed just because an offer includes an available service window.

Industrial-company detail may expose known input/output categories and actual discoverable needs through this card and Overview. It does not disclose hidden inventory, margins or future orders. Model catalogues retain the enduring-historical-model rule; a manufacturer lacking a current offer does not erase the model from discovery.

## 18. Relationship and meaningful company history

Relationship presentation uses the real evidence described in Section 7. Show the period, sample and applicable role for measures such as completed orders, timely deliveries, disputes or overdue payments. No history means insufficient evidence, not perfect reliability or a zero rating.

A company may be a reliable service partner and a strong competitor on the same route. Keep these facts independent. A qualitative “stable relationship” label must resolve to its actual contributing history rather than a new all-purpose company-strength/relationship number.

The company timeline retains significant known events such as expansion, public service openings/closures, major projects, publicly known asset sales/acquisitions, ownership change, restructuring and agreements with the player. Do not expose secret strategy changes or turn every minor update into a world-news item.

Distinguish event time from when the company learned the information. Historical entries retain event-time meaning and link to the current permitted object detail or retained record, following UI-D24. A later rename, repair or acquisition must not rewrite the original event as if it had always been true.

The timeline reuses canonical events; the future news presentation may link to them without creating a second event history. Follow notifications use UI-D24 and never increase the player's information rights.

## 19. Knowledge provenance and permission boundaries

Use the same information categories as City/Region presentation:

- public;
- observed;
- contractually known;
- commercially known;
- estimated;
- unknown/unavailable.

A clean overview need not label every self-evidently public name. However, material uncertainty, incomplete coverage, estimates and stale observations must be visible before opening a tooltip. Supporting source, timestamp, method and reporting period can be revealed through hover/focus/detail.

Knowledge can legitimately follow local company presence, public services, shared infrastructure, actual commercial dealings and adopted information systems. These are evidence sources, not a new espionage minigame. Opening a company, searching, zooming the camera or rendering a vehicle does not itself grant omniscience or refresh every private record. Logical observation/communication must respect the existing era, location and permission rules rather than camera-frame behaviour.

Apply permissions before producing counts, aggregates, sorted rows, filters, tooltips and linked details. A hidden contract count or precise private capacity total must not leak through an otherwise redacted screen. Unknown is not zero. Contract knowledge of one delivery/slot does not reveal the provider's entire schedule.

Inactive-region companies retain the allowed macro/public information boundary. Inspection does not activate their region or instantiate detailed hidden operations. More capable technology improves only supported information access; it never grants unrestricted competitor data merely because the calendar advances.

## 20. Ownership information and group relationships

Show only known owners, subsidiaries and share percentages, plus the player's actual recorded interest and distributions where applicable. Distinguish the selected company, parent and subsidiaries by stable identity. State whether a displayed scope is one company or a group.

A minority shareholding is not operational control or automatic access to private accounts. Display the actual rights granted by the ownership model; do not invent a control threshold, settlement formula or due-diligence entitlement here. Unknown ownership is shown as incomplete/unknown rather than guessed.

Recorded dividends link to Finance and use UI-D34's neutral amount presentation. Expected distributions are not cash already received. Do not sum subsidiary assets/turnover into group totals without a supported scope and reconciliation.

The Ownership card links into the confirmed UI-D39 [UI_OWNERSHIP.md](UI_OWNERSHIP.md) workflow. UI-D37 still owns what ownership information is visible; UI-D39 owns buying stakes, control, subsidiary management modes, direct-control context, integration and infrastructure/company transactions. Do not infer direct operational control from a minority holding.

## 21. Renaming, acquisition, dissolution and retained identity

Renaming changes presentation, not company identity. Equal names cannot merge companies or retarget agreements.

Acquisition alone does not imply dissolution. A subsidiary may retain its identity and operation; show the actual recorded relationship. If a company really ceases operation or is dissolved, keep a read-only historical detail with the relevant date, our former agreements and a verified successor link only when one exists.

Do not automatically transfer contracts, cancel obligations, move vehicles or duplicate assets when the company detail changes state. The underlying business lifecycle owns any successor transfer. The detail reports that transition and retains the original counterparty history.

## 22. Refresh, persistence and presentation safety

The company view derives from canonical company identities, agreements, offers, observations, ownership records and events. Use event-driven/cached views with bounded lists; opening a detail must not scan all world companies or run a second economic simulation.

Save/load preserves the necessary knowledge/provenance and references through their owning systems. Reopening does not refresh stale information to omniscient live state, rediscover the same asset as new, duplicate an agreement or replay a payment/event. Revalidate inspection/control rights if a company or asset changed ownership while a window stayed open.

Preserve selected card, filters, scroll and pinned identity during permitted live updates. Tooltips remain accessible during pause; ordinary navigation never changes time, acknowledges an incident, submits a bid or accepts an offer. Test Czech/English text, enlarged UI, incomplete information and missing/retired objects without clipping essential quantities, money signs or action consequences.
