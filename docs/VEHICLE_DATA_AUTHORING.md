# Tranzit — Vehicle data authoring specification

> **Status:** implementation-facing content specification.
>
> Read together with [VEHICLE_CATALOGUE.md](VEHICLE_CATALOGUE.md), [VEHICLE_COVERAGE_AUDIT.md](VEHICLE_COVERAGE_AUDIT.md), [V1_CONTENT_MANIFEST.md](V1_CONTENT_MANIFEST.md) and GAME_DESIGN Section 15.
>
> This document converts the approved vehicle design into versioned data structures and initial authoring defaults. It is not implementation evidence.

## 1. Data ownership

Keep the following as separate stable data objects:

1. `vehicle_model_family`
2. `vehicle_template`
3. `equipment_option`
4. `conversion_path`
5. `manufacturer`
6. `factory_capability`
7. `support_family`
8. `regional_market_profile`
9. `dealer_stock_policy`
10. `used_market_seed_profile`
11. `certification_profile`
12. `import_route_profile`

A concrete vehicle instance references these definitions but stores its own physical identity, history, condition, current template and ownership.

## 2. Vehicle model-family schema

Required fields:

```yaml
schema_version:
id:
fictional_name:
manufacturer_id:
real_prototype_reference:
prototype_sources:
introduction_date:
vehicle_mode: road | rail
vehicle_kind:
role_tags:
physical_platform:
  length_m:
  width_m:
  height_m:
  wheelbase_m:
  empty_mass_t:
  service_mass_t:
  axle_count:
  axle_load_t:
  structural_max_speed_kph:
rail:
  gauge_mm:
  wheel_arrangement:
  minimum_curve_m:
  coupler_family:
  brake_family:
  electrification_systems:
road:
  drive_layout:
  gvwr_t:
  gcwr_t:
traction:
  propulsion_type:
  fuel_or_energy:
  continuous_power_kw:
  max_power_kw:
  starting_tractive_effort_kn:
base_capacity:
  seats:
  standing:
  berths:
  payload_t:
  cargo_volume_m3:
facility_requirements:
support_family_id:
regional_market_profile_id:
factory_capability_ids:
default_template_ids:
used_market_seed_profile_id:
certification_profile_id:
visual_family_id:
sound_family_id:
localization_keys:
notes:
```

Do not store a hard `available_until`.

## 3. Template schema

A template is one valid configuration of an existing fixed platform.

```yaml
schema_version:
id:
model_family_id:
display_name:
built_in: true | false
equipment_option_ids:
derived:
  empty_mass_t:
  service_mass_t:
  seats:
  standing:
  berths:
  payload_t:
  cargo_volume_m3:
  certified_max_speed_kph:
  fuel_or_energy:
  continuous_power_kw:
  max_power_kw:
  maintenance_family_id:
  purchase_component_cost:
compatibility_tags:
certification_variant_id:
visual_variant_refs:
```

Derived fields are generated from platform + equipment and persisted/versioned only where needed for save reproducibility.

## 4. Equipment-option groups

### 4.1 Passenger vehicles

Use only meaningful groups supported by the model:

- **layout/class** — Economy, Business/1st class, mixed zones, sleeper/dining/service spaces;
- **comfort** — seat density/type, insulation, heating, HVAC, lighting, later power/Wi-Fi;
- **flex space** — luggage, bikes, prams, wheelchair/flexible standing space;
- **service** — toilets, catering, luggage/service modules;
- **technical** — brake package, heating/control, train protection, approved speed package.

### 4.2 Road freight

- fixed factory body/platform variant;
- cargo securing/loading equipment;
- refrigeration or specialist handling where supported;
- factory driveline/final-drive option;
- cab/safety/comfort package.

### 4.3 Locomotives

- country/train-protection package;
- train-heating/control package;
- approved engine/traction rebuild;
- braking/speed package;
- communication/safety package.

No option can change fundamental body/frame geometry.

## 5. Initial support families

Support families exist to avoid maintaining one bespoke workshop technology tree per model while preserving real distinctions.

