#!/usr/bin/env python3
"""Convert a content.md file (with <!-- ===== deck slide N ===== --> markers + ## titles)
into slidev-compatible markdown with layout heuristics.

Usage: python3 to_slidev.py <input.md> <output.md>

Heuristics:
  - text + 1 image    → layout: image-right
  - text + N images   → layout: two-cols (text left, images stacked right)
  - just images       → centered full-bleed
  - just text         → default layout
"""
import importlib.util
import re
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("split_content", _HERE / "split_content.py")
_split = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_split)
SKIP_SLIDES = {k for k, v in _split.MAPPING.items() if v in ("_skip", "_planning")}

NAV_TERMS = {
    "The problems", "Existing solutions", "What's needed",
    "Proposed architecture", "Discussion & outlook", "FAIR",
}

# Per-slide layout overrides: (deck, slide_num) -> layout
LAYOUT_OVERRIDES = {
    ("sydney", 3): "cover",  # speaker intro / title slide
    ("sydney", 12): {"layout": "full-image", "image": "./assets/diagrams/neurodesk-ecosystem-architecture.png"},
    ("sydney", 13): {"layout": "full-image", "image": "./assets/diagrams/neurodesk-ecosystem-architecture-crop-1.png"},
    ("sydney", 14): {"layout": "full-image", "image": "./assets/diagrams/neurodesk-ecosystem-architecture-crop-2.png"},
    ("sydney", 15): {"layout": "full-image", "image": "./assets/diagrams/neurodesk-ecosystem-architecture-crop-3.png"},
    ("sydney", 21): {"layout": "full-image", "image": "./assets/screenshots/screenshot-xnat-dashboard-projects.png"},
    ("sydney", 22): {"layout": "full-image", "image": "./assets/screenshots/screenshot-xnat-mr-session-scans.png"},
    ("sydney", 23): {"layout": "full-image", "image": "./assets/screenshots/screenshot-xnat-jupyter-notebook-launch.png"},
    ("sydney", 24): {"layout": "full-image", "image": "./assets/screenshots/screenshot-jupyterlab-neurodesk-launcher.png"},
    ("sydney", 25): {"layout": "full-image", "image": "./assets/screenshots/screenshot-neurodesk-terminal-module-loading.png"},
    ("sydney", 26): {"layout": "full-image", "image": "./assets/screenshots/screenshot-fsleyes-nifti-file-browser.png"},
    ("sydney", 27): {"layout": "full-image", "image": "./assets/screenshots/neurodesk-desktop-app-menu.png"},
    ("sydney", 28): {"layout": "full-image", "image": "./assets/screenshots/screenshot-neurodesk-mri-viewer.png"},
    ("sydney", 30): {
        "layout": "comparison-arrow",
        "image1": "./assets/screenshots/screenshot-neurocontainers-builder-ui.png",
        "image2": "./assets/screenshots/screenshot-neurocontainers-builder-ui-2.png",
        "cornerImage": "./assets/diagrams/neurocontainers-architecture-stack.png",
    },
    ("sydney", 32): {
        "layout": "image-left-crop",
        "image": "./assets/screenshots/neurodesk-virtual-desktop-screenshot.png",
    },
    ("sydney", 33): {
        "layout": "image-left-crop",
        "image": "./assets/screenshots/screenshot-jupyter-notebook-brain-mri.png",
    },
    ("sydney", 35): {
        "layout": "image-right-contain",
        "image": "./assets/screenshots/screenshot-dicompare-workspace.png",
    },
    ("sydney", 36): {
        "layout": "full-video",
        "video": "./assets/videos/qsmbly-demo.mov",
        "link": "qsmbly.neurodesk.org",
    },
    ("sydney", 37): {
        "layout": "image-left-crop",
        "image": "./assets/screenshots/screenshot-claude-code-neurodesk-bypass-permissions.png",
    },
    ("sydney", 39): {
        "layout": "title-image",
        "image": "./assets/diagrams/open-recon-pipeline-container-build-package-deploy.png",
    },
    ("sydney", 40): {
        "layout": "image-cover-top-title",
        "image": "./assets/screenshots/deep-learning-vessel-segmentation-mra.png",
        "credit": '"image credit: Daniel Güllmar"',
    },
}

