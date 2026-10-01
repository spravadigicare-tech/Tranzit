# Tranzit — Vehicle content authoring defaults

> **Status:** balancing/content authoring specification. This document turns the rules in [VEHICLE_CATALOGUE.md](VEHICLE_CATALOGUE.md) into repeatable data-authoring defaults for factories, offers, support, maintenance and the 1900 starting market.
>
> These values are **game balancing defaults unless explicitly identified as sourced historical dates/specifications**. They are not implementation evidence and do not override the physical vehicle rules in [GAME_DESIGN.md](GAME_DESIGN.md).

## 1. Purpose and authoring principle

The vehicle system needs enough structured data that the simulation can answer, without hidden exceptions:

- who can build a model today;
- where it is built;
- whether the factory has capacity;
- how long production will take;
- where dealer stock can plausibly exist;
- whether the model is common or exotic in a region;
- who can service it;
- how difficult parts are to obtain;
- what a used unit is actually worth;
- whether a chosen template can be built or retrofitted;
- what happens to all of those answers as decades pass.

Do not author one universal `availability` number.

Keep at least these layers separate:

1. historical model introduction;
2. factory production capability;
3. current factory backlog;
4. regional sales/dealer presence;
5. physical dealer stock;
6. used-market stock;
7. national approval;
8. legal/trade access;
9. delivery logistics;
10. workshop capability;
11. parts/support capability;
12. individual vehicle condition.

## 2. Manufacturer capability timeline

The table below defines **capability lineage anchors**, not every corporate/legal rename. A corporate rename must not rewrite the manufacturer stored on already-built assets.

| Fictional lineage | Historical anchor | Vehicle capability timeline used for authoring | Map treatment |
|---|---|---|---|
| **ČMS → ČMD Praha** | BMMF/ČKD industrial lineage | pre-1900 steam/rail engineering and wagon capability; interwar locomotive/vehicle production; post-war diesel/electric engineering; later decline/restructuring | active-map Praha manufacturer when relevant capability exists |
| **Neškoda Plzeň** | Škoda Works | locomotive parts before 1900; locomotive repair 1917–1918; **complete locomotive production from 1920**; steam then electric locomotive lineage; later modern electric rolling-stock production | active-map Plzeň heavy rail factory |
| **Ringhauer Smíchov** | Ringhoffer | strong 19th-century wagon/coach production; passenger/freight rolling stock into 20th century; later corporate consolidation | active-map coach/wagon/body factory while capability exists |
| **Studena Vagónka** | Staudinger Waggonfabrik / Vagonka Studénka | **company founded December 1900**; passenger/freight rolling stock; later railcars/EMU; personal rolling-stock production moved to Ostrava in 2001; Škoda Group from 2005 | active-map Studénka until relocation; later Ostrava/Škoda-linked plant |
| **Lorin & Klement** | Laurin & Klement | motor vehicles from early 20th century; documented Type E commercial/omnibus production from 1908; later integrated into Škoda automotive lineage | active-map Mladá Boleslav early road manufacturer |
| **Fatra Kopřivnice** | Tatra | carriage works from 1850; railway wagons from 1881; first car 1897; first truck 1898; strong truck lineage through the full game period | active-map Kopřivnice road/heavy vehicle factory |
| **Pragov Praha** | Praga | early/mid-century road vehicles; RN 1933–1953; V3S 1953–1990 across several production arrangements; Praga plant ceases normal truck manufacture after industrial reorganization in 1964, while production lineage continues elsewhere | model production capability may move between factories; brand lineage remains distinct |
| **Aviat Letňany** | Avia | post-war industrial manufacturer; medium commercial-vehicle production becomes relevant for the A-series era | active-map Praha-Letňany when road-vehicle capability is authored |
| **VIAZ** | LIAZ | heavy truck lineage from post-war Škoda 706 production; modern 100-series production begins in 1974 and evolves through later ranges | active-map north-Bohemian heavy truck factory network |
| **Karusa → Ivego Vysoké Mýto** | Sodomka/Karosa/Irisbus/Iveco | Sodomka site 1895; first bus body 1928; Karosa from 1948; 700 series from 1981; Renault cooperation from 1993; Irisbus control 1999; Iveco ownership 2003; Iveco Czech 2007; Iveco Bus brand 2013 | one continuous Vysoké Mýto production site with changing company/brand ownership |
| **SORA Libchavy** | SOR | company founded 1991; own bus development starts 1992; first prototype 1993; later broad domestic/export bus production | active-map Libchavy bus manufacturer from its real era |
| **CZ LOKA** | CZ LOKO lineage | Czech Třebová rail workshops from 1849; diesel-electric repair capability from 1966; electric locomotive repair from 1988; modernized vehicles from early 2000s; own diesel-electric locomotive design thereafter | workshop/rebuild capability predates own-new-build capability |
| **Daimlar / Benc / Mercator-Benz** | Daimler/Benz/Mercedes-Benz | off-map German road-vehicle lineage; first commercial motor vehicles in the 1890s; later broad truck/bus production | macro off-map manufacturer(s) + importers |
| **MANN / Büsink** | MAN/Büssing | off-map German commercial-vehicle lineage | macro off-map manufacturer/importer network |
| **Símens Mobility** | Siemens | off-map electrical/rail manufacturer; modern locomotive families as authored | macro off-map rail manufacturer |
| **Bombardír Transportation** | Bombardier/ADtranz/Alstom lineage | modern international locomotive/rolling-stock production; TRAXX-era supply | macro off-map rail manufacturer |
| **PESKA Bydgoszcz** | PESA | modern Polish rail manufacturer | off-map Poland unless final map covers source plant |
| **Soláris Bus** | Solaris | modern Polish bus manufacturer; Urbino family from 1999 | off-map Poland |
| **Ikarusz** | Ikarus | Hungarian bus production with major export presence in the later socialist era | off-map Hungary |
| **Alstrom Ferroviaria** | Fiat Ferroviaria/Alstom | modern high-speed/tilting rolling stock | off-map Italy/France |
| **Städler Rail** | Stadler | modern regional/mainline rolling stock | off-map Switzerland/other plants |

