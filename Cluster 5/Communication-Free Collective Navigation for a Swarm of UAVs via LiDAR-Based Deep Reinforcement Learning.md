# Communication-Free Collective Navigation for a Swarm of UAVs via LiDAR-Based Deep Reinforcement Learning.pdf

## Page 1

1
Communication-Free Collective Navigation for a Swarm of UAVs
via LiDAR-Based Deep Reinforcement Learning
Myong-Yol Choi, Hankyoul Ko, Hanse Cho, Changseung Kim, Seunghwan Kim, Jaemin Seo,
and Hyondong Oh
Abstract—This paper presents a deep reinforcement learning
(DRL) based controller for collective navigation of unmanned
aerial vehicle (UAV) swarms in communication-denied envi-
ronments, enabling robust operation in complex, obstacle-rich
environments. Inspired by biological swarms where informed
individuals guide groups without explicit communication, we
employ an implicit leader-follower framework. In this paradigm,
only the leader possesses goal information, while follower UAVs
learn robust policies using only onboard LiDAR sensing, without
requiring any inter-agent communication or leader identification.
Our system utilizes LiDAR point clustering and an extended
Kalman filter for stable neighbor tracking, providing reliable
perception independent of external positioning systems. The core
of our approach is a DRL controller, trained in GPU-accelerated
Nvidia Isaac Sim, that enables followers to learn complex emergent
behaviors—balancing flocking and obstacle avoidance—using only
local perception. This allows the swarm to implicitly follow the
leader while robustly addressing perceptual challenges such as
occlusion and limited field-of-view. The robustness and sim-to-
real transfer of our approach are confirmed through extensive
simulations and challenging real-world experiments with a swarm
of five UAVs, which successfully demonstrated collective navigation
across diverse indoor and outdoor environments without any
communication or external localization.
Index Terms—Multi-robot systems, collective navigation, sensor-
based control, deep reinforcement learning.
I. INTRODUCTION
A. Background and Motivation
U
NMANNED aerial vehicle (UAV) swarms have demon-
strated remarkable potential across diverse applications
including search and rescue, surveillance, environmental moni-
toring, and precision agriculture due to their mobility, flexibility,
and ability to access hard-to-reach areas [1]. By leveraging
the complementary sensing capabilities and spatial coverage of
multiple agents, UAV swarms can accomplish complex missions
that are difficult or impossible for individual UAVs to achieve
efficiently [2]. Collective navigation, where multiple UAVs
This research was supported by Theater Defense Research Center funded
by Defense Acquisition Program Administration under Grant UD200043CD,
National Research Foundation of Korea (NRF) grant funded by the Korea
government (MSIT) (2023R1A2C2003130), and Unmanned Vehicles Core
Technology Research and Development Program through the National Research
Foundation of Korea (NRF) and Unmanned Vehicle Advanced Research Center
(UVARC) funded by the Ministry of Science and ICT, the Republic of Korea
(2020M3C1C1A01082375). (Myong-Yol Choi led the project, and Myong-
Yol Choi and Hankyoul Ko contributed equally to this work.)(Corresponding
author: Hyondong Oh.)
M.-Y. Choi, H. Ko, H. Cho, C. Kim, S. Kim, and J. Seo are with the Department
of Mechanical Engineering, Ulsan National Institute of Science and Technology,
Ulsan, Korea (e-mail: mychoi@unist.ac.kr; kyoul@unist.ac.kr; joahdzl@unist.ac.kr;
pon02124@unist.ac.kr; kevin6960@unist.ac.kr; qkek1019@unist.ac.kr).
H. Oh is with the Department of Mechanical Engineering, Korea Advanced
Institute of Science and Technology, Daejeon, Korea (e-mail: h.oh@kaist.ac.kr).
Fig. 1. An example of real-world validation of the proposed LiDAR-based
collective navigation. (a) A swarm of five UAVs on standby for takeoff. (b)
Trajectories of the swarm reconstructed from onboard LiDAR. (c) Sequential
snapshots of the swarm avoiding obstacles to reach a goal without external
localization or communication. More details can be found in the attached
video at https://youtu.be/U4i3Spisugg.
move together toward common destinations while maintaining
group cohesion, has emerged as a key enabling capability for
these applications [3].
The foundations of collective motion have been extensively
studied across multiple disciplines. Reynolds [4] pioneered
distributed behavioral models using three fundamental rules:
collision avoidance, velocity matching, and flock centering.
Vicsek and Zafeiris [5] later demonstrated that large-scale order
can emerge from a much simpler rule: local velocity matching
with noise. Olfati-Saber [6] provided rigorous mathematical
analysis introducing collective potential functions and α-lattice
structures for multi-agent coordination.
However, real-world deployment of UAV swarms faces
critical challenges in communication-constrained environments.
Inter-UAV communication can become unavailable or unreli-
able due to electronic jamming, signal interference, or natural
disasters [7]. Moreover, even when communication is available,
the bandwidth requirements and latency constraints for large-
scale swarms can limit scalability and real-time coordination [8].
arXiv:2601.13657v1  [cs.RO]  20 Jan 2026

## Page 2

2
In such scenarios, communication-dependent methods become
ineffective, necessitating robust communication-free collective
navigation capabilities that rely solely on onboard perception
and local decision-making.
Biological studies have provided significant insights into
communication-free collective navigation. Berdahl et al. [9]
identified five key mechanisms in animal collective behavior:
the many wrongs principle (averaging individual errors),
leadership (guidance by knowledgeable individuals), emergent
sensing (pooling sensory information), social learning, and
collective learning. Particularly relevant to this work, Couzin
et al. [10] demonstrated that effective group navigation can
emerge from simple local interactions, where a small number
of informed individuals can guide entire groups toward a
destination without explicit communication or identification.
This information asymmetry offers significant practical advan-
tages for UAV swarms: it eliminates the need for mission
broadcasting to all agents, reduces computational overhead,
and enables scenarios where mission updates can only reach a
subset of accessible UAVs. In communication-denied environ-
ments, where distributing goal information to the entire swarm
may be infeasible, this approach becomes essential.
This biological phenomenon directly inspires the implicit
leader-follower framework proposed in this paper. In this
framework, follower UAVs navigate without goal information
or explicit leader identification. Instead, followers learn to
maintain cohesion with neighboring UAVs through local
perception. As the informed leader navigates toward the goal,
the entire swarm naturally moves in that direction through
the followers’ learned cohesion behavior, without requiring
explicit coordination or mission broadcasting. This emergent
coordination eliminates the need for leader identification or
goal information while preserving robust collective navigation.
B. Related Works
1) Communication-Dependent Swarm Navigation: Current
UAV swarm implementations for collective navigation are
broadly categorized into centralized and distributed approaches
based on coordination architectures. Centralized approaches
rely on external infrastructure for global coordination and
precise state estimation. Representative systems include motion
capture-based control such as Crazyswarm [11] and nonlinear
model predictive control [12], which achieve high-precision in-
door navigation in obstacle-known environments by leveraging
ground control stations for agent tracking. While demonstrating
excellent coordination accuracy, their infrastructure dependence
limits applicability to controlled indoor settings and causes
network collapse upon infrastructure failure.
Distributed methods achieve coordination through decen-
tralized decision-making without centralized control, typically
requiring inter-agent communication for state or trajectory shar-
ing. MADER [13] segments trajectory planning into perception,
polyhedral representation, and optimization for multi-agent
coordination. EGO-Swarm [14] employs optimization-based
methods partitioned into mapping, planning, and control mod-
ules, enabling autonomous flight in cluttered forests through
trajectory information sharing. Zhou et al. [15] introduce a
spatial-temporal optimization framework for fully autonomous
UAV swarms navigating dense, unknown environments without
external facilities. V´as´arhelyi et al. [16] demonstrate evolution-
ary optimization for outdoor flocking using GNSS localization
and wireless inter-agent communication. Recent learning-based
approaches include deep reinforcement learning (DRL) for
collision avoidance in fixed-wing UAVs [17] and end-to-end
DRL for quadrotor swarms mapping local observations to motor
thrusts, enabling zero-shot transfer to real robots in obstacle-
dense environments [18]. However, these distributed methods
fundamentally rely on continuous inter-agent communication
for coordination—whether for trajectory sharing or state
information exchange. Additionally, they typically assume
either global mission knowledge across all agents or the ability
to explicitly identify and communicate with informed leaders,
limiting their applicability when communication is infeasible.
2) Perception Strategies for Communication-Free Swarm
Navigation: To enable operation when communication is
unavailable, communication-free approaches employ onboard
sensor-based perception for surrounding UAV detection and au-
tonomous coordination, eliminating inter-agent communication
dependency. Vision-based approaches have been extensively
explored through diverse methodologies. Saska et al. [19]
achieved relative localization using monocular cameras with
circular patterns in GNSS-denied environments. Schilling et
al. [20] utilized six omnidirectional cameras without position
sharing or visual markers, with subsequent work [21] achieving
markerless outdoor flocking with three UAVs. Ahmad et
al. [22] validated PACNav using ultraviolet-based relative
sensing for navigation with four UAVs in natural forests.
Wang et al. [23] implemented a bio-inspired visual projection
field (VPF) approach with six UAVs in controlled indoor
environments.
However, vision-based systems face limitations. First, they
suffer from illumination dependency, with performance de-
grading under varying lighting conditions including sunlight,
shadows, or darkness. Second, monocular vision requires
additional processing or motion to resolve scale ambiguity
in depth estimation. Third, omnidirectional perception re-
quires multiple cameras, critically increasing system com-
plexity through increased onboard computational demands
for processing multiple video streams and complex inter-
camera calibration and synchronization. These factors become
particularly prohibitive for small UAV platforms with limited
computation budgets.
LiDAR-based approaches provide promising alternatives
that directly address these vision-based limitations. Unlike
vision systems, LiDAR offers illumination-invariant perception,
maintaining consistent performance across diverse lighting
conditions. The direct time-of-flight measurements eliminate
depth ambiguity inherent in monocular vision, while a sin-
gle 360-degree scanning LiDAR achieves omnidirectional
awareness without the computational overhead, multi-stream
processing, and complex calibration requirements of multi-
camera systems. These characteristics make LiDAR particularly
suitable for resource-constrained UAV platforms. Recent work
has begun exploring LiDAR for swarm coordination. Swarm-
LIO2 [24] demonstrates a fully decentralized LiDAR-inertial

