# Tranzit — External company relationship and agreements UI

> **Status: CONFIRMED UI DIRECTION — UI-D27, 2026-09-30.** The player explicitly required that the detail of another company expose **all agreements between that company and the player's company**. This decision confirms the bilateral relationship/agreement presentation only; the broader World/city/company screen composition remains open until separately accepted. Exact visual dimensions, column widths and localized labels remain design work. This specification is not an implemented or tested UI.

Read with [UI_UX_DESIGN.md](UI_UX_DESIGN.md), especially UI-D09 (exact-object links), UI-D15 (minimalism/tooltips), UI-D17 (commercial contracts), UI-D19 (finance), UI-D24 (events) and UI-D26 (capacity/access). [GAME_DESIGN.md](GAME_DESIGN.md) owns the actual customer, partner, supplier, infrastructure, facility, leasing, service and other agreement mechanics. This document must not create a duplicate contract system merely to make the company detail complete.

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
- through-ticket / protected-connection partnership agreements;
- infrastructure access agreements;
- rail/station Capacity Orders and related capacity agreements;
- station/terminal/depot/workshop/facility rental or service access;
- maintenance/service agreements;
- fuel/material/supply agreements;
- vehicle lease/rental agreements;
- property/infrastructure lease or access arrangements;
- connection agreements;
- other accepted bilateral contracts/committed orders already defined by the core game.

This list is illustrative, not permission to invent a new agreement type.

A vehicle purchase, infrastructure sale or other completed one-off transaction may remain visible in **History** when the underlying system records a transaction/agreement, but it is not presented as an active recurring agreement after completion.

Quotes, discovered opportunities, draft bids and unaccepted proposals are not active agreements.

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

A pending quote is not an accounts payable item. A forecast customer volume is not receivable cash.

## 9. Permissions and privacy

Because the player is a party to **our agreements**, their own accepted terms are inspectable even when the counterparty is a private company.

This does not reveal:

- the counterparty's agreements with unrelated competitors;
- private bids from other carriers;
- internal costs/margins;
- private fleet commitments unrelated to the player's contract;
- confidential customer/supplier relationships to which the player is not a party.

Publicly available information can still appear through normal world/company information rules.

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

| ID | Required scenario |
|---|---|
| EXTCO-A01 | Give one external company simultaneous roles as customer, station/facility provider and subcontracting partner. Its detail exposes all player-company agreements in one place without duplicating the underlying contracts. |
| EXTCO-A02 | Show Active, future committed, pending proposal/renewal and historical agreements together. Pending proposals never grant active rights/revenue/capacity. |
| EXTCO-A03 | Open an agreement from the external company, then follow links to Line/station/Finance and back. Every view resolves the same stable agreement identity and values. |
| EXTCO-A04 | Use a multi-owner Capacity Order. Each owner's company detail shows only its own component(s) and links to the coordinated order without claiming full-route coverage. |
| EXTCO-A05 | Verify the counterpart's unrelated private contracts, bids, costs and fleet commitments remain hidden while the player's own agreement terms stay inspectable. |
| EXTCO-A06 | Expire, renew, terminate and complete several agreements, then save/load. Status/history, financial state and counterpart relationships persist without duplicate contracts or postings. |
| EXTCO-A07 | Verify CZ/EN, enlarged UI, filters and large history. Material terms/actions remain accessible without hover-only dependence or rendering every historical record continuously. |

## 14. Decision record

| ID | Decision | Status |
|---|---|---|
| UI-D27 | Every external-company detail provides a directly accessible, complete view of all agreements between that company and the player's company, with active/future/pending/history separation and links to each canonical owning workflow | CONFIRMED on 2026-09-30 |

UI-D27 does **not** by itself confirm the broader proposed World/city/company dashboard. It only locks the bilateral company-relationship/agreement requirement so any later World UI must include it.
