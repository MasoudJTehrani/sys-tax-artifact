# System-level attack taxonomy for Deep Learning in Autonomous Vehicles

> A compact, taxonomy-first README for researchers. This repository contains a taxonomy-style index of system-level attacks on DL components in Autonomous Vehicles (papers published 2017-01-01 → 2024-01-01). The taxonomy and mappings below are derived from the uploaded paper used to build this repo.

---

## Quick start

- **What this repo is:** a lightweight, curated taxonomy and index (titles + links) of the 21 papers the authors selected for system-level attacks on DL in AVs. Unlike a bibliography, this README prioritizes *taxonomy-based discovery* (categories, leaves, and links to papers) so researchers can quickly find papers by attack properties.
- **Where the content comes from:** the taxonomy and mappings were extracted from the uploaded paper (Tehrani et al., *A Taxonomy of System-Level Attacks on Deep Learning Models in Autonomous Vehicles*). See the original paper for full details and full references.

- **Files included in this document:**
  - `README.md` (this content, taxonomy + ASCII tree + short mapping table)
  - `data/papers.csv` (machine-friendly CSV summary)
  - `data/summary.json` (machine-friendly JSON summary)

---

## Scope & inclusion criteria (short)

- **Time window:** studies published between **2017-01-01** and **2024-01-01**.
- **What we include:** papers that *execute an attack in an AV context and report a system-level failure or observable system-level effect* (e.g., crash, lane-departure, freeze, wrong decision). This intentionally excludes papers that only report model-level mispredictions without any system-level evaluation. See the paper for the exact filtering process and rationale.

- **What we exclude (and why):**
  - Sensor *physical removal/physical tampering* papers that only remove sensors or physically damage hardware without targeting DL model inputs are outside our focus when they do not produce DL-based model mispredictions leading to system-level failures.
  - Network-only attacks (purely communication-layer exploits) were excluded because the taxonomy focuses on attacks that manipulate the *DL components or their inputs/outputs* and track how those model-level changes propagate to system-level failures.

(These inclusion/exclusion rules are exactly the ones used to reduce the initial corpus to 21 papers in the source paper.)

---

## What is a "system-level attack"?

A **system-level attack** is an adversarial action that (1) causes a DL component in an autonomous vehicle to produce a model-level error (e.g., misdetection, wrong steering-angle prediction, misclassification) and (2) — crucially — that model-level error **propagates** into a measurable failure at the vehicle/system level (e.g., lane departure, collision, emergency braking, freezing).

This emphasizes the *end-to-end chain* from environmental or digital manipulation → **model misprediction** → **system-level consequence**. The taxonomy classifies attacks based on where and how the chain is built (attacked target, attacker capability, model under attack, application, system-level result, etc.).

---

## Why we focus on attacks that target DL parts (not e.g., pure camera destruction or network takeover)

Short answer: the taxonomy explicitly aims to study the *propagation* from model-level faults to system-level failures. Network-only or purely physical-destruction attacks (e.g., smashing a camera, cutting a wire) can of course disable a vehicle, but they do not help us understand how **subtle manipulations of DL inputs/weights/pipeline** cause the vehicle to behave incorrectly in a way that *depends on the model’s internals or outputs*.

Practically:
- The goal is to catalogue *system-level consequences that arise because a DL model misbehaved* (e.g., adversarial patch → misdetection → car steers into another lane). Sensor damage / network removal are outside this chain.
- Focusing on DL-oriented, model-linked attacks enables taxonomy categories such as: *Attacked Target (input image, roadside, training data, sensor spoofing), DL model under attack (object detection vs end-to-end vs steering-angle predictor), Attack Type (evasion vs poisoning), Attacker’s knowledge (white/black/gray) and System-level results (crash, freeze, sign-ignorance, etc.).*

If you want a separate index that *also* includes sensor-physical-damage or network-only attacks, we can add a supplemental folder (recommendation: `supplementary/other-threats.md`).

---

## ASCII taxonomy tree (textual) — leaves link to paper anchors below

(Leaf lists use the reference numbers from the original paper; each number below links to the short title entry in the **Papers** section.)

```
System-level attack taxonomy
├─ Application Domain
│  ├─ Cars -> [1,3,4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
│  └─ Drones -> [2,4,6]
├─ DL Model Under Attack
│  ├─ Object Detection & Tracking -> [1,3,4,6,7,8,9,13,14,15,16,19,20]
│  ├─ End-to-end (raw input → control) -> [2,5,11,12,17,18,21]
│  └─ Steering wheel / Angle prediction (prediction/planning) -> [13,17]
├─ Module Under Attack
│  ├─ Perception        -> [1,3,4,6,7,8,9,13,14,15,16,19,20]
│  ├─ End-to-end        -> [2,5,11,12,17,18,21]
│  └─ Planning/Control  -> [10]
├─ Attacked Target
│  ├─ Input image       -> [1,4,6,11,16]
│  ├─ Road / Roadside   -> [12,13,14,15,17,19]
│  ├─ Sensors (e.g. LiDAR camera interference) -> [9,20]
│  └─ Training data     -> [10]
├─ Attack Type
│  ├─ Evasion  -> [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20]
│  └─ Poisoning -> [10,21]
├─ Attacker's Knowledge
│  ├─ White-box -> [1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,18,20,21]
│  └─ Black-box -> [11,14,17,19]
└─ System-level Results
   ├─ Vehicle crash (to objects/vehicles/pedestrians) -> [1,3,10,12,16]
   ├─ Losing the path / Lane departure -> [5,11,12,18,21]
   ├─ Freeze / Sudden braking -> [2,4,5,6,11,12,14,15,17,19,21]
   └─ Wrong decision / Sign ignorance -> [9,10,19]
```