## Page 3

3
state estimation system for aerial swarms, achieving robust
neighbor detection through reflective tape that produces distinc-
tive high-intensity returns in LiDAR reflectivity measurements.
The system has been validated with five UAVs in real-world
experiments, demonstrating the practicality of LiDAR-based
perception for swarm coordination.
3) Control Strategies for Communication-Free Swarm Navi-
gation: While communication-free perception enables neighbor
detection without information exchange, achieving truly au-
tonomous coordination requires control strategies that make
navigation decisions based purely on local sensory observa-
tions, without communicated state information. This includes
challenges of real-time occlusion handling, limited field-
of-view (FOV), complex swarm interactions, and obstacle
avoidance using only onboard sensor data. Traditional heuristic
methods, such as Reynolds’ principles [4] and potential field-
based obstacle avoidance [6], provide stable flocking without
communication but exhibit limitations. Manually designing
fixed rules that generalize across diverse environmental condi-
tions—including varying obstacle densities, swarm sizes, and
spatial constraints—is extremely challenging. These rule-based
approaches often suffer from local minima where conflicting
objectives trap agents in suboptimal behaviors [6] and cannot
adaptively adjust to dynamic swarm configurations [21]–[23],
often resulting in overly conservative maneuvers.
Learning-based approaches emerged to address these limi-
tations, enabling agents to learn adaptive control policies for
balancing flocking and obstacle avoidance in communication-
free settings. Imitation learning trains UAV policies using expert
demonstrations, partially mitigating heuristic rule rigidity, but is
constrained by the quality and coverage of expert data [20], [25].
Acquiring high-quality demonstration data for communication-
free coordination is inherently challenging, requiring experts
to manually demonstrate complex behaviors under diverse
conditions with partial observability.
DRL offers a powerful alternative, overcoming both heuristic
rule rigidity and imitation learning’s data dependency by
enabling agents to learn policies through direct environmental
interaction. DRL can automatically discover strategies to
balance multiple competing objectives—maintaining cohe-
sion, avoiding collisions, and handling perception uncertain-
ties—through reward-driven optimization, without requiring
explicit rule design or expert demonstrations. Huang et al. [26]
proposed vision-based decentralized collision avoidance using
depth images and DRL for multi-UAV navigation without
inter-UAV communication, but validated only in obstacle-free
simulation environments. Bai et al. [27] extended this for
communication-denied environments with limited visual fields,
but validated in simulations with simplified dynamics and pre-
known obstacles, limiting real-world applicability assessment.
As existing learning-based approaches are mostly validated
in simulations, a critical gap in real-world validation remains,
which this study addresses.
C. Contributions
To overcome these limitations, we propose a novel LiDAR-
based collective navigation system for robust operation in
GNSS-denied and communication-denied environments. Build-
ing upon [24], we eliminate all communication dependencies
by enabling coordination through purely local sensing. Each
UAV uses a single LiDAR sensor for 360-degree neighbor
detection, removing the need for external localization or inter-
agent communication. We employ an implicit leader-follower
architecture where only the leader possesses goal information,
while followers coordinate through learned reactive behaviors.
Follower control policies are trained via DRL using proximal
policy optimization (PPO) [28] to learn flocking and obstacle
avoidance solely from local LiDAR observations. As an on-
policy algorithm, PPO enables synchronous data collection from
multiple UAVs and efficient batch updates in GPU-accelerated
parallel environments. The DRL training enables followers to
autonomously discover control strategies that balance cohesion
with neighbors and collision avoidance with obstacles. Through
this learned flocking behavior, the swarm collectively navigates
to the destination as the leader moves toward the goal, without
requiring explicit leader identification or goal information. The
proposed system is validated through extensive simulations
and real-world experiments involving five UAVs. A sample
result of the real-world experiments is depicted in Fig. 1.
To the best of our knowledge, this is the first LiDAR-based
collective navigation system for a swarm of UAVs using DRL
that operates without any information exchange and has been
validated in real-world deployments. The key contributions are:
i) A fully communication-free, LiDAR-based perception
framework for neighbor detection and tracking to achieve
robust UAV swarm coordination;
ii) A DRL-based control policy that enables implicit leader-
follower coordination by learning to balance flocking and
obstacle avoidance under realistic perception constraints;
and
iii) Comprehensive validation via extensive simulations and
real-world experiments with five UAVs in diverse indoor
and outdoor environments.
II. PROBLEM FORMULATION
A. Problem Definition
This study addresses the collective navigation of a swarm
of N UAVs toward a specific destination in a GNSS-denied
and communication-constrained environment. As illustrated in
Fig. 2, the swarm consists of one informed leader UAV, which
possesses destination information via pre-loaded waypoints,
and N−1 uninformed follower UAVs without such information.
We assume a complete absence of information exchange,
meaning each UAV cannot explicitly distinguish whether other
UAVs are leaders or followers, requiring an implicit leader-
follower framework. Each follower must utilize its onboard
LiDAR sensors to perceive its surroundings in real-time,
making autonomous decisions based only on locally observed
information. The core challenge is for the swarm to maintain
cohesion and effectively avoid obstacles, moving collectively
toward the destination without dispersing, while addressing
perceptual challenges such as occlusion and limited FOV.

## Page 4

4
Fig. 2. Scenario of the communication-free collective navigation problem.
A leader visits a known waypoint sequence, while followers, unaware of the
goal or leader’s identity, use only local perception for flocking and obstacle
avoidance to indirectly follow the leader.
B. System Models
The state of each UAV i is its local position pi
t ∈R3, velocity
vi
t ∈R3, and orientation (quaternion qi
t ∈R4) at time t. Each
UAV i has a LiDAR sensor providing a raw point cloud zi
t of its
surroundings, which feeds into a perception module (Sec. III-A).
From this data, UAV i’s state (pi
t, vi
t, qi
t) is estimated by
LiDAR-inertial odometry (LIO). Concurrently, the perception
module processes zi
t to detect and track neighbors N i
t and
obstacles Oi
t.
While all UAVs share the same kinematic model for position
updates,
pi
t+1 = pi
t + vi
t∆t,
their control policies for determining velocity commands differ
by role.
The leader’s velocity is determined by a local planner L
using its estimated state, perceived obstacles, and predefined
waypoints W:
vl
t+1 = L(pl
t, ql
t, Ol
t, W).
Each follower learns a control policy π, detailed in Sec. III-B,
that generates velocity commands based only on its estimated
state and local perception of neighbors and obstacles:
vf
t+1 = π(vf
t , qf
t , N f
t , Of
t ).
The follower’s policy π intentionally excludes position pf
t as
an input, even though it is available from LIO. This design is
critical for learning a generalizable policy. Including pf
t could
cause the policy to learn correlations between coordinates
within the locally generated map and required control actions.
Such map-dependent policies would fail in novel environments
with different trajectories and layouts. By restricting input
to the UAV’s kinematic state—velocity vf
t and orientation
qf
t —along with local perception of neighbors N f
t and obstacles
Of
t , the policy learns a robust, egocentric strategy based on
immediate kinematic state and surroundings rather than position
relative to an arbitrary starting point, significantly enhancing
transferability.
C. Flocking Considerations for Implicit Following
Flocking refers to coordinated collective motion emerging
when individual agents follow simple local interaction rules [4].
Traditional flocking behaviors consist of three fundamental
rules: cohesion for staying close to neighboring UAVs, sepa-
ration for maintaining safe distances to avoid collisions with
neighbors, and alignment for matching velocity directions with
neighbors.
However, we deliberately exclude the alignment term
from our flocking behavior. This design choice is crucial
for our communication-free implicit leader-follower scenario,
where followers cannot identify the leader and the leader
may exhibit diverse motion patterns—including hovering,
directional changes, or backward movement—depending on
mission objectives and obstacle configurations. Incorporating
velocity alignment would cause followers to align with the
average velocity direction of all perceived neighbors rather
than specifically following the leader’s directional changes.
Since followers cannot distinguish the leader, when the leader
suddenly changes direction to navigate toward a new location,
followers maintaining alignment with neighbors’ average
velocity would dilute the leader’s influence, potentially causing
loss of the leader and mission failure. Therefore, our flocking
behavior incorporates only cohesion and separation, allowing
followers to navigate collectively while being responsive to
the leader’s positional changes rather than being constrained
by the swarm’s average velocity direction.
D. Objectives
The primary objective of this study is to develop a robust
control policy, π, trained via DRL. Using only onboard LiDAR
data, this policy must enable followers to learn a balance
between two types of local behaviors: flocking (cohesion and
separation) and obstacle avoidance. The successful execution
of these behaviors results in the emergent behavior of implicit
leader-following, where the swarm naturally moves toward
the destination as followers maintain positional cohesion
with neighbors, which in turn are influenced by the leader’s
goal-directed motion. Ultimately, the system aims to achieve
collective movement in a fully communication-free manner.
III. METHODOLOGY
To address the problem defined in Sec. II, the proposed
system is built upon a decentralized control architecture
where each UAV independently perceives its environment and
makes decisions. This architecture is composed of two core
modules: a LiDAR-based perception system (Fig. 3) that detects
neighboring UAVs and obstacles in real-time, and a DRL
control policy (Fig. 4) that learns to balance the competing
demands of flocking and obstacle avoidance. The perception
system generates local observations that are fed as an input to
the control policy, which in turn outputs velocity commands.
The integration of these modules enables the emergent behavior
of stable collective navigation, allowing the entire swarm to
reach a target destination known only to the leader, without
explicit communication or reliance on an external positioning
system.
A. LiDAR-Based Perception System
The proposed LiDAR-based perception pipeline consists
of three main components: (1) a LIO module for ego-state
estimation, (2) an object tracker module for neighbor detection

