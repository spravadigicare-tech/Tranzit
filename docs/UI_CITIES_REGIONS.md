# Tranzit — City, region and world-context UI

> **Status: CONFIRMED UI DIRECTION — UI-D28, 2026-09-30.** The player accepted a City detail and a higher-level Region view centred on population/economic context, directional passenger/freight demand, transport network, opportunities, the player's local presence and public-authority relationships. City/region information must respect what the player's company can actually know, and municipal agreements must be directly accessible. Exact visual dimensions, charts, thresholds and localized labels remain design work. This specification is not an implemented or tested UI.

Read with [UI_UX_DESIGN.md](UI_UX_DESIGN.md), especially UI-D09 (exact-object links), UI-D15 (minimalism/tooltips), UI-D20 (company/branches), UI-D21 (map opportunities), UI-D24 (events), UI-D26 (capacity/access) and UI-D27 (bilateral agreements with external companies). [GAME_DESIGN.md](GAME_DESIGN.md), especially Sections 2, 6–10, 28 and 33–35, owns world simulation, city growth, passenger choice/demand, industrial/economic state, knowledge/communications, municipal permissions/contracts and macro events. This document defines presentation only.

## 1. City detail

Clicking a city from the map, a Line, opportunity, branch, contract or another linked object opens a normal movable/resizable City detail window.

The default overview answers:

1. What is this city and how is it changing?
2. What transport demand and economic activity are relevant?
3. What transport already serves it?
4. Where are the known opportunities or constraints?
5. What presence, rights and agreements does the player's company have here?

Keep the top area concise. Illustrative presentation:

> **Brno**
>
> Population: 238,000 · growing
>
> Our presence: branch · 6 Lines · 2 used terminals
>
> Opportunity: growing commuter demand toward Vyškov
>
> Constraint: main rail station has little compatible morning-peak capacity

Only show claims the simulation actually supports. “Growing” or “limited capacity” must have an inspectable source/period.

## 2. City cards

Use independently openable cards:

| Card | Content |
|---|---|
| Population and demand / Obyvatelstvo a poptávka | Current population, change over time, important trip purposes/flows, time-of-day/seasonal patterns and known unmet demand |
| Companies and industry / Firmy a průmysl | Significant known firms/facilities, production/consumption roles, known transport needs and direct company details |
| Transport network / Doprava | Stations/terminals, relevant infrastructure and visible services/operators serving the city |
| Opportunities / Příležitosti | Discoverable jobs/tenders, known passenger/freight gaps and evidence-backed potential from UI-D21 |
| Our presence / Naše působení | Branches, Lines/Patterns, facilities, commercial coverage, licences/permissions and dependencies in the city; legal gaps open the canonical UI-D33 Licences and expansion workflow |
| City and authority / Město a autorita | Municipal relationship, public development/transport priorities, permissions/concessions, public-service contracts, public infrastructure/access and all agreements between the city/authority and the player's company; permit/application detail reuses UI-D33 |

Hide cards/subsections that truly have no relevance, but do not hide a material missing licence, municipal requirement or active agreement.

## 3. Demand is directional and time-scoped

Do not present only a generic city-level “Demand: High” score.

Passenger demand should be inspectable as origin-destination flows with a relevant period/time context.

Illustrative example:

> **Brno → Vyškov**
>
> Morning work peak
>
> Known demand: 680 passengers / displayed period
>
> Known compatible service capacity: ~510
>
> Our compatible capacity: 120
>
> Observed/estimated unmet preferred demand: 160–190

Available actions can include:

- Show on map;
- View existing services;
- Open affected Line;
- Prepare Line change;
- Prepare new Line;
- inspect demand basis.

The exact figures above are examples only.

A demand gap is not equivalent to guaranteed demand for the player's service. Existing competitors, transfers, price, frequency, reliability, travel time, capacity, private motoring and other actual alternatives still matter.

Show which part of the demand is:

- observed from actual waiting/boarding/Trip history;
- estimated from the passenger-demand model;
- forecast for a future period;
- unknown/incomplete.

