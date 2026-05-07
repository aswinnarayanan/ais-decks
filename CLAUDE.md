# ais-decks

Slidev-based presentation decks for AIS / Neurodesk / Sciget.

## Why this repo exists

Aswin runs three streams (AIS umbrella, Neurodesk + Sciget within it). Many talks reuse the same logos, contributor lists, architecture diagrams, FAIR slides. One repo lets all decks share `shared/assets/` and `shared/components/`. Splitting into per-talk repos can happen later if any single deck grows heavy or needs to be public on its own.

## Repo layout

```
ais-decks/
├── shared/
│   ├── assets/        # logos, contributor photos, architecture exports — used across talks
│   ├── components/    # SectionNav.vue and any other reusable Vue components
│   └── styles/        # base style.css overrides
├── <year>-<venue>-<topic>/   # one folder per talk, e.g. 2026-sydney-neurodesk
│   ├── slides.md
│   ├── assets/        # talk-specific images/videos only
│   └── style.css      # talk-specific overrides
├── package.json       # shared slidev deps for all talks
├── .gitattributes     # Git LFS patterns
└── README.md
```

Talks reference shared assets via relative paths: `![](../shared/assets/logos/ais.png)`.

## First talk to migrate: 2026-sydney-neurodesk

Source artefacts live at `~/work/presentations/sydney-2026-slidev/`:
- `slides.md` — 7 slides ported (5 from original pptx + 2 sample slides)
- `assets/` — 8.5MB of images (filenames preserved as `imageNN.ext` for traceability)
- `claude-brainextraction.mov` — demo video (~80MB)
- `style.css` — global CSS overrides
- `components/SectionNav.vue` — section navigation component

Original pptx at `~/work/presentations/sydney-2026-neurodesk-draft.pptx` (291MB, 49 slides, 3 embedded videos). Don't delete — it's the reference for porting the remaining 44 slides.

## Engine choice: Slidev

Evaluated alternatives: Marp, reveal.js, slidesdown, Quarto, Remark.

Picked Slidev because:
- Markdown-first author interface, Vue component escape hatches when needed
- Mermaid + code highlighting + drawings out of the box
- Click-driven motion via `v-click` + `v-motion`
- Aswin's stack already markdown-heavy (Obsidian, LikeC4, Marp, Mermaid)
- Source is plain text, AI-editable, version-controllable

Tradeoffs accepted:
- Heavier than Marp (more deps, ~700 npm packages, ~100MB+ build with assets)
- HTML/Vue creep when layouts get non-trivial
- pptx export = each slide rendered as image (not editable in PowerPoint)
- PDF export loses animations/videos
- `file://` opening of built HTML breaks (ES modules); needs HTTP server

## Conventions

- Theme: `default` (was `seriph` initially, switched after early testing)
- Global slide transition: `transition: fade` in deck-wide frontmatter
- `mdc: false` — keeps it as standard markdown + raw HTML for styling. More portable to GitHub/other renderers than MDC `{class="..."}` syntax
- Image sizing via inline `<img class="...">` (UnoCSS classes) rather than markdown + scoped CSS — keeps everything visible in the slide source
- Reusable Vue components in `shared/components/` (don't duplicate per talk)
- Section navigation: `<SectionNav active="The problems" />` — pass section name to highlight current section in footer

## Slidev gotchas (learned the hard way)

- **`v-motion` click-based animation requires `v-click` on the SAME element** (Vue internal bug per slidev docs). Without `v-click`, `:click-N` variants don't fire
- **`v-click` hides element until clicked**. To keep visible-from-start while still letting v-motion drive motion: `v-click="[0, N]"` range + force `class="!opacity-100"` or set `opacity: 1` in every motion state
- **Click count auto-detected from highest `:click-N`**. Override with `clicks: N` in slide frontmatter
- **Mermaid doesn't auto-fit slide**. Use ` ```mermaid {scale: 0.6}` to scale down. `flowchart TD` (top-down) usually fits slide aspect better than `LR`
- **Mermaid can't be animated per-element** — renders whole SVG at once. Workarounds: multiple progressive blocks, CSS keyframes on generated SVG (fragile), or hand-build with HTML+`v-click`
- **Use `<SlidevVideo>` not raw `<video>`** for videos. Handles slidev-specific concerns (autoreset on slide change, PDF poster). `.mov` files need `type="video/quicktime"` in `<source>`. Convert to `.mp4` (H.264) for cross-browser/Linux Firefox compatibility
- **Default v-click fade** is opacity transition. Snaps text font-weight rendering on lower-DPI screens. Disable with `style.css` rule on `.slidev-vclick-target { transition: none !important; animation: none !important; }`
- **Slide-relative sizing**: prefer `max-height: 70%` (slide-relative) over `max-h-[70vh]` (viewport-relative). vh is unpredictable across screens

## Build / present

```bash
# Dev preview (live reload):
npx slidev <talk-folder>/slides.md

# Static HTML build (per talk):
npx slidev build <talk-folder>/slides.md --base /<repo>/<talk-folder>/

# PDF export (needs playwright-chromium):
npm install -D playwright-chromium
npx slidev export <talk-folder>/slides.md
```

To present: built HTML via any static server (`npx http-server dist`). Direct `file://` opening breaks because of ES module CORS rules. Always serve via HTTP.

## Git LFS (set up from day one)

`.gitattributes`:
```
*.mov filter=lfs diff=lfs merge=lfs -text
*.mp4 filter=lfs diff=lfs merge=lfs -text
*.webm filter=lfs diff=lfs merge=lfs -text
```

GitHub free LFS: 1GB storage + 1GB/month bandwidth. Plenty until you have many video-heavy decks.

## Deployment

- Private repo for now (this is prototype/personal)
- Future: GitHub Pages per talk via per-folder builds + GitHub Actions
- For Sydney 2026: present from local HTML build via `npx http-server dist`. PDF export as fallback if AV booth is locked down

## Naming convention for talks

`<year>-<venue>-<topic>` — sortable, unambiguous, easy to grep:
- `2026-sydney-neurodesk`
- `2026-melbourne-ais` (hypothetical)
- `2027-sciget-launch` (hypothetical)

## Aswin context

NIF Imaging Informatics Fellow at UQ AIBN. Dual (soon triple) stream lead on FDRI/AIS/HIRF without a dedicated PM. Leverages markdown-first stack and AI tooling to compress PM overhead. RSE background, not a traditional academic. Australian English, no em dashes, conversational tone in writing.

## What to do first when picking up this repo

1. Read this file
2. `git status` — check current state
3. Look at `package.json` — confirm slidev version
4. Check which talks exist as subfolders
5. If continuing the Sydney 2026 port: reference `~/work/presentations/sydney-2026-slidev/_extracted/ppt/` for original pptx slide content (44 slides remain)
6. Ask user what they want to work on (new talk, continuing port, theme work, asset additions)
