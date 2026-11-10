# Tracker validation

Executed November 9, 2026 using Playwright and system Chromium against an isolated local HTTP server. All requests were local; no TikTok account was contacted.

- PASS: Initial dashboard, exact pooled engagement, visible charts and approved logos
- PASS: Ten complete scripts accessible in the playbook
- PASS: Ten timed scripts expose exact commentary with synchronized visuals and readable timecodes
- PASS: Owner-selected handle, precise audience, goals, tone, proposed concepts and conditional demo CTA are visible
- PASS: 30-day plan, 13 publishing slots, month navigation and preparation detail dialog
- PASS: Create, metric entry, live engagement, pooled overview update, escaped text and reload persistence
- PASS: Edit synchronizes calendar; unknown/zero metrics and invalid numbers/unsafe URLs handled
- PASS: Combined search/status/category/inclusive-date filters and empty state
- PASS: JSON export contains entire workspace even after filters
- PASS: Delete confirmation, cancellation and persisted removal
- PASS: Import validation rejects invalid dates/unsafe links; cancellation and backup restoration work
- PASS: Reset requires confirmation and restores fictional samples
- PASS: Keyboard Escape closes modal and restores focus
- PASS: All four views fit a 390px mobile viewport
- PASS: Unreadable saved data is warned about and not overwritten
- PASS: Empty workspace and no-denominator engagement state
- PASS: Storage failure retains session work and clearly requests export
- PASS: No uncaught browser JavaScript errors

Screenshots and exported test backup are ignored under `tests/artifacts/`. Browser temporary files are ignored under `.runtime/`. These checks exercise the demonstration UI, not TikTok or a live ProfitLane product.