## Page 5

5
Fig. 3. Overview of the onboard perception system. (a) The perception pipeline. (b) The object tracker filters raw LiDAR points, clusters them using DBSCAN,
tracks them with an EKF, and validates them based on temporal consistency.
and tracking, and (3) a point downsampling module that
transforms the raw point cloud into low-dimensional features
for computational efficiency. The resulting perception outputs
are fed into the neural network. Each UAV is equipped with
reflective tape to produce high-intensity LiDAR returns, crucial
for detection. Based on the high-intensity returns, the object
tracker operates in three stages with all geometry computed
in the local map frame: filtering, clustering/tracking, and
validation.
1) Point Cloud Filtering: The first stage filters the raw
point cloud of each UAV i, zi
t, as shown in Fig. 3(b)-1. To
improve point density, we stack the most recent B point clouds.
Each point bp is transformed into the map frame using the
transformation mp = Tm←b bp, where Tm←b is obtained from
the LIO module and subsequently gated by its Euclidean
distance to the UAV position, retaining only points within
range [dmin, dmax].
The resulting distance-gated points, Pd, are filtered based
on two criteria. First, we identify high-intensity points Phigh.
Since reflective tape provides high-intensity returns, points with
intensity I greater than or equal to threshold Ihigh are utilized
as key seeds to detect new objects.
Phigh = { p ∈Pd | I ≥Ihigh }.
Second, we retain region of interest (ROI) points Proi to
maintain tracks during temporary occlusions. From remaining
low-intensity points Plow, we select those within radius rroi of
existing track centroids mˆcj.
Proi = { p ∈Plow | min
j
∥mp −mˆcj∥2 ≤rroi}.
Finally, the union Pfiltered = Phigh ∪Proi is passed to the next
stage as shown in Fig. 3(b)-2.
TABLE I
PARAMETERS FOR THE LIDAR-BASED PERCEPTION SYSTEM
Parameter
Value
Description
Point Cloud Filtering
B
2
Number of stacked point clouds
dmin
0.05m
Minimum distance for point gating
dmax
10.0m
Maximum distance for point gating
Ihigh
170
Threshold for LiDAR intensity (0–255) for highly
reflective points
rroi
0.3m
ROI radius around existing tracks
Clustering and Tracking
ε
0.1m
Distance threshold for DBSCAN clustering
nmin
8B
Minimum points per cluster (scaled by stacked
frames)
dmatch
0.2m
Association threshold for matching clusters to tracks
tinactive
0.5s
Timeout for deactivating unobserved tracks
Cluster Validation
ρhigh
0.05
High-intensity ratio threshold for validation
τon
0.01s
Continuous duration for validation
2) Clustering and Tracking: The filtered point set Pfiltered
is grouped into individual clusters Ck using the density-
based spatial clustering of applications with noise (DBSCAN)
algorithm [29], which forms clusters based on a distance
threshold ε defining the maximum allowable distance between
points and a minimum number of points nmin. Since point
density decreases with distance, we apply distance-adaptive
validation where the minimum point threshold scales with
range. Each cluster is tracked using the extended Kalman
filter (EKF) [30] with a constant velocity model to estimate
smooth motion trajectories of neighboring UAVs, as depicted
in Fig. 3(b)-3. Data association matches each valid cluster to
the nearest existing track if their distance is below threshold
dmatch. An associated track is updated via EKF, and a new
track is created for a new cluster. A track is deactivated if
unobserved for timeout tinactive.

## Page 6

6
Fig. 4. The proposed DRL architecture. An encoder processes observations into a latent vector, and actor and critic heads use it to determine the policy and
estimate value.
3) Cluster Validation: The final stage validates if a tracked
object is a reliable neighbor UAV as shown in Fig. 3(b)-4. A
track is confirmed as a reliable neighbor if the ratio of high-
intensity points within its cluster exceeds threshold ρhigh for
continuous duration τon. The set of all validated neighbors at
time t constitutes the perception output Nt, used by the control
policy.
B. Deep Reinforcement Learning Framework
The follower UAVs learn a decentralized control policy
using a DRL framework, as illustrated in Fig. 4. We model the
follower’s control problem as a partially observable Markov
decision process (POMDP), formally defined by the 7-tuple
(S, A, T , R, Ω, O, γ), where S is the state space, A is the
action space, T : S × A × S →[0, 1] is the state transition
function, R : S × A →R is the reward function, Ωis the
observation space, O : S →Ωis the observation function,
and γ ∈[0, 1] is the discount factor. In our model-free DRL
approach, the agent does not explicitly know S, T , or O.
Instead, it learns an optimal policy π : Ω→A through direct
interaction with the environment, relying on observations ot ∈
Ω, actions at ∈A, and rewards rt ∈R sampled from R.
1) Observation and Action Spaces: The agent’s observation
ot ∈Ωat time step t is a composite input vector designed for
decentralized control, comprising: (1) a 7-D ego-state vector
(3-D velocity and 4-D quaternion) for self-motion awareness,
(2) a 42-D vector encoding the relative states of up to six
neighbors, and (3) a two-channel H × W occupancy grid
derived from LiDAR data for spatial understanding of obstacles,
where H = 72 and W = 12 correspond to the horizontal and
vertical resolution of the downsampled point cloud.
For neighbor representation, we select up to six nearest
neighbors visible within the LiDAR’s FOV, accounting for
occlusions that may temporarily hide agents. Each neighbor is
encoded as a 7-D vector containing relative position, relative
velocity, and a binary mask. The use of a fixed number of
observable neighbors is a topological approach inspired by
robust collective behaviors in animal swarms [31]. The selection
of six neighbors balances performance and computational
load, empirically verified in Sec. IV-E. When fewer than six
neighbors are detected due to occlusions or limited vertical
FOV, zero-padding and binary masks maintain a fixed input
size while indicating the presence or absence of valid neighbor
information.
The occupancy grid’s first channel contains proximity
information, representing distance to the nearest obstacle in
each cell, while the second channel provides a binary mask
indicating cell occupancy. Based on this observation, the
agent generates an action at ∈A, a continuous 3-D vector
representing the desired velocity command v ∈R3.
2) Reward Function: The reward function R is a multi-
objective sum designed to encourage complex emergent behav-
iors, with total reward:
rtotal = rflock + robstacle + rstable + rperception + rcollision.
The flocking reward balances separation from nearby agents
and cohesion with the flock’s center of mass:
rflock = wflock(rseparation + rcohesion),
where rseparation penalizes violating a safety distance, and
rcohesion penalizes straying from the flock’s center.
rseparation = −
X
j∈N i
dsep −∥pi −pj∥2
dsep −2ruav

I∥pi−pj∥2<dsep,
rcohesion = −
∥pi −pcom∥2 −dcoh

I∥pi−pcom∥2>dcoh.
Here, pi is the UAV’s position, pj is the neighbor’s position,
pcom is the center of mass, dsep and dcoh are distance thresholds,
ruav is the UAV radius, and I is the indicator function.
The obstacle avoidance reward penalizes obstacle proximity
and approach:
robstacle = wobstacle(rproximity + rdirection),

## Page 7

7
Fig. 5. Illustration of reward function components for learning communication-
free collective navigation. (a) Flocking: cohesion encourages staying close to
neighbors, while separation maintains safe distances. (b) Obstacle avoidance:
proximity penalizes closeness to obstacles, and direction penalizes movement
toward obstacles. (c) Stable flight: altitude maintenance encourages following
the leader’s altitude, and attitude stability promotes upright orientation. (d)
Neighbor perception: visibility rewards keeping neighbors within FOV, recovery
triggers descent when all neighbors are lost.
where rproximity penalizes distance to the nearest obstacle, and
rdirection penalizes moving towards obstacles.
rproximity = −
dprox −mink(dk
obs)
dprox −ruav
4
Imink dk
obs<dprox,
rdirection = −
X
k
max(0, dprox −dk
obs)∥vi∥2I|θk|<θthreshold.
Here, k indexes the individual obstacle points observed by
the LiDAR; dk
obs is the distance to the k-th point, and θk is
the angle between the UAV’s velocity and the ray to the k-th
obstacle point. dprox and θthreshold are defined as the proximity
and angle thresholds used for obstacle avoidance.
The stable flight reward is:
rstable = wstable(raltitude + rattitude),
including raltitude for altitude maintenance and rattitude for
attitude stability.
raltitude = exp
 
