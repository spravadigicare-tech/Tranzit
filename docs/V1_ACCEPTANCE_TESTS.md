# Tranzit — V1 acceptance tests and release gates

Prepared: 2026-09-30. Initial status of every test in this document: NOT RUN. No Unity implementation, build, benchmark or test pass is supplied by this handoff.

Read with [V1_SCOPE.md](V1_SCOPE.md), [V1_IMPLEMENTATION_BRIEF.md](V1_IMPLEMENTATION_BRIEF.md), [V1_CONTENT_MANIFEST.md](V1_CONTENT_MANIFEST.md), [GAME_DESIGN.md](GAME_DESIGN.md) and [CONTRACT_CANCELLATION.md](CONTRACT_CANCELLATION.md).

## 1. Completion means evidence

A class, an empty panel or a plan is not evidence that a mechanic works. A compiled library is not evidence that the Windows game is playable. An attractive generated image is not an in-engine screenshot. Test code that has not executed remains NOT RUN.

Use these statuses: NOT IMPLEMENTED, IMPLEMENTED/NOT RUN, PASS, FAIL and BLOCKED. Every PASS records build/commit, content version, seed, setup, steps, expected/observed result, command or manual procedure, date and evidence path. A BLOCKED item names the actual missing tool/data/permission, not a speculative excuse.

Release-blocking severity:

- P0: state corruption, duplicated/lost money/cargo/assets, unsafe simultaneous occupancy, teleportation, crash or inability to load a valid save.
- P1: an approved main mechanic, essential player workflow, offline world/content, AI parity, localization or graphical presentation is missing or nonfunctional; ordinary operation deadlocks without a valid explanation/recovery.
- P2: nonblocking polish/balance defects that do not remove or misrepresent a promised mechanic.

No known P0/P1 may be hidden in a release labelled complete V1. Unexecuted essential gates cannot count as passing. Document any P2 separately. The list below is a minimum regression contract, not a promise that all conceivable defects have been eliminated.

## 2. Release gates

| Gate | Required result |
|---|---|
| RG-01 Reproducibility | Clean checkout opens, resolves pinned dependencies, compiles and builds; documented commands, exit codes and logs are usable |
| RG-02 Standalone/offline | Windows x64 player runs through the normal menu and gameplay without the Editor, an account or network data calls |
| RG-03 End-to-end gameplay | All golden journeys below pass through actual player UI with connected simulation, costs and consequences |
| RG-04 Integrity | Cargo, assets, money, reservations, full-train occupancy and facility/staff capacity invariants survive stress and fault injection |
| RG-05 Persistence | Mid-operation save/load and continued operation match the equivalent uninterrupted run within documented numeric tolerances |
| RG-06 Content/presentation | Approved geographic coverage, period initialization, meaningful catalogue/progression, coherent graphics/audio and complete Czech/English interfaces |
| RG-07 Competition/economy | Autonomous real carriers, actual production/demand/supply, credible business openings, loss-making decisions and recoverable disruption |
| RG-08 Performance/stability | Documented normal/developed-network benchmarks at all speeds and long-run soak; no advancing clock ahead of unprocessed essential operations |
| RG-09 Transparency | Every main feature mapped to implementation/tests/evidence; no hidden placeholders, invented passes or unreported blockers |

## 3. Golden player journeys

These must pass on the standalone build, not only a headless fixture. Automated UI coverage may complement manual playthroughs. The normal start uses ordinary resources and commands; developer money, instantaneous construction or spawned player fleets do not count.

### G-01 — From a new company to paid road freight

Start 1900 with the small loan in a documented viable area. Before establishing a branch, inspect only allowed public world/licence/premises information. Confirm that New Game created cash/debt/basic market-entry right but no branch, fleet, depot, activity licence or customer. Choose and fund real office premises/setup, appoint the director, fill minimum office/operating staff, obtain required activity rights, discover a real cargo opportunity, arrange endpoints, acquire and physically receive a suitable road vehicle, arrange parking/service/fuel, accept the job and execute it. Verify the opening tutorial/checklist ends after the first functioning operation. Save and reload while the vehicle is moving. Complete delivery and inspect revenue, every cost and remaining debt. Repeat with tutorial Off and with a deliberate capacity or licence omission; the UI must still explain the real blocker.

Pass: no free branch/fleet/licence/customer, no hidden bypass or forced transport archetype, real delivery and correct balances, opening-only tutorial is optional and does not suppress normal blockers, and every missing prerequisite links to its real workflow.

### G-02 — Railway startup using existing infrastructure

Start a rail-capable opening, arrange branch coverage and permissions, lease or own appropriate yard/depot space, buy/lease physical traction and wagons, arrange delivery, purchase route/station access and define a Line/Pattern. Watch preparation, shunting, loading, the actual Trip and a physically valid return/next duty. Inspect segment/station usage fees and profit.

Pass: a rail service is usable without first building an entire national network, but still consumes real assets, crew, access and infrastructure capacity.

### G-03 — Build and improve the network

Build an industrial siding or passing loop using the free-form tools, contractor, land, materials and real construction stages. Include a bridge or tunnel where appropriate. Operate a service over it. Later extend/upgrade while other traffic continues where physically possible. Compare disruption with/without offered mitigation.

Pass: construction changes the real network and cost ledger; preview/unfinished track is not usable; closures and temporary capacity reductions affect operation.

### G-04 — One shipment over several Trips and modes

Transport one 100 t shipment using road collection, rail trunk and road delivery. Split the inbound rail leg 40/40/20 and the next leg 70/30 after real handling. Display one shipment with independently traceable parts. Delay one feeder, cancel one future allocation and fill one transfer store.

