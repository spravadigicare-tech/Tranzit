# Tranzit — Ownership, acquisitions and infrastructure market UI

> **Status: CONFIRMED UI DIRECTION — UI-D39, refined 2026-09-30.** Ownership is deliberately lightweight. A controlled subsidiary remains an AI-managed company; the player does not switch into it and micromanage its ordinary operation. Control instead gives a small set of meaningful owner actions: set broad direction, issue a concrete directive such as changing a Line, transfer capital/assets, and approve or initiate major company decisions. The subsidiary then solves the operational consequences through the same real simulation rules as any other company. Minority ownership remains investment/governance only. Infrastructure remains physical and retains applicable obligations/state through ownership changes. This specification is not an implemented or tested UI.

Read with [GAME_DESIGN.md](GAME_DESIGN.md), especially Sections 29 and 38–39; [UI_EXTERNAL_COMPANIES.md](UI_EXTERNAL_COMPANIES.md) for UI-D37; [UI_COMPANY.md](UI_COMPANY.md); [UI_FINANCE.md](UI_FINANCE.md); [UI_CAPACITY_ACCESS.md](UI_CAPACITY_ACCESS.md); [UI_CONSTRUCTION.md](UI_CONSTRUCTION.md); and [UI_UX_DESIGN.md](UI_UX_DESIGN.md).

## 1. Workspace

Primary entry:

**Company → Ownership and acquisitions / Firma → Vlastnictví a akvizice**

Use three practical views:

- **Our holdings / Naše podíly**
- **Companies / Firmy**
- **Infrastructure / Infrastruktura**

Contextual actions from a company or asset open the same workflow already scoped to that target.

Do not build a stock-exchange or corporate-management minigame.

## 2. Ownership is not the same as control

Always distinguish:

- ownership/economic interest;
- actual control rights.

A minority stake may provide:

- dividends/distributions;
- ownership information the player is entitled to receive;
- applicable governance rights.

It does not permit operational owner directives unless the player actually controls the company.

Show, for example:

> Our holding: 20%  
> Control: none

or:

> Our holding: 65%  
> Control: yes

Do not hard-code one universal control percentage into presentation. Control follows the actual ownership/governance rules.

## 3. Buying a stake or company

Shares/stakes are purchasable only when a real seller/opportunity exists or owners are willing to negotiate.

Keep the interaction simple:

- buy an offered stake;
- make an offer;
- acquire a controlling stake;
- acquire the whole company.

No order book, short selling, derivatives or trading minigame.

Before a major acquisition, show the known material scope:

- purchase price;
- ownership/control obtained;
- cash/debt;
- major assets/infrastructure;
- active Lines;
- relevant contracts/leases;
- licences/permissions;
- material obligations or change-of-control issues.

The acquisition view respects UI-D37 knowledge boundaries.

## 4. Controlled subsidiary: always AI-managed

A controlled subsidiary remains its own company and **continues to be operated by its AI management**.

The player does not switch into the subsidiary's normal full management UI and does not manually manage its daily:

- duties;
- staff scheduling;
- maintenance;
- routine procurement;
- ordinary vehicle assignments;
- disruption recovery;
- everyday commercial work.

The subsidiary keeps separate:

- cash/debt;
- staff/management;
- contracts;
- licences;
- vehicles;
- infrastructure;
- inventories;
- projects/orders;
- operating history.

Control gives owner authority, not a second company to micromanage.

## 5. Four owner interactions

Keep owner interaction deliberately small.

### 5.1 Direction

Set only broad company direction, for example:

- grow / maintain / reduce;
- preferred transport/business focus;
- permitted or preferred expansion region;
- broad investment limit where needed.

Do not create dozens of policy sliders.

### 5.2 Directives

The player can issue an owner directive for a meaningful concrete outcome.

Typical directives:

- create a Line;
- change a Line;
- close a Line;
- increase/decrease service capacity;
- expand into a region;
- build/upgrade a major facility;
- acquire/sell a major asset where governance allows.