−
hi −hl
α
2!
,
rattitude = exp
 
−
uz −1
β
2!
.
Here, hi is the UAV’s altitude, hl is the leader’s altitude, and
uz is the z-component of the UAV’s up-vector. Parameters α
and β control sensitivity.
The neighbor perception reward encourages maintaining
awareness of neighboring UAVs:
rperception = wperception(rvisibility + rrecovery),
composed of rvisibility for keeping neighbors within FOV by
minimizing occlusion and rrecovery for descent when no neigh-
bors are detected. This descent acts as a recovery maneuver to
re-acquire neighbors that may have fallen out of the limited
vertical FOV.
rvisibility =
|N i
perceived|
|N i|
,
rrecovery = −|hi −hrecovery|IN i
perceived=0.
TABLE II
PARAMETERS FOR THE REWARD FUNCTION
Parameter
Value
Description
Reward Weights
wflock
1.5
Weight for the flocking reward
wobstacle
2.0
Weight for the obstacle avoidance reward
wstable
1.0
Weight for the stable flight reward
waware
1.0
Weight for the situational awareness reward
Flocking
dsep
1.6m
Safety distance for separation
dcoh
2.0m
Cohesion distance threshold from center of mass
ruav
0.2m
Radius of the UAV
Obstacle Avoidance
dprox
3.0m
Proximity threshold for obstacles
θthreshold
20◦
Angle threshold for direction penalty
Stable Flight
α
0.1
Scaling parameter for altitude reward
β
0.1
Scaling parameter for attitude reward
Situational Awareness
hrecovery
1.0 m
Target altitude for emergency descent
Here, N i
perceived is the set of neighbors detected by LiDAR
accounting for occlusions and limited FOV, and hrecovery is the
target descent altitude.
Finally, the collision penalty is a sparse negative reward
applied upon any collision event and triggers episode termina-
tion:
rcollision = −10Icollision.
A collision event is triggered if the distance between centers
of any two UAVs becomes less than 2ruav, or the distance
between a UAV’s center and an obstacle point becomes less
than ruav.
3) Network Architecture and Training: Our control policy is
implemented as an actor-critic network, illustrated in Fig. 4. The
network consists of a shared encoder processing observations,
followed by actor and critic heads. The entire policy is trained
end-to-end using the PPO algorithm [28].
The two-channel 72×12 LiDAR occupancy grid is processed
by a convolutional neural network (CNN). The resulting feature
map is flattened and passed through a fully-connected layer
to produce a 256-D feature vector, which is concatenated
with the 7-D ego-state vector and 42-D neighbor-state vector.
The combined feature vector is passed through a multi-layer
perceptron (MLP), outputting a final 512-D shared feature
vector. The shared vector is consumed by two separate heads.
The actor head is an MLP with a hidden layer of 256 units
that outputs the mean and standard deviation for a continuous
Gaussian policy. The critic head is a similar MLP outputting a
single scalar representing the value function.
The training process consists of two core stages: advantage
estimation, followed by policy and value function optimization.
To evaluate how much better a specific action is compared
with the average action in a given state, we use an advantage
function,
ˆAt. We apply generalized advantage estimation
(GAE) [32], which computes advantages based on the temporal
difference (TD) error, δt:
δt = Rt + γVϕ(ot+1) −Vϕ(ot),
(1)
where Rt is the reward, Vϕ is the value estimated by the
critic network, and γ is the discount factor. GAE calculates

## Page 8

8
Fig. 6. Simulation environments. (a) The cluttered training environment with spawn area at the map center and goal point randomly sampled on a circle of
30m radius centered at the spawn region. (b) and (c) show unseen test environments for evaluating generalization.
the advantage as an exponentially-weighted sum of these TD
errors:
ˆAGAE(γ,λ)
t
=
T −t−1
X
l=0
(γλ)lδt+l,
(2)
where λ ∈[0, 1] controls the bias-variance trade-off. The
resulting advantages ˆAt are normalized to zero mean and
unit variance before policy optimization.
The policy and value networks are optimized jointly by
minimizing a total loss function:
L(θ, ϕ) = ˆEt[−LCLIP(θ) + c1LVF(ϕ) −c2H[πθ](ot)],
(3)
where c1 and c2 are hyperparameters weighting the differ-
ent terms. The primary component is the clipped surrogate
objective:
LCLIP(θ) = ˆEt
h
min

rt(θ) ˆAt, clip(rt(θ), 1 −ϵ, 1 + ϵ) ˆAt
i
.
(4)
Here, rt(θ) =
πθ(at|ot)
πθold(at|ot) is the probability ratio between
current and old policies. This clipping mechanism is the core
of PPO’s stability, discouraging overly large policy updates.
The second component, the value function loss LVF, reduces
the variance of advantage estimates. The value network
minimizes the error between its prediction Vϕ(ot) and the
value target V targ
t
, computed using value estimates from the
network used during data collection:
V targ
t
= ˆAt + Vϕold(ot).
(5)
This loss is the squared error:
LVF(ϕ) = (Vϕ(ot) −V targ
t
)2.
(6)
Finally, an entropy bonus H[πθ](ot) encourages exploration,
where H is the entropy of the policy’s action distribution:
H[πθ](ot) = Ea∼πθ[−log πθ(a|ot)].
(7)
Key hyperparameters are set to ϵ = 0.1, c1 = 1.0, c2 = 0.001,
γ = 0.99, λ = 0.95, using the Adam optimizer with learning
rates of 1 × 10−3 for the encoder, actor, and critic.
IV. SIMULATIONS
A. Simulation Setup
We trained and evaluated our DRL policy in Nvidia Isaac Sim
using the OmniDrones [33] framework for GPU-accelerated
parallel simulations. Each training simulation instance featured
a swarm of five UAVs, comprising one leader and four
followers, navigating an environment with randomly placed
pillars as shown in Fig. 6(a).
1) Environment Configuration: At the beginning of each
training episode, the swarm was spawned in an obstacle-free
region at the map center, with UAVs randomly positioned on a
3 × 3 grid with 1.6m spacing to ensure safe initial separation.
The goal point was randomly sampled on a 30m radius circle
centered at the spawn region. To enhance policy robustness
and generalization, we randomized initial UAV orientations,
the leader’s speed, and goal location for each episode.
Training was conducted across 512 parallel environments for
500 million timesteps, leveraging GPU acceleration (Nvidia
RTX 4090 and Intel i9-14900K) for efficient data collection and
policy updates. Each episode terminated under four conditions:
(1) collision between UAVs, (2) collision between a UAV and
obstacle, (3) flying below minimum allowable altitude, and
(4) flying above maximum allowable altitude, ensuring the
policy learns to maintain swarm cohesion, avoid collisions, and
preserve stable flight within operational constraints.
2) Leader Navigation: The leader UAV utilized a planner
combining the rapidly-exploring random tree (RRT) [34] with
the artificial potential field (APF) [35] for real-time navigation.
RRT generates a local path toward the waypoint to prevent
APF from falling into local minima. Then, APF computes
an attractive force toward the RRT-generated path direction
and repulsive forces from nearby obstacles detected by the
360-degree LiDAR. The final velocity command is obtained
by combining these APF forces, enabling the UAV to follow
the RRT path while maintaining safe distances from obstacles.
This integration allows smooth and safe navigation in unknown
environments.
3) Perception Modeling: While our physical system uses
reflective tape for neighbor detection, in simulation we ab-
stracted this process using the simulator’s ground-truth data to
identify neighbors. This abstraction allowed us to focus training
on the control policy while incorporating key perceptual
challenges based on our hardware’s empirical characteristics:
(1) estimation errors in relative neighbor states with Gaussian
distributions (relative position: σpos = 0.02m, relative velocity:
σvel = 0.05m/s), (2) limited FOV identical to the physical
sensor (−7◦to 52◦vertical), (3) occlusions calculated based
on physical UAV dimensions, and (4) processing latency
reflecting actual onboard computation. Latency was determined
by measuring end-to-end delay on the onboard computer,
from sensor data acquisition through our perception pipeline
to policy input generation. To ensure temporal consistency,
data synchronization introduces delays of 0.1s for ego state
and LiDAR data for obstacles, and 0.2s for relative neighbor
information.

## Page 9

9
B. Evaluation Metrics
To quantitatively evaluate the proposed policy, six metrics
were defined: success rate (SR), mission progress (MP), flock
radius (FR), minimum separation (MS), alignment (AL), and
minimum distance to obstacles (MDO). All results represent
mean and standard deviation from 100 independent trials per
scenario.
1) Success Rate (SR): The percentage of trials where all
UAVs successfully followed the leader to the destination
without collisions, serving as the primary indicator of mis-
sion completion. Evaluation terminates when: (1) UAV-UAV
collision, (2) UAV-obstacle collision, (3) flying below/above
altitude limits, or (4) complete leader loss from all followers’
perception. SR is defined as
SR = Nsuccessful trials
Ntrials
× 100.
2) Mission Progress (MP): The ratio of distance advanced
toward the destination relative to total distance from start to
destination, averaged over all trials. This evaluates navigation
effectiveness and if collective behavior enables consistent
forward progress. Let the leader’s starting position be Pstart,
goal position be Pgoal, and position at trial k end be P k
end. MP
is calculated as:
MP =
1
Ntrials
Ntrials
X
k=1
" 
1 −∥P k
end −Pgoal∥2
∥Pstart −Pgoal∥2