Pass: exactly 100 t is accounted for unless a separately recorded loss is injected; parts recover independently; no duplicated reservation or virtual transfer; final payment/completion follows actual accepted delivery.

### G-05 — Passenger revenue, integrated tickets and a protected transfer

Operate a local bus feeder, rail service and intercity/local onward service with actual walking links and appropriate ticket channels. Define a company/default tariff and an integrated rail/bus tariff system with one single-journey product plus weekly and monthly passes. Use open/optional/required reservations where supported and at least two capacity zones/products. Sell a period pass, use it across a covered transfer, observe actual queues/crowding and verify that pass ownership does not create capacity. Miss a protected connection and reduce the next train's capacity.

Pass: one integrated covered journey does not charge duplicate base fares at each transfer; weekly/monthly validity uses 7/14 game days; a pass sale posts revenue once while covered boardings do not duplicate cash; mandatory reservations still use real segment capacity; sold product terms survive later tariff changes; re-accommodation/rebooking/refund follows rules, money/capacity reconcile, and the player can inspect why passengers chose or rejected the service.

### G-06 — Contract lifecycle and capacity release

Win a recurring contract, reserve its resources, operate it, accept a real volume amendment, review renewal and then release only part of the associated capacity early. Test a price change outside an accepted clause and a required new tender.

Pass: extra work revalidates requirements; auto-renew never silently accepts a changed obligation; cancellation affects only released future capacity, reconciles prepayments and does not charge fictional future use. Non-renewal before its deadline is not early cancellation.

### G-07 — Breakdown, maintenance and enduring technology

Run a steam/legacy road vehicle, schedule external and internal service, force a valid breakdown fixture and recover it physically. In a later-date test state, remove some external provider capabilities through actual market changes and compare support quotes. Retain an equipped/staffed own workshop and operate the old vehicle again.

Pass: no model disappears by date, no unexplained annual fuel/wear penalty, support scarcity has visible reasons, and owned support consumes real resources rather than being a free repair button.

### G-08 — Rival carrier and business expansion

Observe an AI rival discovering, bidding, purchasing/staffing, operating and maintaining a service. Compete for limited stock/slots/customer demand. Open a new region through real rights/presence/access. Buy a minority stake without receiving operational control, then obtain control of a company, issue a Line directive and transfer a needed vehicle/capital while the subsidiary remains AI-managed. Finally test optional integration. Separately acquire infrastructure carrying existing access/capacity commitments.

Pass: the rival cannot cheat to fulfil its bid; region activation/acquisition duplicates nothing; minority ownership grants no invented control; the controlled subsidiary remains AI-managed and must satisfy owner directives through real resources/constraints; harmful owner transfers create real consequences rather than teleportation or protected AI exceptions; integration and infrastructure ownership changes preserve physical state, liabilities, licences/contracts and sold priority rights according to their actual transfer rules.

### G-09 — Delegation, growth and financial distress

Create several Lines and branch workload, appoint a manager, set budget/approval policies and observe a routine delegated action. Deliberately overcommit and encounter negative cash flow. Reduce service, sell or lease-return an asset, borrow/restructure where feasible and continue. Separately test deep insolvency with no recovery path.

Pass: managers respect limits; ordinary staff remain aggregate; distress is a process with understandable causes; bankruptcy does not erase obligations mid-operation without the defined process.

### G-10 — Complete presentation and persistence tour

Visit every major screen in both languages, build/place/select/follow assets, inspect an early and later technology scene, rotate/zoom around a busy station, cross chunk/origin boundaries, save while several systems are active, close and resume offline.

Pass: no debug-only main workflow, missing translation/prefab/material, misleading chart or camera-dependent simulation result; saved state resumes coherently.

## 4. Focused regression cases

Unless marked manual, implement deterministic integration/unit tests as appropriate. Add PlayMode coverage where a scene/UI behaviour is involved.

### 4.1 Clock, units and event ordering

| ID | Fixture/action | Expected invariant/result |
|---|---|---|
| T-01 | Cross day 14/month boundary and December/year boundary | 14-day months, 168-day years and continuous weekdays; no day 15 or leap-day runtime |
| T-02 | Run identical seed and commands to the same game timestamp at 0.5/1/2/4/8/16x | Same authoritative decisions/accounting; only documented numeric tolerance, not speed-dependent income or consumption |
| T-03 | Change speed repeatedly during loading, motion, maintenance and billing | No duplicated/skipped event, payment or movement |
| T-04 | 60 km constant 60 km/h analytical movement without dwell/acceleration | One game hour; 120/60/3.75 real seconds at 0.5/1/16x in an adequately supplied time-budget test |
| T-05 | Several essential events fall within one rendered frame at 16x | Chronological event/occupancy processing, no tunnelling or skipped cutoffs |
| T-06 | Arrival/handling completion/cutoff/departure share a timestamp | Documented stable causal ordering; readiness not inferred from merely approaching a terminal |
| T-07 | Manual pause, pause-menu pause, critical-event pause, focus-loss pause, save/load, close and reopen | Independent pause reasons: closing the menu/focus return removes only its own reason; successful load finishes safely paused; no unauthorized game-time advancement or offline catch-up; focus-loss behaviour follows its On/Off setting |
| T-08 | Import real dates from 28/29/30/31-day months and already-authored game dates | Validate source dates; apply DATA_PIPELINE proportional conversion exactly once; game-authored dates remain unchanged; stable prerequisite/source-date/ID order for collisions |

