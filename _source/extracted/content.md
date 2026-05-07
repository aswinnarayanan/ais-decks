# Master content (extracted from pptx)

Combined source-of-truth markdown for AIS / Neurodesk / Sciget content.
Each section below is one deck. Slide markers (`<!-- ===== deck slide N ===== -->`)
preserve provenance back to the original pptx.

Edit freely. Once topic boundaries are clear, split into `content/<stream>/<topic>.md`.

---

# Deck: sydney

_Source: `sydney-2026-neurodesk-draft.pptx` (49 slides)_

<!-- ===== sydney slide 1 ===== -->
## Workshops

Neurodesk app demo

Play.neurodesk.cloud.edu.au

How to upload/download data. Use ui

Demo tools notebook in edu

Ipyniivue integration

Will update play Australia image

Agent live demo

Mention AIS XNAT demo, HPC integration


1

<!-- ===== sydney slide 2 ===== -->
## Presentation

Agents – reuse claude code video

Webapps – qsmbly

, vesselboost, musclemap, dicompare

Openrecon

Neurodeskedu

AIS


2

<!-- ===== sydney slide 3 ===== -->
## Neurodesk overview

Aswin Narayanan

The University of Queensland

National Imaging Facility


3


![](./assets/logos/nif-logo.svg)

![](./assets/logos/uq-logo.svg)

<!-- ===== sydney slide 4 ===== -->
## Today’s roadmap

4


- 1

- 3

- 5

- 4

- 2

- What are the problems?

- What’s
- needed

- Discussion
- &
- Outlook

- Existing
- Solutions

- Proposed
- Architecture

- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/graphics/sciget-mascot-bilby-bicycle.png)

![](./assets/logos/neurodesk-logo-3.png)

![](./assets/graphics/winding-road-graphic.png)

<!-- ===== sydney slide 5 ===== -->
## Finding and Sharing Workflows

5


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

Finding workflows


Getting the  workflows to work


Troubleshooting workflows


Sharing workflows


![](./assets/graphics/confused-researcher-at-desk-with-programming-languages.png)

![](./assets/graphics/illustration-researcher-segmentation-error.png)

![](./assets/graphics/researcher-error-vs-success-illustration.png)

<!-- ===== sydney slide 6 ===== -->
## Challenges in Scientific Data Analysis

6


- Non-reproducible workflows

notebook


cloud provider


HPC cluster


- Data management

- Data storage and privacy

- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/figures/freesurfer-cortical-thickness-mean-abs-diff.jpeg)

![](./assets/figures/brain-cortical-thickness-tmap.jpeg)

![](./assets/icons/icon-laptop-3.png)

![](./assets/icons/icon-cloud-computing.png)

![](./assets/icons/icon-server-monitor-data-storage.png)

![](./assets/screenshots/screenshot-file-listing-2dbox-3dbox-demo-npz.png)

![](./assets/icons/icon-automated-workflow-system.png)

![](./assets/icons/icon-cloud-server.png)

![](./assets/screenshots/glatard-2020-reproducibility-neuroimaging-across-os-paper-title.png)

> **EMF/WMF (manual convert):** `media/image39.emf`

<!-- ===== sydney slide 7 ===== -->
## Installing and maintaining scientific software is not fun …

7


… on your

notebook?


… on your lab workstation?


… on a cloud

provider?


… on a high

performance cluster?


… on a secure environment?


- ?

… on an

imaging instrument?


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/icons/icon-laptop.png)

![](./assets/icons/icon-desktop-computer-tower.png)

![](./assets/icons/icon-cloud-computer.png)

![](./assets/icons/server-rack-laptop-terminal.png)

![](./assets/screenshots/fsl-fmri-analysis-screenshot.png)

![](./assets/logos/mrtrix3-logo.jpeg)

![](./assets/figures/ants-brain-normalization.jpeg)

![](./assets/screenshots/bart-toolbox-mri-code-banner.png)

![](./assets/logos/spinal-cord-toolbox-logo.png)

![](./assets/logos/afni-logo.png)

![](./assets/logos/julia-logo.png)

![](./assets/logos/freesurfer-logo.png)

![](./assets/logos/python-logo-2.png)

![](./assets/logos/itk-snap-logo.png)

![](./assets/logos/logo-partition-magic.png)

![](./assets/icons/icon-ct-mri-scanner.png)

<!-- ===== sydney slide 8 ===== -->
## Today’s roadmap

8


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

- 1

- 3

- 5

- 4

- 2

- What are the problems?

- What’s
- needed

- Discussion
- &
- Outlook

- Existing
- Solutions

- Proposed
- Architecture

![](./assets/graphics/sciget-mascot-bilby-bicycle.png)

![](./assets/graphics/winding-road-graphic.png)

![](./assets/logos/neurodesk-logo-3.png)

<!-- ===== sydney slide 9 ===== -->
## Neurodesk contributors

![](./assets/graphics/contributor-map.png)


<!-- ===== sydney slide 10 ===== -->
## What is Neurodesk?

10


- Neurodesk uses software containers to make scientific software
- accessible

- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/screenshots/screenshot-fsl-feat-fmri-analysis.png)

![](./assets/logos/mrtrix3-logo.jpeg)

![](./assets/figures/ants-brain-normalization.jpeg)

![](./assets/screenshots/bart-mri-reconstruction-code.png)

![](./assets/logos/spinal-cord-toolbox-logo.png)

![](./assets/logos/afni-logo.png)

![](./assets/logos/julia-logo.png)

![](./assets/logos/freesurfer-logo.png)

![](./assets/logos/python-logo-2.png)

![](./assets/logos/itk-snap-logo.png)

![](./assets/logos/logo-virtualbox.png)

![](./assets/logos/neurodesk-logo-4.png)

![](./assets/logos/mrtrix3-logo.jpeg)

![](./assets/figures/ants-brain-normalization.jpeg)

![](./assets/logos/spinal-cord-toolbox-logo.png)

![](./assets/logos/afni-logo.png)

![](./assets/logos/freesurfer-logo.png)

![](./assets/logos/python-logo-2.png)

![](./assets/logos/itk-snap-logo.png)

![](./assets/logos/logo-virtualbox.png)

