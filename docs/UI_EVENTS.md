# Tranzit — Events, incidents and notifications UI

> **Status: CONFIRMED UI DIRECTION — UI-D24, 2026-09-30.** The player accepted one event centre split by player-action need, grouped root-cause incidents, lightweight informational toasts, persistent history and optional per-object Follow notifications. Critical-event auto-pause continues to follow UI-D08. Exact layout dimensions, iconography, event thresholds and per-event override settings remain design work. This specification is not an implemented or tested UI.

Read with [UI_UX_DESIGN.md](UI_UX_DESIGN.md), especially UI-D07 (floating windows), UI-D08 (critical auto-pause), UI-D09 (exact-object links), UI-D15 (minimalism/tooltips) and Section 7, plus [UI_NEWS.md](UI_NEWS.md) under UI-D40. This focused document owns the player-company event-centre and notification presentation. Gameplay systems retain ownership of incidents, decisions, deadlines, recovery policies and consequences. UI-D40 separately owns public/world news and campaign-history presentation.

## 1. One event centre

The fixed bottom-bar event/decision indicator opens one movable/resizable **Events / Události** window. Use four primary views:

1. **Needs decision / Vyžaduje rozhodnutí**
2. **In progress / Probíhá**
3. **Information / Informace**
4. **History / Historie**

The grouping is based primarily on **what the player needs to do**, not on which internal subsystem emitted the message. A vehicle failure, contract exception and construction delay can therefore share the same interaction model while keeping their domain-specific details.

World News is separate. A historical/economic/company/infrastructure event can appear in UI-D40 as public/world context while the same underlying cause creates an item here only when it produces a concrete player-company information/decision state. Do not duplicate one simulation event into unrelated authoritative records.

Keep counts concise in the bottom bar. Do not turn every informational event into a flashing badge. The event centre is an inbox/history surface over authoritative simulation state, not a second incident engine.

## 2. Needs decision

This view contains active situations where automation cannot or is not permitted to choose a valid response within current player policies, budgets or authority.

Each row/card shows:

- concise problem statement;
- root cause or current best-known cause;
- affected object(s);
- operational/commercial impact;
- deadline or time remaining where meaningful;
- whether the game is currently paused because this incident qualified as critical;
- direct actions or links to the existing corrective workflow.

Example, illustrative only:

> Trip 10:20 has no suitable available vehicle.
>
> The original vehicle failed. Dispatcher found no replacement satisfying the Line requirements.
>
> Departure in 36 min · 128 reserved passengers affected.
>
> Open Trip · Review vehicles · Review cancellation/recovery

Do not provide a destructive shortcut merely because an action is common. A Cancel Trip action still uses the normal impact/permission checks.

A problem moves here when an automated response exhausts its authority, a manager explicitly requests approval, or a new fact makes the prior authorized plan invalid. Transitioning into Needs decision must preserve the incident identity and history rather than generating an unrelated duplicate.

## 3. In progress

This view contains material active incidents that still affect operation or business but are already being handled under authorized dispatcher/manager policy.

Show:

- current effect;
- selected recovery/handling action;
- relevant estimated resolution where supported;
- downstream risk;
- responsible manager/dispatcher or policy;
- direct links to affected objects.

Example:

> R12 Trip delayed +14 min.
>
> Dispatcher used 7 min of turnaround recovery. Next duty currently expected +4 min.
>
> Open Trip · Open Line · Review recovery history

Routine authorized handling does not demand acknowledgement and does not auto-pause by itself. If the situation resolves, it moves to history/information according to importance. If recovery fails, a new material escalation occurs, or a decision exceeds delegated authority, the same incident can move into Needs decision and may trigger critical auto-pause if UI-D08 criteria are met.

## 4. Information

Use Information for useful completed or non-actionable events, such as:

- vehicle delivered;
- maintenance completed;
- construction stage/project completed;
- ordinary successful contract renewal;
- licence/technology/model availability becoming relevant;
- routine operational completion worth retaining.

Show these as small, unobtrusive corner **toasts** when appropriate, then retain them in Information/history. A toast is presentation only: it does not pause time, acknowledge a related incident, change camera position or open a workflow automatically.

Group related routine events where that improves readability, for example:

