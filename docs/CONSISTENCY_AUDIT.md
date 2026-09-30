# Tranzit — Repository consistency audit

Date: 2026-09-30. Reviewed baseline: `a2b45f570bd91730f8c76d2f6a74058e28853c60`.

## 1. Coverage and limits

The complete baseline consisted of ten Markdown files: AGENTS, README, GAME_DESIGN, CONTRACT_CANCELLATION, V1_SCOPE, V1_IMPLEMENTATION_BRIEF, V1_CONTENT_MANIFEST, V1_ACCEPTANCE_TESTS, IMPLEMENTATION_STATUS and OPENCODE_START. All were reviewed, including all 43 numbered top-level core-design sections. The core file's Git blob was verified as `a433371d4b7721edba3a258af3f5e6a64d496a74` before editing.

There was no Unity project, game source, asset library or executable game test suite in that baseline. This is a specification/cross-system review and a documentation-tooling change, not a runtime bug-fix claim or proof that V1 works. Natural-language review and structural checks cannot prove the absence of every future implementation conflict.

## 2. Resolved findings

| ID | Conflict or implementation risk | Resolution / canonical location | Regression evidence required from game |
|---|---|---|---|
| A-01 | Wider game and first release could be read as competing scope; geography mentioned Hungary instead of the approved adjoining set | Core 2.1, 3.1, 13, 33 and 42 explicitly distinguish V1 from later base-game content; V1 territory preserved; AGENTS assigns document responsibility | W-16, RG-06 |
| A-02 | Enduring historical-vehicle rules lived only in the V1 addendum despite applying to the whole game | Detailed rule moved intact to core 15.11; V1 links to it rather than maintaining another version | V-10, V-11, G-07 |
| A-03 | Two names for physical cargo and an ambiguous contract-wide execution plan could create parallel subsystems or shared mutable shipment state | Core 11.9 defines Shipment, CargoLot, TransportPlan and TripAllocation once; core 11.0.1 separates reusable contract template from versioned execution | C-01–C-20 |
| A-04 | Repeated freight-priority definitions could diverge | Core 11.0.1 owns allocation tiers; the canonical cargo model and V1 scope reference them without a competing weighted-score rule | C-09, C-10, C-18 |
| A-05 | Spoilage/return disposition could be counted as terminal while a physical load still occupied a vehicle/store | Core 11.9 distinguishes physical stock pending disposal/return from completed terminal accounting and linked receiving inventory | C-12, C-19 |
| A-06 | Workforce prose said onboard sales never add dwell, contradicting non-through compartment-stock rules | Core 8.4 points to the explicit 14.5 exception; no individual crew/passenger simulation added | V-15 |
| A-07 | Missing ticket channel was described as blocking all journeys, despite an explicit unpaid open-boarding rule | Core 32.2 distinguishes paid sales, unreserved physical boarding and reservation-required confirmation; no fabricated fare | F-17 |
| A-08 | Passenger-group priority could be misread as permission to replace already confirmed individual bookings | Core 32.2 applies priority only to available capacity and requires explicit resolution of existing bookings | F-18 |
| A-09 | Run-around was listed alongside turning as if both changed locomotive facing | Core 14.2 separates facing, travel direction and consist-end position; reverse speed and route limits remain binding | N-10, N-17 |
| A-10 | Core delivery fallback described modern low-loaders without an era gate, contrary to the existing 1900 acceptance scenario | Core 15.8 requires actual period-compatible equipment, route and provider; otherwise delivery is blocked or replanned | V-03 |
| A-11 | An intermediate-service test could be read as silently allowing refueling inside a Trip | Core 18.2/18.4 and V-07 preserve the approved between-Trip rule; long services need real turnaround or valid traction exchange | V-06, V-07 |
| A-12 | Individually valid slot windows need not have a feasible chain of midpoint times; early tolerance could also violate a public departure promise | Core 32.2 checks the entire midpoint/running-margin/dwell chain and forbids early departure from published passenger boarding stops | N-15, N-16 |
| A-13 | Private operational High priority could be interpreted as an advantage against another equal-rights operator | Core 32.2 limits private preference to own services; inter-operator equal-rights dispatch uses a published neutral stable rule | N-05, N-18 |
| A-14 | Version/suspension boundaries did not explicitly handle delayed departures or already generated/preparing Trips | Core 32.2 selects versions by scheduled departure and handles pending Trips, preparation, bookings and suspension dispatch explicitly | F-08, F-09, F-19, F-20 |
| A-15 | Selecting concrete fleet assets late could be mistaken for making no binding capacity reservation before preparation | Core 32.6 reserves shared interval/capability capacity before binding serial-number assets | V-16 |
| A-16 | A road-turnaround example included an optional buffer in its physical minimum | Core 32.6 distinguishes 4-minute physical work from 2-minute planned buffer | V-17 |
| A-17 | Setup preview wording could expose routine local jobs before a branch became operational | Core 7.5 and brief 6.1 allow public setup context without bypassing local Opportunity Board discovery | W-01, W-02, W-15 |
| A-18 | Prepaid partial cancellation needed an explicit exactly-once settlement boundary | Focused cancellation specification separates liability, credited prepayment, new cash payment and refund in one idempotent transaction | F-03, F-21 |
| A-19 | Real-date conversion was deliberately delegated but still unspecified, leaving incompatible import conventions possible | Core 3.4 and DATA_PIPELINE define a versioned proportional source-date mapping, preserved originals and no double conversion | T-08, W-14 |
| A-20 | README said the 1900 preset was implemented, despite documentation-only status; currency authority was implicit in core | README/status corrected, core 38 states the money unit, and actual documentation checks are kept separate from unrun game gates | U-02, RG-09 |
| A-21 | A generic small-storage rule could grant freight handling to every passenger-only station | Core 12.1 requires declared finite integrated freight capability, equipment and space | C-21 |
| A-22 | Mixed reservation/physical state names could trigger fictional unloading or free occupied capacity at Trip end | Core 11.9 separates commercial allocation from physical handling/custody | C-08, C-22 |

