# Tranzit — Technology and research UI

> **Status: CONFIRMED UI DIRECTION — UI-D38, 2026-09-30.** The player accepted a deliberately simple Technology workspace. Research does not act as a universal company-wide upgrade button: completing a technology primarily unlocks concrete capabilities, assets, construction standards, modules, upgrades or company systems. The owning gameplay system then decides whether the player must build, buy, upgrade, install or adopt anything further. Company-wide adoption exists only where the technology is genuinely an organizational/business system. Exact research durations, costs, categories and visual dimensions remain content/design work. This specification is not an implemented or tested UI.

Read with [GAME_DESIGN.md](GAME_DESIGN.md), especially Sections 3.5, 7.2, 15.11, 21–28 and 40. Read also [UI_UX_DESIGN.md](UI_UX_DESIGN.md), UI-D15, [UI_CONSTRUCTION.md](UI_CONSTRUCTION.md), [UI_COMPANY.md](UI_COMPANY.md), [UI_DEPOTS.md](UI_DEPOTS.md), [UI_MAINTENANCE.md](UI_MAINTENANCE.md), [UI_FLEET.md](UI_FLEET.md) and [UI_STATIONS.md](UI_STATIONS.md). These owning systems keep authority over the physical purchase/build/upgrade/install action after a technology unlock.

## 1. One simple Technology workspace

Use **Company → Technology / Firma → Technologie** as the primary entry.

Do not build a separate research-management game.

The default workspace can be filtered by:

- **Available / Dostupné**
- **In progress / Probíhá**
- **In use / Používané**
- **All / Vše**

Optional categories can include:

- Operations and signalling
- Infrastructure and construction
- Maintenance
- Company systems
- Sales and passenger information
- Logistics/automation

Use a searchable list/card view rather than requiring a giant full-screen technology tree.

## 2. Core rule: research unlocks possibilities

Keep these stages conceptually separate:

1. **Technology exists in the world** — historically available or plausibly reachable at the current date.
2. **Company has access/knowledge** — either because the technology is already commonly available, or because the company has completed/acquired the necessary research/know-how.
3. **Capability is actually implemented where required** — the player builds, buys, upgrades, installs or adopts it through the owning system.

Completing research never automatically:

- upgrades existing track;
- constructs a workshop;
- expands a station;
- upgrades every branch;
- buys vehicles;
- installs equipment;
- creates trained staff;
- creates inventory;
- changes an already completed physical asset without a real project.

## 3. Not every technology needs research

A technology that is already established and commercially available in the selected era may be usable without making the player “research” a historical invention again.

Example:

> **Telephone coordination**
>
> Status: Available for adoption
>
> The technology already exists in the world.  
> Your company can adopt the corresponding business system when its requirements are met.

Research is primarily used when:

- the company wants earlier access within historically plausible limits;
- company-specific know-how is genuinely required;
- the technology belongs to a research progression rather than ordinary market adoption.

Start-year initialization remains authoritative. A later-start company does not need to rediscover technology already established in that era.

## 4. Technology card

Keep the default technology detail focused on five things:

- **What it enables**
- **What it unlocks**
- **Prerequisites**
- **Research cost/time**, if research is required
- **Current company status**

Example:

> **Advanced rail maintenance**
>
> Enables access to heavier overhaul capability.
>
> **Unlocks**
> Heavy Maintenance Workshop  
> Advanced inspection equipment
>
> **Prerequisite**
> Basic mechanical workshop knowledge
>
> Research: [money icon] 4,200 · 14 game days
>
> **Start research**

Do not fill the default view with research-point formulas or hidden multipliers.

Longer historical/technical explanation can live under More information.

## 5. Unlock result types

A technology can unlock one or more different kinds of result.

### 5.1 New buildable or construction standard

Example:

> **Improved railway permanent way**
>
> Unlocks:
> - higher track construction standard;
> - higher supported axle-load option;
> - higher design-speed option where geometry permits;
> - compatible advanced switches/modules where defined.

After research:

> **Researched**
>
> New construction options are available in **Build**.
>
> **Show unlocked construction**

The technology does not modify existing track.

Existing infrastructure must be upgraded through the normal construction/project system, with real cost, time, materials, access effects and disruption.

### 5.2 New facility/module

Example:

> **Heavy railway maintenance**
>
> Unlocks:
> - Heavy Maintenance Workshop;
> - compatible overhaul equipment/modules.

After completion, these appear in the appropriate construction/facility workflow.

