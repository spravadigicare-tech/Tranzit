# Tranzit — Data pipeline conventions

Status: specification plus documentation-validation reference examples, not a completed world importer or bundled geographic dataset. Shared runtime time rules remain in [GAME_DESIGN Section 3](GAME_DESIGN.md#3-time-start-dates-and-historical-progression).

## 1. Date domains and provenance

Every authored date declares its domain: `source_gregorian` or `game_calendar`. Never infer the domain from whether its day happens to be at most 14.

Keep the original source date, source calendar, precision, source/provenance reference and conversion version alongside the resulting game date. A source using another historical calendar must first receive a documented, sourced conversion; do not relabel it Gregorian. A year-only or approximate source must retain that precision and an explicit authored scheduling decision, not silently acquire a supposedly historical exact date.

Already game-authored dates use 12 months with 14 days each and are validated directly. They must never be sent through the source-date conversion a second time.

## 2. Gregorian source-date conversion

Engineering convention: `gregorian-month-proportional-v1`. It preserves year, month, seasons and ordering within a source month, while fitting the approved shorter calendar. It is not a claim that the game preserves real elapsed-day counts or historical weekdays.

First validate the complete Gregorian source date, including month length and leap-year validity. Then use integer arithmetic:

```text
L = number of days in the validated source month
game_year = source_year
game_month = source_month
game_day = 1 + ((source_day - 1) * 14) // L
```

Apply this to every imported day, including source days 1–14. Mapping only days above 14 would reorder events and mix two calendars. Retain the original date; never use the game date as the input to another conversion.

| Source | Game date or result |
|---|---|
| 1900-01-01 | 1900-01-01 |
| 1900-01-14 | 1900-01-06 |
| 1900-01-31 | 1900-01-14 |
| 1900-02-28 | 1900-02-14 |
| 1900-02-29 | Reject invalid source date |
| 2000-02-29 | 2000-02-14 |
| Game-authored 1900-01-14 | Remains 1900-01-14; no conversion |

Runtime calendar arithmetic, payroll, interest, contracts, timetables, duration/age calculations and seasonal recurrence use the shared 168-day game year. Gregorian date libraries are allowed in the source-import/reference-validation step only, not as runtime period arithmetic.

Source rate units also need explicit normalization. This date mapping does not automatically convert a historical annual production figure, wage or interest rate into an in-game rate.

## 3. Collisions and historical initialization

Several source dates can map to one game day. Resolve event prerequisites first; for otherwise independent events use original source date/time and then stable event ID. Validate cycles, missing prerequisites and duplicate IDs. Preserve the resulting deterministic order in content and save compatibility metadata.

Mapped order does not replace the simulator's separate causal event phases for arrivals, handling completion, cutoffs and departures. Those phases must be documented and tested when the simulation scheduler is implemented.

Events predating a selected start belong to initialized world state rather than a replay queue. Keep stable event IDs across initialization and progression so an event is not applied twice. Approximate/date-varied events must still honor their prerequisites and declared bounds.

Changing this conversion version requires rebuilding and validating affected content plus an explicit save migration/compatibility decision. Existing saves must not silently retime contracts or replay historical events.

## 4. Remaining world-production work

The full pipeline still needs the approved coverage polygon, provenance-tracked terrain/water/settlement data, historical overlays, jurisdictions, networks, firms, catalogues, localization, chunk baking and bundled offline outputs. See [V1_CONTENT_MANIFEST](V1_CONTENT_MANIFEST.md) and [V1_IMPLEMENTATION_BRIEF](V1_IMPLEMENTATION_BRIEF.md).

The date convention supplies none of those datasets. Their exact authored values, licences, historical plausibility and release coverage require implementation/content evidence; a documentation check is not a world-build test.

## 5. Verification

Run `python3 Tools/check_docs.py` and `python3 -m unittest discover -s Tools/tests -v`. The validator tests exercise the reference conversion, invalid dates, month endpoints and monotonic ordering, as well as documentation integrity. They do not execute the Unity calendar or satisfy T-01–T-08 by themselves. The eventual importer and runtime must pass the game acceptance scenarios independently.
