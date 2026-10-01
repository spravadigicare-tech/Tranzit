# Tranzit — Historical vehicle catalogue and production plan

> **Status:** researched content specification for the base game from the 1900 start onward.
>
> This document extends the vehicle-content target in [V1_CONTENT_MANIFEST.md](V1_CONTENT_MANIFEST.md) and obeys the lifecycle rules in [GAME_DESIGN.md](GAME_DESIGN.md), especially Section 15. Vehicle names and manufacturers are fictionalized; the technical and historical inspiration is real.
>
> The catalogue is deliberately broader than the minimum V1 opening set. It is a content plan, not implementation evidence: meshes, machine-readable definitions, factories, offers, sounds, balancing, tests and save support still have to be authored.

## 1. Non-negotiable catalogue rules

1. **No vehicle appears from a menu.** Every physical unit is either manufactured by a real simulated factory/company, already exists as a seeded/used physical asset, sits in finite dealer stock, or enters the active world through a defined off-map import point.
2. **Introduction is not expiry.** A model has an introduction date, never a hard `available_until`. Old vehicles stay searchable and usable while technically serviceable. New-build offers can disappear naturally when the manufacturer stops ordinary production, but used vehicles and special-order capability can survive.
3. **Historical choice, not a single obvious upgrade.** In every broad era the player should normally have at least:
   - a cheap/light option;
   - a balanced general-purpose option;
   - a high-capacity/high-performance or specialist option;
   - used older equipment as a cash-saving alternative where real stock exists.
4. **Factories are economic actors.** Active-map factories consume inputs, workforce and production capacity. Their backlog and material supply affect delivery time.
5. **Off-map factories are still physical sources.** They are represented by macro production capacity outside the detailed map. Completed vehicles enter at a valid rail/road border or import terminal and then continue physically to the buyer.
6. **Specifications are transparent.** Performance is not a hidden "era bonus". Power, tractive effort, mass, capacity, axle load, route compatibility, consumption, maintenance and crew requirements create the gameplay differences.
7. **Prototype values are rounded game-authoring targets.** Exact production batches varied. Where a family covers several real subtypes, the game uses a representative value and records the real prototype/source in the content data.
8. **The map begins in 1900 but the world does not.** Period-appropriate older vehicles already exist in 1900 as used stock. Their manufacture date, condition and owner are seeded rather than replaying pre-1900 production.

## 2. Fictional manufacturer lineages

The names should feel recognisable enough to be a historical wink without using the real marque unchanged.

| Fictional company | Real-world inspiration | Main plant / source in game | Default source logic |
|---|---|---|---|
| **ČMS Praha — Českomoravská strojírna** | BMMF / ČKD lineage | Praha | Active-map rail factory if Praha is active; later evolves into ČMD |
| **ČMD Praha — Českomoravská dopravní** | ČKD | Praha | Active-map locomotive/vehicle factory |
| **Neškoda Plzeň** | Škoda Works / Škoda Transportation | Plzeň | Active-map heavy-industry and rail factory |
| **Ringhauer Smíchov** | Ringhoffer | Praha-Smíchov | Active-map coach/wagon factory; later can merge/rebrand |
| **Lorin & Klement** | Laurin & Klement | Mladá Boleslav | Active-map early road vehicle factory |
| **Fatra Kopřivnice** | Tatra | Kopřivnice | Active-map road vehicle factory |
| **Pragov Praha** | Praga | Praha | Active-map trucks/buses/light commercial vehicles |
| **VIAZ** | LIAZ | Liberec / Mnichovo Hradiště lineage | Active-map road factory where region is active |
| **Karusa Vysoké Mýto** | Karosa | Vysoké Mýto | Active-map bus factory |
| **SORA Libchavy** | SOR | Libchavy | Active-map bus factory |
| **Studena Vagónka** | Vagonka Studénka | Studénka | Active-map railcar/EMU factory |
| **CZ LOKA** | CZ LOKO | Česká Třebová / Jihlava lineage | Active-map modern locomotive works / rebuild specialist |
| **Daimlar Motoren** | Daimler | off-map Germany unless the final clipping includes the plant | Import |
| **Benc & Cie.** | Benz | off-map Germany | Import |
| **Büsink** | Büssing | off-map Germany | Import |
| **MANN** | MAN | off-map Germany | Import |
| **Mercator-Benz** | Mercedes-Benz | off-map Germany | Import |
| **Símens Mobility** | Siemens Mobility | off-map Germany | Import |
| **PESKA Bydgoszcz** | PESA | off-map Poland unless the final clipping reaches the plant | Import |
| **Alstrom Ferroviaria** | Alstom / Fiat Ferroviaria | off-map Italy/France | Import |
| **Ivego Bus** | Iveco Bus | off-map / licensed local body production where historically justified | Import or local assembly offer |
| **Städler Rail** | Stadler Rail | off-map Switzerland/Poland | Import |

A corporate merger or ownership change must not delete old physical vehicles or their original manufacturer identity.

## 3. Rail traction catalogue

### 3.1 Steam, diesel and electric locomotives