### 4.2 Shipment inventory and allocation

| ID | Fixture/action | Expected invariant/result |
|---|---|---|
| C-01 | Allocate 100 t across 40/40/20 Trips | One shipment; sum of physical parts equals 100 t; each part has one location |
| C-02 | Repartition arrived compatible parts into 70/30 onward allocations | No resetting age/quality/deadline and no requirement to retain the inbound partition |
| C-03 | 63 t free, 5 t split increment | At most 60 t allocated; exact remaining quantity |
| C-04 | Indivisible machine or handling unit exceeds compatible capacity | No fractional unit and an explicit capacity/compatibility blocker |
| C-05 | Two planners or duplicate commands reserve the same lot/Trip | One atomic valid result, no negative free capacity or double invoice |
| C-06 | Reserve the next leg before predecessor arrival | Forecast reservation allowed only with valid dependencies; loading blocked until actual readiness |
| C-07 | Cancel an uncommitted future Trip | Only affected allocations released/replanned; unaffected parts keep progress and obligations |
| C-08 | Cancel after partial loading or after departure | Physical unload/recovery required; cargo does not instantly return to a terminal pool |
| C-09 | Customer no-show versus carrier/subcontractor missed cutoff | Correct release/protected recovery and responsibility; no automatic downgrade of carrier-fault cargo |
| C-10 | Recovery cargo conflicts with another protected booking | Visible protected-capacity conflict; extra valid capacity/recovery or explicit breach, not secret displacement |
| C-11 | Warehouse full during arrival or before onward loading | Cargo stays at a valid physical location; no disappearance, teleport or capacity overflow |
| C-12 | Part delivered, part spoiled, part waiting | Delivery, loss and waiting reconcile; only accepted quantity earns the applicable payment |
| C-13 | Co-locate different ages/qualities/contracts | No laundering of age/quality/obligations through merging; correct lineage preserved |
| C-14 | A→B and B→C bookings versus A→C booking | Capacity reusable only on disjoint intervals; actual unload releases it |
| C-15 | `do_not_split` versus `deliver_together` | Distinct validated commercial/physical meanings; no false full completion after first arrival |
| C-16 | Load incompatible volume/positions/hazard cargo despite spare tonnes | Reject with the real limiting dimension; nominal tonnes do not imply compatibility |
| C-17 | End a contract or change Pattern version with in-flight lots | Obligations/history remain; only affected future routing changes; no resetting the shipment |
| C-18 | Long wait under permanent high-tier saturation | Explain shortage and propose added capacity; no false guaranteed starvation prevention or priority breach |
| C-19 | Spoilage or return recorded while cargo still occupies a vehicle/store | Physical inventory/capacity remains until actual disposition; linked return inventory and original terminal accounting balance exactly once |
| C-20 | Replan one shipment using a shared contract Transport Plan template | Only its execution version changes; other shipments, accepted quantities and template remain intact |
| C-21 | Minor freight at an equipped station versus a passenger-only halt | Only declared compatible finite integrated storage/handling is usable; no implicit warehouse or passenger-platform loading |
| C-22 | Release an unloaded reservation; end a Trip with cargo remaining onboard during turnaround | No fictional unloading for a reservation; physically retained cargo still occupies capacity across Trip boundaries and is not billed/delivered twice |
| C-23 | Same fresh cargo spends equal simulated time in ambient, ice/refrigerated and later mechanical-cold conditions | Quality/exposure decreases according to the authored condition multiplier; refrigeration slows but never resets/reverses age; save/load and speed changes give the same result for equal simulated elapsed time |
| C-24 | Perishable multi-leg route with handling/storage gaps | Planner includes loading, travel, transfer and storage time in the quality-feasible arrival. A refrigerated trunk leg cannot hide an overlong ambient transfer; upgrading the vehicle/store or shortening the route can make the same shipment feasible |
| C-25 | Perishable stock rotation and market coverage | Equivalent stock is consumed/dispatched by earliest expiry/highest quality risk subject to contractual compatibility. Inventory expected to spoil before use does not count as full usable stock cover or suppress shortage/price pressure like sound stock |
| C-26 | Perishable cargo left untouched in storage | Put fresh cargo into ambient and refrigerated storage, perform no manipulation/UI inspection until after its next quality threshold, and advance simulation time. Scheduled spoilage/quality events fire at the correct game timestamps; ambient cargo degrades/spoils sooner, refrigerated cargo later, and spoiled cargo remains physical inventory occupying capacity until real disposition |

### 4.3 Rail/road topology and resource protection

