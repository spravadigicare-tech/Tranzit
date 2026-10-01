# Tranzit — Station and terminal UI

> **Status: CONFIRMED UI DIRECTION — UI-D14, 2026-09-30.** The player approved a station/terminal overview, requested a station-style arrivals/departures board in a separate window and a list with information about serving Lines, and deferred the track/platform/stand schematic. Exact styling, dimensions and secondary-control placement remain implementation/visual-design details. This specification is not an implemented or tested UI.

Read with [UI_UX_DESIGN.md](UI_UX_DESIGN.md), especially the shared floating-window, contextual-link and pause rules. This focused extension owns station/terminal presentation. [GAME_DESIGN.md](GAME_DESIGN.md), especially Sections 12, 19–20 and 32, continues to own physical facilities, access, capacity, station calls and dispatch. [V1_SCOPE.md](V1_SCOPE.md) still limits first-release transport modes. This screen does not add modes or replace the operating rules.

## 1. Station overview

Use the same movable/resizable window system as other object details. Show the facility name/type, owner, operating state, the player's relationship/access, and an explicit Locate on map action. Do not move the camera merely because the player opened a text link.

The default overview shows what is happening here: physically present vehicles, upcoming arrivals/departures, waiting passengers or cargo where applicable, important bottlenecks and incidents. Distinguish current facts, scheduled calls and estimates. Expose actual platform/handling/passenger-flow constraints rather than one unexplained overall capacity percentage.

Keep **Arrivals and departures / Příjezdy a odjezdy** and **Serving Lines / Obsluhující linky** directly accessible from this overview. A Trip board is not a substitute for the Line list, nor is the Line list a substitute for current departures. Vehicle, Trip, Line, company and facility references use exact-object links under UI-D09.

Below the summary, use openable cards for Capacity, **Passenger access/catchment where applicable**, Equipment and services, Staff, Access and agreements, and Economics. Adapt the contents to the actual facility: a small bus stop should not display irrelevant railway-workshop settings. Keep layout compact and usable in Czech/English at the existing 1080p and enlarged-UI baseline.

### Passenger access / catchment

For passenger stations/stops, show the station's **direct walking catchment** separately from its broader **feeder-reachable catchment**.

Useful information includes:

- economic centre(s) with direct walk access;
- approximate share of each centre within the walking-time threshold where the simulation supports it;
- significant nearby centres that are outside walking reach;
- urban feeder Lines/stops that currently connect those centres to the station;
- expected feeder travel/transfer time, frequency and material capacity/reliability constraint;
- major uncovered passenger origins where known.

Do not shade the whole city market as directly served by a station. A city can have one commodity market while passenger access remains highly local.

Map inspection can show walking-access envelopes based on actual pedestrian access routes and, as a separate layer/treatment, centres reachable through current public-transport feeders. A feeder reach is not permanent station territory: if the Line is suspended, full, badly timed or disrupted, the effective itinerary changes.

Where catchments of several stations overlap, show competing feasible access rather than assigning the neighbourhood exclusively to one station.

For an owned facility, expose management and development actions only to the extent permitted by actual ownership, agreements and regulations. For a third-party facility, emphasize the player's usable services, booked capacity, access conditions and charges. Do not present foreign station management as player-controlled. Public information may be inspected, but competitors' private costs, contracts, allocations and staff data are not revealed merely by opening this screen. Changes and purchases keep their existing validated confirmation workflows.

## 2. Separate arrivals and departures board

### 2.1 Window and appearance

Opening **Arrivals and departures** creates or focuses a separate floating window bound to that station. The station overview stays available. The board can be moved, resized, pinned, minimized and kept open beside a Line or vehicle window. Reopening the same station board restores/focuses it rather than creating redundant copies; boards for different stations may coexist. Its header always names the station and selected view/date.

Make this recognizably a **railway-station information board**, not just another generic management table. Recommended styling within the confirmed dark theme: a near-black surface, high-contrast warm-light lettering, orderly aligned rows and columns, and prominent Arrivals/Departures headings. A restrained split-flap-board influence is appropriate, but no animated mechanical display, live camera, sound effect or separate theme per era is required. Exact colour/font tokens remain design work. Readable proportional labels and aligned time columns take precedence over decorative lettering.

This is the player's management UI, not a newly installed physical passenger-information module. Its look does not grant a station modern equipment, better passenger information or precise forecasts before those capabilities/data exist. Show only available information, with estimates/unknowns and timestamps where relevant.

