Social media TikTok files for ProfitLane (TikTok Lead)

# ProfitLane TikTok marketing package

A college-project launch plan and working local content tracker for Angel. All sample performance is fictional. ProfitLane is in development; product videos describe proposed workflows, not verified capabilities. Nothing connects to TikTok or publishes content.

## What is here

- **`index.html`** — interactive studio: overview, calendar, searchable post library and script rehearsal library.
- **`profile-and-strategy.md`** — owner-selected handle, display name, bio, approved-logo guidance, audience, goals, tone, proposed product concepts, link/CTA plan and measurement.
- **`angel-stakeholder-feedback.md`** — Angel’s exact questions/responses, preserved verbatim.
- **`research/`** — the four original research entries and comparison index, preserved as historical research.
- **`content-calendar.md` / `content-calendar.csv`** — 30 daily entries from November 9 to December 8, 2026. Each includes a concept, hook, format, message, caption, hashtags and CTA. Thirteen are publishing days; seventeen are preparation, engagement or review days with reserve ideas.
- **`video-scripts.md`** — first ten scheduled posts, with full scripts, first 2–3 second hooks, scenes, overlays, captions, tags, CTAs and lengths.
- **`content.js`** — reference calendar and scripts read by the tracker. Initial editable posts are drawn from its publishing days.
- **`tracker.js` / `tracker.css`** — dependency-free dashboard behavior and brand styling.
- **`build-content.py`** — curated reference source and optional documentation generator. Requires Python 3, not needed to use the tracker.
- **`tests/tracker.test.cjs`** — browser interaction tests. See testing notes below.

The original one-line folder description above is preserved. Only this folder is changed. The dashboard reads the existing `../brand/brand.css` and logo assets; keep the repository's folder structure intact. It uses the brand font stacks (Barlow/Barlow Condensed when installed, approved system fallbacks otherwise) and makes no font network requests. `brand/HOW-TO-USE.md` was absent when inspected; the brand kit and stylesheet were followed.

## Alignment with Angel's direction

The working handle is **@profitlane.dispatch**, selected by Angel; availability/registration is unverified. Independent dispatchers are the primary audience. Independent operators interested in starting their own dispatching are secondary. Combine educational, professional, casual and relatable delivery to support **brand awareness and attracting potential customers**. Angel is willing to appear and prefers straightforward client-to-client conversations; confirm his background wording and any authentic examples before filming.

AI system tracking is Angel's proposed concept for helping dispatchers identify logistics companies using AI in broker–dispatcher negotiation/communication so they can choose whom to work with. Its method, accuracy and availability are unverified. The proposed 1–100 recommendation score considers weight relative to distance, pre-trip deadhead, diesel prices in relevant areas, pallet count and load payment; it is not a validated profitability or booking decision. Both remain concepts in these materials. The functional TikTok tracker is not evidence of a working ProfitLane dispatching product.

The current draft invites follows once the account is available. Product-exploration and demo-request CTAs are conditional on an approved real page, actual demo and functioning request route; no business email, URL or phone number is invented. The calendar retains 30 days and 13 publishing slots. Existing educational calculations and titles are retained, with targeted updates to founder content, concept explanations and CTAs. Research entries are unchanged observations from before this alignment; read current product positioning in the playbook alongside the exact stakeholder record.

**Existing browser data is preserved:** updated reference scripts/calendar and fresh sample data reflect the revised draft. Your already-saved post copy is not silently overwritten. Export a backup and edit the relevant saved posts manually. Resetting sample data replaces your entire local library and is optional. No account is registered and nothing is published by these changes.

## Open the tracker

**If the chat link shows “an error occurred inside the visualization”:** download `profitlane-tiktok-download.zip`, extract it, and double-click `OPEN-TRACKER.html` in a regular browser. The chat preview is not a reliable way to run this multi-file app. The ZIP includes a self-contained tracker with embedded CSS, JavaScript, approved logos, reference documents and CSV. It requires no installation, server or neighboring brand folder. You can also download `profitlane-tiktok-standalone.html` alone and open it in your browser. Keep the downloaded HTML in the same location for repeat visits; changing browser or file location can change which local data you see. Export/import a backup to transfer work between versions or browsers.

The standalone file is generated by `python3 build-standalone.py` from this folder after updating the source files. Rebuild it after regenerating content or changing the tracker. This also refreshes the ZIP. All generated files stay here; brand files are only read. Documentation links in the standalone version open embedded text documents, and its calendar CSV download is embedded too.

The original repository version remains available:

Open `social-tiktok/index.html` in a current Chrome, Edge, Firefox or Safari with JavaScript enabled. There is no build, npm install or backend. Direct-file storage can vary by browser; for consistent local persistence, serve the repository:

```sh
cd /path/to/MGMT-3450-Team-3
python3 -m http.server 8000 --bind 127.0.0.1
```

Then open the server's `/social-tiktok/` path in your local browser. In a hosted coding workspace use its supported browser access; this package does not create a public preview. The port can be changed if occupied. Use the same address/port/browser to return to the same saved workspace.

## Use the workspace

