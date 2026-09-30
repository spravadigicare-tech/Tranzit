"""One-off reviewed migration for the 2026-09-30 documentation audit.

This file is removed from the final delivery tree. No game code is generated.
"""
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    'AGENTS.md': 'cb3fe856c1e4aacf51f1e25c1eae55fbe92167cb',
    'README.md': 'aa48e39459c84870ee6b1581c25739b7ad5524c5',
    'docs/CONTRACT_CANCELLATION.md': 'eb6fd21002a6bd0fc4efdd30183b0191be456cc9',
    'docs/GAME_DESIGN.md': 'a433371d4b7721edba3a258af3f5e6a64d496a74',
    'docs/IMPLEMENTATION_STATUS.md': 'c27d4340bff512f0d7508b2f7b1f9ad3b992ad3a',
    'docs/OPENCODE_START.md': '2f42e608c62dfd7006e82a6d0ee42fc6d30b52a2',
    'docs/V1_ACCEPTANCE_TESTS.md': 'e59445d9f6a6a8bc06d4ffe2b745e2eef85149d7',
    'docs/V1_CONTENT_MANIFEST.md': '0597347a2081ffe5cda0f001bed8a8eb6ede600e',
    'docs/V1_IMPLEMENTATION_BRIEF.md': '2b331357d4839346f9aeff2755b874171ea467ee',
    'docs/V1_SCOPE.md': '2af03b6c313db1c91b63faa6e5a3957d5803b94f',
}
texts = {}
for name, expected in EXPECTED.items():
    raw = (ROOT / name).read_bytes()
    actual = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    if actual != expected:
        raise SystemExit(f'Refusing stale migration: {name}: {actual} != {expected}')
    texts[name] = raw.decode('utf-8')


def replace(name, old, new):
    count = texts[name].count(old)
    if count != 1:
        raise SystemExit(f'Expected exactly one match in {name}: {old[:100]!r}; got {count}')
    texts[name] = texts[name].replace(old, new, 1)


def section(name, start, end):
    text = texts[name]
    a, b = text.index(start), text.index(end, text.index(start) + len(start))
    return text[a:b]


G = 'docs/GAME_DESIGN.md'
S = 'docs/V1_SCOPE.md'
B = 'docs/V1_IMPLEMENTATION_BRIEF.md'
T = 'docs/V1_ACCEPTANCE_TESTS.md'
M = 'docs/V1_CONTENT_MANIFEST.md'