The company still needs:

- a valid site/facility;
- construction or upgrade;
- equipment;
- qualified staff;
- parts/supplies;
- actual workshop capacity.

### 5.3 Upgrade for an existing object

A technology can unlock a new upgrade level for:

- branch;
- station;
- depot/workshop;
- terminal;
- infrastructure;
- another supported physical/system object.

Example:

> **Office systems III unlocked**

The branch detail can now offer:

> Office systems II → III  
> [money icon] 2,800 · 3 game days  
> **Prepare upgrade**

The Technology screen links to that workflow; it does not execute the upgrade itself.

### 5.4 Company-wide system/adoption

Some technologies are genuinely organizational and therefore use a simple **Adopt / Zavést** action.

Examples can include:

- centralized reservations;
- centralized dispatch;
- customer database;
- electronic ordering;
- later company-wide planning/administrative systems.

Example:

> **Centralized reservations**
>
> Research/knowledge: complete  
> Company system: not adopted
>
> Adoption:
> [money icon] 8,500 · 9 game days
>
> **Adopt**

After adoption, the corresponding company capability becomes available subject to any remaining local/facility requirements.

Do not require per-branch clicks unless the underlying mechanic genuinely needs a physical/local installation.

### 5.5 Direct know-how capability

If a technology represents know-how that needs no separate physical acquisition or company implementation step, its capability may become active when research/knowledge completes.

Use this only when there is genuinely nothing left to build, buy, install or adopt.

## 6. One technology may unlock several things

A technology can have several unlocks across systems.

Example:

> **Modern railway construction methods**
>
> Unlocks 5 items:
>
> Infrastructure: 2  
> Construction modules: 2  
> Facility upgrade: 1
>
> **Show unlocked items**

Each item links to its canonical destination.

Do not duplicate the construction, fleet or facility catalogue inside Technology.

## 7. Research capacity stays simple

Show research capacity as a small planning constraint, for example:

> Research projects: 1 / 1 active

Later capability may increase this to additional slots through:

- an internal research department/centre;
- an external research contract;
- other already-defined progression.

Do not add:

- manual scientist assignment;
- research points;
- continuous percentage funding sliders;
- per-project staff micromanagement;
- multiple hidden laboratory quality scores.

A project shows:

- technology;
- provider/source;
- remaining/expected time;
- cost;
- prerequisite/blocker if any.

## 8. Internal versus external research

Where supported, a research project may be:

- handled by the player's own research capability; or
- purchased from an external research/technical partner.

External research uses a real external company/agreement where applicable and links to UI-D37.

Do not create a separate fake research-provider marketplace if the existing external-company/commercial systems can represent the offer/contract.

External research capacity remains finite where the core economy models it.

## 9. Prerequisites without a giant tech tree

Technology dependencies remain real, but the normal UI should not require navigating a huge branching tree.

Example:

> **Advanced signalling**
>
> Missing prerequisite:
> **Block signalling**
>
> **Open prerequisite**

A compact prerequisite/dependency view can show upstream/downstream relationships when requested.

The normal browse experience remains list/filter/search first.

## 10. Contextual technology links

Other systems may surface a relevant technology when it explains a real limitation.

Examples:

From a branch:

> A later company system can reduce this administrative dependency.  
> **Open relevant technology**

From construction:

> Higher track standard unavailable.  
> **Requires: Improved railway permanent way**

From maintenance:

> Heavy overhaul unavailable.  
> **Requires: Heavy railway maintenance**

From a station:

> Realtime passenger information unavailable.  
> **Requires supporting company/local information capability**

These links open the exact technology detail under UI-D09.

They do not auto-start research or purchase an upgrade.

## 11. Vehicle technology and manufacturer availability

Technology access and vehicle-market availability remain separate.

Research/technology may make a new vehicle family, propulsion system or capability usable by the company where the wider design supports that relationship.

It still does not:

- create a manufacturer;
- create market stock;
- eliminate production lead time;
- deliver a vehicle;
- bypass licence/infrastructure compatibility.

Actual vehicle models/offers remain owned by the Fleet/market system and manufacturer availability rules.

Historical vehicle models remain discoverable under the no-end-year rule after introduction; technology progression must not add a hard disappearance date.

## 12. Existing assets do not upgrade themselves

When a technology improves:

- track standard;
- signalling;
- electrification;
- station facilities;
- workshop capability;
- branch systems;
- another physical asset;

existing assets retain their current configuration until the relevant real upgrade occurs.

