# Tranzit — Main menu, save/load, pause and settings UI

> **Status: CONFIRMED UI DIRECTION — UI-D36, 2026-09-30.** The player accepted the main-menu, campaign-organized save/load, pause-menu and settings proposal. Escape/pause-menu behaviour is confirmed here. UI-D08 now also confirms configurable focus-loss pause and intentionally simple notification settings. Exact visual dimensions, default autosave interval/count, graphics-option inventory and key defaults remain implementation/content work. This specification is not an implemented or tested UI.

Read with [UI_UX_DESIGN.md](UI_UX_DESIGN.md), especially UI-D04, UI-D06–UI-D08, UI-D15, UI-D24, UI-D35 and UI-D34. [V1_SCOPE.md](V1_SCOPE.md) owns full persistence/offline/save safety. [V1_IMPLEMENTATION_BRIEF.md](V1_IMPLEMENTATION_BRIEF.md) owns implementation guidance and release integration.

## 1. Main menu

Keep the main menu compact.

When a valid campaign exists, primary actions are:

- **Continue / Pokračovat**
- **Load Game / Načíst hru**
- **New Game / Nová hra**
- **Settings / Nastavení**
- **Credits / Autoři**
- **Quit / Ukončit**

If no valid campaign/save exists, hide or disable Continue with an explicit reason rather than linking it to an empty load screen.

Continue loads the most recent valid continuation candidate, not merely the newest timestamp if that save is known invalid/corrupt.

A compact last-campaign summary can show:

- company name;
- game date/time;
- real save timestamp;
- small campaign facts such as Lines/vehicles if already available cheaply and accurately.

Do not turn the main menu into a live management dashboard.

## 2. Campaign-organized save browser

Organize saves primarily by **campaign/company identity**, not one flat global list.

Inside a campaign distinguish:

- Manual saves;
- Quicksave slot/rotation;
- Autosave rotation.

Example:

> **Vítkova doprava**
>
> Manual  
> Before Austrian expansion  
> 1904 M6 D12
>
> Quicksave  
> 1904 M7 D3 · 14:22
>
> Autosaves  
> Autosave 1  
> Autosave 2  
> Autosave 3

Exact autosave count is a setting/default, not locked here.

## 3. Save metadata

Every save row exposes enough information to choose safely:

- campaign/company name;
- game date/time;
- real-world save timestamp;
- save type: Manual / Autosave / Quicksave;
- game version;
- save-format/version compatibility;
- optional concise campaign state summary.

If incompatible/corrupt:

> **Cannot load**
>
> This save was created by an incompatible game/save format.

or another precise detected reason.

Do not leave an unexplained disabled Load button.

## 4. Atomic save safety

Saving must be failure-safe.

For a successful manual/quicksave:

> **Game saved**

Use a short toast/status, not a blocking success modal.

If saving fails:

> **Game could not be saved**
>
> The previous valid save was preserved.

The failure is a visible critical UI condition under UI-D15. Do not hide it only in history.

Write/replace saves atomically or through another implementation that guarantees the previous valid save is not destroyed by an incomplete write.

A save command must not:

- advance simulation time;
- replay a transaction;
- finalize an uncommitted draft;
- change the current speed/pause reason;
- duplicate an order or payment.

## 5. Manual save, quicksave and autosave

Support:

- named/manual save slots;
- quicksave;
- quickload;
- rotating autosaves.

Quicksave remains logically distinct from the autosave rotation so an autosave does not unexpectedly replace the player's latest deliberate quicksave.

### Autosave timing

Autosave cadence uses **real elapsed application play time**, not simulation game time.

Therefore 16× simulation does not produce autosaves sixteen times as often as 1×.

Settings expose at least:

- Autosave On/Off;
- interval;
- number of retained autosaves.

Exact default values remain implementation/content decisions.

Autosave timing itself creates no simulated economic time and does not run while the application is closed.

## 6. Loading during a running campaign

Loading another save is a destructive context change.

If the current campaign has unsaved authoritative progress and/or relevant dirty drafts that would be lost, show a clear warning:

> **Load this game?**
>
> Unsaved progress since the last save will be lost.
>
> Unsaved planning drafts: 2
>
> **Load · Cancel**

Do not warn about “unsaved progress” when there is none.

Where appropriate provide a Save first route rather than forcing the user to cancel and navigate elsewhere.

After any successful manual load or quickload, the simulation finishes **paused** by default.

The loaded save may retain its previously selected running-speed preference for later resume, but loading itself does not immediately resume the simulation.

## 7. Pause menu

Pressing **Esc** in ordinary gameplay with no higher-priority transient interaction opens the pause menu and adds a **pause-menu pause reason**.

Pause menu actions:

- Continue;
- Save Game;
- Load Game;
- Settings;
- Main Menu;
- Quit Game.

Opening the pause menu does not alter the remembered selected running speed.

## 8. Independent pause reasons