# Put detailed cross-release rules in the core, rather than two parallel sources.
vehicles = section(S, '## 4. Historical vehicles remain usable and discoverable', '## 5. Shipment splitting:')
vehicles = vehicles.replace('## 4. Historical vehicles remain usable and discoverable', '### 15.11 Enduring historical vehicle availability', 1)
vehicles = vehicles.replace('The user explicitly requested no artificial end of vehicle availability.', 'Historical vehicle availability has no artificial end date.', 1)
replace(G, '## 16. Maintenance', vehicles + '## 16. Maintenance')
replace(S, section(S, '## 4. Historical vehicles remain usable and discoverable', '## 5. Shipment splitting:'), '''## 4. Historical vehicles remain usable and discoverable

The no-end-year rule applies to the whole game, not only V1. Its complete definition is now in [GAME_DESIGN Section 15.11](GAME_DESIGN.md#1511-enduring-historical-vehicle-availability): permanent model discoverability, finite actual offers, serviceable physical assets, economic external-support scarcity and a real in-house support alternative. Horse-drawn equipment can survive into 1900 without enabling an Early Ages start.

This section is a release reminder, not a second vehicle-availability specification.

''')
cargo = section(S, '## 5. Shipment splitting:', '## 6. Save, interaction')
cargo = cargo.replace('## 5. Shipment splitting: one order, many physical portions', '### 11.9 Shipments and physical cargo lots', 1)
cargo = cargo.replace('It is the executable batch concept called CargoBatch in the core design, not a second competing cargo subsystem.', 'It is the sole executable cargo-batch entity; do not create a second cargo subsystem.', 1)
cargo = cargo.replace('### Units and indivisibility', '#### Units and indivisibility', 1).replace('### Physical and commercial invariants', '#### Physical and commercial invariants', 1)
allocation_start = cargo.index('### Allocation policy consistent with the core design')
state_start = cargo.index('Reservations can pass through', allocation_start)
recovery_start = cargo.index('Cutoff release is responsibility-aware.', state_start)
replan_start = cargo.index('On terminal/route/Trip disruption', recovery_start)
cargo = cargo[:allocation_start] + '''#### Allocation and execution lifecycle

The single allocation policy is defined in Section 11.0.1: physical compatibility, protected/guaranteed obligations, firm recurring/framework cargo, confirmed one-off jobs, then spot cargo. Deadline/quality urgency and stable booking order apply within a tier. No weighted profitability score or ageing rule may override protected commitments. A permanently saturated tier cannot promise starvation prevention; expose the shortfall and propose capacity or recovery.

''' + cargo[state_start:recovery_start] + '''Cutoff responsibility and recovery use Section 11.0.1. The lot retains its readiness state, cause/responsibility for a missed transfer and current recovery assignment; rebooking does not reset that history or release another protected commitment.

''' + cargo[replan_start:]
old_cargo = section(G, '### 11.9 Cargo batches', '### 11.10 Multi-leg logistics')
replace(G, old_cargo, cargo)
replace(S, section(S, '## 5. Shipment splitting:', '## 6. Save, interaction'), '''## 5. One shipment, multiple physical lots and Trips

The canonical model and complete invariants are in [GAME_DESIGN Section 11.9](GAME_DESIGN.md#119-shipments-and-physical-cargo-lots). `Shipment` is the commercial consignment, `CargoLot` its independently located physical portion, `TransportPlan` the versioned execution chain and `TripAllocation` the quantity reserved on a specific Trip/stop interval. There is no competing batch subsystem.

V1 must support one 100 t shipment using 40 + 40 + 20 t inbound and 70 + 30 t onward capacity after actual transfer handling, preserving quantity, age, quality, obligations and lineage. Reservation changes never move physical cargo. The sole freight-priority policy is in GAME_DESIGN Section 11.0.1, including responsibility-aware cutoffs and protected recovery.

''')
texts[G] = texts[G].replace('CargoBatches', 'CargoLots').replace('CargoBatch', 'CargoLot')
replace(G, 'Instead, each contract uses a **Transport Plan** describing how the complete customer obligation is physically fulfilled from contractual origin to contractual destination.', 'Instead, a contract defines a reusable **Transport Plan** template describing fulfilment from contractual origin to destination. Each shipment or passenger-group execution uses a versioned instance of that plan. Replanning one shipment must not mutate the template or the execution state of other shipments. The cargo identities and accounting are defined in Section 11.9.')

