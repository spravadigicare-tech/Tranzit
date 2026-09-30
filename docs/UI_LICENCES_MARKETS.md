# Tranzit — Licences, permits and market-entry UI

> **Status: CONFIRMED UI DIRECTION — UI-D33, 2026-09-30.** The player accepted one company workspace for market-entry rights, activity licences, specific permits/approvals and active applications. The UI must keep legal market entry, activity licensing, local commercial presence and physical infrastructure access distinct; show requirements and critical-path readiness without paperwork micromanagement; and expose public-authority agreements through the same stable agreement model used elsewhere. Exact visual dimensions, localized labels and balancing values remain design/content work. This specification is not an implemented or tested UI.

Read with [UI_UX_DESIGN.md](UI_UX_DESIGN.md), especially UI-D09, UI-D15, UI-D17, UI-D20, UI-D24, UI-D26–UI-D28 and UI-D32. [GAME_DESIGN.md](GAME_DESIGN.md), especially Sections 2.4, 7.2, 7.5, 19, 33 and the relevant contract/permit rules, owns market entry, commercial coverage, licences, concessions, permissions and infrastructure access. This document defines presentation only.

## 1. Entry and purpose

Use **Company → Licences and expansion / Firma → Licence a expanze** as the primary workspace.

Provide four main views:

- **Markets and regions / Trhy a regiony**
- **Licences / Licence**
- **Permits / Povolení**
- **Applications / Žádosti**

The workspace answers:

1. Where may the company legally conduct business?
2. Which regulated activities may it perform in each jurisdiction?
3. Which narrower permits/approvals are needed for specific operations?
4. Which applications are pending and what blocks the planned operation?

Do not collapse these into one generic “unlocked region” flag.

## 2. Markets and regions

The Markets and regions view shows where the company has valid **market-entry/business rights** and where expansion is still required.

Example:

> **Bohemia**
>
> Market-entry right: Active  
> Commercial presence: Praha, Plzeň  
> Road passenger licence: Active  
> Rail passenger licence: Active  
> Rail freight licence: Missing
>
> **Austria**
>
> Market-entry right: Missing  
> Local branch/presence: None  
> Existing home licences: not sufficient for this jurisdiction
>
> **Review market entry**

Keep these concepts separate:

- market-entry/business right;
- commercial coverage/local presence;
- activity licence;
- municipal/local concession;
- physical station/route/facility access;
- infrastructure capacity/slots.

One does not imply another.

## 3. Market-entry detail

Opening a prospective market shows the actual current authority offer/requirements rather than a generic unlock price.

Illustrative presentation:

> **Expansion into Austria**
>
> Market-entry offer  
> Scope: Wien + Niederösterreich  
> Entry fee: [money icon] 42,000  
> Term: long-term
>
> Requirements  
> Financial standing — met  
> Reputation requirement — met  
> Local commercial presence before operation — required  
> Rail passenger activity licence — missing
>
> **This grants**
> business/market-entry rights in the stated scope
>
> **This does not grant**
> infrastructure capacity, stations, vehicles, customers, operating licences or local concessions

The example amount is illustrative only.

A market-entry right must never be presented as if it automatically activates the region’s full operating capability.

## 4. Alternative authority terms

Where the existing market-entry mechanics allow different negotiated conditions, show them as comparable concrete offers/terms.

Illustrative options:

> **Option A**  
> Higher entry fee  
> no additional investment commitment
>
> **Option B**  
> Lower fee  
> obligation to establish a local branch
>
> **Option C**  
> Broader territorial scope  
> infrastructure/public-service commitment required

Do not implement this as a technology-tree unlock.

Every option must show:

- authority/counterparty;
- geographic scope;
- upfront and recurring cost;
- validity;
- mandatory commitments;
- deadlines;
- local-presence requirements;
- renewal/termination where applicable;
- consequence of failing an accepted commitment.

An accepted option becomes a real agreement with stable identity.

## 5. Activity licences

The Licences view shows regulated transport/activity permissions separately from market entry.

Example:

> **Rail passenger operation**
>
> Bohemia: Active  
> Austria: not recognized / missing
>
> Enables: rail passenger operation in covered jurisdiction  
> Does not include: infrastructure/station capacity or municipal concessions
>
> **Austria requirements**
>
> Financial standing — met  
> Insurance — met  
> Qualified responsible manager — missing  
> Technical/maintenance capability — met
>
> Application fee: [money icon] 18,000  
> Expected processing: approximately 6 game days
>
> **Apply · Open manager requirement**