> 5 vehicles completed maintenance.
>
> View vehicles

Do not emit five equivalent toasts merely because five objects changed state in the same logical batch. Preserve individual underlying object links/details when the grouped item is expanded.

Important information that creates a real upcoming obligation can remain visible until seen, but “seen” is not the same as resolved, paid, accepted or acknowledged where those are distinct domain states.

## 5. Root-cause grouping and incident hierarchy

**One root cause should normally create one parent incident.** Downstream effects are grouped beneath it instead of generating an alarm storm.

Example:

> Track closure Praha–Kolín
>
> 8 Trips affected
> 3 Shipments at risk
> 2 contractual obligations at risk
>
> Open incident

The incident detail expands the affected Trips, Shipments, Lines, contracts, vehicles, facilities and projects with exact-object links.

Use stable incident identity and explicit causal relationships. A downstream item can become separately actionable when it genuinely needs its own decision, but it retains a visible parent/root-cause link.

Do not group unrelated incidents merely because they happen at the same station or in the same hour. Conversely, do not create separate critical auto-pause events for every downstream consequence of the same unchanged root cause.

Material escalation may update severity/impact and trigger a new pause under UI-D08. Minor count changes alone should not repeatedly interrupt the player.

## 6. Critical incident presentation and pause

UI-D08 remains authoritative:

- genuinely critical incidents automatically pause by default;
- routine delays and authorized routine recovery do not;
- pause occurs at a consistent simulation event boundary;
- the player explicitly resumes through time controls;
- closing, acknowledging or resolving the event view never automatically resumes;
- the same unchanged incident does not repeatedly pause after deliberate resume;
- a genuinely new critical incident or material escalation may pause again;
- incident auto-pause/acknowledgement state persists across save/load.

When a critical event occurs, show a prominent but compact notice explaining **why the game paused**, the current impact and the route to its event detail. Do not cover the whole screen with a modal that prevents map inspection or planning.

The notice may remain until the player has seen it, but visibility/acknowledgement does not equal operational resolution.

## 7. Historical record

History is a chronological, filterable record of meaningful events and resolved incidents. It preserves the event-time facts.

An old message such as:

> Month 3, Day 8, 10:14 — Vehicle 014 failed during Trip 08:20.

remains historically true even if the vehicle is now repaired.

When a historical record links to Vehicle 014, clicking it opens the vehicle's **current live detail** unless the user explicitly opens the event snapshot/history subsection. Make the distinction between:

- historical event snapshot;
- current object state.

Do not rewrite old event text to match current conditions. If an object no longer exists or is no longer controlled, follow UI-D09 retained-history/read-only rules.

History filters may include severity, domain, object, unresolved/resolved state and time period. Filtering does not mutate or delete simulation history.

## 8. Follow / Sledovat objects

Allow the player to explicitly **Follow / Sledovat** an inspectable object such as a Line, vehicle, construction project, contract, Shipment or relevant facility.

Following is a UI preference. It does not:

- change simulation priorities;
- increase reliability;
- reserve resources;
- affect dispatcher/manager authority;
- alter object ownership;
- create extra simulation events.

It changes notification presentation only: the player may receive lower-severity updates for followed objects that would otherwise remain only in history or object detail.

Examples:

- monitor a newly launched Line during its first operating days;
- follow delivery of an important locomotive;
- follow a major construction project;
- follow a high-value customer contract.

Make Follow state visible in the object's detail and event filters. Unfollow returns to normal notification policy without deleting prior history.

Follow must be bounded against spam. Repeated low-level updates from the same object should still aggregate by event/root cause. A player following 100 vehicles should not force 100 separate toasts for one depot-wide event.

Persist Follow preferences in the save/UI preference state as appropriate without turning them into gameplay authority.

## 9. Event states and acknowledgement

Keep these concepts separate where applicable:

- **new/unseen** — player has not viewed the event;
- **seen/acknowledged** — player has viewed or explicitly acknowledged presentation;
- **in progress** — operational/business issue remains active and is being handled;
- **needs decision** — active issue awaits player authority;
- **resolved** — underlying incident no longer requires active handling;
- **historical** — retained record after resolution/completion.

Acknowledging a notice does not:

- repair a vehicle;
- clear a route;
- accept a contract amendment;
- cancel a Trip;
- pay an invoice;
- resolve a Shipment;
- resume time.

An incident can be seen but unresolved. It can also be resolved before the player opens it if authorized automation handled it.

## 10. Toast and attention policy

Use attention proportional to required action:

| Event type | Presentation |
|---|---|
| Critical + needs decision | Auto-pause under UI-D08 + prominent compact notice + Needs decision |
| Important decision, non-critical | Persistent indicator/Needs decision; no automatic pause unless another rule qualifies it |
| Active handled problem | In progress; optional restrained toast on material state change |
| Routine successful/informational event | Small transient toast or grouped summary, retained in Information/history |
| Followed-object minor event | Optional lower-severity toast/entry, still aggregated to avoid spam |

No category uses colour alone. Provide text/icon semantics and keyboard/focus access.

A toast disappearing does not remove the event from history. Hovering/opening a toast is not acknowledgement unless explicitly designed and labelled as such; normal object-link clicks should not accidentally mark unrelated incidents resolved.

## 11. Filters, search and counters

Provide simple filters for:

- status/view;
- severity/attention level;
- domain (operations, fleet, construction, commercial, company/finance, etc.);
- followed objects;
- selected Line/contract/project or other object where context exists;
- time range in History.

Search can find event text/object names but must resolve object links through stable identities, not parsed localized strings.

Bottom-bar counts should prioritize **unseen decisions and critical/unresolved attention**, not total lifetime history. Avoid alarming “999+” badges merely because the campaign has years of historical events.

## 12. Save/load and performance

Persist stable incident IDs, root-cause relationships, handling state, decision requirement, acknowledgement/seen state, escalation state required by UI-D08, and historical snapshots needed for explanation.

Save/load must not:

- regenerate the same event as new;
- replay old toasts as fresh;
- duplicate root-cause incidents;
- re-trigger auto-pause for an unchanged already-presented critical incident;
- lose a pending player decision;
- rewrite historical text from current live state.

Use event-driven updates. Do not scan every Trip, vehicle and contract every frame merely to populate the event centre. Domain systems emit/update meaningful incident/event records with structured reasons and affected object IDs.

## 13. Acceptance evidence to collect

| ID | Required scenario |
|---|---|
| EVTUI-A01 | Trigger a critical incident at 0.5x, 1x and 16x. Verify one auto-pause, compact cause/impact notice, usable map/windows and explicit resume only. |
| EVTUI-A02 | Trigger one closure affecting many Trips, Shipments and contracts. Verify one parent incident with expandable impacts rather than one alarm per affected object. |
| EVTUI-A03 | Let dispatcher handle a routine delay. It appears in In progress/history without auto-pause; if recovery exceeds authority, the same incident moves to Needs decision. |
| EVTUI-A04 | Generate several routine completions together. Verify grouped toast/Information entry and exact underlying object links without duplicated gameplay events. |
| EVTUI-A05 | Open an old event after the linked vehicle/Line has changed state. Historical snapshot stays unchanged while the object link opens current live detail. |
| EVTUI-A06 | Follow a new Line and a vehicle, receive additional low-severity updates, then unfollow. Simulation behaviour remains identical; grouped spam controls still apply. |
| EVTUI-A07 | Acknowledge/close/resolve notices in different orders. No action automatically resumes a critical pause or performs the underlying gameplay command. |
| EVTUI-A08 | Save/load with unseen, in-progress, needs-decision, resolved and followed-object events. IDs, state, history and pause-deduplication persist without replaying old notifications as new. |

## 14. Decision record

| ID | Decision | Status |
|---|---|---|
| UI-D24 | One event centre organized by Needs decision / In progress / Information / History, root-cause incident grouping, restrained grouped toasts, historical snapshots and optional Follow notifications for chosen objects; UI-D08 remains authoritative for critical auto-pause | CONFIRMED on 2026-09-30 |

UI-D24 resolves the notification-layout proposal in UI_UX_DESIGN Section 7.1 while preserving its problem-explanation model. UI-D40 owns World News/history and ordinary news never auto-pauses merely because it is news. UI-D36 settles precise pause-menu transitions. Application-focus behaviour and detailed per-event auto-pause override settings remain open under UI-D08.
