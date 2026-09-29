# Tranzit — Living Game Design

> **Status:** Living source of truth. This document describes the current agreed design. It is not a chronological idea log.
>
> **Maintenance rule:** Before adding or changing any feature, review all affected sections and resolve contradictions. Remove or rewrite obsolete decisions instead of appending conflicting alternatives.
>
> **Related specification:** [CONTRACT_CANCELLATION.md](CONTRACT_CANCELLATION.md) defines the current proportionate cancellation and early-capacity-release rules.

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

## 2. World, map and regions

### 2.1 Geography

The first playable world is based on real European geography, initially focused on Central Europe. The first production scope should prioritize areas corresponding to modern Czechia plus nearby Central European regions; Germany, Austria, Hungary and Poland are natural early expansion targets.

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

The base game's default/earliest selectable start is **1900**. New games can also start in **1925, 1950 or 1975**. The player chooses a start region, then must **physically establish and construct the first regional office/branch in a chosen city**. Choosing a later year does not automatically grant a large established company or a free prebuilt branch.

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
- Day-of-month dates that do not exist in the game calendar, including historical holidays/events after the 14th, need an explicit documented conversion when content is authored. The exact real-date-to-game-date mapping is still to be specified; do not silently create invalid dates or assume a 31-day month.
- UI must distinguish game time from estimated real playtime. Calendar, contracts and timetables show game-time units consistently.

Test month/year rollover, two complete weeks per month, cross-year winter seasons, seasonal renewals and speed changes during trips, maintenance and construction. For equivalent simulated elapsed time, different selected speeds must not change resource accounting or bypass physical movements, reservation conflicts, deadlines or other events.

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

Passenger demand can be seasonal, but the strength and composition of seasonality must be historically plausible. Leisure/tourism demand depends on the chosen year, income, free time, transport accessibility, urbanization and relevant destinations, not simply how recently the player founded the company. Seasonal passenger peaks can include holiday/leisure travel, commuting cycles, fairs/events and later mass tourism. The Early Ages DLC must not project modern travel behaviour backwards into its earlier period, and a 1975 base-game start must not inherit an 1820 demand profile.

Passenger demand also has historically grounded daily and weekly rhythms. Work shifts, market days, school schedules, religious/rest days, weekends and later modern commuting patterns can shape peaks, but the profile must evolve by era rather than using one modern 24/7 template for the whole campaign.

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
- customer-facing ticket/sales/service desk functions where historically appropriate;
- space for local managers/admin staff;
- direct organizational connection to the passenger hub.

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
- deliberately overstaff to create spare capacity and faster response during growth/peaks.

Staffing affects concrete capacity and processing performance. It does not create unrelated global bonuses.

If staffing is below the branch's minimum operating requirement, the branch cannot provide normal commercial service until the shortage is resolved.

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
- inspect opportunities;
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

Ordinary employees are aggregated rather than simulated as persistent individual people.

The workforce is split by operational role so the game stays simple without breaking facility capacity.

### 8.1 Company-wide mobile operating staff

Drivers, train crews and similar mobile operating staff are pooled **across the whole company** by qualification rather than being permanently tied to a specific region or depot.

The game tracks aggregated availability such as:

- number of qualified train drivers,
- road-vehicle drivers,
- conductors/on-board crews where required,
- licence/vehicle-type qualifications,
- usable shift/work-hour capacity.

A Trip consumes the required crew capacity for its duration. If the company does not have enough qualified staff, the Trip cannot be staffed or must be cancelled/rescheduled.

Crew capacity also respects aggregated **shift and rest requirements**. The game does not track an individual driver's sleep schedule, but longer, overnight or continuous operations consume more effective staffing capacity because legal/safe rest and crew rotation must be covered.

Long-distance or long-duration Trips can require crew changes. The service planner should show when a service needs:

- one crew for the full Trip,
- a planned crew change,
- multiple crews for continuous/night operation,
- additional onboard staff because of service class or regulations.

Crew-change requirements are handled as operational planning constraints rather than persistent individual-person simulation. The game may use defined eligible change locations such as major stations, depots or terminals, but it does not require the player to assign named ordinary employees.

The UI must translate staffing needs into understandable requirements such as:

- train-driver hours/day,
- road-driver hours/day,
- number of effective full-time crews required,
- peak crew requirement,
- additional staffing required for night/weekend patterns.

