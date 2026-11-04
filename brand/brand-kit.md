# ProfitLane Brand Kit

## Brand idea

ProfitLane is a useful partner for independent dispatchers, with owner-operators as a secondary audience. It brings the details of a load offer into view so dispatchers have better information and leverage in rate conversations. The human dispatcher stays in control. Fair pay for the people doing the hauling is the purpose; the tool supports their work without promising an outcome.

## Default identity

**Version 1 — Amber outline** is the default. It refines the original Option 2 / Concept B roadside badge using charcoal gray, amber and white, with off-white presentation surfaces. The original hexagon vertices, road-edge paths, dashed center-stripe coordinates, rounded square (128 × 128, radius 12), and icon-to-wordmark proportions are retained. The existing outlined-hexagon version is the geometry reference for both active versions; its paths and outline thickness are unchanged.

The full logo keeps its original 440 × 112 viewBox, icon transform `translate(0 8) scale(.75)`, and wordmark at x=114, y=73, bold Arial/Helvetica/system sans-serif, 50 units with -1.5 letter spacing. Full-color lockups have an off-white background and charcoal wordmark.

## Two logo versions

| Version | Hexagon | Road | Center stripe | Square background |
| --- | --- | --- | --- | --- |
| **1 — Default** | Amber outline | White | White | Charcoal gray |
| **2 — Alternative** | Amber outline | White | White | Charcoal gray |

- Version 1: [Full logo](logo.svg) · [Square icon](logo-icon.svg).
- Version 2: [Full logo](logo-v2.svg) · [Square icon](logo-icon-v2.svg).
- Single ink: [One-color logo](logo-one-color.svg), with the original badge outline, road and stripe in charcoal gray, without a square background.

Use Version 1 for the website, social profiles and general communications. Version 2 retains its alternative filenames, with the same approved shape and color treatment as Version 1. The main guide shows both full logos and icons at large size, plus each icon at exactly 48 × 48 CSS pixels. Original B/C exploration assets are retained in `archive/` as historical references, not active brand assets. Their existing geometry is retained, and their colors are updated to charcoal gray, white and amber where the corresponding shapes exist.

## Palette and shared CSS variables

| Variable | Value | Use |
| --- | --- | --- |
| `--color-primary` | `#2B2F33` | Charcoal gray; main brand color and primary controls |
| `--color-secondary` | `#F5A623` | Amber; supporting surfaces with charcoal text |
| `--color-accent` | `#F5A623` | Amber; emphasis on charcoal |
| `--color-text` | `#2B2F33` | Charcoal gray; reading text |
| `--color-background` | `#F7F5F0` | Off-white; page and logo surfaces |
| `--color-success` | `#27653F` | Existing positive status color |
| `--color-warning` | `#875600` | Existing caution status color |
| `--color-error` | `#AD3039` | Existing error status color |
| `--font-heading` | Barlow Condensed | Original Concept B heading family |
| `--font-body` | Barlow | Original Concept B body family |

Full-color symbols use **charcoal gray #2B2F33** for the rounded square, **amber #F5A623** for the hexagon outline, and **white #FFFFFF** for the road and center lane dashes. Full-logo presentation backgrounds remain **off-white #F7F5F0**, with charcoal gray wordmarks. Status colors are separate interface tokens, preserved from the prior default stylesheet. Pair statuses with written labels and symbols, not color alone.

Use charcoal on off-white or amber; use off-white or amber on charcoal. Do not use amber for small text on off-white, off-white text on amber, or status text on amber. Focus outlines use charcoal on the guide’s off-white surface.

## Typography

Use **Barlow Condensed**, weight 600–700, for headings, and **Barlow**, weight 400, 600 or 700, for body text. Both are free Google Fonts. Keep paragraphs in sentence case and body copy at least 16px on phones. The font stacks retain Arial Narrow/Impact/Arial for headings and Segoe UI/Arial for body text so the guide works offline. SVG wordmarks intentionally keep the original Arial/Helvetica/system sans-serif styling; use the supplied logo files rather than retyping them.

## Official tagline

Made for dispatchers by dispatchers.

Use this exact wording and punctuation wherever a tagline is shown. Set it in the existing body font, Barlow, with the existing brand colors.

## Tone of voice

Sound like a knowledgeable colleague: straightforward, helpful, practical and human. Respect dispatchers’ expertise. Be confident about the information, modest about what it predicts and honest about missing inputs. Use concrete words like miles, costs, time and offers. Present the AI as assistance to a person, with the person making the decision. Invite visitors to try the tool and judge its usefulness for themselves.

Example phrases:

- “See what the miles leave on the table.”
- “Use the score as a starting point, then weigh what you know.”
- “You know your trucker. We help you check the numbers.”
- “Some offers need a closer look. Let’s work through the details.”

## Do's and Don'ts

- **Logo:** Use the default files unless explicitly showing the alternative. Preserve proportions and leave at least a quarter of the icon’s width clear around the artwork. Use full logos at 180px wide or larger. Check icons at their actual display size; the guide includes 48px specimens. Don’t alter the road, redraw the hexagon, add shadows or stretch the wordmark.
- **One color:** The single-ink file uses only charcoal gray #2B2F33. A printer may replace every fill with a single ink, black, or white on a dark surface. Do not add a background square that hides the road or put dark artwork on a dark surface.
- **Color:** Keep the symbol to charcoal gray, amber and white, and retain off-white for full-logo presentation surfaces. Keep amber highlights readable by pairing them with charcoal. Use the separate status colors only for interface feedback, with text labels.
- **Social:** Use the square icon, centered. For a circular crop, inset the complete square by about 10% on each side so the hexagon remains visible. Use one clear thought per post and check it on a phone; avoid dense text or the full wordmark inside a tiny profile image.
- **Tone:** Explain a concrete benefit and its limits. Don’t promise higher pay, a perfect score or a risk-free load. Avoid “dominate,” “guaranteed” and “maximum profits.”
- **AI positioning:** Keep dispatchers central. Say “check the offer” or “review the numbers.” Don’t imply autonomous negotiation or replacing dispatchers.
- **Purpose:** Focus on useful support and fair conversations for working people. Avoid dollar signs, wealth imagery, luxury cues and money-first promises.

## Using this folder

Open `index.html` directly in a browser; no server, JavaScript, packages or build step are needed. All local links are relative. Optional Google Fonts loading is the only remote resource; system fallbacks keep all content readable without it. The load score and controls are visual specimens, not working product features. The example 76/100 has no calculated meaning or recommendation threshold.
