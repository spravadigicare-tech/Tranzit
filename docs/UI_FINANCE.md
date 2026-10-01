# Tranzit — Company finance UI

> **Status: CONFIRMED UI DIRECTION — UI-D19, 2026-09-30.** The player accepted a compact finance overview, task-based cards, direct inspection of the source of important figures, consistent reporting periods and a strict distinction between uncommitted plans, binding commitments and actual payments. Exact visual tokens, column widths and localized labels remain design work. This is not an implemented or tested UI.

Read with [UI_UX_DESIGN.md](UI_UX_DESIGN.md), particularly UI-D07 (floating windows), UI-D09 (object links), UI-D15 (minimalism/tooltips) and the shared pause rules. [GAME_DESIGN.md](GAME_DESIGN.md), Sections 3.4, 7.1 and 38, owns financial time units, founding loans and simple finance/failure mechanics. Contract, asset, construction and operating specifications own the transactions being reported. [CONTRACT_CANCELLATION.md](CONTRACT_CANCELLATION.md) owns applicable settlement rules. This document defines presentation, not a new accounting, banking, tax or securities simulation.

## 1. One finance workspace

Open the same **Finance / Finance** window through **Company / Firma** or by clicking the company's cash/current-period result in the **upper-left HUD** under UI-D41. Reuse/focus the existing matching view rather than creating an unrelated second dashboard. Keep normal movement, resizing, pinning, minimize/restore and map access.

The overview answers three questions: **How much cash is available now? What is generating or consuming money? What will the company have to pay?** Keep a compact visible summary, explanations on hover/keyboard focus and complete breakdowns on click. Do not expose every transaction or calculation on the default screen.

Always identify the company, selected reporting period and forecast horizon where applicable. Cash is a point-in-time balance; operating results describe a period; upcoming payments describe future due dates. Do not present the three as values for one indistinguishable time basis. Amounts use authoritative exact integer/fixed-point `money` values and localized number formatting. Under UI-D34, compact player-facing amounts use the dedicated neutral money icon rather than repeating the word `money`; tooltips/focus/accessibility and text-only or ambiguous contexts still identify the unit as `money`. No real-world currency symbol is used.

## 2. Visible summary and warnings

| Summary | Required meaning |
|---|---|
| Cash now / Peníze | Actual current company cash. Expected receipts, unused borrowing possibilities, asset values and draft funding are not already cash. Where an existing rule restricts funds, distinguish the cash balance from the spendable portion instead of inventing a new reservation mechanic. |
| Result for period / Výsledek za období | Revenue/cost or operating-cash-flow result from the existing reporting model, with an explicit label and period. Operating result, net cash movement and forecast are different measures; show their basis on inspection rather than using the terms interchangeably. |
| Upcoming commitments / Nejbližší závazky | Remaining payable amounts from accepted agreements/orders, with the next due dates and a stated look-ahead horizon. Forecast operating expenses and draft estimates are separately identified. |

Below these values, surface a specific material risk and a route to its sources. For example: an upcoming accepted construction instalment may leave insufficient cash for known operating payments. This is an illustrative warning, not a new hard reserve threshold or an automatic insolvency verdict.

Explain the affected payment dates, known obligations and assumptions. A cash projection that depends on customer payment or future sales must say so. Unknown timing or amount is not zero. A loss, one late payment and an exhausted cash balance must not all collapse into the same unexplained red score.

Use existing financial-distress and critical-incident rules. A forecast warning does not automatically declare bankruptcy, halt all operations, borrow money or sell assets. Critical auto-pause follows UI-D08; opening the financial view or making a forecast visible never creates a second incident.

## 3. Openable task cards

Use five compact functional groups, with a useful summary and direct access to detail. They are independently accessible, not wizard steps.

| Card | Content |
|---|---|
| Revenue and costs / Výnosy a náklady | Actual reported sources of income and expense: transport, vehicle operation, staff, infrastructure, maintenance and other existing categories. Distinguish operating cash flow, financing and investment movements rather than treating every receipt as earned revenue. |
| Payments and commitments / Platby a závazky | Paid transactions, outstanding obligations, due dates and expected incoming payments, linked to the relevant agreements/orders. Separate posted payments, unpaid bills, committed future payments and estimates. |
| Loans / Půjčky | Each real loan, outstanding principal, repayment schedule, interest and disclosed conditions. Access existing borrowing/repayment actions without creating an additional credit product. |
| Investments and plans / Investice a plány | Started projects, confirmed vehicle purchases and other accepted investments, with already-paid, remaining committed and estimated amounts. Unlaunched construction/Line plans appear separately as nonbinding scenarios. |
| Operating results / Výsledky provozu | Comparable results for Lines, contracts or facilities over the selected period, with access to the underlying revenues, costs and objects. These are alternative analytical views, not independent totals to add together. |