The game does **not** simulate individual crew members commuting between Praha and Ostrava or require staff-repositioning trains. This is intentionally abstracted to avoid low-value micromanagement.

Expansion into another region therefore does not require maintaining a separate arbitrary pool of drivers there, although local licences/language/regulatory requirements may still require the company to have the appropriate qualified staff category where historically/gameplay relevant.

### 8.2 Facility-bound staff

Employees whose work directly determines the capacity of a physical facility remain allocated to that facility or local operation, for example:

- mechanics/workshop staff,
- station and terminal staff,
- warehouse/loading staff,
- local office/admin staff,
- local dispatch/yard staff where the facility requires them,
- safety/security/cleaning where relevant.

This preserves existing physical systems: a workshop with too few mechanics really repairs vehicles more slowly, and an understaffed terminal really handles less cargo.

Company HR can still recruit and rebalance these employees at a higher level, and later managers can automate staffing targets.

### 8.3 Business/administrative staff

Sales, contract, HR and general administrative capacity can be aggregated at company/division/office level depending on the system they support.

Insufficient staffing creates concrete operational consequences such as slower maintenance, reduced opening hours, delayed handling, inability to cover all Trips or weaker contract-processing capacity.

Staffing hours, rest periods and wage periods use the shared game clock and explicit rate units in Section 3.4. Changing the speed selector does not change the crew required for the same service.

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

### 10.2 Industrial geography

Industry is dynamic but geographically grounded.

Resource extraction is constrained by plausible deposits and land conditions.

Large deposits may effectively last the full campaign; smaller deposits can deplete and close.

Processing/manufacturing industries are more flexible and can choose locations based on labour, transport, markets and inputs.

New firms and facilities may emerge over time. Existing firms can expand, open new plants, acquire other firms or decline.

### 10.3 Historical and seasonal demand

Commodity importance changes over time.

Examples:

- coal becomes critical in the industrial age and later declines relatively,
- oil and gas rise later,
- electricity systems alter energy demand,
- modern renewables change demand again.

Demand can also be seasonal where the underlying economy supports it. Examples include harvests, food processing, heating fuel, construction seasons and other recurring production/consumption cycles.

Seasonality must come from the actual simulated business/population context rather than flat global multipliers. Its intensity and cargo mix can change by era, region, technology and economic development.

Industrial decline can leave physical brownfields.

### 10.4 Market accessibility

Firms do not search every destination in Europe every tick.

Regional/market accessibility is cached and updated when relevant transport or economic conditions change.

Better infrastructure can open previously uneconomic markets.

## 11. Contracts and cargo

### 11.0 Opportunity Board / commercial opportunities

The player's primary discovery UI for available business is a **filterable Opportunity Board**. It aggregates only opportunities the company is currently able to discover under the branch/commercial-coverage and communications rules in Section 7.2, plus any public/direct opportunities that the company's current business systems can plausibly receive.

The board can contain:

- one-off transport jobs,
- recurring/framework transport contracts,
- public/state/municipal tenders,
- private customer tenders,
- direct customer offers,
- subcontracting opportunities from other carriers,
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

Cargo gameplay is primarily contract-driven.

Early game emphasizes direct management of individual jobs and vehicles.

Contract types include:

- one-off shipment,
- recurring/framework contract,
- state/public contract,
- carrier subcontract,
- long-term supply contract.

Contract awards should consider transparent factors such as price, capacity, reliability, relevant reputation and customer-specific relationship history. The player must be able to inspect the important decision factors before or after bidding.

Large customers may reserve their most important contracts for carriers with proven history, while still exposing smaller trial jobs that let new entrants build trust.

Contracts can be seasonal or have seasonal volume profiles when the underlying customer demand is seasonal. A seasonal contract must show its expected calendar profile before signing, including peak months/periods, expected baseline volume and likely surge range. Historical plausibility applies: early eras should not generate modern mass-tourism or modern consumption patterns simply because the calendar says summer/winter.

All contractual periods and volume-rate units use Section 3's calendar. A monthly volume covers 14 game days; a yearly term covers 168. Notice, cancellation, expiry and renewal must use that same basis.

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

### 11.9 Cargo batches

Cargo is simulated in batches, not per kilogram/item.