### 2.1 Capability-state data

For each manufacturer/model combination author dated state changes:

```text
series_production
low_rate_special_order
parts_and_overhaul_only
external_specialist_support_only
used_market_only
```

A model does not need to pass through every state.

The state changes control **new-build offers**, not whether existing vehicles may operate.

## 3. Factory scale and production-slot defaults

Factories need finite capacity without becoming a factory-management game for the player.

Use these authoring scale classes:

| Factory class | Typical content | Simultaneous production-slot guidance | Batch behaviour |
|---|---|---:|---|
| **Craft / bodybuilder** | 1900 coachbuilder, specialist wagon/body shop | 1–3 | individual units or tiny batches |
| **Small industrial** | early road vehicles, specialist wagons, small railcars | 2–6 | short batches |
| **Medium serial** | mature bus/truck plant, wagon works | 6–16 | parallel batches |
| **Heavy rail** | locomotives, EMU/DMU, major coach works | 4–12 heavy slots | long overlapping builds |
| **Large serial road** | mature mass-produced buses/trucks | 12–40 | larger repeating batches |
| **Macro off-map** | large external manufacturer outside detailed world | aggregate equivalent capacity | no fake infinite stock; capacity remains finite at macro level |

One production slot does not mean one generic vehicle/day. Every model defines a **factory-work requirement**.

### 3.1 Initial production-time bands

These are game-time balancing defaults for a factory already capable of the model, excluding queue/backlog and delivery.

| Vehicle | Mature series-production build time | Special/low-rate build |
|---|---:|---:|
| Horse-drawn road vehicle/body | 4–10 game days | 8–18 days |
| Early 1900 motor road vehicle | 12–28 days | 20–42 days |
| Mature rigid truck/tractor | 5–12 days | 10–24 days |
| Bus/coach | 7–16 days | 14–30 days |
| Simple 2-axle freight wagon | 4–9 days | 8–18 days |
| Bogie/special freight wagon | 8–18 days | 14–32 days |
| Passenger coach | 10–24 days | 18–40 days |
| Small railcar | 18–35 days | 30–56 days |
| Mainline steam locomotive | 28–56 days | 42–84 days |
| Diesel/electric locomotive | 35–70 days | 56–98 days |
| 2–3 car multiple unit | 42–84 days | 70–126 days |
| Large fixed high-speed trainset | 84–168 days | not ordinary special-order unless authored |

