# Tranzit — TODO

> **Purpose:** single living backlog for work that is still open, undecided, blocked or intentionally queued.
>
> This file answers **what remains to do**. It is not implementation evidence and it is not a second game-design specification.
>
> - Gameplay/UI rules belong in their owning design documents.
> - Actual implementation/test evidence belongs in [IMPLEMENTATION_STATUS.md](IMPLEMENTATION_STATUS.md).
> - Release proof belongs in [V1_ACCEPTANCE_TESTS.md](V1_ACCEPTANCE_TESTS.md) and recorded evidence.
> - Completed design decisions remain documented in their owning files even after they leave this backlog.

Last reviewed: 2026-09-30 after UI-D36 and the repository-wide UI gap audit.

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

### Finish the remaining major UI/UX gaps

- [ ] **[DESIGN] External Company & Competitor Detail** — complete the full external-company object beyond UI-D27 bilateral agreements: adaptive roles, public/known operation/network, products/services, relationship/history, ownership and competitor information boundaries. Proposed next decision: **UI-D37**.
- [ ] **[DESIGN] Technology & Research UI** — research capacity, historically available technology, company adoption/install requirements, active/completed research and concrete capability effects. Proposed **UI-D38**.
- [ ] **[DESIGN] Ownership, Acquisitions & Infrastructure Market UI** — shares/control, acquisitions, subsidiaries/integration, asset/infrastructure purchases and sales, inherited contracts/liabilities. Proposed **UI-D39**.
- [ ] **[DESIGN] News & Historical Events UI** — world news, historical/macroeconomic developments, source/impact explanation and navigation into affected regions/industries/company decisions. Proposed **UI-D40**.
- [ ] **[DESIGN] Final navigation taxonomy + global search** — finalize detailed contents under Build / Operations / Business / Assets / Company / World only after the remaining workflows above are specified; include searchable known objects without bypassing information boundaries.

## Open decisions

- [ ] **[DESIGN] Application-focus loss/return** — decide what happens to simulation/pause state on Alt-Tab, focus loss and focus return. This is the remaining focus-related part of UI-D08.
- [ ] **[DESIGN] Detailed event auto-pause/notification overrides** — decide how much per-event customization Settings should expose beyond the confirmed default that critical incidents auto-pause.
- [ ] **[DESIGN] External-company full layout** — UI-D27 confirms all bilateral agreements, but the complete external-company/competitor detail is still open until UI-D37 is accepted.
- [ ] **[DESIGN] Player-facing vocabulary/navigation glossary** — final Czech/English labels for domain objects remain candidates in UI_UX_DESIGN Section 4.2; resolve with final navigation instead of independently.

## Next

### After the remaining UI decisions

- [ ] **[DOC] Run a final UI consistency audit** — remove stale “proposed/open” wording superseded by UI-D01–UI-D40, verify cross-links, decision table and acceptance scenarios.
- [ ] **[DOC] Reconcile final navigation with README, UI_UX_DESIGN and V1_IMPLEMENTATION_BRIEF**.
- [ ] **[DOC] Review UI-D27 wording after UI-D37** so it no longer says the broader external-company layout is open once that detail is confirmed.
- [ ] **[DOC] Review UI_EVENTS/UI_SYSTEM_MENU after the focus/override decisions** and close the remaining UI-D08 status if fully resolved.

### Implementation handoff

- [ ] **[IMPL] Reinspect the current repository/toolchain and begin M0** according to [OPENCODE_START.md](OPENCODE_START.md) and [V1_IMPLEMENTATION_BRIEF.md](V1_IMPLEMENTATION_BRIEF.md).
- [ ] **[IMPL] Maintain [IMPLEMENTATION_STATUS.md](IMPLEMENTATION_STATUS.md)** as code/tests/evidence appear; do not infer implementation from the completed design backlog.
- [ ] **[TEST] Execute acceptance/build evidence progressively** rather than waiting until the end; formal release gates remain in [V1_ACCEPTANCE_TESTS.md](V1_ACCEPTANCE_TESTS.md).

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

The following design directions are already accepted and should **not** be reopened merely because they no longer appear under Now:

- [x] UI-D01–UI-D15 — global visual/window/navigation/pause/link/Line/station/minimalism foundations.
- [x] UI-D16–UI-D24 — depots, commercial, construction, finance, company, map, fleet, shipments, events.
- [x] UI-D25–UI-D33 — Trip, capacity/access, external-company agreements, cities/regions, tariffs, maintenance, duties, procurement, licences/market entry.
- [x] UI-D34 — neutral compact money icon for the single money accounting unit.
- [x] UI-D35 — New Game and opening-only company-founding tutorial.
- [x] UI-D36 — main menu, campaign saves, atomic save safety, pause-menu lifecycle, Esc priority and settings.
- [x] Documentation checks currently cover structural validation and validator tests; they are **not** gameplay implementation evidence.