A batch tracks type, quantity, origin, destination, deadline/quality constraints and contract.

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

Stations have small implicit handling/storage capacity for minor shipments.

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

Primary modes in the base game, subject to the selected year and technological availability:

- road transport,
- railway,
- inland water/shipping,
- urban transport: bus, tram, trolleybus, metro.

The early horse-drawn/dostavnik startup progression and the emergence of the first railways are principally Early Ages DLC content. Horse-drawn or older technology can still appear in the base world where appropriate; starting in a later year does not unlock unavailable future modes or force all existing modes to be used by the player.

Aircraft are explicitly out of current scope.

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
- technology.

The player normally requests service capacity, not exact second-by-second paths.

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
- departure times or interval,
- validity date range,
- train length/type,
- expected dwell/turnaround,
- required direction on each section,
- number of calls/movements generated by the pattern.

The normal player workflow is:

1. **Choose validity** — use the Service Pattern calendar or override with a temporary/seasonal date range.
2. **Choose service level** — guaranteed, standard or flexible/ad-hoc where offered.
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

Real train movement still uses local section/block reservations. A train reserves only near-future sections, not its entire route.

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

Steam locomotives and other one-directional equipment cannot magically reverse at a terminus.

Possible solutions include:

- run-around tracks,
- turntables,
- reversing triangles,
- second locomotive,
- later bidirectional trainsets.

### 14.3 Train feasibility

Before dispatch, the game calculates whether a consist can physically operate the planned route based on weight, traction, gradients and infrastructure.

The player should not discover a predictable traction problem only after the train stalls.

Heavy trains may need helpers/bank engines on specific sections.

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

### 14.5 Passenger classes and comfort

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

A retrofit can extend usefulness, but cannot make a fundamentally obsolete vehicle equal to a modern one.

Availability is evaluated against the selected start year and region. Do not gate an already established historical feature behind replaying its earlier invention solely because a new company was founded in 1925, 1950 or 1975; compatible vehicles and installed equipment are still required.

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
- used-vehicle age, mileage/hours and condition.

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

### 15.4 Dealer maintenance and service contracts

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

If no technically/legal continuous rail route exists from the asset's current location to the player's receiving network, the default fallback is **specialized heavy road transport**.

Rail vehicles are transported **one physical vehicle per suitable heavy-haul movement by default**, unless a later explicitly supported transport system can safely carry more.

The transport should be visually represented as a recognizable oversized/special movement, typically including:

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

A large purchase can therefore create a delivery sequence. Example: five locomotives bought without a rail connection may require five separate heavy-haul movements over several days/weeks rather than all appearing at once.

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

Depots/stations maintain real inventories.

The player can:

1. buy delivered supply,
2. buy at source and transport it personally,
3. buy at source and hire another carrier through the shared External Transport Order in Section 30.1,
4. use a recurring supply contract.

Automatic reorder thresholds can be configured and later delegated.

Recurring supply agreements can use Auto-renew under Section 11.12. Renewal extends the commercial agreement; inventory reorder thresholds separately determine actual orders and deliveries. Renewing a supply contract never fills a depot automatically or bypasses physical transport.

Electricity is purchased through physical grid connections/capacity rather than moved as cargo wagons.

## 19. Infrastructure ownership and access

Infrastructure can be:

- state/public,
- municipal,
- privately owned.

### 19.1 Public infrastructure

A state may commission construction and retain ownership.

It can later tender transport services over the infrastructure.

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
- ticketing/booking facilities where historically relevant,
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
- accessibility,
- interchange quality,
- operating/staff requirements.

Platform length is physical. A train that is longer than the usable platform cannot be treated as fully accommodated without an explicit operational rule/penalty.

Passenger circulation matters at an aggregated level. The game does not need to simulate every person through every doorway, but station design should calculate practical flow constraints from entrances, platforms and connections. Representative visible pedestrians should follow the actual layout.

A station can therefore become a bottleneck even when the surrounding railway still has track capacity.

### 20.1 Passenger station progression

Available station modules evolve with history and technology.

Small stations can rely on simple buildings, platforms and manual ticketing where suitable. The available catalogue is initialized for the selected year; founding a new company in a later year does not reset station technology to the beginning of railways.

Depending on era, station modules can include:

- larger covered platforms,
- improved passenger circulation,
- underpasses/footbridges,
- electric lighting,
- modern information systems,
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
- baggage/cargo handling where relevant,
- shunting/turnaround requirements,
- interchange capacity.

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

Passenger platforms are normally allocated **dynamically to Trips according to station capacity and compatibility**, rather than permanently belonging to one operator.

A station can therefore serve several operators at the same time as long as its real infrastructure can accommodate their services.

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

### 29.1 Ownership and acquisitions

The player can buy shares in competitors, receive dividends, acquire controlling stakes or buy them outright.

Acquired companies can remain independent subsidiaries or be integrated.

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

Possible arrangements:

- through-ticketing,
- sale of partner seats,
- reserved seat allocations,
- integrated transfer/rebooking arrangements.

A through journey can use multiple operators under one itinerary/ticket.

Missed connections and reliability influence passenger attractiveness.

## 31. Pricing

Early game pricing is manually controlled.

Later, pricing can be delegated to managers by scope:

- division,
- region,
- group of lines,
- specific service.

Managers can optimize within player-defined constraints such as target margin, occupancy or competitive position.

Lower-level manual settings override delegated policies.

## 32. Service lines and timetables

Regular passenger lines are available from the start, and freight services can use either scheduled or demand-driven operating patterns.

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

### 32.3 Feeder and connection relationships

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

The system must show the resulting expected transfer quality and any fleet/capacity consequences.

Later dispatching and information technology can automate connection coordination more effectively, but physical travel and actual delays remain real. A connecting vehicle cannot teleport or ignore infrastructure constraints simply because services are linked.

### 32.4 Line-level stop service modes

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

### 32.5 Vehicle assignment from fleet pools

Trips normally receive concrete vehicles/consists dynamically from the relevant regional fleet pool rather than from permanently fixed vehicle-to-line assignments.

A Line or Service Pattern can still define:

- required vehicle capabilities,
- preferred consist family/type,
- preferred or required **operating/dispatch depot**,
- fallback operating depots,
- minimum reserve policy.

Parking and maintenance are separate from the Line's operating depot. Individual assets or their fleet group can have separate parking and maintenance facility preferences.

The timetable planner must include real depot-to-service positioning, parking needs, maintenance windows and necessary repositioning movements when calculating required fleet size and feasibility.

If a Service Pattern includes locomotive exchange, the planner must also validate that each exchange point has suitable local traction capacity. It must not assume a replacement locomotive can appear from nowhere or make two locomotives perform pointless long-distance deadheads from the same depot.

A specific vehicle may be manually pinned to a Line/Pattern as an override where the player wants that level of control, but this is not the default operating model.

### 32.6 Crew requirement planning

Service planning must validate both vehicle availability and aggregated crew capacity.

For each Service Pattern, the planner estimates:

- total operating hours,
- peak simultaneous crew demand,
- day/night/weekend staffing burden,
- whether crew changes are required,
- suitable locations for those changes where applicable,
- spare crew margin after the timetable is activated.

The planner should warn when a timetable is technically possible with vehicles but cannot be covered by available qualified staff.

Later managers can automatically adjust staffing targets or propose timetable changes, but they cannot create crew capacity that the company does not actually employ.

Crew planning remains aggregated across the company and does not introduce individual employee pathfinding or home-depot assignment.

## 33. Urban transport

Supported urban modes:

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

### 33.1 Municipal operators

Cities can own normal transport companies that behave as local competitors/operators.

A hybrid model is used:

- cities maintain a minimum service,
- municipal operators can run services directly,
- cities can tender routes, areas or entire networks to private operators.

Municipal operator scope is local: city plus agglomeration, with only limited short intercity reach where plausible.

The player can operate urban transport through a group-wide division or dedicated city subsidiaries.

Optional renewal of a municipal operating contract follows Section 11.12. An agreed extension can renew automatically; a service that requires a new competition must be awarded through that competition rather than retained through a checkbox.

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

Finance is intentionally simpler than the operational/economic simulation.

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

Infrastructure can be bought and sold.

A buyer may:

- continue operating it,
- offer access to other carriers,
- tender services,
- repurpose/rebuild it,
- demolish it and allow urban redevelopment.

Partial asset sales are allowed, e.g. sell the track but keep a depot or station.

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