# Authority and release boundaries; keep the wider design rather than delete it.
replace(G, '> **Related specification:** [CONTRACT_CANCELLATION.md](CONTRACT_CANCELLATION.md) defines the current proportionate cancellation and early-capacity-release rules.', '> **Related specifications:** [V1_SCOPE.md](V1_SCOPE.md) defines the approved first-release boundary; this document also covers the wider base game. [CONTRACT_CANCELLATION.md](CONTRACT_CANCELLATION.md) owns proportionate cancellation and early-capacity-release rules. Detailed cargo and vehicle-availability rules are centralized here in Sections 11.9 and 15.11. Document responsibilities are defined in [AGENTS.md](../AGENTS.md).')
replace(G, 'The first playable world is based on real European geography, initially focused on Central Europe. The first production scope should prioritize areas corresponding to modern Czechia plus nearby Central European regions; Germany, Austria, Hungary and Poland are natural early expansion targets.', 'The first playable world covers the entire territory corresponding to present-day Czechia plus adjoining parts of Germany, Poland, Austria and Slovakia, as defined in V1_SCOPE. These modern geographic labels describe coverage, not the jurisdictions of 1900. The exact clipping polygon is an authoring deliverable; Hungary and further European territory are later expansion possibilities, not substitutes for the approved adjoining coverage.')
replace(G, 'The base game\'s default/earliest selectable start is **1900**. New games can also start in **1925, 1950 or 1975**.', 'The wider base game\'s default/earliest selectable start is **1900**, with later presets **1925, 1950 and 1975**. First-playable V1 requires only the 1900 preset, with continued historical progression; the later presets remain future base-game scope.')
replace(G, 'Primary modes in the base game, subject to the selected year and technological availability:', 'Primary modes in the wider base game, subject to the selected year and technological availability:')
replace(G, 'Aircraft are explicitly out of current scope.', 'First-playable V1 implements rail and road freight/passengers, including intercity and local buses. Water, tram, trolleybus and metro operation remain later base-game scope. Aircraft are explicitly out of current scope.')
replace(G, 'Supported urban modes:', 'Wider base-game urban modes (only buses are required in first-playable V1):')
replace(G, '## 42. Current out-of-scope / deferred\n', '## 42. Current out-of-scope / deferred\n\nV1-specific deferrals are water, tram, trolleybus and metro operation and the 1925/1950/1975 new-game presets. These remain wider base-game goals, distinct from the broader deferred list below.\n')
replace('README.md', 'Only 1900 is implemented for the first playable target.', 'Only the 1900 preset is required for the first playable target; it is not yet implemented in the inspected documentation-only baseline.')
replace(G, 'Finance is intentionally simpler than the operational/economic simulation.', 'Finance is intentionally simpler than the operational/economic simulation. The single accounting unit is literally `money` in both Czech and English, with localized number formatting but no historical currency switching, currency symbols or foreign-exchange subsystem. Use exact fixed-point/integer money postings; Sections 7.1 and 38.1 govern startup debt.')

# Office bootstrap is not a hidden branch/discovery bypass.
replace(G, '- inspect opportunities;\n- buy vehicles and arrange facilities.', '- inspect public setup costs and eligible public/direct opportunities; routine local jobs remain undiscovered until commercial coverage exists under Section 7.2;\n- buy vehicles and arrange facilities.')
replace(B, 'The UI can preview setup opportunities and costs without granting the commercial benefits of an unbuilt branch.', 'Before a branch is operational, the UI may preview premises/seller/setup costs and public aggregate market indicators, not reveal the hidden routine local Opportunity Board or allow acceptance of undiscovered jobs. Eligible public/direct opportunities still follow Section 7.2. Setup previews do not grant branch benefits.')

# Ticketing has an explicit non-through-stock exception and unpaid-boarder rule.
replace(G, 'The volume of onboard ticket sales itself does not add station dwell time or create extra per-passenger staffing simulation.', 'Ordinary onboard ticket sales do not add station dwell when staff can circulate while running. Non-through compartment stock is the explicit aggregate station-dwell exception in Section 14.5. Neither case creates per-passenger staffing simulation.')
replace(G, 'A passenger must be able to acquire a valid ticket/reservation through at least one suitable channel for the intended itinerary.\n\nIf no usable sales channel exists, that journey option becomes less attractive or unavailable even if the physical vehicle has spare seats.\n\nThe Line Planner should therefore flag:\n\n> **Ticket sales unavailable at [boarding point]**\n\nwhen a passenger stop has no viable ticketing path for the configured service/reservation policy.', '''A paid journey requires a usable sales channel; a reservation-required zone additionally requires confirmed capacity before boarding. Without a way to confirm that reservation, the reservation-required option is unavailable even if physical space exists.

Do not confuse ticket sales with physical boarding. Open/optional unreserved boarding follows the explicit onboard-sales rule above: an otherwise eligible passenger may board free uncommitted capacity without a pre-purchased ticket, but if no eligible selling crew or other actual payment channel collects the fare, that journey earns no fare. Do not fabricate revenue, a reservation or a fare-evasion minigame. Existing prepaid tickets remain valid and are never charged twice.

The Line Planner must distinguish **Ticket sales unavailable / fare revenue at risk** from **Reservation unavailable / boarding blocked**. Forecast revenue uses actual reachable sales channels and the applicable boarding policy, not the existence of seats alone.''')
replace(G, '1. protected passenger-contract allocations;\n2. confirmed individual reservations;\n3. open/walk-up passenger demand.', '1. protected passenger-contract allocations;\n2. confirmed individual reservations;\n3. open/walk-up passenger demand.\n\nThese tiers allocate uncommitted capacity; they are not permission to take an already confirmed seat away. A newly accepted group contract must fit around existing confirmed individual reservations, or obtain an explicit re-accommodation/amendment before acceptance. Carrier-caused capacity loss uses the recovery rules rather than silently selling the same seat twice.')

