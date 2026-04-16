# Cooperative Path Planning for Autonomous UAV Swarms Using MASAC-CA Algorithm.pdf

## Page 1

Received: 9 October 2025
Revised: 2 November 2025
Accepted: 9 November 2025
Published: 14 November 2025
Citation:
Hu, W.; Zhang, M.; Xu, X.;
Qiu, S.; Liao, T.; Yue, L. Cooperative
Path Planning for Autonomous UAV
Swarms Using MASAC-CA
Algorithm. Symmetry 2025, 17, 1970.
https://doi.org/10.3390/
sym17111970
Copyright: © 2025 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license
(https://creativecommons.org/
licenses/by/4.0/).
Article
Cooperative Path Planning for Autonomous UAV Swarms Using
MASAC-CA Algorithm
Wenli Hu 1, Mingyuan Zhang 1,2, Xinhua Xu 1,2, Shaohua Qiu 1,2
, Tao Liao 1,2,*
and Longfei Yue 1,*
1
National Key Laboratory of Electromagnetic Energy Technology, Naval University of Engineering,
Wuhan 430033, China; m24381103@nue.edu.cn (W.H.)
2
East Lake Laboratory, Wuhan 430033, China
*
Correspondence: 1610061148@nue.edu.cn (T.L.); corresylf@163.com (L.Y.)
Abstract
Cooperative path planning for unmanned aerial vehicle (UAV) swarms has attracted con-
siderable research attention, yet it remains challenging in complex, uncertain environments.
To tackle this problem, we model the cooperative path planning task as a heterogeneous
decentralized Markov Decision Process (MDP), emphasizing the symmetry-inspired role
assignment between leader and wingmen UAVs, which ensures balanced and coordi-
nated behaviors in dynamic settings. We address the problem using a Multi-Agent Soft
Actor-Critic (MASAC) framework enhanced with a symmetry-aware reward mechanism
designed to optimize multiple cooperative objectives: simultaneous arrival, formation
topology preservation, dynamic obstacle avoidance, trajectory smoothness, and inter-agent
collision avoidance. This design promotes behavioral symmetry among agents, enhanc-
ing both coordination efficiency and system robustness. Simulation results demonstrate
that our method achieves efficient swarm coordination and reliable obstacle avoidance.
Quantitative evaluations show that our MASAC-CA algorithm achieves a Mission Success
Rate (MSR) of 99.0% with 2–5 wingmen, representing approximately 13% improvement
over baseline MASAC, while maintaining Formation Keeping Rates (FKR) of 59.68–26.29%
across different swarm sizes. The method also reduces collisions to near zero in cluttered
environments while keeping flight duration, path length, and energy consumption at
levels comparable to baseline algorithms. Finally, the proposed model’s robustness and
effectiveness are validated in complex uncertain environments, underscoring the value of
symmetry principles in multi-agent system design.
Keywords: UAV swarm; path planning; multi-agent reinforcement learning; soft actor-critic;
Markov Decision Process
1. Introduction
With the development of robotics, micro-electro-mechanical systems (MEMSs), and
artificial intelligence technologies, unmanned aerial vehicle (UAV) systems have been
extensively deployed in environmental monitoring, data collecting, service delivery, and
emergence communication. Significant limitations are observed in single-UAV systems
during target tracking, where evasive maneuvers tend to cause mission failure due to
target loss or UAV destruction. Multi-UAV cooperative path planning, utilizing distributed
decision-making and multi-objective optimization [1], can significantly enhance mission
robustness and operational efficiency. At its core lies the multi-UAV cooperative decision-
making and optimization process [2]. This process must integrate mission requirements,
Symmetry 2025, 17, 1970
https://doi.org/10.3390/sym17111970

## Page 2

Symmetry 2025, 17, 1970
2 of 24
inter-UAV collaborative relationships [3], and obstacle avoidance constraints to generate
flight trajectories that achieve spatiotemporal and task-level coordination.
To tackle the multi-UAV cooperative path planning problem, this study proposes the
MASAC-CA algorithm (Multi-Agent Soft Actor-Critic with Cooperative Arrival), built
upon the Multi-Agent Soft Actor-Critic (MASAC) [4,5] framework. The algorithm models
the path planning problem as a heterogeneous Markov Decision Process (MDP) [6]. This
heterogeneity introduces a purposeful asymmetry in agent roles and state representations,
which in turn enables the emergence of highly symmetric and coordinated collective be-
haviors, such as formation keeping and simultaneous arrival. Through task cooperativity
analysis and the design of refined reward functions, it achieves multi-objective coordi-
nation encompassing simultaneous arrival, formation topology preservation, dynamic
obstacle avoidance, trajectory smoothness, and inter-agent collision avoidance. The reward
mechanism is designed with a symmetry-aware principle, ensuring that the incentives for
coordination are balanced across different agents, promoting behavioral symmetry where
needed (e.g., velocity matching) while respecting their functional asymmetries (e.g., leader-
initiated coordination). By integrating core elements such as approach speed, flight time
coordination, and arrival timing, this design establishes a systematic guidance mechanism
for cooperative policy. The main contributions of this paper are as follows:
1.
We propose a hierarchically structured reward mechanism specifically designed for
precision simultaneous arrival missions. This architecture systematically integrates
sparse terminal rewards with dense intermediate incentives, incorporating a post-
arrival holding mechanism for the leader UAV to prevent formation disintegration.
The framework combines stagnation penalties, temporal efficiency incentives, and
collision avoidance penalties to achieve multi-objective cooperative optimization.
Notably, the integration of formation maintenance rewards and obstacle avoidance
penalties establishes a dual-layer collision prevention system, significantly enhancing
operational safety while preserving formation integrity throughout mission execution.
2.
We introduce a novel heterogeneous Markov Decision Process formulation that ad-
dresses Multi-UAV coordination challenges in simultaneous arrival scenarios [6]. The
framework employs distinct state representations: the leader UAV’s state space incor-
porates a mission completion flag, enabling real-time terminal condition awareness,
while wingmen states include the leader UAV’s positional coordinates [7]. This de-
sign establishes the leader’s arrival status and position as essential state information,
with the completion flag serving as a global coordination signal [8]. The architecture
ensures continuous positional tracking by wingmen throughout all mission phases,
including operation after the leader reaches the target, creating state-level coopera-
tive coupling that accurately models the leader–follower formation and eliminates
formation instability risks inherent in conventional homogeneous approaches.
3.
Our methodology rigorously implements the Centralized Training with Decentralized
Execution (CTDE) [9] paradigm to balance coordination efficiency with operational
autonomy. During training, we employ centralized integration of agent experiences
for joint policy optimization, preventing behavioral conflicts and suboptimal so-
lutions [10]. During execution, each agent operates independently using locally
observable states with decentralized policy networks, ensuring system robustness,
real-time responsiveness, and resilience to communication latency [11]. This approach
enables effective cooperative behavior while maintaining the operational indepen-
dence required for dynamic environments [12]. The overall framework is illustrated
in Figure 1.

## Page 3

Symmetry 2025, 17, 1970
3 of 24
B.Collaborative path planning for drone clusters 
based on MASAC algorithm and modeling as 
Markov decision process
A1
A2
A3
A4
< S,A,P,R,ϒ   >
C. Following the principle 
of "centralized training, 
distributed execution"
A.Design collaborative reward design to enable the leader and 
wingman to collaborate to reach the target location
D. Formation 
distance reward 
design to avoid 
collisions between 
aircraft
Π 
S
A
Q
Critic
Actor
Centralized Training
θk
Decentralized 
Execution
Πk 
   