| ID | Scope | Typical models | Workshop needs | Parts behaviour |
|---|---|---|---|---|
| `steam_light_central_eu` | light/simple steam | ČMS 97, 99 | steam fitters, boiler work, basic machining | broad early availability; later specialist |
| `steam_mainline_central_eu` | large steam | 170, N534, N387, N475, N556, N498 | heavy boiler/rod/wheel work, larger lifting capacity | strong domestic support mid-century, specialist later |
| `electric_skoda_dc_early` | early DC electric | Bobina, Šestikolo | HV electric capability, traction motors, contactors | strong domestic support, declines gradually |
| `electric_skoda_ac_early` | early AC electric | Laminát | transformer/HV AC support | region/system specific |
| `electric_skoda_dual_legacy` | later classic electrics | Eso, Pershing | solid-state/control + HV | broad domestic support |
| `electric_modern_multisystem` | modern MS locomotives | 109X, Vektron, TRAX MS | diagnostics, HV, ETCS/country packages | OEM/specialist-heavy |
| `diesel_ckd_small` | small/medium ČKD diesel | Hektor, D742 | diesel-electric workshop, medium lifting | strong domestic parts ecosystem |
| `diesel_ckd_heavy` | heavy ČKD diesel | Čmelda, Barda, Brýlovec | heavy diesel/electrical | broad regional support |
| `diesel_modern_import` | modern imported diesel | ER20 | diagnostics, OEM components | importer/specialist support |
| `railcar_legacy_cz` | legacy motor cars | M120, M131, M240, M262, M152, 842 | railcar diesel/mechanical | domestic but model-specific ageing |
| `emu_legacy_cz` | domestic EMUs | 471 | HV electric + EMU systems | domestic specialist |
| `emu_modern_cz` | modern domestic EMUs | Panter | diagnostics, AC/DC HV | manufacturer/specialist |
| `dmu_modern_import` | modern imported DMUs | 844, 847 | diesel multiple-unit diagnostics | importer/specialist |
| `passenger_coach_wood_early` | wooden/early coaches | L2, B4, early service cars | carpentry, brake/underframe | broad early, specialist heritage later |
| `passenger_coach_steel_standard` | steel/UIC coaches | Y64, Z80 | bogie/brake/HVAC depending template | broad |
| `passenger_trainset_premium` | Pendolino/ComfortJet-class | 680, Comfort 9 | OEM diagnostics/specialist tooling | concentrated OEM network |
| `wagon_early_2axle` | early freight wagons | O10, G10, P12, Z10, I8, H15 | wheels/brakes/body repair | broad |
| `wagon_modern_standard` | modern bogie freight | E28, F50, Z55, R55, intermodal | bogie/brake/specialist tank/reefer as relevant | broad EU market |
| `road_horse_traction` | horse-drawn | H2, H4, omnibus | stable/coachbuilder support | local |
| `road_early_petrol` | pioneering ICE road | Daimlar, L&K, early Pragov | basic engine/mechanical shop | sparse early, improves |
| `road_steam_early` | steam road | Thornycroft | steam specialist | scarce import support |
| `road_cz_legacy_medium` | Praga/Avia/LIAZ medium | RN, V3S, A30, VIAZ | conventional diesel workshop | broad domestic |
| `road_tatra_aircooled_legacy` | Tatra heavy | 111, 138, 148, 815 | specialist heavy chassis/air-cooled engines | strong domestic/regional |
| `road_modern_heavy_cz` | modern Tatra | Fénix | modern heavy diesel diagnostics | domestic/OEM |
| `road_modern_heavy_eu` | Actros/TGX-class | Mercator, MANN | modern truck diagnostics | broad EU |
| `road_battery_heavy_eu` | eActros-class | electric tractors | HV battery, diagnostics, charging | OEM/specialist early |
| `bus_cz_legacy` | 706/Karosa high-floor | 706 RO/RTO, ŠM/ŠL, 700/900 series | conventional bus workshop | broad domestic |
| `bus_eu_legacy` | Ikarus/O303 | imported legacy bus/coach | standard diesel + brand parts | regional |
| `bus_modern_diesel_eu` | CN12/Crossway/Urbino/Lion's City | modern buses | diagnostics, emissions systems | broad but brand-dependent |
| `bus_battery_eu` | NS12E/electric Crossway etc. | battery buses | HV battery, charging, diagnostics | manufacturer/specialist |

