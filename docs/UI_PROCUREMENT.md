# Tranzit — Procurement, supplies and suppliers UI

> **Status: CONFIRMED UI DIRECTION — UI-D32, 2026-09-30.** The player accepted one procurement/supply workspace for physical operating supplies, purchase orders, suppliers and reorder rules. The UI must keep on-hand inventory distinct from reserved, ordered, in-transit and physically received quantities; show location-specific stock and projected shortage; reuse recurring supply agreements and the shared External Transport Order; and link supplier relationships to UI-D27. Exact visual dimensions, labels, default horizons and balancing thresholds remain design/content work. This specification is not an implemented or tested UI.

Read with [UI_UX_DESIGN.md](UI_UX_DESIGN.md), especially UI-D09 (exact-object links), UI-D15 (minimalism/tooltips), UI-D16 (facility supplies), UI-D18 (construction), UI-D19 (finance), UI-D27 (external-company agreements), UI-D30 (maintenance) and UI-D31 (duties). [GAME_DESIGN.md](GAME_DESIGN.md), especially Sections 11.12, 18 and 30.1, owns supply agreements, physical inventories, recurring procurement, fueling/operating supplies and External Transport Orders. This document presents those mechanics; it does not add another inventory, transport or contract system.

## 1. Entry and purpose

Use **Business → Procurement and suppliers / Obchod → Nákup a dodavatelé** as the primary company-wide workspace.

Provide four main views:

- **Inventory / Zásoby**
- **Orders / Objednávky**
- **Suppliers / Dodavatelé**
- **Reorder rules / Pravidla doplňování**

The overview answers:

1. What important operating supplies does the company physically have, and where?
2. Which purchase orders/deliveries are expected?
3. Where is a shortage likely before the next valid replenishment?
4. Which suppliers/agreements and transport responsibilities underpin those supplies?

Illustrative summary:

> 3 stocked items below target  
> 2 purchase deliveries in transit  
> 1 delivery at risk
>
> Main issue: Brno depot has approximately 3 operating days of coal remaining

Do not replace this with one company-wide generic “supply health” score.

## 2. Inventory is physical and location-specific

The default inventory view groups supplies by their real storage/facility location.

Example:

> **Brno depot**
>
> Coal  
> On hand: 84 t  
> Reserved/committed internally: 12 t  
> Target stock: 160 t  
> Known/forecast consumption: ~27 t/day  
> Confirmed inbound: 60 t  
> Expected arrival: Day 5

Relevant supply categories can include, where the facility actually uses/stores them:

- coal;
- diesel/petrol or other stocked fuel;
- water/traction consumables where modelled as stock;
- lubricants;
- maintenance parts/materials;
- catering/service supplies;
- construction/project materials where shown contextually from their owning project/procurement records;
- other canonical physical operating supplies.

Do not show electricity as a stored cargo quantity when GAME_DESIGN models it through grid connection/capacity.

A company total may aggregate compatible quantities for reporting, but must not imply that 100 t stored in Praha is immediately usable at Brno.

## 3. Supply states must stay distinct

At minimum distinguish:

- **On hand / Na skladě** — physically present inventory;
- **Reserved / Rezervováno** — on-hand quantity committed to known internal work where the inventory model records such reservation;
- **Ordered / Objednáno** — accepted commercial purchase, not yet physically in transit/received;
- **In transit / V přepravě** — physical delivery movement has begun;
- **Received / Přijato** — physically delivered and accepted into destination inventory;
- **Unavailable/short / Nedostupné** — required amount cannot currently be sourced or delivered in time.

A quote, planned reorder or draft purchase is not Ordered.

An accepted order is not On hand.

An in-transit delivery is not usable at the destination until physically received/handled under the owning rules.

The UI must never solve a shortage by simply moving an ordered number into local stock.

## 4. Inventory row and local forecast

Each important inventory row can show:

| Field | Meaning |
|---|---|
| Supply | Exact canonical item/category |
| Location | Physical storage/facility |
| On hand | Current physical usable stock |
| Reserved | Already committed local quantity where applicable |
| Target / reorder point | Player/company policy value |
| Consumption basis | Recent/known/forecast use and period |
| Confirmed inbound | Accepted quantity not yet received |
| ETA | Supported expected arrival, otherwise Unknown |
| Projected minimum | Lowest supported projected stock before inbound/replenishment |
| Risk | Stockout/low buffer/transport/supplier issue |

Do not treat a target level as a hard physical minimum unless another rule makes it so.

A target is a procurement policy. Zero stock is a physical fact.

## 5. Shortage projection

Warnings should use projected consumption and inbound deliveries rather than a universal “below 20%” trigger.

Example:

> **Brno depot — coal**
>
> On hand: 84 t  
> Known/planned consumption before next delivery: 55 t  
> Expected stock immediately before delivery: 29 t  
> Confirmed inbound: 60 t
>
> Current plan is expected to remain supplied.

Or:

> **Stockout likely before delivery**
>
> Current stock is projected to run out approximately 11 h before the currently expected inbound delivery.

The projection should consider only information the company can reasonably know, for example:

- planned vehicle duties and expected fuel/consumable use;
- known maintenance jobs and reserved parts/materials;
- accepted construction work/material consumption;
- known facility operations;
- confirmed purchase quantity;
- expected delivery/transport timing;
- actual historical consumption where used as a forecast basis.

Label estimates and forecast horizon. Do not present uncertain supplier/transport arrival as guaranteed.

## 6. Procurement orders

The Orders view contains real purchase lifecycle records, not only invoices.

A row can show:

- item/quantity;
- supplier;
- destination;
- order state;
- unit/total price;
- buyer/supplier transport responsibility;
- pickup/readiness;
- expected arrival;
- quantity already shipped/received;
- linked recurring agreement/reorder rule;
- payment state where relevant;
- current blocker/risk.

Possible lifecycle presentation follows the owning systems, for example:

**Draft/proposal → Offered/quoted → Accepted/ordered → Ready for pickup → In transit → Partially received → Received/closed**

Only expose states that actually exist for that purchase/supplier. Do not invent “shipped” for supplier-delivered goods before physical transport begins.

Partial deliveries must reconcile exactly to the order quantity.

## 7. One-off purchase and recurring supply agreements

The workspace supports the existing procurement choices:

1. delivered purchase;
2. purchase at source with player's own transport;
3. purchase at source with external transport;
4. recurring supply agreement.

A recurring agreement can expose actual terms such as:

- supplier;
- item/specification;
- destination or pickup point;
- recurring/fixed quantity where the agreement defines one;
- price/price rule;
- validity;
- Auto-renew;
- minimum/maximum quantity where defined;
- transport responsibility;
- service/availability commitments;
- notice/termination terms.

Example:

> **Coal supply framework**
>
> Destination: Brno depot  
> Planned recurring delivery: 60 t every 7 days  
> Price: 14 money/t  
> Transport: supplier  
> Auto-renew: On

The example does not create a universal mandatory contract form. Use only fields supported by the actual agreement.

Auto-renew extends the agreement; it does not physically deliver or refill anything by itself.

## 8. Reorder rules

Reorder rules are separate from supplier-contract renewal.

Typical rule:

> Reorder when usable stock falls below 80 t  
> Target after replenishment: 160 t  
> Preferred supplier/agreement: Bohemia Coal  
> Maximum authorized unit price: 18 money/t  
> External fallback: allowed  
> Manager approval above: configured threshold

The exact fields depend on the existing delegation/procurement model, but every automated rule must expose:

- trigger;
- target/quantity calculation;
- supplier selection scope;
- budget/price authority;
- fallback behavior;
- responsible manager/policy where delegated.

An automatic reorder:

- cannot fabricate supplier inventory;
- cannot exceed actual supplier capacity;
- cannot exceed manager/player authority;
- cannot assume delivery transport exists;
- cannot bypass storage capacity;
- cannot buy an incompatible item;
- cannot silently exceed a configured maximum price/budget.