| ID | Fixture/action | Expected invariant/result |
|---|---|---|
| N-01 | Opposing trains enter a single-track section | Safe reservation/holding; no shared conflicting occupancy |
| N-02 | Train head clears but tail remains on junction/block | Resource stays occupied until full train clears |
| N-03 | A normal platform is closed but another compatible one is reachable | Reassign physically valid alternative rather than wait for an imaginary owned platform |
| N-04 | Free platform is too short or unreachable from train direction | Not selected; explicit length/path explanation |
| N-05 | Guaranteed competitor call conflicts with owner's lower-class call | Contracted rights, safety and valid windows govern priority, not ownership |
| N-06 | Own late train leaves tolerance; separately owner-caused disruption | Out-of-slot versus qualifying reprotection distinguished and charged correctly |
| N-07 | Wide slot window but short dwell, and narrow window with long occupancy | Commercial window and physical occupation remain distinct constraints |
| N-08 | Section preferred/bidirectional/strict-one-way rules; one track under work | Only technically and contractually valid dynamic track use; no global-direction shortcut |
| N-09 | Excess length/weight, insufficient traction, incompatible power/gauge | Pre-activation and final readiness block with actual constraints |
| N-10 | Run-around, turntable and coupling operation, then save mid-operation | Correct orientations, paths and sequential operations; no asset flip or remote assembly |
| N-11 | Deadlock/cycle of resource requests | Prevent unsafe entry or produce an explicit safe recovery plan; never delete/nudge trains through each other |
| N-12 | Road vehicle lacks legal turn/access to a destination entrance | No delivery by proximity; valid alternate route or actionable blocker |
| N-13 | Road congestion, intersection queue and blocked loading entrance | Real delay propagates; no overlap, virtual unloading or arbitrary direction reversal |
| N-14 | Multi-owner Capacity Order partly fails or quote becomes stale | No false fully protected status, double purchase or hidden accepted fees; accepted rights remain traceable |
| N-15 | Individually valid slot windows have infeasible midpoints | Whole-chain midpoint/running-margin/dwell check rejects or requests different windows; no hidden non-midpoint timetable |
| N-16 | Passenger train is ready in early slot tolerance or skips a request stop | No departure before the published time at a boarding stop; waiting consumes valid physical capacity |
| N-17 | Run-around with a locomotive whose reverse-running speed is limited | Consist-end position changes, facing does not; reverse limits enter feasibility. A turntable/triangle is a separate physical operation |
| N-18 | Different operators request equal-rights conflicting movements | Published neutral stable dispatch rule; neither ownership nor private High operational priority creates an advantage |

### 4.4 Vehicles, service and staff

| ID | Fixture/action | Expected invariant/result |
|---|---|---|
| V-01 | Buy 4 dealer vehicles when only 3 physical units exist | Finite inventory and atomic ownership; fourth requires another offer/order |
| V-02 | Buy a wagon at a remote seller and assign immediate departure | Delivery/hauling required; ownership alone does not imply presence |
| V-03 | No valid rail delivery path and no era-compatible specialist provider | Explicit delivery blocker; no modern heavy-haul vehicle in 1900 or teleport fallback |
| V-04 | Manufacturer backlog/material shortage changes after order | Real queued production/delivery changes with visible cause, not on-demand spawning |
| V-05 | Routine service due versus hard safety limit | Player policy can adjust preventive timing but never dispatch beyond hard invalidity |
| V-06 | Two vehicles compete for one workshop bay or fuelling point | Scheduled finite capacity, actual location and return movement; no parallel instant service |
| V-07 | Long duty exceeds remaining fuel or inspection interval | Feasible between-Trip service/turnaround or valid traction exchange; otherwise block before predictable failure. No implicit mid-Trip refueling |
| V-08 | Vehicle immobilized on occupied track/road | Real rescue/tow/worksite path and capacity; consequences propagate |
| V-09 | Lease expires, sale closes or scrap order issued during use | No disappearing asset; contractual obligation and physical handover/disposal remain distinct |
| V-10 | Old model after newer technology appears | Catalogue and valid existing operation persist; no hard end-year lock |
| V-11 | External support declines but own workshop retains capability | Quotes expose provider/parts/capacity costs; internal staff/equipment/supplies still consumed |
| V-12 | Mandatory driver unavailable versus optional service crew shortage | No driverless dispatch; optional shortage follows legal/product limits and actual service effects |
| V-13 | Vehicle ready but crew shift/rest capacity exhausted | Real crew feasibility/recovery, no use of the same qualified capacity twice |
| V-14 | Substitute or shorten a consist | Revalidate operating envelope and protected capacity; correct rebooking/refunds for displaced users |
| V-15 | Corridor and non-through coaches use onboard sales; repeat with prepaid tickets | Ordinary circulation adds no ticketing dwell; only actually required non-through handling adds aggregate dwell; no per-person staffing |
| V-16 | Two future Patterns claim the same compatible fleet before concrete asset selection | Shared interval/capability reservations prevent overcommitment; later asset binding does not reserve the resource twice |
| V-17 | Road turnaround: 4-minute exchange, parallel 2-minute crew change, 2-minute buffer | Physical minimum is 4 minutes, planned turnaround 6 minutes; optional buffer is not charged as mandatory work |

### 4.5 Contracts, passengers and money