Use existing editors where useful, but submitting the change creates an **owner directive**, not direct player operation of the subsidiary.

Example:

> Owner changed R12 to a 30-minute interval.
>
> Morava Rail now needs:
> +3 suitable trainsets  
> additional crew capacity  
> more depot capacity  
> revised infrastructure slots

The subsidiary then solves those requirements itself through its normal planners/markets/contracts.

If it cannot currently execute the directive:

> **Directive blocked**
>
> No suitable vehicles available  
> Required route capacity unavailable
>
> **Show blockers**

The directive remains explainable rather than silently failing or cheating.

### 5.3 Capital and asset transfer

Allow straightforward owner transactions:

- capital contribution;
- dividend/distribution where permitted;
- intra-group loan where useful;
- transfer/sale/lease of a vehicle or infrastructure asset.

Every transfer is real.

A transferred vehicle:

- keeps its physical location;
- retains current operational state until the effective transfer;
- may create a fleet shortage in the subsidiary;
- does not teleport or duplicate.

Before confirming, show the main known consequence.

Example:

> Transfer Locomotive 021 to parent company
>
> Current use: R8  
> No replacement currently available  
> Morava Rail will need to reorganize service or acquire replacement capacity.
>
> **Transfer anyway**

After the transfer, the subsidiary's AI resolves the shortage through normal rules.

### 5.4 Major company decisions

The owner can initiate or approve major matters such as:

- major borrowing;
- acquisition/sale of another company;
- major infrastructure sale;
- appointment/removal of top management;
- whole-company integration.

Keep this to genuinely material decisions. Routine purchases/contracts stay with subsidiary management.

## 6. Editing a subsidiary Line

A controlled subsidiary's Line can open the same familiar Line information/editor components where useful.

The difference is authority.

For the player's own company:

> Prepare change / Activate

For a subsidiary:

> **Issue directive**

The directive records the desired outcome/configuration.

The subsidiary then:

1. validates it;
2. obtains vehicles/staff/capacity/permissions/facilities as required;
3. prepares the operational change;
4. applies it only when real prerequisites allow.

The owner can inspect progress/blockers without manually executing every dependency.

## 7. Owner directives can create problems

Do not protect the player from bad owner decisions by refusing every harmful action.

If the player removes a needed vehicle or orders an aggressive Line change, show the consequence and allow it where legally/physically possible.

The subsidiary must then react using normal simulation:

- reserve/substitute assets;
- reorganize duties;
- acquire/lease replacements;
- delay the directive;
- reduce service;
- surface an unresolved blocker.

The AI cannot invent resources merely because the owner issued a directive.

## 8. Group overview

Company UI shows a compact group/holdings list:

> **Our group**
>
> Morava Rail — 100%, controlled  
> Central Coaches — 65%, controlled
>
> **Minority investments**
>
> Bohemia Logistics — 18%

For each controlled subsidiary show only the useful owner-level information:

- ownership/control;
- broad direction;
- active owner directives;
- major blocker/decision;
- compact financial/operating summary where appropriate.

Open the normal UI-D37 company detail for broader company information.

Avoid a complex organizational-chart editor.

## 9. Intra-group use without transfer

Group ownership does not automatically make every asset free/shared.

If another group company uses a subsidiary's:

- workshop;
- depot;
- infrastructure;
- transport capacity;
- leased vehicle;
- supply/service;

use the canonical access/agreement/capacity rules where needed.

Group relationship can simplify commercial intent, but not physical capacity.

## 10. Company integration

A controlled subsidiary can optionally be integrated into the parent.

Integration is separate from ordinary owner control.

Before confirmation show material effects on:

- assets/infrastructure;
- staff;
- cash/debt;
- contracts/leases;
- licences;
- Lines/services;
- projects/orders;
- non-transferable/change-of-control obligations.

Physical vehicles/assets stay where they are.

Running Trips, cargo, construction and maintenance do not reset or teleport.