| ID / fictional model | Intro | Real prototype basis | Primary role | Power / starting TE | Max speed | Service mass | Key route limits | Production/source |
|---|---:|---|---|---:|---:|---:|---|---|
| **ČMS 97 “Mravenec”** | 1878 | kkStB 97 / later ČSD 310.0 | yard, industrial, tiny local trains | 230 kW / ~45 kN | 40 km/h | 29 t | 3 coupled axles, ~9.7 t/axle, 90 m curves | Praha factory or seeded used stock in 1900 |
| **ČMS 99 “Lokálka”** | 1897 | kkStB 99 / ČSD 320.0 | local mixed traffic | ~300 kW / ~70 kN | 50 km/h | 39 t | light branch-line locomotive; low coal/water endurance | Praha factory; used stock common in 1900 |
| **ČMS 170 “Horal”** | 1897 | kkStB 170 / ČSD 434.0 | heavy freight, gradients | ~900 kW / ~125 kN | 60 km/h | 69 t loco + tender | ~14 t axle load; tender requires turning/run-around planning | multiple Austro-Hungarian plants; Praha build or regional import |
| **ČMS 6 “Rychlík”** | 1894 | kkStB 6 / contemporary express 2'B engines | passenger / express | ~700 kW / ~70 kN | 80 km/h | ~55 t + tender | less adhesion than freight engines; needs better track | active-map or Austrian off-map supply |
| **Neškoda N387 “Mikádo”** | 1926 | ČSD 387.0 | premier express | 1,546 kW / 109 kN | 110 km/h | 92.8 t loco | 150 m curves, high coal/water use, good track required | **Plzeň factory**, active-map manufacture |
| **Neškoda N475 “Šlechtična”** | 1947 | ČSD 475.1 | universal passenger / fast mixed | 1,480 kW / ~150 kN | 100 km/h | 102.7 t loco | 150 m curves; stronger track and depot facilities | **Plzeň factory** |
| **Neškoda N556 “Silák”** | 1951 | ČSD 556.0 | maximum steam freight | 1,620 kW / 218 kN | 80 km/h | 99 t loco, ~185 t with tender | 16.8 t axle load; large turntable/service demand | **Plzeň factory** |
| **Neškoda N498 “Albatros”** | 1954 | ČSD 498.1 | top steam express | 2,000 kW / ~180 kN | 120 km/h | 113 t loco | premium track; expensive coal/water/service | **Plzeň factory** |
| **Neškoda E500 “Bobina”** | 1953 | ČSD E 499.0 / class 140 | early mainline DC electric | 2,032 kW cont. / 212 kN | 120 km/h | 80–82 t | 3 kV DC only, ~20 t axle load | **Plzeň factory** |
| **ČMD D435 “Hektor”** | 1958 | ČSD T 435.0 / class 720 | shunting, local freight | 553 kW / 200 kN start | 60 km/h | 61 t | no train heating in base build; excellent 70 m curve access | **Praha factory** |
| **Neškoda E670 “Šestikolo”** | 1961 | ČSD E 669.1 / class 181 | heavy electric freight | ~2,790 kW / ~340 kN | 90 km/h | ~124 t | 3 kV DC, six axles, high track load but huge adhesion | **Plzeň factory** |
| **ČMD D478 “Barda”** | 1964 | ČSD T 478.1 / classes 749/751 | universal diesel mainline | 1,103 kW / 215 kN | 100 km/h | 75 t | diesel; passenger-heating capability depends on version | **Praha factory** |
| **ČMD D753 “Brýlovec”** | 1970 | ČSD T 478.3 / class 753 | mainline diesel freight/passenger | ~1,325 kW / ~215 kN | 100 km/h | ~74 t | 4 axles, diesel; later retrofit families possible | **Praha factory** |
| **Neškoda ES500 “Eso”** | 1980 | ČSD ES 499.1 / class 363 | dual-system universal electric | 3,480 kW DC / 3,060 kW AC | 120 km/h | 87 t | 3 kV DC + 25 kV 50 Hz; ~21.8 t axle load | **Plzeň factory** |
| **Neškoda E162 “Pershing”** | 1984 | classes 162/163 | fast single-system electric | 3,480 kW / ~285 kN | 140 km/h | ~85 t | cheaper than multisystem; route-limited by voltage | **Plzeň factory** |
| **Neškoda 109X “Zátopek”** | 2008 | Škoda 109E / class 380 | premium multisystem express | 6,400 kW / 275 kN | 200 km/h | 88 t | 3 kV DC + 25 kV AC + 15 kV AC; modern signalling/approval | **Plzeň factory** |
| **Símens Vektron MS** | 2010 | Siemens Vectron MS | universal international electric | 6,400 kW / ~300 kN | 200 km/h | ~90 t | multi-system configuration; country packages/ETCS matter | off-map German manufacture → rail import |
| **CZ LOKA EffiShunter 1000** | 2017 | CZ LOKO EffiShunter 1000 | modern shunting/local freight | ~900–970 kW / up to ~340 kN | 100 km/h | ~80–92 t by version | diesel-electric/AC traction; efficient low-speed work | active-map modern works / finite factory capacity |

### 3.2 Why this remains a choice rather than a linear upgrade

- A 1958 Hektor does not make the 1900 Mravenec vanish; it is simply faster to start, easier to fuel and much more capable, while an old steam tank engine can still be cheaper on a tiny industrial siding with existing steam support.
- Electric locomotives are powerful but only useful where the correct electrification exists.
- A multisystem locomotive saves locomotive changes but costs substantially more to buy, finance and maintain.
- Six-axle freight traction gains adhesion but can lose route access on lightly built lines.
- Modern locomotives have better availability and energy use, but old equipment remains viable where the player's own workshop has the skills/parts.

## 4. Passenger rail vehicles and coaches