× 100
#
.
3) Flock Radius (FR): The maximum flock extent, defined as
distance from swarm center to farthest UAV, averaged over the
episode and trials. Compact formation ensures agents remain
within perceptual range. Larger FR indicates fragmentation
risks. For N UAVs, let pi,k
t
be position of UAV i at time t in
trial k and pc,k
t
= 1
N
PN
j=1 pj,k
t
be the center. Let Tk denote
episode length of trial k. FR is calculated by
FR =
1
Ntrials
Ntrials
X
k=1
"
1
Tk
Tk
X
t=1
max
i=1,...,N ∥pi,k
t
−pc,k
t ∥2
#
.
4) Minimum Separation (MS): A safety metric evaluating
collision avoidance between agents, defined as minimum
distance between the closest UAV pair, averaged over episode
and trials. Adequate separation is fundamental to safe collective
navigation.
MS =
1
Ntrials
Ntrials
X
k=1
"
1
Tk
Tk
X
t=1
min
i̸=j ∥pi,k
t
−pj,k
t ∥2
#
.
5) Alignment (AL): A metric measuring directional con-
sistency, averaged over episode and trials. High AL indicates
coherent swarm movement. It is the average cosine similarity
between each UAV’s velocity vi,k
t
and swarm average velocity
vavg,k
t
=
1
N
PN
j=1 vj,k
t . Values near 1 indicate well-aligned
formation.
AL =
1
Ntrials
Ntrials
X
k=1
"
1
Tk
Tk
X
t=1
1
N
N
X
i=1
vi,k
t
· vavg,k
t
∥vi,k
t ∥2∥vavg,k
t
∥2
#
.
6) Minimum Distance to Obstacles (MDO): A safety metric
evaluating obstacle avoidance, defined as minimum distance
between any UAV and any obstacle detection point, averaged
over episode and trials. This measures safety margins main-
tained during navigation. Let om,k
t
denote position of the m-th
LiDAR detection point among M total points:
MDO =
1
Ntrials
Ntrials
X
k=1
"
1
Tk
Tk
X
t=1
min
i=1,...,N
m=1,...,M
∥pi,k
t
−om,k
t
∥2
#
.
C. Performance Comparison
To demonstrate the superiority and practical applicability of
the proposed method, we conducted comparative evaluations
against baseline methods satisfying two critical criteria: compat-
ibility with real-world deployment on physical UAV platforms
with actual sensor constraints and demonstrated effectiveness
in communication-free collective navigation scenarios.
1) Baseline Methods: Our baseline selection comprises three
representative approaches meeting these criteria. The first two
are heuristic-based methods validated in real-world experiments.
PACNav [22] is a bio-inspired distributed control method
enabling collective navigation without GNSS or inter-UAV
communication by introducing two metrics: path persistence
(measuring how consistently a UAV flies straight) and path
similarity (measuring directional consistency among neighbors).
Uninformed UAVs identify reliable leaders by selecting neigh-
bors exhibiting high path persistence and similarity, enabling
emergent collective navigation toward unknown destinations.
The method incorporates reactive collision avoidance for
environmental obstacles and inter-UAV conflicts, validated
with four UAVs in natural forests.
The second baseline employs a bio-inspired VPF [23],
which mimics avian visual perception for communication-free
flocking. Instead of exchanging state information, each UAV
uses VPF to observe neighbors and obstacles, distinguishing
between repulsion zones (objects appearing large) and attraction
zones (objects appearing small) based on perceived size. This
enables the three fundamental flocking behaviors—separation,
attraction, and velocity alignment—without inter-UAV commu-
nication. The approach incorporates an implicit heterogeneous
flocking framework, where a small minority of informed UAVs
guide the uninformed majority through emergent collective
behavior, with uninformed agents following the swarm’s overall
motion without explicitly identifying leaders. The method has
been validated with six UAVs in indoor environments with
obstacles, where a motion capture system was installed.
For the learning-based baseline, the DAgger approach [25]
trains an end-to-end visuomotor controller by imitating an
expert policy combining modified Reynolds’ flocking rules
with APF-based obstacle avoidance. The expert policy, which
has access to ground-truth state information in simulation,
generates optimal control commands that the student policy
learns to replicate using only onboard camera images and
IMU data. Through centralized training and decentralized
execution, the learned policy achieves vision-only cooperative
flight without GNSS or inter-UAV communication. While
validated exclusively in high-fidelity Gazebo simulations with

## Page 10

10
TABLE III
PERFORMANCE COMPARISON WITH BASELINE METHODS
Metric
Method
No obstacles
Training environment
Test environment
Cluttered pillars
Simplified forest
Forest
Min. obstacle gap
10m
5m
5m
5m
SR (%)
PACNav [22]
100.0±0.0
96.0±0.0
82.0±0.0
38.0±0.0
31.0±0.0
VPF [23]
100.0±0.0
80.0±0.0
27.0±0.0
6.0±0.0
5.0±0.0
DAgger [25]
100.0±0.0
93.0±0.0
69.0±0.0
34.0±0.0
22.0±0.0
Proposed
100.0±0.0
99.0±0.0
97.0±0.0
97.0±0.0
72.0±0.0
MP (%)
PACNav [22]
100.0±0.0
98.6±8.8
93.0±18.6
72.2±26.6
67.6±28.2
VPF [23]
100.0±0.0
92.6±17.5
62.0±32.3
47.0±24.4
39.7±22.7
DAgger [25]
100.0±0.0
97.1±11.4
85.6±25.4
74.5±25.9
69.1±24.0
Proposed
100.0±0.0
99.3±7.0
99.5±3.3
98.2±10.4
88.2±23.6
FR (m)
PACNav [22]
1.80±0.14
1.83±0.12
1.85±0.10
1.85±0.10
1.82±0.10
VPF [23]
2.20±0.44
2.23±0.55
2.54±1.57
2.44±1.44
2.31±0.79
DAgger [25]
2.96±0.44
2.85±0.44
2.65±0.37
2.59±0.56
2.59±0.46
Proposed
1.61±0.13
1.56±0.12
1.47±0.09
1.40±0.06
1.39±0.15
MS (m)
PACNav [22]
1.23±0.07
1.25±0.06
1.26±0.06
1.27±0.04
1.25±0.05
VPF [23]
1.49±0.03
1.48±0.04
1.48±0.05
1.46±0.05
1.47±0.06
DAgger [25]
1.54±0.11
1.53±0.11
1.51±0.11
1.49±0.13
1.49±0.13
Proposed
1.55±0.02
1.53±0.02
1.51±0.02
1.47±0.03
1.46±0.04
AL
PACNav [22]
0.87±0.08
0.83±0.08
0.79±0.07
0.73±0.05
0.75±0.06
VPF [23]
0.92±0.03
0.92±0.04
0.89±0.06
0.89±0.05
0.87±0.09
DAgger [25]
0.79±0.02
0.77±0.03
0.74±0.04
0.67±0.04
0.68±0.05
Proposed
0.94±0.01
0.94±0.01
0.93±0.02
0.90±0.02
0.88±0.11
MDO (m)
PACNav [22]
-
2.18±0.33
1.89±0.40
0.82±0.45
0.82±0.32
VPF [23]
-
2.12±0.41
1.81±0.57
1.27±0.45
0.73±0.45
DAgger [25]
-
1.89±0.40
1.52±0.54
0.93±0.58
0.76±0.41
Proposed
-
2.27±0.15
1.88±0.16
1.56±0.09
0.79±0.32
complex scenarios (pillar forests, narrow gaps), the method
demonstrates superior learning efficiency and performance
compared with other learning algorithms (MADDPG [17],
SAC [27], and MAGAIL [36]). For our comparison, we directly
implemented the expert policy itself rather than retraining the
imitation learning policy. This design ensures fair comparison
by eliminating approximation error from imitation learning,
evaluating the fundamental control strategy rather than policy
distillation quality, providing an upper bound on DAgger
method’s performance.
2) Fair Comparison Setup: For fair comparison, we uni-
fied all methods to use identical LiDAR-based perception
(same FOV, range, occlusion handling) while preserving each
method’s control strategy. Parameters were independently
tuned to achieve similar flocking behavior in obstacle-free
environments, ensuring equivalent baseline capability before
testing in complex scenarios.
3) Evaluation Environments: Comparative evaluation was
conducted with five UAVs (one leader and four followers) in
various environments to verify generalization performance and
robustness. First, evaluations were performed in the training
environment with three obstacle density levels: none, sparse
with minimum 10m gap, and dense with minimum 5m gap.
Two new test environments were introduced: a simplified forest
with irregularly distributed trees and rocks, and a more realistic
complex forest featuring trees and rocks with detailed trunks
and foliage as shown in Fig. 6(b) and (c).
4) Results and Analysis: As shown in Table III, the proposed
DRL method consistently outperforms all baselines, with
Fig. 7. Example trajectory of the proposed policy in the forest test environment
with multiple waypoints. The swarm of five UAVs successfully navigates
through dense obstacles by following the leader while maintaining cohesion.
The leader sequentially visits four waypoints to reach the goal.
performance gaps widening in complex environments. All
methods succeed without obstacles, but degrade sharply in
cluttered scenarios (5–31% success in realistic forests), whereas
our policy maintains 72% success and 88.2% mission progress.