If the rule cannot produce a valid purchase, surface the reason and, when player authority is needed, create a decision item under UI-D24.

## 9. Supplier view and bilateral relationship

The Suppliers view lists counterparties from actual known procurement relationships/offers.

A supplier row can show:

- company;
- supplied categories;
- currently known active offers/capacity where the player's information permits;
- active recurring agreements;
- outstanding orders;
- recent delivery performance where known;
- next renewal/expiry;
- current issue.

Clicking the company opens its canonical external-company detail.

UI-D27 applies: **Our agreements / Naše dohody** must show all agreements between the supplier and the player's company, not only the currently selected supply contract.

Do not expose:

- supplier's private contracts with competitors;
- exact hidden production/inventory unless contract/public/commercial knowledge grants it;
- internal cost/margin;
- guaranteed future capacity not actually contracted/offered.

## 10. Transport responsibility

Every physical purchase must make delivery responsibility explicit.

Examples:

> **Delivery: 60 t coal**  
> Seller: Bohemia Coal  
> Transport responsibility: **Supplier**

or:

> Transport responsibility: **Buyer**
>
> Transport not yet arranged.
>
> **Arrange transport**

If the buyer is responsible, the player can use:

- own valid transport capacity;
- the shared **External Transport Order** in GAME_DESIGN Section 30.1;
- another canonical framework/provider arrangement where available.

The contextual action opens the existing External Transport Order with item, quantity, origin, destination and required timing prefilled. Do not create a separate “supply delivery marketplace”.

Supplier-provided transport is also physical. It can be delayed or capacity-constrained; it is not an invisible teleport.

## 11. Supplier/production shortfall

If an accepted/expected supply changes because the supplier cannot fulfil its obligation, show the actual known state and consequence.

Illustrative:

> **Bohemia Coal delivery at risk**
>
> Contracted/ordered: 60 t  
> Currently confirmed available for this delivery: 35 t  
> Reason: supplier production shortfall
>
> Brno depot is now projected to fall below its configured target before the next replenishment.
>
> **Find alternative offer · Review agreement · Open affected facility**

Do not silently rewrite an accepted 60 t order to 35 t without preserving the original commitment/history and any applicable breach/recovery consequence.

If the supplier has not formally changed a commitment but risk has merely increased, show **at risk/forecast** rather than falsely declaring a reduced confirmed quantity.

## 12. Shortage impact on operation

A supply shortage should link to the exact dependent operation.

Examples:

- fuel shortage → affected vehicle duties/Lines;
- maintenance part shortage → blocked maintenance jobs/vehicles;
- catering/service supply shortage → affected passenger-service tasks;
- construction material shortage → affected project/stage;
- facility consumable shortage → affected facility capability.

Do not automatically cancel every dependent Trip just because the projection crosses a target.

The dispatcher/manager can apply existing recovery/policy logic. A hard physical shortage that makes a Trip impossible becomes a real readiness blocker.

Possible contextual actions include only real existing workflows, such as:

- increase/modify order;
- find another supplier/offer;
- arrange faster/alternative transport;
- open affected duty/Line/facility/project;
- change an authorized operating policy.

## 13. Construction procurement integration

Construction remains owned by UI-D18 and its project/material rules.

The Procurement workspace may show:

- accepted project material purchases;
- supplier agreements;
- deliveries;
- transport status;
- company-wide supplier relationship.

It must not maintain a separate construction-material requirement or inventory ledger.

A construction project's Materials card remains the contextual source for what that project needs and when. Procurement provides the cross-company purchasing/delivery perspective.

## 14. Maintenance procurement integration

UI-D30 remains authoritative for maintenance-job readiness.

Procurement can show parts/material purchases and supplier agreements, but the maintenance job still owns:

- which part/material is required;
- whether it is compatible;
- whether it is already reserved for the job;
- when service can start.

Ordered parts are not workshop inventory. Physically receiving the part at a different location does not make it available to the job without real transfer where required.

