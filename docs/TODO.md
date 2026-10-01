# Tranzit — TODO

> **Purpose:** single living backlog for work that is still open, undecided, blocked or intentionally queued.
>
> This file answers **what remains to do**. It is not implementation evidence and it is not a second game-design specification.
>
> - Gameplay/UI rules belong in their owning design documents.
> - Actual implementation/test evidence belongs in [IMPLEMENTATION_STATUS.md](IMPLEMENTATION_STATUS.md).
> - Release proof belongs in [V1_ACCEPTANCE_TESTS.md](V1_ACCEPTANCE_TESTS.md) and recorded evidence.
> - Completed design decisions remain documented in their owning files even after they leave this backlog.

Last reviewed: 2026-10-01. At the player's request, further connection-agreement design is handed off to a separate conversation. Connection agreements remain in V1; only discussion in this thread is paused. Preserve accepted passenger-cooperation rules and keep unresolved details open until the separate discussion is reconciled into the owning specifications.

## How to use this backlog

Use the following prefixes where useful:

- **[DESIGN]** unresolved product/UX decision or missing focused specification;
- **[DOC]** documentation reconciliation/audit work;
- **[IMPL]** implementation work that should happen next;
- **[TEST]** validation/evidence still to run;
- **[CONTENT]** authored data/assets/balancing work;
- **[BLOCKED]** cannot currently proceed because a concrete dependency is unavailable.

Rules:

1. Before substantial work, read this file together with the relevant source-of-truth documents and [IMPLEMENTATION_STATUS.md](IMPLEMENTATION_STATUS.md).
2. Add a task when a real remaining action, unresolved decision, blocker or follow-up is discovered.
3. Do **not** use TODO text to override an accepted mechanic. Update the owning design/specification first, then reflect the resulting remaining work here.
4. When a design task is accepted, update every affected owning/summarizing/test document in the same change where practical, then mark/remove the TODO item.
5. When implementation work completes, **do not mark it done merely because code exists**. Update [IMPLEMENTATION_STATUS.md](IMPLEMENTATION_STATUS.md) with implementation paths and actual test/build evidence; then close the TODO item only at the level actually completed.
6. A task that is merely postponed belongs under **Deferred**, with the reason/scope owner. A task that cannot proceed belongs under **Blocked**, with the concrete blocker.
7. Keep **Now** short and actionable. Move lower-priority work to **Next** rather than letting Now become a full project dump.
8. Avoid duplicating the M0–M8 milestone tables or SYS-01–SYS-16 evidence ledger here. Link to them instead.
9. Keep **Done recently** short. It is a convenience recap, not a permanent changelog; accepted decisions remain in their canonical documents and Git history.
10. After editing documentation, run the repository documentation checks required by AGENTS.md.

## Now

The market/economy/public-tender, V1 multi-operator passenger-ticket and final UI/navigation documentation passes are complete and reconciled. Keep connection-agreement design in its separate thread. The next executable work in this repository is the implementation handoff/M0 work below; do not treat the still-blank connection-agreement specification as decided.

## Open decisions

- [ ] **[DESIGN] Connection agreements — redesign from scratch in separate thread** — still required for V1. The dedicated [CONNECTION_AGREEMENTS.md](CONNECTION_AGREEMENTS.md) is intentionally blank; do not carry forward prior draft mechanics unless explicitly re-approved there.

## Next

### Vehicle content authoring

- [ ] **[CONTENT] Turn [VEHICLE_CATALOGUE.md](VEHICLE_CATALOGUE.md) into versioned machine-readable vehicle/factory/import/dealer data** — validate the exact representative configuration for every prototype, author explicit `money` prices, production inputs/lead times, consumption, maintenance/support families and regional offer weights, then create functional prefabs/LODs/sounds. A catalogue row alone is not implemented content.
- [ ] **[CONTENT] Author physical manufacturer and import supply for the vehicle roster** — active-map factories need dated capabilities/backlogs and real inputs; off-map manufacturers need finite macro capacity plus border/import delivery nodes. Dealer and used stock must reference physical assets rather than spawn vehicles on demand.

