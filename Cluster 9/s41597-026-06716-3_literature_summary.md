# Article Title
s41597-026-06716-3.pdf

# Source File
`Cluster 9/s41597-026-06716-3.md`

# Novelties
- The main contributions of this work are: • A comprehensive, open-access dataset of 240 fixed-wing missions, covering all flight phases (take-off, cruise, loiter, waypoint tracking, autonomous landing) with two avionics architectures.
  - Evidence Section: `Method/Discussion context`
- The aircraft is equipped with a DJI O3 digital FPV system to enhance the pilot’s situational awareness, as well as an Arducam USB camera with an 8 mm fixed lens in the Jetson configuration to enable onboard video capture and inference.
  - Evidence Section: `9 gram servo. The motor is driven by an electronic speed controller (ESC) that is linked to a PM02D power`
- Conversely, the Pixhawk 6X with Jetson Orin NX, when equipped with SSD storage, a camera, Wi-Fi and a power distribution unit, exceeds 1,700 €, reflecting its enhanced computational capabilities and suitability for on-board AI inference.
  - Evidence Section: `Method/Discussion context`

# Practical Implementation Disadvantages
- The dataset contains 240 fully annotated autonomous missions flown outdoors over repeatable, waypoint-based trajectories using two onboard architectures: a compact SpeedyBee F405 flight controller running INAV, and a Holybro Pixhawk 6X paired with a Jetson Orin NX companion computer running PX4.
  - Evidence Section: `Method/Discussion context`
- Each log provides synchronised multi-sensor telemetry (IMU, GNSS, barometric altitude, actuator states, flight modes, and power metrics) at high temporal resolution, enabling realistic modelling of flight dynamics, estimator behaviour, and sensor noise.
  - Evidence Section: `Method/Discussion context`
- The paper documents hardware integration, communication architecture, mission procedures, and the dataset file structure, and includes representative analyses to illustrate reuse for contested, safety-critical, and complex operational environments in field.
  - Evidence Section: `Method/Discussion context`

# Conclusion
This summary extracts only novelty and practical implementation disadvantages grounded in the source text.