| ID / fictional model | Intro | Real basis | Type | Capacity | Max speed | Power / mass | Gameplay distinction | Production/source |
|---|---:|---|---|---:|---:|---|---|---|
| **Ringhauer L2** | 1885 | Central-European 2-axle wooden local coach | coach | 40–44 seats | 50 km/h | ~10–12 t | cheap, low comfort, short platforms, slow train limit | Smíchov factory / used stock |
| **Ringhauer B4 Corridor** | 1895 | 4-axle bogie corridor coach | coach | 50–58 seats | 80 km/h | ~25–30 t | smoother ride, through circulation, heavier/more expensive | Smíchov factory |
| **Ringhauer Luxus Schlaf** | 1898 | period sleeping/dining stock | sleeper/service | 18–24 berths or 28 dining seats | 80 km/h | ~28–32 t | premium fares, service staff/supplies, low capacity | Smíchov or off-map luxury-car builder |
| **Ringhauer Post/Gepäck** | 1885 | baggage/post/service coach | service | baggage/mail volume instead of seats | 65 km/h | ~14 t | luggage/mail/guards; no ordinary passenger capacity | Smíchov factory |
| **ČMS M120 “Věžák”** | 1930 | ČSD M 120.4 | petrol railcar | ~32 seats | ~55 km/h | ~90 kW / ~12 t | very cheap branch-line train, no locomotive/run-around | Praha factory |
| **Studena M131 “Hurvínek”** | 1948 | ČSD M 131.1 | diesel railcar | ~48 seats | 60 km/h | ~114 kW / ~16 t | branch-line economy, can work with trailers | Studénka factory |
| **Studena M262 “Kredenc”** | 1949 | ČSD M 262.0 | diesel railcar | ~56 seats | 90 km/h | ~300 kW / ~43 t | faster regional service, more comfort/cost | Studénka factory |
| **Ringhauer Y64** | 1964 | UIC-Y family | bogie coach | 72–88 seats by class | 140 km/h | ~38–42 t | standardized mainline coach, steam/electric heating variants | domestic works or regional licence build |
| **Studena M152 “Orchestrion”** | 1975 | ČSD M 152.0 / class 810 | diesel railcar | 55 seated + 40 standing | 80 km/h | 155 kW / 20 t | tiny lines, very low axle load/cost, modest acceleration/comfort | Studénka factory |
| **Ringhauer Z80** | 1980 | UIC-Z / Bmz-type coach | fast coach | ~60–80 seats | 160 km/h | ~42–48 t | faster, air-conditioned variants, higher comfort and electrical demand | domestic / off-map licensed builds |
| **Alstrom 680 “Nakláněč”** | 2003 | ČD class 680 Pendolino | 7-car EMU | 331 seats | 200 km/h | 3,920 kW / 385 t | tilting, multisystem, expensive dedicated fixed consist | off-map Italy → rail import |
| **PESKA 844 “RegioRys”** | 2011 | PESA Link II / class 844 | 2-car DMU | 120 seated + ~120 standing | 120 km/h | 2×390 kW / 84.4 t | low-entry regional diesel, 1st-class zone, bikes/WC | off-map Poland → rail import |
| **Neškoda 640 “Panter”** | 2012 | RegioPanter | 3-car EMU | 234 seated | 160 km/h | 2,040 kW / ~151–152 t | fast acceleration, low-floor regional electric, dual-voltage | Plzeň/Studénka active-map manufacture |
| **PESKA 847 “RegioLiška”** | 2023 | RegioFox / class 847 | 2-car DMU | 115 seated | 120 km/h | ~750 kW / ~83 t | modern non-electrified regional service, low-entry, HVO-compatible family | off-map Poland import |
| **Neškoda Comfort 9** | 2025 | ComfortJet / Siemens Viaggio platform | 9-car non-traction push-pull set | 555 seats, incl. 99 first class + 18 restaurant seats | 230 km/h design | ~237 m full set | very high comfort/capacity; needs compatible high-speed locomotive and long platforms | Siemens–Škoda production chain; individual coaches are physically delivered |

The player can still build locomotive-hauled trains from individual coaches. Fixed trainsets trade flexibility for quicker turnarounds, high acceleration and integrated amenities.

## 5. Freight rolling stock

These are physical wagons, not abstract cargo-capacity tokens. The exact 1900 designs vary by railway, so the game uses representative Central-European families tied to real period construction practice.

| ID | Intro | Real basis | Empty mass | Payload / volume | Max speed | Cargo / handling | Source |
|---|---:|---|---:|---:|---:|---|---|
| **Ringhauer O10** | 1880 | 2-axle wooden/steel open wagon | ~8 t | 10 t / ~22 m³ | 45 km/h | coal, ore, timber, bulk | Smíchov + other regional plants |
| **Ringhauer G10** | 1880 | 2-axle covered goods wagon | ~9 t | 10 t / ~35 m³ | 55 km/h | general cargo, bagged goods | Smíchov |
| **Ringhauer P12** | 1885 | 2-axle flat/bolster wagon | ~7 t | 12 t | 50 km/h | timber, machinery, long loads | Smíchov |
| **Ringhauer Z10** | 1890 | early riveted tank wagon | ~8 t | 10 t / ~12 m³ | 45 km/h | oils/chemicals; restricted handling | specialist tank builder / dealer |
| **Ringhauer I8 “Lednice”** | 1895 | ice-insulated/refrigerated van | ~10 t | 8 t / ~28 m³ | 55 km/h | meat/dairy/perishables; consumes ice/cooling supplies | Smíchov / specialist body shop |
| **Ringhauer H15** | 1890 | heavy machinery / well wagon family | ~10 t | 15 t indivisible load | 40 km/h | machinery/transformer/large unit | specialist domestic build |
| **R20 Open** | 1930 | steel 2-axle open wagon | ~10 t | 20 t / ~35 m³ | 65 km/h | bulk; faster loading/unloading | domestic wagon works |
| **G25 Standard** | 1950 | UIC-era covered van precursor | ~12 t | 25 t / ~60 m³ | 100 km/h | general cargo/palletized later | domestic/regional plants |
| **E28 Standard** | 1955 | UIC Es-family open wagon | ~12 t | 28 t / ~36 m³ | 100 km/h | coal/scrap/stone | domestic/regional plants |
| **F50 Hopper** | 1960 | bogie self-discharging hopper | ~23 t | 50–55 t | 100 km/h | coal/ore/aggregate; rapid discharge facility | heavy wagon plant |
| **Z55 Tank** | 1960 | bogie tank wagon | ~24 t | ~55 t / 60–70 m³ | 100 km/h | fuel/chemicals; hazard compatibility | specialist plant |
| **R55 Flat** | 1965 | bogie flat/R-family | ~22 t | 55–60 t | 100 km/h | timber/steel/vehicles/machinery | heavy wagon plant |
| **S60 Container** | 1970 | early ISO container flat | ~20 t | 60 t; 40–60 ft loading positions | 100 km/h | containers only once container technology/terminals unlock | domestic/off-map build |
| **I45 Reefer** | 1970 | mechanical refrigerated wagon | ~25 t | ~45 t | 100 km/h | active refrigeration, fuel/electric support | specialist plant |
| **S70 Intermodal** | 1995 | Sgnss/Sdggmrs-family modern intermodal | ~20–35 t | 60–70 t | 120 km/h | containers/swap bodies/semitrailers by subtype | domestic or import |
| **F68 MegaHopper** | 2000 | modern high-capacity bogie hopper | ~22 t | 68 t | 120 km/h | bulk, rapid automated discharge | domestic/import |