## 15. Finance integration

Purchase and supply agreements link to UI-D19.

Distinguish:

- quoted price;
- committed order value;
- deposit/prepayment;
- payable invoice;
- paid cash;
- recurring future commitment;
- transport charge;
- refund/credit where applicable.

Do not count an accepted order both as immediate expense and again when its invoice is posted if the accounting rules distinguish commitment from cash/expense recognition.

Procurement forecast/target quantities are not financial postings.

## 16. History and auditability

Retain meaningful procurement history:

- original order quantity/terms;
- amendments;
- partial shipments/receipts;
- delays;
- supplier shortfalls;
- alternative procurement/recovery;
- final accepted quantity;
- cancellation/expiry;
- payment/credit references.

Historical orders remain linked to the supplier and destination even if current prices or stock change.

A supplier detail link opens current company state; historical order terms remain the event/order-time record.

## 17. Save/load and state safety

Persist canonical purchase/order/agreement identity, quantities, state, destination, transport responsibility, received amounts, reorder policy and linked supplier/transport records through the owning systems.

After save/load:

- accepted orders do not revert to drafts;
- in-transit deliveries do not reappear at source;
- received quantities are not received twice;
- reorder rules do not fire duplicate purchases merely because the save loaded;
- outstanding transport orders remain the same movements;
- prepaid/paid amounts are not reposted;
- stock projection recomputes from authoritative inventory/commitments without creating stock.

Opening, filtering, comparing or changing a draft reorder rule does not buy, transport or receive goods.

## 18. Acceptance evidence to collect

| ID | Required scenario |
|---|---|
| PROCUI-A01 | Inspect the same coal supply as On hand, Reserved, Ordered, In transit and Received through its lifecycle. Quantities never appear physically at destination before receipt and reconcile exactly after partial delivery. |
| PROCUI-A02 | Compare Praha and Brno depot inventories for the same item. Company totals never make remote stock immediately usable at the other facility. |
| PROCUI-A03 | Project a normal replenishment and a stockout-before-arrival case from real duties/consumption and confirmed inbound. Forecast period/source/uncertainty are inspectable; no fixed universal percentage warning substitutes for it. |
| PROCUI-A04 | Configure a reorder rule with trigger, target, supplier, price/budget authority and fallback. Supplier capacity/transport/storage failure blocks or escalates the order rather than spawning stock. |
| PROCUI-A05 | Buy at source with buyer transport responsibility. Use own transport or open the canonical External Transport Order; no separate supply-delivery marketplace or teleport appears. |
| PROCUI-A06 | Use a recurring supply agreement with Auto-renew and a separate reorder threshold. Renewal alone creates no inventory/order; the reorder/order lifecycle remains distinct. |
| PROCUI-A07 | Trigger supplier shortfall after a larger commitment. Original terms/history remain, risk/confirmed change is distinguished and downstream depot/Line/maintenance effects link to the same root cause. |
| PROCUI-A08 | Inspect a supplier that also has another agreement with the player. Supplier view and UI-D27 expose the same stable company/agreement identities without leaking competitor contracts. |
| PROCUI-A09 | Link construction materials and maintenance parts into the procurement view. Project/job requirements remain owned by their canonical systems and quantities are not duplicated. |
| PROCUI-A10 | Save/load with a pending reorder trigger, accepted purchase, partial receipt and in-transit External Transport Order. No duplicate purchase, receipt, payment or stock appears; CZ/EN and enlarged UI remain usable. |

## 19. Decision record

| ID | Decision | Status |
|---|---|---|
| UI-D32 | Business procurement workspace with Inventory / Orders / Suppliers / Reorder rules, location-specific physical stock, projected shortage, recurring supply agreements, real transport responsibility, supplier relationship links and automation bounded by real supplier/capacity/budget constraints | CONFIRMED on 2026-09-30 |

UI-D32 complements UI-D01–UI-D31. GAME_DESIGN Section 18.6 remains authoritative for supply procurement and Section 30.1 for external transport.