Only rights/obligations that may legally/business-wise transfer do so.

Historical company identity remains inspectable.

## 11. Infrastructure market

Infrastructure can be bought/sold as real physical assets.

An offer should expose the material known scope:

- seller;
- included assets;
- price;
- physical condition;
- existing leases/access rights;
- capacity commitments;
- active works/projects;
- important dependencies.

Buying infrastructure does not reset it or create capacity.

## 12. Existing rights survive ownership change where applicable

Buying a station, line or other infrastructure does not automatically cancel valid:

- guaranteed slots;
- leases;
- tenant rights;
- access agreements;
- service agreements;
- capacity commitments.

Ownership cannot be used to erase already contracted rights.

## 13. Partial asset sale

Allow partial sales, for example:

> sell track  
> keep depot

The review must expose newly created dependencies.

Example:

> Retained depot requires access over the railway being sold.  
> No post-sale access is secured.

The player can arrange access, change the sale or accept the consequence.

Do not create a free access right.

## 14. Distress opportunities

A distressed company can create concrete opportunities such as:

- stake for sale;
- company sale;
- depot/track/station sale.

Keep these tied to real companies/assets and obligations.

Do not create an abstract unlimited bankruptcy shop.

## 15. Save/load safety

Persist:

- ownership/control;
- subsidiary direction;
- active owner directives and progress;
- capital/asset transactions;
- acquisition/integration state;
- infrastructure transactions.

Save/load must not duplicate:

- shares;
- acquisition payments;
- owner directives;
- asset transfers;
- dividends/loans;
- infrastructure ownership changes.

It must not teleport assets or reset subsidiary AI response.

## 16. Acceptance evidence to collect

| ID | Required scenario |
|---|---|
| OWNUI-A01 | Buy a minority stake and verify financial/governance information without owner directives or operational control. |
| OWNUI-A02 | Obtain control. Subsidiary remains AI-managed and separate; no full direct-control/company-context mode appears. |
| OWNUI-A03 | Change a subsidiary Line through an owner directive. The subsidiary acquires/replans real dependencies itself and reports blockers without cheating. |
| OWNUI-A04 | Transfer a currently used vehicle to the parent. Show the shortage consequence, preserve physical location/state, and let subsidiary AI resolve the resulting fleet problem. |
| OWNUI-A05 | Give a simple growth/region/business-focus direction. AI decisions remain within that direction without dozens of separate policy controls. |
| OWNUI-A06 | Make capital contribution, dividend/distribution or intra-group loan. Money posts once to the correct separate ledgers. |
| OWNUI-A07 | Use group-owned workshop/infrastructure through real access/capacity rules; common ownership does not create physical capacity. |
| OWNUI-A08 | Integrate a controlled subsidiary with active Trips, debt, contracts and a non-transferable licence. No physical reset/teleport; incompatible rights remain explicit. |
| OWNUI-A09 | Buy infrastructure carrying third-party access/capacity rights. Applicable commitments survive ownership change. |
| OWNUI-A10 | Sell part of an infrastructure complex while retaining a dependent depot. Missing post-sale access is explicit and not invented. |
| OWNUI-A11 | Save/load with active owner directives, acquisition, asset transfer and infrastructure sale. No duplicate command/payment/ownership transition occurs. |
| OWNUI-A12 | Verify CZ/EN, enlarged UI, exact-object links and compact owner-level group overview. |

## 17. Decision record

| ID | Decision | Status |
|---|---|---|
| UI-D39 | Lightweight ownership/acquisition/infrastructure-market UI. Controlled subsidiaries always remain AI-managed; control provides a small set of owner interactions: broad direction, concrete owner directives, capital/asset transfer and major-company decisions. Subsidiary AI implements consequences through normal simulation. No full direct-control mode | CONFIRMED; refined on 2026-09-30 |

UI-D39 complements UI-D01–UI-D40. GAME_DESIGN Sections 29.1 and 39 own the canonical ownership/acquisition/infrastructure-market mechanics.