### 2.2 Contents and controls

Provide **Departures / Odjezdy** and **Arrivals / Příjezdy** views. A combined view may be offered if it remains readable; it is an optional refinement. Keep the station, selected game date and time range explicit. Refresh the current view from the shared simulation; support inspection of other dates without confusing them with Now. Use the shared 14-day-month calendar, including cross-midnight calls.

| Column | Meaning |
|---|---|
| Planned time | The advertised/planned time of this station call, not always the Trip's origin departure |
| Line / service | Recognizable Line identifier/name and, where relevant, the concrete service/Trip identifier |
| Origin or destination | Origin in Arrivals, destination in Departures; direction/via information where useful |
| Operator | The carrier, where known; useful at shared facilities |
| Expected / actual time | Clearly identified estimate before the event, actual time after it; unknown is not on time |
| Platform / stand | The actual current published/known assignment appropriate to the facility; unknown or provisional assignments remain labelled |
| Status | For example on time, expected delay, boarding/loading, arrived, departed, cancelled or platform changed, as supported by real state |

A compact board may combine time/status fields, but the full meaning must remain accessible. Show delay against the relevant planned arrival or departure at this station. Do not imply that the planned time, an estimate and a contracted capacity window are the same thing.

Each row represents a concrete call of a Trip at this facility. Clicking it opens that Trip. The Line name and available vehicle/operator references provide their own direct links. Repeated visits by one Trip must remain distinguishable by call sequence, date and time; a loop must not overwrite its earlier call.

Use chronological ordering and keep selection/scroll stable during updates. Provide usable filters for passenger/freight service and own/all visible operators where relevant. Default to passenger service at a passenger station and to the appropriate operation at a freight facility; never mix freight loading with passenger boarding without a label. The board can show other carriers' visible calls without granting control of those carriers. The absence of private data is not permission to fabricate it.

### 2.3 Operational accuracy

- Platforms/stands are dynamically assigned under existing rules. Display a changed assignment and make it noticeable with text/icon feedback. Before assignment, show a localized pending/unknown value rather than inventing a permanent platform for the Line. This board does not allocate platforms or buy capacity.
- Keep cancelled calls visible with a clear status and reason in the relevant dated view/history. A cancelled or rerouted-away call must not continue looking like an expected arrival. Preserve its explanation and available replacement-service links rather than silently deleting it.
- Demand-driven service without a fixed departure time shows its known condition, readiness or available estimate, not an invented scheduled timestamp. Before a concrete Trip exists, any displayed prospective service is explicitly a Pattern/condition and links there rather than to a fabricated Trip.
- Unlaunched draft Lines, hypothetical timetable previews and proposed stops are not live/public service. Do not generate board rows, ticket sales or missed-departure incidents merely because a saved plan mentions this station. Published/committed future service follows its actual version/calendar and is distinguishable from a draft.
- A route passing through the location without a scheduled station call is not a boarding/alighting service. Do not populate passenger boards or serving-Line entries solely from geometric intersection with the station.
- Planned, expected and actual data use the existing station-call/Trip state and capacity ledgers. The board is not a second timetable engine. Showing the same Trip in several windows never duplicates it or changes its dispatch priority.

Opening, switching or closing the board does not pause/resume the game. It remains inspectable during manual and critical-event pause; those pauses still stop time-driven operation. Auto-pause is caused by a qualifying incident, not by a delayed row becoming visible. Reuse the existing incident identity/notification rules instead of creating a fresh incident on every board refresh.

## 3. Serving Lines and their information

Include a real **Serving Lines** list in the station detail, with a compact preview and access to the full list. It identifies Lines whose relevant Patterns actually call here, not only the vehicles currently present or the next few Trips. A low-frequency or seasonal Line can serve the station even when there is no departure right now.

| Field | Information to expose |
|---|---|
| Line | Name/number and colour with text identification; direct link to the Line detail |
| Operator and mode | Carrier and passenger/freight purpose appropriate to the mode |
| Route and direction | Where the service goes from here, and whether this is a terminus, origin or intermediate call |
| Calling variants | Which Patterns stop here, including differences in route or stopping pattern |
| Service calendar | Operating days, seasonal/date validity and hours where applicable |
| Frequency / departure rule | Known interval, sparse departure times or demand-driven rule; do not manufacture one average interval for irregular service |
| Next call and status | Next applicable call if known, with cancelled/suspended or service-not-today information as appropriate |
| Own-service access | Link to relevant station-call agreements/rights for the player's service where available; not a promise that every platform is theirs |

