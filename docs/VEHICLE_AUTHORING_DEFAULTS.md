# Tranzit — Vehicle content authoring defaults

> **Status:** balancing and data-authoring companion to [VEHICLE_CATALOGUE.md](VEHICLE_CATALOGUE.md).
>
> These values are initial content defaults, not claims that the game is implemented. Historical prototype values remain sourced per model; balancing values below exist to make the catalogue internally consistent and testable.

## 1. Authoring goals

Vehicle content should answer six separate questions:

1. **What physically exists?** — model family, factory-produced variant and concrete vehicle instance.
2. **What can be ordered?** — current manufacturer capability, dealer stock, used listings and leases.
3. **Where can it be supported?** — parts, workshop skill/equipment and service-provider network.
4. **What can it physically do?** — performance, capacity, route compatibility and equipment template.
5. **What does it cost to own and operate?** — configured purchase cost, energy/fuel, staff, maintenance and downtime.
6. **How quickly can the player actually get it?** — backlog, manufacturing, approval, import and physical delivery.

Do not collapse these into one `availability`, `reliability` or `running_cost` scalar.

## 2. Stable content identities

Use separate IDs for:

- `manufacturer_id` — corporate identity;
- `factory_id` — physical production plant;
- `model_family_id` — underlying physical platform/model family;
- `factory_variant_id` — fixed body/chassis/platform variant;
- `equipment_option_id` — one supported configurable package;
- `template_id` — saved combination of options;
- `support_family_id` — parts/tools/skills compatibility;
- `vehicle_instance_id` — one physical serial asset;
- `approval_family_id` — national/type-approval identity where needed.

Renaming, mergers and ownership changes never rewrite stable IDs.

## 3. Manufacturer/factory capability states

Every factory/model pairing has a dated capability timeline.

| State | Can build complete vehicle? | Parts | Retrofit/overhaul | Typical commercial effect |
|---|---|---|---|---|
| `series` | Yes | Strong | Yes | ordinary lead time and pricing |
| `low_rate` | Yes, finite/special order | Moderate/strong | Yes | higher unit cost, longer setup |
| `support_only` | No | Yes | Yes | used/rebuild market only |
| `specialist_only` | No | External/limited | Specialist | scarce support and long lead time |
| `heritage_only` | No | Reproduction/local substitutes only | Heritage specialist | expensive restoration, no normal new build |
| `none` | No | No current supplier | No current qualified provider | existing asset remains but support requires a newly found/created capability |

A capability transition is effective-dated. It never deletes assets or model definitions.

## 4. Regional market-strength weights

These weights guide dealer stock, used-market prevalence, quote friction and ordinary support availability. They are **not hard probabilities used blindly**; actual physical assets and companies still control offers.

| Market relationship | Dealer/stock weight | Parts/support weight | Used-market weight | Direct-order friction |
|---|---:|---:|---:|---|
| Home/core market | 1.00 | 1.00 | 1.00 | baseline |
| Strong export market | 0.70 | 0.75 | 0.70 | low |
| Established secondary export | 0.40 | 0.50 | 0.40 | moderate |
| Rare export market | 0.15 | 0.20 | 0.15 | high |
| No established network | 0.00 dealer seeding | 0.05 specialist knowledge | 0.02 exceptional used | direct factory/importer quote only |

The player can still deliberately request an import from a `No established network` market when trade/logistics allow it.

### 4.1 Initial manufacturer-market examples

These are starting authoring directions for the Czech-and-adjoining-region world, not trademark/licence claims.

| Fictional manufacturer | Home/core | Strong export / nearby | Rare/special order |
|---|---|---|---|
| ČMS / ČMD | Czech lands / Czechoslovak successor market | Slovakia, Poland, Austria, selected Eastern/Central Europe | distant Western markets |
| Neškoda | Czech lands / Czechoslovak successor market | Slovakia, Central/Eastern Europe; later broader European rail market | distant markets outside export programmes |
| Ringhauer | Czech lands / former Austro-Hungarian region | Austria, Slovakia, regional railways | distant markets |
| Fatra | Czech lands / Czechoslovakia | Central/Eastern Europe, selected export markets | distant Western markets depending era |
| Pragov | Czech lands / Czechoslovakia | regional/Eastern export | distant markets |
| VIAZ | Czechoslovakia | Eastern/Central Europe | Western markets |
| Karusa | Czechoslovakia/Czechia | Slovakia, Eastern/Central Europe | distant markets |
| SORA | Czechia | Slovakia and nearby Central Europe | distant markets |
| Símens | Germany/Austria | broad European market | global special order |
| Mercator-Benz | Germany | broad European road market | global |
| MANN | Germany | broad European road market | global |
| PESKA | Poland | Central/Eastern Europe | wider Europe by programme |
| Soláris | Poland | broad European urban-bus market | distant markets |
| Ikarusz | Hungary | historically strong Eastern/Central export | Western/distant markets |
| Alstrom | France/Italy lineage | broad European market | global by programme |