# Separate facing, physical travel direction and position at the consist end.
replace(G, 'Steam locomotives and other one-directional equipment cannot magically reverse at a terminus.\n\nPossible solutions include:\n\n- run-around tracks,\n- turntables,\n- reversing triangles,\n- second locomotive,\n- later bidirectional trainsets.', '''Keep **physical facing**, **permitted travel direction** and **position in the consist** separate. A steam locomotive may run backwards only when that model and operation permit it, with the defined speed/visibility/route limits. It never flips its model or orientation by changing a timetable direction.

A run-around moves a locomotive to the other end of the consist but does **not** turn the locomotive's physical facing. A turntable or reversing triangle turns it through real movement. These are not interchangeable capabilities.

A terminal solution can use a valid run-around plus permitted reverse running, actual turning facilities, a second suitably positioned locomotive, or later bidirectional equipment. Feasibility checks the complete combination, including track access, coupling/control and resulting performance. Section 16.3 applies the same distinctions to rescue/backing movements.''')

# Do not make a modern low-loader a mandatory fallback in 1900.
replace(G, 'If no technically/legal continuous rail route exists from the asset\'s current location to the player\'s receiving network, the default fallback is **specialized heavy road transport**.', 'If no technically/legal continuous rail route exists, **specialized heavy road transport** is a possible fallback only when the current era has suitable real equipment, handling/loading capability, a valid route and an available provider. It is not a guaranteed 1900 delivery method. If none exists, show a delivery blocker and offer another seller/receiving point, a real connection project or another explicitly supported period-compatible solution; do not fabricate modern equipment.')
replace(G, 'The transport should be visually represented as a recognizable oversized/special movement, typically including:', 'Where supported by the period and provider, the transport is visually represented as a recognizable oversized/special movement. A later-era example includes:')
replace(G, 'Example: five locomotives bought without a rail connection may require five separate heavy-haul movements over several days/weeks rather than all appearing at once.', 'Later-era example, when compatible road transport exists: five locomotives bought without a rail connection may require five separate heavy-haul movements over several days/weeks rather than all appearing at once.')

# Preserve the approved between-Trip energy model, rather than invent an exception.
replace(G, 'Normal scheduled fueling/charging takes place **between Trips** at a physical compatible facility.', 'Normal scheduled fueling/charging, including traction coal/water and aggregate animal-traction supplies, takes place **between Trips** at a physical compatible facility. An ordinary intermediate stop in the same Trip does not silently enable refueling. Passenger toilet/water servicing is not traction refueling.')
replace(G, 'If none exists, the Trip is not ready and the UI explains the reason, for example:', 'If none exists, the Trip is not ready. A longer service can be planned as successive Trips with a real fueling turnaround, or use a physically valid traction exchange whose locomotives have sufficient energy for their assigned segments. Such planning retains passenger/cargo custody, capacity and commercial obligations; it never resets fuel by renaming a Trip. The UI explains a remaining blocker, for example:')
replace(T, '| V-07 | Long duty exceeds remaining fuel or inspection interval | Feasible intermediate service plan or blocked dispatch before predictable failure |', '| V-07 | Long duty exceeds remaining fuel or inspection interval | Feasible between-Trip service/turnaround or valid traction exchange; otherwise block before predictable failure. No implicit mid-Trip refueling |')