Actor of UAV k
Wingman
Leader
Experience Replay Buffer
Destination
Satellite
Obstacle
Interference 
zone
NFZ
Figure 1. General idea diagram.
2. Related Work
In Section 2, we survey recent advances in path planning through two methodological
paradigms: traditional optimization methods and reinforcement learning methods.
2.1. Traditional Path Planning Methods
Current UAV path planning approaches exhibit a heavy reliance on precise mathemat-
ical models of the environment [13]. Algorithms such as Dijkstra determine optimal paths
through exhaustive node traversal, while A* enhances search efficiency via a heuristic eval-
uation function [14]. D*, conversely, facilitates dynamic path updates [15]. However, their
applicability in complex environments is severely hampered by the “curse of dimension-
ality”, resulting in prohibitive computational complexity or in-tractability [16]. Heuristic
techniques, including Particle Swarm Optimization (PSO) [17] and Ant Colony Optimiza-
tion (ACO) [18], effectively circumvent this dimensionality curse, offering advantages such
as rapid planning speed and robust global exploration capabilities [19]. Nevertheless,
their effectiveness is predominantly confined to static environment [20], rendering them
inadequate for dynamic scenarios characterized by unknown global states and stringent
real-time planning requirements [21].
2.2. Reinforcement Learning Methods
Deep Reinforcement Learning (DRL), which integrates perceptual capabilities with
decision-making, presents a transformative approach to dynamic path planning. By formu-
lating the problem as a sequential decision optimization task and adopting an “offline train-
ing, online inference” paradigm, DRL enables the learning of optimal agent policies and
facilitates real-time planning in complex dynamic environments, demonstrating notable
adaptability and transferability. Key single-agent DRL contributions include the Double
Deep Q-Network (DDQN) algorithm [22], augmented with Kalman filtering for efficient
UAV tracking of maneuvering targets; the MN-DDPG method [23], utilizing hybrid noise
to enhance exploration efficiency [24]; the Twin Delayed DDPG (TD3) algorithm [25], ad-
dressing challenges in continuous state and action spaces; the Imitation-enhanced Dueling
Double Deep Q-Network (ID3QN) algorithm [26], balancing exploration-exploitation via

## Page 4

Symmetry 2025, 17, 1970
4 of 24
an ε-imitation strategy; and the Soft Actor-Critic (SAC) algorithm [27], tackling underwater
robot localization and tracking. Critically, however, these single-agent DRL algorithms lack
the capacity for effective multi-UAV cooperative planning.
Extending to multi-agent systems, the decoupled Multi-Agent Deep Deterministic
Policy Gradient (MADDPG) framework [28] has been applied to UAV swarm autonomous
tracking and obstacle avoidance. This framework optimizes cooperative decision-making
under the CTDE principle, mitigating issues of suboptimality and centralization dominance.
Nevertheless, constrained by the inherent exploration limitations of its underlying DDPG
algorithm, MADDPG suffers from low sample learning efficiency.
Beyond MADDPG, other multi-agent reinforcement learning paradigms have attracted
considerable research interest. The Multi-Agent Proximal Policy Optimization (MAPPO) al-
gorithm [29], built on on-policy learning and a clipped objective function, exhibits excellent
training stability in cooperative multi-agent settings. However, its on-policy nature leads to
inherently lower sample efficiency, hindering its practical deployment in computationally
demanding UAV simulation tasks.
In contrast, value decomposition methods such as QMIX [30] have demonstrated
outstanding performance in discrete decision-making domains like StarCraft. By enforcing
a monotonicity constraint to aggregate individual Q-values into a global Q-value, these
methods achieve efficient decentralized execution and implicit credit assignment. However,
this structural constraint, while enforcing a form of functional symmetry in value decompo-
sition, limits the policy representational capacity, as it cannot model cooperative scenarios
requiring an agent to take a locally suboptimal action for greater global benefit—a form
of strategic asymmetry. Moreover, QMIX is fundamentally designed for discrete action
spaces, rendering it difficult to apply directly to UAV path planning problems that require
fine-grained continuous control.
To address these gaps, we introduce the MASAC-CA algorithm, founded on three
core technical contributions deeply rooted in the principles of symmetry and asymmetry
for effective coordination. First, it utilizes a heterogeneous MDP with role-aware states,
creating an asymmetric information structure (including the leader’s terminal flag) that
is essential for orchestrating symmetric outcomes like simultaneous arrival. This design
ensures that the asymmetric roles are leveraged to achieve symmetric spatiotemporal
coordination. Second, it leverages the MASAC framework to combine the sample efficiency
of off-policy learning with innate support for continuous control, facilitated by an improved
CTDE paradigm. The CTDE paradigm itself embodies a symmetric-asymmetric duality:
asymmetric information access during training versus symmetric execution capabilities
during deployment. Third, it employs a maximum entropy objective to boost exploration
beyond monotonicity limitations, encouraging a more symmetric exploration of the action
space for all agents. Together, these features enable robust multi-objective coordination
encompassing simultaneous arrival, formation keeping, and collision/obstacle avoidance,
proving particularly effective for cooperative UAV path planning in complex uncertain
environments by skillfully managing the interplay between symmetry and asymmetry.
3. Problem Formulation
3.1. Problem Statement for UAV Swarms Cooperative Path Planning
As illustrated in Figure 2, a swarm of N heterogeneous UAVs (using N = 3 as an
example) forms a formation characterized by one leader UAV and multiple wingman UAVs.
The swarm must dynamically maneuver around randomly distributed obstacles (including
jamming zones and No-Fly Zones (NFZs)) within the environment. They are required
to establish the formation mid-flight and ultimately reach a randomly designated goal
location. The UAVs utilize satellite data to pre-determine the approximate goal position.

## Page 5

Symmetry 2025, 17, 1970
5 of 24
During flight, they continuously sense the external environment via onboard sensors to
avoid hazardous areas, fulfilling their mission while ensuring operational safety. The UAVs
possess distinct roles: one serves as the leader UAV, while the others function as wingman
UAVs, with differing performance capabilities between types.
Satellite
Wingman-2
Wingman-1
Leader
Wingman-1
Wingman-2
Leader
Form a formation 
midway and maintain it
Target location
UAV cluster arrives 
at target location
Jamming 
zone
No-fly zone
Obstacle
×
×
×
 
Figure 2. Schematic diagram of UAV swarm collaborative path planning experiment.
There is exactly one leader UAV. Its primary task is to navigate around obstacles to
reach the goal location. The wingman UAVs, which may comprise multiple UAVs, must
continuously follow the leader UAV while maintaining formation and avoiding obstacles.
They must reach the goal within a short time delta relative to the leader. Wingmen may
sacrifice themselves to protect the leader if necessary.
In summary, the tasks required for cooperative path planning in UAV swarms include:
1.
The leader UAV must avoid obstacles (including jamming zones and NFZs) to prevent
collisions that could damage the UAV while ensuring it does not enter airspace
restricted to UAV overflight or interference zones.
2.
The leader UAV and the wingman UAVs are considered to have arrived simulta-
neously if they reach the target location within a time difference of less than ten
time steps.
3.
The wingmen should stay as much as possible at a safe distance from the leader UAV
to maintain formation.
The task is considered successful if the leader UAV reaches the target location within
the specified time while avoiding obstacles, and the wingman UAVs avoids obstacles as
much as possible, with all UAVs arriving simultaneously within ten time steps.
Mission failure is defined under the following conditions:
1.
The leader UAV collides with an obstacle resulting in destruction, or enters an NFZ or
jamming zone.
2.
The leader UAV fails to reach the goal location within the stipulated timeframe,
indicating inadequate planning.

## Page 6

Symmetry 2025, 17, 1970
6 of 24
3.2. UAV Kinematic Model
In the cooperative path planning of a UAV swarm, the kinematic models of all UAVs
are identical. The kinematic equation constraints can be expressed as:









.xi = vi cos ψi
.yi = vi sin ψi
.
ψi = ωi
.vi = ai
(1)
where (xi, yi) are the horizontal and vertical coordinates of the UAV, ψi is the heading
angle, vi denotes the velocity magnitude, ωi represents the angular velocity, and ui is the
acceleration (i = 1, 2 . . . , N −1).
The discrete dynamic equation constraints for the UAV swarm from time t to t + 1 are:









xt+1
i
= xt
i + vt
i cos ψt
i∆t
yt+1
i
= yt
i + vt
i sin ψt
i∆t
vt+1
i
= vt
i + at
i∆t
ψt+1
i
= ψt
i + ωt
i∆t
(2)
The state of each UAV satisfies the following constraints:

























xi,min ≤xt
i ≤xi,max
yi,min ≤yt
i ≤yi,max
vi,min ≤vt
i ≤vi,max
ψi,min ≤ψt
i ≤ψi,max
ui,min ≤ut
i ≤ui,max
ωi,min ≤ωt
i ≤ωi,max
q
(xt
i −xO)2 + (yt
i −yO)2 ≥RO
(3)
where (xO, yO) are the horizontal and vertical coordinates of the obstacle, RO is the radius
of the obstacle.
3.3. MDP Modeling of UAV Swarm Cooperative Path Planning
MDP is an ideal model for sequential decision-making under environmental condi-
tions [31–35]. In this paper, MDP is used to describe the decision model of UAV swarm
path planning, which can be defined as a five-tuple < S, A, P, R, γ > .
(1)
State Set
S is the state set, S = {s0, s1, . . . , sk−1, . . . , sN−1}, where sk−1 represents the state
observation information of the k-th UAV (1 ≤k ≤N), and N is the total number of
UAVs. This paper addresses cooperative path planning for UAV swarms. Each UAV’s
observation comprises two parts: the first part consists of its intrinsic attributes including
coordinates, heading angle, and speed magnitude, which are symmetric across all agents;
the second part comprises type-dependent observational state information—for the leader,
this includes the goal’s coordinates, obstacle coordinates, obstacle flag, and goal-reached
flag; for wingmen, this includes coordinates of the leader, obstacle, and goal. This design
introduces a controlled asymmetry in the observation space, which is crucial for facilitating
role-specific decision-making that ultimately leads to symmetric collective outcomes, such
as maintaining a symmetric formation geometry around the leader.

