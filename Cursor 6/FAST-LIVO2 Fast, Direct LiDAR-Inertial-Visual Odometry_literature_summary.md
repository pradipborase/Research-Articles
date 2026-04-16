# Article Title
FAST-LIVO2 Fast, Direct LiDAR-Inertial-Visual Odometry.pdf

# Source File
`Cursor 6/FAST-LIVO2 Fast, Direct LiDAR-Inertial-Visual Odometry.md`

# Novelties
- (e5) and (e6) depict the camera first-person view from indoor to outdoor, highlighting large illumination variation from sudden overexposure to normal (see our accompanying video on YouTube: youtu.be/aSAwVqR22mo).
  - Evidence Section: `Method/Discussion context`
- Abstract—This paper proposes FAST-LIVO2: a fast, direct LiDAR-inertial-visual odometry framework to achieve accurate and robust state estimation in Simultaneous Localization and Mapping (SLAM) tasks and provide great potential in real- time, onboard robotic applications.
  - Evidence Section: `Method/Discussion context`
- To enhance the efficiency, we use direct methods for both the visual and LiDAR fusion, where the LiDAR module registers raw points without extracting edge or plane features and the visual module minimizes direct photometric errors without extracting ORB or FAST corner features.
  - Evidence Section: `Method/Discussion context`

# Practical Implementation Disadvantages
- (a)-(c) showcase airborne mapping, (d) represents a retail street collected with a handheld device, and (e) demonstrates an experiment where a UAV carrying a LiDAR, camera and inertial sensor perform real-time state estimation (i.e., FAST-LIVO2), trajectory planning, and tracking control all on its onboard computer.
  - Evidence Section: `Method/Discussion context`
- In (d)-(e), blue lines represent the computed trajectory.
  - Evidence Section: `Method/Discussion context`
- We conduct extensive experiments on both benchmark and private datasets, demonstrating that our proposed system significantly outperforms other state-of-the-art odometry systems in terms of accuracy, robustness, and computation efficiency.
  - Evidence Section: `Method/Discussion context`

# Conclusion
This summary extracts only novelty and practical implementation disadvantages grounded in the source text.