### Implementation handoff

- [ ] **[IMPL] Reinspect the current repository/toolchain and begin M0** according to [OPENCODE_START.md](OPENCODE_START.md) and [V1_IMPLEMENTATION_BRIEF.md](V1_IMPLEMENTATION_BRIEF.md).
- [ ] **[IMPL] Maintain [IMPLEMENTATION_STATUS.md](IMPLEMENTATION_STATUS.md)** as code/tests/evidence appear; do not infer implementation from the completed design backlog.
- [ ] **[TEST] Execute acceptance/build evidence progressively** rather than waiting until the end; formal release gates remain in [V1_ACCEPTANCE_TESTS.md](V1_ACCEPTANCE_TESTS.md). UI-D37's EXTCO-A01–EXTCO-A16 are evidence requirements, not executed gameplay tests.

## Blocked

No project-wide blocker is currently recorded here.

When adding one, state exactly:

- blocked task;
- missing dependency/tool/data/decision;
- what can still proceed;
- next action that would unblock it.

Do not use “blocked” for work that is merely lower priority.

## Deferred

These are intentional non-blockers for the current V1/UI direction:

- [ ] **Embedded station track/platform/stand schematic** — explicitly deferred under UI-D14; main-map physical geometry remains real.
- [ ] **Deep nested glossary/tooltips** — deferred; first-layer hover/focus explanations are required under UI-D15.
- [ ] **Mandatory expert railway timetable editor** — outside current required normal play; high-level Capacity Order/timetable planning is canonical.
- [ ] **Exact visual tokens/pixel dimensions** — resolve during visual implementation/testing; not a product-decision blocker unless readability/interaction reveals a real problem.
- [ ] **Later start presets 1925 / 1950 / 1975** — wider base-game scope, not first-playable V1.
- [ ] **Water, tram, trolleybus and metro operation** — wider base-game scope, not first-playable V1.
- [ ] **Early Ages pre-1900 playable start** — planned DLC scope.

## Done recently

These are completed design/documentation tasks, not implemented game features. Remaining parts of partially confirmed decisions stay open above and in the owning register.