## Page 11

11
TABLE IV
SCALABILITY ANALYSIS OF THE PROPOSED DRL POLICY WITH VARYING NUMBERS OF FOLLOWER UAVS
Metric
Min. obstacle gap
Number of followers
2
4
6
8
10
SR (%)
No obstacles
100.0±0.0
100.0±0.0
100.0±0.0
98.0±0.0
93.0±0.0
10m
100.0±0.0
99.0±0.0
96.0±0.0
84.0±0.0
70.0±0.0
5m
93.0±0.0
97.0±0.0
88.0±0.0
56.0±0.0
46.0±0.0
MP (%)
No obstacles
100.0±0.0
100.0±0.0
100.0±0.0
99.2±7.5
95.3±18.2
10m
100.0±0.0
99.3±7.0
97.7±12.8
91.7±21.9
88.5±23.4
5m
98.0±9.7
99.5±3.3
96.8±10.2
79.6±22.9
70.3±27.6
FR (m)
No obstacles
1.13±0.18
1.61±0.13
1.93±0.06
2.15±0.06
2.32±0.05
10m
1.08±0.15
1.56±0.12
1.88±0.06
2.14±0.06
2.33±0.06
5m
1.04±0.13
1.47±0.09
1.85±0.05
2.12±0.05
2.32±0.07
MS (m)
No obstacles
1.60±0.01
1.55±0.02
1.47±0.03
1.39±0.02
1.34±0.02
10m
1.60±0.01
1.53±0.02
1.46±0.03
1.38±0.02
1.34±0.02
5m
1.60±0.01
1.51±0.02
1.44±0.03
1.37±0.02
1.32±0.03
AL
No obstacles
0.97±0.02
0.94±0.01
0.89±0.02
0.85±0.02
0.84±0.04
10m
0.97±0.02
0.94±0.01
0.89±0.02
0.85±0.02
0.84±0.03
5m
0.97±0.02
0.93±0.02
0.88±0.02
0.84±0.03
0.83±0.04
MDO (m)
No obstacles
-
-
-
-
-
10m
2.45±0.13
2.27±0.15
2.17±0.18
2.00±0.24
1.68±0.29
5m
2.12±0.21
1.88±0.16
1.65±0.29
1.49±0.37
1.35±0.45
The proposed method achieves the most compact flock (smallest
radius) and organized formation (highest alignment) while
maintaining safe separation and obstacle distances, effectively
balancing task completion, cohesion, and collision avoidance.
Beyond quantitative evaluation with single goal points, Fig. 7
demonstrates the proposed policy’s versatility in handling
sequential waypoint navigation. The swarm successfully follows
the leader through four waypoints in the forest test environment,
maintaining cohesion and obstacle avoidance. This capability
naturally emerges from the learned flocking behavior and
obstacle avoidance, as followers implicitly follow the leader
regardless of waypoint number or configuration.
D. Scalability Analysis
To evaluate the scalability of the proposed DRL policy, a
single model trained with five UAVs (one leader and four
followers) was tested by varying the number of followers from
two to ten. Table IV illustrates performance variation with
respect to follower count and environmental complexity.
Success rate and mission progress decreased with increasing
swarm size and environmental complexity, with significant
degradation when eight or more followers navigated narrow
gaps. This decline stems from a geometric constraint: the policy
maintains similar altitudes for reliable neighbor detection within
LiDAR’s limited vertical FOV (−7◦to 52◦), causing horizontal
rather than vertical formation expansion. With 10 followers,
the flock radius reaches 2.32m (total diameter 4.6m), making
navigation through 5m gaps physically challenging. This tight
margin between swarm size and obstacle spacing causes high
failure rates in large-scale swarms.
Flock radius increased with swarm size regardless of envi-
ronment, while minimum separation and alignment decreased.
Reduced separation implies higher collision risk, and decreased
alignment reveals a key limitation of decentralized control:
difficulty achieving directional consensus in large swarms
without communication. The policy demonstrates moderate
scalability but degrades due to geometric constraints, suggesting
that robust large-scale application requires policies that better
utilize three-dimensional space.
E. Ablation Studies
1) Effect of Reward Components: We validated each reward
term by systematically removing components and evaluating six
configurations: (1) without flocking reward, (2) without obstacle
avoidance, (3) without stable flight, (4) without neighbor
perception, (5) uniform weights, and (6) proposed method
with tuned weights. Each was trained for 500 million timesteps
and tested across three obstacle densities.
As shown in Table V, removing flocking reward completely
destroys collective navigation (0% success), with followers
hovering at initial positions while the leader moves away.
Without cohesion incentives, followers cannot establish leader-
following behavior, demonstrating this reward is fundamentally
essential for implicit coordination in communication-free
settings.
Removing obstacle avoidance shows minor degradation in
simple environments (96% success rate) but drops to 86%
in dense scenarios, indicating explicit guidance significantly
improves robustness despite some learning through collision
penalties. The stable flight reward proves critical—its removal
causes catastrophic failure (11%, 9%, and 3% success rates) as
followers drift in altitude, losing neighbors outside LiDAR’s
limited FOV (−7◦to 52◦), with increased flock radius (2.94m
to 3.60m) and erratic flight patterns. This highlights altitude
consistency as prerequisite for effective coordination with
limited FOV sensors.
The
neighbor
perception
reward
shows
environment-
dependent importance, with minimal impact in simple scenarios
(99% and 96%) but significant drops to 67% in dense envi-
ronments, suggesting visibility mechanisms become critical

## Page 12

12
TABLE V
ABLATION STUDY OF REWARD COMPONENTS ACROSS ENVIRONMENTS WITH VARYING OBSTACLE DENSITIES
Metric
Min. obstacle gap
Configuration
w/o rflocking
w/o robstacle
w/o rstable
w/o rperception
Uniform
Proposed
SR (%)
No obstacles
0.0±0.0
96.0±0.0
11.0±0.0
99.0±0.0
82.0±0.0
100.0±0.0
10m
0.0±0.0
96.0±0.0
9.0±0.0
96.0±0.0
74.0±0.0
99.0±0.0
5m
0.0±0.0
86.0±0.0
3.0±0.0
67.0±0.0
54.0±0.0
97.0±0.0
MS (%)
No obstacles
-
97.8±11.8
28.0±39.8
99.2±8.5
92.6±20.9
100.0±0.0
10m
-
99.2±5.8
32.5±39.0
98.9±6.4
92.0±22.6
99.3±7.0
5m
-
94.2±16.3
35.7±29.3
81.3±30.3
80.0±32.5
99.5±3.3
FR (m)
No obstacles
-
2.02±0.11
3.60±0.87
2.29±0.15
2.85±0.26
1.61±0.13
10m
-
2.03±0.10
3.35±0.79
2.26±0.14
2.86±0.25
1.56±0.12
5m
-
2.00±0.09
2.94±0.78
2.23±0.14
2.83±0.29
1.47±0.09
MS (m)
No obstacles
-
1.58±0.02
1.55±0.05
1.53±0.04
1.42±0.07
1.55±0.02
10m
-
1.58±0.01
1.55±0.04
1.52±0.03
1.40±0.06
1.53±0.02
5m
-
1.57±0.02
1.55±0.04
1.50±0.04
1.38±0.05
1.51±0.02
AL
No obstacles
-
0.94±0.02
0.90±0.04
0.94±0.01
0.95±0.02
0.94±0.01
10m
-
0.94±0.01
0.90±0.04
0.94±0.01
0.94±0.02
0.94±0.01
5m
-
0.94±0.02
0.90±0.04
0.92±0.03
0.93±0.03
0.93±0.02
MDO (m)
No obstacles
-
-
-
-
-
-
10m
-
2.25±0.18
2.22±0.17
2.41±0.15
2.36±0.14
2.27±0.15
5m
-
1.66±0.26
1.86±0.30
1.82±0.27
1.74±0.20
1.88±0.16
as occlusion increases. Uniform weights achieve moderate
performance (82%, 74%, and 54%) but consistently under-
perform the proposed method (100%, 99%, and 97%). These
results validate each component’s distinct role: flocking enables
leader-following, obstacle avoidance ensures safety, stable flight
maintains controllability, and perception enhances robustness,
with tuned weights effectively balancing these competing
objectives.
2) Effect of Observable Neighbors: To determine the ap-
propriate number of observable neighbors, we performed an
ablation study using eleven UAVs (one leader and ten followers)
across environments with varying complexity. The results,
shown in Fig. 8, indicate a clear trend: while increasing
the number of neighbors generally improves success rate,
performance gains diminish after a certain point.
In the obstacle-free environment, success rate saturated at
94% with only four neighbors, showing no further improvement
with additional information. In more challenging environments
with obstacles, a larger number of neighbors proved beneficial,
though a noticeable slowdown in performance gains was
observed. For instance, in the dense obstacles environment
(5m spacing), increasing observable neighbors from five to
six yielded a substantial 20% increase in success rate (from
26% to 46%). In contrast, further increasing from six to ten
provided only a marginal 4% gain (from 46% to 50%), after
which performance showed no significant improvement.
This analysis reveals that |N| = 6 is a critical threshold
capturing the majority of performance benefits from situational
awareness, particularly in complex scenarios. Beyond this
number, marginal gains in success rate are outweighed by
increased computational cost. Specifically, each additional
neighbor contributes new data points, and the computational
load of the object tracker, which scales quadratically (O(n2))
with the number of points n, becomes a significant bottleneck
on onboard embedded systems. Therefore, setting observable
neighbors to six provides balance, ensuring high performance
Fig. 8.
An effect of observable neighbors on success rate in collective
navigation.
across various environments without imposing unnecessary
computational burdens on the agents.
V. EXPERIMENTS
A. System Overview
We used custom 250 mm quadrotors equipped with a Livox
Mid-360 LiDAR, an Nvidia Jetson Orin NX, and a Pixhawk
6C flight controller as shown in Fig. 9. To ensure the UAV is
detectable from any angle, reflective tape was affixed to all sides
of its body. All computation, including FAST-LIO2 [37] for ego-
pose estimation, an object tracker for neighbor detection and
tracking, point downsampling, and neural network inference,
was performed onboard.
B. Performance of LiDAR-based detection
We evaluated the LiDAR-based detection performance under
various conditions. The number of LiDAR returns decreases
inversely with the square of the distance, and beyond approxi-
mately 10 m the low point density prevented reliable detection
for our UAV size. In addition, the reflective tape’s intensity