# Timetable feasibility, public departure promises and lifecycle boundaries.
replace(G, 'The system must therefore solve the whole chain coherently. A station time cannot be accepted if the preceding leg cannot physically reach it or if the following capacity window cannot be reached after dwell.', 'The system must solve the whole chain coherently using the **midpoints of the candidate windows**, not merely show that the windows overlap some possible trajectory. For every leg, planned arrival minus planned departure must cover the feasible running profile and its selected recovery margin; planned departure after a call must cover required dwell/preparation. If individually valid windows have infeasible midpoints, request a different complete slot chain or reject the proposal. Do not silently move the published time away from its accepted midpoint to make the calculation pass.')
replace(G, 'Within the player\'s own network, or where competing movements have equivalent contractual rights and a tie/recovery choice genuinely exists, operational priority can be used as a dispatcher preference.', 'Operational priority may resolve a choice between the same company\'s services with equivalent contractual rights. It is not a player-controlled tie-break against another operator. Equal-rights inter-operator conflicts use the infrastructure owner\'s published neutral dispatch rule with stable ordering, subject to safety and contractual recovery; ownership and a private High setting confer no extra rights.')
replace(G, 'The midpoint rule applies to timetable construction. Real trains can of course arrive/depart elsewhere inside the valid window as operations unfold.', 'The midpoint rule applies to timetable construction. Actual arrivals and permitted movements can occur elsewhere inside the valid window, but a passenger Trip must not leave a published boarding stop **before its advertised departure time** merely because the slot allows earlier use. Skipping a request stop must not cause early departure from a later published boarding stop. Wait/regulate at a valid location with real occupancy. Freight and non-boarding operational movements follow their explicit cutoff/access terms. Late operation and its consequences remain possible.')
replace(G, 'Trips before the effective boundary are generated/operated under the old version.\n\nTrips on or after the boundary use the new version.\n\nA Trip already in progress when the boundary passes keeps the version under which it departed; it is not rewritten mid-journey.', '''Use the Trip's **scheduled origin departure timestamp** to select the Pattern version, not its generation time or delayed actual departure. Trips scheduled before the boundary retain the old version even if they depart late. Trips scheduled at or after the boundary use the new version.

Already generated future Trips, tickets, allocations and preparation tasks on the replaced version must be explicitly migrated/revalidated or cancelled/recovered. Old and new generation must not create duplicate occurrences. Preparatory movements and loaded cargo cannot be undone by deleting an object.

A Trip already running keeps its original version and obligations; it is never rewritten mid-journey. Suspension/emergency actions remain separate from version selection.''')
replace(G, 'A Line/Pattern in **Suspended until further notice** remains a real company object with its history, configuration and dependencies, but generates no new commercial Trips after the suspension boundary.', 'A Line/Pattern in **Suspended until further notice** remains a real company object with its history, configuration and dependencies, but cannot start a new commercial Trip while suspension is effective. Stop future generation/sales and explicitly cancel or replan already generated but not departed affected Trips, including delayed departures. Resolve preparation, loaded quantities, reservations and obligations through the impact check; do not only disable the generator and allow its old queue to dispatch.')
replace(G, '> basic turnaround buffer: 2 min  \n> minimum next departure: **10:48**', '> physical minimum next departure: **10:46**<br>\n> additional planned recovery buffer: 2 min<br>\n> planned next departure: **10:48**')
replace(G, '##### Planning versus commitment\n\nBefore the preparation horizon, the planner primarily maintains **feasibility coverage**:', '##### Planning versus commitment\n\nDeferring concrete asset IDs does not defer capacity accounting. Future confirmed work reserves compatible time/capability capacity in the shared ledger, including preparation, maintenance and reserve obligations. Every planner uses those same reservations. Selecting serial-number assets later binds existing commitments rather than creating a second reservation or discovering that the same fleet was promised twice.\n\nBefore the preparation horizon, the planner primarily maintains **feasibility coverage**:')

# Conservation distinguishes a terminal disposition from physical spoilage/return work.
replace(G, '- For each shipment: created quantity equals undelivered physical quantity plus accepted delivered quantity plus explicitly recorded loss/spoilage/return disposition, with no duplicated terminal state.', '- For each shipment: created quantity equals its remaining physical quantity plus accepted delivered quantity plus explicitly completed terminal dispositions, with no duplicated terminal state. Spoiled cargo awaiting disposal and cargo awaiting return are still physical inventory and consume capacity. A completed return/reclassification links the receiving inventory or return shipment and closes the original quantity exactly once; recording a write-off is not permission to erase a physical load. Production, consumption and disposal are explicit inventory transformations, not reservation edits.')

