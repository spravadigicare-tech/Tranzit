# Tranzit — New Game and company founding UI

> **Status: CONFIRMED UI DIRECTION — UI-D35, 2026-09-30.** The player accepted a short New Game setup followed by a real in-world company founding flow. New Game chooses only campaign/company-level inputs; it does not grant a branch, fleet, depot, activity licence or customers. The optional tutorial/onboarding checklist exists only for the opening company-founding phase and ends after the first functioning transport operation. Tutorial mode can be Full / Basics only / Off. Normal blockers, Needs attention and contextual explanations remain part of the game regardless of tutorial mode. Exact visual dimensions, wording and tutorial copy remain implementation/content work. This is not an implemented or tested UI.

Read with [UI_UX_DESIGN.md](UI_UX_DESIGN.md), especially UI-D04, UI-D06, UI-D09, UI-D15, UI-D20, UI-D22, UI-D24, UI-D33 and UI-D34. [GAME_DESIGN.md](GAME_DESIGN.md), especially Sections 2.4, 3.5, 7.1–7.5 and 38.1, owns start-year initialization, market-entry rights, first branch, founding loans and licences. [V1_SCOPE.md](V1_SCOPE.md) owns the first-playable restriction to the 1900 preset.

## 1. Two separate phases

Keep two concepts distinct:

1. **New Game setup** — choose campaign/company-level starting inputs.
2. **Company founding in the world** — spend real money, establish the first physical branch, staff it, obtain licences, secure vehicles/facilities and launch the first real operation.

New Game does not pre-buy or pre-build operational assets.

## 2. New Game setup

The New Game flow should remain short.

Primary choices:

- start year;
- starting region;
- founding-loan tier;
- company identity;
- tutorial level.

For first-playable V1, only **1900** is selectable. The UI may already be structured to support later 1925 / 1950 / 1975 presets when they become available, but disabled future presets must not pretend they are playable.

Do not ask the player to choose a permanent transport archetype such as Rail / Road / Freight / Passenger.

## 3. Starting-region selection

Select the starting region from a map/world overview rather than a text-only difficulty menu.

A region detail can show public, date-appropriate facts such as:

- major cities;
- population/economic context;
- major industry;
- existing road/rail infrastructure;
- known public operators/competitors;
- public setup/legal information;
- publicly advertised tenders where allowed;
- broad market characteristics.

Example:

> **Bohemia · 1900**
>
> Basic market-entry right: included  
> Major cities: Praha, Plzeň, České Budějovice  
> Existing rail network: extensive  
> Road network: developing  
> Known carriers: 7
>
> **You receive**
> the company's basic business/market-entry right in the starting region
>
> **You do not receive**
> a branch, vehicles, depot, activity licence, customers or infrastructure capacity

Do not label regions Easy / Hard or rank them for the player. Show relevant facts and let the player decide.

Before the first branch exists, public/world knowledge is visible, but ordinary hidden local opportunities remain subject to the commercial-coverage rules.

## 4. Founding-loan selection

Show the three canonical founding-loan tiers as comparable cards:

- Small;
- Standard;
- Large.

For each, show:

- immediate cash received;
- principal owed;
- interest rate;
- repayment frequency;
- scheduled instalment;
- maturity/end;
- estimated total repayment under agreed terms.

Use UI-D34 compact money icon + localized amount.

Do not label the larger loan as a higher difficulty. Choosing a larger tier changes financing/cash/debt only; it does not alter AI intelligence, demand, reputation or opportunity quality.

The values are content/balance data and can depend on the start year/economy.

## 5. Company identity

Keep identity setup lightweight.

At minimum:

- company name;
- optional short display name/initials where useful;
- company visual identity options already supported by the art/UI system.

Do not turn founding into a logo editor or legal-form simulator unless separately approved.

Changing identity presentation does not change business mechanics.

## 6. Tutorial level

New Game provides:

- **Full / Plný**
- **Basics only / Jen základ**
- **Off / Vypnuto**

### Full

Shows the complete opening founding checklist and contextual first-use guidance for the key startup workflows.

### Basics only

Shows only the minimum founding path and essential explanation of the major object types/workflows.

### Off

No tutorial checklist or first-use tutorial prompts.

Even with tutorial Off, the game still shows:

- real readiness blockers;
- Needs decision incidents;
- invalid-action explanations;
- required confirmation/consequence previews;
- tooltips/help under UI-D15;
- legal/physical/financial constraints.

These are normal interface/gameplay information, not tutorial content.

Tutorial settings can be changed later without modifying the simulation state.

## 7. Confirm company creation

Before confirming, show a concise summary:

> Start: Bohemia · 1900  
> Company: [name]  
> Founding loan: Standard  
> Starting cash: [money icon] …  
> Debt: [money icon] …  
> Tutorial: Full

The confirmation must state clearly that the player starts with **no branch, no fleet and no operating licence**.

Creating the company:

- creates the company identity;
- creates the selected founding loan/debt;
- posts the starting cash;
- grants the starting-region basic market-entry right;
- initializes the campaign/world at the selected date.

It does not create any operating asset or customer contract.

Repeated confirmation cannot create duplicate starting loans/cash.

## 8. Entering the world

After creation, load the normal world and start **paused**.

The player owns only what New Game actually created.

Open a small non-blocking onboarding card when tutorial mode requires it:

> **Build your company**
>
> You do not yet have an operational branch.
>
> Establish your first physical office to begin normal local commercial activity.
>
> **Choose branch location**

The world remains fully inspectable. The player can:

- move/rotate/zoom the camera;
- inspect cities;
- inspect public companies/operators;
- inspect public infrastructure;
- inspect public licence requirements;
- inspect publicly known market information.

Do not trap the player in a full-screen mandatory tutorial wizard.

## 9. First branch selection

The first branch must use the real branch/premises systems.

Possible contextually valid paths include:

### Rent office space

Show:

- upfront/setup cost;
- recurring rent;
- available office capacity;
- start/readiness time;
- landlord/agreement.

### Build a small owned branch

Show:

- site/land requirement;
- construction/setup cost;
- expected completion;
- future physical expansion possibilities;
- required permits/project dependencies.

### Use office space at a transport hub

Only where a real suitable owner/site offer exists.

Show:

- hub;
- owner;
- available office module/space;
- recurring/upfront terms;
- actual agreement/access requirements.

Selecting a city alone does not create the branch.

## 10. Founding checklist

The opening checklist uses real game states and links directly to canonical workflows.

Example:

> **Company not yet ready for transport operation**
>
> Branch — under setup  
> Branch director — missing  
> Office staff — below minimum  
> Activity licence — none selected  
> First commercial opportunity — available after coverage activates  
> Vehicle/operating facilities — none

Each row opens the existing real workflow:

- Branch → UI-D20 / construction/rental;
- Director/workforce → UI-D20;
- Licence → UI-D33;
- Vehicle acquisition → UI-D22;
- Depot/facility → UI-D16 / agreements;
- Opportunity → UI-D17;
- Finance → UI-D19.

There is no separate tutorial inventory, fake starter market or free tutorial asset.

## 11. Non-linear founding

The checklist is not a wizard.

The player may:

- inspect/buy a vehicle before the branch completes;
- inspect licence requirements early;
- lease a depot before accepting a job;
- research rail access before deciding between road and rail;
- prepare several options while paused.

A real accepted purchase/agreement remains binding even if the player changes their startup plan.

Hard dependencies only block the action that actually requires them.

## 12. Recommendations without forced specialization

The tutorial can present one or more **example viable paths**, not mandatory classes.

For example:

> **One possible path to first revenue**
>
> establish branch  
> obtain Road Freight licence  
> accept a small local job  
> acquire/lease compatible vehicle  
> secure parking/service  
> launch transport

The player can ignore this and pursue passenger rail, road passenger, mixed operation or another feasible combination.

Recommended plans must use the same real prices, assets, licences, sellers and availability as manual play. They do not grant free or reserved resources.

## 13. Public information before the first branch

Before normal commercial coverage exists, the player must still be able to make an informed branch/location decision using plausible public information.

Allow, where public/known:

- cities/population;
- major industry/economic context;
- existing roads/rail/stations;
- public operators/services;
- public licence/permit costs and requirements;
- available office/premises offers;
- vehicle/dealer/public marketplace basics where the company is legally allowed to inspect/buy;
- publicly advertised tenders/direct opportunities allowed by existing discovery rules.