<!-- ===== sydney slide 11 ===== -->
## (untitled slide 11)

11


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/diagrams/neurodesk-ecosystem-architecture.png)

<!-- ===== sydney slide 12 ===== -->
## Reproducible workflows

12


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/diagrams/neurodesk-ecosystem-architecture.png)

<!-- ===== sydney slide 13 ===== -->
## Portable to different infrastructure

13


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/diagrams/neurodesk-ecosystem-architecture.png)

<!-- ===== sydney slide 14 ===== -->
## (untitled slide 14)

14


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/diagrams/neurodesk-ecosystem-architecture.png)

![](./assets/graphics/sciget-bilby-trio-working.png)

<!-- ===== sydney slide 15 ===== -->
## (untitled slide 15)

15


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/diagrams/neurodesk-ecosystem-architecture.png)

<!-- ===== sydney slide 16 ===== -->
## Uptake in the community

more than 3500 monthly users from over 85 countries

more than 60 000 downloads

currently used in 3 university courses with more than 100 students (UQ, Wollongong and University of South Carolina)

used in workshops with more than 50 simultaneous users (e.g. SNIRP 24, VSS 24, MGH Boston 23, CMRR Minnesota 23, Technion Israel 23)


16


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/figures/world-map-neurodesk-usage-heatmap.png)

<!-- ===== sydney slide 17 ===== -->
## Today’s roadmap

17


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

- 1

- 3

- 5

- 4

- 2

- What are the problems?

- What’s
- needed

- Discussion
- &
- Outlook

- Existing
- Solutions

- Proposed
- Architecture

![](./assets/graphics/sciget-mascot-bilby-bicycle.png)

![](./assets/graphics/winding-road-graphic.png)

![](./assets/logos/neurodesk-logo-3.png)

<!-- ===== sydney slide 18 ===== -->
## Foundational Digital Research Infrastructure

          - A consistent data management environment that could support all NIF nodes
          - A technical roadmap that helps plan for the future
          - A support model for node partners, national-scale projects, data partners and users
          - A funding model that supports continuous improvement and expansion
          - An effective infrastructure governance model
          - $10M project + $2.2M in infrastructure

18


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/logos/ncris-national-research-infrastructure-logo.png)

![](./assets/logos/ais-logo.png)

<!-- ===== sydney slide 19 ===== -->
## What is the Australian Imaging Service?

19


Our mission is to increase research reproducibility and drive the adoption of innovative but trusted analysis techniques.

NCRIS invested national platform for collaborative imaging research.

Integration with imaging facilities and clinical sites

Secure, audited data management, access, and deidentification

Browser accessible viewing, annotation, & analysis

One-click reproducible pipeline library, curated collection and custom developed


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/logos/ncris-national-research-infrastructure-logo.png)

![](./assets/logos/ais-logo.png)

<!-- ===== sydney slide 20 ===== -->
## AIS Architecture

20


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/diagrams/ais-platform-architecture-overview.png)

![](./assets/logos/ncris-national-research-infrastructure-logo.png)

![](./assets/logos/ais-logo.png)

<!-- ===== sydney slide 21 ===== -->
## (untitled slide 21)

21


![](./assets/screenshots/screenshot-xnat-dashboard-projects.png)

<!-- ===== sydney slide 22 ===== -->
## (untitled slide 22)

22


![](./assets/screenshots/screenshot-xnat-mr-session-scans.png)

<!-- ===== sydney slide 23 ===== -->
## (untitled slide 23)

23


![](./assets/screenshots/screenshot-xnat-jupyter-notebook-launch.png)

<!-- ===== sydney slide 24 ===== -->
## (untitled slide 24)

24


![](./assets/screenshots/screenshot-jupyterlab-neurodesk-launcher.png)

<!-- ===== sydney slide 25 ===== -->
## (untitled slide 25)

25


![](./assets/screenshots/screenshot-neurodesk-terminal-module-loading.png)

<!-- ===== sydney slide 26 ===== -->
## (untitled slide 26)

26


![](./assets/screenshots/screenshot-fsleyes-nifti-file-browser.png)

<!-- ===== sydney slide 27 ===== -->
## (untitled slide 27)

27


![](./assets/screenshots/neurodesk-desktop-app-menu.png)

<!-- ===== sydney slide 28 ===== -->
## (untitled slide 28)

28


![](./assets/screenshots/screenshot-neurodesk-mri-viewer.png)

<!-- ===== sydney slide 29 ===== -->
## Today’s roadmap

29


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

- 1

- 3

- 5

- 4

- 2

- What are the problems?

- What’s
- needed

- Discussion
- &
- Outlook

- Existing
- Solutions

- Proposed
- Architecture

![](./assets/graphics/sciget-mascot-bilby-bicycle.png)

![](./assets/graphics/winding-road-graphic.png)

![](./assets/logos/neurodesk-logo-3.png)

<!-- ===== sydney slide 30 ===== -->
## User Interface to include new tools

30


🔗 neurodesk.org/neurocontainers-ui/


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/screenshots/screenshot-neurocontainers-builder-ui.png)

![](./assets/diagrams/neurocontainers-architecture-stack.png)

![](./assets/screenshots/screenshot-container-release-progress-dashboard.png)

<!-- ===== sydney slide 31 ===== -->
## Cloud servers

31


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/screenshots/neurodesk-play-website.png)

![](./assets/screenshots/neurodesk-play-jupyterhub-login.png)

![](./assets/screenshots/screenshot-neurodesk-jupyterhub-server-options.png)

![](./assets/screenshots/screenshot-neurodesk-jupyterlab-launcher.png)

> **EMF/WMF (manual convert):** `media/image98.emf`

<!-- ===== sydney slide 32 ===== -->
## Virtual Desktops

32


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/screenshots/neurodesk-virtual-desktop-screenshot.png)

![](./assets/logos/neurodesk-logo.png)

> **EMF/WMF (manual convert):** `media/image98.emf`

<!-- ===== sydney slide 33 ===== -->
## ComputationalNotebooks

33


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/screenshots/screenshot-jupyter-notebook-brain-mri.png)

![](./assets/screenshots/screenshot-neurodesk-ipyniivue-visualization.png)

> **EMF/WMF (manual convert):** `media/image98.emf`