These times intentionally use the game's 14-day months/168-day year. They are not converted Gregorian manufacturing records.

Actual completion time is:

> earliest free compatible slot  
> + factory work  
> + material/input delays  
> + ordered configuration work  
> + certification/pre-delivery work  
> + delivery/import time

### 3.2 Batch learning/scale

For repeated identical units in one contract, allow modest manufacturing efficiency from common setup and purchasing.

Default authoring ceiling:

- units 1–2: 100% nominal factory work each;
- units 3–10: down to ~95% each;
- units 11–30: down to ~90% each;
- larger standardized series: floor around ~85% each unless a model/factory specifically justifies stronger mass-production economics.

This is **factory-work reduction**, not an automatic equal retail discount. Materials, delivery, dealer margin and scarce capacity still cost money.

## 4. Regional market-strength model

Use explicit market-presence tiers rather than binary availability.

| Tier | Meaning | Dealer-stock weight | Quote friction | Parts/support baseline | Used-market prevalence |
|---|---|---:|---|---|---|
| **Home** | domestic/core production market | 1.00 | lowest | strongest | high once fleet matures |
| **Core export** | established ordinary export market | 0.65 | low | strong-medium | medium-high |
| **Secondary export** | known but less common market | 0.30 | medium | medium-low | medium |
| **Rare import** | unusual/special-order market | 0.08 | high | weak | low |
| **No ordinary presence** | no dealer network; direct quote may still be possible | 0.00 dealer seeding | highest | external/specialist only | near-zero local stock |

These values are **relative seeding/order weights**, not probabilities shown to the player.

Trade law, war, sanctions, approval and transport-route state are applied separately.

### 4.1 Initial regional profiles

Use these as starting authoring directions:

- Czech/Bohemian domestic brands: **Home** in Czech lands; normally **Core export** or **Secondary export** in nearby Central/Eastern European markets according to era/model.
- Austrian/German manufacturers: normally at least **Core export** into Czech lands when historical trade conditions permit; early 1900 specialist motor vehicles can still be **Secondary/Rare** because the market itself is immature.
- Hungarian Ikarusz in the 1970s–1980s: **Core export** across the socialist Central/Eastern European market.
- Western premium/import models during restricted-trade eras: dealer tier may fall to **Rare import/No ordinary presence** while the model remains historically known.
- Solaris/PESA in the modern Czech/Polish market: generally **Core export** where actual regional sales justify it.
- modern pan-European locomotive platforms such as Vectron/TRAXX: **Core export** in compatible European markets after approval.

## 5. Parts and service-support families

Do not create a unique workshop skill for every model. Group support where the same physical skills/equipment realistically overlap.

### 5.1 Rail support families

| ID | Capability family | Typical vehicles |
|---|---|---|
| **rail_steam_light** | small/medium steam, basic boiler/running gear | ČMS 97/99 and similar |
| **rail_steam_mainline** | tender locomotives, larger boilers, valve gear | ČMS 170, N534, N387 |
| **rail_steam_heavy_modern** | large late steam, high-output auxiliaries | N475/N498/N556 |
| **rail_diesel_mechanical_light** | early/light railcars | M120, M131 |
| **rail_diesel_hydraulic_mechanical_regional** | mid-century motor cars | M240/M262 and relevant trailers |
| **rail_diesel_electric_ckd** | ČKD-style diesel-electric families | Hektor, Čmelda, Barda, Brýlovec, Kocour |
| **rail_electric_skoda_legacy_dc** | early DC electrics | Bobina, Šestikolo |
| **rail_electric_skoda_legacy_ac** | early AC electrics | Laminát |
| **rail_electric_skoda_dual_modern** | modern dual/multisystem Škoda | Eso, Pershing, 109X by package |
| **rail_electric_pan_european_modern** | modular modern EU locomotives | TRAXX, Vektron |
| **rail_dmu_modern** | electronically controlled modern DMU | 842, 844, 847 |
| **rail_emu_modern** | modern EMU traction/HVAC/control | 471, Panter |
| **rail_high_speed_trainset** | integrated high-speed/tilting sets | 680 |
| **rail_coach_wood_legacy** | wooden/early steel coaches | L2, early B4 |
| **rail_coach_mainline_legacy** | conventional bogie coaches | B4/Y64 |
| **rail_coach_modern** | high-speed HVAC/electrical coaches | Z80, Comfort 9 |
| **rail_wagon_basic** | open/covered/flat conventional wagons | O10/G10/P12/R20 |
| **rail_wagon_special** | tank/refrigerated/heavy-load | Z10/I8/H15 and successors |
| **rail_wagon_modern_bogie** | modern hopper/tank/intermodal | F50/Z55/R55/S60/S70/F68 |