Do not reveal hidden routine local private opportunities merely because the user opened New Game or selected a city.

## 14. When the tutorial ends

The opening tutorial/checklist is **temporary**.

It completes after the player reaches a first genuine functioning transport operation with the required founding prerequisites satisfied.

The completion condition should use real states, approximately:

- first active branch/commercial presence;
- required accountable branch management/staff present;
- relevant activity licence/right valid;
- required vehicle/facility/access dependencies valid;
- first real Line/Trip or accepted job has entered functioning operation.

Do not require one specific transport mode or exact tutorial sequence.

Then show a brief completion state:

> **Company operational**
>
> Your first transport operation is running.

After completion, remove the startup checklist from the normal interface.

Do not keep telling the player to buy a second vehicle or expand to another city.

## 15. Normal attention after tutorial

Once founding onboarding ends, the game relies on normal systems:

- UI-D24 Needs decision / events;
- company/workforce warnings;
- Line/Trip readiness;
- maintenance/procurement alerts;
- licence/contract renewal;
- opportunities and map analysis.

These are not tutorial steps.

If the company later loses its last branch or all operations stop, do not restart the New Game tutorial automatically.

## 16. First-use contextual guidance

In Full/Basics tutorial modes, selected complex systems can display concise first-use guidance the first time they are opened, for example:

- Capacity Order;
- Line/Pattern distinction;
- integrated tariff system;
- vehicle duties.

This guidance is presentation only and can be dismissed.

It cannot:

- pause/resume unless the player manually pauses;
- alter settings/values;
- submit orders;
- accept agreements;
- change game state.

The player can disable future tutorial guidance globally.

## 17. Save/load and onboarding persistence

Persist:

- tutorial level;
- completed/seen onboarding steps;
- dismissed first-use guidance;
- whether company-founding tutorial has completed;
- actual company/branch/licence/asset state independently.

After save/load:

- completed startup tutorial does not restart;
- a partially completed founding checklist resumes from actual state;
- a purchase made before save remains purchased rather than being granted again by the tutorial;
- tutorial Off remains Off;
- changing tutorial level does not alter the campaign.

The checklist derives completion from canonical state where practical rather than trusting a duplicated tutorial-only state flag.

## 18. Acceptance evidence to collect

| ID | Required scenario |
|---|---|
| NEWUI-A01 | Start V1 New Game and verify only 1900 is selectable; choose region, company identity and each founding-loan tier without selecting a permanent transport archetype. |
| NEWUI-A02 | Confirm a new company. World opens paused with starting cash/debt/basic market-entry right but no branch/fleet/depot/activity licence/customer/slot. Repeated confirmation cannot duplicate cash/debt. |
| NEWUI-A03 | Before first branch, inspect public city/infrastructure/licence/premises information while normal hidden local private opportunities remain undiscovered. |
| NEWUI-A04 | Establish the first branch through rent, owned construction or real hub-space offer where available. Setup/lease/construction remains a real agreement/project and branch benefits do not appear early. |
| NEWUI-A05 | Complete founding in a non-recommended order and with different transport modes. The checklist follows real state rather than forcing sequence or granting free resources. |
| NEWUI-A06 | Compare Full / Basics only / Off. Tutorial content changes, while blockers, decision incidents, invalid-action reasons and consequence confirmations remain present in all modes. |
| NEWUI-A07 | Complete the first real operation. Startup checklist ends and does not later instruct the mature company to buy/expand. Normal Needs attention remains active. |
| NEWUI-A08 | Save/load during partial founding and after tutorial completion. Actual purchases/agreements/onboarding state persist with no replayed loan, branch, licence or asset. |
| NEWUI-A09 | Verify CZ/EN, enlarged UI, keyboard access and UI-D34 money icon throughout region/loan/branch setup; accessibility text still identifies amounts as money. |

## 19. Decision record

| ID | Decision | Status |
|---|---|---|
| UI-D35 | Short New Game setup followed by real in-world company founding; no free operational assets or mode archetype; optional Full/Basics/Off opening tutorial that ends after first functioning transport operation while normal blockers/attention systems remain permanent | CONFIRMED on 2026-09-30 |

UI-D35 complements UI-D01–UI-D34. GAME_DESIGN Sections 7.1–7.5 and 38.1 remain authoritative for company founding mechanics.