Group a Line once by stable identity with expandable calling variants/directions. Do not count each Trip as another Line or imply every variant serves this station. Provide own/all visible operators and mode/status filters as needed. Follow Line, Pattern and next-Trip links using the existing navigation and permissions. Operator/Line naming collisions must not merge distinct objects.

Distinguish operating service, temporarily suspended service, future committed service and the player's unlaunched plans. Pending/proposed connections can be inspected separately as plans; they do not count as operating station coverage or public departures. A Line that does not run on the selected date is not automatically closed or suspended. Use the actual calendar/status, not whether the board happens to be empty.

When a confirmed Pattern version removes/adds this station or changes its calendar, update the relevant future view. Existing running Trips and their original calls remain attached to their original version under the canonical rules. Merely editing a future draft cannot remove current calls or rewrite the station's active service list.

## 4. Station schematic deferred

**Do not require or implement a track, platform or stand schematic inside the station window for V1 under this decision.** The player explicitly said to leave the schematic out for now. It remains a possible later UI enhancement, not an unfinished release gate or a reason to delay the approved lists/board.

Use readable lists and the existing main-world map/Locate action instead. This deferral does not remove real track/platform geometry, dynamic allocation, physical capacity, occupancy, construction or world visuals. It does not require a substitute live 3D camera inside the window. Physical site management still uses the existing world interaction and relevant card workflows.

## 5. Acceptance evidence to collect

These scenarios extend the UI evidence required by [V1_ACCEPTANCE_TESTS.md](V1_ACCEPTANCE_TESTS.md); none has been run on a game build as part of this specification.

| ID | Required scenario |
|---|---|
| STUI-A01 | Open a small stop, a passenger station and a freight terminal. Their summaries/cards show applicable operations and real bottlenecks. Inspect owned and third-party sites: only permitted actions and data are available. |
| STUI-A02 | Open a station's board beside its overview and a Line window; move/resize, pin, minimize/restore and open another station's board. Titles remain unambiguous, existing windows/drafts survive, and pause/speed never changes merely from navigation. Verify station-board styling and legible CZ/EN at 1080p/enlarged scale. |
| STUI-A03 | Check arrival/departure views for on-time, delayed, cancelled, changed-platform, unknown-assignment, cross-midnight and repeated-visit calls. Planned/estimated/actual times and call identities remain distinct. No numbered platform is invented or fixed by Line. |
| STUI-A04 | Inspect multiple operators and passenger/freight filters, demand-driven service, a geometric pass-through and an unlaunched draft. No private data, fabricated Trip/time, phantom boarding stop or draft-generated departure appears. |
| STUI-A05 | Inspect a rail station in one economic centre, a nearby walkable centre and a distant centre in the same city market. Direct catchment includes only genuinely walk-accessible demand. Add a real bus feeder from the distant centre and verify feeder-reachable demand appears separately; suspending the feeder removes that itinerary without changing the city commodity market. |
| STUI-A05 | Inspect the serving-Line list with multiple calling/non-calling variants, seasonal and suspended services, a future committed version and a draft. The correct Lines, operators, directions, calendars, next calls and states remain clear and directly linked. |
| STUI-A06 | Change a Pattern with an explicit future effective time, cancel/reroute a call, then save/load. Board/list state uses the same authoritative identities, preserves running Trips and history, and does not duplicate calls, bookings or notifications. Renamed/unavailable linked objects follow UI-D09. |
| STUI-A07 | Complete station inspection, board navigation and calling-Line inspection without any embedded track/platform/stand schematic or live-camera dependency. Main-world geometry and ordinary map navigation remain available. |

## 6. Decision record

| ID | Decision | Status |
|---|---|---|
| UI-D14 | Station/terminal overview and relevant cards; a separate station-style arrivals/departures window; serving-Line list and information; embedded track/platform/stand schematic deferred | CONFIRMED on 2026-09-30 |

This focused decision complements UI-D01–UI-D13 in UI_UX_DESIGN. It does not approve other unresolved screens, depot-specific UI, exact fonts/colours, optional combined-board view or a new passenger-information technology.