Keep filter/sort controls predictable and only show relevant secondary fields on expansion. Adapt the cards and tables to smaller windows and enlarged Czech/English UI. Essential amounts, units, periods, active filters and negative signs cannot disappear through clipping or decorative formatting.

## 4. From a figure to its source

Clicking a significant amount opens its breakdown. From there, the player can reach the responsible Line, vehicle, facility, contract, purchase, construction project or loan through UI-D09 links. For example, maintenance costs lead to the relevant work/charges and then to the actual vehicle or workshop, not to a generic fleet search.

Use stable transaction and object identities. The finance window reports the same postings and commitments as the commercial, construction, depot and Line views; it does not create a parallel ledger. If a transaction spans several Lines or functions, disclose its recorded allocation basis. Do not allocate all of a shared vehicle's costs to every Line using it or count one customer payment once per transport leg.

Keep any unallocated company overhead visible rather than silently discarding it or inventing precision. Line, contract and facility breakdowns may describe the same economic event from different perspectives. Company totals count that event once; show a reconciliation when a scoped result excludes shared overhead or uses a different cost basis.

A tooltip explains the metric's definition, main contributing factors and calculation basis. A full transaction/history list opens in a stable detail, not a long transient hover popup. Retained records for sold vehicles, ended contracts and completed projects remain attributable; links may open read-only history when the current object is unavailable.

## 5. Reporting periods and navigation

Use a shared reporting-period control for the finance cards. Preserve the selected date interval when drilling from a company financial total into the financial results of a Line, contract or facility. If the target cannot represent that interval, show the limitation instead of silently substituting another period.

This does not replace a target's live operational status with historical data or overwrite another window's pinned identity, unsaved changes or unrelated filters. Display historical results and current operation as different contexts. Preserve a way back to the source, including scroll position and active filters.

Dates and accrual/reporting units follow the shared 14-day month and 168-day year. Mark partial periods, comparison periods and the future cash look-ahead clearly. Loans, payroll and agreements retain their own authoritative due dates; selecting another report period does not reschedule them.

For an object with no operation yet, show no operating history or insufficient data as appropriate. Do not invent zero profitability, count a forecast as achieved performance or rank incomparable partial periods as if they were equivalent.

## 6. Plans, commitments, payments and cash outlook

Keep the following states separate in every relevant view:

- **Uncommitted plan:** a cost/revenue estimate for an unlaunched Line, offer or construction proposal. It is not debt or an automatically reserved payment.
- **Accepted commitment:** an actual order, agreement or accepted project scope with remaining obligations and real due dates/conditions.
- **Posted payment:** cash that has actually moved, linked to its economic purpose and any settlement.

The optional inclusion of a saved plan in a future-spending preview is a scenario toggle only. Identify which plans are included and show their assumptions. It does not launch projects, submit offers, buy vehicles, secure land, reserve capacity or authorize financing. A scenario's projected negative balance is not the company's current cash balance.

Accepted purchases made while preparing an otherwise unlaunched plan remain real obligations. Include them in the baseline outlook once, and count only the additional uncommitted scope when that plan is included as a scenario. Deleting the design does not remove paid land or cancel its separately accepted orders.

Separate firm amounts/dates, contractually variable amounts and estimated demand-dependent income. An unpaid customer bill is a receivable/expected receipt, not money already received. A contingent penalty is not a posted charge until the governing rules make it one. Display the state and basis instead of summing every possible expense into a fake amount due now.

Avoid double counting deposits, stage payments and outstanding balances. An already paid deposit is not still a future cash outflow. Applicable cancellation views reconcile total liability, prepaid credit, additional payment and refundable excess, while consumed services and existing debt remain separate under CONTRACT_CANCELLATION. A refund is not fresh transport revenue.

Cash and operating performance remain distinguishable: drawing a loan increases cash and debt, not transport earnings; repaying principal is a financing payment, distinct from interest and operating costs. Asset purchases and disposals retain their existing reporting treatment. Do not add depreciation, tax filings or formal accounting tasks just to fill a card. Missing reporting attribution is an implementation gap to resolve transparently, not permission to invent numbers.