### Freight-wagon gameplay

- Braked/unbraked and through-brake eras matter. A cheap old wagon can lower the permitted speed of the entire train.
- Ice-cooled vehicles need real ice/cold-chain supply; later mechanical reefers need fuel/energy and more maintenance.
- Container wagons do not appear before the container/terminal technology exists.
- Heavy wagons require axle-load-compatible routes and stronger loading facilities.
- A customer's private wagons are still physical assets and do not imply that the customer can operate the mainline train.

## 6. Road freight catalogue

### 6.1 1900 opening set

| ID / fictional model | Intro | Real basis | Payload | Power | Max speed | Crew | Production/source |
|---|---:|---|---:|---:|---:|---|---|
| **Městský valník H2** | pre-1900 | 2-horse urban dray | 2.0 t | animal traction | 8 km/h practical | driver | local coachbuilder + horse/stable supply |
| **Těžký povoz H4** | pre-1900 | 4-horse heavy wagon | 4.0 t | animal traction | 6 km/h practical | driver/handler | local coachbuilder |
| **Daimlar Lastwagen 5** | 1896 | Daimler Motor-Lastwagen | selectable 1.2–5.0 t; game base 3.0 t | 4.4–7.4 kW | 12 km/h | driver | off-map German import |
| **Thornycroft Steam 1T “Konvice”** | 1896 | Thornycroft steam carriage/wagon | ~1.0 t | compound steam | ~12–16 km/h | driver/fireman on heavier duty | off-map British import; rare dealer/special order |

This already gives four different 1900 freight choices without introducing an anachronistic modern truck: cheap horses, heavy horse haulage, scarce petrol trucks and a specialist steam vehicle.

### 6.2 Successor road vehicles

| ID / fictional model | Intro | Real basis | Format / payload | Power | Max speed | Best use | Production/source |
|---|---:|---|---|---:|---:|---|---|
| **Lorin & Klement E Cargo** | 1908 | L&K Type E commercial / Montenegro utility family | rigid/van, ~1.5 t class or ~4.8 m³ body | period petrol four-cylinder | ~30 km/h authoring target | local deliveries / parcels | Mladá Boleslav |
| **Pragov N** | 1915 | early Praga N truck family | rigid, ~3 t | ~30 kW | ~35 km/h | general freight | Praha |
| **Fatra 13** | 1924 | Tatra 13 | light rigid, 1.0 t payload | 8.8 kW | 45 km/h | city/local light freight | Kopřivnice |
| **Pragov RN** | 1933 | Praga RN | medium rigid, ~2–3 t | ~38–50 kW | ~60 km/h | versatile medium freight | Praha |
| **Fatra 111** | 1942 | Tatra 111 | 6×6, ~8–10 t | ~154 kW | 65 km/h | heavy/rough-road freight | Kopřivnice |
| **Pragov V3S** | 1953 | Praga V3S | 6×6, 5.5 t road / 3.5 t off-road | 70 kW | 60 km/h | construction, rough roads, recovery | Praha |
| **Neškoda 706 RT** | 1957 | Škoda 706 RT | rigid/tractor, ~7–9 t chassis payload | ~118 kW | ~70 km/h | normal regional freight | domestic heavy truck works |
| **VIAZ 100** | 1974 | LIAZ 100 | rigid or tractor; ~16–38 t GVW/GCW class | ~200–235 kW | 85 km/h | highway freight | Liberec/Mnichovo Hradiště lineage |
| **Fatra 815** | 1983 | Tatra 815 | 4×4–8×8; heavy rigid/tractor | 170–265+ kW | 80 km/h | quarry, construction, heavy haul | Kopřivnice |
| **Mercator Actros I** | 1996 | Mercedes-Benz Actros | 4×2 tractor, 40 t GCW class | ~290–390 kW | 90 km/h limiter | long-haul | off-map German import |
| **MANN TGX** | 2007 | MAN TGX | tractor/rigid, 40–44 t GCW class | 279–471 kW by engine | 90 km/h limiter | long-haul/high productivity | off-map German import |
| **Fatra Fénix** | 2011 | Tatra Phoenix | 4×4–8×8 rigid/tractor, up to ~45 t combination in road build | 227–390 kW | 85 km/h | heavy regional/rough terrain | Kopřivnice |
| **MANN TGE Cargo** | 2017 | MAN TGE / modern large van | 1.2–3.1 t payload depending chassis | 103–130 kW | 100–120 km/h game cap by body | dense urban/light freight | import |
| **Mercator eActros 600** | 2024 | Mercedes-Benz eActros 600 | 44 t technically permissible combination mass | 400 kW continuous / 600 kW max | 90 km/h limiter authoring cap | high-capacity zero-tailpipe-emission trunk routes | off-map German import; 600 kWh usable battery, charging required |

