# System-level attack taxonomy for Deep Learning in Autonomous Vehicles

> A compact, taxonomy-first README for researchers. This repository contains a taxonomy-style index of system-level attacks on DL components in Autonomous Vehicles (papers published 2017-01-01 → 2024-01-01). The taxonomy and mappings below are derived from the uploaded paper used to build this repo.

---

## Quick start

- **What this repo is:** a lightweight, curated taxonomy and index (titles + links) of the 21 papers the authors selected for system-level attacks on DL in AVs. Unlike a bibliography, this README prioritizes *taxonomy-based discovery* (categories, leaves, and links to papers) so researchers can quickly find papers by attack properties.
- **Where the content comes from:** the taxonomy and mappings were extracted from the uploaded paper (Tehrani et al., *A Taxonomy of System-Level Attacks on Deep Learning Models in Autonomous Vehicles*). See the original paper for full details and full references. 

- **Files included in this document:**
  - `README.md` (this content, taxonomy + ASCII tree + full mapping preview)
  - `data/papers_full.csv` (full taxonomy mapping — exact headers preserved from the paper's Appendix Tables 3–5)
  - `data/summary_full.json` (machine-friendly JSON summary mirroring the full CSV)

---

## Scope & inclusion criteria (short)

- **Time window:** studies published between **2017-01-01** and **2024-01-01**.
- **What we include:** papers that *execute an attack in an AV context and report a system-level failure or observable system-level effect* (e.g., crash, lane-departure, freeze, wrong decision). This intentionally excludes papers that only report model-level mispredictions without any system-level evaluation.

- **What we exclude (and why):**
  - Sensor *physical removal/physical tampering* papers that only remove sensors or physically damage hardware without targeting DL model inputs are outside our focus when they do not produce DL-based model mispredictions leading to system-level failures. 
  - Network-only attacks (purely communication-layer exploits) were excluded because the taxonomy focuses on attacks that manipulate the *DL components or their inputs/outputs* and track how those model-level changes propagate to system-level failures. 

(These inclusion/exclusion rules are those used to reduce the initial corpus to 21 papers in the source paper.)

---

## What is a "system-level attack"?

A **system-level attack** is an adversarial action that (1) causes a DL component in an autonomous vehicle to produce a model-level error (e.g., misdetection, wrong steering-angle prediction, misclassification) and (2) — crucially — that model-level error **propagates** into a measurable failure at the vehicle/system level (e.g., lane departure, collision, emergency braking, freezing).

This emphasizes the *end-to-end chain* from environment/digital manipulation → **model misprediction** → **system-level consequence**. The taxonomy classifies attacks based on where and how the chain is built (attacked target, attacker capability, model under attack, application, system-level result, etc.).

---

## Full taxonomy tree (textual)

Below is the **full taxonomy tree (textual)** that mirrors the paper's taxonomy (12 top-level categories and subcategories). Each leaf lists the reference numbers of the papers from the original paper; those reference numbers map to the **Papers** section below.

```
System-level attack taxonomy
├─ Application Domain
│  ├─ Cars -> [1,3,4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
│  └─ Drones -> [2,4,6]
│
├─ DL Model Under Attack
│  ├─ Object Detection & Tracking -> [1,3,4,6,7,8,9,13,14,15,16,19,20]
│  ├─ Steering Wheel Angle Prediction -> [5,17,21]
│  ├─ Road Line Detection / Lane Detection -> [12,14,18]
│  └─ End-to-end (E2E) / Driving Agents -> [2,5,11,12,17,18,21]
│
├─ System Under Attack
│  ├─ Simulation (SSF / MSF / other simulators) -> [2,4,5,10,11,12,17,18,21]
│  ├─ Real AVs (Tesla, etc.) -> [1,3,7,8,9,13,15,16,20]
│  └─ Multi-Sensor Fusion (MSF) vs Single-Sensor Fusion (SSF) distinctions -> MSF papers: [1,3,7,8,13,15,16,20]; SSF papers: [2,4,5,6,11,12,17,18,21]
│
├─ Attack Scenario
│  ├─ Following / Vehicle-to-vehicle scenarios -> [3,5]
│  ├─ Intersection scenarios -> [1,12]
│  ├─ Waypoint / Destination tracking (drones) -> [2,6]
│  └─ Generic driving scenarios (simulation experiments) -> [4,7,8,9,10,11,13,14,15,16,17,18,19,20,21]
│
├─ Attacked Target
│  ├─ Input image -> [1,4,6,11,16]
│  ├─ Road / Roadside (paint, billboards, projections) -> [12,13,14,15,17,18,19]
│  ├─ Sensors (camera/LiDAR/laser interference) -> [9,20]
│  └─ Training data / Backdoor (Trojan) -> [10,21]
│
├─ Attacker's Capability (examples)
│  ├─ Attach stickers / patches / projections -> [3,5,6,12,14,15,18,19]
│  ├─ Install malware / manipulate training -> [4,10,21]
│  └─ Laser / sensor spoofing -> [9,20]
│
├─ Attack Strategy (Attack Type)
│  ├─ Evasion -> [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20]
│  └─ Poisoning (Backdoor/Trojan) -> [10,21]
│
├─ Attacker's System/Model Knowledge
│  ├─ White-box (WM) -> many papers list WM or mixed knowledge (see CSV for per-paper detail)
│  ├─ Black-box (BS) -> [11,14,17,19]
│  └─ Gray-box (GS) -> [2,8,...] (see CSV for exact labels)
│
├─ Attack/Error Specificity
│  ├─ Generic Attack / Generic Error (AG / EG) -> [1,4,5,15,19]
│  └─ Specific Attack / Specific Error (AS / ES) -> [2,3,6,7,8,9,10,11,12,13,14,16,17,18,20,21]
│
├─ Failure Specificity
│  ├─ Generic (aims to cause any failure) -> [1,4,5,15,19]
│  └─ Specific (aims at a targeted system-level failure) -> [2,3,6,7,8,9,10,11,12,13,14,16,17,18,20,21]
│
├─ Model-level Results
│  ├─ Misdetection / Missing detection -> [1,3,4,6,7,8,9,13,14,15,16,19,20]
│  └─ Misclassification / Wrong steering angle / Increased latency -> [2,5,10,11,12,17,18,21]
│
└─ System-level Results (Failure Propagation)
   ├─ Vehicle crash / collision -> [1,3,10,12,16]
   ├─ Losing the path / Lane departure -> [5,11,12,18,21]
   ├─ Freeze / Sudden braking / Emergency brake -> [2,4,5,6,11,12,14,15,17,19,20,21]
   └─ Sign ignorance / Wrong decision -> [9,10,19]
```

---

## Short taxonomy mapping (full mapping from the paper)

Below is the **full mapping** of all 21 papers across the taxonomy categories exactly as represented in the uploaded CSV (the paper's Appendix Tables 3–5). The CSV included in the repository is `data/papers_full.csv` and contains the exact headers from the paper's Appendix:

`Ref, App Domain, DL Model Under Attack, System Under attack, Attack Scenario, Attacked Target, Attacker's Capability, Attack Strategy, Attacker's System/Model knowledge, Attack/Error Specificity, Failure Specificity, Model-level results, System-level results (Failure Propagation)`

> For readability in the README we show a compact preview of the first 4 rows. The full `data/papers_full.csv` is included in the repo for programmatic use and contains all 21 rows.

| Ref | App Domain | DL Model Under Attack | System Under attack | Attack Scenario | Attacked Target | Attacker's Capability | Attack Strategy | Attacker's System/Model knowledge | Attack/Error Specificity | Failure Specificity | Model-level results | System-level results (Failure Propagation) |
|-----:|:-----------|:----------------------|:--------------------|:----------------|:----------------|:----------------------|:----------------|:----------------------------------:|:-----------------------:|:-------------------:|:-------------------:|:-----------------------------------------|
| [1] | Cars | SORT(Y5), FairMOT, ByteTrack, BoT-SORT (Perception) | Baidu Apollo in LGSVL simulator (MSF) | AVs changing lanes when another car is in the adjacent lane or approaching an intersection with a stop sign where another car is present | Input image | Purturbing the image input to insert fake bounding boxes into it | Evasion | WM / BS | AG / EG | Generic | Losing detection and subsequently tracking of the target object | Crashing into another car |
| [2] | Drones | A variation of DroNet (E2E) | Parrot Bebop 2 Drone and Matlab simulation (SSF) | Drones moving to its destination | Environment (anything that can hold a patch horizontally) | Attaching the patch to anything that can hold it horizontally, facing the drone. | Evasion | WM / GS | AG / ES | Specific | Misdetection of objects and Misprediction of the steering wheel angle | Crashing to objects, freezing or going off-route |
| [3] | Cars | OpenPilot's Adaptive Cruise Control ACC system (Perception) | CARLA and Baidu Apollo (MSF) | AV driving behind the attacker's vehicle | Vehicles and Trucks | Placing the patch on the back of a vehicle and drive it in front of the AV | Evasion | WM / BS | AS / ES | Specific | Misdetection of the vehicle in front | Acceleration and crash into the car in front |
| [4] | Cars, Drones | YOLO v5 (Perception) | Vision-based guidance system in CARLA or AirSim (SSF) | AVs following their target | Input image | Inserting the malware into the system and training the perturbations on the real training set | Evasion | WM / BS | AG / EG | Generic | Misdetection of the correct coordinates of the target bounding box | Losing path, stability and collision to surrounding obstacles |

---

## Papers (short-list — titles only, linked to the taxonomy mapping above)

Below we list the 21 papers included in the taxonomy. **Only the short title is listed here**; users should consult the original paper (or the paper’s ref list) for full bibliographic details and PDFs.

1. <a id="ref-1"></a>SlowTrack: Increasing the latency of camera-based perception in autonomous driving using adversarial examples (Ma et al., 2024)
2. <a id="ref-2"></a>RPAU: Fooling the eyes of UAVs via physical adversarial patches (Liu et al., 2024)
3. <a id="ref-3"></a>Adversarial attacks on adaptive cruise control systems (Guo et al., 2023)
4. <a id="ref-4"></a>Learning when to use adaptive adversarial image perturbations against autonomous vehicles (Yoon et al., 2023)
5. <a id="ref-5"></a>DeepManeuver: Adversarial test generation for trajectory manipulation of autonomous vehicles (von Stein et al., 2023)
6. <a id="ref-6"></a>Kidnapping deep learning-based multirotors using optimized flying adversarial patches (Hanfeld et al., 2023)
7. <a id="ref-7"></a>Does physical adversarial example really matter to autonomous driving? (Wang et al., 2023)
8. <a id="ref-8"></a>On data fabrication in collaborative vehicular perception: Attacks and countermeasures (Zhang et al., 2023)
9. <a id="ref-9"></a>Rolling colors: Adversarial laser exploits against traffic light recognition (Yan et al., 2022)
10. <a id="ref-10"></a>Stop-and-go: Exploring backdoor attacks on deep reinforcement learning-based traffic congestion control systems (Wang et al., 2021)
11. <a id="ref-11"></a>Attack and fault injection in self-driving agents on the CARLA simulator – experience report (Piazzesi et al., 2021)
12. <a id="ref-12"></a>Dirty road can attack: Security of deep learning based automated lane centering under Physical-World attack (Sato et al., 2021)
13. <a id="ref-13"></a>Invisible for both camera and LiDAR: Security of multi-sensor fusion based perception in autonomous driving (Cao et al., 2021)
14. <a id="ref-14"></a>Too good to be safe: Tricking lane detection in autonomous driving with crafted perturbations (Jing et al., 2021)
15. <a id="ref-15"></a>Robust roadside physical adversarial attack against deep learning in LiDAR perception modules (Yang et al., 2021)
16. <a id="ref-16"></a>ML-driven malware that targets AV safety (Jha et al., 2020)
17. <a id="ref-17"></a>Attacking vision-based perception in end-to-end autonomous driving models (Boloor et al., 2020)
18. <a id="ref-18"></a>Feasibility and suppression of adversarial patch attacks on end-to-end vehicle control (Pavlitskaya et al., 2020)
19. <a id="ref-19"></a>Phantom of the ADAS: split-second phantom attacks (Nassi et al., 2020)
20. <a id="ref-20"></a>Adversarial sensor attack on LiDAR-based perception (Cao et al., 2019)
21. <a id="ref-21"></a>Trojaning attack on neural networks (Liu et al., 2017)

---

## data/papers_full.csv (what's inside)

The `data/papers_full.csv` included in the repository contains the full appendix mapping for all 21 papers. The headers are exactly as used in the paper and preserved verbatim in the CSV. Use this file for programmatic filtering or to copy/paste into other tools.

---

## data/summary_full.json (what's inside)

The `data/summary_full.json` mirrors the CSV contents as an array of JSON objects (each object is one paper with all taxonomy fields). This file is useful for scripts or web UIs that want to load the taxonomy programmatically.

---

## Contributing

If you want to **add a paper** or **adjust a mapping**: please open a PR and add a row to `data/papers_full.csv` and update `data/summary_full.json`. Use the same fields and the `Ref` number should map to the number used in the original paper (or, if adding a new paper, add a new `Ref` number and include the source link).

Suggested paragraph for CONTRIBUTING.md (you can copy-paste):

> Thank you for contributing. This repository is a living taxonomy compiled from Tehrani et al.'s paper. Please add papers that match these criteria: (1) the attack demonstrates a DL-model-level misprediction and (2) the authors report a system-level effect or vehicle-level consequence. When possible, provide a stable link (DOI / arXiv / project page) and list which taxonomy categories apply. We will review PRs and merge after basic sanity checks.

---

## Notes & Next steps (suggestions)

- If you want external links to each paper (DOI/arXiv), add a `url` column to `data/papers_full.csv` and I can regenerate the README titles with direct links.
- I can also produce a `data/papers_view.md` that renders the full CSV as a readable Markdown table (if you prefer viewing in docs rather than downloading the CSV).

---

*Taxonomy and full mapping generated from the uploaded paper.*

<!-- End of document -->

