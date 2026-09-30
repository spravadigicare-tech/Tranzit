# Tranzit — Map layers and opportunity discovery UI

> **Status: CONFIRMED UI DIRECTION — UI-D21, 2026-09-30.** The player accepted purpose-based map layers and explicitly required them to reveal opportunities, not only diagnose problems. This focused specification promotes the map-layer outline in UI_UX_DESIGN Section 8 to a confirmed direction, including the opportunity-discovery requirements below. Exact visual tokens, thresholds, column widths and localized labels remain design work. This is a specification, not an implemented or tested UI.

Read with [UI_UX_DESIGN.md](UI_UX_DESIGN.md), particularly UI-D07 (windows), UI-D09 (exact-object links), UI-D15 (minimalism and tooltips) and the pause rules. This document owns map-layer presentation. [UI_COMMERCIAL.md](UI_COMMERCIAL.md) owns the existing Opportunity Board and commercial workflow; there is no second market or duplicate opportunity database. [GAME_DESIGN.md](GAME_DESIGN.md), Sections 2, 6–12, 17–28 and 32, owns geography, discovery, demand, capacity, facilities and operations. [V1_SCOPE.md](V1_SCOPE.md) retains the release boundary.

## 1. Purpose and entry point

**The map must help the player decide both what to fix and where to grow.** Opportunity discovery is a normal map workflow, not a hidden tooltip, an incident-only filter or a later optional enhancement. A player with a healthy network must still find useful reasons to inspect these layers.

Keep the normal world visually clean. A compact **Layers / Vrstvy** control at the bottom-bar area opens the layer selector without replacing the map, closing windows or moving the camera. Selecting a layer shows its name, legend, relevant filters and a clear Off / Vypnout control. Switching it off restores the normal map while preserving window and camera context.

Use one primary analytical layer at a time by default, rather than overlapping several incompatible colour meanings. The selected Line, object or inspected connection can remain highlighted as context. Switching or clearing a layer never changes the selected simulation speed or pause state.

## 2. Layer groups

| Layer | Purpose and information |
|---|---|
| Lines and network / Linky a síť | Actual Line routes, stops and connections, with own/selected-Line and rail/road filters where relevant. Separate operating services from explicit planning previews. |
| Capacity and restrictions / Kapacita a omezení | Relevant section/facility utilization, closures, queues and compatible spare capacity. Distinguish current occupancy from reservations and planned use in a stated period. |
| Ownership and access / Vlastnictví a přístupy | Asset ownership separately from the player's usable rights, contracted access and restrictions. Spare physical space is not automatically available for purchase or public use. |
| Demand and opportunities / Poptávka a příležitosti | Known passenger/cargo demand, discoverable business offers, service gaps and evidence-backed ways to use or extend the player's network. See Section 3. |
| Facilities and commercial coverage / Zázemí a obchodní pokrytí | Select one relevant subview: operating bases, maintenance, energy/supply, handling, or actual branch commercial coverage. Do not merge these different capabilities into a universal coverage radius. |
| Construction and plans / Stavby a plány | Saved unstarted proposals, started works and completed infrastructure as separate states. Use line style/pattern as well as colour; a draft is not a reserved corridor or usable track. |

Filters are task-specific and combinable within the active layer. Do not require a player to use every filter before seeing useful information. Exact control placement and decorative treatment remain visual-design work under UI-D15.

## 3. Demand and opportunities are first-class

### 3.1 Explicit offers versus potential

Distinguish two fundamentally different things:

- **Available business:** an actual discoverable job, customer request or tender from the existing Opportunity Board, with the same identity, terms, eligibility and deadline.
- **Potential to investigate:** a signal derived from available demand, service history or the player's own capacity. It is not a signed customer, a guaranteed contract, a reservation or proof of profit.

The default layer should make both discoverable with a clear legend and simple category filters. Suggested filters are Passenger / Freight, Available jobs, Service gaps, Use own capacity, and Growth/seasonal demand. These are filters of existing data and its explanation, not new types of simulated customers or a separate strategy-scoring system.

### 3.2 Opportunity cases to support

| Opportunity | What the map should explain | Contextual next step |
|---|---|---|
| A discoverable job or tender | Who needs transport, origin/destination, relevant quantity or service requirement, deadline and current known feasibility | Open the exact opportunity in the existing Contract Planner |
| An underserved passenger connection | Known demand between places or at a time of day compared with available service, including observed waiting or denied boarding where known | Inspect the demand and relevant Lines; prepare a new Line or a future change |
| Freight demand without a suitable known service | Commodity, direction, quantity/time basis, handling needs and the known transport gap | Open the customer/job when available, or investigate a Transport Plan |
| Better use of own services, including return journeys | A selected Line/Trip/duty has compatible uncommitted capacity and a discoverable demand source could fit its direction and timing | Inspect the candidate opportunity and shared-capacity feasibility; no automatic loading or booking |
| Growth, a new known customer or a seasonal peak | The available source data indicates growing or time-limited demand, with period, direction and forecast uncertainty | Inspect the source and prepare an additional service, changed frequency or another existing planning option |
| A connection or facility investment to investigate | Known demand and network/handling constraints suggest an interchange, endpoint or capacity improvement could help | Open relevant stations, access terms or a saved construction proposal for evaluation |