Treat pause causes independently.

At minimum relevant reasons include:

- manual player Pause;
- critical-incident pause under UI-D08/UI-D24;
- pause menu;
- load-safe pause after loading.

Closing the pause menu removes only the pause-menu reason.

### Example: game was running

> running at 4×  
> Esc → pause menu  
> Continue → pause-menu reason removed  
> simulation resumes at 4×

### Example: game was already manually paused

> manual Pause  
> Esc → pause menu  
> Continue → pause menu closes  
> simulation remains paused

### Example: critical incident paused the game

> critical incident → paused  
> Esc → pause menu  
> Continue → pause menu closes  
> critical pause remains

Closing/acknowledging an incident still does not resume automatically under UI-D08/UI-D24.

This resolves pause-menu lifecycle; application focus loss/return is not decided here.

## 9. Escape priority

Esc acts consistently by interaction context:

1. if a transient map/build placement/drawing action is active, Esc cancels/exits that transient action;
2. if a focused edit/draft interaction has an Esc-close semantic, Esc exits/cancels that edit with dirty-state protection where needed;
3. otherwise Esc opens/closes the pause menu.

One Esc during track placement must not unexpectedly leave the campaign for the pause menu while the placement cancellation still requires handling.

Repeated Esc cannot discard committed agreements or delete saved drafts without the normal confirmation rules.

## 10. Main-menu and quit confirmation from campaign

Returning to the main menu or quitting the application must explicitly account for unsaved progress.

When unsaved changes/progress exist:

> **Return to main menu?**
>
> Unsaved progress since 19:42 will be lost.
>
> **Save and exit · Exit without saving · Cancel**

Use equivalent wording for Quit.

If there is no unsaved authoritative progress/dirty draft, avoid a misleading “you will lose progress” message. A simple confirmation may still be used for accidental Quit prevention if desired, but it must describe the real state.

**Save and exit** proceeds only after a successful save. If saving fails, remain in the campaign and show the save failure; do not exit and silently lose progress.

## 11. Settings structure

Use one Settings window/screen with categories:

- **Graphics / Grafika**
- **Audio / Zvuk**
- **Game / Hra**
- **Controls / Ovládání**
- **Interface / Rozhraní**
- **Language / Jazyk**

Use normal concise lists/forms, not a wizard.

Settings that can safely apply immediately should do so with visible current values. Settings requiring apply/restart must say so before confirmation.

## 12. Graphics settings

Support the actually implemented render settings, including where applicable:

- resolution;
- fullscreen/windowed/borderless modes;
- VSync;
- FPS limit;
- quality preset;
- shadows;
- draw distance;
- vegetation/world detail;
- anti-aliasing;
- other real rendering controls.

Quality presets can be:

- Low;
- Medium;
- High;
- Ultra;
- Custom.

A preset is only a convenience bundle of visible settings. Once a bundled value is changed manually, show Custom where appropriate.

Do not expose fake sliders that have no engine effect.

## 13. Audio settings

Separate meaningful channels, for example:

- Master;
- Effects;
- Vehicles;
- Environment;
- UI;
- Music if music exists.

Voice volume is not required when no voice acting exists.

Settings must use the same audio routing actually implemented by the game.

## 14. Game settings

Include settings such as:

- Autosave;
- Tutorial: Full / Basics only / Off;
- critical incidents automatically pause: On by default;
- pause when game loses focus: On by default;
- informational toasts: On/Off.

Do not introduce unapproved difficulty/cheat sliders here.

Changing tutorial mode after founding follows UI-D35 and changes guidance only.

Turning critical auto-pause off changes only the allowed UI notification/pause policy; it must not remove the incident, safety consequence or required decision.

V1 intentionally has no per-event-type auto-pause/notification matrix. **Informational toasts** controls lightweight toast presentation only; event-centre records and important states remain available.

With **Pause when game loses focus** On, focus loss adds an independent focus-loss pause reason without changing the remembered running speed. Returning to the game removes only that reason. If no other pause reason remains, the game resumes at the remembered speed; manual, critical, pause-menu and load-safe pause reasons remain intact. With the setting Off, focus loss/return does not alter the simulation clock.

## 15. Controls

Keyboard/mouse bindings are remappable.

Provide:

- searchable action list;
- current binding;
- secondary binding where supported;
- reset category/all defaults;
- conflict detection.

Example:

> Search: speed
>
> Pause  
> Speed up  
> Speed down

If assigning an already-used binding:

> **Conflict**
>
> This key is already assigned to Rotate camera.

The UI must provide a deliberate replace/keep/cancel resolution rather than silently unbinding an unrelated action.

Critical menu/navigation controls must remain recoverable even after custom bindings.

## 16. Interface settings

Include:

- UI scale;
- tooltip delay;
- text-size/readability option if implemented separately;
- supported number-format/display preferences;
- first-use tips On/Off;
- Reset window layout.

