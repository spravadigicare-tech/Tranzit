# Tranzit — Ownership, acquisitions and infrastructure market UI

> **Status: CONFIRMED UI DIRECTION — UI-D39, 2026-09-30.** The player accepted a lightweight ownership/acquisition model with materially deeper control over controlled subsidiaries. Minority ownership remains investment/governance rather than direct operational authority. A controlled company may remain autonomous, be strategically directed, or be opened in direct-control context using the same normal game systems in that company's name. Companies retain separate cash, obligations, licences, staff and assets until a real transfer/integration occurs. Whole-company integration is optional, not required to exercise control. Infrastructure remains a physical asset with inherited agreements, condition and operational dependencies. Exact legal/control thresholds, valuation formulas and transaction-pricing balance remain core/content work. This specification is not an implemented or tested UI.

Read with [GAME_DESIGN.md](GAME_DESIGN.md), especially Sections 29, 38–39; [UI_EXTERNAL_COMPANIES.md](UI_EXTERNAL_COMPANIES.md) for UI-D37; [UI_COMPANY.md](UI_COMPANY.md); [UI_FINANCE.md](UI_FINANCE.md); [UI_CAPACITY_ACCESS.md](UI_CAPACITY_ACCESS.md); [UI_CONSTRUCTION.md](UI_CONSTRUCTION.md); and [UI_UX_DESIGN.md](UI_UX_DESIGN.md). Acquisition never bypasses physical continuity, existing contracts, licences, debt, access rights or save/load identity.

## 1. Workspace

Primary entry:

**Company → Ownership and acquisitions / Firma → Vlastnictví a akvizice**

Use three practical views:

- **Our holdings / Naše podíly**
- **Companies / Firmy**
- **Infrastructure / Infrastruktura**

Contextual actions from UI-D37 company detail or an infrastructure asset open this same workflow already scoped to the selected target.

Do not build a deep stock-exchange simulator.

## 2. Ownership is not the same as control

Always distinguish:

- economic ownership percentage/share;
- governance/control rights;
- direct operational authority.

A minority stake can provide:

- dividends/distributions where applicable;
- ownership information the player is entitled to receive;
- governance/voting rights where defined;
- exposure to value/performance.

It does **not** automatically permit:

- editing the company's Lines;
- moving its vehicles;
- spending its cash;
- selling its infrastructure;
- changing staff;
- cancelling its contracts.

The UI shows the actual state, for example:

> Our holding: 20%  
> Control: none

or:

> Our holding: 65%  
> Control: yes

Do not hard-code one universal percentage threshold into presentation. Control follows the actual ownership/governance rules of the company/jurisdiction.

## 3. Buying shares or a stake

Shares/stakes are purchasable only when a real seller/transaction opportunity exists or the relevant owners are willing to negotiate.

Possible flows include:

- buy an offered block;
- make an offer for a specified stake;
- respond to a counteroffer;
- acquire a controlling block;
- acquire the whole company.

Example:

> 15% stake offered  
> Seller: founders of Morava Rail  
> Price: [money icon] 84,000  
> Our holding after purchase: 25%
>
> **Buy stake**

Or:

> Requested stake: 40%  
> Offer: [money icon] 220,000
>
> **Submit offer**

The counterparty can accept, reject or counter according to the actual company/ownership simulation.

No order book, short selling, derivatives, intraday chart or speculative trading minigame is required.

## 4. Acquisition review

Before buying a controlling stake or whole company, show what the player is actually acquiring.

A review can include, where known and applicable:

- purchase price;
- ownership percentage/control obtained;
- cash/debt position;
- vehicles/rolling stock;
- branches and facilities;
- owned infrastructure/land;
- active Lines/services;
- staff/management;
- leases;
- active contracts and agreements;
- current projects/orders;
- licences/permissions;
- material disputes/obligations.

Also show known change-of-control or non-transferable items.

Example:

