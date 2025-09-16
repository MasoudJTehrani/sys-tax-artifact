The root node branches into 12 top-level categories, each further subdivided into relevant subcategories. The leaf nodes of the tree contain lists of papers associated with their respective (sub)categories.

Each category and subcategory is detailed in the following.

1. **Application Domain:**  
   Domain or vehicle type that is the target of the attack, such as "Cars" and "Drones."
   
   If we compare the application domains covered by the papers included in the taxonomy with the possible AV types reported in the paper, we notice that most AV surfaces,
   including **sea, underwater, and space**, are uncovered. On the other hand, all these uncovered AV types represent **critical domains where security testing would be quite important**.
   We conclude that research is missing on the **system-level security** of AVs operating on surfaces other than land and air.

---

2. **DL Model Under Attack:**  
   The DL model under attack is the component responsible for system-level failures, such as **YOLOv5, ResNet-34, or DAVE-2**. This category has four subcategories:  

   - **Object Detection & Tracking:** DL models that handle object detection or tracking, e.g., YOLO.  
   - **Steering Wheel Angle Prediction:** Models that control the vehicle’s steering angle.  
   - **Road Line Detection:** Models that detect and follow road lines.  
   - **Traffic Control:** Models that assist in navigating complex traffic situations.  

---

3. **System Under Attack:**  
   The autonomous system under attack, such as a driving agent like **Baidu Apollo** in the **LGSVL simulator** or the driving agent in the **CARLA simulator**.  

   Subcategories:  
   - **Simulation:** The system is simulated.  
   - **Real AVs:** The system is a real-world autonomous vehicle.  

   Examples:  
   - Simulated: Baidu Apollo, CARLA's agent.  
   - Less popular simulators: BeamNG, Udacity.  
   - Real vehicle: Tesla.  

   Systems may use either **multi-sensor fusion (MSF)** or **single-sensor fusion (SSF)** for autonomous decision-making.  

   Comparison with other simulation environments reveals that **sea, underwater, and space simulators** are missing. This gap highlights the need for **research on system-level attacks** in these environments.

---

4. **Attack Scenario:**  
   The scenario in which an attack is designed to be effective, e.g., a car at an intersection or in a traffic jam. This category describes the **necessary conditions for an attack**:  

   - **Without Constraints:** No specific environmental or situational requirements.  
   - **With Constraints:** Specific conditions must be satisfied.  
     - **Roads:** Requires changes to the road itself.  
     - **Objects & Cars:** Requires placement of objects like billboards or other cars in precise locations.  
     - **Driving Condition:** Requires the AV to be in a specific situation (e.g., approaching a traffic light, at an intersection, or navigating a turn).  

---

5. **Attacked Target:**  
   The **specific element targeted** by the attack, which can include:  
   - **Input Image:** Directly altering images fed to the DL model.  
   - **Road or Roadside:** Changing road features.  
   - **Sensors:** Interfering with AV sensors.  
   - **Objects:** Billboards or traffic elements.  
   - **Signs:** E.g., stop signs.  
   - **Training Data:** Modifying data used to train the DL model.

---

6. **Attacker's Capability:**  
   The skills or access required to execute an attack. Subcategories:  
   - **Environmental Manipulation:** Changing the physical environment (placing objects on the road).  
   - **Software Interference:** Altering software or acting as a man-in-the-middle.  
   - **Sensor Interference:** Disrupting sensors (e.g., lasers).  
   - **Model Manipulation:** Modifying the DL model, e.g., adding backdoors to training data.

---

7. **Attack Type:**  
   The general approach of the attacker:  
   - **Poisoning:** Altering training data.  
   - **Evasion:** Causing mis-prediction during inference.

---

8. **Attacker's Knowledge:**  
   The attacker's access to the system or model, categorized by **white-box, black-box, or grey-box**:  
   - **Model-level White-Box:** Full access to model code and datasets.  
   - **Model-level Black-Box:** Access only to inputs and outputs.  
   - **System-level White-Box:** Unrestricted access to the system, including code, hardware, DL models, simulator, and datasets.  
   - **System-level Black-Box:** Limited to input (sensor) and output (actuator) data.  
   - **System-level Grey-Box:** Partial insights, not full access.

---

9. **Attack/Error Specificity:**  
   Describes whether attacks or resulting errors are targeted or general:  
   - **Attack-Specific:** Targets one particular object or aspect.  
   - **Attack-Generic:** Can affect a wider range of targets.  
   - **Error-Specific:** Produces a specific misbehavior/output.  
   - **Error-Generic:** Produces any kind of misbehavior.

---

10. **System's Failure Specificity:**  
    Indicates if the attacker aims for a specific system-level failure:  
    - **Failure-Specific:** Specific outcome expected, e.g., sudden braking.  
    - **Failure-Generic:** General system failure, no specific target.

---

11. **Model-level Results:**  
    Outcomes at the DL model level:  
    - **Steering Angle Misprediction:** Incorrect steering prediction.  
    - **Object Misdetection:** Failure to detect objects.  
    - **Misclassification:** Wrong classification of objects, e.g., traffic lights.  
    - **Wrong Decision:** Incorrect decisions, e.g., in traffic scenarios.

---

12. **System-level Results:**  
    Outcomes at the system level, caused by model-level misbehavior:  
    - **Vehicle Crash To:** AV crashes into:  
      - **Vehicles:** Other cars (often non-autonomous).  
      - **Objects:** Road curbs, billboards, cones, etc.  
      - **Pedestrians**  
    - **Losing the Path:** AV goes off-path or into another lane.  
    - **Changing in Speed/Brake:** AV accelerates, decelerates, or brakes suddenly.  
    - **Sign Ignorance:** AV ignores traffic lights or stop signs.
