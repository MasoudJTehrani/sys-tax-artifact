# System-level attack taxonomy for Deep Learning in Autonomous Vehicles

> A compact, taxonomy-first README for researchers. This repository contains a taxonomy-style index of system-level attacks on DL components in Autonomous Vehicles (papers published 2017-01-01 → 2024-01-01). The taxonomy and mappings below are derived from the paper: A Taxonomy of System-Level Attacks on Deep Learning Models in Autonomous Vehicles, used to build this repo.

---

## Quick start

- **What this repo is:** a lightweight, curated taxonomy and index (titles + links) of the 21 papers the authors selected for system-level attacks on DL in AVs. Unlike a bibliography, this README prioritizes *taxonomy-based discovery* (categories, leaves, and links to papers) so researchers can quickly find papers by attack properties.
- **Where the content comes from:** the taxonomy and mappings were extracted from the paper (Tehrani et al., *A Taxonomy of System-Level Attacks on Deep Learning Models in Autonomous Vehicles*). See the original paper for full details and full references. 

- **Files included in this document:**
  - `README.md` (this content, taxonomy + ASCII tree + full mapping preview)
  - `data/papers_full.csv` (full taxonomy mapping — exact headers preserved from the paper's Appendix Tables 3–5)
  - `data/summary_full.json` (machine-friendly JSON summary mirroring the full CSV)
  - `papers_full_view.md` a readable Markdown version of the full taxonomy mapping.
---

## Scope & inclusion criteria (short)

- **Time window:** studies published between **2017-01-01** and **2024-01-01**.
- **What we include:** papers that *execute an attack on DL components in an AV context and report a system-level failure or observable system-level effect* (e.g., crash, lane-departure, freeze, wrong decision). This intentionally excludes papers that only report model-level mispredictions without any system-level evaluation.

- **What we exclude (and why):**
  - Sensor *physical removal/physical tampering* papers that only remove sensors or physically damage hardware without targeting DL model inputs are outside our focus when they do not produce DL-based model mispredictions leading to system-level failures. 
  - Network-only attacks (purely communication-layer exploits) were excluded because the taxonomy focuses on attacks that manipulate the *DL components or their inputs/outputs* and track how those model-level changes propagate to system-level failures. 

---

## What is a "system-level attack"?

A **system-level attack** is an adversarial action that (1) causes a DL component in an autonomous vehicle to produce a model-level error (e.g., misdetection, wrong steering-angle prediction, misclassification) and (2) — crucially — that model-level error **propagates** into a measurable failure at the vehicle/system level (e.g., lane departure, collision, emergency braking, freezing).

This emphasizes the *end-to-end chain* from environment/digital manipulation → **model misprediction** → **system-level consequence**. The taxonomy classifies attacks based on where and how the chain is built (attacked target, attacker capability, model under attack, application, system-level result, etc.).

---

## Taxonomy mapping

| Ref | Title | App Domain | DL Model Under Attack | System Under attack | Attack Scenario | Attacked Target | Attacker's Capability | Attack Strategy | Attacker's System/Model knowledge | Attack/Error Specificity | Failure Specificity | Model-level results | System-level results (Failure Propagation) |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| [1] | SlowTrack: Increasing the latency of camera-based perception in autonomous driving using adversarial examples | Cars | SORT(Y5), FairMOT, ByteTrack, BoT-SORT(Perception) | Baidu Apollo in LGSVL simulator (MSF) | AVs changing lanes when another car is in the adjacent lane or approaching an intersection with a stop sign where another car is present | Input image | Purturbing the image input to insert fake bounding boxes into it | Evasion | WM / BS | AG / EG | Generic | Losing detection and subsequently tracking of the target object | Crashing into another car |
| [2] | RPAU: Fooling the eyes of UAVs via physical adversarial patches | Drones | A variation of DroNet (E2E) | Parrot Bebop 2 Drone and Matlab simulation (SSF) | Drones moving to its destination | Environment (anything that can hold a patch horizontally) | 'Attaching the patch to anything that can hold it horizontally, facing the drone.' | Evasion | WM / GS | AG / ES | Specific | Misdetection of objects and Misprediction of the steering wheel angle | Crashing to objects, freezing or going off-route |
| [3] | Adversarial attacks on adaptive cruise control systems | Cars | OpenPilot's Adaptive CruiseControl ACC system (Perception) | CARLA and Baidu Apollo (MSF) | AV driving behind the attacker's vehicle | Vehicles and Trucks | Placing the patch on the back of a vehicleand drive it in front of the AV | Evasion | WM / BS | AS / ES | Specific | Misprediction of range, speed, and time-to-collision | Emergency braking or the vehicle freezing |
| [4] | Learning when to use adaptive adversarial image perturbations against autonomous vehicles | Cars | YOLOv3, YOLOv5, and Mask R-CNN (Perception) | End-to-end AVs (E2E) | AV driving to its destination | Roadside advertisements and other objects | Placing a physical perturbation on roadside advertisements or other objects | Evasion | WM / BS | AS / ES | Specific | Misdetection of vehicles and other traffic objects | Crashing to objects or the vehicle freezing |
| [5] | DeepManeuver: Adversarial test generation for trajectory manipulation of autonomous vehicles | Cars | DeepManeuver and LGSVL simulator (E2E) | A self-driving car in LGSVL simulator (SSF) | AVs driving to its destination | A self-driving car | Applying an adversarial perturbation to the driving trajectory of the vehicle | Evasion | WM / BS | AG / ES | Specific | Prediction of a manipulated trajectory | Manipulating the AV's trajectory to make it get into a crash with other vehicles or leave its lane unexpectedly |
| [6] | Kidnapping deep learning-based multirotors using optimized flying adversarial patches | Drones | A custom neural network (E2E) | A deep learning-based multirotor | Drones moving to its destination | Environment (anything that can hold a patch horizontally) | 'Applying optimized patches to billboards or a drone' | Evasion | WM / BS | AG / ES | Specific | Misprediction of the steering wheel angle | Crashing into objects, freezing, or going off-route |
| [7] | Does physical adversarial example really matter to autonomous driving? | Cars | Various DNN models (Perception) | Various AV systems | AV driving to its destination | The environment (anywhere with a smooth surface) | 'Attaching adversarial patches to physical objects or the road' | Evasion | BM / BS | AG / ES | Specific | Misclassification of traffic signs and objects | The vehicle going to the wrong lane or freezing |
| [8] | On data fabrication in collaborative vehicular perception: Attacks and countermeasures | Cars | Collaborative vehicular perception (Perception) | CARLA (MSF) | AVs driving | V2X (Vehicle-to-everything) communication | Injecting false data points into the V2X communication channel | Evasion | WM / BS | AG / ES | Generic | Detecting nonexistent objects and obstacles | Crashing to objects or freezing or emergency braking |
| [9] | Rolling colors: Adversarial laser exploits against traffic light recognition | Cars | YOLOv5, RetinaNet and others (Perception) | Tesla's Autopilot and Baidu Apollo (MSF) | AVs driving | Traffic lights | Shooting a low-powered laser on the traffic lights to change their colors | Evasion | WM / BS | AG / ES | Specific | Misclassification of traffic lights | The vehicle passing red lights or freezing at green lights |
| [10] | Stop-and-go: Exploring backdoor attacks on deep reinforcement learning-based traffic congestion control systems | Traffic | Traffic congestion control systems (Reinforcement learning) | CARLA (MSF) | AVs on the road | The traffic congestion control system of a smart city | Retraining the model with a Trojan attack where a pre-defined pattern triggers a backdoor. | Poisoning | WM / BS | AS / ES | Specific | The model's output being manipulated | Manipulating the traffic flow of a smart city |
| [11] | Attack and fault injection in self-driving agents on the CARLA simulator – experience report | Cars | Deep Learning models and agents (E2E) | AV agents in the CARLA simulator (SSF) | AVs driving to its destination | The CARLA simulator's files | Modifying a specific file in the simulator to inject a fault | Fault injection | WM / BS | AS / ES | Specific | Injecting errors into the agents' data | The vehicle going to the wrong lane or crashing to objects |
| [12] | Dirty road can attack: Security of deep learning based automated lane centering under Physical-World attack | Cars | Lane centering modules (Perception) | AVs with lane centering modules (SSF) | AVs driving to its destination | The road | Drawing on the road to affect the lane detection | Evasion | WM / BS | AG / ES | Specific | Misdetection of lanes and other objects | The vehicle going to the wrong lane or freezing |
| [13] | Invisible for both camera and LiDAR: Security of multi-sensor fusion based perception in autonomous driving | Cars | Multi-sensor fusion (Perception) | Driving agents with camera and LiDAR (MSF) | AVs driving to its destination | The environment | Placing adversarial patches or posters in the AV's path | Evasion | WM / BS | AG / ES | Specific | Misclassification of objects in both camera and LiDAR | The vehicle freezing or not reacting to obstacles or crashing |
| [14] | Too good to be safe: Tricking lane detection in autonomous driving with crafted perturbations | Cars | Lane detection modules (Perception) | AVs with lane detection modules (E2E) | AVs driving | Road and surrounding | Drawing on the road to affect the lane detection | Evasion | WM / BS | AG / ES | Specific | Misdetection of lanes | The vehicle going to the wrong lane or freezing or crashing |
| [15] | Robust roadside physical adversarial attack against deep learning in LiDAR perception modules | Cars | LiDAR-based modules (Perception) | AVs with LiDAR sensors (SSF) | AVs driving | Road and surrounding | Drawing on the road to affect the lane detection | Evasion | BM / BS | AG / ES | Specific | Misdetection of objects | The vehicle going to the wrong lane or freezing or crashing |
| [16] | ML-driven malware that targets AV safety | Cars | NN models that control the AV safety | AV safety systems (Perception) | AVs driving | An infected USB stick connected to the car's system | Plugging an infected USB into the car's system to manipulate the AV safety controls | Malware | WM / BS | AS / ES | Specific | Manipulating the safety controls | The vehicle going to the wrong lane or freezing or crashing |
| [17] | Attacking vision-based perception in end-to-end autonomous driving models | Cars | End-to-end models (E2E) | End-to-end AVs (E2E) | AVs driving | Input image | Applying an adversarial perturbation to the image input | Evasion | WM / BS | AG / ES | Specific | Misprediction of the steering wheel angle | The vehicle going to the wrong lane or crashing to objects |
| [18] | Feasibility and suppression of adversarial patch attacks on end-to-end vehicle control | Cars | DriveNet (an extension of Dave2) (E2E) | Autonomous Driving agent in CARLA (SSF) | AVs driving past a roadside billboard | Billboard | Placing adversarial patches on billboards located on the right side of the roadside | Evasion | WM / BS | AS / EG | Specific | Misprediction of the steering wheel angle | Collision with the poster |
| [19] | Phantom of the ADAS: split-second phantom attacks | Cars | Faster_rcnn_inception_v2 and Tesla's (Perception) model | Tesla Model X HW 2.5/3 & Renault Captur (equipped with Mobileye 630) (MSF) | AVs driving | The environment (anywhere with a smooth surface) | 'Projecting a phantom using a projector or embedding the phantom on a digital advertising billboard' | Evasion | BM / BS | AG / EG | Generic | Detecting phantoms as real road signs or real-world objects | Acting according to the detected object (Brake or decelerate or follow a phantom lane into collision or into the upcoming lane and, etc...) |
| [20] | Adversarial sensor attack on LiDAR-based perception | Cars | DNN of the Lidar-based (Perception) module in Baidu Apollo | Driving agent in Baidu Apollo (MSF) | AVs driving | LIDAR Sensor | Injecting spoofed LiDAR data points by shooting lasers at the AV | Evasion | WM / BS | AG / ES | Specific | Detecting nonexistent obstacles | Emergency braking or the vehicle freezing |
| [21] | Trojaning attack on neural networks | Cars | NN model of Udacity Simulator (E2E) | Udacity Simulator (SSF) | AVs driving | Billboards | Retraining the model with Trojan data and attaching it to billboards. | Poisoning | WM / BS | AG / ES | Specific | Misprediction of the steering wheel angle | Collision with the poster |
---

## Papers

Below we list the 21 papers included in the taxonomy. These papers are sorted by publication year.

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
## Full taxonomy tree (image)

![Alt text](images/tree.png)

---

## Full taxonomy tree (textual)

Below is the **full taxonomy tree (textual)** that mirrors the paper's taxonomy (12 top-level categories and subcategories). Each leaf lists the reference numbers of the papers from the original paper; those reference numbers map to the **Papers** section above.

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

## data/papers_full.csv (what's inside)

The `data/papers_full.csv` included in the repository contains the full appendix mapping for all 21 papers. The headers are exactly as used in the paper and preserved verbatim in the CSV. Use this file for programmatic filtering or to copy/paste into other tools.

---

## data/summary_full.json (what's inside)

The `data/summary_full.json` mirrors the CSV contents as an array of JSON objects (each object is one paper with all taxonomy fields). This file is useful for scripts or web UIs that want to load the taxonomy programmatically.

---

## Contributing

If you want to **add a paper** or **adjust a mapping**: please open a PR and add a row to `data/papers_full.csv` and update `data/summary_full.json`. Use the same fields and the `Ref` number should map to the number used in the original paper (or, if adding a new paper, add a new `Ref` number and include the source link).


> Thank you for contributing. This repository is a living taxonomy compiled from Tehrani et al.'s paper. Please add papers that match these criteria: (1) the attack demonstrates a DL-model-level misprediction and (2) the authors report a system-level effect or vehicle-level consequence. When possible, provide a stable link (DOI / arXiv / project page) and list which taxonomy categories apply. We will review PRs and merge after basic sanity checks.

---

## Citation 
If you find this taxonomy useful, please consider giving it a star &#127775;, and cite the published paper:
[https://arxiv.org/abs/2503.09385](https://arxiv.org/abs/2412.04510)
```bibtex
@article{tehrani2024taxonomy,
  title={A Taxonomy of System-Level Attacks on Deep Learning Models in Autonomous Vehicles},
  author={Tehrani, Masoud Jamshidiyan and Kim, Jinhan and Foulefack, Rosmael Zidane Lekeufack and Marchetto, Alessandro and Tonella, Paolo},
  journal={arXiv preprint arXiv:2412.04510},
  year={2024}
}
```

## How to Replicate:
1. Install <a href="https://github.com/jonatasgrosman/findpapers">findpapers</a> by using ``pip install findpapers``.
2. Find our query from the **send_query.py**. Copy it and run it to find and extract the papers.
3. Change the ``json_dir_path = './findpapers'`` in the **venue_filter.py** to the direction of your outputed list of papers.
4. Run the **venue_filter.py** to filter venues based on the listed venues in **chosen_venues.txt** file.
5. You will have a **papers_after_venue_filter.csv** which contains the title, abstract, URLs, venue, and published date of the papers.

- Note: The **venue_freq.py** file outputs the number of papers extracted from each venue, separated by journals and conferences. You can skip running this code, as it was only intended for us to find related venues.


