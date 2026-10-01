# Tranzit — Company, branches and workforce UI

> **Status: CONFIRMED UI DIRECTION — UI-D20, 2026-09-30.** The player accepted a compact Company overview, five task-based cards, branch lists/details, aggregate workforce management and named-manager responsibility/authority views. Exact dimensions, column widths and localized labels remain visual-design work. This specification is not an implemented or tested UI.

Read with [UI_UX_DESIGN.md](UI_UX_DESIGN.md), especially shared floating windows, UI-D09 object links, UI-D15 minimalism/tooltips and the pause rules. This focused document resolves the Company/branch/personnel presentation within the main document's otherwise proposed detailed taxonomy. [GAME_DESIGN.md](GAME_DESIGN.md), Sections 2.4, 7–8 and 27–28, owns market access, branches, management, workforce and technology. [V1_SCOPE.md](V1_SCOPE.md) retains the release boundary. [UI_FINANCE.md](UI_FINANCE.md) owns the existing financial window; [UI_DEPOTS.md](UI_DEPOTS.md) and [UI_STATIONS.md](UI_STATIONS.md) own facility-specific views. Do not duplicate their ledgers or change their mechanics here.

## 1. Company overview

Open Company / Firma from the fixed bottom bar into the shared movable/resizable window. Identify the company and the current organizational scope. The overview answers: **Does the company have the people, administrative capacity and permissions its operation needs, and who is responsible?** It is not another financial dashboard.

Show a few relevant company facts and concise actionable exceptions, such as a director vacancy, understaffed operation, an overloaded branch or a missing/expiring licence. Keep these different causes distinguishable. Each exception links to its branch, profession, manager, licence and affected work where applicable. State whether authorized management is handling it or a player decision is needed. No large empty alert panel is needed when nothing requires attention.

Use independently openable compact cards, not a mandatory setup sequence:

| Card | Overview and opened detail |
|---|---|
| Branches / Pobočky | Physical offices, commercial coverage, director, administrative workload and missing dependencies; direct branch detail |
| Workforce / Personál | Requirements, filled capacity, shortages/reserve and salary by ordinary profession; sources of workload and supported staffing controls |
| Management and authority / Vedení a pravomoci | Named people, occupied/vacant roles, responsibility, effective delegated policies and decisions awaiting approval |
| Licences and permissions / Licence a oprávnění | What the company may operate and where, applications, requirements, validity and renewal/expiry risks; open the confirmed UI-D33 Licences and expansion workspace for the full market/licence/permit/application view |
| Company systems / Firemní systémy | Actually adopted communication/business systems, current capabilities, available improvements and their concrete requirements/effects; open UI-D38 Technology for research/unlock/adoption state |

Provide direct access to Finance, opening/focusing the same window as the bottom-bar cash amount. Do not maintain a second balance, loan interface or transaction history inside Company. UI-D39 owns group/subsidiary control. Company adds a compact **Our group / Naše skupina** view when relevant, showing ownership, control state, broad direction, active owner directives and important decisions/issues. Controlled subsidiaries remain AI-managed; do not duplicate their full Line/Fleet/Finance UI inside the parent overview.

## 2. Branch list and detail

Use a compact branch list with city, director, operating state, administrative workload and the main issue. Search/filter/sort should preserve selection and scroll during updates. Clicking a branch opens its exact detail using the usual reusable/pinned-window rules.

The branch header identifies its physical office and state. Its overview shows the cities/territory it can actually commercially cover, what work it handles and why capacity is limited. Detail areas expose premises and equipment, aggregate staffing, leadership and linked contracts, opportunities or Lines. Show the basis and period of workload values on inspection rather than a generic branch-quality bonus.

Commercial coverage follows the company's adopted operating model in GAME_DESIGN Section 7.2. It is not an invented kilometre radius, a transport licence or proof of station access. At the local-office stage, an office covers its own city/locality market (0 hops). Later adopted communications/organization can extend that branch to directly neighbouring markets (1 hop), then further authored hop ranges or regional coverage. Several branches contribute the union of their reachable markets. Internal economic centres/neighbourhoods inside one city market do not require separate branches. A route merely passing through a market is not the same as commercially serving it, and filters cannot reveal unknown local opportunities outside legitimate discovery.

Distinguish insufficient physical space, equipment/system capability, ordinary staffing below minimum, workload above capacity and a named-director vacancy. Preserve the existing vacancy/grace-period rules: losing a director does not instantly delete running services. Show exactly what is restricted, the operational impact and the way to recruit or reassign a replacement. An active branch needs its one accountable director under the core rules, not two competing director assignments.

Premises expansion/replacement links to the construction workflow. Changing a staffing target, drawing an office expansion or selecting an equipment level does not immediately create people, completed floor space or future-era technology. Keep ordinary equipment quality separate from major communications/coverage unlocks.