# Per-slide logo overrides — replaces auto-detected logos
AIS_LOGOS = [
    "./assets/logos/ais-logo.png",
    "./assets/logos/nif-logo.svg",
    "./assets/logos/ncris-national-research-infrastructure-logo.png",
]
CLOUD_LOGOS = [
    "./assets/logos/ardc-logo.png",
    "./assets/logos/egi-logo.png",
    "./assets/logos/jetstream2-logo.png",
]
LOGO_OVERRIDES = {
    ("sydney", 7): [],   # software logos are content (chaos jumble), not branding
    ("sydney", 10): [],  # software logos are content, not branding
    **{("sydney", n): [] for n in range(21, 29)},  # full-screen screenshots, no pill
    ("sydney", 30): [],  # neurocontainers UI — no pill
    ("sydney", 31): CLOUD_LOGOS,  # cloud servers — ARDC, EGI, Jetstream2
    ("sydney", 32): [],  # virtual desktops — no pill
    ("sydney", 33): [],  # computational notebooks — no pill
    ("sydney", 34): [],  # neurodeskEDU — no pill
    ("sydney", 35): [],  # webassembly — no pill
    ("sydney", 36): [],  # webassembly outlook — no pill
    ("sydney", 37): [],  # coding agents — no pill
    ("sydney", 38): [],  # streamline translation — no pill
    ("sydney", 39): ["./assets/logos/siemens-healthineers-logo.png"],  # Siemens for OpenRecon
    ("sydney", 40): [],  # vessel/brain/prostate — no pill
    ("sydney", 41): [],  # summary — no pill
    **{("sydney", n): AIS_LOGOS for n in range(18, 50) if not (21 <= n <= 28) and n not in (30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41)},
}

# Section assignment per slide (drives the SectionNav highlight)
SECTION_OVERRIDES = {
    # The problems
    **{("sydney", n): "The problems" for n in range(5, 8)},
    # Existing solutions
    **{("sydney", n): "Existing solutions" for n in range(9, 17)},
    # Proposed architecture (skip 21-28 — full-screen screenshots, no nav)
    **{("sydney", n): "Proposed architecture" for n in range(18, 29) if not (21 <= n <= 28)},
    # What's needed
    **{("sydney", n): "What's needed" for n in range(30, 35)},
    # Discussion & outlook
    **{("sydney", n): "Discussion & outlook" for n in range(35, 46)},
}

