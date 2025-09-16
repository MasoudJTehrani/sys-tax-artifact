```
System-level Attack Taxonomy
├─ Application Domain
│  ├─ Cars — [1, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
│  └─ Drones — [2, 4, 6]
├─ DL Model Under Attack
│  ├─ Object Detection & Tracking — [1, 3, 4, 6, 7, 8, 9, 13, 15, 16, 19, 20]
│  ├─ Steering Wheel Angle Prediction — [2, 5, 11, 12, 18, 21]
│  ├─ Road Line Detection — [13, 17]
│  └─ Traffic Control — [10]
├─ Module Under Attack
│  ├─ Perception — [1, 3, 4, 6, 7, 8, 9, 13, 14, 15, 16, 19, 20]
│  ├─ Planning — [10] 
│  └─ End-to-end — [2, 5, 11, 12, 17, 18, 21]
├─ System Under Attack
│  ├─ Simulation
│  │  ├─ SSF — [2, 4, 5, 10, 11, 12, 17, 18, 21]
│  │  └─ MSF — [1, 3, 7, 8, 9, 13, 15, 16, 20]
│  └─ Real AVs
│     ├─ SSF — [2, 6, 14]
│     └─ MSF — [19]
├─ Attack Scenario
│  ├─ Without Constraints — [2, 4, 6, 12, 19, 20, 21]
│  └─ With Constraints
│     ├─ Roads — [13, 14, 15]
│     ├─ Objects & Cars — [5, 10, 11, 16, 18]
│     └─ Driving Conditions — [1, 3, 7, 8, 9, 17]
├─ Attacked Target
│  ├─ Input image — [1, 4, 6, 11, 16]
│  ├─ Road / Roadside — [12, 13, 14, 15, 17, 19]
│  ├─ Sensors — [9, 20]
│  ├─ Objects / Signs — [2, 3, 5, 7, 8, 18, 19, 21]
│  └─ Train Data — [10]
├─ Attacker's Capability
│  ├─ Environmental Manipulation — [2, 3, 5, 6, 12, 13, 14, 15, 17, 18, 19]
│  ├─ Software Interference — [1, 4, 7, 8, 11, 16]
│  ├─ Sensor Interference — [9, 20]
│  └─ Model Manipulation — [10, 11, 21]
├─ Attack Type
│  ├─ Evasion — [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
│  └─ Poisoning — [10, 21]
├─ Attacker's System / Model Knowledge
│  ├─ Model-level Knowledge
│  │  ├─ White-Box — [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 18, 20, 21]
│  │  └─ Black-Box — [11, 14, 17, 19]
│  └─ System-level Knowledge
│     ├─ White-Box — [16]
│     ├─ Black-Box — [1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21]
│     └─ Gray-Box — [2, 8]
├─ Attack / Error Specificity
│  ├─ Attack
│  │  ├─ Specific — [5, 7, 8, 9, 10, 13, 16, 17, 18]
│  │  └─ Generic — [1, 2, 3, 4, 6, 11, 12, 14, 15, 19, 20, 21]
│  └─ Error
│     ├─ Specific — [2, 3, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 20, 21]
│     └─ Generic — [1, 4, 5, 11, 18, 19]
├─ System's Failure Specificity
│  ├─ Generic — [1, 4, 5, 15, 19]
│  └─ Specific — [2, 3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 20, 21]
├─ Model-Level Results
│  ├─ Steering Angle Misprediction — [2, 5, 11, 12, 18, 21]
│  ├─ Object Misdetection — [1, 2, 3, 4, 6, 7, 8, 11, 13, 14, 15, 16, 17, 19, 20]
│  ├─ Misclassification — [9]
│  └─ Wrong Decision — [10]
└─ System-Level Results
   ├─ Vehicle Crash to:
   │  ├─ Vehicles — [1, 3, 10, 12, 16]
   │  ├─ Objects — [2, 4, 5, 8, 11, 12, 13, 17, 18, 19]
   │  └─ Pedestrians — [7]
   ├─ Losing the path — [2, 4, 5, 6, 11, 12, 14, 15, 17, 19, 21]
   ├─ Changing in Speed/Brake — [2, 3, 8, 9, 15, 16, 19, 20]
   └─ Sign Ignorance — [7, 9]
```