## 3. Ordinary workforce: professions, not individual applicants

The primary view is a profession table, not a list of ordinary people. Each row shows **required capacity, currently filled capacity, shortage/reserve and offered salary**. Market/reference salary and achievable staffing may be exposed where the simulation supplies them; estimates remain visibly estimates.

Opening a profession shows which Lines, duties, branches or facilities produce the requirement, already committed workload, relevant staffing targets and any proposed additional demand. State units and time basis: headcount/FTE-equivalent, driver-hours, duty capacity and a qualification-specific reserve are not interchangeable totals. A saved unlaunched Line or project may appear in a labelled scenario, not silently increase actual committed payroll or staffing demand.

Edit the salary policy for the selected ordinary profession at company level under GAME_DESIGN Section 8.3. Facility views link to that policy rather than introducing independent branch wages. Preview the affected scope and expected cost before applying a policy change. Keep salary periods consistent with the 14-day game month and use the literal accounting token `money`.

Hiring and attrition remain automatic, aggregate and time-dependent. Raising wages or setting a target does not instantly fill a shortage, guarantee a forecast or create an ordinary-worker hiring minigame. A manager's individual salary is separate from this ordinary-profession policy.

Respect the distinction between company-wide mobile crew pools and facility-bound staff. A regional filter does not create an independent driver reserve pool. Mechanics, handling staff and office workers still need the appropriate aggregate allocation to actual facilities. Spare conductors cannot cover missing qualified train drivers, and nominal affordable positions are not usable staff capacity. A single employee-capacity pool cannot be counted as free in several concurrent duties/facilities.

## 4. Named managers, responsibility and authority

Managers and important specialists remain identifiable individuals. The management list shows name, role, actual scope, salary and any pending decision. Reveal relevant skills, bounded traits and career information in the person's detail; emphasize role fit without inventing a universal best-manager score.

Clearly separate **the person's skills** from **what they are allowed to decide**. The authority view shows permitted routine actions, budget/approval limits, applicable policies, inherited versus local settings and escalation to the player. Display effective scope and policy origin, following the existing hierarchy/manual-override rules rather than inventing a second permissions system.

Provide a traceable decision history: who acted, which objects were affected, what rule/budget authorized it, its reason and outcome. Pending decisions link to the relevant contextual review. An audit entry does not authorize replaying an order. Changes to permissions govern eligible subsequent actions, not automatic reversal of completed purchases or contracts.

Only the branch-director requirement is mandatory as defined in the core. Additional managers/departments are useful when workload and delegation justify them, not mandatory unlocks for every screen. Preserve access to departments and subordinate scopes through existing organizational relationships without requiring a drag-and-drop organizational chart or manual assignment of every employee.

Recruitment, reassignment and dismissal reuse GAME_DESIGN Section 7.4: current shared-market availability and disclosed terms, no poaching or new bidding/negotiation loop, and the existing immediate hiring/dismissal rules. Dismissal previews its existing severance and the roles it leaves vacant. Revalidate candidate availability and role assignments before a binding action; multiple windows cannot hire one person twice or put them in conflicting roles. History and identity survive reassignment or return to the shared labour market.

Delegation never creates vehicles, staff, slots or permissions, exceeds valid capacity, or bypasses required approvals. The player can inspect and override eligible decisions through the existing workflows rather than manually repeat work already handled by the dispatcher.

## 5. Licences, permissions and company systems

The Company card is a compact summary. The confirmed detailed workflow lives in [UI_LICENCES_MARKETS.md](UI_LICENCES_MARKETS.md) under UI-D33. Licences show the enabled activity, issuing jurisdiction, territorial scope, requirements, current application/validity state, costs, supported processing estimate and renewal rules. Keep company/market entry, activity licensing and specific operational approvals distinct. A missing-licence alert opens that exact licence/market-entry/permit requirement, not a generic settings screen.

Show separately: activity allowed but region not entered; region accessible but activity licence missing; both held but physical access/capacity still absent. Municipal operating permission is not automatically a transport contract. An application or forecast completion is not an issued right, and a licence does not supply a vehicle or station slot.

Applications and renewal/withdrawal actions use existing rules and explicit validation; do not add paperwork forms or a new regulatory minigame. Pending requirements can change, with a visible reason. Losing a right surfaces affected operation and existing recovery/consequence rules rather than silently deleting it.

Company systems show what has actually been adopted, what capability it provides and what installation, staffing, funds or technology is still required. Distinguish historically available, researched/unlocked, being adopted and usable where supported. UI-D38 [UI_TECHNOLOGY.md](UI_TECHNOLOGY.md) owns the detailed Technology workspace. In particular, a calendar date or improved office furnishings do not automatically grant centralized coverage, online sales or remote information. A completed technology can unlock branch/station/facility/construction upgrades without applying them; only genuine company-wide systems use the simple adoption project defined by UI-D38.