Window-layout reset affects UI preferences only, not simulation objects/drafts.

UI scale must remain usable in CZ/EN at supported resolutions.

First-use tips are separate from the already completed founding tutorial and can be disabled independently.

## 17. Language

Support:

- Čeština;
- English.

Prefer runtime language switching without application restart.

If a specific technical limitation makes restart unavoidable, the UI must say so before applying; restart-free switching is the desired implementation direction, not permission to silently leave half the UI in the previous language.

Switch all localized surfaces consistently:

- menus;
- windows;
- tooltips;
- errors;
- confirmations;
- tutorials;
- event text;
- accessibility labels where localized.

Player-authored names are not automatically translated.

## 18. Drafts, transient form text and save authority

Distinguish persistent planning data from transient UI editing state.

Examples:

- saved Line/Pattern draft → persistent campaign state;
- accepted order/agreement → persistent campaign state;
- construction plan intentionally saved as a plan → persistent campaign state;
- text typed into an unsubmitted confirmation/form field → not a binding action;
- window geometry → UI preference, not simulation authority.

Saving cannot convert transient form edits into accepted purchases, bids, orders, licences or construction commands.

If transient dirty text would be lost by Load/Main Menu/Quit, include it in the unsaved-change warning where practical.

## 19. UI preferences versus campaign state

Store interface/user preferences separately from authoritative campaign state where practical, including:

- window layout;
- UI scale;
- tooltip delay;
- audio/graphics options;
- control bindings;
- language;
- first-use tip preference.

Loading an older campaign must not roll back the user's graphics/audio/keybindings just because the save was made before those settings changed.

Campaign-specific state such as the selected tutorial completion status remains preserved under UI-D35 where relevant.

## 20. Save browser and deletion safety

Deleting/overwriting a save requires clear target identity.

When overwriting a manual save:

> Replace “Before Austrian expansion”?

Do not confuse overwriting a save file with changing the loaded simulation state.

Deleting a save never deletes the campaign's other slots unless an explicit delete-campaign action exists and is separately confirmed.

Autosave rotation may remove the oldest autosave according to the configured retention policy without a modal each time.

## 21. Accessibility and failure states

All menu/save/settings functions must work with keyboard and mouse.

Use text plus icons/colour for:

- valid/incompatible/corrupt save;
- dirty/unsaved state;
- setting conflicts;
- save success/failure.

A missing save thumbnail/screenshot cannot make the save unusable.

The user must be able to recover from:

- unsupported resolution/UI layout;
- bad key binding;
- failed save;
- corrupt/incompatible slot;
- interrupted load.

## 22. Acceptance evidence to collect

| ID | Required scenario |
|---|---|
| MENUUI-A01 | Main menu with no saves, one campaign and multiple campaigns. Continue selects the latest valid continuation candidate; invalid saves explain why they cannot load. |
| MENUUI-A02 | Create manual, quick and rotating autosaves. Browser groups by campaign/type; autosave cadence is identical in real elapsed play time at 0.5× and 16×. |
| MENUUI-A03 | Interrupt/fail a save write. Previous valid save remains loadable; UI reports failure visibly and no gameplay command/payment/draft is committed by saving. |
| MENUUI-A04 | Load/quickload while running with and without unsaved progress/dirty drafts. Warnings reflect actual lost state and every successful load completes safely paused. |
| MENUUI-A05 | Test pause menu from running 4×, manual pause and critical-event pause. Closing the menu removes only its own pause reason and never auto-resumes another pause cause. |
| MENUUI-A06 | Press Esc during track placement, dirty form editing and ordinary gameplay. Priority order is consistent and does not accidentally discard a draft or open the pause menu prematurely. |
| MENUUI-A07 | Return to main menu/Quit with unsaved progress. Save and exit exits only after successful save; simulated save failure leaves the campaign open. |
| MENUUI-A08 | Change Graphics/Audio/Game/Controls/Interface settings, create a key conflict and reset window layout. Settings affect their actual systems without changing simulation authority. |
| MENUUI-A09 | Switch CZ/EN at runtime where supported, inspect tooltip/error/tutorial/accessibility text and player-authored names. No partial-language state or unwanted name translation. |
| MENUUI-A10 | Save/load after changing user preferences. Campaign authority restores from save while graphics/audio/keybindings/window preferences follow current user settings, not stale campaign copies. |

## 23. Decision record

| ID | Decision | Status |
|---|---|---|
| UI-D36 | Compact main menu, campaign-organized manual/quick/autosaves, atomic save safety, safe paused load, independent pause-menu reason, Esc priority, unsaved-exit protection and Graphics/Audio/Game/Controls/Interface/Language settings | CONFIRMED on 2026-09-30 |

UI-D36 complements UI-D01–UI-D35. It owns the pause-menu lifecycle; UI-D08 is now fully resolved, including focus-loss pause behaviour and the decision not to provide a per-event override matrix in V1.