<!-- ===== sydney slide 34 ===== -->
## NeurodeskEDU

34


https://neurodesk.org/edu/


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/diagrams/neurodesk-learning-resources-tutorials-examples.png)

<!-- ===== sydney slide 35 ===== -->
## WebAssembly to compute client-side in the browser

https://dicompare.neurodesk.org


35


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/screenshots/screenshot-dicompare-workspace.png)

> **VIDEO (manual):** `media/media1.mov`

<!-- ===== sydney slide 36 ===== -->
## Outlook - WebAssembly to compute client-side in the browser

https://qsmbly.neurodesk.org/


36


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/screenshots/screenshot-qsmbly-browser-app.png)

> **VIDEO (manual):** `media/media2.mov`

<!-- ===== sydney slide 37 ===== -->
## Neurodesk + coding agents = analysis agents!

37


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/screenshots/screenshot-claude-code-neurodesk-bypass-permissions.png)

> **VIDEO (manual):** `media/media3.mov`

<!-- ===== sydney slide 38 ===== -->
## Could we streamline translation even further?

38


?


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

<!-- ===== sydney slide 39 ===== -->
## Bringing cutting-edge techniques to MRI scanners

39


FDA approval for diagnostic workflows


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/diagrams/open-recon-pipeline-container-build-package-deploy.png)

![](./assets/logos/siemens-healthineers-logo.png)

<!-- ===== sydney slide 40 ===== -->
## Deep learning-based vessel segmentation

image credit: Daniel Güllmar


40


image credit: Daniel Güllmar


FSL BET brain extraction


image credit: Jonathan Goodwin


Deep learning-based prostate fiducial marker detection


https://neurodesk.org/getting-started/neurocontainers/openrecon/


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/screenshots/deep-learning-vessel-segmentation-mra.png)

![](./assets/screenshots/screenshot-siemens-healthineers-brain-mri-viewer.png)

![](./assets/screenshots/screenshot-mr-viewgo-pelvic-mri-series.jpeg)

<!-- ===== sydney slide 41 ===== -->
## Summary

41


https://neurodesk.org/getting-started/neurocontainers/openrecon/


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/logos/neurodesk-logo-4.png)

> **EMF/WMF (manual convert):** `media/image122.emf`

<!-- ===== sydney slide 42 ===== -->
## WP11: making analyses more accessible :coding agents + sciget = analysis agents

42


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/screenshots/screenshot-claude-code-neurodesk-bypass-permissions.png)

> **VIDEO (manual):** `media/media3.mov`

<!-- ===== sydney slide 43 ===== -->
## Enable various collaboration models

43


Centralised  collaboration


Decentralised  collaboration


Dao et al., 2025


- Data privacy
- assurance

- Simplified data management

- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

> **EMF/WMF (manual convert):** `media/image123.emf`
> **EMF/WMF (manual convert):** `media/image123.emf`

<!-- ===== sydney slide 44 ===== -->
## Open Data workflow in Neurodesk

44


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

> **EMF/WMF (manual convert):** `media/image124.emf`

<!-- ===== sydney slide 45 ===== -->
## (untitled slide 45)

45


Masson-Trottier et al., 2025, Aperture Neuro


- FAIR

- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/diagrams/sciget-reproducible-workflow-architecture.jpeg)

<!-- ===== sydney slide 46 ===== -->
## Today’s roadmap

46


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

- 1

- 3

- 5

- 4

- 2

- What are the problems?

- What’s
- needed

- Discussion
- &
- Outlook

- Existing
- Solutions

- Proposed
- Architecture

![](./assets/graphics/sciget-mascot-bilby-bicycle.png)

![](./assets/graphics/winding-road-graphic.png)

![](./assets/logos/neurodesk-logo-3.png)

<!-- ===== sydney slide 47 ===== -->
## Roadmap

47


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/logos/github-copilot-logo.jpeg)

![](./assets/logos/github-actions-logo.png)

![](./assets/logos/neurodesk-logo-2.png)

![](./assets/logos/ardc-logo.png)

![](./assets/logos/open-science-grid-logo.png)

![](./assets/logos/egi-logo.png)

![](./assets/logos/jetstream2-logo.png)

![](./assets/logos/ais-logo.png)

![](./assets/logos/jupyter-logo.png)

![](./assets/logos/oracle-cloud-infrastructure-logo.jpeg)

![](./assets/logos/cernvm-file-system-logo.png)

![](./assets/logos/gitops-logo.png)

![](./assets/logos/nif-logo.svg)

![](./assets/logos/kubernetes-logo.png)

![](./assets/logos/wellcome-logo.png)

![](./assets/logos/chan-zuckerberg-initiative-logo.jpeg)

![](./assets/logos/xnat-logo.png)

![](./assets/logos/doi-logo.png)

![](./assets/logos/siemens-healthineers-logo-2.png)

![](./assets/logos/aws-logo-2.png)

<!-- ===== sydney slide 48 ===== -->
## Support and acknowledgements

48


  - NIF co-investment (1M AUD)
  - ARDC platform grant 2020-2023 (650k AUD)
  - EOSS6 2024 – 2026 (600k AUD)
  - UQ Global Development funding (8K AUD)

Grant Funding


  - > 10 active contributors
  - hosting of CVMFS through Open Science Grid, EGI and JetStream2

Community


  - ARDC Nectar Cloud (since 2021)
  - AWS (since 2024)
  - EGI (since 2024)
  - Google Cloud (since 2023)
  - JetStream2 (since 2023)
  - Oracle Cloud (2021 – 2023)

Support from Cloud providers


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/logos/qcif-logo.png)

![](./assets/logos/open-science-grid-logo.png)

![](./assets/logos/egi-logo-2.png)

![](./assets/logos/ardc-logo.png)

![](./assets/logos/aws-logo-2.png)

![](./assets/logos/google-cloud-logo.png)

![](./assets/logos/oracle-cloud-infrastructure-logo.jpeg)

![](./assets/logos/nif-logo.svg)

![](./assets/logos/uq-logo.png)

![](./assets/logos/swinburne-university-logo.png)

![](./assets/logos/university-of-sydney-logo.png)

![](./assets/logos/wellcome-logo-2.png)