### Road body/configuration rule

A chassis family is not dozens of fake separate vehicles. A truck definition can support historically plausible factory/body-builder variants:

- flatbed;
- covered box;
- tipper;
- tanker;
- refrigerated body;
- tractor + semi-trailer;
- recovery/tow body;
- heavy-haul tractor.

Body changes alter tare mass, payload, cargo compatibility, price, loading method and maintenance. A body is manufactured/installed physically by the factory or a bodybuilder; it is not a free menu toggle after purchase.

## 7. Bus and coach catalogue

| ID / fictional model | Intro | Real basis | Seats / total capacity | Power | Max speed | Role | Production/source |
|---|---:|---|---|---:|---:|---|---|
| **Koňský omnibus O12** | pre-1900 | horse omnibus | 12 seated | animal | 8 km/h practical | city/local | local coachbuilder |
| **Benc Omnibus 1895** | 1895 | Benz Omnibus | 7 passengers + driver | 3.7 kW | ~15 km/h practical | tiny pioneering motor service | off-map import |
| **Lorin & Klement H-Bus** | 1908 | L&K Type H omnibus | ~12 seats authoring configuration | ~23.5 kW (32 hp) | ~30 km/h authoring target | local/interurban | Mladá Boleslav |
| **Pragov NO** | 1930 | Praga NO bus family | ~30–40 seats | ~60–75 kW | ~60 km/h | interurban/city | Praha |
| **Neškoda 706 RO** | 1947 | Škoda 706 RO | ~35–40 seated, ~60 total | ~100 kW | ~65 km/h | first post-war mass bus | domestic build |
| **Neškoda 706 RTO** | 1958 | Škoda 706 RTO | ~38–41 seated; urban total ~70 | ~118 kW | ~85 km/h | city/intercity variants | domestic build / Karusa bodywork |
| **Karusa ŠM 11** | 1965 | Karosa ŠM 11 | 24–31 seated + 59–67 standing | 132–154 kW | 65 km/h | high-capacity city bus | Vysoké Mýto |
| **Karusa ŠL 11** | 1965 | Karosa ŠL 11 | ~45 seated + ~30–40 standing | ~132–147 kW | 70–100 km/h by version | regional bus | Vysoké Mýto |
| **Karusa C734** | 1981 | Karosa C 734 | 45 seated + ~27–30 standing | 148–155 kW | 100 km/h | durable intercity/regional | Vysoké Mýto |
| **Karusa B731** | 1981 | Karosa B 731 | ~31 seated, ~90 total | ~148–190 kW by batch | ~70 km/h | city bus, automatic | Vysoké Mýto |
| **Karusa C934** | 1996 | Karosa C 934 | ~45 seated | ~180–220 kW | 100 km/h | improved regional/intercity | Vysoké Mýto |
| **Karusa C954** | 2002 | Karosa C 954 | 49 or 53 seated, ~88 total | 228 kW | 105 km/h | high-floor intercity | Vysoké Mýto |
| **SORA CN12** | 2004 | SOR CN 12 | 39–45 seated + standing | 194–210 kW | 100 km/h | low-entry regional | Libchavy |
| **Ivego Crossway 12** | 2006 | Irisbus/Iveco Crossway | ~45–55 seated | ~220–265 kW | 100 km/h | mainstream intercity | off-map / licensed assembly |
| **SORA NS12E** | 2017 | SOR NS 12 electric family | 29–35 seated + standing by configuration | 160 kW | 80 km/h | city electric | Libchavy; 242/388 kWh battery variants, charging required |
| **Ivego Crossway LE Elec** | 2025 | Crossway LE electric | configuration-dependent, ~80 total | 290 kW rated / 310 kW max drive | 85 km/h | modern regional/city electric | off-map import; charging required |

## 8. Era coverage — player should never be left with one sensible option

This matrix is the balancing target for **new offers plus credible used stock**, not a promise that every model is always in dealer inventory.

| Era | Rail freight traction | Rail passenger | Road freight | Bus/passenger road |
|---|---|---|---|---|
| **1900–1914** | ČMS 97 / 99 / 170 plus used older engines | 2-axle cheap coaches vs bogie corridor/premium stock | horses vs Daimlar petrol vs rare steam vs early local trucks after 1907 | horse omnibus vs Benc vs early L&K |
| **1915–1929** | old steam remains; improved local/express steam orders; used market grows | locomotive-hauled local/express/sleeper combinations | Pragov N, Fatra 13, older horses and imported trucks | early motor buses + surviving horse service |
| **1930–1946** | mature steam: cheap older vs fast/heavy newer | M120 railcar vs loco-hauled trains | Pragov RN, Fatra 13, larger domestic/imported trucks | Pragov NO and used earlier buses |
| **1947–1957** | N475 passenger, N556 freight, N498 express, older steam still cheap | M131/M262 vs coaches | Fatra 111, Pragov V3S, Neškoda 706 RT | 706 RO/RTO |
| **1958–1969** | Hektor diesel, Bobina/Šestikolo electric, steam still usable | railcars + UIC-Y coaches | V3S/706 RT/Fatra heavy trucks | RTO vs Karusa ŠM/ŠL |
| **1970–1989** | Barda/Brýlovec diesel, Šestikolo/Eso electric, used older fleet | M152 cheap branch unit vs UIC-Y/Z locomotive trains | VIAZ 100 vs Fatra 815 plus older cheap trucks | Karusa Š-series then 700-series city/regional variants |
| **1990–2009** | Eso/Pershing, rebuilt diesels, imported modern electrics | UIC-Z/Bmz stock, Pendolino from 2003 | used VIAZ/Fatra vs modern imported long-haul tractors | Karusa 700/900 vs C954/Crossway/SORA |
| **2010–2022** | Vektron / 109X / EffiShunter plus huge used market | RegioRys, Panter, Pendolino, loco-hauled fast stock | Fatra Fénix vs MANN/Mercator vs vans | SORA CN12, Crossway, electric city options |
| **2023+ authored modern stage** | Vektron/109X/modern shunters; old fleet still supportable | Panter / RegioLiška / Comfort 9 / Pendolino | diesel long-haul vs electric trunk vs specialist Fatra | modern diesel/HVO vs battery-electric |