## 7. Loans and financial actions

The founding loan remains real debt, with the selected tier and accepted terms visible after startup. Subsequent borrowing uses the normal products in GAME_DESIGN Section 38 rather than offering another founding loan.

For each loan show lender/product identity as available, original and outstanding principal, next instalment, remaining schedule, interest-rate basis, total/remaining payments where determinable and applicable early-repayment conditions. A variable/conditional total must be labelled as an estimate, not a guaranteed payoff amount. Do not add a new lender marketplace or bond trading.

Borrowing, permitted early repayment, asset disposal, contract changes and distress recovery open the corresponding existing workflow with current validation and an impact preview. Disclose immediate cash effect, resulting debt and future payments before confirmation. A plan-affordability warning never takes out a loan on the player's behalf.

Keep purchase, repayment, cancellation and renewal approval within existing authority/budget rules. Scenario controls, links and tooltips are navigation/analysis only. Repeated confirmation, parallel windows or restored UI state cannot duplicate a payment, refund, loan or sale. The timing of binding commands during pause remains governed by the shared command rules, not decided by this screen.

## 8. Refresh, persistence and boundaries

Build financial views from authoritative postings, outstanding commitments and cached/event-driven reports. Opening cards or changing periods must not rerun the economy, accrue interest or reapply invoices. Bounded forecasts use known schedules and explicit assumptions rather than a second simulation running secretly ahead of the campaign.

During manual or critical-event pause, the UI, tooltips and scenario inspection remain usable while game-time accruals and physical work remain stopped. Save/load retains the underlying obligations/postings and reconstructs their views without replaying settlements. Restored cached estimates require revalidation before any binding action.

Respect company ownership and information permissions. A link to an external provider does not expose its private accounts. Do not introduce consolidated-company accounting or foreign-exchange rules through an additional filter; only report supported scopes and make their boundaries explicit.

No fixed chart design, financial reserve percentage, loan rate, profitability target or new failure condition is approved here. The goal is simple, traceable financial decision-making over the agreed game economy.

## 9. Acceptance evidence to collect

These are required checks for this confirmed UI direction, not claims that an implemented game has passed them.

| ID | Scenario |
|---|---|
| FINUI-A01 | Open Finance through Company and the upper-left HUD cash/current-period result. Verify the same workspace, compact summary/cards, clear current-cash versus period-result versus future-payment basis, readable CZ/EN and enlarged UI. |
| FINUI-A02 | Drill from a company cost total into a Line, vehicle/workshop and its charge. Retain period/source context, stable links and history for a retired asset; shared costs and cross-view totals reconcile without duplicate postings. |
| FINUI-A03 | Compare current cash, unpaid incoming amounts, accepted stage payments and variable forecasts. Change the look-ahead and inspect assumptions; unknown values are not zero and projected cash is not current spendable money. |
| FINUI-A04 | Include/exclude an unstarted plan in a spending scenario. It creates no debt/order/operation. Separately accepted land, vehicle or supplier commitments remain in the baseline, including after deleting the draft, and are not counted again in its incremental estimate. |
| FINUI-A05 | Inspect a real loan disbursement, principal repayment and interest payment. Cash, debt and operating result remain distinct; terms and game-calendar due dates stay visible. Preview permitted new borrowing/early repayment without applying it on hover or repeated confirmation. |
| FINUI-A06 | Settle a supported cancellation with prepaid credit and outstanding used-service charges. Immediate cash effect, remaining commitment and historical payments reconcile to the canonical settlement once; no duplicate refund or fresh-revenue misclassification. |
| FINUI-A07 | Inspect a partial reporting period, an idle/new Line and overlapping Line/contract/facility analyses. Preserve dates, scope and allocation basis; no invented observations or summing alternative analyses as independent company totals. |
| FINUI-A08 | Refresh, change scope, follow links and save/load while running, manually paused and critically paused. No accrual/payment is generated by reporting, no private provider data is exposed, and existing windows/drafts and incident identity remain intact. |

## 10. Decision record

| ID | Decision | Status |
|---|---|---|
| UI-D19 | One company finance window with a compact cash/result/commitment summary, five task cards, source-linked figures and shared reporting periods; draft scenarios remain separate from accepted obligations and actual payments | CONFIRMED on 2026-09-30 |

This supplements the confirmed UI directions and focused station, depot, commercial and construction specifications. General company, branch and personnel screen proposals are not approved by this finance decision.