A service gap is not established merely because there is no direct Line or no player-owned Line. Existing transfers, rival services, other modes, time windows and available demand matter to the extent known. Likewise, idle vehicles or empty return capacity alone do not prove there is paying work. An infrastructure extension is not automatically the recommended answer when an existing service or rented access can meet the need.

Use only the data already supported by the simulation and the player's knowledge. If enough evidence for a case is not available, show the limitation and allow investigation; do not generate a fabricated opportunity marker. These cases do not authorize a new all-network profit optimizer or exact forecasts in every era.

### 3.3 Presentation on the map

Use restrained, distinguishable markers and contextual origin-to-destination connections rather than a map permanently filled with arrows. A city or firm marker can summarize several related opportunities; selection reveals a compact list and the relevant directions. At wider zoom, cluster or aggregate; at closer zoom, expose the actual known locations. Mark approximate or regional data as such rather than inventing a precise endpoint.

Magnitude or intensity must have an inspectable meaning, such as known volume over the selected period or observed unmet demand. Do not present an opaque universal opportunity score. Keep passenger counts, cargo mass/volume, revenue estimates and already-reserved loads separate; they cannot share one unexplained scale.

Provide a compact expandable list of the opportunities represented in the current map scope. It shares filters and identities with the markers. This makes the view usable without finding every small symbol or relying only on hover. Selecting a row highlights its known map context without starting a business action. Related sources and existing details use UI-D09; explicit Locate remains distinct from opening a linked object.

### 3.4 What an opportunity explains

The concise hover/focus explanation and click-open detail should answer:

| Question | Required presentation |
|---|---|
| What is the opportunity? | Plain description and explicit offer-versus-potential label |
| Why is it shown? | Concrete source: customer request, demand observation, queue history, known growth or compatible spare capacity |
| Where and when? | Known origin/destination or area, relevant dates/time windows and reporting period |
| How much is known? | Quantity and units when supported; actual, forecast, incomplete and stale data clearly distinguished |
| What is missing? | Main known licence, coverage, endpoint, fleet, staff, access or capacity dependency; not a hidden all-green claim |
| What can the player do next? | Open the real job/customer, inspect demand, evaluate against a selected service, or prepare an existing Line/Transport Plan/construction proposal |

Illustrative presentation, not fixed balancing or a generated job:

> Potential: improve morning service between two towns.
>
> Known demand exceeds available seats in the displayed morning period. Some passengers remain waiting after departures.
>
> Inspect demand · Open affected Line · Prepare change

Another example:

> Potential: use the return leg of an existing freight service.
>
> A known request goes in the return direction. Suitable spare capacity may exist, but its time window and loading access still need checking.
>
> Open request · Check against this Line

No guaranteed-profit badge is implied. Only show a margin estimate after the existing planner has enough cost, access, timing and demand information, and label its assumptions. A customer asking for transport is not necessarily offering acceptable terms, and a forecast volume is not guaranteed revenue.

## 4. Safe handoff to planning

Opening an opportunity marker or source detail is navigation. Explicit Prepare Line / Prepare change / Evaluate transport actions may prefill an editable proposal using the selected known context, but must not overwrite another draft, submit a bid, activate a service, acquire land or reserve resources.

Reuse the Contract Planner and Opportunity Board for actual offers. Reuse Line cards for service plans and versioned changes, the Transport Plan for multi-leg fulfilment, and the construction planner for real infrastructure proposals. There is no map-only pricing, matching, bidding, dispatch or capacity ledger.

Any compatibility hint is scoped to the selected mode/cargo, direction, service version and date or planning horizon. Revalidate after relevant changes and before an accepted command. Infrastructure slots, compatible fleet capacity, physical empty space and actual free commercial capacity are different facts. Protected or already booked capacity cannot become an opportunity for double sale.

An existing obligation to recover delayed cargo remains a real problem/commitment, not a new optional revenue opportunity. Opportunities use distinct icon/label semantics from critical incidents and do not trigger critical-event pause merely because the player views them. An already qualifying critical incident still follows the shared incident rules independently.

## 5. Knowledge, time and world boundaries

