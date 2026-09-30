# Tranzit — Tariffs, integrated networks and period tickets

> **Status: PARTIALLY CONFIRMED — UI-D29, 2026-09-30.** The player explicitly requested configurable integrated groups of Lines with common per-kilometre rates, coexisting company/global tariffs, and discounted weekly/monthly tickets for those integrated systems. These capabilities are confirmed requirements. The detailed solution below is a proposal for review, not blanket approval of the preceding tariff-screen proposal or a completed implementation specification. No UI or gameplay has been implemented or tested by this document.

Read with [UI_UX_DESIGN.md](UI_UX_DESIGN.md), especially UI-D09, UI-D11/UI-D12 and UI-D15; [GAME_DESIGN.md](GAME_DESIGN.md), Sections 3, 6.2, 28, 30.3, 31, 32.2 and 32.4; [UI_FINANCE.md](UI_FINANCE.md), [UI_TRIPS.md](UI_TRIPS.md) and [UI_EXTERNAL_COMPANIES.md](UI_EXTERNAL_COMPANIES.md). [V1_SCOPE.md](V1_SCOPE.md) retains the release boundary. [CONTRACT_CANCELLATION.md](CONTRACT_CANCELLATION.md) does not define retail ticket refunds.

## 1. Confirmed requested capabilities

The player must be able to:

- maintain a global/company tariff rather than configure every Line independently;
- create named integrated tariff systems containing selected Lines;
- give the integrated Lines common kilometre rates instead of manually copying prices between Lines;
- offer cheaper weekly and monthly ticket products for an integrated system, alongside ordinary fares.

The intended integrated system is a commercial grouping, not a new Line, Service Pattern, Trip, infrastructure owner or mandatory geographic region. A shared rate must remain genuinely shared, not several independent copies that drift apart.

The user's request expands pricing/product mechanics as well as their UI. GAME_DESIGN Section 31 currently defines company defaults and Line overrides but not the full integrated-network and period-ticket lifecycle. Before implementation, the accepted solution must be incorporated into that owning section and its dependent rules; do not treat this proposal as an implicit override of existing mechanics.

## 2. Proposed distinction: tariff, network and ticket product

Keep three related concepts separate:

| Concept | Responsibility |
|---|---|
| Tariff | Reusable pricing rules: base/minimum fare, distance or zones, permitted classes and supplements |
| Integrated tariff system | Which Lines/services accept a shared tariff and its products, with an explicit effective scope |
| Ticket product | What is purchased: one journey or travel during a stated period, its price, area/network, classes and conditions |

A company-wide default tariff is not automatically a company-wide unlimited ticket. The player can separately create a company-wide ticket product if that optional proposal is accepted.

## 3. Proposed global, system and Line relationship

Retain the global/company/division/mode defaults from GAME_DESIGN Section 31. For integrated services, add an explicit shared-system layer:

**Company default → integrated-system tariff where applicable → only explicitly permitted product/class exceptions.**

A Line outside a system can retain the existing standalone Line override. Within a system, an ordinary integrated product uses the system's shared rules. A Line override must not silently make the same accepted integrated ticket cost more or cease to work.

A system can inherit selected company parameters and override others. Show the source of every editable rate as Inherited from company, Defined by this system, or Constrained by agreement/authority. Inherited values remain references, not copies. Review affected systems/Lines before applying a change to a global default.

A premium service can have a separately disclosed supplement or accept different products/classes only if those exceptions are part of the system's published scope. Do not promise all services are included while charging an undisclosed exception later.

Regulated prices, concessions, customer-group contract prices and already sold entitlements cannot be overridden by this hierarchy. Contract passenger pricing remains distinct from retail fares.

### Overlap proposal

A Line may need to accept both a local-system product and a broader company-network product. Model this as explicit accepted products, not stacked tariff discounts. A traveller's existing valid product is considered before a new ticket is charged. Where several products could apply, show a deterministic, inspectable choice under their conditions; do not charge multiple full fares for the same covered leg. The exact overlap/selection rule remains to be confirmed in the core design.

## 4. Proposed integrated travel

The player selects the participating Lines, potentially combining rail and road services. System membership alone does not provide vehicles, timetable coordination, infrastructure access, municipal permission, a usable sales channel or additional physical capacity.

Proposed default for an integrated single-journey ticket: calculate the covered itinerary using the common rate and its actual tariff distance, with any base charge applied once to the integrated journey rather than again at every covered transfer. Display transfer/time limits and any fare boundary. The tariff-distance and transfer rules must be made explicit in GAME_DESIGN before implementation; do not charge disruption detours retroactively or use straight-line distance as travelled distance.