## 6. Group and subsidiary overview — UI-D39

When the player controls or owns stakes in other companies, Company exposes a compact group/holdings view.

Show:

- controlled subsidiaries;
- minority investments;
- ownership percentage/economic interest;
- actual control state;
- broad company direction;
- active owner directives;
- one material blocker/decision where relevant;
- direct link to UI-D37 company detail and UI-D39 ownership workflow.

A controlled subsidiary keeps its own cash, debt, staff, licences, contracts, assets and operating state until a real transaction/integration changes them.

The subsidiary remains AI-managed. The player interacts through the small owner-action set in UI-D39 rather than switching the entire normal UI into that company's command context.

A Line or major asset belonging to a controlled subsidiary can still be opened and, where allowed, edited as an **owner directive**. The subsidiary then handles the actual vehicles, staff, capacity, permissions, procurement and operational consequences.

Intra-group capital, loans, dividends/distributions, leases, asset transfers and shared facility/access arrangements link to the canonical UI-D39/Finance/agreement workflows and remain real transactions.

Do not add a second dense layer of subsidiary policies or a mandatory organization-chart editor.

## 7. Shared interaction and state safety

Apply the same dark, minimalist components across company, branches and personnel. Keep current scope, important shortage/vacancy, units, periods, unsaved state and action consequences visible. Tooltips explain workload, staffing estimates, skills and effective policy; opened details contain long lists, editable rules and history. Use keyboard/focus access as well as hover, with complete Czech/English presentation at 1080p and enlarged UI scales.

Links resolve stable identities and preserve source context, pinned objects and drafts. Inspection does not grant private competitor information or ownership rights. A renamed/closed branch or unavailable manager opens valid history or an explicit unavailable state, not a similarly named replacement.

Refresh from actual state changes; do not recalculate the whole company every rendered frame or create per-person workers for this screen. Save/load preserves actual people, role assignments, policies, workforce capacity, office state, applications and adoption progress. Restoring a window/filter does not hire, pay, apply a draft or duplicate decisions.

Normal window/card/tooltip use never changes speed or pause. Planning remains available in manual or critical-event pause, while recruitment, application processing, training and other time-driven work stay stopped. Binding commands retain existing validation/timing rules; this UI decision does not settle the separately unresolved general timing of binding commands during pause.

## 8. Acceptance evidence to collect

These checks describe evidence required when implemented, not passing game tests. Read with [V1_ACCEPTANCE_TESTS.md](V1_ACCEPTANCE_TESTS.md).

| ID | Required scenario |
|---|---|
| COUI-A01 | Open Company and all five cards. Find a branch, profession, manager and licence directly from a scoped issue; Finance reuses UI-D19, with no duplicate ledger or mandatory organizational chart. |
| COUI-A02 | Inspect 0-hop local and technology-expanded 1+/regional branch coverage. Distinguish internal economic centres from separate city/locality markets, pass-through from commercially served markets, licence/access from coverage, minimum staffing from overload, and director vacancy from instant loss of all running services. |
| COUI-A03 | Change a profession's salary and a facility staffing target. Inspect cost/scope and achievable fill estimates; no instant hires or individual ordinary applicants. Mobile crew pools and facility-bound capacity remain distinct with correct qualifications and time units. |
| COUI-A04 | Compare committed staffing demand with an unlaunched-plan scenario, including concurrent duties and multiple facilities. Do not double-count staff, turn an estimate into a reservation or create regional crew pools through filtering. |
| COUI-A05 | Inspect manager skills versus effective authority, inherited/local policy and decision history. Reassign/recruit/dismiss through existing checks, with candidate races, disclosed severance and visible vacancy effects; no duplicated employment, replayed actions or retroactive cancellation. |
| COUI-A06 | Inspect missing, pending, valid and expired rights and planned/adopted company systems. Requirements, processing and actual capability stay distinct; navigation cannot issue permissions, unlock technology or reveal hidden opportunities. |
| COUI-A07 | Save/load with a vacancy, pending application, staffing shortage and delegated decision. Preserve authority/history without duplicate hiring or payments; opening/closing/hovering never changes pause/speed and no time-driven work progresses while paused. |
| COUI-A08 | Test CZ/EN, keyboard/focus tooltips, narrowed/resized windows and enlarged UI. Important scope, periods, shortages and consequences stay readable; source links preserve drafts, selection and pinned identities. |

## 9. Decision record

| ID | Decision | Status |
|---|---|---|
| UI-D20 | Company overview with Branches, Workforce, Management and authority, Licences and permissions, and Company systems; direct Finance access; branch details, profession-based staffing and named-manager scope/policy/history | CONFIRMED on 2026-09-30 |

This decision complements the existing UI specifications. It does not approve the separate map-overlay proposal, add staffing/HR mechanics or change branch coverage, salaries, recruitment, licensing or technology progression.