![](./assets/logos/chan-zuckerberg-initiative-logo.png)

<!-- ===== sydney slide 49 ===== -->
## Thank you!

49


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

- Communities

- Data repositories and collections

- Domains and Flavours

- Infrastructure

sciget.org

neurodesk.org

---

# Deck: sciget

_Source: `eresearch-2025-sciget-final.pptx` (58 slides)_

<!-- ===== sciget slide 1 ===== -->
## SCIGETMaking Scientific Software Accessible

Aswin Narayanan


1


![](./assets/logos/nif-logo.svg)

<!-- ===== sciget slide 2 ===== -->
## Today’s roadmap

2


- 1

- 3

- 5

- 4

- 2

- What are the problems?

- What’s
- needed

- Discussion
- &
- Outlook

- Existing
- Solutions

- Proposed
- Architecture

- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/graphics/sciget-mascot-bilby-bicycle.png)

![](./assets/logos/sciget-logo.png)

![](./assets/graphics/winding-road-graphic.png)

<!-- ===== sciget slide 3 ===== -->
## The need for FAIR analyses

… Findability, Accessibility, Interoperability, and Reusability …

principles apply not only to ‘data’ in the conventional sense, but also to the algorithms, tools, and workflows that led to that data.


3


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

Wilkinson, M. D. et al. The FAIR Guiding Principles for scientific data management and stewardship.

<!-- ===== sciget slide 4 ===== -->
## Challenges in Scientific Data Analysis

4


- Non-reproducible workflows

notebook


cloud provider


HPC cluster


- Data management

- Data storage and privacy

- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/figures/freesurfer-cortical-thickness-mean-abs-diff.jpeg)

![](./assets/figures/brain-cortical-thickness-tmap.jpeg)

![](./assets/icons/icon-laptop-3.png)

![](./assets/icons/icon-cloud-computing.png)

![](./assets/icons/icon-server-monitor-data-storage.png)

![](./assets/screenshots/screenshot-file-listing-2dbox-3dbox-demo-npz.png)

![](./assets/icons/icon-automated-workflow-system.png)

![](./assets/icons/icon-cloud-server.png)

![](./assets/screenshots/glatard-2020-reproducibility-neuroimaging-across-os-paper-title.png)

> **EMF/WMF (manual convert):** `media/image27.emf`

<!-- ===== sciget slide 5 ===== -->
## Finding and Sharing Workflows

5


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

Finding workflows


Getting the  workflows to work


Troubleshooting workflows


Sharing workflows


![](./assets/graphics/confused-researcher-at-desk-with-programming-languages.png)

![](./assets/graphics/illustration-researcher-segmentation-error.png)

![](./assets/graphics/researcher-error-vs-success-illustration.png)

<!-- ===== sciget slide 6 ===== -->
## Installing and maintaining scientific software is not fun …

6


… on your

notebook?


… on your lab workstation?


… on a cloud

provider?


… on a high

performance cluster?


… on a secure environment?


- ?

… on an

imaging instrument?


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/icons/icon-laptop.png)

![](./assets/icons/icon-desktop-computer-tower.png)

![](./assets/icons/icon-cloud-computer.png)

![](./assets/icons/server-rack-laptop-terminal.png)

![](./assets/icons/icon-safe-vault.png)

![](./assets/icons/icon-desktop-monitor.png)

![](./assets/icons/icon-desktop-monitor.png)

![](./assets/icons/icon-padlock.png)

![](./assets/icons/icon-padlock.png)

![](./assets/screenshots/fsl-fmri-analysis-screenshot.png)

![](./assets/logos/mrtrix3-logo.jpeg)

![](./assets/figures/ants-brain-normalization.jpeg)

![](./assets/screenshots/bart-toolbox-mri-code-banner.png)

![](./assets/logos/spinal-cord-toolbox-logo.png)

![](./assets/logos/afni-logo.png)

![](./assets/logos/julia-logo.png)

![](./assets/logos/freesurfer-logo.png)

![](./assets/logos/python-logo-2.png)

![](./assets/logos/itk-snap-logo.png)

![](./assets/logos/logo-partition-magic.png)

![](./assets/icons/icon-ct-mri-scanner.png)

<!-- ===== sciget slide 7 ===== -->
## Today’s roadmap

7


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

- 1

- 3

- 5

- 4

- 2

- What are the problems?

- What’s
- needed

- Discussion
- &
- Outlook

- Existing
- Solutions

- Proposed
- Architecture

![](./assets/graphics/sciget-mascot-bilby-bicycle.png)

![](./assets/graphics/winding-road-graphic.png)

![](./assets/logos/sciget-logo.png)

<!-- ===== sciget slide 8 ===== -->

# Neurodesk contributors

![](./assets/graphics/contributor-map.png)

A global community of researchers, engineers, and supporters.


<!-- ===== sciget slide 9 ===== -->
## What is Neurodesk?

9


- Neurodesk uses software containers to make scientific software
- accessible

- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/screenshots/screenshot-fsl-feat-fmri-analysis.png)

![](./assets/logos/mrtrix3-logo.jpeg)

![](./assets/figures/ants-brain-normalization.jpeg)

![](./assets/screenshots/bart-mri-reconstruction-code.png)

![](./assets/logos/spinal-cord-toolbox-logo.png)

![](./assets/logos/afni-logo.png)

![](./assets/logos/julia-logo.png)

![](./assets/logos/freesurfer-logo.png)

![](./assets/logos/python-logo-2.png)

![](./assets/logos/itk-snap-logo.png)

![](./assets/logos/logo-virtualbox.png)

![](./assets/logos/neurodesk-logo-4.png)

![](./assets/logos/mrtrix3-logo.jpeg)

![](./assets/figures/ants-brain-normalization.jpeg)

![](./assets/logos/spinal-cord-toolbox-logo.png)

![](./assets/logos/afni-logo.png)

![](./assets/logos/freesurfer-logo.png)

![](./assets/logos/python-logo-2.png)

![](./assets/logos/itk-snap-logo.png)

![](./assets/logos/logo-virtualbox.png)

<!-- ===== sciget slide 10 ===== -->
## (untitled slide 10)

10


- Next section

- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/diagrams/neurodesk-ecosystem-architecture.png)