| ID | Fixture/action | Expected invariant/result |
|---|---|---|
| F-01 | Small/standard/large startup loans and first repayment | Explicit principal/cash/interest/payment schedule; changing tier does not alter demand/AI/reputation |
| F-02 | Repeat preview/accept, retry after timeout, reload during invoice event | Preview side-effect free; exactly one accepted posting/obligation |
| F-03 | Cancel 2 of 10 slot calls early with prepaid fees | Fee only on affected remaining commitment, disclosed cap/credit, no double recovery or unused per-use fee |
| F-04 | Turn off renewal before deadline; separately after future term committed | First is normal non-renewal; second preserves bound future obligations and visible cancellation terms |
| F-05 | Renew customer contract while slot/crew/supply dependency expires | Missing coverage blocks unattended commitment; no unauthorized supporting purchase |
| F-06 | Seasonal renewal crosses year boundary | Correct season and 14-day-month dates; not an invented full-year volume |
| F-07 | Price/scope change outside indexation or public contract requires tender | Approval/new award needed; auto-renew cannot silently accept or guarantee a win |
| F-08 | New Pattern takes effect while an old Trip is moving | Running Trip retains old version; future bookings/cargo/slots handled by explicit transition |
| F-09 | Suspend until further notice, retain/release slots, then resume | Ongoing costs visible; tickets/contracts preserved; full readiness check on restart |
| F-10 | Sold passenger A→B and another B→C reservation | Correct per-zone per-segment capacity; no needless whole-route seat lock or oversell |
| F-11 | Walk-up passenger denied boarding | Remains in aggregate physical queue or follows explicit abandonment/rebooking; no disappearance/reappearance elsewhere |
| F-12 | Protected missed connection due to own/partner/external cause | Actual acceptable rebooking/partner option or refund; responsibility and compensation distinct |
| F-13 | Old timetable-only versus later realtime information | Passenger choice reacts only to plausibly available information; actual vehicle state unchanged |
| F-14 | Group passenger contract and ordinary tariff bookings share a Trip | Shared real capacity, separate prices/obligations, no duplicate revenue |
| F-15 | Negative cash, salvageable assets and later deep insolvency | Distress process before game over; costs/loans/sales reconcile without free rescues |
| F-16 | Same work at different speeds and game-period rate boundaries | Equal per-work costs and explicit calendar accrual; no 365-day or conventional-month leakage |
| F-17 | Open/optional unreserved passenger boards without a ticket or selling crew | No invented fare; prepaid tickets remain valid; planner shows lost-revenue risk. Reservation-required boarding still needs confirmation |
| F-18 | A new group contract requests seats already sold to individuals | Reject/reduce or explicitly resolve commitments before acceptance; group priority cannot silently displace a confirmed reservation |
| F-19 | A pre-boundary scheduled Trip departs late after a Pattern-version boundary | Retains old version; future generated occurrences migrate once with preparation/cargo preserved; no duplicate Trip |
| F-20 | Suspend with future Trips already generated or a departure delayed past the boundary | No new commercial departure during suspension; running Trips continue unless explicitly recovered; bookings/preparation handled |
| F-21 | Retry prepaid partial cancellation before/after save | Liability, credited prepayment, refund and new cash payment reconcile exactly once with each owner |
| F-22 | Weekly/monthly pass crosses game-month/year boundary | Exact 7/14-day validity on the shared clock; no Gregorian 30-day leakage and no expiry from wall-clock time/pause |
| F-23 | Pass holder boards reservation-required and full services | Fare entitlement does not create capacity; required reservation must exist and full services admit no phantom passenger |
| F-24 | Tariff/system changes after passes were sold | Existing sold product keeps purchased version/price/scope until expiry or explicit refund/recovery; no retrospective surcharge or silent revocation |
| F-25 | One pass used on several Lines/Trips | Cash posted once at sale; per-Line analytical allocation never creates duplicate revenue and uses only information technology can support |
| F-26 | Overlapping local-system and company-network products | Existing valid entitlement covers the leg once; discounts do not stack and no duplicate base fare is charged |
| F-27 | New Game confirmation retried/double-clicked | Exactly one founding loan, starting cash posting and starting-region market-entry grant; no duplicate company/founding benefits |
| F-28 | Save/load before and after founding tutorial completion | Checklist derives from actual state, does not replay purchases/loan/licences and does not restart after first functioning operation |
| F-29 | Tutorial Full/Basics/Off | Only onboarding/context guidance changes; normal blockers, Needs decision, safety/legal constraints and confirmations remain identical |
| F-30 | Interrupted/failed overwrite save | Previous valid save remains loadable; failed write cannot corrupt both old/new state or commit a gameplay action |
| F-31 | Autosave at 0.5× versus 16× for same real play duration | Same configured real-time autosave cadence/rotation; game-speed change does not multiply save frequency |
| F-32 | Pause menu opened from running/manual/critical pause | Closing pause menu removes only menu pause; remembered running speed/manual/critical state remains correct |
| F-33 | Load/quit with and without dirty authoritative state | Warning reflects actual unsaved progress/drafts; Save and exit exits only on successful save; successful load is paused |

### 4.6 World, construction, economy and AI

| ID | Fixture/action | Expected invariant/result |
|---|---|---|
| W-01 | Start without own transport/infrastructure | Viable genuine providers allow first office/delivery/service; no circular mandatory prerequisite |
| W-02 | Missing branch in served city versus simple pass-through | Correct local commercial coverage rule; traversal alone does not require a branch |
| W-03 | Technology exists/research completes versus actual company/object adoption | World availability or research completion only unlocks the applicable capability/options; branch/station/workshop/track/company-system effects require their real owning upgrade/adoption prerequisites and costs, with no automatic retrofit |
| W-04 | Firm runs out of recipe input; transport restores it | Real production/demand response and inventory conversion, not arbitrary contract generation |
| W-05 | Material or contractor capacity shortage during building | Correct stage pause/cost/delivery dependency; no finished asset by timer alone |
| W-06 | Cancel preview versus demolish completed protected station | Free preview cancellation; actual project cost/permission/physical impact for demolition |
| W-07 | Expand corridor while occupied or under partial closure | Safe staged topology update and rerouting; trains/loads not deleted or moved to nearest node |
| W-08 | Unload terrain chunk and rebase origin with active construction/vehicle | Same logical positions/distances/edits after reload; no seam/precision-induced route break |
| W-09 | Activate a macro region twice or after save/reload | Single coherent state transfer; no duplicated firms/assets/inventories or replayed past history |
| W-10 | AI bids for unavailable equipment/slots and faces delivery lead time | Same feasibility limits; credible future investment only, no impossible guaranteed capacity |
| W-11 | Rival sells an asset, acquires company or becomes insolvent | Same ownership and liability rules; no duplicate asset/debt and no cost immunity off camera |
| W-12 | Manager attempts a purchase above budget or forbidden cancellation | Requires approval/rejects; delegated authority never exceeds explicit player policy |
| W-13 | Weather/incident closes a route and later reopens it | Real capacity/speed/supply effects and recovery, clear reason, no flat hidden income modifier |
| W-14 | Later technology/historical event and source-date conversion | Correct prerequisites/date order; no unauthorized new start preset or forced end of campaign |