> **Acquire Morava Rail**
>
> Purchase price: [money icon] 740,000
>
> Includes:
> 38 vehicles/rolling-stock assets  
> 3 depots  
> 2 owned stations  
> 61 km owned infrastructure
>
> Also inherits:
> debt [money icon] 112,000  
> 14 active contracts  
> 3 leases
>
> Needs attention:
> 1 licence may require replacement/recognition  
> 2 customer contracts contain change-of-control conditions

The transaction review respects UI-D37 information boundaries. Opening an acquisition flow does not reveal previously unknown private information unless the transaction/due-diligence rules legitimately provide it.

## 5. Controlled subsidiary modes

A controlled company remains one separate company identity unless integrated.

The player may operate it using three management modes.

### 5.1 Autonomous

The subsidiary continues to operate through its AI management within player-defined group constraints.

The player can set high-level policy such as:

- growth posture;
- investment budget;
- minimum cash reserve;
- debt limits;
- permitted regions/markets;
- permitted transport modes/business areas;
- whether acquisitions are allowed;
- whether major infrastructure sales require approval;
- dividend/distribution policy.

Routine operations remain delegated.

### 5.2 Managed / strategically directed

The subsidiary keeps routine management, but major plans and decisions can be proposed to or directly instructed by the player.

The player can, subject to the company's real authority/resources:

- approve/reject major new Lines;
- order expansion into a specific region;
- request a depot/station/infrastructure project;
- approve major fleet purchases;
- set fleet/service/tariff policies;
- start technology/research/adoption work;
- appoint/remove top management;
- set budgets and approval thresholds;
- require approval for large borrowing, acquisitions, infrastructure sales or other material actions.

The subsidiary may generate proposals such as:

> Expand Brno–Zlín  
> Investment: [money icon] 83,000  
> 2 additional trainsets  
> depot expansion  
> regional licence
>
> **Approve · Edit plan · Reject**

Approving uses the same real gameplay systems and constraints; it does not grant the required assets or rights for free.

### 5.3 Direct control

A controlled company can be opened in **direct-control context**.

The current-company selector makes the active command authority explicit, for example:

> Digicare Transport ▼  
> Morava Rail  
> Central Coaches

When Morava Rail is active, the normal interfaces operate on Morava Rail's authoritative state:

- Lines;
- Fleet;
- Duties;
- Finance;
- Branches;
- Staff/management;
- Construction;
- Procurement;
- Maintenance;
- Contracts;
- Technology;
- licences/market access.

The world is not reloaded. Only the company whose authority/resources the player is currently exercising changes.

Direct control does not merge the subsidiary into the parent.

## 6. Separate company economies

Every company retains its own:

- cash;
- debt;
- revenues/costs;
- contracts;
- licences;
- staff;
- vehicles;
- infrastructure;
- inventories;
- orders;
- reputation/history where applicable.

When directly controlling a subsidiary, the bottom-bar cash and company-scoped summaries show that company's money, not group-consolidated cash.

The parent cannot spend subsidiary cash, and the subsidiary cannot spend parent cash, unless a real intra-group transaction provides funds.

## 7. Intra-group finance

Controlled companies may use real intra-group financial transactions such as:

### Capital contribution

> Parent → subsidiary  
> [money icon] 50,000

Parent cash decreases and subsidiary cash increases according to the actual transaction/accounting rule.

### Intra-group loan

Show:

- lender/borrower;
- principal;
- rate/terms where applicable;
- repayment schedule;
- outstanding balance.

It remains a real receivable/liability, not free cash.

### Dividend/distribution

A controlled or minority-owned company may distribute funds where the financial/company rules permit.

Example:

> Distribution: [money icon] 20,000  
> Our ownership: 75%  
> Player company receives: [money icon] 15,000

Do not create dividend cash if the company cannot legally/economically make the distribution under the simplified finance rules.

## 8. Intra-group asset transfers

Assets can move between group companies only through an explicit valid transfer.

Supported forms can include, where applicable:

- sale;
- lease;
- capital contribution/transfer;
- other canonical ownership transfer.

For a vehicle transfer, show:

- current owner → new owner;
- price/terms;
- current physical location;
- current duty/commitment;
- effective transfer timing;
- agreements or rights that do/do not transfer.

Ownership transfer never teleports the asset.

A running vehicle remains physically where it is and its ongoing obligations must be resolved consistently before/through the effective transfer.

Use the same principle for depots, stations, track, land and other transferable assets.

## 9. Shared use without ownership transfer

Group membership does not automatically make every asset free/shared.

A subsidiary-owned workshop, station, depot, transport service or capacity can be used by another group company through a real agreement/access rule where appropriate.

Examples:

- maintenance agreement;
- depot/yard access;
- station/infrastructure capacity;
- vehicle lease;
- supply/service agreement;
- external transport;
- ticketing/partner arrangement.

These reuse the canonical agreement systems. Group ownership can affect commercial terms/policy, but it does not erase capacity or physical constraints.

## 10. Subsidiary management and authority

For controlled companies, the player can appoint/remove top management where governance rights allow it.

Use the existing management/delegation model for:

- budgets;
- purchase limits;
- contract limits;
- borrowing approval;
- acquisition approval;
- infrastructure sale approval;
- region/market expansion authority;
- operational policy.

Example:

> CEO: Karel Beneš
>
> May:
> buy vehicles up to [money icon] 20,000  
> sign routine contracts  
> adjust Lines
>
> Requires parent approval:
> enter a new country  
> borrow above [money icon] 50,000  
> buy/sell infrastructure  
> acquire another company

Do not create a second unrelated manager-policy system for subsidiaries.

## 11. Group overview

Once the player owns stakes in multiple companies, Company UI provides a compact group view.

Example:

> **Our group**
>
> Digicare Transport  
> ├ Morava Rail — 100%, controlled  
> └ Central Coaches — 65%, controlled
>
> Minority investments  
> Bohemia Logistics — 18%

Show:

- ownership;
- control status;
- management mode;
- major issue/decision;
- current financial/operating summary where entitled;
- direct link to company detail or direct-control context.

Avoid a mandatory complex organizational-chart editor.

## 12. Company integration

A controlled subsidiary can optionally be **integrated into the parent** where allowed.

Integration is a real organizational/legal transition, not merely changing the selected-company dropdown.

Before confirming, show effects on:

- vehicles/assets;
- infrastructure/land;
- staff;
- debt;
- contracts;
- leases;
- licences/permissions;
- Lines/services;
- active projects/orders;
- cash/inventories;
- names/identity/history;
- non-transferable/change-of-control items.

Physical assets remain in place.

Running Trips, cargo, construction and maintenance do not teleport/reset.

Contracts/licences transfer only where their real rules permit it. Items requiring consent/reapplication remain explicit dependencies/problems.

Historical identity remains inspectable after integration.

## 13. Infrastructure market

Infrastructure can be bought/sold as real physical assets.

Examples include:

- station/terminal;
- depot/workshop;
- track/corridor;
- yard;
- land/site;
- infrastructure complex;
- supported partial asset package.

An offer shows:

- seller;
- exact included asset scope;
- price;
- ownership;
- physical condition;
- relevant maintenance state;
- active leases/access agreements;
- capacity commitments;
- projects/work orders;
- legal/access constraints;
- dependencies affecting the buyer.

Buying infrastructure does not create new capacity or reset its current state.

## 14. Existing third-party rights survive sale where applicable

Buying an infrastructure owner/asset does not automatically cancel:

- guaranteed slots;
- leases;
- tenant rights;
- access agreements;
- construction commitments;
- service agreements;
- easements/connection rights;
- other binding obligations.

Example:

The player buys a station with competitor guaranteed calls.

Those valid calls remain protected according to their agreements.

Ownership is not a button to evict competitors from already contracted capacity.

## 15. Partial asset sale

Support partial sales such as:

> sell track  
> keep depot

The review must expose dependencies created by the proposed split.

Example:

> After sale, retained Brno depot requires access over the sold railway section.  
> No post-sale access agreement is currently secured.

The player can then:

- arrange retained access;
- change sale scope;
- cancel the proposed transaction.

Do not allow the UI to silently create access just to make the sale feasible.

## 16. Selling player-owned assets

From a player-owned infrastructure detail, **Sell** opens the same canonical asset-sale workflow.

Show:

- proposed buyer;
- offered price;
- exact ownership scope;
- active contracts/leases/access;
- player Lines/facilities depending on the asset;
- post-sale rights, if any;
- debts/security/other applicable encumbrances.

A sale remains a proposal until explicitly accepted.

## 17. Distress and acquisition opportunities

A distressed external company may create real opportunities such as:

- offered assets;
- offered ownership stake;
- owner seeking a controlling buyer;
- restructuring transaction.

Do not create an abstract unlimited “bankruptcy shop”.

The opportunity remains tied to concrete company/asset identities and their real obligations/state.

## 18. Save/load and identity safety

Persist:

- ownership percentages/rights;
- control state;
- subsidiary management mode;
- group policies/approval limits;
- intra-group loans/transfers;
- acquisition proposals;
- accepted acquisitions;
- integration state;
- infrastructure-sale proposals/transactions.

Save/load must never:

- duplicate shares;
- duplicate acquisition payment;
- transfer an asset twice;
- merge cash ledgers accidentally;
- reset subsidiary AI policy;
- restart completed integration;
- lose inherited contracts/rights;
- teleport transferred physical assets.

## 19. Acceptance evidence to collect

| ID | Required scenario |
|---|---|
| OWNUI-A01 | Buy a minority stake and verify dividends/governance information without direct operational control or access to private subsidiary commands. |
| OWNUI-A02 | Obtain actual control and switch the company between Autonomous, Managed and Direct control without changing ownership or merging ledgers. |
| OWNUI-A03 | Direct-control a subsidiary and use normal Line/Fleet/Finance/Construction/etc. UI against that company's separate cash/assets/contracts. Switching back leaves both companies' authority/state intact. |
| OWNUI-A04 | Set subsidiary strategy, budget and approval thresholds; AI management operates within them and surfaces material proposals without inventing resources. |
| OWNUI-A05 | Make capital contribution, intra-group loan and dividend/distribution. Cash/debt/receivables post exactly once to the correct company ledgers. |
| OWNUI-A06 | Transfer/lease a vehicle between group companies while it has a physical location/current duty. Ownership changes only through the real transaction and the asset never teleports/duplicates. |
| OWNUI-A07 | Use a subsidiary workshop/infrastructure from another group company via a real agreement. Group ownership does not bypass physical capacity/access. |
| OWNUI-A08 | Integrate a controlled subsidiary with active vehicles, Trips, staff, debt, contracts and a non-transferable licence. Assets remain physical; eligible obligations transfer once; the incompatible licence remains an explicit issue. |
| OWNUI-A09 | Buy infrastructure carrying third-party guaranteed access and active maintenance/construction state. All applicable obligations/state survive the ownership change. |
| OWNUI-A10 | Sell part of an infrastructure complex while retaining a dependent depot. UI identifies loss of access and does not create a free post-sale right. |
| OWNUI-A11 | Save/load during stake acquisition, group transfer, infrastructure sale and integration. No duplicate share, money posting, ownership transfer or asset occurs. |
| OWNUI-A12 | Verify CZ/EN, enlarged UI, exact-object links and UI-D34 money display across holdings, acquisitions, transfers and group overview. |

## 20. Decision record

| ID | Decision | Status |
|---|---|---|
| UI-D39 | Lightweight ownership/acquisition/infrastructure-market UI with separate ownership versus control; controlled subsidiaries can be autonomous, strategically managed or directly controlled through the normal company UI; company economies remain separate; explicit intra-group finance/assets/access and optional real integration preserve physical/contracts/licence continuity | CONFIRMED on 2026-09-30 |

UI-D39 complements UI-D01–UI-D38. GAME_DESIGN Sections 29.1 and 39 own the canonical ownership/acquisition/infrastructure-market mechanics.