# Per-slide hand-crafted bodies: (deck, slide_num) -> raw body (overrides auto-render)
MANUAL_BODIES = {
    ("sydney", 5): """# Finding and Sharing Workflows

<div class="flex gap-3 mt-12 items-start">
  <figure class="flex-1 text-center">
    <img src="./assets/graphics/confused-researcher-at-desk-with-programming-languages.png" class="h-64 mx-auto" />
    <figcaption class="mt-4 text-base font-medium">Finding workflows</figcaption>
  </figure>
  <span class="text-5xl text-gray-400 mt-24">→</span>
  <figure class="flex-[2] text-center">
    <img src="./assets/graphics/researcher-error-vs-success-illustration.png" class="h-64 mx-auto" />
    <figcaption class="mt-4 text-base font-medium">Getting the workflows to work<br/>Troubleshooting workflows</figcaption>
  </figure>
  <span class="text-5xl text-gray-400 mt-24">→</span>
  <figure class="flex-1 text-center">
    <img src="./assets/graphics/illustration-researcher-segmentation-error.png" class="h-64 mx-auto" />
    <figcaption class="mt-4 text-base font-medium">Sharing workflows</figcaption>
  </figure>
</div>
""",
    ("sydney", 6): """# Challenges in Scientific Data Analysis

<div class="grid grid-cols-4 gap-6 mt-8">

  <div class="flex flex-col items-center text-center">
    <div class="flex-1 flex flex-col items-center justify-center gap-2">
      <div class="flex gap-1">
        <img src="./assets/figures/brain-cortical-thickness-tmap.jpeg" class="h-16 object-contain" />
        <img src="./assets/figures/freesurfer-cortical-thickness-mean-abs-diff.jpeg" class="h-16 object-contain" />
      </div>
      <img src="./assets/screenshots/glatard-2020-reproducibility-neuroimaging-across-os-paper-title.png" class="h-12 object-contain" />
    </div>
    <h5 class="mt-3">Non-reproducible workflows</h5>
  </div>

  <div class="flex flex-col items-center text-center">
    <div class="flex-1 flex flex-col items-center justify-center gap-2 text-6xl" style="color: var(--c-heading);">
      <figure class="text-center">
        <mdi-laptop class="mx-auto" />
        <figcaption class="text-sm mt-1">Laptop</figcaption>
      </figure>
      <div class="flex gap-4">
        <figure class="text-center">
          <mdi-server class="mx-auto" />
          <figcaption class="text-sm mt-1">HPC</figcaption>
        </figure>
        <figure class="text-center">
          <mdi-cloud class="mx-auto" />
          <figcaption class="text-sm mt-1">Cloud</figcaption>
        </figure>
      </div>
    </div>
    <h5 class="mt-3">Portability</h5>
  </div>

  <div class="flex flex-col items-center text-center">
    <div class="flex-1 flex items-center justify-center">
      <img src="./assets/screenshots/screenshot-file-listing-2dbox-3dbox-demo-npz.png" class="h-28 object-contain" />
    </div>
    <h5 class="mt-3">Data management</h5>
  </div>

  <div class="flex flex-col items-center text-center">
    <div class="flex-1 flex items-center justify-center gap-4 text-5xl" style="color: var(--c-heading);">
      <mdi-database />
      <mdi-lock />
    </div>
    <h5 class="mt-3">Data storage and privacy</h5>
  </div>

</div>

<div class="flex gap-2 items-center justify-center mt-8 mb-12">
  <img src="./assets/graphics/confused-researcher-at-desk-with-programming-languages.png" class="h-24 object-contain" />
  <img src="./assets/graphics/researcher-error-vs-success-illustration.png" class="h-24 object-contain" />
  <img src="./assets/graphics/illustration-researcher-segmentation-error.png" class="h-24 object-contain" />
</div>
""",
    ("sydney", 10): """# What is Neurodesk?

<div class="grid grid-cols-3 gap-6 mt-8 items-center">

  <div class="relative h-72">
    <img src="./assets/logos/mrtrix3-logo.jpeg" class="absolute h-12 object-contain bg-white rounded p-1" style="top: 2%; left: 10%; transform: rotate(-12deg);" />
    <img src="./assets/logos/afni-logo.png" class="absolute h-12 object-contain bg-white rounded p-1" style="top: 12%; left: 60%; transform: rotate(8deg);" />
    <img src="./assets/logos/freesurfer-logo.png" class="absolute h-10 object-contain bg-white rounded p-1" style="top: 25%; left: 25%; transform: rotate(-5deg);" />
    <img src="./assets/logos/fsl-logo.png" class="absolute h-10 object-contain bg-white rounded p-1" style="top: 35%; left: 70%; transform: rotate(-10deg);" />
    <img src="./assets/logos/python-logo.png" class="absolute h-12 object-contain bg-white rounded p-1" style="top: 45%; left: 5%; transform: rotate(15deg);" />
    <img src="./assets/logos/julia-logo.png" class="absolute h-10 object-contain bg-white rounded p-1" style="top: 55%; left: 50%; transform: rotate(-8deg);" />
    <img src="./assets/logos/mne-python-logo.png" class="absolute h-10 object-contain bg-white rounded p-1" style="top: 65%; left: 15%; transform: rotate(6deg);" />
    <img src="./assets/logos/itk-snap-logo.png" class="absolute h-12 object-contain bg-white rounded p-1" style="top: 75%; left: 60%; transform: rotate(10deg);" />
    <img src="./assets/logos/spinal-cord-toolbox-logo.png" class="absolute h-10 object-contain bg-black rounded p-1 ring-4 ring-white" style="top: 85%; left: 25%; transform: rotate(-15deg);" />
  </div>

  <div class="text-center px-4">
    <p class="text-lg leading-relaxed">Neurodesk uses <strong>software containers</strong> to make scientific software accessible.</p>
  </div>

  <div class="flex flex-col items-center bg-white rounded-xl p-4 text-black">
    <img src="./assets/logos/neurodesk-logo.png" class="h-32 object-contain mb-3" />
    <div class="grid grid-cols-3 gap-3 w-full border-t border-gray-200 pt-4">
      <div class="flex items-center justify-center h-14"><img src="./assets/logos/mrtrix3-logo.jpeg" class="max-h-full max-w-full object-contain" /></div>
      <div class="flex items-center justify-center h-14"><img src="./assets/logos/afni-logo.png" class="max-h-full max-w-full object-contain" /></div>
      <div class="flex items-center justify-center h-14"><img src="./assets/logos/freesurfer-logo.png" class="max-h-full max-w-full object-contain" /></div>
      <div class="flex items-center justify-center h-14"><img src="./assets/logos/fsl-logo.png" class="max-h-full max-w-full object-contain" /></div>
      <div class="flex items-center justify-center h-14"><img src="./assets/logos/python-logo.png" class="max-h-full max-w-full object-contain" /></div>
      <div class="flex items-center justify-center h-14"><img src="./assets/logos/julia-logo.png" class="max-h-full max-w-full object-contain" /></div>
      <div class="flex items-center justify-center h-14"><img src="./assets/logos/mne-python-logo.png" class="max-h-full max-w-full object-contain" /></div>
      <div class="flex items-center justify-center h-14"><img src="./assets/logos/itk-snap-logo.png" class="max-h-full max-w-full object-contain" /></div>
      <div class="flex items-center justify-center h-14"><img src="./assets/logos/spinal-cord-toolbox-logo.png" class="max-h-full max-w-full object-contain bg-black rounded p-1" /></div>
    </div>
  </div>

</div>
""",
    ("sydney", 12): "<!-- full-image via layout -->",
    ("sydney", 13): "<!-- full-image via layout -->",
    ("sydney", 14): "<!-- full-image via layout -->",
    ("sydney", 15): "<!-- full-image via layout -->",
    ("sydney", 21): "<!-- full-image via layout -->",
    ("sydney", 22): "<!-- full-image via layout -->",
    ("sydney", 23): "<!-- full-image via layout -->",
    ("sydney", 24): "<!-- full-image via layout -->",
    ("sydney", 25): "<!-- full-image via layout -->",
    ("sydney", 26): "<!-- full-image via layout -->",
    ("sydney", 27): "<!-- full-image via layout -->",
    ("sydney", 28): "<!-- full-image via layout -->",
    ("sydney", 32): """# Virtual Desktops

- **Desktop in a container**
- **Support GUIs**
- **Command line interface**
- **No dependency issues**
- **Software streaming** (CVMFS)
""",
    ("sydney", 33): """# Computational Notebooks

- **Code, docs, results**
- **Software as modules**
- **AI copilots and agents**
- **Sharable, citable, publishable**
- **Teaching and learning platform**
""",
    ("sydney", 35): """# Webapps

- **Browser-native** — no desktop install
- **Local processing** — data never leaves your machine
- **Suited for sensitive patient data**
- **Tools**: dicompare, QSMbly, MuscleMap, VesselBoost
""",
    ("sydney", 36): "<!-- full-video via layout -->",
    ("sydney", 38): """# Could we streamline translation even further?

<div class="flex items-center justify-center gap-3 mt-16">
  <img src="./assets/graphics/translation-step-1-develop.png" class="h-28 w-28 object-contain rounded" />
  <span class="text-4xl" style="color: #5b7c4f;">→</span>
  <img src="./assets/graphics/translation-step-2-acquire.png" class="h-28 w-28 object-contain rounded" />
  <span class="text-4xl" style="color: #5b7c4f;">→</span>
  <img src="./assets/graphics/translation-step-3-export.png" class="h-28 w-28 object-contain rounded" />
  <span class="text-4xl" style="color: #5b7c4f;">→</span>
  <img src="./assets/graphics/translation-step-4-implement.png" class="h-28 w-28 object-contain rounded" />
  <span class="text-4xl" style="color: #5b7c4f;">→</span>
  <img src="./assets/graphics/translation-step-5-integrate.png" class="h-28 w-28 object-contain rounded" />
</div>

<div class="flex items-center justify-center gap-4 mt-8 px-8">
  <p class="font-semibold m-0">Develop analysis pipeline</p>
  <div class="flex-1 flex items-center min-w-0">
    <div class="flex-1 border-t-2 border-dashed" style="border-color: #5b7c4f;"></div>
    <span class="text-3xl -ml-2" style="color: #5b7c4f;">→</span>
  </div>
  <p class="font-semibold m-0">Integrate into clinical workflow</p>
</div>

<div class="flex items-center justify-center flex-wrap gap-x-6 gap-y-2 mt-10 opacity-60">
  <span class="text-base" style="transform: rotate(-4deg); display: inline-block;">programming languages</span>
  <span class="text-sm italic" style="transform: rotate(3deg); display: inline-block;">open-source tools</span>
  <span class="text-lg font-bold" style="transform: rotate(-2deg); display: inline-block;">complex dependencies</span>
  <span class="text-xs" style="transform: rotate(6deg); display: inline-block;">visualisation</span>
  <span class="text-base italic" style="transform: rotate(-3deg); display: inline-block;">versioning</span>
  <span class="text-base font-bold" style="transform: rotate(-5deg); display: inline-block;">…</span>
</div>
""",
    ("sydney", 39): """# Bringing cutting-edge techniques to MRI scanners
""",
    ("sydney", 41): """# Summary

<div class="flex flex-col items-stretch max-w-[700px] gap-3 mt-4">
  <div class="flex items-center gap-4">
    <img src="./assets/graphics/translation-step-1-develop.png" class="h-12 w-12 object-contain rounded flex-shrink-0" />
    <span class="flex-1 px-5 py-3 rounded-lg" style="background: #5b7c4f; color: white;">Develop analysis workflow & build Open Recon package</span>
  </div>
  <div class="flex items-center gap-4">
    <img src="./assets/graphics/translation-step-2-acquire.png" class="h-12 w-12 object-contain rounded flex-shrink-0" />
    <span class="flex-1 px-5 py-3 rounded-lg" style="background: #5b7c4f; color: white;">Run on the scanner using Open Recon</span>
  </div>
</div>

<div class="flex items-center justify-center gap-4 mt-8">

  <div class="text-center px-5 py-5 rounded-xl flex flex-col items-center gap-3 bg-gray-100" style="width: 220px; min-height: 200px;">
    <img src="./assets/logos/neurodesk-logo.png" class="h-20 object-contain" />
    <p class="font-semibold text-xs m-0 leading-snug">Neurodesk makes building software containers accessible</p>
  </div>

  <span class="text-5xl font-bold" style="color: #5b7c4f;">+</span>

  <div class="text-center px-5 py-5 rounded-xl flex flex-col items-center gap-3 bg-gray-100" style="width: 220px; min-height: 200px;">
    <img src="./assets/graphics/mri-scanner-illustration.png" class="h-20 object-contain" />
    <p class="font-semibold text-xs m-0 leading-snug">Open Recon integrates containers into the scanner</p>
  </div>

  <span class="text-5xl font-bold" style="color: #5b7c4f;">=</span>

  <div class="text-center px-5 py-5 rounded-xl flex flex-col items-center gap-3 bg-gray-100" style="width: 220px; min-height: 200px;">
    <mdi-sync class="text-6xl" style="color: #5b7c4f;" />
    <p class="font-semibold text-xs m-0 leading-snug">Faster development and translation cycles</p>
  </div>

</div>

<p class="text-xs opacity-60 mt-6 text-center">🔗 neurodesk.org/getting-started/neurocontainers/openrecon/</p>
""",
    ("sydney", 40): """# Deep learning-based vessel segmentation
""",
    ("sydney", 37): """# Neurodesk + coding agents = analysis agents!

- **Develop analysis code** alongside an AI agent
- **OpenCode** — open-source coding agent
- **Codex** — coding agent from OpenAI
- **Claude Code** — coding agent from Anthropic
- **Notebook Intelligence** — notebook coding agent
- **Sandboxed** in the Neurodesk container
""",
    ("sydney", 34): """# NeurodeskEDU

<p class="absolute top-12 right-12 text-base opacity-70">🔗 neurodesk.org/edu</p>

<div class="flex items-center justify-center mt-4" style="height: 420px;">
  <img src="./assets/screenshots/neurodesk-edu.png" class="max-h-full max-w-full object-contain" />
</div>
""",
    ("sydney", 31): """# Cloud servers

<div class="flex gap-4 mt-4 items-center" style="height: 380px;">
  <div class="flex flex-col gap-3 flex-1 h-full items-center justify-center">
    <img src="./assets/screenshots/neurodesk-play-launch.png" class="max-h-[160px] max-w-full object-contain border border-gray-200 rounded" />
    <div class="flex gap-2 w-full justify-center items-center">
      <img src="./assets/screenshots/neurodesk-play-github-signin.png" class="max-h-[160px] max-w-[62%] object-contain border border-gray-200 rounded" />
      <img src="./assets/screenshots/neurodesk-play-aaf-signin.png" class="max-h-[120px] max-w-[34%] object-contain border border-gray-200 rounded" />
    </div>
  </div>
  <span class="text-5xl text-gray-400 flex-shrink-0">→</span>
  <div class="flex-1 h-full flex items-center justify-center">
    <img src="./assets/screenshots/neurodesk-play-jupyterlab.png" class="max-h-full max-w-full object-contain border border-gray-200 rounded" />
  </div>
</div>

<img src="./assets/diagrams/cloud-servers-corner.png" class="absolute top-4 right-4 h-24 object-contain !opacity-90" />
""",
    ("sydney", 30): """# User Interface to include new tools

<p class="opacity-70">🔗 neurodesk.org/neurocontainers-ui/</p>
""",
    ("sydney", 19): """# What is the Australian Imaging Service?

<p class="text-base italic mt-2 mb-6 opacity-80">Our mission is to increase research reproducibility and drive the adoption of innovative but trusted analysis techniques.</p>

<ul class="space-y-4 text-base">
  <li class="flex items-center gap-4">
    <mdi-account-group class="text-4xl shrink-0" />
    <span>NCRIS invested national platform for collaborative imaging research</span>
  </li>
  <li class="flex items-center gap-4">
    <HealthiconsCtScan class="text-4xl shrink-0" />
    <span>Integration with imaging facilities and clinical sites</span>
  </li>
  <li class="flex items-center gap-4">
    <mdi-lock class="text-4xl shrink-0" />
    <span>Secure, audited data management, access, and deidentification</span>
  </li>
  <li class="flex items-center gap-4">
    <mdi-monitor class="text-4xl shrink-0" />
    <span>Browser accessible viewing, annotation, &amp; analysis</span>
  </li>
  <li class="flex items-center gap-4">
    <mdi-gesture-tap-button class="text-4xl shrink-0" />
    <span>One-click reproducible pipeline library, curated collection and custom developed</span>
  </li>
</ul>
""",
    ("sydney", 18): """# Foundational Digital Research Infrastructure

<ul class="space-y-4 text-lg mt-8 pb-12">
  <li><strong>A consistent data management environment</strong> that could support all NIF nodes</li>
  <li><strong>A technical roadmap</strong> that helps plan for the future</li>
  <li><strong>A support model</strong> for node partners, national-scale projects, data partners and users</li>
  <li><strong>A funding model</strong> that supports continuous improvement and expansion</li>
  <li><strong>An effective infrastructure governance model</strong></li>
  <li><strong>Everything</strong> for $10M project + $2.2M in infrastructure</li>
</ul>
""",
    ("sydney", 16): """# Uptake in the community

<div class="grid grid-cols-2 gap-8 mt-6 items-center">
  <ul class="space-y-3 text-base">
    <li>more than <strong>3,500 monthly users</strong> from over 85 countries</li>
    <li>more than <strong>60,000 downloads</strong></li>
    <li>used in <strong>3 university courses</strong> with more than 100 students (UQ, Wollongong, University of South Carolina)</li>
    <li>used in workshops with more than <strong>50 simultaneous users</strong> (SNIRP 24, VSS 24, MGH Boston 23, CMRR Minnesota 23, Technion Israel 23)</li>
  </ul>
  <div class="bg-white rounded-lg p-4">
    <img src="./assets/figures/world-map-neurodesk-usage-heatmap.png" class="max-h-[60vh] w-full object-contain" />
  </div>
</div>
""",
    ("sydney", 7): """# Installing and maintaining scientific software is not fun…

<div class="relative h-32 mt-6 mb-2">
  <img src="./assets/logos/mrtrix3-logo.jpeg" class="absolute h-10 object-contain bg-white rounded p-1" style="top: 10%; left: 3%; transform: rotate(-12deg);" />
  <img src="./assets/logos/afni-logo.png" class="absolute h-10 object-contain bg-white rounded p-1" style="top: 55%; left: 14%; transform: rotate(8deg);" />
  <img src="./assets/logos/freesurfer-logo.png" class="absolute h-10 object-contain bg-white rounded p-1" style="top: 8%; left: 24%; transform: rotate(-5deg);" />
  <img src="./assets/logos/fsl-logo.png" class="absolute h-10 object-contain bg-white rounded p-1" style="top: 50%; left: 35%; transform: rotate(-10deg);" />
  <img src="./assets/logos/python-logo.png" class="absolute h-10 object-contain bg-white rounded p-1" style="top: 12%; left: 46%; transform: rotate(15deg);" />
  <img src="./assets/logos/julia-logo.png" class="absolute h-10 object-contain bg-white rounded p-1" style="top: 55%; left: 56%; transform: rotate(-8deg);" />
  <img src="./assets/logos/mne-python-logo.png" class="absolute h-10 object-contain bg-white rounded p-1" style="top: 8%; left: 67%; transform: rotate(6deg);" />
  <img src="./assets/logos/itk-snap-logo.png" class="absolute h-10 object-contain bg-white rounded p-1" style="top: 52%; left: 78%; transform: rotate(10deg);" />
  <img src="./assets/logos/spinal-cord-toolbox-logo.png" class="absolute h-10 object-contain bg-black rounded p-1 ring-4 ring-white" style="top: 12%; left: 88%; transform: rotate(-15deg);" />
</div>

<IconRow>
  <IconCell caption="… on your notebook?"><mdi-laptop /></IconCell>
  <IconCell caption="… on your lab workstation?"><mdi-desktop-tower-monitor /></IconCell>
  <IconCell caption="… on a secure environment?"><mdi-lock /></IconCell>
  <IconCell caption="… on a cloud provider?"><mdi-cloud /></IconCell>
  <IconCell caption="… on a high performance cluster?"><mdi-server /></IconCell>
  <IconCell caption="… on an imaging instrument?"><HealthiconsCtScan /></IconCell>
</IconRow>
""",
}


