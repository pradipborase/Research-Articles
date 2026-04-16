# Article Title
Deep_Reinforcement_Learning_Multi-UAV_Trajectory_Control_for_Target_Tracking.pdf

# Source File
`Cluster 2 — AI and Machine Learning for UAV Control/Deep_Reinforcement_Learning_Multi-UAV_Trajectory_Control_for_Target_Tracking.md`

# Novelties
- 20, OCTOBER 15, 2021 15441 Deep Reinforcement Learning Multi-UAV Trajectory Control for Target Tracking Jiseon Moon , Member, IEEE, Savvas Papaioannou , Member, IEEE, Christos Laoudias , Member, IEEE, Panayiotis Kolios , and Sunwoo Kim , Senior Member, IEEE Abstract—In this article, we propose a novel deep rein- forcement learning (DRL...
  - Evidence Section: `Method/Discussion context`
- Subsequently, the proposed DRL-based controller selects the optimal joint control actions according to the Cramér–Rao lower bound (CRLB) of the joint measurement likelihood function to achieve high tracking performance.
  - Evidence Section: `Method/Discussion context`
- Speciﬁcally, the optimal UAV control actions are quantiﬁed by the proposed reward function, which considers both the CRLB of the entire system and each UAV’s individual contribution to the system, called global reward and difference reward, respectively.
  - Evidence Section: `Method/Discussion context`

# Practical Implementation Disadvantages
- This solution deals with complex environments, where the number of targets is unknown and varying.
  - Evidence Section: `Method/Discussion context`
- However, the table-based Q learning is difﬁcult to apply to large-scale problems with continuous state or action because of the memory capacity caused by a lot of states and actions.
  - Evidence Section: `Method/Discussion context`
- During the DRL training stage, the agent’s transition (sk, ak, rk, sk+1) is stored into a replay memory D.
  - Evidence Section: `Method/Discussion context`

# Conclusion
This summary extracts only novelty and practical implementation disadvantages grounded in the source text.
