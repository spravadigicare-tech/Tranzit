# OpenCode — Start implementing Tranzit V1

This file is an execution prompt. The detailed source of truth is in the linked repository documents. Do not treat this prompt as a substitute for their rules.

## Task

Implement the first genuinely playable Tranzit V1 in this repository. Deliver an offline Windows game, not only documentation, a scaffold, a simulation library, a menu or a train-movement demo.

Read `AGENTS.md`, `docs/V1_SCOPE.md`, the complete `docs/GAME_DESIGN.md`, `docs/CONTRACT_CANCELLATION.md`, `docs/V1_IMPLEMENTATION_BRIEF.md`, `docs/V1_CONTENT_MANIFEST.md` and `docs/V1_ACCEPTANCE_TESTS.md`. Inspect the current files, branch and toolchain before making changes. Do not assume the repo still has no code just because that was true at handoff preparation.

The scope is already decided:

- Only the 1900 new-game preset in V1, but continued calendar/technology progression.
- Rail passengers/freight, road freight, intercity and local buses. No water, tram, trolleybus, metro or aircraft implementation for this release.
- Complete Czech geographic coverage plus adjoining German, Polish, Austrian and Slovak territory, real locations/relief and a historically plausible offline authored world.
- Existing infrastructure and real AI competitors; the player starts small with a loan, not a free branch/fleet.
- One unit named `money`; Czech and English UI; coherent stylized 3D model-world graphics.
- One shared simulation clock: 1 real second = 1 game minute at 1x, 14 days/month, 168 days/year, speeds 0.5x through 16x and pause. Geographic length and actual performance determine travel time.
- Physical assets/cargo never teleport. Shipments split across Trips while quantities, capacity, custody and obligations remain conserved. Protected commitments cannot be silently displaced by a profitability/priority score.
- No end-year removal of introduced vehicle models. Real offers/support capacity can change economically; own compatible support can keep old equipment useful.
- Every applicable main mechanic, full save/load and meaningful failures must work through UI. Simple coherent original assets are acceptable; labelled debug primitives are not final graphics.

## Execute

Follow M0–M8 in the implementation brief. First establish the real Unity project/build/test foundation and then implement a visible, playable small-road loop. Continue toward rail, multi-leg logistics, passenger operation, business/AI, lifecycle/progression, full content and release verification. A vertical slice is an internal milestone, not finished V1.

Make routine technical and initial balancing decisions yourself, document them and keep values configurable. Do not reopen approved product questions. Verify current package/API compatibility and pin the chosen versions. Preserve unrelated changes and avoid destructive Git operations.

Use shared validation/ledgers for player, AI and planners. Keep simulation authority separate from rendering. Add tests, localization and persistence with every subsystem; do not defer all of them until the end. Develop recognizable graphics in parallel with gameplay.

Maintain `docs/IMPLEMENTATION_STATUS.md` as a requirement → implementation → test → evidence ledger. Run compilation/tests/builds actually available to you and record exact commands and results. Use bounded process timeouts, logs and explicit completion conditions; never wait indefinitely on a running Editor/watch/game process.

A missing Unity installation, licence, credential or data source is an explicit blocker, not a fabricated success or permission to change the game. Work on nonblocked tasks and report the exact remaining requirement. On interruption, persist completed work, real failing/passing tests and the next executable task so the next session resumes rather than replans.

## Definition of done

All release gates in `docs/V1_ACCEPTANCE_TESTS.md` have real evidence. The player can start, build, acquire, staff, contract, transport, earn/lose money, handle disruption, compete, delegate, progress and save/reload in the standalone offline game. The full approved world and usable content are bundled. Main screens are functional in Czech and English. Supply the Windows build, reproducible build/run instructions, actual test/performance results and known issues.

Do not claim V1 is complete merely because the code was written or compiles. Do not claim a tested build if no build/test was run. Start implementation rather than responding with another broad plan.