| W-17 | Research technology that unlocks workshop, track standard and branch/station upgrade | Canonical construction/facility/upgrade options become available; no building, retrofit, vehicle stock, staff or capacity is created by research completion |
| W-18 | Established-era technology for a newly founded later-start company | No pointless rediscovery of already-established world technology; company still pays/builds/adopts required equipment/systems |
| W-19 | Company-wide business system adoption | One simple adoption project where appropriate; capability activates only after completion, while genuine local physical requirements remain separate and no per-site busywork is invented |
| W-20 | Minority stake versus controlled subsidiary | Minority investment cannot issue owner directives; after real control is obtained, the subsidiary stays AI-managed with separate ledgers and only the defined owner-action set becomes available |
| W-21 | Owner Line directive | Player changes a controlled subsidiary Line as an owner directive; subsidiary management must secure real vehicles/staff/capacity/permissions before applying it, or report blockers without cheating |
| W-22 | Intra-group capital/loan/dividend/asset transfer | Explicit postings/ownership changes exactly once; a transferred used vehicle/infrastructure remains physical, may create a real subsidiary shortage and existing commitments are not silently erased |
| W-23 | Acquire/integrate company with active contracts/licences/Trips | Transfer only eligible rights/obligations; change-of-control/non-transferable items remain explicit; no reset/teleport/duplicate asset or running operation |
| W-24 | Buy/sell infrastructure with active third-party rights | Applicable leases/access/capacity/condition/projects survive ownership change; partial sale exposes dependent post-sale access instead of granting it freely |
| W-25 | Major historical/regulatory world event | One canonical event changes the real underlying rules/state; World News explains it, while player-specific actionable consequences appear through UI-D24 only where needed; no duplicate effect or news-driven auto-pause |
| W-26 | Significant company acquisition/insolvency/infrastructure opening | World News records the meaningful known event and links to stable company/asset identities; routine purchases and daily operations do not flood the feed |
| W-27 | Material commodity/economic shift | News shows only supported known causes/exposure and links to affected procurement/operations; no opaque flat income modifier or fabricated company impact |
| W-28 | Early-era remote event and later communication capability | Discovery/publication timing respects information provenance and communication capability; opening News never grants omniscient remote knowledge |
| W-29 | Save/load before and after world-news discovery | Canonical event and read/history state persist without duplicate firing, identity retargeting, hidden-data leak or new pause |
| W-30 | Final HUD/navigation at normal and enlarged UI scale | Company/finance stays upper-left, Search/Layers upper-right, bottom Build + grouped management + Events/time remain usable without duplicated controls or clipped material state |
| W-31 | Global search over known and hidden objects | Known cities/Lines/vehicles/companies/contracts/functions resolve to exact identities; hidden/private/undiscovered objects stay absent and search never issues gameplay commands or activates a region |
| W-32 | Focus loss/return with setting On and Off | With On, focus loss adds only its own pause reason and return removes only that reason; otherwise-running game resumes at remembered speed, while manual/critical/menu/load pauses remain. With Off, focus change does not alter simulation time |
| W-33 | Critical auto-pause and informational-toast settings | Global critical auto-pause On/Off and informational-toasts On/Off affect only presentation/pause policy; no per-event matrix exists, and incidents/history/safety consequences remain intact |
| W-34 | Commit binding actions while simulation is paused | Valid purchase/order/agreement/application/project commands commit exactly once at the current game timestamp; immediate ledger/reservation/ownership effects apply where canonical, while all elapsed processing/physical work remains at zero progress until resume |
| W-35 | Partner-operated through-ticket segment with profitable and loss-making rate | Passenger-facing partner segment uses operator public tariff; seller payable uses negotiated money/km partner rate; difference may be positive or negative, remains visible, and posts exactly once without changing physical capacity rules |
| W-36 | Asymmetric partner-capacity agreement by Line | Configure each company side independently with different enabled state, explicit covered Lines and partner rate. Only listed Lines can be sold through the agreement; selecting all current Lines does not auto-enrol future Lines, and amendment preserves stable identities |
| W-37 | Recurring supply schedules in two-week month | Weekly selected weekdays repeat in both game weeks; monthly mode creates exactly one delivery in Week 1 or Week 2 on a selected weekday or within the selected-week window; pricing may be per delivery or per physical unit, but the UI always shows the computed total for one scheduled delivery and posts it exactly once, with no numeric Gregorian-style recurrence |
| W-38 | Local commodity market price and corridor intelligence | Two market areas with different real production/consumption conditions produce explainable local reference prices and surplus/deficit signals; physical deliveries update stock immediately, each market-area × commodity performs at most two ordinary market calculations per game day, and the reference price moves in at most four lightweight adjustment steps toward the latest target. Ordinary cumulative movement never exceeds ±5% of the prior day's reference price. Stock coverage in days of normal consumption materially changes price pressure; sustained deliveries from surplus to deficit reduce the imbalance and can narrow the price gap over later updates. Market exposes only legitimately known information, does not fabricate a contract, and uses no hidden profit score. A separately classified major shock may exceed the ordinary cap but never exceeds ±15% over one full game day; routine shortages and single delayed deliveries cannot use the exceptional path. |
| W-39 | Intra-city market areas and final consumption | One large city contains at least two local market areas with distinct price/surplus conditions and real firms/endpoints; a shop/service-style final consumer receives only part of its physical input, continues at reduced supported activity, and sustained shortage slows supported local growth/activity instead of instant shutdown; moving goods inside one city still requires physical transport |
| W-51 | Perishable delivery and storage policy | Operate meat/dairy/produce flows with and without compatible cold vehicles/storage. Period-appropriate cold chain makes useful regional/intercity delivery feasible, storage targets respect effective usable life, cold capacity is finite, quality never resets at transfer and spoiled/at-risk physical stock remains accounted until real disposition |
| W-40 | Player-initiated producer/buyer transport proposal | From legitimately known Market data, link a real producer with spare output to a real buyer with unmet demand and submit a transport proposal. Seller/buyer independently accept/reject their commodity terms; the player never becomes speculative owner of the goods and no unknown buyer/cargo is fabricated |
| W-41 | Transparent sealed public-service tender | Authority publishes mandatory service conditions and weighted scoring with price/requested subsidy the largest normal factor plus applicable relevant-mode reliability, commercial reliability, comfort and reputation. Every submitted bid has a concrete feasible service plan; rival bids stay sealed until closing; post-award breakdown explains the winner without AI-only cost/reliability cheats |
| W-42 | Awarded public-service contract lifecycle | Winner changes vehicles/timetable while preserving binding service outcomes, then experiences isolated and repeated failures. Minor failure affects measured history only; repeated/material breach escalates through payment/penalty/cure rules and can end in legitimate termination/re-tender. Test both fixed-term and an eligible indefinite contract |
| W-43 | Contract freight versus open freight | A freight Line carries protected/contract allocations plus open compatible cargo. Open carriage uses the published cargo-category tariff/commodity override and cannot exceed the allowed percentage of a firm's real uncontracted flow; spare capacity does not spawn anonymous cargo or displace protected commitments |
| W-44 | Three public infrastructure contract models | Exercise one state-owned corridor with player service operating right, one Build–Operate–Transfer concession and one publicly co-funded private project. Finance, ownership, access obligations, operating rights, expiry/handover and save/load remain distinct; no fourth generic state-infrastructure-management concession appears |
| W-45 | Canonical commodity chains reach real sinks | Exercise forestry/furniture, food, textile, construction and heavy-industry/energy chains from real production through physical transport to final city/utility/construction/operating consumption. No final product accumulates without a defined sink; iron and steel remain distinct and can be simultaneous recipe inputs |
| W-46 | Historical chain evolution without global replacement | Advance content so chemicals/plastics/natural gas/electronics or another later chain becomes available. Existing plants keep old recipes until modernization, older commodities/routes remain viable where economics support them, and the new chain creates real physical input/output demand rather than a flat production bonus |
| W-49 | Multi-input production cannot substitute missing goods | Run a machinery/furniture/modern-manufacturing recipe requiring at least three parallel commodity groups. Remove one required input while leaving the others abundant: dependent output falls/halts according to the recipe, inventories are not silently substituted, and the shortage/required input is explainable in UI/AI planning |
| W-50 | Electronics is one grouped commodity | Introduce advanced electronics production with chemical, plastics, metal-product and electricity dependencies. Chips/semiconductor components remain internal to the electronics group; downstream modern machinery/spare-parts/consumer recipes consume electronics rather than a separate chips cargo |
| W-47 | Installed assets create maintenance freight | Operate legacy and modern vehicle/factory/workshop/infrastructure assets. Legacy assets consume real basic spare parts while later equipment can require modern spare parts; both must be sourced, transported, stocked and consumed, and introduction of modern parts does not silently rewrite legacy demand. Paying a maintenance invoice alone cannot spawn the needed physical parts |
| W-48 | Coal demand is displaced by real modernization | Advance a mixed region from coal-heavy steam/heating/power/town-gas use into oil/electric/gas alternatives. Coal demand falls only where actual consumers modernize or alternatives become competitive; remaining viable coal consumers/mines continue operating, and local prices/flows adjust rather than coal being globally disabled |
| W-15 | No active branch, but setup preview and marketplace are available | Public setup information does not reveal/accept hidden routine jobs; eligible public/direct opportunities obey communication rules |
| W-16 | Compare first-release selection UI with wider-design catalogues | Only 1900, rail and road in V1; wider presets/modes are not removed from design or silently enabled; exact approved geographic coverage retained |