The player does not manually fill forms or carry bureaucratic document items.

## 6. Licence matrix

For a multi-region company, provide a compact matrix by activity and jurisdiction.

Example:

| Activity | Bohemia | Austria | Saxony |
|---|---|---|---|
| Road freight | Active | Missing | Active |
| Road passenger | Active | Missing | Missing |
| Rail freight | Missing | Application pending | Active |
| Rail passenger | Active | Missing | Missing |

Clicking a cell opens the exact jurisdiction/activity detail.

The matrix is navigation, not a replacement for requirement detail.

Do not imply that one national licence automatically applies across all jurisdictions unless the actual recognition rules say so.

## 7. Specific permits and approvals

Specific permits are narrower than activity licences.

Examples can include, where applicable:

- oversized/special road movement;
- dangerous-goods movement;
- exceptional route approval;
- vehicle approval in a jurisdiction;
- construction/demolition permit;
- temporary event operation;
- specific municipal stop/route approval;
- other canonical project/operation approvals.

Use views such as:

- Active
- Pending
- Needs attention
- History

Do not force the player to browse hundreds of irrelevant permits.

Most specific permits should surface contextually from the operation that needs them.

## 8. Contextual permit request

When a plan encounters a missing permit, explain it in place and link into this workspace.

Example:

> **Missing oversized-movement permit**
>
> Route: Brno → Ostrava  
> Expected processing: 2 game days  
> Fee: [money icon] 320
>
> **Apply**

The request should be prefilled from the actual movement/project.

Applying does not guarantee approval before the planned date; the planner uses the pending status/estimated processing in readiness.

If another contracted provider is legally responsible for the permit, show that responsibility rather than making the player apply twice.

## 9. Applications view

Provide one practical list of administrative processes currently underway.

Example:

> **4 active applications**
>
> Rail Freight Licence — Austria  
> expected decision: ~4 days
>
> Depot construction permit — Brno  
> waiting for municipal authority
>
> Special movement permit — Plzeň  
> expected decision: today
>
> Market entry — Niederösterreich  
> awaiting player acceptance of authority terms

Each row shows:

- application type;
- issuing authority;
- scope;
- submitted date;
- current state;
- expected processing date/range where supported;
- missing requirement or requested response;
- fee/payment state;
- dependent Line/contract/project/vehicle;
- next player action only when one is truly required.

Do not create one notification per day merely because an application remains pending.

## 10. Critical-path readiness

Line, Contract and Construction planners should use these same legal dependencies in their readiness calculations.

Example:

> **Planned start: Day 12**
>
> Market-entry right — secured  
> Austrian rail-passenger licence — pending, estimated Day 9  
> Wien branch — under construction, estimated Day 11  
> infrastructure access — secured  
> fleet — ready
>
> **Earliest currently supported readiness: Day 11**
>
> Risk: licence decision date is estimated, not guaranteed.

Do not replace this with “4/5 requirements complete”.

Show:

- which dependency is on the critical path;
- whether its date is firm, expected or unknown;
- whether the missing item blocks bidding, activation or only later operation;
- what action can change the outcome.

## 11. Licence expiry, renewal and suspension

A live licence/permission shows:

- effective date;
- expiry, if any;
- Auto-renew availability/state where applicable;
- renewal application deadline;
- current compliance requirements;
- dependent objects.

Example:

> **Rail Passenger Licence**
>
> Expires in 9 days
>
> Used by:  
> 6 Lines  
> 41 future Trips  
> 2 public-service contracts
>
> Renewal: new application required
>
> **Renew · Show dependencies**

Turning off Auto-renew does not cancel the active term.

If a licence becomes invalid, dependent operations receive a legal blocker according to the owning lifecycle/recovery rules. Do not silently delete Lines, Trips, vehicles or contracts.

A running movement already in progress follows the applicable safe/legal recovery rules rather than teleporting or vanishing.

## 12. Explainable approval/refusal

Administrative outcomes must expose the actual reason.

Examples:

> **Application refused**
>
> Required financial standing is not met.

or:

> **Conditionally approved**
>
> Operation may begin only after a qualified responsible manager is appointed.

Do not use unexplained random refusal probabilities.