Exact dated export-market changes belong in data, not hardcoded logic.

## 5. Support families

Support compatibility should be broad enough to avoid hundreds of tiny part classes but specific enough that old/foreign technology matters.

### 5.1 Rail support families

| ID | Typical content | Workshop capability |
|---|---|---|
| `rail_steam_light_pre1918` | small/local steam locomotives | boiler/steam fitting, rods, mechanical machining |
| `rail_steam_mainline` | large steam locomotives | heavy lifting, boiler work, wheel/rod machining |
| `rail_diesel_mechanical_light` | light railcars/small diesel units | diesel mechanical, gearbox, basic electrical |
| `rail_diesel_electric_legacy` | Hektor/Barda/Brýlovec/Čmelda/Kocour families | heavy diesel, generator/traction motors, legacy controls |
| `rail_electric_dc_legacy` | Bobina/Pershing-style DC stock | high-voltage DC, traction motors, legacy controls |
| `rail_electric_ac_legacy` | Laminát-style AC stock | transformer/AC traction legacy tooling |
| `rail_electric_dualsystem_legacy` | Eso-family | DC+AC equipment, electronics |
| `rail_modern_ac_drive` | 109X/Vektron/TRAX/EffiShunter electrical systems | power electronics, diagnostics, modern safety systems |
| `rail_coach_wood_legacy` | early wooden coaches | carpentry, mechanical brakes/heating |
| `rail_coach_steel_conventional` | Y/Z and conventional steel coaches | bogies, brakes, HVAC/electrical by template |
| `rail_multiple_unit_legacy` | M131/M240/M152/842 etc. | integrated drivetrain/body systems |
| `rail_multiple_unit_modern` | 471/844/847/Panter/Pendolino | diagnostics, electronics, HVAC, modern doors/control |

A workshop can support several families if equipped/staffed appropriately.

### 5.2 Road support families

| ID | Typical content |
|---|---|
| `road_horse_operation` | harness/vehicle maintenance + stable support |
| `road_petrol_pioneer_pre1914` | early petrol commercial vehicles |
| `road_steam_pioneer` | steam road vehicles |
| `road_legacy_petrol_diesel_pre1950` | interwar commercial vehicles |
| `road_heavy_diesel_legacy` | V3S/706/Fatra/VIAZ-era heavy trucks |
| `road_light_medium_legacy` | Aviat and similar distribution vehicles |
| `road_modern_diesel_euro` | modern European vans/trucks |
| `road_battery_heavy` | battery-electric heavy road vehicles |
| `bus_legacy_front_engine` | early/RO/RTO-type buses |
| `bus_legacy_rear_engine` | ŠM/ŠL/700/900/Ikarusz families |
| `bus_modern_diesel` | Crossway/SORA/MAN/Solaris modern buses |
| `bus_modern_battery` | battery-electric buses |

## 6. Parts availability states

A support family in a region can have:

- `common` — ordinary local stock and several providers;
- `available` — normal order, modest lead time;
- `scarce` — specialist suppliers, longer lead time;
- `reproduction` — made to order locally/by specialist;
- `salvage` — mostly donor vehicles/used parts;
- `unavailable` — no current legitimate source.

A specific repair can combine several parts states. Do not reduce the whole model to one permanent "obsolete" multiplier.

## 7. Maintenance authoring bands

Exact intervals are model data. When an exact historical maintenance schedule is unavailable or too detailed, author one of these transparent baseline bands and calibrate by playtest.

| Band | Routine inspection target | Intermediate service | Heavy overhaul tendency | Typical use |
|---|---|---|---|---|
| A — simple/light | frequent visual checks | short workshop job | long relative interval | horse vehicles, simple wagons, basic road vehicles |
| B — conventional | regular mileage/hour/calendar service | moderate job | medium interval | ordinary trucks/buses/coaches |
| C — heavy mechanical | regular + subsystem checks | longer service | significant heavy work | steam, large diesels, heavy trucks |
| D — electrical/complex | diagnostic + mechanical schedule | specialist job | scheduled component overhaul | electrics, EMUs/DMUs |
| E — modern integrated | condition/diagnostic-led + legal schedule | modular specialist service | major component replacement/overhaul | modern traction/battery/complex trainsets |

Each actual model still stores explicit kilometre/hour/calendar triggers and required workshop family. The band is only an authoring starting point.

## 8. Explainable failure characteristics

Model data can define named tendencies with trigger inputs instead of opaque reliability scores.

Examples:

| Characteristic | Simulation consequence |
|---|---|
| Simple mechanical design | lower repair-skill requirement, more local providers |
| High thermal load | sustained high-power use accelerates relevant condition loss |
| Complex electrical controls | low ordinary mechanical wear but specialist diagnostics required |
| Strong underframe / conservative design | slower structural condition degradation |
| Weak cooling in heavy duty | hot weather/high-load duty raises defect probability |
| Mature mass-produced family | broad parts/support network in strong markets |
| Low-volume imported model | support depends more strongly on importer/specialists |

Every characteristic must be justified by the real prototype family or generic technology, not invented solely for balance.

## 9. Equipment-option groups

### 9.1 Passenger rail/road

Use only the groups the platform supports:

- class/layout: dense economy, economy, business/first, mixed zones;
- flexible space: luggage, bikes, prams, wheelchair;
- catering/service: none, vending/basic service, galley, restaurant;
- sanitation: none/period toilet/retention toilet;
- climate: basic heating, improved heating/ventilation, HVAC;
- accessibility: steps/basic, lifts/ramps, low-entry/low-floor where built into platform;
- passenger information: period signage, PA, electronic information, later network/Wi-Fi;
- technical: brakes, train heating/control, door control, safety systems, certified speed package.

Seat count is derived from the physical layout. Comfort equipment consumes real space/mass/cost when applicable.

### 9.2 Freight wagons

Configuration options are narrower:

- brake package;
- permitted speed package;
- securing/lashing equipment;
- removable covers/tarpaulin where supported;
- insulation/ice equipment;
- mechanical refrigeration on compatible later platforms;
- hazardous/tank fittings;
- container securing equipment on compatible flats;
- loading/discharge equipment.

A wagon cannot change between unrelated body families.

### 9.3 Locomotives

- train heating;
- country signalling/train-protection;
- radio/communications;
- braking/control package;
- historically offered engine/traction rebuild;
- multiple-working/control package;
- certified speed package.

### 9.4 Road freight

Fixed factory body/platform plus:

- cargo securing/handling;
- tipper/hydraulic equipment where that factory body supports it;
- refrigeration;
- tank/pump package;
- trailer coupling/fifth wheel where platform supports it;
- final-drive/engine factory option;
- cab comfort/safety;
- later telematics/emissions equipment.

## 10. Template naming and inheritance

Built-in templates are convenience presets. Recommended naming:

- `Economy`
- `Economy Neo`
- `Business`
- `Business Neo`
- `Regional`
- `Intercity`
- `Cargo Standard`
- `Cargo Cold`
- `Heavy Duty`
- `International`

Player-created templates inherit the model family's equipment compatibility but do not inherit future equipment automatically. If a new package unlocks historically, existing templates stay unchanged until the player edits/duplicates them.

## 11. Purchase-price authoring

Until explicit `money` values are calibrated, calculate a normalized configured acquisition index:

`configured_index = platform_index + equipment_index + destination_adaptation_index + scarcity/setup_index`

Do not use this index directly as player money.

Initial guidance:

| Acquisition state | Relative effect versus ordinary current-series domestic order |
|---|---|
| High-volume standardized fleet order | lower per-unit production/setup component |
| One-off ordinary series order | baseline |
| Rare factory option | modest premium |
| Low-rate/special-order obsolete model | large setup premium |
| Strong-market import | transport + modest commercial friction |
| Rare distant import | transport + broker/approval + support-risk premium |
| Dealer stock | premium for immediate manufactured inventory |
| Used excellent | condition/age/market-driven; can approach new price if scarce |
| Used worn | strong discount offset by near-term work |
| Heritage/restored | restoration cost and collector/specialist market can exceed utility value |

The game exposes actual money amounts and reasons; these bands only guide content balancing.

## 12. Production lead-time authoring

A factory order is:

`quote/commitment → queue → material readiness → assembly → test/acceptance → finished stock → physical delivery`

Initial relative bands:

| Vehicle | Single-unit production work | Batch behavior |
|---|---|---|
| simple wagon/coach body | short | strong batch efficiency |
| early road vehicle | medium, high artisanal content | limited early batch efficiency |
| mature truck/bus | medium | strong batch efficiency |
| steam locomotive | long | moderate batch efficiency |
| legacy diesel/electric locomotive | long | moderate |
| modern locomotive | long | moderate; electronics/supplier dependencies |
| railcar/EMU | long | strong programme/batch logic |
| complex fixed trainset | very long | programme-level staged production |

Actual completion depends on real plant backlog and inputs. A table value never overrides factory capacity.

## 13. 1900 opening-market seed

The 1900 seed must make several legitimate starts possible without guaranteeing every model locally.

### 13.1 Rail vehicle world stock

For each supported starting macro-area, target:

- at least 2–4 identifiable used light/local steam locomotives potentially tradeable across nearby operators/dealers;
- at least 1–3 identifiable used/mainline steam locomotives potentially tradeable;
- active production capability for at least one light/local steam family somewhere in the active or nearby off-map market;
- active production capability for at least one heavier steam family;
- finite dealer/builder stock of representative freight/passenger wagons;
- enough used passenger/freight rolling stock listings to assemble a small train without assuming all stock is at one seller.

This is a **world fixture target**, not a guarantee that every asset is affordable or immediately available to the player.

### 13.2 Road vehicle world stock

In a supported starting macro-area, target:

- abundant local horse-drawn new/used supply;
- several physical horse freight vehicles for sale/lease across local coachbuilders/dealers;
- at least one credible imported early motor-truck quote path;
- a small chance of physical imported motor stock in a major-city dealer/importer;
- rare steam-road quote/stock through specialist importers rather than normal ubiquitous inventory;
- motor omnibus import/order access in major markets, while horse omnibus supply remains the normal cheap passenger-road option.

### 13.3 Starting dealer behavior

Do not seed one omniscient super-dealer.

A 1900 major-city vehicle market can instead contain:

- local coachbuilder/horse-vehicle seller;
- railway works/manufacturer sales office;
- wagon/coach works;
- general machinery/import agent;
- specialist foreign-motor importer.

Smaller towns rely more on order/import and used listings.

## 14. 1900 representative acquisition profiles

These profiles provide balancing contrast.

| Vehicle | Price position | Lead-time position | Support | Primary trade-off |
|---|---|---|---|---|
| Městský valník H2 | very low | short/local build | common | slow but cheap/flexible |
| Těžký povoz H4 | low | short-medium | common | payload at very low speed |
| Daimlar Lastwagen 5 | very high | long import/order | scarce | much faster motor flexibility |
| Thornycroft Steam 1T | very high | very long/specialist import | very scarce | experimental/specialist alternative |
| ČMS 97 Mravenec | low used / moderate new | used immediate-ish or factory queue | strong regional | tiny/light/cheap but low power |
| ČMS 99 Lokálka | medium | factory/used | strong regional | better local mixed service |
| ČMS 170 Horal | high | long | established heavy-steam network | serious freight capability |
| ČMS 6 Rychlík | used/scarce | no ordinary new production in 1900 | specialist but known | speed/express at used-market scarcity |

The 1900 opening should therefore feel technologically transitional rather than artificially motorized.

## 15. Used-market valuation inputs

Used price is derived from:

- configured new/replacement value if a comparable new build exists;
- age;
- individual condition;
- remaining inspection/service margin;
- mileage/hours;
- current support/parts access;
- current regional demand;
- scarcity;
- retrofit/template desirability;
- delivery/collection responsibility;
- legal/certification status.

Do not impose an automatic depreciation curve that forces every old but desirable/rare asset to near-zero value.

## 16. Lease/rental authoring

Lease supply must be historically appropriate.

- 1900 road/rail leasing is limited and provider-specific; do not seed a modern fleet-leasing market.
- Equipment hire, railway-company rolling-stock arrangements and dealer/manufacturer finance can represent period-appropriate alternatives where documented/plausible.
- Modern eras can have dedicated lessors and larger standardized pools.
- A lessor owns physical units or has committed manufacturer delivery; no infinite catalogue leasing.

## 17. Data fields required before implementation

Each model/factory variant should eventually have machine-readable values for:

```text
stable IDs
real prototype / source provenance
fixed introduction date
factory capability timeline
regional market-strength timeline
physical dimensions/mass/axles
performance/tractive effort/power
platform structural limits
base capacity/body function
supported equipment groups/options
default templates
support family
parts families
maintenance triggers/workshop requirements
consumption curve inputs
failure characteristics
crew qualifications
route/energy/control compatibility
production inputs/work units
configured-cost basis
dealer/used seeding weights
approval families
prefab/LOD/animation/sound refs
localization
```

No content row counts as implemented until the physical asset, data, UI, save/load and relevant tests exist.

## 18. Content audit checklist

Before accepting a vehicle family:

- real prototype existed and introduction date is sourced;
- fictional name/manufacturer are internally consistent;
- gameplay role is materially distinct or fills a coverage gap;
- physical manufacture/import source exists;
- support family is defined;
- template/equipment options are bounded and intuitive;
- route/cargo/passenger compatibility is explicit;
- operating consumption has physical inputs;
- maintenance is explainable;
- used-market behavior is possible;
- no hard expiry date exists;
- current new-build capability can still cease naturally;
- imports/exports obey trade state;
- off-map buyer pickup rule is preserved;
- no player-funded fictional vehicle design is introduced.