A workshop can support several families through equipment + qualified staff.

## 6. Maintenance interval authoring

Do not use one universal interval.

Each template defines several limits where relevant:

```yaml
maintenance:
  routine:
    calendar_days:
    distance_km:
    operating_hours:
  intermediate:
    calendar_days:
    distance_km:
    operating_hours:
  heavy:
    calendar_days:
    distance_km:
    operating_hours:
  inspection:
    legal_or_safety_interval:
  condition_thresholds:
```

Initial balancing principle:

- early steam: frequent routine attention, high labour demand, simple local parts;
- mature steam: high servicing labour + large periodic heavy work;
- early ICE: short intervals and variable reliability;
- mature diesel: longer routine intervals but increasing specialist systems;
- modern electronic vehicles: fewer routine interventions, higher diagnostic/specialist dependence;
- battery EVs: low drivetrain routine service but high-value battery/HV support.

Exact values must be calibrated per prototype/era rather than inferred only from this principle.

## 7. Regional market profiles

Use four presence tiers:

| Tier | Meaning |
|---|---|
| `home` | factory/dealer dense, high stock chance, strong parts/service, deep used market |
| `core_export` | regular dealers/importers, normal certification packages, good support |
| `secondary_export` | direct import/broker common enough, limited dealer stock/support |
| `rare_import` | special-order/import only, sparse parts/service, no arbitrary prohibition |

Example initial profiles:

| Manufacturer | Home | Core export | Secondary export | Rare import |
|---|---|---|---|---|
| ČMS/ČMD/Neškoda/Ringhauer/Studena | Czech/Slovak active regions | Austria, Germany, Poland and neighbouring Central Europe where historically plausible | wider Europe | overseas |
| Fatra/Pragov/VIAZ/Karusa/SORA/Aviat | Czech/Slovak regions | neighbouring Central/Eastern Europe | wider Europe | overseas |
| Daimlar/Benc/Büsink/MANN/Mercator/Símens/Bombardír | Germany | Central/Western Europe | broader Europe | non-European distant markets |
| PESKA/Soláris | Poland | Central/Eastern Europe | wider Europe | distant overseas |
| Ikarusz | Hungary | Eastern/Central Europe | Western Europe where export history supports | distant overseas |
| Ivego/Alstrom | France/Italy source areas | Western/Central Europe | broader Europe | distant overseas |
| Städler | Switzerland/Germany/Poland production network by model | Europe | selected export regions | other |

Per-model export history can override the manufacturer default.

## 8. Factory-capability states

Every model/manufacturer relation uses explicit dated states:

```yaml
factory_capability:
  model_family_id:
  factory_id:
  start_date:
  state: series | low_rate_special | parts_overhaul_only | inactive
  nominal_units_per_game_month:
  batch_size:
  setup_hours:
  labour_hours_per_unit:
  material_recipe_id:
  compatible_template_constraints:
```

A model can remain searchable after all factories are `inactive`.

## 9. Production lead-time model

Initial authoring formula:

> quoted lead = queue wait + setup + unit/batch production + QA/acceptance + supplier-risk allowance

Do not store one fixed "delivery days" number.

Important inputs:

- plant utilization;
- committed orders;
- selected template complexity;
- batch size;
- material availability;
- destination-market adaptation;
- first-type certification where applicable;
- external transport/import leg.

For V1 balancing, quote ranges may use P50/P90 estimates rather than false exact certainty.

## 10. Dealer-stock policy

Dealer stock is model/configuration specific.

```yaml
dealer_stock_policy:
  model_family_id:
  region_tier:
  eligible_template_ids:
  target_stock_min:
  target_stock_max:
  reorder_point:
  reorder_batch:
  dealer_markup_band:
  stock_age_discount_curve:
```