The UI may show:

> **Upgrade now available**
>
> 6 owned stations can use this module.

This is navigation/opportunity information, not an automatic retrofit command.

## 13. Adoption and rollout boundaries

For company-system technologies, keep adoption simple:

- one adoption project where possible;
- visible cost;
- visible time;
- visible prerequisites;
- visible capability gained.

Local physical dependencies remain separate only where they are meaningful.

Example:

A company may adopt a centralized passenger-information system, while an individual rural station still needs a supported local information capability before passengers there receive live updates.

Do not make the player individually “install the same software” at dozens of locations unless a physical/local upgrade is part of the actual mechanic.

## 14. Status model

Use a small understandable set of statuses such as:

- **Not yet available**
- **Missing prerequisite**
- **Available to research**
- **Researching**
- **Unlocked / Researched**
- **Available to adopt** — company-system technologies only
- **Adopting** — where applicable
- **In use**

A technology can be **Unlocked** while none of its physical buildables have yet been built.

Do not call that technology “not implemented” merely because the player has not constructed the newly unlocked workshop.

## 15. Cost and time

Research/adoption uses:

- UI-D34 money display;
- shared game calendar;
- explicit cost/time;
- actual provider/capacity where required.

Pause stops research/adoption progress with all other time-driven simulation.

Changing game speed changes wall-clock completion time but not the game-time duration/cost of the same project.

## 16. History and explainability

Technology history can retain meaningful milestones:

- research started;
- research completed;
- company adoption started/completed;
- major unlocked capability;
- replacement/superseding technology becoming available.

Do not log every percentage tick.

Where a capability changed, the player should be able to answer:

- which technology enabled it;
- when the company gained access;
- whether a separate physical upgrade/adoption remains necessary.

## 17. Save/load safety

Persist:

- discovered/available technology state;
- completed company research/knowledge;
- active research projects;
- research capacity commitments;
- company-system adoption projects;
- completed adoption state.

After save/load:

- research does not complete twice;
- cost is not paid twice;
- unlocked construction/catalogue entries remain unlocked;
- existing physical assets are not silently upgraded;
- an in-progress company adoption resumes from authoritative progress;
- restoring the Technology window does not start/stop projects.

## 18. Acceptance evidence to collect

| ID | Required scenario |
|---|---|
| TECHUI-A01 | Inspect technologies that are historically unavailable, already commercially available, researchable and already researched. A later-start company does not re-research an established invention merely because it is newly founded. |
| TECHUI-A02 | Research a workshop technology. Completion unlocks the workshop/module in the owning construction/facility UI but creates no building, equipment, staff or maintenance capacity. |
| TECHUI-A03 | Research a higher track standard. New construction/upgrade options appear, while existing track remains unchanged until a real construction project upgrades it. |
| TECHUI-A04 | Unlock a branch/station/facility upgrade and follow the direct link into that object's normal upgrade workflow. Technology never charges/builds the upgrade a second time. |
| TECHUI-A05 | Complete a company-system technology, then run its one company-level adoption project. Capability stays unavailable until adoption finishes where adoption is required; local physical dependencies remain explicit without per-site busywork. |
| TECHUI-A06 | Use a technology with several unlocks across construction/facility/other systems. All links point to canonical objects/catalogues and no duplicate inventory/marketplace exists. |
| TECHUI-A07 | Run own and external research with finite research capacity. Provider/cost/time are explicit; no research points/scientist micromanagement or fabricated external capacity is introduced. |
| TECHUI-A08 | Save/load active research and adoption, then complete them at different simulation speeds. No duplicate payment/unlock occurs and equal game-time work produces the same result. |
| TECHUI-A09 | Verify vehicle-related technology does not create market stock, delivery or a hard model end-year. Fleet/market availability remains authoritative. |
| TECHUI-A10 | Verify CZ/EN, enlarged UI, contextual prerequisite links and concise list/filter/search operation without requiring a giant technology tree. |

## 19. Decision record

| ID | Decision | Status |
|---|---|---|
| UI-D38 | One simple Technology workspace. Research/knowledge unlocks concrete options; physical assets/upgrades remain in their owning systems; only genuine company-wide systems use a simple adoption project. No research-point/scientist micromanagement or mandatory giant tech tree | CONFIRMED on 2026-09-30 |

UI-D38 complements UI-D01–UI-D37. GAME_DESIGN Sections 27–28 remain authoritative for technology/research/automation mechanics.
