# Tranzit — Living Game Design

> **Status:** Living source of truth. This document describes the current agreed design. It is not a chronological idea log.
>
> **Maintenance rule:** Before adding or changing any feature, review all affected sections and resolve contradictions. Remove or rewrite obsolete decisions instead of appending conflicting alternatives.
>
> **Related specifications:** [V1_SCOPE.md](V1_SCOPE.md) defines the approved first-release boundary; this document also covers the wider base game. [CONTRACT_CANCELLATION.md](CONTRACT_CANCELLATION.md) owns proportionate cancellation and early-capacity-release rules. Detailed cargo and vehicle-availability rules are centralized here in Sections 11.9 and 15.11. Document responsibilities are defined in [AGENTS.md](../AGENTS.md).

## 1. Vision

Tranzit is a long-form transport and business simulation built in Unity. The base game starts around **1900**, with selectable new-game years **1900, 1925, 1950 and 1975**. The player starts as a small regional carrier and can grow into a multinational transport group. Campaign duration follows the unified time model in Section 3; there is no fixed short completion-time target.

The game should feel like a living model railway / model world viewed from above: a large stylized but believable Central European world that changes physically, economically and technologically over decades. The earlier playable period, originally envisaged from around 1820, is reserved for the first planned DLC, **Early Ages**, rather than the base-game starting experience.

Core pillars:

1. **Physical continuity** — vehicles, rolling stock and infrastructure physically exist in the world. They do not teleport, magically reverse direction or disappear into menus.
2. **Deep but scalable simulation** — the economy, cities, industries, passengers and competitors should feel alive, but use aggregation, event-driven logic, caching and simulation LOD instead of brute-force per-agent simulation.
3. **Historical technological progression** — technology changes what the player can build, how the company is managed and what markets exist.
4. **Progressive delegation** — early game is hands-on; later, managers, dispatchers and information systems automate increasingly large parts of the company.
5. **Dynamic economy** — transport demand should emerge from companies, cities, supply chains, passengers, state contracts and technology rather than from arbitrary cargo generators.
6. **Infrastructure matters** — depots, terminals, stations, sidings, turning facilities, maintenance bases, storage, access rights and track capacity are gameplay, not decoration.
7. **The world responds to the player** — good transport can change city growth, industrial geography and regional prosperity.
8. **Explainable simulation** — important outcomes must be traceable to visible rules, inputs and state. Avoid hidden modifiers and opaque scores when the player can instead be shown why something happened.

### 1.1 Explainability and no hidden mechanics

Tranzit should avoid **hidden gameplay mechanics**.

Whenever a system materially affects the player's operation, finances, demand, reputation, reliability, contract outcome or feasibility, the UI should expose the important reasons behind that result.

The player does not need to see every internal calculation by default, but must be able to inspect the causal chain.

Examples:

> Line attractiveness decreased  
> - average delay increased from 3.1 to 7.4 min  
> - 6.2% of protected connections were missed  
> - passenger comfort fell because Standard cleaning was skipped on 18% of recent Trips

> Contract bid ranked poorly  
> - price: competitive  
> - historical reliability: below customer target  
> - insufficient guaranteed reserve capacity  
> - strong competitor relationship with customer

> Trip cannot depart  
> - compatible locomotive unavailable  
> - reserve locomotive is in maintenance until 06:42  
> - next compatible locomotive can reach the station at 07:05

Do not hide material outcomes behind unexplained values such as:

- generic "+10% efficiency";
- unexplained reliability penalties;
- invisible relationship modifiers;
- arbitrary AI preference;
- opaque feasibility failures.

Where an aggregate score is useful for readability, it must remain drillable into the real contributing factors.

#### UI explanation pattern

The long-term UI should support contextual explanations through **hover/focus tooltips** and linked highlighted terms.

A tooltip can contain highlighted concepts that themselves expose a second contextual explanation after a short intentional hover/focus delay, similar to nested glossary/tooltips used in complex strategy games.

This is a future UI interaction pattern rather than a requirement to implement immediately, but the simulation/data model should preserve enough source information to support it.

Tooltip nesting must remain controlled:

- use it for meaningful game concepts and causal explanations;
- avoid infinite/deep chains;
- keep the first layer concise;
- allow the player to lock/pin an explanation when inspecting a deeper term;
- keyboard/focus interaction must provide an equivalent to mouse hover.

The key design requirement is not the visual tooltip itself. It is that systems retain **reason codes / contributing factors / source values** instead of returning only a final unexplained number.

## 2. World, map and regions

### 2.1 Geography

The first playable world covers the entire territory corresponding to present-day Czechia plus adjoining parts of Germany, Poland, Austria and Slovakia, as defined in V1_SCOPE. These modern geographic labels describe coverage, not the jurisdictions of 1900. The exact clipping polygon is an authoring deliverable; Hungary and further European territory are later expansion possibilities, not substitutes for the approved adjoining coverage.

The map must be physically large enough that major cities have meaningful space between them. Travel should feel like travel, not like moving between adjacent miniature towns. Journey duration follows the common time ratio in Section 3, not a separate visual travel clock.

The long-term architecture must allow a procedural map generator later, but the initial world is authored from real geography.

### 2.2 Region identity

Regions differ naturally rather than through arbitrary game bonuses:

- terrain and relief,
- city density,
- typical industries and resources,
- agricultural character,
- historical architecture,
- infrastructure,
- population and economic potential.

The Czech lands should visibly feel different from Austria, Hungary, Saxony, Bavaria, Poland, etc.

### 2.3 Terrain

The world is not grid-based.

Roads, rails, canals and other linear infrastructure use free-form spline placement. Buildings can be freely rotated. Snapping exists only where physical connections are required.

Terrain is geographically distinct by region: hills, plains, mountains, forests, fields, rivers and other landforms should reflect the region.

### 2.4 Unlocking countries and regions

The world outside the active territory exists only as a lightweight macro layer until unlocked.

Entering a country requires real expansion rather than a simple unlock button:

- appropriate national/regional market-entry right or concession,
- a local branch or acquisition where required,
- a physical connection or credible access route.

The player's **selected starting region is the exception**: basic legal permission for the newly founded company to conduct business in that starting region is granted as part of new-game setup. The player does not spend the opening minutes waiting for a generic "company may exist here" permit.

This starting-region permission is only a basic business/market-entry right. It does **not** include mode-specific operating licences such as rail freight, passenger road transport or hazardous-goods authority.

A national agreement initially grants access to roughly 1–3 regions depending on price, reputation and negotiated conditions. Further regions must be acquired individually.

Regions have different values based on population, industries, resources, infrastructure, strategic location and market potential.

Terms can be negotiated with the state, e.g. higher entry fee, infrastructure commitment, required services or local employment in exchange for cheaper/broader access.

When a region becomes active, it is instantiated directly at the current historical date from its macro state. It does not simulate every preceding year retroactively. Once activated, it remains simulated. The same date-appropriate initialization principle applies when starting a new game in 1900, 1925, 1950 or 1975.

### 2.5 World outside the active map

Inactive Europe and the wider world are not fully simulated, but the player receives period-appropriate newspaper/world-news items, potentially with stylized illustrations, so the world feels larger than the active map.

These reports can foreshadow technologies, economic changes and future expansion opportunities.

## 3. Time, start dates and historical progression

### 3.1 Base game and Early Ages scope

The wider base game's default/earliest selectable start is **1900**, with later presets **1925, 1950 and 1975**. First-playable V1 requires only the 1900 preset, with continued historical progression; the later presets remain future base-game scope. The player chooses a start region, then must **physically establish and construct the first regional office/branch in a chosen city**. Choosing a later year does not automatically grant a large established company or a free prebuilt branch.

The pre-1900 playable period, with an intended beginning around **1820**, is reserved for the first planned DLC, **Early Ages**. Its detailed content and release schedule are not specified here. Early Ages extends the historical content backwards using the same core systems, rather than requiring a second simulation engine or a different calendar.

Earlier-era concepts in this specification are retained where useful as DLC design or as the history of assets surviving into later years. The base game must not require playing through a pre-railway phase. Steam traction, coal/water infrastructure, existing historic buildings, old lines and suitable older second-hand vehicles remain relevant to the base game when appropriate to the selected year. Moving the earlier start to DLC does not remove these shared systems.

In this document, **early game** normally means the small-company stage of the chosen start, not automatically the year 1820. Historically early technologies and behaviours must be filtered by the selected date and content scope.

### 3.2 One simulation clock and a shortened calendar

The game uses **one shared simulation time** for vehicle movement, departures, transfers, loading, cargo perishability, crew shifts, maintenance, production, financial periods, contracts, construction, seasons, research and historical progression. Do not introduce an independently advancing historical-year clock or skip unplayed operating days to force a shorter campaign.

The agreed calendar is:

- 60 simulation seconds per minute;
- 60 minutes per hour;
- 24 hours per day;
- 7 days per week;
- **14 days per month**, exactly two full weeks;
- **12 months per year**;
- **168 days per year**, exactly 24 weeks.

Month names and seasonal meaning remain. A three-month season spans 42 game days. All months have days 1–14; there are no 28–31-day months or leap-day exceptions. Weekday progression remains continuous across month and year boundaries.

At **1×**, **one real second equals one game minute**. This is the base speed, not literal real-time 1:1. Simulation time advances by `real_elapsed_seconds × 60 × speed_multiplier` in simulation seconds.

The speed controls support **0.5×, 1×, 2×, 4×, 8× and 16×**. The slowest running speed is **0.5×** and the maximum selectable acceleration is **16×**. At 0.5× one real second represents 30 game seconds; at 16× it represents 16 game minutes. Changing speed accelerates/slows the whole simulation consistently, including the visible movement of trains and other vehicles.

### 3.3 Resulting duration

At a constant 1×, one game hour takes one real minute, one day 24 real minutes, one week 2 h 48 min, one month 5 h 36 min, and one year **67 h 12 min**.

| Game period | At 0.5× | At 1× | At 16× |
|---|---:|---:|---:|
| One day | 48 min | 24 min | 1 min 30 s |
| One 14-day month | 11 h 12 min | 5 h 36 min | 21 min |
| One 168-day year | 134 h 24 min | 67 h 12 min | 4 h 12 min |

For the reference endpoint 2020, using exact elapsed year differences:

| Start year | Elapsed years to 2020 | Continuous 0.5× | Continuous 1× | Continuous 16× |
|---|---:|---:|---:|---:|
| 1900 | 120 | 16,128 h | 8,064 h | 504 h |
| 1925 | 95 | 12,768 h | 6,384 h | 399 h |
| 1950 | 70 | 9,408 h | 4,704 h | 294 h |
| 1975 | 45 | 6,048 h | 3,024 h | 189 h |

These are arithmetic wall-clock durations at uninterrupted constant speed, assuming the machine sustains the selected rate. They are not guaranteed completion times or performance measurements. Normal mixed-speed play takes a duration determined by the actual speed history. **2020 is a comparison date, not a mandatory ending or victory condition.**

The previous 100–150-hour campaign target is retired. Do not compress years independently to recover it, and do not implement acceleration above 16× to shorten the campaign.

A trip lasting **3.5 game hours** takes **3 min 30 s at 1×**, **7 min at 0.5×**, or **13.125 s at 16×**, excluding any extra game-time delays. The earlier 12–15-real-minute target for this example is retired. Route distance, vehicle performance and operational dwell determine game-time travel; there is no separate arbitrary real-minute duration assigned to a route.

### 3.4 Calendar consistency across systems

Every calendar consumer must use the same 14-day-month model. Do not mix ordinary Gregorian date arithmetic or 365-day financial years with the game calendar.

- Timetables, weekday patterns, seasonal operating windows and rail/station slots use game dates and game minutes.
- Contract duration, notice/cure periods, cancellation calculations, automatic renewals, research dates and construction schedules use the same dates. Seasonal renewal retains the same season in the next game year.
- Financial and production data must state their units explicitly: per game hour/day/week/month/year or per trip/tonne/km. Normalize imported assumptions deliberately; do not combine conventional-month expenses with only 14 days of revenue by accident. Calendar rates and physical per-use costs must not be charged twice.
- Fuel, distance-based wear and material consumption remain tied to actual simulated operation. Speed selection changes wall-clock duration, not the quantity consumed by the same completed work.
- Population and production growth, vehicle/calendar ageing and technology availability advance with the common clock. Historical regional snapshots are initialized at the selected start year rather than replayed from the DLC era.
- Imported historical dates use the versioned authoring conversion in DATA_PIPELINE.md: validate the Gregorian source date, retain its original value, preserve year/month and map **every** source day with `game_day = 1 + floor((source_day - 1) * 14 / source_month_length)`. Game-authored dates already use days 1–14 and are never converted again. Gregorian rules exist only in this import step, not runtime billing, schedules or ageing. Colliding mapped events follow prerequisites and stable source-date/ID order.
- UI must distinguish game time from estimated real playtime. Calendar, contracts and timetables show game-time units consistently.

Test month/year rollover, two complete weeks per month, cross-year winter seasons, seasonal renewals and speed changes during trips, maintenance and construction. For equivalent simulated elapsed time, different selected speeds must not change resource accounting or bypass physical movements, reservation conflicts, deadlines or other events.

### 3.4.1 Binding commands while paused

Pause stops **simulation time**, not the player's ability to make administrative decisions.

While the simulation is paused, the player may explicitly commit otherwise valid binding actions, including for example:

- purchases and leases;
- submitted orders and capacity requests;
- bids/contracts and accepted agreements;
- licence/permit applications;
- construction project launch;
- Line/Service Pattern activation or future-version changes;
- capital/asset transfers and other validated company transactions.

The command is validated against the authoritative state and committed **once at the current game timestamp**.

Any immediate state change that is inherently part of the transaction still occurs at that timestamp, for example:

- money reservation/payment where the transaction requires it;
- creation of the accepted order/agreement/application/project record;
- ownership/commitment change where the canonical transaction is immediate;
- reservation of finite stock/capacity where acceptance itself legally/operationally creates that reservation.

Pause never grants free elapsed work. Anything whose completion depends on time makes **zero progress** until simulation time resumes, including:

- manufacturing/delivery;
- construction;
- licence/application processing;
- recruitment/training;
- research/adoption;
- maintenance/repair;
- loading/handling;
- vehicle movement/repositioning;
- AI/company follow-up work;
- deadlines and periodic accounting.

A command whose counterparty/system response is not defined as immediate can enter its normal submitted/pending state while paused and wait for simulation time to advance.

Repeated clicks or parallel windows must remain idempotent. Pausing cannot bypass price/availability/permission validation, force an AI counterparty to respond instantly, complete a physical step, or move a deadline.

This rule applies consistently to manual pause, critical-event pause and other simulation-pause reasons whenever the relevant gameplay UI is available. A pause-menu overlay may temporarily block interaction as a UI state, but it does not define different transaction semantics.

### 3.5 Date-appropriate starts and history

The world is historically anchored but not fully deterministic:

- major political and technological shifts happen approximately in their real periods;
- exact years and severity can vary;
- smaller economic events can diverge significantly between campaigns.

Initialize political boundaries, jurisdictions, licences, population, architecture, existing infrastructure, firms, competitors, manufacturer catalogues, demand and available technologies for the chosen start year. Do not apply the political or technological state of 1820 to every new game. Events preceding the selected date are part of the initialized world, not queued for replay.

Technology should not be only year-gated. Historical year is the baseline, but research can bring some technologies forward within plausible bounds. A later start does not require re-researching historical prerequisites that are already established in that start's world; acquiring equipment, staff, facilities and any company-specific permissions still costs resources.

The 16× setting is a simulation/performance requirement to validate on representative late-game networks, not an already measured capability. Rendering may be culled and updates batched, but insufficient performance must not be hidden by dropping essential simulation events or advancing the calendar while vehicles remain behind.

## 4. Visual direction

### 4.1 Camera and presentation

- 3D top-down strategy camera.
- Free camera rotation.
- Strong diorama/model-world/model-railway feeling.
- The player should feel like they are building and managing a living miniature world.
- No first-person mode is required.

### 4.2 Art direction

Stylized realism: visually believable but slightly illustrated/stylized rather than photorealistic.

Strong Central/Eastern European identity:

- European street patterns,
- dense historic centres,
- traditional blocks,
- industrial districts,
- later socialist-era housing estates where appropriate,
- suburban growth,
- occasional high-rise landmarks but few generic skyscrapers,
- regional architectural differences,
- historical evolution of building styles.

Cities must not look like generic American grids.

## 5. Simulation architecture principles

These are design constraints, not optional optimizations.

### 5.1 Simulation LOD

Different levels of detail are used depending on relevance and camera distance:

- **Detailed:** visible local movement, station operations, representative pedestrians, physical train movements.
- **Standard:** exact operational state without unnecessary visual/physics detail.
- **Aggregated:** remote areas use scheduled/event-based state transitions rather than continuous simulation.

All levels use the shared simulation clock in Section 3. Changing camera location or time speed must not remove physical occupancy, skip contracted movements or give remote operators different capacity rules.

### 5.2 Event-driven systems

Do not update everything every frame.

Examples:

- economic firms tick daily/weekly/monthly,
- maintenance wear can update after trips/segments,
- route options are cached,
- pathfinding reruns only when relevant topology/service conditions change,
- breakdowns can be scheduled probabilistically at trip start instead of rolled every frame.

These intervals are game-time intervals under Section 3, not wall-clock timers. The same events must be processed at 0.5× through 16× without double-counting or silently omitting work.

### 5.3 Physical continuity

Every player vehicle and relevant rolling-stock asset always has a logical world location.

A vehicle may stop being rendered at distance, but it never logically disappears.

Vehicles cannot:

- teleport to depots,
- magically reverse,
- change train composition through menus without physical shunting/transfer,
- appear in a remote region without transport.

The only abstract boundary is the not-yet-simulated outside world. Imported vehicles enter through defined map entry/import points and then become normal physical assets.

## 6. Population, passengers and cities

### 6.1 Population model

Population is primarily aggregated, not one persistent simulated person per inhabitant.

Demand is generated as origin-destination flows segmented by purpose and passenger type.

Representative visible NPCs are spawned only to visualize real aggregate flows around the camera.

Example:

- simulation says 300 passengers are on a train,
- the rendered scene may show 50–80 representative people,
- the underlying transport count remains 300.

Passenger waiting at stops/stations is also represented as **aggregated queue state**, not persistent individual people.

The simulation can track meaningful grouped state such as:

- boarding stop/station;
- intended destination or compatible itinerary group;
- passenger segment/purpose where materially relevant;
- class/product requirement;
- reservation/open-boarding status;
- time already spent waiting.

Representative visible passengers can be spawned from that queue when the location is rendered.

### 6.2 Passenger trip choice

Trips can combine multiple modes and operators:

home/zone → walk/bus/tram → station → train → transfer → local transport → destination zone.

Passenger choice depends on factors such as:

- price,
- travel time,
- frequency,
- reliability,
- number/quality of transfers,
- comfort,
- operator reputation,
- purpose of journey.

Journey purposes include work, business, school, tourism/leisure, family/social visits and other meaningful categories.

Different segments value time, price, comfort and reliability differently.

#### Passenger service factors

Passenger-service quality is represented through **separate visible factors**, not one opaque master score.

Core factors include:

- **Comfort** — seating/berth quality, temperature/heating/air conditioning where relevant, ride/service amenities and the physical vehicle product; standing/crowding can reduce the experienced comfort on affected travel legs.
- **Cleanliness** — driven by actual cleaning/service history and turnaround servicing rather than an abstract vehicle bonus.
- **Crowding** — based on actual per-vehicle/per-zone occupancy relative to seated and standing capacity, evaluated over the affected journey segments.
- **Reliability** — derived from real operating history under Section 9.2.
- **Travel time** — based on the actual published itinerary, including running time, dwell and expected transfer time.
- **Frequency / availability** — how often a usable service is offered for the passenger's intended journey/time window.
- **Transfer quality** — number of transfers, walking time, connection reliability, protected-connection status and interchange quality.
- **Price** — the actual fare applicable to the intended itinerary/product.
- **Operator/service reputation** — where relevant, based on visible historical outcomes rather than a hidden arbitrary preference.

The UI should present these factors separately.

Do not collapse them into a mandatory single value such as:

> Service quality: 78 / 100

A compact overall indicator can exist as a navigation aid only if it is immediately explainable and can be expanded into the underlying factors. Gameplay decisions must use the underlying factors, not a second hidden score disconnected from them.

Example Line detail:

> Comfort: Good  
> - modern seating  
> - air conditioning available  
> - Standard turnaround servicing

> Cleanliness: Fair  
> - 12% of recent planned cleanings skipped during disruption  
> - latest full clean: 3 duties ago

> Reliability  
> - 91% within +5 min over last 30 Trips  
> - 1 cancellation  
> - 2 protected connections missed

> Crowding  
> - average peak load: 94% seated capacity  
> - 18% of peak passengers used standing capacity on applicable segments

Each displayed state must retain enough source values/reason codes to support the explainability rules in Section 1.1.

#### Passenger-segment weighting

Passengers do not all value the factors equally.

Journey purpose/passenger segment defines visible or inspectable preferences, for example:

- **business** — stronger weight on travel time, frequency, reliability and connection quality;
- **commuter/work** — strong weight on frequency, reliability, travel time and price;
- **student/school** — stronger price sensitivity, with frequency still important;
- **tourism/leisure** — greater tolerance for travel time in exchange for price/comfort depending on market;
- **premium/first-class customer** — greater weight on comfort, crowding and service quality.

These are broad behavioural tendencies, not rigid personality classes.

Weights should also evolve with:

- historical period;
- income/prosperity;
- trip length;
- purpose;
- available alternatives.

The game should expose the important reasons for an itinerary choice.

Example:

> **Why passengers prefer Service A over Service B**  
> + 22 min faster  
> + 2 departures/hour instead of 1  
> + better recent reliability  
> - fare is 14% higher  
> - slightly more crowded at peak

The UI does not need to expose raw internal utility math by default, but the relevant inputs, direction of effect and material weighting must be inspectable. Do not allow a passenger choice to be materially decided by an invisible unexplained modifier.

For crowding, itinerary evaluation should consider the actual **length/duration of the affected crowded segment** rather than treating one brief standing leg as equivalent to standing for the entire journey.

Passenger choice can use only disruption information that passengers can plausibly know under Section 28.1. A current delay that has not yet reached the passenger-facing information system must not be treated as if every passenger knows it instantly.

Passenger demand can be seasonal, but the strength and composition of seasonality must be historically plausible. Leisure/tourism demand depends on the chosen year, income, free time, transport accessibility, urbanization and relevant destinations, not simply how recently the player founded the company. Seasonal passenger peaks can include holiday/leisure travel, commuting cycles, fairs/events and later mass tourism. The Early Ages DLC must not project modern travel behaviour backwards into its earlier period, and a 1975 base-game start must not inherit an 1820 demand profile.

Passenger demand also has historically grounded daily and weekly rhythms. Work shifts, market days, school schedules, religious/rest days, weekends and later modern commuting patterns can shape peaks, but the profile must evolve by era rather than using one modern 24/7 template for the whole campaign.

These peaks can create visible waiting queues when offered service capacity is temporarily below demand. Adding frequency or compatible capacity should reduce the real accumulated queue rather than only changing a hidden demand modifier.

### 6.3 Private cars

Private motoring grows with technology, household prosperity, road quality and vehicle availability.

Cars compete with public transport and can reduce demand for trains/buses where public transport is unattractive.

Private traffic is economically aggregated and visually represented with traffic agents rather than one permanent simulation object per privately owned car.

Road congestion affects buses and trucks.

The player can later influence modal choice through infrastructure such as:

- P+R,
- parking,
- transport hubs,
- toll roads/highways,
- good interchange design.

### 6.4 City growth

Cities physically expand on the map.

Growth uses both:

1. a historical baseline based on real importance/population trajectory;
2. dynamic simulation based on accessibility, jobs, goods supply, transport quality and regional economy.

Without player intervention, cities should remain broadly plausible historically. Good or bad transport can significantly alter their trajectory.

Urban form evolves over time. Historic cores, industrial districts, interwar growth, later housing estates and modern suburbs should look different.

Protected/historic areas can restrict demolition and construction.

Old industrial sites can become brownfields and later be redeveloped, including adaptive reuse into housing/offices while retaining an industrial visual character.

### 6.5 Start-year initialization

Cities and their existing historical layers are initialized for 1900, 1925, 1950 or 1975 as selected. Existing older buildings and infrastructure can be present without the player having played their construction era. Demand, private motoring and industrial development must match that date; the player's small initial company does not make the whole world technologically young.

## 7. Company progression and organization

### 7.1 Early game and selected start

The player starts with a legally founded but operationally minimal company in the selected year:

- the selected **founding-loan package** provides the initial cash,
- no free prebuilt regional branch,
- no free mandatory starting fleet,
- no automatic depot, terminal or operating infrastructure,
- only the basic company state needed to begin purchasing/constructing the first real assets.

After choosing the starting region, the player must select a city/site and **establish the first regional branch/office**. This can be a standalone building, rented office space, or an integrated office module in a suitable transport hub if the player already has access to such a site. The first branch is therefore an actual physical commercial location and one of the player's first capital decisions, not a menu-only headquarters granted at game start.

The first branch:

- costs money to establish/build,
- takes construction/setup time appropriate to the era and building type,
- occupies a real site,
- requires any relevant land/lease and local permission rules,
- becomes the company's first local commercial/administrative hub once operational,
- determines the initial local commercial presence/catchment under Section 7.2.

The player cannot operate as if a branch exists before construction/setup is complete. The new-game flow may keep the company setup interface available while the branch is being placed, but it must not silently grant the branch's commercial reach, local staffing capacity or other benefits early.

Exact branch building variants, starting capital, vehicle models and fleet quantities remain balancing/content decisions. A later start does not automatically award a large network, established customer history or free infrastructure.

The mandatory handful-of-horse-drawn-vehicles start belongs to the planned Early Ages experience around 1820, not to every base-game start. Base-game startup options must fit 1900, 1925, 1950 or 1975 and the chosen region. Surviving older vehicles may remain available where appropriate to their date and condition.

At new-game setup, the player chooses one of **three starting-capital tiers**. All three are loans rather than free money:

1. **Small founding loan** — lowest starting cash and lowest total debt; intended for a cautious, very small start.
2. **Standard founding loan** — more cash for vehicles, facilities and working capital, with a larger principal but still favourable terms.
3. **Large founding loan** — the highest starting cash and debt, intended to let the player establish a broader initial operation without turning the start into an established large company.

The exact currency amounts are balancing values and can vary by selected year/economy. The tiers should preserve the same relative role across 1900, 1925, 1950 and 1975 instead of using one nominal amount whose purchasing power changes radically by era.

All three founding loans receive deliberately favourable startup terms compared with ordinary commercial borrowing:

- low interest,
- long maturity,
- manageable scheduled repayments,
- no punitive increase in interest merely because the player chose the larger starting tier.

The larger tier still creates a larger total obligation and should therefore cost more over time, but repayment must remain proportionate and survivable for a reasonably operated new company. A higher starting tier should buy flexibility and faster setup, not function as a disguised hard mode through crushing early instalments.

The setup UI must show for each tier:

- cash received,
- principal owed,
- interest rate,
- repayment frequency,
- scheduled instalment,
- maturity/end date,
- estimated total repayment under the agreed terms.

Choosing a founding-loan tier does not change AI difficulty, demand, reputation or contract quality by itself. It changes only the player's initial financing and resulting balance-sheet obligation.

The company start is **transport-mode neutral**.

There are no predefined company classes/archetypes such as Road, Rail, Shipping or Mixed, and selecting a start year or founding-loan tier does not silently assign bonuses, penalties or permanent specialization.

After choosing year, region and founding-loan tier, the player decides how to spend the available capital. The **first branch/office is one of the required first expenditures**, after which the player can build out the chosen operation. Depending on the selected date, region and legal framework, spending can include:

- construction/setup of the first regional branch/office,
- chosen activity licences/concessions (the starting-region basic business right itself is already included),
- first vehicles/rolling stock,
- leased or owned infrastructure access,
- depot/parking/maintenance capacity,
- station/terminal access and slots,
- staff and operating supplies,
- optional owned infrastructure where financially realistic.

The setup may provide recommendations or starter templates for inexperienced players, but these are convenience presets only. They must translate into the same purchases and rules as a manually configured start and may be freely modified before confirmation.

The player can therefore start as road-only, rail-focused, mixed-mode or pursue another viable combination without the game assigning a permanent identity. Later divisions and subsidiaries emerge from actual company growth and player decisions rather than from a character-class choice made at new-game creation.

A mode that requires infrastructure, permits, staff or capital beyond the selected starting resources is not made artificially available merely because the start is neutral. Neutrality means freedom to choose within real constraints, not bypassing them.

### 7.2 Branches, administrative capacity and commercial reach

Branches are physical **commercial/administrative facilities**, not depots or abstract map unlocks.

They provide local business presence and office capacity for functions such as:

- sales and customer relationships,
- contract/tender processing,
- local administration,
- licence/permit handling,
- regional management,
- support for the company's nearby operational facilities and Lines.

A branch does **not** automatically provide vehicle parking, maintenance, storage, cargo handling or passenger-terminal capacity. Those remain separate physical facilities unless a specific mixed-use site explicitly includes them.

A branch can be established in three main physical forms:

1. **Standalone owned office** — a dedicated company building/site.
2. **Rented office space** — leased space in an existing building, with lower upfront cost but recurring rent and limited expansion freedom.
3. **Integrated transport-hub office module** — an office/branch module built into or attached to a sufficiently large passenger railway station, bus station/terminal or other suitable major passenger hub.

An integrated transport-hub branch is an upgrade/module of that physical hub rather than a second overlapping building placed on the same site.

It can provide:

- local branch/commercial presence;
- office/admin capacity;
- space for an optional customer-facing ticket/sales/service module;
- space for local managers/admin staff;
- direct organizational connection to the passenger hub.

A branch does **not** sell passenger tickets merely because it exists. Ticket sales require the relevant sales/ticketing upgrade under the passenger-ticketing rules in Section 32.

It does **not** automatically increase platform, parking, maintenance or vehicle-handling capacity unless separate hub modules provide those functions.

The hub must have enough physical/building capacity for the office module. A tiny rural halt cannot host a large regional headquarters simply because it has a platform.

If the player owns the station/terminal, the branch module can be constructed as part of the normal modular upgrade system.

If the station/terminal is owned by another party, an integrated branch is possible only if the owner offers suitable commercial/office space and the player signs the corresponding facility/space access agreement. The player does not gain ownership of the station by renting office space inside it.

The office module can later be expanded, relocated to a standalone building or retained as a smaller local branch when a larger headquarters is built elsewhere.

Integrated, rented and standalone branches all use the same aggregate equipment/staffing model below. The player does not furnish an integrated station office item by item either.

This allows a transport company to grow naturally around major hubs: a busy station can contain both the operating passenger infrastructure and the company's local commercial office while keeping their capacities/accounting separate.

Branch progression is based on several practical sizes rather than a single building with arbitrary percentage bonuses:

1. **Small branch / local office** — cheap first presence with limited office staff and administrative throughput.
2. **Regional branch** — larger office capacity, support for more contracts/operations and space for regional management/specialists.
3. **Area headquarters / large regional office** — a high-capacity administrative centre that can coordinate several smaller branches and a much larger operating footprint.

Names/visual variants can differ by era and region, but these functional roles remain consistent.

Branch capacity is driven by real workload. Relevant workload can include:

- number and complexity of active contracts,
- bids/tenders being processed,
- important customer relationships,
- locally managed Lines and facilities,
- licences/regulatory work,
- managers and office staff assigned to the branch.

#### Branch activation, equipment and staffing

A branch becomes operational when:

- its physical premises are ready or the lease has started;
- the basic office setup has been purchased/installed;
- at least the minimum ordinary office staffing required for that branch size is funded and available;
- one named **branch director** is assigned under Section 7.4.

The game does **not** simulate or require the player to buy individual desks, chairs, telephones, filing cabinets, computers or other office items.

Opening a branch includes a single **office setup purchase** appropriate to the selected year and branch type. It represents the normal equipment needed to make the premises functional.

After opening, the player can choose how much to invest in the branch through two simple management dimensions:

1. **Office equipment / systems level**
2. **Office staffing level**

These are aggregate investment choices, not room-by-room or employee-by-employee micromanagement.

##### Office equipment / systems level

The player can keep the branch at a basic functional standard or invest in better contemporary equipment and internal systems.

A higher level can improve concrete office functions such as:

- administrative throughput;
- speed of processing bids, contracts and amendments;
- customer-response speed;
- efficiency of licence/permit administration;
- effective workload that the same office staff can handle.

The exact form is era-appropriate. In 1900 this can represent better communications, filing/accounting equipment and office organization; later it can represent improved telephone systems, office machines, computers and internal business systems.

This **equipment-quality investment is separate from major technology unlocks** in Sections 7.2 and 28. Spending more on a 1900 office cannot buy a modern online system before it exists, and ordinary equipment upgrades do not silently remove the branch-at-every-city rule.

Use a small number of understandable levels rather than a continuous equipment inventory, for example:

- **Basic** — cheapest functional setup;
- **Standard** — normal well-equipped branch;
- **High** — higher recurring/depreciation cost for better throughput and service.

Names and exact effects can vary by era, but the player should always see the actual cost and operational effect before changing level.

##### Office staffing level

Ordinary office staff are **aggregated**, consistent with the workforce model in Section 8.

The player does not hire every clerk or salesperson as a named character.

Instead the branch has an aggregate staffing level/headcount and wage cost. The player can:

- run lean with lower payroll and less spare administrative capacity;
- staff around expected workload;
- deliberately target spare capacity for growth/peaks.

Ordinary branch employees are filled through the aggregate workforce system in Section 8. The branch does not recruit office staff individually. Its filled capacity depends on the company-wide salary policy for the relevant ordinary office/admin category and the available labour market.

Staffing affects concrete capacity and processing performance. It does not create unrelated global bonuses.

If filled staffing is below the branch's minimum operating requirement, the branch cannot provide normal commercial service until the shortage is resolved.

If staffing is above the minimum but below current workload, the branch remains open but becomes progressively overloaded.

##### Combined effect and UI

The branch UI should summarize the interaction of:

- physical branch size/capacity;
- equipment/systems level;
- aggregate staffing;
- current workload;
- any named manager/specialist effects where applicable.

Example:

> **Brno Branch**  
> Director: Jana Nováková  
> Premises: Small office  
> Equipment: Standard  
> Office staff: 5 / recommended 6  
> Administrative load: 91%  
> Contract processing: slightly delayed

The UI should explain why performance changes. Avoid opaque modifiers such as "+12% branch quality" when the actual effect is increased administrative throughput or faster response.

Investment has diminishing returns and real cost. A lavishly equipped, heavily staffed tiny office cannot exceed hard physical limits indefinitely; at some point the player must expand, move or build a larger branch.

The UI should expose an understandable administrative-load indicator rather than hide capacity in a generic bonus. If a branch is overloaded, consequences can include:

- slower processing of bids/contracts/amendments,
- slower response to customer/admin tasks,
- reduced effectiveness of delegated regional management,
- delays in routine local administrative actions.

Overload should degrade performance progressively rather than suddenly disabling an entire region.

#### Local-office operating model

A newly founded company begins with a **local-office operating model**.

At this stage, a branch's ordinary commercial reach is the **city/locality in which that branch physically exists**.

The Opportunity Board therefore shows routine commercial opportunities only for cities where the company has an active branch.

To commercially serve another city under this early operating model, the company normally needs an active branch in that city as well.

"Serve" means that the city is a commercial origin, destination or scheduled passenger/cargo stop where the company boards, alights, loads, unloads, sells/fulfils local transport or maintains a local customer relationship.

A vehicle may **pass through** a city or region without a branch if route/access rules permit it. Merely traversing a road, railway or waterway does not create a branch requirement.

Example:

> Branch Praha + branch Plzeň  
> → the company can discover local business in Praha and Plzeň and operate a Praha–Plzeň commercial service.  
> → a train may pass through Beroun without a branch there if it does not commercially serve Beroun.  
> → adding Beroun as a commercial stop initially requires establishing a Beroun branch.

This applies consistently to passenger and cargo operations where local commercial handling is required.

The rule creates a deliberate early-company expansion loop:

**build branch → discover local demand → secure endpoint/access → start service → expand to another city → build another branch**

It is not a kilometre-radius system.

#### Technology-driven reduction of branch dependence

The need for a branch in every commercially served city is **not permanent**.

Company communications, sales, reservation, dispatch and ordering technology can progressively centralize work and increase the geographic area that one office can serve.

The progression can include, depending on era:

- improved postal/administrative systems,
- telegraph/telephone coordination,
- centralized reservation and sales systems,
- computerized dispatch/customer databases,
- electronic ordering,
- modern online/self-service booking and digital customer systems.

Historical availability alone is not enough. The player's company must actually adopt/install the relevant business system where required.

Early improvements can reduce administrative friction and allow some centralized processing without immediately eliminating local offices.

Later systems can explicitly unlock broader operating models, for example:

- one branch can commercially cover several nearby cities;
- a regional headquarters can cover a defined broader territory;
- some customer types no longer require a local office;
- modern online systems can remove the branch-at-every-stop requirement for ordinary business almost entirely.

Even in a modern company, a branch can still be required where:

- law/licence terms demand local presence,
- a public concession requires it,
- a strategic customer contract requires dedicated local representation,
- local administrative or operational workload justifies it.

The UI must show the company's current **commercial coverage model** and explain why a city currently requires or does not require a branch.

#### Opportunity Board visibility

Opportunity discovery follows the current branch/technology coverage rules.

At the starting local-office stage:

- routine Opportunity Board results are limited to cities with active branches;
- filters cannot reveal ordinary hidden opportunities in unserved cities;
- building a new branch causes that city's normal commercial pipeline to become visible.

Later communication/business-system upgrades can broaden what appears on the Opportunity Board in line with the newly unlocked commercial coverage.

Public/nationally advertised tenders or direct approaches outside normal coverage can exist only when the current communication/business system plausibly allows the company to receive them. Seeing such an opportunity does not automatically waive a local-branch requirement for performing the contract.

If a visible contract requires service in a city that the company cannot yet commercially cover, the Contract Planner must show:

> **Local presence required: establish branch in [city]**

or the appropriate technology/coverage alternative.

#### Physical growth

Branches can be physically expanded or replaced.

Possible growth paths include:

- extend the existing building/site where land and permissions allow,
- add office/management capacity through suitable modules or wings,
- rebuild/replace the branch with a larger office,
- establish a new larger branch elsewhere and later sell/repurpose the old site.

Branch construction/redevelopment follows the normal land, construction and demolition rules. A central site can therefore become constrained or expensive as the city grows.

The game does **not** simulate individual desks, rooms or office furniture. The physical building/site exists, while its internal office layout is represented through aggregate office/administrative capacity and installed functional modules.

A larger branch should therefore solve a concrete company-scaling problem: more administrative/management capacity and better local support, not a flat revenue multiplier.

### 7.3 Divisions and subsidiaries

The player begins as one company.

As the company grows, it may create divisions such as Rail, Road, Shipping, Urban Transport and Infrastructure.

A division may later be spun out into a subsidiary with its own:

- finances,
- contracts,
- licences,
- management,
- workforce,
- reputation,
- assets.

Subsidiaries can remain 100% owned, be partly sold, or eventually merged.

### 7.4 Managers, departments and delegation

Managers and important specialists are named individuals. Ordinary staff are aggregated.

Management is hierarchical but intentionally lightweight.

#### Mandatory branch director

Every active branch/local office must have exactly one **branch director** (or period-/region-appropriate equivalent) assigned.

The director is a named individual and represents the accountable local manager for that branch.

A branch without a director cannot provide normal commercial service. If the director leaves, is dismissed or becomes unavailable, the branch enters a temporary **management vacancy** state:

- existing operations do not instantly disappear;
- basic administration can continue for a short grace period;
- new bids/contracts, approvals and delegated decisions become restricted or slower;
- the UI clearly warns that a replacement director is required.

The player is not expected to micromanage the director's daily tasks.

Director attributes can influence concrete outcomes such as:

- administrative throughput;
- commercial/customer handling;
- staff efficiency;
- contract processing;
- local reputation/relationship handling;
- quality of delegated decisions.

The effect must be understandable and bounded. A strong director improves a real process; they do not provide an unexplained global "+10% company" modifier.

#### Optional managers

As a branch, region or division grows, the player can appoint additional named managers.

Possible scopes include:

- commercial/sales;
- operations;
- finance/administration;
- staff/HR;
- fleet/technical;
- maintenance;
- station/depot/terminal management;
- group of Lines;
- specific Line/service;
- regional/area management;
- whole division/company.

Additional managers are **not required simply because a feature exists**. They become useful when workload/scale justifies delegation.

A manager can provide two main benefits:

1. **Automation/delegation** — the manager can make routine decisions within player-defined rules.
2. **Specialist performance benefit** — their skills improve the process they actually manage.

Examples:

- commercial manager can automatically handle routine bids within minimum-margin rules;
- operations manager can adjust routine vehicle/crew allocation and service recovery;
- maintenance manager can schedule routine maintenance within workshop/fleet constraints;
- HR manager can keep ordinary staffing near player-defined targets;
- finance/admin manager can handle routine renewals/payments/administrative workflows within limits.

The player always remains able to override delegated decisions.

#### Departments

Larger branches, area headquarters and divisions can create **departments** around selected management functions.

A department is not a building-room simulator. It is an organizational unit consisting of:

- one responsible manager;
- aggregated ordinary staff;
- a defined budget/staffing level;
- any required office/system capacity.

Possible departments can include, depending on company scale and era:

- Commercial / Sales;
- Operations / Dispatch;
- Finance / Administration;
- HR;
- Technical / Fleet;
- Maintenance planning;
- Customer service;
- Infrastructure/project management.

Departments provide scale benefits primarily by:

- handling a larger workload without overloading one manager/director;
- unlocking broader automation;
- improving specialist throughput/quality;
- enabling a manager to supervise staff and subordinate scopes rather than personally handling every item.

Creating a department should solve an actual scaling problem. It should not be optimal to create every department immediately in a two-vehicle company just to collect passive bonuses.

A small branch can operate with only:

> Branch director + aggregated office staff

A larger branch might evolve into:

> Branch director  
> → Commercial manager + Commercial department  
> → Operations manager + Operations department  
> → Finance/Admin manager + admin staff

The exact hierarchy is flexible; the player is not forced into one corporate org chart.

#### Scope and hierarchy

Possible management scopes include:

- whole company/division,
- country/region or area headquarters,
- branch/local office,
- department,
- station/depot/terminal,
- group of Lines,
- specific Line/service.

A larger area headquarters can coordinate several subordinate branches. This is an organizational hierarchy over real offices, not a replacement for the physical branch sites or their local workload/capacity.

A higher-level manager can set policies/limits for subordinate managers. Lower-scope manual overrides take precedence.

Managers/departments must respect the same physical and commercial constraints as the player. Automation cannot:

- invent vehicles or staff;
- exceed parking/workshop capacity;
- ignore licences/access;
- accept contracts outside authorized margin/risk limits;
- create transport slots;
- bypass the branch/commercial-coverage rules.

#### Shared management labour market

Named managers and important specialists are recruited from a **shared labour market used by all transport companies**, including AI competitors.

Candidates are real market participants rather than private player-only rolls.

This means:

- the player and AI firms can see/recruit from the same underlying candidate pool;
- a candidate can accept employment with only one company at a time;
- if an AI company hires a candidate first, that person disappears from the available market;
- market quality/quantity can vary by region, city size, era and wider economic conditions.

The player cannot directly poach or recruit a manager who is currently employed by another company.

There is no active headhunting mechanic where the player offers a higher salary/signing bonus to break another company's employment relationship.

An employed manager returns to the available labour market only after becoming free again, for example because:

- their employer dismisses them;
- their employment ends;
- they resign/leave under the game's normal employment rules;
- their employer fails/collapses and releases staff.

A manager leaving the player's company follows the same rule: they can later appear in the shared market and may be hired by a competitor.

The game should preserve enough continuity that experienced former managers can become recognizable recurring market participants rather than being deleted and replaced by anonymous random rolls.

AI companies use the same recruitment constraints and cannot hire unavailable managers.

#### Hiring flow

Manager recruitment is intentionally immediate and does not use salary negotiation or a delayed acceptance mini-game.

Each available candidate listing already shows the employment terms required to hire that person, primarily:

- salary;
- role/position being considered;
- relevant skills;
- traits;
- previous experience/history where known.

If the candidate is still available and the player clicks **Hire**, the employment agreement is created immediately and the manager joins the company at once.

There is no separate sequence of:

- submitting an offer;
- waiting several game days;
- counter-offers;
- competing salary bids;
- signing bonuses used to outbid another company.

Because the labour market is shared, availability can still change before the player acts. If another company hires the candidate first, the listing disappears or becomes unavailable.

The player therefore makes a direct trade-off between:

- candidate quality/role fit;
- salary;
- current need;
- risk that a desirable candidate may be hired by another company.

Reassigning an already employed manager inside the player's own company is an internal organizational action and does not send them back through the labour market.

#### Dismissal

Manager dismissal is intentionally simple.

The player can dismiss a named manager immediately. There is no separate notice-period, disciplinary, negotiation or HR mini-game.

Immediate dismissal costs a fixed **severance payment equal to two monthly salaries** of that manager.

The confirmation UI must show the severance amount before dismissal.

After dismissal:

- the manager immediately leaves the player's organizational structure;
- any role/department depending on them becomes vacant;
- the manager becomes eligible to return to the shared labour market;
- their skills, traits and career history are preserved.

If the dismissed person was a mandatory branch director, the branch enters the existing management-vacancy state until a replacement is assigned.

AI companies use the same dismissal cost and labour-market return rules.

#### Manager skills

Managers use a **small shared skill model**, not a large RPG character sheet.

The core skill set is:

1. **Leadership** — ability to coordinate people, subordinate managers and departments; improves manageable organizational workload and quality of delegation.
2. **Commercial** — sales, customer relationships, bidding, pricing and contract negotiation.
3. **Operations** — scheduling, dispatch, service recovery and day-to-day transport operations.
4. **Finance & Administration** — budgeting, administrative processing, contracts, licences and financial discipline.
5. **Technical** — fleet, maintenance, infrastructure and technical-operational understanding.
6. **People** — staffing, retention, recruitment and workforce organization.

Use a clear bounded scale, such as **0–100**, but do not present a single synthesized "overall rating" as the primary measure of manager quality.

Every management position defines **1–3 key skills** from the shared skill set. No normal position should require all six skills.

A position can distinguish:

- **Primary skill** — the most important competency for the role;
- **Secondary skills** — zero to two additional competencies that materially affect performance.

The role's actual performance is calculated from only those 1–3 relevant skills plus applicable traits, workload and organizational context. Unrelated skills remain visible in the person's profile but do not artificially influence role performance.

Examples:

- Branch Director: Leadership + Commercial + Finance/Admin;
- Commercial Manager: Commercial + Finance/Admin;
- Operations Manager: Operations + Leadership;
- Fleet/Technical Manager: Technical + Operations;
- HR Manager: People + Leadership;
- Maintenance Manager: Technical + Operations;
- Line Manager: Operations + Commercial;
- Finance Manager: Finance/Admin + Leadership.

A candidate can therefore be excellent for one role and mediocre for another.

The hiring UI should visually emphasize the **1–3 required skills for the vacancy** and show how the candidate compares with the role's needs, rather than hiding the decision behind a generic star rating.

Do not create a single universal "manager quality" value that makes one person automatically best for every position.

Example:

> **Jan Král — Branch Director candidate**  
> Leadership 67  
> Commercial 74  
> Finance & Administration 61  
> Operations 42  
> Technical 28  
> People 55

The player can inspect all skills, but the UI should visually emphasize the ones relevant to the vacancy.

#### Traits

A manager can have a **small number of meaningful traits**, normally no more than 1–2 prominent traits.

Traits are qualitative specializations or behavioural tendencies, not another layer of ten hidden stats.

Examples can include:

- **Strong Negotiator** — better commercial outcomes in eligible negotiations;
- **Crisis Operator** — better service-recovery/delegated disruption decisions;
- **Cost Conscious** — stronger cost control, with effects tied to budgets/procurement;
- **Customer Focused** — stronger customer-service/relationship handling;
- **Technical Specialist** — stronger technical decision quality in relevant roles;
- **Staff Developer** — improves ordinary staff/manager development under their scope;
- **Conservative Planner** — favours larger operational buffers and lower risk;
- **Growth Oriented** — more willing to use spare capacity/budget for expansion within delegated limits.

Traits must always have an understandable domain and effect.

Traits can be:

- mostly positive;
- mostly negative;
- or **trade-off traits** that provide a meaningful advantage together with a corresponding downside.

Trade-off traits are encouraged when they create distinct management styles rather than obvious best-in-slot bonuses.

Examples:

- **Cost Conscious** — reduces routine operating/admin overspend but tends to choose leaner reserves and defer nonessential investment when delegated;
- **Conservative Planner** — keeps larger operational buffers and lowers disruption risk but can reduce asset utilization and growth speed;
- **Growth Oriented** — pursues expansion opportunities more aggressively within authorized limits but can consume cash/reserve capacity faster;
- **Customer First** — improves relationship/customer-service decisions but may authorize more expensive recovery/compensation choices within its allowed budget;
- **Perfectionist** — improves quality/accuracy of relevant work but can increase processing time under high workload;
- **Decisive** — responds faster to routine disruptions but is somewhat more likely to choose a costly solution when several options are close.

Negative effects must remain bounded and transparent. Traits should change incentives/decision style, not randomly sabotage the player.

Do not generate traits that provide unrelated magic bonuses such as "+5% revenue everywhere".

Where a trait changes automated decision behaviour, the player must be able to understand both the upside and downside before assigning broad delegation authority.

#### Experience and development

Managers can improve over time through the work they actually perform.

Development is **slow and role-related** rather than conventional XP/level grinding.

Examples:

- repeated bidding/customer work can slowly improve Commercial;
- managing complex operations can improve Operations;
- supervising a larger team/department can improve Leadership;
- fleet/maintenance responsibility can improve Technical.

Skills should not increase simply because game time passes.

Growth uses diminishing returns: improving from weak to competent is easier than turning an already exceptional manager into a near-perfect one.

A manager working far outside their strengths can gain experience, but the game should not encourage repeatedly rotating people through every department just to maximize all six stats.

Training/education can exist as a supporting investment where historically appropriate, but it supplements real experience rather than instantly converting money into elite managers.

Manager history should retain meaningful career information such as previous employers, major roles and accumulated experience so experienced individuals remain recognizable when they return to the shared labour market.

#### Manager effects and transparency

Skills and traits affect only systems within the manager's actual scope.

Their impact can include:

- administrative/department throughput;
- quality/speed of delegated decisions;
- commercial terms within negotiation limits;
- staffing efficiency;
- operational recovery quality;
- maintenance/fleet planning;
- budget discipline.

They do not bypass hard constraints.

A 95 Operations manager still cannot dispatch a train without:

- a real vehicle;
- qualified crew;
- valid infrastructure access;
- available capacity;
- required licences;
- physical service endpoints.

The UI should translate management effects into understandable operational consequences wherever practical, for example:

> Commercial manager reduces expected routine bid-processing time from 18 h to 14 h.

rather than only:

> Commercial +8%.

#### Cost and performance

Named managers have salaries and skill profiles.

Departments add recurring payroll/office overhead because their ordinary staff are real aggregate employees.

Benefits should be tied to managed work, for example:

- faster processing;
- larger manageable workload;
- better utilization;
- fewer avoidable administrative errors/delays;
- better routine pricing or scheduling within the manager's competence;
- reduced player micromanagement through automation.

Use diminishing returns and clear capacity limits so management investment matters without becoming a stack of mandatory percentage buffs.

Routine HR and management tasks can increasingly be automated as the company grows, but the director/manager hierarchy remains visible so the player understands who is responsible for what.

### 7.5 Licences, concessions and operating permissions

Licensing is layered so regulation creates meaningful business constraints without turning company startup into an administration simulator.

The game distinguishes three concepts:

1. **Basic company / market-entry right** — permission for the company to exist and conduct business in a jurisdiction/region.
2. **Activity licence** — permission to perform a specific regulated transport activity.
3. **Specific operational permit/approval** — narrower approval tied to a cargo, vehicle, route, facility or special operation.

#### Starting-region rule

At new-game creation, the selected starting region includes the player's basic company/market-entry right.

This right is automatic and has no waiting period. The player can therefore:

- take the founding loan;
- buy/lease land;
- build the first branch;
- inspect public setup costs and eligible public/direct opportunities; routine local jobs remain undiscovered until commercial coverage exists under Section 7.2;
- buy vehicles and arrange facilities.

The company still cannot legally operate a regulated transport activity until the relevant **activity licence** has been obtained.

The start remains transport-mode neutral because no road/rail/water/passenger/cargo specialism is granted automatically.

#### Activity licences

Activity licences are acquired only when the player chooses to enter that line of business.

Possible categories, depending on era/jurisdiction, include:

- road freight operator;
- road passenger operator;
- rail freight operator;
- rail passenger operator;
- inland water/shipping operator;
- urban passenger operator where a general operator licence is required;
- infrastructure operation where relevant;
- hazardous/special cargo authority;
- other historically relevant regulated activities.

These are functional categories, not a promise that every country/year uses exactly the same modern legal labels.

The jurisdiction and historical era can change:

- which licences exist;
- which authority issues them;
- fee level;
- processing time;
- required capital/insurance;
- responsible-manager or professional-competence requirement;
- technical/facility requirements;
- whether access is open, capped or concession-based.

Avoid redundant paperwork. A routine licence whose requirements are already met should be a simple application with clear cost/time, not a mini-game.

#### Requirements and application

A licence can require some combination of:

- application/issue fee;
- minimum capital or financial standing;
- insurance;
- responsible qualified manager/specialist;
- appropriate branch/local presence;
- proof of technical/maintenance capability;
- safety/operating plan;
- customer/public tender award or concession where historically appropriate.

The player does not manually fill bureaucratic forms.

The licence UI shows:

- what the licence enables;
- jurisdiction/regions covered;
- cost;
- expected processing time;
- current requirements and which are already satisfied;
- expiry/renewal rules if any;
- consequences of losing/suspending it.

If a requirement changes materially while the application is pending, the reason must be shown.

#### Expansion to another region/country

Entering another country/region uses the market-entry framework in Section 2.4 in addition to activity licensing.

A company that already holds a Rail Freight activity licence at home may still need:

- recognition/local equivalent in the new jurisdiction;
- a national concession/market-entry agreement;
- local branch/presence where required;
- route/infrastructure access.

Expansion rights and activity licences must not be collapsed into one opaque unlock.

The UI should distinguish clearly:

- **You may operate this activity, but not in this region yet**;
- **You may do business in this region, but lack the required activity licence**;
- **You have both, but still lack physical infrastructure access**.

Licences never create vehicles, depots, station access, slots or service endpoints.

#### Contract Planner integration

The Contract Planner is the main place where a missing licence becomes visible in context.

Example:

> **Missing: Rail Freight Operator licence**  
> Cost: 18,000  
> Expected processing: 6 game days  
> Requirement: qualified rail operations manager  
> Status: manager missing  
> **Apply / View requirements**

The planner must include licence processing time in the readiness/critical-path calculation.

If bidding rules allow future readiness, the player may submit a bid before the licence is issued only when obtaining it by the contract start is credible. Winning the contract does not automatically grant the licence.

AI operators follow the same legal requirements and processing/capacity rules.

#### Special permits

Specific permits/approvals handle narrow cases that should not become permanent new company-wide licences.

Examples can include:

- oversized/special road movement;
- dangerous-goods movement;
- exceptional route approval;
- vehicle approval for a jurisdiction;
- construction/demolition permit;
- temporary event operation.

Where another provider is responsible for the operation, such as an external heavy-haul company, the provider can handle the relevant permit under its service agreement. The player should not duplicate the same paperwork.

## 8. Workforce

Ordinary employees are **fully aggregated** rather than simulated as persistent individual people.

Only named managers and important specialists use the individual-person system in Section 7.4.

The ordinary-workforce system is built around **job categories, required capacity, offered salary and achievable staffing**, not individual applicants.

### 8.1 Aggregate staffing model

Each ordinary job category has a company employment policy.

Examples include:

- train drivers;
- road-vehicle drivers;
- conductors/on-board staff;
- mechanics;
- station/terminal staff;
- warehouse/loading staff;
- shunting/yard staff;
- office/admin staff;
- cleaning/security/service staff where relevant.

For each category the player primarily sets a **salary level** for all ordinary employees in that position.

The UI then shows:

- salary offered;
- market/reference salary where useful;
- required staffing capacity;
- currently filled capacity;
- realistically available capacity at the offered salary;
- resulting shortage or reserve.

Example:

> **Road drivers**  
> Salary: 2,400 / month  
> Required: 34 FTE-equivalent  
> Filled: 29  
> Available at current salary: ~31  
> **Shortage: 5**

The player does not:

- browse ordinary-worker candidates;
- hire employees one by one;
- negotiate individual wages;
- assign personalities/skills to ordinary workers;
- manage individual resignations or careers.

Hiring and attrition happen automatically in aggregate toward the capacity that the current salary and labour market can support.

### 8.2 Salary and labour-market availability

Offering a higher salary generally makes a position easier to fill and retain.

Offering too little can create a persistent staffing shortage even when the company has budgeted enough nominal positions.

The relationship is influenced by the real labour market, including where relevant:

- city/region population;
- local unemployment/labour supply;
- competing employers;
- profession scarcity;
- qualification requirements;
- historical period;
- working conditions implied by the role;
- company reputation as an employer where the system supports it.

The game should avoid fake precision. Labour availability can be shown as a practical estimate/range when exact future hiring cannot be guaranteed.

Salary does not instantly spawn workers.

Aggregate staffing moves toward the achievable level over appropriate game-time recruitment/attrition intervals. A large shortage therefore takes time to fill even after a salary increase.

Likewise, lowering salary does not cause an entire workforce to vanish at once. Retention pressure appears progressively.

The system is event-/period-driven and must not simulate individual job applications continuously.

### 8.3 One policy per ordinary position

By default, ordinary employees in the same company job category use the same salary policy.

Examples:

- all ordinary road drivers use the Road Driver salary;
- all ordinary train drivers use the Train Driver salary;
- all ordinary mechanics use the Mechanic salary.

This keeps labour management understandable and prevents branch-by-branch wage micromanagement.

Different genuinely distinct qualifications can remain separate job categories where they create real operational constraints, for example:

- road driver versus train driver;
- standard driver versus a legally required specialist qualification;
- mechanic versus specialized technical staff.

Do not split the workforce into dozens of nearly identical wage categories merely for flavour.

Manager salaries remain individual because named managers use the separate labour-market system in Section 7.4.

### 8.4 Company-wide mobile operating staff and crew reserve

Drivers, train crews and similar mobile operating staff are pooled **across the whole company** by qualification rather than permanently tied to a specific region or depot.

The game tracks aggregated availability such as:

- qualified train-driver capacity;
- road-driver capacity;
- conductors/on-board crews where required;
- licence/vehicle-type qualification capacity;
- usable shift/work-hour capacity;
- capacity already committed to planned Trips;
- deliberately uncommitted crew reserve.

A Trip consumes the required crew capacity for its duration. If the company does not have enough compatible filled capacity, the Trip cannot be staffed normally and enters the crew-recovery process in Section 32.7.

Crew capacity also respects aggregated **shift and rest requirements**. The game does not track an individual driver's sleep schedule, but longer, overnight or continuous operations consume more effective staffing capacity because legal/safe rest and crew rotation must be covered.

#### Company crew reserve

The player sets a **company-wide crew reserve target** for relevant operating-staff categories/qualifications.

Examples:

- train drivers;
- road drivers;
- conductors/on-board staff;
- specialist qualifications where legally or technically distinct.

The reserve represents paid qualified capacity intentionally kept above the normal planned timetable requirement so the company can absorb short-notice staffing failures.

The reserve target can be expressed as either:

- an absolute effective crew/FTE-equivalent capacity;
- or a percentage above planned peak requirement.

Example:

> Train drivers  
> Planned peak requirement: 42.0 crew-equivalents  
> Reserve target: 10%  
> Target reserve: 4.2  
> Currently available reserve: 3.6

A larger reserve increases payroll but reduces the probability that ordinary crew disruption becomes a Trip delay or cancellation.

A smaller reserve lowers normal cost but leaves less recovery capacity.

The effect must be exposed as actual available staffing capacity rather than a hidden reliability bonus.

Reserve capacity is still qualification-specific. Spare conductors cannot substitute for train drivers, and staff lacking a required licence/qualification cannot cover that role.

Local legal/language/qualification requirements can still restrict whether company-wide capacity is compatible with a particular Trip, but the player does not manage a separate mandatory reserve slider for every region.

Long-distance or long-duration Trips can require crew changes. The service planner should show when a service needs:

- one crew for the full Trip;
- a planned crew change;
- multiple crews for continuous/night operation;
- additional onboard staff because of service class or regulations.

Crew-change requirements are handled as operational planning constraints rather than persistent individual-person simulation. The game may use defined eligible change locations such as major stations, depots or terminals, but it does not require the player to assign named ordinary employees.

The UI must translate staffing needs into understandable requirements such as:

- train-driver hours/day;
- road-driver hours/day;
- conductor/onboard-staff hours where ticket checking/sales/service requires them;
- number of crew-duty/shift blocks required;
- number of effective full-time crews required;
- peak crew requirement;
- target and currently available reserve;
- additional staffing required for night/weekend patterns.

Where a Service Pattern requires conductors/onboard staff, that requirement contributes to crew capacity. Ordinary onboard ticket sales do not add station dwell when staff can circulate while running. Non-through compartment stock is the explicit aggregate station-dwell exception in Section 14.5. Neither case creates per-passenger staffing simulation.

The game does **not** simulate individual crew members commuting between Praha and Ostrava or require staff-repositioning trains.

Expansion into another region therefore does not require maintaining a separate arbitrary reserve pool there, although local licence/language/regulatory rules can require an appropriately qualified staff category.

### 8.5 Facility-bound staff

Employees whose work directly determines the capacity of a physical facility remain **allocated in aggregate** to that facility or local operation.

Examples:

- mechanics/workshop staff;
- station and terminal staff;
- warehouse/loading staff;
- local office/admin staff;
- local dispatch/yard staff where required;
- safety/security/cleaning where relevant.

The player still does not hire these people individually.

Instead the facility has:

- required staff capacity;
- target staff capacity;
- filled staff capacity supplied from the relevant job category;
- resulting operational capacity.

This preserves the physical simulation:

- a workshop with too few mechanics repairs vehicles more slowly;
- an understaffed terminal handles less cargo;
- an understaffed branch processes administration more slowly;
- an understaffed station can have reduced service/handling capacity.

Facility staffing can use automatic targets. Managers can later adjust those targets within delegated policy.

### 8.6 Business and administrative staff

Sales, contract, HR and general administrative staff are aggregated at company/division/office/department level depending on the system they support.

Their salary policy and labour availability follow the same ordinary-workforce rules.

Named directors/managers are separate from this capacity.

For example, a branch can have:

> 1 named Branch Director  
> + 6.4 FTE-equivalent ordinary office staff

rather than seven individually simulated office workers.

### 8.7 Staffing demand and planning

Every planner that creates workload should expose its staffing consequence before commitment.

Examples include:

- a new Service Pattern increasing driver-hours required;
- a larger workshop increasing mechanic demand;
- a new terminal increasing handling-staff demand;
- a contract increasing branch/admin workload.

The Contract Planner should show staffing requirements as:

- current filled capacity;
- already committed capacity;
- additional requirement;
- current labour-market fillability at the player's salary policy;
- expected time/risk to close a shortage.

A contract is not credibly ready merely because the player can afford wages. If the labour market cannot supply enough qualified capacity by the start date, staffing remains a real readiness risk.

### 8.8 Automation and management

Routine recruitment is automatic.

The player manages ordinary workforce mainly by:

- setting salary by job category;
- setting/accepting staffing targets where relevant;
- approving exceptional qualification/training investment where needed.

An HR manager/department can later automate salary recommendations and staffing targets within player-defined budget/coverage rules.

Automation must not create workers beyond the simulated labour market.

### 8.9 Time and accounting

Staffing hours, rest periods and wage periods use the shared game clock and explicit rate units in Section 3.4.

Salary is presented/accounted consistently against the game's 14-day-month calendar.

Changing the simulation speed selector does not alter wage cost or the crew capacity required for the same service.

## 9. Reputation and customer relationships

Reputation is not a single cosmetic score.

The design should support:

- overall company reputation,
- regional reputation,
- potentially service/segment reputation.

Reputation can affect:

- passenger operator choice,
- customer contract decisions,
- public tenders,
- licence negotiations,
- relations with municipalities/states,
- hiring,
- partner-carrier relationships.

Demolition, service quality, reliability, accidents and contract performance can alter reputation.

### 9.1 Customer-specific relationships

Important customers such as factories, mines, municipalities and large commercial firms can also have a direct long-term relationship with each transport operator.

This relationship is separate from general reputation and is built through actual business history, for example:

- completed contracts,
- reliability and on-time performance,
- damage/spoilage rates,
- pricing consistency,
- responsiveness to urgent jobs,
- capacity offered,
- contract breaches,
- length of cooperation.

The system must be transparent. A customer decision must never feel like a hidden arbitrary modifier.

When evaluating or awarding a contract, the UI should show the major reasons for the customer's preference, for example:

- strong existing relationship,
- better historical reliability,
- lower bid,
- higher guaranteed capacity,
- better local reputation,
- prior contract failure,
- insufficient experience with this customer.

A player who currently has a weak relationship must have a credible path to improve it. Customers should offer smaller/less critical jobs or trial contracts that allow a new carrier to prove itself before becoming competitive for major long-term contracts.

Normal local discovery of these opportunities depends on branch/commercial presence under Section 7.2. Publicly advertised tenders and direct customer approaches can still expose opportunities outside the branch network, but they do not grant the full local sales pipeline.

Existing relationships are an advantage, not an unbeatable lock-in. A new carrier can win business through better price, service quality, capacity or successful smaller contracts.

Customer relationship evaluation must use cached historical aggregates and contract outcomes rather than expensive continuous AI.

### 9.2 Service reliability and on-time performance

Reliability is derived from **real Trip history**, not from an abstract hidden reliability stat.

Line and Service Pattern analytics can expose measures such as:

- average arrival/departure delay;
- on-time performance;
- cancellation rate;
- short-formation/reduced-capacity rate;
- protected connections missed;
- passengers rebooked because of operator disruption;
- contractual/SLA service failures where relevant.

The exact metrics shown can differ by service type, but they must originate from actual operating events.

#### On-time definition

"On time" does not mean exactly zero seconds of delay.

The game uses an explicit visible tolerance appropriate to the metric/service being reported.

For example, a dashboard can define:

> On-time arrival: arrival no more than 5 min after published time

or another period/service-appropriate threshold.

The UI must display the threshold used; do not show an unexplained percentage.

Different contracts or authorities can use their own explicit SLA thresholds. Those contractual measurements remain distinct from the company's general passenger-facing reliability metric.

For longer-distance services, the UI can emphasize:

- final-destination punctuality;
- major interchange punctuality;
- protected-connection success;

rather than treating every minor intermediate variation as equally important.

#### Reliability feeds other systems transparently

Historical reliability can influence:

- passenger service choice;
- operator/service reputation;
- customer relationships;
- tenders/contracts;
- management recommendations.

When it does, the contributing operating history must be inspectable.

Example:

> Passenger reliability perception: Below average  
> - last 30 relevant Trips: 84% within +5 min  
> - 3 cancellations  
> - 7 protected missed connections  
> - improving over the last 10 Trips

Do not apply an invisible random reliability modifier on top of the observed operating record unless a separate real causal factor exists and is shown.

Analytics are calculated from event/history aggregates and rolling windows rather than rescanning every historic Trip every frame.

## 10. Economy and industries

### 10.1 Firms

Industrial and commercial firms are economic entities with simplified but real state:

- cash/debt,
- workforce aggregate,
- production capacity,
- input inventories,
- output inventories,
- suppliers/customers,
- orders/contracts,
- profitability,
- ownership.

They do not run expensive continuous AI.

Firms, operating facilities and physical buildings are separate identities. A firm can close a plant, fail or be acquired without deleting the building. A vacated industrial property can remain idle, be purchased and adapted by another firm, or be converted over time to another plausible use such as warehousing, offices or housing. New industries may therefore reuse older industrial sites rather than always building on untouched land.

The economy supports three broad physical-goods roles without forcing every firm to have a transportable output:

1. **Primary producers** create extractive/agricultural inputs from plausible resources or productive land.
2. **Processors/manufacturers** consume physical inputs and create other physical commodities.
3. **Final consumers/services** consume physical commodities but can produce a non-transportable economic effect instead of another cargo item.

A processor/manufacturer recipe can require **several independent inputs at the same time**. Production is constrained by the actual required bundle: abundant steel cannot replace missing electronics, and abundant chemicals cannot replace missing processed wood, unless a separately authored recipe/version explicitly permits that substitution. This multi-input rule applies equally to AI firms and player-relevant procurement/forecast UI.

Industrial/fleet/facility ownership also creates **maintenance demand**. Operating factories, vehicles, workshops, utilities and infrastructure consume spare parts and selected technical supplies over time according to asset type, age, utilization, condition and technology. This recurring demand is physical and must be sourced/transported; it is not an abstract maintenance-cost modifier that bypasses the commodity system.

Representative shops, distributors, hospitality/services, institutions and similar entities can stand in for household-facing consumption. Do not simulate every household or every small shop individually. Their physical inputs still have real inventories and delivery needs; their non-cargo output can contribute to local commercial activity, service availability and city development.

For the 1900 economy, food consumption is not one generic commodity. Use a limited set of meaningful categories such as grain, flour/bakery products, meat, dairy products and fruit/vegetables, with appropriate production/processing/storage and perishability differences. Keep the level above individual retail products so the system remains legible and scalable.

Construction demand likewise uses distinct physical commodities rather than one generic building-material item. Baseline 1900 coverage includes stone/gravel, bricks, cement, processed timber and steel products where historically/regionally appropriate. Their different sources, storage/handling requirements and compatible vehicles should create materially different logistics without splitting into unnecessary retail-level variants.

For heavy industry, **coke is not a separate player-facing transport commodity** in the baseline design. Coal covers the relevant solid-fuel/reductant input at the gameplay level; internal processing detail may be abstracted inside the industrial recipe where needed. This keeps the useful transport decisions around coal, iron ore, iron/steel, metal products and machinery without an extra near-duplicate cargo step.

Heavy industry also feeds the installed economy after initial construction through two spare-parts generations:

- **basic spare parts** for older/mechanical vehicles, factories, workshops, utilities and infrastructure;
- **modern spare parts**, introduced later for newer equipment and systems and increasingly using plastics, industrial chemicals and electronics.

An asset's technology/content definition determines which spare-parts generation it consumes. Newer parts do not automatically replace the needs of older equipment, so a long-lived legacy fleet or factory can keep supporting real basic-spare-parts demand while modern assets create a parallel newer supply chain. Asset maintenance must therefore create recurring secondary freight flows instead of being represented only by a money expense.

Resource extraction remains **resource-specific**. Coal mines, iron-ore mines, stone/gravel quarries and other extraction industries are separate facility/industry types tied to plausible deposits and producing their own commodities. Do not collapse them into one generic mine merely because some downstream processing detail is abstracted.

**Iron and steel are distinct transport/economic commodities.** Industrial recipes declare each required input independently. A downstream firm may require iron, steel, or **both at the same time** for different parts of its production process. They are not generic substitutes and must not be silently treated as interchangeable.

For textiles, the baseline game uses one aggregated **textile raw materials** commodity instead of splitting wool and cotton into separate cargo types. Processing still creates distinct textiles/fabric and then clothing/garments for retail/final consumption. This abstraction is intentional to keep the commodity catalogue manageable while preserving a multi-stage transport chain.

Industrial recipes can **evolve historically** as new materials and processes become available. For example, later textile production may begin requiring dyes, industrial chemicals or synthetic inputs. The same principle applies to other industries: newly introduced technologies can add or replace real recipe inputs and create new supplier/transport relationships. Do not treat this as a free global stat upgrade; a firm must actually obtain the newly required physical inputs, or continue an older viable process where the design/content allows it.

Existing facilities do **not** switch automatically to a newer recipe when the technology appears. A plant can continue using its older process while that process remains technically supported and economically viable. Moving to a newer process requires a real modernization/investment step with explicit cost, duration and any required equipment/facility changes. The new process can change inputs, outputs, efficiency, quality, staffing or energy use, and those changes become effective only after the modernization actually completes.

Modernization normally causes a **partial production reduction**, not a full plant shutdown. The affected facility continues operating at reduced capacity during the work, with the reduction based on the scope of the modernization. A complete shutdown is not the default modernization mechanic and should be used only if a future explicitly authored process genuinely requires it.

The energy/chemical economy distinguishes **crude oil**, **raw natural gas**, **processed/distribution gas**, **refined fuels**, and **industrial chemicals**.

Industrial chemicals are a real physical commodity, not a generic hidden category. Chemical-industry facilities produce them from historically appropriate feedstocks, and downstream firms can require them explicitly as inputs for plastics, dyes, fertilizers, resins/adhesives and selected later manufactured products. A downstream recipe can therefore add chemicals as one more required physical input without replacing its other material requirements. Crude oil and raw natural gas are separate primary resources. Refined fuels are downstream products of crude-oil processing. Raw natural gas requires real treatment/processing before becoming distribution-quality gas for city and industrial consumption.

City/industrial gas supply can use different historically valid production routes. Around the 1900 start, coal-based gasworks can produce distribution gas; later, processed natural gas can increasingly replace that route as extraction, treatment and gas-network technology develops. Both routes feed the **same canonical distribution-gas commodity and downstream demand**. Existing coal-gas plants do not disappear automatically when natural gas becomes available.

Distribution gas is a fixed-network utility product, analogous to electricity in that it is delivered through real gas-network connections/capacity rather than teleported or treated as generic wagon/truck cargo. Player-facing pipeline construction/operation is not implied unless separately included in scope. A later transportable gas-derived product such as LPG may be authored as its own physical cargo with appropriate tank/storage compatibility.

Demand for oil/gas/fuels should emerge and grow with the relevant technologies and industries rather than being globally modern from the 1900 start.

Later liquid-fuel economies can also create transportable **lubricants/technical fluids** consumed by combustion vehicles, workshops and industrial machinery. These are operating supplies distinct from fuel itself where the content/balance justifies the additional logistics.

Shortage is gradual rather than binary. A final consumer that receives only part of its requirement continues operating at the supported level. Persistent material shortage can raise local unmet demand/reference prices, reduce commercial activity and slow city growth, and can cause real firms to seek additional supply or publish discoverable transport/business opportunities. One missed delivery does not instantly close the business or collapse city growth.

Every authored commodity chain must ultimately terminate in a **real final-use sink tied to the city/urban economy**. Intermediate commodities may pass through many firms, but the chain must eventually be consumed by household-facing retail/services, construction/buildings, utilities, public institutions, transport/operating consumption, or another explicit final-use activity that supports city population, employment, services or development. Do not create commodity chains whose final product simply accumulates indefinitely at another producer with no economic consumer.

The final sink does not have to be a literal municipal authority. A shop selling clothing, a furniture retailer, a construction project consuming cement/steel, a utility consuming fuel/gas, or a transport company consuming coal/fuel are all valid final-use endpoints because their output is service/activity rather than another transportable commodity.

For manufactured retail items that are not strategically distinct enough to warrant their own cargo type, use one aggregated **consumer goods** commodity. Important categories with materially different chains or handling—such as food, clothing and furniture—remain separate. This aggregation prevents the late-game commodity catalogue from fragmenting into many low-value retail SKUs.

### 10.2 Industrial geography

Industry is dynamic but geographically grounded.

Resource extraction is constrained by plausible deposits and land conditions.

Large deposits may effectively last the full campaign; smaller deposits can deplete and close.

Processing/manufacturing industries are more flexible and can choose locations based on labour, transport, markets and inputs.

New firms and facilities may emerge over time in response to technology, demand, labour, capital, inputs, transport accessibility and suitable sites. Existing firms can expand, open or close individual plants, acquire other firms or properties, be acquired, decline or fail.

A new industry can buy and adapt a suitable existing property when plausible. Industrial decline can therefore leave brownfields that later return to productive use or are converted as the surrounding city changes.

### 10.3 Historical and seasonal demand

Commodity importance and the available commodity catalogue change over time. New technologies and industries can introduce new physical commodity groups and supply chains, for example later petroleum products, plastics, industrial chemicals and electronics. These are world/economic developments, not player-level unlock rewards.

Older commodities do not disappear on a hard global end date. Their demand can decline, relocate or survive for decades according to actual industries, technologies, prices and regional conditions. Existing viable firms and flows continue until real economic causes change them.

Historical substitution acts on **specific uses** of a commodity. When a new technology appears, it can take market share from an older input only where firms, utilities, transport operators or households actually modernize and where the new alternative is available/economic. This changes production volumes, local prices and freight demand over time.

Coal is the reference case: it can begin as a major input to steam transport, heavy industry, heating, electricity and town gas, then lose portions of those markets to refined fuels, electricity, processed natural gas and later generation technologies. Coal demand can therefore fall sharply without the commodity or its mines being globally disabled. Regions/firms with remaining viable uses can continue producing and consuming it.

Examples:

- coal becomes critical in the industrial age and later declines relatively,
- oil and gas rise later,
- electricity systems alter energy demand,
- modern renewables change demand again.

Demand can also be seasonal where the underlying economy supports it. Examples include harvests, food processing, heating fuel, construction seasons and other recurring production/consumption cycles.

The canonical commodity-group/chain catalogue is owned by [V1_CONTENT_MANIFEST.md](V1_CONTENT_MANIFEST.md). It includes forestry/furniture/paper, several food chains, textiles/clothing, distinct construction materials including glass, coal/iron/steel/metal/machinery, maintenance supplies, early gas/electric utility demand, historically bounded oil products and general consumer goods. Later historical content adds chemicals, plastics, natural gas, fertilizers, medical supplies and electronics. **Electronics includes semiconductor chips/components rather than exposing chips as a separate cargo group.** Older viable routes are displaced only through real modernization/economics, never a global cutoff.

Seasonality must come from the actual simulated business/population context rather than flat global multipliers. Its intensity and cargo mix can change by era, region, technology and economic development.

Industrial decline can leave physical brownfields.

### 10.4 Market accessibility

Firms do not search every destination in Europe every tick.

Regional/market accessibility is cached and updated when relevant transport or economic conditions change.

Better infrastructure can open previously uneconomic markets.

### 10.5 Local commodity markets and prices

Physical commodities have **real local market prices** that can differ between market areas, including several distinct market areas inside one large city.

The hierarchy is **firm/facility → market area → city/region aggregation**. A market area is a local economic catchment, not a teleportation zone. Two firms in the same market area still require real physical transport between their actual endpoints. Small settlements may have one market area; large cities can have several, such as a centre, industrial district, port/rail district or peripheral production zone.

Market-area boundaries can evolve gradually as cities expand, industrial concentrations move and transport accessibility changes. Do not redraw them every tick; changes are coarse/event-driven and preserve stable identities/history where possible.

Each commodity has a historically evolving **base/reference value** appropriate to the era. Local price formation is anchored around that value but driven by the simulated local economy rather than a fixed global commodity table. Relevant inputs include:

- local production and available seller inventory;
- local consumption and buyer demand;
- contracted/committed supply already spoken for;
- storage constraints and stock buffers;
- accessibility of alternative suppliers/markets;
- available transport capacity and effective transport cost;
- seasonal and historical changes in production/consumption;
- disruptions or shortages that materially affect availability.

A local reference price is an economic signal, not an automatic transaction price or guaranteed trade. A high reference price in Brno and a low one in Jihlava can create an incentive for firms to buy/sell across those markets, but actual trade still requires willing firms, compatible quantities, transport, facilities, licences and contractual terms.

Concrete purchase/sale terms are negotiated with the actual firm. Commercial UI should show the relevant local reference price beside the concrete quoted/negotiated price, quantity, contract duration and transport responsibility so the player can understand the comparison without exposing a counterparty's private reservation price or internal margin.

The player's transport company is not a general commodity-speculation business. It normally transports cargo owned by real sellers/buyers. The player can still buy physical commodities genuinely consumed by its own operations or projects, such as coal, fuel, electricity, parts or construction supplies, through the canonical procurement/supplier systems.

Transport can **change the local markets themselves**. When sustained flows move a commodity from a surplus/cheap market into a deficit/expensive market:

- the origin surplus shrinks and its local price can rise;
- the destination deficit shrinks and its local price can fall;
- the price gap and unmet demand can therefore narrow over time;
- if demand, production or accessibility later changes, the gap can widen again.

Do not preserve an artificial permanent arbitrage gap after transport has materially changed the underlying supply/demand balance. Likewise, do not snap prices to equality instantly: adjustment follows the coarse/event-driven market update model and actual physical deliveries/available stock.

This means a successful freight corridor can partially consume the market imbalance that originally made it attractive. Long-term profitability depends on continuing production/consumption, growth, seasonality, competing carriers and changing transport/access costs rather than a fixed route bonus.

Prices must be explainable. The UI should be able to show why a market is expensive/cheap, for example:

> Brno — timber  
> Local demand: 390 t/month  
> Local supply: 80 t/month  
> Net deficit: 310 t/month  
> Alternative supply access: limited  
> Current local reference price: 27 money/t

Do not expose perfect information the player's company could not plausibly know. Market visibility follows the same branch/communications/information rules as other commercial intelligence; unknown or stale information should be labelled accordingly.

Local price changes are event/coarse-tick driven and aggregated. Do not continuously solve every firm-to-firm market pair every frame.

### 10.6 Market intelligence for transport opportunities

The player can inspect aggregated market intelligence to identify potential transport corridors before a concrete customer opportunity exists.

Useful views can include:

- commodity;
- city/market area;
- local production;
- local consumption;
- surplus/deficit;
- local reference price and recent trend;
- known major producers/buyers;
- known existing transport availability/capacity where the player can legitimately observe it.

A price gap between two markets can indicate a potential transport opportunity, but the game must not convert it into an automatic profit score. The player decides whether the corridor is worth pursuing.

This market-intelligence layer is distinct from the Opportunity Board:

- **Market** answers where supply/demand/price imbalances exist;
- **Opportunity Board** lists concrete discoverable jobs/tenders/offers from real counterparties.

The two systems can link to each other, but one does not fabricate the other.

The Market supports three legitimate ways to turn intelligence into business:

1. **React to an Opportunity** already created by a real customer/authority.
2. **Propose a commercial connection** between a legitimately known producer and buyer whose real supply/demand can support the trade, while offering the transport service. The player does not buy/resell the commodity; both counterparties independently evaluate the resulting sale/purchase and transport economics.
3. **Build or extend a transport corridor/service strategically** and let firms discover/use the resulting real transport option when it is competitive.

The second and third paths must not manufacture demand, inventory or counterparties. If the player knows only an aggregate deficit but not a concrete buyer, the UI may show that the company lacks sufficient commercial intelligence rather than revealing hidden firms.

Opening a specific commodity in Market automatically activates its corresponding market analysis on the main map while keeping the Market window available. The spatial view exposes both local surplus/deficit and local reference price together; exact visual encoding is UI implementation work.

## 11. Contracts and cargo

### 11.0 Opportunity Board / commercial opportunities

The player's primary discovery UI for available business is a **filterable Opportunity Board**. It aggregates only opportunities the company is currently able to discover under the branch/commercial-coverage and communications rules in Section 7.2, plus any public/direct opportunities that the company's current business systems can plausibly receive.

The board can contain:

- one-off freight or passenger/group transport jobs;
- recurring/framework freight or passenger transport contracts;
- public/state/municipal tenders;
- private customer tenders, including tour operators/employers/event organizers;
- direct customer offers;
- subcontracting opportunities from other carriers;
- strategically advertised opportunities outside the normal branch network.

The board is a discovery and comparison interface, not a source of fake demand. Every listed opportunity must originate from a real simulated customer, public authority, carrier partner or market need.

The list must remain usable as the company grows. The player can filter and sort without opening each opportunity individually.

Core filters should include, where relevant:

- transport mode: road, rail, water, urban/multimodal;
- passenger vs cargo;
- cargo type/family;
- origin region/city/customer;
- destination region/city/customer;
- local branch/region;
- one-off vs recurring/framework vs tender;
- public vs private vs carrier-subcontract;
- contract duration;
- start date / deadline;
- expected volume or passenger requirement;
- required capacity;
- estimated revenue/value;
- expected margin when enough cost data is known;
- relationship/customer;
- reputation/qualification requirement;
- required licences/permissions;
- infrastructure or terminal requirements;
- service-level / delivery-time requirement;
- seasonal vs year-round;
- opportunity status, such as new, viewed, bid submitted, expiring soon.

Useful sorting can include:

- newest,
- deadline soonest,
- highest value,
- highest estimated margin,
- shortest/longest duration,
- lowest missing-capability gap,
- best customer relationship,
- nearest origin/operating area.

Filters must be combinable and easy to clear. The UI should support saved filter presets or favourites later, but the base interaction must remain simple enough for early-game use.

The board should also support a **feasibility summary** for each opportunity without requiring the full contract planner. Example statuses:

- **Ready** — existing fleet/infrastructure/staff can plausibly fulfil it;
- **Requires investment** — feasible after specific purchases/building/access;
- **Missing licence/access** — blocked by a concrete legal/infrastructure prerequisite;
- **Capacity conflict** — current commitments make the requirement infeasible;
- **Outside local pipeline** — visible only because it is public/directly offered.

These statuses are explanations, not automatic accept/reject decisions. A player may still bid strategically on an opportunity that requires investment.

The game should avoid overwhelming the player with every theoretical opportunity in Europe. At the starting local-office stage, routine discovery is city-scoped: if the company has only a Praha branch, ordinary local opportunities from Brno are not merely filtered out — they are not known to the company yet. Later company communication/IT systems broaden this scope under Section 7.2. The board can summarize or paginate large result sets rather than continuously rendering every opportunity.

When the player opens an opportunity, the next step is the normal contract evaluation/planning flow: inspect terms, estimate fleet/infrastructure/staff needs, secure any required capacity, and bid/accept according to the contract model below.

### 11.0.1 Opportunity detail and Contract Planner

Opening an Opportunity Board item launches a **Contract Planner**. Its purpose is to answer five questions before the player commits:

1. **What exactly is the customer asking for?**
2. **Can the company physically and legally perform it?**
3. **What must be bought, built, hired or contracted first?**
4. **Can everything be ready before the required start date?**
5. **What is the expected financial result and risk?**

The planner should be useful for a tiny first job and for a later strategic multimodal contract. Detail is progressively disclosed rather than forcing every player through a large expert form.

#### Contract summary

The first view should show the commercially important terms in a compact summary:

- customer / contracting authority;
- origin and destination;
- passenger or cargo type;
- expected/minimum/maximum volume as applicable;
- one-off, recurring, framework, seasonal or tender structure;
- contract start/end dates;
- operating/service windows;
- delivery-time or service-level requirement;
- guaranteed/reserved capacity requirement;
- offered price or current bid price;
- performance bonuses;
- penalties and material breach conditions;
- exclusivity where relevant;
- award deadline and expected award date;
- relationship/reputation/qualification requirements;
- required licences, insurance or local presence.

The planner must distinguish **guaranteed contractual quantities** from forecasts. A customer estimate such as "typically 300–500 t/month" must not be presented as guaranteed revenue unless the contract actually guarantees that volume/payment.

#### Proposed operating solution

The player can select or let the planner suggest one or more feasible operating concepts.

Examples:

- direct road haul;
- rail with local truck collection/delivery;
- direct train;
- multimodal rail/water/road;
- own transport plus partner/subcontracted leg.

A proposal defines enough operational detail to estimate feasibility:

- route and mode(s);
- required Service Pattern(s) or demand-driven movements;
- approximate frequency;
- train/vehicle/consist requirement;
- terminals/stations used;
- transfer points and storage;
- operating/dispatch depots;
- maintenance coverage;
- required third-party infrastructure access.

The player is never forced to accept the suggested solution. Alternative valid solutions can be compared.

#### Contract Transport Plan and transport legs

A signed or proposed customer contract is **not directly bound to one Line**.

Instead, a contract defines a reusable **Transport Plan** template describing fulfilment from contractual origin to destination. Each shipment or passenger-group execution uses a versioned instance of that plan. Replanning one shipment must not mutate the template or the execution state of other shipments. The cargo identities and accounting are defined in Section 11.9.

The Transport Plan is composed of one or more ordered **transport legs**.

Example:

> Customer factory  
> → own truck collection leg  
> → Praha freight terminal  
> → existing Praha–Brno freight Line / Service Pattern  
> → Brno freight terminal  
> → external last-mile carrier  
> → final customer

Each leg can use one of several execution types:

1. **Existing Line / Service Pattern** — allocate contract cargo/passenger demand onto an existing regular service with sufficient compatible spare capacity.
2. **New Line / Service Pattern** — create a new regular service because recurring volume justifies one.
3. **Own ad-hoc / demand-driven movement** — use the player's own fleet for a non-regular pickup, delivery or one-off movement without creating a permanent Line.
4. **External carrier** — purchase that leg through the shared External Transport Order system in Section 30.1.
5. **Customer-provided leg/service** — the customer or another contract party is explicitly responsible for that leg.

A contract can therefore combine several modes and several operating mechanisms without pretending that the whole obligation is one train, truck or Line.

The Transport Plan records for each leg:

- origin and destination endpoint;
- cargo/passenger responsibility;
- execution type;
- assigned Line/Service Pattern where applicable;
- frequency or dispatch condition;
- required capacity;
- transfer/storage point;
- timing/deadline contribution;
- responsible carrier/operator;
- infrastructure/access dependencies.

Transfers between legs are physical.

CargoLot state moves through the real chain:

- pickup/loading;
- movement;
- unload/transfer;
- physical storage/waiting where necessary;
- loading onto the next Trip;
- final delivery.

No leg handoff teleports cargo between vehicles, terminals or operators.

##### Existing regular lines as shared capacity

A regular freight Line/Service Pattern can carry demand from **multiple contracts and non-contract cargo at the same time**.

Recurring freight business is primarily contract-driven. A freight Line can additionally publish **open/spot carriage** for compatible spare capacity, but this is deliberately supplementary rather than the normal way a large stable industrial flow is moved.

Open freight uses a public tariff by handling/cargo category (for example ordinary/general goods, bulk, liquids, refrigerated/perishable, hazardous and special/oversized categories), with optional commodity-specific overrides. Contract freight uses its separately negotiated transport price.

A firm can send only a bounded **percentage of its relevant uncontracted flow** through open carriage. This prevents a huge stable producer-consumer flow from silently becoming unlimited anonymous spot cargo. The percentage is **not global**: it can vary transparently by firm type/size, commodity/handling category, flow regularity and the specific producer-consumer relationship. The current limit and its contributing reasons must be inspectable in the commercial/market context; do not hide it behind an unexplained modifier. It must never exceed the real available uncontracted quantity. Stable, predictable high-volume flows should generally have a lower open-carriage share and create a stronger incentive for the parties/carrier to negotiate a recurring contract, while more irregular or standardized flows can tolerate a higher share.

Open carriage still requires a real origin, destination, compatible handling, available Trip capacity and physical loading/unloading. It never creates cargo merely because a timetable has spare space.

Example:

> Praha–Brno Night Freight  
> Total usable capacity: 600 t  
> Contract A allocation: 80 t  
> Contract B allocation: 120 t  
> One-off jobs: 40 t  
> Remaining sellable/usable capacity: 360 t

The Contract Planner should first check whether suitable existing services have compatible spare capacity before proposing a dedicated new Line.

If an existing service is usable, the planner shows:

- total compatible capacity;
- already committed contract capacity;
- expected non-contract load;
- new contract requirement;
- remaining reserve after allocation.

A contract allocation is a real capacity commitment and cannot be double-booked.

##### Freight reservation cutoff and missed connection handling

Reserved freight capacity on a regular Trip can have a **cargo readiness cutoff** before departure.

Before that cutoff, the reserved capacity remains protected for the contract cargo.

If the contract cargo is not physically ready by the cutoff, the system must determine **why** before deciding whether that capacity can be released.

The key distinction is responsibility:

1. **Customer-side / customer-provided delay** — the customer or a customer-responsible leg failed to present the cargo on time.
2. **Carrier-side delay** — the player's own collection leg, terminal handling, fleet, staff, planning or another responsibility controlled by the player caused the cargo to miss the cutoff.
3. **Player-contracted subcontractor delay** — treated toward the customer as carrier-side responsibility unless the customer contract explicitly says otherwise; the player may separately seek compensation from the subcontractor.
4. **Qualifying external/infrastructure disruption** — handled according to the contract/access force-majeure, re-protection and compensation rules rather than automatically assigning blame to either side.

If the cargo is late because of **customer-side responsibility**, the unused reserved capacity may be released after the contractual cutoff, subject to any minimum-payment/no-show terms.

If the cargo is late because of **carrier-side responsibility**, the system must **not** treat the missing cargo as a customer no-show and silently release the commercial obligation.

The dispatcher then chooses a recovery action:

- **Hold the trunk Trip** for the delayed cargo when the expected wait is acceptable and the Trip can still operate within its slot/tolerance and downstream commitments;
- **Hold and accept operational consequences** where the player/authorized manager deliberately chooses to wait beyond the normal margin, understanding that the Trip can lose slot protection, delay other cargo/passengers and create additional access/penalty costs;
- **Depart without the cargo**, record a carrier-side missed connection, and automatically rebook the affected CargoLot onto the next compatible Trip with sufficient capacity;
- create an **ad-hoc recovery movement** or hire an external carrier when waiting for the next normal Trip would breach the customer SLA.

The recovery choice must consider the whole Transport Plan, not only the current train.

Example:

> Contract cargo is due on the 18:00 freight Trip.  
> Player-operated collection truck arrives 22 minutes late.  
> Holding the train 8 minutes still fits the rail slot; holding 22 minutes does not.  
> → dispatcher can wait 8 minutes if that makes the transfer, otherwise depart and rebook/arrange recovery.

If the Trip departs without carrier-delayed contract cargo, the player's obligation **continues**.

The missed quantity is carried forward as an unfulfilled priority requirement and must be assigned to:

- the next compatible scheduled Trip;
- an added/overflow Trip;
- an ad-hoc own movement;
- or an external carrier.

If the delayed quantity causes the next Trip to exceed compatible capacity, lower-priority discretionary/spot cargo can be displaced according to the loading-priority rules, but another guaranteed customer commitment cannot be silently broken.

Any contractual SLA breach, late-delivery penalty or relationship impact remains attached to the responsible customer contract. Rebooking does not erase the failure.

The player can set a **maximum hold policy** at Line/Service Pattern or contract-allocation level, with manager automation allowed inside that limit. The UI should show the likely consequences of waiting versus departing.

##### Freight loading priority and capacity allocation

A freight Trip does not simply load cargo in arbitrary arrival order or by one hidden profitability score.

Loading is determined in two stages:

1. **Physical compatibility / usable capacity**
2. **Commercial priority within that compatible capacity**

###### Physical compatibility first

Before priority is considered, the system determines which cargo can physically use which part of the consist/capacity.

Relevant constraints can include:

- wagon/vehicle cargo type;
- weight capacity;
- volume capacity;
- pallet/container/vehicle positions where relevant;
- axle/load limits;
- refrigeration/temperature capability;
- dangerous-goods compatibility/separation;
- loading/unloading equipment;
- destination/route compatibility;
- train-length and total-train-weight limits;
- wagon placement or handling constraints where operationally material.

The game must therefore not present a freight Trip as having "100 t free" if the only available space is in wagons incompatible with the waiting cargo.

The UI should show **compatible free capacity** for the selected cargo/contract, not only total nominal tonnes.

###### Commercial priority tiers

Within physically compatible capacity, the default loading priority is:

1. **Protected / guaranteed contract commitments**
2. **Firm recurring or framework contract cargo without a hard guarantee**
3. **Confirmed one-off transport jobs**
4. **Spot / opportunistic cargo**

Guaranteed capacity remains protected until its contractual readiness cutoff under the rules above.

After a valid **customer-side** no-show/cutoff release, that unused capacity becomes available to lower-priority cargo for that Trip.

If the cargo missed the connection because of **carrier-side responsibility**, its commercial obligation is not downgraded to spot cargo. It remains a recovery obligation under the rules above.

###### Recovery cargo and guaranteed commitments

Carrier-fault recovery cargo from a missed guaranteed connection remains a **protected contractual obligation**.

However, it cannot silently displace another customer's already valid guaranteed commitment on the next Trip.

If two or more protected commitments cannot all fit because the carrier created an overload, the dispatcher must expose the conflict and create a recovery plan, such as:

- add compatible capacity/vehicles to the Trip where feasible;
- add an overflow/ad-hoc Trip;
- use another compatible scheduled Trip;
- hire an external carrier;
- accept a visible breach/late delivery for the affected contract.

The system must not solve a carrier-created capacity deficit by secretly breaking a different guaranteed contract.

###### Priority inside the same tier

When several compatible CargoLots share the same commercial priority tier, the dispatcher uses transparent urgency rather than arbitrary first-come randomness.

The primary ordering should consider:

1. **last feasible departure / SLA urgency** — cargo that must use this Trip to meet its deadline goes before cargo that can safely use a later Trip;
2. **perishability / quality risk** where the contracts otherwise have similar urgency;
3. **earlier confirmed booking/readiness** as a final deterministic tie-breaker.

The UI should be able to explain why one batch received capacity ahead of another.

Example:

> Batch A deadline: 04:00 tomorrow — next Trip would be too late  
> Batch B deadline: 18:00 tomorrow — next Trip remains feasible  
> → Batch A receives the remaining compatible capacity.

A higher-margin spot shipment does not jump ahead of a lower-margin guaranteed contract merely because it is more profitable.

###### Loading plan and consist use

The system generates a physical loading/consist plan from the selected CargoLots.

For rail this can include:

- which wagons carry which CargoLots;
- required wagon type;
- destination grouping where useful;
- dangerous-goods separation;
- unloading order / wagon positioning where relevant;
- resulting train weight and length.

The player does not need to assign every pallet or tonne manually by default.

Yard/terminal automation can build the plan, but the wagons, loading tracks, handling equipment and shunting movements must physically exist.

Advanced/manual overrides can pin a contract/cargo family to specific capacity where the player wants tighter control.

###### Unused and released capacity

Capacity that remains unused after all protected/confirmed cargo is allocated can be offered to lower-priority cargo.

For a regular freight service this allows spare capacity to earn additional revenue without weakening protected commitments.

The Line/Trip UI should distinguish:

- **guaranteed reserved**;
- **firm booked**;
- **one-off booked**;
- **spot allocated**;
- **still free compatible capacity**.

This accounting is recalculated when cargo readiness, consist, contracts or recovery obligations change.

If the existing Pattern cannot cover the requirement, the planner can propose:

- larger/more vehicles;
- higher frequency;
- another Service Pattern on the same Line;
- a new Line;
- an ad-hoc overflow movement;
- external carrier capacity.

##### Local collection and last-mile legs

A local pickup/delivery leg does not automatically need its own Line.

For example, a factory-to-terminal road collection can be a demand-driven contract leg:

> when an eligible shipment batch is ready  
> → assign compatible truck capacity  
> → collect from customer endpoint  
> → deliver to terminal before the booked trunk departure.

If repeated volume grows enough, the player can later convert such work into a regular freight Line/Pattern and use it for several contracts.

##### Contract versus Line lifecycle

A **Contract** defines the commercial obligation.

A **Line** defines a reusable regular operating service.

A **Service Pattern** defines one repeating operating variant of that Line.

A **Trip** is one concrete physical movement.

A **Transport Plan** connects the commercial obligation to those operating objects.

This means:

- a Line can exist without any contract;
- one Line can serve many contracts;
- one contract can use many Lines;
- one contract can mix Lines, ad-hoc movements and external carriers;
- ending one contract does not automatically delete a shared Line;
- changing a Line must revalidate every contract allocation that depends on it.

The planner should preserve this separation throughout the UI so the player never has to rebuild the same route/timetable manually for each customer.

#### Requirement checklist

Every material requirement is classified into a transparent checklist.

Typical categories:

- **Fleet / rolling stock** — compatible vehicles, locomotives, wagons and reserve requirement;
- **Service endpoints** — valid origin/destination station, stop, siding, loading point, terminal, berth or equivalent, including whether customer-provided;
- **Infrastructure access** — road/legal access, rail sections, station slots, ports, terminals;
- **Owned or rented facilities** — depot, parking, storage, warehouse, cold store, loading equipment, branch and contracted third-party capacity;
- **Staff** — operating crews and facility-bound staff;
- **Maintenance** — suitable workshop coverage and expected maintenance load;
- **Shunting/yard** — where train formation/transfer requires it;
- **Licences / concessions / permits**;
- **Customer-specific requirements** such as temperature control, dangerous-goods capability or comfort class;
- **Partner/subcontract capacity**;
- **Commercial coverage / local presence** — whether every commercially served city is covered by a required branch or by a later technology-enabled coverage model;
- **Administrative capacity** at the responsible branch/office;
- **Operating supplies / energy** where materially constraining.

Each item shows one of a small number of states:

- **Available** — already covered;
- **Available with spare capacity** — covered and shows remaining margin;
- **Committed / tight** — technically available but conflicts with or materially reduces existing reserve;
- **Must acquire** — available on the market but not currently owned/contracted;
- **Must build** — physical infrastructure/facility required;
- **Must negotiate** — third-party access, partner capacity or permission is not yet secured;
- **Unavailable / incompatible** — the proposed solution cannot currently satisfy the requirement.

The checklist must name the real bottleneck. It should say, for example, "needs 6 refrigerated wagons, you own 4" rather than "fleet insufficient".

#### Current assets versus incremental requirement

The planner must reuse existing capacity before assuming everything is a new purchase.

For each relevant asset/resource, show:

- total compatible capacity;
- capacity already committed elsewhere;
- spare capacity;
- additional capacity needed for this contract;
- reserve/surge margin required by the proposed terms.

Example:

> Refrigerated wagons: 12 owned / 9 already committed / 3 spare / **5 required** → **2 additional needed**

The same principle applies to staff, terminals, storage, workshop time and infrastructure slots.

The system must not double-book an asset simply because two independent contract screens each found it "available" at different times. Feasibility is recalculated when commitments change.

#### Startup / investment plan

Requirements that are not already covered become a project-style **startup plan**.

Possible line items:

- vehicle purchase or lease;
- used-vehicle acquisition;
- depot or terminal construction;
- facility expansion;
- branch construction/upgrade;
- infrastructure access agreement;
- Capacity Order;
- licence/permit application;
- recruitment;
- supply agreement;
- subcontractor/partner agreement.

For each item, show:

- expected one-time cost;
- recurring cost where applicable;
- earliest realistic availability date;
- dependency on another item;
- whether the price/capacity is confirmed or only estimated.

The planner can provide actions such as **Buy vehicles**, **Request capacity**, **Rent facility/access**, **Build facility**, **Apply for licence** or **Hire carrier**, opening the relevant existing system. **Rent facility/access** uses the shared infrastructure/facility access-agreement rules in Section 19.3. **Hire carrier** opens the shared External Transport Order from Section 30.1 with the required leg/cargo/timing already filled in; it is not a separate subcontracting marketplace.

It must **not automatically spend money or sign third-party agreements** merely because the player opened a contract planner or clicked an automatic feasibility calculation.

#### Readiness timeline

A contract can be economically attractive but impossible to start on time.

The planner therefore calculates a high-level critical-path readiness estimate from real lead times such as:

- vehicle manufacturing/readiness;
- normal vehicle repositioning/delivery;
- specialist heavy-haul provider availability, permit preparation and transport where required;
- used-vehicle physical delivery;
- construction;
- licence/permit processing;
- infrastructure-capacity negotiation;
- recruitment;
- vehicle repositioning;
- partner agreement.

The UI should show:

- contract start date;
- expected ready date;
- schedule buffer;
- the item currently defining the critical path.

Example:

> Required start: 4 May  
> Earliest credible readiness: 11 May  
> **7 days late — main constraint: terminal construction**

Where possible, it can propose concrete alternatives such as using an existing third-party terminal, leasing vehicles or negotiating a later contract start.

#### Economics

Financial analysis separates **startup investment**, **recurring operating cost** and **contract revenue**.

Typical cost categories include:

- vehicle acquisition/lease;
- construction/upgrades;
- access/slot reservation fees;
- actual infrastructure usage fees;
- fuel/energy;
- crew and facility staff;
- maintenance/wear;
- loading/handling/storage;
- partner/subcontract payments;
- branch/admin overhead attributable to the contract where material;
- financing cost where the proposed investment requires borrowing;
- expected empty/deadhead/repositioning movements.

Revenue can include:

- guaranteed fixed payment;
- per-unit/per-passenger payment;
- minimum-volume payment;
- forecast variable volume;
- expected performance bonuses, shown separately from guaranteed revenue.

The planner should show at least:

- upfront investment required;
- expected revenue per relevant game period;
- expected recurring cost;
- expected operating contribution/margin;
- expected cash impact;
- approximate investment payback where meaningful;
- exposure to contractual penalties / reserved-capacity commitments.

Do **not** create fake precision.

Confirmed contractual prices and known fees can be exact. Variable quantities such as fuel price, uncertain demand, maintenance, congestion or partner rates should be shown as estimates/ranges or with clearly stated assumptions.

A useful default can be:

- **Guaranteed / floor case** — only contractually guaranteed revenue and reasonably committed costs;
- **Expected case** — current expected volume/cost assumptions;
- **Risk flags** — major variables that could materially change the result.

A speculative "best case" should not be used to make a weak contract appear attractive.

#### Opportunity economics versus company economics

The planner must distinguish:

- **contract profitability** — revenue and incremental costs caused by the contract;
- **cash feasibility** — whether the company can actually finance the required startup investment and survive the ramp-up period.

A profitable five-year contract can still be impossible for a small company if it requires an unaffordable terminal before the first payment.

The UI should therefore show projected minimum cash requirement / funding gap before activation where material.

#### Bid changes update the plan

For bid/tender contracts, changing commercial parameters should update the feasibility and economics immediately.

Examples:

- lower bid price reduces margin;
- stronger SLA may require extra reserve fleet;
- higher guaranteed volume can require another train/vehicle cycle;
- shorter response window may require locally staged reserve assets;
- longer term can improve investment payback while increasing commitment risk.

This connects the existing parameter-based negotiation system to real operational consequences.

#### Bidding before all resources are owned

The company does not always need to own every required asset before submitting a bid.

If the tender/contract rules permit it, the player may bid based on a credible acquisition/construction plan.

The planner distinguishes:

- **ready now**;
- **credible by required start date**;
- **at risk**;
- **cannot credibly be ready**.

If awarded, the contract becomes a real future commitment. The game does not magically deliver the planned assets. The player must complete the required purchases, construction, access negotiations and staffing before operations begin.

AI competitors use the same principle: a bid may rely on credible planned investment but cannot assume impossible lead times or nonexistent capacity.

#### Dependency handling

A customer contract and its supporting agreements remain separate.

For example, winning a rail freight contract does not automatically:

- buy rail/station slots;
- purchase wagons;
- sign a fuel contract;
- build a warehouse;
- hire a subcontractor.

The planner can group these requirements into one implementation checklist and coordinate their workflows, but each purchase/agreement remains explicit and subject to its own capacity, price and contract rules.

If a supporting dependency later fails, the player receives a concrete warning and the contract feasibility status updates.

#### Performance

Contract feasibility uses cached network, fleet, facility, staffing and access data and is recalculated on relevant changes rather than continuously every frame.

Full route/cost recalculation can run when:

- an opportunity is opened;
- the proposed operating solution changes;
- bid terms change materially;
- company capacity/commitments change;
- a required access/facility price changes;
- the player explicitly refreshes/rechecks the plan.

The board may use cheaper cached feasibility summaries; the full planner performs the deeper calculation.

### 11.1 Contracts are central

Cargo gameplay is primarily contract-driven, while passenger gameplay combines normal market demand with **public and commercial passenger contracts**.

Early game emphasizes direct management of individual jobs and vehicles.

Contract types include:

- one-off freight shipment;
- recurring/framework freight contract;
- state/public/municipal transport contract;
- carrier subcontract;
- long-term supply contract;
- one-off commercial passenger/group transport;
- recurring commercial passenger/group transport;
- reserved passenger-capacity agreement on an existing Line.

Contract awards should consider transparent factors such as price, capacity, reliability, relevant reputation and customer-specific relationship history. The player must be able to inspect the important decision factors before or after bidding.

Public authorities can maintain a small set of **public development/transport priorities** derived from real aggregate conditions and policy goals, such as an under-served passenger corridor, insufficient freight capacity, poor regional accessibility or a strategically important economic connection. These priorities are inspectable before a tender exists and show the supporting known problem/evidence and status. A priority is not a guaranteed future tender.

Authorities are not omniscient and do not subsidize a corridor merely because the player could profit from it. A service tender is created when the authority has a real public/strategic need, available policy/budget authority and the existing market/service does not already satisfy the stated requirement. The tender's payment is a public service/operating subsidy or other explicit contract payment; it does not fabricate passengers or cargo.

For **public/state/municipal service tenders**, use an explicit two-stage rule:

1. every submitted proposal must satisfy all mandatory tender requirements; an invalid proposal cannot be submitted as a compliant bid;
2. compliant bids are scored using the authority's published criteria and weights.

Price/requested operating subsidy is normally the highest-weight factor, but an authority can also publish weights for relevant-mode operating reliability, company commercial reliability, comfort/service quality where applicable, and company reputation. Do not use hidden preference weights. The UI shows the formula/weights and the player's currently knowable inputs before submission.

Relevant-mode reliability is derived from real history for the mode being tendered, such as rail versus road. Commercial reliability is separate and reflects fulfilment of contracts, promised launch dates, payments/fees and other business obligations. General reputation remains a separate criterion so the same history is not counted twice. New carriers/new modes start from a mildly positive neutral baseline rather than zero or a strong bonus; real history progressively replaces that prior. Ordinary isolated failures have small effects, repeated failures create a trend, and serious material breaches can cause a larger change.

A public-tender bid contains a **concrete service proposal**, not only a subsidy number. It can extend an existing Line, alter a future Line version or propose a new Line/Pattern, provided the proposal meets the tender's required served points/corridor, minimum frequency, capacity, timing/travel-time and quality constraints. The bidder can choose how to meet those outcomes. A proposal may depend on feasible future purchases/access that can genuinely be secured by the promised start date, but it cannot rely on impossible or fabricated capacity.

Competitors' submitted bid terms remain sealed until the tender closes. The player can see the published evaluation method and evaluate their own proposal, but cannot simply undercut a visible rival by one money unit. After award, the result exposes the material scoring breakdown for all legitimately public bids so the outcome is explainable.

Winning binds the **service outcomes promised by the award**, not every internal operating detail forever. The operator may later change vehicles, exact timetable or internal resource allocation without a new award if the service continues to meet all binding route/coverage, frequency, capacity, journey-time, comfort/quality and reliability conditions. Material changes outside those bounds require the applicable amendment/authority process.

Public-service failure is progressive: minor isolated failures affect measured reliability; repeated/material failure can reduce the corresponding subsidy/payment, trigger contract penalties and a cure period; persistent or serious breach can allow termination and a new tender. The operator can also terminate under the contract's notice/settlement rules. Public-service contracts may be fixed-term or, where explicitly offered, indefinite with notice/termination rules. Strategic indefinite awards may require published minimum history/qualification thresholds; other tenders may remain open to new entrants.

Large customers may reserve their most important contracts for carriers with proven history, while still exposing smaller trial jobs that let new entrants build trust.

Contracts can be seasonal or have seasonal volume profiles when the underlying customer demand is seasonal. A seasonal contract must show its expected calendar profile before signing, including peak months/periods, expected baseline volume and likely surge range. Historical plausibility applies: early eras should not generate modern mass-tourism or modern consumption patterns simply because the calendar says summer/winter.

All contractual periods and volume-rate units use Section 3's calendar. A monthly volume covers 14 game days; a yearly term covers 168. Notice, cancellation, expiry and renewal must use that same basis.

#### 11.1.1 Commercial passenger and group-transport contracts

Private organizations can purchase passenger transport in the same simulated market rather than every passenger movement coming only from anonymous individual demand.

Possible customers include:

- tour operators / travel agencies;
- companies/employers;
- schools/universities;
- hotels/resorts;
- event organizers;
- clubs/associations;
- conference organizers;
- other organizations needing a defined group moved.

Typical contract examples include:

- **Tour-operator excursion:** transport 48 tourists from Praha to Český Krumlov in the morning and return them in the evening;
- **Multi-day tour movement:** move a tour group between several cities on specified dates;
- **Corporate shuttle:** recurring employee transport between a station/city and a factory/office;
- **School trip:** one-off group movement with specified pickup/return windows;
- **Event transport:** move defined groups to/from a fair, concert or sporting event;
- **Reserved seats on a regular service:** a tour operator buys 40 seats on selected weekly departures of an existing intercity Line.

These contracts can be fulfilled through the normal **Contract Transport Plan**.

Depending on the requirement, a passenger leg can use:

- an existing passenger Line / Service Pattern with reserved compatible capacity;
- a dedicated ad-hoc bus/coach/train movement without creating a permanent Line;
- a newly created recurring Line/Pattern;
- an external passenger carrier;
- a customer-provided leg.

A one-off tour does **not** require the player to create a permanent Line simply because the group travels between two cities.

Example:

> Tour operator contract: 52 passengers, Praha hotel → Salzburg hotel  
> Leg 1: charter bus from hotel to Praha station  
> Leg 2: 52 reserved seats on player's existing Praha–Salzburg train  
> Leg 3: external local coach from Salzburg station to hotel

Alternatively, if the player has suitable coaches and the economics work:

> one dedicated charter coach Trip Praha hotel → Salzburg hotel

The Contract Planner compares these alternatives using real capacity, travel time, cost and readiness.

Commercial passenger contracts can specify requirements such as:

- passenger count or range;
- guaranteed/minimum paid capacity;
- pickup/drop-off location;
- departure/arrival window;
- return journey;
- baggage requirement;
- comfort/service class;
- accessibility;
- catering/other onboard service where relevant;
- dedicated vehicle requirement;
- exclusivity/no-mixing requirement where requested;
- maximum transfers;
- SLA / punctuality;
- cancellation/no-show terms.

A customer can either pay:

- a fixed group/charter price;
- a per-passenger amount with a guaranteed minimum;
- a recurring reserved-capacity fee;
- or another clearly disclosed contract structure.

If a contract reserves seats on a normal passenger Line, those seats become a real capacity commitment for the relevant origin-destination legs and Trips. They do not require a separate train/bus unless the contract explicitly asks for dedicated transport.

Unused contracted passenger capacity can be released after the applicable contractual cutoff/no-show rules, but carrier-caused feeder/connection failure must not be treated as a customer no-show. Recovery follows the same responsibility principle used for freight connections.

Commercial group transport remains distinct from ordinary individual passenger demand. Normal passengers still choose and buy travel from the simulated passenger market; a tour operator or employer contract is a separate commercial commitment.

### 11.2 Contract award models

Contract complexity scales with importance so routine work does not become paperwork:

1. **Small / routine jobs:** fixed offer; accept or decline.
2. **Medium contracts:** the player mainly bids price and capacity.
3. **Large contracts:** structured tender with price, guaranteed capacity, delivery/service level and contract duration.
4. **Strategic long-term contracts:** structured tender plus limited negotiation over terms such as price, guaranteed volume, duration, service level and penalties.

Negotiation is parameter-based rather than a dialogue mini-game. The UI should immediately show the commercial effect of changing a term.

Routine bidding can later be delegated to commercial managers using player-defined rules such as minimum margin, maximum commitment, customer priority and approval thresholds.

AI competitors must bid from their real available capacity, costs, network access, relationship and strategy. They must not generate fake impossible bids simply to beat the player.

Renewal of eligible recurring agreements follows Section 11.12. Auto-renewal does not bypass a required new tender or grant an incumbent an automatic win.

### 11.3 Exclusivity

Large or strategic contracts can include exclusivity.

An exclusive contract can guarantee the carrier all or most of a customer's defined transport volume for the covered flow, period or commodity.

In return, the carrier accepts stronger obligations such as:

- guaranteed minimum capacity,
- stricter reliability/service-level targets,
- stronger penalties for failure,
- potentially reserved fleet/infrastructure capacity,
- limited ability to reject individual shipments within the agreed range.

Exclusivity is optional and must be priced as a risk/reward trade-off. It can create stable revenue and deepen customer relationships, but can become costly if the carrier overcommits.

The customer must still have emergency fallback rights where the contract explicitly allows them, for example after repeated SLA breaches or when the carrier cannot accept the guaranteed volume.

### 11.4 Performance bonuses

Medium, large and strategic contracts can include optional bonus tiers above the minimum SLA.

Examples:

- contract requires delivery within 48 hours, but average delivery under 30 hours earns a higher rate;
- contract requires 95% on-time performance, while 99% earns a periodic performance bonus;
- contract guarantees a minimum monthly volume, while handling surge volume without failure earns an additional payment;
- exceptionally low damage/spoilage can improve payout for sensitive cargo.

Bonuses must be visible before signing and tied to measurable contract KPIs. They should reward operational excellence rather than create hidden modifiers.

Performance above the contractual minimum can also improve customer-specific relationship history and relevant reputation, but the direct financial bonus and the relationship/reputation effect remain separate systems.

### 11.5 Reserved capacity commitments

Some medium, large and strategic contracts can require the carrier to keep a defined amount of transport capacity available for the customer, including surge/emergency capacity that may not be used every day.

This must be completely transparent and expressed in both commercial and physical terms before signing.

The contract planner should show, for the proposed route and service pattern:

- guaranteed tonnes/passengers per period,
- maximum surge requirement,
- response window,
- estimated number and type of wagons/vehicles required,
- locomotives/traction required,
- terminal/storage requirements,
- expected infrastructure capacity consumption,
- estimated staff requirement,
- how much of the player's currently available fleet would become committed,
- what spare capacity remains after accepting the contract.

For example, instead of only displaying "reserve 200 t capacity", the UI should translate that into something like "requires approximately 8 compatible wagons and 1 suitable locomotive available within 24 hours on this corridor" based on the player's current rolling stock and route.

Reserved capacity is a real commitment, not a hidden score. Assets do not necessarily need to sit idle permanently: they may perform other work when scheduling still guarantees the contracted response time. Dispatch automation may manage this later, but it must never allocate committed assets in a way that silently makes the SLA impossible.

If current fleet, depot, terminal or infrastructure capacity cannot credibly satisfy the commitment, the game must warn the player before the bid is submitted and explain the bottleneck.

The Contract Planner in Section 11.0.1 is the primary pre-signing UI for this physical-capacity accounting. It must reuse the same fleet, staff, terminal, storage and infrastructure commitment data rather than maintaining a separate approximate capacity model.

AI competitors are subject to the same capacity accounting and cannot promise reserve capacity they cannot realistically provide.

### 11.6 Contract renegotiation

Long-running contracts can be reopened when material operating conditions change.

Valid triggers can include:

- major fuel or energy price shocks,
- border closures or regulatory changes,
- loss of access to a previously valid route,
- major infrastructure disruption,
- exceptional input-cost inflation,
- customer-requested volume or SLA changes,
- mutually agreed strategic restructuring.

Renegotiation is not a free escape from a bad deal. The requesting side must state what changed and propose concrete revised terms.

Possible changes include:

- price,
- guaranteed volume,
- reserved capacity,
- delivery/service-level target,
- contract duration,
- penalties,
- exclusivity.

The counterparty can accept, reject or make a counteroffer.

The UI must show why the other party reacts the way it does, using transparent factors such as the size of the cost shock, existing relationship, alternative carriers, contract performance and remaining contract duration.

A weak justification or repeated attempts to reopen favourable terms can damage customer relationship and reputation. A genuine external shock should carry much smaller or no reputational penalty.

Contracts may also contain pre-agreed adjustment clauses, such as fuel-price indexing or automatic rate review at defined intervals, reducing the need for manual renegotiation.

Commercial managers may later handle routine renegotiations within player-defined limits, while material strategic changes can require player approval.

### 11.7 Customer-driven contract expansion

A customer's real economic growth can increase transport demand during an existing relationship.

When a factory, mine, city or other customer expands production/consumption beyond the original contracted volume, it may first offer the incumbent carrier an extension or amendment to the existing contract rather than automatically creating an unrelated tender.

The offer must show:

- current contracted volume,
- new requested volume,
- whether the increase is permanent, seasonal or temporary,
- additional reserved capacity required,
- estimated additional wagons/vehicles/traction,
- terminal/storage and infrastructure impact,
- revised price/revenue,
- any change in SLA, penalties or exclusivity.

A strong relationship can give the incumbent carrier first negotiation rights or a limited response window, but never guarantees that the extra business is awarded automatically.

The player can:

- accept the expansion,
- accept only part of it,
- negotiate revised commercial terms,
- decline it.

If the incumbent declines or cannot credibly provide the additional capacity, the customer can tender the incremental volume to competitors while keeping the original contract in place where practical.

This creates natural growth paths: a small early contract can expand into a strategically important account as the customer's business grows.

Capacity feasibility uses the same transparent physical accounting as reserved-capacity commitments; the game must warn about concrete fleet, depot, terminal or infrastructure bottlenecks before acceptance.

### 11.8 Early termination and breach

Long-running contracts can end before their planned expiry.

Either side can terminate according to the contract's agreed rules, including notice periods, break clauses, breach thresholds and financial penalties.

Possible customer-side termination reasons include:

- repeated SLA failures,
- failure to provide guaranteed or reserved capacity,
- serious cargo damage/spoilage,
- repeated missed deliveries,
- regulatory or licence loss,
- insolvency or operational collapse of the carrier.

Possible carrier-side termination reasons include:

- persistent customer non-payment,
- customer failure to provide agreed minimum volume,
- unsafe or impossible operating conditions,
- loss of legal access that cannot reasonably be resolved,
- strategic withdrawal where the contract permits early exit.

Voluntary early termination without a contractual cause is possible only where the contract allows it and can trigger:

- termination fee / liquidated damages,
- repayment of bonuses or incentives where specified,
- customer relationship damage,
- relevant reputation impact,
- loss of exclusivity or preferred-carrier status.

The UI must show the expected consequences before the player confirms termination. Proportionate ordinary cancellation fees and early capacity release follow [CONTRACT_CANCELLATION.md](CONTRACT_CANCELLATION.md); its cap is not a waiver of unrelated damage or breach liabilities.

A breach should not cause an arbitrary immediate cancellation unless the contract explicitly allows it. Most long-term agreements should use escalating enforcement:

1. warning / breach notice,
2. cure period or corrective-action requirement,
3. contractual penalty,
4. possible renegotiation or temporary restriction,
5. termination if the breach remains unresolved or is severe enough.

Serious one-off failures can skip parts of this escalation where the contract clearly defines them as material breach.

The same rules apply to AI companies and customers; they cannot cancel contracts without a valid contractual or simulated reason.

### 11.9 Shipments and physical cargo lots

Use one canonical naming model. `Shipment` is a commercial consignment belonging to an optional customer contract. `CargoLot` is an independently located physical portion of that shipment. It is the sole executable cargo-batch entity; do not create a second cargo subsystem.

`TransportPlan` describes the route/responsibility chain. A contract may provide a reusable plan template; a shipment uses a versioned instance/execution plan. `PlanLeg` describes one required physical transfer. `TripAllocation` reserves a quantity of a cargo lot on a specific Trip between boarding/loading and alighting/unloading endpoints.

Suggested identities and responsibilities:

| Object | Responsibility |
|---|---|
| Shipment | Ordered quantity, origin/destination, commodity, contract, deadline, service obligations, split/delivery policy and summary |
| CargoLot | Exact quantity, physical location/carrier, current leg, quality/age, handling-unit membership and lineage |
| TransportPlan / PlanLeg | Ordered feasible endpoints, modes/operators, transfer dependencies, valid alternatives and plan version |
| TripAllocation | Lot/quantity, Trip and occupied route segments, physical capacity pool, state, reservation protection and reason codes |
| HandlingOperation | Actual loading, unloading, transshipment and quantity moved between authoritative locations |
| Capacity ledger | Segment-specific reservations for actual resources; no double-booked wagons, seats, mass, volume or handling slots |

A shipment does not permanently belong to one Trip, Line or partition. Example: 100 t uses 40 + 40 + 20 t inbound Trips, then 70 + 30 t outbound Trips after physically arriving and becoming ready at the transfer point. Keep one shipment in UI. A remaining quantity can wait without a Trip allocation.

#### Units and indivisibility

Represent cargo quantities in integer base units/fixed precision, not uncontrolled floating-point subtraction. Definitions declare the unit, mass/volume conversion, allowed split increment and any indivisible handling units. Do not universally assume 1 t is the minimum.

A pallet, vehicle, container or oversized machine can be indivisible. Commodity divisibility does not imply its current packaging can be split without a real repacking operation. Entire-shipment `do_not_split` and `deliver_together` are different contractual conditions; do not silently infer one from the other.

Loading 63 t of remaining mass capacity with a 5 t split increment admits at most 60 t, subject to volume, positions, route load and other constraints. No rounding creates or destroys cargo.

#### Physical and commercial invariants

- Every positive physical quantity has exactly one authoritative location: a facility/vehicle or an explicit handling state with precisely accounted source/destination quantities.
- A reservation changes a plan/capacity ledger, not the cargo's physical location.
- For each shipment: created quantity equals its remaining physical quantity plus accepted delivered quantity plus explicitly completed terminal dispositions, with no duplicated terminal state. Spoiled cargo awaiting disposal and cargo awaiting return are still physical inventory and consume capacity. A completed return/reclassification links the receiving inventory or return shipment and closes the original quantity exactly once; recording a write-off is not permission to erase a physical load. Production, consumption and disposal are explicit inventory transformations, not reservation edits.
- Partial delivery contributes only the accepted quantity. Full completion follows the contract's delivery policy, not the first arriving lot.
- Rebooking one part cannot cancel or reset the other parts' progress.
- A future-leg reservation may exist before arrival if backed by the predecessor plan and compatible capacity. Loading cannot occur before actual arrival, required handling and readiness.
- Do not interpret `required minus all allocations ever created` as waiting cargo. Completed/cancelled historical allocations and reservations on several legs would double-count it. Derive unreserved quantity for the selected lot/leg from live reservations against that lot's currently eligible quantity. Keep an event/audit history separately.
- Segment capacity is released after actual unloading. Cargo from A to B and cargo from B to C can reuse capacity; cargo from A to C blocks both segments.
- Different qualities, deadlines, contracts, indivisible units or custody states must not be merged in a way that loses obligations. Lots may share a visual pile or vehicle while remaining distinct records.
- Combining compatible lots never resets cargo age, spoilage exposure, cost basis or responsibility. Preserve constituent state or do not merge.
- Destination storage and transfer handling capacity are real; arriving cargo cannot disappear into a full warehouse.

Reservations must be transactional. Failed validation, duplicate clicks, save/load or two planners selecting the same capacity cannot reserve the same quantity twice. Save IDs, reservation versions and idempotency keys.

#### Allocation and execution lifecycle

The single allocation policy is defined in Section 11.0.1: physical compatibility, protected/guaranteed obligations, firm recurring/framework cargo, confirmed one-off jobs, then spot cargo. Deadline/quality urgency and stable booking order apply within a tier. No weighted profitability score or ageing rule may override protected commitments. A permanently saturated tier cannot promise starvation prevention; expose the shortfall and propose capacity or recovery.

Commercial allocation state (such as Planned, Reserved, Committed, Cancelled or Completed) is separate from physical handling/custody state (such as Waiting, Loading, Loaded, InTransit or Unloading). Replanning supersedes a versioned allocation and preserves its history; it never rewrites the lot location. Releasing an unloaded reservation requires the applicable contractual approval/recovery, but no fictional unloading operation. Cancelling a partially loaded or running allocation preserves the actual onboard quantity until physical unloading/recovery is possible. A cancelled Trip is not evidence that its load is back in storage.

Cutoff responsibility and recovery use Section 11.0.1. The lot retains its readiness state, cause/responsibility for a missed transfer and current recovery assignment; rebooking does not reset that history or release another protected commitment.

On terminal/route/Trip disruption, replan only affected lots and dependencies. Use event-driven bounded-horizon planning, cached routes, a deterministic tie-break and a material-improvement threshold to prevent allocation ping-pong.

### 11.10 Multi-leg logistics

One customer contract can contain multiple transport legs and modes.

Cargo can physically wait in storage between legs.

Example:

farm → wagon → local terminal → warehouse → regional train → hub → long-distance train → local truck → customer.

### 11.11 Perishability and special requirements

Cargo can have properties such as:

- perishability,
- temperature requirement,
- fragility,
- hazard class,
- handling requirements.

Perishable goods lose value or become unusable if delivered too slowly or without appropriate cold-chain capability.

### 11.12 Optional automatic renewal of recurring contracts

**Auto-renew** is a shared contract feature, not an infrastructure-slot-only feature. Eligible agreements expose the same simple optional checkbox, labelled **Automatically renew contract** / **Automaticky obnovovat smlouvu**.

Eligible recurring agreements can include:

- regular freight transport and recurring passenger-service contracts,
- fuel, material and other operating-supply contracts,
- recurring outsourced maintenance and service agreements,
- carrier-partnership and recurring subcontracting agreements,
- rail and station capacity agreements.

The feature applies whether the player's company buys or provides the recurring service. One-off shipments, vehicle purchases and completed construction projects do not repeat automatically. A recurring framework can renew without duplicating its completed individual orders.

Enabling the checkbox authorizes the game to arrange the next agreed term before expiry. It does not force the counterparty to accept, override the contract's renewal rights, bypass a required tender or guarantee that demand and capacity still exist. Public/municipal service contracts may renew automatically only where their agreed terms permit renewal; otherwise the next award follows the normal tender process.

Automatic renewal preserves the agreed scope, volume range, service level, exclusivity and renewal duration. Prices may change automatically only through an already accepted adjustment/indexation clause. A new price proposal, larger volume, changed route, stronger guarantee or other material change is a renewal proposal requiring the player or an appropriately authorized manager, not silent acceptance through the checkbox.

Before committing to the next term, revalidate the relevant capacity and dependencies: fleet, crew, maintenance, terminal/storage capacity, route access, licences, supply/service availability, required slots and authorized budget. Existing and newly renewed obligations must not double-book the same resources. Renewal must not promise transportation which the company cannot credibly provide.

Linked agreements remain separate commitments. Renewing a customer contract does not automatically enable renewal of its slot, fuel or subcontracting agreements. The planner checks their coverage for the next term and can coordinate already authorized renewals. Missing or unconfirmed critical coverage blocks unattended acceptance and raises a clear warning; it does not authorize extra purchases or a partially protected service behind the player's back.

For seasonal agreements, renew the next equivalent season and retain the seasonal volume/service calendar. For example, an annually recurring August–October contract renews for August–October of the following year, not for November–January or all twelve months. A continuous agreement renews for its next agreed continuous term. Renewal does not manufacture cargo, passengers or new demand.

The contract detail and overview show:

- Auto-renew on/off and whether renewal is allowed,
- the current expiry, renewal/notice deadline and proposed next term,
- agreed price or an explicitly labelled estimate under indexation,
- renewal status: scheduled, awaiting counterparty, needs approval, blocked or renewed,
- the concrete reason for a block or change, and the required action.

Routine successful renewals go into a summary; exceptions are raised before the relevant notice/renewal deadline with time to respond. Existing customer history, performance records and unresolved obligations carry forward rather than resetting on renewal.

Turning Auto-renew off prevents the next uncommitted renewal subject to the displayed notice rules. It does not cancel the active term, undo an already committed renewal or waive penalties. Failed renewal likewise does not silently terminate the current agreement; expiry, amendments and early termination still follow Sections 11.6–11.8.

The checkbox remains simple. Optional managerial approval/budget limits use the existing delegation hierarchy and manual overrides rather than a separate mandatory renewal-management system. The same renewal and capacity rules apply to AI companies. Process renewals on scheduled decision dates and relevant changes, not by scanning every contract every frame.

## 12. Storage and terminals

### 12.1 Storage

A freight-capable station can include a small integrated handling/storage allowance for minor shipments in its definition. That allowance has declared cargo compatibility, physical footprint, finite quantity/throughput and the required staff/equipment. It is not invisible unlimited storage. A passenger-only halt/platform gains no freight-handling capability or free warehouse merely by being a station.

Large volumes require physical storage infrastructure.

Examples:

- general warehouse,
- cold storage,
- coal yard,
- silos,
- tanks.

Storage has real capacity. If full, cargo must wait elsewhere, remain in vehicles or be rerouted.

### 12.2 Cargo platforms and modules

Cargo handling infrastructure is modular.

A basic freight platform may handle one cargo family.

More expensive facilities can support multiple modules, e.g. up to several cargo types.

Large logistics terminals can connect platform/track infrastructure to adjacent warehouses, tanks, silos or yards.

Specialized facilities are more efficient than universal ones.

Passenger platforms are not generic freight handling points. Freight trains may pass through compatible tracks but cannot normally perform cargo handling there.

Passenger platform function is defined by the passenger-station modules in Section 20: platform length, access, circulation and amenities affect what services the station can handle and how efficiently passengers transfer.

### 12.3 Handling time

Loading/unloading takes time based on:

- cargo,
- infrastructure,
- workforce,
- technology,
- platform/track length,
- handling equipment.

Handling improves historically with mechanization, pumps, cranes, conveyors, containers, etc.

### 12.4 Service endpoints and customer-provided facilities

Every commercial Trip/transport leg needs a **real physical service endpoint** at origin and destination.

Owning a vehicle and having a route is not enough. The vehicle must have a physically valid place where passengers/cargo can board, alight, load, unload or transfer.

A required endpoint can be supplied in one of three main ways:

1. **Customer-provided endpoint** — the customer/authority provides a usable station, stop, siding, loading dock, terminal, berth or other facility as part of the contract.
2. **Player-owned endpoint** — the player builds/owns the required station, stop, terminal, loading facility or other suitable infrastructure.
3. **Third-party access** — the player leases/rents/buys access to an existing compatible facility owned by another company, municipality, state or infrastructure owner.

The contract must make clear which endpoints are included and which are the carrier's responsibility.

Customer-provided infrastructure is not free abstract capacity. It is a real physical facility with:

- location and route connectivity;
- supported vehicle/mode/cargo type;
- loading/boarding capability;
- length/size/geometry constraints;
- operating hours where relevant;
- handling/passenger capacity;
- workforce/equipment where supplied by the customer;
- any access or usage restrictions.

A customer can therefore offer a contract such as:

> Factory A provides its private loading siding and loader. Deliver to Municipal Terminal B, with station access included in the contract.

In that case the player does not have to build those endpoints, but must still provide compatible vehicles, route/access between them and any other required resources.

A different contract may provide only the cargo/customer and require the carrier to arrange both endpoints.

For passenger/public-service contracts, an authority/customer can similarly include access to existing stops, bus stations, rail stations, tram platforms or another public terminal. A private commercial passenger service may instead require the player to own or separately secure access to suitable stops/stations.

Endpoint capacity can be a real bottleneck. A customer-provided loading point can be too small for the player's preferred train length, have insufficient handling rate or be occupied by another operator.

The Contract Planner must show each endpoint explicitly as one of:

- **Included by customer/authority**;
- **Owned by company**;
- **Third-party access secured**;
- **Access required**;
- **Construction required**;
- **Incompatible / insufficient capacity**.

The planner must not recommend a service as feasible if there is no physically valid origin/destination service point.

A customer-provided endpoint remains owned/controlled by that customer unless the contract explicitly transfers another right. Contract expiry can therefore remove the player's right to use the facility.

## 13. Transport modes

Primary modes in the wider base game, subject to the selected year and technological availability:

- road transport,
- railway,
- inland water/shipping,
- urban transport: bus, tram, trolleybus, metro.

The early horse-drawn/dostavnik startup progression and the emergence of the first railways are principally Early Ages DLC content. Horse-drawn or older technology can still appear in the base world where appropriate; starting in a later year does not unlock unavailable future modes or force all existing modes to be used by the player.

First-playable V1 implements rail and road freight/passengers, including intercity and local buses. Water, tram, trolleybus and metro operation remain later base-game scope. Aircraft are explicitly out of current scope.

### 13.1 Roads

Road capacity is simpler than rail slotting.

Vehicles need physical/legal access and are affected by congestion, surface quality, weather and restrictions.

Roads may be public, municipal, state-owned or private/tolled.

### 13.2 Railways

Rail is capacity- and geometry-constrained.

Track is divided into meaningful operational sections between stations/junctions rather than tiny segments.

Each section has practical capacity influenced by:

- number of tracks,
- signalling,
- passing loops,
- speeds,
- traffic mix,
- technology,
- section-level track direction configuration.

Directionality is therefore not a whole-line property. Each physical track in each meaningful section can have its own preferred/bidirectional/one-way operating rule under Section 32.3.

The player normally requests service capacity, not exact second-by-second paths or a permanently assigned physical track.

A contracted rail slot protects movement capacity through the relevant section/corridor and operating window. Detailed track choice inside that infrastructure is dynamic under Section 32.3.

Possible capacity products:

- guaranteed,
- standard,
- flexible.

Once infrastructure capacity has been sold/reserved, operational priority follows the **contracted slot/access class**, not asset ownership.

A private owner may reserve capacity for its own trains before selling the remainder, but after third-party capacity is contracted the owner cannot arbitrarily push its own lower-priority trains ahead of a competitor that holds a higher-priority or guaranteed slot.

During normal disruption/recovery, dispatching prioritizes according to:

- guaranteed/standard/flexible access class,
- the specific time window and contractual rights,
- operational safety,
- recovery rules defined in the access agreement.

Ownership of the track is not itself a tie-breaker after capacity has been contractually allocated.

If the owner wants higher priority for its own trains, it must reserve that capacity for itself in advance under the same capacity accounting.

Reserved rail capacity has a defined **tolerance window** around the contracted operating time.

The width of that window is **not a universal fixed value**. It is calculated/offered per movement or service pattern from the characteristics of the service.

Relevant inputs can include:

- passenger versus freight service;
- access/service class;
- train length and weight;
- acceleration/braking and expected speed profile;
- cargo type and amount;
- expected loading/unloading work;
- passenger boarding/alighting volume where relevant;
- shunting or locomotive-exchange requirements;
- expected dwell/turnaround variability;
- infrastructure/signalling characteristics;
- congestion and available scheduling margin;
- historically appropriate operating/dispatch technology.

A short, high-frequency passenger service can therefore receive a tighter slot window than a heavy mixed freight service with variable handling.

The system must distinguish **slot-window width** from **actual infrastructure occupancy time**.

- The slot window describes when the movement may validly arrive/depart/enter while retaining its contracted protection.
- Occupancy time describes how long the train physically blocks/uses a section, junction, track or platform once it is there.

A long/heavy train can therefore both need a broader timing window **and** occupy infrastructure longer, but one does not mechanically equal the other.

A wider **guaranteed** slot can be more expensive or consume more sellable scheduling flexibility because the infrastructure owner must protect a larger operating margin. A flexible/ad-hoc product can offer a broad possible time range without the same protection, so window width alone does not determine price/priority.

If a Trip misses its slot beyond that window because of the operator's own delay, it loses its guaranteed priority for that occurrence and becomes an out-of-slot train. Dispatching then fits it into the nearest compatible spare capacity without displacing trains that are still inside their valid contracted windows.

The access agreement can define:

- slot start/end or target time,
- early/late tolerance,
- what priority applies after the tolerance is exceeded,
- whether an out-of-slot movement pays an additional fee,
- any cancellation/no-show rule for severely late services.

Rail-capacity slots are **non-transferable between operators**. The holder cannot resell, lease or privately assign the slot to another carrier.

If the holder no longer needs the capacity, it can release it back to the infrastructure owner according to the access agreement. The owner may then allocate or sell that capacity again through the normal process.

The cause of delay matters. If the Trip misses the slot primarily because the infrastructure/station owner failed to provide previously contracted capacity or because of another protected infrastructure-side disruption covered by the agreement, the operator should not automatically lose its contractual protection. The agreement can instead preserve priority, rebook the slot or trigger compensation.

The UI must show whether a late Trip is still **inside tolerance**, **out of slot**, or **reprotected due to infrastructure-side disruption**.

Capacity reservations can be **permanent/long-running or time-limited**. A carrier may reserve capacity only for a defined period such as:

- harvest season,
- summer/winter timetable,
- a few months for a temporary large contract,
- a holiday/peak period,
- a temporary replacement service.

The reservation validity can mirror the Service Pattern calendar, including date range, selected weekdays and time windows. When the validity expires, the capacity returns automatically to the infrastructure owner unless a renewal has been agreed.

Capacity agreements use the shared **Auto-renew** checkbox and rules in Section 11.12. Before renewal, the infrastructure owner must still offer the requested capacity, the slot pattern must match the intended Service Pattern, and the next validity period must pass the same finite-capacity checks as a new reservation.

Renewal preserves the agreed seasonal/date pattern, access class and tolerance unless a change is explicitly approved. Price changes follow the already agreed indexation rules; other material changes or refusals pause unattended renewal and trigger a warning before expiry. Auto-renewal does not create capacity, displace another operator's valid rights or make slots transferable.

### 13.2.1 Capacity order editor

The player should normally obtain rail and station capacity through a simple **Capacity Order** workflow launched directly from a Line or Service Pattern.

The same workflow can be launched from the Contract Planner when a proposed contract solution requires new rail/station capacity. The Contract Planner supplies the proposed route, service dates and operating requirement; the Capacity Order remains a separate agreement and still requires explicit player approval.

The player should not manually buy dozens of disconnected section and station slots one by one.

The editor pre-fills the request from the selected Service Pattern:

- route and infrastructure owners,
- stations/terminals used,
- operating days,
- requested frequency/interval or broad departure windows;
- optional preferred/anchor times;
- validity date range,
- train length/type,
- expected leg running times;
- expected dwell/turnaround;
- service/consist/cargo characteristics used to derive appropriate slot-window widths;
- required direction on each section,
- number of calls/movements generated by the pattern.

The Capacity Order returns compatible **time windows** for the required route and station calls. The Line Planner then constructs the actual published/planned timetable from those accepted windows under Section 32.2, using the midpoint of each arrival/departure slot as the planned time.

The normal player workflow is:

1. **Choose validity** — use the Service Pattern calendar or override with a temporary/seasonal date range.
2. **Choose service level** — guaranteed, standard or flexible/ad-hoc where offered. The UI can recommend a stronger product for a High operational-priority Pattern, but the player must explicitly buy it.
3. **Review tolerance** — normally use recommended tolerance; advanced adjustment is optional if the owner offers alternatives.
4. **Choose renewal** — simple **Auto-renew** checkbox for recurring/long-running capacity agreements.
5. **Review capacity result and price** — then submit/accept the capacity order.

The system automatically expands one request into all required infrastructure rights along the route, including both:

- line-section capacity,
- station-call capacity.

The result is presented as one understandable order summary rather than a list of raw signalling blocks.

The order screen should show:

- requested Service Pattern,
- validity period and days,
- Auto-renew on/off,
- requested calls/movements per time window,
- accepted/proposed arrival and departure slot windows at relevant stations;
- reason/inputs behind unusually tight or wide windows where material;
- resulting planned midpoint times;
- expected physical occupancy/dwell time separately from the window width;
- capacity availability for every required section/station,
- total reservation fee,
- expected per-use charges,
- owners involved,
- any missing connection/access agreement,
- any incompatible infrastructure,
- any time window that cannot be supplied,
- expected congestion/tolerance risk.

Capacity availability should use a simple visual timeline/heatmap with states such as:

- available,
- tight,
- unavailable,
- owner refused access.

If the exact requested pattern cannot be supplied, the editor should offer concrete alternatives rather than forcing manual reconstruction, for example:

- shift the pattern by +12 minutes,
- use a nearby off-peak window,
- downgrade selected movements to flexible access,
- reduce frequency,
- use an alternative station/route where physically valid.

A **Find nearest available capacity** action can search around the requested timetable and propose the smallest practical shift that makes the complete route feasible.

For routes crossing several infrastructure owners, the capacity order acts as a coordinated request. It can return a mixed result such as two accepted owners and one refusal. The Service Pattern is not considered fully protected until all required capacity has been obtained.

The player can inspect the detailed section/station breakdown when desired, but the default workflow stays at Service Pattern level.

Capacity orders are not tradable assets. If the player reduces/cancels the Service Pattern, unused capacity can only be released back to the relevant infrastructure owner under the existing agreement.

The same high-level capacity philosophy is used for constrained passenger stations: operators buy/reserve station-call slots against finite station capacity, then the station dynamically assigns the actual compatible platform for each Trip. Station-slot capacity and line-section capacity remain separate constraints and both must be available.

Real train movement still uses local section/block reservations. A train reserves only near-future sections, not its entire route. The exact track/block sequence can change dynamically under Section 32.3 as occupancy and disruption evolve, while respecting the Trip's access rights and protected capacity.

### 13.3 Water

Open navigable water does not use railway-style path slots.

Gameplay focuses on:

- licences/access rights,
- ports,
- locks,
- canals,
- bottlenecks,
- water depth,
- terminal capacity.

The player can build canals and modify waterways, subject to cost, technology and permission.

## 14. Rail operations and rolling stock

### 14.1 Physical train composition and shunting

Every locomotive and wagon is an individual asset.

Trains are physically assembled and disassembled on real track.

A consist cannot be changed through a menu without the required physical movements.

Moving wagons between sidings, platforms, loading tracks, storage tracks and assembled consists requires real **shunting movements**.

Shunting can be performed by:

- a dedicated shunting locomotive/vehicle,
- a normal line locomotive temporarily taken away from line work,
- period-appropriate simpler methods in very early/small facilities where plausible.

Dedicated shunters are physical fleet assets with their own location, fuel/energy use, maintenance state and parking requirement.

The player does not need to micromanage every coupling action by default. A yard/dispatcher can generate and execute the necessary shunting plan automatically, but the locomotives, wagons, tracks and movements must still physically exist.

### 14.2 Direction and turning

Vehicles respect directionality.

Keep **physical facing**, **permitted travel direction** and **position in the consist** separate. A steam locomotive may run backwards only when that model and operation permit it, with the defined speed/visibility/route limits. It never flips its model or orientation by changing a timetable direction.

A run-around moves a locomotive to the other end of the consist but does **not** turn the locomotive's physical facing. A turntable or reversing triangle turns it through real movement. These are not interchangeable capabilities.

A terminal solution can use a valid run-around plus permitted reverse running, actual turning facilities, a second suitably positioned locomotive, or later bidirectional equipment. Feasibility checks the complete combination, including track access, coupling/control and resulting performance. Section 16.3 applies the same distinctions to rescue/backing movements.

### 14.3 Train feasibility

Before dispatch, the game calculates whether a consist can physically operate the planned route based on:

- total weight;
- total length;
- axle/load limits;
- locomotive power and tractive effort;
- acceleration/braking performance where relevant;
- gradients;
- curvature/geometry restrictions;
- electrification/traction system;
- permitted speed;
- station/platform length;
- other infrastructure compatibility.

The player should not discover a predictable traction, length or load problem only after the train has departed.

For criteria-based consists under Section 32.6, these calculations also define the Pattern's **operating envelope**. The dispatcher may select any real consist inside that envelope but cannot substitute one that invalidates the planned running time, platform fit or reserved slot assumptions.

Heavy trains may need helpers/bank engines on specific sections. A helper requirement is part of feasibility and must be represented by real available traction, not an abstract performance bonus.

### 14.4 Locomotive exchange and local traction bases

A long-distance Service Pattern may change locomotives en route, but a locomotive exchange should only exist where it is operationally justified by **local traction availability**.

Typical valid reasons include:

- electrified section changing to non-electrified section,
- incompatible electrification system,
- major traction/performance requirement change,
- route-specific technical or regulatory compatibility,
- historically plausible operating practice where a local traction base serves a distinct corridor.

A planned exchange point must have a suitable **local operating/dispatch depot or traction base** with compatible locomotives physically available for that onward segment, or another equivalent nearby facility that can realistically stage them.

The planner should not recommend an exchange where both locomotives would have to deadhead from the same distant depot just to swap places. In that case the exchange normally adds pointless movements and should be rejected unless another explicit operational constraint makes it necessary.

For a planned exchange, the local onward locomotive is normally staged from its own nearby depot/pool. The incoming locomotive is then:

- sent to local parking/service,
- reassigned to another local Trip,
- or later returned through useful work/repositioning.

The locomotive exchange is a physical station/yard operation:

1. train arrives on a suitable track;
2. incoming locomotive uncouples and physically clears the consist;
3. onward locomotive physically approaches and couples;
4. required checks/preparation occur;
5. the Trip continues.

The exchange consumes real track/yard capacity and adds dwell time.

The Service Pattern planner can automatically suggest valid exchange points only when all of the following are true:

- onward traction is actually required or materially advantageous,
- the station/yard geometry supports the operation,
- a suitable local traction base exists,
- the regional pool can credibly provide the required onward locomotive,
- the added dwell and shunting capacity are accounted for.

If no valid local traction base exists, the system should normally recommend one of:

- use a locomotive capable of the entire route,
- build/establish a **small standalone traction base** at a suitable point,
- upgrade an existing parking/operating facility with traction-base modules,
- change the route,
- shorten the service,
- use another compatible traction solution.

Later technologies such as multi-system, dual-mode or otherwise more versatile vehicles can remove exchange points and thereby reduce dwell time, fleet complexity and station capacity usage.

### 14.5 Passenger classes, comfort and reservation policy

Rail can offer different classes from early periods.

Over time the player can add comfort/service features such as:

- improved seating,
- heating,
- lighting,
- toilets,
- dining,
- sleeping accommodation,
- air conditioning,
- service/baggage functions.

Comfort expectations rise over time.

Vehicle comfort contributes to the separate **Comfort** factor in Section 6.2. Actual cleaning/turnaround history contributes separately to **Cleanliness**, and occupancy contributes separately to **Crowding**. Do not merge all passenger-service effects into one hidden vehicle-quality score.

A retrofit can extend usefulness, but cannot make a fundamentally obsolete vehicle equal to a modern one.

Availability is evaluated against the selected start year and region. Do not gate an already established historical feature behind replaying its earlier invention solely because a new company was founded in 1925, 1950 or 1975; compatible vehicles and installed equipment are still required.

#### Passenger-capacity zones

Passenger capacity is tracked in **capacity zones** rather than as individually simulated seat numbers.

A capacity zone can correspond to:

- a whole passenger coach;
- one class/section inside a coach;
- a sleeping-car/accommodation category;
- a bus/coach seating class;
- another physically distinct passenger-capacity area.

A zone stores the relevant usable capacity, for example:

- seated places;
- standing places where permitted;
- sleeper/berth places;
- class/comfort level;
- accessibility/special-service capacity.

Capacity is accounted for **per travel leg between commercial stops**. A passenger Praha→Pardubice releases that capacity for later legs after Pardubice.

The game does not need to assign or render seat numbers such as "Coach 3, Seat 42" unless a future feature explicitly requires them.

#### Reservation policy per zone

Each passenger-capacity zone can use one of three reservation policies:

1. **Open boarding** — no reservation is required; passengers board from available physical capacity.
2. **Optional reservation** — capacity can be sold/reserved in advance, while remaining capacity can still be sold to walk-up passengers.
3. **Reservation required** — the passenger must hold confirmed capacity for that zone/Trip/leg before boarding.

The policy can be configured at Line/Service Pattern level and inherited by the consist, with an override for individual vehicle/coach/capacity zones.

Example:

> Coach 1 — First Class — **Reservation required**  
> Coaches 2–4 — Second Class — **Optional reservation**  
> Coach 5 — Regional/open section — **Open boarding**

This allows the player to create differentiated products without defining a separate Line for every passenger class.

A reservation-required zone does **not** necessarily mean the ticket must be purchased days in advance. If sales systems, station facilities and cutoff rules permit, a walk-up passenger can still purchase the remaining capacity shortly before departure; the system simply creates a confirmed reservation before boarding.

#### Seated versus standing capacity

Passenger standing capacity is defined **on the individual vehicle / passenger-capacity zone**, not as one Line-wide abstract percentage.

Each applicable coach, bus, tram car, trainset section or other passenger zone can define:

- seated/berth capacity;
- standing capacity where legally/physically permitted;
- total usable physical occupancy.

Standing capacity can therefore differ between vehicles in the same consist.

Examples:

> Coach 1 — 54 seats / 0 standing  
> Coach 2 — 72 seats / 18 standing  
> Coach 3 — 72 seats / 18 standing

Advance/reserved intercity capacity is normally tied to **seated or berth capacity**, not standing capacity.

Standing capacity is mainly appropriate for:

- urban transport;
- suburban/regional services;
- vehicle types and eras where standing travel is permitted.

A passenger with a confirmed reserved seat/berth is guaranteed the corresponding capacity class unless a disruption forces re-accommodation.

Open-boarding passengers can use standing capacity where the actual vehicle/zone permits it.

Standing is not a separate hidden penalty system.

Once occupancy exceeds available seated capacity in a zone and passengers begin standing, the affected zone's passenger experience worsens through the existing transparent factors:

- **Crowding** increases;
- **Comfort** decreases for passengers exposed to that standing/crowding condition.

The effect is calculated only for the affected vehicle/zone and travel leg rather than automatically penalizing the whole consist.

Crowding is evaluated **per commercial leg between stops**.

Example:

> Praha → Kolín  
> Coach 2: 72 seats / 18 standing  
> Occupancy: 84  
> → 12 standing passengers; elevated Crowding and reduced Comfort in Coach 2

> Kolín → Pardubice  
> Occupancy drops to 66  
> → all passengers can be seated; standing penalty ends for that leg

The duration/distance of the crowded portion matters to passenger choice and experience.

A short standing segment can be acceptable for many urban/suburban passengers, while prolonged standing has a larger negative effect.

Different passenger segments and service types can therefore tolerate standing differently, but the underlying reason remains visible:

- whether standing occurred;
- how many passengers were affected;
- on which vehicle/zone;
- for how much of the journey.

#### Simplified distribution across coaches/zones

Passenger allocation inside one compatible consist is deliberately simplified.

The system automatically distributes passengers as evenly as practical across **compatible passenger-capacity zones**, while respecting hard product constraints such as:

- passenger class;
- reservation-required capacity;
- accessibility requirements;
- sleeper/berth or other special accommodation;
- zones where standing is or is not permitted.

It does **not** simulate detailed passenger preference for the first/last coach, platform entrance location, stair position or individual walking decisions along the platform.

For ordinary unreserved passengers in equivalent coaches, the allocator should prefer balancing occupancy so that one compatible coach is not heavily overcrowded while another equivalent coach remains mostly empty.

Example:

> 3 equivalent Second Class coaches  
> 210 passengers total  
> → approximately 70 passengers per coach rather than 110 / 70 / 30

Small differences can arise from reservations, different capacities or special zones, but not from a separate detailed boarding-behaviour simulation.

This simplification keeps per-vehicle crowding and comfort meaningful without introducing unnecessary passenger pathfinding/micromanagement.

No separate opaque "overcrowding score" should be applied on top of these factors.

If total seated + permitted standing capacity is full, additional open-boarding passengers cannot board that zone/vehicle and follow the normal denied-boarding/alternative-service logic.

The UI must distinguish:

- reserved seated/berth capacity;
- unreserved seated capacity;
- standing capacity;
- passengers currently standing;
- total physical occupancy.

#### Disruption and consist changes

Reservations attach to a **capacity category/zone requirement**, not to one immutable physical seat.

If a coach is substituted, removed or replaced, the dispatcher/passenger system tries to preserve:

- class;
- seated/berth guarantee;
- accessibility requirement;
- relevant comfort/service requirement.

If replacement capacity is insufficient, affected passengers require re-accommodation, rebooking, upgrade/downgrade compensation or another service according to the passenger policy.

A consist change must therefore revalidate reserved passenger capacity before dispatch rather than silently overbooking the train.

#### Onboard staff circulation

Passenger coaches can differ in whether onboard staff can physically move through the passenger accommodation **while the train is running**.

Keep this as a simple vehicle capability rather than a detailed walking simulation:

- **Through-circulation available** — staff can move through the relevant coach/consist internally while running. Normal onboard ticket sale/control does not add station dwell.
- **No through-circulation** — typical of older non-corridor compartment stock with direct exterior access to separate compartments. Staff cannot practically service every compartment internally while the train is moving.

For non-through-circulation stock, onboard ticket sale/control can require additional station-stop work when passengers rely on the conductor rather than pre-purchase.

The extra time is calculated in aggregate from the relevant boarding/ticketing demand and coach layout. The game does not simulate the conductor visiting each door individually.

If passengers already hold valid tickets from station/branch/pre-sale channels, no artificial ticketing dwell is added merely because the coach is non-through.

In a mixed consist, only the passenger capacity that onboard staff cannot reach internally is subject to this limitation.

This vehicle capability can therefore make older stock operationally distinct without adding a separate ticket-inspection minigame.

## 15. Vehicle lifecycle

### 15.1 Vehicle Marketplace

Vehicle acquisition is handled through a shared **Vehicle Marketplace** rather than disconnected purchase menus.

The marketplace has four primary acquisition sources:

1. **Manufacturer order** — order a newly built vehicle directly from a manufacturer.
2. **Dealer stock** — buy a brand-new vehicle that a dealer already has physically in stock.
3. **Used market** — buy a concrete existing vehicle from another owner/seller.
4. **Lease / rental** — obtain use of a vehicle for a defined period without buying it outright.

The same underlying vehicle definitions and compatibility rules apply regardless of acquisition source.

The marketplace supports filters/sorting appropriate to the selected mode and era, such as:

- road / rail / urban / water vehicle type;
- passenger / cargo role;
- cargo compatibility;
- traction / fuel / power system;
- capacity;
- power/tractive effort where relevant;
- maximum speed;
- dimensions / axle load / route compatibility;
- comfort/service class;
- purchase price;
- lease price;
- estimated operating cost;
- delivery/readiness date;
- manufacturer/model;
- new/used/dealer/lease source;
- physical location;
- used-vehicle age, mileage/hours and condition;
- current maintenance/inspection margin and known next required service.

When opened from a Contract Planner, Line planner or another requirement screen, the marketplace can inherit filters such as "show compatible vehicles for this route/contract". The player can clear or modify those filters.

A vehicle listing/order must make the acquisition timeline visible. **Available** never means the asset can teleport into service.

### 15.2 Manufacturer orders

Vehicle manufacturers are real economic firms in the world, but simulated at a calmer level than transport operators.

They have:

- factories,
- material demand,
- workforce,
- production capacity,
- order backlog,
- expansion potential.

Vehicles use fictional manufacturers/models inspired by real historical technology, not real trademarks.

A direct manufacturer order is normally the cheapest way to obtain a **new** vehicle of a current model, but it has a production lead time.

New vehicles are ordered and physically produced over time. Production lead times depend on:

- factory capacity,
- current backlog,
- model complexity,
- input/material availability,
- ordered quantity,
- historically appropriate production technology.

An order for several vehicles consumes real manufacturer capacity. Large orders can be completed/delivered in batches rather than all units appearing simultaneously.

Where the model supports configurable factory options, manufacturer orders can offer more configuration flexibility than dealer-stock vehicles.

The order UI should show:

- unit price,
- quantity,
- configuration,
- current production estimate,
- expected first/last unit completion,
- known backlog/material risks,
- delivery/import method and estimated readiness at the player's receiving point.

A production estimate can move when the manufacturer's real supply/capacity situation changes, but material delays should be explained rather than silently changing a date.

### 15.3 Dealers and immediately available new stock

Vehicle dealers/distributors are commercial entities that can purchase new vehicles from manufacturers and hold a limited number as **physical dealer stock**.

Dealer stock provides a deliberate trade-off:

- vehicle is already manufactured;
- quantity is limited to the dealer's actual inventory;
- price is higher than a normal factory order because of dealer margin/scarcity;
- purchase can be completed immediately without waiting for manufacturing;
- physical delivery/collection still takes real time.

Example: a company that urgently needs two trucks for a new contract can buy two dealer-stock units at a premium instead of waiting for a cheaper factory order.

Dealer inventory is finite. If a dealer has three compatible vehicles, the player cannot buy ten from stock.

Dealer stock can include:

- common/high-demand configurations of current models;
- demonstrator/pre-registered vehicles where appropriate;
- stock from multiple manufacturers represented by that dealer.

Highly customized or unusual specifications normally require a manufacturer order rather than being guaranteed in dealer inventory.

Dealer pricing can depend on:

- manufacturer/list price,
- local demand,
- stock scarcity,
- age of stock,
- delivery/import cost,
- dealer markup.

Dealer stock does not spawn on demand for the player. Dealers replenish by ordering from manufacturers, so factory shortages/backlogs can later reduce dealer availability.

Dealer-stock vehicles have a physical dealer location or defined import/delivery point. Purchase transfers ownership immediately, but the vehicle becomes operational only after it physically reaches a compatible receiving/operating location.

Delivery can use, where appropriate:

- player collection,
- dealer-arranged delivery,
- contracted transport,
- player's own transport,
- rail movement/towing for compatible rolling stock.

### 15.4 Vehicle maintenance policy, workshops and service contracts

Vehicle maintenance has two distinct layers:

1. **Hard maintenance / inspection requirements** — legal, safety, manufacturer or technical limits that cannot be exceeded.
2. **Preventive maintenance policy** — the player's chosen margin for how early the company normally services vehicles before those hard limits.

#### Maintenance policy hierarchy

The company defines a default **maintenance policy** for its fleet.

The player can override that default for:

- a fleet group;
- a vehicle type/model;
- a specific exceptional vehicle where needed.

Inheritance works from company default downward. The UI must always show whether a policy is inherited or manually overridden.

The policy is expressed through understandable operating choices rather than hidden reliability modifiers.

Relevant settings can include:

- target service point as a percentage of the allowed interval;
- minimum remaining mileage/hours/calendar time before assigning a long Trip;
- preferred workshop/service provider;
- whether planned maintenance may be advanced to fill an available workshop window;
- how far routine preventive maintenance may be deferred when operationally necessary;
- minimum post-service reserve expected before returning the vehicle to intensive work.

Example:

> Company default: service at ~80% of allowed interval  
> Heavy road fleet override: ~75%  
> Heritage rail fleet override: ~65%

A more conservative policy:

- sends vehicles to maintenance earlier;
- consumes more workshop capacity and fleet downtime;
- requires more spare fleet;
- reduces the probability that wear-related defects become operational failures.

A more aggressive policy:

- keeps vehicles in revenue service longer;
- reduces planned downtime in the short term;
- operates closer to hard limits;
- increases the chance that defects or unscheduled repairs disrupt service.

The effect must come from vehicle condition, wear and maintenance state rather than an arbitrary company-wide reliability bonus.

#### Hard maintenance and inspection limits

Some maintenance actions are mandatory.

A vehicle can have hard limits based on, where relevant:

- calendar time;
- mileage/distance;
- operating hours;
- engine/traction hours;
- inspection cycles;
- component-specific limits;
- legal/regulatory inspection dates;
- manufacturer/service requirements.

The simulation can use a combination of these without forcing the player to manage every component individually.

Once a hard safety/legal limit is reached, the vehicle becomes **not dispatchable** for normal commercial service until the required maintenance/inspection is completed.

The player cannot override this through a disruption policy.

The planner should warn well before a hard limit would collide with committed Trips.

#### Maintenance scheduling

Planned maintenance is integrated into normal fleet scheduling.

The maintenance planner looks for suitable windows between Trips and considers:

- remaining interval before the target service point;
- hard deadline;
- physical vehicle location;
- travel/repositioning time to the workshop;
- workshop compatibility;
- available workshop slots/capacity;
- estimated service duration;
- parts/material availability where relevant;
- future Trip commitments;
- fleet reserve;
- return/repositioning time after service.

A vehicle is therefore not merely marked unavailable for an abstract number of hours. It must physically reach a compatible workshop, occupy real capacity, complete the work and return or reposition for its next assignment.

The planner can advance routine maintenance when an otherwise idle period creates a useful service window.

It can also defer preventive maintenance toward the hard limit when the player's policy permits, but it cannot schedule work beyond a mandatory limit.

Example:

> Locomotive #104  
> Preventive target: 12,000 km  
> Current: 11,240 km  
> Hard limit: 14,000 km  
> Free workshop window tomorrow 02:00–07:00  
> Next heavy assignment would add 1,900 km  
> → planner recommends servicing tomorrow before that assignment

#### Interaction with Service Patterns and fleet assignment

Fleet availability shown in the Line Planner must account for planned maintenance.

A vehicle that is technically owned but committed to a workshop is not spare fleet.

Criteria-based assignment should prefer vehicles whose remaining maintenance margin is compatible with the planned duty.

The dispatcher must not assign a vehicle to a duty that would predictably cross a hard inspection/maintenance limit before a valid service opportunity exists.

For pinned vehicles, the planner must warn if their maintenance schedule conflicts with the Pattern and can invoke the configured substitution/disruption rules where allowed.

Maintenance therefore participates in the same readiness calculations as:

- vehicle location;
- preparation horizon;
- fleet reserve;
- depot/parking requirements;
- Trip commitments.

#### Unscheduled defects and breakdown risk

Maintenance policy influences the probability of wear-related unscheduled defects, but failures must remain probabilistic rather than guaranteed at a simple percentage threshold.

Risk can depend on:

- vehicle age;
- accumulated use;
- current condition;
- maintenance history;
- quality/timeliness of servicing;
- operating severity;
- historical technology/reliability;
- known model characteristics where appropriate.

A recently maintained vehicle can still fail, and a vehicle close to its service target does not automatically break.

When a defect affects an upcoming Trip, the day-of-operation disruption policy in Section 32.6 determines whether the operator substitutes equipment, waits, runs reduced, rebuilds the consist or cancels.

#### In-service breakdowns

Breakdowns that occur **during a running Trip** use a deliberately simple operational model.

The game does not expose dozens of technical failure states to the player. Each defect is resolved into one of four practical outcomes:

1. **Continue to destination** — the vehicle can safely complete the current Trip, possibly with reduced comfort/service, but must be inspected/repaired afterwards.
2. **Continue with restriction** — the vehicle can continue only with a clear operating restriction such as reduced speed/power. The Trip continues, but delay/slot/connection consequences are recalculated.
3. **Next suitable stop only** — the vehicle may move only as far as the next suitable station/terminal/safe operating point, where the Trip must be terminated or recovery performed.
4. **Immobilized / immediate stop** — the vehicle cannot continue under its own normal operation and requires rescue, towing, replacement traction, roadside assistance or another physical recovery action.

The exact technical defect determines which of these outcomes is safe and legal. Player policy cannot override that boundary.

A **suitable stop** is not automatically the next commercial stop. It must be a place where the affected vehicle/consist can realistically be handled, for example:

- sufficient track/platform/roadside space;
- ability to unload passengers/cargo safely;
- shunting/turnaround capability where required;
- access for a replacement locomotive/vehicle;
- workshop/depot/recovery access where relevant.

For rail, failures can affect only part of the consist.

Examples:

- locomotive failure while coaches remain usable → replacement/rescue locomotive can take over;
- one coach becomes unfit for further service → reach a suitable station, detach it where physically possible, then continue with reduced capacity;
- minor passenger-service defect → finish Trip, then repair;
- major traction/safety defect → stop or reach only the next suitable point.

Recovery remains physical. A rescue locomotive, tow vehicle or replacement vehicle must actually travel from where it is available; it cannot appear instantly.

If a stopped vehicle blocks real infrastructure, that blockage affects other traffic until the asset is moved or the infrastructure is cleared.

After the operational outcome is known, passenger/cargo consequences are handled separately through the existing systems:

- delay and missed connections;
- rebooking/re-accommodation;
- refunds;
- compensation;
- cargo recovery/SLA consequences.

This keeps breakdown gameplay deep enough to create meaningful disruptions without turning vehicle failures into a component-by-component engineering simulator.

#### Maintenance capacity and reserve fleet

The planner should expose the operational trade-off between workshop policy and spare fleet.

**Maintenance demand and fleet reserve are separate concepts.**

Vehicles already expected to be unavailable because of planned maintenance, inspection, repair, delivery/repositioning or another committed duty do not count as operational reserve during that period.

Example:

> Fleet: 20 buses  
> Peak scheduled requirement: 17  
> Normal maintenance demand: 1  
> Other committed/unavailable: 0  
> Effective operational reserve: 2 buses

If the player runs a very conservative maintenance policy with too little fleet reserve or workshop capacity, the company can create its own recurring availability shortage.

Likewise, aggressive maintenance deferral can temporarily increase available fleet but create more unscheduled failures and hard-deadline conflicts later.

Managers can recommend changes, but explicit player policy remains authoritative.

#### Fleet reserve policy

The player can define a target **fleet reserve** so normal scheduling deliberately preserves enough compatible vehicles/rolling stock for breakdowns, short-notice substitution, maintenance overruns and other disruption.

The policy hierarchy is:

1. **Company default**;
2. **vehicle category / fleet group override**;
3. **Service Pattern override** where a particular service needs a different protection level.

The UI must show whether the effective reserve target is inherited or overridden.

Reserve can be expressed as:

- a percentage above the relevant planned peak requirement;
- an absolute number of compatible vehicles/assets;
- for rail rolling stock, a suitable combination by functional category where needed.

Examples:

> Road coach fleet  
> Planned peak requirement: 20  
> Reserve target: 10%  
> Target reserve: 2 compatible coaches

> Mainline locomotives  
> Planned peak requirement: 8  
> Reserve target: 1 locomotive

> Sleeper cars  
> Planned peak requirement: 5  
> Reserve target: 1 compatible sleeper

A reserve target is based on **compatible operational capacity**, not only raw vehicle count.

A spare locomotive that cannot operate the relevant traction system or a spare coach that lacks a required passenger product does not satisfy that reserve requirement.

##### Reserve is protected headroom, not permanently idle stock

Fleet reserve is not a list of vehicles that must sit unused forever.

A nominal reserve asset may perform:

- another short Trip;
- repositioning;
- light secondary work;
- maintenance preparation;
- another compatible duty;

as long as the planner still expects the configured reserve to be available when required and does not jeopardize known future commitments.

The dispatcher therefore protects **availability headroom**, not fixed serial numbers, unless the player explicitly pins a particular spare asset.

Routine timetable planning should not consume the reserve below its target without warning.

The player can still deliberately operate below target. The game should show this as an operational risk rather than prevent it with an arbitrary hard block unless a contract/regulation specifically requires reserved capacity.

##### Effective reserve calculation

For a compatibility pool and planning window, the system calculates approximately:

> compatible fleet  
> − scheduled operating requirement  
> − planned maintenance/inspection/repair unavailability  
> − delivery/repositioning and other committed duties  
> = effective operational reserve

The resulting reserve is compared with the configured target.

Because rail fleets contain different functional assets, reserve is checked separately where necessary, for example:

- locomotives/traction;
- passenger coach classes/types;
- sleeper/dining/special-service coaches;
- freight wagon families;
- trainsets.

The system should not claim that excess ordinary Second Class coaches compensate for having no spare locomotive.

##### Interaction with disruption recovery

When a vehicle fails shortly before a Trip, the day-of-operation disruption policy in Section 32.6 normally checks compatible reserve capacity first when substitution is permitted.

Using reserve for a failure can temporarily push the company below its target.

That is allowed, but the planner then exposes the reduced protection for subsequent Trips until:

- the failed asset returns;
- another compatible asset becomes free;
- maintenance completes;
- the company acquires/leases additional capacity;
- or the timetable requirement falls.

A reserve is therefore a resilience policy, not guaranteed immunity from multiple simultaneous failures.

##### Pattern-specific reserve protection

A Service Pattern can override the inherited company/fleet reserve target when justified.

Examples:

- a premium intercity service keeps a stronger locomotive/coach reserve;
- a remote bus operation keeps one compatible backup vehicle;
- a low-priority seasonal freight service accepts almost no dedicated reserve.

The override affects planning protection for that service but does not create new vehicles.

If several Patterns depend on the same compatibility pool, the fleet planner reconciles their reserve requirements and must not double-count the same spare asset as independently guaranteed to multiple simultaneous failures.

##### UI and planning feedback

Fleet and Line planners should show, for the relevant planning window:

- total compatible fleet;
- scheduled requirement;
- known maintenance/repair unavailability;
- other committed duties;
- configured reserve target;
- effective reserve;
- reserve shortfall/surplus.

Example:

> Compatible buses: 24  
> Peak scheduled: 20  
> Planned maintenance: 2  
> Other unavailable: 0  
> Target reserve: 2  
> Effective reserve: 2  
> **Reserve status: met**

or:

> Compatible locomotives: 10  
> Peak scheduled: 8  
> Planned maintenance: 1  
> Target reserve: 2  
> Effective reserve: 1  
> **Reserve shortfall: 1 locomotive**

Managers can recommend a higher/lower reserve target, acquisition/lease or timetable adjustment, but explicit player policy remains authoritative.

#### Own and external maintenance

Maintenance can be performed by:

- the player's own compatible workshop;
- a dealer/authorized service provider;
- another compatible third-party workshop;
- another party responsible under a lease/service agreement.

The same maintenance policy applies regardless of provider. Outsourcing changes cost, travel time, booking priority and available capacity; it does not remove the physical maintenance requirement.

Some dealers can also operate or contract **authorized service/workshop capacity** for the vehicle types/brands they represent.

The player can therefore buy a vehicle from a dealer and separately order maintenance/services from the same dealer where offered.

Dealer service can include:

- pre-delivery inspection/preparation;
- warranty work;
- scheduled routine maintenance;
- repairs;
- diagnostics;
- manufacturer/dealer-approved retrofits;
- recalls/service campaigns where relevant;
- pickup/delivery or transport coordination where offered.

Dealer maintenance is not an abstract instant repair.

The dealer/service partner has real workshop capacity and workload. A vehicle must physically reach the service location, occupy workshop capacity and then physically return/reposition after service.

The player can choose:

- one-off dealer service;
- recurring maintenance agreement for a vehicle/fleet group;
- own workshop maintenance;
- another compatible third-party workshop.

Recurring dealer-maintenance agreements use the shared contract/Auto-renew rules in Section 11.12. They can specify:

- covered vehicle classes/models;
- included service level;
- labour/routine-service pricing;
- priority/booking terms;
- parts responsibility;
- pickup/delivery responsibility;
- warranty coverage where applicable.

A dealer contract does **not** guarantee infinite workshop slots. The maintenance planner must account for the dealer's actual capacity, travel downtime and existing reservations/commitments.

Warranty can reduce or remove eligible repair cost, but it does not teleport the vehicle or eliminate downtime.

Dealer service availability can be especially useful for a small/new company that cannot yet justify building its own workshop.

### 15.5 Used vehicle market

Used vehicles come from actual sellers.

Each used listing refers to a concrete physical asset with relevant state such as:

- age/manufacture date;
- mileage/hours;
- condition;
- maintenance history/last major service where known;
- configuration/retrofits;
- current location;
- seller.

Listings occupy real storage/depot space for the seller.

Unsold vehicles can be discounted and eventually scrapped.

A used vehicle is usually available for ownership transfer without factory production time, but may need:

- physical delivery/repositioning;
- inspection;
- repair/maintenance;
- retrofit;
- regulatory approval/compatibility work.

Imports from inactive foreign regions enter through defined import points and are physically delivered into the active world.

At new-game initialization, period-appropriate used vehicles can already exist with manufacture dates before the chosen start. Their age and condition are initialized rather than manufactured by replaying earlier decades.

### 15.6 Leasing and rental

Some vehicles can be obtained through leasing/rental where historically and commercially appropriate.

Lease/rental provides lower upfront cash requirement in exchange for:

- recurring lease payments;
- defined term;
- usage/condition rules;
- return requirements;
- possible mileage/hour limits or excess-use charges where appropriate;
- ownership remaining with the lessor unless a purchase option is explicitly part of the agreement.

A leasing provider must have a real vehicle available or a credible manufacturer-backed delivery plan. Leasing cannot create nonexistent inventory.

The contract must clearly state who is responsible for:

- routine maintenance;
- heavy maintenance;
- insurance/required cover;
- damage outside normal wear;
- physical delivery and return;
- permitted modifications/retrofits.

Leased vehicles are normal physical fleet assets while under the player's control: they consume parking, depot, staff, fuel/energy and infrastructure capacity and can break down.

At lease end, the asset must physically reach the agreed return point unless the agreement is renewed or converted to purchase where allowed.

Early lease termination can carry a transparent, proportionate contractual fee under the same general philosophy as other recurring agreements; it should not be a hidden ruinous penalty.

### 15.7 Marketplace integration with Contract Planner

The Contract Planner can open the Vehicle Marketplace pre-filtered to vehicles that satisfy a missing fleet requirement.

For example:

> Required: 5 refrigerated wagons  
> Spare compatible fleet: 3  
> Missing: 2  
> **Find compatible vehicles**

The result can compare:

- factory order lead time/cost;
- dealer-stock premium and immediate availability;
- suitable used assets;
- lease/rental alternatives.

The Contract Planner must include the chosen acquisition method in startup cost and readiness calculations.

A higher-priced dealer vehicle can therefore be the rational choice when factory production would miss the contract start date.

### 15.8 Physical delivery and ownership transition

All acquisition sources obey physical continuity.

A vehicle becomes available for normal dispatch only when it has physically reached a valid operating/receiving location.

Buying a vehicle therefore creates a **vehicle delivery requirement** unless the player is taking possession at a location from which the asset can immediately enter normal operation.

The delivery planner first determines the simplest physically valid delivery method. If an external carrier/provider is required, booking is performed through the single **External Transport Order** system in Section 30.1 rather than through a separate vehicle-delivery marketplace.

#### Rail vehicles with a continuous rail route

For locomotives, wagons and other rolling stock, the preferred method is direct rail delivery whenever a continuous technically compatible rail path exists between the seller/manufacturer/dealer location and the player's receiving network.

A rail delivery still has to respect:

- track gauge;
- loading gauge / vehicle dimensions;
- axle/load restrictions;
- electrification and traction compatibility where the vehicle moves under its own power;
- legal/technical route approval;
- infrastructure access and capacity;
- direction/turning constraints where relevant.

A compatible self-propelled rail vehicle may travel under its own power as a delivery/repositioning movement.

Non-powered rolling stock must be hauled by a compatible locomotive. Multiple compatible newly purchased wagons can be consolidated into a delivery train where practical.

A locomotive that cannot operate under its own power over the complete route may still be hauled/dead-towed if its physical rail compatibility permits it.

The delivery movement is a real movement on the railway and consumes real capacity. It can be delayed by congestion, unavailable slots, border/access restrictions or another operational problem.

#### Rail vehicles without a usable continuous rail route

If no technically/legal continuous rail route exists, **specialized heavy road transport** is a possible fallback only when the current era has suitable real equipment, handling/loading capability, a valid route and an available provider. It is not a guaranteed 1900 delivery method. If none exists, show a delivery blocker and offer another seller/receiving point, a real connection project or another explicitly supported period-compatible solution; do not fabricate modern equipment.

Rail vehicles are transported **one physical vehicle per suitable heavy-haul movement by default**, unless a later explicitly supported transport system can safely carry more.

Where supported by the period and provider, the transport is visually represented as a recognizable oversized/special movement. A later-era example includes:

- heavy tractor unit;
- specialized low-loader / modular trailer;
- the actual locomotive/wagon physically loaded on the trailer;
- one or more escort vehicles where required;
- warning lights/beacons and other period-appropriate oversized-load markings.

This is intended to be visible gameplay/world activity, not an invisible delivery timer.

A specialist road movement can require high-level route feasibility based on:

- road width/geometry;
- bridge/load limits;
- clearance/height;
- tight urban turns;
- road restrictions;
- border/permit requirements.

The player does not manually steer the transport or file every individual road permit. The provider plans a feasible route and the UI exposes any major blocker, detour, delay or exceptional permit requirement.

#### Specialist heavy-haul providers

Oversized rail-vehicle transport is a specialist commercial service with **finite market capacity**.

The player normally orders it from an external heavy-haul provider unless the company later owns appropriate specialist equipment and is legally/technically able to perform the movement itself.

A provider can have a limited number of suitable:

- heavy tractors;
- modular/low-loader trailers;
- trained crews;
- escort resources;
- available work slots.

Therefore purchasing a locomotive from dealer stock does **not** guarantee immediate road delivery.

The pre-filled External Transport Order shows compatible heavy-haul providers and, where known:

- transport price;
- earliest pickup date;
- estimated delivery duration;
- required route/permit preparation;
- suitable equipment availability;
- whether an escort vehicle is included;
- current queue / capacity status.

If only a few companies in the region own suitable equipment, the player may need to wait for the next available specialist transport slot.

A large purchase can therefore create a delivery sequence. Later-era example, when compatible road transport exists: five locomotives bought without a rail connection may require five separate heavy-haul movements over several days/weeks rather than all appearing at once.

Specialist providers use real finite capacity under the same general economic principle as construction companies, manufacturers and workshops. They cannot accept unlimited simultaneous oversized movements.

The player can compare delivery providers, but a quoted **earliest pickup** is part of the readiness calculation and cannot be ignored by the Contract Planner.

#### Ordering and integration

The Vehicle Marketplace should offer an **Arrange delivery** action immediately after purchase/lease where delivery is required. This is a contextual shortcut into the External Transport Order, pre-filled with the purchased asset, its current location and the intended receiving point.

The player can also leave an owned vehicle at the seller/dealer temporarily and arrange transport later, but it remains physically located there and may incur storage/holding charges where applicable.

The transport-service agreement remains separate from the vehicle purchase. A dealer may offer dealer-arranged transport, but accepting it still creates/uses the same underlying External Transport Order and consumes a real dealer-owned or third-party transport resource.

The Contract Planner includes:

- production/readiness date;
- delivery-order waiting time;
- physical transit time;
- receiving-location readiness;

when deciding whether a planned vehicle can support a future contract by its required start date.

For an urgent contract, a dealer-stock locomotive may therefore still be too slow if no specialist heavy-haul provider is available soon enough.

#### Other vehicle types

Self-propelled road vehicles normally reach the player by driving over a valid road route, through dealer/manufacturer delivery or player collection.

Vehicles that cannot legally/technically travel normally on public roads can use an appropriate transport service under the same physical-delivery principle.

Water vehicles similarly require a navigable physical route or an explicitly supported specialist transport solution.

Remote rendering may be aggregated, but the logical movement/location must remain continuous at all simulation LODs.

### 15.9 Retrofit

Vehicles and wagons can receive period-appropriate retrofits.

Retrofit can improve condition, comfort or systems and extend life, but only within structural limits.

Dealer/manufacturer-authorized retrofit can be one source of retrofit work, but any provider still needs appropriate physical workshop capability and time.

### 15.10 Scrapping

Assets can be physically sent to appropriate scrapping/disposal facilities. Material value can be partially recovered.


### 15.11 Enduring historical vehicle availability

Historical vehicle availability has no artificial end date. A model has an introduction date, but not a hard retirement date that removes it from the catalogue or disables existing assets.

Keep separate:

1. technology/model existence;
2. physical assets already in the world;
3. finite dealer/used inventory;
4. actual manufacturing or special-order offers;
5. maintenance capability and parts/support availability;
6. technical, safety and route compatibility.

Once introduced, a model stays searchable. Existing assets can be owned, resold, repaired and operated indefinitely while technically serviceable and compatible. Do not make a calendar rollover delete a model, expire its technology or force scrapping. If there is no available seller or manufacturer, show `no current offer`, not `unavailable after year X`.

Ordinary new production of an old model can decline or end through manufacturer economics and capability; that is not a global purchase ban. Used stock comes from real assets. Where a manufacturer retains the relevant capability, new/special-order production can be offered with finite capacity, cost and lead time. Do not guarantee unlimited stock or fabricate a used asset to satisfy a search.

As technology becomes uncommon, fewer independent workshops may retain suitable equipment, skills and supplies. External repair quotes can then reflect a longer journey, scarcity of compatible workshop slots, specialist labour or difficult parts procurement. Providers must expose those reasons, not apply an unexplained annual obsolescence multiplier.

A player-owned compatible workshop, trained workforce and retained know-how can preserve support. This is not free maintenance: staff, equipment, materials, capacity and downtime still cost money. In-house work can be economical at sufficient utilisation; it is not universally cheaper than outsourcing.

Keep physical age/condition separate from technological obsolescence. Repair needs can grow with actual wear, and an old design can remain less efficient than a new design. Do not increase an unchanged engine's fuel consumption merely because a new year/model arrived. Existing safety and compatibility rules still apply, but do not invent a technology-wide retirement prohibition to defeat this decision.

Horse-drawn freight vehicles and omnibuses are valid surviving 1900 equipment beside early motor or steam-powered road vehicles where plausible. They need compatible stable/service facilities, staff and operating supplies at an aggregate level. Do not add a horse-breeding or per-animal life simulator. Their survival does not enable the pre-1900 Early Ages start.

## 16. Maintenance

### 16.1 Vehicle maintenance model

Each player vehicle has a lightweight individual state:

- condition,
- age,
- mileage/hours,
- last major service,
- base reliability,
- limited active faults if needed.

No deep per-component maintenance simulator is required.

Risk also depends on the quality of the surrounding maintenance system:

- mechanics,
- workshop capacity,
- utilization,
- distance to suitable facilities,
- equipment,
- parts/supplies.

### 16.2 Physical service

Vehicles must physically travel to an appropriate **maintenance facility** for service.

Maintenance facilities are distinct from ordinary parking/storage facilities. A location may provide both functions, but this is not required.

A suitable external dealer/authorized-service workshop under Section 15.4 is a valid maintenance facility when its supported vehicle type, service level and real workshop capacity cover the required work. Outsourcing service does not bypass physical travel, workshop occupancy or downtime.

A vehicle or vehicle group can have an assigned/preferred maintenance facility, with allowed fallbacks where configured. The assigned facility must actually support the required vehicle type and maintenance level.

If a workshop is full, vehicles wait physically in yards/parking or at another valid holding location.

Remote fleets without nearby maintenance suffer real downtime because vehicles must travel farther for inspections and repairs.

Self-propelled vehicles travel to maintenance under their own power when their condition and route permit it.

Non-powered rail vehicles such as passenger/freight wagons must be **physically hauled to maintenance** if the workshop is not located in the same yard.

The preferred transfer hierarchy is:

1. use an available compatible line/transfer locomotive from the relevant depot or regional pool;
2. consolidate multiple wagons requiring the same transfer where practical;
3. if no suitable line locomotive is available, a compatible shunting locomotive may perform the transfer as a fallback.

Using a shunting locomotive outside normal yard work is deliberately inefficient. Compared with a line locomotive it can have:

- much lower maximum speed,
- lower practical towing capacity,
- fewer wagons per transfer,
- greater journey time,
- higher disruption per transported wagon,
- restrictions on which main-line routes it may legally/technically use.

A slow maintenance transfer occupies real track sections/slots and can therefore reduce corridor capacity or delay other trains. The planner must show this consequence before dispatch where material.

A shunter fallback is allowed only when the specific locomotive and route are technically and legally compatible; the game must not use it as a universal escape hatch.

If no valid locomotive can haul a wagon to the assigned maintenance facility, the wagon remains out of service until suitable traction or another valid maintenance solution is available.

After service, the vehicle/wagon must also physically return to an operational or parking location; it does not teleport back to a line or pool.

### 16.3 Operational failures and rail recovery

Most vehicle faults should **degrade operation rather than immediately immobilize the vehicle**.

Typical non-critical locomotive/vehicle faults can cause:

- reduced maximum speed,
- reduced traction/power,
- higher fuel/energy consumption,
- reduced reliability for the remainder of the Trip,
- loss of some comfort/service equipment,
- a requirement to visit maintenance after completing the current reasonable operating task.

If the train can still move safely, the preferred behaviour is to finish the current delivery/service where practical, unload/drop off passengers or cargo as planned, and then travel physically to a suitable maintenance facility.

The UI and dispatcher must make the degraded state visible and may recommend withdrawing the vehicle earlier when continuing would create excessive risk or disruption.

A fully immobilizing failure on the main line is intentionally rare.

When a locomotive/train becomes unable to move:

1. the affected track section becomes physically blocked;
2. dispatching checks whether other trains can route around the obstruction;
3. if there is no usable bypass or passing route, trains already committed toward the blockage may have to stop and **reverse/back out to the nearest suitable station, siding, crossover or junction** to clear the corridor;
4. a compatible rescue/recovery locomotive must physically travel to the failed train;
5. the failed locomotive or entire consist is then physically hauled to the nearest suitable safe location or maintenance facility.

Recovery traction can come from:

- an available line/transfer locomotive,
- another compatible locomotive reassigned from nearby service,
- a shunting locomotive only as a constrained last-resort option where route, speed and towing limits permit.

The dispatcher should choose a recovery plan that minimizes total network disruption, but it cannot teleport trains, ignore directionality or pass through occupied track.

Backing/reversing movements must respect train direction, signalling/infrastructure and available crossovers. If the current consist cannot reverse normally, the recovery plan may need another locomotive attached at the opposite end or another physically valid movement.

A blocked single-track section can therefore create real knock-on disruption until the failed train is removed. Double-track or bypass infrastructure can greatly reduce the impact.

Because severe immobilizations are rare, the player should not routinely micromanage rescue operations. Dispatch automation can generate the recovery plan, while the player is shown:

- where the blockage is,
- which services are affected,
- selected rescue locomotive,
- estimated clearance time,
- any trains that must reverse/reroute,
- expected capacity and delay impact.

Poor maintenance, severe faults or extreme conditions can increase the chance of an immobilizing failure, but normal well-maintained operation should make such events exceptional.

### 16.4 Infrastructure maintenance

Track/road infrastructure has aggregated condition by meaningful section.

Maintenance depends on workforce, bases, equipment, budget and age.

Poor maintenance should first create:

- speed restrictions,
- delays,
- closures,
- repair work,

before becoming a serious accident risk.

Infrastructure maintenance can be done in-house or outsourced.

Recurring outsourced maintenance agreements can use Auto-renew under Section 11.12. Renewal extends the agreement, not the contractor's physical workforce or equipment capacity.

## 17. Depots and operating facilities

Depots are physical infrastructure, not menus.

Rail depot layout can include:

- arrival track,
- storage/sidings,
- service hall,
- coal/water/fuel,
- turning facilities,
- departure route.

Poor depot geometry can create real operational inefficiency.

Road vehicles need garages/parking/service facilities.

### 17.1 Regional fleet pools and facility roles

Operational vehicles are not normally hard-bound to one Line. By default, compatible vehicles belong to a **regional fleet pool** and dispatching assigns actual assets to Trips as needed.

The dispatcher must choose from real physical assets and consider:

- current vehicle location,
- compatibility with the Service Pattern,
- passenger/cargo capacity,
- traction and route feasibility,
- maintenance condition and upcoming service,
- fuel/energy requirements,
- reserved-capacity commitments,
- deadhead/repositioning distance and time,
- parking/yard capacity,
- maintenance-facility capacity,
- other already-assigned Trips.

Tranzit distinguishes three facility roles:

1. **Operating/dispatch depot** — configured primarily on a Line or Service Pattern; this is where the service is normally staged, dispatched, turned around or recovered.
2. **Parking/storage facility** — where an idle vehicle or wagon can physically stand when it is not needed in active service.
3. **Maintenance facility** — where the vehicle is physically sent for inspections, servicing or repair.

For rail operations, an operating/dispatch depot can also act as a **local traction base** for locomotive exchange. This means it keeps suitable locomotives physically available to work onward segments from that location.

A traction base can also be built as a smaller standalone facility. It is cheaper and simpler than a full depot and is intended for local locomotive staging rather than heavy maintenance.

A basic traction base can include:

- a small number of locomotive parking/staging tracks,
- access/turnaround track geometry,
- period-appropriate fuel, coal or water supply where required,
- basic crew/operational facilities,
- light inspection or minor servicing only where the selected module supports it.

It does **not** automatically provide:

- heavy maintenance,
- large workshop capacity,
- wagon repair,
- major overhauls,
- extensive storage yards.

A typical early or mid-game traction base may hold only 2–4 locomotives. Its purpose is to support locomotive exchanges, helper/banking operations, rescue coverage or a remote cluster of Lines without forcing the player to build a full maintenance depot.

Locomotives based there still need a separate compatible maintenance facility for heavier scheduled work and must physically travel there when service is due.

The same modular principle applies to **road-vehicle operating bases**.

A small road base can provide only what a local bus/truck fleet actually needs, for example:

- physical parking spaces,
- basic dispatch/crew facilities,
- period-appropriate fuel storage/pumps or later charging infrastructure,
- washing/basic inspection where installed.

It does **not** require a full mechanical workshop.

Heavier scheduled maintenance and repairs can be centralized in a larger regional road maintenance facility. Buses/trucks must physically drive there when service is due, creating real downtime and travel cost.

This makes it viable to operate several cheap local parking/dispatch bases around a region while maintaining one larger workshop, instead of forcing the player to duplicate expensive maintenance infrastructure everywhere.

A small road base can later be upgraded modularly with:

- more parking,
- fuel/charging capacity,
- light-service bays,
- full workshop modules,
- spare-parts storage.

**Tram, trolleybus and metro depots/garages are different:** their basic depot type always includes a minimum workshop/maintenance capability. The player does not build a pure parking-only depot for these modes.

A basic tram/trolleybus/metro depot therefore includes:

- vehicle storage/parking,
- dispatch access,
- basic inspection and routine maintenance workshop capacity,
- required power infrastructure for the vehicle type,
- basic operational staff facilities.

Metro depots must also be physically connected to the metro network they serve.

Larger/heavier maintenance capacity can still require expansion modules or a larger central workshop, but every tram/trolleybus/metro depot can perform routine service by default.

One site can provide more than one role, but it does not have to. A cheap road parking yard therefore does not need a full workshop, and a regional road fleet can share a more distant maintenance base.

A Line or Service Pattern can define:

- preferred/primary operating depot,
- one or more allowed fallback operating depots,
- required operating depot where operationally necessary.

Vehicles/rolling stock can separately define:

- preferred parking facility,
- preferred maintenance facility,
- allowed fallback facilities.

To avoid micromanagement, parking and maintenance assignments can be inherited from a regional pool, vehicle class or fleet group, with optional overrides for individual assets.

These assignments are planning preferences, not teleport destinations. The actual physical location of every asset remains authoritative.

A vehicle allocated from another location must physically deadhead/reposition to the service start, consuming time, infrastructure capacity, fuel/energy and potentially crew resources.

When a Trip finishes, the dispatcher may keep the asset near the next useful work rather than forcing an unnecessary return to a parking facility. If it becomes idle, it must eventually occupy a real valid parking/storage location.

When maintenance becomes due, the asset must physically travel to a suitable maintenance facility. It does not matter whether that facility is the same site used by the Line for operations or parking.

Parking and workshop capacity are real. If a facility is full, additional assets cannot be hidden inside it.

Dispatch automation must not double-book assets, exceed physical parking/workshop capacity or silently consume capacity reserved for contracts. If a timetable cannot be covered, the planner must explain the concrete shortage.

### 17.2 Owned versus rented operating facilities

The player does **not** need to own every depot, yard, parking area or workshop used by the company.

A small/new carrier can rent or contract capacity in a compatible third-party facility instead of immediately constructing its own.

Possible rented capacity includes:

- road vehicle parking/dispatch spaces;
- locomotive/rail vehicle staging tracks;
- wagon sidings/storage;
- light or heavy workshop capacity;
- fuel/charging/water facilities;
- shunting/yard services;
- crew/dispatch facilities where offered.

A facility owner can be:

- another transport company;
- a specialist depot/workshop operator;
- municipality/state/public infrastructure entity;
- manufacturer/dealer/service partner;
- another private infrastructure owner.

Rental/access is a real commercial agreement tied to **finite physical capacity**.

A facility cannot rent the same parking track, workshop slot or yard capacity to unlimited companies.

The agreement can define:

- capacity reserved;
- supported vehicle types;
- validity period;
- access/operating hours;
- recurring fixed fee;
- per-use fee;
- priority level;
- included fuel/service/shunting functions;
- notice/cancellation terms;
- Auto-renew where appropriate.

Rented capacity behaves like owned capacity for physical feasibility, but ownership remains with the provider.

A vehicle still physically travels to and occupies the rented site. The provider can become a bottleneck, suffer disruption or refuse expansion beyond the contracted capacity.

This allows an early company to start with, for example:

> 4 rented truck parking spaces + outsourced dealer maintenance

instead of immediately buying land and building a full depot.

Similarly, a rail operator can initially rent a few sidings/staging tracks and maintenance services at an existing yard if the owner offers them.

The player can later replace rented capacity with owned facilities when scale, cost or strategic control makes that worthwhile.

The Contract Planner and Line/Service Pattern planner must treat owned and contracted third-party capacity consistently. If the rental expires or is terminated, services depending on it become at risk rather than continuing with invisible free capacity.

### 17.3 Shunting capability

Any rail depot, yard or freight/passenger facility that regularly assembles, disassembles or rearranges consists needs sufficient **shunting capability**.

A larger active operating depot should normally have at least one dedicated shunting locomotive/vehicle available. Larger yards may need several, and shunting capacity can become a real bottleneck.

Very small or early facilities may operate without a dedicated shunter by using a line locomotive or historically appropriate simpler methods. This is allowed, but it consumes line-locomotive time and reduces operational efficiency.

Shunting workload is driven by real activity such as:

- attaching/detaching passenger or freight wagons,
- moving wagons to loading/unloading tracks,
- transferring vehicles to storage tracks,
- moving locomotives to fuel/water/service facilities,
- re-forming consists for different Trips,
- moving vehicles in/out of workshops.

The UI should expose a clear yard/depot capacity indicator such as expected shunting workload versus available shunting capacity, rather than forcing the player to schedule each movement manually.

If shunting capacity is insufficient:

- consist preparation takes longer,
- departures can be delayed,
- loading tracks/sidings stay occupied longer,
- line locomotives may be borrowed for shunting if the player allows it,
- the planner should identify shunting as the actual bottleneck.

Shunting capability evolves historically. Later technologies can reduce labour/time requirements and introduce more efficient dedicated shunters or yard equipment, but physical movement is never replaced by teleportation.

Dedicated shunters are usually assigned to a facility/yard rather than to a passenger or freight Line. They still need parking and maintenance facilities under the same physical rules as other vehicles.

Shunters can also be used as a **fallback wagon-transfer locomotive** for maintenance or other necessary local repositioning when no suitable line/transfer locomotive is available. This removes the shunter from normal yard work for the duration of the trip and therefore reduces shunting capacity at its home facility.

Because shunters are optimized for yard work rather than main-line hauling, such transfers are slow and limited in train length. They consume real main-line capacity and can become an intentionally visible operational penalty for under-investing in suitable transfer traction or maintenance coverage.

## 18. Energy and operating supplies

Fuel and many operating supplies are real goods.

Examples:

- coal,
- diesel/petrol,
- water,
- lubricants,
- parts,
- catering supplies.

Road operating bases may therefore need real fuel deliveries, or later sufficient electrical charging/grid capacity, depending on the vehicles assigned there.

Depots, stations and terminals can maintain real inventories and energy-service infrastructure where installed.

### 18.1 Vehicle fuel / energy state

Vehicles that carry their own fuel/energy have a real operating state such as:

- fuel quantity;
- battery/energy state;
- historically appropriate consumable traction supply such as coal/water where relevant.

Consumption is based on actual operation and remains tied to the common simulation clock/rules in Section 3.

The player does **not** normally click a manual Refuel action for every vehicle.

Instead, fueling/charging is integrated into fleet and Trip scheduling.

### 18.2 Where fueling and charging can happen

Normal scheduled fueling/charging, including traction coal/water and aggregate animal-traction supplies, takes place **between Trips** at a physical compatible facility. An ordinary intermediate stop in the same Trip does not silently enable refueling. Passenger toilet/water servicing is not traction refueling.

Valid locations include:

1. **Depot / operating base** with the required fuel/charging module;
2. **Passenger or freight station/terminal** with the required fueling/charging infrastructure.

Simply being at a depot or station is not enough. The site must have infrastructure compatible with the vehicle/energy type.

Examples include:

- diesel/petrol pumps and storage;
- coal/water servicing where historically appropriate;
- electric charging equipment;
- other mode-specific energy-service modules.

A third-party station/terminal can provide fueling/charging only when the operator has the relevant service/access right and the facility owner offers that service.

Fuel/energy does not appear inside a vehicle automatically merely because the Trip ended at a station.

### 18.3 Automatic fueling between Trips

The dispatcher automatically inserts fueling/charging into the vehicle's turnaround plan when needed and when a compatible facility is available.

A typical vehicle duty can therefore be:

> Trip A  
> → arrive at terminal  
> → refuel/charge during turnaround  
> → Trip B

or:

> Trip A  
> → deadhead to operating depot  
> → refuel  
> → prepare for next Trip

The player can inspect the planned task, but routine fueling is automated.

The planner considers:

- current fuel/energy state;
- expected consumption of the next Trip/duty;
- desired operating reserve;
- time available before the next Trip;
- fueling/charging rate;
- number/capacity of pumps, chargers or service points;
- site inventory;
- electrical grid capacity where relevant;
- repositioning time if the vehicle must visit another facility.

Fueling therefore consumes real turnaround time and facility capacity.

### 18.4 Trip energy feasibility

Before a Trip is committed, the planner checks that the assigned vehicle can complete the planned duty with a valid energy plan.

A Trip cannot depend on fuel/energy that does not physically exist or on a refueling point the company cannot use.

If the vehicle does not have enough energy for the next Trip, the planner must find a valid between-Trip fueling/charging opportunity before departure.

If none exists, the Trip is not ready. A longer service can be planned as successive Trips with a real fueling turnaround, or use a physically valid traction exchange whose locomotives have sufficient energy for their assigned segments. Such planning retains passenger/cargo custody, capacity and commercial obligations; it never resets fuel by renaming a Trip. The UI explains a remaining blocker, for example:

> Bus #37: insufficient fuel for next duty  
> Required before departure: 82 L  
> Current: 41 L  
> No compatible fueling point available at this terminal

The planner can resolve this by:

- using another compatible vehicle with sufficient range;
- scheduling fueling at the current depot/station;
- repositioning to a compatible fueling facility if time permits;
- changing the duty/turnaround plan;
- delaying/cancelling according to the applicable disruption policy if the problem reaches day-of-operation.

The dispatcher should not intentionally send a vehicle onto a Trip that is predictably unable to finish because of insufficient fuel/energy.

### 18.5 Facility capacity and shortages

Fueling/charging infrastructure has finite practical capacity.

Examples:

- one pump cannot service unlimited buses simultaneously;
- a charging site has a finite number of charging positions and available electrical power;
- a rail fueling/service point can handle only the vehicles/trains that physically fit and can be processed in time.

The timetable/fleet planner should detect recurring fueling bottlenecks when they are predictable.

The facility also needs the actual energy/supply available.

For stocked fuels/supplies, inventory can run low or empty.

For electricity, usable charging is constrained by the site's grid connection/capacity.

A facility with no remaining fuel, no available charging power or no free service capacity cannot complete the planned task merely because the module exists.

### 18.6 Supply procurement

The player can:

1. buy delivered supply,
2. buy at source and transport it personally,
3. buy at source and hire another carrier through the shared External Transport Order in Section 30.1,
4. use a recurring supply contract.

Automatic reorder thresholds can be configured and later delegated.

Recurring supply agreements can use Auto-renew under Section 11.12. Renewal extends the commercial agreement; inventory reorder thresholds separately determine actual orders and deliveries. Renewing a supply contract never fills a depot automatically or bypasses physical transport.

For scheduled recurring physical-supply agreements, use the game's two-week month directly rather than Gregorian-style numeric delivery dates.

Supported baseline schedule forms are:

- **Weekly** — select one or more weekdays. The delivery recurs on those weekdays in both game weeks of every active month. Selecting Tuesday, Wednesday and Thursday therefore creates three scheduled deliveries per week, six per 14-day month.
- **Once per month** — choose **Week 1** or **Week 2**, then either a specific weekday in that week or an allowed delivery window covering that selected week. A window means the supplier may fulfil the one monthly delivery on any valid day inside it; it does not create seven deliveries.

Each scheduled occurrence is one contractual delivery with its own physical fulfilment state.

Recurring-supply pricing may use an explicit commercial basis such as **price per delivery** or **price per physical unit** (for example money/t). Whatever basis is negotiated, the UI must always calculate and show the **total expected price of one scheduled delivery** from the agreed quantity and price rule. Example: 20 money/t × 60 t = 1,200 money for that delivery. Each fulfilled scheduled occurrence creates its resulting commercial charge exactly once.

Quantity, item, handover location and transport responsibility remain explicit contract terms. A scheduled delivery still requires actual supplier stock/production, storage capacity and physical transport; reaching the scheduled weekday does not teleport inventory.

Electricity is purchased through physical grid connections/capacity rather than moved as cargo wagons.

## 19. Infrastructure ownership and access

Infrastructure can be:

- state/public,
- municipal,
- privately owned.

### 19.1 Public infrastructure

A state may commission construction and retain ownership.

Publicly supported corridor/infrastructure projects use a **small enumerated set of contract/ownership models**, not arbitrary mixes of funding, ownership and operating rights assembled per tender. Each model must make the following explicit before bidding: who finances construction, who owns the completed asset, who operates it, what access obligations apply, how long the arrangement lasts and what happens at expiry/termination.

Supported models:

1. **State-owned infrastructure with operating right** — the public authority finances/owns the infrastructure while the player can win the right/obligation to operate transport services over it. The player is not the infrastructure manager merely because it operates services there.
2. **Build–Operate–Transfer concession** — the player finances/builds the specified infrastructure, operates it for the agreed concession period under published conditions, then transfers the asset to the public authority at the defined handover point.
3. **Publicly co-funded private infrastructure** — the authority contributes to construction while ownership remains private/player-side, subject to explicit funding conditions such as access obligations, fee constraints, minimum service/capacity commitments or a required operating period.

Do **not** add a separate model where state-owned infrastructure is simply entrusted to the player for infrastructure management/administration. Do not create a free-form legal/PPP contract builder merely because real-world arrangements can be more complex.

The state can later tender transport services over the infrastructure.

### 19.2 Private infrastructure

The player can finance and own infrastructure and charge access fees.

A private infrastructure owner can reserve as much capacity as it wants for its own services and can decide whether, to whom and on what commercial terms it sells the remaining capacity.

**Mandatory open access is exceptional, not routine.**

The state/regulator should interfere with private access rights only in clearly defined exceptional situations, such as:

- war or national emergency,
- temporary strategic transport necessity,
- disaster response,
- infrastructure that received public funding under an explicit access condition,
- a specific concession/licence whose terms already included emergency/public-service access.

Such intervention should normally be temporary, clearly communicated and limited to the actual exceptional need.

Outside these cases, a private owner may refuse competitors even when spare capacity exists. The economic counterweight is the very high cost of duplicating infrastructure, which should often make voluntary access agreements commercially attractive to both sides.

Building private rail should be very expensive so sharing existing infrastructure is often rational.

### 19.3 Facility and infrastructure access agreements

Ownership is not required to use every facility.

Where the owner is willing, the player can buy/rent access to existing stations, terminals, depots, sidings, parking areas, workshops or other operational infrastructure.

These access agreements reserve or permit real capacity rather than creating abstract rights without physical space.

Terms can include:

- fixed recurring access fee;
- per-use fee;
- reserved capacity;
- operating windows;
- supported vehicle/cargo/service types;
- service/shunting/handling included;
- priority;
- contract duration and renewal;
- notice/cancellation rules.

Facility-access agreements use the relevant underlying capacity system. For example, renting depot parking consumes parking capacity; station calls consume station capacity/slots; workshop contracts consume workshop capacity.

The game should reuse the same access-agreement concept across planners rather than create separate unrelated rental systems for every facility type.

### 19.4 Connection agreements

The player cannot simply place a switch into someone else's track.

Connecting to foreign infrastructure requires a connection agreement/permit.

Terms can include:

- one-time fee,
- ongoing fee,
- capacity contribution,
- financing upgrades,
- guaranteed access rights.

## 20. Stations, terminals and infrastructure capacity

Stations and terminals can also be publicly or privately owned.

Other operators may pay for platform, track, storage and terminal use.

Passenger stations are **modular physical facilities**, not single abstract buildings.

Larger passenger stations/terminals can also support an **integrated company branch/office module** under Section 7.2. This module contributes commercial/administrative capacity, not railway platform/track capacity, and follows normal ownership/rental rules.

A passenger rail station can be assembled from functional elements such as:

- platform tracks,
- passenger platforms of configurable length,
- station/entrance building,
- waiting areas,
- ticket office/booking-sales modules where historically relevant,
- shelters/canopies,
- toilets and basic amenities,
- pedestrian access paths,
- stairs/ramps,
- footbridges or underpasses,
- concourse/transfer halls,
- baggage/service facilities,
- later retail/commercial modules,
- company branch/office module where the station is large enough,
- parking and P+R,
- taxi/drop-off space,
- adjacent bus/tram/trolleybus/metro interchange modules.

Not every station needs every module. A rural halt can be extremely simple, while a major hub can grow into a large multi-modal complex.

Station capability and passenger experience emerge from its real modules and layout.

Relevant station effects can include:

- maximum train length served,
- number of simultaneous trains,
- passenger throughput,
- transfer walking time,
- boarding/alighting speed,
- shelter/comfort,
- ticketing/processing capacity,
- passenger-information capability,
- accessibility,
- interchange quality,
- operating/staff requirements.

Platform length is physical. A train that is longer than the usable platform cannot be treated as fully accommodated without an explicit operational rule/penalty.

Passenger circulation matters at an aggregated level. The game does not need to simulate every person through every doorway, but station design should calculate practical flow constraints from entrances, platforms and connections. Representative visible pedestrians should follow the actual layout.

A station can therefore become a bottleneck even when the surrounding railway still has track capacity.

### 20.1 Passenger station progression

Available station modules evolve with history and technology.

Small stations can rely on simple buildings and platforms. Ticket sales are available only when the station has a compatible ticket-office/booking-sales module or another valid sales channel exists. The available catalogue is initialized for the selected year; founding a new company in a later year does not reset station technology to the beginning of railways.

Depending on era, station modules can include:

- larger covered platforms,
- improved passenger circulation,
- underpasses/footbridges,
- electric lighting,
- passenger-information/announcement modules appropriate to the era,
- later realtime electronic information systems,
- escalators/lifts where appropriate,
- automated ticketing,
- integrated urban-transport interchanges,
- larger commercial/concourse facilities.

A station can evolve in two main ways:

1. **Extension / modular growth** — keep the existing station building and add new halls, wings, platforms, circulation links or interchange modules around it.
2. **Full replacement** — demolish the existing main station building or selected major station modules and construct a larger/newer replacement.

Full replacement is a real construction project, not an instant upgrade. It can require:

- demolition time/cost,
- construction materials and contractor capacity,
- temporary passenger access or temporary station facilities,
- reduced station throughput during construction,
- temporary closure of affected entrances/platforms where necessary,
- municipal/state approval where the site is regulated,
- heritage approval or prohibition if the original structure is protected.

The project planner should show how much of the station can remain operational during each construction stage.

The player can optionally purchase **construction mitigation measures** to reduce the negative impact of the rebuild. These are project-level choices rather than separately micromanaged temporary networks.

Possible mitigation measures include:

- temporary passenger platforms,
- temporary entrance/ticketing building,
- temporary pedestrian routing,
- temporary bus replacement/shuttle service,
- staged platform closures,
- temporary interchange relocation,
- additional contractor shifts/work windows where available.

Each measure has a clear cost and effect, such as:

- higher temporary passenger throughput,
- smaller transfer-time penalty,
- lower reputation impact,
- fewer cancelled Trips,
- shorter effective disruption window.

The UI should compare the expected station impact **with and without** each mitigation option before the player approves the construction plan.

Temporary facilities are physically represented where practical, but their detailed internal management is automated. After the project is complete they are normally removed automatically unless the player explicitly chooses to retain a useful element.

A replacement project does not automatically demolish the whole railway site. Tracks, platforms, buildings and interchange modules can be retained or rebuilt independently where the design permits.

Upgrading a station therefore does not automatically erase its historic fabric. Existing buildings/platforms can remain, be extended, repurposed, replaced or protected depending on the site and era.

Where an old station building is preserved, it may remain as an entrance, secondary hall, commercial space or heritage element inside a much larger modern station complex.

### 20.2 Multimodal interchange

Urban and intercity transport should connect through real station geometry.

A bus terminal, tram stop, trolleybus stop, metro entrance, taxi area or P+R facility can be attached to or placed near a rail station.

Transfer quality depends on actual walking distance, access routes, waiting environment and timetable coordination.

A transfer is therefore better when modes are physically integrated than when passengers must cross a large area or street network.

### 20.3 Station capacity, ownership and access charges

Station capacity is distinct from line/track-section capacity.

A station may be constrained by:

- platform occupancy,
- platform length,
- throat/junction conflicts,
- passenger-flow capacity,
- waiting/concourse/platform capacity during major passenger peaks;
- baggage/cargo handling where relevant,
- shunting/turnaround requirements,
- turnaround-service capacity such as fueling, cleaning and crew-change support where installed,
- interchange capacity.

Passenger waiting capacity remains aggregated. The game does not need to place every waiting passenger physically, but a severe sustained queue at a small facility can become a real station-flow bottleneck.

The UI should identify the actual station bottleneck rather than expose one generic capacity percentage.

Station owners can charge other operators for relevant use.

Station access normally has **two commercial components**:

1. **Capacity reservation / station-slot fee** — payment for the right to schedule a defined number of station calls in specified time windows.
2. **Actual usage fee** — charged when the Trip really uses the station and may depend on service type, train length, dwell time and used station services.

Additional charges can apply for:

- terminal services,
- storage/handling,
- interchange facilities,
- shunting/turnaround services,
- exceptional long dwell or overnight occupation where relevant.

A station-call slot is a right to station capacity, **not ownership of a numbered platform**.

### 20.4 Station slots and dynamic platform allocation

Passenger platforms are normally allocated **dynamically to Trips according to station capacity and compatibility**, rather than permanently belonging to one operator or Line.

A station can therefore serve several operators at the same time as long as its real infrastructure can accommodate their services.

A Trip has no default right to wait for "its usual platform" while another compatible platform stands free. The station allocator should use any contractually and physically compatible platform that minimizes conflict and delay. Closures, engineering works and disruption can therefore move a Trip between platforms automatically.

Before a regular Service Pattern is activated at a constrained station, the operator normally needs enough **station-call slots** for the planned calls.

Slots are sold/reserved against the station's calculated usable capacity by time window, for example:

- peak-hour calls,
- off-peak calls,
- daily/weekly bundles,
- seasonal service windows,
- temporary date ranges for short-term contracts or replacement services.

Station-slot validity can follow the Service Pattern calendar. The Capacity Order editor in Section 13.2.1 should normally request required station calls together with the route capacity so the player does not have to buy them separately.

Station capacity agreements use the common Auto-renew rules in Section 11.12 and the rail-capacity renewal checks in Section 13.2. Renewal must revalidate the complete route and station requirements for the next service period.

The station owner cannot sell unlimited slots. The capacity planner maintains:

- safe/usable station-call capacity,
- capacity reserved by the owner for its own services,
- any temporary emergency/public-service capacity obligation that is currently active,
- already committed guaranteed third-party capacity,
- standard/flexible commitments,
- operational reserve for disruption where configured,
- remaining sellable capacity.

A private owner can deliberately reserve part or all of the station's capacity for its own Lines/Service Patterns. Those self-reserved slots consume real station capacity exactly like third-party slots and therefore reduce what can be sold externally.

Mandatory third-party access is rare. It can appear only under exceptional rules such as war/national emergency, disaster response, a temporary strategic state order or a previously agreed public-funding/concession condition.

When such an obligation is active, the UI must show:

- why it exists,
- how much capacity is affected,
- when it starts and is expected to end,
- whether the owner receives compensation or regulated access fees.

Outside these exceptional cases, private station owners are free to refuse third-party access even if spare capacity exists.

Peak capacity can therefore become scarce and more expensive.

A Service Pattern with four guaranteed morning calls consumes four relevant capacity rights from that time window even though the actual numbered platform is assigned dynamically later.

The station allocator considers factors such as:

- platform length,
- current and planned platform occupancy,
- arrival/departure direction and accessible track geometry,
- through platform versus terminating/bay platform suitability,
- electrification/traction compatibility where relevant,
- required passenger facilities,
- expected dwell time,
- turnaround/shunting needs,
- throat/junction conflicts,
- contractual access priority.

Operators primarily contract for **station-call capacity**, not necessarily for one permanently numbered platform.

Access agreements can provide different slot products, for example:

- **guaranteed slot** — the owner must provide a compatible platform within the agreed operating window; highest reservation price;
- **standard slot** — normal scheduled access with less contractual protection during major disruption;
- **flexible/ad-hoc slot** — cheapest; used only when spare capacity exists and can be retimed or rejected when the station is constrained.

Once a slot is sold/reserved, dispatch priority follows the slot product and contract terms regardless of who owns the station.

The owner may reserve peak capacity for its own services in advance, but cannot later displace a competitor's guaranteed slot simply because the owner's own train is late or more commercially valuable.

During disruption, a guaranteed third-party call can therefore take precedence over the owner's own standard/flexible call if that is what the contracted priorities require.

Each station-call slot also has a **tolerance window**.

If a train arrives outside that window because of its own operating delay, the guaranteed station-call priority for that occurrence expires. The train remains eligible to use the station, but it must be fitted into the next compatible spare platform/call capacity and cannot displace an on-time guaranteed call.

Typical status shown to the player:

- **On time / protected** — inside the slot window;
- **Late but protected** — still inside tolerance;
- **Out of slot** — tolerance exceeded; waiting for spare capacity;
- **Reprotected** — lateness caused by a qualifying infrastructure/station-side failure under the access agreement.

The slot contract can define different tolerance values by service type or access product. Guaranteed products can have wider or more predictable tolerance than cheaper flexible access.

Station-call slots are **non-transferable between operators**. The holder cannot resell, lease or privately assign them to another carrier.

If the holder no longer needs the reserved station capacity, it can release it back to the station owner according to the access agreement. The owner can then allocate or sell the returned capacity again.

Unused guaranteed/standard slots still have a reservation cost because the owner has withheld that capacity from other operators.

An operator without a pre-purchased slot, or a train that has fallen out of its slot window, may request an ad-hoc call. It is accepted only if real spare station capacity exists, usually at a higher per-call price or with lower priority.

A dedicated platform can still exist as an exceptional contractual or infrastructure rule where operationally justified, but it is not the default model.

The access-planning UI should show, by relevant time window:

- total usable station capacity,
- capacity reserved for the owner's own services,
- temporary emergency/public-service capacity obligations if active,
- already reserved third-party calls,
- remaining sellable slots,
- player's currently owned/reserved slots,
- expected per-call usage charges,
- expected peak congestion,
- the concrete constraint that limits further sales if capacity is exhausted.

For an ordinary private station, a third-party request can simply be refused by the owner. If access is mandatory because an exceptional public-service rule is active, the UI must explain that rule and enforce only the capacity covered by it.

This prevents hidden oversubscription: if the station is effectively full in the 07:00–08:00 window, neither the player nor an AI operator can buy another guaranteed peak slot unless capacity is expanded or another commitment is released.

The allocator should assign a concrete compatible platform when planning/dispatching each Trip. If disruption makes the planned platform unavailable, it can automatically reassign the train to another valid platform.

Dynamic reassignment must still respect physical track access. The game cannot assign a train to a free platform that the train cannot physically reach without conflicting movements or invalid direction changes.

If no compatible platform is available, the train must:

- wait outside/at an approach signal,
- use another permitted station/stop if the Service Pattern allows it,
- be retimed/rerouted by dispatching,
- or have the Trip disrupted/cancelled as a last resort.

When choosing which delayed/disrupted Trip receives scarce platform capacity first, dispatching uses contractual slot priority rather than favouring the station owner's trains.

The UI should show station utilization and explain why a Trip is waiting, for example: "no compatible 300 m platform available" or "station throat conflict".

To preserve performance, platform allocation is event/schedule driven: it is recalculated when Trips are planned, approach the station or when a relevant disruption/infrastructure change occurs, not continuously every frame.

Rail infrastructure capacity remains strategic rather than requiring a full expert timetable simulator by default.

The UI should communicate section and station utilization clearly, including peak bottlenecks.

Advanced timetable tools may exist later, but are not mandatory for normal play.

## 21. Construction

### 21.1 Contractors

The player does not instantly build infrastructure.

Construction is delivered by external construction companies or, later, a player-owned construction division.

There are:

- many smaller contractors for local/simple works,
- fewer large contractors capable of major railways, highways, tunnels and canals.

Contractors have real capacity, specialization, price, technology and utilization.

### 21.2 Contractor priority market

Projects can purchase higher priority.

A contractor has guaranteed and flexible capacity. Competitors may outbid for some flexible capacity, but cannot arbitrarily steal an entire signed project.

Reallocation happens in bounded intervals, not constant bid ping-pong.

There is a practical capacity ceiling: money cannot create nonexistent workers/equipment.

### 21.3 Construction stages

Construction is visible in simplified physical stages such as:

- preparation/groundworks,
- under construction,
- completed.

Long projects progress along their route rather than the whole project appearing half-built everywhere.

### 21.4 Construction logistics

Large projects consume real materials such as timber, stone, steel, ballast and concrete.

The player chooses whether:

- the construction company supplies/logistics everything,
- the player supplies materials,
- responsibility is split.

Construction sites have temporary storage.

Lack of material can halt a stage.

### 21.5 Temporary construction infrastructure

Contractors can automatically establish simplified temporary site infrastructure such as:

- access roads,
- storage areas,
- site huts/camps,
- equipment yards.

These are mainly operational/visual and should not require heavy micromanagement.

After completion, relevant temporary roads can be removed, retained or converted.

Large reconstruction projects can also offer optional **operational mitigation packages**. These are higher-level project options that reduce disruption through temporary facilities, staged closures or substitute transport rather than forcing the player to manually build every temporary element.

Mitigation consumes extra money, contractor capacity and sometimes temporary land, so the player chooses between a cheaper disruptive rebuild and a more expensive construction plan that preserves more operating capacity.

### 21.6 Technological construction progress

Construction speed and capability improve historically through mechanization and specialized equipment, including later track-laying/maintenance trains.

Construction duration, deliveries and contractor work windows use the common game calendar. Later starts initialize the appropriate available construction technology; they do not force an industrial-era contractor back into an earlier manual-only technology stage.

## 22. Terrain engineering

Terraforming is not a free standalone brush.

Terrain modification is permitted only as part of a building/infrastructure project or modification.

Earthworks are real project scope requiring:

- excavation/fill,
- machines,
- workers,
- time,
- potentially transported materials.

## 23. Bridges and tunnels

Bridges and tunnels have period-specific structural technologies.

Options differ in:

- cost,
- construction time,
- load limit,
- speed limit,
- span/capability,
- lifespan,
- maintenance.

Old bridges may become inadequate for later heavier/faster vehicles and require reinforcement or replacement.

## 24. Construction corridors and future-proofing

When building linear infrastructure, the player may acquire/reserve a wider corridor than immediately needed.

Example: build one track today but reserve land/earthworks for a second track later.

Reserved corridors prevent normal city development inside them and make future expansion cheaper/easier.

## 25. Infrastructure upgrades under operation

Infrastructure is upgraded section by section.

If geometry permits, operation can continue with reduced capacity:

- one track closed while another handles bidirectional traffic,
- staged electrification,
- signalling upgrades,
- platform extensions.

Single-track routes may require full closures, work windows or construction of a parallel track first.

The project planner should show expected capacity impacts and possible diversions.

## 26. Land and demolition

Land under company infrastructure is an asset, managed by corridor/site rather than individual parcels.

Land value changes over time as cities grow.

An old depot on the edge of town can later become valuable central land.

Demolition in built-up areas is handled at project level rather than negotiating every house individually.

Projects show:

- affected buildings,
- protected structures,
- compensation cost,
- approval status,
- reputation impact.

Public-interest expropriation may be possible through the state under suitable conditions, at significant cost/reputation impact.

Demolition rules also apply to the player's own infrastructure. Replacing an existing station building, depot structure or terminal module requires an explicit demolition/redevelopment project rather than an abstract upgrade. If the structure is protected, demolition may be prohibited or require exceptional approval even when the player owns it.

Brownfields/abandoned buildings are easier to redevelop.

## 27. Technology and research

Technology broadly follows historical chronology, but research can accelerate access within plausible limits.

Possible research capacity progression:

- one basic research slot,
- own research department/centre,
- external research contract,
- later additional capacity.

Technology has prerequisites.

Progression includes not only vehicles but also:

- construction methods,
- signalling,
- electrification,
- communications,
- dispatching,
- maintenance,
- business systems,
- logistics automation.

The available technology baseline depends on the selected new-game year (Section 3.5). Pre-1900 invention progression is Early Ages content; already established technology remains available in the base game as appropriate. Availability does not give the player free equipment or erase company-specific installation/training requirements.

## 28. Automation and information technology

Technological progress changes both how much manual management is required and **how geographically centralized the company can become**.

The wider historical progression can include:

- local paper-based offices,
- telegraph,
- telephone,
- centralized reservation/sales systems,
- telephone booking/sales,
- automated/self-service ticketing,
- centralized dispatch,
- electromechanical systems,
- computer planning and customer databases,
- electronic ordering,
- modern online/self-service booking and digital customer systems.

This is not a mandatory invention sequence restarted for every new company. Start-year data determines which technologies exist in the world, but the player's company still needs to adopt/install the relevant systems, staff and organizational processes to gain their benefits.

A newly founded 1950 or 1975 company can therefore have access to contemporary technology, but it does not automatically begin with a mature nationwide centralized commercial system for free.

Business-system upgrades can progressively change the branch rules in Section 7.2:

- reduce local administrative workload,
- let one office process work for multiple cities,
- widen Opportunity Board discovery,
- centralize customer relationships/reservations,
- eventually remove the ordinary branch-at-every-commercial-stop requirement where law/contracts allow.

### 28.1 Passenger information progression

Passenger information uses three practical capability levels:

1. **Timetable only** — passengers know the published schedule and normal stop/platform information, but current disruption is generally not known until they reach the relevant station/stop or receive local staff information.
2. **Operational updates** — current delays, cancellations and platform/stop changes can be communicated at equipped stations/terminals through period-appropriate staff, announcements or boards.
3. **Realtime information** — live operational information can reach passengers before and during the journey, allowing current ETA/platform information and earlier disruption rerouting/rebooking.

These are gameplay capabilities, not hidden quality multipliers. Do not add separate information-accuracy, awareness or coverage percentages unless a later design specifically requires them.

The capability controls **when passenger decisions may react to known disruption**:

- with Timetable only, passengers primarily choose from the published timetable;
- with Operational updates, passengers can react once current information reaches the station/terminal;
- with Realtime information, passengers can react before reaching the station or during the journey, and protected itineraries can be rebooked earlier.

Information technology never changes the real vehicle position, delay or capacity. It only changes what passengers can know and when recovery can begin.

The company's central information technology and the local facility capability both matter where applicable. A modern company can therefore have realtime information at a major equipped station while a small rural halt still provides only basic timetable information.

Do not model individual loudspeakers, displays or information clerks. The relevant station/terminal module represents the capability at the appropriate level of abstraction.

The UI should show concrete consequences such as:

- current disruption information unavailable;
- delay/cancellation communicated at station;
- platform change communicated;
- alternative selected before departure;
- protected connection rebooked earlier.

The pre-1900 progression belongs mainly to Early Ages, while the same technology definitions can remain relevant to inherited infrastructure in later starts.

Automation makes a large modern company manageable without removing the underlying physical simulation.

## 29. Competitors and company market

AI transport companies are profit-seeking economic actors.

They have:

- capital,
- vehicles,
- staff,
- contracts,
- costs,
- infrastructure,
- regional presence.

They can grow, shrink, sell assets or fail.

The player's initial competitive exposure is mostly local because the company starts small. The selected historical year determines how developed existing competitors and networks are; a later start must not reset every rival to a tiny early-industrial business. Competition increases naturally as the player's network and active regions connect.

### 29.1 Ownership, control and acquisitions

The player can buy shares in competitors, receive dividends/distributions, acquire controlling stakes or buy companies outright.

Keep **economic ownership** separate from **control/operating authority**.

A minority holding can create investment and governance rights, but it does not automatically let the player spend the target company's cash, move its vehicles, edit its Lines, sell its infrastructure or cancel its contracts.

Control follows the actual ownership/governance rules applicable to that company rather than one universal hard-coded percentage. The UI must show separately:

- ownership percentage/economic interest;
- whether the player currently has control;
- which governance/approval rights follow from that position.

A controlled company can remain a separate **subsidiary** or be integrated into the parent.

#### Controlled subsidiaries

A controlled subsidiary remains its own company identity unless a real integration occurs. It keeps separate:

- cash and debt;
- revenues/costs;
- contracts and agreements;
- licences/permissions;
- staff and managers;
- vehicles and rolling stock;
- infrastructure/land;
- inventories, projects and orders;
- operating history and identity.

The subsidiary remains **AI-managed**. Control does not turn it into a second fully player-operated company.

The player instead has a small set of owner powers:

1. **Broad direction** — simple high-level intent such as grow/maintain/reduce, business/mode focus, preferred expansion region and a broad investment limit where needed.
2. **Owner directives** — concrete strategic/operational outcomes such as create/change/close a Line, change service capacity, expand into a region, build/upgrade a major facility or initiate a major asset action.
3. **Capital and asset transactions** — capital contribution, dividend/distribution, intra-group loan where useful, and explicit sale/lease/transfer of vehicles or infrastructure.
4. **Major company decisions** — material borrowing, acquisitions, major infrastructure sales, top-management changes and optional whole-company integration.

Do not turn these powers into dozens of detailed policy sliders.

An owner directive states the desired result; the subsidiary's management must then satisfy its real prerequisites through the normal systems.

Example:

> Owner directive: change R12 to 30-minute interval.

The subsidiary may need more vehicles, staff, depot capacity and infrastructure slots. It must acquire/replan those resources legitimately before the change can operate.

If a directive cannot currently be fulfilled, keep it blocked/pending with explainable causes rather than cheating or silently ignoring it.

The player may use familiar Line/asset editors to define a directive, but submitting the result does not directly execute every dependent operation on the subsidiary's behalf.

An owner can make a harmful decision where legally/physically valid. Taking a vehicle away from a subsidiary may create a real shortage. The subsidiary then uses the normal dispatcher/market/recovery rules to reorganize, replace capacity, reduce service or surface an unresolved problem.

The parent cannot spend subsidiary cash, and the subsidiary cannot spend parent cash, without a real transaction.

Group-company interaction uses real ledgers, ownership transfers, agreements and capacity. It never teleports assets or erases physical constraints.

A controlled subsidiary's top management uses the existing management/delegation model internally; the player does not separately configure every routine manager rule merely because the company is controlled.

#### Whole-company integration

Integration is optional. It is not required merely to obtain meaningful control over a subsidiary.

Before integration, the player must see the consequences for:

- assets and infrastructure;
- staff;
- cash/debt;
- contracts/leases;
- licences/permissions;
- Lines/services;
- projects/orders;
- inventories;
- non-transferable or change-of-control obligations.

Integration transfers only what the applicable rules permit.

Physical vehicles/assets remain in their actual locations; running Trips, cargo, construction and maintenance do not reset or teleport.

Contracts and licences that require consent, recognition or reapplication remain explicit dependencies rather than being silently rewritten.

The acquired company's historical identity remains inspectable after integration.

Companies can also own industrial firms or other business assets, but direct factory-building is not a primary early-game focus.

## 30. Carrier cooperation and external transport procurement

Transport companies can be both competitors and partners.

Recurring partnership and subcontracting frameworks can use Auto-renew under Section 11.12. Their renewal preserves the distinction between purchased transport/seat capacity and non-transferable infrastructure slots; it does not transfer a partner's rail or station slots to the player.

### 30.1 One External Transport Order system

The game has **one shared system for buying transport services from another carrier/provider**: the **External Transport Order**.

Do not create separate transport marketplaces for:

- subcontracting a customer's cargo leg;
- moving purchased vehicles;
- specialized heavy-haul transport;
- hiring a carrier to collect purchased fuel/materials;
- other one-off external physical transport needs.

Different screens may offer contextual actions such as **Arrange delivery**, **Hire carrier**, **Find subcontractor** or **Order heavy haul**, but these actions all open the same External Transport Order flow with the relevant fields pre-filled.

The canonical order contains, as applicable:

- what is being transported;
- quantity / number of physical assets;
- origin and destination;
- earliest pickup / required delivery window;
- transport mode(s);
- special equipment or handling requirements;
- dimensions/weight/hazard/temperature constraints;
- SLA/deadline;
- whether recurring service is required;
- responsibility for loading/unloading, permits and escort;
- insurance/liability requirements.

The system then shows compatible providers and offers using their real capabilities and finite capacity.

For each offer, the UI can show:

- provider;
- price;
- earliest pickup;
- estimated arrival;
- equipment/capacity used;
- reliability/history where known;
- important conditions/exclusions;
- whether the order is one-off or part of an existing framework agreement.

The player chooses one offer and signs one transport-service agreement. The order then becomes a real physical movement or sequence of movements.

Provider availability is not fabricated for convenience. If no suitable carrier/equipment is available in time, the order can remain unfulfilled, require a later date or require a different transport solution.

The same procurement engine supports ordinary carriers and specialized transport firms. A heavy-haul company is therefore not accessed through a separate marketplace; it appears as a compatible provider only when the order requires its specialist equipment.

Contextual screens may hide irrelevant advanced fields, but they must not implement separate pricing, provider-capacity or booking logic.

### 30.2 Cargo subcontracting

A customer may contract the player for an end-to-end move, while parts are subcontracted to other carriers.

One-off subcontracted transport is purchased through the External Transport Order in Section 30.1. Repeated cooperation can instead use a framework/reserved-capacity agreement that the same procurement flow can reference.

Cooperation can range from:

- one-off subcontract,
- framework partner agreement,
- reserved partner capacity,
- integrated network cooperation.

Cargo transfer remains physical through real terminals/storage.

The prime contractor remains responsible to the customer and can seek SLA compensation from a failing subcontractor.

### 30.3 Passenger cooperation

Passenger cooperation is based on fixed services and seats.

#### Bilateral cooperation agreement builder

Company-to-company passenger cooperation uses one **bilateral agreement builder** rather than a separate hard-coded form for every possible partnership.

The agreement has two explicit party columns:

> **Our company** | **Partner company**

The player composes the proposal by enabling the supported cooperation clauses and setting the values that belong to each side. Clauses may be asymmetric: one party can grant a right or accept an obligation that the other does not.

This is a structured clause builder, not free-form legal text. Every clause maps to an existing canonical simulation mechanic and must have defined validation/consequences.

A submitted proposal can be accepted, rejected or countered by the other company. A counterproposal changes explicit clause values; it does not invent hidden terms.

For V1 passenger cooperation, **partner-capacity sales** is defined here and allows either or both parties to sell eligible capacity operated by the other party as part of one through ticket.

**Connection-agreement mechanics are intentionally reset and not specified here.** They remain required V1 design work and will be redesigned from scratch in [CONNECTION_AGREEMENTS.md](CONNECTION_AGREEMENTS.md). Do not infer their lifecycle, timetable coordination, frequency, protection, activation or termination rules from prior drafts.

A through journey can use multiple operators under one itinerary/ticket when the required partner-capacity sales right exists.

#### Partner capacity settlement

The partner-capacity-sales clause is configured **independently for each side of the bilateral agreement**.

For each direction, the agreement shows:

- whether that side may sell the other company's capacity;
- the specific eligible Lines covered by that right;
- the partner rate in money/km owed to the operating carrier.

The two directions are therefore separate:

- **Partner sells our capacity** → selected player-company Lines + rate owed to us per km;
- **We sell partner capacity** → selected partner Lines + rate owed to the partner per km.

Either direction can be enabled or disabled independently. The selected Line sets and rates do not have to match.

The Line scope is explicit and versioned with the agreement. Selecting **all current Lines** is allowed as an editing convenience, but it stores the current concrete Line set; a future newly created Line is not silently added to the agreement without an amendment.

Keep retail price and settlement price separate:

- the passenger-facing price of the partner segment is derived from the operating carrier's applicable public retail tariff;
- the selling carrier owes the operating carrier the agreed partner rate multiplied by the covered distance;
- the difference between retail revenue for that segment and the partner settlement is the seller's margin.

The margin may be positive, zero or negative.

Example:

> Public retail rate: 0.50 money/km  
> Partner rate: 0.40 money/km  
> Covered distance: 150 km  
> Passenger pays for partner segment: 75 money  
> Seller owes partner: 60 money  
> Seller margin: +15 money

A deliberately unfavourable deal is valid:

> Public retail rate: 0.50 money/km  
> Partner rate: 0.55 money/km  
> Covered distance: 150 km  
> Passenger pays for partner segment: 75 money  
> Seller owes partner: 82.5 money  
> Seller margin: −7.5 money

Do not silently block a negative-margin agreement. The player may accept it for strategic/network reasons after seeing the consequence.

AI negotiation of the partner rate should remain explainable and relatively simple. Inputs can include:

- relationship/reputation;
- whether the parties compete strongly on the relevant market;
- expected passenger volume/value brought by the seller;
- strategic interest in the connection/market;
- current commercial leverage/capacity pressure.

Do not turn this into a separate revenue-management or negotiation minigame.

Partner settlement creates a real inter-company payable/receivable and must post exactly once. Settlement/accounting timing follows the normal agreement/finance rules; do not create a second hidden passenger ledger.

Connection agreements, once redefined, remain conceptually separate from partner-capacity sales.

Missed connections and reliability influence passenger attractiveness.

## 31. Pricing, integrated tariff systems and passenger tickets

Passenger retail pricing is based on reusable **tariffs and ticket products**, not a manual fare table for every origin-destination pair.

Keep three concepts separate:

1. **Tariff** — reusable fare-calculation rules such as base/minimum fare, distance or zones, class modifiers and permitted supplements/discounts.
2. **Integrated tariff system** — a named commercial network containing selected Lines/Service Patterns that share a tariff and accept defined ticket products.
3. **Ticket product** — what the passenger actually purchases, such as a single journey, weekly network ticket or monthly network ticket.

An integrated tariff system is not a Line, Service Pattern, Trip, infrastructure owner, region or capacity pool. Membership does not create vehicles, slots, stations, passenger demand or protected connections.

### 31.1 Tariff hierarchy and inheritance

A company/division can define one or more default passenger tariffs for a mode/service family.

A Line normally inherits its applicable company/division/mode tariff.

Where a Line participates in an integrated tariff system, the system's shared tariff applies to products covered by that system. The normal hierarchy is therefore:

1. company/division/mode default tariff;
2. integrated-system tariff where the Line/product belongs to that system;
3. Line-specific override for standalone/non-integrated pricing where explicitly enabled;
4. Service Pattern or passenger-capacity-zone/class modifier only where a real product difference requires it.

The UI must always show whether a price/rule is:

- inherited from a company/division default;
- defined by an integrated system;
- manually overridden on the Line;
- constrained by a public contract/concession/regulation;
- manager-controlled within player-defined bounds.

Inherited values remain references, not copied numbers. Changing a company-level inherited rate updates all inheriting systems/Lines from the effective date; explicit overrides remain unchanged. Before applying a broad change, show the affected systems/Lines and sold-product consequences.

A Line can participate in more than one accepted ticket-product scope where explicitly configured, for example a local integrated system and a broader company-wide network pass. Products are accepted explicitly; discounts are not stacked automatically.

Regulated prices, public-service caps, passenger-group/customer contract prices and already sold retail entitlements cannot be overridden retroactively by this hierarchy.

### 31.2 What a tariff defines

A tariff contains a small number of understandable rules rather than hundreds of pairwise fares.

Depending on mode/era, it can define:

- base/minimum fare;
- distance-based rate;
- zone-based rule;
- class/comfort multipliers;
- premium/reservation supplements;
- advance-purchase discount policy;
- last-minute/load-factor adjustment where technology permits;
- regulated concession categories where applicable;
- refund/flexibility conditions where supported;
- public-contract/concession minimum/maximum constraints.

The fare for an actual single journey is calculated from the applicable tariff and the passenger's real covered itinerary.

The player does not manually enter every origin-destination pair.

For distance-based pricing, tariff distance is derived from the actual valid commercial itinerary/route definition used for the priced journey. Do not use straight-line geographic distance or retroactively charge passengers for disruption detours. If a permanent route change materially changes tariff distance, it applies only to new eligible sales from the configured effective time.

### 31.3 Integrated tariff systems

The player can create named **integrated tariff systems** and add selected passenger Lines/Service Patterns to them.

A system can include multiple company modes, such as regional rail and connecting buses, when the services and sales/reservation capabilities support the product.

A system defines:

- participating Lines/Patterns;
- effective date/version;
- covered modes/classes/zones;
- shared tariff rules;
- accepted ticket products;
- transfer validity/rules;
- explicit supplements/exclusions;
- applicable sales/checking/reservation capabilities.

A shared kilometre or zone rate is one authoritative system value. It is not copied independently into every member Line.

A system can inherit some parameters from the company default and override others.

For an integrated single journey, the fare is calculated across the covered itinerary under one system rather than charging a new full base fare at every covered transfer. Any base charge applies once to that integrated journey unless the published product explicitly defines another rule. Premium supplements remain possible when clearly disclosed.

Example:

> Regional Network  
> 2 rail Lines + 4 bus Lines  
> shared rate: 0.5 money/km  
> covered itinerary: 12 km rail + 8 km bus  
> distance component: 10 money

This example is illustrative balancing only.

An integrated fare does **not** automatically create a protected connection. Protected itinerary/rebooking rights remain governed by Section 32.4 and require the relevant through-ticket/connection policy.

### 31.4 Ticket products

Each tariff/system can offer one or more passenger ticket products.

Required baseline products include:

- **Single journey** — one covered journey under the applicable fare rules;
- **Weekly ticket** — repeated eligible travel in its defined scope for **7 game days**;
- **Monthly ticket** — repeated eligible travel in its defined scope for **14 game days**.

The player can set weekly/monthly products cheaper than repeated equivalent single fares. Their price is independently configurable; the game must not force a fixed discount percentage.

The same framework can also support, where the player chooses and the era/rules allow:

- daily/time-limited products;
- route-limited passes;
- zone-limited passes;
- class-specific products;
- company-wide network products;
- integrated-system products.

A company-wide default tariff is not automatically a company-wide unlimited ticket. A broad network pass is a separate ticket product with its own price and acceptance scope.

Each product defines:

- name;
- selling tariff/system;
- network/Line/zone scope;
- eligible passenger class/capacity categories;
- price;
- validity rule;
- supplements/exclusions;
- transfer conditions;
- reservation requirements/supplements;
- refund/change conditions.

A period ticket permits repeated covered journeys during its validity. It is not merely a discount card that charges the base fare again on every boarding.

### 31.5 Period-ticket validity

Use the shared game calendar from Section 3.

Baseline validity is elapsed game time from the ticket's selected start:

- weekly = exactly 7 game days;
- monthly = exactly 14 game days.

Do not use 30/31-day civil months or wall-clock time.

The ticket stores:

- product/version purchased;
- actual purchase price;
- validity start;
- validity end;
- covered scope/classes;
- relevant terms at sale.

A period ticket must be valid **when the passenger boards each covered Trip**.

If it expires while the passenger is already physically travelling on that Trip, that Trip remains covered through the passenger's booked/alighting stop. A later transfer boarded after expiry requires another valid entitlement unless the passenger holds a separate still-valid single integrated journey whose transfer rules cover it.

This prevents a ticket from becoming invalid halfway between two stations while still preserving a precise expiry boundary for later boardings.

Alternative first-use or fixed-calendar-period products can be added only as explicitly separate products; do not silently reinterpret weekly/monthly tickets.

### 31.6 Overlapping valid products and fare charging

A passenger can hold more than one valid product.

When boarding/pricing a leg:

1. identify already held products that validly cover the leg/class;
2. if one covers the base fare, do **not** sell another base fare for the same leg;
3. charge only an explicitly required uncovered supplement/reservation/service component;
4. if no held product covers the journey, evaluate available eligible products/single fare according to the passenger-choice model.

Do not stack multiple percentage discounts or charge two full fares because two systems overlap.

If several held products cover the same leg equally, no extra payment is created merely to choose between them; record the entitlement source deterministically for audit/reporting, preferring the product specifically associated with the booked itinerary when one exists, otherwise a stable product-priority rule.

At purchase time, the passenger-demand system can compare eligible ticket products using expected travel needs, price and alternatives. It must not know future random events or buy a period pass using perfect future information.

### 31.7 Travel entitlement is not capacity

Owning a valid ticket/pass does not create physical passenger capacity.

A period ticket:

- pays for covered travel;
- does not reserve a seat/berth/standing place on every future Trip;
- does not guarantee that a full open-boarding vehicle will admit another passenger;
- does not override protected passenger-contract or confirmed-reservation capacity.

Where a capacity zone is **reservation required**, a pass holder still needs confirmed compatible capacity for the selected Trip/leg. The base fare can already be covered by the pass; only any separately published reservation/supplement component remains payable.

For **optional reservation**, the pass can be combined with a specific reservation where capacity exists.

For **open boarding**, the pass holder boards only if eligible physical capacity remains.

Reservation and ticket entitlement use the same passenger-capacity ledger as other passengers; no duplicate capacity is created.

### 31.8 Sales, validation and historical technology

A product can be sold only through sales channels the company/infrastructure actually provides under Section 32.

A simple own-company common tariff or paper season ticket can exist in early eras where period-appropriate administration, sales and checking are available. It does **not** require online technology.

However, technology affects:

- geographic sales reach;
- advance purchase;
- ability to verify reservations across the network;
- speed of product validation;
- centralized account/entitlement handling;
- multi-operator integration;
- dynamic/yield pricing.

A station without a sales channel does not magically sell a pass. A passenger already holding a legitimately purchased valid pass can still use it where period-appropriate inspection/validation is supported; that does not create a modern real-time reservation system.

### 31.9 Changes, versions and sold-ticket protection

Tariff systems and ticket products are versioned with explicit effective dates.

Changing:

- a system rate;
- participating Lines;
- included class;
- ticket price;
- validity;
- supplement;
- transfer rule;
- sales/acceptance scope

creates a future product/system version when existing sold entitlements could be affected.

Already sold tickets retain the price, validity and rights promised by the purchased version.

Removing a Line/class or shortening future product validity must not silently revoke already sold valid rights. Before publication, show:

- number/aggregate of outstanding affected entitlements where known;
- existing reservations;
- effective date;
- whether old products will continue to be honoured until expiry;
- any required replacement/refund plan;
- affected Lines/systems/public contracts.

The default is to **honour sold period-ticket rights until their individual expiry** on services that remain physically/legal operable. If the operator removes or cancels the covered service such that the promised entitlement cannot reasonably be honoured, apply the existing passenger rebooking/refund rules; additional compensation remains separate.

Do not apply infrastructure-capacity cancellation formulas from CONTRACT_CANCELLATION.md to retail passengers.

### 31.10 Revenue and reporting

A ticket/product sale creates **one actual payment**.

A pass-covered boarding does not create another full fare payment.

Financial and Line/system reports distinguish:

- direct single-journey ticket revenue;
- weekly/monthly/other pass sales;
- reservation/premium supplements;
- refunds;
- compensation;
- analytical allocation of pass revenue to used Lines/services where the reporting model provides it.

Analytical allocation is not another cash receipt.

Where usage information is limited by historical technology, do not fabricate exact pass-by-Line utilization. Use only observations the company can credibly obtain. Finance must preserve one cash posting even if management reports allocate that sale analytically across several Lines.

The UI can compare a period product against equivalent single journeys for an example route/travel pattern, but must not claim a universal savings percentage or guaranteed demand effect.

### 31.11 Fixed, advance and dynamic pricing

A tariff can use increasingly sophisticated pricing modes where historically/technologically appropriate:

- **Fixed** — stable calculated fare independent of booking time/load;
- **Advance** — predefined discounts/surcharges based on booking horizon;
- **Dynamic / yield** — price can also respond to sold load factor, demand forecast and remaining time.

The player can always keep pricing simple.

Advanced real-time yield pricing requires suitable reservation/information technology and is not available merely because the calendar year is modern.

Later, pricing can be delegated to commercial managers by scope:

- division;
- region;
- integrated tariff system;
- group of Lines;
- specific Line/service.

Managers optimize only within player-defined tariff bounds such as:

- minimum/maximum fare;
- maximum last-minute premium;
- target occupancy;
- minimum margin;
- permitted discount range.

A manager cannot override a regulated fare, public-contract cap, sold ticket right or explicit player lock.

### 31.12 Public/urban fares and integrated systems

Urban/public transport can use the same tariff/product framework, but city/concession rules may impose:

- flat fares;
- zones;
- transfer validity;
- fare caps;
- mandatory concession categories;
- required acceptance of specified public ticket products.

Where the city controls the fare, the player's participating Lines inherit/accept the allowed tariff/product rules and cannot use unrestricted yield pricing.

A municipal integrated system can therefore include several player Lines or, where an actual cooperation/authority agreement exists, services from several operators. The authority agreement owns the permitted products and settlement/acceptance terms; the player cannot unilaterally declare competitors' Lines part of its system.

### 31.13 Contract passenger pricing

Commercial passenger/group contracts under Section 11.1.1 use their negotiated contract price and do not automatically pay the public individual-passenger tariff.

When a contract reserves capacity on a normal Line, the capacity ledger is shared, but the commercial payment remains the contract's agreed price.

If contract passengers also hold public/retail products, do not create duplicate fare revenue; the contract terms determine the applicable commercial settlement.

### 31.14 Multi-operator tariff integration

Multi-operator integrated fares are allowed only through an actual cooperation/authority agreement under Sections 30.3/33.

Such an agreement can define:

- participating operators/Lines;
- accepted products;
- sales responsibility;
- reservation compatibility;
- revenue settlement/allocation;
- refund/rebooking responsibility;
- data/information capability;
- validity/renewal/termination.

The player cannot add another operator's service to its own pass merely because the services connect.

The exact settlement formula is agreement/content data, not a hidden universal percentage. Each operator receives only the settlement defined by the agreement, and passenger retail payment must not be double-counted as full revenue by every participant.


## 32. Service lines and timetables

A Line is a reusable operating service, not a synonym for a customer contract.

The player can create ordinary **commercial intercity passenger or freight Lines independently of a contract** when all required conditions are satisfied, including:

- commercial coverage/local presence;
- relevant operating licence;
- valid service endpoints/stops;
- infrastructure/station/terminal access;
- required capacity/slots;
- fleet;
- staff;
- operating/depot/maintenance coverage.

A commercial Line then earns revenue from simulated passenger/cargo demand and can later carry contract allocations as described by the Transport Plan in Section 11.0.1.

Regular passenger lines are available from the start where the above requirements are met, and freight services can use either scheduled or demand-driven operating patterns.

On a low-demand local market, low frequencies and small vehicles may be the only profitable choice. Actual demand depends on the selected year, region and service quality; a newly started company in 1975 does not imply universally low demand in its world.

The player can also use demand-driven departure policies, e.g.:

- depart when X passengers are booked,
- depart when minimum cargo load is reached,
- depart when a contracted shipment is ready,
- or after a maximum wait time.

Over time, demand growth supports more frequent and higher-capacity scheduled services.

### 32.1 Service hierarchy: Line → Service Pattern → Trip

All scheduled transport uses a three-level hierarchy:

1. **Line** — the commercial/operational corridor or service family the player manages as one unit.
2. **Service Pattern** — a specific operating variant of that line: route, stop pattern, calendar, vehicle requirements and service rules.
3. **Trip** — one concrete physical movement on a specific date/time using real assigned vehicles/consists.

Example:

- Line: R1 Praha–Brno
  - Pattern: Local — serves all selected intermediate stops
  - Pattern: Express — serves only major stops
  - Pattern: Short-turn — terminates at an intermediate point
  - Pattern: Night/seasonal — different calendar and consist rules
- Trips: the actual 06:00, 08:00, 10:00 departures generated from those patterns.

Lines aggregate business and operating performance across their patterns. Patterns remain individually inspectable for profitability, occupancy, reliability, fleet demand and timetable quality.

The same hierarchy applies to passenger and freight services. Freight patterns can differ by cargo focus, stop logic or demand-driven departure rules.

A Service Pattern should still meaningfully belong to its parent Line. If a proposed variant shares too little route, purpose or operating identity with the parent, the UI should recommend creating a separate Line instead of allowing one line to become an arbitrary container for an entire network.

### 32.2 Service calendars

A line can contain multiple repeating service patterns instead of one permanent timetable.

Each service pattern can define:

- validity period/date range,
- days of week,
- exact departure times and/or repeating intervals,
- time-of-day windows,
- capacity/vehicle requirements,
- optional departure conditions for demand-driven freight/passenger services,
- exceptions such as holidays, temporary closures or special-event service.

Use the 14-day-month calendar in Section 3 for every pattern and exception. Each month contains two complete seven-day weeks. Seasonal patterns, cross-year date ranges and slot orders must agree on the same game dates; no pattern can reference a nonexistent day 15–31.

Where the service uses constrained third-party rail/station infrastructure, the same calendar can be passed directly into the Capacity Order editor to request only the capacity needed for those dates/times. Seasonal patterns therefore do not require year-round slot purchases.

Example patterns can include weekday, weekend, summer, winter or harvest-season service.

Low-volume services can use sparse exact departures such as Monday/Thursday or one/two departures per day. High-frequency rail/urban services can use interval-based patterns when justified by the selected era, demand and operating resources.

Service calendars must respect actual physical fleet availability. Before activation, the planner calculates the number and type of vehicles/consists required from real cycle times, turnaround, depot movements and maintenance assumptions. If the fleet cannot cover the timetable, the game must explain the shortage rather than creating abstract vehicles.

Before activation, each commercial Service Pattern must also have valid service endpoints under Section 12.4, any required station/terminal/stop access, and commercial coverage/local presence under Section 7.2 for every served city. A vehicle cannot run a commercial Trip to an abstract destination with nowhere to board/load/unload or to a city the company is not yet organizationally allowed to serve. Pass-through locations do not create this requirement.

Timetable templates may later be reused across multiple lines, with local overrides. Managers/dispatch systems can suggest frequency changes based on observed demand, but player overrides remain possible.

#### Service Pattern versions and effective dates

A running Service Pattern is **versioned** rather than edited destructively in place.

When the player changes a materially operational parameter of an active Pattern, the planner creates a **new future version** with an explicit **effective date/time**.

Material changes include, for example:

- stop pattern;
- route/corridor;
- departure frequency;
- timetable/slot pattern;
- operating days;
- vehicle/consist requirement, pinned assets or assignment criteria;
- passenger-capacity configuration;
- reservation policy;
- operating depot where it changes real movements;
- major dwell/turnaround rules.

The currently active version continues operating until the transition point.

Example:

> Pattern v3 — active until 5 May, 23:59  
> Pattern v4 — effective 6 May, 00:00

The player can prepare and validate v4 while v3 continues running normally.

##### Pre-activation impact check

Before a new Pattern version can become active, the Line Planner revalidates all dependencies affected by the change.

The impact check includes:

- route/infrastructure access;
- rail/station capacity slots;
- vehicle/consist requirement;
- fleet availability and repositioning;
- crew/staff requirement;
- depot/parking/maintenance capacity;
- commercial coverage/local presence;
- passenger ticketing/sales availability;
- passenger reservations and protected itineraries;
- freight contract allocations;
- passenger/group contracts;
- feeder/connection relationships;
- tariff/reservation-policy compatibility where relevant.

The UI should summarize concrete impacts, for example:

> **Pattern v4 from 6 May**  
> 2 new rail capacity orders required  
> 2 old capacity reservations can be released  
> 14 passenger reservations affected  
> 11 can be rebooked automatically  
> 3 require refund or manual policy decision  
> Contract A remains feasible  
> Contract B loses required frequency  
> Fleet requirement changes from 4 to 5 trainsets

A future version cannot be marked **Ready for activation** while a hard blocker remains unresolved.

##### Rail/station slot transition

A timetable change does not automatically rewrite existing infrastructure agreements.

The new Pattern version must secure its required rail/station capacity through the existing Capacity Order system.

Old capacity remains tied to the old Pattern version until:

- the old version expires;
- the player releases it early under the access agreement;
- or a coordinated amendment/replacement is explicitly agreed.

Any cancellation/release fee follows the existing capacity-cancellation rules; versioning does not waive contractual obligations.

This allows a safe overlap period where the company can secure new slots before giving up the old ones, at the cost of temporarily paying for both where necessary.

##### Passenger reservations, rebooking and refunds

When future passenger reservations have already been sold for dates after the new version's effective date, the planner compares them against the replacement timetable/capacity.

For each affected booking, the system first attempts automatic migration/rebooking where the promised journey remains reasonably satisfiable.

Examples:

- departure moved by 4 minutes but the same protected itinerary remains valid → migrate automatically;
- one stop removed → affected passengers require rebooking or refund;
- First Class capacity reduced below already sold reservations → unresolved capacity conflict requiring re-accommodation or refund;
- connection window becomes invalid → itinerary must be reprotected/rebooked or refunded.

If no acceptable replacement itinerary exists, the operator can **refund the affected ticket/reservation**.

Refund handling is aggregate; the player does not manually process individual passengers.

Depending on the fare/product and disruption policy, the system can use:

- **automatic rebooking first, refund if impossible**;
- **offer rebooking or refund** where passenger choice is modeled;
- **automatic full refund** when the operator cancels the promised service and no equivalent journey exists.

The refund returns the fare amount covered by the affected ticket/product according to its tariff rules.

Any additional delay/cancellation compensation is separate from the refund. If the operator caused the disruption and the applicable tariff, public-service contract or jurisdiction rules provide compensation, the player can owe both:

- refund/re-accommodation cost;
- additional compensation/credit.

The impact screen shows aggregate:

- passengers/bookings affected;
- automatically migrated;
- automatically rebooked;
- requiring refund;
- estimated refund value;
- estimated additional compensation.

Once a future version is published for sale, new reservations for dates on/after its effective date use that future version rather than the currently active timetable.

##### Freight and passenger contracts

Contracts are not automatically rewritten when a Pattern changes.

Every Transport Plan allocation pointing to the Pattern is revalidated against the new version.

The planner checks:

- required origin/destination stops still exist;
- required frequency/capacity remains available;
- SLA/timing remains feasible;
- reserved passenger/freight capacity still exists;
- transfers to other legs remain feasible.

If a contract becomes infeasible, activation is blocked or explicitly flagged as a contractual breach risk until the player changes the Pattern, reallocates the contract to another service or accepts the commercial consequence where contract terms allow it.

##### Transition of Trips

Use the Trip's **scheduled origin departure timestamp** to select the Pattern version, not its generation time or delayed actual departure. Trips scheduled before the boundary retain the old version even if they depart late. Trips scheduled at or after the boundary use the new version.

Already generated future Trips, tickets, allocations and preparation tasks on the replaced version must be explicitly migrated/revalidated or cancelled/recovered. Old and new generation must not create duplicate occurrences. Preparatory movements and loaded cargo cannot be undone by deleting an object.

A Trip already running keeps its original version and obligations; it is never rewritten mid-journey. Suspension/emergency actions remain separate from version selection.

The UI keeps prior Pattern versions available for audit/history but only the current/future relevant versions participate in planning.

#### Line and Service Pattern suspension / closure

A running regular service has explicit lifecycle actions rather than being deleted from the simulation.

The player can:

1. **Suspend Service Pattern** — temporarily stop one Pattern while the parent Line remains active.
2. **Suspend Line** — temporarily stop all active Patterns belonging to that Line.
3. **Close Service Pattern** — permanently end one Pattern.
4. **Close Line** — permanently end the Line and all remaining active/future Patterns.

Suspension can be either:

- **scheduled** — start/end date is known in advance;
- **until further notice** — no planned restart date.

A Line/Pattern in **Suspended until further notice** remains a real company object with its history, configuration and dependencies, but cannot start a new commercial Trip while suspension is effective. Stop future generation/sales and explicitly cancel or replan already generated but not departed affected Trips, including delayed departures. Resolve preparation, loaded quantities, reservations and obligations through the impact check; do not only disable the generator and allow its old queue to dispatch.

A Trip that has already departed before suspension takes effect completes under its existing plan unless a separate emergency/cancellation action explicitly terminates it.

##### Suspension impact check

Suspension uses the same dependency/impact philosophy as Pattern versioning.

Before confirmation, the UI shows the effect on:

- future passenger reservations;
- protected itineraries/connections;
- passenger/group contracts;
- freight contract allocations;
- municipal/public-service obligations;
- rail/station capacity agreements;
- vehicle/fleet utilization;
- crew/staff demand;
- feeder/connection Lines;
- depot/parking demand;
- expected refunds/compensation;
- reputation/customer impact where relevant.

Example:

> **Suspend Line R12 from 8 May — until further notice**  
> 74 passenger reservations affected  
> 61 can be rebooked automatically  
> 13 require refund  
> 2 passenger contracts require replacement transport  
> 6 rail/station capacity reservations affected  
> estimated refunds: X  
> estimated contractual exposure: Y

Commercial Lines can generally be suspended/closed at the player's discretion after accepting these consequences.

A municipal/public-service or other contracted Line may be blocked from suspension where the governing contract/concession does not permit it. The player must first arrange replacement service, obtain agreement, terminate/renegotiate the contract or explicitly accept a breach where the rules allow that action.

##### Passenger handling during suspension/closure

Future ticket sales for affected Trips stop once the suspension/closure is committed and published.

Existing affected bookings are handled in this order:

1. migrate to an equivalent surviving Pattern/Trip where possible;
2. rebook to another valid itinerary;
3. use a permitted partner/replacement service;
4. refund when no acceptable replacement exists.

Refund and compensation use the rules in the Service Pattern versioning and passenger-recovery sections.

Closing/suspending a Line does not silently delete already sold passenger obligations.

##### Freight and contract handling

Freight/customer allocations attached to an affected Pattern/Line are revalidated.

The planner can move the relevant Transport Plan leg to:

- another existing Line/Pattern;
- a temporary/ad-hoc own movement;
- an external carrier;
- another valid transport solution.

If no solution preserves the contract terms, the player is shown the expected SLA/breach/termination consequences before confirming suspension/closure.

##### Infrastructure capacity during suspension

Suspending a service does **not** automatically cancel its rail/station capacity agreements.

For each affected recurring capacity agreement, the player chooses or follows an authorized policy to:

- **Keep reserved capacity** — continue paying reservation charges so restart can reuse the protected slots, subject to the agreement;
- **Release/cancel capacity** — return it to the infrastructure owner under the existing cancellation rules and pay any applicable cancellation fee;
- **Reduce/amend capacity** — where the owner offers a temporary lower commitment.

For a short scheduled suspension, keeping slots can be rational.

For **Suspend until further notice**, the UI must explicitly surface the ongoing cost of retaining unused protected capacity and recommend reviewing whether to release it. It must not silently keep years of expensive slots nor silently cancel them.

If capacity is released, the service has no right to reclaim the same slots later.

##### Reopening a suspended service

A suspended Line/Pattern never resumes merely because the player toggles a switch.

The player chooses **Resume service**, after which the Line Planner performs a fresh readiness check using the intended restart date.

It revalidates:

- route/infrastructure availability;
- required rail/station slots;
- city/operating permissions;
- licences;
- endpoints/stops;
- fleet and consist;
- vehicle physical locations/repositioning;
- crew/staff;
- depot/parking/maintenance;
- ticket-sales channels;
- contracts/allocations;
- connections;
- current timetable feasibility.

If previously retained slots remain valid, they can be reused.

If slots were released or expired, new Capacity Orders are required and the new timetable can differ from the old one.

A long suspension can therefore make restart materially different because:

- infrastructure changed;
- competitors acquired former slots;
- vehicles were reassigned/sold;
- licences/permissions changed;
- demand shifted.

The old Line/Pattern configuration is retained as a starting proposal, not treated as guaranteed current feasibility.

##### Permanent closure

Permanent closure preserves operating history and financial/statistical records but ends future service generation.

Closing a Line does not automatically:

- sell its vehicles;
- demolish stations/depots;
- cancel unrelated contracts;
- sell infrastructure;
- dismiss staff.

Those resources return to their normal pools/ownership state and can be reassigned or disposed of separately.

Any capacity agreements, passenger bookings and contracts affected by permanent closure must be explicitly resolved through the same systems above.

#### Passenger ticket sales and reservations

Ordinary individual passenger demand is monetized through **ticket sales**, not customer contracts.

For each candidate journey, the passenger-demand system chooses among available itineraries/operators based on the existing factors in Section 6.2, then attempts to purchase/use the required capacity.

Passenger sales are aggregated but capacity-accurate by:

- Trip;
- origin-destination leg;
- passenger class/capacity zone;
- reservation policy;
- protected multi-leg itinerary where one is sold.

A passenger place sold Praha→Brno does not block the same place Brno→Vídeň.

When a ticket covers several connecting Trips, the system can reserve compatible capacity on each required leg and mark the journey as a protected itinerary under Section 32.4.

##### Open boarding

For open-boarding services, passengers arrive according to simulated demand and join an aggregated **waiting queue** at the relevant stop/station until they board, choose another option or abandon the journey.

When a compatible Trip arrives, waiting demand boards subject to:

- intended destination/itinerary;
- passenger class/product compatibility;
- reservation priority where applicable;
- actual seated/standing capacity of the arriving vehicle/zone.

If capacity is exhausted:

- remaining passengers stay in the queue for a later suitable service where feasible;
- choose another operator/mode/route;
- or abandon the trip.

Queue state remains physical to the stop/station. Passengers denied boarding do not disappear and reappear elsewhere.

Repeated denied boarding and long waits reduce the attractiveness of that service through the already visible passenger factors such as waiting time, frequency, crowding and reliability perception.

The stop/station UI should expose useful aggregate queue information, for example:

> Waiting now: 420 passengers  
> Next compatible Trip capacity available: 310  
> Expected left behind after departure: ~110

Where demand is split across several destinations/classes/services, the UI can show the relevant grouped breakdown without listing individual passengers.

This is the default model for much urban/local transport.

##### Optional advance sale

For optional-reservation capacity, passengers can buy confirmed capacity before departure.

The remaining unreserved capacity stays available to later purchasers/walk-up demand until the applicable sales cutoff.

The Line/Trip UI can therefore show, by leg and class:

> Capacity: 220 seated  
> Reserved/sold in advance: 147  
> Forecast additional demand: 51  
> Currently uncommitted: 73

The player does not manage individual reservations.

##### Reservation-required capacity

A reservation-required zone accepts only passengers with confirmed available capacity for the relevant Trip/leg.

This can be configured for only part of a consist, such as First Class, sleeper cars or another premium section, while other coaches remain optional/open.

##### Passenger tariff application

Ordinary passenger tickets use the tariff system in Section 31.

The default is:

- inherit the company/division/mode tariff;
- optionally enable a **Line-specific override**;
- apply the relevant passenger class/capacity-zone modifier;
- calculate the fare automatically for the actual origin-destination legs.

The player therefore edits a tariff, not a matrix of every station pair.

The applicable tariff can still use inputs such as:

- distance/zone;
- passenger class;
- time until departure;
- sold load factor;
- expected demand;
- day/time/season;
- flexibility/refund conditions where supported;
- competitive alternatives.

This allows advance-purchase discounts or higher last-minute pricing where historically/technologically appropriate.

The player can keep a Line on simple fixed pricing or manually tune its tariff independently of other Lines.

More advanced yield-style pricing can be delegated to commercial management later.

Technology matters: sophisticated real-time/digital pricing should not exist before the company has the required information/reservation systems.

##### Passenger ticket-sales channels

A passenger Line can only sell tickets/reservations through **sales channels the company or infrastructure actually provides**.

Ticketing is not automatically available everywhere a vehicle stops.

Supported channels can include:

1. **Branch sales desk** — a company branch with a ticketing/sales upgrade.
2. **Station/terminal ticket office** — a passenger station/terminal with a compatible booking-sales module and an access/sales agreement where the player does not own the facility.
3. **Onboard conductor / crew sales** — tickets sold after boarding or immediately before/at departure by eligible onboard staff.
4. **Telephone/central reservation sales** — unlocked by the appropriate company communications/reservation system.
5. **Automated/self-service sales** — station machines or other automated channels where historically available and installed.
6. **Online/digital sales** — unlocked only after the company adopts the required modern digital reservation/sales system.

The available mix evolves by era and company technology. A modern calendar year alone does not grant a channel for free.

###### Branch and station sales

A branch or station must have the appropriate **ticketing/booking upgrade** to sell tickets.

The upgrade represents the required counter/office systems, staff workload and period-appropriate equipment. The player does not buy individual ticket printers, telephones or terminals.

Ticket-sales capacity is finite.

A small ticket office can become a bottleneck during peak periods, creating:

- queues;
- longer purchase time;
- missed departures for late-arriving passengers;
- reduced ability to process reservations/complex tickets.

The facility can be upgraded or supplemented by other channels.

A ticket office in a third-party station does not appear automatically. The player needs permission/commercial space or an agreed station sales arrangement.

###### Conductor / onboard sales

Eligible passenger services can allow **ticket purchase from a conductor/onboard staff**.

This is especially useful for:

- regional/local services;
- small stops without a ticket office;
- earlier historical periods;
- passengers boarding where no other sales channel is available.

Conductors/onboard staff are ordinary aggregated workforce under Section 8, not named individuals.

Onboard ticket sale/control is intentionally **abstracted**.

Where onboard staff can physically circulate through the relevant passenger accommodation while the vehicle is running, ticket sale/control does **not** consume additional dwell time.

If a passenger boards without a previously purchased ticket and the Trip carries a conductor/onboard ticket-selling crew, the fare is charged through the applicable onboard tariff/policy while the vehicle is already in service.

Older/non-through passenger stock is the exception: if onboard staff cannot reach the relevant compartments internally while running, conductor-based ticket handling can add aggregated station dwell under the onboard-circulation rules in Section 14.5.

The game does not simulate the conductor walking through individual coaches or checking each passenger separately.

The Line/Service Pattern can define whether onboard sales are:

- allowed;
- prohibited;
- allowed only when no station sales channel exists;
- subject to an onboard surcharge.

An onboard surcharge is part of the tariff policy, not an arbitrary penalty. It can be disabled for stations where no pre-purchase option exists.

For **open boarding**, a passenger can board without a pre-purchased ticket. If a conductor is present, the fare is collected onboard automatically.

For **optional reservation**, a passenger without an advance reservation can use remaining uncommitted capacity. If a conductor is present, the corresponding fare is collected onboard automatically.

For **reservation-required** capacity, the passenger still needs confirmed capacity for that Trip/leg. Onboard sale can create that reservation only when the company system can verify real remaining capacity.

If a passenger boards a service where no conductor/onboard ticket-selling crew is present and no ticket has been purchased beforehand, the operator does **not** collect a fare from that passenger for that journey.

The base design does not add a separate fare-evasion inspection minigame to compensate for this. Services intentionally operated without conductors are expected to be uncommon outside operating models where another pre-boarding/self-service sales system covers most demand.

The system never sells or assigns onboard capacity that has already been reserved/committed elsewhere.

###### Telephone and digital progression

Company sales technology can progressively expand reach:

- local in-person sales only;
- telephone inquiry/booking;
- centralized reservation office;
- automated station sales;
- connected computerized reservation network;
- online/mobile/self-service digital sales.

These systems connect directly to the commercial-coverage technology progression in Sections 7.2 and 28.

Better sales technology can:

- let passengers buy from farther away;
- increase advance-sale share;
- reduce pressure on station counters;
- make reservations across multiple company Lines easier;
- enable more sophisticated pricing/yield management.

It does not create passenger demand by itself.

###### Passenger choice and unavailable sales

A paid journey requires a usable sales channel; a reservation-required zone additionally requires confirmed capacity before boarding. Without a way to confirm that reservation, the reservation-required option is unavailable even if physical space exists.

Do not confuse ticket sales with physical boarding. Open/optional unreserved boarding follows the explicit onboard-sales rule above: an otherwise eligible passenger may board free uncommitted capacity without a pre-purchased ticket, but if no eligible selling crew or other actual payment channel collects the fare, that journey earns no fare. Do not fabricate revenue, a reservation or a fare-evasion minigame. Existing prepaid tickets remain valid and are never charged twice.

The Line Planner must distinguish **Ticket sales unavailable / fare revenue at risk** from **Reservation unavailable / boarding blocked**. Forecast revenue uses actual reachable sales channels and the applicable boarding policy, not the existence of seats alone.

##### Passenger capacity commitments

Passenger-group contracts under Section 11.1.1 and ordinary individual reservations consume the **same physical capacity ledger**.

Capacity priority is:

1. protected passenger-contract allocations;
2. confirmed individual reservations;
3. open/walk-up passenger demand.

These tiers allocate uncommitted capacity; they are not permission to take an already confirmed seat away. A newly accepted group contract must fit around existing confirmed individual reservations, or obtain an explicit re-accommodation/amendment before acceptance. Carrier-caused capacity loss uses the recovery rules rather than silently selling the same seat twice.

Unused contracted capacity can be released according to its contract cutoff rules.

Confirmed individual reservations cannot be silently displaced to sell the seat again at a higher price.

The system must not oversell one physical seat/berth/standing place across overlapping origin-destination legs.

#### Dynamic station dwell

Passenger-stop dwell is **not always one fixed duration**.

The Service Pattern defines a planned **minimum/target dwell** for ordinary timetable construction, while the actual Trip can require more time when real boarding/alighting conditions demand it.

Actual dwell can depend on:

- number of passengers boarding;
- number of passengers alighting;
- vehicle capacity and crowding;
- number/width/layout of usable doors;
- platform/stop passenger-flow capacity;
- accessibility assistance where required;
- baggage/passenger-service handling that physically affects boarding;
- vehicle type and operating mode;
- whether the stop is an ordinary intermediate call or a larger interchange.

Ticket inspection and onboard ticket sales normally do **not** add dwell time when onboard staff can circulate through the passenger accommodation while the vehicle is running.

With older non-through compartment stock, conductor-based ticket handling can add dwell at stops because the staff cannot service the relevant compartments internally in motion. Pre-purchased tickets avoid that additional ticketing work.

Example:

> Planned dwell: 2 min  
> Normal passenger exchange: ~1 min 35 s  
> Heavy exchange this Trip: 2 min 40 s  
> Result: +40 s departure delay

The timetable planner uses the configured target dwell plus reasonable expected passenger-exchange assumptions when constructing the schedule.

The real Trip then uses the actual required dwell, subject to the physical minimum.

A low-demand stop can therefore clear faster than a major interchange, while a crowded urban/suburban stop can exceed its target and create small real delays.

The player does not manage dwell passenger-by-passenger.

Line/Pattern defaults can be overridden for important stops where a deliberately longer planned dwell is useful, for example:

- major interchange;
- crew change;
- scheduled connection protection;
- baggage/service work;
- terminal preparation.

Dwell is distinct from **turnaround**.

- **Dwell** is the time needed for an intermediate commercial/operational stop before the same Trip continues.
- **Turnaround** under the vehicle-duty rules is the transition between one completed Trip and the next Trip, potentially including cleaning, fueling, consist changes and other service preparation.

Passenger exchange throughput is aggregated and event-driven; the game does not need per-passenger doorway simulation to calculate dwell.

#### Slot-driven timetable construction

For constrained rail services, the timetable is built primarily from **compatible infrastructure/station slot windows plus estimated travel time between them**, rather than by independently typing an exact clock time at every station.

The player first defines the intended service, for example:

- operating days;
- desired frequency / interval;
- broad first and last service window;
- required stops;
- target/minimum dwell, with actual passenger-exchange dwell allowed to vary;
- important connections;
- optional preferred time at a key origin/destination.

The planner then breaks the service into consecutive operational legs between station calls.

Each leg receives an estimated **base running time** based on:

- route distance;
- line/infrastructure speed;
- selected vehicle/consist performance;
- gradients and traction constraints;
- stopping pattern;
- expected infrastructure conditions.

The estimate can be represented as a range where appropriate rather than pretending every Trip will take an identical number of seconds.

The published/planned running time can then include a separate **running-time recovery margin** under the rules below.

The timetable planner then searches for a **continuous sequence of compatible time windows**:

> station departure slot  
> → route/section capacity windows  
> → estimated leg duration  
> → next station arrival slot  
> → dwell  
> → next departure slot

The system must solve the whole chain coherently using the **midpoints of the candidate windows**, not merely show that the windows overlap some possible trajectory. For every leg, planned arrival minus planned departure must cover the feasible running profile and its selected recovery margin; planned departure after a call must cover required dwell/preparation. If individually valid windows have infeasible midpoints, request a different complete slot chain or reject the proposal. Do not silently move the published time away from its accepted midpoint to make the calculation pass.

If a downstream slot is later than originally preferred, subsequent planned calls shift with it. The planner can also work backwards from an important required arrival/connection.

##### Running-time recovery margin

The timetable distinguishes between:

- **base/expected running time** — the physically realistic travel time for the planned route, vehicle and normal operating conditions;
- **planned running time** — the timetable time actually allowed between calls;
- **running-time recovery margin** — planned running time minus the base/expected running time.

Example:

> Base running time: 54 min  
> Planned running time: 58 min  
> Running-time recovery margin: 4 min

The margin exists so small operational delays can be absorbed during the journey without requiring unsafe or unrealistic driving.

A Trip that departs 3 minutes late can therefore still arrive close to schedule when:

- enough recovery margin remains;
- infrastructure permits normal progress;
- the vehicle can recover time within its normal permitted performance;
- doing so does not violate another protected slot/capacity constraint.

The system must **never** recover time by exceeding vehicle, infrastructure or safety limits.

Recovery therefore means using previously planned slack, not giving vehicles a temporary speed bonus.

###### Running-time profile

To avoid segment-by-segment micromanagement, a Service Pattern can use a simple **running-time profile**:

- **Tight** — little recovery margin; higher fleet/infrastructure efficiency but delays propagate more easily.
- **Standard** — normal practical recovery margin.
- **Robust** — more recovery margin; greater resilience at the cost of slower published schedules and potentially higher fleet requirement.
- **Custom** — player sets the desired margin manually where more control is useful.

Exact margin is calculated from the route/service characteristics rather than one universal number for every mode.

Relevant inputs can include:

- service type;
- route length;
- number of intermediate stops;
- infrastructure variability/congestion;
- vehicle performance;
- historical operating/dispatch technology;
- desired reliability level.

The profile is configured at Service Pattern level, with stop/segment override only where operationally justified.

###### Margin consumption and recovery

Running-time recovery margin is consumed dynamically.

Example:

> Depart Praha: +3 min  
> Running-time margin Praha–Pardubice: 4 min  
> Actual conditions allow 2 min to be recovered  
> Arrive Pardubice: +1 min

Unused margin does not force the vehicle to arrive early merely because it could.

Where timetable/slot rules require a planned arrival window, the dispatcher normally regulates progress so the Trip remains operationally sensible rather than arriving excessively early and occupying station capacity unnecessarily.

If delay exceeds the available running-time margin, the remaining delay carries into:

- the next station dwell;
- downstream slot status;
- passenger connections;
- the vehicle duty;
- crew duty timing;
- eventual turnaround.

Running-time margin is separate from:

- **dwell margin** at an intermediate stop;
- **turnaround buffer** between two Trips;
- **rail/station slot tolerance** granted by infrastructure.

The UI should show these separately so the player can understand where timetable resilience actually comes from.

###### Planning trade-off

More recovery margin improves punctuality resilience but is not free.

A more robust schedule can:

- increase end-to-end journey time;
- reduce passenger attractiveness where competitors are faster;
- require more vehicles/crew to maintain the same frequency;
- consume different infrastructure timing windows.

A tighter schedule can improve nominal travel time and asset utilization but makes small disruptions propagate more easily.

The Line Planner should show the practical impact of changing the profile before activation.

##### Operational service priority

A Service Pattern can also define a simple **operational priority** that expresses how strongly the company wants to protect that service's punctuality during conflicts and disruption.

Keep the setting simple:

- **Low** — service can absorb more waiting/recovery delay where useful;
- **Normal** — balanced default;
- **High** — protect departure/on-time running strongly and avoid holding it for lower-priority connections unless explicitly configured.

This is a **company operating policy**, not a replacement for contractual infrastructure priority.

It can influence:

- how long the Trip is willing to wait for connecting passengers;
- which of the company's own services should absorb delay when two recoveries conflict;
- whether a reserve vehicle/crew should preferentially protect one service;
- which duty is reworked first during disruption;
- how aggressively available running-time/turnaround margin is used to restore punctuality.

A typical network can therefore use:

> **Express / intercity** — High operational priority  
> short connection-hold limit  
> protect planned departure and downstream slots

> **Regional feeder** — Low/Normal operational priority  
> longer connection-hold limit for protected passengers arriving from the Express  
> allowed to absorb more delay when doing so preserves the connection

This creates intentionally asymmetric connections.

Example:

> Express arrives 6 min late into hub  
> Regional feeder is configured to wait up to 10 min for that protected connection  
> → Regional waits and departs +6 min

On the reverse connection:

> Regional arrives 6 min late toward the Express  
> Express hold limit is 2 min  
> → Express departs on time/near schedule and affected protected passengers are rebooked if the connection is missed

The exact outcome still depends on:

- available slot tolerance;
- platform/track capacity;
- vehicle/crew duty consequences;
- downstream connections;
- legal/public-service requirements;
- configured connection-hold limits.

A high-priority service is therefore **not guaranteed to be on time**. The setting tells the dispatcher which service should normally be protected when several valid recovery choices exist.

###### Relationship to infrastructure access priority

Operational service priority must never override another train's stronger contracted infrastructure rights.

Rail/station dispatching still follows Section 13.2:

- safety first;
- valid slot/access class;
- contracted time window/tolerance;
- applicable recovery rights.

If a High-priority Express has only a flexible/out-of-slot movement while another operator has a valid guaranteed slot, the Express cannot simply be sent first because the player marked it High.

Operational priority may resolve a choice between the same company's services with equivalent contractual rights. It is not a player-controlled tie-break against another operator. Equal-rights inter-operator conflicts use the infrastructure owner's published neutral dispatch rule with stable ordering, subject to safety and contractual recovery; ownership and a private High setting confer no extra rights.

The Capacity Order UI can recommend a stronger access product for a High-priority service, but changing operational priority does not automatically purchase or upgrade infrastructure rights.

###### Connection-priority interaction

Operational priority works together with the existing per-connection **maximum hold policy** rather than replacing it.

The priority provides a useful default/recommendation:

- lower-priority feeder → longer suggested hold for higher-priority incoming service;
- higher-priority trunk/express → shorter suggested hold;
- equal-priority services → balanced hold based on passenger count and downstream impact.

The player can override the suggested hold for an individual connection.

This keeps the model understandable: **priority says which service the company prefers to protect; hold time says exactly how long a specific connection may wait.**

##### Slot-window width and planned midpoint

Every confirmed arrival/departure slot is a **time window**, not just one timestamp.

Its width is derived from the actual service/consist/handling requirement and the accepted infrastructure product under Section 13.2 rather than from one global default.

Examples of factors that can widen or tighten a station-call slot include:

- amount/type of cargo to load or unload;
- expected passenger exchange;
- train length/weight;
- shunting or locomotive exchange;
- terminal handling technology;
- service class and requested reliability;
- available station/corridor capacity.

For example, a lightly loaded express passenger call may receive a relatively narrow arrival/departure window, while a heavy freight call with significant loading work can receive a wider one.

The timetable planner must also calculate the separate **planned dwell/occupancy duration**. A ten-minute slot window does not mean the train automatically occupies the platform for ten minutes; the actual planned occupancy comes from the physical operation being performed.

The published/planned timetable time is placed **at the midpoint of that confirmed slot window by default**.

Examples:

> Departure slot: 06:08–06:14  
> Planned departure: **06:11**

> Arrival slot: 07:20–07:28  
> Planned arrival: **07:24**

This creates usable operating margin on both sides of the planned time instead of placing the timetable at the edge of the protected window.

For a station call, planned arrival and planned departure are derived separately from their relevant confirmed windows, with the planned dwell fitting between them.

If a slot window changes during planning, the displayed planned time moves automatically to the new midpoint.

The player may express a preferred/anchor time, but once infrastructure capacity is confirmed the **slot window is authoritative** and the planned time is the midpoint of the accepted window. If the resulting time is unacceptable, the player requests a different slot rather than manually moving the planned time outside its capacity window.

Operational status then compares the real Trip against that slot window:

- before/inside the early tolerance;
- on/near planned midpoint;
- inside late tolerance;
- out of slot once the protected window/tolerance is exceeded.

The midpoint rule applies to timetable construction. Actual arrivals and permitted movements can occur elsewhere inside the valid window, but a passenger Trip must not leave a published boarding stop **before its advertised departure time** merely because the slot allows earlier use. Skipping a request stop must not cause early departure from a later published boarding stop. Wait/regulate at a valid location with real occupancy. Freight and non-boarding operational movements follow their explicit cutoff/access terms. Late operation and its consequences remain possible.

##### Frequency planning

For an interval service, the player can request something like:

> every 60 minutes, approximately 06:00–22:00

The planner searches for a repeating family of feasible slot chains as close as practical to that interval.

If exact spacing is unavailable, it should show the resulting pattern before confirmation, for example:

> requested: 60 min  
> achievable: 58 / 62 / 60 / 60 min spacing

and offer alternatives such as shifting the pattern, reducing frequency or using a different service/capacity class.

For sparse services, the player can request a small number of departures or broad departure windows instead of a strict interval.

Exact manual clock times remain available as **preferences/anchors**, especially for important connections, but rail capacity is ultimately secured as time windows.

### 32.3 Line Planner routing and dynamic path assignment

The Line Planner defines the **commercial/operating route**, not a permanently hard-coded sequence of individual road lanes, railway tracks, junction routes or platform numbers.

#### Planning the nominal route

The normal workflow is:

1. choose the ordered commercial stops/endpoints;
2. let the planner find the best compatible route between them over infrastructure the company can legally use;
3. optionally add routing constraints/overrides.

The player does **not** need to click every road segment or railway track.

Optional route controls can include:

- **via waypoint** — force the Line/Pattern through a selected city, junction, station or corridor;
- **required section** — keep a strategically chosen infrastructure section in the nominal route;
- **avoid section/corridor** — prevent normal routing through an unwanted area;
- **preferred route** — favour one compatible corridor while still allowing operational diversion where permitted.

Example:

> Praha → Pardubice → Brno  
> via: Česká Třebová

The route planner then resolves the detailed physical path automatically.

The resulting nominal route is used for:

- timetable/travel-time estimates;
- capacity orders;
- infrastructure/access checks;
- operating-cost estimates;
- traction/vehicle compatibility;
- contract feasibility.

#### Dynamic railway track assignment

A rail Service Pattern is **not assigned permanently to one exact track through every section**.

Track-direction rules are defined **per railway section**, using the same meaningful section boundaries used for rail capacity between stations/junctions/operational nodes.

Each physical track inside a section can have one of these operating modes:

- **Preferred A → B** — normal traffic uses this direction;
- **Preferred B → A** — normal traffic uses the opposite direction;
- **Bidirectional** — both directions are normal and equally permitted;
- **One-way only** — opposite-direction running is technically/operationally prohibited.

A preferred direction is not the same as a hard one-way restriction.

On a track marked with a preferred direction, the dispatcher uses that direction under normal operation. Running against the preferred direction is allowed only when:

- the section is technically/signalling-capable of movement in both directions;
- no better normally directed path is reasonably available;
- the movement is needed for disruption recovery, engineering works, overtaking/routing or another material operational reason;
- required access/capacity and conflict protection remain valid.

Opposite-direction running therefore consumes real capacity and can block or delay trains moving in the preferred direction.

A typical double-track section can therefore be configured as:

> Track 1: preferred A → B  
> Track 2: preferred B → A

while still allowing temporary single-line working over one track during a closure if that track supports bidirectional signalling/operation.

A single-track railway section is normally configured as **bidirectional**, with dispatching resolving opposing movements through available blocks, stations and passing loops.

Direction configuration is local to each section. The next section can have a different arrangement because of:

- track count changes;
- junction geometry;
- signalling technology;
- historical infrastructure layout;
- temporary engineering configuration.

For each concrete Trip, the dispatcher/infrastructure system selects the actual usable railway path from the compatible tracks section by section according to:

- current occupancy;
- signalling/block availability;
- each track's section-level direction mode;
- closures/work zones;
- train length/load/gauge;
- electrification/traction compatibility;
- contracted capacity/priority;
- disruption/recovery needs.

If one track of a double-track or multi-track railway is closed, a Trip can use another compatible track where signalling, direction mode and capacity allow it.

This is a physical reroute through real infrastructure, not teleportation. It can increase travel time, create conflicts or reduce corridor capacity.

The player normally manages the **corridor and capacity product**, while dispatching manages detailed track usage.

A Trip must never gain access to infrastructure that the operator has no legal/contractual right to use merely because it is a convenient diversion.

If a disruption requires a materially different corridor, one of the following must apply:

- the company already has compatible access/capacity there;
- the relevant infrastructure owner re-protects the service onto an alternative route under the disruption/access agreement;
- the player/dispatcher obtains an ad-hoc compatible access solution where available;
- otherwise the Trip waits, reroutes only as far as permitted, or is cancelled.

Infrastructure-side re-protection under Section 13.2 can therefore include a valid alternate route, but cannot invent physical capacity.

#### Dynamic station track and platform assignment

Passenger/freight station calls reserve **station-call capacity**, not a permanently owned numbered platform.

For each Trip, the station allocator dynamically chooses a compatible arrival/departure track and platform using:

- current and expected occupancy;
- platform length;
- approach/departure geometry;
- electrification/traction compatibility;
- passenger/freight facility requirements;
- dwell/turnaround needs;
- shunting conflicts;
- contractual priority.

A train does **not** wait for a historically/preferentially used platform if another compatible platform is available and the station can route it there.

Example:

> Platform 2 is closed for works.  
> Platform 4 is compatible and free.  
> → the arriving Trip is routed to Platform 4 automatically.

The same applies during ordinary congestion: a compatible free platform can be substituted dynamically.

A Trip waits outside/inside the station only when no compatible path/platform capacity is currently available or when another protected movement has contractual/operational priority.

A dedicated numbered platform can still exist only as an exceptional explicit agreement or physical requirement. It is not the default Line Planner model.

Platform changes should propagate to passenger information/wayfinding systems where the historical technology supports it. In earlier eras, late changes can carry a larger operational/passenger inconvenience cost because communication is weaker.

#### Dynamic road routing

Road Lines use the same high-level principle.

The Service Pattern stores stops and routing preferences/waypoints, while each Trip can select a currently usable physical road path that respects:

- legal access;
- road restrictions;
- vehicle dimensions/weight;
- closures;
- congestion;
- one-way rules;
- toll/access policy.

A temporary detour can therefore occur without editing the Line itself.

#### Stability versus flexibility

Dynamic routing should not make services wander arbitrarily.

The dispatcher prefers the nominal route and only deviates when there is a material operational reason such as:

- closure;
- congestion/capacity conflict;
- disruption;
- unavailable platform/track;
- a clearly better authorized path under current conditions.

The player can inspect the nominal route and any active diversion.

Service metrics distinguish planned running time from disruption/diversion effects.

### 32.4 Feeder and connection relationships

Connections should normally be planned at **Line or Service Pattern level**, not by manually linking every individual Trip.

The player can declare that one line or service pattern:

- feeds another line,
- should receive passengers from another line,
- should coordinate bidirectionally around a hub.

The timetable planner then calculates suitable departures using:

- actual travel time,
- transfer walking/handling time,
- desired transfer buffer,
- historical reliability/delay distribution,
- service frequency,
- physical vehicle availability.

Example: the player marks a regional bus as a feeder for a specific rail service. The system schedules the bus to arrive early enough for a reliable transfer rather than requiring the player to set every bus arrival manually.

The player can set high-level preferences such as:

- target transfer buffer,
- maximum acceptable wait,
- whether the feeder may wait for a delayed connection,
- which connection has priority.

These settings can be asymmetric and can inherit recommendations from each Pattern's operational service priority.

A lower-priority regional feeder can therefore be configured to wait longer for a delayed higher-priority Express, while the Express waits only briefly for the regional feeder in the opposite direction.

The system must show the resulting expected transfer quality and any fleet/capacity consequences.

Later dispatching and information technology can automate connection coordination more effectively, but physical travel and actual delays remain real. A connecting vehicle cannot teleport or ignore infrastructure constraints simply because services are linked.

#### Protected passenger itineraries and automatic rebooking

Passenger connection recovery is based on a **protected itinerary**, not merely on the fact that two Trips happen to connect geographically.

A protected itinerary exists when the passenger is sold one journey containing multiple legs under a through-ticket / connection relationship that the selling operator is willing and able to protect.

Example:

> Plzeň → Praha on Trip A  
> Praha → Brno on Trip B  
> sold as one protected itinerary

The itinerary records:

- planned legs/Trips;
- transfer station;
- planned transfer time;
- minimum valid connection time;
- passenger class/capacity requirement;
- operator(s) responsible for each leg;
- through-ticket/rebooking rights;
- applicable compensation/recovery policy.

The system must not sell a protected itinerary whose planned connection is already below the required minimum transfer time.

Two independently purchased tickets do **not** automatically create a protected connection unless the relevant tariff/partnership policy explicitly says they do.

##### Connection hold decision

When an incoming Trip is delayed, the dispatcher can evaluate whether the connecting Trip should wait.

The decision can consider:

- number of protected connecting passengers;
- expected arrival delay;
- maximum hold policy;
- whether the outgoing Trip remains inside its rail/station slot tolerance;
- downstream connections;
- other reserved passengers already onboard/expected;
- crew/fleet implications;
- operational service priority of the involved Patterns;
- service importance/contract obligations;
- available later alternatives.

The player sets high-level hold policies at Line/Service Pattern/connection level. Routine decisions are automatic and can later be delegated to an operations manager.

A connection should not be held indefinitely merely because protected passengers exist.

Example:

> 18 protected passengers arriving 6 min late  
> outgoing Trip can wait 7 min without losing slot protection  
> → hold connection

versus:

> incoming Trip 28 min late  
> outgoing Trip would lose its slot and break several downstream connections  
> → depart and trigger rebooking

##### Automatic rebooking

If a protected connection is missed, affected passengers are **automatically rebooked without player intervention** onto the earliest reasonable itinerary that satisfies their passenger-capacity requirements.

The recovery search can use:

1. a later Trip on the same Line;
2. another suitable Line/Pattern of the player's company;
3. a partner operator where a through-ticket/rebooking agreement exists;
4. another authorized recovery option defined by the passenger policy.

Rebooking is a capacity operation, not teleportation.

The passenger group remains physically at the transfer location until the replacement Trip actually departs.

The system must reserve real compatible capacity on the replacement itinerary.

How early that recovery can be communicated/applied to the passenger depends on the passenger-information capability in Section 28.1. The operations system can know that a connection is at risk before the passenger-facing system is historically able to communicate it.

##### Capacity priority during recovery

Passengers displaced by a carrier-caused missed protected connection become **recovery passengers**.

They receive high priority for currently uncommitted compatible capacity, but they do **not** silently displace passengers who already hold valid confirmed reservations on the replacement Trip.

If the next Trip is full, the recovery system can:

- use the next later compatible Trip;
- reroute through another connection;
- use a higher class as a free operational upgrade where capacity exists;
- offer a lower class only with appropriate refund/compensation and where the service policy permits;
- add an extra/ad-hoc passenger movement where operationally justified;
- use a partner operator under an applicable agreement.

A passenger whose ticket guaranteed seated/berth capacity is not automatically converted to standing travel merely to solve the operator's disruption.

##### Responsibility for a missed connection

The system tracks why the connection failed.

Typical responsibility categories are:

- **player/operator-caused** — delay/cancellation on the player's own leg or another responsibility controlled by the player;
- **partner-caused** — a partner leg failed under a through-ticket agreement;
- **infrastructure/external disruption** — qualifying infrastructure/weather/regulatory event;
- **passenger-caused** — passenger arrived too late outside the protected journey process;
- **unprotected separate tickets** — no guaranteed connection existed.

If the player/operator is responsible, rebooking is provided without charging the passenger another fare and any applicable delay compensation/service cost belongs to the operator.

If a partner is responsible, the passenger-facing recovery can still be seamless where the partnership provides it; commercial settlement/compensation between operators is handled separately.

Infrastructure-caused disruption can still require the operator to re-accommodate passengers even if the operator may later receive infrastructure-side compensation.

Passenger-caused or unprotected missed connections follow the fare/ticket rules and do not automatically create free protected recovery.

##### Compensation

Passenger compensation should remain understandable rather than become a legal-claims simulator.

Tariff, public-service contract or jurisdiction rules can define simple delay bands such as:

- no compensation;
- partial fare refund/credit;
- larger refund for severe delay/cancellation;
- additional recovery support for major disruption where applicable.

The UI should show expected compensation exposure for a major disruption and aggregate routine cases automatically.

Compensation/rebooking cost is distinct from reputation/reliability impact.

##### Historical technology and passenger handling

The **gameplay decision/rebooking process is automatic** so the player does not manually rebook individual passengers.

However, the passenger-facing process reflects available technology.

In earlier eras, re-accommodation may require passengers to use:

- station ticket office;
- branch sales office;
- conductor/onboard staff.

This can consume ticketing/service capacity and take time.

Later centralized reservation, telephone and digital systems make rebooking faster and more seamless.

Technology therefore changes the efficiency/customer experience of recovery without requiring the player to click through individual cases.

### 32.5 Line-level stop service modes

Stop behaviour is configured on the **Service Pattern** (with optional defaults inherited from its Line), not on the station itself.

A station/terminal only exposes its physical capabilities and access rules. Each line that uses it independently defines how that line should serve the location.

This allows the same station to be:

- mandatory for one regional line,
- conditional/on-request for another line,
- skipped by an express service,
- pass-through only for a freight service.

For each stop entry in a Service Pattern, supported modes include:

- **Mandatory:** this line always calls there when the trip runs.
- **Conditional:** this line calls only when a defined condition is met.
- **On request / booked:** this line skips the stop unless there is real passenger booking, cargo work, pickup/drop-off demand or another configured trigger.
- **Pass-through only:** this line may traverse the station/terminal infrastructure but performs no commercial stop there.

Typical line-level conditional triggers can include:

- passengers booked to board/alight,
- cargo batch assigned for pickup or delivery,
- minimum cargo quantity reached,
- contract-required call,
- operational need such as crew/service activity where applicable.

Freight services should normally skip intermediate freight terminals when that specific service has no assigned work there. This avoids unnecessary dwell time and keeps line capacity usage realistic.

Passenger request stops can be appropriate for low-demand local services, especially in early eras or rural areas. The system should only activate the stop when real underlying demand exists rather than through cosmetic randomness.

Timetable planning must account for both cases:

- base running time when the line skips the stop,
- additional dwell/handling time when that line serves it.

For regular planning, the UI should show expected/typical trip time and a reasonable worst-case or high-load trip time so the player understands how the line's conditional stops affect connections and fleet requirements.

Feeder/connection planning must use the actual expected stop pattern of the relevant lines/service patterns and enough buffer to avoid creating impossible transfers when several conditional stops activate.

Dispatch automation can later decide individual conditional calls automatically within the rules of that line, but the player must always be able to inspect why a specific trip stopped or skipped a location.

### 32.6 Vehicle and consist assignment

A Line/Service Pattern can define its vehicle assignment in **three ways**:

1. **Specific vehicles / fixed consist** — the player selects the exact physical vehicles/rolling-stock assets to use.
2. **Criteria-based assignment** — the player defines technical/capacity rules and the dispatcher selects suitable real assets from the fleet pool.
3. **Hybrid assignment** — some vehicles are pinned while the remaining positions/capacity are filled dynamically by criteria.

The player can therefore choose between tight operational control and scalable fleet automation.

#### Specific vehicles / fixed consist

The player can explicitly assign:

- a specific locomotive;
- specific passenger/freight coaches or wagons;
- a specific bus/tram/trainset;
- a complete ordered rail consist.

Example:

> Locomotive #104  
> First Class Coach #18  
> Second Class Coach #44  
> Second Class Coach #51  
> Dining Coach #7

These are real physical assets.

The planner must validate:

- whether each asset is physically available;
- whether it can reach the operating depot/service start;
- maintenance conflicts;
- overlapping Trip assignments;
- route/infrastructure compatibility;
- resulting capacity/performance.

By default, a strictly pinned vehicle is **not silently substituted** if unavailable.

The player can optionally allow a fallback policy such as:

- exact asset required;
- same model/class substitute allowed;
- any vehicle meeting Pattern criteria allowed.

This makes it possible to preserve a special/premium consist without forcing the same rigidity on every service.

#### Criteria-based assignment

Instead of naming specific assets, the player can define a **vehicle/consist rule set**.

Relevant rail criteria can include, where applicable:

- traction type / power system;
- minimum locomotive power;
- minimum tractive effort or required route-performance capability;
- minimum permitted top speed;
- maximum total train weight;
- maximum total train length;
- maximum axle load;
- minimum passenger/cargo capacity;
- required passenger classes/capacity zones;
- minimum/maximum number of coaches/wagons;
- required wagon/coach types;
- required comfort/service features;
- reservation-capable capacity;
- accessibility;
- baggage/catering/sleeper requirement;
- cargo compatibility;
- brake/safety/technical compatibility;
- allowed/excluded vehicle models/families.

Relevant road/urban criteria can include:

- vehicle category;
- minimum passenger/cargo capacity;
- maximum dimensions/weight where route constrained;
- minimum permitted top speed;
- power/grade capability;
- fuel/traction type;
- comfort/accessibility;
- baggage/door/standing capacity;
- required service equipment.

The UI should distinguish **minimum requirements** from **hard maximum limits**.

Example:

> Passenger rail Pattern  
> Min top speed: 120 km/h  
> Min traction capability: route requirement met  
> Max consist length: 210 m  
> Max consist weight: 430 t  
> First Class seats: ≥ 32  
> Total seated capacity: ≥ 280  
> Restaurant/dining coach: required

The dispatcher then selects actual available vehicles that satisfy the complete rule set.

#### Hybrid consists

A Pattern can pin selected components while leaving others dynamic.

Example:

> Dining Coach #7 — fixed  
> 1 First Class coach — criteria-based  
> 3–5 Second Class coaches — criteria-based  
> locomotive — criteria-based, min required route performance

This is useful for:

- branded/premium vehicles;
- special service coaches;
- scarce sleeper/dining cars;
- historic equipment;
- a specific customer-contract vehicle;
- keeping the rest of the fleet flexible.

Pinned and dynamic components still form one real physical consist and must be assembled through normal shunting rules.

#### Performance envelope

Criteria-based assignment is constrained by a **prevalidated operating envelope**.

The Pattern must define enough limits that any dispatcher-selected consist remains compatible with:

- route geometry;
- gradients;
- traction/electrification;
- line speed;
- station/platform length;
- axle/load limits;
- turnaround/shunting facilities;
- planned running times;
- contracted rail/station slot windows.

The dispatcher must not choose a technically valid but too-slow/heavy/long consist that would invalidate the timetable.

Typical envelope rules therefore include:

- minimum route-capable performance;
- minimum top speed;
- maximum train length;
- maximum train weight;
- maximum axle load;
- minimum acceleration/tractive performance where materially needed.

If the actual available fleet cannot form a consist inside the envelope, the Trip is not considered covered.

The planner reports the concrete reason, for example:

> 4 compatible coaches available, but required 280-seat consist needs 5.  
> Available locomotive meets power requirement but resulting consist is 224 m; platform limit is 210 m.

#### Dynamic capacity within a Pattern

A criteria-based Pattern can permit a **range** of consist sizes.

Example:

> 3–6 Second Class coaches  
> minimum 240 seats  
> maximum 230 m total length

The dispatcher can choose a shorter or longer consist based on:

- booked/reserved passenger demand;
- freight allocations;
- demand forecast;
- vehicle availability;
- maintenance state;
- operating cost;
- required reserve policy.

However, all permitted variants must remain inside the Pattern's validated operating envelope and infrastructure/slot assumptions.

If adding/removing vehicles would materially change running time, dwell, slot-window requirement or another protected operating assumption, the planner must revalidate that consist variant before it can be used.

This prevents "automatic capacity scaling" from silently breaking the timetable.

#### Fleet pool and physical assignment

Criteria-based Trips receive concrete vehicles/consists dynamically from the relevant fleet pool.

Selection considers:

- current physical location;
- compatibility with the complete Pattern rule set;
- existing commitments;
- maintenance state and remaining service/inspection margin;
- fuel/energy state;
- repositioning/deadhead cost and time;
- parking/depot capacity;
- reserve commitments;
- expected next work.

The dispatcher can optimize among eligible assets but cannot create abstract vehicles.

Parking and maintenance are separate from the Line's operating depot. Individual assets or fleet groups can retain separate parking/maintenance preferences.

The timetable planner includes real depot-to-service positioning, maintenance windows, consist assembly and necessary repositioning when calculating required fleet size and feasibility.

If a Service Pattern includes locomotive exchange, each segment can have its own fixed/criteria-based traction rule. The planner still validates local traction-base availability and physical exchange operations.

#### Assignment transparency

Before activation, the planner shows:

- required/pinned assets;
- number of currently eligible dynamic assets;
- expected number of consists/vehicles simultaneously required;
- inherited/effective fleet-reserve target;
- effective reserve after known maintenance and other commitments;
- any reserve shortfall;
- any time periods where the fleet pool cannot satisfy the hard operating requirement at all.

For a concrete Trip, the player can inspect which real assets were selected and why.

The player can override the automatic selection when desired, but the override must still satisfy all hard physical, contractual and timetable constraints.

#### Vehicle duties / daily circulation

Concrete Trips are linked into **vehicle duties** (oběhy): physically feasible sequences of work performed by one vehicle, trainset, locomotive or consist over time.

A duty can contain:

- commercial Trips;
- deadhead/repositioning movements;
- turnaround time;
- fueling/charging;
- cleaning/service preparation;
- maintenance/inspection windows;
- shunting/consist changes where relevant;
- parking/stabling;
- return to or departure from a depot/operating base.

Example road duty:

> Praha depot  
> → 06:00 Praha–Plzeň  
> → 08:15 Plzeň–Praha  
> → refuel at Praha terminal  
> → 11:00 Praha–Plzeň  
> → 13:15 Plzeň–Praha  
> → park at depot

A vehicle duty is not restricted to one Line.

If vehicle compatibility, timing and commercial rules permit, the dispatcher can chain Trips from different Lines/Service Patterns into one efficient duty.

Example:

> regional Line A morning Trip  
> → short repositioning  
> → intercity Line B midday Trip  
> → evening return on Line A

This allows the same fleet to be used efficiently without requiring the player to manually assign every vehicle to one permanent Line.

##### Automatic duty construction

The dispatcher normally builds duties automatically.

It chooses feasible Trip sequences using:

- Trip departure/arrival times, including planned running-time recovery margin;
- actual origin/destination location;
- required turnaround time;
- vehicle/consist compatibility;
- physical repositioning time;
- fueling/charging requirements;
- maintenance state and planned maintenance;
- configured turnaround service-profile tasks;
- depot/parking availability;
- preparation horizon;
- fleet-reserve policy;
- known future commitments.

The system should prefer useful continuous work over unnecessary empty movement, while still preserving required reserve and maintenance coverage.

It cannot chain two Trips merely because their timetable times look compatible if the vehicle cannot physically move between them in time.

##### Duty feasibility

Every transition between two duty tasks is validated physically.

For example:

> Trip A arrives 08:15 at Plzeň  
> Trip B departs 08:25 from Praha

is not a valid same-vehicle duty, even if the same vehicle type can operate both services.

The planner must include:

- travel/repositioning time;
- minimum turnaround;
- fueling/charging/service time;
- shunting/consist preparation;
- any required access/slots for repositioning movements.

For rail, a consist cannot be magically reformed between Trips. If the next Trip needs a different consist, the required shunting and vehicle movements must fit into the duty.

##### Minimum turnaround time

Every transition from one Trip to the next has a calculated **minimum turnaround time**.

The minimum is the shortest physically and operationally feasible interval before the same vehicle/consist can begin the next Trip.

It is derived from the actual required tasks rather than one fixed value per mode.

Relevant turnaround tasks can include:

- passenger alighting/boarding;
- cargo unloading/loading where applicable;
- crew change;
- basic inspection/readiness checks;
- mandatory/basic cleaning where required;
- optional turnaround service-profile tasks such as cleaning, catering or water servicing;
- fueling/charging;
- vehicle direction change;
- repositioning within the station/terminal/depot;
- locomotive run-around;
- locomotive exchange;
- coupling/uncoupling vehicles;
- adding/removing coaches or wagons;
- other required shunting;
- terminal/platform clearance and approach/departure movements.

Only tasks actually required for that transition are included.

Example road turnaround:

> arrival 10:42  
> passenger exchange: 4 min  
> driver change: 2 min, parallel with boarding  
> physical minimum next departure: **10:46**<br>
> additional planned recovery buffer: 2 min<br>
> planned next departure: **10:48**

Example rail turnaround:

> arrival 14:10  
> passenger unloading/loading: 8 min  
> locomotive run-around: 14 min  
> brake/readiness check: 5 min after coupling  
> minimum next departure: **14:29**

Tasks can overlap where physically realistic. The system should not simply add every duration serially when cleaning, passenger boarding and crew change can occur in parallel.

Conversely, dependent operations remain sequential where necessary. A brake check cannot complete before a replacement locomotive has coupled.

##### Infrastructure affects turnaround

The same vehicle can have different minimum turnaround times at different terminals.

The calculation considers available physical infrastructure such as:

- platform/berth/stand capacity;
- run-around track;
- crossovers/turning facilities;
- shunting tracks;
- fueling/charging points;
- cleaning/service facilities;
- passenger-flow/boarding capacity;
- terminal road geometry;
- staff/service capacity.

A terminal without a run-around facility cannot pretend to perform a locomotive run-around.

If the required operation is impossible at that location, the planner must propose another operating method, vehicle configuration or terminal rather than assigning an arbitrary time penalty.

Examples include:

- use a bidirectional trainset;
- use locomotives at both ends;
- change locomotive at a station with suitable facilities;
- reposition to a depot/yard;
- choose a different terminal.

##### Turnaround service profile

Turnaround can include **optional passenger-service tasks** in addition to the hard operational minimum.

These tasks consume real time, staff/facility capacity and operating cost, but improve the quality of the next Trip.

To avoid micromanagement, the player normally selects a **turnaround service profile** on the Line/Service Pattern, for example:

- **Minimal** — only mandatory operational tasks; fastest turnaround, lowest service quality.
- **Standard** — routine cleaning/service appropriate to the vehicle and journey.
- **Premium** — more thorough cleaning and passenger-service preparation; longer and more expensive turnaround.
- **Custom** — player selects the supported optional tasks individually.

Typical optional tasks can include:

- quick interior cleaning;
- full interior cleaning;
- toilet/water servicing;
- catering replenishment;
- sleeper/bedding preparation where relevant;
- other period-appropriate passenger-service preparation.

The exact available tasks depend on vehicle type, era and facility capability.

A bus stop with no service facilities cannot perform a full interior/catering turnaround merely because the Pattern requests it.

Likewise, a station can support these tasks only if the required service infrastructure and staff capacity are available.

The planner shows the impact before the timetable is confirmed.

Example:

> **Brno turnaround**  
> Hard operational minimum: 11 min  
> Standard cleaning: +5 min  
> Water/toilet service: +3 min, partly parallel  
> Planned service turnaround minimum: 16 min  
> Passenger comfort/service effect: improved

Optional tasks can overlap when physically realistic.

The service profile affects **actual passenger experience**, not a generic arbitrary bonus.

For example, skipping cleaning repeatedly can reduce perceived cleanliness/comfort and eventually attractiveness/reputation for the affected service, while regular or premium servicing helps maintain the expected quality level.

A premium product can therefore justify longer terminal time and higher operating cost.

The player can also configure which optional tasks may be skipped automatically during disruption.

Example:

> Standard cleaning — may be skipped if incoming delay > 8 min  
> Catering replenishment — do not skip on Premium Pattern

Mandatory safety checks, legally required servicing and any contractually required passenger-service feature cannot be skipped through this setting.

If the dispatcher skips an optional service task to recover delay, the next Trip departs sooner but receives the corresponding service-quality consequence.

##### Planned turnaround buffer

The player may schedule **more** than the physical minimum to improve resilience.

The timetable therefore distinguishes:

- **minimum turnaround** — hard physical/operational requirement;
- **planned turnaround** — actual interval allowed by the timetable;
- **turnaround buffer** — planned minus minimum.

Example:

> Minimum turnaround: 11 min  
> Planned turnaround: 18 min  
> Recovery buffer: 7 min

A player cannot intentionally publish a normal duty with planned turnaround below the known minimum.

Longer buffers consume fleet and terminal capacity but can absorb incoming delay and reduce knock-on disruption.

##### Delay and turnaround recovery

If an incoming Trip is late, part or all of the planned turnaround buffer can be consumed.

Example:

> Planned turnaround: 18 min  
> Minimum turnaround: 11 min  
> Incoming delay: 5 min  
> Next Trip can still depart on time using 5 of 7 min buffer

If incoming delay exceeds the buffer, the next Trip is at risk.

The dispatcher can then use applicable recovery actions such as:

- use a substitute/reserve vehicle;
- omit non-essential turnaround tasks only where policy, safety and service rules permit;
- perform compatible tasks in parallel;
- delay the next Trip;
- rebuild the remaining vehicle duty;
- cancel the affected Trip.

Safety/legal checks and mandatory physical operations can never be skipped merely to preserve punctuality.

##### Turnaround in timetable and fleet planning

Turnaround is included when:

- building vehicle duties;
- calculating fleet requirement;
- validating timetable feasibility;
- reserving terminal/station occupancy;
- planning crew changes;
- planning fueling/charging;
- estimating disruption propagation.

The Line Planner should expose the main reason when turnaround is driving fleet requirement or preventing a tighter timetable.

Example:

> Requested 30-minute frequency requires 7 trainsets  
> Current turnaround at Brno: 24 min  
> Reducing turnaround to 14 min would require a bidirectional consist or improved terminal operation

This lets infrastructure and rolling-stock design create meaningful operational trade-offs without requiring the player to micromanage every individual turnaround action.

##### Automatic fleet requirement

Fleet requirement is calculated from the actual set of feasible duties rather than from a simple abstract formula such as “frequency × route time”.

The planner therefore exposes:

- number of simultaneous duties;
- number of concrete vehicles/consists required;
- deadhead/repositioning workload;
- maintenance coverage;
- fleet reserve after duties are built.

A timetable change can therefore alter fleet requirement even when total number of Trips remains similar.

##### Manual override

The player can inspect and edit generated duties when desired.

Supported overrides can include:

- pin a specific physical vehicle/consist to a duty;
- force two compatible Trips into the same duty;
- prevent two Trips from sharing a duty;
- require a return to a selected depot/base;
- insert a preferred fueling/maintenance stop;
- lock part or all of a generated duty.

Manual edits are revalidated against all physical/time constraints.

If a requested manual duty is impossible, the game explains the blocking reason rather than accepting it and failing silently later.

##### Dynamic assignment and duty templates

For criteria-based fleets, a duty does not necessarily need a specific serial-number vehicle months in advance.

The planner can first create a **duty requirement** such as:

> Intercity coach duty  
> 05:30–17:10  
> min 50 seats  
> compatible with Lines A and B  
> fueling opportunity at 10:20

The concrete compatible vehicle is assigned according to the preparation/commitment rules below.

For fixed/pinned fleets, the duty can already refer to a specific physical vehicle.

##### Delay propagation through duties

A vehicle remains physical across its complete duty.

If Trip A arrives late and the same vehicle is planned for Trip B, that delay can propagate into Trip B unless the dispatcher recovers by:

- shortening turnaround where safely possible;
- assigning a reserve/substitute vehicle;
- reworking the remaining duty;
- delaying Trip B;
- cancelling a later Trip under the disruption policy.

The system must show downstream duty conflicts so the player can see that one disruption may affect later services.

This is distinct from passenger connection recovery: one is a **vehicle-resource dependency**, the other a passenger itinerary dependency.

##### Duty regeneration

Duties are recalculated when relevant inputs change, including:

- timetable/Pattern version;
- vehicle assignment criteria;
- fleet availability;
- maintenance plan;
- fueling/charging infrastructure;
- depot/base assignment;
- disruption that materially changes later work.

Routine recalculation is event-driven and should preserve stable existing duties where possible rather than arbitrarily reshuffling the entire fleet every minute.

#### Trip preparation horizon and concrete asset reservation

A planned Trip does not need all of its concrete physical assets locked far in advance.

Instead, the dispatcher calculates a **preparation horizon** for each Trip: the point before departure at which the company must begin committing specific vehicles/rolling stock and executing the physical work required to make the Trip ready.

The horizon is derived from the actual preparation work rather than one universal fixed value.

Relevant inputs include:

- transport mode and vehicle type;
- fixed versus criteria-based versus hybrid assignment;
- current physical location of candidate vehicles;
- required repositioning/deadhead travel;
- train consist complexity;
- shunting/assembly/disassembly work;
- fueling, charging or other energy preparation;
- cleaning and servicing;
- catering, bedding or other passenger-service preparation;
- cargo-specific wagon/equipment preparation;
- mandatory technical/safety checks;
- locomotive exchange staging;
- depot/yard/workshop capacity and congestion;
- staff availability;
- historically appropriate operating technology.

A simple bus Trip from its home garage can therefore have a much shorter preparation horizon than a long-distance passenger train that requires a locomotive, several coach types, catering, cleaning and physical shunting.

##### Player minimum lead-time override

The Line/Service Pattern can define an optional **minimum preparation lead time**.

Example:

> Automatically calculated preparation horizon: 2 h 20 min  
> Player minimum: 4 h  
> Effective preparation horizon: 4 h

The override is a minimum, not a promise that preparation can always wait until that point.

If physical repositioning or preparation requires more time, the dispatcher starts earlier.

The player can therefore choose a more conservative operating style without manually setting every Trip's preparation timestamp.

##### Planning versus commitment

Deferring concrete asset IDs does not defer capacity accounting. Future confirmed work reserves compatible time/capability capacity in the shared ledger, including preparation, maintenance and reserve obligations. Every planner uses those same reservations. Selecting serial-number assets later binds existing commitments rather than creating a second reservation or discovering that the same fleet was promised twice.

Before the preparation horizon, the planner primarily maintains **feasibility coverage**:

- enough suitable fleet is expected to exist;
- no known maintenance/assignment conflict makes the Trip impossible;
- reserve margin is visible;
- likely candidate assets can be identified without necessarily locking them.

At or before the preparation horizon, the dispatcher begins turning the plan into concrete commitments.

This can include:

1. selecting/reserving specific vehicles from the eligible fleet pool;
2. initiating required repositioning/deadhead movements;
3. reserving depot/yard/shunting capacity;
4. assembling the physical consist;
5. fueling/charging at a compatible depot/station/terminal service point where required;
6. cleaning/catering/other required servicing;
7. performing applicable technical/readiness checks;
8. positioning the completed vehicle/consist for boarding/loading/departure.

Pinned vehicles are already predetermined, but the same preparation logic still determines when they must be physically committed and moved into position.

Criteria-based/hybrid services keep more flexibility until the dispatcher reaches the point where specific assets are needed for real preparation work.

##### Progressive commitment

Preparation can use several internal checkpoints rather than one instantaneous lock.

A typical sequence can be:

> **Planned** — Trip exists in timetable; fleet feasibility checked  
> **Preparing** — concrete assets are being selected/positioned/serviced  
> **Assembling** — physical consist/shunting or equivalent preparation in progress  
> **Ready** — required vehicle/consist, crew and departure prerequisites are available  
> **Running** — Trip has departed  
> **Completed** — Trip finished

Not every mode needs every visible state. A bus service may move directly from Preparing to Ready without an assembly phase.

The UI should expose useful operational status without requiring the player to micromanage every intermediate task.

##### Final readiness check

Shortly before departure, the dispatcher performs a **final readiness check** against the actual Trip rather than relying on the earlier planning estimate.

It verifies, as applicable:

- assigned physical vehicles are present;
- consist is correctly assembled;
- route/traction/infrastructure compatibility remains valid;
- required maintenance/safety status is valid;
- fuel/energy is sufficient for the planned Trip/duty until the next valid fueling/charging opportunity;
- crew capacity is available;
- required onboard staff are available;
- passenger/cargo capacity matches the final consist;
- loading/boarding facility is usable;
- departure slot/access remains valid;
- required service equipment is ready.

If all hard requirements are satisfied, the Trip becomes Ready.

If something has failed or is missing, the dispatcher immediately applies the Pattern's **day-of-operation disruption policy** below.

##### Preparation conflicts are real capacity conflicts

Preparation tasks consume real facilities and time.

Two trains cannot simultaneously use the same single shunting track, service bay or fueling point beyond that facility's capacity.

If several upcoming Trips require the same constrained depot/yard resource, the dispatcher must schedule their preparation coherently.

The timetable/fleet planner should therefore detect recurring preparation bottlenecks before activation where they are predictable.

A Trip should not repeatedly fail at departure because a known depot cannot physically prepare the planned number of vehicles in time.

##### Recalculation

The preparation horizon is recalculated when a material input changes, including:

- vehicle assignment rules;
- operating depot;
- timetable/departure time;
- consist size;
- preparation/service requirements;
- infrastructure or depot access;
- significant disruption;
- manual player reassignment.

The horizon is not recalculated every frame. It is event-driven and scheduled, consistent with the wider simulation architecture.

#### Day-of-operation vehicle failure and disruption policy

A vehicle/consist becoming unavailable shortly before a Trip does not have one universal automatic outcome.

The Line/Service Pattern can define a **vehicle-disruption policy** that tells the dispatcher which recovery actions are allowed and in what preferred order.

Typical actions include:

1. **Substitute compatible vehicle(s)** — normally draw first from compatible available fleet reserve, then from other safely reassignable assets, while satisfying the Pattern's hard operating envelope.
2. **Run short / omit failed vehicle(s)** — operate with a reduced consist if the remaining train is physically valid and the player's policy permits it.
3. **Delay departure for replacement/repair** — hold the Trip for a configurable maximum time while a replacement is positioned, a repair is completed or shunting is performed.
4. **Use an alternate valid consist** — rebuild the train from available vehicles under the Pattern's criteria/hybrid rules.
5. **Cancel the Trip** — if no acceptable recovery remains.

The player can define the preferred order and limits, for example:

> 1. substitute same coach type  
> 2. wait up to 12 min for any compatible replacement  
> 3. depart without the coach if minimum protected capacity remains  
> 4. otherwise cancel

Different Patterns can use different policies.

A premium long-distance service can prefer delaying for a replacement rather than losing a required First Class or sleeper vehicle, while a frequent regional service can prefer departing short-formed rather than causing a large delay.

The dispatcher can execute routine decisions automatically inside the configured policy. The player may intervene manually before departure where time permits.

##### Hard constraints still apply

A disruption policy cannot authorize an impossible or unsafe consist.

Any replacement/reduced consist must still satisfy applicable hard constraints, including:

- route/traction compatibility;
- braking/safety requirements;
- maximum length/weight/axle load;
- minimum locomotive/tractive performance;
- required control/coupling compatibility;
- infrastructure limits;
- legally or contractually mandatory equipment;
- any minimum capacity that a public-service/customer contract makes a hard requirement.

If removing a vehicle changes performance enough to invalidate the booked timetable/slot assumptions, the dispatcher must re-evaluate expected timing and slot status before departure.

##### Passenger consequences are resolved after the operational decision

The **operational recovery decision** and the **passenger-commercial recovery** are separate steps.

Example:

> One Second Class coach fails before departure.  
> Pattern policy permits the train to depart without it.  
> The Trip therefore runs short-formed.  
> The passenger system then evaluates the capacity that was actually lost.

After the final operating consist and departure decision are known, the system compares real available passenger capacity with:

- protected passenger-contract allocations;
- confirmed individual reservations;
- protected multi-leg itineraries;
- open/walk-up demand.

If all confirmed commitments still fit, the Trip can run with lower spare capacity and no confirmed passenger must be displaced.

If confirmed commitments no longer fit, affected passengers are handled through the existing passenger-recovery rules.

The system attempts, as applicable:

1. re-accommodation within the same Trip, including a valid free upgrade where appropriate;
2. rebooking onto another Trip/itinerary;
3. partner/replacement transport where available;
4. refund when an acceptable replacement cannot be provided.

If the operator's equipment failure, short-formation, delay or cancellation causes a qualifying service failure, any additional compensation is calculated separately according to the applicable tariff, public-service contract, customer contract or jurisdiction rules.

The player therefore sees the complete consequence of the dispatch choice, for example:

> **Depart without Coach #51**  
> Departure delay: +0 min  
> Capacity lost: 68 Second Class seats  
> 42 unused seats absorbed by remaining consist  
> 18 passengers re-accommodated on this train  
> 6 passengers rebooked to 08:11  
> 2 passengers refunded  
> Estimated refund/compensation cost: X  
> Reliability impact: Y

versus:

> **Wait for replacement coach**  
> Expected departure delay: +14 min  
> All reservations preserved  
> 1 protected connection at risk  
> Estimated delay-compensation exposure: X

The dispatcher can use these consequences when choosing among equally permitted recovery options, but it must obey the player's configured priority/maximum-delay policy and cannot silently optimize only for profit.

##### Freight consequences

The same operational policy principle applies to freight rolling stock.

If a freight Trip departs with reduced compatible capacity, protected/guaranteed cargo commitments are revalidated against the actual consist.

Cargo that no longer fits follows the existing loading-priority and freight-recovery rules:

- protected commitments remain priority obligations;
- discretionary/spot cargo can be displaced first;
- guaranteed cargo that cannot be carried is rebooked/recovered rather than silently deleted;
- SLA/penalty consequences remain attached to the responsible contract.

### 32.7 Crew requirement planning and recovery policy

Service planning must validate both vehicle availability and aggregated qualified crew capacity.

For each Service Pattern, the planner estimates:

- total operating hours;
- peak simultaneous crew demand;
- day/night/weekend staffing burden;
- whether crew changes are required;
- suitable locations for those changes where applicable;
- company reserve remaining after the timetable is activated.

The planner should warn when a timetable is technically possible with vehicles but would consume too much of the player's intended crew reserve or cannot be covered by available qualified staff at all.

Crew planning remains aggregated across the company and does not introduce individual employee pathfinding, named ordinary-driver assignment or mandatory region-by-region reserve management.

#### Crew duties / shift blocks

Operating staff are scheduled into aggregated **crew duties** (shift blocks) covering one or more consecutive Trips.

A crew duty represents qualified staffing capacity, not a named employee.

A typical duty can contain:

- one or more Trip segments;
- planned turnaround/waiting time;
- a crew change at an eligible location;
- legally/safely required break/rest boundaries;
- required crew category/qualification.

Example:

> Train-driver duty A  
> Praha 06:00 → Brno 09:10  
> duty ends / crew change

> Train-driver duty B  
> Brno 09:35 → Wien 11:20

The train/vehicle can therefore continue on its own vehicle duty while the operating crew changes.

The dispatcher builds crew duties automatically from the timetable and checks:

- required qualification;
- Trip timing;
- maximum effective duty/shift duration;
- required rest/break rules;
- planned crew-change locations;
- available company crew capacity;
- company crew reserve.

Crew changes are allowed only at operationally suitable locations such as appropriate stations, terminals, depots or other designated change points.

The game does not simulate the named person travelling home, commuting across the map or individually taking a lunch break. Those realities are represented through aggregate duty/rest capacity.

A Line Planner should expose the practical result, for example:

> 8 train-driver duty blocks/day  
> 3 conductor duty blocks/day  
> 1 planned crew change at Brno  
> Peak train-driver requirement: 5.4 crew-equivalents  
> Reserve remaining: 0.8

A timetable that would require an impossible crew duty, such as exceeding allowed duration without a valid change point, is not considered fully feasible.

Manual control remains high-level. The player can:

- mark/prefer a crew-change point;
- prevent an unsuitable change point;
- require a crew change before/after a selected segment.

The player does not manually assign ordinary employees to individual shifts.

If delay causes a planned crew duty to overrun or miss a crew-change window, the dispatcher re-evaluates the remaining duty and uses the company crew-recovery policy below.

#### Company crew-recovery policy

The player defines a **company-wide crew-recovery policy** for short-notice staffing failures.

The policy can differ by genuinely distinct crew category where necessary, because a missing driver/strojvedoucí is operationally different from missing optional onboard service staff.

The dispatcher can use actions such as:

1. **Draw from crew reserve** — assign compatible uncommitted qualified capacity.
2. **Wait for crew capacity** — delay departure for up to a player-defined maximum while compatible capacity becomes available.
3. **Depart with reduced non-mandatory onboard staffing** — only where law, safety, service contract and the Pattern's service rules permit it.
4. **Cancel the Trip** — when mandatory crew cannot be supplied within the allowed waiting policy.

Example company policy:

> Train driver unavailable  
> 1. use reserve if available  
> 2. wait up to 12 min for compatible crew capacity  
> 3. otherwise cancel Trip

Example for onboard staff:

> Conductor/onboard staff shortage  
> 1. use reserve  
> 2. wait up to 5 min  
> 3. if legal minimum is still met, depart with reduced onboard service  
> 4. otherwise cancel

A Trip can never depart without legally/technically mandatory crew.

For example, the absence of the only required driver or train driver cannot be converted into a reduced-service departure.

If optional onboard staffing is reduced, the actual consequences are applied. These can include:

- onboard ticket sales disabled/reduced;
- lower onboard service capacity;
- longer checking/service times;
- contractual/service-quality impact where applicable.

#### Crew shortage consequences

If waiting for crew delays the Trip, that delay flows through the normal operating systems:

- rail/station slot tolerance;
- protected passenger connections;
- freight/customer SLA;
- subsequent vehicle/crew duties;
- rebooking;
- refunds;
- compensation where applicable.

If the Trip is cancelled, passenger/cargo obligations are resolved through the existing recovery rules rather than disappearing.

The UI should compare the practical consequence of the allowed options where useful, for example:

> **Wait for train driver — up to 10 min**  
> reserve currently unavailable  
> next compatible crew capacity expected in ~7 min  
> slot remains protected up to +9 min  
> 2 passenger connections at risk

versus:

> **Cancel Trip now**  
> 146 passengers affected  
> 118 can be rebooked  
> 28 require later service/refund  
> estimated refund/compensation exposure: X

The dispatcher executes routine cases automatically inside the company policy.

Later operations/HR managers can recommend reserve-size or recovery-policy changes, but they cannot override explicit player limits or create staff capacity that the company does not employ.

## 33. Urban transport

Wider base-game urban modes (only buses are required in first-playable V1):

- buses,
- trams,
- trolleybuses,
- metro.

Urban transport follows the same physical rules:

- real vehicles,
- depots,
- maintenance,
- staff,
- power/infrastructure,
- physical capacity.

For tram, trolleybus and metro operations, a basic depot/garage always contains routine workshop capability; parking-only facilities are not the default depot type for these modes.

Urban networks feed intercity stations and can materially influence passenger demand.

### 33.1 Municipal operators, contracts and city permission

Cities can own normal transport companies that behave as local competitors/operators.

A hybrid model is used:

- cities maintain a minimum service;
- municipal operators can run services directly;
- cities can tender routes, areas or entire networks to private operators;
- private operators can sometimes run commercially at their own revenue risk, but only with explicit city permission/concession.

A player **cannot simply create an urban public-transport Line inside a city because vehicles and road/track capacity are available**.

Before a bus, tram, trolleybus or metro Line is activated as urban public transport, the player must have one of:

1. **Municipal operating contract / tender award** — the city orders the service and defines some or all of its required route, frequency, fares/SLA or coverage, with the agreed compensation/revenue model.
2. **City operating permission / concession** — the city allows the player to operate the service commercially without necessarily guaranteeing a subsidy or minimum revenue.

A city permission is therefore distinct from a customer contract.

It can specify constraints such as:

- permitted route/area;
- allowed stops;
- minimum/maximum frequency;
- operating hours;
- fare rules or caps where applicable;
- service-quality requirements;
- street/stop/infrastructure access;
- validity period;
- renewal/termination terms.

The city can refuse a proposed private Line where it conflicts with regulation, street capacity, an exclusive concession or the municipality's transport policy.

Where permission is granted without a service contract, the player bears normal commercial demand risk and earns passenger revenue from the simulated market.

Where a municipal contract exists, the resulting service still uses the normal:

**Line → Service Pattern → Trip**

operating hierarchy. The contract is attached through the Contract Transport Plan and does not replace the Line object.

A single urban Line can also satisfy more than one compatible public/commercial obligation where contract and city rules permit it; capacity/rights must not be double-counted.

Municipal operator scope is local: city plus agglomeration, with only limited short intercity reach where plausible.

The player can operate urban transport through a group-wide division or dedicated city subsidiaries.

Optional renewal of a municipal operating contract follows Section 11.12. An agreed extension can renew automatically; a service that requires a new competition must be awarded through that competition rather than retained through a checkbox.

City operating permission/concession renewal follows its own agreed validity/renewal terms and cannot be assumed permanent.

## 34. Roads inside cities

Urban streets are primarily controlled by municipalities/states.

The player cannot freely redraw built-up street networks.

In undeveloped peripheral areas, construction freedom is much greater.

Major urban interventions require approval and compensation and can harm regional reputation.

## 35. Historical events and macroeconomy

History affects the transport business but does not become a war/politics strategy game.

Major events can alter:

- borders,
- licences,
- cross-border access,
- passenger demand,
- commodity demand,
- state contracts,
- material availability,
- prices,
- industrial production.

Wars/conflicts should be represented mainly through economic/regulatory consequences, not combat visuals.

Large accidents/destruction caused directly by historical events should be rare.

Economic booms and recessions should emerge as meaningful operating conditions rather than flat income modifiers.

Historical state is initialized at the selected start year under Section 3.5. Events prior to that date contribute to the starting world rather than firing again after game creation. Future events follow the same simulation calendar and historically anchored variation rules.

## 36. Weather and seasons

Weather is visual and operational.

Early technology is more vulnerable to:

- snow,
- mud,
- heavy rain,
- poor roads,
- low water levels.

Technology progressively improves resilience through better surfaces, drainage, snow clearing, vehicles and forecasting.

Most weather disruption should be handled automatically and appear as delay/cost.

Rare major events can require direct player decisions:

- flood,
- severe drought,
- landslide,
- damaged bridge/track.

Season lengths and recurring demand profiles follow the 168-day game year in Section 3. Climate/technology susceptibility is initialized for the chosen era; a new company in a later start is not automatically subject to Early Ages road conditions.

## 37. Safety and accidents

Major accidents are rare.

Risk is influenced by:

- vehicle condition,
- infrastructure condition,
- maintenance coverage,
- signalling/safety technology,
- traffic intensity,
- weather.

Normal neglect should produce speed restrictions, failures and closures before catastrophic accidents become likely.

Major accidents can have real consequences:

- damaged assets,
- line closure,
- repair costs,
- aggregated casualty impact,
- state scrutiny,
- reputation damage.

## 38. Finance and failure

Finance is intentionally simpler than the operational/economic simulation. The single accounting unit is literally `money` in both Czech and English, with localized number formatting but no historical currency switching, real-world currency symbols or foreign-exchange subsystem. Player-facing UI may use one dedicated neutral coin/token icon as compact shorthand for `money`; this icon is not a second currency, historical symbol or exchange-rate mechanic. Full text, tooltips/accessibility labels and ambiguous contexts retain the `money` unit name. Use exact fixed-point/integer money postings; Sections 7.1 and 38.1 govern startup debt.

Core tools:

- cash,
- operating cash flow,
- simple bank loans.

No deep bond-market simulator is required.

### 38.1 Founding loan

Every new company begins with one of the three founding-loan tiers defined in Section 7.1. Initial cash is therefore financed rather than granted for free.

The founding loan is a special startup product with intentionally favourable conditions compared with ordinary later borrowing. Its purpose is to let the player establish a viable operation without making the opening hours primarily a debt-service survival test.

Founding-loan rules:

- low fixed or otherwise clearly predictable interest;
- long repayment horizon;
- manageable instalments even for the largest starting tier;
- larger tiers have larger principals and therefore higher total repayments, but not disproportionately punitive rates;
- terms are disclosed completely before starting the game;
- repayments use the shared game calendar and financial period rules from Section 3.4.

The player can repay the founding loan early if ordinary loan rules allow it; any early-repayment fee, if used at all, should be small and disclosed rather than punitive.

The founding loan remains real debt on the balance sheet. It affects cash flow and solvency calculations and does not disappear when the company grows.

After the game starts, additional financing uses normal commercial loan products rather than repeatedly granting founding-loan terms.

Infrastructure and land can be sold to states or competitors.

A distressed company can:

- cut services,
- sell vehicles,
- sell infrastructure,
- borrow,
- request limited state emergency financing/restructuring.

Bankruptcy is a process, not an instant failure. Game over occurs only when the company is deeply insolvent with no viable assets/financing path left.

Financial rates, reporting and billing periods use explicit game-time units under Section 3.4. A game month has 14 days and a game year 168 days. Do not use hidden conventional-calendar accruals or accelerate only financial/historical time separately from operations.

## 39. Infrastructure market

Infrastructure can be bought and sold as real physical assets.

A buyer may:

- continue operating it;
- offer access to other carriers;
- tender services;
- repurpose/rebuild it;
- demolish it and allow urban redevelopment.

A purchase transfers ownership; it does **not** reset the asset.

Where applicable, the buyer inherits the asset's real state and binding obligations, including:

- physical condition and maintenance state;
- existing leases/tenancies;
- valid infrastructure/station/access agreements;
- guaranteed capacity commitments;
- active construction/repair work;
- applicable land/connection rights and restrictions.

Buying a station or corridor does not automatically cancel a competitor's already valid protected access merely because ownership changed.

Partial asset sales are allowed, e.g. sell the track but keep a depot or station.

A partial-sale review must expose dependencies created by the split. If the retained depot needs access over the sold track, the sale does not silently create a free post-sale access right. The player must retain/negotiate real access, change the sale scope or accept the consequence.

Selling or transferring an infrastructure asset never teleports vehicles/cargo or creates new capacity.

Company acquisitions and intra-group infrastructure transfers follow Section 29.1. UI-D39 in UI_OWNERSHIP.md defines the confirmed player-facing workflow.

## 40. Research, historical vehicles and manufacturers

Real-world trademarks/brands are avoided.

Vehicles and manufacturers are fictional but historically plausible in appearance, parameters and availability.

Manufacturers are economically present enough to make supply, capacity and backlog meaningful, without becoming a separate deep management game.

## 41. Performance non-negotiables

The game must be designed from the first prototype to scale.

Do not build a small-world architecture that assumes later optimization will fix it.

Key expectations:

- simulation LOD,
- event-driven updates,
- cached network paths/options,
- aggregated remote populations and private traffic,
- aggregate inactive-world macro simulation,
- no per-frame economic AI,
- no per-person persistent population simulation,
- no per-component vehicle maintenance simulation,
- physical continuity preserved logically even when rendering is culled.

Validate supported speeds from 0.5× to 16× on representative operating loads, including a developed network. The maximum is 16×, not a promise that current unimplemented code already sustains that rate. Higher speed may reduce visual detail but must not skip reservations, physical movement, transfers, service events, contracts or resource accounting. All subsystems advance on the same clock.

## 42. Current out-of-scope / deferred

V1-specific deferrals are water, tram, trolleybus and metro operation and the 1925/1950/1975 new-game presets. These remain wider base-game goals, distinct from the broader deferred list below.

- **Early Ages**, the first planned DLC: playable pre-1900 history with an intended start around 1820. Preserve extensibility and earlier-era design context, but do not make this content mandatory for the base game.
- Aircraft.
- Full procedural world generator.
- Deep factory ownership/building gameplay.
- Deep construction-company side business.
- Full per-person life simulation.
- Detailed mechanical component maintenance.
- Combat/war simulation.
- Scenario/campaign victory objectives.
- Mandatory expert railway timetable editor.

The base-game start choices and time model are defined in Section 3. Older buildings, infrastructure and vehicles that are still relevant in those years are not excluded merely because their origins predate 1900.

These deferred areas may be revisited later without compromising the current architecture. Early Ages has a planned place as the first DLC, not a specified delivery date.

## 43. Cross-system consistency checklist

Every new feature or design change must be checked against at least:

1. Physical continuity — does anything teleport or bypass required movement/infrastructure?
2. Time progression — does it use the unified 14-day-month calendar and remain coherent at 0.5× through 16×, for each of the 1900/1925/1950/1975 starts? Is pre-1900 content correctly scoped to Early Ages rather than silently required by the base game?
3. Technology — what unlocks or improves it, and is already-established technology initialized correctly for a later start?
4. Economy — who pays, supplies, consumes and profits, and are all calendar-rate units consistent?
5. Contracts — does it create or consume transport demand?
6. Ownership/licensing — who owns it and who is allowed to use it?
7. Infrastructure capacity — where are the bottlenecks?
8. Workforce/management — who operates it and can it be delegated?
9. Reputation/public authority — are permissions or public consequences involved?
10. Simulation performance — can it run at European scale using aggregation/event-driven logic?
11. Inactive regions — does it require full simulation outside unlocked territory?
12. AI competitors — can AI companies use the same rules without cheating?
13. UI clarity — can the player understand the system without micromanagement?
14. Existing rules — does it contradict any currently agreed rule in this document or the relevant focused specification?

If a conflict appears, update all affected sections before treating the feature as accepted.