# Keep booking state separate from physical handling and declare small freight capacity.
replace(G, 'Reservations can pass through Planned, Reserved, Committed, Loading/Loaded, InTransit, Unloaded/Completed, Cancelled and Replanned states. Operational loading states and commercial allocation states may be separate state machines. Define transitions explicitly. A committed or loaded part is not casually moved to another Trip; cancellation requires a feasible physical recovery/unloading operation.', 'Commercial allocation state (such as Planned, Reserved, Committed, Cancelled or Completed) is separate from physical handling/custody state (such as Waiting, Loading, Loaded, InTransit or Unloading). Replanning supersedes a versioned allocation and preserves its history; it never rewrites the lot location. Releasing an unloaded reservation requires the applicable contractual approval/recovery, but no fictional unloading operation. Cancelling a partially loaded or running allocation preserves the actual onboard quantity until physical unloading/recovery is possible. A cancelled Trip is not evidence that its load is back in storage.')
replace(G, 'Stations have small implicit handling/storage capacity for minor shipments.', 'A freight-capable station can include a small integrated handling/storage allowance for minor shipments in its definition. That allowance has declared cargo compatibility, physical footprint, finite quantity/throughput and the required staff/equipment. It is not invisible unlimited storage. A passenger-only halt/platform gains no freight-handling capability or free warehouse merely by being a station.')

# Historical date conversion is an engineering convention explicitly delegated by V1.
replace(G, '- Day-of-month dates that do not exist in the game calendar, including historical holidays/events after the 14th, need an explicit documented conversion when content is authored. The exact real-date-to-game-date mapping is still to be specified; do not silently create invalid dates or assume a 31-day month.', '- Imported historical dates use the versioned authoring conversion in DATA_PIPELINE.md: validate the Gregorian source date, retain its original value, preserve year/month and map **every** source day with `game_day = 1 + floor((source_day - 1) * 14 / source_month_length)`. Game-authored dates already use days 1–14 and are never converted again. Gregorian rules exist only in this import step, not runtime billing, schedules or ageing. Colliding mapped events follow prerequisites and stable source-date/ID order.')
replace(S, section(S, '### Historical date input', '## 4. Historical vehicles'), '''### Historical date input

Use the explicit conversion in GAME_DESIGN Section 3.4 and [DATA_PIPELINE.md](DATA_PIPELINE.md). Source dates are validated and retained; imported days are proportionally mapped to 1–14, while game-authored dates are not remapped. This is a documented engineering convention, not an additional historical fact or gameplay clock. The pipeline still requires actual sourced geographic/historical content.

''')
replace('AGENTS.md', 'Historical source dates outside days 1–14 require an explicitly documented conversion in the core/data-pipeline specification before use. The handoff has not silently chosen a conversion formula.', 'Historical source dates use the explicit versioned import conversion in GAME_DESIGN Section 3.4 and docs/DATA_PIPELINE.md. Apply it once to source dates, not to already-authored game dates; runtime systems never use Gregorian period arithmetic.')
replace(T, '| T-08 | Import real dates from 28/29/30/31-day months | Valid source-date checking, documented conversion to 1–14 and stable order for colliding events |', '| T-08 | Import real dates from 28/29/30/31-day months and already-authored game dates | Validate source dates; apply DATA_PIPELINE proportional conversion exactly once; game-authored dates remain unchanged; stable prerequisite/source-date/ID order for collisions |')