Map discovery follows the same branch, communication, customer and public/direct-opportunity rules as GAME_DESIGN Section 7.2 and the Opportunity Board. Filters do not reveal ordinary unknown local jobs outside commercial coverage, competitor-private contracts or exact inventories. Publicly known regional growth may justify an investigation without revealing confidential jobs or guaranteeing permission to operate there.

Unknown information is not zero demand. Display the available source, coverage, timestamp and precision where relevant. If knowledge or a time-critical offer becomes stale or unavailable, update its state and preserve useful history without suggesting it is still accepting bids. Do not reset its deadline when the map is reopened.

Demand needs an explicit direction and temporal scope where these affect decisions. A seasonal market, commuting peak and one-off deadline are not interchangeable with a year-round service. Use the shared 14-day-month game calendar. Historical availability and adopted company information systems remain meaningful; the map's modern appearance grants neither modern forecasting nor passenger information equipment.

Inactive regions retain their macro simulation and available information level. Opening a layer, zooming or selecting a public signal does not unlock a region, run detailed hidden Trips there or grant commercial access. Any proposed service still goes through the existing market-entry, local-presence, licensing and physical feasibility checks.

## 6. Readability, state and performance

Legends state what colours, patterns, symbols and quantities mean. Do not reuse Line-identification colours as the sole warning/opportunity cue. Show live/planned/forecast scope and active filters; provide a direct return to the ordinary world view. Construction ghosts and proposed services stay distinguishable from completed or active infrastructure/services even without colour.

Use reusable hover/focus explanations with a click-open alternative under UI-D15. Main actions and material warnings stay discoverable. Test Czech/English text, 1080p and enlarged UI without covering the essential bottom controls. Clicking UI cannot place infrastructure or pan the world behind it. The layer does not reintroduce an embedded station/depot schematic or a second live camera.

Use event-driven updates, existing demand/history aggregates, caches and bounded visible-scope queries. Do not evaluate every possible city pair, customer, vehicle and price combination every frame. Cheap signals may remain unevaluated until the player opens a relevant planner. Preserve stable source identities, filters and selection through refresh; several views of one job or physical load must not inflate totals.

After save/load, restore useful layer/filter preferences with valid references, not a second world state. Revalidate stale signals; restoring or hovering a marker does not create cargo, reserve capacity, submit an order or activate a draft. Ordinary layer interaction remains available during manual and critical-event pause without advancing time.

## 7. Acceptance evidence to collect

These scenarios define evidence still to collect on an implemented build. Documentation checks do not demonstrate them.

| ID | Required scenario |
|---|---|
| MAPUI-A01 | Toggle each layer with existing floating windows open. Verify one primary analytical layer, relevant filters, legend, explicit Off, retained camera/selection and no pause/speed or gameplay changes. |
| MAPUI-A02 | On a healthy network with no critical incident, find a real discoverable job and an evidence-backed expansion/underused-capacity signal. Opportunity access must not depend on finding an error or opening an incident list. |
| MAPUI-A03 | Compare unmet passenger demand, a known freight request, a compatible return-leg opportunity and seasonal growth. Each exposes its source, direction, units, period, knowledge limits and a suitable existing planning action. Empty capacity alone does not create a job or promise profit. |
| MAPUI-A04 | Inspect an indirect connection and a market already served by a competitor. Absence of a direct/player Line alone is not reported as absence of service. Distinguish potential, forecast and contractual quantities. |
| MAPUI-A05 | Open the same job from map/list/Opportunity Board and verify one identity and current terms. Prefill a proposal without replacing a saved draft or submitting/activating it. Award, expiry or stale capacity requires current-state revalidation. |
| MAPUI-A06 | Inspect an uncovered city, a public opportunity and an inactive region. No unknown ordinary jobs, confidential rival data or detailed inactive-world operations are revealed. Missing data is distinct from zero demand, and visible potential grants no access rights. |
| MAPUI-A07 | Compare physical occupancy, planned compatible use, existing protected reservations, drafts and completed infrastructure. No double-sale, phantom vehicle, draft corridor reservation or premature operating service is implied. |
| MAPUI-A08 | Test clustered markers, a large visible result set, filters, keyboard/focus tooltips, CZ/EN, enlarged UI, pause and save/load. Keep source identity/counts, valid input routing and bounded/event-driven evaluation. |

## 8. Decision record

| ID | Decision | Status |
|---|---|---|
| UI-D21 | Clean default map, purpose-based layers with one primary analysis and explicit scope/legend; opportunity discovery alongside diagnostics, including actual known offers and evidence-backed growth/capacity potential with direct planning links | CONFIRMED on 2026-09-30 |

UI-D21 confirms the map-layer direction previously outlined as proposed in UI_UX_DESIGN Section 8. It does not change discovery permissions, economics, demand generation, protected capacity, region unlocking or earlier window/tooltip decisions. Remaining exact styling and optional refinements are not silently approved.
