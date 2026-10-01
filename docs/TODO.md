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

Continue the current market/economy/public-tender design pass and reconcile each accepted decision immediately into its owning documents. Do not reopen connection-agreement design in this conversation; its separate-thread handoff remains under Open decisions rather than Deferred or Done.

## Open decisions

- [ ] **[DESIGN/CONTENT] Initial production/recipe quantities and capacities** — the market price-response curve, economic-centre formation and firm-owned-logistics defaults are now defined in V1_CONTENT_MANIFEST 7.1–7.3. Still set the initial facility production rates, recipe input/output quantities, seeded inventories and representative capacity bands for the canonical commodity chains so the authored 1900 economy starts viable without arbitrary cargo generation or bootstrap deadlocks. Keep these as versioned balancing data with explicit units and measured playtest revision, not hidden difficulty modifiers.
- [ ] **[DESIGN] Connection agreements — redesign from scratch in separate thread** — still required for V1. The dedicated [CONNECTION_AGREEMENTS.md](CONNECTION_AGREEMENTS.md) is intentionally blank; do not carry forward prior draft mechanics unless explicitly re-approved there.
- [ ] **[DESIGN] Remaining multi-operator passenger ticket cooperation details for V1** — retain the already agreed capacity-sales clause, two directional partner rates and public-tariff-versus-partner-rate margin model, including negative margins. Complete remaining ticket cooperation and product-scope details without reopening those choices. Shared multi-company weekly/monthly products and tariff governance remain a separate unresolved scope question. Connection coordination and partner-capacity sales remain independent; pausing the connection discussion does not remove or finalize the capacity-sales workflow.

## Next

### After the remaining UI decisions

- [ ] **[DOC] Run a final UI consistency audit** — remove stale “proposed/open” wording only where a decision has actually been confirmed, verify cross-links, decision table and acceptance scenarios. UI-D41 navigation/search and UI-D08 focus/notification behaviour are already confirmed. Keep connection-agreement details open until the separate-thread decisions are reconciled; do not report all V1 design decisions as closed in the meantime.
- [ ] **[DOC] Reconcile final navigation with README, UI_UX_DESIGN and V1_IMPLEMENTATION_BRIEF**.

### Implementation handoff

- [ ] **[IMPL] Reinspect the current repository/toolchain and begin M0** according to [OPENCODE_START.md](OPENCODE_START.md) and [V1_IMPLEMENTATION_BRIEF.md](V1_IMPLEMENTATION_BRIEF.md).
- [ ] **[IMPL] Maintain [IMPLEMENTATION_STATUS.md](IMPLEMENTATION_STATUS.md)** as code/tests/evidence appear; do not infer implementation from the completed design backlog.
- [ ] **[TEST] Execute acceptance/build evidence progressively** rather than waiting until the end; formal release gates remain in [V1_ACCEPTANCE_TESTS.md](V1_ACCEPTANCE_TESTS.md). UI-D37's EXTCO-A01–EXTCO-A14 are evidence requirements, not executed gameplay tests.

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
- [x] **[DESIGN/DOC] Market/economy refinement (2026-10-01)** — confirmed stable city/locality commodity markets with evolving internal economic centres, final-consumer sinks, historical commodity evolution, reference-versus-negotiated prices, active producer/buyer transport proposals, contract-first freight with transparently flow-dependent bounded open carriage, transparent concrete-plan public-service tenders, and all three public infrastructure/concession models in V1; owning design/UI/test documents updated. Remaining market/commodity balancing work stays open above.
- [x] **[DESIGN/CONTENT] Economic-centre and firm-logistics balancing defaults (2026-10-01)** — set monthly centre-development evaluation, 800 m target/1,000 m split review, explicit resident/job/anchor formation gates, persistence/decline rules, and no hard centre-count cap. Firm logistics now uses explicit local make-or-buy defaults; exceptional captive intercity road capacity requires sustained large/specialist lane utilization, targets 25–35% of stable base load and is hard-capped at 40%, while non-transport captive mainline rail haulage remains 0%. Core design, content manifest, implementation brief and acceptance scenarios are reconciled.
- [x] **[DESIGN/CONTENT] Commodity reference-price response curve (2026-10-01)** — defined an explainable stock-coverage + 7-day flow + alternative-access target model, explicit piecewise contributions, 50% target smoothing, 0.5% deadband, ordinary 0.50×–2.00× target range with ±5% daily movement, and exceptional 0.35×–3.00× target range with ±15% daily movement. Implementation brief and acceptance coverage are reconciled.
- [x] **[DESIGN/CONTENT] Canonical commodity chains (2026-10-01)** — finalized a grouped multi-input commodity network: 1900 forestry/furniture/paper, food, textile, construction/glass, heavy-industry, energy and maintenance chains plus staged chemicals/plastics/gas/fertilizer/medical/electronics expansion. Firms can require several inputs in parallel; electronics includes chips/components rather than exposing a separate chips cargo.
- [x] **[DESIGN/DOC] UI-D37 — External Company & Competitor Detail** — expanded [UI_EXTERNAL_COMPANIES.md](UI_EXTERNAL_COMPANIES.md) around preserved UI-D27 agreements, registered the decision/acceptance scenarios in [UI_UX_DESIGN.md](UI_UX_DESIGN.md), and reconciled README and obsolete company-layout-open wording. Six adaptive cards, source/time/permission limits, canonical offer routing and retained company history are confirmed.
- [x] Documentation checks cover structural validation and validator tests; they are **not** gameplay implementation evidence.