No approved mode, map territory, time speed, physical-operation requirement, AI constraint or enduring-vehicle rule was removed to resolve these findings. Detailed cargo/vehicle rules were relocated to their canonical core sections, not deleted. Existing acceptance IDs were retained and 18 focused regression scenarios were added.

## 3. Verification

Commands:

```sh
python3 Tools/check_docs.py
python3 -m unittest discover -s Tools/tests -v
git diff --check
```

Executed locally on 2026-09-30 with Python 3.13.5 against the complete edited snapshot: documentation checks **PASS** (12 Markdown files, 236 numbered headings, 44 local links, 192 scenario/requirement definitions, zero errors); validator self-tests **22/22 PASS**; `git diff --check` **PASS**. Reapplying the reviewed migration to a fresh exact baseline reproduced all ten edited original files byte-for-byte. These are documentation/tooling results, not game tests. GitHub CI must verify the delivery snapshot before promotion. Game compilation, Unity tests, standalone playthroughs, acceptance scenarios and performance benchmarks remain **NOT RUN**.

The validator checks numbered-heading uniqueness, core section references, local links/anchors, duplicate scenario IDs, repeated long prose, SYS-01–SYS-16 coverage and selected explicit regressions. Its self-tests include failures as well as valid cases and exercise only the source-date reference algorithm. It is not a natural-language contradiction solver or a replacement for game integration tests.

## 4. Remaining implementation and authoring work

The exact world clipping polygon, sourced historical content, complete catalogues, balancing, package pins and runtime scheduler phases still need actual implementation/authoring and evidence. These are already delegated engineering/content choices, not reasons to reopen approved product decisions. This audit found no further blocking product question requiring an invented change or an additional user decision.

The next game-development task remains M0 in [IMPLEMENTATION_STATUS](IMPLEMENTATION_STATUS.md), not another rewrite of the high-level plan. Follow the documented source ownership when a future real design decision changes, and update dependent tests at the same time.
