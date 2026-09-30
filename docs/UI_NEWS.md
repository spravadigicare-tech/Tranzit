# Tranzit — News and historical events UI

> **Status: CONFIRMED UI DIRECTION — UI-D40, 2026-09-30.** The player accepted a deliberately simple world-news/history feed. It communicates meaningful world, company, infrastructure, economic and historical changes, explains concrete known impact on the player's company where applicable, and links to the real affected objects/workflows. It is not a second incident system and not an event-choice minigame. Normal world news never auto-pauses by itself; any actual critical operational/business consequence is surfaced separately through UI-D24/UI-D08. Exact visual styling, significance thresholds and content cadence remain design/content work. This specification is not an implemented or tested UI.

Read with [UI_EVENTS.md](UI_EVENTS.md), [UI_EXTERNAL_COMPANIES.md](UI_EXTERNAL_COMPANIES.md), [UI_CITIES_REGIONS.md](UI_CITIES_REGIONS.md), [UI_MAP_LAYERS.md](UI_MAP_LAYERS.md), [UI_LICENCES_MARKETS.md](UI_LICENCES_MARKETS.md), [UI_OWNERSHIP.md](UI_OWNERSHIP.md) and [GAME_DESIGN.md](GAME_DESIGN.md), especially Sections 2, 7.2, 28–29 and 35–37.

## 1. One world news/history feed

Primary entry:

**World → News / Svět → Zprávy**

Use one feed with filters rather than several unrelated event systems.

Useful filters:

- **Important / Důležité**
- **Companies / Firmy**
- **Economy / Ekonomika**
- **Infrastructure / Infrastruktura**
- **Historical / Historie**
- **All / Vše**

The default view prioritizes meaningful recent events.

## 2. Purpose

The feed answers:

- what important changed in the world;
- when and where it happened;
- what objects/companies/regions are involved;
- whether the player's company has a known material impact;
- where the player can inspect that impact.

It does not ask the player to make arbitrary narrative choices.

## 3. World and infrastructure news

Examples of valid news:

- major railway/road/infrastructure opening;
- major closure or long reconstruction;
- significant new station/terminal/depot where publicly relevant;
- major infrastructure purchase/sale;
- new international or regional connection;
- public tender/concession announcement where actually public;
- major access/regulatory change.

Example:

> **New railway opened between X and Y**
>
> Operator/owner: Central Rail
>
> The corridor shortens travel between the two regions.
>
> **Show on map · Open company**

Opening the item never creates access, capacity or a commercial opportunity by itself.

## 4. Historical and regulatory events

Historically anchored or simulated major events can appear as news when they become known to the player.

Example:

> **Border regime changed**
>
> New cross-border freight conditions take effect on Day 8.
>
> **Impact on our company**
> 2 active Lines use the affected crossing  
> 1 licence requires review
>
> **Review impact**

The impact links to the real Lines/licence workflows.

Do not represent historical change as an unexplained flat modifier such as “−12% revenue”.

## 5. Economy and market news

Significant economic changes can include:

- material/energy price shift;
- industrial expansion/contraction;
- major demand shift;
- recession/boom conditions;
- supplier disruption;
- major commodity shortage/surplus;
- meaningful labour/market change where modeled.

Example:

> **Coal prices rose materially**
>
> Cause: reduced regional output
>
> **Our exposure**
> 4 depots consume coal  
> forecast operating cost: higher
>
> **Open Procurement**

Only show a player-impact summary if the simulation can actually derive it from known/authorized information.

Do not attach generic “this may affect you” text to every news item.

## 6. Company news

UI-D37 company history remains the canonical company-specific record.

World News surfaces only significant known company events such as:

- major new service/network expansion;
- entry into a new market/region;
- acquisition or sale;
- insolvency/restructuring;
- major infrastructure project;
- significant public contract/tender result;
- company founding/dissolution;
- major ownership/control change.

Example:

> **Morava Rail acquired Central Coaches**
>
> **Open Morava Rail · Open Central Coaches**

News does not duplicate the entire company history database.

## 7. Player-company events

Routine player operations do not belong in World News.

Examples that stay in UI-D24 Events/History:

- Trip delay;
- vehicle breakdown;
- maintenance completion;
- routine delivery;
- loading completion;
- ordinary contract task;
- dispatcher recovery.

A major public milestone of the player's company may appear in World News/history if it is genuinely significant, for example:

- first international route;
- major acquisition;
- opening of a major infrastructure project;
- major public concession;
- company restructuring.

This is historical/public context, not a second operational alert.

## 8. World News versus Events

Keep the distinction strict:

### World News

Answers:

> What changed in the world?

Characteristics:

- public/world context;
- historical/economic/company/infrastructure development;
- normally non-blocking;
- never pauses by itself;
- can be read later.

### UI-D24 Events

Answers:

> What does our company need to know or do operationally?

Characteristics:

- player-company operational/business state;
- needs decision / in progress / information / history;
- can be critical;
- can trigger UI-D08 auto-pause when criteria are met.

One real cause can therefore produce both:

- a World News item for the global event;
- a UI-D24 incident for a concrete player-company consequence.

Example:

> Border rules change → World News  
> Player Line loses valid permission tomorrow → Needs decision incident