### 4.7 Saves, UI and runtime integrity

| ID | Fixture/action | Expected invariant/result |
|---|---|---|
| S-01 | Save during loading, coupling, maintenance, building and movement | Consistent transaction boundary, all authority restored, no restarted free task |
| S-02 | Save immediately before/after renewal, payment or delivery event | Event executes exactly once across reload |
| S-03 | Compare uninterrupted run with saved/reloaded equivalent | Matching IDs, RNG state, obligations, queues, inventories, reservations and money within declared tolerances |
| S-04 | Disk full, interrupted write or invalid new save | Previous good save retained; clear error, no false success notification |
| S-05 | Unknown/newer schema, missing content or corrupt checksum | Safe rejection/recovery; no silently removed assets/contracts or partial loaded state |
| S-06 | Supported migration and repeated quickload | Migration preserves invariants; UI subscribes once; no duplicate events or leaked worlds |
| S-07 | Manual save slots, autosave rotation and Continue | Correct newest valid compatible save selection and protected rotation; labels understandable |
| U-01 | Every main screen populated/empty/blocked in Czech and English | No missing keys, untranslated hardcoded messages or broken Czech glyphs |
| U-02 | Switch language, number format and UI scale during play | Stable IDs/money token; no re-created simulation or changed amounts |
| U-03 | Select/drag over UI, rotate construction preview, cancel tool | No click-through purchase, accidental demolition or hidden simulation action |
| U-04 | Inspect rejection, quote, overcrowding, delay and negative margin | Concrete inputs and reason codes shown; corrective action discoverable |
| U-05 | Camera follow/zoom/rotate across busy stations and distant terrain | Coherent visible operation, readable signals/assets, no camera-dependent simulation |
| U-06 | Fresh standalone offline session with game files only | No Editor-only asset paths, network map dependency, missing shaders/models or manual scene setup |
| U-07 | Review presentation screenshots and sound manually | Real in-engine evidence; coherent art rather than labelled debug primitives; audio/settings functional |
| U-08 | Onboarding followed from New Game without debug tools | Reach legitimate first service; guide dismissible; no rule bypasses |
| U-09 | Review core objects/navigation across Czech and English | Canonical UI_GLOSSARY labels are used consistently; Line/Service Pattern/Trip, Shipment/Cargo portion/Transport plan and order/agreement identities are not conflated |
| D-01 | Run build/test script with invalid Unity path or hung process | Nonzero exit/actionable log and timeout; no endless wait or false completion |
| D-02 | Clean rebuild from pinned content/package versions | Reproducible definitions/IDs and useful change report; no dependence on another developer's Library folder |