<!-- ===== sciget slide 11 ===== -->
## Reproducible workflows

11


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/diagrams/neurodesk-ecosystem-architecture.png)

<!-- ===== sciget slide 12 ===== -->
## Portable to different infrastructure

12


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/diagrams/neurodesk-ecosystem-architecture.png)

<!-- ===== sciget slide 13 ===== -->
## (untitled slide 13)

13


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/diagrams/neurodesk-ecosystem-architecture.png)

![](./assets/graphics/sciget-bilby-trio-working.png)

<!-- ===== sciget slide 14 ===== -->
## (untitled slide 14)

14


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/diagrams/neurodesk-ecosystem-architecture.png)

<!-- ===== sciget slide 15 ===== -->
## (untitled slide 15)

15


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/diagrams/neurodesk-workflow-cycle-diagram.png)

<!-- ===== sciget slide 16 ===== -->
## Enable various collaboration models

Centralised  collaboration


Decentralised  collaboration


16


Dao et al., 2025


- Data privacy
- assurance

- Simplified data management

- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

> **EMF/WMF (manual convert):** `media/image75.emf`
> **EMF/WMF (manual convert):** `media/image75.emf`

<!-- ===== sciget slide 17 ===== -->
## Uptake in the community

more than 1000 monthly users from over 60 countries

more than 16 000 downloads

currently used in 3 university courses with more than 100 students (UQ, Wollongong and University of South Carolina)

used in workshops with more than 50 simultaneous users (e.g. SNIRP 24, VSS 24, MGH Boston 23, CMRR Minnesota 23, Technion Israel 23)


17


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/figures/sciget-global-uptake-heatmap.png)

<!-- ===== sciget slide 18 ===== -->
## Today’s roadmap

18


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

- 1

- 3

- 5

- 4

- 2

- What are the problems?

- What’s
- needed

- Discussion
- &
- Outlook

- Existing
- Solutions

- Proposed
- Architecture

![](./assets/logos/sciget-logo.png)

![](./assets/graphics/sciget-mascot-bilby-bicycle.png)

![](./assets/graphics/winding-road-graphic.png)

<!-- ===== sciget slide 19 ===== -->
## (untitled slide 19)

- COMMUNITY
- WORKSHOPS 2025

- NATIONAL IMAGING FACILITY

- 6 AUGUST
- ADELAIDE

Working partnerships


AI-ready data


- Experiment and study design

- Skills and expertise

- Harmonised instruments

- Engaged peak user communities

- Population catchment

- Non-imaging data

- Seamless digital infrastructure

- FAIR and CARE

- Impactful National Imaging Data Collections

- Data Collections and Partnerships Program

- Clinical-research-industry partnerships

- 100+ peak imaging equipment and specialised expertise

- Spanning Australia’s population and innovation precincts

“NIF is uniquely positioned to generate impactful national data collections that can be used to solve big questions in medical research”


![](./assets/logos/ncris-national-research-infrastructure-logo.png)

![](./assets/logos/nif-logo.svg)

![](./assets/figures/orientation-field-pattern.png)

![](./assets/icons/icon-person-verified-credential.png)

![](./assets/icons/icon-mri-scanner-2.png)

![](./assets/graphics/australia-outline-map.png)

![](./assets/logos/ais-logo.png)

> **EMF/WMF (manual convert):** `media/image82.emf`

<!-- ===== sciget slide 20 ===== -->
## (untitled slide 20)

20


          - A consistent data management environment that could support all NIF nodes
          - A technical roadmap that helps plan for the future
          - A support model for node partners, national-scale projects, data partners and users
          - A funding model that supports continuous improvement and expansion
          - An effective infrastructure governance model
          - $10M project + $2.2M in infrastructure

- Foundational Digital Research Infrastructure

- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/logos/ncris-national-research-infrastructure-logo.png)

![](./assets/logos/nif-logo.svg)

![](./assets/logos/ais-logo.png)

<!-- ===== sciget slide 21 ===== -->
## (untitled slide 21)

- COMMUNITY
- WORKSHOPS 2025

- NATIONAL IMAGING FACILITY

- 6 AUGUST
- ADELAIDE

$10M NIF Foundational Digital Research Infrastructure


Increasing Adoption:

- 13  ~18 Nodes
- 500  >1,000 users
Data Capture

- Unified instrument data uploader
- DICOM or proprietary
- University or Hospital
Data Management & National Support

- National self-service portal
- Data & Metadata Expansion

Automated & Interactive Analysis

- Software catalogues
- Cost Controls and Management
- Automated software testing
- Streamlined community contributions
Community of Practice & User Engagement

- Drive user requirements
- Drive community adoption
- Lead national training workshops

![](./assets/logos/ncris-national-research-infrastructure-logo.png)

![](./assets/logos/nif-logo.svg)

![](./assets/figures/orientation-field-pattern.png)

![](./assets/logos/ais-logo.png)

<!-- ===== sciget slide 22 ===== -->
## (untitled slide 22)

22


- What is the Australian Imaging Service?

Our mission is to increase research reproducibility and drive the adoption of innovative but trusted analysis techniques.

NCRIS invested national platform for collaborative imaging research.

Integration with imaging facilities and clinical sites

Secure, audited data management, access, and deidentification

Browser accessible viewing, annotation, & analysis

One-click reproducible pipeline library, curated collection and custom developed


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/icons/icon-electronic-health-record.png)

![](./assets/icons/icon-mri-scanner.png)

![](./assets/icons/icon-unlocked-padlock.png)

![](./assets/icons/icon-team-network.png)

![](./assets/icons/icon-finger-pressing-button.png)

![](./assets/logos/ncris-national-research-infrastructure-logo.png)

![](./assets/logos/nif-logo.svg)

![](./assets/logos/ais-logo.png)

![](./assets/screenshots/sciget-session-infrastructure-identifiers-theme.png)

![](./assets/screenshots/sciget-schedule-ais-talk-sullivan.png)

<!-- ===== sciget slide 23 ===== -->
## (untitled slide 23)

23


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/diagrams/ais-platform-architecture-overview.png)

![](./assets/logos/ncris-national-research-infrastructure-logo.png)

![](./assets/logos/nif-logo.svg)

