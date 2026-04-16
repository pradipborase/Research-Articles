# Article Title
Frequency-Dependent H∞ Control for Wind Disturbance Rejection of a Fully Actuated UAV,.pdf

# Source File
`Cluster 1 — UAV Dynamics, Flight Mechanics, and Control/Frequency-Dependent H∞ Control for Wind Disturbance Rejection of a Fully Actuated UAV,.md`

# Novelties
- Bannwarth, Shahab Kazemi and Karl Stol Department of Mechanical and Mechatronics Engineering, University of Auckland, Auckland, New Zealand Corresponding author: Shahab Kazemi; Email: shahab.kazemi@auckland.ac.nz Received: 5 October 2023; Accepted: 25 March 2024 Keywords: Multirotor UAV; disturbance rejection; H∞control Abstract In thi...
  - Evidence Section: `Method/Discussion context`
- The proposed H∞controller solves the frequency-dependent actuator allocation problem by augmenting the dynamic model with weighting transfer functions.
  - Evidence Section: `Method/Discussion context`
- This novel frequency-dependent allocation utilizes the attitude-thrust for low-frequency disturbances and vectored-thrust for high-frequency disturbances, which exploits the maximum potential of the fully actuated UAV.
  - Evidence Section: `Method/Discussion context`

# Practical Implementation Disadvantages
- Vectored-thrust is high-bandwidth but saturation-constrained, while attitude-thrust generates larger forces with lower bandwidth.
  - Evidence Section: `Method/Discussion context`
- This recognition is critical, as vectored-thrust is more prone to actuator saturation and better suited for smaller amplitude, higher-frequency commands.
  - Evidence Section: `Method/Discussion context`
- In the trimming algorithm, position and rate states are constrained to zero.
  - Evidence Section: `Method/Discussion context`

# Conclusion
This summary extracts only novelty and practical implementation disadvantages grounded in the source text.