A forecast is not a reservation or guaranteed revenue.

## 4. Passenger-flow explanation

Where the simulation knows broad trip purpose/segment, allow inspection of why a flow exists, for example:

- commuting/work;
- school/study;
- business;
- leisure/tourism;
- event/market-day;
- another historically appropriate purpose.

Do not turn this into individual-person simulation.

The UI can explain why one flow prefers an existing alternative using the actual passenger-choice factors from GAME_DESIGN, such as:

- travel time;
- frequency;
- reliability;
- transfers;
- price;
- comfort/crowding;
- operator/service reputation.

Do not hide a passenger decision behind one universal demand or service-quality score.

## 5. Freight and industrial context

A city is also a gateway to its economic entities.

The Companies and industry card lists significant **known** firms/facilities with concise roles, for example:

> **Pražské strojírny**
>
> Produces: machinery
>
> Known major inputs: steel, coal
>
> Known transport demand: 180 t / displayed period
>
> Main known flow: Praha → Brno

Clicking opens the exact external-company/facility detail.

The city screen does not expose every firm's exact inventories, future orders, private contracts, internal margins or supplier list unless the player's information rights actually provide them.

Use the external-company UI-D27 requirement: where the player has agreements with a selected company, **Our agreements / Naše dohody** are directly accessible from that company's detail.

## 6. Transport network

The Transport card gives a concise local transport picture.

Relevant information can include:

- passenger/freight stations and terminals;
- major road/rail infrastructure;
- Lines/Patterns calling in the city;
- visible operators;
- important interchanges;
- known congestion/capacity constraints;
- major construction/disruption;
- relevant route/access ownership.

Do not transform the city detail into a second map. Provide **Show on map** and use UI-D21 layers for spatial analysis.

For other operators, respect public/private information boundaries. A public service and communicated timetable can be visible while private costs, fleet reserve and customer contracts remain hidden.

## 7. Opportunities inside the city

The City opportunity view reuses the same identities/data as UI-D17 and UI-D21.

Separate:

- actual discoverable Opportunity Board jobs/tenders;
- evidence-backed passenger/freight potential to investigate;
- public municipal tenders/concessions;
- known capacity/facility investment opportunities.

Do not generate a duplicate city-only opportunity database.

Example potential:

> Morning capacity toward Vyškov is consistently below known demand.

This can open demand evidence and existing services, then a Line planner.

Example actual offer:

> Municipal tender: local bus network expansion.

This opens the canonical commercial opportunity/tender detail.

Opportunity discovery still follows branch/commercial-coverage and communications rules. A city filter cannot reveal hidden routine private jobs merely because the city window is open.

## 8. Our presence

The city detail directly summarizes the player's actual footprint:

- active branch(es) and commercial coverage;
- Lines/Patterns serving the city;
- owned/rented stations, terminals, depots, workshops or other relevant facilities;
- infrastructure owned or accessed;
- municipal/region licences and activity permissions;
- station/route/access agreements;
- current public-service/customer contracts tied to the city;
- relevant construction projects.

Each item links to the canonical object detail.

Distinguish:

- **commercial coverage**;
- **activity licence**;
- **municipal permission/concession**;
- **physical endpoint/facility access**;
- **infrastructure capacity/access**.

One does not imply another.

If the player currently cannot commercially serve the city, the UI explains the missing reason, such as:

> Local presence required under current company operating model.

or:

> Passenger activity licence missing.

or:

> Municipal operating permission required for this urban service.

## 9. City authority and our agreements

A city/municipality/public authority can interact with the player's company in several roles:

- regulator/authority;
- customer;
- public-service commissioner;
- infrastructure/station/road owner;
- landlord/facility provider;
- grantor of concession/permission;
- construction/land authority where applicable.

The City and authority card must provide a directly accessible **Our agreements with the city / Naše dohody s městem** list.

This follows the same identity/lifecycle principles as UI-D27:

- Active;
- Future committed;
- Pending;
- History.