Example, illustrative only:

> System: Regional Network
>
> Members: two regional rail Lines and four connecting bus Lines
>
> Shared distance rate: 0.5 money/km
>
> Covered journey: 12 km by rail + 8 km by bus
>
> Distance fare: 10 money, before any explicitly configured base fare or supplement

An integrated fare is not automatically a guaranteed connection. Protected-connection/rebooking rights remain an explicit entitlement under Section 32.4.

## 5. Proposed ticket products

Required product capabilities are weekly and monthly integrated tickets. Single-journey pricing remains available. Optional daily, zone-limited, route-limited and company-wide products are proposals, not additional approved release gates.

Each product defines its name, network/Line scope, eligible class, price, validity and applicable reservation/transfer/refund conditions. For the core weekly/monthly proposal, a time ticket permits repeated covered journeys during its validity; it is not merely a percentage discount on every separately paid journey. That precise entitlement still needs approval.

Use the existing game calendar:

- weekly validity: 7 game days;
- monthly validity: 14 game days;
- no 30-day month or wall-clock expiry.

Proposed initial validity model: an explicitly selected start timestamp plus the product's stated game-time duration. Show exact start and end, including cross-month/year cases. Fixed calendar-period products or first-use activation can be considered separately; do not implement both silently.

Keep price independently configurable for each product. Display a comparison against equivalent single journeys using a chosen example route/travel pattern, never a universal savings claim. Example prices are not balancing commitments:

| Example product | Illustrative price |
|---|---:|
| One 20 km journey at 0.5 money/km | 10 money |
| Weekly network ticket | 70 money |
| Monthly network ticket | 120 money |

For this example, the weekly product matches seven single journeys and becomes cheaper from the eighth; the monthly product matches twelve and becomes cheaper from the thirteenth. Different journeys have different break-even points. An unlimited network product need not be cheaper for an occasional short-distance traveller.

## 6. Proposed UI

Use the existing floating-window/card interaction, not a mandatory setup wizard. Suggested entry: **Business → Tariffs and tickets / Obchod → Tarify a jízdenky**.

Keep company tariffs and integrated systems discoverable together, with ticket products and selling/reservation capability accessible from the same workspace. Exact top-level tab names from the earlier proposal are not locked by this document.

A system detail can use independently openable cards:

| Card | Compact content |
|---|---|
| Lines and validity / Linky a platnost | Participating Lines, covered modes/classes, exclusions and effective version |
| Rates / Sazby | Common km/zone rules, inherited values and concrete journey price examples |
| Tickets / Jízdenky | Single, weekly and monthly products, prices, exact validity and travel entitlement |
| Sales and reservations / Prodej a rezervace | Which real channels can sell or validate each product and confirm reservations |
| Results / Výsledky | Product sales, known use, revenue and capacity consequences for a labelled period |

The player can save an incomplete proposed system/product, return later and edit cards in any order. Saving is not publishing, selling tickets, signing partner agreements or activating Lines. Publication is a separate effective-dated action with current validation and consequences.

Line details show both the default fare source and accepted ticket products. A customer-facing explanation should make it clear that a system ticket is accepted even if a separate standalone fare also exists.

Retain the earlier proposed rate calculator, channel readiness and reservation-zone presentation as supporting ideas. Do not require a matrix of every station pair or a giant dashboard.

## 7. Existing constraints and proposed integration safeguards

### Travel entitlement versus capacity

A period ticket pays for eligible travel; it must not reserve a place on every future Trip. Pass holders still require actual compatible segment capacity. Where reservations are mandatory, a specific Trip/leg reservation is still required, possibly with a disclosed supplement. Its fare portion can already be covered by the pass. No capacity is double-booked or created by product ownership.

Open boarding and optional reservations retain existing rules. A traveller with a valid prepaid entitlement is not charged the same fare again merely because the current Trip lacks onboard ticket sellers. A station without sales can accept a legitimately purchased product only through a period-appropriate supported checking process; it does not gain an invisible sales/real-time reservation system.

### Historical technology and demand

Do not gate a simple paper-based season ticket or an own-company common tariff behind online technology. Appropriate early-era sales/checking and administration still need to exist. Modern dynamic pricing and instant cross-provider reservation checks retain their real technology requirements.