![](./assets/logos/ais-logo.png)

<!-- ===== sciget slide 24 ===== -->
## From Neurodesk to Sciget

24


- Extract Core Framework

- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/diagrams/neurodesk-container-build-deploy-architecture.png)

![](./assets/graphics/sciget-mascot-bilby-2.png)

> **EMF/WMF (manual convert):** `media/image104.emf`

<!-- ===== sciget slide 25 ===== -->
## Communities

Neuroimaging Community


Preclinical Imaging

Community


…

Community


25


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/diagrams/sciget-community-build-deploy-architecture.png)

![](./assets/diagrams/container-build-deploy-diverse-environments.png)

![](./assets/diagrams/neurodesk-container-workflow-diagram.png)

![](./assets/icons/icon-brain-circuit-open-box.png)

![](./assets/logos/sciget-logo.png)

![](./assets/graphics/sciget-mascot-bilby.png)

> **EMF/WMF (manual convert):** `media/image110.emf`

<!-- ===== sciget slide 26 ===== -->
## User Interface to include new tools

26


🔗 neurodesk.org/neurocontainers-ui/


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/screenshots/screenshot-neurocontainers-builder-ui.png)

![](./assets/screenshots/screenshot-sciget-container-registration-form.png)

<!-- ===== sciget slide 27 ===== -->
## GitHub actions build the application containers

27


-- all automated


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/screenshots/screenshot-github-actions-workflow-runs.png)

![](./assets/diagrams/neurocontainers-architecture-stack.png)

![](./assets/screenshots/screenshot-container-release-progress-dashboard.png)

![](./assets/screenshots/sciget-dashboard-released-containers.png)

<!-- ===== sciget slide 28 ===== -->
## Cloud servers

28


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/screenshots/neurodesk-play-website.png)

![](./assets/icons/icon-cursor-pointer.png)

![](./assets/screenshots/neurodesk-play-jupyterhub-login.png)

![](./assets/icons/icon-cursor-pointer.png)

![](./assets/screenshots/screenshot-neurodesk-jupyterhub-server-options.png)

![](./assets/icons/icon-cursor-pointer.png)

![](./assets/screenshots/screenshot-neurodesk-jupyterlab-launcher.png)

![](./assets/logos/ardc-nectar-research-cloud-logo.png)

![](./assets/logos/egi-logo.png)

![](./assets/logos/jetstream2-logo.png)

> **EMF/WMF (manual convert):** `media/image120.emf`

<!-- ===== sciget slide 29 ===== -->
## Virtual Desktops

29


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/screenshots/neurodesk-virtual-desktop-screenshot.png)

![](./assets/logos/neurodesk-logo.png)

![](./assets/screenshots/sciget-virtual-desktop-file-browser-terminal.png)

> **EMF/WMF (manual convert):** `media/image120.emf`

<!-- ===== sciget slide 30 ===== -->
## Software distribution using CVMFS

CVMFS delivers and caches >500GB of software containers for on-demand access


30


https://neurodesk.org/developers/cvmfs/


Local SQUID proxy


HPC


Desktop


Laptop


Stratum 1: US


Stratum 1: EU


Stratum 1: AUS


Stratum 0: US


GeoIP


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/icons/icon-computing-tiers-laptop-desktop-server-cloud.png)

![](./assets/icons/server-tower-case.png)

![](./assets/logos/maxmind-logo.gif)

![](./assets/icons/icon-stratum-0-server.png)

![](./assets/icons/icon-server-web.png)

![](./assets/icons/icon-server-web.png)

![](./assets/icons/icon-server-web.png)

![](./assets/screenshots/screenshot-cvmfs-neurodesk-containers-listing.png)

![](./assets/diagrams/neurocontainers-architecture-stack.png)

![](./assets/logos/ardc-nectar-research-cloud-logo.png)

![](./assets/logos/egi-logo.png)

![](./assets/logos/jetstream2-logo.png)

![](./assets/logos/open-science-grid-logo.png)

<!-- ===== sciget slide 31 ===== -->
## ComputationalNotebooks

31


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/screenshots/screenshot-jupyter-notebook-brain-mri.png)

![](./assets/screenshots/screenshot-neurodesk-ipyniivue-visualization.png)

> **EMF/WMF (manual convert):** `media/image120.emf`

<!-- ===== sciget slide 32 ===== -->
## Enable various collaboration models

Centralised  collaboration


Decentralised  collaboration


32


Dao et al., 2025


- Data privacy
- assurance

- Simplified data management

- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

> **EMF/WMF (manual convert):** `media/image75.emf`
> **EMF/WMF (manual convert):** `media/image75.emf`

<!-- ===== sciget slide 33 ===== -->
## (untitled slide 33)

33


Masson-Trottier, et al., 2025


- FAIR

- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/diagrams/sciget-reproducible-workflow-architecture.jpeg)

![](./assets/logos/xnat-logo.png)

<!-- ===== sciget slide 34 ===== -->
## Today’s roadmap

34


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

- 1

- 3

- 5

- 4

- 2

- What are the problems?

- What’s
- needed

- Discussion
- &
- Outlook

- Existing
- Solutions

- Proposed
- Architecture

![](./assets/graphics/sciget-mascot-bilby-bicycle.png)

![](./assets/graphics/winding-road-graphic.png)

![](./assets/logos/sciget-logo.png)

<!-- ===== sciget slide 35 ===== -->
## XNAT Deployment Overview

35


- xnat.rcc.uq.edu.au

- ctp.rcc.uq.edu.au

- xnat

- postgres

- ctp

- shadow-xnat

- hub.rcc.uq.edu.au

- nfs

- rdm

- jupyterhub

- notebook

- Researchers/Collaborators

- Clinical Sites

- container svc

- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/logos/kubernetes-ingress-logo.png)

![](./assets/icons/kubernetes-service-icon.png)

![](./assets/icons/kubernetes-pod-icon.png)

![](./assets/logos/kubernetes-logo-2.png)

![](./assets/logos/kubernetes-ingress-logo.png)

![](./assets/icons/kubernetes-service-icon.png)

![](./assets/icons/kubernetes-pod-icon.png)

![](./assets/icons/kubernetes-namespace-icon.png)