1. **Overview:** see library size, Published count, known Published views and pooled engagement. Pipeline and pillar bars have visible numeric labels. All charts include the explicitly fictional sample records until you remove them.
2. **Calendar:** use the arrows to browse months or “Launch month” to return to November 2026. Select a scheduled post to edit. Dashed preparation/review prompts and the 30-day cards show the original reference plan. They do not move when you edit a post.
3. **New post:** enter title, description, date, category and status. Expand the copy section for hook, format, caption, tags and CTA. Save, then use Edit to update or Delete to remove (with confirmation). Status is manual: Idea → Planned → Ready → Published. Ready does not mean anything was scheduled on TikTok.
4. **Post library:** search title, description, notes, hook, caption or hashtags. Combine status/category/date filters; bounds include their dates. Clear resets the filters. Filters affect the table only, not overview charts or calendar.
5. **Results:** after publishing manually, paste an HTTPS video URL and enter cumulative views, likes, comments and shares from the same observation time. Use notes for the “as of” date, watch time, qualified questions and one next step. A blank count is unknown; enter `0` only when measured. Counts must be nonnegative whole numbers. A URL does not verify that the video exists.
6. **Engagement:** `(likes + comments + shares) / views × 100`. All four metrics are needed and views must exceed zero. Otherwise show `—`; zero views does not produce an infinite rate. The editor/table calculate a per-post rate regardless of status. The overview pools only Published records with complete positive-view data: total eligible interactions ÷ total eligible views. It is not a mean of percentages, and excludes saves. See strategy for measurement limits.
7. **Backup:** Export backup downloads versioned JSON for all current posts, regardless of filters. Import JSON validates records and asks before replacing the current workspace. Unknown categories/statuses, negative/fractional counts, invalid dates and unsafe URL protocols are rejected. Maximum 2,000 posts / 5 MB import. Reset to sample data also requires confirmation. Export before resetting or importing.

Browser localStorage is not a shared database, cloud sync or automatic backup. Clearing site data, changing browser/profile/address or using private mode can lose access to it. If storage is blocked/full the app keeps session edits and warns you to export. If saved data is unreadable, the original stored value is protected, samples appear, and edits are session-only until a deliberate import/reset. Avoid editing in multiple tabs; a notice appears if another tab changes the stored workspace. Exported files can contain sensitive notes, so keep real customer details out.

## Update the content calendar

For everyday use, edit a post's date, copy, status or category inside the tracker; its calendar entry, table, statistics and charts update together. The launch plan is a suggested window, not an automated schedule. Add desired time and audience time zone to notes (for example “test 6 p.m. Central”); the date field does not schedule publication or convert time zones.

To move the whole launch, edit each planned date and compare the resulting calendar. For a non-publishing day, use the reference idea as a reserve and create a post only if you decide to publish it. Export a backup after planning. The browser's edits do **not** rewrite the Markdown, CSV or script library.

For repository reference changes, edit the curated concepts, dates and scripts in `build-content.py`, then run from this folder:

```sh
python3 build-content.py
```

This intentionally regenerates `content.js`, `content-calendar.md`, `content-calendar.csv` and `video-scripts.md`. Check those files for other students' edits first; do not run the generator blindly over their work. Existing browser data stays untouched: importing a backup or explicitly resetting starts a changed reference set. The generator does not alter strategy, branding, application code or other folders.

## Launch with Angel

Confirm account name availability and founder wording; obtain permission for any personal story. Review the package together. Replace/delete the three fictional Published samples before measuring a real account. Update dates to the actual launch, rehearse scripts, check arithmetic and fictional-data labels, then mark reviewed videos Ready. Use original/approved audio, check captions and never film while driving. Product concepts must keep the in-development/unvalidated labels. No guaranteed rate improvements, earnings, validated scores or customer results are claimed here.

Use the existing default square logo for the profile; see the playbook for safe cropping. Add a profile link only to Angel's approved real destination and only when eligible. Until usable access exists, invite follows and questions rather than claiming a trial is available. Publish manually after Angel's review. Enter actual metrics consistently, compare equal windows each week, and choose the next topic from useful questions and measured interest.

## Testing

The tracker has no runtime dependencies. Its optional browser test uses an existing Playwright installation and Chromium. It writes temporary browser profiles and test artifacts only under `social-tiktok/.runtime/` and `social-tiktok/tests/artifacts/` (ignored). Test a fresh workspace, not your personal live tracker data.

From the repository root, using an environment with `playwright` available to Node:

```sh
node social-tiktok/tests/tracker.test.cjs
```

The test starts its own local HTTP server on an available port, exercises a separate browser profile and closes its own server/browser afterward. It does not contact TikTok. In restricted coding sandboxes, browser and socket creation may require the platform's supported execution permission. See `tests/RESULTS.md` for the actual checks run and their results.

### Portable download checks

`TRACKER_ENTRY=profitlane-tiktok-standalone.html node social-tiktok/tests/tracker.test.cjs` runs the interaction suite against the portable build. `node social-tiktok/tests/portable.test.cjs` serves the HTML as the only file in an isolated directory and checks embedded branding, documents, CSV, saved edits and the absence of external resource requests. Direct file navigation cannot be verified in this managed Chromium because its policy blocks `file://` pages; a regular desktop browser is the intended downloaded-file viewer.