Proposed demand effect: repeat travellers compare a period product with expected eligible journeys and available alternatives. Existing holders face no additional base fare for a covered journey, but still care about time, frequency, crowding and reliability. Products must not create passengers or add an arbitrary loyalty/revenue multiplier. Use aggregate traveller/entitlement cohorts rather than a permanent individual resident simulation.

### Revenue

A sale creates one payment under the financial rules. A pass-covered boarding must not create a second full ticket payment. Line/system profitability reports must distinguish direct single-fare revenue, pass revenue and any analytical allocation of that revenue to covered services. Allocation is not another cash receipt. No artificial exact utilisation data may be shown before the company's information systems can support it.

### Changes and expiry

Store the purchased product/version and its actual price and validity. New rates affect new eligible sales from an explicit effective time, not existing paid tickets. Removing a Line or partner, shortening validity or changing classes must not silently revoke sold rights. Before publication, expose affected holders, outstanding reservations and any required honouring, replacement or refund plan. Exact retail refund and in-progress-journey expiry rules remain open and belong in the core design; the infrastructure cancellation formula must not be applied to passengers.

### Other operators

An own-company system is possible without another carrier. Multi-operator participation is a potential extension of existing passenger cooperation, not permission to add competitors unilaterally. It would require accepted ticket-recognition, sale/settlement and responsibility terms, visible under Our agreements. Exact multi-operator settlement and governance are not approved by this request.

## 8. Consistency work before implementation

When the detailed proposal is accepted, reconcile the owning mechanics and dependent presentation in one change:

- GAME_DESIGN Section 31: global/system/Line hierarchy, integrated fares, product validity/coverage and change protection;
- Sections 6.2 and 32.2: aggregate period-ticket choice, paid entitlement, real sales channels and specific-trip reservations;
- Section 32.4: fare integration versus protected connections, expiry during disruption and passenger recovery;
- Section 30.3 only if multi-operator integration is approved;
- Section 38 and UI_FINANCE: one payment, pass-related reporting and no duplicate revenue;
- UI_UX_DESIGN, Line/Trip/station/firm screens and relevant acceptance/save contracts: shared identities, readiness and exact-object navigation.

The request does not add new transport modes, a second clock, individual passenger micromanagement or a parallel ticket/capacity ledger. Own and AI operators must use the same capability, price, validity, knowledge and capacity constraints. Cache versioned fare/eligibility calculations and update aggregates on relevant events, not every frame.

## 9. Proposed validation scenarios

These are evidence to collect after mechanics are confirmed and implemented, not passing tests.

| ID | Scenario |
|---|---|
| TARUI-P01 | Several Lines inherit one global tariff; some join a system with a shared km rate. Change an inherited and an overridden parameter; affected scope is explained and unrelated fares are unchanged. |
| TARUI-P02 | Use a rail-to-bus integrated journey. Covered transfers do not trigger duplicate base fares; outside-network travel and supplements are explained. Fare integration alone does not promise a protected connection. |
| TARUI-P03 | Compare singles with weekly/monthly tickets for occasional and regular travellers. Show the route-specific cost comparison without fake demand or guaranteed savings. |
| TARUI-P04 | Test 7/14-game-day validity across month/year boundaries at different speeds, in pause and after save/load. Expiry follows only the common game clock. |
| TARUI-P05 | Use a pass in open, optional-reservation and mandatory-reservation zones. Paid entitlement is not a seat guarantee; confirmed bookings are preserved and full services do not admit extra passengers. |
| TARUI-P06 | Record one pass sale and several covered boardings. Cash is posted once; analytical Line attribution and any refund do not duplicate revenue or omit operating costs. |
| TARUI-P07 | Change a system rate or remove a participating Line after passes were sold. Historical terms and reservations remain traceable; no silent revocation or retrospective surcharge occurs. |
| TARUI-P08 | Test overlapping eligible products, invalid class, missing sales/checking capability, delayed travel near expiry, pending partner agreement and incomplete drafts. Each unresolved rule must be specified before acceptance tests can be finalised. |

## 10. Decision record

| ID | Scope | Status |
|---|---|---|
| UI-D29 | Integrated groups of Lines with common kilometre rates, coexisting global tariffs and discounted weekly/monthly tickets | Required capabilities confirmed by explicit user request on 2026-09-30; detailed UI, hierarchy, entitlement and lifecycle proposal pending |

Do not mark UI-D29 fully confirmed until the player has reviewed the detailed proposal. Do not implement the new pricing mechanics from this document alone while GAME_DESIGN still lacks the corresponding accepted rules.