## Page 13

13
Fig. 9. Hardware and system overview. (a) A custom quadrotor equipped with a LiDAR, onboard computer, and reflective tape. (b) The onboard software
architecture, showing the flow from sensor data to actuator commands.
Fig. 10. Real-world validation in indoor environments. (a), (e) Experimental setups for cluttered blocks and wall. (b), (f) Corresponding swarm trajectories
visualizing the flock radius. (c), (g) Minimum separation and (d), (h) Minimum distance to obstacles over time, respectively.
drops sharply at incident angles greater than about 45 degrees,
leading to missed detections due to insufficient intensity. To
address these limitations, reflective tape was affixed to all sides
of the UAV.
Detection rate is defined as the proportion of instances in
which a UAV present in the scene is successfully detected by
the LiDAR and precision represents the proportion of LiDAR
detections that correspond to actual UAVs. Excluding cases
where neighboring UAVs were outside the LiDAR’s FOV, our
experiments demonstrated a detection rate of 100% and a
precision of 99.2%, measured as the ratio of correctly detected
instances across all time steps.
C. Experimental Results
To validate the sim-to-real transfer, we conducted experi-
ments in controlled indoor and unstructured outdoor environ-
ments, with results in Fig. 10, Fig. 11, and Table VI. The
results presented for each environment were obtained from a

## Page 14

14
Fig. 11. Real-world validation in outdoor environments. (a), (e), (i) Experimental setups for pillars, display tower, and short forest. (b), (f), (j) Corresponding
swarm trajectories visualizing the flock radius. (c), (g), (k) Minimum separation and (d), (h), (l) Minimum distance to obstacles over time, respectively.
single trial, where the reported metrics represent the temporal
mean and standard deviation over the entire episode length.
The successful sim-to-real transfer of our policy was clearly
demonstrated in diverse real-world environments. In indoor
trials, the swarm successfully navigated cluttered obstacles
while maintaining robust cohesion and separation. The low
alignment scores observed were a direct result of confined
space, which necessitated frequent maneuvering for collision
avoidance. Both the minimum separation between agents and
minimum distance to obstacles consistently remained above
the collision distance threshold throughout all experiments,
ensuring safe navigation without any collisions. Meanwhile,
in outdoor scenarios with unpredictable variables such as
wind and varying lighting conditions, the swarm demonstrated
robust performance with these safety margins maintained
across diverse obstacle configurations. The short forest scenario
presented the most challenging obstacle avoidance conditions
due to its dense vegetation, yet the policy successfully main-
tained collision-free navigation. The higher alignment scores
in open areas suggest the policy adaptively transitions to a

## Page 15

15
TABLE VI
REAL-WORLD EXPERIMENT RESULTS WITH FIVE UAVS
Metric
Indoor environments
Outdoor environments
Cluttered blocks
Wall
Pillars
Display tower
Short forest
FR (m)
2.31±0.28
2.54±0.28
2.86±0.53
2.60±0.27
2.30±0.30
MS (m)
1.50±0.28
1.39±0.36
1.34±0.34
1.55±0.16
1.36±0.27
AL
0.48±0.40
0.52±0.42
0.72±0.34
0.81±0.21
0.74±0.30
MDO (m)
1.88±0.92
4.25±1.45
2.82±1.83
5.82±4.69
1.57±1.13
more organized and efficient formation when space allows.
Collectively, these results validate that the single policy exhibits
excellent generalization and robustness under complex and
various real-world conditions.
VI. CONCLUSIONS
This paper introduced a fully communication-free system for
collective UAV swarm navigation using a single LiDAR and a
DRL policy. Our implicit leader-follower framework, enabled
by a robust perception pipeline and a learned controller, allows
a swarm to perform complex navigation in communication-
denied environments. We rigorously validated our approach
through extensive simulations and challenging real-world
experiments. The DRL-based policy outperformed existing
methods in simulation and demonstrated successful sim-to-real
transfer, with a five-UAV swarm navigating diverse indoor and
outdoor environments. This study validated the practicality and
robustness of using DRL for communication-free collective
navigation.
Future work will focus on enhancing scalability to larger
swarms and exploring more complex collective behaviors like
adaptive role-switching.
AUTHOR CONTRIBUTIONS
Myong-Yol Choi: Conceptualization, project administration,
investigation, methodology, software, validation, data curation,
formal analysis, visualization, and writing—original draft.
Hankyoul Ko: Investigation, software, validation, data curation,
formal analysis, and visualization. Hanse Cho: Investigation,
data curation, and formal analysis. Changseung Kim, Seungh-
wan Kim, and Jaemin Seo: Investigation. Hyondong Oh: Su-
pervision, funding acquisition, resources, and writing—review
and editing.
REFERENCES
[1] D. Floreano and R. J. Wood, “Science, technology and the future of
small autonomous drones,” Nature, vol. 521, no. 7553, pp. 460–466,
2015.
[2] Y. Alqudsi and M. Makaraci, “UAV swarms: research, challenges, and
future directions,” Journal of Engineering and Applied Science, vol. 72,
no. 1, p. 12, 2025.
[3] M. Dorigo, G. Theraulaz, and V. Trianni, “Reflections on the future of
swarm robotics,” Science robotics, vol. 5, no. 49, pp. 1–3, 2020.
[4] C. W. Reynolds, “Flocks, herds and schools: A distributed behavioral
model,” in Proc. 14th Annual Conference on Computer Graphics and
Interactive Techniques, 1987, pp. 25–34.
[5] T. Vicsek and A. Zafeiris, “Collective motion,” Physics Reports, vol.
517, no. 3-4, pp. 71–140, 2012.
[6] R. Olfati-Saber, “Flocking for multi-agent dynamic systems: Algorithms
and theory,” IEEE Transactions on Automatic Control, vol. 51, no. 3, pp.
401–420, 2006.
[7] M. Coppola, K. N. McGuire, C. De Wagter, and G. C. De Croon, “A
survey on swarming with micro air vehicles: Fundamental challenges
and constraints,” Frontiers in Robotics and AI, vol. 7, p. 18, 2020.
[8] W. Chen, J. Liu, H. Guo, and N. Kato, “Toward robust and intelligent
drone swarm: Challenges and future directions,” IEEE Network, vol. 34,
no. 4, pp. 278–283, 2020.
[9] A. M. Berdahl, A. B. Kao, A. Flack, P. A. Westley, E. A. Codling,
I. D. Couzin, A. I. Dell, and D. Biro, “Collective animal navigation
and migratory culture: From theoretical models to empirical evidence,”
Philosophical Transactions of the Royal Society B: Biological Sciences,
vol. 373, no. 1746, p. 20170009, 2018.
[10] I. D. Couzin, J. Krause, N. R. Franks, and S. A. Levin, “Effective
leadership and decision-making in animal groups on the move,” Nature,
vol. 433, no. 7025, pp. 513–516, 2005.
[11] J. A. Preiss, W. Honig, G. S. Sukhatme, and N. Ayanian, “Crazyswarm:
A large nano-quadcopter swarm,” in Proc. IEEE International Conference
on Robotics and Automation, 2017, pp. 3299–3304.
[12] E. Soria, F. Schiano, and D. Floreano, “Predictive control of aerial
swarms in cluttered environments,” Nature Machine Intelligence, vol. 3,
no. 6, pp. 545–554, 2021.
[13] J. Tordesillas and J. P. How, “Mader: Trajectory planner in multiagent
and dynamic environments,” IEEE Transactions on Robotics, vol. 38,
no. 1, pp. 463–476, 2021.
[14] X. Zhou, J. Zhu, H. Zhou, C. Xu, and F. Gao, “Ego-swarm: A fully
autonomous and decentralized quadrotor swarm system in cluttered
environments,” in 2021 IEEE international conference on robotics and
automation, 2021, pp. 4101–4107.
[15] X. Zhou, X. Wen, Z. Wang, Y. Gao, H. Li, Q. Wang, T. Yang, H. Lu,
Y. Cao, and C. Xu, “Swarm of micro flying robots in the wild,” Science
Robotics, vol. 7, no. 66, pp. 1–18, 2022.
[16] G. V´as´arhelyi, C. Vir´agh, G. Somorjai, T. Nepusz, A. E. Eiben, and
T. Vicsek, “Optimized flocking of autonomous drones in confined
environments,” Science Robotics, vol. 3, no. 20, pp. 1–13, 2018.
[17] C. Yan, C. Wang, X. Xiang, K. H. Low, X. Wang, X. Xu, and
L. Shen, “Collision-avoiding flocking with multiple fixed-wing UAVs
in obstacle-cluttered environments: A task-specific curriculum-based
MADRL approach,” IEEE Transactions on Neural Networks and Learning
Systems, vol. 35, no. 8, pp. 10 894–10 908, 2023.
[18] Z. Huang, Z. Yang, R. Krupani, B. S¸enbas¸lar, S. Batra, and G. S.
Sukhatme, “Collision avoidance and navigation for a quadrotor swarm us-
ing end-to-end deep reinforcement learning,” in 2024 IEEE International
Conference on Robotics and Automation, 2024, pp. 300–306.
[19] M. Saska, T. Baca, J. Thomas, J. Chudoba, L. Preucil, T. Krajnik,
J. Faigl, G. Loianno, and V. Kumar, “System for deployment of groups
of unmanned micro aerial vehicles in GPS-denied environments using
onboard visual relative localization,” Autonomous Robots, vol. 41, pp.
919–944, 2017.
[20] F. Schilling, J. Lecoeur, F. Schiano, and D. Floreano, “Learning
vision-based flight in drone swarms by imitation,” IEEE Robotics and
Automation Letters, vol. 4, no. 4, pp. 4523–4530, 2019.
[21] F. Schilling, F. Schiano, and D. Floreano, “Vision-based drone flocking
in outdoor environments,” IEEE Robotics and Automation Letters, vol. 6,
no. 2, pp. 2954–2961, 2021.
[22] A. Ahmad, D. B. Licea, G. Silano, T. B´aˇca, and M. Saska, “Pacnav: A
collective navigation approach for UAV swarms deprived of communica-
tion and external localization,” Bioinspiration & Biomimetics, vol. 17,
no. 6, p. 066019, 2022.
[23] F. Wang, J. Huang, K. H. Low, and T. Hu, “Collective navigation of
aerial vehicle swarms: A flocking inspired approach,” IEEE Transactions
on Intelligent Vehicles, vol. 9, no. 1, pp. 1040–1053, 2023.
[24] F. Zhu, Y. Ren, L. Yin, F. Kong, Q. Liu, R. Xue, W. Liu, Y. Cai,
G. Lu, and H. Li, “Swarm-LIO2: Decentralized, efficient LiDAR-inertial
odometry for UAV swarms,” IEEE Transactions on Robotics, vol. 41,
pp. 960–981, 2024.