A later calendar date can continue beyond authored modern events. The catalogue does not artificially stop the game; genuinely future vehicle technology is not invented until separately authored.

## 9. Acquisition, manufacture and import implementation

### 9.1 Active-map production

A new order from an active-map manufacturer creates a production order with:

- model/configuration;
- factory;
- required major material groups;
- labour and plant-hours;
- scheduled production slot;
- unit/batch completion dates;
- physical finished-vehicle inventory;
- delivery order to the buyer.

Suggested major inputs, aggregated enough for game performance:

- locomotives/railcars: steel, machinery/components, electrical equipment where applicable, fuel/engine components, interior fittings;
- coaches/wagons: steel/timber by era, bogies/wheelsets, brakes/couplers, body/interior equipment;
- trucks/buses: chassis/drivetrain, steel/body materials, tyres, electrical equipment, interior/body fittings;
- batteries for modern EVs: battery-pack component as a high-value industrial input rather than free embedded energy storage.

Do not require the player to source these inputs for a third-party manufacturer unless the contract specifically transfers that responsibility. The manufacturer's own procurement AI normally handles them.

### 9.2 Off-map manufacture

Vehicle purchasing is **not limited by the player's commercial presence, branches, licences or the detailed playable map**. A company based entirely inside the active world may order a historically plausible vehicle from a manufacturer in another playable country, from a neighbouring off-map region, or from a much more distant market such as Britain, France or the United States.

For an external manufacturer:

1. the order consumes finite macro factory capacity at the real source region represented by that manufacturer;
2. a completion date is generated from the actual external backlog/capacity model;
3. after completion, the vehicle enters a **long-distance delivery chain** rather than teleporting to the active map;
4. delivery cost and duration depend on source distance, vehicle type, required transshipment/handling, transport mode, permits/customs and historically available logistics;
5. the shipment reaches the active world through a suitable border/import node or other authored gateway and only then continues physically to the buyer's receiving point;
6. import/border/customs/approval time and cost are applied where historically/jurisdictionally relevant;
7. the final in-map movement follows GAME_DESIGN Section 15.8.

The player therefore does **not** need a branch or operating licence in the manufacturer's country merely to buy a vehicle there. Operating that vehicle commercially in a jurisdiction remains subject to the normal local licences, approvals and route compatibility.

A distant source can be commercially unattractive without being artificially forbidden. For example, importing a British steam road vehicle into Bohemia in 1900 may be possible but expensive and slow because the player pays the real delivery chain from Britain to the active-world import point. Likewise, a later North American specialist vehicle can be imported if the period has suitable shipping/rail/road logistics and the vehicle can be legally and technically accepted.

The external transport leg is paid by the buyer unless the purchase contract explicitly includes delivery. The seller may arrange transport, but it still uses real finite carrier capacity and real travel time. No off-map manufacturer gets a free hidden delivery shortcut.

### 9.2.1 Target-market adaptation and certification

Technical adaptation for the destination market is normally the **supplier's responsibility**, not a separate player workshop project before delivery.

When a vehicle needs destination-specific changes, the manufacturer, dealer or contracted bodybuilder can include them in the order configuration and price. Depending on era and vehicle type this can include, for example:

- lighting/signalling equipment;
- braking/control equipment;
- couplers/buffers;
- gauges/instruments/markings;
- electrical or heating compatibility;
- road-side driving equipment and legally required mirrors/lights;
- country-specific safety or radio/train-protection equipment where historically applicable.

The player sees the added cost, lead time and any resulting performance/weight/configuration consequences before accepting the order.

**National certification/type approval is separate from those physical modifications.**

If the exact vehicle model/configuration is already approved for normal operation in the destination country, the player's newly purchased units only need the ordinary registration/acceptance/inspection steps applicable to that era.

If the model/configuration has **not yet been operated/approved in that country**, the buyer may have to fund and wait for a first national type-approval/certification process before normal commercial use. The vehicle can still be manufactured and delivered while approval is pending if legally/logistically plausible, but it cannot enter normal commercial service until approval is complete.

Once a model/configuration has a valid approval in that country, later identical units do **not** repeat the full first-type process. They use the simpler per-unit registration/acceptance path unless regulation, configuration or technical standards materially change.

Certification complexity depends on real compatibility questions, not on an abstract foreign-vehicle penalty. Rail examples include gauge, loading gauge, axle load, braking, couplers, electrification, train protection and control systems. Road examples include dimensions, axle/GVW limits, brakes, lighting, visibility, steering/layout and other period-appropriate national requirements.

A supplier may offer a pre-approved destination-market variant. That can cost more than the base export model but avoids a first-buyer adaptation burden and may shorten approval.

### 9.3 Dealer stock

Dealers may pre-order common configurations. Dealer stock therefore has:

- a serial/asset identity;
- physical location;
- manufacture date;
- owner;
- exact configuration;
- finite quantity.

A dealer can sell three trucks from stock only if three trucks exist there.

### 9.4 Used stock