## Page 7

Symmetry 2025, 17, 1970
7 of 24
For the leader:
s0 =
h
x0, y0, ψ0, v0, xG, yG, xO, yO, o f , win
i
o f =
(
1, dO ≤2RO
0, otherwise
dO =
q
(x0 −xO)2 + (y0 −yO)2
win =
(
1, dG ≤D1
0, otherwise
(4)
(x0, y0) denotes the leader’s horizontal and vertical coordinates, with a heading angle
of ψ0 and a speed magnitude of v0. (xG, yG) denotes the goal location’s horizontal and
vertical coordinates, while (xO, yO) denotes the obstacle’s horizontal and vertical coordi-
nates. dO represents the distance between the UAV and the obstacle. RO is the radius of
the obstacle. The obstacle flag o f is set to 1 if dO is less than twice the obstacle’s radius;
otherwise, it is 0. dG is the distance between the UAV and the goal location. D1 is the target
arrival determination threshold. The target reached flag win is set to 1 if dG is less than D1;
otherwise, it is 0.
For wingmen:
sk = [xk, yk, ψk, vk, xG, yG, xO, yO, x0, y0]
k = 1, 2, . . . , N −1
(5)
(x0, y0) denotes the leader’s horizontal and vertical coordinates, while (xk, yk) repre-
sents the coordinates of the k-th wingman. Each respective wingman has a heading angle
of ψi and speed magnitude vi.
(2)
Action Set
A is the action set, A = {a0, a1, . . . , ak−1, . . . , aN−1}, where ak−1 represents the action
of the k-th UAV. UAV maneuver decisions are implemented by determining appropriate
acceleration and angular velocity to achieve desired speed and heading angle. The joint
action space for the k-th UAV is ak−1 = {uk−1, ωk−1}T, where uk−1 denotes the k-th UAV’s
acceleration and ωk−1 denotes its angular velocity.
(3)
State Transition Probability
P(s′|s, a) denotes the probability of a UAV transitioning from state s to state s′ after
taking action a.
(4)
Discount Factor
The discount factor is a core hyperparameter in the MDP framework that modulates
the agent’s temporal bias (myopic vs. far-sighted) and guarantees mathematical tractability
of the problem. Its value lies in the interval [0, 1].
(5)
Reward Set
To satisfy cooperative path planning requirements for UAV swarms, the reward
function incorporates proximity speed and approximated flight time terms. Separate
reward functions are designed for two UAV types:
For the leader UAV:
(a)
Boundary penalty redge.
As shown in Equation (6), dist_d represents the distances from the UAV to each of the
four boundaries, dG is the distance between the UAV and the target location, S is the safety
boundary threshold (which triggers a penalty when the UAV’s distance to any boundary is
less than this threshold, with the penalty increasing as the UAV gets closer to the boundary;
otherwise, no penalty occurs), C is the boundary penalty coefficient, S1 is the initial safety

## Page 8

Symmetry 2025, 17, 1970
8 of 24
boundary threshold, and C1 is the initial boundary penalty coefficient. When the UAV
enters within the target approach threshold D2, both the safety boundary threshold and
the boundary penalty coefficient are reduced by half; this relaxation of boundary penalty
constraints when the UAV is near the target prevents the UAV from being overly cautious
about boundary collisions and facilitates closer approach to the target.
redge = ∑max

0, S −dist_d
S

∗C;
C =
(
0.5C1, dG < D2
C1, otherwise
S =
(
0.5S1, dG < D2
S1, otherwise
(6)
(b)
Obstacle avoidance penalty robs
dO denotes the distance between the UAV and an obstacle, and RO represents the
radius of the obstacle. A linear penalty is applied when the UAV’s distance to the ob-
stacle is less than three times the obstacle’s radius but greater than one times its radius
(RO ≤dO ≤3RO), where the penalty increases progressively as the UAV approaches the
obstacle, providing incremental avoidance guidance. If the distance falls below the obsta-
cle’s radius (dO < RO), the UAV is destroyed and receives a collision penalty P1, compelling
it to learn obstacle avoidance. Otherwise, no obstacle penalty is applied.
robs =







P1,
dO < RO
dO−60
400 ,
RO ≤dO ≤3RO
0,
otherwise
(7)
(c)
Goal reward rgoal
dG denotes the distance between the leader UAV and the target point, D1 is the target
arrival determination threshold, and C2 is the heading deviation penalty coefficient. When
the leader UAV’s distance to the target point is less than a fixed threshold (dG ≤D1), the
leader reaches the goal and receives reward P (target achievement reward). As shown in
Figure 3a, φ0 represents the angular difference between the leader’s heading ψ0 and the
bearing angle θ0 from the leader to the target point. This encourages the leader UAV to fly
toward the target direction.
rgoal =
(
P,
dG ≤D1
φ0 × C2,
otherwise
(8)
φ0 = ψ0 −θ0
(9)
(d)
Formation distance reward r f ollow
Provided that the leader UAV has not crashed or reached the target location,
→
L denotes
the position of the leader UAV,
→
Pi represents the current position of the i-th wingman UAV,
αi is its ideal angular position,
→
Qi is the ideal position for this wingman, and di is the
distance between the wingman’s current position and its ideal position. D is the ideal
formation distance between the wingman and leader, σ is the formation distance tolerance
threshold, and C3 is the formation penalty coefficient. As illustrated in Figure 3b, when
the positional deviation di between the wingman’s actual and ideal positions is within
the tolerance threshold (0 ≤di ≤σ), the reward value decreases gradually as increases;
when the deviation exceeds the threshold (di > σ), the reward decreases sharply with

## Page 9

Symmetry 2025, 17, 1970
9 of 24
increasing di; maximum reward is attained when the wingman’s actual and ideal positions
coincide, thereby guiding wingman to maintain formation with the leader while avoiding
inter-agent collisions.
→
L = [x0, y0],
→
Pi = [xi, yi]
αi = (i −1) × 2π
N
→
Qi =
→
L + D · [cos αi, sin αi]
di =

→
Pi −
→
Qi
(i = 1, . . . , N −1)
r f ollow =







C3
N−1
∑
i=1
e
−di
2
2σ2 ,
o f = 0 ∧win = 0
0,
otherwise
.
(10)
(e)
Stagnation penalty rstagnation
A stagnation penalty rstagnation is subsequently designed.
→
L denotes the leader UAV’s
position at the current timestep,
→
L′ represents its position at the previous timestep, ∆is
the distance between these positions, NS is the stagnation step count, and Nmax is the
stagnation determination displacement threshold. C4 serves as the stagnation penalty
weight coefficient. When ∆< Nmax, NS increments by 1; when ∆≥Nmax, NS decrements
by 1 until reaching 0. The stagnation penalty reward is proportional to NS to prevent the
leader UAV from remaining stationary.
→
L = (x0, y0), ∆=

→
L −
→
L′

NS =



NS + 1,
∆< Nmax
max(0, NS −1),
∆≥Nmax
rstagnation =



−C4 × NS,
∆< Nmax
0,
otherwise
(11)
Downrange
Leader
Crossrange
ψ0
θ0
φ0
v0
Destination
Crossrange
Downrange
ψk
θk
φk
vk
Vck
Destination
Wingman
Wingman
Destination
Downrange
Crossrange
L
P1
Leader
Q1
（a）
（b）
（c）
Figure 3. Relevant Geometric Definitions: (a) Geometric definition of φ0 for the Leader; (b) Ideal
formation position of Leader and Wingman; (c) Geometric definitions of φk and VCk for the Wingman.
(f)
Time penalty rtime_penalty

## Page 10

Symmetry 2025, 17, 1970
10 of 24
This component encourages rapid decision-making by imposing a penalty of C5 per
timestep (where C5 is the time penalty coefficient) when the leader UAV has neither crashed
nor reached the target location.
rtime_penalty =
(
C5,
dG ≤D1 ∧dO ≥RO
0,
otherwise
(12)
(g)
Speed coordination reward rspeed
li denotes the distance from the i-th wingman to the leader UAV, ∆vi is the speed
difference between the wingman and leader, D3 is the formation coordination distance
threshold, and C6 is the speed difference tolerance. When li remains within distance D3
and ∆vi is less than C6, the speed coordination reward increments by 1, ensuring wingmen
match the leader’s speed.
li = ∥(xi, yi) −(x0, y0)∥
∆vi = ∥vi −v0∥2
rspeed = rspeed +
N−1
∑
i=1
H(x)
H(x) =
(
1,
0 ≤li ≤D3Λ∆vi < C6
0,
otherwise
(13)
(h)
Temporal coordination reward rreachstep
t f,i denotes the timestep when the i-th wingman reaches the target, tlead represents the
timestep when the leader reaches the target, ∆ti is the arrival time difference between wing-
man and leader, and Tmax is the formation time coordination tolerance. When ∆ti < Tmax, a
linearly decreasing reward is applied where smaller time differences yield higher rewards,
guiding leader and wingmen to achieve simultaneous arrival at target.
∆ti =
t f,i −tlead

rreachstep[i] =



200 −20∆ti,
∆ti < Tmax
0,
otherwise
rreachstep =
N−1
∑
i=1
rreachstep[i]
(14)
(i)
Terminal achievement reward rtermination
Case 1: All wingmen reach the target within 10 timesteps after the leader’s ar-
rival. Case 2: Leader reaches within 1000 timesteps but wingmen fail to arrive within
1010 timesteps. Case 3: Leader fails to reach within the designated 1000 timesteps. Here,
P2 is the base reward for full formation coordination success, P3 is the base reward for
leader’s core mission completion, and t represents elapsed timesteps. This incentivizes
rapid task accomplishment by both leader and wingmen.
rtermination =





P2 −t,
ifcase1
P3 −t,
elifcase2
0,
elsecase3
(15)
The reward function for the leader UAV is defined as: RL = ωL,1 × redge + ωL,2 ×
robs+ωL,3 × rgoal + ωL,4 × r f ollow + ωL,5 × rstagnation + ωL,6 × rtime_penalty + ωL,7 × rspeed +
ωL,8 × rreachstep+ωL,9 × rtermination, Here, ωL,1 to ωL,9 represent the weights assigned to
each reward component.

## Page 11

Symmetry 2025, 17, 1970
11 of 24
For wingmen, the boundary penalty (redge), obstacle avoidance penalty (robs), goal
achievement reward (rgoal), formation distance reward (r f ollow), stagnation penalty
(rstagnation), time penalty (rtime_penalty), speed coordination reward (rspeed), and arrival time
difference reward (rreachstep) mirror those of the leader but with adjusted parameters (C2
= 5, C3 = 20, C4 = 1, C5 = −0.5). The formation distance, speed coordination, and arrival
time difference rewards are specific to the k-th wingman relative to the leader (i.e., i = k
in Equations (9), (12) and (13)). Additionally, the remaining flight time difference reward
(r∆tgo [36]) is introduced. As shown in Figure 3c, vk denotes the speed magnitude of the k-th
wingman (v0 for the leader), φk represents the angular difference between the wingman’s
heading angle ψk and the bearing angle θk from the wingman to the target point. VCk is
the closing velocity component of the k-th wingman along the line-of-sight to the target
point (VC0 for the leader). The term tgok approximates the remaining flight time for the
k-th wingman (tgo0 for the leader), and C7 is the remaining flight time difference penalty
coefficient. The difference in approximated remaining flight time between wingman k and
the leader is ∆tgok. A larger time difference incurs a higher penalty, guiding the leader and
wingmen to reach the target simultaneously.
VCk = vk × cos φk
tgok =
VCk
∥(xi,yi)−(xG,yG)∥2
∆tgok = tgok −tgo0
r∆tgo = −C7 × ∆tgok
(16)
The reward function for the k-th wingman is: RF,k = ωF,1 × redge,k + ωF,2 × robs,k +
ωF,3×rgoal,k + ωF,4 × r f ollow,k + ωF,5 × rstagnation,k + ωF,6 × rtime_penalty,k + ωF,7 × rspeed,k +
ωF,8 × rreachstep,k+ωF,9 × r∆tgo,k, where ωF,1 to ωF,9 denote the corresponding weights.
The overall reward set R comprises the leader’s reward RL and the rewards for the
N −1 wingmen RF, k, expressed as: R = [RL, RF,1, RF,2, . . . , RF,N−1].
The weights assigned to sub-rewards are determined based on their relative im-
portance to the overall mission accomplishment. The core principle guiding the weight
selection process is to ensure that the agent prioritizes learning critical survival behaviors
(e.g., obstacle avoidance) and primary mission objectives (e.g., synchronized arrival) over
secondary goals (e.g., perfect formation maintenance). Initial weight values were heuris-
tically assigned according to this priority and were subsequently empirically fine-tuned
through ablation studies. The learning process demonstrates significant sensitivity to
weight balancing. For instance, excessively increasing the weight for formation distance
reward could lead the agent to over-prioritize precise positioning, potentially compro-
mising goal attainment or even resulting in collisions. Conversely, if the weight for the
synchronized arrival reward is set too low, the agent may successfully avoid obstacles but
fail to coordinate arrival times.
4. Method
4.1. MASAC-CA Algorithm
The core of our approach is the MASAC-CA algorithm, which formulates the UAV
swarm path planning problem within a Reinforcement Learning (RL) paradigm guided by
symmetry principles. The overall RL concept, modeled as a heterogeneous Markov Deci-
sion Process (MDP), is depicted in Figure 4. The heterogeneity in the MDP is not arbitrary;
it is a deliberate asymmetric design to enforce symmetry in the group’s spatiotemporal
execution. The leader-wingman role asymmetry, reflected in their state representations
and reward functions, serves as the foundation for achieving symmetric formation flight
and simultaneous arrival. The MASAC-CA algorithm adopts a centralized training with

## Page 12

Symmetry 2025, 17, 1970
12 of 24
decentralized execution framework, where both the leader UAV and each wingman UAV
operate an independent Soft Actor-Critic (SAC) algorithm. This CTDE architecture itself
exhibits a form of procedural symmetry: during execution, all agents symmetrically utilize
their local policies, while the asymmetric coordination knowledge is distilled into these
policies during the centralized training phase. The specific architectural details and training
procedure of the MASAC-CA algorithm are presented in Figure 5 and described in the
following subsections. During training, the Actor (policy network) takes the state informa-
tion sk(t) of agent k at time t as input and outputs the parameters of the action probability
distribution, which governs the agent’s execution of action ak(t). The physical environment
executes the collective action set A (comprising all agents’ actions), yielding the state set
S(t+1) at t + 1 and the reward set R(t) at t. Subsequently, the current state set S(t), action
set A(t), reward set R(t), and next state set S(t+1) are stored in the experience replay
buffer. Finally, a batch of data is randomly sampled from the buffer, and agent k uses the
concatenated state-action information (sk, ak) as input to its Critic network to guide the
training of the value network.
Figure 4. Reinforcement learning block diagram of the MASAC-CA algorithm.
 
Figure 5. MASAC-CA algorithm framework.

## Page 13

Symmetry 2025, 17, 1970
13 of 24
4.2. Algorithm Update Procedure
For agent k, the update processes for its Actor network, Critic network, and entropy
network are similar to the traditional SAC algorithm. The policy network is approximated
by an Actor network with weight parameters θ, while the value network is approximated
by a Critic network with weight parameters ω. This study employs the Adaptive Moment
Estimation (Adam) algorithm to optimize and update the MASAC-CA network parameters.
B denotes the experience replay buffer. Loss calculation requires averaging over a batch
of samples drawn from the buffer, reflecting the average quality of the sampled data. As
shown in Figure 5, data (R(t),A(t),S(t),S(t+1))
sampled from the experience replay
buffer is used to update the Q Critic networks. Based on the optimal Bellman equation,
U(t)(q) = r(t) + γ · v(S(t+1)) serves as the estimated true value of state S(t). The pre-
dicted value estimate of state S(t) is given by qi(S(t),A(t); ω(i)).(i = 0, 1) evaluated at the
taken A(t). Finally, the MSE (Mean Squared Error) is used as the loss function, where the
average is computed over a batch of data drawn from the buffer. This trains the neural
networks Q0 Critic and Q1 Critic.
LMSE = ∑B[qi(S(t),A(t);ω(i)) −U(t)(q)]2
|B|
(17)
Similarly, data (R(t),A(t),S(t),S(t+1))
sampled from the buffer is used to update
the V Critic network. The estimated true value of state S(t) is given by U(t)(v), which
incorporates an entropy term. The predicted value estimate is provided by the V Critic’s
output v(S(t);ω(i)).. The MSE loss function is then used to train the V Critic neural network.
U(t)(v) = EA′(t)∼π(·|S(t);θ)

min
i=0,1qi(S(t), A′(t);ω(i)) −α ln π(A′(t)|S(t);θ)
i
LMSE =
∑B[v

S(t);ω(v))−U(t)(v)]
2
|B|
(18)
The target V Critic network parameters, denoted by ω, are softly updated using the
following equation, where τ is the soft update rate [37].
ω ←(1 −τ) · ω + τ · ω
(19)
The loss for training the Actor network is given by the following expression:
L = −1
|B|∑B EA′(t)∼π(·|S(t);θ)

q0
S
t),A′t)) −α ln π(A′(t)|S(t);θ)]
(20)
This loss is used for gradient descent training of the Actor network, optimized via
the Adam algorithm. A′(t) denotes a newly sampled action under state S(t) according
to the current policy π of the Actor network—not drawn from the experience replay
buffer. α is the entropy reward coefficient, determining the importance of the entropy term
ln π(A′(t)|S(t);θ); a higher α indicates greater importance. This work employs Ornstein–
Uhlenbeck (OU) noise, which generates temporally correlated exploration, as the explo-
ration noise for the policy network. The complete training procedure of MASAC-CA is
summarized in Algorithm 1.

## Page 14

Symmetry 2025, 17, 1970
14 of 24
Algorithm 1: MASAC-CA training procedure
Multi-Agent Soft Actor-Critic with Cooperative Arrival (MASAC-CA)
Input: Number of agents N, learning rates ηθ, ηω, ηα, soft update rate τ, discount factor
γ, replay buffer size B, batch size M
Output: Trained policy networks πk for all agents k = 1, . . . , N
1. Initialize:
Actor networks πk with parameters θk for each agent k
Critic networks Q0,k, Q1,k with parameters ω0,k, ω1,k
Value network Vk with parameters ωV,k
Target value network V′
k with parameters ω′
V,k ←ωV,k
Replay buffer D with capacity B
Entropy coefficient α
2. for episode = 1 to Emax do
3. Initialize environment, obtain initial heterogeneous state S(0)
4. for t = 0 to T −1 do
5.
for each agent k do
6.
Sample action ak(t) ∼πk(· | sk(t); θk)
7.
end for
8.
Execute joint action A(t) = [a1(t), . . . , aN(t)]
9.
Observe comprehensive reward R(t) and next heterogeneous state S(t + 1)
10. Store transition (S(t), A(t), R(t), S(t + 1)) in D
11.
if | D |≥M then
12.
Sample minibatch {(S, A, R, S′)} ∼D of size M
13.
//Update Critic networks
14.
for each agent k do
15.
U(q)
k
= rk + γ · V′
k(S′; ω′
V,k) # Equation (17)
16.
Update ωi,k by minimizing:
L(ωi,k) = E[(Qi,k(S, A; ωi,k) −U(q)
k )2], i = 0, 1 # Equation (17)
17.
end for
18.
//Update Value networks
19.
for each agent k do
20.
Sample A′ ∼π(S; θ)
21.
U(v)
k
= E[min
i=0,1Qi,kt(S, A′) −α log π(A′ | S; θ] # Equation (18)
22.
Update ωV,k by minimizing:
L(ωV,k) = E[(Vk(S; ωV,k) −U(v)
k )2] # Equation (18)
23.
end for
24. //Update Actor networks
25.
for each agent k do
26.
Update θk by minimizing:
L(θk) = −E[Q0,k(S, A′) −α log π(A′ | S; θ)] # Equation (20)
27.
end for
28. //Soft update target networks
29.
for each agent k do
30.
ω′
V,k ←(1 −τ)ω′
V,k + τωV,k # Equation (19)
31.
end for
32. end if
33. end for
34. end for

## Page 15

Symmetry 2025, 17, 1970
15 of 24
5. Experiments
5.1. Simulation Environment and Algorithm Parameter Settings
This study designs a reinforcement learning interaction environment for UAV path
planning.
The simulation platform was developed in Python within the PyCharm
(Professional 2025.1.1) IDE. The core algorithm was implemented using the PyTorch 2.8.1
deep learning framework, and the environment was built following the OpenAI Gym inter-
face standards for standardized agent-environment interactions. Numerical computation
and visualization were handled using NumPy 1.23.3, Matplotlib 3.5.1, and PyGame 2.1.2.
At each episode, the initial states of the UAV swarm, goal position and obstacle position
are fully randomly initialized [5]. Since the UAVs in this paper are primarily intended
for air-to-ground operations, their motion is simplified to a single altitude, conforming to
kinematic equations in two-dimensional space. Consequently, the following assumptions
are made:
(1)
The real-world three-dimensional motion of UAVs is simplified into a two-dimensional form.
(2)
The position information of the goal location and obstacles is assumed known, ac-
quired by ground-based radar and communicated to the UAVs.
The cooperative path planning simulation environment for the unmanned swarm is
defined as a 10,000 m × 8000 m two-dimensional plane. This custom environment features
a built-in physics engine that computes state transitions based on the UAV kinematic
model (Equations (1)–(3)) and handles collision detection. The composite reward function
described in Section 3.3 is computed at each step. There are two distinct types of UAVs:
the leader UAV, with a speed range of 100~200 m/s, acceleration control input range
of −3~3 m/s2, and angular velocity range of −0.6~0.6 rad/s; and the wingman, which
possesses higher maneuverability than the leader one to facilitate maintaining formation.
Its speed range is 100~500 m/s, acceleration range is −8~8 m/s2, and angular velocity
range is −1.2~1.2 rad/s. The planning task is deemed successful, ending the episode, if
both the leader and wingman UAVs arrive within the circular area of the goal location
within a short time difference. Conversely, the planning task fails and the episode ends if
the leader UAV enters the circular area of any obstacle zone, which signifies a collision.
Table 1 lists all parameters and hyperparameters used in the MASAC-CA algorithm.
The parameters for the OU noise are set to σOU = 0.1, θOU = 0.1, dtOU = 0.01, and OU
noise is only added during the first 20 episodes. As shown in Algorithm 1, the actor network
is a fully connected layer with a structure of 10-256-256-2, utilizing relu and tanh activation
functions. The neural network’s initial weights are randomly sampled from a normal
distribution with a mean of 0 and a variance of 0.1, with a learning rate of 1 × 10−3. The
learning rates for the actor, critic, and entropy networks were chosen based on established
practices in SAC literature and preliminary hyperparameter tuning. Specifically, the actor
employs a lower learning rate to ensure stable policy updates. The critic network takes
the augmented information of state and action as input; the number of input layer nodes
is 10 × N + 2, and it uses only the relu activation function. Its initial weights are also
randomly sampled from a normal distribution (mean 0, variance 0.1), with a learning rate
of 3 × 10−3. A higher learning rate for the critic facilitates rapid convergence of value
estimates, providing a stable foundation for the actor’s updates. The entropy network lacks
a fully connected layer structure; its log entropy weight is automatically adjusted during
training, with a learning rate of 3 × 10−4. The smallest learning rate is used for the entropy
network to ensure smooth and stable adjustment of the exploration-exploitation trade-off.
Table 2 lists the parameter settings of the reward functions introduced in Section 3.3.

## Page 16

Symmetry 2025, 17, 1970
16 of 24
Table 1. Parameters and hyperparameters of MASAC-CA.
Parameter
Hyperparameter
Actor Network
Critic Network
Actor learning rate: 1 × 10−3
Maxstep: 1000
Input: 10
Input:10 × N + 2
Critic learning rate: 3 × 10−3
Batch size: 128
Hidden: (256, 256)
Hidden: (256, 256)
Entropy learning rate: 3 × 10−4
Maxepisode: 800
Output: 2
Output: 1
Soft update rate: 1 × 10−2
Replay buffer: 20,000
Activation: relu, tanh
Activation: relu
Discount factor: 0.9
Optimizer: adam
Weights: N(0, 0.1)
Weights: N(0, 0.1)
Table 2. MASAC-CA reward function parameters settings.
Reward Function Parameters
Parameter
Symbol
Parameter Description
Leader
Value
Wingman
Value
Environment Interaction Parameters
dO
Obstacle radius
20 m
D1
Target arrival determination threshold
40 m
D2
Target proximity threshold
50 m
S1
Basic safety boundary threshold
20 m
Penalty Coefficients
P1
Collision penalty
−500
C1
Basic boundary penalty coefficient
−50
C2
Heading deviation penalty coefficient
10
5
C3
Formation penalty coefficient
300
400
C4
Stagnation penalty weight coefficient
0.1
1
C5
Time penalty coefficient
−0.6
−0.5
C7
Remaining flight time difference penalty coefficient
——
100
Formation Coordination Parameters
D
Ideal formation distance
30 m
σ
Formation distance tolerance threshold
15 m
D3
Formation coordination distance threshold
50 m
C6
Velocity difference tolerance
2 m/s
Tmax
Formation coordination time threshold
10 s
Nmax
Stagnation determination displacement threshold
5 m
Reward Parameters
P
Target achievement reward
2000
1000
P2
Full formation coordination reward
1500
——
P3
Core mission achievement reward
1000
——
5.2. Training Process Comparison
During the training phase, the time step ∆t is set to 1, employing a dual-UAV for-
mation cooperative training architecture with a dynamically generated random obstacle
and a randomly generated goal point. When a mission fails due to collision with the
obstacle, boundary violation, or timeout, the current training episode is immediately reset
while maintaining a fixed total of 800 training episodes. To ensure statistical reliability
and address performance variability concerns, we conducted multiple independent train-
ing runs (n = 50) and present the mean reward curves with standard deviation bands
for MASAC-CA in Figure 6. This statistical validation demonstrates the algorithm’s con-
sistency across different random seeds, with tight confidence intervals confirming the
reproducibility of our results. As depicted in Figure 7, under the guidance of our meticu-
lously designed reward function for simultaneous arrival tasks and heterogeneous Markov
Decision Process (MDP) modeling, the resulting cooperative control strategy demonstrates
wingmen’s ability to maintain stable preset formation distances while following the leader
throughout all flight phases—including initial high-maneuverability turns, mid-term cruise

## Page 17

Symmetry 2025, 17, 1970
17 of 24
segments, and final precision approach turns. By accumulating and normalizing per-step
agent rewards across episodes, we compared the leader sub-reward, wingman sub-reward,
and total reward curves of our MASAC-CA algorithm against baseline MASAC, as well
as two additional baselines: Random Strategy and MADDPG. Unlike MASAC’s volatile
normalized rewards (plunging from 0.89 to 0.45 due to frequent leader collisions with
obstacles causing premature termination), the highly unstable rewards of Random Strat-
egy (exhibiting severe fluctuations and persistently low values across episodes), and the
unstable performance of MADDPG’s wingman sub-rewards (indicating its difficulty in
maintaining a fixed formation topology over the long term), MASAC-CA’s spatiotemporal
coordination rewards yield: wingman sub-rewards stabilizing after 100 episodes with
minor fluctuations, while leader sub-rewards remain consistently stable post-100 episodes
(confirming reliable obstacle avoidance and timely target arrival). This strategy thus en-
sures successful swarm cooperative path planning—obstacle avoidance, target arrival, and
formation maintenance—by strategically managing wingman risks, enabling both leader
and wingmen to consecutively reach targets within minimal time differentials.
Figure 6. Reward Curves with Mean and Standard Deviation for MASAC-CA.
Figure 7. Comparison of training reward curves between MASAC-CA and baseline.

## Page 18

Symmetry 2025, 17, 1970
18 of 24
5.3. Testing Process Comparison
To evaluate the performance of the MASAC-CA algorithm, multiple Monte Carlo tests
were conducted on the trained cooperative path planning decisions of the UAV swarm, as
presented in Table 3, using mission success rate (MSR, where nC is the number of successful
episodes with both leader and wingmen reaching the goal and nT is the total test episodes),
formation keeping rate (FKR, measuring the proportion of time steps tC maintaining
formation versus total steps tT), total flight duration (T, with t f being the terminal time
until collision or goal arrival), flight trajectory length (S, integrating velocity v over flight
duration), flight energy consumption (C, integrating acceleration a and angular velocity
ω over flight duration), collision number (CN, tallying collisions ncn across episodes),
and abruptness (A, quantifying heading angle changes ∆εt exceeding π
6 ) as performance
metrics [38].
Table 3. Performance evaluation indicators for collaborative path planning algorithm of UAV cluster.
Metric Name
Symbol
Formula
Mission Success Rate
JMSR
JMSR = nC
nT
Formation Keeping Rate
JFKR
JFKR = tC
tT
Total Flight Duration
JT
JT = t f
Flight Trajectory Length
JS
JS = R t f
0 vdt
Flight Energy Consumption
JC
JC = R t f
0 (|a| + |ω|)dt
Number of Collisions
JCN
JCN =
nT
∑
k=1
ncn
Abruptness
JA
JA =
t f
∑
t=1
(
0,
i f |∆εt| < π
6
1,
otherwise
5.3.1. Wingman Quantity Analysis
For clear observation of flight trajectories, the time step is set to 0.1 during the test-
ing phase. Utilizing the trained neural network weights from Section 3.2, experiments
were conducted with the number of wingman UAV expanded to 2, 3, and 4. Performance
metrics—including Mission Success Rate (MSR), Formation Keeping Rate (FKR), total flight
duration, trajectory length, and energy consumption—were evaluated through 100 Monte
Carlo tests (results summarized in Table 4). While MASAC-CA performs comparably to
MASAC in total flight duration, trajectory length, and energy consumption, it achieves
about 13% improvement in MSR (approaching 100%) and significantly enhanced FKR. This
effectively resolves critical challenges in swarm cooperative path planning, demonstrating
the algorithm’s superiority. In contrast, both the Random Strategy and the MADDPG algo-
rithm perform poorly due to their inability to maintain formation and achieve coordinated
arrival at the target.
Table 4. The performance metrics of MASAC and MASAC-CA algorithms for varying numbers of
UAVs.
Number
Algorithm
JMSR (%)
JFKR(%)
JT
JS
JC
2
MASAC
87.0
22.83
203.93
116.63
229.45
MASAC-CA
99.0
59.68
253.81
142.69
282.85
Random Strategy
0.0
7.10
999.0
510.05
999.83
MADDPG
0.0
5.55
215.01
122.86
184.78

## Page 19

Symmetry 2025, 17, 1970
19 of 24
Table 4. Cont.
Number
Algorithm
JMSR (%)
JFKR(%)
JT
JS
JC
3
MASAC
83.0
10.77
195.05
111.78
219.55
MASAC-CA
99.0
40.91
253.52
140.62
283.34
Random Strategy
0.0
1.54
999.0
501.34
999.66
MADDPG
0.0
1.11
218.67
123.55
187.64
4
MASAC
83.0
1.75
200.34
111.67
229.99
MASAC-CA
99.0
33.81
253.31
140.34
279.19
Random Strategy
0.0
0.35
999.0
495.85
1002.41
MADDPG
97.0
1.96
209.99
121.99
180.68
5
MASAC
87.0
1.57
214.61
119.63
242.24
MASAC-CA
99.0
26.29
257.27
137.99
287.19
Random Strategy
0.0
0.15
999.0
499.76
1001.76
MADDPG
0.0
0.13
218.46
124.45
188.63
5.3.2. Cooperative Behavior Analysis
Figure 8 illustrates the temporal evolution of heading angle, velocity, and inter-agent
distance between the leader and the k-th wingman during a test episode. Through com-
parative analysis of the four algorithms, distinct differences in their cooperative control
capabilities become evident. In terms of heading angle and velocity coordination, MASAC-
CA (solid red lines) demonstrates superior performance, achieving near-perfect alignment
in both heading angles and velocities for both UAVs after 75 timesteps. In contrast, MASAC
(dashed blue lines) fails to achieve velocity convergence between the two UAVs, while
MADDPG (dash-dotted purple lines) exhibits significant disparities in both velocity and
heading angle. This phenomenon arises because the reward functions of both MASAC
and MADDPG inadequately address the temporal consistency requirements for formation
maintenance, lacking effective cooperative guidance mechanisms.
Regarding inter-agent distance control, the algorithmic differences become more pro-
nounced. The random policy (dotted gray lines) occasionally achieves velocity and heading
alignment but maintains an excessive separation exceeding 100 m, rendering effective
formation maintenance impossible. This reflects the inherent inefficiency of random explo-
ration in complex environments—completely lacking learning capability and formation
awareness, the inter-agent distances remain purely stochastic, preventing meaningful coop-
eration. MADDPG exhibits more hazardous behavior: its distance curve initially decreases
sharply to 2 m before growing continuously without stabilization, indicating not only poor
formation keeping but also high collision risk. This instability stems from MADDPG’s
lack of explicit leader-wingman role coordination mechanisms, resulting in behavioral
inconsistencies. MASAC’s distance behavior also proves problematic: the curve initially
decreases to approximately 3 m (indicating high collision risk) before overshooting and
increasing. This non-monotonic behavior results from flawed reward design—providing
constant distance rewards within a 50-m threshold without precise guidance toward the
ideal range, causing initial aggressive approach followed by subsequent overshoot.
Conversely, MASAC-CA exhibits exceptional performance in distance control: it
smoothly reduces distance within the first 25 timesteps before stabilizing within the safe
30–40 m range. This optimal performance benefits from its Gaussian-based reward design,
which peaks at the ideal distance (30 m), enabling smooth and stable convergence. The
results demonstrate that under MASAC-CA, wingmen effectively converge toward the

## Page 20

Symmetry 2025, 17, 1970
20 of 24
leader while maintaining safe distances, achieving synchronized formation movement
with significantly enhanced cooperative formation-keeping capability. This reflects the
successful enforcement of spatial symmetry in the swarm’s configuration, a direct result
of the asymmetric role assignment and symmetric incentive mechanism in our reward
design—markedly superior to MADDPG’s unstable performance and the completely unco-
ordinated behavior of the random policy.
 
Figure 8. Curves of heading angle, velocity and distance between leader and the k-th wingman.
5.3.3. Algorithm Robustness Analysis
To evaluate the model’s adaptability in complex uncertain environments, a scenario
comprising ten randomized obstacles, a randomized goal, one leader UAV and three wing-
men was designed (Figure 9). The distinct colors of the obstacles are used to differentiate
them and enhance visual clarity. Robustness was verified through perturbations applied to
the goal position during frames 80–180 (simulating positioning errors or environmental
interference). During training, episodes terminated upon collision or goal arrival, whereas
during validation, episodes concluded only upon goal arrival. Simulations demonstrate
the model maintains formation and achieves coordinated goal arrival under complex un-
certainties. Statistical results in Figure 10 confirm MASAC-CA’s superiority over MASAC
and random policy [4] across all metrics (particularly in formation keeping and collision
prevention). As depicted in Figure 11 (∆t = 1), collision counts and abruptness statistics over
100 episodes reveal: with increasing obstacle density, MASAC-CA maintains near-constant
collision counts and abruptness while MASAC exhibits linear escalation. This superior col-
lision avoidance (CN) performance is attributed to our core designs: an intelligent reward
function with explicit safety penalties, a heterogeneous state design enabling real-time

## Page 21

Symmetry 2025, 17, 1970
21 of 24
leader–follower coordination, and the robust CTDE framework. These elements collectively
empower the swarm with enhanced collaborative obstacle avoidance capabilities. The
results prove MASAC-CA’s significantly higher flight stability and safety.
Figure 9. Simulation results of the model’s adaptability and robustness in complex uncertain environments.
Figure 10. Statistical results of various evaluation metrics in complex uncertain environments.
Figure 11. Trend curves of CN and abruptness across varying obstacle densities.

## Page 22

Symmetry 2025, 17, 1970
22 of 24
6. Conclusions
In this paper, a cooperative path planning method for UAV swarms, termed MASAC-
CA, was proposed and evaluated. The approach builds on a heterogeneous MDP formula-
tion with agent-specific state representations—including a terminal flag for the leader and
leader-referenced coordinates for wingmen—and a composite reward function that incen-
tivizes simultaneous arrival while satisfying formation, safety, and spatial constraints. The
core design philosophy leverages strategic asymmetry in roles and information structures
to engender robust symmetries in the collective behavior, such as stable formation topology
and synchronized arrival. This symmetry–asymmetry duality is central to the method’s
effectiveness. The complex reward scheme is designed to enhance training stability and con-
vergence relative to baseline algorithms. Simulation results demonstrate that MASAC-CA
improves mission success rates by ~13% (reaching near 100%), sustains safe formation
distance (30–40 m), reduces collisions to near zero, and exhibits robustness in cluttered
environments. Moreover, the method maintains high performance in environments with
multiple random obstacles, confirming its robustness.
In the future, we will extend the framework to 3D dynamic target pursuit scenarios,
which involves addressing several key challenges: expanding the state space to include
altitude and 3D orientation, extending the action space for 3D motion control, adapting
the reward function for 3D formation keeping (using Euclidean distance) and obstacle
avoidance (considering spherical obstacles), and developing strategies to mitigate the
increased complexity and curse of dimensionality. The inherent spatial symmetries (e.g., ro-
tational symmetry in formations) and asymmetries (e.g., in obstacle distributions) of 3D
environments will be explicitly considered in the state and reward design. While this study
validates the algorithm using a fixed formation topology, the proposed heterogeneous MDP
and reward architecture provide a foundation that can be extended to support dynamic
swarm topologies adapted to different mission phases or environmental constraints. This
could involve studying morphological symmetry transitions, where the swarm dynamically
reconfigures its symmetric pattern (e.g., from a linear line to a V-shape) in response to
environmental cues. Additionally, to enhance practical applicability, we will systematically
investigate the impact of realistic communication impairments, such as packet loss and
delays, on system performance. This will involve modeling these constraints within the
training environment and developing communication-aware policies to improve the ro-
bustness of MASAC-CA in real-world wireless network conditions. Furthermore, to bridge
the gap between simulation and real-world deployment, future research will focus on the
integration of onboard sensors and real-time data fusion techniques, enabling the system
to operate autonomously in GPS-denied and communication-limited environments. The
heterogeneous MDP architecture and CTDE paradigm validated in this 2D study provide a
solid foundation for these extensions. We will subsequently promote its practical imple-
mentation in real UAV swarm platforms operating in complex and uncertain environments.
Author Contributions: Conceptualization, W.H. and M.Z.; methodology, W.H. and L.Y.; software,
W.H.; validation, M.Z., X.X., S.Q. and T.L.; formal analysis, W.H.; investigation, W.H.; resources,
W.H.; data curation, W.H.; writing—original draft, W.H.; writing—review & editing, L.Y. and M.Z.;
visualization, W.H.; supervision, M.Z., X.X., S.Q., T.L. and L.Y.; project administration, M.Z., X.X.,
S.Q., T.L. and L.Y. All authors have read and agreed to the published version of the manuscript.
Funding: This research received no external funding.
Data Availability Statement: The original contributions presented in this study are included in the
article. Further inquiries can be directed to the corresponding authors.
Conflicts of Interest: The authors declare no conflicts of interest.

## Page 23

Symmetry 2025, 17, 1970
23 of 24
References
1.
Shao, S.K.; Peng, Y.; He, C.L.; Du, Y. Efficient path planning for UAV formation via comprehensively improved particle swarm
optimization. ISA Trans. 2020, 97, 415–430. [CrossRef] [PubMed]
2.
Wu, Y.; Gou, J.Z.; Hu, X.T.; Huang, Y. A new consensus theory-based method for formation control and obstacle avoidance of
UAVs. Aerosp. Sci. Technol. 2020, 107, 106332. [CrossRef]
3.
Qu, C.Z.; Gai, W.D.; Zhong, M.Y.; Zhang, J. A novel reinforcement learning based grey wolf optimizer algorithm for unmanned
aerial vehicles (UAVs) path planning. Appl. Soft Comput. 2020, 89, 106099. [CrossRef]
4.
Fang, C.L.; Yang, F.S.; Pan, Q. Multi-UAV cooperative path planning based on MASAC reinforcement learning algorithm. Sci. Sin.
Informationis 2024, 54, 1871–1883. [CrossRef]
5.
Northwestern Polytechnical University Shenzhen Research Institute. UAV Path Planning Method and Device Based on Maximum
Entropy Safe Reinforcement Learning. CN202410423432.7, 14 June 2024.
6.
Kim, S.; Jung, D. Multiresolution approximation MDP for multi-target reconnaissance online planning. Int. J. Aeronaut. Space Sci.
2025, 26, 2657–2676. [CrossRef]
7.
Bany Salameh, H.; Hussienat, A.; Alhafnawi, M.; Al-Ajlouni, A. Autonomous UAV-based surveillance system for multi-target
detection using reinforcement learning. Clust. Comput. 2024, 27, 9381–9394. [CrossRef]
8.
Ryu, S.K.; Jeong, B.M.; Choi, H.L. MDP formulation for multi-UAVs mission planning with refueling constraints. In Robot
Intelligence Technology and Applications 7, Proceedings of the 10th International Conference on Robot Intelligence Technology and
Applications (RiTA 2022), Kuala Lumpur, Malaysia, 7–9 December 2022; Jo, J., Myung, H., Alshehhi, A.A., Eds.; Lecture Notes in
Networks and Systems; Springer: Cham, Switzerland, 2023; Volume 642, pp. 89–103. [CrossRef]
9.
Zheng, Y.; Xin, B.; He, B.; Ding, Y. Mean policy-based proximal policy optimization for maneuvering decision in multi-UAV air
combat. Neural Comput. Appl. 2024, 36, 19667–19690. [CrossRef]
10.
Xu, L.; Zhang, X.; Xiao, D.; Liu, B.; Liu, A. Research on heterogeneous multi-UAV collaborative decision-making method based
on improved PPO. Appl. Intell. 2024, 54, 9892–9905. [CrossRef]
11.
Qu, P.; He, C.; Wu, X.; Wang, E.; Xu, S.; Liu, H.; Sun, X. Double mixing networks based monotonic value function decomposition
algorithm for swarm intelligence in UAVs. Auton. Agent Multi-Agent Syst. 2025, 39, 16. [CrossRef]
12.
Zhang, Y.; Wang, S.; Chen, Z.; Xu, X.; Funiak, S.; Liu, J. Towards cost-efficient federated multi-agent RL with learnable aggregation.
In Advances in Knowledge Discovery and Data Mining, Proceedings of the 28th Pacific-Asia Conference on Knowledge Discovery and Data
Mining (PAKDD 2024), Taipei, Taiwan, 7–10 May 2024; Yang, D.N., Xie, X., Tseng, V.S., Pei, J., Huang, J.W., Lin, J.C.W., Eds.; Lecture
Notes in Computer Science; Springer: Singapore, 2024; Volume 14646, pp. 154–168. [CrossRef]
13.
Dijkstra, E.W. A note on two problems in connexion with graphs. Numer. Math. 1959, 1, 269–271. [CrossRef]
14.
Hart, P.E.; Nilsson, N.J.; Raphael, B. A formal basis for the heuristic determination of minimum cost paths. IEEE Trans. Syst. Sci.
Cybern. 1968, 4, 100–107. [CrossRef]
15.
Stentz, A. Optimal and efficient path planning for partially-known environments. In Proceedings of the IEEE International
Conference on Robotics and Automation, San Diego, CA, USA, 8–13 May 1994; pp. 3310–3317.
16.
Dewangan, R.K.; Shukla, A.; Godfrey, W.W. Three dimensional path planning using grey wolf optimizer for UAVs. Appl. Intell.
2019, 49, 2201–2217. [CrossRef]
17.
Han, Z.; Chen, M.; Shao, S.; Zhou, T.; Wu, Q. Path planning of unmanned autonomous helicopter based on hybrid satisficing
decision-enhanced swarm intelligence algorithm. IEEE Trans. Cogn. Dev. Syst. 2023, 15, 1371–1385. [CrossRef]
18.
Wu, W.H.; Guo, X.F.; Zhou, S.Y. Dynamic path planning based on improved constrained differential evolution algorithm. Control
Decis. 2020, 35, 2381–2390.
19.
Yu, X.B.; Jiang, N.J.; Wang, X.M.; Li, M. A hybrid algorithm based on grey wolf optimizer and differential evolution for UAV path
planning. Expert Syst. Appl. 2023, 215, 119327. [CrossRef]
20.
Xu, L.; Cao, X.B.; Du, W.B.; Li, Y. Cooperative path planning optimization for multiple UAVs with communication constraints.
Knowl.-Based Syst. 2023, 260, 110164. [CrossRef]
21.
Zhu, D.; Yang, S.X. Bio-inspired neural network-based optimal path planning for UUVs under the effect of ocean currents. IEEE
Trans. Intell. Veh. 2022, 7, 231–239. [CrossRef]
22.
Lin, L.; Zhang, X.S.; Han, C.L.; Ma, H. UAV maneuvering target tracking based on Kalman filter and DDQN algorithm. Tactical
Missile Technol. 2022, 98–104.
23.
Li, B.; Yang, Z.P.; Chen, D.Q.; Liang, S.-Y.; Ma, H. Maneuvering target tracking of UAV based on MN-DDPG and transfer learning.
Def. Technol. 2021, 17, 457–466. [CrossRef]
24.
Hua, X.; Wang, X.Q.; Rui, T.; Shao, F.; Wang, D. Vision-based end-to-end target tracking control technology for UAV. J. Zhejiang
Univ. 2022, 56, 1–9.
25.
Zhang, H.H.; He, P.K.; Zhang, M. UAV target tracking method based on deep reinforcement learning. In Proceedings of the 2022
International Conference on Cyber-Physical Social Intelligence (ICCSI), Beijing, China, 18–21 November 2022; pp. 274–277.

## Page 24

Symmetry 2025, 17, 1970
24 of 24
26.
Xiang, X.J. Coordinated formation control for fixed-wing UAVs based on deep reinforcement learning. Acta Aeronaut. Astronaut.
Sin. 2021, 42, 1–10.
27.
Masmitja, I.; Martin, M.; Katija, K.; Gomariz, S.; Navarro, J. A reinforcement learning path planning approach for range-only
underwater target localization with autonomous vehicles. IEEE J. Ocean. Eng. 2022, 47, 689–702.
28.
Wen, C.; Dong, W.H.; Xie, W.J.; Cai, M.; Hu, D.X. Autonomous tracking and obstacle avoidance for UAV swarm based on
decoupled MADDPG. Flight Dyn. 2022, 40, 24–31.
29.
Si, P.; Wu, B.; Yang, R.; Li, M.; Sun, Y. UAV Path Planning Based on Multi-Agent Deep Reinforcement Learning. J. Beijing Univ.
Technol. 2023, 49, 449–458.
30.
Galilici, M.; Martin, M.; Masmitja, I. TransfQMix: Transformers for Leveraging the Graph Structure of Multi-Agent Reinforcement
Learning Problems. In Proceedings of the 2023 International Conference on Autonomous Agents and Multiagent Systems
(AAMAS), London, UK, 29 May–2 June 2023; pp. 1–9.
31.
Ragi, S.; Chong, E.K.P. UAV path planning in a dynamic environment via partially observable Markov decision process. IEEE
Trans. Aerosp. Electron. Syst. 2013, 49, 2397–2412. [CrossRef]
32.
Zhang, T.T.; Yang, X.J. Autonomous coordination saturation attacks method for loitering munitions in urban scenarios based on
reinforcement learning. J. Command Control 2023, 9, 457–468.
33.
Wang, L.; Wang, K.; Pan, C.; Xu, W.; Aslam, N.; Hanzo, L. Multi-agent deep reinforcement learning-based trajectory planning for
multi-UAV assisted mobile edge computing. IEEE Trans. Cogn. Commun. Netw. 2020, 7, 73–84. [CrossRef]
34.
Bellman, R. A Markovian decision process. J. Math. Mech. 1957, 6, 679–684. [CrossRef]
35.
Bertsekas, D. Reinforcement Learning and Optimal Control; Athena Scientific: Belmont, MA, USA, 2019.
36.
Yuksek, B.; Demirezen, M.U.; Inalhan, G.; Tsourdos, A. Cooperative planning for an unmanned combat aerial vehicle fleet using
reinforcement learning. J. Aerosp. Inf. Syst. 2021, 18, 739–750. [CrossRef]
37.
Haarnoja, T.; Zhou, A.; Abbeel, P.; Levine, S. Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with
a Stochastic Actor. In Proceedings of the International Conference on Machine Learning, Stockholm, Sweden, 10–15 July 2018;
pp. 1861–1870.
38.
Guo, T.; Jiang, N.; Li, B.; Zhu, X.; Wang, Y.; Du, W. UAV Navigation in High Dynamic Environments: A Deep Reinforcement
Learning Approach. Chin. J. Aeronaut. 2021, 34, 479–489. [CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