## Page 16

16
[25] Y. Wan, J. Tang, Z. Zhao, and X. Chen, “Distributed vision-only cooper-
ative flight of multiple quadrotors in unknown cramped environments,”
IEEE Transactions on Intelligent Vehicles, vol. 10, no. 7, pp. 3902–3915,
2024.
[26] H. Huang, G. Zhu, Z. Fan, H. Zhai, Y. Cai, Z. Shi, Z. Dong, and
Z. Hao, “Vision-based distributed multi-UAV collision avoidance via deep
reinforcement learning for navigation,” in 2022 IEEE/RSJ International
Conference on Intelligent Robots and Systems, 2022, pp. 13 745–13 752.
[27] C. Bai, P. Yan, H. Piao, W. Pan, and J. Guo, “Learning-based multi-UAV
flocking control with limited visual field and instinctive repulsion,” IEEE
Transactions on Cybernetics, vol. 54, no. 1, pp. 462–475, 2023.
[28] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, “Prox-
imal policy optimization algorithms,” arXiv preprint arXiv:1707.06347,
2017.
[29] M. Ester, H.-P. Kriegel, J. Sander, and X. Xu, “A density-based algorithm
for discovering clusters in large spatial databases with noise,” in Proc.
2nd International Conference on Knowledge Discovery and Data Mining,
1996, pp. 226–231.
[30] R. E. Kalman, “A new approach to linear filtering and prediction
problems,” Journal of Basic Engineering, vol. 82, no. 1, pp. 35–45,
1960.
[31] M. Ballerini, N. Cabibbo, R. Candelier, A. Cavagna, E. Cisbani,
I. Giardina, V. Lecomte, A. Orlandi, G. Parisi, A. Procaccini et al.,
“Interaction ruling animal collective behavior depends on topological
rather than metric distance: Evidence from a field study,” Proceedings
of the National Academy of Sciences, vol. 105, no. 4, pp. 1232–1237,
2008.
[32] J. Schulman, P. Moritz, S. Levine, M. Jordan, and P. Abbeel, “High-
dimensional continuous control using generalized advantage estimation,”
arXiv preprint arXiv:1506.02438, 2015.
[33] B. Xu, F. Gao, C. Yu, R. Zhang, Y. Wu, and Y. Wang, “Omnidrones: An
efficient and flexible platform for reinforcement learning in drone control,”
IEEE Robotics and Automation Letters, vol. 9, no. 3, pp. 2838–2844,
2024.
[34] S. LaValle, “Rapidly-exploring random trees: A new tool for path
planning,” Research Report 9811, 1998.
[35] O. Khatib, “Real-time obstacle avoidance for manipulators and mobile
robots,” The International Journal of Robotics Research, vol. 5, no. 1,
pp. 90–98, 1986.
[36] Z. Fang, D. Jiang, J. Huang, C. Cheng, Q. Sha, B. He, and G. Li,
“Autonomous underwater vehicle formation control and obstacle avoidance
using multi-agent generative adversarial imitation learning,” Ocean
Engineering, vol. 262, p. 112182, 2022.
[37] W. Xu, Y. Cai, D. He, J. Lin, and F. Zhang, “FAST-LIO2: Fast direct
LiDAR-inertial odometry,” IEEE Transactions on Robotics, vol. 38, no. 4,
pp. 2053–2073, 2022.
Myong-Yol Choi is currently a Ph.D. candidate at
the Department of Mechanical Engineering, Ulsan
National Institute of Science and Technology, Ulsan,
Republic of Korea. He received a B.S. degree in
Mechanical and Aerospace Engineering from Ulsan
National Institute of Science and Technology, Ulsan,
Republic of Korea, in 2022. His research focuses on
learning-based collective behaviors for autonomous
swarms of unmanned vehicles.
Hankyoul Ko is currently an undergraduate student
at the Department of Mechanical Engineering, Ulsan
National Institute of Science and Technology, Ulsan,
Republic of Korea. His research focuses on unmanned
aerial vehicles, sensor fusion for localization, and
robotic perception.
Hanse Cho is currently a M.S. student at the
Department of Mechanical Engineering, Ulsan Na-
tional Institute of Science and Technology, Ulsan,
Republic of Korea. He received a B.S. degree in
Mechanical and Control Engineering from Handong
Global University, Pohang, Republic of Korea, in
2024. His research focuses on flocking and swarm
control.
Changseung Kim is currently a Ph.D. candidate at
the Department of Mechanical Engineering, Ulsan
National Institute of Science and Technology, Ulsan,
Republic of Korea. He received a B.S. degree in Me-
chanical Engineering from Inha University, Incheon,
Republic of Korea, in 2021. His research focuses
on multi-sensor fusion simultaneous localization and
mapping.
Seunghwan Kim is currently a Ph.D. candidate at
the Department of Mechanical Engineering, Ulsan
National Institute of Science and Technology, Ulsan,
Republic of Korea. He received a B.S. degree in Me-
chanical Engineering from Inha University, Incheon,
Republic of Korea, in 2021. His research focuses
on environmental monitoring, active perception, and
autonomous exploration.
Jaemin Seo is currently a Ph.D. candidate at the De-
partment of Mechanical Engineering, Ulsan National
Institute of Science and Technology, Ulsan, Republic
of Korea. He received a B.S. degree in Aerospace
Engineering from Pusan National University, Busan,
Republic of Korea, in 2019. His research focuses on
environmental monitoring, informative path planning,
and cooperative search strategy.
Hyondong Oh is currently an Associate Professor
at the Department of Mechanical Engineering, Ko-
rea Advanced Institute of Science and Technology,
Daejeon, Republic of Korea. He received his B.S.
and M.S. degrees in Aerospace Engineering from
Korea Advanced Institute of Science and Technology,
Daejeon, Republic of Korea, in 2004 and 2010,
respectively, and a Ph.D. in Aerospace Engineering
from Cranfield University, Cranfield, United King-
dom, in 2013. He was a Postdoctoral Researcher at
the University of Surrey, Guildford, United Kingdom,
from 2013 to 2014, an Assistant Professor at Loughborough University,
Loughborough, United Kingdom, from 2014 to 2016, and an Associate
Professor at the Ulsan National Institute of Science and Technology, Ulsan,
Republic of Korea, from 2016 to 2025. His research interests include decision
making for unmanned vehicles, cooperative control, path planning, nonlinear
guidance and control, and sensor/information fusion.