A workshop can hold several capability families.

### 5.2 Road support families

| ID | Capability family | Typical vehicles |
|---|---|---|
| **road_horse_vehicle** | wagon/body, harness/stable support | H2/H4/horse omnibus |
| **road_early_petrol** | primitive ignition/carburetion/solid-tyre era | Daimlar/Benc/L&K early vehicles |
| **road_early_steam** | steam road vehicle boiler/drive | Thornycroft-type |
| **road_cz_medium_legacy** | Praga/light-medium domestic trucks | Pragov N/RN, related buses |
| **road_cz_heavy_aircooled** | Tatra heavy air-cooled truck families | Fatra 111/138/148/815 |
| **road_cz_v3s_family** | V3S/S5T-type service ecosystem | Pragov V3S |
| **road_cz_liaz_legacy** | 706/LIAZ road truck ecosystem | 706 RT/VIAZ 100 |
| **road_cz_avio_light** | Avia medium/light truck ecosystem | Aviat A30 |
| **road_bus_karosa_legacy** | 706 RTO/Š-series/700/900 body + domestic driveline | Karusa families |
| **road_bus_ikarus_legacy** | Ikarus articulated/standard buses | Ikarusz 280 |
| **road_eu_heavy_modern** | modern EU diesel tractor electronics/diagnostics | Actros/TGX |
| **road_tatra_modern** | modern Phoenix/Force-style heavy truck | Fatra Fénix |
| **road_bus_eu_modern** | modern CAN-bus diesel/HVO bus | Crossway/Lion City/Solaris |
| **road_ev_bus** | HV battery/e-drive/charging | SORA NS12E, electric Crossway |
| **road_ev_heavy** | high-voltage heavy truck | eActros-class |
| **road_modern_van** | modern light commercial van | TGE-class |

## 6. Maintenance interval authoring defaults

Maintenance uses both planned targets and hard limits under GAME_DESIGN Section 15.4.

Do not model dozens of individual components. Author 3–5 interval types per vehicle family.

### 6.1 Steam rail

Typical event set:

- **service/preparation**: every operating day or duty cycle — coal/water/ash/lubrication/inspection;
- **light examination**: 1,500–3,000 km or 1 game month;
- **workshop examination**: 8,000–15,000 km or 3–6 game months;
- **heavy overhaul**: 60,000–120,000 km or 2–4 game years;
- **boiler/legal inspection**: separate hard calendar interval.

Later/high-output steam normally has higher workshop complexity even if its mileage interval is similar.

### 6.2 Diesel/electric rail

Legacy diesel:

- routine check: 2,000–5,000 km;
- scheduled service: 12,000–25,000 km;
- major examination: 80,000–160,000 km;
- heavy engine/traction overhaul: 400,000–800,000 km or multi-year calendar interval.

Modern diesel/electric:

- routine inspection: 5,000–10,000 km;
- scheduled service: 25,000–50,000 km;
- major examination: 150,000–300,000 km;
- heavy overhaul: 800,000–1,500,000 km depending model/support package.

EMU/DMU/trainsets may use shorter workshop visits but more specialist diagnostic capability.

### 6.3 Conventional coaches/wagons

- running/safety inspection: 5,000–15,000 km or monthly;
- scheduled workshop service: 30,000–80,000 km;
- bogie/brake heavy work: 150,000–400,000 km;
- major body/structural examination: multi-year hard calendar interval.

Special tank/refrigerated/hazard wagons add equipment-specific inspections.

### 6.4 Road vehicles

Early motor vehicle:

- daily/basic attention is significant;
- light service: 500–1,500 km;
- workshop service: 3,000–8,000 km;
- major overhaul: 20,000–50,000 km.

Mid-century truck/bus:

- light service: 2,500–5,000 km;
- scheduled service: 8,000–15,000 km;
- major service: 40,000–80,000 km;
- engine/driveline overhaul: 150,000–300,000 km.

