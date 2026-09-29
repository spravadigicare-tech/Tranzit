# Tranzit

A long-form transport and business simulation built in Unity.

The player starts as a small regional carrier and can grow into a multinational transport group while cities, industries, infrastructure, technology and political boundaries evolve around them.

## Base game and planned DLC

The base game begins around **1900**, with selectable new-game starts in **1900, 1925, 1950 and 1975**. The world is initialized for the selected year, while the player still starts with a small company.

The earlier playable period, intended to begin around **1820**, is reserved for the first planned DLC, **Early Ages**. Historic buildings, steam operations and suitable older vehicles can still be part of the base game where appropriate to its dates. The DLC release schedule is not specified.

## Shared time model

- A week has 7 days; a month has **14 days**; a year has **12 months / 168 days**.
- At **1×**, **one real second equals one game minute**.
- Running speeds: **0.5×, 1×, 2×, 4×, 8× and 16×**.
- One common clock governs vehicles, operations, economics, construction, contracts, seasons and historical progression.

At uninterrupted 16×, reaching the reference year 2020 takes approximately **504 h from 1900**, **399 h from 1925**, **294 h from 1950**, or **189 h from 1975**. These are mathematical durations assuming the selected simulation rate is sustained, not measured performance or promised completion times. The previous short campaign-duration target is retired. **2020 is not a mandatory ending.**

## Project documents

- [Living Game Design](docs/GAME_DESIGN.md) — core gameplay source of truth; Section 3 defines start years, calendar, speed controls and date-appropriate initialization.
- [Contract cancellation](docs/CONTRACT_CANCELLATION.md) — current detailed rules for capped early-exit fees, returned slots and non-renewal.
- [Agent instructions](AGENTS.md) — mandatory rules for AI/OpenCode development agents, including which design documents to review.

The design is intentionally maintained as a living specification: obsolete decisions should be rewritten or removed rather than preserved as conflicting alternatives. Focused specifications elaborate the linked core design and must be reviewed together with the affected systems.

These documents specify the intended game; recording a rule does not mean it has already been implemented or benchmarked in Unity.