def parse_slide(deck: str, num: str, body: str) -> dict:
    """Pull title, text lines, image refs, and other markers from a slide block."""
    title = None
    text_lines: list[str] = []
    images: list[str] = []
    notes: list[str] = []

    for raw in body.splitlines():
        line = raw.rstrip()
        s = line.strip()
        if not s:
            text_lines.append("")
            continue
        # Title line
        if s.startswith("## "):
            t = s[3:].strip()
            if t.startswith("(untitled"):
                title = None
            else:
                title = t
            continue
        # Image
        m = re.match(r"!\[\]\(([^)]+)\)", s)
        if m:
            images.append(m.group(1))
            continue
        # Strip bare slide-number lines and section nav terms
        bullet = s.lstrip("-").strip()
        if bullet == num:
            continue
        if bullet in NAV_TERMS:
            continue
        # Notes / quote
        if s.startswith(">"):
            notes.append(s)
            continue
        text_lines.append(s)

    # Collapse trailing/leading blanks
    while text_lines and not text_lines[0].strip():
        text_lines.pop(0)
    while text_lines and not text_lines[-1].strip():
        text_lines.pop()

    return {
        "deck": deck, "num": num, "title": title,
        "text": "\n".join(text_lines).strip(),
        "images": images, "notes": notes,
    }