Rules:

- common templates are more likely to be stocked;
- specialist/high-cost variants are normally factory order;
- stock is actual physical inventory;
- dealer replenishment consumes manufacturer capacity.

## 11. 1900 used-market seeding

Seed real assets, not listings without vehicles.

### 11.1 Rail

For each opening region with rail access, world generation should aim for:

- several older small/tank locomotives owned by existing operators/industries;
- at least one credible used light locomotive listing or disposal opportunity over the opening period;
- a smaller chance of used mainline locomotives;
- mixed passenger/freight rolling stock with realistic age distributions.

Suggested 1900 manufacture-year bands:

- 1875–1884: 10–15% of seeded older rail assets;
- 1885–1894: 35–45%;
- 1895–1900: 40–50%.

Older does not automatically mean worse; condition comes from individual history.

### 11.2 Road

Opening regions should contain:

- many horse-drawn commercial vehicles;
- a very small early motor-vehicle population;
- rare imported motor/steam vehicles concentrated in richer/larger markets.

Suggested road-commercial composition around 1900:

- horse-drawn: 92–97%;
- motor/steam commercial: 3–8% in developed urban/industrial markets, lower elsewhere.

These are world-authoring targets, not historical-statistical claims for every locality.

### 11.3 Listing rate

Only a bounded share of existing assets should be for sale.

Opening used-market listing targets:

- ordinary horse/commercial road stock: 2–6% of local relevant fleet;
- early motor road: 1–4%;
- ordinary freight/passenger wagons: 1–3%;
- locomotives: 0.5–2%, with very low absolute numbers in small markets.

If a region has too few assets for percentages to be meaningful, authored fixture rules may guarantee at least one plausible starter opportunity over an opening time window rather than spawning one instantly on day 1.

## 12. 1900 dealer/new-order availability

### Rail

Player-visible strategies should include:

- domestic/regional factory order for current steam;
- used older steam;
- dealer/broker/import quote where historically plausible;
- new rolling-stock orders from active domestic wagon/coach works.

### Road

Player-visible strategies should include:

- local horse vehicle/coachbuilder order;
- used horse stock;
- rare Daimlar/Benc/other imported motor quote;
- rare steam-road import where suitable;
- domestic motor-commercial orders only from their fixed historical introduction dates.

No 1900 fixture may seed a later vehicle early just to ensure choice.

## 13. Certification data

Certification is country + template/configuration scoped.

```yaml
certification_profile:
  id:
  model_family_id:
  template_constraints:
  jurisdiction_id:
  first_type_approval_required:
  supplier_adaptation_package_ids:
  approval_duration_basis:
  approval_cost_basis:
  per_unit_acceptance_required:
  incompatibility_reasons:
```

A previously approved identical template avoids repeated first-type approval.

## 14. Import route data

Inbound off-map vehicles need an authored route family, not a teleport timer.

Examples:

- Central Europe rail delivery;
- road self-delivery;
- hauled/dead-towed rail delivery;
- Britain → Channel/North Sea ferry/ship + continental rail/road;
- overseas → seaport + onward rail/road.

```yaml
import_route_profile:
  id:
  origin_macro_region:
  destination_gateway_ids:
  available_modes:
  distance_band:
  transshipment_count:
  customs_border_steps:
  era_prerequisites:
  base_capacity:
  disruption_tags:
```

Outbound off-map resale remains buyer-collected under GAME_DESIGN Section 15.5.

## 15. Operating-consumption curves

Use a small number of calibrated load points rather than one nominal consumption value.

Road ICE example authoring fields:

```yaml
consumption_curve:
  idle_per_game_hour:
  empty_flat_per_100km:
  half_load_flat_per_100km:
  full_load_flat_per_100km:
  hill_severity_factor:
  urban_stop_start_factor:
```

Electric rail/road equivalent uses kWh. Steam uses coal/fuel + water. Horse traction uses feed/water/rest demand.

