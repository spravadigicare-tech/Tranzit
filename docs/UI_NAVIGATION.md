# Tranzit — Final navigation and global search UI

> **Status: CONFIRMED UI DIRECTION — UI-D41, 2026-09-30.** The player confirmed the final HUD/navigation composition: company/finance in the upper-left HUD, global search and map-layer controls in the upper-right HUD, and one compact bottom bar with a distinct Build action, a grouped management navigation cluster, and events/time controls. This replaces the earlier bottom-bar proposal that also carried company/cash/search/map-layer functions. Exact pixel dimensions, icons and spacing remain visual implementation work. This specification is not an implemented or tested UI.

Read with [UI_UX_DESIGN.md](UI_UX_DESIGN.md), especially UI-D05, UI-D06, UI-D07, UI-D09 and UI-D15. All navigation opens the already-defined canonical workflows; it must not create duplicate systems.

## 1. Final HUD composition

Use this functional composition:

```text
┌─────────────────────────────────────────────────────────────────┐
│ ☰  TRANZIT EXPRESS                                      🔍 Layers │
│    ◉ 124 800   +3 420                                     │
│                                                               │
│                                                               │
│                         WORLD                                 │
│                                                               │
│                                                               │
│                                                               │
│                                                               │
│                                                               │
│                                                               │
│  [ + STAVĚT ]   [ PROVOZ  OBCHOD  MAJETEK | FIRMA  SVĚT ]   [! 3] Day 8 14:32  ⏸ 4× │
└─────────────────────────────────────────────────────────────────┘
```

The diagram is a functional wireframe, not a pixel-perfect layout.

## 2. Upper-left HUD — company and finance

Show:

- Menu;
- current player-company name/identity;
- current cash using UI-D34 money icon;
- compact current financial-period result where useful and clearly period-scoped.

Clicking:

- company identity opens Company overview;
- cash/result opens Finance;
- Menu opens UI-D36 system menu.

Controlled subsidiaries remain AI-managed under UI-D39 and do not become selectable active-company contexts here.

## 3. Upper-right HUD — world tools

Show:

- **Global search**
- **Layers / Vrstvy**
- other genuinely map/view-specific controls only where later needed.

Map Layers opens UI-D21.

Do not duplicate Layers under World navigation.

Search and Layers remain available while ordinary floating windows are open.

## 4. Bottom bar — three functional areas

### 4.1 Build

Keep **+ Build / + Stavět** visually distinct from ordinary management navigation.

It opens the canonical construction catalogue/map-building workflow.

Build is an action on the world, not another management list.

### 4.2 Main management navigation

Use one visually grouped central cluster:

> **Operations · Business · Assets | Company · World**

The separator is visual grouping, not another menu level.

Do not display six equal isolated toolbar buttons if the grouped treatment can make the hierarchy clearer.

### 4.3 Events and time

The right side contains:

- compact UI-D24 event/decision indicator;
- game date/time;
- pause;
- current speed and access to supported speed choices.

Events and time remain visually separate from the main management cluster.

## 5. Final navigation taxonomy

### Operations / Provoz

Contains:

- **Lines / Linky**
- **Trips / Jízdy**
- **Duties / Oběhy**
- **Capacity & access / Kapacita a přístup**

Operational incidents are not duplicated here because UI-D24 has dedicated event access.

### Business / Obchod

Contains:

- **Market / Trh**
- **Opportunities / Příležitosti**
- **Offers / Nabídky**
- **Contracts / Smlouvy**
- **Shipments / Zásilky**
- **Procurement & suppliers / Nákup a dodavatelé**
- **Tariffs & tickets / Tarify a jízdenky**

External Transport Order remains a contextual canonical workflow reached from the relevant contract/shipment/procurement/delivery context rather than a separate top-level navigation item.

### Assets / Majetek

Contains:

- **Vehicles / Vozidla**
- **Depots & workshops / Depa a dílny**
- **Stations & terminals / Stanice a terminály**
- **Infrastructure / Infrastruktura**
- **Maintenance / Údržba**
- **Construction projects / Stavební projekty**

Do not duplicate Procurement inventory as another unrelated asset database. Facility-specific stock remains reachable from its facility detail.

### Company / Firma

Contains:

- **Company overview / Přehled firmy**
- **Branches / Pobočky**
- **People & management / Lidé a management**
- **Finance**
- **Licences & expansion / Licence a expanze**
- **Technology / Technologie**
- **Ownership & acquisitions / Vlastnictví a akvizice**