Where uncertainty exists, it should come from actual authority capacity, competition/concession rules, changing requirements or another modeled factor and remain explainable.

## 13. Authorities as counterparties

Public authorities can be:

- market-entry grantors;
- licence/permit issuers;
- municipal transport authorities;
- public customers;
- infrastructure/facility owners;
- concession grantors;
- construction/land authorities.

Their detail should expose **Our agreements / Naše dohody** using the same stable agreement principles as UI-D27/UI-D28.

For example, an authority relationship can contain:

- market-entry agreement;
- rail-passenger licence;
- municipal concession;
- public-service contract;
- station/infrastructure-access agreement;
- active/past permit/application.

These remain distinct objects. Do not collapse the entire relationship into one universal “relationship with Austria” agreement or score.

## 14. Costs and money display

Application fees, entry fees, recurring charges and financial requirements use the global money presentation rule in UI-D34:

- compact amount: neutral money icon + localized number;
- no real-world currency symbol;
- tooltip/accessibility text identifies the unit as **money**;
- full explanatory text may write “money” where needed for clarity.

The icon is presentation shorthand only. It does not create a second currency or historical exchange-rate system.

## 15. Region activation and information boundaries

Market entry and detailed world activation are related but not identical.

An inactive/macro region does not become fully simulated merely because the player inspects its licence page.

When actual market-entry/activation conditions are met, instantiate/activate the region through the existing GAME_DESIGN rules at the current historical date.

Before entry, the player may see public/negotiable setup information that the company can plausibly know, but not hidden local private opportunities or exact competitor commitments.

## 16. Save/load and state safety

Persist stable identities and states for market-entry agreements, licences, permits and applications through the owning systems.

After save/load:

- pending applications do not submit twice;
- paid fees are not charged again;
- approved licences remain approved;
- expired licences remain historical;
- a conditional approval retains its unmet condition;
- dependencies reconstruct against the same Line/contract/project;
- a refusal does not reroll simply because the save was loaded.

Opening, filtering or inspecting requirements does not submit an application, accept an authority offer or pay a fee.

## 17. Acceptance evidence to collect

| ID | Required scenario |
|---|---|
| LICUI-A01 | Inspect one home region and one new jurisdiction. Market entry, local commercial coverage, activity licence and physical infrastructure access remain visibly distinct. |
| LICUI-A02 | Compare multiple market-entry terms with different fee/scope/local-presence/public-service commitments. Accepting one creates only its explicit rights/obligations and no free licence/slot/customer. |
| LICUI-A03 | Use the licence matrix for several activities/jurisdictions and open exact requirement details. Recognition/local-equivalent rules are not hidden behind one global unlock. |
| LICUI-A04 | Submit an activity licence with one missing responsible-manager requirement. Pending/conditional/refused/approved states expose actual reasons and never rely on opaque RNG. |
| LICUI-A05 | Trigger a contextual special permit from a vehicle/project/operation. The application is prefilled, appears in the central Applications list and does not duplicate when reopened. |
| LICUI-A06 | Build an international Line whose critical path includes licence, branch and infrastructure access. Earliest readiness and uncertainty reconcile with the canonical dependencies rather than a completion percentage. |
| LICUI-A07 | Approach licence expiry with several Lines/Trips/contracts dependent on it. Renewal/non-renewal/suspension preserves objects/history and creates legal blockers rather than deleting operations. |
| LICUI-A08 | Inspect a public authority that is simultaneously licence issuer, customer and infrastructure owner. Our agreements exposes distinct canonical objects without merging them or leaking unrelated private data. |
| LICUI-A09 | Save/load with pending applications, paid fee, conditional approval and an expiring licence. No duplicate submission/payment or rerolled decision occurs. |
| LICUI-A10 | Verify CZ/EN, enlarged UI, neutral money-icon display and keyboard-accessible explanation of the accounting unit. No real-world currency symbol appears. |

## 18. Decision record

| ID | Decision | Status |
|---|---|---|
| UI-D33 | Company Licences and expansion workspace with Markets and regions / Licences / Permits / Applications, strict separation of market entry, commercial coverage, activity licences and physical access, contextual permit requests and critical-path readiness | CONFIRMED on 2026-09-30 |

UI-D33 complements UI-D01–UI-D32. GAME_DESIGN Sections 2.4 and 7.5 remain authoritative for market entry and licensing mechanics.