Possible canonical items include, where actually defined by the simulation:

- municipal public-transport contract;
- city operating permission/concession;
- station/bus-terminal access;
- office/facility rental;
- public infrastructure capacity/access;
- public construction/land agreements;
- public tender award;
- other accepted bilateral municipal agreement.

Example:

> **Our agreements with Brno**
>
> Municipal bus concession — Active
>
> Bus-terminal access — Active
>
> Public-service Line 17 contract — Active
>
> New-stop approval — Pending

Do not create one fake umbrella “city contract” when the simulation contains several distinct agreements.

Pending approval does not grant the right before approval.

### 9.1 Public priorities and prospective tenders

Cities, regions and states can expose a small, readable set of **current public priorities** before a concrete tender exists. Examples include improving a weak intercity passenger connection, increasing freight-corridor capacity, serving an underconnected area or supporting a strategically important economic corridor.

A priority shows the real public problem/evidence, its geographic/service scope, relative importance and state such as **Monitoring**, **Considering intervention**, **Preparing tender** or **Addressed**. Where supported, show the relevant demand/capacity/economic evidence rather than a hidden authority desire score.

A priority is **not a promise that a tender will be issued** and does not reserve budget/capacity. If the authority later advertises a concrete service tender, that tender appears as the same canonical public Opportunity in Business → Opportunities.

The same legitimately known priority objects are aggregated in **World → Public priorities** so a larger company can scan known state/regional/municipal goals without opening every city. The central list links back to the owning authority/area and never reveals undiscovered private opportunities.

## 10. City history and trend views

Important values can expose historical development, for example:

- population;
- jobs/economic activity where supported;
- major passenger-flow magnitude;
- industrial output/activity;
- transport accessibility;
- waiting/denied boarding;
- network/service capacity;
- selected local reputation/relationship indicators.

Default view remains compact:

> Population: 238,000 ↑
>
> Change over last 3 game years: +6.4%

Clicking opens the trend/detail. Exact period choices are design work but must use the shared 168-day game year.

Explain major known drivers where the simulation supports them, such as:

- historical baseline;
- employment change;
- industrial growth/decline;
- improved/worsened accessibility;
- goods supply;
- broader regional economy.

Do not claim one cause when growth actually comes from several factors.

## 11. Region view

A Region view is a higher-level **aggregation/navigation layer**, not a new simulation subsystem.

It summarizes cities and relevant world/economic/transport state within the selected region.

Illustrative header:

> **Jižní Morava**
>
> 7 cities in active scope
>
> 3 company branches
>
> 14 operating Lines
>
> Main known growth flow: Brno–Vyškov
>
> Main network constraint: Brno main station
>
> Main known freight opportunity: Brno–Břeclav industrial corridor

Use compact cards:

- Cities;
- Economy;
- Transport;
- Opportunities;
- Public priorities;
- Our network/presence.

The Region view should help answer **where to inspect next**. It must not replace City, company, station, Contract or Line details.

## 12. Region aggregation rules

Region summaries must preserve the meaning of underlying data.

Do not:

- sum incompatible passenger flows into one unexplained “demand” number;
- add repeated transfer legs as unique passengers;
- count one Line once per city and call that the number of unique Lines unless explicitly labelled;
- mix player-owned and third-party infrastructure;
- treat unknown cities as zero opportunity;
- imply a regional average represents every local market.

Every aggregate shows its unit, period and scope.

When an aggregate is driven mostly by one city/corridor, allow direct drill-down to that source.

## 13. Knowledge and information provenance

The city/region UI must never become a cheat encyclopedia.

Classify displayed information where relevant as:

- **publicly known** — population, major infrastructure, public operators/services, public tenders or generally known major firms;
- **observed** — waiting queues, actual service history, the player's own sales/transport/operations;
- **commercially known** — discovered customers/opportunities available through the player's branch/communications coverage;
- **contractual** — information the player knows because it is party to an agreement;
- **estimated/forecast** — modelled future/current estimates;
- **unknown/unavailable** — information the player cannot currently know.

