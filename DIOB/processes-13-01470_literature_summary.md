# Article Title
processes-13-01470.pdf

# Source File
`DIOB/processes-13-01470.md`

# Novelties
- First, to suppress the influence caused by external disturbance torque, considering the fact that the angular velocity can be obtained by the inertial measurement unit (IMU), a reduced-order extended state observer (ESO) is applied as a feedforward compensation to improve the robustness of the tracking system.
  - Evidence Section: `Method/Discussion context`
- Then, an ESO-based nonlinear PID controller is constructed to track the desired attitude command, and the rigorous proof of the convergence of the closed-loop system is derived by utilizing the Lyapunov method.
  - Evidence Section: `Method/Discussion context`
- Finally, the effectiveness of the proposed method is illustrated by numerical simulations and platform experiments.
  - Evidence Section: `Method/Discussion context`

# Practical Implementation Disadvantages
- However, their practical deployment remains constrained by inherent challenges such as strong nonlinear dynamics, under- actuation, and high sensitivity to environmental disturbances like wind gusts, payload variations, and sensor noise.
  - Evidence Section: `Method/Discussion context`
- These limitations underscore the critical importance of robust and precise attitude control for achieving stable and reliable flight performance.
  - Evidence Section: `Method/Discussion context`
- In [8], by using error scaling in the integral operation, the nonlinear PID controller for attitude stabilization was developed.
  - Evidence Section: `Method/Discussion context`

# Conclusion
This summary extracts only novelty and practical implementation disadvantages grounded in the source text.
