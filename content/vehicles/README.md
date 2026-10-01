# Vehicle content data

This directory contains versioned machine-readable **authoring data** for Tranzit's vehicle system.

It is intentionally separate from gameplay code and art. A row here is not a claim that the vehicle is implemented, rendered or tested.

## Current scope

The committed authoring pack now covers:

- manufacturer/source identities;
- support/maintenance families;
- regional market-presence profiles;
- the complete 1900 opening vehicle families required by the current V1 content target;
- dated model/template/equipment packs for **1900, 1901–1919, 1920–1959, 1960–1989 and 1990–2026**;
- opening-market seeding defaults for the 1900 start;
- historical progression from steam/horse/early motor operation through diesel/electric rail, standardized road fleets, intermodal equipment and modern electric vehicles.

Rows remain authoring data, not implemented Unity assets. Representative prototype values, sources and production lineages are retained per model; values marked as authoring estimates still require final asset/balance validation before release.

## Rules

- Stable IDs never change because of localization or company renaming.
- Real brands/prototypes appear only in provenance fields. Player-facing names are fictionalized.
- `introduction_year` is historical content, not a randomized unlock.
- There is no `available_until` gameplay gate.
- New-build capability is represented separately through manufacturer/factory capability state.
- Physical dealer/used stock is runtime world state; this folder only defines how it may be seeded/generated.
- All prices remain relative authoring indices until explicit `money` balancing is completed.
- Game calendar durations use the 14-day month/168-day year.
- Source URLs and source precision must be retained.

Authoring rules are defined in:

- `docs/VEHICLE_CATALOGUE.md`
- `docs/VEHICLE_CONTENT_AUTHORING.md`
- `docs/VEHICLE_COVERAGE_AUDIT.md`
