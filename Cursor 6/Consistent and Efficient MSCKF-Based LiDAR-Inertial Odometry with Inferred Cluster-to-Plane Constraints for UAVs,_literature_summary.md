# Article Title
Consistent and Efficient MSCKF-Based LiDAR-Inertial Odometry with Inferred Cluster-to-Plane Constraints for UAVs,.pdf

# Source File
`Cursor 6/Consistent and Efficient MSCKF-Based LiDAR-Inertial Odometry with Inferred Cluster-to-Plane Constraints for UAVs,.md`

# Novelties
- To address these issues, this paper proposes a consistent and efficient tightly-coupled LIO framework tailored for UAVs.
  - Evidence Section: `Method/Discussion context`
- Within the efficient Multi-State Constraint Kalman Filter (MSCKF) framework, we build coplanar constraints inferred from planar features observed across a sliding window.
  - Evidence Section: `Method/Discussion context`
- By applying null- space projection to sliding-window coplanar constraints, we eliminate the direct dependency on feature parameters in the state vector, thereby mitigating overconfidence and improving consistency.
  - Evidence Section: `Method/Discussion context`

# Practical Implementation Disadvantages
- However, most state-of-the-art (SOTA) LiDAR-Inertial Odometry (LIO) systems still suffer from estimation inconsistency and computa- tional bottlenecks when deployed on such platforms.
  - Evidence Section: `Method/Discussion context`
- It exhibits improved robustness in degenerate scenarios, achieves the lowest memory usage via its map-free nature, and runs in real-time on resource- constrained embedded platforms (e.g., NVIDIA Jetson TX2).
  - Evidence Section: `Method/Discussion context`
- While LiDAR provides precise ranging, deploying LiDAR-Inertial Odometry (LIO) on UAVs is challenged by stringent Size, Weight, and Power (SWaP) constraints.
  - Evidence Section: `Method/Discussion context`

# Conclusion
This summary extracts only novelty and practical implementation disadvantages grounded in the source text.