## 5. Combination and invariant testing

Test interactions, not only individual systems. Required high-risk combinations include:

- split shipment + delayed feeder + saturated next Trip + protected booking;
- short-formed train + already sold class capacity + protected passenger transfer;
- infrastructure owner fault + missed slot + downstream customer SLA;
- construction closure + busy yard + emergency rescue;
- renewal + changing Pattern version + prepaid partial cancellation;
- AI purchase + player purchase + the same final dealer vehicle;
- obsolete technology + workshop queue + fuel/parts shortage;
- active/macro transition + in-flight import + save/load;
- origin rebase + long train tail spanning several blocks;
- save boundary + event retry + money/quantity commitment.

Run representative short fixtures across all six running speeds, detailed/standard/remote presentation states, and before/during/after-save boundaries. Use pairwise selection for routine combinations and full combinations for conservation/occupancy/save-critical cases. Do not substitute one speed or one camera view for the whole test matrix.

Add randomized/property tests with reproducible seeds for sequences of reserve, split, load, unload, replan, cancel, deliver, lose/spoil and restore operations. Assert nonnegative inventory, exact transport conservation, unique asset ownership/location, segment-capacity bounds and idempotent money postings after every committed transition. Keep failing seeds as permanent regressions.

Shipment conservation counts each quantity in one mutually exclusive current or terminal state. Production/consumption are explicit transformations, not transport events. A cancelled reservation is not destroyed cargo. A refunded ticket is not an additional passenger. State these accounting domains precisely in test code.

Full simulation bit-for-bit equality across arbitrary CPUs is not promised. Within the same supported build/runtime, require deterministic logical outcomes with explicit geometric/numeric tolerances. Monetary and integer cargo accounting must remain exact.

## 6. Performance, long-run and graphical verification

Use the workload definitions in V1_CONTENT_MANIFEST. Record actual graph nodes/edges, trains, wagons, road vehicles, Patterns, active groups, regions and AI companies so an empty scene cannot masquerade as a large-world test.

Run each workload after warm-up at 0.5/1/2/4/8/16x, with normal camera and busy-station views, and record requested/achieved time ratio, frame p50/p95/p99, simulation step cost, memory/GC, event backlog, path-cache behaviour and save/load duration. A displayed 16x button is not a 16x benchmark.

Perform a multi-hour wall-clock soak with active services and recurring saves, plus headless multi-year tests for event/calendar/contract stability. Developer fast-forward fixtures are permitted for tests but must not become a player setting beyond 16x. Include year boundaries, multiple seasonal renewals, technology introduction and an evolving supplier/competitor economy.

Check for unbounded history/event/booking growth, repeated whole-network searches, resource starvation, stuck vehicles and delayed operations hidden by an advancing calendar. Historical archives may be compacted, but outstanding obligations and audit necessities cannot be discarded.

Visual evidence must include the 1900 world overview, a town/station at useful detail, road freight/passenger operation, a steam consist, a junction/yard operation, a bridge/tunnel, a construction stage, a multi-leg cargo detail, a busy passenger transfer, later progression and localized management panels. No missing materials, stretched default objects or debug labels standing in for assets.

## 7. Evidence template

Use one entry per actual run or a machine-readable equivalent:

```
Test ID:
Status: NOT RUN | PASS | FAIL | BLOCKED
Commit/build:
Editor/player version:
Content manifest/hash:
OS/CPU/GPU/RAM/settings:
Seed and simulation timestamp:
Setup:
Commands or manual steps:
Expected:
Observed:
Evidence path:
Defect/blocker and severity:
Retest result:
```

For the requirement matrix, maintain:

```
Requirement ID | Scope/core section | Implementation paths | Test IDs | Latest actual result | Evidence | Remaining work
```

Final release handover includes the playable Windows build, exact build instructions, change summary, completed matrix, real test/performance results and known issues. The current handoff only specifies this work; all game tests start unexecuted.
