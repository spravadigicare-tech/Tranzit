# Tranzit — Contract cancellation and early capacity release

> **Status:** Current agreed design rule. This is a focused specification, not a chronological change log or an implemented feature.
>
> Read together with [GAME_DESIGN.md](GAME_DESIGN.md), especially Sections 11.8 (early termination), 11.12 (automatic renewal), 13.2–13.2.1 (rail capacity and ordering), 20.3–20.4 (station access) and 38 (financial distress).

## 1. Agreed principle

A carrier that voluntarily returns contracted rail or station slots before the end of the committed term pays a contractual cancellation fee. The fee must be meaningful but proportionate and capped. Routine cancellation must remain a viable business decision, not an intentionally ruinous punishment that locks the player into years of unwanted capacity.

Exact percentages, fee-period caps and notice lengths remain balancing parameters, not fixed values approved in the design discussion. This rule does not guarantee immunity from insolvency for a company already in serious financial distress.

## 2. What incurs the fee

Early cancellation or reduction affects only the capacity being released and its remaining committed period. Returning two of ten calls must not trigger a penalty calculated on all ten. Rail and station access use the same rule, even when several owners are involved in one Capacity Order.

The calculation uses the affected reservation commitment, not the company's total assets, revenue or current cash. It should charge only a bounded portion of the remaining reservation fees, subject to a clearly disclosed cap. It must not demand all remaining years of reservation fees plus an additional cancellation penalty.

Notice can reduce the charge under the agreed terms; the applicable notice bands must be visible before signing. A short-notice release may cost more than an early notice, but remains subject to the cap. No exact fee schedule is locked in yet.

Cancellation charges and retained prepaid amounts for the same cancelled future reservation must be reconciled so that the same loss is not charged twice. Settlement is one idempotent ledger transaction per accepted release: distinguish the total cancellation liability, any prepaid amount credited against it, additional cash payable and excess refundable prepayment. Retrying or partially executing a release cannot apply the cap, charge or credit twice. Already consumed services and existing unpaid invoices remain separately payable. Do not charge future per-use fees for calls that will no longer take place.

The infrastructure owner receives the cancellation payment and regains the released capacity from its effective release date. The carrier cannot sell or lease the slot to another carrier. Reallocation by the owner still follows the existing finite-capacity and access rules.

## 3. Renewal is not cancellation

Letting a term expire normally, or disabling Auto-renew before the displayed renewal/notice deadline, does not incur an early-cancellation fee. Existing debts and charges for services already used are unaffected.

Turning Auto-renew off does not undo a renewal that has already become binding. Where an additional term is already committed, exiting it uses the disclosed cancellation rules. The UI must distinguish the active term, an already committed future term and a renewal that has not yet been accepted.

An owner refusing renewal is not a voluntary early cancellation by the carrier. Qualifying owner-side failures or exceptional disruptions follow the agreed renegotiation, relief and compensation provisions rather than automatically imposing the carrier's ordinary cancellation fee.

## 4. Transparent confirmation

The contract and Capacity Order editor show the cancellation method, cap and notice rules before acceptance. Before confirming early release, the player sees:

- exactly which calls, periods and agreements are affected;
- the effective end/release date;
- the cancellation fee and the applied cap;
- any prepaid credit/refund and separately outstanding charges;
- the total immediate payment and future reservation costs avoided;
- affected Service Patterns, customer contracts or connections;
- any remaining obligations after the release.

For a multi-owner order, show one total with a per-owner breakdown. Avoid individually modest charges unexpectedly adding up to an undisclosed large bill.

The system must warn when a released slot would leave a continuing transport contract or timetable without capacity. It does not cancel related customer contracts, remove vehicles, teleport trains or free physically occupied track. Slot release changes future commercial rights; physical occupation and safe clearing movements remain governed by the operational simulation.

## 5. Relationship, automation and consistency

Using an explicitly agreed ordinary cancellation option is not automatically treated as repeated SLA failure or serious misconduct. Any relationship effect must be explained and proportionate to the actual disruption. Genuine breaches, damage claims and customer-service failures retain their existing rules; this cancellation cap is not a blanket waiver of unrelated liabilities.

Delegated managers may cancel or reduce capacity only within their existing approval and budget permissions. Turning on automatic renewal does not authorize unrestricted early cancellation or arbitrary new fees.

The same cancellation and payment rules apply to the player and AI carriers. Evaluate fees when the user previews, changes or confirms a cancellation, not every frame. Preserve contract history and unresolved obligations.

Other recurring agreements may use the same transparent, proportionate early-exit principle where their terms allow voluntary exit, but must use a fee basis appropriate to the service. Do not blindly apply a slot-reservation formula to the total value of transported cargo, fuel purchases or construction works.