Group/subsidiary information remains within Company/UI-D39 rather than another top-level navigation category.

### World / Svět

Contains:

- **Cities & regions / Města a regiony**
- **Companies / Firmy**
- **Public priorities / Veřejné priority**
- **News / Zprávy**

Public priorities is the central known/public overview of current state, regional and municipal development/transport goals. The same priority objects remain reachable from the relevant authority/city/region detail; this screen does not create a second tender database. Concrete advertised tenders remain **Business → Opportunities**.

Do not include Map Layers here; Layers is a direct upper-right HUD tool.

Do not create a separate Competitors section. Competitor is a role of a Company under UI-D37.

## 6. Global search

Global search is a navigation tool, not a command palette.

It can find known/available:

- cities/regions;
- Lines;
- Trips where useful;
- vehicles;
- stations/terminals;
- depots/workshops;
- branches;
- companies;
- contracts;
- shipments;
- infrastructure;
- other stable inspectable objects;
- navigation functions such as Maintenance or Licences.

Example query:

> Brno

Possible grouped results:

> **City** — Brno  
> **Station** — Brno hlavní nádraží  
> **Our asset** — Brno depot  
> **Branch** — Brno branch  
> **Company** — RailServ Brno

Function result example:

> **Function** — Assets → Maintenance

Clicking a result opens the exact canonical object/workflow using UI-D09.

## 7. Search respects information visibility

Search never reveals an object merely because it exists in the simulation database.

Results must respect:

- public knowledge;
- observed knowledge;
- contractual/commercial knowledge;
- discovered opportunities;
- macro/inactive-region visibility;
- ownership and permission boundaries.

Search must not reveal:

- hidden competitor facilities;
- unrelated private contracts;
- unknown vehicles;
- undiscovered opportunities;
- private data that UI-D37/UI-D28 would otherwise hide.

Searching does not activate a region.

## 8. Search result identity

Group results by type and show enough context to distinguish similar names.

Example:

> **Brno depot**  
> Railway depot · Brno · our company
>
> **Brno depot**  
> Bus garage · Brno · Morava Rail

Use stable identities, not text matching alone, for navigation.

Historical/inactive objects may appear when legitimately retained and searchable, but must be visibly marked as historical/read-only.

## 9. Search is not a command console

Do not allow search strings to directly perform gameplay actions such as:

- sell vehicle;
- create Line;
- buy asset;
- cancel contract;
- change speed.

Search can navigate to the relevant function/object where the player can then use the normal validated workflow.

## 10. Interaction and persistence

Opening HUD menus/search/layers:

- does not pause/resume;
- does not change speed;
- does not acknowledge incidents;
- does not issue gameplay commands;
- does not discard drafts.

Preserve useful search query/results while navigating where practical, without making search state authoritative campaign data.

## 11. Acceptance evidence to collect

| ID | Required scenario |
|---|---|
| NAVUI-A01 | At 1080p and enlarged UI scale, upper-left company/finance, upper-right Search/Layers and bottom three-area bar remain readable/reachable without duplicating controls. |
| NAVUI-A02 | Open Build, every main management group and Events/time controls. Each resolves to its canonical workflow; the grouped bottom bar does not become a second dashboard. |
| NAVUI-A03 | Verify Operations/Business/Assets/Company/World contents match the final taxonomy and no duplicate Competitors, Layers or External Transport Order top-level screen appears. |
| NAVUI-A04 | Search for a city, Line, vehicle, company, contract and function; results are grouped/identifiable and open exact UI-D09 targets. |
| NAVUI-A05 | Search for unknown/private competitor data and undiscovered opportunities. They remain absent; search does not unlock regions or bypass provenance. |
| NAVUI-A06 | Test duplicate names, renamed/historical objects and CZ/EN strings. Search opens the correct stable identity and clearly marks historical targets. |
| NAVUI-A07 | Open search/layers/menus while running and paused, with dirty planners/windows. No command, pause/speed change, acknowledgement or lost edit occurs. |

## 12. Decision record

| ID | Decision | Status |
|---|---|---|
| UI-D41 | Final HUD/navigation: upper-left company/finance, upper-right global Search + Layers, bottom bar with distinct Build action, grouped Operations/Business/Assets | Company/World navigation, and separate Events/time controls. Global search navigates only to known objects/functions and never acts as a command palette or information bypass | CONFIRMED on 2026-09-30 |