---

## Short taxonomy mapping (compact table)

> The table below is a compact, machine-friendly mapping of the 21 papers. It intentionally lists minimal fields: `Ref`, `Year`, `Title` (short), `AttackType`, `DLModule`, `AppDomain`, `AttackedTarget`, `SystemResult`.

> NOTE: the original paper includes full mapping tables in an Appendix (Tables 3–5). This compact table mirrors that mapping but shows only key fields so repo users can filter quickly.

| Ref | Year | Title (short) | AttackType | DLModule | AppDomain | AttackedTarget | SystemResult |
|-----:|:----:|:--------------|:-----------|:---------|:----------|:---------------|:-------------|
| 1 | 2024 | SlowTrack: Increasing the latency of camera-based perception | Evasion | Perception (Obj detect/track) | Cars | Input image | Crash (high success reported) |
| 2 | 2024 | RPAU: Fooling the eyes of UAVs via physical adversarial patches | Evasion | End-to-end (drone perception/control) | Drones | Objects/Signs / environment | Crash / freeze / veer off |
| 3 | 2023 | Adversarial attacks on adaptive cruise control systems | Evasion | Perception / ACC pipeline | Cars | Objects/Signs (lead vehicle patch) | Collision / wrong distance |
| 4 | 2023 | Learning when to use adaptive adversarial image perturbations | Evasion | Perception | Cars / Drones | Input image | Lose tracking / collision |
| 5 | 2023 | DeepManeuver: adversarial test generation for trajectory manipulation | Evasion | End-to-end / steering | Cars | Objects/Signs (billboard) | Off-road / collision |
| 6 | 2023 | Kidnapping multirotors using flying adversarial patches | Evasion | Perception / tracking | Drones | Input image / patch | Drone hijack / follow patch |
| 7 | 2023 | Does physical adv. example really matter to AVs? (SysAdv) | Evasion | Perception | Cars | Objects/Signs | Higher success — crashes |
| 8 | 2023 | On data fabrication in collaborative vehicular perception | Evasion | Perception (LiDAR collab) | Cars | Objects (shared features) | Object spoof/removal |
| 9 | 2022 | Rolling colors: laser exploits against traffic light recognition | Evasion | Perception (cam) | Cars | Sensors (camera) | Misclassification -> sign ignorance |
|10 | 2021 | Stop-and-go: backdoor attacks on DRL traffic control | Poisoning | Planning / DRL control | Cars | Training data | Wrong decision / collisions |
|11 | 2021 | Attack & fault injection in self-driving agents (CARLA) | Evasion | End-to-end / NN agents | Cars | Input image / NN weights | Collisions / lane departure |
|12 | 2021 | Dirty road can attack: lane centering under physical attack | Evasion | End-to-end / lane detection | Cars | Road / Roadside | Wrong steering / off-road |
|13 | 2021 | Invisible for camera & LiDAR: multi-sensor fusion attacks | Evasion | Perception (MSF) | Cars | Road / Roadside | Undetected object -> collision |
|14 | 2021 | Too good to be safe: tricking lane detection | Evasion | Perception / lane detection | Cars | Road / Roadside | Veer into wrong lane |
|15 | 2021 | Robust roadside physical adversarial attack (LiDAR) | Evasion | Perception (LiDAR) | Cars | Roadside | Change lane / stop |
|16 | 2020 | ML-driven malware that targets AV safety | Evasion | Perception / sensor fusion | Cars | Input image / feeds | Emergency braking / crash |
|17 | 2020 | Attacking vision-based perception in end-to-end driving | Evasion | End-to-end | Cars | Road / Roadside | Wrong steering / turn wrong way |
|18 | 2020 | Feasibility & suppression of adversarial patch attacks on E2E control | Evasion | End-to-end | Cars | Objects/Signs / billboard | Steering to patch / collision |
|19 | 2020 | Phantom of the ADAS: split-second phantom attacks | Evasion | Perception | Cars | Roadside / projection | Erroneous braking / wrong action |
|20 | 2019 | Adversarial sensor attack on LiDAR-based perception | Evasion | Perception (LiDAR) | Cars | Sensors (LiDAR) | Freeze / sudden brake |
|21 | 2017 | Trojaning attack on neural networks (backdoor) | Poisoning | End-to-end / NN model | Cars | Objects/Signs / billboard | Steering misprediction -> off-road |