## 16. Price authoring

Do not finalize absolute `money` prices until the economy reference basket is locked.

For now store:

- same-era platform cost index;
- equipment option cost indices;
- factory labour/material share;
- dealer markup band;
- import/logistics cost basis;
- certification cost basis;
- maintenance labour/material indices;
- residual/salvage basis.

When explicit `money` values are authored, retain the decomposed basis so prices remain explainable.

## 17. Initial validated parameter corrections

The expanded catalogue should use these researched values where present:

| Model | Validated authoring anchors |
|---|---|
| ČMD D742 | 883 kW, 192 kN max tractive effort, 90 km/h, 64 t, 80 m minimum curve, ~16 t axle load |
| ČMD D669 | 993 kW, 280 kN, 90 km/h, 114.6 t, 80 m minimum curve |
| Neškoda A489 | 3,080 kW, 320 kN max tractive effort, 110 km/h, 85 t, 25 kV 50 Hz |
| Studena 471 | 2,000 kW, 140 km/h, 310 seats incl. 23 first class, up to ~643 total passengers, 79.2 m |
| Soláris Urbino 12 | production from 1999; 12 m low-floor; up to ~105 total; early diesel engines around 162–184 kW depending template |
| MANN Lion City 12 | 12.2 m modern family; up to 37 seats in current diesel two-door configuration; diesel templates around 206–265 kW in later generation |

These anchors do not imply every historical subseries shares one identical configuration.

## 17.1 Initial manufacturer/factory capability timeline

These are authoring anchors for capability state transitions. They are intentionally capability-level rather than exact annual output schedules.

| Fictional manufacturer / plant | Capability timeline |
|---|---|
| **Ringhauer Smíchov** | Railway-car/wagon production active before the 1900 start; broad passenger/freight body capability at opening. In 1936 the historical lineage consolidates into a larger wagon-building concern. The game can preserve the original plant/company identity or record the merger while keeping existing assets unchanged. |
| **Neškoda Plzeň** | Heavy engineering exists in 1900, but complete own locomotive production starts after WWI; first own locomotive capability from 1920. Steam locomotive capability expands through the interwar/post-war period; electric locomotive capability begins in the late 1920s and later becomes a core line. |
| **ČMS / ČMD Praha** | Opening-era railway machinery/locomotive capability reflects the Bohemian-Moravian engineering lineage. Later capability shifts increasingly toward diesel/electric locomotive production and overhaul. |
| **Studena Vagónka** | Railway-car/wagon production is active through the 20th century; later becomes a major railcar/EMU production source. |
| **Lorin & Klement, Mladá Boleslav** | Early road-vehicle capability active before/around the 1900 start for bicycles/motor vehicles, with commercial-vehicle/bus variants becoming available only on their fixed historical dates. |
| **Fatra Kopřivnice** | Road/commercial vehicle capability active before the 1900 start through the Nesselsdorf/Tatra lineage; authored truck families begin on their fixed historical introduction dates. |
| **Pragov Praha** | Road-vehicle capability appears when the historical Praga lineage supports the relevant authored model families; no pre-introduction generic truck spawning. |
| **VIAZ** | Truck production capability begins from the early 1950s industrial lineage; the modern 100-series capability begins from 1974/1975. |
| **Karusa Vysoké Mýto** | Bus-body production lineage is active by 1947; Karosa state-enterprise identity from 1948. 706 RO-family production from 1947, RTO-family from the later 1950s and Š 11 family from 1965. |
| **Aviat Letňany** | Medium commercial-vehicle production capability appears with the Avia/Saviem-derived programme; A30-family availability follows its historical introduction rather than being backfilled earlier. |
| **SORA Libchavy** | Company formation in 1991; bus development starts in 1992 and first prototype appears in 1993. No SOR-badged bus production before that. |
| **CZ LOKA** | Modern locomotive rebuild/new-build capability follows the historical successor/rebuild specialist timeline; do not project modern EffiShunter capability backwards. |

### Authoring rule for mergers and successor firms

A merger, nationalization, privatization or company-name change can alter:

- factory owner;
- active brand/manufacturer identity for new orders;
- support network;
- export network;
- capability investment.

It never rewrites the original manufacturer field of an existing physical vehicle.

### Source anchors

- Ringhoffer/VÚKV history: railway-vehicle design/manufacture at Smíchov from the 19th century; 1936 merger into Ringhoffer-Tatra.
- Škoda Group history: first complete Škoda locomotive delivered in 1920; first electric locomotive programme in the 1920s; substantial interwar export activity.
- LIAZ history: vehicle production in the Liberec/Mnichovo Hradiště/Rýnovice network from 1951; 100-series introduced in 1974–1975.
- Iveco Bus/Karosa history: 706 RO production from 1947, Karosa state enterprise from 1948, RTO programme in the later 1950s, Š 11 production from 1965.
- SOR official history: company established in 1991, development from 1992, first prototype in 1993.

## 17.2 Initial regional market/export profiles

These defaults should be refined per model, but are sufficient to prevent every manufacturer from having identical worldwide availability.

| Manufacturer family | 1900–1945 profile | 1946–1989 profile | 1990+ profile |
|---|---|---|---|
| Ringhauer / domestic wagon works | home CZ/Bohemian-Austrian sphere; core regional Central Europe | home/Central Europe; successor-network supply | mainly legacy/used/support, successor products handled by later works |
| Neškoda | before 1920 heavy components rather than complete own locomotives; from 1920 strong domestic + active exports | strong domestic/Central/Eastern Europe plus selected exports | strong domestic/EU rail market, broader exports by model |
| ČMS/ČMD | home Central Europe, selected regional exports | strong domestic/Eastern-bloc + export programmes | legacy/rebuild/used ecosystem, successor specialists |
| Fatra | home Czech/Slovak/Central Europe | strong Central/Eastern Europe and selected global specialist exports | specialist heavy-road exports remain broad |
| Pragov | home/regional Central Europe | strong domestic/regional | used/legacy support dominates later |
| VIAZ | n/a before capability | home + Eastern/Central Europe, selected exports | used/legacy market; later successor availability is separate |
| Karusa | n/a before bus lineage | strong home + significant export share | home/core Central Europe then Ivego-successor network |
| SORA | n/a | n/a until 1991 | home Czech/Slovak, core Central/Eastern Europe, selected EU exports |
| German manufacturers | Germany home; Central/Western Europe core | strong European export | broad EU/global |
| Ikarusz | Hungary home | very strong Eastern-bloc/Central Europe export | used/support-heavy after classic production era |
| PESKA/Soláris | n/a/limited before modern period | domestic Polish capability by relevant model era | Poland home, Central/Eastern Europe core, broader EU exports |

## 17.3 Initial factory-capacity balancing bands

These are **game balancing bands**, not claims of historical monthly output.

Use them to initialize the economic simulation before plant-specific calibration:

| Factory scale | Road vehicles / game month | Railcars/locomotives / game month | Coaches/wagons / game month |
|---|---:|---:|---:|
| small/specialist | 2–8 | 0.5–2 | 2–10 |
| medium | 8–30 | 1–5 | 10–40 |
| large/mass-production | 30–120+ | 3–12 | 30–120+ |

The 14-day game month is the accounting unit here. A fractional rail rate means one unit may take several game months.

Actual output is constrained by labour, material supply, plant-hours, setup/changeover and backlog. Do not turn these bands into guaranteed free output.

## 18. Completion gate for one vehicle family

A model family is content-complete only when all of the following exist:

- researched prototype provenance;
- machine-readable model definition;
- at least one valid template;
- equipment compatibility matrix;
- factory/source capability;
- regional market profile;
- support/maintenance family;
- consumption curve;
- explicit purchase/operating cost basis;
- certification/import handling where relevant;
- prefab/LODs/materials/sounds/anchors;
- used-market behaviour;
- save/load identity support;
- tests for compatibility, production/import/delivery, retrofit and resale.

A Markdown catalogue row alone never satisfies this gate.