These are two presentations of one underlying cause, not duplicate simulation events.

## 9. Player impact section

Where there is a real known impact, a news item can include:

> **For our company**
>
> 3 Lines  
> 1 Contract  
> 2 Facilities
>
> **Show impact**

The impact view links to the actual objects.

Possible impacts include:

- affected Lines/Trips;
- affected contracts;
- licence/permit changes;
- procurement/material exposure;
- infrastructure/access changes;
- affected branches/regions;
- tariff/customer consequences where actually modeled.

If there is no identified impact:

> **No direct known impact**

Do not fabricate impact counts from weak guesses.

## 10. Information provenance and delay

A modern-looking news feed must not imply omniscient real-time information.

News can be known because it is:

- public;
- locally observed;
- reported through company presence;
- contractually communicated;
- received through historically appropriate communications;
- estimated/analysed from known facts.

The feed can therefore show:

- publication/known date;
- event date;
- source/provenance where relevant;
- uncertainty/staleness.

A remote event may become known later in earlier eras.

Inactive/macro-region information follows the same knowledge boundaries as the rest of the game.

## 11. Significance filtering

Do not turn every state change into news.

Suitable news categories include:

- major historical/macroeconomic changes;
- border/regulatory changes;
- major infrastructure opening/closure/project;
- major company entry/exit/acquisition/insolvency;
- significant new public service;
- significant technology/industry milestone;
- major public tender/concession;
- rare large disaster/weather event with broader relevance.

Do not generate news for:

- one routine vehicle purchase;
- ordinary service/maintenance completion;
- minor delay;
- one normal supplier delivery;
- routine daily contract activity.

Use significance thresholds/content rules rather than a firehose.

## 12. Notifications

Ordinary news:

- does not pause;
- can create a small restrained toast/badge;
- remains available in the feed.

Example:

> **Important world news available**

Do not use a modal for routine news.

If a world event creates a critical player-company consequence, the critical part follows UI-D24/UI-D08.

## 13. History archive

The feed also acts as a lightweight campaign history.

Allow browsing by year/period, for example:

> 1904  
> 1903  
> 1902  
> 1901

Meaningful entries can include:

- world/historical events;
- major infrastructure;
- acquisitions/ownership changes;
- major company milestones;
- significant player-company milestones;
- major economic changes.

Do not attempt to preserve every low-level transaction in this archive.

## 14. Direct navigation

Use UI-D09 exact-object links.

A news item can link to:

- company;
- city/region;
- infrastructure;
- affected Line/Contract;
- licence/permit;
- procurement item;
- ownership/acquisition;
- construction project;
- technology;
- relevant map location.

Opening a link does not acknowledge a separate UI-D24 incident unless that incident is explicitly opened/acknowledged.

## 15. Save/load and identity safety

Persist:

- canonical underlying world events;
- discovered/known timing;
- news presentation state such as read/unread where useful;
- source/provenance;
- links to stable object identities.

After save/load:

- a historical event does not fire twice;
- the same acquisition does not produce duplicate world history;
- old news retains event-time meaning;
- renamed/acquired/dissolved companies preserve correct historical identity;
- loading does not suddenly reveal previously unknown remote events unless their knowledge condition is met.

## 16. Acceptance evidence to collect

| ID | Required scenario |
|---|---|
| NEWSUI-A01 | Trigger/initialize a major historical/regulatory event. News explains concrete change and links to affected world objects without using an opaque flat modifier. |
| NEWSUI-A02 | World event affects two player Lines and one licence. News shows real impact links while a separate actionable UI-D24 incident appears only for the actual player decision; no duplicated simulation event or auto-pause from news alone. |
| NEWSUI-A03 | Trigger meaningful company expansion, acquisition and insolvency. Feed shows only significant public/known changes and links to UI-D37/UI-D39 identities/history. |
| NEWSUI-A04 | Trigger ordinary delay, maintenance completion and routine supplier delivery. They do not become World News merely because they are events. |
| NEWSUI-A05 | Trigger a material commodity/economic change. Impact is shown only from actual known company exposure and links to Procurement/affected objects; unknown exposure is not fabricated. |
| NEWSUI-A06 | Compare early-era local/remote events and a later communication capability. News arrival/provenance follows actual information capability rather than instant omniscience. |
| NEWSUI-A07 | Browse multi-year campaign history with acquisitions, infrastructure openings and major player milestones. Archive remains concise and links to stable historical/current identities. |
| NEWSUI-A08 | Save/load before and after news discovery. No event/news duplication, identity retargeting, hidden-data leak or new pause is introduced by reload. |
| NEWSUI-A09 | Verify CZ/EN, enlarged UI, keyboard access, filters and restrained notification presentation. |

## 17. Decision record

| ID | Decision | Status |
|---|---|---|
| UI-D40 | Simple World News/history feed for meaningful historical, economic, infrastructure and company changes; concrete known player impact with object links; strict separation from UI-D24 incidents; no narrative-choice minigame or auto-pause from ordinary news | CONFIRMED on 2026-09-30 |

UI-D40 complements UI-D01–UI-D39. GAME_DESIGN Sections 35–37 and the relevant underlying systems remain authoritative for actual world events and consequences.