> This compact table follows the exact mapping used in the paper's Appendix (Tables 3–5).

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

## data/papers.csv (CSV preview)

```csv
ref,year,title,attack_type,dl_module,app_domain,attacked_target,system_result
1,2024,SlowTrack: Increasing the latency of camera-based perception,Evasion,Perception,Cars,Input image,Crash
2,2024,RPAU: Fooling the eyes of UAVs via physical adversarial patches,Evasion,End-to-end,Drones,Objects/Signs,Crash/Freeze
3,2023,Adversarial attacks on adaptive cruise control systems,Evasion,Perception,Cars,Objects/Signs,Collision
4,2023,Learning when to use adaptive adversarial image perturbations,Evasion,Perception,Cars,Input image,Lose tracking/Crash
5,2023,DeepManeuver: Adversarial test generation,Evasion,End-to-end,Cars,Objects/Signs,Off-road/Collision
6,2023,Kidnapping multirotors using flying patches,Evasion,Perception,Drones,Input image,Drone hijack
7,2023,Does physical adv. example matter to AVs?,Evasion,Perception,Cars,Objects/Signs,Crash (improved success)
8,2023,On data fabrication in collaborative perception,Evasion,Perception,Cars,Objects/Signs,Spoof/Remove objects
9,2022,Rolling colors: laser exploits,Evasion,Perception,Cars,Sensors,Sign misclass/ignore
10,2021,Stop-and-go: backdoor attacks,Poisoning,Planning,Cars,Training data,Wrong decisions/Collision
11,2021,Attack & fault injection in CARLA,Evasion,End-to-end,Cars,Input image/weights,Collisions/Lane departure
12,2021,Dirty road can attack,Evasion,End-to-end,Cars,Road/Roadside,Wrong steering/Off-road
13,2021,Invisible for camera & LiDAR,Evasion,Perception,Cars,Road/Roadside,Undetected object -> collision
14,2021,Too good to be safe: tricking lane detection,Evasion,Perception,Cars,Road/Roadside,Veer into wrong lane
15,2021,Robust roadside physical adversarial attack,Evasion,Perception,Cars,Roadside,Change lane/stop
16,2020,ML-driven malware targeting AV safety,Evasion,Perception,Cars,Input feeds,Emergency braking/Crash
17,2020,Attacking vision-based perception in E2E models,Evasion,End-to-end,Cars,Road/Roadside,Wrong steering/Turn wrong way
18,2020,Feasibility & suppression of patch attacks,Evasion,End-to-end,Cars,Objects/Signs,Steer to patch/Collision
19,2020,Phantom of the ADAS:Episodes,Evasion,Perception,Cars,Roadside/Projection,Erroneous braking
20,2019,Adversarial sensor attack on LiDAR-based perception,Evasion,Perception,Cars,Sensors,Freeze/Sudden brake
21,2017,Trojaning attack on neural networks,Poisoning,End-to-end,Cars,Objects/Signs,Steering misprediction
```
```

---

## data/summary.json (preview)

```json
[
  {"ref":1, "year":2024, "title":"SlowTrack: Increasing the latency of camera-based perception", "attack_type":"Evasion", "dl_module":"Perception", "app_domain":"Cars"},
  {"ref":2, "year":2024, "title":"RPAU: Fooling the eyes of UAVs via physical adversarial patches", "attack_type":"Evasion", "dl_module":"End-to-end", "app_domain":"Drones"},
  {"ref":3, "year":2023, "title":"Adversarial attacks on adaptive cruise control systems", "attack_type":"Evasion", "dl_module":"Perception", "app_domain":"Cars"}
  /* ... remaining entries (4..21) mirror the CSV above */
]
```

> *Full `data/summary.json` and `data/papers.csv` are included in this repository (same folder). The preview above is intentionally compact.*

---

## Contributing

If you want to **add a paper** or **adjust a mapping**: please open a PR and add a row to `data/papers.csv` and update `data/summary.json`. Use the same fields and the `ref` number should map to the number used in the original paper (or, if adding a new paper, add a new `ref` number and include the source).

Suggested paragraph for CONTRIBUTING.md (you can copy-paste):

> Thank you for contributing. This repository is a living taxonomy compiled from Tehrani et al.'s paper. Please add papers that match these criteria: (1) attack demonstrates a DL-model-level misprediction and (2) the authors report a system-level effect or vehicle-level consequence. When possible, provide a stable link (DOI / arXiv / project page) and list which taxonomy categories apply. We will review PRs and merge after basic sanity checks.

---

## Notes & Next steps (suggestions)

- Add a small script `scripts/filter_by_category.py` that loads `data/papers.csv` and allows quick filters by `AttackType`, `DLModule`, or `SystemResult`.
- Add `supplementary/other-threats.md` if you want a separate index of sensor-only or network-only attacks.
- If you want badges (CI, license, zenodo, paper), I can propose a concise badges block — let me know which CI and license you plan to use.

---

*Taxonomy and compact mapping generated from the uploaded paper.*

<!-- End of document -->