Used listings always reference an existing asset. For 1900 initialization, older models are seeded with plausible manufacture years and condition. Later used supply emerges from actual AI/player fleet sales, repossessions, dealer trade-ins and withdrawals from service.

### 9.5 Historical production changes

Ordinary factory production can change because:

- the manufacturer introduces a successor;
- tooling is repurposed;
- the company closes/merges;
- demand falls;
- inputs or workforce become constrained;
- regulation changes.

That affects **offers**, not the model definition. A player with an old locomotive does not lose it because the real-world production run ended.

## 9.6 Vehicle templates, variants and conversions

Every materially different vehicle configuration is represented by its own **vehicle template / variant** under one underlying model family.

Examples:

- passenger coach family:
  - `Economy`
  - `Business`
  - `Economy Neo`
  - `Business Neo`
- locomotive family:
  - original production configuration;
  - later train-protection retrofit;
  - revised heating/control package;
  - major engine/traction rebuild;
- road vehicle family:
  - factory-produced body/configuration variants are separate templates where historically offered;
  - later upgraded driveline/interior/safety packages remain within that fixed physical body/platform.

A template is not only a cosmetic skin. It defines the actual configuration that matters to simulation, such as:

- passenger classes/zones and seat count;
- cargo/body compatibility and payload within the fixed factory body/platform;
- installed equipment;
- power/traction package;
- braking/control systems;
- heating/HVAC;
- accessibility;
- comfort/service equipment;
- energy/fuel system;
- safety/train-protection package;
- mass and resulting axle/payload consequences;
- maintenance and parts family.

A concrete physical vehicle instance always references exactly one active template.

A template never changes the vehicle's fundamental body shell, frame geometry or visual platform. If a historically different body existed, it is authored as a separate factory-produced variant/model template rather than created later by a workshop reshape. A coach does not become a different coachbody, and a rigid truck does not become an unrelated tanker chassis through retrofit.


Changing configuration does **not** mutate statistics instantly. The player orders a **retrofit to an existing target template**. The job can be performed by the player's own compatible workshop or by an external qualified provider; the player does not manually edit individual parts on the vehicle.

A retrofit creates a real workshop/manufacturer job that:

1. reserves the physical vehicle;
2. requires a compatible workshop/provider and skills;
3. consumes real parts/materials;
4. occupies real workshop time/capacity;
5. changes the vehicle instance to the target template only when the job finishes.

The same serial/asset identity remains throughout the conversion. Ownership history, mileage, age and maintenance history are preserved.

Each conversion path is explicit. The game does not automatically allow arbitrary movement between every pair of templates. A conversion definition can specify:

- valid source template(s);
- target template;
- eligible workshop/provider families;
- required parts/materials;
- labour/plant time;
- cost;
- minimum/maximum vehicle condition where relevant;
- whether seats/body/equipment removed from the vehicle have residual value or reusable stock;
- certification/inspection required after the conversion;
- performance/capacity changes.

### Simple fleet-template editor

The player-facing editor must remain intentionally simple and understandable.

The normal workflow is:

1. choose the **vehicle model family**;
2. choose or duplicate an existing **template**;
3. edit only the small set of meaningful configuration groups supported by that family;
4. see the resulting capacity, compatibility, weight, cost and maintenance consequences immediately;
5. save the template under a player-facing name;
6. apply it to a new manufacturer order or create a conversion job for existing vehicles.

Do not expose engineering-level component trees, hundreds of individual part numbers or free-form stat editing.

For a passenger coach, the editor may expose groups such as:

- passenger layout/class zones;
- seat density/comfort package;
- luggage/bike/wheelchair allocation;
- HVAC/heating package;
- catering/service equipment;
- accessibility package;
- approved speed/braking/control package.

For a truck:

- chassis-cab family;
- the existing factory body/platform is fixed and cannot be reshaped by retrofit;
- cargo equipment supported by that body;
- refrigeration/tank/specialist equipment only where the original body/platform was designed to accept it;
- engine/driveline option when genuinely offered;
- safety/comfort package.

For a locomotive:

- only historically and technically supported factory/retrofit packages;
- train protection/control;
- heating/electrical package;
- approved traction/engine rebuilds;
- country equipment packages.

Templates should use clear player-facing names such as `Economy`, `Business`, `Economy Neo` or a custom player name. Internally they retain stable IDs and structured component/configuration references.

The editor must never imply that the player designs a vehicle from first principles. It configures or converts within real supported options for that model family.

## 10. Core specification schema for every authored vehicle

Machine-readable vehicle data should eventually include at least:

```text
id
localization_name
fictional_manufacturer_id
real_prototype_reference
introduction_game_date
source_region / factory_id
production_mode = active_map | off_map_import | bodybuilder | seeded_used_only
vehicle_family
role_tags[]
traction_or_propulsion
fuel_or_energy
power_kw
starting_tractive_effort_kn (rail where relevant)
max_speed_kph
empty_mass_t
service_mass_t
payload_t / cargo_volume_m3 / seats / standing / berths
length_m
width_m
height_m
axle_count
axle_load_t
minimum_curve_m (rail)
gauge_mm (rail)
electrification_systems[]
coupler_and_brake_family
train_heating/control_compatibility
road_drive_layout / permitted_gvw_or_gcw (road)
body_or_cargo_compatibility[]
crew_requirements[]
facility_requirements[]
loading_requirements[]
consumption_model
maintenance_family
maintenance_intervals
parts_support_family
retrofit_options[]
ordinary_production_capability
special_order_capability
dealer_stock_weight
used_market_weight
manufacturer_lead_time_basis
purchase_cost_index
operating_cost_index
reliability/condition_base_inputs
prefab / LOD / sound / animation refs
research_sources[]
notes
```

### Cost-index convention for content authoring

Until the economy is balanced in the single game unit `money`, use a **same-era purchase-cost index**:

- 50–70 = cheap/basic;
- 80–120 = ordinary mainstream;
- 130–180 = premium/heavy/specialist;
- 200+ = exceptional high-performance trainset/special equipment.

The index is not shown to the player and is not a hidden gameplay modifier. It is an authoring tool that must later be converted into explicit visible purchase prices using the era economy.

## 11. Initial gameplay cost/maintenance positioning

| Family example | Cost index | Maintenance burden | Consumption burden | Intended reason to buy |
|---|---:|---|---|---|
| ČMS 97 Mravenec | 55 used / 80 special-new | medium-high labour, simple parts | high coal per useful tonne-km | tiny curves, cheap used asset |
| ČMS 170 Horal | 100 | high steam servicing | high | heavy 1900 freight |
| Neškoda N387 Mikádo | 150 | high | high | speed/prestige |
| Hektor | 90 | medium | medium diesel | cheap dieselization / shunting |
| Bobina | 120 | medium | low energy where electrified | reliable electric mainline |
| Eso | 145 | medium | low-medium | dual-system flexibility |
| 109X / Vektron | 220–240 | medium-high specialist | low-medium | interoperability, speed, power |
| Horse H2 | 45 | stable/animal support | feed/rest | cheapest tiny local delivery |
| Daimlar 1896 | 140 in 1900 | very high scarcity | petrol | speed/flexibility without horses |
| Pragov V3S | 85 | medium | high fuel | rough-road access |
| VIAZ 100 | 100 | medium | medium | normal high-capacity road freight |
| Fatra Fénix | 145 | medium | medium | terrain + modern payload |
| eActros-class | 180+ | medium | electricity / charging downtime | trunk efficiency, later emission rules |
| Koňský omnibus | 50 | stable support | feed/rest | cheap small local passenger route |
| Karusa C734 | 95 | medium | medium-high diesel | robust regional workhorse |
| SORA CN12 | 115 | medium | medium | low-entry regional flexibility |
| Crossway LE electric | 170+ | medium | electricity / charging | modern accessible zero-tailpipe route |

Exact prices, service intervals and fuel consumption values should be balanced only after route economics and manufacturer production costs are in place.

## 12. Research basis / prototype anchors

The following sources were used to anchor dates and representative specifications. The content definitions should retain per-model provenance rather than relying only on this summary.

### Rail
- kkStB 97 / ČSD 310.0: https://en.wikipedia.org/wiki/KkStB_97
- kkStB 99 / ČSD 320.0: https://en.wikipedia.org/wiki/KkStB_99
- kkStB 170 / ČSD 434.0: https://de.wikipedia.org/wiki/KkStB_170
- ČSD 387.0: https://en.wikipedia.org/wiki/%C4%8CSD_Class_387.0
- ČSD 475.1: https://web.kurzy.cz/wiki/Lokomotiva_475.1
- ČSD 556.0: https://loco-info.com/locomotive/16923?lng=en&t=Type
- ČSD 498.1: public technical summaries cross-checked against preserved-locomotive data
- ČSD E 499.0 / class 140: https://de.wikipedia.org/wiki/%C4%8CSD-Baureihe_E_499.0
- ČSD T 435.0 / class 720: https://www.atlaslokomotiv.net/loko-720.html
- ČSD T 478.1 / classes 749/751: https://de.wikipedia.org/wiki/%C4%8CSD-Baureihe_T_478.1
- class 363: https://spz.logout.cz/vozidla/363/data363.html
- Škoda 109E: https://www.skodagroup.com/cs/produkty-a-sluzby/rychlikove-lokomotivy
- Siemens Vectron: https://press.siemens.com/global/en/feature/vectron-vehicle-concept
- EffiShunter 1000: CZ LOKO catalogue / product data
- M 152.0 / class 810: https://en.wikipedia.org/wiki/%C4%8CSD_Class_M_152.0
- PESA Link / class 844: https://www.pshzd.cz/m844.html
- RegioPanter: https://www.skodagroup.com/cs/reference/regiopanter-cesko
- class 680 Pendolino: public ČD/class technical data

### Road
- Benz Omnibus 1895: https://de.wikipedia.org/wiki/Benz_Omnibus_%281895%29
- Daimler Motor-Lastwagen 1896: https://de.wikipedia.org/wiki/Daimler_Motor-Lastwagen_%281896%29
- Thornycroft steam carriage: period Automotor and Horseless Vehicle Journal material
- Praga V3S: Czech Army technical data
- Tatra 815: Czech Army technical data
- Tatra Phoenix: https://www.tatra.cz/tatra-phoenix/
- Karosa Š series / ŠM 11: preserved-bus technical data and Karosa historical sources
- Karosa C 734: historical technical data / preserved vehicles
- Karosa C 954: manufacturer technical sheet / preserved documentation
- SOR CN 12: manufacturer technical sheet
- Iveco Crossway LE electric: current manufacturer technical sheet
- MAN TGX/TGE: current MAN technical data

## 13. Follow-up authoring work

This research closes the **model-selection direction**, not the implementation/content task. Before a model can count as delivered content:

1. create versioned machine-readable definitions using the schema above;
2. choose one representative configuration for each family and validate exact prototype values;
3. add factory/company definitions and factory capability timelines;
4. add off-map manufacturer/import nodes;
5. balance explicit `money` purchase prices, production inputs, fuel/energy use and maintenance intervals;
6. author meshes/LODs/material variants, interiors where visible, couplers, lights, animation and sound;
7. author dealer/used-market seeding weights by date and region;
8. add compatibility tests for gauge/electrification/axle load/body/cargo/loading/maintenance;
9. add acceptance coverage proving that a purchased vehicle is manufactured/stocked/imported and physically delivered rather than spawned.