![](./assets/icons/kubernetes-pod-icon.png)

![](./assets/icons/icon-mri-scanner.jpg)

![](./assets/icons/icon-person-female.png)

![](./assets/icons/icon-person-silhouette.png)

![](./assets/icons/icon-kubernetes-persistent-volume.png)

![](./assets/icons/icon-laptop-2.png)

![](./assets/icons/icon-server-tower.png)

![](./assets/icons/kubernetes-pod-icon.png)

![](./assets/icons/kubernetes-namespace-icon.png)

![](./assets/icons/kubernetes-namespace-icon.png)

![](./assets/logos/kubernetes-ingress-logo.png)

![](./assets/icons/kubernetes-service-icon.png)

![](./assets/icons/kubernetes-node-icon.png)

![](./assets/icons/kubernetes-node-icon.png)

![](./assets/icons/kubernetes-node-icon.png)

![](./assets/icons/icon-kubernetes-persistent-volume.png)

![](./assets/icons/kubernetes-node-icon.png)

![](./assets/icons/kubernetes-pod-icon.png)

![](./assets/icons/kubernetes-pod-icon.png)

![](./assets/icons/kubernetes-job-icon.png)

![](./assets/logos/rdm-research-data-manager-uq-logo.png)

![](./assets/logos/ais-logo.png)

![](./assets/logos/xnat-logo.png)

![](./assets/logos/neurodesk-logo-2.png)

![](./assets/logos/jupyter-logo.png)

![](./assets/logos/ardc-nectar-research-cloud-logo.png)

<!-- ===== sciget slide 36 ===== -->
## (untitled slide 36)

36


![](./assets/screenshots/screenshot-xnat-dashboard-projects.png)

<!-- ===== sciget slide 37 ===== -->
## (untitled slide 37)

37


![](./assets/screenshots/screenshot-xnat-mr-session-scans.png)

<!-- ===== sciget slide 38 ===== -->
## (untitled slide 38)

38


![](./assets/screenshots/screenshot-xnat-jupyter-notebook-launch.png)

<!-- ===== sciget slide 39 ===== -->
## (untitled slide 39)

39


![](./assets/screenshots/screenshot-jupyterlab-neurodesk-launcher.png)

<!-- ===== sciget slide 40 ===== -->
## (untitled slide 40)

40


![](./assets/screenshots/screenshot-neurodesk-terminal-module-loading.png)

<!-- ===== sciget slide 41 ===== -->
## (untitled slide 41)

41


![](./assets/screenshots/screenshot-fsleyes-nifti-file-browser.png)

<!-- ===== sciget slide 42 ===== -->
## (untitled slide 42)

42


![](./assets/screenshots/neurodesk-desktop-app-menu.png)

<!-- ===== sciget slide 43 ===== -->
## (untitled slide 43)

43


![](./assets/screenshots/screenshot-neurodesk-mri-viewer.png)

<!-- ===== sciget slide 44 ===== -->
## Today’s roadmap

44


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

- 1

- 3

- 5

- 4

- 2

- What are the problems?

- What’s
- needed

- Discussion
- &
- Outlook

- Existing
- Solutions

- Proposed
- Architecture

![](./assets/graphics/sciget-mascot-bilby-bicycle.png)

![](./assets/graphics/winding-road-graphic.png)

![](./assets/logos/sciget-logo.png)

<!-- ===== sciget slide 45 ===== -->
## (untitled slide 45)

45


Neuroimaging Community


- Research Infrastructure

Data Providers


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/graphics/jupyter-notebook-browser-illustration.png)

![](./assets/logos/neurodesk-logo-4.png)

![](./assets/logos/sciget-logo-2.png)

![](./assets/diagrams/cvmfs-stratum-replication-architecture.png)

![](./assets/diagrams/sciget-source-to-workflow-diagram.png)

![](./assets/logos/mne-python-logo.png)

![](./assets/logos/fieldtrip-logo.png)

![](./assets/logos/brainstorm-logo.png)

![](./assets/logos/nvivo-logo.png)

![](./assets/logos/afni-logo.png)

![](./assets/logos/brainlife-logo.png)

![](./assets/logos/fsl-logo.png)

![](./assets/logos/github-logo.png)

![](./assets/diagrams/mri-scanner-imaging-clinical-data-pipeline.jpeg)

![](./assets/logos/bids-brain-imaging-data-structure-logo.png)

![](./assets/logos/openneuro-logo.png)

![](./assets/diagrams/task-dependency-graph.png)

![](./assets/logos/aws-logo.png)

![](./assets/logos/ardc-nectar-research-cloud-logo.png)

![](./assets/logos/pawsey-logo.png)

![](./assets/graphics/hpc-data-centre-banner.jpeg)

![](./assets/logos/massive-logo-with-bsi-iso9001.png)

![](./assets/logos/sciget-logo.png)

![](./assets/logos/datalad-logo.png)

![](./assets/logos/nextcloud-logo.png)

![](./assets/logos/owncloud-logo.png)

![](./assets/logos/onedrive-logo.png)

![](./assets/logos/dropbox-logo.png)

![](./assets/logos/osf-logo.png)

> **EMF/WMF (manual convert):** `media/image110.emf`

<!-- ===== sciget slide 46 ===== -->
## (untitled slide 46)

46


- Other communities…

- General Science

- Neuroimaging

46


Data Providers


- Research Infrastructure

- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/logos/eessi-logo.png)

![](./assets/logos/clowder-logo.png)

![](./assets/logos/bioimage-archive-logo.jpeg)

![](./assets/logos/pitschi-cat-logo.png)

![](./assets/logos/empiar-logo.png)

![](./assets/logos/idr-logo.jpeg)

![](./assets/logos/neurodesk-logo-4.png)

![](./assets/diagrams/mri-scanner-imaging-clinical-data-pipeline.jpeg)

![](./assets/logos/bids-brain-imaging-data-structure-logo.png)

![](./assets/logos/openneuro-logo.png)

![](./assets/diagrams/neurodesk-container-build-deploy-architecture.png)

![](./assets/graphics/jupyter-notebook-browser-illustration.png)

![](./assets/logos/sciget-logo-2.png)

![](./assets/diagrams/cvmfs-stratum-replication-architecture.png)

