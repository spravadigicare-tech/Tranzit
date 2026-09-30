# Tranzit — Player-facing terminology glossary

> **Status: CONFIRMED terminology baseline, 2026-09-30.** This glossary fixes the normal Czech/English player-facing names of core simulation objects. It does not rename internal stable IDs, serialized types or code symbols. Contextual prose may use natural grammar, but must not blur distinct domain identities.

## Core transport and commercial objects

| Domain identity | Czech | English | Meaning |
|---|---|---|---|
| Line | **Linka** | **Line** | Player/company-defined transport service grouping. |
| Service Pattern | **Varianta linky** | **Service pattern** | A recurring operating variant of a Line with its own stops/calendar/service characteristics. |
| Trip | **Jízda** | **Trip** | One concrete dated execution/departure of a Service Pattern. |
| Duty | **Oběh vozidla** | **Vehicle duty** | Planned sequence of work for one vehicle/consist. |
| Crew Duty | **Směna posádky** | **Crew duty** | Aggregate crew work block/assignment. |
| Contract | **Smlouva** | **Contract** | Binding customer/business obligation. |
| Opportunity | **Příležitost** | **Opportunity** | Discoverable commercial possibility before a binding agreement. |
| Offer / Bid | **Nabídka** | **Offer / Bid** | Commercial proposal submitted or received in a context where the counterparty is explicit. |
| Shipment | **Zásilka** | **Shipment** | One commercial freight consignment. |
| CargoLot | **Část zásilky** | **Cargo portion** | Independently located physical portion of a Shipment. |
| TransportPlan | **Přepravní plán** | **Transport plan** | Versioned execution chain for moving a Shipment/obligation. |
| TripAllocation | **Přidělení k jízdě** | **Trip allocation** | Capacity committed to a specific Trip/segment for cargo or another obligation. |
| CapacityOrder | **Objednávka kapacity** | **Capacity order** | Request/order for infrastructure/station capacity for a Service Pattern. |
| Capacity Agreement | **Dohoda o kapacitě** | **Capacity agreement** | Accepted capacity/access arrangement resulting from the relevant workflow. |

## Company, assets and world

| Domain identity | Czech | English |
|---|---|---|
| Company | **Firma** | **Company** |
| Branch | **Pobočka** | **Branch** |
| Vehicle | **Vozidlo** | **Vehicle** |
| Fleet | **Vozidla** | **Fleet** |
| Depot | **Depo** | **Depot** |
| Workshop | **Dílna** | **Workshop** |
| Station | **Stanice** | **Station** |
| Stop | **Zastávka** | **Stop** |
| Terminal | **Terminál** | **Terminal** |
| Infrastructure | **Infrastruktura** | **Infrastructure** |
| Maintenance | **Údržba** | **Maintenance** |
| Procurement | **Nákup a dodavatelé** | **Procurement & suppliers** |
| Licence | **Licence** | **Licence** |
| Permit | **Povolení** | **Permit** |
| Technology | **Technologie** | **Technology** |
| City | **Město** | **City** |
| Region | **Region** | **Region** |
| News | **Zprávy** | **News** |

## Top-level navigation

| Czech | English |
|---|---|
| **Stavět** | **Build** |
| **Provoz** | **Operations** |
| **Obchod** | **Business** |
| **Majetek** | **Assets** |
| **Firma** | **Company** |
| **Svět** | **World** |
| **Vrstvy** | **Layers** |
| **Události** | **Events** |

## Usage rules

- Do not use **Jízda / Trip** for a Line or timetable template. A Trip is one concrete dated execution.
- Do not use **Zásilka / Shipment** for an individual physical split portion; that is **Část zásilky / Cargo portion**.
- Do not use **Smlouva / Contract** for an Opportunity, Offer or non-binding draft.
- **Varianta linky / Service pattern** remains distinct from both the parent Line and its dated Trips.
- **Oběh vozidla / Vehicle duty** is distinct from **Směna posádky / Crew duty**.
- **Objednávka kapacity / Capacity order** is a request/workflow; an accepted right/agreement is not still merely an order.
- In compact contextual text, natural shorter wording is allowed when identity is already unambiguous, e.g. “dnešní jízda 10:20”, but object headers, links, filters and help should use the canonical term.
- Internal stable English IDs and serialized/code names do not change because of localization.
- Do not expose raw type names such as `CargoLot`, `TransportPlan` or `CapacityOrder` to the player unless in developer/debug surfaces.
