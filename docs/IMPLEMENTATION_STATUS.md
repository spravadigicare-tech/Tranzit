# Tranzit — Implementation status

Last initialized: 2026-09-30, during preparation of the OpenCode handoff.

## Current evidence

Inspected baseline: main commit `0ff59b98d8b9bdcbe3fec32299086bdcdb306c44`. It contained only AGENTS.md, README.md, GAME_DESIGN.md and CONTRACT_CANCELLATION.md. The handoff adds specifications and this ledger, not a Unity game.

- Design/implementation handoff: prepared.
- Unity project and game implementation: not present in the inspected baseline; not created by this handoff.
- Windows build: not produced.
- Game compilation, automated tests, player walkthroughs and benchmarks: NOT RUN.
- Historical geodata and game assets: not supplied by this handoff.
- The user's local Unity/toolchain installation has not been inspected by this handoff. Do not infer that it is installed or missing.

Reinspect the current working tree before using these statements as current status. Replace them with actual implementation evidence as work proceeds.

## Milestones

| Milestone | Initial state | Evidence |
|---|---|---|
| M0 Reproducible foundation | NOT IMPLEMENTED | No Unity project at inspected baseline |
| M1 Visible world and road business | NOT IMPLEMENTED | None |
| M2 Rail and construction | NOT IMPLEMENTED | None |
| M3 Shared network logistics | NOT IMPLEMENTED | None |
| M4 Passenger operation | NOT IMPLEMENTED | None |
| M5 Business and autonomous competitors | NOT IMPLEMENTED | None |
| M6 Lifecycle/progression/disruption | NOT IMPLEMENTED | None |
| M7 Full world/content/presentation | NOT IMPLEMENTED | None |
| M8 Release verification | NOT RUN | No game build |

## Requirement coverage

Definitions: see V1_IMPLEMENTATION_BRIEF Section 6. Use actual code/test paths and evidence when updating.

| Requirement | Initial implementation status | Test evidence | Remaining work |
|---|---|---|---|
| SYS-01 Clock/world authority | NOT IMPLEMENTED | NOT RUN | Implement and test |
| SYS-02 Historical world/development | NOT IMPLEMENTED | NOT RUN | Author data, implement and test |
| SYS-03 Company/staff/management | NOT IMPLEMENTED | NOT RUN | Implement and test |
| SYS-04 Firms/business/contracts | NOT IMPLEMENTED | NOT RUN | Implement and test |
| SYS-05 Split/multi-leg logistics | NOT IMPLEMENTED | NOT RUN | Implement and test |
| SYS-06 Transport/access/capacity | NOT IMPLEMENTED | NOT RUN | Implement and test |
| SYS-07 Physical fleet/lifecycle | NOT IMPLEMENTED | NOT RUN | Implement and test |
| SYS-08 Construction/land/market | NOT IMPLEMENTED | NOT RUN | Implement and test |
| SYS-09 Passenger markets/services | NOT IMPLEMENTED | NOT RUN | Implement and test |
| SYS-10 Lines/Patterns/Trips/duties | NOT IMPLEMENTED | NOT RUN | Implement and test |
| SYS-11 Technology/support | NOT IMPLEMENTED | NOT RUN | Author data, implement and test |
| SYS-12 Competitors/cooperation | NOT IMPLEMENTED | NOT RUN | Implement and test |
| SYS-13 Money/finance/distress | NOT IMPLEMENTED | NOT RUN | Implement and test |
| SYS-14 Incidents/recovery | NOT IMPLEMENTED | NOT RUN | Implement and test |
| SYS-15 UI/art/localization | NOT IMPLEMENTED | NOT RUN | Produce, integrate and verify |
| SYS-16 Save/build/validation | NOT IMPLEMENTED | NOT RUN | Implement and run verification |

## Next executable task

Follow docs/OPENCODE_START.md. Inspect the current repo and local Unity/toolchain, choose/pin the compatible editor/packages, create the real project/build/test foundation and begin M0. Do not spend the first implementation session replacing the already prepared high-level plan.

## Ongoing entry template

```
Date/commit:
Milestone and requirement IDs:
Implemented paths:
Test command/build/seed:
Observed result and evidence:
Failures/blockers:
Known limitations:
Next executable task:
```

Only change a test to PASS after executing it. Keep release gates unpassed until the corresponding evidence exists. A partial internal milestone is not the completed playable V1.