![](./assets/diagrams/sciget-source-to-workflow-diagram.png)

![](./assets/logos/github-logo.png)

![](./assets/logos/datalad-logo.png)

![](./assets/logos/nextcloud-logo.png)

![](./assets/logos/owncloud-logo.png)

![](./assets/logos/onedrive-logo.png)

![](./assets/logos/dropbox-logo.png)

![](./assets/logos/osf-logo.png)

![](./assets/diagrams/task-dependency-graph.png)

![](./assets/logos/aws-logo.png)

![](./assets/logos/ardc-nectar-research-cloud-logo.png)

![](./assets/logos/pawsey-logo.png)

![](./assets/graphics/hpc-data-centre-banner.jpeg)

![](./assets/logos/massive-logo-with-bsi-iso9001.png)

![](./assets/graphics/sciget-mascot-bilby.png)

![](./assets/logos/open-science-grid-logo.png)

![](./assets/logos/egi-logo.png)

![](./assets/logos/jetstream2-logo.png)

![](./assets/logos/r-project-logo.png)

![](./assets/logos/rstudio-logo.png)

![](./assets/logos/julia-logo.png)

![](./assets/logos/python-logo.png)

![](./assets/logos/alphafold-logo.png)

![](./assets/logos/openfoam-logo.png)

![](./assets/logos/nextflow-logo.png)

<!-- ===== sciget slide 47 ===== -->
## Roadmap

47


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/logos/github-copilot-logo.jpeg)

![](./assets/logos/github-actions-logo.png)

![](./assets/logos/neurodesk-logo-2.png)

![](./assets/logos/ardc-logo.png)

![](./assets/logos/open-science-grid-logo.png)

![](./assets/logos/egi-logo.png)

![](./assets/logos/jetstream2-logo.png)

![](./assets/logos/ais-logo.png)

![](./assets/logos/jupyter-logo.png)

![](./assets/logos/oracle-cloud-infrastructure-logo.jpeg)

![](./assets/logos/cernvm-file-system-logo.png)

![](./assets/logos/gitops-logo.png)

![](./assets/logos/nif-logo.svg)

![](./assets/logos/kubernetes-logo.png)

![](./assets/logos/wellcome-logo.png)

![](./assets/logos/chan-zuckerberg-initiative-logo.jpeg)

![](./assets/logos/xnat-logo.png)

![](./assets/logos/doi-logo.png)

![](./assets/logos/siemens-healthineers-logo-2.png)

![](./assets/logos/aws-logo-2.png)

<!-- ===== sciget slide 48 ===== -->
## Thanks to the following people…

Neurodesk & Sciget team

Steffen Bollmann

Thuy Dao

Michèle Masson-Trottier

Joshua Scarsbrook

Moni Dörig

Akshit Beniwal

Kyle Mapue

AIS

Mark Endrei and team (UQ RCC)

Ryan Sullivan and team (USyd)


48


![](./assets/photos/neurodesk-team-group-photo.jpeg)

<!-- ===== sciget slide 49 ===== -->
## Support and acknowledgements

49


  - NIF co-investment (1M AUD)
  - ARDC platform grant 2020-2023 (650k AUD)
  - EOSS6 2024 – 2026 (600k AUD)
  - UQ Global Development funding (8K AUD)

Grant Funding


  - > 10 active contributors
  - hosting of CVMFS through Open Science Grid, EGI and JetStream2

Community


  - ARDC Nectar Cloud (since 2021)
  - AWS (since 2024)
  - EGI (since 2024)
  - Google Cloud (since 2023)
  - JetStream2 (since 2023)
  - Oracle Cloud (2021 – 2023)

Support from Cloud providers


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

![](./assets/logos/qcif-logo.png)

![](./assets/logos/open-science-grid-logo.png)

![](./assets/logos/egi-logo-2.png)

![](./assets/logos/ardc-logo.png)

![](./assets/logos/aws-logo-2.png)

![](./assets/logos/google-cloud-logo.png)

![](./assets/logos/oracle-cloud-infrastructure-logo.jpeg)

![](./assets/logos/nif-logo.svg)

![](./assets/logos/uq-logo.png)

![](./assets/logos/swinburne-university-logo.png)

![](./assets/logos/university-of-sydney-logo.png)

![](./assets/logos/wellcome-logo-2.png)

![](./assets/logos/chan-zuckerberg-initiative-logo.png)

![](./assets/logos/iawards-national-winner-technology-platform-badge.png)

<!-- ===== sciget slide 50 ===== -->
## Thank you!

50


- The problems

- Existing solutions

- What's needed

- Proposed architecture

- Discussion & outlook

- Communities?

- Data repositories and collections?

- Domains and Flavours?

- Infrastructure?

sciget.org

neurodesk.org


Neurodesk Nature Methodsdoi.org/10.1038/s41592-023-02145-x


![](./assets/icons/icon-group-people.png)

<!-- ===== sciget slide 51 ===== -->
## (untitled slide 51)

51


![](./assets/screenshots/screenshot-xnat-dashboard-projects.png)

<!-- ===== sciget slide 52 ===== -->
## (untitled slide 52)

52


![](./assets/screenshots/screenshot-xnat-mr-session-scans.png)

<!-- ===== sciget slide 53 ===== -->
## (untitled slide 53)

53


![](./assets/screenshots/screenshot-xnat-jupyter-notebook-launch.png)

<!-- ===== sciget slide 54 ===== -->
## (untitled slide 54)

54


![](./assets/screenshots/screenshot-jupyterlab-neurodesk-launcher.png)

<!-- ===== sciget slide 55 ===== -->
## (untitled slide 55)

55


![](./assets/screenshots/screenshot-neurodesk-terminal-module-loading.png)

<!-- ===== sciget slide 56 ===== -->
## (untitled slide 56)

56


![](./assets/screenshots/neurodesk-desktop-app-menu.png)

<!-- ===== sciget slide 57 ===== -->
## (untitled slide 57)

57


![](./assets/screenshots/screenshot-fsleyes-nifti-file-browser.png)

<!-- ===== sciget slide 58 ===== -->
## (untitled slide 58)

58


![](./assets/screenshots/screenshot-neurodesk-mri-viewer.png)