# Concise source ownership instead of several independently editable rule copies.
replace('AGENTS.md', 'Together these form the **living source of truth**, not a historical log.', '''Document responsibility is explicit:

- `GAME_DESIGN.md` owns shared game mechanics, including the calendar (3), cargo identities/invariants (11.9) and enduring vehicle availability (15.11).
- `V1_SCOPE.md` owns the first-release inclusion/exclusion boundary. Its summaries link to the shared mechanics rather than redefine them.
- `CONTRACT_CANCELLATION.md` owns the focused ordinary-cancellation calculation and settlement rules.
- The brief and content manifest own engineering guidance and adjustable defaults, not silent product overrides. `DATA_PIPELINE.md` owns documented import conventions.
- Acceptance scenarios define required evidence; `IMPLEMENTATION_STATUS.md` records only observed progress/results. Neither creates a gameplay exception.

There is no universal "last paragraph wins" rule. A genuine mechanics conflict still requires correcting the owning section and its dependent summaries/tests; do not treat a release-scope document or example as blanket permission to override it.

Run `python3 Tools/check_docs.py` and `python3 -m unittest discover -s Tools/tests -v` after documentation edits. These check documentation structure and selected explicit regressions, not the correctness or completion of the unimplemented game.

Together these form the **living source of truth**, not a historical log.''')
replace('AGENTS.md', 'The cargo allocation rules in V1_SCOPE and GAME_DESIGN use compatibility and contractual priority tiers, not one unrestricted hidden score.', 'The canonical cargo rules in GAME_DESIGN Sections 11.0.1 and 11.9 use compatibility and contractual priority tiers, not one unrestricted hidden score.')
replace(B, 'Cargo uses V1_SCOPE Section 5.', 'Cargo uses the canonical GAME_DESIGN Section 11.9, referenced by V1_SCOPE Section 5.')
replace(B, 'Distinguish commercial rail/station slot windows from actual track/platform occupancy. Timetable construction uses compatible offered windows and planned midpoint times under the core design.', 'Distinguish commercial rail/station slot windows from actual track/platform occupancy. Timetable construction validates the complete chain of offered-window midpoints, running margins and dwell under the core design. Early slot tolerance never authorizes leaving a published passenger boarding stop early.')
replace(M, '- direction/turning rules and permitted reverse operations;', '- physical facing, permitted reverse operations and consist-end position; run-around and actual turning are distinct capabilities;')
replace(M, '- required staff/qualification and service/facility families;', '- required staff/qualification and service/facility families; passenger through-circulation capability and any resulting aggregate ticketing dwell;')
replace(M, 'Keep 1900 historical overlays separate from modern geometry sources.', 'Keep 1900 historical overlays separate from modern geometry sources. Apply the versioned source-date convention in DATA_PIPELINE.md once; retain the original dates and provenance.')
replace('docs/CONTRACT_CANCELLATION.md', 'Cancellation charges and retained prepaid amounts for the same cancelled future reservation must be reconciled so that the same loss is not charged twice.', 'Cancellation charges and retained prepaid amounts for the same cancelled future reservation must be reconciled so that the same loss is not charged twice. Settlement is one idempotent ledger transaction per accepted release: distinguish the total cancellation liability, any prepaid amount credited against it, additional cash payable and excess refundable prepayment. Retrying or partially executing a release cannot apply the cap, charge or credit twice.')
replace('docs/OPENCODE_START.md', 'Read `AGENTS.md`, `docs/V1_SCOPE.md`,', 'Read `AGENTS.md`, `docs/DATA_PIPELINE.md`, `docs/V1_SCOPE.md`,')
replace('README.md', '| [Implementation Status](docs/IMPLEMENTATION_STATUS.md) | Current implementation/test evidence and next executable task |', '| [Implementation Status](docs/IMPLEMENTATION_STATUS.md) | Current implementation/test evidence and next executable task |\n| [Data Pipeline](docs/DATA_PIPELINE.md) | Defined date-import convention and still-required data-production work |\n| [Consistency Audit](docs/CONSISTENCY_AUDIT.md) | Review coverage, resolved contradictions and limits of documentation verification |')

