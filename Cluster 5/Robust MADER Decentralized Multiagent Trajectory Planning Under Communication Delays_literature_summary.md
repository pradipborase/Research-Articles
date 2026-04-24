# Article Title
Robust MADER Decentralized Multiagent Trajectory Planning Under Communication Delays.pdf

# Source File
`Cluster 5/Robust MADER Decentralized Multiagent Trajectory Planning Under Communication Delays.md`

# Novelties
- Hardware Demonstration SCP [8] decNS [9] LSC [10] No No Yes decMPC [11] No Yes No decGroup [12] Yes/No2 No Yes ADPP [13] Yes3 No Yes MADER [4] Yes No No EGO- Swarm [5] Yes No Yes AsyncBVC [14] Yes Yes No RMADER (proposed) Yes Yes Yes 2decGroup triggers joint-optimization in dense environments and switches to a centralized, synchronous ...
  - Evidence Section: `Method/Discussion context`
- EGO-Swarm [5] also proposes a decentralized, asynchronous planner that requires agents to periodically broadcast a trajectory at a fixed frequency, and each agent immediately performs collision checks upon receiving the message.
  - Evidence Section: `Method/Discussion context`
- EGO-Swarm is the first fully decentralized, asynchronous trajectory planner success- fully demonstrating hardware experiments, yet it still suffers from a collision due to communication delays, as shown in Section III.
  - Evidence Section: `Method/Discussion context`

# Practical Implementation Disadvantages
- Decentralized planners are more scalable and robust to failures of the centralized machine.
  - Evidence Section: `Method/Discussion context`
- Asynchronous approaches do not require a synchronous mechanism among agents and therefore more scalable than synchronous approaches, but they are also more susceptible to communication delays since agents are planning and executing trajectories independently.
  - Evidence Section: `Method/Discussion context`
- However, the future tra- jectories are constrained by past separating planes, which can overconstrain the solution space and hence increase the conservatism.
  - Evidence Section: `Method/Discussion context`

# Conclusion
This summary extracts only novelty and practical implementation disadvantages grounded in the source text.