def render(slide: dict) -> str:
    title = slide["title"] or f"_({slide['deck']} slide {slide['num']})_"
    text = slide["text"]
    all_imgs = slide["images"]
    # Separate logos (small branding) from content images (drive layout)
    logos = [i for i in all_imgs if "/logos/" in i]
    imgs = [i for i in all_imgs if i not in logos]
    has_text = bool(text.strip())
    n_imgs = len(imgs)

    fm_lines = []
    body_lines = []

    section = SECTION_OVERRIDES.get((slide["deck"], int(slide["num"])))
    if section:
        fm_lines.append(f'section: "{section}"')

    logo_override = LOGO_OVERRIDES.get((slide["deck"], int(slide["num"])))
    if logo_override is not None:
        logos = list(logo_override)

    # Manual body override: hand-crafted slide body wins over heuristics
    manual = MANUAL_BODIES.get((slide["deck"], int(slide["num"])))
    if manual:
        layout_override = LAYOUT_OVERRIDES.get((slide["deck"], int(slide["num"])))
        if isinstance(layout_override, dict):
            for key, value in layout_override.items():
                fm_lines.append(f"{key}: {value}")
        elif layout_override and layout_override != "cover":
            fm_lines.append(f"layout: {layout_override}")
        if logos:
            fm_lines.append("logos:")
            for logo in logos[:6]:
                fm_lines.append(f"  - {logo}")
        out = ["---", *fm_lines, "---", "", f"<!-- {slide['deck']} slide {slide['num']} (manual) -->", "", manual.rstrip()]
        return "\n".join(out) + "\n"

    override = LAYOUT_OVERRIDES.get((slide["deck"], int(slide["num"])))
    if override == "cover":
        fm_lines = ["layout: cover"]
        body_lines = [f"# {title}", ""]
        if text:
            body_lines.append(text)
    elif has_text and n_imgs == 1:
        fm_lines = [f"layout: image-right", f"image: {imgs[0]}"]
        body_lines = [f"# {title}", "", text]
    elif has_text and n_imgs > 1:
        # Detect caption-grid: multiple short text lines roughly matching image count
        text_lines = [l.strip() for l in text.split("\n") if l.strip()]
        captions = [l for l in text_lines if len(l) < 60 and not l.startswith("-")]
        is_caption_grid = len(captions) >= 2 and len(captions) >= n_imgs - 1 and len(captions) <= n_imgs + 1
        if is_caption_grid:
            cols = min(n_imgs, 4)
            body_lines = [f"# {title}", ""]
            body_lines.append(f'<div class="grid grid-cols-{cols} gap-6 mt-8">')
            for i, img in enumerate(imgs[:cols]):
                cap = captions[i] if i < len(captions) else ""
                body_lines.append('  <div class="flex flex-col items-center text-center">')
                body_lines.append(f'    <img src="{img}" class="h-56 w-auto object-contain" />')
                if cap:
                    body_lines.append(f'    <p class="mt-3 text-sm">{cap}</p>')
                body_lines.append("  </div>")
            body_lines.append("</div>")
        else:
            # two-cols: text left, images stacked right
            fm_lines = [f"layout: two-cols"]
            body_lines = [
                f"# {title}", "",
                text, "",
                "::right::", "",
            ]
            per_h = max(20, 80 // n_imgs)
            for img in imgs[:4]:
                body_lines.append(f'<img src="{img}" class="max-h-[{per_h}%] max-w-full object-contain mx-auto my-2" />')
            if n_imgs > 4:
                body_lines.append(f"<!-- {n_imgs - 4} more images on this slide, manual review -->")
    elif not has_text and n_imgs >= 1:
        # Image-only slide: center first image full-bleed; if collage, stack
        if n_imgs == 1:
            body_lines = [
                f"# {title}", "",
                f'<img src="{imgs[0]}" class="max-h-[80%] max-w-full object-contain mx-auto" />',
            ]
        else:
            body_lines = [f"# {title}", ""]
            per_h = max(15, 70 // n_imgs)
            for img in imgs[:8]:
                body_lines.append(f'<img src="{img}" class="max-h-[{per_h}%] max-w-full object-contain mx-auto my-1" />')
            if n_imgs > 8:
                body_lines.append(f"<!-- {n_imgs - 8} more images, manual review -->")
    else:
        # Text only
        body_lines = [f"# {title}", "", text]

    if logos:
        fm_lines.append("logos:")
        for logo in logos[:6]:
            fm_lines.append(f"  - {logo}")

    out = ["---"]
    out.extend(fm_lines)
    out.append("---")
    out.append("")
    out.append(f"<!-- {slide['deck']} slide {slide['num']} -->")
    out.append("")
    out.extend(body_lines)
    if slide["notes"]:
        out.append("")
        out.extend(slide["notes"])
    return "\n".join(out).rstrip() + "\n"


def main():
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])
    text = src.read_text()
    parts = re.split(r"<!-- ===== (\w+) slide (\d+) =====[^\n]*-->", text)
    # parts: [preamble, deck1, num1, body1, deck2, num2, body2, ...]

    global_config = (
        "theme: default\n"
        "title: AIS / Neurodesk / Sciget master\n"
        "mdc: false\n"
        "fonts:\n"
        "  sans: 'Manrope'\n"
        "  weights: '300,400,500,600,700'\n"
    )

    # Synthetic "recap" slides injected after a given (deck, num)
    INSERT_AFTER = {
        ("sydney", 15): """---
section: "Existing solutions"
layout: full-image
image: ./assets/diagrams/neurodesk-ecosystem-architecture.png
---

<!-- recap: full architecture (after crops) -->
""",
        ("sydney", 35): """---
layout: full-video
video: ./assets/videos/dicompare-demo.mov
link: dicompare.neurodesk.org
---

<!-- dicompare demo video -->
""",
        ("sydney", 37): """---
layout: full-video
video: ./assets/videos/coding-agents-demo.mov
---

<!-- coding agents demo video -->
""",
        ("sydney", 40): """---
layout: image-cover-top-title
image: ./assets/screenshots/screenshot-siemens-healthineers-brain-mri-viewer.png
---

# FSL BET brain extraction
""" + """
---
layout: image-cover-top-title
image: ./assets/screenshots/screenshot-mr-viewgo-pelvic-mri-series.jpeg
credit: "image credit: Jonathan Goodwin"
---

# Deep learning-based prostate fiducial marker detection
""",
        ("sydney", 39): """---
logos:
  - ./assets/logos/siemens-healthineers-logo.png
---

# Open Recon — Neurodesk on the scanner

- **Siemens partnership** — run containers directly on MRIs via the Open Recon feature
- **At point of acquisition** — bring advanced analysis methods into the scanning process
- **FDA approval pathway** — diagnostic workflows possible via Siemens' ecosystem
- **Workflow:** Build container in Neurodesk → package for Open Recon → upload to Siemens C2P → deploy on any Open Recon-enabled scanner
- **Open Recon repository** — packaging and distribution

<div class="flex items-center justify-center mt-8 mb-12">
  <img src="./assets/diagrams/open-recon-pipeline-container-build-package-deploy.png" class="max-h-32 max-w-full object-contain opacity-80" />
</div>
""",
    }

    slides = []
    i = 1
    while i < len(parts):
        deck, num, body = parts[i], parts[i + 1], parts[i + 2]
        if (deck, int(num)) in SKIP_SLIDES:
            i += 3
            continue
        slide = parse_slide(deck, num, body)
        slides.append(render(slide))
        if (deck, int(num)) in INSERT_AFTER:
            slides.append(INSERT_AFTER[(deck, int(num))])
        i += 3

    # Inject global config into the first slide's frontmatter (avoids a blank slide 1)
    if slides:
        slides[0] = slides[0].replace("---\n", f"---\n{global_config}", 1)

    dst.write_text("\n".join(slides))
    print(f"Wrote {dst}")


if __name__ == "__main__":
    main()