# Extend existing test tables without renumbering any original scenario.
insertions = {
'### 4.3 Rail/road topology and resource protection': '''| C-19 | Spoilage or return recorded while cargo still occupies a vehicle/store | Physical inventory/capacity remains until actual disposition; linked return inventory and original terminal accounting balance exactly once |
| C-20 | Replan one shipment using a shared contract Transport Plan template | Only its execution version changes; other shipments, accepted quantities and template remain intact |
| C-21 | Minor freight at an equipped station versus a passenger-only halt | Only declared compatible finite integrated storage/handling is usable; no implicit warehouse or passenger-platform loading |
| C-22 | Release an unloaded reservation; end a Trip with cargo remaining onboard during turnaround | No fictional unloading for a reservation; physically retained cargo still occupies capacity across Trip boundaries and is not billed/delivered twice |

''',
'### 4.4 Vehicles, service and staff': '''| N-15 | Individually valid slot windows have infeasible midpoints | Whole-chain midpoint/running-margin/dwell check rejects or requests different windows; no hidden non-midpoint timetable |
| N-16 | Passenger train is ready in early slot tolerance or skips a request stop | No departure before the published time at a boarding stop; waiting consumes valid physical capacity |
| N-17 | Run-around with a locomotive whose reverse-running speed is limited | Consist-end position changes, facing does not; reverse limits enter feasibility. A turntable/triangle is a separate physical operation |
| N-18 | Different operators request equal-rights conflicting movements | Published neutral stable dispatch rule; neither ownership nor private High operational priority creates an advantage |

''',
'### 4.5 Contracts, passengers and money': '''| V-15 | Corridor and non-through coaches use onboard sales; repeat with prepaid tickets | Ordinary circulation adds no ticketing dwell; only actually required non-through handling adds aggregate dwell; no per-person staffing |
| V-16 | Two future Patterns claim the same compatible fleet before concrete asset selection | Shared interval/capability reservations prevent overcommitment; later asset binding does not reserve the resource twice |
| V-17 | Road turnaround: 4-minute exchange, parallel 2-minute crew change, 2-minute buffer | Physical minimum is 4 minutes, planned turnaround 6 minutes; optional buffer is not charged as mandatory work |

''',
'### 4.6 World, construction, economy and AI': '''| F-17 | Open/optional unreserved passenger boards without a ticket or selling crew | No invented fare; prepaid tickets remain valid; planner shows lost-revenue risk. Reservation-required boarding still needs confirmation |
| F-18 | A new group contract requests seats already sold to individuals | Reject/reduce or explicitly resolve commitments before acceptance; group priority cannot silently displace a confirmed reservation |
| F-19 | A pre-boundary scheduled Trip departs late after a Pattern-version boundary | Retains old version; future generated occurrences migrate once with preparation/cargo preserved; no duplicate Trip |
| F-20 | Suspend with future Trips already generated or a departure delayed past the boundary | No new commercial departure during suspension; running Trips continue unless explicitly recovered; bookings/preparation handled |
| F-21 | Retry prepaid partial cancellation before/after save | Liability, credited prepayment, refund and new cash payment reconcile exactly once with each owner |

''',
'### 4.7 Saves, UI and runtime integrity': '''| W-15 | No active branch, but setup preview and marketplace are available | Public setup information does not reveal/accept hidden routine jobs; eligible public/direct opportunities obey communication rules |
| W-16 | Compare first-release selection UI with wider-design catalogues | Only 1900, rail and road in V1; wider presets/modes are not removed from design or silently enabled; exact approved geographic coverage retained |

'''
}
for heading, rows in insertions.items():
    replace(T, '\n\n' + heading, '\n' + rows.rstrip() + '\n\n' + heading)

replace('docs/IMPLEMENTATION_STATUS.md', 'Last initialized: 2026-09-30, during preparation of the OpenCode handoff.', 'Last reviewed: 2026-09-30, during the repository-wide documentation consistency audit.')
replace('docs/IMPLEMENTATION_STATUS.md', 'Inspected baseline: main commit `0ff59b98d8b9bdcbe3fec32299086bdcdb306c44`. It contained only AGENTS.md, README.md, GAME_DESIGN.md and CONTRACT_CANCELLATION.md. The handoff adds specifications and this ledger, not a Unity game.', 'Audited baseline: main commit `a2b45f570bd91730f8c76d2f6a74058e28853c60`. All ten tracked files were documentation. This audit corrects specifications and adds documentation validation tooling, not a Unity game. Review scope and limitations are in [CONSISTENCY_AUDIT.md](CONSISTENCY_AUDIT.md).')
replace('docs/IMPLEMENTATION_STATUS.md', '- Design/implementation handoff: prepared.', '- Design/implementation handoff: prepared; cross-system documentation audit completed.\n- Documentation lint and validator unit tests: see the audit report and actual CI/local run evidence. These do not pass any game acceptance gate.')

# Write only after every original blob and replacement has validated.
for name, text in texts.items():
    if text != (ROOT / name).read_text(encoding='utf-8'):
        (ROOT / name).write_text(text, encoding='utf-8')
        print(f'UPDATED {name}')
