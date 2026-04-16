# Article Title
ABenchmarkComparisonofMonocularVisual-InertialOdometry AlgorithmsforFlyingRobots.pdf

# Source File
`Cluster 8/ABenchmarkComparisonofMonocularVisual-InertialOdometry AlgorithmsforFlyingRobots.md`

# Novelties
- In particular, we consider the following pipelines: • MSCKF - an extended Kalman Filter (EKF) orginally proposed in [1], but with many subsequent variations.
  - Evidence Section: `Method/Discussion context`
- • SVO [5]+MSF [6] - a loosely-coupled conﬁguration of a visual odometry pose estimator and an extended Kalman Filter for fusing the visual pose estimate with the inertial sensor data, as proposed in [7].
  - Evidence Section: `Method/Discussion context`
- While this could potentially be accomplished within a framework like SLAMBench [13] for dense RGB-D SLAM, currently no such framework for VIO algorithms exists.
  - Evidence Section: `Method/Discussion context`

# Practical Implementation Disadvantages
- However, due to the power and payload constraints of aerial platforms, state estimation algorithms must provide these qualities under the computational constraints of embedded hardware.
  - Evidence Section: `Method/Discussion context`
- It is not clear from existing results in the literature, however, which VIO algorithms perform well under the accuracy, latency, and computational constraints of a ﬂying robot with onboard state estimation.
  - Evidence Section: `Method/Discussion context`
- This paper evaluates an array of publicly-available VIO pipelines (MSCKF, OKVIS, ROVIO, VINS-Mono, SVO+MSF, and SVO+GTSAM) on different hardware conﬁgurations, including several single- board computer systems that are typically found on ﬂying robots.
  - Evidence Section: `Method/Discussion context`

# Conclusion
This summary extracts only novelty and practical implementation disadvantages grounded in the source text.