- [x] Accepted foundations within UI-D01–UI-D15 — global visual/window/navigation/pause/link/Line/station/minimalism directions; UI-D05 terminology and UI-D08 exceptional pause behaviour are fully resolved.
- [x] UI-D16–UI-D24 — depots, commercial, construction, finance, company, map, fleet, shipments, events.
- [x] UI-D25–UI-D33 — Trip, capacity/access, external-company agreements, cities/regions, tariffs, maintenance, duties, procurement, licences/market entry.
- [x] UI-D34 — neutral compact money icon for the single money accounting unit.
- [x] UI-D35 — New Game and opening-only company-founding tutorial.
- [x] UI-D36 — main menu, campaign saves, atomic save safety, pause-menu lifecycle, Esc priority and settings.
- [x] UI-D37 — adaptive external-company/competitor detail around the existing bilateral-agreement model.
- [x] UI-D38 — simple technology/research UI with concrete unlocks and company-level adoption only where genuinely needed.
- [x] UI-D39 — ownership/acquisitions/infrastructure market; controlled subsidiaries remain AI-managed, with a small owner-action set and separate company economies.
- [x] UI-D40 — simple World News/history feed with significant world changes, known player impact and strict separation from UI-D24 incidents.
- [x] UI-D41 — final HUD/navigation and global search, with company/finance top-left, Search/Layers top-right and grouped bottom navigation.
- [x] **[DESIGN/DOC] V1 multi-operator passenger ticket cooperation (2026-10-01)** — retained asymmetric Line-scoped partner-capacity sales and two directional money/km rates with public-fare-versus-settlement margin including negative margins. V1 is explicitly limited to a two-operator single-journey through ticket containing a seller leg and partner leg; no pure/recursive resale or shared multi-company weekly/monthly pass. Sold tickets capture fare/agreement versions, real reservation rules still apply, and capacity resale alone creates no timetable coordination or protected connection.
- [x] **[DOC] Final UI/navigation consistency audit (2026-10-01)** — reconciled README, UI_UX_DESIGN, UI_NAVIGATION-dependent focused specs and V1_IMPLEMENTATION_BRIEF with confirmed UI-D36–UI-D41. Removed stale pending claims, fixed Finance/cash to the upper-left HUD, Layers to the upper-right HUD, retained Build + Operations/Business/Assets | Company/World + Events/time in the bottom bar, and made UI_NAVIGATION authoritative so workflow tables cannot create a second navigation taxonomy. Connection-agreement design remains intentionally open in its separate specification.
- [x] **[DESIGN/DOC] Market/economy refinement (2026-10-01)** — confirmed stable city/locality commodity markets with evolving internal economic centres, final-consumer sinks, historical commodity evolution, reference-versus-negotiated prices, active producer/buyer transport proposals, contract-first freight with transparently flow-dependent bounded open carriage, transparent concrete-plan public-service tenders, and all three public infrastructure/concession models in V1; subsequent price-response, centre/logistics and production/recipe balancing passes below complete the associated initial V1 defaults.
- [x] **[DESIGN/CONTENT] Economic-centre and firm-logistics balancing defaults (2026-10-01)** — set monthly centre-development evaluation, 800 m target/1,000 m split review, explicit resident/job/anchor formation gates, persistence/decline rules, and no hard centre-count cap. Firm logistics now uses explicit local make-or-buy defaults; exceptional captive intercity road capacity requires sustained large/specialist lane utilization, targets 25–35% of stable base load and is hard-capped at 40%, while non-transport captive mainline rail haulage remains 0%. Core design, content manifest, implementation brief and acceptance scenarios are reconciled.
- [x] **[DESIGN/CONTENT] Commodity reference-price response curve (2026-10-01)** — defined an explainable stock-coverage + 7-day flow + alternative-access target model, explicit piecewise contributions, 50% target smoothing, 0.5% deadband, ordinary 0.50×–2.00× target range with ±5% daily movement, and exceptional 0.35×–3.00× target range with ±15% daily movement. Implementation brief and acceptance coverage are reconciled.
- [x] **[DESIGN/CONTENT] Initial 1900 production/recipe balancing (2026-10-01)** — added versioned small/medium/large facility output bands, explicit baseline recipe coefficients, seeded inventory coverage, ordinary 65–80% starting utilization, 90–110% full-world ordinary recurrent supply/demand guidance and starting-area freight-flow fixtures. Reference chains were cross-checked so same-scale upstream capacity can support downstream operation, utility conversions use explicit MWh-equivalent coefficients, and construction demand scales from real project quantity plus project-family material mixes rather than a flat package. Acceptance coverage verifies real inventories/recipes and rejects anonymous cargo generation.
- [x] **[DESIGN/CONTENT] Canonical commodity chains (2026-10-01)** — finalized a grouped multi-input commodity network: 1900 forestry/furniture/paper, food, textile, construction/glass, heavy-industry, energy and maintenance chains plus staged chemicals/plastics/gas/fertilizer/medical/electronics expansion. Firms can require several inputs in parallel; electronics includes chips/components rather than exposing a separate chips cargo.
- [x] **[DESIGN/DOC] UI-D37 — External Company & Competitor Detail** — expanded [UI_EXTERNAL_COMPANIES.md](UI_EXTERNAL_COMPANIES.md) around preserved UI-D27 agreements, registered the decision/acceptance scenarios in [UI_UX_DESIGN.md](UI_UX_DESIGN.md), and reconciled README and obsolete company-layout-open wording. Six adaptive cards, source/time/permission limits, canonical offer routing and retained company history are confirmed.
- [x] Documentation checks cover structural validation and validator tests; they are **not** gameplay implementation evidence.