Modern diesel road:

- scheduled service: 20,000–50,000 km depending duty;
- major scheduled work: 100,000–250,000 km;
- heavy drivetrain work: condition/usage based, commonly several hundred thousand km.

Battery-electric road:

- fewer combustion-service tasks;
- separate HV/e-drive/cooling inspections;
- battery condition is tracked as a high-value subsystem;
- tyre/brake/suspension/body wear still follows real duty.

These are starting balancing bands. Model-specific data may override them when sourced/needed.

## 7. Support decline and parts availability

Parts/support is not a calendar penalty applied directly to the vehicle.

Each support family has regional **provider count/capability** and parts-source state.

Suggested support states:

| State | Gameplay meaning |
|---|---|
| **Mass support** | many compatible workshops, ordinary stocked parts |
| **Normal support** | several providers, short procurement |
| **Specialist support** | few providers, booking/travel delay, some made-to-order parts |
| **Heritage support** | very few specialists, long lead time, fabrication/rebuild common |
| **Owner-supported only** | no ordinary external offer; player may continue with own retained capability/stock |
| **No current support** | vehicle can remain stored/sold but cannot complete required work until capability is restored |

Support can improve again if:

- a specialist starts offering service;
- the player develops own compatible workshop/skills;
- a successor produces replacement parts;
- a sufficiently large fleet/order creates an economic reason for a provider to enter the market.

## 8. New-vehicle offer and dealer-stock defaults

### 8.1 Factory quotes

A current series-production model normally has:

- **Home market:** direct factory quote always discoverable; dealer alternatives common;
- **Core export:** factory/importer quote discoverable; dealers often available;
- **Secondary export:** quote available through importer/broker or direct request;
- **Rare import:** quote may need active request and destination adaptation;
- **No ordinary presence:** direct request can still succeed if manufacturer is willing/legal/logistically able to export.

### 8.2 Dealer stock target

Dealer inventory should cover urgency, not replace manufacturer ordering.

Suggested normal stock policy by dealer size:

| Dealer | Typical total new vehicles in stock | Unusual/specialist share |
|---|---:|---:|
| small local road dealer | 2–6 | usually 0 |
| regional road dealer | 6–18 | 0–2 |
| large/import road dealer | 15–40 | 1–5 |
| rail distributor/sales yard | 0–4 locomotives/railcars + 4–20 wagons/coaches | model-dependent |
| specialist heavy/special dealer | 0–3 | most stock is itself specialist |

Dealer stock is an actual physical inventory generated from past dealer orders.

A common configuration may sit in stock. A player-defined unusual template normally requires a factory order/retrofit.

## 9. 1900 opening-market seed

The opening world must already contain a credible vehicle ecosystem.

### 9.1 Factory state

At 1900 initialization:

- **ČMS/Ringhauer-type domestic rail works** have active steam/wagon/coach capabilities appropriate to the date;
- **Neškoda Plzeň does not yet build complete locomotives**; it can exist as a major heavy industrial works with locomotive-component capability, gaining complete-locomotive capability in 1920;
- **Studena Vagónka** is only just founded in December 1900 and should not be treated as a mature starting supplier at the first day of a January-like 1900 start unless the authored game date is after its foundation;
- **Lorin & Klement** exists as an emerging motor-vehicle company but the authored Type E utility family does not appear before its fixed historical introduction;
- **Fatra/Kopřivnice** has real wagon/early motor/truck capability;
- German/Austrian/British early motor and steam-road manufacturers are available as off-map suppliers where trade/logistics permit.

### 9.2 Used rail seed per active starting market

For a normal rail-capable starting region, target discoverable physical used listings across the wider reachable market:

- 2–5 light/yard/local steam locomotives;
- 1–3 mixed/general locomotives;
- 1–2 passenger/express-capable locomotives;
- 12–30 ordinary freight wagons across basic bodies;
- 3–8 specialist freight wagons;
- 4–12 passenger/service coaches.

These are **market-level ranges**, not guaranteed units in the player's city.

At least one reasonable rail opening path should exist through used stock or a valid factory order.

### 9.3 Used/new road seed per active starting market

Target:

- 4–12 horse freight vehicles available through local builders/dealers/used owners;
- 2–6 horse omnibuses/passenger bodies across municipalities/private operators;
- 0–3 immediately purchasable early motor freight vehicles;
- 0–2 immediately purchasable motor omnibuses;
- additional early motor vehicles available by off-map factory/import order.

The deliberately low motor stock makes early motorization feel pioneering without making it impossible.

### 9.4 Initial condition distribution

Used seed should not all be junk or perfect museum pieces.

Default condition mix:

- Excellent: 10%;
- Good: 45%;
- Worn: 35%;
- Overhaul due: 10%.

Adjust by owner type/model age.

A railway actively selling a recently displaced but maintained locomotive can produce a good/excellent listing; industrial disposal after years of hard service is more likely worn.

## 10. Used-market listing behaviour

An owner considers sale when a physical vehicle is:

- surplus after service reduction;
- displaced by fleet modernization;
- too expensive for the owner's support network;
- incompatible with future route/infrastructure plans;
- repossessed/liquidated;
- deliberately traded in;
- stored beyond the owner's economic retention threshold.

Do not manufacture listings just because the player opens the marketplace.

### 10.1 Asking-price components

Used asking price derives from:

- replacement/new-build value of the model/nearest equivalent;
- individual condition;
- remaining hard-inspection margin;
- template/equipment value;
- local demand;
- support availability;
- scarcity/collectability only where economically relevant;
- seller urgency;
- delivery responsibility.

Age by itself is not a fixed depreciation curve.

A very old but freshly overhauled specialist asset can be worth more than a newer worn one.

## 11. Cost-index defaults before explicit `money` balancing

Until the global economy supplies explicit prices, use relative cost indices to catch roster mistakes.

### 11.1 New-build platform index by role

| Role | Normal same-era platform range |
|---|---:|
| horse road vehicle | 35–60 |
| early motor road vehicle | 100–180 |
| mature light commercial | 60–100 |
| medium rigid truck | 80–120 |
| heavy rigid/tractor | 100–150 |
| specialist heavy/terrain truck | 130–190 |
| ordinary bus | 90–130 |
| premium/intercity coach | 120–180 |
| battery-electric bus/truck | 150–220 |
| basic freight wagon | 35–60 |
| specialist freight wagon | 60–110 |
| ordinary passenger coach | 70–110 |
| premium/sleeper/service coach | 100–160 |
| light railcar | 90–140 |
| conventional steam locomotive | 90–150 |
| premium/heavy steam locomotive | 140–190 |
| legacy diesel/electric locomotive | 120–180 |
| modern universal locomotive | 180–240 |
| regional DMU/EMU | 180–280 |
| high-speed fixed trainset | 450+ |

Equipment/template packages modify this base transparently.

### 11.2 Import cost components

Import does not use a generic percentage surcharge.

Quote calculation keeps separate:

- factory configured price;
- importer/dealer margin if used;
- origin collection;
- long-distance transport;
- transshipment/handling;
- customs/duties/fees;
- destination adaptation;
- first-type approval where needed;
- final delivery.

This is especially important in 1900, where transport and handling can make a distant early motor vehicle dramatically more expensive than its factory price.

## 12. Equipment-template data defaults

Each model family declares:

- fixed physical platform;
- factory variant(s);
- equipment groups;
- option dependencies/exclusions;
- configuration mass;
- passenger/cargo capacity consequences;
- cost/material/work requirements;
- maintenance/support requirements;
- certification impact.

### 12.1 Passenger capacity packages

Use explicit floor/space accounting rather than an arbitrary comfort multiplier.

A package can exchange:

- seat count;
- seat pitch/space;
- class/service area;
- luggage/bike/wheelchair space;
- toilet/catering area;
- standing area where legal;
- crew/service area.

A `Business` template should therefore cost capacity/space and equipment money rather than simply adding a fare bonus.

### 12.2 Neo/refurbishment packages

A `Neo` template means a real authored modernization package that can include:

- refreshed seats/interior;
- better lighting;
- HVAC where physically possible;
- electrical outlets/information equipment in later eras;
- accessibility improvements within platform limits;
- updated brakes/control/safety equipment where supported.

It does not reset structural age or transform the body shell.

## 13. Production-input groups

Vehicle production should use existing economy commodities where possible rather than inventing one "vehicle parts" resource for everything.

Suggested aggregate bill-of-material groups:

### Rail locomotive / multiple unit
- steel/metal products;
- machinery/components;
- wheelsets/bogies;
- traction/engine equipment;
- electrical equipment where relevant;
- glass/interior materials;
- rubber/plastics in later eras;
- electronics in later eras.

### Coaches/wagons
- steel/metal products;
- timber in earlier construction;
- wheelsets/bogies;
- brake/coupler equipment;
- interior materials for passenger stock;
- insulation/cooling machinery for refrigerated stock.

### Road vehicle
- steel/metal products;
- engine/drivetrain/machinery;
- tyres/rubber;
- glass;
- body/interior materials;
- electrical/electronic equipment by era;
- battery pack for modern BEV.

Do not require every nut/bolt as a commodity.

## 14. Research/provenance anchors

Important factory-history anchors used for the current content timeline:

- Škoda Group history — complete locomotive production in Plzeň from 1920; interwar export and locomotive development: https://www.skodagroup.com/cs/stranka/historie
- Škoda Vagonka history — Studénka company founded 12 December 1900; passenger rolling-stock production later moved to Ostrava; Škoda Group from 2005: https://www.skodagroup.com/cs/stranka/historie-skoda-vagonka
- Tatra company profile/history — wagon production from 1881, first car 1897, first truck 1898, documented heavy-truck milestones: https://www.tatra.cz/o-spolecnosti/
- Praga company history — RN 1933–1953, V3S 1953–1990 and broad export/use history: https://pragaglobal.com/praga-history/
- Vysoké Mýto / Karosa / Iveco lineage — Sodomka 1895, first bus 1928, Karosa 1948, 700 series 1981, Renault/Irisbus/Iveco transitions: https://www.ivecogroup.com/media/brand_press_releases/2025/EMEA-%28English%29/Iveco-Bus/iveco_bus_celebrates_the_130th_anniversary_of_the_vysoke_myto_plant_in_the_year_when_iveco_turns_50_20250603T075023T059_1nnrakmuat453kfrwrvgdm5q
- SOR company history — founded 1991, own bus development from 1992, first prototype 1993: https://www.sor.cz/spolecnost/o-nas/
- CZ LOKO history — rail workshops 1849, diesel-electric repair 1966, electric repair 1988, own modernized/new locomotive milestones: https://www.czloko.cz/vyvoj-czloko-v-historickych-datech.htm
- LIAZ 100-series production start and representative technical/economic data: https://www.automobilrevue.cz/rubriky/clanky/historie/liaz-liberecke-automobilove-zavody-byl-jednou_44696.html
- Laurin & Klement Type E commercial/omnibus specifications and 1908 production: https://www.skoda-storyboard.com/cs/tiskove-zpravy-archiv/pribehy-mene-znamych-modelu-z-historie-125-let-skoda-auto-laurin-klement-e-cerna-hora/
- Solaris history — Urbino family world premiere and first customer deliveries in 1999: https://www.solarisbus.com/en/about-us/history
- Siemens Vectron platform/approval/power examples: https://press.siemens.com/global/en/feature/vectron-vehicle-concept

## 15. Machine-readable authoring output

The eventual data layer should split records instead of storing one giant vehicle object.

Recommended manifests:

```text
manufacturers
factories
factory_capabilities
vehicle_model_families
vehicle_factory_variants
equipment_options
vehicle_templates_builtin
retrofit_paths
support_families
workshop_capabilities
parts_sources
regional_market_profiles
type_approvals
dealer_profiles
vehicle_offers
physical_vehicle_instances
historical_trade_rules
```

Stable IDs survive localization, corporate rename and save/load.

## 16. Completion criteria for authored vehicle data

A vehicle family is **content-data complete** only when it has:

- sourced prototype/inspiration record;
- fixed introduction date;
- physical platform dimensions/mass/route constraints;
- representative traction/power/capacity values;
- factory/source capability;
- factory variant(s);
- supported equipment options;
- production input/work requirement;
- production-capability lifecycle;
- regional-market profile;
- support family;
- maintenance intervals/hard inspections;
- operating-consumption curve/bands;
- retrofit paths where applicable;
- approval/import metadata;
- new/dealer/used offer behaviour;
- explicit `money` price after economy balancing.

Art/prefab/sound/test completeness remains separate and is still required before the row counts as delivered V1 content.
