# Article Title
event_triggered_cascade_active_disturbance_rejection_control_for_quadrotor_trajectory_tracking.pdf

# Source File
`DIOB/event_triggered_cascade_active_disturbance_rejection_control_for_quadrotor_trajectory_tracking.md`

# Novelties
- The proposed method decouples the system into position and velocity subsystems, with dedicated extended state observers (ESOs) and controllers designed for each subsystem to achieve accurate estimation and compensation of system nonlinearities, coupling eﬀects, and external disturbances.
  - Evidence Section: `Method/Discussion context`
- Additionally, an online self-tuning method based on particle swarm optimization (PSO) is introduced to enhance controller adaptability.
  - Evidence Section: `Method/Discussion context`
- Simulation results validate the robustness and eﬃciency of the proposed approach.
  - Evidence Section: `Method/Discussion context`

# Practical Implementation Disadvantages
- To further optimize computational resource utilization, a hybrid event-triggering mechanism incorporating both static and dynamic thresholds is developed.
  - Evidence Section: `Method/Discussion context`
- This mechanism updates system states and con- trol commands only at triggering instants, signiﬁcantly reducing computational overhead.
  - Evidence Section: `Method/Discussion context`
- As a vertical take-oﬀand landing (VTOL) platform capable of stationary hovering and agile maneu- vering, quadrotor systems exhibit superior environmental adaptability compared to ﬁxed-wing UAVs, enabling the execution of complex missions within conﬁned and challenging airspace.
  - Evidence Section: `Method/Discussion context`

# Conclusion
This summary extracts only novelty and practical implementation disadvantages grounded in the source text.