Exact labels/icons can be refined, but uncertainty/source must be inspectable and material estimates identifiable without relying only on tooltip.

The modern interface appearance must not grant modern real-time data in 1900. Available precision, delay, geographic reach and forecast quality follow historical/company technology under GAME_DESIGN Section 28.

## 14. World and inactive-region boundaries

City/region details in inactive or macro-simulated areas expose only the allowed aggregate/public information level.

Opening a city/region window or map layer does not:

- instantiate all local Trips;
- unlock commercial coverage;
- grant licences;
- expose private opportunities;
- create detailed passenger queues that were not simulated;
- grant infrastructure access.

When the player later enters/activates a region through the existing world/market-entry rules, additional detail can become available from the same stable city/company identities where supported.

## 15. Map integration

City and Region windows provide explicit map actions:

- Show city/region;
- show selected demand flow;
- show our network/presence;
- show opportunities;
- show capacity/restrictions;
- show facilities/coverage.

These actions reuse UI-D21 map layers. They do not create separate rendering/analysis semantics.

Selecting a demand flow can highlight origin/destination and relevant known services/alternatives. It does not automatically create a new Line proposal.

## 16. Save/load and live updates

Persist stable City/Region identities, knowledge state/provenance where needed, player-company relationships/agreements and selected UI context.

After save/load:

- discovered opportunities remain the same canonical objects unless expired/changed by simulation;
- hidden opportunities are not accidentally revealed;
- historical city/region data remains consistent;
- trend lines do not reset because the window was closed;
- municipal agreement state remains canonical;
- map selection/filter state can restore without changing game authority.

Live city growth or demand updates preserve selection/scroll and do not constantly reorder the screen while the player is reading.

## 17. Acceptance evidence to collect

| ID | Required scenario |
|---|---|
| CITYUI-A01 | Open a City with branches, Lines, multiple operators, stations and several firms. The overview exposes population/change, our presence, one meaningful opportunity/constraint and direct task cards without becoming a giant dashboard. |
| CITYUI-A02 | Inspect passenger demand between several city pairs/time periods. Flows distinguish observed/estimated/forecast state, existing alternatives and compatible capacity; a gap never guarantees the player's future revenue. |
| CITYUI-A03 | Inspect a city firm with known freight needs and then its external-company detail. Public/commercially known data is visible, private inventories/contracts remain hidden and UI-D27 Our agreements is complete. |
| CITYUI-A04 | Open City authority with a public-service contract, concession, terminal-access agreement and pending approval. Our agreements with the city shows all canonical items with active/future/pending/history separation and no fake umbrella contract. |
| CITYUI-A05 | Compare city trend values across several game years and inspect causal contributors. Period/unit/source remain explicit and no modern data precision is granted in an early era. |
| CITYUI-A06 | Open Region and drill from a regional flow/constraint/opportunity into City, Line, company, station and map-layer detail. Aggregates reconcile and do not double-count Lines/passengers/cargo. |
| CITYUI-A07 | Open a macro/inactive-region city. The view stays at its allowed information level and does not instantiate detailed hidden operations, opportunities or customer inventories. |
| CITYUI-A08 | Change branch coverage, licence/permission, a municipal agreement and a Line serving the city, then save/load. Our presence and authority/agreement views update without duplicate rights or lost history. |
| CITYUI-A09 | Verify CZ/EN, enlarged UI, map highlighting and paused/running inspection. Browsing or comparing city/region data performs no contract, construction, capacity or time-control action. |

## 18. Decision record

| ID | Decision | Status |
|---|---|---|
| UI-D28 | City detail with population/demand, firms/industry, transport, opportunities, player presence and municipal authority/agreement views; directional/time-scoped demand; trend history; Region as a higher-level aggregation/navigation view; all information respects knowledge provenance | CONFIRMED on 2026-09-30 |

UI-D28 complements UI-D01–UI-D27. It does not change city growth, passenger demand, industrial production, opportunity discovery, municipal contract/permission mechanics, region activation or information-technology rules.
